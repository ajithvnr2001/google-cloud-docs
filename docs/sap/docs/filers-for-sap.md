---
url: https://docs.cloud.google.com/sap/docs/filers-for-sap/
title: File sharing solutions for SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:30.709018+00:00
---

# File sharing solutions for SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/filers-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  File sharing solutions for SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud supports several file sharing solutions for SAP on Google Cloud. Which you choose depends on what you are using the file sharing solution for, whether your SAP systems extend across zones or regions, and the performance requirements of your workloads.

## Supported file sharing solutions for SAP on Google Cloud

The following table shows the file sharing solutions that Google Cloud supports for SAP systems.

If you are already using one of these file sharing solutions for other purposes and the solution meets all the requirements of your SAP workloads, then you can use that solution for your SAP systems also.

**Important:** NetApp Cloud Volumes Services (CVS) for Google Cloud has reached its end of support. If you're using NetApp CVS, then we strongly recommend that you transition to another file sharing solution such as [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) at the earliest. File sharing solution | Description  
---|---  
[Filestore](https://cloud.google.com/filestore) |  Google Cloud high-performance, fully managed file storage.  For multi-zonal high-availability deployments, we recommend that you use the [Regional service tier of Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers#regional) (Filestore Regional). For single-zone high-performance deployments, we recommend that you use the [Zonal service tier of Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers-zonal) (Filestore Zonal). For information about the Filestore service tiers, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers). For information about how to perform basic operations in Filestore by using the Google Cloud console, see [Create a Filestore instance by using the Google Cloud console](https://docs.cloud.google.com/filestore/docs/create-instance-console).   
[NetApp Cloud Volumes ONTAP](https://docs.netapp.com/us-en/storage-management-cloud-volumes-ontap/index.html) |  A full-featured, smart storage solution that you deploy and manage yourself on a Compute Engine instance.  For more information about NetApp Cloud Volumes ONTAP on Google Cloud, see [Supported configurations for Cloud Volumes ONTAP in Google Cloud](https://docs.netapp.com/us-en/storage-management-cloud-volumes-ontap/reference-configs-gcp.html).   
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) |  Google Cloud NetApp Volumes is a fully managed, cloud-based data storage service that provides advanced data management capabilities and highly scalable performance. NetApp Volumes offers four service levels: _Flex_ , _Standard_ , _Premium_ , and _Extreme_. For the SAP HANA data and log directories, you must use the Premium or Extreme service level. For SAP HANA shared files, you can use the Flex, Standard, or Premium service level.  For more information, see [About Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).  
  
## File sharing solutions by SAP use case

The following table lists the most common use cases for file sharing solutions in SAP landscapes and the solutions that support the use cases.

Use case | Purpose | Recommended solutions  
---|---|---  
**Interface directory** | For use as a general storage location by SAP and other software systems to pass files between servers. | 

  * Filestore Regional or Zonal
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes: the Flex, Standard, Premium, or Extreme service level

  
**SAP transport directory** |  For use as an SAP storage location by SAP systems to hold shared application files in distributed or high-availability deployments, or to transport SAP files and updates between different operational environments.  | 

  * Filestore Regional or Zonal
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes: the Flex, Standard, Premium, or Extreme service level

  
**Backup directory** |  For use by SAP or other systems as a centralized storage location for backups.  | 

  * Filestore Regional or Zonal
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes: the Standard, Premium, or Extreme service level
  * Cloud Storage, by using the Backint feature of Google Cloud's Agent for SAP

  
**SAP HANA scaleout system directory** |  For use within a single zone by SAP HANA scaleout systems to share binaries and configuration files between the SAP HANA nodes.  | 

  * Filestore Regional or Zonal
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes, Premium or Extreme service level

  
**SAP HANA shared files** |  For storing shared binaries and configuration files used by the SAP HANA nodes.  | 

  * Filestore Regional or Zonal
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes, Premium or Flex service level

  
**SAP HANA data and log persistence** |  For the persistence of the `/hana/data` and `/hana/log` directories.  | 

  * Google Cloud NetApp Volumes: the Premium or Extreme service level
  * [NetApp Cloud Volumes ONTAP HA pair](https://docs.netapp.com/us-en/storage-management-cloud-volumes-ontap/concept-ha-google-cloud.html)

  
  
## Features supported by each file sharing solution

The following table shows the common features that SAP systems require of file sharing solutions and the solutions that support those features.

Feature | Filestore Zonal | Filestore Regional | NetApp Cloud Volumes ONTAP | Google Cloud NetApp Volumes  
---|---|---|---|---  
**Disaster recovery** | Asynchronous instance replication or backup restore | Asynchronous instance replication or backup restore | Automated with [Snapmirror](https://docs.netapp.com/us-en/ontap/concepts/snapmirror-disaster-recovery-data-transfer-concept.html) | Cross-region or cross-zone volume replication  
**High availability** | Zonal service, 99.9% SLA | Multi-zonal service, 99.99% SLA | Multi-zone HA solution;  
99.99% SLA for only the Google Cloud infrastructure |  The Flex service level as a regional service with 99.99% [SLA](https://cloud.google.com/netapp/volumes/sla). The Premium or Extreme service level as a zonal service with 99.95% [SLA](https://cloud.google.com/netapp/volumes/sla). The Flex service level as a zonal service with 99.9% [SLA](https://cloud.google.com/netapp/volumes/sla).  
**Snapshots/Backup** | Yes | Yes | Yes | Yes  
**Managed service** | Yes | Yes | No | Yes  
**Protocols** | NFSv3, NFSv4.1 | NFSv3, NFSv4.1 | NFSv3, NFSv4.1, SMB, iSCSI | NFSv3, NFSv4.1, SMB, iSCSI  
**Regional replication** | Yes | Yes | With [Snapmirror](https://docs.netapp.com/us-en/ontap/concepts/snapmirror-disaster-recovery-data-transfer-concept.html) | Yes  
**Regional availability** | In [supported regions](https://docs.cloud.google.com/filestore/docs/regions) | In [supported regions](https://docs.cloud.google.com/filestore/docs/regions) | All regions. See the [Global regions map](https://bluexp.netapp.com/cloud-volumes-global-regions). | In [supported regions](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels#supported_regions)  
**RPO for disaster recovery** | About 30 minutes, with instance replicationNote 1 | About 30 minutes, with instance replicationNote 1 | As low as 15 minutesNote 1 | As low as 10 minutesNote 1 for cross-region replication.  
**Minimum storage** | See [Zonal tier](https://docs.cloud.google.com/filestore/docs/service-tiers-zonal) | See [Regional tier](https://docs.cloud.google.com/filestore/docs/service-tiers-regional) | 100 GB volume with 638 GB system disk | See [Google Cloud NetApp Volumes service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels)  
**Throughput performance** | See [Zonal tier](https://docs.cloud.google.com/filestore/docs/service-tiers-zonal)Note 2 | See [Regional tier](https://docs.cloud.google.com/filestore/docs/service-tiers-regional)Note 2 | Configuration dependent. See the [NetApp documentation.](https://www.netapp.com/pdf.html?item=/media/9090-tr4816pdf.pdf) | See [Volume performance sizing](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing)  
**Support provider** | Google Cloud | Google Cloud | NetApp for NetApp software, and Google Cloud for the infrastructure | Google Cloud  
  
**Table notes:**

  * **Note 1:** The times shown are approximate and depend on a variety of factors, including your system and network configuration, backup intervals, and recovery procedures.
  * **Note 2:** With the Filestore Zonal and Regional tiers, throughput scales with allocated capacity. For more information, see [Zonal tier](https://docs.cloud.google.com/filestore/docs/service-tiers-zonal) and [Regional tier](https://docs.cloud.google.com/filestore/docs/service-tiers-regional). You can also configure throughput to set up [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
