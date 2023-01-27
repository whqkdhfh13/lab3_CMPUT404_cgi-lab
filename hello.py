#!/usr/bin/env python3
import os
import json

print("content-type: application/json")
# print("content-type: text/html")
print(json.dumps(dict(os.environ), indent=2))
# print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")