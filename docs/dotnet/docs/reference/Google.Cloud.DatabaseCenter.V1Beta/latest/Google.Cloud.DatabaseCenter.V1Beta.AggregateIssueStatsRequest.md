---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest
title: Database Center v1beta API - Class AggregateIssueStatsRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:51.805725+00:00
---

# Database Center v1beta API - Class AggregateIssueStatsRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class AggregateIssueStatsRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class AggregateIssueStatsRequest : IMessage<AggregateIssueStatsRequest>, IEquatable<AggregateIssueStatsRequest>, IDeepCloneable<AggregateIssueStatsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class AggregateIssueStatsRequest.

AggregateIssueStatsRequest represents the input to the AggregateIssueStats method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregateIssueStatsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### AggregateIssueStatsRequest()
    
    
    public AggregateIssueStatsRequest()

### AggregateIssueStatsRequest(AggregateIssueStatsRequest)
    
    
    public AggregateIssueStatsRequest(AggregateIssueStatsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
  
  
## Properties 

### BaselineDate
    
    
    public Date BaselineDate { get; set; }

Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### Filter
    
    
    public string Filter { get; set; }

Optional. The expression to filter resources.

Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info,'resource_name', etc.

The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.

Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.

The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SignalTypeGroups
    
    
    public RepeatedField<SignalTypeGroup> SignalTypeGroups { get; }

Optional. Lists of signal types that are issues.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SignalTypeGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalTypeGroup)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
