---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/ilb-service/
title: Configure internal load balancers \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:57.175750+00:00
---

# Configure internal load balancers  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/ilb-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure internal load balancers Stay organized with collections  Save and categorize content based on your preferences. 

Internal load balancers (ILB) expose services within the organization from an internal IP pool assigned to the organization. An ILB service is never accessible from any endpoint outside of the organization.

By default, you can access ILB services within the same project from any cluster in the organization. The default [project network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview) doesn't let you access any project resources from outside the project, and this restriction applies to ILB services as well. If the Platform Administrator (PA) configures project network policies that allow access to your project from other projects, then the ILB service is also accessible from those other projects in the same organization.

## Before you begin

To configure ILBs, you must have the following:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project).
  * The necessary identity and access roles:

    * Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.



## Create an internal load balancer

Create ILBs using three different methods in GDC:

  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview) to create ILBs.
  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/networking-api-overview) to create ILBs



You can target pod or VM workloads using the KRM API and gdcloud CLI. You can only target workloads in the cluster where the `Service` object is created when you use the Kubernetes Service directly from the Kubernetes cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
