---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant/
title: Use feature flags for multi-tenant architecture \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:36:06.635727+00:00
---

# Use feature flags for multi-tenant architecture  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Use feature flags for multi-tenant architecture Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to implement App Lifecycle Manager feature flags in a multi-tenant environment without modifying your existing binary deployment process.

## Prerequisites

Before you begin, ensure you have:

  1. Completed the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart).
  2. A `gcloud` environment configured to manage App Lifecycle Manager resources.
  3. An existing App offering. For more information about how to create an App offering, see [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).



## Resource modeling

In a multi-tenant setup, we recommend that you define a unit kind for your service or application, and a unit for every _instance of the service or application_ (representing a tenant or deployment). 

To implement feature flags in a multi-tenant environment, define Common Expression Language (CEL) attributes that identify your tenants, configure your application to inject tenant identifiers at runtime, and use evaluation rules to affect features for specific tenants.

For simpler cases, you can also manually create separate rollouts for each customer.

### 1\. Create App offering (if not already done)
    
    
    gcloud beta app-lifecycle-manager saas create "SAAS_NAME" \
        --project="PROJECT_ID" \
        --location="global" \
        --locations=name="LOCATION_1"
    

### 2\. Create UnitKind
    
    
    gcloud beta app-lifecycle-manager unit-kinds create "tenant-service-kind" \
        --project="PROJECT_ID" \
        --location="global" \
        --saas="SAAS_NAME"
    

### 3\. Create units for tenants

When creating units, use **Labels** to categorize tenant services into groups (e.g., `group=beta`, `group=preview`, `group=all`).
    
    
    # Create a unit for Tenant A (Beta group)
    gcloud beta app-lifecycle-manager units create "tenant-a-service" \
        --unit-kind="tenant-service-kind" \
        --location="LOCATION_1" \
        --labels="group=beta"
    
    # Create a unit for Tenant B (Standard group)
    gcloud beta app-lifecycle-manager units create "tenant-b-service" \
        --unit-kind="tenant-service-kind" \
        --location="LOCATION_1" \
        --labels="group=all"
    

## Define attributes and flags

You must formally define attributes (like `customerID`) to ensure type safety in evaluation rules.

### 1\. Create the customerID attribute
    
    
    gcloud beta app-lifecycle-manager flags attributes create "customer-id-attr" \
        --key="customerID" \
        --attribute-value-type="STRING" \
        --location=global
    

### 2\. Create the feature flag
    
    
    gcloud beta app-lifecycle-manager flags create "enhanced-search" \
        --key="enhanced-search" \
        --flag-value-type=BOOL \
        --unit-kind="tenant-service-kind"
    

## Application integration

Integrate the OpenFeature SDK into your service. Your application must inject the `customerID` into the context at runtime.

### Go Example:
    
    
    // Inject customerID into the evaluation context
    evalCtx := map[string]any{
        "customerID": currentTenant.ID,
    }
    
    // Evaluate the flag
    isEnabled, err := client.BooleanValue(
        context.Background(),
        "enhanced-search",
        false,
        evalCtx,
    )
    

## Configure tenant-specific targeting

Use evaluation rules to enable a feature for specific customers.
    
    
    gcloud beta app-lifecycle-manager flags update "enhanced-search" \
        --location="global"
        --evaluation-spec='{
          "rules": [{
            "id": "allowlist-for-premium-tenants",
            "condition": "customerID in [\"tenant-xyz-123\", \"tenant-abc-789\"]",
            "target": "Enabled"
          }],
          "defaultTarget": "Disabled",
          "attributes": ["projects/PROJECT_ID/locations/global/flagAttributes/customer-id-attr"]
        }'
    

## Manual gradual rollout with filters

For simpler use cases, you can emulate waves by triggering separate rollouts manually for each customer label.

### 1\. Create revision and release
    
    
    # Create a Revision (Snapshot)
    gcloud beta app-lifecycle-manager flags revisions create "enhanced-search-rev-1" \
        --location=global \
        --flag="enhanced-search"
    
    # Create a Release
    gcloud beta app-lifecycle-manager flags releases create "release-of-enhanced-search" \
        --location=global \
        --unit-kind="tenant-service-kind" \
        --revisions="enhanced-search-rev-1"
    

### 2\. Trigger manual rollouts

You can manually orchestrate the rollout by triggering separate operations per target group using `--unit-filter`.
    
    
    # Rollout to Beta group first
    gcloud beta app-lifecycle-manager rollouts create "beta-rollout" \
        --flag-release="release-of-enhanced-search" \
        --rollout-kind="rollout-kind-of-enhanced-search" \
        --location=global \
        --rollout-orchestration-strategy="Google.Cloud.Simple.AllAtOnce" \
        --unit-filter="labels.group == beta"
    
    # After verification, rollout to the rest of the fleet
    gcloud beta app-lifecycle-manager rollouts create "full-rollout" \
        --flag-release="release-of-enhanced-search" \
        --rollout-kind="rollout-kind-of-enhanced-search" \
        --location=global \
        --rollout-orchestration-strategy="Google.Cloud.Production" \
        --unit-filter="labels.group == all"
    

## What's next

  * Learn about [Experimentation and A/B Testing](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-experimentation).
  * Learn about [Troubleshooting](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
