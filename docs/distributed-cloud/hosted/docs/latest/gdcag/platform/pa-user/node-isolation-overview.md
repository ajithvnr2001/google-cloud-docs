---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/node-isolation-overview/
title: Node isolation overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:04.508341+00:00
---

# Node isolation overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/node-isolation-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Node isolation overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the benefits and limitations of node isolation in a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster. Node isolation with dedicated node pools enhances cluster security by giving you precise control over where specific pods run within the cluster.

Workload isolation provides some benefits, such as:

  * Reduced risk of privilege escalation attacks in your Kubernetes cluster.
  * More control over pods that require additional resources.



For these cases, consider isolating your container workloads in dedicated node pools for more control and optimization. Be sure to also consider the limitations so you make an informed decision on the added maintenance cost that node isolation requires.

This document is intended for audiences such as IT administrators within the platform administrator group who are responsible for managing the node pools of a Kubernetes cluster, and application developers within the application operator group who are responsible for managing container workloads. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Why should I isolate my workloads?

While not mandatory, dedicating node pools to specific container workloads can prevent potential problems. However, this approach demands more management, and is often not essential.

Kubernetes clusters use privileged GDC-managed workloads to enable specific cluster capabilities and features, such as metrics gathering. These workloads are given special permissions to run correctly in the cluster.

Workloads that you deploy to your nodes might have the potential to be compromised by a malicious entity. Running these workloads alongside privileged GDC-managed workloads means that an attacker who breaks out of a compromised container can use the credentials of the privileged workload on the node to escalate privileges in your cluster.

Dedicated node pools are also useful when you must schedule pods that require more resources than others, such as more memory or more local disk space. 

You can use the following mechanisms to schedule your workloads on a dedicated node pool:

  * **[Node taints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints)** : informs your Kubernetes cluster to avoid scheduling workloads on specific nodes without a corresponding toleration.
  * **[Node affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity)** : informs your Kubernetes cluster to schedule specific pods on dedicated nodes.



Node isolation is an advanced defense-in-depth mechanism that you must only use alongside other isolation features, such as minimally-privileged containers and service accounts. Node isolation might not cover all escalation paths, and must never be used as a primary security boundary.

## How node isolation works

To implement node isolation for your workloads, you must do the following:

  1. Taint and label a node pool for your workloads.

  2. Update your workloads with the corresponding toleration and node affinity rule.




This guide assumes that you start with one node pool in your cluster. Using node affinity in addition to node taints isn't mandatory, but we recommend it because you benefit from greater control over scheduling.

## Recommendations and best practices

After setting up node isolation, we recommend that you do the following:

  * When creating new node pools, prevent most GDC-managed workloads from running on those nodes by adding your own taint to those node pools.

  * Whenever you deploy new workloads to your cluster, such as when installing third-party tooling, audit the permissions that the pods require. When possible, avoid deploying workloads that use elevated permissions to shared nodes.




## Limitations

The following limitations apply to pods running in an isolated node pool:

  * Attackers can still initiate Denial-of-Service (DoS) attacks from the compromised node.

  * If you deploy `DaemonSet` resources that have elevated permissions and can tolerate any taint, those pods might be a pathway for privilege escalation from a compromised node.

  * Compromised nodes can still read many resources, including all pods and namespaces in the cluster.

  * Compromised nodes can access secrets and credentials used by every pod running on that node.

  * Compromised nodes can still bypass egress network policies.

  * Using a separate node pool to isolate your workloads can impact your cost efficiency, autoscaling, and resource utilization.

  * Some GDC-managed workloads must run on every node in your cluster, and are configured to tolerate all taints.




## What's next

  * [Isolate container workloads in dedicated node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/isolate-container-workloads)
  * [Kubernetes cluster overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
