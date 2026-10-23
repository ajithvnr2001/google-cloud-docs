---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview/
title: About the GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:16.971286+00:00
---

# About the GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  About the GKE On-Prem API Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a brief overview of the GKE On-Prem API and provides links to the Google Distributed Cloud (software only) for bare metal and VMware documentation where you can learn more.

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using standard applications. The GKE On-Prem API runs in Google Cloud's infrastructure. The Google Cloud console, the Google Cloud CLI, and Terraform are clients of the API, and they use the API to create, update, upgrade, and delete clusters in your data center.

## Protect the API with VPC Service Controls

To further secure the GKE On-Prem API, you can protect it using VPC Service Controls.

VPC Service Controls provides additional security for the GKE On-Prem API. Using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that originate outside the perimeter.

To learn more about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

For the greatest protection by VPC Service Controls, ensure that your admin cluster isn't publicly accessible. For more information, see the following Google Distributed Cloud documentation:

  * Bare metal: [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster)

  * VMware: [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/hardening-your-cluster)




## What's next

  * Bare metal:

    * [Choose a tool to manage cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools)
    * [Create a user cluster using GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api)
    * [Create an admin cluster using GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-admin-cluster-api)
    * [Configure a cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster)
  * VMware:

    * [Choose a tool to manage cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools)
    * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)
    * [Configure a cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
