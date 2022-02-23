import json
import os

with open("input.json", "r") as file:
    data = json.load(file)
    days = {}

    for region in data:
        for event in data[region]["events"]:
            event = {
                "name": event["title"],
                "region": region,
                "date": event["date"],
                "notes": event["notes"],
            }
            try:
                days[event["date"]].append(event)
            except KeyError:
                days[event["date"]] = [event]


output_folder = "dist"
if not os.path.isdir(output_folder):
    raise Exception(f"Output folder {output_folder} not found.")

for day in days:
    with open(f"dist/days/{day}", "w", encoding="utf-8") as file:
        json.dump(days[day], file, ensure_ascii=False, indent=4)
