---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-functions-randomgen/
title: Generate a random number and return result in JSON \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:09.246977+00:00
---

# Generate a random number and return result in JSON  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-functions-randomgen/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Generate a random number and return result in JSON Stay organized with collections  Save and categorize content based on your preferences. 

After receiving an HTTP request, this function generates a random number between 1 and 100, and then returns the number in JSON format.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use Workflows with Cloud Run and Cloud Run functions tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/run/cloud-run)
  * [Using Workflows to connect services](https://docs.cloud.google.com/run/docs/tutorials/workflows)
  * [Workflows Tutorial (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/tutorials/workflows-1st-gen)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    import random
    from flask import jsonify
    
    
    @functions_framework.http
    def randomgen(request):
        randomNum = random.randint(1, 100)
        output = {"random": randomNum}
        return jsonify(output)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
