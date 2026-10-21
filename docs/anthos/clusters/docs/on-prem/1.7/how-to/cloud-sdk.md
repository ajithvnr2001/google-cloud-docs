---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/cloud-sdk/
title: Installing Google Cloud CLI \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:10:49.700245+00:00
---

# Installing Google Cloud CLI  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/cloud-sdk/

**Version 1.7**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.7 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/overview)



Send feedback 

#  Installing Google Cloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to install Google Cloud CLI before you install Google Distributed Cloud.

To install Google Distributed Cloud, you need certain tools that are in gcloud CLI. Use the following steps to install the tooling, including upgrading your existing gcloud CLI installation.

To install gcloud CLI and related tooling:

  1. Install gcloud CLI:

     * [Install gcloud CLI](https://docs.cloud.google.com/sdk/docs) but skip the `gcloud init` command.

     * If you already have a version installed, run the following command to list what components and versions you have:
           
           gcloud components list

If you have the `latest available version` and both the `anthos-auth` and `kubectl` components are `Installed`, you can stop here.

  2. Retrieve the latest components and versions:

     1. Run the following command to update gcloud CLI:
            
            gcloud components update

     2. To install the `anthos-auth` and `kubectl` components, run the following commands:
            
            gcloud components install kubectl
            gcloud components install anthos-auth




## What's next

[Create a Cloud project (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/cloud-project-quickstart).

[Create Google Cloud projects (full instructions)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/multiple-gcp-projects).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
