---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-regional-views-global-resources/
title: Troubleshoot regional views of global resources \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:36.272196+00:00
---

# Troubleshoot regional views of global resources  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-regional-views-global-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot regional views of global resources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot consistency, replication delays, and quota metric behavior when querying global resources through Compute Engine regional view API endpoints. For more information about regionalized read-only endpoints, see [Regional views of global resources](https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources).

## Replication delays or missing resources

When you query regional metadata endpoints, you might observe that newly created global resources or recently updated metadata fields don't immediately appear in regional responses.

Regional view APIs serve read requests by querying a regional read-only replica of the central global database. Updates made to primary global resources using standard global endpoints are replicated asynchronously to these regional replicas.

This asynchronous replication means regional views are _eventually consistent_. P99 replication latency from the central global database to regional replicas is typically under 60 seconds.

**Resolution** : To resolve this issue, try one of the following:

  * **Wait for replication** : Most replication updates complete within 60 seconds. If an automated script or client workload queries a newly created resource, ensure your client implements retry logic with exponential backoff.
  * **Understand transparent fallback** : If an explicit `GET` request for a specific resource ID targeting a regional replica results in a cache miss, Compute Engine automatically attempts a fallback read to the central global database within the same transaction.
  * **Query global endpoints for strong consistency** : If your deployment pipeline strictly requires immediate read-after-write consistency without replication latency, query canonical global endpoints directly instead of regional views. For example, query [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get), [`images.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get), or [`images.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/list).



## `404 Not Found` responses

You might receive a `404 Not Found` HTTP status code when attempting to retrieve a specific image or project view.

A `404 Not Found` error might occur for the following reasons:

  * The target resource does not exist in the central global database.
  * The target resource was created within the last few seconds, replication to the regional replica has not completed, and the transparent fallback request to the central global database timed out or failed.
  * You specified an invalid region parameter or project ID in the request URL.



**Resolution** : To resolve this issue, try the following:

  1. Verify that the requested resource exists globally by running a standard global `describe` or `list` request—for example, `gcloud compute images describe IMAGE_NAME` or `gcloud compute project-info describe --project=PROJECT_ID`.
  2. Inspect the request URL path to ensure the target `REGION` string is valid and active.
  3. If the resource was newly created, retry the request after 60 seconds.



## Missing `quota` array in `projectViews` responses

When querying a `compute.Project` resource using regional `projectViews.get` endpoints, the `quota` array is excluded from the response.

To maintain regional fault isolation and high availability, the `projectViews` endpoint reads strictly from its regional replica. Because it doesn't perform cross-region fanouts to collect quota usage across zones, the `quota` array is excluded.

**Resolution** : To resolve this issue, do the following:

  * Ensure that your applications don't expect the `quota` array in responses returned by regional `projectViews` endpoints.
  * To retrieve accurate quota configuration and real-time usage metrics across all regions and zones, query the global [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get) endpoint or monitor Compute Engine API quota metrics in Cloud Monitoring.



## What's next

  * Review [Use regional views for resilient control-plane reads](https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources).
  * Learn how to [Access global resources regionally for high availability](https://docs.cloud.google.com/compute/docs/architecture/access-global-resources-regionally).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
