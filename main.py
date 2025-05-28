from fastapi import FastAPI

app = FastAPI() 


@app.get("/")  # Decorator (we can specify Url)
def root():  # Function
    return {"message": "Hello World.."}

@app.get("/posts")  #get - give me data
def get_posts():
    return {"posts": "This is your posts"}

@app.post("/createposts")  #post - here is some data
def create_posts():
    return {"message": "successfully created posts"}