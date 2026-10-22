---
url: https://docs.cloud.google.com/datastream/docs/bq-map-data-types/
title: Data type mappings in BigQuery \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:18.370777+00:00
---

# Data type mappings in BigQuery  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/bq-map-data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Data type mappings in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

Datastream automatically converts data types from supported sources into compatible BigQuery data types. Understanding these mappings helps you plan destination schemas, work with MongoDB binary JSON (BSON) documents in BigQuery, and query PostgreSQL arrays as a BigQuery `ARRAY` data type.

## Map data types

The following table lists data type conversions from supported source databases to the BigQuery destination.

All sourcesMySQLOraclePostgreSQLSpanner (GoogleSQL)Spanner (PostgreSQL)SQL ServerSalesforce

Source database | Source data type | BigQuery data type  
---|---|---  
MySQL | `BIGINT(size)` | `INT64`  
MySQL | `BIGINT (unsigned)` | `DECIMAL`  
MySQL | `BINARY(size)` | `STRING (hex encoded)`  
MySQL | `BIT(size)` | `INT64`  
MySQL | `BLOB(size)` | `STRING (hex encoded)`  
MySQL | `BOOL` | `INT64`  
MySQL | `CHAR(size)` | `STRING`  
MySQL | `DATE` | `DATE`  
MySQL | `DATETIME(fsp)` | `DATETIME`  
MySQL | `DECIMAL(precision, scale)` | If the precision value is ≤ 38 and the scale value is ≤ 9, then `NUMERIC`. Otherwise, `BIGNUMERIC`.  
MySQL | `DOUBLE(size, d)` | `FLOAT64`  
MySQL | `ENUM(val1, val2, val3, ...)` | `STRING`  
MySQL | `FLOAT(precision)` | `FLOAT64`  
MySQL | `FLOAT(size, d)` | `FLOAT64`  
MySQL | `INTEGER(size)` | `INT64`  
MySQL | `INTEGER (unsigned)` | `INT64`  
MySQL | `JSON` | `JSON` `BOOLEAN`, `NUMBER`, `OBJECT`, `STRING`, `ARRAY`, and `NULL` data types are supported.  
MySQL | `LONGBLOB` | `STRING (hex encoded)`  
MySQL | `LONGTEXT` | `STRING`  
MySQL | `MEDIUMBLOB` | `STRING (hex encoded)`  
MySQL | `MEDIUMINT(size)` | `INT64`  
MySQL | `MEDIUMTEXT` | `STRING`  
MySQL | `SET(val1, val2, val3, ...)` | `STRING`  
MySQL | `SMALLINT(size)` | `INT64`  
MySQL | `TEXT(size)` | `STRING`  
MySQL | `TIME(fsp)` | `INTERVAL`  
MySQL | `TIMESTAMP(fsp)` | `TIMESTAMP`  
MySQL | `TINYBLOB` | `STRING (hex encoded)`  
MySQL | `TINYINT(size)` | `INT64`  
MySQL | `TINYTEXT` | `STRING`  
MySQL | `VARBINARY(size)` | `STRING (hex encoded)`  
MySQL | `VARCHAR` | `STRING`  
MySQL | `YEAR` | `INT64`  
Oracle | `ANYDATA` | `UNSUPPORTED`  
Oracle | `BFILE` | `UNSUPPORTED`  
Oracle | `BINARY DOUBLE` | `FLOAT64`  
Oracle | `BINARY FLOAT` | `FLOAT64`  
Oracle | `BLOB` | `BYTES`  
Oracle | `CHAR` | `STRING`  
Oracle | `CLOB` | `STRING`  
Oracle | `DATE` | `DATETIME` Zero dates aren't supported and are replaced with `NULL` values.  
Oracle | `DOUBLE PRECISION` | `FLOAT64`  
Oracle | `FLOAT(p)` | `FLOAT64`  
Oracle | `INTERVAL DAY TO SECOND` | `UNSUPPORTED`  
Oracle | `INTERVAL YEAR TO MONTH` | `UNSUPPORTED`  
Oracle | `LONG` or `LONG RAW` | `UNSUPPORTED`  
Oracle | `NCHAR` | `STRING`  
Oracle | `NCLOB` | `STRING`  
Oracle | `NUMBER` | `STRING`  
Oracle |  `NUMBER(precision=*)` | `STRING`  
Oracle |  `NUMBER(precision, scale<=0)` | If precision ≤ 18, then `INT64`. If 18 < precision ≤ 78, then map to [parameterized decimal types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#parameterized_decimal_type). If precision ≥ 79, map to `STRING`.  
Oracle | `NUMBER(precision, scale>0)` | If 0 < precision ≤ 78, then map to [parameterized decimal types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#parameterized_decimal_type). If precision ≥ 79, map to `STRING`.  
Oracle | `NVARCHAR2` | `STRING`  
Oracle | `RAW` | `STRING`  
Oracle | `ROWID` | `STRING`  
Oracle | `SDO_GEOMETRY` | `UNSUPPORTED`  
Oracle | `SMALLINT` | `INT64`  
Oracle | `TIMESTAMP` | `TIMESTAMP` Zero dates aren't supported and are replaced with `NULL` values.  
Oracle | `TIMESTAMP WITH TIME ZONE` | `TIMESTAMP` Zero dates aren't supported and are replaced with `NULL` values.  
Oracle | `UDT (user-defined type)` | `UNSUPPORTED`  
Oracle | `UROWID` | `UNSUPPORTED`  
Oracle | `VARCHAR` | `STRING`  
Oracle | `VARCHAR2` | `STRING`  
Oracle | `XMLTYPE` | `UNSUPPORTED`  
PostgreSQL | `ARRAY` | `JSON` Arrays of `DATE`, `TIMESTAMP`, or `TIMESTAMP WITH TIME ZONE` data types aren't supported.  
PostgreSQL | `BIGINT` | `INT64`  
PostgreSQL | `BIT` | `BYTES`  
PostgreSQL | `BIT VARYING` | `BYTES`  
PostgreSQL | `BOOLEAN` | `BOOLEAN`  
PostgreSQL | `BOX` | `UNSUPPORTED`  
PostgreSQL | `BYTEA` | `BYTES`  
PostgreSQL | `CHARACTER` | `STRING`  
PostgreSQL | `CHARACTER VARYING` | `STRING`  
PostgreSQL | `CIDR` | `STRING`  
PostgreSQL | `CIRCLE` | `UNSUPPORTED`  
PostgreSQL | `DATE` | `DATE`  
PostgreSQL | `DOUBLE PRECISION` | `FLOAT64`  
PostgreSQL | `ENUM` | `STRING`  
PostgreSQL | `INET` | `STRING`  
PostgreSQL | `INTEGER` | `INT64`  
PostgreSQL | `INTERVAL` | `INTERVAL`  
PostgreSQL | `JSON` | `JSON`  
PostgreSQL | `JSONB` | `JSON`  
PostgreSQL | `LINE` | `UNSUPPORTED`  
PostgreSQL | `LSEG` | `UNSUPPORTED`  
PostgreSQL | `MACADDR` | `STRING`  
PostgreSQL | `MONEY` | `FLOAT64`  
PostgreSQL | `NUMERIC` | If precision = `-1`, then `STRING` (BigQuery `NUMERIC` types require fixed precision). Otherwise, `BIGNUMERIC` or `NUMERIC`. For more information, see the [Arbitrary precision numbers](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL) section in the PostgreSQL documentation.  
PostgreSQL | `OID` | `INT64`  
PostgreSQL | `PATH` | `UNSUPPORTED`  
PostgreSQL | `POINT` | `UNSUPPORTED`  
PostgreSQL | `POLYGON` | `UNSUPPORTED`  
PostgreSQL | `REAL` | `FLOAT64`  
PostgreSQL | `SMALLINT` | `INT64`  
PostgreSQL | `SMALLSERIAL` | `INT64`  
PostgreSQL | `SERIAL` | `INT64`  
PostgreSQL | `TEXT` | `STRING`  
PostgreSQL | `TIME` | `TIME`  
PostgreSQL | `TIMESTAMP` | `TIMESTAMP`  
PostgreSQL | `TIMESTAMP WITH TIME ZONE` | `TIMESTAMP`  
PostgreSQL | `TIME WITH TIME ZONE` | `TIME`  
PostgreSQL | `TSQUERY` | `STRING`  
PostgreSQL | `TSVECTOR` | `STRING`  
PostgreSQL | `TXID SNAPSHOT` | `STRING`  
PostgreSQL | `UUID` | `STRING`  
PostgreSQL | `XML` | `STRING`  
SQL Server | `BIGINT` | `INT64`  
SQL Server | `BINARY` | `BYTES`  
SQL Server | `BIT` | `BOOL`  
SQL Server | `CHAR` | `STRING`  
SQL Server | `DATE` | `DATE`  
SQL Server | `DATETIME2` | `DATETIME`  
SQL Server | `DATETIME` | `DATETIME`  
SQL Server | `DATETIMEOFFSET` | `TIMESTAMP`  
SQL Server | `DECIMAL` | If the scale value is ≤ 9 and the `(precision - scale)` value is ≤ 29, then `NUMERIC`. Otherwise, `BIGNUMERIC`.  
SQL Server | `FLOAT` | `FLOAT64`  
SQL Server | `GEOGRAPHY` | `STRUCT` Contains the following nested fields: `value` (`BYTES` in Well-Known Binary format), `srid` (`INT64`), and `type` (`STRING`).  
SQL Server | `GEOMETRY` | `STRUCT` Contains the following nested fields: `value` (`BYTES` in Well-Known Binary format), `srid` (`INT64`), and `type` (`STRING`).  
SQL Server | `IMAGE` | `BYTES`  
SQL Server | `INT` | `INT64`  
SQL Server | `MONEY` | `NUMERIC`  
SQL Server | `NCHAR` | `STRING`  
SQL Server | `NTEXT` | `STRING`  
SQL Server | `NUMERIC` | If the scale value is ≤ 9 and the `(precision - scale)` value is ≤ 29, then `NUMERIC`. Otherwise, `BIGNUMERIC`.  
SQL Server | `NVARCHAR` | `STRING`  
SQL Server | `NVARCHAR(MAX)` | `STRING`  
SQL Server | `REAL` | `FLOAT64`  
SQL Server | `SMALLDATETIME` | `DATETIME`  
SQL Server | `SMALLINT` | `INT64`  
SQL Server | `SMALLMONEY` | `NUMERIC`  
SQL Server | `TEXT` | `STRING`  
SQL Server | `TIME` | `TIME`  
SQL Server | `TIMESTAMP` or `ROWVERSION` | `BYTES`  
SQL Server | `TINYINT` | `INT64`  
SQL Server | `UNIQUEIDENTIFIER` | `STRING`  
SQL Server | `VARBINARY` | `BYTES`  
SQL Server | `VARBINARY(MAX)` | `BYTES`  
SQL Server | `VARCHAR` | `STRING`  
SQL Server | `VARCHAR(MAX)` | `STRING`  
SQL Server | `XML` | `STRING`  
Salesforce | `BOOLEAN` | `BOOLEAN`  
Salesforce | `BYTE` | `BYTES`  
Salesforce | `DATE` | `DATE`  
Salesforce | `DATETIME` | `DATETIME`  
Salesforce | `DOUBLE` | `BIGNUMERIC`  
Salesforce | `INT` | `INT64`  
Salesforce | `STRING` | `STRING`  
Salesforce | `TIME` | `TIME`  
Salesforce | `ANYTYPE`  
(can be either `STRING`, `DATE`, `NUMBER`, or `BOOLEAN`) | `STRING`  
Salesforce | `COMBOBOX` | `STRING`  
Salesforce | `CURRENCY` | `FLOAT64` Maximum allowed length is 18 digits.  
Salesforce | `DATACATEGORYGROUPREFERENCE` | `STRING`  
Salesforce | `EMAIL` | `STRING`  
Salesforce | `ENCRYPTEDSTRING` | `STRING`  
Salesforce | `ID` | `STRING`  
Salesforce | `JUNCTIONIDLIST` | `STRING`  
Salesforce | `MASTERRECORD` | `STRING`  
Salesforce | `MULTIPICKLIST` | `STRING`  
Salesforce | `PERCENT` | `FLOAT64` Maximum allowed length is 18 digits.  
Salesforce | `PHONE` | `STRING`  
Salesforce | `PICKLIST` | `STRING`  
Salesforce | `REFERENCE` | `STRING`  
Salesforce | `TEXTAREA` | `STRING` Maximum allowed length is 255 characters.  
Salesforce | `URL` | `STRING`  
Spanner (GoogleSQL) | `ARRAY` | `JSON`  
Spanner (GoogleSQL) | `BOOL` | `BOOLEAN`  
Spanner (GoogleSQL) | `BYTES` | `BYTES`  
Spanner (GoogleSQL) | `DATE` | `DATE`  
Spanner (GoogleSQL) | `FLOAT32` | `FLOAT64`  
Spanner (GoogleSQL) | `FLOAT64` | `FLOAT64`  
Spanner (GoogleSQL) | `INT64` | `INT64`  
Spanner (GoogleSQL) | `JSON` | `JSON`  
Spanner (GoogleSQL) | `NUMERIC` | `STRING`  
Spanner (GoogleSQL) | `STRING` | `STRING`  
Spanner (GoogleSQL) | `TIMESTAMP` | `TIMESTAMP WITH TIME ZONE`  
Spanner (GoogleSQL) | `UUID` | `STRING`  
Spanner (GoogleSQL) | `PROTO` | `UNSUPPORTED`  
Spanner (GoogleSQL) | `ENUM` | `UNSUPPORTED`  
Spanner (PostgreSQL) | `ARRAY` | `JSON`  
Spanner (PostgreSQL) | `BIGINT` | `INT64`  
Spanner (PostgreSQL) | `BOOL` | `BOOLEAN`  
Spanner (PostgreSQL) | `BYTEA` | `BYTES`  
Spanner (PostgreSQL) | `DATE` | `DATE`  
Spanner (PostgreSQL) | `DECIMAL` | `STRING`  
Spanner (PostgreSQL) | `DOUBLE PRECISION` | `FLOAT64`  
Spanner (PostgreSQL) | `FLOAT8` | `FLOAT64`  
Spanner (PostgreSQL) | `INT8` | `INT64`  
Spanner (PostgreSQL) | `JSONB` | `JSON`  
Spanner (PostgreSQL) | `NUMERIC` | `STRING`  
Spanner (PostgreSQL) | `TIMESTAMP WITH TIME ZONE` | `TIMESTAMP WITH TIME ZONE`  
Spanner (PostgreSQL) | `TIMESTAMPZ` | `TIMESTAMP WITH TIME ZONE`  
Spanner (PostgreSQL) | `UUID` | `STRING`  
Spanner (PostgreSQL) | `VARCHAR` | `STRING`  
  
### MongoDB data types

MongoDB binary JSON (BSON) documents are written to BigQuery in one of two modes, depending on what you specify during stream creation (see [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams#createastream-mongodb-strict)): Canonical mode (default) or Strict mode.

  * Canonical mode (default): the modern, more descriptive format that prioritizes data fidelity. It ensures that every BSON type is explicitly labeled, for example, that it distinguishes between a 32-bit and 64-bit integer, to prevent loss of precision during data exchange. Canonical mode might be slightly slower than strict mode, but it supports all data types. For more information, see [MongoDB Extended JSON](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json/).
  * Strict mode: a legacy format designed to be compatible with JSON parsers, using specific conventions, such as `"$date"`, to represent types that don't exist in standard JSON. Certain data types, such as `Infinity`, `-Infinity`, and `NaN`, aren't supported. For more information, see [MongoDB Extended JSON (v1)](https://www.mongodb.com/docs/manual/reference/mongodb-extended-json-v1/#mongodb-extended-json--v1-).



The following table shows how data types are represented in BigQuery in both modes, along with example values:

BSON data type | Example value | Canonical mode | Strict mode  
---|---|---|---  
`DOUBLE` | `3.1415926535` | `{"$numberDouble":"3.1415926535"}` | `3.1415926535`  
`Infinity` | `Infinity` | `{"$numberDouble":"Infinity"}` | Unsupported  
`-Infinity` | `-Infinity` | `{"$numberDouble":"-Infinity"}` | Unsupported  
`NaN` | `NaN` | `{"$numberDouble":"NaN"}` | Unsupported  
`STRING` | `"Hello, MongoDB!"` | `"Hello, MongoDB!"` | `"Hello, MongoDB!"`  
`ARRAY` |  `
    
    
    [
      "item1",
      123,
      true,
      { subItem: "object in array" }
    ]
            

` |  `["item1",{"$numberInt":"123"},true,{"subItem":"object in array"}]` | `["item1",123,true,{"subItem":"object in array"}]`  
`BINARY DATA` | `new BinData(0, "SGVsbG8gQmluYXJ5IERhdGE=")` |  `{"$binary":{"base64":"SGVsbG8gQmluYXJ5IERhdGE=","subType":"00"}}` | `{"$binary":"SGVsbG8gQmluYXJ5IERhdGE=","$type":"00"}`  
`BOOLEAN` | `true` | `true` | `true`  
`DATE` | `2024-12-25T10:30:00.000+00:00` | `{"$date":{"$numberLong":"1735122600000"}}` | `{"$date": 1735122600000}`  
`NULL` | `null` | `null` | `null`  
`REGEX` | `/^mongo(db)?$/i` |  `{"$regularExpression":{"pattern":"^mongo(db)?$","options":"i"}}` | `{"$options":"i","$regex":"^mongo(db)?$"}`  
`JAVASCRIPT` | `function() {return this.stringField.length;}` |  `{"$code":"function() {\n return this.stringField.length;\n }"}` |  `{"$code":"function() {\n return this.stringField.length;\n }"}`  
`DECIMAL128` | `NumberDecimal("1234567890.1234567890")` | `{"$numberDecimal":"1234567890.1234567890"}` | `{"$numberDecimal":"1234567890.1234567890"}`  
`OBJECTID` | `ObjectId('673c5d8dbfe2e51808cc2c3d')` | `{"$oid": "673c5d8dbfe2e51808cc2c3d"}` | `{"$oid": "673c5d8dbfe2e51808cc2c3d"}`  
`LONG` | `3567587327` | `{"$numberLong": "3567587327"}` | `{"$numberLong": "3567587327"}`  
`INT32` | `42` | `{"$numberInt": "42"}` | `42`  
`INT64` | `1864712049423024127` | `{"$numberLong": "1864712049423024127"}` | `{"$numberLong": "1864712049423024127"}`  
`TIMESTAMP` | `new Timestamp(1747888877, 1)` | `{"$timestamp":{"t":1747888877,"i":1}}` | `{"$timestamp":{"i":1,"t":1747888877}}`  
  
## Query a PostgreSQL array as a BigQuery array data type

To query a PostgreSQL array as a [BigQuery `ARRAY` data type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type), convert the `JSON` values to a BigQuery array by using the BigQuery [`JSON_VALUE_ARRAY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_value_array) function:
    
    
      SELECT
        ARRAY(
          SELECT CAST(element AS TYPE)
          FROM UNNEST(JSON_VALUE_ARRAY(BQ_COLUMN_NAME, '$')) AS element
        ) AS array_col
      

Replace the following:

  * TYPE: the BigQuery type that matches the element type in the PostgreSQL source array. For example, if the source type is an array of `BIGINT` values, then replace TYPE with `INT64`. For more information about how to map the data types, see Map data types.
  * BQ_COLUMN_NAME: the name of the relevant column in the BigQuery table.



There are two exceptions to the way that you convert the values:

  * For arrays of `BIT`, `BIT_VARYING`, or `BYTEA` values in the source column, run the following query:
        
        SELECT
          ARRAY(
            SELECT FROM_BASE64(element)
            FROM UNNEST(JSON_VALUE_ARRAY(BQ_COLUMN_NAME, '$')) AS element
          ) AS array_of_bytes

  * For arrays of `JSON` or `JSONB` values in the source column, use the [`JSON_QUERY_ARRAY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_query_array) function:
        
        SELECT
          ARRAY(
            SELECT element
            FROM UNNEST(JSON_QUERY_ARRAY(BQ_COLUMN_NAME, '$')) AS element
          ) AS array_of_jsons




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
