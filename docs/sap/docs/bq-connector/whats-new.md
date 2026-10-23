---
url: https://docs.cloud.google.com/sap/docs/bq-connector/whats-new/
title: What's new with BigQuery Connector for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:45.807633+00:00
---

# What's new with BigQuery Connector for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/whats-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  What's new with BigQuery Connector for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This document lists significant changes to the BigQuery Connector for SAP including version-specific enhancements.

To view all of the announcements from SAP on Google Cloud, see [Release notes](https://docs.cloud.google.com/sap/docs/release-notes).

## Updating BigQuery Connector for SAP

For information on how to update BigQuery Connector for SAP, see [Update BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#bqc4sap-operations-bqc-update).

## Version 2.15

Version 2.15 of the BigQuery Connector for SAP introduces the following bug fixes:

  * **Standalone SLT column descriptions** : When you use [standalone SAP LT Replication Server system configurations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#perf-architecture), you can view column descriptions correctly. This version resolves an issue where column descriptions failed to display.

  * **Pub/Sub attribute consistency** : When you use [CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api), your message attributes remain consistent with the payload JSON. This version resolves an issue that caused the `operation_flag` attribute to mismatch due to attribute overwrites when processing multiple record types within a single batch.




## Version 2.14

Version 2.14 of the BigQuery Connector for SAP introduces the following enhancement:

  * **Enhanced security for configuration tables** : To align with a security-first approach, the configuration tables `/GOOG/CLIENT_KEY` and `/GOOG/SERVIC_MAP` are assigned to the custom authorization group `ZSGC`. To maintain access to these tables, you must assign the `ZSGC` authorization group to existing user roles. Otherwise, users cannot access these tables. For more information, see [Manage authorizations for configuration tables](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#manage-authorizations-config-tables).



## Version 2.13

Version 2.13 of the BigQuery Connector for SAP introduces the following enhancement:

  * **Fixed data replication failure for partitioned tables when schema caching is enabled** : This version resolves an issue that prevented data replication for [partitioned tables](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#table_partitioning) when [table schema caching](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#table-schema-caching) was enabled. The connector correctly handles partitioning metadata to help ensure successful replication. This update lets you maximize the performance of your partitioned table replications by using schema caching to reduce BigQuery API calls.



## Version 2.12

Version 2.12 of the BigQuery Connector for SAP introduces the following enhancements:

  * **File-based replication to Cloud Storage** : This feature lets you replicate SAP data to Cloud Storage as JSON files. Once the data is available in your Cloud Storage bucket, the replication journey by the connector is complete. This offers you the flexibility to use your own [data integration methods](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication#whats-next) to manage the final ingestion into BigQuery for analytics. For more information, see [File-based replication to Cloud Storage](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#file-based-replication-gcs).

  * **Table schema caching** : For [streaming data replication to BigQuery](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only), to improve replication performance and resolve the BigQuery API quota limit error, you can enable table schema caching. With this feature enabled, the connector retrieves table schema definitions directly from memory when no changes are detected. This reduces the number of `tables.get` calls to the BigQuery API, which helps in keeping your replication within quota limits. For more information, see the [Troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting#too-many-api-requests).

  * **Unicode data handling** : This release resolves an issue to ensure that Unicode and non-ASCII characters are accurately replicated. This fix applies to [CDC replication to BigQuery through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#cdc-replication-with-pubsub) and [file-based replication to Cloud Storage](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#file-based-replication-gcs).




## Version 2.11

Version 2.11 of the BigQuery Connector for SAP introduces the following enhancements:

  * **Support for data replication to multiple Google Cloud projects by using project-specific service accounts** : This feature lets you set up JWT authentication, where you use project-specific service accounts to meet the unique security and billing requirements of each target project. For more information about how to do this, see [Authenticate with JWT by using project-specific service accounts to multiple projects](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt-project-specific-sa).



## Version 2.10

Version 2.10 of the BigQuery Connector for SAP introduces the following enhancements:

  * **Support for non-ASCII characters in Change Data Capture (CDC) replication through Pub/Sub** : We resolved an issue where CDC replication through Pub/Sub failed if your source data contained non-ASCII characters. The BigQuery Connector for SAP successfully performs CDC replication through Pub/Sub, ensuring your data, including non-ASCII characters, replicates to BigQuery.

  * **Enhanced server-side error handling** : To help you troubleshoot missing replication records, server-side error handling provides detailed logs. You can review the SAP LT Replication Server application logs to access this detailed error information.




## Version 2.9

Version 2.9 of the BigQuery Connector for SAP introduces the following enhancements:

  * **Change Data Capture (CDC) replication through Pub/Sub** : CDC replication through Pub/Sub updates your BigQuery tables by processing and applying streamed changes to existing data. This keeps your BigQuery data always up-to-date and accurately reflecting any additions, changes, or deletions from your SAP source tables. As a result, your analytics always have the latest information without the need for custom deduplication.

The BigQuery Connector for SAP captures any updates or deletions to SAP records, and publishes these changes to a Pub/Sub topic. A BigQuery subscription then streams the changes to the relevant BigQuery table by using the [Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api).

For more information, see [Overview of the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview).




## Version 2.8

Version 2.8 of the BigQuery Connector for SAP introduces the following enhancements:

  * **Record compression option at field level** : The BigQuery Connector for SAP offers record compression option at the field level. This option lets you replicate specified empty fields with their initial values to BigQuery, while still using record compression at the table level. For more information, see [Record compression](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#record_compression).

  * **Transaction to view the version of BigQuery Connector for SAP** : You can view the version of the BigQuery Connector for SAP installed on your system, by using the transaction `/GOOG/BQC_VERSION`.

  * **Enhanced HTTP error handling** : The enhancement spot `/GOOG/ES_GCP_HTTP_CLIENT` lets you handle HTTP errors originating on the SAP client side, enabling more robust and customized integrations. For more information, see [Enhanced HTTP error handling](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#enhancement-exits).

  * **Cluster table replication** : An issue that prevented replication of multiple tables belonging to the same cluster within a single Mass Transfer ID has been resolved. From version 2.8 of the BigQuery Connector for SAP, you can replicate all cluster tables within a single Mass Transfer ID.




## Version 2.7

Version 2.7 of the BigQuery Connector for SAP extends support for using the SAP SLT add-on - DMIS 2018 SP 11.

## Version 2.6

Version 2.6 of the BigQuery Connector for SAP introduces the following enhancements:

  * **Create Table tool** : For empty source tables in SAP, the Create Table tool lets you create tables in the BigQuery dataset. For information about how to run the tool, see [Create Table tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#create-table-tool).

  * **Mass Field Conversion tool** : For mass conversion of target field mapping into `STRING`, you can use the Mass Field Conversion tool. For information about how to run the tool, see [Mass Field Conversion tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#mass-field-conversion-tool).

  * **Read-only view of BigQuery Connector for SAP settings** : For users who only need to view the BigQuery Connector for SAP settings, BigQuery Connector for SAP provides a custom transaction `/GOOG/SLT_SETT_DISP`. Administrators can grant access to this transaction for users who require read-only access only. For more information, see [View the connector settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#view-bqc-settings).

  * **Custom name for the PSE file** : For the PSE file used for signing the JSON Key, which is used in JWT-based authentication, BigQuery Connector for SAP supports custom name. Previously, the PSE filename was required to be `SAPZG_JWT100.PSE`.

  * **The Break at First Error Flag (`BREAK`) is enabled by default**: For new mass transfer keys created using the transaction `/GOOG/SLT_SETTINGS`, the `BREAK` flag is enabled by default.

  * **Enabled replication of cluster tables** : BigQuery Connector for SAP supports replication of data from cluster tables to BigQuery. If you've applied a hotfix for the replication of data from cluster tables, then before updating the BigQuery Connector for SAP to version 2.6, you must delete the hotfix. For more information about deleting a hotfix, see the SAP page [Creating, Editing, and Deleting Enhancement Implementations](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/5f/103a4280da9923e10000000a155106/content.htm?no_cache=true).

  * **Enhancements to the replication validation report** :

    * You can execute the replication validation report for specific tables in the mass transfer configuration. For more information, see [Run the Replication Validation tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#validate-rep-tool).

    * All count fields of the table `/GOOG/REPL_RES` can accommodate values greater than the 32-bit integer limit (`-2,147,483,648` to `+2,147,583,647`).

    * To follow the GoogleSQL [lexical structure and syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/lexical), all path expressions for querying counts on BigQuery are enclosed in backticks (`).

  * **Fixed default audience for JWT based authentication** : If you use Private Service Connect to connect to Google Cloud, then the default audience is correctly set during authentication. If you've applied a hotfix for this issue, then before updating the BigQuery Connector for SAP to version 2.6, you must delete the hotfix. For more information about deleting a hotfix, see the SAP page [Creating, Editing, and Deleting Enhancement Implementations](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/5f/103a4280da9923e10000000a155106/content.htm?no_cache=true).

  * **Fixed mapping of`INT8` data type**: In [supported versions](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#reqs-software-sap) of the SAP system, the mapping from `INT8` to `INTEGER` data type functions as expected.

  * **Improved error messages** : To help make troubleshooting easier, the clarity and comprehensibility of error messages are enhanced within the SDK.




## Version 2.5

### Enhancements

  * **Support for RFC destinations** : You can now use RFC destinations to connect to Google Cloud. To get you started, the transport files include sample RFC destinations. By using RFC destinations, you can perform the following: connect to Google Cloud through Private Service Connect endpoints, configure proxy server settings, and enable HTTP compression. For more information, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).

  * **Support for using Private Service Connect** : You can now use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC) endpoints to allow private consumption of Google Cloud APIs and services. You specify your PSC endpoints in your RFC destinations that the connector uses to connect to Google Cloud. RFC destinations are new with version 2.5 of BigQuery Connector for SAP. For more information, see [Specify Private Service Connector endpoints](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#specify_psc_endpoints).

  * **Token caching** : To improve replication performance and fault tolerance, the BigQuery Connector for SAP supports caching of the access token that allows access to BigQuery. For more information, see [Enable token caching](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#enable-token-caching).

  * **Automatic retry of access token retrieval for off-Google Cloud workloads** : For SAP workloads that are running outside of Google Cloud, BigQuery Connector for SAP now automatically retries access token retrieval in case there is a failure to do so. You can control the number of retries by setting a value for the advanced setting parameter `CMD_EXEC_TRIES`. For more information, see [Advanced settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#advanced-settings).

  * **Authenticate to Google Cloud using JWT for off-Google Cloud workloads** : For SAP workloads that are running outside of Google Cloud, you can now set up authentication to Google Cloud and authorization to access BigQuery using JSON Web Tokens (JWT) signed by Google Cloud. With JWT based authentication, you can authenticate to Google Cloud without the need of installing the Google Cloud CLI and creating an OS level command on the SAP LT Replication Server host. For more information, see [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt).

  * **Dynamic chunk sizing** : The dynamic chunk size feature lets you automatically reduce the chunk size and retry replication to BigQuery when the byte size of a chunk exceeds the maximum byte size for HTTP requests that BigQuery accepts. For more information, see [Dynamic chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#dynamic-chunk-size).

  * **New enhancement exit** : This version introduces a new enhancement exit that lets you collect logging data in case of HTTP errors, after the HTTP calls to BigQuery API. You can use those logs for troubleshooting the HTTP errors. For more information, see [Enhancement exits](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#enhancement-exits).

  * **Load Simulation tool** : The Load Simulation tool lets you simulate load to BigQuery. This in turn lets you assess replication performance, identify potential problems, understand the root cause of issues, and resolve them prior to actual replication of SAP data into BigQuery by using BigQuery Connector for SAP. For more information, see [Load Simulation tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#load-simulation-tool).




## Version 2.2 to 2.4 (Not available)

Version 2.2 to 2.4 of BigQuery Connector for SAP are not available.

## Version 2.1

### Enhancements

  * **Language support** : The connector supports execution of background jobs that are running on the SAP LT Replication Server in all languages that SAP SLT supports. For more information, see [Language support](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#bq-language-support).

  * **Troubleshooting invalid data errors** : The connector contains improved error messages to help you troubleshoot invalid data errors. For more information, see [Issue: Error messages related to invalid data](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/troubleshooting#bq-invalid-data-error).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
