from notion_client import Client
from config import NOTION_TOKEN, DATA_SOURCE_ID

notion = Client(auth=NOTION_TOKEN)

response = notion.data_sources.query(
    data_source_id=DATA_SOURCE_ID
)

print("\n===== LIFE OS TASKS =====\n")

for page in response["results"]:

    props = page["properties"]

    task = props["Task"]["title"][0]["plain_text"]

    completed = props["Completed"]["number"]

    target = props["Target"]["number"]

    progress = props["Progress"]["formula"]["number"]

    icon = props["Icon"]["rich_text"][0]["plain_text"]

    print(
        f"{icon} {task} | "
        f"{completed}/{target} | "
        f"{progress}%"
    )