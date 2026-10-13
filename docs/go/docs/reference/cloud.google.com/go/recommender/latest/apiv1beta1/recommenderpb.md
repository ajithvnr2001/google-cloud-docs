---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/recommender/latest/apiv1beta1/recommenderpb/
title: Recommender API v1beta1 - Package cloud.google.com/go/recommender/apiv1beta1/recommenderpb (v1.20.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:37.630997+00:00
---

# Recommender API v1beta1 - Package cloud.google.com/go/recommender/apiv1beta1/recommenderpb (v1.20.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/recommender/latest/apiv1beta1/recommenderpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Recommender API v1beta1 - Package cloud.google.com/go/recommender/apiv1beta1/recommenderpb (v1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.6  1.12.8  1.11.3  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/recommender/apiv1beta1/recommenderpb). 

##  Constants 

### Recommender_ListInsights_FullMethodName, Recommender_GetInsight_FullMethodName, Recommender_MarkInsightAccepted_FullMethodName, Recommender_ListRecommendations_FullMethodName, Recommender_GetRecommendation_FullMethodName, Recommender_MarkRecommendationClaimed_FullMethodName, Recommender_MarkRecommendationSucceeded_FullMethodName, Recommender_MarkRecommendationFailed_FullMethodName, Recommender_GetRecommenderConfig_FullMethodName, Recommender_UpdateRecommenderConfig_FullMethodName, Recommender_GetInsightTypeConfig_FullMethodName, Recommender_UpdateInsightTypeConfig_FullMethodName, Recommender_ListRecommenders_FullMethodName, Recommender_ListInsightTypes_FullMethodName
    
    
    const (
    	Recommender_ListInsights_FullMethodName                = "/google.cloud.recommender.v1beta1.Recommender/ListInsights"
    	Recommender_GetInsight_FullMethodName                  = "/google.cloud.recommender.v1beta1.Recommender/GetInsight"
    	Recommender_MarkInsightAccepted_FullMethodName         = "/google.cloud.recommender.v1beta1.Recommender/MarkInsightAccepted"
    	Recommender_ListRecommendations_FullMethodName         = "/google.cloud.recommender.v1beta1.Recommender/ListRecommendations"
    	Recommender_GetRecommendation_FullMethodName           = "/google.cloud.recommender.v1beta1.Recommender/GetRecommendation"
    	Recommender_MarkRecommendationClaimed_FullMethodName   = "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationClaimed"
    	Recommender_MarkRecommendationSucceeded_FullMethodName = "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationSucceeded"
    	Recommender_MarkRecommendationFailed_FullMethodName    = "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationFailed"
    	Recommender_GetRecommenderConfig_FullMethodName        = "/google.cloud.recommender.v1beta1.Recommender/GetRecommenderConfig"
    	Recommender_UpdateRecommenderConfig_FullMethodName     = "/google.cloud.recommender.v1beta1.Recommender/UpdateRecommenderConfig"
    	Recommender_GetInsightTypeConfig_FullMethodName        = "/google.cloud.recommender.v1beta1.Recommender/GetInsightTypeConfig"
    	Recommender_UpdateInsightTypeConfig_FullMethodName     = "/google.cloud.recommender.v1beta1.Recommender/UpdateInsightTypeConfig"
    	Recommender_ListRecommenders_FullMethodName            = "/google.cloud.recommender.v1beta1.Recommender/ListRecommenders"
    	Recommender_ListInsightTypes_FullMethodName            = "/google.cloud.recommender.v1beta1.Recommender/ListInsightTypes"
    )

## Variables 

### Insight_Category_name, Insight_Category_value
    
    
    var (
    	Insight_Category_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CATEGORY_UNSPECIFIED",
    		1: "COST",
    		2: "SECURITY",
    		3: "PERFORMANCE",
    		4: "MANAGEABILITY",
    	}
    	Insight_Category_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CATEGORY_UNSPECIFIED": 0,
    		"COST":                 1,
    		"SECURITY":             2,
    		"PERFORMANCE":          3,
    		"MANAGEABILITY":        4,
    	}
    )

Enum value maps for Insight_Category.

### Insight_Severity_name, Insight_Severity_value
    
    
    var (
    	Insight_Severity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SEVERITY_UNSPECIFIED",
    		1: "LOW",
    		2: "MEDIUM",
    		3: "HIGH",
    		4: "CRITICAL",
    	}
    	Insight_Severity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SEVERITY_UNSPECIFIED": 0,
    		"LOW":                  1,
    		"MEDIUM":               2,
    		"HIGH":                 3,
    		"CRITICAL":             4,
    	}
    )

Enum value maps for Insight_Severity.

### InsightStateInfo_State_name, InsightStateInfo_State_value
    
    
    var (
    	InsightStateInfo_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "ACCEPTED",
    		3: "DISMISSED",
    	}
    	InsightStateInfo_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"ACCEPTED":          2,
    		"DISMISSED":         3,
    	}
    )

Enum value maps for InsightStateInfo_State.

### Recommendation_Priority_name, Recommendation_Priority_value
    
    
    var (
    	Recommendation_Priority_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PRIORITY_UNSPECIFIED",
    		1: "P4",
    		2: "P3",
    		3: "P2",
    		4: "P1",
    	}
    	Recommendation_Priority_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PRIORITY_UNSPECIFIED": 0,
    		"P4":                   1,
    		"P3":                   2,
    		"P2":                   3,
    		"P1":                   4,
    	}
    )

Enum value maps for Recommendation_Priority.

### Impact_Category_name, Impact_Category_value
    
    
    var (
    	Impact_Category_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CATEGORY_UNSPECIFIED",
    		1: "COST",
    		2: "SECURITY",
    		3: "PERFORMANCE",
    		4: "MANAGEABILITY",
    		5: "SUSTAINABILITY",
    	}
    	Impact_Category_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CATEGORY_UNSPECIFIED": 0,
    		"COST":                 1,
    		"SECURITY":             2,
    		"PERFORMANCE":          3,
    		"MANAGEABILITY":        4,
    		"SUSTAINABILITY":       5,
    	}
    )

Enum value maps for Impact_Category.

### RecommendationStateInfo_State_name, RecommendationStateInfo_State_value
    
    
    var (
    	RecommendationStateInfo_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		6: "CLAIMED",
    		3: "SUCCEEDED",
    		4: "FAILED",
    		5: "DISMISSED",
    	}
    	RecommendationStateInfo_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"CLAIMED":           6,
    		"SUCCEEDED":         3,
    		"FAILED":            4,
    		"DISMISSED":         5,
    	}
    )

Enum value maps for RecommendationStateInfo_State.

### File_google_cloud_recommender_v1beta1_insight_proto
    
    
    var File_google_cloud_recommender_v1beta1_insight_proto protoreflect.FileDescriptor

### File_google_cloud_recommender_v1beta1_insight_type_config_proto
    
    
    var File_google_cloud_recommender_v1beta1_insight_type_config_proto protoreflect.FileDescriptor

### File_google_cloud_recommender_v1beta1_recommendation_proto
    
    
    var File_google_cloud_recommender_v1beta1_recommendation_proto protoreflect.FileDescriptor

### File_google_cloud_recommender_v1beta1_recommender_config_proto
    
    
    var File_google_cloud_recommender_v1beta1_recommender_config_proto protoreflect.FileDescriptor

### File_google_cloud_recommender_v1beta1_recommender_service_proto
    
    
    var File_google_cloud_recommender_v1beta1_recommender_service_proto protoreflect.FileDescriptor

### Recommender_ServiceDesc
    
    
    var Recommender_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.recommender.v1beta1.Recommender",
    	HandlerType: (*RecommenderServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListInsights",
    			Handler:    _Recommender_ListInsights_Handler,
    		},
    		{
    			MethodName: "GetInsight",
    			Handler:    _Recommender_GetInsight_Handler,
    		},
    		{
    			MethodName: "MarkInsightAccepted",
    			Handler:    _Recommender_MarkInsightAccepted_Handler,
    		},
    		{
    			MethodName: "ListRecommendations",
    			Handler:    _Recommender_ListRecommendations_Handler,
    		},
    		{
    			MethodName: "GetRecommendation",
    			Handler:    _Recommender_GetRecommendation_Handler,
    		},
    		{
    			MethodName: "MarkRecommendationClaimed",
    			Handler:    _Recommender_MarkRecommendationClaimed_Handler,
    		},
    		{
    			MethodName: "MarkRecommendationSucceeded",
    			Handler:    _Recommender_MarkRecommendationSucceeded_Handler,
    		},
    		{
    			MethodName: "MarkRecommendationFailed",
    			Handler:    _Recommender_MarkRecommendationFailed_Handler,
    		},
    		{
    			MethodName: "GetRecommenderConfig",
    			Handler:    _Recommender_GetRecommenderConfig_Handler,
    		},
    		{
    			MethodName: "UpdateRecommenderConfig",
    			Handler:    _Recommender_UpdateRecommenderConfig_Handler,
    		},
    		{
    			MethodName: "GetInsightTypeConfig",
    			Handler:    _Recommender_GetInsightTypeConfig_Handler,
    		},
    		{
    			MethodName: "UpdateInsightTypeConfig",
    			Handler:    _Recommender_UpdateInsightTypeConfig_Handler,
    		},
    		{
    			MethodName: "ListRecommenders",
    			Handler:    _Recommender_ListRecommenders_Handler,
    		},
    		{
    			MethodName: "ListInsightTypes",
    			Handler:    _Recommender_ListInsightTypes_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/recommender/v1beta1/recommender_service.proto",
    }

Recommender_ServiceDesc is the grpc.ServiceDesc for Recommender service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterRecommenderServer 
    
    
    func RegisterRecommenderServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv RecommenderServer)

## CostProjection
    
    
    type CostProjection struct {
    
    	// An approximate projection on amount saved or amount incurred. Negative cost
    	// units indicate cost savings and positive cost units indicate increase.
    	// See google.type.Money documentation for positive/negative units.
    	//
    	// A user's permissions may affect whether the cost is computed using list
    	// prices or custom contract prices.
    	Cost *money.Money `protobuf:"bytes,1,opt,name=cost,proto3" json:"cost,omitempty"`
    	// Duration for which this cost applies.
    	Duration *durationpb.Duration `protobuf:"bytes,2,opt,name=duration,proto3" json:"duration,omitempty"`
    	// contains filtered or unexported fields
    }

Contains metadata about how much money a recommendation can save or incur.

### func (*CostProjection) Descriptor 
    
    
    func (*CostProjection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CostProjection.ProtoReflect.Descriptor instead.

### func (*CostProjection) GetCost 
    
    
    func (x *CostProjection) GetCost() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*CostProjection) GetDuration 
    
    
    func (x *CostProjection) GetDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*CostProjection) ProtoMessage 
    
    
    func (*CostProjection) ProtoMessage()

### func (*CostProjection) ProtoReflect 
    
    
    func (x *CostProjection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CostProjection) Reset 
    
    
    func (x *CostProjection) Reset()

### func (*CostProjection) String 
    
    
    func (x *CostProjection) String() [string](https://pkg.go.dev/builtin#string)

## GetInsightRequest
    
    
    type GetInsightRequest struct {
    
    	// Required. Name of the insight.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request to the `GetInsight` method.

### func (*GetInsightRequest) Descriptor 
    
    
    func (*GetInsightRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetInsightRequest.ProtoReflect.Descriptor instead.

### func (*GetInsightRequest) GetName 
    
    
    func (x *GetInsightRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetInsightRequest) ProtoMessage 
    
    
    func (*GetInsightRequest) ProtoMessage()

### func (*GetInsightRequest) ProtoReflect 
    
    
    func (x *GetInsightRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetInsightRequest) Reset 
    
    
    func (x *GetInsightRequest) Reset()

### func (*GetInsightRequest) String 
    
    
    func (x *GetInsightRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetInsightTypeConfigRequest
    
    
    type GetInsightTypeConfigRequest struct {
    
    	// Required. Name of the InsightTypeConfig to get.
    	//
    	// Acceptable formats:
    	//
    	// * `projects/[PROJECT_NUMBER]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config`
    	//
    	// * `projects/[PROJECT_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config`
    	//
    	// * `organizations/[ORGANIZATION_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the GetInsightTypeConfig` method.

### func (*GetInsightTypeConfigRequest) Descriptor 
    
    
    func (*GetInsightTypeConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetInsightTypeConfigRequest.ProtoReflect.Descriptor instead.

### func (*GetInsightTypeConfigRequest) GetName 
    
    
    func (x *GetInsightTypeConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetInsightTypeConfigRequest) ProtoMessage 
    
    
    func (*GetInsightTypeConfigRequest) ProtoMessage()

### func (*GetInsightTypeConfigRequest) ProtoReflect 
    
    
    func (x *GetInsightTypeConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetInsightTypeConfigRequest) Reset 
    
    
    func (x *GetInsightTypeConfigRequest) Reset()

### func (*GetInsightTypeConfigRequest) String 
    
    
    func (x *GetInsightTypeConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetRecommendationRequest
    
    
    type GetRecommendationRequest struct {
    
    	// Required. Name of the recommendation.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request to the `GetRecommendation` method.

### func (*GetRecommendationRequest) Descriptor 
    
    
    func (*GetRecommendationRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetRecommendationRequest.ProtoReflect.Descriptor instead.

### func (*GetRecommendationRequest) GetName 
    
    
    func (x *GetRecommendationRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetRecommendationRequest) ProtoMessage 
    
    
    func (*GetRecommendationRequest) ProtoMessage()

### func (*GetRecommendationRequest) ProtoReflect 
    
    
    func (x *GetRecommendationRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetRecommendationRequest) Reset 
    
    
    func (x *GetRecommendationRequest) Reset()

### func (*GetRecommendationRequest) String 
    
    
    func (x *GetRecommendationRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetRecommenderConfigRequest
    
    
    type GetRecommenderConfigRequest struct {
    
    	// Required. Name of the Recommendation Config to get.
    	//
    	// Acceptable formats:
    	//
    	// * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
    	//
    	// * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
    	//
    	// * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the GetRecommenderConfig` method.

### func (*GetRecommenderConfigRequest) Descriptor 
    
    
    func (*GetRecommenderConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetRecommenderConfigRequest.ProtoReflect.Descriptor instead.

### func (*GetRecommenderConfigRequest) GetName 
    
    
    func (x *GetRecommenderConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetRecommenderConfigRequest) ProtoMessage 
    
    
    func (*GetRecommenderConfigRequest) ProtoMessage()

### func (*GetRecommenderConfigRequest) ProtoReflect 
    
    
    func (x *GetRecommenderConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetRecommenderConfigRequest) Reset 
    
    
    func (x *GetRecommenderConfigRequest) Reset()

### func (*GetRecommenderConfigRequest) String 
    
    
    func (x *GetRecommenderConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## Impact
    
    
    type Impact struct {
    
    	// Category that is being targeted.
    	Category Impact_Category `protobuf:"varint,1,opt,name=category,proto3,enum=google.cloud.recommender.v1beta1.Impact_Category" json:"category,omitempty"`
    	// Contains projections (if any) for this category.
    	//
    	// Types that are valid to be assigned to Projection:
    	//
    	//	*Impact_CostProjection
    	//	*Impact_SecurityProjection
    	//	*Impact_SustainabilityProjection
    	Projection isImpact_Projection `protobuf_oneof:"projection"`
    	// contains filtered or unexported fields
    }

Contains the impact a recommendation can have for a given category.

### func (*Impact) Descriptor 
    
    
    func (*Impact) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Impact.ProtoReflect.Descriptor instead.

### func (*Impact) GetCategory 
    
    
    func (x *Impact) GetCategory() Impact_Category

### func (*Impact) GetCostProjection 
    
    
    func (x *Impact) GetCostProjection() *CostProjection

### func (*Impact) GetProjection 
    
    
    func (x *Impact) GetProjection() isImpact_Projection

### func (*Impact) GetSecurityProjection 
    
    
    func (x *Impact) GetSecurityProjection() *SecurityProjection

### func (*Impact) GetSustainabilityProjection 
    
    
    func (x *Impact) GetSustainabilityProjection() *SustainabilityProjection

### func (*Impact) ProtoMessage 
    
    
    func (*Impact) ProtoMessage()

### func (*Impact) ProtoReflect 
    
    
    func (x *Impact) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Impact) Reset 
    
    
    func (x *Impact) Reset()

### func (*Impact) String 
    
    
    func (x *Impact) String() [string](https://pkg.go.dev/builtin#string)

## Impact_Category
    
    
    type Impact_Category [int32](https://pkg.go.dev/builtin#int32)

The category of the impact.

### Impact_CATEGORY_UNSPECIFIED, Impact_COST, Impact_SECURITY, Impact_PERFORMANCE, Impact_MANAGEABILITY, Impact_SUSTAINABILITY
    
    
    const (
    	// Default unspecified category. Don't use directly.
    	Impact_CATEGORY_UNSPECIFIED Impact_Category = 0
    	// Indicates a potential increase or decrease in cost.
    	Impact_COST Impact_Category = 1
    	// Indicates a potential increase or decrease in security.
    	Impact_SECURITY Impact_Category = 2
    	// Indicates a potential increase or decrease in performance.
    	Impact_PERFORMANCE Impact_Category = 3
    	// Indicates a potential increase or decrease in manageability.
    	Impact_MANAGEABILITY Impact_Category = 4
    	// Indicates a potential increase or decrease in sustainability.
    	Impact_SUSTAINABILITY Impact_Category = 5
    )

### func (Impact_Category) Descriptor 
    
    
    func (Impact_Category) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Impact_Category) Enum 
    
    
    func (x Impact_Category) Enum() *Impact_Category

### func (Impact_Category) EnumDescriptor 
    
    
    func (Impact_Category) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Impact_Category.Descriptor instead.

### func (Impact_Category) Number 
    
    
    func (x Impact_Category) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Impact_Category) String 
    
    
    func (x Impact_Category) String() [string](https://pkg.go.dev/builtin#string)

### func (Impact_Category) Type 
    
    
    func (Impact_Category) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Impact_CostProjection
    
    
    type Impact_CostProjection struct {
    	// Use with CategoryType.COST
    	CostProjection *CostProjection `protobuf:"bytes,100,opt,name=cost_projection,json=costProjection,proto3,oneof"`
    }

## Impact_SecurityProjection
    
    
    type Impact_SecurityProjection struct {
    	// Use with CategoryType.SECURITY
    	SecurityProjection *SecurityProjection `protobuf:"bytes,101,opt,name=security_projection,json=securityProjection,proto3,oneof"`
    }

## Impact_SustainabilityProjection
    
    
    type Impact_SustainabilityProjection struct {
    	// Use with CategoryType.SUSTAINABILITY
    	SustainabilityProjection *SustainabilityProjection `protobuf:"bytes,102,opt,name=sustainability_projection,json=sustainabilityProjection,proto3,oneof"`
    }

## Insight
    
    
    type Insight struct {
    
    	// Name of the insight.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Free-form human readable summary in English. The maximum length is 500
    	// characters.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// Fully qualified resource names that this insight is targeting.
    	TargetResources [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,rep,name=target_resources,json=targetResources,proto3" json:"target_resources,omitempty"`
    	// Insight subtype. Insight content schema will be stable for a given subtype.
    	InsightSubtype [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,opt,name=insight_subtype,json=insightSubtype,proto3" json:"insight_subtype,omitempty"`
    	// A struct of custom fields to explain the insight.
    	// Example: "grantedPermissionsCount": "1000"
    	Content *structpb.Struct `protobuf:"bytes,3,opt,name=content,proto3" json:"content,omitempty"`
    	// Timestamp of the latest data used to generate the insight.
    	LastRefreshTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=last_refresh_time,json=lastRefreshTime,proto3" json:"last_refresh_time,omitempty"`
    	// Observation period that led to the insight. The source data used to
    	// generate the insight ends at last_refresh_time and begins at
    	// (last_refresh_time - observation_period).
    	ObservationPeriod *durationpb.Duration `protobuf:"bytes,5,opt,name=observation_period,json=observationPeriod,proto3" json:"observation_period,omitempty"`
    	// Information state and metadata.
    	StateInfo *InsightStateInfo `protobuf:"bytes,6,opt,name=state_info,json=stateInfo,proto3" json:"state_info,omitempty"`
    	// Category being targeted by the insight.
    	Category Insight_Category `protobuf:"varint,7,opt,name=category,proto3,enum=google.cloud.recommender.v1beta1.Insight_Category" json:"category,omitempty"`
    	// Insight's severity.
    	Severity Insight_Severity `protobuf:"varint,15,opt,name=severity,proto3,enum=google.cloud.recommender.v1beta1.Insight_Severity" json:"severity,omitempty"`
    	// Fingerprint of the Insight. Provides optimistic locking when updating
    	// states.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=etag,proto3" json:"etag,omitempty"`
    	// Recommendations derived from this insight.
    	AssociatedRecommendations []*Insight_RecommendationReference `protobuf:"bytes,8,rep,name=associated_recommendations,json=associatedRecommendations,proto3" json:"associated_recommendations,omitempty"`
    	// contains filtered or unexported fields
    }

An insight along with the information used to derive the insight. The insight may have associated recommendations as well.

### func (*Insight) Descriptor 
    
    
    func (*Insight) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Insight.ProtoReflect.Descriptor instead.

### func (*Insight) GetAssociatedRecommendations 
    
    
    func (x *Insight) GetAssociatedRecommendations() []*Insight_RecommendationReference

### func (*Insight) GetCategory 
    
    
    func (x *Insight) GetCategory() Insight_Category

### func (*Insight) GetContent 
    
    
    func (x *Insight) GetContent() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*Insight) GetDescription 
    
    
    func (x *Insight) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Insight) GetEtag 
    
    
    func (x *Insight) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*Insight) GetInsightSubtype 
    
    
    func (x *Insight) GetInsightSubtype() [string](https://pkg.go.dev/builtin#string)

### func (*Insight) GetLastRefreshTime 
    
    
    func (x *Insight) GetLastRefreshTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Insight) GetName 
    
    
    func (x *Insight) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Insight) GetObservationPeriod 
    
    
    func (x *Insight) GetObservationPeriod() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Insight) GetSeverity 
    
    
    func (x *Insight) GetSeverity() Insight_Severity

### func (*Insight) GetStateInfo 
    
    
    func (x *Insight) GetStateInfo() *InsightStateInfo

### func (*Insight) GetTargetResources 
    
    
    func (x *Insight) GetTargetResources() [][string](https://pkg.go.dev/builtin#string)

### func (*Insight) ProtoMessage 
    
    
    func (*Insight) ProtoMessage()

### func (*Insight) ProtoReflect 
    
    
    func (x *Insight) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Insight) Reset 
    
    
    func (x *Insight) Reset()

### func (*Insight) String 
    
    
    func (x *Insight) String() [string](https://pkg.go.dev/builtin#string)

## InsightStateInfo
    
    
    type InsightStateInfo struct {
    
    	// Insight state.
    	State InsightStateInfo_State `protobuf:"varint,1,opt,name=state,proto3,enum=google.cloud.recommender.v1beta1.InsightStateInfo_State" json:"state,omitempty"`
    	// A map of metadata for the state, provided by user or automations systems.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

Information related to insight state.

### func (*InsightStateInfo) Descriptor 
    
    
    func (*InsightStateInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightStateInfo.ProtoReflect.Descriptor instead.

### func (*InsightStateInfo) GetState 
    
    
    func (x *InsightStateInfo) GetState() InsightStateInfo_State

### func (*InsightStateInfo) GetStateMetadata 
    
    
    func (x *InsightStateInfo) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*InsightStateInfo) ProtoMessage 
    
    
    func (*InsightStateInfo) ProtoMessage()

### func (*InsightStateInfo) ProtoReflect 
    
    
    func (x *InsightStateInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsightStateInfo) Reset 
    
    
    func (x *InsightStateInfo) Reset()

### func (*InsightStateInfo) String 
    
    
    func (x *InsightStateInfo) String() [string](https://pkg.go.dev/builtin#string)

## InsightStateInfo_State
    
    
    type InsightStateInfo_State [int32](https://pkg.go.dev/builtin#int32)

Represents insight state.

### InsightStateInfo_STATE_UNSPECIFIED, InsightStateInfo_ACTIVE, InsightStateInfo_ACCEPTED, InsightStateInfo_DISMISSED
    
    
    const (
    	// Unspecified state.
    	InsightStateInfo_STATE_UNSPECIFIED InsightStateInfo_State = 0
    	// Insight is active. Content for ACTIVE insights can be updated by Google.
    	// ACTIVE insights can be marked DISMISSED OR ACCEPTED.
    	InsightStateInfo_ACTIVE InsightStateInfo_State = 1
    	// Some action has been taken based on this insight. Insights become
    	// accepted when a recommendation derived from the insight has been marked
    	// CLAIMED, SUCCEEDED, or FAILED. ACTIVE insights can also be marked
    	// ACCEPTED explicitly. Content for ACCEPTED insights is immutable. ACCEPTED
    	// insights can only be marked ACCEPTED (which may update state metadata).
    	InsightStateInfo_ACCEPTED InsightStateInfo_State = 2
    	// Insight is dismissed. Content for DISMISSED insights can be updated by
    	// Google. DISMISSED insights can be marked as ACTIVE.
    	InsightStateInfo_DISMISSED InsightStateInfo_State = 3
    )

### func (InsightStateInfo_State) Descriptor 
    
    
    func (InsightStateInfo_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InsightStateInfo_State) Enum 
    
    
    func (x InsightStateInfo_State) Enum() *InsightStateInfo_State

### func (InsightStateInfo_State) EnumDescriptor 
    
    
    func (InsightStateInfo_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightStateInfo_State.Descriptor instead.

### func (InsightStateInfo_State) Number 
    
    
    func (x InsightStateInfo_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InsightStateInfo_State) String 
    
    
    func (x InsightStateInfo_State) String() [string](https://pkg.go.dev/builtin#string)

### func (InsightStateInfo_State) Type 
    
    
    func (InsightStateInfo_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## InsightType
    
    
    type InsightType struct {
    
    	// The insight_type’s name in format insightTypes/{insight_type}
    	// eg: insightTypes/google.iam.policy.Insight
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The type of insight.

### func (*InsightType) Descriptor 
    
    
    func (*InsightType) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightType.ProtoReflect.Descriptor instead.

### func (*InsightType) GetName 
    
    
    func (x *InsightType) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*InsightType) ProtoMessage 
    
    
    func (*InsightType) ProtoMessage()

### func (*InsightType) ProtoReflect 
    
    
    func (x *InsightType) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsightType) Reset 
    
    
    func (x *InsightType) Reset()

### func (*InsightType) String 
    
    
    func (x *InsightType) String() [string](https://pkg.go.dev/builtin#string)

## InsightTypeConfig
    
    
    type InsightTypeConfig struct {
    
    	// Name of insight type config.
    	// Eg,
    	// projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// InsightTypeGenerationConfig which configures the generation of
    	// insights for this insight type.
    	InsightTypeGenerationConfig *InsightTypeGenerationConfig `protobuf:"bytes,2,opt,name=insight_type_generation_config,json=insightTypeGenerationConfig,proto3" json:"insight_type_generation_config,omitempty"`
    	// Fingerprint of the InsightTypeConfig. Provides optimistic locking when
    	// updating.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// Last time when the config was updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. Immutable. The revision ID of the config.
    	// A new revision is committed whenever the config is changed in any way.
    	// The format is an 8-character hexadecimal string.
    	RevisionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=revision_id,json=revisionId,proto3" json:"revision_id,omitempty"`
    	// Allows clients to store small amounts of arbitrary data. Annotations must
    	// follow the Kubernetes syntax.
    	// The total size of all keys and values combined is limited to 256k.
    	// Key can have 2 segments: prefix (optional) and name (required),
    	// separated by a slash (/).
    	// Prefix must be a DNS subdomain.
    	// Name must be 63 characters or less, begin and end with alphanumerics,
    	// with dashes (-), underscores (_), dots (.), and alphanumerics between.
    	Annotations map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// A user-settable field to provide a human-readable name to be used in user
    	// interfaces.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for an InsightType.

### func (*InsightTypeConfig) Descriptor 
    
    
    func (*InsightTypeConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightTypeConfig.ProtoReflect.Descriptor instead.

### func (*InsightTypeConfig) GetAnnotations 
    
    
    func (x *InsightTypeConfig) GetAnnotations() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*InsightTypeConfig) GetDisplayName 
    
    
    func (x *InsightTypeConfig) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*InsightTypeConfig) GetEtag 
    
    
    func (x *InsightTypeConfig) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*InsightTypeConfig) GetInsightTypeGenerationConfig 
    
    
    func (x *InsightTypeConfig) GetInsightTypeGenerationConfig() *InsightTypeGenerationConfig

### func (*InsightTypeConfig) GetName 
    
    
    func (x *InsightTypeConfig) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*InsightTypeConfig) GetRevisionId 
    
    
    func (x *InsightTypeConfig) GetRevisionId() [string](https://pkg.go.dev/builtin#string)

### func (*InsightTypeConfig) GetUpdateTime 
    
    
    func (x *InsightTypeConfig) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*InsightTypeConfig) ProtoMessage 
    
    
    func (*InsightTypeConfig) ProtoMessage()

### func (*InsightTypeConfig) ProtoReflect 
    
    
    func (x *InsightTypeConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsightTypeConfig) Reset 
    
    
    func (x *InsightTypeConfig) Reset()

### func (*InsightTypeConfig) String 
    
    
    func (x *InsightTypeConfig) String() [string](https://pkg.go.dev/builtin#string)

## InsightTypeGenerationConfig
    
    
    type InsightTypeGenerationConfig struct {
    
    	// Parameters for this InsightTypeGenerationConfig. These configs can be used
    	// by or are applied to all subtypes.
    	Params *structpb.Struct `protobuf:"bytes,1,opt,name=params,proto3" json:"params,omitempty"`
    	// contains filtered or unexported fields
    }

A configuration to customize the generation of insights. Eg, customizing the lookback period considered when generating a insight.

### func (*InsightTypeGenerationConfig) Descriptor 
    
    
    func (*InsightTypeGenerationConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightTypeGenerationConfig.ProtoReflect.Descriptor instead.

### func (*InsightTypeGenerationConfig) GetParams 
    
    
    func (x *InsightTypeGenerationConfig) GetParams() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*InsightTypeGenerationConfig) ProtoMessage 
    
    
    func (*InsightTypeGenerationConfig) ProtoMessage()

### func (*InsightTypeGenerationConfig) ProtoReflect 
    
    
    func (x *InsightTypeGenerationConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsightTypeGenerationConfig) Reset 
    
    
    func (x *InsightTypeGenerationConfig) Reset()

### func (*InsightTypeGenerationConfig) String 
    
    
    func (x *InsightTypeGenerationConfig) String() [string](https://pkg.go.dev/builtin#string)

## Insight_Category
    
    
    type Insight_Category [int32](https://pkg.go.dev/builtin#int32)

Insight category.

### Insight_CATEGORY_UNSPECIFIED, Insight_COST, Insight_SECURITY, Insight_PERFORMANCE, Insight_MANAGEABILITY
    
    
    const (
    	// Unspecified category.
    	Insight_CATEGORY_UNSPECIFIED Insight_Category = 0
    	// The insight is related to cost.
    	Insight_COST Insight_Category = 1
    	// The insight is related to security.
    	Insight_SECURITY Insight_Category = 2
    	// The insight is related to performance.
    	Insight_PERFORMANCE Insight_Category = 3
    	// This insight is related to manageability.
    	Insight_MANAGEABILITY Insight_Category = 4
    )

### func (Insight_Category) Descriptor 
    
    
    func (Insight_Category) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Insight_Category) Enum 
    
    
    func (x Insight_Category) Enum() *Insight_Category

### func (Insight_Category) EnumDescriptor 
    
    
    func (Insight_Category) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Insight_Category.Descriptor instead.

### func (Insight_Category) Number 
    
    
    func (x Insight_Category) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Insight_Category) String 
    
    
    func (x Insight_Category) String() [string](https://pkg.go.dev/builtin#string)

### func (Insight_Category) Type 
    
    
    func (Insight_Category) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Insight_RecommendationReference
    
    
    type Insight_RecommendationReference struct {
    
    	// Recommendation resource name, e.g.
    	// projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/recommendations/[RECOMMENDATION_ID]
    	Recommendation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=recommendation,proto3" json:"recommendation,omitempty"`
    	// contains filtered or unexported fields
    }

Reference to an associated recommendation.

### func (*Insight_RecommendationReference) Descriptor 
    
    
    func (*Insight_RecommendationReference) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Insight_RecommendationReference.ProtoReflect.Descriptor instead.

### func (*Insight_RecommendationReference) GetRecommendation 
    
    
    func (x *Insight_RecommendationReference) GetRecommendation() [string](https://pkg.go.dev/builtin#string)

### func (*Insight_RecommendationReference) ProtoMessage 
    
    
    func (*Insight_RecommendationReference) ProtoMessage()

### func (*Insight_RecommendationReference) ProtoReflect 
    
    
    func (x *Insight_RecommendationReference) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Insight_RecommendationReference) Reset 
    
    
    func (x *Insight_RecommendationReference) Reset()

### func (*Insight_RecommendationReference) String 
    
    
    func (x *Insight_RecommendationReference) String() [string](https://pkg.go.dev/builtin#string)

## Insight_Severity
    
    
    type Insight_Severity [int32](https://pkg.go.dev/builtin#int32)

Insight severity levels.

### Insight_SEVERITY_UNSPECIFIED, Insight_LOW, Insight_MEDIUM, Insight_HIGH, Insight_CRITICAL
    
    
    const (
    	// Insight has unspecified severity.
    	Insight_SEVERITY_UNSPECIFIED Insight_Severity = 0
    	// Insight has low severity.
    	Insight_LOW Insight_Severity = 1
    	// Insight has medium severity.
    	Insight_MEDIUM Insight_Severity = 2
    	// Insight has high severity.
    	Insight_HIGH Insight_Severity = 3
    	// Insight has critical severity.
    	Insight_CRITICAL Insight_Severity = 4
    )

### func (Insight_Severity) Descriptor 
    
    
    func (Insight_Severity) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Insight_Severity) Enum 
    
    
    func (x Insight_Severity) Enum() *Insight_Severity

### func (Insight_Severity) EnumDescriptor 
    
    
    func (Insight_Severity) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Insight_Severity.Descriptor instead.

### func (Insight_Severity) Number 
    
    
    func (x Insight_Severity) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Insight_Severity) String 
    
    
    func (x Insight_Severity) String() [string](https://pkg.go.dev/builtin#string)

### func (Insight_Severity) Type 
    
    
    func (Insight_Severity) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListInsightTypesRequest
    
    
    type ListInsightTypesRequest struct {
    
    	// The number of InsightTypes to return per page. The service may return
    	// fewer than this value.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListRecommenders` call.
    	// Provide this to retrieve the subsequent page.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `ListInsightTypes` method.

### func (*ListInsightTypesRequest) Descriptor 
    
    
    func (*ListInsightTypesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInsightTypesRequest.ProtoReflect.Descriptor instead.

### func (*ListInsightTypesRequest) GetPageSize 
    
    
    func (x *ListInsightTypesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListInsightTypesRequest) GetPageToken 
    
    
    func (x *ListInsightTypesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightTypesRequest) ProtoMessage 
    
    
    func (*ListInsightTypesRequest) ProtoMessage()

### func (*ListInsightTypesRequest) ProtoReflect 
    
    
    func (x *ListInsightTypesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInsightTypesRequest) Reset 
    
    
    func (x *ListInsightTypesRequest) Reset()

### func (*ListInsightTypesRequest) String 
    
    
    func (x *ListInsightTypesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListInsightTypesResponse
    
    
    type ListInsightTypesResponse struct {
    
    	// The set of recommenders available
    	InsightTypes []*InsightType `protobuf:"bytes,1,rep,name=insight_types,json=insightTypes,proto3" json:"insight_types,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response for the `ListInsightTypes` method.

### func (*ListInsightTypesResponse) Descriptor 
    
    
    func (*ListInsightTypesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInsightTypesResponse.ProtoReflect.Descriptor instead.

### func (*ListInsightTypesResponse) GetInsightTypes 
    
    
    func (x *ListInsightTypesResponse) GetInsightTypes() []*InsightType

### func (*ListInsightTypesResponse) GetNextPageToken 
    
    
    func (x *ListInsightTypesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightTypesResponse) ProtoMessage 
    
    
    func (*ListInsightTypesResponse) ProtoMessage()

### func (*ListInsightTypesResponse) ProtoReflect 
    
    
    func (x *ListInsightTypesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInsightTypesResponse) Reset 
    
    
    func (x *ListInsightTypesResponse) Reset()

### func (*ListInsightTypesResponse) String 
    
    
    func (x *ListInsightTypesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListInsightsRequest
    
    
    type ListInsightsRequest struct {
    
    	// Required. The container resource on which to execute the request.
    	// Acceptable formats:
    	//
    	// * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
    	//
    	// * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
    	//
    	// * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
    	//
    	// * `folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
    	//
    	// * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
    	//
    	// LOCATION here refers to GCP Locations:
    	// https://cloud.google.com/about/locations/
    	// INSIGHT_TYPE_ID refers to supported insight types:
    	// https://cloud.google.com/recommender/docs/insights/insight-types.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of results to return from this request.
    	// Non-positive values are ignored. If not specified, the server will
    	// determine the number of results to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. If present, retrieves the next batch of results from the
    	// preceding call to this method. `page_token` must be the value of
    	// `next_page_token` from the previous response. The values of other method
    	// parameters must be identical to those in the previous call.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filter expression to restrict the insights returned. Supported
    	// filter fields:
    	//
    	// * `stateInfo.state`
    	//
    	// * `insightSubtype`
    	//
    	// * `severity`
    	//
    	// Examples:
    	//
    	// * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`
    	//
    	// * `insightSubtype = PERMISSIONS_USAGE`
    	//
    	// * `severity = CRITICAL OR severity = HIGH`
    	//
    	// * `stateInfo.state = ACTIVE AND (severity = CRITICAL OR severity = HIGH)`
    	//
    	// (These expressions are based on the filter language described at
    	// https://google.aip.dev/160)
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `ListInsights` method.

### func (*ListInsightsRequest) Descriptor 
    
    
    func (*ListInsightsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInsightsRequest.ProtoReflect.Descriptor instead.

### func (*ListInsightsRequest) GetFilter 
    
    
    func (x *ListInsightsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightsRequest) GetPageSize 
    
    
    func (x *ListInsightsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListInsightsRequest) GetPageToken 
    
    
    func (x *ListInsightsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightsRequest) GetParent 
    
    
    func (x *ListInsightsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightsRequest) ProtoMessage 
    
    
    func (*ListInsightsRequest) ProtoMessage()

### func (*ListInsightsRequest) ProtoReflect 
    
    
    func (x *ListInsightsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInsightsRequest) Reset 
    
    
    func (x *ListInsightsRequest) Reset()

### func (*ListInsightsRequest) String 
    
    
    func (x *ListInsightsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListInsightsResponse
    
    
    type ListInsightsResponse struct {
    
    	// The set of insights for the `parent` resource.
    	Insights []*Insight `protobuf:"bytes,1,rep,name=insights,proto3" json:"insights,omitempty"`
    	// A token that can be used to request the next page of results. This field is
    	// empty if there are no additional results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to the `ListInsights` method.

### func (*ListInsightsResponse) Descriptor 
    
    
    func (*ListInsightsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInsightsResponse.ProtoReflect.Descriptor instead.

### func (*ListInsightsResponse) GetInsights 
    
    
    func (x *ListInsightsResponse) GetInsights() []*Insight

### func (*ListInsightsResponse) GetNextPageToken 
    
    
    func (x *ListInsightsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInsightsResponse) ProtoMessage 
    
    
    func (*ListInsightsResponse) ProtoMessage()

### func (*ListInsightsResponse) ProtoReflect 
    
    
    func (x *ListInsightsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInsightsResponse) Reset 
    
    
    func (x *ListInsightsResponse) Reset()

### func (*ListInsightsResponse) String 
    
    
    func (x *ListInsightsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListRecommendationsRequest
    
    
    type ListRecommendationsRequest struct {
    
    	// Required. The container resource on which to execute the request.
    	// Acceptable formats:
    	//
    	// * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
    	//
    	// * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
    	//
    	// * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
    	//
    	// * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
    	//
    	// * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`
    	//
    	// LOCATION here refers to GCP Locations:
    	// https://cloud.google.com/about/locations/
    	// RECOMMENDER_ID refers to supported recommenders:
    	// https://cloud.google.com/recommender/docs/recommenders.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of results to return from this request.
    	// Non-positive values are ignored. If not specified, the server will
    	// determine the number of results to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. If present, retrieves the next batch of results from the
    	// preceding call to this method. `page_token` must be the value of
    	// `next_page_token` from the previous response. The values of other method
    	// parameters must be identical to those in the previous call.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filter expression to restrict the recommendations returned. Supported
    	// filter fields:
    	//
    	// * `state_info.state`
    	//
    	// * `recommenderSubtype`
    	//
    	// * `priority`
    	//
    	// Examples:
    	//
    	// * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`
    	//
    	// * `recommenderSubtype = REMOVE_ROLE OR recommenderSubtype = REPLACE_ROLE`
    	//
    	// * `priority = P1 OR priority = P2`
    	//
    	// * `stateInfo.state = ACTIVE AND (priority = P1 OR priority = P2)`
    	//
    	// (These expressions are based on the filter language described at
    	// https://google.aip.dev/160)
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `ListRecommendations` method.

### func (*ListRecommendationsRequest) Descriptor 
    
    
    func (*ListRecommendationsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRecommendationsRequest.ProtoReflect.Descriptor instead.

### func (*ListRecommendationsRequest) GetFilter 
    
    
    func (x *ListRecommendationsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendationsRequest) GetPageSize 
    
    
    func (x *ListRecommendationsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListRecommendationsRequest) GetPageToken 
    
    
    func (x *ListRecommendationsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendationsRequest) GetParent 
    
    
    func (x *ListRecommendationsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendationsRequest) ProtoMessage 
    
    
    func (*ListRecommendationsRequest) ProtoMessage()

### func (*ListRecommendationsRequest) ProtoReflect 
    
    
    func (x *ListRecommendationsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRecommendationsRequest) Reset 
    
    
    func (x *ListRecommendationsRequest) Reset()

### func (*ListRecommendationsRequest) String 
    
    
    func (x *ListRecommendationsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListRecommendationsResponse
    
    
    type ListRecommendationsResponse struct {
    
    	// The set of recommendations for the `parent` resource.
    	Recommendations []*Recommendation `protobuf:"bytes,1,rep,name=recommendations,proto3" json:"recommendations,omitempty"`
    	// A token that can be used to request the next page of results. This field is
    	// empty if there are no additional results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to the `ListRecommendations` method.

### func (*ListRecommendationsResponse) Descriptor 
    
    
    func (*ListRecommendationsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRecommendationsResponse.ProtoReflect.Descriptor instead.

### func (*ListRecommendationsResponse) GetNextPageToken 
    
    
    func (x *ListRecommendationsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendationsResponse) GetRecommendations 
    
    
    func (x *ListRecommendationsResponse) GetRecommendations() []*Recommendation

### func (*ListRecommendationsResponse) ProtoMessage 
    
    
    func (*ListRecommendationsResponse) ProtoMessage()

### func (*ListRecommendationsResponse) ProtoReflect 
    
    
    func (x *ListRecommendationsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRecommendationsResponse) Reset 
    
    
    func (x *ListRecommendationsResponse) Reset()

### func (*ListRecommendationsResponse) String 
    
    
    func (x *ListRecommendationsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListRecommendersRequest
    
    
    type ListRecommendersRequest struct {
    
    	// The number of RecommenderTypes to return per page. The service may return
    	// fewer than this value.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListRecommenders` call.
    	// Provide this to retrieve the subsequent page.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `ListRecommender` method.

### func (*ListRecommendersRequest) Descriptor 
    
    
    func (*ListRecommendersRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRecommendersRequest.ProtoReflect.Descriptor instead.

### func (*ListRecommendersRequest) GetPageSize 
    
    
    func (x *ListRecommendersRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListRecommendersRequest) GetPageToken 
    
    
    func (x *ListRecommendersRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendersRequest) ProtoMessage 
    
    
    func (*ListRecommendersRequest) ProtoMessage()

### func (*ListRecommendersRequest) ProtoReflect 
    
    
    func (x *ListRecommendersRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRecommendersRequest) Reset 
    
    
    func (x *ListRecommendersRequest) Reset()

### func (*ListRecommendersRequest) String 
    
    
    func (x *ListRecommendersRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListRecommendersResponse
    
    
    type ListRecommendersResponse struct {
    
    	// The set of recommenders available
    	Recommenders []*RecommenderType `protobuf:"bytes,1,rep,name=recommenders,proto3" json:"recommenders,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response for the `ListRecommender` method.

### func (*ListRecommendersResponse) Descriptor 
    
    
    func (*ListRecommendersResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRecommendersResponse.ProtoReflect.Descriptor instead.

### func (*ListRecommendersResponse) GetNextPageToken 
    
    
    func (x *ListRecommendersResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRecommendersResponse) GetRecommenders 
    
    
    func (x *ListRecommendersResponse) GetRecommenders() []*RecommenderType

### func (*ListRecommendersResponse) ProtoMessage 
    
    
    func (*ListRecommendersResponse) ProtoMessage()

### func (*ListRecommendersResponse) ProtoReflect 
    
    
    func (x *ListRecommendersResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRecommendersResponse) Reset 
    
    
    func (x *ListRecommendersResponse) Reset()

### func (*ListRecommendersResponse) String 
    
    
    func (x *ListRecommendersResponse) String() [string](https://pkg.go.dev/builtin#string)

## MarkInsightAcceptedRequest
    
    
    type MarkInsightAcceptedRequest struct {
    
    	// Required. Name of the insight.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. State properties user wish to include with this state.  Full
    	// replace of the current state_metadata.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Fingerprint of the Insight. Provides optimistic locking.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `MarkInsightAccepted` method.

### func (*MarkInsightAcceptedRequest) Descriptor 
    
    
    func (*MarkInsightAcceptedRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkInsightAcceptedRequest.ProtoReflect.Descriptor instead.

### func (*MarkInsightAcceptedRequest) GetEtag 
    
    
    func (x *MarkInsightAcceptedRequest) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*MarkInsightAcceptedRequest) GetName 
    
    
    func (x *MarkInsightAcceptedRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkInsightAcceptedRequest) GetStateMetadata 
    
    
    func (x *MarkInsightAcceptedRequest) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*MarkInsightAcceptedRequest) ProtoMessage 
    
    
    func (*MarkInsightAcceptedRequest) ProtoMessage()

### func (*MarkInsightAcceptedRequest) ProtoReflect 
    
    
    func (x *MarkInsightAcceptedRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkInsightAcceptedRequest) Reset 
    
    
    func (x *MarkInsightAcceptedRequest) Reset()

### func (*MarkInsightAcceptedRequest) String 
    
    
    func (x *MarkInsightAcceptedRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkRecommendationClaimedRequest
    
    
    type MarkRecommendationClaimedRequest struct {
    
    	// Required. Name of the recommendation.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// State properties to include with this state. Overwrites any existing
    	// `state_metadata`.
    	// Keys must match the regex `/^[a-z0-9][a-z0-9_.-]{0,62}$/`.
    	// Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Fingerprint of the Recommendation. Provides optimistic locking.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `MarkRecommendationClaimed` Method.

### func (*MarkRecommendationClaimedRequest) Descriptor 
    
    
    func (*MarkRecommendationClaimedRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkRecommendationClaimedRequest.ProtoReflect.Descriptor instead.

### func (*MarkRecommendationClaimedRequest) GetEtag 
    
    
    func (x *MarkRecommendationClaimedRequest) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationClaimedRequest) GetName 
    
    
    func (x *MarkRecommendationClaimedRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationClaimedRequest) GetStateMetadata 
    
    
    func (x *MarkRecommendationClaimedRequest) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationClaimedRequest) ProtoMessage 
    
    
    func (*MarkRecommendationClaimedRequest) ProtoMessage()

### func (*MarkRecommendationClaimedRequest) ProtoReflect 
    
    
    func (x *MarkRecommendationClaimedRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkRecommendationClaimedRequest) Reset 
    
    
    func (x *MarkRecommendationClaimedRequest) Reset()

### func (*MarkRecommendationClaimedRequest) String 
    
    
    func (x *MarkRecommendationClaimedRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkRecommendationFailedRequest
    
    
    type MarkRecommendationFailedRequest struct {
    
    	// Required. Name of the recommendation.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// State properties to include with this state. Overwrites any existing
    	// `state_metadata`.
    	// Keys must match the regex `/^[a-z0-9][a-z0-9_.-]{0,62}$/`.
    	// Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Fingerprint of the Recommendation. Provides optimistic locking.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `MarkRecommendationFailed` Method.

### func (*MarkRecommendationFailedRequest) Descriptor 
    
    
    func (*MarkRecommendationFailedRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkRecommendationFailedRequest.ProtoReflect.Descriptor instead.

### func (*MarkRecommendationFailedRequest) GetEtag 
    
    
    func (x *MarkRecommendationFailedRequest) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationFailedRequest) GetName 
    
    
    func (x *MarkRecommendationFailedRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationFailedRequest) GetStateMetadata 
    
    
    func (x *MarkRecommendationFailedRequest) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationFailedRequest) ProtoMessage 
    
    
    func (*MarkRecommendationFailedRequest) ProtoMessage()

### func (*MarkRecommendationFailedRequest) ProtoReflect 
    
    
    func (x *MarkRecommendationFailedRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkRecommendationFailedRequest) Reset 
    
    
    func (x *MarkRecommendationFailedRequest) Reset()

### func (*MarkRecommendationFailedRequest) String 
    
    
    func (x *MarkRecommendationFailedRequest) String() [string](https://pkg.go.dev/builtin#string)

## MarkRecommendationSucceededRequest
    
    
    type MarkRecommendationSucceededRequest struct {
    
    	// Required. Name of the recommendation.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// State properties to include with this state. Overwrites any existing
    	// `state_metadata`.
    	// Keys must match the regex `/^[a-z0-9][a-z0-9_.-]{0,62}$/`.
    	// Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Fingerprint of the Recommendation. Provides optimistic locking.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `MarkRecommendationSucceeded` Method.

### func (*MarkRecommendationSucceededRequest) Descriptor 
    
    
    func (*MarkRecommendationSucceededRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MarkRecommendationSucceededRequest.ProtoReflect.Descriptor instead.

### func (*MarkRecommendationSucceededRequest) GetEtag 
    
    
    func (x *MarkRecommendationSucceededRequest) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationSucceededRequest) GetName 
    
    
    func (x *MarkRecommendationSucceededRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationSucceededRequest) GetStateMetadata 
    
    
    func (x *MarkRecommendationSucceededRequest) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*MarkRecommendationSucceededRequest) ProtoMessage 
    
    
    func (*MarkRecommendationSucceededRequest) ProtoMessage()

### func (*MarkRecommendationSucceededRequest) ProtoReflect 
    
    
    func (x *MarkRecommendationSucceededRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MarkRecommendationSucceededRequest) Reset 
    
    
    func (x *MarkRecommendationSucceededRequest) Reset()

### func (*MarkRecommendationSucceededRequest) String 
    
    
    func (x *MarkRecommendationSucceededRequest) String() [string](https://pkg.go.dev/builtin#string)

## Operation
    
    
    type Operation struct {
    
    	// Type of this operation. Contains one of 'add', 'remove', 'replace', 'move',
    	// 'copy', 'test' and 'custom' operations. This field is case-insensitive and
    	// always populated.
    	Action [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=action,proto3" json:"action,omitempty"`
    	// Type of GCP resource being modified/tested. This field is always populated.
    	// Example: cloudresourcemanager.googleapis.com/Project,
    	// compute.googleapis.com/Instance
    	ResourceType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=resource_type,json=resourceType,proto3" json:"resource_type,omitempty"`
    	// Contains the fully qualified resource name. This field is always populated.
    	// ex: //cloudresourcemanager.googleapis.com/projects/foo.
    	Resource [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=resource,proto3" json:"resource,omitempty"`
    	// Path to the target field being operated on. If the operation is at the
    	// resource level, then path should be "/". This field is always populated.
    	Path [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=path,proto3" json:"path,omitempty"`
    	// Can be set with action 'copy' to copy resource configuration across
    	// different resources of the same type. Example: A resource clone can be
    	// done via action = 'copy', path = "/", from = "/",
    	// source_resource =  and resource_name = 

Contains an operation for a resource loosely based on the JSON-PATCH format with support for:

  * Custom filters for describing partial array patch.
  * Extended path values for describing nested arrays.
  * Custom fields for describing the resource for which the operation is being described.
  * Allows extension to custom operations not natively supported by RFC6902.



See <https://tools.ietf.org/html/rfc6902> for details on the original RFC.

### func (*Operation) Descriptor 
    
    
    func (*Operation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Operation.ProtoReflect.Descriptor instead.

### func (*Operation) GetAction 
    
    
    func (x *Operation) GetAction() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetPath 
    
    
    func (x *Operation) GetPath() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetPathFilters 
    
    
    func (x *Operation) GetPathFilters() map[[string](https://pkg.go.dev/builtin#string)]*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Value)

### func (*Operation) GetPathValue 
    
    
    func (x *Operation) GetPathValue() isOperation_PathValue

### func (*Operation) GetPathValueMatchers 
    
    
    func (x *Operation) GetPathValueMatchers() map[[string](https://pkg.go.dev/builtin#string)]*ValueMatcher

### func (*Operation) GetResource 
    
    
    func (x *Operation) GetResource() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetResourceType 
    
    
    func (x *Operation) GetResourceType() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetSourcePath 
    
    
    func (x *Operation) GetSourcePath() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetSourceResource 
    
    
    func (x *Operation) GetSourceResource() [string](https://pkg.go.dev/builtin#string)

### func (*Operation) GetValue 
    
    
    func (x *Operation) GetValue() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Value)

### func (*Operation) GetValueMatcher 
    
    
    func (x *Operation) GetValueMatcher() *ValueMatcher

### func (*Operation) ProtoMessage 
    
    
    func (*Operation) ProtoMessage()

### func (*Operation) ProtoReflect 
    
    
    func (x *Operation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Operation) Reset 
    
    
    func (x *Operation) Reset()

### func (*Operation) String 
    
    
    func (x *Operation) String() [string](https://pkg.go.dev/builtin#string)

## OperationGroup
    
    
    type OperationGroup struct {
    
    	// List of operations across one or more resources that belong to this group.
    	// Loosely based on RFC6902 and should be performed in the order they appear.
    	Operations []*Operation `protobuf:"bytes,1,rep,name=operations,proto3" json:"operations,omitempty"`
    	// contains filtered or unexported fields
    }

Group of operations that need to be performed atomically.

### func (*OperationGroup) Descriptor 
    
    
    func (*OperationGroup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OperationGroup.ProtoReflect.Descriptor instead.

### func (*OperationGroup) GetOperations 
    
    
    func (x *OperationGroup) GetOperations() []*Operation

### func (*OperationGroup) ProtoMessage 
    
    
    func (*OperationGroup) ProtoMessage()

### func (*OperationGroup) ProtoReflect 
    
    
    func (x *OperationGroup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OperationGroup) Reset 
    
    
    func (x *OperationGroup) Reset()

### func (*OperationGroup) String 
    
    
    func (x *OperationGroup) String() [string](https://pkg.go.dev/builtin#string)

## Operation_Value
    
    
    type Operation_Value struct {
    	// Value for the `path` field. Will be set for actions:'add'/'replace'.
    	// Maybe set for action: 'test'. Either this or `value_matcher` will be set
    	// for 'test' operation. An exact match must be performed.
    	Value *structpb.Value `protobuf:"bytes,7,opt,name=value,proto3,oneof"`
    }

## Operation_ValueMatcher
    
    
    type Operation_ValueMatcher struct {
    	// Can be set for action 'test' for advanced matching for the value of
    	// 'path' field. Either this or `value` will be set for 'test' operation.
    	ValueMatcher *ValueMatcher `protobuf:"bytes,10,opt,name=value_matcher,json=valueMatcher,proto3,oneof"`
    }

## Recommendation
    
    
    type Recommendation struct {
    
    	// Name of recommendation.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Free-form human readable summary in English. The maximum length is 500
    	// characters.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// Contains an identifier for a subtype of recommendations produced for the
    	// same recommender. Subtype is a function of content and impact, meaning a
    	// new subtype might be added when significant changes to `content` or
    	// `primary_impact.category` are introduced. See the Recommenders section
    	// to see a list of subtypes for a given Recommender.
    	//
    	// Examples:
    	//
    	//	For recommender = "google.iam.policy.Recommender",
    	//	recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE"
    	RecommenderSubtype [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,12,opt,name=recommender_subtype,json=recommenderSubtype,proto3" json:"recommender_subtype,omitempty"`
    	// Last time this recommendation was refreshed by the system that created it
    	// in the first place.
    	LastRefreshTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=last_refresh_time,json=lastRefreshTime,proto3" json:"last_refresh_time,omitempty"`
    	// The primary impact that this recommendation can have while trying to
    	// optimize for one category.
    	PrimaryImpact *Impact `protobuf:"bytes,5,opt,name=primary_impact,json=primaryImpact,proto3" json:"primary_impact,omitempty"`
    	// Optional set of additional impact that this recommendation may have when
    	// trying to optimize for the primary category. These may be positive
    	// or negative.
    	AdditionalImpact []*Impact `protobuf:"bytes,6,rep,name=additional_impact,json=additionalImpact,proto3" json:"additional_impact,omitempty"`
    	// Recommendation's priority.
    	Priority Recommendation_Priority `protobuf:"varint,17,opt,name=priority,proto3,enum=google.cloud.recommender.v1beta1.Recommendation_Priority" json:"priority,omitempty"`
    	// Content of the recommendation describing recommended changes to resources.
    	Content *RecommendationContent `protobuf:"bytes,7,opt,name=content,proto3" json:"content,omitempty"`
    	// Information for state. Contains state and metadata.
    	StateInfo *RecommendationStateInfo `protobuf:"bytes,10,opt,name=state_info,json=stateInfo,proto3" json:"state_info,omitempty"`
    	// Fingerprint of the Recommendation. Provides optimistic locking when
    	// updating states.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=etag,proto3" json:"etag,omitempty"`
    	// Insights that led to this recommendation.
    	AssociatedInsights []*Recommendation_InsightReference `protobuf:"bytes,14,rep,name=associated_insights,json=associatedInsights,proto3" json:"associated_insights,omitempty"`
    	// Corresponds to a mutually exclusive group ID within a recommender.
    	// A non-empty ID indicates that the recommendation belongs to a mutually
    	// exclusive group. This means that only one recommendation within the group
    	// is suggested to be applied.
    	XorGroupId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,18,opt,name=xor_group_id,json=xorGroupId,proto3" json:"xor_group_id,omitempty"`
    	// contains filtered or unexported fields
    }

A recommendation along with a suggested action. E.g., a rightsizing recommendation for an underutilized VM, IAM role recommendations, etc

### func (*Recommendation) Descriptor 
    
    
    func (*Recommendation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Recommendation.ProtoReflect.Descriptor instead.

### func (*Recommendation) GetAdditionalImpact 
    
    
    func (x *Recommendation) GetAdditionalImpact() []*Impact

### func (*Recommendation) GetAssociatedInsights 
    
    
    func (x *Recommendation) GetAssociatedInsights() []*Recommendation_InsightReference

### func (*Recommendation) GetContent 
    
    
    func (x *Recommendation) GetContent() *RecommendationContent

### func (*Recommendation) GetDescription 
    
    
    func (x *Recommendation) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation) GetEtag 
    
    
    func (x *Recommendation) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation) GetLastRefreshTime 
    
    
    func (x *Recommendation) GetLastRefreshTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Recommendation) GetName 
    
    
    func (x *Recommendation) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation) GetPrimaryImpact 
    
    
    func (x *Recommendation) GetPrimaryImpact() *Impact

### func (*Recommendation) GetPriority 
    
    
    func (x *Recommendation) GetPriority() Recommendation_Priority

### func (*Recommendation) GetRecommenderSubtype 
    
    
    func (x *Recommendation) GetRecommenderSubtype() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation) GetStateInfo 
    
    
    func (x *Recommendation) GetStateInfo() *RecommendationStateInfo

### func (*Recommendation) GetXorGroupId 
    
    
    func (x *Recommendation) GetXorGroupId() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation) ProtoMessage 
    
    
    func (*Recommendation) ProtoMessage()

### func (*Recommendation) ProtoReflect 
    
    
    func (x *Recommendation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Recommendation) Reset 
    
    
    func (x *Recommendation) Reset()

### func (*Recommendation) String 
    
    
    func (x *Recommendation) String() [string](https://pkg.go.dev/builtin#string)

## RecommendationContent
    
    
    type RecommendationContent struct {
    
    	// Operations to one or more Google Cloud resources grouped in such a way
    	// that, all operations within one group are expected to be performed
    	// atomically and in an order.
    	OperationGroups []*OperationGroup `protobuf:"bytes,2,rep,name=operation_groups,json=operationGroups,proto3" json:"operation_groups,omitempty"`
    	// Condensed overview information about the recommendation.
    	Overview *structpb.Struct `protobuf:"bytes,3,opt,name=overview,proto3" json:"overview,omitempty"`
    	// contains filtered or unexported fields
    }

Contains what resources are changing and how they are changing.

### func (*RecommendationContent) Descriptor 
    
    
    func (*RecommendationContent) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommendationContent.ProtoReflect.Descriptor instead.

### func (*RecommendationContent) GetOperationGroups 
    
    
    func (x *RecommendationContent) GetOperationGroups() []*OperationGroup

### func (*RecommendationContent) GetOverview 
    
    
    func (x *RecommendationContent) GetOverview() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*RecommendationContent) ProtoMessage 
    
    
    func (*RecommendationContent) ProtoMessage()

### func (*RecommendationContent) ProtoReflect 
    
    
    func (x *RecommendationContent) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RecommendationContent) Reset 
    
    
    func (x *RecommendationContent) Reset()

### func (*RecommendationContent) String 
    
    
    func (x *RecommendationContent) String() [string](https://pkg.go.dev/builtin#string)

## RecommendationStateInfo
    
    
    type RecommendationStateInfo struct {
    
    	// The state of the recommendation, Eg ACTIVE, SUCCEEDED, FAILED.
    	State RecommendationStateInfo_State `protobuf:"varint,1,opt,name=state,proto3,enum=google.cloud.recommender.v1beta1.RecommendationStateInfo_State" json:"state,omitempty"`
    	// A map of metadata for the state, provided by user or automations systems.
    	StateMetadata map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=state_metadata,json=stateMetadata,proto3" json:"state_metadata,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

Information for state. Contains state and metadata.

### func (*RecommendationStateInfo) Descriptor 
    
    
    func (*RecommendationStateInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommendationStateInfo.ProtoReflect.Descriptor instead.

### func (*RecommendationStateInfo) GetState 
    
    
    func (x *RecommendationStateInfo) GetState() RecommendationStateInfo_State

### func (*RecommendationStateInfo) GetStateMetadata 
    
    
    func (x *RecommendationStateInfo) GetStateMetadata() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*RecommendationStateInfo) ProtoMessage 
    
    
    func (*RecommendationStateInfo) ProtoMessage()

### func (*RecommendationStateInfo) ProtoReflect 
    
    
    func (x *RecommendationStateInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RecommendationStateInfo) Reset 
    
    
    func (x *RecommendationStateInfo) Reset()

### func (*RecommendationStateInfo) String 
    
    
    func (x *RecommendationStateInfo) String() [string](https://pkg.go.dev/builtin#string)

## RecommendationStateInfo_State
    
    
    type RecommendationStateInfo_State [int32](https://pkg.go.dev/builtin#int32)

Represents Recommendation State.

### RecommendationStateInfo_STATE_UNSPECIFIED, RecommendationStateInfo_ACTIVE, RecommendationStateInfo_CLAIMED, RecommendationStateInfo_SUCCEEDED, RecommendationStateInfo_FAILED, RecommendationStateInfo_DISMISSED
    
    
    const (
    	// Default state. Don't use directly.
    	RecommendationStateInfo_STATE_UNSPECIFIED RecommendationStateInfo_State = 0
    	// Recommendation is active and can be applied. Recommendations content can
    	// be updated by Google.
    	//
    	// ACTIVE recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.
    	RecommendationStateInfo_ACTIVE RecommendationStateInfo_State = 1
    	// Recommendation is in claimed state. Recommendations content is
    	// immutable and cannot be updated by Google.
    	//
    	// CLAIMED recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.
    	RecommendationStateInfo_CLAIMED RecommendationStateInfo_State = 6
    	// Recommendation is in succeeded state. Recommendations content is
    	// immutable and cannot be updated by Google.
    	//
    	// SUCCEEDED recommendations can be marked as SUCCEEDED, or FAILED.
    	RecommendationStateInfo_SUCCEEDED RecommendationStateInfo_State = 3
    	// Recommendation is in failed state. Recommendations content is immutable
    	// and cannot be updated by Google.
    	//
    	// FAILED recommendations can be marked as SUCCEEDED, or FAILED.
    	RecommendationStateInfo_FAILED RecommendationStateInfo_State = 4
    	// Recommendation is in dismissed state. Recommendation content can be
    	// updated by Google.
    	//
    	// DISMISSED recommendations can be marked as ACTIVE.
    	RecommendationStateInfo_DISMISSED RecommendationStateInfo_State = 5
    )

### func (RecommendationStateInfo_State) Descriptor 
    
    
    func (RecommendationStateInfo_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RecommendationStateInfo_State) Enum 
    
    
    func (x RecommendationStateInfo_State) Enum() *RecommendationStateInfo_State

### func (RecommendationStateInfo_State) EnumDescriptor 
    
    
    func (RecommendationStateInfo_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommendationStateInfo_State.Descriptor instead.

### func (RecommendationStateInfo_State) Number 
    
    
    func (x RecommendationStateInfo_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RecommendationStateInfo_State) String 
    
    
    func (x RecommendationStateInfo_State) String() [string](https://pkg.go.dev/builtin#string)

### func (RecommendationStateInfo_State) Type 
    
    
    func (RecommendationStateInfo_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Recommendation_InsightReference
    
    
    type Recommendation_InsightReference struct {
    
    	// Insight resource name, e.g.
    	// projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/insights/[INSIGHT_ID]
    	Insight [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=insight,proto3" json:"insight,omitempty"`
    	// contains filtered or unexported fields
    }

Reference to an associated insight.

### func (*Recommendation_InsightReference) Descriptor 
    
    
    func (*Recommendation_InsightReference) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Recommendation_InsightReference.ProtoReflect.Descriptor instead.

### func (*Recommendation_InsightReference) GetInsight 
    
    
    func (x *Recommendation_InsightReference) GetInsight() [string](https://pkg.go.dev/builtin#string)

### func (*Recommendation_InsightReference) ProtoMessage 
    
    
    func (*Recommendation_InsightReference) ProtoMessage()

### func (*Recommendation_InsightReference) ProtoReflect 
    
    
    func (x *Recommendation_InsightReference) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Recommendation_InsightReference) Reset 
    
    
    func (x *Recommendation_InsightReference) Reset()

### func (*Recommendation_InsightReference) String 
    
    
    func (x *Recommendation_InsightReference) String() [string](https://pkg.go.dev/builtin#string)

## Recommendation_Priority
    
    
    type Recommendation_Priority [int32](https://pkg.go.dev/builtin#int32)

Recommendation priority levels.

### Recommendation_PRIORITY_UNSPECIFIED, Recommendation_P4, Recommendation_P3, Recommendation_P2, Recommendation_P1
    
    
    const (
    	// Recommendation has unspecified priority.
    	Recommendation_PRIORITY_UNSPECIFIED Recommendation_Priority = 0
    	// Recommendation has P4 priority (lowest priority).
    	Recommendation_P4 Recommendation_Priority = 1
    	// Recommendation has P3 priority (second lowest priority).
    	Recommendation_P3 Recommendation_Priority = 2
    	// Recommendation has P2 priority (second highest priority).
    	Recommendation_P2 Recommendation_Priority = 3
    	// Recommendation has P1 priority (highest priority).
    	Recommendation_P1 Recommendation_Priority = 4
    )

### func (Recommendation_Priority) Descriptor 
    
    
    func (Recommendation_Priority) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Recommendation_Priority) Enum 
    
    
    func (x Recommendation_Priority) Enum() *Recommendation_Priority

### func (Recommendation_Priority) EnumDescriptor 
    
    
    func (Recommendation_Priority) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Recommendation_Priority.Descriptor instead.

### func (Recommendation_Priority) Number 
    
    
    func (x Recommendation_Priority) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Recommendation_Priority) String 
    
    
    func (x Recommendation_Priority) String() [string](https://pkg.go.dev/builtin#string)

### func (Recommendation_Priority) Type 
    
    
    func (Recommendation_Priority) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RecommenderClient
    
    
    type RecommenderClient interface {
    	// Lists insights for the specified Cloud Resource. Requires the
    	// recommender.*.list IAM permission for the specified insight type.
    	ListInsights(ctx context.Context, in *ListInsightsRequest, opts ...grpc.CallOption) (*ListInsightsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested insight. Requires the recommender.*.get IAM permission
    	// for the specified insight type.
    	GetInsight(ctx context.Context, in *GetInsightRequest, opts ...grpc.CallOption) (*Insight, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Insight State as Accepted. Users can use this method to
    	// indicate to the Recommender API that they have applied some action based
    	// on the insight. This stops the insight content from being updated.
    	//
    	// MarkInsightAccepted can be applied to insights in ACTIVE state. Requires
    	// the recommender.*.update IAM permission for the specified insight.
    	MarkInsightAccepted(ctx context.Context, in *MarkInsightAcceptedRequest, opts ...grpc.CallOption) (*Insight, [error](https://pkg.go.dev/builtin#error))
    	// Lists recommendations for the specified Cloud Resource. Requires the
    	// recommender.*.list IAM permission for the specified recommender.
    	ListRecommendations(ctx context.Context, in *ListRecommendationsRequest, opts ...grpc.CallOption) (*ListRecommendationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested recommendation. Requires the recommender.*.get
    	// IAM permission for the specified recommender.
    	GetRecommendation(ctx context.Context, in *GetRecommendationRequest, opts ...grpc.CallOption) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Claimed. Users can use this method to
    	// indicate to the Recommender API that they are starting to apply the
    	// recommendation themselves. This stops the recommendation content from being
    	// updated. Associated insights are frozen and placed in the ACCEPTED state.
    	//
    	// MarkRecommendationClaimed can be applied to recommendations in CLAIMED or
    	// ACTIVE state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationClaimed(ctx context.Context, in *MarkRecommendationClaimedRequest, opts ...grpc.CallOption) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Succeeded. Users can use this method to
    	// indicate to the Recommender API that they have applied the recommendation
    	// themselves, and the operation was successful. This stops the recommendation
    	// content from being updated. Associated insights are frozen and placed in
    	// the ACCEPTED state.
    	//
    	// MarkRecommendationSucceeded can be applied to recommendations in ACTIVE,
    	// CLAIMED, SUCCEEDED, or FAILED state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationSucceeded(ctx context.Context, in *MarkRecommendationSucceededRequest, opts ...grpc.CallOption) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Failed. Users can use this method to
    	// indicate to the Recommender API that they have applied the recommendation
    	// themselves, and the operation failed. This stops the recommendation content
    	// from being updated. Associated insights are frozen and placed in the
    	// ACCEPTED state.
    	//
    	// MarkRecommendationFailed can be applied to recommendations in ACTIVE,
    	// CLAIMED, SUCCEEDED, or FAILED state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationFailed(ctx context.Context, in *MarkRecommendationFailedRequest, opts ...grpc.CallOption) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested Recommender Config. There is only one instance of the
    	// config for each Recommender.
    	GetRecommenderConfig(ctx context.Context, in *GetRecommenderConfigRequest, opts ...grpc.CallOption) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates a Recommender Config. This will create a new revision of the
    	// config.
    	UpdateRecommenderConfig(ctx context.Context, in *UpdateRecommenderConfigRequest, opts ...grpc.CallOption) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested InsightTypeConfig. There is only one instance of the
    	// config for each InsightType.
    	GetInsightTypeConfig(ctx context.Context, in *GetInsightTypeConfigRequest, opts ...grpc.CallOption) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates an InsightTypeConfig change. This will create a new revision of the
    	// config.
    	UpdateInsightTypeConfig(ctx context.Context, in *UpdateInsightTypeConfigRequest, opts ...grpc.CallOption) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))
    	// Lists all available Recommenders.
    	// No IAM permissions are required.
    	ListRecommenders(ctx context.Context, in *ListRecommendersRequest, opts ...grpc.CallOption) (*ListRecommendersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists available InsightTypes.
    	// No IAM permissions are required.
    	ListInsightTypes(ctx context.Context, in *ListInsightTypesRequest, opts ...grpc.CallOption) (*ListInsightTypesResponse, [error](https://pkg.go.dev/builtin#error))
    }

RecommenderClient is the client API for Recommender service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewRecommenderClient 
    
    
    func NewRecommenderClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) RecommenderClient

## RecommenderConfig
    
    
    type RecommenderConfig struct {
    
    	// Name of recommender config.
    	// Eg,
    	// projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// RecommenderGenerationConfig which configures the Generation of
    	// recommendations for this recommender.
    	RecommenderGenerationConfig *RecommenderGenerationConfig `protobuf:"bytes,2,opt,name=recommender_generation_config,json=recommenderGenerationConfig,proto3" json:"recommender_generation_config,omitempty"`
    	// Fingerprint of the RecommenderConfig. Provides optimistic locking when
    	// updating.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=etag,proto3" json:"etag,omitempty"`
    	// Last time when the config was updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. Immutable. The revision ID of the config.
    	// A new revision is committed whenever the config is changed in any way.
    	// The format is an 8-character hexadecimal string.
    	RevisionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=revision_id,json=revisionId,proto3" json:"revision_id,omitempty"`
    	// Allows clients to store small amounts of arbitrary data. Annotations must
    	// follow the Kubernetes syntax.
    	// The total size of all keys and values combined is limited to 256k.
    	// Key can have 2 segments: prefix (optional) and name (required),
    	// separated by a slash (/).
    	// Prefix must be a DNS subdomain.
    	// Name must be 63 characters or less, begin and end with alphanumerics,
    	// with dashes (-), underscores (_), dots (.), and alphanumerics between.
    	Annotations map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// A user-settable field to provide a human-readable name to be used in user
    	// interfaces.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for a Recommender.

### func (*RecommenderConfig) Descriptor 
    
    
    func (*RecommenderConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommenderConfig.ProtoReflect.Descriptor instead.

### func (*RecommenderConfig) GetAnnotations 
    
    
    func (x *RecommenderConfig) GetAnnotations() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*RecommenderConfig) GetDisplayName 
    
    
    func (x *RecommenderConfig) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*RecommenderConfig) GetEtag 
    
    
    func (x *RecommenderConfig) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*RecommenderConfig) GetName 
    
    
    func (x *RecommenderConfig) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RecommenderConfig) GetRecommenderGenerationConfig 
    
    
    func (x *RecommenderConfig) GetRecommenderGenerationConfig() *RecommenderGenerationConfig

### func (*RecommenderConfig) GetRevisionId 
    
    
    func (x *RecommenderConfig) GetRevisionId() [string](https://pkg.go.dev/builtin#string)

### func (*RecommenderConfig) GetUpdateTime 
    
    
    func (x *RecommenderConfig) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*RecommenderConfig) ProtoMessage 
    
    
    func (*RecommenderConfig) ProtoMessage()

### func (*RecommenderConfig) ProtoReflect 
    
    
    func (x *RecommenderConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RecommenderConfig) Reset 
    
    
    func (x *RecommenderConfig) Reset()

### func (*RecommenderConfig) String 
    
    
    func (x *RecommenderConfig) String() [string](https://pkg.go.dev/builtin#string)

## RecommenderGenerationConfig
    
    
    type RecommenderGenerationConfig struct {
    
    	// Parameters for this RecommenderGenerationConfig. These configs can be used
    	// by or are applied to all subtypes.
    	Params *structpb.Struct `protobuf:"bytes,1,opt,name=params,proto3" json:"params,omitempty"`
    	// contains filtered or unexported fields
    }

A Configuration to customize the generation of recommendations. Eg, customizing the lookback period considered when generating a recommendation.

### func (*RecommenderGenerationConfig) Descriptor 
    
    
    func (*RecommenderGenerationConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommenderGenerationConfig.ProtoReflect.Descriptor instead.

### func (*RecommenderGenerationConfig) GetParams 
    
    
    func (x *RecommenderGenerationConfig) GetParams() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*RecommenderGenerationConfig) ProtoMessage 
    
    
    func (*RecommenderGenerationConfig) ProtoMessage()

### func (*RecommenderGenerationConfig) ProtoReflect 
    
    
    func (x *RecommenderGenerationConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RecommenderGenerationConfig) Reset 
    
    
    func (x *RecommenderGenerationConfig) Reset()

### func (*RecommenderGenerationConfig) String 
    
    
    func (x *RecommenderGenerationConfig) String() [string](https://pkg.go.dev/builtin#string)

## RecommenderServer
    
    
    type RecommenderServer interface {
    	// Lists insights for the specified Cloud Resource. Requires the
    	// recommender.*.list IAM permission for the specified insight type.
    	ListInsights(context.Context, *ListInsightsRequest) (*ListInsightsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested insight. Requires the recommender.*.get IAM permission
    	// for the specified insight type.
    	GetInsight(context.Context, *GetInsightRequest) (*Insight, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Insight State as Accepted. Users can use this method to
    	// indicate to the Recommender API that they have applied some action based
    	// on the insight. This stops the insight content from being updated.
    	//
    	// MarkInsightAccepted can be applied to insights in ACTIVE state. Requires
    	// the recommender.*.update IAM permission for the specified insight.
    	MarkInsightAccepted(context.Context, *MarkInsightAcceptedRequest) (*Insight, [error](https://pkg.go.dev/builtin#error))
    	// Lists recommendations for the specified Cloud Resource. Requires the
    	// recommender.*.list IAM permission for the specified recommender.
    	ListRecommendations(context.Context, *ListRecommendationsRequest) (*ListRecommendationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested recommendation. Requires the recommender.*.get
    	// IAM permission for the specified recommender.
    	GetRecommendation(context.Context, *GetRecommendationRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Claimed. Users can use this method to
    	// indicate to the Recommender API that they are starting to apply the
    	// recommendation themselves. This stops the recommendation content from being
    	// updated. Associated insights are frozen and placed in the ACCEPTED state.
    	//
    	// MarkRecommendationClaimed can be applied to recommendations in CLAIMED or
    	// ACTIVE state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationClaimed(context.Context, *MarkRecommendationClaimedRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Succeeded. Users can use this method to
    	// indicate to the Recommender API that they have applied the recommendation
    	// themselves, and the operation was successful. This stops the recommendation
    	// content from being updated. Associated insights are frozen and placed in
    	// the ACCEPTED state.
    	//
    	// MarkRecommendationSucceeded can be applied to recommendations in ACTIVE,
    	// CLAIMED, SUCCEEDED, or FAILED state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationSucceeded(context.Context, *MarkRecommendationSucceededRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Marks the Recommendation State as Failed. Users can use this method to
    	// indicate to the Recommender API that they have applied the recommendation
    	// themselves, and the operation failed. This stops the recommendation content
    	// from being updated. Associated insights are frozen and placed in the
    	// ACCEPTED state.
    	//
    	// MarkRecommendationFailed can be applied to recommendations in ACTIVE,
    	// CLAIMED, SUCCEEDED, or FAILED state.
    	//
    	// Requires the recommender.*.update IAM permission for the specified
    	// recommender.
    	MarkRecommendationFailed(context.Context, *MarkRecommendationFailedRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested Recommender Config. There is only one instance of the
    	// config for each Recommender.
    	GetRecommenderConfig(context.Context, *GetRecommenderConfigRequest) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates a Recommender Config. This will create a new revision of the
    	// config.
    	UpdateRecommenderConfig(context.Context, *UpdateRecommenderConfigRequest) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))
    	// Gets the requested InsightTypeConfig. There is only one instance of the
    	// config for each InsightType.
    	GetInsightTypeConfig(context.Context, *GetInsightTypeConfigRequest) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates an InsightTypeConfig change. This will create a new revision of the
    	// config.
    	UpdateInsightTypeConfig(context.Context, *UpdateInsightTypeConfigRequest) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))
    	// Lists all available Recommenders.
    	// No IAM permissions are required.
    	ListRecommenders(context.Context, *ListRecommendersRequest) (*ListRecommendersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists available InsightTypes.
    	// No IAM permissions are required.
    	ListInsightTypes(context.Context, *ListInsightTypesRequest) (*ListInsightTypesResponse, [error](https://pkg.go.dev/builtin#error))
    }

RecommenderServer is the server API for Recommender service. All implementations should embed UnimplementedRecommenderServer for forward compatibility

## RecommenderType
    
    
    type RecommenderType struct {
    
    	// The recommender's name in format RecommenderTypes/{recommender_type}
    	// eg:  recommenderTypes/google.iam.policy.Recommender
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The type of a recommender.

### func (*RecommenderType) Descriptor 
    
    
    func (*RecommenderType) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RecommenderType.ProtoReflect.Descriptor instead.

### func (*RecommenderType) GetName 
    
    
    func (x *RecommenderType) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RecommenderType) ProtoMessage 
    
    
    func (*RecommenderType) ProtoMessage()

### func (*RecommenderType) ProtoReflect 
    
    
    func (x *RecommenderType) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RecommenderType) Reset 
    
    
    func (x *RecommenderType) Reset()

### func (*RecommenderType) String 
    
    
    func (x *RecommenderType) String() [string](https://pkg.go.dev/builtin#string)

## SecurityProjection
    
    
    type SecurityProjection struct {
    
    	// This field can be used by the recommender to define details specific to
    	// security impact.
    	Details *structpb.Struct `protobuf:"bytes,2,opt,name=details,proto3" json:"details,omitempty"`
    	// contains filtered or unexported fields
    }

Contains various ways of describing the impact on Security.

### func (*SecurityProjection) Descriptor 
    
    
    func (*SecurityProjection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SecurityProjection.ProtoReflect.Descriptor instead.

### func (*SecurityProjection) GetDetails 
    
    
    func (x *SecurityProjection) GetDetails() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*SecurityProjection) ProtoMessage 
    
    
    func (*SecurityProjection) ProtoMessage()

### func (*SecurityProjection) ProtoReflect 
    
    
    func (x *SecurityProjection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SecurityProjection) Reset 
    
    
    func (x *SecurityProjection) Reset()

### func (*SecurityProjection) String 
    
    
    func (x *SecurityProjection) String() [string](https://pkg.go.dev/builtin#string)

## SustainabilityProjection
    
    
    type SustainabilityProjection struct {
    
    	// Carbon Footprint generated in kg of CO2 equivalent.
    	// Chose kg_c_o2e so that the name renders correctly in camelCase (kgCO2e).
    	KgCO2E [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=kg_c_o2e,json=kgCO2e,proto3" json:"kg_c_o2e,omitempty"`
    	// Duration for which this sustanability applies.
    	Duration *durationpb.Duration `protobuf:"bytes,2,opt,name=duration,proto3" json:"duration,omitempty"`
    	// contains filtered or unexported fields
    }

Contains metadata about how much sustainability a recommendation can save or incur.

### func (*SustainabilityProjection) Descriptor 
    
    
    func (*SustainabilityProjection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SustainabilityProjection.ProtoReflect.Descriptor instead.

### func (*SustainabilityProjection) GetDuration 
    
    
    func (x *SustainabilityProjection) GetDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*SustainabilityProjection) GetKgCO2E 
    
    
    func (x *SustainabilityProjection) GetKgCO2E() [float64](https://pkg.go.dev/builtin#float64)

### func (*SustainabilityProjection) ProtoMessage 
    
    
    func (*SustainabilityProjection) ProtoMessage()

### func (*SustainabilityProjection) ProtoReflect 
    
    
    func (x *SustainabilityProjection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SustainabilityProjection) Reset 
    
    
    func (x *SustainabilityProjection) Reset()

### func (*SustainabilityProjection) String 
    
    
    func (x *SustainabilityProjection) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedRecommenderServer
    
    
    type UnimplementedRecommenderServer struct {
    }

UnimplementedRecommenderServer should be embedded to have forward compatible implementations.

### func (UnimplementedRecommenderServer) GetInsight 
    
    
    func (UnimplementedRecommenderServer) GetInsight([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetInsightRequest) (*Insight, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) GetInsightTypeConfig 
    
    
    func (UnimplementedRecommenderServer) GetInsightTypeConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetInsightTypeConfigRequest) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) GetRecommendation 
    
    
    func (UnimplementedRecommenderServer) GetRecommendation([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetRecommendationRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) GetRecommenderConfig 
    
    
    func (UnimplementedRecommenderServer) GetRecommenderConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetRecommenderConfigRequest) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) ListInsightTypes 
    
    
    func (UnimplementedRecommenderServer) ListInsightTypes([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListInsightTypesRequest) (*ListInsightTypesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) ListInsights 
    
    
    func (UnimplementedRecommenderServer) ListInsights([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListInsightsRequest) (*ListInsightsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) ListRecommendations 
    
    
    func (UnimplementedRecommenderServer) ListRecommendations([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListRecommendationsRequest) (*ListRecommendationsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) ListRecommenders 
    
    
    func (UnimplementedRecommenderServer) ListRecommenders([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListRecommendersRequest) (*ListRecommendersResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) MarkInsightAccepted 
    
    
    func (UnimplementedRecommenderServer) MarkInsightAccepted([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkInsightAcceptedRequest) (*Insight, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) MarkRecommendationClaimed 
    
    
    func (UnimplementedRecommenderServer) MarkRecommendationClaimed([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkRecommendationClaimedRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) MarkRecommendationFailed 
    
    
    func (UnimplementedRecommenderServer) MarkRecommendationFailed([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkRecommendationFailedRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) MarkRecommendationSucceeded 
    
    
    func (UnimplementedRecommenderServer) MarkRecommendationSucceeded([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *MarkRecommendationSucceededRequest) (*Recommendation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) UpdateInsightTypeConfig 
    
    
    func (UnimplementedRecommenderServer) UpdateInsightTypeConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateInsightTypeConfigRequest) (*InsightTypeConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecommenderServer) UpdateRecommenderConfig 
    
    
    func (UnimplementedRecommenderServer) UpdateRecommenderConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateRecommenderConfigRequest) (*RecommenderConfig, [error](https://pkg.go.dev/builtin#error))

## UnsafeRecommenderServer
    
    
    type UnsafeRecommenderServer interface {
    	// contains filtered or unexported methods
    }

UnsafeRecommenderServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to RecommenderServer will result in compilation errors.

## UpdateInsightTypeConfigRequest
    
    
    type UpdateInsightTypeConfigRequest struct {
    
    	// Required. The InsightTypeConfig to update.
    	InsightTypeConfig *InsightTypeConfig `protobuf:"bytes,1,opt,name=insight_type_config,json=insightTypeConfig,proto3" json:"insight_type_config,omitempty"`
    	// The list of fields to be updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// If true, validate the request and preview the change, but do not actually
    	// update it.
    	ValidateOnly [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=validate_only,json=validateOnly,proto3" json:"validate_only,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `UpdateInsightTypeConfig` method.

### func (*UpdateInsightTypeConfigRequest) Descriptor 
    
    
    func (*UpdateInsightTypeConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateInsightTypeConfigRequest.ProtoReflect.Descriptor instead.

### func (*UpdateInsightTypeConfigRequest) GetInsightTypeConfig 
    
    
    func (x *UpdateInsightTypeConfigRequest) GetInsightTypeConfig() *InsightTypeConfig

### func (*UpdateInsightTypeConfigRequest) GetUpdateMask 
    
    
    func (x *UpdateInsightTypeConfigRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateInsightTypeConfigRequest) GetValidateOnly 
    
    
    func (x *UpdateInsightTypeConfigRequest) GetValidateOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateInsightTypeConfigRequest) ProtoMessage 
    
    
    func (*UpdateInsightTypeConfigRequest) ProtoMessage()

### func (*UpdateInsightTypeConfigRequest) ProtoReflect 
    
    
    func (x *UpdateInsightTypeConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateInsightTypeConfigRequest) Reset 
    
    
    func (x *UpdateInsightTypeConfigRequest) Reset()

### func (*UpdateInsightTypeConfigRequest) String 
    
    
    func (x *UpdateInsightTypeConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateRecommenderConfigRequest
    
    
    type UpdateRecommenderConfigRequest struct {
    
    	// Required. The RecommenderConfig to update.
    	RecommenderConfig *RecommenderConfig `protobuf:"bytes,1,opt,name=recommender_config,json=recommenderConfig,proto3" json:"recommender_config,omitempty"`
    	// The list of fields to be updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// If true, validate the request and preview the change, but do not actually
    	// update it.
    	ValidateOnly [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=validate_only,json=validateOnly,proto3" json:"validate_only,omitempty"`
    	// contains filtered or unexported fields
    }

Request for the `UpdateRecommenderConfig` method.

### func (*UpdateRecommenderConfigRequest) Descriptor 
    
    
    func (*UpdateRecommenderConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateRecommenderConfigRequest.ProtoReflect.Descriptor instead.

### func (*UpdateRecommenderConfigRequest) GetRecommenderConfig 
    
    
    func (x *UpdateRecommenderConfigRequest) GetRecommenderConfig() *RecommenderConfig

### func (*UpdateRecommenderConfigRequest) GetUpdateMask 
    
    
    func (x *UpdateRecommenderConfigRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateRecommenderConfigRequest) GetValidateOnly 
    
    
    func (x *UpdateRecommenderConfigRequest) GetValidateOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateRecommenderConfigRequest) ProtoMessage 
    
    
    func (*UpdateRecommenderConfigRequest) ProtoMessage()

### func (*UpdateRecommenderConfigRequest) ProtoReflect 
    
    
    func (x *UpdateRecommenderConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateRecommenderConfigRequest) Reset 
    
    
    func (x *UpdateRecommenderConfigRequest) Reset()

### func (*UpdateRecommenderConfigRequest) String 
    
    
    func (x *UpdateRecommenderConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## ValueMatcher
    
    
    type ValueMatcher struct {
    
    	// Types that are valid to be assigned to MatchVariant:
    	//
    	//	*ValueMatcher_MatchesPattern
    	MatchVariant isValueMatcher_MatchVariant `protobuf_oneof:"match_variant"`
    	// contains filtered or unexported fields
    }

Contains various matching options for values for a GCP resource field.

### func (*ValueMatcher) Descriptor 
    
    
    func (*ValueMatcher) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ValueMatcher.ProtoReflect.Descriptor instead.

### func (*ValueMatcher) GetMatchVariant 
    
    
    func (x *ValueMatcher) GetMatchVariant() isValueMatcher_MatchVariant

### func (*ValueMatcher) GetMatchesPattern 
    
    
    func (x *ValueMatcher) GetMatchesPattern() [string](https://pkg.go.dev/builtin#string)

### func (*ValueMatcher) ProtoMessage 
    
    
    func (*ValueMatcher) ProtoMessage()

### func (*ValueMatcher) ProtoReflect 
    
    
    func (x *ValueMatcher) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ValueMatcher) Reset 
    
    
    func (x *ValueMatcher) Reset()

### func (*ValueMatcher) String 
    
    
    func (x *ValueMatcher) String() [string](https://pkg.go.dev/builtin#string)

## ValueMatcher_MatchesPattern
    
    
    type ValueMatcher_MatchesPattern struct {
    	// To be used for full regex matching. The regular expression is using the
    	// Google RE2 syntax (https://github.com/google/re2/wiki/Syntax), so to be
    	// used with RE2::FullMatch
    	MatchesPattern [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=matches_pattern,json=matchesPattern,proto3,oneof"`
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
