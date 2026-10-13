---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/places/apiv1/placespb/
title: Places API (New) v1 - Package cloud.google.com/go/maps/places/apiv1/placespb (v1.43.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:08.579880+00:00
---

# Places API (New) v1 - Package cloud.google.com/go/maps/places/apiv1/placespb (v1.43.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/places/apiv1/placespb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Places API (New) v1 - Package cloud.google.com/go/maps/places/apiv1/placespb (v1.43.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.43.0 (latest)  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.1  1.20.4  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.0  1.12.1  1.11.7  1.10.0  1.9.0  1.8.0  1.7.3  1.6.4  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.0  0.5.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/maps/places/apiv1/placespb). 

##  Constants 

### Places_SearchNearby_FullMethodName, Places_SearchText_FullMethodName, Places_GetPhotoMedia_FullMethodName, Places_GetPlace_FullMethodName, Places_AutocompletePlaces_FullMethodName
    
    
    const (
    	Places_SearchNearby_FullMethodName       = "/google.maps.places.v1.Places/SearchNearby"
    	Places_SearchText_FullMethodName         = "/google.maps.places.v1.Places/SearchText"
    	Places_GetPhotoMedia_FullMethodName      = "/google.maps.places.v1.Places/GetPhotoMedia"
    	Places_GetPlace_FullMethodName           = "/google.maps.places.v1.Places/GetPlace"
    	Places_AutocompletePlaces_FullMethodName = "/google.maps.places.v1.Places/AutocompletePlaces"
    )

## Variables 

### AddressDescriptor_Landmark_SpatialRelationship_name, AddressDescriptor_Landmark_SpatialRelationship_value
    
    
    var (
    	AddressDescriptor_Landmark_SpatialRelationship_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "NEAR",
    		1: "WITHIN",
    		2: "BESIDE",
    		3: "ACROSS_THE_ROAD",
    		4: "DOWN_THE_ROAD",
    		5: "AROUND_THE_CORNER",
    		6: "BEHIND",
    	}
    	AddressDescriptor_Landmark_SpatialRelationship_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"NEAR":              0,
    		"WITHIN":            1,
    		"BESIDE":            2,
    		"ACROSS_THE_ROAD":   3,
    		"DOWN_THE_ROAD":     4,
    		"AROUND_THE_CORNER": 5,
    		"BEHIND":            6,
    	}
    )

Enum value maps for AddressDescriptor_Landmark_SpatialRelationship.

### AddressDescriptor_Area_Containment_name, AddressDescriptor_Area_Containment_value
    
    
    var (
    	AddressDescriptor_Area_Containment_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CONTAINMENT_UNSPECIFIED",
    		1: "WITHIN",
    		2: "OUTSKIRTS",
    		3: "NEAR",
    	}
    	AddressDescriptor_Area_Containment_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CONTAINMENT_UNSPECIFIED": 0,
    		"WITHIN":                  1,
    		"OUTSKIRTS":               2,
    		"NEAR":                    3,
    	}
    )

Enum value maps for AddressDescriptor_Area_Containment.

### EVConnectorType_name, EVConnectorType_value
    
    
    var (
    	EVConnectorType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "EV_CONNECTOR_TYPE_UNSPECIFIED",
    		1:  "EV_CONNECTOR_TYPE_OTHER",
    		2:  "EV_CONNECTOR_TYPE_J1772",
    		3:  "EV_CONNECTOR_TYPE_TYPE_2",
    		4:  "EV_CONNECTOR_TYPE_CHADEMO",
    		5:  "EV_CONNECTOR_TYPE_CCS_COMBO_1",
    		6:  "EV_CONNECTOR_TYPE_CCS_COMBO_2",
    		7:  "EV_CONNECTOR_TYPE_TESLA",
    		8:  "EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T",
    		9:  "EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET",
    		10: "EV_CONNECTOR_TYPE_NACS",
    	}
    	EVConnectorType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"EV_CONNECTOR_TYPE_UNSPECIFIED":             0,
    		"EV_CONNECTOR_TYPE_OTHER":                   1,
    		"EV_CONNECTOR_TYPE_J1772":                   2,
    		"EV_CONNECTOR_TYPE_TYPE_2":                  3,
    		"EV_CONNECTOR_TYPE_CHADEMO":                 4,
    		"EV_CONNECTOR_TYPE_CCS_COMBO_1":             5,
    		"EV_CONNECTOR_TYPE_CCS_COMBO_2":             6,
    		"EV_CONNECTOR_TYPE_TESLA":                   7,
    		"EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T":        8,
    		"EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET": 9,
    		"EV_CONNECTOR_TYPE_NACS":                    10,
    	}
    )

Enum value maps for EVConnectorType.

### FuelOptions_FuelPrice_FuelType_name, FuelOptions_FuelPrice_FuelType_value
    
    
    var (
    	FuelOptions_FuelPrice_FuelType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "FUEL_TYPE_UNSPECIFIED",
    		1:  "DIESEL",
    		19: "DIESEL_PLUS",
    		2:  "REGULAR_UNLEADED",
    		3:  "MIDGRADE",
    		4:  "PREMIUM",
    		5:  "SP91",
    		6:  "SP91_E10",
    		7:  "SP92",
    		8:  "SP95",
    		9:  "SP95_E10",
    		10: "SP98",
    		11: "SP99",
    		12: "SP100",
    		13: "LPG",
    		14: "E80",
    		15: "E85",
    		20: "E100",
    		16: "METHANE",
    		17: "BIO_DIESEL",
    		18: "TRUCK_DIESEL",
    	}
    	FuelOptions_FuelPrice_FuelType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FUEL_TYPE_UNSPECIFIED": 0,
    		"DIESEL":                1,
    		"DIESEL_PLUS":           19,
    		"REGULAR_UNLEADED":      2,
    		"MIDGRADE":              3,
    		"PREMIUM":               4,
    		"SP91":                  5,
    		"SP91_E10":              6,
    		"SP92":                  7,
    		"SP95":                  8,
    		"SP95_E10":              9,
    		"SP98":                  10,
    		"SP99":                  11,
    		"SP100":                 12,
    		"LPG":                   13,
    		"E80":                   14,
    		"E85":                   15,
    		"E100":                  20,
    		"METHANE":               16,
    		"BIO_DIESEL":            17,
    		"TRUCK_DIESEL":          18,
    	}
    )

Enum value maps for FuelOptions_FuelPrice_FuelType.

### PriceLevel_name, PriceLevel_value
    
    
    var (
    	PriceLevel_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PRICE_LEVEL_UNSPECIFIED",
    		1: "PRICE_LEVEL_FREE",
    		2: "PRICE_LEVEL_INEXPENSIVE",
    		3: "PRICE_LEVEL_MODERATE",
    		4: "PRICE_LEVEL_EXPENSIVE",
    		5: "PRICE_LEVEL_VERY_EXPENSIVE",
    	}
    	PriceLevel_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PRICE_LEVEL_UNSPECIFIED":    0,
    		"PRICE_LEVEL_FREE":           1,
    		"PRICE_LEVEL_INEXPENSIVE":    2,
    		"PRICE_LEVEL_MODERATE":       3,
    		"PRICE_LEVEL_EXPENSIVE":      4,
    		"PRICE_LEVEL_VERY_EXPENSIVE": 5,
    	}
    )

Enum value maps for PriceLevel.

### Place_BusinessStatus_name, Place_BusinessStatus_value
    
    
    var (
    	Place_BusinessStatus_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "BUSINESS_STATUS_UNSPECIFIED",
    		1: "OPERATIONAL",
    		2: "CLOSED_TEMPORARILY",
    		3: "CLOSED_PERMANENTLY",
    		4: "FUTURE_OPENING",
    	}
    	Place_BusinessStatus_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"BUSINESS_STATUS_UNSPECIFIED": 0,
    		"OPERATIONAL":                 1,
    		"CLOSED_TEMPORARILY":          2,
    		"CLOSED_PERMANENTLY":          3,
    		"FUTURE_OPENING":              4,
    	}
    )

Enum value maps for Place_BusinessStatus.

### Place_OpeningHours_SecondaryHoursType_name, Place_OpeningHours_SecondaryHoursType_value
    
    
    var (
    	Place_OpeningHours_SecondaryHoursType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "SECONDARY_HOURS_TYPE_UNSPECIFIED",
    		1:  "DRIVE_THROUGH",
    		2:  "HAPPY_HOUR",
    		3:  "DELIVERY",
    		4:  "TAKEOUT",
    		5:  "KITCHEN",
    		6:  "BREAKFAST",
    		7:  "LUNCH",
    		8:  "DINNER",
    		9:  "BRUNCH",
    		10: "PICKUP",
    		11: "ACCESS",
    		12: "SENIOR_HOURS",
    		13: "ONLINE_SERVICE_HOURS",
    	}
    	Place_OpeningHours_SecondaryHoursType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SECONDARY_HOURS_TYPE_UNSPECIFIED": 0,
    		"DRIVE_THROUGH":                    1,
    		"HAPPY_HOUR":                       2,
    		"DELIVERY":                         3,
    		"TAKEOUT":                          4,
    		"KITCHEN":                          5,
    		"BREAKFAST":                        6,
    		"LUNCH":                            7,
    		"DINNER":                           8,
    		"BRUNCH":                           9,
    		"PICKUP":                           10,
    		"ACCESS":                           11,
    		"SENIOR_HOURS":                     12,
    		"ONLINE_SERVICE_HOURS":             13,
    	}
    )

Enum value maps for Place_OpeningHours_SecondaryHoursType.

### SearchNearbyRequest_RankPreference_name, SearchNearbyRequest_RankPreference_value
    
    
    var (
    	SearchNearbyRequest_RankPreference_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RANK_PREFERENCE_UNSPECIFIED",
    		1: "DISTANCE",
    		2: "POPULARITY",
    	}
    	SearchNearbyRequest_RankPreference_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RANK_PREFERENCE_UNSPECIFIED": 0,
    		"DISTANCE":                    1,
    		"POPULARITY":                  2,
    	}
    )

Enum value maps for SearchNearbyRequest_RankPreference.

### SearchTextRequest_RankPreference_name, SearchTextRequest_RankPreference_value
    
    
    var (
    	SearchTextRequest_RankPreference_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RANK_PREFERENCE_UNSPECIFIED",
    		1: "DISTANCE",
    		2: "RELEVANCE",
    	}
    	SearchTextRequest_RankPreference_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RANK_PREFERENCE_UNSPECIFIED": 0,
    		"DISTANCE":                    1,
    		"RELEVANCE":                   2,
    	}
    )

Enum value maps for SearchTextRequest_RankPreference.

### RoutingPreference_name, RoutingPreference_value
    
    
    var (
    	RoutingPreference_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ROUTING_PREFERENCE_UNSPECIFIED",
    		1: "TRAFFIC_UNAWARE",
    		2: "TRAFFIC_AWARE",
    		3: "TRAFFIC_AWARE_OPTIMAL",
    	}
    	RoutingPreference_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ROUTING_PREFERENCE_UNSPECIFIED": 0,
    		"TRAFFIC_UNAWARE":                1,
    		"TRAFFIC_AWARE":                  2,
    		"TRAFFIC_AWARE_OPTIMAL":          3,
    	}
    )

Enum value maps for RoutingPreference.

### TransitLine_VehicleType_name, TransitLine_VehicleType_value
    
    
    var (
    	TransitLine_VehicleType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "VEHICLE_TYPE_UNSPECIFIED",
    		1:  "RAIL",
    		2:  "METRO_RAIL",
    		3:  "SUBWAY",
    		4:  "TRAM",
    		5:  "MONORAIL",
    		6:  "HEAVY_RAIL",
    		7:  "COMMUTER_TRAIN",
    		8:  "HIGH_SPEED_TRAIN",
    		9:  "LONG_DISTANCE_TRAIN",
    		10: "BUS",
    		11: "INTERCITY_BUS",
    		12: "TROLLEYBUS",
    		13: "SHARE_TAXI",
    		14: "COACH",
    		15: "FERRY",
    		16: "CABLE_CAR",
    		17: "GONDOLA_LIFT",
    		18: "FUNICULAR",
    		19: "SPECIAL",
    		20: "HORSE_CARRIAGE",
    		21: "AIRPLANE",
    	}
    	TransitLine_VehicleType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"VEHICLE_TYPE_UNSPECIFIED": 0,
    		"RAIL":                     1,
    		"METRO_RAIL":               2,
    		"SUBWAY":                   3,
    		"TRAM":                     4,
    		"MONORAIL":                 5,
    		"HEAVY_RAIL":               6,
    		"COMMUTER_TRAIN":           7,
    		"HIGH_SPEED_TRAIN":         8,
    		"LONG_DISTANCE_TRAIN":      9,
    		"BUS":                      10,
    		"INTERCITY_BUS":            11,
    		"TROLLEYBUS":               12,
    		"SHARE_TAXI":               13,
    		"COACH":                    14,
    		"FERRY":                    15,
    		"CABLE_CAR":                16,
    		"GONDOLA_LIFT":             17,
    		"FUNICULAR":                18,
    		"SPECIAL":                  19,
    		"HORSE_CARRIAGE":           20,
    		"AIRPLANE":                 21,
    	}
    )

Enum value maps for TransitLine_VehicleType.

### TravelMode_name, TravelMode_value
    
    
    var (
    	TravelMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TRAVEL_MODE_UNSPECIFIED",
    		1: "DRIVE",
    		2: "BICYCLE",
    		3: "WALK",
    		4: "TWO_WHEELER",
    	}
    	TravelMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TRAVEL_MODE_UNSPECIFIED": 0,
    		"DRIVE":                   1,
    		"BICYCLE":                 2,
    		"WALK":                    3,
    		"TWO_WHEELER":             4,
    	}
    )

Enum value maps for TravelMode.

### File_google_maps_places_v1_address_descriptor_proto
    
    
    var File_google_maps_places_v1_address_descriptor_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_attribution_proto
    
    
    var File_google_maps_places_v1_attribution_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_content_block_proto
    
    
    var File_google_maps_places_v1_content_block_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_contextual_content_proto
    
    
    var File_google_maps_places_v1_contextual_content_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_ev_charging_proto
    
    
    var File_google_maps_places_v1_ev_charging_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_fuel_options_proto
    
    
    var File_google_maps_places_v1_fuel_options_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_geometry_proto
    
    
    var File_google_maps_places_v1_geometry_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_photo_proto
    
    
    var File_google_maps_places_v1_photo_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_place_proto
    
    
    var File_google_maps_places_v1_place_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_places_service_proto
    
    
    var File_google_maps_places_v1_places_service_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_polyline_proto
    
    
    var File_google_maps_places_v1_polyline_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_price_range_proto
    
    
    var File_google_maps_places_v1_price_range_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_reference_proto
    
    
    var File_google_maps_places_v1_reference_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_review_proto
    
    
    var File_google_maps_places_v1_review_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_route_modifiers_proto
    
    
    var File_google_maps_places_v1_route_modifiers_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_routing_preference_proto
    
    
    var File_google_maps_places_v1_routing_preference_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_routing_summary_proto
    
    
    var File_google_maps_places_v1_routing_summary_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_transit_proto
    
    
    var File_google_maps_places_v1_transit_proto protoreflect.FileDescriptor

### File_google_maps_places_v1_travel_mode_proto
    
    
    var File_google_maps_places_v1_travel_mode_proto protoreflect.FileDescriptor

### Places_ServiceDesc
    
    
    var Places_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.maps.places.v1.Places",
    	HandlerType: (*PlacesServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "SearchNearby",
    			Handler:    _Places_SearchNearby_Handler,
    		},
    		{
    			MethodName: "SearchText",
    			Handler:    _Places_SearchText_Handler,
    		},
    		{
    			MethodName: "GetPhotoMedia",
    			Handler:    _Places_GetPhotoMedia_Handler,
    		},
    		{
    			MethodName: "GetPlace",
    			Handler:    _Places_GetPlace_Handler,
    		},
    		{
    			MethodName: "AutocompletePlaces",
    			Handler:    _Places_AutocompletePlaces_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/maps/places/v1/places_service.proto",
    }

Places_ServiceDesc is the grpc.ServiceDesc for Places service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterPlacesServer 
    
    
    func RegisterPlacesServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv PlacesServer)

## AddressDescriptor
    
    
    type AddressDescriptor struct {
    
    	// A ranked list of nearby landmarks. The most recognizable and nearby
    	// landmarks are ranked first.
    	Landmarks []*AddressDescriptor_Landmark `protobuf:"bytes,1,rep,name=landmarks,proto3" json:"landmarks,omitempty"`
    	// A ranked list of containing or adjacent areas. The most recognizable and
    	// precise areas are ranked first.
    	Areas []*AddressDescriptor_Area `protobuf:"bytes,2,rep,name=areas,proto3" json:"areas,omitempty"`
    	// contains filtered or unexported fields
    }

A relational description of a location. Includes a ranked set of nearby landmarks and precise containing areas and their relationship to the target location.

### func (*AddressDescriptor) Descriptor 
    
    
    func (*AddressDescriptor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddressDescriptor.ProtoReflect.Descriptor instead.

### func (*AddressDescriptor) GetAreas 
    
    
    func (x *AddressDescriptor) GetAreas() []*AddressDescriptor_Area

### func (*AddressDescriptor) GetLandmarks 
    
    
    func (x *AddressDescriptor) GetLandmarks() []*AddressDescriptor_Landmark

### func (*AddressDescriptor) ProtoMessage 
    
    
    func (*AddressDescriptor) ProtoMessage()

### func (*AddressDescriptor) ProtoReflect 
    
    
    func (x *AddressDescriptor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AddressDescriptor) Reset 
    
    
    func (x *AddressDescriptor) Reset()

### func (*AddressDescriptor) String 
    
    
    func (x *AddressDescriptor) String() [string](https://pkg.go.dev/builtin#string)

## AddressDescriptor_Area
    
    
    type AddressDescriptor_Area struct {
    
    	// The area's resource name.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The area's place id.
    	PlaceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=place_id,json=placeId,proto3" json:"place_id,omitempty"`
    	// The area's display name.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Defines the spatial relationship between the target location and the
    	// area.
    	Containment AddressDescriptor_Area_Containment `protobuf:"varint,4,opt,name=containment,proto3,enum=google.maps.places.v1.AddressDescriptor_Area_Containment" json:"containment,omitempty"`
    	// contains filtered or unexported fields
    }

Area information and the area's relationship with the target location.

Areas includes precise sublocality, neighborhoods, and large compounds that are useful for describing a location.

### func (*AddressDescriptor_Area) Descriptor 
    
    
    func (*AddressDescriptor_Area) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddressDescriptor_Area.ProtoReflect.Descriptor instead.

### func (*AddressDescriptor_Area) GetContainment 
    
    
    func (x *AddressDescriptor_Area) GetContainment() AddressDescriptor_Area_Containment

### func (*AddressDescriptor_Area) GetDisplayName 
    
    
    func (x *AddressDescriptor_Area) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*AddressDescriptor_Area) GetName 
    
    
    func (x *AddressDescriptor_Area) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AddressDescriptor_Area) GetPlaceId 
    
    
    func (x *AddressDescriptor_Area) GetPlaceId() [string](https://pkg.go.dev/builtin#string)

### func (*AddressDescriptor_Area) ProtoMessage 
    
    
    func (*AddressDescriptor_Area) ProtoMessage()

### func (*AddressDescriptor_Area) ProtoReflect 
    
    
    func (x *AddressDescriptor_Area) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AddressDescriptor_Area) Reset 
    
    
    func (x *AddressDescriptor_Area) Reset()

### func (*AddressDescriptor_Area) String 
    
    
    func (x *AddressDescriptor_Area) String() [string](https://pkg.go.dev/builtin#string)

## AddressDescriptor_Area_Containment
    
    
    type AddressDescriptor_Area_Containment [int32](https://pkg.go.dev/builtin#int32)

Defines the spatial relationship between the target location and the area.

### AddressDescriptor_Area_CONTAINMENT_UNSPECIFIED, AddressDescriptor_Area_WITHIN, AddressDescriptor_Area_OUTSKIRTS, AddressDescriptor_Area_NEAR
    
    
    const (
    	// The containment is unspecified.
    	AddressDescriptor_Area_CONTAINMENT_UNSPECIFIED AddressDescriptor_Area_Containment = 0
    	// The target location is within the area region, close to the
    	// center.
    	AddressDescriptor_Area_WITHIN AddressDescriptor_Area_Containment = 1
    	// The target location is within the area region, close to the edge.
    	AddressDescriptor_Area_OUTSKIRTS AddressDescriptor_Area_Containment = 2
    	// The target location is outside the area region, but close by.
    	AddressDescriptor_Area_NEAR AddressDescriptor_Area_Containment = 3
    )

### func (AddressDescriptor_Area_Containment) Descriptor 
    
    
    func (AddressDescriptor_Area_Containment) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AddressDescriptor_Area_Containment) Enum 
    
    
    func (x AddressDescriptor_Area_Containment) Enum() *AddressDescriptor_Area_Containment

### func (AddressDescriptor_Area_Containment) EnumDescriptor 
    
    
    func (AddressDescriptor_Area_Containment) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddressDescriptor_Area_Containment.Descriptor instead.

### func (AddressDescriptor_Area_Containment) Number 
    
    
    func (x AddressDescriptor_Area_Containment) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AddressDescriptor_Area_Containment) String 
    
    
    func (x AddressDescriptor_Area_Containment) String() [string](https://pkg.go.dev/builtin#string)

### func (AddressDescriptor_Area_Containment) Type 
    
    
    func (AddressDescriptor_Area_Containment) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AddressDescriptor_Landmark
    
    
    type AddressDescriptor_Landmark struct {
    
    	// The landmark's resource name.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The landmark's place id.
    	PlaceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=place_id,json=placeId,proto3" json:"place_id,omitempty"`
    	// The landmark's display name.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A set of type tags for this landmark. For a complete list of possible
    	// values, see
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	Types [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=types,proto3" json:"types,omitempty"`
    	// Defines the spatial relationship between the target location and the
    	// landmark.
    	SpatialRelationship AddressDescriptor_Landmark_SpatialRelationship `protobuf:"varint,5,opt,name=spatial_relationship,json=spatialRelationship,proto3,enum=google.maps.places.v1.AddressDescriptor_Landmark_SpatialRelationship" json:"spatial_relationship,omitempty"`
    	// The straight line distance, in meters, between the center point of the
    	// target and the center point of the landmark. In some situations, this
    	// value can be longer than `travel_distance_meters`.
    	StraightLineDistanceMeters [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,6,opt,name=straight_line_distance_meters,json=straightLineDistanceMeters,proto3" json:"straight_line_distance_meters,omitempty"`
    	// The travel distance, in meters, along the road network from the target to
    	// the landmark, if known. This value does not take into account the mode of
    	// transportation, such as walking, driving, or biking.
    	TravelDistanceMeters *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,7,opt,name=travel_distance_meters,json=travelDistanceMeters,proto3,oneof" json:"travel_distance_meters,omitempty"`
    	// contains filtered or unexported fields
    }

Basic landmark information and the landmark's relationship with the target location.

Landmarks are prominent places that can be used to describe a location.

### func (*AddressDescriptor_Landmark) Descriptor 
    
    
    func (*AddressDescriptor_Landmark) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddressDescriptor_Landmark.ProtoReflect.Descriptor instead.

### func (*AddressDescriptor_Landmark) GetDisplayName 
    
    
    func (x *AddressDescriptor_Landmark) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*AddressDescriptor_Landmark) GetName 
    
    
    func (x *AddressDescriptor_Landmark) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AddressDescriptor_Landmark) GetPlaceId 
    
    
    func (x *AddressDescriptor_Landmark) GetPlaceId() [string](https://pkg.go.dev/builtin#string)

### func (*AddressDescriptor_Landmark) GetSpatialRelationship 
    
    
    func (x *AddressDescriptor_Landmark) GetSpatialRelationship() AddressDescriptor_Landmark_SpatialRelationship

### func (*AddressDescriptor_Landmark) GetStraightLineDistanceMeters 
    
    
    func (x *AddressDescriptor_Landmark) GetStraightLineDistanceMeters() [float32](https://pkg.go.dev/builtin#float32)

### func (*AddressDescriptor_Landmark) GetTravelDistanceMeters 
    
    
    func (x *AddressDescriptor_Landmark) GetTravelDistanceMeters() [float32](https://pkg.go.dev/builtin#float32)

### func (*AddressDescriptor_Landmark) GetTypes 
    
    
    func (x *AddressDescriptor_Landmark) GetTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*AddressDescriptor_Landmark) ProtoMessage 
    
    
    func (*AddressDescriptor_Landmark) ProtoMessage()

### func (*AddressDescriptor_Landmark) ProtoReflect 
    
    
    func (x *AddressDescriptor_Landmark) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AddressDescriptor_Landmark) Reset 
    
    
    func (x *AddressDescriptor_Landmark) Reset()

### func (*AddressDescriptor_Landmark) String 
    
    
    func (x *AddressDescriptor_Landmark) String() [string](https://pkg.go.dev/builtin#string)

## AddressDescriptor_Landmark_SpatialRelationship
    
    
    type AddressDescriptor_Landmark_SpatialRelationship [int32](https://pkg.go.dev/builtin#int32)

Defines the spatial relationship between the target location and the landmark.

### AddressDescriptor_Landmark_NEAR, AddressDescriptor_Landmark_WITHIN, AddressDescriptor_Landmark_BESIDE, AddressDescriptor_Landmark_ACROSS_THE_ROAD, AddressDescriptor_Landmark_DOWN_THE_ROAD, AddressDescriptor_Landmark_AROUND_THE_CORNER, AddressDescriptor_Landmark_BEHIND
    
    
    const (
    	// This is the default relationship when nothing more specific below
    	// applies.
    	AddressDescriptor_Landmark_NEAR AddressDescriptor_Landmark_SpatialRelationship = 0
    	// The landmark has a spatial geometry and the target is within its
    	// bounds.
    	AddressDescriptor_Landmark_WITHIN AddressDescriptor_Landmark_SpatialRelationship = 1
    	// The target is directly adjacent to the landmark.
    	AddressDescriptor_Landmark_BESIDE AddressDescriptor_Landmark_SpatialRelationship = 2
    	// The target is directly opposite the landmark on the other side of the
    	// road.
    	AddressDescriptor_Landmark_ACROSS_THE_ROAD AddressDescriptor_Landmark_SpatialRelationship = 3
    	// On the same route as the landmark but not besides or across.
    	AddressDescriptor_Landmark_DOWN_THE_ROAD AddressDescriptor_Landmark_SpatialRelationship = 4
    	// Not on the same route as the landmark but a single turn away.
    	AddressDescriptor_Landmark_AROUND_THE_CORNER AddressDescriptor_Landmark_SpatialRelationship = 5
    	// Close to the landmark's structure but further away from its street
    	// entrances.
    	AddressDescriptor_Landmark_BEHIND AddressDescriptor_Landmark_SpatialRelationship = 6
    )

### func (AddressDescriptor_Landmark_SpatialRelationship) Descriptor 
    
    
    func (AddressDescriptor_Landmark_SpatialRelationship) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AddressDescriptor_Landmark_SpatialRelationship) Enum 
    
    
    func (x AddressDescriptor_Landmark_SpatialRelationship) Enum() *AddressDescriptor_Landmark_SpatialRelationship

### func (AddressDescriptor_Landmark_SpatialRelationship) EnumDescriptor 
    
    
    func (AddressDescriptor_Landmark_SpatialRelationship) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddressDescriptor_Landmark_SpatialRelationship.Descriptor instead.

### func (AddressDescriptor_Landmark_SpatialRelationship) Number 
    
    
    func (x AddressDescriptor_Landmark_SpatialRelationship) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AddressDescriptor_Landmark_SpatialRelationship) String 
    
    
    func (x AddressDescriptor_Landmark_SpatialRelationship) String() [string](https://pkg.go.dev/builtin#string)

### func (AddressDescriptor_Landmark_SpatialRelationship) Type 
    
    
    func (AddressDescriptor_Landmark_SpatialRelationship) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AuthorAttribution
    
    
    type AuthorAttribution struct {
    
    	// Name of the author of the [Photo][google.maps.places.v1.Photo] or
    	// [Review][google.maps.places.v1.Review].
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// URI of the author of the [Photo][google.maps.places.v1.Photo] or
    	// [Review][google.maps.places.v1.Review].
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Profile photo URI of the author of the
    	// [Photo][google.maps.places.v1.Photo] or
    	// [Review][google.maps.places.v1.Review].
    	PhotoUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=photo_uri,json=photoUri,proto3" json:"photo_uri,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the author of the UGC data. Used in [Photo][google.maps.places.v1.Photo], and [Review][google.maps.places.v1.Review].

### func (*AuthorAttribution) Descriptor 
    
    
    func (*AuthorAttribution) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AuthorAttribution.ProtoReflect.Descriptor instead.

### func (*AuthorAttribution) GetDisplayName 
    
    
    func (x *AuthorAttribution) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*AuthorAttribution) GetPhotoUri 
    
    
    func (x *AuthorAttribution) GetPhotoUri() [string](https://pkg.go.dev/builtin#string)

### func (*AuthorAttribution) GetUri 
    
    
    func (x *AuthorAttribution) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*AuthorAttribution) ProtoMessage 
    
    
    func (*AuthorAttribution) ProtoMessage()

### func (*AuthorAttribution) ProtoReflect 
    
    
    func (x *AuthorAttribution) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AuthorAttribution) Reset 
    
    
    func (x *AuthorAttribution) Reset()

### func (*AuthorAttribution) String 
    
    
    func (x *AuthorAttribution) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesRequest
    
    
    type AutocompletePlacesRequest struct {
    
    	// Required. The text string on which to search.
    	Input [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=input,proto3" json:"input,omitempty"`
    	// Optional. Bias results to a specified location.
    	//
    	// At most one of `location_bias` or `location_restriction` should be set. If
    	// neither are set, the results will be biased by IP address, meaning the IP
    	// address will be mapped to an imprecise location and used as a biasing
    	// signal.
    	LocationBias *AutocompletePlacesRequest_LocationBias `protobuf:"bytes,2,opt,name=location_bias,json=locationBias,proto3" json:"location_bias,omitempty"`
    	// Optional. Restrict results to a specified location.
    	//
    	// At most one of `location_bias` or `location_restriction` should be set. If
    	// neither are set, the results will be biased by IP address, meaning the IP
    	// address will be mapped to an imprecise location and used as a biasing
    	// signal.
    	LocationRestriction *AutocompletePlacesRequest_LocationRestriction `protobuf:"bytes,3,opt,name=location_restriction,json=locationRestriction,proto3" json:"location_restriction,omitempty"`
    	// Optional. Included primary Place type (for example, "restaurant" or
    	// "gas_station") in Place Types
    	// (https://developers.google.com/maps/documentation/places/web-service/place-types),
    	// or only `(regions)`, or only `(cities)`. A Place is only returned if its
    	// primary type is included in this list. Up to 5 values can be specified. If
    	// no types are specified, all Place types are returned.
    	IncludedPrimaryTypes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=included_primary_types,json=includedPrimaryTypes,proto3" json:"included_primary_types,omitempty"`
    	// Optional. Only include results in the specified regions, specified as up to
    	// 15 CLDR two-character region codes. An empty set will not restrict the
    	// results. If both `location_restriction` and `included_region_codes` are
    	// set, the results will be located in the area of intersection.
    	IncludedRegionCodes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=included_region_codes,json=includedRegionCodes,proto3" json:"included_region_codes,omitempty"`
    	// Optional. The language in which to return results. Defaults to en-US. The
    	// results may be in mixed languages if the language used in `input` is
    	// different from `language_code` or if the returned Place does not have a
    	// translation from the local language to `language_code`.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// Optional. The region code, specified as a CLDR two-character region code.
    	// This affects address formatting, result ranking, and may influence what
    	// results are returned. This does not restrict results to the specified
    	// region. To restrict results to a region, use `region_code_restriction`.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Optional. The origin point from which to calculate geodesic distance to the
    	// destination (returned as `distance_meters`). If this value is omitted,
    	// geodesic distance will not be returned.
    	Origin *latlng.LatLng `protobuf:"bytes,8,opt,name=origin,proto3" json:"origin,omitempty"`
    	// Optional. A zero-based Unicode character offset of `input` indicating the
    	// cursor position in `input`. The cursor position may influence what
    	// predictions are returned.
    	//
    	// If empty, defaults to the length of `input`.
    	InputOffset [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,9,opt,name=input_offset,json=inputOffset,proto3" json:"input_offset,omitempty"`
    	// Optional. If true, the response will include both Place and query
    	// predictions. Otherwise the response will only return Place predictions.
    	IncludeQueryPredictions [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,10,opt,name=include_query_predictions,json=includeQueryPredictions,proto3" json:"include_query_predictions,omitempty"`
    	// Optional. A string which identifies an Autocomplete session for billing
    	// purposes. Must be a URL and filename safe base64 string with at most 36
    	// ASCII characters in length. Otherwise an INVALID_ARGUMENT error is
    	// returned.
    	//
    	// The session begins when the user starts typing a query, and concludes when
    	// they select a place and a call to Place Details or Address Validation is
    	// made. Each session can have multiple queries, followed by one Place Details
    	// or Address Validation request. The credentials used for each request within
    	// a session must belong to the same Google Cloud Console project. Once a
    	// session has concluded, the token is no longer valid; your app must generate
    	// a fresh token for each session. If the `session_token` parameter is
    	// omitted, or if you reuse a session token, the session is charged as if no
    	// session token was provided (each request is billed separately).
    	//
    	// We recommend the following guidelines:
    	//
    	//   - Use session tokens for all Place Autocomplete calls.
    	//   - Generate a fresh token for each session. Using a version 4 UUID is
    	//     recommended.
    	//   - Ensure that the credentials used for all Place Autocomplete, Place
    	//     Details, and Address Validation requests within a session belong to the
    	//     same Cloud Console project.
    	//   - Be sure to pass a unique session token for each new session. Using the
    	//     same token for more than one session will result in each request being
    	//     billed individually.
    	SessionToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=session_token,json=sessionToken,proto3" json:"session_token,omitempty"`
    	// Optional. Include pure service area businesses if the field is set to true.
    	// Pure service area business is a business that visits or delivers to
    	// customers directly but does not serve customers at their business address.
    	// For example, businesses like cleaning services or plumbers. Those
    	// businesses do not have a physical address or location on Google Maps.
    	// Places will not return fields including `location`, `plus_code`, and other
    	// location related fields for these businesses.
    	IncludePureServiceAreaBusinesses [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=include_pure_service_area_businesses,json=includePureServiceAreaBusinesses,proto3" json:"include_pure_service_area_businesses,omitempty"`
    	// Optional. If true, include businesses that are not yet open but will open
    	// in the future.
    	IncludeFutureOpeningBusinesses [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,13,opt,name=include_future_opening_businesses,json=includeFutureOpeningBusinesses,proto3" json:"include_future_opening_businesses,omitempty"`
    	// contains filtered or unexported fields
    }

Request proto for AutocompletePlaces.

### func (*AutocompletePlacesRequest) Descriptor 
    
    
    func (*AutocompletePlacesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesRequest.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesRequest) GetIncludeFutureOpeningBusinesses 
    
    
    func (x *AutocompletePlacesRequest) GetIncludeFutureOpeningBusinesses() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutocompletePlacesRequest) GetIncludePureServiceAreaBusinesses 
    
    
    func (x *AutocompletePlacesRequest) GetIncludePureServiceAreaBusinesses() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutocompletePlacesRequest) GetIncludeQueryPredictions 
    
    
    func (x *AutocompletePlacesRequest) GetIncludeQueryPredictions() [bool](https://pkg.go.dev/builtin#bool)

### func (*AutocompletePlacesRequest) GetIncludedPrimaryTypes 
    
    
    func (x *AutocompletePlacesRequest) GetIncludedPrimaryTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) GetIncludedRegionCodes 
    
    
    func (x *AutocompletePlacesRequest) GetIncludedRegionCodes() [][string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) GetInput 
    
    
    func (x *AutocompletePlacesRequest) GetInput() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) GetInputOffset 
    
    
    func (x *AutocompletePlacesRequest) GetInputOffset() [int32](https://pkg.go.dev/builtin#int32)

### func (*AutocompletePlacesRequest) GetLanguageCode 
    
    
    func (x *AutocompletePlacesRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) GetLocationBias 
    
    
    func (x *AutocompletePlacesRequest) GetLocationBias() *AutocompletePlacesRequest_LocationBias

### func (*AutocompletePlacesRequest) GetLocationRestriction 
    
    
    func (x *AutocompletePlacesRequest) GetLocationRestriction() *AutocompletePlacesRequest_LocationRestriction

### func (*AutocompletePlacesRequest) GetOrigin 
    
    
    func (x *AutocompletePlacesRequest) GetOrigin() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*AutocompletePlacesRequest) GetRegionCode 
    
    
    func (x *AutocompletePlacesRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) GetSessionToken 
    
    
    func (x *AutocompletePlacesRequest) GetSessionToken() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesRequest) ProtoMessage 
    
    
    func (*AutocompletePlacesRequest) ProtoMessage()

### func (*AutocompletePlacesRequest) ProtoReflect 
    
    
    func (x *AutocompletePlacesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesRequest) Reset 
    
    
    func (x *AutocompletePlacesRequest) Reset()

### func (*AutocompletePlacesRequest) String 
    
    
    func (x *AutocompletePlacesRequest) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesRequest_LocationBias
    
    
    type AutocompletePlacesRequest_LocationBias struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*AutocompletePlacesRequest_LocationBias_Rectangle
    	//	*AutocompletePlacesRequest_LocationBias_Circle
    	Type isAutocompletePlacesRequest_LocationBias_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The region to search. The results may be biased around the specified region.

### func (*AutocompletePlacesRequest_LocationBias) Descriptor 
    
    
    func (*AutocompletePlacesRequest_LocationBias) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesRequest_LocationBias.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesRequest_LocationBias) GetCircle 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) GetCircle() *Circle

### func (*AutocompletePlacesRequest_LocationBias) GetRectangle 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) GetRectangle() *[viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport).[Viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport#Viewport)

### func (*AutocompletePlacesRequest_LocationBias) GetType 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) GetType() isAutocompletePlacesRequest_LocationBias_Type

### func (*AutocompletePlacesRequest_LocationBias) ProtoMessage 
    
    
    func (*AutocompletePlacesRequest_LocationBias) ProtoMessage()

### func (*AutocompletePlacesRequest_LocationBias) ProtoReflect 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesRequest_LocationBias) Reset 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) Reset()

### func (*AutocompletePlacesRequest_LocationBias) String 
    
    
    func (x *AutocompletePlacesRequest_LocationBias) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesRequest_LocationBias_Circle
    
    
    type AutocompletePlacesRequest_LocationBias_Circle struct {
    	// A circle defined by a center point and radius.
    	Circle *Circle `protobuf:"bytes,2,opt,name=circle,proto3,oneof"`
    }

## AutocompletePlacesRequest_LocationBias_Rectangle
    
    
    type AutocompletePlacesRequest_LocationBias_Rectangle struct {
    	// A viewport defined by a northeast and a southwest corner.
    	Rectangle *viewport.Viewport `protobuf:"bytes,1,opt,name=rectangle,proto3,oneof"`
    }

## AutocompletePlacesRequest_LocationRestriction
    
    
    type AutocompletePlacesRequest_LocationRestriction struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*AutocompletePlacesRequest_LocationRestriction_Rectangle
    	//	*AutocompletePlacesRequest_LocationRestriction_Circle
    	Type isAutocompletePlacesRequest_LocationRestriction_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The region to search. The results will be restricted to the specified region.

### func (*AutocompletePlacesRequest_LocationRestriction) Descriptor 
    
    
    func (*AutocompletePlacesRequest_LocationRestriction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesRequest_LocationRestriction.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesRequest_LocationRestriction) GetCircle 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) GetCircle() *Circle

### func (*AutocompletePlacesRequest_LocationRestriction) GetRectangle 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) GetRectangle() *[viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport).[Viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport#Viewport)

### func (*AutocompletePlacesRequest_LocationRestriction) GetType 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) GetType() isAutocompletePlacesRequest_LocationRestriction_Type

### func (*AutocompletePlacesRequest_LocationRestriction) ProtoMessage 
    
    
    func (*AutocompletePlacesRequest_LocationRestriction) ProtoMessage()

### func (*AutocompletePlacesRequest_LocationRestriction) ProtoReflect 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesRequest_LocationRestriction) Reset 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) Reset()

### func (*AutocompletePlacesRequest_LocationRestriction) String 
    
    
    func (x *AutocompletePlacesRequest_LocationRestriction) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesRequest_LocationRestriction_Circle
    
    
    type AutocompletePlacesRequest_LocationRestriction_Circle struct {
    	// A circle defined by a center point and radius.
    	Circle *Circle `protobuf:"bytes,2,opt,name=circle,proto3,oneof"`
    }

## AutocompletePlacesRequest_LocationRestriction_Rectangle
    
    
    type AutocompletePlacesRequest_LocationRestriction_Rectangle struct {
    	// A viewport defined by a northeast and a southwest corner.
    	Rectangle *viewport.Viewport `protobuf:"bytes,1,opt,name=rectangle,proto3,oneof"`
    }

## AutocompletePlacesResponse
    
    
    type AutocompletePlacesResponse struct {
    
    	// Contains a list of suggestions, ordered in descending order of relevance.
    	Suggestions []*AutocompletePlacesResponse_Suggestion `protobuf:"bytes,1,rep,name=suggestions,proto3" json:"suggestions,omitempty"`
    	// contains filtered or unexported fields
    }

Response proto for AutocompletePlaces.

### func (*AutocompletePlacesResponse) Descriptor 
    
    
    func (*AutocompletePlacesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse) GetSuggestions 
    
    
    func (x *AutocompletePlacesResponse) GetSuggestions() []*AutocompletePlacesResponse_Suggestion

### func (*AutocompletePlacesResponse) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse) ProtoMessage()

### func (*AutocompletePlacesResponse) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse) Reset 
    
    
    func (x *AutocompletePlacesResponse) Reset()

### func (*AutocompletePlacesResponse) String 
    
    
    func (x *AutocompletePlacesResponse) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion
    
    
    type AutocompletePlacesResponse_Suggestion struct {
    
    	// Types that are valid to be assigned to Kind:
    	//
    	//	*AutocompletePlacesResponse_Suggestion_PlacePrediction_
    	//	*AutocompletePlacesResponse_Suggestion_QueryPrediction_
    	Kind isAutocompletePlacesResponse_Suggestion_Kind `protobuf_oneof:"kind"`
    	// contains filtered or unexported fields
    }

An Autocomplete suggestion result.

### func (*AutocompletePlacesResponse_Suggestion) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion) GetKind 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) GetKind() isAutocompletePlacesResponse_Suggestion_Kind

### func (*AutocompletePlacesResponse_Suggestion) GetPlacePrediction 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) GetPlacePrediction() *AutocompletePlacesResponse_Suggestion_PlacePrediction

### func (*AutocompletePlacesResponse_Suggestion) GetQueryPrediction 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) GetQueryPrediction() *AutocompletePlacesResponse_Suggestion_QueryPrediction

### func (*AutocompletePlacesResponse_Suggestion) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) Reset()

### func (*AutocompletePlacesResponse_Suggestion) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion_FormattableText
    
    
    type AutocompletePlacesResponse_Suggestion_FormattableText struct {
    
    	// Text that may be used as is or formatted with `matches`.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// A list of string ranges identifying where the input request matched in
    	// `text`. The ranges can be used to format specific parts of `text`. The
    	// substrings may not be exact matches of `input` if the matching was
    	// determined by criteria other than string matching (for example, spell
    	// corrections or transliterations).
    	//
    	// These values are Unicode character offsets of `text`. The ranges are
    	// guaranteed to be ordered in increasing offset values.
    	Matches []*AutocompletePlacesResponse_Suggestion_StringRange `protobuf:"bytes,2,rep,name=matches,proto3" json:"matches,omitempty"`
    	// contains filtered or unexported fields
    }

Text representing a Place or query prediction. The text may be used as is or formatted.

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion_FormattableText) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion_FormattableText.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) GetMatches 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_FormattableText) GetMatches() []*AutocompletePlacesResponse_Suggestion_StringRange

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) GetText 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_FormattableText) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion_FormattableText) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_FormattableText) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_FormattableText) Reset()

### func (*AutocompletePlacesResponse_Suggestion_FormattableText) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_FormattableText) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion_PlacePrediction
    
    
    type AutocompletePlacesResponse_Suggestion_PlacePrediction struct {
    
    	// The resource name of the suggested Place. This name can be used in
    	// other APIs that accept Place names.
    	Place [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=place,proto3" json:"place,omitempty"`
    	// The unique identifier of the suggested Place. This identifier can be
    	// used in other APIs that accept Place IDs.
    	PlaceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=place_id,json=placeId,proto3" json:"place_id,omitempty"`
    	// Contains the human-readable name for the returned result. For
    	// establishment results, this is usually the business name and address.
    	//
    	// `text` is recommended for developers who wish to show a single UI
    	// element. Developers who wish to show two separate, but related, UI
    	// elements may want to use `structured_format` instead. They are two
    	// different ways to represent a Place prediction. Users should not try to
    	// parse `structured_format` into `text` or vice versa.
    	//
    	// This text may be different from the `display_name` returned by
    	// GetPlace.
    	//
    	// May be in mixed languages if the request `input` and `language_code`
    	// are in different languages or if the Place does not have a translation
    	// from the local language to `language_code`.
    	Text *AutocompletePlacesResponse_Suggestion_FormattableText `protobuf:"bytes,3,opt,name=text,proto3" json:"text,omitempty"`
    	// A breakdown of the Place prediction into main text containing the name
    	// of the Place and secondary text containing additional disambiguating
    	// features (such as a city or region).
    	//
    	// `structured_format` is recommended for developers who wish to show two
    	// separate, but related, UI elements. Developers who wish to show a
    	// single UI element may want to use `text` instead. They are two
    	// different ways to represent a Place prediction. Users should not try to
    	// parse `structured_format` into `text` or vice versa.
    	StructuredFormat *AutocompletePlacesResponse_Suggestion_StructuredFormat `protobuf:"bytes,4,opt,name=structured_format,json=structuredFormat,proto3" json:"structured_format,omitempty"`
    	// List of types that apply to this Place from Table A or Table B in
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	//
    	// A type is a categorization of a Place. Places with shared types will
    	// share similar characteristics.
    	Types [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=types,proto3" json:"types,omitempty"`
    	// The length of the geodesic in meters from `origin` if `origin` is
    	// specified. Certain predictions such as routes may not populate this
    	// field.
    	DistanceMeters [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=distance_meters,json=distanceMeters,proto3" json:"distance_meters,omitempty"`
    	// contains filtered or unexported fields
    }

Prediction results for a Place Autocomplete prediction.

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion_PlacePrediction.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetDistanceMeters 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetDistanceMeters() [int32](https://pkg.go.dev/builtin#int32)

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetPlace 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetPlace() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetPlaceId 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetPlaceId() [string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetStructuredFormat 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetStructuredFormat() *AutocompletePlacesResponse_Suggestion_StructuredFormat

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetText 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetText() *AutocompletePlacesResponse_Suggestion_FormattableText

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) GetTypes 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) GetTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) Reset()

### func (*AutocompletePlacesResponse_Suggestion_PlacePrediction) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_PlacePrediction) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion_PlacePrediction_
    
    
    type AutocompletePlacesResponse_Suggestion_PlacePrediction_ struct {
    	// A prediction for a Place.
    	PlacePrediction *AutocompletePlacesResponse_Suggestion_PlacePrediction `protobuf:"bytes,1,opt,name=place_prediction,json=placePrediction,proto3,oneof"`
    }

## AutocompletePlacesResponse_Suggestion_QueryPrediction
    
    
    type AutocompletePlacesResponse_Suggestion_QueryPrediction struct {
    
    	// The predicted text. This text does not represent a Place, but rather a
    	// text query that could be used in a search endpoint (for example,
    	// Text Search).
    	//
    	// `text` is recommended for developers who wish to show a single UI
    	// element. Developers who wish to show two separate, but related, UI
    	// elements may want to use `structured_format` instead. They are two
    	// different ways to represent a query prediction. Users should not try to
    	// parse `structured_format` into `text` or vice versa.
    	//
    	// May be in mixed languages if the request `input` and `language_code`
    	// are in different languages or if part of the query does not have a
    	// translation from the local language to `language_code`.
    	Text *AutocompletePlacesResponse_Suggestion_FormattableText `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// A breakdown of the query prediction into main text containing the query
    	// and secondary text containing additional disambiguating features (such
    	// as a city or region).
    	//
    	// `structured_format` is recommended for developers who wish to show two
    	// separate, but related, UI elements. Developers who wish to show a
    	// single UI element may want to use `text` instead. They are two
    	// different ways to represent a query prediction. Users should not try to
    	// parse `structured_format` into `text` or vice versa.
    	StructuredFormat *AutocompletePlacesResponse_Suggestion_StructuredFormat `protobuf:"bytes,2,opt,name=structured_format,json=structuredFormat,proto3" json:"structured_format,omitempty"`
    	// contains filtered or unexported fields
    }

Prediction results for a Query Autocomplete prediction.

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion_QueryPrediction.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) GetStructuredFormat 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_QueryPrediction) GetStructuredFormat() *AutocompletePlacesResponse_Suggestion_StructuredFormat

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) GetText 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_QueryPrediction) GetText() *AutocompletePlacesResponse_Suggestion_FormattableText

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_QueryPrediction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_QueryPrediction) Reset()

### func (*AutocompletePlacesResponse_Suggestion_QueryPrediction) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_QueryPrediction) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion_QueryPrediction_
    
    
    type AutocompletePlacesResponse_Suggestion_QueryPrediction_ struct {
    	// A prediction for a query.
    	QueryPrediction *AutocompletePlacesResponse_Suggestion_QueryPrediction `protobuf:"bytes,2,opt,name=query_prediction,json=queryPrediction,proto3,oneof"`
    }

## AutocompletePlacesResponse_Suggestion_StringRange
    
    
    type AutocompletePlacesResponse_Suggestion_StringRange struct {
    
    	// Zero-based offset of the first Unicode character of the string
    	// (inclusive).
    	StartOffset [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=start_offset,json=startOffset,proto3" json:"start_offset,omitempty"`
    	// Zero-based offset of the last Unicode character (exclusive).
    	EndOffset [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=end_offset,json=endOffset,proto3" json:"end_offset,omitempty"`
    	// contains filtered or unexported fields
    }

Identifies a substring within a given text.

### func (*AutocompletePlacesResponse_Suggestion_StringRange) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion_StringRange) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion_StringRange.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion_StringRange) GetEndOffset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StringRange) GetEndOffset() [int32](https://pkg.go.dev/builtin#int32)

### func (*AutocompletePlacesResponse_Suggestion_StringRange) GetStartOffset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StringRange) GetStartOffset() [int32](https://pkg.go.dev/builtin#int32)

### func (*AutocompletePlacesResponse_Suggestion_StringRange) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion_StringRange) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion_StringRange) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StringRange) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion_StringRange) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StringRange) Reset()

### func (*AutocompletePlacesResponse_Suggestion_StringRange) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StringRange) String() [string](https://pkg.go.dev/builtin#string)

## AutocompletePlacesResponse_Suggestion_StructuredFormat
    
    
    type AutocompletePlacesResponse_Suggestion_StructuredFormat struct {
    
    	// Represents the name of the Place or query.
    	MainText *AutocompletePlacesResponse_Suggestion_FormattableText `protobuf:"bytes,1,opt,name=main_text,json=mainText,proto3" json:"main_text,omitempty"`
    	// Represents additional disambiguating features (such as a city or
    	// region) to further identify the Place or refine the query.
    	SecondaryText *AutocompletePlacesResponse_Suggestion_FormattableText `protobuf:"bytes,2,opt,name=secondary_text,json=secondaryText,proto3" json:"secondary_text,omitempty"`
    	// contains filtered or unexported fields
    }

Contains a breakdown of a Place or query prediction into main text and secondary text.

For Place predictions, the main text contains the specific name of the Place. For query predictions, the main text contains the query.

The secondary text contains additional disambiguating features (such as a city or region) to further identify the Place or refine the query.

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) Descriptor 
    
    
    func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutocompletePlacesResponse_Suggestion_StructuredFormat.ProtoReflect.Descriptor instead.

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) GetMainText 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StructuredFormat) GetMainText() *AutocompletePlacesResponse_Suggestion_FormattableText

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) GetSecondaryText 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StructuredFormat) GetSecondaryText() *AutocompletePlacesResponse_Suggestion_FormattableText

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) ProtoMessage 
    
    
    func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) ProtoMessage()

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) ProtoReflect 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StructuredFormat) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) Reset 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StructuredFormat) Reset()

### func (*AutocompletePlacesResponse_Suggestion_StructuredFormat) String 
    
    
    func (x *AutocompletePlacesResponse_Suggestion_StructuredFormat) String() [string](https://pkg.go.dev/builtin#string)

## Circle
    
    
    type Circle struct {
    
    	// Required. Center latitude and longitude.
    	//
    	// The range of latitude must be within [-90.0, 90.0]. The range of the
    	// longitude must be within [-180.0, 180.0].
    	Center *latlng.LatLng `protobuf:"bytes,1,opt,name=center,proto3" json:"center,omitempty"`
    	// Required. Radius measured in meters. The radius must be within [0.0,
    	// 50000.0].
    	Radius [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=radius,proto3" json:"radius,omitempty"`
    	// contains filtered or unexported fields
    }

Circle with a LatLng as center and radius.

### func (*Circle) Descriptor 
    
    
    func (*Circle) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Circle.ProtoReflect.Descriptor instead.

### func (*Circle) GetCenter 
    
    
    func (x *Circle) GetCenter() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*Circle) GetRadius 
    
    
    func (x *Circle) GetRadius() [float64](https://pkg.go.dev/builtin#float64)

### func (*Circle) ProtoMessage 
    
    
    func (*Circle) ProtoMessage()

### func (*Circle) ProtoReflect 
    
    
    func (x *Circle) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Circle) Reset 
    
    
    func (x *Circle) Reset()

### func (*Circle) String 
    
    
    func (x *Circle) String() [string](https://pkg.go.dev/builtin#string)

## ContentBlock
    
    
    type ContentBlock struct {
    
    	// Content related to the topic.
    	Content *localized_text.LocalizedText `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
    	// The list of resource names of the referenced places. This name can be used
    	// in other APIs that accept Place resource names.
    	ReferencedPlaces [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=referenced_places,json=referencedPlaces,proto3" json:"referenced_places,omitempty"`
    	// contains filtered or unexported fields
    }

A block of content that can be served individually.

### func (*ContentBlock) Descriptor 
    
    
    func (*ContentBlock) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContentBlock.ProtoReflect.Descriptor instead.

### func (*ContentBlock) GetContent 
    
    
    func (x *ContentBlock) GetContent() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*ContentBlock) GetReferencedPlaces 
    
    
    func (x *ContentBlock) GetReferencedPlaces() [][string](https://pkg.go.dev/builtin#string)

### func (*ContentBlock) ProtoMessage 
    
    
    func (*ContentBlock) ProtoMessage()

### func (*ContentBlock) ProtoReflect 
    
    
    func (x *ContentBlock) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContentBlock) Reset 
    
    
    func (x *ContentBlock) Reset()

### func (*ContentBlock) String 
    
    
    func (x *ContentBlock) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent
    
    
    type ContextualContent struct {
    
    	// List of reviews about this place, contextual to the place query.
    	Reviews []*Review `protobuf:"bytes,1,rep,name=reviews,proto3" json:"reviews,omitempty"`
    	// Information (including references) about photos of this place, contextual
    	// to the place query.
    	Photos []*Photo `protobuf:"bytes,2,rep,name=photos,proto3" json:"photos,omitempty"`
    	// Experimental: See
    	// https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    	// for more details.
    	//
    	// Justifications for the place.
    	Justifications []*ContextualContent_Justification `protobuf:"bytes,3,rep,name=justifications,proto3" json:"justifications,omitempty"`
    	// contains filtered or unexported fields
    }

Experimental: See <https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative> for more details.

Content that is contextual to the place query.

### func (*ContextualContent) Descriptor 
    
    
    func (*ContextualContent) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent.ProtoReflect.Descriptor instead.

### func (*ContextualContent) GetJustifications 
    
    
    func (x *ContextualContent) GetJustifications() []*ContextualContent_Justification

### func (*ContextualContent) GetPhotos 
    
    
    func (x *ContextualContent) GetPhotos() []*Photo

### func (*ContextualContent) GetReviews 
    
    
    func (x *ContextualContent) GetReviews() []*Review

### func (*ContextualContent) ProtoMessage 
    
    
    func (*ContextualContent) ProtoMessage()

### func (*ContextualContent) ProtoReflect 
    
    
    func (x *ContextualContent) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent) Reset 
    
    
    func (x *ContextualContent) Reset()

### func (*ContextualContent) String 
    
    
    func (x *ContextualContent) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent_Justification
    
    
    type ContextualContent_Justification struct {
    
    	// Types that are valid to be assigned to Justification:
    	//
    	//	*ContextualContent_Justification_ReviewJustification_
    	//	*ContextualContent_Justification_BusinessAvailabilityAttributesJustification_
    	Justification isContextualContent_Justification_Justification `protobuf_oneof:"justification"`
    	// contains filtered or unexported fields
    }

Experimental: See <https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative> for more details.

Justifications for the place. Justifications answers the question of why a place could interest an end user.

### func (*ContextualContent_Justification) Descriptor 
    
    
    func (*ContextualContent_Justification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent_Justification.ProtoReflect.Descriptor instead.

### func (*ContextualContent_Justification) GetBusinessAvailabilityAttributesJustification 
    
    
    func (x *ContextualContent_Justification) GetBusinessAvailabilityAttributesJustification() *ContextualContent_Justification_BusinessAvailabilityAttributesJustification

### func (*ContextualContent_Justification) GetJustification 
    
    
    func (x *ContextualContent_Justification) GetJustification() isContextualContent_Justification_Justification

### func (*ContextualContent_Justification) GetReviewJustification 
    
    
    func (x *ContextualContent_Justification) GetReviewJustification() *ContextualContent_Justification_ReviewJustification

### func (*ContextualContent_Justification) ProtoMessage 
    
    
    func (*ContextualContent_Justification) ProtoMessage()

### func (*ContextualContent_Justification) ProtoReflect 
    
    
    func (x *ContextualContent_Justification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent_Justification) Reset 
    
    
    func (x *ContextualContent_Justification) Reset()

### func (*ContextualContent_Justification) String 
    
    
    func (x *ContextualContent_Justification) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent_Justification_BusinessAvailabilityAttributesJustification
    
    
    type ContextualContent_Justification_BusinessAvailabilityAttributesJustification struct {
    
    	// If a place provides takeout.
    	Takeout [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=takeout,proto3" json:"takeout,omitempty"`
    	// If a place provides delivery.
    	Delivery [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=delivery,proto3" json:"delivery,omitempty"`
    	// If a place provides dine-in.
    	DineIn [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=dine_in,json=dineIn,proto3" json:"dine_in,omitempty"`
    	// contains filtered or unexported fields
    }

Experimental: See <https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative> for more details. BusinessAvailabilityAttributes justifications. This shows some attributes a business has that could interest an end user.

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) Descriptor 
    
    
    func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent_Justification_BusinessAvailabilityAttributesJustification.ProtoReflect.Descriptor instead.

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetDelivery 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetDelivery() [bool](https://pkg.go.dev/builtin#bool)

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetDineIn 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetDineIn() [bool](https://pkg.go.dev/builtin#bool)

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetTakeout 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) GetTakeout() [bool](https://pkg.go.dev/builtin#bool)

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) ProtoMessage 
    
    
    func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) ProtoMessage()

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) ProtoReflect 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) Reset 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) Reset()

### func (*ContextualContent_Justification_BusinessAvailabilityAttributesJustification) String 
    
    
    func (x *ContextualContent_Justification_BusinessAvailabilityAttributesJustification) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent_Justification_BusinessAvailabilityAttributesJustification_
    
    
    type ContextualContent_Justification_BusinessAvailabilityAttributesJustification_ struct {
    	// Experimental: See
    	// https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    	// for more details.
    	BusinessAvailabilityAttributesJustification *ContextualContent_Justification_BusinessAvailabilityAttributesJustification `protobuf:"bytes,2,opt,name=business_availability_attributes_justification,json=businessAvailabilityAttributesJustification,proto3,oneof"`
    }

## ContextualContent_Justification_ReviewJustification
    
    
    type ContextualContent_Justification_ReviewJustification struct {
    	HighlightedText *ContextualContent_Justification_ReviewJustification_HighlightedText `protobuf:"bytes,1,opt,name=highlighted_text,json=highlightedText,proto3" json:"highlighted_text,omitempty"`
    	// The review that the highlighted text is generated from.
    	Review *Review `protobuf:"bytes,2,opt,name=review,proto3" json:"review,omitempty"`
    	// contains filtered or unexported fields
    }

Experimental: See <https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative> for more details.

User review justifications. This highlights a section of the user review that would interest an end user. For instance, if the search query is "firewood pizza", the review justification highlights the text relevant to the search query.

### func (*ContextualContent_Justification_ReviewJustification) Descriptor 
    
    
    func (*ContextualContent_Justification_ReviewJustification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent_Justification_ReviewJustification.ProtoReflect.Descriptor instead.

### func (*ContextualContent_Justification_ReviewJustification) GetHighlightedText 
    
    
    func (x *ContextualContent_Justification_ReviewJustification) GetHighlightedText() *ContextualContent_Justification_ReviewJustification_HighlightedText

### func (*ContextualContent_Justification_ReviewJustification) GetReview 
    
    
    func (x *ContextualContent_Justification_ReviewJustification) GetReview() *Review

### func (*ContextualContent_Justification_ReviewJustification) ProtoMessage 
    
    
    func (*ContextualContent_Justification_ReviewJustification) ProtoMessage()

### func (*ContextualContent_Justification_ReviewJustification) ProtoReflect 
    
    
    func (x *ContextualContent_Justification_ReviewJustification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent_Justification_ReviewJustification) Reset 
    
    
    func (x *ContextualContent_Justification_ReviewJustification) Reset()

### func (*ContextualContent_Justification_ReviewJustification) String 
    
    
    func (x *ContextualContent_Justification_ReviewJustification) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent_Justification_ReviewJustification_
    
    
    type ContextualContent_Justification_ReviewJustification_ struct {
    	// Experimental: See
    	// https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    	// for more details.
    	ReviewJustification *ContextualContent_Justification_ReviewJustification `protobuf:"bytes,1,opt,name=review_justification,json=reviewJustification,proto3,oneof"`
    }

## ContextualContent_Justification_ReviewJustification_HighlightedText
    
    
    type ContextualContent_Justification_ReviewJustification_HighlightedText struct {
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// The list of the ranges of the highlighted text.
    	HighlightedTextRanges []*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange `protobuf:"bytes,2,rep,name=highlighted_text_ranges,json=highlightedTextRanges,proto3" json:"highlighted_text_ranges,omitempty"`
    	// contains filtered or unexported fields
    }

The text highlighted by the justification. This is a subset of the review itself. The exact word to highlight is marked by the HighlightedTextRange. There could be several words in the text being highlighted.

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) Descriptor 
    
    
    func (*ContextualContent_Justification_ReviewJustification_HighlightedText) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent_Justification_ReviewJustification_HighlightedText.ProtoReflect.Descriptor instead.

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) GetHighlightedTextRanges 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText) GetHighlightedTextRanges() []*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) GetText 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) ProtoMessage 
    
    
    func (*ContextualContent_Justification_ReviewJustification_HighlightedText) ProtoMessage()

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) ProtoReflect 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) Reset 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText) Reset()

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText) String 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText) String() [string](https://pkg.go.dev/builtin#string)

## ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange
    
    
    type ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange struct {
    	StartIndex [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=start_index,json=startIndex,proto3" json:"start_index,omitempty"`
    	EndIndex   [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=end_index,json=endIndex,proto3" json:"end_index,omitempty"`
    	// contains filtered or unexported fields
    }

The range of highlighted text.

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) Descriptor 
    
    
    func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange.ProtoReflect.Descriptor instead.

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) GetEndIndex 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) GetEndIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) GetStartIndex 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) GetStartIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) ProtoMessage 
    
    
    func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) ProtoMessage()

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) ProtoReflect 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) Reset 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) Reset()

### func (*ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) String 
    
    
    func (x *ContextualContent_Justification_ReviewJustification_HighlightedText_HighlightedTextRange) String() [string](https://pkg.go.dev/builtin#string)

## EVChargeOptions
    
    
    type EVChargeOptions struct {
    
    	// Number of connectors at this station. However, because some ports can have
    	// multiple connectors but only be able to charge one car at a time (e.g.) the
    	// number of connectors may be greater than the total number of cars which can
    	// charge simultaneously.
    	ConnectorCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=connector_count,json=connectorCount,proto3" json:"connector_count,omitempty"`
    	// A list of EV charging connector aggregations that contain connectors of the
    	// same type and same charge rate.
    	ConnectorAggregation []*EVChargeOptions_ConnectorAggregation `protobuf:"bytes,2,rep,name=connector_aggregation,json=connectorAggregation,proto3" json:"connector_aggregation,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the EV Charge Station hosted in Place. Terminology follows <https://afdc.energy.gov/fuels/electricity_infrastructure.html> One port could charge one car at a time. One port has one or more connectors. One station has one or more ports.

### func (*EVChargeOptions) Descriptor 
    
    
    func (*EVChargeOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EVChargeOptions.ProtoReflect.Descriptor instead.

### func (*EVChargeOptions) GetConnectorAggregation 
    
    
    func (x *EVChargeOptions) GetConnectorAggregation() []*EVChargeOptions_ConnectorAggregation

### func (*EVChargeOptions) GetConnectorCount 
    
    
    func (x *EVChargeOptions) GetConnectorCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*EVChargeOptions) ProtoMessage 
    
    
    func (*EVChargeOptions) ProtoMessage()

### func (*EVChargeOptions) ProtoReflect 
    
    
    func (x *EVChargeOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EVChargeOptions) Reset 
    
    
    func (x *EVChargeOptions) Reset()

### func (*EVChargeOptions) String 
    
    
    func (x *EVChargeOptions) String() [string](https://pkg.go.dev/builtin#string)

## EVChargeOptions_ConnectorAggregation
    
    
    type EVChargeOptions_ConnectorAggregation struct {
    
    	// The connector type of this aggregation.
    	Type EVConnectorType `protobuf:"varint,1,opt,name=type,proto3,enum=google.maps.places.v1.EVConnectorType" json:"type,omitempty"`
    	// The static max charging rate in kw of each connector in the aggregation.
    	MaxChargeRateKw [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=max_charge_rate_kw,json=maxChargeRateKw,proto3" json:"max_charge_rate_kw,omitempty"`
    	// Number of connectors in this aggregation.
    	Count [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=count,proto3" json:"count,omitempty"`
    	// Number of connectors in this aggregation that are currently available.
    	AvailableCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=available_count,json=availableCount,proto3,oneof" json:"available_count,omitempty"`
    	// Number of connectors in this aggregation that are currently out of
    	// service.
    	OutOfServiceCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=out_of_service_count,json=outOfServiceCount,proto3,oneof" json:"out_of_service_count,omitempty"`
    	// The timestamp when the connector availability information in this
    	// aggregation was last updated.
    	AvailabilityLastUpdateTime *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=availability_last_update_time,json=availabilityLastUpdateTime,proto3" json:"availability_last_update_time,omitempty"`
    	// contains filtered or unexported fields
    }

EV charging information grouped by [type, max_charge_rate_kw]. Shows EV charge aggregation of connectors that have the same type and max charge rate in kw.

### func (*EVChargeOptions_ConnectorAggregation) Descriptor 
    
    
    func (*EVChargeOptions_ConnectorAggregation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EVChargeOptions_ConnectorAggregation.ProtoReflect.Descriptor instead.

### func (*EVChargeOptions_ConnectorAggregation) GetAvailabilityLastUpdateTime 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetAvailabilityLastUpdateTime() *timestamppb.Timestamp

### func (*EVChargeOptions_ConnectorAggregation) GetAvailableCount 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetAvailableCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*EVChargeOptions_ConnectorAggregation) GetCount 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*EVChargeOptions_ConnectorAggregation) GetMaxChargeRateKw 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetMaxChargeRateKw() [float64](https://pkg.go.dev/builtin#float64)

### func (*EVChargeOptions_ConnectorAggregation) GetOutOfServiceCount 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetOutOfServiceCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*EVChargeOptions_ConnectorAggregation) GetType 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) GetType() EVConnectorType

### func (*EVChargeOptions_ConnectorAggregation) ProtoMessage 
    
    
    func (*EVChargeOptions_ConnectorAggregation) ProtoMessage()

### func (*EVChargeOptions_ConnectorAggregation) ProtoReflect 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EVChargeOptions_ConnectorAggregation) Reset 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) Reset()

### func (*EVChargeOptions_ConnectorAggregation) String 
    
    
    func (x *EVChargeOptions_ConnectorAggregation) String() [string](https://pkg.go.dev/builtin#string)

## EVConnectorType
    
    
    type EVConnectorType [int32](https://pkg.go.dev/builtin#int32)

See <http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6872107> for additional information/context on EV charging connector types.

### EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED, EVConnectorType_EV_CONNECTOR_TYPE_OTHER, EVConnectorType_EV_CONNECTOR_TYPE_J1772, EVConnectorType_EV_CONNECTOR_TYPE_TYPE_2, EVConnectorType_EV_CONNECTOR_TYPE_CHADEMO, EVConnectorType_EV_CONNECTOR_TYPE_CCS_COMBO_1, EVConnectorType_EV_CONNECTOR_TYPE_CCS_COMBO_2, EVConnectorType_EV_CONNECTOR_TYPE_TESLA, EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T, EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET, EVConnectorType_EV_CONNECTOR_TYPE_NACS
    
    
    const (
    	// Unspecified connector.
    	EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED EVConnectorType = 0
    	// Other connector types.
    	EVConnectorType_EV_CONNECTOR_TYPE_OTHER EVConnectorType = 1
    	// J1772 type 1 connector.
    	EVConnectorType_EV_CONNECTOR_TYPE_J1772 EVConnectorType = 2
    	// IEC 62196 type 2 connector. Often referred to as MENNEKES.
    	EVConnectorType_EV_CONNECTOR_TYPE_TYPE_2 EVConnectorType = 3
    	// CHAdeMO type connector.
    	EVConnectorType_EV_CONNECTOR_TYPE_CHADEMO EVConnectorType = 4
    	// Combined Charging System (AC and DC). Based on SAE.
    	//
    	//	Type-1 J-1772 connector
    	EVConnectorType_EV_CONNECTOR_TYPE_CCS_COMBO_1 EVConnectorType = 5
    	// Combined Charging System (AC and DC). Based on Type-2
    	// Mennekes connector
    	EVConnectorType_EV_CONNECTOR_TYPE_CCS_COMBO_2 EVConnectorType = 6
    	// The generic TESLA connector. This is NACS in the North America but can be
    	// non-NACS in other parts of the world (e.g. CCS Combo 2 (CCS2) or GB/T).
    	// This value is less representative of an actual connector type, and more
    	// represents the ability to charge a Tesla brand vehicle at a Tesla owned
    	// charging station.
    	EVConnectorType_EV_CONNECTOR_TYPE_TESLA EVConnectorType = 7
    	// GB/T type corresponds to the GB/T standard in China. This type covers all
    	// GB_T types.
    	EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T EVConnectorType = 8
    	// Unspecified wall outlet.
    	EVConnectorType_EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET EVConnectorType = 9
    	// The North American Charging System (NACS), standardized as SAE J3400.
    	EVConnectorType_EV_CONNECTOR_TYPE_NACS EVConnectorType = 10
    )

### func (EVConnectorType) Descriptor 
    
    
    func (EVConnectorType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (EVConnectorType) Enum 
    
    
    func (x EVConnectorType) Enum() *EVConnectorType

### func (EVConnectorType) EnumDescriptor 
    
    
    func (EVConnectorType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EVConnectorType.Descriptor instead.

### func (EVConnectorType) Number 
    
    
    func (x EVConnectorType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (EVConnectorType) String 
    
    
    func (x EVConnectorType) String() [string](https://pkg.go.dev/builtin#string)

### func (EVConnectorType) Type 
    
    
    func (EVConnectorType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## FuelOptions
    
    
    type FuelOptions struct {
    
    	// The last known fuel price for each type of fuel this station has. There is
    	// one entry per fuel type this station has. Order is not important.
    	FuelPrices []*FuelOptions_FuelPrice `protobuf:"bytes,1,rep,name=fuel_prices,json=fuelPrices,proto3" json:"fuel_prices,omitempty"`
    	// contains filtered or unexported fields
    }

The most recent information about fuel options in a gas station. This information is updated regularly.

### func (*FuelOptions) Descriptor 
    
    
    func (*FuelOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FuelOptions.ProtoReflect.Descriptor instead.

### func (*FuelOptions) GetFuelPrices 
    
    
    func (x *FuelOptions) GetFuelPrices() []*FuelOptions_FuelPrice

### func (*FuelOptions) ProtoMessage 
    
    
    func (*FuelOptions) ProtoMessage()

### func (*FuelOptions) ProtoReflect 
    
    
    func (x *FuelOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FuelOptions) Reset 
    
    
    func (x *FuelOptions) Reset()

### func (*FuelOptions) String 
    
    
    func (x *FuelOptions) String() [string](https://pkg.go.dev/builtin#string)

## FuelOptions_FuelPrice
    
    
    type FuelOptions_FuelPrice struct {
    
    	// The type of fuel.
    	Type FuelOptions_FuelPrice_FuelType `protobuf:"varint,1,opt,name=type,proto3,enum=google.maps.places.v1.FuelOptions_FuelPrice_FuelType" json:"type,omitempty"`
    	// The price of the fuel.
    	Price *money.Money `protobuf:"bytes,2,opt,name=price,proto3" json:"price,omitempty"`
    	// The time the fuel price was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// contains filtered or unexported fields
    }

Fuel price information for a given type.

### func (*FuelOptions_FuelPrice) Descriptor 
    
    
    func (*FuelOptions_FuelPrice) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FuelOptions_FuelPrice.ProtoReflect.Descriptor instead.

### func (*FuelOptions_FuelPrice) GetPrice 
    
    
    func (x *FuelOptions_FuelPrice) GetPrice() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*FuelOptions_FuelPrice) GetType 
    
    
    func (x *FuelOptions_FuelPrice) GetType() FuelOptions_FuelPrice_FuelType

### func (*FuelOptions_FuelPrice) GetUpdateTime 
    
    
    func (x *FuelOptions_FuelPrice) GetUpdateTime() *timestamppb.Timestamp

### func (*FuelOptions_FuelPrice) ProtoMessage 
    
    
    func (*FuelOptions_FuelPrice) ProtoMessage()

### func (*FuelOptions_FuelPrice) ProtoReflect 
    
    
    func (x *FuelOptions_FuelPrice) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FuelOptions_FuelPrice) Reset 
    
    
    func (x *FuelOptions_FuelPrice) Reset()

### func (*FuelOptions_FuelPrice) String 
    
    
    func (x *FuelOptions_FuelPrice) String() [string](https://pkg.go.dev/builtin#string)

## FuelOptions_FuelPrice_FuelType
    
    
    type FuelOptions_FuelPrice_FuelType [int32](https://pkg.go.dev/builtin#int32)

Types of fuel.

### FuelOptions_FuelPrice_FUEL_TYPE_UNSPECIFIED, FuelOptions_FuelPrice_DIESEL, FuelOptions_FuelPrice_DIESEL_PLUS, FuelOptions_FuelPrice_REGULAR_UNLEADED, FuelOptions_FuelPrice_MIDGRADE, FuelOptions_FuelPrice_PREMIUM, FuelOptions_FuelPrice_SP91, FuelOptions_FuelPrice_SP91_E10, FuelOptions_FuelPrice_SP92, FuelOptions_FuelPrice_SP95, FuelOptions_FuelPrice_SP95_E10, FuelOptions_FuelPrice_SP98, FuelOptions_FuelPrice_SP99, FuelOptions_FuelPrice_SP100, FuelOptions_FuelPrice_LPG, FuelOptions_FuelPrice_E80, FuelOptions_FuelPrice_E85, FuelOptions_FuelPrice_E100, FuelOptions_FuelPrice_METHANE, FuelOptions_FuelPrice_BIO_DIESEL, FuelOptions_FuelPrice_TRUCK_DIESEL
    
    
    const (
    	// Unspecified fuel type.
    	FuelOptions_FuelPrice_FUEL_TYPE_UNSPECIFIED FuelOptions_FuelPrice_FuelType = 0
    	// Diesel fuel.
    	FuelOptions_FuelPrice_DIESEL FuelOptions_FuelPrice_FuelType = 1
    	// Diesel plus fuel.
    	FuelOptions_FuelPrice_DIESEL_PLUS FuelOptions_FuelPrice_FuelType = 19
    	// Regular unleaded.
    	FuelOptions_FuelPrice_REGULAR_UNLEADED FuelOptions_FuelPrice_FuelType = 2
    	// Midgrade.
    	FuelOptions_FuelPrice_MIDGRADE FuelOptions_FuelPrice_FuelType = 3
    	// Premium.
    	FuelOptions_FuelPrice_PREMIUM FuelOptions_FuelPrice_FuelType = 4
    	// SP 91.
    	FuelOptions_FuelPrice_SP91 FuelOptions_FuelPrice_FuelType = 5
    	// SP 91 E10.
    	FuelOptions_FuelPrice_SP91_E10 FuelOptions_FuelPrice_FuelType = 6
    	// SP 92.
    	FuelOptions_FuelPrice_SP92 FuelOptions_FuelPrice_FuelType = 7
    	// SP 95.
    	FuelOptions_FuelPrice_SP95 FuelOptions_FuelPrice_FuelType = 8
    	// SP95 E10.
    	FuelOptions_FuelPrice_SP95_E10 FuelOptions_FuelPrice_FuelType = 9
    	// SP 98.
    	FuelOptions_FuelPrice_SP98 FuelOptions_FuelPrice_FuelType = 10
    	// SP 99.
    	FuelOptions_FuelPrice_SP99 FuelOptions_FuelPrice_FuelType = 11
    	// SP 100.
    	FuelOptions_FuelPrice_SP100 FuelOptions_FuelPrice_FuelType = 12
    	// Liquefied Petroleum Gas.
    	FuelOptions_FuelPrice_LPG FuelOptions_FuelPrice_FuelType = 13
    	// E 80.
    	FuelOptions_FuelPrice_E80 FuelOptions_FuelPrice_FuelType = 14
    	// E 85.
    	FuelOptions_FuelPrice_E85 FuelOptions_FuelPrice_FuelType = 15
    	// E 100.
    	FuelOptions_FuelPrice_E100 FuelOptions_FuelPrice_FuelType = 20
    	// Methane.
    	FuelOptions_FuelPrice_METHANE FuelOptions_FuelPrice_FuelType = 16
    	// Bio-diesel.
    	FuelOptions_FuelPrice_BIO_DIESEL FuelOptions_FuelPrice_FuelType = 17
    	// Truck diesel.
    	FuelOptions_FuelPrice_TRUCK_DIESEL FuelOptions_FuelPrice_FuelType = 18
    )

### func (FuelOptions_FuelPrice_FuelType) Descriptor 
    
    
    func (FuelOptions_FuelPrice_FuelType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (FuelOptions_FuelPrice_FuelType) Enum 
    
    
    func (x FuelOptions_FuelPrice_FuelType) Enum() *FuelOptions_FuelPrice_FuelType

### func (FuelOptions_FuelPrice_FuelType) EnumDescriptor 
    
    
    func (FuelOptions_FuelPrice_FuelType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FuelOptions_FuelPrice_FuelType.Descriptor instead.

### func (FuelOptions_FuelPrice_FuelType) Number 
    
    
    func (x FuelOptions_FuelPrice_FuelType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (FuelOptions_FuelPrice_FuelType) String 
    
    
    func (x FuelOptions_FuelPrice_FuelType) String() [string](https://pkg.go.dev/builtin#string)

### func (FuelOptions_FuelPrice_FuelType) Type 
    
    
    func (FuelOptions_FuelPrice_FuelType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GetPhotoMediaRequest
    
    
    type GetPhotoMediaRequest struct {
    
    	// Required. The resource name of a photo media in the format:
    	// `places/{place_id}/photos/{photo_reference}/media`.
    	//
    	// The resource name of a photo as returned in a Place object's `photos.name`
    	// field comes with the format
    	// `places/{place_id}/photos/{photo_reference}`. You need to append `/media`
    	// at the end of the photo resource to get the photo media resource name.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Specifies the maximum desired width, in pixels, of the image. If
    	// the image is smaller than the values specified, the original image will be
    	// returned. If the image is larger in either dimension, it will be scaled to
    	// match the smaller of the two dimensions, restricted to its original aspect
    	// ratio. Both the max_height_px and max_width_px properties accept an integer
    	// between 1 and 4800, inclusively. If the value is not within the allowed
    	// range, an INVALID_ARGUMENT error will be returned.
    	//
    	// At least one of max_height_px or max_width_px needs to be specified. If
    	// neither max_height_px nor max_width_px is specified, an INVALID_ARGUMENT
    	// error will be returned.
    	MaxWidthPx [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=max_width_px,json=maxWidthPx,proto3" json:"max_width_px,omitempty"`
    	// Optional. Specifies the maximum desired height, in pixels, of the image. If
    	// the image is smaller than the values specified, the original image will be
    	// returned. If the image is larger in either dimension, it will be scaled to
    	// match the smaller of the two dimensions, restricted to its original aspect
    	// ratio. Both the max_height_px and max_width_px properties accept an integer
    	// between 1 and 4800, inclusively. If the value is not within the allowed
    	// range, an INVALID_ARGUMENT error will be returned.
    	//
    	// At least one of max_height_px or max_width_px needs to be specified. If
    	// neither max_height_px nor max_width_px is specified, an INVALID_ARGUMENT
    	// error will be returned.
    	MaxHeightPx [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=max_height_px,json=maxHeightPx,proto3" json:"max_height_px,omitempty"`
    	// Optional. If set, skip the default HTTP redirect behavior and render a text
    	// format (for example, in JSON format for HTTP use case) response. If not
    	// set, an HTTP redirect will be issued to redirect the call to the image
    	// media. This option is ignored for non-HTTP requests.
    	SkipHttpRedirect [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=skip_http_redirect,json=skipHttpRedirect,proto3" json:"skip_http_redirect,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching a photo of a place using a photo resource name.

### func (*GetPhotoMediaRequest) Descriptor 
    
    
    func (*GetPhotoMediaRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPhotoMediaRequest.ProtoReflect.Descriptor instead.

### func (*GetPhotoMediaRequest) GetMaxHeightPx 
    
    
    func (x *GetPhotoMediaRequest) GetMaxHeightPx() [int32](https://pkg.go.dev/builtin#int32)

### func (*GetPhotoMediaRequest) GetMaxWidthPx 
    
    
    func (x *GetPhotoMediaRequest) GetMaxWidthPx() [int32](https://pkg.go.dev/builtin#int32)

### func (*GetPhotoMediaRequest) GetName 
    
    
    func (x *GetPhotoMediaRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetPhotoMediaRequest) GetSkipHttpRedirect 
    
    
    func (x *GetPhotoMediaRequest) GetSkipHttpRedirect() [bool](https://pkg.go.dev/builtin#bool)

### func (*GetPhotoMediaRequest) ProtoMessage 
    
    
    func (*GetPhotoMediaRequest) ProtoMessage()

### func (*GetPhotoMediaRequest) ProtoReflect 
    
    
    func (x *GetPhotoMediaRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPhotoMediaRequest) Reset 
    
    
    func (x *GetPhotoMediaRequest) Reset()

### func (*GetPhotoMediaRequest) String 
    
    
    func (x *GetPhotoMediaRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetPlaceRequest
    
    
    type GetPlaceRequest struct {
    
    	// Required. The resource name of a place, in the `places/{place_id}` format.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Place details will be displayed with the preferred language if
    	// available.
    	//
    	// Current list of supported languages:
    	// https://developers.google.com/maps/faq#languagesupport.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// Optional. The Unicode country/region code (CLDR) of the location where the
    	// request is coming from. This parameter is used to display the place
    	// details, like region-specific place name, if available. The parameter can
    	// affect results based on applicable law.
    	// For more information, see
    	// https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.
    	//
    	// Note that 3-digit region codes are not currently supported.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Optional. A string which identifies an Autocomplete session for billing
    	// purposes. Must be a URL and filename safe base64 string with at most 36
    	// ASCII characters in length. Otherwise an INVALID_ARGUMENT error is
    	// returned.
    	//
    	// The session begins when the user starts typing a query, and concludes when
    	// they select a place and a call to Place Details or Address Validation is
    	// made. Each session can have multiple queries, followed by one Place Details
    	// or Address Validation request. The credentials used for each request within
    	// a session must belong to the same Google Cloud Console project. Once a
    	// session has concluded, the token is no longer valid; your app must generate
    	// a fresh token for each session. If the `session_token` parameter is
    	// omitted, or if you reuse a session token, the session is charged as if no
    	// session token was provided (each request is billed separately).
    	//
    	// We recommend the following guidelines:
    	//
    	//   - Use session tokens for all Place Autocomplete calls.
    	//   - Generate a fresh token for each session. Using a version 4 UUID is
    	//     recommended.
    	//   - Ensure that the credentials used for all Place Autocomplete, Place
    	//     Details, and Address Validation requests within a session belong to the
    	//     same Cloud Console project.
    	//   - Be sure to pass a unique session token for each new session. Using the
    	//     same token for more than one session will result in each request being
    	//     billed individually.
    	SessionToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=session_token,json=sessionToken,proto3" json:"session_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching a Place based on its resource name, which is a string in the `places/{place_id}` format.

### func (*GetPlaceRequest) Descriptor 
    
    
    func (*GetPlaceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPlaceRequest.ProtoReflect.Descriptor instead.

### func (*GetPlaceRequest) GetLanguageCode 
    
    
    func (x *GetPlaceRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*GetPlaceRequest) GetName 
    
    
    func (x *GetPlaceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetPlaceRequest) GetRegionCode 
    
    
    func (x *GetPlaceRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*GetPlaceRequest) GetSessionToken 
    
    
    func (x *GetPlaceRequest) GetSessionToken() [string](https://pkg.go.dev/builtin#string)

### func (*GetPlaceRequest) ProtoMessage 
    
    
    func (*GetPlaceRequest) ProtoMessage()

### func (*GetPlaceRequest) ProtoReflect 
    
    
    func (x *GetPlaceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPlaceRequest) Reset 
    
    
    func (x *GetPlaceRequest) Reset()

### func (*GetPlaceRequest) String 
    
    
    func (x *GetPlaceRequest) String() [string](https://pkg.go.dev/builtin#string)

## Photo
    
    
    type Photo struct {
    
    	// Identifier. A reference representing this place photo which may be used to
    	// look up this place photo again (also called the API "resource" name:
    	// `places/{place_id}/photos/{photo}`).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The maximum available width, in pixels.
    	WidthPx [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=width_px,json=widthPx,proto3" json:"width_px,omitempty"`
    	// The maximum available height, in pixels.
    	HeightPx [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=height_px,json=heightPx,proto3" json:"height_px,omitempty"`
    	// This photo's authors.
    	AuthorAttributions []*AuthorAttribution `protobuf:"bytes,4,rep,name=author_attributions,json=authorAttributions,proto3" json:"author_attributions,omitempty"`
    	// A link where users can flag a problem with the photo.
    	FlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=flag_content_uri,json=flagContentUri,proto3" json:"flag_content_uri,omitempty"`
    	// A link to show the photo on Google Maps.
    	GoogleMapsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=google_maps_uri,json=googleMapsUri,proto3" json:"google_maps_uri,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a photo of a place.

### func (*Photo) Descriptor 
    
    
    func (*Photo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Photo.ProtoReflect.Descriptor instead.

### func (*Photo) GetAuthorAttributions 
    
    
    func (x *Photo) GetAuthorAttributions() []*AuthorAttribution

### func (*Photo) GetFlagContentUri 
    
    
    func (x *Photo) GetFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetGoogleMapsUri 
    
    
    func (x *Photo) GetGoogleMapsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetHeightPx 
    
    
    func (x *Photo) GetHeightPx() [int32](https://pkg.go.dev/builtin#int32)

### func (*Photo) GetName 
    
    
    func (x *Photo) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetWidthPx 
    
    
    func (x *Photo) GetWidthPx() [int32](https://pkg.go.dev/builtin#int32)

### func (*Photo) ProtoMessage 
    
    
    func (*Photo) ProtoMessage()

### func (*Photo) ProtoReflect 
    
    
    func (x *Photo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Photo) Reset 
    
    
    func (x *Photo) Reset()

### func (*Photo) String 
    
    
    func (x *Photo) String() [string](https://pkg.go.dev/builtin#string)

## PhotoMedia
    
    
    type PhotoMedia struct {
    
    	// The resource name of a photo media in the format:
    	// `places/{place_id}/photos/{photo_reference}/media`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A short-lived uri that can be used to render the photo.
    	PhotoUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=photo_uri,json=photoUri,proto3" json:"photo_uri,omitempty"`
    	// contains filtered or unexported fields
    }

A photo media from Places API.

### func (*PhotoMedia) Descriptor 
    
    
    func (*PhotoMedia) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoMedia.ProtoReflect.Descriptor instead.

### func (*PhotoMedia) GetName 
    
    
    func (x *PhotoMedia) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*PhotoMedia) GetPhotoUri 
    
    
    func (x *PhotoMedia) GetPhotoUri() [string](https://pkg.go.dev/builtin#string)

### func (*PhotoMedia) ProtoMessage 
    
    
    func (*PhotoMedia) ProtoMessage()

### func (*PhotoMedia) ProtoReflect 
    
    
    func (x *PhotoMedia) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PhotoMedia) Reset 
    
    
    func (x *PhotoMedia) Reset()

### func (*PhotoMedia) String 
    
    
    func (x *PhotoMedia) String() [string](https://pkg.go.dev/builtin#string)

## Place
    
    
    type Place struct {
    
    	// This Place's resource name, in `places/{place_id}` format.  Can be used to
    	// look up the Place.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The unique identifier of a place.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
    	// The localized name of the place, suitable as a short human-readable
    	// description. For example, "Google Sydney", "Starbucks", "Pyrmont", etc.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,31,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A set of type tags for this result. For example, "political" and
    	// "locality". For the complete list of possible values, see Table A and Table
    	// B at
    	// https://developers.google.com/maps/documentation/places/web-service/place-types
    	Types [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=types,proto3" json:"types,omitempty"`
    	// The primary type of the given result. This type must be one of the Places
    	// API supported types. For example, "restaurant", "cafe", "airport", etc.  A
    	// place can only have a single primary type.  For the complete list of
    	// possible values, see Table A and Table B at
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	// The primary type may be missing if the place's primary type is not a
    	// supported type. When a primary type is present, it is always one of the
    	// types in the `types` field.
    	PrimaryType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,50,opt,name=primary_type,json=primaryType,proto3" json:"primary_type,omitempty"`
    	// The display name of the primary type, localized to the request language if
    	// applicable. For the complete list of possible values, see Table A and Table
    	// B at
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	// The primary type may be missing if the place's primary type is not a
    	// supported type.
    	PrimaryTypeDisplayName *localized_text.LocalizedText `protobuf:"bytes,32,opt,name=primary_type_display_name,json=primaryTypeDisplayName,proto3" json:"primary_type_display_name,omitempty"`
    	// The type label of the place on Google Maps, localized to the request
    	// language if applicable, for example, "Restaurant", "Cafe", "Airport", etc.
    	// The type label may be different from the primary type display name and may
    	// not be a supported type in [Places API Place Types
    	// table](https://developers.google.com/maps/documentation/places/web-service/place-types).
    	GoogleMapsTypeLabel *localized_text.LocalizedText `protobuf:"bytes,96,opt,name=google_maps_type_label,json=googleMapsTypeLabel,proto3" json:"google_maps_type_label,omitempty"`
    	// A human-readable phone number for the place, in national format.
    	NationalPhoneNumber [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=national_phone_number,json=nationalPhoneNumber,proto3" json:"national_phone_number,omitempty"`
    	// A human-readable phone number for the place, in international format.
    	InternationalPhoneNumber [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=international_phone_number,json=internationalPhoneNumber,proto3" json:"international_phone_number,omitempty"`
    	// A full, human-readable address for this place.
    	FormattedAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=formatted_address,json=formattedAddress,proto3" json:"formatted_address,omitempty"`
    	// A short, human-readable address for this place.
    	ShortFormattedAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,51,opt,name=short_formatted_address,json=shortFormattedAddress,proto3" json:"short_formatted_address,omitempty"`
    	// The address in postal address format.
    	PostalAddress *postaladdress.PostalAddress `protobuf:"bytes,90,opt,name=postal_address,json=postalAddress,proto3" json:"postal_address,omitempty"`
    	// Repeated components for each locality level.
    	// Note the following facts about the address_components[] array:
    	// - The array of address components may contain more components than the
    	// formatted_address.
    	// - The array does not necessarily include all the political entities that
    	// contain an address, apart from those included in the formatted_address. To
    	// retrieve all the political entities that contain a specific address, you
    	// should use reverse geocoding, passing the latitude/longitude of the address
    	// as a parameter to the request.
    	// - The format of the response is not guaranteed to remain the same between
    	// requests. In particular, the number of address_components varies based on
    	// the address requested and can change over time for the same address. A
    	// component can change position in the array. The type of the component can
    	// change. A particular component may be missing in a later response.
    	AddressComponents []*Place_AddressComponent `protobuf:"bytes,10,rep,name=address_components,json=addressComponents,proto3" json:"address_components,omitempty"`
    	// Plus code of the place location lat/long.
    	PlusCode *Place_PlusCode `protobuf:"bytes,11,opt,name=plus_code,json=plusCode,proto3" json:"plus_code,omitempty"`
    	// The position of this place.
    	Location *latlng.LatLng `protobuf:"bytes,12,opt,name=location,proto3" json:"location,omitempty"`
    	// A viewport suitable for displaying the place on an average-sized map. This
    	// viewport should not be used as the physical boundary or the service area of
    	// the business.
    	Viewport *viewport.Viewport `protobuf:"bytes,13,opt,name=viewport,proto3" json:"viewport,omitempty"`
    	// A rating between 1.0 and 5.0, based on user reviews of this place.
    	Rating [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,14,opt,name=rating,proto3" json:"rating,omitempty"`
    	// A URL providing more information about this place.
    	GoogleMapsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,15,opt,name=google_maps_uri,json=googleMapsUri,proto3" json:"google_maps_uri,omitempty"`
    	// The authoritative website for this place, e.g. a business' homepage.
    	// Note that for places that are part of a chain (e.g. an IKEA store), this
    	// will usually be the website for the individual store, not the overall
    	// chain.
    	WebsiteUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,16,opt,name=website_uri,json=websiteUri,proto3" json:"website_uri,omitempty"`
    	// List of reviews about this place, sorted by relevance. A maximum of 5
    	// reviews can be returned.
    	Reviews []*Review `protobuf:"bytes,53,rep,name=reviews,proto3" json:"reviews,omitempty"`
    	// The regular hours of operation. Note that if a place is always open (24
    	// hours), the `close` field will not be set. Clients can rely on always open
    	// (24 hours) being represented as an
    	// [`open`](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#Period)
    	// period containing
    	// [`day`](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#Point)
    	// with value `0`,
    	// [`hour`](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#Point)
    	// with value `0`, and
    	// [`minute`](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#Point)
    	// with value `0`.
    	RegularOpeningHours *Place_OpeningHours `protobuf:"bytes,21,opt,name=regular_opening_hours,json=regularOpeningHours,proto3" json:"regular_opening_hours,omitempty"`
    	// Number of minutes this place's timezone is currently offset from UTC.
    	// This is expressed in minutes to support timezones that are offset by
    	// fractions of an hour, e.g. X hours and 15 minutes.
    	UtcOffsetMinutes *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,22,opt,name=utc_offset_minutes,json=utcOffsetMinutes,proto3,oneof" json:"utc_offset_minutes,omitempty"`
    	// IANA Time Zone Database time zone. For example "America/New_York".
    	TimeZone *datetime.TimeZone `protobuf:"bytes,88,opt,name=time_zone,json=timeZone,proto3" json:"time_zone,omitempty"`
    	// Information (including references) about photos of this place. A maximum of
    	// 10 photos can be returned.
    	Photos []*Photo `protobuf:"bytes,54,rep,name=photos,proto3" json:"photos,omitempty"`
    	// The place's address in adr microformat: http://microformats.org/wiki/adr.
    	AdrFormatAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,24,opt,name=adr_format_address,json=adrFormatAddress,proto3" json:"adr_format_address,omitempty"`
    	// The business status for the place.
    	BusinessStatus Place_BusinessStatus `protobuf:"varint,25,opt,name=business_status,json=businessStatus,proto3,enum=google.maps.places.v1.Place_BusinessStatus" json:"business_status,omitempty"`
    	// The date this place will open in the future. This field is only
    	// populated if the business status is FUTURE_OPENING.
    	OpeningDate *date.Date `protobuf:"bytes,95,opt,name=opening_date,json=openingDate,proto3" json:"opening_date,omitempty"`
    	// Price level of the place.
    	PriceLevel PriceLevel `protobuf:"varint,26,opt,name=price_level,json=priceLevel,proto3,enum=google.maps.places.v1.PriceLevel" json:"price_level,omitempty"`
    	// A set of data provider that must be shown with this result.
    	Attributions []*Place_Attribution `protobuf:"bytes,27,rep,name=attributions,proto3" json:"attributions,omitempty"`
    	// The total number of reviews (with or without text) for this place.
    	UserRatingCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,28,opt,name=user_rating_count,json=userRatingCount,proto3,oneof" json:"user_rating_count,omitempty"`
    	// A truncated URL to an icon mask. User can access different icon type by
    	// appending type suffix to the end (eg, ".svg" or ".png").
    	IconMaskBaseUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,29,opt,name=icon_mask_base_uri,json=iconMaskBaseUri,proto3" json:"icon_mask_base_uri,omitempty"`
    	// Background color for icon_mask in hex format, e.g. #909CE1.
    	IconBackgroundColor [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,30,opt,name=icon_background_color,json=iconBackgroundColor,proto3" json:"icon_background_color,omitempty"`
    	// Specifies if the business supports takeout.
    	Takeout *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,33,opt,name=takeout,proto3,oneof" json:"takeout,omitempty"`
    	// Specifies if the business supports delivery.
    	Delivery *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,34,opt,name=delivery,proto3,oneof" json:"delivery,omitempty"`
    	// Specifies if the business supports indoor or outdoor seating options.
    	DineIn *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,35,opt,name=dine_in,json=dineIn,proto3,oneof" json:"dine_in,omitempty"`
    	// Specifies if the business supports curbside pickup.
    	CurbsidePickup *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,36,opt,name=curbside_pickup,json=curbsidePickup,proto3,oneof" json:"curbside_pickup,omitempty"`
    	// Specifies if the place supports reservations.
    	Reservable *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,38,opt,name=reservable,proto3,oneof" json:"reservable,omitempty"`
    	// Specifies if the place serves breakfast.
    	ServesBreakfast *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,39,opt,name=serves_breakfast,json=servesBreakfast,proto3,oneof" json:"serves_breakfast,omitempty"`
    	// Specifies if the place serves lunch.
    	ServesLunch *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,40,opt,name=serves_lunch,json=servesLunch,proto3,oneof" json:"serves_lunch,omitempty"`
    	// Specifies if the place serves dinner.
    	ServesDinner *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,41,opt,name=serves_dinner,json=servesDinner,proto3,oneof" json:"serves_dinner,omitempty"`
    	// Specifies if the place serves beer.
    	ServesBeer *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,42,opt,name=serves_beer,json=servesBeer,proto3,oneof" json:"serves_beer,omitempty"`
    	// Specifies if the place serves wine.
    	ServesWine *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,43,opt,name=serves_wine,json=servesWine,proto3,oneof" json:"serves_wine,omitempty"`
    	// Specifies if the place serves brunch.
    	ServesBrunch *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,44,opt,name=serves_brunch,json=servesBrunch,proto3,oneof" json:"serves_brunch,omitempty"`
    	// Specifies if the place serves vegetarian food.
    	ServesVegetarianFood *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,45,opt,name=serves_vegetarian_food,json=servesVegetarianFood,proto3,oneof" json:"serves_vegetarian_food,omitempty"`
    	// The hours of operation for the next seven days (including today). The time
    	// period starts at midnight on the date of the request and ends at 11:59 pm
    	// six days later. This field includes the special_days subfield of all hours,
    	// set for dates that have exceptional hours.
    	CurrentOpeningHours *Place_OpeningHours `protobuf:"bytes,46,opt,name=current_opening_hours,json=currentOpeningHours,proto3" json:"current_opening_hours,omitempty"`
    	// Contains an array of entries for the next seven days including information
    	// about secondary hours of a business. Secondary hours are different from a
    	// business's main hours. For example, a restaurant can specify drive through
    	// hours or delivery hours as its secondary hours. This field populates the
    	// type subfield, which draws from a predefined list of opening hours types
    	// (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the
    	// place. This field includes the special_days subfield of all hours, set for
    	// dates that have exceptional hours.
    	CurrentSecondaryOpeningHours []*Place_OpeningHours `protobuf:"bytes,47,rep,name=current_secondary_opening_hours,json=currentSecondaryOpeningHours,proto3" json:"current_secondary_opening_hours,omitempty"`
    	// Contains an array of entries for information about regular secondary hours
    	// of a business. Secondary hours are different from a business's main hours.
    	// For example, a restaurant can specify drive through hours or delivery hours
    	// as its secondary hours. This field populates the type subfield, which draws
    	// from a predefined list of opening hours types (such as DRIVE_THROUGH,
    	// PICKUP, or TAKEOUT) based on the types of the place.
    	RegularSecondaryOpeningHours []*Place_OpeningHours `protobuf:"bytes,49,rep,name=regular_secondary_opening_hours,json=regularSecondaryOpeningHours,proto3" json:"regular_secondary_opening_hours,omitempty"`
    	// Contains a summary of the place. A summary is comprised of a textual
    	// overview, and also includes the language code for these if applicable.
    	// Summary text must be presented as-is and can not be modified or altered.
    	EditorialSummary *localized_text.LocalizedText `protobuf:"bytes,52,opt,name=editorial_summary,json=editorialSummary,proto3" json:"editorial_summary,omitempty"`
    	// Place provides outdoor seating.
    	OutdoorSeating *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,55,opt,name=outdoor_seating,json=outdoorSeating,proto3,oneof" json:"outdoor_seating,omitempty"`
    	// Place provides live music.
    	LiveMusic *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,56,opt,name=live_music,json=liveMusic,proto3,oneof" json:"live_music,omitempty"`
    	// Place has a children's menu.
    	MenuForChildren *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,57,opt,name=menu_for_children,json=menuForChildren,proto3,oneof" json:"menu_for_children,omitempty"`
    	// Place serves cocktails.
    	ServesCocktails *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,58,opt,name=serves_cocktails,json=servesCocktails,proto3,oneof" json:"serves_cocktails,omitempty"`
    	// Place serves dessert.
    	ServesDessert *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,59,opt,name=serves_dessert,json=servesDessert,proto3,oneof" json:"serves_dessert,omitempty"`
    	// Place serves coffee.
    	ServesCoffee *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,60,opt,name=serves_coffee,json=servesCoffee,proto3,oneof" json:"serves_coffee,omitempty"`
    	// Place is good for children.
    	GoodForChildren *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,62,opt,name=good_for_children,json=goodForChildren,proto3,oneof" json:"good_for_children,omitempty"`
    	// Place allows dogs.
    	AllowsDogs *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,63,opt,name=allows_dogs,json=allowsDogs,proto3,oneof" json:"allows_dogs,omitempty"`
    	// Place has restroom.
    	Restroom *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,64,opt,name=restroom,proto3,oneof" json:"restroom,omitempty"`
    	// Place accommodates groups.
    	GoodForGroups *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,65,opt,name=good_for_groups,json=goodForGroups,proto3,oneof" json:"good_for_groups,omitempty"`
    	// Place is suitable for watching sports.
    	GoodForWatchingSports *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,66,opt,name=good_for_watching_sports,json=goodForWatchingSports,proto3,oneof" json:"good_for_watching_sports,omitempty"`
    	// Payment options the place accepts. If a payment option data is not
    	// available, the payment option field will be unset.
    	PaymentOptions *Place_PaymentOptions `protobuf:"bytes,67,opt,name=payment_options,json=paymentOptions,proto3" json:"payment_options,omitempty"`
    	// Options of parking provided by the place.
    	ParkingOptions *Place_ParkingOptions `protobuf:"bytes,70,opt,name=parking_options,json=parkingOptions,proto3" json:"parking_options,omitempty"`
    	// A list of sub-destinations related to the place.
    	SubDestinations []*Place_SubDestination `protobuf:"bytes,71,rep,name=sub_destinations,json=subDestinations,proto3" json:"sub_destinations,omitempty"`
    	// Information about the accessibility options a place offers.
    	AccessibilityOptions *Place_AccessibilityOptions `protobuf:"bytes,72,opt,name=accessibility_options,json=accessibilityOptions,proto3,oneof" json:"accessibility_options,omitempty"`
    	// The most recent information about fuel options in a gas station. This
    	// information is updated regularly.
    	FuelOptions *FuelOptions `protobuf:"bytes,78,opt,name=fuel_options,json=fuelOptions,proto3" json:"fuel_options,omitempty"`
    	// Information of ev charging options.
    	EvChargeOptions *EVChargeOptions `protobuf:"bytes,79,opt,name=ev_charge_options,json=evChargeOptions,proto3" json:"ev_charge_options,omitempty"`
    	// AI-generated summary of the place.
    	GenerativeSummary *Place_GenerativeSummary `protobuf:"bytes,80,opt,name=generative_summary,json=generativeSummary,proto3" json:"generative_summary,omitempty"`
    	// List of places in which the current place is located.
    	ContainingPlaces []*Place_ContainingPlace `protobuf:"bytes,82,rep,name=containing_places,json=containingPlaces,proto3" json:"containing_places,omitempty"`
    	// Indicates whether the place is a pure service area business. Pure service
    	// area business is a business that visits or delivers to customers directly
    	// but does not serve customers at their business address. For example,
    	// businesses like cleaning services or plumbers. Those businesses may not
    	// have a physical address or location on Google Maps.
    	PureServiceAreaBusiness *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,83,opt,name=pure_service_area_business,json=pureServiceAreaBusiness,proto3,oneof" json:"pure_service_area_business,omitempty"`
    	// The address descriptor of the place. Address descriptors include additional
    	// information that help describe a location using landmarks and areas. See
    	// address descriptor regional coverage in
    	// https://developers.google.com/maps/documentation/geocoding/address-descriptors/coverage.
    	AddressDescriptor *AddressDescriptor `protobuf:"bytes,84,opt,name=address_descriptor,json=addressDescriptor,proto3" json:"address_descriptor,omitempty"`
    	// Links to trigger different Google Maps actions.
    	GoogleMapsLinks *Place_GoogleMapsLinks `protobuf:"bytes,85,opt,name=google_maps_links,json=googleMapsLinks,proto3" json:"google_maps_links,omitempty"`
    	// The price range associated with a Place.
    	PriceRange *PriceRange `protobuf:"bytes,86,opt,name=price_range,json=priceRange,proto3" json:"price_range,omitempty"`
    	// AI-generated summary of the place using user reviews.
    	ReviewSummary *Place_ReviewSummary `protobuf:"bytes,87,opt,name=review_summary,json=reviewSummary,proto3" json:"review_summary,omitempty"`
    	// The summary of amenities near the EV charging station.
    	EvChargeAmenitySummary *Place_EvChargeAmenitySummary `protobuf:"bytes,89,opt,name=ev_charge_amenity_summary,json=evChargeAmenitySummary,proto3" json:"ev_charge_amenity_summary,omitempty"`
    	// A summary of points of interest near the place.
    	NeighborhoodSummary *Place_NeighborhoodSummary `protobuf:"bytes,91,opt,name=neighborhood_summary,json=neighborhoodSummary,proto3" json:"neighborhood_summary,omitempty"`
    	// The consumer alert message for the place when we detect suspicious review
    	// activity on a business or a business violates our policies.
    	ConsumerAlert *Place_ConsumerAlert `protobuf:"bytes,92,opt,name=consumer_alert,json=consumerAlert,proto3" json:"consumer_alert,omitempty"`
    	// If this Place is permanently closed and has moved to a new Place, this
    	// field contains the new Place's resource name, in `places/{place_id}`
    	// format. If this Place moved multiple times, this field will represent the
    	// first moved place. This field will not be populated if this Place has not
    	// moved.
    	MovedPlace [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,93,opt,name=moved_place,json=movedPlace,proto3" json:"moved_place,omitempty"`
    	// If this Place is permanently closed and has moved to a new Place, this
    	// field contains the new Place's place ID. If this Place moved multiple
    	// times, this field will represent the first moved Place. This field will not
    	// be populated if this Place has not moved.
    	MovedPlaceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,94,opt,name=moved_place_id,json=movedPlaceId,proto3" json:"moved_place_id,omitempty"`
    	// The transit station information for the place.
    	TransitStation *TransitStation `protobuf:"bytes,98,opt,name=transit_station,json=transitStation,proto3" json:"transit_station,omitempty"`
    	// contains filtered or unexported fields
    }

All the information representing a Place.

### func (*Place) Descriptor 
    
    
    func (*Place) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place.ProtoReflect.Descriptor instead.

### func (*Place) GetAccessibilityOptions 
    
    
    func (x *Place) GetAccessibilityOptions() *Place_AccessibilityOptions

### func (*Place) GetAddressComponents 
    
    
    func (x *Place) GetAddressComponents() []*Place_AddressComponent

### func (*Place) GetAddressDescriptor 
    
    
    func (x *Place) GetAddressDescriptor() *AddressDescriptor

### func (*Place) GetAdrFormatAddress 
    
    
    func (x *Place) GetAdrFormatAddress() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetAllowsDogs 
    
    
    func (x *Place) GetAllowsDogs() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetAttributions 
    
    
    func (x *Place) GetAttributions() []*Place_Attribution

### func (*Place) GetBusinessStatus 
    
    
    func (x *Place) GetBusinessStatus() Place_BusinessStatus

### func (*Place) GetConsumerAlert 
    
    
    func (x *Place) GetConsumerAlert() *Place_ConsumerAlert

### func (*Place) GetContainingPlaces 
    
    
    func (x *Place) GetContainingPlaces() []*Place_ContainingPlace

### func (*Place) GetCurbsidePickup 
    
    
    func (x *Place) GetCurbsidePickup() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetCurrentOpeningHours 
    
    
    func (x *Place) GetCurrentOpeningHours() *Place_OpeningHours

### func (*Place) GetCurrentSecondaryOpeningHours 
    
    
    func (x *Place) GetCurrentSecondaryOpeningHours() []*Place_OpeningHours

### func (*Place) GetDelivery 
    
    
    func (x *Place) GetDelivery() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetDineIn 
    
    
    func (x *Place) GetDineIn() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetDisplayName 
    
    
    func (x *Place) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place) GetEditorialSummary 
    
    
    func (x *Place) GetEditorialSummary() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place) GetEvChargeAmenitySummary 
    
    
    func (x *Place) GetEvChargeAmenitySummary() *Place_EvChargeAmenitySummary

### func (*Place) GetEvChargeOptions 
    
    
    func (x *Place) GetEvChargeOptions() *EVChargeOptions

### func (*Place) GetFormattedAddress 
    
    
    func (x *Place) GetFormattedAddress() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetFuelOptions 
    
    
    func (x *Place) GetFuelOptions() *FuelOptions

### func (*Place) GetGenerativeSummary 
    
    
    func (x *Place) GetGenerativeSummary() *Place_GenerativeSummary

### func (*Place) GetGoodForChildren 
    
    
    func (x *Place) GetGoodForChildren() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetGoodForGroups 
    
    
    func (x *Place) GetGoodForGroups() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetGoodForWatchingSports 
    
    
    func (x *Place) GetGoodForWatchingSports() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetGoogleMapsLinks 
    
    
    func (x *Place) GetGoogleMapsLinks() *Place_GoogleMapsLinks

### func (*Place) GetGoogleMapsTypeLabel 
    
    
    func (x *Place) GetGoogleMapsTypeLabel() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place) GetGoogleMapsUri 
    
    
    func (x *Place) GetGoogleMapsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetIconBackgroundColor 
    
    
    func (x *Place) GetIconBackgroundColor() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetIconMaskBaseUri 
    
    
    func (x *Place) GetIconMaskBaseUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetId 
    
    
    func (x *Place) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetInternationalPhoneNumber 
    
    
    func (x *Place) GetInternationalPhoneNumber() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetLiveMusic 
    
    
    func (x *Place) GetLiveMusic() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetLocation 
    
    
    func (x *Place) GetLocation() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*Place) GetMenuForChildren 
    
    
    func (x *Place) GetMenuForChildren() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetMovedPlace 
    
    
    func (x *Place) GetMovedPlace() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetMovedPlaceId 
    
    
    func (x *Place) GetMovedPlaceId() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetName 
    
    
    func (x *Place) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetNationalPhoneNumber 
    
    
    func (x *Place) GetNationalPhoneNumber() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetNeighborhoodSummary 
    
    
    func (x *Place) GetNeighborhoodSummary() *Place_NeighborhoodSummary

### func (*Place) GetOpeningDate 
    
    
    func (x *Place) GetOpeningDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*Place) GetOutdoorSeating 
    
    
    func (x *Place) GetOutdoorSeating() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetParkingOptions 
    
    
    func (x *Place) GetParkingOptions() *Place_ParkingOptions

### func (*Place) GetPaymentOptions 
    
    
    func (x *Place) GetPaymentOptions() *Place_PaymentOptions

### func (*Place) GetPhotos 
    
    
    func (x *Place) GetPhotos() []*Photo

### func (*Place) GetPlusCode 
    
    
    func (x *Place) GetPlusCode() *Place_PlusCode

### func (*Place) GetPostalAddress 
    
    
    func (x *Place) GetPostalAddress() *[postaladdress](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/postaladdress).[PostalAddress](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/postaladdress#PostalAddress)

### func (*Place) GetPriceLevel 
    
    
    func (x *Place) GetPriceLevel() PriceLevel

### func (*Place) GetPriceRange 
    
    
    func (x *Place) GetPriceRange() *PriceRange

### func (*Place) GetPrimaryType 
    
    
    func (x *Place) GetPrimaryType() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetPrimaryTypeDisplayName 
    
    
    func (x *Place) GetPrimaryTypeDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place) GetPureServiceAreaBusiness 
    
    
    func (x *Place) GetPureServiceAreaBusiness() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetRating 
    
    
    func (x *Place) GetRating() [float64](https://pkg.go.dev/builtin#float64)

### func (*Place) GetRegularOpeningHours 
    
    
    func (x *Place) GetRegularOpeningHours() *Place_OpeningHours

### func (*Place) GetRegularSecondaryOpeningHours 
    
    
    func (x *Place) GetRegularSecondaryOpeningHours() []*Place_OpeningHours

### func (*Place) GetReservable 
    
    
    func (x *Place) GetReservable() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetRestroom 
    
    
    func (x *Place) GetRestroom() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetReviewSummary 
    
    
    func (x *Place) GetReviewSummary() *Place_ReviewSummary

### func (*Place) GetReviews 
    
    
    func (x *Place) GetReviews() []*Review

### func (*Place) GetServesBeer 
    
    
    func (x *Place) GetServesBeer() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesBreakfast 
    
    
    func (x *Place) GetServesBreakfast() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesBrunch 
    
    
    func (x *Place) GetServesBrunch() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesCocktails 
    
    
    func (x *Place) GetServesCocktails() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesCoffee 
    
    
    func (x *Place) GetServesCoffee() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesDessert 
    
    
    func (x *Place) GetServesDessert() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesDinner 
    
    
    func (x *Place) GetServesDinner() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesLunch 
    
    
    func (x *Place) GetServesLunch() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesVegetarianFood 
    
    
    func (x *Place) GetServesVegetarianFood() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetServesWine 
    
    
    func (x *Place) GetServesWine() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetShortFormattedAddress 
    
    
    func (x *Place) GetShortFormattedAddress() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetSubDestinations 
    
    
    func (x *Place) GetSubDestinations() []*Place_SubDestination

### func (*Place) GetTakeout 
    
    
    func (x *Place) GetTakeout() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place) GetTimeZone 
    
    
    func (x *Place) GetTimeZone() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[TimeZone](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#TimeZone)

### func (*Place) GetTransitStation 
    
    
    func (x *Place) GetTransitStation() *TransitStation

### func (*Place) GetTypes 
    
    
    func (x *Place) GetTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*Place) GetUserRatingCount 
    
    
    func (x *Place) GetUserRatingCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Place) GetUtcOffsetMinutes 
    
    
    func (x *Place) GetUtcOffsetMinutes() [int32](https://pkg.go.dev/builtin#int32)

### func (*Place) GetViewport 
    
    
    func (x *Place) GetViewport() *[viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport).[Viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport#Viewport)

### func (*Place) GetWebsiteUri 
    
    
    func (x *Place) GetWebsiteUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place) ProtoMessage 
    
    
    func (*Place) ProtoMessage()

### func (*Place) ProtoReflect 
    
    
    func (x *Place) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place) Reset 
    
    
    func (x *Place) Reset()

### func (*Place) String 
    
    
    func (x *Place) String() [string](https://pkg.go.dev/builtin#string)

## Place_AccessibilityOptions
    
    
    type Place_AccessibilityOptions struct {
    
    	// Place offers wheelchair accessible parking.
    	WheelchairAccessibleParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=wheelchair_accessible_parking,json=wheelchairAccessibleParking,proto3,oneof" json:"wheelchair_accessible_parking,omitempty"`
    	// Places has wheelchair accessible entrance.
    	WheelchairAccessibleEntrance *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=wheelchair_accessible_entrance,json=wheelchairAccessibleEntrance,proto3,oneof" json:"wheelchair_accessible_entrance,omitempty"`
    	// Place has wheelchair accessible restroom.
    	WheelchairAccessibleRestroom *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=wheelchair_accessible_restroom,json=wheelchairAccessibleRestroom,proto3,oneof" json:"wheelchair_accessible_restroom,omitempty"`
    	// Place has wheelchair accessible seating.
    	WheelchairAccessibleSeating *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=wheelchair_accessible_seating,json=wheelchairAccessibleSeating,proto3,oneof" json:"wheelchair_accessible_seating,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the accessibility options a place offers.

### func (*Place_AccessibilityOptions) Descriptor 
    
    
    func (*Place_AccessibilityOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_AccessibilityOptions.ProtoReflect.Descriptor instead.

### func (*Place_AccessibilityOptions) GetWheelchairAccessibleEntrance 
    
    
    func (x *Place_AccessibilityOptions) GetWheelchairAccessibleEntrance() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_AccessibilityOptions) GetWheelchairAccessibleParking 
    
    
    func (x *Place_AccessibilityOptions) GetWheelchairAccessibleParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_AccessibilityOptions) GetWheelchairAccessibleRestroom 
    
    
    func (x *Place_AccessibilityOptions) GetWheelchairAccessibleRestroom() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_AccessibilityOptions) GetWheelchairAccessibleSeating 
    
    
    func (x *Place_AccessibilityOptions) GetWheelchairAccessibleSeating() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_AccessibilityOptions) ProtoMessage 
    
    
    func (*Place_AccessibilityOptions) ProtoMessage()

### func (*Place_AccessibilityOptions) ProtoReflect 
    
    
    func (x *Place_AccessibilityOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_AccessibilityOptions) Reset 
    
    
    func (x *Place_AccessibilityOptions) Reset()

### func (*Place_AccessibilityOptions) String 
    
    
    func (x *Place_AccessibilityOptions) String() [string](https://pkg.go.dev/builtin#string)

## Place_AddressComponent
    
    
    type Place_AddressComponent struct {
    
    	// The full text description or name of the address component. For example,
    	// an address component for the country Australia may have a long_name of
    	// "Australia".
    	LongText [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=long_text,json=longText,proto3" json:"long_text,omitempty"`
    	// An abbreviated textual name for the address component, if available. For
    	// example, an address component for the country of Australia may have a
    	// short_name of "AU".
    	ShortText [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=short_text,json=shortText,proto3" json:"short_text,omitempty"`
    	// An array indicating the type(s) of the address component.
    	Types [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=types,proto3" json:"types,omitempty"`
    	// The language used to format this components, in CLDR notation.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

The structured components that form the formatted address, if this information is available.

### func (*Place_AddressComponent) Descriptor 
    
    
    func (*Place_AddressComponent) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_AddressComponent.ProtoReflect.Descriptor instead.

### func (*Place_AddressComponent) GetLanguageCode 
    
    
    func (x *Place_AddressComponent) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*Place_AddressComponent) GetLongText 
    
    
    func (x *Place_AddressComponent) GetLongText() [string](https://pkg.go.dev/builtin#string)

### func (*Place_AddressComponent) GetShortText 
    
    
    func (x *Place_AddressComponent) GetShortText() [string](https://pkg.go.dev/builtin#string)

### func (*Place_AddressComponent) GetTypes 
    
    
    func (x *Place_AddressComponent) GetTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*Place_AddressComponent) ProtoMessage 
    
    
    func (*Place_AddressComponent) ProtoMessage()

### func (*Place_AddressComponent) ProtoReflect 
    
    
    func (x *Place_AddressComponent) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_AddressComponent) Reset 
    
    
    func (x *Place_AddressComponent) Reset()

### func (*Place_AddressComponent) String 
    
    
    func (x *Place_AddressComponent) String() [string](https://pkg.go.dev/builtin#string)

## Place_Attribution
    
    
    type Place_Attribution struct {
    
    	// Name of the Place's data provider.
    	Provider [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=provider,proto3" json:"provider,omitempty"`
    	// URI to the Place's data provider.
    	ProviderUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=provider_uri,json=providerUri,proto3" json:"provider_uri,omitempty"`
    	// contains filtered or unexported fields
    }

Information about data providers of this place.

### func (*Place_Attribution) Descriptor 
    
    
    func (*Place_Attribution) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_Attribution.ProtoReflect.Descriptor instead.

### func (*Place_Attribution) GetProvider 
    
    
    func (x *Place_Attribution) GetProvider() [string](https://pkg.go.dev/builtin#string)

### func (*Place_Attribution) GetProviderUri 
    
    
    func (x *Place_Attribution) GetProviderUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_Attribution) ProtoMessage 
    
    
    func (*Place_Attribution) ProtoMessage()

### func (*Place_Attribution) ProtoReflect 
    
    
    func (x *Place_Attribution) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_Attribution) Reset 
    
    
    func (x *Place_Attribution) Reset()

### func (*Place_Attribution) String 
    
    
    func (x *Place_Attribution) String() [string](https://pkg.go.dev/builtin#string)

## Place_BusinessStatus
    
    
    type Place_BusinessStatus [int32](https://pkg.go.dev/builtin#int32)

Business status for the place.

### Place_BUSINESS_STATUS_UNSPECIFIED, Place_OPERATIONAL, Place_CLOSED_TEMPORARILY, Place_CLOSED_PERMANENTLY, Place_FUTURE_OPENING
    
    
    const (
    	// Default value. This value is unused.
    	Place_BUSINESS_STATUS_UNSPECIFIED Place_BusinessStatus = 0
    	// The establishment is operational, not necessarily open now.
    	Place_OPERATIONAL Place_BusinessStatus = 1
    	// The establishment is temporarily closed.
    	Place_CLOSED_TEMPORARILY Place_BusinessStatus = 2
    	// The establishment is permanently closed.
    	Place_CLOSED_PERMANENTLY Place_BusinessStatus = 3
    	// The establishment will open in the future.
    	Place_FUTURE_OPENING Place_BusinessStatus = 4
    )

### func (Place_BusinessStatus) Descriptor 
    
    
    func (Place_BusinessStatus) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Place_BusinessStatus) Enum 
    
    
    func (x Place_BusinessStatus) Enum() *Place_BusinessStatus

### func (Place_BusinessStatus) EnumDescriptor 
    
    
    func (Place_BusinessStatus) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_BusinessStatus.Descriptor instead.

### func (Place_BusinessStatus) Number 
    
    
    func (x Place_BusinessStatus) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Place_BusinessStatus) String 
    
    
    func (x Place_BusinessStatus) String() [string](https://pkg.go.dev/builtin#string)

### func (Place_BusinessStatus) Type 
    
    
    func (Place_BusinessStatus) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Place_ConsumerAlert
    
    
    type Place_ConsumerAlert struct {
    
    	// The overview of the consumer alert message.
    	Overview [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=overview,proto3" json:"overview,omitempty"`
    	// The details of the consumer alert message.
    	Details *Place_ConsumerAlert_Details `protobuf:"bytes,2,opt,name=details,proto3" json:"details,omitempty"`
    	// The language code of the consumer alert message. This is a BCP 47
    	// language code.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

The consumer alert message for the place when we detect suspicious review activity on a business or a business violates our policies.

### func (*Place_ConsumerAlert) Descriptor 
    
    
    func (*Place_ConsumerAlert) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ConsumerAlert.ProtoReflect.Descriptor instead.

### func (*Place_ConsumerAlert) GetDetails 
    
    
    func (x *Place_ConsumerAlert) GetDetails() *Place_ConsumerAlert_Details

### func (*Place_ConsumerAlert) GetLanguageCode 
    
    
    func (x *Place_ConsumerAlert) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert) GetOverview 
    
    
    func (x *Place_ConsumerAlert) GetOverview() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert) ProtoMessage 
    
    
    func (*Place_ConsumerAlert) ProtoMessage()

### func (*Place_ConsumerAlert) ProtoReflect 
    
    
    func (x *Place_ConsumerAlert) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ConsumerAlert) Reset 
    
    
    func (x *Place_ConsumerAlert) Reset()

### func (*Place_ConsumerAlert) String 
    
    
    func (x *Place_ConsumerAlert) String() [string](https://pkg.go.dev/builtin#string)

## Place_ConsumerAlert_Details
    
    
    type Place_ConsumerAlert_Details struct {
    
    	// The title to show together with the description.
    	Title [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=title,proto3" json:"title,omitempty"`
    	// The description of the consumer alert message.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// The link to show together with the description to provide more
    	// information.
    	AboutLink *Place_ConsumerAlert_Details_Link `protobuf:"bytes,3,opt,name=about_link,json=aboutLink,proto3" json:"about_link,omitempty"`
    	// contains filtered or unexported fields
    }

The details of the consumer alert message.

### func (*Place_ConsumerAlert_Details) Descriptor 
    
    
    func (*Place_ConsumerAlert_Details) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ConsumerAlert_Details.ProtoReflect.Descriptor instead.

### func (*Place_ConsumerAlert_Details) GetAboutLink 
    
    
    func (x *Place_ConsumerAlert_Details) GetAboutLink() *Place_ConsumerAlert_Details_Link

### func (*Place_ConsumerAlert_Details) GetDescription 
    
    
    func (x *Place_ConsumerAlert_Details) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert_Details) GetTitle 
    
    
    func (x *Place_ConsumerAlert_Details) GetTitle() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert_Details) ProtoMessage 
    
    
    func (*Place_ConsumerAlert_Details) ProtoMessage()

### func (*Place_ConsumerAlert_Details) ProtoReflect 
    
    
    func (x *Place_ConsumerAlert_Details) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ConsumerAlert_Details) Reset 
    
    
    func (x *Place_ConsumerAlert_Details) Reset()

### func (*Place_ConsumerAlert_Details) String 
    
    
    func (x *Place_ConsumerAlert_Details) String() [string](https://pkg.go.dev/builtin#string)

## Place_ConsumerAlert_Details_Link
    
    
    type Place_ConsumerAlert_Details_Link struct {
    
    	// The title to show for the link.
    	Title [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=title,proto3" json:"title,omitempty"`
    	// The uri of the link.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=uri,proto3" json:"uri,omitempty"`
    	// contains filtered or unexported fields
    }

The link to show together with the description to provide more information.

### func (*Place_ConsumerAlert_Details_Link) Descriptor 
    
    
    func (*Place_ConsumerAlert_Details_Link) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ConsumerAlert_Details_Link.ProtoReflect.Descriptor instead.

### func (*Place_ConsumerAlert_Details_Link) GetTitle 
    
    
    func (x *Place_ConsumerAlert_Details_Link) GetTitle() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert_Details_Link) GetUri 
    
    
    func (x *Place_ConsumerAlert_Details_Link) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ConsumerAlert_Details_Link) ProtoMessage 
    
    
    func (*Place_ConsumerAlert_Details_Link) ProtoMessage()

### func (*Place_ConsumerAlert_Details_Link) ProtoReflect 
    
    
    func (x *Place_ConsumerAlert_Details_Link) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ConsumerAlert_Details_Link) Reset 
    
    
    func (x *Place_ConsumerAlert_Details_Link) Reset()

### func (*Place_ConsumerAlert_Details_Link) String 
    
    
    func (x *Place_ConsumerAlert_Details_Link) String() [string](https://pkg.go.dev/builtin#string)

## Place_ContainingPlace
    
    
    type Place_ContainingPlace struct {
    
    	// The resource name of the place in which this place is located.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The place id of the place in which this place is located.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
    	// contains filtered or unexported fields
    }

Info about the place in which this place is located.

### func (*Place_ContainingPlace) Descriptor 
    
    
    func (*Place_ContainingPlace) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ContainingPlace.ProtoReflect.Descriptor instead.

### func (*Place_ContainingPlace) GetId 
    
    
    func (x *Place_ContainingPlace) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ContainingPlace) GetName 
    
    
    func (x *Place_ContainingPlace) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ContainingPlace) ProtoMessage 
    
    
    func (*Place_ContainingPlace) ProtoMessage()

### func (*Place_ContainingPlace) ProtoReflect 
    
    
    func (x *Place_ContainingPlace) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ContainingPlace) Reset 
    
    
    func (x *Place_ContainingPlace) Reset()

### func (*Place_ContainingPlace) String 
    
    
    func (x *Place_ContainingPlace) String() [string](https://pkg.go.dev/builtin#string)

## Place_EvChargeAmenitySummary
    
    
    type Place_EvChargeAmenitySummary struct {
    
    	// An overview of the available amenities. This is guaranteed to be
    	// provided.
    	Overview *ContentBlock `protobuf:"bytes,1,opt,name=overview,proto3" json:"overview,omitempty"`
    	// A summary of the nearby coffee options.
    	Coffee *ContentBlock `protobuf:"bytes,2,opt,name=coffee,proto3" json:"coffee,omitempty"`
    	// A summary of the nearby restaurants.
    	Restaurant *ContentBlock `protobuf:"bytes,3,opt,name=restaurant,proto3" json:"restaurant,omitempty"`
    	// A summary of the nearby stores.
    	Store *ContentBlock `protobuf:"bytes,4,opt,name=store,proto3" json:"store,omitempty"`
    	// A link where users can flag a problem with the summary.
    	FlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=flag_content_uri,json=flagContentUri,proto3" json:"flag_content_uri,omitempty"`
    	// The AI disclosure message "Summarized with Gemini"
    	// (and its localized variants). This will be in the language specified in
    	// the request if available.
    	DisclosureText *localized_text.LocalizedText `protobuf:"bytes,6,opt,name=disclosure_text,json=disclosureText,proto3" json:"disclosure_text,omitempty"`
    	// contains filtered or unexported fields
    }

The summary of amenities near the EV charging station. This only applies to places with type `electric_vehicle_charging_station`. The `overview` field is guaranteed to be provided while the other fields are optional.

### func (*Place_EvChargeAmenitySummary) Descriptor 
    
    
    func (*Place_EvChargeAmenitySummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_EvChargeAmenitySummary.ProtoReflect.Descriptor instead.

### func (*Place_EvChargeAmenitySummary) GetCoffee 
    
    
    func (x *Place_EvChargeAmenitySummary) GetCoffee() *ContentBlock

### func (*Place_EvChargeAmenitySummary) GetDisclosureText 
    
    
    func (x *Place_EvChargeAmenitySummary) GetDisclosureText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_EvChargeAmenitySummary) GetFlagContentUri 
    
    
    func (x *Place_EvChargeAmenitySummary) GetFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_EvChargeAmenitySummary) GetOverview 
    
    
    func (x *Place_EvChargeAmenitySummary) GetOverview() *ContentBlock

### func (*Place_EvChargeAmenitySummary) GetRestaurant 
    
    
    func (x *Place_EvChargeAmenitySummary) GetRestaurant() *ContentBlock

### func (*Place_EvChargeAmenitySummary) GetStore 
    
    
    func (x *Place_EvChargeAmenitySummary) GetStore() *ContentBlock

### func (*Place_EvChargeAmenitySummary) ProtoMessage 
    
    
    func (*Place_EvChargeAmenitySummary) ProtoMessage()

### func (*Place_EvChargeAmenitySummary) ProtoReflect 
    
    
    func (x *Place_EvChargeAmenitySummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_EvChargeAmenitySummary) Reset 
    
    
    func (x *Place_EvChargeAmenitySummary) Reset()

### func (*Place_EvChargeAmenitySummary) String 
    
    
    func (x *Place_EvChargeAmenitySummary) String() [string](https://pkg.go.dev/builtin#string)

## Place_GenerativeSummary
    
    
    type Place_GenerativeSummary struct {
    
    	// The overview of the place.
    	Overview *localized_text.LocalizedText `protobuf:"bytes,1,opt,name=overview,proto3" json:"overview,omitempty"`
    	// A link where users can flag a problem with the overview summary.
    	OverviewFlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=overview_flag_content_uri,json=overviewFlagContentUri,proto3" json:"overview_flag_content_uri,omitempty"`
    	// The AI disclosure message "Summarized with Gemini"
    	// (and its localized variants). This will be in the language specified in
    	// the request if available.
    	DisclosureText *localized_text.LocalizedText `protobuf:"bytes,6,opt,name=disclosure_text,json=disclosureText,proto3" json:"disclosure_text,omitempty"`
    	// contains filtered or unexported fields
    }

AI-generated summary of the place.

### func (*Place_GenerativeSummary) Descriptor 
    
    
    func (*Place_GenerativeSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_GenerativeSummary.ProtoReflect.Descriptor instead.

### func (*Place_GenerativeSummary) GetDisclosureText 
    
    
    func (x *Place_GenerativeSummary) GetDisclosureText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_GenerativeSummary) GetOverview 
    
    
    func (x *Place_GenerativeSummary) GetOverview() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_GenerativeSummary) GetOverviewFlagContentUri 
    
    
    func (x *Place_GenerativeSummary) GetOverviewFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GenerativeSummary) ProtoMessage 
    
    
    func (*Place_GenerativeSummary) ProtoMessage()

### func (*Place_GenerativeSummary) ProtoReflect 
    
    
    func (x *Place_GenerativeSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_GenerativeSummary) Reset 
    
    
    func (x *Place_GenerativeSummary) Reset()

### func (*Place_GenerativeSummary) String 
    
    
    func (x *Place_GenerativeSummary) String() [string](https://pkg.go.dev/builtin#string)

## Place_GoogleMapsLinks
    
    
    type Place_GoogleMapsLinks struct {
    
    	// A link to show the directions to the place. The link only populates the
    	// destination location and uses the default travel mode `DRIVE`.
    	DirectionsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=directions_uri,json=directionsUri,proto3" json:"directions_uri,omitempty"`
    	// A link to show this place.
    	PlaceUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=place_uri,json=placeUri,proto3" json:"place_uri,omitempty"`
    	// A link to write a review for this place on Google Maps.
    	WriteAReviewUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=write_a_review_uri,json=writeAReviewUri,proto3" json:"write_a_review_uri,omitempty"`
    	// A link to show reviews of this place on Google Maps.
    	ReviewsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=reviews_uri,json=reviewsUri,proto3" json:"reviews_uri,omitempty"`
    	// A link to show photos of this place on Google Maps.
    	PhotosUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=photos_uri,json=photosUri,proto3" json:"photos_uri,omitempty"`
    	// contains filtered or unexported fields
    }

Links to trigger different Google Maps actions.

### func (*Place_GoogleMapsLinks) Descriptor 
    
    
    func (*Place_GoogleMapsLinks) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_GoogleMapsLinks.ProtoReflect.Descriptor instead.

### func (*Place_GoogleMapsLinks) GetDirectionsUri 
    
    
    func (x *Place_GoogleMapsLinks) GetDirectionsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GoogleMapsLinks) GetPhotosUri 
    
    
    func (x *Place_GoogleMapsLinks) GetPhotosUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GoogleMapsLinks) GetPlaceUri 
    
    
    func (x *Place_GoogleMapsLinks) GetPlaceUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GoogleMapsLinks) GetReviewsUri 
    
    
    func (x *Place_GoogleMapsLinks) GetReviewsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GoogleMapsLinks) GetWriteAReviewUri 
    
    
    func (x *Place_GoogleMapsLinks) GetWriteAReviewUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_GoogleMapsLinks) ProtoMessage 
    
    
    func (*Place_GoogleMapsLinks) ProtoMessage()

### func (*Place_GoogleMapsLinks) ProtoReflect 
    
    
    func (x *Place_GoogleMapsLinks) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_GoogleMapsLinks) Reset 
    
    
    func (x *Place_GoogleMapsLinks) Reset()

### func (*Place_GoogleMapsLinks) String 
    
    
    func (x *Place_GoogleMapsLinks) String() [string](https://pkg.go.dev/builtin#string)

## Place_NeighborhoodSummary
    
    
    type Place_NeighborhoodSummary struct {
    
    	// An overview summary of the neighborhood.
    	Overview *ContentBlock `protobuf:"bytes,1,opt,name=overview,proto3" json:"overview,omitempty"`
    	// A detailed description of the neighborhood.
    	Description *ContentBlock `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// A link where users can flag a problem with the summary.
    	FlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=flag_content_uri,json=flagContentUri,proto3" json:"flag_content_uri,omitempty"`
    	// The AI disclosure message "Summarized with Gemini"
    	// (and its localized variants). This will be in the language specified in
    	// the request if available.
    	DisclosureText *localized_text.LocalizedText `protobuf:"bytes,4,opt,name=disclosure_text,json=disclosureText,proto3" json:"disclosure_text,omitempty"`
    	// contains filtered or unexported fields
    }

A summary of points of interest near the place.

### func (*Place_NeighborhoodSummary) Descriptor 
    
    
    func (*Place_NeighborhoodSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_NeighborhoodSummary.ProtoReflect.Descriptor instead.

### func (*Place_NeighborhoodSummary) GetDescription 
    
    
    func (x *Place_NeighborhoodSummary) GetDescription() *ContentBlock

### func (*Place_NeighborhoodSummary) GetDisclosureText 
    
    
    func (x *Place_NeighborhoodSummary) GetDisclosureText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_NeighborhoodSummary) GetFlagContentUri 
    
    
    func (x *Place_NeighborhoodSummary) GetFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_NeighborhoodSummary) GetOverview 
    
    
    func (x *Place_NeighborhoodSummary) GetOverview() *ContentBlock

### func (*Place_NeighborhoodSummary) ProtoMessage 
    
    
    func (*Place_NeighborhoodSummary) ProtoMessage()

### func (*Place_NeighborhoodSummary) ProtoReflect 
    
    
    func (x *Place_NeighborhoodSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_NeighborhoodSummary) Reset 
    
    
    func (x *Place_NeighborhoodSummary) Reset()

### func (*Place_NeighborhoodSummary) String 
    
    
    func (x *Place_NeighborhoodSummary) String() [string](https://pkg.go.dev/builtin#string)

## Place_OpeningHours
    
    
    type Place_OpeningHours struct {
    
    	// Whether the opening hours period is currently active. For regular opening
    	// hours and current opening hours, this field means whether the place is
    	// open. For secondary opening hours and current secondary opening hours,
    	// this field means whether the secondary hours of this place is active.
    	OpenNow *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=open_now,json=openNow,proto3,oneof" json:"open_now,omitempty"`
    	// The periods that this place is open during the week. The periods are in
    	// chronological order, in the place-local timezone. An empty (but not
    	// absent) value indicates a place that is never open, e.g.
    	// because it is closed temporarily for renovations.
    	//
    	// The starting day of `periods` is NOT fixed and should not be assumed to
    	// be Sunday. The API determines the start day based on a variety of
    	// factors. For example, for a 24/7 business, the first period may begin on
    	// the day of the request. For other businesses, it might be the first day
    	// of the week that they are open.
    	//
    	// NOTE: The ordering of the `periods` array is independent of the ordering
    	// of the `weekday_descriptions` array. Do not assume they will begin on the
    	// same day.
    	Periods []*Place_OpeningHours_Period `protobuf:"bytes,2,rep,name=periods,proto3" json:"periods,omitempty"`
    	// Localized strings describing the opening hours of this place, one string
    	// for each day of the week.
    	//
    	// NOTE: The order of the days and the start of the week is determined by
    	// the locale (language and region). The ordering of the `periods` array is
    	// independent of the ordering of the `weekday_descriptions` array. Do not
    	// assume they will begin on the same day.
    	//
    	// Will be empty if the hours are unknown or could not be converted to
    	// localized text. Example: "Sun: 18:00–06:00"
    	WeekdayDescriptions [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=weekday_descriptions,json=weekdayDescriptions,proto3" json:"weekday_descriptions,omitempty"`
    	// A type string used to identify the type of secondary hours.
    	SecondaryHoursType Place_OpeningHours_SecondaryHoursType `protobuf:"varint,4,opt,name=secondary_hours_type,json=secondaryHoursType,proto3,enum=google.maps.places.v1.Place_OpeningHours_SecondaryHoursType" json:"secondary_hours_type,omitempty"`
    	// Structured information for special days that fall within the period that
    	// the returned opening hours cover. Special days are days that could impact
    	// the business hours of a place, e.g. Christmas day. Set for
    	// current_opening_hours and current_secondary_opening_hours if there are
    	// exceptional hours.
    	SpecialDays []*Place_OpeningHours_SpecialDay `protobuf:"bytes,5,rep,name=special_days,json=specialDays,proto3" json:"special_days,omitempty"`
    	// The next time the current opening hours period starts up to 7 days in the
    	// future. This field is only populated if the opening hours period is not
    	// active at the time of serving the request.
    	NextOpenTime *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=next_open_time,json=nextOpenTime,proto3" json:"next_open_time,omitempty"`
    	// The next time the current opening hours period ends up to 7 days in the
    	// future. This field is only populated if the opening hours period is
    	// active at the time of serving the request.
    	NextCloseTime *timestamppb.Timestamp `protobuf:"bytes,7,opt,name=next_close_time,json=nextCloseTime,proto3" json:"next_close_time,omitempty"`
    	// contains filtered or unexported fields
    }

Information about business hour of the place.

### func (*Place_OpeningHours) Descriptor 
    
    
    func (*Place_OpeningHours) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_OpeningHours.ProtoReflect.Descriptor instead.

### func (*Place_OpeningHours) GetNextCloseTime 
    
    
    func (x *Place_OpeningHours) GetNextCloseTime() *timestamppb.Timestamp

### func (*Place_OpeningHours) GetNextOpenTime 
    
    
    func (x *Place_OpeningHours) GetNextOpenTime() *timestamppb.Timestamp

### func (*Place_OpeningHours) GetOpenNow 
    
    
    func (x *Place_OpeningHours) GetOpenNow() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_OpeningHours) GetPeriods 
    
    
    func (x *Place_OpeningHours) GetPeriods() []*Place_OpeningHours_Period

### func (*Place_OpeningHours) GetSecondaryHoursType 
    
    
    func (x *Place_OpeningHours) GetSecondaryHoursType() Place_OpeningHours_SecondaryHoursType

### func (*Place_OpeningHours) GetSpecialDays 
    
    
    func (x *Place_OpeningHours) GetSpecialDays() []*Place_OpeningHours_SpecialDay

### func (*Place_OpeningHours) GetWeekdayDescriptions 
    
    
    func (x *Place_OpeningHours) GetWeekdayDescriptions() [][string](https://pkg.go.dev/builtin#string)

### func (*Place_OpeningHours) ProtoMessage 
    
    
    func (*Place_OpeningHours) ProtoMessage()

### func (*Place_OpeningHours) ProtoReflect 
    
    
    func (x *Place_OpeningHours) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_OpeningHours) Reset 
    
    
    func (x *Place_OpeningHours) Reset()

### func (*Place_OpeningHours) String 
    
    
    func (x *Place_OpeningHours) String() [string](https://pkg.go.dev/builtin#string)

## Place_OpeningHours_Period
    
    
    type Place_OpeningHours_Period struct {
    
    	// The time that the place starts to be open.
    	Open *Place_OpeningHours_Period_Point `protobuf:"bytes,1,opt,name=open,proto3" json:"open,omitempty"`
    	// The time that the place starts to be closed.
    	Close *Place_OpeningHours_Period_Point `protobuf:"bytes,2,opt,name=close,proto3" json:"close,omitempty"`
    	// contains filtered or unexported fields
    }

A period the place remains in open_now status.

### func (*Place_OpeningHours_Period) Descriptor 
    
    
    func (*Place_OpeningHours_Period) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_OpeningHours_Period.ProtoReflect.Descriptor instead.

### func (*Place_OpeningHours_Period) GetClose 
    
    
    func (x *Place_OpeningHours_Period) GetClose() *Place_OpeningHours_Period_Point

### func (*Place_OpeningHours_Period) GetOpen 
    
    
    func (x *Place_OpeningHours_Period) GetOpen() *Place_OpeningHours_Period_Point

### func (*Place_OpeningHours_Period) ProtoMessage 
    
    
    func (*Place_OpeningHours_Period) ProtoMessage()

### func (*Place_OpeningHours_Period) ProtoReflect 
    
    
    func (x *Place_OpeningHours_Period) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_OpeningHours_Period) Reset 
    
    
    func (x *Place_OpeningHours_Period) Reset()

### func (*Place_OpeningHours_Period) String 
    
    
    func (x *Place_OpeningHours_Period) String() [string](https://pkg.go.dev/builtin#string)

## Place_OpeningHours_Period_Point
    
    
    type Place_OpeningHours_Period_Point struct {
    
    	// A day of the week, as an integer in the range 0-6.  0 is Sunday, 1 is
    	// Monday, etc.
    	Day *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=day,proto3,oneof" json:"day,omitempty"`
    	// The hour in 24 hour format. Ranges from 0 to 23.
    	Hour *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=hour,proto3,oneof" json:"hour,omitempty"`
    	// The minute. Ranges from 0 to 59.
    	Minute *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=minute,proto3,oneof" json:"minute,omitempty"`
    	// Date in the local timezone for the place.
    	Date *date.Date `protobuf:"bytes,6,opt,name=date,proto3" json:"date,omitempty"`
    	// Whether or not this endpoint was truncated. Truncation occurs when
    	// the real hours are outside the times we are willing to return hours
    	// between, so we truncate the hours back to these boundaries. This
    	// ensures that at most 24 * 7 hours from midnight of the day of the
    	// request are returned.
    	Truncated [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=truncated,proto3" json:"truncated,omitempty"`
    	// contains filtered or unexported fields
    }

Status changing points.

### func (*Place_OpeningHours_Period_Point) Descriptor 
    
    
    func (*Place_OpeningHours_Period_Point) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_OpeningHours_Period_Point.ProtoReflect.Descriptor instead.

### func (*Place_OpeningHours_Period_Point) GetDate 
    
    
    func (x *Place_OpeningHours_Period_Point) GetDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*Place_OpeningHours_Period_Point) GetDay 
    
    
    func (x *Place_OpeningHours_Period_Point) GetDay() [int32](https://pkg.go.dev/builtin#int32)

### func (*Place_OpeningHours_Period_Point) GetHour 
    
    
    func (x *Place_OpeningHours_Period_Point) GetHour() [int32](https://pkg.go.dev/builtin#int32)

### func (*Place_OpeningHours_Period_Point) GetMinute 
    
    
    func (x *Place_OpeningHours_Period_Point) GetMinute() [int32](https://pkg.go.dev/builtin#int32)

### func (*Place_OpeningHours_Period_Point) GetTruncated 
    
    
    func (x *Place_OpeningHours_Period_Point) GetTruncated() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_OpeningHours_Period_Point) ProtoMessage 
    
    
    func (*Place_OpeningHours_Period_Point) ProtoMessage()

### func (*Place_OpeningHours_Period_Point) ProtoReflect 
    
    
    func (x *Place_OpeningHours_Period_Point) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_OpeningHours_Period_Point) Reset 
    
    
    func (x *Place_OpeningHours_Period_Point) Reset()

### func (*Place_OpeningHours_Period_Point) String 
    
    
    func (x *Place_OpeningHours_Period_Point) String() [string](https://pkg.go.dev/builtin#string)

## Place_OpeningHours_SecondaryHoursType
    
    
    type Place_OpeningHours_SecondaryHoursType [int32](https://pkg.go.dev/builtin#int32)

A type used to identify the type of secondary hours.

### Place_OpeningHours_SECONDARY_HOURS_TYPE_UNSPECIFIED, Place_OpeningHours_DRIVE_THROUGH, Place_OpeningHours_HAPPY_HOUR, Place_OpeningHours_DELIVERY, Place_OpeningHours_TAKEOUT, Place_OpeningHours_KITCHEN, Place_OpeningHours_BREAKFAST, Place_OpeningHours_LUNCH, Place_OpeningHours_DINNER, Place_OpeningHours_BRUNCH, Place_OpeningHours_PICKUP, Place_OpeningHours_ACCESS, Place_OpeningHours_SENIOR_HOURS, Place_OpeningHours_ONLINE_SERVICE_HOURS
    
    
    const (
    	// Default value when secondary hour type is not specified.
    	Place_OpeningHours_SECONDARY_HOURS_TYPE_UNSPECIFIED Place_OpeningHours_SecondaryHoursType = 0
    	// The drive-through hour for banks, restaurants, or pharmacies.
    	Place_OpeningHours_DRIVE_THROUGH Place_OpeningHours_SecondaryHoursType = 1
    	// The happy hour.
    	Place_OpeningHours_HAPPY_HOUR Place_OpeningHours_SecondaryHoursType = 2
    	// The delivery hour.
    	Place_OpeningHours_DELIVERY Place_OpeningHours_SecondaryHoursType = 3
    	// The takeout hour.
    	Place_OpeningHours_TAKEOUT Place_OpeningHours_SecondaryHoursType = 4
    	// The kitchen hour.
    	Place_OpeningHours_KITCHEN Place_OpeningHours_SecondaryHoursType = 5
    	// The breakfast hour.
    	Place_OpeningHours_BREAKFAST Place_OpeningHours_SecondaryHoursType = 6
    	// The lunch hour.
    	Place_OpeningHours_LUNCH Place_OpeningHours_SecondaryHoursType = 7
    	// The dinner hour.
    	Place_OpeningHours_DINNER Place_OpeningHours_SecondaryHoursType = 8
    	// The brunch hour.
    	Place_OpeningHours_BRUNCH Place_OpeningHours_SecondaryHoursType = 9
    	// The pickup hour.
    	Place_OpeningHours_PICKUP Place_OpeningHours_SecondaryHoursType = 10
    	// The access hours for storage places.
    	Place_OpeningHours_ACCESS Place_OpeningHours_SecondaryHoursType = 11
    	// The special hours for seniors.
    	Place_OpeningHours_SENIOR_HOURS Place_OpeningHours_SecondaryHoursType = 12
    	// The online service hours.
    	Place_OpeningHours_ONLINE_SERVICE_HOURS Place_OpeningHours_SecondaryHoursType = 13
    )

### func (Place_OpeningHours_SecondaryHoursType) Descriptor 
    
    
    func (Place_OpeningHours_SecondaryHoursType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Place_OpeningHours_SecondaryHoursType) Enum 
    
    
    func (x Place_OpeningHours_SecondaryHoursType) Enum() *Place_OpeningHours_SecondaryHoursType

### func (Place_OpeningHours_SecondaryHoursType) EnumDescriptor 
    
    
    func (Place_OpeningHours_SecondaryHoursType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_OpeningHours_SecondaryHoursType.Descriptor instead.

### func (Place_OpeningHours_SecondaryHoursType) Number 
    
    
    func (x Place_OpeningHours_SecondaryHoursType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Place_OpeningHours_SecondaryHoursType) String 
    
    
    func (x Place_OpeningHours_SecondaryHoursType) String() [string](https://pkg.go.dev/builtin#string)

### func (Place_OpeningHours_SecondaryHoursType) Type 
    
    
    func (Place_OpeningHours_SecondaryHoursType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Place_OpeningHours_SpecialDay
    
    
    type Place_OpeningHours_SpecialDay struct {
    
    	// The date of this special day.
    	Date *date.Date `protobuf:"bytes,1,opt,name=date,proto3" json:"date,omitempty"`
    	// contains filtered or unexported fields
    }

Structured information for special days that fall within the period that the returned opening hours cover. Special days are days that could impact the business hours of a place, e.g. Christmas day.

### func (*Place_OpeningHours_SpecialDay) Descriptor 
    
    
    func (*Place_OpeningHours_SpecialDay) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_OpeningHours_SpecialDay.ProtoReflect.Descriptor instead.

### func (*Place_OpeningHours_SpecialDay) GetDate 
    
    
    func (x *Place_OpeningHours_SpecialDay) GetDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*Place_OpeningHours_SpecialDay) ProtoMessage 
    
    
    func (*Place_OpeningHours_SpecialDay) ProtoMessage()

### func (*Place_OpeningHours_SpecialDay) ProtoReflect 
    
    
    func (x *Place_OpeningHours_SpecialDay) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_OpeningHours_SpecialDay) Reset 
    
    
    func (x *Place_OpeningHours_SpecialDay) Reset()

### func (*Place_OpeningHours_SpecialDay) String 
    
    
    func (x *Place_OpeningHours_SpecialDay) String() [string](https://pkg.go.dev/builtin#string)

## Place_ParkingOptions
    
    
    type Place_ParkingOptions struct {
    
    	// Place offers free parking lots.
    	FreeParkingLot *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=free_parking_lot,json=freeParkingLot,proto3,oneof" json:"free_parking_lot,omitempty"`
    	// Place offers paid parking lots.
    	PaidParkingLot *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=paid_parking_lot,json=paidParkingLot,proto3,oneof" json:"paid_parking_lot,omitempty"`
    	// Place offers free street parking.
    	FreeStreetParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=free_street_parking,json=freeStreetParking,proto3,oneof" json:"free_street_parking,omitempty"`
    	// Place offers paid street parking.
    	PaidStreetParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=paid_street_parking,json=paidStreetParking,proto3,oneof" json:"paid_street_parking,omitempty"`
    	// Place offers valet parking.
    	ValetParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=valet_parking,json=valetParking,proto3,oneof" json:"valet_parking,omitempty"`
    	// Place offers free garage parking.
    	FreeGarageParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=free_garage_parking,json=freeGarageParking,proto3,oneof" json:"free_garage_parking,omitempty"`
    	// Place offers paid garage parking.
    	PaidGarageParking *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=paid_garage_parking,json=paidGarageParking,proto3,oneof" json:"paid_garage_parking,omitempty"`
    	// contains filtered or unexported fields
    }

Information about parking options for the place. A parking lot could support more than one option at the same time.

### func (*Place_ParkingOptions) Descriptor 
    
    
    func (*Place_ParkingOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ParkingOptions.ProtoReflect.Descriptor instead.

### func (*Place_ParkingOptions) GetFreeGarageParking 
    
    
    func (x *Place_ParkingOptions) GetFreeGarageParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetFreeParkingLot 
    
    
    func (x *Place_ParkingOptions) GetFreeParkingLot() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetFreeStreetParking 
    
    
    func (x *Place_ParkingOptions) GetFreeStreetParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetPaidGarageParking 
    
    
    func (x *Place_ParkingOptions) GetPaidGarageParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetPaidParkingLot 
    
    
    func (x *Place_ParkingOptions) GetPaidParkingLot() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetPaidStreetParking 
    
    
    func (x *Place_ParkingOptions) GetPaidStreetParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) GetValetParking 
    
    
    func (x *Place_ParkingOptions) GetValetParking() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_ParkingOptions) ProtoMessage 
    
    
    func (*Place_ParkingOptions) ProtoMessage()

### func (*Place_ParkingOptions) ProtoReflect 
    
    
    func (x *Place_ParkingOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ParkingOptions) Reset 
    
    
    func (x *Place_ParkingOptions) Reset()

### func (*Place_ParkingOptions) String 
    
    
    func (x *Place_ParkingOptions) String() [string](https://pkg.go.dev/builtin#string)

## Place_PaymentOptions
    
    
    type Place_PaymentOptions struct {
    
    	// Place accepts credit cards as payment.
    	AcceptsCreditCards *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=accepts_credit_cards,json=acceptsCreditCards,proto3,oneof" json:"accepts_credit_cards,omitempty"`
    	// Place accepts debit cards as payment.
    	AcceptsDebitCards *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=accepts_debit_cards,json=acceptsDebitCards,proto3,oneof" json:"accepts_debit_cards,omitempty"`
    	// Place accepts cash only as payment. Places with this attribute may still
    	// accept other payment methods.
    	AcceptsCashOnly *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=accepts_cash_only,json=acceptsCashOnly,proto3,oneof" json:"accepts_cash_only,omitempty"`
    	// Place accepts NFC payments.
    	AcceptsNfc *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=accepts_nfc,json=acceptsNfc,proto3,oneof" json:"accepts_nfc,omitempty"`
    	// contains filtered or unexported fields
    }

Payment options the place accepts.

### func (*Place_PaymentOptions) Descriptor 
    
    
    func (*Place_PaymentOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_PaymentOptions.ProtoReflect.Descriptor instead.

### func (*Place_PaymentOptions) GetAcceptsCashOnly 
    
    
    func (x *Place_PaymentOptions) GetAcceptsCashOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_PaymentOptions) GetAcceptsCreditCards 
    
    
    func (x *Place_PaymentOptions) GetAcceptsCreditCards() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_PaymentOptions) GetAcceptsDebitCards 
    
    
    func (x *Place_PaymentOptions) GetAcceptsDebitCards() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_PaymentOptions) GetAcceptsNfc 
    
    
    func (x *Place_PaymentOptions) GetAcceptsNfc() [bool](https://pkg.go.dev/builtin#bool)

### func (*Place_PaymentOptions) ProtoMessage 
    
    
    func (*Place_PaymentOptions) ProtoMessage()

### func (*Place_PaymentOptions) ProtoReflect 
    
    
    func (x *Place_PaymentOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_PaymentOptions) Reset 
    
    
    func (x *Place_PaymentOptions) Reset()

### func (*Place_PaymentOptions) String 
    
    
    func (x *Place_PaymentOptions) String() [string](https://pkg.go.dev/builtin#string)

## Place_PlusCode
    
    
    type Place_PlusCode struct {
    
    	// Place's global (full) code, such as "9FWM33GV+HQ", representing an
    	// 1/8000 by 1/8000 degree area (~14 by 14 meters).
    	GlobalCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=global_code,json=globalCode,proto3" json:"global_code,omitempty"`
    	// Place's compound code, such as "33GV+HQ, Ramberg, Norway", containing
    	// the suffix of the global code and replacing the prefix with a formatted
    	// name of a reference entity.
    	CompoundCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=compound_code,json=compoundCode,proto3" json:"compound_code,omitempty"`
    	// contains filtered or unexported fields
    }

Plus code (<http://plus.codes>) is a location reference with two formats: global code defining a 14mx14m (1/8000th of a degree) or smaller rectangle, and compound code, replacing the prefix with a reference location.

### func (*Place_PlusCode) Descriptor 
    
    
    func (*Place_PlusCode) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_PlusCode.ProtoReflect.Descriptor instead.

### func (*Place_PlusCode) GetCompoundCode 
    
    
    func (x *Place_PlusCode) GetCompoundCode() [string](https://pkg.go.dev/builtin#string)

### func (*Place_PlusCode) GetGlobalCode 
    
    
    func (x *Place_PlusCode) GetGlobalCode() [string](https://pkg.go.dev/builtin#string)

### func (*Place_PlusCode) ProtoMessage 
    
    
    func (*Place_PlusCode) ProtoMessage()

### func (*Place_PlusCode) ProtoReflect 
    
    
    func (x *Place_PlusCode) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_PlusCode) Reset 
    
    
    func (x *Place_PlusCode) Reset()

### func (*Place_PlusCode) String 
    
    
    func (x *Place_PlusCode) String() [string](https://pkg.go.dev/builtin#string)

## Place_ReviewSummary
    
    
    type Place_ReviewSummary struct {
    
    	// The summary of user reviews.
    	Text *localized_text.LocalizedText `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// A link where users can flag a problem with the summary.
    	FlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=flag_content_uri,json=flagContentUri,proto3" json:"flag_content_uri,omitempty"`
    	// The AI disclosure message "Summarized with Gemini"
    	// (and its localized variants). This will be in the language specified in
    	// the request if available.
    	DisclosureText *localized_text.LocalizedText `protobuf:"bytes,3,opt,name=disclosure_text,json=disclosureText,proto3" json:"disclosure_text,omitempty"`
    	// A link to show reviews of this place on Google Maps.
    	ReviewsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=reviews_uri,json=reviewsUri,proto3" json:"reviews_uri,omitempty"`
    	// contains filtered or unexported fields
    }

AI-generated summary of the place using user reviews.

### func (*Place_ReviewSummary) Descriptor 
    
    
    func (*Place_ReviewSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_ReviewSummary.ProtoReflect.Descriptor instead.

### func (*Place_ReviewSummary) GetDisclosureText 
    
    
    func (x *Place_ReviewSummary) GetDisclosureText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_ReviewSummary) GetFlagContentUri 
    
    
    func (x *Place_ReviewSummary) GetFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ReviewSummary) GetReviewsUri 
    
    
    func (x *Place_ReviewSummary) GetReviewsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Place_ReviewSummary) GetText 
    
    
    func (x *Place_ReviewSummary) GetText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Place_ReviewSummary) ProtoMessage 
    
    
    func (*Place_ReviewSummary) ProtoMessage()

### func (*Place_ReviewSummary) ProtoReflect 
    
    
    func (x *Place_ReviewSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_ReviewSummary) Reset 
    
    
    func (x *Place_ReviewSummary) Reset()

### func (*Place_ReviewSummary) String 
    
    
    func (x *Place_ReviewSummary) String() [string](https://pkg.go.dev/builtin#string)

## Place_SubDestination
    
    
    type Place_SubDestination struct {
    
    	// The resource name of the sub-destination.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The place id of the sub-destination.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
    	// contains filtered or unexported fields
    }

Sub-destinations are specific places associated with a main place. These provide more specific destinations for users who are searching within a large or complex place, like an airport, national park, university, or stadium. For example, sub-destinations at an airport might include associated terminals and parking lots. Sub-destinations return the place ID and place resource name, which can be used in subsequent Place Details (New) requests to fetch richer details, including the sub-destination's display name and location.

### func (*Place_SubDestination) Descriptor 
    
    
    func (*Place_SubDestination) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place_SubDestination.ProtoReflect.Descriptor instead.

### func (*Place_SubDestination) GetId 
    
    
    func (x *Place_SubDestination) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*Place_SubDestination) GetName 
    
    
    func (x *Place_SubDestination) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Place_SubDestination) ProtoMessage 
    
    
    func (*Place_SubDestination) ProtoMessage()

### func (*Place_SubDestination) ProtoReflect 
    
    
    func (x *Place_SubDestination) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place_SubDestination) Reset 
    
    
    func (x *Place_SubDestination) Reset()

### func (*Place_SubDestination) String 
    
    
    func (x *Place_SubDestination) String() [string](https://pkg.go.dev/builtin#string)

## PlacesClient
    
    
    type PlacesClient interface {
    	// Search for places near locations.
    	SearchNearby(ctx context.Context, in *SearchNearbyRequest, opts ...grpc.CallOption) (*SearchNearbyResponse, [error](https://pkg.go.dev/builtin#error))
    	// Text query based place search.
    	SearchText(ctx context.Context, in *SearchTextRequest, opts ...grpc.CallOption) (*SearchTextResponse, [error](https://pkg.go.dev/builtin#error))
    	// Get a photo media with a photo reference string.
    	GetPhotoMedia(ctx context.Context, in *GetPhotoMediaRequest, opts ...grpc.CallOption) (*PhotoMedia, [error](https://pkg.go.dev/builtin#error))
    	// Get the details of a place based on its resource name, which is a string
    	// in the `places/{place_id}` format.
    	GetPlace(ctx context.Context, in *GetPlaceRequest, opts ...grpc.CallOption) (*Place, [error](https://pkg.go.dev/builtin#error))
    	// Returns predictions for the given input.
    	AutocompletePlaces(ctx context.Context, in *AutocompletePlacesRequest, opts ...grpc.CallOption) (*AutocompletePlacesResponse, [error](https://pkg.go.dev/builtin#error))
    }

PlacesClient is the client API for Places service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewPlacesClient 
    
    
    func NewPlacesClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) PlacesClient

## PlacesServer
    
    
    type PlacesServer interface {
    	// Search for places near locations.
    	SearchNearby(context.Context, *SearchNearbyRequest) (*SearchNearbyResponse, [error](https://pkg.go.dev/builtin#error))
    	// Text query based place search.
    	SearchText(context.Context, *SearchTextRequest) (*SearchTextResponse, [error](https://pkg.go.dev/builtin#error))
    	// Get a photo media with a photo reference string.
    	GetPhotoMedia(context.Context, *GetPhotoMediaRequest) (*PhotoMedia, [error](https://pkg.go.dev/builtin#error))
    	// Get the details of a place based on its resource name, which is a string
    	// in the `places/{place_id}` format.
    	GetPlace(context.Context, *GetPlaceRequest) (*Place, [error](https://pkg.go.dev/builtin#error))
    	// Returns predictions for the given input.
    	AutocompletePlaces(context.Context, *AutocompletePlacesRequest) (*AutocompletePlacesResponse, [error](https://pkg.go.dev/builtin#error))
    }

PlacesServer is the server API for Places service. All implementations should embed UnimplementedPlacesServer for forward compatibility

## Polyline
    
    
    type Polyline struct {
    
    	// Encapsulates the type of polyline. Routes API output defaults to
    	// `encoded_polyline`.
    	//
    	// Types that are valid to be assigned to PolylineType:
    	//
    	//	*Polyline_EncodedPolyline
    	PolylineType isPolyline_PolylineType `protobuf_oneof:"polyline_type"`
    	// contains filtered or unexported fields
    }

A route polyline. Only supports an [encoded polyline](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which can be passed as a string and includes compression with minimal lossiness. This is the Routes API default output.

### func (*Polyline) Descriptor 
    
    
    func (*Polyline) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Polyline.ProtoReflect.Descriptor instead.

### func (*Polyline) GetEncodedPolyline 
    
    
    func (x *Polyline) GetEncodedPolyline() [string](https://pkg.go.dev/builtin#string)

### func (*Polyline) GetPolylineType 
    
    
    func (x *Polyline) GetPolylineType() isPolyline_PolylineType

### func (*Polyline) ProtoMessage 
    
    
    func (*Polyline) ProtoMessage()

### func (*Polyline) ProtoReflect 
    
    
    func (x *Polyline) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Polyline) Reset 
    
    
    func (x *Polyline) Reset()

### func (*Polyline) String 
    
    
    func (x *Polyline) String() [string](https://pkg.go.dev/builtin#string)

## Polyline_EncodedPolyline
    
    
    type Polyline_EncodedPolyline struct {
    	// An [encoded
    	// polyline](https://developers.google.com/maps/documentation/utilities/polylinealgorithm),
    	// as returned by the [Routes API by
    	// default](https://developers.google.com/maps/documentation/routes/reference/rest/v2/TopLevel/computeRoutes#polylineencoding).
    	// See the
    	// [encoder](https://developers.google.com/maps/documentation/utilities/polylineutility)
    	// and
    	// [decoder](https://developers.google.com/maps/documentation/routes/polylinedecoder)
    	// tools.
    	EncodedPolyline [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=encoded_polyline,json=encodedPolyline,proto3,oneof"`
    }

## PriceLevel
    
    
    type PriceLevel [int32](https://pkg.go.dev/builtin#int32)

Price level of the place.

### PriceLevel_PRICE_LEVEL_UNSPECIFIED, PriceLevel_PRICE_LEVEL_FREE, PriceLevel_PRICE_LEVEL_INEXPENSIVE, PriceLevel_PRICE_LEVEL_MODERATE, PriceLevel_PRICE_LEVEL_EXPENSIVE, PriceLevel_PRICE_LEVEL_VERY_EXPENSIVE
    
    
    const (
    	// Place price level is unspecified or unknown.
    	PriceLevel_PRICE_LEVEL_UNSPECIFIED PriceLevel = 0
    	// Place provides free services.
    	PriceLevel_PRICE_LEVEL_FREE PriceLevel = 1
    	// Place provides inexpensive services.
    	PriceLevel_PRICE_LEVEL_INEXPENSIVE PriceLevel = 2
    	// Place provides moderately priced services.
    	PriceLevel_PRICE_LEVEL_MODERATE PriceLevel = 3
    	// Place provides expensive services.
    	PriceLevel_PRICE_LEVEL_EXPENSIVE PriceLevel = 4
    	// Place provides very expensive services.
    	PriceLevel_PRICE_LEVEL_VERY_EXPENSIVE PriceLevel = 5
    )

### func (PriceLevel) Descriptor 
    
    
    func (PriceLevel) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PriceLevel) Enum 
    
    
    func (x PriceLevel) Enum() *PriceLevel

### func (PriceLevel) EnumDescriptor 
    
    
    func (PriceLevel) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PriceLevel.Descriptor instead.

### func (PriceLevel) Number 
    
    
    func (x PriceLevel) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PriceLevel) String 
    
    
    func (x PriceLevel) String() [string](https://pkg.go.dev/builtin#string)

### func (PriceLevel) Type 
    
    
    func (PriceLevel) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## PriceRange
    
    
    type PriceRange struct {
    
    	// The low end of the price range (inclusive). Price should be at or above
    	// this amount.
    	StartPrice *money.Money `protobuf:"bytes,1,opt,name=start_price,json=startPrice,proto3" json:"start_price,omitempty"`
    	// The high end of the price range (exclusive). Price should be lower than
    	// this amount.
    	EndPrice *money.Money `protobuf:"bytes,2,opt,name=end_price,json=endPrice,proto3" json:"end_price,omitempty"`
    	// contains filtered or unexported fields
    }

The price range associated with a Place. `end_price` could be unset, which indicates a range without upper bound (e.g. "More than $100").

### func (*PriceRange) Descriptor 
    
    
    func (*PriceRange) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PriceRange.ProtoReflect.Descriptor instead.

### func (*PriceRange) GetEndPrice 
    
    
    func (x *PriceRange) GetEndPrice() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*PriceRange) GetStartPrice 
    
    
    func (x *PriceRange) GetStartPrice() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*PriceRange) ProtoMessage 
    
    
    func (*PriceRange) ProtoMessage()

### func (*PriceRange) ProtoReflect 
    
    
    func (x *PriceRange) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PriceRange) Reset 
    
    
    func (x *PriceRange) Reset()

### func (*PriceRange) String 
    
    
    func (x *PriceRange) String() [string](https://pkg.go.dev/builtin#string)

## References
    
    
    type References struct {
    
    	// Reviews that serve as references.
    	Reviews []*Review `protobuf:"bytes,1,rep,name=reviews,proto3" json:"reviews,omitempty"`
    	// The list of resource names of the referenced places. This name can be used
    	// in other APIs that accept Place resource names.
    	Places [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=places,proto3" json:"places,omitempty"`
    	// contains filtered or unexported fields
    }

Experimental: See <https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative> for more details.

Reference that the generative content is related to.

### func (*References) Descriptor 
    
    
    func (*References) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use References.ProtoReflect.Descriptor instead.

### func (*References) GetPlaces 
    
    
    func (x *References) GetPlaces() [][string](https://pkg.go.dev/builtin#string)

### func (*References) GetReviews 
    
    
    func (x *References) GetReviews() []*Review

### func (*References) ProtoMessage 
    
    
    func (*References) ProtoMessage()

### func (*References) ProtoReflect 
    
    
    func (x *References) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*References) Reset 
    
    
    func (x *References) Reset()

### func (*References) String 
    
    
    func (x *References) String() [string](https://pkg.go.dev/builtin#string)

## Review
    
    
    type Review struct {
    
    	// A reference representing this place review which may be used to look up
    	// this place review again (also called the API "resource" name:
    	// `places/{place_id}/reviews/{review}`).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A string of formatted recent time, expressing the review time relative
    	// to the current time in a form appropriate for the language and country.
    	RelativePublishTimeDescription [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=relative_publish_time_description,json=relativePublishTimeDescription,proto3" json:"relative_publish_time_description,omitempty"`
    	// The localized text of the review.
    	Text *localized_text.LocalizedText `protobuf:"bytes,9,opt,name=text,proto3" json:"text,omitempty"`
    	// The review text in its original language.
    	OriginalText *localized_text.LocalizedText `protobuf:"bytes,12,opt,name=original_text,json=originalText,proto3" json:"original_text,omitempty"`
    	// A number between 1.0 and 5.0, also called the number of stars.
    	Rating [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,7,opt,name=rating,proto3" json:"rating,omitempty"`
    	// This review's author.
    	AuthorAttribution *AuthorAttribution `protobuf:"bytes,13,opt,name=author_attribution,json=authorAttribution,proto3" json:"author_attribution,omitempty"`
    	// Timestamp for the review.
    	PublishTime *timestamppb.Timestamp `protobuf:"bytes,14,opt,name=publish_time,json=publishTime,proto3" json:"publish_time,omitempty"`
    	// A link where users can flag a problem with the review.
    	FlagContentUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,15,opt,name=flag_content_uri,json=flagContentUri,proto3" json:"flag_content_uri,omitempty"`
    	// A link to show the review on Google Maps.
    	GoogleMapsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,16,opt,name=google_maps_uri,json=googleMapsUri,proto3" json:"google_maps_uri,omitempty"`
    	// The date when the author visited the place. This is truncated to the year
    	// and month of the visit.
    	VisitDate *date.Date `protobuf:"bytes,17,opt,name=visit_date,json=visitDate,proto3" json:"visit_date,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a review of a place.

### func (*Review) Descriptor 
    
    
    func (*Review) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Review.ProtoReflect.Descriptor instead.

### func (*Review) GetAuthorAttribution 
    
    
    func (x *Review) GetAuthorAttribution() *AuthorAttribution

### func (*Review) GetFlagContentUri 
    
    
    func (x *Review) GetFlagContentUri() [string](https://pkg.go.dev/builtin#string)

### func (*Review) GetGoogleMapsUri 
    
    
    func (x *Review) GetGoogleMapsUri() [string](https://pkg.go.dev/builtin#string)

### func (*Review) GetName 
    
    
    func (x *Review) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Review) GetOriginalText 
    
    
    func (x *Review) GetOriginalText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Review) GetPublishTime 
    
    
    func (x *Review) GetPublishTime() *timestamppb.Timestamp

### func (*Review) GetRating 
    
    
    func (x *Review) GetRating() [float64](https://pkg.go.dev/builtin#float64)

### func (*Review) GetRelativePublishTimeDescription 
    
    
    func (x *Review) GetRelativePublishTimeDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Review) GetText 
    
    
    func (x *Review) GetText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*Review) GetVisitDate 
    
    
    func (x *Review) GetVisitDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*Review) ProtoMessage 
    
    
    func (*Review) ProtoMessage()

### func (*Review) ProtoReflect 
    
    
    func (x *Review) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Review) Reset 
    
    
    func (x *Review) Reset()

### func (*Review) String 
    
    
    func (x *Review) String() [string](https://pkg.go.dev/builtin#string)

## RouteModifiers
    
    
    type RouteModifiers struct {
    
    	// Optional. When set to true, avoids toll roads where reasonable, giving
    	// preference to routes not containing toll roads. Applies only to the `DRIVE`
    	// and `TWO_WHEELER` [`TravelMode`][google.maps.places.v1.TravelMode].
    	AvoidTolls [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=avoid_tolls,json=avoidTolls,proto3" json:"avoid_tolls,omitempty"`
    	// Optional. When set to true, avoids highways where reasonable, giving
    	// preference to routes not containing highways. Applies only to the `DRIVE`
    	// and `TWO_WHEELER` [`TravelMode`][google.maps.places.v1.TravelMode].
    	AvoidHighways [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=avoid_highways,json=avoidHighways,proto3" json:"avoid_highways,omitempty"`
    	// Optional. When set to true, avoids ferries where reasonable, giving
    	// preference to routes not containing ferries. Applies only to the `DRIVE`
    	// and `TWO_WHEELER` [`TravelMode`][google.maps.places.v1.TravelMode].
    	AvoidFerries [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=avoid_ferries,json=avoidFerries,proto3" json:"avoid_ferries,omitempty"`
    	// Optional. When set to true, avoids navigating indoors where reasonable,
    	// giving preference to routes not containing indoor navigation. Applies only
    	// to the `WALK` [`TravelMode`][google.maps.places.v1.TravelMode].
    	AvoidIndoor [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=avoid_indoor,json=avoidIndoor,proto3" json:"avoid_indoor,omitempty"`
    	// contains filtered or unexported fields
    }

Encapsulates a set of optional conditions to satisfy when calculating the routes.

### func (*RouteModifiers) Descriptor 
    
    
    func (*RouteModifiers) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RouteModifiers.ProtoReflect.Descriptor instead.

### func (*RouteModifiers) GetAvoidFerries 
    
    
    func (x *RouteModifiers) GetAvoidFerries() [bool](https://pkg.go.dev/builtin#bool)

### func (*RouteModifiers) GetAvoidHighways 
    
    
    func (x *RouteModifiers) GetAvoidHighways() [bool](https://pkg.go.dev/builtin#bool)

### func (*RouteModifiers) GetAvoidIndoor 
    
    
    func (x *RouteModifiers) GetAvoidIndoor() [bool](https://pkg.go.dev/builtin#bool)

### func (*RouteModifiers) GetAvoidTolls 
    
    
    func (x *RouteModifiers) GetAvoidTolls() [bool](https://pkg.go.dev/builtin#bool)

### func (*RouteModifiers) ProtoMessage 
    
    
    func (*RouteModifiers) ProtoMessage()

### func (*RouteModifiers) ProtoReflect 
    
    
    func (x *RouteModifiers) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RouteModifiers) Reset 
    
    
    func (x *RouteModifiers) Reset()

### func (*RouteModifiers) String 
    
    
    func (x *RouteModifiers) String() [string](https://pkg.go.dev/builtin#string)

## RoutingParameters
    
    
    type RoutingParameters struct {
    
    	// Optional. An explicit routing origin that overrides the origin defined in
    	// the polyline. By default, the polyline origin is used.
    	Origin *latlng.LatLng `protobuf:"bytes,1,opt,name=origin,proto3" json:"origin,omitempty"`
    	// Optional. The travel mode.
    	TravelMode TravelMode `protobuf:"varint,2,opt,name=travel_mode,json=travelMode,proto3,enum=google.maps.places.v1.TravelMode" json:"travel_mode,omitempty"`
    	// Optional. The route modifiers.
    	RouteModifiers *RouteModifiers `protobuf:"bytes,3,opt,name=route_modifiers,json=routeModifiers,proto3" json:"route_modifiers,omitempty"`
    	// Optional. Specifies how to compute the routing summaries. The server
    	// attempts to use the selected routing preference to compute the route. The
    	// traffic aware routing preference is only available for the `DRIVE` or
    	// `TWO_WHEELER` `travelMode`.
    	RoutingPreference RoutingPreference `protobuf:"varint,4,opt,name=routing_preference,json=routingPreference,proto3,enum=google.maps.places.v1.RoutingPreference" json:"routing_preference,omitempty"`
    	// contains filtered or unexported fields
    }

Parameters to configure the routing calculations to the places in the response, both along a route (where result ranking will be influenced) and for calculating travel times on results.

### func (*RoutingParameters) Descriptor 
    
    
    func (*RoutingParameters) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RoutingParameters.ProtoReflect.Descriptor instead.

### func (*RoutingParameters) GetOrigin 
    
    
    func (x *RoutingParameters) GetOrigin() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*RoutingParameters) GetRouteModifiers 
    
    
    func (x *RoutingParameters) GetRouteModifiers() *RouteModifiers

### func (*RoutingParameters) GetRoutingPreference 
    
    
    func (x *RoutingParameters) GetRoutingPreference() RoutingPreference

### func (*RoutingParameters) GetTravelMode 
    
    
    func (x *RoutingParameters) GetTravelMode() TravelMode

### func (*RoutingParameters) ProtoMessage 
    
    
    func (*RoutingParameters) ProtoMessage()

### func (*RoutingParameters) ProtoReflect 
    
    
    func (x *RoutingParameters) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RoutingParameters) Reset 
    
    
    func (x *RoutingParameters) Reset()

### func (*RoutingParameters) String 
    
    
    func (x *RoutingParameters) String() [string](https://pkg.go.dev/builtin#string)

## RoutingPreference
    
    
    type RoutingPreference [int32](https://pkg.go.dev/builtin#int32)

A set of values that specify factors to take into consideration when calculating the route.

### RoutingPreference_ROUTING_PREFERENCE_UNSPECIFIED, RoutingPreference_TRAFFIC_UNAWARE, RoutingPreference_TRAFFIC_AWARE, RoutingPreference_TRAFFIC_AWARE_OPTIMAL
    
    
    const (
    	// No routing preference specified. Default to `TRAFFIC_UNAWARE`.
    	RoutingPreference_ROUTING_PREFERENCE_UNSPECIFIED RoutingPreference = 0
    	// Computes routes without taking live traffic conditions into consideration.
    	// Suitable when traffic conditions don't matter or are not applicable.
    	// Using this value produces the lowest latency.
    	// Note: For [`TravelMode`][google.maps.places.v1.TravelMode]
    	// `DRIVE` and `TWO_WHEELER`, the route and duration chosen are based on road
    	// network and average time-independent traffic conditions, not current road
    	// conditions. Consequently, routes may include roads that are temporarily
    	// closed. Results for a given
    	// request may vary over time due to changes in the road network, updated
    	// average traffic conditions, and the distributed nature of the service.
    	// Results may also vary between nearly-equivalent routes at any time or
    	// frequency.
    	RoutingPreference_TRAFFIC_UNAWARE RoutingPreference = 1
    	// Calculates routes taking live traffic conditions into consideration.
    	// In contrast to `TRAFFIC_AWARE_OPTIMAL`, some optimizations are applied to
    	// significantly reduce latency.
    	RoutingPreference_TRAFFIC_AWARE RoutingPreference = 2
    	// Calculates the routes taking live traffic conditions into consideration,
    	// without applying most performance optimizations. Using this value produces
    	// the highest latency.
    	RoutingPreference_TRAFFIC_AWARE_OPTIMAL RoutingPreference = 3
    )

### func (RoutingPreference) Descriptor 
    
    
    func (RoutingPreference) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RoutingPreference) Enum 
    
    
    func (x RoutingPreference) Enum() *RoutingPreference

### func (RoutingPreference) EnumDescriptor 
    
    
    func (RoutingPreference) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RoutingPreference.Descriptor instead.

### func (RoutingPreference) Number 
    
    
    func (x RoutingPreference) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RoutingPreference) String 
    
    
    func (x RoutingPreference) String() [string](https://pkg.go.dev/builtin#string)

### func (RoutingPreference) Type 
    
    
    func (RoutingPreference) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RoutingSummary
    
    
    type RoutingSummary struct {
    
    	// The legs of the trip.
    	//
    	// When you calculate travel duration and distance from a set origin, `legs`
    	// contains a single leg containing the duration and distance from the origin
    	// to the destination.  When you do a search along route, `legs` contains two
    	// legs: one from the origin to place, and one from the place to the
    	// destination.
    	Legs []*RoutingSummary_Leg `protobuf:"bytes,1,rep,name=legs,proto3" json:"legs,omitempty"`
    	// A link to show directions on Google Maps using the waypoints from the given
    	// routing summary. The route generated by this link is not guaranteed to be
    	// the same as the route used to generate the routing summary.
    	// The link uses information provided in the request, from fields including
    	// `routingParameters` and `searchAlongRouteParameters` when applicable, to
    	// generate the directions link.
    	DirectionsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=directions_uri,json=directionsUri,proto3" json:"directions_uri,omitempty"`
    	// contains filtered or unexported fields
    }

The duration and distance from the routing origin to a place in the response, and a second leg from that place to the destination, if requested. **Note:** Adding `routingSummaries` in the field mask without also including either the `routingParameters.origin` parameter or the `searchAlongRouteParameters.polyline.encodedPolyline` parameter in the request causes an error.

### func (*RoutingSummary) Descriptor 
    
    
    func (*RoutingSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RoutingSummary.ProtoReflect.Descriptor instead.

### func (*RoutingSummary) GetDirectionsUri 
    
    
    func (x *RoutingSummary) GetDirectionsUri() [string](https://pkg.go.dev/builtin#string)

### func (*RoutingSummary) GetLegs 
    
    
    func (x *RoutingSummary) GetLegs() []*RoutingSummary_Leg

### func (*RoutingSummary) ProtoMessage 
    
    
    func (*RoutingSummary) ProtoMessage()

### func (*RoutingSummary) ProtoReflect 
    
    
    func (x *RoutingSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RoutingSummary) Reset 
    
    
    func (x *RoutingSummary) Reset()

### func (*RoutingSummary) String 
    
    
    func (x *RoutingSummary) String() [string](https://pkg.go.dev/builtin#string)

## RoutingSummary_Leg
    
    
    type RoutingSummary_Leg struct {
    
    	// The time it takes to complete this leg of the trip.
    	Duration *durationpb.Duration `protobuf:"bytes,1,opt,name=duration,proto3" json:"duration,omitempty"`
    	// The distance of this leg of the trip.
    	DistanceMeters [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=distance_meters,json=distanceMeters,proto3" json:"distance_meters,omitempty"`
    	// contains filtered or unexported fields
    }

A leg is a single portion of a journey from one location to another.

### func (*RoutingSummary_Leg) Descriptor 
    
    
    func (*RoutingSummary_Leg) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RoutingSummary_Leg.ProtoReflect.Descriptor instead.

### func (*RoutingSummary_Leg) GetDistanceMeters 
    
    
    func (x *RoutingSummary_Leg) GetDistanceMeters() [int32](https://pkg.go.dev/builtin#int32)

### func (*RoutingSummary_Leg) GetDuration 
    
    
    func (x *RoutingSummary_Leg) GetDuration() *durationpb.Duration

### func (*RoutingSummary_Leg) ProtoMessage 
    
    
    func (*RoutingSummary_Leg) ProtoMessage()

### func (*RoutingSummary_Leg) ProtoReflect 
    
    
    func (x *RoutingSummary_Leg) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RoutingSummary_Leg) Reset 
    
    
    func (x *RoutingSummary_Leg) Reset()

### func (*RoutingSummary_Leg) String 
    
    
    func (x *RoutingSummary_Leg) String() [string](https://pkg.go.dev/builtin#string)

## SearchNearbyRequest
    
    
    type SearchNearbyRequest struct {
    
    	// Place details will be displayed with the preferred language if available.
    	// If the language code is unspecified or unrecognized, place details of any
    	// language may be returned, with a preference for English if such details
    	// exist.
    	//
    	// Current list of supported languages:
    	// https://developers.google.com/maps/faq#languagesupport.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// The Unicode country/region code (CLDR) of the location where the
    	// request is coming from. This parameter is used to display the place
    	// details, like region-specific place name, if available. The parameter can
    	// affect results based on applicable law.
    	//
    	// For more information, see
    	// https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.
    	//
    	// Note that 3-digit region codes are not currently supported.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// Included Place type (eg, "restaurant" or "gas_station") from
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	//
    	// Up to 50 types from [Table
    	// A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a)
    	// may be specified.
    	//
    	// If there are any conflicting types, i.e. a type appears in both
    	// included_types and excluded_types, an INVALID_ARGUMENT error is
    	// returned.
    	//
    	// If a Place type is specified with multiple type restrictions, only places
    	// that satisfy all of the restrictions are returned. For example, if we
    	// have {included_types = ["restaurant"], excluded_primary_types =
    	// ["restaurant"]}, the returned places provide "restaurant"
    	// related services but do not operate primarily as "restaurants".
    	IncludedTypes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=included_types,json=includedTypes,proto3" json:"included_types,omitempty"`
    	// Excluded Place type (eg, "restaurant" or "gas_station") from
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	//
    	// Up to 50 types from [Table
    	// A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a)
    	// may be specified.
    	//
    	// If the client provides both included_types (e.g. restaurant) and
    	// excluded_types (e.g. cafe), then the response should include places that
    	// are restaurant but not cafe. The response includes places that match at
    	// least one of the included_types and none of the excluded_types.
    	//
    	// If there are any conflicting types, i.e. a type appears in both
    	// included_types and excluded_types, an INVALID_ARGUMENT error is returned.
    	//
    	// If a Place type is specified with multiple type restrictions, only places
    	// that satisfy all of the restrictions are returned. For example, if we
    	// have {included_types = ["restaurant"], excluded_primary_types =
    	// ["restaurant"]}, the returned places provide "restaurant"
    	// related services but do not operate primarily as "restaurants".
    	ExcludedTypes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=excluded_types,json=excludedTypes,proto3" json:"excluded_types,omitempty"`
    	// Included primary Place type (e.g. "restaurant" or "gas_station") from
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	// A place can only have a single primary type from the supported types table
    	// associated with it.
    	//
    	// Up to 50 types from [Table
    	// A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a)
    	// may be specified.
    	//
    	// If there are any conflicting primary types, i.e. a type appears in both
    	// included_primary_types and excluded_primary_types, an INVALID_ARGUMENT
    	// error is returned.
    	//
    	// If a Place type is specified with multiple type restrictions, only places
    	// that satisfy all of the restrictions are returned. For example, if we
    	// have {included_types = ["restaurant"], excluded_primary_types =
    	// ["restaurant"]}, the returned places provide "restaurant"
    	// related services but do not operate primarily as "restaurants".
    	IncludedPrimaryTypes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=included_primary_types,json=includedPrimaryTypes,proto3" json:"included_primary_types,omitempty"`
    	// Excluded primary Place type (e.g. "restaurant" or "gas_station") from
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	//
    	// Up to 50 types from [Table
    	// A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a)
    	// may be specified.
    	//
    	// If there are any conflicting primary types, i.e. a type appears in both
    	// included_primary_types and excluded_primary_types, an INVALID_ARGUMENT
    	// error is returned.
    	//
    	// If a Place type is specified with multiple type restrictions, only places
    	// that satisfy all of the restrictions are returned. For example, if we
    	// have {included_types = ["restaurant"], excluded_primary_types =
    	// ["restaurant"]}, the returned places provide "restaurant"
    	// related services but do not operate primarily as "restaurants".
    	ExcludedPrimaryTypes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,rep,name=excluded_primary_types,json=excludedPrimaryTypes,proto3" json:"excluded_primary_types,omitempty"`
    	// Maximum number of results to return. It must be between 1 and 20 (default),
    	// inclusively. If the number is unset, it falls back to the upper limit. If
    	// the number is set to negative or exceeds the upper limit, an
    	// INVALID_ARGUMENT error is returned.
    	MaxResultCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=max_result_count,json=maxResultCount,proto3" json:"max_result_count,omitempty"`
    	// Required. The region to search.
    	LocationRestriction *SearchNearbyRequest_LocationRestriction `protobuf:"bytes,8,opt,name=location_restriction,json=locationRestriction,proto3" json:"location_restriction,omitempty"`
    	// How results will be ranked in the response.
    	RankPreference SearchNearbyRequest_RankPreference `protobuf:"varint,9,opt,name=rank_preference,json=rankPreference,proto3,enum=google.maps.places.v1.SearchNearbyRequest_RankPreference" json:"rank_preference,omitempty"`
    	// Optional. Parameters that affect the routing to the search results.
    	RoutingParameters *RoutingParameters `protobuf:"bytes,10,opt,name=routing_parameters,json=routingParameters,proto3" json:"routing_parameters,omitempty"`
    	// Optional. If true, include businesses that are not yet open but will open
    	// in the future.
    	IncludeFutureOpeningBusinesses [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,15,opt,name=include_future_opening_businesses,json=includeFutureOpeningBusinesses,proto3" json:"include_future_opening_businesses,omitempty"`
    	// contains filtered or unexported fields
    }

Request proto for Search Nearby.

### func (*SearchNearbyRequest) Descriptor 
    
    
    func (*SearchNearbyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchNearbyRequest.ProtoReflect.Descriptor instead.

### func (*SearchNearbyRequest) GetExcludedPrimaryTypes 
    
    
    func (x *SearchNearbyRequest) GetExcludedPrimaryTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetExcludedTypes 
    
    
    func (x *SearchNearbyRequest) GetExcludedTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetIncludeFutureOpeningBusinesses 
    
    
    func (x *SearchNearbyRequest) GetIncludeFutureOpeningBusinesses() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchNearbyRequest) GetIncludedPrimaryTypes 
    
    
    func (x *SearchNearbyRequest) GetIncludedPrimaryTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetIncludedTypes 
    
    
    func (x *SearchNearbyRequest) GetIncludedTypes() [][string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetLanguageCode 
    
    
    func (x *SearchNearbyRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetLocationRestriction 
    
    
    func (x *SearchNearbyRequest) GetLocationRestriction() *SearchNearbyRequest_LocationRestriction

### func (*SearchNearbyRequest) GetMaxResultCount 
    
    
    func (x *SearchNearbyRequest) GetMaxResultCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchNearbyRequest) GetRankPreference 
    
    
    func (x *SearchNearbyRequest) GetRankPreference() SearchNearbyRequest_RankPreference

### func (*SearchNearbyRequest) GetRegionCode 
    
    
    func (x *SearchNearbyRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*SearchNearbyRequest) GetRoutingParameters 
    
    
    func (x *SearchNearbyRequest) GetRoutingParameters() *RoutingParameters

### func (*SearchNearbyRequest) ProtoMessage 
    
    
    func (*SearchNearbyRequest) ProtoMessage()

### func (*SearchNearbyRequest) ProtoReflect 
    
    
    func (x *SearchNearbyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchNearbyRequest) Reset 
    
    
    func (x *SearchNearbyRequest) Reset()

### func (*SearchNearbyRequest) String 
    
    
    func (x *SearchNearbyRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchNearbyRequest_LocationRestriction
    
    
    type SearchNearbyRequest_LocationRestriction struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*SearchNearbyRequest_LocationRestriction_Circle
    	Type isSearchNearbyRequest_LocationRestriction_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The region to search.

### func (*SearchNearbyRequest_LocationRestriction) Descriptor 
    
    
    func (*SearchNearbyRequest_LocationRestriction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchNearbyRequest_LocationRestriction.ProtoReflect.Descriptor instead.

### func (*SearchNearbyRequest_LocationRestriction) GetCircle 
    
    
    func (x *SearchNearbyRequest_LocationRestriction) GetCircle() *Circle

### func (*SearchNearbyRequest_LocationRestriction) GetType 
    
    
    func (x *SearchNearbyRequest_LocationRestriction) GetType() isSearchNearbyRequest_LocationRestriction_Type

### func (*SearchNearbyRequest_LocationRestriction) ProtoMessage 
    
    
    func (*SearchNearbyRequest_LocationRestriction) ProtoMessage()

### func (*SearchNearbyRequest_LocationRestriction) ProtoReflect 
    
    
    func (x *SearchNearbyRequest_LocationRestriction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchNearbyRequest_LocationRestriction) Reset 
    
    
    func (x *SearchNearbyRequest_LocationRestriction) Reset()

### func (*SearchNearbyRequest_LocationRestriction) String 
    
    
    func (x *SearchNearbyRequest_LocationRestriction) String() [string](https://pkg.go.dev/builtin#string)

## SearchNearbyRequest_LocationRestriction_Circle
    
    
    type SearchNearbyRequest_LocationRestriction_Circle struct {
    	// A circle defined by center point and radius.
    	Circle *Circle `protobuf:"bytes,2,opt,name=circle,proto3,oneof"`
    }

## SearchNearbyRequest_RankPreference
    
    
    type SearchNearbyRequest_RankPreference [int32](https://pkg.go.dev/builtin#int32)

How results will be ranked in the response.

### SearchNearbyRequest_RANK_PREFERENCE_UNSPECIFIED, SearchNearbyRequest_DISTANCE, SearchNearbyRequest_POPULARITY
    
    
    const (
    	// RankPreference value not set. Will use rank by POPULARITY by default.
    	SearchNearbyRequest_RANK_PREFERENCE_UNSPECIFIED SearchNearbyRequest_RankPreference = 0
    	// Ranks results by distance.
    	SearchNearbyRequest_DISTANCE SearchNearbyRequest_RankPreference = 1
    	// Ranks results by popularity.
    	SearchNearbyRequest_POPULARITY SearchNearbyRequest_RankPreference = 2
    )

### func (SearchNearbyRequest_RankPreference) Descriptor 
    
    
    func (SearchNearbyRequest_RankPreference) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SearchNearbyRequest_RankPreference) Enum 
    
    
    func (x SearchNearbyRequest_RankPreference) Enum() *SearchNearbyRequest_RankPreference

### func (SearchNearbyRequest_RankPreference) EnumDescriptor 
    
    
    func (SearchNearbyRequest_RankPreference) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchNearbyRequest_RankPreference.Descriptor instead.

### func (SearchNearbyRequest_RankPreference) Number 
    
    
    func (x SearchNearbyRequest_RankPreference) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SearchNearbyRequest_RankPreference) String 
    
    
    func (x SearchNearbyRequest_RankPreference) String() [string](https://pkg.go.dev/builtin#string)

### func (SearchNearbyRequest_RankPreference) Type 
    
    
    func (SearchNearbyRequest_RankPreference) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SearchNearbyResponse
    
    
    type SearchNearbyResponse struct {
    
    	// A list of places that meets user's requirements like places
    	// types, number of places and specific location restriction.
    	Places []*Place `protobuf:"bytes,1,rep,name=places,proto3" json:"places,omitempty"`
    	// A list of routing summaries where each entry associates to the
    	// corresponding place in the same index in the `places` field. If the routing
    	// summary is not available for one of the places, it will contain an empty
    	// entry. This list should have as many entries as the list of places if
    	// requested.
    	RoutingSummaries []*RoutingSummary `protobuf:"bytes,2,rep,name=routing_summaries,json=routingSummaries,proto3" json:"routing_summaries,omitempty"`
    	// contains filtered or unexported fields
    }

Response proto for Search Nearby.

### func (*SearchNearbyResponse) Descriptor 
    
    
    func (*SearchNearbyResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchNearbyResponse.ProtoReflect.Descriptor instead.

### func (*SearchNearbyResponse) GetPlaces 
    
    
    func (x *SearchNearbyResponse) GetPlaces() []*Place

### func (*SearchNearbyResponse) GetRoutingSummaries 
    
    
    func (x *SearchNearbyResponse) GetRoutingSummaries() []*RoutingSummary

### func (*SearchNearbyResponse) ProtoMessage 
    
    
    func (*SearchNearbyResponse) ProtoMessage()

### func (*SearchNearbyResponse) ProtoReflect 
    
    
    func (x *SearchNearbyResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchNearbyResponse) Reset 
    
    
    func (x *SearchNearbyResponse) Reset()

### func (*SearchNearbyResponse) String 
    
    
    func (x *SearchNearbyResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextRequest
    
    
    type SearchTextRequest struct {
    
    	// Required. The text query for textual search.
    	TextQuery [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text_query,json=textQuery,proto3" json:"text_query,omitempty"`
    	// Place details will be displayed with the preferred language if available.
    	// If the language code is unspecified or unrecognized, place details of any
    	// language may be returned, with a preference for English if such details
    	// exist.
    	//
    	// Current list of supported languages:
    	// https://developers.google.com/maps/faq#languagesupport.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// The Unicode country/region code (CLDR) of the location where the
    	// request is coming from. This parameter is used to display the place
    	// details, like region-specific place name, if available. The parameter can
    	// affect results based on applicable law.
    	//
    	// For more information, see
    	// https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.
    	//
    	// Note that 3-digit region codes are not currently supported.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// How results will be ranked in the response.
    	RankPreference SearchTextRequest_RankPreference `protobuf:"varint,4,opt,name=rank_preference,json=rankPreference,proto3,enum=google.maps.places.v1.SearchTextRequest_RankPreference" json:"rank_preference,omitempty"`
    	// The requested place type. Full list of types supported:
    	// https://developers.google.com/maps/documentation/places/web-service/place-types.
    	// Only support one included type.
    	IncludedType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=included_type,json=includedType,proto3" json:"included_type,omitempty"`
    	// Used to restrict the search to places that are currently open.  The default
    	// is false.
    	OpenNow [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=open_now,json=openNow,proto3" json:"open_now,omitempty"`
    	// Filter out results whose average user rating is strictly less than this
    	// limit. A valid value must be a float between 0 and 5 (inclusively) at a
    	// 0.5 cadence i.e. [0, 0.5, 1.0, ... , 5.0] inclusively. The input rating
    	// will round up to the nearest 0.5(ceiling). For instance, a rating of 0.6
    	// will eliminate all results with a less than 1.0 rating.
    	MinRating [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,9,opt,name=min_rating,json=minRating,proto3" json:"min_rating,omitempty"`
    	// Maximum number of results to return. It must be between 1 and 20,
    	// inclusively. The default is 20.  If the number is unset, it falls back to
    	// the upper limit. If the number is set to negative or exceeds the upper
    	// limit, an INVALID_ARGUMENT error is returned.
    	MaxResultCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,10,opt,name=max_result_count,json=maxResultCount,proto3" json:"max_result_count,omitempty"`
    	// Used to restrict the search to places that are marked as certain price
    	// levels. Users can choose any combinations of price levels. Default to
    	// select all price levels.
    	PriceLevels []PriceLevel `protobuf:"varint,11,rep,packed,name=price_levels,json=priceLevels,proto3,enum=google.maps.places.v1.PriceLevel" json:"price_levels,omitempty"`
    	// Used to set strict type filtering for included_type. If set to true, only
    	// results of the same type will be returned. Default to false.
    	StrictTypeFiltering [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=strict_type_filtering,json=strictTypeFiltering,proto3" json:"strict_type_filtering,omitempty"`
    	// The region to search. This location serves as a bias which means results
    	// around given location might be returned. Cannot be set along with
    	// location_restriction.
    	LocationBias *SearchTextRequest_LocationBias `protobuf:"bytes,13,opt,name=location_bias,json=locationBias,proto3" json:"location_bias,omitempty"`
    	// The region to search. This location serves as a restriction which means
    	// results outside given location will not be returned. Cannot be set along
    	// with location_bias.
    	LocationRestriction *SearchTextRequest_LocationRestriction `protobuf:"bytes,14,opt,name=location_restriction,json=locationRestriction,proto3" json:"location_restriction,omitempty"`
    	// Optional. Set the searchable EV options of a place search request.
    	EvOptions *SearchTextRequest_EVOptions `protobuf:"bytes,15,opt,name=ev_options,json=evOptions,proto3" json:"ev_options,omitempty"`
    	// Optional. Additional parameters for routing to results.
    	RoutingParameters *RoutingParameters `protobuf:"bytes,16,opt,name=routing_parameters,json=routingParameters,proto3" json:"routing_parameters,omitempty"`
    	// Optional. Additional parameters proto for searching along a route.
    	SearchAlongRouteParameters *SearchTextRequest_SearchAlongRouteParameters `protobuf:"bytes,17,opt,name=search_along_route_parameters,json=searchAlongRouteParameters,proto3" json:"search_along_route_parameters,omitempty"`
    	// Optional. Include pure service area businesses if the field is set to true.
    	// Pure service area business is a business that visits or delivers to
    	// customers directly but does not serve customers at their business address.
    	// For example, businesses like cleaning services or plumbers. Those
    	// businesses do not have a physical address or location on Google Maps.
    	// Places will not return fields including `location`, `plus_code`, and other
    	// location related fields for these businesses.
    	IncludePureServiceAreaBusinesses [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,20,opt,name=include_pure_service_area_businesses,json=includePureServiceAreaBusinesses,proto3" json:"include_pure_service_area_businesses,omitempty"`
    	// Optional. If true, include businesses that are not yet open but will open
    	// in the future.
    	IncludeFutureOpeningBusinesses [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,21,opt,name=include_future_opening_businesses,json=includeFutureOpeningBusinesses,proto3" json:"include_future_opening_businesses,omitempty"`
    	// contains filtered or unexported fields
    }

Request proto for SearchText.

### func (*SearchTextRequest) Descriptor 
    
    
    func (*SearchTextRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest.ProtoReflect.Descriptor instead.

### func (*SearchTextRequest) GetEvOptions 
    
    
    func (x *SearchTextRequest) GetEvOptions() *SearchTextRequest_EVOptions

### func (*SearchTextRequest) GetIncludeFutureOpeningBusinesses 
    
    
    func (x *SearchTextRequest) GetIncludeFutureOpeningBusinesses() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchTextRequest) GetIncludePureServiceAreaBusinesses 
    
    
    func (x *SearchTextRequest) GetIncludePureServiceAreaBusinesses() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchTextRequest) GetIncludedType 
    
    
    func (x *SearchTextRequest) GetIncludedType() [string](https://pkg.go.dev/builtin#string)

### func (*SearchTextRequest) GetLanguageCode 
    
    
    func (x *SearchTextRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*SearchTextRequest) GetLocationBias 
    
    
    func (x *SearchTextRequest) GetLocationBias() *SearchTextRequest_LocationBias

### func (*SearchTextRequest) GetLocationRestriction 
    
    
    func (x *SearchTextRequest) GetLocationRestriction() *SearchTextRequest_LocationRestriction

### func (*SearchTextRequest) GetMaxResultCount 
    
    
    func (x *SearchTextRequest) GetMaxResultCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchTextRequest) GetMinRating 
    
    
    func (x *SearchTextRequest) GetMinRating() [float64](https://pkg.go.dev/builtin#float64)

### func (*SearchTextRequest) GetOpenNow 
    
    
    func (x *SearchTextRequest) GetOpenNow() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchTextRequest) GetPriceLevels 
    
    
    func (x *SearchTextRequest) GetPriceLevels() []PriceLevel

### func (*SearchTextRequest) GetRankPreference 
    
    
    func (x *SearchTextRequest) GetRankPreference() SearchTextRequest_RankPreference

### func (*SearchTextRequest) GetRegionCode 
    
    
    func (x *SearchTextRequest) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*SearchTextRequest) GetRoutingParameters 
    
    
    func (x *SearchTextRequest) GetRoutingParameters() *RoutingParameters

### func (*SearchTextRequest) GetSearchAlongRouteParameters 
    
    
    func (x *SearchTextRequest) GetSearchAlongRouteParameters() *SearchTextRequest_SearchAlongRouteParameters

### func (*SearchTextRequest) GetStrictTypeFiltering 
    
    
    func (x *SearchTextRequest) GetStrictTypeFiltering() [bool](https://pkg.go.dev/builtin#bool)

### func (*SearchTextRequest) GetTextQuery 
    
    
    func (x *SearchTextRequest) GetTextQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SearchTextRequest) ProtoMessage 
    
    
    func (*SearchTextRequest) ProtoMessage()

### func (*SearchTextRequest) ProtoReflect 
    
    
    func (x *SearchTextRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextRequest) Reset 
    
    
    func (x *SearchTextRequest) Reset()

### func (*SearchTextRequest) String 
    
    
    func (x *SearchTextRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextRequest_EVOptions
    
    
    type SearchTextRequest_EVOptions struct {
    
    	// Optional. Minimum required charging rate in kilowatts. A place with a
    	// charging rate less than the specified rate is filtered out.
    	MinimumChargingRateKw [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=minimum_charging_rate_kw,json=minimumChargingRateKw,proto3" json:"minimum_charging_rate_kw,omitempty"`
    	// Optional. The list of preferred EV connector types. A place that does not
    	// support any of the listed connector types is filtered out.
    	ConnectorTypes []EVConnectorType `protobuf:"varint,2,rep,packed,name=connector_types,json=connectorTypes,proto3,enum=google.maps.places.v1.EVConnectorType" json:"connector_types,omitempty"`
    	// contains filtered or unexported fields
    }

Searchable EV options of a place search request.

### func (*SearchTextRequest_EVOptions) Descriptor 
    
    
    func (*SearchTextRequest_EVOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest_EVOptions.ProtoReflect.Descriptor instead.

### func (*SearchTextRequest_EVOptions) GetConnectorTypes 
    
    
    func (x *SearchTextRequest_EVOptions) GetConnectorTypes() []EVConnectorType

### func (*SearchTextRequest_EVOptions) GetMinimumChargingRateKw 
    
    
    func (x *SearchTextRequest_EVOptions) GetMinimumChargingRateKw() [float64](https://pkg.go.dev/builtin#float64)

### func (*SearchTextRequest_EVOptions) ProtoMessage 
    
    
    func (*SearchTextRequest_EVOptions) ProtoMessage()

### func (*SearchTextRequest_EVOptions) ProtoReflect 
    
    
    func (x *SearchTextRequest_EVOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextRequest_EVOptions) Reset 
    
    
    func (x *SearchTextRequest_EVOptions) Reset()

### func (*SearchTextRequest_EVOptions) String 
    
    
    func (x *SearchTextRequest_EVOptions) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextRequest_LocationBias
    
    
    type SearchTextRequest_LocationBias struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*SearchTextRequest_LocationBias_Rectangle
    	//	*SearchTextRequest_LocationBias_Circle
    	Type isSearchTextRequest_LocationBias_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The region to search. This location serves as a bias which means results around given location might be returned.

### func (*SearchTextRequest_LocationBias) Descriptor 
    
    
    func (*SearchTextRequest_LocationBias) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest_LocationBias.ProtoReflect.Descriptor instead.

### func (*SearchTextRequest_LocationBias) GetCircle 
    
    
    func (x *SearchTextRequest_LocationBias) GetCircle() *Circle

### func (*SearchTextRequest_LocationBias) GetRectangle 
    
    
    func (x *SearchTextRequest_LocationBias) GetRectangle() *[viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport).[Viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport#Viewport)

### func (*SearchTextRequest_LocationBias) GetType 
    
    
    func (x *SearchTextRequest_LocationBias) GetType() isSearchTextRequest_LocationBias_Type

### func (*SearchTextRequest_LocationBias) ProtoMessage 
    
    
    func (*SearchTextRequest_LocationBias) ProtoMessage()

### func (*SearchTextRequest_LocationBias) ProtoReflect 
    
    
    func (x *SearchTextRequest_LocationBias) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextRequest_LocationBias) Reset 
    
    
    func (x *SearchTextRequest_LocationBias) Reset()

### func (*SearchTextRequest_LocationBias) String 
    
    
    func (x *SearchTextRequest_LocationBias) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextRequest_LocationBias_Circle
    
    
    type SearchTextRequest_LocationBias_Circle struct {
    	// A circle defined by center point and radius.
    	Circle *Circle `protobuf:"bytes,2,opt,name=circle,proto3,oneof"`
    }

## SearchTextRequest_LocationBias_Rectangle
    
    
    type SearchTextRequest_LocationBias_Rectangle struct {
    	// A rectangle box defined by northeast and southwest corner.
    	// `rectangle.high()` must be the northeast point of the rectangle
    	// viewport. `rectangle.low()` must be the southwest point of the
    	// rectangle viewport. `rectangle.low().latitude()` cannot be greater than
    	// `rectangle.high().latitude()`. This will result in an empty latitude
    	// range. A rectangle viewport cannot be wider than 180 degrees.
    	Rectangle *viewport.Viewport `protobuf:"bytes,1,opt,name=rectangle,proto3,oneof"`
    }

## SearchTextRequest_LocationRestriction
    
    
    type SearchTextRequest_LocationRestriction struct {
    
    	// Types that are valid to be assigned to Type:
    	//
    	//	*SearchTextRequest_LocationRestriction_Rectangle
    	Type isSearchTextRequest_LocationRestriction_Type `protobuf_oneof:"type"`
    	// contains filtered or unexported fields
    }

The region to search. This location serves as a restriction which means results outside given location will not be returned.

### func (*SearchTextRequest_LocationRestriction) Descriptor 
    
    
    func (*SearchTextRequest_LocationRestriction) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest_LocationRestriction.ProtoReflect.Descriptor instead.

### func (*SearchTextRequest_LocationRestriction) GetRectangle 
    
    
    func (x *SearchTextRequest_LocationRestriction) GetRectangle() *[viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport).[Viewport](https://pkg.go.dev/google.golang.org/genproto/googleapis/geo/type/viewport#Viewport)

### func (*SearchTextRequest_LocationRestriction) GetType 
    
    
    func (x *SearchTextRequest_LocationRestriction) GetType() isSearchTextRequest_LocationRestriction_Type

### func (*SearchTextRequest_LocationRestriction) ProtoMessage 
    
    
    func (*SearchTextRequest_LocationRestriction) ProtoMessage()

### func (*SearchTextRequest_LocationRestriction) ProtoReflect 
    
    
    func (x *SearchTextRequest_LocationRestriction) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextRequest_LocationRestriction) Reset 
    
    
    func (x *SearchTextRequest_LocationRestriction) Reset()

### func (*SearchTextRequest_LocationRestriction) String 
    
    
    func (x *SearchTextRequest_LocationRestriction) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextRequest_LocationRestriction_Rectangle
    
    
    type SearchTextRequest_LocationRestriction_Rectangle struct {
    	// A rectangle box defined by northeast and southwest corner.
    	// `rectangle.high()` must be the northeast point of the rectangle
    	// viewport. `rectangle.low()` must be the southwest point of the
    	// rectangle viewport. `rectangle.low().latitude()` cannot be greater than
    	// `rectangle.high().latitude()`. This will result in an empty latitude
    	// range. A rectangle viewport cannot be wider than 180 degrees.
    	Rectangle *viewport.Viewport `protobuf:"bytes,1,opt,name=rectangle,proto3,oneof"`
    }

## SearchTextRequest_RankPreference
    
    
    type SearchTextRequest_RankPreference [int32](https://pkg.go.dev/builtin#int32)

How results will be ranked in the response.

### SearchTextRequest_RANK_PREFERENCE_UNSPECIFIED, SearchTextRequest_DISTANCE, SearchTextRequest_RELEVANCE
    
    
    const (
    	// For a categorical query such as "Restaurants in New York City", RELEVANCE
    	// is the default. For non-categorical queries such as "Mountain View, CA"
    	// we recommend that you leave rankPreference unset.
    	SearchTextRequest_RANK_PREFERENCE_UNSPECIFIED SearchTextRequest_RankPreference = 0
    	// Ranks results by distance.
    	SearchTextRequest_DISTANCE SearchTextRequest_RankPreference = 1
    	// Ranks results by relevance. Sort order determined by normal ranking
    	// stack.
    	SearchTextRequest_RELEVANCE SearchTextRequest_RankPreference = 2
    )

### func (SearchTextRequest_RankPreference) Descriptor 
    
    
    func (SearchTextRequest_RankPreference) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SearchTextRequest_RankPreference) Enum 
    
    
    func (x SearchTextRequest_RankPreference) Enum() *SearchTextRequest_RankPreference

### func (SearchTextRequest_RankPreference) EnumDescriptor 
    
    
    func (SearchTextRequest_RankPreference) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest_RankPreference.Descriptor instead.

### func (SearchTextRequest_RankPreference) Number 
    
    
    func (x SearchTextRequest_RankPreference) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SearchTextRequest_RankPreference) String 
    
    
    func (x SearchTextRequest_RankPreference) String() [string](https://pkg.go.dev/builtin#string)

### func (SearchTextRequest_RankPreference) Type 
    
    
    func (SearchTextRequest_RankPreference) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SearchTextRequest_SearchAlongRouteParameters
    
    
    type SearchTextRequest_SearchAlongRouteParameters struct {
    
    	// Required. The route polyline.
    	Polyline *Polyline `protobuf:"bytes,1,opt,name=polyline,proto3" json:"polyline,omitempty"`
    	// contains filtered or unexported fields
    }

Specifies a precalculated polyline from the [Routes API](https://developers.google.com/maps/documentation/routes) defining the route to search. Searching along a route is similar to using the `locationBias` or `locationRestriction` request option to bias the search results. However, while the `locationBias` and `locationRestriction` options let you specify a region to bias the search results, this option lets you bias the results along a trip route.

Results are not guaranteed to be along the route provided, but rather are ranked within the search area defined by the polyline and, optionally, by the `locationBias` or `locationRestriction` based on minimal detour times from origin to destination. The results might be along an alternate route, especially if the provided polyline does not define an optimal route from origin to destination.

### func (*SearchTextRequest_SearchAlongRouteParameters) Descriptor 
    
    
    func (*SearchTextRequest_SearchAlongRouteParameters) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextRequest_SearchAlongRouteParameters.ProtoReflect.Descriptor instead.

### func (*SearchTextRequest_SearchAlongRouteParameters) GetPolyline 
    
    
    func (x *SearchTextRequest_SearchAlongRouteParameters) GetPolyline() *Polyline

### func (*SearchTextRequest_SearchAlongRouteParameters) ProtoMessage 
    
    
    func (*SearchTextRequest_SearchAlongRouteParameters) ProtoMessage()

### func (*SearchTextRequest_SearchAlongRouteParameters) ProtoReflect 
    
    
    func (x *SearchTextRequest_SearchAlongRouteParameters) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextRequest_SearchAlongRouteParameters) Reset 
    
    
    func (x *SearchTextRequest_SearchAlongRouteParameters) Reset()

### func (*SearchTextRequest_SearchAlongRouteParameters) String 
    
    
    func (x *SearchTextRequest_SearchAlongRouteParameters) String() [string](https://pkg.go.dev/builtin#string)

## SearchTextResponse
    
    
    type SearchTextResponse struct {
    
    	// A list of places that meet the user's text search criteria.
    	Places []*Place `protobuf:"bytes,1,rep,name=places,proto3" json:"places,omitempty"`
    	// A list of routing summaries where each entry associates to the
    	// corresponding place in the same index in the `places` field. If the routing
    	// summary is not available for one of the places, it will contain an empty
    	// entry. This list will have as many entries as the list of places if
    	// requested.
    	RoutingSummaries []*RoutingSummary `protobuf:"bytes,2,rep,name=routing_summaries,json=routingSummaries,proto3" json:"routing_summaries,omitempty"`
    	// Experimental: See
    	// https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    	// for more details.
    	//
    	// A list of contextual contents where each entry associates to the
    	// corresponding place in the same index in the places field. The contents
    	// that are relevant to the `text_query` in the request are preferred. If the
    	// contextual content is not available for one of the places, it will return
    	// non-contextual content. It will be empty only when the content is
    	// unavailable for this place. This list will have as many entries as the
    	// list of places if requested.
    	ContextualContents []*ContextualContent `protobuf:"bytes,3,rep,name=contextual_contents,json=contextualContents,proto3" json:"contextual_contents,omitempty"`
    	// contains filtered or unexported fields
    }

Response proto for SearchText.

### func (*SearchTextResponse) Descriptor 
    
    
    func (*SearchTextResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchTextResponse.ProtoReflect.Descriptor instead.

### func (*SearchTextResponse) GetContextualContents 
    
    
    func (x *SearchTextResponse) GetContextualContents() []*ContextualContent

### func (*SearchTextResponse) GetPlaces 
    
    
    func (x *SearchTextResponse) GetPlaces() []*Place

### func (*SearchTextResponse) GetRoutingSummaries 
    
    
    func (x *SearchTextResponse) GetRoutingSummaries() []*RoutingSummary

### func (*SearchTextResponse) ProtoMessage 
    
    
    func (*SearchTextResponse) ProtoMessage()

### func (*SearchTextResponse) ProtoReflect 
    
    
    func (x *SearchTextResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchTextResponse) Reset 
    
    
    func (x *SearchTextResponse) Reset()

### func (*SearchTextResponse) String 
    
    
    func (x *SearchTextResponse) String() [string](https://pkg.go.dev/builtin#string)

## TransitAgency
    
    
    type TransitAgency struct {
    
    	// Agency name (e.g. "VTA") in the requested language.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The URL of the agency's homepage.
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=url,proto3" json:"url,omitempty"`
    	// The URL of the agency's fare details page.
    	FareUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=fare_url,json=fareUrl,proto3" json:"fare_url,omitempty"`
    	// Icon identifier for localized branded icon of a transit system (e.g. London
    	// Underground) which should be used instead of TransitLine.vehicle_icon in
    	// the UI.
    	Icon *TransitIcon `protobuf:"bytes,4,opt,name=icon,proto3" json:"icon,omitempty"`
    	// The transit lines that are served by this agency.
    	Lines []*TransitLine `protobuf:"bytes,5,rep,name=lines,proto3" json:"lines,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a transit agency.

### func (*TransitAgency) Descriptor 
    
    
    func (*TransitAgency) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitAgency.ProtoReflect.Descriptor instead.

### func (*TransitAgency) GetDisplayName 
    
    
    func (x *TransitAgency) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitAgency) GetFareUrl 
    
    
    func (x *TransitAgency) GetFareUrl() [string](https://pkg.go.dev/builtin#string)

### func (*TransitAgency) GetIcon 
    
    
    func (x *TransitAgency) GetIcon() *TransitIcon

### func (*TransitAgency) GetLines 
    
    
    func (x *TransitAgency) GetLines() []*TransitLine

### func (*TransitAgency) GetUrl 
    
    
    func (x *TransitAgency) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*TransitAgency) ProtoMessage 
    
    
    func (*TransitAgency) ProtoMessage()

### func (*TransitAgency) ProtoReflect 
    
    
    func (x *TransitAgency) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitAgency) Reset 
    
    
    func (x *TransitAgency) Reset()

### func (*TransitAgency) String 
    
    
    func (x *TransitAgency) String() [string](https://pkg.go.dev/builtin#string)

## TransitIcon
    
    
    type TransitIcon struct {
    
    	// The URL of the icon.
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=url,proto3" json:"url,omitempty"`
    	// Whether the name is contained in the icon and there is no need to display
    	// it next to the icon.
    	NameIncluded [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=name_included,json=nameIncluded,proto3" json:"name_included,omitempty"`
    	// contains filtered or unexported fields
    }

Icon for a transit line, vehicle, or agency.

### func (*TransitIcon) Descriptor 
    
    
    func (*TransitIcon) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitIcon.ProtoReflect.Descriptor instead.

### func (*TransitIcon) GetNameIncluded 
    
    
    func (x *TransitIcon) GetNameIncluded() [bool](https://pkg.go.dev/builtin#bool)

### func (*TransitIcon) GetUrl 
    
    
    func (x *TransitIcon) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*TransitIcon) ProtoMessage 
    
    
    func (*TransitIcon) ProtoMessage()

### func (*TransitIcon) ProtoReflect 
    
    
    func (x *TransitIcon) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitIcon) Reset 
    
    
    func (x *TransitIcon) Reset()

### func (*TransitIcon) String 
    
    
    func (x *TransitIcon) String() [string](https://pkg.go.dev/builtin#string)

## TransitLine
    
    
    type TransitLine struct {
    
    	// The id of the transit line that can be used to uniquely identify the line
    	// among other transit lines in the same transit station. This identifier is
    	// not guaranteed to be stable across different responses.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// The type of vehicle using this line.
    	VehicleType TransitLine_VehicleType `protobuf:"varint,2,opt,name=vehicle_type,json=vehicleType,proto3,enum=google.maps.places.v1.TransitLine_VehicleType" json:"vehicle_type,omitempty"`
    	// The long name for this transit line (e.g. "Sunnydale local").
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The short name for this transit line (e.g. "S2").
    	ShortDisplayName *localized_text.LocalizedText `protobuf:"bytes,4,opt,name=short_display_name,json=shortDisplayName,proto3" json:"short_display_name,omitempty"`
    	// The text color of labels for this transit line in #RRGGBB hex format,
    	// e.g. #909CE1.
    	TextColor [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=text_color,json=textColor,proto3" json:"text_color,omitempty"`
    	// The background color of the labels for this transit line in #RRGGBB hex
    	// format, e.g. #909CE1. This color can also be used for drawing shapes for
    	// this transit line.
    	BackgroundColor [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=background_color,json=backgroundColor,proto3" json:"background_color,omitempty"`
    	// The URL of a webpage with details about this line.
    	Url [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=url,proto3" json:"url,omitempty"`
    	// Icon identifier for this particular line (e.g. subway lines in New York).
    	Icon *TransitIcon `protobuf:"bytes,8,opt,name=icon,proto3" json:"icon,omitempty"`
    	// Icon identifier for this particular vehicle type.
    	VehicleIcon *TransitIcon `protobuf:"bytes,9,opt,name=vehicle_icon,json=vehicleIcon,proto3" json:"vehicle_icon,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a single transit line.

### func (*TransitLine) Descriptor 
    
    
    func (*TransitLine) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitLine.ProtoReflect.Descriptor instead.

### func (*TransitLine) GetBackgroundColor 
    
    
    func (x *TransitLine) GetBackgroundColor() [string](https://pkg.go.dev/builtin#string)

### func (*TransitLine) GetDisplayName 
    
    
    func (x *TransitLine) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitLine) GetIcon 
    
    
    func (x *TransitLine) GetIcon() *TransitIcon

### func (*TransitLine) GetId 
    
    
    func (x *TransitLine) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*TransitLine) GetShortDisplayName 
    
    
    func (x *TransitLine) GetShortDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitLine) GetTextColor 
    
    
    func (x *TransitLine) GetTextColor() [string](https://pkg.go.dev/builtin#string)

### func (*TransitLine) GetUrl 
    
    
    func (x *TransitLine) GetUrl() [string](https://pkg.go.dev/builtin#string)

### func (*TransitLine) GetVehicleIcon 
    
    
    func (x *TransitLine) GetVehicleIcon() *TransitIcon

### func (*TransitLine) GetVehicleType 
    
    
    func (x *TransitLine) GetVehicleType() TransitLine_VehicleType

### func (*TransitLine) ProtoMessage 
    
    
    func (*TransitLine) ProtoMessage()

### func (*TransitLine) ProtoReflect 
    
    
    func (x *TransitLine) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitLine) Reset 
    
    
    func (x *TransitLine) Reset()

### func (*TransitLine) String 
    
    
    func (x *TransitLine) String() [string](https://pkg.go.dev/builtin#string)

## TransitLine_VehicleType
    
    
    type TransitLine_VehicleType [int32](https://pkg.go.dev/builtin#int32)

The type of vehicle for a transit line.

### TransitLine_VEHICLE_TYPE_UNSPECIFIED, TransitLine_RAIL, TransitLine_METRO_RAIL, TransitLine_SUBWAY, TransitLine_TRAM, TransitLine_MONORAIL, TransitLine_HEAVY_RAIL, TransitLine_COMMUTER_TRAIN, TransitLine_HIGH_SPEED_TRAIN, TransitLine_LONG_DISTANCE_TRAIN, TransitLine_BUS, TransitLine_INTERCITY_BUS, TransitLine_TROLLEYBUS, TransitLine_SHARE_TAXI, TransitLine_COACH, TransitLine_FERRY, TransitLine_CABLE_CAR, TransitLine_GONDOLA_LIFT, TransitLine_FUNICULAR, TransitLine_SPECIAL, TransitLine_HORSE_CARRIAGE, TransitLine_AIRPLANE
    
    
    const (
    	// Default value when vehicle type is not specified.
    	TransitLine_VEHICLE_TYPE_UNSPECIFIED TransitLine_VehicleType = 0
    	// Rail.
    	TransitLine_RAIL TransitLine_VehicleType = 1
    	// Metro rail.
    	TransitLine_METRO_RAIL TransitLine_VehicleType = 2
    	// Subway.
    	TransitLine_SUBWAY TransitLine_VehicleType = 3
    	// Tram.
    	TransitLine_TRAM TransitLine_VehicleType = 4
    	// Monorail.
    	TransitLine_MONORAIL TransitLine_VehicleType = 5
    	// Heavy rail.
    	TransitLine_HEAVY_RAIL TransitLine_VehicleType = 6
    	// Commuter train.
    	TransitLine_COMMUTER_TRAIN TransitLine_VehicleType = 7
    	// High speed train.
    	TransitLine_HIGH_SPEED_TRAIN TransitLine_VehicleType = 8
    	// Long distance train.
    	TransitLine_LONG_DISTANCE_TRAIN TransitLine_VehicleType = 9
    	// Bus.
    	TransitLine_BUS TransitLine_VehicleType = 10
    	// Intercity bus.
    	TransitLine_INTERCITY_BUS TransitLine_VehicleType = 11
    	// Trolleybus.
    	TransitLine_TROLLEYBUS TransitLine_VehicleType = 12
    	// Share taxi.
    	TransitLine_SHARE_TAXI TransitLine_VehicleType = 13
    	// Coach.
    	TransitLine_COACH TransitLine_VehicleType = 14
    	// Ferry.
    	TransitLine_FERRY TransitLine_VehicleType = 15
    	// Cable car.
    	TransitLine_CABLE_CAR TransitLine_VehicleType = 16
    	// Gondola lift.
    	TransitLine_GONDOLA_LIFT TransitLine_VehicleType = 17
    	// Funicular.
    	TransitLine_FUNICULAR TransitLine_VehicleType = 18
    	// Special.
    	TransitLine_SPECIAL TransitLine_VehicleType = 19
    	// Horse carriage.
    	TransitLine_HORSE_CARRIAGE TransitLine_VehicleType = 20
    	// Airplane.
    	TransitLine_AIRPLANE TransitLine_VehicleType = 21
    )

### func (TransitLine_VehicleType) Descriptor 
    
    
    func (TransitLine_VehicleType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TransitLine_VehicleType) Enum 
    
    
    func (x TransitLine_VehicleType) Enum() *TransitLine_VehicleType

### func (TransitLine_VehicleType) EnumDescriptor 
    
    
    func (TransitLine_VehicleType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitLine_VehicleType.Descriptor instead.

### func (TransitLine_VehicleType) Number 
    
    
    func (x TransitLine_VehicleType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TransitLine_VehicleType) String 
    
    
    func (x TransitLine_VehicleType) String() [string](https://pkg.go.dev/builtin#string)

### func (TransitLine_VehicleType) Type 
    
    
    func (TransitLine_VehicleType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## TransitStation
    
    
    type TransitStation struct {
    
    	// The name of the station in the local language.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The transit agencies that serve this station.
    	Agencies []*TransitAgency `protobuf:"bytes,2,rep,name=agencies,proto3" json:"agencies,omitempty"`
    	// Transit stops at this station.
    	Stops []*TransitStop `protobuf:"bytes,3,rep,name=stops,proto3" json:"stops,omitempty"`
    	// contains filtered or unexported fields
    }

Represents transit-specific information for a place.

### func (*TransitStation) Descriptor 
    
    
    func (*TransitStation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitStation.ProtoReflect.Descriptor instead.

### func (*TransitStation) GetAgencies 
    
    
    func (x *TransitStation) GetAgencies() []*TransitAgency

### func (*TransitStation) GetDisplayName 
    
    
    func (x *TransitStation) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitStation) GetStops 
    
    
    func (x *TransitStation) GetStops() []*TransitStop

### func (*TransitStation) ProtoMessage 
    
    
    func (*TransitStation) ProtoMessage()

### func (*TransitStation) ProtoReflect 
    
    
    func (x *TransitStation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitStation) Reset 
    
    
    func (x *TransitStation) Reset()

### func (*TransitStation) String 
    
    
    func (x *TransitStation) String() [string](https://pkg.go.dev/builtin#string)

## TransitStop
    
    
    type TransitStop struct {
    
    	// The id of the transit stop that can be used to uniquely identify the stop
    	// among other transit stops in the same transit station. This identifier is
    	// not guaranteed to be stable across different responses.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// The name of the stop.
    	DisplayName *localized_text.LocalizedText `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The platform code represented by this stop. It can be formatted in any way.
    	// (eg: "2", "Platform 2", "2-4", or "1x").
    	PlatformCode *localized_text.LocalizedText `protobuf:"bytes,3,opt,name=platform_code,json=platformCode,proto3" json:"platform_code,omitempty"`
    	// The verbatim text written on the signboard for this platform, e.g. "Towards
    	// Central" or "East side & Brooklyn". When `platform_code` is absent, this
    	// field is potentially the only identifier for the platform; however, both
    	// `platform_code` and `signage_text` may be set simultaneously.
    	SignageText *localized_text.LocalizedText `protobuf:"bytes,4,opt,name=signage_text,json=signageText,proto3" json:"signage_text,omitempty"`
    	// Human readable identifier of the stop, used by transit agencies to
    	// distinguish stops with the same name.
    	StopCode *localized_text.LocalizedText `protobuf:"bytes,5,opt,name=stop_code,json=stopCode,proto3" json:"stop_code,omitempty"`
    	// The stop's location.
    	Location *latlng.LatLng `protobuf:"bytes,6,opt,name=location,proto3" json:"location,omitempty"`
    	// Wheelchair accessibility of this stop. This field indicates whether there
    	// is an accessible path from outside the station to the stop. It does not
    	// indicate whether it is possible to board a vehicle from the stop.
    	WheelchairAccessibleEntrance *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=wheelchair_accessible_entrance,json=wheelchairAccessibleEntrance,proto3,oneof" json:"wheelchair_accessible_entrance,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a transit stop within a station. This is a specific location where passengers board and alight transit vehicles, such as a platform or bus bay. This is distinct from a `Departure`, which is an event of a vehicle leaving a stop at a specific time.

### func (*TransitStop) Descriptor 
    
    
    func (*TransitStop) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransitStop.ProtoReflect.Descriptor instead.

### func (*TransitStop) GetDisplayName 
    
    
    func (x *TransitStop) GetDisplayName() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitStop) GetId 
    
    
    func (x *TransitStop) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*TransitStop) GetLocation 
    
    
    func (x *TransitStop) GetLocation() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*TransitStop) GetPlatformCode 
    
    
    func (x *TransitStop) GetPlatformCode() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitStop) GetSignageText 
    
    
    func (x *TransitStop) GetSignageText() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitStop) GetStopCode 
    
    
    func (x *TransitStop) GetStopCode() *[localized_text](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text).[LocalizedText](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/localized_text#LocalizedText)

### func (*TransitStop) GetWheelchairAccessibleEntrance 
    
    
    func (x *TransitStop) GetWheelchairAccessibleEntrance() [bool](https://pkg.go.dev/builtin#bool)

### func (*TransitStop) ProtoMessage 
    
    
    func (*TransitStop) ProtoMessage()

### func (*TransitStop) ProtoReflect 
    
    
    func (x *TransitStop) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransitStop) Reset 
    
    
    func (x *TransitStop) Reset()

### func (*TransitStop) String 
    
    
    func (x *TransitStop) String() [string](https://pkg.go.dev/builtin#string)

## TravelMode
    
    
    type TravelMode [int32](https://pkg.go.dev/builtin#int32)

Travel mode options. These options map to what [Routes API offers](https://developers.google.com/maps/documentation/routes/reference/rest/v2/RouteTravelMode).

### TravelMode_TRAVEL_MODE_UNSPECIFIED, TravelMode_DRIVE, TravelMode_BICYCLE, TravelMode_WALK, TravelMode_TWO_WHEELER
    
    
    const (
    	// No travel mode specified. Defaults to `DRIVE`.
    	TravelMode_TRAVEL_MODE_UNSPECIFIED TravelMode = 0
    	// Travel by passenger car.
    	TravelMode_DRIVE TravelMode = 1
    	// Travel by bicycle.  Not supported with `search_along_route_parameters`.
    	TravelMode_BICYCLE TravelMode = 2
    	// Travel by walking.  Not supported with `search_along_route_parameters`.
    	TravelMode_WALK TravelMode = 3
    	// Motorized two wheeled vehicles of all kinds such as scooters and
    	// motorcycles. Note that this is distinct from the `BICYCLE` travel mode
    	// which covers human-powered transport.  Not supported with
    	// `search_along_route_parameters`. Only supported in those countries listed
    	// at [Countries and regions supported for two-wheeled
    	// vehicles](https://developers.google.com/maps/documentation/routes/coverage-two-wheeled).
    	TravelMode_TWO_WHEELER TravelMode = 4
    )

### func (TravelMode) Descriptor 
    
    
    func (TravelMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TravelMode) Enum 
    
    
    func (x TravelMode) Enum() *TravelMode

### func (TravelMode) EnumDescriptor 
    
    
    func (TravelMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TravelMode.Descriptor instead.

### func (TravelMode) Number 
    
    
    func (x TravelMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TravelMode) String 
    
    
    func (x TravelMode) String() [string](https://pkg.go.dev/builtin#string)

### func (TravelMode) Type 
    
    
    func (TravelMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedPlacesServer
    
    
    type UnimplementedPlacesServer struct {
    }

UnimplementedPlacesServer should be embedded to have forward compatible implementations.

### func (UnimplementedPlacesServer) AutocompletePlaces 
    
    
    func (UnimplementedPlacesServer) AutocompletePlaces([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AutocompletePlacesRequest) (*AutocompletePlacesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedPlacesServer) GetPhotoMedia 
    
    
    func (UnimplementedPlacesServer) GetPhotoMedia([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPhotoMediaRequest) (*PhotoMedia, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedPlacesServer) GetPlace 
    
    
    func (UnimplementedPlacesServer) GetPlace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPlaceRequest) (*Place, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedPlacesServer) SearchNearby 
    
    
    func (UnimplementedPlacesServer) SearchNearby([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchNearbyRequest) (*SearchNearbyResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedPlacesServer) SearchText 
    
    
    func (UnimplementedPlacesServer) SearchText([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchTextRequest) (*SearchTextResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafePlacesServer
    
    
    type UnsafePlacesServer interface {
    	// contains filtered or unexported methods
    }

UnsafePlacesServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to PlacesServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
