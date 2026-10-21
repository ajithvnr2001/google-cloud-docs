---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/max-instances/
title: Configure maximum instances (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:39.364489+00:00
---

# Configure maximum instances (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/max-instances/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure maximum instances (1st gen)

You can control the scaling behavior of your function by setting a maximum number of Cloud Run functions instances. Setting maximum instances controls cost and prevents downstream resources from being overwhelmed with traffic.

Cloud Run functions scales by creating new instances of your function. Each of these instances can handle only one request at a time, so large spikes in request volume might result in creating many instances.

Automatic scaling is beneficial most of the time, but in some cases you might want to limit the total number of instances that can exist at any given time. For example, your function might interact with a database that can only handle a certain number of open connections.

## Setting and clearing maximum instances limits

You can set a maximum number of instances for a function during deployment. Each function has its own maximum instances setting. Functions scale independently of each other.

### Setting maximum instances limits

You can set a maximum instances limit using either the Google Cloud CLI or the Google Cloud console. If you don't specify a limit, Cloud Run functions sets a default of 3000.

To set a maximum instances limit:

###  Console 

  1. Go to the [Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click **Create function**.

  3. Fill in the required fields for your function.

  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.

  5. In the **Maximum number of instances** field in the **Autoscaling** section, enter a value or use the default.




###  gcloud 

To set a maximum instances limit, run the `deploy` command with the `--max-instances` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --max-instances MAX_INSTANCE_LIMIT

Replace the following:

  * FUNCTION_NAME: The name of the function.

  * MAX_INSTANCE_LIMIT: The number to set as the maximum instances limit - for example, 3000.




### Clearing maximum instances limits

You can clear a maximum instances limit for a function using either the `gcloud` command-line tool or the Google Cloud console.

###  Console 

To clear a maximum instances limit for a function:

  1. Go to the [Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click an existing function to go to its details page. You can see the function's current maximum instances limit in the **Details** tab.

  3. Click **Edit**.

  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.

  5. In the **Maximum number of instances** field in the **Autoscaling** section, enter `0`.




###  gcloud 

To clear a maximum instances limit for a function, run the `deploy` command with the `--clear-max-instances` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --clear-max-instances

## Limits & best practices

This section provides guidelines for using maximum instances.

### Choose a maximum instance value

The optimal value for the maximum instances setting depends on your function's characteristics, including how long an invocation takes to execute, its expected average and peak invocation frequency, and your application's tolerance for invocation failures. A good rule of thumb is to start with a maximum instances value of 3, then monitor for invocation failures and adjust the maximum instances value upward as necessary.

### Guard against excessive scale-ups

When no maximum instances limit is specified, Cloud Run functions favors _scaling up to meet demand_ over limiting throughput. This means that the number of simultaneous instances that your function might have is effectively unlimited unless you've configured such a limit.

We recommend assigning a `--max-instances` limit to any functions that send requests to throughput-constrained or otherwise unscalable downstream services. A maximum instances limit improves overall system stability and helps guard against abnormally high request levels.

### Request handling when all instances are busy

Under normal circumstances, your function scales up by creating new instances to handle incoming traffic load. But when you have set a maximum instances limit, you might encounter a scenario where there are insufficient instances to meet incoming traffic load.

In that scenario, Cloud Run functions attempts to serve a new inbound request for up to 30 seconds:

  * If an instance finishes processing its request during this time period, it might start to process the new inbound request.
  * If no instance becomes available, the request will fail.



Requests sent to overloaded [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) fail with a response code of

  * `429 Too Many Requests` if a maximum instances value is configured, or
  * `500 Internal Server Error` if no maximum instances value is configured



Events destined for event-driven functions will automatically be saved until capacity is available.

### Max instances limits that exceed Cloud Run functions scaling ability

When you specify a maximum instances limit, you are specifying an upper limit. Setting a large limit does not mean that your function will scale up to the specified number of instances. It only means that the number of instances that co-exist at any point in time shouldn't exceed the limit.

Further, setting a maximum instances limit might affect the scaling strategies that Cloud Run functions uses to meet your traffic demand. In general, Cloud Run functions will prioritize honoring your specified limit rather than scaling up and potentially exceeding your limit.

### Handling traffic spikes

In some cases, such as rapid traffic surges, Cloud Run functions might, for a short period of time, create more instances than the specified maximum instances limit. If your function cannot tolerate this temporary behavior, you might want to factor in a safety margin and set a lower maximum instances value than your function can tolerate.

### Deployments

When you deploy a new version of your function, Cloud Run functions migrates traffic from the earlier version to the new one. Because maximum instances limits are set for each version of your function independently, you might temporarily exceed the specified limit during the period after deployment.

For example, a function might have a maximum instances limit of 5. Under normal circumstances, the function scales up to 5 instances as it handles requests. When a new version of the function is deployed, the new version has its own max instances limit of 5.

Requests that are already being handled by the previous version of the function are not interrupted when a new version of the function is deployed. Instead, these requests will continue to make progress. New inbound requests will be handled by the newly-deployed version of the function.

Thus, the function in the previous example might have up to 10 total instances (5 for each version of your function) during the period after deploying the new version. The amount of time required for instances of the previous function to terminate depends on the time required for those instances to finish handling any active requests. This is an additional factor to take into account when selecting an appropriate max instances limit.

### Clearing maximum instances limits

Setting maximum instances for a function to 0 clears the function's existing maximum instances limit but does not pause your function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
