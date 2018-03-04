#!/usr/bin/env python

import requests

url = "https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/scoring/invocations"

payload = "{\"x\": 6,\"y\": 9}"
headers = {
    'x-amz-date': "20180304T020831Z",
    'authorization': "AWS4-HMAC-SHA256 Credential=ASIAJ25I7AD67LWW66KQ/20180304/us-east-1/lambda/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date;x-amz-security-token, Signature=e772f9660517d0bb81b7497f07112640372e28aab8f75690f1aa14647ab6ea51",
    'x-amz-security-token': "FQoDYXdzEDsaDPJO2VN1fyF32SgRSyLnAbvmsE9OtU5X/tFnKW9AIQTA8Pic0cRWO0GmyzrJ/JCuUWfGuawc9xamCui8ngYjdt2tm9hVlnSzB9nU0ZyGYBV9nf0vAi4pblIrQ+BHKWoPoWFdpgMFjnuCCVIEri6a7LdhSebA1Sdt9qhD8y9ecQncixaC9SNZDXo4NBPHrhpFnvnUJenEgvjRoDYwEG3Mp/YCDekYLQy8VcQPhAUdrWcjJ636yqKznjBwPCBJFA55tmZtJeDffck3yYSblD+ierFXy6M9Nz5qjxDAra87DtwBYbFbtCDBVRkbiBr6FkoNrL7VdTcAJCjPpe3UBQ==",
    'content-type': "application/json",
    'host': "lambda.us-east-1.amazonaws.com",
    'cache-control': "no-cache",
    'postman-token': "c95d2e3a-904f-1c6b-c1df-f6c21f889d16"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)