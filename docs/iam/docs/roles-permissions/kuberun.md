---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun/
title: Knative serving roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:52:21.297010+00:00
---

# Knative serving roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/kuberun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Knative serving roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Knative serving. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Knative serving roles

Knative serving offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### KubeRun Events Control Plane Service Agent 

(`roles/kuberun.eventsControlPlaneServiceAgent`) Service account role used to setup authentication for the control plane used by KubeRun Events.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudscheduler.jobs.create` `cloudscheduler.jobs.delete` `cloudscheduler.jobs.get` `logging.sinks.create` `logging.sinks.delete` `logging.sinks.get` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.get` `pubsub.topics.getIamPolicy` `pubsub.topics.setIamPolicy` `resourcemanager.projects.get` `storage.buckets.get` `storage.buckets.update`  
  
#### KubeRun Events Data Plane Service Agent 

(`roles/kuberun.eventsDataPlaneServiceAgent`) Service account role used to setup authentication for the data plane used by KubeRun Events.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudtrace.traces.patch` `monitoring.timeSeries.create` `pubsub.subscriptions.consume` `pubsub.subscriptions.get` `pubsub.topics.get` `pubsub.topics.publish` `resourcemanager.projects.get`  
  
## Knative serving permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
