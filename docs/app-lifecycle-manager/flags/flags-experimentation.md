---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-experimentation/
title: Configure experimentation and A/B testing using feature flags \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:46.858995+00:00
---

# Configure experimentation and A/B testing using feature flags  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-experimentation/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Configure experimentation and A/B testing using feature flags Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Lifecycle Manager feature flag allocations help you to test your application by splitting traffic percentages. This lets some of your users see one variant of your application, while other users see a different variant, helping you determine which variants or features are more successful (this process is often referred to as _A/B testing_). Feature flag allocations help you define how to split your traffic, and integrate allocated variants with your application.

This guide shows you how to define variants, configure traffic splitting, and integrate variants with your application.

To simplify tracking and analysis, you should assign descriptive string IDs to your variants (e.g., "experimental" and "baseline") and use these names directly in your code and analysis pipelines.

## Prerequisites

Before you begin, ensure you have:

  1. Completed the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart) or [Use feature flags (standalone quickstart)](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart).
  2. A Google Cloud CLI environment configured to manage App Lifecycle Manager resources.



## Configure a feature flag allocation

To configure an experimental feature flag: 

  1. Define the randomized attribute (e.g., `userID`) which will be used for sticky bucketing to ensure a consistent experience for each user.
         
         gcloud beta app-lifecycle-manager flags attributes create "user-id-attr" \
               --key="userID" \
               --attribute-value-type="STRING" \
               --location=global
         

  2. Use an allocation to define the split (50/50, for example), referencing your descriptive variant IDs.
         
         # Create a flag with explicitly named variants for the experiment and a 50/50 allocation referencing the custom IDs
         gcloud beta app-lifecycle-manager flags create "search-algo-test" \
           --key="search-algo-test" \
           --flag-value-type=BOOL \
           --location="global" \
           --unit-kind="demo-test-unitkind" \
           --variants='[
               {
               "id": "experimental",
               "booleanValue": true
               },
               {
               "id": "baseline",
               "booleanValue": false
               }
           ]'\
           --evaluation-spec='{
               "allocations": [{
                   "id": "search-split-50-50",
                   "randomizedOn": "userID",
                   "slots": [
                   {"variant": "baseline", "weight": 50},
                   {"variant": "experimental", "weight": 50}
                   ]
               }],
               "defaultTarget": "search-split-50-50",
               "attributes": ["projects/PROJECT_ID/locations/global/flagAttributes/user-id-attr"]
           }'
         

  3. In your backend service, initialize the OpenFeature SDK and inject the `userID` into the evaluation context. Use the `BooleanValueDetails` (or equivalent for your language) method to retrieve the `variantID` (string) in your application. This lets you switch your backend logic based on the descriptive name rather than only a boolean value.
         
         // 1. Prepare evaluation context
         evalCtx := map[string]any{"userID": currentUser.ID}
         
         // 2. Fetch evaluation details to get the variant name
         details, err := client.BooleanValueDetails(ctx, "search-algo-test", false, evalCtx)
         
         // 3. Execute logic based on the Variant ID (string name)
         if details.Variant == "experimental" {
             results = search.ExperimentalV2(query)
         } else {
             results = search.BaselineV1(query)
         }
         

  4. Use descriptive variant names so that your auditing and analysis generate documentation automatically. To audit evaluations, log the `details.Variant` string alongside your performance metrics:
         
         startTime := time.Now()
          // ... perform search ...
          duration := time.Since(startTime)
         
          // Audit: Log the descriptive variant name ("experimental" or "baseline")
          logger.Info("Search performed",
             "variant", details.Variant,
             "latency_ms", duration.Milliseconds(),
          )
         

By comparing metrics for the "Experimental" group versus the "Baseline" group, you can manually analyze whether the new algorithm improves backend efficiency or search relevance before proceeding with a full rollout.




## What's next

  * Learn about [Troubleshooting](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
