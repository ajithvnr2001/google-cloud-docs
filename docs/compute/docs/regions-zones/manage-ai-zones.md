---
url: https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones/
title: Manage AI zone visibility \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:11.208092+00:00
---

# Manage AI zone visibility  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage AI zone visibility Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to check if AI zones are visible for your Google Cloud project, and how to turn AI zone visibility on or off. 

AI zones are specialized zones optimized for artificial intelligence (AI) and machine learning (ML) training and inference workloads. To help your team discover and use AI zones in your Google Cloud project, turn on _AI zone visibility_. AI zone visibility determines whether Google Cloud displays AI zones in your project's zone listings and console interfaces. If you turn off AI zone visibility, then Google Cloud hides AI zones from the following interfaces:

  * Google Cloud console
  * Google Cloud CLI zone listing commands
  * REST API



If the parent region is active in your project, then turning off AI zone visibility doesn't restrict API endpoints or block regional platform settings in the background, such as `compute.InstanceSettings`. To prevent creation of resources in AI zones, see Restrict resource creation in AI zones.

To learn more about AI zones, read the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) documentation.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to turn on or turn off AI zone visibility, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Check if AI zones are visible for a project

To check if AI zones are visible for your Google Cloud project, verify whether or not the feature `ai-zones-visibility` ([Preview](https://cloud.google.com/products#product-launch-stages)) is turned on for your Google Cloud project. For new Google Cloud projects, AI zone visibility is turned off by default.

###  Google Cloud CLI 

Use the [`gcloud compute preview-features list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/preview-features/list). The response that you get indicates if the feature `ai-zones-visibility` is turned on or turned off.
    
    
    gcloud compute preview-features list --filter="name=ai-zones-visibility"
    

###  REST 

Make the following `GET` request to the [`previewFeatures.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/previewFeatures/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/previewFeatures/ai-zones-visibility
    

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Make AI zones visible for a project

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To make AI zones visible for your Google Cloud project, turn on AI zone visibility for your project.

###  Google Cloud CLI 

Use the [`gcloud compute preview-features` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/preview-features/update), setting the activation status as `enabled` and the rollout plan as `fast-rollout`.
    
    
    gcloud compute preview-features update ai-zones-visibility \
        --activation-status=enabled \
        --rollout-plan=fast-rollout
    

###  REST 

Make the following `PATCH` request to the [`previewFeatures.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/previewFeatures/update). In the request body, include the following fields:

  * The `activation_status` field, set to `ENABLED`.
  * The `rollout_operation.predefined_rollout_plan` field, set to `ROLLOUT_PLAN_FAST_ROLLOUT`.


    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/previewFeatures/ai-zones-visibility
    {
      "activation_status": "ENABLED",
      "rollout_operation": {
        "rollout_input": {
          "predefined_rollout_plan": "ROLLOUT_PLAN_FAST_ROLLOUT"
        }
      }
    }
    

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Hide AI zones for your project

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To hide AI zones from your Google Cloud project's zone listings and console deployment interfaces, turn off AI zone visibility.

**Caution:** Turning off AI zone visibility hides AI zones from zone listing commands, but it doesn't block actual usage of AI zones, such as direct API calls that specify an AI zone or regional services (such as regional managed instance groups) that automatically manage resources across all zones in the parent region. To prevent creation of resources in AI zones, see Restrict resource creation in AI zones.

###  Google Cloud CLI 

Use the [`gcloud compute preview-features` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/preview-features/update), setting the activation status as `unspecified` and the rollout plan as `fast-rollout`.
    
    
    gcloud compute preview-features update ai-zones-visibility \
        --activation-status=unspecified \
        --rollout-plan=fast-rollout
    

###  REST 

Make the following `PATCH` request to the [`previewFeatures.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/previewFeatures/update). In the request body, include the following fields:

  * The `activation_status` field, set to `ACTIVATION_STATE_UNSPECIFIED`.
  * The `rollout_operation.predefined_rollout_plan` field, set to `ROLLOUT_PLAN_FAST_ROLLOUT`.


    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/previewFeatures/ai-zones-visibility
    {
      "activation_status": "ACTIVATION_STATE_UNSPECIFIED",
      "rollout_operation": {
        "rollout_input": {
          "predefined_rollout_plan": "ROLLOUT_PLAN_FAST_ROLLOUT"
        }
      }
    }
    

Replace `PROJECT_ID` with your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

### Restrict resource creation in AI zones

If your organization has data residency, compliance, or governance requirements mandating that no resources or system configurations exist in AI zones, use Organization Policy Service to restrict resource creation in AI zones. For more information, see [Restrict resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

**Note:** If your Google Cloud project allows a region group that contains AI zones, such as `in:europe-west4-locations` or `in:us-central1-locations`, then you must add the specific AI zone within that region group to your Organization Policy's deny list. For example, if you're using `in:us-central1-locations` to allowlist the Google Cloud region `us-central1`, then you must also add `Deny: us-central1-ai1b` to your Organization Policy's deny list. For a list of AI zones, see [AI zone locations](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones#locations).

## What's next

  * Learn more about [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)
  * Learn about [Changing the default region or zone](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region)
  * Learn more about [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
