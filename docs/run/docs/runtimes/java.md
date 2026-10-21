---
url: https://docs.cloud.google.com/run/docs/runtimes/java/
title: The Java runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:05.205533+00:00
---

# The Java runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The Java runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [Java Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-java) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for Java development, see [Set up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

## Supported Java runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Java 25 | java25 | 
* google-24 (default)
* google-24-full
| 
* [google-24/java25](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/java25)
* [google-24-full/java25](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/java25)
| October 2031 |   
Java 21 | java21 | 
* google-22 (default)
* google-22-full
| 
* [google-22/java21](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/java21)
* [google-22-full/java21](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java21)
| September 2031 |   
Java 17 | java17 | 
* google-22 (default)
* google-22-full
| 
* [google-22/java17](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/java17)
* [google-22-full/java17](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java17)
| October 2027 |   
Java 11 | java11 |  google-18-full  |  [google-18-full/java11](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/java11) | 2024-10-31 | 2025-10-31  
  
## Select your runtime

You can select one of the supported Java runtimes for your function during deployment. 

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [Java base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image java25
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a Java runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#java) for more information.

## Specifying dependencies

You can specify dependencies for your function using [Maven](https://maven.apache.org) or [Gradle](https://gradle.org). For more information, see [Specify dependencies in Java](https://docs.cloud.google.com/run/docs/runtimes/java-dependencies).

## Environment variables

Your Java runtime automatically sets certain environment variables for your function to use as needed. For details, see [Configure environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables).

## Execution ID

For Java functions that use `functions-framework` version 1.4.0 or later, you can use the logging class `java.util.logging.Logger` to add a unique execution ID to log outputs. Using `stdout` or `stderr` (for example, `System.println()`) does not add the execution ID.

Note that:

  * If you created your function using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest) (for example, by using `gcloud functions`, the REST API, or Terraform), this execution ID is added automatically.

  * If you created your function using the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/cloud-run-admin-api-overview) (for example, by using Google Cloud console, `gcloud run`, the REST API, or Terraform), you need to set the `LOG_EXECUTION_ID` environment variable to `true` to use this feature.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
