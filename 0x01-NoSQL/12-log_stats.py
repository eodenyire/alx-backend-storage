#!/usr/bin/env python3
from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client.logs  # Database name
    collection = db.nginx  # Collection name

    # Get total number of logs
    total_logs = collection.count_documents({})

    # Get count for each method
    methods_count = {
        "GET": collection.count_documents({"method": "GET"}),
        "POST": collection.count_documents({"method": "POST"}),
        "PUT": collection.count_documents({"method": "PUT"}),
        "PATCH": collection.count_documents({"method": "PATCH"}),
        "DELETE": collection.count_documents({"method": "DELETE"})
    }

    # Get count for GET requests to /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Display results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
