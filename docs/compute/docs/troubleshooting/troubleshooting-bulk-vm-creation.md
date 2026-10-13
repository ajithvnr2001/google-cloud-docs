---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-bulk-vm-creation/
title: Troubleshooting bulk VM creation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:54.279670+00:00
---

# Troubleshooting bulk VM creation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-bulk-vm-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting bulk VM creation Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to resolve issues with [bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api) creation operations.

## Operation errors

When you use the bulk instance API to create VMs, `create` requests return `HTTP 200 OK` with a status of `RUNNING` if the request starts successfully. If the request doesn't start successfully, the API returns one of the responses below.

### Invalid

If the following API response fields are present when you create VMs, your API request isn't written correctly, or it uses a property that isn't supported by the bulk API.

**API response fields:**

  * `HTTP 400`
  * `"reason": "invalid"`



To resolve this issue, do the following:

  1. View the `message` field in the response to determine which property in the request caused the error.
  2. Update the property that caused the error.
  3. Retry the request.
  4. If the request fails again, try using the API Explorer to validate the request. For more information, see [Validating API requests](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#validating_api_requests).



### Quota exceeded

If the following API response fields are present when you create VMs, you reached a quota limit for a resource. For more information about quotas, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

**API response fields:**

  * `HTTP 403`
  * `"reason": "quotaExceeded"`

To resolve this issue, do the following: 
  1. View the `message` field to identify which resource quota the request exceeded.
  2. Do one of the following: 
     * Retry the request with a smaller number of VMs
     * [Request an increase in quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota)



### Rate limit exceeded

If the following API response fields are present when you create VMs, you reached the 20 request per second request limit or you have more than 10 bulk operations running at the same time.

**API response fields:**

  * `HTTP 403`
  * `"reason": "rateLimitExceeded"`



To resolve this issue, wait until some requests complete and try your request again.

### Insufficient capacity

If the following API response fields are present when you create VMs, the region or zone you tried to create VMs in has insufficient capacity.

**API response fields:**

  * `HTTP 503`
  * `"reason": "insufficientCapacity"`

To resolve this issue, do one of the following: 
  * Create VMs in a different region
  * Create VMs in a different zone if using the zonal endpoint
  * Try a different VM configuration
  * Retry your request later



## Request status errors

When you use the bulk instance API to create VMs, your `create` request returns `HTTP 200 OK` with a status of `RUNNING` if the request starts successfully. However, the request may fail before it completes. You can [check the status of your request](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api#checking_the_status_of_vms_created_with_the_bulk_instance_api) to ensure the request completed successfully. If the request didn't complete successfully, you see one of the following request statuses.

### Quota exceeded

If the following API response fields are present when you poll operations, your request failed because you reached a quota limit for a resource. For more information about quotas, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

**API response fields:**

  * `"status": "done"`
  * `"httpErrorMessage": "FORBIDDEN"`
  * `"code"": "QUOTA_EXCEEDED"`



To resolve this issue, do the following:

  1. View the `message` field to identify which resource quota the request exceeded.
  2. Do one of the following: 
     * Retry the request with a smaller number of VMs
     * [Request an increase in quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota)



### Resource already exists

If the following API response fields are present when you poll operations, your request failed because it tried to create a resource that already exists.

**API response fields:**

  * `code: RESOURCE_ALREADY_EXISTS`
  * `httpErrorMessage: CONFLICT`
  * `status: DONE`



To resolve this issue, do the following:

  1. View the `message` field to identify the name of the resource that already exists.
  2. Retry your request using a different `namePattern`. For more information, see [Creating multiple VMs in a region](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api#creating_multiple_vms_in_a_region).



### Insufficient capacity

If the following API response fields are present when you poll operations, your request failed because the region or zone (if using the zonal endpoint) you tried to create VMs in has insufficient capacity.

**API response fields:**

  * `"status": "DONE"`
  * `"httpErrorMessage": "SERVICE UNAVAILABLE"`
  * `"code": "ZONE_RESOURCE_POOL_EXHAUSTED"`



To resolve this issue, do one of the following:

  * Create VMs in a different region
  * Create VMs in a different zone if using the zonal endpoint
  * Try a different VM configuration
  * Retry your request later



## What's next?

  * To learn more about using the bulk instance API, review [Using the bulk instance API](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
