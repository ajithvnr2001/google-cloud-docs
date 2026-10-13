---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest
title: Database Center v1beta API - Class AggregateFleetRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:50.501936+00:00
---

# Database Center v1beta API - Class AggregateFleetRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class AggregateFleetRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class AggregateFleetRequest : IPageRequest, IMessage<AggregateFleetRequest>, IEquatable<AggregateFleetRequest>, IDeepCloneable<AggregateFleetRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class AggregateFleetRequest.

The request message to aggregate fleet which are grouped by a field.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregateFleetRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### AggregateFleetRequest()
    
    
    public AggregateFleetRequest()

### AggregateFleetRequest(AggregateFleetRequest)
    
    
    public AggregateFleetRequest(AggregateFleetRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
  
  
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

Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc.

The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.

Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GroupBy
    
    
    public string GroupBy { get; set; }

Optional. A field that statistics are grouped by. Valid values are any combination of the following:

  * container
  * product.type
  * product.engine
  * product.version
  * location
  * sub_resource_type
  * management_type
  * tag.key
  * tag.value
  * tag.source
  * tag.inherited
  * label.key
  * label.value
  * label.source
  * has_maintenance_schedule
  * has_deny_maintenance_schedules Comma separated list.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. Valid values to order by are:

  * resource_groups_count
  * resources_count
  * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields. For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `AggregateFleet` call. Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
