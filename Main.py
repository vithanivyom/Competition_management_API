import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    HOST = os.getenv("FASTAPI_HOST")
    PORT = os.getenv("FASTAPI_PORT")
    uvicorn.run("Project_1.app:app", host= HOST , port= int(PORT) , reload= True)
