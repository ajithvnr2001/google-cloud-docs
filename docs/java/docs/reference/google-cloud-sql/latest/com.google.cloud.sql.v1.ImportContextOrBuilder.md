---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContextOrBuilder
title: Interface ImportContextOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:31.146974+00:00
---

# Interface ImportContextOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContextOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportContextOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface ImportContextOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBakImportOptions()
    
    
    public abstract ImportContext.SqlBakImportOptions getBakImportOptions()

Import parameters specific to SQL Server .BAK files

`.google.cloud.sql.v1.ImportContext.SqlBakImportOptions bak_import_options = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlBakImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlBakImportOptions)` | The bakImportOptions.  
  
### getBakImportOptionsOrBuilder()
    
    
    public abstract ImportContext.SqlBakImportOptionsOrBuilder getBakImportOptionsOrBuilder()

Import parameters specific to SQL Server .BAK files

`.google.cloud.sql.v1.ImportContext.SqlBakImportOptions bak_import_options = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlBakImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlBakImportOptionsOrBuilder)` |   
  
### getCsvImportOptions()
    
    
    public abstract ImportContext.SqlCsvImportOptions getCsvImportOptions()

Options for importing data as CSV.

`.google.cloud.sql.v1.ImportContext.SqlCsvImportOptions csv_import_options = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlCsvImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlCsvImportOptions)` | The csvImportOptions.  
  
### getCsvImportOptionsOrBuilder()
    
    
    public abstract ImportContext.SqlCsvImportOptionsOrBuilder getCsvImportOptionsOrBuilder()

Options for importing data as CSV.

`.google.cloud.sql.v1.ImportContext.SqlCsvImportOptions csv_import_options = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlCsvImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlCsvImportOptionsOrBuilder)` |   
  
### getDatabase()
    
    
    public abstract String getDatabase()

The target database for the import. If `fileType` is `SQL`, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. For entire instance parallel import operations, the database is overridden by the database name stored in subdirectory name. If `fileType` is `CSV`, one database must be specified.

`string database = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The database.  
  
### getDatabaseBytes()
    
    
    public abstract ByteString getDatabaseBytes()

The target database for the import. If `fileType` is `SQL`, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. For entire instance parallel import operations, the database is overridden by the database name stored in subdirectory name. If `fileType` is `CSV`, one database must be specified.

`string database = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for database.  
  
### getFileType()
    
    
    public abstract SqlFileType getFileType()

The file type for the specified uri.\`SQL`: The file contains SQL statements. \`CSV`: The file contains CSV data.

`.google.cloud.sql.v1.SqlFileType file_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SqlFileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFileType)` | The fileType.  
  
### getFileTypeValue()
    
    
    public abstract int getFileTypeValue()

The file type for the specified uri.\`SQL`: The file contains SQL statements. \`CSV`: The file contains CSV data.

`.google.cloud.sql.v1.SqlFileType file_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for fileType.  
  
### getImportUser()
    
    
    public abstract String getImportUser()

The PostgreSQL user for this import operation. PostgreSQL instances only.

`string import_user = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The importUser.  
  
### getImportUserBytes()
    
    
    public abstract ByteString getImportUserBytes()

The PostgreSQL user for this import operation. PostgreSQL instances only.

`string import_user = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for importUser.  
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#importContext`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#importContext`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getSqlImportOptions()
    
    
    public abstract ImportContext.SqlImportOptions getSqlImportOptions()

Optional. Options for importing data from SQL statements.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions sql_import_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptions)` | The sqlImportOptions.  
  
### getSqlImportOptionsOrBuilder()
    
    
    public abstract ImportContext.SqlImportOptionsOrBuilder getSqlImportOptionsOrBuilder()

Optional. Options for importing data from SQL statements.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions sql_import_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlImportOptionsOrBuilder)` |   
  
### getTdeImportOptions()
    
    
    public abstract ImportContext.SqlTdeImportOptions getTdeImportOptions()

Optional. Import parameters specific to SQL Server TDE certificates

` .google.cloud.sql.v1.ImportContext.SqlTdeImportOptions tde_import_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlTdeImportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlTdeImportOptions)` | The tdeImportOptions.  
  
### getTdeImportOptionsOrBuilder()
    
    
    public abstract ImportContext.SqlTdeImportOptionsOrBuilder getTdeImportOptionsOrBuilder()

Optional. Import parameters specific to SQL Server TDE certificates

` .google.cloud.sql.v1.ImportContext.SqlTdeImportOptions tde_import_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ImportContext.SqlTdeImportOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ImportContext.SqlTdeImportOptionsOrBuilder)` |   
  
### getUri()
    
    
    public abstract String getUri()

Path to the import file in Cloud Storage, in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are supported when `fileType` is `SQL`. The instance must have write permissions to the bucket and read access to the file.

`string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Path to the import file in Cloud Storage, in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are supported when `fileType` is `SQL`. The instance must have write permissions to the bucket and read access to the file.

`string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasBakImportOptions()
    
    
    public abstract boolean hasBakImportOptions()

Import parameters specific to SQL Server .BAK files

`.google.cloud.sql.v1.ImportContext.SqlBakImportOptions bak_import_options = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bakImportOptions field is set.  
  
### hasCsvImportOptions()
    
    
    public abstract boolean hasCsvImportOptions()

Options for importing data as CSV.

`.google.cloud.sql.v1.ImportContext.SqlCsvImportOptions csv_import_options = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the csvImportOptions field is set.  
  
### hasSqlImportOptions()
    
    
    public abstract boolean hasSqlImportOptions()

Optional. Options for importing data from SQL statements.

` .google.cloud.sql.v1.ImportContext.SqlImportOptions sql_import_options = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlImportOptions field is set.  
  
### hasTdeImportOptions()
    
    
    public abstract boolean hasTdeImportOptions()

Optional. Import parameters specific to SQL Server TDE certificates

` .google.cloud.sql.v1.ImportContext.SqlTdeImportOptions tde_import_options = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tdeImportOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
