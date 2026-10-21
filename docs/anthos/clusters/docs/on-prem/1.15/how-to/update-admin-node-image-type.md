---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-admin-node-image-type/
title: Update admin node image type \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:57.120444+00:00
---

# Update admin node image type  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-admin-node-image-type/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Update admin node image type Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/update-admin-node-image-type)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/update-admin-node-image-type)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes how to update the admin node image type. This affects the `osImageType` field in the admin cluster configuration file for Google Distributed Cloud.

You can update the admin node image type with the `gkectl update admin` command as described here.

## Update the admin node image type to COS

  1. In your admin cluster configuration file, set [`osImageType`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#os-image-type-field) to `cos`

  2. For each of your admin clusters, run gkectl update command: 
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace:

     * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.



## Update the admin node image type to Ubuntu

  1. In your admin cluster configuration file, set [`osImageType`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#os-image-type-field) to `ubuntu_containerd`

  2. For each of your admin clusters, run gkectl update command: 
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace:

     * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
