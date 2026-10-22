---
url: https://docs.cloud.google.com/functions/docs/samples/functions-tips-gcp-apis/
title: Cached library \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:18.101495+00:00
---

# Cached library  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-tips-gcp-apis/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cached library Stay organized with collections  Save and categorize content based on your preferences. 

HTTP Cloud Function that uses a cached client library instance to reduce the number of connections required per function invocation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Optimize networking (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/networking)



## Code sample

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    /**
     * HTTP Cloud Function that uses a cached client library instance to
     * reduce the number of connections required per function invocation.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} req.body Cloud Function request context body.
     * @param {String} req.body.topic The Cloud Pub/Sub topic to publish to.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('gcpApiCall', (req, res) => {
      const topic = pubsub.topic(req.body.topic);
    
      const data = Buffer.from('Test message');
      topic.publishMessage({data}, err => {
        if (err) {
          res.status(500).send(`Error publishing the message: ${err}`);
        } else {
          res.status(200).send('1 message published');
        }
      });
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    import functions_framework
    from google.cloud import pubsub_v1
    
    
    # Create a global Pub/Sub client to avoid unneeded network activity
    pubsub = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    
    
    @functions_framework.http
    def gcp_api_call(request):
        """
        HTTP Cloud Function that uses a cached client library instance to
        reduce the number of connections required per function invocation.
        Args:
            request (flask.Request): The request object.
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
    
        """
        The `GCP_PROJECT` environment variable is set automatically in the Python 3.7 runtime.
        In later runtimes, it must be specified by the user upon function deployment.
        See this page for more information:
            https://cloud.google.com/functions/docs/configuring/env-var#python_37_and_go_111
        """
        project = os.getenv("GCP_PROJECT")
        request_json = request.get_json()
    
        topic_name = request_json["topic"]
        topic_path = pubsub.topic_path(project, topic_name)
    
        # Process the request
        data = b"Test message"
        pubsub.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data=data)
    
        return "1 message published"
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
