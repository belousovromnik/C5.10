import os
import random

from bottle import route, run
from answer import answer, answer_api

def generate_message():
    return answer()


@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html


@route("/api/roll/<some_id:int>")
def example_api_response(some_id):
    return {"requested_id": some_id, "random_number": random.randrange(some_id), "str": "sdads"}


@route("/api/generate")
def api_response_one():
    ans = answer_api()
    print(ans)
    return ans


@route("/api/generate/<cnt:int>")
def api_response_many(cnt):
    # ans = answer_api(cnt)
    # print(ans)
    return answer_api(cnt)


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
