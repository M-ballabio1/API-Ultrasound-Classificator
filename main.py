from fastapi import FastAPI, File,  Request
from fastapi.openapi.utils import get_openapi
from utils.prediction_mobile_net import prediction_ml, read_image, resize_imagefile

description = """
**Mobile-Net classificator implemented in Tensorflow** and if you want to interact with API using a UI, go to Streamlit application.

This API is created for scientific purpose to support explaination of scientific paper about MLOps.
The goal was the deployment of deep learning model in production using the best practice of MLOps science.

### Author and Contributors:

- Matteo Ballabio (author)

- Matteo Testi (contributor)

### Usage:

- Input: ultrasound image (suggested 224x224x1)

- Output: json file with classification probability

### Limit Usage:

There's a fix limit to HTTPs API's requests (each Ip address can send 5 https request for day)

"""


app = FastAPI(
    title="Mobile-Net - Ultrasound Image classification",
    description=description,
    version="1.0", 
    contact={
        "name": "Matteo Ballabio",
        "email": "matteoballabio99@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mobile-Net - Ultrasound Image classification 🚀",
        version="1.0",
        description=description,
        contact={
        "name": "Matteo Ballabio",
        "email": "matteoballabio99@gmail.com"},
        license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"},
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.post("/classification")
def get_classification(request: Request, file: bytes = File(...)):
    """Get classification class from image file"""
    image=read_image(file)
    image2=resize_imagefile(image)
    class_image = prediction_ml(image2)
    return (class_image)
