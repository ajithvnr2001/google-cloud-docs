---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auditmanager/latest/apiv1main/auditmanagerpb/
title: Audit Manager API v1main - Package cloud.google.com/go/auditmanager/apiv1main/auditmanagerpb (v0.1.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:54.260727+00:00
---

# Audit Manager API v1main - Package cloud.google.com/go/auditmanager/apiv1main/auditmanagerpb (v0.1.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auditmanager/latest/apiv1main/auditmanagerpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Audit Manager API v1main - Package cloud.google.com/go/auditmanager/apiv1main/auditmanagerpb (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.0 (latest)  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/auditmanager/apiv1main/auditmanagerpb). 

##  Constants 

### AuditManager_EnrollResource_FullMethodName, AuditManager_GenerateAuditScopeReport_FullMethodName, AuditManager_GenerateAuditReport_FullMethodName, AuditManager_ListAuditReports_FullMethodName, AuditManager_GetAuditReport_FullMethodName, AuditManager_GetResourceEnrollmentStatus_FullMethodName, AuditManager_ListResourceEnrollmentStatuses_FullMethodName, AuditManager_ListControls_FullMethodName
    
    
    const (
    	AuditManager_EnrollResource_FullMethodName                 = "/google.cloud.auditmanager.v1.AuditManager/EnrollResource"
    	AuditManager_GenerateAuditScopeReport_FullMethodName       = "/google.cloud.auditmanager.v1.AuditManager/GenerateAuditScopeReport"
    	AuditManager_GenerateAuditReport_FullMethodName            = "/google.cloud.auditmanager.v1.AuditManager/GenerateAuditReport"
    	AuditManager_ListAuditReports_FullMethodName               = "/google.cloud.auditmanager.v1.AuditManager/ListAuditReports"
    	AuditManager_GetAuditReport_FullMethodName                 = "/google.cloud.auditmanager.v1.AuditManager/GetAuditReport"
    	AuditManager_GetResourceEnrollmentStatus_FullMethodName    = "/google.cloud.auditmanager.v1.AuditManager/GetResourceEnrollmentStatus"
    	AuditManager_ListResourceEnrollmentStatuses_FullMethodName = "/google.cloud.auditmanager.v1.AuditManager/ListResourceEnrollmentStatuses"
    	AuditManager_ListControls_FullMethodName                   = "/google.cloud.auditmanager.v1.AuditManager/ListControls"
    )

## Variables 

### OperationState_name, OperationState_value
    
    
    var (
    	OperationState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "OPERATION_STATE_UNSPECIFIED",
    		10: "OPERATION_STATE_NOT_STARTED",
    		20: "OPERATION_STATE_EVALUATION_IN_PROGRESS",
    		21: "OPERATION_STATE_EVALUATION_DONE",
    		30: "OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS",
    		31: "OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE",
    		40: "OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS",
    		50: "OPERATION_STATE_DONE",
    		60: "OPERATION_STATE_FAILED",
    	}
    	OperationState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"OPERATION_STATE_UNSPECIFIED":                            0,
    		"OPERATION_STATE_NOT_STARTED":                            10,
    		"OPERATION_STATE_EVALUATION_IN_PROGRESS":                 20,
    		"OPERATION_STATE_EVALUATION_DONE":                        21,
    		"OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS": 30,
    		"OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE":        31,
    		"OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS":            40,
    		"OPERATION_STATE_DONE":                                   50,
    		"OPERATION_STATE_FAILED":                                 60,
    	}
    )

Enum value maps for OperationState.

### ComplianceState_name, ComplianceState_value
    
    
    var (
    	ComplianceState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "COMPLIANCE_STATE_UNSPECIFIED",
    		1: "COMPLIANT",
    		2: "VIOLATION",
    		3: "MANUAL_REVIEW_NEEDED",
    		4: "ERROR",
    		5: "AUDIT_NOT_SUPPORTED",
    	}
    	ComplianceState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMPLIANCE_STATE_UNSPECIFIED": 0,
    		"COMPLIANT":                    1,
    		"VIOLATION":                    2,
    		"MANUAL_REVIEW_NEEDED":         3,
    		"ERROR":                        4,
    		"AUDIT_NOT_SUPPORTED":          5,
    	}
    )

Enum value maps for ComplianceState.

### GenerateAuditScopeReportRequest_AuditScopeReportFormat_name, GenerateAuditScopeReportRequest_AuditScopeReportFormat_value
    
    
    var (
    	GenerateAuditScopeReportRequest_AuditScopeReportFormat_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED",
    		1: "AUDIT_SCOPE_REPORT_FORMAT_ODF",
    	}
    	GenerateAuditScopeReportRequest_AuditScopeReportFormat_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED": 0,
    		"AUDIT_SCOPE_REPORT_FORMAT_ODF":         1,
    	}
    )

Enum value maps for GenerateAuditScopeReportRequest_AuditScopeReportFormat.

### GenerateAuditReportRequest_AuditReportFormat_name, GenerateAuditReportRequest_AuditReportFormat_value
    
    
    var (
    	GenerateAuditReportRequest_AuditReportFormat_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "AUDIT_REPORT_FORMAT_UNSPECIFIED",
    		1: "AUDIT_REPORT_FORMAT_ODF",
    	}
    	GenerateAuditReportRequest_AuditReportFormat_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"AUDIT_REPORT_FORMAT_UNSPECIFIED": 0,
    		"AUDIT_REPORT_FORMAT_ODF":         1,
    	}
    )

Enum value maps for GenerateAuditReportRequest_AuditReportFormat.

### ResourceEnrollmentStatus_ResourceEnrollmentState_name, ResourceEnrollmentStatus_ResourceEnrollmentState_value
    
    
    var (
    	ResourceEnrollmentStatus_ResourceEnrollmentState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RESOURCE_ENROLLMENT_STATE_UNSPECIFIED",
    		1: "NOT_ENROLLED",
    		2: "INHERITED",
    		3: "ENROLLED",
    	}
    	ResourceEnrollmentStatus_ResourceEnrollmentState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RESOURCE_ENROLLMENT_STATE_UNSPECIFIED": 0,
    		"NOT_ENROLLED":                          1,
    		"INHERITED":                             2,
    		"ENROLLED":                              3,
    	}
    )

Enum value maps for ResourceEnrollmentStatus_ResourceEnrollmentState.

### AuditReport_ReportGenerationState_name, AuditReport_ReportGenerationState_value
    
    
    var (
    	AuditReport_ReportGenerationState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "REPORT_GENERATION_STATE_UNSPECIFIED",
    		1: "IN_PROGRESS",
    		2: "COMPLETED",
    		3: "FAILED",
    		4: "SUMMARY_UNKNOWN",
    	}
    	AuditReport_ReportGenerationState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"REPORT_GENERATION_STATE_UNSPECIFIED": 0,
    		"IN_PROGRESS":                         1,
    		"COMPLETED":                           2,
    		"FAILED":                              3,
    		"SUMMARY_UNKNOWN":                     4,
    	}
    )

Enum value maps for AuditReport_ReportGenerationState.

### Control_Family_name, Control_Family_value
    
    
    var (
    	Control_Family_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "FAMILY_UNSPECIFIED",
    		1:  "AC",
    		2:  "AT",
    		3:  "AU",
    		4:  "CA",
    		5:  "CM",
    		6:  "CP",
    		7:  "IA",
    		8:  "IR",
    		9:  "MA",
    		10: "MP",
    		11: "PE",
    		12: "PL",
    		13: "PS",
    		14: "RA",
    		15: "SA",
    		16: "SC",
    		17: "SI",
    		18: "SR",
    	}
    	Control_Family_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FAMILY_UNSPECIFIED": 0,
    		"AC":                 1,
    		"AT":                 2,
    		"AU":                 3,
    		"CA":                 4,
    		"CM":                 5,
    		"CP":                 6,
    		"IA":                 7,
    		"IR":                 8,
    		"MA":                 9,
    		"MP":                 10,
    		"PE":                 11,
    		"PL":                 12,
    		"PS":                 13,
    		"RA":                 14,
    		"SA":                 15,
    		"SC":                 16,
    		"SI":                 17,
    		"SR":                 18,
    	}
    )

Enum value maps for Control_Family.

### AuditManager_ServiceDesc
    
    
    var AuditManager_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.auditmanager.v1.AuditManager",
    	HandlerType: (*AuditManagerServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "EnrollResource",
    			Handler:    _AuditManager_EnrollResource_Handler,
    		},
    		{
    			MethodName: "GenerateAuditScopeReport",
    			Handler:    _AuditManager_GenerateAuditScopeReport_Handler,
    		},
    		{
    			MethodName: "GenerateAuditReport",
    			Handler:    _AuditManager_GenerateAuditReport_Handler,
    		},
    		{
    			MethodName: "ListAuditReports",
    			Handler:    _AuditManager_ListAuditReports_Handler,
    		},
    		{
    			MethodName: "GetAuditReport",
    			Handler:    _AuditManager_GetAuditReport_Handler,
    		},
    		{
    			MethodName: "GetResourceEnrollmentStatus",
    			Handler:    _AuditManager_GetResourceEnrollmentStatus_Handler,
    		},
    		{
    			MethodName: "ListResourceEnrollmentStatuses",
    			Handler:    _AuditManager_ListResourceEnrollmentStatuses_Handler,
    		},
    		{
    			MethodName: "ListControls",
    			Handler:    _AuditManager_ListControls_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/auditmanager/v1/auditmanager.proto",
    }

AuditManager_ServiceDesc is the grpc.ServiceDesc for AuditManager service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_auditmanager_v1_auditmanager_proto
    
    
    var File_google_cloud_auditmanager_v1_auditmanager_proto protoreflect.FileDescriptor

## Functions 

### func RegisterAuditManagerServer 
    
    
    func RegisterAuditManagerServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AuditManagerServer)

## AuditManagerClient
    
    
    type AuditManagerClient interface {
    	// Enrolls the customer resource(folder/project/organization) to the audit
    	// manager service by creating the audit managers Service Agent in customers
    	// workload and granting required permissions to the Service Agent. Please
    	// note that if enrollment request is made on the already enrolled workload
    	// then enrollment is executed overriding the existing set of destinations.
    	EnrollResource(ctx context.Context, in *EnrollResourceRequest, opts ...grpc.CallOption) (*Enrollment, [error](https://pkg.go.dev/builtin#error))
    	// Generates a demo report highlighting different responsibilities
    	// (Google/Customer/ shared) required to be fulfilled for the customer's
    	// workload to be compliant with the given standard.
    	GenerateAuditScopeReport(ctx context.Context, in *GenerateAuditScopeReportRequest, opts ...grpc.CallOption) (*AuditScopeReport, [error](https://pkg.go.dev/builtin#error))
    	// Register the Audit Report generation requests and returns the OperationId
    	// using which the customer can track the report generation progress.
    	GenerateAuditReport(ctx context.Context, in *GenerateAuditReportRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists audit reports in the selected parent scope
    	ListAuditReports(ctx context.Context, in *ListAuditReportsRequest, opts ...grpc.CallOption) (*ListAuditReportsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Get the overall audit report
    	GetAuditReport(ctx context.Context, in *GetAuditReportRequest, opts ...grpc.CallOption) (*AuditReport, [error](https://pkg.go.dev/builtin#error))
    	// Get a resource along with its enrollment status.
    	GetResourceEnrollmentStatus(ctx context.Context, in *GetResourceEnrollmentStatusRequest, opts ...grpc.CallOption) (*ResourceEnrollmentStatus, [error](https://pkg.go.dev/builtin#error))
    	// Fetches all resources under the parent along with their enrollment.
    	ListResourceEnrollmentStatuses(ctx context.Context, in *ListResourceEnrollmentStatusesRequest, opts ...grpc.CallOption) (*ListResourceEnrollmentStatusesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets controls needed to be implemented to be compliant to a standard.
    	ListControls(ctx context.Context, in *ListControlsRequest, opts ...grpc.CallOption) (*ListControlsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AuditManagerClient is the client API for AuditManager service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAuditManagerClient 
    
    
    func NewAuditManagerClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AuditManagerClient

## AuditManagerServer
    
    
    type AuditManagerServer interface {
    	// Enrolls the customer resource(folder/project/organization) to the audit
    	// manager service by creating the audit managers Service Agent in customers
    	// workload and granting required permissions to the Service Agent. Please
    	// note that if enrollment request is made on the already enrolled workload
    	// then enrollment is executed overriding the existing set of destinations.
    	EnrollResource(context.Context, *EnrollResourceRequest) (*Enrollment, [error](https://pkg.go.dev/builtin#error))
    	// Generates a demo report highlighting different responsibilities
    	// (Google/Customer/ shared) required to be fulfilled for the customer's
    	// workload to be compliant with the given standard.
    	GenerateAuditScopeReport(context.Context, *GenerateAuditScopeReportRequest) (*AuditScopeReport, [error](https://pkg.go.dev/builtin#error))
    	// Register the Audit Report generation requests and returns the OperationId
    	// using which the customer can track the report generation progress.
    	GenerateAuditReport(context.Context, *GenerateAuditReportRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists audit reports in the selected parent scope
    	ListAuditReports(context.Context, *ListAuditReportsRequest) (*ListAuditReportsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Get the overall audit report
    	GetAuditReport(context.Context, *GetAuditReportRequest) (*AuditReport, [error](https://pkg.go.dev/builtin#error))
    	// Get a resource along with its enrollment status.
    	GetResourceEnrollmentStatus(context.Context, *GetResourceEnrollmentStatusRequest) (*ResourceEnrollmentStatus, [error](https://pkg.go.dev/builtin#error))
    	// Fetches all resources under the parent along with their enrollment.
    	ListResourceEnrollmentStatuses(context.Context, *ListResourceEnrollmentStatusesRequest) (*ListResourceEnrollmentStatusesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets controls needed to be implemented to be compliant to a standard.
    	ListControls(context.Context, *ListControlsRequest) (*ListControlsResponse, [error](https://pkg.go.dev/builtin#error))
    }

AuditManagerServer is the server API for AuditManager service. All implementations should embed UnimplementedAuditManagerServer for forward compatibility

## AuditReport
    
    
    type AuditReport struct {
    
    	// Identifier. The name of this Audit Report, in the format of scope given in
    	// request.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Report summary with compliance, violation counts etc.
    	ReportSummary *ReportSummary `protobuf:"bytes,2,opt,name=report_summary,json=reportSummary,proto3" json:"report_summary,omitempty"`
    	// Output only. ClientOperationId
    	OperationId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=operation_id,json=operationId,proto3" json:"operation_id,omitempty"`
    	// Output only. The location where the generated report will be uploaded.
    	DestinationDetails *DestinationDetails `protobuf:"bytes,4,opt,name=destination_details,json=destinationDetails,proto3" json:"destination_details,omitempty"`
    	// Output only. Compliance Standard.
    	ComplianceStandard [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=compliance_standard,json=complianceStandard,proto3" json:"compliance_standard,omitempty"`
    	// Output only. The parent scope on which the report was generated.
    	Scope [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=scope,proto3" json:"scope,omitempty"`
    	// Output only. Creation time of the audit report.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,7,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The overall status of controls
    	ControlDetails []*ControlDetails `protobuf:"bytes,8,rep,name=control_details,json=controlDetails,proto3" json:"control_details,omitempty"`
    	// Output only. The state of Audit Report Generation.
    	ReportGenerationState AuditReport_ReportGenerationState `protobuf:"varint,9,opt,name=report_generation_state,json=reportGenerationState,proto3,enum=google.cloud.auditmanager.v1.AuditReport_ReportGenerationState" json:"report_generation_state,omitempty"`
    	// Output only. Compliance Framework of Audit Report
    	ComplianceFramework [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,opt,name=compliance_framework,json=complianceFramework,proto3" json:"compliance_framework,omitempty"`
    	// Output only. The ID/ Number for the scope on which the audit report was
    	// generated.
    	ScopeId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=scope_id,json=scopeId,proto3" json:"scope_id,omitempty"`
    	// contains filtered or unexported fields
    }

An audit report.

### func (*AuditReport) Descriptor 
    
    
    func (*AuditReport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AuditReport.ProtoReflect.Descriptor instead.

### func (*AuditReport) GetComplianceFramework 
    
    
    func (x *AuditReport) GetComplianceFramework() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) GetComplianceStandard 
    
    
    func (x *AuditReport) GetComplianceStandard() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) GetControlDetails 
    
    
    func (x *AuditReport) GetControlDetails() []*ControlDetails

### func (*AuditReport) GetCreateTime 
    
    
    func (x *AuditReport) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AuditReport) GetDestinationDetails 
    
    
    func (x *AuditReport) GetDestinationDetails() *DestinationDetails

### func (*AuditReport) GetName 
    
    
    func (x *AuditReport) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) GetOperationId 
    
    
    func (x *AuditReport) GetOperationId() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) GetReportGenerationState 
    
    
    func (x *AuditReport) GetReportGenerationState() AuditReport_ReportGenerationState

### func (*AuditReport) GetReportSummary 
    
    
    func (x *AuditReport) GetReportSummary() *ReportSummary

### func (*AuditReport) GetScope 
    
    
    func (x *AuditReport) GetScope() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) GetScopeId 
    
    
    func (x *AuditReport) GetScopeId() [string](https://pkg.go.dev/builtin#string)

### func (*AuditReport) ProtoMessage 
    
    
    func (*AuditReport) ProtoMessage()

### func (*AuditReport) ProtoReflect 
    
    
    func (x *AuditReport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AuditReport) Reset 
    
    
    func (x *AuditReport) Reset()

### func (*AuditReport) String 
    
    
    func (x *AuditReport) String() [string](https://pkg.go.dev/builtin#string)

## AuditReport_ReportGenerationState
    
    
    type AuditReport_ReportGenerationState [int32](https://pkg.go.dev/builtin#int32)

The different states of the Audit Manager report generation.

### AuditReport_REPORT_GENERATION_STATE_UNSPECIFIED, AuditReport_IN_PROGRESS, AuditReport_COMPLETED, AuditReport_FAILED, AuditReport_SUMMARY_UNKNOWN
    
    
    const (
    	// Unspecified. Invalid state.
    	AuditReport_REPORT_GENERATION_STATE_UNSPECIFIED AuditReport_ReportGenerationState = 0
    	// Audit report generation process is in progress, ie. operation state is
    	// neither OPERATION_STATE_DONE nor OPERATION_STATE_FAILED.
    	AuditReport_IN_PROGRESS AuditReport_ReportGenerationState = 1
    	// Audit report generation process is completed. Operation state is
    	// OPERATION_STATE_DONE.
    	AuditReport_COMPLETED AuditReport_ReportGenerationState = 2
    	// Audit report generation process has failed. Operation state is
    	// OPERATION_STATE_FAILED.
    	AuditReport_FAILED AuditReport_ReportGenerationState = 3
    	// Audit report generation process has completed. But report summary is
    	// unknown. This is valid for older reports.
    	AuditReport_SUMMARY_UNKNOWN AuditReport_ReportGenerationState = 4
    )

### func (AuditReport_ReportGenerationState) Descriptor 
    
    
    func (AuditReport_ReportGenerationState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AuditReport_ReportGenerationState) Enum 
    
    
    func (x AuditReport_ReportGenerationState) Enum() *AuditReport_ReportGenerationState

### func (AuditReport_ReportGenerationState) EnumDescriptor 
    
    
    func (AuditReport_ReportGenerationState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AuditReport_ReportGenerationState.Descriptor instead.

### func (AuditReport_ReportGenerationState) Number 
    
    
    func (x AuditReport_ReportGenerationState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AuditReport_ReportGenerationState) String 
    
    
    func (x AuditReport_ReportGenerationState) String() [string](https://pkg.go.dev/builtin#string)

### func (AuditReport_ReportGenerationState) Type 
    
    
    func (AuditReport_ReportGenerationState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AuditScopeReport
    
    
    type AuditScopeReport struct {
    
    	// The options in which the audit scope report is exported.
    	//
    	// Types that are assignable to AuditReport:
    	//
    	//	*AuditScopeReport_ScopeReportContents
    	AuditReport isAuditScopeReport_AuditReport `protobuf_oneof:"audit_report"`
    	// Identifier. The name of this Audit Report, in the format of scope given in
    	// request.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

The audit scope report.

### func (*AuditScopeReport) Descriptor 
    
    
    func (*AuditScopeReport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AuditScopeReport.ProtoReflect.Descriptor instead.

### func (*AuditScopeReport) GetAuditReport 
    
    
    func (m *AuditScopeReport) GetAuditReport() isAuditScopeReport_AuditReport

### func (*AuditScopeReport) GetName 
    
    
    func (x *AuditScopeReport) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AuditScopeReport) GetScopeReportContents 
    
    
    func (x *AuditScopeReport) GetScopeReportContents() [][byte](https://pkg.go.dev/builtin#byte)

### func (*AuditScopeReport) ProtoMessage 
    
    
    func (*AuditScopeReport) ProtoMessage()

### func (*AuditScopeReport) ProtoReflect 
    
    
    func (x *AuditScopeReport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AuditScopeReport) Reset 
    
    
    func (x *AuditScopeReport) Reset()

### func (*AuditScopeReport) String 
    
    
    func (x *AuditScopeReport) String() [string](https://pkg.go.dev/builtin#string)

## AuditScopeReport_ScopeReportContents
    
    
    type AuditScopeReport_ScopeReportContents struct {
    	// The audit scope report content in byte format.
    	ScopeReportContents [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=scope_report_contents,json=scopeReportContents,proto3,oneof"`
    }

## ComplianceState
    
    
    type ComplianceState [int32](https://pkg.go.dev/builtin#int32)

The compliance state after evaluation.

### ComplianceState_COMPLIANCE_STATE_UNSPECIFIED, ComplianceState_COMPLIANT, ComplianceState_VIOLATION, ComplianceState_MANUAL_REVIEW_NEEDED, ComplianceState_ERROR, ComplianceState_AUDIT_NOT_SUPPORTED
    
    
    const (
    	// Unspecified. Invalid state.
    	ComplianceState_COMPLIANCE_STATE_UNSPECIFIED ComplianceState = 0
    	// Compliant.
    	ComplianceState_COMPLIANT ComplianceState = 1
    	// Violation.
    	ComplianceState_VIOLATION ComplianceState = 2
    	// MANUAL_REVIEW_NEEDED, requires manual review
    	ComplianceState_MANUAL_REVIEW_NEEDED ComplianceState = 3
    	// Error while computing status.
    	ComplianceState_ERROR ComplianceState = 4
    	// Cannot be audited
    	ComplianceState_AUDIT_NOT_SUPPORTED ComplianceState = 5
    )

### func (ComplianceState) Descriptor 
    
    
    func (ComplianceState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ComplianceState) Enum 
    
    
    func (x ComplianceState) Enum() *ComplianceState

### func (ComplianceState) EnumDescriptor 
    
    
    func (ComplianceState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComplianceState.Descriptor instead.

### func (ComplianceState) Number 
    
    
    func (x ComplianceState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ComplianceState) String 
    
    
    func (x ComplianceState) String() [string](https://pkg.go.dev/builtin#string)

### func (ComplianceState) Type 
    
    
    func (ComplianceState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Control
    
    
    type Control struct {
    
    	// Output only. The control identifier used to fetch the findings. This is
    	// same as the control report name.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// Output only. Display name of the control.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. Group where the control belongs. E.g. Access Control.
    	Family Control_Family `protobuf:"varint,3,opt,name=family,proto3,enum=google.cloud.auditmanager.v1.Control_Family" json:"family,omitempty"`
    	// Output only. Regulatory Family of the control E.g. Access Control
    	ControlFamily *ControlFamily `protobuf:"bytes,10,opt,name=control_family,json=controlFamily,proto3" json:"control_family,omitempty"`
    	// Output only. Regulatory control ask of the control
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
    	// Output only. The type of responsibility for implementing this control. It
    	// can be google, customer or shared.
    	ResponsibilityType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=responsibility_type,json=responsibilityType,proto3" json:"responsibility_type,omitempty"`
    	// Output only. Description of the google responsibility for implementing this
    	// control.
    	GoogleResponsibilityDescription [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=google_responsibility_description,json=googleResponsibilityDescription,proto3" json:"google_responsibility_description,omitempty"`
    	// Output only. Implementation of the google responsibility for implementing
    	// this control.
    	GoogleResponsibilityImplementation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=google_responsibility_implementation,json=googleResponsibilityImplementation,proto3" json:"google_responsibility_implementation,omitempty"`
    	// Output only. Description of the customer responsibility for implementing
    	// this control.
    	CustomerResponsibilityDescription [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=customer_responsibility_description,json=customerResponsibilityDescription,proto3" json:"customer_responsibility_description,omitempty"`
    	// Output only. Implementation of the customer responsibility for implementing
    	// this control.
    	CustomerResponsibilityImplementation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=customer_responsibility_implementation,json=customerResponsibilityImplementation,proto3" json:"customer_responsibility_implementation,omitempty"`
    	// contains filtered or unexported fields
    }

A control.

### func (*Control) Descriptor 
    
    
    func (*Control) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Control.ProtoReflect.Descriptor instead.

### func (*Control) GetControlFamily 
    
    
    func (x *Control) GetControlFamily() *ControlFamily

### func (*Control) GetCustomerResponsibilityDescription 
    
    
    func (x *Control) GetCustomerResponsibilityDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetCustomerResponsibilityImplementation 
    
    
    func (x *Control) GetCustomerResponsibilityImplementation() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetDescription 
    
    
    func (x *Control) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetDisplayName 
    
    
    func (x *Control) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetFamily 
    
    
    func (x *Control) GetFamily() Control_Family

### func (*Control) GetGoogleResponsibilityDescription 
    
    
    func (x *Control) GetGoogleResponsibilityDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetGoogleResponsibilityImplementation 
    
    
    func (x *Control) GetGoogleResponsibilityImplementation() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetId 
    
    
    func (x *Control) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*Control) GetResponsibilityType 
    
    
    func (x *Control) GetResponsibilityType() [string](https://pkg.go.dev/builtin#string)

### func (*Control) ProtoMessage 
    
    
    func (*Control) ProtoMessage()

### func (*Control) ProtoReflect 
    
    
    func (x *Control) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Control) Reset 
    
    
    func (x *Control) Reset()

### func (*Control) String 
    
    
    func (x *Control) String() [string](https://pkg.go.dev/builtin#string)

## ControlDetails
    
    
    type ControlDetails struct {
    
    	// The control for which the findings are being reported.
    	Control *Control `protobuf:"bytes,1,opt,name=control,proto3" json:"control,omitempty"`
    	// Output only. Overall status of the findings for the control.
    	ComplianceState ComplianceState `protobuf:"varint,2,opt,name=compliance_state,json=complianceState,proto3,enum=google.cloud.auditmanager.v1.ComplianceState" json:"compliance_state,omitempty"`
    	// Report summary with compliance, violation counts etc.
    	ControlReportSummary *ReportSummary `protobuf:"bytes,3,opt,name=control_report_summary,json=controlReportSummary,proto3" json:"control_report_summary,omitempty"`
    	// contains filtered or unexported fields
    }

The evaluation details for a control.

### func (*ControlDetails) Descriptor 
    
    
    func (*ControlDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ControlDetails.ProtoReflect.Descriptor instead.

### func (*ControlDetails) GetComplianceState 
    
    
    func (x *ControlDetails) GetComplianceState() ComplianceState

### func (*ControlDetails) GetControl 
    
    
    func (x *ControlDetails) GetControl() *Control

### func (*ControlDetails) GetControlReportSummary 
    
    
    func (x *ControlDetails) GetControlReportSummary() *ReportSummary

### func (*ControlDetails) ProtoMessage 
    
    
    func (*ControlDetails) ProtoMessage()

### func (*ControlDetails) ProtoReflect 
    
    
    func (x *ControlDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ControlDetails) Reset 
    
    
    func (x *ControlDetails) Reset()

### func (*ControlDetails) String 
    
    
    func (x *ControlDetails) String() [string](https://pkg.go.dev/builtin#string)

## ControlFamily
    
    
    type ControlFamily struct {
    
    	// The ID of the regulatory control family.
    	FamilyId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=family_id,json=familyId,proto3" json:"family_id,omitempty"`
    	// The display name of the regulatory control family.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

The regulatory family of the control.

### func (*ControlFamily) Descriptor 
    
    
    func (*ControlFamily) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ControlFamily.ProtoReflect.Descriptor instead.

### func (*ControlFamily) GetDisplayName 
    
    
    func (x *ControlFamily) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ControlFamily) GetFamilyId 
    
    
    func (x *ControlFamily) GetFamilyId() [string](https://pkg.go.dev/builtin#string)

### func (*ControlFamily) ProtoMessage 
    
    
    func (*ControlFamily) ProtoMessage()

### func (*ControlFamily) ProtoReflect 
    
    
    func (x *ControlFamily) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ControlFamily) Reset 
    
    
    func (x *ControlFamily) Reset()

### func (*ControlFamily) String 
    
    
    func (x *ControlFamily) String() [string](https://pkg.go.dev/builtin#string)

## Control_Family
    
    
    type Control_Family [int32](https://pkg.go.dev/builtin#int32)

The family of the control. For example, Access Control.

### Control_FAMILY_UNSPECIFIED, Control_AC, Control_AT, Control_AU, Control_CA, Control_CM, Control_CP, Control_IA, Control_IR, Control_MA, Control_MP, Control_PE, Control_PL, Control_PS, Control_RA, Control_SA, Control_SC, Control_SI, Control_SR
    
    
    const (
    	// Unspecified. Invalid state.
    	Control_FAMILY_UNSPECIFIED Control_Family = 0
    	// Access Control
    	Control_AC Control_Family = 1
    	// Awareness and Training
    	Control_AT Control_Family = 2
    	// Audit and Accountability
    	Control_AU Control_Family = 3
    	// Certification, Accreditation and Security Assessments
    	Control_CA Control_Family = 4
    	// Configuration Management
    	Control_CM Control_Family = 5
    	// Contingency Planning
    	Control_CP Control_Family = 6
    	// Identification and Authentication
    	Control_IA Control_Family = 7
    	// Incident Response
    	Control_IR Control_Family = 8
    	// Maintenance
    	Control_MA Control_Family = 9
    	// Media Protection
    	Control_MP Control_Family = 10
    	// Physical and Environmental Protection
    	Control_PE Control_Family = 11
    	// Security Planning
    	Control_PL Control_Family = 12
    	// Personnel Security
    	Control_PS Control_Family = 13
    	// Risk Assessment
    	Control_RA Control_Family = 14
    	// System Services and Acquisition
    	Control_SA Control_Family = 15
    	// System and Communications Protection
    	Control_SC Control_Family = 16
    	// System and Information Integrity
    	Control_SI Control_Family = 17
    	// Supply Chain Risk Management
    	Control_SR Control_Family = 18
    )

### func (Control_Family) Descriptor 
    
    
    func (Control_Family) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Control_Family) Enum 
    
    
    func (x Control_Family) Enum() *Control_Family

### func (Control_Family) EnumDescriptor 
    
    
    func (Control_Family) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Control_Family.Descriptor instead.

### func (Control_Family) Number 
    
    
    func (x Control_Family) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Control_Family) String 
    
    
    func (x Control_Family) String() [string](https://pkg.go.dev/builtin#string)

### func (Control_Family) Type 
    
    
    func (Control_Family) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DestinationDetails
    
    
    type DestinationDetails struct {
    
    	// Types that are assignable to Destination:
    	//
    	//	*DestinationDetails_GcsBucketUri
    	Destination isDestinationDetails_Destination `protobuf_oneof:"destination"`
    	// contains filtered or unexported fields
    }

The locations where the generated reports are saved.

### func (*DestinationDetails) Descriptor 
    
    
    func (*DestinationDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DestinationDetails.ProtoReflect.Descriptor instead.

### func (*DestinationDetails) GetDestination 
    
    
    func (m *DestinationDetails) GetDestination() isDestinationDetails_Destination

### func (*DestinationDetails) GetGcsBucketUri 
    
    
    func (x *DestinationDetails) GetGcsBucketUri() [string](https://pkg.go.dev/builtin#string)

### func (*DestinationDetails) ProtoMessage 
    
    
    func (*DestinationDetails) ProtoMessage()

### func (*DestinationDetails) ProtoReflect 
    
    
    func (x *DestinationDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DestinationDetails) Reset 
    
    
    func (x *DestinationDetails) Reset()

### func (*DestinationDetails) String 
    
    
    func (x *DestinationDetails) String() [string](https://pkg.go.dev/builtin#string)

## DestinationDetails_GcsBucketUri
    
    
    type DestinationDetails_GcsBucketUri struct {
    	// The Cloud Storage bucket where the audit report is/will be uploaded.
    	GcsBucketUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=gcs_bucket_uri,json=gcsBucketUri,proto3,oneof"`
    }

## EnrollResourceRequest
    
    
    type EnrollResourceRequest struct {
    
    	// Required. The resource to be enrolled to the audit manager. Scope format
    	// should be resource_type/resource_identifier Eg:
    	// projects/{project}/locations/{location},
    	// folders/{folder}/locations/{location}
    	// organizations/{organization}/locations/{location}
    	Scope [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=scope,proto3" json:"scope,omitempty"`
    	// Required. List of destination among which customer can choose to upload
    	// their reports during the audit process. While enrolling at a
    	// organization/folder level, customer can choose Cloud storage bucket in any
    	// project. If the audit is triggered at project level using the service agent
    	// at organization/folder level, all the destination options associated with
    	// respective organization/folder level service agent will be available to
    	// auditing projects.
    	Destinations []*EnrollResourceRequest_EligibleDestination `protobuf:"bytes,2,rep,name=destinations,proto3" json:"destinations,omitempty"`
    	// contains filtered or unexported fields
    }

Request message to subscribe the Audit Manager service for given resource.

### func (*EnrollResourceRequest) Descriptor 
    
    
    func (*EnrollResourceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EnrollResourceRequest.ProtoReflect.Descriptor instead.

### func (*EnrollResourceRequest) GetDestinations 
    
    
    func (x *EnrollResourceRequest) GetDestinations() []*EnrollResourceRequest_EligibleDestination

### func (*EnrollResourceRequest) GetScope 
    
    
    func (x *EnrollResourceRequest) GetScope() [string](https://pkg.go.dev/builtin#string)

### func (*EnrollResourceRequest) ProtoMessage 
    
    
    func (*EnrollResourceRequest) ProtoMessage()

### func (*EnrollResourceRequest) ProtoReflect 
    
    
    func (x *EnrollResourceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EnrollResourceRequest) Reset 
    
    
    func (x *EnrollResourceRequest) Reset()

### func (*EnrollResourceRequest) String 
    
    
    func (x *EnrollResourceRequest) String() [string](https://pkg.go.dev/builtin#string)

## EnrollResourceRequest_EligibleDestination
    
    
    type EnrollResourceRequest_EligibleDestination struct {
    
    	// The options for the report destination location.
    	//
    	// Types that are assignable to EligibleDestinations:
    	//
    	//	*EnrollResourceRequest_EligibleDestination_EligibleGcsBucket
    	EligibleDestinations isEnrollResourceRequest_EligibleDestination_EligibleDestinations `protobuf_oneof:"eligible_destinations"`
    	// contains filtered or unexported fields
    }

The destination details where the audit report must be uploaded.

### func (*EnrollResourceRequest_EligibleDestination) Descriptor 
    
    
    func (*EnrollResourceRequest_EligibleDestination) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EnrollResourceRequest_EligibleDestination.ProtoReflect.Descriptor instead.

### func (*EnrollResourceRequest_EligibleDestination) GetEligibleDestinations 
    
    
    func (m *EnrollResourceRequest_EligibleDestination) GetEligibleDestinations() isEnrollResourceRequest_EligibleDestination_EligibleDestinations

### func (*EnrollResourceRequest_EligibleDestination) GetEligibleGcsBucket 
    
    
    func (x *EnrollResourceRequest_EligibleDestination) GetEligibleGcsBucket() [string](https://pkg.go.dev/builtin#string)

### func (*EnrollResourceRequest_EligibleDestination) ProtoMessage 
    
    
    func (*EnrollResourceRequest_EligibleDestination) ProtoMessage()

### func (*EnrollResourceRequest_EligibleDestination) ProtoReflect 
    
    
    func (x *EnrollResourceRequest_EligibleDestination) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EnrollResourceRequest_EligibleDestination) Reset 
    
    
    func (x *EnrollResourceRequest_EligibleDestination) Reset()

### func (*EnrollResourceRequest_EligibleDestination) String 
    
    
    func (x *EnrollResourceRequest_EligibleDestination) String() [string](https://pkg.go.dev/builtin#string)

## EnrollResourceRequest_EligibleDestination_EligibleGcsBucket
    
    
    type EnrollResourceRequest_EligibleDestination_EligibleGcsBucket struct {
    	// The Cloud Storage bucket location where the audit report and evidences
    	// can be uploaded during the `GenerateAuditReport` API call.
    	EligibleGcsBucket [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=eligible_gcs_bucket,json=eligibleGcsBucket,proto3,oneof"`
    }

## Enrollment
    
    
    type Enrollment struct {
    
    	// Identifier. The name of this Enrollment, in the format of scope given in
    	// request.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The locations where the generated reports can be uploaded.
    	DestinationDetails []*DestinationDetails `protobuf:"bytes,3,rep,name=destination_details,json=destinationDetails,proto3" json:"destination_details,omitempty"`
    	// contains filtered or unexported fields
    }

The enrollment resource.

### func (*Enrollment) Descriptor 
    
    
    func (*Enrollment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Enrollment.ProtoReflect.Descriptor instead.

### func (*Enrollment) GetDestinationDetails 
    
    
    func (x *Enrollment) GetDestinationDetails() []*DestinationDetails

### func (*Enrollment) GetName 
    
    
    func (x *Enrollment) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Enrollment) ProtoMessage 
    
    
    func (*Enrollment) ProtoMessage()

### func (*Enrollment) ProtoReflect 
    
    
    func (x *Enrollment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Enrollment) Reset 
    
    
    func (x *Enrollment) Reset()

### func (*Enrollment) String 
    
    
    func (x *Enrollment) String() [string](https://pkg.go.dev/builtin#string)

## GenerateAuditReportRequest
    
    
    type GenerateAuditReportRequest struct {
    
    	// Set of options for the report destination location.
    	//
    	// Types that are assignable to Destination:
    	//
    	//	*GenerateAuditReportRequest_GcsUri
    	Destination isGenerateAuditReportRequest_Destination `protobuf_oneof:"destination"`
    	// Required. Scope for which the AuditScopeReport is required. Must be of
    	// format resource_type/resource_identifier Eg:
    	// projects/{project}/locations/{location},
    	// folders/{folder}/locations/{location}
    	Scope [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=scope,proto3" json:"scope,omitempty"`
    	// Required. Compliance Standard against which the Scope Report must be
    	// generated. Eg: FEDRAMP_MODERATE
    	ComplianceStandard [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=compliance_standard,json=complianceStandard,proto3" json:"compliance_standard,omitempty"`
    	// Required. The format in which the audit report should be created.
    	ReportFormat GenerateAuditReportRequest_AuditReportFormat `protobuf:"varint,4,opt,name=report_format,json=reportFormat,proto3,enum=google.cloud.auditmanager.v1.GenerateAuditReportRequest_AuditReportFormat" json:"report_format,omitempty"`
    	// Required. Compliance framework against which the Report must be generated.
    	ComplianceFramework [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=compliance_framework,json=complianceFramework,proto3" json:"compliance_framework,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting the Audit Report.

### func (*GenerateAuditReportRequest) Descriptor 
    
    
    func (*GenerateAuditReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAuditReportRequest.ProtoReflect.Descriptor instead.

### func (*GenerateAuditReportRequest) GetComplianceFramework 
    
    
    func (x *GenerateAuditReportRequest) GetComplianceFramework() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditReportRequest) GetComplianceStandard 
    
    
    func (x *GenerateAuditReportRequest) GetComplianceStandard() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditReportRequest) GetDestination 
    
    
    func (m *GenerateAuditReportRequest) GetDestination() isGenerateAuditReportRequest_Destination

### func (*GenerateAuditReportRequest) GetGcsUri 
    
    
    func (x *GenerateAuditReportRequest) GetGcsUri() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditReportRequest) GetReportFormat 
    
    
    func (x *GenerateAuditReportRequest) GetReportFormat() GenerateAuditReportRequest_AuditReportFormat

### func (*GenerateAuditReportRequest) GetScope 
    
    
    func (x *GenerateAuditReportRequest) GetScope() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditReportRequest) ProtoMessage 
    
    
    func (*GenerateAuditReportRequest) ProtoMessage()

### func (*GenerateAuditReportRequest) ProtoReflect 
    
    
    func (x *GenerateAuditReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateAuditReportRequest) Reset 
    
    
    func (x *GenerateAuditReportRequest) Reset()

### func (*GenerateAuditReportRequest) String 
    
    
    func (x *GenerateAuditReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateAuditReportRequest_AuditReportFormat
    
    
    type GenerateAuditReportRequest_AuditReportFormat [int32](https://pkg.go.dev/builtin#int32)

The options for the audit report format.

### GenerateAuditReportRequest_AUDIT_REPORT_FORMAT_UNSPECIFIED, GenerateAuditReportRequest_AUDIT_REPORT_FORMAT_ODF
    
    
    const (
    	// Unspecified. Invalid state.
    	GenerateAuditReportRequest_AUDIT_REPORT_FORMAT_UNSPECIFIED GenerateAuditReportRequest_AuditReportFormat = 0
    	// Audit Report creation format is Open Document.
    	GenerateAuditReportRequest_AUDIT_REPORT_FORMAT_ODF GenerateAuditReportRequest_AuditReportFormat = 1
    )

### func (GenerateAuditReportRequest_AuditReportFormat) Descriptor 
    
    
    func (GenerateAuditReportRequest_AuditReportFormat) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (GenerateAuditReportRequest_AuditReportFormat) Enum 
    
    
    func (x GenerateAuditReportRequest_AuditReportFormat) Enum() *GenerateAuditReportRequest_AuditReportFormat

### func (GenerateAuditReportRequest_AuditReportFormat) EnumDescriptor 
    
    
    func (GenerateAuditReportRequest_AuditReportFormat) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAuditReportRequest_AuditReportFormat.Descriptor instead.

### func (GenerateAuditReportRequest_AuditReportFormat) Number 
    
    
    func (x GenerateAuditReportRequest_AuditReportFormat) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (GenerateAuditReportRequest_AuditReportFormat) String 
    
    
    func (x GenerateAuditReportRequest_AuditReportFormat) String() [string](https://pkg.go.dev/builtin#string)

### func (GenerateAuditReportRequest_AuditReportFormat) Type 
    
    
    func (GenerateAuditReportRequest_AuditReportFormat) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GenerateAuditReportRequest_GcsUri
    
    
    type GenerateAuditReportRequest_GcsUri struct {
    	// Destination Cloud storage bucket where report and evidence must be
    	// uploaded. The Cloud storage bucket provided here must be selected among
    	// the buckets entered during the enrollment process.
    	GcsUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=gcs_uri,json=gcsUri,proto3,oneof"`
    }

## GenerateAuditScopeReportRequest
    
    
    type GenerateAuditScopeReportRequest struct {
    
    	// Required. Scope for which the AuditScopeReport is required. Must be of
    	// format resource_type/resource_identifier Eg:
    	// projects/{project}/locations/{location},
    	// folders/{folder}/locations/{location}
    	Scope [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=scope,proto3" json:"scope,omitempty"`
    	// Required. Compliance Standard against which the Scope Report must be
    	// generated. Eg: FEDRAMP_MODERATE
    	ComplianceStandard [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=compliance_standard,json=complianceStandard,proto3" json:"compliance_standard,omitempty"`
    	// Required. The format in which the Scope report bytes should be returned.
    	ReportFormat GenerateAuditScopeReportRequest_AuditScopeReportFormat `protobuf:"varint,4,opt,name=report_format,json=reportFormat,proto3,enum=google.cloud.auditmanager.v1.GenerateAuditScopeReportRequest_AuditScopeReportFormat" json:"report_format,omitempty"`
    	// Required. Compliance framework against which the Scope Report must be
    	// generated.
    	ComplianceFramework [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=compliance_framework,json=complianceFramework,proto3" json:"compliance_framework,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting audit scope report.

### func (*GenerateAuditScopeReportRequest) Descriptor 
    
    
    func (*GenerateAuditScopeReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAuditScopeReportRequest.ProtoReflect.Descriptor instead.

### func (*GenerateAuditScopeReportRequest) GetComplianceFramework 
    
    
    func (x *GenerateAuditScopeReportRequest) GetComplianceFramework() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditScopeReportRequest) GetComplianceStandard 
    
    
    func (x *GenerateAuditScopeReportRequest) GetComplianceStandard() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditScopeReportRequest) GetReportFormat 
    
    
    func (x *GenerateAuditScopeReportRequest) GetReportFormat() GenerateAuditScopeReportRequest_AuditScopeReportFormat

### func (*GenerateAuditScopeReportRequest) GetScope 
    
    
    func (x *GenerateAuditScopeReportRequest) GetScope() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAuditScopeReportRequest) ProtoMessage 
    
    
    func (*GenerateAuditScopeReportRequest) ProtoMessage()

### func (*GenerateAuditScopeReportRequest) ProtoReflect 
    
    
    func (x *GenerateAuditScopeReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateAuditScopeReportRequest) Reset 
    
    
    func (x *GenerateAuditScopeReportRequest) Reset()

### func (*GenerateAuditScopeReportRequest) String 
    
    
    func (x *GenerateAuditScopeReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateAuditScopeReportRequest_AuditScopeReportFormat
    
    
    type GenerateAuditScopeReportRequest_AuditScopeReportFormat [int32](https://pkg.go.dev/builtin#int32)

The options for the audit scope report format.

### GenerateAuditScopeReportRequest_AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED, GenerateAuditScopeReportRequest_AUDIT_SCOPE_REPORT_FORMAT_ODF
    
    
    const (
    	// Unspecified. Invalid format.
    	GenerateAuditScopeReportRequest_AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED GenerateAuditScopeReportRequest_AuditScopeReportFormat = 0
    	// Audit Scope Report creation format is Open Document.
    	GenerateAuditScopeReportRequest_AUDIT_SCOPE_REPORT_FORMAT_ODF GenerateAuditScopeReportRequest_AuditScopeReportFormat = 1
    )

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Descriptor 
    
    
    func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Enum 
    
    
    func (x GenerateAuditScopeReportRequest_AuditScopeReportFormat) Enum() *GenerateAuditScopeReportRequest_AuditScopeReportFormat

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) EnumDescriptor 
    
    
    func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAuditScopeReportRequest_AuditScopeReportFormat.Descriptor instead.

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Number 
    
    
    func (x GenerateAuditScopeReportRequest_AuditScopeReportFormat) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) String 
    
    
    func (x GenerateAuditScopeReportRequest_AuditScopeReportFormat) String() [string](https://pkg.go.dev/builtin#string)

### func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Type 
    
    
    func (GenerateAuditScopeReportRequest_AuditScopeReportFormat) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GetAuditReportRequest
    
    
    type GetAuditReportRequest struct {
    
    	// Required. Format
    	// projects/{project}/locations/{location}/auditReports/{audit_report},
    	// folders/{folder}/locations/{location}/auditReports/{audit_report}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting the overall audit report for an audit report name.

### func (*GetAuditReportRequest) Descriptor 
    
    
    func (*GetAuditReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAuditReportRequest.ProtoReflect.Descriptor instead.

### func (*GetAuditReportRequest) GetName 
    
    
    func (x *GetAuditReportRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAuditReportRequest) ProtoMessage 
    
    
    func (*GetAuditReportRequest) ProtoMessage()

### func (*GetAuditReportRequest) ProtoReflect 
    
    
    func (x *GetAuditReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAuditReportRequest) Reset 
    
    
    func (x *GetAuditReportRequest) Reset()

### func (*GetAuditReportRequest) String 
    
    
    func (x *GetAuditReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetResourceEnrollmentStatusRequest
    
    
    type GetResourceEnrollmentStatusRequest struct {
    
    	// Required. Format
    	// folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status},
    	// projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status},
    	// organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting the enrollment status of a resource.

### func (*GetResourceEnrollmentStatusRequest) Descriptor 
    
    
    func (*GetResourceEnrollmentStatusRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetResourceEnrollmentStatusRequest.ProtoReflect.Descriptor instead.

### func (*GetResourceEnrollmentStatusRequest) GetName 
    
    
    func (x *GetResourceEnrollmentStatusRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetResourceEnrollmentStatusRequest) ProtoMessage 
    
    
    func (*GetResourceEnrollmentStatusRequest) ProtoMessage()

### func (*GetResourceEnrollmentStatusRequest) ProtoReflect 
    
    
    func (x *GetResourceEnrollmentStatusRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetResourceEnrollmentStatusRequest) Reset 
    
    
    func (x *GetResourceEnrollmentStatusRequest) Reset()

### func (*GetResourceEnrollmentStatusRequest) String 
    
    
    func (x *GetResourceEnrollmentStatusRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAuditReportsRequest
    
    
    type ListAuditReportsRequest struct {
    
    	// Required. The parent scope for which to list the reports.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of resources to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The next_page_token value returned from a previous List request,
    	// if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting to list the audit reports.

### func (*ListAuditReportsRequest) Descriptor 
    
    
    func (*ListAuditReportsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAuditReportsRequest.ProtoReflect.Descriptor instead.

### func (*ListAuditReportsRequest) GetPageSize 
    
    
    func (x *ListAuditReportsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAuditReportsRequest) GetPageToken 
    
    
    func (x *ListAuditReportsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAuditReportsRequest) GetParent 
    
    
    func (x *ListAuditReportsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAuditReportsRequest) ProtoMessage 
    
    
    func (*ListAuditReportsRequest) ProtoMessage()

### func (*ListAuditReportsRequest) ProtoReflect 
    
    
    func (x *ListAuditReportsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAuditReportsRequest) Reset 
    
    
    func (x *ListAuditReportsRequest) Reset()

### func (*ListAuditReportsRequest) String 
    
    
    func (x *ListAuditReportsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAuditReportsResponse
    
    
    type ListAuditReportsResponse struct {
    
    	// Output only. The audit reports.
    	AuditReports []*AuditReport `protobuf:"bytes,1,rep,name=audit_reports,json=auditReports,proto3" json:"audit_reports,omitempty"`
    	// Output only. The token to retrieve the next page of results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message with all the audit reports.

### func (*ListAuditReportsResponse) Descriptor 
    
    
    func (*ListAuditReportsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAuditReportsResponse.ProtoReflect.Descriptor instead.

### func (*ListAuditReportsResponse) GetAuditReports 
    
    
    func (x *ListAuditReportsResponse) GetAuditReports() []*AuditReport

### func (*ListAuditReportsResponse) GetNextPageToken 
    
    
    func (x *ListAuditReportsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAuditReportsResponse) ProtoMessage 
    
    
    func (*ListAuditReportsResponse) ProtoMessage()

### func (*ListAuditReportsResponse) ProtoReflect 
    
    
    func (x *ListAuditReportsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAuditReportsResponse) Reset 
    
    
    func (x *ListAuditReportsResponse) Reset()

### func (*ListAuditReportsResponse) String 
    
    
    func (x *ListAuditReportsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListControlsRequest
    
    
    type ListControlsRequest struct {
    
    	// Required. Format
    	// projects/{project}/locations/{location}/standards/{standard},
    	// folders/{folder}/locations/{location}/standards/{standard}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of resources to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The next_page_token value returned from a previous List request,
    	// if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting all the controls for a compliance standard.

### func (*ListControlsRequest) Descriptor 
    
    
    func (*ListControlsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListControlsRequest.ProtoReflect.Descriptor instead.

### func (*ListControlsRequest) GetPageSize 
    
    
    func (x *ListControlsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListControlsRequest) GetPageToken 
    
    
    func (x *ListControlsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListControlsRequest) GetParent 
    
    
    func (x *ListControlsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListControlsRequest) ProtoMessage 
    
    
    func (*ListControlsRequest) ProtoMessage()

### func (*ListControlsRequest) ProtoReflect 
    
    
    func (x *ListControlsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListControlsRequest) Reset 
    
    
    func (x *ListControlsRequest) Reset()

### func (*ListControlsRequest) String 
    
    
    func (x *ListControlsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListControlsResponse
    
    
    type ListControlsResponse struct {
    
    	// Output only. The controls for the compliance standard.
    	Controls []*Control `protobuf:"bytes,1,rep,name=controls,proto3" json:"controls,omitempty"`
    	// Output only. The token to retrieve the next page of results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message with all the controls for a compliance standard.

### func (*ListControlsResponse) Descriptor 
    
    
    func (*ListControlsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListControlsResponse.ProtoReflect.Descriptor instead.

### func (*ListControlsResponse) GetControls 
    
    
    func (x *ListControlsResponse) GetControls() []*Control

### func (*ListControlsResponse) GetNextPageToken 
    
    
    func (x *ListControlsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListControlsResponse) ProtoMessage 
    
    
    func (*ListControlsResponse) ProtoMessage()

### func (*ListControlsResponse) ProtoReflect 
    
    
    func (x *ListControlsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListControlsResponse) Reset 
    
    
    func (x *ListControlsResponse) Reset()

### func (*ListControlsResponse) String 
    
    
    func (x *ListControlsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListResourceEnrollmentStatusesRequest
    
    
    type ListResourceEnrollmentStatusesRequest struct {
    
    	// Required. The parent scope for which the list of resources with enrollments
    	// are required.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of resources to return.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The next_page_token value returned from a previous List request,
    	// if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message for listing all the descendent resources under parent with enrollment.

### func (*ListResourceEnrollmentStatusesRequest) Descriptor 
    
    
    func (*ListResourceEnrollmentStatusesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListResourceEnrollmentStatusesRequest.ProtoReflect.Descriptor instead.

### func (*ListResourceEnrollmentStatusesRequest) GetPageSize 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListResourceEnrollmentStatusesRequest) GetPageToken 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceEnrollmentStatusesRequest) GetParent 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceEnrollmentStatusesRequest) ProtoMessage 
    
    
    func (*ListResourceEnrollmentStatusesRequest) ProtoMessage()

### func (*ListResourceEnrollmentStatusesRequest) ProtoReflect 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListResourceEnrollmentStatusesRequest) Reset 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) Reset()

### func (*ListResourceEnrollmentStatusesRequest) String 
    
    
    func (x *ListResourceEnrollmentStatusesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListResourceEnrollmentStatusesResponse
    
    
    type ListResourceEnrollmentStatusesResponse struct {
    
    	// The resources with their enrollment status.
    	ResourceEnrollmentStatuses []*ResourceEnrollmentStatus `protobuf:"bytes,1,rep,name=resource_enrollment_statuses,json=resourceEnrollmentStatuses,proto3" json:"resource_enrollment_statuses,omitempty"`
    	// Output only. The token to retrieve the next page of results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message with all the descendent resources with enrollment.

### func (*ListResourceEnrollmentStatusesResponse) Descriptor 
    
    
    func (*ListResourceEnrollmentStatusesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListResourceEnrollmentStatusesResponse.ProtoReflect.Descriptor instead.

### func (*ListResourceEnrollmentStatusesResponse) GetNextPageToken 
    
    
    func (x *ListResourceEnrollmentStatusesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListResourceEnrollmentStatusesResponse) GetResourceEnrollmentStatuses 
    
    
    func (x *ListResourceEnrollmentStatusesResponse) GetResourceEnrollmentStatuses() []*ResourceEnrollmentStatus

### func (*ListResourceEnrollmentStatusesResponse) ProtoMessage 
    
    
    func (*ListResourceEnrollmentStatusesResponse) ProtoMessage()

### func (*ListResourceEnrollmentStatusesResponse) ProtoReflect 
    
    
    func (x *ListResourceEnrollmentStatusesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListResourceEnrollmentStatusesResponse) Reset 
    
    
    func (x *ListResourceEnrollmentStatusesResponse) Reset()

### func (*ListResourceEnrollmentStatusesResponse) String 
    
    
    func (x *ListResourceEnrollmentStatusesResponse) String() [string](https://pkg.go.dev/builtin#string)

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
    	// have [Operation.error][] value with a
    	// [google.rpc.Status.code][google.rpc.Status.code] of 1, corresponding to
    	// `Code.CANCELLED`.
    	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=requested_cancellation,json=requestedCancellation,proto3" json:"requested_cancellation,omitempty"`
    	// Output only. API version used to start the operation.
    	ApiVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=api_version,json=apiVersion,proto3" json:"api_version,omitempty"`
    	// contains filtered or unexported fields
    }

The metadata of the long-running operation.

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

## OperationState
    
    
    type OperationState [int32](https://pkg.go.dev/builtin#int32)

The different execution states of the Audit Manager service.

### OperationState_OPERATION_STATE_UNSPECIFIED, OperationState_OPERATION_STATE_NOT_STARTED, OperationState_OPERATION_STATE_EVALUATION_IN_PROGRESS, OperationState_OPERATION_STATE_EVALUATION_DONE, OperationState_OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS, OperationState_OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE, OperationState_OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS, OperationState_OPERATION_STATE_DONE, OperationState_OPERATION_STATE_FAILED
    
    
    const (
    	// Unspecified. Invalid state.
    	OperationState_OPERATION_STATE_UNSPECIFIED OperationState = 0
    	// Audit report generation process has not started.
    	OperationState_OPERATION_STATE_NOT_STARTED OperationState = 10
    	// Audit Manager is currently evaluating the workloads against specific
    	// standard.
    	OperationState_OPERATION_STATE_EVALUATION_IN_PROGRESS OperationState = 20
    	// Audit Manager has completed Evaluation for the workload.
    	OperationState_OPERATION_STATE_EVALUATION_DONE OperationState = 21
    	// Audit Manager is creating audit report from the evaluated data.
    	OperationState_OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS OperationState = 30
    	// Audit Manager has completed generation of the audit report.
    	OperationState_OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE OperationState = 31
    	// Audit Manager is uploading the audit report and evidences to the customer
    	// provided destination.
    	OperationState_OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS OperationState = 40
    	// Audit report generation process is completed.
    	OperationState_OPERATION_STATE_DONE OperationState = 50
    	// Audit report generation process has failed.
    	OperationState_OPERATION_STATE_FAILED OperationState = 60
    )

### func (OperationState) Descriptor 
    
    
    func (OperationState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OperationState) Enum 
    
    
    func (x OperationState) Enum() *OperationState

### func (OperationState) EnumDescriptor 
    
    
    func (OperationState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OperationState.Descriptor instead.

### func (OperationState) Number 
    
    
    func (x OperationState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OperationState) String 
    
    
    func (x OperationState) String() [string](https://pkg.go.dev/builtin#string)

### func (OperationState) Type 
    
    
    func (OperationState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ReportGenerationProgress
    
    
    type ReportGenerationProgress struct {
    
    	// Output only. The current state of execution for report generation.
    	State OperationState `protobuf:"varint,1,opt,name=state,proto3,enum=google.cloud.auditmanager.v1.OperationState" json:"state,omitempty"`
    	// Output only. States the reason of failure during the audit report
    	// generation process. This field is set only if the state attribute is
    	// OPERATION_STATE_FAILED.
    	FailureReason [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=failure_reason,json=failureReason,proto3" json:"failure_reason,omitempty"`
    	// Shows the progress of the CESS service evaluation process. The progress is
    	// defined in terms of percentage complete and is being fetched from the CESS
    	// service.
    	EvaluationPercentComplete [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,20,opt,name=evaluation_percent_complete,json=evaluationPercentComplete,proto3" json:"evaluation_percent_complete,omitempty"`
    	// Shows the report generation progress of the CESS Result Processor Service.
    	// The // progress is defined in terms of percentage complete and is being
    	// fetched from the CESS service. If report_generation_in_progress is non zero
    	// then evaluation_percent_complete will be 100%.
    	ReportGenerationPercentComplete [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,30,opt,name=report_generation_percent_complete,json=reportGenerationPercentComplete,proto3" json:"report_generation_percent_complete,omitempty"`
    	// Shows the report uploading progress of the CESS Result Processor Service.
    	// The progress is defined in terms of percentage complete and is being
    	// fetched from the CESS service. If report_uploading_in_progress is non zero
    	// then evaluation_percent_complete and report_generation_percent_complete
    	// will be 100%.
    	ReportUploadingPercentComplete [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,40,opt,name=report_uploading_percent_complete,json=reportUploadingPercentComplete,proto3" json:"report_uploading_percent_complete,omitempty"`
    	// Output only. The Cloud Storage bucket where the audit report will be
    	// uploaded once the evaluation process is completed.
    	DestinationGcsBucket [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,50,opt,name=destination_gcs_bucket,json=destinationGcsBucket,proto3" json:"destination_gcs_bucket,omitempty"`
    	// Output only. The name of the audit report.
    	AuditReport [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,51,opt,name=audit_report,json=auditReport,proto3" json:"audit_report,omitempty"`
    	// contains filtered or unexported fields
    }

The `ReportGenerationProgress` is part of [google.longrunning.Operation][google.longrunning.Operation] returned to the client for every `GetOperation` request.

### func (*ReportGenerationProgress) Descriptor 
    
    
    func (*ReportGenerationProgress) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportGenerationProgress.ProtoReflect.Descriptor instead.

### func (*ReportGenerationProgress) GetAuditReport 
    
    
    func (x *ReportGenerationProgress) GetAuditReport() [string](https://pkg.go.dev/builtin#string)

### func (*ReportGenerationProgress) GetDestinationGcsBucket 
    
    
    func (x *ReportGenerationProgress) GetDestinationGcsBucket() [string](https://pkg.go.dev/builtin#string)

### func (*ReportGenerationProgress) GetEvaluationPercentComplete 
    
    
    func (x *ReportGenerationProgress) GetEvaluationPercentComplete() [float64](https://pkg.go.dev/builtin#float64)

### func (*ReportGenerationProgress) GetFailureReason 
    
    
    func (x *ReportGenerationProgress) GetFailureReason() [string](https://pkg.go.dev/builtin#string)

### func (*ReportGenerationProgress) GetReportGenerationPercentComplete 
    
    
    func (x *ReportGenerationProgress) GetReportGenerationPercentComplete() [float64](https://pkg.go.dev/builtin#float64)

### func (*ReportGenerationProgress) GetReportUploadingPercentComplete 
    
    
    func (x *ReportGenerationProgress) GetReportUploadingPercentComplete() [float64](https://pkg.go.dev/builtin#float64)

### func (*ReportGenerationProgress) GetState 
    
    
    func (x *ReportGenerationProgress) GetState() OperationState

### func (*ReportGenerationProgress) ProtoMessage 
    
    
    func (*ReportGenerationProgress) ProtoMessage()

### func (*ReportGenerationProgress) ProtoReflect 
    
    
    func (x *ReportGenerationProgress) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportGenerationProgress) Reset 
    
    
    func (x *ReportGenerationProgress) Reset()

### func (*ReportGenerationProgress) String 
    
    
    func (x *ReportGenerationProgress) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary
    
    
    type ReportSummary struct {
    
    	// Total number of checks.
    	TotalCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
    	// Number of compliant checks.
    	CompliantCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=compliant_count,json=compliantCount,proto3" json:"compliant_count,omitempty"`
    	// Number of checks with violations.
    	ViolationCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=violation_count,json=violationCount,proto3" json:"violation_count,omitempty"`
    	// Number of checks with "manual review needed" status.
    	ManualReviewNeededCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=manual_review_needed_count,json=manualReviewNeededCount,proto3" json:"manual_review_needed_count,omitempty"`
    	// Number of checks that could not be performed due to errors.
    	ErrorCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=error_count,json=errorCount,proto3" json:"error_count,omitempty"`
    	// contains filtered or unexported fields
    }

The additional information for an audit operation.

### func (*ReportSummary) Descriptor 
    
    
    func (*ReportSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary.ProtoReflect.Descriptor instead.

### func (*ReportSummary) GetCompliantCount 
    
    
    func (x *ReportSummary) GetCompliantCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ReportSummary) GetErrorCount 
    
    
    func (x *ReportSummary) GetErrorCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ReportSummary) GetManualReviewNeededCount 
    
    
    func (x *ReportSummary) GetManualReviewNeededCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ReportSummary) GetTotalCount 
    
    
    func (x *ReportSummary) GetTotalCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ReportSummary) GetViolationCount 
    
    
    func (x *ReportSummary) GetViolationCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ReportSummary) ProtoMessage 
    
    
    func (*ReportSummary) ProtoMessage()

### func (*ReportSummary) ProtoReflect 
    
    
    func (x *ReportSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary) Reset 
    
    
    func (x *ReportSummary) Reset()

### func (*ReportSummary) String 
    
    
    func (x *ReportSummary) String() [string](https://pkg.go.dev/builtin#string)

## ResourceEnrollmentStatus
    
    
    type ResourceEnrollmentStatus struct {
    
    	// Identifier. The name of this resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Enrollment which contains enrolled destination details for a
    	// resource
    	Enrollment *Enrollment `protobuf:"bytes,2,opt,name=enrollment,proto3" json:"enrollment,omitempty"`
    	// Output only. Is resource enrolled.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/auditmanager/v1/auditmanager.proto.
    	Enrolled [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=enrolled,proto3" json:"enrolled,omitempty"`
    	// Output only. Display name of the project/folder/organization.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. Enrollment state of the resource.
    	EnrollmentState ResourceEnrollmentStatus_ResourceEnrollmentState `protobuf:"varint,5,opt,name=enrollment_state,json=enrollmentState,proto3,enum=google.cloud.auditmanager.v1.ResourceEnrollmentStatus_ResourceEnrollmentState" json:"enrollment_state,omitempty"`
    	// contains filtered or unexported fields
    }

A resource with its enrollment status.

### func (*ResourceEnrollmentStatus) Descriptor 
    
    
    func (*ResourceEnrollmentStatus) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResourceEnrollmentStatus.ProtoReflect.Descriptor instead.

### func (*ResourceEnrollmentStatus) GetDisplayName 
    
    
    func (x *ResourceEnrollmentStatus) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceEnrollmentStatus) GetEnrolled 
    
    
    func (x *ResourceEnrollmentStatus) GetEnrolled() [bool](https://pkg.go.dev/builtin#bool)

Deprecated: Marked as deprecated in google/cloud/auditmanager/v1/auditmanager.proto.

### func (*ResourceEnrollmentStatus) GetEnrollment 
    
    
    func (x *ResourceEnrollmentStatus) GetEnrollment() *Enrollment

### func (*ResourceEnrollmentStatus) GetEnrollmentState 
    
    
    func (x *ResourceEnrollmentStatus) GetEnrollmentState() ResourceEnrollmentStatus_ResourceEnrollmentState

### func (*ResourceEnrollmentStatus) GetName 
    
    
    func (x *ResourceEnrollmentStatus) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ResourceEnrollmentStatus) ProtoMessage 
    
    
    func (*ResourceEnrollmentStatus) ProtoMessage()

### func (*ResourceEnrollmentStatus) ProtoReflect 
    
    
    func (x *ResourceEnrollmentStatus) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ResourceEnrollmentStatus) Reset 
    
    
    func (x *ResourceEnrollmentStatus) Reset()

### func (*ResourceEnrollmentStatus) String 
    
    
    func (x *ResourceEnrollmentStatus) String() [string](https://pkg.go.dev/builtin#string)

## ResourceEnrollmentStatus_ResourceEnrollmentState
    
    
    type ResourceEnrollmentStatus_ResourceEnrollmentState [int32](https://pkg.go.dev/builtin#int32)

The different enrollment states of a resource.

### ResourceEnrollmentStatus_RESOURCE_ENROLLMENT_STATE_UNSPECIFIED, ResourceEnrollmentStatus_NOT_ENROLLED, ResourceEnrollmentStatus_INHERITED, ResourceEnrollmentStatus_ENROLLED
    
    
    const (
    	// Unspecified. Invalid state.
    	ResourceEnrollmentStatus_RESOURCE_ENROLLMENT_STATE_UNSPECIFIED ResourceEnrollmentStatus_ResourceEnrollmentState = 0
    	// Not enrolled.
    	ResourceEnrollmentStatus_NOT_ENROLLED ResourceEnrollmentStatus_ResourceEnrollmentState = 1
    	// Resource is not enrolled but the parent is enrolled.
    	ResourceEnrollmentStatus_INHERITED ResourceEnrollmentStatus_ResourceEnrollmentState = 2
    	// Enrolled.
    	ResourceEnrollmentStatus_ENROLLED ResourceEnrollmentStatus_ResourceEnrollmentState = 3
    )

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) Descriptor 
    
    
    func (ResourceEnrollmentStatus_ResourceEnrollmentState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) Enum 
    
    
    func (x ResourceEnrollmentStatus_ResourceEnrollmentState) Enum() *ResourceEnrollmentStatus_ResourceEnrollmentState

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) EnumDescriptor 
    
    
    func (ResourceEnrollmentStatus_ResourceEnrollmentState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ResourceEnrollmentStatus_ResourceEnrollmentState.Descriptor instead.

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) Number 
    
    
    func (x ResourceEnrollmentStatus_ResourceEnrollmentState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) String 
    
    
    func (x ResourceEnrollmentStatus_ResourceEnrollmentState) String() [string](https://pkg.go.dev/builtin#string)

### func (ResourceEnrollmentStatus_ResourceEnrollmentState) Type 
    
    
    func (ResourceEnrollmentStatus_ResourceEnrollmentState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedAuditManagerServer
    
    
    type UnimplementedAuditManagerServer struct {
    }

UnimplementedAuditManagerServer should be embedded to have forward compatible implementations.

### func (UnimplementedAuditManagerServer) EnrollResource 
    
    
    func (UnimplementedAuditManagerServer) EnrollResource([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *EnrollResourceRequest) (*Enrollment, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) GenerateAuditReport 
    
    
    func (UnimplementedAuditManagerServer) GenerateAuditReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateAuditReportRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) GenerateAuditScopeReport 
    
    
    func (UnimplementedAuditManagerServer) GenerateAuditScopeReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateAuditScopeReportRequest) (*AuditScopeReport, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) GetAuditReport 
    
    
    func (UnimplementedAuditManagerServer) GetAuditReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAuditReportRequest) (*AuditReport, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) GetResourceEnrollmentStatus 
    
    
    func (UnimplementedAuditManagerServer) GetResourceEnrollmentStatus([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetResourceEnrollmentStatusRequest) (*ResourceEnrollmentStatus, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) ListAuditReports 
    
    
    func (UnimplementedAuditManagerServer) ListAuditReports([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAuditReportsRequest) (*ListAuditReportsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) ListControls 
    
    
    func (UnimplementedAuditManagerServer) ListControls([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListControlsRequest) (*ListControlsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedAuditManagerServer) ListResourceEnrollmentStatuses 
    
    
    func (UnimplementedAuditManagerServer) ListResourceEnrollmentStatuses([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListResourceEnrollmentStatusesRequest) (*ListResourceEnrollmentStatusesResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeAuditManagerServer
    
    
    type UnsafeAuditManagerServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAuditManagerServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AuditManagerServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
