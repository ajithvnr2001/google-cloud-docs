---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/scalability/
title: Config Controller scalability guidelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:00.947681+00:00
---

# Config Controller scalability guidelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/scalability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Config Controller scalability guidelines Stay organized with collections  Save and categorize content based on your preferences. 

This page provides recommendations to help plan your config management architecture on Config Controller instances and keep your Google Cloud resource creation and management within service-level objectives (SLO).

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure and plan capacity and infrastructure needs. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Use namespaced mode

We recommended using Config Connector in [namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced) because it can be easier to manage high numbers of resources. You can set each namespace to correspond to a single namespace, which can help manage quotas and configurations, since resources have read and write quotas per project. Starting in version 1.119.0, you can increase reconciliation rate limits by namespace. By increasing rate limits, you can allow reconciliation for more than 10,000 resources per namespace in a 10 minute interval. Both Config Connector and Config Sync support namespaced mode, which allows for mapping each namespace to a single Google Cloud project.

## Scalability targets

The following table represents values we regularly test. We know that Config Connector can handle larger numbers. We have shown that 30,000 resources can be managed in a single namespace. However there is some tuning needed to make this work. We recommend you review the Namespaced mode for suggestions on these changes.

Config Controller scalability targets are groups of resources tested by Google and with the use of Config Sync GitOps. You can use these targets to help plan your config management architecture.

These targets are not hard limits. Stretching the amount of one resource kind won't necessarily make the Config Controller instance unavailable, but it could reduce the total amount of other resource kinds in the same Config Controller instance that you can deploy.

The tables on this page are intended as references and are not exhaustive.

### Single namespace

The following example shows a Config Controller instance with one Config Connector namespace in the cluster. Config Connector can create and manage the following number of resources in that namespace:

**Resource type** | **Suggested limit**  
---|---  
`SQLInstance` | 450  
`SQLDatabase` | 2,250  
`SQLUser` | 2,500  
`StorageBucket` | 5,000  
`ContainerCluster` | 50  
`ContainerNodepool` | 200  
`IAMServiceAccount` | 2,500  
`IAMPartialPolicy` | 7,500  
  
### Multiple namespaces

The following example shows a Config Controller instance with 50 Config Connector namespaces in a cluster. Config Connector can create and manage the following number of resources in each namespace:

**Resource type** | **Suggested limit**  
---|---  
`SQLInstance` | 9  
`SQLDatabase` | 45  
`SQLUser` | 45  
`StorageBucket` | 100  
`ContainerCluster` | 1  
`ContainerNodepool` | 4  
`IAMServiceAccount` | 50  
`IAMPartialPolicy` | 150  
  
### Config Connector namespaces

Config Controller uses [Config Connector namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced) by default. The following tables shows an example of the number of Config Connector namespaces you can have in a single Config Connector instance.

**`--cluster-ipv4-cidr-block`** | **Number of nodes** | **Number of Config Connector namespaces**  
---|---|---  
/18 | 64 | 600  
/19 | 32 | 300  
/20 (default and recommended) | 16 | 120  
/21 | 8 | 60  
  
## Checking scalability targets

You can use the following resources to help determine if you have reached scalability targets.

### Google Cloud API Quotas

You can [view your Google Cloud API quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage). When some quotas are close to their limits, consider Sharding API quota by Google Cloud projects. To learn more about monitoring and alerting on quota metrics, see [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).

### Config Connector memory use

You can [view your Config Connector memory use in the GKE monitoring dashboard](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing#access). When Config Connector's memory use is close to its limit, consider Sharding by namespace.

## Scaling up Config Controller

If you have reached scalability targets, you should consider further scaling up your Config Controller instances. This section outlines different methods you can use to scale up your Config Controller instances.

### Sharding by namespace

If you reach a scalability target with a single Config Connector namespace, you can [Configure Config Connector to manage resources in your namespaces](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced#project-namespace).

**Note:** this method works if Config Connector is installed in namespaced mode, which is the default for Config Controller.

Each namespace uses its own service accounts and operator workloads, which allows Config Connector to manage your resources at scale. If you use one Config Connector instance to manage multiple Google Cloud projects, you can use one Config Connector namespace to manage each Google Cloud project.

### Sharding API quota by Google Cloud projects

If you reach a scalability target due to reaching Google Cloud API Quotas, you can bind different IAM service accounts owned by different Google Cloud projects to different namespaces where Config Connector is installed in namespaced mode. You can then [split your resources into different projects](https://docs.cloud.google.com/config-connector/docs/troubleshooting#split_your_resources_into_multiple_projects).

### Sharding by Config Connector instances

If you reach a scalability target with multiple Config Connector namespaces, you can [create and use more than one Config Controller instance](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup#create). With more than one Config Controller instance, you can shard your resource config management, for example, by different development environments, application teams, or GitOps directories within your organization.

## Other scalability considerations

### Google Cloud API quotas

If you've run into errors indicating that you've exceeded the API quota limit, you might have created too many Config Connector resources of the same Kind under the same project. Those resources can generate too many API requests to the same API endpoint because of the [reconciliation strategy](https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation) in Config Connector.

To resolve this, you can either shard API quota by Google Cloud project or request [a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### GKE limitations

Since Config Controller is built on top of GKE, there are limitations from GKE that you should consider. The following sections cover specific considerations related to Config Controller. For more information about general limits and best practices for large GKE clusters, see [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters).

#### Kubernetes service account limit

​​The number of [Kubernetes Service Accounts (KSA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#kubernetes-service-accounts) created in a single GKE cluster should not exceed 3,000 because you might encounter a [`gke-metadata-server` Pod crash issue](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-security#metadata-server-crashes).

Whenever you add a Config Connector namespace, it also creates a Kubernetes service account.

#### GKE control plane performance issues

The [GKE cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) can have performance issues if a Config Controller instance has too many Config Connector namespaces. You should limit the number of Config Connector namespaces to under 500 per cluster.

Whenever you add a Config Connector namespace, it also creates a controller pod.

## What's next

  * Learn [how to shard Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/sharding)
  * Get help with [troubleshooting Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
