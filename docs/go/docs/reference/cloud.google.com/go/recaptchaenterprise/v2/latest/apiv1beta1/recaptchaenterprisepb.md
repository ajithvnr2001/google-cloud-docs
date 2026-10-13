---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/recaptchaenterprise/v2/latest/apiv1beta1/recaptchaenterprisepb/
title: reCAPTCHA Enterprise API v1beta1 - Package cloud.google.com/go/recaptchaenterprise/v2/apiv1beta1/recaptchaenterprisepb (v2.28.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:47.385912+00:00
---

# reCAPTCHA Enterprise API v1beta1 - Package cloud.google.com/go/recaptchaenterprise/v2/apiv1beta1/recaptchaenterprisepb (v2.28.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/recaptchaenterprise/v2/latest/apiv1beta1/recaptchaenterprisepb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  reCAPTCHA Enterprise API v1beta1 - Package cloud.google.com/go/recaptchaenterprise/v2/apiv1beta1/recaptchaenterprisepb (v2.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.28.0 (latest)  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.5  2.19.4  2.18.0  2.17.3  2.16.0  2.15.0  2.14.3  2.13.1  2.12.0  2.11.1  2.10.0  2.9.2  2.8.4  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/recaptchaenterprise/v2/apiv1beta1/recaptchaenterprisepb). 

##  Constants 

### RecaptchaEnterpriseServiceV1Beta1_CreateAssessment_FullMethodName, RecaptchaEnterpriseServiceV1Beta1_AnnotateAssessment_FullMethodName
    
    
    const (
    	RecaptchaEnterpriseServiceV1Beta1_CreateAssessment_FullMethodName   = "/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/CreateAssessment"
    	RecaptchaEnterpriseServiceV1Beta1_AnnotateAssessment_FullMethodName = "/google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1/AnnotateAssessment"
    )

## Variables 

### TransactionEvent_TransactionEventType_name, TransactionEvent_TransactionEventType_value
    
    
    var (
    	TransactionEvent_TransactionEventType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "TRANSACTION_EVENT_TYPE_UNSPECIFIED",
    		1:  "MERCHANT_APPROVE",
    		2:  "MERCHANT_DENY",
    		3:  "MANUAL_REVIEW",
    		4:  "AUTHORIZATION",
    		5:  "AUTHORIZATION_DECLINE",
    		6:  "PAYMENT_CAPTURE",
    		7:  "PAYMENT_CAPTURE_DECLINE",
    		8:  "CANCEL",
    		9:  "CHARGEBACK_INQUIRY",
    		10: "CHARGEBACK_ALERT",
    		11: "FRAUD_NOTIFICATION",
    		12: "CHARGEBACK",
    		13: "CHARGEBACK_REPRESENTMENT",
    		14: "CHARGEBACK_REVERSE",
    		15: "REFUND_REQUEST",
    		16: "REFUND_DECLINE",
    		17: "REFUND",
    		18: "REFUND_REVERSE",
    	}
    	TransactionEvent_TransactionEventType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TRANSACTION_EVENT_TYPE_UNSPECIFIED": 0,
    		"MERCHANT_APPROVE":                   1,
    		"MERCHANT_DENY":                      2,
    		"MANUAL_REVIEW":                      3,
    		"AUTHORIZATION":                      4,
    		"AUTHORIZATION_DECLINE":              5,
    		"PAYMENT_CAPTURE":                    6,
    		"PAYMENT_CAPTURE_DECLINE":            7,
    		"CANCEL":                             8,
    		"CHARGEBACK_INQUIRY":                 9,
    		"CHARGEBACK_ALERT":                   10,
    		"FRAUD_NOTIFICATION":                 11,
    		"CHARGEBACK":                         12,
    		"CHARGEBACK_REPRESENTMENT":           13,
    		"CHARGEBACK_REVERSE":                 14,
    		"REFUND_REQUEST":                     15,
    		"REFUND_DECLINE":                     16,
    		"REFUND":                             17,
    		"REFUND_REVERSE":                     18,
    	}
    )

Enum value maps for TransactionEvent_TransactionEventType.

### AnnotateAssessmentRequest_Annotation_name, AnnotateAssessmentRequest_Annotation_value
    
    
    var (
    	AnnotateAssessmentRequest_Annotation_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ANNOTATION_UNSPECIFIED",
    		1: "LEGITIMATE",
    		2: "FRAUDULENT",
    		3: "PASSWORD_CORRECT",
    		4: "PASSWORD_INCORRECT",
    	}
    	AnnotateAssessmentRequest_Annotation_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ANNOTATION_UNSPECIFIED": 0,
    		"LEGITIMATE":             1,
    		"FRAUDULENT":             2,
    		"PASSWORD_CORRECT":       3,
    		"PASSWORD_INCORRECT":     4,
    	}
    )

Enum value maps for AnnotateAssessmentRequest_Annotation.

### AnnotateAssessmentRequest_Reason_name, AnnotateAssessmentRequest_Reason_value
    
    
    var (
    	AnnotateAssessmentRequest_Reason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "REASON_UNSPECIFIED",
    		1:  "CHARGEBACK",
    		8:  "CHARGEBACK_FRAUD",
    		9:  "CHARGEBACK_DISPUTE",
    		10: "REFUND",
    		11: "REFUND_FRAUD",
    		12: "TRANSACTION_ACCEPTED",
    		13: "TRANSACTION_DECLINED",
    		2:  "PAYMENT_HEURISTICS",
    		7:  "INITIATED_TWO_FACTOR",
    		3:  "PASSED_TWO_FACTOR",
    		4:  "FAILED_TWO_FACTOR",
    		5:  "CORRECT_PASSWORD",
    		6:  "INCORRECT_PASSWORD",
    		14: "SOCIAL_SPAM",
    	}
    	AnnotateAssessmentRequest_Reason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"REASON_UNSPECIFIED":   0,
    		"CHARGEBACK":           1,
    		"CHARGEBACK_FRAUD":     8,
    		"CHARGEBACK_DISPUTE":   9,
    		"REFUND":               10,
    		"REFUND_FRAUD":         11,
    		"TRANSACTION_ACCEPTED": 12,
    		"TRANSACTION_DECLINED": 13,
    		"PAYMENT_HEURISTICS":   2,
    		"INITIATED_TWO_FACTOR": 7,
    		"PASSED_TWO_FACTOR":    3,
    		"FAILED_TWO_FACTOR":    4,
    		"CORRECT_PASSWORD":     5,
    		"INCORRECT_PASSWORD":   6,
    		"SOCIAL_SPAM":          14,
    	}
    )

Enum value maps for AnnotateAssessmentRequest_Reason.

### Assessment_ClassificationReason_name, Assessment_ClassificationReason_value
    
    
    var (
    	Assessment_ClassificationReason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CLASSIFICATION_REASON_UNSPECIFIED",
    		1: "AUTOMATION",
    		2: "UNEXPECTED_ENVIRONMENT",
    		3: "TOO_MUCH_TRAFFIC",
    		4: "UNEXPECTED_USAGE_PATTERNS",
    		5: "LOW_CONFIDENCE_SCORE",
    		6: "SUSPECTED_CARDING",
    		7: "SUSPECTED_CHARGEBACK",
    	}
    	Assessment_ClassificationReason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CLASSIFICATION_REASON_UNSPECIFIED": 0,
    		"AUTOMATION":                        1,
    		"UNEXPECTED_ENVIRONMENT":            2,
    		"TOO_MUCH_TRAFFIC":                  3,
    		"UNEXPECTED_USAGE_PATTERNS":         4,
    		"LOW_CONFIDENCE_SCORE":              5,
    		"SUSPECTED_CARDING":                 6,
    		"SUSPECTED_CHARGEBACK":              7,
    	}
    )

Enum value maps for Assessment_ClassificationReason.

### Event_FraudPrevention_name, Event_FraudPrevention_value
    
    
    var (
    	Event_FraudPrevention_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "FRAUD_PREVENTION_UNSPECIFIED",
    		1: "ENABLED",
    		2: "DISABLED",
    	}
    	Event_FraudPrevention_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FRAUD_PREVENTION_UNSPECIFIED": 0,
    		"ENABLED":                      1,
    		"DISABLED":                     2,
    	}
    )

Enum value maps for Event_FraudPrevention.

### TokenProperties_InvalidReason_name, TokenProperties_InvalidReason_value
    
    
    var (
    	TokenProperties_InvalidReason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INVALID_REASON_UNSPECIFIED",
    		1: "UNKNOWN_INVALID_REASON",
    		2: "MALFORMED",
    		3: "EXPIRED",
    		4: "DUPE",
    		5: "SITE_MISMATCH",
    		6: "MISSING",
    		7: "BROWSER_ERROR",
    	}
    	TokenProperties_InvalidReason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INVALID_REASON_UNSPECIFIED": 0,
    		"UNKNOWN_INVALID_REASON":     1,
    		"MALFORMED":                  2,
    		"EXPIRED":                    3,
    		"DUPE":                       4,
    		"SITE_MISMATCH":              5,
    		"MISSING":                    6,
    		"BROWSER_ERROR":              7,
    	}
    )

Enum value maps for TokenProperties_InvalidReason.

### AccountDefenderAssessment_AccountDefenderLabel_name, AccountDefenderAssessment_AccountDefenderLabel_value
    
    
    var (
    	AccountDefenderAssessment_AccountDefenderLabel_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ACCOUNT_DEFENDER_LABEL_UNSPECIFIED",
    		1: "PROFILE_MATCH",
    		2: "SUSPICIOUS_LOGIN_ACTIVITY",
    		3: "SUSPICIOUS_ACCOUNT_CREATION",
    		4: "RELATED_ACCOUNTS_NUMBER_HIGH",
    	}
    	AccountDefenderAssessment_AccountDefenderLabel_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ACCOUNT_DEFENDER_LABEL_UNSPECIFIED": 0,
    		"PROFILE_MATCH":                      1,
    		"SUSPICIOUS_LOGIN_ACTIVITY":          2,
    		"SUSPICIOUS_ACCOUNT_CREATION":        3,
    		"RELATED_ACCOUNTS_NUMBER_HIGH":       4,
    	}
    )

Enum value maps for AccountDefenderAssessment_AccountDefenderLabel.

### File_google_cloud_recaptchaenterprise_v1beta1_recaptchaenterprise_proto
    
    
    var File_google_cloud_recaptchaenterprise_v1beta1_recaptchaenterprise_proto protoreflect.FileDescriptor

### RecaptchaEnterpriseServiceV1Beta1_ServiceDesc
    
    
    var RecaptchaEnterpriseServiceV1Beta1_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1",
    	HandlerType: (*RecaptchaEnterpriseServiceV1Beta1Server)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateAssessment",
    			Handler:    _RecaptchaEnterpriseServiceV1Beta1_CreateAssessment_Handler,
    		},
    		{
    			MethodName: "AnnotateAssessment",
    			Handler:    _RecaptchaEnterpriseServiceV1Beta1_AnnotateAssessment_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/recaptchaenterprise/v1beta1/recaptchaenterprise.proto",
    }

RecaptchaEnterpriseServiceV1Beta1_ServiceDesc is the grpc.ServiceDesc for RecaptchaEnterpriseServiceV1Beta1 service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterRecaptchaEnterpriseServiceV1Beta1Server 
    
    
    func RegisterRecaptchaEnterpriseServiceV1Beta1Server(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv RecaptchaEnterpriseServiceV1Beta1Server)

## AccountDefenderAssessment
    
    
    type AccountDefenderAssessment struct {
    
    	// Labels for this request.
    	Labels []AccountDefenderAssessment_AccountDefenderLabel `protobuf:"varint,1,rep,packed,name=labels,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.AccountDefenderAssessment_AccountDefenderLabel" json:"labels,omitempty"`
    	// contains filtered or unexported fields
    }

Account defender risk assessment.

### func (*AccountDefenderAssessment) Descriptor 
    
    
    func (*AccountDefenderAssessment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountDefenderAssessment.ProtoReflect.Descriptor instead.

### func (*AccountDefenderAssessment) GetLabels 
    
    
    func (x *AccountDefenderAssessment) GetLabels() []AccountDefenderAssessment_AccountDefenderLabel

### func (*AccountDefenderAssessment) ProtoMessage 
    
    
    func (*AccountDefenderAssessment) ProtoMessage()

### func (*AccountDefenderAssessment) ProtoReflect 
    
    
    func (x *AccountDefenderAssessment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AccountDefenderAssessment) Reset 
    
    
    func (x *AccountDefenderAssessment) Reset()

### func (*AccountDefenderAssessment) String 
    
    
    func (x *AccountDefenderAssessment) String() [string](https://pkg.go.dev/builtin#string)

## AccountDefenderAssessment_AccountDefenderLabel
    
    
    type AccountDefenderAssessment_AccountDefenderLabel [int32](https://pkg.go.dev/builtin#int32)

Labels returned by account defender for this request.

### AccountDefenderAssessment_ACCOUNT_DEFENDER_LABEL_UNSPECIFIED, AccountDefenderAssessment_PROFILE_MATCH, AccountDefenderAssessment_SUSPICIOUS_LOGIN_ACTIVITY, AccountDefenderAssessment_SUSPICIOUS_ACCOUNT_CREATION, AccountDefenderAssessment_RELATED_ACCOUNTS_NUMBER_HIGH
    
    
    const (
    	// Default unspecified type.
    	AccountDefenderAssessment_ACCOUNT_DEFENDER_LABEL_UNSPECIFIED AccountDefenderAssessment_AccountDefenderLabel = 0
    	// The request matches a known good profile for the user.
    	AccountDefenderAssessment_PROFILE_MATCH AccountDefenderAssessment_AccountDefenderLabel = 1
    	// The request is potentially a suspicious login event and should be further
    	// verified either via multi-factor authentication or another system.
    	AccountDefenderAssessment_SUSPICIOUS_LOGIN_ACTIVITY AccountDefenderAssessment_AccountDefenderLabel = 2
    	// The request matched a profile that previously had suspicious account
    	// creation behavior. This could mean this is a fake account.
    	AccountDefenderAssessment_SUSPICIOUS_ACCOUNT_CREATION AccountDefenderAssessment_AccountDefenderLabel = 3
    	// The account in the request has a high number of related accounts. It does
    	// not necessarily imply that the account is bad but could require
    	// investigating.
    	AccountDefenderAssessment_RELATED_ACCOUNTS_NUMBER_HIGH AccountDefenderAssessment_AccountDefenderLabel = 4
    )

### func (AccountDefenderAssessment_AccountDefenderLabel) Descriptor 
    
    
    func (AccountDefenderAssessment_AccountDefenderLabel) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AccountDefenderAssessment_AccountDefenderLabel) Enum 
    
    
    func (x AccountDefenderAssessment_AccountDefenderLabel) Enum() *AccountDefenderAssessment_AccountDefenderLabel

### func (AccountDefenderAssessment_AccountDefenderLabel) EnumDescriptor 
    
    
    func (AccountDefenderAssessment_AccountDefenderLabel) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AccountDefenderAssessment_AccountDefenderLabel.Descriptor instead.

### func (AccountDefenderAssessment_AccountDefenderLabel) Number 
    
    
    func (x AccountDefenderAssessment_AccountDefenderLabel) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AccountDefenderAssessment_AccountDefenderLabel) String 
    
    
    func (x AccountDefenderAssessment_AccountDefenderLabel) String() [string](https://pkg.go.dev/builtin#string)

### func (AccountDefenderAssessment_AccountDefenderLabel) Type 
    
    
    func (AccountDefenderAssessment_AccountDefenderLabel) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AnnotateAssessmentRequest
    
    
    type AnnotateAssessmentRequest struct {
    
    	// Required. The resource name of the Assessment, in the format
    	// `projects/{project_number}/assessments/{assessment_id}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The annotation that is assigned to the Event. This field can be
    	// left empty to provide reasons that apply to an event without concluding
    	// whether the event is legitimate or fraudulent.
    	Annotation AnnotateAssessmentRequest_Annotation `protobuf:"varint,2,opt,name=annotation,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.AnnotateAssessmentRequest_Annotation" json:"annotation,omitempty"`
    	// Optional. Reasons for the annotation that are assigned to the event.
    	Reasons []AnnotateAssessmentRequest_Reason `protobuf:"varint,3,rep,packed,name=reasons,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.AnnotateAssessmentRequest_Reason" json:"reasons,omitempty"`
    	// Optional. Unique stable hashed user identifier to apply to the assessment.
    	// This is an alternative to setting the `hashed_account_id` in
    	// `CreateAssessment`, for example, when the account identifier is not yet
    	// known in the initial request. It is recommended that the identifier is
    	// hashed using hmac-sha256 with stable secret.
    	HashedAccountId [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,4,opt,name=hashed_account_id,json=hashedAccountId,proto3" json:"hashed_account_id,omitempty"`
    	// Optional. If the assessment is part of a payment transaction, provide
    	// details on payment lifecycle events that occur in the transaction.
    	TransactionEvent *TransactionEvent `protobuf:"bytes,5,opt,name=transaction_event,json=transactionEvent,proto3" json:"transaction_event,omitempty"`
    	// contains filtered or unexported fields
    }

The request message to annotate an Assessment.

### func (*AnnotateAssessmentRequest) Descriptor 
    
    
    func (*AnnotateAssessmentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotateAssessmentRequest.ProtoReflect.Descriptor instead.

### func (*AnnotateAssessmentRequest) GetAnnotation 
    
    
    func (x *AnnotateAssessmentRequest) GetAnnotation() AnnotateAssessmentRequest_Annotation

### func (*AnnotateAssessmentRequest) GetHashedAccountId 
    
    
    func (x *AnnotateAssessmentRequest) GetHashedAccountId() [][byte](https://pkg.go.dev/builtin#byte)

### func (*AnnotateAssessmentRequest) GetName 
    
    
    func (x *AnnotateAssessmentRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*AnnotateAssessmentRequest) GetReasons 
    
    
    func (x *AnnotateAssessmentRequest) GetReasons() []AnnotateAssessmentRequest_Reason

### func (*AnnotateAssessmentRequest) GetTransactionEvent 
    
    
    func (x *AnnotateAssessmentRequest) GetTransactionEvent() *TransactionEvent

### func (*AnnotateAssessmentRequest) ProtoMessage 
    
    
    func (*AnnotateAssessmentRequest) ProtoMessage()

### func (*AnnotateAssessmentRequest) ProtoReflect 
    
    
    func (x *AnnotateAssessmentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AnnotateAssessmentRequest) Reset 
    
    
    func (x *AnnotateAssessmentRequest) Reset()

### func (*AnnotateAssessmentRequest) String 
    
    
    func (x *AnnotateAssessmentRequest) String() [string](https://pkg.go.dev/builtin#string)

## AnnotateAssessmentRequest_Annotation
    
    
    type AnnotateAssessmentRequest_Annotation [int32](https://pkg.go.dev/builtin#int32)

Enum that represents the types of annotations.

### AnnotateAssessmentRequest_ANNOTATION_UNSPECIFIED, AnnotateAssessmentRequest_LEGITIMATE, AnnotateAssessmentRequest_FRAUDULENT, AnnotateAssessmentRequest_PASSWORD_CORRECT, AnnotateAssessmentRequest_PASSWORD_INCORRECT
    
    
    const (
    	// Default unspecified type.
    	AnnotateAssessmentRequest_ANNOTATION_UNSPECIFIED AnnotateAssessmentRequest_Annotation = 0
    	// Provides information that the event turned out to be legitimate.
    	AnnotateAssessmentRequest_LEGITIMATE AnnotateAssessmentRequest_Annotation = 1
    	// Provides information that the event turned out to be fraudulent.
    	AnnotateAssessmentRequest_FRAUDULENT AnnotateAssessmentRequest_Annotation = 2
    	// Provides information that the event was related to a login event in which
    	// the user typed the correct password. Deprecated, prefer indicating
    	// CORRECT_PASSWORD through the reasons field instead.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/recaptchaenterprise/v1beta1/recaptchaenterprise.proto.
    	AnnotateAssessmentRequest_PASSWORD_CORRECT AnnotateAssessmentRequest_Annotation = 3
    	// Provides information that the event was related to a login event in which
    	// the user typed the incorrect password. Deprecated, prefer indicating
    	// INCORRECT_PASSWORD through the reasons field instead.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/recaptchaenterprise/v1beta1/recaptchaenterprise.proto.
    	AnnotateAssessmentRequest_PASSWORD_INCORRECT AnnotateAssessmentRequest_Annotation = 4
    )

### func (AnnotateAssessmentRequest_Annotation) Descriptor 
    
    
    func (AnnotateAssessmentRequest_Annotation) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AnnotateAssessmentRequest_Annotation) Enum 
    
    
    func (x AnnotateAssessmentRequest_Annotation) Enum() *AnnotateAssessmentRequest_Annotation

### func (AnnotateAssessmentRequest_Annotation) EnumDescriptor 
    
    
    func (AnnotateAssessmentRequest_Annotation) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotateAssessmentRequest_Annotation.Descriptor instead.

### func (AnnotateAssessmentRequest_Annotation) Number 
    
    
    func (x AnnotateAssessmentRequest_Annotation) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AnnotateAssessmentRequest_Annotation) String 
    
    
    func (x AnnotateAssessmentRequest_Annotation) String() [string](https://pkg.go.dev/builtin#string)

### func (AnnotateAssessmentRequest_Annotation) Type 
    
    
    func (AnnotateAssessmentRequest_Annotation) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AnnotateAssessmentRequest_Reason
    
    
    type AnnotateAssessmentRequest_Reason [int32](https://pkg.go.dev/builtin#int32)

Enum that represents potential reasons for annotating an assessment.

### AnnotateAssessmentRequest_REASON_UNSPECIFIED, AnnotateAssessmentRequest_CHARGEBACK, AnnotateAssessmentRequest_CHARGEBACK_FRAUD, AnnotateAssessmentRequest_CHARGEBACK_DISPUTE, AnnotateAssessmentRequest_REFUND, AnnotateAssessmentRequest_REFUND_FRAUD, AnnotateAssessmentRequest_TRANSACTION_ACCEPTED, AnnotateAssessmentRequest_TRANSACTION_DECLINED, AnnotateAssessmentRequest_PAYMENT_HEURISTICS, AnnotateAssessmentRequest_INITIATED_TWO_FACTOR, AnnotateAssessmentRequest_PASSED_TWO_FACTOR, AnnotateAssessmentRequest_FAILED_TWO_FACTOR, AnnotateAssessmentRequest_CORRECT_PASSWORD, AnnotateAssessmentRequest_INCORRECT_PASSWORD, AnnotateAssessmentRequest_SOCIAL_SPAM
    
    
    const (
    	// Default unspecified reason.
    	AnnotateAssessmentRequest_REASON_UNSPECIFIED AnnotateAssessmentRequest_Reason = 0
    	// Indicates that the transaction had a chargeback issued with no other
    	// details. When possible, specify the type by using CHARGEBACK_FRAUD or
    	// CHARGEBACK_DISPUTE instead.
    	AnnotateAssessmentRequest_CHARGEBACK AnnotateAssessmentRequest_Reason = 1
    	// Indicates that the transaction had a chargeback issued related to an
    	// alleged unauthorized transaction from the cardholder's perspective (for
    	// example, the card number was stolen).
    	AnnotateAssessmentRequest_CHARGEBACK_FRAUD AnnotateAssessmentRequest_Reason = 8
    	// Indicates that the transaction had a chargeback issued related to the
    	// cardholder having provided their card details but allegedly not being
    	// satisfied with the purchase (for example, misrepresentation, attempted
    	// cancellation).
    	AnnotateAssessmentRequest_CHARGEBACK_DISPUTE AnnotateAssessmentRequest_Reason = 9
    	// Indicates that the completed payment transaction was refunded by the
    	// seller.
    	AnnotateAssessmentRequest_REFUND AnnotateAssessmentRequest_Reason = 10
    	// Indicates that the completed payment transaction was determined to be
    	// fraudulent by the seller, and was cancelled and refunded as a result.
    	AnnotateAssessmentRequest_REFUND_FRAUD AnnotateAssessmentRequest_Reason = 11
    	// Indicates that the payment transaction was accepted, and the user was
    	// charged.
    	AnnotateAssessmentRequest_TRANSACTION_ACCEPTED AnnotateAssessmentRequest_Reason = 12
    	// Indicates that the payment transaction was declined, for example due to
    	// invalid card details.
    	AnnotateAssessmentRequest_TRANSACTION_DECLINED AnnotateAssessmentRequest_Reason = 13
    	// Indicates the transaction associated with the assessment is suspected of
    	// being fraudulent based on the payment method, billing details, shipping
    	// address or other transaction information.
    	AnnotateAssessmentRequest_PAYMENT_HEURISTICS AnnotateAssessmentRequest_Reason = 2
    	// Indicates that the user was served a 2FA challenge. An old assessment
    	// with `ENUM_VALUES.INITIATED_TWO_FACTOR` reason that has not been
    	// overwritten with `PASSED_TWO_FACTOR` is treated as an abandoned 2FA flow.
    	// This is equivalent to `FAILED_TWO_FACTOR`.
    	AnnotateAssessmentRequest_INITIATED_TWO_FACTOR AnnotateAssessmentRequest_Reason = 7
    	// Indicates that the user passed a 2FA challenge.
    	AnnotateAssessmentRequest_PASSED_TWO_FACTOR AnnotateAssessmentRequest_Reason = 3
    	// Indicates that the user failed a 2FA challenge.
    	AnnotateAssessmentRequest_FAILED_TWO_FACTOR AnnotateAssessmentRequest_Reason = 4
    	// Indicates the user provided the correct password.
    	AnnotateAssessmentRequest_CORRECT_PASSWORD AnnotateAssessmentRequest_Reason = 5
    	// Indicates the user provided an incorrect password.
    	AnnotateAssessmentRequest_INCORRECT_PASSWORD AnnotateAssessmentRequest_Reason = 6
    	// Indicates that the user sent unwanted and abusive messages to other users
    	// of the platform, such as spam, scams, phishing, or social engineering.
    	AnnotateAssessmentRequest_SOCIAL_SPAM AnnotateAssessmentRequest_Reason = 14
    )

### func (AnnotateAssessmentRequest_Reason) Descriptor 
    
    
    func (AnnotateAssessmentRequest_Reason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AnnotateAssessmentRequest_Reason) Enum 
    
    
    func (x AnnotateAssessmentRequest_Reason) Enum() *AnnotateAssessmentRequest_Reason

### func (AnnotateAssessmentRequest_Reason) EnumDescriptor 
    
    
    func (AnnotateAssessmentRequest_Reason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotateAssessmentRequest_Reason.Descriptor instead.

### func (AnnotateAssessmentRequest_Reason) Number 
    
    
    func (x AnnotateAssessmentRequest_Reason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AnnotateAssessmentRequest_Reason) String 
    
    
    func (x AnnotateAssessmentRequest_Reason) String() [string](https://pkg.go.dev/builtin#string)

### func (AnnotateAssessmentRequest_Reason) Type 
    
    
    func (AnnotateAssessmentRequest_Reason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AnnotateAssessmentResponse
    
    
    type AnnotateAssessmentResponse struct {
    	// contains filtered or unexported fields
    }

Empty response for AnnotateAssessment.

### func (*AnnotateAssessmentResponse) Descriptor 
    
    
    func (*AnnotateAssessmentResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotateAssessmentResponse.ProtoReflect.Descriptor instead.

### func (*AnnotateAssessmentResponse) ProtoMessage 
    
    
    func (*AnnotateAssessmentResponse) ProtoMessage()

### func (*AnnotateAssessmentResponse) ProtoReflect 
    
    
    func (x *AnnotateAssessmentResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AnnotateAssessmentResponse) Reset 
    
    
    func (x *AnnotateAssessmentResponse) Reset()

### func (*AnnotateAssessmentResponse) String 
    
    
    func (x *AnnotateAssessmentResponse) String() [string](https://pkg.go.dev/builtin#string)

## Assessment
    
    
    type Assessment struct {
    
    	// Output only. The resource name for the Assessment in the format
    	// `projects/{project_number}/assessments/{assessment_id}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The event being assessed.
    	Event *Event `protobuf:"bytes,2,opt,name=event,proto3" json:"event,omitempty"`
    	// Output only. Legitimate event score from 0.0 to 1.0.
    	// (1.0 means very likely legitimate traffic while 0.0 means very likely
    	// non-legitimate traffic).
    	Score [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,3,opt,name=score,proto3" json:"score,omitempty"`
    	// Output only. Properties of the provided event token.
    	TokenProperties *TokenProperties `protobuf:"bytes,4,opt,name=token_properties,json=tokenProperties,proto3" json:"token_properties,omitempty"`
    	// Output only. Reasons contributing to the risk analysis verdict.
    	Reasons []Assessment_ClassificationReason `protobuf:"varint,5,rep,packed,name=reasons,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.Assessment_ClassificationReason" json:"reasons,omitempty"`
    	// Information about the user's credentials used to check for leaks.
    	// This feature is part of the Early Access Program (EAP). Exercise caution,
    	// and do not deploy integrations based on this feature in a production
    	// environment.
    	PasswordLeakVerification *PasswordLeakVerification `protobuf:"bytes,7,opt,name=password_leak_verification,json=passwordLeakVerification,proto3" json:"password_leak_verification,omitempty"`
    	// Assessment returned by account defender when a hashed_account_id is
    	// provided.
    	AccountDefenderAssessment *AccountDefenderAssessment `protobuf:"bytes,8,opt,name=account_defender_assessment,json=accountDefenderAssessment,proto3" json:"account_defender_assessment,omitempty"`
    	// Assessment returned by Fraud Prevention when TransactionData is provided.
    	FraudPreventionAssessment *FraudPreventionAssessment `protobuf:"bytes,11,opt,name=fraud_prevention_assessment,json=fraudPreventionAssessment,proto3" json:"fraud_prevention_assessment,omitempty"`
    	// contains filtered or unexported fields
    }

A reCAPTCHA Enterprise assessment resource.

### func (*Assessment) Descriptor 
    
    
    func (*Assessment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Assessment.ProtoReflect.Descriptor instead.

### func (*Assessment) GetAccountDefenderAssessment 
    
    
    func (x *Assessment) GetAccountDefenderAssessment() *AccountDefenderAssessment

### func (*Assessment) GetEvent 
    
    
    func (x *Assessment) GetEvent() *Event

### func (*Assessment) GetFraudPreventionAssessment 
    
    
    func (x *Assessment) GetFraudPreventionAssessment() *FraudPreventionAssessment

### func (*Assessment) GetName 
    
    
    func (x *Assessment) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Assessment) GetPasswordLeakVerification 
    
    
    func (x *Assessment) GetPasswordLeakVerification() *PasswordLeakVerification

### func (*Assessment) GetReasons 
    
    
    func (x *Assessment) GetReasons() []Assessment_ClassificationReason

### func (*Assessment) GetScore 
    
    
    func (x *Assessment) GetScore() [float32](https://pkg.go.dev/builtin#float32)

### func (*Assessment) GetTokenProperties 
    
    
    func (x *Assessment) GetTokenProperties() *TokenProperties

### func (*Assessment) ProtoMessage 
    
    
    func (*Assessment) ProtoMessage()

### func (*Assessment) ProtoReflect 
    
    
    func (x *Assessment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Assessment) Reset 
    
    
    func (x *Assessment) Reset()

### func (*Assessment) String 
    
    
    func (x *Assessment) String() [string](https://pkg.go.dev/builtin#string)

## Assessment_ClassificationReason
    
    
    type Assessment_ClassificationReason [int32](https://pkg.go.dev/builtin#int32)

Reasons contributing to the risk analysis verdict.

### Assessment_CLASSIFICATION_REASON_UNSPECIFIED, Assessment_AUTOMATION, Assessment_UNEXPECTED_ENVIRONMENT, Assessment_TOO_MUCH_TRAFFIC, Assessment_UNEXPECTED_USAGE_PATTERNS, Assessment_LOW_CONFIDENCE_SCORE, Assessment_SUSPECTED_CARDING, Assessment_SUSPECTED_CHARGEBACK
    
    
    const (
    	// Default unspecified type.
    	Assessment_CLASSIFICATION_REASON_UNSPECIFIED Assessment_ClassificationReason = 0
    	// Interactions matched the behavior of an automated agent.
    	Assessment_AUTOMATION Assessment_ClassificationReason = 1
    	// The event originated from an illegitimate environment.
    	Assessment_UNEXPECTED_ENVIRONMENT Assessment_ClassificationReason = 2
    	// Traffic volume from the event source is higher than normal.
    	Assessment_TOO_MUCH_TRAFFIC Assessment_ClassificationReason = 3
    	// Interactions with the site were significantly different than expected
    	// patterns.
    	Assessment_UNEXPECTED_USAGE_PATTERNS Assessment_ClassificationReason = 4
    	// Too little traffic has been received from this site thus far to generate
    	// quality risk analysis.
    	Assessment_LOW_CONFIDENCE_SCORE Assessment_ClassificationReason = 5
    	// The request matches behavioral characteristics of a carding attack.
    	Assessment_SUSPECTED_CARDING Assessment_ClassificationReason = 6
    	// The request matches behavioral characteristics of chargebacks for fraud.
    	Assessment_SUSPECTED_CHARGEBACK Assessment_ClassificationReason = 7
    )

### func (Assessment_ClassificationReason) Descriptor 
    
    
    func (Assessment_ClassificationReason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Assessment_ClassificationReason) Enum 
    
    
    func (x Assessment_ClassificationReason) Enum() *Assessment_ClassificationReason

### func (Assessment_ClassificationReason) EnumDescriptor 
    
    
    func (Assessment_ClassificationReason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Assessment_ClassificationReason.Descriptor instead.

### func (Assessment_ClassificationReason) Number 
    
    
    func (x Assessment_ClassificationReason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Assessment_ClassificationReason) String 
    
    
    func (x Assessment_ClassificationReason) String() [string](https://pkg.go.dev/builtin#string)

### func (Assessment_ClassificationReason) Type 
    
    
    func (Assessment_ClassificationReason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CreateAssessmentRequest
    
    
    type CreateAssessmentRequest struct {
    
    	// Required. The name of the project in which the assessment is created,
    	// in the format `projects/{project_number}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The assessment details.
    	Assessment *Assessment `protobuf:"bytes,2,opt,name=assessment,proto3" json:"assessment,omitempty"`
    	// contains filtered or unexported fields
    }

The create assessment request message.

### func (*CreateAssessmentRequest) Descriptor 
    
    
    func (*CreateAssessmentRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAssessmentRequest.ProtoReflect.Descriptor instead.

### func (*CreateAssessmentRequest) GetAssessment 
    
    
    func (x *CreateAssessmentRequest) GetAssessment() *Assessment

### func (*CreateAssessmentRequest) GetParent 
    
    
    func (x *CreateAssessmentRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAssessmentRequest) ProtoMessage 
    
    
    func (*CreateAssessmentRequest) ProtoMessage()

### func (*CreateAssessmentRequest) ProtoReflect 
    
    
    func (x *CreateAssessmentRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAssessmentRequest) Reset 
    
    
    func (x *CreateAssessmentRequest) Reset()

### func (*CreateAssessmentRequest) String 
    
    
    func (x *CreateAssessmentRequest) String() [string](https://pkg.go.dev/builtin#string)

## Event
    
    
    type Event struct {
    
    	// Optional. The user response token provided by the reCAPTCHA client-side
    	// integration on your site.
    	Token [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
    	// Optional. The site key that was used to invoke reCAPTCHA on your site and
    	// generate the token.
    	SiteKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=site_key,json=siteKey,proto3" json:"site_key,omitempty"`
    	// Optional. The user agent present in the request from the user's device
    	// related to this event.
    	UserAgent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=user_agent,json=userAgent,proto3" json:"user_agent,omitempty"`
    	// Optional. The IP address in the request from the user's device related to
    	// this event.
    	UserIpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=user_ip_address,json=userIpAddress,proto3" json:"user_ip_address,omitempty"`
    	// Optional. The expected action for this type of event. This should be the
    	// same action provided at token generation time on client-side platforms
    	// already integrated with reCAPTCHA.
    	ExpectedAction [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=expected_action,json=expectedAction,proto3" json:"expected_action,omitempty"`
    	// Optional. Unique stable hashed user identifier for the request. The
    	// identifier must be hashed using hmac-sha256 with stable secret.
    	HashedAccountId [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,6,opt,name=hashed_account_id,json=hashedAccountId,proto3" json:"hashed_account_id,omitempty"`
    	// Optional. Data describing a payment transaction to be assessed. Sending
    	// this data enables reCAPTCHA Fraud Prevention and the
    	// FraudPreventionAssessment component in the response.
    	TransactionData *TransactionData `protobuf:"bytes,13,opt,name=transaction_data,json=transactionData,proto3" json:"transaction_data,omitempty"`
    	// Optional. The Fraud Prevention setting for this Assessment.
    	FraudPrevention Event_FraudPrevention `protobuf:"varint,17,opt,name=fraud_prevention,json=fraudPrevention,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.Event_FraudPrevention" json:"fraud_prevention,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*Event) Descriptor 
    
    
    func (*Event) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event.ProtoReflect.Descriptor instead.

### func (*Event) GetExpectedAction 
    
    
    func (x *Event) GetExpectedAction() [string](https://pkg.go.dev/builtin#string)

### func (*Event) GetFraudPrevention 
    
    
    func (x *Event) GetFraudPrevention() Event_FraudPrevention

### func (*Event) GetHashedAccountId 
    
    
    func (x *Event) GetHashedAccountId() [][byte](https://pkg.go.dev/builtin#byte)

### func (*Event) GetSiteKey 
    
    
    func (x *Event) GetSiteKey() [string](https://pkg.go.dev/builtin#string)

### func (*Event) GetToken 
    
    
    func (x *Event) GetToken() [string](https://pkg.go.dev/builtin#string)

### func (*Event) GetTransactionData 
    
    
    func (x *Event) GetTransactionData() *TransactionData

### func (*Event) GetUserAgent 
    
    
    func (x *Event) GetUserAgent() [string](https://pkg.go.dev/builtin#string)

### func (*Event) GetUserIpAddress 
    
    
    func (x *Event) GetUserIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*Event) ProtoMessage 
    
    
    func (*Event) ProtoMessage()

### func (*Event) ProtoReflect 
    
    
    func (x *Event) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event) Reset 
    
    
    func (x *Event) Reset()

### func (*Event) String 
    
    
    func (x *Event) String() [string](https://pkg.go.dev/builtin#string)

## Event_FraudPrevention
    
    
    type Event_FraudPrevention [int32](https://pkg.go.dev/builtin#int32)

Setting that controls Fraud Prevention assessments.

### Event_FRAUD_PREVENTION_UNSPECIFIED, Event_ENABLED, Event_DISABLED
    
    
    const (
    	// Default, unspecified setting. `fraud_prevention_assessment` is returned
    	// if `transaction_data` is present in `Event` and Fraud Prevention is
    	// enabled in the Google Cloud console.
    	Event_FRAUD_PREVENTION_UNSPECIFIED Event_FraudPrevention = 0
    	// Enable Fraud Prevention for this assessment, if Fraud Prevention is
    	// enabled in the Google Cloud console.
    	Event_ENABLED Event_FraudPrevention = 1
    	// Disable Fraud Prevention for this assessment, regardless of the Google
    	// Cloud console settings.
    	Event_DISABLED Event_FraudPrevention = 2
    )

### func (Event_FraudPrevention) Descriptor 
    
    
    func (Event_FraudPrevention) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Event_FraudPrevention) Enum 
    
    
    func (x Event_FraudPrevention) Enum() *Event_FraudPrevention

### func (Event_FraudPrevention) EnumDescriptor 
    
    
    func (Event_FraudPrevention) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_FraudPrevention.Descriptor instead.

### func (Event_FraudPrevention) Number 
    
    
    func (x Event_FraudPrevention) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Event_FraudPrevention) String 
    
    
    func (x Event_FraudPrevention) String() [string](https://pkg.go.dev/builtin#string)

### func (Event_FraudPrevention) Type 
    
    
    func (Event_FraudPrevention) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## FraudPreventionAssessment
    
    
    type FraudPreventionAssessment struct {
    
    	// Output only. Probability (0-1) of this transaction being fraudulent.
    	// Summarizes the combined risk of attack vectors below.
    	TransactionRisk [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=transaction_risk,json=transactionRisk,proto3" json:"transaction_risk,omitempty"`
    	// Output only. Assessment of this transaction for risk of a stolen
    	// instrument.
    	StolenInstrumentVerdict *FraudPreventionAssessment_StolenInstrumentVerdict `protobuf:"bytes,2,opt,name=stolen_instrument_verdict,json=stolenInstrumentVerdict,proto3" json:"stolen_instrument_verdict,omitempty"`
    	// Output only. Assessment of this transaction for risk of being part of a
    	// card testing attack.
    	CardTestingVerdict *FraudPreventionAssessment_CardTestingVerdict `protobuf:"bytes,3,opt,name=card_testing_verdict,json=cardTestingVerdict,proto3" json:"card_testing_verdict,omitempty"`
    	// Output only. Assessment of this transaction for behavioral trust.
    	BehavioralTrustVerdict *FraudPreventionAssessment_BehavioralTrustVerdict `protobuf:"bytes,4,opt,name=behavioral_trust_verdict,json=behavioralTrustVerdict,proto3" json:"behavioral_trust_verdict,omitempty"`
    	// contains filtered or unexported fields
    }

Assessment for Fraud Prevention.

### func (*FraudPreventionAssessment) Descriptor 
    
    
    func (*FraudPreventionAssessment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FraudPreventionAssessment.ProtoReflect.Descriptor instead.

### func (*FraudPreventionAssessment) GetBehavioralTrustVerdict 
    
    
    func (x *FraudPreventionAssessment) GetBehavioralTrustVerdict() *FraudPreventionAssessment_BehavioralTrustVerdict

### func (*FraudPreventionAssessment) GetCardTestingVerdict 
    
    
    func (x *FraudPreventionAssessment) GetCardTestingVerdict() *FraudPreventionAssessment_CardTestingVerdict

### func (*FraudPreventionAssessment) GetStolenInstrumentVerdict 
    
    
    func (x *FraudPreventionAssessment) GetStolenInstrumentVerdict() *FraudPreventionAssessment_StolenInstrumentVerdict

### func (*FraudPreventionAssessment) GetTransactionRisk 
    
    
    func (x *FraudPreventionAssessment) GetTransactionRisk() [float32](https://pkg.go.dev/builtin#float32)

### func (*FraudPreventionAssessment) ProtoMessage 
    
    
    func (*FraudPreventionAssessment) ProtoMessage()

### func (*FraudPreventionAssessment) ProtoReflect 
    
    
    func (x *FraudPreventionAssessment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FraudPreventionAssessment) Reset 
    
    
    func (x *FraudPreventionAssessment) Reset()

### func (*FraudPreventionAssessment) String 
    
    
    func (x *FraudPreventionAssessment) String() [string](https://pkg.go.dev/builtin#string)

## FraudPreventionAssessment_BehavioralTrustVerdict
    
    
    type FraudPreventionAssessment_BehavioralTrustVerdict struct {
    
    	// Output only. Probability (0-1) of this transaction attempt being executed
    	// in a behaviorally trustworthy way.
    	Trust [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=trust,proto3" json:"trust,omitempty"`
    	// contains filtered or unexported fields
    }

Information about behavioral trust of the transaction.

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) Descriptor 
    
    
    func (*FraudPreventionAssessment_BehavioralTrustVerdict) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FraudPreventionAssessment_BehavioralTrustVerdict.ProtoReflect.Descriptor instead.

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) GetTrust 
    
    
    func (x *FraudPreventionAssessment_BehavioralTrustVerdict) GetTrust() [float32](https://pkg.go.dev/builtin#float32)

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) ProtoMessage 
    
    
    func (*FraudPreventionAssessment_BehavioralTrustVerdict) ProtoMessage()

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) ProtoReflect 
    
    
    func (x *FraudPreventionAssessment_BehavioralTrustVerdict) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) Reset 
    
    
    func (x *FraudPreventionAssessment_BehavioralTrustVerdict) Reset()

### func (*FraudPreventionAssessment_BehavioralTrustVerdict) String 
    
    
    func (x *FraudPreventionAssessment_BehavioralTrustVerdict) String() [string](https://pkg.go.dev/builtin#string)

## FraudPreventionAssessment_CardTestingVerdict
    
    
    type FraudPreventionAssessment_CardTestingVerdict struct {
    
    	// Output only. Probability (0-1) of this transaction attempt being part of
    	// a card testing attack.
    	Risk [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=risk,proto3" json:"risk,omitempty"`
    	// contains filtered or unexported fields
    }

Information about card testing fraud, where an adversary is testing fraudulently obtained cards or brute forcing their details.

### func (*FraudPreventionAssessment_CardTestingVerdict) Descriptor 
    
    
    func (*FraudPreventionAssessment_CardTestingVerdict) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FraudPreventionAssessment_CardTestingVerdict.ProtoReflect.Descriptor instead.

### func (*FraudPreventionAssessment_CardTestingVerdict) GetRisk 
    
    
    func (x *FraudPreventionAssessment_CardTestingVerdict) GetRisk() [float32](https://pkg.go.dev/builtin#float32)

### func (*FraudPreventionAssessment_CardTestingVerdict) ProtoMessage 
    
    
    func (*FraudPreventionAssessment_CardTestingVerdict) ProtoMessage()

### func (*FraudPreventionAssessment_CardTestingVerdict) ProtoReflect 
    
    
    func (x *FraudPreventionAssessment_CardTestingVerdict) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FraudPreventionAssessment_CardTestingVerdict) Reset 
    
    
    func (x *FraudPreventionAssessment_CardTestingVerdict) Reset()

### func (*FraudPreventionAssessment_CardTestingVerdict) String 
    
    
    func (x *FraudPreventionAssessment_CardTestingVerdict) String() [string](https://pkg.go.dev/builtin#string)

## FraudPreventionAssessment_StolenInstrumentVerdict
    
    
    type FraudPreventionAssessment_StolenInstrumentVerdict struct {
    
    	// Output only. Probability (0-1) of this transaction being executed with a
    	// stolen instrument.
    	Risk [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=risk,proto3" json:"risk,omitempty"`
    	// contains filtered or unexported fields
    }

Information about stolen instrument fraud, where the user is not the legitimate owner of the instrument being used for the purchase.

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) Descriptor 
    
    
    func (*FraudPreventionAssessment_StolenInstrumentVerdict) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FraudPreventionAssessment_StolenInstrumentVerdict.ProtoReflect.Descriptor instead.

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) GetRisk 
    
    
    func (x *FraudPreventionAssessment_StolenInstrumentVerdict) GetRisk() [float32](https://pkg.go.dev/builtin#float32)

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) ProtoMessage 
    
    
    func (*FraudPreventionAssessment_StolenInstrumentVerdict) ProtoMessage()

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) ProtoReflect 
    
    
    func (x *FraudPreventionAssessment_StolenInstrumentVerdict) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) Reset 
    
    
    func (x *FraudPreventionAssessment_StolenInstrumentVerdict) Reset()

### func (*FraudPreventionAssessment_StolenInstrumentVerdict) String 
    
    
    func (x *FraudPreventionAssessment_StolenInstrumentVerdict) String() [string](https://pkg.go.dev/builtin#string)

## PasswordLeakVerification
    
    
    type PasswordLeakVerification struct {
    
    	// Optional. Scrypt hash of the username+password that the customer wants to
    	// verify against a known password leak.
    	HashedUserCredentials [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=hashed_user_credentials,json=hashedUserCredentials,proto3" json:"hashed_user_credentials,omitempty"`
    	// Output only. Whether or not the user's credentials are present in a known
    	// leak.
    	CredentialsLeaked [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=credentials_leaked,json=credentialsLeaked,proto3" json:"credentials_leaked,omitempty"`
    	// Optional. The username part of the user credentials for which we want to
    	// trigger a leak check in canonicalized form. This is the same data used to
    	// create the hashed_user_credentials on the customer side.
    	CanonicalizedUsername [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=canonicalized_username,json=canonicalizedUsername,proto3" json:"canonicalized_username,omitempty"`
    	// contains filtered or unexported fields
    }

Password leak verification info.

### func (*PasswordLeakVerification) Descriptor 
    
    
    func (*PasswordLeakVerification) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PasswordLeakVerification.ProtoReflect.Descriptor instead.

### func (*PasswordLeakVerification) GetCanonicalizedUsername 
    
    
    func (x *PasswordLeakVerification) GetCanonicalizedUsername() [string](https://pkg.go.dev/builtin#string)

### func (*PasswordLeakVerification) GetCredentialsLeaked 
    
    
    func (x *PasswordLeakVerification) GetCredentialsLeaked() [bool](https://pkg.go.dev/builtin#bool)

### func (*PasswordLeakVerification) GetHashedUserCredentials 
    
    
    func (x *PasswordLeakVerification) GetHashedUserCredentials() [][byte](https://pkg.go.dev/builtin#byte)

### func (*PasswordLeakVerification) ProtoMessage 
    
    
    func (*PasswordLeakVerification) ProtoMessage()

### func (*PasswordLeakVerification) ProtoReflect 
    
    
    func (x *PasswordLeakVerification) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PasswordLeakVerification) Reset 
    
    
    func (x *PasswordLeakVerification) Reset()

### func (*PasswordLeakVerification) String 
    
    
    func (x *PasswordLeakVerification) String() [string](https://pkg.go.dev/builtin#string)

## RecaptchaEnterpriseServiceV1Beta1Client
    
    
    type RecaptchaEnterpriseServiceV1Beta1Client interface {
    	// Creates an Assessment of the likelihood an event is legitimate.
    	CreateAssessment(ctx context.Context, in *CreateAssessmentRequest, opts ...grpc.CallOption) (*Assessment, [error](https://pkg.go.dev/builtin#error))
    	// Annotates a previously created Assessment to provide additional information
    	// on whether the event turned out to be authentic or fradulent.
    	AnnotateAssessment(ctx context.Context, in *AnnotateAssessmentRequest, opts ...grpc.CallOption) (*AnnotateAssessmentResponse, [error](https://pkg.go.dev/builtin#error))
    }

RecaptchaEnterpriseServiceV1Beta1Client is the client API for RecaptchaEnterpriseServiceV1Beta1 service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewRecaptchaEnterpriseServiceV1Beta1Client 
    
    
    func NewRecaptchaEnterpriseServiceV1Beta1Client(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) RecaptchaEnterpriseServiceV1Beta1Client

## RecaptchaEnterpriseServiceV1Beta1Server
    
    
    type RecaptchaEnterpriseServiceV1Beta1Server interface {
    	// Creates an Assessment of the likelihood an event is legitimate.
    	CreateAssessment(context.Context, *CreateAssessmentRequest) (*Assessment, [error](https://pkg.go.dev/builtin#error))
    	// Annotates a previously created Assessment to provide additional information
    	// on whether the event turned out to be authentic or fradulent.
    	AnnotateAssessment(context.Context, *AnnotateAssessmentRequest) (*AnnotateAssessmentResponse, [error](https://pkg.go.dev/builtin#error))
    }

RecaptchaEnterpriseServiceV1Beta1Server is the server API for RecaptchaEnterpriseServiceV1Beta1 service. All implementations should embed UnimplementedRecaptchaEnterpriseServiceV1Beta1Server for forward compatibility

## TokenProperties
    
    
    type TokenProperties struct {
    
    	// Whether the provided user response token is valid. When valid = false, the
    	// reason could be specified in invalid_reason or it could also be due to
    	// a user failing to solve a challenge or a sitekey mismatch (i.e the sitekey
    	// used to generate the token was different than the one specified in the
    	// assessment).
    	Valid [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=valid,proto3" json:"valid,omitempty"`
    	// Reason associated with the response when valid = false.
    	InvalidReason TokenProperties_InvalidReason `protobuf:"varint,2,opt,name=invalid_reason,json=invalidReason,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.TokenProperties_InvalidReason" json:"invalid_reason,omitempty"`
    	// The timestamp corresponding to the generation of the token.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// The hostname of the page on which the token was generated.
    	Hostname [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=hostname,proto3" json:"hostname,omitempty"`
    	// Action name provided at token generation.
    	Action [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=action,proto3" json:"action,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*TokenProperties) Descriptor 
    
    
    func (*TokenProperties) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TokenProperties.ProtoReflect.Descriptor instead.

### func (*TokenProperties) GetAction 
    
    
    func (x *TokenProperties) GetAction() [string](https://pkg.go.dev/builtin#string)

### func (*TokenProperties) GetCreateTime 
    
    
    func (x *TokenProperties) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TokenProperties) GetHostname 
    
    
    func (x *TokenProperties) GetHostname() [string](https://pkg.go.dev/builtin#string)

### func (*TokenProperties) GetInvalidReason 
    
    
    func (x *TokenProperties) GetInvalidReason() TokenProperties_InvalidReason

### func (*TokenProperties) GetValid 
    
    
    func (x *TokenProperties) GetValid() [bool](https://pkg.go.dev/builtin#bool)

### func (*TokenProperties) ProtoMessage 
    
    
    func (*TokenProperties) ProtoMessage()

### func (*TokenProperties) ProtoReflect 
    
    
    func (x *TokenProperties) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TokenProperties) Reset 
    
    
    func (x *TokenProperties) Reset()

### func (*TokenProperties) String 
    
    
    func (x *TokenProperties) String() [string](https://pkg.go.dev/builtin#string)

## TokenProperties_InvalidReason
    
    
    type TokenProperties_InvalidReason [int32](https://pkg.go.dev/builtin#int32)

Enum that represents the types of invalid token reasons.

### TokenProperties_INVALID_REASON_UNSPECIFIED, TokenProperties_UNKNOWN_INVALID_REASON, TokenProperties_MALFORMED, TokenProperties_EXPIRED, TokenProperties_DUPE, TokenProperties_SITE_MISMATCH, TokenProperties_MISSING, TokenProperties_BROWSER_ERROR
    
    
    const (
    	// Default unspecified type.
    	TokenProperties_INVALID_REASON_UNSPECIFIED TokenProperties_InvalidReason = 0
    	// If the failure reason was not accounted for.
    	TokenProperties_UNKNOWN_INVALID_REASON TokenProperties_InvalidReason = 1
    	// The provided user verification token was malformed.
    	TokenProperties_MALFORMED TokenProperties_InvalidReason = 2
    	// The user verification token had expired.
    	TokenProperties_EXPIRED TokenProperties_InvalidReason = 3
    	// The user verification had already been seen.
    	TokenProperties_DUPE TokenProperties_InvalidReason = 4
    	// The user verification token did not match the provided site key.
    	// This may be a configuration error (for example, development keys used in
    	// production) or end users trying to use verification tokens from other
    	// sites.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/recaptchaenterprise/v1beta1/recaptchaenterprise.proto.
    	TokenProperties_SITE_MISMATCH TokenProperties_InvalidReason = 5
    	// The user verification token was not present.  It is a required input.
    	TokenProperties_MISSING TokenProperties_InvalidReason = 6
    	// A retriable error (such as network failure) occurred on the browser.
    	// Could easily be simulated by an attacker.
    	TokenProperties_BROWSER_ERROR TokenProperties_InvalidReason = 7
    )

### func (TokenProperties_InvalidReason) Descriptor 
    
    
    func (TokenProperties_InvalidReason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TokenProperties_InvalidReason) Enum 
    
    
    func (x TokenProperties_InvalidReason) Enum() *TokenProperties_InvalidReason

### func (TokenProperties_InvalidReason) EnumDescriptor 
    
    
    func (TokenProperties_InvalidReason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TokenProperties_InvalidReason.Descriptor instead.

### func (TokenProperties_InvalidReason) Number 
    
    
    func (x TokenProperties_InvalidReason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TokenProperties_InvalidReason) String 
    
    
    func (x TokenProperties_InvalidReason) String() [string](https://pkg.go.dev/builtin#string)

### func (TokenProperties_InvalidReason) Type 
    
    
    func (TokenProperties_InvalidReason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## TransactionData
    
    
    type TransactionData struct {
    
    	// Unique identifier for the transaction. This custom identifier can be used
    	// to reference this transaction in the future, for example, labeling a refund
    	// or chargeback event. Two attempts at the same transaction should use the
    	// same transaction id.
    	TransactionId *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=transaction_id,json=transactionId,proto3,oneof" json:"transaction_id,omitempty"`
    	// The payment method for the transaction. The allowed values are:
    	//
    	// * credit-card
    	// * debit-card
    	// * gift-card
    	// * processor-{name} (If a third-party is used, for example,
    	// processor-paypal)
    	// * custom-{name} (If an alternative method is used, for example,
    	// custom-crypto)
    	PaymentMethod [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=payment_method,json=paymentMethod,proto3" json:"payment_method,omitempty"`
    	// The Bank Identification Number - generally the first 6 or 8 digits of the
    	// card.
    	CardBin [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=card_bin,json=cardBin,proto3" json:"card_bin,omitempty"`
    	// The last four digits of the card.
    	CardLastFour [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=card_last_four,json=cardLastFour,proto3" json:"card_last_four,omitempty"`
    	// The currency code in ISO-4217 format.
    	CurrencyCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=currency_code,json=currencyCode,proto3" json:"currency_code,omitempty"`
    	// The decimal value of the transaction in the specified currency.
    	Value [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,5,opt,name=value,proto3" json:"value,omitempty"`
    	// The value of shipping in the specified currency. 0 for free or no shipping.
    	ShippingValue [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,12,opt,name=shipping_value,json=shippingValue,proto3" json:"shipping_value,omitempty"`
    	// Destination address if this transaction involves shipping a physical item.
    	ShippingAddress *TransactionData_Address `protobuf:"bytes,6,opt,name=shipping_address,json=shippingAddress,proto3" json:"shipping_address,omitempty"`
    	// Address associated with the payment method when applicable.
    	BillingAddress *TransactionData_Address `protobuf:"bytes,7,opt,name=billing_address,json=billingAddress,proto3" json:"billing_address,omitempty"`
    	// Information about the user paying/initiating the transaction.
    	User *TransactionData_User `protobuf:"bytes,8,opt,name=user,proto3" json:"user,omitempty"`
    	// Information about the user or users fulfilling the transaction.
    	Merchants []*TransactionData_User `protobuf:"bytes,13,rep,name=merchants,proto3" json:"merchants,omitempty"`
    	// Items purchased in this transaction.
    	Items []*TransactionData_Item `protobuf:"bytes,14,rep,name=items,proto3" json:"items,omitempty"`
    	// Information about the payment gateway's response to the transaction.
    	GatewayInfo *TransactionData_GatewayInfo `protobuf:"bytes,10,opt,name=gateway_info,json=gatewayInfo,proto3" json:"gateway_info,omitempty"`
    	// contains filtered or unexported fields
    }

Transaction data associated with a payment protected by reCAPTCHA.

### func (*TransactionData) Descriptor 
    
    
    func (*TransactionData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionData.ProtoReflect.Descriptor instead.

### func (*TransactionData) GetBillingAddress 
    
    
    func (x *TransactionData) GetBillingAddress() *TransactionData_Address

### func (*TransactionData) GetCardBin 
    
    
    func (x *TransactionData) GetCardBin() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData) GetCardLastFour 
    
    
    func (x *TransactionData) GetCardLastFour() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData) GetCurrencyCode 
    
    
    func (x *TransactionData) GetCurrencyCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData) GetGatewayInfo 
    
    
    func (x *TransactionData) GetGatewayInfo() *TransactionData_GatewayInfo

### func (*TransactionData) GetItems 
    
    
    func (x *TransactionData) GetItems() []*TransactionData_Item

### func (*TransactionData) GetMerchants 
    
    
    func (x *TransactionData) GetMerchants() []*TransactionData_User

### func (*TransactionData) GetPaymentMethod 
    
    
    func (x *TransactionData) GetPaymentMethod() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData) GetShippingAddress 
    
    
    func (x *TransactionData) GetShippingAddress() *TransactionData_Address

### func (*TransactionData) GetShippingValue 
    
    
    func (x *TransactionData) GetShippingValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*TransactionData) GetTransactionId 
    
    
    func (x *TransactionData) GetTransactionId() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData) GetUser 
    
    
    func (x *TransactionData) GetUser() *TransactionData_User

### func (*TransactionData) GetValue 
    
    
    func (x *TransactionData) GetValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*TransactionData) ProtoMessage 
    
    
    func (*TransactionData) ProtoMessage()

### func (*TransactionData) ProtoReflect 
    
    
    func (x *TransactionData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionData) Reset 
    
    
    func (x *TransactionData) Reset()

### func (*TransactionData) String 
    
    
    func (x *TransactionData) String() [string](https://pkg.go.dev/builtin#string)

## TransactionData_Address
    
    
    type TransactionData_Address struct {
    
    	// The recipient name, potentially including information such as "care of".
    	Recipient [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=recipient,proto3" json:"recipient,omitempty"`
    	// The first lines of the address. The first line generally contains the
    	// street name and number, and further lines may include information such as
    	// an apartment number.
    	Address [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=address,proto3" json:"address,omitempty"`
    	// The town/city of the address.
    	Locality [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=locality,proto3" json:"locality,omitempty"`
    	// The state, province, or otherwise administrative area of the address.
    	AdministrativeArea [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=administrative_area,json=administrativeArea,proto3" json:"administrative_area,omitempty"`
    	// The CLDR country/region of the address.
    	RegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=region_code,json=regionCode,proto3" json:"region_code,omitempty"`
    	// The postal or ZIP code of the address.
    	PostalCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=postal_code,json=postalCode,proto3" json:"postal_code,omitempty"`
    	// contains filtered or unexported fields
    }

Structured address format for billing and shipping addresses.

### func (*TransactionData_Address) Descriptor 
    
    
    func (*TransactionData_Address) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionData_Address.ProtoReflect.Descriptor instead.

### func (*TransactionData_Address) GetAddress 
    
    
    func (x *TransactionData_Address) GetAddress() [][string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) GetAdministrativeArea 
    
    
    func (x *TransactionData_Address) GetAdministrativeArea() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) GetLocality 
    
    
    func (x *TransactionData_Address) GetLocality() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) GetPostalCode 
    
    
    func (x *TransactionData_Address) GetPostalCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) GetRecipient 
    
    
    func (x *TransactionData_Address) GetRecipient() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) GetRegionCode 
    
    
    func (x *TransactionData_Address) GetRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Address) ProtoMessage 
    
    
    func (*TransactionData_Address) ProtoMessage()

### func (*TransactionData_Address) ProtoReflect 
    
    
    func (x *TransactionData_Address) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionData_Address) Reset 
    
    
    func (x *TransactionData_Address) Reset()

### func (*TransactionData_Address) String 
    
    
    func (x *TransactionData_Address) String() [string](https://pkg.go.dev/builtin#string)

## TransactionData_GatewayInfo
    
    
    type TransactionData_GatewayInfo struct {
    
    	// Name of the gateway service (for example, stripe, square, paypal).
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Gateway response code describing the state of the transaction.
    	GatewayResponseCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=gateway_response_code,json=gatewayResponseCode,proto3" json:"gateway_response_code,omitempty"`
    	// AVS response code from the gateway
    	// (available only when reCAPTCHA is called after authorization).
    	AvsResponseCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=avs_response_code,json=avsResponseCode,proto3" json:"avs_response_code,omitempty"`
    	// CVV response code from the gateway
    	// (available only when reCAPTCHA is called after authorization).
    	CvvResponseCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=cvv_response_code,json=cvvResponseCode,proto3" json:"cvv_response_code,omitempty"`
    	// contains filtered or unexported fields
    }

Details about the transaction from the gateway.

### func (*TransactionData_GatewayInfo) Descriptor 
    
    
    func (*TransactionData_GatewayInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionData_GatewayInfo.ProtoReflect.Descriptor instead.

### func (*TransactionData_GatewayInfo) GetAvsResponseCode 
    
    
    func (x *TransactionData_GatewayInfo) GetAvsResponseCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_GatewayInfo) GetCvvResponseCode 
    
    
    func (x *TransactionData_GatewayInfo) GetCvvResponseCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_GatewayInfo) GetGatewayResponseCode 
    
    
    func (x *TransactionData_GatewayInfo) GetGatewayResponseCode() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_GatewayInfo) GetName 
    
    
    func (x *TransactionData_GatewayInfo) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_GatewayInfo) ProtoMessage 
    
    
    func (*TransactionData_GatewayInfo) ProtoMessage()

### func (*TransactionData_GatewayInfo) ProtoReflect 
    
    
    func (x *TransactionData_GatewayInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionData_GatewayInfo) Reset 
    
    
    func (x *TransactionData_GatewayInfo) Reset()

### func (*TransactionData_GatewayInfo) String 
    
    
    func (x *TransactionData_GatewayInfo) String() [string](https://pkg.go.dev/builtin#string)

## TransactionData_Item
    
    
    type TransactionData_Item struct {
    
    	// The full name of the item.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The value per item that the user is paying, in the transaction currency,
    	// after discounts.
    	Value [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=value,proto3" json:"value,omitempty"`
    	// The quantity of this item that is being purchased.
    	Quantity [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=quantity,proto3" json:"quantity,omitempty"`
    	// When a merchant is specified, its corresponding account_id. Necessary to
    	// populate marketplace-style transactions.
    	MerchantAccountId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=merchant_account_id,json=merchantAccountId,proto3" json:"merchant_account_id,omitempty"`
    	// contains filtered or unexported fields
    }

Line items being purchased in this transaction.

### func (*TransactionData_Item) Descriptor 
    
    
    func (*TransactionData_Item) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionData_Item.ProtoReflect.Descriptor instead.

### func (*TransactionData_Item) GetMerchantAccountId 
    
    
    func (x *TransactionData_Item) GetMerchantAccountId() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Item) GetName 
    
    
    func (x *TransactionData_Item) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_Item) GetQuantity 
    
    
    func (x *TransactionData_Item) GetQuantity() [int64](https://pkg.go.dev/builtin#int64)

### func (*TransactionData_Item) GetValue 
    
    
    func (x *TransactionData_Item) GetValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*TransactionData_Item) ProtoMessage 
    
    
    func (*TransactionData_Item) ProtoMessage()

### func (*TransactionData_Item) ProtoReflect 
    
    
    func (x *TransactionData_Item) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionData_Item) Reset 
    
    
    func (x *TransactionData_Item) Reset()

### func (*TransactionData_Item) String 
    
    
    func (x *TransactionData_Item) String() [string](https://pkg.go.dev/builtin#string)

## TransactionData_User
    
    
    type TransactionData_User struct {
    
    	// Unique account identifier for this user. If using account defender,
    	// this should match the hashed_account_id field. Otherwise, a unique and
    	// persistent identifier for this account.
    	AccountId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
    	// The epoch milliseconds of the user's account creation.
    	CreationMs [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=creation_ms,json=creationMs,proto3" json:"creation_ms,omitempty"`
    	// The email address of the user.
    	Email [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=email,proto3" json:"email,omitempty"`
    	// Whether the email has been verified to be accessible by the user (OTP or
    	// similar).
    	EmailVerified [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=email_verified,json=emailVerified,proto3" json:"email_verified,omitempty"`
    	// The phone number of the user, with country code.
    	PhoneNumber [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=phone_number,json=phoneNumber,proto3" json:"phone_number,omitempty"`
    	// Whether the phone number has been verified to be accessible by the user
    	// (OTP or similar).
    	PhoneVerified [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=phone_verified,json=phoneVerified,proto3" json:"phone_verified,omitempty"`
    	// contains filtered or unexported fields
    }

Details about a user's account involved in the transaction.

### func (*TransactionData_User) Descriptor 
    
    
    func (*TransactionData_User) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionData_User.ProtoReflect.Descriptor instead.

### func (*TransactionData_User) GetAccountId 
    
    
    func (x *TransactionData_User) GetAccountId() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_User) GetCreationMs 
    
    
    func (x *TransactionData_User) GetCreationMs() [int64](https://pkg.go.dev/builtin#int64)

### func (*TransactionData_User) GetEmail 
    
    
    func (x *TransactionData_User) GetEmail() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_User) GetEmailVerified 
    
    
    func (x *TransactionData_User) GetEmailVerified() [bool](https://pkg.go.dev/builtin#bool)

### func (*TransactionData_User) GetPhoneNumber 
    
    
    func (x *TransactionData_User) GetPhoneNumber() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionData_User) GetPhoneVerified 
    
    
    func (x *TransactionData_User) GetPhoneVerified() [bool](https://pkg.go.dev/builtin#bool)

### func (*TransactionData_User) ProtoMessage 
    
    
    func (*TransactionData_User) ProtoMessage()

### func (*TransactionData_User) ProtoReflect 
    
    
    func (x *TransactionData_User) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionData_User) Reset 
    
    
    func (x *TransactionData_User) Reset()

### func (*TransactionData_User) String 
    
    
    func (x *TransactionData_User) String() [string](https://pkg.go.dev/builtin#string)

## TransactionEvent
    
    
    type TransactionEvent struct {
    
    	// Optional. The type of this transaction event.
    	EventType TransactionEvent_TransactionEventType `protobuf:"varint,1,opt,name=event_type,json=eventType,proto3,enum=google.cloud.recaptchaenterprise.v1beta1.TransactionEvent_TransactionEventType" json:"event_type,omitempty"`
    	// Optional. The reason or standardized code that corresponds with this
    	// transaction event, if one exists. For example, a CHARGEBACK event with code
    	// 6005.
    	Reason [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
    	// Optional. The value that corresponds with this transaction event, if one
    	// exists. For example, a refund event where $5.00 was refunded. Currency is
    	// obtained from the original transaction data.
    	Value [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=value,proto3" json:"value,omitempty"`
    	// Optional. Timestamp when this transaction event occurred; otherwise assumed
    	// to be the time of the API call.
    	EventTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=event_time,json=eventTime,proto3" json:"event_time,omitempty"`
    	// contains filtered or unexported fields
    }

Describes an event in the lifecycle of a payment transaction.

### func (*TransactionEvent) Descriptor 
    
    
    func (*TransactionEvent) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionEvent.ProtoReflect.Descriptor instead.

### func (*TransactionEvent) GetEventTime 
    
    
    func (x *TransactionEvent) GetEventTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TransactionEvent) GetEventType 
    
    
    func (x *TransactionEvent) GetEventType() TransactionEvent_TransactionEventType

### func (*TransactionEvent) GetReason 
    
    
    func (x *TransactionEvent) GetReason() [string](https://pkg.go.dev/builtin#string)

### func (*TransactionEvent) GetValue 
    
    
    func (x *TransactionEvent) GetValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*TransactionEvent) ProtoMessage 
    
    
    func (*TransactionEvent) ProtoMessage()

### func (*TransactionEvent) ProtoReflect 
    
    
    func (x *TransactionEvent) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TransactionEvent) Reset 
    
    
    func (x *TransactionEvent) Reset()

### func (*TransactionEvent) String 
    
    
    func (x *TransactionEvent) String() [string](https://pkg.go.dev/builtin#string)

## TransactionEvent_TransactionEventType
    
    
    type TransactionEvent_TransactionEventType [int32](https://pkg.go.dev/builtin#int32)

Enum that represents an event in the payment transaction lifecycle.

### TransactionEvent_TRANSACTION_EVENT_TYPE_UNSPECIFIED, TransactionEvent_MERCHANT_APPROVE, TransactionEvent_MERCHANT_DENY, TransactionEvent_MANUAL_REVIEW, TransactionEvent_AUTHORIZATION, TransactionEvent_AUTHORIZATION_DECLINE, TransactionEvent_PAYMENT_CAPTURE, TransactionEvent_PAYMENT_CAPTURE_DECLINE, TransactionEvent_CANCEL, TransactionEvent_CHARGEBACK_INQUIRY, TransactionEvent_CHARGEBACK_ALERT, TransactionEvent_FRAUD_NOTIFICATION, TransactionEvent_CHARGEBACK, TransactionEvent_CHARGEBACK_REPRESENTMENT, TransactionEvent_CHARGEBACK_REVERSE, TransactionEvent_REFUND_REQUEST, TransactionEvent_REFUND_DECLINE, TransactionEvent_REFUND, TransactionEvent_REFUND_REVERSE
    
    
    const (
    	// Default, unspecified event type.
    	TransactionEvent_TRANSACTION_EVENT_TYPE_UNSPECIFIED TransactionEvent_TransactionEventType = 0
    	// Indicates that the transaction is approved by the merchant. The
    	// accompanying reasons can include terms such as 'INHOUSE', 'ACCERTIFY',
    	// 'CYBERSOURCE', or 'MANUAL_REVIEW'.
    	TransactionEvent_MERCHANT_APPROVE TransactionEvent_TransactionEventType = 1
    	// Indicates that the transaction is denied and concluded due to risks
    	// detected by the merchant. The accompanying reasons can include terms such
    	// as 'INHOUSE',  'ACCERTIFY',  'CYBERSOURCE', or 'MANUAL_REVIEW'.
    	TransactionEvent_MERCHANT_DENY TransactionEvent_TransactionEventType = 2
    	// Indicates that the transaction is being evaluated by a human, due to
    	// suspicion or risk.
    	TransactionEvent_MANUAL_REVIEW TransactionEvent_TransactionEventType = 3
    	// Indicates that the authorization attempt with the card issuer succeeded.
    	TransactionEvent_AUTHORIZATION TransactionEvent_TransactionEventType = 4
    	// Indicates that the authorization attempt with the card issuer failed.
    	// The accompanying reasons can include Visa's '54' indicating that the card
    	// is expired, or '82' indicating that the CVV is incorrect.
    	TransactionEvent_AUTHORIZATION_DECLINE TransactionEvent_TransactionEventType = 5
    	// Indicates that the transaction is completed because the funds were
    	// settled.
    	TransactionEvent_PAYMENT_CAPTURE TransactionEvent_TransactionEventType = 6
    	// Indicates that the transaction could not be completed because the funds
    	// were not settled.
    	TransactionEvent_PAYMENT_CAPTURE_DECLINE TransactionEvent_TransactionEventType = 7
    	// Indicates that the transaction has been canceled. Specify the reason
    	// for the cancellation. For example, 'INSUFFICIENT_INVENTORY'.
    	TransactionEvent_CANCEL TransactionEvent_TransactionEventType = 8
    	// Indicates that the merchant has received a chargeback inquiry due to
    	// fraud for the transaction, requesting additional information before a
    	// fraud chargeback is officially issued and a formal chargeback
    	// notification is sent.
    	TransactionEvent_CHARGEBACK_INQUIRY TransactionEvent_TransactionEventType = 9
    	// Indicates that the merchant has received a chargeback alert due to fraud
    	// for the transaction. The process of resolving the dispute without
    	// involving the payment network is started.
    	TransactionEvent_CHARGEBACK_ALERT TransactionEvent_TransactionEventType = 10
    	// Indicates that a fraud notification is issued for the transaction, sent
    	// by the payment instrument's issuing bank because the transaction appears
    	// to be fraudulent. We recommend including TC40 or SAFE data in the
    	// `reason` field for this event type. For partial chargebacks, we recommend
    	// that you include an amount in the `value` field.
    	TransactionEvent_FRAUD_NOTIFICATION TransactionEvent_TransactionEventType = 11
    	// Indicates that the merchant is informed by the payment network that the
    	// transaction has entered the chargeback process due to fraud. Reason code
    	// examples include Discover's '6005' and '6041'. For partial chargebacks,
    	// we recommend that you include an amount in the `value` field.
    	TransactionEvent_CHARGEBACK TransactionEvent_TransactionEventType = 12
    	// Indicates that the transaction has entered the chargeback process due to
    	// fraud, and that the merchant has chosen to enter representment. Reason
    	// examples include Discover's '6005' and '6041'. For partial chargebacks,
    	// we recommend that you include an amount in the `value` field.
    	TransactionEvent_CHARGEBACK_REPRESENTMENT TransactionEvent_TransactionEventType = 13
    	// Indicates that the transaction has had a fraud chargeback which was
    	// illegitimate and was reversed as a result. For partial chargebacks, we
    	// recommend that you include an amount in the `value` field.
    	TransactionEvent_CHARGEBACK_REVERSE TransactionEvent_TransactionEventType = 14
    	// Indicates that the merchant has received a refund for a completed
    	// transaction. For partial refunds, we recommend that you include an amount
    	// in the `value` field. Reason example: 'TAX_EXEMPT' (partial refund of
    	// exempt tax)
    	TransactionEvent_REFUND_REQUEST TransactionEvent_TransactionEventType = 15
    	// Indicates that the merchant has received a refund request for this
    	// transaction, but that they have declined it. For partial refunds, we
    	// recommend that you include an amount in the `value` field. Reason
    	// example: 'TAX_EXEMPT' (partial refund of exempt tax)
    	TransactionEvent_REFUND_DECLINE TransactionEvent_TransactionEventType = 16
    	// Indicates that the completed transaction was refunded by the merchant.
    	// For partial refunds, we recommend that you include an amount in the
    	// `value` field. Reason example: 'TAX_EXEMPT' (partial refund of exempt
    	// tax)
    	TransactionEvent_REFUND TransactionEvent_TransactionEventType = 17
    	// Indicates that the completed transaction was refunded by the merchant,
    	// and that this refund was reversed. For partial refunds, we recommend that
    	// you include an amount in the `value` field.
    	TransactionEvent_REFUND_REVERSE TransactionEvent_TransactionEventType = 18
    )

### func (TransactionEvent_TransactionEventType) Descriptor 
    
    
    func (TransactionEvent_TransactionEventType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TransactionEvent_TransactionEventType) Enum 
    
    
    func (x TransactionEvent_TransactionEventType) Enum() *TransactionEvent_TransactionEventType

### func (TransactionEvent_TransactionEventType) EnumDescriptor 
    
    
    func (TransactionEvent_TransactionEventType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TransactionEvent_TransactionEventType.Descriptor instead.

### func (TransactionEvent_TransactionEventType) Number 
    
    
    func (x TransactionEvent_TransactionEventType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TransactionEvent_TransactionEventType) String 
    
    
    func (x TransactionEvent_TransactionEventType) String() [string](https://pkg.go.dev/builtin#string)

### func (TransactionEvent_TransactionEventType) Type 
    
    
    func (TransactionEvent_TransactionEventType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedRecaptchaEnterpriseServiceV1Beta1Server
    
    
    type UnimplementedRecaptchaEnterpriseServiceV1Beta1Server struct {
    }

UnimplementedRecaptchaEnterpriseServiceV1Beta1Server should be embedded to have forward compatible implementations.

### func (UnimplementedRecaptchaEnterpriseServiceV1Beta1Server) AnnotateAssessment 
    
    
    func (UnimplementedRecaptchaEnterpriseServiceV1Beta1Server) AnnotateAssessment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AnnotateAssessmentRequest) (*AnnotateAssessmentResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedRecaptchaEnterpriseServiceV1Beta1Server) CreateAssessment 
    
    
    func (UnimplementedRecaptchaEnterpriseServiceV1Beta1Server) CreateAssessment([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateAssessmentRequest) (*Assessment, [error](https://pkg.go.dev/builtin#error))

## UnsafeRecaptchaEnterpriseServiceV1Beta1Server
    
    
    type UnsafeRecaptchaEnterpriseServiceV1Beta1Server interface {
    	// contains filtered or unexported methods
    }

UnsafeRecaptchaEnterpriseServiceV1Beta1Server may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to RecaptchaEnterpriseServiceV1Beta1Server will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
