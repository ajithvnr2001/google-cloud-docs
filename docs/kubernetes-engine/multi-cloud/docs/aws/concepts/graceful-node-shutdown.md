---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/graceful-node-shutdown/
title: Graceful node shutdown in GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:41.120688+00:00
---

# Graceful node shutdown in GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/graceful-node-shutdown/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Graceful node shutdown in GKE on AWS Stay organized with collections  Save and categorize content based on your preferences. 

Starting from version 1.26, GKE on AWS automatically enables [Graceful Node Shutdown](https://kubernetes.io/blog/2021/04/21/graceful-node-shutdown-beta). This feature manages the graceful termination of Pods during node shutdowns. Graceful termination lets Pods save their state, and release resources before the node is shut down. This method of terminating Pods minimizes the risk of data loss. It also minimizes the risk of interruptions to other Pods and services that rely on or interact with the Pods being shut down, thus enhancing the resilience of your clusters.

## How it works

An event such as scheduled maintenance, node scaling, or a hardware issue, triggers a node shutdown. The `kubelet` component detects the event and initiates the graceful node termination process by instructing `systemd` to delay the system shutdown for a specified duration. This delay gives the node time to drain and evict the Pods running on it.

The goal of graceful node termination is to gracefully terminate both non-system and critical system Pods before the node shuts down. The following default settings are used:

  * `ShutdownGracePeriod`: 30 seconds
  * `ShutdownGracePeriodCriticalPods`: 15 seconds



These settings give non-system Pods 15 seconds to gracefully terminate before they are forcibly stopped. Critical system Pods have 15 seconds to shut down after the non-system Pods have terminated. However, since the feature operates on a best-effort basis, there's a possibility that a node might not be able to shut down gracefully within the designated 30-second period.

## Triggers and limitations

Events that trigger graceful node shutdown include planned events such as the following:

  * User-commanded shutdowns
  * Termination of instances
  * Scheduled maintenance
  * Scaling down a cluster



In these scenarios, the `kubelet` detects the node shutdown event and initiates the graceful node shutdown process.

In contrast, graceful node shutdown can't be activated when the shutdown command doesn't trigger the `systemd` inhibitor lock mechanism that the `kubelet` component relies on. Examples of those kinds of situations include the following:

  * Network disconnections
  * Hardware malfunctions
  * Insufficient resources such as memory or CPU
  * Unexpected power outages.



In these cases, the node might shut down abruptly, potentially causing disruptions or data loss.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
