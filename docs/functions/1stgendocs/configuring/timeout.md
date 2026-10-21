---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/timeout/
title: Function timeout (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.307501+00:00
---

# Function timeout (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/timeout/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Function timeout (1st gen)

If a function runs for too long, the system takes steps to terminate or throttle it. This timeout period defaults to 60 seconds, but you can extend or reduce it when you deploy the function. The maximum timeout duration is nine minutes (540 seconds).

When function execution reaches its timeout, a response message with an HTTP error status, generally 408, is immediately returned to the caller; function execution is halted.

## Set a timeout duration

You can set a function's timeout duration at deployment using the Google Cloud CLI or the Google Cloud console.

###  gcloud 

If you are deploying using the gcloud CLI, use the [`--timeout`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--timeout) flag:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME --no-gen2 --timeout=TIMEOUT_DURATION ...
    

To edit an existing timeout duration with Google Cloud CLI, redeploy the function with a new timeout value.

###  Console 

To set the timeout duration during function creation in the Google Cloud console:

  1. Go to the [Cloud Run functions Overview page](https://console.cloud.google.com/functions/list) in the Google Cloud console.
  2. Click **Create function**.
  3. Fill in the required fields for your function.
  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.
  5. In the **Timeout** field, enter a number of seconds.

To edit an existing timeout duration in Google Cloud console, on the functions overview page click the name of the function to go to its details page. On the details page click **Edit** , expand the **Runtime, build...** section, and click the **Runtime** tab, where you can directly edit the value in the **Timeout** field.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
