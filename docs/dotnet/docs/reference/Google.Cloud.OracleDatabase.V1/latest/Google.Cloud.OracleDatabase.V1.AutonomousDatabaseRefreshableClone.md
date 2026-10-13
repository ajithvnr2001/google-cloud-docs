---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone
title: Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseRefreshableClone (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:32.430737+00:00
---

# Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseRefreshableClone (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseRefreshableClone (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AutonomousDatabaseRefreshableClone : IMessage<AutonomousDatabaseRefreshableClone>, IEquatable<AutonomousDatabaseRefreshableClone>, IDeepCloneable<AutonomousDatabaseRefreshableClone>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class AutonomousDatabaseRefreshableClone.

An Autonomous Database refreshable clone

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutonomousDatabaseRefreshableClone

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutonomousDatabaseRefreshableClone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutonomousDatabaseRefreshableClone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutonomousDatabaseRefreshableClone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### AutonomousDatabaseRefreshableClone()
    
    
    public AutonomousDatabaseRefreshableClone()

### AutonomousDatabaseRefreshableClone(AutonomousDatabaseRefreshableClone)
    
    
    public AutonomousDatabaseRefreshableClone(AutonomousDatabaseRefreshableClone other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutonomousDatabaseRefreshableClone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone)`  
  
  
## Properties 

### AutonomousDatabaseName
    
    
    public AutonomousDatabaseName AutonomousDatabaseName { get; set; }

[AutonomousDatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseRefreshableClone#Google_Cloud_OracleDatabase_V1_AutonomousDatabaseRefreshableClone_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseName)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The GCP resource name of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Region
    
    
    public string Region { get; set; }

Output only. The Google Cloud region where the refreshable clone exists.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
