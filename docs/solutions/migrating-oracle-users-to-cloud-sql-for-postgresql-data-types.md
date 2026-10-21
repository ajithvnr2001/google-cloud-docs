---
url: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-data-types/
title: Migrating Oracle\u00ae users to Cloud SQL for PostgreSQL: Data types, users, and tables \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:30.963434+00:00
---

# Migrating Oracle® users to Cloud SQL for PostgreSQL: Data types, users, and tables  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle® users to Cloud SQL for PostgreSQL: Data types, users, and tables Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres) version 12. In addition to the [introductory setup part](https://docs.cloud.google.com/solutions/setting-up-cloud-sql-for-postgresql-for-production), the series includes the following parts:

  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Terminology and functionality](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-terminology)
  * Migrating Oracle users to Cloud SQL for PostgreSQL: Data types, users, and tables (this document)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-queries)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-security)
  * [Migrating Oracle Database users and schemas to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/solutions/migrating-oracle-database-to-cloud-sql-for-postgresql)



## Data types

Cloud SQL for PostgreSQL provides multiple data types that are fully equivalent or similar to the Oracle provided data types. The following table lists the most common [PostgreSQL data types](https://www.postgresql.org/docs/12/datatype.html), followed by a comparison between Oracle primitive data types and the corresponding Cloud SQL for PostgreSQL data types; where a data type is not supported, an alternative data type is listed.

### Cloud SQL for PostgreSQL 12 primitive data types

Cloud SQL for PostgreSQL data type family | Cloud SQL for PostgreSQL data type name | Data type specification  
---|---|---  
**String/character** | `CHAR(n)` | Stores exactly `n` characters. Alias of `CHARACTER(n)`.  
| `CHARACTER(n)` | Stores exactly `n` characters.  
| `VARCHAR(n)` | Stores a variable number of characters, up to a maximum of `n` characters. Alias of `CHARACTER VARYING(n)`.  
| `CHARACTER VARYING(n)` | Stores a variable number of characters, up to a maximum of `n` characters.  
| `TEXT` | Specific variant of `VARCHAR` that does not require you to specify an upper limit on the number of characters. The longest possible character string that could be stored is 1 GB (same for all string character data types).  
**Numeric** | `SMALLINT` | Min value is -32768 | Max value is 32767.  
| `INTEGER` | Min value is -2147483648 | Max value is 2147483647.  
| `BIGINT` | Min value is -2^63 | Max value is 2^63-1.  
| `REAL` | Single-precision floating-point number (4 bytes).  
| `DOUBLE PRECISION` | Double-precision floating-point number (8 bytes).  
| `DECIMAL (p,s)` | Able to store any value with `p` digits and `s` decimals.  
| `NUMERIC(p,s)` | Able to store any value with `p` digits and `s` decimals.  
| `SMALLSERIAL` | Auto-incrementing Integer. Min value is 1 | Max value is 32767.  
| `SERIAL` | Auto-incrementing Integer. Min value is 1 | Max value is 2147483647.  
| `BIGSERIAL` | Auto-incrementing Integer. Min value is 1 | Max value is 2^63-1.  
**Monetary** | `MONEY` | Currency amount with a fixed fractional precision. Min value is -92233720368547758.08 | Max value is +92233720368547758.07.   
**Date & time** | `DATE` | \- Values with a date part but no time part.  
\- The supported range is 4713 BC to 5874897 AD with a resolution of 1 day.  
| `TIMESTAMP (p)` | \- Values that contain both date and time parts.  
\- The supported range is 4713 BC to 294276 AD.  
\- Resolution is `p` fractional digits in seconds (or 1 microsecond if unspecified).  
| `TIMESTAMP (p) with time zone` | \- Values that contain both date, time and time zone.  
\- The supported range is 4713 BC to 294276 AD.  
\- Resolution is `p` fractional digits in seconds (or 1 microsecond if unspecified).  
| `TIME (p)` | \- Values with a time part but no date part.  
\- The supported range is 00:00:00 to 24:00:00.  
\- Resolution is `p` fractional digits in seconds (or 1 microsecond if unspecified).  
| `TIME (p) with time zone` | \- Values with a time and time zone but no date part.  
\- The supported range is 00:00:00 to 24:00:00.  
\- Resolution is `p` fractional digits in seconds (or 1 microsecond if unspecified).  
| `INTERVAL (p)` | \- Time interval  
\- The supported range is -178000000 to 178000000 years.  
\- Resolution is `p` fractional digits in seconds (or 1 microsecond if unspecified).  
**JSON** | `JSON` | Textual JSON data.  
| `JSONB` | Binary JSON data.  
**XML** | `XML` | XML data.  
  
**Geometric** | `GEOMETRY` | The column type to specify when you want to use the following data models.  
| `POINT` | An `(x,y)` value.  
| `LINE` | An `(A, B, C)` tuple where `Ax + By + C = 0` and `A` and `B` are not both 0.  
  
OR  
  
Point 1 and point 2 in the following formats:  
  
`[ ( x1 , y1 ) , ( x2 , y2 ) ]  
( ( x1 , y1 ) , ( x2 , y2 ) )  
( x1 , y1 ) , ( x2 , y2 )  
x1 , y1 , x2 , y2`  
| `LSEG` | A line segment `((x1,y1),(x2,y2))`.  
| `BOX` | Rectangular box `((x1,y1),(x2,y2))`.  
| `PATH` | A sequence of points `((x1,y1),...)`.  
| `POLYGON` | A sequence of points, effectively a closed path.  
| `CIRCLE` | `(x,y),r)` (center point and radius)  
**Logical** | `BOOLEAN` | \- Holds a true, false or null value.  
\- Accepts values such as `yes`, `true`, `t`, `on`, and `1` as true.  
**Bit / binary data** | `BIT (n)` | Fixed-length bit string.  
| `BYTEA` | Binary data / byte array.  
**Network address types** | `CIDER` | IPv4 and IPv6 networks.  
| `INET` | IPv4 and IPv6 hosts and networks.  
| `MACADDR` | MAC addresses.  
| `MACADDR8` | MAC addresses (EUI-64 format).  
**Others** | `PG_LSN` | Cloud SQL for PostgreSQL log sequence number.  
| `TSQUERY` | Text search query.  
| `TSVECTOR` | Text search document.  
| `TXID_SNAPSHOT` | User-level transaction ID snapshot.  
| `UUID` | Universally unique identifier.  
  
### Oracle to Cloud SQL for PostgreSQL data type conversion

Oracle data type family | Oracle data type name | Oracle data type specification | Cloud SQL for PostgreSQL to Oracle equivalent | Cloud SQL for PostgreSQL corresponding/alternative  
---|---|---|---|---  
**String/character** | `CHAR(n)` | Maximum size of 2000 bytes. | Yes | `CHAR(n)`  
| `CHARACTER(n)` | Maximum size of 2000 bytes. | Yes | `CHARACTER(n)`  
| `NCHAR(n)` | Maximum size of 2000 bytes. | No | `CHAR(n)`  
| `VARCHAR(n)` | Maximum size of 2000 bytes. | Yes | `VARCHAR(n)`  
| `NCHAR VARYING(n)` | Varying-length UTF-8 string Maximum size  
of 4000 bytes. | No | `CHARACTER VARYING(n)`  
| `VARCHAR2(n) 11g` | Maximum size of 4000 bytes maximum size of 32 KB in PL/SQL. | Yes* | `VARCHAR(n)`  
| `VARCHAR2(n)  
12g` | Maximum size of 32767 bytes `MAX_STRING_SIZE= EXTENDED`. | Yes* | `VARCHAR(n)`  
| `NVARCHAR2(n)` | Maximum size of 4000 bytes. | No | `VARCHAR(n)`  
| `LONG` | Maximum size of 2 GB. | Yes* | `TEXT`  
| `RAW(n)` | Maximum size of 2000 bytes. | Yes* | `BYTEA`  
| `LONG RAW` | Maximum size of 2 GB. | Yes* | `BYTEA`  
**Numeric** | `NUMBER` | Floating-point number. | Yes* | `NUMERIC(p,s)`  
| `NUMBER(*)` | Floating-point number. | Yes* | `DOUBLE PRECISION`  
| `NUMERIC(p,s)` | Precision can range from 1 to 38. | Yes | `NUMERIC(p,s)`  
| `FLOAT(p,s)` | Floating-point number. | Yes* | `DOUBLE PRECISION`  
| `DEC(p,s)` | Fixed-point number. | Yes | `DEC(p,s)`  
| `DECIMAL(p,s)` | Fixed-point number. | Yes | `DECIMAL(p,s)`  
| `INT` | 38-digit integer. | Yes | `INT`  
| `INTEGER` | 38-digit integer. | Yes | `INTEGER`  
| `SMALLINT` | 38-digit integer. | Yes | `SMALLINT`  
| `REAL` | Floating-point number. | Yes* | `DOUBLE PRECISION`  
| `DOUBLE PRECISION` | Floating-point number. | Yes | `DOUBLE PRECISION`  
**Date & time** | `DATE` | Stores date and time data (year, month, day, hour, minute and second). | Yes* | `TIMESTAMP(0)`  
| `TIMESTAMP(p)` | Date and time with fraction. | Yes | `TIMESTAMP(p)`  
| `TIMESTAMP(p) WITH TIME ZONE` | Date and time with fraction and time zone. | Yes | `TIMESTAMP (p) WITH TIME ZONE`  
| `INTERVAL YEAR(p) TO MONTH` | Date interval. | Yes* | `INTERVAL YEAR TO MONTH`  
| `INTERVAL DAY(p) TO SECOND(s)` | Day and time interval. | Yes* | `INTERVAL DAY TO SECOND(s)`  
**Logical** | `BOOLEAN` | Values `TRUE`, `FALSE`, and `NULL`. Cannot be assigned to a database table column. | Yes | `BOOLEAN`  
**XML** | `XMLTYPE` | XML data. | No | `XML`  
**LOB** | `BFILE` | Pointer to binary file, with a maximum size of 4 GB. | No | `VARCHAR(255)`  
| `CLOB` | Character large object with a maximum file size of 4GB. | No | `TEXT`  
| `BLOB` | Binary large object with a maximum size of 4 GB. | No | `BYTEA`  
| `NCLOB` | Variable-length Unicode string with a maximum file size of 4 GB. | No | `TEXT`  
**ROWID** | `ROWID` | Physical row address. | No | `CTID`  
| `UROWID(n)` | Universal row ID of the logical row addresses. | No | `CTID`  
**Spatial** | `SDO_ GEOMETRY` | The geometric description of a spatial object. | Yes | Postgres has various geometry types including `point`, `line`, `path`, `polygon`, `circle`, ....  
| `SDO_TOPO_ GEOMETRY` | Describes a topology geometry. | Yes | PostGIS, a widely used Postgres extension, provides several topology types.  
| `SDO_GEORASTER` | A raster grid or image object is stored in a single row. | Yes | PostGIS, a widely used Postgres extension, provides a tool for loading raster files into the database.  
**Media types** | `ORDDicom` | Supports the storage and management of Digital Imaging and Communications in Medicine (DICOM) files. | Yes, with workaround | Postgres provides a binary type, `bytea`, for storing large objects.  
| `ORDDoc` | Supports storage and management of any type of media data. | Yes, with workaround | Postgres provides a binary type, `bytea`, for storing large objects.  
| `ORDImage` | Supports the storage and management of image data. | Yes, with workaround | Postgres provides a binary type, `bytea`, for storing large objects.  
| `ORDVideo` | Supports the storage and management of video data. | Workaround | Postgres provides a binary type, `bytea`, for storing large objects.  
  
* The corresponding data type in Cloud SQL for PostgreSQL is mostly compatible with Oracle but carries a different name.

### User-defined types

Oracle refers to user-defined types (UDTs) as `OBJECT TYPES`, which are managed using PL/SQL. User-defined types let the user create application-dedicated, complex data types that are based on and extend from the built-in Oracle data types list.

Oracle user-defined types | Oracle overview or implementation | Cloud SQL for PostgreSQL support | Cloud SQL for PostgreSQL corresponding or alternative solution  
---|---|---|---  
**Abstract data type (ADT)** | `CREATE TYPE ADT_DEMO AS OBJECT (  
ID NUMBER(6),  
NAME VARCHAR2(20)  
);` | Partially with different syntax | Cloud SQL for PostgreSQL composite types are specified by a list of attribute names and data types:  
  
`CREATE TYPE ADT_DEMO AS  
(  
ID NUMERIC(6),  
NAME VARCHAR(20)  
);`  
**VARRAY type** | `CREATE TYPE VARRAY_DEMO AS VARRAY (5) OF VARCHAR2(25);` | No | As a workaround, Cloud SQL for PostgreSQL allows columns to be defined as array:  
  
`CREATE TABLE VARRAY_TABLE (  
NAME VARCHAR(25)[]  
);`  
**Nested table type** | `CREATE TYPE NTT_DEMO AS OBJECT (  
ID NUMBER(6),  
NAME VARCHAR2(20)  
) ;   
CREATE TYPE NTT_TABLE AS TABLE OF NTT_DEMO;` | No | As a workaround, use a combination of composite types and array column definition in Cloud SQL for PostgreSQL to achieve similar functionality as Oracle's Nested table type.  
  
`CREATE TYPE NTT_DEMO AS  
(  
ID NUMERIC(6),  
NAME VARCHAR(20)  
);   
CREATE TABLE NTT_TABLE (  
RECORD NTT_DEMO[]  
);`  
**Incomplete type** | Incomplete types are types without attributes and methods. They could be referenced by other types. However, you must provide the type definition before using it.  
  
`CREATE TYPE INCOMPLETE_DEMO;` | No | `N/A`  
  
## Users

This section discusses creating users and assigning permissions, and the necessity of converting Oracle tables into Cloud SQL for PostgreSQL tables.

### User creation and permissions

Oracle database user accounts (Oracle "user" and "schema" being identical) can be used for authenticating and connecting to database sessions, while authorization access is set at the user's individual level for specific database objects/permissions.

In general there are two types of database users:

  * **Administrators:** managing the database instance, users, and resources.
  * **User Accounts:** serving logical operations such as applications.



Administrators grant privileges to user and application user accounts in order to access the database objects. Oracle database permissions are granted to a user for specific operations (for example, create session/connect) or specific database objects (for example, `SELECT` on a specific table or `EXECUTE` on a specific stored procedure).

In Oracle, there is the concept of users and roles. Users are used to authenticate with the database and roles provide grouping of permissions which can be granted as a whole.

In Cloud SQL for PostgreSQL, users and roles are synonymous. A user in Cloud SQL for PostgreSQL is a role with `connect` permission. You can use either the `CREATE USER` or `CREATE ROLE` statement to create a database user. Unlike Oracle, in Cloud SQL for PostgreSQL, schemas and users are created separately. A schema is a collection of objects (for example, tables, data types, functions, etc.) and it's owned by a user.

Oracle Create User |   
---|---  
`CREATE USER user_name IDENTIFIED BY password;` |   
**Cloud SQL for PostgreSQL Create User** |   
`CREATE USER user WITH PASSWORD 'password';`   
  
**OR**  
  
`CREATE ROLE user WITH LOGIN PASSWORD 'password';` |   
  
### Conversion considerations

  * Users are defined at the root level and are valid for all databases contained in the same Cloud SQL for PostgreSQL cluster. This is similar to "common users" in Oracle 12c.
  * The Cloud SQL for PostgreSQL `CREATE USER` syntax is different from Oracle's and cannot be migrated as is. `CREATE USER` in Cloud SQL for PostgreSQL is an alias for `CREATE ROLE` except that the `LOGIN` option is enabled by default.



## Tables

Oracle tables are constructed from many elements such as column data types, table constraints, indexes, partitions, Oracle tables proprietary features, and more. To successfully migrate into Cloud SQL for PostgreSQL database tables, all Oracle table elements must be converted into Cloud SQL for PostgreSQL tables. Some elements are supported with no or minor modifications, while some elements must be modified completely.

From a migration perspective, converting PL/SQL into Cloud SQL for PostgreSQL probably requires more effort because converting Oracle tables into Cloud SQL for PostgreSQL tables is a crucial stage with significant importance and further implications on performance and data size.

The following are the main differences between Oracle and Cloud SQL for PostgreSQL tables and related features. These differences are discussed in the remaining parts of the series.

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



## What's next

  * Explore more about [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/users) user accounts.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
