---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-import-ova/
title: Optional: Manually import OVAs to vSphere \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:43.419956+00:00
---

# Optional: Manually import OVAs to vSphere  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-import-ova/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Optional: Manually import OVAs to vSphere Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to manually import the OVAs needed for your cluster nodes to vSphere.

Typically there is no need to manually import OVAs, because `gkectl` imports the OVAs automatically.

The typical procedure is as follows:

  * Create an admin workstation.

  * On your admin workstation, create a cluster configuration file.

  * On your admin workstation, run `gkectl prepare`. This command fetches the OVAs from a Cloud Storage bucket, imports the OVAs to vSphere, and marks the OVAs as templates.

  * On your admin workstation, run `gkectl create` to create a cluster.




## Why manually import?

If your security policies do not allow your admin workstation to have access to your ESXI hosts, then `gkectl` cannot automatically import OVAs to vSphere.

Also, if you want to use Windows Server for some of your user clusster nodes, you must manually import an OVA. For more information, see Windows Server.

## Determine which OVAs you need

Before you create an admin cluster, you fill in an admin cluster configuration file. In the configuration file, you set the [`osImageType`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#osimagetype) field to specify the type of OS image you want to use for your admin cluster nodes. The options are:

  * Ubuntu with containerd
  * Ubuntu
  * Container Optimized OS (COS)



Before you create a user cluster, you fill in a user cluster configuration file. In the configuration file, you specify one or more [node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepools-section). For each node pool, you specify the [type of OS image](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field) you want to use for the nodes in the pool.

The options are:

  * Ubuntu with containerd
  * Ubuntu
  * Container Optimized OS (COS)
  * Windows Server



For each OS that you plan to use in an admin cluster or user cluster, you need to download the OS image from Cloud Storage and import it to vSphere.

## Ubuntu or Ubuntu with containerd

Download the Ubuntu OVA from Cloud Storage:
    
    
    gcloud storage cp gs://gke-on-prem-release/node-os-ubuntu/gke-on-prem-ubuntu-VERSION.ova ./
    

Replace `VERSION` with the complete version number, for example, `1.36.200-gke.118`. To get the version number, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

Import the OVA to vSphere and mark it as a template:
    
    
    govc import.ova -options - gke-on-prem-release/node-os-ubuntu/gke-on-prem-ubuntu-VERSION.ova <<EOF
    {
      "DiskProvisioning": "thin",
      "MarkAsTemplate": true
    }
    EOF
    

## Container Optimized OS

Download the COS OVA from Cloud Storage:
    
    
    gcloud storage cp gs://gke-on-prem-release/node-os-cos/gke-on-prem-cos-VERSION.ova ./
    

Replace `VERSION` with the complete version number, for example, `1.36.200-gke.118`. To get the version number, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

Import the OVA to vSphere and mark it as a template:
    
    
    govc import.ova -options - gke-on-prem-release/node-os-cos/gke-on-prem-cos-VERSION.ova <<EOF
    {
      "DiskProvisioning": "thin",
      "MarkAsTemplate": true
    }
    EOF
    

## Windows Server

Follow these steps: [Create a VMware vSphere template for Windows Server 2019](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/manage/hybrid/server/best-practices/vmware-windows-template).

For more information, see [Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
