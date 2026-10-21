---
url: https://docs.cloud.google.com/logging/docs/release-notes/
title: Logging release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:39.266775+00:00
---

# Logging release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Resources ](https://docs.cloud.google.com/logging/quotas)



Send feedback 

#  Logging release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Logging. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

For a combined list of all release notes for the products in Google Cloud Observability, see [Consolidated release notes](https://docs.cloud.google.com/stackdriver/docs/release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## September 28, 2026

Deprecated

The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

Breaking

Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

## September 14, 2026

Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## August 26, 2026

Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

## August 14, 2026

Announcement

The Telemetry API for logs ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP logs into Cloud Logging by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp/overview).

## June 22, 2026

Security

If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see [Errors routing to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage).

## June 18, 2026

Change

The Cloud Logging API adds support for the `ca` regional endpoint. For a complete list of regional endpoints, see the [REST reference pages](https://docs.cloud.google.com/logging/docs/reference/v2/rest?rep_location=global).

## May 28, 2026

Announcement

You can view the available regional endpoints for the Cloud Logging API on the REST reference pages. For an example, see [Method: projects.locations.buckets.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list?rep_location=global).

## May 15, 2026

Feature

Starting with version 2.66.0, the Ops Agent can export your logs and metrics by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Logging API and Cloud Monitoring API. During the preview [Preview](https://docs.cloud.google.com/products#product-launch-stages) period, you can opt-in to using the Telemetry API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## April 22, 2026

Feature

The [Cloud Logging API MCP server](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp) is generally available (GA). To learn about using the Logging MCP server to let agents and AI applications interact with your log entries, see [Use the Cloud Logging remote MCP server](https://docs.cloud.google.com/logging/docs/use-logging-mcp).

## April 20, 2026

Libraries

### Go

#### [v1.16.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0) (2026-04-13)

## April 13, 2026

Libraries

### Go

#### [v1.15.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.14.0...logging/v1.15.0) (2026-04-09)

## April 07, 2026

Feature

You can now ingest OTLP-formatted logs into Cloud Logging by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP log ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-logs/overview). The Telemetry API for log ingestion is in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

## April 06, 2026

Libraries

### Go

#### [v1.14.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0) (2026-04-02)

## April 03, 2026

Announcement

Cloud Logging adds support for the `ca` multi-region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions). This note is incorrect; see entry for June 18, 2026.

## April 02, 2026

Feature

The filter capabilities for log views have been extended to include support for disjunctive clauses, negation statements, and labels. To learn more, see [Filters for log views](https://docs.cloud.google.com/logging/docs/logs-views#view-filter).

## March 30, 2026

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

## March 12, 2026

Issue

The automatic backfill operation performed on a log bucket that has been upgraded to use Log Analytics has been temporarily paused. To manually initiate the backfill operation, contact [Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support).

## February 12, 2026

Feature

You no longer need to configure BigQuery reservation assignments to create SQL-based alerting policies or run Log Analytics queries on BigQuery slots. These queries now use on-demand slots by default if no BigQuery reservation assignment exists.

For more information, see the following documents:

  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset#dedicated)
  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting#sql-policies-bigquery)



## February 09, 2026

Feature

You can use the [Cloud Logging API MCP server](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp) to let agents and AI applications interact with your log entries. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## February 02, 2026

Libraries

### Java

#### [3.24.0](https://github.com/googleapis/java-logging/compare/v3.23.11...v3.24.0) (2026-01-26)

##### Features

  * Bump minor version ([#1923](https://github.com/googleapis/java-logging/issues/1923)) ([ad7958c](https://github.com/googleapis/java-logging/commit/ad7958c789a86fd7fe2c10e3ce4ea57174aee379))



## January 29, 2026

Feature

You can now export your Crashlytics data and (optionally) Firebase sessions data to Cloud Logging. Once the data is exported, it's also available to Cloud Monitoring, so you can filter your logs, build custom dashboards, set up custom alerts, and even export the data to other services. For information about how to export your Crashlytics data, see [Export Crashlytics data to Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-export), and for information about how you can use this data, see [What can you do with Crashlytics data in Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do).

## January 26, 2026

Change

To support correlation between log and trace data, the following changes have been made:

  * The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

  * If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.

  * If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.




To learn more about default scopes, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

Feature

You can now install and manage the Ops Agent on virtual machines across zones in your Google Cloud project by using global VM Extension Manager extension policies. Global and zonal extension policies can keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

## January 20, 2026

Announcement

Cloud Logging adds support for the `asia-southeast3` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## January 19, 2026

Libraries

### Java

#### [3.23.10](https://github.com/googleapis/java-logging/compare/v3.23.9...v3.23.10) (2026-01-15)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.65.1 ([e0ca81e](https://github.com/googleapis/java-logging/commit/e0ca81e148d4f7dd6426640c574b453905cbe000))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.55.1 ([#1911](https://github.com/googleapis/java-logging/issues/1911)) ([93eadba](https://github.com/googleapis/java-logging/commit/93eadbaba65210e8686ea5240430fdbc86038fd5))
  * Update googleapis/sdk-platform-java action to v2.65.1 ([#1910](https://github.com/googleapis/java-logging/issues/1910)) ([3853159](https://github.com/googleapis/java-logging/commit/3853159f7255910dd33900086d410351f4cb0e98))



## December 22, 2025

Libraries

### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Java

#### [3.24.0-rc1](https://github.com/googleapis/java-logging/compare/v3.23.9...v3.24.0-rc1) (2025-12-16)

##### Features

  * [java] allow passing libraries_bom_version from env ([#1967](https://github.com/googleapis/java-logging/issues/1967)) ([#1615](https://github.com/googleapis/java-logging/issues/1615)) ([dc00cd0](https://github.com/googleapis/java-logging/commit/dc00cd0da891b59f3c22cd7ce281868f5ce8b433))
  * Add an API method for reordering firewall policies ([#1538](https://github.com/googleapis/java-logging/issues/1538)) ([9cd6b96](https://github.com/googleapis/java-logging/commit/9cd6b96d9946828c02ccff2ff846a06cc6fff329))
  * Add Cloud Run Jobs support ([#1574](https://github.com/googleapis/java-logging/issues/1574)) ([1dd64d0](https://github.com/googleapis/java-logging/commit/1dd64d078e0d4cbb1e16cb1d050ba192492d6a60))
  * enable hermetic library generation ([#1620](https://github.com/googleapis/java-logging/issues/1620)) ([034b9c4](https://github.com/googleapis/java-logging/commit/034b9c42ac8ba12f20dbde9e90ae8e59ea4c5748))
  * introduce `java.time` methods ([#1729](https://github.com/googleapis/java-logging/issues/1729)) ([323eb33](https://github.com/googleapis/java-logging/commit/323eb332a65f39c5588cf65ecae0a3454903a1c6))
  * Log Analytics features of the Cloud Logging API ([#1335](https://github.com/googleapis/java-logging/issues/1335)) ([7d43b80](https://github.com/googleapis/java-logging/commit/7d43b8049c71187fffcde39274db38ebb54cddfa))
  * **logging:** OpenTelemetry trace/span ID integration for Java logging library ([#1596](https://github.com/googleapis/java-logging/issues/1596)) ([67db829](https://github.com/googleapis/java-logging/commit/67db829621fd1c4a876d158fe1afb4927821fa54))
  * next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))
  * next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))
  * update with latest from main ([#1904](https://github.com/googleapis/java-logging/issues/1904)) ([d613362](https://github.com/googleapis/java-logging/commit/d61336242d51197207c94698735dfea72ec94c12))
  * Upgrade protobuf gen code to 4.33 ([#1905](https://github.com/googleapis/java-logging/issues/1905)) ([e25b532](https://github.com/googleapis/java-logging/commit/e25b5323d0ff7ca6d1c195d0eb342408621cdd76))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.31.0 ([#1502](https://github.com/googleapis/java-logging/issues/1502)) ([c7a20de](https://github.com/googleapis/java-logging/commit/c7a20de29bf6fae079f8d73e3062025a79c220c9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.32.0 ([#1511](https://github.com/googleapis/java-logging/issues/1511)) ([e2f574c](https://github.com/googleapis/java-logging/commit/e2f574caa0b8c2a2cdb3b186fbf2d599d6ef4c2b))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.37.0 ([#1553](https://github.com/googleapis/java-logging/issues/1553)) ([15b05fc](https://github.com/googleapis/java-logging/commit/15b05fc4a8e6c4069414110b749525082821e509))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.39.0 ([#1587](https://github.com/googleapis/java-logging/issues/1587)) ([848418b](https://github.com/googleapis/java-logging/commit/848418b426c2e93e636dbd9de71985c386ccb9d2))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.47.0 ([90b88ee](https://github.com/googleapis/java-logging/commit/90b88ee70ee84bdcb0af4aced50b5ee61e0a706c))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.49.0 ([a1ec68d](https://github.com/googleapis/java-logging/commit/a1ec68d539e4d0720fb2cf72314deb4f485f3d4a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.50.0 ([afcf63c](https://github.com/googleapis/java-logging/commit/afcf63cc063c4e0f5159c3ac5dbe2d372c335beb))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.0 ([04d8868](https://github.com/googleapis/java-logging/commit/04d886849a4b41fad17f501f2c40ae54e6daa71a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.58.0 ([45b4878](https://github.com/googleapis/java-logging/commit/45b4878eeec35f8c19a3cd3cd33331e9ece6b5c6))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.59.0 ([f2362fb](https://github.com/googleapis/java-logging/commit/f2362fb4c05d34fda4a1c9788ea87822ac887d9e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.1 ([1438bff](https://github.com/googleapis/java-logging/commit/1438bff5bc7028fbf125895f0bdd2bb50490effa))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.2 ([eeca440](https://github.com/googleapis/java-logging/commit/eeca440da06c24afc07e669f6f087246d91cd933))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.3 ([5d5d8a7](https://github.com/googleapis/java-logging/commit/5d5d8a76c58c3329f90e4fa84f5e81a1d3296894))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))
  * enable v2.LogEntry Protobufs converter functions ([#1509](https://github.com/googleapis/java-logging/issues/1509)) ([9ef4d90](https://github.com/googleapis/java-logging/commit/9ef4d9048b1ecdc887ebc9cb4898a4bfe3f6c154))
  * Fixed outdated link to X-Cloud-Trace-Context header description ([#1713](https://github.com/googleapis/java-logging/issues/1713)) ([d474313](https://github.com/googleapis/java-logging/commit/d4743138b9e5c9fd4e9c59b0793028f1e424e6e4))
  * **java:** handle empty modules ([09eeff0](https://github.com/googleapis/java-logging/commit/09eeff0b4608bad1e854252ff73688a867a071f1))
  * **java:** skip fixing poms for special modules ([#1744](https://github.com/googleapis/java-logging/issues/1744)) ([#1256](https://github.com/googleapis/java-logging/issues/1256)) ([09eeff0](https://github.com/googleapis/java-logging/commit/09eeff0b4608bad1e854252ff73688a867a071f1))
  * next release candidate ([31ee5a3](https://github.com/googleapis/java-logging/commit/31ee5a3b89701fbd9468a6ed903a9fc1951d65d5))
  * regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))
  * Remove org.jspecify dependency ([#1364](https://github.com/googleapis/java-logging/issues/1364)) ([8138f46](https://github.com/googleapis/java-logging/commit/8138f463e170f1927280d3c083fa403b184fca47))
  * Replace internal Structs class with google-cloud-core version ([#1501](https://github.com/googleapis/java-logging/issues/1501)) ([21e1929](https://github.com/googleapis/java-logging/commit/21e19295923a33759229e2e992d003409ab1feb3))



##### Dependencies

  * update actions/checkout action to v4 ([#1570](https://github.com/googleapis/java-logging/issues/1570)) ([ea0db35](https://github.com/googleapis/java-logging/commit/ea0db3579da6e965e778233b3cba4862b3fff65c))
  * update actions/github-script action to v7 ([#1571](https://github.com/googleapis/java-logging/issues/1571)) ([16d6192](https://github.com/googleapis/java-logging/commit/16d61928b6d4887faebbdd48a694a2edff8cb752))
  * update actions/setup-java action to v4 ([#1572](https://github.com/googleapis/java-logging/issues/1572)) ([9eb8834](https://github.com/googleapis/java-logging/commit/9eb88346fac9688c0e56bec83f7407c5690a5b7f))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.1 ([#1243](https://github.com/googleapis/java-logging/issues/1243)) ([fdf6b7a](https://github.com/googleapis/java-logging/commit/fdf6b7a44435286a47e1143a53a8307bb5b8fc63))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.2 ([#1258](https://github.com/googleapis/java-logging/issues/1258)) ([d4bc663](https://github.com/googleapis/java-logging/commit/d4bc663a0a0295594fb6333cf9bf2a6fd7a7b7e8))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.10.1 ([#1354](https://github.com/googleapis/java-logging/issues/1354)) ([b2f1111](https://github.com/googleapis/java-logging/commit/b2f1111fc8df71b40a85505e1b8209d315cc2c90))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.11.0 ([#1367](https://github.com/googleapis/java-logging/issues/1367)) ([8cd2a53](https://github.com/googleapis/java-logging/commit/8cd2a53b396d4671514bf8cca1b4c2a62cfb457c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.12.0 ([#1382](https://github.com/googleapis/java-logging/issues/1382)) ([8241302](https://github.com/googleapis/java-logging/commit/824130227897ed17c5b8a1becf32a695d844b2bb))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.0 ([#1388](https://github.com/googleapis/java-logging/issues/1388)) ([03179b0](https://github.com/googleapis/java-logging/commit/03179b0697f17bfc114ff114e454464ed76f8d5b))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.1 ([#1395](https://github.com/googleapis/java-logging/issues/1395)) ([1a29b9d](https://github.com/googleapis/java-logging/commit/1a29b9da803238ff1dee0c69d9449d97d4324477))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.14.0 ([#1409](https://github.com/googleapis/java-logging/issues/1409)) ([f9af381](https://github.com/googleapis/java-logging/commit/f9af381b302aeefa401e5bc2f51d97c09f1484e5))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.15.0 ([#1424](https://github.com/googleapis/java-logging/issues/1424)) ([4f82f33](https://github.com/googleapis/java-logging/commit/4f82f339e47014821eca217f5200080e6b78e03f))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.16.1 ([#1434](https://github.com/googleapis/java-logging/issues/1434)) ([e9e9835](https://github.com/googleapis/java-logging/commit/e9e9835e6c7b52364104a1e4a503027efb722422))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.17.0 ([#1444](https://github.com/googleapis/java-logging/issues/1444)) ([748e8a2](https://github.com/googleapis/java-logging/commit/748e8a29026b6eb782a559df207a70555289f906))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.18.0 ([#1454](https://github.com/googleapis/java-logging/issues/1454)) ([dc25a87](https://github.com/googleapis/java-logging/commit/dc25a87cb6e1d64c2e2c811a928ea2553a684daa))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.19.0 ([#1468](https://github.com/googleapis/java-logging/issues/1468)) ([5835a7d](https://github.com/googleapis/java-logging/commit/5835a7dc1c839eb3bc379470846451bd51fdfc24))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.2.0 ([#1269](https://github.com/googleapis/java-logging/issues/1269)) ([e196a80](https://github.com/googleapis/java-logging/commit/e196a802d0d004dcec2ddfb352ed9aebebe68810))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.20.0 ([#1484](https://github.com/googleapis/java-logging/issues/1484)) ([f3227db](https://github.com/googleapis/java-logging/commit/f3227dbbb6ef7f8b16ff4a6d39882f57868915f1))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.21.0 ([#1500](https://github.com/googleapis/java-logging/issues/1500)) ([6cce3c9](https://github.com/googleapis/java-logging/commit/6cce3c9bbe051180789c7ff4fbdde4c45fe46888))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.22.0 ([#1510](https://github.com/googleapis/java-logging/issues/1510)) ([b40e846](https://github.com/googleapis/java-logging/commit/b40e8465590dadec7c9ff26eb27e92c16b059489))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.23.0 ([#1518](https://github.com/googleapis/java-logging/issues/1518)) ([30ba9ed](https://github.com/googleapis/java-logging/commit/30ba9ed687f5469d36138a138f68cd998cf60b53))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.3.0 ([#1282](https://github.com/googleapis/java-logging/issues/1282)) ([58ac608](https://github.com/googleapis/java-logging/commit/58ac608ddbf5803bb394bb4833cf8af0bbb22e91))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.4.0 ([#1290](https://github.com/googleapis/java-logging/issues/1290)) ([84d42ae](https://github.com/googleapis/java-logging/commit/84d42ae6da926785462088de23947bc742f9dc0a))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.5.0 ([#1301](https://github.com/googleapis/java-logging/issues/1301)) ([9fa6f05](https://github.com/googleapis/java-logging/commit/9fa6f05a9ea1444d9abad4e0eae5fd854bb2608c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.6.0 ([#1308](https://github.com/googleapis/java-logging/issues/1308)) ([febcf49](https://github.com/googleapis/java-logging/commit/febcf49085ed0fb6be02aaf9108805dd4cce31b8))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.7.0 ([#1318](https://github.com/googleapis/java-logging/issues/1318)) ([973d260](https://github.com/googleapis/java-logging/commit/973d2601bc1639b09d4dd89dd2b6f90cd1b779e9))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.8.0 ([#1326](https://github.com/googleapis/java-logging/issues/1326)) ([5a56f1b](https://github.com/googleapis/java-logging/commit/5a56f1b5087e65bc097d5c8a85d000d12bbbca8c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.9.0 ([#1342](https://github.com/googleapis/java-logging/issues/1342)) ([8b14ae1](https://github.com/googleapis/java-logging/commit/8b14ae17514481a5925ae3ff079cc4f1b4ad6d94))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.24.0 ([#1526](https://github.com/googleapis/java-logging/issues/1526)) ([235f1aa](https://github.com/googleapis/java-logging/commit/235f1aa380d4f34f65d4cc957b3d26fa6a35e226))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.25.0 ([#1535](https://github.com/googleapis/java-logging/issues/1535)) ([7fde779](https://github.com/googleapis/java-logging/commit/7fde7795f03ac96353912829b42adc0035a41d26))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.27.0 ([#1552](https://github.com/googleapis/java-logging/issues/1552)) ([6c5464d](https://github.com/googleapis/java-logging/commit/6c5464d1c5a74962fcd459a1e03282747e148a44))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.0 ([#1560](https://github.com/googleapis/java-logging/issues/1560)) ([d52e623](https://github.com/googleapis/java-logging/commit/d52e62343aa814183baa4fa8ea39d41a5e7c423f))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#1563](https://github.com/googleapis/java-logging/issues/1563)) ([81aa3e6](https://github.com/googleapis/java-logging/commit/81aa3e6b6662d62844b289a22e8aba50dff36a51))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#1569](https://github.com/googleapis/java-logging/issues/1569)) ([8eb0781](https://github.com/googleapis/java-logging/commit/8eb0781b1e1e6e369a6ff0a03d1db4cd0462a6a7))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.29.0 ([#1586](https://github.com/googleapis/java-logging/issues/1586)) ([edcaf8d](https://github.com/googleapis/java-logging/commit/edcaf8de643a7f7f419ee6059c706d0ef0ef4873))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.30.0 ([#1603](https://github.com/googleapis/java-logging/issues/1603)) ([16967e5](https://github.com/googleapis/java-logging/commit/16967e5ba704a75419904ba2aaabce0cbc116352))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.30.1 ([#1611](https://github.com/googleapis/java-logging/issues/1611)) ([e7a0904](https://github.com/googleapis/java-logging/commit/e7a0904a1faf04b0de400c1778f976494246e39e))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.31.0 ([#1625](https://github.com/googleapis/java-logging/issues/1625)) ([9db8f3b](https://github.com/googleapis/java-logging/commit/9db8f3b948e20fa406f315b670341da2b00f0856))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.32.0 ([#1649](https://github.com/googleapis/java-logging/issues/1649)) ([cb428d1](https://github.com/googleapis/java-logging/commit/cb428d19a1ea750520d336c9d1042d50f3801f15))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.33.0 ([#1664](https://github.com/googleapis/java-logging/issues/1664)) ([cb6de76](https://github.com/googleapis/java-logging/commit/cb6de767ba726a1178b4ebd0b481a4fc2454b910))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.34.0 ([#1677](https://github.com/googleapis/java-logging/issues/1677)) ([dbd050c](https://github.com/googleapis/java-logging/commit/dbd050c354cee5272c37dd323358b222cea5e87e))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.35.0 ([#1683](https://github.com/googleapis/java-logging/issues/1683)) ([31ec2b9](https://github.com/googleapis/java-logging/commit/31ec2b972d5e11e12fe0432f42e3e5b8f23312c6))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#1698](https://github.com/googleapis/java-logging/issues/1698)) ([9491512](https://github.com/googleapis/java-logging/commit/94915125fd2425ffba5ef86da0c54af3c1d2c138))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.37.0 ([#1702](https://github.com/googleapis/java-logging/issues/1702)) ([1f7da17](https://github.com/googleapis/java-logging/commit/1f7da17810fa22b8437edc88e4f95b3ed5cb8349))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#1755](https://github.com/googleapis/java-logging/issues/1755)) ([d404381](https://github.com/googleapis/java-logging/commit/d4043815246423efe542356dc50ba663092b8df0))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#1808](https://github.com/googleapis/java-logging/issues/1808)) ([6327c51](https://github.com/googleapis/java-logging/commit/6327c51f3a8ecfb7af678c8c040b066e7f938863))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#1813](https://github.com/googleapis/java-logging/issues/1813)) ([c15da84](https://github.com/googleapis/java-logging/commit/c15da84716d6d554ae26919412e8d4313fd980bc))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#1848](https://github.com/googleapis/java-logging/issues/1848)) ([162ef56](https://github.com/googleapis/java-logging/commit/162ef563793270c236ecf7ca2524ad3b560d7a12))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#1853](https://github.com/googleapis/java-logging/issues/1853)) ([c21a635](https://github.com/googleapis/java-logging/commit/c21a635f054b1cd8a6e5aea7450017af85ba03c7))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#1858](https://github.com/googleapis/java-logging/issues/1858)) ([0252352](https://github.com/googleapis/java-logging/commit/0252352ca34dd494c4471f3a90391df762d676df))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#1869](https://github.com/googleapis/java-logging/issues/1869)) ([94405fa](https://github.com/googleapis/java-logging/commit/94405fa929c48db114dd10ae39a0f3e520865bbf))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * update dependency io.opentelemetry:opentelemetry-bom to v1.45.0 ([#1638](https://github.com/googleapis/java-logging/issues/1638)) ([7e007d4](https://github.com/googleapis/java-logging/commit/7e007d4f966ed7e9c75cbf0ce951441052e8735c))
  * update dependency io.opentelemetry:opentelemetry-bom to v1.46.0 ([#1747](https://github.com/googleapis/java-logging/issues/1747)) ([5ef2853](https://github.com/googleapis/java-logging/commit/5ef285387d63b79bff7e43b233c7f9770f378dba))
  * update dependency org.apache.maven.plugins:maven-deploy-plugin to v3.1.3 ([2b6ea70](https://github.com/googleapis/java-logging/commit/2b6ea703aad05e714f5634fbd74e0b9bca0c51f9))
  * update dependency org.easymock:easymock to v5.2.0 ([#1421](https://github.com/googleapis/java-logging/issues/1421)) ([f931544](https://github.com/googleapis/java-logging/commit/f9315443ba97104f1a23e5695ed72cb4bd2dfa10))
  * update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.10.0 ([#1528](https://github.com/googleapis/java-logging/issues/1528)) ([b3e4f9b](https://github.com/googleapis/java-logging/commit/b3e4f9b77bffc49a4f9569d4b7a9318a0d5ea5c0))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.20 ([#1279](https://github.com/googleapis/java-logging/issues/1279)) ([296cce1](https://github.com/googleapis/java-logging/commit/296cce153cbd263e620c1fbb028466f62f7251dd))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.21 ([#1319](https://github.com/googleapis/java-logging/issues/1319)) ([5aef8d6](https://github.com/googleapis/java-logging/commit/5aef8d6492c9ebf8e989ee652dcf4a1d82cac8a4))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.22 ([#1340](https://github.com/googleapis/java-logging/issues/1340)) ([b3b9d5f](https://github.com/googleapis/java-logging/commit/b3b9d5ffe078a3203725f3709c1840cb88f6e9ea))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.23 ([#1374](https://github.com/googleapis/java-logging/issues/1374)) ([dce3c4c](https://github.com/googleapis/java-logging/commit/dce3c4c9413c2d1674b6ddaf6fe9351a28f0673a))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.24 ([#1411](https://github.com/googleapis/java-logging/issues/1411)) ([0487cdf](https://github.com/googleapis/java-logging/commit/0487cdff06c0ce9529d4c662991cf84ad25b9f40))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.26 ([#1420](https://github.com/googleapis/java-logging/issues/1420)) ([ff581a6](https://github.com/googleapis/java-logging/commit/ff581a67270777fe15e291794df3b49041c111e3))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.27 ([#1430](https://github.com/googleapis/java-logging/issues/1430)) ([9e750a3](https://github.com/googleapis/java-logging/commit/9e750a3c3685671ee573a7e8190622d7f9002b51))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.28 ([#1455](https://github.com/googleapis/java-logging/issues/1455)) ([3080cec](https://github.com/googleapis/java-logging/commit/3080cec373f8d9d61ce57363553925a07702d552))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.0 ([#1456](https://github.com/googleapis/java-logging/issues/1456)) ([f27713e](https://github.com/googleapis/java-logging/commit/f27713ed55159754715cca5ff205364e315a7c05))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.1 ([#1542](https://github.com/googleapis/java-logging/issues/1542)) ([af784bc](https://github.com/googleapis/java-logging/commit/af784bce7c5272a346ce5016464c87af7d69b442))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.20 ([#1280](https://github.com/googleapis/java-logging/issues/1280)) ([6363196](https://github.com/googleapis/java-logging/commit/63631966432aac89883dd80c0087576454616cc2))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.21 ([#1320](https://github.com/googleapis/java-logging/issues/1320)) ([fc2d065](https://github.com/googleapis/java-logging/commit/fc2d0655e5b3d2ea9aedf1a4fd65fad8cf815462))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.22 ([#1341](https://github.com/googleapis/java-logging/issues/1341)) ([cfc0106](https://github.com/googleapis/java-logging/commit/cfc0106c359c153031bddcac7dadc292a9bb561e))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.23 ([#1375](https://github.com/googleapis/java-logging/issues/1375)) ([a15c73c](https://github.com/googleapis/java-logging/commit/a15c73cbf8c22971f690d38fa87b6b349851d5c8))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.26 ([#1412](https://github.com/googleapis/java-logging/issues/1412)) ([bd9be4e](https://github.com/googleapis/java-logging/commit/bd9be4e8aecd5b7a532a6f2eb91151201a41334f))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.27 ([#1431](https://github.com/googleapis/java-logging/issues/1431)) ([7c2aa2c](https://github.com/googleapis/java-logging/commit/7c2aa2cc3b5651674591dc4e6cb89774d14e6513))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.0 ([#1397](https://github.com/googleapis/java-logging/issues/1397)) ([f15d246](https://github.com/googleapis/java-logging/commit/f15d2462962c261be5726d5a68b6a1d31aa916fc))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.1 ([#1471](https://github.com/googleapis/java-logging/issues/1471)) ([debc77f](https://github.com/googleapis/java-logging/commit/debc77f4ce57d768474c27eb6c056f7c10c7d743))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.2 ([#1530](https://github.com/googleapis/java-logging/issues/1530)) ([20981dc](https://github.com/googleapis/java-logging/commit/20981dc90ca1b73b74d9f5a0c7f0dfa4d9960ab9))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.2 ([#1245](https://github.com/googleapis/java-logging/issues/1245)) ([e73a704](https://github.com/googleapis/java-logging/commit/e73a704fa92d8f2abfe3b979e741b7f00ab89bca))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.3 ([#1329](https://github.com/googleapis/java-logging/issues/1329)) ([dfb98f4](https://github.com/googleapis/java-logging/commit/dfb98f47098d4560fc3ef93f126af1770ae4faf6))
  * update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))
  * update googleapis/sdk-platform-java action to v2.52.0 ([#1753](https://github.com/googleapis/java-logging/issues/1753)) ([3dcf86a](https://github.com/googleapis/java-logging/commit/3dcf86adc3e1ef3d5866cd043149808601c213b8))
  * update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))
  * update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))
  * update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))
  * update googleapis/sdk-platform-java action to v2.58.0 ([#1806](https://github.com/googleapis/java-logging/issues/1806)) ([b94da77](https://github.com/googleapis/java-logging/commit/b94da779d8263ce6c1845bb8baa6a9e9aedc2ccf))
  * update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))
  * update googleapis/sdk-platform-java action to v2.62.1 ([#1855](https://github.com/googleapis/java-logging/issues/1855)) ([b6ce498](https://github.com/googleapis/java-logging/commit/b6ce4988391dba73e019aa9f597ce6cc23f81a8c))
  * update googleapis/sdk-platform-java action to v2.62.3 ([#1868](https://github.com/googleapis/java-logging/issues/1868)) ([cac5cd9](https://github.com/googleapis/java-logging/commit/cac5cd99e6a1738100248c9d235f4fa2987967d0))
  * update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))
  * update sdk platform java dependencies ([#1707](https://github.com/googleapis/java-logging/issues/1707)) ([2359040](https://github.com/googleapis/java-logging/commit/23590409f5c4aaff5c741e860fc0916f7ec4c963))
  * update sdk platform java dependencies ([#1717](https://github.com/googleapis/java-logging/issues/1717)) ([ee9ef91](https://github.com/googleapis/java-logging/commit/ee9ef91a9ebaed9faa5870a29be40b0c1531a226))
  * update sdk platform java dependencies ([#1725](https://github.com/googleapis/java-logging/issues/1725)) ([531f8c5](https://github.com/googleapis/java-logging/commit/531f8c5089a260840eee7ff97d315307f074f5e6))
  * update sdk platform java dependencies ([#1736](https://github.com/googleapis/java-logging/issues/1736)) ([88b4cdf](https://github.com/googleapis/java-logging/commit/88b4cdf71463285e50a815e0635d36301d583e4c))
  * update sdk-platform-java-config to 3.55.0-rc1 ([#1903](https://github.com/googleapis/java-logging/issues/1903)) ([750a9d7](https://github.com/googleapis/java-logging/commit/750a9d7ed49e1134a94cd88819398459b32a815a))



##### Documentation

  * Documentation update for OpenTelemetry and tracing ([#1657](https://github.com/googleapis/java-logging/issues/1657)) ([e3c6670](https://github.com/googleapis/java-logging/commit/e3c667094170ac7d404addc797facbe997ca51d3))
  * Fix typo in code comments ([#1520](https://github.com/googleapis/java-logging/issues/1520)) ([0440fc6](https://github.com/googleapis/java-logging/commit/0440fc6dfa3c5cd19f0d7d941af242872da1bbd3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



## December 15, 2025

Libraries

### Java

#### [3.23.9](https://github.com/googleapis/java-logging/compare/v3.23.8...v3.23.9) (2025-12-11)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.2 ([fcb7ec1](https://github.com/googleapis/java-logging/commit/fcb7ec1ba7ae7c9a041d68c76e7b72a7e0861cf7))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.2 ([#1897](https://github.com/googleapis/java-logging/issues/1897)) ([ab9862f](https://github.com/googleapis/java-logging/commit/ab9862f655bc89fa3e4e381567dcd0a9d8afdbf9))
  * Update googleapis/sdk-platform-java action to v2.64.2 ([#1898](https://github.com/googleapis/java-logging/issues/1898)) ([5860f51](https://github.com/googleapis/java-logging/commit/5860f516596686ef3054969b8c69de7eb48629e3))



## December 12, 2025

Change

The default setting for the time-range selector for the Logs Explorer is now five minutes. The previous default was one hour.

## December 08, 2025

Feature

You can now install and manage the Ops Agent on virtual machines in a specified zone by using VM Extension Manager extension policies. You can use extension policies to keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

## November 17, 2025

Libraries

### Java

#### [3.23.8](https://github.com/googleapis/java-logging/compare/v3.23.7...v3.23.8) (2025-11-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * Update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))



### Java

#### [3.23.8](https://github.com/googleapis/java-logging/compare/v3.23.7...v3.23.8) (2025-11-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * Update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))



## November 03, 2025

Libraries

### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



## October 27, 2025

Libraries

### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



## October 13, 2025

Libraries

### Java

#### [3.23.6](https://github.com/googleapis/java-logging/compare/v3.23.5...v3.23.6) (2025-10-08)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([5d5d8a7](https://github.com/googleapis/java-logging/commit/5d5d8a76c58c3329f90e4fa84f5e81a1d3296894))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#1869](https://github.com/googleapis/java-logging/issues/1869)) ([94405fa](https://github.com/googleapis/java-logging/commit/94405fa929c48db114dd10ae39a0f3e520865bbf))
  * Update googleapis/sdk-platform-java action to v2.62.3 ([#1868](https://github.com/googleapis/java-logging/issues/1868)) ([cac5cd9](https://github.com/googleapis/java-logging/commit/cac5cd99e6a1738100248c9d235f4fa2987967d0))



## October 09, 2025

Feature

The query builder in the Log Analytics page is [generally available](https://docs.cloud.google.com/products#product-launch-stages) (GA). For more information, see [Build, edit, and run a query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

## September 29, 2025

Libraries

### Java

#### [3.23.5](https://github.com/googleapis/java-logging/compare/v3.23.4...v3.23.5) (2025-09-24)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([eeca440](https://github.com/googleapis/java-logging/commit/eeca440da06c24afc07e669f6f087246d91cd933))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#1858](https://github.com/googleapis/java-logging/issues/1858)) ([0252352](https://github.com/googleapis/java-logging/commit/0252352ca34dd494c4471f3a90391df762d676df))



## September 22, 2025

Announcement

Cloud Logging has removed the quota for write requests per minute, which has been replaced by volume-based regional quotas. We've also removed the references to August dates for the removal of the old quota from the public documentation. For more information, see [Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits).

## September 15, 2025

Libraries

### Java

#### [3.23.4](https://github.com/googleapis/java-logging/compare/v3.23.3...v3.23.4) (2025-09-11)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([1438bff](https://github.com/googleapis/java-logging/commit/1438bff5bc7028fbf125895f0bdd2bb50490effa))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#1853](https://github.com/googleapis/java-logging/issues/1853)) ([c21a635](https://github.com/googleapis/java-logging/commit/c21a635f054b1cd8a6e5aea7450017af85ba03c7))
  * Update googleapis/sdk-platform-java action to v2.62.1 ([#1855](https://github.com/googleapis/java-logging/issues/1855)) ([b6ce498](https://github.com/googleapis/java-logging/commit/b6ce4988391dba73e019aa9f597ce6cc23f81a8c))



## September 08, 2025

Libraries

### Node.js

#### [11.2.1](https://github.com/googleapis/nodejs-logging/compare/v11.2.0...v11.2.1) (2025-09-03)

##### Bug Fixes

  * **logging:** Specifying resourceNames should fetch logs only from those resources ([#1597](https://github.com/googleapis/nodejs-logging/issues/1597)) ([ff7899f](https://github.com/googleapis/nodejs-logging/commit/ff7899f5e91da6540d3f68476b2d9acd58ff0993))



## August 25, 2025

Libraries

### Java

#### [3.23.3](https://github.com/googleapis/java-logging/compare/v3.23.2...v3.23.3) (2025-08-20)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#1848](https://github.com/googleapis/java-logging/issues/1848)) ([162ef56](https://github.com/googleapis/java-logging/commit/162ef563793270c236ecf7ca2524ad3b560d7a12))



## August 11, 2025

Libraries

### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



## August 04, 2025

Libraries

### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



Feature

You can now build queries without manually writing SQL in the Log Analytics page by using the query builder. This feature is in Public Preview. For more information, see [Build and run a SQL query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

## July 14, 2025

Libraries

### Java

#### [3.23.0](https://github.com/googleapis/java-logging/compare/v3.22.6...v3.23.0) (2025-07-11)

##### Features

  * Next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))



### Java

#### [3.23.0](https://github.com/googleapis/java-logging/compare/v3.22.6...v3.23.0) (2025-07-11)

##### Features

  * Next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))



## June 30, 2025

Libraries

### Java

#### [3.22.6](https://github.com/googleapis/java-logging/compare/v3.22.5...v3.22.6) (2025-06-25)

##### Bug Fixes

  * Regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))



### Java

#### [3.22.6](https://github.com/googleapis/java-logging/compare/v3.22.5...v3.22.6) (2025-06-25)

##### Bug Fixes

  * Regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))



## June 09, 2025

Libraries

### Java

#### [3.22.5](https://github.com/googleapis/java-logging/compare/v3.22.4...v3.22.5) (2025-06-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([f2362fb](https://github.com/googleapis/java-logging/commit/f2362fb4c05d34fda4a1c9788ea87822ac887d9e))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#1813](https://github.com/googleapis/java-logging/issues/1813)) ([c15da84](https://github.com/googleapis/java-logging/commit/c15da84716d6d554ae26919412e8d4313fd980bc))



## June 06, 2025

Announcement

Cloud Logging begins enforcement of the new volume-based regional quotas. For more information, see [Logging API quotas and limits](https://docs.cloud.google.com/logging/quotas#api-limits).

## June 04, 2025

Feature

You can now cancel a running query in the Logs Explorer by clicking the **Stop query** button.

## May 29, 2025

Feature

You can now configure the observability scope or set the default log scope by using the Google Cloud CLI. You must use version 254.0 or higher. For more information, see [Configure observability scopes](https://docs.cloud.google.com/stackdriver/docs/scopes/configure) and [Set the default log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#set-default).

## May 26, 2025

Libraries

### Java

#### [3.22.4](https://github.com/googleapis/java-logging/compare/v3.22.3...v3.22.4) (2025-05-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([45b4878](https://github.com/googleapis/java-logging/commit/45b4878eeec35f8c19a3cd3cd33331e9ece6b5c6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#1808](https://github.com/googleapis/java-logging/issues/1808)) ([6327c51](https://github.com/googleapis/java-logging/commit/6327c51f3a8ecfb7af678c8c040b066e7f938863))
  * Update googleapis/sdk-platform-java action to v2.58.0 ([#1806](https://github.com/googleapis/java-logging/issues/1806)) ([b94da77](https://github.com/googleapis/java-logging/commit/b94da779d8263ce6c1845bb8baa6a9e9aedc2ccf))



## May 12, 2025

Libraries

### Java

#### [3.22.3](https://github.com/googleapis/java-logging/compare/v3.22.2...v3.22.3) (2025-05-06)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * Update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))



### Java

#### [3.22.3](https://github.com/googleapis/java-logging/compare/v3.22.2...v3.22.3) (2025-05-06)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * Update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))



## May 08, 2025

Feature

Log Analytics can now automatically infer fields of a column when the data type is JSON. You can also view how often these inferred fields appear in your data.

## April 28, 2025

Libraries

### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Java

#### [3.22.2](https://github.com/googleapis/java-logging/compare/v3.22.1...v3.22.2) (2025-04-25)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Java

#### [3.22.1](https://github.com/googleapis/java-logging/compare/v3.22.0...v3.22.1) (2025-04-25)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



Libraries

### Java

#### [3.22.2](https://github.com/googleapis/java-logging/compare/v3.22.1...v3.22.2) (2025-04-25)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))



Libraries

### Java

#### [3.22.1](https://github.com/googleapis/java-logging/compare/v3.22.0...v3.22.1) (2025-04-25)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))



## April 21, 2025

Libraries

### Python

#### [3.12.0](https://github.com/googleapis/python-logging/compare/v3.11.4...v3.12.0) (2025-04-10)

##### Features

  * Add REST Interceptors which support reading metadata ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Add support for opt-in debug logging ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Added flushes/close functionality to logging handlers ([#917](https://github.com/googleapis/python-logging/issues/917)) ([d179304](https://github.com/googleapis/python-logging/commit/d179304b344277e349456f72cd90c56f28011286))



##### Bug Fixes

  * Allow protobuf 6.x ([#977](https://github.com/googleapis/python-logging/issues/977)) ([6757890](https://github.com/googleapis/python-logging/commit/675789001344fdae68ee20ec14e14c11c83a0433))
  * **deps:** Require google-cloud-audit-log >= 0.3.1 ([#979](https://github.com/googleapis/python-logging/issues/979)) ([1cc00ec](https://github.com/googleapis/python-logging/commit/1cc00ecf646a7a36eb32afd2e5df3d9aa7f564b1))
  * Fix typing issue with gRPC metadata when key ends in -bin ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))



##### Documentation

  * Added documentation on log_level and excluded_loggers params in setup_logging ([#971](https://github.com/googleapis/python-logging/issues/971)) ([70d9d25](https://github.com/googleapis/python-logging/commit/70d9d25bf8c3c85a3c5523ecc7fbdbf72f08c583))
  * Update README to break infinite redirect loop ([#972](https://github.com/googleapis/python-logging/issues/972)) ([52cd907](https://github.com/googleapis/python-logging/commit/52cd907bb313df2766ec11e3d24c7e10cda31ca7))



### Python

#### [3.12.0](https://github.com/googleapis/python-logging/compare/v3.11.4...v3.12.0) (2025-04-10)

##### Features

  * Add REST Interceptors which support reading metadata ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Add support for opt-in debug logging ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Added flushes/close functionality to logging handlers ([#917](https://github.com/googleapis/python-logging/issues/917)) ([d179304](https://github.com/googleapis/python-logging/commit/d179304b344277e349456f72cd90c56f28011286))



##### Bug Fixes

  * Allow protobuf 6.x ([#977](https://github.com/googleapis/python-logging/issues/977)) ([6757890](https://github.com/googleapis/python-logging/commit/675789001344fdae68ee20ec14e14c11c83a0433))
  * **deps:** Require google-cloud-audit-log >= 0.3.1 ([#979](https://github.com/googleapis/python-logging/issues/979)) ([1cc00ec](https://github.com/googleapis/python-logging/commit/1cc00ecf646a7a36eb32afd2e5df3d9aa7f564b1))
  * Fix typing issue with gRPC metadata when key ends in -bin ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))



##### Documentation

  * Added documentation on log_level and excluded_loggers params in setup_logging ([#971](https://github.com/googleapis/python-logging/issues/971)) ([70d9d25](https://github.com/googleapis/python-logging/commit/70d9d25bf8c3c85a3c5523ecc7fbdbf72f08c583))
  * Update README to break infinite redirect loop ([#972](https://github.com/googleapis/python-logging/issues/972)) ([52cd907](https://github.com/googleapis/python-logging/commit/52cd907bb313df2766ec11e3d24c7e10cda31ca7))



Announcement

Cloud Logging adds support for the `europe-north2` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## April 17, 2025

Feature

In the Logs Explorer, you can now view the most frequently occurring fields and values in the JSON payload of your logs. For more information, see the [**Fields** pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel) documentation.

## April 04, 2025

Feature

You can include pipe syntax in the SQL queries you run on the [Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) page. [Pipe syntax](https://docs.cloud.google.com/bigquery/docs/pipe-syntax-guide) supports a linear query structure designed to make your queries easier to read, write, and maintain. The pipe syntax feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## March 24, 2025

Libraries

### Java

#### [3.22.0](https://github.com/googleapis/java-logging/compare/v3.21.4...v3.22.0) (2025-03-18)

##### Features

  * Next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))



### Java

#### [3.22.0](https://github.com/googleapis/java-logging/compare/v3.21.4...v3.22.0) (2025-03-18)

##### Features

  * Next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))



## March 13, 2025

Feature

[App Hub application](https://docs.cloud.google.com/app-hub/docs/overview) labels are now attached to your log entries. The **Log Fields** pane of the **Logs Explorer** now includes facets for application, service, and workload labels. For more information, see [**Log Fields** pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel).

## March 12, 2025

Feature

You can now use the Observability API to set the default log scope. This feature is in Public Preview. For more information, see the following documents:

  * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage)
  * [Observability scopes overview](https://docs.cloud.google.com/stackdriver/docs/scopes/configure)
  * [Observability API reference](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest)



## March 11, 2025

Change

The API to create and manage Log Scopes is now Generally Available (GA). You can create and manage log scopes by using the Cloud Console, the Google Cloud CLI, and Terraform. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

## March 03, 2025

Libraries

### Java

#### [3.21.4](https://github.com/googleapis/java-logging/compare/v3.21.3...v3.21.4) (2025-02-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * Update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))



### Java

#### [3.21.4](https://github.com/googleapis/java-logging/compare/v3.21.3...v3.21.4) (2025-02-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * Update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))



## February 18, 2025

Feature

You can now use custom constraints with Organization Policy to provide more granular control over your Cloud Logging resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/logging/docs/custom-constraints).

## February 17, 2025

Libraries

### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



## February 06, 2025

Feature

You can now create and manage your log views by using the Google Cloud console. For more information, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## February 03, 2025

Libraries

### Java

#### [3.21.2](https://github.com/googleapis/java-logging/compare/v3.21.1...v3.21.2) (2025-01-29)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#1755](https://github.com/googleapis/java-logging/issues/1755)) ([d404381](https://github.com/googleapis/java-logging/commit/d4043815246423efe542356dc50ba663092b8df0))
  * Update dependency io.opentelemetry:opentelemetry-bom to v1.46.0 ([#1747](https://github.com/googleapis/java-logging/issues/1747)) ([5ef2853](https://github.com/googleapis/java-logging/commit/5ef285387d63b79bff7e43b233c7f9770f378dba))
  * Update googleapis/sdk-platform-java action to v2.52.0 ([#1753](https://github.com/googleapis/java-logging/issues/1753)) ([3dcf86a](https://github.com/googleapis/java-logging/commit/3dcf86adc3e1ef3d5866cd043149808601c213b8))



Libraries

### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



## January 21, 2025

Announcement

On April 22, 2025, Cloud Logging will replace the single, global quota for the number of calls to write log entries with a set of volume-based regional quotas. For more information, see [Logging API quotas and limits](https://docs.cloud.google.com/logging/quotas#api-limits).

## January 20, 2025

Libraries

### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



## January 13, 2025

Feature

You can now create analytics views, which let you transform your log data into a custom format. You can then use SQL to query your analytics views. This feature is in Public Preview. For more information, see the following documents:

  * [About analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views)
  * [Create, query, and manage analytics views](https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views)



## January 06, 2025

Libraries

### Go

#### [1.13.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.12.0...logging/v1.13.0) (2025-01-02)

##### Features

  * **logging:** Change go gapic transport to grpc+rest in logging ([#11289](https://github.com/googleapis/google-cloud-go/issues/11289)) ([a5f250b](https://github.com/googleapis/google-cloud-go/commit/a5f250baf8085bdb07807869a7c4a3a0ca3f535d))



##### Bug Fixes

  * **logging:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))
  * **logging:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **logging:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



### Go

#### [1.13.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.12.0...logging/v1.13.0) (2025-01-02)

##### Features

  * **logging:** Change go gapic transport to grpc+rest in logging ([#11289](https://github.com/googleapis/google-cloud-go/issues/11289)) ([a5f250b](https://github.com/googleapis/google-cloud-go/commit/a5f250baf8085bdb07807869a7c4a3a0ca3f535d))



##### Bug Fixes

  * **logging:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))
  * **logging:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **logging:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



## December 18, 2024

Feature

You can now create custom roles that let you create and manage Log Scopes. Log Scopes are in Public Preview. For more information, see [Create and manage log scopes: Before you begin](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#before-you-begin).

Announcement

Cloud Logging adds support for the `northamerica-south1` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## December 13, 2024

Feature

Reporting of the "pending" status of the Ops Agent on the Cloud Monitoring **VM Instances** dashboard has been refined to include additional states. For more information, see [Use **VM Instances** dashboard](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#verify-agent-running-with-vm-instance-dashboard).

## December 06, 2024

Feature

Editing Log Analytics charts that are saved to a dashboard directly in the **Dashboards** page is now generally available (GA).

## November 08, 2024

Change

Audit Logging now populates the [`status.details`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog#status) field in the audit log with the `google.rpc.ErrorInfo` and `google.rpc.Help` proto payload types in cases where an API returns an error status and that status includes one of those types in the details field.

## October 29, 2024

Feature

You can now create and manage log scopes by using the Google Cloud CLI, in addition to using the Cloud Console and Terraform. Log scopes are in Public Preview. For more information, see

  * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage)
  * [gcloud logging scopes](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes)



## October 28, 2024

Feature

You can now use tags to annotate your log buckets and use the tags to manage access to the log buckets. For more information, see [Manage log buckets by using tags](https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags).

## October 24, 2024

Feature

You can now create alerting policies that monitor the results of your SQL queries. For more information about SQL-based alerting policies, see the following documents:

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Manage incidents for SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/sql-based-incidents)



## October 09, 2024

Change

Ops Agent release 2.51.0 adds support for Compute Engine Arm VMs that are running Rocky Linux 8.

## October 07, 2024

Feature

You can now include pipe syntax in the SQL queries you run on the Log Analytics page. For more information, see the BigQuery documentation about [pipe syntax](https://docs.cloud.google.com/bigquery/docs/pipe-syntax).

## October 02, 2024

Feature

You can now use Terraform commands to a create or update a log scope. For more information, see [Create a log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#create).

## September 30, 2024

Change

The layout of the Logs Explorer page has been changed. For more information, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Change

The pricing for vended network logs has changed. For more information see the following:

  * [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary)
  * [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs)
  * [Network telemetry log pricing](https://docs.cloud.google.com/vpc/network-pricing#network-telemetry)



## September 19, 2024

Feature

You can now query your log data from the Log Analytics page by using reserved BigQuery slots. For more information, see [Query and view logs in Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

## September 16, 2024

Feature

There is a new Cloud Observability Overview page in the Google Cloud console. The new page, which you can customize, introduces the Cloud Observability products, and provides information about your logs, dashboards, incidents, and more. This page can help you detect issues in your resources, view relevant events, and view signals that matter to you.

Feature

You can now create and manage your log scopes by using the Logging API in addition to using the Cloud Console. This feature is in public preview. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

## August 13, 2024

Feature

Introducing log scopes. Log scopes are persistent, project-level resources that list a set of resources to be searched for log entries. For example, you might configure a log scope to contain multiple projects and several log views. If you select your log scope when using the Logs Explorer, it displays the log entries that originate in the specified projects and those in the specified log views.

You can create, edit, and delete log scopes. You can also set one log scope as the default log scope, which determines the resources that the Logs Explorer searches for log entries.

For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

## July 19, 2024

Feature

The [permissions](https://docs.cloud.google.com/logging/docs/access-control#saved-queries) required to use saved and recent queries have changed. You can also define a location in your [default resource settings](https://docs.cloud.google.com/logging/docs/default-settings) where saved and recent queries are saved. This location must align with your organization policy.

## July 08, 2024

Change

Log buckets in all regions supported by Cloud Logging can now be upgraded to use Log Analytics. For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## July 03, 2024

Change

Agent-installation policies for the Ops Agent are now GA. For more information, see [Overview of agent policies for the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies-overview).

Feature

You can now view the estimated number of byte processed along with the validation status of your SQL query when running queries in Log Analytics. You can use this information to understand the relative volume of data that your SQL query will scan.

## June 26, 2024

Feature

You can now analyze your billable log volume when using Log Analytics. This feature is in Public Preview. For more information, see [Analyze log volume with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/log-volume).

## June 25, 2024

Feature

Ops Agent version 2.48.0 introduces support for Compute Engine VMs that are running Deep Learning VM Images based on Debian 11 (Bullseye). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## June 24, 2024

Feature

Gauges and scorecards are now available to visualize the results of your SQL queries. For more information, see [Chart query results with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/charts).

## June 13, 2024

Feature

You can now use Terraform commands to attach an IAM role binding to a log view that grants a principal access to the log view. For more information about log views and about controlling access to log views, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## May 29, 2024

Change

Ops Agent version 2.47.0 introduces support for Compute Engine VMs that are running Ubuntu 24.04 LTS (Noble Numbat). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## May 15, 2024

Change

You can now attach an IAM role binding to a log view that grants a principal access to the log view. For more information about log views and about controlling access to log views, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## April 03, 2024

Feature

The Logging query language now supports the `cast` and `regexp_extract` functions. For more information, see the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) documentation.

## March 28, 2024

Feature

Pie charts are now available for visualizing data in the **Log Analytics** page. For more information, see [Change chart type](https://docs.cloud.google.com/logging/docs/analyze/charts#change_chart_type).

## March 26, 2024

Feature

You can now configure your aggregated sink to be intercepting, which prevents logs from being passed through the Log Router of child resources. For more information, see [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

Change

Duet AI in Google Cloud is now Gemini for Google Cloud. See our [blog post](https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/) for more information.

## March 11, 2024

Change

You can now use SQL `JOIN` and `UNION` operators on the **Log Analytics** page to combine tables in multiple Google Cloud projects.

## March 07, 2024

Change

Log buckets in the `africa-south1` region can now be upgraded to use Log Analytics. For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## February 20, 2024

Feature

You can now configure and save a Log Analytics chart directly in Monitoring. For more information, see [Add charts generated from a Log Analytics query](https://docs.cloud.google.com/monitoring/charts/view-logs#add-sql-chart).

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java)



## February 13, 2024

Feature

[Copying log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) is now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

## February 12, 2024

Feature

You can now display Log Analytics query results as a table in your Monitoring dashboards by selecting **Table** as the widget type.

## February 08, 2024

Change

You can now create log buckets in the `africa-south1` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## February 07, 2024

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * europe-west10



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## January 31, 2024

Fixed

Fixed a bug that caused the audit log associated with an API that performs both Data Access and Admin Activity operations to be classified as a Data Access log. These logs are now always classified as Admin Activity audit logs.

## January 16, 2024

Feature

You can now edit Log Analytics charts that are saved to a dashboard directly in the **Dashboards** page. For more information, see [Edit a chart saved to a custom dashboard](https://docs.cloud.google.com/logging/docs/analyze/charts#edit_a_chart_saved_to_a_custom_dashboard).

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

## January 08, 2024

Feature

You can now go to the Log Analytics page from the Logs Explorer page by clicking the **Analyze results** button, which automatically translates the Logging query language query into a SQL query. For more information, see [Analyze results](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#analyze-results).

## December 13, 2023

Feature

Charting in the **Log Analytics** page is now generally available (GA). In addition to features available in the preview, the GA release includes the ability to select `none` as an aggregation function on a chart.

## December 05, 2023

Feature

You can now query for a specific error group in the **Logs Explorer** and **Log Analytics** pages by using the error group ID. For more information, see [Find error group details for a log entry](https://docs.cloud.google.com/logging/docs/analyze/find-logs-error-groups#details).

## December 01, 2023

Feature

Ops Agent version 2.44.0 introduces the following features:

  * Support for Compute Engine VMs that are running Ubuntu 23.10 (Mantic Minotaur). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).
  * Support for Compute Engine Arm VMs that are running Debian 12 (Bookworm). For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).
  * An option to prevent the agent from collecting self logs and sending them to Cloud Logging. For more information, see [Collection of self logs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#self-log-collection).



## November 29, 2023

Feature

You can now specify an inclusion filter or exclusion filter that is applied to the `_Default` sinks of new resources. For more information, see [Configure default filter of `_Default` sinks](https://docs.cloud.google.com/logging/docs/default-settings#default-sink-filter).

## November 10, 2023

Feature

You can now load saved queries in the **Log Analytics** page by using the **Load** button. The **Load** button lets you edit the query in the **Query** pane before running the query.

## November 06, 2023

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * me-central2



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## November 02, 2023

Feature

You can now set a custom time interval for charts in the **Log Analytics** page. The custom time interval can be specified in minutes, hours, or days.

## November 01, 2023

Feature

[Summarizing log entries with Duet AI assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-duet-ai) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## October 24, 2023

Feature

Ops Agent version 2.43.0 introduces support for Compute Engine Arm VMs that are running SLES 15 and OpenSUSE Leap 15. For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## October 16, 2023

Change

You can now create log buckets in the us-west8 region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## October 12, 2023

Change

You can now configure the format of the timestamp in your query results in the **Logs Explorer**. For more information, see [Logs Explorer overview: Configure the Time column](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#customize_time).

## October 09, 2023

Change

When you install the Ops Agent on a Compute Engine VM by using the Cloud Monitoring **VM Instances** dashboard or the **Observability** tab on a Compute Engine VM details page, the agent is now installed with an Ops Agent OS policy. This installation method replaces the prior set of manual steps. For more information, see [Installing the agent by using the Google Cloud console](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#gce-ui-install).

## September 29, 2023

Issue

Ops Agent versions 2.39.0 and 2.40.0 crash if you use them on Compute Engine VMs with attached GPUs. Use Ops Agent version 2.38.0, or versions 2.41.0 and newer, on VMs with attached GPUs.

## September 18, 2023

Feature

You can now save charts generated from a Log Analytics SQL query to a custom dashboard. For more information, see [Save a chart to a custom dashboard](https://docs.cloud.google.com/logging/docs/analyze/charts#save-chart-dashboard).

Change

You can now customize the **Logs Dashboard** page by using custom dashboards. For more information, see [Visualize log severity and error metrics](https://docs.cloud.google.com/logging/docs/view/dashboard).

Change

You can now use the **Log fields** pane of the **Logs Explorer** to filter your Kubernetes Container logs by their service name. The service name is extracted from the value of the `pod_name` label. For more information, see [Logs fields pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel).

## September 12, 2023

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * us-east5
  * us-south1
  * me-central1
  * europe-west12



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## August 29, 2023

Feature

[Summarizing log entries with Duet AI assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-duet-ai) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## August 21, 2023

Feature

You can now view your query results as a chart in the **Log Analytics** page. For more information, see [Chart query results with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/charts).

Feature

Identity and Access Management (IAM) deny policies can now include Cloud Logging permissions. For a list of Cloud Logging permissions that are supported by deny policies, see [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

## August 16, 2023

Change

The behavior of simple text searches as changed. To improve the performance, the [Search function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions) is automatically invoked when you don't wrap the search terms in double quotes.

## August 14, 2023

Feature

Version 2.37.0 of the Ops Agent introduces runtime health checks for errors in the configuration of logging pipelines and in parsing logs. These errors are reported to Cloud Logging. For more information, see [Agent health checks](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

## August 07, 2023

Change

Cloud Logging now supports the following regions:

  * europe-west10
  * europe-west12
  * me-central2



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## August 01, 2023

Feature

Ops Agent version 2.36.0 introduces support for Compute Engine Arm VMs that are running Debian 11 (Bullseye). For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## July 26, 2023

Change

Starting with version 2.35.0, the Ops Agent health-check log is renamed `ops-agent-health`; earlier versions of the Ops Agent that support health checks use the name `ops-agent-health-checks`.

## July 21, 2023

Feature

You can now view logs that are stored in log buckets in different projects by using the **Refine scope** button in the **Logs Explorer**. For more information, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

Change

The Cloud Logging agent for Windows version 1-21 is now available. This version has no user-visible changes but upgrades the `grpc` gem and others to fix vulnerabilities. This also includes the switch to Ruby 3, from version 1-20 of the Logging agent.

## July 20, 2023

Change

Support for routing your logs through the Log Router of another Google Cloud project is now Generally Available (GA). For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## July 19, 2023

Change

The pricing language for Cloud Logging has changed; however, the free allotments and the rates haven't changed. For more information, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).

## July 18, 2023

Change

You can now upgrade log buckets in **most** regions to use Log Analytics. To determine if the region of a log bucket is supported, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## July 10, 2023

Feature

Time ranges are now synchronized between select Logging and Monitoring pages.

## July 06, 2023

Feature

The Google Cloud console can now automatically install the Ops Agent for you when you create a VM instance. During the installation process, the Compute Engine VM Manager creates an Ops Agent OS policy that installs the agent and reinstalls it when necessary. For more information, see [Install the Ops Agent during VM creation](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation).

## June 20, 2023

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * asia-east1
  * europe-north1
  * northamerica-northeast2
  * us-east4



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## June 12, 2023

Feature

You can now create log sinks with user-defined service accounts. For more information, see [Configure log sinks with user-managed service accounts](https://docs.cloud.google.com/logging/docs/routing/user-managed-service-accounts).

## June 05, 2023

Feature

You can now configure CMEK and a default storage location for individual folders, in addition to organizations. For more information, see [Configure default settings for organizations and folders](https://docs.cloud.google.com/logging/docs/default-settings) and [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## May 31, 2023

Change

Cloud Logging no longer creates a dedicated service account for each log sink. Instead, Logging reuses an existing service account when one is available for the resource type. Logging creates a service account when none are available. For more information, see [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#dest-auth).

## May 22, 2023

Feature

You can now use SQL `JOIN` and `UNION` operators in queries on the **Log Analytics** page. For more information, see [Combine data from multiple sources](https://docs.cloud.google.com/logging/docs/analyze/examples#multi-query-ops).

## May 19, 2023

Change

Log buckets with Log Analytics enabled now support the use of Customer Managed Encryption Keys (CMEK). For information about enabling Log Analytics on log buckets, see [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket) or [Upgrade a bucket to use Log Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

## May 15, 2023

Feature

You can now customize the time range of your queries in the **Log Analytics** page by using the time-range selector. There are several time range options, such as preset times, custom start and end times, and relative time ranges. For more information, see [Filter by time](https://docs.cloud.google.com/logging/docs/analyze/examples#filter-time).

## April 26, 2023

Feature

Version 2.31.0 of the Ops Agent introduces built-in support for log rotation. For more information, see [Configure log rotation in the Ops Agent](https://stackdriver/docs/solutions/agents/ops-agent/rotate-logs#configure-log-rotation).

## April 18, 2023

Feature

You can now configure Log Analytics on Cloud Logging buckets and BigQuery linked datasets by using the following Terraform modules:

  * [google_logging_project_bucket_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_project_bucket_config)

  * [google_logging_linked_dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_linked_dataset)




## April 11, 2023

Change

The Logging Query Language now supports a built-in `SEARCH` function that you can use to find strings in your log data. The `SEARCH` function is now GA. For more information, see [`SEARCH` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions).

## March 31, 2023

Change

Effective 1 April 2023, storage costs apply to logs data retained longer than 30 days. For pricing details, see [ Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary). Prior to 1 April 2023, there are no charges for retaining logs longer than 30 days. To review the billable storage for your log buckets, go to the **Logs Storage** page of the Google Cloud console.

## March 29, 2023

Change

When you create a [log view](https://docs.cloud.google.com/logging/docs/logs-views) and use the [`source()`](https://docs.cloud.google.com/logging/docs/view/logging-query-language#source) function in your filter, the argument to the function is now validated to ensure that it is a single string representing a project, folder, billing account or organization.

## March 27, 2023

Feature

The Cloud Logging API now supports the following region:

  * Doha: `me-central1`



## March 22, 2023

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * `asia-northeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `northamerica-northeast1`
  * `us-east1`
  * `us-west2`



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## March 14, 2023

Feature

The Logging Query Language now supports a built-in `SEARCH` function that you can use to find strings in your log data. The `SEARCH` function is in preview. For more information, see [`SEARCH` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions).

## March 10, 2023

Feature

Starting with version 2.28.0, the Ops Agent limits the amount of disk space it can use to store buffer chunks. The Ops Agent creates buffer chunks when logging data can't be sent to the Logging API. Without a limit, these chunks might consume all available space, interrupting other services on the VM. When a network outage causes buffer chunks to be written to disk, the Ops Agent now uses a platform-specific amount of disk space to store the chunks.

Feature

[Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm) are now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA). In addition to features available in the preview, the GA release includes the ability to create bucket-level log-based metrics in the Google Cloud console.

## March 09, 2023

Feature

You can now route logs through the Log Router of another Google Cloud project. The logs can then be managed by the other Google Cloud project, which includes log-based metrics, log-based alerts, and other log sinks. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## March 01, 2023

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * `us-central1`
  * `us-west1`
  * `asia-south1`



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

Change

You can now use the gcloud CLI to do the following:

  * Create a log bucket and upgrade that bucket to use Log Analytics.
  * Upgrade an existing log bucket to use Log Analytics.
  * Create a linked dataset in BigQuery.



For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

## February 23, 2023

Feature

The time-range selector in the Logs Explorer has been updated to support a larger set of time range options, such as preset times, custom start and end times, and relative time ranges. For more information, see [Use the time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range).

## February 17, 2023

Feature

You can create log buckets that use Log Analytics and upgrade existing log buckets to use Log Analytics by using the Logging API. For more information, see [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#api).

## February 16, 2023

Feature

Version 2.25.1 of the Ops Agent introduces health checks. When the Ops Agent starts, it performs a series of checks for conditions that prevent the agent from running correctly. If the agent detects one of the conditions, it writes a message to its health-check log and exits. For more information, see [Find Ops Agent troubleshooting information](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info).

## February 01, 2023

Change

To help you manage your costs, the **Logs Storage** page now displays the billable storage for the current month for each log bucket. For reference, this page also displays each log bucket's ingested bytes for the current and previous months.

## January 17, 2023

Change

You can now save your SQL queries, and you can set custom retention periods on log buckets upgraded to use Log Analytics. For more information, see [Save a query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#save-query).

Change

Log Analytics is now GA. For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

## December 19, 2022

Feature

Cloud Logging now supports the following regions:

  * `US`

  * `EU`




For more information, see [Data regionality for Cloud Logging](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## November 07, 2022

Feature

You can now dynamically include your log content in your alert notifications for easier troubleshooting. For more information about extracting log content into labels, see [Create a log-based alert (Monitoring API)](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

## November 04, 2022

Feature

The **Logs** tab available for each cluster on the **Kubernetes Engine > Clusters** page now includes suggested queries for your logs. For more information about using your GKE logs, see [Viewing your GKE logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs#accessing_your_logs).

## November 03, 2022

Change

You can now collect Aerospike logs from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Aerospike](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/aerospike).

## October 24, 2022

Feature

You can now instrument gRPC applications to use [Microservices observability](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

## October 21, 2022

Feature

To show or hide log entries similar to a log entry displayed in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), expand the log entry and use the **Similar entries** menu.

## October 04, 2022

Feature

You can now collect Oracle Database logs and metrics from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Oracle Database](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/oracledb).

## September 27, 2022

Feature

Using Log Analytics, you can run SQL queries that analyze your log data to generate useful insights. Log Analytics also let you use [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) to query your log data. For more information, see [Log Analytics](https://docs.cloud.google.com/logging/docs/log-analytics).

## September 20, 2022

Feature

The Cloud Logging API now supports the following region:

  * Israel: `me-west1`.



## September 15, 2022

Change

Support for adding [custom indexed `LogEntry` fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) to your Cloud Logging buckets is now Generally Available. These indexes make querying your logs data faster.

## September 08, 2022

Change

Cloud Audit Logging no longer redacts the principal email associated with service accounts in audit logs. For more information, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).

## August 15, 2022

Feature

Bucket-level log-based metrics are now available in [Preview](https://cloud.google.com/products#product-launch-stages). You can now create log-based metrics that are computed from the logs routed to a specific log bucket. For more information, see [Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

## August 04, 2022

Feature

The Logs Explorer query results now show an icon for log entries that are part of error groups. You can click the icon to view details about the error group, exclude or show only log entries from the error group in the query results, or view related documentation. For more information, see [Find log entries with error groups](https://docs.cloud.google.com/logging/docs/analyze/find-logs-error-groups).

## July 26, 2022

Feature

You can now collect Couchbase logs and metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Couchbase](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase).

## July 18, 2022

Feature

You can now search your correlated log entries in the Logs Explorer. For more information, see [Correlate log entries](https://docs.cloud.google.com/logging/docs/view/correlate-logs).

## July 15, 2022

Feature

You can now collect SAP HANA logs and metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: SAP HANA](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana).

Feature

You can now collect Vault logs from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: Vault](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party#vault).

## July 14, 2022

Change

Log-based alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Log-based alerts match on the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. The minimum autoclose duration for incidents is now 30 minutes. For more information, see [Monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) and [Use log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

## June 29, 2022

Feature

You can now collect Apache Flink logs from the Ops Agent, starting with version 2.17.0. For more information, see [Monitoring third-party applications: Flink](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/flink).

## June 27, 2022

Change

The Cloud Logging agent version 1-18 for Windows is now available. This version updates the location of the position files so they are retained across upgrades. For installation information, see [Installing the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/install-index).

## May 30, 2022

Announcement

The Logs Explorer has now replaced the Legacy Log Viewer.

The Logs Explorer is the updated version of the Logging interface, and lets you quickly and efficiently retrieve, view, and analyze logs from your queries. For a detailed tour of the Logs Explorer's features, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## May 27, 2022

Change

Support has been removed for two previously deprecated system metrics: `logging.googleapis.com/excluded_log_entry_count` and `logging.googleapis.com/excluded_byte_count`.

## May 26, 2022

Feature

You can now collect IIS logs and additional metrics from the Ops Agent, starting with versions 2.14.0 (logs) and 2.15.0 (additional metrics). For more information, see [Monitoring third-party applications: IIS](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/iis).

Feature

You can now collect Jetty logs from the Ops Agent, starting with version 2.16.0. For more information, see [Monitoring third-party applications: Jetty](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/jetty).

Feature

You can now collect Active Directory Domain Services logs and metrics from the Ops Agent, starting with version 2.15.0. For more information, see [Monitoring third-party applications: Active Directory Domain Services](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/active_directory_ds).

Feature

You can now collect Varnish logs and metrics from the Ops Agent, starting with versions 2.16.0 (logs) and 2.15.0 (metrics). For more information, see [Monitoring third-party applications: Varnish](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/varnish).

## May 20, 2022

Feature

You can now see more log entries in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) as a result of several style changes.

## May 05, 2022

Feature

You can now hide large amounts of similar log entries from your query results in the Logs Explorer. To learn more, see [Hide similar logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#hide-similar-logs).

## April 28, 2022

Feature

You can now comment within your Logging queries. For more information, see [Logging query language: comments](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comments).

## April 26, 2022

Feature

You can now do the following in the improved Logs Explorer:

  * Use the new [plain-text search field](https://docs.cloud.google.com/logging/docs/view/building-queries#search-text) and [filter menus ](https://docs.cloud.google.com/logging/docs/view/building-queries#query-builder-menus) to construct queries without using the query language
  * Customize your [date and time format preferences](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range) for building queries and to display dates and times in the UI.
  * Toggle on and off the default [summary fields](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#add_summary_fields) to see a raw-text view of your logs.



Feature

When querying your logs data in the Logs Explorer, you can now [select queries from a library](https://logging/docs/view/building-queries#library-queries), making it easier to explore your data and find logs during time-critical troubleshooting sessions.

## April 25, 2022

Feature

The Cloud Logging API now supports the following regions:

  * Europe: 
    * `europe-southwest1`
    * `europe-west6`
    * `europe-west8`
    * `europe-west9`
  * South America: 
    * `southamerica-west1`



For more information, see [Data Regionality for Cloud Logging](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## April 14, 2022

Feature

In the Logs Explorer, pinning log entries has been improved and new options to view pinned log entries in different resource contexts have been added. To learn more, see [Pin log entries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#pin-logs).

## April 04, 2022

Change

You can now [add indexed `LogEntry` fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) to your Cloud Logging buckets to make querying your logs data faster.

## March 25, 2022

Feature

Cloud Logging now supports organization policies that can enforce CMEK protection. For information, see [CMEK organization policies](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#org-policy).

## March 21, 2022

Change

Customer-managed encryption keys (CMEK) for Logs Storage are now Generally Available (GA). CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, see [Manage the keys that protect Logging storage data ](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).

## March 11, 2022

Feature

You can now collect RabbitMQ logs from the Ops Agent, starting with version 2.12.0. For more information, see [Monitoring third-party applications: RabbitMQ](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/rabbitmq).

## February 22, 2022

Feature

You can now collect Apache CouchDB logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: CouchDB](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchdb).

Feature

You can now collect Apache HBase logs and metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: HBase](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hbase).

Feature

You can now collect Apache Hadoop logs and metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: Hadoop](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hadoop).

Feature

You can now collect Apache ZooKeeper logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: ZooKeeper](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/zookeeper).

Feature

You can now collect WildFly logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: WildFly](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/wildfly).

## February 14, 2022

Feature

You can now configure default storage regions and disabled `_Default` sinks for your Google Cloud organizations and all of their new projects and folders. For details, see [Configure default resource settings for Logging](https://docs.cloud.google.com/logging/docs/default-settings).

Feature

You can now collect Apache Kafka metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Kafka](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/kafka).

Feature

You can now collect MongoDB logs from the Ops Agent, starting with version 2.10.0. For more information, see [Collect logs from third-party applications: MongoDB](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/mongodb).

Feature

You can now collect Apache Solr metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Solr](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/solr).

## February 10, 2022

Feature

Your regional preferences, including date and time formatting, are now supported in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#time-range).

## February 09, 2022

Feature

Compute Engine resource names, alongside their corresponding resource IDs, are now supported in the Logs Explorer. For details, see [View Compute Engine logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#compute-engine).

## January 26, 2022

Feature

You can now collect Apache Tomcat metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Apache Tomcat](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/tomcat).

Feature

You can now collect PostgreSQL metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

Feature

Starting with Ops Agent version 2.9.0, you can use the `exclude_logs` logging processor to prevent the Ops Agent from ingesting specific logs. For more information, see [Logging processors](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processors).

Feature

You can now collect Elasticsearch logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Elasticsearch](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch).

## January 07, 2022

Feature

You can now collect MariaDB metrics and logs from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MariaDB](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mariadb).

## November 22, 2021

Deprecated

On or after March 1, 2022, the [Legacy Logs Viewer will be shut down](https://docs.cloud.google.com/logging/docs/view/log-viewer-shutdown) and all users will be redirected to use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-preview).

## October 20, 2021

Feature

You can now collect Redis logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: Redis](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/redis).

Feature

You can now collect MySQL logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: MySQL](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/mysql).

Feature

You can now collect Cassandra logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: Cassandra](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/cassandra).

## October 11, 2021

Change

Cloud Logging now supports the asia-south2, asia-southeast2, australia-southeast2, northamerica-northeast2, and us-west4 regions. For a full list or regions, see [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization).

## October 06, 2021

Feature

The Ops Agent now supports collecting logs from the systemd-journald service, starting with Ops Agent version 2.4.0. For information on configuring the `systemd_journald` receiver, see [Configuring the Ops Agent: Logging receivers](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-receivers).

Feature

You can now collect Apache httpd logs from the Ops Agent, starting with version 2.4.0. For more information, see [Collecting logs from third-party applications: Apache httpd](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/apache).

## August 31, 2021

Feature

You can now collect nginx metrics and logs from the Ops Agent, starting with version 2.1.0. For more information, see [Monitoring third-party applications: nginx](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/nginx).

## August 18, 2021

Feature

You can now use Chef to install and manage the [Google Cloud operations suite agents](https://docs.cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Chef Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-chef/blob/master/README.md) documentation.

## August 02, 2021

Feature

You can now use Puppet to install and manage the [Google Cloud operations suite agents](https://docs.cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Puppet Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-puppet/blob/master/README.md) documentation.

## July 30, 2021

Feature

Cloud Logging now lets you control access to individual log entry fields using field-level access control. To learn more, see [Field-level access control](https://docs.cloud.google.com/logging/docs/field-level-acl).

## July 29, 2021

Change

Cloud Logging now supports the asia-east2 and europe-central2 regions. For a full list or regions, see [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization).

## July 26, 2021

Change

Log entries that are exported to BigQuery that result in a schema mismatch are now being written to an error table. For more information, see [Mismatches in schema](https://docs.cloud.google.com/logging/docs/export/bigquery#mismatch).

## July 23, 2021

Feature

You can now use [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm) keys for organization-level Log Router CMEK. For more information, see [Enabling customer-managed encryption keys for Log Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## July 15, 2021

Change

You can now view Monitoring data and link to the resources in the Cloud Console for Compute Engine logs in the Logs Explorer. For more information, see [Viewing Monitoring data](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

## July 13, 2021

Change

Starting on October 12, 2021, your Dataflow logs that are ingested and stored in Cloud Logging will be charged at the standard [Cloud Logging prices](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary). It's recommended that you review the volume of Dataflow logs ingested into Cloud Logging through [Metrics Explorer in Cloud Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesQuery%22:%22fetch%20dataflow_job%5Cn%7C%20metric%20%27logging.googleapis.com%2Fbyte_count%27%5Cn%7C%20group_by%2030d,%20%5Bvalue_byte_count_aggregate:%20aggregate\(value.byte_count\)%5D%5Cn%7C%20every%2030d%5Cn%7C%20group_by%20%5B%5D,%5Cn%20%20%20%5Bvalue_byte_count_aggregate_aggregate:%5Cn%20%20%20%20%20%20aggregate\(value_byte_count_aggregate\)%5D%5Cn%7C%20group_by%20%5B%5D,%5Cn%20%20%20%5Bvalue_byte_count_aggregate_aggregate_aggregate:%5Cn%20%20%20%20%20%20aggregate\(value_byte_count_aggregate_aggregate\)%5D%22,%22targetAxis%22:%22Y1%22,%22plotType%22:%22STACKED_BAR%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221m%22%7D%7D). For information on optimizing the log volume for your Dataflow jobs, see [Controlling log volume](https://docs.cloud.google.com/dataflow/docs/guides/logging#LogControls).

Change

The Cloud Console now supports creating Logging sinks at the organization or folder level. For information on creating sinks, see [Exporting logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## July 12, 2021

Feature

You can now install the Logging and Monitoring agents on multiple VMs from the **Inventory** tab on the Cloud Monitoring **VM Instances** page. You can select multiple VMs in your fleet for agent installation. The page generates the necessary installation command and provides a link to Cloud Shell, where you can run the command.

## July 07, 2021

Feature

The **Share link** feature for queries in the Logs Explorer now lets you choose whether to include an absolute time range or a relative time range. With an absolute time range, the query includes static time values for the results, so the query always returns the same results. With a relative time range, you can set a value like "last 1 hour", and the results change as time passes.

Feature

**Preview** : Cloud Logging now supports alerts based on matching the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. You can create log-based alerts by using the Logs Explorer or the Monitoring API. For more information, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) and [Using log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

## June 30, 2021

Feature

Cloud Logging lets you copy logs from a Cloud Logging bucket to a Cloud Storage bucket. To learn more, see [Copying log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs).

Change

The Ops Agent is now Generally Available as version 2.0.0. This agent combines logging and metrics into a single agent. The Ops Agent is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency.

For installation information, see [Installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index). For information about migrating from an earlier version, see the [transition guide](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition).

The GA version of the Ops Agent can be configured to collect specific sets of metrics, as described in [Configuring the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration). There is a small number of metrics that the GA version of the Ops Agent handles differently from the Preview versions of the Ops Agent and the Monitoring agent; see [Differences in metric collection](https://docs.cloud.google.com/monitoring/api/metrics_agent#metric-agent-diffs).

## June 25, 2021

Change

Log entries viewed in JSON format in the Cloud Console are now displayed with the field names in alphabetical order.

## June 15, 2021

Change

You can now view Monitoring data and link to the resources in the Cloud Console for certain logs, such as Google Kubernetes Engine logs, in the Logs Explorer. For more information, see [Viewing Monitoring data](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

## May 06, 2021

Feature

The Logs Explorer Histogram offers new time controls, including zooming and scrolling, to give you more in-depth analysis of your logs data. For details, see [Analyzing logs using time controls](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#analyzing_logs_histogram).

## May 03, 2021

Feature

You can now add custom fields in the Logs Explorer to better analyze logs and refine your queries. For more information, see [Adding fields to **Log fields** pane ](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#custom-fields).

## April 27, 2021

Feature

You can now install the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent), [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent), and [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on VMs running OpenSUSE Leap versions 15, 15.1, and 15.2.

## April 21, 2021

Feature

You can now provision and manage the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent) on Windows using Ansible. For more information, refer to the [Ansible Role for Cloud Ops](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible/blob/master/README.md) documentation.

## April 12, 2021

Feature

Shared queries are now generally available (GA). To learn more, see [Shared queries](https://docs.cloud.google.com/logging/docs/view/building-queries#shared-queries).

## April 08, 2021

Feature

The Google Cloud [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. This agent combines logging and metrics into a single agent that is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency. It supports both Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to install the Google Cloud Ops Agent via [Ansible](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible) on Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to provision the Google Cloud Ops Agent via [Terraform](https://registry.terraform.io/modules/terraform-google-modules/cloud-operations/google/latest/submodules/agent-policy) on Linux and Windows Compute Engine VMs.

## April 06, 2021

Change

Cloud Logging now supports [22 regions](https://docs.cloud.google.com/logging/docs/storage#regionalization) in which you can create a log bucket so that you can meet compliance and audit requirements when storing your logs.

## March 29, 2021

Change

Logs Views are now Generally Available (GA). Using Logs Views, you can control who has access to the logs within your Logs Buckets. For more information on this feature, refer to the [Managing Logs Views](https://docs.cloud.google.com/logging/docs/logs-views) guide.

## March 18, 2021

Feature

Cloud Logging now shows the breakdown of log severity levels in the Histogram pane. To learn more, see the [Histogram section](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#histogram-panel) on the Logs Explorer page.

## March 12, 2021

Change

Suggested queries is now generally available (GA). To learn more, go to [Suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries).

## March 04, 2021

Feature

Compute Engine's **VM Instances** dashboard now provides an **Operations** menu. The "View metrics" menu option brings you to the **Infrastructure summary** dashboard in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Feature

Kubernetes Engine's **Clusters** and **Workloads** dashboards now provide an **Operations** menu. The "View metrics" menu option brings you to the **GKE Dashboard** in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

## February 18, 2021

Change

Cloud Logging agent for Windows version 1-14 is now available. This version changes the default Windows configuration from using gRPC to REST for sending logs to the Cloud Logging API. For more information, refer to the [release information on GitHub](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/windows-v1-14).

## February 08, 2021

Change

Logging truncates oversized [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) label keys and values. For details, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas#log-limits).

## January 29, 2021

Change

Cloud Logging has increased the number of `entries.write` API calls from 60,000 to 120,000 per minute. For more information on quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## January 26, 2021

Feature

The `gcloud` commands for [managing Agent Policies](https://docs.cloud.google.com/stackdriver/docs/solutions/managing-agent-policies) are now available in beta. For more information, refer to the [`gcloud` documentation for Agent Policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies).

## January 22, 2021

Change

The Logs Explorer now provides a higher degree of contrast that improves readability.

## January 14, 2021

Change

Cloud Logging now lets you share your saved queries with other users of a project. To learn more, go to the [Shared queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#shared-queries).

## December 16, 2020

Announcement

Logs regionalization is now generally available. You can set the region in which you want to store your logs data. For information about this feature, refer to the [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization) documentation.

## December 08, 2020

Fixed

Cloud Logging calculates the system logs-based metrics `byte_count` and `log_entry_count` on stored logs only, unlike user-defined logs-based metrics which are calculated on both stored and excluded logs. For more information, see [System logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system_logs-based_metrics).

This change is currently rolling out and affects all users after December 11, 2020.

## December 07, 2020

Feature

In the Logs Explorer, you can now stream your log entries in real time as Cloud Logging ingests them. To learn more, see [Streaming logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#stream-logs).

## November 13, 2020

Feature

You can now use the **Share link** button in the Logs Explorer to create and share a shortened URL of your current query. For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## November 06, 2020

Feature

By using the new `gcloud` command and API for live tailing, you can now stream your logs in real time as your applications write them to the Cloud Logging API. To learn more, see [Live tailing log entries](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#live-tailing).

## November 05, 2020

Announcement

Beta release: You can set the region in which you want to store your logs data. For information about this feature, refer to the [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization) documentation.

## October 28, 2020

Feature

You can now create sinks from within the **Logs Explorer** and **Logs Router** pages. To learn more, see [Exporting logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

Announcement

To help you understand your logs volume and usage within the context of your Logs Buckets, the **Resource Usage** page has been moved to the **Logs Storage** page, which now contains your resource usage information. To learn more, see [Tracking logs usage](https://docs.cloud.google.com/logging/docs/exclusions#tracking).

## October 22, 2020

Change

Cloud Logging now calculates logs-based metrics from both ingested and excluded logs. In other words, you can now calculate logs-based metrics from logs without ingesting them into a Logs Bucket. 

This change started rolling out **October 18, 2020** and will finish rolling out **October, 30 2020**.

For more information, see [Overview of logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Announcement

Logs Views are now available in Preview. Using Logs Views, you can control who has access to the logs within your Logs Buckets. For more information on this feature, refer to the [Managing Logs Views](https://docs.cloud.google.com/logging/docs/logs-views) guide.

## October 20, 2020

Change

Recent queries is now generally available (GA). To learn more, go to [Recent queries](https://docs.cloud.google.com/logging/docs/view/building-queries#recent-queries).

## October 19, 2020

Feature

In the Logs Explorer you can now download your logs in JSON and CSV to your computer, Google Drive, or view them in a new tab. To learn more, see [Downloading logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#download_logs).

## October 15, 2020

Feature

The [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. Ops Agent provides a single agent to collect logs and metrics on Compute Engine instances.

Note that the Ops Agent uses new configuration files that are not compatible with the standalone Cloud Monitoring and Cloud Logging agents.

## October 13, 2020

Announcement

We've renamed the Logs Viewer (Preview) to the Logs Explorer. The Logs Explorer offers a robust set of tools for analyzing your logs data and is now the default viewer for Cloud Logging. To learn more, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface). 

The Logs Viewer (Classic) is now called the Legacy Logs Viewer. It will continue to be available and maintained until March 2021, but won't be actively developed further.

## October 12, 2020

Change

Cloud Logging has deprecated the following two logs-based metrics related to exclusions:

  * `logging.googleapis.com/excluded_log_entry_count`
  * `logging.googleapis.com/excluded_byte_count`



Cloud Logging will stop populating these metrics on October 1, 2021.

## September 22, 2020

Feature

The histogram panel in the Logs Viewer (Preview) now contains a viewport to help you quickly understand the time range of the log entries you're viewing within the Query results pane. To learn more, go to the [Histogram panel](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#histogram-panel).

## September 21, 2020

Change

Logs Buckets are now generally available. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide.

## September 17, 2020

Feature

In the Logs Viewer (Preview), you can now pin log entries within the **Query results** and **Histogram** panes. To learn more, go to [Pinning logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#pin-logs).

Feature

In the Logs Viewer (Preview), you can now view a log entry in its resource context. To learn more, go to [Viewing a pinned log entry in its resource context](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#resource-context).

Feature

You can now copy a link to a log entry in the Logs Viewer (Preview). To learn more, go to [Copy a link to a log entry](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#copy-link).

## September 14, 2020

Feature

Cloud Logging now offers the ability to view a history of your ran queries through the **Recent** queries tab. To learn more, go to the [Recent queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#recent-queries).

## September 01, 2020

Change

Cloud Logging updated IAM custom role permissions. Users with custom roles should verify their permissions are correct. For a list of the permissions and roles, go to the [Permissions and Roles section on the Access control page](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).

## August 24, 2020

Feature

You can now view Cloud Trace information from within the Logs Viewer. To learn more, go to the [Trace data section on the Using Logs Viewer (Preview) page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#trace_data).

## August 17, 2020

Feature

To help you explore your logs more efficiently, Cloud Logging now provides suggested queries based on the context of your Google Cloud project. For more information, go to [Suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries).

## August 11, 2020

Feature

Beta release: You can now use Logs Buckets to centralize or divide your logs based on your needs. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide.

Change

Users now manage logs exclusions through logs sinks. As a result, custom roles that have the `logging.sinks.*` permissions can now control the volume of logs ingested into Cloud Logging through logs sinks.

We recommend that you review any custom roles with the `logging.sinks.*` permissions so that you can make adjustments as needed.

## August 03, 2020

Feature

Alpha release: You can now use Logs Buckets to centralize or divide your logs based on your needs. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide. To participate in the alpha or to get notified when Logs Buckets goes beta, fill out the [sign up form](https://docs.google.com/forms/d/e/1FAIpQLSeBVpNBivnTAAd4G3rdait9t94uG9TWc07oGwNRGcE071TeCA/viewform).

## July 30, 2020

Change

The Logs field explorer panel is now generally available (GA). To learn more, see the [Logs field explorer section on Logs Viewer (Preview) interface page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#logs-field-panel).

## June 30, 2020

Feature

Cloud Logging now contains a Logs Dashboard page that provides a high-level overview into the health of your systems running within a project. To learn more, see [Logs Dashboard](https://docs.cloud.google.com/logging/docs/view/dashboard).

## June 05, 2020

Change

Custom retention is now generally available (GA). In order to have time to explore this feature, you won't be charged for extended retention of logs until March 31, 2021. To learn more, see the [Logging pricing section on the Pricing for Google Cloud's operations suite page](https://cloud.google.com/stackdriver/pricing#logging-costs).

## June 03, 2020

Feature

In the Logs Viewer (Preview), you can now save your queries, which can then be viewed and run from the **Saved** queries tab. For more information, see the [Saved queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries).

## May 18, 2020

Feature

**Logs Viewer** now contains the **Logs field explorer** panel, which lets you view aggregation-based results for your project's log fields and makes it more efficient to refine queries. To learn more, go to the [Logs Viewer (Preview) page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## May 11, 2020

Feature

You can now use regular expressions to query your logs data and create filters. For more information, go to [Using regular expressions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#regular-expressions).

## April 27, 2020

Change

The Logs Viewer (Preview) is now GA. To learn more, go to the [Logs Viewer (Preview) Overview page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-preview).

## March 17, 2020

Change

Incoming log entries must have timestamps that don't exceed the [logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Cloud Logging.

## March 12, 2020

Change

Cloud Logging Agent for Windows version 1-11 is now available. This version upgrades `fluentd` from 1.4.2 to 1.7.4. Go to [Installing the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/installation) for information on installing this version of the agent.

## March 10, 2020

Feature

Logs Viewer (Preview) now contains a histogram panel. The histogram panel lets you visualize your logs data to more easily spot patterns and troubleshoot issues. For more information, see [Using Logs Viewer (Preview)](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## February 24, 2020

Feature

Beta release: You can now use the new Logs Viewer (Preview) to view, parse and analyze log data, and refine your query parameters. Go to [Logs Viewer interface (Preview)](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) for more information.

## February 17, 2020

Change

BETA: You can now configure the retention periods of your logs data. For more information, go to [Storing logs](https://docs.cloud.google.com/logging/docs/storage).

## January 17, 2020

Feature

Customer-managed encryption keys (CMEK) for the Logs Router are now Generally Available (GA). CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, go to [Enabling customer-managed encryption keys for Logs Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## December 16, 2019

Feature

GA release: You can now use partitioned tables for logs exports to BigQuery. For details, go to [Partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).

## December 13, 2019

Change

Google Kubernetes Engine (GKE) version 1.15, which is now generally available, drops support for GKE versions 1.12 and earlier. As a result, the beta version of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your GKE clusters are running version 1.12 or earlier, then you must upgrade them as soon as possible.

## December 11, 2019

Deprecated

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated. If you're using Legacy Stackdriver, then you must [migrate to Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) before Legacy Stackdriver is decommissioned. For more information, see [Legacy Stackdriver support for GKE deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy).

## November 18, 2019

Feature

Customer-managed encryption keys (CMEK) for the Logs Router are now available in Beta. CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, go to [Enabling customer-managed encryption keys for Logs Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## September 20, 2019

Feature

Beta release: Stackdriver Logging now offers partitioned tables for exports to BigQuery. For details, go to [Partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).

## September 10, 2019

Feature

Stackdriver Logging now lets you save your advanced log queries to a Saved Searches library, where they can be managed and shared. Go to [Saved searches](http://cloud.google.com/logging/docs/view/overview#saved-searches) for details.

Change

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver Kubernetes Engine Monitoring is now the default Stackdriver support option. This is a change from prior versions where Stackdriver Logging and Stackdriver Monitoring were the default Stackdriver support option. For more information, see [Overview of Stackdriver support for GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine).

## May 21, 2019

Feature

[Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) is now generally available. Users of the legacy Stackdriver support for [monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/monitoring) and [logging](https://docs.cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/logging) for Google Kubernetes Engine are encouraged to [migrate to Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) as soon as possible.

## April 23, 2019

Change

The maximum size of a log entry has been increased to 256 KB from 100 KB. For details on logging usage limits, go to [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## April 15, 2019

Feature

A new Windows version (v1-9) of the Stackdriver Logging agent is now available. The new version saves the agent service logs on disk for easier troubleshooting and supports the `config.d` configuration extension directory.

## March 15, 2019

Change

Stackdriver agents are subject to an updated [deprecation policy](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy). As part of this transition, the next major version of the Stackdriver Monitoring and Stackdriver Logging agents will stop supporting operating systems that are at the end of their lifecycle, as well as some [third-party agent plugins](https://monitoring/agent/plugins/).

## February 22, 2019

Change

You now have two choices for the access control model when creating a Cloud Storage bucket: bucket-only (new) and object-level. Select **Set object-level and bucket-level permissions** as the access control model during bucket creation if you intend to use the bucket as a sink destination. See [Errors exporting to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#errors_exporting_to_cloud_storage) for details.

## January 22, 2019

Change

In the Stackdriver Logging API, log sinks, metrics, and exclusions have two new output-only fields: create time and last update time. See [LogSink](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/sinks) for an example. If this information isn't available for older resources, these fields aren't present.

## December 03, 2018

Feature

The Logs Viewer has a new option to display a log entry in its resource context. It can also pin a log entry while allowing you to change the display context. See [Viewing Logs](https://docs.cloud.google.com/logging/docs/view/overview) for details.

## November 01, 2018

Feature

You can now view error and success metrics for your log sinks using [export system metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system_logs-based_metrics).

## October 19, 2018

Feature

You can now link from certain App Engine request logs to a detailed trace that explains the request's latency. You can also filter log entries according to their latencies, and if they contain detailed trace data viewable by Stackdriver Trace. See [Viewing latency in Trace](http://cloud.google.com/logging/docs/view/overview#show-latency) for details.

## October 01, 2018

Feature

The Logs Viewer can now download up to 300 log entries in JSON or CSV format. See [Viewing Logs](https://docs.cloud.google.com/logging/docs/view/overview) for details.

## September 14, 2018

Feature

The format of service account names for older log [sinks](https://docs.cloud.google.com/logging/docs/export#sink-terms) is being changed so that all log sinks will have consistent service account names. This naming format has already been applied to project-level sinks on BigQuery, Cloud Pub/Sub, and Cloud Storage permission pages. In the coming weeks, this naming format will be applied to organization-level sinks and folder-level sinks, and to sinks listed on the **Logs Exports** page in the Logs Viewer. There are no associated changes to functionality or granted permissions.

## September 05, 2018

Feature

**Access Transparency** logging is now Generally Available. See [Overview of Access Transparency](https://cloud.google.com/logging/docs/audit/access-transparency-overview) for details.

## July 25, 2018

Change

Audit logs exports to BigQuery now feature a compact format. On March 1, 2019, the older extended format will be removed.

## June 29, 2018

Change

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based pricing. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## June 26, 2018

Feature

You can now immediately disable all logs ingestion. For instructions, see [Stopping all logs ingestion](https://docs.cloud.google.com/logging/docs/exclusions#stop-logs).

## June 19, 2018

Feature

Google Cloud Storage logs streaming time has been reduced from 12 hours to 3 hours. For details, see [Using Exported Logs](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#gcs-availability).

## June 18, 2018

Change

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use of Stackdriver is free**. The service tiers have been removed, and you can experience all features without incurring costs. Thereafter, Stackdriver switches to consumption-based pricing. For more information, see [Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## June 12, 2018

Feature

You can now enable and configure your Data Access audit logs using the Google Cloud console. For details, see [Configuring Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## May 17, 2018

Feature

You can now see your Logging usage and estimate your bill according to the new Stackdriver pricing and in advance of billing enforcement. See [Estimating your bills](https://docs.cloud.google.com/stackdriver/estimating-bills) for details.

## May 08, 2018

Feature

You can now specify custom fields in your Logs Viewer log-entry summary lines. See [Add custom fields](https://docs.cloud.google.com/logging/docs/view/overview#custom-fields) for details.

## May 02, 2018

Feature

[Stackdriver Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) is released in Beta for Kubernetes 1.10 clusters running in [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/). The previous Stackdriver support is still available for those who do not opt into this Beta release. This release affects Logging by introducing new [monitored resource types](https://cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_cluster) and new [Kubernetes metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes).

## April 10, 2018

Feature

You can now specify that the Stackdriver Logging agent converts your payloads to JSON format for certain log inputs. For details on enabling this feature, see [Structured Logging](https://docs.cloud.google.com/logging/docs/structured-logging).

## March 12, 2018

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

Feature

Logging data retention has been increased to 30 days for all projects.

## February 01, 2018

Feature

The Logging agent now supports partial success for logs ingestion. Any invalid log entries in a full set will be dropped, and the valid log entries now will be successfully ingested into the Stackdriver Logging API; previously, the full set would have been dropped if it contained any invalid log entries. To enable partial success, upgrade your Logging agent to [google-fluentd v1.5.27](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/v1.5.27).

## December 13, 2017

Feature

Filtering logs by **time range** is now available in the Logs Viewer. For more information, see [Scroll to a time](https://docs.cloud.google.com/logging/docs/view/overview#scroll-to-time).

## December 04, 2017

Change

**Logging agent recommendation** : VM instances should have at least 1 GB of memory to run the Logging agent.

Feature

**Google Cloud Platform HTTP(S) load balancing logging** now includes logs for **rejected requests** , such as those due to invalid or expired URL signatures, and aligns **httpRequest.requestSize** with metrics from the [Stackdriver Monitoring API](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing). For more information, see [HTTP(S) Load Balancing Logging](https://docs.cloud.google.com/compute/docs/load-balancing/http#logging).

## November 29, 2017

Feature

**Logs-based metrics** are now Generally Available. For more information, see [Overview of Logs-based Metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Change

**Logging agent installation instructions** : The checksum validation step for the installation script has been removed. You can see the new instructions on the [logging agent installation](https://docs.cloud.google.com/logging/docs/agent/installation) page.

Fixed

**Logs Viewer** update: Fixes a problem related to the daylight saving time transition in the U.K. If you see your logs displaying in the wrong time zone, you can set your default time zone by using the **Jump to date** drop-down menu to select a different time zone. For more information, see [Logs Viewer user interfaces](https://docs.cloud.google.com/logging/docs/view/overview#the_user_interfaces).

## November 01, 2017

Change

**Pricing changes** : Billing for logs overages will begin **March 31, 2018**. This date extends the one that was previously communicated to give Stackdriver customers more time to apply the [exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions) feature to control which logs are stored in Logging. Billing for custom and user-defined logs-based metrics is still postponed. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

## October 30, 2017

Feature

**Exclusion filters** are now Generally Available. For more information, see [Excluding Logs](https://docs.cloud.google.com/logging/docs/exclusions), and the **Resource Usage** page in the Logs Viewer.

## October 24, 2017

Change

The **`gcloud logging` command group** is now generally available. `gcloud beta logging` will be removed at the end of December 2017. For more information, see [gcloud logging](https://docs.cloud.google.com/sdk/gcloud/reference/logging).

## September 12, 2017

Feature

**Admin Activity audit logs** retention has been extended to 400 days for both the Stackdriver Basic and Premium service tiers. For more information, see [Audit log retention](https://docs.cloud.google.com/logging/docs/audit#audit_log_retention).

Feature

**Logging agent update** to 1.5.18-1. Allows enabling JSON detection via configuration, fixes a problem with string-valued timestamps, and allows setting the following [`LogEntry`](https://logging/docs/api/reference/rest/v2/LogEntry) fields: `trace`, `sourceLocation`, and `operation`.

## August 31, 2017

Feature

**Logs-based metrics** now support extracting values from log entries to create distribution metrics and to populate user-defined metric labels. This lets you create multiple time series in a single logs-based metric. Also, the latency of logs-based metrics has dropped from approximately 5 minutes to 1 minute, so you can respond more quickly to the metrics. For more information, see [Overview of Logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Feature

**Exclusion filters** let you control which logs are kept in Stackdriver Logging. The **Resource Usage** page in the Logs Viewer breaks down log volume by resource type. For more information, see [Excluding Logs](https://docs.cloud.google.com/logging/docs/exclusions).

Change

**Logging agent** : The Stackdriver Logging agent package has been updated to version 1.5.17. The agent will now send smaller requests, improving log delivery latency and increasing queries per second, which may affect users with high log volumes. Also, the package's bundled Ruby has been updated to version 2.2.7. If you have configuration snippets or extra gems that depend on older Ruby features, you may have to update them.

Change

**Pricing changes** : The free per-project allotment of logs is being increased from 5 GB to 50 GB. Beginning December 1, 2017, we will enforce the new limits and begin charging for logs kept in Stackdriver Logging above the limits. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

## August 23, 2017

Feature

**Aggregated Exports** : Organizations and folders can now export selected log entries from all of their projects with a single sink created in the organization or folder. For more information, see [Aggregated Exports](https://docs.cloud.google.com/logging/docs/export/aggregated_exports).

Change

**Timestamp handling**. The following changes to log entry timestamps have been made or are planned. 1\. Logging does not modify the user-provided `timestamp` field, except to set it to the current time if it is omitted. A second field, `receivedTimestamp`, is set to the time Logging receives the entry. 2\. The `timestamp` field is used to compute the age of log entries and to enforce the [log retention period](https://docs.cloud.google.com/logging/quotas). Prior to the change, the `receivedTimestamp` field is used for that purpose. 3\. Logging discards log entries whose timestamps are more than 24 hours in the future or are further in the past than the log entry's retention period. Prior to the change, future timestamps and very old timestamps are handled in an unpredictable fashion. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

## July 10, 2017

Change

**API Migration**. Information about the deprecated v1 API is being removed from general documentation. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

Feature

**IAM support** for Logging now includes custom roles. For more information, see Logging [Access Control](https://docs.cloud.google.com/logging/docs/access-control).

## June 05, 2017

Issue

**Exported audit logs in BigQuery** : The BigQuery schema for exported audit log entries changed on June 5, 2017. The following audit log components now have shortened field names when they are exported to BigQuery: `protoPayload`, `protoPayload.serviceData`, `protoPayload.request`, and `protoPayload.response`. This is a breaking change for queries involving these fields. For more information see [Audit log field changes](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#bigquery-overview).

Feature

**Apps Script** : You can access your Apps Script logs in Logging.

Feature

**Logs Viewer** : You can more easily expand all fields in a log entry.

## May 01, 2017

Feature

Data access logs are now available and are user-configurable. See [Configuring Data Access Logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

Feature

**Aggregated exports of logs** : You can now create log sinks in organizations, billing accounts, and folders. Those sinks can export log entries from all included projects. See [Aggregated Exports](https://docs.cloud.google.com/logging/docs/export/aggregated_exports).

Deprecated

**v1 API turndown: writeLogEntries** : As a final step in the v1 API turndown, the v1 `WriteLogEntries` method will be shut down on October 1, 2017. You must migrate any applications that write log entries using the v1 API. You must also upgrade any manually-installed Logging agents in your VM instances. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://cloud.google.com/logging/docs/apis).

Deprecated

**v1 API turndown: sinks and logs-based metrics** : Migrate your remaining v1 export sinks and v1 logs-based metrics. If you do not, Logging will migrate them by mid-July, 2017. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

## April 01, 2017

Feature

**Resource types** : Several new resource types are added, including types for Cloud Bigtable, Cloud Dataflow, and Cloud Container Engine.

## March 31, 2017

Change

**V1 API turndown** : The date of the v1 API turndown has changed. See the release note for May 2017.

Change

**Logging agent for Windows** : If you install the Logging agent on VM instances running Microsoft Windows, be aware that there are restrictions on the folders used for the installer and the installed agent. For details, [Installing on Linux and Windows](https://docs.cloud.google.com/logging/docs/agent/installation#joint-install).

## February 06, 2017

Feature

**App Engine Flexible Environment** : For App Engine Flexible Environment, the Logs Viewer can now display application log entries ("log lines") inside the log entry for the associated service request. This is similar to the functionality in the App Engine Standard Environment.

Feature

**Resuming log streaming** : The Logs Viewer now automatically resumes streaming logs when its browser window or tab is selected. You no longer have to restart streaming when returning to the page.

Feature

**Exporting logs from organizations, folders, and billing accounts** : The [`gcloud logging`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command-line tool now supports creating log sinks to export audit logs from organizations, folders, and billing accounts. This feature also supported in the API.

Feature

**Viewing multiple logs** : Previously in the Logs Viewer, you could view a single log or "all logs" from a single resource type. Now you can select any number of logs within a resource type to view, using the log name dropdown menu.

For example, when viewing App Engine applications, the default is now to display log entries from any of these logs: `ngnix.request`, `stdout`, `request log`, and `stderr`.

Change

**Remove daily API quotas** : The Logging API no longer includes daily API quotas. The API still enforces short-term (per 100s) quotas on API calls, as displayed in the Stackdriver Logging API dashboard.

Change

**Deleting logs-based metrics in alerting policies** : Attempting to delete a [logs-based metric](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics) that is used in one or more Stackdriver Monitoring alerting policies now fails with the status `FAILED_PRECONDITION`. You must remove the metric from the alerting policies or delete the alerting policies prior to deleting the logs-based metric.

Issue

**Logs retention and source restriction** : With the implementation of the Basic and Premium service tiers in December 2016, Stackdriver Logging began enforcing retention and log source restrictions for projects that are in the Stackdriver Basic tier or are not associated with a Stackdriver account. In the Basic tier, log entries are visible for 7 days after they are received, and logs from non-Google Cloud sources, including Amazon Web Services, are rejected.

## December 12, 2016

Change

**Logs Viewer v2** : The Logs Viewer has been migrated to the Stackdriver Logging API v2. For the full documentation, [Viewing Logs (v2)](https://docs.cloud.google.com/logging/docs/view/overview). Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

Feature

**New LogEntry fields** : Fields `trace` and `sourceLocation` were added to [`LogEntry`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/LogEntry).

Feature

**List logs** : the Stackdriver Logging API now has "list logs" methods: [`organizations.logs.list`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/list) and [`projects.logs.list`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/projects.logs/list).

## November 21, 2016

Feature

**Sinks** : The Stackdriver Logging API now allows both projects and organizations to own sinks. In addition, sinks can now export log entries to destinations in other projects. See [`LogSink`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.sinks).

Feature

**Organizations** : The Stackdriver Logging API now allows both projects and organizations to own logs. A log belonging to an organization is named `"organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"`. See [`organizations.logs.delete`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/delete).

## October 20, 2016

Feature

Logging is generally available to Google Cloud Platform customers. Individual features that are in Alpha or Beta release are marked as such in the documentation.

Change

**Pricing** : Stackdriver is now available in Basic and Premium service tiers. All existing and new Stackdriver accounts are entered into a 30-day free trial of the Premium Tier. At the end of the trial period, you could lose some functionality you had during the Beta release unless you upgrade to the Premium Tier. For more details, see [Pricing](https://cloud.google.com/stackdriver/pricing).

Feature

**API v2** : The Stackdriver Logging API v2 is generally available, providing a simplified log format. During a transition period, you can use the same API at either of these two endpoints: `https://logging.googleapis.com/v2beta1/...` or `https://logging.googleapis.com/v2/...`.

Deprecated

**API v1** : The Stackdriver Logging API v1 (v1beta3) is deprecated. Users of this API should migrate to the v2 API. The v1 API will be removed from service on March 30, 2017. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

## September 09, 2016

Change

The Google Cloud Logging API is now known as the Stackdriver Logging API. This change does not affect any code.

## June 15, 2016

Change

A change to the v2beta1 API might affect some existing code. In the following methods, the parameter `projectName` has been changed to `parent`: `sinks.create`, `sinks.list`, `metrics.list`, `metrics.create`.

Change

The Google Logging API v2beta1 reference documentation now includes code snippets for each method. For example, see [`entries.list`](https://docs.cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list).

## April 27, 2016

Change

The user documentation has been reorganized. The [documentation landing page](https://docs.cloud.google.com/logging/docs) and the left-side navigation entries have changed. Existing URLs to individual documentation pages will be redirected if necessary.

## March 23, 2016

Change

Google Cloud Logging is now **Stackdriver Logging** , part of the [Google Stackdriver](https://cloud.google.com/products/operations) suite of products. You can now manage logs from Amazon EC2 virtual machine instances alongside your Google Cloud projects. See [Logging agent](https://docs.cloud.google.com/logging/docs/agent) for more details.

## February 18, 2016

Change

The [logging agent authorization](https://docs.cloud.google.com/logging/docs/agent/authorization) instructions now recommend storing private-key credentials as `/etc/google/auth/application_default_credentials.json`. You do not have to move your existing file at `/root/.config/gcloud/application_default_credentials.json`.

## January 29, 2016

Change

The [Logs Viewer](https://docs.cloud.google.com/logging/docs/view/logs_viewer) now lets you [view the structure](https://docs.cloud.google.com/logging/docs/view/logs_viewer#expanding) of log entries. You can also [show or hide](https://docs.cloud.google.com/logging/docs/view/logs_viewer#similar) log entries with similar field values.

## December 10, 2015

Change

Version 2 of the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/apis) is now available. Among other changes, the V2 API lets you retrieve log entries from Logging using the [`entries.list`](https://docs.cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list) method.

## October 22, 2015

Change

The [Logs Viewer](https://docs.cloud.google.com/logging/docs/view/logs_viewer) now has cascading menus for selecting log entries from Google App Engine and Google Compute Engine.

## October 13, 2015

Change

See [logs-based-metrics](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics) to learn how to create Google Cloud Monitoring metrics using logs filters.

Change

The list of [log types](https://docs.cloud.google.com/logging/docs/view/logs_index) has been expanded.

## September 15, 2015

Change

Added [Java examples](https://docs.cloud.google.com/logging/docs/api/tasks) of Logging API usage. Simplified the [authorization code](https://docs.cloud.google.com/logging/docs/api/tasks/authorization) for Java and Python, and the same code now runs on App Engine, Compute Engine, and your development workstation.

## September 09, 2015

Change

The [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) in the Google Cloud SDK is now named `gcloud beta logging`.

## August 12, 2015

Feature

The [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/api-overview) and [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) now support project sinks. A project sink can export log entries from any combination of logs, based on [advanced logs filters](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

## August 03, 2015

Feature

Cloud Logging now has advanced logs filters that let you specify arbitrary Boolean expressions that match on log entries. See [Using advanced logs filters](https://docs.cloud.google.com/logging/docs/view/advanced-queries) in the Logs Viewer, and the [Advanced Logs Filters guide](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

## June 15, 2015

Change

The logging agent has new, simpler [installation instructions](https://docs.cloud.google.com/logging/docs/agent/installation) You no longer have to edit the agent's configuration file to install [private-key authorization](https://docs.cloud.google.com/logging/docs/agent/authorization).

Change

The Logging documentation has been reorganized. The [table of contents](https://docs.cloud.google.com/logging/docs) now groups all information about the logging agent, viewing logs, and exporting logs in individual sections.

## May 21, 2015

Change

A new Google Cloud console UI panel for the [logs export feature](https://docs.cloud.google.com/logging/docs/export/configure_export) was released. The UI lets you export a subset of your logs from a logs service. For example, you could export `syslog` from Google Compute Engine without exporting `activity_log`.

## April 28, 2015

Feature

You can now stream logs from Cloud Logging to [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) and from there to your own endpoints. This involves changes to [logs export](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#pubsub-overview). For example, use Cloud Pub/Sub to route logs through [Google Cloud Dataflow](https://docs.cloud.google.com/dataflow/docs) and into tools like [Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## March 19, 2015

Feature

The `google-fluentd` logging agent supports [two dozen third-party logs](https://docs.cloud.google.com/logging/docs/view/logs_index).

Feature

Cloud Logging is now available in Beta release, allowing you to configure, visualize, analyze and export your Google Compute Engine and Google App Engine logs.

Feature

The [Google Cloud Logging API](https://docs.cloud.google.com/logging/docs/api) is now available in Beta release. The API lets you write logs, create logs, and control the export of logs. Client libraries make it easy to use the API in your favorite programming language.

Feature

The `google-fluentd` logging agent runs with [additional operating systems](https://docs.cloud.google.com/logging/docs/agent/installation), including Debian, Ubuntu, Red Hat, and CentOS. A single script installs the agent on any supported operating system.

Feature

The [`glcoud logging`](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) command-line interface, which uses the API, is now available in Beta release. The commands provide an easy way to perform administrative tasks such configuring logs export.

Change

The [Logs Viewer refresh](https://docs.cloud.google.com/logging/docs/view/logs_viewer) brings more search options and quicker access to [logs export configurations](https://docs.cloud.google.com/logging/docs/export/configure_export). Regex-search has been removed as part of this refresh.

Change

The Cloud Logging documentation has been improved with more set-up options, [simpler procedures](https://docs.cloud.google.com/logging/docs/agent/installation) and [more examples](https://docs.cloud.google.com/logging/docs/export/using_exported_logs).

## January 15, 2015

Feature

Beta release: App Engine logs can be exported to Cloud Storage and BigQuery.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
