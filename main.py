from fastapi import FastAPI, HTTPException, Request, status, Response
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
import json
import author_route, book_route

app = FastAPI()
app.include_router(author_route.router)
app.include_router(book_route.router)


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
      "message": "Oops! Something went wrong"
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

@app.get("/error_endpoint")
async def raise_exception():
  raise HTTPException(status_code=400)