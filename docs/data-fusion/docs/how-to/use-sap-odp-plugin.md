---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin/
title: SAP ODP batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:26.288344+00:00
---

# SAP ODP batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  SAP ODP batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance about configuring the SAP ODP plugin in Cloud Data Fusion. 

The [SAP ODP](https://learning.sap.com/learning-journey/upgrading-your-sap-bw-skills-to-sap-bw-4hana/introducing-odp_f2dbacc1-4492-4cd5-8b62-4785bb538ea0) plugin enables bulk data integration from SAP applications with BigQuery or other supported target systems using Cloud Data Fusion. The plugin has the following key features:

  * Uses SAP ECC, SAP S4/HANA, or SAP BW as a source system
  * Uses [SAP CDC (Change Data Capture)](https://help.sap.com/docs/SAP_DATA_SERVICES/e54136ab6a4a43e6a370265bf0a2d744/57200fa06d6d1014b3fc9283b0e91070.html) to track and extract new and delta data in the data sources
  * Uses batch extraction mode
  * Supports [SAP DataSources](https://learning.sap.com/learning-journey/upgrading-your-sap-bw-skills-to-sap-bw-4hana/working-with-odp-context-sap-extractors_c442fe8f-ec26-4def-bc41-7fb10dd53bf9) and [ABAP CDS views](https://learning.sap.com/learning-journey/upgrading-your-sap-bw-skills-to-sap-bw-4hana/working-with-odp-context-cds-view-based-extraction_f01df9a0-0e79-4d76-be38-d2cfac4dde42) as data sources



## Supported software versions

Software | Versions  
---|---  
SAP S4/HANA | SAP S4/HANA 1909 and later  
SAP ECC | SAP ERP6 NW 7.31 SP16 and later  
SAP JCo | SAP JCo version 3.0.20 and later  
Cloud Data Fusion | 6.3 and later  
**Note:** This documentation applies to Cloud Data Fusion 6.8.3 and later, and SAP ODP plugin 0.10.0 and later.

For more information about SAP on Google Cloud, see the [Overview of SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).

## Before you begin

Set up the following systems and services that are used by the SAP ODP plugin:

  1. [**Configure the SAP ERP system**](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-sap-erp). This process includes the following steps: 
     * Install the SAP Transport files.
     * Set up the required SAP authorizations and roles.
     * Set up the SAP Java Connector.
  2. [**Deploy the ODP plugin in Cloud Data Fusion**](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin#deploy-sap-plugin).

     * Important: choose a plugin version that's compatible with the Cloud Data Fusion version.
     * If you upgrade the version of your Cloud Data Fusion instance or plugin, evaluate the impact of the changes to the pipeline's functional scope and performance.
  3. **Establish RFC connectivity between Cloud Data Fusion and SAP**.

     * Ensure that communication is enabled between the Cloud Data Fusion instance and the SAP server.
     * For private instances, set up [VPC network peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering).
     * Both the SAP system and the Cloud Data Fusion instance must be in the same project.



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **SapODP**. The SAP ODP node appears in your pipeline.
  4. To configure the source, go to the SAP ODP node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the SAP ODP node—for example, `SAP ODP tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to SAP, follow these steps:

        1. Keep **Use connection** turned off.
        2. In the **Connection** section, enter the following information from the SAP account in these fields:

           1. In the **Reference name** field, enter a name for the connection that identifies this source for lineage.
           2. In the **SAP client** field, enter the client name of a specific instance or environment within SAP. An SAP administrator can provide the client name.
           3. In the **SAP language** field, enter an SAP logon language. The default is **EN** (English).
           4. Select one of the following **Connection types**.

**Note:** **Load balanced (via SAP Message Server)** is recommended.
              * **Direct (via SAP Application Server)**. If you choose this default type, enter information in the following fields: **SAP application server host** , **SAP system number** , and **SAP router**.
              * **Load balanced (via SAP Message Server)**. If you choose this type, enter information in the following fields: **SAP Message Server host** , **SAP Message Server service or port number** , **SAP System ID (SID)** , and **SAP logon group name**.
           5. In the **Context** field, select the type of data source you're using.

           6. In the **SAP ODP source name** field, enter the name of the data source you're using.

           7. In the **Extract type** field, select the type of data extraction. The default is **Full (all data)**.

           8. Provide the SAP credentials: ask the SAP administrator for **SAP logon username** and **Password**.

           9. In the **JCo Library Cloud Storage path** field, enter the SAP Java Connector (SAP JCo) path in Cloud Storage that contains the SAP JCo library files you uploaded.

           10. To generate a schema based on the metadata from SAP that maps SAP data types to corresponding Cloud Data Fusion data types, click **Get schema**. For more information see, Data type mappings.

           11. Optional: to optimize the ingestion load from SAP, enter information in the following fields:

              1. In the **SAP ODP subscriber name** field, identify the subscriber for the data extraction from a valid DataSource.
              2. Using **Filter options** lets you extract records based on selection conditions.
              3. In the **Number of splits** field, you can create partitions to extract data records in parallel, which improves performance. The number of splits can affect SAP work processes and must be selected carefully.
              4. In the **Package size** field, specify the number of records to extract in a Single SAP network call. The package size impacts performance and available resources and must be selected carefully.

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).

If a connection doesn't exist, to create a reusable connection, follow these steps:

        1. Click **Add connection > SapOdp**.
        2. On the **Create a SapOdp connection** page that opens, enter a connection name and description.
        3. In the **SAP client** field, enter the client name of a specific instance or environment in SAP. An SAP administrator can provide the client name.
        4. In the **SAP language** field, enter an SAP logon language. The default is **EN** (English).
        5. Select one of the following **Connection types**.

**Note:** **Load balanced (via SAP Message Server)** is recommended.
           * **Direct (via SAP Application Server)**. If you choose this default type, enter information in the following fields: **SAP application server host** , **SAP system number** , and **SAP router**.
           * **Load balanced (via SAP Message Server)**. If you choose this type, enter information in the following fields: **SAP Message Server host** , **SAP Message Server service or port number** , **SAP System ID (SID)** , and **SAP logon group name**.
        6. In the SAP ODP source name, enter the ODP DataSource name from SAP.

        7. Provide the SAP credentials: ask the SAP administrator for the **SAP logon username** and **Password** values.

        8. In the **JCo Library Cloud Storage path** field, enter the SAP Java Connector (SAP JCo) path in Cloud Storage that contains the SAP JCo library files that you uploaded.

        9. In the **Wait time** field, enter a time to wait (in seconds) before the next retry—for example, `60`.

        10. In the **Retry count** field, enter the maximum number of retry attempts—for example, `3`.

        11. Optional: in the **Additional SAP connection properties** field, enter key-value pairs that must override the SAP JCo defaults.

        12. Click **Create**.




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Use a reusable connection. If a connection is used, you don't need to provide the credentials. For more information, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).  
**Name** | No | Yes | The name of the reusable connection.  
**SAP client** | Yes | Yes | The specific instance or environment in an SAP system.  
**SAP language** | Yes | Yes | The language in which the SAP user interface and data are displayed and processed.  
**Connection type** | No | Yes | The SAP connection type: **Direct** or**Load balanced**.  
**SAP application server host** | Yes | No | For the **Direct** connection type only, this hostname is from the SAP Application Server, which serves as a middleware layer between SAP clients (such as the SAP web interface, web browsers, or mobile apps) and the underlying database.  
**SAP system number** | Yes | No | For the **Direct** connection type only, this number is the unique identifier assigned to each SAP system. For example, `00`.  
**SAP router** | Yes | No | For the **Direct** connection type only, this is the router string for the proxy server, which provides a secure channel for communication between SAP systems and external clients or partners.  
**SAP Message Server host** | Yes | No | For the **Load balanced** connection type only, this is the name of the host, which facilitates load balancing across multiple application servers in SAP.  
**SAP Message Server service or port number** | Yes | No | For the **Load balanced** connection type only, this is the network port where the SAP Message Server listens for incoming connections from SAP clients and application servers within SAP.  
**SAP system ID (SID)** | Yes | No | For the **Load balanced** connection type only, this ID is assigned to each SAP system.  
**SAP logon group name** | Yes | No | The name of the logical grouping or configuration of multiple SAP application servers. The default is `PUBLIC`.  
**Object type** | N/A | N/A | The supported object types: **DataSources/Extractors** or **ABAP Core Data Services**.  
**SAP ODP source name** | Yes | Yes | The SAP DataSources or CDS view name (for example, `2LIS_02_ITM`).  
**Extract type** | Yes | Yes | The plugin supports the following two types of data extraction: 

  * **Full (all data)** : extracts all available data.
  * **Sync (automatic selection based on previous execution)** : determines whether full, delta (incremental), or recovery (recover data from last execution) mode should be run, based on the previous execution type and status available in SAP. It extracts full data in the initial pipeline execution (ODP mode F) and changes data in subsequent pipeline executions (ODP modes D, R).

  
**SAP logon username** | Yes | Yes | Username for SAP  
Recommended: If the username changes periodically, use a [macro](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382043060/Using+macros+to+create+a+dynamic+data+pipeline).  
**SAP logon password** | Yes | Yes | SAP password.  
Recommended: use [secure macros](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys).  
**GCP project ID** | Yes | Yes | Google Cloud project ID.  
**SAP JCo library GCS path** | Yes | Yes | The path to the Cloud Storage where you uploaded the SAP JCo library files.  
**Get schema** | N/A | N/A | The plugin generates a schema based on the metadata from SAP, which maps SAP data types to the corresponding Cloud Data Fusion data types. See Data type mapping.  
**SAP ODP subscriber name** | Yes | Yes | The ODP subscriber for the data extraction from a valid SAP DataSource or CDS view. It must have the following: 

  * A maximum of 32 characters, without spaces
  * Contain only `a` to `z`, `A` to `Z`, `0` to `9`, `_`, or `/`
  * Unique for different pipelines extracting data from the same SAP DataSource

If the field is left blank, Cloud Data Fusion generates an ID using a combination of the project ID, namespace, and pipeline names. You can reuse a previous subscription, such as one created by a third-party tool.  
**Wait time** | Yes | No | This property lets data engineers select an appropriate wait time after each network call from Cloud Data Fusion to SAP.  
**Retry count** | Yes | No | The number of retry attempts while waiting for the network call to complete.  
**Filter options (equal)** | Yes | No | The value a field must have to be read.  
Filter options are lists of metadata field names and their value pairs. They define the filter condition to apply when reading data from an SAP DataSource. Only records that satisfy the conditions are extracted.  
The filter key corresponds to a field in the schema. It must be of a simple type (not `ARRAY`, `RECORD`, or `UNION`). **Example usage** :  
Field name: `MTART`  
Value: `FERT`  
**Filter options (range)** | Yes | No | The low and high bounds the value a field must have to be read.  
Filter options are lists of metadata field names and their value pairs. They define the filter condition to apply when reading data from an SAP DataSource. Only records that satisfy the conditions are extracted.  
The filter key corresponds to a field in the schema. It has the format low AND high. **Example usage** :  
Field name: `ERDAT`  
Low value: `2023-11-01`  
High value: `2023-11-30`  
**Filter options (less equal)** | Yes | No | The value that a field must be less than or equal to.  
Filter options are lists of metadata field names and their value pairs. They define the filter condition to apply when reading data from an SAP DataSource. Only records that satisfy the conditions are extracted.  
The filter key corresponds to a field in the schema. It must be of a simple type (not `ARRAY`, `RECORD`, or `UNION`). **Example usage** :  
Field name: `MATNR`  
Value: `10008`  
**Filter options (greater equal)** | Yes | No | The value that a field must be greater than to be read.  
Filter options are lists of metadata field names and their value pairs. They define the filter condition to apply when reading data from an SAP DataSource. Only records that satisfy the conditions are extracted.  
The filter key corresponds to a field in the schema. It must be of a simple type (not `ARRAY`, `RECORD`, or `UNION`). **Example usage** :  
Field name: `MATNR`  
Value: `10008`  
**Filter options (not equal)** | Yes | No | Defines the value that a field must not be equal to be read.  
Filter options are lists of metadata field names and their value pairs. They define the filter condition to apply when reading data from an SAP DataSource. Only records that satisfy the conditions are extracted.  
The filter key corresponds to a field in the schema. It must be of a simple type (not `ARRAY`, `RECORD`, or `UNION`). **Example usage** :  
Field name: `MTART`  
Value: `FERT`  
**Number of splits to generate** | Yes | No | Creates partitions to extract records in parallel.  
The runtime engine creates the specified number of partitions (and SAP connections) while extracting the records.  
_Use caution when increasing this value because it increases the simultaneous connections with SAP_.  
**Recommended** : plan for SAP connections for each pipeline and the total number of pipelines running concurrently.  
If the value is 0 or left blank, Cloud Data Fusion chooses an appropriate value, based on the number of executors available, the records to extract, and the package size.  
**Package size (in KB)** | Yes | No | The number of records to extract in a single SAP network call. It's the number of records that SAP buffers in memory during every network extract call.  
_Use caution when setting this property_. Multiple data pipelines extracting data can peak the memory usage, causing failures due to `Out of memory` errors. 

  * Enter a positive, whole number.
  * If 0 or left blank, the plugin uses a standard value of 70000, or an appropriately calculated value.
  * If the data pipeline fails due to `Out of memory` errors, either decrease the package size or increase the memory available for your SAP work processes.

  
**Additional SAP connection properties** | Yes | No | Set additional SAP JCo properties to override the SAP JCo defaults. For example, setting `jco.destination.pool_capacity = 10` overrides the default connection pool capacity.  
  
### Data type mappings

The following table is a list of SAP data types with corresponding Cloud Data Fusion types.

SAP data type | ABAP type | SAP description | Cloud Data Fusion data type  
---|---|---|---  
`INT1` (Numeric) | b | 1-byte integer | int  
`INT2` (Numeric) | s | 2-byte integer | int  
`INT4` (Numeric) | i | 4-byte integer | int  
`INT8` (Numeric) | 8 | 8-byte integer | long  
`DEC` (Numeric) | p | Packed number in BCD format (DEC) | decimal  
`DF16_DEC`, `DF16_RAW` (Numeric) | a | Decimal floating point 8 bytes IEEE 754r | double  
`DF34_DEC`, `DF34_RAW` (Numeric) | e | Decimal floating point 16 bytes IEEE 754r | double  
`FLTP` (Numeric) | f | Binary floating point number | double  
`CHAR`, `LCHR` (Character) | c | Character string | string  
`SSTRING`, `[GEOM_EWKB](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abenlength_functions.htm)` (Character) | string | Character string | string  
`STRING` (Character) | string | Character string CLOB | bytes  
`NUMC`, `ACCP` (Character) | n | Numeric text | string  
`RAW`, `LRAW` (Byte) | x | Binary data | bytes  
`RAWSTRING` (Byte) | xstring | Byte string BLOB | bytes  
`DATS` (Date/Time) | d | Date | date  
`TIMS` (Date/Time) | t | Time | time  
`TIMS` (Date/Time) | utcl | [Utclong](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abenbuiltin_types_date_time.htm)), TimeStamp | timestamp  
  
## Limitations

To ensure pipelines are correctly defined and executed, review the following plugin limitations:

  * Package sizes greater than 50k aren't supported.
  * Data sources that don't support delta extraction fail in Sync mode.
  * In a custom data source, if the package size isn't handled, then the pipeline fails in large data extractions.



## Use cases

Two extraction contexts are supported:

  * DataSources or Extractors (SAPI)
  * ODP context ABAP CDS (ABAP_CDS)



The ODP plugin supports the following standard and custom data sources for both contexts:

ODP data source | Context | Full extraction | Delta extraction  
---|---|---|---  
SAP Standard pre-delivered | SAPI | Supported | Supported  
Custom (Z*) | SAPI | Supported | Supported  
SAP Standard pre delivered | ABAP_CDS | Supported | Supported  
Custom (Z*) | ABAP_CDS | Supported | Supported  
  
## Release notes

  * [March 02, 2026](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_02_2026)
  * [January 29, 2026](https://docs.cloud.google.com/data-fusion/docs/release-notes#January_29_2026)
  * [July 20, 2025](https://docs.cloud.google.com/data-fusion/docs/release-notes#July_20_2025)
  * [September 26, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#September_26_2024)
  * [December 19, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#December_19_2023)
  * [September 6, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#September_06_2023)
  * [July 20, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#July_20_2023)
  * [March 8, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_08_2023)



## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs).
  * Learn more about [SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
