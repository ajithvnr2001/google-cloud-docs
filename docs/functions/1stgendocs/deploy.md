---
url: https://docs.cloud.google.com/functions/1stgendocs/deploy/
title: Deploy a Cloud Run function (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.639531+00:00
---

# Deploy a Cloud Run function (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/deploy/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Cloud Run function (1st gen)

This guide shows you how to deploy a legacy 1st gen Cloud Run function from source code. If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run.

The deployment process takes your source code and configuration settings and [builds a runnable image](https://docs.cloud.google.com/functions/1stgendocs/building) that Cloud Run functions manages automatically in order to handle requests to your function.

## Deployment basics

Users deploying Cloud Run functions must have the [Cloud Run functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) IAM role or a role that includes the same permissions. See also [Additional configuration for deployment](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

Deploy a function using the gcloud CLI as follows:

  1. Use the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command to deploy a function:
         
         gcloud functions deploy YOUR_FUNCTION_NAME \
           [--gen2] \
           --region=YOUR_REGION \
           --runtime=YOUR_RUNTIME \
           --source=YOUR_SOURCE_LOCATION \
           --entry-point=YOUR_CODE_ENTRYPOINT \
           TRIGGER_FLAGS
         

The first argument, `YOUR_FUNCTION_NAME`, is a name for your deployed function. The function name must start with a letter followed by up to 62 letters, numbers, hyphens, or underscores, and must end with a letter or a number.

     * The [`--gen2`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--gen2) flag specifies that you want to deploy to Cloud Run functions. As of September 2024, this becomes the default. To deploy to 1st gen, use [`--no-gen2`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--gen2).

     * The [`--region`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--region) flag specifies the region in which to deploy your function. See [Locations](https://docs.cloud.google.com/functions/1stgendocs/locations) for a list of regions supported by Cloud Run functions.

     * The [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag specifies which language runtime your function uses. Cloud Run functions supports several runtimes - see [Runtimes](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#runtimes) for more information.

     * The [`--source`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--source) flag specifies the location of your function source code. See the following sections for details:

       * Deploy from your local machine
       * Deploy from Cloud Storage
     * The [`--entry-point`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--entry-point) flag specifies the entry point to your function in your source code. This is the code that will be executed when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code. See [Function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) for more information.

     * To specify the [trigger](https://docs.cloud.google.com/functions/1stgendocs/calling) for your function, additional flags (represented as `TRIGGER_FLAGS` above) are required, depending on the trigger you want to use:

Trigger flags | Trigger description  
---|---  
` [ --trigger-http](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-http)` | Trigger the function with an HTTP(S) request. See [HTTP triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/http) for more information.  
` [ --trigger-topic](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-topic)=YOUR_PUBSUB_TOPIC` | Trigger the function when a message is published to the specified Pub/Sub topic. See [Pub/Sub triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) for more information.  
` [ --trigger-bucket](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-bucket)=YOUR_STORAGE_BUCKET` | Trigger the function when an object is created or overwritten in the specified Cloud Storage bucket. See [ Cloud Storage triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/storage) for more information.  
` [ --trigger-event](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-event)=EVENT_TYPE  
[[--trigger-resource](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-resource)=RESOURCE] ` | Trigger the function when the specified event occurs. Specifying a resource is required for some event types. See [ Triggers supported in Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/calling#1st-gen-triggers) for more information.  
  
You can optionally specify additional [configuration](https://docs.cloud.google.com/functions/1stgendocs/configuring), [networking](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings), and [security](https://docs.cloud.google.com/functions/1stgendocs/securing) options when you deploy a function.

For a complete reference on the deployment command and its flags, see the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) documentation.

For some example deployment commands, see Command-line examples.




## Deploy from your local machine

This section describes how to use gcloud CLI to deploy a function from source code located on your local machine.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Follow the deployment instructions above using the `gcloud functions deploy` command.

For the `--source` flag, specify a local file system path to the root directory of the function source code - see [Source directory structure](https://docs.cloud.google.com/functions/1stgendocs/writing#directory-structure). The current working directory is used if this flag is omitted.

You can also optionally use the [`--stage-bucket`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--stage-bucket) flag to specify a Cloud Storage bucket to upload your source code to as part of deployment.

During upload of your source code, Cloud Run functions excludes unnecessary files through the [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file.




## Deploy from Cloud Storage

This section describes how to use gcloud CLI to deploy a function from source code located in a Cloud Storage bucket. The source code must be packaged as a ZIP file.

For Cloud Run functions to read from a Cloud Storage bucket, you must grant the `storage.objects.get` permission to the account performing the deployment.

See [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) in the Cloud Storage documentation for information about controlling access to buckets.

With this permission you can now deploy a function from Cloud Storage:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Follow the deployment instructions above using the `gcloud functions deploy` command.

For the `--source` flag, specify a Cloud Storage path, starting with `gs://`. The object at the path must be a ZIP file containing the function source code. Your function source files must be located at the root of the ZIP file - see [Source directory structure](https://docs.cloud.google.com/functions/1stgendocs/writing#directory-structure).




## Command-line examples

This section shows deployment commands for some example deployment scenarios.

For details about different triggers supported by Cloud Run functions, see [Cloud Run functions triggers](https://docs.cloud.google.com/functions/1stgendocs/calling).

### HTTP function from local source code

Suppose you have an HTTP function as follows:

  * The function uses Node.js 22.
  * The source code is located in the current working directory (`.`).
  * The entry point in the code is named `myHttpFunction`.



To deploy the function to Cloud Run functions with the name `my-http-function` in the region `us-central1`, you use the following command:
    
    
    gcloud functions deploy my-http-function \
      --no-gen2 \
      --region=us-central1 \
      --runtime=nodejs22 \
      --source=. \
      --entry-point=myHttpFunction \
      --trigger-http
    

### Pub/Sub function from source code in Cloud Storage

Suppose you have an event-driven function as follows:

  * The function handles Pub/Sub message publish events.
  * The function uses Python 3.12.
  * The source code is located in Cloud Storage at the path `gs://my-bucket/my_function_source.zip`.
  * The entry point in the code is named `pubsub_handler`.



To deploy the function to Cloud Run functions with the name `my-pubsub-function` in the region `europe-west1`, and have the function triggered by messages on the Pub/Sub topic `my-topic`, you use the following command:
    
    
    gcloud functions deploy my-pubsub-function \
      --no-gen2 \
      --region=europe-west1 \
      --runtime=python312 \
      --source=gs://my-bucket/my_function_source.zip \
      --entry-point=pubsub_handler \
      --trigger-topic=my-topic
    

### Cloud Storage function from local source code

Suppose you have an event-driven function as follows:

  * The function handles Cloud Storage object deletion events.
  * The function uses Java 17.
  * The source code is located locally at the path `./functions/storage-function`.
  * The entry point in the code is named `myproject.StorageFunction`.



To deploy the function to Cloud Run functions with the name `my-storage-function` in the region `asia-northeast1`, and have the function triggered by events in the Cloud Storage bucket `my-bucket`, you use the following command:
    
    
    gcloud functions deploy my-storage-function \
      --no-gen2 \
      --region=asia-northeast1 \
      --runtime=java17 \
      --source=./functions/storage-function \
      --entry-point=myproject.StorageFunction \
      --trigger-resource=gs://my-bucket \
      --trigger-event=google.storage.object.delete
    

## Next steps

  * See details about [Cloud Run functions triggers](https://docs.cloud.google.com/functions/1stgendocs/calling).
  * Learn about the [Cloud Run functions build process](https://docs.cloud.google.com/functions/1stgendocs/building).
  * Explore additional Cloud Run functions [configuration options](https://docs.cloud.google.com/functions/1stgendocs/configuring).
  * Learn about [securing Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/securing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
