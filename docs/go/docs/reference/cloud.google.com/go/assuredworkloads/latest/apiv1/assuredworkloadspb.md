---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/assuredworkloads/latest/apiv1/assuredworkloadspb/
title: Assured Workloads API v1 - Package cloud.google.com/go/assuredworkloads/apiv1/assuredworkloadspb (v1.20.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:48.304109+00:00
---

# Assured Workloads API v1 - Package cloud.google.com/go/assuredworkloads/apiv1/assuredworkloadspb (v1.20.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/assuredworkloads/latest/apiv1/assuredworkloadspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Assured Workloads API v1 - Package cloud.google.com/go/assuredworkloads/apiv1/assuredworkloadspb (v1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.6  1.11.12  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/assuredworkloads/apiv1/assuredworkloadspb). 

##  Constants 

### AssuredWorkloadsService_CreateWorkload_FullMethodName, AssuredWorkloadsService_UpdateWorkload_FullMethodName, AssuredWorkloadsService_RestrictAllowedResources_FullMethodName, AssuredWorkloadsService_DeleteWorkload_FullMethodName, AssuredWorkloadsService_GetWorkload_FullMethodName, AssuredWorkloadsService_ListWorkloads_FullMethodName, AssuredWorkloadsService_ListViolations_FullMethodName, AssuredWorkloadsService_GetViolation_FullMethodName, AssuredWorkloadsService_AcknowledgeViolation_FullMethodName
    
    
    const (
    	AssuredWorkloadsService_CreateWorkload_FullMethodName           = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/CreateWorkload"
    	AssuredWorkloadsService_UpdateWorkload_FullMethodName           = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/UpdateWorkload"
    	AssuredWorkloadsService_RestrictAllowedResources_FullMethodName = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/RestrictAllowedResources"
    	AssuredWorkloadsService_DeleteWorkload_FullMethodName           = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/DeleteWorkload"
    	AssuredWorkloadsService_GetWorkload_FullMethodName              = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/GetWorkload"
    	AssuredWorkloadsService_ListWorkloads_FullMethodName            = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/ListWorkloads"
    	AssuredWorkloadsService_ListViolations_FullMethodName           = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/ListViolations"
    	AssuredWorkloadsService_GetViolation_FullMethodName             = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/GetViolation"
    	AssuredWorkloadsService_AcknowledgeViolation_FullMethodName     = "/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/AcknowledgeViolation"
    )

## Variables 

### Workload_ComplianceRegime_name, Workload_ComplianceRegime_value
    
    
    var (
    	Workload_ComplianceRegime_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "COMPLIANCE_REGIME_UNSPECIFIED",
    		1:  "IL4",
    		2:  "CJIS",
    		3:  "FEDRAMP_HIGH",
    		4:  "FEDRAMP_MODERATE",
    		5:  "US_REGIONAL_ACCESS",
    		6:  "HIPAA",
    		7:  "HITRUST",
    		8:  "EU_REGIONS_AND_SUPPORT",
    		9:  "CA_REGIONS_AND_SUPPORT",
    		10: "ITAR",
    		11: "AU_REGIONS_AND_US_SUPPORT",
    		12: "ASSURED_WORKLOADS_FOR_PARTNERS",
    	}
    	Workload_ComplianceRegime_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMPLIANCE_REGIME_UNSPECIFIED":  0,
    		"IL4":                            1,
    		"CJIS":                           2,
    		"FEDRAMP_HIGH":                   3,
    		"FEDRAMP_MODERATE":               4,
    		"US_REGIONAL_ACCESS":             5,
    		"HIPAA":                          6,
    		"HITRUST":                        7,
    		"EU_REGIONS_AND_SUPPORT":         8,
    		"CA_REGIONS_AND_SUPPORT":         9,
    		"ITAR":                           10,
    		"AU_REGIONS_AND_US_SUPPORT":      11,
    		"ASSURED_WORKLOADS_FOR_PARTNERS": 12,
    	}
    )

Enum value maps for Workload_ComplianceRegime.

### Workload_KajEnrollmentState_name, Workload_KajEnrollmentState_value
    
    
    var (
    	Workload_KajEnrollmentState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "KAJ_ENROLLMENT_STATE_UNSPECIFIED",
    		1: "KAJ_ENROLLMENT_STATE_PENDING",
    		2: "KAJ_ENROLLMENT_STATE_COMPLETE",
    	}
    	Workload_KajEnrollmentState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"KAJ_ENROLLMENT_STATE_UNSPECIFIED": 0,
    		"KAJ_ENROLLMENT_STATE_PENDING":     1,
    		"KAJ_ENROLLMENT_STATE_COMPLETE":    2,
    	}
    )

Enum value maps for Workload_KajEnrollmentState.

### Workload_Partner_name, Workload_Partner_value
    
    
    var (
    	Workload_Partner_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PARTNER_UNSPECIFIED",
    		1: "LOCAL_CONTROLS_BY_S3NS",
    	}
    	Workload_Partner_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PARTNER_UNSPECIFIED":    0,
    		"LOCAL_CONTROLS_BY_S3NS": 1,
    	}
    )

Enum value maps for Workload_Partner.

### Workload_ResourceInfo_ResourceType_name, Workload_ResourceInfo_ResourceType_value
    
    
    var (
    	Workload_ResourceInfo_ResourceType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RESOURCE_TYPE_UNSPECIFIED",
    		1: "CONSUMER_PROJECT",
    		4: "CONSUMER_FOLDER",
    		2: "ENCRYPTION_KEYS_PROJECT",
    		3: "KEYRING",
    	}
    	Workload_ResourceInfo_ResourceType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RESOURCE_TYPE_UNSPECIFIED": 0,
    		"CONSUMER_PROJECT":          1,
    		"CONSUMER_FOLDER":           4,
    		"ENCRYPTION_KEYS_PROJECT":   2,
    		"KEYRING":                   3,
    	}
    )

Enum value maps for Workload_ResourceInfo_ResourceType.

### Workload_SaaEnrollmentResponse_SetupState_name, Workload_SaaEnrollmentResponse_SetupState_value
    
    
    var (
    	Workload_SaaEnrollmentResponse_SetupState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SETUP_STATE_UNSPECIFIED",
    		1: "STATUS_PENDING",
    		2: "STATUS_COMPLETE",
    	}
    	Workload_SaaEnrollmentResponse_SetupState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SETUP_STATE_UNSPECIFIED": 0,
    		"STATUS_PENDING":          1,
    		"STATUS_COMPLETE":         2,
    	}
    )

Enum value maps for Workload_SaaEnrollmentResponse_SetupState.

### Workload_SaaEnrollmentResponse_SetupError_name, Workload_SaaEnrollmentResponse_SetupError_value
    
    
    var (
    	Workload_SaaEnrollmentResponse_SetupError_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SETUP_ERROR_UNSPECIFIED",
    		1: "ERROR_INVALID_BASE_SETUP",
    		2: "ERROR_MISSING_EXTERNAL_SIGNING_KEY",
    		3: "ERROR_NOT_ALL_SERVICES_ENROLLED",
    		4: "ERROR_SETUP_CHECK_FAILED",
    	}
    	Workload_SaaEnrollmentResponse_SetupError_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SETUP_ERROR_UNSPECIFIED":            0,
    		"ERROR_INVALID_BASE_SETUP":           1,
    		"ERROR_MISSING_EXTERNAL_SIGNING_KEY": 2,
    		"ERROR_NOT_ALL_SERVICES_ENROLLED":    3,
    		"ERROR_SETUP_CHECK_FAILED":           4,
    	}
    )

Enum value maps for Workload_SaaEnrollmentResponse_SetupError.

### RestrictAllowedResourcesRequest_RestrictionType_name, RestrictAllowedResourcesRequest_RestrictionType_value
    
    
    var (
    	RestrictAllowedResourcesRequest_RestrictionType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RESTRICTION_TYPE_UNSPECIFIED",
    		1: "ALLOW_ALL_GCP_RESOURCES",
    		2: "ALLOW_COMPLIANT_RESOURCES",
    	}
    	RestrictAllowedResourcesRequest_RestrictionType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RESTRICTION_TYPE_UNSPECIFIED": 0,
    		"ALLOW_ALL_GCP_RESOURCES":      1,
    		"ALLOW_COMPLIANT_RESOURCES":    2,
    	}
    )

Enum value maps for RestrictAllowedResourcesRequest_RestrictionType.

### Violation_State_name, Violation_State_value
    
    
    var (
    	Violation_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		2: "RESOLVED",
    		3: "UNRESOLVED",
    		4: "EXCEPTION",
    	}
    	Violation_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"RESOLVED":          2,
    		"UNRESOLVED":        3,
    		"EXCEPTION":         4,
    	}
    )

Enum value maps for Violation_State.

### Violation_Remediation_RemediationType_name, Violation_Remediation_RemediationType_value
    
    
    var (
    	Violation_Remediation_RemediationType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "REMEDIATION_TYPE_UNSPECIFIED",
    		1: "REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION",
    		2: "REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION",
    		3: "REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION",
    		4: "REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION",
    	}
    	Violation_Remediation_RemediationType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"REMEDIATION_TYPE_UNSPECIFIED":                                       0,
    		"REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION":                           1,
    		"REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION":               2,
    		"REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION":                3,
    		"REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION": 4,
    	}
    )

Enum value maps for Violation_Remediation_RemediationType.

### AssuredWorkloadsService_ServiceDesc
    
    
    var AssuredWorkloadsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.assuredworkloads.v1.AssuredWorkloadsService",
    	HandlerType: (*AssuredWorkloadsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateWorkload",
    			Handler:    _AssuredWorkloadsService_CreateWorkload_Handler,
    		},
    		{
    			MethodName: "UpdateWorkload",
    			Handler:    _AssuredWorkloadsService_UpdateWorkload_Handler,
    		},
    		{
    			MethodName: "RestrictAllowedResources",
    			Handler:    _AssuredWorkloadsService_RestrictAllowedResources_Handler,
    		},
    		{
    			MethodName: "DeleteWorkload",
    			Handler:    _AssuredWorkloadsService_DeleteWorkload_Handler,
    		},
    		{
    			MethodName: "GetWorkload",
    			Handler:    _AssuredWorkloadsService_GetWorkload_Handler,
    		},
    		{
    			MethodName: "ListWorkloads",
    			Handler:    _AssuredWorkloadsService_ListWorkloads_Handler,
    		},
    		{
    			MethodName: "ListViolations",
    			Handler:    _AssuredWorkloadsService_ListViolations_Handler,
    		},
    		{
    			MethodName: "GetViolation",
    			Handler:    _AssuredWorkloadsService_GetViolation_Handler,
    		},
    		{
    			MethodName: "AcknowledgeViolation",
    			Handler:    _AssuredWorkloadsService_AcknowledgeViolation_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/assuredworkloads/v1/assuredworkloads.proto",
    }

AssuredWorkloadsService_ServiceDesc is the grpc.ServiceDesc for AssuredWorkloadsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_assuredworkloads_v1_assuredworkloads_proto
    
    
    var File_google_cloud_assuredworkloads_v1_assuredworkloads_proto protoreflect.FileDescriptor

## Functions 

### func RegisterAssuredWorkloadsServiceServer 
    
    
    func RegisterAssuredWorkloadsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AssuredWorkloadsServiceServer)

## AcknowledgeViolationRequest
    
    
    type AcknowledgeViolationRequest struct {
    
    	// Required. The resource name of the Violation to acknowledge.
    	// Format:
    	// organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Business justification explaining the need for violation acknowledgement
    	Comment [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=comment,proto3" json:"comment,omitempty"`
    	// Optional. This field is deprecated and will be removed in future version of the API.
    	// Name of the OrgPolicy which was modified with non-compliant change and
    	// resulted in this violation.
    	// Format:
    	// projects/{project_number}/policies/{constraint_name}
    	// folders/{folder_id}/policies/{constraint_name}
    	// organizations/{organization_id}/policies/{constraint_name}
    	//
    	// Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.
    	NonCompliantOrgPolicy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=non_compliant_org_policy,json=nonCompliantOrgPolicy,proto3" json:"non_compliant_org_policy,omitempty"`
    	// contains filtered or unexported fields
    }

Request for acknowledging the violation Next Id: 4

### func (*AcknowledgeViolationRequest) Descriptor 
    
    
    func (*AcknowledgeViolationRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AcknowledgeViolationRequest.ProtoReflect.Descriptor instead.

### func (*AcknowledgeViolationRequest) GetComment 
    
    
    func (x *AcknowledgeViolationRequest) GetComment() [string](https://pkg.go.dev/builtin#string)

### func (*AcknowledgeViolationRequest) GetName 
    
    
    func (x *AcknowledgeViolationRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AcknowledgeViolationRequest) GetNonCompliantOrgPolicy 
    
    
    func (x *AcknowledgeViolationRequest) GetNonCompliantOrgPolicy() [string](https://pkg.go.dev/builtin#string)

Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.

### func (*AcknowledgeViolationRequest) ProtoMessage 
    
    
    func (*AcknowledgeViolationRequest) ProtoMessage()

### func (*AcknowledgeViolationRequest) ProtoReflect 
    
    
    func (x *AcknowledgeViolationRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AcknowledgeViolationRequest) Reset 
    
    
    func (x *AcknowledgeViolationRequest) Reset()

### func (*AcknowledgeViolationRequest) String 
    
    
    func (x *AcknowledgeViolationRequest) String() [string](https://pkg.go.dev/builtin#string)

## AcknowledgeViolationResponse
    
    
    type AcknowledgeViolationResponse struct {
    	// contains filtered or unexported fields
    }

Response for violation acknowledgement

### func (*AcknowledgeViolationResponse) Descriptor 
    
    
    func (*AcknowledgeViolationResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AcknowledgeViolationResponse.ProtoReflect.Descriptor instead.

### func (*AcknowledgeViolationResponse) ProtoMessage 
    
    
    func (*AcknowledgeViolationResponse) ProtoMessage()

### func (*AcknowledgeViolationResponse) ProtoReflect 
    
    
    func (x *AcknowledgeViolationResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AcknowledgeViolationResponse) Reset 
    
    
    func (x *AcknowledgeViolationResponse) Reset()

### func (*AcknowledgeViolationResponse) String 
    
    
    func (x *AcknowledgeViolationResponse) String() [string](https://pkg.go.dev/builtin#string)

## AssuredWorkloadsServiceClient
    
    
    type AssuredWorkloadsServiceClient interface {
    	// Creates Assured Workload.
    	CreateWorkload(ctx context.Context, in *CreateWorkloadRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing workload.
    	// Currently allows updating of workload display_name and labels.
    	// For force updates don't set etag field in the Workload.
    	// Only one update operation per workload can be in progress.
    	UpdateWorkload(ctx context.Context, in *UpdateWorkloadRequest, opts ...grpc.CallOption) (*Workload, [error](https://pkg.go.dev/builtin#error))
    	// Restrict the list of resources allowed in the Workload environment.
    	// The current list of allowed products can be found at
    	// https://cloud.google.com/assured-workloads/docs/supported-products
    	// In addition to assuredworkloads.workload.update permission, the user should
    	// also have orgpolicy.policy.set permission on the folder resource
    	// to use this functionality.
    	RestrictAllowedResources(ctx context.Context, in *RestrictAllowedResourcesRequest, opts ...grpc.CallOption) (*RestrictAllowedResourcesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the workload. Make sure that workload's direct children are already
    	// in a deleted state, otherwise the request will fail with a
    	// FAILED_PRECONDITION error.
    	DeleteWorkload(ctx context.Context, in *DeleteWorkloadRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Gets Assured Workload associated with a CRM Node
    	GetWorkload(ctx context.Context, in *GetWorkloadRequest, opts ...grpc.CallOption) (*Workload, [error](https://pkg.go.dev/builtin#error))
    	// Lists Assured Workloads under a CRM Node.
    	ListWorkloads(ctx context.Context, in *ListWorkloadsRequest, opts ...grpc.CallOption) (*ListWorkloadsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists the Violations in the AssuredWorkload Environment.
    	// Callers may also choose to read across multiple Workloads as per
    	// [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash
    	// character) as a wildcard character instead of workload-id in the parent.
    	// Format `organizations/{org_id}/locations/{location}/workloads/-`
    	ListViolations(ctx context.Context, in *ListViolationsRequest, opts ...grpc.CallOption) (*ListViolationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves Assured Workload Violation based on ID.
    	GetViolation(ctx context.Context, in *GetViolationRequest, opts ...grpc.CallOption) (*Violation, [error](https://pkg.go.dev/builtin#error))
    	// Acknowledges an existing violation. By acknowledging a violation, users
    	// acknowledge the existence of a compliance violation in their workload and
    	// decide to ignore it due to a valid business justification. Acknowledgement
    	// is a permanent operation and it cannot be reverted.
    	AcknowledgeViolation(ctx context.Context, in *AcknowledgeViolationRequest, opts ...grpc.CallOption) (*AcknowledgeViolationResponse, [error](https://pkg.go.dev/builtin#error))
    }

AssuredWorkloadsServiceClient is the client API for AssuredWorkloadsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAssuredWorkloadsServiceClient 
    
    
    func NewAssuredWorkloadsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AssuredWorkloadsServiceClient

## AssuredWorkloadsServiceServer
    
    
    type AssuredWorkloadsServiceServer interface {
    	// Creates Assured Workload.
    	CreateWorkload(context.Context, *CreateWorkloadRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing workload.
    	// Currently allows updating of workload display_name and labels.
    	// For force updates don't set etag field in the Workload.
    	// Only one update operation per workload can be in progress.
    	UpdateWorkload(context.Context, *UpdateWorkloadRequest) (*Workload, [error](https://pkg.go.dev/builtin#error))
    	// Restrict the list of resources allowed in the Workload environment.
    	// The current list of allowed products can be found at
    	// https://cloud.google.com/assured-workloads/docs/supported-products
    	// In addition to assuredworkloads.workload.update permission, the user should
    	// also have orgpolicy.policy.set permission on the folder resource
    	// to use this functionality.
    	RestrictAllowedResources(context.Context, *RestrictAllowedResourcesRequest) (*RestrictAllowedResourcesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the workload. Make sure that workload's direct children are already
    	// in a deleted state, otherwise the request will fail with a
    	// FAILED_PRECONDITION error.
    	DeleteWorkload(context.Context, *DeleteWorkloadRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Gets Assured Workload associated with a CRM Node
    	GetWorkload(context.Context, *GetWorkloadRequest) (*Workload, [error](https://pkg.go.dev/builtin#error))
    	// Lists Assured Workloads under a CRM Node.
    	ListWorkloads(context.Context, *ListWorkloadsRequest) (*ListWorkloadsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists the Violations in the AssuredWorkload Environment.
    	// Callers may also choose to read across multiple Workloads as per
    	// [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash
    	// character) as a wildcard character instead of workload-id in the parent.
    	// Format `organizations/{org_id}/locations/{location}/workloads/-`
    	ListViolations(context.Context, *ListViolationsRequest) (*ListViolationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves Assured Workload Violation based on ID.
    	GetViolation(context.Context, *GetViolationRequest) (*Violation, [error](https://pkg.go.dev/builtin#error))
    	// Acknowledges an existing violation. By acknowledging a violation, users
    	// acknowledge the existence of a compliance violation in their workload and
    	// decide to ignore it due to a valid business justification. Acknowledgement
    	// is a permanent operation and it cannot be reverted.
    	AcknowledgeViolation(context.Context, *AcknowledgeViolationRequest) (*AcknowledgeViolationResponse, [error](https://pkg.go.dev/builtin#error))
    }

AssuredWorkloadsServiceServer is the server API for AssuredWorkloadsService service. All implementations should embed UnimplementedAssuredWorkloadsServiceServer for forward compatibility

## CreateWorkloadOperationMetadata
    
    
    type CreateWorkloadOperationMetadata struct {
    
    	// Optional. Time when the operation was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Optional. The display name of the workload.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Optional. The parent of the workload.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Compliance controls that should be applied to the resources managed by
    	// the workload.
    	ComplianceRegime Workload_ComplianceRegime `protobuf:"varint,4,opt,name=compliance_regime,json=complianceRegime,proto3,enum=google.cloud.assuredworkloads.v1.Workload_ComplianceRegime" json:"compliance_regime,omitempty"`
    	// contains filtered or unexported fields
    }

Operation metadata to give request details of CreateWorkload.

### func (*CreateWorkloadOperationMetadata) Descriptor 
    
    
    func (*CreateWorkloadOperationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateWorkloadOperationMetadata.ProtoReflect.Descriptor instead.

### func (*CreateWorkloadOperationMetadata) GetComplianceRegime 
    
    
    func (x *CreateWorkloadOperationMetadata) GetComplianceRegime() Workload_ComplianceRegime

### func (*CreateWorkloadOperationMetadata) GetCreateTime 
    
    
    func (x *CreateWorkloadOperationMetadata) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*CreateWorkloadOperationMetadata) GetDisplayName 
    
    
    func (x *CreateWorkloadOperationMetadata) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*CreateWorkloadOperationMetadata) GetParent 
    
    
    func (x *CreateWorkloadOperationMetadata) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateWorkloadOperationMetadata) ProtoMessage 
    
    
    func (*CreateWorkloadOperationMetadata) ProtoMessage()

### func (*CreateWorkloadOperationMetadata) ProtoReflect 
    
    
    func (x *CreateWorkloadOperationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateWorkloadOperationMetadata) Reset 
    
    
    func (x *CreateWorkloadOperationMetadata) Reset()

### func (*CreateWorkloadOperationMetadata) String 
    
    
    func (x *CreateWorkloadOperationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## CreateWorkloadRequest
    
    
    type CreateWorkloadRequest struct {
    
    	// Required. The resource name of the new Workload's parent.
    	// Must be of the form `organizations/{org_id}/locations/{location_id}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. Assured Workload to create
    	Workload *Workload `protobuf:"bytes,2,opt,name=workload,proto3" json:"workload,omitempty"`
    	// Optional. A identifier associated with the workload and underlying projects which
    	// allows for the break down of billing costs for a workload. The value
    	// provided for the identifier will add a label to the workload and contained
    	// projects with the identifier as the value.
    	ExternalId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=external_id,json=externalId,proto3" json:"external_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request for creating a workload.

### func (*CreateWorkloadRequest) Descriptor 
    
    
    func (*CreateWorkloadRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateWorkloadRequest.ProtoReflect.Descriptor instead.

### func (*CreateWorkloadRequest) GetExternalId 
    
    
    func (x *CreateWorkloadRequest) GetExternalId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateWorkloadRequest) GetParent 
    
    
    func (x *CreateWorkloadRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateWorkloadRequest) GetWorkload 
    
    
    func (x *CreateWorkloadRequest) GetWorkload() *Workload

### func (*CreateWorkloadRequest) ProtoMessage 
    
    
    func (*CreateWorkloadRequest) ProtoMessage()

### func (*CreateWorkloadRequest) ProtoReflect 
    
    
    func (x *CreateWorkloadRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateWorkloadRequest) Reset 
    
    
    func (x *CreateWorkloadRequest) Reset()

### func (*CreateWorkloadRequest) String 
    
    
    func (x *CreateWorkloadRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteWorkloadRequest
    
    
    type DeleteWorkloadRequest struct {
    
    	// Required. The `name` field is used to identify the workload.
    	// Format:
    	// organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The etag of the workload.
    	// If this is provided, it must match the server's etag.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Request for deleting a Workload.

### func (*DeleteWorkloadRequest) Descriptor 
    
    
    func (*DeleteWorkloadRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteWorkloadRequest.ProtoReflect.Descriptor instead.

### func (*DeleteWorkloadRequest) GetEtag 
    
    
    func (x *DeleteWorkloadRequest) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteWorkloadRequest) GetName 
    
    
    func (x *DeleteWorkloadRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteWorkloadRequest) ProtoMessage 
    
    
    func (*DeleteWorkloadRequest) ProtoMessage()

### func (*DeleteWorkloadRequest) ProtoReflect 
    
    
    func (x *DeleteWorkloadRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteWorkloadRequest) Reset 
    
    
    func (x *DeleteWorkloadRequest) Reset()

### func (*DeleteWorkloadRequest) String 
    
    
    func (x *DeleteWorkloadRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetViolationRequest
    
    
    type GetViolationRequest struct {
    
    	// Required. The resource name of the Violation to fetch (ie. Violation.name).
    	// Format:
    	// organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching a Workload Violation.

### func (*GetViolationRequest) Descriptor 
    
    
    func (*GetViolationRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetViolationRequest.ProtoReflect.Descriptor instead.

### func (*GetViolationRequest) GetName 
    
    
    func (x *GetViolationRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetViolationRequest) ProtoMessage 
    
    
    func (*GetViolationRequest) ProtoMessage()

### func (*GetViolationRequest) ProtoReflect 
    
    
    func (x *GetViolationRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetViolationRequest) Reset 
    
    
    func (x *GetViolationRequest) Reset()

### func (*GetViolationRequest) String 
    
    
    func (x *GetViolationRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetWorkloadRequest
    
    
    type GetWorkloadRequest struct {
    
    	// Required. The resource name of the Workload to fetch. This is the workload's
    	// relative path in the API, formatted as
    	// "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
    	// For example,
    	// "organizations/123/locations/us-east1/workloads/assured-workload-1".
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching a workload.

### func (*GetWorkloadRequest) Descriptor 
    
    
    func (*GetWorkloadRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetWorkloadRequest.ProtoReflect.Descriptor instead.

### func (*GetWorkloadRequest) GetName 
    
    
    func (x *GetWorkloadRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetWorkloadRequest) ProtoMessage 
    
    
    func (*GetWorkloadRequest) ProtoMessage()

### func (*GetWorkloadRequest) ProtoReflect 
    
    
    func (x *GetWorkloadRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetWorkloadRequest) Reset 
    
    
    func (x *GetWorkloadRequest) Reset()

### func (*GetWorkloadRequest) String 
    
    
    func (x *GetWorkloadRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListViolationsRequest
    
    
    type ListViolationsRequest struct {
    
    	// Required. The Workload name.
    	// Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Specifies the time window for retrieving active Violations.
    	// When specified, retrieves Violations that were active between start_time
    	// and end_time.
    	Interval *TimeWindow `protobuf:"bytes,2,opt,name=interval,proto3" json:"interval,omitempty"`
    	// Optional. Page size.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. Page token returned from previous request.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A custom filter for filtering by the Violations properties.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching violations in an organization.

### func (*ListViolationsRequest) Descriptor 
    
    
    func (*ListViolationsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListViolationsRequest.ProtoReflect.Descriptor instead.

### func (*ListViolationsRequest) GetFilter 
    
    
    func (x *ListViolationsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListViolationsRequest) GetInterval 
    
    
    func (x *ListViolationsRequest) GetInterval() *TimeWindow

### func (*ListViolationsRequest) GetPageSize 
    
    
    func (x *ListViolationsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListViolationsRequest) GetPageToken 
    
    
    func (x *ListViolationsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListViolationsRequest) GetParent 
    
    
    func (x *ListViolationsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListViolationsRequest) ProtoMessage 
    
    
    func (*ListViolationsRequest) ProtoMessage()

### func (*ListViolationsRequest) ProtoReflect 
    
    
    func (x *ListViolationsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListViolationsRequest) Reset 
    
    
    func (x *ListViolationsRequest) Reset()

### func (*ListViolationsRequest) String 
    
    
    func (x *ListViolationsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListViolationsResponse
    
    
    type ListViolationsResponse struct {
    
    	// List of Violations under a Workload.
    	Violations []*Violation `protobuf:"bytes,1,rep,name=violations,proto3" json:"violations,omitempty"`
    	// The next page token. Returns empty if reached the last page.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response of ListViolations endpoint.

### func (*ListViolationsResponse) Descriptor 
    
    
    func (*ListViolationsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListViolationsResponse.ProtoReflect.Descriptor instead.

### func (*ListViolationsResponse) GetNextPageToken 
    
    
    func (x *ListViolationsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListViolationsResponse) GetViolations 
    
    
    func (x *ListViolationsResponse) GetViolations() []*Violation

### func (*ListViolationsResponse) ProtoMessage 
    
    
    func (*ListViolationsResponse) ProtoMessage()

### func (*ListViolationsResponse) ProtoReflect 
    
    
    func (x *ListViolationsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListViolationsResponse) Reset 
    
    
    func (x *ListViolationsResponse) Reset()

### func (*ListViolationsResponse) String 
    
    
    func (x *ListViolationsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListWorkloadsRequest
    
    
    type ListWorkloadsRequest struct {
    
    	// Required. Parent Resource to list workloads from.
    	// Must be of the form `organizations/{org_id}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Page size.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Page token returned from previous request. Page token contains context from
    	// previous request. Page token needs to be passed in the second and following
    	// requests.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// A custom filter for filtering by properties of a workload. At this time,
    	// only filtering by labels is supported.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request for fetching workloads in an organization.

### func (*ListWorkloadsRequest) Descriptor 
    
    
    func (*ListWorkloadsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListWorkloadsRequest.ProtoReflect.Descriptor instead.

### func (*ListWorkloadsRequest) GetFilter 
    
    
    func (x *ListWorkloadsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListWorkloadsRequest) GetPageSize 
    
    
    func (x *ListWorkloadsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListWorkloadsRequest) GetPageToken 
    
    
    func (x *ListWorkloadsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListWorkloadsRequest) GetParent 
    
    
    func (x *ListWorkloadsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListWorkloadsRequest) ProtoMessage 
    
    
    func (*ListWorkloadsRequest) ProtoMessage()

### func (*ListWorkloadsRequest) ProtoReflect 
    
    
    func (x *ListWorkloadsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListWorkloadsRequest) Reset 
    
    
    func (x *ListWorkloadsRequest) Reset()

### func (*ListWorkloadsRequest) String 
    
    
    func (x *ListWorkloadsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListWorkloadsResponse
    
    
    type ListWorkloadsResponse struct {
    
    	// List of Workloads under a given parent.
    	Workloads []*Workload `protobuf:"bytes,1,rep,name=workloads,proto3" json:"workloads,omitempty"`
    	// The next page token. Return empty if reached the last page.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response of ListWorkloads endpoint.

### func (*ListWorkloadsResponse) Descriptor 
    
    
    func (*ListWorkloadsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListWorkloadsResponse.ProtoReflect.Descriptor instead.

### func (*ListWorkloadsResponse) GetNextPageToken 
    
    
    func (x *ListWorkloadsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListWorkloadsResponse) GetWorkloads 
    
    
    func (x *ListWorkloadsResponse) GetWorkloads() []*Workload

### func (*ListWorkloadsResponse) ProtoMessage 
    
    
    func (*ListWorkloadsResponse) ProtoMessage()

### func (*ListWorkloadsResponse) ProtoReflect 
    
    
    func (x *ListWorkloadsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListWorkloadsResponse) Reset 
    
    
    func (x *ListWorkloadsResponse) Reset()

### func (*ListWorkloadsResponse) String 
    
    
    func (x *ListWorkloadsResponse) String() [string](https://pkg.go.dev/builtin#string)

## RestrictAllowedResourcesRequest
    
    
    type RestrictAllowedResourcesRequest struct {
    
    	// Required. The resource name of the Workload. This is the workloads's
    	// relative path in the API, formatted as
    	// "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
    	// For example,
    	// "organizations/123/locations/us-east1/workloads/assured-workload-1".
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The type of restriction for using gcp products in the Workload environment.
    	RestrictionType RestrictAllowedResourcesRequest_RestrictionType `protobuf:"varint,2,opt,name=restriction_type,json=restrictionType,proto3,enum=google.cloud.assuredworkloads.v1.RestrictAllowedResourcesRequest_RestrictionType" json:"restriction_type,omitempty"`
    	// contains filtered or unexported fields
    }

Request for restricting list of available resources in Workload environment.

### func (*RestrictAllowedResourcesRequest) Descriptor 
    
    
    func (*RestrictAllowedResourcesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RestrictAllowedResourcesRequest.ProtoReflect.Descriptor instead.

### func (*RestrictAllowedResourcesRequest) GetName 
    
    
    func (x *RestrictAllowedResourcesRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RestrictAllowedResourcesRequest) GetRestrictionType 
    
    
    func (x *RestrictAllowedResourcesRequest) GetRestrictionType() RestrictAllowedResourcesRequest_RestrictionType

### func (*RestrictAllowedResourcesRequest) ProtoMessage 
    
    
    func (*RestrictAllowedResourcesRequest) ProtoMessage()

### func (*RestrictAllowedResourcesRequest) ProtoReflect 
    
    
    func (x *RestrictAllowedResourcesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RestrictAllowedResourcesRequest) Reset 
    
    
    func (x *RestrictAllowedResourcesRequest) Reset()

### func (*RestrictAllowedResourcesRequest) String 
    
    
    func (x *RestrictAllowedResourcesRequest) String() [string](https://pkg.go.dev/builtin#string)

## RestrictAllowedResourcesRequest_RestrictionType
    
    
    type RestrictAllowedResourcesRequest_RestrictionType [int32](https://pkg.go.dev/builtin#int32)

The type of restriction.

### RestrictAllowedResourcesRequest_RESTRICTION_TYPE_UNSPECIFIED, RestrictAllowedResourcesRequest_ALLOW_ALL_GCP_RESOURCES, RestrictAllowedResourcesRequest_ALLOW_COMPLIANT_RESOURCES
    
    
    const (
    	// Unknown restriction type.
    	RestrictAllowedResourcesRequest_RESTRICTION_TYPE_UNSPECIFIED RestrictAllowedResourcesRequest_RestrictionType = 0
    	// Allow the use all of all gcp products, irrespective of the compliance
    	// posture. This effectively removes gcp.restrictServiceUsage OrgPolicy
    	// on the AssuredWorkloads Folder.
    	RestrictAllowedResourcesRequest_ALLOW_ALL_GCP_RESOURCES RestrictAllowedResourcesRequest_RestrictionType = 1
    	// Based on Workload's compliance regime, allowed list changes.
    	// See - https://cloud.google.com/assured-workloads/docs/supported-products
    	// for the list of supported resources.
    	RestrictAllowedResourcesRequest_ALLOW_COMPLIANT_RESOURCES RestrictAllowedResourcesRequest_RestrictionType = 2
    )

### func (RestrictAllowedResourcesRequest_RestrictionType) Descriptor 
    
    
    func (RestrictAllowedResourcesRequest_RestrictionType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RestrictAllowedResourcesRequest_RestrictionType) Enum 
    
    
    func (x RestrictAllowedResourcesRequest_RestrictionType) Enum() *RestrictAllowedResourcesRequest_RestrictionType

### func (RestrictAllowedResourcesRequest_RestrictionType) EnumDescriptor 
    
    
    func (RestrictAllowedResourcesRequest_RestrictionType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RestrictAllowedResourcesRequest_RestrictionType.Descriptor instead.

### func (RestrictAllowedResourcesRequest_RestrictionType) Number 
    
    
    func (x RestrictAllowedResourcesRequest_RestrictionType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RestrictAllowedResourcesRequest_RestrictionType) String 
    
    
    func (x RestrictAllowedResourcesRequest_RestrictionType) String() [string](https://pkg.go.dev/builtin#string)

### func (RestrictAllowedResourcesRequest_RestrictionType) Type 
    
    
    func (RestrictAllowedResourcesRequest_RestrictionType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RestrictAllowedResourcesResponse
    
    
    type RestrictAllowedResourcesResponse struct {
    	// contains filtered or unexported fields
    }

Response for restricting the list of allowed resources.

### func (*RestrictAllowedResourcesResponse) Descriptor 
    
    
    func (*RestrictAllowedResourcesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RestrictAllowedResourcesResponse.ProtoReflect.Descriptor instead.

### func (*RestrictAllowedResourcesResponse) ProtoMessage 
    
    
    func (*RestrictAllowedResourcesResponse) ProtoMessage()

### func (*RestrictAllowedResourcesResponse) ProtoReflect 
    
    
    func (x *RestrictAllowedResourcesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RestrictAllowedResourcesResponse) Reset 
    
    
    func (x *RestrictAllowedResourcesResponse) Reset()

### func (*RestrictAllowedResourcesResponse) String 
    
    
    func (x *RestrictAllowedResourcesResponse) String() [string](https://pkg.go.dev/builtin#string)

## TimeWindow
    
    
    type TimeWindow struct {
    
    	// The start of the time window.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// The end of the time window.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// contains filtered or unexported fields
    }

Interval defining a time window.

### func (*TimeWindow) Descriptor 
    
    
    func (*TimeWindow) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TimeWindow.ProtoReflect.Descriptor instead.

### func (*TimeWindow) GetEndTime 
    
    
    func (x *TimeWindow) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TimeWindow) GetStartTime 
    
    
    func (x *TimeWindow) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TimeWindow) ProtoMessage 
    
    
    func (*TimeWindow) ProtoMessage()

### func (*TimeWindow) ProtoReflect 
    
    
    func (x *TimeWindow) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TimeWindow) Reset 
    
    
    func (x *TimeWindow) Reset()

### func (*TimeWindow) String 
    
    
    func (x *TimeWindow) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedAssuredWorkloadsServiceServer
    
    
    type UnimplementedAssuredWorkloadsServiceServer struct {
    }

UnimplementedAssuredWorkloadsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAssuredWorkloadsServiceServer) AcknowledgeViolation 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) AcknowledgeViolation([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AcknowledgeViolationRequest) (*AcknowledgeViolationResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) CreateWorkload 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) CreateWorkload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateWorkloadRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) DeleteWorkload 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) DeleteWorkload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteWorkloadRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) GetViolation 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) GetViolation([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetViolationRequest) (*Violation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) GetWorkload 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) GetWorkload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetWorkloadRequest) (*Workload, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) ListViolations 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) ListViolations([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListViolationsRequest) (*ListViolationsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) ListWorkloads 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) ListWorkloads([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListWorkloadsRequest) (*ListWorkloadsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) RestrictAllowedResources 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) RestrictAllowedResources([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RestrictAllowedResourcesRequest) (*RestrictAllowedResourcesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAssuredWorkloadsServiceServer) UpdateWorkload 
    
    
    func (UnimplementedAssuredWorkloadsServiceServer) UpdateWorkload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateWorkloadRequest) (*Workload, [error](https://pkg.go.dev/builtin#error))

## UnsafeAssuredWorkloadsServiceServer
    
    
    type UnsafeAssuredWorkloadsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAssuredWorkloadsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AssuredWorkloadsServiceServer will result in compilation errors.

## UpdateWorkloadRequest
    
    
    type UpdateWorkloadRequest struct {
    
    	// Required. The workload to update.
    	// The workload's `name` field is used to identify the workload to be updated.
    	// Format:
    	// organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
    	Workload *Workload `protobuf:"bytes,1,opt,name=workload,proto3" json:"workload,omitempty"`
    	// Required. The list of fields to be updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request for Updating a workload.

### func (*UpdateWorkloadRequest) Descriptor 
    
    
    func (*UpdateWorkloadRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateWorkloadRequest.ProtoReflect.Descriptor instead.

### func (*UpdateWorkloadRequest) GetUpdateMask 
    
    
    func (x *UpdateWorkloadRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateWorkloadRequest) GetWorkload 
    
    
    func (x *UpdateWorkloadRequest) GetWorkload() *Workload

### func (*UpdateWorkloadRequest) ProtoMessage 
    
    
    func (*UpdateWorkloadRequest) ProtoMessage()

### func (*UpdateWorkloadRequest) ProtoReflect 
    
    
    func (x *UpdateWorkloadRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateWorkloadRequest) Reset 
    
    
    func (x *UpdateWorkloadRequest) Reset()

### func (*UpdateWorkloadRequest) String 
    
    
    func (x *UpdateWorkloadRequest) String() [string](https://pkg.go.dev/builtin#string)

## Violation
    
    
    type Violation struct {
    
    	// Output only. Immutable. Name of the Violation.
    	// Format:
    	// organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Description for the Violation.
    	// e.g. OrgPolicy gcp.resourceLocations has non compliant value.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// Output only. Time of the event which triggered the Violation.
    	BeginTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=begin_time,json=beginTime,proto3" json:"begin_time,omitempty"`
    	// Output only. The last time when the Violation record was updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. Time of the event which fixed the Violation.
    	// If the violation is ACTIVE this will be empty.
    	ResolveTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=resolve_time,json=resolveTime,proto3" json:"resolve_time,omitempty"`
    	// Output only. Category under which this violation is mapped.
    	// e.g. Location, Service Usage, Access, Encryption, etc.
    	Category [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=category,proto3" json:"category,omitempty"`
    	// Output only. State of the violation
    	State Violation_State `protobuf:"varint,7,opt,name=state,proto3,enum=google.cloud.assuredworkloads.v1.Violation_State" json:"state,omitempty"`
    	// Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in
    	// this violation.
    	OrgPolicyConstraint [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=org_policy_constraint,json=orgPolicyConstraint,proto3" json:"org_policy_constraint,omitempty"`
    	// Output only. Immutable. Audit Log Link for violated resource
    	// Format:
    	// https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder}
    	AuditLogLink [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=audit_log_link,json=auditLogLink,proto3" json:"audit_log_link,omitempty"`
    	// Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and
    	// resulted this violation.
    	//
    	//	Format:
    	//	projects/{project_number}/policies/{constraint_name}
    	//	folders/{folder_id}/policies/{constraint_name}
    	//	organizations/{organization_id}/policies/{constraint_name}
    	NonCompliantOrgPolicy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,12,opt,name=non_compliant_org_policy,json=nonCompliantOrgPolicy,proto3" json:"non_compliant_org_policy,omitempty"`
    	// Output only. Compliance violation remediation
    	Remediation *Violation_Remediation `protobuf:"bytes,13,opt,name=remediation,proto3" json:"remediation,omitempty"`
    	// Output only. A boolean that indicates if the violation is acknowledged
    	Acknowledged [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,14,opt,name=acknowledged,proto3" json:"acknowledged,omitempty"`
    	// Optional. Timestamp when this violation was acknowledged last.
    	// This will be absent when acknowledged field is marked as false.
    	AcknowledgementTime *timestamppb.Timestamp `protobuf:"bytes,15,opt,name=acknowledgement_time,json=acknowledgementTime,proto3,oneof" json:"acknowledgement_time,omitempty"`
    	// Output only. Immutable. Audit Log link to find business justification provided for violation
    	// exception. Format:
    	// https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization}
    	ExceptionAuditLogLink [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,16,opt,name=exception_audit_log_link,json=exceptionAuditLogLink,proto3" json:"exception_audit_log_link,omitempty"`
    	// contains filtered or unexported fields
    }

Workload monitoring Violation.

### func (*Violation) Descriptor 
    
    
    func (*Violation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation.ProtoReflect.Descriptor instead.

### func (*Violation) GetAcknowledged 
    
    
    func (x *Violation) GetAcknowledged() [bool](https://pkg.go.dev/builtin#bool)

### func (*Violation) GetAcknowledgementTime 
    
    
    func (x *Violation) GetAcknowledgementTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Violation) GetAuditLogLink 
    
    
    func (x *Violation) GetAuditLogLink() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetBeginTime 
    
    
    func (x *Violation) GetBeginTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Violation) GetCategory 
    
    
    func (x *Violation) GetCategory() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetDescription 
    
    
    func (x *Violation) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetExceptionAuditLogLink 
    
    
    func (x *Violation) GetExceptionAuditLogLink() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetName 
    
    
    func (x *Violation) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetNonCompliantOrgPolicy 
    
    
    func (x *Violation) GetNonCompliantOrgPolicy() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetOrgPolicyConstraint 
    
    
    func (x *Violation) GetOrgPolicyConstraint() [string](https://pkg.go.dev/builtin#string)

### func (*Violation) GetRemediation 
    
    
    func (x *Violation) GetRemediation() *Violation_Remediation

### func (*Violation) GetResolveTime 
    
    
    func (x *Violation) GetResolveTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Violation) GetState 
    
    
    func (x *Violation) GetState() Violation_State

### func (*Violation) GetUpdateTime 
    
    
    func (x *Violation) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Violation) ProtoMessage 
    
    
    func (*Violation) ProtoMessage()

### func (*Violation) ProtoReflect 
    
    
    func (x *Violation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Violation) Reset 
    
    
    func (x *Violation) Reset()

### func (*Violation) String 
    
    
    func (x *Violation) String() [string](https://pkg.go.dev/builtin#string)

## Violation_Remediation
    
    
    type Violation_Remediation struct {
    
    	// Required. Remediation instructions to resolve violations
    	Instructions *Violation_Remediation_Instructions `protobuf:"bytes,1,opt,name=instructions,proto3" json:"instructions,omitempty"`
    	// Values that can resolve the violation
    	// For example: for list org policy violations, this will either be the list
    	// of allowed or denied values
    	CompliantValues [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=compliant_values,json=compliantValues,proto3" json:"compliant_values,omitempty"`
    	// Output only. Reemediation type based on the type of org policy values violated
    	RemediationType Violation_Remediation_RemediationType `protobuf:"varint,3,opt,name=remediation_type,json=remediationType,proto3,enum=google.cloud.assuredworkloads.v1.Violation_Remediation_RemediationType" json:"remediation_type,omitempty"`
    	// contains filtered or unexported fields
    }

Represents remediation guidance to resolve compliance violation for AssuredWorkload

### func (*Violation_Remediation) Descriptor 
    
    
    func (*Violation_Remediation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_Remediation.ProtoReflect.Descriptor instead.

### func (*Violation_Remediation) GetCompliantValues 
    
    
    func (x *Violation_Remediation) GetCompliantValues() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation) GetInstructions 
    
    
    func (x *Violation_Remediation) GetInstructions() *Violation_Remediation_Instructions

### func (*Violation_Remediation) GetRemediationType 
    
    
    func (x *Violation_Remediation) GetRemediationType() Violation_Remediation_RemediationType

### func (*Violation_Remediation) ProtoMessage 
    
    
    func (*Violation_Remediation) ProtoMessage()

### func (*Violation_Remediation) ProtoReflect 
    
    
    func (x *Violation_Remediation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Violation_Remediation) Reset 
    
    
    func (x *Violation_Remediation) Reset()

### func (*Violation_Remediation) String 
    
    
    func (x *Violation_Remediation) String() [string](https://pkg.go.dev/builtin#string)

## Violation_Remediation_Instructions
    
    
    type Violation_Remediation_Instructions struct {
    
    	// Remediation instructions to resolve violation via gcloud cli
    	GcloudInstructions *Violation_Remediation_Instructions_Gcloud `protobuf:"bytes,1,opt,name=gcloud_instructions,json=gcloudInstructions,proto3" json:"gcloud_instructions,omitempty"`
    	// Remediation instructions to resolve violation via cloud console
    	ConsoleInstructions *Violation_Remediation_Instructions_Console `protobuf:"bytes,2,opt,name=console_instructions,json=consoleInstructions,proto3" json:"console_instructions,omitempty"`
    	// contains filtered or unexported fields
    }

Instructions to remediate violation

### func (*Violation_Remediation_Instructions) Descriptor 
    
    
    func (*Violation_Remediation_Instructions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_Remediation_Instructions.ProtoReflect.Descriptor instead.

### func (*Violation_Remediation_Instructions) GetConsoleInstructions 
    
    
    func (x *Violation_Remediation_Instructions) GetConsoleInstructions() *Violation_Remediation_Instructions_Console

### func (*Violation_Remediation_Instructions) GetGcloudInstructions 
    
    
    func (x *Violation_Remediation_Instructions) GetGcloudInstructions() *Violation_Remediation_Instructions_Gcloud

### func (*Violation_Remediation_Instructions) ProtoMessage 
    
    
    func (*Violation_Remediation_Instructions) ProtoMessage()

### func (*Violation_Remediation_Instructions) ProtoReflect 
    
    
    func (x *Violation_Remediation_Instructions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Violation_Remediation_Instructions) Reset 
    
    
    func (x *Violation_Remediation_Instructions) Reset()

### func (*Violation_Remediation_Instructions) String 
    
    
    func (x *Violation_Remediation_Instructions) String() [string](https://pkg.go.dev/builtin#string)

## Violation_Remediation_Instructions_Console
    
    
    type Violation_Remediation_Instructions_Console struct {
    
    	// Link to console page where violations can be resolved
    	ConsoleUris [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=console_uris,json=consoleUris,proto3" json:"console_uris,omitempty"`
    	// Steps to resolve violation via cloud console
    	Steps [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=steps,proto3" json:"steps,omitempty"`
    	// Additional urls for more information about steps
    	AdditionalLinks [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=additional_links,json=additionalLinks,proto3" json:"additional_links,omitempty"`
    	// contains filtered or unexported fields
    }

Remediation instructions to resolve violation via cloud console

### func (*Violation_Remediation_Instructions_Console) Descriptor 
    
    
    func (*Violation_Remediation_Instructions_Console) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_Remediation_Instructions_Console.ProtoReflect.Descriptor instead.

### func (*Violation_Remediation_Instructions_Console) GetAdditionalLinks 
    
    
    func (x *Violation_Remediation_Instructions_Console) GetAdditionalLinks() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Console) GetConsoleUris 
    
    
    func (x *Violation_Remediation_Instructions_Console) GetConsoleUris() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Console) GetSteps 
    
    
    func (x *Violation_Remediation_Instructions_Console) GetSteps() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Console) ProtoMessage 
    
    
    func (*Violation_Remediation_Instructions_Console) ProtoMessage()

### func (*Violation_Remediation_Instructions_Console) ProtoReflect 
    
    
    func (x *Violation_Remediation_Instructions_Console) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Violation_Remediation_Instructions_Console) Reset 
    
    
    func (x *Violation_Remediation_Instructions_Console) Reset()

### func (*Violation_Remediation_Instructions_Console) String 
    
    
    func (x *Violation_Remediation_Instructions_Console) String() [string](https://pkg.go.dev/builtin#string)

## Violation_Remediation_Instructions_Gcloud
    
    
    type Violation_Remediation_Instructions_Gcloud struct {
    
    	// Gcloud command to resolve violation
    	GcloudCommands [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=gcloud_commands,json=gcloudCommands,proto3" json:"gcloud_commands,omitempty"`
    	// Steps to resolve violation via gcloud cli
    	Steps [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=steps,proto3" json:"steps,omitempty"`
    	// Additional urls for more information about steps
    	AdditionalLinks [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=additional_links,json=additionalLinks,proto3" json:"additional_links,omitempty"`
    	// contains filtered or unexported fields
    }

Remediation instructions to resolve violation via gcloud cli

### func (*Violation_Remediation_Instructions_Gcloud) Descriptor 
    
    
    func (*Violation_Remediation_Instructions_Gcloud) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_Remediation_Instructions_Gcloud.ProtoReflect.Descriptor instead.

### func (*Violation_Remediation_Instructions_Gcloud) GetAdditionalLinks 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) GetAdditionalLinks() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Gcloud) GetGcloudCommands 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) GetGcloudCommands() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Gcloud) GetSteps 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) GetSteps() [][string](https://pkg.go.dev/builtin#string)

### func (*Violation_Remediation_Instructions_Gcloud) ProtoMessage 
    
    
    func (*Violation_Remediation_Instructions_Gcloud) ProtoMessage()

### func (*Violation_Remediation_Instructions_Gcloud) ProtoReflect 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Violation_Remediation_Instructions_Gcloud) Reset 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) Reset()

### func (*Violation_Remediation_Instructions_Gcloud) String 
    
    
    func (x *Violation_Remediation_Instructions_Gcloud) String() [string](https://pkg.go.dev/builtin#string)

## Violation_Remediation_RemediationType
    
    
    type Violation_Remediation_RemediationType [int32](https://pkg.go.dev/builtin#int32)

Classifying remediation into various types based on the kind of violation. For example, violations caused due to changes in boolean org policy requires different remediation instructions compared to violation caused due to changes in allowed values of list org policy.

### Violation_Remediation_REMEDIATION_TYPE_UNSPECIFIED, Violation_Remediation_REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION, Violation_Remediation_REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION, Violation_Remediation_REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION, Violation_Remediation_REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION
    
    
    const (
    	// Unspecified remediation type
    	Violation_Remediation_REMEDIATION_TYPE_UNSPECIFIED Violation_Remediation_RemediationType = 0
    	// Remediation type for boolean org policy
    	Violation_Remediation_REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION Violation_Remediation_RemediationType = 1
    	// Remediation type for list org policy which have allowed values in the
    	// monitoring rule
    	Violation_Remediation_REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION Violation_Remediation_RemediationType = 2
    	// Remediation type for list org policy which have denied values in the
    	// monitoring rule
    	Violation_Remediation_REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION Violation_Remediation_RemediationType = 3
    	// Remediation type for gcp.restrictCmekCryptoKeyProjects
    	Violation_Remediation_REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION Violation_Remediation_RemediationType = 4
    )

### func (Violation_Remediation_RemediationType) Descriptor 
    
    
    func (Violation_Remediation_RemediationType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Violation_Remediation_RemediationType) Enum 
    
    
    func (x Violation_Remediation_RemediationType) Enum() *Violation_Remediation_RemediationType

### func (Violation_Remediation_RemediationType) EnumDescriptor 
    
    
    func (Violation_Remediation_RemediationType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_Remediation_RemediationType.Descriptor instead.

### func (Violation_Remediation_RemediationType) Number 
    
    
    func (x Violation_Remediation_RemediationType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Violation_Remediation_RemediationType) String 
    
    
    func (x Violation_Remediation_RemediationType) String() [string](https://pkg.go.dev/builtin#string)

### func (Violation_Remediation_RemediationType) Type 
    
    
    func (Violation_Remediation_RemediationType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Violation_State
    
    
    type Violation_State [int32](https://pkg.go.dev/builtin#int32)

Violation State Values

### Violation_STATE_UNSPECIFIED, Violation_RESOLVED, Violation_UNRESOLVED, Violation_EXCEPTION
    
    
    const (
    	// Unspecified state.
    	Violation_STATE_UNSPECIFIED Violation_State = 0
    	// Violation is resolved.
    	Violation_RESOLVED Violation_State = 2
    	// Violation is Unresolved
    	Violation_UNRESOLVED Violation_State = 3
    	// Violation is Exception
    	Violation_EXCEPTION Violation_State = 4
    )

### func (Violation_State) Descriptor 
    
    
    func (Violation_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Violation_State) Enum 
    
    
    func (x Violation_State) Enum() *Violation_State

### func (Violation_State) EnumDescriptor 
    
    
    func (Violation_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Violation_State.Descriptor instead.

### func (Violation_State) Number 
    
    
    func (x Violation_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Violation_State) String 
    
    
    func (x Violation_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Violation_State) Type 
    
    
    func (Violation_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload
    
    
    type Workload struct {
    
    	// Optional. The resource name of the workload.
    	// Format:
    	// organizations/{organization}/locations/{location}/workloads/{workload}
    	//
    	// Read-only.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The user-assigned display name of the Workload.
    	// When present it must be between 4 to 30 characters.
    	// Allowed characters are: lowercase and uppercase letters, numbers,
    	// hyphen, and spaces.
    	//
    	// Example: My Workload
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. The resources associated with this workload.
    	// These resources will be created when creating the workload.
    	// If any of the projects already exist, the workload creation will fail.
    	// Always read only.
    	Resources []*Workload_ResourceInfo `protobuf:"bytes,3,rep,name=resources,proto3" json:"resources,omitempty"`
    	// Required. Immutable. Compliance Regime associated with this workload.
    	ComplianceRegime Workload_ComplianceRegime `protobuf:"varint,4,opt,name=compliance_regime,json=complianceRegime,proto3,enum=google.cloud.assuredworkloads.v1.Workload_ComplianceRegime" json:"compliance_regime,omitempty"`
    	// Output only. Immutable. The Workload creation timestamp.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Optional. The billing account used for the resources which are
    	// direct children of workload. This billing account is initially associated
    	// with the resources created as part of Workload creation.
    	// After the initial creation of these resources, the customer can change
    	// the assigned billing account.
    	// The resource name has the form
    	// `billingAccounts/{billing_account_id}`. For example,
    	// `billingAccounts/012345-567890-ABCDEF`.
    	BillingAccount [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=billing_account,json=billingAccount,proto3" json:"billing_account,omitempty"`
    	// Optional. ETag of the workload, it is calculated on the basis
    	// of the Workload contents. It will be used in Update & Delete operations.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=etag,proto3" json:"etag,omitempty"`
    	// Optional. Labels applied to the workload.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Input only. The parent resource for the resources managed by this Assured Workload. May
    	// be either empty or a folder resource which is a child of the
    	// Workload parent. If not specified all resources are created under the
    	// parent organization.
    	// Format:
    	// folders/{folder_id}
    	ProvisionedResourcesParent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,13,opt,name=provisioned_resources_parent,json=provisionedResourcesParent,proto3" json:"provisioned_resources_parent,omitempty"`
    	// Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS
    	// CMEK key is provisioned.
    	// This field is deprecated as of Feb 28, 2022.
    	// In order to create a Keyring, callers should specify,
    	// ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.
    	KmsSettings *Workload_KMSSettings `protobuf:"bytes,14,opt,name=kms_settings,json=kmsSettings,proto3" json:"kms_settings,omitempty"`
    	// Input only. Resource properties that are used to customize workload resources.
    	// These properties (such as custom project id) will be used to create
    	// workload resources if possible. This field is optional.
    	ResourceSettings []*Workload_ResourceSettings `protobuf:"bytes,15,rep,name=resource_settings,json=resourceSettings,proto3" json:"resource_settings,omitempty"`
    	// Output only. Represents the KAJ enrollment state of the given workload.
    	KajEnrollmentState Workload_KajEnrollmentState `protobuf:"varint,17,opt,name=kaj_enrollment_state,json=kajEnrollmentState,proto3,enum=google.cloud.assuredworkloads.v1.Workload_KajEnrollmentState" json:"kaj_enrollment_state,omitempty"`
    	// Optional. Indicates the sovereignty status of the given workload.
    	// Currently meant to be used by Europe/Canada customers.
    	EnableSovereignControls [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,18,opt,name=enable_sovereign_controls,json=enableSovereignControls,proto3" json:"enable_sovereign_controls,omitempty"`
    	// Output only. Represents the SAA enrollment response of the given workload.
    	// SAA enrollment response is queried during GetWorkload call.
    	// In failure cases, user friendly error message is shown in SAA details page.
    	SaaEnrollmentResponse *Workload_SaaEnrollmentResponse `protobuf:"bytes,20,opt,name=saa_enrollment_response,json=saaEnrollmentResponse,proto3" json:"saa_enrollment_response,omitempty"`
    	// Output only. Urls for services which are compliant for this Assured Workload, but which
    	// are currently disallowed by the ResourceUsageRestriction org policy.
    	// Invoke RestrictAllowedResources endpoint to allow your project developers
    	// to use these services in their environment."
    	CompliantButDisallowedServices [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,24,rep,name=compliant_but_disallowed_services,json=compliantButDisallowedServices,proto3" json:"compliant_but_disallowed_services,omitempty"`
    	// Optional. Compliance Regime associated with this workload.
    	Partner Workload_Partner `protobuf:"varint,25,opt,name=partner,proto3,enum=google.cloud.assuredworkloads.v1.Workload_Partner" json:"partner,omitempty"`
    	// contains filtered or unexported fields
    }

A Workload object for managing highly regulated workloads of cloud customers.

### func (*Workload) Descriptor 
    
    
    func (*Workload) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload.ProtoReflect.Descriptor instead.

### func (*Workload) GetBillingAccount 
    
    
    func (x *Workload) GetBillingAccount() [string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetComplianceRegime 
    
    
    func (x *Workload) GetComplianceRegime() Workload_ComplianceRegime

### func (*Workload) GetCompliantButDisallowedServices 
    
    
    func (x *Workload) GetCompliantButDisallowedServices() [][string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetCreateTime 
    
    
    func (x *Workload) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Workload) GetDisplayName 
    
    
    func (x *Workload) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetEnableSovereignControls 
    
    
    func (x *Workload) GetEnableSovereignControls() [bool](https://pkg.go.dev/builtin#bool)

### func (*Workload) GetEtag 
    
    
    func (x *Workload) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetKajEnrollmentState 
    
    
    func (x *Workload) GetKajEnrollmentState() Workload_KajEnrollmentState

### func (*Workload) GetKmsSettings 
    
    
    func (x *Workload) GetKmsSettings() *Workload_KMSSettings

Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.

### func (*Workload) GetLabels 
    
    
    func (x *Workload) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetName 
    
    
    func (x *Workload) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetPartner 
    
    
    func (x *Workload) GetPartner() Workload_Partner

### func (*Workload) GetProvisionedResourcesParent 
    
    
    func (x *Workload) GetProvisionedResourcesParent() [string](https://pkg.go.dev/builtin#string)

### func (*Workload) GetResourceSettings 
    
    
    func (x *Workload) GetResourceSettings() []*Workload_ResourceSettings

### func (*Workload) GetResources 
    
    
    func (x *Workload) GetResources() []*Workload_ResourceInfo

### func (*Workload) GetSaaEnrollmentResponse 
    
    
    func (x *Workload) GetSaaEnrollmentResponse() *Workload_SaaEnrollmentResponse

### func (*Workload) ProtoMessage 
    
    
    func (*Workload) ProtoMessage()

### func (*Workload) ProtoReflect 
    
    
    func (x *Workload) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Workload) Reset 
    
    
    func (x *Workload) Reset()

### func (*Workload) String 
    
    
    func (x *Workload) String() [string](https://pkg.go.dev/builtin#string)

## Workload_ComplianceRegime
    
    
    type Workload_ComplianceRegime [int32](https://pkg.go.dev/builtin#int32)

Supported Compliance Regimes.

### Workload_COMPLIANCE_REGIME_UNSPECIFIED, Workload_IL4, Workload_CJIS, Workload_FEDRAMP_HIGH, Workload_FEDRAMP_MODERATE, Workload_US_REGIONAL_ACCESS, Workload_HIPAA, Workload_HITRUST, Workload_EU_REGIONS_AND_SUPPORT, Workload_CA_REGIONS_AND_SUPPORT, Workload_ITAR, Workload_AU_REGIONS_AND_US_SUPPORT, Workload_ASSURED_WORKLOADS_FOR_PARTNERS
    
    
    const (
    	// Unknown compliance regime.
    	Workload_COMPLIANCE_REGIME_UNSPECIFIED Workload_ComplianceRegime = 0
    	// Information protection as per DoD IL4 requirements.
    	Workload_IL4 Workload_ComplianceRegime = 1
    	// Criminal Justice Information Services (CJIS) Security policies.
    	Workload_CJIS Workload_ComplianceRegime = 2
    	// FedRAMP High data protection controls
    	Workload_FEDRAMP_HIGH Workload_ComplianceRegime = 3
    	// FedRAMP Moderate data protection controls
    	Workload_FEDRAMP_MODERATE Workload_ComplianceRegime = 4
    	// Assured Workloads For US Regions data protection controls
    	Workload_US_REGIONAL_ACCESS Workload_ComplianceRegime = 5
    	// Health Insurance Portability and Accountability Act controls
    	Workload_HIPAA Workload_ComplianceRegime = 6
    	// Health Information Trust Alliance controls
    	Workload_HITRUST Workload_ComplianceRegime = 7
    	// Assured Workloads For EU Regions and Support controls
    	Workload_EU_REGIONS_AND_SUPPORT Workload_ComplianceRegime = 8
    	// Assured Workloads For Canada Regions and Support controls
    	Workload_CA_REGIONS_AND_SUPPORT Workload_ComplianceRegime = 9
    	// International Traffic in Arms Regulations
    	Workload_ITAR Workload_ComplianceRegime = 10
    	// Assured Workloads for Australia Regions and Support controls
    	// Available for public preview consumption.
    	// Don't create production workloads.
    	Workload_AU_REGIONS_AND_US_SUPPORT Workload_ComplianceRegime = 11
    	// Assured Workloads for Partners
    	Workload_ASSURED_WORKLOADS_FOR_PARTNERS Workload_ComplianceRegime = 12
    )

### func (Workload_ComplianceRegime) Descriptor 
    
    
    func (Workload_ComplianceRegime) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_ComplianceRegime) Enum 
    
    
    func (x Workload_ComplianceRegime) Enum() *Workload_ComplianceRegime

### func (Workload_ComplianceRegime) EnumDescriptor 
    
    
    func (Workload_ComplianceRegime) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_ComplianceRegime.Descriptor instead.

### func (Workload_ComplianceRegime) Number 
    
    
    func (x Workload_ComplianceRegime) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_ComplianceRegime) String 
    
    
    func (x Workload_ComplianceRegime) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_ComplianceRegime) Type 
    
    
    func (Workload_ComplianceRegime) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload_KMSSettings (deprecated)
    
    
    type Workload_KMSSettings struct {
    
    	// Required. Input only. Immutable. The time at which the Key Management Service will automatically create a
    	// new version of the crypto key and mark it as the primary.
    	NextRotationTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=next_rotation_time,json=nextRotationTime,proto3" json:"next_rotation_time,omitempty"`
    	// Required. Input only. Immutable. [next_rotation_time] will be advanced by this period when the Key
    	// Management Service automatically rotates a key. Must be at least 24 hours
    	// and at most 876,000 hours.
    	RotationPeriod *durationpb.Duration `protobuf:"bytes,2,opt,name=rotation_period,json=rotationPeriod,proto3" json:"rotation_period,omitempty"`
    	// contains filtered or unexported fields
    }

Settings specific to the Key Management Service. This message is deprecated. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.

Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.

### func (*Workload_KMSSettings) Descriptor (deprecated)
    
    
    func (*Workload_KMSSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_KMSSettings.ProtoReflect.Descriptor instead.

### func (*Workload_KMSSettings) GetNextRotationTime (deprecated)
    
    
    func (x *Workload_KMSSettings) GetNextRotationTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Workload_KMSSettings) GetRotationPeriod (deprecated)
    
    
    func (x *Workload_KMSSettings) GetRotationPeriod() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Workload_KMSSettings) ProtoMessage (deprecated)
    
    
    func (*Workload_KMSSettings) ProtoMessage()

### func (*Workload_KMSSettings) ProtoReflect (deprecated)
    
    
    func (x *Workload_KMSSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Workload_KMSSettings) Reset (deprecated)
    
    
    func (x *Workload_KMSSettings) Reset()

### func (*Workload_KMSSettings) String (deprecated)
    
    
    func (x *Workload_KMSSettings) String() [string](https://pkg.go.dev/builtin#string)

## Workload_KajEnrollmentState
    
    
    type Workload_KajEnrollmentState [int32](https://pkg.go.dev/builtin#int32)

Key Access Justifications(KAJ) Enrollment State.

### Workload_KAJ_ENROLLMENT_STATE_UNSPECIFIED, Workload_KAJ_ENROLLMENT_STATE_PENDING, Workload_KAJ_ENROLLMENT_STATE_COMPLETE
    
    
    const (
    	// Default State for KAJ Enrollment.
    	Workload_KAJ_ENROLLMENT_STATE_UNSPECIFIED Workload_KajEnrollmentState = 0
    	// Pending State for KAJ Enrollment.
    	Workload_KAJ_ENROLLMENT_STATE_PENDING Workload_KajEnrollmentState = 1
    	// Complete State for KAJ Enrollment.
    	Workload_KAJ_ENROLLMENT_STATE_COMPLETE Workload_KajEnrollmentState = 2
    )

### func (Workload_KajEnrollmentState) Descriptor 
    
    
    func (Workload_KajEnrollmentState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_KajEnrollmentState) Enum 
    
    
    func (x Workload_KajEnrollmentState) Enum() *Workload_KajEnrollmentState

### func (Workload_KajEnrollmentState) EnumDescriptor 
    
    
    func (Workload_KajEnrollmentState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_KajEnrollmentState.Descriptor instead.

### func (Workload_KajEnrollmentState) Number 
    
    
    func (x Workload_KajEnrollmentState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_KajEnrollmentState) String 
    
    
    func (x Workload_KajEnrollmentState) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_KajEnrollmentState) Type 
    
    
    func (Workload_KajEnrollmentState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload_Partner
    
    
    type Workload_Partner [int32](https://pkg.go.dev/builtin#int32)

Supported Assured Workloads Partners.

### Workload_PARTNER_UNSPECIFIED, Workload_LOCAL_CONTROLS_BY_S3NS
    
    
    const (
    	// Unknown partner regime/controls.
    	Workload_PARTNER_UNSPECIFIED Workload_Partner = 0
    	// S3NS regime/controls.
    	Workload_LOCAL_CONTROLS_BY_S3NS Workload_Partner = 1
    )

### func (Workload_Partner) Descriptor 
    
    
    func (Workload_Partner) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_Partner) Enum 
    
    
    func (x Workload_Partner) Enum() *Workload_Partner

### func (Workload_Partner) EnumDescriptor 
    
    
    func (Workload_Partner) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_Partner.Descriptor instead.

### func (Workload_Partner) Number 
    
    
    func (x Workload_Partner) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_Partner) String 
    
    
    func (x Workload_Partner) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_Partner) Type 
    
    
    func (Workload_Partner) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload_ResourceInfo
    
    
    type Workload_ResourceInfo struct {
    
    	// Resource identifier.
    	// For a project this represents project_number.
    	ResourceId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=resource_id,json=resourceId,proto3" json:"resource_id,omitempty"`
    	// Indicates the type of resource.
    	ResourceType Workload_ResourceInfo_ResourceType `protobuf:"varint,2,opt,name=resource_type,json=resourceType,proto3,enum=google.cloud.assuredworkloads.v1.Workload_ResourceInfo_ResourceType" json:"resource_type,omitempty"`
    	// contains filtered or unexported fields
    }

Represent the resources that are children of this Workload.

### func (*Workload_ResourceInfo) Descriptor 
    
    
    func (*Workload_ResourceInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_ResourceInfo.ProtoReflect.Descriptor instead.

### func (*Workload_ResourceInfo) GetResourceId 
    
    
    func (x *Workload_ResourceInfo) GetResourceId() [int64](https://pkg.go.dev/builtin#int64)

### func (*Workload_ResourceInfo) GetResourceType 
    
    
    func (x *Workload_ResourceInfo) GetResourceType() Workload_ResourceInfo_ResourceType

### func (*Workload_ResourceInfo) ProtoMessage 
    
    
    func (*Workload_ResourceInfo) ProtoMessage()

### func (*Workload_ResourceInfo) ProtoReflect 
    
    
    func (x *Workload_ResourceInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Workload_ResourceInfo) Reset 
    
    
    func (x *Workload_ResourceInfo) Reset()

### func (*Workload_ResourceInfo) String 
    
    
    func (x *Workload_ResourceInfo) String() [string](https://pkg.go.dev/builtin#string)

## Workload_ResourceInfo_ResourceType
    
    
    type Workload_ResourceInfo_ResourceType [int32](https://pkg.go.dev/builtin#int32)

The type of resource.

### Workload_ResourceInfo_RESOURCE_TYPE_UNSPECIFIED, Workload_ResourceInfo_CONSUMER_PROJECT, Workload_ResourceInfo_CONSUMER_FOLDER, Workload_ResourceInfo_ENCRYPTION_KEYS_PROJECT, Workload_ResourceInfo_KEYRING
    
    
    const (
    	// Unknown resource type.
    	Workload_ResourceInfo_RESOURCE_TYPE_UNSPECIFIED Workload_ResourceInfo_ResourceType = 0
    	// Consumer project.
    	// AssuredWorkloads Projects are no longer supported. This field will be
    	// ignored only in CreateWorkload requests. ListWorkloads and GetWorkload
    	// will continue to provide projects information.
    	// Use CONSUMER_FOLDER instead.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/assuredworkloads/v1/assuredworkloads.proto.
    	Workload_ResourceInfo_CONSUMER_PROJECT Workload_ResourceInfo_ResourceType = 1
    	// Consumer Folder.
    	Workload_ResourceInfo_CONSUMER_FOLDER Workload_ResourceInfo_ResourceType = 4
    	// Consumer project containing encryption keys.
    	Workload_ResourceInfo_ENCRYPTION_KEYS_PROJECT Workload_ResourceInfo_ResourceType = 2
    	// Keyring resource that hosts encryption keys.
    	Workload_ResourceInfo_KEYRING Workload_ResourceInfo_ResourceType = 3
    )

### func (Workload_ResourceInfo_ResourceType) Descriptor 
    
    
    func (Workload_ResourceInfo_ResourceType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_ResourceInfo_ResourceType) Enum 
    
    
    func (x Workload_ResourceInfo_ResourceType) Enum() *Workload_ResourceInfo_ResourceType

### func (Workload_ResourceInfo_ResourceType) EnumDescriptor 
    
    
    func (Workload_ResourceInfo_ResourceType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_ResourceInfo_ResourceType.Descriptor instead.

### func (Workload_ResourceInfo_ResourceType) Number 
    
    
    func (x Workload_ResourceInfo_ResourceType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_ResourceInfo_ResourceType) String 
    
    
    func (x Workload_ResourceInfo_ResourceType) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_ResourceInfo_ResourceType) Type 
    
    
    func (Workload_ResourceInfo_ResourceType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload_ResourceSettings
    
    
    type Workload_ResourceSettings struct {
    
    	// Resource identifier.
    	// For a project this represents project_id. If the project is already
    	// taken, the workload creation will fail.
    	// For KeyRing, this represents the keyring_id.
    	// For a folder, don't set this value as folder_id is assigned by Google.
    	ResourceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=resource_id,json=resourceId,proto3" json:"resource_id,omitempty"`
    	// Indicates the type of resource. This field should be specified to
    	// correspond the id to the right resource type (CONSUMER_FOLDER or
    	// ENCRYPTION_KEYS_PROJECT)
    	ResourceType Workload_ResourceInfo_ResourceType `protobuf:"varint,2,opt,name=resource_type,json=resourceType,proto3,enum=google.cloud.assuredworkloads.v1.Workload_ResourceInfo_ResourceType" json:"resource_type,omitempty"`
    	// User-assigned resource display name.
    	// If not empty it will be used to create a resource with the specified
    	// name.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Represent the custom settings for the resources to be created.

### func (*Workload_ResourceSettings) Descriptor 
    
    
    func (*Workload_ResourceSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_ResourceSettings.ProtoReflect.Descriptor instead.

### func (*Workload_ResourceSettings) GetDisplayName 
    
    
    func (x *Workload_ResourceSettings) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Workload_ResourceSettings) GetResourceId 
    
    
    func (x *Workload_ResourceSettings) GetResourceId() [string](https://pkg.go.dev/builtin#string)

### func (*Workload_ResourceSettings) GetResourceType 
    
    
    func (x *Workload_ResourceSettings) GetResourceType() Workload_ResourceInfo_ResourceType

### func (*Workload_ResourceSettings) ProtoMessage 
    
    
    func (*Workload_ResourceSettings) ProtoMessage()

### func (*Workload_ResourceSettings) ProtoReflect 
    
    
    func (x *Workload_ResourceSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Workload_ResourceSettings) Reset 
    
    
    func (x *Workload_ResourceSettings) Reset()

### func (*Workload_ResourceSettings) String 
    
    
    func (x *Workload_ResourceSettings) String() [string](https://pkg.go.dev/builtin#string)

## Workload_SaaEnrollmentResponse
    
    
    type Workload_SaaEnrollmentResponse struct {
    
    	// Indicates SAA enrollment status of a given workload.
    	SetupStatus *Workload_SaaEnrollmentResponse_SetupState `protobuf:"varint,1,opt,name=setup_status,json=setupStatus,proto3,enum=google.cloud.assuredworkloads.v1.Workload_SaaEnrollmentResponse_SetupState,oneof" json:"setup_status,omitempty"`
    	// Indicates SAA enrollment setup error if any.
    	SetupErrors []Workload_SaaEnrollmentResponse_SetupError `protobuf:"varint,2,rep,packed,name=setup_errors,json=setupErrors,proto3,enum=google.cloud.assuredworkloads.v1.Workload_SaaEnrollmentResponse_SetupError" json:"setup_errors,omitempty"`
    	// contains filtered or unexported fields
    }

Signed Access Approvals (SAA) enrollment response.

### func (*Workload_SaaEnrollmentResponse) Descriptor 
    
    
    func (*Workload_SaaEnrollmentResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_SaaEnrollmentResponse.ProtoReflect.Descriptor instead.

### func (*Workload_SaaEnrollmentResponse) GetSetupErrors 
    
    
    func (x *Workload_SaaEnrollmentResponse) GetSetupErrors() []Workload_SaaEnrollmentResponse_SetupError

### func (*Workload_SaaEnrollmentResponse) GetSetupStatus 
    
    
    func (x *Workload_SaaEnrollmentResponse) GetSetupStatus() Workload_SaaEnrollmentResponse_SetupState

### func (*Workload_SaaEnrollmentResponse) ProtoMessage 
    
    
    func (*Workload_SaaEnrollmentResponse) ProtoMessage()

### func (*Workload_SaaEnrollmentResponse) ProtoReflect 
    
    
    func (x *Workload_SaaEnrollmentResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Workload_SaaEnrollmentResponse) Reset 
    
    
    func (x *Workload_SaaEnrollmentResponse) Reset()

### func (*Workload_SaaEnrollmentResponse) String 
    
    
    func (x *Workload_SaaEnrollmentResponse) String() [string](https://pkg.go.dev/builtin#string)

## Workload_SaaEnrollmentResponse_SetupError
    
    
    type Workload_SaaEnrollmentResponse_SetupError [int32](https://pkg.go.dev/builtin#int32)

Setup error of SAA enrollment.

### Workload_SaaEnrollmentResponse_SETUP_ERROR_UNSPECIFIED, Workload_SaaEnrollmentResponse_ERROR_INVALID_BASE_SETUP, Workload_SaaEnrollmentResponse_ERROR_MISSING_EXTERNAL_SIGNING_KEY, Workload_SaaEnrollmentResponse_ERROR_NOT_ALL_SERVICES_ENROLLED, Workload_SaaEnrollmentResponse_ERROR_SETUP_CHECK_FAILED
    
    
    const (
    	// Unspecified.
    	Workload_SaaEnrollmentResponse_SETUP_ERROR_UNSPECIFIED Workload_SaaEnrollmentResponse_SetupError = 0
    	// Invalid states for all customers, to be redirected to AA UI for
    	// additional details.
    	Workload_SaaEnrollmentResponse_ERROR_INVALID_BASE_SETUP Workload_SaaEnrollmentResponse_SetupError = 1
    	// Returned when there is not an EKM key configured.
    	Workload_SaaEnrollmentResponse_ERROR_MISSING_EXTERNAL_SIGNING_KEY Workload_SaaEnrollmentResponse_SetupError = 2
    	// Returned when there are no enrolled services or the customer is
    	// enrolled in CAA only for a subset of services.
    	Workload_SaaEnrollmentResponse_ERROR_NOT_ALL_SERVICES_ENROLLED Workload_SaaEnrollmentResponse_SetupError = 3
    	// Returned when exception was encountered during evaluation of other
    	// criteria.
    	Workload_SaaEnrollmentResponse_ERROR_SETUP_CHECK_FAILED Workload_SaaEnrollmentResponse_SetupError = 4
    )

### func (Workload_SaaEnrollmentResponse_SetupError) Descriptor 
    
    
    func (Workload_SaaEnrollmentResponse_SetupError) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_SaaEnrollmentResponse_SetupError) Enum 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupError) Enum() *Workload_SaaEnrollmentResponse_SetupError

### func (Workload_SaaEnrollmentResponse_SetupError) EnumDescriptor 
    
    
    func (Workload_SaaEnrollmentResponse_SetupError) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_SaaEnrollmentResponse_SetupError.Descriptor instead.

### func (Workload_SaaEnrollmentResponse_SetupError) Number 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupError) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_SaaEnrollmentResponse_SetupError) String 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupError) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_SaaEnrollmentResponse_SetupError) Type 
    
    
    func (Workload_SaaEnrollmentResponse_SetupError) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Workload_SaaEnrollmentResponse_SetupState
    
    
    type Workload_SaaEnrollmentResponse_SetupState [int32](https://pkg.go.dev/builtin#int32)

Setup state of SAA enrollment.

### Workload_SaaEnrollmentResponse_SETUP_STATE_UNSPECIFIED, Workload_SaaEnrollmentResponse_STATUS_PENDING, Workload_SaaEnrollmentResponse_STATUS_COMPLETE
    
    
    const (
    	// Unspecified.
    	Workload_SaaEnrollmentResponse_SETUP_STATE_UNSPECIFIED Workload_SaaEnrollmentResponse_SetupState = 0
    	// SAA enrollment pending.
    	Workload_SaaEnrollmentResponse_STATUS_PENDING Workload_SaaEnrollmentResponse_SetupState = 1
    	// SAA enrollment comopleted.
    	Workload_SaaEnrollmentResponse_STATUS_COMPLETE Workload_SaaEnrollmentResponse_SetupState = 2
    )

### func (Workload_SaaEnrollmentResponse_SetupState) Descriptor 
    
    
    func (Workload_SaaEnrollmentResponse_SetupState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Workload_SaaEnrollmentResponse_SetupState) Enum 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupState) Enum() *Workload_SaaEnrollmentResponse_SetupState

### func (Workload_SaaEnrollmentResponse_SetupState) EnumDescriptor 
    
    
    func (Workload_SaaEnrollmentResponse_SetupState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Workload_SaaEnrollmentResponse_SetupState.Descriptor instead.

### func (Workload_SaaEnrollmentResponse_SetupState) Number 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Workload_SaaEnrollmentResponse_SetupState) String 
    
    
    func (x Workload_SaaEnrollmentResponse_SetupState) String() [string](https://pkg.go.dev/builtin#string)

### func (Workload_SaaEnrollmentResponse_SetupState) Type 
    
    
    func (Workload_SaaEnrollmentResponse_SetupState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
