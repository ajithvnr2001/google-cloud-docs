---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-run-floor/
title: Calculate math floor \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:35.889317+00:00
---

# Calculate math floor  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-run-floor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Calculate math floor Stay organized with collections  Save and categorize content based on your preferences. 

After receiving an HTTP request, extracts input from the JSON body, calculates its math.floor, and returns the result.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use Workflows with Cloud Run and Cloud Run functions tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/run/cloud-run)
  * [Using Workflows to connect services](https://docs.cloud.google.com/run/docs/tutorials/workflows)
  * [Workflows Tutorial (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/tutorials/workflows-1st-gen)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    import logging
    import os
    import math
    
    from flask import Flask, request
    
    app = Flask(__name__)
    
    
    @app.route('/', methods=['POST'])
    def handle_post():
        content = json.loads(request.data)
        input = float(content['input'])
        return f"{math.floor(input)}", 200
    
    
    if __name__ != '__main__':
        # Redirect Flask logs to Gunicorn logs
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
        app.logger.info('Service started...')
    else:
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
