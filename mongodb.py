import urllib.parse

# Replace these with your MongoDB credentials
username = "vvish"
password = "7766"  # special characters included
cluster  = "cluster0.mongodb.net"  # your cluster address
database = "test"  # default database

# Percent-encode username and password
username_enc = urllib.parse.quote(username)
password_enc = urllib.parse.quote(password)

# Build full connection string
connection_string = f"mongodb+srv://{username_enc}:{password_enc}@{cluster}/{database}?retryWrites=true&w=majority"

print("Use this connection string in VS Code MongoDB extension:")
print(connection_string)
