---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/support/latest/apiv2/supportpb/
title: Google Cloud Support API v2 - Package cloud.google.com/go/support/apiv2/supportpb (v1.15.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:56.118852+00:00
---

# Google Cloud Support API v2 - Package cloud.google.com/go/support/apiv2/supportpb (v1.15.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/support/latest/apiv2/supportpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Google Cloud Support API v2 - Package cloud.google.com/go/support/apiv2/supportpb (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.6  1.0.11  0.2.2  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/support/apiv2/supportpb). 

##  Constants 

### CaseAttachmentService_ListAttachments_FullMethodName, CaseAttachmentService_GetAttachment_FullMethodName
    
    
    const (
    	CaseAttachmentService_ListAttachments_FullMethodName = "/google.cloud.support.v2.CaseAttachmentService/ListAttachments"
    	CaseAttachmentService_GetAttachment_FullMethodName   = "/google.cloud.support.v2.CaseAttachmentService/GetAttachment"
    )

### CaseService_GetCase_FullMethodName, CaseService_ListCases_FullMethodName, CaseService_SearchCases_FullMethodName, CaseService_CreateCase_FullMethodName, CaseService_UpdateCase_FullMethodName, CaseService_EscalateCase_FullMethodName, CaseService_CloseCase_FullMethodName, CaseService_SearchCaseClassifications_FullMethodName
    
    
    const (
    	CaseService_GetCase_FullMethodName                   = "/google.cloud.support.v2.CaseService/GetCase"
    	CaseService_ListCases_FullMethodName                 = "/google.cloud.support.v2.CaseService/ListCases"
    	CaseService_SearchCases_FullMethodName               = "/google.cloud.support.v2.CaseService/SearchCases"
    	CaseService_CreateCase_FullMethodName                = "/google.cloud.support.v2.CaseService/CreateCase"
    	CaseService_UpdateCase_FullMethodName                = "/google.cloud.support.v2.CaseService/UpdateCase"
    	CaseService_EscalateCase_FullMethodName              = "/google.cloud.support.v2.CaseService/EscalateCase"
    	CaseService_CloseCase_FullMethodName                 = "/google.cloud.support.v2.CaseService/CloseCase"
    	CaseService_SearchCaseClassifications_FullMethodName = "/google.cloud.support.v2.CaseService/SearchCaseClassifications"
    )

### CommentService_ListComments_FullMethodName, CommentService_CreateComment_FullMethodName, CommentService_GetComment_FullMethodName
    
    
    const (
    	CommentService_ListComments_FullMethodName  = "/google.cloud.support.v2.CommentService/ListComments"
    	CommentService_CreateComment_FullMethodName = "/google.cloud.support.v2.CommentService/CreateComment"
    	CommentService_GetComment_FullMethodName    = "/google.cloud.support.v2.CommentService/GetComment"
    )

### SupportEventSubscriptionService_CreateSupportEventSubscription_FullMethodName, SupportEventSubscriptionService_GetSupportEventSubscription_FullMethodName, SupportEventSubscriptionService_ListSupportEventSubscriptions_FullMethodName, SupportEventSubscriptionService_UpdateSupportEventSubscription_FullMethodName, SupportEventSubscriptionService_DeleteSupportEventSubscription_FullMethodName, SupportEventSubscriptionService_UndeleteSupportEventSubscription_FullMethodName, SupportEventSubscriptionService_ExpungeSupportEventSubscription_FullMethodName
    
    
    const (
    	SupportEventSubscriptionService_CreateSupportEventSubscription_FullMethodName   = "/google.cloud.support.v2.SupportEventSubscriptionService/CreateSupportEventSubscription"
    	SupportEventSubscriptionService_GetSupportEventSubscription_FullMethodName      = "/google.cloud.support.v2.SupportEventSubscriptionService/GetSupportEventSubscription"
    	SupportEventSubscriptionService_ListSupportEventSubscriptions_FullMethodName    = "/google.cloud.support.v2.SupportEventSubscriptionService/ListSupportEventSubscriptions"
    	SupportEventSubscriptionService_UpdateSupportEventSubscription_FullMethodName   = "/google.cloud.support.v2.SupportEventSubscriptionService/UpdateSupportEventSubscription"
    	SupportEventSubscriptionService_DeleteSupportEventSubscription_FullMethodName   = "/google.cloud.support.v2.SupportEventSubscriptionService/DeleteSupportEventSubscription"
    	SupportEventSubscriptionService_UndeleteSupportEventSubscription_FullMethodName = "/google.cloud.support.v2.SupportEventSubscriptionService/UndeleteSupportEventSubscription"
    	SupportEventSubscriptionService_ExpungeSupportEventSubscription_FullMethodName  = "/google.cloud.support.v2.SupportEventSubscriptionService/ExpungeSupportEventSubscription"
    )

## Variables 

### Case_State_name, Case_State_value
    
    
    var (
    	Case_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "NEW",
    		2: "IN_PROGRESS_GOOGLE_SUPPORT",
    		3: "ACTION_REQUIRED",
    		4: "SOLUTION_PROVIDED",
    		5: "CLOSED",
    	}
    	Case_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED":          0,
    		"NEW":                        1,
    		"IN_PROGRESS_GOOGLE_SUPPORT": 2,
    		"ACTION_REQUIRED":            3,
    		"SOLUTION_PROVIDED":          4,
    		"CLOSED":                     5,
    	}
    )

Enum value maps for Case_State.

### Case_Priority_name, Case_Priority_value
    
    
    var (
    	Case_Priority_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PRIORITY_UNSPECIFIED",
    		1: "P0",
    		2: "P1",
    		3: "P2",
    		4: "P3",
    		5: "P4",
    	}
    	Case_Priority_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PRIORITY_UNSPECIFIED": 0,
    		"P0":                   1,
    		"P1":                   2,
    		"P2":                   3,
    		"P3":                   4,
    		"P4":                   5,
    	}
    )

Enum value maps for Case_Priority.

### Escalation_Reason_name, Escalation_Reason_value
    
    
    var (
    	Escalation_Reason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "REASON_UNSPECIFIED",
    		1: "RESOLUTION_TIME",
    		2: "TECHNICAL_EXPERTISE",
    		3: "BUSINESS_IMPACT",
    	}
    	Escalation_Reason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"REASON_UNSPECIFIED":  0,
    		"RESOLUTION_TIME":     1,
    		"TECHNICAL_EXPERTISE": 2,
    		"BUSINESS_IMPACT":     3,
    	}
    )

Enum value maps for Escalation_Reason.

### SupportEventSubscription_State_name, SupportEventSubscription_State_value
    
    
    var (
    	SupportEventSubscription_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "WORKING",
    		2: "FAILING",
    		3: "DELETED",
    	}
    	SupportEventSubscription_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"WORKING":           1,
    		"FAILING":           2,
    		"DELETED":           3,
    	}
    )

Enum value maps for SupportEventSubscription_State.

### SupportEventSubscription_FailureReason_name, SupportEventSubscription_FailureReason_value
    
    
    var (
    	SupportEventSubscription_FailureReason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "FAILURE_REASON_UNSPECIFIED",
    		1: "PERMISSION_DENIED",
    		2: "TOPIC_NOT_FOUND",
    		3: "OTHER",
    	}
    	SupportEventSubscription_FailureReason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FAILURE_REASON_UNSPECIFIED": 0,
    		"PERMISSION_DENIED":          1,
    		"TOPIC_NOT_FOUND":            2,
    		"OTHER":                      3,
    	}
    )

Enum value maps for SupportEventSubscription_FailureReason.

### CaseAttachmentService_ServiceDesc
    
    
    var CaseAttachmentService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.support.v2.CaseAttachmentService",
    	HandlerType: (*CaseAttachmentServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListAttachments",
    			Handler:    _CaseAttachmentService_ListAttachments_Handler,
    		},
    		{
    			MethodName: "GetAttachment",
    			Handler:    _CaseAttachmentService_GetAttachment_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/support/v2/attachment_service.proto",
    }

CaseAttachmentService_ServiceDesc is the grpc.ServiceDesc for CaseAttachmentService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### CaseService_ServiceDesc
    
    
    var CaseService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.support.v2.CaseService",
    	HandlerType: (*CaseServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetCase",
    			Handler:    _CaseService_GetCase_Handler,
    		},
    		{
    			MethodName: "ListCases",
    			Handler:    _CaseService_ListCases_Handler,
    		},
    		{
    			MethodName: "SearchCases",
    			Handler:    _CaseService_SearchCases_Handler,
    		},
    		{
    			MethodName: "CreateCase",
    			Handler:    _CaseService_CreateCase_Handler,
    		},
    		{
    			MethodName: "UpdateCase",
    			Handler:    _CaseService_UpdateCase_Handler,
    		},
    		{
    			MethodName: "EscalateCase",
    			Handler:    _CaseService_EscalateCase_Handler,
    		},
    		{
    			MethodName: "CloseCase",
    			Handler:    _CaseService_CloseCase_Handler,
    		},
    		{
    			MethodName: "SearchCaseClassifications",
    			Handler:    _CaseService_SearchCaseClassifications_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/support/v2/case_service.proto",
    }

CaseService_ServiceDesc is the grpc.ServiceDesc for CaseService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### CommentService_ServiceDesc
    
    
    var CommentService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.support.v2.CommentService",
    	HandlerType: (*CommentServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListComments",
    			Handler:    _CommentService_ListComments_Handler,
    		},
    		{
    			MethodName: "CreateComment",
    			Handler:    _CommentService_CreateComment_Handler,
    		},
    		{
    			MethodName: "GetComment",
    			Handler:    _CommentService_GetComment_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/support/v2/comment_service.proto",
    }

CommentService_ServiceDesc is the grpc.ServiceDesc for CommentService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_support_v2_actor_proto
    
    
    var File_google_cloud_support_v2_actor_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_attachment_proto
    
    
    var File_google_cloud_support_v2_attachment_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_attachment_service_proto
    
    
    var File_google_cloud_support_v2_attachment_service_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_case_proto
    
    
    var File_google_cloud_support_v2_case_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_case_service_proto
    
    
    var File_google_cloud_support_v2_case_service_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_comment_proto
    
    
    var File_google_cloud_support_v2_comment_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_comment_service_proto
    
    
    var File_google_cloud_support_v2_comment_service_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_escalation_proto
    
    
    var File_google_cloud_support_v2_escalation_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_support_event_subscription_proto
    
    
    var File_google_cloud_support_v2_support_event_subscription_proto protoreflect.FileDescriptor

### File_google_cloud_support_v2_support_event_subscription_service_proto
    
    
    var File_google_cloud_support_v2_support_event_subscription_service_proto protoreflect.FileDescriptor

### SupportEventSubscriptionService_ServiceDesc
    
    
    var SupportEventSubscriptionService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.support.v2.SupportEventSubscriptionService",
    	HandlerType: (*SupportEventSubscriptionServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_CreateSupportEventSubscription_Handler,
    		},
    		{
    			MethodName: "GetSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_GetSupportEventSubscription_Handler,
    		},
    		{
    			MethodName: "ListSupportEventSubscriptions",
    			Handler:    _SupportEventSubscriptionService_ListSupportEventSubscriptions_Handler,
    		},
    		{
    			MethodName: "UpdateSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_UpdateSupportEventSubscription_Handler,
    		},
    		{
    			MethodName: "DeleteSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_DeleteSupportEventSubscription_Handler,
    		},
    		{
    			MethodName: "UndeleteSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_UndeleteSupportEventSubscription_Handler,
    		},
    		{
    			MethodName: "ExpungeSupportEventSubscription",
    			Handler:    _SupportEventSubscriptionService_ExpungeSupportEventSubscription_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/support/v2/support_event_subscription_service.proto",
    }

SupportEventSubscriptionService_ServiceDesc is the grpc.ServiceDesc for SupportEventSubscriptionService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterCaseAttachmentServiceServer 
    
    
    func RegisterCaseAttachmentServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CaseAttachmentServiceServer)

### func RegisterCaseServiceServer 
    
    
    func RegisterCaseServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CaseServiceServer)

### func RegisterCommentServiceServer 
    
    
    func RegisterCommentServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CommentServiceServer)

### func RegisterSupportEventSubscriptionServiceServer 
    
    
    func RegisterSupportEventSubscriptionServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv SupportEventSubscriptionServiceServer)

## Actor
    
    
    type Actor struct {
    
    	// The name to display for the actor. If not provided, it is inferred from
    	// credentials supplied during case creation. When an email is provided, a
    	// display name must also be provided. This will be obfuscated if the user
    	// is a Google Support agent.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The email address of the actor. If not provided, it is inferred from the
    	// credentials supplied during case creation. When a name is provided, an
    	// email must also be provided. If the user is a Google Support agent, this is
    	// obfuscated.
    	//
    	// This field is deprecated. Use `username` instead.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/support/v2/actor.proto.
    	Email [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=email,proto3" json:"email,omitempty"`
    	// Output only. Whether the actor is a Google support actor.
    	GoogleSupport [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=google_support,json=googleSupport,proto3" json:"google_support,omitempty"`
    	// Output only. The username of the actor. It may look like an email or other
    	// format provided by the identity provider. If not provided, it is inferred
    	// from the credentials supplied. When a name is provided, a username must
    	// also be provided. If the user is a Google Support agent, this will not be
    	// set.
    	Username [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=username,proto3" json:"username,omitempty"`
    	// contains filtered or unexported fields
    }

An Actor represents an entity that performed an action. For example, an actor could be a user who posted a comment on a support case, a user who uploaded an attachment, or a service account that created a support case.

### func (*Actor) Descriptor 
    
    
    func (*Actor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Actor.ProtoReflect.Descriptor instead.

### func (*Actor) GetDisplayName 
    
    
    func (x *Actor) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Actor) GetEmail 
    
    
    func (x *Actor) GetEmail() [string](https://pkg.go.dev/builtin#string)

Deprecated: Marked as deprecated in google/cloud/support/v2/actor.proto.

### func (*Actor) GetGoogleSupport 
    
    
    func (x *Actor) GetGoogleSupport() [bool](https://pkg.go.dev/builtin#bool)

### func (*Actor) GetUsername 
    
    
    func (x *Actor) GetUsername() [string](https://pkg.go.dev/builtin#string)

### func (*Actor) ProtoMessage 
    
    
    func (*Actor) ProtoMessage()

### func (*Actor) ProtoReflect 
    
    
    func (x *Actor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Actor) Reset 
    
    
    func (x *Actor) Reset()

### func (*Actor) String 
    
    
    func (x *Actor) String() [string](https://pkg.go.dev/builtin#string)

## Attachment
    
    
    type Attachment struct {
    
    	// Output only. Identifier. The resource name of the attachment.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The time at which the attachment was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The user who uploaded the attachment. Note, the name and email
    	// will be obfuscated if the attachment was uploaded by Google support.
    	Creator *Actor `protobuf:"bytes,3,opt,name=creator,proto3" json:"creator,omitempty"`
    	// The filename of the attachment (e.g. `"graph.jpg"`).
    	Filename [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filename,proto3" json:"filename,omitempty"`
    	// Output only. The MIME type of the attachment (e.g. text/plain).
    	MimeType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=mime_type,json=mimeType,proto3" json:"mime_type,omitempty"`
    	// Output only. The size of the attachment in bytes.
    	SizeBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,6,opt,name=size_bytes,json=sizeBytes,proto3" json:"size_bytes,omitempty"`
    	// contains filtered or unexported fields
    }

An Attachment contains metadata about a file that was uploaded to a case - it is NOT a file itself. That being said, the name of an Attachment object can be used to download its accompanying file through the `media.download` endpoint.

While attachments can be uploaded in the console at the same time as a comment, they're associated on a "case" level, not a "comment" level.

### func (*Attachment) Descriptor 
    
    
    func (*Attachment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Attachment.ProtoReflect.Descriptor instead.

### func (*Attachment) GetCreateTime 
    
    
    func (x *Attachment) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Attachment) GetCreator 
    
    
    func (x *Attachment) GetCreator() *Actor

### func (*Attachment) GetFilename 
    
    
    func (x *Attachment) GetFilename() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetMimeType 
    
    
    func (x *Attachment) GetMimeType() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetName 
    
    
    func (x *Attachment) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Attachment) GetSizeBytes 
    
    
    func (x *Attachment) GetSizeBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*Attachment) ProtoMessage 
    
    
    func (*Attachment) ProtoMessage()

### func (*Attachment) ProtoReflect 
    
    
    func (x *Attachment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Attachment) Reset 
    
    
    func (x *Attachment) Reset()

### func (*Attachment) String 
    
    
    func (x *Attachment) String() [string](https://pkg.go.dev/builtin#string)

## Case
    
    
    type Case struct {
    
    	// Identifier. The resource name for the case.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The short summary of the issue reported in this case.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A broad description of the issue.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
    	// The issue classification applicable to this case.
    	Classification *CaseClassification `protobuf:"bytes,4,opt,name=classification,proto3" json:"classification,omitempty"`
    	// The timezone of the user who created the support case.
    	// It should be in a format IANA recognizes: https://www.iana.org/time-zones.
    	// There is no additional validation done by the API.
    	TimeZone [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=time_zone,json=timeZone,proto3" json:"time_zone,omitempty"`
    	// The email addresses to receive updates on this case.
    	SubscriberEmailAddresses [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,rep,name=subscriber_email_addresses,json=subscriberEmailAddresses,proto3" json:"subscriber_email_addresses,omitempty"`
    	// Output only. The current status of the support case.
    	State Case_State `protobuf:"varint,12,opt,name=state,proto3,enum=google.cloud.support.v2.Case_State" json:"state,omitempty"`
    	// Output only. The time this case was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,13,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time this case was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,14,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// The user who created the case.
    	//
    	// Note: The name and email will be obfuscated if the case was created by
    	// Google Support.
    	Creator *Actor `protobuf:"bytes,15,opt,name=creator,proto3" json:"creator,omitempty"`
    	// A user-supplied email address to send case update notifications for. This
    	// should only be used in BYOID flows, where we cannot infer the user's email
    	// address directly from their EUCs.
    	ContactEmail [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,35,opt,name=contact_email,json=contactEmail,proto3" json:"contact_email,omitempty"`
    	// Whether the case is currently escalated.
    	Escalated [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,17,opt,name=escalated,proto3" json:"escalated,omitempty"`
    	// Whether this case was created for internal API testing and should not be
    	// acted on by the support team.
    	TestCase [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,19,opt,name=test_case,json=testCase,proto3" json:"test_case,omitempty"`
    	// The language the user has requested to receive support in. This should be a
    	// BCP 47 language code (e.g., `"en"`, `"zh-CN"`, `"zh-TW"`, `"ja"`, `"ko"`).
    	// If no language or an unsupported language is specified, this field defaults
    	// to English (en).
    	//
    	// Language selection during case creation may affect your available support
    	// options. For a list of supported languages and their support working hours,
    	// see: https://cloud.google.com/support/docs/language-working-hours
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,23,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// The priority of this case.
    	Priority Case_Priority `protobuf:"varint,32,opt,name=priority,proto3,enum=google.cloud.support.v2.Case_Priority" json:"priority,omitempty"`
    	// contains filtered or unexported fields
    }

A Case is an object that contains the details of a support case. It contains fields for the time it was created, its priority, its classification, and more. Cases can also have comments and attachments that get added over time.

A case is parented by a Google Cloud organization or project.

Organizations are identified by a number, so the name of a case parented by an organization would look like this:
    
    
    organizations/123/cases/456
    

Projects have two unique identifiers, an ID and a number, and they look like this:
    
    
    projects/abc/cases/456
    
    
    
    projects/123/cases/456
    

You can use either of them when calling the API. To learn more about project identifiers, see [AIP-2510](https://google.aip.dev/cloud/2510).

### func (*Case) Descriptor 
    
    
    func (*Case) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Case.ProtoReflect.Descriptor instead.

### func (*Case) GetClassification 
    
    
    func (x *Case) GetClassification() *CaseClassification

### func (*Case) GetContactEmail 
    
    
    func (x *Case) GetContactEmail() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetCreateTime 
    
    
    func (x *Case) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Case) GetCreator 
    
    
    func (x *Case) GetCreator() *Actor

### func (*Case) GetDescription 
    
    
    func (x *Case) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetDisplayName 
    
    
    func (x *Case) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetEscalated 
    
    
    func (x *Case) GetEscalated() [bool](https://pkg.go.dev/builtin#bool)

### func (*Case) GetLanguageCode 
    
    
    func (x *Case) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetName 
    
    
    func (x *Case) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetPriority 
    
    
    func (x *Case) GetPriority() Case_Priority

### func (*Case) GetState 
    
    
    func (x *Case) GetState() Case_State

### func (*Case) GetSubscriberEmailAddresses 
    
    
    func (x *Case) GetSubscriberEmailAddresses() [][string](https://pkg.go.dev/builtin#string)

### func (*Case) GetTestCase 
    
    
    func (x *Case) GetTestCase() [bool](https://pkg.go.dev/builtin#bool)

### func (*Case) GetTimeZone 
    
    
    func (x *Case) GetTimeZone() [string](https://pkg.go.dev/builtin#string)

### func (*Case) GetUpdateTime 
    
    
    func (x *Case) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Case) ProtoMessage 
    
    
    func (*Case) ProtoMessage()

### func (*Case) ProtoReflect 
    
    
    func (x *Case) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Case) Reset 
    
    
    func (x *Case) Reset()

### func (*Case) String 
    
    
    func (x *Case) String() [string](https://pkg.go.dev/builtin#string)

## CaseAttachmentServiceClient
    
    
    type CaseAttachmentServiceClient interface {
    	// List all the attachments associated with a support case.
    	ListAttachments(ctx context.Context, in *ListAttachmentsRequest, opts ...grpc.CallOption) (*ListAttachmentsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve an attachment associated with a support case.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// attachment="projects/some-project/cases/23598314/attachments/0684M00000P3h1fQAB"
    	//
    	//	curl \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$attachment"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	// request = (
    	//
    	//	supportApiService.cases()
    	//	.attachments()
    	//	.get(name="projects/some-project/cases/43595344/attachments/0684M00000P3h1fQAB")
    	//
    	// )
    	// print(request.execute())
    	// ```
    	GetAttachment(ctx context.Context, in *GetAttachmentRequest, opts ...grpc.CallOption) (*Attachment, [error](https://pkg.go.dev/builtin#error))
    }

CaseAttachmentServiceClient is the client API for CaseAttachmentService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCaseAttachmentServiceClient 
    
    
    func NewCaseAttachmentServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CaseAttachmentServiceClient

## CaseAttachmentServiceServer
    
    
    type CaseAttachmentServiceServer interface {
    	// List all the attachments associated with a support case.
    	ListAttachments(context.Context, *ListAttachmentsRequest) (*ListAttachmentsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve an attachment associated with a support case.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// attachment="projects/some-project/cases/23598314/attachments/0684M00000P3h1fQAB"
    	//
    	//	curl \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$attachment"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	// request = (
    	//
    	//	supportApiService.cases()
    	//	.attachments()
    	//	.get(name="projects/some-project/cases/43595344/attachments/0684M00000P3h1fQAB")
    	//
    	// )
    	// print(request.execute())
    	// ```
    	GetAttachment(context.Context, *GetAttachmentRequest) (*Attachment, [error](https://pkg.go.dev/builtin#error))
    }

CaseAttachmentServiceServer is the server API for CaseAttachmentService service. All implementations should embed UnimplementedCaseAttachmentServiceServer for forward compatibility

## CaseClassification
    
    
    type CaseClassification struct {
    
    	// The unique ID for a classification. Must be specified for case creation.
    	//
    	// To retrieve valid classification IDs for case creation, use
    	// `caseClassifications.search`.
    	//
    	// Classification IDs returned by `caseClassifications.search` are guaranteed
    	// to be valid for at least 6 months. If a given classification is
    	// deactiveated, it will immediately stop being returned. After 6 months,
    	// `case.create` requests using the classification ID will fail.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=id,proto3" json:"id,omitempty"`
    	// A display name for the classification.
    	//
    	// The display name is not static and can change. To uniquely and consistently
    	// identify classifications, use the `CaseClassification.id` field.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

A Case Classification represents the topic that a case is about. It's very important to use accurate classifications, because they're used to route your cases to specialists who can help you.

A classification always has an ID that is its unique identifier. A valid ID is required when creating a case.

### func (*CaseClassification) Descriptor 
    
    
    func (*CaseClassification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CaseClassification.ProtoReflect.Descriptor instead.

### func (*CaseClassification) GetDisplayName 
    
    
    func (x *CaseClassification) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*CaseClassification) GetId 
    
    
    func (x *CaseClassification) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*CaseClassification) ProtoMessage 
    
    
    func (*CaseClassification) ProtoMessage()

### func (*CaseClassification) ProtoReflect 
    
    
    func (x *CaseClassification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CaseClassification) Reset 
    
    
    func (x *CaseClassification) Reset()

### func (*CaseClassification) String 
    
    
    func (x *CaseClassification) String() [string](https://pkg.go.dev/builtin#string)

## CaseServiceClient
    
    
    type CaseServiceClient interface {
    	// Retrieve a case.
    	GetCase(ctx context.Context, in *GetCaseRequest, opts ...grpc.CallOption) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve all cases under a parent, but not its children.
    	//
    	// For example, listing cases under an organization only returns the cases
    	// that are directly parented by that organization. To retrieve cases
    	// under an organization and its projects, use `cases.search`.
    	ListCases(ctx context.Context, in *ListCasesRequest, opts ...grpc.CallOption) (*ListCasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Search for cases using a query.
    	SearchCases(ctx context.Context, in *SearchCasesRequest, opts ...grpc.CallOption) (*SearchCasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Create a new case and associate it with a parent.
    	//
    	// It must have the following fields set: `display_name`, `description`,
    	// `classification`, and `priority`. If you're just testing the API and don't
    	// want to route your case to an agent, set `testCase=true`.
    	CreateCase(ctx context.Context, in *CreateCaseRequest, opts ...grpc.CallOption) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Update a case. Only some fields can be updated.
    	UpdateCase(ctx context.Context, in *UpdateCaseRequest, opts ...grpc.CallOption) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Escalate a case, starting the Google Cloud Support escalation management
    	// process.
    	//
    	// This operation is only available for some support services. Go to
    	// https://cloud.google.com/support and look for 'Technical support
    	// escalations' in the feature list to find out which ones let you
    	// do that.
    	EscalateCase(ctx context.Context, in *EscalateCaseRequest, opts ...grpc.CallOption) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Close a case.
    	CloseCase(ctx context.Context, in *CloseCaseRequest, opts ...grpc.CallOption) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve valid classifications to use when creating a support case.
    	//
    	// Classifications are hierarchical. Each classification is a string
    	// containing all levels of the hierarchy separated by `" > "`. For example,
    	// `"Technical Issue > Compute > Compute Engine"`.
    	//
    	// Classification IDs returned by this endpoint are valid for at least six
    	// months. When a classification is deactivated, this endpoint immediately
    	// stops returning it. After six months, `case.create` requests using the
    	// classification will fail.
    	SearchCaseClassifications(ctx context.Context, in *SearchCaseClassificationsRequest, opts ...grpc.CallOption) (*SearchCaseClassificationsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CaseServiceClient is the client API for CaseService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCaseServiceClient 
    
    
    func NewCaseServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CaseServiceClient

## CaseServiceServer
    
    
    type CaseServiceServer interface {
    	// Retrieve a case.
    	GetCase(context.Context, *GetCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve all cases under a parent, but not its children.
    	//
    	// For example, listing cases under an organization only returns the cases
    	// that are directly parented by that organization. To retrieve cases
    	// under an organization and its projects, use `cases.search`.
    	ListCases(context.Context, *ListCasesRequest) (*ListCasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Search for cases using a query.
    	SearchCases(context.Context, *SearchCasesRequest) (*SearchCasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Create a new case and associate it with a parent.
    	//
    	// It must have the following fields set: `display_name`, `description`,
    	// `classification`, and `priority`. If you're just testing the API and don't
    	// want to route your case to an agent, set `testCase=true`.
    	CreateCase(context.Context, *CreateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Update a case. Only some fields can be updated.
    	UpdateCase(context.Context, *UpdateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Escalate a case, starting the Google Cloud Support escalation management
    	// process.
    	//
    	// This operation is only available for some support services. Go to
    	// https://cloud.google.com/support and look for 'Technical support
    	// escalations' in the feature list to find out which ones let you
    	// do that.
    	EscalateCase(context.Context, *EscalateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Close a case.
    	CloseCase(context.Context, *CloseCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve valid classifications to use when creating a support case.
    	//
    	// Classifications are hierarchical. Each classification is a string
    	// containing all levels of the hierarchy separated by `" > "`. For example,
    	// `"Technical Issue > Compute > Compute Engine"`.
    	//
    	// Classification IDs returned by this endpoint are valid for at least six
    	// months. When a classification is deactivated, this endpoint immediately
    	// stops returning it. After six months, `case.create` requests using the
    	// classification will fail.
    	SearchCaseClassifications(context.Context, *SearchCaseClassificationsRequest) (*SearchCaseClassificationsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CaseServiceServer is the server API for CaseService service. All implementations should embed UnimplementedCaseServiceServer for forward compatibility

## Case_Priority
    
    
    type Case_Priority [int32](https://pkg.go.dev/builtin#int32)

The case Priority. P0 is most urgent and P4 the least.

### Case_PRIORITY_UNSPECIFIED, Case_P0, Case_P1, Case_P2, Case_P3, Case_P4
    
    
    const (
    	// Priority is undefined or has not been set yet.
    	Case_PRIORITY_UNSPECIFIED Case_Priority = 0
    	// Extreme impact on a production service. Service is hard down.
    	Case_P0 Case_Priority = 1
    	// Critical impact on a production service. Service is currently unusable.
    	Case_P1 Case_Priority = 2
    	// Severe impact on a production service. Service is usable but greatly
    	// impaired.
    	Case_P2 Case_Priority = 3
    	// Medium impact on a production service.  Service is available, but
    	// moderately impaired.
    	Case_P3 Case_Priority = 4
    	// General questions or minor issues.  Production service is fully
    	// available.
    	Case_P4 Case_Priority = 5
    )

### func (Case_Priority) Descriptor 
    
    
    func (Case_Priority) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Case_Priority) Enum 
    
    
    func (x Case_Priority) Enum() *Case_Priority

### func (Case_Priority) EnumDescriptor 
    
    
    func (Case_Priority) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Case_Priority.Descriptor instead.

### func (Case_Priority) Number 
    
    
    func (x Case_Priority) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Case_Priority) String 
    
    
    func (x Case_Priority) String() [string](https://pkg.go.dev/builtin#string)

### func (Case_Priority) Type 
    
    
    func (Case_Priority) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Case_State
    
    
    type Case_State [int32](https://pkg.go.dev/builtin#int32)

The status of a support case.

### Case_STATE_UNSPECIFIED, Case_NEW, Case_IN_PROGRESS_GOOGLE_SUPPORT, Case_ACTION_REQUIRED, Case_SOLUTION_PROVIDED, Case_CLOSED
    
    
    const (
    	// Case is in an unknown state.
    	Case_STATE_UNSPECIFIED Case_State = 0
    	// The case has been created but no one is assigned to work on it yet.
    	Case_NEW Case_State = 1
    	// The case is currently being handled by Google support.
    	Case_IN_PROGRESS_GOOGLE_SUPPORT Case_State = 2
    	// Google is waiting for a response.
    	Case_ACTION_REQUIRED Case_State = 3
    	// A solution has been offered for the case, but it isn't yet closed.
    	Case_SOLUTION_PROVIDED Case_State = 4
    	// The case has been resolved.
    	Case_CLOSED Case_State = 5
    )

### func (Case_State) Descriptor 
    
    
    func (Case_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Case_State) Enum 
    
    
    func (x Case_State) Enum() *Case_State

### func (Case_State) EnumDescriptor 
    
    
    func (Case_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Case_State.Descriptor instead.

### func (Case_State) Number 
    
    
    func (x Case_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Case_State) String 
    
    
    func (x Case_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Case_State) Type 
    
    
    func (Case_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CloseCaseRequest
    
    
    type CloseCaseRequest struct {
    
    	// Required. The name of the case to close.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the CloseCase endpoint.

### func (*CloseCaseRequest) Descriptor 
    
    
    func (*CloseCaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloseCaseRequest.ProtoReflect.Descriptor instead.

### func (*CloseCaseRequest) GetName 
    
    
    func (x *CloseCaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CloseCaseRequest) ProtoMessage 
    
    
    func (*CloseCaseRequest) ProtoMessage()

### func (*CloseCaseRequest) ProtoReflect 
    
    
    func (x *CloseCaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CloseCaseRequest) Reset 
    
    
    func (x *CloseCaseRequest) Reset()

### func (*CloseCaseRequest) String 
    
    
    func (x *CloseCaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## Comment
    
    
    type Comment struct {
    
    	// Output only. Identifier. The resource name of the comment.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The time when the comment was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The user or Google Support agent who created the comment.
    	Creator *Actor `protobuf:"bytes,3,opt,name=creator,proto3" json:"creator,omitempty"`
    	// The full comment body.
    	//
    	// Maximum of 12800 characters.
    	Body [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=body,proto3" json:"body,omitempty"`
    	// Output only. DEPRECATED. DO NOT USE.
    	//
    	// A duplicate of the `body` field.
    	//
    	// This field is only present for legacy reasons.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/support/v2/comment.proto.
    	PlainTextBody [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=plain_text_body,json=plainTextBody,proto3" json:"plain_text_body,omitempty"`
    	// contains filtered or unexported fields
    }

A comment associated with a support case.

Case comments are the primary way for Google Support to communicate with a user who has opened a case. When a user responds to Google Support, the user's responses also appear as comments.

### func (*Comment) Descriptor 
    
    
    func (*Comment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Comment.ProtoReflect.Descriptor instead.

### func (*Comment) GetBody 
    
    
    func (x *Comment) GetBody() [string](https://pkg.go.dev/builtin#string)

### func (*Comment) GetCreateTime 
    
    
    func (x *Comment) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Comment) GetCreator 
    
    
    func (x *Comment) GetCreator() *Actor

### func (*Comment) GetName 
    
    
    func (x *Comment) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Comment) GetPlainTextBody 
    
    
    func (x *Comment) GetPlainTextBody() [string](https://pkg.go.dev/builtin#string)

Deprecated: Marked as deprecated in google/cloud/support/v2/comment.proto.

### func (*Comment) ProtoMessage 
    
    
    func (*Comment) ProtoMessage()

### func (*Comment) ProtoReflect 
    
    
    func (x *Comment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Comment) Reset 
    
    
    func (x *Comment) Reset()

### func (*Comment) String 
    
    
    func (x *Comment) String() [string](https://pkg.go.dev/builtin#string)

## CommentServiceClient
    
    
    type CommentServiceClient interface {
    	// List all the comments associated with a case.
    	ListComments(ctx context.Context, in *ListCommentsRequest, opts ...grpc.CallOption) (*ListCommentsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Add a new comment to a case.
    	//
    	// The comment must have the following fields set: `body`.
    	CreateComment(ctx context.Context, in *CreateCommentRequest, opts ...grpc.CallOption) (*Comment, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve a comment.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// comment="projects/some-project/cases/43595344/comments/234567890"
    	//
    	//	curl \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$comment"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	//
    	// request = supportApiService.cases().comments().get(
    	//
    	//	name="projects/some-project/cases/43595344/comments/234567890",
    	//
    	// )
    	// print(request.execute())
    	// ```
    	GetComment(ctx context.Context, in *GetCommentRequest, opts ...grpc.CallOption) (*Comment, [error](https://pkg.go.dev/builtin#error))
    }

CommentServiceClient is the client API for CommentService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCommentServiceClient 
    
    
    func NewCommentServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CommentServiceClient

## CommentServiceServer
    
    
    type CommentServiceServer interface {
    	// List all the comments associated with a case.
    	ListComments(context.Context, *ListCommentsRequest) (*ListCommentsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Add a new comment to a case.
    	//
    	// The comment must have the following fields set: `body`.
    	CreateComment(context.Context, *CreateCommentRequest) (*Comment, [error](https://pkg.go.dev/builtin#error))
    	// Retrieve a comment.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// comment="projects/some-project/cases/43595344/comments/234567890"
    	//
    	//	curl \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$comment"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	//
    	// request = supportApiService.cases().comments().get(
    	//
    	//	name="projects/some-project/cases/43595344/comments/234567890",
    	//
    	// )
    	// print(request.execute())
    	// ```
    	GetComment(context.Context, *GetCommentRequest) (*Comment, [error](https://pkg.go.dev/builtin#error))
    }

CommentServiceServer is the server API for CommentService service. All implementations should embed UnimplementedCommentServiceServer for forward compatibility

## CreateCaseRequest
    
    
    type CreateCaseRequest struct {
    
    	// Required. The name of the parent under which the case should be created.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The case to be created.
    	Case *Case `protobuf:"bytes,2,opt,name=case,proto3" json:"case,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the CreateCase endpoint.

### func (*CreateCaseRequest) Descriptor 
    
    
    func (*CreateCaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateCaseRequest.ProtoReflect.Descriptor instead.

### func (*CreateCaseRequest) GetCase 
    
    
    func (x *CreateCaseRequest) GetCase() *Case

### func (*CreateCaseRequest) GetParent 
    
    
    func (x *CreateCaseRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateCaseRequest) ProtoMessage 
    
    
    func (*CreateCaseRequest) ProtoMessage()

### func (*CreateCaseRequest) ProtoReflect 
    
    
    func (x *CreateCaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateCaseRequest) Reset 
    
    
    func (x *CreateCaseRequest) Reset()

### func (*CreateCaseRequest) String 
    
    
    func (x *CreateCaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateCommentRequest
    
    
    type CreateCommentRequest struct {
    
    	// Required. The name of the case to which the comment should be added.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The comment to be added.
    	Comment *Comment `protobuf:"bytes,2,opt,name=comment,proto3" json:"comment,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the CreateComment endpoint.

### func (*CreateCommentRequest) Descriptor 
    
    
    func (*CreateCommentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateCommentRequest.ProtoReflect.Descriptor instead.

### func (*CreateCommentRequest) GetComment 
    
    
    func (x *CreateCommentRequest) GetComment() *Comment

### func (*CreateCommentRequest) GetParent 
    
    
    func (x *CreateCommentRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateCommentRequest) ProtoMessage 
    
    
    func (*CreateCommentRequest) ProtoMessage()

### func (*CreateCommentRequest) ProtoReflect 
    
    
    func (x *CreateCommentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateCommentRequest) Reset 
    
    
    func (x *CreateCommentRequest) Reset()

### func (*CreateCommentRequest) String 
    
    
    func (x *CreateCommentRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateSupportEventSubscriptionRequest
    
    
    type CreateSupportEventSubscriptionRequest struct {
    
    	// Required. The parent resource name where the support event subscription
    	// will be created. Format: organizations/{organization_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The Pub/Sub configuration to create.
    	SupportEventSubscription *SupportEventSubscription `protobuf:"bytes,2,opt,name=support_event_subscription,json=supportEventSubscription,proto3" json:"support_event_subscription,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for CreateSupportEventSubscription.

### func (*CreateSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*CreateSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*CreateSupportEventSubscriptionRequest) GetParent 
    
    
    func (x *CreateSupportEventSubscriptionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSupportEventSubscriptionRequest) GetSupportEventSubscription 
    
    
    func (x *CreateSupportEventSubscriptionRequest) GetSupportEventSubscription() *SupportEventSubscription

### func (*CreateSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*CreateSupportEventSubscriptionRequest) ProtoMessage()

### func (*CreateSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *CreateSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateSupportEventSubscriptionRequest) Reset 
    
    
    func (x *CreateSupportEventSubscriptionRequest) Reset()

### func (*CreateSupportEventSubscriptionRequest) String 
    
    
    func (x *CreateSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteSupportEventSubscriptionRequest
    
    
    type DeleteSupportEventSubscriptionRequest struct {
    
    	// Required. The name of the support event subscription to delete.
    	// Format:
    	// organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for DeleteSupportEventSubscription.

### func (*DeleteSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*DeleteSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteSupportEventSubscriptionRequest) GetName 
    
    
    func (x *DeleteSupportEventSubscriptionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*DeleteSupportEventSubscriptionRequest) ProtoMessage()

### func (*DeleteSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *DeleteSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteSupportEventSubscriptionRequest) Reset 
    
    
    func (x *DeleteSupportEventSubscriptionRequest) Reset()

### func (*DeleteSupportEventSubscriptionRequest) String 
    
    
    func (x *DeleteSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

## EscalateCaseRequest
    
    
    type EscalateCaseRequest struct {
    
    	// Required. The name of the case to be escalated.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The escalation information to be sent with the escalation request.
    	Escalation *Escalation `protobuf:"bytes,2,opt,name=escalation,proto3" json:"escalation,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the EscalateCase endpoint.

### func (*EscalateCaseRequest) Descriptor 
    
    
    func (*EscalateCaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EscalateCaseRequest.ProtoReflect.Descriptor instead.

### func (*EscalateCaseRequest) GetEscalation 
    
    
    func (x *EscalateCaseRequest) GetEscalation() *Escalation

### func (*EscalateCaseRequest) GetName 
    
    
    func (x *EscalateCaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*EscalateCaseRequest) ProtoMessage 
    
    
    func (*EscalateCaseRequest) ProtoMessage()

### func (*EscalateCaseRequest) ProtoReflect 
    
    
    func (x *EscalateCaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EscalateCaseRequest) Reset 
    
    
    func (x *EscalateCaseRequest) Reset()

### func (*EscalateCaseRequest) String 
    
    
    func (x *EscalateCaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## Escalation
    
    
    type Escalation struct {
    
    	// Required. The reason why the Case is being escalated.
    	Reason Escalation_Reason `protobuf:"varint,4,opt,name=reason,proto3,enum=google.cloud.support.v2.Escalation_Reason" json:"reason,omitempty"`
    	// Required. A free text description to accompany the `reason` field above.
    	// Provides additional context on why the case is being escalated.
    	Justification [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=justification,proto3" json:"justification,omitempty"`
    	// contains filtered or unexported fields
    }

An escalation of a support case.

### func (*Escalation) Descriptor 
    
    
    func (*Escalation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Escalation.ProtoReflect.Descriptor instead.

### func (*Escalation) GetJustification 
    
    
    func (x *Escalation) GetJustification() [string](https://pkg.go.dev/builtin#string)

### func (*Escalation) GetReason 
    
    
    func (x *Escalation) GetReason() Escalation_Reason

### func (*Escalation) ProtoMessage 
    
    
    func (*Escalation) ProtoMessage()

### func (*Escalation) ProtoReflect 
    
    
    func (x *Escalation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Escalation) Reset 
    
    
    func (x *Escalation) Reset()

### func (*Escalation) String 
    
    
    func (x *Escalation) String() [string](https://pkg.go.dev/builtin#string)

## Escalation_Reason
    
    
    type Escalation_Reason [int32](https://pkg.go.dev/builtin#int32)

An enum detailing the possible reasons a case may be escalated.

### Escalation_REASON_UNSPECIFIED, Escalation_RESOLUTION_TIME, Escalation_TECHNICAL_EXPERTISE, Escalation_BUSINESS_IMPACT
    
    
    const (
    	// The escalation reason is in an unknown state or has not been specified.
    	Escalation_REASON_UNSPECIFIED Escalation_Reason = 0
    	// The case is taking too long to resolve.
    	Escalation_RESOLUTION_TIME Escalation_Reason = 1
    	// The support agent does not have the expertise required to successfully
    	// resolve the issue.
    	Escalation_TECHNICAL_EXPERTISE Escalation_Reason = 2
    	// The issue is having a significant business impact.
    	Escalation_BUSINESS_IMPACT Escalation_Reason = 3
    )

### func (Escalation_Reason) Descriptor 
    
    
    func (Escalation_Reason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Escalation_Reason) Enum 
    
    
    func (x Escalation_Reason) Enum() *Escalation_Reason

### func (Escalation_Reason) EnumDescriptor 
    
    
    func (Escalation_Reason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Escalation_Reason.Descriptor instead.

### func (Escalation_Reason) Number 
    
    
    func (x Escalation_Reason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Escalation_Reason) String 
    
    
    func (x Escalation_Reason) String() [string](https://pkg.go.dev/builtin#string)

### func (Escalation_Reason) Type 
    
    
    func (Escalation_Reason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ExpungeSupportEventSubscriptionRequest
    
    
    type ExpungeSupportEventSubscriptionRequest struct {
    
    	// Required. The name of the support event subscription to expunge.
    	// Format:
    	// organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for ExpungeSupportEventSubscription.

### func (*ExpungeSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*ExpungeSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExpungeSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*ExpungeSupportEventSubscriptionRequest) GetName 
    
    
    func (x *ExpungeSupportEventSubscriptionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ExpungeSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*ExpungeSupportEventSubscriptionRequest) ProtoMessage()

### func (*ExpungeSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *ExpungeSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ExpungeSupportEventSubscriptionRequest) Reset 
    
    
    func (x *ExpungeSupportEventSubscriptionRequest) Reset()

### func (*ExpungeSupportEventSubscriptionRequest) String 
    
    
    func (x *ExpungeSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetAttachmentRequest
    
    
    type GetAttachmentRequest struct {
    
    	// Required. The name of the attachment to get.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for getting an attachment.

### func (*GetAttachmentRequest) Descriptor 
    
    
    func (*GetAttachmentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAttachmentRequest.ProtoReflect.Descriptor instead.

### func (*GetAttachmentRequest) GetName 
    
    
    func (x *GetAttachmentRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAttachmentRequest) ProtoMessage 
    
    
    func (*GetAttachmentRequest) ProtoMessage()

### func (*GetAttachmentRequest) ProtoReflect 
    
    
    func (x *GetAttachmentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAttachmentRequest) Reset 
    
    
    func (x *GetAttachmentRequest) Reset()

### func (*GetAttachmentRequest) String 
    
    
    func (x *GetAttachmentRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetCaseRequest
    
    
    type GetCaseRequest struct {
    
    	// Required. The full name of a case to be retrieved.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the GetCase endpoint.

### func (*GetCaseRequest) Descriptor 
    
    
    func (*GetCaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCaseRequest.ProtoReflect.Descriptor instead.

### func (*GetCaseRequest) GetName 
    
    
    func (x *GetCaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCaseRequest) ProtoMessage 
    
    
    func (*GetCaseRequest) ProtoMessage()

### func (*GetCaseRequest) ProtoReflect 
    
    
    func (x *GetCaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCaseRequest) Reset 
    
    
    func (x *GetCaseRequest) Reset()

### func (*GetCaseRequest) String 
    
    
    func (x *GetCaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetCommentRequest
    
    
    type GetCommentRequest struct {
    
    	// Required. The name of the comment to retrieve.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the GetComment endpoint.

### func (*GetCommentRequest) Descriptor 
    
    
    func (*GetCommentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCommentRequest.ProtoReflect.Descriptor instead.

### func (*GetCommentRequest) GetName 
    
    
    func (x *GetCommentRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCommentRequest) ProtoMessage 
    
    
    func (*GetCommentRequest) ProtoMessage()

### func (*GetCommentRequest) ProtoReflect 
    
    
    func (x *GetCommentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCommentRequest) Reset 
    
    
    func (x *GetCommentRequest) Reset()

### func (*GetCommentRequest) String 
    
    
    func (x *GetCommentRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSupportEventSubscriptionRequest
    
    
    type GetSupportEventSubscriptionRequest struct {
    
    	// Required. The name of the support event subscription to retrieve.
    	// Format:
    	// organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for GetSupportEventSubscription.

### func (*GetSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*GetSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*GetSupportEventSubscriptionRequest) GetName 
    
    
    func (x *GetSupportEventSubscriptionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*GetSupportEventSubscriptionRequest) ProtoMessage()

### func (*GetSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *GetSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSupportEventSubscriptionRequest) Reset 
    
    
    func (x *GetSupportEventSubscriptionRequest) Reset()

### func (*GetSupportEventSubscriptionRequest) String 
    
    
    func (x *GetSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAttachmentsRequest
    
    
    type ListAttachmentsRequest struct {
    
    	// Required. The name of the case for which attachments should be listed.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of attachments fetched with each request.
    	//
    	// If not provided, the default is 10. The maximum page size that will be
    	// returned is 100.
    	//
    	// The size of each page can be smaller than the requested page size and can
    	// include zero. For example, you could request 100 attachments on one page,
    	// receive 0, and then on the next page, receive 90.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying the page of results to return. If unspecified, the
    	// first page is retrieved.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the ListAttachments endpoint.

### func (*ListAttachmentsRequest) Descriptor 
    
    
    func (*ListAttachmentsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAttachmentsRequest.ProtoReflect.Descriptor instead.

### func (*ListAttachmentsRequest) GetPageSize 
    
    
    func (x *ListAttachmentsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAttachmentsRequest) GetPageToken 
    
    
    func (x *ListAttachmentsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAttachmentsRequest) GetParent 
    
    
    func (x *ListAttachmentsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAttachmentsRequest) ProtoMessage 
    
    
    func (*ListAttachmentsRequest) ProtoMessage()

### func (*ListAttachmentsRequest) ProtoReflect 
    
    
    func (x *ListAttachmentsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAttachmentsRequest) Reset 
    
    
    func (x *ListAttachmentsRequest) Reset()

### func (*ListAttachmentsRequest) String 
    
    
    func (x *ListAttachmentsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAttachmentsResponse
    
    
    type ListAttachmentsResponse struct {
    
    	// The list of attachments associated with a case.
    	Attachments []*Attachment `protobuf:"bytes,1,rep,name=attachments,proto3" json:"attachments,omitempty"`
    	// A token to retrieve the next page of results. Set this in the `page_token`
    	// field of subsequent `cases.attachments.list` requests. If unspecified,
    	// there are no more results to retrieve.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for the ListAttachments endpoint.

### func (*ListAttachmentsResponse) Descriptor 
    
    
    func (*ListAttachmentsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAttachmentsResponse.ProtoReflect.Descriptor instead.

### func (*ListAttachmentsResponse) GetAttachments 
    
    
    func (x *ListAttachmentsResponse) GetAttachments() []*Attachment

### func (*ListAttachmentsResponse) GetNextPageToken 
    
    
    func (x *ListAttachmentsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAttachmentsResponse) ProtoMessage 
    
    
    func (*ListAttachmentsResponse) ProtoMessage()

### func (*ListAttachmentsResponse) ProtoReflect 
    
    
    func (x *ListAttachmentsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAttachmentsResponse) Reset 
    
    
    func (x *ListAttachmentsResponse) Reset()

### func (*ListAttachmentsResponse) String 
    
    
    func (x *ListAttachmentsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListCasesRequest
    
    
    type ListCasesRequest struct {
    
    	// Required. The name of a parent to list cases under.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// An expression used to filter cases.
    	//
    	// If it's an empty string, then no filtering happens. Otherwise, the endpoint
    	// returns the cases that match the filter.
    	//
    	// Expressions use the following fields separated by `AND` and specified with
    	// `=`:
    	//
    	// - `state`: Can be `OPEN` or `CLOSED`.
    	// - `priority`: Can be `P0`, `P1`, `P2`, `P3`, or `P4`. You
    	// can specify multiple values for priority using the `OR` operator. For
    	// example, `priority=P1 OR priority=P2`.
    	// - `creator.email`: The email address of the case creator.
    	//
    	// EXAMPLES:
    	//
    	// - `state=CLOSED`
    	// - `state=OPEN AND creator.email="tester@example.com"`
    	// - `state=OPEN AND (priority=P0 OR priority=P1)`
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=filter,proto3" json:"filter,omitempty"`
    	// The maximum number of cases fetched with each request. Defaults to 10.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying the page of results to return. If unspecified, the
    	// first page is retrieved.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the ListCases endpoint.

### func (*ListCasesRequest) Descriptor 
    
    
    func (*ListCasesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCasesRequest.ProtoReflect.Descriptor instead.

### func (*ListCasesRequest) GetFilter 
    
    
    func (x *ListCasesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListCasesRequest) GetPageSize 
    
    
    func (x *ListCasesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListCasesRequest) GetPageToken 
    
    
    func (x *ListCasesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCasesRequest) GetParent 
    
    
    func (x *ListCasesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListCasesRequest) ProtoMessage 
    
    
    func (*ListCasesRequest) ProtoMessage()

### func (*ListCasesRequest) ProtoReflect 
    
    
    func (x *ListCasesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCasesRequest) Reset 
    
    
    func (x *ListCasesRequest) Reset()

### func (*ListCasesRequest) String 
    
    
    func (x *ListCasesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCasesResponse
    
    
    type ListCasesResponse struct {
    
    	// The list of cases associated with the parent after any
    	// filters have been applied.
    	Cases []*Case `protobuf:"bytes,1,rep,name=cases,proto3" json:"cases,omitempty"`
    	// A token to retrieve the next page of results. Set this in the `page_token`
    	// field of subsequent `cases.list` requests. If unspecified, there are no
    	// more results to retrieve.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for the ListCases endpoint.

### func (*ListCasesResponse) Descriptor 
    
    
    func (*ListCasesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCasesResponse.ProtoReflect.Descriptor instead.

### func (*ListCasesResponse) GetCases 
    
    
    func (x *ListCasesResponse) GetCases() []*Case

### func (*ListCasesResponse) GetNextPageToken 
    
    
    func (x *ListCasesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCasesResponse) ProtoMessage 
    
    
    func (*ListCasesResponse) ProtoMessage()

### func (*ListCasesResponse) ProtoReflect 
    
    
    func (x *ListCasesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCasesResponse) Reset 
    
    
    func (x *ListCasesResponse) Reset()

### func (*ListCasesResponse) String 
    
    
    func (x *ListCasesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListCommentsRequest
    
    
    type ListCommentsRequest struct {
    
    	// Required. The name of the case for which to list comments.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of comments to fetch. Defaults to 10.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying the page of results to return. If unspecified, the
    	// first page is returned.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the ListComments endpoint.

### func (*ListCommentsRequest) Descriptor 
    
    
    func (*ListCommentsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCommentsRequest.ProtoReflect.Descriptor instead.

### func (*ListCommentsRequest) GetPageSize 
    
    
    func (x *ListCommentsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListCommentsRequest) GetPageToken 
    
    
    func (x *ListCommentsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCommentsRequest) GetParent 
    
    
    func (x *ListCommentsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListCommentsRequest) ProtoMessage 
    
    
    func (*ListCommentsRequest) ProtoMessage()

### func (*ListCommentsRequest) ProtoReflect 
    
    
    func (x *ListCommentsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCommentsRequest) Reset 
    
    
    func (x *ListCommentsRequest) Reset()

### func (*ListCommentsRequest) String 
    
    
    func (x *ListCommentsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCommentsResponse
    
    
    type ListCommentsResponse struct {
    
    	// List of the comments associated with the case.
    	Comments []*Comment `protobuf:"bytes,1,rep,name=comments,proto3" json:"comments,omitempty"`
    	// A token to retrieve the next page of results. Set this in the `page_token`
    	// field of subsequent `cases.comments.list` requests. If unspecified, there
    	// are no more results to retrieve.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for the ListComments endpoint.

### func (*ListCommentsResponse) Descriptor 
    
    
    func (*ListCommentsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCommentsResponse.ProtoReflect.Descriptor instead.

### func (*ListCommentsResponse) GetComments 
    
    
    func (x *ListCommentsResponse) GetComments() []*Comment

### func (*ListCommentsResponse) GetNextPageToken 
    
    
    func (x *ListCommentsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCommentsResponse) ProtoMessage 
    
    
    func (*ListCommentsResponse) ProtoMessage()

### func (*ListCommentsResponse) ProtoReflect 
    
    
    func (x *ListCommentsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCommentsResponse) Reset 
    
    
    func (x *ListCommentsResponse) Reset()

### func (*ListCommentsResponse) String 
    
    
    func (x *ListCommentsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSupportEventSubscriptionsRequest
    
    
    type ListSupportEventSubscriptionsRequest struct {
    
    	// Required. The fully qualified name of the Cloud resource to list support
    	// event subscriptions under. Format: organizations/{organization_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Filter expression based on AIP-160.
    	// Supported fields:
    	// - pub_sub_topic
    	// - state
    	//
    	// Examples:
    	// - `pub_sub_topic="projects/example-project/topics/example-topic"`
    	// - `state=WORKING`
    	// - `pub_sub_topic="projects/example-project/topics/example-topic" AND
    	// state=WORKING`
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Whether to show deleted subscriptions. By default, deleted
    	// subscriptions are not returned.
    	ShowDeleted [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=show_deleted,json=showDeleted,proto3" json:"show_deleted,omitempty"`
    	// Optional. The maximum number of support event subscriptions to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying the page of results to return. If
    	// unspecified, the first page is retrieved.
    	//
    	// When paginating, all other parameters provided to
    	// `ListSupportEventSubscriptions` must match the call that provided the page
    	// token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for ListSupportEventSubscriptions.

### func (*ListSupportEventSubscriptionsRequest) Descriptor 
    
    
    func (*ListSupportEventSubscriptionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSupportEventSubscriptionsRequest.ProtoReflect.Descriptor instead.

### func (*ListSupportEventSubscriptionsRequest) GetFilter 
    
    
    func (x *ListSupportEventSubscriptionsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListSupportEventSubscriptionsRequest) GetPageSize 
    
    
    func (x *ListSupportEventSubscriptionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSupportEventSubscriptionsRequest) GetPageToken 
    
    
    func (x *ListSupportEventSubscriptionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSupportEventSubscriptionsRequest) GetParent 
    
    
    func (x *ListSupportEventSubscriptionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListSupportEventSubscriptionsRequest) GetShowDeleted 
    
    
    func (x *ListSupportEventSubscriptionsRequest) GetShowDeleted() [bool](https://pkg.go.dev/builtin#bool)

### func (*ListSupportEventSubscriptionsRequest) ProtoMessage 
    
    
    func (*ListSupportEventSubscriptionsRequest) ProtoMessage()

### func (*ListSupportEventSubscriptionsRequest) ProtoReflect 
    
    
    func (x *ListSupportEventSubscriptionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSupportEventSubscriptionsRequest) Reset 
    
    
    func (x *ListSupportEventSubscriptionsRequest) Reset()

### func (*ListSupportEventSubscriptionsRequest) String 
    
    
    func (x *ListSupportEventSubscriptionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSupportEventSubscriptionsResponse
    
    
    type ListSupportEventSubscriptionsResponse struct {
    
    	// The support event subscriptions.
    	SupportEventSubscriptions []*SupportEventSubscription `protobuf:"bytes,1,rep,name=support_event_subscriptions,json=supportEventSubscriptions,proto3" json:"support_event_subscriptions,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for ListSupportEventSubscriptions.

### func (*ListSupportEventSubscriptionsResponse) Descriptor 
    
    
    func (*ListSupportEventSubscriptionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSupportEventSubscriptionsResponse.ProtoReflect.Descriptor instead.

### func (*ListSupportEventSubscriptionsResponse) GetNextPageToken 
    
    
    func (x *ListSupportEventSubscriptionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSupportEventSubscriptionsResponse) GetSupportEventSubscriptions 
    
    
    func (x *ListSupportEventSubscriptionsResponse) GetSupportEventSubscriptions() []*SupportEventSubscription

### func (*ListSupportEventSubscriptionsResponse) ProtoMessage 
    
    
    func (*ListSupportEventSubscriptionsResponse) ProtoMessage()

### func (*ListSupportEventSubscriptionsResponse) ProtoReflect 
    
    
    func (x *ListSupportEventSubscriptionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSupportEventSubscriptionsResponse) Reset 
    
    
    func (x *ListSupportEventSubscriptionsResponse) Reset()

### func (*ListSupportEventSubscriptionsResponse) String 
    
    
    func (x *ListSupportEventSubscriptionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchCaseClassificationsRequest
    
    
    type SearchCaseClassificationsRequest struct {
    
    	// An expression used to filter case classifications.
    	//
    	// If it's an empty string, then no filtering happens. Otherwise, case
    	// classifications will be returned that match the filter.
    	Query [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
    	// The maximum number of classifications fetched with each request.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying the page of results to return. If unspecified, the
    	// first page is retrieved.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the SearchCaseClassifications endpoint.

### func (*SearchCaseClassificationsRequest) Descriptor 
    
    
    func (*SearchCaseClassificationsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCaseClassificationsRequest.ProtoReflect.Descriptor instead.

### func (*SearchCaseClassificationsRequest) GetPageSize 
    
    
    func (x *SearchCaseClassificationsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchCaseClassificationsRequest) GetPageToken 
    
    
    func (x *SearchCaseClassificationsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCaseClassificationsRequest) GetQuery 
    
    
    func (x *SearchCaseClassificationsRequest) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCaseClassificationsRequest) ProtoMessage 
    
    
    func (*SearchCaseClassificationsRequest) ProtoMessage()

### func (*SearchCaseClassificationsRequest) ProtoReflect 
    
    
    func (x *SearchCaseClassificationsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCaseClassificationsRequest) Reset 
    
    
    func (x *SearchCaseClassificationsRequest) Reset()

### func (*SearchCaseClassificationsRequest) String 
    
    
    func (x *SearchCaseClassificationsRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchCaseClassificationsResponse
    
    
    type SearchCaseClassificationsResponse struct {
    
    	// The classifications retrieved.
    	CaseClassifications []*CaseClassification `protobuf:"bytes,1,rep,name=case_classifications,json=caseClassifications,proto3" json:"case_classifications,omitempty"`
    	// A token to retrieve the next page of results. Set this in the `page_token`
    	// field of subsequent `caseClassifications.list` requests. If unspecified,
    	// there are no more results to retrieve.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for SearchCaseClassifications endpoint.

### func (*SearchCaseClassificationsResponse) Descriptor 
    
    
    func (*SearchCaseClassificationsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCaseClassificationsResponse.ProtoReflect.Descriptor instead.

### func (*SearchCaseClassificationsResponse) GetCaseClassifications 
    
    
    func (x *SearchCaseClassificationsResponse) GetCaseClassifications() []*CaseClassification

### func (*SearchCaseClassificationsResponse) GetNextPageToken 
    
    
    func (x *SearchCaseClassificationsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCaseClassificationsResponse) ProtoMessage 
    
    
    func (*SearchCaseClassificationsResponse) ProtoMessage()

### func (*SearchCaseClassificationsResponse) ProtoReflect 
    
    
    func (x *SearchCaseClassificationsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCaseClassificationsResponse) Reset 
    
    
    func (x *SearchCaseClassificationsResponse) Reset()

### func (*SearchCaseClassificationsResponse) String 
    
    
    func (x *SearchCaseClassificationsResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchCasesRequest
    
    
    type SearchCasesRequest struct {
    
    	// The name of the parent resource to search for cases under.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=parent,proto3" json:"parent,omitempty"`
    	// An expression used to filter cases.
    	//
    	// Expressions use the following fields separated by `AND` and specified with
    	// `=`:
    	//
    	// - `state`: Can be `OPEN` or `CLOSED`.
    	// - `priority`: Can be `P0`, `P1`, `P2`, `P3`, or `P4`. You
    	// can specify multiple values for priority using the `OR` operator. For
    	// example, `priority=P1 OR priority=P2`.
    	// - `creator.email`: The email address of the case creator.
    	//
    	// To search across `displayName`, `description`, and comments, use a global
    	// restriction with no keyword or operator. For example, `"my search"`.
    	//
    	// To search only cases updated after a certain date, use `update_time`
    	// restricted with that particular date, time, and timezone in ISO datetime
    	// format. For example, `update_time>"2020-01-01T00:00:00-05:00"`.
    	// `update_time` only supports the greater than operator (`>`).
    	//
    	// If you are using the `v2` version of the API, you must specify the case
    	// parent in the `parent` field. If you provide an empty `query`, all cases
    	// under the parent resource will be returned.
    	//
    	// If you are using the `v2beta` version of the API, you must specify the case
    	// parent in the `query` field using one of the two fields below, which are
    	// only available for `v2beta`. The `parent` field will be ignored.
    	//
    	// - `organization`: An organization name in the form
    	// `organizations/

The request message for the SearchCases endpoint.

### func (*SearchCasesRequest) Descriptor 
    
    
    func (*SearchCasesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCasesRequest.ProtoReflect.Descriptor instead.

### func (*SearchCasesRequest) GetPageSize 
    
    
    func (x *SearchCasesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchCasesRequest) GetPageToken 
    
    
    func (x *SearchCasesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCasesRequest) GetParent 
    
    
    func (x *SearchCasesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCasesRequest) GetQuery 
    
    
    func (x *SearchCasesRequest) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCasesRequest) ProtoMessage 
    
    
    func (*SearchCasesRequest) ProtoMessage()

### func (*SearchCasesRequest) ProtoReflect 
    
    
    func (x *SearchCasesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCasesRequest) Reset 
    
    
    func (x *SearchCasesRequest) Reset()

### func (*SearchCasesRequest) String 
    
    
    func (x *SearchCasesRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchCasesResponse
    
    
    type SearchCasesResponse struct {
    
    	// The list of cases associated with the parent after any
    	// filters have been applied.
    	Cases []*Case `protobuf:"bytes,1,rep,name=cases,proto3" json:"cases,omitempty"`
    	// A token to retrieve the next page of results. Set this in the
    	// `page_token` field of subsequent `cases.search` requests. If unspecified,
    	// there are no more results to retrieve.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

The response message for the SearchCases endpoint.

### func (*SearchCasesResponse) Descriptor 
    
    
    func (*SearchCasesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCasesResponse.ProtoReflect.Descriptor instead.

### func (*SearchCasesResponse) GetCases 
    
    
    func (x *SearchCasesResponse) GetCases() []*Case

### func (*SearchCasesResponse) GetNextPageToken 
    
    
    func (x *SearchCasesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCasesResponse) ProtoMessage 
    
    
    func (*SearchCasesResponse) ProtoMessage()

### func (*SearchCasesResponse) ProtoReflect 
    
    
    func (x *SearchCasesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCasesResponse) Reset 
    
    
    func (x *SearchCasesResponse) Reset()

### func (*SearchCasesResponse) String 
    
    
    func (x *SearchCasesResponse) String() [string](https://pkg.go.dev/builtin#string)

## SupportEventSubscription
    
    
    type SupportEventSubscription struct {
    
    	// Identifier. The resource name of the support event subscription.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The name of the Pub/Sub topic to publish notifications to.
    	// Format: projects/{project}/topics/{topic}
    	PubSubTopic [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=pub_sub_topic,json=pubSubTopic,proto3" json:"pub_sub_topic,omitempty"`
    	// Output only. The state of the subscription.
    	State SupportEventSubscription_State `protobuf:"varint,3,opt,name=state,proto3,enum=google.cloud.support.v2.SupportEventSubscription_State" json:"state,omitempty"`
    	// Output only. Reason why subscription is failing. State of subscription
    	// must be FAILING in order for this to have a value.
    	FailureReason SupportEventSubscription_FailureReason `protobuf:"varint,4,opt,name=failure_reason,json=failureReason,proto3,enum=google.cloud.support.v2.SupportEventSubscription_FailureReason" json:"failure_reason,omitempty"`
    	// Output only. The time at which the subscription was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time at which the subscription was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. The time at which the subscription was deleted.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,7,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Output only. The time at which the subscription will be purged.
    	PurgeTime *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=purge_time,json=purgeTime,proto3" json:"purge_time,omitempty"`
    	// contains filtered or unexported fields
    }

A support event subscription.

You can also manage support event subscriptions using other tools:

  * [`gcloud support support-event-subscriptions`](https://docs.cloud.google.com/sdk/gcloud/reference/support/support-event-subscriptions) (or [`gcloud beta`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/support/support-event-subscriptions) for beta)
  * [Terraform `google_cloud_support_support_event_subscription`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription) (or [google-beta provider](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription) for beta)



### func (*SupportEventSubscription) Descriptor 
    
    
    func (*SupportEventSubscription) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SupportEventSubscription.ProtoReflect.Descriptor instead.

### func (*SupportEventSubscription) GetCreateTime 
    
    
    func (x *SupportEventSubscription) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SupportEventSubscription) GetDeleteTime 
    
    
    func (x *SupportEventSubscription) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SupportEventSubscription) GetFailureReason 
    
    
    func (x *SupportEventSubscription) GetFailureReason() SupportEventSubscription_FailureReason

### func (*SupportEventSubscription) GetName 
    
    
    func (x *SupportEventSubscription) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SupportEventSubscription) GetPubSubTopic 
    
    
    func (x *SupportEventSubscription) GetPubSubTopic() [string](https://pkg.go.dev/builtin#string)

### func (*SupportEventSubscription) GetPurgeTime 
    
    
    func (x *SupportEventSubscription) GetPurgeTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SupportEventSubscription) GetState 
    
    
    func (x *SupportEventSubscription) GetState() SupportEventSubscription_State

### func (*SupportEventSubscription) GetUpdateTime 
    
    
    func (x *SupportEventSubscription) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*SupportEventSubscription) ProtoMessage 
    
    
    func (*SupportEventSubscription) ProtoMessage()

### func (*SupportEventSubscription) ProtoReflect 
    
    
    func (x *SupportEventSubscription) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SupportEventSubscription) Reset 
    
    
    func (x *SupportEventSubscription) Reset()

### func (*SupportEventSubscription) String 
    
    
    func (x *SupportEventSubscription) String() [string](https://pkg.go.dev/builtin#string)

## SupportEventSubscriptionServiceClient
    
    
    type SupportEventSubscriptionServiceClient interface {
    	// Creates a support event subscription for an organization.
    	CreateSupportEventSubscription(ctx context.Context, in *CreateSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Gets a support event subscription.
    	GetSupportEventSubscription(ctx context.Context, in *GetSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Lists support event subscriptions for an organization.
    	ListSupportEventSubscriptions(ctx context.Context, in *ListSupportEventSubscriptionsRequest, opts ...grpc.CallOption) (*ListSupportEventSubscriptionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates a support event subscription.
    	UpdateSupportEventSubscription(ctx context.Context, in *UpdateSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Soft deletes a support event subscription.
    	DeleteSupportEventSubscription(ctx context.Context, in *DeleteSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Undeletes a support event subscription.
    	UndeleteSupportEventSubscription(ctx context.Context, in *UndeleteSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Expunges a support event subscription.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// support_event_subscription="organizations/123456789/supportEventSubscriptions/abcdef123456"
    	//
    	//	curl \
    	//	  --request POST \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$support_event_subscription:expunge"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	//
    	// request = supportApiService.supportEventSubscriptions().expunge(
    	//
    	//	name="organizations/123456789/supportEventSubscriptions/abcdef123456"
    	//
    	// )
    	// print(request.execute())
    	// ```
    	ExpungeSupportEventSubscription(ctx context.Context, in *ExpungeSupportEventSubscriptionRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

SupportEventSubscriptionServiceClient is the client API for SupportEventSubscriptionService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewSupportEventSubscriptionServiceClient 
    
    
    func NewSupportEventSubscriptionServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) SupportEventSubscriptionServiceClient

## SupportEventSubscriptionServiceServer
    
    
    type SupportEventSubscriptionServiceServer interface {
    	// Creates a support event subscription for an organization.
    	CreateSupportEventSubscription(context.Context, *CreateSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Gets a support event subscription.
    	GetSupportEventSubscription(context.Context, *GetSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Lists support event subscriptions for an organization.
    	ListSupportEventSubscriptions(context.Context, *ListSupportEventSubscriptionsRequest) (*ListSupportEventSubscriptionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates a support event subscription.
    	UpdateSupportEventSubscription(context.Context, *UpdateSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Soft deletes a support event subscription.
    	DeleteSupportEventSubscription(context.Context, *DeleteSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Undeletes a support event subscription.
    	UndeleteSupportEventSubscription(context.Context, *UndeleteSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))
    	// Expunges a support event subscription.
    	//
    	// EXAMPLES:
    	//
    	// cURL:
    	//
    	// ```shell
    	// support_event_subscription="organizations/123456789/supportEventSubscriptions/abcdef123456"
    	//
    	//	curl \
    	//	  --request POST \
    	//	  --header "Authorization: Bearer $(gcloud auth print-access-token)" \
    	//	  "https://cloudsupport.googleapis.com/v2/$support_event_subscription:expunge"
    	//
    	// ```
    	//
    	// Python:
    	//
    	// ```python
    	// import googleapiclient.discovery
    	//
    	// api_version = "v2"
    	// supportApiService = googleapiclient.discovery.build(
    	//
    	//	serviceName="cloudsupport",
    	//	version=api_version,
    	//	discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    	//
    	// )
    	//
    	// request = supportApiService.supportEventSubscriptions().expunge(
    	//
    	//	name="organizations/123456789/supportEventSubscriptions/abcdef123456"
    	//
    	// )
    	// print(request.execute())
    	// ```
    	ExpungeSupportEventSubscription(context.Context, *ExpungeSupportEventSubscriptionRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

SupportEventSubscriptionServiceServer is the server API for SupportEventSubscriptionService service. All implementations should embed UnimplementedSupportEventSubscriptionServiceServer for forward compatibility

## SupportEventSubscription_FailureReason
    
    
    type SupportEventSubscription_FailureReason [int32](https://pkg.go.dev/builtin#int32)

The reason why the subscription is failing.

### SupportEventSubscription_FAILURE_REASON_UNSPECIFIED, SupportEventSubscription_PERMISSION_DENIED, SupportEventSubscription_TOPIC_NOT_FOUND, SupportEventSubscription_OTHER
    
    
    const (
    	// Unspecified failure reason.
    	SupportEventSubscription_FAILURE_REASON_UNSPECIFIED SupportEventSubscription_FailureReason = 0
    	// The service account (i.e.
    	// cloud-support-apievents@system.gserviceaccount.com) lacks the permission
    	// to publish to the customer's Pub/Sub topic.
    	SupportEventSubscription_PERMISSION_DENIED SupportEventSubscription_FailureReason = 1
    	// The specified Pub/Sub topic does not exist.
    	SupportEventSubscription_TOPIC_NOT_FOUND SupportEventSubscription_FailureReason = 2
    	// Message failed to publish due to a system-side error.
    	SupportEventSubscription_OTHER SupportEventSubscription_FailureReason = 3
    )

### func (SupportEventSubscription_FailureReason) Descriptor 
    
    
    func (SupportEventSubscription_FailureReason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SupportEventSubscription_FailureReason) Enum 
    
    
    func (x SupportEventSubscription_FailureReason) Enum() *SupportEventSubscription_FailureReason

### func (SupportEventSubscription_FailureReason) EnumDescriptor 
    
    
    func (SupportEventSubscription_FailureReason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SupportEventSubscription_FailureReason.Descriptor instead.

### func (SupportEventSubscription_FailureReason) Number 
    
    
    func (x SupportEventSubscription_FailureReason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SupportEventSubscription_FailureReason) String 
    
    
    func (x SupportEventSubscription_FailureReason) String() [string](https://pkg.go.dev/builtin#string)

### func (SupportEventSubscription_FailureReason) Type 
    
    
    func (SupportEventSubscription_FailureReason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SupportEventSubscription_State
    
    
    type SupportEventSubscription_State [int32](https://pkg.go.dev/builtin#int32)

The state of the subscription.

### SupportEventSubscription_STATE_UNSPECIFIED, SupportEventSubscription_WORKING, SupportEventSubscription_FAILING, SupportEventSubscription_DELETED
    
    
    const (
    	// Unspecified state.
    	SupportEventSubscription_STATE_UNSPECIFIED SupportEventSubscription_State = 0
    	// Subscription is active and working.
    	SupportEventSubscription_WORKING SupportEventSubscription_State = 1
    	// Subscription is failing. Notifications cannot be published for some
    	// reason.
    	SupportEventSubscription_FAILING SupportEventSubscription_State = 2
    	// Subscription has been deleted and is pending purge. Notifications are not
    	// sent for deleted subscriptions. Deleted subscriptions are purged after
    	// their `purge_time` has passed.
    	SupportEventSubscription_DELETED SupportEventSubscription_State = 3
    )

### func (SupportEventSubscription_State) Descriptor 
    
    
    func (SupportEventSubscription_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SupportEventSubscription_State) Enum 
    
    
    func (x SupportEventSubscription_State) Enum() *SupportEventSubscription_State

### func (SupportEventSubscription_State) EnumDescriptor 
    
    
    func (SupportEventSubscription_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SupportEventSubscription_State.Descriptor instead.

### func (SupportEventSubscription_State) Number 
    
    
    func (x SupportEventSubscription_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SupportEventSubscription_State) String 
    
    
    func (x SupportEventSubscription_State) String() [string](https://pkg.go.dev/builtin#string)

### func (SupportEventSubscription_State) Type 
    
    
    func (SupportEventSubscription_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UndeleteSupportEventSubscriptionRequest
    
    
    type UndeleteSupportEventSubscriptionRequest struct {
    
    	// Required. The name of the support event subscription to undelete.
    	// Format:
    	// organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for UndeleteSupportEventSubscription.

### func (*UndeleteSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*UndeleteSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UndeleteSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*UndeleteSupportEventSubscriptionRequest) GetName 
    
    
    func (x *UndeleteSupportEventSubscriptionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*UndeleteSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*UndeleteSupportEventSubscriptionRequest) ProtoMessage()

### func (*UndeleteSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *UndeleteSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UndeleteSupportEventSubscriptionRequest) Reset 
    
    
    func (x *UndeleteSupportEventSubscriptionRequest) Reset()

### func (*UndeleteSupportEventSubscriptionRequest) String 
    
    
    func (x *UndeleteSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedCaseAttachmentServiceServer
    
    
    type UnimplementedCaseAttachmentServiceServer struct {
    }

UnimplementedCaseAttachmentServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedCaseAttachmentServiceServer) GetAttachment 
    
    
    func (UnimplementedCaseAttachmentServiceServer) GetAttachment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAttachmentRequest) (*Attachment, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseAttachmentServiceServer) ListAttachments 
    
    
    func (UnimplementedCaseAttachmentServiceServer) ListAttachments([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAttachmentsRequest) (*ListAttachmentsResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedCaseServiceServer
    
    
    type UnimplementedCaseServiceServer struct {
    }

UnimplementedCaseServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedCaseServiceServer) CloseCase 
    
    
    func (UnimplementedCaseServiceServer) CloseCase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CloseCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) CreateCase 
    
    
    func (UnimplementedCaseServiceServer) CreateCase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) EscalateCase 
    
    
    func (UnimplementedCaseServiceServer) EscalateCase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *EscalateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) GetCase 
    
    
    func (UnimplementedCaseServiceServer) GetCase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) ListCases 
    
    
    func (UnimplementedCaseServiceServer) ListCases([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListCasesRequest) (*ListCasesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) SearchCaseClassifications 
    
    
    func (UnimplementedCaseServiceServer) SearchCaseClassifications([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchCaseClassificationsRequest) (*SearchCaseClassificationsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) SearchCases 
    
    
    func (UnimplementedCaseServiceServer) SearchCases([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchCasesRequest) (*SearchCasesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCaseServiceServer) UpdateCase 
    
    
    func (UnimplementedCaseServiceServer) UpdateCase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateCaseRequest) (*Case, [error](https://pkg.go.dev/builtin#error))

## UnimplementedCommentServiceServer
    
    
    type UnimplementedCommentServiceServer struct {
    }

UnimplementedCommentServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedCommentServiceServer) CreateComment 
    
    
    func (UnimplementedCommentServiceServer) CreateComment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateCommentRequest) (*Comment, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCommentServiceServer) GetComment 
    
    
    func (UnimplementedCommentServiceServer) GetComment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCommentRequest) (*Comment, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCommentServiceServer) ListComments 
    
    
    func (UnimplementedCommentServiceServer) ListComments([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListCommentsRequest) (*ListCommentsResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedSupportEventSubscriptionServiceServer
    
    
    type UnimplementedSupportEventSubscriptionServiceServer struct {
    }

UnimplementedSupportEventSubscriptionServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedSupportEventSubscriptionServiceServer) CreateSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) CreateSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) DeleteSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) DeleteSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) ExpungeSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) ExpungeSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ExpungeSupportEventSubscriptionRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) GetSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) GetSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) ListSupportEventSubscriptions 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) ListSupportEventSubscriptions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSupportEventSubscriptionsRequest) (*ListSupportEventSubscriptionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) UndeleteSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) UndeleteSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UndeleteSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedSupportEventSubscriptionServiceServer) UpdateSupportEventSubscription 
    
    
    func (UnimplementedSupportEventSubscriptionServiceServer) UpdateSupportEventSubscription([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSupportEventSubscriptionRequest) (*SupportEventSubscription, [error](https://pkg.go.dev/builtin#error))

## UnsafeCaseAttachmentServiceServer
    
    
    type UnsafeCaseAttachmentServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCaseAttachmentServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CaseAttachmentServiceServer will result in compilation errors.

## UnsafeCaseServiceServer
    
    
    type UnsafeCaseServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCaseServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CaseServiceServer will result in compilation errors.

## UnsafeCommentServiceServer
    
    
    type UnsafeCommentServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCommentServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CommentServiceServer will result in compilation errors.

## UnsafeSupportEventSubscriptionServiceServer
    
    
    type UnsafeSupportEventSubscriptionServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeSupportEventSubscriptionServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to SupportEventSubscriptionServiceServer will result in compilation errors.

## UpdateCaseRequest
    
    
    type UpdateCaseRequest struct {
    
    	// Required. The case to update.
    	Case *Case `protobuf:"bytes,1,opt,name=case,proto3" json:"case,omitempty"`
    	// A list of attributes of the case that should be updated. Supported values
    	// are `priority`, `display_name`, and `subscriber_email_addresses`. If no
    	// fields are specified, all supported fields are updated.
    	//
    	// Be careful - if you do not provide a field mask, then you might
    	// accidentally clear some fields. For example, if you leave the field mask
    	// empty and do not provide a value for `subscriber_email_addresses`, then
    	// `subscriber_email_addresses` is updated to empty.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

The request message for the UpdateCase endpoint

### func (*UpdateCaseRequest) Descriptor 
    
    
    func (*UpdateCaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateCaseRequest.ProtoReflect.Descriptor instead.

### func (*UpdateCaseRequest) GetCase 
    
    
    func (x *UpdateCaseRequest) GetCase() *Case

### func (*UpdateCaseRequest) GetUpdateMask 
    
    
    func (x *UpdateCaseRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateCaseRequest) ProtoMessage 
    
    
    func (*UpdateCaseRequest) ProtoMessage()

### func (*UpdateCaseRequest) ProtoReflect 
    
    
    func (x *UpdateCaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateCaseRequest) Reset 
    
    
    func (x *UpdateCaseRequest) Reset()

### func (*UpdateCaseRequest) String 
    
    
    func (x *UpdateCaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSupportEventSubscriptionRequest
    
    
    type UpdateSupportEventSubscriptionRequest struct {
    
    	// Required. The support event subscription to update.
    	// The `name` field is used to identify the configuration to update.
    	SupportEventSubscription *SupportEventSubscription `protobuf:"bytes,1,opt,name=support_event_subscription,json=supportEventSubscription,proto3" json:"support_event_subscription,omitempty"`
    	// Optional. The list of fields to update. The only supported value is
    	// pub_sub_topic.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for UpdateSupportEventSubscription.

### func (*UpdateSupportEventSubscriptionRequest) Descriptor 
    
    
    func (*UpdateSupportEventSubscriptionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSupportEventSubscriptionRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSupportEventSubscriptionRequest) GetSupportEventSubscription 
    
    
    func (x *UpdateSupportEventSubscriptionRequest) GetSupportEventSubscription() *SupportEventSubscription

### func (*UpdateSupportEventSubscriptionRequest) GetUpdateMask 
    
    
    func (x *UpdateSupportEventSubscriptionRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSupportEventSubscriptionRequest) ProtoMessage 
    
    
    func (*UpdateSupportEventSubscriptionRequest) ProtoMessage()

### func (*UpdateSupportEventSubscriptionRequest) ProtoReflect 
    
    
    func (x *UpdateSupportEventSubscriptionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSupportEventSubscriptionRequest) Reset 
    
    
    func (x *UpdateSupportEventSubscriptionRequest) Reset()

### func (*UpdateSupportEventSubscriptionRequest) String 
    
    
    func (x *UpdateSupportEventSubscriptionRequest) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
