---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1161/
title: Google Distributed Cloud air-gapped 1.16.1 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:12.336434+00:00
---

# Google Distributed Cloud air-gapped 1.16.1 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1161/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.16.1 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## June 5, 2026

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.16.1 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Important

**1.16.1 upgrade sequence requirements**

To safely upgrade to Distributed Cloud 1.16.1, you must complete all [mandatory pre-upgrade checks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/io-upgrade/intro) and execute the required upgrade sequence in order. Direct upgrades from any version prior to 1.15.1 will fail.

**If you are on version 1.14.7 or earlier** :

  1. **Apply hotfixes** : Install all required hotfixes for your current version.
  2. **Upgrade to 1.15.3** : Initiate and complete the upgrade to 1.15.3.
  3. **Upgrade to 1.16.1** : Initiate and complete the final upgrade to 1.16.1.



**If you are on version 1.15.1 or 1.15.3** : Upgrade directly to 1.16.1.

**If you are on version 1.15.2** : You must first upgrade to 1.15.3, and then upgrade to 1.16.1.

* * *

Feature

The following new features are available: 

**Cluster management**

  * Added support for A-series H200 and B300 machines for Kubernetes cluster nodes. For more information, see [Cluster node machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines).



**Infrastructure**

  * Added support for B300 bare metal machines in an organization.



**Managed Harbor Services**

  * Added support for project Service Accounts. This lets you use your service account identity to securely interact with your Harbor instances and manage container repositories. For more information, see [Managed Harbor Service overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/mhs-overview#mhs-features).



**Networking**

  * Cloud DNS is now generally available. This service provides a reliable, scalable way to manage Domain Name Service records, using a Kubernetes API or the command line. For more information, See [About Cloud DNS](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview).

  * DNS now supports TLS based encryption of all DNS traffic for system and first party services, both internally within Distributed Cloud, and between Distributed Cloud and customer networks.




**Observability**

  * Added observability tracking for workloads. This feature provides monitoring and logging capabilities designed to streamline the tracking and troubleshooting of workloads. For more information, see [Observability tracking for workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/track-metering).



**Storage**

  * Added support for auto-synchronous dual-zone buckets. During normal operations, the ingest policy synchronously writes object copies to both designated zones, with fallback to asynchronous replication during outages. 

  * Added support for supplying checksums in trailing HTTP headers in object uploads. This improves data integrity and error detection. For more information, see [Upload and download storage objects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upload-download-storage-objects).

  * Added enhancement that ensures object storage credentials are automatically deleted when their associated Service Account is removed. This prevents orphaned secrets in a project namespace. For more information, see [Delete storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-storage-buckets).

  * Added support for windowed uptime SLO for zonal S3 availability. This change ensures that health metrics are not skewed by multiple retries from single high-volume projects, providing a more accurate reflection of the actual user experience across an organization. 




**Virtual machines**

  * Added A-series A4 B300 machines to the list of supported VM machine types. For more information, see [View VM machine type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type#a-machine-series).

  * Added Windows 2022 image support for bring-your-own (BYO) custom images. For more information, see [GDC-supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images).

  * Added Secure Boot certificate renewal support for VMs with expiring certificates. For more information, see [Update Secure Boot certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot-cert-update).

  * Increased the maximum [Tier 1 networking](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-config-network) egress bandwidth limit from 25 Gbps to 32 Gbps per VM, depending on machine type and vCPU count, to handle demanding workloads.




* * *

Security

Updated the Rocky OS image version to 20260318 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2019-15505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15505)
  * [CVE-2020-36558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-36558)
  * [CVE-2021-4204](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4204)
  * [CVE-2021-33631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33631)
  * [CVE-2021-47461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47461)
  * [CVE-2021-47670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47670)
  * [CVE-2022-0500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0500)
  * [CVE-2022-0854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0854)
  * [CVE-2022-1016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1016)
  * [CVE-2022-1048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1048)
  * [CVE-2022-1158](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1158)
  * [CVE-2022-1679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1679)
  * [CVE-2022-2503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2503)
  * [CVE-2022-2639](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2639)
  * [CVE-2022-2873](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2873)
  * [CVE-2022-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2938)
  * [CVE-2022-2964](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2964)
  * [CVE-2022-3028](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3028)
  * [CVE-2022-3239](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3239)
  * [CVE-2022-3545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3545)
  * [CVE-2022-3564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3564)
  * [CVE-2022-3565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3565)
  * [CVE-2022-3567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3567)
  * [CVE-2022-3625](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3625)
  * [CVE-2022-3628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3628)
  * [CVE-2022-4129](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4129)
  * [CVE-2022-4139](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4139)
  * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)
  * [CVE-2022-4378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4378)
  * [CVE-2022-20141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20141)
  * [CVE-2022-20368](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20368)
  * [CVE-2022-21499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21499)
  * [CVE-2022-23222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23222)
  * [CVE-2022-26373](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-26373)
  * [CVE-2022-28390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28390)
  * [CVE-2022-29581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29581)
  * [CVE-2022-30594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30594)
  * [CVE-2022-36879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36879)
  * [CVE-2022-39188](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39188)
  * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)
  * [CVE-2022-41218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41218)
  * [CVE-2022-41222](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41222)
  * [CVE-2022-41674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41674)
  * [CVE-2022-41858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41858)
  * [CVE-2022-42896](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42896)
  * [CVE-2022-43750](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43750)
  * [CVE-2022-45884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45884)
  * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)
  * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)
  * [CVE-2022-47929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47929)
  * [CVE-2022-48637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48637)
  * [CVE-2022-48796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48796)
  * [CVE-2022-48839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48839)
  * [CVE-2022-48925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48925)
  * [CVE-2022-48929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48929)
  * [CVE-2022-49058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49058)
  * [CVE-2022-49111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49111)
  * [CVE-2022-49114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49114)
  * [CVE-2022-49122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49122)
  * [CVE-2022-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49290)
  * [CVE-2022-49291](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49291)
  * [CVE-2022-49328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49328)
  * [CVE-2022-49669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49669)
  * [CVE-2022-49696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49696)
  * [CVE-2022-49788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49788)
  * [CVE-2022-49803](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49803)
  * [CVE-2022-49846](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49846)
  * [CVE-2022-49872](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49872)
  * [CVE-2022-49907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49907)
  * [CVE-2022-49921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49921)
  * [CVE-2022-49977](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49977)
  * [CVE-2022-50020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50020)
  * [CVE-2022-50022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50022)
  * [CVE-2022-50030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50030)
  * [CVE-2022-50050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50050)
  * [CVE-2022-50066](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50066)
  * [CVE-2022-50087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50087)
  * [CVE-2022-50341](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50341)
  * [CVE-2022-50356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50356)
  * [CVE-2022-50367](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50367)
  * [CVE-2022-50386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50386)
  * [CVE-2022-50403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50403)
  * [CVE-2022-50410](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50410)
  * [CVE-2022-50543](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50543)
  * [CVE-2023-0266](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0266)
  * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)
  * [CVE-2023-0394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0394)
  * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)
  * [CVE-2023-0590](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0590)
  * [CVE-2023-0597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0597)
  * [CVE-2023-1073](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1073)
  * [CVE-2023-1079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1079)
  * [CVE-2023-1095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1095)
  * [CVE-2023-1192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1192)
  * [CVE-2023-1195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1195)
  * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)
  * [CVE-2023-1252](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1252)
  * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)
  * [CVE-2023-1382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1382)
  * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)
  * [CVE-2023-1838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1838)
  * [CVE-2023-1855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1855)
  * [CVE-2023-1998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1998)
  * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)
  * [CVE-2023-2162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2162)
  * [CVE-2023-2163](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2163)
  * [CVE-2023-2176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2176)
  * [CVE-2023-2235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2235)
  * [CVE-2023-2513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2513)
  * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)
  * [CVE-2023-3161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3161)
  * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)
  * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)
  * [CVE-2023-3567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3567)
  * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)
  * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)
  * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)
  * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)
  * [CVE-2023-3812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3812)
  * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)
  * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)
  * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)
  * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)
  * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)
  * [CVE-2023-4459](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4459)
  * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)
  * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)
  * [CVE-2023-4732](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4732)
  * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)
  * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)
  * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)
  * [CVE-2023-6546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6546)
  * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)
  * [CVE-2023-6610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6610)
  * [CVE-2023-6622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6622)
  * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)
  * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)
  * [CVE-2023-7324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7324)
  * [CVE-2023-23454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23454)
  * [CVE-2023-26545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26545)
  * [CVE-2023-28464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28464)
  * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)
  * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)
  * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)
  * [CVE-2023-33203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33203)
  * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)
  * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)
  * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)
  * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)
  * [CVE-2023-38409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38409)
  * [CVE-2023-39198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39198)
  * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)
  * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)
  * [CVE-2023-44466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44466)
  * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)
  * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)
  * [CVE-2023-51042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51042)
  * [CVE-2023-51043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51043)
  * [CVE-2023-51779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51779)
  * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)
  * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)
  * [CVE-2023-52525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52525)
  * [CVE-2023-52530](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52530)
  * [CVE-2023-52707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52707)
  * [CVE-2023-52922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52922)
  * [CVE-2023-53178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53178)
  * [CVE-2023-53226](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53226)
  * [CVE-2023-53232](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53232)
  * [CVE-2023-53257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53257)
  * [CVE-2023-53297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53297)
  * [CVE-2023-53322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53322)
  * [CVE-2023-53354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53354)
  * [CVE-2023-53365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53365)
  * [CVE-2023-53401](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53401)
  * [CVE-2023-53513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53513)
  * [CVE-2023-53581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53581)
  * [CVE-2023-53675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53675)
  * [CVE-2023-53680](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53680)
  * [CVE-2023-53705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53705)
  * [CVE-2023-53821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-53821)
  * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)
  * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)
  * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)
  * [CVE-2024-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25742)
  * [CVE-2024-26585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26585)
  * [CVE-2024-26598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26598)
  * [CVE-2024-26669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26669)
  * [CVE-2024-26704](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26704)
  * [CVE-2024-26832](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26832)
  * [CVE-2024-26852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26852)
  * [CVE-2024-26923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26923)
  * [CVE-2024-36904](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36904)
  * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)
  * [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)
  * [CVE-2024-41090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41090)
  * [CVE-2024-42281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42281)
  * [CVE-2024-42285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42285)
  * [CVE-2024-46858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46858)
  * [CVE-2024-47696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47696)
  * [CVE-2024-49978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-49978)
  * [CVE-2024-53104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53104)
  * [CVE-2024-53141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53141)
  * [CVE-2024-53150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53150)
  * [CVE-2024-56642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56642)
  * [CVE-2024-56661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56661)
  * [CVE-2025-21756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21756)
  * [CVE-2025-21785](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21785)
  * [CVE-2025-21919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21919)
  * [CVE-2025-21927](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21927)
  * [CVE-2025-22004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-22004)
  * [CVE-2025-23150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-23150)
  * [CVE-2025-37738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37738)
  * [CVE-2025-37797](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37797)
  * [CVE-2025-37890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37890)
  * [CVE-2025-37914](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37914)
  * [CVE-2025-38000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38000)
  * [CVE-2025-38051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38051)
  * [CVE-2025-38052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38052)
  * [CVE-2025-38061](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38061)
  * [CVE-2025-38079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38079)
  * [CVE-2025-38086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38086)
  * [CVE-2025-38107](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38107)
  * [CVE-2025-38124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38124)
  * [CVE-2025-38159](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38159)
  * [CVE-2025-38177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38177)
  * [CVE-2025-38200](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38200)
  * [CVE-2025-38211](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38211)
  * [CVE-2025-38250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38250)
  * [CVE-2025-38332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38332)
  * [CVE-2025-38350](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38350)
  * [CVE-2025-38352](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38352)
  * [CVE-2025-38380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38380)
  * [CVE-2025-38415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38415)
  * [CVE-2025-38459](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38459)
  * [CVE-2025-38461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38461)
  * [CVE-2025-38464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38464)
  * [CVE-2025-38498](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38498)
  * [CVE-2025-38684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38684)
  * [CVE-2025-38718](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38718)
  * [CVE-2025-38729](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38729)
  * [CVE-2025-39697](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39697)
  * [CVE-2025-39751](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39751)
  * [CVE-2025-39757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39757)
  * [CVE-2025-39817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39817)
  * [CVE-2025-39955](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39955)
  * [CVE-2025-39971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-39971)
  * [CVE-2025-40154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40154)
  * [CVE-2025-40186](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40186)
  * [CVE-2025-40258](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40258)
  * [CVE-2025-40277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40277)
  * [CVE-2025-40304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40304)
  * [CVE-2025-40322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-40322)
  * [CVE-2025-68285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-68285)
  * [CVE-2025-68349](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-68349)
  * [CVE-2026-23074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-23074)



* * *

Issue

The following issues are identified: 

**Cloud DNS**

  * Generic error messages are returned when the DNS OIRv2 feature gate stage is insufficient. 

  * The `dns-core-mz-cp` subcomponent reconciliation fails. 

  * DNS resolution fails from endpoints. 

  * Global gdcloud CLI required for Cloud DNS configurations. 




**Cluster management**

  * Kubernetes cluster is not removed after deletion. 

  * Static pods stuck due to kubelet deadlock. 

  * In an `accredited` environment, applying a `SubcomponentOverride` custom resource to override feature gates for an operable component causes continuous controller restarts. 

  * Accumulation of orphaned `Available` local `PersistentVolume` objects after node replacements or pod churn can cause `kube-apiserver` out-of-memory restarts on shared clusters and standard clusters. 




**Documentation**

  * Stale documentation shipped with the product release. 

  * Documentation instructions in tabbed format aren't viewable. 




**Endpoint detection and response**

  * The **Isolate Host** option is visible but not effective in the Kibana UI. 



**Firewall**

  * Cell configuration generation erroneously requires a `vsys` license for infrastructure firewalls. 



**GDC console**

  * Documentation hosted in the GDC console shows a 404 error. 



**gdcloud CLI**

  * Running any gdcloud CLI command prints an uninitialized feature flag warning. 



**Harbor**

  * Failover Registries report a `404 Not Found` error. 



**Hardware security module**

  * A file descriptor leak causes a `ServicesNotStarted` error. 



**Identity and access management**

  * Running gdcloud CLI or `kubectl` commands when `core/organization_console_url` is set to the global console URL might intermittently fail with a `401 Unauthorized` error. 

  * An `IAMRoleBinding` for `k8s-networkpolicy-admin` or `k8s-networkpolicy-viewer` causes `ZonalRoleBindingReplica` errors. 

  * A `CustomRole` resource that includes a `zonalRules` section might not grant permissions reliably. 

  * Keycloak deployment fails for the `opsservices` organization. 

  * Keycloak user attribute modifications for Tenable are not reflected. 

  * The Keycloak identity provider must be configured manually in the OIRv2 root admin cluster. 

  * RotatableSecret ais-encryption-key-secret is reporting false with IAM-0100 timed out. 




**Infrastructure as Code (IAC)**

  * Upgrades from GDC version 1.15 to 1.16 with IAC might fail. 

  * GitLab job might fail silently and prevent GitLab startup. 

  * The IAC-3211 alert falsely triggers for an `iac-creds-replica` secret expiration. 




**Inventory**

b/534561687 #} 

  * Bootstrapping or deployment fails due to special characters in auto-generated passwords. 

  * The root admin cluster deployment fails due to a device model and transceiver model validation error. 

  * During inventory validation, a warning is shown when a cable has `FS` as a transceiver vendor. 

  * Cell or rack names with more than two letters aren't supported. 

  * Preflight validation (`2-mgmtsw-connection`) reports false management switch connection failures (`VAL-E1001`) for bare-metal server `LOM1` ports or storage switch `mgmt0` ports during initial installation or a re-bootstrap. 

  * Cell configuration validation fails for the single NTP appliance in an OIRv2 rack because the TOR switch pairing check requires a connection on both TOR switches. 




**IO shell**

  * Expired `IOShell` resources block resource creation or updates. 

  * Usernames that don't follow RFC 1123 break IO Shell creation. 

  * Hyphens in organization or zone names cause naming collisions. 

  * SSH connections to bare metal nodes using management internal IP addresses fail. 




**IP address management (IPAM)**

  * After upgrading to 1.16.1 or later, service accounts that manage subnets referencing a parent in the `platform` namespace require the `shared-subnet-user` role in the `platform` namespace. 



**Key management system**

  * KMS configured to use a CTM root key does not failover when an HSM is unavailable. 

  * The `kms-mz-global-cm` subcomponent upgrade fails in organization clusters. 

  * Unable to SSH to Thales HSM devices from IO Shell. **Monitoring**

  * The `mon-system` StatefulSet Helm upgrade fails with forbidden Pod spec. 

  * Platform administrators cannot view the Alerting page in the GDC console for the `platform-obs` project. 




**Networking**

  * External `kubectl` requests to standard cluster API servers fail with an `RBAC: access denied` error when only `matchTypes: ["api-server"]` is configured in an `OrganizationNetworkPolicy`. 



**Network Time Protocol (NTP)**

  * The `ntp-relay-controller` pod might enter a crash loop state due to out-of-memory errors. 

  * The `manage_syncserver_time.py` script crashes when checking time during deployment. 

  * When deploying OIRv2 management switches, NTP configuration and encryption might not apply to the running configuration. 

  * NTP servers trigger false hardware reference clock sync alerts. 




**Operating system**

  * User clusters stuck in `Reconciling` state due to insufficient `/var/log` partition size. 

  * Node upgrades fail or system locks up due to `pam_tty_audit.so` session leaks. 




**Platform authentication**

  * Expired `*-cert` secrets leak after Kubernetes cluster deletion. 



**Resource Manager**

  * The Resource Manager project controller might enter a crash loop state due to out-of-memory errors. 



**Security Information and Event Management (SIEM)**

  * Elastic storage disks can reach full capacity in roughly 30 days. 

  * SIEM v2 rollout fails to complete on non-OIRv2 clusters. 

  * Splunk indexer volumes trigger false-positive storage threshold alerts. 




**Servers**

  * Bootstrapper installation fails during file system configuration with a `matched no disk` error. 

  * The server bootstrap fails with an iDRAC error. 

  * Server provisioning fails with a `BMCConfigPreinstallLicenseInstallCompleted` status condition error for Dell servers. 

  * A `BareMetalHostNetwork` custom resource might contain multiple management gateway routes. 




**Storage**

  * Bootstrapping a new tenant organization hangs during the `VMImageDistributing` step when Nearline storage is enabled. 

  * The ONTAP S3 event audit logging is disabled. 

  * ONTAP upgrade fails due to missing network routes. 

  * The `StorageCluster` validation fails during bootstrap. 

  * When performing list object requests on buckets containing multi-part uploads, the requests might fail and the `obj-s3-availability` metric might drop. 

  * Object storage audit log forwarding might fail during a sequential upgrade due to missing `Bucket` custom resources. 

  * Object storage audit log forwarder fails due to DNS lookup failure. 

  * StorageGRID upgrades might get stuck with a no upgrade uploaded error. 

  * Bucket creation and updates take longer than expected. 




**Ticketing system**

  * The `ts-app-server-1` pod restarts periodically. 



**Virtual machines**

  * Perimeter cluster VMs might fail during creation due to missing `macvtap` (`/dev/tap*`) devices when `onetd` recreates the `adminvrf0` and `datavrf0` VLAN interfaces. 

  * When you create a Windows VM using the gdcloud CLI CLI `gdcloud compute instances create`, the VM fails to boot due to the default BIOS boot type `bios` and missing secure boot flags. 

  * `gpu-controller-controller-manager pod` enters an `ImagePullBackOff` state during upgrade to release 1.16.1. 

  * A-series `a4-ultragpu-8g` VMs that use a guest OS with a 4.x kernel might take over 25 minutes to start. 

  * VM creation with types `a3-ultragpu-8g` and `a4-ultragpu-8g` on a newly reprovisioned server fails with errors. 

  * The monthly `dbsadmin` password rotation of the VM metadata server database fails because Database Service no longer deletes the `db-pw-metadata-dbcluster` secret after applying the password. After the next restart of the `metadata-server-controller-manager` pods or the database, the metadata server can't connect to its database. 




**Vulnerability management**

  * Vulnerability scans using Tenable Enclave might not complete. 

  * Unable to access Tenable Enclave. 




* * *

Fixed

The following issues are fixed: 

**Firewall**

  * Legacy firewall rules might block organization to root admin traffic after upgrade. 



**Identity and access management**

  * An OPA Gatekeeper trust issue after a root CA rotation prevents IAM role creation in new projects. 



**Networking**

  * Preflight validation no longer reports false connection failures between the management switches and the firewall management ports. 



**Storage**

  * Frequent OBJ-A0003 alerts persist despite standard silencing efforts. 

  * After StorageGRID primary admin node downtime, object storage upgrade attempts performed using an `ObjectStorageUpgradeRequest` CR might fail due to requests being directed to the non-primary StorageGRID admin node. 




**Virtual machines**

  * When you import a VM disk image using the `gdcloud compute images import` command or the `VirtualMachineImageImport` custom resource, the import operation gets stuck at the `JobImport` stage if the `VirtualMachineImageImport` resource name exceeds 33 characters (or 28 characters for the image name passed to the gdcloud CLI). 



* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.32.1100-gke.88 to apply the latest security patches and important updates. 

For more information, see the [Google Distributed Cloud for bare metal 1.32.1100 release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#April_23_2026).




* * *

Deprecated

The following features are deprecated: 

**Database services**

  * The Database Service is deprecating its legacy high availability (HA) implementation in versions 1.14.12 and earlier. Legacy HA database clusters will be supported until its sunset date, which is to be announced. There is no user-facing change in the new HA feature, as the API for enabling and disabling HA remains the same. To verify if your HA database cluster is using the new implementation, check if the annotation `dbcluster.dbadmin.goog/raasEnabled` exists on your HA database cluster CR. This annotation will only appear on HA database clusters using the new implementation. If you don't have this annotation, you can [migrate to the latest HA implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-ha#migrate-latest-ha).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
