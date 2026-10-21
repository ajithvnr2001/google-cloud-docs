---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/use-cases/
title: Use cases for Google Cloud NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:27.778910+00:00
---

# Use cases for Google Cloud NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Use cases for Google Cloud NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

NetApp Volumes expedites the deployment of various cloud-based applications through the rapid provisioning of shared file services or block storage and offers a rich set of storage management features. Primary use cases include file services, DevOps, databases, and clustered applications.

## File services

NetApp Volumes is a fault-tolerant, scalable storage platform for creating a cloud-based file system that you can access with standard NFS or SMB protocols. With its high performance capabilities, NetApp Volumes delivers enterprise-level network-attached storage solutions on Google Cloud that are similar to an on-premises experience, which include the following complete range of supporting features:

  * Read-only and read-write client access control

  * Connections over both NFSv3 and NFSv4.1 protocols

  * Active Directory (AD) integration and SMB connections




You can use file services as you migrate workloads or create new applications in Google Cloud. For example, you can use an SMB share to support individual user or group file sharing across Windows clients. You can also use SMB share to support file and profile sharing for virtual desktops. Alternatively, you can use NFS or SMB volumes to share files between your applications, or as a backup destination.

NetApp Volumes helps you migrate existing workloads to Google Cloud and provides you with a platform to develop and maintain a file storage solution in the cloud, which reduces hardware, procurement time, cooling, power use, and minimizes physical space.

## Block storage

NetApp Volumes block storage provides high-performance and reliable block storage in Google Cloud, ideal for organizations that need to deploy and manage self-managed databases such as Oracle, Microsoft SQL Server, MySQL, PostgreSQL, and other enterprise applications. This solution is ideal for workloads that require direct disk access, granular control over storage provisioning, and consistent low-latency performance. Common use cases include supporting mission-critical database environments and hosting enterprise software that benefits from robust data protection, rapid snapshotting, and seamless scalability. With NetApp Volumes block storage, the users can migrate, modernize, and operate these applications in Google Cloud without compromising on performance or reliability.

## Enterprise applications

You can rehost your applications which are deployed on-premises to NetApp Volumes. NetApp Volumes continues to preserve their core capabilities for file storage workflows. This includes a subset of enterprise applications that typically don't require refactoring.

By using NetApp Volumes, you can create fully managed NFS shares for Linux-based applications and SMB shares for Windows-based applications in seconds, or iSCSI volumes that can be partitioned and formatted as needed by the application. You can scale them up or down for capacity and performance without any impact on your workflows or users.

You can preserve application service delivery life cycles with quick snapshots and copies for development, testing, and staging environments, which further accelerates production releases and minimizes lead times.

## Google Cloud VMware Engine storage

Google Cloud supports VMware vSphere workloads with Google Cloud VMware Engine. Private clouds built with Google Cloud VMware Engine often need additional storage. This additional storage is used for either direct attachment to a single VM, or as datastores for multiple VMs with large storage requirements.

NetApp Volumes can be attached to a VM's guest operating system using either SMB or NFS protocols. These volumes can be used for file sharing across different applications running in either Compute Engine or Google Cloud VMware Engine. They can also be used for user and group file sharing in virtual desktop environments.

When you need large amounts of storage, you can use NetApp Volumes as datastores with Google Cloud VMware Engine hosts. NetApp Volumes as datastores can be more cost-effective than adding Google Cloud VMware Engine nodes, reducing the overall solution cost.

NetApp Volumes NFSv3 volumes let you support more storage in a cost-efficient manner and include NetApp Volumes rich set of data management features to protect your data such as snapshot copies, volume replication, and backup.

For more information, see [Using NFS volume as vSphere datastore hosted by Google Cloud NetApp Volumes](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-datastores-gcve).

## Persistent storage for stateful Google Kubernetes Engine applications

NetApp Volumes provides fast, reliable, and persistent storage for your stateful applications that run on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) or other self-managed Kubernetes distributions running in Google Cloud.

Most containerized enterprise applications have state and configuration data that need to be backed by persistent storage. Persistent storage allows your application state and configuration data to remain accessible through rapid container creation and destruction during various application execution sequences such as upgrades, scaling, and rollbacks. [NetApp Trident](https://docs.netapp.com/us-en/trident/trident-get-started/intro.html#what-is-astra) is a Container Storage Interface (CSI) compliant orchestrator that integrates with Kubernetes to provide:

  * Dynamic provisioning

  * Consumption

  * Management of persistent volumes with stateful containerized applications using [NetApp Volumes](https://docs.netapp.com/us-en/trident/trident-use/gcnv.html)

  * Data protection with CSI [snapshots](https://docs.netapp.com/us-en/trident/trident-concepts/snapshots.html)




Although it isn't mandatory, Trident simplifies the deployment and use of stateful applications with Kubernetes.

GKE lets you build, deploy, manage, and run containerized applications. GKE accelerates the development and deployment of highly portable applications through a declarative, self-healing, autoscaling platform. For more information, see GKE documentation on how to [deploy a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).

Google Cloud NetApp Volumes provides persistent storage for Kubernetes stateful applications with the following characteristics:

  * **Persistent volumes** : provides persistent storage outside the Kubernetes cluster for your Kubernetes applications requiring shared access to storage with read-write-many (RWX) [access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes). You can mount persistent volumes as read-write by many nodes at once using the RWX access mode. You can also use the read-write-once (RWO), read-only-many (ROX), or the read-write-once-pod (RWOP) access modes with NetApp Volumes for applications that require those access modes.

  * **Provisioned persistent volumes** : uses dynamically and statically provisioned Kubernetes persistent volumes (PV).

  * **Persistent volumes expansion** : stateful applications use Kubernetes PVs. NetApp Volumes lets you expand an existing PV after creation.

  * **Label storage volumes** : labels storage volumes for better identification and management in multi-cluster environments.

  * **Protect volumes** : it is important to provide data protection and recovery in case of a disaster. NetApp Volumes supports customer initiated snapshots and backup schedules to protect the data in a persistent volume.

  * **Access to persistent storage through NFSv3 and NFSv4.1** : supports the volume creation and access to persistent storage for Kubernetes applications with NFSv3 and NFSv4.1 using the [Trident CSI driver](https://docs.netapp.com/us-en/trident/trident-use/gcnv.html). Trident supports [Trident Cloud Identity](https://docs.netapp.com/us-en/trident/trident-use/gcnv.html#cloud-identity-for-gke) for NetApp Volumes authentication with GKE clusters. NetApp Volumes also supports the creation of volume subdirectories and access using the [NFS Container Storage Interface (CSI) driver](https://github.com/kubernetes-csi/csi-driver-nfs).

  * **Access to persistent storage through SMB** : supports volume creation and access to persistent storage for Kubernetes applications with SMB using the [Trident CSI driver](https://docs.netapp.com/us-en/trident/trident-use/gcnv.html). Trident supports [Trident Cloud Identity](https://docs.netapp.com/us-en/trident/trident-use/gcnv.html#cloud-identity-for-gke) for NetApp Volumes authentication with GKE clusters. NetApp Volumes also supports the creation of volume subdirectories and access to persistent storage through SMB using the [SMB Container Storage Interface (CSI) driver](https://github.com/kubernetes-csi/csi-driver-smb).




## Databases

You can use NetApp Volumes to quickly access primary databases or snapshot copies of open source or enterprise databases.

NetApp Volumes supports different levels of performance for each file system. Database administrators can allocate individual storage pools for hot or cold data, which allows them to control the use of high-performance and high-capacity storage. You can use NetApp Volumes to ensure file systems are available and resilient against system failures, which simplifies the setup for reliable database services in the cloud.

## Electronic design automation

[Electronic design automation (EDA)](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/architectural-patterns-eda) workloads present specific data management challenges, such as large datasets, numerous files, intensive metadata operations, and strict performance requirements.

NetApp Volumes provides a robust solution customized for electronic design automation workloads. The large capacity volumes feature of NetApp Volumes accommodates the large datasets that electronic design automation processes generate. NetApp Volumes ensures smooth data operations and accessibility by efficiently managing numerous files. It also optimizes the intensive metadata operations crucial for the performance and management of electronic design automation workloads. NetApp Volumes delivers the performance that electronic design automation workload users need for regular product releases.

NetApp Volumes offers a service that simplifies data management for electronic design automation workloads. It addresses the challenges of electronic design automation workloads and helps users maintain high productivity and efficiency. NetApp Volumes also helps users meet performance requirements and product release schedules to remain competitive.

For more information about EDA reference architecture, see [Benefits of using Google Cloud NetApp Volumes for EDA](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Benefits-of-using-Google-Cloud-NetApp-Volumes-for-Electronic-Design-Automation/ba-p/457461).

For more information about EDA implementation guidance, see [Optimize Linux NFS client access for electronic design automation workloads](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/optimize-client-access-for-eda). For benchmark results, see [Electronic design automation workload benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks#electronic_design_automation_workload_benchmarks).

## What's next

  * See the [quickstart guide for how to create a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-storage-pool).

  * Read about NetApp Volumes [application resilience considerations](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
