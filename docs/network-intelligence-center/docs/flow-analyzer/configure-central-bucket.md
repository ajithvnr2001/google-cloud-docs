---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/configure-central-bucket/
title: Configure a central bucket \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:02.265973+00:00
---

# Configure a central bucket  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/configure-central-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Configure a central bucket Stay organized with collections  Save and categorize content based on your preferences. 

You can decide to not store logs in the __Default_ bucket to route them to a central networking bucket (or multiple buckets for larger organizations).

You can achieve this by performing any of the following:

  * Use an [aggregated](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) sink configured at the folder or organization level. Optionally, such a sink allows intercept logs to avoid duplication.
  * Manually configure sinks in projects to route traffic to specific buckets.



To analyze networking logs in the organization using Observability Analytics, we recommend you route them to the central networking bucket before you enable VPC Flow Logs.

  1. [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket).
  2. Route logs to the newly created bucket. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).
  3. [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).
  4. Configure log routing for each project.
  5. [Enable VPC Flow Logs for each resource](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs).



## Route logs from the projects to a central bucket

By default, Observability Analytics lets you analyze the logs in a single log bucket. To view data from multiple projects, you must create a central log bucket and route logs to this central bucket.

The bucket that is used to store networking logs must be upgraded to support [Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
