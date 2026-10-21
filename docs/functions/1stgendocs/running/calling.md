---
url: https://docs.cloud.google.com/functions/1stgendocs/running/calling/
title: Call local functions \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:33.470188+00:00
---

# Call local functions  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/running/calling/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Call local functions

## Setup

This document assumes that you've [set up a locally running function](https://docs.cloud.google.com/functions/1stgendocs/running/overview) on `localhost` using either [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/running/function-frameworks) or [Buildpacks](https://docs.cloud.google.com/functions/1stgendocs/running/overview). It also assumes that you've installed the `curl` tool on your local machine.

**Note:** while some operating systems include `curl` by default, others (such as Windows) do not. See [this page](https://curl.haxx.se/download.html) for instructions on how to install `curl` on your machine. Alternatively, you can also use other HTTP testing tools such as [Postman](https://postman.com/downloads) to test your functions.

## Sending requests to local functions

You can trigger locally-running functions by sending them HTTP requests routed via a local serving process.

Determine where your function is running locally by checking the URL displayed when you started [running the function](https://docs.cloud.google.com/functions/1stgendocs/running/overview). By default, your function will be hosted at `localhost:8080`.

### HTTP functions

When you test your HTTP function from your development environment, it normally listens for requests on `localhost:8080`. This interface is only accessible from the machine or VM your function is running on; requests sent from any other system can't reach it. For this reason, you must issue the HTTP request from the same system that your function is running on. In the following examples, if your function is listening on a port other than _8080_ , replace the _8080_ in the example with the port number for your function.

#### Testing HTTP functions with Cloud Shell

If you're using Cloud Shell to build and test your function, start your function locally in the Cloud Shell terminal window, then issue the HTTP trigger request from a browser or `curl` instance as follows:

### Browser

Click the ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg) icon on your cloud shell toolbar and choose _port 8080_ or _Change port_ to pick a different port. This opens a browser window on the correct system and issues a GET request to the indicated port.

### Curl

To control the format of your HTTP request or to see the unformatted reply, use `curl`:

  1. Click the **+** icon on the Cloud Shell menu bar to open a new terminal window on the same system your function is running on.
  2. From within that window, run the `curl` command to trigger your function. For example:
         
         curl localhost:8080
         




#### Testing HTTP functions on your desktop server

If you're building and running your function on your local desktop system, first start your function locally, then issue your HTTP trigger request from a browser or `curl` instance as follows:

### Browser

Open a new browser window or tab and type `http://localhost:8080` into the browser address bar. This opens a browser window to `localhost:8080` on your desktop server to trigger your function.

### Curl

Open a new terminal window on your local desktop, then run the `curl` command in that window to trigger your function. For example:
    
    
     curl localhost:8080
    

This runs the specified `curl` command to trigger your function and displays the unformatted response.

### CloudEvent functions

You can send sample events to [CloudEvent functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#cloudevent-functions) using `curl`. The following `curl` requests show how to send sample [Cloud Pub/Sub](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) and [Cloud Storage](https://docs.cloud.google.com/functions/1stgendocs/calling/storage) events to a CloudEvent function running at `localhost:8080`.

###  Pub/Sub 
    
    
    curl localhost:8080 \
      -X POST \
      -H "Content-Type: application/json" \
      -H "ce-id: 123451234512345" \
      -H "ce-specversion: 1.0" \
      -H "ce-time: 2020-01-02T12:34:56.789Z" \
      -H "ce-type: google.cloud.pubsub.topic.v1.messagePublished" \
      -H "ce-source: //pubsub.googleapis.com/projects/MY-PROJECT/topics/MY-TOPIC" \
      -d '{
            "message": {
              "data": "d29ybGQ=",
              "attributes": {
                 "attr1":"attr1-value"
              }
            },
            "subscription": "projects/MY-PROJECT/subscriptions/MY-SUB"
          }'
        

**Note:** `data` values from [Cloud Pub/Sub events](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) have `base64`-encoded `data` values. Functions that need access to the original Cloud Pub/Sub message's `data` value are expected to perform this decoding. In this example, `base64`-encoding the word `world` gives us `d29ybGQ=`. 

###  Storage 
    
    
    curl localhost:8080 \
      -X POST \
      -H "Content-Type: application/json" \
      -H "ce-id: 123451234512345" \
      -H "ce-specversion: 1.0" \
      -H "ce-time: 2020-01-02T12:34:56.789Z" \
      -H "ce-type: google.cloud.storage.object.v1.finalized" \
      -H "ce-source: //storage.googleapis.com/projects/_/buckets/MY-BUCKET-NAME" \
      -H "ce-subject: objects/MY_FILE.txt" \
      -d '{
            "bucket": "MY_BUCKET",
            "contentType": "text/plain",
            "kind": "storage#object",
            "md5Hash": "...",
            "metageneration": "1",
            "name": "MY_FILE.txt",
            "size": "352",
            "storageClass": "MULTI_REGIONAL",
            "timeCreated": "2020-04-23T07:38:57.230Z",
            "timeStorageClassUpdated": "2020-04-23T07:38:57.230Z",
            "updated": "2020-04-23T07:38:57.230Z"
          }'
        

**Note:** The `data` value in the example above contains the most commonly-used attributes of a Cloud Storage Object event. See the [ Cloud Storage Object reference ](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) for a complete list of Cloud Storage object properties. 

### Background functions

You can send sample events to [background functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions) using `curl`. The following `curl` requests show how to send sample [Cloud Pub/Sub](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) and [Cloud Storage](https://docs.cloud.google.com/functions/1stgendocs/calling/storage) events to a background function running at `localhost:8080`.

###  Pub/Sub 
    
    
    # 'world' base64-encoded is 'd29ybGQ='
    curl localhost:8080 \
      -X POST \
      -H "Content-Type: application/json" \
      -d '{
            "context": {
              "eventId":"1144231683168617",
              "timestamp":"2020-05-06T07:33:34.556Z",
              "eventType":"google.pubsub.topic.publish",
              "resource":{
                "service":"pubsub.googleapis.com",
                "name":"projects/sample-project/topics/gcf-test",
                "type":"type.googleapis.com/google.pubsub.v1.PubsubMessage"
              }
            },
            "data": {
              "@type": "type.googleapis.com/google.pubsub.v1.PubsubMessage",
              "attributes": {
                 "attr1":"attr1-value"
              },
              "data": "d29ybGQ="
            }
          }'
        

**Note:** `data` values from [Cloud Pub/Sub events](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) are sent to the function as `base64`-encoded strings. 

###  Storage 
    
    
    curl localhost:8080 \
      -X POST \
      -H "Content-Type: application/json" \
      -d '{
            "context": {
              "eventId": "1147091835525187",
              "timestamp": "2020-04-23T07:38:57.772Z",
              "eventType": "google.storage.object.finalize",
              "resource": {
                 "service": "storage.googleapis.com",
                 "name": "projects/_/buckets/MY_BUCKET/MY_FILE.txt",
                 "type": "storage#object"
              }
            },
            "data": {
              "bucket": "MY_BUCKET",
              "contentType": "text/plain",
              "kind": "storage#object",
              "md5Hash": "...",
              "metageneration": "1",
              "name": "MY_FILE.txt",
              "size": "352",
              "storageClass": "MULTI_REGIONAL",
              "timeCreated": "2020-04-23T07:38:57.230Z",
              "timeStorageClassUpdated": "2020-04-23T07:38:57.230Z",
              "updated": "2020-04-23T07:38:57.230Z"
            }
          }'
        

**Note:** The `data` value in the example above contains the most commonly-used attributes of a Cloud Storage Object event. See the [ Cloud Storage Object reference ](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) for a complete list of Cloud Storage object properties. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
