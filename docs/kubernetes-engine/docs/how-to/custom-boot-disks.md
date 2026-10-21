---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks/
title: Configuring a custom boot disk \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:03.743959+00:00
---

# Configuring a custom boot disk  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configuring a custom boot disk Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to customize a node boot disk in your Google Kubernetes Engine (GKE) [clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) and [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).

## Overview

When you create a GKE cluster or node pool, you can choose the type of Persistent Disk onto which the Kubernetes node file system is installed for each node. By default, GKE uses balanced Persistent Disks in version 1.24 or later. You can also specify other Persistent Disk types, such as standard or SSD. For more information, see [Storage options](https://docs.cloud.google.com/compute/docs/disks).

**Note:** This feature differs from [Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd), which can't be used as a boot disk.

Balanced and SSD Persistent Disks have disk quotas which are different from standard Persistent Disk quotas. If you are switching from standard to balanced Persistent Disks, you may need to request for quota increases. For more information, see [Resource quotas](https://docs.cloud.google.com/compute/quotas#disk_quota).

## Benefits of using an SSD boot disk

Using an SSD Persistent Disk as a boot disk for your nodes offers some performance benefits:

  * [Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) have faster boot times.
  * Binaries and files served from containers are available to the node faster. This can increase performance for I/O-intensive [workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview), such as [web-serving applications](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app) that host static files or short-running, I/O-intensive [batch jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/).
  * Files stored on the node's local media (exposed through `hostPath` or `emptyDir` volumes) can see improved I/O performance.



## Specifying a node boot disk type

You can specify the boot disk type when you create a cluster or node pool.

### gcloud

To create a cluster with a custom boot disk, run the following command.

`[DISK-TYPE]` can be one of the following values:

  * `pd-balanced` (the default in version 1.24 or later)
  * `pd-standard` (the default in version 1.23 or earlier)
  * `pd-ssd`
  * `hyperdisk-balanced`

**Note:** The available disk types depend on the machine series of your nodes. For example, the N4 machine series only supports `hyperdisk-balanced` as a boot disk. For up-to-date information on machine type and disk compatibility, see the [machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) documentation.

For more information, see [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types).
    
    
    gcloud container clusters create [CLUSTER_NAME] --disk-type [DISK_TYPE]

To create a node pool in an existing cluster:
    
    
    gcloud container node-pools create [POOL_NAME] --disk-type [DISK_TYPE]

For example, the following command creates a cluster, `example-cluster`, with the SSD Persistent Disk type, `pd-ssd`:
    
    
    gcloud container clusters create example-cluster --disk-type pd-ssd

### Console

To select the boot disk when creating your cluster with the Google Cloud console:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster as needed.

  3. From the navigation menu, expand **default-pool** and click **Nodes**.

  4. In the **Boot disk type** drop-down list, select a Persistent Disk type.

  5. Click **Create**.




To create a node pool with a custom boot disk for an existing cluster:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure your node pool as needed.

  6. From the navigation menu, click **Nodes**.

  7. In the **Boot disk type** drop-down list, select a Persistent Disk type.

  8. Click **Create**.




## Protecting node boot disks

A node boot disk stores your container image, some system process logs, Pod logs, and the writable container layer by default.

If your workloads use `configMap`, `emptyDir`, or `hostPath` volumes, your Pods could write additional data to node boot disks. You can configure `emptyDir` to be backed by tmpfs to stop this. To learn how, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir). Since `secret`, `downwardAPI`, and `projected` volumes are backed by [tmpfs](https://www.kernel.org/doc/html/latest/filesystems/tmpfs.html) the Pods using them don't write data to the node boot disk.

By default, Google Cloud [encrypts customer content at rest](https://docs.cloud.google.com/security/encryption/default-encryption#encryption_of_data_at_rest) including your node boot disks, and GKE manages encryption for you without any action on your part.

However, when using volumes that write to the node boot disk, you may want to further control how your workload data is protected in GKE. You can do this by either preventing Pods from writing to node boot disks , or using Customer Managed Encryption Keys (CMEK) for node boot disks.

### Prevent Pods from writing to boot disks

To prevent Pods from writing data directly to the node boot disk, use one of the following methods.

#### Policy Controller

Policy Controller is a feature of GKE Enterprise that lets you declare and enforce custom policies at scale across your GKE clusters in fleets.

  1. [Install Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller).
  2. Define a constraint that restricts the following volume types by using the [`k8sPspVolumeTypes` constraint template](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspvolumetypes): 
     * `configMap`
     * `emptyDir` (if not backed by tmpfs)
     * `hostPath` For instructions, see [Use the constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints) in the Policy Controller documentation.



The following example constraint restricts these volume types in all Pods in the cluster:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPVolumeTypes
    metadata:
      name: deny-boot-disk-writes
    spec:
      match:
        kinds:
        - apiGroups: [""]
          kinds: ["Pod"]
      parameters:
        volumes:
        - configMap
        - emptyDir
        - hostPath
    

#### PodSecurity admission controller

The built-in Kubernetes PodSecurity admission controller lets you enforce different levels of the Pod Security Standards in specific namespaces or in the cluster. The Restricted policy prevents Pods from writing to the node boot disk.

To use the PodSecurity admission controller, see [Apply predefined Pod-level security policies using PodSecurity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission).

### Customer-managed encryption

If you want to control and manage encryption key rotation yourself, you can use Customer Managed Encryption Keys (CMEK). These keys are used to encrypt the data encryption keys that encrypt your data. To learn how to use CMEK for node boot disks, see [Using customer-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#boot-disks).

A limitation of CMEK for node boot disks is that it cannot be changed after node pool creation. This means:

  * If the node pool was created with customer-managed encryption, you cannot subsequently disable encryption on the boot disks.
  * If the node pool was created without customer-managed encryption, you cannot subsequently enable encryption on the boot disks. However, you can create a new node pool with customer-managed encryption enabled and delete the previous node pool.



## Limitations

Before configuring a custom boot disk, consider the following limitations:

  * The [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series), [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms), and [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) machine series don't support the `pd-standard` node boot disk type.



## What's next

  * [Learn how to specify a minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform).
  * [Learn more about customer managed encryption](https://docs.cloud.google.com/security/encryption/default-encryption#key_management).
  * [Learn about using Customer Managed Encryption keys in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
