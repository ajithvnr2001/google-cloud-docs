---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route
title: DataStream v1 API - Class Route (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:44.827844+00:00
---

# DataStream v1 API - Class Route (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class Route (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.Route)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.Route)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.Route)


    
    
    public sealed class Route : IMessage<Route>, IEquatable<Route>, IDeepCloneable<Route>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1 API class Route.

The route resource is the child of the private connection resource, used for defining a route for a private connection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Route

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Constructors 

### Route()
    
    
    public Route()

### Route(Route)
    
    
    public Route(Route other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The create time of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DestinationAddress
    
    
    public string DestinationAddress { get; set; }

Required. Destination address for connection

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DestinationPort
    
    
    public int DestinationPort { get; set; }

Destination port for connection

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Display name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Identifier. The resource's name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RouteName
    
    
    public RouteName RouteName { get; set; }

[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route#Google_Cloud_Datastream_V1_Route_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The update time of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
