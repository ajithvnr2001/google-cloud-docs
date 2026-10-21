---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/http/
title: HTTP triggers (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:35.542329+00:00
---

# HTTP triggers (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/http/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP triggers (1st gen)

In Cloud Run functions, an HTTP trigger enables a function to run in response to HTTP(S) requests. When you specify an HTTP trigger for a function, the function is assigned a URL at which it can receive requests. HTTP triggers support the `GET`, `POST`, `PUT`, `DELETE`, and `OPTIONS` request methods.

By default, requests to a function with an HTTP trigger require [authentication](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating). You can choose to allow unauthenticated calls during deployment. See [Allowing unauthenticated HTTP function invocation](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) for more information.

You use [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) to implement Cloud Run functions that can handle general HTTP(S) requests.

## Deployment

You can specify an HTTP trigger when you deploy a function. See [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy) for general instructions on how to deploy a function, and this section for additional information specific to configuring HTTP triggers during deployment.

###  gcloud 

If you are [deploying using the gcloud CLI](https://docs.cloud.google.com/functions/1stgendocs/deploy#gcloud), the flags shown here are used to configure HTTP triggers:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME \
    --no-gen2 \
    --trigger-http \
    [--allow-unauthenticated] \
    [--security-level=SECURITY_LEVEL] \
    ...
    

  * The [`--trigger-http`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-http) flag specifies that the function uses an HTTP trigger.
  * The [`--allow-unauthenticated`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--allow-unauthenticated) flag specifies that the function can be called without authentication. Omitting this flag means that calls to the function require authentication. See [Authenticating for invocation](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating) for more information.
  * The [`--security-level`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--security-level) flag controls whether the function endpoint requires HTTPS. The value `secure-always` means HTTPS is required and non-SSL HTTP requests are not supported. The value `secure-optional` means both HTTP and HTTPS are supported. The default is `secure-always`.



###  Console 

If you are [deploying using the Google Cloud console](https://docs.cloud.google.com/functions/1stgendocs/deploy#console), you can configure an HTTP trigger in the **Trigger** section:

  1. In the **Trigger type** field, select **HTTP**.
  2. In the **Authentication** field, select an option depending on whether you want to allow unauthenticated invocations of your function. By default, authentication is required. See [Authenticating for invocation](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating) for more information.
  3. Select or clear the **Require HTTPS** checkbox to control whether the function endpoint requires HTTPS. If deselected, both HTTP and HTTPS are supported.



## Function URL

After your function is deployed with an HTTP trigger, you can retrieve its assigned URL.

Cloud Run functions have assigned URLs that have the following format. These URLs have a deterministic format, meaning that you can predict what the URL will be before you deploy the function:
    
    
    https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME

You can retrieve your function's URL(s) as follows:

###  gcloud 
    
    
      gcloud functions describe YOUR_FUNCTION_NAME   
    
      --format="value(httpsTrigger.url)"
      

###  Console 

  1. Go to the Cloud Run functions overview page in the Google Cloud console:

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click the name of the function whose URL you want to retrieve.

  3. Click the Edit tab.

  4. View your function's URL in the **Trigger** section.




## Next steps

  * Learn how to [write HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions).
  * Learn how to [deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy).
  * See the [HTTP function tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/http-1st-gen) for an example of writing, deploying, and calling an HTTP function.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
