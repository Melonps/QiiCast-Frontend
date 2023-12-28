import json
import random

random.seed(42)

sample_url = "https://qiita.com/tamura__246/items/366b5581c03dd74f4508"

data = {
    "pages": []
}
for i in range(100):
    this_data = {
        "url": sample_url,
        "rating": random.random(),
        "title": f"sample title {i}",
    }
    data["pages"].append(this_data)

with open("dummy_data.json", "w") as f:
    json.dump(data, f, indent=2)