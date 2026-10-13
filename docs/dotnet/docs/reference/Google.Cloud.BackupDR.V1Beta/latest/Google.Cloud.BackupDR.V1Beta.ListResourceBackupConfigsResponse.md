---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse
title: Backup and DR Service v1beta API - Class ListResourceBackupConfigsResponse (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:13.665277+00:00
---

# Backup and DR Service v1beta API - Class ListResourceBackupConfigsResponse (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1beta API - Class ListResourceBackupConfigsResponse (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ListResourceBackupConfigsResponse : IPageResponse<ResourceBackupConfig>, IEnumerable<ResourceBackupConfig>, IEnumerable, IMessage<ListResourceBackupConfigsResponse>, IEquatable<ListResourceBackupConfigsResponse>, IDeepCloneable<ListResourceBackupConfigsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup and DR Service v1beta API class ListResourceBackupConfigsResponse.

Response for ListResourceBackupConfigs.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListResourceBackupConfigsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[ResourceBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ResourceBackupConfig), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ResourceBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ResourceBackupConfig), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListResourceBackupConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListResourceBackupConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListResourceBackupConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta)

## Assembly

Google.Cloud.BackupDR.V1Beta.dll

## Constructors 

### ListResourceBackupConfigsResponse()
    
    
    public ListResourceBackupConfigsResponse()

### ListResourceBackupConfigsResponse(ListResourceBackupConfigsResponse)
    
    
    public ListResourceBackupConfigsResponse(ListResourceBackupConfigsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListResourceBackupConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ListResourceBackupConfigsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token identifying a page of results the server should return.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceBackupConfigs
    
    
    public RepeatedField<ResourceBackupConfig> ResourceBackupConfigs { get; }

The list of ResourceBackupConfigs for the specified scope.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ResourceBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ResourceBackupConfig)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<ResourceBackupConfig> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[ResourceBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.ResourceBackupConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
