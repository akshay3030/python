#!/usr/bin/env python

import requests

url = "https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/scoring/invocations"

payload = "{\"x\": 6,\"y\": 9}"
headers = {
    'x-amz-date': "20180304T011932Z",
    'authorization': "AWS4-HMAC-SHA256 Credential=ASIAJ6APQ544BWZFEKBA/20180304/us-east-1/lambda/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date;x-amz-security-token, Signature=c0413790fc76e665f8d18373dd776f22e0c39c73cdd57741d41ea381a7e1f8d4",
    'x-amz-security-token': "FQoDYXdzEDoaDMu+1KS4LXeCmWo+MiLnAXmxNWFVxoHYuARJbBoEqZsw9YxMaaJ4DOEV6x53dmiu/7B8I067AGpOzLPJ6sDlvLAYd/OBc8DDGnNTdliB/DUno82OQeAcpuEt4YUB3TOEYFfa//6WWPqPt7nWOqPW6WybTo0ihJxkzRIj59zj/Amwy0totd8fD9QYFWfDsOKFMNJwHDnhO3dfHmlUIw3rexamZywYB68987TpDyglgu4XXUf3J7cQ/Ge+xnm7B1gRvX53uPPQ5Mmxjl78nPcVCZaHXQRyFH7sg6PqacE2yjg6666ewSCnMnP7xETmZB6i8rVvzf7USCiFke3UBQ==",
    'content-type': "application/json",
    'host': "lambda.us-east-1.amazonaws.com",
    'cache-control': "no-cache",
    'postman-token': "9f541fff-0daf-fbd1-384f-169f000bb0b6"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)