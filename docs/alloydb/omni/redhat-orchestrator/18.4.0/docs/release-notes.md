---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/release-notes/
title: AlloyDB Omni release notes \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:21:27.894911+00:00
---

# AlloyDB Omni release notes  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/release-notes/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/resources)



Send feedback 

#  AlloyDB Omni release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to AlloyDB Omni. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/alloydbomni-release-notes.xml) directly. 

## October 14, 2026

Announcement

AlloyDB Omni using the Red Hat RPM orchestrator 1.0.1 is generally available ([GA](https://docs.cloud.google.com/products#product-launch-stages)) for AlloyDB Omni version 18.4.0. It includes the following:

  * Support for [PostgreSQL version 18.4](https://www.postgresql.org/docs/release/18.4/).
  * Critical security patches, internal stability improvements, and bug fixes.
  * A [shared responsibility matrix](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/shared-responsibility) that clarifies the operational boundaries between you and Google Cloud when deploying AlloyDB Omni using the Red Hat RPM orchestrator.



Security

Fixes for the following vulnerabilities are available for version 18.4.0:

  * [CVE-2026-19385](https://nvd.nist.gov/vuln/detail/CVE-2026-19385)
  * [CVE-2026-18408](https://nvd.nist.gov/vuln/detail/CVE-2026-18408)
  * [CVE-2026-16239](https://nvd.nist.gov/vuln/detail/CVE-2026-16239)
  * [CVE-2026-15742](https://nvd.nist.gov/vuln/detail/CVE-2026-15742)
  * [CVE-2026-15741](https://nvd.nist.gov/vuln/detail/CVE-2026-15741)
  * [CVE-2026-14680](https://nvd.nist.gov/vuln/detail/CVE-2026-14680)
  * [CVE-2026-14679](https://nvd.nist.gov/vuln/detail/CVE-2026-14679)
  * [CVE-2026-14677](https://nvd.nist.gov/vuln/detail/CVE-2026-14677)
  * [CVE-2026-14671](https://nvd.nist.gov/vuln/detail/CVE-2026-14671)
  * [CVE-2026-14670](https://nvd.nist.gov/vuln/detail/CVE-2026-14670)
  * [CVE-2026-14669](https://nvd.nist.gov/vuln/detail/CVE-2026-14669)
  * [CVE-2026-14668](https://nvd.nist.gov/vuln/detail/CVE-2026-14668)
  * [CVE-2026-14664](https://nvd.nist.gov/vuln/detail/CVE-2026-14664)
  * [CVE-2026-14662](https://nvd.nist.gov/vuln/detail/CVE-2026-14662)
  * [CVE-2026-6471](https://nvd.nist.gov/vuln/detail/CVE-2026-6471)
  * [CVE-2026-6464](https://nvd.nist.gov/vuln/detail/CVE-2026-6464)



## September 08, 2026

Announcement

[AlloyDB Omni using the Red Hat RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview) version 18.3.0 is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). This release provides a fully orchestrated experience for Linux using Red Hat RPMs and includes the following features:

  * Supports [PostgreSQL version 18.3](https://www.postgresql.org/docs/release/18.3/).
  * Supports [tuning startup configurations and customizing PostgreSQL ports and cache settings](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-database-parameters).
  * Automates [component failure handling and provides read endpoints for standby instances](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-high-availability).
  * Supports automated pgBackRest backups and restores to Google Cloud Storage, Amazon S3, and S3-compatible storage. For more information, see [Backup and restore data using pgBackRest](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/backup-restore-pgbackrest). Features include the following: 
    * Periodic full, incremental, and differential backups.
    * Dynamic backup pausing.
    * Backup retention configuration.
    * In-place, point-in-time restores.
  * Supports read pool instances to scale read-only workloads.
  * Supports dynamically adding or deleting database nodes.
  * Provides a framework to [define and collect custom database metrics to enhance monitoring](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/improve-observability-custom-monitoring-metrics).
  * Streamlines updates for control and data plane components and supports rollbacks.
  * Redirects data path and control path logs to the log disk, and supports log rotation. For more information, see [Configure logging for a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-log-redirection).
  * Provides AlloyDB AI parity for the RPM orchestrator, including AI enablement and [ScaNN index troubleshooting](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/troubleshoot-scann-indexes).
  * Provides SELinux support for all orchestrator components. This support lets you enable security policies during and after cluster bootstrap. For more information, see [SELinux policy specifications](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster#selinux-policy-specifications).



## April 22, 2026

Announcement

[AlloyDB Omni using the Red Hat RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview) is now available in [Preview](https://docs.cloud.google.com/products#product-launch-stages) for AlloyDB Omni version 18.1.0. To get started, [submit this form to request access](https://forms.gle/zxuHekMtV67Bw9Av9).

This release provides full orchestration for AlloyDB Omni Red Hat RPM orchestrator and includes the following features:

  * Provides complete automation for deployment and a centralized control plane to manage AlloyDB Omni using the Red Hat RPM orchestrator. For more information, see [Install the AlloyDB Omni orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-orchestrator).
  * Streamlines provisioning of AlloyDB Omni software using an integrated Ansible collection. For more information, see [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).
  * Simplifies initial setup and cluster creation for faster environment readiness. For more information, see [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).
  * Supports high availability and automated failover for the Red Hat RPM orchestrator deployment option, with built-in health monitoring. For more information, see [Manage High Availability](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability).
  * Supports backup and restore using pgBackRest. For more information, see [Backup and restore using pgBackRest](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/backup-restore-pgbackrest).
  * Supports automated configuration and rotation of SSL/TLS certificates for secure database communication. For more information, see [Configure TLS Certificates](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/overview).
  * Supports external load balancers to manage traffic and enhance availability. For more information, see [Configure a load balancer](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-load-balancer).
  * Integrates seamlessly with PgBouncer connection pooler for efficient connection management. For more information, see [Use the PgBouncer connection pooler](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/use-pgbouncer-connection-pooler).
  * Centrally manages PostgreSQL configuration settings and database parameters using the automated control plane. For more information, see [Configure database parameters](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-database-parameters).
  * Supports automated log management, enabling log redirection to a log volume for optimal disk usage and auditability. For more information, see [Configure logging for a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-logging-cluster).
  * Generates diagnosis dump files with system state and diagnostic logs to troubleshoot issues. For more information, see [Generate diagnosis dump files](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-dump-files).



Change

The naming conventions for AlloyDB Omni deployment options are updated to more accurately reflect their respective installation and orchestration methods.  
The following table summarizes the primary name changes:

**Original name** |  **New name**  
---|---  
AlloyDB Omni for containers |  AlloyDB Omni using containers  
AlloyDB Omni for Kubernetes |  AlloyDB Omni using the container orchestrator  
AlloyDB Omni for Linux |  AlloyDB Omni using RPM  
Red Hat RPM orchestrator |  AlloyDB Omni using the RPM orchestrator  
  
This update clarifies the distinction between AlloyDB Omni deployment environments (such as Kubernetes or standalone Linux) and the packaging and orchestration technologies used to manage them. For more information, see [Choose your deployment environment](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
