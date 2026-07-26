#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Number of logs
    print(f"{collection.count_documents({})} logs")

    # Methods
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")

    # Status check
    print(
        f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check"
    )
    
