---
url: https://docs.cloud.google.com/alloydb/docs/extended-support/
title: Extended support for AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:56.441246+00:00
---

# Extended support for AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/extended-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  Extended support for AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers extended support for AlloyDB for PostgreSQL major versions that reach end-of-life (EOL) based on PostgreSQL community policies. For an additional cost, AlloyDB extended support gives you extra time to plan major version upgrades while continuing to receive security patches, bug fixes, and standard support coverage.

**Important:** All AlloyDB instances that run community end-of-life (EOL) major versions of PostgreSQL are automatically enrolled in extended support.

## Overview

AlloyDB major versions that reach end-of-life (EOL) by the developer community are automatically enrolled in AlloyDB extended support. For more information about AlloyDB database versions and extended support timelines, see [Major and minor versions supported by AlloyDB](https://docs.cloud.google.com/alloydb/docs/db-version-policies#timeline-table).

During extended support, AlloyDB clusters are automatically enrolled, and you receive the following benefits:

  * Security fixes: instances receive patches for all critical and high severity Common Vulnerabilities and Exposures (CVE).
  * Product bug fixes: resolution of bugs in AlloyDB-maintained code. 
  * Service Level Agreement (SLA): coverage for clusters that meet the eligibility criteria as documented in the [SLA](https://cloud.google.com/alloydb/sla). 
  * Support for new cluster creation: you can create new AlloyDB clusters that use major versions in extended support.



When an instance is enrolled in extended support, you're charged for the cost of extended support in addition to the regular costs of the instance. For more information about pricing, see the [Extended support for AlloyDB](https://cloud.google.com/alloydb/pricing#extended-support-pricing).

Clusters that are enrolled in extended support don't receive new features and service improvements that are implemented in AlloyDB for PostgreSQL after the end of your regular support period. We strongly recommend that you operate your clusters on major versions that are in regular support. To stay in regular support, you can upgrade your cluster.

## Lifecycle of an extended support instance

An extended support instance goes through several phases before extended support ends.

### Before the extended support period begins

Three months before a AlloyDB major version enters extended support and before billing for extended support starts, notifications for your cluster appear in the Google Cloud console. The project owner also receives email notifications about the upcoming extended support event.

### Cluster enrollment

A cluster enters the extended support period when its major version reaches the AlloyDB end-of-life (EOL) date, which is three months after the major version reaches its EOL by the PostgreSQL developer community. At this time, all AlloyDB for PostgreSQL clusters running the major version that has reached EOL are automatically enrolled in extended support.

On the date when a major version enters extended support, all clusters that are running the major version are automatically enrolled and are billed for extended support, in addition to regular instance charges.

To enroll in extended support and to keep your instance on an existing major version that reaches EOL, you don't need to do anything.

### End of extended support

A cluster can remain in extended support for up to three years. After a major version has been in extended support for three years, the major version is deprecated. When a major version is deprecated, AlloyDB automatically upgrades all deprecated major version clusters to the default major version.

After the upgrade, the clusters receive standard support. The upgrade is performed as part of regular AlloyDB maintenance. For more information about the end of extended support for major versions, see [Deprecation](https://docs.cloud.google.com/alloydb/docs/db-version-policies#deprecation).

To remove a cluster from extended support before the three-year period ends, upgrade the cluster to a major version in standard support. Whether you upgrade the cluster yourself or the cluster is upgraded automatically, after the upgrade is complete, the additional charges for extended support are stopped, and you are billed only for the costs of the cluster.

## Pricing

Extended support is a paid service and is in addition to the current costs of your cluster. For more information about pricing, see the [Extended support for AlloyDB](https://cloud.google.com/alloydb/pricing#extended-support-pricing). 

## Upgrade clusters to opt out of extended support

Although clusters are automatically enrolled in extended support, you can opt out of extended support at any time by upgrading your cluster to a major version in regular support. To avoid additional extended support charges, we recommend that you upgrade your cluster before the start of the extended support period.

If you upgrade a cluster that's enrolled in extended support to a major version that's in regular support, then you're no longer charged for extended support.

To upgrade your cluster, you can perform an in-place major version upgrade or you can migrate data to upgrade the database. For more information, see [Upgrade a cluster's major server version](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
