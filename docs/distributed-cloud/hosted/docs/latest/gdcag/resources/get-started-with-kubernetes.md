---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/get-started-with-kubernetes/
title: Kubernetes concepts for GDC \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:45.040499+00:00
---

# Kubernetes concepts for GDC  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/get-started-with-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Kubernetes concepts for GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the basic fundamentals of the open source container orchestration platform Kubernetes. Many components of Google Distributed Cloud (GDC) air-gapped are based on Kubernetes, and a lot of the documentation assumes that you're already familiar with basic Kubernetes concepts and terminology. If you're not familiar with Kubernetes, use this document as a reference for recommended reading to get you started.

Learning Kubernetes basics is essential for designing, deploying, and managing GDC applications and underlying system components. The following technical professionals must understand Kubernetes to successfully operate GDC:

  * Operators within the infrastructure operator group responsible for installing and maintaining the underlying GDC software and hardware infrastructure.
  * Administrators within the platform administrator group responsible for designing resilient infrastructure and application architectures on GDC.
  * Developers within the application operator group responsible for building applications.



For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

## About Kubernetes

Kubernetes is an open source container orchestration platform. At its core, a Kubernetes cluster is a set of worker machines called nodes that run containerized applications. The entire cluster is managed by the control plane, which includes components like the API server, scheduler, and etcd database, and is responsible for maintaining the state of the cluster.

Applications are packaged into pods, the smallest deployable units in Kubernetes, which can contain one or more containers and run on the nodes. To organize resources within a cluster, often for different teams or environments, Kubernetes uses namespaces.

The lifecycle and state of pods are managed by controllers. For example, `Deployment` objects manage rolling updates and `ReplicaSet` objects ensure a specific number of pod replicas are running. To provide stable network endpoints, such as IP addresses and DNS names for accessing pods, Kubernetes uses services.

Since container storage is ephemeral by default, Kubernetes offers various storage abstractions, such as volumes and persistent volumes to manage data.

To secure access to cluster resources and the Kubernetes API, Kubernetes uses role-based access control (RBAC) to define roles, cluster roles, and bindings to grant specific permissions to users and service accounts.

## Key concepts

The following are some key concepts that we use throughout the GDC documentation. This is not an exhaustive list of Kubernetes concepts. You can find much more to read and explore in the provided topics from the Kubernetes documentation and our recommended reading.

### Nodes and clusters

All Kubernetes workloads run on _nodes_. In GDC, a node is a virtual machine (VM). On other Kubernetes platforms, a node could be either a physical or virtual machine. Each node is managed by the Kubernetes control plane and has all the necessary components to run pods. A _cluster_ is a set of nodes that can be treated together as a single entity, on which you deploy a containerized application.

Learn more in the Kubernetes documentation:

  * [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
  * [Cluster architecture](https://kubernetes.io/docs/concepts/architecture/)
  * [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)



### Kubernetes control plane

The Kubernetes _control plane_ is a set of system components that manage the overall state of your cluster, including the _Kubernetes API server_ that lets you interact with your clusters and applications by using the kubectl CLI and other tools, a _scheduler_ to schedule pods on available nodes, and the _controllers_ that track and manage cluster state. The control plane is provided and managed by GDC.

For more information, see the Kubernetes [Control plane components](https://kubernetes.io/docs/concepts/architecture/#control-plane-components) documentation.

### Pods

In Kubernetes, containerized applications run inside a _pod_. A pod is the smallest deployable unit of computing that you can create and manage in Kubernetes. A pod has one or more _containers_. When a pod runs multiple containers, such as an application server and a proxy server, the containers are managed as a single entity and share the pod's resources.

Learn more in the Kubernetes documentation:

  * [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
  * [Containers](https://kubernetes.io/docs/concepts/containers/)



### Namespaces

Kubernetes namespaces provide a mechanism for further grouping and selecting resources, such as pods and services, within a cluster. For example, if you have multiple application teams running workloads on a single cluster.

For more information, see the Kubernetes [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) documentation.

### Controllers

Kubernetes controllers track and manage the state of your clusters and workloads, based on the state that you specify. For example, you could set the behavior for a cluster to run three pods, with a designated container in each pod. Different controllers track different Kubernetes resource types, including the following:

  * **Deployment** : A `Deployment` is a Kubernetes object that represents one or more identical pods, called _replicas_. A deployment runs multiple replicas of the pods distributed among the nodes of a cluster. A deployment automatically replaces any pods that fail or become unresponsive.
  * **StatefulSet** : A `StatefulSet` object is like a deployment but maintains a persistent unique identity for each of its pods. `StatefulSet` objects can be useful in applications with persistent state, like stateful applications.
  * **DaemonSet** : A `DaemonSet` object lets you add default pods to some or all of your nodes. These are often helper services for your workloads, such as a log collection daemon or a monitoring daemon.
  * **ReplicaSet** : A `ReplicaSet` object is a set of identical pods. A `ReplicaSet` is usually managed as part of a `Deployment` object.



Learn more in the Kubernetes documentation:

  * [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  * [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  * [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
  * [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)



### Kubernetes Service

By default, you can't control which cluster node a pod is running on, so pods don't have stable IP addresses. To get an IP address for an application running in Kubernetes, you must define a networking abstraction on top of its pods called a [Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#services). A Kubernetes Service provides a stable networking endpoint for a set of pods. There are several [types of services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#types_of_services), including `LoadBalancer` services, that expose an external IP address so that you can reach applications from outside the cluster.

Kubernetes also has a built-in DNS system for internal address resolution, which assigns a DNS name, such as `helloserver.default.cluster.local` to services. This lets pods within the cluster reach other pods in the cluster using a stable address. You can't use this DNS name outside the cluster, such as from the gdcloud CLI.

For more information, see the Kubernetes [Services](https://kubernetes.io/docs/concepts/services-networking/service/) documentation.

### Storage

If your applications need to save data that exists beyond the lifetime of its pod, such as in stateful applications, you can use a Kubernetes `PersistentVolume` object to provision this storage. You can also choose to use ephemeral storage, which is destroyed when the corresponding pod terminates.

Learn more in the Kubernetes documentation:

  * [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
  * [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)



### Role-based access control

Kubernetes includes a _role-based access control (RBAC)_ mechanism that lets you create authorization policies for accessing your clusters and their resources. When using GDC, you'll often use a combination of Kubernetes RBAC and GDC's Identity and Access Management (IAM) to secure your applications.

For more information, see the Kubernetes [Role-based access control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation.

## Recommended reading

This section provides links to recommended resources for learning more about Kubernetes. In particular, [Kubernetes.io](https://kubernetes.io/), the official Kubernetes website, has comprehensive, reliable material about all things Kubernetes.

### External guides and tutorials

  * [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/): A thorough conceptual overview of Kubernetes.
  * [Tutorial: Learn Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/): Learn the basics of Kubernetes with an example.
  * [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/): When you're ready to move beyond the basics, this section of the Kubernetes documentation provides tutorials on a variety of Kubernetes topics, from stateful applications to security.



### Reference documentation

  * [Kubernetes glossary](https://kubernetes.io/docs/reference/glossary): A comprehensive, standardized list of Kubernetes terminology. If you're not sure about a Kubernetes term, reference the glossary.



## What's next

  * [Kubernetes workloads for HA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/enhance-kubernetes-ha)
  * [Kubernetes clusters in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
