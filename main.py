from fastapi import FastAPI
import uvicorn
import tensorflow
from tensorflow.keras.utils import get_file, load_img, img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.nn import softmax
from tensorflow import expand_dims
import numpy as np
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import sessionlocal, engine, Base
import model
import os

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


ML_model = load_model(os.path.abspath('mnist_model.h5'))

prediction_classes = np.array(['0','1','2','3','4','5','6','7','8','9'])

@app.get('/')
def base(db:Session = Depends(get_db)):
    return db.query(model.row).all()

@app.post('/prediction')
def prediction(image_url: str = '', db:Session = Depends(get_db) ):
    if image_url == '':
        return {'attention': 'No link provided'}
    else:

        #checking if the link is already in the db
        result = db.query(model.row).filter(model.row.url == image_url).first()
        if result:
            return {'prediction' : result.prediction}
        # handling exceptions with the provided link
        try:
            image_path = get_file(origin=image_url)
        except Exception as e:
            print(e)



    # Preprocessing of the saved image
        img = image.load_img(image_path, grayscale=True, target_size= (28,28))
        img_array = image.img_to_array(img)
        img_array = expand_dims(img_array, axis= 0)
        normalized_image_data = img_array / np.max(img_array)
    # Prediction
        prediction = ML_model.predict(normalized_image_data)
        score = prediction[0]
        class_prediction = prediction_classes[tensorflow.argmax(score)]

    # Adding the row to the database and returning the endpoint request
        row = model.row()
        row.url = image_url
        row.prediction = class_prediction
        db.add(row)
        db.commit()

        return {'prediction': class_prediction}



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


