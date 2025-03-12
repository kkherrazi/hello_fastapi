# GET at /

curl -X 'POST' -i \
  'http://127.0.0.1:8000/user' \
  -H 'Content-Type: application/json' \
  -d '{
  "userid": 12345,
  "name": "Khalid",
  "adresse": "something else"
}'