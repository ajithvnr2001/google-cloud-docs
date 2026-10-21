---
url: https://docs.cloud.google.com/functions/1stgendocs/running/functions-emulator/
title: Run functions using the Functions Emulator \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.552425+00:00
---

# Run functions using the Functions Emulator  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/running/functions-emulator/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run functions using the Functions Emulator

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Google Cloud CLI _Functions Emulator_ enables you to you manage local instances of your Cloud Run functions through the [gcloud alpha functions local](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/local) command. This lets you deploy and test your functions on your local system before deploying them to the Google Cloud environment.

The Functions Emulator uses [Google Cloud's buildpacks](https://cloud.google.com/docs/buildpacks/overview) to package your function code into locally-runnable container images. You then run these images locally with [Docker](https://docs.docker.com/get-docker/).

**Note:** The `gcloud alpha functions local` command is available as an alpha pre-release, and might be unstable or change without notice. If you prefer to run your functions locally without containerization, use the [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/running/function-frameworks).

## Installation prerequisites

Before proceeding, make sure you have the following installed:

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Buildpacks pack tool](https://buildpacks.io/docs/tools/pack/)
  * [Docker](https://www.docker.com/get-started/)



## Deploy your function locally

To deploy your function locally with the Functions Emulator, use the `gcloud functions` command:

###  Node.js 
    
    
      gcloud alpha functions local deploy LOCAL_DEPLOYMENT_NAME \
        --entry-point=ENTRY_POINT \
        --no-gen2 \
        --runtime=nodejs22

###  Python 
    
    
      gcloud alpha functions local deploy LOCAL_DEPLOYMENT_NAME \
        --entry-point=ENTRY_POINT \
        --runtime=python314

###  Go 
    
    
      gcloud alpha functions local deploy LOCAL_DEPLOYMENT_NAME \
        --entry-point=ENTRY_POINT \
        --no-gen2 \
        --runtime=go121

###  Java 
    
    
      gcloud alpha functions local deploy LOCAL_DEPLOYMENT_NAME \
        --entry-point=ENTRY_POINT \
        --no-gen2 \
        --runtime=java17 

**Note:** Java functions use `[PACKAGE_NAME].[CLASS_NAME]` as an entry-point value. 

###  Ruby 
    
    
      gcloud alpha functions local deploy LOCAL_DEPLOYMENT_NAME \
        --entry-point=ENTRY_POINT \
        --runtime=ruby40

Replace:

  * LOCAL_DEPLOYMENT_NAME: The name under which you are locally deploying your function.
  * ENTRY_POINT: The entry point of your function.



You can further configure your deployment command with the following optional flags:

Flag | Description  
---|---  
`--port` | The port on which to listen for requests (default: `8080`).  
`--builder` | The name of the [buildpack builder](https://docs.cloud.google.com/docs/buildpacks/builders) to use.  
  
The `--builder` value defaults to the App Engine builder for your function's language. For example, it defaults to `gcr.io/serverless-runtimes/google-22-full/builder/python` for Python.

When you first use the `gcloud alpha` command, the `gcloud` command will prompt you to install the [gcloud alpha](https://cloud.google.com/sdk/gcloud#release_levels) command set.

## Call your local function

To call your local function without data, use the following command:
    
    
    gcloud alpha functions local call LOCAL_DEPLOYMENT_NAME
    

Replace LOCAL_DEPLOYMENT_NAME with the name you want to locally deploy your function under.

**Note:** `gcloud alpha functions local call` calls your function with an HTTP POST request. To use a different HTTP method, use a dedicated HTTP request tool such as `curl`. See [calling local functions](https://docs.cloud.google.com/functions/1stgendocs/running/calling) for instructions on how to interact with your locally-running function using `curl`.

To include data in the call to your local function, choose the tab that matches your function type:

### HTTP function

Call your local HTTP function as follows:
    
    
    gcloud alpha functions local call LOCAL_DEPLOYMENT_NAME \
        --data='{"message": "MESSAGE"}'
    

Replace:

  * LOCAL_DEPLOYMENT_NAME: The name to locally deploy your function under.
  * ENTRY_POINT: The entry point of your function.
  * MESSAGE: A text string to pass in as the body of the HTTP request.



### CloudEvent function

To call your local CloudEvent function, you must supply a `CloudEvent` JSON object describing the trigger event:
    
    
    gcloud alpha functions local call LOCAL_DEPLOYMENT_NAME \
        --cloud-event="CLOUD_EVENT_JSON"
    

Replace:

  * LOCAL_DEPLOYMENT_NAME: The name to locally deploy your function under.
  * ENTRY_POINT: The entry point of your function.
  * CLOUD_EVENT_JSON: A JSON-encoded string in structured content mode describing the triggering event. For more details and examples, see [CloudEvents - JSON event format](https://docs.cloud.google.com/eventarc/docs/workflows/cloudevents).



Here is an example command line:
    
    
    gcloud alpha functions local call my-function --cloud-event='{
     "specversion" : "1.0",
      "type" : "com.github.pull.create",
      "source" : "https://github.com/cloudevents/spec/pull",
      "subject" : "123",
      "id" : "ce",
      "time" : "2021-01-27T18:30:00Z", "data" : "{\n \"subscription\": \"projects\/test-project\/subscriptions\/my-subscription\",\n \"message\": {\n \"attributes\": {\n \"attr1\":\"attr1-value\"\n },\n \"data\": \"d29ybGQ=\",\n \"messageId\": \"message-id\",\n \"publishTime\":\"2021-02-05T04:06:14.109Z\",\n \"orderingKey\": \"ordering-key\"\n }\n}"
      }'
    

See [CloudEvent specs](https://github.com/cloudevents/spec/blob/main/cloudevents/formats/json-format.md) for more information about how the JSON format is defined for CloudEvents.

## Delete your local function deployment

Delete your local function deployment with the following command:
    
    
    gcloud alpha functions local delete LOCAL_DEPLOYMENT_NAME
    

Replace LOCAL_DEPLOYMENT_NAME with the name to locally deploy your function under.

This command undeploys your function but doesn't delete the function code.

## Next steps

  * Learn how to [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy) on Google Cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
