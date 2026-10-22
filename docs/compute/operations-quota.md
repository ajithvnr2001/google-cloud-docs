---
url: https://docs.cloud.google.com/compute/operations-quota/
title: Compute Engine concurrent operation quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:00.704143+00:00
---

# Compute Engine concurrent operation quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/operations-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine concurrent operation quotas Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the concurrent operation quotas for Compute Engine.

## Concurrent operation quotas

Concurrent operation quotas define the number of in-flight or concurrent operations that can occur at any point of time. Any API request that creates, modifies, or deletes a Compute Engine resource is subject to a concurrent operation limit check to ensure that the total number of in-flight operations at any point of time does not exceed the limit specified for that operation.

### Concurrent operation limit exceeded error

If your project exceeds the concurrent operation limit for any in-flight operation, you receive a `403` error with the reason `rateLimitExceeded`.

The API response of the error looks similar to the following:
    
    
        "error": {
          "code": 403,
          "message": "Rate Limit Exceeded",
          "errors": [
            {
              "message": "Rate Limit Exceeded",
              "domain": "usageLimits",
              "reason": "rateLimitExceeded",
            ...
            ...
            }
          ],
          "details": [
            {
              "@type": "type.googleapis.com/google.rpc.ErrorInfo",
              "reason": "CONCURRENT_OPERATIONS_QUOTA_EXCEEDED",
              "domain": "compute.googleapis.com",
              "metadata": {
                "containerType": "PROJECT",
                "containerId": "PROJECT_ID",
                "quotaMetric": "QUOTA_METRIC",
                "quotaLimit": "QUOTA_LIMIT",
                "operationType": "OPERATION_TYPE",
                "location": "global | REGION"
              }
            },
            {
              "@type": "type.googleapis.com/google.rpc.Help",
              "links": [
                {
                  "description": "Concurrent operations quota documentation.",
                  "url": "https://cloud.google.com/compute/operations-quota#concurrent_operation_limits"
                }
              ]
            },
          ...
          ... 

The error details contain the following values:

  * `PROJECT_ID`: the ID of the project in which the quota exceeds the limit.

  * `QUOTA_METRIC`: the metric for the concurrent quota that exceeds the limit. It can be one of the following:

    * `compute.googleapis.com/global_concurrent_operations`
    * `compute.googleapis.com/regional_concurrent_operations`
  * `QUOTA_LIMIT`: the limit name of the concurrent quota. It can be one of the following:

    * `GlobalConcurrentOperationsPerProject`
    * `GlobalConcurrentOperationsPerProjectOperationType`
    * `RegionalConcurrentOperationsPerProject`
    * `RegionalConcurrentOperationsPerProjectOperationType`
  * `OPERATION_TYPE`: the global or regional operation for which the quota exceeds the limit. For a list of operations, see Concurrent operation quota groups.

  * The `location` can be one of the following:

    * `global`: specifies that the limit exceeded for global operation quota
    * `REGION`: specifies the region where the limit exceeded for the operation quota



The detailed error logs are returned only through API response. Error in Logs Explorer is similar to the following:
    
    
       "protoPayload":{
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "message": "Rate Limit Exceeded"
        }
        "serviceName": "compute.googleapis.com",
        "methodName": "METHOD_NAME",
        ...
        ...
        "response": {
          "error": {
            "message": "Rate Limit Exceeded",
            "code": 403,
            "errors": [
              {
                "message": "Rate Limit Exceeded",
                "reason": "rateLimitExceeded",
                "domain": "usageLimits"
              }
            ]
          },
          "@type": "type.googleapis.com/error"
        },
        ...
        ... 

The `METHOD_NAME` in the error represents the API method for which the rate limit exceeded. For example, `v1.compute.instances.stop`.

### Concurrent operation quota groups

This section describes the limits for various Compute Engine in-flight or concurrent operations.

#### Global operation quotas

Concurrent global operations consume a global limit that is specified for operation types per project. The following table lists the global quotas for in-flight operations and the corresponding metrics.

You can view the quota for global operations by using the Google Cloud console, Google Cloud CLI, and Service Usage API. For more information, see View concurrent operation quotas and limits.

Quota name  
Description | Metric name | Methods that consume this quota  
---|---|---  
`Concurrent global operations per project`  
Limits the total number of concurrent global operations for a project. [View this quota in the Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?metric=compute.googleapis.com/global_concurrent_operations) | ` compute.googleapis.com/global_concurrent_operations ` | All global methods. The HTTP request URL contains `global` for these methods. For example, the `[networks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert)` method: `POST /compute/v1/projects/{project}/global/networks`  
`Concurrent global operations per project operation type`  
Limits the number of concurrent operations per project per operation type. [View this quota in the Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?metric=compute.googleapis.com/global_concurrent_operations) | ` compute.googleapis.com/global_concurrent_operations ` |  All global methods. The default concurrent operation quota is `500` in-flight operations per project, except for the following methods, which have different default limits:  `[globaladdresses.move](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/move)` `[firewalls.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/delete)` `[firewalls.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert)` `[images.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/delete)` `[images.deprecate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/deprecate)` `[images.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert)` `[images.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/patch)` `[images.setLabels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setLabels)` `[images.setIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/setIamPolicy)` `[licenses.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/licenses/insert)` `[machineimages.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineImages/delete)` `[machineimages.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineImages/insert)` `[networks.addPeering](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/addPeering)` `[networks.removePeering](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/removePeering)` `[networks.updatePeering](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/updatePeering)` `[projects.setCommonInstaneMetadata](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/updatePeering)` `[publicAdvertisedPrefixes.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/delete)` `[publicAdvertisedPrefixes.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes/insert)` ` [routes.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/delete)` ` [routes.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/insert)` ` [securityPolicies.patchRule](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patchRule)` ` [snapshots.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/delete)` ` [snapshots.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert)` ` [snapshots.setLabels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/setLabels)` ` [snapshots.setIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/setIamPolicy)` ` [snapshotSettings.patch](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshotSettings/patch)`  
  
#### Regional operation quotas

Concurrent regional operations consume a regional limit that is specified for operation types per project in a given region.

The following table lists the regional quotas for in-flight operations and the corresponding metrics.

You can view the quota for regional operations by using the Google Cloud console, Google Cloud CLI, and Service Usage API. For more information, see View concurrent operation quotas and limits.

Quota name  
Description | Metric name | Methods that consume this quota  
---|---|---  
` Concurrent regional operations per project `  
Limits the total number of concurrent regional operations for a project. [View this quota in the Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?metric=compute.googleapis.com/regional_concurrent_operations) | ` compute.googleapis.com/regional_concurrent_operations ` | All regional methods. The HTTP request URL contains `regions` or `zones` for these methods. For example, the `[instances.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert)` method: `POST /compute/v1/projects/{project}/zones/{zone}/instances`  
` Concurrent regional operations per project operation type `  
Limits the number of concurrent regional operations per project per operation type. [View this quota in the Google Cloud console](https://console.cloud.google.com/iam-admin/quotas?metric=compute.googleapis.com/regional_concurrent_operations) | ` compute.googleapis.com/regional_concurrent_operations ` |  All regional methods. The default concurrent operation quota is `500` in-flight operations per project per region, except for the following methods, which have different default limits: `[ addresses.move](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/move) ` `[ disks.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) ` `[ instances.delete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/delete) ` `[ instances.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) ` `[ instances.simulateMaintenanceEvent](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/simulateMaintenanceEvent) ` `[ networkEndpointGroups.attachNetworkEndpoints](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/attachNetworkEndpoints) ` `[ networkEndpointGroups.detachNetworkEndpoints](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/detachNetworkEndpoints) ` `[ publicDelegatedPrefixes.delete ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicDelegatedPrefixes/delete)` `[ publicDelegatedPrefixes.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicDelegatedPrefixes/insert) `  
  
### View concurrent operation quotas and limits

To view the quota usage and limits in a project, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

The **Quotas** page lists all quota usage and limits for your project. By default, the list is sorted to show your most used quotas first, which helps you see limits that are at risk of being exceeded.

  2. To filter the list and to view the usage and limit for any specific quota, select the **Quota** or **Metric** in the **Filter** field.

For example, select the Quota `Concurrent global operations per project operation type` to see the quota usage for global methods per operation type.

To filter the quota for a specific operation, add **Dimensions** to the filter query and select the **operation_type**. For example, select `firewalls_insert` to see the quota usage and limit for `firewalls.insert` operation.




###  gcloud 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use the Google Cloud CLI to view the usage and limit of concurrent operation quotas.

To use this approach, ensure that you have installed the [alpha commands](https://docs.cloud.google.com/sdk/docs/components#alpha_and_beta_components) component. If you're using Cloud Shell to interact with Google Cloud, the Google Cloud CLI is installed for you.

To view the quota, use the following command:
    
    
    gcloud alpha services quota list \
        --service=compute.googleapis.com \
        --consumer=projects/PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project for which you want to view the quota.

### Best practices

The following checklist summarizes the best practices for reducing insufficient concurrent operation limit errors:

  * [Wait for operations to be done](https://docs.cloud.google.com/compute/docs/api/best-practices#wait-for-operations)
  * [Rely on error codes, not error messages](https://docs.cloud.google.com/compute/docs/api/best-practices#rely-on-errors-not-messages)
  * [Minimize client-side retries to preserve API rate limits](https://docs.cloud.google.com/compute/docs/api/best-practices#preserve-API-rate-limits)
    * [Avoid short polling](https://docs.cloud.google.com/compute/docs/api/best-practices#avoid-short-polling)
    * [Use bursting sparingly and selectively](https://docs.cloud.google.com/compute/docs/api/best-practices#limit-bursting)
    * [Always make your calls in a retry loop with exponential backoff](https://docs.cloud.google.com/compute/docs/api/best-practices#retry-with-exponential-backoff)
    * [Use a client-side rate limiter](https://docs.cloud.google.com/compute/docs/api/best-practices#use-client-side-rate-limiter)
    * [Split up your applications across multiple projects](https://docs.cloud.google.com/compute/docs/api/best-practices#multiple-projects)



## What's next

  * Read about [Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
