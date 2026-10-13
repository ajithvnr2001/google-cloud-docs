---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties
title: Backup and DR Service v1beta API - Class CloudSqlInstanceBackupProperties (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:26.704345+00:00
---

# Backup and DR Service v1beta API - Class CloudSqlInstanceBackupProperties (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1beta API - Class CloudSqlInstanceBackupProperties (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class CloudSqlInstanceBackupProperties : IMessage<CloudSqlInstanceBackupProperties>, IEquatable<CloudSqlInstanceBackupProperties>, IDeepCloneable<CloudSqlInstanceBackupProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup and DR Service v1beta API class CloudSqlInstanceBackupProperties.

CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudSqlInstanceBackupProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta)

## Assembly

Google.Cloud.BackupDR.V1Beta.dll

## Constructors 

### CloudSqlInstanceBackupProperties()
    
    
    public CloudSqlInstanceBackupProperties()

### CloudSqlInstanceBackupProperties(CloudSqlInstanceBackupProperties)
    
    
    public CloudSqlInstanceBackupProperties(CloudSqlInstanceBackupProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties)`  
  
  
## Properties 

### DatabaseInstalledVersion
    
    
    public string DatabaseInstalledVersion { get; set; }

Output only. The installed database version of the Cloud SQL instance when the backup was taken.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FinalBackup
    
    
    public bool FinalBackup { get; set; }

Output only. Whether the backup is a final backup.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceCreateTime
    
    
    public Timestamp InstanceCreateTime { get; set; }

Output only. The instance creation timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### InstanceDeleteTime
    
    
    public Timestamp InstanceDeleteTime { get; set; }

Output only. The instance delete timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### InstanceTier
    
    
    public string InstanceTier { get; set; }

Output only. The tier (or machine type) for this instance. Example: `db-custom-1-3840`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceInstance
    
    
    public string SourceInstance { get; set; }

Output only. The source instance of the backup. Format: projects/{project}/instances/{instance}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceInstanceAsInstanceName
    
    
    public InstanceName SourceInstanceAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.InstanceName)-typed view over the [SourceInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.CloudSqlInstanceBackupProperties#Google_Cloud_BackupDR_V1Beta_CloudSqlInstanceBackupProperties_SourceInstance) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.InstanceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
