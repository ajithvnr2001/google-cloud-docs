---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage/
title: GDC Ready storage partners \u00a0|\u00a0 Google Distributed Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:27.899924+00:00
---

# GDC Ready storage partners  |  Google Distributed Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)



Send feedback 

#  GDC Ready storage partners Stay organized with collections  Save and categorize content based on your preferences. 

This page is for Storage specialists who connect or help connect storage with other services, such as Google Cloud. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## GDC Ready storage qualification

Google Cloud established the following requirements to be met for a storage partner's system to achieve Google Distributed Cloud (GDC) ready qualification. [Container Storage Interface (CSI)](https://github.com/container-storage-interface/spec) is a vendor independent standard for vendors to expose their block and file storage systems to Container Orchestration Systems (COs) like Kubernetes. GDC Ready storage qualification ensures that our storage partners' CSI drivers can provide a seamless experience between GDC (on VMware or bare metal) and the partners' file storage systems.

For a partner's CSI driver to be considered for the program, the partner must support the following:

  * Ability to deploy the storage CSI driver and its dependencies, using the Kubernetes framework
  * Core functions that customers require today, including dynamic provisioning of volumes, by using the Kubernetes built-in storage APIs
  * Ability to manage storage for Kubernetes scale up and scale down scenarios
  * Workload portability with persistence storage for the stateful workloads



For Google Distributed Cloud software only on VMware qualifications, storage partners are given the option of which version of vSphere to perform their qualification with. If you do not see a specific version of vSphere included in the qualification matrix for a given partner, check with the partner to confirm their support.

For Google Distributed Cloud software only on bare metal qualifications, storage partners performed the qualifications on one or more operating systems based on their support of the OS. If you do not see a specific OS or version, check with the partner to confirm support.

You can find out more about the program in [GDC ready partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/anthos-ready-partners).

## GDC version validation

We no longer validate each release of Google Distributed Cloud software only with each storage partner because we haven't experienced any major conflicts with the listed vendors. For concerns about storage partners and validating Google Distributed Cloud software only, reach out to your technical account manager or support team member. To learn more about the version support policy, see the [Google Distributed Cloud software only support page](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/getting-support#version_support_policy).

The following vendors have previously validated different versions of support for their storage offerings:

  * Dell EMC
  * Hitachi
  * NetApp
  * Portworx
  * Robin.io
  * VMware



## Dell EMC

### Solution: CSI Driver for PowerStore

Description: Container Storage Interface (CSI) specification was designed to provide an interface that Container Orchestrators (like Kubernetes) can use to provision storage. Storage vendors implement CSI Drivers that conform to the specification which provide storage services by using this vendor neutral container storage interface.

Web page: [https://github.com/dell/csi-powerstore/](https://github.com/dell/csi-powerstore)

### Solution: CSI Driver for PowerFlex

Description: The PowerFlex CSI Driver by Dell implements the standardized interface (CSI spec) between enabled Container Orchestrator (CO) and Dell PowerFlex Systems. The driver is a plug-in that is installed into Kubernetes to provide persistent storage using Dell storage systems. The CSI driver for PowerFlex offers several enterprise grade features including, but not limited to the following: static provisioning, dynamic provisioning, creation & deletion of volume snapshots, and expansion.

Web page:

  * <https://github.com/dell/csi-powerflex>
  * <https://dell.github.io/csm-docs/docs/deployment/helm/drivers/installation/powerflex/>



Additional capabilities previously validated:

  * [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)
  * [Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
  * [Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)



## Hitachi

### Solution: Hitachi Storage Plug-in for Containers

| **Qualification matrix**  
---|---  
|  | GDC version | Driver version | **Bare metal support** | Additional capabilities tested  
---|---|---|---  
os versions  
1.33.x | 3.18.3 | RHEL 9.4 | [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)   
[Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)   
[Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)  
  
Description: The Hitachi Vantara Container Storage Interface (CSI) is a plugin and set of components that integrate Kubernetes distributions with Hitachi storage platforms (VSP) E series, F series, G series, VSP 5000 series, VSP One Block 20 series, and VSP One Block High End (VSP One Block 85) enterprise-class hybrid and all-flash storage systems.

HSPC is a software component that contains libraries, settings, and commands that you can use to create a container in order to run your stateful applications. The component enables the stateful applications to persist and maintain data after the life cycle of the container has ended. HSPC provides persistent volumes from Hitachi VSP series storage, utilizes built-in high-availability and orchestrates storage tasks between hosts in a cluster.

Web pages:

  * [Hitachi Vantara Documentation](https://docs.hitachivantara.com/search/documents?value-filters=Option%7E%2522Containers%2522*Product_custom%7E%2522Adapters%2522&content-lang=en-US)
  * [Hitachi Vantara GitHub](https://github.com/hitachi-vantara/csi-operator-hitachi)

**Note:** You must [register](https://support.hitachivantara.com/en/anonymous-dashboard.html) to access Hitachi Vantara's support site.

## NetApp

### Solution: CSI Trident for Kubernetes

| **Qualification matrix**  
---|---  
|  | GDC version | Driver version | **vSphere support** | Additional capabilities tested  
---|---|---|---  
vSphere version  
1.32.x | 25.10.0 | 8.0.3 | [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)   
[Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)   
[Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)   
[ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)   
[Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/)  
  
Description: The Container Storage Interface (CSI) provides a framework to standardize communications between container orchestrators and storage systems. CSI is a community effort driven by the Cloud Native Computing Foundation (CNCF) Storage Special Interest Group (SIG). NetApp implemented CSI in Trident to simplify the consumption of persistent storage for Kubernetes users while offering a universal interface to all major NetApp storage platforms. CSI is supported by Trident versions 19.07 or above and it can be downloaded from [docs.netapp](https://docs.netapp.com/us-en/trident/index.html).

Web page:

  * [netapp.com](https://www.netapp.com/developer/)
  * [github.com/NetApp/trident](https://github.com/NetApp/trident)

**Note:** You must upgrade to [1.28.200-gke.111](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history) or higher with NetApp for GDCV v1.28. RHEL 8.10 is tested with GDC 1.30.x on bare metal, but it isn't supported due to observed issues with `multipathd`.

## Portworx

### Solution: Portworx with CSI

Description: The [Portworx](https://portworx.com/) Enterprise Storage Platform for Kubernetes is built to address the business requirements needed to run data-rich applications on Kubernetes in production. The Portworx Enterprise platform provides solutions for scalable, performant container storage, [Kubernetes backup](https://portworx.com/kubernetes-backup/) and [disaster recovery](https://portworx.com/kubernetes-disaster-recovery/), multi-cloud operations, data security, capacity management, and compliance and governance.

Web page:

  * <https://docs.portworx.com/operations/operate-kubernetes/storage-operations/csi/>
  * [ReadWriteMany access mode and Dataplane v2 (DPv2)](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2)



If you use Google Distributed Cloud software only on VMware with [Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-cluster-configuration-file#enabledataplanev2-field) and [sharedv4 service volumes](https://docs.portworx.com/portworx-enterprise/concepts/shared-volumes), we recommend that you use version 1.28.200-gke.111 or higher.

For Google Distributed Cloud software only on bare metal, create a cluster that includes kube-proxy (included by default) with the [Px-StoreV2](https://docs.portworx.com/portworx-enterprise/concepts/px-store-v2) driver.

For Google Distributed Cloud software only on VMware and bare metal, Google Distributed Cloud version 1.32.x is qualified for [PX-StoreV2](https://docs.portworx.com/portworx-enterprise/concepts/px-store-v2).

**Note:** We have found some issues with GDC 1.31.x running on RHEL 8.10 with driver 3.0.5 and we do not recommend this combination.

Additional capabilities previously validated:

  * [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)
  * [Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
  * [ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)



## Robin.io

### Solution: ROBIN Storage

Description: The ROBIN cloud built-in storage is an application-aware container storage that offers advanced data management capabilities and runs on any Kubernetes distribution including GKE on Google Cloud and GDC. ROBIN cloud built-in storage delivers bare-metal performance and enables you to protect (by using snapshots, backups), secure (by using encryption), collaborate (by using clones and git like push/pull workflows), and make portable (by using cloud-sync) any stateful application that is deployed using helm charts or operators.

Web page:

  * <https://docs.robin.io/>
  * [ReadWriteMany access mode and Dataplane v2 (DPv2)](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2)



If you use Google Distributed Cloud software only on VMware with [Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-cluster-configuration-file#enabledataplanev2-field) and RWX volumes, we recommend that you use the following clusters versions:

  * For minor version 1.28, use version 1.28.200-gke.111 or higher.
  * For Google Distributed Cloud software only on bare metal, we recommend that you don't create a cluster [without kube-proxy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/no-kube-proxy) with this driver.



Additional capabilities previously validated:

  * [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)
  * [Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
  * [Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)
  * [ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)



## VMware

### Solution: vSphere CSI Driver*

| **Qualification matrix**  
---|---  
|  | GDC version | Driver version | **vSphere support** | Additional capabilities tested  
---|---|---|---  
vSphere version*  
1.33.x | 3.5.0 | 7.0.3  
8.0.3 | [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)   
[Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)   
[Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)  
1.34.x | 3.5.0 | 7.0.3  
8.0.3 | [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)   
[Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)   
[Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)  
1.35.x | 3.6.0 | 7.0.3  
8.0.3 | [Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)   
[Raw Block](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)   
[Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)  
  
*VMware vSphere CSI pre-installed with GDC is generally available as of GDC version 1.7.x. For VM configuration requirements, see the VMware [prerequisites](https://vsphere-csi-driver.sigs.k8s.io/driver-deployment/prerequisites.html#vm_configuration) documentation.

Description: The VMware vSphere Container Storage Interface (CSI) is an out-of-tree plug-in that exposes vSphere storage to containerized workloads on Kubernetes. The plug-in enables VMware vSAN and other types of vSphere storage. It communicates with the Cloud Native Storage (CNS) control plane on VMware vCenter Server for all storage provisioning operations.

Web page:

  * <https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver>



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
