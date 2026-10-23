---
url: https://docs.cloud.google.com/apigee/docs/hybrid/kubernetes-resources/
title: Kubernetes and custom resources used by Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:27.001641+00:00
---

# Kubernetes and custom resources used by Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/kubernetes-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Kubernetes and custom resources used by Apigee Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the Kubernetes resources and custom resources that are used by Apigee installations. Users installing Apigee should have role-based access control (RBAC) for these resources, in most cases `Create`, `Delete`, `Update`, and `Patch`.

##  Third party resources 

###  Cert Manager 

CRD  
---  
`ClusterIssuer`  
`Issuer`  
`Certificate`  
  
##  Kubernetes and variants 

###  Kubernetes 

Resource  
---  
`StorageClass` (Optional, if the default StorageClass is not used. For information on changing the default and creating a custom storage class, see [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/latest/cassandra-config).)  
`PriorityClass` (Required for `apigeectl` only)  
`Namespace`  
`ServiceAccount`  
`ClusterRole`  
`ClusterRoleBinding`  
`Role`  
`RoleBinding`  
`CustomResourceDefinition`  
`MutatingWebhookConfiguration`  
`ValidatingWebhookConfiguration`  
`Secret`  
`ConfigMap`  
`Deployment`  
`Job`  
`CronJob`  
  
###  OpenShift 

Resource  
---  
`SecurityContextConstraints`  
  
##  Apigee resources 

###  Apigee 

CRD | Definition  
---|---  
`ApigeeDatastore` | `ApigeeDatastore` manages Cassandra StatefulSet and ensures the Apigee hybrid setup has a reliable Cassandra database to store all its configurations, keys, and tokens. The `ApigeeDatastore` is not associated with any of the organizations and environments.  
`ApigeeDeployment` | `ApigeeDeployment` is a CRD in Apigee hybrid used to configure and manage the Apigee runtime components (like Message Processor, Router) deployed within a Kubernetes cluster. It acts as a blueprint defining which components to deploy, their configurations, and desired state, making it a central tool for managing Apigee in a hybrid setup.  
`ApigeeOrganization` | `ApigeeOrganization` is a CRD used in Apigee hybrid to represent an Apigee organization within the hybrid runtime plane. This CRD allows you to create and manage Apigee organizations directly within your Kubernetes cluster, enabling you to configure and control various aspects of your Apigee environment, including API proxies, products, developers, and other organizational settings. The `ApigeeOrganization` resources can support multiple environments within an organization (org-wide scope).  
`ApigeeEnvironment` | `ApigeeEnvironment` is a CRD used in Apigee hybrid to represent an Apigee environment within a Kubernetes cluster. It enables the creation and management of Apigee environments directly within the cluster, allowing for control over environment-specific settings, deployments, and configurations. This facilitates better organization and management of different deployment stages (e.g., dev, test, prod) within the hybrid Apigee setup. The `ApigeeEnvironment` resources support one environment and are therefore created for each environment separately.  
`ApigeeRedis` | `ApigeeRedis` is a CRD used in Apigee hybrid to provision and manage a Redis instance specifically for Apigee components within a Kubernetes cluster. `ApigeeRedis` is used for storing cluster-level rate limit counts used for distributed rate limiting in Apigee and Apigee hybrid. This applies only if SpikeArrest policy has the option [ UseEffectiveCount](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount) enabled. This dedicated `ApigeeRedis` instance serves as a high-performance data store, enabling functionalities like caching, session management, and rate limiting for the Apigee runtime plane.  
`ApigeeRoute` | `ApigeeRoute` is a CRD used in Apigee hybrid to define and manage routing configurations for external traffic to reach Apigee services running within a Kubernetes cluster. This CRD allows you to specify ingress rules, load balancing, and other routing policies to direct incoming requests to the appropriate Apigee components, ensuring efficient and secure access to your APIs.  
`ApigeeRouteConfig` | `ApigeeRouteConfig` is a CRD in Apigee hybrid used to configure routing rules for external traffic to access Apigee services running in a Kubernetes cluster. It enables you to define hostnames, paths, and associated backend services to direct incoming requests to the correct Apigee components, providing flexibility and control over how external clients interact with your Apigee deployment.  
`ApigeeTelemetry` | `ApigeeTelemetry` is a CRD in Apigee hybrid used to configure the collection and export of telemetry data (logs, metrics, traces) from the Apigee runtime plane components running in a Kubernetes cluster. This CRD allows you to specify destinations like Google Cloud Operations or other compatible systems, enabling centralized monitoring, analysis, and troubleshooting of your Apigee deployment.  
`ApigeeIssues` | `ApigeeIssues` is a CRD in Apigee hybrid used to track and manage known issues or problems within the Apigee platform deployment. It serves as a centralized repository for recording, categorizing, and resolving issues, facilitating collaboration between teams and ensuring efficient troubleshooting and problem resolution within the hybrid environment.  
`CassandraDataReplication` | `CassandraDataReplication` CRD in Apigee Hybrid is specifically designed for managing data replication between different Cassandra clusters in a multi-region Apigee hybrid deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
