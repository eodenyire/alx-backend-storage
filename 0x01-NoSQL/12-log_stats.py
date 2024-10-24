#!/usr/bin/env python3
""" 12. Log stats
    This script connects to a MongoDB database to retrieve and display
    statistics about Nginx logs, including the total number of logs and
    counts for different HTTP methods.
"""

from pymongo import MongoClient, errors


def log_stats():
    """Fetch and print statistics from the Nginx logs in MongoDB.
    
    This function connects to the MongoDB server, retrieves the total
    number of log entries, counts the occurrences of specific HTTP methods,
    and counts the number of GET requests to the '/status' path.
    """
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        logs_collection = client.logs.nginx
        total = logs_collection.count_documents({})
        get = logs_collection.count_documents({"method": "GET"})
        post = logs_collection.count_documents({"method": "POST"})
        put = logs_collection.count_documents({"method": "PUT"})
        patch = logs_collection.count_documents({"method": "PATCH"})
        delete = logs_collection.count_documents({"method": "DELETE"})
        path = logs_collection.count_documents({"method": "GET", "path": "/status"})
        
        print(f"{total} logs")
        print("Methods:")
        print(f"\tmethod GET: {get}")
        print(f"\tmethod POST: {post}")
        print(f"\tmethod PUT: {put}")
        print(f"\tmethod PATCH: {patch}")
        print(f"\tmethod DELETE: {delete}")
        print(f"{path} status check")
    
    except errors.ConnectionError:
        print("Could not connect to MongoDB.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    log_stats()
