#!/usr/bin/env python3
""" Log stats """

from pymongo import MongoClient

def nginx_logs_stats():
    """ Prints stats about nginx logs stored in MongoDB
    
    nginx_collection: The nginx document collection

    """
    client = MongoClient("mongodb://localhost:27017/")
    
    logs = client.logs
    collection = logs.nginx

    nginx_logs = collection.count_documents({})

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_stats = {method: collection.count_documents({"method": method}) for method in methods}

    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{nginx_logs} logs")
    print("Methods:")

    for method in methods:
        print(f"\tmethod {method}: {method_stats[method]}")

    print(f"{get_status_count} status check")

    # Top 10 most frequent IP addresses
    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    nginx_logs_stats()
