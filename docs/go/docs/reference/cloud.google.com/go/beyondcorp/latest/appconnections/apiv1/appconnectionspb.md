---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appconnections/apiv1/appconnectionspb/
title: BeyondCorp AppConnections API v1 - Package cloud.google.com/go/beyondcorp/appconnections/apiv1/appconnectionspb (v1.10.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:33.326449+00:00
---

# BeyondCorp AppConnections API v1 - Package cloud.google.com/go/beyondcorp/appconnections/apiv1/appconnectionspb (v1.10.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appconnections/apiv1/appconnectionspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  BeyondCorp AppConnections API v1 - Package cloud.google.com/go/beyondcorp/appconnections/apiv1/appconnectionspb (v1.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.0 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.6  1.0.11  0.6.1  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/beyondcorp/appconnections/apiv1/appconnectionspb). 

##  Constants 

### AppConnectionsService_ListAppConnections_FullMethodName, AppConnectionsService_GetAppConnection_FullMethodName, AppConnectionsService_CreateAppConnection_FullMethodName, AppConnectionsService_UpdateAppConnection_FullMethodName, AppConnectionsService_DeleteAppConnection_FullMethodName, AppConnectionsService_ResolveAppConnections_FullMethodName
    
    
    const (
    	AppConnectionsService_ListAppConnections_FullMethodName    = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/ListAppConnections"
    	AppConnectionsService_GetAppConnection_FullMethodName      = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/GetAppConnection"
    	AppConnectionsService_CreateAppConnection_FullMethodName   = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/CreateAppConnection"
    	AppConnectionsService_UpdateAppConnection_FullMethodName   = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/UpdateAppConnection"
    	AppConnectionsService_DeleteAppConnection_FullMethodName   = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/DeleteAppConnection"
    	AppConnectionsService_ResolveAppConnections_FullMethodName = "/google.cloud.beyondcorp.appconnections.v1.AppConnectionsService/ResolveAppConnections"
    )

## Variables 

### AppConnection_Type_name, AppConnection_Type_value
    
    
    var (
    	AppConnection_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "TCP_PROXY",
    	}
    	AppConnection_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"TCP_PROXY":        1,
    	}
    )

Enum value maps for AppConnection_Type.

### AppConnection_State_name, AppConnection_State_value
    
    
    var (
    	AppConnection_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "CREATING",
    		2: "CREATED",
    		3: "UPDATING",
    		4: "DELETING",
    		5: "DOWN",
    	}
    	AppConnection_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"CREATING":          1,
    		"CREATED":           2,
    		"UPDATING":          3,
    		"DELETING":          4,
    		"DOWN":              5,
    	}
    )

Enum value maps for AppConnection_State.

### AppConnection_Gateway_Type_name, AppConnection_Gateway_Type_value
    
    
    var (
    	AppConnection_Gateway_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "GCP_REGIONAL_MIG",
    	}
    	AppConnection_Gateway_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"GCP_REGIONAL_MIG": 1,
    	}
    )

Enum value maps for AppConnection_Gateway_Type.

### AppConnectionsService_ServiceDesc
    
    
    var AppConnectionsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.beyondcorp.appconnections.v1.AppConnectionsService",
    	HandlerType: (*AppConnectionsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListAppConnections",
    			Handler:    _AppConnectionsService_ListAppConnections_Handler,
    		},
    		{
    			MethodName: "GetAppConnection",
    			Handler:    _AppConnectionsService_GetAppConnection_Handler,
    		},
    		{
    			MethodName: "CreateAppConnection",
    			Handler:    _AppConnectionsService_CreateAppConnection_Handler,
    		},
    		{
    			MethodName: "UpdateAppConnection",
    			Handler:    _AppConnectionsService_UpdateAppConnection_Handler,
    		},
    		{
    			MethodName: "DeleteAppConnection",
    			Handler:    _AppConnectionsService_DeleteAppConnection_Handler,
    		},
    		{
    			MethodName: "ResolveAppConnections",
    			Handler:    _AppConnectionsService_ResolveAppConnections_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/beyondcorp/appconnections/v1/app_connections_service.proto",
    }

AppConnectionsService_ServiceDesc is the grpc.ServiceDesc for AppConnectionsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_beyondcorp_appconnections_v1_app_connections_service_proto
    
    
    var File_google_cloud_beyondcorp_appconnections_v1_app_connections_service_proto protoreflect.FileDescriptor

## Functions 

### func RegisterAppConnectionsServiceServer 
    
    
    func RegisterAppConnectionsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AppConnectionsServiceServer)

Deprecated: Do not use.

## AppConnection
    
    
    type AppConnection struct {
    
    	// Required. Unique resource name of the AppConnection.
    	// The name is ignored when creating a AppConnection.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Timestamp when the resource was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Timestamp when the resource was last modified.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Optional. Resource labels to represent user provided metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Optional. An arbitrary user-provided name for the AppConnection. Cannot
    	// exceed 64 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. A unique identifier for the instance generated by the
    	// system.
    	Uid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=uid,proto3" json:"uid,omitempty"`
    	// Required. The type of network connectivity used by the AppConnection.
    	Type AppConnection_Type `protobuf:"varint,7,opt,name=type,proto3,enum=google.cloud.beyondcorp.appconnections.v1.AppConnection_Type" json:"type,omitempty"`
    	// Required. Address of the remote application endpoint for the BeyondCorp
    	// AppConnection.
    	ApplicationEndpoint *AppConnection_ApplicationEndpoint `protobuf:"bytes,8,opt,name=application_endpoint,json=applicationEndpoint,proto3" json:"application_endpoint,omitempty"`
    	// Optional. List of [google.cloud.beyondcorp.v1main.Connector.name] that are
    	// authorized to be associated with this AppConnection.
    	Connectors [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,rep,name=connectors,proto3" json:"connectors,omitempty"`
    	// Output only. The current state of the AppConnection.
    	State AppConnection_State `protobuf:"varint,10,opt,name=state,proto3,enum=google.cloud.beyondcorp.appconnections.v1.AppConnection_State" json:"state,omitempty"`
    	// Optional. Gateway used by the AppConnection.
    	Gateway *AppConnection_Gateway `protobuf:"bytes,11,opt,name=gateway,proto3" json:"gateway,omitempty"`
    	// Output only. Reserved for future use.
    	SatisfiesPzs *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=satisfies_pzs,json=satisfiesPzs,proto3,oneof" json:"satisfies_pzs,omitempty"`
    	// Output only. Reserved for future use.
    	SatisfiesPzi *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,13,opt,name=satisfies_pzi,json=satisfiesPzi,proto3,oneof" json:"satisfies_pzi,omitempty"`
    	// contains filtered or unexported fields
    }

A BeyondCorp AppConnection resource represents a BeyondCorp protected AppConnection to a remote application. It creates all the necessary GCP components needed for creating a BeyondCorp protected AppConnection. Multiple connectors can be authorized for a single AppConnection.

### func (*AppConnection) Descriptor 
    
    
    func (*AppConnection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection.ProtoReflect.Descriptor instead.

### func (*AppConnection) GetApplicationEndpoint 
    
    
    func (x *AppConnection) GetApplicationEndpoint() *AppConnection_ApplicationEndpoint

### func (*AppConnection) GetConnectors 
    
    
    func (x *AppConnection) GetConnectors() [][string](https://pkg.go.dev/builtin#string)

### func (*AppConnection) GetCreateTime 
    
    
    func (x *AppConnection) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AppConnection) GetDisplayName 
    
    
    func (x *AppConnection) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection) GetGateway 
    
    
    func (x *AppConnection) GetGateway() *AppConnection_Gateway

### func (*AppConnection) GetLabels 
    
    
    func (x *AppConnection) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*AppConnection) GetName 
    
    
    func (x *AppConnection) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection) GetSatisfiesPzi 
    
    
    func (x *AppConnection) GetSatisfiesPzi() [bool](https://pkg.go.dev/builtin#bool)

### func (*AppConnection) GetSatisfiesPzs 
    
    
    func (x *AppConnection) GetSatisfiesPzs() [bool](https://pkg.go.dev/builtin#bool)

### func (*AppConnection) GetState 
    
    
    func (x *AppConnection) GetState() AppConnection_State

### func (*AppConnection) GetType 
    
    
    func (x *AppConnection) GetType() AppConnection_Type

### func (*AppConnection) GetUid 
    
    
    func (x *AppConnection) GetUid() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection) GetUpdateTime 
    
    
    func (x *AppConnection) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AppConnection) ProtoMessage 
    
    
    func (*AppConnection) ProtoMessage()

### func (*AppConnection) ProtoReflect 
    
    
    func (x *AppConnection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AppConnection) Reset 
    
    
    func (x *AppConnection) Reset()

### func (*AppConnection) String 
    
    
    func (x *AppConnection) String() [string](https://pkg.go.dev/builtin#string)

## AppConnectionOperationMetadata
    
    
    type AppConnectionOperationMetadata struct {
    
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
    	// of the operation. Operations that have successfully been cancelled
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

### func (*AppConnectionOperationMetadata) Descriptor 
    
    
    func (*AppConnectionOperationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnectionOperationMetadata.ProtoReflect.Descriptor instead.

### func (*AppConnectionOperationMetadata) GetApiVersion 
    
    
    func (x *AppConnectionOperationMetadata) GetApiVersion() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnectionOperationMetadata) GetCreateTime 
    
    
    func (x *AppConnectionOperationMetadata) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AppConnectionOperationMetadata) GetEndTime 
    
    
    func (x *AppConnectionOperationMetadata) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AppConnectionOperationMetadata) GetRequestedCancellation 
    
    
    func (x *AppConnectionOperationMetadata) GetRequestedCancellation() [bool](https://pkg.go.dev/builtin#bool)

### func (*AppConnectionOperationMetadata) GetStatusMessage 
    
    
    func (x *AppConnectionOperationMetadata) GetStatusMessage() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnectionOperationMetadata) GetTarget 
    
    
    func (x *AppConnectionOperationMetadata) GetTarget() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnectionOperationMetadata) GetVerb 
    
    
    func (x *AppConnectionOperationMetadata) GetVerb() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnectionOperationMetadata) ProtoMessage 
    
    
    func (*AppConnectionOperationMetadata) ProtoMessage()

### func (*AppConnectionOperationMetadata) ProtoReflect 
    
    
    func (x *AppConnectionOperationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AppConnectionOperationMetadata) Reset 
    
    
    func (x *AppConnectionOperationMetadata) Reset()

### func (*AppConnectionOperationMetadata) String 
    
    
    func (x *AppConnectionOperationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## AppConnection_ApplicationEndpoint
    
    
    type AppConnection_ApplicationEndpoint struct {
    
    	// Required. Hostname or IP address of the remote application endpoint.
    	Host [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=host,proto3" json:"host,omitempty"`
    	// Required. Port of the remote application endpoint.
    	Port [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=port,proto3" json:"port,omitempty"`
    	// contains filtered or unexported fields
    }

ApplicationEndpoint represents a remote application endpoint.

### func (*AppConnection_ApplicationEndpoint) Descriptor 
    
    
    func (*AppConnection_ApplicationEndpoint) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection_ApplicationEndpoint.ProtoReflect.Descriptor instead.

### func (*AppConnection_ApplicationEndpoint) GetHost 
    
    
    func (x *AppConnection_ApplicationEndpoint) GetHost() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection_ApplicationEndpoint) GetPort 
    
    
    func (x *AppConnection_ApplicationEndpoint) GetPort() [int32](https://pkg.go.dev/builtin#int32)

### func (*AppConnection_ApplicationEndpoint) ProtoMessage 
    
    
    func (*AppConnection_ApplicationEndpoint) ProtoMessage()

### func (*AppConnection_ApplicationEndpoint) ProtoReflect 
    
    
    func (x *AppConnection_ApplicationEndpoint) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AppConnection_ApplicationEndpoint) Reset 
    
    
    func (x *AppConnection_ApplicationEndpoint) Reset()

### func (*AppConnection_ApplicationEndpoint) String 
    
    
    func (x *AppConnection_ApplicationEndpoint) String() [string](https://pkg.go.dev/builtin#string)

## AppConnection_Gateway
    
    
    type AppConnection_Gateway struct {
    
    	// Required. The type of hosting used by the gateway.
    	Type AppConnection_Gateway_Type `protobuf:"varint,2,opt,name=type,proto3,enum=google.cloud.beyondcorp.appconnections.v1.AppConnection_Gateway_Type" json:"type,omitempty"`
    	// Output only. Server-defined URI for this resource.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Output only. Ingress port reserved on the gateways for this
    	// AppConnection, if not specified or zero, the default port is 19443.
    	IngressPort [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=ingress_port,json=ingressPort,proto3" json:"ingress_port,omitempty"`
    	// Required. AppGateway name in following format:
    	// `projects/{project_id}/locations/{location_id}/appgateways/{gateway_id}`
    	AppGateway [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=app_gateway,json=appGateway,proto3" json:"app_gateway,omitempty"`
    	// Output only. L7 private service connection for this resource.
    	L7Psc [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=l7psc,proto3" json:"l7psc,omitempty"`
    	// contains filtered or unexported fields
    }

Gateway represents a user facing component that serves as an entrance to enable connectivity.

### func (*AppConnection_Gateway) Descriptor 
    
    
    func (*AppConnection_Gateway) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection_Gateway.ProtoReflect.Descriptor instead.

### func (*AppConnection_Gateway) GetAppGateway 
    
    
    func (x *AppConnection_Gateway) GetAppGateway() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection_Gateway) GetIngressPort 
    
    
    func (x *AppConnection_Gateway) GetIngressPort() [int32](https://pkg.go.dev/builtin#int32)

### func (*AppConnection_Gateway) GetL7Psc 
    
    
    func (x *AppConnection_Gateway) GetL7Psc() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection_Gateway) GetType 
    
    
    func (x *AppConnection_Gateway) GetType() AppConnection_Gateway_Type

### func (*AppConnection_Gateway) GetUri 
    
    
    func (x *AppConnection_Gateway) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*AppConnection_Gateway) ProtoMessage 
    
    
    func (*AppConnection_Gateway) ProtoMessage()

### func (*AppConnection_Gateway) ProtoReflect 
    
    
    func (x *AppConnection_Gateway) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AppConnection_Gateway) Reset 
    
    
    func (x *AppConnection_Gateway) Reset()

### func (*AppConnection_Gateway) String 
    
    
    func (x *AppConnection_Gateway) String() [string](https://pkg.go.dev/builtin#string)

## AppConnection_Gateway_Type
    
    
    type AppConnection_Gateway_Type [int32](https://pkg.go.dev/builtin#int32)

Enum listing possible gateway hosting options.

### AppConnection_Gateway_TYPE_UNSPECIFIED, AppConnection_Gateway_GCP_REGIONAL_MIG
    
    
    const (
    	// Default value. This value is unused.
    	AppConnection_Gateway_TYPE_UNSPECIFIED AppConnection_Gateway_Type = 0
    	// Gateway hosted in a GCP regional managed instance group.
    	AppConnection_Gateway_GCP_REGIONAL_MIG AppConnection_Gateway_Type = 1
    )

### func (AppConnection_Gateway_Type) Descriptor 
    
    
    func (AppConnection_Gateway_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AppConnection_Gateway_Type) Enum 
    
    
    func (x AppConnection_Gateway_Type) Enum() *AppConnection_Gateway_Type

### func (AppConnection_Gateway_Type) EnumDescriptor 
    
    
    func (AppConnection_Gateway_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection_Gateway_Type.Descriptor instead.

### func (AppConnection_Gateway_Type) Number 
    
    
    func (x AppConnection_Gateway_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AppConnection_Gateway_Type) String 
    
    
    func (x AppConnection_Gateway_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (AppConnection_Gateway_Type) Type 
    
    
    func (AppConnection_Gateway_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AppConnection_State
    
    
    type AppConnection_State [int32](https://pkg.go.dev/builtin#int32)

Represents the different states of a AppConnection.

### AppConnection_STATE_UNSPECIFIED, AppConnection_CREATING, AppConnection_CREATED, AppConnection_UPDATING, AppConnection_DELETING, AppConnection_DOWN
    
    
    const (
    	// Default value. This value is unused.
    	AppConnection_STATE_UNSPECIFIED AppConnection_State = 0
    	// AppConnection is being created.
    	AppConnection_CREATING AppConnection_State = 1
    	// AppConnection has been created.
    	AppConnection_CREATED AppConnection_State = 2
    	// AppConnection's configuration is being updated.
    	AppConnection_UPDATING AppConnection_State = 3
    	// AppConnection is being deleted.
    	AppConnection_DELETING AppConnection_State = 4
    	// AppConnection is down and may be restored in the future.
    	// This happens when CCFE sends ProjectState = OFF.
    	AppConnection_DOWN AppConnection_State = 5
    )

### func (AppConnection_State) Descriptor 
    
    
    func (AppConnection_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AppConnection_State) Enum 
    
    
    func (x AppConnection_State) Enum() *AppConnection_State

### func (AppConnection_State) EnumDescriptor 
    
    
    func (AppConnection_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection_State.Descriptor instead.

### func (AppConnection_State) Number 
    
    
    func (x AppConnection_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AppConnection_State) String 
    
    
    func (x AppConnection_State) String() [string](https://pkg.go.dev/builtin#string)

### func (AppConnection_State) Type 
    
    
    func (AppConnection_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AppConnection_Type
    
    
    type AppConnection_Type [int32](https://pkg.go.dev/builtin#int32)

Enum containing list of all possible network connectivity options supported by BeyondCorp AppConnection.

### AppConnection_TYPE_UNSPECIFIED, AppConnection_TCP_PROXY
    
    
    const (
    	// Default value. This value is unused.
    	AppConnection_TYPE_UNSPECIFIED AppConnection_Type = 0
    	// TCP Proxy based BeyondCorp AppConnection. API will default to this if
    	// unset.
    	AppConnection_TCP_PROXY AppConnection_Type = 1
    )

### func (AppConnection_Type) Descriptor 
    
    
    func (AppConnection_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AppConnection_Type) Enum 
    
    
    func (x AppConnection_Type) Enum() *AppConnection_Type

### func (AppConnection_Type) EnumDescriptor 
    
    
    func (AppConnection_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AppConnection_Type.Descriptor instead.

### func (AppConnection_Type) Number 
    
    
    func (x AppConnection_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AppConnection_Type) String 
    
    
    func (x AppConnection_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (AppConnection_Type) Type 
    
    
    func (AppConnection_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AppConnectionsServiceClient (deprecated)
    
    
    type AppConnectionsServiceClient interface {
    	// Deprecated: Do not use.
    	// Lists AppConnections in a given project and location.
    	ListAppConnections(ctx context.Context, in *ListAppConnectionsRequest, opts ...grpc.CallOption) (*ListAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Gets details of a single AppConnection.
    	GetAppConnection(ctx context.Context, in *GetAppConnectionRequest, opts ...grpc.CallOption) (*AppConnection, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Creates a new AppConnection in a given project and location.
    	CreateAppConnection(ctx context.Context, in *CreateAppConnectionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Updates the parameters of a single AppConnection.
    	UpdateAppConnection(ctx context.Context, in *UpdateAppConnectionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Deletes a single AppConnection.
    	DeleteAppConnection(ctx context.Context, in *DeleteAppConnectionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Resolves AppConnections details for a given AppConnector.
    	// An internal method called by a connector to find AppConnections to connect
    	// to.
    	ResolveAppConnections(ctx context.Context, in *ResolveAppConnectionsRequest, opts ...grpc.CallOption) (*ResolveAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AppConnectionsServiceClient is the client API for AppConnectionsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

Deprecated: Do not use.

### func NewAppConnectionsServiceClient (deprecated)
    
    
    func NewAppConnectionsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AppConnectionsServiceClient

Deprecated: Do not use.

## AppConnectionsServiceServer (deprecated)
    
    
    type AppConnectionsServiceServer interface {
    	// Deprecated: Do not use.
    	// Lists AppConnections in a given project and location.
    	ListAppConnections(context.Context, *ListAppConnectionsRequest) (*ListAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Gets details of a single AppConnection.
    	GetAppConnection(context.Context, *GetAppConnectionRequest) (*AppConnection, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Creates a new AppConnection in a given project and location.
    	CreateAppConnection(context.Context, *CreateAppConnectionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Updates the parameters of a single AppConnection.
    	UpdateAppConnection(context.Context, *UpdateAppConnectionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Deletes a single AppConnection.
    	DeleteAppConnection(context.Context, *DeleteAppConnectionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deprecated: Do not use.
    	// Resolves AppConnections details for a given AppConnector.
    	// An internal method called by a connector to find AppConnections to connect
    	// to.
    	ResolveAppConnections(context.Context, *ResolveAppConnectionsRequest) (*ResolveAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AppConnectionsServiceServer is the server API for AppConnectionsService service. All implementations should embed UnimplementedAppConnectionsServiceServer for forward compatibility

Deprecated: Do not use.

## CreateAppConnectionRequest
    
    
    type CreateAppConnectionRequest struct {
    
    	// Required. The resource project name of the AppConnection location using the
    	// form: `projects/{project_id}/locations/{location_id}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. User-settable AppConnection resource ID.
    	//   - Must start with a letter.
    	//   - Must contain between 4-63 characters from `/[a-z][0-9]-/`.
    	//   - Must end with a number or a letter.
    	AppConnectionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=app_connection_id,json=appConnectionId,proto3" json:"app_connection_id,omitempty"`
    	// Required. A BeyondCorp AppConnection resource.
    	AppConnection *AppConnection `protobuf:"bytes,3,opt,name=app_connection,json=appConnection,proto3" json:"app_connection,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if the original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set, validates request by executing a dry-run which would not
    	// alter the resource in any way.
    	ValidateOnly [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=validate_only,json=validateOnly,proto3" json:"validate_only,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.CreateAppConnection.

### func (*CreateAppConnectionRequest) Descriptor 
    
    
    func (*CreateAppConnectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAppConnectionRequest.ProtoReflect.Descriptor instead.

### func (*CreateAppConnectionRequest) GetAppConnection 
    
    
    func (x *CreateAppConnectionRequest) GetAppConnection() *AppConnection

### func (*CreateAppConnectionRequest) GetAppConnectionId 
    
    
    func (x *CreateAppConnectionRequest) GetAppConnectionId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAppConnectionRequest) GetParent 
    
    
    func (x *CreateAppConnectionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAppConnectionRequest) GetRequestId 
    
    
    func (x *CreateAppConnectionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAppConnectionRequest) GetValidateOnly 
    
    
    func (x *CreateAppConnectionRequest) GetValidateOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*CreateAppConnectionRequest) ProtoMessage 
    
    
    func (*CreateAppConnectionRequest) ProtoMessage()

### func (*CreateAppConnectionRequest) ProtoReflect 
    
    
    func (x *CreateAppConnectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAppConnectionRequest) Reset 
    
    
    func (x *CreateAppConnectionRequest) Reset()

### func (*CreateAppConnectionRequest) String 
    
    
    func (x *CreateAppConnectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteAppConnectionRequest
    
    
    type DeleteAppConnectionRequest struct {
    
    	// Required. BeyondCorp Connector name using the form:
    	// `projects/{project_id}/locations/{location_id}/appConnections/{app_connection_id}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if the original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set, validates request by executing a dry-run which would not
    	// alter the resource in any way.
    	ValidateOnly [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=validate_only,json=validateOnly,proto3" json:"validate_only,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.DeleteAppConnection.

### func (*DeleteAppConnectionRequest) Descriptor 
    
    
    func (*DeleteAppConnectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteAppConnectionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteAppConnectionRequest) GetName 
    
    
    func (x *DeleteAppConnectionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAppConnectionRequest) GetRequestId 
    
    
    func (x *DeleteAppConnectionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAppConnectionRequest) GetValidateOnly 
    
    
    func (x *DeleteAppConnectionRequest) GetValidateOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteAppConnectionRequest) ProtoMessage 
    
    
    func (*DeleteAppConnectionRequest) ProtoMessage()

### func (*DeleteAppConnectionRequest) ProtoReflect 
    
    
    func (x *DeleteAppConnectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteAppConnectionRequest) Reset 
    
    
    func (x *DeleteAppConnectionRequest) Reset()

### func (*DeleteAppConnectionRequest) String 
    
    
    func (x *DeleteAppConnectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAppConnectionRequest
    
    
    type GetAppConnectionRequest struct {
    
    	// Required. BeyondCorp AppConnection name using the form:
    	// `projects/{project_id}/locations/{location_id}/appConnections/{app_connection_id}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.GetAppConnection.

### func (*GetAppConnectionRequest) Descriptor 
    
    
    func (*GetAppConnectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAppConnectionRequest.ProtoReflect.Descriptor instead.

### func (*GetAppConnectionRequest) GetName 
    
    
    func (x *GetAppConnectionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAppConnectionRequest) ProtoMessage 
    
    
    func (*GetAppConnectionRequest) ProtoMessage()

### func (*GetAppConnectionRequest) ProtoReflect 
    
    
    func (x *GetAppConnectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAppConnectionRequest) Reset 
    
    
    func (x *GetAppConnectionRequest) Reset()

### func (*GetAppConnectionRequest) String 
    
    
    func (x *GetAppConnectionRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAppConnectionsRequest
    
    
    type ListAppConnectionsRequest struct {
    
    	// Required. The resource name of the AppConnection location using the form:
    	// `projects/{project_id}/locations/{location_id}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of items to return.
    	// If not specified, a default value of 50 will be used by the service.
    	// Regardless of the page_size value, the response may include a partial list
    	// and a caller should only rely on response's
    	// [next_page_token][google.cloud.beyondcorp.appconnections.v1.ListAppConnectionsResponse.next_page_token]
    	// to determine if there are more instances left to be queried.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The next_page_token value returned from a previous
    	// ListAppConnectionsRequest, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A filter specifying constraints of a list operation.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Specifies the ordering of results. See
    	// [Sorting
    	// order](https://cloud.google.com/apis/design/design_patterns#sorting_order)
    	// for more information.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.ListAppConnections.

### func (*ListAppConnectionsRequest) Descriptor 
    
    
    func (*ListAppConnectionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAppConnectionsRequest.ProtoReflect.Descriptor instead.

### func (*ListAppConnectionsRequest) GetFilter 
    
    
    func (x *ListAppConnectionsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsRequest) GetOrderBy 
    
    
    func (x *ListAppConnectionsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsRequest) GetPageSize 
    
    
    func (x *ListAppConnectionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAppConnectionsRequest) GetPageToken 
    
    
    func (x *ListAppConnectionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsRequest) GetParent 
    
    
    func (x *ListAppConnectionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsRequest) ProtoMessage 
    
    
    func (*ListAppConnectionsRequest) ProtoMessage()

### func (*ListAppConnectionsRequest) ProtoReflect 
    
    
    func (x *ListAppConnectionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAppConnectionsRequest) Reset 
    
    
    func (x *ListAppConnectionsRequest) Reset()

### func (*ListAppConnectionsRequest) String 
    
    
    func (x *ListAppConnectionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAppConnectionsResponse
    
    
    type ListAppConnectionsResponse struct {
    
    	// A list of BeyondCorp AppConnections in the project.
    	AppConnections []*AppConnection `protobuf:"bytes,1,rep,name=app_connections,json=appConnections,proto3" json:"app_connections,omitempty"`
    	// A token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// A list of locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for BeyondCorp.ListAppConnections.

### func (*ListAppConnectionsResponse) Descriptor 
    
    
    func (*ListAppConnectionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAppConnectionsResponse.ProtoReflect.Descriptor instead.

### func (*ListAppConnectionsResponse) GetAppConnections 
    
    
    func (x *ListAppConnectionsResponse) GetAppConnections() []*AppConnection

### func (*ListAppConnectionsResponse) GetNextPageToken 
    
    
    func (x *ListAppConnectionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsResponse) GetUnreachable 
    
    
    func (x *ListAppConnectionsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListAppConnectionsResponse) ProtoMessage 
    
    
    func (*ListAppConnectionsResponse) ProtoMessage()

### func (*ListAppConnectionsResponse) ProtoReflect 
    
    
    func (x *ListAppConnectionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAppConnectionsResponse) Reset 
    
    
    func (x *ListAppConnectionsResponse) Reset()

### func (*ListAppConnectionsResponse) String 
    
    
    func (x *ListAppConnectionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ResolveAppConnectionsRequest
    
    
    type ResolveAppConnectionsRequest struct {
    
    	// Required. The resource name of the AppConnection location using the form:
    	// `projects/{project_id}/locations/{location_id}`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. BeyondCorp Connector name of the connector associated with those
    	// AppConnections using the form:
    	// `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}`
    	AppConnectorId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=app_connector_id,json=appConnectorId,proto3" json:"app_connector_id,omitempty"`
    	// Optional. The maximum number of items to return.
    	// If not specified, a default value of 50 will be used by the service.
    	// Regardless of the page_size value, the response may include a partial list
    	// and a caller should only rely on response's
    	// [next_page_token][google.cloud.beyondcorp.appconnections.v1.ResolveAppConnectionsResponse.next_page_token]
    	// to determine if there are more instances left to be queried.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The next_page_token value returned from a previous
    	// ResolveAppConnectionsResponse, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.ResolveAppConnections.

### func (*ResolveAppConnectionsRequest) Descriptor 
    
    
    func (*ResolveAppConnectionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResolveAppConnectionsRequest.ProtoReflect.Descriptor instead.

### func (*ResolveAppConnectionsRequest) GetAppConnectorId 
    
    
    func (x *ResolveAppConnectionsRequest) GetAppConnectorId() [string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsRequest) GetPageSize 
    
    
    func (x *ResolveAppConnectionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ResolveAppConnectionsRequest) GetPageToken 
    
    
    func (x *ResolveAppConnectionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsRequest) GetParent 
    
    
    func (x *ResolveAppConnectionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsRequest) ProtoMessage 
    
    
    func (*ResolveAppConnectionsRequest) ProtoMessage()

### func (*ResolveAppConnectionsRequest) ProtoReflect 
    
    
    func (x *ResolveAppConnectionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResolveAppConnectionsRequest) Reset 
    
    
    func (x *ResolveAppConnectionsRequest) Reset()

### func (*ResolveAppConnectionsRequest) String 
    
    
    func (x *ResolveAppConnectionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ResolveAppConnectionsResponse
    
    
    type ResolveAppConnectionsResponse struct {
    
    	// A list of BeyondCorp AppConnections with details in the project.
    	AppConnectionDetails []*ResolveAppConnectionsResponse_AppConnectionDetails `protobuf:"bytes,1,rep,name=app_connection_details,json=appConnectionDetails,proto3" json:"app_connection_details,omitempty"`
    	// A token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// A list of locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for BeyondCorp.ResolveAppConnections.

### func (*ResolveAppConnectionsResponse) Descriptor 
    
    
    func (*ResolveAppConnectionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResolveAppConnectionsResponse.ProtoReflect.Descriptor instead.

### func (*ResolveAppConnectionsResponse) GetAppConnectionDetails 
    
    
    func (x *ResolveAppConnectionsResponse) GetAppConnectionDetails() []*ResolveAppConnectionsResponse_AppConnectionDetails

### func (*ResolveAppConnectionsResponse) GetNextPageToken 
    
    
    func (x *ResolveAppConnectionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsResponse) GetUnreachable 
    
    
    func (x *ResolveAppConnectionsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsResponse) ProtoMessage 
    
    
    func (*ResolveAppConnectionsResponse) ProtoMessage()

### func (*ResolveAppConnectionsResponse) ProtoReflect 
    
    
    func (x *ResolveAppConnectionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResolveAppConnectionsResponse) Reset 
    
    
    func (x *ResolveAppConnectionsResponse) Reset()

### func (*ResolveAppConnectionsResponse) String 
    
    
    func (x *ResolveAppConnectionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ResolveAppConnectionsResponse_AppConnectionDetails
    
    
    type ResolveAppConnectionsResponse_AppConnectionDetails struct {
    
    	// A BeyondCorp AppConnection in the project.
    	AppConnection *AppConnection `protobuf:"bytes,1,opt,name=app_connection,json=appConnection,proto3" json:"app_connection,omitempty"`
    	// If type=GCP_REGIONAL_MIG, contains most recent VM instances, like
    	// `https://www.googleapis.com/compute/v1/projects/{project_id}/zones/{zone_id}/instances/{instance_id}`.
    	RecentMigVms [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=recent_mig_vms,json=recentMigVms,proto3" json:"recent_mig_vms,omitempty"`
    	// contains filtered or unexported fields
    }

Details of the AppConnection.

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) Descriptor 
    
    
    func (*ResolveAppConnectionsResponse_AppConnectionDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResolveAppConnectionsResponse_AppConnectionDetails.ProtoReflect.Descriptor instead.

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) GetAppConnection 
    
    
    func (x *ResolveAppConnectionsResponse_AppConnectionDetails) GetAppConnection() *AppConnection

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) GetRecentMigVms 
    
    
    func (x *ResolveAppConnectionsResponse_AppConnectionDetails) GetRecentMigVms() [][string](https://pkg.go.dev/builtin#string)

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) ProtoMessage 
    
    
    func (*ResolveAppConnectionsResponse_AppConnectionDetails) ProtoMessage()

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) ProtoReflect 
    
    
    func (x *ResolveAppConnectionsResponse_AppConnectionDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) Reset 
    
    
    func (x *ResolveAppConnectionsResponse_AppConnectionDetails) Reset()

### func (*ResolveAppConnectionsResponse_AppConnectionDetails) String 
    
    
    func (x *ResolveAppConnectionsResponse_AppConnectionDetails) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedAppConnectionsServiceServer
    
    
    type UnimplementedAppConnectionsServiceServer struct {
    }

UnimplementedAppConnectionsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAppConnectionsServiceServer) CreateAppConnection 
    
    
    func (UnimplementedAppConnectionsServiceServer) CreateAppConnection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateAppConnectionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAppConnectionsServiceServer) DeleteAppConnection 
    
    
    func (UnimplementedAppConnectionsServiceServer) DeleteAppConnection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteAppConnectionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAppConnectionsServiceServer) GetAppConnection 
    
    
    func (UnimplementedAppConnectionsServiceServer) GetAppConnection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAppConnectionRequest) (*AppConnection, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAppConnectionsServiceServer) ListAppConnections 
    
    
    func (UnimplementedAppConnectionsServiceServer) ListAppConnections([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAppConnectionsRequest) (*ListAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAppConnectionsServiceServer) ResolveAppConnections 
    
    
    func (UnimplementedAppConnectionsServiceServer) ResolveAppConnections([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ResolveAppConnectionsRequest) (*ResolveAppConnectionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAppConnectionsServiceServer) UpdateAppConnection 
    
    
    func (UnimplementedAppConnectionsServiceServer) UpdateAppConnection([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAppConnectionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

## UnsafeAppConnectionsServiceServer
    
    
    type UnsafeAppConnectionsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAppConnectionsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AppConnectionsServiceServer will result in compilation errors.

## UpdateAppConnectionRequest
    
    
    type UpdateAppConnectionRequest struct {
    
    	// Required. Mask of fields to update. At least one path must be supplied in
    	// this field. The elements of the repeated paths field may only include these
    	// fields from [BeyondCorp.AppConnection]:
    	// * `labels`
    	// * `display_name`
    	// * `application_endpoint`
    	// * `connectors`
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. AppConnection message with updated fields. Only supported fields
    	// specified in update_mask are updated.
    	AppConnection *AppConnection `protobuf:"bytes,2,opt,name=app_connection,json=appConnection,proto3" json:"app_connection,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if the original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set, validates request by executing a dry-run which would not
    	// alter the resource in any way.
    	ValidateOnly [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=validate_only,json=validateOnly,proto3" json:"validate_only,omitempty"`
    	// Optional. If set as true, will create the resource if it is not found.
    	AllowMissing [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=allow_missing,json=allowMissing,proto3" json:"allow_missing,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for BeyondCorp.UpdateAppConnection.

### func (*UpdateAppConnectionRequest) Descriptor 
    
    
    func (*UpdateAppConnectionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAppConnectionRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAppConnectionRequest) GetAllowMissing 
    
    
    func (x *UpdateAppConnectionRequest) GetAllowMissing() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateAppConnectionRequest) GetAppConnection 
    
    
    func (x *UpdateAppConnectionRequest) GetAppConnection() *AppConnection

### func (*UpdateAppConnectionRequest) GetRequestId 
    
    
    func (x *UpdateAppConnectionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateAppConnectionRequest) GetUpdateMask 
    
    
    func (x *UpdateAppConnectionRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAppConnectionRequest) GetValidateOnly 
    
    
    func (x *UpdateAppConnectionRequest) GetValidateOnly() [bool](https://pkg.go.dev/builtin#bool)

### func (*UpdateAppConnectionRequest) ProtoMessage 
    
    
    func (*UpdateAppConnectionRequest) ProtoMessage()

### func (*UpdateAppConnectionRequest) ProtoReflect 
    
    
    func (x *UpdateAppConnectionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAppConnectionRequest) Reset 
    
    
    func (x *UpdateAppConnectionRequest) Reset()

### func (*UpdateAppConnectionRequest) String 
    
    
    func (x *UpdateAppConnectionRequest) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
