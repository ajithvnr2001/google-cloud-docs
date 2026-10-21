---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk/
title: Installing Google Cloud CLI \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:40.532989+00:00
---

# Installing Google Cloud CLI  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



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




## Installing if you are behind a proxy

If you are behind a corporate proxy or firewall, the gcloud CLI might not be able to access the internet with its default settings.

For information about how to install the gcloud CLI in this situation, see

[Configuring the gcloud CLI for use behind a proxy/firewall](https://docs.cloud.google.com/sdk/docs/proxy-settings).

## What's next

[Create Google Cloud projects (full instructions)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
