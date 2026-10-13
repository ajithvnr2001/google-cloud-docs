---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition
title: Cloud Optimization v1 API - Class ShipmentRoute.Types.Transition (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:32.754627+00:00
---

# Cloud Optimization v1 API - Class ShipmentRoute.Types.Transition (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Optimization v1 API - Class ShipmentRoute.Types.Transition (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.6.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.5.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.4.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.3.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.2.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.1.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.0.0/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/1.0.0-beta01/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)


    
    
    public sealed class ShipmentRoute.Types.Transition : IMessage<ShipmentRoute.Types.Transition>, IEquatable<ShipmentRoute.Types.Transition>, IDeepCloneable<ShipmentRoute.Types.Transition>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Optimization v1 API class ShipmentRoute.Types.Transition.

Transition between two events on the route. See the description of [ShipmentRoute][google.cloud.optimization.v1.ShipmentRoute].

If the vehicle does not have a `start_location` and/or `end_location`, the corresponding travel metrics are 0.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ShipmentRoute.Types.Transition

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Optimization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1)

## Assembly

Google.Cloud.Optimization.V1.dll

## Constructors 

### Transition()
    
    
    public Transition()

### Transition(Transition)
    
    
    public Transition(ShipmentRoute.Types.Transition other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.Transition)`  
  
  
## Properties 

### BreakDuration
    
    
    public Duration BreakDuration { get; set; }

Sum of the duration of the breaks occurring during this transition, if any. Details about each break's start time and duration are stored in [ShipmentRoute.breaks][google.cloud.optimization.v1.ShipmentRoute.breaks].

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### DelayDuration
    
    
    public Duration DelayDuration { get; set; }

Sum of the delay durations applied to this transition. If any, the delay starts exactly `delay_duration` seconds before the next event (visit or vehicle end). See [TransitionAttributes.delay][google.cloud.optimization.v1.TransitionAttributes.delay].

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Loads
    
    
    [Obsolete]
    public RepeatedField<CapacityQuantity> Loads { get; }

Deprecated: Use [Transition.vehicle_loads][google.cloud.optimization.v1.ShipmentRoute.Transition.vehicle_loads] instead.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CapacityQuantity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.CapacityQuantity)` |   
  
### RoutePolyline
    
    
    public ShipmentRoute.Types.EncodedPolyline RoutePolyline { get; set; }

The encoded polyline representation of the route followed during the transition. This field is only populated if [populate_transition_polylines] [google.cloud.optimization.v1.OptimizeToursRequest.populate_transition_polylines] is set to true.

**Property Value**  
---  
**Type** | **Description**  
`[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[EncodedPolyline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.EncodedPolyline)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Start time of this transition.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### TotalDuration
    
    
    public Duration TotalDuration { get; set; }

Total duration of the transition, provided for convenience. It is equal to:

  * next visit `start_time` (or `vehicle_end_time` if this is the last transition) - this transition's `start_time`;
  * if `ShipmentRoute.has_traffic_infeasibilities` is false, the following additionally holds: `total_duration = travel_duration + delay_duration
  * break_duration + wait_duration`.



**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### TrafficInfoUnavailable
    
    
    public bool TrafficInfoUnavailable { get; set; }

When traffic is requested via [OptimizeToursRequest.consider_road_traffic] [google.cloud.optimization.v1.OptimizeToursRequest.consider_road_traffic], and the traffic info couldn't be retrieved for a `Transition`, this boolean is set to true. This may be temporary (rare hiccup in the realtime traffic servers) or permanent (no data for this location).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TravelDistanceMeters
    
    
    public double TravelDistanceMeters { get; set; }

Distance traveled during the transition.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### TravelDuration
    
    
    public Duration TravelDuration { get; set; }

Travel duration during this transition.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### VehicleLoads
    
    
    public MapField<string, ShipmentRoute.Types.VehicleLoad> VehicleLoads { get; }

Vehicle loads during this transition, for each type that either appears in this vehicle's [Vehicle.load_limits][google.cloud.optimization.v1.Vehicle.load_limits], or that have non-zero [Shipment.load_demands][google.cloud.optimization.v1.Shipment.load_demands] on some shipment performed on this route.

The loads during the first transition are the starting loads of the vehicle route. Then, after each visit, the visit's `load_demands` are either added or subtracted to get the next transition's loads, depending on whether the visit was a pickup or a delivery.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types)[VehicleLoad](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute.Types.VehicleLoad)` |   
  
### WaitDuration
    
    
    public Duration WaitDuration { get; set; }

Time spent waiting during this transition. Wait duration corresponds to idle time and does not include break time. Also note that this wait time may be split into several non-contiguous intervals.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
