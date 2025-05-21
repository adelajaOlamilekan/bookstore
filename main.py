from fastapi import FastAPI, HTTPException, Request, status, Response, Depends
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
import json
import author_route, book_route, user_route
from uploads_and_downloads.uploads import upload_router
from exceptions import ValueExceptionError
# from sql_example.database import SesssionLocal, User
from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(author_route.router)
app.include_router(book_route.router)
app.include_router(user_route.router)
app.include_router(upload_router.router)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
  request: Request,
  exc: RequestValidationError
):
  return PlainTextResponse("This is a plain text response"
                           f"\n {json.dumps(exc.errors(), indent=2)}",
                           status_code=status.HTTP_400_BAD_REQUEST)
  
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc:HTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={
      "message": "Oops! Something went wrong",
      "detail": exc.detail
    }
  )

@app.exception_handler(ResponseValidationError)
async def response_validation_error(response: Response, exc: ResponseValidationError):
  return JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
      "detail": "Oops! response is invalid"
    }
  )

@app.exception_handler(user_route.ResourceExistsError)
async def resource_exists_error(response: Response, exc:user_route.ResourceExistsError):
  # exc.details.update({"extra_info": "Who is there"})
  return JSONResponse(
    content={"message": exc.message}, 
    status_code=exc.error_code
  )

@app.exception_handler(ValueExceptionError)
async def value_error(response: Response, exc: ValueExceptionError):
  print("Value Error")
  return JSONResponse(
    content={"message": exc.message},
    status_code=exc.error_code
  )
@app.get("/error_endpoint")
async def raise_exception():
  raise HTTPException(status_code=400)


