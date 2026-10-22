---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/node-image/
title: Node image \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:46.237446+00:00
---

# Node image  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/node-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Node image Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the node operating system (node OS) image that runs on Google Distributed Cloud (software only) for VMware cluster nodes.

For version 1.35 and later, cluster nodes run `ubuntu_cgv2` by default. For version 1.34 and earlier, cluster nodes run `ubuntu_containerd` by default. The image is similar to [Google Kubernetes Engine's Ubuntu node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

Google Distributed Cloud node pools also support [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) (`cos_cgv2` or `cos`). Container-Optimized OS on Google Distributed Cloud supports [kdump](https://en.wikipedia.org/wiki/Kdump_\(Linux\)) for debugging kernel issues.

As of version 1.35, Kubernetes no longer supports cgroup v1, and Google Distributed Cloud no longer supports the `ubuntu_containerd` and `cos` OS image types. To learn how to migrate your cluster nodes to cgroup v2 images (`ubuntu_cgv2` and `cos_cgv2`), see [Migrate to cgroup v2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-to-cgroupv2).

Google Distributed Cloud offers the following node image options for your cluster:

### 1.35+

OS | Node images | Status  
---|---|---  
Container-Optimized OS with [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * cos_cgv2

| General Availability  
Ubuntu with containerd and [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * ubuntu_cgv2

| General Availability  
  
### 1.29

OS | Node images | Status  
---|---|---  
Container-Optimized OS | 

  * cos

| General Availability  
Container-Optimized OS with [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * cos_cgv2

| General Availability  
Ubuntu with containerd | 

  * ubuntu_containerd

| General Availability  
Ubuntu with containerd and [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * ubuntu_cgv2

| General Availability  
  
### 1.28

OS | Node images | Status  
---|---|---  
Container-Optimized OS | 

  * cos

| General Availability  
Container-Optimized OS with [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * cos_cgv2

| Preview  
Ubuntu with containerd | 

  * ubuntu_containerd

| General Availability  
Ubuntu with containerd and [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) | 

  * ubuntu_cgv2

| Preview  
  
### 1.16

OS | Node images | Status  
---|---|---  
Container-Optimized OS | 

  * cos

| General Availability  
Ubuntu with containerd | 

  * ubuntu_containerd

| General Availability  
  
## Kubernetes version

New Google Distributed Cloud versions sometimes introduce a new Kubernetes version for clusters. Version changes are announced in [Release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/release-notes). To learn which Kubernetes version your cluster runs, see [Versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history).

## Preinstalled tools

  * The node OS has the following tools preinstalled: `arping` `cloud-utils`, `conntrack`, `logrotate`, `prips`, and `systemd-container`.
  * The node OS has the `debug-toolbox` container image preinstalled. `debug-toolbox` includes several packages for debugging node issues. You run an accompanying shell script, `toolbox`, to unpack and run the `debug-toolbox` container. [Learn about the `toolbox` script](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/toolbox).



## Networking

As of version 1.1.0-gke.6, the node OS default networking configuration is disabled to support static IP allocation.

## Security

See [node security](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/security#node_security).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
