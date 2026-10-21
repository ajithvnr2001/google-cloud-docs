---
url: https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts/
title: View ongoing rollouts \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:38.542694+00:00
---

# View ongoing rollouts  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/view-ongoing-rollouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  View ongoing rollouts Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Quotas lets you view quota value rollouts that are in progress. This section explains how to view these rollouts from the Google Cloud console and the Cloud Quotas API.

## Understand ongoing rollouts

When another Google Cloud service increases the default quota values for resources and APIs, these changes take place gradually. This might result in ongoing rollouts across different regions or resources. During the rollout, the quota value that appears in the Google Cloud console or Cloud Quotas API won't reflect the new, increased quota value until the rollout completes.

**Note:** During an ongoing rollout, both the Google Cloud console and Cloud Quotas API show the older quota value that is currently applied to your resources. This ensures that your applications and services function as expected. Only after the rollout completes, does the increased quota value appear.

## View ongoing rollouts from the console

If there are ongoing quota rollouts in progress, an informational message appears at the top of the Cloud Quotas page in the console. The message appears similar to the following text, which also contains a link. Click **quotas** to filter so that only quotas with ongoing rollouts appear:
    
    
    Values for **_quotas_** are being updated. This may take 2-3 weeks to complete.

The update rolling update indicator appears next to the quota values impacted by ongoing rollouts.

If you don't see the update rolling update indicator, follow these steps:

  1. In the Google Cloud console, go to the **IAM & Admin > Quotas & System Limits** page: 

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

  2. Click the link to **quotas** in the informational message. This turns on the filter: **Has ongoing rollout: True**.

  3. The table updates to show a update rolling update indicator next to quota values with ongoing rollouts.




The rolling update indicator also appears in the **Edit Quotas** and monitoring **Quota usage chart** panels to help you identify quotas with in progress rollouts.

## View ongoing rollouts from the Cloud Quotas API

You can also view ongoing rollouts using the Cloud Quotas API. For more information, see instructions on how to [set up the Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/development-environment) and [implement common use cases](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases).

The Cloud Quotas API resource model uses the `QuotaInfo` and `QuotaPreference` resources to indicate ongoing rollouts:

  * The `QuotaInfo` resource returns the previous quota value during ongoing rollouts. For quotas experiencing an ongoing rollout, a `rollout_info` field appears in the response under `QuotaDetails`. This field indicates that there is both an ongoing rollout and an increase in the quota value for the dimensions specified in each `dimensionsInfo` resource.

  * The `QuotaPreference` resource returns the previous quota value during ongoing rollouts.




During ongoing rollouts, the following Cloud Quota APIs return the previous quota value:

  * [GetQuotaInfo](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/get)
  * [ListQuotaInfo](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.services.quotaInfos/list)
  * [CreateQuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/create)
  * [UpdateQuotaPreference](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences/patch)



### Before you use the Cloud Quotas API

The following sections assume that you are familiar with the Cloud Quotas API. Before you use the Cloud Quotas API, make sure that you set up your development environment and are comfortable with the commands to make GET requests for quota information:

  * For an overview, see [Cloud Quotas API overview](https://docs.cloud.google.com/docs/quotas/api-overview).
  * For instructions on how to set up your development environment, see instructions on how to [set up the Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/development-environment).
  * To see an example API request and response, see the example that shows how to [get quota info for a service specific dimension](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases#get_quota_info_for_a_service_specific_dimension).



### Example API response during a ongoing rollout

The following example shows the results of a regional quota supported in four regions: us-central1, us-central2, us-west1, us-east1. Its default value is 200 in us-central1 and 100 in all other regions. This regional quota also has an additional quota override of 300 in us-central2.

Assume that the service producer updates the default value to be `220` in us-central1 and us-central2. The example that follows shows a QuotaInfo response where the service config rollout is ongoing for us-central1 and us-central2:

  * For each location, the `details` field displays the quota value before the rollout completes.
  * For us-central1, the quota value is as `200` and the `rolloutInfo` field indicates that an ongoing rollout is in progress. The quota value changes to 220 only after the rollout completes.
  * For us-central2, the quota value is `300` due to the quota override. The `rolloutInfo` field does not appear because the quota value remains unchanged after the rollout completes.
  * For both us-west1 and us-east1, the value defaults to `100`.


    
    
    "name": "projects/PROJECT_NUMBER/locations/global/services/compute.googleapis.com/quotaInfos/GPUS-PER-GPU-FAMILY-per-project-region",
    "quotatId": "GPUS-PER-GPU-FAMILY-per-project-region",
    "metric": "compute.googleapis.com/gpus_per_gpu_family",
    "service": "compute.googleapis.com",
    "isPrecise": true,
    "containerType": "PROJECT",
    "dimensions": [
      "gpu_family",
      "region"
    ],
    "quotaDisplayName": "GPUs per GPU family",
    "metricDisplayName": "GPUs",
    "dimensionsInfos": [
     {
            "dimensions": { "region" : "us-central1" } ,
            "**details** ": {
                "value": **200** ,
                "**rolloutInfo** ": {
                  "ongoingRollout": true
                }
            },
            "applicableLocations":  [ "us-central1" ] ,
    },
     {
            "dimensions": { "region" : "us-central2" } ,
            "**details** ": {
                "value": **300** ,
            },
            "applicableLocations":  [ "us-central2" ]
    },
    {
            "dimensions": {},
            "**details** ": {
                "value": **100** ,
            },
             "applicableLocations": [ "us-west1", "us-east1" ]
    }]

## What's next

  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
  * [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts)
  * [Known issues](https://docs.cloud.google.com/docs/quotas/known-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
