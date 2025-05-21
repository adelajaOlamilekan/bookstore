from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse
import shutil
import os
from pathlib import Path

router = APIRouter()

@router.post("/uploadfile")
async def upload_file(
  file: UploadFile = File(...)
):
  
  #create directory in project base directory 
  upload_directory = Path("upload")
  Path.mkdir(upload_directory, exist_ok=True)

  #write the file to disk
  with open(Path.joinpath(upload_directory, file.filename), "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  return {"filename": file.filename}

@router.get("/downloadfile/filename", response_class=FileResponse)
async def download_file(filename: str): 
  filepath = Path(f"upload/{filename}")
  # print(Path("upload").exists(), Path(__name__).parents[0].joinpath("/uploads"))
  if not filepath.exists():
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail= f"File {filename} not found"
    )
  
  return FileResponse(path=f"upload/{filename}", filename=filename)