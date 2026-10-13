---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest
title: Google BigQuery Data Transfer v1 API - Class CheckValidCredsRequest (4.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:49.039123+00:00
---

# Google BigQuery Data Transfer v1 API - Class CheckValidCredsRequest (4.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery Data Transfer v1 API - Class CheckValidCredsRequest (4.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.11.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.10.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.9.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.8.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.7.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.6.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.5.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.4.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.3.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.2.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.1.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 4.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/4.0.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/3.4.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/3.3.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/3.2.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/3.1.0/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)


    
    
    public sealed class CheckValidCredsRequest : IMessage<CheckValidCredsRequest>, IEquatable<CheckValidCredsRequest>, IDeepCloneable<CheckValidCredsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google BigQuery Data Transfer v1 API class CheckValidCredsRequest.

A request to determine whether the user has valid credentials. This method is used to limit the number of OAuth popups in the user interface. The user id is inferred from the API call context. If the data source has the Google+ authorization type, this method returns false, as it cannot be determined whether the credentials are already valid merely based on the user id.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CheckValidCredsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CheckValidCredsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CheckValidCredsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CheckValidCredsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.DataTransfer.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1)

## Assembly

Google.Cloud.BigQuery.DataTransfer.V1.dll

## Constructors 

### CheckValidCredsRequest()
    
    
    public CheckValidCredsRequest()

### CheckValidCredsRequest(CheckValidCredsRequest)
    
    
    public CheckValidCredsRequest(CheckValidCredsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CheckValidCredsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest)`  
  
  
## Properties 

### DataSourceName
    
    
    public DataSourceName DataSourceName { get; set; }

[DataSourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataSourceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.CheckValidCredsRequest#Google_Cloud_BigQuery_DataTransfer_V1_CheckValidCredsRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataSourceName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The data source in the form: `projects/{project_id}/dataSources/{data_source_id}` or `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
