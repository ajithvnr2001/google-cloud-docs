---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle/
title: Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::Vehicle (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:50.442416+00:00
---

# Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::Vehicle (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Optimization V1 API - Class Google::Cloud::Optimization::V1::Vehicle (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.1  0.1.1 

Reference documentation and code samples for the Cloud Optimization V1 API class Google::Cloud::Optimization::V1::Vehicle.

Models a vehicle in a shipment problem. Solving a shipment problem will build a route starting from `start_location` and ending at `end_location` for this vehicle. A route is a sequence of visits (see `ShipmentRoute`).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #break_rule
    
    
    def break_rule() -> ::Google::Cloud::Optimization::V1::BreakRule

**Returns**

  * ([::Google::Cloud::Optimization::V1::BreakRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-BreakRule)) — Describes the break schedule to be enforced on this vehicle. If empty, no breaks will be scheduled for this vehicle. 



### #break_rule=
    
    
    def break_rule=(value) -> ::Google::Cloud::Optimization::V1::BreakRule

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::BreakRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-BreakRule)) — Describes the break schedule to be enforced on this vehicle. If empty, no breaks will be scheduled for this vehicle. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::BreakRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-BreakRule)) — Describes the break schedule to be enforced on this vehicle. If empty, no breaks will be scheduled for this vehicle. 



### #break_rule_indices
    
    
    def break_rule_indices() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — Deprecated: No longer used. Indices in the `break_rule` field in the source [ShipmentModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentModel "Google::Cloud::Optimization::V1::ShipmentModel \(class\)"). They correspond to break rules enforced on the vehicle.

As of 2018/03, at most one rule index per vehicle can be specified. 




### #break_rule_indices=
    
    
    def break_rule_indices=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — Deprecated: No longer used. Indices in the `break_rule` field in the source [ShipmentModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentModel "Google::Cloud::Optimization::V1::ShipmentModel \(class\)"). They correspond to break rules enforced on the vehicle.

As of 2018/03, at most one rule index per vehicle can be specified. 




**Returns**

  * (::Array<::Integer>) — Deprecated: No longer used. Indices in the `break_rule` field in the source [ShipmentModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentModel "Google::Cloud::Optimization::V1::ShipmentModel \(class\)"). They correspond to break rules enforced on the vehicle.

As of 2018/03, at most one rule index per vehicle can be specified. 




### #capacities
    
    
    def capacities() -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantity>

**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantity)>) — Deprecated: Use [Vehicle.load_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle#Google__Cloud__Optimization__V1__Vehicle_load_limits_instance_ "Google::Cloud::Optimization::V1::Vehicle#load_limits \(method\)") instead. 



### #capacities=
    
    
    def capacities=(value) -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantity>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantity)>) — Deprecated: Use [Vehicle.load_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle#Google__Cloud__Optimization__V1__Vehicle_load_limits_instance_ "Google::Cloud::Optimization::V1::Vehicle#load_limits \(method\)") instead. 



**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantity)>) — Deprecated: Use [Vehicle.load_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle#Google__Cloud__Optimization__V1__Vehicle_load_limits_instance_ "Google::Cloud::Optimization::V1::Vehicle#load_limits \(method\)") instead. 



### #cost_per_hour
    
    
    def cost_per_hour() -> ::Float

**Returns**

  * (::Float) — Vehicle costs: all costs add up and must be in the same unit as [Shipment.penalty_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_penalty_cost_instance_ "Google::Cloud::Optimization::V1::Shipment#penalty_cost \(method\)").

Cost per hour of the vehicle route. This cost is applied to the total time taken by the route, and includes travel time, waiting time, and visit time. Using `cost_per_hour` instead of just `cost_per_traveled_hour` may result in additional latency. 




### #cost_per_hour=
    
    
    def cost_per_hour=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Vehicle costs: all costs add up and must be in the same unit as [Shipment.penalty_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_penalty_cost_instance_ "Google::Cloud::Optimization::V1::Shipment#penalty_cost \(method\)").

Cost per hour of the vehicle route. This cost is applied to the total time taken by the route, and includes travel time, waiting time, and visit time. Using `cost_per_hour` instead of just `cost_per_traveled_hour` may result in additional latency. 




**Returns**

  * (::Float) — Vehicle costs: all costs add up and must be in the same unit as [Shipment.penalty_cost](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_penalty_cost_instance_ "Google::Cloud::Optimization::V1::Shipment#penalty_cost \(method\)").

Cost per hour of the vehicle route. This cost is applied to the total time taken by the route, and includes travel time, waiting time, and visit time. Using `cost_per_hour` instead of just `cost_per_traveled_hour` may result in additional latency. 




### #cost_per_kilometer
    
    
    def cost_per_kilometer() -> ::Float

**Returns**

  * (::Float) — Cost per kilometer of the vehicle route. This cost is applied to the distance reported in the [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)") and does not apply to any distance implicitly traveled from the `arrival_location` to the `departure_location` of a single `VisitRequest`. 



### #cost_per_kilometer=
    
    
    def cost_per_kilometer=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Cost per kilometer of the vehicle route. This cost is applied to the distance reported in the [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)") and does not apply to any distance implicitly traveled from the `arrival_location` to the `departure_location` of a single `VisitRequest`. 



**Returns**

  * (::Float) — Cost per kilometer of the vehicle route. This cost is applied to the distance reported in the [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)") and does not apply to any distance implicitly traveled from the `arrival_location` to the `departure_location` of a single `VisitRequest`. 



### #cost_per_traveled_hour
    
    
    def cost_per_traveled_hour() -> ::Float

**Returns**

  * (::Float) — Cost per traveled hour of the vehicle route. This cost is applied only to travel time taken by the route (i.e., that reported in [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)")), and excludes waiting time and visit time. 



### #cost_per_traveled_hour=
    
    
    def cost_per_traveled_hour=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Cost per traveled hour of the vehicle route. This cost is applied only to travel time taken by the route (i.e., that reported in [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)")), and excludes waiting time and visit time. 



**Returns**

  * (::Float) — Cost per traveled hour of the vehicle route. This cost is applied only to travel time taken by the route (i.e., that reported in [ShipmentRoute.transitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute#Google__Cloud__Optimization__V1__ShipmentRoute_transitions_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute#transitions \(method\)")), and excludes waiting time and visit time. 



### #end_load_intervals
    
    
    def end_load_intervals() -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantityInterval>

**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.end_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_end_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#end_load_interval \(method\)") instead. 



### #end_load_intervals=
    
    
    def end_load_intervals=(value) -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantityInterval>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.end_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_end_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#end_load_interval \(method\)") instead. 



**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.end_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_end_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#end_load_interval \(method\)") instead. 



### #end_location
    
    
    def end_location() -> ::Google::Type::LatLng

**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle ends after it has completed its last `VisitRequest`. If not specified the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_location` must not be specified. 



### #end_location=
    
    
    def end_location=(value) -> ::Google::Type::LatLng

**Parameter**

  * **value** ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle ends after it has completed its last `VisitRequest`. If not specified the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_location` must not be specified. 



**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle ends after it has completed its last `VisitRequest`. If not specified the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_location` must not be specified. 



### #end_tags
    
    
    def end_tags() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Specifies tags attached to the end of the vehicle's route.

Empty or duplicate strings are not allowed. 




### #end_tags=
    
    
    def end_tags=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Specifies tags attached to the end of the vehicle's route.

Empty or duplicate strings are not allowed. 




**Returns**

  * (::Array<::String>) — Specifies tags attached to the end of the vehicle's route.

Empty or duplicate strings are not allowed. 




### #end_time_windows
    
    
    def end_time_windows() -> ::Array<::Google::Cloud::Optimization::V1::TimeWindow>

**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may arrive at its end location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




### #end_time_windows=
    
    
    def end_time_windows=(value) -> ::Array<::Google::Cloud::Optimization::V1::TimeWindow>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may arrive at its end location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may arrive at its end location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




### #end_waypoint
    
    
    def end_waypoint() -> ::Google::Cloud::Optimization::V1::Waypoint

**Returns**

  * ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle ends after it has completed its last `VisitRequest`. If neither `end_waypoint` nor `end_location` is specified, the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_waypoint` must not be specified. 



### #end_waypoint=
    
    
    def end_waypoint=(value) -> ::Google::Cloud::Optimization::V1::Waypoint

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle ends after it has completed its last `VisitRequest`. If neither `end_waypoint` nor `end_location` is specified, the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_waypoint` must not be specified. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle ends after it has completed its last `VisitRequest`. If neither `end_waypoint` nor `end_location` is specified, the vehicle's `ShipmentRoute` ends immediately when it completes its last `VisitRequest`. If the shipment model has duration and distance matrices, `end_waypoint` must not be specified. 



### #extra_visit_duration_for_visit_type
    
    
    def extra_visit_duration_for_visit_type() -> ::Google::Protobuf::Map{::String => ::Google::Protobuf::Duration}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Protobuf::Duration}) — Specifies a map from visit_types strings to durations. The duration is time in addition to [VisitRequest.duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment-VisitRequest#Google__Cloud__Optimization__V1__Shipment__VisitRequest_duration_instance_ "Google::Cloud::Optimization::V1::Shipment::VisitRequest#duration \(method\)") to be taken at visits with the specified `visit_types`. This extra visit duration adds cost if `cost_per_hour` is specified. Keys (i.e. `visit_types`) cannot be empty strings.

If a visit request has multiple types, a duration will be added for each type in the map. 




### #extra_visit_duration_for_visit_type=
    
    
    def extra_visit_duration_for_visit_type=(value) -> ::Google::Protobuf::Map{::String => ::Google::Protobuf::Duration}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Protobuf::Duration}) — Specifies a map from visit_types strings to durations. The duration is time in addition to [VisitRequest.duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment-VisitRequest#Google__Cloud__Optimization__V1__Shipment__VisitRequest_duration_instance_ "Google::Cloud::Optimization::V1::Shipment::VisitRequest#duration \(method\)") to be taken at visits with the specified `visit_types`. This extra visit duration adds cost if `cost_per_hour` is specified. Keys (i.e. `visit_types`) cannot be empty strings.

If a visit request has multiple types, a duration will be added for each type in the map. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Protobuf::Duration}) — Specifies a map from visit_types strings to durations. The duration is time in addition to [VisitRequest.duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment-VisitRequest#Google__Cloud__Optimization__V1__Shipment__VisitRequest_duration_instance_ "Google::Cloud::Optimization::V1::Shipment::VisitRequest#duration \(method\)") to be taken at visits with the specified `visit_types`. This extra visit duration adds cost if `cost_per_hour` is specified. Keys (i.e. `visit_types`) cannot be empty strings.

If a visit request has multiple types, a duration will be added for each type in the map. 




### #fixed_cost
    
    
    def fixed_cost() -> ::Float

**Returns**

  * (::Float) — Fixed cost applied if this vehicle is used to handle a shipment. 



### #fixed_cost=
    
    
    def fixed_cost=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Fixed cost applied if this vehicle is used to handle a shipment. 



**Returns**

  * (::Float) — Fixed cost applied if this vehicle is used to handle a shipment. 



### #ignore
    
    
    def ignore() -> ::Boolean

**Returns**

  * (::Boolean) — If true, `used_if_route_is_empty` must be false, and this vehicle will remain unused.

If a shipment is performed by an ignored vehicle in `injected_first_solution_routes`, it is skipped in the first solution but is free to be performed in the response.

If a shipment is performed by an ignored vehicle in `injected_solution_constraint` and any related pickup/delivery is constrained to remain on the vehicle (i.e., not relaxed to level `RELAX_ALL_AFTER_THRESHOLD`), it is skipped in the response. If a shipment has a non-empty `allowed_vehicle_indices` field and all of the allowed vehicles are ignored, it is skipped in the response. 




### #ignore=
    
    
    def ignore=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, `used_if_route_is_empty` must be false, and this vehicle will remain unused.

If a shipment is performed by an ignored vehicle in `injected_first_solution_routes`, it is skipped in the first solution but is free to be performed in the response.

If a shipment is performed by an ignored vehicle in `injected_solution_constraint` and any related pickup/delivery is constrained to remain on the vehicle (i.e., not relaxed to level `RELAX_ALL_AFTER_THRESHOLD`), it is skipped in the response. If a shipment has a non-empty `allowed_vehicle_indices` field and all of the allowed vehicles are ignored, it is skipped in the response. 




**Returns**

  * (::Boolean) — If true, `used_if_route_is_empty` must be false, and this vehicle will remain unused.

If a shipment is performed by an ignored vehicle in `injected_first_solution_routes`, it is skipped in the first solution but is free to be performed in the response.

If a shipment is performed by an ignored vehicle in `injected_solution_constraint` and any related pickup/delivery is constrained to remain on the vehicle (i.e., not relaxed to level `RELAX_ALL_AFTER_THRESHOLD`), it is skipped in the response. If a shipment has a non-empty `allowed_vehicle_indices` field and all of the allowed vehicles are ignored, it is skipped in the response. 




### #label
    
    
    def label() -> ::String

**Returns**

  * (::String) — Specifies a label for this vehicle. This label is reported in the response as the `vehicle_label` of the corresponding [ShipmentRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute "Google::Cloud::Optimization::V1::ShipmentRoute \(class\)"). 



### #label=
    
    
    def label=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a label for this vehicle. This label is reported in the response as the `vehicle_label` of the corresponding [ShipmentRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute "Google::Cloud::Optimization::V1::ShipmentRoute \(class\)"). 



**Returns**

  * (::String) — Specifies a label for this vehicle. This label is reported in the response as the `vehicle_label` of the corresponding [ShipmentRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute "Google::Cloud::Optimization::V1::ShipmentRoute \(class\)"). 



### #load_limits
    
    
    def load_limits() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::Vehicle::LoadLimit}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::Vehicle::LoadLimit}) — Capacities of the vehicle (weight, volume, # of pallets for example). The keys in the map are the identifiers of the type of load, consistent with the keys of the [Shipment.load_demands](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_load_demands_instance_ "Google::Cloud::Optimization::V1::Shipment#load_demands \(method\)") field. If a given key is absent from this map, the corresponding capacity is considered to be limitless. 



### #load_limits=
    
    
    def load_limits=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::Vehicle::LoadLimit}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::Vehicle::LoadLimit}) — Capacities of the vehicle (weight, volume, # of pallets for example). The keys in the map are the identifiers of the type of load, consistent with the keys of the [Shipment.load_demands](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_load_demands_instance_ "Google::Cloud::Optimization::V1::Shipment#load_demands \(method\)") field. If a given key is absent from this map, the corresponding capacity is considered to be limitless. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Optimization::V1::Vehicle::LoadLimit}) — Capacities of the vehicle (weight, volume, # of pallets for example). The keys in the map are the identifiers of the type of load, consistent with the keys of the [Shipment.load_demands](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Shipment#Google__Cloud__Optimization__V1__Shipment_load_demands_instance_ "Google::Cloud::Optimization::V1::Shipment#load_demands \(method\)") field. If a given key is absent from this map, the corresponding capacity is considered to be limitless. 



### #route_distance_limit
    
    
    def route_distance_limit() -> ::Google::Cloud::Optimization::V1::DistanceLimit

**Returns**

  * ([::Google::Cloud::Optimization::V1::DistanceLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-DistanceLimit)) — Limit applied to the total distance of the vehicle's route. In a given `OptimizeToursResponse`, the route distance is the sum of all its [transitions.travel_distance_meters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_distance_meters_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_distance_meters \(method\)"). 



### #route_distance_limit=
    
    
    def route_distance_limit=(value) -> ::Google::Cloud::Optimization::V1::DistanceLimit

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::DistanceLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-DistanceLimit)) — Limit applied to the total distance of the vehicle's route. In a given `OptimizeToursResponse`, the route distance is the sum of all its [transitions.travel_distance_meters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_distance_meters_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_distance_meters \(method\)"). 



**Returns**

  * ([::Google::Cloud::Optimization::V1::DistanceLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-DistanceLimit)) — Limit applied to the total distance of the vehicle's route. In a given `OptimizeToursResponse`, the route distance is the sum of all its [transitions.travel_distance_meters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_distance_meters_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_distance_meters \(method\)"). 



### #route_duration_limit
    
    
    def route_duration_limit() -> ::Google::Cloud::Optimization::V1::Vehicle::DurationLimit

**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the total duration of the vehicle's route. In a given `OptimizeToursResponse`, the route duration of a vehicle is the difference between its `vehicle_end_time` and `vehicle_start_time`. 



### #route_duration_limit=
    
    
    def route_duration_limit=(value) -> ::Google::Cloud::Optimization::V1::Vehicle::DurationLimit

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the total duration of the vehicle's route. In a given `OptimizeToursResponse`, the route duration of a vehicle is the difference between its `vehicle_end_time` and `vehicle_start_time`. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the total duration of the vehicle's route. In a given `OptimizeToursResponse`, the route duration of a vehicle is the difference between its `vehicle_end_time` and `vehicle_start_time`. 



### #route_modifiers
    
    
    def route_modifiers() -> ::Google::Cloud::Optimization::V1::RouteModifiers

**Returns**

  * ([::Google::Cloud::Optimization::V1::RouteModifiers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-RouteModifiers)) — Optional. A set of conditions to satisfy that affect the way routes are calculated for the given vehicle. 



### #route_modifiers=
    
    
    def route_modifiers=(value) -> ::Google::Cloud::Optimization::V1::RouteModifiers

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::RouteModifiers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-RouteModifiers)) — Optional. A set of conditions to satisfy that affect the way routes are calculated for the given vehicle. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::RouteModifiers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-RouteModifiers)) — Optional. A set of conditions to satisfy that affect the way routes are calculated for the given vehicle. 



### #start_load_intervals
    
    
    def start_load_intervals() -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantityInterval>

**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.start_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_start_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#start_load_interval \(method\)") instead. 



### #start_load_intervals=
    
    
    def start_load_intervals=(value) -> ::Array<::Google::Cloud::Optimization::V1::CapacityQuantityInterval>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.start_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_start_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#start_load_interval \(method\)") instead. 



**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::CapacityQuantityInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-CapacityQuantityInterval)>) — Deprecated: Use [Vehicle.LoadLimit.start_load_interval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-LoadLimit#Google__Cloud__Optimization__V1__Vehicle__LoadLimit_start_load_interval_instance_ "Google::Cloud::Optimization::V1::Vehicle::LoadLimit#start_load_interval \(method\)") instead. 



### #start_location
    
    
    def start_location() -> ::Google::Type::LatLng

**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle starts before picking up any shipments. If not specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_location` must not be specified. 



### #start_location=
    
    
    def start_location=(value) -> ::Google::Type::LatLng

**Parameter**

  * **value** ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle starts before picking up any shipments. If not specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_location` must not be specified. 



**Returns**

  * ([::Google::Type::LatLng](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Type-LatLng)) — Geographic location where the vehicle starts before picking up any shipments. If not specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_location` must not be specified. 



### #start_tags
    
    
    def start_tags() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Specifies tags attached to the start of the vehicle's route.

Empty or duplicate strings are not allowed. 




### #start_tags=
    
    
    def start_tags=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Specifies tags attached to the start of the vehicle's route.

Empty or duplicate strings are not allowed. 




**Returns**

  * (::Array<::String>) — Specifies tags attached to the start of the vehicle's route.

Empty or duplicate strings are not allowed. 




### #start_time_windows
    
    
    def start_time_windows() -> ::Array<::Google::Cloud::Optimization::V1::TimeWindow>

**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may depart its start location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




### #start_time_windows=
    
    
    def start_time_windows=(value) -> ::Array<::Google::Cloud::Optimization::V1::TimeWindow>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may depart its start location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




**Returns**

  * (::Array<[::Google::Cloud::Optimization::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-TimeWindow)>) — Time windows during which the vehicle may depart its start location. They must be within the global time limits (see [ShipmentModel.global_*][google.cloud.optimization.v1.ShipmentModel.global_start_time] fields). If unspecified, there is no limitation besides those global time limits.

Time windows belonging to the same repeated field must be disjoint, i.e. no time window can overlap with or be adjacent to another, and they must be in chronological order.

`cost_per_hour_after_soft_end_time` and `soft_end_time` can only be set if there is a single time window. 




### #start_waypoint
    
    
    def start_waypoint() -> ::Google::Cloud::Optimization::V1::Waypoint

**Returns**

  * ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle starts before picking up any shipments. If neither `start_waypoint` nor `start_location` is specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_waypoint` must not be specified. 



### #start_waypoint=
    
    
    def start_waypoint=(value) -> ::Google::Cloud::Optimization::V1::Waypoint

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle starts before picking up any shipments. If neither `start_waypoint` nor `start_location` is specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_waypoint` must not be specified. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Waypoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Waypoint)) — Waypoint representing a geographic location where the vehicle starts before picking up any shipments. If neither `start_waypoint` nor `start_location` is specified, the vehicle starts at its first pickup. If the shipment model has duration and distance matrices, `start_waypoint` must not be specified. 



### #travel_duration_limit
    
    
    def travel_duration_limit() -> ::Google::Cloud::Optimization::V1::Vehicle::DurationLimit

**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the travel duration of the vehicle's route. In a given `OptimizeToursResponse`, the route travel duration is the sum of all its [transitions.travel_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_duration_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_duration \(method\)"). 



### #travel_duration_limit=
    
    
    def travel_duration_limit=(value) -> ::Google::Cloud::Optimization::V1::Vehicle::DurationLimit

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the travel duration of the vehicle's route. In a given `OptimizeToursResponse`, the route travel duration is the sum of all its [transitions.travel_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_duration_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_duration \(method\)"). 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::DurationLimit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-DurationLimit)) — Limit applied to the travel duration of the vehicle's route. In a given `OptimizeToursResponse`, the route travel duration is the sum of all its [transitions.travel_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-ShipmentRoute-Transition#Google__Cloud__Optimization__V1__ShipmentRoute__Transition_travel_duration_instance_ "Google::Cloud::Optimization::V1::ShipmentRoute::Transition#travel_duration \(method\)"). 



### #travel_duration_multiple
    
    
    def travel_duration_multiple() -> ::Float

**Returns**

  * (::Float) — Specifies a multiplicative factor that can be used to increase or decrease travel times of this vehicle. For example, setting this to 2.0 means that this vehicle is slower and has travel times that are twice what they are for standard vehicles. This multiple does not affect visit durations. It does affect cost if `cost_per_hour` or `cost_per_traveled_hour` are specified. This must be in the range [0.001, 1000.0]. If unset, the vehicle is standard, and this multiple is considered 1.0.

WARNING: Travel times will be rounded to the nearest second after this multiple is applied but before performing any numerical operations, thus, a small multiple may result in a loss of precision.

See also `extra_visit_duration_for_visit_type` below. 




### #travel_duration_multiple=
    
    
    def travel_duration_multiple=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Specifies a multiplicative factor that can be used to increase or decrease travel times of this vehicle. For example, setting this to 2.0 means that this vehicle is slower and has travel times that are twice what they are for standard vehicles. This multiple does not affect visit durations. It does affect cost if `cost_per_hour` or `cost_per_traveled_hour` are specified. This must be in the range [0.001, 1000.0]. If unset, the vehicle is standard, and this multiple is considered 1.0.

WARNING: Travel times will be rounded to the nearest second after this multiple is applied but before performing any numerical operations, thus, a small multiple may result in a loss of precision.

See also `extra_visit_duration_for_visit_type` below. 




**Returns**

  * (::Float) — Specifies a multiplicative factor that can be used to increase or decrease travel times of this vehicle. For example, setting this to 2.0 means that this vehicle is slower and has travel times that are twice what they are for standard vehicles. This multiple does not affect visit durations. It does affect cost if `cost_per_hour` or `cost_per_traveled_hour` are specified. This must be in the range [0.001, 1000.0]. If unset, the vehicle is standard, and this multiple is considered 1.0.

WARNING: Travel times will be rounded to the nearest second after this multiple is applied but before performing any numerical operations, thus, a small multiple may result in a loss of precision.

See also `extra_visit_duration_for_visit_type` below. 




### #travel_mode
    
    
    def travel_mode() -> ::Google::Cloud::Optimization::V1::Vehicle::TravelMode

**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::TravelMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-TravelMode)) — The travel mode which affects the roads usable by the vehicle and its speed. See also `travel_duration_multiple`. 



### #travel_mode=
    
    
    def travel_mode=(value) -> ::Google::Cloud::Optimization::V1::Vehicle::TravelMode

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Vehicle::TravelMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-TravelMode)) — The travel mode which affects the roads usable by the vehicle and its speed. See also `travel_duration_multiple`. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::TravelMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-TravelMode)) — The travel mode which affects the roads usable by the vehicle and its speed. See also `travel_duration_multiple`. 



### #unloading_policy
    
    
    def unloading_policy() -> ::Google::Cloud::Optimization::V1::Vehicle::UnloadingPolicy

**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::UnloadingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-UnloadingPolicy)) — Unloading policy enforced on the vehicle. 



### #unloading_policy=
    
    
    def unloading_policy=(value) -> ::Google::Cloud::Optimization::V1::Vehicle::UnloadingPolicy

**Parameter**

  * **value** ([::Google::Cloud::Optimization::V1::Vehicle::UnloadingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-UnloadingPolicy)) — Unloading policy enforced on the vehicle. 



**Returns**

  * ([::Google::Cloud::Optimization::V1::Vehicle::UnloadingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-optimization-v1/latest/Google-Cloud-Optimization-V1-Vehicle-UnloadingPolicy)) — Unloading policy enforced on the vehicle. 



### #used_if_route_is_empty
    
    
    def used_if_route_is_empty() -> ::Boolean

**Returns**

  * (::Boolean) — This field only applies to vehicles when their route does not serve any shipments. It indicates if the vehicle should be considered as used or not in this case.

If true, the vehicle goes from its start to its end location even if it doesn't serve any shipments, and time and distance costs resulting from its start --> end travel are taken into account.

Otherwise, it doesn't travel from its start to its end location, and no `break_rule` or delay (from `TransitionAttributes`) are scheduled for this vehicle. In this case, the vehicle's `ShipmentRoute` doesn't contain any information except for the vehicle index and label. 




### #used_if_route_is_empty=
    
    
    def used_if_route_is_empty=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — This field only applies to vehicles when their route does not serve any shipments. It indicates if the vehicle should be considered as used or not in this case.

If true, the vehicle goes from its start to its end location even if it doesn't serve any shipments, and time and distance costs resulting from its start --> end travel are taken into account.

Otherwise, it doesn't travel from its start to its end location, and no `break_rule` or delay (from `TransitionAttributes`) are scheduled for this vehicle. In this case, the vehicle's `ShipmentRoute` doesn't contain any information except for the vehicle index and label. 




**Returns**

  * (::Boolean) — This field only applies to vehicles when their route does not serve any shipments. It indicates if the vehicle should be considered as used or not in this case.

If true, the vehicle goes from its start to its end location even if it doesn't serve any shipments, and time and distance costs resulting from its start --> end travel are taken into account.

Otherwise, it doesn't travel from its start to its end location, and no `break_rule` or delay (from `TransitionAttributes`) are scheduled for this vehicle. In this case, the vehicle's `ShipmentRoute` doesn't contain any information except for the vehicle index and label. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
