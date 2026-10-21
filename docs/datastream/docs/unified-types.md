---
url: https://docs.cloud.google.com/datastream/docs/unified-types/
title: Mappings of unified types to source and destination data types \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:57.676443+00:00
---

# Mappings of unified types to source and destination data types  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/unified-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Mappings of unified types to source and destination data types Stay organized with collections  Save and categorize content based on your preferences. 

Unified types are the data types that appear in the Avro or JSON events. They are a Datastream-specific, unified representation of a data type across multiple data sources and destinations that Datastream supports.

The unified types are the superset of all type representations across all supported source types, which represent the original source type in a generic but lossless way.

The following tables list:

  * The unified types associated with Datastream
  * The mappings between Oracle, MySQL, SQL Server, PostgreSQL, Salesforce, Spanner, ServiceNow, MongoDB, and Workday ([Preview](https://cloud.google.com/products/#product-launch-stages)) data types and the Datastream unified types



Refer to the [BigQuery destination documentation](https://docs.cloud.google.com/datastream/docs/destination-bigquery) for information about the mappings between the data types for the different sources and BigQuery.

## Datastream unified types

Type name | Info | Avro definition | JSON definition  
---|---|---|---  
`BOOLEAN` | boolean | boolean | boolean  
`BYTES` | A sequence of unsigned bytes | bytes | string  
`DATE` | Days since the epoch | [ A date logical type](https://avro.apache.org/docs/1.9.2/spec.html#Date) | string [ISO-8601]  
`DATETIME` | The date (in days since the epoch) and time (in microseconds since midnight) | A custom type
    
    
    {
      "type": "record",
      "name": "datetime",
      "fields": [
        {"name": "date",
         "type": "int",
         "logicalType": "date"},
        {"name": "time",
         "type": "long",
         "logicalType": "time-micros"}
      ]
    }
        

| string [ISO-8601]  
`DECIMAL (p,s)` | An arbitrary-precision signed decimal number | [ A decimal logical type](https://avro.apache.org/docs/1.9.2/spec.html#Decimal) | number  
`DOUBLE` | 64-bit floating point numbers | double | number  
`FLOAT` | 32-bit floating point numbers | float | number  
`GEOMETRY` | A spatial geometry or geography object | A custom type
    
    
    {
      "type": "record",
      "name": "geometry",
      "fields": [
        {"name": "value",
         "type": "bytes"},
        {"name": "srid",
         "type": "int"},
        {"name": "type",
         "type": "string"}
      ]
    }
        

| nested JSON  
`INTEGER` | A 32-bit integer | int | number  
`INTERVAL` | Duration between two events (in months, hours, and microseconds) | A custom type
    
    
    {
      "type": "record",
      "name": "interval",
      "fields": [
        {"name": "months",
         "type": "int"}
        {"name": "hours",
         "type": "int"},
        {"name": "micros",
         "type": "long"}
      ]
    }
        

| string [ISO-8601]  
`JSON` | A JSON object | A custom logical type
    
    
    {
      "type": "string",
      "logicalType": "json"
    }
    

| nested JSON  
`LONG` | A 64-bit integer | long | number  
`NUMBER` | A numeric data type | A custom logical type
    
    
    {
      "type": "string",
      "logicalType": "number"
    }
    

| string  
`STRING` | An unlimited string length | string | string  
`TIME` | How many microseconds elapsed since midnight, regardless of timezone. | [ A time-micros logical type](https://avro.apache.org/docs/1.9.2/spec.html#Time+%28microsecond+precision%29) | string [ISO-8601]  
`TIME INTERVAL` | How many microseconds elapsed between two events | A custom logical type
    
    
    {
      "type": "long",
      "logicalType": "time-interval-micros"
    }
    

| long  
`TIMESTAMP` | How many microseconds elapsed since the epoch, regardless of timezone | [ A timestamp logical type](https://avro.apache.org/docs/1.9.2/spec.html#Timestamp+%28microsecond+precision%29) | string [ISO-8601]  
`TIMESTAMP WITH TIME ZONE` | How many microseconds elapsed since the epoch with a specific timezone offset in milliseconds | A custom type
    
    
    {
      "type": "record",
      "name": "timestampTz",
      "fields": [
        {"name": "timestamp",
         "type": "long"
         "logicalType": "timestamp-micros"},
        {"name": "offset",
         "type": "int"
         "logicalType": "time-millis"}
      ]
    }
        

| string [ISO-8601]  
`TIME WITH TIME ZONE` | How many microseconds elapsed since midnight with a specific timezone offset | A custom type
    
    
    {
      "type": "record",
      "name": "timeTz",
      "fields": [
        {"name": "time",
         "type": "long"
         "logicalType": "time-micros"},
        {"name": "offset",
         "type": "int",
         "logicalType": "time-millis"}
      ]
    }
        

| string [ISO-8601]  
`UNSUPPORTED` | An unsupported data type | A custom logical type
    
    
    {
      "type": "null",
      "logicalType": "unsupported"
    }
    

| null  
`VARCHAR` | A string with a maximum length of n characters | A custom logical type
    
    
    {
      "type": "string",
      "logicalType": "varchar"
      "length": N
    }
    

| string  
  
## Map Oracle data types to Datastream unified types

**Oracle data type** | **Datastream unified type**  
---|---  
`ANYDATA` | `UNSUPPORTED`  
`BFILE` | `STRING`  
`BINARY DOUBLE` | `DOUBLE`  
`BINARY FLOAT` | `FLOAT`  
`BLOB` | `BYTES`  
`CHAR` | `VARCHAR`  
`CLOB` | `STRING`  
`DATE` | `DATETIME` Zero dates aren't supported and are replaced with `NULL` values.  
`DOUBLE PRECISION` | `DOUBLE`  
`FLOAT(p)` | `DOUBLE`  
`INTERVAL DAY TO SECOND` | `UNSUPPORTED`  
`INTERVAL YEAR TO MONTH` | `UNSUPPORTED`  
`LONG/LONG RAW` | `UNSUPPORTED`  
`NCHAR` | `STRING`  
`NCLOB` | `STRING`  
`NUMBER` | `NUMBER`  
`NUMBER(p,s<=0)` | If p<=18, then `LONG`. If p>18 or p=`*`, then `NUMBER`.  If the scale value (`s`) is less than 0, then Datastream assigns `s` to be equal to 0.  
`NUMBER(p,s>0)` | If p=`*`, then `DECIMAL(38,s)`, else `DECIMAL(p,s)`.If the precision value (`p`) is less than the scale value (`s`), then Datastream assigns `p` to be equal to `s`.  
`NVARCHAR2` | `STRING`  
`RAW` | `STRING`  
`ROWID` | `STRING`  
`SDO_GEOMETRY` | `UNSUPPORTED`  
`SMALLINT` | `INTEGER`  
`TIMESTAMP` | `TIMESTAMP` Zero dates aren't supported and are replaced with `NULL` values.  
`TIMESTAMP WITH TIME ZONE` | `TIMESTAMP WITH TIME ZONE` Zero dates aren't supported and are replaced with `NULL` values.  
[`UDT` (user-defined type)](https://docs.oracle.com/cd/E14435_01/win.111/e10927/featUDTs.htm#CJAGCAID) | `UNSUPPORTED`  
`UROWID` | `UNSUPPORTED`  
`VARCHAR` | `VARCHAR`  
`VARCHAR2` | `VARCHAR`  
`XMLTYPE` | `UNSUPPORTED`  
  
## Map MySQL data types to Datastream unified types

**MySQL data type** | **Datastream unified type**  
---|---  
`BIGINT(size) SIGNED` | `LONG`  
`BIGINT(size) UNSIGNED` | If the destination is BigQuery, then `DECIMAL`, if Cloud Storage, then `NUMBER`  
`BINARY(size)` | `STRING (hex encoded)`  
`BIT(size)` | `LONG`  
`BLOB(size)` | `STRING (hex encoded)`  
`BOOL` | `INTEGER`  
`CHAR(size)` | `STRING`  
`DATE` | If the destination is BigQuery, then `DATE`, if Cloud Storage, then `TIMESTAMP`  
`DATETIME(fsp)` | If the destination is BigQuery, then `DATETIME`, if Cloud Storage, then `TIMESTAMP`  
`DECIMAL(size, d)` | `DECIMAL(size, d)`  
`DOUBLE(size, d)` | `DOUBLE`  
`ENUM(val1, val2, val3, ...)` | `STRING`  
`FLOAT(p)` | `FLOAT`  
`FLOAT(size, d)` | `FLOAT`  
`GEOMETRY` | `UNSUPPORTED`  
`INTEGER(size) SIGNED` | `INTEGER`  
`INTEGER(size) UNSIGNED` | `LONG`  
`JSON` | If the destination is BigQuery, then `JSON`, if Cloud Storage, then `STRING` For BigQuery, `BOOLEAN`, `NUMBER`, `OBJECT`, `STRING`, `ARRAY` and `NULL` data types are supported.  
`LONGBLOB` | `STRING (hex encoded)`  
`LONGTEXT` | `STRING`  
`MEDIUMBLOB` | `STRING (hex encoded)`  
`MEDIUMINT(size)` | `INTEGER`  
`MEDIUMTEXT` | `STRING`  
`SET(val1, val2, val3, ...)` | `STRING`  
`SMALLINT(size)` | `INTEGER`  
`TEXT(size)` | `STRING`  
`TIME(fsp)` | If the destination is BigQuery, then `INTERVAL`, if Cloud Storage, then `TIME_INTERVAL`  
`TIMESTAMP(fsp)` | `TIMESTAMP`  
`TINYBLOB` | `STRING (hex encoded)`  
`TINYINT(size)` | `INTEGER`  
`TINYTEXT` | `STRING`  
`VARBINARY(size)` | `STRING (hex encoded)`  
`VARCHAR` | `STRING`  
`YEAR` | `INTEGER`  
  
## Map PostgreSQL data types to Datastream unified types

**PostgreSQL data type** | **Datastream unified type**  
---|---  
`ARRAY` | `JSON` Arrays of `DATE`, `TIMESTAMP` or `TIMESTAMP WITH TIME ZONE` data types aren't supported.  
`BIGINT` | `LONG`  
`BIT` | `BYTES`  
`BIT VARYING` | `BYTES`  
`BOOLEAN` | `BOOLEAN`  
`BOX` | `UNSUPPORTED`  
`BYTEA` | `BYTES`  
`CHARACTER` | 

  * If there is limit for length, then map to `VARCHAR`
  * Otherwise, map to `STRING`

  
`CHARACTER VARYING` | 

  * If there is limit for length, then map to `VARCHAR`
  * Otherwise, map to `STRING`

  
`CIDR` | `STRING`  
`CIRCLE` | `UNSUPPORTED`  
`CITEXT` | `STRING`  
`COMPOSITE` | `UNSUPPORTED`  
`DATE` | `DATE`  
`DOUBLE PRECISION` | `DOUBLE`  
`ENUM` | `STRING`  
`INET` | `STRING`  
`INTEGER` | `INTEGER`  
`INTERVAL` | `INTERVAL`  
`JSON` | `JSON`  
`JSONB` | `JSON`  
`LINE` | `UNSUPPORTED`  
`LSEG` | `UNSUPPORTED`  
`MACADDR` | `STRING`  
`MONEY` | `DOUBLE`  
`NUMERIC` | 

  * If precision = -1 and scale = -1 then map to `NUMBER`
  * Otherwise, map to `DECIMAL`

  
`OID` | `LONG`  
`PATH` | `UNSUPPORTED`  
`POINT` | `UNSUPPORTED`  
`POLYGON` | `UNSUPPORTED`  
`REAL` | `FLOAT`  
`SMALLINT` | `INTEGER`  
`SMALLSERIAL` | `INTEGER`  
`SERIAL` | `INTEGER`  
`TEXT` | `STRING`  
`TIME` | `TIME`  
`TIMESTAMP` | `TIMESTAMP`  
`TIMESTAMP WITH TIME ZONE` | `TIMESTAMP WITH TIME ZONE`  
`TIME WITH TIME ZONE` | `TIME WITH TIME ZONE`  
`TSQUERY` | `STRING`  
`TSVECTOR` | `STRING`  
`TXID SNAPSHOT` | `STRING`  
`UUID` | `STRING`  
`XID` | `STRING`  
`XID8` | `STRING`  
`XML` | `STRING`  
  
## Map SQL Server data types to Datastream unified types

**SQL Server data type** | **Datastream unified type**  
---|---  
`BIGINT` | `LONG`  
`BINARY` | `BYTES`  
`BIT` | `BOOLEAN`  
`CHAR` | `STRING`  
`DATE` | `DATE`  
`DATETIME2` | `DATETIME`  
`DATETIME` | `DATETIME`  
`DATETIMEOFFSET` | `TIMESTAMP WITH TIME ZONE`  
`DECIMAL` | `DECIMAL (p, s)`  
`FLOAT` | `DOUBLE`  
`GEOGRAPHY` | `GEOMETRY`  
`GEOMETRY` | `GEOMETRY`  
`INT` | `INTEGER`  
`IMAGE` | `BYTES`  
`MONEY` | `DECIMAL`  
`NCHAR` | `STRING`  
`NVARCHAR` | `STRING`  
`NVARCHAR(MAX)` | `STRING`  
`NTEXT` | `STRING`  
`NUMERIC` | `DECIMAL (p, s)`  
`REAL` | `FLOAT`  
`SMALLDATETIME` | `DATETIME`  
`SMALLINT` | `INTEGER`  
`SMALLMONEY` | `DECIMAL`  
`TEXT` | `STRING`  
`TINYINT` | `INTEGER`  
`TIME` | `TIME`  
`TIMESTAMP/ROWVERSION` | `BYTES`  
`UNIQUEIDENTIFIER` | `STRING`  
`VARCHAR` | `STRING`  
`VARCHAR(MAX)` | `STRING`  
`VARBINARY` | `BYTES`  
`VARBINARY(MAX)` | `BYTES`  
`XML` | `STRING`  
  
## Map Salesforce data types to Datastream unified types

There are two types of data types that Salesforce supports:

  * [Primitive data types](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/primitive_data_types.htm)
  * [Field types](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/field_types.htm)



### Primitive data type mappings

**Salesforce data type** | **Datastream unified type**  
---|---  
`BOOLEAN` | `BOOLEAN`  
`BYTE` | `BYTES`  
`DATE` | If the destination is BigQuery, then `DATE`, if Cloud Storage, then `TIMESTAMP`  
`DATETIME` | If the destination is BigQuery, then `DATETIME`, if Cloud Storage, then `TIMESTAMP`  
`DOUBLE` | `DOUBLE`  
`INT` | `INTEGER`  
`STRING` | `STRING`  
`TIME` | `TIME`  
  
### Field data type mappings

**Salesforce data type** | **Datastream unified type**  
---|---  
`ADDRESS` | Sub-fields of this compound field are replicated with their respective data types  
`ANYTYPE` (can be either `STRING`, `DATE`, `NUMBER`, or `BOOLEAN`) | `STRING`  
`COMBOBOX` | `STRING`  
`CURRENCY` | `DOUBLE`  
`DATACATEGORYGROUPREFERENCE` | `STRING`  
`EMAIL` | `STRING`  
`ENCRYPTEDSTRING` | `STRING`  
`GEOLOCATION` | Sub-fields of this compound field are replicated with their respective data types  
`ID` | `STRING`  
`JUNCTIONIDLIST` | `STRING`  
`MASTERRECORD` | `STRING`  
`MULTIPICKLIST` | `STRING`  
`PERCENT` | `DOUBLE`  
`PHONE` | `STRING`  
`PICKLIST` | `STRING`  
`REFERENCE` | `STRING`  
`TEXTAREA` | `STRING`  
`URL` | `STRING`  
  
## Map Workday data types to Datastream unified types

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Workday data type** | **Datastream unified type**  
---|---  
`ARRAYS` | `ARRAY`  
`BASE64BINARY` | `BYTES`  
`BOOLEAN` | `BOOLEAN`  
`COMPLEX TYPES` | `JSON`  
`DATE` | `DATE`  
`DATETIME` | `TIMESTAMP`  
`DECIMAL` | `DECIMAL`  
`STRING` | `STRING`  
  
## Map Spanner (GoogleSQL) data types to Datastream unified types

**Spanner data type** | **Unified data type**  
---|---  
`ARRAY` | `ARRAY`  
`BOOL` | `BOOLEAN`  
`BYTES` | `BYTES`  
`DATE` | `DATE`  
`FLOAT32` | `FLOAT`  
`FLOAT64` | `DOUBLE`  
`INT64` | `LONG`  
`JSON` | `JSON`  
`NUMERIC` | `NUMBER`  
`STRING` | `STRING`  
`TIMESTAMP` | `TIMESTAMP WITH TIME ZONE`  
`UUID` | `STRING`  
`PROTO` | `UNSUPPORTED`  
`ENUM` | `UNSUPPORTED`  
  
## Map Spanner (PostgreSQL) data types to Datastream unified types

**Spanner data type** | **Unified data type**  
---|---  
`ARRAY` | `ARRAY`  
`BIGINT` | `LONG`  
`BOOL` | `BOOLEAN`  
`BYTEA` | `BYTES`  
`CHARACTER VARYING` | `STRING`  
`DATE` | `DATE`  
`DECIMAL` | `NUMBER`  
`DOUBLE PRECISION` | `DOUBLE`  
`FLOAT8` | `DOUBLE`  
`INT8` | `LONG`  
`JSONB` | `JSON`  
`NUMERIC` | `NUMBER`  
`TEXT` | `STRING`  
`TIMESTAMP WITH TIME ZONE` | `TIMESTAMP WITH TIME ZONE`  
`TIMESTAMPTZ` | `TIMESTAMP WITH TIME ZONE`  
`VARCHAR` | `STRING`  
`UUID` | `STRING`  
  
## Map ServiceNow data types to Datastream unified types

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**ServiceNow data type** | **Datastream unified type**  
---|---  
`action_conditions` | `STRING`  
`approval_rules` | `STRING`  
`audio` | `STRING`  
`auto_increment` | `LONG`  
`auto_number` | `STRING`  
`boolean` | `BOOLEAN`  
`bootstrap_color` | `STRING`  
`breakdown_element` | `STRING`  
`calendar_date_time` | `DATETIME`  
`catalog_preview` | `STRING`  
`char` | `STRING`  
`choice` | `STRING`  
`collection` | `STRING`  
`color` | `STRING`  
`color_display` | `STRING`  
`composite_field` | `STRING`  
`composite_name` | `STRING`  
`compressed` | `STRING`  
`conditions` | `STRING`  
`condition_string` | `STRING`  
`counter` | `STRING`  
`css` | `STRING`  
`currency` | `DOUBLE`  
`currency2` | `JSON`  
`data_array` | `STRING`  
`data_object` | `JSON`  
`data_structure` | `JSON`  
`date` | `STRING`  
`datetime` | `DATETIME`  
`days_of_week` | `STRING`  
`day_of_week` | `INTEGER`  
`decimal` | `DOUBLE`  
`documentation_field` | `STRING`  
`document_id` | `JSON`  
`domain_id` | `JSON`  
`domain_path` | `STRING`  
`due_date` | `DATETIME`  
`dynamic_attribute_store` | `STRING`  
`email` | `STRING`  
`email_script` | `STRING`  
`expression` | `STRING`  
`external_names` | `STRING`  
`field_list` | `STRING`  
`field_name` | `STRING`  
`file_attachment` | `STRING`  
`float` | `DOUBLE`  
`formula` | `STRING`  
`geo_point` | `STRING`  
`glide_action_list` | `STRING`  
`glide_date` | `DATE`  
`glide_date_time` | `DATETIME`  
`glide_duration` | `TIME INTERVAL`  
`glide_encrypted` | `STRING`  
`glide_list` | `STRING`  
`glide_precise_time` | `DATETIME`  
`glide_time` | `DATETIME` To accurately represent the value stored in the database and account for potential timezone shifts beyond the 24-hour boundary, `glide_time` is mapped to the `DATETIME` unified type.  
`glide_utc_time` | `TIME`  
`glide_var` | `STRING`  
`glyphicon` | `STRING`  
`graphql_schema` | `STRING`  
`guid` | `STRING`  
`hash` | `STRING`  
`html` | `STRING`  
`html_script` | `STRING`  
`html_template` | `STRING`  
`icon` | `STRING`  
`image` | `STRING`  
`index_name` | `STRING`  
`insert_timestamp` | `DATETIME`  
`int` | `INTEGER`  
`integer` | `INTEGER`  
`integer_date` | `DATE`  
`integer_time` | `TIME`  
`internal_type` | `STRING`  
`ip_addr` | `STRING`  
`ip_address` | `STRING`  
`journal` | `STRING`  
`journal_input` | `STRING`  
`journal_list` | `STRING`  
`json` | `JSON`  
`json_translations` | `JSON`  
`language` | `STRING`  
`le_progress` | `STRING`  
`long` | `LONG`  
`longint` | `LONG`  
`mask_code` | `STRING`  
`metric_absolute` | `DOUBLE`  
`metric_counter` | `DOUBLE`  
`metric_derive` | `DOUBLE`  
`metric_gauge` | `DOUBLE`  
`mid_config` | `STRING`  
`month_of_year` | `INTEGER`  
`multi_small` | `STRING`  
`multi_two_lines` | `STRING`  
`name_values` | `JSON`  
`nds_icon` | `STRING`  
`nl_task_int1` | `INTEGER`  
`order_index` | `INTEGER`  
`password` | `STRING`  
`password2` | `STRING`  
`percent_complete` | `DOUBLE`  
`phone_number` | `STRING`  
`phone_number_e164` | `STRING`  
`ph_number` | `STRING`  
`price` | `DOUBLE`  
`properties` | `STRING`  
`radio` | `STRING`  
`records` | `STRING`  
`record_hierarchy_path` | `STRING`  
`reference` | `JSON`  
`reference_name` | `STRING`  
`related_tags` | `STRING`  
`reminder_field_name` | `STRING`  
`repeat_count` | `INTEGER`  
`repeat_type` | `STRING`  
`replication_payload` | `STRING`  
`schedule_date_time` | `TIMESTAMP WITH TIME ZONE`  
`schedule_interval_count` | `INTEGER`  
`script` | `STRING`  
`script_client` | `STRING`  
`script_plain` | `STRING`  
`script_server` | `STRING`  
`short_field_name` | `STRING`  
`short_table_name` | `STRING`  
`simple_name_values` | `JSON`  
`slushbucket` | `STRING`  
`snapshot_template_value` | `STRING`  
`source_id` | `JSON`  
`source_name` | `STRING`  
`source_table` | `STRING`  
`string` | `STRING`  
`string_boolean` | `STRING`  
`string_full_utf8` | `STRING`  
`structure` | `STRING`  
`sysevent_name` | `STRING`  
`sysrule_field_name` | `STRING`  
`sys_class_name` | `STRING`  
`sys_class_path` | `STRING`  
`table_name` | `STRING`  
`template_value` | `STRING`  
`timer` | `TIME INTERVAL`  
`time` | `TIME`  
`translated` | `STRING`  
`translated_field` | `STRING`  
`translated_html` | `STRING`  
`translated_text` | `STRING`  
`tree_code` | `STRING`  
`tree_path` | `STRING`  
`url` | `STRING`  
`user_image` | `STRING`  
`user_input` | `STRING`  
`user_roles` | `STRING`  
`variables` | `STRING`  
`variable_conditions` | `STRING`  
`variable_template_value` | `STRING`  
`version` | `STRING`  
`video` | `STRING`  
`week_of_month` | `INTEGER`  
`wide_text` | `STRING`  
`wiki_text` | `STRING`  
`wms_job` | `STRING`  
`workflow` | `STRING`  
`workflow_conditions` | `STRING`  
`xml` | `STRING`  
  
## MongoDB data types

Each MongoDB document is written as `JSON` unified type in Datastream. For examples of how data types are written in BigQuery, see [Configure a BigQuery destination](https://docs.cloud.google.com/datastream/docs/bq-map-data-types#mongodb-data-types).

## Microsoft Dataverse data types

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Each Microsoft Dataverse record is written as `JSON` unified type in Datastream.

## Salesforce Marketing Cloud data types

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Each Salesforce Marketing Cloud record is written as `JSON` unified type in Datastream.

## What's next

  * For more information about configuring an Oracle source, see [Configure a source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database).
  * For more information about configuring a MySQL source, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).
  * For more information about configuring a PostgreSQL source, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).
  * For more information about configuring a SQL Server source, see [Configure a source SQL Server database](https://docs.cloud.google.com/datastream/docs/configure-your-source-sql-server-database).
  * For more information about configuring a Salesforce source, see [Configure a source Salesforce org](https://docs.cloud.google.com/datastream/docs/configure-salesforce-org).
  * For more information about configuring a ServiceNow source, see [Configure a source ServiceNow instance](https://docs.cloud.google.com/datastream/docs/configure-servicenow).
  * For more information about configuring a Workday source, see [Configure a source Workday instance](https://docs.cloud.google.com/datastream/docs/configure-workday).
  * For more information about configuring a MongoDB source, see [Configure a source MongoDB database](https://docs.cloud.google.com/datastream/docs/configure-mongodb).
  * For more information about configuring a Salesforce Marketing Cloud source, see [Configure a Salesforce Marketing Cloud source](https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
