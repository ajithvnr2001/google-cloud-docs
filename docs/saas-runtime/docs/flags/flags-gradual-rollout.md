---
url: https://docs.cloud.google.com/saas-runtime/docs/flags/flags-gradual-rollout/
title: Use gradual feature rollouts \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:25:37.124644+00:00
---

# Use gradual feature rollouts  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/flags/flags-gradual-rollout/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Use gradual feature rollouts Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to configure and execute a gradual feature rollout using App Lifecycle Manager feature flags. You'll learn how to define targeting attributes, configure percentage-based allocations, and execute a progressive rollout safely.

We will use a scenario where you want to enable an `enhanced-search` algorithm for only 1% of your traffic, randomized by the attribute `userID`, while the remaining 99% continue using standard search.

## Prerequisites

Before you begin, ensure you have completed one of the standard quickstarts to provision your baseline infrastructure or standalone feature flag resources:

  * [Quickstart: Deploy feature flags with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart)
  * [Quickstart: Use feature flags Standalone](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-standalone-quickstart)



## Integrate the flag in your application

To support percentage-based allocations driven by user data, your application must attach the attribute value (e.g., `userID`) to the OpenFeature Evaluation Context at runtime before calling the evaluation method.

The following examples demonstrate how to retrieve the initialized client and evaluate the flag with targeting context attached.

```go import ( "context" "fmt" "log"
    
    
    "github.com/open-feature/go-sdk/pkg/openfeature"
    

)

// Example userID - in a real application, this would come from the request context. var userID = "example-user-123"

// 1. Get client client := openfeature.NewClient("simple-api")

// 2. Create Evaluation Context with user data evalCtx := openfeature.NewEvaluationContext( userID, map[string]interface{}{ "userID": userID, // Ensure userID is passed dynamically }, )

// 3. Evaluate flag (defaults to false if unreachable) isEnhanced, err := client.BooleanValue(context.Background(), "enhanced-search", false, evalCtx) if err != nil { log.Printf("Flag evaluation failed: %v", err) }

// 4. Execute business logic if isEnhanced { log.Printf("Enhanced search algorithm for user %s", userID) } else { log.Printf("Standard search algorithm for user %s", userID) } `</devsite-tab> <devsite-tab title="Java">`java // 1. Get client var client = OpenFeatureAPI.getInstance().getClient("simple-api");

// 2. Create Evaluation Context with user data var context = new dev.openfeature.sdk.MutableContext(); context.add("userID", userID); 

// 3. Evaluate flag boolean isEnhanced = client.getBooleanValue("enhanced-search", false, context);

// 4. Execute business logic if (isEnhanced) { System.out.println("Executing enhanced search algorithm..."); } else { System.out.println("Executing standard search algorithm..."); } `</devsite-tab> <devsite-tab title="Python">`python import openfeature from openfeature.evaluation_context import EvaluationContext

# 1\. Get client

client = openfeature.api.get_client()

# 2\. Create Evaluation Context with user data

eval_ctx = EvaluationContext( targeting_key=str(user_id), attributes={ "userID": user_id,  
} )

# 3\. Evaluate flag

is_enhanced = client.get_boolean_value( "enhanced-search", False, eval_ctx )

# 4\. Execute business logic

if is_enhanced: print(f"Executing enhanced search for user {user_id}") else: print(f"Executing standard search for user {user_id}") ``` 

## Configure flag behavior

Define the randomized attribute parameter and associate it with a percentage-based allocation rule on the feature flag resource.

  1. **Create the targeting attribute:** Define the `userID` attribute resource globally to register it for targeting evaluation.
         
         gcloud beta app-lifecycle-manager flags attributes create "user-id-attr" \
           --key="userID" \
           --attribute-value-type="STRING" \
           --location="global"
         

  2. **Define the flag allocation rule:** Construct the feature flag resource to assign 1% weight to the `enabled` variant randomized on `userID`.
         
         gcloud beta app-lifecycle-manager flags create "enhanced-search" \
           --key="enhanced-search" \
           --flag-value-type=BOOL \
           --location="global" \
           --unit-kind="demo-test-unitKind" \
           --variants='[ { "id": "Enabled", "booleanValue": true }, { "id": "Disabled", "booleanValue": false } ]' \
           --evaluation-spec='{
             "allocations": [{
               "id": "percentage-rollout",
               "randomizedOn": "userID",
               "slots": [
                 {"variant": "enabled", "weight": 1},
                 {"variant": "disabled", "weight": 99}
               ]
             }],
             "defaultTarget": "percentage-rollout",
             "attributes": ["projects/PROJECT_ID/locations/global/flagAttributes/user-id-attr"]
           }' \
         




## Create a flag configuration rollout

To distribute the newly created gradual allocation rule safely, progress through the standard immutable rollout phases.

  1. **Create a revision:** Capture a snapshot of the 1% allocation configuration.
         
         gcloud beta app-lifecycle-manager flags revisions create "enhanced-search-rev-1" \
            --location="global" \
            --flag="enhanced-search"
         

  2. **Create a release:** Package the revision for deployment against your unit kinds.
         
         gcloud beta app-lifecycle-manager flags releases create "release-of-enhanced-search" \
            --location="global" \
            --unit-kind="demo-test-unitkind" \
            --flag-revisions="enhanced-search-rev-1"
         

  3. **Initiate the rollout:** Define your orchestration strategy and deploy the configuration.
         
         gcloud beta app-lifecycle-manager rollout-kinds create "rollout-kind-of-enhanced-search" \
            --unit-kind="demo-test-unikind" \
            --rollout-orchestration-strategy="Google.Cloud.Simple.AllAtOnce" \
            --location="global"
         
         gcloud beta app-lifecycle-manager rollouts create "rollout-of-enhanced-search" \
            --flag-release="release-of-enhanced-search" \
            --rollout-kind="rollout-kind-of-enhanced-search" \
            --location="global"
         

  4. **Monitor the rollout:** Confirm the deployment reaches a `SUCCEEDED` state.
         
         gcloud beta app-lifecycle-manager rollouts describe "rollout-of-enhanced-search" \
            --location="global"
         




## Update flag targeting

Once the 1% rollout is deemed successful and stable, expand the rollout percentage audience by updating the flag's internal allocation weight (e.g., to 50%).

  1. **Update the flag specification:** Change the allocation slots to 50% enabled and 50% disabled.
         
         gcloud beta app-lifecycle-manager flags update "enhanced-search" \
           --evaluation-spec='{
             "allocations": [{
               "id": "percentage-rollout",
               "randomizedOn": "userID",
               "slots": [
                 {"variant": "enabled", "weight": 50},
                 {"variant": "disabled", "weight": 50}
               ]
             }],
             "defaultTarget": "percentage-rollout",
             "attributes": ["projects/PROJECT_ID/locations/global/flagAttributes/user-id-attr"]
           }'
         

  2. **Deploy the expansion:** Follow the lifecycle to distribute the updated weight to connected clients.
         
         gcloud beta app-lifecycle-manager flags revisions create "enhanced-search-rev-2" \
            --location="global" \
            --flag="enhanced-search"
         
         gcloud beta app-lifecycle-manager flags releases create "enhanced-search-50pct" \
            --location="global" \
            --unit-kind="demo-test-unitkind" \
            --flag-revisions="enhanced-search-rev-2"
         
         gcloud beta app-lifecycle-manager rollouts create "rollout-of-enhanced-search-50pct" \
            --flag-release="enhanced-search-50pct" \
            --rollout-kind="rollout-kind-of-enhanced-search" \
            --location="global"
         

This operation can be repeated continuously until the feature reaches 100% deployment.




## Decommission a flag

**Warning:** The `gcloud beta app-lifecycle-manager flags releases create "obsolete-enhanced-search" --all-flags` command doesn't remove or detach flags from units or unit kinds. Use this call as a workaround:
    
    
    curl --request POST
    "https://saasservicemgmt.googleapis.com/v1beta1/projects/PROJECT_ID/locations/global/flagReleases?flagReleaseId=obsolete-enhanced-search"
    --header "Authorization: Bearer $(gcloud auth application-default print-access-token)"
    --header "Content-Type: application/json"
    --header "Accept: application/json"
    --data "{ "unitKind": "projects/PROJECT_ID/locations/global/unitKinds/UNIT_KIND_ID", "obsoleteFlags": ["projects/PROJECT_ID/locations/global/flags/enhanced-search"] }"
    

Once a feature flag completes its rollout and serves as standard operational behavior, it must be safely decommissioned.

  1. **Remove from application:** Remove all flag evaluation conditional logic from your application codebase and deploy the updated payload to production.
  2. **Mark for cleanup:** Set the flag state to `CLEANUP` to explicitly signal intent to deprovision it.
  3. **Deploy final rollout:** Execute a final rollout to make the backend configuration explicitly unavailable, after which you can securely delete the flag and revision metadata from the management plane.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
