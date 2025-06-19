import requests
import json

SERP_API_KEY = '你的API KEY'
GOOGLE_SCHOLAR_ID = 'FZvs20wAAAAJ'

params = {
    "api_key": SERP_API_KEY,
    "engine": "google_scholar_author",
    "author_id": GOOGLE_SCHOLAR_ID
}

response = requests.get("https://serpapi.com/search", params=params)
data = response.json()

# 保存结果
with open("results/gs_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# citations
citations = data.get("cited_by", {}).get("value", 0)
shield_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(citations)
}
with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
    json.dump(shield_data, f, indent=2, ensure_ascii=False)

print("✅ SerpAPI Done")
