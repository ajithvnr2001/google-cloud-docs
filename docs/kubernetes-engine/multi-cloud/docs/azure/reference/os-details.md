---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/os-details/
title: Operating system details \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:04.234128+00:00
---

# Operating system details  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/os-details/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Operating system details

GKE on Azure manages the Azure virtual machine instances and the operating system running on these instances. In Kubernetes versions 1.26 and higher, GKE on Azure uses Ubuntu 22.04 LTS base images for Linux nodes. In Kubernetes versions 1.25 and lower, GKE on Azure uses Ubuntu 20.04 LTS.

The base Azure VM is maintained by Canonical. Google tests these images as part of the GKE on Azure release process. When a cluster or node pool is upgraded, the underlying virtual machine instances are terminated and recreated with the latest OS version.

When an instance launches, GKE on Azure performs additional configuration including:

  * Optimizing network settings for Kubernetes
  * Installing packages from the Ubuntu archive (Ubuntu only)
  * Disabling unattended apt package upgrades and reboots (Ubuntu only)
  * Installing Google Kubernetes Engine and Kubernetes binaries

**Note:** GKE on Azure is not affected by the [dockershim deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd) as clusters use the containerd runtime.

## Ubuntu

### Kubernetes 1.35

Kubernetes version | Publisher | Offer | SKU | Version  
---|---|---|---|---  
1.35.3-gke.300 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202602250  
  
### Kubernetes 1.34

Kubernetes version | Publisher | Offer | SKU | Version  
---|---|---|---|---  
1.34.1-gke.4700 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202512181  
1.34.6-gke.200 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202602250  
  
### Kubernetes 1.33

Kubernetes version | Publisher | Offer | SKU | Version  
---|---|---|---|---  
1.33.4-gke.900 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202507300  
1.33.5-gke.1900 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202512181  
1.33.10-gke.200 | Canonical | 0001-com-ubuntu-server-jammy | 22_04-lts-gen2 | 22.04.202602250  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
