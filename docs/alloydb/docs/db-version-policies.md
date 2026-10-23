---
url: https://docs.cloud.google.com/alloydb/docs/db-version-policies/
title: Database version policies \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:55.262540+00:00
---

# Database version policies  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/db-version-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  Database version policies Stay organized with collections  Save and categorize content based on your preferences. 

To plan database upgrades and keep your clusters running on supported PostgreSQL releases, you can use the major and minor database version support policies, lifecycle timelines, and deprecation schedules for AlloyDB for PostgreSQL.

For information about AlloyDB Omni version policies, see [AlloyDB Omni database version policies](https://docs.cloud.google.com/alloydb/omni/docs/db-version-policies). 

## AlloyDB version policies

AlloyDB instances run a database server created and maintained by Google Cloud that is fully compatible with PostgreSQL. You have control over which major PostgreSQL version your instances are compatible with. AlloyDB keeps the minor version compatibility of instances automatically updated.

Every AlloyDB cluster supports compatibility with a specific PostgreSQL major version—for example, PostgreSQL 18. You choose the major version when you create the cluster. After you choose a major version, the cluster retains that major version for the duration of its lifetime unless you initiate a major version upgrade. You can upgrade a cluster by performing an [in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version) or by [migrating the cluster's data to a new cluster](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade).

Every AlloyDB instance runs a database service that is compatible with a specific minor PostgreSQL version—for example, 16.3. AlloyDB releases minor version compatibility updates several times per year, and automatically applies these updates to instances. These updates keep every instance up to date with the most recent bug fixes and security patches available for its major version.

## Major version policy

This section describes the compatibility and support lifecycle for major versions in AlloyDB.

### Regular support

Google Cloud aims to offer timely support for AlloyDB compatibility with new PostgreSQL major versions. The timing of that support depends on the AlloyDB product:

  * AlloyDB for PostgreSQL: Google Cloud aims to support compatibility with a new major PostgreSQL version within five months of a general availability release by the PostgreSQL developer community.

The first phase of this support is regular support. During regular support, AlloyDB provides minor version and maintenance updates, and it applies security fixes to the instances. AlloyDB offers regular support for a major version as long as the database engine developer community supports the major version, no less than five years. After the major version reaches end-of-life (EOL) by the community, the major version enters the extended support phase of the lifecycle.


\- AlloyDB in Google Distributed Cloud: Google Cloud aims to support compatibility with a new major PostgreSQL version within four months of the availability of that major version in AlloyDB Omni. 

These are general guidelines. The actual release times for new version might differ.

### Extended support

Google Cloud uses [the PostgreSQL community's end-of-life schedule](https://www.postgresql.org/support/versioning/) when planning the end of regular support for compatibility with any PostgreSQL major version.

For AlloyDB major versions that reach their EOL, AlloyDB offers extended support. Extended support lets you continue running your AlloyDB instances for three years after the developer community stops supporting the major versions on which the instances are running. Extended support is offered for three years. You can use this time to plan, test, and perform the upgrade of your instances to a major version that is in regular support. For more information about performing a major version upgrade, see [Upgrade the database major version in-place](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version) and [Upgrade a cluster's major server version](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade) by migrating data.

For more information about extended support, see [Extended support in AlloyDB](https://docs.cloud.google.com/alloydb/docs/extended-support).

### Deprecation

After extended support ends for a major version, AlloyDB deprecates the major version. When Google Cloud plans to end extended support for a major version of PostgreSQL, Google Cloud provides the following to project owners:

  * End-of-support notices, sent at least 12 months ahead of time, at the end of the second year of extended support.
  * Tools and documentation to minimize upgrade disruption.



Any AlloyDB cluster still running the deprecated major database version at the end of the extended support period is automatically upgraded to the default version at that time.

### Major version support timeline

The following table shows the dates when AlloyDB support for compatible versions became generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

PostgreSQL compatible major version | AlloyDB regular support start date | AlloyDB Omni version support GA date | AlloyDB extended support start date | AlloyDB deprecation date  
---|---|---|---|---  
PostgreSQL 18 | March 18, 2026 | April 9, 2026 | - | -  
PostgreSQL 17 | September 22, 2025 | December 15, 2025 | February 1, 2030 | February 1, 2033  
PostgreSQL 16 | October 23, 2024 | April 8, 2025 | February 1, 2029 | February 1, 2032  
PostgreSQL 15 | January 19, 2024 | October 11, 2023 | February 1, 2028 | February 1, 2031  
PostgreSQL 14 | December 12, 2022 | Not applicable | February 1, 2027 | February 1, 2030  
  
## Version dependencies for AlloyDB features

Some AlloyDB features might require a major version of PostgreSQL compatibility in order to run on an AlloyDB instance. Minimum version requirements for features are documented.

## Minor version support

AlloyDB and AlloyDB in Distributed Cloud aim to release compatibility support for a new minor PostgreSQL version every quarter. These updates include bug fixes and security fixes. The release schedule can vary depending on the need for additional bug fixes.

After AlloyDB releases support for a new minor PostgreSQL version, Google Cloud automatically applies this update to all instances. These updates are propagated during a subsequent maintenance rollout. For more information about automatic AlloyDB maintenance, see [About maintenance](https://docs.cloud.google.com/alloydb/docs/maintenance).

For example, if AlloyDB releases support for a new minor version of PostgreSQL 17, then a cluster configured with PostgreSQL 17 compatibility has all of its instances upgraded to this new minor version during a subsequent scheduled maintenance operation.

When you create an AlloyDB instance, it runs the most recently supported minor version within the major PostgreSQL version.

## Supported major and minor version support

AlloyDB supports compatibility with the following PostgreSQL database versions:

PostgreSQL-compatible version | AlloyDB  
---|---  
PostgreSQL 18 | 18.3  
PostgreSQL 17 (default) | 17.9  
PostgreSQL 16 | 16.13  
PostgreSQL 15 |  15.17  
PostgreSQL 14 |  14.22  
  
#### PostgreSQL 18 compatibility

Before you use PostgreSQL 18 as your database version, consider the following:

  * Logical replication from the standby server isn't supported.



#### PostgreSQL 17 compatibility

Before you use PostgreSQL 17 as your database version, consider the following:

  * Logical replication from the standby server isn't supported.



#### PostgreSQL 16 compatibility

Before you use PostgreSQL 16 as your database version, consider the following:

  * Logical replication from the standby server isn't supported.



## Security updates

When the PostgreSQL community releases minor versions with security fixes, the AlloyDB security team reviews them for the criticality and impact.

For AlloyDB for PostgreSQL, critical fixes are backported and your clusters are updated as part of a subsequent maintenance rollout. Google Cloud aims to apply critical patches within one month.

Less severe fixes are included in future minor version upgrades. This ensures that your clusters are always up to date with the latest security fixes, and are protected from potential attacks.

## What's next

  * [AlloyDB Omni database version policies](https://docs.cloud.google.com/alloydb/omni/docs/db-version-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
