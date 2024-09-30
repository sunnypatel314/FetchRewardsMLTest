# Fetch Rewards Machine Learning Assessment

This web app allows us to perform an inference procedure on a machine learning model to predict the number of total receipts scanned for any month in 2022. The model was trained on data (receipt counts) from 2021. 

## Assumptions/Notes (Please read before evaluating)
- This model is suppose to predict the number of scanned receipts for each MONTH in the year 2022 (as per the instructions); this means there are only 12 possible inputs you can give for inference (one for each month in 2022).
- A little knowledge of Docker is required to follow these instructions.
- If you get a warning about a potentially malicious 'model.pt' file, please ignore it. The warning is just saying that the file could have something other than the model weights inside. This is absolutely true because it also has the scaler parameters, but nothing malicious.

## Requirements
- Fast/Easy Setup with Docker:
    - [Docker](https://www.docker.com/products/docker-desktop/) (Docker allows consistency across all machines by running lightweight containers)
- Slow/Manual Setup with Python:
    - [Python](https://www.python.org/downloads/) (If you can, I recommend downloading Anaconda and using their base environment, but any Python 3.7 and up will do)

## Running with Docker (Fast/Easy Setup)
- Clone this repository:
  ```
  git clone https://github.com/sunnypatel314/FetchRewardsMLTest.git
  ```
- Enter the clone repository's working directory:
  ```
  cd FetchRewardsMLTest
  ```
- Run the Docker engine and keep it running in the background (assuming you have Docker installed at this point).
- Build the Docker image by running this in the root of the working directory (it might take a little while for the image to build):
  ```
  docker build -t receipts_predictor .
  ```
- Run the image you have just built:
  ```
  docker run -p 8000:8000 receipts_predictor
  ```
- Port 8000 should be ready for your HTTP requests.

## Running with Python (Slow/Manual Setup)
- Clone this repository:
  ```
  git clone https://github.com/sunnypatel314/FetchRewardsMLTest.git
  ```
- Enter the clone repository's working directory:
  ```
  cd FetchRewardsMLTest
  ```
- **Optional** Create and activate a virtual environment:
    - Create the environment:
        ```
        python -m venv <my_env_name>
        ```
    - Activate the environment:
        - If you are on Windows:
            ```
            .\<my_env_name>\Scripts\activate
            ```
        - If you are on Mac or Linux:
            ```
            source <my_env_name>/bin/activate
            ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Start Flask server:
  ```
  python app.py
  ```
- Port 8000 should be ready for your HTTP requests.


## API Endpoints

I recommend using Postman for the API calls; that is what I will be showing in the documentation.
Make sure you have selected the 'raw' radio button under the 'Body' tab and the data type for the requests is JSON.
![image](https://github.com/user-attachments/assets/59384a21-136c-45db-99e7-3995d58fef68)

Please keep your Postman data clean. Do not leave comments in the request body when sending requests. In my experience, this leads to weird behavior and errors.
In other words, do not do something like this:
![image](https://github.com/user-attachments/assets/175eb6cd-6e94-49cf-a84a-d763706d0760)

#### POST "/predict" - Predict number of scanned receipts for given month
- Request: 
  ```
  {
    "month<str>": "March" // case insensitive and must be a valid month
  }
  ```
  or
  ```
  {
    "month<str>": "3" // must be a valid month number (1-12)
  }
  ```
- Response:
   - Successful:
       - **Status Code 200 (OK)** if the model successfully made a prediction.
   - Unsuccessful:
       - **Status Code 400 (Bad request)** if request includes an invalid data type or you are missing the field 'month'.

**Note about model training**: 
If you want to train this model yourself, then you can download the python notebook in the ./notebooks folder and run it in Jupyter Notebook. 

## Thank you!
- I just wanted to say thank you for evaluating my assessment.
