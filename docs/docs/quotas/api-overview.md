---
url: https://docs.cloud.google.com/docs/quotas/api-overview/
title: Cloud Quotas API overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:17.217540+00:00
---

# Cloud Quotas API overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Cloud Quotas API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Quotas API lets you programmatically adjust project-level [quotas](https://docs.cloud.google.com/docs/quotas/overview) and automate project-level quota [adjustment requests](https://docs.cloud.google.com/docs/quotas/overview#about_increase_requests). For example, you can use the Cloud Quotas API to:

  * **Automate quota adjustments** : You can use the Cloud Quotas API to request quota adjustments based on your own criteria. For example, to avoid quota exceeded errors, you can use the API to programmatically request a quota adjustment when Compute Engine resources reach 80% of the available quota.

  * **Reuse quota configurations across projects** : The Cloud Quotas API can clone your quota configurations from project to project. If there is a known set of quotas that need to be increased for every new Google Cloud project, you can use the Cloud Quotas API to automate this in the creation logic of your project. Quota adjustment requests are subject to Google Cloud approval.

  * **Serve customer quota requests** : If you are a SaaS provider integrated with Google Cloud, you might receive quota increase requests through a customer-facing portal other than the Google Cloud console. These requests must be forwarded to Google Cloud for processing. The Cloud Quotas API can automatically forward customer requests.

  * **Enable client configuration version control** : The Cloud Quotas API is declarative. You can treat quota configurations as code and store configurations in your own version controlled system for history and rollback.




## Limitations

Cloud Quotas has the following limitations:

  * In most cases, quota _increase_ adjustments must be made at the [project-level](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). A limited number of products support [organization-level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) quota increase adjustments. To see if a Google Cloud product supports organization-level quota increase adjustments, refer to the documentation for that product.

  * You can request quota _decrease_ adjustments for project-, organization-, and [folder-level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) quotas.




## Service endpoint

The service endpoint is a base URL that specifies the network address of an API service. One service might have multiple endpoints. The Cloud Quotas API service has the following endpoint and all URIs are relative to it:

`https://cloudquotas.googleapis.com`

## Required roles

To get the permissions that you need to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources, ask your administrator to grant you the Cloud Quotas Admin (`cloudquotas.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to access the `cloudquotas_quotaPreferences`, `cloudquotas_quotaInfos`, and `cloudquotas_quotaAdjusterSettings` resources:

  * `cloudquotas.quotas.update`
  * `cloudquotas.quotas.get`
  * `monitoring.timeSeries.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## API resource model

The Cloud Quotas API resource model consists of two resources: `QuotaPreference` and `QuotaInfo`.

### Quota preference

The `QuotaPreference` resource represents your quota preference for a particular [dimension combination](https://docs.cloud.google.com/docs/quotas/configure-dimensions#dimension_precedence). Use this resource to adjust the quotas in your projects, folders, or organizations.

#### Set a preferred value for a region

The following example shows a `QuotaPreference` resource in a `CreateQuotaPreference` method.
    
    
    {
        "service": "compute.googleapis.com",
        "quotaId": "GPUS-PER-GPU-FAMILY-per-project-region",
        "quotaConfig": {
            "preferredValue": 100
        },
        "dimensions": {
            "region": "us-central1"
        }
    }

The `preferredValue` of 100 indicates that the requester wants the `GPUS-PER-GPU-FAMILY-per-project-region` quota to be set to that value. The dimensions field indicates the preference only applies to region `us-central1`.

#### Verify the granted value

View your quota preference and look at the `grantedValue` field to verify the granted value.

To view your quota preference using the Google Cloud CLI, run the following in your terminal:
    
    
    gcloud alpha quotas preferences describe QUOTA_PREFERENCE_ID --project=PROJECT

Replace the following:

  * `QUOTA_PREFERENCE_ID`: the ID of your quota preference. This is the value that was specified when the quota preference was created.
  * `PROJECT`: the ID or number of your Google Cloud project.



If you made a quota adjustment request and the request is partially approved or denied, a `stateDetail` field appears after the `grantedValue` field. The `grantedValue` shows the adjustment that was made, and the `stateDetail` field provides more context about the final state of the request-for example, explaining a partially approved state or detailing the reason for a denial.

To see if the granted value is the final value approved, look at the `reconciling` field. If your request is still undergoing evaluation, the `reconciling` field is set to `true`. If the `reconciling` field is set to `false` or is omitted, the granted value is the final value approved.

The following code snippets show examples of the quota preference object. They use a demo quota preference with the ID `compute_googleapis_com-gpus-us-central1`.

### gcloud

If you view your quota preference using the gcloud CLI, the output looks similar to the following:
    
    
    createTime: '2023-01-15T01:30:15.01Z'
    dimensions:
        region: us-central1
    name: projects/PROJECT_NUMBER/locations/global/quotaPreferences/compute_googleapis_com-gpus-us-central1
    quotaConfig:
        grantedValue: '100'
        preferredValue: '100'
        traceId: 123acd-345df23
        requestOrigin: ORIGIN_UNSPECIFIED
    service: compute.googleapis.com
    quotaId: GPUS-PER-GPU-FAMILY-per-project-region
    updateTime: '2023-01-16T02:35:16.01Z'

### REST

If you view your quota preference using the Cloud Quotas API, the output looks similar to the following:
    
    
    {
        "name": "projects/PROJECT_NUMBER/locations/global/quotaPreferences/compute_googleapis_com-gpus-us-central1",
        "service": "compute.googleapis.com",
        "quotaId": "GPUS-PER-GPU-FAMILY-per-project-region",
        "quotaConfig": {
            "preferredValue": 100,
            "grantedValue": 100,
            "traceId": "123acd-345df23",
            "requestOrigin": "ORIGIN_UNSPECIFIED"
        },
        "dimensions": {
            "region": "us-central1"
        },
        "createTime": "2023-01-15T01:30:15.01Z",
        "updateTime": "2023-01-16T02:35:16.01Z"
    }

This output includes the following values:

  * `PROJECT_NUMBER`: an automatically generated unique identifier for your project.



The response shows a `grantedValue` of 100, meaning the `preferredValue` from the previous example has been approved and fulfilled. Preferences for different dimensions are different `QuotaPreference` resources. For example, `QuotaPreference` for CPU in regions `us-central1` and `us-east1` are two distinct resources.

#### Quota preference is required

`QuotaPreference` resources are used to indicate your preferred value for a particular quota. The current value for a particular quota is based on:

  * `QuotaPreference` requests made by you.

  * Approved quota increase requests by Google Cloud.

  * Changes to quotas initiated by Google Cloud.




The ability to delete a `QuotaPreference` is not supported. However, you can set a preferred quota value lower than the Google Cloud approved value to add further guardrails.

For more information on the `QuotaPreference` resource, see the [Cloud Quotas API Reference](https://docs.cloud.google.com/docs/quotas/reference/rest).

For more information on the `QuotaPreference` queries, see [Implement common use cases](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases).

### Quota info

`QuotaInfo` is a read-only resource that provides information about a particular quota for a given project, folder, or organization. It displays information from the quotas defined by Google Cloud services and any fulfilled quota adjustments initiated by customers. The `QuotaInfo` resource contains information such as the metadata, container type, and dimensions.

**Note:** `QuotaInfo` resources are constructed by incorporating information from different sources, a default quota configuration exists even in the case where a `QuotaPreference` has not been set. Until the customer submits a chosen state through a `quotaPreference.create` or `quotaPreference.patch` command, the `QuotaInfo` resource relies on the default quota information available.

#### Set different quota values by region

The following `QuotaInfo` resource example shows that the CPU quota for the project is 200 for region `us-central1` and 100 for all other regions.
    
    
    {
        "name": "projects/PROJECT_NUMBER/locations/global/services/compute.googleapis.com/quotaInfos/CPUS-per-project-region",
        "quotaId": "CPUS-per-project-region",
        "metric": "compute.googleapis.com/cpus",
        "containerType": "PROJECT",
        "dimensions": [
            "region"
        ],
        "isPrecise": true,
        "quotaDisplayName": "CPUs per project per region",
        "metricDisplayName": "CPUs",
        "dimensionsInfo": [
            {
                "dimensions": {
                    "region": "us-central1"
                },
                "details": {
                    "quotaValue": 200,
                    "resetValue": 200
                },
                "applicableLocations": [
                    "us-central1",
                ]
            },
            {
                "details": {
                    "quotaValue": 100,
                    "resetValue": 100
                },
                "applicableLocations": [
                    "us-central2",
                    "us-west1",
                    "us-east1"
                ]
            }
        ]
    }

This output includes the following values:

  * `PROJECT_NUMBER`: an automatically generated unique identifier for your project.



#### Set a global quota

The following `QuotaInfo` resource example shows a rate quota with a per minute refresh interval. The dimensions are blank, which indicates that this is a global quota. All quotas without a region or zone dimension are global.
    
    
    {
        "name": "projects/PROJECT_NUMBER/locations/global/services/compute.googleapis.com/quotaInfos/ReadRequestsPerMinutePerProject",
        "quotaId": "ReadRequestsPerMinutePerProject",
        "metric": "compute.googleapis.com/read_requests",
        "refreshInterval": "minute",
        "containerType": "PROJECT",
        "dimensions": [],
        "isPrecise": false,
        "quotaDisplayName": "Read Requests per Minute",
        "metricDisplayName": "Read Requests",
        "dimensionsInfo": [
            {
                "details": {
                    "quotaValue": 100,
                    "resetValue": 200
                },
                "applicableLocations": [
                    "global"
                ]
            }
        ]
    }

This output includes the following values:

  * `PROJECT_NUMBER`: an automatically generated unique identifier for your project.



For more details on the `QuotaInfo` resource, see the [Cloud Quotas API Reference](https://docs.cloud.google.com/docs/quotas/reference/rest).

For more details on the `QuotaPreference` queries, see [Implement common use cases](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases).

### Quota adjuster settings

The `QuotaAdjusterSettings` resource represents your quota adjuster settings for a particular project. When enabled, the quota adjuster monitors your usage of the specified resources and issues quota adjustment requests when resource use approaches its quota value.

  * To view the current quota adjuster settings for a project, use a [GET](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaAdjusterSettings/getQuotaAdjusterSettings) operation to retrieve the `QuotaAdjusterSettings` resource.

  * To enable quota adjuster for a project, use an [PATCH](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaAdjusterSettings/updateQuotaAdjusterSettings) operation to set the following `QuotaAdjusterSettings` resource options:
        
        "quota_adjuster_settings" :{
             "name": "projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings",
             "enablement": ENABLED,
        }
        

Replace `PROJECT_NUMBER` with the unique identifier for your project.




For details, see [Enable the quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster#enable) and [Disable the quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster#disable).

## Resource names

Resources are named entities and are identified by resource names. Resource names are used in all requests and responses, and each resource must have its own unique resource name. Each resource name is encoded by a set of fields.

### Quota preference resource

The naming convention for a `QuotaPreference` resource uses the following pattern:
    
    
    projects/PROJECT_NUMBER/locations/global/quotaPreferences/QUOTA_PREFERENCE_ID

You can set the `quotaPreferenceId` when creating a quota preference, otherwise an ID is generated. It is recommended that a `quotaPreferenceId` naming scheme encodes the service name, quota ID, location and other dimensions. The `quotaPreferenceId` must be unique for the project, folder, or organization.

As an example `quotaPreference` One pattern to encode your quota preference ID is the following: 
    
    
    SERVICE_LOCATION_DIMENSION1-VALUES-IN-ORDER

The following example demonstrates this pattern: 
    
    
    compute_us-central1_nvidia-200

The `location` field in a resource name is always `global`. The Cloud Quotas API is a global service.

With a resource name, you should use the [`GET`](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaPreferences/get) method to retrieve a `QuotaPreference`. You can also call the [`PATCH`](https://docs.cloud.google.com/docs/quotas/reference/rest/v1beta/organizations.locations.quotaPreferences/patch) method with the `allow_missing` option enabled to create or update a `QuotaPreference`.

### Quota info resource

The naming convention for a `QuotaInfo` resource uses the following pattern:
    
    
    projects/PROJECT_NUMBER/locations/global/services/SERVICE_NAME/quotaInfos/QUOTA_ID

### Quota adjuster settings resource

The naming convention for a `QuotaAdjusterSettings` resource uses the following pattern:
    
    
    projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings

## What's next?

  * [Implement common use cases](https://docs.cloud.google.com/docs/quotas/implement-common-use-cases)

  * Cloud Quotas API [reference](https://docs.cloud.google.com/docs/quotas/reference/rest)

  * Understand [quotas](https://docs.cloud.google.com/docs/quotas/overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
