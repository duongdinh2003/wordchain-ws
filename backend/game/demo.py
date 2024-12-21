"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-11199.c252.ap-southeast-1-1.ec2.redns.redis-cloud.com',
    port=11199,
    decode_responses=True,
    username="default",
    password="PYbBNI9pTV8eOMaL2sNWR3V2NcUB5Qk3",
)

cursor = 0
keys = []

try:
    # Flush all db
    # response = r.flushall()
    # print("flushall response:", response)

    # Get all keys
    # keys = r.keys('*')
    # print("All keys:", keys)

    # scan batch
    # while True:
    #     cursor, batch_keys = r.scan(cursor, match="*", count=100)
    #     keys.extend(batch_keys)
    #     if cursor == 0:
    #         break
    # print("All keys:", keys)

    # Connection list
    clients = r.execute_command("CLIENT LIST")
    print("Clients list:")
    print(clients)
    connection_count = len(clients)
    print("Connection count:", connection_count)

    # Turn off connection
    r.execute_command("CLIENT KILL TYPE normal")
    print("OK")
except Exception as error:
    print("Error connect redis:", error)

r.close()
