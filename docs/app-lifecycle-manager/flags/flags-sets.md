---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-sets/
title: Use flag sets \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:59.983451+00:00
---

# Use flag sets  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-sets/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Use flag sets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to group flags, create releases from sets, and configure flags to subscribe to [flag sets](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-sets).

Flag sets are logical containers for managing groups of related feature flags. As your applications grow and the number of individual flags increases, managing them in a flat list can become cumbersome and error-prone.

Flag sets allow you to organize flags based on functional area, application component, or any other logical criteria, providing a higher-level abstraction for flag operations.

## Prerequisites

Before you begin, ensure you have:

  1. A `gcloud` environment configured to manage App Lifecycle Manager resources.
  2. Completed the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart).



## Group feature flags

To group flags, you associate them with a `flag_set` identifier during creation, or update an existing flag. This identifier creates a clear boundary of ownership and lets you use the flags set as a single resource. 

### Create a flag in a flag set
    
    
    gcloud beta app-lifecycle-manager flags create "auth-flag" \
        --key="auth-flag" \
        --flag-value-type=BOOL \
        --location=global \
        --flag-set="auth-module-flags" \
        --description="Flag for the core authentication service."
    

### Update an existing flag to add to a flag set
    
    
    gcloud beta app-lifecycle-manager flags update "auth-flag" \
        --location="global"
        --flag-set="auth-module-flags"
    

## Create a release from a flag set

Instead of manually creating point-in-time snapshots (`FlagRevisions`) for every flag, you can create a `FlagRelease` that references one or more sets. App Lifecycle Manager automatically handles the creation of all necessary immutable snapshots.
    
    
    gcloud beta app-lifecycle-manager flags releases create "auth-release-v1.2" \
        --location=global \
        --flag-sets='["auth-module-flags"]' \
        --unit-kind="UNIT_KIND_NAME"
    

Replace `UNIT_KIND_NAME` with your unit kind.

### Create a release for all flags

You can set the `all_flags` boolean to `true` to fetch all flags linked to the rollout's unit kind:
    
    
    gcloud beta app-lifecycle-manager flags releases create "all-flags-release" \
        --location=global \
        --all-flags \
        --unit-kind="UNIT_KIND_NAME"
    

## Consuming a flag set

To subscribe to a flag set, use a selector when you initialize the OpenFeature provider.

### Go example:

The selector tells the flag source to filter for this specific set:
    
    
    provider := flagd.NewProvider(
        // The selector tells the flag source to filter for this specific set
        flagd.WithSelector("flagSetId=auth-module-flags"),
        // ... other options
    )
    

Selector Behavior:

  * **Empty selector** : Selects only flags that have no flag set ID.
  * **`flagSetId=*`** : Selects all flags associated with the unit.
  * **`flagSetId=X`** : Selects only flags where the set is exactly `X`.



## What's next

  * Learn about [Complex Targeting with CEL](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-targeting).
  * Learn about [Multi-Tenant Architecture](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
