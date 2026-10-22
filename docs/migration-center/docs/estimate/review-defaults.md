---
url: https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults/
title: Review default assumptions \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:03.484867+00:00
---

# Review default assumptions  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review default assumptions Stay organized with collections  Save and categorize content based on your preferences. 

To further refine your estimate results for migrating your on-premises infrastructure to Google Cloud, you can review and update the default assumptions used to calculate your cloud spend estimate.

However, the defaults are based on customer best practices. You must modify them for specific use cases only.

## Compute sizing default assumptions

To modify the compute sizing default assumptions, follow these steps:

  1. On the **Infrastructure** tab, click **Edit compute sizing details**.
  2. In the **Edit compute sizing details** pane that appears, edit the values of the fields listed in the following table as required:

Section| Field| Description| Default value  
---|---|---|---  
**Server**| **Compute servers older than 5 years**|  The percentage of servers that are older than 5 years.| `50%`  
**Efficiency factor for old Compute servers**|  The percentage of old servers that are efficient.| `55%`  
**Utilization**| **% of vCPUs not running 24x7**|  The percentage of vCPUs that don't run 24x7.| `50%`  
**% of time those vCPUs can be turned off (Compute)**|  The percentage of time these vCPUs can be turned off completely.| `20%`  
**Distribution of workloads** | **% of vCPUs (high-performance)** | The percentage of vCPUs reserved for high-performance workloads, such as databases, streaming, game servers, inference jobs. | `20%`  
**Machine type (high-performance)** | The machine type used for high-performance workloads. | `C3`  
**% of vCPUs (balanced)** | The percentage of vCPUs reserved for workloads that require a balance of price and performance, such as microservices, web and app servers, business intelligence solutions. | `60%`  
**Machine type** | The machine type used for balanced workloads. | `N2`  
**% of vCPUs (cost-optimized)** | The percentage of vCPUs reserved for workloads for which you want to minimize costs, such as development and testing environments, internal applications, batch processing jobs. | `20%`  
**Machine type (cost-optimized)** | The machine type used for cost-optimized workloads. | `E2`  
**Memory**| **Memory to Compute ratio (Compute)**|  Memory, in GB, to include for each vCPU.| `4`  



## Non-x86 sizing default assumptions

To modify the non-x86 infrastructure sizing default assumptions, follow these steps:

  1. On the **Infrastructure** tab, click **Edit non-x86 sizing details**.
  2. In the **Edit non-x86 sizing details** pane that appears, edit the values of the fields listed in the following table as required:

Section| Field| Description| Default value  
---|---|---|---  
**Emulation prices**| **Monthly Google Cloud cost per MIPS cost**|  The monthly cost for each MIPS running on Google Cloud.| `$4`  
**Emulation cost for lift and shift**|  The monthly cost of running the mainframe emulator for lift and shift mainframe applications.| `$0`  
**Price per month for Solaris emulation**|  The monthly cost for each Solaris emulation running on Google Cloud.| `$4`  
**Price per month for Solaris emulation licensing**|  The monthly cost for each Solaris emulation licensing on Google Cloud.| `$0`  
**Price per month for AIX emulation**|  The monthly cost for each AIX emulation running on Google Cloud.| `$4`  
**Price per month for AIX emulation licensing**|  The monthly cost for each AIX emulation licensing on Google Cloud.| `$0`  
**Price per month for HP UX emulation**|  The monthly cost for each HP UX emulation running on Google Cloud.| `$4`  
**Price per month for HP UX emulation licensing**|  The monthly cost for each HP UX emulation licensing on Google Cloud.| `$0`  
**Price per month for other emulation**|  The monthly cost for each of other emulation running on Google Cloud.| `$4`  
**Price per month for other emulation licensing**|  The monthly cost for each of other emulation licensing on Google Cloud.| `$0`  
Other CoLo prices| **Mainframe CoLo monthly price**|  Monthly cost for each mainframe colocation running on Google Cloud.| `$4`  



## Storage sizing default assumptions

To modify the storage sizing default assumptions, follow these steps:

  1. On the **Infrastructure** tab, click **Edit storage sizing details**.
  2. In the **Edit storage sizing details** pane that appears, edit the values of the fields listed in the following table as required:

Section| Field| Description| Default value  
---|---|---|---  
**Persistent Disk (Block storage)**| **Note** : The sum of values specified for **Storage footprint for HDD** and **Storage footprint for SSD** must add up to `100%`.  
**Storage footprint for HDD**|  The percentage of total storage in a [persistent disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) block storage resource with standard performance (hard disk drive).| `90%`  
**Storage footprint for SSD**|  The percentage of total storage in a [persistent disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) block storage resource with high-performance (solid state drive).| `10%`  
**Filestore  
(File storage)**| **Note** : The sum of percentages of the **Storage footprint for filestore HDD** and **Storage footprint for filestore SSD** must add up to `100%`.  
**Storage footprint for filestore HDD**|  The percentage of the total storage on [Filestore](https://docs.cloud.google.com/filestore/docs/overview) with standard-performance (hard disk drive).| `50%`  
**Storage footprint for filestore SSD**|  The percentage of the total storage on [Filestore](https://docs.cloud.google.com/filestore/docs/overview) with high-performance (solid state drive).| `50%`  
**Google Cloud Storage (Object storage)**| **Note:** The sum of percentages of the following Object storages must add up to `100%`.  
**Standard: High-frequency access**|  The percentage of object storage with high-frequency access (Standard). Suggested for frequently accessed data such as websites, streaming videos, and mobile applications.| `20%`  
**Nearline: Low-frequency access**|  The percentage of object storage with low-frequency access (Nearline). It is lower in terms of cost and suggested for data that can be stored for at least 30 days, such as data backup and long-tail multimedia content.| `40%`  
**Coldline: Low-frequency access**|  The percentage of object storage with low-frequency access (Coldline). It is very low cost and suggested for data that can be stored for at least 90 days, such as disaster recovery.| `20%`  
**Archive: Once a year access**|  The percentage of object storage with once-per-year access frequency (Archive). It is the lowest in terms of cost and suggested for data that can be stored for at least 365 days, such as regulatory archives.| `20%`  



## Oracle sizing default assumptions

To modify the Oracle sizing default assumptions, follow these steps:

  1. On the **Workloads and licenses** tab, click **Edit Oracle sizing details**.
  2. In the **Edit Oracle sizing details** pane that appears, edit the values of the fields listed in the following table as required:

Section| Field| Description| Default value  
---|---|---|---  
**Oracle edition breakdown**| **Note:** The sum of values specified for **% of Oracle Enterprise Edition vCPUs** and **% of Oracle Standard Edition vCPUs** must add up to `100%`.  
**% of Oracle Enterprise Edition vCPUs**|  The percentage of Oracle vCPUs that are on Oracle Enterprise Edition.| `70%`  
**% of Enterprise Edition vCPUs on 10g**|  The percentage of Oracle Enterprise Edition vCPUs that are on Oracle Database 10g.| `10%`  
**% of Oracle Standard Edition vCPUs**|  The percentage of Oracle vCPUs that are on Oracle Standard Edition.| `30%`  
**Oracle to PostgreSQL migration**| **% of Oracle Standard Edition migrating to PostgreSQL**|  The percentage of Oracle vCPUs migrating from Oracle Standard Edition to PostgreSQL.| `15%`  
**% of Oracle 10g or older migrating to PostgreSQL**|  The percentage of Oracle vCPUs migrating from Oracle Database 10g or other earlier versions of Oracle databases to PostgreSQL.| `100%`  
**Replace Exadata**| **Note:** The sum of values specified for **% of Exadata to Bare Metal Server** , **% of Exadata to BigQuery** , and **% of Exadata to Exadata CoLo (Hosting)** must add up to `100%`.  
**% of Exadata to Bare Metal Server**|  The percentage of Exadata vCPUs migrating to [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-planning).| `25%`  
**% of Exadata to BigQuery**|  The percentage of Exadata vCPUs migrating to [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction).| `25%`  
**% of Exadata to Exadata CoLo (Hosting)**|  The percentage of Exadata vCPUs migrating to colocated Exadata vCPUs running on Google Cloud.| `50%`  
**Exadata Storage in GB**|  The storage usage, in GB, for Oracle Exadata.| `0`  
**Additional migration defaults**| **Migrating reporting to BigQuery**|  The percentage of reporting vCPUs migrating to BigQuery.| `15%`  
**Move test / dev databases to snapshots**|  The percentage of test or developer database vCPUs migrating to snapshots.| `25%`  
**Better consolidation due to newer CPU / higher memory**|  The percentage of consolidation due to newer CPU or higher memory.| `25%`  
**Prices for Oracle to Google Cloud**| **Postgres price percentage on top of the Compute Engine monthly price**|  The percentage of Postgres price on top of the Compute Engine monthly price.| `80%`  
**BigQuery price percentage on top of the Compute Engine monthly price**|  The percentage of BigQuery price on top of the Compute Engine monthly prices.| `80%`  
**Exadata CoLo monthly price**|  The monthly price for colocated Exadata vCPUs running on Google Cloud.| `0`  



## SAP sizing default assumptions

To modify the SAP sizing default assumptions, follow these steps:

  1. On the **Workloads and licenses** tab, click **Edit SAP sizing details**.
  2. In the **Edit SAP sizing details** pane that appears, edit the values of the fields listed in the following table as required:

Section| Field| Description| Default value  
---|---|---|---  
**SAP workload**| **SAP workload that is currently outsourced**|  Such as Systems Integrator and Managed Service Provider.| `30%`  
**% subject to geo-specific regulations/rules for applications**|  The percentage of SAP vCPUs subject to geo-specific regulations or rules for applications.| `20%`  
**SAP database server**| **% SAP Servers older than 5 years**|  The percentage of the SAP server vCPUs that are older than 5 years.| `35%`  
**% system utilization of older SAP servers**|  The percentage of old SAP server vCPUs that are in use.| `60%`  
**Memory to vCPU ratio for SAP**|  The ratio of SAP RAM, in MB, and the number of SAP vCPUs.| `6`  
**% memory utilization for SAP**|  The percentage of memory used on SAP.| `90%`  
**% vCPUs not running 24x7**|  The percentage of the SAP vCPUs that don't run 24x7.| `40%`  
**% of time those vCPUs can be turned off for SAP**|  The percentage of the time that the SAP vCPUs can be turned off.| `20%`  
**SAP application server**| **% x86**|  The percentage of the SAP vCPUs that are x86 vCPUs.| `90%`  
**x86 - Linux**|  The percentage of the SAP vCPUs that are x86 Linux vCPUs.| `80%`  
**x86 - Windows**|  The percentage of the SAP vCPUs that are x86 Windows vCPUs.| `20%`  
**% non-X86 on IBM Power - AIX**|  The percentage of non-x86 SAP application server vCPUs running on IBM Power Systems with the AIX operating system.| `100%`  
**Shapes to use for SAP database and applications**| **Shape to use for SAP apps**|  Possible values are `N2D Predefined`, and `N2D Standard`, `N2D High Memory`| `N2D Predefined`  
**Shape to use for SAP databases**|  Shape to use for SAP databases. Possible values are `N2D Predefined`, `N2D Standard`, or `N2D High Memory`.| `N2D Predefined`  
**SAP database**| **Note:** The sum of values specified for **Database on Oracle DB** , **Database on MS SQL Server** , **Database on Hana** , and **Database on Other (DB2, ASE, etc.)** must add up to `100%`.  
**Database on Oracle DB**|  The percentage of SAP databases that are on Oracle DB.| `60%`  
**Oracle DB on AIX**|  The percentage of Oracle databases vCPUs that are on AIX.| `80%`  
**Oracle DB on Linux**|  The percentage of Oracle databases vCPUs that are on a Linux machine.| `20%`  
**Database on MS SQL Server**|  The percentage of SAP databases that are on MS SQL server.| `10%`  
**MS SQL Server on Windows**|  The percentage of MS SQL Server vCPUs that are on a Windows machine.| `100%`  
**Database on Hana**|  The percentage of SAP databases that are on Hana.| `15%`  
**Hana on Linux**|  The percentage of Hana vCPUs that are on a Linux machine.| `80%`  
**Hana on Power Linux**|  The percentage of Hana vCPUs that are on a Power Linux machine.| `20%`  
**Database on Other (DB2, ASE, etc.)**|  The percentage of SAP databases that are Other (DB2, ASE, etc.).| `15%`  
**Other on AIX**|  The percentage of other databases (DB2, ASE, etc.) that are on AIX.| `80%`  
**Other on Linux**|  The percentage of other databases (DB2, ASE, etc.) that are on a Linux machine.| `20%`  
**SAP prices**| **SAP application CoLo monthly price**|  Monthly price for SAP application colocation.| `0`  
**SAP database CoLo monthly price**|  Monthly price for SAP database colocation.| `0`  
  
## What's next

  * To learn how to scan your infrastructure and discover your assets, see how to [start an asset discovery](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
