---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels/
title: Google Cloud NetApp Volumes service levels \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:59.000633+00:00
---

# Google Cloud NetApp Volumes service levels  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Google Cloud NetApp Volumes service levels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the capabilities of different service levels that NetApp Volumes offers to its users.

NetApp Volumes offers the following service levels:

  * Flex Unified

Flex Unified offers two different operation modes. For more information about modes, see [Default-mode versus ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#flex_unified_default-mode_versus_ontap-mode). Both modes are available as regular or large capacity pools.

  * Flex File

  * Standard

  * Premium

  * Extreme


**Important:** Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. For more information, see [Migration to Flex Unified service level](https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified).

Each service level offers different capacity options and performance levels to fit different use cases. The following table summarizes the features across service levels:

**Features** | **Service level type**  
---|---  
| Flex Unified | Flex File | Standard or Premium or Extreme  
**Storage pools**  
**Capacity** | 1 to 425 TiB | 1 to 200 TiB (regular pool)  
1 to 300 TiB (if custom performance is enabled) | Standard: 2 to 200 TiB   
  
Premium or Extreme: 2 TiB to 10 PiB  
**Large capacity pools** | Zonal only, no iSCSI:  
6 TiB to 2.48 PiB  
without auto-tiering  
  
6 TiB to 20 PiB  
with auto-tiering | No | Premium or Extreme: 2 TiB to 10 PiB  
**Granular resizing** | Yes, the storage pool can increase in 1 GiB increments | Yes, the storage pool can increase in 1 GiB increments | Yes, the storage pool can increase and decrease in 1 GiB increments  
**Performance** | Up to 5 GiBps throughput and 160,000 IOPS per storage pool  
  
Regions with limited performance:  
up to 1.6 GiBps throughput and  
90,000 IOPS per storage pool. Large capacity pools aren't supported.  
  
Large volumes up to 22 GiBps throughput and 750,000 IOPS. | Default performance: up to 16 KiBps per GiB of provisioned pool capacity   
  
Custom performance: up to 5 GiBps per zonal storage pool in select regions  | Standard: Up to 16 KiBps per GiB of provisioned volume capacity   
  
Premium: Up to 64 KiBps per GiB of provisioned volume capacity  
  
Extreme: Up to 128 KiBps per GiB of provisioned volume capacity  
  
Up to a maximum of 5 GiBps for regular volumes and 30 GiBps for large capacity volumes   
**Manual QoS** | Yes | No | Yes  
**Volumes**  
**High availability** | Zonal and Regional  
  
Zonal for large capacity pools | Zonal or Regional with the option for volume replication | Zonal with the option for volume replication  
**Capacity** | 1 GiB to 300 TiB  
  
1 GiB to 128 TiB (iSCSI and NVMe/TCP)  
  
20 MiB to 300 TiB  
(ONTAP-mode only) | 1 GiB to 100 TiB (regular volume)  
1 GiB to 300 TiB (if custom performance is enabled) | 100 GiB to 100 TiB  
**Large capacity volumes for NFS and SMB** | Default large volumes  
(48 member volumes):  
4.8 TiB to 2.48 PiB  
without auto-tiering  
4.8 TiB to 20 PiB  
with auto-tiering  
  
With custom number of member volumes (minimum 2):  
2,400 GiB to 2.48 PiB  
without auto-tiering  
2,400 GiB to 20 PiB  
with auto-tiering  
  
Minimum volume size of 100 GiB for ONTAP-mode | No | Standard: No  
  
Premium or Extreme: 15 TiB to 3 PiB  
(in allow-listed General Availability (GA))   
**Granular resizing** | Yes, the volume can increase and decrease in 1 GiB increments, but decreasing iSCSI volumes isn't supported | Yes, the volume can increase and decrease in 1 GiB increments | Yes, the volume can increase and decrease in 1 GiB increments  
**Auto-tiering** | Yes, with hot-tier autogrow | Yes, for custom-performance Flex File zonal pools in selected regions | Standard: No  
  
Premium or Extreme: Yes   
**Volume snapshots** | Up to 255 snapshots per volume  
  
Up to 1,023 snapshots per volume (ONTAP-mode only) | Up to 255 snapshots per volume | Up to 255 snapshots per volume  
**Volume clones** | Yes, thin and thick clones | Yes, thick clones | Yes, thick clones  
**Volume reversion** | Yes | Yes | Yes  
**Volume backups** | Yes | Yes | Yes  
**Service level changes allowed** | User can change provisioned throughput and IOPS of the pool | No | Standard: No  
  
Premium or Extreme: Yes, between Premium and Extreme  
**User and group quotas within volume** | Yes | No | Yes  
**FlexCache** | Yes | No | Standard: No  
  
Premium or Extreme: Yes (in allow-listed General Availability (GA))   
**Protocols**  
**SMB version support** | SMB 2.1, 3.0, and 3.1.1 | SMB 2.1, 3.0, and 3.1.1 | SMB 2.1, 3.0, and 3.1.1  
**SMB workgroup mode** | Yes (ONTAP-mode only) | Only domain mode | Only domain mode  
**SMB access-based enumeration (ABE)** | Yes | Yes | Yes  
**SMB3 encryption** | Yes | Yes | Yes  
**SMB3 continuously  
available shares** | Microsoft SQL Server and FSLogix | No | Microsoft SQL Server and FSLogix  
**NFS version support** | NFSv3, NFSv4.1, and NFSv4.2  
| NFSv3 and NFSv4.1 | NFSv3, NFSv4.1, and NFSv4.2  
**NFS extended group support** | Yes | Yes | Yes  
**NFSv4.1 security  
identifiers** | Yes | No | Yes  
**NFSv4.1 numeric IDs** | Yes | Yes | Yes  
**NFSv4.1 ACLs** | Yes | Yes | Yes  
**NFSv4.1 Kerberos** | krb5, krb5i, and krb5p | krb5, krb5i, and krb5p | krb5, krb5i, and krb5p  
**NFSv3 and NFSv4.1** | On the same volume | On the same volume | On the same volume  
**SMB and NFSv3/4.1** | On the same volume | No | On the same volume  
**NFSv4.2 extended attributes** | Yes, for NFSv4.1 enabled volumes | No | Yes, for NFSv4.1 enabled volumes  
**iSCSI** | Yes, on non-large capacity pools only | No | No  
**NVMe/TCP** | Yes (ONTAP-mode only) | No | No  
**S3 multiprotocol** | Yes (ONTAP-mode only) | No | No  
**All-squash** | Yes | Yes | Yes  
**Encryption at rest**  
**Google-owned and Google-managed encryption keys** | Yes | Yes | Yes  
**Customer-managed keys** | Yes | Yes | Yes  
**Active Directory integration**  
**Organizational Unit support** | Yes | Yes | Yes  
**Active Directory site support** | Yes | Yes | Yes  
**LDAP signing and sealing** | LDAP signing only, if required by domain controller | SMB LDAP: signing only, if required by domain controller  
  
NFS LDAP: required | LDAP signing only if required by domain controller  
**AES support for Kerberos** | Yes | Always on | Yes  
**Support local Administrators group** | Yes | Yes | Yes  
**Support local Backups Operators group** | Yes | Yes | Yes  
**Support defining Windows Security Operators** | Yes | Yes | Yes  
**Active Directory as LDAP server** | NFS, RFC2307bis schema  
  
Other schemas or LDAP servers with ONTAP-mode only | NFS, RFC2307bis schema | NFS, RFC2307bis schema  
**Active Directory as Kerberos server** | SMB, NFSv4.1, and NFSv4.2 | SMB, NFSv4.1, and NFSv4.2 | SMB, NFSv4.1, and NFSv4.2  
**Volume replication**  
**Volume replication to other locations** | Yes, between regular Flex Unified pools only. The other location can be other zone or region. | Yes, to Flex pools only. The other location must be another region. | Standard: Yes, to Standard pools only  
  
Premium or Extreme: Yes, between Premium and Extreme pools only. The other location must be another region.   
**Replication schedules** | 10 minute, 1 hour, and daily intervals  
  
Custom schedule (ONTAP-mode only) | 10 minute, 1 hour, and daily intervals | 10 minute, 1 hour, and daily intervals  
**Access to destination with  
active replication** | Read-only | Read-only | Read-only  
**Access to destination with  
stopped replication** | Read-write | Read-write | Read-write  
**Replication can switch directions** | Yes | Yes | Yes  
**Snapshots in replication** | Yes | Yes | Yes  
**Volume migration between ONTAP and NetApp Volumes** | Yes | No | Yes (in allow-listed General Availability (GA))  
**External replication (SnapMirror between ONTAP and NetApp Volumes)** | Yes | No | Yes (in allow-listed General Availability (GA))  
**Backups**  
**Manual backups** | Yes | Yes | Yes  
**Backup schedules** | Daily, weekly, and monthly  | Daily, weekly, and monthly | Daily, weekly, and monthly  
**Backup restores** | Full-volume, in region   
  
Full-volume within cross-regions | Full-volume, in region | Full-volume, in region   
  
Full-volume within cross-regions  
**Backup vault location** | Regional, same region   
  
Cross-region | Regional, same region | Regional, same region   
  
Cross-region  
**Selective file restore** | Yes | No | Yes  
**Immutable backups** | Yes (in allow-listed General Availability (GA)) | Yes (in allow-listed General Availability (GA)) | Yes (in allow-listed General Availability (GA))  
**CMEK backup** | Yes | No | Yes  
**Networking**  
**Shared VPC support** | Yes | Yes | Yes  
  
## Supported regions

The following table lists regions available for use in NetApp Volumes across service levels. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

Region name | Region description | Flex Unified | Flex File | Standard or Premium or Extreme  
---|---|---|---|---  
`africa-south1` | Johannesburg, South Africa | No | Yes | No  
`asia-east1` | Changhua County, Taiwan | Yes | Yes | No  
`asia-east2` | Hong Kong | No | Yes | No  
`asia-northeast1` | Tokyo, Japan | Yes (limited performance) | Yes | No  
`asia-northeast2` | Osaka, Japan | Yes | Yes | No  
`asia-northeast3` | Seoul, South Korea | No | Yes | No  
`asia-south1` | Mumbai, India | Yes | Yes | No  
`asia-south2` | Delhi, India | No | Yes | No  
`asia-southeast1` | Jurong West, Singapore | Yes | Yes | Yes  
`asia-southeast2` | Jakarta, Indonesia | No | Yes | No  
`australia-southeast1` | Sydney, Australia | Yes | Yes | Yes  
`australia-southeast2` | Melbourne, Australia | Yes | Yes | No  
`europe-central2` | Warsaw, Poland | No | Yes | No  
`europe-north1` | Hamina, Finland | No | Yes | No  
`europe-north2` | Stockholm, Sweden | No | Yes | No  
`europe-southwest1` | Madrid, Spain | Yes | Yes | Yes  
`europe-west1` | St. Ghislain, Belgium | Yes | Yes | No  
`europe-west2` | London, UK | Yes (limited performance) | Yes | Yes  
`europe-west3` | Frankfurt, Germany | Yes | Yes | Yes  
`europe-west4` | Eemshaven, Netherlands | Yes | Yes | Yes  
`europe-west6` | Zurich, Switzerland | No | Yes | Yes  
`europe-west8` | Milan, Italy | Yes | Yes | No  
`europe-west9` | Paris, France | Yes (limited performance) | Yes | No  
`europe-west10` | Berlin, Germany | No | Yes | No  
`europe-west12` | Turin, Italy | No | Yes | No  
`me-central1` | Doha, Qatar | No | Yes | No  
`me-central2` | Dammam, Saudi Arabia | Yes | Yes | No  
`me-west1` | Tel Aviv, Israel | Yes | Yes | No  
`northamerica-northeast1` | Montréal, Canada | No | Yes | Yes  
`northamerica-northeast2` | Toronto, Canada | No | Yes | Yes  
`northamerica-south1` | Queretaro, Mexico | No | Yes | No  
`southamerica-east1` | São Paulo, Brazil | Yes | Yes | No  
`southamerica-west1` | Santiago, Chile | No | Yes | No  
`us-central1` | Iowa, US | Yes | Yes | Yes  
`us-east1` | South Carolina, US | Yes | Yes | No  
`us-east4` | Northern Virginia, US | Yes | Yes | Yes  
`us-east5` | Columbus, US | Yes (limited performance) | Yes | No  
`us-south1` | Dallas, US | Yes | Yes | No  
`us-west1` | Oregon, US | Yes | Yes | No  
`us-west2` | Los Angeles, US | Yes (limited performance) | Yes | Yes  
`us-west3` | Salt Lake City, US | Yes (limited performance) | Yes | Yes  
`us-west4` | Las Vegas, US | Yes | Yes | Yes  
  
### Supported regions for Flex Unified custom performance

The following are the regions available for use for Flex Unified custom performance.

Region name | Region description | Zone names  
---|---|---  
`asia-east1` | Changhua County, Taiwan |  `asia-east1-b`  
`asia-east1-c`  
`asia-northeast2` | Osaka, Japan |  `asia-northeast2-a`  
`asia-northeast2-b`  
`asia-northeast2-c`  
`asia-south1` | Mumbai, India |  `asia-south1-b`  
`asia-south1-c`  
`asia-southeast1` | Jurong West, Singapore |  `asia-southeast1-a`  
`asia-southeast1-b`  
`australia-southeast1` | Sydney, Australia |  `australia-southeast1-a`  
`australia-southeast1-b`  
`australia-southeast1-c`  
`australia-southeast2` | Melbourne, Australia |  `australia-southeast2-a`  
`australia-southeast2-b`  
`australia-southeast2-c`  
`europe-southwest1` | Madrid, Spain |  `europe-southwest1-a`  
`europe-southwest1-b`  
`europe-west1` | St. Ghislain, Belgium |  `europe-west1-b`  
`europe-west1-c`  
`europe-west1-d`  
`europe-west3` | Frankfurt, Germany |  `europe-west3-a`  
`europe-west3-b`  
`europe-west3-c`  
`europe-west4` | Eemshaven, Netherlands |  `europe-west4-a`  
`europe-west4-b`  
`europe-west4-c`  
`europe-west8` | Milan, Italy |  `europe-west8-b`  
`europe-west8-c`  
`me-central2` | Dammam, Saudi Arabia |  `me-central2-a`  
`me-central2-b`  
`me-central2-c`  
`me-west1` | Tel Aviv, Israel |  `me-west1-a`  
`me-west1-b`  
`me-west1-c`  
`southamerica-east1` | São Paulo, Brazil |  `southamerica-east1-a`  
`southamerica-east1-b`  
`southamerica-east1-c`  
`us-central1` | Iowa, US |  `us-central1-a`  
`us-central1-b`  
`us-central1-c`  
`us-east1` | South Carolina, US |  `us-east1-b`  
`us-east1-c`  
`us-east1-d`  
`us-east4` | N. Virginia, US |  `us-east4-a`  
`us-east4-b`  
`us-east4-c`  
`us-south1` | Dallas, US |  `us-south1-a`  
`us-south1-b`  
`us-west1` | Oregon, US |  `us-west1-a`  
`us-west1-b`  
`us-west4` | Las Vegas, US |  `us-west4-a`  
`us-west4-b`  
  
### Supported regions for Flex Unified limited performance

The following regions support the Flex Unified limited performance, where the peak performance of a storage pool is capped to 1.6 GiBps and 90,000 IOPS. Large capacity pools aren't supported.

Region name | Region description | Zone names  
---|---|---  
`asia-northeast1` | Tokyo, Japan |  `asia-northeast1-b`  
`asia-northeast1-c`  
`europe-west2` | London, United Kingdom |  `europe-west2-b`  
`europe-west2-c`  
`europe-west9` | Paris, France |  `europe-west9-a`  
`europe-west9-b`  
`europe-west9-c`  
`us-east5` | Columbus, US |  `us-east5-b`  
`us-east5-c`  
`us-west3` | Salt Lake City, US |  `us-west3-a`  
`us-west3-b`  
`us-west3-c`  
`us-west2` | Los Angeles, US |  `us-west2-b`  
`us-west2-c`  
  
### Supported regions for Flex File custom performance

The following are the regions available for use for Flex File custom performance.

Region name | Region description | Zone names  
---|---|---  
`asia-east1` | Changhua County, Taiwan |  `asia-east1-a`  
`asia-east1-c`  
`asia-northeast1` | Tokyo, Japan |  `asia-northeast1-b`  
`asia-northeast1-c`  
`asia-northeast3` | Seoul, South Korea |  `asia-northeast3-b`  
`asia-northeast3-c`  
`asia-south1` | Mumbai, India |  `asia-south1-a`  
`asia-south1-b`  
`asia-south2` | Delhi, India |  `asia-south2-b`  
`asia-southeast1` | Jurong West, Singapore |  `asia-southeast1-a`  
`asia-southeast1-b`  
`europe-north2` | Stockholm, Sweden |  `europe-north2-a`  
`europe-north2-b`  
`europe-north2-c`  
`europe-west1` | St. Ghislain, Belgium |  `europe-west1-b`  
`europe-west1-c`  
`europe-west2` | London, United Kingdom |  `europe-west2-a`  
`europe-west2-b`  
`europe-west3` | Frankfurt, Germany |  `europe-west3-b`  
`europe-west4` | Eemshaven, Netherlands |  `europe-west4-a`  
`europe-west4-b`  
`europe-west4-c`  
`europe-west8` | Milan, Italy |  `europe-west8-b`  
`europe-west8-c`  
`europe-west9` | Paris, France |  `europe-west9-a`  
`europe-west9-c`  
`me-west1` | Tel Aviv, Israel |  `me-west1-b`  
`northamerica-northeast2` | Toronto, Canada |  `northamerica-northeast2-b`  
`northamerica-south1` | Queretaro, Mexico |  `northamerica-south1-a`  
`northamerica-south1-b`  
`northamerica-south1-c`  
`southamerica-east1` | São Paulo, Brazil |  `southamerica-east1-a`  
`us-central1` | Iowa, US |  `us-central1-a`  
`us-central1-b`  
`us-central1-c`  
`us-east1` | South Carolina, US |  `us-east1-b`  
`us-east1-c`  
`us-east1-d`  
`us-east4` | N. Virginia, US |  `us-east4-a`  
`us-east4-b`  
`us-east4-c`  
`us-east5` | Columbus, US |  `us-east5-a`  
`us-east5-b`  
`us-south1` | Dallas, US |  `us-south1-a`  
`us-west1` | Oregon, US |  `us-west1-a`  
`us-west1-b`  
`us-west1-c`  
`us-west3` | Salt Lake City, US |  `us-west3-a`  
`us-west3-b`  
`us-west4` | Las Vegas, US |  `us-west4-a`  
`us-west4-b`  
`us-west8` | Phoenix, US |  `us-west8-a`  
`us-west8-b`  
`us-west8-c`  
  
## What's next

NetApp Volumes [use cases](https://docs.cloud.google.com/netapp/volumes/docs/discover/use-cases).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
