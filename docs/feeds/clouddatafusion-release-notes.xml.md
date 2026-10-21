---
url: https://docs.cloud.google.com/feeds/clouddatafusion-release-notes.xml
title: Cloud Data Fusion - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:23:28.964759+00:00
---

# Cloud Data Fusion - Release notes

> Source: https://docs.cloud.google.com/feeds/clouddatafusion-release-notes.xml

tag:google.com,2016:clouddatafusion-release-notesCloud Data Fusion - Release notesGoogle Cloud Platform2026-09-16T00:00:00-07:00September 16, 2026tag:google.com,2016:clouddatafusion-release-notes#September_16_20262026-09-16T00:00:00-07:00Change 

The BigQuery Source plugin version 0.24.7 is available in Cloud Data Fusion version 6.11.0 and later. This release includes the following change:

  * Fixed an issue that caused intermittent pipeline failures in the BigQuery Source plugin when errors occurred during the creation of the temporary staging bucket ([PLUGIN-1787](https://cdap.atlassian.net/browse/PLUGIN-1787)).

]]> August 07, 2026tag:google.com,2016:clouddatafusion-release-notes#August_07_20262026-08-07T00:00:00-07:00Change 

The Cloud SQL for MySQL and Cloud SQL for PostgreSQL plugins, version 1.11.14, are available in Cloud Data Fusion version 6.10.x. Version 1.12.5 of these plugins is available in Cloud Data Fusion version 6.11.x.

This release includes the following feature:

  * You can now configure transaction isolation levels in the Cloud SQL for MySQL and Cloud SQL for PostgreSQL plugins. This configuration applies to both batch sources and sinks, providing more precise control over data consistency and database locking ([PLUGIN-1779](https://cdap.atlassian.net/browse/PLUGIN-1779)).



### Change

The Windows Share Copy Action plugin version 2.12.5 is available in Cloud Data Fusion version 6.9.1 and later. Version 2.13.2 of this plugin is available in Cloud Data Fusion version 6.11.0 and later.

This release includes the following change:

  * Added support for the modern SMBv2 and SMBv3 protocols to improve connection performance and reliability, while maintaining backward compatibility with pipelines that use SMBv1 ([PLUGIN-1960](https://cdap.atlassian.net/browse/PLUGIN-1960)).

]]> July 15, 2026tag:google.com,2016:clouddatafusion-release-notes#July_15_20262026-07-15T00:00:00-07:00Feature 

Cloud Data Fusion version 6.11.1.4 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

### Fixed

Fixed in Cloud Data Fusion 6.11.1.4:

  * Fixed a race condition where successfully completed Dataproc jobs were incorrectly marked as `failed` on the Dataproc console due to premature program cancellation ([CDAP-21219](https://cdap.atlassian.net/browse/CDAP-21219)).
  * Fixed an issue where the **Pipeline list** page would hang due to a race condition in an internal service ([CDAP-21241](https://cdap.atlassian.net/browse/CDAP-21241)).
  * Fixed a security vulnerability in log downloads by enforcing strict validation on requested log paths and query parameters to prevent unauthorized access ([CDAP-21260](https://cdap.atlassian.net/browse/CDAP-21260)).



### Change

Changes in Cloud Data Fusion 6.11.1.4:

  * Increased the default Wrangler browsing limit to 2,000 items ([CDAP-21259](https://cdap.atlassian.net/browse/CDAP-21259)).

]]> June 29, 2026tag:google.com,2016:clouddatafusion-release-notes#June_29_20262026-06-29T00:00:00-07:00Change 

The Salesforce plugin version 1.7.4 is available in Cloud Data Fusion version 6.8.0 and later.

This release includes the following change:

  * Added support for the client credentials grant type in the Salesforce plugin. To select the grant type, use the new **OAuth Grant Type** field in the console ([PLUGIN-1953](https://cdap.atlassian.net/browse/PLUGIN-1953)).

]]> June 05, 2026tag:google.com,2016:clouddatafusion-release-notes#June_05_20262026-06-05T00:00:00-07:00Feature 

Cloud Data Fusion version 6.11.1.3 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

### Fixed

Fixed in Cloud Data Fusion 6.11.1.3:

  * Fixed an issue that caused pipeline preview runs to fail with an `InaccessibleObjectException` when using certain plugins, such as Cloud SQL for PostgreSQL ([CDAP-21212](https://cdap.atlassian.net/browse/CDAP-21212)).

  * Fixed an issue causing custom plugins to lose their logging context when running in parallel pipeline branches, ensuring consistent log propagation across both linear and parallel branched pipeline executions ([CDAP-21245](https://cdap.atlassian.net/browse/CDAP-21245)).

  * Fixed critical security vulnerabilities in CDAP ([CDAP-21250](https://cdap.atlassian.net/browse/CDAP-21250)).

  * Improved the latency of the **List pipelines** page ([CDAP-21244](https://cdap.atlassian.net/browse/CDAP-21244)).

  * Fixed an issue causing intermittent service unavailability after instance upgrades ([CDAP-21254](https://cdap.atlassian.net/browse/CDAP-21254)).




### Change

Changes in Cloud Data Fusion 6.11.1.3:

  * Introduced a `deployStrategy` query parameter in the [Deploy Application API](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Create-an-Application) to skip the re-deployment of an existing pipeline if its configuration hasn't changed ([CDAP-21246](https://cdap.atlassian.net/browse/CDAP-21246)).



### Change

The Snowflake plugin version 1.2.1 is available in Cloud Data Fusion version 6.11.1 and later. This release includes the following change:

  * Upgraded the Snowflake JDBC driver version from 3.14.4 to 4.0.2 and adapted to breaking API changes. This update migrates stream upload and download methods to use the new `UploadStreamConfig` and `DownloadStreamConfig` builders, updates OAuth2 authentication logic, and adds passphrase validation for key-pair authentication ([PLUGIN-1954](https://cdap.atlassian.net/browse/PLUGIN-1954)).

]]> May 18, 2026tag:google.com,2016:clouddatafusion-release-notes#May_18_20262026-05-18T00:00:00-07:00Change 

The HTTP plugin version 1.5.2 is available in Cloud Data Fusion version 6.11.1. This release includes the following change:

  * Fixed an issue in the HTTP plugin where OAuth2 token requests bypassed configured proxies, causing connection failures in restricted environments. Authentication requests now correctly route through the configured proxy ([PLUGIN-1956](https://cdap.atlassian.net/browse/PLUGIN-1956)).



### Change

The Multi-table plugin version 1.4.2 is available in Cloud Data Fusion version 6.11.1 and later. This release includes the following changes:

  * Introduced informational logging to flag when source tables or custom SQL queries yield zero records, which improves data pipeline observability. The split-generation logic is also updated to handle empty tables and prevent false-alarm logs during multi-split processing ([PLUGIN-1950](https://cdap.atlassian.net/browse/PLUGIN-1950)).

]]> March 17, 2026tag:google.com,2016:clouddatafusion-release-notes#March_17_20262026-03-17T00:00:00-07:00Fixed 

Cloud Data Fusion version 6.11.1.2 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

This release includes the following changes:

  * Fixed an issue that caused pipelines to get stuck in the provisioning state when processing large run records ([CDAP-21234](https://cdap.atlassian.net/browse/CDAP-21234)).

  * Fixed the triggers panel in the pipeline details page to display the correct triggers count on initial load ([CDAP-21230](https://cdap.atlassian.net/browse/CDAP-21230)).

  * Updated the GraphQL query mechanism to cache the pipelines list and fix the long loading screen in the deployed pipelines list page ([CDAP-21229](https://cdap.atlassian.net/browse/CDAP-21229)).


]]> March 02, 2026tag:google.com,2016:clouddatafusion-release-notes#March_02_20262026-03-02T00:00:00-08:00Change 

The SAP ODP plugin version 0.12.1 is available in Cloud Data Fusion version 6.10 and later. This release includes the following features and changes:

  * Hierarchy data sources are now supported for extraction.

  * ODQ fields are populated with TSN, package number, and record number for full extraction.

  * Structured SAP messages are now displayed according to the message type (for example, type `E` as error and type `I` as information). Earlier, all messages from SAP displayed as errors.

  * You can now use the TVARVC table entries with parameter `/GOOG/ODP_TRANSFER_MODE` (for all data sources) or `/GOOG/M_DatasourceName` (for individual data sources) to determine if data is transferred in CHAR or XML format. Maintain 'C' to transfer data in CHAR format. Maintain an empty value to transfer data in XML format.


]]> February 09, 2026tag:google.com,2016:clouddatafusion-release-notes#February_09_20262026-02-09T00:00:00-08:00Feature 

Cloud Data Fusion version 6.11.1.1 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This release includes the following feature:

  * `InstanceV3` monitored-resource: Introduced `datafusion.googleapis.com/InstanceV3` as the default monitored resource for instance-level metrics and system service logs. This resource excludes the `org_id` and `namespace` labels found in `InstanceV2`. Emission of `InstanceV2` metrics and logs is disabled by default for new and upgraded instances but can be re-enabled using the REST API.

For more information, see [Metrics overview](https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview) and [View pipeline logs](https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs).




### Fixed

Fixed in Cloud Data Fusion 6.11.1.1:

  * Fixed retries in message publishing when the messaging service is temporarily unavailable ([CDAP-21043](https://cdap.atlassian.net/browse/CDAP-21043)).
  * Fixed a security vulnerability where user-provided code in preview runners could access sensitive data from other preview runs ([CDAP-21211](https://cdap.atlassian.net/browse/CDAP-21211)).
  * Fixed an issue where internal task workers running user code could hang indefinitely. The system now forces completed tasks to exit and uses a health check to restart unresponsive workers ([CDAP-21213](https://cdap.atlassian.net/browse/CDAP-21213)).
  * Fixed an issue where the list apps API endpoint failed to return all deployed pipelines when used with pagination ([CDAP-21220](https://cdap.atlassian.net/browse/CDAP-21220)).

]]> January 29, 2026tag:google.com,2016:clouddatafusion-release-notes#January_29_20262026-01-29T00:00:00-08:00Feature 

The SAP Table Reader plugin version 0.11.5 is available in Cloud Data Fusion version 6.10 and later.

This release includes the following change:

  * Fixed an issue in the SAP Table Reader where running in Snapshot mode caused the Clean Up RFM process to generate an unnecessary `Job abort failed` error message in the detail logs.

]]> September 09, 2025tag:google.com,2016:clouddatafusion-release-notes#September_09_20252025-09-09T00:00:00-07:00Change 

The Salesforce plugin version 1.7.0 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following change:

  * Upgrade of Salesforce Bulk API V1 version from 62.0 to 64.0 ([PLUGIN-1926](https://cdap.atlassian.net/browse/PLUGIN-1926)).



Salesforce has deprecated certain fields in the API version 64.0. Upgrading to Salesforce plugin version 1.7.0 might cause pipelines that use these fields, to fail. To ensure your pipelines continue to work, you must manually update your pipeline schema to either load a new schema or remove the deprecated fields. For more information, see [Prerequisites for upgrading to Salesforce plugin version 1.7.0](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#upgrade-prereq).

]]> August 28, 2025tag:google.com,2016:clouddatafusion-release-notes#August_28_20252025-08-28T00:00:00-07:00Change 

The ServiceNow plugin version 1.2.7 is available in Cloud Data Fusion version 6.10.1. This release includes the following change:

  * Fixed an issue related to schema backward compatibility while upgrading from plugin version 1.1.0 ([PLUGIN-1902](https://cdap.atlassian.net/browse/PLUGIN-1902)).

]]> August 27, 2025tag:google.com,2016:clouddatafusion-release-notes#August_27_20252025-08-27T00:00:00-07:00Feature 

Cloud Data Fusion version 6.11.1 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This release includes the following features:

  * Added support for HTTP access tokens (Bearer authentication) in Bitbucket Server for [source control management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) ([CDAP-21049](https://cdap.atlassian.net/browse/CDAP-21049)).
  * A new API is available to retrieve the application count for each namespace ([CDAP-21161](https://cdap.atlassian.net/browse/CDAP-21161)).



### Fixed

Fixed in Cloud Data Fusion 6.11.1:

  * To prevent storage issues on static Dataproc clusters, temporary pipeline data is automatically deleted after a successful run ([CDAP-21076](https://cdap.atlassian.net/browse/CDAP-21076)).
  * Fixed an issue that prevented [Expression Language (EL)](https://github.com/data-integrations/wrangler/blob/develop/wrangler-core/src/main/java/io/cdap/wrangler/expression/EL.java) from being used within user-defined directives ([CDAP-21204](https://cdap.atlassian.net/browse/CDAP-21204)).
  * Fixed an issue where a pipeline would fail when reading an encrypted file from Cloud Storage using Tink ([PLUGIN-1717](https://cdap.atlassian.net/browse/PLUGIN-1717)).



### Deprecated

Dataproc 2.0 is no longer supported in Cloud Data Fusion version 6.11.1 and later.

### Change

Changes in Cloud Data Fusion 6.11.1:

  * The Java runtime environment is upgraded from Java 8 to Java 11 ([CDAP-21184](https://cdap.atlassian.net/browse/CDAP-21184)).
  * To create ephemeral Dataproc clusters, Cloud Data Fusion uses the Dataproc 2.3 image by default ([CDAP-21187](https://cdap.atlassian.net/browse/CDAP-21187)).
  * The pipeline JSON size limit for creating new pipelines and importing pipelines as JSON is increased to 5MB (previously 2MB) ([CDAP-21194](https://docs.cloud.google.com/feeds/CDAP-21194)).
  * On the Pipeline details page, the inbound triggers sidebar features a paginated list of pipelines where you can select the pipelines you want to add to the trigger. Additionally, a refresh button is added to update the existing list of triggers and pipelines ([CDAP-21195](https://cdap.atlassian.net/browse/CDAP-21195)).

]]> July 25, 2025tag:google.com,2016:clouddatafusion-release-notes#July_25_20252025-07-25T00:00:00-07:00Feature 

You can now attach tags to Cloud Data Fusion instances during instance creation. This ensures immediate metadata for better organization, cost tracking, and policy automation. For more information, see [Attach tags during instance creation](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-with-tags#add-tags).

]]> July 23, 2025tag:google.com,2016:clouddatafusion-release-notes#July_23_20252025-07-23T00:00:00-07:00Fixed 

The Cloud Data Fusion version 6.10.1.5 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.5 includes reliability fixes.

]]> July 20, 2025tag:google.com,2016:clouddatafusion-release-notes#July_20_20252025-07-20T00:00:00-07:00Change 

The SAP ODP plugin version 0.12 is available in Cloud Data Fusion version 6.10 and later. This release includes the following changes:

  * Support for old SAP ODP RFCs is removed to align with SAP Note 3255746.
  * Messages have been updated when attempting to extract data from unsupported hierarchy data sources.



We recommend upgrading all your pipelines to the latest SAP ODP plugin version, as earlier versions are no longer compliant with SAP Guidelines.

**Note:** This release is backward compatible. ]]> July 16, 2025tag:google.com,2016:clouddatafusion-release-notes#July_16_20252025-07-16T00:00:00-07:00Change 

The Oracle plugin version 1.12.3 is available in Cloud Data Fusion (via Hub) versions 6.11.0 and later, and 1.11.8 is available in Cloud Data Fusion (via Hub) version 6.10.

This release provides backward compatibility for recent schema changes, including the following:

  * [Precisionless numbers](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_14_2023): In version 1.10.0, precisionless numbers were handled as strings.
  * [Improved timestamp handling](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_14_2023): Version 1.11.0 introduced improvements to timestamp handling.



To address backward compatibility for these changes, two new hidden fields are introduced in Oracle batch source configurations: `treatPrecisionlessNumAsDeci` and `treatAsOldTimestamp`. Both flags default to `false`. To enable these flags, edit the respective values in your exported connection JSON (if using connections) or pipeline JSON (if not using connections) before re-importing or re-deploying ([PLUGIN-1893](https://cdap.atlassian.net/browse/PLUGIN-1893)).

]]> June 12, 2025tag:google.com,2016:clouddatafusion-release-notes#June_12_20252025-06-12T00:00:00-07:00Change 

The Elasticsearch plugin version 1.11.0 is available in Cloud Data Fusion version 6.11.0. This release includes the following change:

  * Upgraded Hadoop version for Elasticsearch plugin compatibility ([PLUGIN-1881](https://cdap.atlassian.net/browse/PLUGIN-1881)).

]]> June 11, 2025tag:google.com,2016:clouddatafusion-release-notes#June_11_20252025-06-11T00:00:00-07:00Change 

The HTTP plugin version 1.4.4 is available in Cloud Data Fusion version 6.10.1. This release includes the following changes:

  * Implemented the Client Credentials Grant flow for HTTP OAuth2, enabling authorized clients to securely access data using the `client_credentials` grant type. Client credentials can be passed through Basic Authentication header, in the request body, or as query parameters ([PLUGIN-1872](https://cdap.atlassian.net/browse/PLUGIN-1872)).

  * Fixed an issue causing the HTTP Source plugin to throw a `NullPointerException` when the `BasePageIterator` received a null response ([PLUGIN-1894](https://cdap.atlassian.net/browse/PLUGIN-1894)).


]]> June 09, 2025tag:google.com,2016:clouddatafusion-release-notes#June_09_20252025-06-09T00:00:00-07:00Change 

Cloud Data Fusion is available in the `northamerica-south1` (Mexico) region. For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

]]> June 02, 2025tag:google.com,2016:clouddatafusion-release-notes#June_02_20252025-06-02T00:00:00-07:00Change 

The [Salesforce plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.10 is available in Cloud Data Fusion versions 6.10.1 and 6.11.0. This release includes the following changes:

  * Upgraded Salesforce API version from 53.0 to 62.0 ([PLUGIN-1891](https://cdap.atlassian.net/browse/PLUGIN-1891)).
  * Added a retry mechanism for all Salesforce API calls from the Salesforce plugin ([PLUGIN-1892](https://cdap.atlassian.net/browse/PLUGIN-1892)).

]]> May 16, 2025tag:google.com,2016:clouddatafusion-release-notes#May_16_20252025-05-16T00:00:00-07:00Change 

The DB plugin versions 1.11.7 and 1.12.2 are available in Cloud Data Fusion versions 6.10.1 and 6.11.0 respectively. This release includes the following change:

  * Added the `TRANSACTION_ISOLATION_LEVEL` property to DB Plugins (PostgreSQL, MySQL, and MSSQL).

]]> May 13, 2025tag:google.com,2016:clouddatafusion-release-notes#May_13_20252025-05-13T00:00:00-07:00Change 

The MariaDB Batch Source plugin versions 1.11.7 and 1.12.2 are available in Cloud Data Fusion versions 6.10.1 and 6.11.0 respectively. This release includes the following changes:

  * Fixed an issue related to the MariaDB `YEAR` data type causing pipeline failures when the date type was manually changed to `DATE`. Validation for this specific scenario is now skipped ([PLUGIN-1888](https://cdap.atlassian.net/browse/PLUGIN-1888)).

  * Fixed an issue that caused pipeline failures with a `java.lang.ClassNotFoundException: Class io.cdap.plugin.db.DBRecord not found` error, which was due to a class loading problem ([PLUGIN-1874](https://cdap.atlassian.net/browse/PLUGIN-1874)).

  * Added a committer to Database plugins to manage committing or rolling back entire tasks, depending on whether the task completes successfully or is aborted ([PLUGIN-1815](https://cdap.atlassian.net/browse/PLUGIN-1815)).


]]> March 31, 2025tag:google.com,2016:clouddatafusion-release-notes#March_31_20252025-03-31T00:00:00-07:00Deprecated 

Cloud Data Fusion version 6.9 is no longer supported. You should upgrade your instances to run in a [supported version](https://docs.cloud.google.com/data-fusion/docs/version-support-policy). For instructions, see [Manage version upgrades for instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

]]> March 28, 2025tag:google.com,2016:clouddatafusion-release-notes#March_28_20252025-03-28T00:00:00-07:00Change 

The Python Transform plugin (version 2.3.2) is available in CDAP version 6.10.1. This includes bug fix for the deprecated `PROTOCOL_TLSv1` on Dataproc 2.0 and later. The issue occurs when earlier TLS versions, such as TLSv1 and TLSv1.1 are disabled by default due to security concerns. Applications relying on `ssl.PROTOCOL_TLSv1` in Python might fail and requires updates to use `ssl.PROTOCOL_TLSv1_2` or later.

]]> March 17, 2025tag:google.com,2016:clouddatafusion-release-notes#March_17_20252025-03-17T00:00:00-07:00Feature 

Cloud Data Fusion version 6.11.0 is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

Cloud Data Fusion 6.11.0 offers high availability with reduced upgrade downtime.

### Feature

When a pipeline run fails, you can retrieve detailed error information on the pipeline details page of the Cloud Data Fusion web interface.

Cloud Data Fusion classifies pipeline errors by category, reason, and message. This classification speeds up resolution and reduces the need to examine complex logs. For more information, see [Retrieve error information for a failed pipeline run](https://docs.cloud.google.com/data-fusion/docs/troubleshoot#pipeline).

### Feature

You can view instance metrics and pipeline metrics in Cloud Monitoring and in the dashboard provided by Cloud Data Fusion. For more information, see [Metrics overview](https://docs.cloud.google.com/data-fusion/docs/concepts/metrics-overview) and [Monitor Cloud Data Fusion system, instance, and pipeline health](https://docs.cloud.google.com/data-fusion/docs/how-to/metrics-views).

### Feature

You can view instance logs and pipeline logs in Cloud Logging, and in the dashboard provided by Cloud Data Fusion. For more information, see [View Cloud Data Fusion logs](https://docs.cloud.google.com/data-fusion/docs/how-to/view-datafusion-logs).

### Deprecated

The following APIs for downloading system service and pipeline run logs are deprecated in 6.11.0:

  * `GET /v3/namespaces/<NAMESPACE_ID>/apps/<APP_ID>/<PROGRAM_TYPE>/<PROGRAM_ID>/logs`
  * `GET /v3/system/services/<SERVICE_ID>/logs`



### Deprecated

The ability to retrieve all applications without pagination using the `GET /v3/namespaces/<NAMESPACE_ID>/apps` endpoint is deprecated in 6.11.0.

### Fixed

Fixed in Cloud Data Fusion 6.11.0:

  * Fixed a null pointer exception in the BigQuery multi-sink plugin when used without a reference name ([PLUGIN-1843](https://cdap.atlassian.net/browse/PLUGIN-1843)).

  * Fixed Joiner plugin failures observed on Dataproc 2.2-debian12 instances ([CDAP-21075](https://cdap.atlassian.net/browse/CDAP-21075)).

  * Fixed an issue that prevented pipelines from accepting empty input in Amazon S3 and Google Cloud Storage source plugins ([PLUGIN-1742](https://cdap.atlassian.net/browse/PLUGIN-1742)).

  * Fixed an issue in RBAC-enabled instances where the pipeline details page displayed an incorrect author name ([CDAP-21069](https://cdap.atlassian.net/browse/CDAP-21069)).




### Change

Changes in Cloud Data Fusion 6.11.0:

  * To create ephemeral clusters, Cloud Data Fusion uses the Dataproc 2.2 image by default. For more information about its limitations in Cloud Data Fusion, see [Change the Dataproc image to version 2.1](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image#change-to-dataproc-21).

  * The maximum concurrent runs limit for triggers is displayed in the console ([CDAP-21072](https://cdap.atlassian.net/browse/CDAP-21072)).

  * Added support for destination table write preference in the BigQuery Execute plugin ([PLUGIN-1438](https://cdap.atlassian.net/browse/PLUGIN-1438)).




### Deprecated

The following APIs for searching and querying metrics are deprecated in 6.11.0:

  * `POST v3/metrics/query`
  * `POST v3/metrics/search`



### Breaking

A soft limit of 2 MB for pipeline JSON size is introduced in 6.11.0. Pipelines exceeding this size might encounter deployment failures.

]]> January 29, 2025tag:google.com,2016:clouddatafusion-release-notes#January_29_20252025-01-29T00:00:00-08:00Fixed 

The [SAP OData plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odata-plugin) version 0.11.6 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following change:

Fixed an issue causing pipeline deployments to fail due to SAP memory dumps when processing large datasets with macro filters: `ERROR Stage 'SAP OData' encountered : CDF_SAP_ODATA_01534 - Service validation failed. Root Cause:Invalid parametertype used at function`.

]]> January 21, 2025tag:google.com,2016:clouddatafusion-release-notes#January_21_20252025-01-21T00:00:00-08:00Feature 

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Data Fusion resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/data-fusion/docs/how-to/create-custom-constraints).

]]> January 13, 2025tag:google.com,2016:clouddatafusion-release-notes#January_13_20252025-01-13T00:00:00-08:00Change 

The [SAP SuccessFactors plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source) version 1.2.4 is available in Cloud Data Fusion version 6.8.0 and later. This release lets you use OAuth 2.0 for ODATA API authentication ([PLUGIN-1741](https://cdap.atlassian.net/browse/PLUGIN-1741)).

]]> December 19, 2024tag:google.com,2016:clouddatafusion-release-notes#December_19_20242024-12-19T00:00:00-08:00Fixed 

The Cloud Data Fusion version 6.10.1.2 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.2 includes the following changes:

  * You can generate audit logs that record data plane activities within your Cloud Data Fusion instance. [Data plane audit logging](https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging#api-interface-reference) is available in Preview for RBAC-enabled instances. 

  * To improve the API response time, by default, all program activity records older than 30 days are cleaned up. Any activity older than 30 days isn't visible in the Cloud Data Fusion studio ([CDAP-14950](https://cdap.atlassian.net/browse/CDAP-14950)).

  * When using role-based access control, performing the List Pipelines operation requires `datafusion.pipelines.list` permission, in addition to `datafusion.namespaces.get` permission. For more information, see [RBAC roles and permissions](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac-roles-and-permissions#permissions_for_common_actions) ([CDAP-20931](https://cdap.atlassian.net/browse/CDAP-20931)).

  * Fixed an issue causing the flow control metric, `flowcontrol.launching.count`, to overcount in cases where servers were restarted when a pipeline run was in progress ([CDAP-21046](https://cdap.atlassian.net/browse/CDAP-21046)).

  * Fixed an issue causing the flow control metric, `flowcontrol.launching.count`, to be stale after a restart when no pipelines were running ([CDAP-21048](https://cdap.atlassian.net/browse/CDAP-21048)).

  * Fixed an issue causing the default max concurrent runs limit for triggers not to appear in the web interface, making it difficult to tell if triggers were working as intended ([CDAP-21072](https://cdap.atlassian.net/browse/CDAP-21072)).

  * Fixed an issue causing the top panel of the **Studio** tab to disappear when you edited a pipeline draft that's based on a pipeline from an earlier Cloud Data Fusion version ([CDAP-21073](https://cdap.atlassian.net/browse/CDAP-21073)).

  * Improved performance by removing a call to the list apps API during pipeline deployment when checking if a pipeline already exists ([CDAP-21074](https://cdap.atlassian.net/browse/CDAP-21074)).


]]>
