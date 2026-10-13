---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.AcquireSsrsLeaseContextOrBuilder
title: Interface AcquireSsrsLeaseContextOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:49.924968+00:00
---

# Interface AcquireSsrsLeaseContextOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.AcquireSsrsLeaseContextOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AcquireSsrsLeaseContextOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface AcquireSsrsLeaseContextOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDuration()
    
    
    public abstract Duration getDuration()

Lease duration needed for SSRS setup.

`optional .google.protobuf.Duration duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The duration.  
  
### getDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getDurationOrBuilder()

Lease duration needed for SSRS setup.

`optional .google.protobuf.Duration duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getReportDatabase()
    
    
    public abstract String getReportDatabase()

The report database to be used for SSRS setup.

`optional string report_database = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reportDatabase.  
  
### getReportDatabaseBytes()
    
    
    public abstract ByteString getReportDatabaseBytes()

The report database to be used for SSRS setup.

`optional string report_database = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for reportDatabase.  
  
### getServiceLogin()
    
    
    public abstract String getServiceLogin()

The username to be used as the service login to connect to the report database for SSRS setup.

`optional string service_login = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceLogin.  
  
### getServiceLoginBytes()
    
    
    public abstract ByteString getServiceLoginBytes()

The username to be used as the service login to connect to the report database for SSRS setup.

`optional string service_login = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceLogin.  
  
### getSetupLogin()
    
    
    public abstract String getSetupLogin()

The username to be used as the setup login to connect to the database server for SSRS setup.

`optional string setup_login = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The setupLogin.  
  
### getSetupLoginBytes()
    
    
    public abstract ByteString getSetupLoginBytes()

The username to be used as the setup login to connect to the database server for SSRS setup.

`optional string setup_login = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for setupLogin.  
  
### hasDuration()
    
    
    public abstract boolean hasDuration()

Lease duration needed for SSRS setup.

`optional .google.protobuf.Duration duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the duration field is set.  
  
### hasReportDatabase()
    
    
    public abstract boolean hasReportDatabase()

The report database to be used for SSRS setup.

`optional string report_database = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reportDatabase field is set.  
  
### hasServiceLogin()
    
    
    public abstract boolean hasServiceLogin()

The username to be used as the service login to connect to the report database for SSRS setup.

`optional string service_login = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceLogin field is set.  
  
### hasSetupLogin()
    
    
    public abstract boolean hasSetupLogin()

The username to be used as the setup login to connect to the database server for SSRS setup.

`optional string setup_login = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the setupLogin field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
