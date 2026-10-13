---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest
title: Chronicle v1 API - Class CreateDataAccessLabelRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:36.452914+00:00
---

# Chronicle v1 API - Class CreateDataAccessLabelRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CreateDataAccessLabelRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CreateDataAccessLabelRequest : IMessage<CreateDataAccessLabelRequest>, IEquatable<CreateDataAccessLabelRequest>, IDeepCloneable<CreateDataAccessLabelRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CreateDataAccessLabelRequest.

Request message for CreateDataAccessLabel.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateDataAccessLabelRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateDataAccessLabelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateDataAccessLabelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateDataAccessLabelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### CreateDataAccessLabelRequest()
    
    
    public CreateDataAccessLabelRequest()

### CreateDataAccessLabelRequest(CreateDataAccessLabelRequest)
    
    
    public CreateDataAccessLabelRequest(CreateDataAccessLabelRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateDataAccessLabelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest)`  
  
  
## Properties 

### DataAccessLabel
    
    
    public DataAccessLabel DataAccessLabel { get; set; }

Required. Data access label to create.

**Property Value**  
---  
**Type** | **Description**  
`[DataAccessLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataAccessLabel)` |   
  
### DataAccessLabelId
    
    
    public string DataAccessLabelId { get; set; }

Required. The ID to use for the data access label, which will become the label's display name and the final component of the label's resource name. The maximum number of characters should be 63. Regex pattern is as per AIP: <https://google.aip.dev/122#resource-id-segments>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource where this Data Access Label will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsInstanceName
    
    
    public InstanceName ParentAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataAccessLabelRequest#Google_Cloud_Chronicle_V1_CreateDataAccessLabelRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
