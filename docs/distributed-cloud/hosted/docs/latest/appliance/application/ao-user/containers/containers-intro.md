---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro/
title: Container workloads in GDC \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:45.332618+00:00
---

# Container workloads in GDC  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Container workloads in GDC Stay organized with collections  Save and categorize content based on your preferences. 

This overview page explains the operating model for container workloads in a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. GDC provides a managed Kubernetes service that supports Kubernetes-native container applications that are widely consumed and supported on Google Kubernetes Engine (GKE).

This page is for developers within the application operator group, who are responsible for managing application workloads for their organization.

## Kubernetes applications for a disconnected environment

_GKE on GDC_ is a managed Kubernetes service that incorporates many GKE features into your GDC device by default. This service eliminates the need to install, upgrade, integrate, and run open source Kubernetes by yourself. You can operate and maintain the provided Kubernetes distribution with a standard KRM API like any other Kubernetes offering that is declarative and idempotent. Likewise, GKE on GDC is offered from the GDC console, gdcloud CLI, and Terraform. For more information on key Kubernetes concepts, see GKE documentation for [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes).

## Container workload state

Containers in GDC are deployed to Kubernetes clusters as the following:

  * Stateless workloads
  * Stateful workloads



You can scale out your GDC Kubernetes cluster nodes based on the requirements of your container workloads, even after cluster provisioning, as your compute requirements evolve.

Kubernetes provides several built-in workload resources to accomplish your preferred container application state. For more information, see Kubernetes [workloads](https://kubernetes.io/docs/concepts/workloads/) documentation.

### Stateless workloads

_Stateless workloads_ are applications that do not store data or application state to the Kubernetes cluster or to persistent storage. Instead, data and application state stay with the client, which makes stateless applications more scalable. For example, a frontend application can be stateless: you deploy multiple replicas to increase its availability and scale down when demand is low, and the replicas have no need for unique identities.

Kubernetes uses the [`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) resource to deploy stateless applications as uniform, non-unique [Pods](https://kubernetes.io/docs/concepts/workloads/pods/). Deployments manage the _desired state_ of your application, such as the following:

  * The amount of Pods to run your application.
  * The version of the container image to run.
  * The labels of the Pods.



You can change the desired state dynamically through updates to the `Deployment` resource's `Pod` specification.

Stateless applications are in contrast to stateful workloads, which use persistent storage to save data and application state.

### Stateful workloads

_Stateful workloads_ are applications that save data to persistent disk storage for use by the server, by clients, and by other applications. An example of a stateful application is a database or key-value store to which data is saved and retrieved by other applications. You must provision persistent storage for your stateful application to use.

Kubernetes uses the [`StatefulSet`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) resource to deploy stateful applications. Pods in `StatefulSet` resources are not interchangeable: each Pod has a unique identifier that is maintained no matter where it is scheduled.

Stateful applications are different from stateless workloads, in which client data is not saved to the server between sessions.

#### Persistent storage for containers

GDC provides persistent block and file storage through [`PersistentVolumeClaim`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PVC) objects. A PVC is a request for storage which is referenced by a `Pod` object. A Pod is a group of one or more containers, with shared storage and network resources. A PVC has an independent lifecycle from the Pod, which lets it persist beyond a single Pod.

You can dynamically provision persistent storage for your stateful workloads so that the underlying volumes are created on demand. In GDC, you configure dynamic provisioning by creating one of the following pre-installed `StorageClass` objects:

  * `standard-rwo`: The `ReadWriteOnce` (RWO) block storage class. The volume can only be accessed by one node at a time. This storage class features an input and output operations per second (IOPS) guarantee and limit of 3 IOPS per GiB.

  * `system-performance-rwo`: The `ReadWriteOnce` performance block storage class. This storage class is a more performant version of RWO storage that features an IOPS guarantee and limit of 30 IOPS per GiB.




You can also create a [`VolumeSnapshot`](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) object to copy your container application's storage volume at a specific point in time without creating an entirely new volume. For example, a database administrator could create a volume snapshot to back up databases before performing edit or delete modifications.

## What's next

  * [Create stateless workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateless-workloads)
  * [Create stateful workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateful-workloads)
  * [Access persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/access-persistent-storage)
  * [Deploy a containerized web server app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/deploy-container-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
