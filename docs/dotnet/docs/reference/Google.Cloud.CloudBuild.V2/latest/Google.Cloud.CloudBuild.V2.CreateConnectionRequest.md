---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest
title: Cloud Build v2 API - Class CreateConnectionRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:19.005798+00:00
---

# Cloud Build v2 API - Class CreateConnectionRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v2 API - Class CreateConnectionRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.4.0/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.3.0/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.2.0/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.1.0/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.0.0/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)


    
    
    public sealed class CreateConnectionRequest : IMessage<CreateConnectionRequest>, IEquatable<CreateConnectionRequest>, IDeepCloneable<CreateConnectionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Build v2 API class CreateConnectionRequest.

Message for creating a Connection

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateConnectionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2)

## Assembly

Google.Cloud.CloudBuild.V2.dll

## Constructors 

### CreateConnectionRequest()
    
    
    public CreateConnectionRequest()

### CreateConnectionRequest(CreateConnectionRequest)
    
    
    public CreateConnectionRequest(CreateConnectionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest)`  
  
  
## Properties 

### Connection
    
    
    public Connection Connection { get; set; }

Required. The Connection to create.

**Property Value**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.Connection)` |   
  
### ConnectionId
    
    
    public string ConnectionId { get; set; }

Required. The ID to use for the Connection, which will become the final component of the Connection's resource name. Names must be unique per-project per-location. Allows alphanumeric characters and any of -._~%!$&amp;'()*+,;=@.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Project and location where the connection will be created. Format: `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.CreateConnectionRequest#Google_Cloud_CloudBuild_V2_CreateConnectionRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
