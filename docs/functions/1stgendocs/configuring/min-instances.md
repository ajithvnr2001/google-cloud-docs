---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/min-instances/
title: Configure minimum instances (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.575991+00:00
---

# Configure minimum instances (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/min-instances/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure minimum instances (1st gen)

You can avoid cold starts for your application and reduce application latency by setting a minimum number of instances.

Cloud Run functions scales by creating new instances of your function. Each of these instances can handle only one request at a time, so large spikes in request volume often cause longer wait times as new instances are created to handle the demand.

Because functions are stateless, your function sometimes initializes the execution environment from scratch, which is called a _cold start_. Cold starts can take significant amounts of time to complete, so we recommend setting a minimum number of Cloud Run functions instances if your application is latency-sensitive.

**Note:** Setting a minimum number of instances incurs cost. For details, see the [Pricing](https://cloud.google.com/functions/pricing) page.

### Idle instances and cold starts

To minimize the impact of [cold starts](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#cold-starts), Cloud Run functions attempts to keep function instances idle for an unspecified amount of time after handling a request. During this idle time, resources such as open database connections might be persisted in case another request needs to be handled. Instances kept idle in this way count toward the maximum instances limit for your function, but you are not billed for this idle time.

This built-in behavior might not be sufficient for your application, particularly if it is latency-sensitive. Explicitly setting a minimum number of instances can further help you avoid cold starts and reduce application latency.

Note that when instances are kept idle because a minimum number of instances has been set, these instances are not considered active unless they have served traffic recently. For example, this means that if a function has not recently served traffic, the "Active Instances" metric may show no instances are active, even if a value for minimum instances has been set.

Note also that when you set a minimum number of instances, you _are_ billed for the idle time of those instances—see [Pricing](https://cloud.google.com/functions/pricing).

## Setting and clearing minimum instance limits

You can set a minimum number of instances for a function during deployment. Each function has its own minimum instances setting.

### Setting minimum instance limits

You can set a minimum instance limit using either the Google Cloud CLI or the Google Cloud console.

###  Console 

To set a minimum instance limit for a new function:

  1. To create a new function, go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click **Create function**.

  3. Fill in the required fields for your function.

  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.

  5. In the **Minimum number of instances** field in the **Autoscaling** section, enter a number greater than or equal to 1.

  6. Click **Next**.

  7. Click **Deploy**.




To set a minimum instance limit for an existing function:

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of an existing function to be taken to its **Function details** page.

  3. Click **Edit**.

  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.

  5. In the **Minimum number of instances** field in the **Autoscaling** section, enter a number greater than or equal to 1.

  6. Click **Next**.

  7. Click **Deploy**.




###  gcloud 

To set a minimum instance limit, run the following command:
    
    
    gcloud functions deploy FUNCTION_NAME \
    --no-gen2 \
    --min-instances MIN_INSTANCE_LIMIT
    

Replace the following:

  * FUNCTION_NAME: The name of your function.

  * MIN_INSTANCE_LIMIT: The number to set as the minimum instance limit, cannot exceed 1000.




The function's minimum instance limit is set.

### Clearing minimum instance limits

You can clear or remove a minimum instance limit using either the Google Cloud CLI or the Google Cloud console.

###  Console 

To clear a function's minimum instance limit:

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of an existing function to be taken to its **Function details** page.

  3. Click **Edit**.

  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.

  5. In the **Minimum number of instances** field in the **Autoscaling** section, enter 0.

  6. Click **Next**.

  7. Click **Deploy**.




###  gcloud 

Use the `--clear-min-instances` flag at deploy time:
    
    
    gcloud functions deploy FUNCTION_NAME --clear-min-instances
    

The function's minimum instance limit is cleared.

## Getting recommendations to set minimum instances

The [Recommender service](https://docs.cloud.google.com/functions/1stgendocs/configuring/recommender) automatically supplies recommendations for deployed functions that could benefit from having minimum instances set.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
