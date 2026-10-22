---
url: https://docs.cloud.google.com/fault-injection-testing/fault-reference/failover-cloud-sql/
title: Failover Cloud SQL fault reference \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:16.997876+00:00
---

# Failover Cloud SQL fault reference  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/fault-reference/failover-cloud-sql/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Failover Cloud SQL fault reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes what happens during an experiment with a Failover Cloud SQL fault type.

## How does the Failover Cloud SQL fault work

The Failover Cloud SQL fault triggers a high availability (HA) failover for a Cloud SQL instance by calling the `failover` method in the Cloud SQL Admin API. The purpose of this fault is to allow you to test your service's behavior and resilience when the primary Cloud SQL instance transitions to the standby instance in another zone within the same region.

The target for this fault is a Cloud SQL instance.

## What happens during experiment execution

As the experiment progresses through the [states](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State), the resources involved undergo the following changes.

**Resource** | **`PREPARING`** | **`INJECTING`** | **`REVERTING`**  
---|---|---|---  
**Instance** | None | Promote HA standby instance | Not applicable  
  
### HA failover validation and retries

The Fault Injection Testing backend performs validation checks before initiating the failover to ensure the environment is suitable. This process occurs during the `INJECTING` stage, before sending the `sqladmin.instances.failover` API call to the Cloud SQL control plane:

  * The system checks that the Cloud SQL instance [state](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.SqlInstanceState) is `RUNNABLE`. If the instance is in any other state during a running experiment, Fault Injection Testing notifies you.
  * It verifies that the `cloudsql.googleapis.com/database/available_for_failover` metric is `TRUE`.



If these conditions are not met, the failover request is enqueued for retry.

### Handling failures

If the failover is already in progress or encounters an error:

  * **During injection:** If the failover call is rejected by the Cloud SQL control plane (for example, if the standby instance is unhealthy), the experiment moves to the `STOPPING` state.
  * **Post-failover monitoring:** If the failover operation does not reach a `DONE` status within a predetermined 10-minute duration, the Fault Injection Testing backend queries the operation errors, moves the experiment to the `STOPPING` state, and marks the experiment as having encountered an error.



Fault Injection Testing relies on the Cloud SQL control plane as the source of truth. The control plane rejects any failover attempt if the standby instance is unhealthy. Fault Injection Testing uses pre-flight checks and status monitoring to avoid or report these failures rather than attempting automated retries after a rejection.

## Manual failback

Because failover is a stateful change, stopping the experiment does not automatically fail back to the original primary instance (as indicated by 'Not applicable' in the `REVERTING` stage). The database will continue to run in the secondary zone.

To return the instance to its original zone after the experiment completes, you must manually initiate another failover using the Google Cloud console or the `gcloud` CLI.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
