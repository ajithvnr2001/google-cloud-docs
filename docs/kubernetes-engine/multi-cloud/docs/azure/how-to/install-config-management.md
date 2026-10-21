---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/install-config-management/
title: Install Config Sync and Policy Controller \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:54.528855+00:00
---

# Install Config Sync and Policy Controller  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/install-config-management/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install Config Sync and Policy Controller

Config Sync and Policy Controller enforce a common configuration across your entire infrastructure. You define configurations, such as custom security policies. These configurations are stored in a version-controlled source of truth, such as a Git repository. Config Sync and Policy Controller then ensure that your infrastructure aligns with these configurations.

## Before you begin

If you host your Config Sync source of truth at a location that's inaccessible from your Azure Virtual Network (VNet), you must open outbound access to your source of truth host from your [node pool security group](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/security-groups#node_pool_security_groups). The following list contains default ports based on your authentication method.

Authentication method | Port  
---|---  
Access to Git with [SSH key pair](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-ssh) | 22  
Access to Git with [Cookiefile](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-cookiefile) | 443  
Access to Git or Helm with [Personal access token](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-token) | 443  
Access to Git with [Google Cloud service account](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#google-service-account) | 443  
Access to OCI or Helm with [`gcenode`](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-gcenode) | 443  
Access to OCI or Helm with [`gcpserviceaccount` and Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#gcenode) | 443  
For more information about modifying Azure security groups, see [Azure network security groups](https://docs.microsoft.com/azure/virtual-network/network-security-groups-overview) and [Azure application security groups](https://docs.microsoft.com/azure/virtual-network/application-security-groups). 

## Installation instructions

To enable Config Sync to sync Kubernetes configuration files from a source of truth, follow the installation instructions in the [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync) documentation.

To enable Policy Controller to audit and enforce admission control policies, follow the installation instructions in the [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller) documentation.

## What's next?

  * Learn about adding [Configs](https://docs.cloud.google.com/anthos-config-management/docs/concepts/configs) to a source of truth.

  * Check the [examples GitHub repository](https://github.com/GoogleCloudPlatform/anthos-config-management-samples).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
