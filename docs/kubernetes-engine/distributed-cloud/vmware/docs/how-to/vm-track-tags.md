---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vm-track-tags/
title: Enable VM tracking \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:06.983887+00:00
---

# Enable VM tracking  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vm-track-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Enable VM tracking Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to enable VM tracking with [vSphere tags](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) when you create a new user cluster.

Each node in your cluster is a VM. When VM tracking is enabled, Google Distributed Cloud attaches tags to your cluster worker nodes and control-plane nodes. You can use the tags to select VMs that belong to a particular user cluster or node pool.

Each control-plane node is given a tag that specifies the cluster name.

Each worker node is given two tags: one that specifies the cluster name and one that specifies both the cluster name and the nodepool name.

On [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field), VM tracking with vSphere tags is supported in Google Distributed Cloud version 1.33 and higher but isn't supported in version 1.31 and 1.32.

## Before you begin

You can enable VM tracking when you create a new user cluster. You cannot enable VM tracking by updating an existing cluster.

## Create vSphere categories

Create these [vSphere categories](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) on the vCenter server specified by [`vCenter.address`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-address-field) in your admin cluster configuration file.

  * machine.onprem.gke.io/cluster-name
  * machine.onprem.gke.io/cluster-name/nodepool-name



## Grant privileges

Grant these [vSphere privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security.html) to the [vCenter credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-credentials-fileref-path-field) specified in your user cluster configuration file:

  * vSphere Tagging.Assign or Unassign vSphere Tag
  * vSphere Tagging.Assign or Unassign vSphere Tag on Object (vSphere 7.0)
  * vSphere Tagging.Create vSphere Tag
  * vSphere Tagging.Delete vSphere Tag



## Enable VM tracking

  1. In your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest), set `enableVMTracking` to `true`.

  2. [Create your user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).




## View the VMs that have an attached tag

In the vSphere web client, you can view the VMs that have a particular tag attached. For example, to view all the VMs in your user cluster, go to `Tags & Custom Attributes`. Then select the tag that belongs to `machine.onprem.gke.io/cluster-name` and has the same name as your user cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
