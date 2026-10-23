---
url: https://docs.cloud.google.com/sap/docs/release-notes/
title: SAP on Google Cloud release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:39.786102+00:00
---

# SAP on Google Cloud release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Resources ](https://docs.cloud.google.com/sap/docs/resources)



Send feedback 

#  SAP on Google Cloud release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains announcements that are important to users of SAP on Google Cloud, including: 

  * SAP certifications of Google Cloud products and services
  * Releases, updates, or deprecations of the Google Cloud products, services, and support that are used with SAP on Google Cloud
  * Relevant known issues and bug fixes

For announcements about Compute Engine VMs, persistent disks, OS images, and other offerings that are not specific to SAP on Google Cloud, see the [Compute Engine release notes page](https://docs.cloud.google.com/compute/docs/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/sapongooglecloud-release-notes.xml) directly. 

## September 29, 2026

Announcement

**Hyperdisk sizing widget for SAP HANA**

To view Hyperdisk-based disk configurations that help you meet SAP HANA size and performance requirements, use the sizing widget that's available in the [Minimum sizes for SSD-based Persistent Disk or Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced) section of the SAP HANA planning guide. This widget lets you select an SAP-certified machine type and view up to three tailored disk configurations that Google Cloud recommends for it.

## September 24, 2026

Announcement

**New SAP certifications: X5 series of memory-optimized bare metal machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the Compute Engine X5 series of memory-optimized bare metal machine types with the Intel Granite Rapids CPU platform.

For more information, see:

  * For SAP HANA, see [X5 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x5-memory-optimized)
  * For SAP NetWeaver, see [X5 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-x5)



## July 24, 2026

Announcement

**New SAP certification for operating system: SLES 16 for SAP**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system SUSE Linux Enterprise Server (SLES) 16 for SAP.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## July 10, 2026

Announcement

**New SAP certifications: M4N series of memory-optimized machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the Compute Engine memory-optimized M4N series machine types with the Intel Emerald Rapids CPU platform.

For more information, see:

  * For SAP HANA, see [M4N memory-optimized machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#m4n-memory-optimized)
  * For SAP NetWeaver, see [M4N memory-optimized machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-mem-optimized-m4n)



## June 23, 2026

Announcement

**ABAP SDK for Google Cloud version 1.14 (On-premises or any cloud edition)**

Version 1.14 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA).

This version resolves an issue that occurred during signature verification for Cloud Storage content repository and removes an unreferenced node from the SPRO configuration menu.

For more information, see [What's new with the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-14).

Announcement

**BigQuery Connector for SAP version 2.15**

Version 2.15 of the BigQuery Connector for SAP is generally available (GA). This version resolves issues related to column descriptions in standalone SLT system configurations and attribute consistency in Pub/Sub messages during Change Data Capture (CDC) replication.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-15).

## June 04, 2026

Announcement

**Google Cloud's Agent for SAP version 3.15**

Version 3.15 of Google Cloud's Agent for SAP is generally available (GA). This version updates the libraries in the agent's [GitHub repository](https://github.com/GoogleCloudPlatform/sapagent) to address vulnerabilities when you're building the agent from its GitHub source.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## June 01, 2026

Announcement

**New SAP certification for operating system: RHEL 10.0 for SAP**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) 10.0 for SAP.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## May 21, 2026

Announcement

**Google Cloud's Agent for SAP version 3.14**

Version 3.14 of Google Cloud's Agent for SAP is generally available (GA). This version introduces support for using a customer-managed encryption key (CMEK) to encrypt disks during disk snapshot based SAP HANA recovery, some logging and stability enhancements, and minor bug fixes.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## May 12, 2026

Announcement

**BigQuery Connector for SAP version 2.14**

Version 2.14 of the BigQuery Connector for SAP is generally available (GA). To protect configuration data, this version assigns the BigQuery Connector for SAP configuration tables to the custom authorization group `ZSGC`. You must ensure your user roles include authorization for this group to maintain access.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-14).

## April 30, 2026

Announcement

**BigQuery Connector for SAP version 2.13**

Version 2.13 of the BigQuery Connector for SAP is generally available (GA). This version resolves an issue where data replication for partitioned tables failed when the table schema caching feature was enabled.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-13).

## April 29, 2026

Announcement

**Google Cloud's Agent for SAP version 3.13**

Version 3.13 of Google Cloud's Agent for SAP is generally available (GA). This version introduces minor bug fixes, enhancements for disk snapshot based recovery for SAP HANA, and security enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## April 20, 2026

Announcement

**Google SecOps for SAP is in Preview**

Google SecOps for SAP is in Preview. This service helps you secure your SAP applications by integrating business-critical telemetry into the Google Security Operations platform, providing unified visibility and AI-powered threat detection across your SAP landscape.

For more information, see [Google SecOps for SAP overview](https://docs.cloud.google.com/sap/docs/secops/overview).

## March 31, 2026

Announcement

**ABAP SDK for Google Cloud version 1.13 (On-premises or any cloud edition)**

Version 1.13 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). For the latest Gemini 3.1 Pro models, this version includes support for function calling with thought signatures and enhanced thinking configurations to optimize model reasoning.

Additionally, this version introduces support for the Parameter Manager API and fixes an issue with the `recordstamp` field in the BigQuery toolkit for SAP when multiple records with the same primary key are replicated to BigQuery.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-13).

## March 16, 2026

Announcement

**Google Cloud's Agent for SAP version 3.12**

Version 3.12 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements for SAP workload validation and disk snapshot based recovery for SAP HANA.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## March 10, 2026

Announcement

**Workload Manager observability service is generally available for SAP workloads**

The observability service of Workload Manager is generally available (GA). This service is a built-in monitoring solution for SAP workloads running on Google Cloud that helps you improve issue detection, root cause analysis, and troubleshooting.

For more information, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).

## February 27, 2026

Change

**SAP NetWeaver certification: CPU platform update for N2D machine types**

The CPU platform AMD EPYC Rome is no longer available for use with N2D machine types. The minimum CPU platform for N2D machine types is AMD EPYC Milan.

For more information about the N2D machine types that you can use to run SAP NetWeaver workloads on Google Cloud, see [N2D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n2d).

## February 18, 2026

Announcement

**New SAP HANA certifications for OLAP and OLTP workloads**

For use with SAP HANA, SAP has certified the following:

  * You can use the `m3-ultramem-128`, `m4-hypermem-64`, `x4-480-6t-metal`, `x4-480-8t-metal`, and `x4-960-12t-metal` machine types to run OLAP workloads in scale-out configurations with up to 8 nodes.
  * You can use the `x4-480-8t-metal` and `x4-960-12t-metal` machine types to run OLTP workloads in scale-out configurations with up to 4 nodes.



For more information, see [Certified Compute Engine machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#certified-vms).

## February 05, 2026

Announcement

**Google Cloud's Agent for SAP version 3.11**

Version 3.11 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements for optimizing performance of SAP HANA running on X4 instances, disk snapshot based backup and recovery for SAP HANA, and VM Extension Manager support to install and manage the agent on your VM fleet.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## January 22, 2026

Announcement

**BigQuery Connector for SAP version 2.12**

Version 2.12 of the BigQuery Connector for SAP is generally available (GA). This version offers file-based replication to Cloud Storage, table schema caching for streaming replication to BigQuery, and enhanced Unicode data handling.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-12).

## December 23, 2025

Change

**Updated IpAddr2 resource configuration for HA clusters**

To make the SAP HANA and SAP NetWeaver HA cluster configurations forward compatible with OS version updates, we recommend that you update the `IpAddr2` resource configuration to use `nic=lo` instead of `nic=eth0`.

For updated guidance, see the HA cluster configuration for your scenario:

  * [HA scale-up cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * [HA scale-up cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)
  * [HA scale-out cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-config-sles)
  * [HA scale-out cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-config-rhel)
  * [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles)
  * [HA cluster manual configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel)



## December 19, 2025

Announcement

**Introducing emergent host maintenance events for X4 instances running SAP HANA**

To perform non-critical hardware repairs that help in preventing host errors on X4 instances, we've introduced _emergent maintenance_ \- a new type of host maintenance event.

While this is a type of unplanned maintenance, it's similar in nature to a [planned host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) because of the following features:

  * It has a 14-day advance notification period.
  * You can manually trigger it, or let Google trigger it for you at the planned start date and time.



For more information, see [Manage host maintenance events for X4 instances running SAP HANA](https://docs.cloud.google.com/sap/docs/manage-maintenance-events-for-bare-metal-instances).

## December 12, 2025

Announcement

**New SAP certification: 6, 8, and 12 TB X4 machine types for SAP HANA scale-up workloads**

For use with SAP HANA scale-up (OLTP and OLAP) workloads running on Google Cloud, SAP has certified the following Compute Engine X4 machine types:

  * `x4-480-6t-metal` \- 6 TB memory
  * `x4-480-8t-metal` \- 8 TB memory
  * `x4-960-12t-metal` \- 12 TB memory



With this certification, the names of all X4 machine types have been updated to convey the memory they offer. For example, `x4-megamem-960-metal` is renamed to `x4-960-16t-metal` because it offers 16 TB memory. This change is backwards compatible.

For more information, see [X4 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-memory-optimized).

## December 05, 2025

Announcement

**New OS certification: Windows Server 2025 for SAP NetWeaver**

For use with SAP NetWeaver systems on Google Cloud, SAP has certified the operating system Windows Server 2025.

For more information, see [Certified SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-apps-on-gc).

## December 02, 2025

Announcement

**BigQuery Connector for SAP version 2.11**

Version 2.11 of the BigQuery Connector for SAP is generally available (GA). This version lets you set up JWT authentication by using project-specific service accounts for data replication to different Google Cloud projects.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-11).

## November 06, 2025

Feature

**Use of Oracle Automatic Storage Management with Oracle Database**

To run Oracle Database with SAP NetWeaver based applications on Google Cloud, SAP and Oracle have validated the use of Oracle Automatic Storage Management (ASM).

For more information, see the following:

  * [Plan Oracle Database implementation for SAP NetWeaver](https://cloud.google.com/sap/docs/oracle-planning)
  * [Deploy Oracle Database for SAP NetWeaver](https://cloud.google.com/sap/docs/oracle-deployment-single-node)



Announcement

**Guidance for RISE with SAP on Google Cloud**

Guidance is available to help you plan for running SAP solutions on Google Cloud that are managed by SAP under the RISE with SAP program. This guidance includes the following topics:

  * An overview about the architecture and involved components.
  * Establishing network connectivity to RISE with SAP on Google Cloud from on-premises systems and Google Cloud projects.
  * Building extensions for RISE with SAP on Google Cloud by using the ABAP SDK for Google Cloud.



For more information, see [Overview of RISE with SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/rise-overview).

## November 04, 2025

Announcement

**Google Cloud's Agent for SAP version 3.10**

Version 3.10 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements for SAP workload evaluations, and disk snapshot based backup and recovery for SAP HANA.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## October 08, 2025

Announcement

**ABAP SDK for Google Cloud version 1.12 (On-premises or any cloud edition)**

Version 1.12 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version lets you integrate Gemma models into your ABAP applications. In addition, the SDK improves your interaction with Gemini models by letting you control the randomness of the model's output and gain insight into the model's reasoning.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-12).

Announcement

**BigQuery Connector for SAP version 2.10**

Version 2.10 of the BigQuery Connector for SAP is generally available (GA). This version resolves the non-ASCII character handling issue in CDC replication through Pub/Sub and enhances server-side error handling.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-10).

## October 03, 2025

Announcement

**New SAP certification for operating system: RHEL for SAP 9.6**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 9.6.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## September 02, 2025

Deprecated

**Support for version 2 of Google Cloud's Agent for SAP has ended**

Support for version 2 of Google Cloud's Agent for SAP ended on July 31, 2025.

If you're using version 2 of the agent, then we strongly recommend that you update to using a supported version as soon as possible. For information about how to update the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

## August 27, 2025

Announcement

**New SAP certifications: Additional M4 memory-optimized machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the `m4-hypermem` Compute Engine memory-optimized machine types with 16, 32, and 64 vCPUs.

For more information, see:

  * [M4 memory-optimized machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#m4-memory-optimized)
  * [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)



## August 04, 2025

Announcement

**New SAP certifications: Additional C4 machine tpes**

SAP has certified the following Compute Engine C4 machine types with the Intel Granite Rapids CPU platform:

  * For use with SAP HANA scale-up (OLTP and OLAP): `c4-highmem-144`, `c4-highmem-288`, and `c4-highmem-288-metal`
  * For use with SAP NetWeaver: `c4-standard-144`, `c4-standard-288`, `c4-standard-288-metal`, `c4-highmem-144`, `c4-highmem-288`, and `c4-highmem-288-metal`



For more information, see the following:

  * [C4 general-purpose VM types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-c4)
  * [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)



## July 30, 2025

Announcement

**Google Cloud's Agent for SAP version 3.9**

Version 3.9 of Google Cloud's Agent for SAP is generally available (GA). This version introduces monitoring and supportability enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## July 28, 2025

Announcement

**New SAP NetWeaver certification: C4D bare metal machine types**

For use with SAP NetWeaver, SAP has certified the following Compute Engine bare metal machine types: `c4d-standard-384-metal` and `c4d-highmem-384-metal`.

For more information, see the following:

  * [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-c4d)
  * [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)



## July 18, 2025

Announcement

**New SAP certification for operating system: SLES 15 SP7 for SAP**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system SUSE Linux Enterprise Server (SLES) 15 SP7 for SAP.

For more information, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## July 08, 2025

Announcement

**BigQuery Connector for SAP version 2.9**

Version 2.9 of the BigQuery Connector for SAP is generally available (GA). This version introduces Change Data Capture (CDC) replication of SAP data into BigQuery through Pub/Sub. This replication path keeps your BigQuery tables up-to-date with the latest changes from your SAP data sources, eliminating the need for custom deduplication.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-9).

## July 03, 2025

Announcement

**ABAP SDK for Google Cloud version 1.11 (On-premises or any cloud edition)**

Version 1.11 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version introduces support for Anthropic Claude models through the Vertex AI SDK for ABAP, integration with the Model Armor API for LLM prompt security, and the WIF authentication validation feature. In addition, this version includes minor enhancements and bug fixes.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-11).

## June 13, 2025

Announcement

**New SAP NetWeaver certification: C4D series of general-purpose machine types**

For use with SAP NetWeaver, SAP has certified the Compute Engine general purpose machine types `c4d-standard` and `c4d-highmem`.

For more information, see [Certified C4D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-c4d).

## June 09, 2025

Announcement

**Google Cloud's Agent for SAP version 3.8**

Version 3.8 of Google Cloud's Agent for SAP is generally available (GA). This version introduces monitoring and supportability enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## April 25, 2025

Announcement

**New SAP certifications: Additional M4 memory-optimized machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the following Compute Engine M4 memory-optimized machine types: **372 GB** `m4-megamem-28` and **6 TB** `m4-ultramem-224`.

For more information, see:

  * For SAP HANA, [M4 memory-optimized VM types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#m4-memory-optimized)
  * For SAP NetWeaver, [M4 memory-optimized VM types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-mem-optimized-m4)



Announcement

**New SAP certification: 3 TB`m4-megamem-224` for SAP HANA scale-out workloads**

For use with SAP HANA scale-out (OLAP and OLTP) workloads, SAP has certified the **3 TB** `m4-megamem-224` memory-optimized machine type. For more information, see [M4 memory-optimized VM types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#m4-memory-optimized).

## April 14, 2025

Announcement

**ABAP SDK for Google Cloud version 1.10 (On-premises or any cloud edition)**

Version 1.10 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). In addition to offering expanded support for more than 294 Google Cloud APIs and few other enhancements, this version introduces the BigQuery AI and ML SDK for ABAP, Business Eventing Toolkit, and the ability to use Cloud Storage as content repository for SAP.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-10).

## April 11, 2025

Announcement

**Use of Oracle Linux images provided by Compute Engine with Oracle Database**

To run Oracle Database with SAP NetWeaver based applications on Google Cloud, SAP and Oracle have validated the use of the Oracle Linux images provided by Compute Engine.

For more information, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/oracle-planning#supported_operating_systems).

## April 01, 2025

Feature

**Terraform support for using NFS solutions with SAP HANA scale-out HA deployments**

While using Terraform to deploy an SAP HANA scale-out HA system on Google Cloud, you can use existing NFS solutions to share the `/hana/shared` and `/hanabackup` volumes with the worker hosts in your deployment:

  * For the `/hana/shared` volume, use the `primary_sap_hana_shared_nfs` and `secondary_sap_hana_shared_nfs` arguments.
  * For the `/hanabackup` volume, use the `primary_sap_hana_backup_nfs` and `secondary_sap_hana_backup_nfs` arguments.



These optional arguments are available from version 1.3.730053050 of the `sap_hana_ha` Terraform module provided by Google Cloud. For more information, see [Terraform: SAP HANA scale-out high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-ha-tf-deployment).

## March 14, 2025

Announcement

**New SAP certifications: M4 series of memory-optimized machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the Compute Engine memory-optimized M4 series machine types with the Intel Emerald Rapids CPU platform.

For more information, see:

  * For SAP HANA, [M4 memory-optimized VM types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#m4-memory-optimized)
  * For SAP NetWeaver, [M4 memory-optimized VM types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-mem-optimized-m4)



## March 05, 2025

Announcement

**Google Cloud's Agent for SAP version 3.7**

Version 3.7 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the following:

  * Support for the disk snapshot based backup and recovery of SAP HANA scale-out systems, except those with the host auto-failover solution.
  * Enhancements for Backint based backup and recovery of SAP HANA.
  * Enhancements for evaluating Pacemaker configurations by using Workload Manager.
  * Support for showing annotations for SAP events in Cloud Monitoring and predefined observability dashboards.
  * Support to validate the Google Cloud setup for using the agent features.
  * Automatic polling of agent configuration, negating the need to restart the agent after you change its configuration.



For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## January 31, 2025

Announcement

**New certification: Oracle Database with Oracle Linux for SAP NetWeaver**

For SAP NetWeaver based applications running on Google Cloud, SAP and Oracle have certified the use of single-node instances of Oracle Database 19c or later with UEK-enabled Oracle Linux 8 or 9.

While using an Oracle Database, all components of your SAP system must use the same version of Oracle Linux. This includes the database, app servers, and any other closely coupled auxiliary system. 

For more information, see the following:

  * [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning)
  * [Deploy Oracle Database for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node)



## January 27, 2025

Announcement

**ABAP SDK for Google Cloud version 1.9 (On-premises or any cloud edition)**

Version 1.9 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). In addition to supporting more Google Cloud APIs and few other enhancements, this version introduces the BigQuery Toolkit for SAP – a dedicated tool to replicate data to BigQuery from within your SAP environment using ABAP.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-9).

## January 26, 2025

Feature

**SAP HANA: support for deploying HA clusters with the`SAPHanaSR-angi` package**

To enable you to use the `SAPHanaSR` Advanced Next Generation Interface (`SAPHanaSR-angi`) package with your SAP HANA HA clusters on SLES 15 SP6 for SAP, or later, we've done the following:

  * Updated our manual deployment guides. For more information, see the following: 
    * [HA scale-up cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)
    * [HA scale-up cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-config-sles)
  * If you use the latest version (1.3.730053050) of our `sap_hana_ha` Terraform module to deploy SAP HANA scale-up HA on SLES 15 SP6 for SAP, or later, then the `SAPHanaSR-angi` package is automatically installed and configured. For more information, see [Terraform: SAP HANA scale-up high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment).



## January 15, 2025

Feature

**Terraform support for deploying sole-tenant nodes for SAP HANA**

You can use Terraform to deploy the following systems with sole-tenant nodes:

  * SAP HANA scale-up
  * SAP HANA scale-up high availability
  * SAP HANA multi-host scale-out without node anti-affinity
  * SAP HANA scale-out high availability without node anti-affinity



For more information, see [Sole tenancy](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-sole-tenancy).

## January 01, 2025

Change

**SAP HANA on RHEL: configuration updated for the`chkSrv.py` HA/DR provider hook**

Aligning with the recommendation from Red Hat, the Google Cloud guidance for configuring the [`chkSrv.py`](http://chkSrv.py) SAP HANA HA/DR provider hook has been updated.

If you use the latest version (1.3.730053050) of our `sap_hana_ha` Terraform module, then the `chkSrv.py` hook is automatically installed with the updated configuration.

For more information, see the following guides:

  * [HA scale-up cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable-hana-hadr-provider-hook)
  * [Terraform: SAP HANA scale-up high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)



## December 30, 2024

Announcement

**ABAP SDK for Google Cloud version 1.1 (SAP BTP edition)**

Version 1.1 of the SAP BTP edition of the ABAP SDK for Google Cloud is generally available (GA). In addition to supporting more Google Cloud APIs and few other enhancements, this version introduces the Vertex AI SDK for ABAP – a dedicated toolset for seamless interaction with Google Cloud's Vertex AI platform from your SAP BTP, ABAP environment.

For more information, see [What's new with the SAP BTP edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new).

## December 09, 2024

Announcement

**New SAP HANA certification: 24 TB and 32TB X4 bare metal machine types for OLAP workloads**

SAP has certified the Compute Engine `x4-megamem-1440-metal` and `x4-megamem-1920-metal` machine types for use with SAP HANA OLAP workloads in scale-out configurations with up to 8 nodes.

For more information, see [X4 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-memory-optimized).

## October 29, 2024

Announcement

**BigQuery Connector for SAP version 2.8**

Version 2.8 of the BigQuery Connector for SAP is generally available (GA). This version offers several enhancements and bug fixes, including the record compression option at field level, a transaction to view the version of BigQuery Connector for SAP, and an enhancement spot for HTTP error handling.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new).

## October 22, 2024

Feature

**SAP NetWeaver: Support for deploying HA cluster that uses the Simple Mount architecture**

To enable you to deploy SAP NetWeaver Central Services (ASCS) with a high availability cluster that uses the Simple Mount architecture, we've done the following:

  * Updated our manual deployment guide. For more information, see [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles).
  * If you use the latest version (1.3.730053050) of our `sap_nw_ha` Terraform module to deploy SAP NetWeaver HA on SLES 15 for SAP or later, then the Simple Mount architecture is automatically deployed. For more information, see [Terraform: HA cluster configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf).



## October 14, 2024

Announcement

**New SAP certification for operating system: SLES 15 SP6 for SAP**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system SUSE Linux Enterprise Server (SLES) 15 SP6 for SAP.

For more information, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## October 09, 2024

Feature

**SAP HANA: support for deploying striped disk to host the data directory**

To enable you to deploy striped disks for hosting the `/hana/data` directory, we have done the following:

  * Updated our documentation with the minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes.

For more information, see [Minimum sizes for SSD-based persistent disks and Hyperdisks](https://cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced) in the SAP HANA planning guide.

  * Introduced deployment automation support through the `enable_data_striping` Terraform argument. You can use this argument to provision a striped disk to host the `/hana/data` directory while deploying SAP HANA scale-up, scale-up HA, and scale-out HA systems with Terraform.

This argument is available from version `1.3.674800406` of the Terraform modules `sap_hana` and `sap_hana_ha`, provided by Google Cloud. For more information, see the deployment guide for your [SAP HANA scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).




Announcement

**Google Cloud's Agent for SAP version 3.6**

Version 3.6 of Google Cloud's Agent for SAP is generally available (GA). This version introduces striped disk support for SAP HANA backup and recovery by using the disk snapshot feature, metric enhancements for monitoring SAP HANA, and other minor enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## September 23, 2024

Announcement

**New SAP HANA certifications: X4 bare metal machine types for OLTP workloads**

SAP has certified the Compute Engine bare metal machine types `x4-megamem-960-metal`, `x4-megamem-1440-metal`, and `x4-megamem-1920-metal`, for use with SAP HANA OLTP workloads in scale-out configurations with up to 4 nodes.

For more information, see [X4 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-memory-optimized).

Announcement

**Google Cloud storage manager for SAP HANA standby nodes version 2.8**

Version 2.8 of the Google Cloud storage manager for SAP HANA standby nodes is generally available (GA). This version includes bug fixes and supportability improvements.

For more information about the storage manager, see [Storage Manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

## September 13, 2024

Deprecated

**Support for version 1 of Google Cloud's Agent for SAP has ended**

Version 1 of Google Cloud's Agent for SAP has reached the end of support.

If you're using version 1 of the agent, then we strongly recommend that you update to using a supported version as soon as possible. For information about supported versions, see [Supported versions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-on-gc-versions#agent4sap). For information about how to update to a supported version of the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

## September 10, 2024

Announcement

**New SAP certification for operating system**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 8.10.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## September 09, 2024

Announcement

**ABAP SDK for Google Cloud version 1.8 (On-premises or any cloud edition)**

Version 1.8 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version introduces the Vertex AI SDK for ABAP, a dedicated toolset for seamless interaction with Google Cloud's Vertex AI platform from SAP environment.

The SDK lets you build AI-powered enterprise features and applications with reduced complexity and development efforts from within your SAP systems.

For more information, see:

  * [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new)
  * [Overview of the Vertex AI SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview)



## August 16, 2024

Announcement

**New SAP certifications: C4 series of general-purpose machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the Compute Engine C4 series of general-purpose machine types.

For more information, see the following:

  * [C4 general-purpose VM types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-c4), for SAP HANA.
  * [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)



## August 15, 2024

Announcement

**Google Cloud's Agent for SAP version 3.5**

Version 3.5 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements to support Workload Manager's observability service for SAP, metric enhancements, and some minor fixes.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## July 18, 2024

Announcement

**New SAP certifications: C3 bare metal machine types**

SAP has certified the following Compute Engine bare metal machine types:

  * `c3-highmem-192-metal` for use with SAP HANA OLAP and OLTP workloads.
  * `c3-standard-192-metal` and `c3-highmem-192-metal` for use with SAP NetWeaver workloads.



For more information, see the following:

  * [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana)
  * [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-c3)
  * [C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)



## July 16, 2024

Announcement

**New SAP certification for operating systems**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 9.4.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## July 08, 2024

Announcement

**New SAP HANA certification: 16 TB X4 bare metal machine type for OLAP workloads**

SAP has certified the Compute Engine 16 TB `x4-megamem-960-metal` machine type for use with SAP HANA OLAP workloads in scale-out configurations with up to 8 nodes.

For more information, see [X4 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-memory-optimized).

## June 27, 2024

Announcement

**New SAP certification: 16 TB X4 bare metal machine type**

The Compute Engine memory-optimized bare metal machine type `x4-megamem-960-metal` is generally available (GA) and certified by SAP for use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads.

For more information, see:

  * [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana)
  * [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)



Announcement

**Google Cloud's Agent for SAP version 3.4**

Version 3.4 of Google Cloud's Agent for SAP is generally available (GA). This version introduces a workload performance diagnostic tool, and enhancements to the Backint and disk snapshot features.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## June 03, 2024

Announcement

**New SAP certifications: X4 series of memory-optimized bare metal machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the following Compute Engine memory-optimized bare metal machine types: `x4-megamem-1440-metal` and `x4-megamem-1920-metal`.

For more information, see:

  * [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana)
  * [Certified machine types for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)
  * [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series)



## May 27, 2024

Announcement

**ABAP SDK for Google Cloud version 1.7 (On-premises or any cloud edition)**

Version 1.7 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version brings in expanded support for more Google Cloud APIs, authentication improvements for Cloud Functions, SDK feature enhancements, and bug fixes.

For more information, see [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/whats-new).

## May 23, 2024

Announcement

**Google Cloud's Agent for SAP version 3.3**

Version 3.3 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements to back up SAP HANA while using the agent's Backint and disk snapshot features. It also introduces support for using `hdbuserstore` keys to authenticate SAP HANA users.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## May 22, 2024

Announcement

**Google Cloud storage manager for SAP HANA standby nodes version 2.7**

Version 2.7 of the Google Cloud storage manager for SAP HANA standby nodes is generally available (GA). This version includes bug fixes and supportability improvements.

For more information about the storage manager, see [Storage Manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

## May 10, 2024

Announcement

**New SAP HANA certification: Hyperdisk Balanced usage with M1 machine types**

For use with SAP HANA on Google Cloud, SAP has certified the usage of Hyperdisk Balanced with the M1 series of memory-optimized machine types.

For more information, see:

  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms)
  * The "Hyperdisk Balanced" tab in [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)



## April 17, 2024

Announcement

**BigQuery Connector for SAP version v2.7**

Version 2.7 of the BigQuery Connector for SAP is generally available (GA). This version extends support for using the SAP SLT add-on DMIS 2018 SP 11.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new).

## April 16, 2024

Announcement

**New SAP HANA certification: Hyperdisk Balanced usage with M2 machine types**

For use with SAP HANA on Google Cloud, SAP has certified the usage of Hyperdisk Balanced with the M2 series of memory-optimized machine types.

For more information, see:

  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms)
  * The "Hyperdisk Balanced" tab in [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)



## April 05, 2024

Announcement

**SAP BTP edition of the ABAP SDK for Google Cloud**

Version 1.0 of the SAP BTP edition of ABAP SDK for Google Cloud is generally available (GA). With the BTP edition of the SDK, developers can create innovative solutions using Google Cloud APIs in their SAP BTP, ABAP environment.

For more information, see:

  * [What's new with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/whats-new)
  * [Overview of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview).



## April 03, 2024

Announcement

**BigQuery Connector for SAP version v2.6**

Version 2.6 of the BigQuery Connector for SAP is generally available (GA). This version offers several enhancements and bug fixes, including the addition of the Create Table tool, the Mass Field Conversion tool, a custom transaction designed to only display the BigQuery Connector for SAP settings, and support for replicating cluster tables to BigQuery.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new).

## April 02, 2024

Announcement

**ABAP SDK for Google Cloud version 1.6 (On-premises or any cloud edition)**

Version 1.6 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version brings in expanded support for more Google Cloud APIs, including support for multi-modal LLMs such as Gemini, SDK feature enhancements, and bug fixes.

For more information, see [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/whats-new).

## April 01, 2024

Announcement

**Google Cloud's Agent for SAP version 3.2**

Version 3.2 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the default collection of Workload Manager evaluation metrics for new agent installations, configuration commands for updating the agent configuration, and enhancements to the Backint, disk snapshot, and Process Monitoring features.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## March 11, 2024

Announcement

**New SAP HANA certification: Hyperdisk Balanced usage with C3 machine types**

For use with SAP HANA on Google Cloud, SAP has certified using Hyperdisk Balanced with `c3-standard-44`, and `c3-highmem` machine types with 44 vCPUs or more.

For more information, see:

  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms)
  * The "Hyperdisk Balanced" tab in [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)



## March 06, 2024

Announcement

**Generally available: Guided Deployment Automation in Workload Manager for SAP**

The Guided Deployment Automation tool in Workload Manager is generally available (GA). You can use this tool to configure and deploy supported SAP workloads directly from the Google Cloud console, or choose to generate and download the equivalent Terraform and Ansible code.

The GA launch adds support for custom OS images, Shared VPC configurations, and increased deployment customization.

For more information, see [About Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).

## February 28, 2024

Feature

**Disk snapshot based backup and recovery for SAP HANA**

From version 3.0, you can use the disk snapshot feature of Google Cloud's Agent for SAP to perform backup and recovery operations for SAP HANA systems running on Google Cloud.

For more information, see [Disk snapshot based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).

## February 14, 2024

Announcement

**Google Cloud's Agent for SAP version 3.1**

Version 3.1 of Google Cloud's Agent for SAP is generally available (GA). This version introduces enhancements for discovering SAP system information and for the Backint feature of the agent.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## January 29, 2024

Announcement

**New SAP HANA certification: Hyperdisk Balanced usage with M3 machine types**

For running SAP HANA on Google Cloud, SAP has certified using Hyperdisk Balanced with M3 machine types.

For more information, see:

  * [About Hyperdisks](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms)
  * The Hyperdisk Balanced sizes tab in [Minimum sizes for SSD-based persistent disks and Hyperdisks](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)



## January 11, 2024

Deprecated

The Cloud Storage Backint agent for SAP HANA is deprecated, and is replaced by the _Backint_ feature of version 3.0 of Google Cloud's Agent for SAP. For upgrade instructions, see [Google Cloud's Agent for SAP operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade-to-agent4sap).

Support for the Cloud Storage Backint agent for SAP HANA ends on February 28, 2025.

Announcement

**Google Cloud's Agent for SAP version 3.0**

Version 3.0 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the following:

  * The optional feature – _Backint based backup and recovery for SAP HANA_. Once you enable this feature, the agent becomes the successor to the Cloud Storage Backint agent for SAP HANA.
  * Improvement for the collection of Workload Manager evaluation metrics.



For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.33**

Version 1.0.33 of the Cloud Storage Backint agent for SAP HANA is available. This version adds a message to the installation and update process that users should upgrade to the Agent for SAP.

For upgrade instructions, see [Google Cloud's Agent for SAP operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade-to-agent4sap).

## December 19, 2023

Announcement

**New SAP certification for operating systems**

For use with SAP HANA on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 9.2.

For more information about SAP-certified operating systems, see [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table).

## November 27, 2023

Announcement

**Google Cloud's Agent for SAP version 2.8**

Version 2.8 of Google Cloud's Agent for SAP is generally available (GA). From this version, the agent additionally collects the SAP Host Agent metrics `Guaranteed IOPS` and `Guaranteed Throughput` for Google Cloud Hyperdisk volumes.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## November 20, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.32**

Version 1.0.32 of the Cloud Storage Backint agent for SAP HANA is available. This version updates the JRE to the latest SAP JRE 21.0.1.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 13, 2023

Announcement

**Google Cloud's Agent for SAP version 2.7**

Version 2.7 of Google Cloud's Agent for SAP is generally available (GA). This version fixes the handling of SAP HANA database passwords that contain special characters, and introduces Process Monitoring metrics related to TCP network.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## October 30, 2023

Announcement

**Google Cloud storage manager for SAP HANA standby nodes version 2.6**

Version 2.6 of the Google Cloud storage manager for SAP HANA standby nodes is generally available (GA). This version includes bug fixes and supportability improvements.

For more information about the storage manager, see [Storage Manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

## October 25, 2023

Fixed

**Cloud Storage Backint agent for SAP HANA version 1.0.31**

Version 1.0.31 of the Cloud Storage Backint agent for SAP HANA is available. This version fixes client libraries to enable Cloud Logging capabilities.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## October 18, 2023

Announcement

**New SAP NetWeaver certification: C3D series of general-purpose machine types**

For use with SAP NetWeaver, SAP has certified the Compute Engine general-purpose machine types `c3d-standard` and `c3d-highmem`.

For more information, see [Certified C3D machine types for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-general-purpose-c3d).

## October 12, 2023

Fixed

**Cloud Storage Backint agent for SAP HANA version 1.0.30**

Version 1.0.30 of the Cloud Storage Backint agent for SAP HANA is available. This version reverts the `google-cloud-storage` client library to an earlier version so that API call retries work correctly.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## October 04, 2023

Announcement

**ABAP SDK for Google Cloud version 1.5 (On-premises or any cloud edition)**

Version 1.5 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version of the SDK offers extended ABAP client libraries to build and deploy ML and AI-driven solutions using a wide range of Google Cloud services. 

This SDK also enables use of the OAuth 2.0 framework to authenticate to Google Cloud APIs using OAuth 2.0 client credentials.

For more information, see [What's new with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/whats-new).

## October 02, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.29**

Version 1.0.29 of the Cloud Storage Backint agent for SAP HANA is available. This version sets the default value of the `HTTP_READ_TIMEOUT` parameter to `-1`; no timeout.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## September 28, 2023

Feature

**SAP HANA Fast Restart enabled using Terraform**

SAP HANA Fast Restart is enabled when you deploy SAP HANA on Google Cloud using the `sap_hana` or `sap_hana_ha` Terraform module, version `202309280828` or later. The fast restart option is enabled through the `enable_fast_restart` Terraform argument, which by default is set to `true`.

For more information, see the deployment guide for your [SAP HANA scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).

## September 21, 2023

Announcement

**Google Cloud's Agent for SAP version 2.6**

Version 2.6 of Google Cloud's Agent for SAP is generally available (GA). This version introduces new options to configure the collection of Process monitoring metrics, and bug fixes for the collection of Workload Manager evaluation metrics.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## September 11, 2023

Announcement

**New SAP HANA certification: Hyperdisk Extreme usage with N2 machine types**

For running SAP HANA on Google Cloud, SAP has certified using Hyperdisk Extreme with N2 machine types that have 80 vCPUs or more.

For more information, see:

  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms)
  * The Hyperdisk Extreme sizes tab in [Minimum sizes for SSD-based persistent disks and Hyperdisks](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced)



Announcement

**New OS certifications for SAP HANA**

For use with SAP HANA on Google Cloud, SAP has certified the following operating systems:

  * Red Hat Enterprise Linux (RHEL) 8.8 for SAP
  * SUSE Linux Enterprise Server (SLES) 15 SP5 for SAP



For more information, see [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table).

## September 06, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.28**

Version 1.0.28 of the Cloud Storage Backint agent for SAP HANA is available. This version includes a new `HTTP_READ_TIMEOUT` parameter.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## August 18, 2023

Announcement

**New SAP NetWeaver certification: N1 machine types on the Intel Skylake platform**

For use with SAP NetWeaver, SAP has certified the Compute Engine N1 machine types that have 64 vCPUs or lower, with the Intel Skylake CPU platform.

For more information, see [N1 general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n1).

## August 16, 2023

Feature

**PD Async Replication support**

For cross-region active-passive disaster recovery for SAP HANA and SAP NetWeaver, [Persistent Disk Asynchronous Replication (PD Async Replication)](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) is supported. You can use PD Async Replication with balanced persistent disks and SSD persistent disks up to a maximum size of 2 TB per volume in supported region pairs.

For more information, see: 

  * SAP HANA: [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage)
  * SAP NetWeaver: [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage)



## August 14, 2023

Announcement

**Google Cloud's Agent for SAP version 2.5**

Version 2.5 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the collection of SAP HANA database metrics for Workload Manager evaluation and includes bug fixes for the collection of Process monitoring metrics.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## August 09, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.27**

Version 1.0.27 of the Cloud Storage Backint agent for SAP HANA is available. This version includes updated libraries.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## August 07, 2023

Announcement

**Google Cloud's Agent for SAP version 2.4**

Version 2.4 of Google Cloud's Agent for SAP is generally available (GA). This version includes bug fixes for the collection of Workload Manager Corosync evaluation metrics.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## August 02, 2023

Announcement

**New SAP HANA certifications: C3 series of general-purpose machine types**

For running SAP HANA OLAP and OLTP scale-up workloads, SAP has certified the Compute Engine general-purpose machine types `c3-standard` and `c3-highmem`.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms).

Announcement

**New SAP NetWeaver certifications: C3 series of general-purpose machine types**

For use with SAP NetWeaver, SAP has certified the Compute Engine general-purpose machine types `c3-standard` and `c3-highmem`.

For more information, see [Certified C3 machine types for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#nw-c3-certs).

## July 27, 2023

Announcement

**Terraform support for deploying SAP HANA scale-out HA cluster on SLES**

You can use Terraform to automate the deployment of an SAP HANA scale-out system in a SUSE Linux Enterprise Server (SLES) high-availability cluster on Google Cloud.

For more information, see [Terraform: SAP HANA scale-out high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-ha-tf-deployment).

## July 21, 2023

Announcement

**Google Cloud's Agent for SAP version 2.3**

Version 2.3 of Google Cloud's Agent for SAP is generally available (GA). This version includes bug fixes for SAP system discovery sending data to Cloud Logging.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## July 17, 2023

Announcement

**Google Cloud's Agent for SAP version 2.1**

Version 2.1 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the SAP system discovery and support bundle collection features, and includes bug fixes.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## July 14, 2023

Feature

**Google Cloud's Agent for SAP is packaged with "for SAP" OS images**

Google Cloud's Agent for SAP is packaged with the following "for SAP" OS images provided by Google Cloud:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



For information about the operating systems supported by Google Cloud's Agent for SAP, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems).

## July 11, 2023

Announcement

**Preview: Guided Deployment Automation in Workload Manager for SAP**

The preview release of the Guided Deployment Automation tool in Workload Manager is available. You can use this tool to configure and deploy SAP systems on Google Cloud.

The preview release includes initial support for the deployment of SAP S/4HANA in the distributed and distributed with high availability (HA) architectures.

For more information, see [About Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).

## July 06, 2023

Announcement

**Backup disk updates for SAP HANA deployment automation**

While automating the deployment of SAP HANA scale-up systems on Google Cloud using Terraform, the following updates are available for hosting the `/hanabackup` volume on a disk:

  * You can use the `backup_disk_type` argument to specify the type of Persistent Disk or Hyperdisk that must be deployed.
  * For compatibility across all machine families, the default disk type has been changed from Standard HDD Persistent Disk to Balanced Persistent Disk.



These updates are available when you use the `sap_hana` and `sap_hana_ha` Terraform modules, version `202307061058` or later, provided by Google Cloud.

For more information, see the deployment guide for your [SAP HANA scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).

## June 26, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.26**

Version 1.0.26 of the Cloud Storage Backint agent for SAP HANA is available. This version includes updated libraries and bug fixes.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## June 12, 2023

Feature

**IP address support for SAP HANA deployment automation**

You can assign static IP addresses to your VM instances while automating the deployment of SAP HANA on Google Cloud using the following Terraform arguments:

  * `vm_static_ip`, `worker_static_ips`, and `standby_static_ips` represent the master, worker, and standby nodes in a scale-out system.
  * `primary_static_ip` and `secondary_static_ip` represent the primary and secondary instances in a scale-up system.



These arguments are available when you use the Terraform module version 202306120959 or later, provided by Google Cloud.

For more information, see the deployment guide for your [SAP HANA scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).

## June 05, 2023

Announcement

**Google Cloud's Agent for SAP version 2.0**

Version 2.0 of Google Cloud's Agent for SAP is generally available (GA). This version introduces the opt-in feature of collecting SAP HANA monitoring metrics, making Google Cloud's Agent for SAP version 2.0 the successor to Google Cloud's monitoring agent for SAP HANA.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

Deprecated

Google Cloud's monitoring agent for SAP HANA is deprecated, and is replaced by the _SAP HANA monitoring metrics collection_ feature of version 2.0 of Google Cloud's Agent for SAP. For upgrade instructions, see [Google Cloud's Agent for SAP operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade-to-agent4sap).

Support for the monitoring agent for SAP HANA ends on May 31, 2024.

## May 17, 2023

Announcement

**Google Cloud's Agent for SAP version 1.6**

Version 1.6 of Google Cloud's Agent for SAP is available. This version includes bug fixes for Process Monitoring metrics collection and agent instances running on Bare Metal Solution servers.

For more information, see [What's new with Google Cloud's Agent for SAP](https://cloud.google.com/sap/docs/agent-for-sap/whats-new).

## May 12, 2023

Announcement

**ABAP SDK for Google Cloud, version 1.0 is generally available (GA)**

Version 1.0 of the ABAP SDK for Google Cloud is generally available (GA). The ABAP SDK for Google Cloud enables native, bi-directional, and real-time integration between SAP applications and Google Cloud services such as Google Cloud Storage, Vertex AI, Maps, and Pub/Sub.

Using the ABAP SDK for Google Cloud, ABAP developers can build and deploy ML and AI-driven solutions based on Google Cloud services driven by real-time changes in their SAP enterprise applications. 

For more information, see [What's new with the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/whats-new).

Announcement

**Compliance and sovereign controls for SAP on Google Cloud**

SAP workloads can leverage Assured Workloads to meet compliance and sovereign control requirements such as data residency, access control, support personnel, or other regulatory requirements.

For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls).

## May 03, 2023

Announcement

**Google Cloud's Agent for SAP version 1.5**

Version 1.5 of Google Cloud's Agent for SAP is available. This version includes bug fixes for agent instances running on Linux machines.

For more information, see [What's new with Google Cloud's Agent for SAP](https://cloud.google.com/sap/docs/agent-for-sap/whats-new).

## April 26, 2023

Announcement

**Google Cloud's Agent for SAP version 1.4**

Version 1.4 of Google Cloud's Agent for SAP is available. This version includes bug fixes for Workload Manager evaluation and Process Monitoring metrics. This version also prevents changes in the Agent configuration file from being overwritten during updates.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## April 19, 2023

Announcement

**Google Cloud's Agent for SAP version 1.3**

Version 1.3 of Google Cloud's Agent for SAP is now available. This version includes bug fixes for Workload Manager evaluation and Process Monitoring metrics. This version also redirects the agent's logs to Cloud Logging by default.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## April 11, 2023

Announcement

**Workload Manager is now generally available (GA) for evaluating SAP workloads**

Workload Manager is a rule-based, cross-project validation service for evaluating workloads running on Google Cloud. 

You can use Workload Manager to evaluate your SAP HANA and SAP NetWeaver workloads, and detect deviations from key best practices that SAP, OS vendors, and Google Cloud prescribe. This helps you improve the quality, reliability, and performance of your SAP workloads.

The set of rules provided will continue to evolve to cover new machine types and storage options as they become available, and extend SAP HANA and SAP NetWeaver best practices as relevant for your SAP workloads.

For information about the best practices that Workload Manager supports for evaluating SAP workloads, see [Best practices for SAP workloads](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices#sap_workloads).

## April 10, 2023

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.25**

Version 1.0.25 of the Cloud Storage Backint agent for SAP HANA is available. This version includes logging enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

Change

**Update from Red Hat for ASCS/ERS order constraints in ENSA2 and ENSA1**

According to Red Hat's recently updated guidance for SAP NetWeaver high-availability clusters on RHEL, you now only need to use one order constraint to start the ASCS resource group and stop the ERS resource group. This applies to both ENSA2 and ENSA1 architectures.

Google Cloud recommends that you update your SAP NetWeaver systems to use a single order constraint at your earliest convenience to comply with Red Hat's recommendation. To align with this update, Google Cloud has revised its guidance to [configure the location and ordering constraints](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#configure_the_location_and_ordering_constraints) for SAP NetWeaver high-availability clusters on RHEL.

For more information from Red Hat, see:

  * [Configuring SAP S/4HANA ASCS/ERS with Standalone Enqueue Server 2 (ENSA2) in Pacemaker](https://access.redhat.com/articles/3974941)
  * [Configuring SAP NetWeaver ASCS/ERS ENSA1 with Standalone Resources in RHEL 7.5+ and RHEL 8](https://access.redhat.com/articles/3569681)



## April 06, 2023

Announcement

**New SAP certification for operating systems**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 9.0.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## March 28, 2023

Change

**Update from SUSE for the Python hook scripts in SAPHanaSR**

According to SUSE's recently updated guidance, all Python hook scripts should be used directly from the SAPHanaSR package. If the scripts are moved or copied to another directory, then the regular SUSE package update will not keep those copies updated.

To align with this update from SUSE, make sure to use the scripts directly from the SAPHanaSR package location. Also, Google Cloud has done the following:

  * Published the Terraform module version 202303280902 and Deployment Manager template version 202303280902, which use the hook scripts directly from the SAPHanaSR package.
  * Updated the guidance to [enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable-hana-hadr-provider-hook) in the manual SAP HANA HA deployment guide for SLES.



For information from SUSE, see [Setting up HANA HA/DR providers](https://documentation.suse.com/sbp/all/single-html/SLES4SAP-hana-sr-guide-PerfOpt-15/#cha.s4s.hana-hook).

## March 27, 2023

Announcement

**Google Cloud's Agent for SAP version 1.2**

Version 1.2 of Google Cloud's Agent for SAP is available. This version includes bug fixes and supportability enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

## March 13, 2023

Announcement

**New SAP HANA certification: Hyperdisk Extreme**

For use with SAP HANA, SAP has certified the Compute Engine disk — Hyperdisk Extreme.

Hyperdisks provide the fastest block storage for Compute Engine for your high-end, memory-intensive SAP HANA workloads. Hyperdisks are durable network storage devices that your VMs can access, similar to persistent disks. For more information, see:

  * [About Hyperdisks](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * [Disk storage for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage)



Change

**SAP HANA: minimum sizes for persistent disks reduced**

[Baseline performance](https://docs.cloud.google.com/compute/docs/disks/performance#baseline_performance) improvements for PD-SSD and PD-Balanced have allowed us to reduce the minimum PD size required for most Compute Engine VM types running SAP HANA. This enables you to optimize your SAP HANA workloads by reducing costs and releasing quota related to disk storage.

We have also updated our Terraform configurations for SAP HANA to use the reduced sizes.

For more information, see [Minimum sizes for SSD-based persistent disks and Hyperdisks](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced) in the SAP HANA planning guide.

Announcement

**Google Cloud's Agent for SAP version 1.1**

Version 1.1 of Google Cloud's agent for SAP is available. This version includes bug fixes and supportability improvements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

Feature

**Disk related enhancements for automating SAP HANA deployments with Terraform**

The Terraform configurations that Google Cloud provides for automating SAP HANA deployments support the following disk related enhancements:

  * Using the argument `disk_type`, you can now specify the default disk type that you want to deploy for your SAP volumes. This argument also supports Hyperdisk Extreme.
  * By default, all SAP volumes are now mounted on separate SSD-based persistent disks or Hyperdisks. Using the argument `use_single_shared_data_log_disk`, you can specify if you want to mount all SAP volumes on a single disk.
  * For scale-up deployments, using the argument `include_backup_disk`, you can now specify if you want to deploy a disk for the SAP HANA backup volume.



These enhancements are available when you automate the deployment of SAP HANA on Google Cloud with Terraform configurations that use the module version 202303130717 or later.

For more information, see the [deployment guide](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions) for your scenario.

## February 14, 2023

Announcement

**Google Cloud's Agent for SAP is generally available (GA)**

To simplify agent installation and operation, while also enabling access to new products, Google Cloud's Agent for SAP v1.0 combines Google Cloud's monitoring agent for SAP NetWeaver with new Process Monitoring and Workload Manager Evaluation functionalities.

In addition to collecting and sending information required by SAP to the SAP Host Agent, on Linux, now you can opt in and enable other functionalities, all built into the same agent. The new optional functionalities include collection of Process Monitoring metrics, such as high-availability cluster status and information, and collection of Workload Manager Evaluation metrics, a way to automatically evaluate your workloads against best practices. 

For more information, see [What's new with Google Cloud's Agent for SAP](https://cloud.google.com/sap/docs/agent-for-sap/whats-new).

Deprecated

Google Cloud's monitoring agent for SAP NetWeaver is deprecated, and is replaced by Google Cloud's Agent for SAP. For information about new installations or how you can upgrade, see [Google Cloud's Agent for SAP operations guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade-to-agent4sap).

Support for the monitoring agent for SAP NetWeaver ends on February 14, 2024.

## February 06, 2023

Feature

**Network interface support for automating SAP HANA deployments**

You can now specify if you want to use Google Virtual NIC (gVNIC) with your VM instance using the new argument `nic_type`. This argument is available when you automate the deployment of SAP HANA on Google Cloud using the following files:

  * Terraform configurations using the module version 202302060649 or later
  * Deployment Manager template versions 202302060649 or later



For more information, see the deployment guide for your SAP HANA scenario:

  * [Automating SAP deployments on Google Cloud with Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap)
  * [Automating SAP deployments on Google Cloud with Deployment Manager](https://docs.cloud.google.com/sap/docs/dm-templates-for-sap)



## January 09, 2023

Announcement

**Google Cloud's monitoring agent for SAP NetWeaver version 2.8**

Version 2.8 of Google Cloud's monitoring agent for SAP NetWeaver is available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Google Cloud's monitoring agent for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

## December 15, 2022

Announcement

**Enhancements to Bare Metal Solution resource management for SAP HANA**

For Bare Metal Solution environments running SAP HANA, you can now view and manage your Bare Metal Solution servers, storage, and networks using the Google Cloud console, CLI, and API.

For more information, see [Maintaining your Bare Metal Solution environment](https://docs.cloud.google.com/sap/docs/sap-hana-on-bms-deployment#maintain_bms_environment) in the SAP HANA on Bare Metal Solution deployment guide.

## December 14, 2022

Change

**Cloud Storage Backint agent for SAP HANA version 1.0.24**

Version 1.0.24 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes logging enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 30, 2022

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.23**

Version 1.0.23 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes stability enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 22, 2022

Announcement

**Terraform configurations for SAP deployments on Google Cloud**

Terraform configurations to automate the deployment of resources for running the following databases on Google Cloud are now generally available (GA):

  * [IBM Db2 for SAP on Linux](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf)
  * [SAP ASE on Linux](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux-tf)



For more information, see [Automating SAP deployments on Google Cloud with Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap).

## November 21, 2022

Announcement

**Google Cloud monitoring agent for SAP NetWeaver version 2.7**

Version 2.7 of the Google Cloud monitoring agent for SAP NetWeaver is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

Change

**Cloud Storage Backint agent for SAP HANA version 1.0.22**

Version 1.0.22 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes enhanced validations for backint configuration and backup stability.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 07, 2022

Announcement

**New SAP certifications: M3 series of memory-optimized machine types**

For use with SAP HANA and SAP NetWeaver, SAP has now certified the Compute Engine memory-optimized M3 series machine types.

For more information, see:

  * [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#m3-memory-optimized)
  * [M3 memory-optimized machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-m3)



## October 25, 2022

Announcement

**New SAP certification for operating systems**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has now certified the operating system SUSE Linux Enterprise Server (SLES) for SAP 15 SP4 .

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



## October 04, 2022

Announcement

**Monitoring agent for SAP HANA version 2.8**

Version 2.8 of the monitoring agent for SAP HANA is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

## September 26, 2022

Announcement

**BigQuery Connector for SAP version 2.5**

Version 2.5 of BigQuery Connector for SAP is now generally available (GA).

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new).

## September 23, 2022

Announcement

**Terraform configuration for SAP NetWeaver high-availability cluster configuration on RHEL**

Terraform configuration to automate the deployment of resources for SAP NetWeaver high-availability cluster configuration on RHEL, on Google Cloud, is now generally available (GA).

For more information, see [Terraform: HA cluster configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel-tf).

## September 16, 2022

Announcement

**New SAP HANA certification: 9 TB m2-hypermem-416 VMs certified for OLTP workloads**

SAP has certified the Compute Engine 9 TB m2-hypermem-416 machine type for SAP HANA OLTP workloads in scale-up or scale-out configurations with up to 4 nodes. SAP workload-based sizing methods must be used.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#m2-memory-optimized).

## August 29, 2022

Announcement

**New SAP certification for operating system**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has now certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 8.6.

For more information about SAP-certified operating systems, see:

  * [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
  * [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)



Announcement

**Monitoring agent for SAP HANA version 2.7**

Version 2.7 of the monitoring agent for SAP HANA is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

## August 24, 2022

Announcement

**Monitoring agent for SAP HANA version 2.6**

Version 2.6 of the monitoring agent for SAP HANA is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

Announcement

**Google Cloud monitoring agent for SAP NetWeaver version 2.6**

Version 2.6 of the Google Cloud monitoring agent for SAP NetWeaver is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

## August 23, 2022

Announcement

**Terraform configurations for SAP deployments on Google Cloud**

Terraform configurations to automate the deployment of the following SAP solutions on Google Cloud are now generally available (GA):

  * SAP HANA single-host scale-up or multi-host scale-out
  * SAP HANA scale-out with host auto-failover
  * SAP HANA scale-up in a Linux high-availability cluster
  * SAP NetWeaver on RHEL or SLES
  * SAP NetWeaver high-availability cluster configuration on SLES



For more information, see [Automating SAP deployments on Google Cloud with Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap).

## August 16, 2022

Announcement

**Monitoring agent for SAP HANA version 2.5**

Version 2.5 of the monitoring agent for SAP HANA is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

## July 26, 2022

Change

**Cloud Storage Backint agent for SAP HANA version 1.0.21**

Version 1.0.21 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes enhancements for backup stability and performance.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## July 14, 2022

Announcement

**Google Cloud monitoring agent for SAP NetWeaver version 2.5**

Version 2.5 of the Google Cloud monitoring agent for SAP NetWeaver is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

## July 07, 2022

Change

**Cloud Storage Backint agent for SAP HANA version 1.0.20**

Version 1.0.20 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes backup stability and logging enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## June 15, 2022

Announcement

**Google Cloud monitoring agent for SAP NetWeaver version 2.4**

Version 2.4 of the Google Cloud monitoring agent for SAP NetWeaver is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

## June 06, 2022

Announcement

**BigQuery Connector for SAP version 2.1**

Version 2.1 of BigQuery Connector for SAP is now available. For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector-for-sap-whats-new).

## June 01, 2022

Announcement

**Google Cloud storage manager for SAP HANA standby nodes version 2.5**

Version 2.5 of the Google Cloud storage manager for SAP HANA standby nodes is now available. This version includes bug fixes and supportability improvements.

For more information about the storage manager, see [Storage Manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh).

## May 30, 2022

Announcement

**Google Cloud Connector for SAP Landscape Management version 2.3.2**

Version 2.3.2 of the Google Cloud Connector for SAP Landscape Management is now available. This version includes bug fixes and supportability improvements.

For more information about the connector, see [Connector for SAP Landscape Management planning guide](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning).

Announcement

**Cloud Storage Backint agent for SAP HANA version 1.0.18**

Version 1.0.18 of the Cloud Storage Backint agent for SAP HANA is now available. This version includes supportability improvements and backup stability enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## May 24, 2022

Announcement

**Google Cloud monitoring agent for SAP NetWeaver version 2.3**

Version 2.3 of the Google Cloud monitoring agent for SAP NetWeaver is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

Announcement

**Monitoring agent for SAP HANA version 2.4**

Version 2.4 of the monitoring agent for SAP HANA is now available. This version includes bug fixes and supportability improvements.

For more information about the agent, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

## May 06, 2022

Announcement

**Extreme persistent disks are available for SAP HANA with improved functionality**

Recent enhancements have further optimized extreme persistent disks, removing any potential limitations for using extreme persistent disks with SAP HANA.

For more information about extreme persistent disks and SAP HANA, see:

  * [Extreme persistent disks](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk)
  * [Persistent disk storage for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage)



## April 18, 2022

Change

**SAP NetWeaver high-availability clusters on SLES - change to recommended configuration**

The recommended configuration for enabling back-end communication between the nodes in a SUSE Linux Enterprise Server (SLES) high-availability cluster for SAP NetWeaver on Google Cloud has changed.

The new guidance uses the `google-guest-agent` to enable back-end communication instead of a startup script.

If you are using a startup script to enable back-end communication in an existing cluster, we recommend that you switch to the `google-guest-agent` configuration at your earliest convenience.

For the updated guidance, see [Enable load balancer back-end communication between the VMs](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#enable-back-end-comms).

Announcement

**SAP NetWeaver high-availability cluster documentation for RHEL**

A new manual configuration guide for SAP NetWeaver high-availability clusters on Red Hat Enterprise Linux (RHEL) is available for use.

For more information, see the [HA cluster configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel).

## April 11, 2022

Announcement

**Storage Manager for SAP HANA Standby Nodes version 2.4**

Version 2.4 adds support for HANA 2.0 SPS 05 revision 59 and later. Google Cloud recommends that you update to version 2.4 at your earliest convenience.

For information about how to upgrade, see [Updating the storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh_update).

## April 08, 2022

Announcement

**Google Cloud monitoring agent for SAP NetWeaver, version 2.2**

Version 2.2 of the monitoring agent for SAP NetWeaver is now available. This version fixes an issue where the "Data Provider Version" was not being supplied on Windows OS's.

For more information, see [SAP NetWeaver Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

Announcement

**Backint agent for SAP HANA version 1.0.17**

Version 1.0.17 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.17 includes bug fixes for Google Cloud Logging integrations.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## February 14, 2022

Announcement

**SAP NetWeaver certifications: T2D AMD-based general-purpose machine types**

For SAP NetWeaver, SAP now certifies Compute Engine general-purpose T2D series machine types with the AMD EPYC Milan CPU platform.

For more information, see [T2D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-t2d).

## February 11, 2022

Announcement

**SAP NetWeaver certifications: C2D AMD-based compute-optimized machine types**

For SAP NetWeaver, SAP now certifies Compute Engine compute-optimized C2D series machine types with the AMD EPYC Milan CPU platform.

For more information, see [C2D compute-optimized machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-compute-optimized-c2d).

## February 09, 2022

Announcement

**SAP NetWeaver certifications: N2D series Compute Engine VMs on the AMD EPYC Milan CPU platform**

For SAP NetWeaver, SAP now certifies Compute Engine N2D series machine types with the AMD EPYC Milan CPU platform.

For more information, see [N2D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n2d).

## February 03, 2022

Announcement

**SAP HANA certifications: N2 series Compute Engine VMs on the Intel Ice Lake CPU platform**

SAP now certifies Compute Engine N2 series machine types with the Intel Ice Lake CPU platform. The new SAP HANA certifications include two new machine sizes, n2-highmem-96 and n2-highmem-128.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-n2-certs).

Announcement

**SAP NetWeaver certifications: N2 series Compute Engine VMs on the Intel Ice Lake CPU platform**

SAP now certifies Compute Engine N2 series machine types with the Intel Ice Lake CPU platform. The new SAP NetWeaver certifications include two new machine sizes, n2-highmem-96 and n2-highmem-128.

For more information, see [N2 general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n2).

## January 31, 2022

Announcement

**BigQuery Connector for SAP:** Google Cloud BigQuery Connector for SAP is now generally available (GA).

With BigQuery Connector for SAP version 2.0, the GA release, you can replicate SAP application data changes into BigQuery in near real-time for analytical and ML/AI consumption. BigQuery Connector for SAP connects SAP Landscape Transformation Replication Server directly to BigQuery through the BigQuery streaming API.

For more information, see:

  * [The SAP on Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/bigquery-connector-for-sap)
  * [The BigQuery Connector for SAP documentation](https://docs.cloud.google.com/sap/docs/bq-connector-for-sap-guides)



## January 21, 2022

Change

**SAP HANA HA/DR provider hook configuration updated for RHEL and SLES high-availability clusters**

The Google Cloud guidance for configuring an SAP HANA HA/DR provider hook has been updated in the HA cluster configuration guides for SAP HANA on RHEL and SLES. You can enable the SAP HANA HA/DR provider hook to improve signaling of SAP HANA's replication state within the Pacemaker cluster.

The latest version of the [Deployment Manager](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment#creating_a_high-availability_linux_cluster_with_sap_hana_installed) template that Google Cloud provides to deploy an HA cluster for SAP HANA configures the hook automatically.

For more information, see:

  * [RHEL: Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable-hana-hadr-provider-hook)
  * [SLES: Enable the SAP HANA HA/DR provider hook](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable-hana-hadr-provider-hook)
  * [Automated SAP HANA HA deployment](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment)



## January 19, 2022

Announcement

**Google Cloud Connector for SAP Landscape Management version 2.3.0**

Version 2.3.0 of the Google Cloud Connector for SAP Landscape Management is now available. Version 2.3.0 adds support for duplicate IP addresses in managed SAP landscapes.

For more information, see [Configuring support for duplicate IP addresses](https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment#c4lm_duplicate_ip_address).

## January 04, 2022

Fixed

**Storage Manager for SAP HANA Standby Nodes version 2.3**

Version 2.3 of the Storage Manager for SAP HANA Standby Nodes is now available. Version 2.3 improves the handling of persistent disks that are in use when a failover occurs.

Google Cloud recommends that you update to version 2.3 at your earliest convenience.

## December 20, 2021

Announcement

**Backint agent for SAP HANA version 1.0.16**

Version 1.0.16 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.16 includes bug fixes and performance enhancements.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## December 16, 2021

Announcement

**Filestore Enterprise for SAP systems**

The Enterprise tier of Filestore (Filestore Enterprise) is now generally available (GA) as a file sharing solution for SAP systems on Google Cloud. The GA release of Filestore Enterprise includes support for multi-zone, high-availability configurations of SAP systems.

For more information, see [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap).

## December 15, 2021

Announcement

Google Cloud monitoring agent for SAP NetWeaver, version 2.1

Version 2.1 of the monitoring agent for SAP NetWeaver is now available. This version updates the JRE that is used by the agent and fixes an issue when upgrading.

For more information, see [SAP NetWeaver Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

Announcement

Backint agent for SAP HANA version 1.0.15

Version 1.0.15 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.15 updates an internal library (maven-artifact) used by the agent.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

Announcement

Monitoring agent for SAP HANA, version 2.2

Version 2.2 of the monitoring agent for SAP HANA is now available. This version updates the JRE that is used by the agent.

For more information, see [Monitoring agent for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-user-guide).

## November 30, 2021

Announcement

**Google Cloud Connector for SAP Landscape Management version 2.2.16**

Version 2.2.16 of the Google Cloud Connector for SAP Landscape Management is now available. Version 2.2.16 adds support for managing SAP systems that are running on the Windows Server, Data Center edition, operating system.

For more information about the software requirements for the systems that are managed by SAP Landscape Management with the Google Cloud Connector for LaMa, see [Managed SAP landscape requirements](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning#managed_sap_landscape_requirements).

## November 18, 2021

Announcement

**Backint agent for SAP HANA version 1.0.14**

Version 1.0.14 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.14 adds tooling for use by the Google Cloud Customer Support team to identify and fix backup issues after a customer opens a case.

**Update, Dec. 13, 2021:** Version 1.0.14 also changed the endpoint that the Backint agent for SAP HANA uses to access the Google APIs from `www.googleapis.com` to `storage.googleapis.com`. If your networking configuration for the Backint agent references the `www.googleapis.com` in, for example, a proxy or in routing rules, you need to update the configuration to reference the `storage.googleapis.com` endpoint instead.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 12, 2021

Fixed

**Backint agent for SAP HANA StorageException issue fixed**

Google Cloud released version 1.0.13 of the Backint agent for SAP HANA, which fixes an issue that could cause a backup that is stored in Cloud Storage to be unusable if a StorageException error occurred during the backup process.

**Apply the fix as soon as possible** by downloading and installing version 1.0.13 of the Backint agent for SAP HANA.

For more information about the issue and the fix, see [StorageException for Cloud Storage can cause corrupted Backint agent backup](https://docs.cloud.google.com/sap/docs/known-issues#backint-issue).

Announcement

**Backint agent for SAP HANA version 1.0.13**

Version 1.0.13 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.13 improves the handling of StorageException errors that might occur when writing backups to Cloud Storage. This version fixes an issue that, under certain circumstances, could make stored backups unusable.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## November 03, 2021

Issue

**FIXED: SAP HANA backup issue with Backint agent**

A critical issue that can result in corrupted backups has been identified that might affect users of the Backint agent for SAP HANA. We are actively working on a fix.

For the fix and for more information, see [StorageException for Cloud Storage can cause corrupted Backint agent backup](https://docs.cloud.google.com/sap/docs/known-issues#backint-issue).

## October 25, 2021

Announcement

**New SAP certifications:** SAP has certified the following operating systems for SAP HANA on Google Cloud:

  * Red Hat Enterprise Linux 8.2
  * Red Hat Enterprise Linux 8.4
  * SUSE Linux Enterprise Server 15 SP3



See [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-oss).

## October 21, 2021

Change

**High-availability configuration guidance changed**

The Google Cloud guidance for configuring Pacemaker clusters for SAP has changed for better integration with Google Cloud infrastructure and to more closely align with the defaults and recommendations that are provided by the operating system vendors. These are non-breaking changes that are recommended for optimal reliability. The changes apply to the fence agent, some cluster resource definitions, and some default settings of the Corosync and Pacemaker cluster properties. The Deployment Manager scripts and manual deployment guides have been updated to reflect these changes.

If you have an existing Linux high-availability cluster for SAP on Google Cloud, compare your current settings to the new recommendations and update your cluster as necessary.

For instructions on displaying your current cluster settings and for an example of the recommended cluster settings, see [Checking your cluster configuration](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment#checking_your_cluster_configuration).

Issue

**SAP HANA scale-out deployment fails due to a Python error**

If you have an existing SAP HANA scale-out system with host auto-failover on Google Cloud and you are upgrading SAP HANA to SAP HANA 2.0 SPS 5 Revision 56 or later, SAP HANA fails to start due to a Python error that prevents the storage manager for SAP HANA from attaching storage. The storage manager for SAP HANA version 2.1 or earlier does not support SAP HANA 2.0 SPS 5 Revision 56 or later.

To resolve the issue, upgrade the storage manager for SAP HANA to version 2.2 or later. For more information, see [Known issues](https://docs.cloud.google.com/sap/docs/known-issues#sap_hana_scale-out_deployment_fails_due_to_a_python_error).

Issue

**High-availability cluster failover issue due to a Corosync communication delay**

For RHEL and SLES operating systems, if there is a temporary delay in the transmission of Corosync messages between the cluster nodes, the delay can incorrectly trigger a failover for your high-availability (HA) cluster for SAP solutions on Google Cloud.

Follow the resolution steps depending on your operating system. For more information, see [Known issues](https://docs.cloud.google.com/sap/docs/known-issues#high-availability_cluster_failover_issue_due_to_a_corosync_communication_delay).

## October 11, 2021

Announcement

**Backint agent for SAP HANA version 1.0.12**

Version 1.0.12 of the Google Cloud Backint agent for SAP HANA is now available. Version 1.0.12 provides compatibility for Backint protocol 1.5, as well as other minor fixes and enhancements. Version 1.0.12 does not include any changes to the features or functionality of the Backint agent for SAP HANA.

For more information about the agent, see [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

Announcement

**Storage Manager for SAP HANA Standby Nodes version 2.2**

Version 2.2 of the Google Cloud storage manager for SAP HANA standby nodes is now available. Version 2.2 adds support for SAP HANA 2.0 rev 56 and above, and includes minor bug fixes and performance enhancements. Version 2.2 does not include any other changes to the features or functionality of the storage manager for SAP HANA.

For more information about the storage manager for SAP HANA, see [SAP HANA host auto-failover on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover).

## September 29, 2021

Announcement

**SAP HANA certification: 12 TB m2-ultramem-416 VMs certified for OLAP scale out**

SAP has certified the Compute Engine 12 TB m2-ultramem-416 machine type for SAP HANA OLAP workloads in scale-out configurations with up to 16 nodes. SAP workload-based sizing is required.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#m2-memory-optimized).

## September 15, 2021

Announcement

**Google Cloud monitoring agent for SAP NetWeaver, version 2.0 is generally available**

Version 2.0 of the monitoring agent for SAP NetWeaver is now generally available (GA). For Linux, version 2.0 of the monitoring agent provides a simpler installation and upgrade path that conforms to the standard OS-based package management. For Windows, only the service name is changed to `google-sapnetweavermonitoring-agent`.

The information collected by version 2.0 of the monitoring agent for SAP NetWeaver is the same as version 1.0.

For more information, see [SAP NetWeaver Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#monitoring_sap_netweaver_on_gcp).

## August 31, 2021

Announcement

**SAP HANA Fast Restart and Compute Engine M2 machines speed memory-error recovery**

Compute Engine recently updated M2 VM types so that they can keep running when uncorrectable memory errors occur by using _memory-poisoning recovery_. Except for the block affected by the error, SAP HANA Fast Restart can then maintain all data in memory, which significantly reduces restart time because only the affected block is reloaded.

For more information, see [Memory-error recovery with Fast Restart on Compute Engine VMs](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#sap-hana-fast-restart-memory-error-recovery).

## August 05, 2021

Change

**High-availability cluster configuration guidance has changed**

To minimize the likelihood of timing errors during a restart after failover, the guidance for setting up Pacemaker clusters on Linux for SAP has changed to include setting a short delay in the startup of Corosync after a failover.

For more information, see:

  * [Manual HA cluster configuration on RHEL for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_a_delay_for_the_restart_of_corosync)
  * [Manual HA cluster configuration on SLES for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#set_a_delay_for_the_restart_of_corosync)
  * [HA cluster configuration on SLES for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#set_a_delay_for_the_restart_of_corosync)



## August 02, 2021

Announcement

**Google Cloud Connector for SAP LaMa is generally available**

The Google Cloud Connector for SAP Landscape Management 3.0, enterprise edition, is now generally available (GA). 

For more information, see the [Connector for SAP Landscape Management planning guide](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning).

## July 15, 2021

Change

**SAP HANA: sizing guidelines for persistent disks reduced**

For most Compute Engine VM types that are certified for SAP HANA, Google Cloud has reduced the required minimum sizes of SSD and balanced persistent disks that are used for block storage by reducing the amount of storage that is allocated to the `/hana/data` volume from 1.5x memory to 1.2x memory. Google Cloud also updated the Deployment Manager templates that Google Cloud provides for SAP HANA to use the reduced sizes.

For more information, see [Minimum sizes for SSD and balanced persistent disks](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).

## June 30, 2021

Announcement

**SAP HANA certification: 12 TB m2-ultramem-416 machine type for OLAP workloads**

SAP has certified the Compute Engine 12 TB m2-ultramem-416 machine type for SAP HANA with OLAP workloads in an SAP HANA scale-up configuration that must be sized by using SAP workload-based sizing methods.

For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#m2-memory-optimized).

Announcement

**SAP NetWeaver is supported on Bare Metal Solution with more database types**

In addition to SAP HANA, you can now run SAP NetWeaver on Bare Metal Solution servers for production workloads with other SAP NetWeaver supported database types, such as Oracle databases. 

For more information, see [SAP NetWeaver on Bare Metal Solution planning guide](https://docs.cloud.google.com/sap/docs/netweaver-on-bms-planning).

## June 29, 2021

Change

**SAP HANA high-availability configurations for SUSE** : Google Cloud changed its guidance for the definition of the `SAPHana` primitive resource by increasing the recommended value of the `op monitor interval` option for both the primary and secondary nodes.

For more information, see [Create the SAPHana primitive resource](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#create_the_saphana_primitive_resource).

## June 10, 2021

Announcement

**SAP NetWeaver high-availability cluster documentation for SLES**

A new load-balancer-based configuration guide for SAP NetWeaver high-availability clusters on SUSE Linux Enterprise Server (SLES) is available for use.

For more information, see the [HA cluster configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles).

## May 26, 2021

Announcement

**GA: Google Cloud monitoring agent for SAP HANA, version 2**

Version 2.0 of the monitoring agent for SAP HANA is now generally available. V2.0 represents a complete refactoring of the monitoring agent for SAP HANA. A new Cloud Monitoring dashboard template for SAP HANA data is now also available for use with V2.0.

For more information, see [Monitoring agent for SAP HANA V2.0 planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-planning-guide).

## May 05, 2021

Announcement

**Updated SAP HANA certification of the 6 TB m2-megamem-416 machine type**

For OLAP workloads, the SAP certification of the Compute Engine 6 TB m2-megamem-416 machine type now includes:

  * Scale-out configurations up to 16 nodes. 
  * Compute Engine persistent disks for storage in scale-up or scale-out configurations.



For more information, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#m2-memory-optimized).

## April 19, 2021

Announcement

**File sharing options for SAP on Google Cloud** : New guidance has been published to help you determine the best file sharing option for your SAP deployments on Google Cloud.

For more information, see [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap).

## April 15, 2021

Issue

**SAP HANA high-availability configurations on Red Hat:** If you configured a RHEL HA cluster for SAP HANA before April 15, 2021 by following the Google Cloud documentation, you need to modify the location constraints of your cluster fencing devices to avoid possible race conditions during failovers.

To see the updated documentation to correct the issue, see [Set up fencing, step 1.b.](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#set_up_fencing)

## March 31, 2021

Announcement

The **Cloud Data Fusion plugin for SAP** is now available. With the SAP Table Batch Source plugin and Cloud Data Fusion, you can create a data pipeline to integrate your SAP data with your data repositories on Google Cloud.

For more information, see [Using the SAP Table Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin).

Feature

The **Deployment Manager template** that Google Cloud provides to automate the deployment of **Linux high-availability clusters for SAP HANA** now supports Red Hat Enterprise Linux (RHEL) images.

For more information, see [Automated SAP HANA HA deployment with load-balancer VIP implementation](https://docs.cloud.google.com/sap/docs/sap-hana-ha-dm-deployment).

## March 12, 2021

Announcement

The **Google Storage Backint agent for SAP HANA** has been updated to version 1.0.8. You can now upload backups to Cloud Storage faster using the Backint agent parallel upload function.

For more information, see [Parallel uploads](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview#parallel_uploads).

## March 11, 2021

Announcement

**Deployment checklists for SAP on Google Cloud:** These additions to the SAP on Google Cloud documentation can help you to migrate your SAP systems to Google Cloud quickly and to avoid costly missteps in the process.

For more information, see [Overview of the SAP on Google Cloud deployment checklists](https://docs.cloud.google.com/sap/docs/checklist-sap-overview).

## March 02, 2021

Announcement

**Google Cloud monitoring agent for SAP NetWeaver, Version 1.1** is now available. This new version removes automatic updates so that you can control when new versions are applied to your system. It also adds support for Bare Metal Solution environments.

For information about the new update method, see [Updating the monitoring agent for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide#nw_mon_agent_updating).

Announcement

**New SAP certifications:** For SAP NetWeaver, the following Compute Engine virtual machine types that use the AMD CPU platform are certified by SAP:

  * n2d-standard-128
  * n2d-standard-224
  * n2d custom machine type vCPU limit increased to 96



For more information, see:

  * [N2D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n2d)
  * [Custom VM configurations](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-custom)



## March 01, 2021

Announcement

The preview release of **Google Cloud monitoring agent for SAP HANA, version 2** is now available. Version 2.0 represents a complete refactoring of the monitoring agent for SAP HANA.

For more information, see [Monitoring agent for SAP HANA V2.0 planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-planning-guide).

Deprecated

Version 1.0 of the Google Cloud monitoring agent for SAP HANA is deprecated. For new installations, use the Google Cloud monitoring agent for SAP HANA V2.0. 

Support for version 1 of the monitoring agent for SAP HANA ends on December 31, 2021.

For information about version 2, see [Monitoring agent for SAP HANA V2.0 planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-monitoring-agent-planning-guide).

## February 16, 2021

Feature

For **SAP HANA host auto-failover,** version 2.0 of the gceStorageClient is now available with a new human-readable name: _Google Cloud Storage Manager for SAP HANA Standby Nodes_ (_Storage Manager for SAP HANA_ for short). The new version uses RPM Package Manager for installation and updates, and supports all versions of SAP HANA that are in mainstream maintenance.

For more information, see [SAP HANA host auto-failover on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover).

Deprecated

Version 1._n_ releases of the gceStorageClient for SAP HANA host auto-failover are deprecated.

If you are using a version 1._n_ release, upgrade to version 2.0 of the gceStorageClient, the _Google Cloud Storage Manager for SAP HANA Standby Nodes_ , at your earliest convenience, but before support is discontinued.

Version 1._n_ releases of the gceStorageClient will be supported until December 31, 2021.

To determine which version you are running, see [Deprecation of version 1._n_ releases of the storage manager for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#host_auto_failover_sm4sh_versions).

## January 20, 2021

Announcement

**New SAP certifications:** For SAP HANA, the following Bare Metal Solution bare-metal machine types are certified by SAP:

  * o2-ultramem-672-metal
  * o2-ultramem-896-metal



For more information, see [Certified machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-vms).

Announcement

**New SAP certifications:** For SAP NetWeaver, the following Bare Metal Solution bare-metal machine types are certified by SAP:

  * o2-standard-32-metal
  * o2-standard-48-metal
  * o2-standard-112-metal
  * o2-highmem-224-metal



For more information, see [Bare Metal Solution machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-bms-machines).

## November 25, 2020

Deprecated

The `sap_hana_ha/template.yaml` file that is provided by Google Cloud to deploy SAP HANA in a SLES high-availability cluster that uses a virtual IP address (VIP) with an alias-IP implementation is deprecated.

As a replacement, use the new `sap_hana_ha_ilb/template.yaml` file that uses a TCP internal load balancer for the VIP.

The deprecated template and the corresponding documentation, [Automated SAP HANA SLES HA deployment with alias-IP VIP implementation](https://docs.cloud.google.com/sap/docs/sap-hana-ha-deployment-guide), will continue to be available for at least 12 months from today.

Announcement

**New SAP certifications:** For SAP NetWeaver, the following Compute Engine virtual machine types that use the AMD CPU platform are certified by SAP:

  * n2d-highmem-48
  * n2d-highmem-64
  * n2d-highmem-80
  * n2d-highmem-96
  * n2d-standard-48
  * n2d-standard-64
  * n2d-standard-80
  * n2d-standard-96



For more information, see [N2D general-purpose machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-n2d).

Feature

You can now automate the deployment of SAP HANA in a SUSE Linux Enterprise Server high-availability (HA) cluster that uses the recommended TCP internal load balancer implementation for the virtual IP address.

For more information, see [Automated deployment of Linux high-availability clusters for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#deployment_manager_for_sap_hana_ha_cluster).

## November 06, 2020

Announcement

**New SAP certifications:** SAP has certified the following operating systems for SAP HANA on Google Cloud:

  * Red Hat Enterprise Linux 7.7
  * Red Hat Enterprise Linux 8.1
  * SUSE Linux Enterprise Server 15 SP2



See [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-oss).

## October 01, 2020

Feature

New guidance for using Compute Engine persistent disks, including balanced persistent disks, with SAP applications and SAP HANA on Google Cloud. See [SAP HANA Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage).

## September 30, 2020

Announcement

Google Cloud Connector for SAP Landscape Management launched in private preview. If you are interested in participating in the preview, contact the preview coordinators [sap-lama-support@google.com](mailto:sap-lama-support@google.com).

## September 24, 2020

Announcement

**New SAP certification** : SAP HANA OLTP workloads on the Compute Engine 6 TB m2-megamem-416 machine type. See [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-vms).

## August 31, 2020

Feature

The Cloud Storage Backint agent for SAP HANA is GA with new options for encryption, removal of automatic updates, and other enhancements. See [Cloud Storage Backint agent for SAP HANA overview](https://docs.cloud.google.com/sap/docs/sap-hana-backint-overview).

## August 04, 2020

Feature

New guidance for SAP HANA high availability deployments regarding available high-availability cluster configurations. See [OS-native HA clusters for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#sap_ha_cluster_configurations).

## July 29, 2020

Announcement

**New SAP certification** : S/4HANA scale out on the Compute Engine 12 TB m2-ultramem-416 machine type. See [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-vms).

## July 16, 2020

Feature

New guidance for SAP HANA high-availability deployments, including steps for migrating a virtual IP implementation from alias IP to a new internal load balancer implementation. See [Migrating a VIP in a SLES HA cluster to an internal load balancer](https://docs.cloud.google.com/sap/docs/sap-hana-ha-vip-migration-sles).

## June 29, 2020

Announcement

**New SAP certification** : SAP HANA OLAP workloads on the Compute Engine 6 TB m2-megamem-416 machine type with NetApp Cloud Volumes Service. See [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-vms).

## June 23, 2020

Feature

New guidance for configuring Linux high-availability clusters for SAP HANA is now available for the users of the Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Server (SLES) operating systems. See:

  * [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



This page includes release announcements from approximately the end of June, 2020 to the present. For more information about the Google Cloud products, services, and solutions that are available for SAP, see: 

  * [Overview of SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)
  * [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps)
  * [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
