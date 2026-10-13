---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseOrBuilder
title: Interface DatabaseOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:01.083260+00:00
---

# Interface DatabaseOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DatabaseOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface DatabaseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCharset()
    
    
    public abstract String getCharset()

The Cloud SQL charset value.

`string charset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The charset.  
  
### getCharsetBytes()
    
    
    public abstract ByteString getCharsetBytes()

The Cloud SQL charset value.

`string charset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for charset.  
  
### getCollation()
    
    
    public abstract String getCollation()

The Cloud SQL collation value.

`string collation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The collation.  
  
### getCollationBytes()
    
    
    public abstract ByteString getCollationBytes()

The Cloud SQL collation value.

`string collation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for collation.  
  
### getDatabaseDetailsCase()
    
    
    public abstract Database.DatabaseDetailsCase getDatabaseDetailsCase()

**Returns**  
---  
**Type** | **Description**  
`[Database.DatabaseDetailsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Database.DatabaseDetailsCase)` |   
  
### getEtag()
    
    
    public abstract String getEtag()

This field is deprecated and will be removed from a future version of the API.

`string etag = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

This field is deprecated and will be removed from a future version of the API.

`string etag = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getInstance()
    
    
    public abstract String getInstance()

The name of the Cloud SQL instance. This does not include the project ID.

`string instance = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instance.  
  
### getInstanceBytes()
    
    
    public abstract ByteString getInstanceBytes()

The name of the Cloud SQL instance. This does not include the project ID.

`string instance = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instance.  
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#database`.

`string kind = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#database`.

`string kind = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public abstract String getName()

The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.

`string name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.

`string name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProject()
    
    
    public abstract String getProject()

The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.

`string project = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The project.  
  
### getProjectBytes()
    
    
    public abstract ByteString getProjectBytes()

The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.

`string project = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for project.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

The URI of this resource.

`string self_link = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

The URI of this resource.

`string self_link = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getSqlserverDatabaseDetails()
    
    
    public abstract SqlServerDatabaseDetails getSqlserverDatabaseDetails()

`.google.cloud.sql.v1beta4.SqlServerDatabaseDetails sqlserver_database_details = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerDatabaseDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlServerDatabaseDetails)` | The sqlserverDatabaseDetails.  
  
### getSqlserverDatabaseDetailsOrBuilder()
    
    
    public abstract SqlServerDatabaseDetailsOrBuilder getSqlserverDatabaseDetailsOrBuilder()

`.google.cloud.sql.v1beta4.SqlServerDatabaseDetails sqlserver_database_details = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerDatabaseDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlServerDatabaseDetailsOrBuilder)` |   
  
### hasSqlserverDatabaseDetails()
    
    
    public abstract boolean hasSqlserverDatabaseDetails()

`.google.cloud.sql.v1beta4.SqlServerDatabaseDetails sqlserver_database_details = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlserverDatabaseDetails field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
