---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/admin-cluster-rbac-policies/
title: Admin cluster RBAC policies \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:53.413891+00:00
---

# Admin cluster RBAC policies  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/admin-cluster-rbac-policies/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Admin cluster RBAC policies Stay organized with collections  Save and categorize content based on your preferences. 

When you fill in the [`gkeConnect` section](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#gkeconnect-section) in your admin cluster configuration file, the cluster is registered to your [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs) during creation or update. To enable fleet management functionality, Google Cloud deploys the [Connect agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) and creates a Google service account that represents the project that the cluster is registered to. The Connect agent establishes a connection with the service account to handle requests to the cluster's Kubernetes API server. This enables access to cluster and workload management features in Google Cloud, including access to the [Google Cloud console](https://docs.cloud.google.com/cloud-console), which lets you interact with your cluster.

The admin cluster's Kubernetes API server needs to be able to authorize requests from the Connect agent. To ensure this, the following [role-based access control (RBAC) policies](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) are configured on the service account:

  * An [**impersonation policy**](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) that authorizes the Connect agent to send requests to the Kubernetes API server on behalf of the service account.

  * A **permissions policy** that specifies the operations that are allowed on other Kubernetes resources.




The service account and RBAC policies are needed so that you can manage the lifecycle of your user clusters in the Google Cloud console.

## What's next

  * [Create user clusters in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
