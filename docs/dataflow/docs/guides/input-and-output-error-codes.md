---
url: https://docs.cloud.google.com/dataflow/docs/guides/input-and-output-error-codes/
title: Input and output error codes \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:20.521379+00:00
---

# Input and output error codes  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/input-and-output-error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Input and output error codes Stay organized with collections  Save and categorize content based on your preferences. 

The I/O metric charts use [canonical error codes](https://docs.cloud.google.com/apis/design/errors#handling_errors). If these error codes persist in your sources and sinks, refer to the following list for potential causes and actions you can take.

  * `RESOURCE_EXHAUSTED`. The project might have run out of [resource quota](https://docs.cloud.google.com/compute/quotas) for the service the source or sink is using.

If the error occurs occasionally or when the **Requests per sec chart** indicates a high volume of requests being made, then this might indicate that you have reached an [API rate limiting quota](https://docs.cloud.google.com/service-infrastructure/docs/rate-limiting) and need to increase the quota.

  * `DEADLINE_EXCEEDED`. Source or sink might have timed out reading or writing a large batch of data. Check the latency chart and worker logs. If the error persists, [contact support](https://cloud.google.com/support-hub/).

  * `INVALID_ARGUMENT`. Parameters specified to the source or sink might be malformed (such as a Pub/Sub topic). Check configuration of the source or sink, and check the worker logs.

  * `FAILED_PRECONDITION`. Check configuration of the source or sink, and check the worker logs. This could also indicate a bug.

  * `OUT_OF_RANGE`. Check that the resource being used by the source or sink exists (such as a Pub/Sub topic or subscription).

  * `UNAUTHENTICATED`. Check that the [Dataflow service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#cloud_dataflow_service_account) has [Identity and Access Management (IAM)](https://docs.cloud.google.com/resource-manager/docs/access-control-org) permissions to the specific service and relevant [APIs are enabled](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.

  * `PERMISSION_DENIED`. Check that the [Dataflow service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#cloud_dataflow_service_account) has [IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org) permissions to the specific service and relevant [APIs are enabled](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.

  * `NOT_FOUND`. Check that the entities being used by the source or sink exist (such as a Pub/Sub topic or subscription).

  * `ABORTED`. Service might not be properly handling the source or sinks attempts to read or write data. If the error persists, [contact support](https://cloud.google.com/support-hub/).

  * `ALREADY_EXISTS`. I/O might be trying to create an entity which already exists (such as a Pub/Sub topic or subscription). If the error persists, [contact support](https://cloud.google.com/support-hub/).

  * `CANCELLED`. This can occur when a Dataflow worker is shut down or source or sink logic intentionally decides to cancel attempts to read or write data.

  * `DATALOSS`. Indicates unrecoverable data loss or corruption occurred. You might want to create a new dataset for your sources and rerun the Dataflow job.

You might also see if there are any backup and restoring instructions available for the underlying Google Cloud service.

  * `UNKNOWN`. Service might be down. Check for updates on [Cloud Status Dashboard for more information](https://status.cloud.google.com/).

  * `INTERNAL`. Service might be down. Check for updates on [Cloud Status Dashboard for more information](https://status.cloud.google.com/).

  * `UNAVAILABLE`. Service might be down. Check for updates on [Cloud Status Dashboard for more information](https://status.cloud.google.com/).

  * `UNIMPLEMENTED`. The source or sink attempted to use the service in an invalid way. Your pipeline might be misconfigured. If the error persists, [contact support](https://cloud.google.com/support-hub/).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
