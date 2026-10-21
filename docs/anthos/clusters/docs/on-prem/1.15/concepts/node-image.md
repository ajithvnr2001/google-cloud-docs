---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/node-image/
title: Node image \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:57.238127+00:00
---

# Node image  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/node-image/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Node image Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/concepts/node-image)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/concepts/node-image)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes the node operating system (node OS) image that runs on Google Distributed Cloud cluster nodes.

Google Distributed Cloud cluster nodes run ubuntu_containerd by default. The image is similar to [Google Kubernetes Engine's Ubuntu node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

Google Distributed Cloud node pools also support [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits). Container-Optimized OS on Google Distributed Cloud supports [kdump](https://en.wikipedia.org/wiki/Kdump_\(Linux\)) for debugging kernel issues.

Google Distributed Cloud offers the following node image options per OS for your cluster:

OS | Node images | Status  
---|---|---  
Container-Optimized OS | 

  * cos

| General Availability  
Ubuntu | 

  * ubuntu_containerd

| General Availability  
  
## Kubernetes version

New Google Distributed Cloud versions sometimes introduce a new Kubernetes version for clusters. Version changes are announced in [Release notes](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/release-notes). To learn which Kubernetes version your cluster runs, see [Versions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history).

## Preinstalled tools

  * Google Distributed Cloud's node OS has the following tools preinstalled: `arping` `cloud-utils`, `conntrack`, `logrotate`, `prips`, `systemd-container`
  * Google Distributed Cloud's node OS has the `debug-toolbox` container image preinstalled. `debug-toolbox` includes several packages for debugging node issues. You run an accompanying shell script, `toolbox`, to unpack and run the `debug-toolbox` container. [Learn about the `toolbox` script](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/toolbox).



## Networking

As of Google Distributed Cloud version 1.1.0-gke.6, the node OS' default networking configuration is disabled to support static IP allocation.

## Security

See [node security](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/security#node_security).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
