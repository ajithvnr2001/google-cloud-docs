---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/apiregistry/latest/apiv1/apiregistrypb/
title: Cloud API Registry API v1 - Package cloud.google.com/go/apiregistry/apiv1/apiregistrypb (v1.1.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:55.293033+00:00
---

# Cloud API Registry API v1 - Package cloud.google.com/go/apiregistry/apiv1/apiregistrypb (v1.1.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/apiregistry/latest/apiv1/apiregistrypb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud API Registry API v1 - Package cloud.google.com/go/apiregistry/apiv1/apiregistrypb (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/apiregistry/apiv1/apiregistrypb). 

##  Constants 

### CloudApiRegistry_GetMcpServer_FullMethodName, CloudApiRegistry_ListMcpServers_FullMethodName, CloudApiRegistry_GetMcpTool_FullMethodName, CloudApiRegistry_ListMcpTools_FullMethodName
    
    
    const (
    	CloudApiRegistry_GetMcpServer_FullMethodName   = "/google.cloud.apiregistry.v1.CloudApiRegistry/GetMcpServer"
    	CloudApiRegistry_ListMcpServers_FullMethodName = "/google.cloud.apiregistry.v1.CloudApiRegistry/ListMcpServers"
    	CloudApiRegistry_GetMcpTool_FullMethodName     = "/google.cloud.apiregistry.v1.CloudApiRegistry/GetMcpTool"
    	CloudApiRegistry_ListMcpTools_FullMethodName   = "/google.cloud.apiregistry.v1.CloudApiRegistry/ListMcpTools"
    )

## Variables 

### State_name, State_value
    
    
    var (
    	State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ENABLED",
    		2: "DISABLED",
    	}
    	State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ENABLED":           1,
    		"DISABLED":          2,
    	}
    )

Enum value maps for State.

### CloudApiRegistry_ServiceDesc
    
    
    var CloudApiRegistry_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.apiregistry.v1.CloudApiRegistry",
    	HandlerType: (*CloudApiRegistryServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetMcpServer",
    			Handler:    _CloudApiRegistry_GetMcpServer_Handler,
    		},
    		{
    			MethodName: "ListMcpServers",
    			Handler:    _CloudApiRegistry_ListMcpServers_Handler,
    		},
    		{
    			MethodName: "GetMcpTool",
    			Handler:    _CloudApiRegistry_GetMcpTool_Handler,
    		},
    		{
    			MethodName: "ListMcpTools",
    			Handler:    _CloudApiRegistry_ListMcpTools_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/apiregistry/v1/service.proto",
    }

CloudApiRegistry_ServiceDesc is the grpc.ServiceDesc for CloudApiRegistry service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_apiregistry_v1_common_proto
    
    
    var File_google_cloud_apiregistry_v1_common_proto protoreflect.FileDescriptor

### File_google_cloud_apiregistry_v1_resources_proto
    
    
    var File_google_cloud_apiregistry_v1_resources_proto protoreflect.FileDescriptor

### File_google_cloud_apiregistry_v1_service_proto
    
    
    var File_google_cloud_apiregistry_v1_service_proto protoreflect.FileDescriptor

## Functions 

### func RegisterCloudApiRegistryServer 
    
    
    func RegisterCloudApiRegistryServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CloudApiRegistryServer)

## CloudApiRegistryClient
    
    
    type CloudApiRegistryClient interface {
    	// Gets a single McpServer.
    	GetMcpServer(ctx context.Context, in *GetMcpServerRequest, opts ...grpc.CallOption) (*McpServer, [error](https://pkg.go.dev/builtin#error))
    	// Lists McpServers in a given Project.
    	ListMcpServers(ctx context.Context, in *ListMcpServersRequest, opts ...grpc.CallOption) (*ListMcpServersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets a single McpTool.
    	GetMcpTool(ctx context.Context, in *GetMcpToolRequest, opts ...grpc.CallOption) (*McpTool, [error](https://pkg.go.dev/builtin#error))
    	// Lists McpTools in a given McpServer.
    	ListMcpTools(ctx context.Context, in *ListMcpToolsRequest, opts ...grpc.CallOption) (*ListMcpToolsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CloudApiRegistryClient is the client API for CloudApiRegistry service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCloudApiRegistryClient 
    
    
    func NewCloudApiRegistryClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CloudApiRegistryClient

## CloudApiRegistryServer
    
    
    type CloudApiRegistryServer interface {
    	// Gets a single McpServer.
    	GetMcpServer(context.Context, *GetMcpServerRequest) (*McpServer, [error](https://pkg.go.dev/builtin#error))
    	// Lists McpServers in a given Project.
    	ListMcpServers(context.Context, *ListMcpServersRequest) (*ListMcpServersResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets a single McpTool.
    	GetMcpTool(context.Context, *GetMcpToolRequest) (*McpTool, [error](https://pkg.go.dev/builtin#error))
    	// Lists McpTools in a given McpServer.
    	ListMcpTools(context.Context, *ListMcpToolsRequest) (*ListMcpToolsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CloudApiRegistryServer is the server API for CloudApiRegistry service. All implementations should embed UnimplementedCloudApiRegistryServer for forward compatibility

## GetMcpServerRequest
    
    
    type GetMcpServerRequest struct {
    
    	// Required. Name of the resource
    	// Format: projects/{project}/locations/{location}/mcpServers/{mcp_server}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a McpServer

### func (*GetMcpServerRequest) Descriptor 
    
    
    func (*GetMcpServerRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetMcpServerRequest.ProtoReflect.Descriptor instead.

### func (*GetMcpServerRequest) GetName 
    
    
    func (x *GetMcpServerRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetMcpServerRequest) ProtoMessage 
    
    
    func (*GetMcpServerRequest) ProtoMessage()

### func (*GetMcpServerRequest) ProtoReflect 
    
    
    func (x *GetMcpServerRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetMcpServerRequest) Reset 
    
    
    func (x *GetMcpServerRequest) Reset()

### func (*GetMcpServerRequest) String 
    
    
    func (x *GetMcpServerRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetMcpToolRequest
    
    
    type GetMcpToolRequest struct {
    
    	// Required. Name of the resource
    	// Format:
    	// projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a McpTool

### func (*GetMcpToolRequest) Descriptor 
    
    
    func (*GetMcpToolRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetMcpToolRequest.ProtoReflect.Descriptor instead.

### func (*GetMcpToolRequest) GetName 
    
    
    func (x *GetMcpToolRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetMcpToolRequest) ProtoMessage 
    
    
    func (*GetMcpToolRequest) ProtoMessage()

### func (*GetMcpToolRequest) ProtoReflect 
    
    
    func (x *GetMcpToolRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetMcpToolRequest) Reset 
    
    
    func (x *GetMcpToolRequest) Reset()

### func (*GetMcpToolRequest) String 
    
    
    func (x *GetMcpToolRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMcpServersRequest
    
    
    type ListMcpServersRequest struct {
    
    	// Required. Parent value for ListMcpServersRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, at most 50 items will be returned. The maximum
    	// value is 100; values above 100 will be coerced to 100.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. An expression that filters the results.
    	// For syntax, see https://google.aip.dev/160.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. A comma-separated list of fields to order by, sorted in ascending
    	// order. Use "desc" after a field name for descending. For syntax, see
    	// https://google.aip.dev/132#ordering.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of McpServers

### func (*ListMcpServersRequest) Descriptor 
    
    
    func (*ListMcpServersRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMcpServersRequest.ProtoReflect.Descriptor instead.

### func (*ListMcpServersRequest) GetFilter 
    
    
    func (x *ListMcpServersRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersRequest) GetOrderBy 
    
    
    func (x *ListMcpServersRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersRequest) GetPageSize 
    
    
    func (x *ListMcpServersRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListMcpServersRequest) GetPageToken 
    
    
    func (x *ListMcpServersRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersRequest) GetParent 
    
    
    func (x *ListMcpServersRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersRequest) ProtoMessage 
    
    
    func (*ListMcpServersRequest) ProtoMessage()

### func (*ListMcpServersRequest) ProtoReflect 
    
    
    func (x *ListMcpServersRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMcpServersRequest) Reset 
    
    
    func (x *ListMcpServersRequest) Reset()

### func (*ListMcpServersRequest) String 
    
    
    func (x *ListMcpServersRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMcpServersResponse
    
    
    type ListMcpServersResponse struct {
    
    	// The list of McpServer
    	McpServers []*McpServer `protobuf:"bytes,1,rep,name=mcp_servers,json=mcpServers,proto3" json:"mcp_servers,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing McpServers

### func (*ListMcpServersResponse) Descriptor 
    
    
    func (*ListMcpServersResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMcpServersResponse.ProtoReflect.Descriptor instead.

### func (*ListMcpServersResponse) GetMcpServers 
    
    
    func (x *ListMcpServersResponse) GetMcpServers() []*McpServer

### func (*ListMcpServersResponse) GetNextPageToken 
    
    
    func (x *ListMcpServersResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersResponse) GetUnreachable 
    
    
    func (x *ListMcpServersResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListMcpServersResponse) ProtoMessage 
    
    
    func (*ListMcpServersResponse) ProtoMessage()

### func (*ListMcpServersResponse) ProtoReflect 
    
    
    func (x *ListMcpServersResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMcpServersResponse) Reset 
    
    
    func (x *ListMcpServersResponse) Reset()

### func (*ListMcpServersResponse) String 
    
    
    func (x *ListMcpServersResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListMcpToolsRequest
    
    
    type ListMcpToolsRequest struct {
    
    	// Required. Parent value for ListMcpToolsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, at most 50 items will be returned. The maximum
    	// value is 100; values above 100 will be coerced to 100.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. An expression that filters the results.
    	// For syntax, see https://google.aip.dev/160.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. A comma-separated list of fields to order by, sorted in ascending
    	// order. Use "desc" after a field name for descending. For syntax, see
    	// https://google.aip.dev/132#ordering.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of McpTools

### func (*ListMcpToolsRequest) Descriptor 
    
    
    func (*ListMcpToolsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMcpToolsRequest.ProtoReflect.Descriptor instead.

### func (*ListMcpToolsRequest) GetFilter 
    
    
    func (x *ListMcpToolsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsRequest) GetOrderBy 
    
    
    func (x *ListMcpToolsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsRequest) GetPageSize 
    
    
    func (x *ListMcpToolsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListMcpToolsRequest) GetPageToken 
    
    
    func (x *ListMcpToolsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsRequest) GetParent 
    
    
    func (x *ListMcpToolsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsRequest) ProtoMessage 
    
    
    func (*ListMcpToolsRequest) ProtoMessage()

### func (*ListMcpToolsRequest) ProtoReflect 
    
    
    func (x *ListMcpToolsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMcpToolsRequest) Reset 
    
    
    func (x *ListMcpToolsRequest) Reset()

### func (*ListMcpToolsRequest) String 
    
    
    func (x *ListMcpToolsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListMcpToolsResponse
    
    
    type ListMcpToolsResponse struct {
    
    	// The list of McpTool
    	McpTools []*McpTool `protobuf:"bytes,1,rep,name=mcp_tools,json=mcpTools,proto3" json:"mcp_tools,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Unordered list. Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing McpTools

### func (*ListMcpToolsResponse) Descriptor 
    
    
    func (*ListMcpToolsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListMcpToolsResponse.ProtoReflect.Descriptor instead.

### func (*ListMcpToolsResponse) GetMcpTools 
    
    
    func (x *ListMcpToolsResponse) GetMcpTools() []*McpTool

### func (*ListMcpToolsResponse) GetNextPageToken 
    
    
    func (x *ListMcpToolsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsResponse) GetUnreachable 
    
    
    func (x *ListMcpToolsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListMcpToolsResponse) ProtoMessage 
    
    
    func (*ListMcpToolsResponse) ProtoMessage()

### func (*ListMcpToolsResponse) ProtoReflect 
    
    
    func (x *ListMcpToolsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListMcpToolsResponse) Reset 
    
    
    func (x *ListMcpToolsResponse) Reset()

### func (*ListMcpToolsResponse) String 
    
    
    func (x *ListMcpToolsResponse) String() [string](https://pkg.go.dev/builtin#string)

## McpServer
    
    
    type McpServer struct {
    
    	// Identifier. The resource name of the MCP Server.
    	// Format:
    	// `projects/{project}/locations/{location}/mcpServers/{mcp_server}`.
    	// Example:
    	// projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp
    	// for 1p
    	// projects/12345/locations/us-central1/mcpServers/apphub:starbucks for
    	// 2p
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A human readable name for the MCP server.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Optional. A human-readable description of the MCP Server's functionality.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
    	// The base URL of the MCP server. Example: [geolocation.googleapis.com/mcp].
    	Urls [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=urls,proto3" json:"urls,omitempty"`
    	// The capabilities that a server may support. Known capabilities defined in
    	// https://modelcontextprotocol.io/specification/2025-06-18/schema#servercapabilities
    	// and additional capabilities defined by the servers.
    	Capabilities *structpb.Struct `protobuf:"bytes,6,opt,name=capabilities,proto3" json:"capabilities,omitempty"`
    	// Output only. The state of the MCP Server.
    	State State `protobuf:"varint,7,opt,name=state,proto3,enum=google.cloud.apiregistry.v1.State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Represents an MCP Server. MCP Servers act as endpoints that expose a collection of tools that can be invoked by agents.

### func (*McpServer) Descriptor 
    
    
    func (*McpServer) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use McpServer.ProtoReflect.Descriptor instead.

### func (*McpServer) GetCapabilities 
    
    
    func (x *McpServer) GetCapabilities() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*McpServer) GetDescription 
    
    
    func (x *McpServer) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*McpServer) GetDisplayName 
    
    
    func (x *McpServer) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*McpServer) GetName 
    
    
    func (x *McpServer) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*McpServer) GetState 
    
    
    func (x *McpServer) GetState() State

### func (*McpServer) GetUrls 
    
    
    func (x *McpServer) GetUrls() [][string](https://pkg.go.dev/builtin#string)

### func (*McpServer) ProtoMessage 
    
    
    func (*McpServer) ProtoMessage()

### func (*McpServer) ProtoReflect 
    
    
    func (x *McpServer) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*McpServer) Reset 
    
    
    func (x *McpServer) Reset()

### func (*McpServer) String 
    
    
    func (x *McpServer) String() [string](https://pkg.go.dev/builtin#string)

## McpTool
    
    
    type McpTool struct {
    
    	// Identifier. The resource name of the McpTool.
    	// Format:
    	// `projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}`.
    	// Example:
    	// projects/12345/locations/us-central1/mcpServers/google:bigquery.googleapis.com:mcp/mcpTools/insert_job
    	// for 1p
    	// projects/12345/locations/us-central1/mcpServers/apphub:starbucks/mcpTools/order_pizza
    	// for 2p
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A human-readable name for the tool, suitable for display.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A human-readable description of the tool's functionality.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
    	// Automatically populated reference to MCP Server. Helpful when multiple
    	// tools are requested across different MCP Servers.
    	McpServerUrls [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=mcp_server_urls,json=mcpServerUrls,proto3" json:"mcp_server_urls,omitempty"`
    	// A JSON Schema object defining the expected parameters for invoking the
    	// tool.
    	InputSchema *structpb.Struct `protobuf:"bytes,5,opt,name=input_schema,json=inputSchema,proto3" json:"input_schema,omitempty"`
    	// Optional. A JSON Schema object defining the expected structure of the
    	// tool's output.
    	OutputSchema *structpb.Struct `protobuf:"bytes,6,opt,name=output_schema,json=outputSchema,proto3" json:"output_schema,omitempty"`
    	// Optional key-value object that allows developers to provide additional
    	// information regarding tool properties, behavior, and usage best practices.
    	// Annotations or tags to facilitate semantic search across tools ("semantic
    	// tags") are not in the MVP scope. When implemented, the first set of
    	// supported annotations will likely be the standard, predefined annotations
    	// from the open-source MCP spec. These include:
    	//   - title: A human-readable title for the tool, useful for UI display.
    	//   - readOnlyHint: If true, indicates the tool does not modify its
    	//     environment.
    	//   - destructiveHint: If true, the tool may perform destructive updates
    	//     (only meaningful when readOnlyHint is false).
    	//   - idempotentHint: If true, calling the tool repeatedly with the same
    	//     arguments has no additional effect (only meaningful when readOnlyHint is
    	//     false).
    	//   - openWorldHint: If true, the tool may interact with an "open world" of
    	//     external entities.
    	Annotations *structpb.Struct `protobuf:"bytes,7,opt,name=annotations,proto3" json:"annotations,omitempty"`
    	// contains filtered or unexported fields
    }

Message describing McpTool object

### func (*McpTool) Descriptor 
    
    
    func (*McpTool) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use McpTool.ProtoReflect.Descriptor instead.

### func (*McpTool) GetAnnotations 
    
    
    func (x *McpTool) GetAnnotations() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*McpTool) GetDescription 
    
    
    func (x *McpTool) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*McpTool) GetDisplayName 
    
    
    func (x *McpTool) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*McpTool) GetInputSchema 
    
    
    func (x *McpTool) GetInputSchema() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*McpTool) GetMcpServerUrls 
    
    
    func (x *McpTool) GetMcpServerUrls() [][string](https://pkg.go.dev/builtin#string)

### func (*McpTool) GetName 
    
    
    func (x *McpTool) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*McpTool) GetOutputSchema 
    
    
    func (x *McpTool) GetOutputSchema() *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct)

### func (*McpTool) ProtoMessage 
    
    
    func (*McpTool) ProtoMessage()

### func (*McpTool) ProtoReflect 
    
    
    func (x *McpTool) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*McpTool) Reset 
    
    
    func (x *McpTool) Reset()

### func (*McpTool) String 
    
    
    func (x *McpTool) String() [string](https://pkg.go.dev/builtin#string)

## State
    
    
    type State [int32](https://pkg.go.dev/builtin#int32)

The state of McpServer resource.

### State_STATE_UNSPECIFIED, State_ENABLED, State_DISABLED
    
    
    const (
    	// The McpServer state is unspecified.
    	State_STATE_UNSPECIFIED State = 0
    	// The McpServer is enabled.
    	State_ENABLED State = 1
    	// The McpServer is disabled.
    	State_DISABLED State = 2
    )

### func (State) Descriptor 
    
    
    func (State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (State) Enum 
    
    
    func (x State) Enum() *State

### func (State) EnumDescriptor 
    
    
    func (State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use State.Descriptor instead.

### func (State) Number 
    
    
    func (x State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (State) String 
    
    
    func (x State) String() [string](https://pkg.go.dev/builtin#string)

### func (State) Type 
    
    
    func (State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedCloudApiRegistryServer
    
    
    type UnimplementedCloudApiRegistryServer struct {
    }

UnimplementedCloudApiRegistryServer should be embedded to have forward compatible implementations.

### func (UnimplementedCloudApiRegistryServer) GetMcpServer 
    
    
    func (UnimplementedCloudApiRegistryServer) GetMcpServer([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetMcpServerRequest) (*McpServer, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCloudApiRegistryServer) GetMcpTool 
    
    
    func (UnimplementedCloudApiRegistryServer) GetMcpTool([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetMcpToolRequest) (*McpTool, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCloudApiRegistryServer) ListMcpServers 
    
    
    func (UnimplementedCloudApiRegistryServer) ListMcpServers([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListMcpServersRequest) (*ListMcpServersResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCloudApiRegistryServer) ListMcpTools 
    
    
    func (UnimplementedCloudApiRegistryServer) ListMcpTools([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListMcpToolsRequest) (*ListMcpToolsResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeCloudApiRegistryServer
    
    
    type UnsafeCloudApiRegistryServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCloudApiRegistryServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CloudApiRegistryServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
