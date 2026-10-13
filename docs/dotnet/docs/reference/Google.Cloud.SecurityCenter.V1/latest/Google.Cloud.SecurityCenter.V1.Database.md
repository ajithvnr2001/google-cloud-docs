---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database
title: Google Cloud Security Command Center v1 API - Class Database (3.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:59.710789+00:00
---

# Google Cloud Security Command Center v1 API - Class Database (3.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1 API - Class Database (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class Database : IMessage<Database>, IEquatable<Database>, IDeepCloneable<Database>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1 API class Database.

Represents database access information, such as queries. A database may be a sub-resource of an instance (as in the case of Cloud SQL instances or Cloud Spanner instances), or the database instance itself. Some database resources might not have the [full resource name](https://google.aip.dev/122#full-resource-names) populated because these resource types, such as Cloud SQL databases, are not yet supported by Cloud Asset Inventory. In these cases only the display name is provided.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Database

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1)

## Assembly

Google.Cloud.SecurityCenter.V1.dll

## Constructors 

### Database()
    
    
    public Database()

### Database(Database)
    
    
    public Database(Database other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.Database)`  
  
  
## Properties 

### DisplayName
    
    
    public string DisplayName { get; set; }

The human-readable name of the database that the user connected to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Grantees
    
    
    public RepeatedField<string> Grantees { get; }

The target usernames, roles, or groups of an SQL privilege grant, which is not an IAM policy change.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Some database resources may not have the [full resource name](https://google.aip.dev/122#full-resource-names) populated because these resource types are not yet supported by Cloud Asset Inventory (e.g. Cloud SQL databases). In these cases only the display name will be provided. The [full resource name](https://google.aip.dev/122#full-resource-names) of the database that the user connected to, if it is supported by Cloud Asset Inventory.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Query
    
    
    public string Query { get; set; }

The SQL statement that is associated with the database access.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UserName
    
    
    public string UserName { get; set; }

The username used to connect to the database. The username might not be an IAM principal and does not have a set format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Version
    
    
    public string Version { get; set; }

The version of the database, for example, POSTGRES_14. See [the complete list](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
