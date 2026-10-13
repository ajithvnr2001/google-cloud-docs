---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest
title: Dataproc Metastore v1beta API - Class DeleteBackupRequest (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:18.841964+00:00
---

# Dataproc Metastore v1beta API - Class DeleteBackupRequest (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class DeleteBackupRequest (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)


    
    
    public sealed class DeleteBackupRequest : IMessage<DeleteBackupRequest>, IEquatable<DeleteBackupRequest>, IDeepCloneable<DeleteBackupRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataproc Metastore v1beta API class DeleteBackupRequest.

Request message for [DataprocMetastore.DeleteBackup][google.cloud.metastore.v1beta.DataprocMetastore.DeleteBackup].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteBackupRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Constructors 

### DeleteBackupRequest()
    
    
    public DeleteBackupRequest()

### DeleteBackupRequest(DeleteBackupRequest)
    
    
    public DeleteBackupRequest(DeleteBackupRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)`  
  
  
## Properties 

### BackupName
    
    
    public BackupName BackupName { get; set; }

[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest#Google_Cloud_Metastore_V1Beta_DeleteBackupRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The relative resource name of the backup to delete, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
