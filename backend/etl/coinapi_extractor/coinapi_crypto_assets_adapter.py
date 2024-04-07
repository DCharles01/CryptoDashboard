from prefect import flow, task, Flow
import pandas as pd
import boto3
import requests
import json
import datetime
from prefect.deployments.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

bucket_name = 'crypto-coinapi'
s3_key = 'assets/'
path = f"data/{datetime.datetime.today().strftime('%Y-%m-%d')}_crypto_assets.json"




@task
def extract_assets_from_coin_api(url: str) -> dict:
    response = requests.get(url)

    assert response.status_code == 200

    return response.json()


@task
def save_json_locally(data: dict):
    file_path = path
    with open(file_path, 'w') as f:
        json.dump(data, f)

    print('Done saving data to json')

@task
def save_to_s3_bucket(file_path: str, s3_bucket: str, s3_key: str) -> None:

    # Specify the local file path of the file you want to upload
    file_path = path

    # Upload the file to S3
    s3 = boto3.client('s3')
    s3.upload_file(file_path, s3_bucket, s3_key)

    print("File uploaded successfully!")


@flow
def extract_save_upload_to_s3():

    try:
        # Attempt to create the directory
        if not os.path.exists('data'):
            os.makedirs('data')
    except Exception as e:
        # Handle any exceptions that occur during directory creation
        print(f"An error occurred while creating the directory: {e}")
    else:
        # If no exceptions occurred, print success message
        print(f"Directory '{directory_path}' created successfully.")

    data = extract_assets_from_coin_api("http://api.coincap.io/v2/assets")

    save_json_locally(data)

    save_to_s3_bucket(path, bucket_name, s3_key + path.split('/')[-1])




if __name__ == "__main__":
    deployment = Deployment.build_from_flow(
        name="crypto_assets",
        flow=extract_save_upload_to_s3,
        version=1,
        schedule=CronSchedule(cron="* * * * *", timezone="America/New_York"),
        is_schedule_active=True,
        work_queue_name="default",
        entrypoint="./coinapi_crypto_assets_adapter.py:extract_save_upload_to_s3",
    )
    deployment.apply(upload=True)

# extract_save_upload_to_s3()




