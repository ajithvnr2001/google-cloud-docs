---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset/
title: About StatefulSets in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:47.076427+00:00
---

# About StatefulSets in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About StatefulSets in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the use of _StatefulSet_ objects in Google Kubernetes Engine (GKE). You can also learn how to [Deploy a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).

## About StatefulSets

StatefulSets represent a set of Pods with unique, persistent identities, and stable hostnames that GKE maintains regardless of where they are scheduled. The state information and other resilient data for any given StatefulSet Pod is maintained in [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) associated with each Pod in the StatefulSet. StatefulSet Pods can be restarted at any time.

For [stateless applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview#stateless_applications), use [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

StatefulSets function similarly in GKE and in Kubernetes. This document describes any GKE-specific considerations. To learn how StatefulSets work, see the [Kubernetes documentation about StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

### Plan networking for StatefulSets

StatefulSets provide persistent storage in the form of a PersistentVolume and a unique network identity (hostname). The following table includes the caveats that application operators should be aware of when configuring a StatefulSet:

Networking caveat | Description | Best practice  
---|---|---  
GKE Services instead of fixed IP addresses  |  Although Pod replicas have a unique ordinal index, support per-replica volumes, and network identity (hostname), the IP addresses that are assigned to a replica can change if GKE reschedules or evicts a Pod. |  To mitigate networking issues, the architecture should use Kubernetes Service resources. For more information, see [Types of Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#types-of-services). **Note:** Applications on Kubernetes may cache IP addresses if other components are installed. For example, [JVM caches name lookups](https://docs.oracle.com/en/java/javase/18/docs/api/java.base/java/net/doc-files/net-properties.html#networkaddress.cache.ttl) indefinitely by default if a security manager is installed. As an application developer, you should audit your application to ensure that it does not cache IP addresses that are resolved from these services.  
Headless Services  |  When initialized, a StatefulSet is paired with a matching headless service. |  Ensure that the `metadata.name` in your Service matches the `serviceName` field in your StatefulSet. This enables each Pod in your application to be addressed at a unique, well-defined network address. Additionally, the headless service provides a multi-IP record for each replica in your StatefulSet, allowing full peer discovery.  
Peer discovery  |  Stateful applications require a minimum number (quorum) of replicas to function with full availability. |  As Pods can crash, be rescheduled, or evicted, each replica in a StatefulSet should be able to leave and rejoin quorum. Applications that require peering should have the capability to discover other peers through headless Services in Kubernetes.  
Health check based on readiness probes and liveness probes  |  Your application should have properly configured readiness, liveness, and startup probes where applicable. Selecting timeouts for each probe is dependent on the requirements of your application. |  For readiness probes, follow these best practices to configure your application to mark readiness when it is ready to serve traffic:

  * **Liveness probes:** You can use liveness probes to signal if a container is healthy. For example, a database replica can use a liveness probe to indicate that GKE should restart the replica, such as deadlock condition 
  * **Readiness probes:** You can use readiness probes to remove a replica from serving traffic temporarily. For example, if you have a database replica that needs to perform a backup, you might use a readiness probe to temporarily stop receiving requests. 
  * **Startup probe:** You can use startup probes to delay health checks until long running initializations are complete. For example, if you have a database replica, you might use a startup probe to wait for initialization of stored data from disk. 

  
  
To read more about probes, see [Configure Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes).

## Work with StatefulSets

To learn how to deploy StatefulSets in your GKE cluster and interact with them, see the Kubernetes documentation about [StatefulSet basics](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/).

## What's next

  * [Learn how to deploy a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps)
  * [Learn how to update StatefulSets using rolling updates](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#rolling-update)
  * [Learn more about deploying workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview)
  * [Read more about StatefulSets in the Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  * [Take a tutorial about upgrading a cluster running a stateful workload](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/upgrading-stateful-workload)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
