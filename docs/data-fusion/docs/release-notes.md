---
url: https://docs.cloud.google.com/data-fusion/docs/release-notes/
title: Cloud Data Fusion release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:22:05.458761+00:00
---

# Cloud Data Fusion release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Resources ](https://docs.cloud.google.com/data-fusion/docs/resources)



Send feedback 

#  Cloud Data Fusion release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Data Fusion. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/clouddatafusion-release-notes.xml) directly. 

## September 16, 2026

Change

The BigQuery Source plugin version 0.24.7 is available in Cloud Data Fusion version 6.11.0 and later. This release includes the following change:

  * Fixed an issue that caused intermittent pipeline failures in the BigQuery Source plugin when errors occurred during the creation of the temporary staging bucket ([PLUGIN-1787](https://cdap.atlassian.net/browse/PLUGIN-1787)).



## August 07, 2026

Change

The Cloud SQL for MySQL and Cloud SQL for PostgreSQL plugins, version 1.11.14, are available in Cloud Data Fusion version 6.10.x. Version 1.12.5 of these plugins is available in Cloud Data Fusion version 6.11.x.

This release includes the following feature:

  * You can now configure transaction isolation levels in the Cloud SQL for MySQL and Cloud SQL for PostgreSQL plugins. This configuration applies to both batch sources and sinks, providing more precise control over data consistency and database locking ([PLUGIN-1779](https://cdap.atlassian.net/browse/PLUGIN-1779)).



Change

The Windows Share Copy Action plugin version 2.12.5 is available in Cloud Data Fusion version 6.9.1 and later. Version 2.13.2 of this plugin is available in Cloud Data Fusion version 6.11.0 and later.

This release includes the following change:

  * Added support for the modern SMBv2 and SMBv3 protocols to improve connection performance and reliability, while maintaining backward compatibility with pipelines that use SMBv1 ([PLUGIN-1960](https://cdap.atlassian.net/browse/PLUGIN-1960)).



## July 15, 2026

Feature

Cloud Data Fusion version 6.11.1.4 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Fixed

Fixed in Cloud Data Fusion 6.11.1.4:

  * Fixed a race condition where successfully completed Dataproc jobs were incorrectly marked as `failed` on the Dataproc console due to premature program cancellation ([CDAP-21219](https://cdap.atlassian.net/browse/CDAP-21219)).
  * Fixed an issue where the **Pipeline list** page would hang due to a race condition in an internal service ([CDAP-21241](https://cdap.atlassian.net/browse/CDAP-21241)).
  * Fixed a security vulnerability in log downloads by enforcing strict validation on requested log paths and query parameters to prevent unauthorized access ([CDAP-21260](https://cdap.atlassian.net/browse/CDAP-21260)).



Change

Changes in Cloud Data Fusion 6.11.1.4:

  * Increased the default Wrangler browsing limit to 2,000 items ([CDAP-21259](https://cdap.atlassian.net/browse/CDAP-21259)).



## June 29, 2026

Change

The Salesforce plugin version 1.7.4 is available in Cloud Data Fusion version 6.8.0 and later.

This release includes the following change:

  * Added support for the client credentials grant type in the Salesforce plugin. To select the grant type, use the new **OAuth Grant Type** field in the console ([PLUGIN-1953](https://cdap.atlassian.net/browse/PLUGIN-1953)).



## June 05, 2026

Feature

Cloud Data Fusion version 6.11.1.3 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Fixed

Fixed in Cloud Data Fusion 6.11.1.3:

  * Fixed an issue that caused pipeline preview runs to fail with an `InaccessibleObjectException` when using certain plugins, such as Cloud SQL for PostgreSQL ([CDAP-21212](https://cdap.atlassian.net/browse/CDAP-21212)).

  * Fixed an issue causing custom plugins to lose their logging context when running in parallel pipeline branches, ensuring consistent log propagation across both linear and parallel branched pipeline executions ([CDAP-21245](https://cdap.atlassian.net/browse/CDAP-21245)).

  * Fixed critical security vulnerabilities in CDAP ([CDAP-21250](https://cdap.atlassian.net/browse/CDAP-21250)).

  * Improved the latency of the **List pipelines** page ([CDAP-21244](https://cdap.atlassian.net/browse/CDAP-21244)).

  * Fixed an issue causing intermittent service unavailability after instance upgrades ([CDAP-21254](https://cdap.atlassian.net/browse/CDAP-21254)).




Change

Changes in Cloud Data Fusion 6.11.1.3:

  * Introduced a `deployStrategy` query parameter in the [Deploy Application API](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Create-an-Application) to skip the re-deployment of an existing pipeline if its configuration hasn't changed ([CDAP-21246](https://cdap.atlassian.net/browse/CDAP-21246)).



Change

The Snowflake plugin version 1.2.1 is available in Cloud Data Fusion version 6.11.1 and later. This release includes the following change:

  * Upgraded the Snowflake JDBC driver version from 3.14.4 to 4.0.2 and adapted to breaking API changes. This update migrates stream upload and download methods to use the new `UploadStreamConfig` and `DownloadStreamConfig` builders, updates OAuth2 authentication logic, and adds passphrase validation for key-pair authentication ([PLUGIN-1954](https://cdap.atlassian.net/browse/PLUGIN-1954)).



## May 18, 2026

Change

The HTTP plugin version 1.5.2 is available in Cloud Data Fusion version 6.11.1. This release includes the following change:

  * Fixed an issue in the HTTP plugin where OAuth2 token requests bypassed configured proxies, causing connection failures in restricted environments. Authentication requests now correctly route through the configured proxy ([PLUGIN-1956](https://cdap.atlassian.net/browse/PLUGIN-1956)).



Change

The Multi-table plugin version 1.4.2 is available in Cloud Data Fusion version 6.11.1 and later. This release includes the following changes:

  * Introduced informational logging to flag when source tables or custom SQL queries yield zero records, which improves data pipeline observability. The split-generation logic is also updated to handle empty tables and prevent false-alarm logs during multi-split processing ([PLUGIN-1950](https://cdap.atlassian.net/browse/PLUGIN-1950)).



## March 17, 2026

Fixed

Cloud Data Fusion version 6.11.1.2 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

This release includes the following changes:

  * Fixed an issue that caused pipelines to get stuck in the provisioning state when processing large run records ([CDAP-21234](https://cdap.atlassian.net/browse/CDAP-21234)).

  * Fixed the triggers panel in the pipeline details page to display the correct triggers count on initial load ([CDAP-21230](https://cdap.atlassian.net/browse/CDAP-21230)).

  * Updated the GraphQL query mechanism to cache the pipelines list and fix the long loading screen in the deployed pipelines list page ([CDAP-21229](https://cdap.atlassian.net/browse/CDAP-21229)).




## March 02, 2026

Change

The SAP ODP plugin version 0.12.1 is available in Cloud Data Fusion version 6.10 and later. This release includes the following features and changes:

  * Hierarchy data sources are now supported for extraction.

  * ODQ fields are populated with TSN, package number, and record number for full extraction.

  * Structured SAP messages are now displayed according to the message type (for example, type `E` as error and type `I` as information). Earlier, all messages from SAP displayed as errors.

  * You can now use the TVARVC table entries with parameter `/GOOG/ODP_TRANSFER_MODE` (for all data sources) or `/GOOG/M_DatasourceName` (for individual data sources) to determine if data is transferred in CHAR or XML format. Maintain 'C' to transfer data in CHAR format. Maintain an empty value to transfer data in XML format.




## February 09, 2026

Feature

Cloud Data Fusion version 6.11.1.1 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This release includes the following feature:

  * `InstanceV3` monitored-resource: Introduced `datafusion.googleapis.com/InstanceV3` as the default monitored resource for instance-level metrics and system service logs. This resource excludes the `org_id` and `namespace` labels found in `InstanceV2`. Emission of `InstanceV2` metrics and logs is disabled by default for new and upgraded instances but can be re-enabled using the REST API.

For more information, see [Metrics overview](https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview) and [View pipeline logs](https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs).




Fixed

Fixed in Cloud Data Fusion 6.11.1.1:

  * Fixed retries in message publishing when the messaging service is temporarily unavailable ([CDAP-21043](https://cdap.atlassian.net/browse/CDAP-21043)).
  * Fixed a security vulnerability where user-provided code in preview runners could access sensitive data from other preview runs ([CDAP-21211](https://cdap.atlassian.net/browse/CDAP-21211)).
  * Fixed an issue where internal task workers running user code could hang indefinitely. The system now forces completed tasks to exit and uses a health check to restart unresponsive workers ([CDAP-21213](https://cdap.atlassian.net/browse/CDAP-21213)).
  * Fixed an issue where the list apps API endpoint failed to return all deployed pipelines when used with pagination ([CDAP-21220](https://cdap.atlassian.net/browse/CDAP-21220)).



## January 29, 2026

Feature

The SAP Table Reader plugin version 0.11.5 is available in Cloud Data Fusion version 6.10 and later.

This release includes the following change:

  * Fixed an issue in the SAP Table Reader where running in Snapshot mode caused the Clean Up RFM process to generate an unnecessary `Job abort failed` error message in the detail logs.



## September 09, 2025

Change

The Salesforce plugin version 1.7.0 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following change:

  * Upgrade of Salesforce Bulk API V1 version from 62.0 to 64.0 ([PLUGIN-1926](https://cdap.atlassian.net/browse/PLUGIN-1926)).



Salesforce has deprecated certain fields in the API version 64.0. Upgrading to Salesforce plugin version 1.7.0 might cause pipelines that use these fields, to fail. To ensure your pipelines continue to work, you must manually update your pipeline schema to either load a new schema or remove the deprecated fields. For more information, see [Prerequisites for upgrading to Salesforce plugin version 1.7.0](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#upgrade-prereq).

## August 28, 2025

Change

The ServiceNow plugin version 1.2.7 is available in Cloud Data Fusion version 6.10.1. This release includes the following change:

  * Fixed an issue related to schema backward compatibility while upgrading from plugin version 1.1.0 ([PLUGIN-1902](https://cdap.atlassian.net/browse/PLUGIN-1902)).



## August 27, 2025

Feature

Cloud Data Fusion version 6.11.1 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This release includes the following features:

  * Added support for HTTP access tokens (Bearer authentication) in Bitbucket Server for [source control management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) ([CDAP-21049](https://cdap.atlassian.net/browse/CDAP-21049)).
  * A new API is available to retrieve the application count for each namespace ([CDAP-21161](https://cdap.atlassian.net/browse/CDAP-21161)).



Fixed

Fixed in Cloud Data Fusion 6.11.1:

  * To prevent storage issues on static Dataproc clusters, temporary pipeline data is automatically deleted after a successful run ([CDAP-21076](https://cdap.atlassian.net/browse/CDAP-21076)).
  * Fixed an issue that prevented [Expression Language (EL)](https://github.com/data-integrations/wrangler/blob/develop/wrangler-core/src/main/java/io/cdap/wrangler/expression/EL.java) from being used within user-defined directives ([CDAP-21204](https://cdap.atlassian.net/browse/CDAP-21204)).
  * Fixed an issue where a pipeline would fail when reading an encrypted file from Cloud Storage using Tink ([PLUGIN-1717](https://cdap.atlassian.net/browse/PLUGIN-1717)).



Deprecated

Dataproc 2.0 is no longer supported in Cloud Data Fusion version 6.11.1 and later.

Change

Changes in Cloud Data Fusion 6.11.1:

  * The Java runtime environment is upgraded from Java 8 to Java 11 ([CDAP-21184](https://cdap.atlassian.net/browse/CDAP-21184)).
  * To create ephemeral Dataproc clusters, Cloud Data Fusion uses the Dataproc 2.3 image by default ([CDAP-21187](https://cdap.atlassian.net/browse/CDAP-21187)).
  * The pipeline JSON size limit for creating new pipelines and importing pipelines as JSON is increased to 5MB (previously 2MB) ([CDAP-21194](https://docs.cloud.google.com/data-fusion/docs/release-notes/CDAP-21194)).
  * On the Pipeline details page, the inbound triggers sidebar features a paginated list of pipelines where you can select the pipelines you want to add to the trigger. Additionally, a refresh button is added to update the existing list of triggers and pipelines ([CDAP-21195](https://cdap.atlassian.net/browse/CDAP-21195)).



## July 25, 2025

Feature

You can now attach tags to Cloud Data Fusion instances during instance creation. This ensures immediate metadata for better organization, cost tracking, and policy automation. For more information, see [Attach tags during instance creation](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-with-tags#add-tags).

## July 23, 2025

Fixed

The Cloud Data Fusion version 6.10.1.5 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.5 includes reliability fixes.

## July 20, 2025

Change

The SAP ODP plugin version 0.12 is available in Cloud Data Fusion version 6.10 and later. This release includes the following changes:

  * Support for old SAP ODP RFCs is removed to align with SAP Note 3255746.
  * Messages have been updated when attempting to extract data from unsupported hierarchy data sources.



We recommend upgrading all your pipelines to the latest SAP ODP plugin version, as earlier versions are no longer compliant with SAP Guidelines.

**Note:** This release is backward compatible.

## July 16, 2025

Change

The Oracle plugin version 1.12.3 is available in Cloud Data Fusion (via Hub) versions 6.11.0 and later, and 1.11.8 is available in Cloud Data Fusion (via Hub) version 6.10.

This release provides backward compatibility for recent schema changes, including the following:

  * [Precisionless numbers](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_14_2023): In version 1.10.0, precisionless numbers were handled as strings.
  * [Improved timestamp handling](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_14_2023): Version 1.11.0 introduced improvements to timestamp handling.



To address backward compatibility for these changes, two new hidden fields are introduced in Oracle batch source configurations: `treatPrecisionlessNumAsDeci` and `treatAsOldTimestamp`. Both flags default to `false`. To enable these flags, edit the respective values in your exported connection JSON (if using connections) or pipeline JSON (if not using connections) before re-importing or re-deploying ([PLUGIN-1893](https://cdap.atlassian.net/browse/PLUGIN-1893)).

## June 12, 2025

Change

The Elasticsearch plugin version 1.11.0 is available in Cloud Data Fusion version 6.11.0. This release includes the following change:

  * Upgraded Hadoop version for Elasticsearch plugin compatibility ([PLUGIN-1881](https://cdap.atlassian.net/browse/PLUGIN-1881)).



## June 11, 2025

Change

The HTTP plugin version 1.4.4 is available in Cloud Data Fusion version 6.10.1. This release includes the following changes:

  * Implemented the Client Credentials Grant flow for HTTP OAuth2, enabling authorized clients to securely access data using the `client_credentials` grant type. Client credentials can be passed through Basic Authentication header, in the request body, or as query parameters ([PLUGIN-1872](https://cdap.atlassian.net/browse/PLUGIN-1872)).

  * Fixed an issue causing the HTTP Source plugin to throw a `NullPointerException` when the `BasePageIterator` received a null response ([PLUGIN-1894](https://cdap.atlassian.net/browse/PLUGIN-1894)).




## June 09, 2025

Change

Cloud Data Fusion is available in the `northamerica-south1` (Mexico) region. For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

## June 02, 2025

Change

The [Salesforce plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.10 is available in Cloud Data Fusion versions 6.10.1 and 6.11.0. This release includes the following changes:

  * Upgraded Salesforce API version from 53.0 to 62.0 ([PLUGIN-1891](https://cdap.atlassian.net/browse/PLUGIN-1891)).
  * Added a retry mechanism for all Salesforce API calls from the Salesforce plugin ([PLUGIN-1892](https://cdap.atlassian.net/browse/PLUGIN-1892)).



## May 16, 2025

Change

The DB plugin versions 1.11.7 and 1.12.2 are available in Cloud Data Fusion versions 6.10.1 and 6.11.0 respectively. This release includes the following change:

  * Added the `TRANSACTION_ISOLATION_LEVEL` property to DB Plugins (PostgreSQL, MySQL, and MSSQL).



## May 13, 2025

Change

The MariaDB Batch Source plugin versions 1.11.7 and 1.12.2 are available in Cloud Data Fusion versions 6.10.1 and 6.11.0 respectively. This release includes the following changes:

  * Fixed an issue related to the MariaDB `YEAR` data type causing pipeline failures when the date type was manually changed to `DATE`. Validation for this specific scenario is now skipped ([PLUGIN-1888](https://cdap.atlassian.net/browse/PLUGIN-1888)).

  * Fixed an issue that caused pipeline failures with a `java.lang.ClassNotFoundException: Class io.cdap.plugin.db.DBRecord not found` error, which was due to a class loading problem ([PLUGIN-1874](https://cdap.atlassian.net/browse/PLUGIN-1874)).

  * Added a committer to Database plugins to manage committing or rolling back entire tasks, depending on whether the task completes successfully or is aborted ([PLUGIN-1815](https://cdap.atlassian.net/browse/PLUGIN-1815)).




## March 31, 2025

Deprecated

Cloud Data Fusion version 6.9 is no longer supported. You should upgrade your instances to run in a [supported version](https://docs.cloud.google.com/data-fusion/docs/version-support-policy). For instructions, see [Manage version upgrades for instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## March 28, 2025

Change

The Python Transform plugin (version 2.3.2) is available in CDAP version 6.10.1. This includes bug fix for the deprecated `PROTOCOL_TLSv1` on Dataproc 2.0 and later. The issue occurs when earlier TLS versions, such as TLSv1 and TLSv1.1 are disabled by default due to security concerns. Applications relying on `ssl.PROTOCOL_TLSv1` in Python might fail and requires updates to use `ssl.PROTOCOL_TLSv1_2` or later.

## March 17, 2025

Feature

Cloud Data Fusion version 6.11.0 is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Cloud Data Fusion 6.11.0 offers high availability with reduced upgrade downtime.

Feature

When a pipeline run fails, you can retrieve detailed error information on the pipeline details page of the Cloud Data Fusion web interface.

Cloud Data Fusion classifies pipeline errors by category, reason, and message. This classification speeds up resolution and reduces the need to examine complex logs. For more information, see [Retrieve error information for a failed pipeline run](https://docs.cloud.google.com/data-fusion/docs/troubleshoot#pipeline).

Feature

You can view instance metrics and pipeline metrics in Cloud Monitoring and in the dashboard provided by Cloud Data Fusion. For more information, see [Metrics overview](https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview) and [Monitor Cloud Data Fusion system, instance, and pipeline health](https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views).

Feature

You can view instance logs and pipeline logs in Cloud Logging, and in the dashboard provided by Cloud Data Fusion. For more information, see [View Cloud Data Fusion logs](https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs).

Deprecated

The following APIs for downloading system service and pipeline run logs are deprecated in 6.11.0:

  * `GET /v3/namespaces/<NAMESPACE_ID>/apps/<APP_ID>/<PROGRAM_TYPE>/<PROGRAM_ID>/logs`
  * `GET /v3/system/services/<SERVICE_ID>/logs`



Deprecated

The ability to retrieve all applications without pagination using the `GET /v3/namespaces/<NAMESPACE_ID>/apps` endpoint is deprecated in 6.11.0.

Fixed

Fixed in Cloud Data Fusion 6.11.0:

  * Fixed a null pointer exception in the BigQuery multi-sink plugin when used without a reference name ([PLUGIN-1843](https://cdap.atlassian.net/browse/PLUGIN-1843)).

  * Fixed Joiner plugin failures observed on Dataproc 2.2-debian12 instances ([CDAP-21075](https://cdap.atlassian.net/browse/CDAP-21075)).

  * Fixed an issue that prevented pipelines from accepting empty input in Amazon S3 and Google Cloud Storage source plugins ([PLUGIN-1742](https://cdap.atlassian.net/browse/PLUGIN-1742)).

  * Fixed an issue in RBAC-enabled instances where the pipeline details page displayed an incorrect author name ([CDAP-21069](https://cdap.atlassian.net/browse/CDAP-21069)).




Change

Changes in Cloud Data Fusion 6.11.0:

  * To create ephemeral clusters, Cloud Data Fusion uses the Dataproc 2.2 image by default. For more information about its limitations in Cloud Data Fusion, see [Change the Dataproc image to version 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21).

  * The maximum concurrent runs limit for triggers is displayed in the console ([CDAP-21072](https://cdap.atlassian.net/browse/CDAP-21072)).

  * Added support for destination table write preference in the BigQuery Execute plugin ([PLUGIN-1438](https://cdap.atlassian.net/browse/PLUGIN-1438)).




Deprecated

The following APIs for searching and querying metrics are deprecated in 6.11.0:

  * `POST v3/metrics/query`
  * `POST v3/metrics/search`



Breaking

A soft limit of 2 MB for pipeline JSON size is introduced in 6.11.0. Pipelines exceeding this size might encounter deployment failures.

## January 29, 2025

Fixed

The [SAP OData plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin) version 0.11.6 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following change:

Fixed an issue causing pipeline deployments to fail due to SAP memory dumps when processing large datasets with macro filters: `ERROR Stage 'SAP OData' encountered : CDF_SAP_ODATA_01534 - Service validation failed. Root Cause:Invalid parametertype used at function`.

## January 21, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Data Fusion resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/data-fusion/docs/how-to/create-custom-constraints).

## January 13, 2025

Change

The [SAP SuccessFactors plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source) version 1.2.4 is available in Cloud Data Fusion version 6.8.0 and later. This release lets you use OAuth 2.0 for ODATA API authentication ([PLUGIN-1741](https://cdap.atlassian.net/browse/PLUGIN-1741)).

## December 19, 2024

Fixed

The Cloud Data Fusion version 6.10.1.2 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.2 includes the following changes:

  * You can generate audit logs that record data plane activities within your Cloud Data Fusion instance. [Data plane audit logging](https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging#api-interface-reference) is available in Preview for RBAC-enabled instances. 

  * To improve the API response time, by default, all program activity records older than 30 days are cleaned up. Any activity older than 30 days isn't visible in the Cloud Data Fusion studio ([CDAP-14950](https://cdap.atlassian.net/browse/CDAP-14950)).

  * When using role-based access control, performing the List Pipelines operation requires `datafusion.pipelines.list` permission, in addition to `datafusion.namespaces.get` permission. For more information, see [RBAC roles and permissions](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac-roles-and-permissions#permissions_for_common_actions) ([CDAP-20931](https://cdap.atlassian.net/browse/CDAP-20931)).

  * Fixed an issue causing the flow control metric, `flowcontrol.launching.count`, to overcount in cases where servers were restarted when a pipeline run was in progress ([CDAP-21046](https://cdap.atlassian.net/browse/CDAP-21046)).

  * Fixed an issue causing the flow control metric, `flowcontrol.launching.count`, to be stale after a restart when no pipelines were running ([CDAP-21048](https://cdap.atlassian.net/browse/CDAP-21048)).

  * Fixed an issue causing the default max concurrent runs limit for triggers not to appear in the web interface, making it difficult to tell if triggers were working as intended ([CDAP-21072](https://cdap.atlassian.net/browse/CDAP-21072)).

  * Fixed an issue causing the top panel of the **Studio** tab to disappear when you edited a pipeline draft that's based on a pipeline from an earlier Cloud Data Fusion version ([CDAP-21073](https://cdap.atlassian.net/browse/CDAP-21073)).

  * Improved performance by removing a call to the list apps API during pipeline deployment when checking if a pipeline already exists ([CDAP-21074](https://cdap.atlassian.net/browse/CDAP-21074)).




## December 17, 2024

Feature

Cloud Data Fusion supports the [CMEK organization policy](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## November 27, 2024

Fixed

The Snowflake plugin version 1.1.4 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following changes ([PLUGIN-1816](https://cdap.atlassian.net/browse/PLUGIN-1816)):

  * Fixed an issue in the Snowflake source causing pipelines to fail if fields contained decimals.
  * Fixed an issue in the Snowflake source causing pipelines to fail if data contained a backslash (`\`). You can set a new escape character using the `cdap.snowflake.source.escape` runtime argument.



Fixed

The Cloud SQL MySQL plugins version 1.11.5 is available in Cloud Data Fusion versions 6.10.0 and later. This release fixes an issue in the Cloud SQL MySQL sink causing pipelines to fail when the schema contains a MySQL reserved word ([PLUGIN-1017](https://cdap.atlassian.net/browse/PLUGIN-1017)).

## November 21, 2024

Fixed

The HTTP plugin version 1.4.3 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following changes ([PLUGIN-1810](https://cdap.atlassian.net/browse/PLUGIN-1810)):

  * In the HTTP streaming source, batch source, and batch sink, a `PATCH` option was added to the **HTTP Method** field.
  * Fixed an issue in the HTTP sink causing data loss when a pipeline didn't fail by default when a non-2xx response code was received.
  * Fixed an issue in the HTTP source causing a pipeline not to fail when the `get_schema` method was called and a non-2xx response code was received.



## November 18, 2024

Fixed

The Cloud SQL MySQL plugins version 1.11.5 is available in Cloud Data Fusion versions 6.8.0 and later. This release fixes an issue in the Cloud SQL MySQL sink causing pipelines to fail when the schema contains a MySQL reserved word ([PLUGIN-1017](https://cdap.atlassian.net/browse/PLUGIN-1017)). This note is incorrect; see entry for [November 27, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#November_27_2024).

Fixed

The [SAP table batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin) plugin version 0.11.5 is available in Cloud Data Fusion version 6.8.0 and later. This release fixes an issue causing the following error: `Error encountered while configuring the stage: Unable to access Cloud Storage or download JCo libraries from Cloud Storage`.

## November 08, 2024

Fixed

The Multiple table plugin version 1.4.1 is available in Cloud Data Fusion versions 6.10.1 and later. This release fixes an issue causing pipelines to fail if a Multiple database tables batch source's **Reference Name** field contains spaces. The field no longer accepts spaces ([PLUGIN-1752](https://cdap.atlassian.net/browse/PLUGIN-1752)).

## October 28, 2024

Fixed

The Oracle plugin version 1.11.4 is available in Cloud Data Fusion versions 6.10.1 and later. This release includes the following change:

  * Fixed an issue causing pipelines with an Oracle sink that has date columns in the input schema to fail ([PLUGIN-1812](https://cdap.atlassian.net/browse/PLUGIN-1812)).



## October 24, 2024

Issue

Using Dataproc version 2.2 in your Cloud Data Fusion pipeline can fail in some cases with the following error: `ERROR [Driver:o.a.s.d.y.ApplicationMaster@97] - User class threw exception: java.lang.NoSuchMethodError: 'org.apache.spark.sql.catalyst.encoders.ExpressionEncoder org.apache.spark.sql.catalyst.encoders.RowEncoder.apply(org.apache.spark.sql.types.StructType)' at io.cdap.cdap.etl.spark.batch.OpaqueDatasetCollection.toDataframeCollection(OpaqueDatasetCollection.java:111)`.  
To avoid this issue, [change the Dataproc image to 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21) ([CDAP-21075](https://cdap.atlassian.net/browse/CDAP-21075)).

## October 14, 2024

Fixed

The [SAP ODATA batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin) plugin version 0.11.5 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following changes:

  * Fixed an issue causing pipelines to fail when the source plugin contained nested fields (an array of records): `ERROR [Executor task launch worker for task 0.0 in stage 0.0 (TID 0):o.a.s.u.Utils@98] - Aborting task io.cdap.cdap.api.data.format.UnexpectedFormatException: Schema must be a record with at least one field.`

  * Added a **Read Timeout** plugin property, which lets you configure the read timeout value for long-running pipelines.




## September 26, 2024

Fixed

The [SAP ODP batch source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin) version 0.11.3 is available in Cloud Data Fusion versions 6.8.0 and later. This release includes the following changes:

  * Fixed an issue causing the following error: `Error encountered while configuring the stage: Unable to access Cloud Storage or download JCo libraries from Cloud Storage`. To address the issue, you must upgrade the Cloud Storage client library to version 2.3.0 or later.

  * Fixed an issue causing memory errors in the SAP system. You can choose to load changed data without loading historical data first. You can select this option in the plugin properties.




## September 23, 2024

Fixed

The Cloud Data Fusion version 6.10.1.1 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.1 includes the following changes:

  * Cloud Data Fusion stores lineage-related information for 30 days by default, in addition to [cleaning up run records](https://docs.cloud.google.com/data-fusion/docs/release-notes#July_18_2024) ([CDAP-21053](https://cdap.atlassian.net/browse/CDAP-21053)).
  * Added support to disable Field level lineage. For more information, see [Explore Data Lineage using metadata](https://docs.cloud.google.com/data-fusion/docs/tutorials/lineage#field_level_lineage) ([CDAP-21007](https://cdap.atlassian.net/browse/CDAP-21007)).
  * Cloud Data Fusion supports running pipelines using [Dataproc 2.2](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.2). For more information about its limitations in Cloud Data Fusion, which are unchanged from Dataproc 2.1, see [Change the Dataproc image to version 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21) ([CDAP-21047](https://cdap.atlassian.net/browse/CDAP-21047)). This note is incorrect; see entry for [October 24, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#October_24_2024).



Fixed

The Cloud Data Fusion version 6.9.2.4 patch revision is GA. 6.9.2.4 includes the following changes:

  * Cloud Data Fusion stores lineage-related information for 30 days by default, in addition to [cleaning up run records](https://docs.cloud.google.com/data-fusion/docs/release-notes#July_18_2024) ([CDAP-21053](https://cdap.atlassian.net/browse/CDAP-21053)).
  * Added support to disable Field level lineage. For more information, see [Explore Data Lineage using metadata](https://docs.cloud.google.com/data-fusion/docs/tutorials/lineage#field_level_lineage) ([CDAP-21007](https://cdap.atlassian.net/browse/CDAP-21007)).
  * Fixed an issue causing the maximum concurrent runs setting not to work as expected for scheduled pipeline runs ([CDAP-20988](https://cdap.atlassian.net/browse/CDAP-20988)).
  * Fixed an issue causing upgrades to fail when the schedule name had hyphens, spaces, or other symbols ([CDAP-20999](https://cdap.atlassian.net/browse/CDAP-20999)).



## September 19, 2024

Fixed

The [SAP SLT No RFC Replication plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-slt-plugin) version 0.11.3 is available in Cloud Data Fusion version 6.8.0 and later. This release fixes an issue causing the following error: `Error encountered while configuring the stage: Unable to access Cloud Storage or download JCo libraries from Cloud Storage`.

## September 06, 2024

Fixed

The CloudSQL MySQL plugin version 1.10.7 is available in Cloud Data Fusion versions 6.9.0 and 6.10.0. This plugin version lets you use a macro to specify the name of the CloudSQL instance in the plugin's **Connection name** field.

## September 01, 2024

Deprecated

Cloud Data Fusion version 6.8 is no longer supported. You should upgrade your instances to run in a [supported version](https://docs.cloud.google.com/data-fusion/docs/version-support-policy). For instructions, see [Manage version upgrades for instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## August 30, 2024

Fixed

Excel plugin version 2.12.3 is available in Cloud Data Fusion 6.10.0 and later. This version fixes an issue in the Excel batch source causing pipelines with large XLSX files to consume high memory and fail ([PLUGIN-1771](https://cdap.atlassian.net/browse/PLUGIN-1771) and [PLUGIN-1795](https://cdap.atlassian.net/browse/PLUGIN-1795)).

Fixed

Excel plugin version 2.11.5 is available in Cloud Data Fusion 6.9 versions. This version fixes an issue in the Excel batch source causing pipelines with large XLSX files to consume high memory and fail ([PLUGIN-1771](https://cdap.atlassian.net/browse/PLUGIN-1771) and [PLUGIN-1795](https://cdap.atlassian.net/browse/PLUGIN-1795)).

Fixed

Excel plugin version 2.10.3 is available in Cloud Data Fusion 6.8 versions. This version fixes an issue in the Excel batch source causing pipelines with large XLSX files to consume high memory and fail ([PLUGIN-1771](https://cdap.atlassian.net/browse/PLUGIN-1771) and [PLUGIN-1795](https://cdap.atlassian.net/browse/PLUGIN-1795)).

## July 31, 2024

Fixed

The Python transform plugin version 2.3.1 is available in Cloud Data Fusion version 6.10.1. The release lets you use a macro in the **Script** plugin property field to pass runtime arguments ([CDAP-21054](https://cdap.atlassian.net/browse/CDAP-21054)).

## July 18, 2024

Change

Cloud Data Fusion versions 6.9 and later store pipeline run records for 30 days by default. For more information, see [View run records](https://docs.cloud.google.com/data-fusion/docs/concepts/deploy-and-run-pipelines#view_run_records).

## July 15, 2024

Fixed

The Cloud Storage Copy/Move plugin version 0.23.2, which is bundled with Google Cloud Platform plugin, is available in Cloud Data Fusion versions 6.10.0 and later. The release lets you use a wildcard character (`*`) in the source path to copy and move multiple files. For example, the source path `gs://demo0/prod/reports/*.csv` copies and moves all CSV files in the `reports` directory ([PLUGIN-698](https://cdap.atlassian.net/browse/PLUGIN-698)).

## July 08, 2024

Feature

You can configure [maintenance windows](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-maintenance-windows) for Cloud Data Fusion instances, in versions 6.8 and later, in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 28, 2024

Fixed

The Cloud Storage Multi File sink plugin version 0.23.2 is available in Cloud Data Fusion version 6.10.1 and later. The release fixes an issue in the Cloud Storage Multi File sink causing pipelines to fail when the Flexible schema property was set to `true` ([PLUGIN-1780](https://cdap.atlassian.net/browse/PLUGIN-1780)).

## June 20, 2024

Fixed

The Oracle sink plugin version 1.10.7 is available in Cloud Data Fusion version 6.9. The release fixes an issue in the Oracle sink causing null values to be assigned to fields in the input schema that have lowercase letters in the field name ([PLUGIN-1793](https://cdap.atlassian.net/browse/PLUGIN-1793)).

## June 05, 2024

Fixed

The Google Sheets plugin version 1.4.3, which is bundled with the Google Drive plugins, is available in the Cloud Data Fusion Hub. The release includes the following changes:

  * Fixed an issue causing the Google Sheets plugin to incorrectly parse column names that have special characters ([PLUGIN-1785](https://cdap.atlassian.net/browse/PLUGIN-1785)).

  * Fixed an issue causing pipelines to fail when the Google Sheets plugin is used with Wrangler and any of the fields required to fetch schema was a macro ([PLUGIN-1791](https://cdap.atlassian.net/browse/PLUGIN-1791)).




## June 04, 2024

Feature

Cloud Data Fusion supports annotating resources with tags in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and [Control access with tags](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-with-tags).

## May 27, 2024

Fixed

The Decompress plugin version 1.2.1 is available in the Hub in Cloud Data Fusion version 6.10.1 and later. The release fixes an issue in the Decompress plugin causing concatenated GZIP files (`.gz`) to not decompress as intended. In version 1.2.1, decompression occurs until EOF is reached ([PLUGIN-1743](https://cdap.atlassian.net/browse/PLUGIN-1743)).

Fixed

The Cloud Storage Multi File sink plugin version 0.22.8 is available in Cloud Data Fusion version 6.9.2. The release fixes an issue in the Cloud Storage Multi File sink causing pipelines to fail when a Flexible schema was set to `true` ([PLUGIN-1780](https://cdap.atlassian.net/browse/PLUGIN-1780)).

## May 21, 2024

Feature

Cloud Data Fusion version 6.10.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the CDAP 6.10.1 release.

Feature

Creating a private instance with [Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect) is GA in Cloud Data Fusion version 6.10.1.

Feature

Per Namespace Service Accounts are GA in Cloud Data Fusion version 6.10.1. For more information, see [Access control with namespace service accounts](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace).

Feature

Syncing multiple pipelines from a namespace is GA in Cloud Data Fusion version 6.10.1, For more information, see [Sync Cloud Data Fusion pipelines with a remote repository](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management#sync-pipelines).

Fixed

The [SAP SuccessFactors batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source) version 1.2.3 is available in the Enterprise edition of Cloud Data Fusion 6.7.0 and later. This release lets you configure a proxy URL and SuccessFactors authentication properties.

Fixed

Fixed in Cloud Data Fusion 6.10.1:

  * Fixed an issue causing runtime arguments of pipeline triggers to not propagate to downstream pipelines ([CDAP-20947](https://cdap.atlassian.net/browse/CDAP-20947)).
  * Fixed an issue in Wrangler causing the `send-to-error-and-continue` directive to not initialize `dq_failure` when the condition is false ([PLUGIN-1736](https://cdap.atlassian.net/browse/PLUGIN-1736)).
  * Fixed an issue that occurs if running a replication pipeline when task workers are enabled ([CDAP-20951](https://cdap.atlassian.net/browse/CDAP-20951)).
  * Improved error reporting in the BigQuery Sink. Fixed an issue in BigQuery Argument Setter where validation error wasn't displayed correctly ([PLUGIN-788](https://cdap.atlassian.net/browse/PLUGIN-788), [PLUGIN-781](https://cdap.atlassian.net/browse/PLUGIN-781), [PLUGIN-782](https://cdap.atlassian.net/browse/PLUGIN-782), [PLUGIN-1318](https://cdap.atlassian.net/browse/PLUGIN-1318)).
  * Improved retries in BigQuery plugin ([PLUGIN-1715](https://cdap.atlassian.net/browse/PLUGIN-1715)).
  * Fixed an issue with the Python plugin, where running in native mode doesn't work as intended ([PLUGIN-1617](https://cdap.atlassian.net/browse/PLUGIN-1617)).
  * Fixed an issue causing certain connection parameters to not propagate in a MySQL connection ([PLUGIN-1728](https://cdap.atlassian.net/browse/PLUGIN-1728)).
  * Fixed an issue causing the Cloud Storage Copy action to timeout while working with large files ([PLUGIN-1735](https://cdap.atlassian.net/browse/PLUGIN-1735)).
  * Fixed an issue causing Copy and Move plugins to not create buckets at the destination path as expected, resulting in a runtime error ([PLUGIN-1738](https://cdap.atlassian.net/browse/PLUGIN-1738)). 
  * Fixed an issue causing empty source input to fail in multiple plugins ([PLUGIN-1742](https://cdap.atlassian.net/browse/PLUGIN-1742)).
  * Fixed an issue with remote execution of Wrangler directives causing type information to not be emitted ([PLUGIN-1778](https://cdap.atlassian.net/browse/PLUGIN-1778)).
  * Fixed an issue causing a `No record field provided`error ([CDAP-21024](https://cdap.atlassian.net/browse/CDAP-21024)).
  * Streaming pipelines in Cloud Data Fusion support the Excel source. Batch pipelines with an Excel source can consume high memory and fail in large pipelines ([PLUGIN-1771](https://cdap.atlassian.net/browse/PLUGIN-1771)).
  * Fixed an issue with using the Conditional plugin as a source for Wrangler, causing CDAP not to fetch the necessary schema ([CDAP-20890](https://cdap.atlassian.net/browse/CDAP-20890)).
  * Fixed an issue with instance upgrades causing existing schedule names to be improperly encoded in the URL, resulting in pre-upgrade failure ([CDAP-20999](https://cdap.atlassian.net/browse/CDAP-20999)).
  * Fixed an issue with schedules causing the maximum concurrent run property to not work as intended ([CDAP-20988](https://cdap.atlassian.net/browse/CDAP-20988)).
  * Fixed an issue causing committed ID to incorrectly propagate when pushing pipeline configurations to Git ([CDAP-20932](https://cdap.atlassian.net/browse/CDAP-20932)).



Change

Changed in Cloud Data Fusion 6.10.1:

  * [Source Control Management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) supports Bitbucket and Gitlab. 
  * Cloud Data Fusion uses the subnet used by the shared VPC network attachment in the default compute profile.
  * Added support for option string field (keep-strings) in `parse-xml-to-json` Wrangler directive ([CDAP-20934](https://cdap.atlassian.net/browse/CDAP-20934)).
  * The BigQuery sink plugin doesn't provide the **Dedupe By** option while in insert mode ([PLUGIN-900](https://cdap.atlassian.net/browse/PLUGIN-900)).
  * The BigQuery plugin supports the JSON type ([PLUGIN-1563](https://cdap.atlassian.net/browse/PLUGIN-1563)).
  * Improved error messages in the Spanner source ([PLUGIN-1748](https://cdap.atlassian.net/browse/PLUGIN-1748)). 
  * Improved retries in Pub/Sub plugin ([PLUGIN-1769](https://cdap.atlassian.net/browse/PLUGIN-1769)).



Breaking

Cloud Data Fusion version 6.10.1 has a known issue in the [Cloud Storage plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-cloud-storage-batch-source) causing pipelines to intermittently fail if the plugin contains a * regex pattern and uses Dataproc 2.0. To mitigate this issue:

  * [Change the Dataproc image to version 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21).
  * Use an older plugin version.
  * [Increase memory for the executor](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#memory-usage).



## April 26, 2024

Fixed

The HTTP plugin (version 1.4.2) is available in Cloud Data Fusion versions 6.8.0 and later. The release fixed an issue in the HTTP source causing an error in the retrieved schema when one of the retrieved columns contained a quoted value with a delimiter, such as a comma ([PLUGIN-1781](https://cdap.atlassian.net/browse/PLUGIN-1781)).

## April 17, 2024

Fixed

The Salesforce Marketing Cloud plugin (version 1.3.1) is available in Cloud Data Fusion version 6.8.0 and later. The release fixed an issue in the Salesforce Marketing sink plugin causing upsert operations to fail ([PLUGIN-1773](https://cdap.atlassian.net/browse/PLUGIN-1773)).

## April 04, 2024

Change

Cloud Data Fusion is available in the `africa-south1` region. For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

## April 02, 2024

Change

The [Google Sheets plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/763265042/Google+Sheets+Batch+Source) version 1.4.2 (bundled with the Google Drive plugins) is available in all Cloud Data Fusion versions. The release includes the following changes:

  * Macros are supported for the following OAuth fields: **Client ID** , **Client secret** , and **Refresh token** ([PLUGIN-1762](https://cdap.atlassian.net/browse/PLUGIN-1762)).
  * You can specify a single file ID in the **File identifier** field ([PLUGIN-1763](https://cdap.atlassian.net/browse/PLUGIN-1763)).
  * Added an **Access token** field, which supports macros ([PLUGIN-1764](https://cdap.atlassian.net/browse/PLUGIN-1764)).
  * You can turn on auto detection for the number of rows and columns ([PLUGIN-1766](https://cdap.atlassian.net/browse/PLUGIN-1766)).



## March 26, 2024

Feature

The [Amazon Redshift batch source connector](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-redshift-batch-source) version 1.11.1 is available in [Preview](https://cloud.google.com/products#product-launch-stages) in Cloud Data Fusion 6.10.0 and later. This source lets you load batch data from your Redshift dataset to a destination, such as BigQuery.

Change

Cloud Data Fusion is available in the following regions:

  * `asia-south2`
  * `me-central2`



For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

Feature

The [Amazon Redshift batch source connector](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-redshift-batch-source) version 1.10.6 is available in [Preview](https://cloud.google.com/products#product-launch-stages) in Cloud Data Fusion 6.9 versions. This source lets you load batch data from your Redshift dataset to a destination, such as BigQuery.

## March 18, 2024

Fixed

The [SAP Ariba batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source) plugin version 1.3.0 is available in the Cloud Data Fusion Enterprise edition, versions 6.7.0 and later. In plugin version 1.3.0, if a failure occurs, the plugin retries API calls. You can configure the retry parameters using the hidden fields in the pipeline configuration JSON.

## March 14, 2024

Fixed

[Salesforce plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.3 is available in Cloud Data Fusion versions 6.8.0 and later. The release includes the following changes:

  * Fixed an issue in the Salesforce sink plugin causing an unsupported type `datetime` error for **DateTime type** fields in the input schema. In this version, the Salesforce sink plugin supports datetime and decimal logical types ([PLUGIN-1749](https://cdap.atlassian.net/browse/PLUGIN-1749)).
  * Fixed an issue in all Salesforce plugins causing a pipeline to fail when using an OAuth macro because the oAuth macro value didn't get passed to the plugin as intended. In this version, all Salesforce plugins support an OAuth macro ([PLUGIN-1767](https://cdap.atlassian.net/browse/PLUGIN-1767)).
  * At the time of failure on the Salesforce sink side, if the **Error handling** property is set to the **Fail on error** option, the Salesforce job is aborted, which stops newer batches from being added to the job due to spark retry settings in CDAP ([PLUGIN-1768](https://cdap.atlassian.net/browse/PLUGIN-1768)).
  * To make debugging easier, additional debug logs and batch results in logs are available.



## March 12, 2024

Fixed

The Cloud Data Fusion version 6.9.2.3 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.9.2.3 includes the following fixes:

  * Skipped running `MetadataConsumerSubscriberService` when [Dataplex Data Lineage Integration](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex) is disabled ([CDAP-20947](https://cdap.atlassian.net/browse/CDAP-20947)).

  * Fixed an issue causing runtime arguments of pipeline triggers to not propagate to downstream pipelines ([CDAP-20943](https://cdap.atlassian.net/browse/CDAP-20943)).

  * Fixed an issue causing pipelines to fail in starting state when the system worker service is intermittently unavailable ([CDAP-20956](https://cdap.atlassian.net/browse/CDAP-20956)).

  * Fixed an issue causing pipelines to fail in starting state when the Compute Engine metadata server is intermittently unavailable ([CDAP-20955](https://cdap.atlassian.net/jira/software/c/projects/CDAP/issues/CDAP-20955)).




## February 29, 2024

Deprecated

Cloud Data Fusion version 6.7 is no longer supported. You should upgrade your instances to run in a [supported version](https://docs.cloud.google.com/data-fusion/docs/version-support-policy). For instructions, see [Manage version upgrades for instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## January 28, 2024

Change

Cloud Data Fusion is available in the following regions:

  * `europe-southwest1`
  * `europe-west8`
  * `europe-west9`
  * `europe-west12`
  * `me-central1`
  * `southamerica-west1`



For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

Change

Cloud Data Fusion supports patch revision upgrades in the Google Cloud console. For more information, see [Manage patch revisions for instances](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision).

## January 27, 2024

Change

Cloud Data Fusion lets you enable and disable Dataplex Lineage, as needed. When you create a new instance in Cloud Data Fusion version 6.8.0 and later, Dataplex Lineage is disabled by default. For more information, see [View lineage in Dataplex](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex).

## January 16, 2024

Feature

Cloud Data Fusion version 6.10.0 is available in [Preview](https://cloud.google.com/products#product-launch-stages). This release is in parallel with the [CDAP 6.10.0 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1962475531).

Feature

[Source control management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) using GitHub is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion version 6.10.0. With this feature, you can use GitHub to maintain version histories of your ETL and ELT pipelines. 

To simplify the experience of synchronizing pipelines between Cloud Data Fusion and GitHub in bulk, pushing and pulling multiple pipelines is available in Preview.

Feature

In versions before 6.10.0, you can only establish connectivity between private Cloud Data Fusion instances and customer resources with VPC Peering. Starting in version 6.10.0, you can use [Private Service Connect interfaces](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect) to establish connectivity using internal IP addresses. Private Service Connect interfaces are easier to set up, use fewer internal IP addresses, and don't require the use of proxies to reach customer resources in peered VPCs, the internet, or on-premises.

Change

Changes in Cloud Data Fusion 6.10.0:

  * Role-based access control in Cloud Data Fusion supports using the Cloud Data Fusion API Service Agent service account while emitting lineage events in RBAC-enabled instances. For more information, see [View lineage in Dataplex](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex).
  * To create ephemeral clusters, Cloud Data Fusion uses the Dataproc 2.1 image by default. For more information about its limitations in Cloud Data Fusion, see [Change the Dataproc image to version 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21) ([CDAP-20841](https://cdap.atlassian.net/browse/CDAP-20841)).
  * Cloud Data Fusion uses the [autoscaling Dataproc profile](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters) by default for ephemeral clusters. 
  * In [Source control management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management), GitHub PAT was removed from the Cloud Data Fusion web interface for repository configurations ([CDAP-20904](https://cdap.atlassian.net/browse/CDAP-20904) and [CDAP-20581](https://cdap.atlassian.net/browse/CDAP-20581)).
  * Improved latency when [BigQuery pushdown](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-transformation-pushdown) is enabled by fetching artifacts from a local cache ([CDAP-20846](https://cdap.atlassian.net/browse/CDAP-20846)).
  * The BigQuery sink supports flexible table names and column names ([PLUGIN-1718](https://cdap.atlassian.net/browse/PLUGIN-1718)).
  * BigQuery sinks support ingesting data to JSON data type fields([PLUGIN-1692](https://cdap.atlassian.net/browse/PLUGIN-1692)).
  * In BigQuery sink jobs, you can add labels in the form of key-value pairs ([PLUGIN-1705](https://cdap.atlassian.net/browse/PLUGIN-1705)).
  * In BigQuery execute jobs, you can add labels in the form of key-value pairs ([PLUGIN-1729](https://cdap.atlassian.net/browse/PLUGIN-1729)).
  * Added capability to run concurrent tasks in task workers ([CDAP-20868](https://cdap.atlassian.net/browse/CDAP-20868)).
  * If a task is stuck, task workers are forcefully restarted ([CDAP-20831](https://cdap.atlassian.net/browse/CDAP-20831)).
  * The Cloud Storage Java Client is upgraded to version 2.3 and later ([PLUGIN-1293](https://cdap.atlassian.net/browse/PLUGIN-1293)).
  * Wrangler is schema aware ([CDAP-15361](https://cdap.atlassian.net/browse/CDAP-15361)).
  * Added validation for incorrect credentials in the Amazon S3 source ([PLUGIN-1694](https://cdap.atlassian.net/browse/PLUGIN-1694)).



Feature

You can control access to Google Cloud resources at the Cloud Data Fusion namespace level using an IAM service account. Per Namespace Service Accounts are available in [Preview](https://cloud.google.com/products#product-launch-stages) in Cloud Data Fusion version 6.10.0. For more information, see [Access control with namespace service accounts](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace).

Change

To support the Private Service Connect integration, the following permissions are added to the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) role:

  * `compute.networkAttachments.get`
  * `compute.networkAttachments.update`
  * `compute.networkAttachments.list`



Fixed

Fixed in Cloud Data Fusion 6.10.0:

  * Fixed an issue in the Postgres DB plugin causing macros to be unsupported for database configuration ([PLUGIN-1681](https://cdap.atlassian.net/browse/PLUGIN-1681)).
  * Fixed an issue causing slowness in the API while fetching runs for all applications in a namespace ([CDAP-20587](https://cdap.atlassian.net/browse/CDAP-20587)).
  * Made the following fixes to Wrangler grammar ([CDAP-20839](https://cdap.atlassian.net/browse/CDAP-20839)): 
    * The `NUMERIC` token type supports negative numbers.
    * The `PROPERTIES` token type supports one or more properties.
  * Fixed an issue causing columns that have all null values to be dropped in Wrangler ([CDAP-20521](https://cdap.atlassian.net/browse/CDAP-20521)).
  * Fixed an issue causing pipeline upgrades to not have the intended description ([CDAP-20815](https://cdap.atlassian.net/browse/CDAP-20815)).



Deprecated

The Spark compute engine running on Scala 2.11 is not supported in Cloud Data Fusion version 6.10.0.

Deprecated

Dataproc 1.5 isn't supported in Cloud Data Fusion version 6.10.0.

Fixed

The [SAP BW Open Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-bwoh-batch-source-plugin) batch source plugin version 0.11.4 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following changes:

  * Fixed an issue causing the following error: `Error encountered while configuring the stage: Unable to access Cloud Storage or download JCo libraries from Cloud Storage`. To address the issue, you must upgrade the Google Storage Client library to version 2.3.0 or later.

  * Add a new plugin property, **Max. retries for read enqueue**.




## December 22, 2023

Fixed

The [Salesforce plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.2 is available in Cloud Data Fusion versions 6.8.0 and later. This version includes the following changes:

  * Fixed an issue in the Salesforce plugin causing the following error in some pipelines that run more than 4 hours: `java.lang.IllegalStateException: SSLException reading next record: javax.net.ssl.SSLException: Connection reset`. The [Connection timeout property](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#properties) was added to the Salesforce plugin properties in the web interface with the default value of 3600 seconds ([PLUGIN-1719](https://cdap.atlassian.net/browse/PLUGIN-1719)).

  * For accuracy, fixed schema handling for referenced object fields: child fields are explicitly marked as non-nullable, regardless of the schema values in the referenced object.




> In earlier versions, when retrieving schema information for fields in referenced objects, such as `contact.account_lastmodifieddate`, the schema inherits properties from the referenced object, causing incorrect non-nullable assumptions ([PLUGIN-1720](https://cdap.atlassian.net/browse/PLUGIN-1720)).

  * A retry mechanism was added in the Salesforce batch source and Multi-Source plugins for connection timeout issues ([PLUGIN-1706](https://cdap.atlassian.net/browse/PLUGIN-1706)).



## December 19, 2023

Fixed

The [SAP ODP batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin) plugin version 0.11.0 is available in Cloud Data Fusion versions 6.8.3 and later. The release includes the following changes:

  * Improved error logging, providing more information about the occurrence and mode of errors.
  * Improved the placeholder values in the **Filter options** fields.
  * Added support for fetching Operational Delta Queue (ODQ) fields by turning on the **Fetch delta fields** toggle.
  * On the **Properties** page for the plugin, changed the name of the **ObjectType** field to **Context**. For more information, see the ODP batch source [properties](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin#properties).



## December 14, 2023

Fixed

The Cloud Data Fusion version 6.9.2.2 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.9.2.2 includes the following fixes:

  * Increased the speed of the batch [`/runs`](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#batch_pipeline_run_records) API call for pipelines that are run thousands of times ([CDAP-20587](https://cdap.atlassian.net/browse/CDAP-20587)).
  * Fixed an issue causing draft pipelines to load incorrectly when you enable an accelerator that automatically installs plugins from a custom hub ([CDAP-20628](https://cdap.atlassian.net/browse/CDAP-20628)).
  * Fixed an issue causing the CDAP service IP to be cached forever ([CDAP-20781](https://cdap.atlassian.net/browse/CDAP-20781)).
  * Fixed an issue causing a `KubeTwillRunnerService` error on shutdown ([CDAP-20792](https://cdap.atlassian.net/browse/CDAP-20792)).
  * Fixed an issue causing pipelines and streaming jobs to fail after an AppFabric restart. ([CDAP-20797](https://cdap.atlassian.net/browse/CDAP-20797)).
  * Fixed an issue causing a slowdown in deploying applications ([CDAP-20820](https://cdap.atlassian.net/browse/CDAP-20820)).
  * Fixed an issue causing refreshed OAuth tokens to not be logged as expected, making it difficult to identify the root cause of some issues ([CDAP-20861](https://cdap.atlassian.net/browse/CDAP-20861)).
  * Fixed an issue in replication where you couldn't select the Tink transformation in the web interface. ([CDAP-20804](https://cdap.atlassian.net/browse/CDAP-20804)).



## December 06, 2023

Deprecated

Cloud Data Fusion versions 6.5 and 6.6 are no longer supported. You should upgrade your instances to run in a [supported version](https://docs.cloud.google.com/data-fusion/docs/version-support-policy). For instructions, see [Manage version upgrades for instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## November 14, 2023

Change

You can update the patch revision version of an instance by adding the optional `--patch_revision` argument to the [`gcloud beta data-fusion instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update) command. For more information, see [Manage patch revisions for instances](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision).

Change

You can apply a patch revision version when you create a new Cloud Data Fusion instance by adding the optional `--patch_revision` argument to the [`gcloud beta data-fusion instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create) command. For more information, see [Manage patch revisions for instances](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision).

## October 30, 2023

Fixed

The Cloud Data Fusion version 6.9.2.1 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). It fixes a regression that causes a pipeline to fail when using Dataproc secondary workers ([CDAP-20807](https://cdap.atlassian.net/browse/CDAP-20807)).

Fixed

The Cloud Data Fusion version 6.8.3.1 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). It fixes a regression that causes a pipeline to fail when using Dataproc secondary workers ([CDAP-20807](https://cdap.atlassian.net/browse/CDAP-20807)).

## October 23, 2023

Announcement

Cloud Data Fusion supports patch revisions. These revisions apply bug fixes between major releases. For more information, see [Versioning in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/versioning).

Fixed

The Cloud Data Fusion version 6.7.3.1 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). It introduces retries in the platform transaction layer to handle a `PSQLException` error thrown from broken database connections ([CDAP-19949](https://cdap.atlassian.net/browse/CDAP-19949) and [CDAP-20722](https://cdap.atlassian.net/browse/CDAP-20722)).

## October 20, 2023

Change

The BigQuery Replication plugin versions 0.8.4 and 0.7.3 are available in Cloud Data Fusion Enterprise edition versions 6.9 and 6.8, respectively. These releases include the following change: the BigQuery Replication sink lets you write data to other projects.

## October 18, 2023

Change

The Cloud Data Fusion [SAP SLT No RFC Replication plugin version 0.11.0](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-slt-plugin) is available in the Hub in Cloud Data Fusion enterprise edition versions 6.8.0 and later. It differs from the existing SAP SLT Replication plugin in the following ways:

  * All data and metadata file formats are in JSON.
  * No SAP RFC inbound calls occur in the SAP SLT No RFC Replication plugin. Accessing schemas and data from the SAP system no longer requires an SAP connection. Metadata and data extraction are sourced from the Cloud Storage bucket.



## September 07, 2023

Feature

Cloud Data Fusion version 6.9.2 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.9.2 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1916960793/CDAP+Release+6.9.2).

Feature

Features in Cloud Data Fusion 6.9.2:

  * [Editing deployed batch pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).
  * [Using Pub/Sub sources in streaming data pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-pubsub-streaming-source) is GA.
  * [Wrangler Filter Pushdown](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown#wrangler-filter-pushdown) is GA.
  * [Pushdown for window aggregations](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown#wrangler-filter-pushdown) is GA.



Change

Changes in Cloud Data Fusion 6.9.2:

  * Cloud Data Fusion supports setting [custom scopes](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#dataproc_vm_access_scopes) when creating a Dataproc cluster ([CDAP-19428](https://cdap.atlassian.net/browse/CDAP-19428)).
  * You can set common metadata labels for Dataproc clusters and jobs using the **Common Labels** property in the **Ephemeral Dataproc** compute profile ([CDAP-20698](https://cdap.atlassian.net/browse/CDAP-20698)).
  * You can set labels for the Dataproc jobs using the **Common Labels** property in the **Existing Dataproc** compute profile ([CDAP-20698](https://cdap.atlassian.net/browse/CDAP-20698)).
  * You can set a pipeline runtime argument with the key `system.profile.properties.labels` and a value representing the labels in the following format: `key1|value1;key2|value2`. This setting overrides the common labels set in the compute profile for pipeline runs ([CDAP-20698](https://cdap.atlassian.net/browse/CDAP-20698)).
  * Cloud Data Fusion supports using [Dataproc temp buckets](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket) in compute profiles ([CDAP-20712](https://cdap.atlassian.net/browse/CDAP-20712)).



Fixed

Fixed in Cloud Data Fusion 6.9.2:

  * Added a retry for Pub/Sub snapshot creation and deletion in a real-time pipeline with a Pub/Sub source when a retryable internal error is thrown ([PLUGIN-1660](https://cdap.atlassian.net/browse/PLUGIN-1660)).
  * Fixed a bug causing the Dynamic Spark plugins to fail when running on Dataproc 1.5 ([CDAP-20674](https://cdap.atlassian.net/browse/CDAP-20674)).
  * Fixed a discrepancy in warning and error counts reported between the pipeline summary tab and system logs ([CDAP-20680](https://cdap.atlassian.net/browse/CDAP-20680)).
  * Fixed a problem when, in rare cases, a cluster couldn't be found with [Cluster Reuse](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters) ([CDAP-20759](https://cdap.atlassian.net/browse/CDAP-20759)).
  * Fixed a bug causing the JavaScript transform to fail on Dataproc 2.1 ([CDAP-20778](https://cdap.atlassian.net/browse/CDAP-20778)).



## September 06, 2023

Change

The [SAP ODP plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin) version 0.7.5 is available in Cloud Data Fusion versions 6.6.0 to 6.8.0. This release includes the following changes:

  * Fixed an issue causing duplicate records or loss of records due to package acknowledgement occurring too early.
  * Filters that you apply are viewable in the logs.



## September 05, 2023

Fixed

The [SAP SuccessFactors Batch Source](https://docs.cloud.google.com/data-fusion/docs/reference/sap-successfactors-batch-source-reference) plugin version 1.2.1 is available in Cloud Data Fusion. The release includes the following changes:

  * Fixed an issue causing an inaccurate error message when the plugin's **Associated Entity Name** property is invalid.

  * Fixed an issue causing inaccurate validation errors when the **Expand Fields** property contains a macro.




## August 09, 2023

Fixed

In the [SAP Table Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin) version 0.10.0, fixed an issue causing failed data pipeline runs when you clicked the **Take a snapshot** toggle because the `FIELDS` parameters weren't exported.

## July 26, 2023

Fixed

In the [SAP SuccessFactors Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/reference/sap-successfactors-batch-source-reference) version 1.2.0, fixed an issue causing a null pointer exception when you provide a valid entity name that has more than one expand option separated by a '/'.

## July 20, 2023

Feature

[Workforce identity federation](https://docs.cloud.google.com/data-fusion/docs/concepts/security#workforce_identity_federation) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion.

Feature

The Cloud Data Fusion SAP ODP plugin supports [extracting data through CDS views](https://docs.cloud.google.com/data-fusion/docs/how-to/extract-data-through-cds-views).

Deprecated

Apache Hadoop MapReduce is deprecated in Cloud Data Fusion versions 6.7.0 and later ([CDAP-18913](https://cdap.atlassian.net/browse/CDAP-18913)).

## July 17, 2023

Change

In the SAP Ariba plugin 1.2.1, a **Token Endpoint field** that takes an authentication URL has been added to the plugin properties. The plugin is available in Cloud Data Fusion version 6.7 and later.

Fixed

In Cloud Data Fusion versions 6.7 and later, [SAP Ariba plugin](https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference) version 1.2.1 fixes the issue causing the following error after entering authentication credentials: `CDF_ARIBA_01501 - Failed to call given Ariba service`. This issue occurs when the SAP Ariba sandbox exists in the following locations: 

  * US 
  * EU
  * UAE
  * KSA



## July 13, 2023

Fixed

The [SAP OData plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin) (version 0.9.1) is available in the Cloud Data Fusion SAP Hub (all versions) with the following changes:

  * Fixed an issue in the SAP OData batch source causing you not to receive a valid error message if the base URL provided is invalid.
  * A warning has been added to the log message when you provide a batch size that is larger than the maximum allowed batch size.



## June 14, 2023

Feature

Cloud Data Fusion version 6.9.1 is in [Preview](https://cloud.google.com/products#product-launch-stages). This release is in parallel with the [CDAP 6.9.1 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1902084097/CDAP+Release+6.9.1).

Feature

Features in Cloud Data Fusion 6.9.1:

  * Cloud Data Fusion supports using [Source Control Management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) to manage pipeline versions through GitHub repositories. Source Control Management is available in [Preview](https://cloud.google.com/products#product-launch-stages) ([CDAP-20228](https://cdap.atlassian.net/browse/CDAP-20228)).

  * [Data Catalog Asset Lineage Integration](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex) is in [GA](https://cloud.google.com/products#product-launch-stages) in versions 6.8.0 and later. In version 6.9.1, it supports the Multiple Database Tables source and the BigQuery Multi Table sink.

  * Cloud Data Fusion supports [editing deployed pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline) ([CDAP-19425](https://cdap.atlassian.net/browse/CDAP-19425)).

  * Cloud Data Fusion supports [Window Aggregation operations](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown#window-aggregations) in Transformation Pushdown to reduce the pipeline execution time by performing SQL operations in BigQuery instead of Spark ([CDAP-19628](https://cdap.atlassian.net/browse/CDAP-19628)).

  * Cloud Data Fusion supports specifying filters in SQL in Wrangler and the pushdown of SQL filters in Wrangler to BigQuery. In the Wrangler transformation, added support for specifying preconditions in SQL, and added support for transformation pushdown for SQL preconditions. For more information, see [Wrangler Filter Pushdown](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown#wrangler-filter-pushdown) ([CDAP-20454](https://cdap.atlassian.net/browse/CDAP-20454)).

  * Cloud Data Fusion supports [Dataproc driver node groups](https://docs.cloud.google.com/dataproc/docs/guides/node-groups/dataproc-driver-node-groups). To use Dataproc driver node groups, when you [create the Dataproc cluster](https://docs.cloud.google.com/dataproc/docs/guides/node-groups/dataproc-driver-node-groups#create_a_driver_node_group_cluster), configure the following properties:

    * `yarn:yarn.nodemanager.resource.memory.enforced=false`
    * `yarn:yarn.nodemanager.admin-env.SPARK_HOME=$SPARK_HOME`
**Note:** The single quotation marks are important in the property when using the [gcloud CLI](https://docs.cloud.google.com/dataproc/docs/guides/node-groups/dataproc-driver-node-groups#create_a_driver_node_group_cluster) to create the cluster (`'yarn:yarn.nodemanager.admin-env.SPARK_HOME=$SPARK_HOME'`) so that the shell doesn't try to resolve the $ locally before submitting ([CDAP-20288](https://cdap.atlassian.net/browse/CDAP-20288)).
  * For the [Multiple Database Tables Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/718831924), added field-level lineage support ([CDAP-20440](https://cdap.atlassian.net/browse/CDAP-20440)).

  * Cloud Data Fusion version 6.9.1 supports the Dataproc image 2.1 compute engine, which runs in Java11. If you [change the Dataproc image to 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21), the JDBC drivers that the database plugins use in those instances must be compatible with Java11 ([CDAP-20543](https://cdap.atlassian.net/browse/CDAP-20543)).

  * Cloud Data Fusion supports the following improvements and changes for real time pipelines with a single Pub/Sub streaming source and no Windower plugins: 

    * The Pub/Sub streaming source has built-in support—data is processed at least once. 
    * Enabling Spark checkpointing isn't required. Pub/Sub streaming source creates a [Pub/Sub snapshot](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_to_a_snapshot) at the beginning of each batch and removes it at the end of each batch. 
    * The Pub/Sub Snapshot creation has a cost associated with it. For more information, see [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing#storage_costs). 
    * The snapshot creations can be monitored using [Cloud Audit logs](https://docs.cloud.google.com/pubsub/docs/audit-logging). 

For more information, see [Read from a Pub/Sub streaming source](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-pubsub-streaming-source) ([PLUGIN-1537](https://cdap.atlassian.net/browse/PLUGIN-1537)).




Change

Changes in Cloud Data Fusion 6.9.1:

  * Updated Cloud Data Fusion docker image dependencies to include fixes for security vulnerabilities.

  * Added the ability to configure Java options for a pipeline run by setting the `system.program.jvm.opts` runtime argument ([CDAP-20381](https://cdap.atlassian.net/browse/CDAP-20381)).

  * Replication pipelines generate logs for stats of events processed by source and target plugins at a fixed interval ([CDAP-20140](https://cdap.atlassian.net/browse/CDAP-20140)).

  * Streaming pipelines that use Spark checkpointing can use macros if the `cdap.streaming.allow.source.macros` runtime argument is set to true. Note that macro evaluation will only be performed for the first run in this case, then stored in the checkpoint. It will not be re-evaluated in later runs ([CDAP-20455](https://cdap.atlassian.net/browse/CDAP-20455)).

  * Improved performance of replication pipelines by caching schema objects for data events ([CDAP-20488](https://cdap.atlassian.net/browse/CDAP-20488)).

  * Added a launch mode setting to the Dataproc provisioners. When set to **Client** mode, the program launcher will run in the Dataproc job itself, and not as a separate YARN application. This reduces start-up time and cluster resources required, but may cause failures if the launcher needs more memory, such as when there's an action plugin that loads data into memory ([CDAP-20500](https://cdap.atlassian.net/browse/CDAP-20500)).

  * Removed duplicate backend calls when a program reads from the secure store ([CDAP-20504](https://cdap.atlassian.net/browse/CDAP-20504)).

  * Added support to upgrade Pipeline Post-run Action (Pipeline Alerts) plugins during the pipeline upgrade process ([CDAP-20567](https://cdap.atlassian.net/browse/CDAP-20567)).

  * Added Lifecycle microservices endpoint to delete a streaming application state for Kafka Consumer Streaming and Google Cloud Pub/Sub Streaming sources ([CDAP-20466](https://cdap.atlassian.net/browse/CDAP-20466)).




Fixed

Fixed in Cloud Data Fusion 6.9.1:

  * For SQL Server replication sources, fixed an issue on the **Review assessment** page, where SQL Server `DATETIME` and `DATETIME2` columns were shown as mapped to `TIMESTAMP` columns in BigQuery. This was a UI bug. The replication job mapped the data types to the BigQuery `DATETIME` type ([CDAP-19389](https://cdap.atlassian.net/browse/CDAP-19389)).

  * For replication jobs, fixed an issue where retries for transient errors from BigQuery might have resulted in data inconsistency ([CDAP-20276](https://cdap.atlassian.net/browse/CDAP-20276)).

  * Fixed an issue where a replication job got stuck in an infinite retry when it failed to process a DDL operation ([CDAP-20301](https://cdap.atlassian.net/browse/CDAP-20301)).

  * When you duplicate a pipeline, Cloud Data Fusion appends `_copy` to the pipeline name when it opens in the Pipeline Studio. In previous releases, Cloud Data Fusion appended `_<v1, v2, v3>` to the name ([CDAP-20373](https://cdap.atlassian.net/browse/CDAP-20373)).

  * Fixed the pipeline stage validation API to return unevaluated macro values to prevent secure macros from being returned ([CDAP-20430](https://cdap.atlassian.net/browse/CDAP-20430)).

  * Fixed an issue that sometimes caused pipelines to fail when running pipelines on Dataproc with the following error: `Unsupported program type: Spark`. The first time a pipeline that only contained actions ran on a newly created or upgraded instance, it succeeded. However, the next pipeline runs, which included sources or sinks, might have failed with this error ([CDAP-20431](https://cdap.atlassian.net/browse/CDAP-20431)).

  * Fixed an issue where the flow control [running count metric](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412753/Metrics#Running-metric) (`system.flowcontrol.running.count`) might be stale if no new pipelines or replication jobs were started ([CDAP-20458](https://cdap.atlassian.net/browse/CDAP-20458)).

  * Fixed an issue where executor resource settings are not honored when `app.pipeline.overwriteConfig` is set ([CDAP-20549](https://cdap.atlassian.net/browse/CDAP-20549)).

  * In the Oracle batch source, the Oracle `NUMBER` data type defined without precision and scale by default was mapped to Cloud Data Fusion `string` data type. If these fields were used by an Oracle Sink to insert into a `NUMBER` data type field in the Oracle table, the pipeline failed due to incompatibility between string and `NUMBER` type. Now, the Oracle Sink inserts these `string` types into `NUMBER` fields in the Oracle table ([PLUGIN-1481](https://cdap.atlassian.net/browse/PLUGIN-1481)).

  * For Oracle batch sources, fixed an issue that caused the pipeline to fail when there was a `TIMESTAMP WITH LOCAL TIME ZONE` column set to `NULLABLE` and the source had values that were `NULL(`[PLUGIN-1494](https://cdap.atlassian.net/browse/PLUGIN-1494)) .

  * Fixed an issue where pipelines that had a Database batch source and an Oracle sink that used a connection object (using SYSDBA) to connect to an Oracle database failed to establish a connection to the Oracle database. This was due to a package conflict between the Database batch source and the Oracle sink plugins ([PLUGIN-1503](https://cdap.atlassian.net/browse/PLUGIN-1503)).

  * Fixed an issue where pipelines failed when the output schema was overridden in certain source plugins. This was because the output schema didn't match the order of the fields from the query. This happened when the pipeline included any of the following batch sources:

  * Database

  * Oracle

  * MySQL

  * SQL Server

  * PostgreSQL

  * DB2

  * MariaDB

  * Netezza

  * Cloud SQL PostgreSQL

  * Cloud SQL MySQL

  * Teradata

Pipelines no longer fail when you override the output schema in these source plugins. Cloud Data Fusion uses the name of the field to match the schema of the field in the result set and the field in the output schema {[PLUGIN-1512](https://cdap.atlassian.net/browse/PLUGIN-1512)).

  * For BigQuery Pushdown, fixed an issue when BigQuery Pushdown was enabled for an existing dataset, the Location where the BigQuery Sink executed jobs was the location specified in the Pushdown configuration, not the BigQuery Dataset location. The configured Location should have only been used when creating resources. Now, if the dataset already exists, the **Location** for the existing dataset is used ([PLUGIN-1513](https://cdap.atlassian.net/browse/PLUGIN-1513)).

  * For the Database sink, fixed an issue where the pipeline didn't fail if there was an error writing data to the database. Now, if there is an error writing data to the database, the pipeline fails and no data is written to the database ([PLUGIN-1514](https://cdap.atlassian.net/browse/PLUGIN-1514)).

  * Fixed an issue that checks `GET` permission on a namespace which does not exist yet during the namespace creation flow ([CDAP-18394](https://cdap.atlassian.net/browse/CDAP-18394)).

  * Fixed an issue where Dataproc continued running a job when it couldn't communicate with the Cloud Data Fusion instance if the replication job or pipeline was deleted in Cloud Data Fusion ([CDAP-20216](https://cdap.atlassian.net/browse/CDAP-20216)).

  * Fixed an issue that caused pipelines with triggers with runtime arguments to fail after the instance was upgraded to Cloud Data Fusion 6.8.0 and 6.9.0 ([CDAP-20568](https://cdap.atlassian.net/browse/CDAP-20568)).

  * Fixed an issue where arguments set by actions and pipeline triggers don't overwrite runtime arguments. You must add the following runtime argument: `system.skip.normal.macro.evaluation=true` ([CDAP-20597](https://cdap.atlassian.net/browse/CDAP-20597)).

  * Fixed an issue that caused the Pipeline Studio page to show an incorrect count of triggers ([CDAP-20655](https://cdap.atlassian.net/browse/CDAP-20655)).

  * Fixed an issue that caused the Trigger's Payload Config to be missing in the UI for an upgraded instance ([CDAP-20660](https://cdap.atlassian.net/browse/CDAP-20660)).

  * Fixed bug where initial offset was not considered in Kafka batch source ([PLUGIN-1594](https://cdap.atlassian.net/browse/PLUGIN-1594)).




Deprecated

With the introduction of editing deployed pipelines in Cloud Data Fusion 6.9.1, the behavior of some APIs have significantly changed. Due to these changes, [some APIs are deprecated](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1888059393/CDAP+Release+6.9.0#Deprecations) ([CDAP-20030](https://cdap.atlassian.net/browse/CDAP-20030)).

Deprecated

In Cloud Data Fusion 6.9.1, all datasets except **FileSet** and **ExternalDataset** are deprecated and will be removed in a future release. All the deprecated datasets use the **Table** dataset in some form, which only works for programs running with the native provisioner on very old Hadoop releases ([CDAP-20667](https://cdap.atlassian.net/browse/CDAP-20667)).

## June 08, 2023

Feature

Cloud Data Fusion version 6.8.3 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.8.3 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1900806145/CDAP+Release+6.8.3).

Feature

Cloud Data Fusion 6.8.3 supports the ability to configure Java options for a pipeline run by setting the `system.program.jvm.opts` runtime argument ([CDAP-20381](https://cdap.atlassian.net/browse/CDAP-20381)).

Change

Cloud Data Fusion 6.8.3 supports upgrades in the Pipeline Post-run Action (Pipeline Alerts) plugins during the pipeline upgrade process ([CDAP-20567](https://cdap.atlassian.net/browse/CDAP-20567)).

Fixed

Fixed in 6.8.3:

  * Fixed an issue where the event publish feature did not work with RBAC-enabled instances ([CDAP-20375](https://cdap.atlassian.net/browse/CDAP-20375)).
  * Fixed an issue where executor resource settings were not honored when `app.pipeline.overwriteConfig` was set ([CDAP-20549](https://cdap.atlassian.net/browse/CDAP-20549)).
  * Fixed an issue that caused pipelines with triggers with runtime arguments to fail after the instance was upgraded to Cloud Data Fusion 6.8.0 and later ([CDAP-20568](https://cdap.atlassian.net/browse/CDAP-20568)).
  * Fixed an issue where arguments set by actions and pipeline triggers don't overwrite runtime arguments. You must add the following runtime argument: `system.skip.normal.macro.evaluation=true` ([CDAP-20597](https://cdap.atlassian.net/browse/CDAP-20597)).
  * Fixed an issue that caused the **Studio** page to show an incorrect count of triggers ([CDAP-20655](https://cdap.atlassian.net/browse/CDAP-20655)).
  * Fixed an issue that caused the Trigger's Payload Config to be missing in the UI for an upgraded instance ([CDAP-20660](https://cdap.atlassian.net/browse/CDAP-20660)).
  * Fixed an issue in the BigQuery Sink where the absence of an ordering key caused an exception ([PLUGIN-1582](https://cdap.atlassian.net/browse/PLUGIN-1582)).
  * Fixed an issue where initial offset was not considered in the Kafka Batch Source ([PLUGIN-1594](https://cdap.atlassian.net/browse/PLUGIN-1594)).



## June 07, 2023

Feature

Zendesk plugins version 1.2.0 is available in the Cloud Data Fusion Hub. The following changes are included in version 1.2.0:

  * [Zendesk Multi Objects Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/758743149/Zendesk+Multi+Objects+Batch+Source) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 
  * The Zendesk plugins support [Connection Management](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).



## June 02, 2023

Feature

The [SAP Ariba Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can connect your data pipeline to an SAP Ariba Source and a BigQuery Sink with this plugin in Cloud Data Fusion versions 6.5.1 and later.

Feature

The [SAP SuccessFactors Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source) is [GA](https://cloud.google.com/products#product-launch-stages). You can connect your data pipeline to an SAP SuccessFactors Source and a BigQuery Sink with this plugin in Cloud Data Fusion versions 6.5.1 and later.

## April 26, 2023

Feature

Cloud Data Fusion version 6.8.2 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.8.2 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1890648065/CDAP+Release+6.8.2).

Fixed

Cloud Data Fusion version 6.8.2 fixes an issue in Cloud Data Fusion versions 6.8.0 and 6.8.1 that may cause the following error: `Unsupported program type: Spark`. The first time a pipeline that only contains actions runs on a newly created or upgraded instance, it succeeds. However, following pipeline runs that also include sources or sinks may fail with this error. For updated settings, see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting-unsupported-program-error).

## March 29, 2023

Fixed

In Cloud Data Fusion version 6.8.1, Dataproc clusters no longer require the following OAUTH scope to function: `https://www.googleapis.com/auth/cloud-platform`.

## March 22, 2023

Breaking

In Cloud Data Fusion versions 6.8.0 and 6.8.1, there's a known issue that may cause the following error: `Unsupported program type: Spark`. The first time a pipeline that only contains actions runs on a newly created or upgraded instance, it succeeds. However, following pipeline runs that also include sources or sinks may fail with this error. For updated settings, see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting-unsupported-program-error).

## March 20, 2023

Change

Salesforce plugins version 1.4.4 is available in all supported Cloud Data Fusion versions with the following changes: 

  * In the [Salesforce Sink](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690848376), added the **Concurrency Mode** property to let you configure the plugin for parallel or serial concurrency. The default value is `Parallel`. Use this property to help resolve lock contention issues with the [Salesforce Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_planning_guidelines.htm). 

  * In the [Salesforce Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690848132), [Salesforce Multi Object Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690815326), [Salesforce Streaming Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/745996519), and [Salesforce Sink](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690848376), added the **Connection Timeout** property, which lets you set the maximum time in milliseconds to wait for connection initialization before it times out. The default value is `30000` ([PLUGIN-1533](https://cdap.atlassian.net/browse/PLUGIN-1533)).

  * In the [Salesforce Streaming Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/745996519), improved error handling in the pipeline logs ([PLUGIN-1469](https://cdap.atlassian.net/browse/PLUGIN-1469)).




## March 14, 2023

Fixed

Oracle plugins version 1.8.6 is available in Cloud Data Fusion versions 6.7.1, 6.7.2, and 6.7.3. Oracle plugins version 1.9.2 is available in Cloud Data Fusion versions 6.8.0 and later. These plugin versions have the following changes:

For the [Oracle Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705167716/Oracle+Batch+Source), fixed a backward compatibility issue. In plugin versions 1.8.3, 1.9.0, and earlier, Cloud Data Fusion maps the Oracle `NUMBER` data type with undefined precision and scale to CDAP `decimal(38,0)` , which can cause data loss due to rounding errors. In plugin versions 1.8.4, 1.8.5, and 1.9.1, the Oracle `NUMBER` data type with undefined precision and scale maps to the CDAP `string` data type by default, which preserves all decimal digits. In versions 1.8.6 and 1.9.2, the Oracle `NUMBER` data type with undefined precision and scale gets mapped to CDAP `string` by default and lets you edit the output schema to use the older mapping to `decimal(38, 0)` data type. For more information, see [Oracle batch source plugin converts NUMBER to string](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#oracle-data-type) ([PLUGIN-1535](https://cdap.atlassian.net/browse/PLUGIN-1535) ).

## March 08, 2023

Feature

[SAP BW OHD](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-bwoh-batch-source-plugin), [SAP ODP](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin), [SAP OData](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin), [SAP SLT](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-slt-plugin), and [SAP Table](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin) plugins version 0.8 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion versions 6.8.0 and later.

## February 28, 2023

Feature

Cloud Data Fusion version 6.8.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.8.1 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1872232449/CDAP+Release+6.8.1).

Fixed

Fixed in 6.8.1:

  * Fixed an issue in instances with role-based access control where deployment and validations failed with `read time out` error after a short time.

  * Fixed an issue that caused replication assessment for Oracle by Datastream to fail when an instance had role-based access control.

  * Fixed an issue that allowed reading secure keys in the system namespace with only the Data Fusion Viewer role (`datafusion.viewer`) or Instance Accessor role (`datafusion.accessor`). For more information about predefined roles for role-based access control in Cloud Data Fusion, see the [Role-based access control (RBAC) overview](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles). 

  * Fixed an issue where the Replication Source plugin's event reader was not stopped by the Delta worker when there were errors, which caused leakage of the plugin's resources ([CDAP-20394](https://cdap.atlassian.net/browse/CDAP-20394)). 

  * Fixed an issue that occurred in certain upgrade scenarios, where pipelines didn't have the **Use Connection** property set and the UI didn't display a plugin's connection properties, such as **Project ID** and **Service Account Type** ([CDAP-20392](https://cdap.atlassian.net/browse/CDAP-20392)).

  * Fixed an issue that caused pipelines to fail if they used a connection property, such as the **Service Account JSON** property, that used a secure macro with JSON as the value ([CDAP-20271](https://cdap.atlassian.net/browse/CDAP-20271)).

  * For Oracle by Datastream Replication sources, fixed an issue where the **Review Assessment** page would freeze when a selected or manually-entered table didn't exist in the source database ([CDAP-20257](https://cdap.atlassian.net/browse/CDAP-20257)).

  * For Oracle by Datastream Replication sources, fixed an issue where the **Select tables and transformations** page failed to load the list of tables and displayed the error `deadline exceeded` when the source database contained a large number of tables ([CDAP-20199](https://cdap.atlassian.net/browse/CDAP-20199)). 

  * Fixed an error in security-enabled instances that caused pipeline launch to fail and return a `token expired` error when evaluating secure macros in provisioner properties ([CDAP-20146](https://cdap.atlassian.net/browse/CDAP-20146)).

  * For [MySQL Replication sources](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/mysql-to-bigquery), fixed an issue that caused Replication jobs to fail during the initial snapshot, if the job included a runtime argument with the Debezium property, [`binary-handling-mode`](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-property-binary-handling-mode) ([CDAP-20121](https://cdap.atlassian.net/browse/CDAP-20121)).

  * For Replication jobs, increased retry duration for API calls to update state/offsets in Replication jobs ([CDAP-20028](https://cdap.atlassian.net/browse/CDAP-20028)).

  * Fixed an issue that prevented upgrades for MySQL and SQL Server Replication jobs in version 6.6.0. Upgrades are supported from version 6.6.0 to 6.7.3 and 6.8.1 ([CDAP-19622](https://cdap.atlassian.net/browse/CDAP-19622)).

  * Fixed upgrades for Oracle by Datastream Replication jobs. You can upgrade Oracle by Datastream Replication jobs from Cloud Data Fusion versions 6.6.0 and 6.7 to version 6.8.1. ([CDAP-20013](https://cdap.atlassian.net/browse/CDAP-20013)).




Change

Changes in Cloud Data Fusion 6.8.1:

  * Cloud Data Fusion supports upgrades for real-time pipelines that have a Kafka Consumer Streaming source from version 6.8.0 to 6.8.1 after you [upgrade your environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

  * ~~Starting in Cloud Data Fusion 6.8.1, Dataproc clusters require the following OAUTH scope to function:`https://www.googleapis.com/auth/cloud-platform`.~~ This scope is no longer required as of [March 29, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_29_2023).

  * March 17, 2023 release note addition: The Oracle Batch Source version 1.9.1 (which comes with Cloud Data Fusion 6.8.1) reads the Oracle `NUMBER` data type with undefined precision and scale as a `string` in Cloud Data Fusion. In previous versions, Cloud Data Fusion reads the Oracle `NUMBER` data type with undefined precision and scale as `decimal (38,0)`, which could result in data loss. For more information, see [Troubleshooting](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1881505800/Oracle+batch+source+plugin+versions+1.9.1+and+1.8.5+converts+Oracle+NUMBER+data+type+with+undefined+precision+and+scale+to+CDAP+string) ([PLUGIN-1119](https://cdap.atlassian.net/browse/PLUGIN-1119)).




Change

March 17, 2023 release note addition: The Oracle Batch Source version 1.8.5 (which comes with Cloud Data Fusion 6.7.3) reads the Oracle `NUMBER` data type with undefined precision and scale as a `string` in Cloud Data Fusion. In plugin versions 1.8.3 and earlier, Cloud Data Fusion reads the Oracle `NUMBER` data type with undefined precision and scale as `decimal (38,0)`, which could result in data loss. For more information, see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#oracle-data-type) ([PLUGIN-1119](https://cdap.atlassian.net/browse/PLUGIN-1119)).

Feature

Cloud Data Fusion version 6.7.3 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.7.3 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1872363521/CDAP+Release+6.7.3).

Fixed

Fixed in 6.7.3:

  * Fixed an issue that allowed reading secure keys in the system namespace with only the Data Fusion Viewer role (`datafusion.viewer`) or Instance Accessor role (`datafusion.accessor`). For more information about predefined roles for role-based access control in Cloud Data Fusion, see the [Role-based access control (RBAC) overview](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles). 

  * Fixed an issue in the BigQuery Replication Target plugin that caused Replication jobs to fail when the BigQuery target table already existed. The new version of the plugin will automatically be used in new Replication jobs ([CDAP-19599](https://cdap.atlassian.net/browse/CDAP-19599)).

  * Fixed an issue that prevented upgrades for MySQL and SQL Server Replication jobs in version 6.6.0. Upgrades are supported from version 6.6.0 to 6.7.3 and 6.8.1 ([CDAP-19622](https://cdap.atlassian.net/browse/CDAP-19622)).

  * Fixed an issue that prevented upgrades for Oracle by Datastream Replication jobs in version 6.6.0. Upgrades are supported from versions 6.6.0 , 6.7.0, 6.7.1, and 6.7.2 to version 6.7.3 ([CDAP-20013](https://cdap.atlassian.net/browse/CDAP-20013)).

  * Fixed an issue that caused pipelines to fail if they used a connection property, such as the **Service Account JSON** property, which used a secure macro with JSON as the value ([CDAP-20271](https://cdap.atlassian.net/browse/CDAP-20271)).

  * Fixed an issue that occurred in certain upgrade scenarios, where pipelines didn't have the **Use Connection** property set and the UI didn't display a plugin's connection properties, such as **Project ID** and **Service Account Type** ([CDAP-20392](https://cdap.atlassian.net/browse/CDAP-20392)).

  * Fixed an issue where the Replication Source plugin's event reader was not stopped by the Delta worker when there were errors, which caused leakage of the plugin's resources ([CDAP-20394](https://cdap.atlassian.net/browse/CDAP-20394)).

  * Fixed an error in security-enabled instances that caused pipeline launch to fail and return a `token expired` error when evaluating secure macros in provisioner properties ([CDAP-20146](https://cdap.atlassian.net/browse/CDAP-20146)).

  * In the Oracle Batch Source (version 1.8.4 and earlier), when the source data included fields with the `NUMBER` data type with undefined precision and scale, Cloud Data Fusion read it as `decimal` and set the precision to `38` and the scale to `0`. If any values in the field had scale other than `0`, values were rounded, which could have resulted in data loss. If the scale for this field is overridden in the plugin output schema, the pipeline fails.   
  
In Oracle batch source version 1.8.5, you can edit the scale of the CDAP `decimal` data type in the output schema. The overridden value is used to map to the Oracle `NUMBER` data type without failing the pipeline. If there are any numbers present in the fields with a scale greater than the scale defined in the plugin, Cloud Data Fusion rounds the values based on the scale you set in the output schema. For example, if you specify `precision=10`, `scale=3`, the value `123.4567` is rounded to `123.457`. For more information about setting precision and scale in a plugin, see [Changing the precision and scale for decimal fields in the output schema](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1124171777) ([PLUGIN-1433](https://cdap.atlassian.net/browse/PLUGIN-1433)).

  * Improved performance for batch pipelines with MySQL sinks ([PLUGIN-1374](https://cdap.atlassian.net/browse/PLUGIN-1374)).

  * For Database plugins (version 2.9.3), fixed a security issue where the database username and password were exposed in the logs ([CDAP-20235](https://cdap.atlassian.net/browse/CDAP-20235)).




## February 23, 2023

Feature

FTP Plugins versions 3.1.0 and 3.2.0 are generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion versions 6.7.2+ and 6.8.0+, respectively. They include support for more file formats and properties. An issue was fixed in the FTP Batch Source that caused pipelines to fail when running with Dataproc 2.0. For more information, see the [CDAP Hub release log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log).

## January 05, 2023

Feature

The [SAP SuccessFactors Batch Source](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source) plugin is available in [Preview](https://cloud.google.com/products#product-launch-stages). You can connect your data pipeline to an SAP SuccessFactors Source and a BigQuery Sink with this plugin in Cloud Data Fusion versions 6.5.1 and later.

## December 15, 2022

Feature

Cloud Data Fusion integrates with Data Catalog for [asset level lineage](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex) in [Preview](https://cloud.google.com/products?hl=en#product-launch-stages).

## December 14, 2022

Feature

Cloud Data Fusion is available in the following regions: 

  * `us-east5`
  * `us-south1`



For more information, see [Locations](https://cloud.google.com/functions/docs/locations) and [Pricing](https://docs.cloud.google.com/data-fusion/pricing).

## December 07, 2022

Feature

Cloud Data Fusion is available in the following region: 

  * `me-west1`



For more information, see [Locations](https://cloud.google.com/functions/docs/locations) and [Pricing](https://docs.cloud.google.com/data-fusion/pricing).

## December 06, 2022

Feature

Cloud Data Fusion version 6.8.0 is in [Preview](https://cloud.google.com/products#product-launch-stages). This release is in parallel with the [CDAP 6.8.0 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1845067785/CDAP+Release+6.8.0).

Change

In Cloud Data Fusion 6.8.0, Reference name is no longer mandatory for the following plugins:

  * BigQuery Source
  * BigQuery Sink
  * Dataplex Source
  * Dataplex Sink
  * Spanner Sink
  * Cloud Storage Sink



For these plugins, their unique identifiers in lineage are generated based on their configuration properties. For example, project `ID+dataset+table` is used as a unique identifier for BigQuery. This identifier can be seen on the lineage diagram. For more information, see [Cloud Data Fusion Plugins](https://docs.cloud.google.com/data-fusion/plugins).

Feature

Features in 6.8.0:

  * [Replication from Oracle to BigQuery using Datastream](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

  * Cloud Data Fusion supports [BigQuery batch source pushdown](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown#source-pushdown).

  * Cloud Data Fusion supports _AND_ [triggers](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382141391/Using+Triggers#Create-an-inbound-trigger-on-a-downstream-pipeline). You can create _OR_ and _AND_ triggers. Previously, all triggers were _OR_ triggers.




Change

Changes in 6.8.0:

  * For [Replication jobs with an Oracle (by Datastream) source](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery), ensured data consistency when multiple CDC events are generated with the same timestamp, by ordering events reliably.

  * For Oracle replication sources, added a [purge policy](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1749778437/Oracle+by+Datastream+Replication+Source#Purge-Policy-\(6.8.0-and-later\)) for a Cloud Storage bucket created by the plugin where Datastream writes its output. 

  * In the [Oracle replication source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1749778437/Oracle+by+Datastream+Replication+Source), added the **GCS Bucket Location** property, where Datastream writes its output. 

  * In the [Oracle replication source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1749778437/Oracle+by+Datastream+Replication+Source), added the list of Datastream regions to the **Region** property. You no longer need to manually enter the Datastream region.

  * The Oracle replication source identifies each row by the Primary key of the table. Previously, the plugin identified each row by the `ROWID`.

  * For Replication jobs, improved performance for Review Assessment.

  * Splitter Transformation based plugins have access to `prepareRun()` and `onRunFinish()` methods. 

  * In Wrangler, added the Average [`arithmetic`](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1827602441/Average+function) function, which calculates the average of the selected columns.

  * In Wrangler, [Numeric functions](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/413466692) support 3 or more columns.

  * In the [Dataplex Sink](https://docs.cloud.google.com/dataplex/docs/ingest-with-data-fusion) plugin, added the **Update Dataplex Metadata** property, which adds support for updating metadata in Dataplex for newly generated data.

  * In the [GCS Delete Action](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464945207) plugin, added support for bulk deletion of files and folders. You can use the (`*`) wildcard character to represent any character.




Fixed

Fixed in 6.8.0:

  * For custom Dataproc compute profiles, fixed the issue causing the wrong Cloud Storage bucket to be used to stage data. Cloud Data Fusion uses the bucket specified in the custom compute profile.

  * Fixed the issue in the BigQuery Replication Target plugin causing Replication jobs to fail when the BigQuery target table already existed. The new version of the plugin is used by default in new Replication jobs. To use the new plugin version in existing jobs, recreate the job.

  * Fixed an issue causing the **Replication Assessment** to get stuck when the Oracle (by Datastream) storage bucket property was empty, or had an invalid bucket name. Cloud Data Fusion returns a `400` error code during assessment when the property is empty or has an invalid bucket name.

  * Fixed an issue causing Replication jobs to fail when the source column name didn't comply with BigQuery table naming conventions. In 6.8.0, if a source column name doesn't comply with BigQuery naming conventions, Cloud Data Fusion replaces invalid characters with an underscore, prepends an underscore when the first character is a number, and truncates the name when it exceeds the maximum length. 

  * In the File batch source, fixed an issue causing **Get Schema** to appear only when **Format** was set to `delimited`. **Get Schema** appears for all formats. 

  * Fixed an issue with the output schema when connecting a Splitter transformation with a Joiner transformation.

  * Fixed an issue causing imports in the Cloud Data Fusion UI to fail for pipelines exported through the Pipeline Microservices.

  * In the Oracle Batch Source, when the source data included fields with the `Numeric` data type (undefined precision and scale), Cloud Data Fusion set the precision to `38` and the scale to `0`. If any values in the field had scale other than `0`, Cloud Data Fusion truncated the values, which could have resulted in data loss. If the scale for a field was overridden in the plugin output schema, the pipeline failed. For more information, see the [CDAP 6.8.0 bug fixes](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1845067785/CDAP+Release+6.8.0#Bug-Fixes).

  * In the Wrangler transformation, fixed the issue causing the pipeline to not fail when the **Error Handling** property was set to `Fail Pipeline`. This happened when an error was returned, but no exception was thrown, and there were `0` records in the output. For example, this happened when one of the directives (such `as.parse-as-simple-date`) failed because the input data wasn't in the correct format. This fix is not available by default. Instead, contact support if you need this fix for your projects. 

  * In Wrangler, fixed the issue causing the Wrangler page to get stuck when a BigQuery table name contained non-alphanumeric characters, such as underscores. Wrangler imports BigQuery tables that follow [BigQuery table naming conventions](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).




Breaking

Upgrading the Cloud Data Fusion version for Replication jobs is broken. Upgrading Replication jobs to Cloud Data Fusion version 6.8.0 isn't recommended.

## December 01, 2022

Feature

Google Cloud Platform Plugins version 0.20.4 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion versions 6.7.1 and 6.7.2. This version includes Dataplex [Source](https://docs.cloud.google.com/dataplex/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/dataplex/docs/ingest-with-data-fusion) plugins in GA. For more information, see the [CDAP Hub release log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#May-23%2C-2022).

Feature

Google Cloud Platform Plugins version 0.19.3 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion version 6.6.0. This version includes Dataplex [Source](https://docs.cloud.google.com/dataplex/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/dataplex/docs/ingest-with-data-fusion) plugins in GA. For more information, see the [CDAP Hub release log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#May-23%2C-2022).

## November 30, 2022

Deprecated

Cloud Data Fusion version 6.4 is no longer [supported](https://docs.cloud.google.com/data-fusion/docs/support/version-support-policy) as of December 1, 2022. You should upgrade your instances to run in a supported version. For instructions, see [Upgrading your Cloud Data Fusion environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## November 08, 2022

Feature

[DNS Resolution](https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use domain or hostnames for sources instead of IP addresses for pipeline design-time activities, such as getting schema, wrangling, and previewing pipelines.

## October 27, 2022

Feature

Cloud Data Fusion version 6.7.2 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.7.2 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1822162962/CDAP+Release+6.7.2).

Change

In Cloud Data Fusion version 6.7.2, the [default machine type](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc#Master-Machine-Type) changed from N2 to E2.

Fixed

Fixed in 6.7.2:

  * In the BigQuery Sink plugin (version 0.20.3), fixed an issue that caused a `NullPointerException` error when table metrics were updated or when the output schema was not defined.
  * In the [Send Email batch pipeline alert](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/688029749), fixed an issue where emails failed to send when the **Protocol** was set to TLS.
  * (Release note added January 5, 2023) In the Cloud Storage Sink and File Sink plugins, fixed an issue that caused `Decimal` values to be formatted incorrectly.



## August 15, 2022

Feature

Cloud Data Fusion version 6.7.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This release is in parallel with the [CDAP 6.7.1](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1808007171/CDAP+Release+6.7.1) release.

Change

Changes in 6.7.1:

  * Enhanced the Dataproc provisioner to prevent unneeded Compute Engine calls, depending on the configuration settings.

  * For new Dataproc compute profiles, changed the default value of [Master Machine Type](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc#Master-Machine-Type) from `n1` to `n2`.




Fixed

Fixed in 6.7.1:

  * Fixed an issue that created duplicate entries in the file cache map, which resulted in multiple attempts to delete the same cache file.

  * Fixed an issue where the Log service left empty folders, which made the mounting of Persistent Disk slow. This caused the Log service not to start in a timely manner. 

  * Fixed an issue that caused pipelines to take a long time to launch or get stuck. This was linked to I/O throttling that occurred on the underlying Persistent Disk.

  * Fixed an issue that caused pipelines to fail when two or more pipelines were scheduled to start simultaneously on a static Dataproc cluster. This was due to a file upload race condition. 

  * Fixed an issue in [flow control](https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control) that caused Appfabric to return a `5xx` error code in rare scenarios, instead of `429 (Too Many Requests Error)`, if the number of concurrently launching or running pipelines was above certain thresholds. 

  * Fixed an issue that resulted in an error when a compute profile was exported from the default namespace after switching from a custom namespace. 

  * Delete, edit, and export no longer appear as operations for pre-configured connections in Cloud Data Fusion. You can view connection details for those connections.

  * Fixed an issue when you started a pipeline multiple times, and then stopped the pipeline before it completed, which resulted in the following UI error: `Program <program name> is not running`. 

  * Removed verbose logs from the BigQuery client libraries in pipeline logs.

  * Fixed an issue that caused the [BigQuery Execute action plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/461865263/Google+Cloud+BigQuery+Execute+Action) configured with an **Encryption Key Name** ([CMEK](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys)) to fail when the SQL query contained DDL Statements.

  * In the [BigQuery Execute action plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/461865263/Google+Cloud+BigQuery+Execute+Action), added the property **Store Results in a BigQuery Table** to the UI, which hides the destination table related properties by default.




Feature

The [SAP Ariba Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source) is available in [Preview](https://cloud.google.com/products#product-launch-stages). You can connect your data pipeline to an SAP Ariba Source and a BigQuery Sink with this plugin in Cloud Data Fusion versions 6.5.1 and later.

## August 01, 2022

Deprecated

Cloud Data Fusion versions 6.1, 6.2, and 6.3 are no longer [supported](https://docs.cloud.google.com/data-fusion/docs/support/version-support-policy). You should upgrade your instances to run in a supported version. For instructions, see [Upgrading your Cloud Data Fusion environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## June 09, 2022

Feature

Cloud Data Fusion version 6.7.0 is in [Preview](https://cloud.google.com/products#product-launch-stages). This release is in parallel with the [CDAP 6.7.0](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1782087786/CDAP+Release+6.7.0) release.

Feature

Features in 6.7.0:

  * [Connection Management](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).
  * [DNS Resolution](https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Cloud Data Fusion supports using domain or hostnames for sources instead of IP addresses for pipeline design-time activities, such as getting schema, wrangling, and previewing pipelines.
  * Transformation Pushdown is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) for `JOIN` operations. Several new transformations are available in [Preview](https://cloud.google.com/products#product-launch-stages), including `Group By` and deduplicate aggregations. Added support for the BigQuery Storage Read API to improve performance when extracting data from BigQuery. For more information, see the [Transformation Pushdown overview](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown).
  * Dataplex [Source](https://docs.cloud.google.com/dataplex/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/dataplex/docs/ingest-with-data-fusion) plugins are available in [Preview](https://cloud.google.com/products#product-launch-stages) as system plugins in Cloud Data Fusion. You no longer need to install the plugins.



Fixed

Fixed in 6.7.0:

  * Fixed an issue in the `Group By` transformation where `Longest String` and `Shortest String` aggregators returned an empty string, even when all records contained null values in the specified field. The `Group By` transformation returns null for empty input.
  * Fixed an issue in the `Group By` transformation that caused the `Concat` and `Concat Distinct` aggregate functions to produce incorrect results in some cases.
  * Fixed an issue in the `Group By` transformation that caused the `Variance`, `Variance If`, and `Standard Deviation` aggregate functions to produce incorrect results in some cases.
  * In the Oracle and MySQL Batch Source plugins, fixed an issue to treat all timestamps, specifically the ones older than the Gregorian cutover date (October 15, 1582), from the database in Gregorian calendar format.
  * Improved the generic Database source plugin to correctly read data when the data type is `NUMBER`, scale is set, and the data contains integer values.
  * Fixed an issue in sources (such as File and Cloud Storage) that resulted in an error if you clicked **Get Schema** when the source file contained delimiters used in regular expressions, such as "`|`" or "`.`". You no longer need to escape delimiters for sources.
  * Fixed an issue where Datastore sources read a maximum of 300 records. Datastore sources read all records.
  * Fixed an issue in BigQuery sinks where the output table was not partitioned correctly in the following cases: 
    * The output table didn't exist.
    * Partitioning type was set to `Time`.
    * Operation was set to `Upsert`.
  * Fixed an issue that caused pipelines with BigQuery sinks that have input schemas with nested array fields to fail.
  * Fixed issues that caused failures when reading maps and named enums from Avro files.



Change

Changes in 6.7.0:

  * Increased pipeline launch and run scalability in Enterprise instances.
  * In Transformation Pushdown, added the ability to [use existing connections](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-transformation-pushdown#enable_on_your_pipeline).
  * Added the ability to [parse files](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1782087786/CDAP+Release+6.7.0#Wrangler) before loading data into a Wrangler workspace.
  * Added the ability to import the schema in JSON and some Avro formats, where schema inference isn't possible before loading data into the Wrangler workspace.
  * In [Connection Management](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections): 
    * Added the ability to edit connections.
    * Added support for connections for [several plugins and sinks](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1782087786/CDAP+Release+6.7.0#Enhancements). 
    * Added the ability to browse partial hierarchies, such as BigQuery datasets and Dataplex zones.
  * In the [Cloud Storage Done File Marker Post-Action plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1114603548/Google+Cloud+Storage+Done+File+Marker+Post-run+Action), added support for the **Location** property, which lets you have buckets and customer-managed encryption keys in locations that are not `US` locations.
  * In the [BigQuery Execution Action plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/461865263/Google+Cloud+BigQuery+Execute+Action) and the [BigQuery Argument Setter action plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/721715749/Google+Cloud+BigQuery+Argument+Setter+Action), added support for the **Dataset Project ID** property, the Project ID of the dataset that stores the query results. It's required if the dataset is in a different project than the BigQuery job.
  * In BigQuery sinks, added support for the `BigNumeric` data type.
  * In the [BigQuery Table Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/461930619/Google+BigQuery+Table+Batch+Source), added the ability to query any temporary table in any project when you set the **Enable querying views** property to `Yes`. Previously, you could only query views.
  * In Cloud Data Loss Prevention plugins, added support for templates from other projects.
  * Added a new pipeline state for when you manually stop a pipeline run: `Stopping`.
  * In the [BigQuery Execute plugin](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/461865263/Google+Cloud+BigQuery+Execute+Action), added the ability to look up the [drive scope](https://docs.cloud.google.com/bigquery/external-data-drive#java) for the service account to read from external tables created from the drive.
  * Improved the generic Database source plugin to correctly read decimal data.
  * Improved the Google Cloud Platform plugins to validate the **Encryption Key Name** property.
  * In the replication configurations, added the ability to [enable soft deletes](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/963543163/Google+BigQuery+Replication+Target) from a BigQuery target.
  * In Wrangler, added support for nested arrays, such as the BigQuery [`STRUCT` data type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type).
  * In the [Cloud Storage File Reader Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/606240774/Google+Cloud+Storage+File+Reader+Batch+Source) plugin, added the **Allow Empty Input** property.
  * In the [Cloud Storage File Reader Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/606240774/Google+Cloud+Storage+File+Reader+Batch+Source) and [Amazon S3 Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/485556388/Amazon+S3+Batch+Source#Configuration) plugins, added the **Enable Quoted Values** property, which lets you treat content between quotes as a value.
  * In the [Joiner](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382141163/Configuring+the+Joiner) transformation, added the **Input with Larger Data Skew** property.
  * **Behavior change** : In the Pipeline Studio, if you click **Stop** on a running pipeline and the pipeline doesn't stop after 6 hours, the pipeline is forcefully terminated.
  * **Behavior change** : In the [Deduplicate Analytics](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/515178583/Deduplicate+Analytics) plugin, limited the **Filter Operation** property to one record. If this property isn't set, a random record is chosen from the group of duplicate records.
  * **Behavior change** : The BigQuery sink supports Nullable Arrays. A `NULL` array is converted to an empty array at insertion time.



Breaking

Cloud Data Fusion version 6.7.0 does not support Dataproc version 1.3. For more information, see the [compatible versions of Dataproc](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#version-compatibility).

## May 23, 2022

Change

Google Cloud Platform Plugins version 0.19.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This version includes Dataplex [Source](https://docs.cloud.google.com/dataplex/docs/process-with-data-fusion) and [Sink](https://docs.cloud.google.com/dataplex/docs/ingest-with-data-fusion) plugins in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [CDAP Hub release log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#May-23%2C-2022).

## April 18, 2022

Feature

Google Drive Plugins version 1.4.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see the [CDAP Hub release log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#April-18%2C-2022).

## April 01, 2022

Feature

(Release note added March 14, 2023) [Role-based access control](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac) (RBAC) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion 6.6.0 and later. This gives administrators fine-grained access control over what users can do at the namespace level.

Feature

Cloud Data Fusion version 6.6.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 31, 2022

Feature

The [SAP SLT Replication plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-slt-plugin) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can replicate your data continuously and in real time from SAP sources into BigQuery with this plugin in Cloud Data Fusion versions 6.4.0 and later.

## February 25, 2022

Feature

Cloud Data Fusion version 6.6.0 is in [Preview](https://cloud.google.com/products#product-launch-stages). This release is in parallel with the [CDAP 6.6.0 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1756069933) .

Feature

Features in 6.6.0:

  * [Cluster reuse](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).
  * [Predefined autoscaling](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#autoscaling) is available in [Preview](https://cloud.google.com/products#product-launch-stages).
  * Cloud Data Fusion [flow control](https://docs.cloud.google.com/data-fusion/docs/concepts/flow-control) prevents you from submitting too many requests, which can cause stuck or failed pipeline runs. It applies to API and scheduled pipeline launch requests for batch and real-time pipelines and replication jobs. It is available in [Preview](https://cloud.google.com/products#product-launch-stages).



Fixed

Fixed in 6.6.0:

  * [Improved instance stability](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1756069933/CDAP+Release+6.6.0#Instance-Stability-and-Memory-Usage). Fixed a number of system service unavailability cases resulting in the message "Necessary services are experiencing intermittent problems" and API call failures.
  * Fixed an issue that caused pipelines to fail when a Database Batch Source included a decimal column with precision greater than 19.
  * Fixed an issue that caused pipelines with a Conditional plugin that were running on MapReduce to fail.
  * Fixed an issue that caused pipelines with a Conditional plugin and running on Spark to fail.
  * Fixed an issue that caused validation to fail for Cloud Storage Multi File Sinks.



Change

Changes in 6.6.0:

  * To enable [cluster reuse](https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters#reuse-clusters), the runtime property `system.profile.properties.clusterReuseEnabled` is no longer required.
  * The new default value of the [Dataproc profile Max Idle Time property](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc#Max-Idle-Time) is 30 minutes. Previously, it had no default value.
  * The new limit for previewing data in the Pipeline Studio is 5000 records.
  * Pagination is supported for [Lifecycle Microservices List applications](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#List-Applications).
  * To prevent out of memory errors due to large lineages, a limit has been set for published lineage messages. For more information, see the [CDAP `metadata.messaging.publish.size.limit` documentation](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/595001520).

  * Fetch Size is supported in the following plugins with the new default of 1000 rows:

    * [Cloud SQL MySQL Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690388993)
    * [Cloud SQL PostgreSQL Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/687997219)
    * [IBM DB2 Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/690880538)
    * [MariaDB Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/962134103)
    * [MySQL Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/745963651)
    * [Netezza Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705232947)
    * [Oracle Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705167716)
    * [PostgreSQL Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/705200589)
    * [SQL Server Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/706642109)
    * [Teradata Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975831138)



## January 31, 2022

Feature

The [SAP OData plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use SAP as a source for batch-based data extraction in Cloud Data Fusion using the Open Data Protocol ([OData](https://www.odata.org)). This plugin is available in any Cloud Data Fusion edition, version 6.4.0 and later.

## December 21, 2021

Feature

The [SAP ODP plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use SAP as a source for batch-based and delta-based data extraction in Cloud Data Fusion through Operational Data Provisioning (ODP). This plugin is available in any Cloud Data Fusion edition, version 6.4.0 and later.

## November 17, 2021

Change

January 7, 2022 correction: Cloud Data Fusion is not yet available in the Santiago (southamerica-west1) region. For available locations, see [Locations](https://cloud.google.com/about/locations).

~~Cloud Data Fusion is now available in the[Santiago (southamerica-west1) region](https://cloud.google.com/data-fusion/pricing#supported_regions).~~

## November 05, 2021

Feature

Cloud Data Fusion version 6.5.1 is now available. This release is in parallel with the [CDAP 6.5.1 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1729331217/CDAP+Release+6.5.1) .

Feature

**GA** : Cloud Data Fusion now supports [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys), which provides user encryption control over the data written to Google internal resources in tenant projects, and data written by Cloud Data Fusion pipelines. The list of [supported plugins](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys#key-behavior) has also expanded.

Fixed

Fixed in 6.5.1 (for more information, see the [CDAP release note](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1729331217/CDAP+Release+6.5.1#Bug-Fixes) ):

  * Fixed an issue where messages could not be retrieved for Kafka topics. 
  * Fixed an issue where you could not create a profile for an existing Dataproc cluster.
  * Fixed an issue that caused pipelines to fail when Transformation Pushdown was enabled and used macros as properties.
  * Fixed an issue that caused long running programs, like Replication, to fail within the default Hadoop delegation token timeout. Now, these tokens get renewed so that the job keeps running.
  * Fixed an issue in Replication that caused an error when you clicked **Configure**. 
  * Fixed an issue that caused a pipeline to fail with an ACCESS DENIED error when running BigQuery jobs. For more information, see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#access-denied-issue) .
  * Fixed an issue in the Cloud Storage connection that prevented browsing and parsing files stored in folders under buckets.
  * Fixed an issue that caused custom formats to be unusable in the Cloud Storage source and sink.



## September 29, 2021

Feature

**Preview** : You can now use SAP as a source for batch-based and delta-based data extraction in Cloud Data Fusion through Operational Data Provisioning (ODP). For more information, see the [SAP ODP plugin overview](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin). This plugin is available in Cloud Data Fusion version 6.4.0 and later.

## September 02, 2021

Feature

**Preview** : Cloud Data Fusion version 6.5.0 is now available. This version is a [Preview](https://cloud.google.com/products/#product-launch-stages). This release is in parallel with the [CDAP 6.5.0 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1661108225/CDAP+Release+6.5.0).

Feature

Features in 6.5.0:

  * **Preview** : Cloud Data Fusion now supports [role-based access control (RBAC)](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac). This gives administrators fine-grained access control over what users can do at the namespace level. 

  * **Preview** : Cloud Data Fusion now supports [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys), which provide user encryption control over the data written to Google internal resources in tenant projects, and data written by Cloud Data Fusion pipelines.

  * **Preview** : Cloud Data Fusion Instance Admins can now create, view, duplicate, delete, import, and export connections from the Pipeline Studio, Wrangler, or the Namespace Admin page. A connection stores sensitive data, such as user credentials and host information, needed to connect to data sources. For more information, see [Managing connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections). 

  * **Preview** : [Transformation pushdown](https://docs.cloud.google.com/data-fusion/docs/concepts/transformation-pushdown) is now available. It helps you efficiently design and execute ELT workloads by pushing join transformations down to BigQuery. It gives users that prefer ELT in BigQuery access to the same visual experience that ETL users get in Cloud Data Fusion, without needing to maintain complex SQL scripts. When you enable Transformation pushdown, Cloud Data Fusion executes Join operations in BigQuery (instead of Apache Spark). All other stages in a pipeline are executed using Spark. For pipelines that perform multiple complex joins, BigQuery can execute these joins operations faster than Spark.

  * **Preview** : [Dataproc cluster reuse](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1683390465) is now available. It can be used to speed up pipeline run startup by reusing clusters from previous runs.




Change

Changes in 6.5.0:

  * In version 6.5.0, Spark 3 is the new default engine used when using Cloud Data Fusion Preview and when running pipelines on Dataproc clusters. After an instance is upgraded to version 6.5.0, any new or upgraded pipeline that uses a Dataproc profile without an explicit image version will use the latest Dataproc image 2.0 that has Spark 3.1 bundled. For more information, see [Upgrade notes for Spark 3](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1661108225/CDAP+Release+6.5.0#Upgrade-Notes-for-Spark-3).

  * Added support for [labels](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc#Labels) in the Dataproc provisioner.

  * Added [Shielded VMs](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) to the configuration settings for the Dataproc provisioner. For more information, see the [CDAP documentation](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc).

  * Added authorization checks for preferences, logging, compute profiles, and metadata endpoints.

  * Added support to search for tables based on schema name when you select tables for a Replication job.

  * Added additional trace logging in the authorization flow for debugging.

  * Added support for `BIGNUMERIC` data type for BigQuery target in replication.

  * **Behavior change** : MySQL, Oracle, Postgres, and SQL Server batch sources, sinks, actions, and pipeline alerts are now installed by default as system plugins. Previously, these plugins were available in the Hub as user plugins.




Issue

You can create connections for Database, MySQL, Oracle, PostgreSQL, and SQL Server sources, but the plugin properties do not include **Use Connection**. This means that you cannot reference a connection in a database source plugin. For more information, see [Known issues: Database connections](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1661108225/CDAP+Release+6.5.0#Database-connections).

Fixed

Fixed in 6.5.0 preview version (for more information, see the [CDAP release note](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1661108225/CDAP+Release+6.5.0)):

  * Fixed an issue in Replication that caused jobs to fail if more than 1000 tables were selected for replication.

  * Fixed an issue that caused replication jobs to hang when there were too many Delete or DDL events.

  * Fixed an issue that caused Wrangler to ignore all the other columns other than the given column when parsing Excel files.

  * Fixed Wrangler to fail pipelines upon error. In Wrangler 6.2 and above, there was a backwards-incompatible change where pipelines did not fail if there was an error and instead were marked as completed. 

  * Improved resilience of [TMS](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480379205/Transactional+Messaging+System). 

  * Fixed an issue that caused File Source Plugin validation to fail when there was a macro in the Format field.




## August 16, 2021

Change

SQL Server source plugin version 1.5.5 is now available. This version fixes a `NullPointerException` bug that occurs in version 1.5.4. Versions 1.5.4 and above support the [Datetime](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type) data type. In versions 1.5.3 and earlier, if you had a Datetime column in your SQL Server source, it mapped to the [Timestamp](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type) data type. Upgrades to version 1.5.4 are backwards incompatible, but upgrades to version 1.5.5 are compatible. For more information, see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#sql-server-datetime) and the [CDAP SQL Server Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/706642109).

## June 23, 2021

Feature

**Preview:** You can now replicate data continuously and in real time from operational data stores in [Oracle into BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery) using the Oracle (by Datastream) plugin. The plugin is available in Cloud Data Fusion version 6.4.0 or later.

## June 16, 2021

Feature

The [SAP accelerator for the order to cash process](https://docs.cloud.google.com/data-fusion/docs/how-to/sap-order-to-cash-accelerator) is now available. It provides sample pipelines that you can use to build your end-to-end order to cash process and analytics with [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion), [BigQuery](https://docs.cloud.google.com/bigquery), and [Looker](https://docs.cloud.google.com/looker). The accelerator is a sample implementation of the [SAP Table Batch Source](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin) plugin, which enables bulk data integration from SAP applications with Cloud Data Fusion. The accelerator is available in Cloud Data Fusion environments running in version 6.3.0 and above.

## May 27, 2021

Feature

Cloud Data Fusion version 6.4.1 is now available. To upgrade, see [Upgrading instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading). This release is in parallel with the [CDAP 6.4.1 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1379074062/CDAP+Release+6.4.1).

Feature

In Cloud Data Fusion version 6.4.1, Replication supports the [Datetime data type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type) in BigQuery targets. You can now read and write to tables that contain Datetime fields.

Fixed

Fixed in 6.4.1 (for more information, see the [CDAP release note](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1379074062/CDAP+Release+6.4.1)):

  * Fixed an issue that caused pipelines with aggregations and Decimal fields to fail with an exception.

  * Fixed the Join Condition Type so that it is displayed in the Joiner plugin for pipelines that were upgraded from versions before 6.4.0. 

  * Fixed Wrangler so that pipelines fail when there is an error. In Wrangler 6.2 and above, there was a backwards-incompatible change where pipelines did not fail if there was an error and were instead marked as complete.

  * Fixed an issue that prevented new previews from being scheduled after the preview manager had been stopped ten times. 

  * Fixed an issue while writing non-null values to a nullable field in BigQuery. 

  * Fixed an issue in the BigQuery plugins to correctly delete temporary storage buckets.

  * Fixed an issue in the BigQuery sink that caused pipelines to fail when the input schema was not provided.

  * Fixed an issue in the BigQuery sink that caused pipelines to fail or give incorrect results. 

  * Fixed an issue that caused pipelines to fail when a Pub/Sub source Subscription field was a macro.




## May 05, 2021

Issue

There is an issue in the BigQuery sink plugin version 0.17.0, which causes data pipelines to fail or give incorrect results. This issue is resolved in BigQuery sink plugin version 0.17.1. For more information, see the Cloud Data Fusion [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#bigquery-sink-issue) page.

## March 31, 2021

Feature

Cloud Data Fusion version 6.4.0 is now available. To upgrade, see [Upgrading instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading). This release is in parallel with the [CDAP 6.4.0](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1162707265/CDAP+Release+6.4.0) release.

Feature

Features in 6.4.0:

  * **GA** : You can now ingest data from SAP tables with the [SAP Table Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin).

  * Cloud Data Fusion now supports the [Datetime data type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type) in the following [plugins](https://docs.cloud.google.com/data-fusion/plugins). You can now read and write to tables that contain Datetime fields:

    * BigQuery batch source
    * BigQuery sink
    * BigQuery multi table sink
    * Bigtable batch source
    * Bigtable sink
    * Datastore batch source
    * Datastore sink
    * Cloud Storage file batch source
    * Cloud Storage file sink
    * Cloud Storage multi file sink
    * Spanner batch source
    * Spanner sink
    * File source
    * File sink
    * Wrangler
    * Amazon S3 batch source
    * Amazon S3 sink
    * Database source 
  * You can configure machine type, cluster properties, and idle TTL for the Dataproc provisioner. For the available settings, see the [CDAP documentation](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480412227/Google+Dataproc).

  * Adding, editing, and deleting comments on draft data pipelines is now supported. For more information, see [Adding comments to a data pipeline](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1124204572/Adding+comments+to+a+data+pipeline).

  * Advanced join conditions are now available in the Joiner plugin. You can specify an arbitrary SQL condition to join on. For more information, see [Join Condition Type](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382141163/Configuring+the+Joiner).

  * A new post-action plugin is now available: [Cloud Storage Done File Marker](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1114603548/Google+Cloud+Storage+Done+File+Marker+Post-run+Action). To help you orchestrate downstream/dependent processes, this post-action plugin marks the end of a pipeline run by creating and storing an empty `SUCCESS` file in the given Cloud Storage bucket upon a pipeline completion, success, or failure.




Change

Changed in version 6.4.0:

  * **Behavior change:** When you validate a plugin, [macros](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382043060/Using+macros+to+create+a+reusable+data+pipeline) get resolved with preferences. In previous releases, to validate a plugin's configuration, you had to change the pipeline to remove the macros. 
  * **Behavior change:** Cloud Data Fusion now determines the schema dynamically at runtime instead of requiring arguments to be set. Multi sink runtime argument requirements have been removed, which lets you add simple transformations in multi-source/multi-sink pipelines. In previous releases, multi-sink plugins require the pipeline to set a runtime argument for each table, with the schema for each table. 

  * You can now filter tables in the [Multiple Database Tables Batch Source](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/718831924/Multiple+Database+Tables+Batch+Source).

  * Multiple Database Batch Source and BigQuery multi-table sink have better error handling and let pipelines continue if one or more tables fail.

  * Cloud Data Fusion Replication changes:

    * March 17, 2023 release note addition: Replication from SQL Server and MySQL is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in Cloud Data Fusion version 6.4.0.
    * Renamed Replication pipelines to Replication jobs.
    * The Customer-managed encryption key (CMEK) configuration property is now available for [BigQuery targets in your Replication jobs](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/963543163/Google+BigQuery+Replication+Target). 
    * On the BigQuery Target properties page, renamed the Staging Bucket Location property to Location. 
    * Improved reliability by restarting Replication from the last known checkpoint.
  * You can now use files with ISO-8859, Windows and EBCDIC encoding types with Amazon S3, File and Cloud Storage File Reader batch source plugins.

  * Cloud Data Fusion now supports running pipelines on a Hadoop cluster with Kerberos enabled.




Fixed

Fixed in 6.4.0 (for more information, see the [CDAP release note](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1162707265/CDAP+Release+6.4.0)): 

  * Fixed Bigtable batch source plugin. In previous versions, pipelines that included the Bigtable source would fail. 
  * FTP batch source now works with empty File System Properties. 
  * Strings are now supported in Min/Max aggregate functions (used in both Group By and Pivot plugins).
  * Fixed Salesforce plugin to correctly parse the schema as Avro schema to be sure all the field names are accepted by Avro.
  * Fixed data pipeline with BigQuery sink that failed with INVALID_ARGUMENT exception if the range specified was a macro. 
  * Fixed a class conflict in the Kinesis Spark Streaming source plugin. You can now run pipelines with this source.
  * Fixed an issue in field validation logic in pipelines with BigQuery sink that caused a NullPointerException.
  * Fixed the Wrangler Generate UUID directive to correctly generate a universally unique identifier (UUID) of the record.
  * Fixed advanced joins to recognize auto broadcast setting.
  * Fixed Pipeline Studio to use current namespace when it fetches data pipeline drafts.
  * Fixed Replication statistics to display on the dashboard for SQL Server.
  * Fixed an issue where clicking the Delete button on Replication Assessment page resulted in an error for the replication job.
  * Schema name is now shown when selecting tables to replicate.
  * Fixed Replication to correctly insert rows that were previous deleted by a replication job.
  * Data pipelines running in Spark 3 enabled Dataproc cluster no longer fail with class not found exception. 
  * Fixed Replication with a SQL Server source to generate rows correctly in BigQuery target table if snapshot failed and restarted.
  * Fixed an issue where SQL Server replication job stopped processing data when the connection was reset by the SQL Server.
  * Fixed an error in Replication wizard step to select tables, columns and events to replicate, where selecting no columns for a table caused the wizard to fetch all columns in a table.
  * Using a macro for a password in a replication job no longer results in an error.
  * Fixed logical type display for data pipeline preview runs.
  * Fixed Dashboard API to return programs running but started before the startTime.
  * Fixed deployed Replication jobs to show advanced configurations in Ui.
  * Fixed data pipeline with Python Evaluator transformation to run without stack trace errors.
  * Added loading indicator while fetching logs in Log Viewer.
  * Fixed Pipeline preview so logical start time function doesn't display as a macro.
  * Fixed fields with a list drop down menu in the Replication wizard to default to Select one.
  * Added message in Replication Assessment when there are tables that CDF cannot access.
  * Used error message when an invalid expression is added in Wrangler.
  * Fixed RENAME directive in Wrangler so it is case sensitive.
  * Fixed Pipeline Operations UI to stop showing the loading icon forever when it gets error from backend.
  * Fixed Wrangler to no longer generate invalid reference names.
  * Fixed Wrangler to display logical types instead of java types.
  * Fixed pipelines from Wrangler to no longer generate incorrect for xml files.
  * Added connection in Wrangler hard codes the name of the JDBC driver.
  * Batch data pipelines with Spark 2.2 engine and HDFS sinks no longer fail with delegation token issue error.



Deprecated

**FTP Batch Source (system plugin for data pipelines)**

FTP Batch Source version 3.0.0 is backward compatible, except that it uses a different artifact. This was done to ensure that updates to the plugin can be delivered out-of-band from Cloud Data Fusion releases, through the Hub.

It is recommended that you use version 3.0.0 or later in your data pipelines.

## March 24, 2021

Feature

Cloud Data Fusion version 6.3.1 is now available. This version fixes a race condition that results in intermittentant failures in concurrent pipeline executions. This release is in parallel with the [CDAP 6.3.1 release](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1180499986/CDAP+Release+6.3.1).

## March 17, 2021

Change

**Preview:** Cloud Data Fusion now supports Access Transparency. Access Transparency is a part of Google's long-term commitment to transparency and user trust. Access Transparency logs record the actions that Google personnel take when accessing customer content. For more information, see the [Access Transparency overview](https://docs.cloud.google.com/logging/docs/audit/access-transparency-overview).

## February 22, 2021

Deprecated

Cloud Data Fusion Beta instances (versions 6.1.0.2 and lower that were created before November 21, 2019) will be turned down on March 1, 2021. Instead, [export](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines) your pipeline, [delete](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance) the old instance to avoid billing impact, [create](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance) a new instance, and [import](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines#import) your pipeline into the new instance.

## February 03, 2021

Feature

**Preview:** You can now [replicate data](https://docs.cloud.google.com/data-fusion/docs/concepts/replication) continuously and in real time from operational data stores, such as SQL Server and MySQL, into BigQuery.

## January 27, 2021

Announcement

Cloud Data Fusion Beta instances (versions 6.1.0.2 and lower that were created before November 21, 2019) will be turned down on March 1, 2021. Instead, [export your pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines), [create a new instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance), and import your pipeline into the new instance. This note is incorrect; see entry for February 18, 2021.

## January 21, 2021

Announcement

Cloud Data Fusion 6.3.0 is now available.

Change

In-place [upgrades](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading) are now supported for minor and patch versions.

Change

You can configure the default system compute profile in the [Developer edition](https://cloud.google.com/data-fusion/pricing) starting in Cloud Data Fusion version 6.3.0.

## October 27, 2020

Change

You can now specify which Cloud Data Fusion version to use when you [create an instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).

Change

You can now specify the service account to use for running your Cloud Data Fusion pipeline on Dataproc:

  * You specify the service account when you [create an instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance). 
  * When you specify the service account, you can also explicitly authorize Cloud Data Fusion to grant the [Service Account User and Data Fusion Runner roles](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion) to the Cloud Data Fusion service account.



## October 21, 2020

Issue

In Cloud Data Fusion versions before 6.2, there is a known issue where pipelines get stuck during execution. Stopping the pipeline results in the following error: `Malformed reply from SOCKS server`. To fix this, [delete the Dataproc cluster, and then update the memory settings in the compute profile](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting).

## September 30, 2020

Change

This release is in parallel with the [CDAP 6.2.2 release](https://github.com/cdapio/cdap/releases).

Change

Cloud Data Fusion now displays the number of pending preview runs, if any, before the current run. In the Studio, the number of pending runs is displayed under the timer.

Change

Improved performance for skewed joins by including Distribution in the [Joiner plugin settings](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382141163/Configuring+the+Joiner+transformation).

Change

Cloud Data Fusion now supports [autoscaling Dataproc clusters](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#autoscaling).

Change

Wrangler now supports [BigQuery views](https://docs.cloud.google.com/bigquery/docs/views-intro) and [materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro).

## August 24, 2020

Change

#### Highlights

Cloud Data Fusion 6.1.4 provides performance and scalability improvements that increase developer productivity and optimize pipeline runtime performance. The release includes scaled-up previews that support up to 50 concurrent runs, capabilities to handle large and complex schemas in Pipeline Studio, an enhanced log viewer, and other critical improvements and fixes.

This release is in parallel with the [CDAP 6.1.4 release](https://github.com/cdapio/cdap/releases).

Feature

You can now create [autoscaling Dataproc clusters](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling).

Feature

You can now use the schema support feature in the UI to edit the precision and scale fields.

Feature

Cloud Data Fusion now has improved memory performance in pipelines by utilizing a disk-only auto-caching strategy.

Fixed

Fixed a bug where the setting for the number of executors in streaming pipelines was ignored.

Change

Cloud Data Fusion now supports large and deeply nested schemas (>5K fields with 20+ levels of nesting).

Fixed

Fixed the stability of state transitions for starting pipelines in AppFabric when AppFabric restarts.

Fixed

Fixed the preview page in table mode so that it shows multiple inputs and outputs with tabs.

Fixed

Fixed a race condition where runtime monitoring failed when programs launched concurrently.

Fixed

Fixed a bug where a metric incorrectly counted the number of the records written in the Google Cloud Storage sink.

Change

Cloud Data Fusion previews now support up to 50 concurrent runs.

## July 16, 2020

Feature

Cloud Data Fusion version 6.1.3 is now available. This version includes performance improvements and minor bug fixes.

  * Improved performance of Joiner plugins, aggregators, program startup, and previews.
  * Added support for custom images. You can select a custom Dataproc image by specifying the image URI.
  * Added support for rendering large schemas (>1000 fields) in the pipelines UI.
  * Added payload compression support to the messaging service.



## April 22, 2020

Feature

Cloud Data Fusion version 6.1.2 is now available. This version includes several stability and performance improvements and new features.

  * Added support for [Field Level Lineage](https://docs.cloud.google.com/data-fusion/docs/tutorials/lineage) for Spark plugins and Streaming pipelines
  * Added support for Spark 2.4
  * Added an option to skip header in the files in delimited, CSV, TSV, and text formats
  * Added an option for database source to replace the characters in the field names



Fixed

Fixed a bug that caused errors when Wrangler's parse-as-csv with header was used when reading multiple small files.

Fixed

Reduced preview startup by 60%. Also added limit to max concurrent preview runs (10 by default).

Fixed

Fixed a bug that caused DBSource plugin to fail in preview mode.

Fixed

Fixed a bug that caused zombie processes when using the Remote Hadoop Provisioner.

Fixed

Fixed a race condition that caused a failure when running a Spark program.

## January 10, 2020

Feature

Cloud Data Fusion version 6.1.1 is now available. This version includes several stability and performance improvements, as well as these new features:

  * Azure Data Lake storage support in Wrangler
  * Enabled Field Level Lineage (Beta)
  * Data Loss Prevention plugin to identify, tokenize, or encrypt sensitive data at scale (Beta)



## December 10, 2019

Feature

Cloud Data Fusion version 6.1.0.5 is now available. This version includes several stability and performance improvements.

## November 21, 2019

Feature

Cloud Data Fusion is now generally available.

Feature

Added support for creating private Cloud Data Fusion instances and executing data pipelines in a VPC-SC environment.

Feature

Added support for creating Cloud Data Fusion instances that use [private IP](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip) addresses.

Feature

Added support to encrypt resources created in Cloud Storage, BigQuery, and Pub/Sub using Cloud Data Fusion with Customer Managed Encryption Keys.

Feature

Added [reference documentation](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference) for creating and managing pipelines and datasets.

Change

The Cloud Data Fusion UI is now available at a different URL in the format: `<instance-name>-<project-id>-dot-<region identifier>.datafusion.googleusercontent.com`.

## May 31, 2019

Change

Added a version number field to the Cloud Data Fusion **Instance details** page in the Google Cloud console.

Fixed

Added support for specifying a subnet for the Dataproc provisioner.

Fixed

Fixed a bug that caused Cloud Data Fusion to launch Dataproc clusters in an incorrect project.

Fixed

Fixed the Cloud Dataproc provisioner to handle networks that do not use automatic subnet creation.

Change

Renamed "Cloud Dataprep service" to "Wrangler service" in the **System Admin** page of the Cloud Data Fusion UI.

## April 10, 2019

Feature

Cloud Data Fusion is now publicly available in beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
