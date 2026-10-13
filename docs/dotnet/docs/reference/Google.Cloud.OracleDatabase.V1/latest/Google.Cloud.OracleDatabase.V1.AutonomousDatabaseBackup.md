---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup
title: Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackup (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:26.670648+00:00
---

# Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackup (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackup (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AutonomousDatabaseBackup : IMessage<AutonomousDatabaseBackup>, IEquatable<AutonomousDatabaseBackup>, IDeepCloneable<AutonomousDatabaseBackup>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class AutonomousDatabaseBackup.

Details of the Autonomous Database Backup resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseBackup/>

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutonomousDatabaseBackup

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### AutonomousDatabaseBackup()
    
    
    public AutonomousDatabaseBackup()

### AutonomousDatabaseBackup(AutonomousDatabaseBackup)
    
    
    public AutonomousDatabaseBackup(AutonomousDatabaseBackup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutonomousDatabaseBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup)`  
  
  
## Properties 

### AutonomousDatabase
    
    
    public string AutonomousDatabase { get; set; }

Required. The name of the Autonomous Database resource for which the backup is being created. Format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AutonomousDatabaseAsAutonomousDatabaseName
    
    
    public AutonomousDatabaseName AutonomousDatabaseAsAutonomousDatabaseName { get; set; }

[AutonomousDatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseName)-typed view over the [AutonomousDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup#Google_Cloud_OracleDatabase_V1_AutonomousDatabaseBackup_AutonomousDatabase) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseName)` |   
  
### AutonomousDatabaseBackupName
    
    
    public AutonomousDatabaseBackupName AutonomousDatabaseBackupName { get; set; }

[AutonomousDatabaseBackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackup#Google_Cloud_OracleDatabase_V1_AutonomousDatabaseBackup_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupName)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. User friendly name for the Backup. The name does not have to be unique.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. labels or tags associated with the resource.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomous_database_backup}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Properties
    
    
    public AutonomousDatabaseBackupProperties Properties { get; set; }

Optional. Various properties of the backup.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
