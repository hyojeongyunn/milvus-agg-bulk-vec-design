from pymilvus import MilvusClient, Collection, CollectionSchema, DataType, FieldSchema, connections
import random

connections.connect(
    host="127.0.0.1", # Replace with your Milvus server IP
    port="19530"
)

# MODE = "insert"
# MODE = "query"
MODE = "insert and query"
# MODE = "drop"

COLLECTION_NAME = "agg_collection"

def insert():
    fields = [FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
              FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=4),
              FieldSchema(name="doc_id", dtype=DataType.INT64)] 

    schema = CollectionSchema(fields=fields, enable_dynamic_field=False)
    collection = Collection(name=COLLECTION_NAME, schema=schema)

    index_params = {
        "metric_type": "COSINE",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128},
    }
    collection.create_index("vector", index_params)

    data = [
        {"id": 1, "vector": [1, 0, 0, 0], "doc_id": 1},
        {"id": 2, "vector": [0, 2, 0, 0], "doc_id": 1},
        {"id": 3, "vector": [0, 3, 0, 0], "doc_id": 2},
        {"id": 4, "vector": [0, 4, 0, 0], "doc_id": 2},
        {"id": 5, "vector": [0, 0, 5, 0], "doc_id": 3},
        {"id": 6, "vector": [0, 0, 6, 0], "doc_id": 3},
        {"id": 7, "vector": [0, 0, 0, 7], "doc_id": 4},
        {"id": 8, "vector": [0, 0, 0, 8], "doc_id": 4},
    ]
    collection.insert(data)

def query():
    collection = Collection(name=COLLECTION_NAME)
    collection.load()

    # Bulk-vector search
    res = collection.search(
        data=[
            [1, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 0, 0, 0]],
        limit=1,
        anns_field="vector",
        param={"metric_type": "COSINE"},
        group_by_field="doc_id")
    
    print(res)

def drop():
    from pymilvus import utility
    utility.drop_collection(COLLECTION_NAME)
    collection = Collection(name=COLLECTION_NAME)
    collection.load()



if MODE == "insert":
    insert()
elif MODE == "query":
    query()
elif MODE == "insert and query":
    insert()
    query()
elif MODE == "drop":
    drop()
else:
    print("unsupported MODE")


'''
When BulkAggType is none:
["['id: 1, distance: 1.0, entity: {}']", "['id: 1, distance: 1.0, entity: {}']", "['id: 1, distance: 1.0, entity: {}']"]
When BulkAggType is sum:
["['id: 1, distance: 3.0, entity: {}']"]

One can fix BulkAggType dynamically with etcd.
'''