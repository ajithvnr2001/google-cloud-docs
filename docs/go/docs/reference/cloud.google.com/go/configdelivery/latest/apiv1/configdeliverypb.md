---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/configdelivery/latest/apiv1/configdeliverypb/
title: Config Delivery API v1 - Package cloud.google.com/go/configdelivery/apiv1/configdeliverypb (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:50.516495+00:00
---

# Config Delivery API v1 - Package cloud.google.com/go/configdelivery/apiv1/configdeliverypb (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/configdelivery/latest/apiv1/configdeliverypb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Config Delivery API v1 - Package cloud.google.com/go/configdelivery/apiv1/configdeliverypb (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/configdelivery/apiv1/configdeliverypb). 

##  Constants 

### ConfigDelivery_ListResourceBundles_FullMethodName, ConfigDelivery_GetResourceBundle_FullMethodName, ConfigDelivery_CreateResourceBundle_FullMethodName, ConfigDelivery_UpdateResourceBundle_FullMethodName, ConfigDelivery_DeleteResourceBundle_FullMethodName, ConfigDelivery_ListFleetPackages_FullMethodName, ConfigDelivery_GetFleetPackage_FullMethodName, ConfigDelivery_CreateFleetPackage_FullMethodName, ConfigDelivery_UpdateFleetPackage_FullMethodName, ConfigDelivery_DeleteFleetPackage_FullMethodName, ConfigDelivery_ListReleases_FullMethodName, ConfigDelivery_GetRelease_FullMethodName, ConfigDelivery_CreateRelease_FullMethodName, ConfigDelivery_UpdateRelease_FullMethodName, ConfigDelivery_DeleteRelease_FullMethodName, ConfigDelivery_ListVariants_FullMethodName, ConfigDelivery_GetVariant_FullMethodName, ConfigDelivery_CreateVariant_FullMethodName, ConfigDelivery_UpdateVariant_FullMethodName, ConfigDelivery_DeleteVariant_FullMethodName, ConfigDelivery_ListRollouts_FullMethodName, ConfigDelivery_GetRollout_FullMethodName, ConfigDelivery_SuspendRollout_FullMethodName, ConfigDelivery_ResumeRollout_FullMethodName, ConfigDelivery_AbortRollout_FullMethodName
    
    
    const (
    	ConfigDelivery_ListResourceBundles_FullMethodName  = "/google.cloud.configdelivery.v1.ConfigDelivery/ListResourceBundles"
    	ConfigDelivery_GetResourceBundle_FullMethodName    = "/google.cloud.configdelivery.v1.ConfigDelivery/GetResourceBundle"
    	ConfigDelivery_CreateResourceBundle_FullMethodName = "/google.cloud.configdelivery.v1.ConfigDelivery/CreateResourceBundle"
    	ConfigDelivery_UpdateResourceBundle_FullMethodName = "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateResourceBundle"
    	ConfigDelivery_DeleteResourceBundle_FullMethodName = "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteResourceBundle"
    	ConfigDelivery_ListFleetPackages_FullMethodName    = "/google.cloud.configdelivery.v1.ConfigDelivery/ListFleetPackages"
    	ConfigDelivery_GetFleetPackage_FullMethodName      = "/google.cloud.configdelivery.v1.ConfigDelivery/GetFleetPackage"
    	ConfigDelivery_CreateFleetPackage_FullMethodName   = "/google.cloud.configdelivery.v1.ConfigDelivery/CreateFleetPackage"
    	ConfigDelivery_UpdateFleetPackage_FullMethodName   = "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateFleetPackage"
    	ConfigDelivery_DeleteFleetPackage_FullMethodName   = "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteFleetPackage"
    	ConfigDelivery_ListReleases_FullMethodName         = "/google.cloud.configdelivery.v1.ConfigDelivery/ListReleases"
    	ConfigDelivery_GetRelease_FullMethodName           = "/google.cloud.configdelivery.v1.ConfigDelivery/GetRelease"
    	ConfigDelivery_CreateRelease_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/CreateRelease"
    	ConfigDelivery_UpdateRelease_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateRelease"
    	ConfigDelivery_DeleteRelease_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteRelease"
    	ConfigDelivery_ListVariants_FullMethodName         = "/google.cloud.configdelivery.v1.ConfigDelivery/ListVariants"
    	ConfigDelivery_GetVariant_FullMethodName           = "/google.cloud.configdelivery.v1.ConfigDelivery/GetVariant"
    	ConfigDelivery_CreateVariant_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/CreateVariant"
    	ConfigDelivery_UpdateVariant_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/UpdateVariant"
    	ConfigDelivery_DeleteVariant_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/DeleteVariant"
    	ConfigDelivery_ListRollouts_FullMethodName         = "/google.cloud.configdelivery.v1.ConfigDelivery/ListRollouts"
    	ConfigDelivery_GetRollout_FullMethodName           = "/google.cloud.configdelivery.v1.ConfigDelivery/GetRollout"
    	ConfigDelivery_SuspendRollout_FullMethodName       = "/google.cloud.configdelivery.v1.ConfigDelivery/SuspendRollout"
    	ConfigDelivery_ResumeRollout_FullMethodName        = "/google.cloud.configdelivery.v1.ConfigDelivery/ResumeRollout"
    	ConfigDelivery_AbortRollout_FullMethodName         = "/google.cloud.configdelivery.v1.ConfigDelivery/AbortRollout"
    )

## Variables 

### DeletionPropagationPolicy_name, DeletionPropagationPolicy_value
    
    
    var (
    	DeletionPropagationPolicy_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "DELETION_PROPAGATION_POLICY_UNSPECIFIED",
    		1: "FOREGROUND",
    		2: "ORPHAN",
    	}
    	DeletionPropagationPolicy_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"DELETION_PROPAGATION_POLICY_UNSPECIFIED": 0,
    		"FOREGROUND": 1,
    		"ORPHAN":     2,
    	}
    )

Enum value maps for DeletionPropagationPolicy.

### FleetPackage_State_name, FleetPackage_State_value
    
    
    var (
    	FleetPackage_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "SUSPENDED",
    	}
    	FleetPackage_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"SUSPENDED":         2,
    	}
    )

Enum value maps for FleetPackage_State.

### FleetPackageInfo_State_name, FleetPackageInfo_State_value
    
    
    var (
    	FleetPackageInfo_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "SUSPENDED",
    		3: "FAILED",
    		4: "DELETING",
    	}
    	FleetPackageInfo_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"SUSPENDED":         2,
    		"FAILED":            3,
    		"DELETING":          4,
    	}
    )

Enum value maps for FleetPackageInfo_State.

### ClusterInfo_State_name, ClusterInfo_State_value
    
    
    var (
    	ClusterInfo_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "WAITING",
    		2: "IN_PROGRESS",
    		3: "STALLED",
    		4: "COMPLETED",
    		5: "ABORTED",
    		6: "CANCELLED",
    		7: "ERROR",
    		8: "UNCHANGED",
    		9: "SKIPPED",
    	}
    	ClusterInfo_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"WAITING":           1,
    		"IN_PROGRESS":       2,
    		"STALLED":           3,
    		"COMPLETED":         4,
    		"ABORTED":           5,
    		"CANCELLED":         6,
    		"ERROR":             7,
    		"UNCHANGED":         8,
    		"SKIPPED":           9,
    	}
    )

Enum value maps for ClusterInfo_State.

### ResourceBundleDeploymentInfo_SyncState_name, ResourceBundleDeploymentInfo_SyncState_value
    
    
    var (
    	ResourceBundleDeploymentInfo_SyncState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SYNC_STATE_UNSPECIFIED",
    		1: "RECONCILING",
    		2: "STALLED",
    		3: "SYNCED",
    		4: "PENDING",
    		5: "ERROR",
    		6: "DELETION_PENDING",
    		7: "DELETING",
    		8: "DELETED",
    	}
    	ResourceBundleDeploymentInfo_SyncState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SYNC_STATE_UNSPECIFIED": 0,
    		"RECONCILING":            1,
    		"STALLED":                2,
    		"SYNCED":                 3,
    		"PENDING":                4,
    		"ERROR":                  5,
    		"DELETION_PENDING":       6,
    		"DELETING":               7,
    		"DELETED":                8,
    	}
    )

Enum value maps for ResourceBundleDeploymentInfo_SyncState.

### Release_Lifecycle_name, Release_Lifecycle_value
    
    
    var (
    	Release_Lifecycle_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "LIFECYCLE_UNSPECIFIED",
    		1: "DRAFT",
    		2: "PUBLISHED",
    	}
    	Release_Lifecycle_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"LIFECYCLE_UNSPECIFIED": 0,
    		"DRAFT":                 1,
    		"PUBLISHED":             2,
    	}
    )

Enum value maps for Release_Lifecycle.

### RolloutInfo_State_name, RolloutInfo_State_value
    
    
    var (
    	RolloutInfo_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "COMPLETED",
    		2: "SUSPENDED",
    		3: "ABORTED",
    		5: "IN_PROGRESS",
    		6: "STALLED",
    		7: "CANCELLED",
    		8: "ABORTING",
    	}
    	RolloutInfo_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"COMPLETED":         1,
    		"SUSPENDED":         2,
    		"ABORTED":           3,
    		"IN_PROGRESS":       5,
    		"STALLED":           6,
    		"CANCELLED":         7,
    		"ABORTING":          8,
    	}
    )

Enum value maps for RolloutInfo_State.

### ConfigDelivery_ServiceDesc
    
    
    var ConfigDelivery_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.configdelivery.v1.ConfigDelivery",
    	HandlerType: (*ConfigDeliveryServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListResourceBundles",
    			Handler:    _ConfigDelivery_ListResourceBundles_Handler,
    		},
    		{
    			MethodName: "GetResourceBundle",
    			Handler:    _ConfigDelivery_GetResourceBundle_Handler,
    		},
    		{
    			MethodName: "CreateResourceBundle",
    			Handler:    _ConfigDelivery_CreateResourceBundle_Handler,
    		},
    		{
    			MethodName: "UpdateResourceBundle",
    			Handler:    _ConfigDelivery_UpdateResourceBundle_Handler,
    		},
    		{
    			MethodName: "DeleteResourceBundle",
    			Handler:    _ConfigDelivery_DeleteResourceBundle_Handler,
    		},
    		{
    			MethodName: "ListFleetPackages",
    			Handler:    _ConfigDelivery_ListFleetPackages_Handler,
    		},
    		{
    			MethodName: "GetFleetPackage",
    			Handler:    _ConfigDelivery_GetFleetPackage_Handler,
    		},
    		{
    			MethodName: "CreateFleetPackage",
    			Handler:    _ConfigDelivery_CreateFleetPackage_Handler,
    		},
    		{
    			MethodName: "UpdateFleetPackage",
    			Handler:    _ConfigDelivery_UpdateFleetPackage_Handler,
    		},
    		{
    			MethodName: "DeleteFleetPackage",
    			Handler:    _ConfigDelivery_DeleteFleetPackage_Handler,
    		},
    		{
    			MethodName: "ListReleases",
    			Handler:    _ConfigDelivery_ListReleases_Handler,
    		},
    		{
    			MethodName: "GetRelease",
    			Handler:    _ConfigDelivery_GetRelease_Handler,
    		},
    		{
    			MethodName: "CreateRelease",
    			Handler:    _ConfigDelivery_CreateRelease_Handler,
    		},
    		{
    			MethodName: "UpdateRelease",
    			Handler:    _ConfigDelivery_UpdateRelease_Handler,
    		},
    		{
    			MethodName: "DeleteRelease",
    			Handler:    _ConfigDelivery_DeleteRelease_Handler,
    		},
    		{
    			MethodName: "ListVariants",
    			Handler:    _ConfigDelivery_ListVariants_Handler,
    		},
    		{
    			MethodName: "GetVariant",
    			Handler:    _ConfigDelivery_GetVariant_Handler,
    		},
    		{
    			MethodName: "CreateVariant",
    			Handler:    _ConfigDelivery_CreateVariant_Handler,
    		},
    		{
    			MethodName: "UpdateVariant",
    			Handler:    _ConfigDelivery_UpdateVariant_Handler,
    		},
    		{
    			MethodName: "DeleteVariant",
    			Handler:    _ConfigDelivery_DeleteVariant_Handler,
    		},
    		{
    			MethodName: "ListRollouts",
    			Handler:    _ConfigDelivery_ListRollouts_Handler,
    		},
    		{
    			MethodName: "GetRollout",
    			Handler:    _ConfigDelivery_GetRollout_Handler,
    		},
    		{
    			MethodName: "SuspendRollout",
    			Handler:    _ConfigDelivery_SuspendRollout_Handler,
    		},
    		{
    			MethodName: "ResumeRollout",
    			Handler:    _ConfigDelivery_ResumeRollout_Handler,
    		},
    		{
    			MethodName: "AbortRollout",
    			Handler:    _ConfigDelivery_AbortRollout_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/configdelivery/v1/config_delivery.proto",
    }

ConfigDelivery_ServiceDesc is the grpc.ServiceDesc for ConfigDelivery service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_configdelivery_v1_config_delivery_proto
    
    
    var File_google_cloud_configdelivery_v1_config_delivery_proto protoreflect.FileDescriptor

## Functions 

### func RegisterConfigDeliveryServer 
    
    
    func RegisterConfigDeliveryServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv ConfigDeliveryServer)

## AbortRolloutRequest
    
    
    type AbortRolloutRequest struct {
    
    	// Required. Name of the Rollout.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Reason for aborting.
    	Reason [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
    	// contains filtered or unexported fields
    }

Message for aborting a rollout.

### func (*AbortRolloutRequest) Descriptor 
    
    
    func (*AbortRolloutRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AbortRolloutRequest.ProtoReflect.Descriptor instead.

### func (*AbortRolloutRequest) GetName 
    
    
    func (x *AbortRolloutRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AbortRolloutRequest) GetReason 
    
    
    func (x *AbortRolloutRequest) GetReason() [string](https://pkg.go.dev/builtin#string)

### func (*AbortRolloutRequest) ProtoMessage 
    
    
    func (*AbortRolloutRequest) ProtoMessage()

### func (*AbortRolloutRequest) ProtoReflect 
    
    
    func (x *AbortRolloutRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AbortRolloutRequest) Reset 
    
    
    func (x *AbortRolloutRequest) Reset()

### func (*AbortRolloutRequest) String 
    
    
    func (x *AbortRolloutRequest) String() [string](https://pkg.go.dev/builtin#string)

## AllAtOnceStrategy
    
    
    type AllAtOnceStrategy struct {
    	// contains filtered or unexported fields
    }

AllAtOnceStrategy causes all clusters to be updated concurrently.

### func (*AllAtOnceStrategy) Descriptor 
    
    
    func (*AllAtOnceStrategy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AllAtOnceStrategy.ProtoReflect.Descriptor instead.

### func (*AllAtOnceStrategy) ProtoMessage 
    
    
    func (*AllAtOnceStrategy) ProtoMessage()

### func (*AllAtOnceStrategy) ProtoReflect 
    
    
    func (x *AllAtOnceStrategy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AllAtOnceStrategy) Reset 
    
    
    func (x *AllAtOnceStrategy) Reset()

### func (*AllAtOnceStrategy) String 
    
    
    func (x *AllAtOnceStrategy) String() [string](https://pkg.go.dev/builtin#string)

## AllAtOnceStrategyInfo
    
    
    type AllAtOnceStrategyInfo struct {
    
    	// Unordered list. resource bundle's deployment status for all targeted
    	// clusters.
    	Clusters []*ClusterInfo `protobuf:"bytes,1,rep,name=clusters,proto3" json:"clusters,omitempty"`
    	// contains filtered or unexported fields
    }

AllAtOnceStrategyInfo represents the status of execution of AllAtOnce rollout strategy.

### func (*AllAtOnceStrategyInfo) Descriptor 
    
    
    func (*AllAtOnceStrategyInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AllAtOnceStrategyInfo.ProtoReflect.Descriptor instead.

### func (*AllAtOnceStrategyInfo) GetClusters 
    
    
    func (x *AllAtOnceStrategyInfo) GetClusters() []*ClusterInfo

### func (*AllAtOnceStrategyInfo) ProtoMessage 
    
    
    func (*AllAtOnceStrategyInfo) ProtoMessage()

### func (*AllAtOnceStrategyInfo) ProtoReflect 
    
    
    func (x *AllAtOnceStrategyInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AllAtOnceStrategyInfo) Reset 
    
    
    func (x *AllAtOnceStrategyInfo) Reset()

### func (*AllAtOnceStrategyInfo) String 
    
    
    func (x *AllAtOnceStrategyInfo) String() [string](https://pkg.go.dev/builtin#string)

## ClusterInfo
    
    
    type ClusterInfo struct {
    
    	// Output only. gkehub membership of target cluster
    	Membership [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=membership,proto3" json:"membership,omitempty"`
    	// Output only. Desired state for the resource bundle.
    	Desired *ResourceBundleDeploymentInfo `protobuf:"bytes,2,opt,name=desired,proto3" json:"desired,omitempty"`
    	// Output only. Initial state of the resource bundle prior to the deployment.
    	Initial *ResourceBundleDeploymentInfo `protobuf:"bytes,3,opt,name=initial,proto3" json:"initial,omitempty"`
    	// Output only. Current state of the resource bundle.
    	Current *ResourceBundleDeploymentInfo `protobuf:"bytes,4,opt,name=current,proto3" json:"current,omitempty"`
    	// Output only. State of the rollout for the cluster.
    	State ClusterInfo_State `protobuf:"varint,5,opt,name=state,proto3,enum=google.cloud.configdelivery.v1.ClusterInfo_State" json:"state,omitempty"`
    	// Output only. Unordered list. Messages convey additional information related
    	// to the deployment.
    	Messages [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,rep,name=messages,proto3" json:"messages,omitempty"`
    	// Output only. Timestamp when reconciliation starts.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,7,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// Output only. Timestamp when reconciliation ends.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// contains filtered or unexported fields
    }

ClusterInfo represents status of a resource bundle rollout for a cluster.

### func (*ClusterInfo) Descriptor 
    
    
    func (*ClusterInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ClusterInfo.ProtoReflect.Descriptor instead.

### func (*ClusterInfo) GetCurrent 
    
    
    func (x *ClusterInfo) GetCurrent() *ResourceBundleDeploymentInfo

### func (*ClusterInfo) GetDesired 
    
    
    func (x *ClusterInfo) GetDesired() *ResourceBundleDeploymentInfo

### func (*ClusterInfo) GetEndTime 
    
    
    func (x *ClusterInfo) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ClusterInfo) GetInitial 
    
    
    func (x *ClusterInfo) GetInitial() *ResourceBundleDeploymentInfo

### func (*ClusterInfo) GetMembership 
    
    
    func (x *ClusterInfo) GetMembership() [string](https://pkg.go.dev/builtin#string)

### func (*ClusterInfo) GetMessages 
    
    
    func (x *ClusterInfo) GetMessages() [][string](https://pkg.go.dev/builtin#string)

### func (*ClusterInfo) GetStartTime 
    
    
    func (x *ClusterInfo) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ClusterInfo) GetState 
    
    
    func (x *ClusterInfo) GetState() ClusterInfo_State

### func (*ClusterInfo) ProtoMessage 
    
    
    func (*ClusterInfo) ProtoMessage()

### func (*ClusterInfo) ProtoReflect 
    
    
    func (x *ClusterInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ClusterInfo) Reset 
    
    
    func (x *ClusterInfo) Reset()

### func (*ClusterInfo) String 
    
    
    func (x *ClusterInfo) String() [string](https://pkg.go.dev/builtin#string)

## ClusterInfo_State
    
    
    type ClusterInfo_State [int32](https://pkg.go.dev/builtin#int32)

State of the rollout for the cluster.

### ClusterInfo_STATE_UNSPECIFIED, ClusterInfo_WAITING, ClusterInfo_IN_PROGRESS, ClusterInfo_STALLED, ClusterInfo_COMPLETED, ClusterInfo_ABORTED, ClusterInfo_CANCELLED, ClusterInfo_ERROR, ClusterInfo_UNCHANGED, ClusterInfo_SKIPPED
    
    
    const (
    	// Unspecified state.
    	ClusterInfo_STATE_UNSPECIFIED ClusterInfo_State = 0
    	// Waiting state.
    	ClusterInfo_WAITING ClusterInfo_State = 1
    	// In progress state.
    	ClusterInfo_IN_PROGRESS ClusterInfo_State = 2
    	// Stalled state.
    	ClusterInfo_STALLED ClusterInfo_State = 3
    	// Completed state.
    	ClusterInfo_COMPLETED ClusterInfo_State = 4
    	// Aborted state.
    	ClusterInfo_ABORTED ClusterInfo_State = 5
    	// Cancelled state.
    	ClusterInfo_CANCELLED ClusterInfo_State = 6
    	// Error state.
    	ClusterInfo_ERROR ClusterInfo_State = 7
    	// Unchanged state.
    	ClusterInfo_UNCHANGED ClusterInfo_State = 8
    	// Skipped state.
    	ClusterInfo_SKIPPED ClusterInfo_State = 9
    )

### func (ClusterInfo_State) Descriptor 
    
    
    func (ClusterInfo_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ClusterInfo_State) Enum 
    
    
    func (x ClusterInfo_State) Enum() *ClusterInfo_State

### func (ClusterInfo_State) EnumDescriptor 
    
    
    func (ClusterInfo_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ClusterInfo_State.Descriptor instead.

### func (ClusterInfo_State) Number 
    
    
    func (x ClusterInfo_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ClusterInfo_State) String 
    
    
    func (x ClusterInfo_State) String() [string](https://pkg.go.dev/builtin#string)

### func (ClusterInfo_State) Type 
    
    
    func (ClusterInfo_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ConfigDeliveryClient
    
    
    type ConfigDeliveryClient interface {
    	// Lists ResourceBundles in a given project and location.
    	ListResourceBundles(ctx context.Context, in *ListResourceBundlesRequest, opts ...grpc.CallOption) (*ListResourceBundlesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ResourceBundle.
    	GetResourceBundle(ctx context.Context, in *GetResourceBundleRequest, opts ...grpc.CallOption) (*ResourceBundle, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new ResourceBundle in a given project and location.
    	CreateResourceBundle(ctx context.Context, in *CreateResourceBundleRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single ResourceBundle.
    	UpdateResourceBundle(ctx context.Context, in *UpdateResourceBundleRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single ResourceBundle.
    	DeleteResourceBundle(ctx context.Context, in *DeleteResourceBundleRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists FleetPackages in a given project and location.
    	ListFleetPackages(ctx context.Context, in *ListFleetPackagesRequest, opts ...grpc.CallOption) (*ListFleetPackagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single FleetPackage.
    	GetFleetPackage(ctx context.Context, in *GetFleetPackageRequest, opts ...grpc.CallOption) (*FleetPackage, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new FleetPackage in a given project and location.
    	CreateFleetPackage(ctx context.Context, in *CreateFleetPackageRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single FleetPackage.
    	UpdateFleetPackage(ctx context.Context, in *UpdateFleetPackageRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single FleetPackage.
    	DeleteFleetPackage(ctx context.Context, in *DeleteFleetPackageRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Releases in a given project and location.
    	ListReleases(ctx context.Context, in *ListReleasesRequest, opts ...grpc.CallOption) (*ListReleasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Release.
    	GetRelease(ctx context.Context, in *GetReleaseRequest, opts ...grpc.CallOption) (*Release, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new Release in a given project, location and resource bundle.
    	CreateRelease(ctx context.Context, in *CreateReleaseRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single Release.
    	UpdateRelease(ctx context.Context, in *UpdateReleaseRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single Release.
    	DeleteRelease(ctx context.Context, in *DeleteReleaseRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Variants in a given project and location.
    	ListVariants(ctx context.Context, in *ListVariantsRequest, opts ...grpc.CallOption) (*ListVariantsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Variant.
    	GetVariant(ctx context.Context, in *GetVariantRequest, opts ...grpc.CallOption) (*Variant, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new Variant in a given project, location, resource bundle, and
    	// release.
    	CreateVariant(ctx context.Context, in *CreateVariantRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single Variant.
    	UpdateVariant(ctx context.Context, in *UpdateVariantRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single Variant.
    	DeleteVariant(ctx context.Context, in *DeleteVariantRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Rollouts in a given project, location, and Fleet Package.
    	ListRollouts(ctx context.Context, in *ListRolloutsRequest, opts ...grpc.CallOption) (*ListRolloutsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Rollout.
    	GetRollout(ctx context.Context, in *GetRolloutRequest, opts ...grpc.CallOption) (*Rollout, [error](https://pkg.go.dev/builtin#error))
    	// Suspend a Rollout.
    	SuspendRollout(ctx context.Context, in *SuspendRolloutRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Resume a Rollout.
    	ResumeRollout(ctx context.Context, in *ResumeRolloutRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Abort a Rollout.
    	AbortRollout(ctx context.Context, in *AbortRolloutRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

ConfigDeliveryClient is the client API for ConfigDelivery service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewConfigDeliveryClient 
    
    
    func NewConfigDeliveryClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) ConfigDeliveryClient

## ConfigDeliveryServer
    
    
    type ConfigDeliveryServer interface {
    	// Lists ResourceBundles in a given project and location.
    	ListResourceBundles(context.Context, *ListResourceBundlesRequest) (*ListResourceBundlesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ResourceBundle.
    	GetResourceBundle(context.Context, *GetResourceBundleRequest) (*ResourceBundle, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new ResourceBundle in a given project and location.
    	CreateResourceBundle(context.Context, *CreateResourceBundleRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single ResourceBundle.
    	UpdateResourceBundle(context.Context, *UpdateResourceBundleRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single ResourceBundle.
    	DeleteResourceBundle(context.Context, *DeleteResourceBundleRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists FleetPackages in a given project and location.
    	ListFleetPackages(context.Context, *ListFleetPackagesRequest) (*ListFleetPackagesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single FleetPackage.
    	GetFleetPackage(context.Context, *GetFleetPackageRequest) (*FleetPackage, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new FleetPackage in a given project and location.
    	CreateFleetPackage(context.Context, *CreateFleetPackageRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single FleetPackage.
    	UpdateFleetPackage(context.Context, *UpdateFleetPackageRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single FleetPackage.
    	DeleteFleetPackage(context.Context, *DeleteFleetPackageRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Releases in a given project and location.
    	ListReleases(context.Context, *ListReleasesRequest) (*ListReleasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Release.
    	GetRelease(context.Context, *GetReleaseRequest) (*Release, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new Release in a given project, location and resource bundle.
    	CreateRelease(context.Context, *CreateReleaseRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single Release.
    	UpdateRelease(context.Context, *UpdateReleaseRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single Release.
    	DeleteRelease(context.Context, *DeleteReleaseRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Variants in a given project and location.
    	ListVariants(context.Context, *ListVariantsRequest) (*ListVariantsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Variant.
    	GetVariant(context.Context, *GetVariantRequest) (*Variant, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new Variant in a given project, location, resource bundle, and
    	// release.
    	CreateVariant(context.Context, *CreateVariantRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single Variant.
    	UpdateVariant(context.Context, *UpdateVariantRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single Variant.
    	DeleteVariant(context.Context, *DeleteVariantRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists Rollouts in a given project, location, and Fleet Package.
    	ListRollouts(context.Context, *ListRolloutsRequest) (*ListRolloutsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Rollout.
    	GetRollout(context.Context, *GetRolloutRequest) (*Rollout, [error](https://pkg.go.dev/builtin#error))
    	// Suspend a Rollout.
    	SuspendRollout(context.Context, *SuspendRolloutRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Resume a Rollout.
    	ResumeRollout(context.Context, *ResumeRolloutRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Abort a Rollout.
    	AbortRollout(context.Context, *AbortRolloutRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

ConfigDeliveryServer is the server API for ConfigDelivery service. All implementations should embed UnimplementedConfigDeliveryServer for forward compatibility

## CreateFleetPackageRequest
    
    
    type CreateFleetPackageRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Id of the requesting object
    	// If auto-generating Id server-side, remove this field and
    	// fleet_package_id from the method_signature of Create RPC
    	FleetPackageId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=fleet_package_id,json=fleetPackageId,proto3" json:"fleet_package_id,omitempty"`
    	// Required. The resource being created.
    	FleetPackage *FleetPackage `protobuf:"bytes,3,opt,name=fleet_package,json=fleetPackage,proto3" json:"fleet_package,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a FleetPackage

### func (*CreateFleetPackageRequest) Descriptor 
    
    
    func (*CreateFleetPackageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateFleetPackageRequest.ProtoReflect.Descriptor instead.

### func (*CreateFleetPackageRequest) GetFleetPackage 
    
    
    func (x *CreateFleetPackageRequest) GetFleetPackage() *FleetPackage

### func (*CreateFleetPackageRequest) GetFleetPackageId 
    
    
    func (x *CreateFleetPackageRequest) GetFleetPackageId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateFleetPackageRequest) GetParent 
    
    
    func (x *CreateFleetPackageRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateFleetPackageRequest) GetRequestId 
    
    
    func (x *CreateFleetPackageRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateFleetPackageRequest) ProtoMessage 
    
    
    func (*CreateFleetPackageRequest) ProtoMessage()

### func (*CreateFleetPackageRequest) ProtoReflect 
    
    
    func (x *CreateFleetPackageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateFleetPackageRequest) Reset 
    
    
    func (x *CreateFleetPackageRequest) Reset()

### func (*CreateFleetPackageRequest) String 
    
    
    func (x *CreateFleetPackageRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateReleaseRequest
    
    
    type CreateReleaseRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Id of the requesting object
    	// If auto-generating Id server-side, remove this field and
    	// release_id from the method_signature of Create RPC
    	ReleaseId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=release_id,json=releaseId,proto3" json:"release_id,omitempty"`
    	// Required. The resource being created
    	Release *Release `protobuf:"bytes,3,opt,name=release,proto3" json:"release,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a Release

### func (*CreateReleaseRequest) Descriptor 
    
    
    func (*CreateReleaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateReleaseRequest.ProtoReflect.Descriptor instead.

### func (*CreateReleaseRequest) GetParent 
    
    
    func (x *CreateReleaseRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReleaseRequest) GetRelease 
    
    
    func (x *CreateReleaseRequest) GetRelease() *Release

### func (*CreateReleaseRequest) GetReleaseId 
    
    
    func (x *CreateReleaseRequest) GetReleaseId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReleaseRequest) GetRequestId 
    
    
    func (x *CreateReleaseRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReleaseRequest) ProtoMessage 
    
    
    func (*CreateReleaseRequest) ProtoMessage()

### func (*CreateReleaseRequest) ProtoReflect 
    
    
    func (x *CreateReleaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateReleaseRequest) Reset 
    
    
    func (x *CreateReleaseRequest) Reset()

### func (*CreateReleaseRequest) String 
    
    
    func (x *CreateReleaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateResourceBundleRequest
    
    
    type CreateResourceBundleRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Id of the requesting object
    	// If auto-generating Id server-side, remove this field and
    	// resource_bundle_id from the method_signature of Create RPC
    	ResourceBundleId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=resource_bundle_id,json=resourceBundleId,proto3" json:"resource_bundle_id,omitempty"`
    	// Required. The resource being created
    	ResourceBundle *ResourceBundle `protobuf:"bytes,3,opt,name=resource_bundle,json=resourceBundle,proto3" json:"resource_bundle,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a ResourceBundle.

### func (*CreateResourceBundleRequest) Descriptor 
    
    
    func (*CreateResourceBundleRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateResourceBundleRequest.ProtoReflect.Descriptor instead.

### func (*CreateResourceBundleRequest) GetParent 
    
    
    func (x *CreateResourceBundleRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateResourceBundleRequest) GetRequestId 
    
    
    func (x *CreateResourceBundleRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateResourceBundleRequest) GetResourceBundle 
    
    
    func (x *CreateResourceBundleRequest) GetResourceBundle() *ResourceBundle

### func (*CreateResourceBundleRequest) GetResourceBundleId 
    
    
    func (x *CreateResourceBundleRequest) GetResourceBundleId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateResourceBundleRequest) ProtoMessage 
    
    
    func (*CreateResourceBundleRequest) ProtoMessage()

### func (*CreateResourceBundleRequest) ProtoReflect 
    
    
    func (x *CreateResourceBundleRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateResourceBundleRequest) Reset 
    
    
    func (x *CreateResourceBundleRequest) Reset()

### func (*CreateResourceBundleRequest) String 
    
    
    func (x *CreateResourceBundleRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateVariantRequest
    
    
    type CreateVariantRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Id of the requesting object
    	VariantId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=variant_id,json=variantId,proto3" json:"variant_id,omitempty"`
    	// Required. The resource being created
    	Variant *Variant `protobuf:"bytes,3,opt,name=variant,proto3" json:"variant,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a Variant

### func (*CreateVariantRequest) Descriptor 
    
    
    func (*CreateVariantRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateVariantRequest.ProtoReflect.Descriptor instead.

### func (*CreateVariantRequest) GetParent 
    
    
    func (x *CreateVariantRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateVariantRequest) GetRequestId 
    
    
    func (x *CreateVariantRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateVariantRequest) GetVariant 
    
    
    func (x *CreateVariantRequest) GetVariant() *Variant

### func (*CreateVariantRequest) GetVariantId 
    
    
    func (x *CreateVariantRequest) GetVariantId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateVariantRequest) ProtoMessage 
    
    
    func (*CreateVariantRequest) ProtoMessage()

### func (*CreateVariantRequest) ProtoReflect 
    
    
    func (x *CreateVariantRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateVariantRequest) Reset 
    
    
    func (x *CreateVariantRequest) Reset()

### func (*CreateVariantRequest) String 
    
    
    func (x *CreateVariantRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteFleetPackageRequest
    
    
    type DeleteFleetPackageRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set to true, any rollouts for this FleetPackage will also be
    	// deleted. (Otherwise, the request will only work if the fleet package has no
    	// rollouts.)
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// Optional. If set to true, then deleting an already deleted or non existing
    	// FleetPackage will succeed.
    	AllowMissing [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=allow_missing,json=allowMissing,proto3" json:"allow_missing,omitempty"`
    	// contains filtered or unexported fields
    }

Message for deleting a FleetPackage

### func (*DeleteFleetPackageRequest) Descriptor 
    
    
    func (*DeleteFleetPackageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteFleetPackageRequest.ProtoReflect.Descriptor instead.

### func (*DeleteFleetPackageRequest) GetAllowMissing 
    
    
    func (x *DeleteFleetPackageRequest) GetAllowMissing() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteFleetPackageRequest) GetForce 
    
    
    func (x *DeleteFleetPackageRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteFleetPackageRequest) GetName 
    
    
    func (x *DeleteFleetPackageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteFleetPackageRequest) GetRequestId 
    
    
    func (x *DeleteFleetPackageRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteFleetPackageRequest) ProtoMessage 
    
    
    func (*DeleteFleetPackageRequest) ProtoMessage()

### func (*DeleteFleetPackageRequest) ProtoReflect 
    
    
    func (x *DeleteFleetPackageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteFleetPackageRequest) Reset 
    
    
    func (x *DeleteFleetPackageRequest) Reset()

### func (*DeleteFleetPackageRequest) String 
    
    
    func (x *DeleteFleetPackageRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteReleaseRequest
    
    
    type DeleteReleaseRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set to true, any variants of this release will also be
    	// deleted. (Otherwise, the request will only work if the release has no
    	// variants.)
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

Message for deleting a Release

### func (*DeleteReleaseRequest) Descriptor 
    
    
    func (*DeleteReleaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteReleaseRequest.ProtoReflect.Descriptor instead.

### func (*DeleteReleaseRequest) GetForce 
    
    
    func (x *DeleteReleaseRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteReleaseRequest) GetName 
    
    
    func (x *DeleteReleaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReleaseRequest) GetRequestId 
    
    
    func (x *DeleteReleaseRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReleaseRequest) ProtoMessage 
    
    
    func (*DeleteReleaseRequest) ProtoMessage()

### func (*DeleteReleaseRequest) ProtoReflect 
    
    
    func (x *DeleteReleaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteReleaseRequest) Reset 
    
    
    func (x *DeleteReleaseRequest) Reset()

### func (*DeleteReleaseRequest) String 
    
    
    func (x *DeleteReleaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteResourceBundleRequest
    
    
    type DeleteResourceBundleRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set to true, any releases of this resource bundle will also be
    	// deleted. (Otherwise, the request will only work if the resource bundle has
    	// no releases.)
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

Message for deleting a ResourceBundle

### func (*DeleteResourceBundleRequest) Descriptor 
    
    
    func (*DeleteResourceBundleRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteResourceBundleRequest.ProtoReflect.Descriptor instead.

### func (*DeleteResourceBundleRequest) GetForce 
    
    
    func (x *DeleteResourceBundleRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteResourceBundleRequest) GetName 
    
    
    func (x *DeleteResourceBundleRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteResourceBundleRequest) GetRequestId 
    
    
    func (x *DeleteResourceBundleRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteResourceBundleRequest) ProtoMessage 
    
    
    func (*DeleteResourceBundleRequest) ProtoMessage()

### func (*DeleteResourceBundleRequest) ProtoReflect 
    
    
    func (x *DeleteResourceBundleRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteResourceBundleRequest) Reset 
    
    
    func (x *DeleteResourceBundleRequest) Reset()

### func (*DeleteResourceBundleRequest) String 
    
    
    func (x *DeleteResourceBundleRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteVariantRequest
    
    
    type DeleteVariantRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for deleting a Variant

### func (*DeleteVariantRequest) Descriptor 
    
    
    func (*DeleteVariantRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteVariantRequest.ProtoReflect.Descriptor instead.

### func (*DeleteVariantRequest) GetName 
    
    
    func (x *DeleteVariantRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteVariantRequest) GetRequestId 
    
    
    func (x *DeleteVariantRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteVariantRequest) ProtoMessage 
    
    
    func (*DeleteVariantRequest) ProtoMessage()

### func (*DeleteVariantRequest) ProtoReflect 
    
    
    func (x *DeleteVariantRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteVariantRequest) Reset 
    
    
    func (x *DeleteVariantRequest) Reset()

### func (*DeleteVariantRequest) String 
    
    
    func (x *DeleteVariantRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeletionPropagationPolicy
    
    
    type DeletionPropagationPolicy [int32](https://pkg.go.dev/builtin#int32)

Deletion Propagation Policy determines what happens to the underlying Kubernetes resources on a cluster when the `FleetPackage` managing those resources no longer targets the cluster or is deleted.

### DeletionPropagationPolicy_DELETION_PROPAGATION_POLICY_UNSPECIFIED, DeletionPropagationPolicy_FOREGROUND, DeletionPropagationPolicy_ORPHAN
    
    
    const (
    	// Unspecified deletion propagation policy. Defaults to FOREGROUND.
    	DeletionPropagationPolicy_DELETION_PROPAGATION_POLICY_UNSPECIFIED DeletionPropagationPolicy = 0
    	// Foreground deletion propagation policy. Any resources synced to the cluster
    	// will be deleted.
    	DeletionPropagationPolicy_FOREGROUND DeletionPropagationPolicy = 1
    	// Orphan deletion propagation policy. Any resources synced to the cluster
    	// will be abandoned.
    	DeletionPropagationPolicy_ORPHAN DeletionPropagationPolicy = 2
    )

### func (DeletionPropagationPolicy) Descriptor 
    
    
    func (DeletionPropagationPolicy) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (DeletionPropagationPolicy) Enum 
    
    
    func (x DeletionPropagationPolicy) Enum() *DeletionPropagationPolicy

### func (DeletionPropagationPolicy) EnumDescriptor 
    
    
    func (DeletionPropagationPolicy) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletionPropagationPolicy.Descriptor instead.

### func (DeletionPropagationPolicy) Number 
    
    
    func (x DeletionPropagationPolicy) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (DeletionPropagationPolicy) String 
    
    
    func (x DeletionPropagationPolicy) String() [string](https://pkg.go.dev/builtin#string)

### func (DeletionPropagationPolicy) Type 
    
    
    func (DeletionPropagationPolicy) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Fleet
    
    
    type Fleet struct {
    
    	// Required. The host project for the GKE fleet. Format is
    	// `projects/{project}`.
    	Project [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=project,proto3" json:"project,omitempty"`
    	// Optional. selector allows targeting a subset of fleet members using their
    	// labels.
    	Selector *Fleet_LabelSelector `protobuf:"bytes,2,opt,name=selector,proto3" json:"selector,omitempty"`
    	// contains filtered or unexported fields
    }

The fleet where the `FleetPackage` should be deployed.

### func (*Fleet) Descriptor 
    
    
    func (*Fleet) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Fleet.ProtoReflect.Descriptor instead.

### func (*Fleet) GetProject 
    
    
    func (x *Fleet) GetProject() [string](https://pkg.go.dev/builtin#string)

### func (*Fleet) GetSelector 
    
    
    func (x *Fleet) GetSelector() *Fleet_LabelSelector

### func (*Fleet) ProtoMessage 
    
    
    func (*Fleet) ProtoMessage()

### func (*Fleet) ProtoReflect 
    
    
    func (x *Fleet) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Fleet) Reset 
    
    
    func (x *Fleet) Reset()

### func (*Fleet) String 
    
    
    func (x *Fleet) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage
    
    
    type FleetPackage struct {
    
    	// Identifier. Name of the `FleetPackage`. Format is
    	// `projects/{project}/locations/{location}/fleetPackages/{fleetPackage}`.
    	// The `fleetPackage` component must match
    	// `[a-z][a-z0-9\-]{0,62}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Time at which the `FleetPackage` was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Most recent time at which the `FleetPackage` was updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Optional. Labels are attributes that can be set and used by both the
    	// user and by Config Delivery. Labels must meet the following constraints:
    	//
    	// * Keys and values can contain only lowercase letters, numeric characters,
    	// underscores, and dashes.
    	// * All characters must use UTF-8 encoding, and international characters are
    	// allowed.
    	// * Keys must start with a lowercase letter or international character.
    	// * Each resource is limited to a maximum of 64 labels.
    	//
    	// Both keys and values are additionally constrained to be <= 128="" bytes.="" labels="">[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Information specifying the source of kubernetes configuration to
    	// deploy.
    	ResourceBundleSelector *FleetPackage_ResourceBundleSelector `protobuf:"bytes,5,opt,name=resource_bundle_selector,json=resourceBundleSelector,proto3" json:"resource_bundle_selector,omitempty"`
    	// Optional. Configuration to select target clusters to deploy kubernetes
    	// configuration to.
    	Target *FleetPackage_Target `protobuf:"bytes,9,opt,name=target,proto3" json:"target,omitempty"`
    	// Optional. The strategy to use to deploy kubernetes configuration to
    	// clusters.
    	RolloutStrategy *RolloutStrategy `protobuf:"bytes,10,opt,name=rollout_strategy,json=rolloutStrategy,proto3" json:"rollout_strategy,omitempty"`
    	// Required. Information specifying how to map a `ResourceBundle` variant to a
    	// target cluster.
    	VariantSelector *FleetPackage_VariantSelector `protobuf:"bytes,11,opt,name=variant_selector,json=variantSelector,proto3" json:"variant_selector,omitempty"`
    	// Output only. Information containing the rollout status of the
    	// `FleetPackage` across all the target clusters.
    	Info *FleetPackageInfo `protobuf:"bytes,13,opt,name=info,proto3" json:"info,omitempty"`
    	// Optional. Information around how to handle kubernetes resources at the
    	// target clusters when the `FleetPackage` is deleted.
    	DeletionPropagationPolicy DeletionPropagationPolicy `protobuf:"varint,15,opt,name=deletion_propagation_policy,json=deletionPropagationPolicy,proto3,enum=google.cloud.configdelivery.v1.DeletionPropagationPolicy" json:"deletion_propagation_policy,omitempty"`
    	// Optional. The desired state of the fleet package.
    	State FleetPackage_State `protobuf:"varint,16,opt,name=state,proto3,enum=google.cloud.configdelivery.v1.FleetPackage_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

A `FleetPackage` resource in the Config Delivery API.

A `FleetPackage` defines a package through which kubernetes configuration is deployed to a fleet of kubernetes clusters.

### func (*FleetPackage) Descriptor 
    
    
    func (*FleetPackage) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage.ProtoReflect.Descriptor instead.

### func (*FleetPackage) GetCreateTime 
    
    
    func (x *FleetPackage) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*FleetPackage) GetDeletionPropagationPolicy 
    
    
    func (x *FleetPackage) GetDeletionPropagationPolicy() DeletionPropagationPolicy

### func (*FleetPackage) GetInfo 
    
    
    func (x *FleetPackage) GetInfo() *FleetPackageInfo

### func (*FleetPackage) GetLabels 
    
    
    func (x *FleetPackage) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage) GetName 
    
    
    func (x *FleetPackage) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage) GetResourceBundleSelector 
    
    
    func (x *FleetPackage) GetResourceBundleSelector() *FleetPackage_ResourceBundleSelector

### func (*FleetPackage) GetRolloutStrategy 
    
    
    func (x *FleetPackage) GetRolloutStrategy() *RolloutStrategy

### func (*FleetPackage) GetState 
    
    
    func (x *FleetPackage) GetState() FleetPackage_State

### func (*FleetPackage) GetTarget 
    
    
    func (x *FleetPackage) GetTarget() *FleetPackage_Target

### func (*FleetPackage) GetUpdateTime 
    
    
    func (x *FleetPackage) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*FleetPackage) GetVariantSelector 
    
    
    func (x *FleetPackage) GetVariantSelector() *FleetPackage_VariantSelector

### func (*FleetPackage) ProtoMessage 
    
    
    func (*FleetPackage) ProtoMessage()

### func (*FleetPackage) ProtoReflect 
    
    
    func (x *FleetPackage) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage) Reset 
    
    
    func (x *FleetPackage) Reset()

### func (*FleetPackage) String 
    
    
    func (x *FleetPackage) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackageError
    
    
    type FleetPackageError struct {
    
    	// Optional. A description of the error.
    	ErrorMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=error_message,json=errorMessage,proto3" json:"error_message,omitempty"`
    	// contains filtered or unexported fields
    }

Information representing an error encountered during rolling out configurations.

### func (*FleetPackageError) Descriptor 
    
    
    func (*FleetPackageError) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackageError.ProtoReflect.Descriptor instead.

### func (*FleetPackageError) GetErrorMessage 
    
    
    func (x *FleetPackageError) GetErrorMessage() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackageError) ProtoMessage 
    
    
    func (*FleetPackageError) ProtoMessage()

### func (*FleetPackageError) ProtoReflect 
    
    
    func (x *FleetPackageError) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackageError) Reset 
    
    
    func (x *FleetPackageError) Reset()

### func (*FleetPackageError) String 
    
    
    func (x *FleetPackageError) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackageInfo
    
    
    type FleetPackageInfo struct {
    
    	// Optional. The active rollout, if any. Format is
    	// `projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/{rollout}`.
    	ActiveRollout [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=active_rollout,json=activeRollout,proto3" json:"active_rollout,omitempty"`
    	// Optional. The last completed rollout, if any. Format is
    	// `projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/{rollout}`.
    	LastCompletedRollout [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=last_completed_rollout,json=lastCompletedRollout,proto3" json:"last_completed_rollout,omitempty"`
    	// Optional. Output only. The current state of the `FleetPackage`.
    	State FleetPackageInfo_State `protobuf:"varint,3,opt,name=state,proto3,enum=google.cloud.configdelivery.v1.FleetPackageInfo_State" json:"state,omitempty"`
    	// Optional. Output only. Errors encountered during configuration deployment
    	// (if any).
    	Errors []*FleetPackageError `protobuf:"bytes,6,rep,name=errors,proto3" json:"errors,omitempty"`
    	// contains filtered or unexported fields
    }

FleetPackageInfo represents the status of the `FleetPackage` across all the target clusters.

### func (*FleetPackageInfo) Descriptor 
    
    
    func (*FleetPackageInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackageInfo.ProtoReflect.Descriptor instead.

### func (*FleetPackageInfo) GetActiveRollout 
    
    
    func (x *FleetPackageInfo) GetActiveRollout() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackageInfo) GetErrors 
    
    
    func (x *FleetPackageInfo) GetErrors() []*FleetPackageError

### func (*FleetPackageInfo) GetLastCompletedRollout 
    
    
    func (x *FleetPackageInfo) GetLastCompletedRollout() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackageInfo) GetState 
    
    
    func (x *FleetPackageInfo) GetState() FleetPackageInfo_State

### func (*FleetPackageInfo) ProtoMessage 
    
    
    func (*FleetPackageInfo) ProtoMessage()

### func (*FleetPackageInfo) ProtoReflect 
    
    
    func (x *FleetPackageInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackageInfo) Reset 
    
    
    func (x *FleetPackageInfo) Reset()

### func (*FleetPackageInfo) String 
    
    
    func (x *FleetPackageInfo) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackageInfo_State
    
    
    type FleetPackageInfo_State [int32](https://pkg.go.dev/builtin#int32)

Possible values for the `FleetPackage` state.

### FleetPackageInfo_STATE_UNSPECIFIED, FleetPackageInfo_ACTIVE, FleetPackageInfo_SUSPENDED, FleetPackageInfo_FAILED, FleetPackageInfo_DELETING
    
    
    const (
    	// Unspecified state.
    	FleetPackageInfo_STATE_UNSPECIFIED FleetPackageInfo_State = 0
    	// `FleetPackage` is active.
    	FleetPackageInfo_ACTIVE FleetPackageInfo_State = 1
    	// `FleetPackage` is suspended.
    	FleetPackageInfo_SUSPENDED FleetPackageInfo_State = 2
    	// `FleetPackage` has failed to reconcile.
    	FleetPackageInfo_FAILED FleetPackageInfo_State = 3
    	// `FleetPackage` is being deleted.
    	FleetPackageInfo_DELETING FleetPackageInfo_State = 4
    )

### func (FleetPackageInfo_State) Descriptor 
    
    
    func (FleetPackageInfo_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (FleetPackageInfo_State) Enum 
    
    
    func (x FleetPackageInfo_State) Enum() *FleetPackageInfo_State

### func (FleetPackageInfo_State) EnumDescriptor 
    
    
    func (FleetPackageInfo_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackageInfo_State.Descriptor instead.

### func (FleetPackageInfo_State) Number 
    
    
    func (x FleetPackageInfo_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (FleetPackageInfo_State) String 
    
    
    func (x FleetPackageInfo_State) String() [string](https://pkg.go.dev/builtin#string)

### func (FleetPackageInfo_State) Type 
    
    
    func (FleetPackageInfo_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## FleetPackage_CloudBuildRepository
    
    
    type FleetPackage_CloudBuildRepository struct {
    
    	// variants_pattern is the configuration for how to read the repository
    	// to find variants.
    	//
    	// Types that are valid to be assigned to Variants:
    	//
    	//	*FleetPackage_CloudBuildRepository_VariantsPattern
    	Variants isFleetPackage_CloudBuildRepository_Variants `protobuf_oneof:"variants"`
    	// Required. Name of the cloud build repository.
    	// Format is projects/{p}/locations/{l}/connections/{c}/repositories/{r}.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. path to the directory or file within the repository that
    	// contains the kubernetes configuration. If unspecified, path is assumed to
    	// the top level root directory of the repository.
    	Path [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=path,proto3" json:"path,omitempty"`
    	// Required. git tag of the underlying git repository.
    	// The git tag must be in the semantic version format `vX.Y.Z`.
    	Tag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=tag,proto3" json:"tag,omitempty"`
    	// Required. Google service account to use in CloudBuild triggers to fetch
    	// and store kubernetes configuration.
    	ServiceAccount [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=service_account,json=serviceAccount,proto3" json:"service_account,omitempty"`
    	// contains filtered or unexported fields
    }

CloudBuildRepository contains information about fetching Kubernetes configuration from a `CloudBuildRepository`.

### func (*FleetPackage_CloudBuildRepository) Descriptor 
    
    
    func (*FleetPackage_CloudBuildRepository) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_CloudBuildRepository.ProtoReflect.Descriptor instead.

### func (*FleetPackage_CloudBuildRepository) GetName 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_CloudBuildRepository) GetPath 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetPath() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_CloudBuildRepository) GetServiceAccount 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetServiceAccount() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_CloudBuildRepository) GetTag 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetTag() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_CloudBuildRepository) GetVariants 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetVariants() isFleetPackage_CloudBuildRepository_Variants

### func (*FleetPackage_CloudBuildRepository) GetVariantsPattern 
    
    
    func (x *FleetPackage_CloudBuildRepository) GetVariantsPattern() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_CloudBuildRepository) ProtoMessage 
    
    
    func (*FleetPackage_CloudBuildRepository) ProtoMessage()

### func (*FleetPackage_CloudBuildRepository) ProtoReflect 
    
    
    func (x *FleetPackage_CloudBuildRepository) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage_CloudBuildRepository) Reset 
    
    
    func (x *FleetPackage_CloudBuildRepository) Reset()

### func (*FleetPackage_CloudBuildRepository) String 
    
    
    func (x *FleetPackage_CloudBuildRepository) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage_CloudBuildRepository_VariantsPattern
    
    
    type FleetPackage_CloudBuildRepository_VariantsPattern struct {
    	// Optional. variants_pattern is a glob pattern that will be used to find
    	// variants in the repository. Examples: `variants/*.yaml`, `us-*`
    	VariantsPattern [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=variants_pattern,json=variantsPattern,proto3,oneof"`
    }

## FleetPackage_ResourceBundleSelector
    
    
    type FleetPackage_ResourceBundleSelector struct {
    
    	// source can be a directly pushed `ResourceBundle` or
    	// `CloudBuildRepository` containing the kubernetes configuration.
    	//
    	// Types that are valid to be assigned to Source:
    	//
    	//	*FleetPackage_ResourceBundleSelector_ResourceBundle
    	//	*FleetPackage_ResourceBundleSelector_CloudBuildRepository
    	Source isFleetPackage_ResourceBundleSelector_Source `protobuf_oneof:"source"`
    	// contains filtered or unexported fields
    }

Information specifying the source of kubernetes configuration to deploy.

### func (*FleetPackage_ResourceBundleSelector) Descriptor 
    
    
    func (*FleetPackage_ResourceBundleSelector) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_ResourceBundleSelector.ProtoReflect.Descriptor instead.

### func (*FleetPackage_ResourceBundleSelector) GetCloudBuildRepository 
    
    
    func (x *FleetPackage_ResourceBundleSelector) GetCloudBuildRepository() *FleetPackage_CloudBuildRepository

### func (*FleetPackage_ResourceBundleSelector) GetResourceBundle 
    
    
    func (x *FleetPackage_ResourceBundleSelector) GetResourceBundle() *FleetPackage_ResourceBundleTag

### func (*FleetPackage_ResourceBundleSelector) GetSource 
    
    
    func (x *FleetPackage_ResourceBundleSelector) GetSource() isFleetPackage_ResourceBundleSelector_Source

### func (*FleetPackage_ResourceBundleSelector) ProtoMessage 
    
    
    func (*FleetPackage_ResourceBundleSelector) ProtoMessage()

### func (*FleetPackage_ResourceBundleSelector) ProtoReflect 
    
    
    func (x *FleetPackage_ResourceBundleSelector) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage_ResourceBundleSelector) Reset 
    
    
    func (x *FleetPackage_ResourceBundleSelector) Reset()

### func (*FleetPackage_ResourceBundleSelector) String 
    
    
    func (x *FleetPackage_ResourceBundleSelector) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage_ResourceBundleSelector_CloudBuildRepository
    
    
    type FleetPackage_ResourceBundleSelector_CloudBuildRepository struct {
    	// Information specifying `CloudBuildRepository`.
    	CloudBuildRepository *FleetPackage_CloudBuildRepository `protobuf:"bytes,3,opt,name=cloud_build_repository,json=cloudBuildRepository,proto3,oneof"`
    }

## FleetPackage_ResourceBundleSelector_ResourceBundle
    
    
    type FleetPackage_ResourceBundleSelector_ResourceBundle struct {
    	// Information specifying `ResourceBundle`.
    	ResourceBundle *FleetPackage_ResourceBundleTag `protobuf:"bytes,1,opt,name=resource_bundle,json=resourceBundle,proto3,oneof"`
    }

## FleetPackage_ResourceBundleTag
    
    
    type FleetPackage_ResourceBundleTag struct {
    
    	// Required. Name of the `ResourceBundle`.
    	// Format is projects/{p}/locations/{l}/resourceBundles/{r}.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Tag refers to a version of the release in a `ResourceBundle`.
    	// This is a Git tag in the semantic version format `vX.Y.Z`.
    	Tag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=tag,proto3" json:"tag,omitempty"`
    	// contains filtered or unexported fields
    }

ResourceBundleTag contains the information to refer to a release for a `ResourceBundle`.

### func (*FleetPackage_ResourceBundleTag) Descriptor 
    
    
    func (*FleetPackage_ResourceBundleTag) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_ResourceBundleTag.ProtoReflect.Descriptor instead.

### func (*FleetPackage_ResourceBundleTag) GetName 
    
    
    func (x *FleetPackage_ResourceBundleTag) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_ResourceBundleTag) GetTag 
    
    
    func (x *FleetPackage_ResourceBundleTag) GetTag() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_ResourceBundleTag) ProtoMessage 
    
    
    func (*FleetPackage_ResourceBundleTag) ProtoMessage()

### func (*FleetPackage_ResourceBundleTag) ProtoReflect 
    
    
    func (x *FleetPackage_ResourceBundleTag) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage_ResourceBundleTag) Reset 
    
    
    func (x *FleetPackage_ResourceBundleTag) Reset()

### func (*FleetPackage_ResourceBundleTag) String 
    
    
    func (x *FleetPackage_ResourceBundleTag) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage_State
    
    
    type FleetPackage_State [int32](https://pkg.go.dev/builtin#int32)

State indicates the desired state for the fleet package. Unspecified value is equivalent to `ACTIVE`. If state is set to `SUSPENDED`, active rollout (if any) will continue but no new rollouts will be scheduled.

### FleetPackage_STATE_UNSPECIFIED, FleetPackage_ACTIVE, FleetPackage_SUSPENDED
    
    
    const (
    	// Unspecified state.
    	FleetPackage_STATE_UNSPECIFIED FleetPackage_State = 0
    	// `FleetPackage` is intended to be active.
    	FleetPackage_ACTIVE FleetPackage_State = 1
    	// `FleetPackage` is intended to be suspended.
    	FleetPackage_SUSPENDED FleetPackage_State = 2
    )

### func (FleetPackage_State) Descriptor 
    
    
    func (FleetPackage_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (FleetPackage_State) Enum 
    
    
    func (x FleetPackage_State) Enum() *FleetPackage_State

### func (FleetPackage_State) EnumDescriptor 
    
    
    func (FleetPackage_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_State.Descriptor instead.

### func (FleetPackage_State) Number 
    
    
    func (x FleetPackage_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (FleetPackage_State) String 
    
    
    func (x FleetPackage_State) String() [string](https://pkg.go.dev/builtin#string)

### func (FleetPackage_State) Type 
    
    
    func (FleetPackage_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## FleetPackage_Target
    
    
    type FleetPackage_Target struct {
    
    	// target for the fleet package.
    	//
    	// Types that are valid to be assigned to Target:
    	//
    	//	*FleetPackage_Target_Fleet
    	Target isFleetPackage_Target_Target `protobuf_oneof:"target"`
    	// contains filtered or unexported fields
    }

The target defines different ways to target set of kubernetes clusters.

### func (*FleetPackage_Target) Descriptor 
    
    
    func (*FleetPackage_Target) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_Target.ProtoReflect.Descriptor instead.

### func (*FleetPackage_Target) GetFleet 
    
    
    func (x *FleetPackage_Target) GetFleet() *Fleet

### func (*FleetPackage_Target) GetTarget 
    
    
    func (x *FleetPackage_Target) GetTarget() isFleetPackage_Target_Target

### func (*FleetPackage_Target) ProtoMessage 
    
    
    func (*FleetPackage_Target) ProtoMessage()

### func (*FleetPackage_Target) ProtoReflect 
    
    
    func (x *FleetPackage_Target) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage_Target) Reset 
    
    
    func (x *FleetPackage_Target) Reset()

### func (*FleetPackage_Target) String 
    
    
    func (x *FleetPackage_Target) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage_Target_Fleet
    
    
    type FleetPackage_Target_Fleet struct {
    	// The GKE fleet information.
    	Fleet *Fleet `protobuf:"bytes,1,opt,name=fleet,proto3,oneof"`
    }

## FleetPackage_VariantSelector
    
    
    type FleetPackage_VariantSelector struct {
    
    	// strategy for selecting a variant.
    	//
    	// Types that are valid to be assigned to Strategy:
    	//
    	//	*FleetPackage_VariantSelector_VariantNameTemplate
    	Strategy isFleetPackage_VariantSelector_Strategy `protobuf_oneof:"strategy"`
    	// contains filtered or unexported fields
    }

VariantSelector contains information for selecting a variant in `ResourceBundle` to deploy to a target cluster.

### func (*FleetPackage_VariantSelector) Descriptor 
    
    
    func (*FleetPackage_VariantSelector) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FleetPackage_VariantSelector.ProtoReflect.Descriptor instead.

### func (*FleetPackage_VariantSelector) GetStrategy 
    
    
    func (x *FleetPackage_VariantSelector) GetStrategy() isFleetPackage_VariantSelector_Strategy

### func (*FleetPackage_VariantSelector) GetVariantNameTemplate 
    
    
    func (x *FleetPackage_VariantSelector) GetVariantNameTemplate() [string](https://pkg.go.dev/builtin#string)

### func (*FleetPackage_VariantSelector) ProtoMessage 
    
    
    func (*FleetPackage_VariantSelector) ProtoMessage()

### func (*FleetPackage_VariantSelector) ProtoReflect 
    
    
    func (x *FleetPackage_VariantSelector) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FleetPackage_VariantSelector) Reset 
    
    
    func (x *FleetPackage_VariantSelector) Reset()

### func (*FleetPackage_VariantSelector) String 
    
    
    func (x *FleetPackage_VariantSelector) String() [string](https://pkg.go.dev/builtin#string)

## FleetPackage_VariantSelector_VariantNameTemplate
    
    
    type FleetPackage_VariantSelector_VariantNameTemplate struct {
    	// Required. variant_name_template is a template that can refer to
    	// variables containing cluster membership metadata such as location,
    	// name, and labels to generate the name of the variant for a target
    	// cluster. The variable syntax is similar to the unix shell variables.
    	//
    	// Available variables are `${membership.name}`, `${membership.location}`,
    	// `${membership.project}` and `${membership.labels['label_name']}`.
    	//
    	// If you want to deploy a specific variant, say "default" to all the
    	// clusters, you can use "default" (string without any variables) as
    	// the variant_name_template.
    	VariantNameTemplate [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=variant_name_template,json=variantNameTemplate,proto3,oneof"`
    }

## Fleet_LabelSelector
    
    
    type Fleet_LabelSelector struct {
    
    	// Optional. match_labels is a map of {key,value} pairs. Each {key,value}
    	// pair must match an existing label key and value exactly in order to
    	// satisfy the match.
    	MatchLabels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=match_labels,json=matchLabels,proto3" json:"match_labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

A label selector is a label query over a set of resources. An empty label selector matches all objects.

### func (*Fleet_LabelSelector) Descriptor 
    
    
    func (*Fleet_LabelSelector) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Fleet_LabelSelector.ProtoReflect.Descriptor instead.

### func (*Fleet_LabelSelector) GetMatchLabels 
    
    
    func (x *Fleet_LabelSelector) GetMatchLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Fleet_LabelSelector) ProtoMessage 
    
    
    func (*Fleet_LabelSelector) ProtoMessage()

### func (*Fleet_LabelSelector) ProtoReflect 
    
    
    func (x *Fleet_LabelSelector) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Fleet_LabelSelector) Reset 
    
    
    func (x *Fleet_LabelSelector) Reset()

### func (*Fleet_LabelSelector) String 
    
    
    func (x *Fleet_LabelSelector) String() [string](https://pkg.go.dev/builtin#string)

## GetFleetPackageRequest
    
    
    type GetFleetPackageRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a FleetPackage

### func (*GetFleetPackageRequest) Descriptor 
    
    
    func (*GetFleetPackageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetFleetPackageRequest.ProtoReflect.Descriptor instead.

### func (*GetFleetPackageRequest) GetName 
    
    
    func (x *GetFleetPackageRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetFleetPackageRequest) ProtoMessage 
    
    
    func (*GetFleetPackageRequest) ProtoMessage()

### func (*GetFleetPackageRequest) ProtoReflect 
    
    
    func (x *GetFleetPackageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetFleetPackageRequest) Reset 
    
    
    func (x *GetFleetPackageRequest) Reset()

### func (*GetFleetPackageRequest) String 
    
    
    func (x *GetFleetPackageRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetReleaseRequest
    
    
    type GetReleaseRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a Release

### func (*GetReleaseRequest) Descriptor 
    
    
    func (*GetReleaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetReleaseRequest.ProtoReflect.Descriptor instead.

### func (*GetReleaseRequest) GetName 
    
    
    func (x *GetReleaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetReleaseRequest) ProtoMessage 
    
    
    func (*GetReleaseRequest) ProtoMessage()

### func (*GetReleaseRequest) ProtoReflect 
    
    
    func (x *GetReleaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetReleaseRequest) Reset 
    
    
    func (x *GetReleaseRequest) Reset()

### func (*GetReleaseRequest) String 
    
    
    func (x *GetReleaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetResourceBundleRequest
    
    
    type GetResourceBundleRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a ResourceBundle.

### func (*GetResourceBundleRequest) Descriptor 
    
    
    func (*GetResourceBundleRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetResourceBundleRequest.ProtoReflect.Descriptor instead.

### func (*GetResourceBundleRequest) GetName 
    
    
    func (x *GetResourceBundleRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetResourceBundleRequest) ProtoMessage 
    
    
    func (*GetResourceBundleRequest) ProtoMessage()

### func (*GetResourceBundleRequest) ProtoReflect 
    
    
    func (x *GetResourceBundleRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetResourceBundleRequest) Reset 
    
    
    func (x *GetResourceBundleRequest) Reset()

### func (*GetResourceBundleRequest) String 
    
    
    func (x *GetResourceBundleRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetRolloutRequest
    
    
    type GetRolloutRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a Rollout

### func (*GetRolloutRequest) Descriptor 
    
    
    func (*GetRolloutRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetRolloutRequest.ProtoReflect.Descriptor instead.

### func (*GetRolloutRequest) GetName 
    
    
    func (x *GetRolloutRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetRolloutRequest) ProtoMessage 
    
    
    func (*GetRolloutRequest) ProtoMessage()

### func (*GetRolloutRequest) ProtoReflect 
    
    
    func (x *GetRolloutRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetRolloutRequest) Reset 
    
    
    func (x *GetRolloutRequest) Reset()

### func (*GetRolloutRequest) String 
    
    
    func (x *GetRolloutRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetVariantRequest
    
    
    type GetVariantRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a Variant

### func (*GetVariantRequest) Descriptor 
    
    
    func (*GetVariantRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetVariantRequest.ProtoReflect.Descriptor instead.

### func (*GetVariantRequest) GetName 
    
    
    func (x *GetVariantRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetVariantRequest) ProtoMessage 
    
    
    func (*GetVariantRequest) ProtoMessage()

### func (*GetVariantRequest) ProtoReflect 
    
    
    func (x *GetVariantRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetVariantRequest) Reset 
    
    
    func (x *GetVariantRequest) Reset()

### func (*GetVariantRequest) String 
    
    
    func (x *GetVariantRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListFleetPackagesRequest
    
    
    type ListFleetPackagesRequest struct {
    
    	// Required. Parent value for ListFleetPackagesRequest.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of FleetPackage.

### func (*ListFleetPackagesRequest) Descriptor 
    
    
    func (*ListFleetPackagesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListFleetPackagesRequest.ProtoReflect.Descriptor instead.

### func (*ListFleetPackagesRequest) GetFilter 
    
    
    func (x *ListFleetPackagesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesRequest) GetOrderBy 
    
    
    func (x *ListFleetPackagesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesRequest) GetPageSize 
    
    
    func (x *ListFleetPackagesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListFleetPackagesRequest) GetPageToken 
    
    
    func (x *ListFleetPackagesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesRequest) GetParent 
    
    
    func (x *ListFleetPackagesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesRequest) ProtoMessage 
    
    
    func (*ListFleetPackagesRequest) ProtoMessage()

### func (*ListFleetPackagesRequest) ProtoReflect 
    
    
    func (x *ListFleetPackagesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListFleetPackagesRequest) Reset 
    
    
    func (x *ListFleetPackagesRequest) Reset()

### func (*ListFleetPackagesRequest) String 
    
    
    func (x *ListFleetPackagesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListFleetPackagesResponse
    
    
    type ListFleetPackagesResponse struct {
    
    	// The list of FleetPackage
    	FleetPackages []*FleetPackage `protobuf:"bytes,1,rep,name=fleet_packages,json=fleetPackages,proto3" json:"fleet_packages,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing FleetPackage

### func (*ListFleetPackagesResponse) Descriptor 
    
    
    func (*ListFleetPackagesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListFleetPackagesResponse.ProtoReflect.Descriptor instead.

### func (*ListFleetPackagesResponse) GetFleetPackages 
    
    
    func (x *ListFleetPackagesResponse) GetFleetPackages() []*FleetPackage

### func (*ListFleetPackagesResponse) GetNextPageToken 
    
    
    func (x *ListFleetPackagesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesResponse) GetUnreachable 
    
    
    func (x *ListFleetPackagesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListFleetPackagesResponse) ProtoMessage 
    
    
    func (*ListFleetPackagesResponse) ProtoMessage()

### func (*ListFleetPackagesResponse) ProtoReflect 
    
    
    func (x *ListFleetPackagesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListFleetPackagesResponse) Reset 
    
    
    func (x *ListFleetPackagesResponse) Reset()

### func (*ListFleetPackagesResponse) String 
    
    
    func (x *ListFleetPackagesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReleasesRequest
    
    
    type ListReleasesRequest struct {
    
    	// Required. Parent value for ListReleasesRequest.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of Releases.

### func (*ListReleasesRequest) Descriptor 
    
    
    func (*ListReleasesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReleasesRequest.ProtoReflect.Descriptor instead.

### func (*ListReleasesRequest) GetFilter 
    
    
    func (x *ListReleasesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesRequest) GetOrderBy 
    
    
    func (x *ListReleasesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesRequest) GetPageSize 
    
    
    func (x *ListReleasesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReleasesRequest) GetPageToken 
    
    
    func (x *ListReleasesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesRequest) GetParent 
    
    
    func (x *ListReleasesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesRequest) ProtoMessage 
    
    
    func (*ListReleasesRequest) ProtoMessage()

### func (*ListReleasesRequest) ProtoReflect 
    
    
    func (x *ListReleasesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReleasesRequest) Reset 
    
    
    func (x *ListReleasesRequest) Reset()

### func (*ListReleasesRequest) String 
    
    
    func (x *ListReleasesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReleasesResponse
    
    
    type ListReleasesResponse struct {
    
    	// The list of Releases
    	Releases []*Release `protobuf:"bytes,1,rep,name=releases,proto3" json:"releases,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing Releases

### func (*ListReleasesResponse) Descriptor 
    
    
    func (*ListReleasesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReleasesResponse.ProtoReflect.Descriptor instead.

### func (*ListReleasesResponse) GetNextPageToken 
    
    
    func (x *ListReleasesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesResponse) GetReleases 
    
    
    func (x *ListReleasesResponse) GetReleases() []*Release

### func (*ListReleasesResponse) GetUnreachable 
    
    
    func (x *ListReleasesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListReleasesResponse) ProtoMessage 
    
    
    func (*ListReleasesResponse) ProtoMessage()

### func (*ListReleasesResponse) ProtoReflect 
    
    
    func (x *ListReleasesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReleasesResponse) Reset 
    
    
    func (x *ListReleasesResponse) Reset()

### func (*ListReleasesResponse) String 
    
    
    func (x *ListReleasesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListResourceBundlesRequest
    
    
    type ListResourceBundlesRequest struct {
    
    	// Required. Parent value for ListResourceBundlesRequest.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of ResourceBundles.

### func (*ListResourceBundlesRequest) Descriptor 
    
    
    func (*ListResourceBundlesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListResourceBundlesRequest.ProtoReflect.Descriptor instead.

### func (*ListResourceBundlesRequest) GetFilter 
    
    
    func (x *ListResourceBundlesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesRequest) GetOrderBy 
    
    
    func (x *ListResourceBundlesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesRequest) GetPageSize 
    
    
    func (x *ListResourceBundlesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListResourceBundlesRequest) GetPageToken 
    
    
    func (x *ListResourceBundlesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesRequest) GetParent 
    
    
    func (x *ListResourceBundlesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesRequest) ProtoMessage 
    
    
    func (*ListResourceBundlesRequest) ProtoMessage()

### func (*ListResourceBundlesRequest) ProtoReflect 
    
    
    func (x *ListResourceBundlesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListResourceBundlesRequest) Reset 
    
    
    func (x *ListResourceBundlesRequest) Reset()

### func (*ListResourceBundlesRequest) String 
    
    
    func (x *ListResourceBundlesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListResourceBundlesResponse
    
    
    type ListResourceBundlesResponse struct {
    
    	// The list of ResourceBundle.
    	ResourceBundles []*ResourceBundle `protobuf:"bytes,1,rep,name=resource_bundles,json=resourceBundles,proto3" json:"resource_bundles,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing ResourceBundles.

### func (*ListResourceBundlesResponse) Descriptor 
    
    
    func (*ListResourceBundlesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListResourceBundlesResponse.ProtoReflect.Descriptor instead.

### func (*ListResourceBundlesResponse) GetNextPageToken 
    
    
    func (x *ListResourceBundlesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesResponse) GetResourceBundles 
    
    
    func (x *ListResourceBundlesResponse) GetResourceBundles() []*ResourceBundle

### func (*ListResourceBundlesResponse) GetUnreachable 
    
    
    func (x *ListResourceBundlesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListResourceBundlesResponse) ProtoMessage 
    
    
    func (*ListResourceBundlesResponse) ProtoMessage()

### func (*ListResourceBundlesResponse) ProtoReflect 
    
    
    func (x *ListResourceBundlesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListResourceBundlesResponse) Reset 
    
    
    func (x *ListResourceBundlesResponse) Reset()

### func (*ListResourceBundlesResponse) String 
    
    
    func (x *ListResourceBundlesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListRolloutsRequest
    
    
    type ListRolloutsRequest struct {
    
    	// Required. Parent value for ListRolloutsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of Rollouts

### func (*ListRolloutsRequest) Descriptor 
    
    
    func (*ListRolloutsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRolloutsRequest.ProtoReflect.Descriptor instead.

### func (*ListRolloutsRequest) GetFilter 
    
    
    func (x *ListRolloutsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsRequest) GetOrderBy 
    
    
    func (x *ListRolloutsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsRequest) GetPageSize 
    
    
    func (x *ListRolloutsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListRolloutsRequest) GetPageToken 
    
    
    func (x *ListRolloutsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsRequest) GetParent 
    
    
    func (x *ListRolloutsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsRequest) ProtoMessage 
    
    
    func (*ListRolloutsRequest) ProtoMessage()

### func (*ListRolloutsRequest) ProtoReflect 
    
    
    func (x *ListRolloutsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRolloutsRequest) Reset 
    
    
    func (x *ListRolloutsRequest) Reset()

### func (*ListRolloutsRequest) String 
    
    
    func (x *ListRolloutsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListRolloutsResponse
    
    
    type ListRolloutsResponse struct {
    
    	// The list of Rollouts
    	Rollouts []*Rollout `protobuf:"bytes,1,rep,name=rollouts,proto3" json:"rollouts,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing Rollouts

### func (*ListRolloutsResponse) Descriptor 
    
    
    func (*ListRolloutsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListRolloutsResponse.ProtoReflect.Descriptor instead.

### func (*ListRolloutsResponse) GetNextPageToken 
    
    
    func (x *ListRolloutsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsResponse) GetRollouts 
    
    
    func (x *ListRolloutsResponse) GetRollouts() []*Rollout

### func (*ListRolloutsResponse) GetUnreachable 
    
    
    func (x *ListRolloutsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListRolloutsResponse) ProtoMessage 
    
    
    func (*ListRolloutsResponse) ProtoMessage()

### func (*ListRolloutsResponse) ProtoReflect 
    
    
    func (x *ListRolloutsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListRolloutsResponse) Reset 
    
    
    func (x *ListRolloutsResponse) Reset()

### func (*ListRolloutsResponse) String 
    
    
    func (x *ListRolloutsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListVariantsRequest
    
    
    type ListVariantsRequest struct {
    
    	// Required. Parent value for ListVariantsRequest.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of Variants.

### func (*ListVariantsRequest) Descriptor 
    
    
    func (*ListVariantsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListVariantsRequest.ProtoReflect.Descriptor instead.

### func (*ListVariantsRequest) GetFilter 
    
    
    func (x *ListVariantsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsRequest) GetOrderBy 
    
    
    func (x *ListVariantsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsRequest) GetPageSize 
    
    
    func (x *ListVariantsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListVariantsRequest) GetPageToken 
    
    
    func (x *ListVariantsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsRequest) GetParent 
    
    
    func (x *ListVariantsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsRequest) ProtoMessage 
    
    
    func (*ListVariantsRequest) ProtoMessage()

### func (*ListVariantsRequest) ProtoReflect 
    
    
    func (x *ListVariantsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListVariantsRequest) Reset 
    
    
    func (x *ListVariantsRequest) Reset()

### func (*ListVariantsRequest) String 
    
    
    func (x *ListVariantsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListVariantsResponse
    
    
    type ListVariantsResponse struct {
    
    	// The list of Variants
    	Variants []*Variant `protobuf:"bytes,1,rep,name=variants,proto3" json:"variants,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing Variants

### func (*ListVariantsResponse) Descriptor 
    
    
    func (*ListVariantsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListVariantsResponse.ProtoReflect.Descriptor instead.

### func (*ListVariantsResponse) GetNextPageToken 
    
    
    func (x *ListVariantsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsResponse) GetUnreachable 
    
    
    func (x *ListVariantsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListVariantsResponse) GetVariants 
    
    
    func (x *ListVariantsResponse) GetVariants() []*Variant

### func (*ListVariantsResponse) ProtoMessage 
    
    
    func (*ListVariantsResponse) ProtoMessage()

### func (*ListVariantsResponse) ProtoReflect 
    
    
    func (x *ListVariantsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListVariantsResponse) Reset 
    
    
    func (x *ListVariantsResponse) Reset()

### func (*ListVariantsResponse) String 
    
    
    func (x *ListVariantsResponse) String() [string](https://pkg.go.dev/builtin#string)

## OperationMetadata
    
    
    type OperationMetadata struct {
    
    	// Output only. The time the operation was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time the operation finished running.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// Output only. Server-defined resource path for the target of the operation.
    	Target [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=target,proto3" json:"target,omitempty"`
    	// Output only. Name of the verb executed by the operation.
    	Verb [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=verb,proto3" json:"verb,omitempty"`
    	// Output only. Human-readable status of the operation, if any.
    	StatusMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=status_message,json=statusMessage,proto3" json:"status_message,omitempty"`
    	// Output only. Identifies whether the user has requested cancellation
    	// of the operation. Operations that have been cancelled successfully
    	// have
    	// [google.longrunning.Operation.error][google.longrunning.Operation.error]
    	// value with a [google.rpc.Status.code][google.rpc.Status.code] of 1,
    	// corresponding to `Code.CANCELLED`.
    	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=requested_cancellation,json=requestedCancellation,proto3" json:"requested_cancellation,omitempty"`
    	// Output only. API version used to start the operation.
    	ApiVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=api_version,json=apiVersion,proto3" json:"api_version,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the metadata of the long-running operation.

### func (*OperationMetadata) Descriptor 
    
    
    func (*OperationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OperationMetadata.ProtoReflect.Descriptor instead.

### func (*OperationMetadata) GetApiVersion 
    
    
    func (x *OperationMetadata) GetApiVersion() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetCreateTime 
    
    
    func (x *OperationMetadata) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*OperationMetadata) GetEndTime 
    
    
    func (x *OperationMetadata) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*OperationMetadata) GetRequestedCancellation 
    
    
    func (x *OperationMetadata) GetRequestedCancellation() [bool](https://pkg.go.dev/builtin#bool)

### func (*OperationMetadata) GetStatusMessage 
    
    
    func (x *OperationMetadata) GetStatusMessage() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetTarget 
    
    
    func (x *OperationMetadata) GetTarget() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetVerb 
    
    
    func (x *OperationMetadata) GetVerb() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) ProtoMessage 
    
    
    func (*OperationMetadata) ProtoMessage()

### func (*OperationMetadata) ProtoReflect 
    
    
    func (x *OperationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OperationMetadata) Reset 
    
    
    func (x *OperationMetadata) Reset()

### func (*OperationMetadata) String 
    
    
    func (x *OperationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## Release
    
    
    type Release struct {
    
    	// Identifier. Name of the Release. Format is
    	// `projects/{project}/locations/location}/resourceBundles/{resource_bundle}/release/[a-z][a-z0-9\-]{0,62}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Time `Release` was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Time `Release` was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Optional. Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Optional. lifecycle of the `Release`.
    	Lifecycle Release_Lifecycle `protobuf:"varint,5,opt,name=lifecycle,proto3,enum=google.cloud.configdelivery.v1.Release_Lifecycle" json:"lifecycle,omitempty"`
    	// Required. version of the `Release`. This must be v

`Release` represents a versioned release containing kubernetes manifests.

### func (*Release) Descriptor 
    
    
    func (*Release) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Release.ProtoReflect.Descriptor instead.

### func (*Release) GetCreateTime 
    
    
    func (x *Release) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Release) GetInfo 
    
    
    func (x *Release) GetInfo() *ReleaseInfo

### func (*Release) GetLabels 
    
    
    func (x *Release) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Release) GetLifecycle 
    
    
    func (x *Release) GetLifecycle() Release_Lifecycle

### func (*Release) GetName 
    
    
    func (x *Release) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Release) GetPublishTime 
    
    
    func (x *Release) GetPublishTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Release) GetUpdateTime 
    
    
    func (x *Release) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Release) GetVersion 
    
    
    func (x *Release) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*Release) ProtoMessage 
    
    
    func (*Release) ProtoMessage()

### func (*Release) ProtoReflect 
    
    
    func (x *Release) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Release) Reset 
    
    
    func (x *Release) Reset()

### func (*Release) String 
    
    
    func (x *Release) String() [string](https://pkg.go.dev/builtin#string)

## ReleaseInfo
    
    
    type ReleaseInfo struct {
    
    	// Output only. path to the oci image the service uploads to on a `Release`
    	// creation.
    	OciImagePath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=oci_image_path,json=ociImagePath,proto3" json:"oci_image_path,omitempty"`
    	// Optional. per-variant paths to the oci images the service uploads on
    	// package release creation
    	VariantOciImagePaths map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=variant_oci_image_paths,json=variantOciImagePaths,proto3" json:"variant_oci_image_paths,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

ReleaseInfo contains extra information about the `ResourceBundle` release e.g., link to an artifact registry OCI image.

### func (*ReleaseInfo) Descriptor 
    
    
    func (*ReleaseInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReleaseInfo.ProtoReflect.Descriptor instead.

### func (*ReleaseInfo) GetOciImagePath 
    
    
    func (x *ReleaseInfo) GetOciImagePath() [string](https://pkg.go.dev/builtin#string)

### func (*ReleaseInfo) GetVariantOciImagePaths 
    
    
    func (x *ReleaseInfo) GetVariantOciImagePaths() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*ReleaseInfo) ProtoMessage 
    
    
    func (*ReleaseInfo) ProtoMessage()

### func (*ReleaseInfo) ProtoReflect 
    
    
    func (x *ReleaseInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReleaseInfo) Reset 
    
    
    func (x *ReleaseInfo) Reset()

### func (*ReleaseInfo) String 
    
    
    func (x *ReleaseInfo) String() [string](https://pkg.go.dev/builtin#string)

## Release_Lifecycle
    
    
    type Release_Lifecycle [int32](https://pkg.go.dev/builtin#int32)

Lifecycle indicates the state of the `Release`. A published release is immutable.

### Release_LIFECYCLE_UNSPECIFIED, Release_DRAFT, Release_PUBLISHED
    
    
    const (
    	// indicates lifecycle has not been specified.
    	Release_LIFECYCLE_UNSPECIFIED Release_Lifecycle = 0
    	// indicates that the `Release` is being edited.
    	Release_DRAFT Release_Lifecycle = 1
    	// indicates that the `Release` is now published (or released) and
    	// immutable.
    	Release_PUBLISHED Release_Lifecycle = 2
    )

### func (Release_Lifecycle) Descriptor 
    
    
    func (Release_Lifecycle) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Release_Lifecycle) Enum 
    
    
    func (x Release_Lifecycle) Enum() *Release_Lifecycle

### func (Release_Lifecycle) EnumDescriptor 
    
    
    func (Release_Lifecycle) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Release_Lifecycle.Descriptor instead.

### func (Release_Lifecycle) Number 
    
    
    func (x Release_Lifecycle) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Release_Lifecycle) String 
    
    
    func (x Release_Lifecycle) String() [string](https://pkg.go.dev/builtin#string)

### func (Release_Lifecycle) Type 
    
    
    func (Release_Lifecycle) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ResourceBundle
    
    
    type ResourceBundle struct {
    
    	// Identifier. Name of the `ResourceBundle`. Format is
    	// `projects/{project}/locations/{location}/resourceBundle
    	// /[a-z][a-z0-9\-]{0,62}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Time `ResourceBundle` was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Time `ResourceBundle` was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Optional. Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Optional. Human readable description of the `ResourceBundle`.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// contains filtered or unexported fields
    }

ResourceBundle represent a collection of kubernetes configuration resources.

### func (*ResourceBundle) Descriptor 
    
    
    func (*ResourceBundle) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResourceBundle.ProtoReflect.Descriptor instead.

### func (*ResourceBundle) GetCreateTime 
    
    
    func (x *ResourceBundle) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ResourceBundle) GetDescription 
    
    
    func (x *ResourceBundle) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundle) GetLabels 
    
    
    func (x *ResourceBundle) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundle) GetName 
    
    
    func (x *ResourceBundle) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundle) GetUpdateTime 
    
    
    func (x *ResourceBundle) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ResourceBundle) ProtoMessage 
    
    
    func (*ResourceBundle) ProtoMessage()

### func (*ResourceBundle) ProtoReflect 
    
    
    func (x *ResourceBundle) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResourceBundle) Reset 
    
    
    func (x *ResourceBundle) Reset()

### func (*ResourceBundle) String 
    
    
    func (x *ResourceBundle) String() [string](https://pkg.go.dev/builtin#string)

## ResourceBundleDeploymentInfo
    
    
    type ResourceBundleDeploymentInfo struct {
    
    	// Output only. Refers to a `ResourceBundle` release.
    	Release [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=release,proto3" json:"release,omitempty"`
    	// Output only. Refers to a version of the `ResourceBundle` release.
    	Version [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=version,proto3" json:"version,omitempty"`
    	// Output only. Refers to a variant in a `ResourceBundle` release.
    	Variant [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=variant,proto3" json:"variant,omitempty"`
    	// Output only. Synchronization state of the `ResourceBundle` deployment.
    	SyncState ResourceBundleDeploymentInfo_SyncState `protobuf:"varint,4,opt,name=sync_state,json=syncState,proto3,enum=google.cloud.configdelivery.v1.ResourceBundleDeploymentInfo_SyncState" json:"sync_state,omitempty"`
    	// Output only. Unordered list. Messages contains information related to the
    	// `ResourceBundle` deployment. For example, in case of an error, indicate the
    	// reason for the error. In case of a pending deployment, reason for why the
    	// deployment of new release is pending.
    	Messages [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=messages,proto3" json:"messages,omitempty"`
    	// contains filtered or unexported fields
    }

ResourceBundleDeploymentInfo represents the status of a resource bundle deployment.

### func (*ResourceBundleDeploymentInfo) Descriptor 
    
    
    func (*ResourceBundleDeploymentInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResourceBundleDeploymentInfo.ProtoReflect.Descriptor instead.

### func (*ResourceBundleDeploymentInfo) GetMessages 
    
    
    func (x *ResourceBundleDeploymentInfo) GetMessages() [][string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundleDeploymentInfo) GetRelease 
    
    
    func (x *ResourceBundleDeploymentInfo) GetRelease() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundleDeploymentInfo) GetSyncState 
    
    
    func (x *ResourceBundleDeploymentInfo) GetSyncState() ResourceBundleDeploymentInfo_SyncState

### func (*ResourceBundleDeploymentInfo) GetVariant 
    
    
    func (x *ResourceBundleDeploymentInfo) GetVariant() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundleDeploymentInfo) GetVersion 
    
    
    func (x *ResourceBundleDeploymentInfo) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceBundleDeploymentInfo) ProtoMessage 
    
    
    func (*ResourceBundleDeploymentInfo) ProtoMessage()

### func (*ResourceBundleDeploymentInfo) ProtoReflect 
    
    
    func (x *ResourceBundleDeploymentInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResourceBundleDeploymentInfo) Reset 
    
    
    func (x *ResourceBundleDeploymentInfo) Reset()

### func (*ResourceBundleDeploymentInfo) String 
    
    
    func (x *ResourceBundleDeploymentInfo) String() [string](https://pkg.go.dev/builtin#string)

## ResourceBundleDeploymentInfo_SyncState
    
    
    type ResourceBundleDeploymentInfo_SyncState [int32](https://pkg.go.dev/builtin#int32)

Synchronization state of the resource bundle deployment.

### ResourceBundleDeploymentInfo_SYNC_STATE_UNSPECIFIED, ResourceBundleDeploymentInfo_RECONCILING, ResourceBundleDeploymentInfo_STALLED, ResourceBundleDeploymentInfo_SYNCED, ResourceBundleDeploymentInfo_PENDING, ResourceBundleDeploymentInfo_ERROR, ResourceBundleDeploymentInfo_DELETION_PENDING, ResourceBundleDeploymentInfo_DELETING, ResourceBundleDeploymentInfo_DELETED
    
    
    const (
    	// Unspecified state.
    	ResourceBundleDeploymentInfo_SYNC_STATE_UNSPECIFIED ResourceBundleDeploymentInfo_SyncState = 0
    	// Reconciling state.
    	ResourceBundleDeploymentInfo_RECONCILING ResourceBundleDeploymentInfo_SyncState = 1
    	// Stalled state.
    	ResourceBundleDeploymentInfo_STALLED ResourceBundleDeploymentInfo_SyncState = 2
    	// Synced state.
    	ResourceBundleDeploymentInfo_SYNCED ResourceBundleDeploymentInfo_SyncState = 3
    	// Pending state.
    	ResourceBundleDeploymentInfo_PENDING ResourceBundleDeploymentInfo_SyncState = 4
    	// Error state.
    	ResourceBundleDeploymentInfo_ERROR ResourceBundleDeploymentInfo_SyncState = 5
    	// Deletion pending state.
    	ResourceBundleDeploymentInfo_DELETION_PENDING ResourceBundleDeploymentInfo_SyncState = 6
    	// Deleting state.
    	ResourceBundleDeploymentInfo_DELETING ResourceBundleDeploymentInfo_SyncState = 7
    	// Deleted state.
    	ResourceBundleDeploymentInfo_DELETED ResourceBundleDeploymentInfo_SyncState = 8
    )

### func (ResourceBundleDeploymentInfo_SyncState) Descriptor 
    
    
    func (ResourceBundleDeploymentInfo_SyncState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ResourceBundleDeploymentInfo_SyncState) Enum 
    
    
    func (x ResourceBundleDeploymentInfo_SyncState) Enum() *ResourceBundleDeploymentInfo_SyncState

### func (ResourceBundleDeploymentInfo_SyncState) EnumDescriptor 
    
    
    func (ResourceBundleDeploymentInfo_SyncState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResourceBundleDeploymentInfo_SyncState.Descriptor instead.

### func (ResourceBundleDeploymentInfo_SyncState) Number 
    
    
    func (x ResourceBundleDeploymentInfo_SyncState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ResourceBundleDeploymentInfo_SyncState) String 
    
    
    func (x ResourceBundleDeploymentInfo_SyncState) String() [string](https://pkg.go.dev/builtin#string)

### func (ResourceBundleDeploymentInfo_SyncState) Type 
    
    
    func (ResourceBundleDeploymentInfo_SyncState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ResumeRolloutRequest
    
    
    type ResumeRolloutRequest struct {
    
    	// Required. Name of the Rollout.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Reason for resuming the rollout.
    	Reason [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
    	// contains filtered or unexported fields
    }

Message for resuming a rollout.

### func (*ResumeRolloutRequest) Descriptor 
    
    
    func (*ResumeRolloutRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResumeRolloutRequest.ProtoReflect.Descriptor instead.

### func (*ResumeRolloutRequest) GetName 
    
    
    func (x *ResumeRolloutRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ResumeRolloutRequest) GetReason 
    
    
    func (x *ResumeRolloutRequest) GetReason() [string](https://pkg.go.dev/builtin#string)

### func (*ResumeRolloutRequest) ProtoMessage 
    
    
    func (*ResumeRolloutRequest) ProtoMessage()

### func (*ResumeRolloutRequest) ProtoReflect 
    
    
    func (x *ResumeRolloutRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResumeRolloutRequest) Reset 
    
    
    func (x *ResumeRolloutRequest) Reset()

### func (*ResumeRolloutRequest) String 
    
    
    func (x *ResumeRolloutRequest) String() [string](https://pkg.go.dev/builtin#string)

## RollingStrategy
    
    
    type RollingStrategy struct {
    
    	// Optional. Maximum number of clusters to update the resource bundle on
    	// concurrently.
    	MaxConcurrent [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=max_concurrent,json=maxConcurrent,proto3" json:"max_concurrent,omitempty"`
    	// contains filtered or unexported fields
    }

RollingStrategy causes a specified number of clusters to be updated concurrently until all clusters are updated.

### func (*RollingStrategy) Descriptor 
    
    
    func (*RollingStrategy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RollingStrategy.ProtoReflect.Descriptor instead.

### func (*RollingStrategy) GetMaxConcurrent 
    
    
    func (x *RollingStrategy) GetMaxConcurrent() [int32](https://pkg.go.dev/builtin#int32)

### func (*RollingStrategy) ProtoMessage 
    
    
    func (*RollingStrategy) ProtoMessage()

### func (*RollingStrategy) ProtoReflect 
    
    
    func (x *RollingStrategy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RollingStrategy) Reset 
    
    
    func (x *RollingStrategy) Reset()

### func (*RollingStrategy) String 
    
    
    func (x *RollingStrategy) String() [string](https://pkg.go.dev/builtin#string)

## RollingStrategyInfo
    
    
    type RollingStrategyInfo struct {
    
    	// Unordered list. resource bundle's deployment status for all targeted
    	// clusters.
    	Clusters []*ClusterInfo `protobuf:"bytes,1,rep,name=clusters,proto3" json:"clusters,omitempty"`
    	// contains filtered or unexported fields
    }

RollingStrategyInfo represents the status of execution of Rolling rollout strategy.

### func (*RollingStrategyInfo) Descriptor 
    
    
    func (*RollingStrategyInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RollingStrategyInfo.ProtoReflect.Descriptor instead.

### func (*RollingStrategyInfo) GetClusters 
    
    
    func (x *RollingStrategyInfo) GetClusters() []*ClusterInfo

### func (*RollingStrategyInfo) ProtoMessage 
    
    
    func (*RollingStrategyInfo) ProtoMessage()

### func (*RollingStrategyInfo) ProtoReflect 
    
    
    func (x *RollingStrategyInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RollingStrategyInfo) Reset 
    
    
    func (x *RollingStrategyInfo) Reset()

### func (*RollingStrategyInfo) String 
    
    
    func (x *RollingStrategyInfo) String() [string](https://pkg.go.dev/builtin#string)

## Rollout
    
    
    type Rollout struct {
    
    	// Identifier. Name of the Rollout. Format is
    	// `projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/[a-z][a-z0-9\-]{0,62}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Reference to the `Release` being rolled out.
    	Release [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=release,proto3" json:"release,omitempty"`
    	// Rollout strategy for rolling out `FleetPackage` to clusters.
    	RolloutStrategy *RolloutStrategy `protobuf:"bytes,4,opt,name=rollout_strategy,json=rolloutStrategy,proto3" json:"rollout_strategy,omitempty"`
    	// Current details of the rollout.
    	Info *RolloutInfo `protobuf:"bytes,5,opt,name=info,proto3" json:"info,omitempty"`
    	// Deletion propagation policy of the rollout.
    	DeletionPropagationPolicy DeletionPropagationPolicy `protobuf:"varint,7,opt,name=deletion_propagation_policy,json=deletionPropagationPolicy,proto3,enum=google.cloud.configdelivery.v1.DeletionPropagationPolicy" json:"deletion_propagation_policy,omitempty"`
    	// Output only. The time the rollout was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time the rollout was most recently updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,9,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// contains filtered or unexported fields
    }

Rollout resource represents an instance of `FleetPackage` rollout operation across a fleet. This is a system generated resource and will be read only for end-users. It will be primarily used by the service to process the changes in the `FleetPackage` and other changes in the environment.

### func (*Rollout) Descriptor 
    
    
    func (*Rollout) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Rollout.ProtoReflect.Descriptor instead.

### func (*Rollout) GetCreateTime 
    
    
    func (x *Rollout) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Rollout) GetDeletionPropagationPolicy 
    
    
    func (x *Rollout) GetDeletionPropagationPolicy() DeletionPropagationPolicy

### func (*Rollout) GetInfo 
    
    
    func (x *Rollout) GetInfo() *RolloutInfo

### func (*Rollout) GetName 
    
    
    func (x *Rollout) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Rollout) GetRelease 
    
    
    func (x *Rollout) GetRelease() [string](https://pkg.go.dev/builtin#string)

### func (*Rollout) GetRolloutStrategy 
    
    
    func (x *Rollout) GetRolloutStrategy() *RolloutStrategy

### func (*Rollout) GetUpdateTime 
    
    
    func (x *Rollout) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Rollout) ProtoMessage 
    
    
    func (*Rollout) ProtoMessage()

### func (*Rollout) ProtoReflect 
    
    
    func (x *Rollout) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Rollout) Reset 
    
    
    func (x *Rollout) Reset()

### func (*Rollout) String 
    
    
    func (x *Rollout) String() [string](https://pkg.go.dev/builtin#string)

## RolloutInfo
    
    
    type RolloutInfo struct {
    
    	// Output only. state contains the overall status of the Rollout.
    	State RolloutInfo_State `protobuf:"varint,1,opt,name=state,proto3,enum=google.cloud.configdelivery.v1.RolloutInfo_State" json:"state,omitempty"`
    	// Output only. Time when the rollout started.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// Output only. Time when the rollout completed.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// Output only. Message containing additional information related to the
    	// rollout.
    	Message [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=message,proto3" json:"message,omitempty"`
    	// Output only. Rollout strategy info represents the status of execution of
    	// rollout strategy.
    	RolloutStrategyInfo *RolloutStrategyInfo `protobuf:"bytes,7,opt,name=rollout_strategy_info,json=rolloutStrategyInfo,proto3" json:"rollout_strategy_info,omitempty"`
    	// contains filtered or unexported fields
    }

RolloutInfo represents the state of the `FleetPackage` at all the clusters the rollout is targeting.

### func (*RolloutInfo) Descriptor 
    
    
    func (*RolloutInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RolloutInfo.ProtoReflect.Descriptor instead.

### func (*RolloutInfo) GetEndTime 
    
    
    func (x *RolloutInfo) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*RolloutInfo) GetMessage 
    
    
    func (x *RolloutInfo) GetMessage() [string](https://pkg.go.dev/builtin#string)

### func (*RolloutInfo) GetRolloutStrategyInfo 
    
    
    func (x *RolloutInfo) GetRolloutStrategyInfo() *RolloutStrategyInfo

### func (*RolloutInfo) GetStartTime 
    
    
    func (x *RolloutInfo) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*RolloutInfo) GetState 
    
    
    func (x *RolloutInfo) GetState() RolloutInfo_State

### func (*RolloutInfo) ProtoMessage 
    
    
    func (*RolloutInfo) ProtoMessage()

### func (*RolloutInfo) ProtoReflect 
    
    
    func (x *RolloutInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RolloutInfo) Reset 
    
    
    func (x *RolloutInfo) Reset()

### func (*RolloutInfo) String 
    
    
    func (x *RolloutInfo) String() [string](https://pkg.go.dev/builtin#string)

## RolloutInfo_State
    
    
    type RolloutInfo_State [int32](https://pkg.go.dev/builtin#int32)

State of the rollout

### RolloutInfo_STATE_UNSPECIFIED, RolloutInfo_COMPLETED, RolloutInfo_SUSPENDED, RolloutInfo_ABORTED, RolloutInfo_IN_PROGRESS, RolloutInfo_STALLED, RolloutInfo_CANCELLED, RolloutInfo_ABORTING
    
    
    const (
    	// Unspecified state.
    	RolloutInfo_STATE_UNSPECIFIED RolloutInfo_State = 0
    	// Rollout completed.
    	RolloutInfo_COMPLETED RolloutInfo_State = 1
    	// Rollout suspended.
    	RolloutInfo_SUSPENDED RolloutInfo_State = 2
    	// Rollout aborted.
    	RolloutInfo_ABORTED RolloutInfo_State = 3
    	// Rollout in progress.
    	RolloutInfo_IN_PROGRESS RolloutInfo_State = 5
    	// Rollout stalled.
    	RolloutInfo_STALLED RolloutInfo_State = 6
    	// Rollout cancelled.
    	RolloutInfo_CANCELLED RolloutInfo_State = 7
    	// Rollout aborting.
    	RolloutInfo_ABORTING RolloutInfo_State = 8
    )

### func (RolloutInfo_State) Descriptor 
    
    
    func (RolloutInfo_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RolloutInfo_State) Enum 
    
    
    func (x RolloutInfo_State) Enum() *RolloutInfo_State

### func (RolloutInfo_State) EnumDescriptor 
    
    
    func (RolloutInfo_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RolloutInfo_State.Descriptor instead.

### func (RolloutInfo_State) Number 
    
    
    func (x RolloutInfo_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RolloutInfo_State) String 
    
    
    func (x RolloutInfo_State) String() [string](https://pkg.go.dev/builtin#string)

### func (RolloutInfo_State) Type 
    
    
    func (RolloutInfo_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RolloutStrategy
    
    
    type RolloutStrategy struct {
    
    	// strategy defines how updates to a resource bundle should be rolled out
    	// across clusters.
    	//
    	// Types that are valid to be assigned to Strategy:
    	//
    	//	*RolloutStrategy_AllAtOnce
    	//	*RolloutStrategy_Rolling
    	Strategy isRolloutStrategy_Strategy `protobuf_oneof:"strategy"`
    	// contains filtered or unexported fields
    }

RolloutStrategy defines different ways to rollout a resource bundle across a set of clusters.

### func (*RolloutStrategy) Descriptor 
    
    
    func (*RolloutStrategy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RolloutStrategy.ProtoReflect.Descriptor instead.

### func (*RolloutStrategy) GetAllAtOnce 
    
    
    func (x *RolloutStrategy) GetAllAtOnce() *AllAtOnceStrategy

### func (*RolloutStrategy) GetRolling 
    
    
    func (x *RolloutStrategy) GetRolling() *RollingStrategy

### func (*RolloutStrategy) GetStrategy 
    
    
    func (x *RolloutStrategy) GetStrategy() isRolloutStrategy_Strategy

### func (*RolloutStrategy) ProtoMessage 
    
    
    func (*RolloutStrategy) ProtoMessage()

### func (*RolloutStrategy) ProtoReflect 
    
    
    func (x *RolloutStrategy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RolloutStrategy) Reset 
    
    
    func (x *RolloutStrategy) Reset()

### func (*RolloutStrategy) String 
    
    
    func (x *RolloutStrategy) String() [string](https://pkg.go.dev/builtin#string)

## RolloutStrategyInfo
    
    
    type RolloutStrategyInfo struct {
    
    	// strategy represents result of applying one of the rollout strategies.
    	//
    	// Types that are valid to be assigned to Strategy:
    	//
    	//	*RolloutStrategyInfo_AllAtOnceStrategyInfo
    	//	*RolloutStrategyInfo_RollingStrategyInfo
    	Strategy isRolloutStrategyInfo_Strategy `protobuf_oneof:"strategy"`
    	// contains filtered or unexported fields
    }

RolloutStrategyInfo represents the status of execution of different types of rollout strategies. Only the field corresponding to the rollout strategy specified at the rollout resource will be populated.

### func (*RolloutStrategyInfo) Descriptor 
    
    
    func (*RolloutStrategyInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RolloutStrategyInfo.ProtoReflect.Descriptor instead.

### func (*RolloutStrategyInfo) GetAllAtOnceStrategyInfo 
    
    
    func (x *RolloutStrategyInfo) GetAllAtOnceStrategyInfo() *AllAtOnceStrategyInfo

### func (*RolloutStrategyInfo) GetRollingStrategyInfo 
    
    
    func (x *RolloutStrategyInfo) GetRollingStrategyInfo() *RollingStrategyInfo

### func (*RolloutStrategyInfo) GetStrategy 
    
    
    func (x *RolloutStrategyInfo) GetStrategy() isRolloutStrategyInfo_Strategy

### func (*RolloutStrategyInfo) ProtoMessage 
    
    
    func (*RolloutStrategyInfo) ProtoMessage()

### func (*RolloutStrategyInfo) ProtoReflect 
    
    
    func (x *RolloutStrategyInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RolloutStrategyInfo) Reset 
    
    
    func (x *RolloutStrategyInfo) Reset()

### func (*RolloutStrategyInfo) String 
    
    
    func (x *RolloutStrategyInfo) String() [string](https://pkg.go.dev/builtin#string)

## RolloutStrategyInfo_AllAtOnceStrategyInfo
    
    
    type RolloutStrategyInfo_AllAtOnceStrategyInfo struct {
    	// AllAtOnceStrategyInfo represents the status of AllAtOnce rollout strategy
    	// execution.
    	AllAtOnceStrategyInfo *AllAtOnceStrategyInfo `protobuf:"bytes,1,opt,name=all_at_once_strategy_info,json=allAtOnceStrategyInfo,proto3,oneof"`
    }

## RolloutStrategyInfo_RollingStrategyInfo
    
    
    type RolloutStrategyInfo_RollingStrategyInfo struct {
    	// RollingStrategyInfo represents the status of Rolling rollout strategy
    	// execution.
    	RollingStrategyInfo *RollingStrategyInfo `protobuf:"bytes,2,opt,name=rolling_strategy_info,json=rollingStrategyInfo,proto3,oneof"`
    }

## RolloutStrategy_AllAtOnce
    
    
    type RolloutStrategy_AllAtOnce struct {
    	// AllAtOnceStrategy causes all clusters to be updated concurrently.
    	AllAtOnce *AllAtOnceStrategy `protobuf:"bytes,1,opt,name=all_at_once,json=allAtOnce,proto3,oneof"`
    }

## RolloutStrategy_Rolling
    
    
    type RolloutStrategy_Rolling struct {
    	// RollingStrategy causes a specified number of clusters to be updated
    	// concurrently until all clusters are updated.
    	Rolling *RollingStrategy `protobuf:"bytes,2,opt,name=rolling,proto3,oneof"`
    }

## SuspendRolloutRequest
    
    
    type SuspendRolloutRequest struct {
    
    	// Required. Name of the Rollout.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. Reason for suspension.
    	Reason [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
    	// contains filtered or unexported fields
    }

Message for suspending a rollout.

### func (*SuspendRolloutRequest) Descriptor 
    
    
    func (*SuspendRolloutRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuspendRolloutRequest.ProtoReflect.Descriptor instead.

### func (*SuspendRolloutRequest) GetName 
    
    
    func (x *SuspendRolloutRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SuspendRolloutRequest) GetReason 
    
    
    func (x *SuspendRolloutRequest) GetReason() [string](https://pkg.go.dev/builtin#string)

### func (*SuspendRolloutRequest) ProtoMessage 
    
    
    func (*SuspendRolloutRequest) ProtoMessage()

### func (*SuspendRolloutRequest) ProtoReflect 
    
    
    func (x *SuspendRolloutRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SuspendRolloutRequest) Reset 
    
    
    func (x *SuspendRolloutRequest) Reset()

### func (*SuspendRolloutRequest) String 
    
    
    func (x *SuspendRolloutRequest) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedConfigDeliveryServer
    
    
    type UnimplementedConfigDeliveryServer struct {
    }

UnimplementedConfigDeliveryServer should be embedded to have forward compatible implementations.

### func (UnimplementedConfigDeliveryServer) AbortRollout 
    
    
    func (UnimplementedConfigDeliveryServer) AbortRollout([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AbortRolloutRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) CreateFleetPackage 
    
    
    func (UnimplementedConfigDeliveryServer) CreateFleetPackage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateFleetPackageRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) CreateRelease 
    
    
    func (UnimplementedConfigDeliveryServer) CreateRelease([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateReleaseRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) CreateResourceBundle 
    
    
    func (UnimplementedConfigDeliveryServer) CreateResourceBundle([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateResourceBundleRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) CreateVariant 
    
    
    func (UnimplementedConfigDeliveryServer) CreateVariant([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateVariantRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) DeleteFleetPackage 
    
    
    func (UnimplementedConfigDeliveryServer) DeleteFleetPackage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteFleetPackageRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) DeleteRelease 
    
    
    func (UnimplementedConfigDeliveryServer) DeleteRelease([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteReleaseRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) DeleteResourceBundle 
    
    
    func (UnimplementedConfigDeliveryServer) DeleteResourceBundle([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteResourceBundleRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) DeleteVariant 
    
    
    func (UnimplementedConfigDeliveryServer) DeleteVariant([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteVariantRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) GetFleetPackage 
    
    
    func (UnimplementedConfigDeliveryServer) GetFleetPackage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetFleetPackageRequest) (*FleetPackage, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) GetRelease 
    
    
    func (UnimplementedConfigDeliveryServer) GetRelease([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetReleaseRequest) (*Release, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) GetResourceBundle 
    
    
    func (UnimplementedConfigDeliveryServer) GetResourceBundle([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetResourceBundleRequest) (*ResourceBundle, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) GetRollout 
    
    
    func (UnimplementedConfigDeliveryServer) GetRollout([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetRolloutRequest) (*Rollout, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) GetVariant 
    
    
    func (UnimplementedConfigDeliveryServer) GetVariant([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetVariantRequest) (*Variant, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ListFleetPackages 
    
    
    func (UnimplementedConfigDeliveryServer) ListFleetPackages([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListFleetPackagesRequest) (*ListFleetPackagesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ListReleases 
    
    
    func (UnimplementedConfigDeliveryServer) ListReleases([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReleasesRequest) (*ListReleasesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ListResourceBundles 
    
    
    func (UnimplementedConfigDeliveryServer) ListResourceBundles([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListResourceBundlesRequest) (*ListResourceBundlesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ListRollouts 
    
    
    func (UnimplementedConfigDeliveryServer) ListRollouts([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListRolloutsRequest) (*ListRolloutsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ListVariants 
    
    
    func (UnimplementedConfigDeliveryServer) ListVariants([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListVariantsRequest) (*ListVariantsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) ResumeRollout 
    
    
    func (UnimplementedConfigDeliveryServer) ResumeRollout([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ResumeRolloutRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) SuspendRollout 
    
    
    func (UnimplementedConfigDeliveryServer) SuspendRollout([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SuspendRolloutRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) UpdateFleetPackage 
    
    
    func (UnimplementedConfigDeliveryServer) UpdateFleetPackage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateFleetPackageRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) UpdateRelease 
    
    
    func (UnimplementedConfigDeliveryServer) UpdateRelease([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateReleaseRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) UpdateResourceBundle 
    
    
    func (UnimplementedConfigDeliveryServer) UpdateResourceBundle([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateResourceBundleRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedConfigDeliveryServer) UpdateVariant 
    
    
    func (UnimplementedConfigDeliveryServer) UpdateVariant([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateVariantRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

## UnsafeConfigDeliveryServer
    
    
    type UnsafeConfigDeliveryServer interface {
    	// contains filtered or unexported methods
    }

UnsafeConfigDeliveryServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ConfigDeliveryServer will result in compilation errors.

## UpdateFleetPackageRequest
    
    
    type UpdateFleetPackageRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// FleetPackage resource by the update.
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask. If the
    	// user does not provide a mask then all fields will be overwritten.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	FleetPackage *FleetPackage `protobuf:"bytes,2,opt,name=fleet_package,json=fleetPackage,proto3" json:"fleet_package,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for updating a FleetPackage

### func (*UpdateFleetPackageRequest) Descriptor 
    
    
    func (*UpdateFleetPackageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateFleetPackageRequest.ProtoReflect.Descriptor instead.

### func (*UpdateFleetPackageRequest) GetFleetPackage 
    
    
    func (x *UpdateFleetPackageRequest) GetFleetPackage() *FleetPackage

### func (*UpdateFleetPackageRequest) GetRequestId 
    
    
    func (x *UpdateFleetPackageRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateFleetPackageRequest) GetUpdateMask 
    
    
    func (x *UpdateFleetPackageRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateFleetPackageRequest) ProtoMessage 
    
    
    func (*UpdateFleetPackageRequest) ProtoMessage()

### func (*UpdateFleetPackageRequest) ProtoReflect 
    
    
    func (x *UpdateFleetPackageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateFleetPackageRequest) Reset 
    
    
    func (x *UpdateFleetPackageRequest) Reset()

### func (*UpdateFleetPackageRequest) String 
    
    
    func (x *UpdateFleetPackageRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateReleaseRequest
    
    
    type UpdateReleaseRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// Release resource by the update.
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask. If the
    	// user does not provide a mask then all fields will be overwritten.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	Release *Release `protobuf:"bytes,2,opt,name=release,proto3" json:"release,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for updating a Release

### func (*UpdateReleaseRequest) Descriptor 
    
    
    func (*UpdateReleaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateReleaseRequest.ProtoReflect.Descriptor instead.

### func (*UpdateReleaseRequest) GetRelease 
    
    
    func (x *UpdateReleaseRequest) GetRelease() *Release

### func (*UpdateReleaseRequest) GetRequestId 
    
    
    func (x *UpdateReleaseRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateReleaseRequest) GetUpdateMask 
    
    
    func (x *UpdateReleaseRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateReleaseRequest) ProtoMessage 
    
    
    func (*UpdateReleaseRequest) ProtoMessage()

### func (*UpdateReleaseRequest) ProtoReflect 
    
    
    func (x *UpdateReleaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateReleaseRequest) Reset 
    
    
    func (x *UpdateReleaseRequest) Reset()

### func (*UpdateReleaseRequest) String 
    
    
    func (x *UpdateReleaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateResourceBundleRequest
    
    
    type UpdateResourceBundleRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// ResourceBundle resource by the update.
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask. If the
    	// user does not provide a mask then all fields will be overwritten.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	ResourceBundle *ResourceBundle `protobuf:"bytes,2,opt,name=resource_bundle,json=resourceBundle,proto3" json:"resource_bundle,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for updating a ResourceBundle

### func (*UpdateResourceBundleRequest) Descriptor 
    
    
    func (*UpdateResourceBundleRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateResourceBundleRequest.ProtoReflect.Descriptor instead.

### func (*UpdateResourceBundleRequest) GetRequestId 
    
    
    func (x *UpdateResourceBundleRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateResourceBundleRequest) GetResourceBundle 
    
    
    func (x *UpdateResourceBundleRequest) GetResourceBundle() *ResourceBundle

### func (*UpdateResourceBundleRequest) GetUpdateMask 
    
    
    func (x *UpdateResourceBundleRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateResourceBundleRequest) ProtoMessage 
    
    
    func (*UpdateResourceBundleRequest) ProtoMessage()

### func (*UpdateResourceBundleRequest) ProtoReflect 
    
    
    func (x *UpdateResourceBundleRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateResourceBundleRequest) Reset 
    
    
    func (x *UpdateResourceBundleRequest) Reset()

### func (*UpdateResourceBundleRequest) String 
    
    
    func (x *UpdateResourceBundleRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateVariantRequest
    
    
    type UpdateVariantRequest struct {
    
    	// Optional. Field mask is used to specify the fields to be overwritten in the
    	// Variant resource by the update.
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask. If the
    	// user does not provide a mask then all fields will be overwritten.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	Variant *Variant `protobuf:"bytes,2,opt,name=variant,proto3" json:"variant,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for updating a Variant

### func (*UpdateVariantRequest) Descriptor 
    
    
    func (*UpdateVariantRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateVariantRequest.ProtoReflect.Descriptor instead.

### func (*UpdateVariantRequest) GetRequestId 
    
    
    func (x *UpdateVariantRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateVariantRequest) GetUpdateMask 
    
    
    func (x *UpdateVariantRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateVariantRequest) GetVariant 
    
    
    func (x *UpdateVariantRequest) GetVariant() *Variant

### func (*UpdateVariantRequest) ProtoMessage 
    
    
    func (*UpdateVariantRequest) ProtoMessage()

### func (*UpdateVariantRequest) ProtoReflect 
    
    
    func (x *UpdateVariantRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateVariantRequest) Reset 
    
    
    func (x *UpdateVariantRequest) Reset()

### func (*UpdateVariantRequest) String 
    
    
    func (x *UpdateVariantRequest) String() [string](https://pkg.go.dev/builtin#string)

## Variant
    
    
    type Variant struct {
    
    	// Optional. labels to represent any metadata associated with the variant.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Input only. Unordered list. resources contain the kubernetes
    	// manifests (YAMLs) for this variant.
    	Resources [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=resources,proto3" json:"resources,omitempty"`
    	// Identifier. Name follows format of
    	// projects/{project}/locations/{location}/resourceBundles/{resource_bundle}/releases/{release}/variants/{variant}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. [Output only] Create time stamp
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. [Output only] Update time stamp
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// contains filtered or unexported fields
    }

Variant represents the content of a `ResourceBundle` variant.

### func (*Variant) Descriptor 
    
    
    func (*Variant) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Variant.ProtoReflect.Descriptor instead.

### func (*Variant) GetCreateTime 
    
    
    func (x *Variant) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Variant) GetLabels 
    
    
    func (x *Variant) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Variant) GetName 
    
    
    func (x *Variant) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Variant) GetResources 
    
    
    func (x *Variant) GetResources() [][string](https://pkg.go.dev/builtin#string)

### func (*Variant) GetUpdateTime 
    
    
    func (x *Variant) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Variant) ProtoMessage 
    
    
    func (*Variant) ProtoMessage()

### func (*Variant) ProtoReflect 
    
    
    func (x *Variant) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Variant) Reset 
    
    
    func (x *Variant) Reset()

### func (*Variant) String 
    
    
    func (x *Variant) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
