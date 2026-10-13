---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.QueryExtensions
title: Google Cloud Datastore v1 API - Class QueryExtensions (5.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:31.821964+00:00
---

# Google Cloud Datastore v1 API - Class QueryExtensions (5.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.QueryExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Datastore v1 API - Class QueryExtensions (5.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public static class QueryExtensions

Reference documentation and code samples for the Google Cloud Datastore v1 API class QueryExtensions.

Extension methods around queries.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QueryExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1)

## Assembly

Google.Cloud.Datastore.V1.dll

## Methods 

### Add(MapField<string, GqlQueryParameter>, string, Value)
    
    
    public static void Add(this MapField<string, GqlQueryParameter> parameters, string parameterName, Value value)

Adds a GQL parameter with the specified value.

**Parameters**  
---  
**Name** | **Description**  
`parameters` | `[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[GqlQueryParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.GqlQueryParameter)`  
The mapping of GQL query parameters to add to. Must not be null.  
`parameterName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parameter. Must not be null.  
`value` | `[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Value)`  
The value to add. May be null, which indicates a value with [NullValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Value#Google_Cloud_Datastore_V1_Value_NullValue) set.  
  
### Add(RepeatedField<GqlQueryParameter>, Value)
    
    
    public static void Add(this RepeatedField<GqlQueryParameter> parameters, Value value)

Adds a GQL parameter with the specified value.

**Parameters**  
---  
**Name** | **Description**  
`parameters` | `[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[GqlQueryParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.GqlQueryParameter)`  
The list of positional GQL query parameters to add to. Must not be null.  
`value` | `[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Value)`  
The value to add. May be null, which indicates a value with [NullValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Value#Google_Cloud_Datastore_V1_Value_NullValue) set.  
  
### Add(RepeatedField<Projection>, string)
    
    
    public static void Add(this RepeatedField<Projection> projections, string propertyName)

Adds a projection with the given property name to the repeated field. This enables projections to be specified in a query with a collection initializer in C# 6 and later.

**Parameters**  
---  
**Name** | **Description**  
`projections` | `[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Projection)`  
The collection of projections to add to. Must not be null.  
`propertyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The property to project. Must not be null.  
  
### Add(RepeatedField<PropertyOrder>, string)
    
    
    public static void Add(this RepeatedField<PropertyOrder> orderings, string propertyName)

Adds an ascending ordering by property name. The ordering is implicitly ascending.

**Parameters**  
---  
**Name** | **Description**  
`orderings` | `[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PropertyOrder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyOrder)`  
The ordering field to add the ordering to. Must not be null.  
`propertyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the property to order by. Must not be null.  
  
### Add(RepeatedField<PropertyOrder>, string, Direction)
    
    
    public static void Add(this RepeatedField<PropertyOrder> orderings, string propertyName, PropertyOrder.Types.Direction direction)

Adds an ordering by property name and direction.

**Parameters**  
---  
**Name** | **Description**  
`orderings` | `[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PropertyOrder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyOrder)`  
The ordering field to add the ordering to. Must not be null.  
`propertyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the property to order by. Must not be null.  
`direction` | `[PropertyOrder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyOrder)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyOrder.Types)[Direction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyOrder.Types.Direction)`  
The direction to order by. Must be `Ascending` or `Descending`.  
  
### Add(RepeatedField<PropertyReference>, string)
    
    
    public static void Add(this RepeatedField<PropertyReference> propertyReferences, string propertyName)

Adds an entry to the list of property references. This enables repeated property reference fields (such as [DistinctOn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Query#Google_Cloud_Datastore_V1_Query_DistinctOn) to be specified in a query with a collection initializer in C# 6 and later.

**Parameters**  
---  
**Name** | **Description**  
`propertyReferences` | `[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PropertyReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyReference)`  
The collection of property references to add to. Must not be null.  
`propertyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The property to project. Must not be null.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
