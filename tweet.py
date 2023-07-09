from fastapi import FastAPI
from requests_oauthlib import OAuth1Session as session
url = "https://api.twitter.com/2/tweets"

app = FastAPI()

@app.post("/tweet")
def tweet(message: str):
    url = "https://api.twitter.com/2/tweets"
    req = session("DbrL4p3HeDmsXFI9jUEamQ1pD", "F4wmgx6lVNeRkzdz2o8H439VwgAKtveolHEE59GHSO3xtKcGXm",
        "1677162987491307525-5gy3MGLGpnDIdVNqEbljzBiod31BHQ", "TZBnIvRU6OwtTv634fdTRKkOGVydVs4O8S5s9Y9XUAg0W")
    
    
    body = {"text":"Hello,World"}

    req.post(url,json=body)