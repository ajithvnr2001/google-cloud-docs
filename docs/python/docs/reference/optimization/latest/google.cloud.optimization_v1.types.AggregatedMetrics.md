---
url: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.AggregatedMetrics
title: Class AggregatedMetrics (1.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:44.934048+00:00
---

# Class AggregatedMetrics (1.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.AggregatedMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AggregatedMetrics (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.0  1.9.1  1.8.5  1.7.0  1.6.0  1.5.0  1.4.3  1.3.2  1.2.0  1.1.3  1.0.1  0.1.1 
    
    
    AggregatedMetrics(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Aggregated metrics for ShipmentRoute (resp. for OptimizeToursResponse over all Transition and/or Visit (resp. over all ShipmentRoute) elements.

## Attributes  
  
---  
**Name** | **Description**  
`performed_shipment_count` |  `int`   
Number of shipments performed. Note that a pickup and delivery pair only counts once.   
`travel_duration` |  `google.protobuf.duration_pb2.Duration`   
Total travel duration for a route or a solution.   
`wait_duration` |  `google.protobuf.duration_pb2.Duration`   
Total wait duration for a route or a solution.   
`delay_duration` |  `google.protobuf.duration_pb2.Duration`   
Total delay duration for a route or a solution.   
`break_duration` |  `google.protobuf.duration_pb2.Duration`   
Total break duration for a route or a solution.   
`visit_duration` |  `google.protobuf.duration_pb2.Duration`   
Total visit duration for a route or a solution.   
`total_duration` |  `google.protobuf.duration_pb2.Duration`   
The total duration should be equal to the sum of all durations above. For routes, it also corresponds to: ShipmentRoute.vehicle_end_time `-` ShipmentRoute.vehicle_start_time  
`travel_distance_meters` |  `float`   
Total travel distance for a route or a solution.   
`max_loads` |  `MutableMapping[str, [google.cloud.optimization_v1.types.ShipmentRoute.VehicleLoad](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.ShipmentRoute.VehicleLoad)]`   
Maximum load achieved over the entire route (resp. solution), for each of the quantities on this route (resp. solution), computed as the maximum over all Transition.vehicle_loads (resp. ShipmentRoute.metrics.max_loads.   
`costs` |  `MutableMapping[str, float]`   
Deprecated: Use ShipmentRoute.route_costs and OptimizeToursResponse.Metrics.costs instead.   
`total_cost` |  `float`   
Deprecated: Use ShipmentRoute.route_total_cost and OptimizeToursResponse.Metrics.total_cost instead.   
  
## Classes 

### CostsEntry
    
    
    CostsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### MaxLoadsEntry
    
    
    MaxLoadsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
