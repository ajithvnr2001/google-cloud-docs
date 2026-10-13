---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter
title: Chronicle v1 API - Class DashboardFilter (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:02.650464+00:00
---

# Chronicle v1 API - Class DashboardFilter (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class DashboardFilter (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class DashboardFilter : IMessage<DashboardFilter>, IEquatable<DashboardFilter>, IDeepCloneable<DashboardFilter>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class DashboardFilter.

Dashboard level filter that can be used in native dashboards as well as inputs to execute query.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DashboardFilter

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DashboardFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DashboardFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DashboardFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### DashboardFilter()
    
    
    public DashboardFilter()

### DashboardFilter(DashboardFilter)
    
    
    public DashboardFilter(DashboardFilter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DashboardFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardFilter)`  
  
  
## Properties 

### AdvancedFilterConfig
    
    
    public AdvancedFilterConfig AdvancedFilterConfig { get; set; }

Optional. Advanced filter configuration for the filter widget.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)` |   
  
### ChartIds
    
    
    public RepeatedField<string> ChartIds { get; }

Chart IDs the filter is applicable for.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataSource
    
    
    public DataSource DataSource { get; set; }

Datasource the filter is applicable for.

**Property Value**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSource)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Display name of the filter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FieldPath
    
    
    public string FieldPath { get; set; }

Filter field path.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FilterOperatorAndFieldValues
    
    
    public RepeatedField<FilterOperatorAndValues> FilterOperatorAndFieldValues { get; }

Operator and values. Can include multiple modifiers.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[FilterOperatorAndValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.FilterOperatorAndValues)` |   
  
### HasIsStandardTimeRangeFilterEnabled
    
    
    public bool HasIsStandardTimeRangeFilterEnabled { get; }

Gets whether the "is_standard_time_range_filter_enabled" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public string Id { get; set; }

ID of the filter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IsMandatory
    
    
    public bool IsMandatory { get; set; }

Optional. Whether this filter is required to be populated by the dashboard consumer prior to the dashboard loading.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsStandardTimeRangeFilter
    
    
    public bool IsStandardTimeRangeFilter { get; set; }

Optional. Whether the filter is a standard time range filter, meaning that it has to be used as the query time range, and not as a predicate in the query. A chart can have at most one standard time range filter applied.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsStandardTimeRangeFilterEnabled
    
    
    public bool IsStandardTimeRangeFilterEnabled { get; set; }

Optional. Whether this standard time range filter is enabled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
