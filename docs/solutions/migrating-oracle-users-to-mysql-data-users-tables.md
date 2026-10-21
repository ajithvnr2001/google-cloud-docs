---
url: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-data-users-tables/
title: Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:29.692514+00:00
---

# Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-data-users-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to Cloud SQL for MySQL version 5.7, second-generation instances. The series includes the following parts:

  * [Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-terminology)
  * Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables (this document)
  * [Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-queries-procedures-functions-triggers)
  * [Migrating Oracle users to Cloud SQL for MySQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-security-ops-monitoring-logging)



## Data types

MySQL provides multiple data types that are fully equivalent or similar to the Oracle provided data types. The following table lists the most common MySQL data types, followed by a comparison between Oracle primitive data types and the corresponding MySQL data types; where a data type is not supported, an alternative data type is listed. Note that a MySQL 5.7 database has a limit of [65,535 bytes](https://dev.mysql.com/doc/refman/5.7/en/column-count-limit.html#row-size-limits), for the entire row (depending on the used character set).

### MySQL 5.7 primitive data types

MySQL data type family | MySQL data type name | Data type specification  
---|---|---  
**String/**  
**character** | 
    
    
    CHAR(_n_)
    

| Stores exactly `_n_` characters.  
| 
    
    
    VARCHAR(_n_)
    

| Stores a variable number of characters, up to a maximum of `_n_` characters.  
| 
    
    
    BINARY
    

| Stores exactly `_n_` bytes.  
| 
    
    
    VARBINARY(_n_)
    

| Stores a variable number of characters, up to a maximum of `_n_` bytes.  
| 
    
    
    BLOB
    

| Binary large object that can hold a variable amount of data.  
| 
    
    
    TEXT
    

| Specific variant of `VARCHAR` that does not require you to specify an upper limit on the number of characters.  
| 
    
    
    ENUM
    

| String object with a value chosen from a list of permitted values that are enumerated explicitly in the column specification when the table is created.  
| 
    
    
    SET
    

| String object that can have zero or more values, each of which must be chosen from a list of permitted values specified when the table is created.  
**Numeric** | 
    
    
    INT
    

| Min value is -2147483648 | Max value is 2147483647.  
| 
    
    
    INTEGER
    

| Min value is -2147483648 | Max value is 2147483647.  
| 
    
    
    TINYINT
    

| Min value is -128 | Max value is 127.  
| 
    
    
    SMALLINT
    

| Min value is -32768 | Max value is 32767.  
| 
    
    
    MEDIUMINT
    

| Min value is -8388608 | Max value is 8388607.  
| 
    
    
    BIGINT
    

| Min value is -2^63 | Max value is 2^63-1.  
| 
    
    
    DECIMAL(_p_ ,_s_)
    

| Able to store any value with `_p_` digits and `_s_` decimals.  
| 
    
    
    NUMERIC(_p_ ,_s_)
    

| Able to store any value with `_p_` digits and `_s_` decimals.  
| 
    
    
    FLOAT(_m_ ,_d_)
    

| Values can be stored with up to `_m_` digits in total, of which `_d_` digits may be after the decimal point.  
| 
    
    
    DOUBLE(_m_ ,_d_)
    

| Values can be stored with up to `_m_` digits in total, of which `_d_` digits may be after the decimal point.  
| 
    
    
    BIT(_m_)
    

| Storage of `_m_`-bit values. `_m_` can range from 1 to 64.  
**Date & time** | 
    
    
    DATE
    

| \- Values with a date part but no time part.  
\- Retrieves and displays `DATE` values in `'YYYY-MM-DD'` format.  
\- The supported range is `'1000-01-01'` to `'9999-12-31'`.  
| 
    
    
    DATETIME
    

| \- Values that contain both date and time parts.  
\- Retrieves and displays `DATETIME` values in `'YYYY-MM-DD HH:MM:SS'` format.  
\- The supported range is `'1000-01-01 00:00:00'` to `'9999-`  
` 12-31 23:59:59'`.  
| 
    
    
    TIMESTAMP
    

| \- Values that contain both date and time parts.  
\- `TIMESTAMP` has a range of `'1970-01-01 00:00:01'` UTC to ` '2038-01-19 03:14:07'` UTC.  
| 
    
    
    TIME
    

| \- Values can range from `'-838:59:59'` to `'838:59:59'`.  
\- The hours part might be so large because the `TIME` type can be used not only to represent a time of day (which must be less than 24 hours), but also elapsed time or a time interval between two events (which might be much greater than 24 hours, or even negative).  
| 
    
    
    YEAR
    

| \- `YEAR` 1-byte type used to represent year values.  
\- Can be declared as `YEAR` or `YEAR(_n_)` and has a display width of `_n_` characters.  
**JSON** | 
    
    
    JSON
    

| Textual JSON data as a data type.  
  
**Spatial (Geometry)** | 
    
    
    GEOMETRY
    

| The column type to specify when you want to use the data models that follow in the rest of this table.  
| 
    
    
    POINT
    

| An `(_x_ ,_y_)` value.  
| 
    
    
    LINESTRING
    

| A line `(pt1, pt2)`.  
| 
    
    
    POLYGON
    

| A sequence of points, effectively a closed path.  
| 
    
    
    MULTIPOINT
    

| Collection of `POINT` values.  
| 
    
    
    MULTI-LINESTRING
    

| Collection of `LINE` values.  
| 
    
    
    MULTIPOLYGON
    

| Collection of `POLYGON` values.  
| 
    
    
    GEOMETRY-COLLECTION
    

| Collection of geometry data types.  
**Logical** | 
    
    
    BOOLEAN
    

| \- Holds a true or false value.  
\- Accepts values such as `TRUE`, `'1'`, and `1` as true.  
\- Uses 1 byte of storage, and can store `NULL`.  
  
### Oracle to MySQL data type conversion

Oracle data type family | Oracle data type name | Oracle data type specification | MySQL to Oracle equivalent | MySQL corresponding/alternative  
---|---|---|---|---  
**String/**  
**Character** | 
    
    
    CHAR(_n_)
    

| Maximum size of 2000 bytes. | Yes | 
    
    
    CHAR(_n_)
      
  
| 
    
    
    CHARACTER(_n_)
    

| Maximum size of 2000 bytes. | Yes | 
    
    
    CHARACTER(_n_)
      
  
| 
    
    
    NCHAR(_n_)
    

| Maximum size of 2000 bytes. | Yes | 
    
    
    NCHAR(_n_)
      
  
| 
    
    
    VARCHAR(_n_)
    

| Maximum size of 2000 bytes. | Yes | 
    
    
    VARCHAR(_n_)
      
  
| 
    
    
    NCHAR
    VARYING(_n_)
    

| Varying-length UTF-8 string Maximum size  
of 4000 bytes. | Yes | 
    
    
    NCHAR
    VARYING(_n_)
      
  
| 
    
    
    VARCHAR2(_n_)
    11g
    

| Maximum size of 4000 bytes Maximum size of 32 KB in PL/SQL. | No | 
    
    
    VARCHAR(_n_)
      
  
| 
    
    
    VARCHAR2(_n_)
    12g
    

| Maximum size of 32767 bytes `MAX_STRING_SIZE=EXTENDED`. | No | 
    
    
    VARCHAR(_n_)
      
  
| 
    
    
    NVARCHAR2(_n_)
    

| Maximum size of 4000 bytes. | No | 
    
    
    VARCHAR(_n_)
      
  
| 
    
    
    LONG
    

| Maximum size of 2 GB. | Yes | 
    
    
    LONG
      
  
| 
    
    
    RAW(_n_)
    

| Maximum size of 2000 bytes. | No | 
    
    
    VARBINARY(_n_)
      
  
| 
    
    
    LONG RAW
    

| Maximum size of 2 GB. | No | 
    
    
    LONGTEXT
      
  
**Numeric** | 
    
    
    NUMBER
    

| Floating-point number. | No | 
    
    
    NUMERIC/DECIMAL(_p_ ,_s_)
      
  
**Numeric** | 
    
    
    NUMBER
    

| Floating-point number. | No | 
    
    
    NUMERIC/DECIMAL(_p_ ,_s_)
      
  
| 
    
    
    NUMBER(*)
    

| Floating-point number. | No | 
    
    
    DOUBLE
      
  
| 
    
    
    NUMERIC(_p_ ,_s_)
    

| Precision can range from 1 to 38. | Yes | 
    
    
    NUMERIC(_p_ ,_s_)
      
  
| 
    
    
    FLOAT(_p_)
    

| Floating-point number. | Yes | 
    
    
    FLOAT(_p_)
      
  
| 
    
    
    DEC(_p_ ,_s_)
    

| Fixed-point number. | Yes | 
    
    
    DEC(_p_ ,_s_)
      
  
| 
    
    
    DECIMAL(_p_ ,_s_)
    

| Fixed-point number. | Yes | 
    
    
    DECIMAL(_p_ ,_s_)
      
  
| 
    
    
    INT
    

| 38-digit integer. | Yes | 
    
    
    INT
      
  
| 
    
    
    INTEGER
    

| 38-digit integer. | Yes | 
    
    
    INTEGER
      
  
| 
    
    
    SMALLINT
    

| 38-digit integer. | Yes | 
    
    
    SMALLINT
      
  
| 
    
    
    REAL
    

| Floating-point number. | Yes | 
    
    
    REAL
      
  
| 
    
    
    DOUBLE PRECISION
    

| Floating-point number. | Yes | 
    
    
    DOUBLE PRECISION
      
  
**Date & Time** | 
    
    
    DATE
    

| Stores date and time data (year, month, day, hour, minute, and second). | Yes | 
    
    
    DATE
      
  
| 
    
    
    TIMESTAMP(_p_)
    

| Date and time with fraction. | Yes | 
    
    
    TIMESTAMP
      
  
| 
    
    
    TIMESTAMP(_p_)
    WITH TIME ZONE
    

| Date and time with fraction and time zone. | No | 
    
    
    DATETIME(_n_)
      
  
| 
    
    
    INTERVAL
    YEAR(_p_)
    TO MONTH
    

| Date interval. | No | 
    
    
    VARCHAR(_n_)
      
  
| 
    
    
    INTERVAL
    DAY(_p_)
    TO SECOND(_s_)
    

| Day and time interval. | No | 
    
    
    VARCHAR(_n_)
      
  
**Logical** | 
    
    
    BOOLEAN
    

| Values `TRUE`, `FALSE`, and `NULL`. Cannot be assigned to a database table column. | Yes | 
    
    
    BOOLEAN
      
  
**XML** | 
    
    
    XMLTYPE
    

| XML data. | No | 
    
    
    LONGTEXT
      
  
**LOB** | 
    
    
    BFILE
    

| Pointer to binary file, with a maximum size of 4 GB. | No | 
    
    
    VARCHAR(255)
      
  
| 
    
    
    CLOB
    

| Character large object with a maximum file size of 4 GB. | No | 
    
    
    LONGTEXT
      
  
| 
    
    
    BLOB
    

| Binary large object with a maximum size of 4 GB. | Yes | 
    
    
    BLOB
      
  
| 
    
    
    NCLOB
    

| Variable-length Unicode string with a maximum file size of 4 GB. | No | 
    
    
    LONGTEXT
      
  
**ROWID** | 
    
    
    ROWID
    

| Physical row address. | No | 
    
    
    CHAR(_n_)
      
  
| 
    
    
    UROWID(_n_)
    

| Universal row ID of the logical row addresses. | No | 
    
    
    VARCHAR(_n_)
      
  
**Spatial** | 
    
    
    SDO_GEOMETRY
    

| The geometric description of a spatial object. | No | 
    
    
    N/A
      
  
| 
    
    
    SDO_TOPO_GEOMETRY
    

| Describes a topology geometry. | No | 
    
    
    N/A
      
  
| 
    
    
    SDO_GEORASTER
    

| A raster grid or image object is stored in a single row. | No | 
    
    
    N/A
      
  
**Media types** | 
    
    
    ORDDicom
    

| Supports the storage and management of audio data. | No | 
    
    
    N/A
      
  
| 
    
    
    ORDDicom
    

| Supports the storage and management of Digital Imaging and Communications in Medicine (DICOM). | No | 
    
    
    N/A
      
  
| 
    
    
    ORDDoc
    

| Supports storage and management of any type of media data. | No | 
    
    
    N/A
      
  
| 
    
    
    ORDImage
    

| Supports the storage and management of image data. | No | 
    
    
    N/A
      
  
| 
    
    
    ORDVideo
    

| Supports the storage and management of video data. | No | 
    
    
    N/A
      
  
### User-defined types

Oracle refers to user-defined types (UDTs) as `OBJECT TYPES`, which are managed using PL/SQL. User-defined types let the user create application-dedicated, complex data types that are based on and extend from the built-in Oracle data types list.

Here's an Oracle example of UDT:
    
    
    SQL> CREATE OR REPLACE TYPE EMP_PHONE_NUM AS OBJECT (
         PHONE_NUM VARCHAR2(11));
    

**Conversion notes**

MySQL does not allow users to create dedicated, defined types.

## Users and tables

This section discusses creating users and assigning them permissions, and the necessity of converting Oracle tables into Cloud SQL for MySQL tables.

### User creation and permissions

Oracle database user accounts (Oracle "user" and "schema" are identical) can be used for authenticating and connecting to database sessions, while authorization access is set at each user's individual level for specific database objects and permissions.

In general, there are two types of database users:

  * **Administrators:** managing the database instance, users, and resources.
  * **User Accounts:** serving logical operations such as applications.



Administrators grant privileges to user and application user accounts in order to access the database objects. Oracle database permissions are granted to a user for specific operations (for example, create session/connect) or specific database objects (for example, `SELECT` on a specific table or `EXECUTE` on a specific stored procedure).

### Conversion considerations

  * The MySQL `CREATE USER` syntax is different from Oracle's and cannot be migrated as is. Also, both databases have different user architecture.
  * When an admin creates a user in MySQL, they must specify the server that the user needs to connect to for database access. The server can be either a specific IP address or DNS, or it's allowed to connect from all sources by using the wildcard % sign).
  * Because the MySQL user name is a two-part attachment between the user name and the server from which the user would be allowed to connect from, a user can be created with the same name but from a different server as the client address (IP/DNS).
  * Once the user is created, it can be granted permission to database objects that are a part of a specific database or schema.
  * Users can also be granted additional permissions according to [Cloud SQL for MySQL allowed permissions](https://docs.cloud.google.com/sql/docs/mysql/users) (for example, the root user will have all privileges except for the [`SUPER`](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_super) and [`FILE`](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_file) privileges). Oracle users can be attached to a dedicated tablespace while in MySQL, so this functionality is not relevant.



### Tables

Oracle tables are constructed from many elements such as column data types, table constraints, indexes, partitions, Oracle tables proprietary features, and more. To successfully migrate into Cloud SQL for MySQL database tables, all Oracle table elements must be converted into MySQL tables. Some elements are supported with no or minor modifications, while some elements must be modified completely.

From a migration perspective, converting PL/SQL into MySQL probably requires more effort because converting Oracle tables into MySQL tables is a crucial stage with significant importance and further implications on performance and data size.

The following are the main differences between Oracle and MySQL tables and related features. These differences are discussed in the remaining parts of the series.

  * Case sensitivity (table and column names)
  * Create table syntax
  * Table and index metadata
  * Constraints support
  * Data types support and limitations
  * Indexes
  * Partitions and partitions management
  * Table and index maintenance
  * Temporary tables
  * Views
  * Visible and invisible columns (Oracle 12c)
  * Table and column character sets



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
