---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/execution-environment-security/
title: Execution environment security \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:42.053356+00:00
---

# Execution environment security  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/execution-environment-security/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Execution environment security

Every function runs on top of a versioned [runtime image](https://cloud.google.com/docs/buildpacks/build-run-image) within the Cloud Run functions secure [execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment). Runtime images contain operating system libraries, [language runtimes](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#runtimes) and other [system packages](https://docs.cloud.google.com/functions/docs/reference/system-packages). Google maintains all Cloud Run functions runtime images, releasing security patches and maintenance updates after a period of stability testing.

## Runtime images

Each runtime has an associated runtime image (also known as a run image) in a public repository on `gcr.io`. For a of list runtime IDs and their runtime images, see [runtimes](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#runtimes).

### Identify your runtime image

You can identify the runtime image used to create your function by inspecting the [build logs](https://docs.cloud.google.com/functions/1stgendocs/building#view_your_build_image_logs) for your function.

Within the build logs, search for `google.run-image`. This gives you the log entry from the build step that describes the version of the runtime image used to build your function. For example, a log entry for a Nodejs function might look like this:
    
    
    {
      ...
      "textPayload": "Step #2 - \"build\": Adding image label google.run-image:
        us.gcr.io/serverless-runtimes/google-22-full/runtimes/nodejs20:nodejs20_20241110_20_18_0_RC00
    ",
      ...
    }
    

## Security update policy

You can choose one of the following security update policies:

  * **Automatic updates** (default): Updates and security patches to the runtime environment are published in new versions of the runtime image. After a period of testing for stability and reliability, the updated runtime is rolled out to all functions resulting in a zero downtime update. Automatic security updates are available with Cloud Run functions (1st gen) and Cloud Run functions. To take on language-level security fixes, you may need to rebuild functions that use compiled languages such as Go or Java.

  * **On deployment updates** : Updates and security patches are applied to runtimes only when functions are deployed or redeployed, unless otherwise noted. Updates on deployment are available on both Cloud Run functions (1st gen) and Cloud Run functions.




The runtime update policy can be changed using the `--runtime-update-policy` [flag](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime-update-policy) in your `gcloud functions deploy` command.

### Set your function's update policy

If you're using Cloud Run functions (1st gen), you can change your function's update policy by including the `--runtime-update-policy` flag in your `gcloud deploy` command as shown here:
    
    
      gcloud functions deploy FUNCTION_NAME --no-gen2 \
        --runtime-update-policy=POLICY ...
    

Replace:

  * FUNCTION_NAME with the name of your function
  * POLICY with `automatic` or `on-deploy`



### Inspect your function's update policy

You can inspect your function's update policy with the following command:
    
    
      gcloud functions describe FUNCTION_NAME \
    

Where FUNCTION_NAME is the name of your function

  * Functions with automatic security updates enabled will have the key `automaticUpdatePolicy`
  * Functions that update on deployment will have the key `onDeployUpdatePolicy`



### Identify the runtime image used after an automatic update

When you enable automatic updates, Cloud Run functions swaps your function's runtime image with a newer revision containing additional security patches and updates. This change appears in your function's [runtime logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging#viewing_runtime_logs).

Inside the runtime logs the `runtime_version` label tells you when a new runtime image is being used on your function. A log entry for a Nodejs function that has been automatically updated might look like this:
    
    
    {
      ...
      "labels:" {
        runtime_version: nodejs20_20230924_20_6_1_RC00
        execution_id: ...
      }
      ...
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
