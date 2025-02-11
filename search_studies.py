from elasticsearch import Elasticsearch
import redis

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")
# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

def search_studies(keyword: str, category: str = None):
    """
    Search studies by keyword and optional category filter.
    """
    query = {
        "bool": {
            "must": [
                {"multi_match": {"query": keyword, "fields": ["title", "description", "keywords"]}}
            ],
            "filter": []
        }
    }
    
    if category:
        query["bool"]["filter"].append({"term": {"category": category}})
    
    results = es.search(index="studies", body={"query": query, "size": 10})
    
    return [hit["_source"]["title"] for hit in results["hits"]["hits"]]

# Example usage
print(search_studies("cognition", "Cognitive Science"))


def add_study_to_autocomplete(title):
    """
    Add a study title to the Redis autocomplete trie.
    """
    for i in range(1, len(title) + 1):
        prefix = title[:i].lower()
        redis_client.zadd("autocomplete", {title: 0})

def autocomplete_search(prefix):
    """
    Return autocomplete suggestions for a given prefix.
    """
    results = redis_client.zrangebylex("autocomplete", f"[{prefix}", f"[{prefix}\xff", start=0, num=5)
    return [title.decode("utf-8") for title in results]

# Example usage
add_study_to_autocomplete("Machine Learning in Psychology")
add_study_to_autocomplete("Machine Vision and AI")
add_study_to_autocomplete("Machine Ethics")

print(autocomplete_search("mach"))  # Returns ["Machine Learning in Psychology", "Machine Vision and AI", "Machine Ethics"]
