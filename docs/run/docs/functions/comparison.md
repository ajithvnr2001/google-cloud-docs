---
url: https://docs.cloud.google.com/run/docs/functions/comparison/
title: Compare Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:57.591583+00:00
---

# Compare Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/functions/comparison/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Compare Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

Understanding how Google Cloud's function deployment options compare helps you transition workloads from the [Cloud Functions API](https://docs.cloud.google.com/functions/docs/reference/rest) to the Cloud Run Admin API. This document details key differences across concepts, configuration, deployment, and triggers and retries.

## Comparison

There are two versions of Cloud Run functions:

  * **Cloud Run functions** , is the latest version of functions, [deployed as a service on Cloud Run](https://docs.cloud.google.com/run/docs/resource-model#functions). They can be created in one of the following ways:

    * [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/cloud-run-admin-api-overview) (Recommended): Functions created with this API (for example, by using Google Cloud console, `gcloud run`, the REST API, or Terraform) can be managed exclusively using the Cloud Run Admin API.
    * [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest): Functions created with this API (for example, by using `gcloud functions`, the REST API, or Terraform) can be managed with the Cloud Run Admin API as well as the Cloud Functions v2 API. When using this API, you specify the trigger when deploying your function. Learn how to [detach](https://docs.cloud.google.com/functions/docs/managing#detach) a v2 API function so that it can be managed exclusively using the Cloud Run Admin API.
  * **Cloud Run functions (1st gen)** , formerly known as Cloud Functions (1st gen), is the original version of functions with limited event triggers, runtimes, and configurability. Learn how to [upgrade your 1st gen functions to Cloud Run](https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions).




By deploying functions directly onto Cloud Run, your functions are automatically built as containers and deployed as a Cloud Run service.

### Concepts

The following table summarizes the conceptual differences for functions.

| **Cloud Run functions** | **Cloud Run functions (1st gen)**  
---|---|---  
Former product name | Cloud Functions (2nd gen) | Cloud Functions (1st gen)  
Resource model | A function is a Cloud Run service that is deployed from source code | A function is deployed from source code  
Types of functions terminology | 

  * HTTP functions
  * CloudEvents functions, also referred to as event-driven functions, are supported in all language runtimes.

| 

  * HTTP functions
  * Only Ruby, .NET, and PHP runtimes support CloudEvents. For Node.js, Go, Python, and Java, create event-driven functions using Background functions.

  
Assigned HTTPS URL | `run.app`  
  
Functions created with the Cloud Functions v2 API also have a `cloudfunctions.net` endpoint. | `cloudfunctions.net`  
Image registry | Artifact Registry only | Artifact Registry or Container Registry (deprecated)  
IAM roles for deployment | 

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/run.serviceusage.serviceUsageConsumer`)
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)

| 

  * [Cloud Functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) (`roles/cloudfunctions.developer`)

  
Internal infrastructure | Cloud Run | Google internal  
Pricing model | [Cloud Run pricing](https://cloud.google.com/run/pricing) | [Cloud Run functions (1st gen) pricing](https://docs.cloud.google.com/functions/pricing-1stgen)  
  
### Configuration

Cloud Run builds functions into containers and deploys them as services. When you deploy a function to Cloud Run, you have complete access and control over the function's behavior. For example, you can enable Direct VPC, configure GPUs, use volume mounts, and more.

The following table summarizes the configuration differences for functions:

| **Cloud Run functions** | **Cloud Run functions (1st gen)**  
---|---|---  
Request timeout | 

  * Up to 60 minutes for HTTP-triggered functions


  * Up to 9 minutes for event-driven functions created with the Cloud Functions v2 API

| 

  * Up to 9 minutes

  
Instance size | Up to 16 GiB RAM with 4 vCPU | Up to 8 GB RAM with 2 vCPU  
Concurrency | Up to 1000 concurrent requests per function instance | 1 concurrent request per function instance  
Traffic splitting | Supported | Not supported  
  
### Deployment

Since August 2024, you can use Cloud Run to deploy and manage functions created with the Cloud Functions v2 API. As a result of this change:

  * Function metadata such as runtime ID and build configurations are stored in the Cloud Run service definition.
  * You can safely edit your function using the Cloud Run Admin API.
  * You can rely on the Cloud Run service definition as the source of truth for your function.



However, note that functions created with the Cloud Run Admin API cannot be modified with the Cloud Functions API.

The following table summarizes the differences in how you create, deploy, edit, and manage functions:

| **Cloud Run functions** | **Cloud Run functions (1st gen)**  
---|---|---  
Google Cloud console | [Cloud Run](https://console.cloud.google.com/run) | [Cloud Run functions (1st gen)](https://console.cloud.google.com/functions)  
Cloud SDK | 

  * [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) for functions created with the Cloud Run Admin API or the Cloud Functions API.
  * [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) for functions created with the Cloud Functions API.

| 

  * [`gcloud functions deploy --no-gen2`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--gen2) for functions created with the Cloud Functions API.

  
REST API | 

  * [`run.googleapis.com`](https://docs.cloud.google.com/run/docs/reference/rest) (v1 and v2) for functions created with the Cloud Run Admin API or the Cloud Functions API.


  * [`cloudfunctions.googleapis.com`](https://docs.cloud.google.com/functions/docs/reference/rest) (v2 only) for functions created with the Cloud Functions API.

| 

  * [`cloudfunctions.googleapis.com`](https://docs.cloud.google.com/functions/docs/reference/rest) (v1 and v2)

  
Terraform  | 

  * [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) for functions created with the Cloud Run Admin API or the Cloud Functions API.


  * [`google_cloudfunctions2_function`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function) for functions created with the Cloud Functions API.

| 

  * [`cloudfunctions_function`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function)

  
  
#### Deploy functions created with the Cloud Functions v2 API

As described previously, you can use Cloud Run tools to deploy and manage functions created with the Cloud Functions v2 API. If you need to deploy your function using the Cloud Functions v2 API (for example, for backward compatibility), you can do so as follows:

  1. Make sure you have the [Cloud Functions Developer](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.developer) IAM role or a role that includes the same permissions. See also [Additional configuration for deployment](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

  2. Use the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command to deploy a function:
         
         gcloud functions deploy YOUR_FUNCTION_NAME \
            --region=YOUR_REGION \
            --runtime=YOUR_RUNTIME \
            --source=YOUR_SOURCE_LOCATION \
            --entry-point=YOUR_CODE_ENTRYPOINT \
            TRIGGER_FLAGS...
         

Replace the following:

     * YOUR_FUNCTION_NAME: the name of the function you want to deploy to. The function name must start with a letter followed by up to 62 letters, numbers, hyphens, or underscores, and must end with a letter or a number. The name of the Cloud Run service that is created for your function will replace underscores with hyphens and uppercase letters will be converted to lowercase. For example, `Function_1` will be given the name `function-1` in Cloud Run.

     * YOUR_REGION: the Google Cloud region where you want to deploy your function. For example, `europe-west1`.

     * YOUR_RUNTIME: the language your function uses. For a list of supported runtimes, see [Runtime support](https://docs.cloud.google.com/functions/docs/runtime-support).

     * YOUR_SOURCE_LOCATION: the location of your function source code.

     * YOUR_CODE_ENTRYPOINT: the entry point to your function in your source code. This is the code that will be executed when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For a complete reference on the `functions deploy` command and its flags, see the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) documentation.

### Triggers and retries

The following table compares triggers and retries for functions:

| **Cloud Run functions** | **Cloud Run functions (1st gen)**  
---|---|---  
Trigger and invoke a function | For function created with the Cloud Run Admin API, you [specify triggers as part of deploying the function](https://docs.cloud.google.com/run/docs/tips/function-retries) in the Google Cloud console or after deploying the function when using the gcloud CLI.  
  
For functions created with the Cloud Functions v2 API, you specify triggers as part of function deployment.  | You specify triggers as part of function deployment.  
Event types | [Support for any event type supported by Eventarc](https://docs.cloud.google.com/run/docs/function-triggers), including 90+ event sources through Cloud Audit Logs. | [Direct support for events from 7 sources](https://docs.cloud.google.com/functions/1stgendocs/calling#1st-gen-triggers).  
Retries | For functions created with the Cloud Run Admin API, update the [retry policy](https://docs.cloud.google.com/eventarc/docs/retry-events) in Eventarc and configure [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) in Pub/Sub.  
  
For functions created with the Cloud Functions v2 API, you specify retries as part of function deployment with the `--retry` flag.  | You specify retries as part of function deployment with the `--retry` flag.  
  
## Detach your function

Functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis) (for example, by using `gcloud functions`, the REST API, or Terraform) can be detached from its existing API environment. After you detach a function, you can only manage it using the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/cloud-run-admin-api-overview). You might want to do this if your workloads need to stay within the `run.googleapis.com` API boundary for [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview), or to ensure that your workloads use the [Cloud Run SKU](https://cloud.google.com/skus/sku-groups/cloud-run). See [Manage functions](https://docs.cloud.google.com/functions/docs/managing) to learn more.

## What's next

  * Try the getting started guide for [deploying a Cloud Run function](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
