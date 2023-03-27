from minio import Minio
import os

if __name__ == "__main__":

    FILE = "PATH"
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    MINIO_API_HOST = "http://localhost:9000"
    MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
    found = MINIO_CLIENT.bucket_exists("minioteste")
    if not found:
       MINIO_CLIENT.make_bucket("minioteste")
    else:
       print("Bucket already exists")

    MINIO_CLIENT.fput_object("minioteste", "img_teste.jpeg", FILE)
    print("It is successfully uploaded to bucket")