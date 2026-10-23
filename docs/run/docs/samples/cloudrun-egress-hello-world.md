---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-egress-hello-world/
title: Using egress and ingress settings to restrict access to services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:22.628875+00:00
---

# Using egress and ingress settings to restrict access to services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-egress-hello-world/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Using egress and ingress settings to restrict access to services Stay organized with collections  Save and categorize content based on your preferences. 

Secure your Cloud Functions by allowing them to be called only by resources, like Cloud Run, in the same Google Cloud project or VPC Service Controls service perimeter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure network settings (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings)



## Code sample

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    import urllib
    
    import google.auth.transport.requests
    import google.oauth2.id_token
    
    
    def get_hello_world(request):
        try:
            url = os.environ.get("URL")
            req = urllib.request.Request(url)
    
            auth_req = google.auth.transport.requests.Request()
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)
            req.add_header("Authorization", f"Bearer {id_token}")
    
            response = urllib.request.urlopen(req)
            return response.read()
    
        except Exception as e:
            print(e)
            return str(e)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
