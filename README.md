# API-Ultrasound-Classificator 🩺

## Details

This project is an API classifier built using a deep learning architecture. It allows you to classify various types of data with high accuracy. You can interact with the application through a user-friendly Streamlit app. Check out the live demo at [App Classifier](https://m-ballabio1-web-app-classificator-main-0ebnyd.streamlit.app/). The code and detailed documentation can be found in this repository.

### VERSION V1▶️
This is the workflow and pipeline utilized in version 1 of this API. The process involves multiple steps, including data collection, preprocessing, feature engineering, model training, validation, and deployment. Each stage is carefully orchestrated to ensure the seamless functioning of the API, delivering efficient and accurate results to users.

![mlops_pipeline_versione1](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/b78b7379-8c3a-45ae-966a-117b50e09525)

This is the screenshot of web application used a default client of this api.

![web_app_st](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/769b3d16-886a-41d8-8321-eb8038a2a488)

[**Live Demo App:** [App Classifier](https://m-ballabio1-web-app-classificator-main-0ebnyd.streamlit.app/)]

## Repository

The code and detailed documentation can be found in this [GitHub repository](https://github.com/M-ballabio1/API-Ultrasound-Classificator).

## Features

- FastAPI with deep learning model of classification
- Hosting API and monitoring access using Render.com
- Deep learning architecture for accurate classification
- User-friendly interface powered by Streamlit

## Usage

1. Install the required dependencies.
2. Clone the repository.
3. Run the Streamlit app.
4. Upload your data for classification.
5. View the classification results.

For more detailed instructions, refer to the documentation in the repository.

Other usage on: [**Live Demo App:** [App Classifier](https://m-ballabio1-web-app-classificator-main-0ebnyd.streamlit.app/)

Image 1: Interaction using Streamlit UI.

## Interaction with the API:

POST: https://api-ultrasound-image-classificator.onrender.com/classification
- Input: images (png or jpg)
- Output: json string (str with odds of classification in each classes)

![Render-API](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/1b8312d0-d331-4419-9593-87b14a78337c)
Image 2: Render platform to monitor Https requests sent.

### VERSION 2▶️
This is the workflow and pipeline utilized in version 2 of this API. The process involves multiple steps, including data collection, preprocessing, feature engineering, model training, validation, and deployment. Each stage is carefully orchestrated to ensure the seamless functioning of the API, delivering efficient and accurate results to users. There are different approach based on automatization of process using Github actions, push in DockerHub and GCS and deploy on Cloud Run (GCP).

![mlops_pipeline_versione2](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/1046e090-38d2-4c3b-9bc4-d32415f97e98)

This is the screenshot of web application used a default client of this api.

![web_app_st](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/769b3d16-886a-41d8-8321-eb8038a2a488)

[**Live Demo App:** [App Classifier](https://m-ballabio1-web-app-classificator-main-0ebnyd.streamlit.app/)]

## Repository

The code and detailed documentation can be found in this [GitHub repository](https://github.com/M-ballabio1/API-Ultrasound-Classificator).

## Features

- Automatically detection of changes in repository and push in Docker Hub, Google Cloud Registry and deploy in Cloud Run.
- FastAPI with deep learning model of classification
- Hosting API and monitoring access using Cloud Run (GCP)
- Deep learning architecture for accurate classification
- User-friendly interface powered by Streamlit

## Usage

1. Install the required dependencies.
2. Clone the repository.
3. Run the Streamlit app.
4. Upload your data for classification.
5. View the classification results.

For more detailed instructions, refer to the documentation in the repository.

Other usage on: [**Live Demo App:** [App Classifier](https://m-ballabio1-web-app-classificator-main-0ebnyd.streamlit.app/)

Image 1: Interaction using Streamlit UI.

## Interaction with the API:

POST: https://api-ultrasound-classificator-cloud-run-pa6vji5wfa-ew.a.run.app/classification
- Input: images (png or jpg)
- Output: json string (str with odds of classification in each classes)

![cloud_run_api](https://github.com/M-ballabio1/API-Ultrasound-Classificator/assets/78934727/9ecad8c1-2890-4a5b-bd30-8fa2d7f708dd)

Image 2: Cloud Run Api

## Feedback and Contributions

Feel free to provide any feedback or suggestions by creating an issue in the repository. Contributions are also welcome!

## License


