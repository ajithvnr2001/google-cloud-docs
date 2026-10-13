---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/policytroubleshooter/latest/apiv1/policytroubleshooterpb/
title: Policy Troubleshooter API v1 - Package cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:05.319425+00:00
---

# Policy Troubleshooter API v1 - Package cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/policytroubleshooter/latest/apiv1/policytroubleshooterpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Policy Troubleshooter API v1 - Package cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.7  1.10.10  1.9.0  1.8.0  1.7.1  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb). 

##  Constants 

### IamChecker_TroubleshootIamPolicy_FullMethodName
    
    
    const (
    	IamChecker_TroubleshootIamPolicy_FullMethodName = "/google.cloud.policytroubleshooter.v1.IamChecker/TroubleshootIamPolicy"
    )

## Variables 

### AccessState_name, AccessState_value
    
    
    var (
    	AccessState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ACCESS_STATE_UNSPECIFIED",
    		1: "GRANTED",
    		2: "NOT_GRANTED",
    		3: "UNKNOWN_CONDITIONAL",
    		4: "UNKNOWN_INFO_DENIED",
    	}
    	AccessState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ACCESS_STATE_UNSPECIFIED": 0,
    		"GRANTED":                  1,
    		"NOT_GRANTED":              2,
    		"UNKNOWN_CONDITIONAL":      3,
    		"UNKNOWN_INFO_DENIED":      4,
    	}
    )

Enum value maps for AccessState.

### HeuristicRelevance_name, HeuristicRelevance_value
    
    
    var (
    	HeuristicRelevance_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HEURISTIC_RELEVANCE_UNSPECIFIED",
    		1: "NORMAL",
    		2: "HIGH",
    	}
    	HeuristicRelevance_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HEURISTIC_RELEVANCE_UNSPECIFIED": 0,
    		"NORMAL":                          1,
    		"HIGH":                            2,
    	}
    )

Enum value maps for HeuristicRelevance.

### BindingExplanation_RolePermission_name, BindingExplanation_RolePermission_value
    
    
    var (
    	BindingExplanation_RolePermission_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ROLE_PERMISSION_UNSPECIFIED",
    		1: "ROLE_PERMISSION_INCLUDED",
    		2: "ROLE_PERMISSION_NOT_INCLUDED",
    		3: "ROLE_PERMISSION_UNKNOWN_INFO_DENIED",
    	}
    	BindingExplanation_RolePermission_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ROLE_PERMISSION_UNSPECIFIED":         0,
    		"ROLE_PERMISSION_INCLUDED":            1,
    		"ROLE_PERMISSION_NOT_INCLUDED":        2,
    		"ROLE_PERMISSION_UNKNOWN_INFO_DENIED": 3,
    	}
    )

Enum value maps for BindingExplanation_RolePermission.

### BindingExplanation_Membership_name, BindingExplanation_Membership_value
    
    
    var (
    	BindingExplanation_Membership_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MEMBERSHIP_UNSPECIFIED",
    		1: "MEMBERSHIP_INCLUDED",
    		2: "MEMBERSHIP_NOT_INCLUDED",
    		3: "MEMBERSHIP_UNKNOWN_INFO_DENIED",
    		4: "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    	}
    	BindingExplanation_Membership_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MEMBERSHIP_UNSPECIFIED":         0,
    		"MEMBERSHIP_INCLUDED":            1,
    		"MEMBERSHIP_NOT_INCLUDED":        2,
    		"MEMBERSHIP_UNKNOWN_INFO_DENIED": 3,
    		"MEMBERSHIP_UNKNOWN_UNSUPPORTED": 4,
    	}
    )

Enum value maps for BindingExplanation_Membership.

### File_google_cloud_policytroubleshooter_v1_checker_proto
    
    
    var File_google_cloud_policytroubleshooter_v1_checker_proto protoreflect.FileDescriptor

### File_google_cloud_policytroubleshooter_v1_explanations_proto
    
    
    var File_google_cloud_policytroubleshooter_v1_explanations_proto protoreflect.FileDescriptor

### IamChecker_ServiceDesc
    
    
    var IamChecker_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.policytroubleshooter.v1.IamChecker",
    	HandlerType: (*IamCheckerServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "TroubleshootIamPolicy",
    			Handler:    _IamChecker_TroubleshootIamPolicy_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/policytroubleshooter/v1/checker.proto",
    }

IamChecker_ServiceDesc is the grpc.ServiceDesc for IamChecker service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterIamCheckerServer 
    
    
    func RegisterIamCheckerServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv IamCheckerServer)

## AccessState
    
    
    type AccessState [int32](https://pkg.go.dev/builtin#int32)

Whether a principal has a permission for a resource.

### AccessState_ACCESS_STATE_UNSPECIFIED, AccessState_GRANTED, AccessState_NOT_GRANTED, AccessState_UNKNOWN_CONDITIONAL, AccessState_UNKNOWN_INFO_DENIED
    
    
    const (
    	// Default value. This value is unused.
    	AccessState_ACCESS_STATE_UNSPECIFIED AccessState = 0
    	// The principal has the permission.
    	AccessState_GRANTED AccessState = 1
    	// The principal does not have the permission.
    	AccessState_NOT_GRANTED AccessState = 2
    	// The principal has the permission only if a condition expression evaluates
    	// to `true`.
    	AccessState_UNKNOWN_CONDITIONAL AccessState = 3
    	// The sender of the request does not have access to all of the policies that
    	// Policy Troubleshooter needs to evaluate.
    	AccessState_UNKNOWN_INFO_DENIED AccessState = 4
    )

### func (AccessState) Descriptor 
    
    
    func (AccessState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AccessState) Enum 
    
    
    func (x AccessState) Enum() *AccessState

### func (AccessState) EnumDescriptor 
    
    
    func (AccessState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccessState.Descriptor instead.

### func (AccessState) Number 
    
    
    func (x AccessState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AccessState) String 
    
    
    func (x AccessState) String() [string](https://pkg.go.dev/builtin#string)

### func (AccessState) Type 
    
    
    func (AccessState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AccessTuple
    
    
    type AccessTuple struct {
    
    	// Required. The principal whose access you want to check, in the form of
    	// the email address that represents that principal. For example,
    	// `alice@example.com` or
    	// `my-service-account@my-project.iam.gserviceaccount.com`.
    	//
    	// The principal must be a Google Account or a service account. Other types of
    	// principals are not supported.
    	Principal [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=principal,proto3" json:"principal,omitempty"`
    	// Required. The full resource name that identifies the resource. For example,
    	// `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.
    	//
    	// For examples of full resource names for Google Cloud services, see
    	// https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
    	FullResourceName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=full_resource_name,json=fullResourceName,proto3" json:"full_resource_name,omitempty"`
    	// Required. The IAM permission to check for the specified principal and
    	// resource.
    	//
    	// For a complete list of IAM permissions, see
    	// https://cloud.google.com/iam/help/permissions/reference.
    	//
    	// For a complete list of predefined IAM roles and the permissions in each
    	// role, see https://cloud.google.com/iam/help/roles/reference.
    	Permission [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=permission,proto3" json:"permission,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the principal, resource, and permission to check.

### func (*AccessTuple) Descriptor 
    
    
    func (*AccessTuple) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccessTuple.ProtoReflect.Descriptor instead.

### func (*AccessTuple) GetFullResourceName 
    
    
    func (x *AccessTuple) GetFullResourceName() [string](https://pkg.go.dev/builtin#string)

### func (*AccessTuple) GetPermission 
    
    
    func (x *AccessTuple) GetPermission() [string](https://pkg.go.dev/builtin#string)

### func (*AccessTuple) GetPrincipal 
    
    
    func (x *AccessTuple) GetPrincipal() [string](https://pkg.go.dev/builtin#string)

### func (*AccessTuple) ProtoMessage 
    
    
    func (*AccessTuple) ProtoMessage()

### func (*AccessTuple) ProtoReflect 
    
    
    func (x *AccessTuple) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccessTuple) Reset 
    
    
    func (x *AccessTuple) Reset()

### func (*AccessTuple) String 
    
    
    func (x *AccessTuple) String() [string](https://pkg.go.dev/builtin#string)

## BindingExplanation
    
    
    type BindingExplanation struct {
    
    	// Required. Indicates whether _this binding_ provides the specified
    	// permission to the specified principal for the specified resource.
    	//
    	// This field does _not_ indicate whether the principal actually has the
    	// permission for the resource. There might be another binding that overrides
    	// this binding. To determine whether the principal actually has the
    	// permission, use the `access` field in the
    	// [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].
    	Access AccessState `protobuf:"varint,1,opt,name=access,proto3,enum=google.cloud.policytroubleshooter.v1.AccessState" json:"access,omitempty"`
    	// The role that this binding grants. For example,
    	// `roles/compute.serviceAgent`.
    	//
    	// For a complete list of predefined IAM roles, as well as the permissions in
    	// each role, see https://cloud.google.com/iam/help/roles/reference.
    	Role [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=role,proto3" json:"role,omitempty"`
    	// Indicates whether the role granted by this binding contains the specified
    	// permission.
    	RolePermission BindingExplanation_RolePermission `protobuf:"varint,3,opt,name=role_permission,json=rolePermission,proto3,enum=google.cloud.policytroubleshooter.v1.BindingExplanation_RolePermission" json:"role_permission,omitempty"`
    	// The relevance of the permission's existence, or nonexistence, in the role
    	// to the overall determination for the entire policy.
    	RolePermissionRelevance HeuristicRelevance `protobuf:"varint,4,opt,name=role_permission_relevance,json=rolePermissionRelevance,proto3,enum=google.cloud.policytroubleshooter.v1.HeuristicRelevance" json:"role_permission_relevance,omitempty"`
    	// Indicates whether each principal in the binding includes the principal
    	// specified in the request, either directly or indirectly. Each key
    	// identifies a principal in the binding, and each value indicates whether the
    	// principal in the binding includes the principal in the request.
    	//
    	// For example, suppose that a binding includes the following principals:
    	//
    	// * `user:alice@example.com`
    	// * `group:product-eng@example.com`
    	//
    	// You want to troubleshoot access for `user:bob@example.com`. This user is a
    	// principal of the group `group:product-eng@example.com`.
    	//
    	// For the first principal in the binding, the key is
    	// `user:alice@example.com`, and the `membership` field in the value is set to
    	// `MEMBERSHIP_NOT_INCLUDED`.
    	//
    	// For the second principal in the binding, the key is
    	// `group:product-eng@example.com`, and the `membership` field in the value is
    	// set to `MEMBERSHIP_INCLUDED`.
    	Memberships map[[string](https://pkg.go.dev/builtin#string)]*BindingExplanation_AnnotatedMembership `protobuf:"bytes,5,rep,name=memberships,proto3" json:"memberships,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// The relevance of this binding to the overall determination for the entire
    	// policy.
    	Relevance HeuristicRelevance `protobuf:"varint,6,opt,name=relevance,proto3,enum=google.cloud.policytroubleshooter.v1.HeuristicRelevance" json:"relevance,omitempty"`
    	// A condition expression that prevents this binding from granting access
    	// unless the expression evaluates to `true`.
    	//
    	// To learn about IAM Conditions, see
    	// https://cloud.google.com/iam/help/conditions/overview.
    	Condition *expr.Expr `protobuf:"bytes,7,opt,name=condition,proto3" json:"condition,omitempty"`
    	// contains filtered or unexported fields
    }

Details about how a binding in a policy affects a principal's ability to use a permission.

### func (*BindingExplanation) Descriptor 
    
    
    func (*BindingExplanation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BindingExplanation.ProtoReflect.Descriptor instead.

### func (*BindingExplanation) GetAccess 
    
    
    func (x *BindingExplanation) GetAccess() AccessState

### func (*BindingExplanation) GetCondition 
    
    
    func (x *BindingExplanation) GetCondition() *[expr](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/expr).[Expr](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/expr#Expr)

### func (*BindingExplanation) GetMemberships 
    
    
    func (x *BindingExplanation) GetMemberships() map[[string](https://pkg.go.dev/builtin#string)]*BindingExplanation_AnnotatedMembership

### func (*BindingExplanation) GetRelevance 
    
    
    func (x *BindingExplanation) GetRelevance() HeuristicRelevance

### func (*BindingExplanation) GetRole 
    
    
    func (x *BindingExplanation) GetRole() [string](https://pkg.go.dev/builtin#string)

### func (*BindingExplanation) GetRolePermission 
    
    
    func (x *BindingExplanation) GetRolePermission() BindingExplanation_RolePermission

### func (*BindingExplanation) GetRolePermissionRelevance 
    
    
    func (x *BindingExplanation) GetRolePermissionRelevance() HeuristicRelevance

### func (*BindingExplanation) ProtoMessage 
    
    
    func (*BindingExplanation) ProtoMessage()

### func (*BindingExplanation) ProtoReflect 
    
    
    func (x *BindingExplanation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BindingExplanation) Reset 
    
    
    func (x *BindingExplanation) Reset()

### func (*BindingExplanation) String 
    
    
    func (x *BindingExplanation) String() [string](https://pkg.go.dev/builtin#string)

## BindingExplanation_AnnotatedMembership
    
    
    type BindingExplanation_AnnotatedMembership struct {
    
    	// Indicates whether the binding includes the principal.
    	Membership BindingExplanation_Membership `protobuf:"varint,1,opt,name=membership,proto3,enum=google.cloud.policytroubleshooter.v1.BindingExplanation_Membership" json:"membership,omitempty"`
    	// The relevance of the principal's status to the overall determination for
    	// the binding.
    	Relevance HeuristicRelevance `protobuf:"varint,2,opt,name=relevance,proto3,enum=google.cloud.policytroubleshooter.v1.HeuristicRelevance" json:"relevance,omitempty"`
    	// contains filtered or unexported fields
    }

Details about whether the binding includes the principal.

### func (*BindingExplanation_AnnotatedMembership) Descriptor 
    
    
    func (*BindingExplanation_AnnotatedMembership) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BindingExplanation_AnnotatedMembership.ProtoReflect.Descriptor instead.

### func (*BindingExplanation_AnnotatedMembership) GetMembership 
    
    
    func (x *BindingExplanation_AnnotatedMembership) GetMembership() BindingExplanation_Membership

### func (*BindingExplanation_AnnotatedMembership) GetRelevance 
    
    
    func (x *BindingExplanation_AnnotatedMembership) GetRelevance() HeuristicRelevance

### func (*BindingExplanation_AnnotatedMembership) ProtoMessage 
    
    
    func (*BindingExplanation_AnnotatedMembership) ProtoMessage()

### func (*BindingExplanation_AnnotatedMembership) ProtoReflect 
    
    
    func (x *BindingExplanation_AnnotatedMembership) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BindingExplanation_AnnotatedMembership) Reset 
    
    
    func (x *BindingExplanation_AnnotatedMembership) Reset()

### func (*BindingExplanation_AnnotatedMembership) String 
    
    
    func (x *BindingExplanation_AnnotatedMembership) String() [string](https://pkg.go.dev/builtin#string)

## BindingExplanation_Membership
    
    
    type BindingExplanation_Membership [int32](https://pkg.go.dev/builtin#int32)

Whether the binding includes the principal.

### BindingExplanation_MEMBERSHIP_UNSPECIFIED, BindingExplanation_MEMBERSHIP_INCLUDED, BindingExplanation_MEMBERSHIP_NOT_INCLUDED, BindingExplanation_MEMBERSHIP_UNKNOWN_INFO_DENIED, BindingExplanation_MEMBERSHIP_UNKNOWN_UNSUPPORTED
    
    
    const (
    	// Default value. This value is unused.
    	BindingExplanation_MEMBERSHIP_UNSPECIFIED BindingExplanation_Membership = 0
    	// The binding includes the principal. The principal can be included
    	// directly or indirectly. For example:
    	//
    	//   - A principal is included directly if that principal is listed in the
    	//     binding.
    	//   - A principal is included indirectly if that principal is in a Google
    	//     group or Google Workspace domain that is listed in the binding.
    	BindingExplanation_MEMBERSHIP_INCLUDED BindingExplanation_Membership = 1
    	// The binding does not include the principal.
    	BindingExplanation_MEMBERSHIP_NOT_INCLUDED BindingExplanation_Membership = 2
    	// The sender of the request is not allowed to access the binding.
    	BindingExplanation_MEMBERSHIP_UNKNOWN_INFO_DENIED BindingExplanation_Membership = 3
    	// The principal is an unsupported type. Only Google Accounts and service
    	// accounts are supported.
    	BindingExplanation_MEMBERSHIP_UNKNOWN_UNSUPPORTED BindingExplanation_Membership = 4
    )

### func (BindingExplanation_Membership) Descriptor 
    
    
    func (BindingExplanation_Membership) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (BindingExplanation_Membership) Enum 
    
    
    func (x BindingExplanation_Membership) Enum() *BindingExplanation_Membership

### func (BindingExplanation_Membership) EnumDescriptor 
    
    
    func (BindingExplanation_Membership) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BindingExplanation_Membership.Descriptor instead.

### func (BindingExplanation_Membership) Number 
    
    
    func (x BindingExplanation_Membership) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (BindingExplanation_Membership) String 
    
    
    func (x BindingExplanation_Membership) String() [string](https://pkg.go.dev/builtin#string)

### func (BindingExplanation_Membership) Type 
    
    
    func (BindingExplanation_Membership) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## BindingExplanation_RolePermission
    
    
    type BindingExplanation_RolePermission [int32](https://pkg.go.dev/builtin#int32)

Whether a role includes a specific permission.

### BindingExplanation_ROLE_PERMISSION_UNSPECIFIED, BindingExplanation_ROLE_PERMISSION_INCLUDED, BindingExplanation_ROLE_PERMISSION_NOT_INCLUDED, BindingExplanation_ROLE_PERMISSION_UNKNOWN_INFO_DENIED
    
    
    const (
    	// Default value. This value is unused.
    	BindingExplanation_ROLE_PERMISSION_UNSPECIFIED BindingExplanation_RolePermission = 0
    	// The permission is included in the role.
    	BindingExplanation_ROLE_PERMISSION_INCLUDED BindingExplanation_RolePermission = 1
    	// The permission is not included in the role.
    	BindingExplanation_ROLE_PERMISSION_NOT_INCLUDED BindingExplanation_RolePermission = 2
    	// The sender of the request is not allowed to access the binding.
    	BindingExplanation_ROLE_PERMISSION_UNKNOWN_INFO_DENIED BindingExplanation_RolePermission = 3
    )

### func (BindingExplanation_RolePermission) Descriptor 
    
    
    func (BindingExplanation_RolePermission) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (BindingExplanation_RolePermission) Enum 
    
    
    func (x BindingExplanation_RolePermission) Enum() *BindingExplanation_RolePermission

### func (BindingExplanation_RolePermission) EnumDescriptor 
    
    
    func (BindingExplanation_RolePermission) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BindingExplanation_RolePermission.Descriptor instead.

### func (BindingExplanation_RolePermission) Number 
    
    
    func (x BindingExplanation_RolePermission) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (BindingExplanation_RolePermission) String 
    
    
    func (x BindingExplanation_RolePermission) String() [string](https://pkg.go.dev/builtin#string)

### func (BindingExplanation_RolePermission) Type 
    
    
    func (BindingExplanation_RolePermission) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ExplainedPolicy
    
    
    type ExplainedPolicy struct {
    
    	// Indicates whether _this policy_ provides the specified permission to the
    	// specified principal for the specified resource.
    	//
    	// This field does _not_ indicate whether the principal actually has the
    	// permission for the resource. There might be another policy that overrides
    	// this policy. To determine whether the principal actually has the
    	// permission, use the `access` field in the
    	// [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].
    	Access AccessState `protobuf:"varint,1,opt,name=access,proto3,enum=google.cloud.policytroubleshooter.v1.AccessState" json:"access,omitempty"`
    	// The full resource name that identifies the resource. For example,
    	// `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.
    	//
    	// If the sender of the request does not have access to the policy, this field
    	// is omitted.
    	//
    	// For examples of full resource names for Google Cloud services, see
    	// https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
    	FullResourceName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=full_resource_name,json=fullResourceName,proto3" json:"full_resource_name,omitempty"`
    	// The IAM policy attached to the resource.
    	//
    	// If the sender of the request does not have access to the policy, this field
    	// is empty.
    	Policy *iampb.Policy `protobuf:"bytes,3,opt,name=policy,proto3" json:"policy,omitempty"`
    	// Details about how each binding in the policy affects the principal's
    	// ability, or inability, to use the permission for the resource.
    	//
    	// If the sender of the request does not have access to the policy, this field
    	// is omitted.
    	BindingExplanations []*BindingExplanation `protobuf:"bytes,4,rep,name=binding_explanations,json=bindingExplanations,proto3" json:"binding_explanations,omitempty"`
    	// The relevance of this policy to the overall determination in the
    	// [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].
    	//
    	// If the sender of the request does not have access to the policy, this field
    	// is omitted.
    	Relevance HeuristicRelevance `protobuf:"varint,5,opt,name=relevance,proto3,enum=google.cloud.policytroubleshooter.v1.HeuristicRelevance" json:"relevance,omitempty"`
    	// contains filtered or unexported fields
    }

Details about how a specific IAM [Policy][google.iam.v1.Policy] contributed to the access check.

### func (*ExplainedPolicy) Descriptor 
    
    
    func (*ExplainedPolicy) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExplainedPolicy.ProtoReflect.Descriptor instead.

### func (*ExplainedPolicy) GetAccess 
    
    
    func (x *ExplainedPolicy) GetAccess() AccessState

### func (*ExplainedPolicy) GetBindingExplanations 
    
    
    func (x *ExplainedPolicy) GetBindingExplanations() []*BindingExplanation

### func (*ExplainedPolicy) GetFullResourceName 
    
    
    func (x *ExplainedPolicy) GetFullResourceName() [string](https://pkg.go.dev/builtin#string)

### func (*ExplainedPolicy) GetPolicy 
    
    
    func (x *ExplainedPolicy) GetPolicy() *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy)

### func (*ExplainedPolicy) GetRelevance 
    
    
    func (x *ExplainedPolicy) GetRelevance() HeuristicRelevance

### func (*ExplainedPolicy) ProtoMessage 
    
    
    func (*ExplainedPolicy) ProtoMessage()

### func (*ExplainedPolicy) ProtoReflect 
    
    
    func (x *ExplainedPolicy) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ExplainedPolicy) Reset 
    
    
    func (x *ExplainedPolicy) Reset()

### func (*ExplainedPolicy) String 
    
    
    func (x *ExplainedPolicy) String() [string](https://pkg.go.dev/builtin#string)

## HeuristicRelevance
    
    
    type HeuristicRelevance [int32](https://pkg.go.dev/builtin#int32)

The extent to which a single data point, such as the existence of a binding or whether a binding includes a specific principal, contributes to an overall determination.

### HeuristicRelevance_HEURISTIC_RELEVANCE_UNSPECIFIED, HeuristicRelevance_NORMAL, HeuristicRelevance_HIGH
    
    
    const (
    	// Default value. This value is unused.
    	HeuristicRelevance_HEURISTIC_RELEVANCE_UNSPECIFIED HeuristicRelevance = 0
    	// The data point has a limited effect on the result. Changing the data point
    	// is unlikely to affect the overall determination.
    	HeuristicRelevance_NORMAL HeuristicRelevance = 1
    	// The data point has a strong effect on the result. Changing the data point
    	// is likely to affect the overall determination.
    	HeuristicRelevance_HIGH HeuristicRelevance = 2
    )

### func (HeuristicRelevance) Descriptor 
    
    
    func (HeuristicRelevance) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (HeuristicRelevance) Enum 
    
    
    func (x HeuristicRelevance) Enum() *HeuristicRelevance

### func (HeuristicRelevance) EnumDescriptor 
    
    
    func (HeuristicRelevance) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HeuristicRelevance.Descriptor instead.

### func (HeuristicRelevance) Number 
    
    
    func (x HeuristicRelevance) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (HeuristicRelevance) String 
    
    
    func (x HeuristicRelevance) String() [string](https://pkg.go.dev/builtin#string)

### func (HeuristicRelevance) Type 
    
    
    func (HeuristicRelevance) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## IamCheckerClient
    
    
    type IamCheckerClient interface {
    	// Checks whether a principal has a specific permission for a specific
    	// resource, and explains why the principal does or does not have that
    	// permission.
    	TroubleshootIamPolicy(ctx context.Context, in *TroubleshootIamPolicyRequest, opts ...grpc.CallOption) (*TroubleshootIamPolicyResponse, [error](https://pkg.go.dev/builtin#error))
    }

IamCheckerClient is the client API for IamChecker service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewIamCheckerClient 
    
    
    func NewIamCheckerClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) IamCheckerClient

## IamCheckerServer
    
    
    type IamCheckerServer interface {
    	// Checks whether a principal has a specific permission for a specific
    	// resource, and explains why the principal does or does not have that
    	// permission.
    	TroubleshootIamPolicy(context.Context, *TroubleshootIamPolicyRequest) (*TroubleshootIamPolicyResponse, [error](https://pkg.go.dev/builtin#error))
    }

IamCheckerServer is the server API for IamChecker service. All implementations should embed UnimplementedIamCheckerServer for forward compatibility

## TroubleshootIamPolicyRequest
    
    
    type TroubleshootIamPolicyRequest struct {
    
    	// The information to use for checking whether a principal has a permission
    	// for a resource.
    	AccessTuple *AccessTuple `protobuf:"bytes,1,opt,name=access_tuple,json=accessTuple,proto3" json:"access_tuple,omitempty"`
    	// contains filtered or unexported fields
    }

Request for [TroubleshootIamPolicy][google.cloud.policytroubleshooter.v1.IamChecker.TroubleshootIamPolicy].

### func (*TroubleshootIamPolicyRequest) Descriptor 
    
    
    func (*TroubleshootIamPolicyRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TroubleshootIamPolicyRequest.ProtoReflect.Descriptor instead.

### func (*TroubleshootIamPolicyRequest) GetAccessTuple 
    
    
    func (x *TroubleshootIamPolicyRequest) GetAccessTuple() *AccessTuple

### func (*TroubleshootIamPolicyRequest) ProtoMessage 
    
    
    func (*TroubleshootIamPolicyRequest) ProtoMessage()

### func (*TroubleshootIamPolicyRequest) ProtoReflect 
    
    
    func (x *TroubleshootIamPolicyRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TroubleshootIamPolicyRequest) Reset 
    
    
    func (x *TroubleshootIamPolicyRequest) Reset()

### func (*TroubleshootIamPolicyRequest) String 
    
    
    func (x *TroubleshootIamPolicyRequest) String() [string](https://pkg.go.dev/builtin#string)

## TroubleshootIamPolicyResponse
    
    
    type TroubleshootIamPolicyResponse struct {
    
    	// Indicates whether the principal has the specified permission for the
    	// specified resource, based on evaluating all of the applicable IAM policies.
    	Access AccessState `protobuf:"varint,1,opt,name=access,proto3,enum=google.cloud.policytroubleshooter.v1.AccessState" json:"access,omitempty"`
    	// List of IAM policies that were evaluated to check the principal's
    	// permissions, with annotations to indicate how each policy contributed to
    	// the final result.
    	//
    	// The list of policies can include the policy for the resource itself. It can
    	// also include policies that are inherited from higher levels of the resource
    	// hierarchy, including the organization, the folder, and the project.
    	//
    	// To learn more about the resource hierarchy, see
    	// https://cloud.google.com/iam/help/resource-hierarchy.
    	ExplainedPolicies []*ExplainedPolicy `protobuf:"bytes,2,rep,name=explained_policies,json=explainedPolicies,proto3" json:"explained_policies,omitempty"`
    	// The general errors contained in the troubleshooting response.
    	Errors []*status.Status `protobuf:"bytes,3,rep,name=errors,proto3" json:"errors,omitempty"`
    	// contains filtered or unexported fields
    }

Response for [TroubleshootIamPolicy][google.cloud.policytroubleshooter.v1.IamChecker.TroubleshootIamPolicy].

### func (*TroubleshootIamPolicyResponse) Descriptor 
    
    
    func (*TroubleshootIamPolicyResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TroubleshootIamPolicyResponse.ProtoReflect.Descriptor instead.

### func (*TroubleshootIamPolicyResponse) GetAccess 
    
    
    func (x *TroubleshootIamPolicyResponse) GetAccess() AccessState

### func (*TroubleshootIamPolicyResponse) GetErrors 
    
    
    func (x *TroubleshootIamPolicyResponse) GetErrors() []*[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*TroubleshootIamPolicyResponse) GetExplainedPolicies 
    
    
    func (x *TroubleshootIamPolicyResponse) GetExplainedPolicies() []*ExplainedPolicy

### func (*TroubleshootIamPolicyResponse) ProtoMessage 
    
    
    func (*TroubleshootIamPolicyResponse) ProtoMessage()

### func (*TroubleshootIamPolicyResponse) ProtoReflect 
    
    
    func (x *TroubleshootIamPolicyResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TroubleshootIamPolicyResponse) Reset 
    
    
    func (x *TroubleshootIamPolicyResponse) Reset()

### func (*TroubleshootIamPolicyResponse) String 
    
    
    func (x *TroubleshootIamPolicyResponse) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedIamCheckerServer
    
    
    type UnimplementedIamCheckerServer struct {
    }

UnimplementedIamCheckerServer should be embedded to have forward compatible implementations.

### func (UnimplementedIamCheckerServer) TroubleshootIamPolicy 
    
    
    func (UnimplementedIamCheckerServer) TroubleshootIamPolicy([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *TroubleshootIamPolicyRequest) (*TroubleshootIamPolicyResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeIamCheckerServer
    
    
    type UnsafeIamCheckerServer interface {
    	// contains filtered or unexported methods
    }

UnsafeIamCheckerServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to IamCheckerServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
