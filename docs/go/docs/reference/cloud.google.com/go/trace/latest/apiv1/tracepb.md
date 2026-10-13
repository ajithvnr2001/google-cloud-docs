---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/trace/latest/apiv1/tracepb/
title: Cloud Trace API v1 - Package cloud.google.com/go/trace/apiv1/tracepb (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:45.409619+00:00
---

# Cloud Trace API v1 - Package cloud.google.com/go/trace/apiv1/tracepb (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/trace/latest/apiv1/tracepb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Trace API v1 - Package cloud.google.com/go/trace/apiv1/tracepb (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.7  1.10.12  1.9.1  1.8.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/trace/apiv1/tracepb). 

##  Constants 

### TraceService_ListTraces_FullMethodName, TraceService_GetTrace_FullMethodName, TraceService_PatchTraces_FullMethodName
    
    
    const (
    	TraceService_ListTraces_FullMethodName  = "/google.devtools.cloudtrace.v1.TraceService/ListTraces"
    	TraceService_GetTrace_FullMethodName    = "/google.devtools.cloudtrace.v1.TraceService/GetTrace"
    	TraceService_PatchTraces_FullMethodName = "/google.devtools.cloudtrace.v1.TraceService/PatchTraces"
    )

## Variables 

### TraceSpan_SpanKind_name, TraceSpan_SpanKind_value
    
    
    var (
    	TraceSpan_SpanKind_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SPAN_KIND_UNSPECIFIED",
    		1: "RPC_SERVER",
    		2: "RPC_CLIENT",
    	}
    	TraceSpan_SpanKind_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SPAN_KIND_UNSPECIFIED": 0,
    		"RPC_SERVER":            1,
    		"RPC_CLIENT":            2,
    	}
    )

Enum value maps for TraceSpan_SpanKind.

### ListTracesRequest_ViewType_name, ListTracesRequest_ViewType_value
    
    
    var (
    	ListTracesRequest_ViewType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "VIEW_TYPE_UNSPECIFIED",
    		1: "MINIMAL",
    		2: "ROOTSPAN",
    		3: "COMPLETE",
    	}
    	ListTracesRequest_ViewType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"VIEW_TYPE_UNSPECIFIED": 0,
    		"MINIMAL":               1,
    		"ROOTSPAN":              2,
    		"COMPLETE":              3,
    	}
    )

Enum value maps for ListTracesRequest_ViewType.

### File_google_devtools_cloudtrace_v1_trace_proto
    
    
    var File_google_devtools_cloudtrace_v1_trace_proto protoreflect.FileDescriptor

### TraceService_ServiceDesc
    
    
    var TraceService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.devtools.cloudtrace.v1.TraceService",
    	HandlerType: (*TraceServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListTraces",
    			Handler:    _TraceService_ListTraces_Handler,
    		},
    		{
    			MethodName: "GetTrace",
    			Handler:    _TraceService_GetTrace_Handler,
    		},
    		{
    			MethodName: "PatchTraces",
    			Handler:    _TraceService_PatchTraces_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/devtools/cloudtrace/v1/trace.proto",
    }

TraceService_ServiceDesc is the grpc.ServiceDesc for TraceService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterTraceServiceServer 
    
    
    func RegisterTraceServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv TraceServiceServer)

## GetTraceRequest
    
    
    type GetTraceRequest struct {
    
    	// Required. ID of the Cloud project where the trace data is stored.
    	ProjectId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
    	// Required. ID of the trace to return.
    	TraceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=trace_id,json=traceId,proto3" json:"trace_id,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the `GetTrace` method.

### func (*GetTraceRequest) Descriptor 
    
    
    func (*GetTraceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetTraceRequest.ProtoReflect.Descriptor instead.

### func (*GetTraceRequest) GetProjectId 
    
    
    func (x *GetTraceRequest) GetProjectId() [string](https://pkg.go.dev/builtin#string)

### func (*GetTraceRequest) GetTraceId 
    
    
    func (x *GetTraceRequest) GetTraceId() [string](https://pkg.go.dev/builtin#string)

### func (*GetTraceRequest) ProtoMessage 
    
    
    func (*GetTraceRequest) ProtoMessage()

### func (*GetTraceRequest) ProtoReflect 
    
    
    func (x *GetTraceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetTraceRequest) Reset 
    
    
    func (x *GetTraceRequest) Reset()

### func (*GetTraceRequest) String 
    
    
    func (x *GetTraceRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListTracesRequest
    
    
    type ListTracesRequest struct {
    
    	// Required. ID of the Cloud project where the trace data is stored.
    	ProjectId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
    	// Optional. Type of data returned for traces in the list. Default is
    	// `MINIMAL`.
    	View ListTracesRequest_ViewType `protobuf:"varint,2,opt,name=view,proto3,enum=google.devtools.cloudtrace.v1.ListTracesRequest_ViewType" json:"view,omitempty"`
    	// Optional. Maximum number of traces to return. If not specified or <= 0,="" the="" implementation="" selects="" a="" reasonable="" value.="" the="" implementation="" may="" return="" fewer="" traces="" than="" the="" requested="" page="" size.="" pagesize="">[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Token identifying the page of results to return. If provided, use the
    	// value of the `next_page_token` field from a previous request.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Start of the time interval (inclusive) during which the trace data was
    	// collected from the application.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// End of the time interval (inclusive) during which the trace data was
    	// collected from the application.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// Optional. A filter against labels for the request.
    	//
    	// By default, searches use prefix matching. To specify exact match, prepend
    	// a plus symbol (`+`) to the search term.
    	// Multiple terms are ANDed. Syntax:
    	//
    	//   - `root:NAME_PREFIX` or `NAME_PREFIX`: Return traces where any root
    	//     span starts with `NAME_PREFIX`.
    	//   - `+root:NAME` or `+NAME`: Return traces where any root span's name is
    	//     exactly `NAME`.
    	//   - `span:NAME_PREFIX`: Return traces where any span starts with
    	//     `NAME_PREFIX`.
    	//   - `+span:NAME`: Return traces where any span's name is exactly
    	//     `NAME`.
    	//   - `latency:DURATION`: Return traces whose overall latency is
    	//     greater or equal to than `DURATION`. Accepted units are nanoseconds
    	//     (`ns`), milliseconds (`ms`), and seconds (`s`). Default is `ms`. For
    	//     example, `latency:24ms` returns traces whose overall latency
    	//     is greater than or equal to 24 milliseconds.
    	//   - `label:LABEL_KEY`: Return all traces containing the specified
    	//     label key (exact match, case-sensitive) regardless of the key:value
    	//     pair's value (including empty values).
    	//   - `LABEL_KEY:VALUE_PREFIX`: Return all traces containing the specified
    	//     label key (exact match, case-sensitive) whose value starts with
    	//     `VALUE_PREFIX`. Both a key and a value must be specified.
    	//   - `+LABEL_KEY:VALUE`: Return all traces containing a key:value pair
    	//     exactly matching the specified text. Both a key and a value must be
    	//     specified.
    	//   - `method:VALUE`: Equivalent to `/http/method:VALUE`.
    	//   - `url:VALUE`: Equivalent to `/http/url:VALUE`.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Field used to sort the returned traces.
    	// Can be one of the following:
    	//
    	//   - `trace_id`
    	//   - `name` (`name` field of root span in the trace)
    	//   - `duration` (difference between `end_time` and `start_time` fields of
    	//     the root span)
    	//   - `start` (`start_time` field of the root span)
    	//
    	// Descending order can be specified by appending `desc` to the sort field
    	// (for example, `name desc`).
    	//
    	// Only one sort field is permitted.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the `ListTraces` method. All fields are required unless specified.

### func (*ListTracesRequest) Descriptor 
    
    
    func (*ListTracesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListTracesRequest.ProtoReflect.Descriptor instead.

### func (*ListTracesRequest) GetEndTime 
    
    
    func (x *ListTracesRequest) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ListTracesRequest) GetFilter 
    
    
    func (x *ListTracesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListTracesRequest) GetOrderBy 
    
    
    func (x *ListTracesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListTracesRequest) GetPageSize 
    
    
    func (x *ListTracesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListTracesRequest) GetPageToken 
    
    
    func (x *ListTracesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListTracesRequest) GetProjectId 
    
    
    func (x *ListTracesRequest) GetProjectId() [string](https://pkg.go.dev/builtin#string)

### func (*ListTracesRequest) GetStartTime 
    
    
    func (x *ListTracesRequest) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ListTracesRequest) GetView 
    
    
    func (x *ListTracesRequest) GetView() ListTracesRequest_ViewType

### func (*ListTracesRequest) ProtoMessage 
    
    
    func (*ListTracesRequest) ProtoMessage()

### func (*ListTracesRequest) ProtoReflect 
    
    
    func (x *ListTracesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListTracesRequest) Reset 
    
    
    func (x *ListTracesRequest) Reset()

### func (*ListTracesRequest) String 
    
    
    func (x *ListTracesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListTracesRequest_ViewType
    
    
    type ListTracesRequest_ViewType [int32](https://pkg.go.dev/builtin#int32)

Type of data returned for traces in the list.

### ListTracesRequest_VIEW_TYPE_UNSPECIFIED, ListTracesRequest_MINIMAL, ListTracesRequest_ROOTSPAN, ListTracesRequest_COMPLETE
    
    
    const (
    	// Default is `MINIMAL` if unspecified.
    	ListTracesRequest_VIEW_TYPE_UNSPECIFIED ListTracesRequest_ViewType = 0
    	// Minimal view of the trace record that contains only the project
    	// and trace IDs.
    	ListTracesRequest_MINIMAL ListTracesRequest_ViewType = 1
    	// Root span view of the trace record that returns the root spans along
    	// with the minimal trace data.
    	ListTracesRequest_ROOTSPAN ListTracesRequest_ViewType = 2
    	// Complete view of the trace record that contains the actual trace data.
    	// This is equivalent to calling the REST `get` or RPC `GetTrace` method
    	// using the ID of each listed trace.
    	ListTracesRequest_COMPLETE ListTracesRequest_ViewType = 3
    )

### func (ListTracesRequest_ViewType) Descriptor 
    
    
    func (ListTracesRequest_ViewType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ListTracesRequest_ViewType) Enum 
    
    
    func (x ListTracesRequest_ViewType) Enum() *ListTracesRequest_ViewType

### func (ListTracesRequest_ViewType) EnumDescriptor 
    
    
    func (ListTracesRequest_ViewType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListTracesRequest_ViewType.Descriptor instead.

### func (ListTracesRequest_ViewType) Number 
    
    
    func (x ListTracesRequest_ViewType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ListTracesRequest_ViewType) String 
    
    
    func (x ListTracesRequest_ViewType) String() [string](https://pkg.go.dev/builtin#string)

### func (ListTracesRequest_ViewType) Type 
    
    
    func (ListTracesRequest_ViewType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListTracesResponse
    
    
    type ListTracesResponse struct {
    
    	// List of trace records as specified by the view parameter.
    	Traces []*Trace `protobuf:"bytes,1,rep,name=traces,proto3" json:"traces,omitempty"`
    	// If defined, indicates that there are more traces that match the request
    	// and that this value should be passed to the next request to continue
    	// retrieving additional traces.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for the `ListTraces` method.

### func (*ListTracesResponse) Descriptor 
    
    
    func (*ListTracesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListTracesResponse.ProtoReflect.Descriptor instead.

### func (*ListTracesResponse) GetNextPageToken 
    
    
    func (x *ListTracesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListTracesResponse) GetTraces 
    
    
    func (x *ListTracesResponse) GetTraces() []*Trace

### func (*ListTracesResponse) ProtoMessage 
    
    
    func (*ListTracesResponse) ProtoMessage()

### func (*ListTracesResponse) ProtoReflect 
    
    
    func (x *ListTracesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListTracesResponse) Reset 
    
    
    func (x *ListTracesResponse) Reset()

### func (*ListTracesResponse) String 
    
    
    func (x *ListTracesResponse) String() [string](https://pkg.go.dev/builtin#string)

## PatchTracesRequest
    
    
    type PatchTracesRequest struct {
    
    	// Required. ID of the Cloud project where the trace data is stored.
    	ProjectId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
    	// Required. The body of the message.
    	Traces *Traces `protobuf:"bytes,2,opt,name=traces,proto3" json:"traces,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the `PatchTraces` method.

### func (*PatchTracesRequest) Descriptor 
    
    
    func (*PatchTracesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PatchTracesRequest.ProtoReflect.Descriptor instead.

### func (*PatchTracesRequest) GetProjectId 
    
    
    func (x *PatchTracesRequest) GetProjectId() [string](https://pkg.go.dev/builtin#string)

### func (*PatchTracesRequest) GetTraces 
    
    
    func (x *PatchTracesRequest) GetTraces() *Traces

### func (*PatchTracesRequest) ProtoMessage 
    
    
    func (*PatchTracesRequest) ProtoMessage()

### func (*PatchTracesRequest) ProtoReflect 
    
    
    func (x *PatchTracesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PatchTracesRequest) Reset 
    
    
    func (x *PatchTracesRequest) Reset()

### func (*PatchTracesRequest) String 
    
    
    func (x *PatchTracesRequest) String() [string](https://pkg.go.dev/builtin#string)

## Trace
    
    
    type Trace struct {
    
    	// Project ID of the Cloud project where the trace data is stored.
    	ProjectId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
    	// Globally unique identifier for the trace. This identifier is a 128-bit
    	// numeric value formatted as a 32-byte hex string. For example,
    	// `382d4f4c6b7bb2f4a972559d9085001d`.
    	TraceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=trace_id,json=traceId,proto3" json:"trace_id,omitempty"`
    	// Collection of spans in the trace.
    	Spans []*TraceSpan `protobuf:"bytes,3,rep,name=spans,proto3" json:"spans,omitempty"`
    	// contains filtered or unexported fields
    }

A trace describes how long it takes for an application to perform an operation. It consists of a set of spans, each of which represent a single timed event within the operation.

### func (*Trace) Descriptor 
    
    
    func (*Trace) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Trace.ProtoReflect.Descriptor instead.

### func (*Trace) GetProjectId 
    
    
    func (x *Trace) GetProjectId() [string](https://pkg.go.dev/builtin#string)

### func (*Trace) GetSpans 
    
    
    func (x *Trace) GetSpans() []*TraceSpan

### func (*Trace) GetTraceId 
    
    
    func (x *Trace) GetTraceId() [string](https://pkg.go.dev/builtin#string)

### func (*Trace) ProtoMessage 
    
    
    func (*Trace) ProtoMessage()

### func (*Trace) ProtoReflect 
    
    
    func (x *Trace) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Trace) Reset 
    
    
    func (x *Trace) Reset()

### func (*Trace) String 
    
    
    func (x *Trace) String() [string](https://pkg.go.dev/builtin#string)

## TraceServiceClient
    
    
    type TraceServiceClient interface {
    	// Returns of a list of traces that match the specified filter conditions.
    	ListTraces(ctx context.Context, in *ListTracesRequest, opts ...grpc.CallOption) (*ListTracesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets a single trace by its ID.
    	GetTrace(ctx context.Context, in *GetTraceRequest, opts ...grpc.CallOption) (*Trace, [error](https://pkg.go.dev/builtin#error))
    	// Sends new traces to Stackdriver Trace or updates existing traces. If the ID
    	// of a trace that you send matches that of an existing trace, any fields
    	// in the existing trace and its spans are overwritten by the provided values,
    	// and any new fields provided are merged with the existing trace data. If the
    	// ID does not match, a new trace is created.
    	PatchTraces(ctx context.Context, in *PatchTracesRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

TraceServiceClient is the client API for TraceService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewTraceServiceClient 
    
    
    func NewTraceServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) TraceServiceClient

## TraceServiceServer
    
    
    type TraceServiceServer interface {
    	// Returns of a list of traces that match the specified filter conditions.
    	ListTraces(context.Context, *ListTracesRequest) (*ListTracesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets a single trace by its ID.
    	GetTrace(context.Context, *GetTraceRequest) (*Trace, [error](https://pkg.go.dev/builtin#error))
    	// Sends new traces to Stackdriver Trace or updates existing traces. If the ID
    	// of a trace that you send matches that of an existing trace, any fields
    	// in the existing trace and its spans are overwritten by the provided values,
    	// and any new fields provided are merged with the existing trace data. If the
    	// ID does not match, a new trace is created.
    	PatchTraces(context.Context, *PatchTracesRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

TraceServiceServer is the server API for TraceService service. All implementations should embed UnimplementedTraceServiceServer for forward compatibility

## TraceSpan
    
    
    type TraceSpan struct {
    
    	// Identifier for the span. Must be a 64-bit integer other than 0 and
    	// unique within a trace. For example, `2205310701640571284`.
    	SpanId [uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,1,opt,name=span_id,json=spanId,proto3" json:"span_id,omitempty"`
    	// Distinguishes between spans generated in a particular context. For example,
    	// two spans with the same name may be distinguished using `RPC_CLIENT`
    	// and `RPC_SERVER` to identify queueing latency associated with the span.
    	Kind TraceSpan_SpanKind `protobuf:"varint,2,opt,name=kind,proto3,enum=google.devtools.cloudtrace.v1.TraceSpan_SpanKind" json:"kind,omitempty"`
    	// Name of the span. Must be less than 128 bytes. The span name is sanitized
    	// and displayed in the Stackdriver Trace tool in the
    	// Google Cloud Platform Console.
    	// The name may be a method name or some other per-call site name.
    	// For the same executable and the same call point, a best practice is
    	// to use a consistent name, which makes it easier to correlate
    	// cross-trace spans.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
    	// Start time of the span in nanoseconds from the UNIX epoch.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// End time of the span in nanoseconds from the UNIX epoch.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// Optional. ID of the parent span, if any.
    	ParentSpanId [uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,6,opt,name=parent_span_id,json=parentSpanId,proto3" json:"parent_span_id,omitempty"`
    	// Collection of labels associated with the span. Label keys must be less than
    	// 128 bytes. Label values must be less than 16 kilobytes (10MB for
    	// `/stacktrace` values).
    	//
    	// Some predefined label keys exist, or you may create your own. When creating
    	// your own, we recommend the following formats:
    	//
    	//   - `/category/product/key` for agents of well-known products (e.g.
    	//     `/db/mongodb/read_size`).
    	//   - `short_host/path/key` for domain-specific keys (e.g.
    	//     `foo.com/myproduct/bar`)
    	//
    	// Predefined labels include:
    	//
    	// *   `/agent`
    	// *   `/component`
    	// *   `/error/message`
    	// *   `/error/name`
    	// *   `/http/client_city`
    	// *   `/http/client_country`
    	// *   `/http/client_protocol`
    	// *   `/http/client_region`
    	// *   `/http/host`
    	// *   `/http/method`
    	// *   `/http/path`
    	// *   `/http/redirected_url`
    	// *   `/http/request/size`
    	// *   `/http/response/size`
    	// *   `/http/route`
    	// *   `/http/status_code`
    	// *   `/http/url`
    	// *   `/http/user_agent`
    	// *   `/pid`
    	// *   `/stacktrace`
    	// *   `/tid`
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

A span represents a single timed event within a trace. Spans can be nested and form a trace tree. Often, a trace contains a root span that describes the end-to-end latency of an operation and, optionally, one or more subspans for its suboperations. Spans do not need to be contiguous. There may be gaps between spans in a trace.

### func (*TraceSpan) Descriptor 
    
    
    func (*TraceSpan) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TraceSpan.ProtoReflect.Descriptor instead.

### func (*TraceSpan) GetEndTime 
    
    
    func (x *TraceSpan) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TraceSpan) GetKind 
    
    
    func (x *TraceSpan) GetKind() TraceSpan_SpanKind

### func (*TraceSpan) GetLabels 
    
    
    func (x *TraceSpan) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*TraceSpan) GetName 
    
    
    func (x *TraceSpan) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*TraceSpan) GetParentSpanId 
    
    
    func (x *TraceSpan) GetParentSpanId() [uint64](https://pkg.go.dev/builtin#uint64)

### func (*TraceSpan) GetSpanId 
    
    
    func (x *TraceSpan) GetSpanId() [uint64](https://pkg.go.dev/builtin#uint64)

### func (*TraceSpan) GetStartTime 
    
    
    func (x *TraceSpan) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TraceSpan) ProtoMessage 
    
    
    func (*TraceSpan) ProtoMessage()

### func (*TraceSpan) ProtoReflect 
    
    
    func (x *TraceSpan) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TraceSpan) Reset 
    
    
    func (x *TraceSpan) Reset()

### func (*TraceSpan) String 
    
    
    func (x *TraceSpan) String() [string](https://pkg.go.dev/builtin#string)

## TraceSpan_SpanKind
    
    
    type TraceSpan_SpanKind [int32](https://pkg.go.dev/builtin#int32)

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

### TraceSpan_SPAN_KIND_UNSPECIFIED, TraceSpan_RPC_SERVER, TraceSpan_RPC_CLIENT
    
    
    const (
    	// Unspecified.
    	TraceSpan_SPAN_KIND_UNSPECIFIED TraceSpan_SpanKind = 0
    	// Indicates that the span covers server-side handling of an RPC or other
    	// remote network request.
    	TraceSpan_RPC_SERVER TraceSpan_SpanKind = 1
    	// Indicates that the span covers the client-side wrapper around an RPC or
    	// other remote request.
    	TraceSpan_RPC_CLIENT TraceSpan_SpanKind = 2
    )

### func (TraceSpan_SpanKind) Descriptor 
    
    
    func (TraceSpan_SpanKind) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TraceSpan_SpanKind) Enum 
    
    
    func (x TraceSpan_SpanKind) Enum() *TraceSpan_SpanKind

### func (TraceSpan_SpanKind) EnumDescriptor 
    
    
    func (TraceSpan_SpanKind) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TraceSpan_SpanKind.Descriptor instead.

### func (TraceSpan_SpanKind) Number 
    
    
    func (x TraceSpan_SpanKind) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TraceSpan_SpanKind) String 
    
    
    func (x TraceSpan_SpanKind) String() [string](https://pkg.go.dev/builtin#string)

### func (TraceSpan_SpanKind) Type 
    
    
    func (TraceSpan_SpanKind) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Traces
    
    
    type Traces struct {
    
    	// List of traces.
    	Traces []*Trace `protobuf:"bytes,1,rep,name=traces,proto3" json:"traces,omitempty"`
    	// contains filtered or unexported fields
    }

List of new or updated traces.

### func (*Traces) Descriptor 
    
    
    func (*Traces) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Traces.ProtoReflect.Descriptor instead.

### func (*Traces) GetTraces 
    
    
    func (x *Traces) GetTraces() []*Trace

### func (*Traces) ProtoMessage 
    
    
    func (*Traces) ProtoMessage()

### func (*Traces) ProtoReflect 
    
    
    func (x *Traces) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Traces) Reset 
    
    
    func (x *Traces) Reset()

### func (*Traces) String 
    
    
    func (x *Traces) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedTraceServiceServer
    
    
    type UnimplementedTraceServiceServer struct {
    }

UnimplementedTraceServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedTraceServiceServer) GetTrace 
    
    
    func (UnimplementedTraceServiceServer) GetTrace([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetTraceRequest) (*Trace, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTraceServiceServer) ListTraces 
    
    
    func (UnimplementedTraceServiceServer) ListTraces([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListTracesRequest) (*ListTracesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTraceServiceServer) PatchTraces 
    
    
    func (UnimplementedTraceServiceServer) PatchTraces([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *PatchTracesRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

## UnsafeTraceServiceServer
    
    
    type UnsafeTraceServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeTraceServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to TraceServiceServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
