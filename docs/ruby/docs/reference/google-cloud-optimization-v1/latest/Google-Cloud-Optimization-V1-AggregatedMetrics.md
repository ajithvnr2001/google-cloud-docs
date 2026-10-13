---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-AggregatedMetrics/
title: Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::AggregatedMetrics (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:05.598879+00:00
---

# Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::AggregatedMetrics (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-AggregatedMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::AggregatedMetrics (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.1  0.1.1 

Reference documentation and code samples for the Cloud Optimization V1 API class Google::Cloud::Optimization::V1::AggregatedMetrics.

Aggregated metrics for [ShipmentRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute "Google::Cloud::Optimization::V1::ShipmentRoute \(class\)") (resp. for [OptimizeToursResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse "Google::Cloud::Optimization::V1::OptimizeToursResponse \(class\)") over all [Transition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition "Google::Cloud::Optimization::V1::ShipmentRoute::Transition \(class\)") and/or [Visit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Visit "Google::Cloud::Optimization::V1::ShipmentRoute::Visit \(class\)") (resp. over all [ShipmentRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute "Google::Cloud::Optimization::V1::ShipmentRoute \(class\)")) elements.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #break_duration
    
    
    def break_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total break duration for a route or a solution. 



### #break_duration=
    
    
    def break_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total break duration for a route or a solution. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total break duration for a route or a solution. 



### #costs
    
    
    def costs() -> ::Google::Protobuf::Map{::String => ::Float}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Float}) — Deprecated: Use [ShipmentRoute.route_costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_costs_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_costs \(method\)") and [OptimizeToursResponse.Metrics.costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_costs_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#costs \(method\)") instead. 



### #costs=
    
    
    def costs=(value) -> ::Google::Protobuf::Map{::String => ::Float}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Float}) — Deprecated: Use [ShipmentRoute.route_costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_costs_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_costs \(method\)") and [OptimizeToursResponse.Metrics.costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_costs_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#costs \(method\)") instead. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Float}) — Deprecated: Use [ShipmentRoute.route_costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_costs_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_costs \(method\)") and [OptimizeToursResponse.Metrics.costs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_costs_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#costs \(method\)") instead. 



### #delay_duration
    
    
    def delay_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total delay duration for a route or a solution. 



### #delay_duration=
    
    
    def delay_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total delay duration for a route or a solution. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total delay duration for a route or a solution. 



### #max_loads
    
    
    def max_loads() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::ShipmentRoute::VehicleLoad}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::ShipmentRoute::VehicleLoad}) — Maximum load achieved over the entire route (resp. solution), for each of the quantities on this route (resp. solution), computed as the maximum over all [Transition.vehicle_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_vehicle_loads_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#vehicle_loads \(method\)") (resp. [ShipmentRoute.metrics.max_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-AggregatedMetrics#Google__Cloud__Optimization__V1__AggregatedMetrics_max_loads_instance_ "Google::Cloud::Optimization::V1::AggregatedMetrics#max_loads \(method\)"). 



### #max_loads=
    
    
    def max_loads=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::ShipmentRoute::VehicleLoad}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::ShipmentRoute::VehicleLoad}) — Maximum load achieved over the entire route (resp. solution), for each of the quantities on this route (resp. solution), computed as the maximum over all [Transition.vehicle_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_vehicle_loads_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#vehicle_loads \(method\)") (resp. [ShipmentRoute.metrics.max_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-AggregatedMetrics#Google__Cloud__Optimization__V1__AggregatedMetrics_max_loads_instance_ "Google::Cloud::Optimization::V1::AggregatedMetrics#max_loads \(method\)"). 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::ShipmentRoute::VehicleLoad}) — Maximum load achieved over the entire route (resp. solution), for each of the quantities on this route (resp. solution), computed as the maximum over all [Transition.vehicle_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_vehicle_loads_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#vehicle_loads \(method\)") (resp. [ShipmentRoute.metrics.max_loads](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-AggregatedMetrics#Google__Cloud__Optimization__V1__AggregatedMetrics_max_loads_instance_ "Google::Cloud::Optimization::V1::AggregatedMetrics#max_loads \(method\)"). 



### #performed_shipment_count
    
    
    def performed_shipment_count() -> ::Integer

**Returns**

  * (::Integer) — Number of shipments performed. Note that a pickup and delivery pair only counts once. 



### #performed_shipment_count=
    
    
    def performed_shipment_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of shipments performed. Note that a pickup and delivery pair only counts once. 



**Returns**

  * (::Integer) — Number of shipments performed. Note that a pickup and delivery pair only counts once. 



### #total_cost
    
    
    def total_cost() -> ::Float

**Returns**

  * (::Float) — Deprecated: Use [ShipmentRoute.route_total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_total_cost_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_total_cost \(method\)") and [OptimizeToursResponse.Metrics.total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_total_cost_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#total_cost \(method\)") instead. 



### #total_cost=
    
    
    def total_cost=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Deprecated: Use [ShipmentRoute.route_total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_total_cost_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_total_cost \(method\)") and [OptimizeToursResponse.Metrics.total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_total_cost_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#total_cost \(method\)") instead. 



**Returns**

  * (::Float) — Deprecated: Use [ShipmentRoute.route_total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_route_total_cost_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#route_total_cost \(method\)") and [OptimizeToursResponse.Metrics.total_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-OptimizeToursResponse-Metrics#Google__Cloud__Optimization__V1__OptimizeToursResponse__Metrics_total_cost_instance_ "Google::Cloud::Optimization::V1::OptimizeToursResponse::Metrics#total_cost \(method\)") instead. 



### #total_duration
    
    
    def total_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — The total duration should be equal to the sum of all durations above. For routes, it also corresponds to: [ShipmentRoute.vehicle_end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_end_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_end_time \(method\)") `-` [ShipmentRoute.vehicle_start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_start_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_start_time \(method\)")



### #total_duration=
    
    
    def total_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — The total duration should be equal to the sum of all durations above. For routes, it also corresponds to: [ShipmentRoute.vehicle_end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_end_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_end_time \(method\)") `-` [ShipmentRoute.vehicle_start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_start_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_start_time \(method\)")



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — The total duration should be equal to the sum of all durations above. For routes, it also corresponds to: [ShipmentRoute.vehicle_end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_end_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_end_time \(method\)") `-` [ShipmentRoute.vehicle_start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_vehicle_start_time_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#vehicle_start_time \(method\)")



### #travel_distance_meters
    
    
    def travel_distance_meters() -> ::Float

**Returns**

  * (::Float) — Total travel distance for a route or a solution. 



### #travel_distance_meters=
    
    
    def travel_distance_meters=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Total travel distance for a route or a solution. 



**Returns**

  * (::Float) — Total travel distance for a route or a solution. 



### #travel_duration
    
    
    def travel_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total travel duration for a route or a solution. 



### #travel_duration=
    
    
    def travel_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total travel duration for a route or a solution. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total travel duration for a route or a solution. 



### #visit_duration
    
    
    def visit_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total visit duration for a route or a solution. 



### #visit_duration=
    
    
    def visit_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total visit duration for a route or a solution. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total visit duration for a route or a solution. 



### #wait_duration
    
    
    def wait_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total wait duration for a route or a solution. 



### #wait_duration=
    
    
    def wait_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total wait duration for a route or a solution. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Protobuf-Duration)) — Total wait duration for a route or a solution. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
