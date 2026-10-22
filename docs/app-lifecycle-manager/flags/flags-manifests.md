---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-manifests/
title: Use feature flag manifests \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:28.451167+00:00
---

# Use feature flag manifests  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-manifests/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Use feature flag manifests Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to create or export flags from an App Lifecycle Manager feature flag manifest.

App Lifecycle Manager feature flags let you control the availability and behavior of features within your applications without requiring new code deployments or infrastructure changes. Feature flag manifests let you create flags in groups, so you don't have to create and synchronize flags across your management plane and local development environment manually. Manifests provide a bulk management utility that lets you manage your flags using JSON files that conform to the [open-source OpenFeature flag manifest schema](https://openfeature.dev/docs/tutorials/open-feature-cli/#flag-manifest-structure).

## Prerequisites

Before you begin, ensure you have:

  1. A `gcloud` environment configured to manage App Lifecycle Manager resources.
  2. Completed the [Deploy feature flags quickstart](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-quickstart).



## Create flags from a manifest

The `push` command lets you create multiple flags at once by providing a local JSON manifest file. 

  1. Create a file named `my_flags.json` with your flag definitions. This file serves as the local source of truth for your manifest.

Example `my_flags.json`:
         
         {
           "flags": {
             "my-flag": {
               "defaultValue": "foo-bar",
               "description": "A description of the flag.",
               "flagType": "string"
             }
           }
         }
         

     1. Run the `push` command specifying your manifest file and the targeted `UnitKind`.
    
    gcloud beta app-lifecycle-manager flags push \
        --file="my_flags.json" \
        --unit-kind="UNIT_KIND_NAME"
    

**Note:** The `push` command is additive--this means it can create flags, but won't update or delete existing flags in the management plane.



## Create a manifest from existing flag configurations

The `pull` command fetches existing flag configurations from the App Lifecycle Manager API and generates a local JSON manifest file. This lets you maintain a local record of your flags or prepare them for use with OpenFeature codegen tools.

  1. Run the `pull` command specifying your chosen output path.
         
         gcloud beta app-lifecycle-manager flags pull \
              --output-file="manifest.json" \
              --unit-kind="UNIT_KIND_NAME" \
              --overwrite-output-file
         

  2. If you are using type-safe flag accessors, run the OpenFeature CLI codegen utility against the new `manifest.json` to update your application's type-safe flag accessors. This ensures the manifests match the keys and types in the management plane.




## What's next

  * Learn about [Complex Targeting with CEL](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-targeting).
  * Learn about [Multi-Tenant Architecture](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-multi-tenant).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
