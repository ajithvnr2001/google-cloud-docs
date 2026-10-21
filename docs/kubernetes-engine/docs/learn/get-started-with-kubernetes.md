---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes/
title: Start learning about Kubernetes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:43.563268+00:00
---

# Start learning about Kubernetes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Start learning about Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

GKE is based on the open source container orchestration platform Kubernetes, and a lot of the documentation on this site assumes that you're already familiar with basic Kubernetes concepts and terminology. If you're not, this page provides a quick overview of Kubernetes fundamentals, with links to recommended reading to get you started.

## Key concepts

The following are some key concepts that we use throughout the GKE documentation. This is not an exhaustive list of Kubernetes concepts; you can find much more to read and explore in the provided topics from the Kubernetes documentation and our recommended reading.

### Nodes and clusters

All Kubernetes workloads run on _nodes_. In GKE, a node is a Compute Engine virtual machine (VM). On other Kubernetes platforms, a node could be either a physical or virtual machine. Each node is managed by the Kubernetes control plane and has all the necessary components to run Pods. A _cluster_ is a set of nodes that can be treated together as a single entity, on which you deploy a containerized application.

Learn more in the Kubernetes documentation:

  * [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
  * [Cluster architecture](https://kubernetes.io/docs/concepts/architecture/)
  * [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)



### Namespaces

Kubernetes namespaces provide a mechanism for further grouping and selecting resources such as Pods and Services within a cluster, for example if you have multiple application teams running workloads on a single cluster.

Learn more in the Kubernetes documentation:

  * [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)



### Pods

In Kubernetes, containerized applications run inside a _Pod_. A Pod is the smallest deployable unit of computing that you can create and manage in Kubernetes. A Pod has one or more _containers_. When a Pod runs multiple containers (for example, an application server and a [proxy server](https://wikipedia.org/wiki/Proxy_server)), the containers are managed as a single entity and share the Pod's resources.

Learn more in the Kubernetes documentation:

  * [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
  * [Containers](https://kubernetes.io/docs/concepts/containers/)



### Controllers

Kubernetes controllers track and manage the state of your clusters and workloads, based on the desired state that you specify (for example, "I would like to run three of this Pod on this cluster, with this container in each Pod"). Different controllers track different Kubernetes resource types, including the following:

  * **Deployments** : A _Deployment_ is a Kubernetes object that represents one or more identical Pods, called _replicas_. A Deployment runs multiple replicas of the Pods distributed among the nodes of a cluster. A Deployment automatically replaces any Pods that fail or become unresponsive.
  * **StatefulSet** : A _StatefulSet_ is like a Deployment but maintains a persistent unique identity for each of its Pods. StatefulSets can be useful in applications with persistent state (stateful applications).
  * **DaemonSets** : A Kubernetes _DaemonSet_ lets you add default Pods to some or all of your nodes. These are often "helper" services for your workloads, such as a log-collection daemon or a monitoring daemon.
  * **ReplicaSets** : A _ReplicaSet_ is a set of identical Pods. A ReplicaSet is usually managed as part of a Deployment.



Learn more in the Kubernetes documentation:

  * [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  * [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  * [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
  * [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)



### Kubernetes Service

By default, you can't control which cluster node a Pod is running on, so Pods don't have stable IP addresses. To get an IP address for an application running in Kubernetes, you must define a networking abstraction on top of its Pods called a [Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#services). A Kubernetes Service provides a stable networking endpoint for a set of Pods. There are several [types of Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#types_of_services), including `LoadBalancer` Services that expose an external IP address so that you can reach applications from outside their cluster.

Kubernetes also has a built-in DNS system for internal address resolution, which assigns DNS names (for example, `helloserver.default.cluster.local`) to Services. This allows Pods inside the cluster to reach other Pods in the cluster using a stable address. You can't use this DNS name outside the cluster, such as from Cloud Shell.

Learn more in the Kubernetes documentation:

  * [Services](https://kubernetes.io/docs/concepts/services-networking/service/)



### Storage

If your applications need to save data that exists beyond the lifetime of their Pod (stateful applications), you can use a Kubernetes _PersistentVolume_ object to provision this storage. In GKE, PersistentVolume storage is backed by Compute Engine disks. You can also choose to use ephemeral storage, which is destroyed when the corresponding Pod terminates.

Learn more in the Kubernetes documentation:

  * [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
  * [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)



### Kubernetes control plane

The Kubernetes _control plane_ is a set of system components that manage the overall state of your cluster, including the _Kubernetes API server_ that lets you interact with your clusters and applications by using `kubectl` and other tools, a _scheduler_ to schedule Pods on available nodes, and the _controllers_ that track and manage cluster state. In GKE, the control plane is provided and managed by Google Cloud.

Learn more in the Kubernetes documentation:

  * [Control plane components](https://kubernetes.io/docs/concepts/architecture/#control-plane-components)



### Role-based access control (RBAC)

Kubernetes includes a _role-based access control (RBAC)_ mechanism that lets you create authorization policies for accessing your clusters and their resources. When using GKE, you'll often use a combination of Kubernetes RBAC and Google Cloud's Identity and Access Management to secure your applications.

Learn more in the Kubernetes documentation:

  * [Role-based access control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)



## Recommended reading

This section provides links to recommended resources for learning more about Kubernetes. In particular, [Kubernetes.io](https://kubernetes.io), the official Kubernetes website, has lots of up-to-date, reliable material about all things Kubernetes.

### Guides and tutorials

  * [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/): A thorough conceptual overview of Kubernetes. [Why you need Kubernetes and what it can do](https://kubernetes.io/docs/concepts/overview/#why-you-need-kubernetes-and-what-can-it-do) is a great introduction to the problems that Kubernetes can solve.
  * [Tutorial: Learn Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/): Walks you through the basics of Kubernetes with a simple example.
  * [Tutorial: Introducing containers](https://docs.cloud.google.com/kubernetes-engine/docs/learn/containers): Learn about containers and container orchestration with a simple example application, finishing with the example running on GKE.
  * [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/): When you're ready to move beyond the basics, this section of the Kubernetes documentation provides tutorials on a variety of Kubernetes topics, from stateful applications to security.



### Reference documentation

  * [Kubernetes glossary](https://kubernetes.io/docs/reference/glossary/?fundamental=true): A comprehensive, standardized list of Kubernetes terminology. If you're not sure about a Kubernetes term, here's where to look it up!



### Videos

  * [Learn Kubernetes with Google](https://www.youtube.com/playlist?list=PLxNYxgaZ8Rscf-XJ5VfXgbDAk1vL4xaMl): A playlist of video guides from Google that cover different Kubernetes features and functionalities, with material for both developers and operators.



### Comic

  * [Kubernetes comic](https://cloud.google.com/kubernetes-engine/kubernetes-comic): Discover the history of Kubernetes and how to use it for continuous integration and delivery, with the unlikely help of the Goddess of Wisdom (and containerized applications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
