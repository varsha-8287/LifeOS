import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from flask import Flask, render_template
from notion_client import Client
from config import NOTION_TOKEN, DATA_SOURCE_ID

app = Flask(__name__)

notion = Client(auth=NOTION_TOKEN)


def get_tasks():

    response = notion.data_sources.query(
        data_source_id=DATA_SOURCE_ID
    )

    tasks = []

    for page in response["results"]:

        props = page["properties"]
        print(props["Task"]["title"])
        tasks.append({
            "task": props["Task"]["title"][0]["plain_text"],
            "completed": props["Completed"]["number"],
            "target": props["Target"]["number"],
            "progress": props["Progress"]["formula"]["number"],
            "icon": props["Icon"]["rich_text"][0]["plain_text"]
        })

    return tasks


@app.route("/")
def home():

    tasks = get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


if __name__ == "__main__":
    app.run(debug=True)