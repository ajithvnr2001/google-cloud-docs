---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin/
title: SAP table batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:42.195993+00:00
---

# SAP table batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  SAP table batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure bulk extractions from SAP application data. 

The SAP table batch source plugin (SAP Table plugin) lets you read data from SAP standard and custom tables or views. It enables bulk data ingestion from SAP applications into BigQuery, or any other supported target system, using Cloud Data Fusion. The plugin has the following key features:

  * Uses SAP ECC, SAP S4/HANA, or SAP BW as a source system
  * Doesn't use [SAP CDC (Change Data Capture)](https://help.sap.com/docs/SAP_DATA_SERVICES/e54136ab6a4a43e6a370265bf0a2d744/57200fa06d6d1014b3fc9283b0e91070.html) to track and extract new and delta data in the data sources
  * Uses batch extraction mode
  * Supports SAP tables and [ABAP CDS views](https://learning.sap.com/learning-journey/upgrading-your-sap-bw-skills-to-sap-bw-4hana/working-with-odp-context-cds-view-based-extraction_f01df9a0-0e79-4d76-be38-d2cfac4dde42) as data sources
  * Accesses SAP data through the application layer



You can read data from:

  * Transparent tables
  * Cluster tables
  * Pool tables
  * ABAP CDS views
  * SAP BW ADSO objects



## Supported software versions

Software | Versions  
---|---  
SAP S4/HANA | SAP S4/HANA 1909 and later  
SAP ECC | SAP ERP6 NW 7.31 SP16 and later  
SAP JCo | SAP JCo version 3.0.20 and later  
Cloud Data Fusion | 6.3 and later  
**Note:** This documentation applies to Cloud Data Fusion 6.8.3 and later, and SAP Table plugin 0.10.0 and later.

For more information about SAP on Google Cloud, see the [Overview of SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).

## Before you begin

Set up the following systems and services that are used by the SAP Table plugin:

  1. [**Configure the SAP ERP system**](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-sap-erp). This process includes the following steps: 
     * Install the SAP Transport files.
     * Set up the required SAP authorizations and roles.
     * Set up the SAP Java Connector.
  2. [**Deploy the plugin in Cloud Data Fusion**](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin#deploy-sap-plugin).

     * Important: choose a plugin version that's compatible with the Cloud Data Fusion version.
     * If you upgrade the version of your Cloud Data Fusion instance or plugin, evaluate the impact of the changes to the pipeline's functional scope and performance.
  3. **Establish RFC connectivity between Cloud Data Fusion and SAP**.

     * Ensure that communication is enabled between the Cloud Data Fusion instance and the SAP server.
     * For private instances, set up [VPC network peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering).
     * Both the SAP system and the Cloud Data Fusion instance must be in the same project.



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **Sap Table**. The SAP Table node appears in your pipeline.
  4. To configure the source, go to the SAP Table node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the SAP Table node—for example, `SAP tables`.
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
           5. In the **SAP table/view name** field, enter the name of the table or view from your SAP system.

           6. Provide the SAP credentials: ask your SAP administrator for **SAP logon username** and **Password**.

           7. In the **JCo Library Cloud Storage path** field, enter the SAP Java Connector (SAP JCo) path in Cloud Storage that contains the SAP JCo library files you uploaded.

           8. To generate a schema based on the metadata from SAP that maps SAP data types to corresponding Cloud Data Fusion data types, click **Get schema**. For more information see, Data type mappings.

           9. Optional: to optimize the ingestion load from SAP, enter information in the following fields:

              1. Using **Filter options** lets you extract records based on selection conditions, such as columns having a defined set of values. Define the conditions in OpenSQL syntax in a `WHERE` clause. For example, this query returns all rows from the `Roster` table where the `SchoolID` column has the value `SchoolID > 52`:
                     
                     SELECT * FROM Roster WHERE SchoolID > 52;
                     

For more information, see Supported filters.

              2. In the **Number of rows to fetch** field, you can limit the data extracted by providing a positive, whole number of rows.

              3. In the **Number of splits** field, you can create partitions to extract data records in parallel, which improves performance. The number of splits can affect SAP work processes and must be selected carefully.

              4. In the **Package size** field, specify the number of records to extract in a Single SAP network call. The package size impacts performance and available resources and must be selected carefully.

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).

If a connection doesn't exist, to create a reusable connection, follow these steps:

        1. Click **Add connection > SapTable**.
        2. On the **Create a SapTable connection** page that opens, enter a connection name and description.
        3. In the **SAP client** field, enter the client name of a specific instance or environment in SAP. An SAP administrator can provide the client name.
        4. In the **SAP language** field, enter an SAP logon language. The default is **EN** (English).
        5. Select one of the following **Connection types**.

**Note:** **Load balanced (via SAP Message Server)** is recommended.
           * **Direct (via SAP Application Server)**. If you choose this default type, enter information in the following fields: **SAP application server host** , **SAP system number** , and **SAP router**.
           * **Load balanced (via SAP Message Server)**. If you choose this type, enter information in the following fields: **SAP Message Server host** , **SAP Message Server service or port number** , **SAP System ID (SID)** , and **SAP logon group name**.
        6. Provide the SAP credentials: ask your SAP administrator for the **SAP logon username** and **Password** values.

        7. In the **JCo Library Cloud Storage path** field, enter the SAP Java Connector (SAP JCo) path in Cloud Storage that contains the SAP JCo library files that you uploaded.

        8. Optional: In the **Additional SAP connection properties** field, enter key-value pairs that must override the SAP JCo defaults.

        9. Click **Create**.




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Use a reusable connection. If a connection is used, you don't need to provide the credentials. For more information, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).  
**Reference name** | No | Yes | If **Use connection** isn't turned on, this field appears. The name of the connection to use for lineage.  
**Name** | No | Yes | If **Use connection** is turned on, this field appears. The name of the reusable connection.  
**SAP client** | Yes | Yes | The instance or environment in an SAP system.  
**Take snapshot** | Yes | Yes | Enable snapshots of data in SAP.  
**When to turn on snapshots** : 

  * Extracting from any active transactional table data
  * Extracting on the tables where the data queries are slower and consume more memory for every extraction call.

  
**When to turn off snapshots** : you're running multiple, large-volume data extractions in parallel. Snapshots use buffer tables in SAP, which might lead to `out of memory` issues in SAP. On completion of data extraction, however, the buffer table is cleared.  
**SAP language** | Yes | Yes | The language in which the SAP user interface and data are displayed and processed.  
**Connection type** | No | Yes | The SAP connection type: **Direct** or**Load balanced**.  
**SAP application server host** | Yes | No | For the **Direct** connection type only, this hostname is from the SAP Application Server, which serves as a middleware layer between SAP clients (such as the SAP web interface, web browsers, or mobile apps) and the underlying database.  
**SAP system number** | Yes | No | For the **Direct** connection type only, this number is the unique identifier assigned to each SAP system. For example, `00`.  
**SAP router** | Yes | No | For the **Direct** connection type only, this is the router string for the proxy server, which provides a secure channel for communication between SAP systems and external clients or partners.  
**SAP Message Server host** | Yes | No | For the **Load balanced** connection type only, this is the name of the host, which facilitates load balancing across multiple application servers in SAP.  
**SAP Message Server service or port number** | Yes | No | For the **Load balanced** connection type only, this is the network port where the SAP Message Server listens for incoming connections from SAP clients and application servers within SAP.  
**SAP system ID (SID)** | Yes | No | For the **Load balanced** connection type only, this ID is assigned to each SAP system.  
**SAP logon group name** | Yes | No | The name of the logical grouping or configuration of multiple SAP application servers. The default is `PUBLIC`.  
**SAP table/view name** | Yes | Yes | A valid, case-insensitive table or view name where all columns can be extracted.  
**SAP logon username** | Yes | Yes | Username for SAP  
Recommended: if the username changes periodically, use a [macro](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382043060/Using+macros+to+create+a+dynamic+data+pipeline).  
**SAP logon password** | Yes | Yes | SAP password.  
Recommended: use [secure macros](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys).  
**GCP project ID** | Yes | Yes | Google Cloud project ID.  
**SAP JCo library GCS path** | Yes | Yes | The path to the Cloud Storage where you uploaded the SAP JCo library files.  
**Get schema** | N/A | N/A | The plugin generates a schema based on the metadata from SAP, which maps SAP data types to the corresponding Cloud Data Fusion data types. See Data type mapping.  
**Additional SAP connection properties** | Yes | No | Set additional SAP JCo properties to override the SAP JCo defaults. For example, setting `jco.destination.pool_capacity = 10` overrides the default connection pool capacity.  
**Filters** | Yes | No | Conditions specified in Open SQL syntax that filter using a SQL `WHERE` clause. Extract records based on conditions, such as those in columns with a defined set of values, or a range of values.   
For more information, see Supported filters.  
**Number of rows to fetch** | Yes | No | Limits the number of extracted records. 

  * Enter a positive, whole number.
  * If the value is `0` or left blank, Cloud Data Fusion extracts all records from the table.
  * If you enter a positive value that is greater than the number of records selected (based on your other filter values), Cloud Data Fusion only extracts the selected records.

  
**Number of splits to generate** | Yes | No | Creates partitions to extract records in parallel.  
The runtime engine creates the specified number of partitions (and SAP connections) while extracting the records.  
_Use caution when increasing this value, as it increases the simultaneous connections with SAP_.  
**Recommended** : plan to have SAP connections for each pipeline and the total number of pipelines running concurrently.  
If the value is 0 or left blank, Cloud Data Fusion chooses an appropriate value, based on the number of executors available, the records to extract, and the package size.  
**Package size** | Yes | No | The number of records to extract in a single SAP network call. It's the number of records that SAP buffers in memory during every network extract call.  
_Use caution when setting this property_. Multiple data pipelines extracting data can peak the memory usage, causing failures due to `Out of memory` errors. 

  * Enter a positive, whole number.
  * If 0 or left blank, the plugin uses a standard value of 70000, or an appropriately calculated value.
  * If the data pipeline fails due to `Out of memory` errors, either decrease the package size or increase the memory available for your SAP work processes.

  
  
### Supported filters

The following filter conditions are supported.

#### Filter containing a comparison operator

Use comparison operators to perform more complex filtering based on comparisons between values.

##### Syntax
    
    
        SELECT * FROM table_name WHERE column_name > value; \
        SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2;
        

##### Example

`AUDAT GT '20230914'`

#### Filter containing a `LIKE` operator

Use `LIKE` operators for pattern matching. To match any character, use the `%` symbol as a wildcard.

##### Syntax
    
    
        SELECT * FROM table_name WHERE column_name LIKE 'pattern%';
        

##### Example

`ERNAM LIKE 'KIRAN%'`

#### Filter containing an `IN` operator

Use `IN` operators to specify a list of values to match against.

##### Syntax
    
    
        SELECT * FROM table_name WHERE column_name \
          IN ('value1', 'value2', 'value3');
        

##### Example

`ERNAM IN ( 'LEE' , 'KIRAN' )`

#### Filter containing a logical operator

Use logical operators to specify a list of values to match against.

##### Syntax
    
    
        SELECT * FROM table_name WHERE condition1 AND condition2; \
          SELECT * FROM table_name WHERE condition1 OR condition2; \
          SELECT * FROM table_name WHERE NOT condition;
        

##### Examples

  * `( AUDAT EQ '20220615' ) AND ( ERNAM LIKE 'LEE%' )`
  * `( AUDAT EQ '20220615' ) OR ( AUDAT EQ '20220617' )`



#### Filter containing a date range

Use date ranges to retrieve rows where a datetime column falls within a specific date range.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE datetime_column >= 'start_date' AND datetime_column <= 'end_date';
        

##### Example

`AUDAT GE '20230910' AND AUDAT LE '20230914'`

#### Filter containing a date comparison

Use date comparisons to retrieve rows where datetime is used.

##### Syntax
    
    
        SELECT * FROM table_name WHERE datetime_column > 'target_date';
        

##### Example

`AUDAT GE '20230910' AND AUDAT LE '20230914'`

#### Filter combining date and time

If your datetime column includes both date and time, you can filter accordingly.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE datetime_column >= 'target_datetime' \
          AND datetime_column <= 'target_datetime';
        

##### Example

`TIMESTAMP GE '20210602144800' AND TIMESTAMP LE '20210624080836'`

(Timestamp format : YYYYMMDDHHMMSS)

#### Filter combining multiple conditions with logical operators

You can retrieve rows that meet multiple conditions using logical operators, such as `AND` and `OR`.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE (column1 = 'value1' AND column2 > value2) \
          OR (column3 = 'value3' AND column4 < value4);
        

##### Example
    
    
        ( ERNAM EQ 'LEE' AND AUDAT GT '20220722' ) \
          OR ( BSTNK EQ 'PO54321065' AND BSTDK LT '20220714' )
        

#### Filter combining nested conditions

You can combine conditions in a nested manner to create complex filters.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE (column1 = 'value1' OR (column2 = 'value2' AND column3 > value3)) \
          AND column4 = 'value4';
        

##### Example
    
    
        ( ERDAT EQ '20220722' OR ( ERNAM EQ 'LEE' AND VDATU GT '20210623' ) ) \
          AND FMBDAT EQ '20220722'
        

#### Filter that uses subqueries

You can use subqueries to filter based on the results from another query.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE column1 IN (SELECT related_column FROM other_table WHERE condition);
        

##### Example

`VBELN IN ( SELECT VBELN FROM VBAK WHERE ERNAM = 'LEE' )`

#### Filter combining date and value conditions

You can combine date-based and value-based conditions in a complex filter.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE (column1 = 'value1' OR column2 = 'value2') \
          AND datetime_column > 'target_datetime';
        

##### Example
    
    
        ( ERDAT EQ '20220722' OR ERNAM EQ 'LEE' ) AND VDATU GT '20210623'
        

#### Filter containing Formatting Dates

In SAP, date and time fields are always saved without `-` or `:` at the database level.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE datetime_column >= 'YYYY-MM-DD HH:MM:SS' \
          AND datetime_column <= 'YYYY-M
        

#### **Not supported** : Filter containing functions and comparison operators

In SAP, functions at the WHERE clause of the QUERY aren't supported.

#### **Not supported** : Filter containing intervals

In SAP, the `NOW()` function isn't supported.

##### Syntax
    
    
        SELECT * FROM table_name \
          WHERE datetime_column >= NOW() - INTERVAL X DAY;
        

#### **Not supported** : Filter extracting date component

In SAP, offset filtering isn't supported.

##### Example
    
    
        WHERE YEAR+0(4) = 2023
        

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
`TIMS` (Date/Time) | utcl | ([Utclong](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abenbuiltin_types_date_time.htm)), TimeStamp | timestamp  
  
## Use cases

Two extraction contexts are supported:

  * SAP Database Tables and Views
  * SAP ABAP CDS



In each of the contexts, the SAP Table plugin supports standard and custom database tables and views.

## Limitations

The SAP Table plugin has the following limitations:

  * It doesn't support joining tables.
  * It doesn't support CDS views with parameters.
  * It doesn't support without key fields.
  * If the Snapshots feature is enabled, using a package size exceeding 30,000 might cause pipeline failures. This package size can vary, depending on the number of columns in the SAP table. You can calculate an optimal package size for a table using this formula: row size (in number of characters) * 5.
  * Connection Manager lets you browse a maximum of 1,000 SAP table names.
  * When a pipeline error occurs, such as an error in the sink, the SAP Table plugin attempts to clean up any active SAP side processes related to the extraction by calling the custom RFM intended for cleanup: `/GOOG/RFC_READ_TABLE_CLEANUP`.



## Release notes

  * [November 18, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#November_18_2024)
  * [August 9, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#August_09_2023)
  * [March 8, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_08_2023)
  * [June 16, 2021](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_16_2021)
  * [March 31, 2021](https://docs.cloud.google.com/data-fusion/docs/release-notes#March_31_2021)



## What's next

  * Learn more about [SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
