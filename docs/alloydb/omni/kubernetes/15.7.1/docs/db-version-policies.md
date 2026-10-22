---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/db-version-policies/
title: Database version policies \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:54.013578+00:00
---

# Database version policies  |  AlloyDB Omni for Kubernetes: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/db-version-policies/

This page documents AlloyDB Omni version **15.7.1** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/resources)



Send feedback 

#  Database version policies Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/db-version-policies)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/db-version-policies)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/db-version-policies)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/db-version-policies)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/db-version-policies)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/db-version-policies)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/db-version-policies)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/db-version-policies)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/db-version-policies)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/db-version-policies)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/db-version-policies)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/db-version-policies)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/db-version-policies)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/db-version-policies)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/db-version-policies)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/db-version-policies)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/db-version-policies)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/db-version-policies)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/db-version-policies)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/db-version-policies)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/db-version-policies)



This page describes the support, retirement, and compatibility policies for AlloyDB Omni major and minor versions, and the AlloyDB Omni Kubernetes operator.

For information about AlloyDB for PostgreSQL version policies, see [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

### AlloyDB Omni version policies

Every version of AlloyDB Omni has compatibility with a specific version of PostgreSQL, as detailed in Support policy.

Because AlloyDB Omni is software that you install and run yourself, you are responsible for regularly updating your AlloyDB Omni installation. Learn about the latest versions of AlloyDB Omni in the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/docs/release-notes).

For AlloyDB Omni, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility. Some AlloyDB Omni releases are updates to AlloyDB Omni itself, independent of updates to PostgreSQL support. These releases include bug fixes and security updates, and are reflected in an incremental increase of the third number in the release version. For example, the 2 in 18.1.2 indicates an update to AlloyDB Omni.

## Support policy

Google provides support for AlloyDB Omni versions and the AlloyDB Omni operator based on the following timelines:

Version type | Support period  
---|---  
**Major versions** | Supported for **5 years** from the initial release date, matching the community support lifecycle of the underlying PostgreSQL version.  
**Minor versions** | Supported for **1 year** from their specific release date.  
**Kubernetes operator versions** | Supported for **1 year** from their specific release date. To find the release date for an operator version, see [AlloyDB Omni release notes](/alloydb/omni/kubernetes/current/docs/release-notes).  
  
## Major version support timeline

The following table lists the general availability (GA) dates of AlloyDB Omni support for PostgreSQL major versions. These dates serve as the "initial release date" for calculating the 5-year support window.

PostgreSQL major version | GA date  
---|---  
18 | April 9, 2026  
17 | December 15, 2025  
16 | April 8, 2025  
15 | October 11, 2023  
  
After a version exceeds its support period, it is considered retired. Google doesn't process support tickets for retired versions and recommends that you upgrade to a supported version to continue receiving assistance.

## Supported PostgreSQL versions

AlloyDB Omni supports compatibility with the following PostgreSQL database versions:

PostgreSQL version | AlloyDB Omni version | Status  
---|---|---  
18.4 | 18.4.0 | Supported  
18.3 | 18.3.0 | Supported  
18.1 | 18.1.0 | Supported  
17.10 | 17.10.0 | Supported  
17.9 | 17.9.0 | Supported  
17.7 | 17.7.0 | Supported  
17.5 | 17.5.0 | Supported  
16.14 | 16.14.0 | Supported  
16.13 | 16.13.0 | Supported  
16.11 | 16.11.0 | Supported  
16.9 | 16.9.0 | Supported  
15.18 | 15.18.0 | Supported  
15.17 | 15.17.0 | Supported  
15.15 | 15.15.0 | Supported  
15.13 | 15.13.0 | Supported  
  
## Patch policy

To ensure the security and stability of your environment, Google applies patches for critical bugs and vulnerabilities according to the following policy:

  * Patches are applied only to the **latest minor version** of each supported major version.
  * If you encounter an issue on an older minor version, you must upgrade to the latest available minor version of that major version to receive the fix.



## Upgrade and compatibility

The version numbers for AlloyDB Omni indicate the version of PostgreSQL they support using the format `MAJOR_VERSION.MINOR_VERSION.OMNI_PATCH_VERSION`. The major and minor version numbers match the version of the underlying PostgreSQL engine, while the third number represents the AlloyDB Omni patch version.

Some AlloyDB Omni releases are updates to AlloyDB Omni itself, independent of updates to PostgreSQL support. These releases include bug fixes and security updates, and are reflected in an incremental increase of the third number in the release version. For example, the 2 in 18.1.2 indicates an update to AlloyDB Omni.

Policy category | Description  
---|---  
**Major version timing** | Google aims to support new PostgreSQL major versions within eight months of the release of the first minor release, version x.1, of a new PostgreSQL major version. For AlloyDB Omni in Google Distributed Cloud, Google aims to support compatibility with a new major PostgreSQL version within four months of its availability in AlloyDB Omni.  
**Minor version timing** | Google aims to release support for new PostgreSQL minor versions every quarter. Because AlloyDB Omni is software that you install and run yourself, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility.  
**Upgrade order** | You must upgrade the AlloyDB Omni operator before upgrading your database clusters (data planes).  
**Security updates** | Google aims to release fixes within one month of a PostgreSQL community security release.  
**Operator compatibility** | The operator is designed to manage data planes up to 1 year old.  
**Upgrade path** | 

  * You can skip minor or patch versions during an upgrade, provided that the version gap doesn't exceed the 1-year support period.
  * Rollbacks are only supported to the version used immediately before the upgrade.

  
  
## Data protection

The AlloyDB Omni operator doesn't perform automatic backups before an upgrade. You are responsible for taking a manual backup of your data before triggering an upgrade process.

## What's next

  * [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
