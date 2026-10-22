---
url: https://docs.cloud.google.com/compute/docs/api/best-practices/
title: Best practices for the Compute Engine API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:04.969751+00:00
---

# Best practices for the Compute Engine API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Best practices for the Compute Engine API Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the recommended best practices for using the Compute Engine API and is intended for users who are already familiar with it. If you are a beginner, learn about the [prerequisites](https://docs.cloud.google.com/compute/docs/api/prereqs) and [using the Compute Engine API](https://docs.cloud.google.com/compute/docs/api/getting-started).

Following these best practices can help you save time, prevent errors, and mitigate the effects of [rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits).

## Use client libraries

Client libraries are the recommended way of programmatically accessing the Compute Engine API. Client libraries provide code that lets you access the API through common programming languages, which can save you time and improve your code's performance.

Learn more about [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries) and [Client library best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices).

## Generate REST requests by using the Cloud console

When creating a resource, generate the REST request using the resource creation pages or details pages in the Google Cloud console. Using a generated REST request saves time and helps prevent syntax errors.

Learn how to [Generate REST requests](https://docs.cloud.google.com/compute/docs/console#restrequest).

## Wait for operations to be done

Don't assume that an operation—any API request that changes a resource—is complete or successful. Instead, use a `wait` method for the `Operation` resource to verify that the operation is done. (You don't need to verify a request that doesn't modify resources—such as a read request using a `GET` HTTP verb—because the API response already indicates if the request was successful. Consequently, the Compute Engine API does not return `Operation` resources for these requests.)

Whenever an API request is successfully initiated, it returns an HTTP `200` status code. Although receiving a `200` indicates that the server received your API request successfully, this status code doesn't indicate if the requested operation has been completed successfully or not. For example, you can receive a `200`, but the operation might not be complete yet or the operation might have failed.

Any request to create, update, or delete for a [long-running operation](https://docs.cloud.google.com/apis/design/design_patterns#long_running_operations) returns an [`Operation` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations), which captures the status of that request. An operation is done when the `status` field of the `Operation` resource is `DONE`. To check the status, use the `wait` method that matches the [scope](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) of the returned `Operation` resource:

  * For zonal operations, use [`zoneOperations.wait`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/wait).
  * For regional operations, use [`regionOperations.wait`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations/wait).
  * For global operations, use [`globalOperations.wait`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations/wait).



The `wait` method returns when the operation is done or when the request is approaching the 2-minute deadline. When using the `wait` method, avoid short polling, which is when your clients continuously make requests to the server without waiting for a response. Using the `wait` method in a retry loop with exponential backoff to check the status of your request, instead of using the `get` method with short polling for the `Operation` resource, helps preserve your [rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits) and reduces latency.

For more information about and examples of using the `wait` method, see [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

To check the status of a requested operation, see [Checking operation status](https://docs.cloud.google.com/compute/docs/api/using-libraries#checking_operation_status).

While waiting for an operation to complete, account for the [operation minimum retention period](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations#operation-retention-period), as completed operations might be removed from the database after this period.

## Paginate list results

When using a [list method](https://docs.cloud.google.com/apis/design/standard_methods#list) (such as a `*.list` method, a `*.aggregatedList` method, or any other method that returns a list), paginate the results whenever possible to ensure that you read the entire response. If you don't paginate, you can only receive up to the first 500 elements as determined by the [`maxResults` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#query-parameters).

For more information about pagination on Google Cloud, see [List Pagination](https://docs.cloud.google.com/apis/design/design_patterns#list_pagination). For specific details and examples, see the reference documentation for the list method that you want to use, such as [`instances.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list).

You can also use Cloud Client Libraries to [handle pagination](https://docs.cloud.google.com/compute/docs/api/using-libraries#handling_pagination).

## Use client-side list filters to avoid quota errors

When you use filters with `*.list` or `*.aggregatedList` methods, you incur additional quota charges if there are more than 10k filtered resources from the requests. For more information, see [`filtered_list_cost_overhead`](https://docs.cloud.google.com/compute/api-quota) in Rate quotas.

If your project exceeds this rate quota, you receive a 403 error with the reason `rateLimitExceeded`. To avoid this error, use client-side filters for the list requests.

**Note:** You cannot request a higher limit for the `filtered_list_cost_overhead` quota.

## Rely on error codes, not error messages

Google APIs must use the canonical error codes defined by [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto), but [error messages](https://docs.cloud.google.com/apis/design/errors#error_messages) can be subject to change without notice. Error messages are generally intended for developers to read, not programs.

Learn more about [API errors](https://docs.cloud.google.com/apis/design/errors).

## Minimize client-side retries to preserve rate quotas

Minimize the number of client-side retries for a project to prevent `rateLimitExceeded` errors and to maximize the utilization of your [rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits). The following practices can help you preserve the rate quotas for your projects:

  * Avoid short polling.
  * Use bursting sparingly and selectively.
  * Always make your calls in a retry loop with exponential backoff.
  * Use a client-side rate limiter.
  * Split your applications across multiple projects.



### Avoid short polling

Avoid short polling, where your clients continuously make requests to the server without waiting for a response. If you short poll, it is more difficult to catch bad requests that count against your quota, even if they do not return useful data.

Instead of short polling, you should wait for operations to be done.

### Use bursting sparingly and selectively

Use bursting sparingly and selectively. Bursting is the act of allowing a specific client to make many API requests in a short time. Usually, bursting is done in response to exceptional scenarios, such as cases where your application needs to handle more traffic than usual. Bursting burns through your rate quota quickly so make sure you use it only when necessary.

When bursting is required, use dedicated batch APIs when possible, such as the [bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api) or [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

Learn more about [batching requests](https://docs.cloud.google.com/compute/docs/api/how-tos/batch).

### Always make your calls in a retry loop with exponential backoff

Use [exponential backoff](https://wikipedia.org/wiki/Exponential_backoff) to progressively space out requests when they timeout or whenever you reach your rate quota.

Any retry loop should have an exponential backoff that ensures frequent retries don't overload your application or exceed your rate quotas. Otherwise, you risk negatively impacting all other systems in the same project.

If you need a retry loop for an operation that failed because you have reached the rate quota, your exponential backoff strategy should allow enough time between retries for the quota bucket to be refilled (usually every minute).

Alternatively, if you need a retry loop for when waiting for an operation reaches timeout, the maximum interval of your exponential backoff strategy shouldn't exceed the operation minimum retention period. Otherwise, you might receive an operation `Not Found` error.

For an example of implementing exponential backoff, see the [exponential backoff algorithm](https://docs.cloud.google.com/iam/docs/retry-strategy) for the Identity and Access Management API.

### Use a client-side rate limiter

Use a client-side rate limiter. A client-side rate limiter sets an artificial limit so that the client in question can only use a certain amount of quota, which prevents any one client from consuming all your quota.

### Split up your applications across multiple projects

Splitting up your applications across multiple projects can help minimize the number of requests for your quota buckets. Since quotas are applied on a per-project level, you can split up your applications so each application has its own dedicated quota bucket.

## Checklist summary

The following checklist summarizes the best practices for using the Compute Engine API.

  * Use client libraries
  * Generate REST requests by using the Cloud console
  * Wait for operations to be done
  * Paginate list results
  * Rely on error codes, not error messages
  * Minimize client-side retries to preserve API rate quotas
    * Avoid short polling
    * Use bursting sparingly and selectively
    * Always make your calls in a retry loop with exponential backoff
    * Use a client-side rate limiter
    * Split up your applications across multiple projects



## What's next

  * Learn how to [improve performance when using the Compute Engine API](https://docs.cloud.google.com/compute/docs/api/how-tos/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
