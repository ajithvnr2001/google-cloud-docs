---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest
title: Google Cloud Dialogflow v2beta1 API - Class ListConversationsRequest (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:28.829660+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ListConversationsRequest (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ListConversationsRequest (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class ListConversationsRequest : IMessage<ListConversationsRequest>, IEquatable<ListConversationsRequest>, IDeepCloneable<ListConversationsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ListConversationsRequest.

The request message for [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListConversationsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ListConversationsRequest()
    
    
    public ListConversationsRequest()

### ListConversationsRequest(ListConversationsRequest)
    
    
    public ListConversationsRequest(ListConversationsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. A filter expression that filters conversations listed in the response. Only `lifecycle_state` can be filtered on in this way. For example, the following expression only returns `COMPLETED` conversations:

`lifecycle_state = "COMPLETED"`

For more information about filtering, see [API Filtering](https://aip.dev/160).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of items to return in a single page. By default 100 and at most 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. The next_page_token value returned from a previous list request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest#Google_Cloud_Dialogflow_V2Beta1_ListConversationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest#Google_Cloud_Dialogflow_V2Beta1_ListConversationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest#Google_Cloud_Dialogflow_V2Beta1_ListConversationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
