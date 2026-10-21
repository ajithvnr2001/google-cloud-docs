---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-vsphere-csi-driver/
title: Using the vSphere Container Storage Interface driver \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:00.068173+00:00
---

# Using the vSphere Container Storage Interface driver  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-vsphere-csi-driver/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Using the vSphere Container Storage Interface driver Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/using-vsphere-csi-driver)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/using-vsphere-csi-driver)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document explains how to use the vSphere Container Storage Interface (CSI) driver with Google Distributed Cloud.

## Overview

The [vSphere CSI driver](https://vsphere-csi-driver.sigs.k8s.io/) is deployed automatically in Google Distributed Cloud. For information about using other CSI drivers, see [Installing a CSI driver](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-csi-driver).

## vSphere requirements

To use the vSphere CSI driver, you must have:

  * A Linux-based [supported version of vCenter Server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements)

  * A [supported version of ESXI](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-requirements)




### Volume expansion

  * Offline [volume expansion](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/storage#volume_expansion) requires both vCenter Server and ESXi to be version 7.0 Update 1 or later

  * Online volume expansion requires both vCenter Server and ESXi to be version 7.0 Update 2 or later.




### Volume snapshot

Volume snapshot requires both vCenter Server and ESXi to be version 7.0 Update 3 or later.

### Cns.Searchable

Your vCenter user account must have the [Cns.Searchable](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-C04F1605-D158-4B65-810F-6F5B109BCDEC.html) privilege on the root vCenter object.

If you are unsure whether your account meets the CSI prerequisites, run `gkectl diagnose cluster` before deploying any CSI workloads.

## Verify that the driver is installed

When the vSphere CSI driver is installed in your user cluster, a StorageClass called `standard-rwo` is created.

List the StorageClass objects:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get storageclass
    

Replace CLUSTER_KUBECONFIG with the path of your cluster kubeconfig file.

Verify that `standard-rwo` appears in the output. For example:
    
    
    standard                 kubernetes.io/vsphere-volume  Delete   Immediate     false      33m
    standard-rwo (default)   csi.vsphere.vmware.com    Delete   Immediate     true       32m
    

Verify that the vSphere CSI driver is installed:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get csinode \
        -o="custom-columns=NAME:metadata.name,DRIVERS:spec.drivers[].name"
    

The output should indicate that the driver is available on all of your cluster nodes. For example:
    
    
    NAME     DRIVERS
    node-0   csi.vsphere.vmware.com
    node-1   csi.vsphere.vmware.com
    node-2   csi.vsphere.vmware.com
    

## Provisioning volumes

To provision volumes with the vSphere CSI driver, set the `storageClassName` field of your [PersistentVolumeClaim](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/) to `standard-rwo`.

## Setting the default storage class

To set `standard-rwo` as the default storage class, see [Default storage class](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/default-storage-class).

## Using a snapshot to restore a volume

See [Restore a volume from a snapshot](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-csi-restore-volume-snapshot).

## Creating additional StorageClasses

You can create additional vSphere CSI StorageClasses in your cluster using the `datastoreurl` or `storagepolicyname` parameters.

The following example uses the `storagepolicyname` parameter:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: gold
    parameters:
      csi.storage.k8s.io/fstype: ext4
      storagepolicyname: "Gold Policy"
    provisioner: csi.vsphere.vmware.com
    

To find the correct value for the `datastoreurl` parameter, run the following command:
    
    
    govc datastore.info DATASTORE_NAME
    

Replace DATASTORE_NAME with the name of your [vSphere datastore](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#vcenter-datastore-field).

Use the value for URL from the output for `datastoreurl`. An example output looks like the following:
    
    
    Name:        DATASTORE_NAME
      Path:      /DATACENTER_NAME/datastore/DATASTORE_NAME
      Type:      VMFS
      URL:       ds:///vmfs/volumes/5d864fa0-7f2184d4-8eb4-3cfdfe0ce9a0/
      Capacity:  20479.8 GB
      Free:      10066.9 GB
    

## Volume cleanup

Volumes provisioned by the vSphere CSI driver are not deleted when you delete a user cluster. You should delete all PVCs and [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) before deleting the cluster. To delete your volumes, run the following command:
    
    
    kubectl delete statefulsets,persistentvolumeclaims --namespace=MY_NAMESPACE --all
    

Replace MY_NAMESPACE with your Kubernetes [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

If you deleted a user cluster without deleting its volumes, you can find the volumes in vSphere user interface:

  1. Select a datastore.

  2. Navigate to **Monitor** > **Cloud Native Storage** > **Container Volumes**.

  3. In the **Details** section of each volume, you can see the Kubernetes cluster name.




## Disabling vSphere CSI driver

To remove vSphere CSI support, add the following to your user cluster configuration:
    
    
    # (Optional) Storage specification for the cluster storage:
    # To disable the vSphere CSI driver, set this to true. The value is set to false by default and 
    # the vSphere CSI driver is enabled by default on vSphere version >= 6.7U3.
      vSphereCSIDisabled: true
    

## What's next

  * [Read more about Google Distributed Cloud storage concepts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/storage)
  * [Set a default StorageClass for your cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/default-storage-class)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
