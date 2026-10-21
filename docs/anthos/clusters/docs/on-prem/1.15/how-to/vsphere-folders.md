---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-folders/
title: Specify vSphere folders in cluster configuration \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:14.753462+00:00
---

# Specify vSphere folders in cluster configuration  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-folders/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Specify vSphere folders in cluster configuration Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/vsphere-folders)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/vsphere-folders)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to specify vSphere objects in cluster configuration files when the vCenter configuration contains parent folders. It also documents the naming rules applied by preflight validations starting with 1.13.0.

Assuming the following example vCenter configuration indicating the path from vCenter root to the specific object

Hosts and Clusters | VMs and Templates | Storage | Network  
---|---|---|---  
      
    
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-cluster-folder
            my-cluster
              my-resourcepool
            

| 
    
    
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-vm-folder
            

| 
    
    
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-storage-folder
            my-datastore
            

| 
    
    
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-network-folder
            my-portgroup
              
  
To create an Anthos cluster in my-resource-pool and my-vm-folder using my-datastore and my-portgroup, specify the following admin cluster configuration:
    
    
        vCenter:
          address: "my-vcenter"
          datacenter: "my-datacenter-folder/my-datacenter"
          cluster: "my-cluster-folder/my-cluster"
          resourcePool: "my-resourcepool"
          datastore: "my-datastore"
          folder: "my-vm-folder"
        network:
          vCenter:
            networkName: "my-network-folder/my-portgroup"
    
      

If your resource pool is nested under another resource pool, specify the full path to your resource pool in your admin cluster configuration, as shown in the following example:
    
    
        vCenter:
          address: "my-vcenter"
          datacenter: "my-datacenter-folder/my-datacenter"
          cluster: "my-cluster-folder/my-cluster"
          resourcePool: "my-cluster-folder/my-cluster/Resources/my-resourcepool/my-nested-resourcepool"
          datastore: "my-datastore"
          folder: "my-vm-folder"
        network:
          vCenter:
            networkName: "my-network-folder/my-portgroup"
      

To create an Anthos admin cluster in the default ResourcePool using my-datastore and my-portgroup, specify the following cluster configuration:
    
    
        vCenter:
          address: "my-vcenter"
          datacenter: "my-datacenter-folder/my-datacenter"
          cluster: "my-cluster-folder/my-cluster"
          resourcePool: "my-cluster-folder/my-cluster/Resources"
          datastore: "my-datastore"
          folder: "my-vm-folder"
        network:
          vCenter:
            networkName: "my-network-folder/my-portgroup"
      

If your vm folder is nested under another vm folder, specify the full path to your vm folder in your admin cluster configuration, as shown in the following example:
    
    
        vCenter:
          address: "my-vcenter"
          datacenter: "my-datacenter-folder/my-datacenter"
          cluster: "my-cluster-folder/my-cluster"
          resourcePool: "my-resourcepool"
          datastore: "my-datastore"
          folder: "/my-datacenter-folder/my-datacenter/vm/my-vm-folder/my-nested-vm-folder"
        network:
          vCenter:
            networkName: "my-network-folder/my-portgroup"
      

Note that you must include the first "/" in your vm folder full path.

This also applies to user cluster and admin workstation configuration since vCenter section is common across these configuration files.

## Naming Rules

Do not specify the parent folder while specifying a datastore as the datastore name must be unique within a datacenter. If a folder is specified, the following error is returned:
    
    
      Datastore name 'storage-folder/my-datastore' should not contain parent folders
    

For all other vSphere object types the parent folder should be specified when vCenter configuration contains parent folders. If the required parent folders are not specified in the cluster configuration but present in the vCenter configuration, the following error is returned: 
    
    
     Parent folder is not specified for cluster, you must specify the full path 'clusters/my-cluster' in the cluster field  

Starting with Anthos Clusters on VMware 1.13.0, vSphere object names are validated according to the above rules for the following operations:

  * gkectl create 
  * gkectl check-config 



There is still a chance that a vSphere object resolution is ambiguous under following example situations 

  * A cluster is upgraded from a previous version which violates the naming rules and vCenter configuration contains a conflicting folder/object, and 
  * Objects with conflicting names were not present during cluster creation but added later 



For example, consider the given vCenter configuration
    
    
     
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-cluster-folder
            my-cluster
              my-resourcepool
      

Next, if the following hierarchy is added later
    
    
    my-vcenter
      my-datacenter-folder
        my-datacenter
          my-cluster
            my-resourcepool
      

the resolution of 'my-resourcepool' is ambiguous if the configuration files did not specify the my-cluster-folder during cluster creation

You may encounter the following error: ` path 'my-resourcepool' resolves to multiple resource pools `

More generally, the vSphere library returns the following error message when the object resolution is ambiguous: 
    
    
     path xxx resolves to multiple objects 

To fix the error, ensure that the path does not contain conflicting object names (such as one within a folder and one without). Remove or rename the object which does not belong to the cluster and causes the conflict. Since the vSphere fields are immutable once the cluster is created, a new cluster creation is required if the conflict cannot be resolved by modifying vCenter configuration. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
