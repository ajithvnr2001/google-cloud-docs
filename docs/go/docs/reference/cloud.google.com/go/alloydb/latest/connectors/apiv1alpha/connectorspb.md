---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydb/latest/connectors/apiv1alpha/connectorspb/
title: AlloyDB connectors v1alpha - Package cloud.google.com/go/alloydb/connectors/apiv1alpha/connectorspb (v1.31.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:06.149686+00:00
---

# AlloyDB connectors v1alpha - Package cloud.google.com/go/alloydb/connectors/apiv1alpha/connectorspb (v1.31.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydb/latest/connectors/apiv1alpha/connectorspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  AlloyDB connectors v1alpha - Package cloud.google.com/go/alloydb/connectors/apiv1alpha/connectorspb (v1.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.31.0 (latest)  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.1  1.15.2  1.14.2  1.13.0  1.12.1  1.11.0  1.10.7  1.9.0  1.8.1  1.7.0  1.6.3  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.2.1  0.1.0 

**Alpha**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/alloydb/connectors/apiv1alpha/connectorspb). 

## Variables 

### MetadataExchangeRequest_AuthType_name, MetadataExchangeRequest_AuthType_value
    
    
    var (
    	MetadataExchangeRequest_AuthType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "AUTH_TYPE_UNSPECIFIED",
    		1: "DB_NATIVE",
    		2: "AUTO_IAM",
    	}
    	MetadataExchangeRequest_AuthType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"AUTH_TYPE_UNSPECIFIED": 0,
    		"DB_NATIVE":             1,
    		"AUTO_IAM":              2,
    	}
    )

Enum value maps for MetadataExchangeRequest_AuthType.

### MetadataExchangeResponse_ResponseCode_name, MetadataExchangeResponse_ResponseCode_value
    
    
    var (
    	MetadataExchangeResponse_ResponseCode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RESPONSE_CODE_UNSPECIFIED",
    		1: "OK",
    		2: "ERROR",
    	}
    	MetadataExchangeResponse_ResponseCode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RESPONSE_CODE_UNSPECIFIED": 0,
    		"OK":                        1,
    		"ERROR":                     2,
    	}
    )

Enum value maps for MetadataExchangeResponse_ResponseCode.

### File_google_cloud_alloydb_connectors_v1alpha_resources_proto
    
    
    var File_google_cloud_alloydb_connectors_v1alpha_resources_proto protoreflect.FileDescriptor

## MetadataExchangeRequest
    
    
    type MetadataExchangeRequest struct {
    
    	// Optional. Connector information.
    	UserAgent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=user_agent,json=userAgent,proto3" json:"user_agent,omitempty"`
    	// Authentication type.
    	AuthType MetadataExchangeRequest_AuthType `protobuf:"varint,2,opt,name=auth_type,json=authType,proto3,enum=google.cloud.alloydb.connectors.v1alpha.MetadataExchangeRequest_AuthType" json:"auth_type,omitempty"`
    	// IAM token used for both IAM user authentiation and
    	// `alloydb.instances.connect` permission check.
    	Oauth2Token [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=oauth2_token,json=oauth2Token,proto3" json:"oauth2_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message used by AlloyDB connectors to exchange client and connection metadata with the server after a successful TLS handshake. This metadata includes an IAM token, which is used to authenticate users based on their IAM identity. The sole purpose of this message is for the use of AlloyDB connectors. Clients should not rely on this message directly as there can be breaking changes in the future.

### func (*MetadataExchangeRequest) Descriptor 
    
    
    func (*MetadataExchangeRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MetadataExchangeRequest.ProtoReflect.Descriptor instead.

### func (*MetadataExchangeRequest) GetAuthType 
    
    
    func (x *MetadataExchangeRequest) GetAuthType() MetadataExchangeRequest_AuthType

### func (*MetadataExchangeRequest) GetOauth2Token 
    
    
    func (x *MetadataExchangeRequest) GetOauth2Token() [string](https://pkg.go.dev/builtin#string)

### func (*MetadataExchangeRequest) GetUserAgent 
    
    
    func (x *MetadataExchangeRequest) GetUserAgent() [string](https://pkg.go.dev/builtin#string)

### func (*MetadataExchangeRequest) ProtoMessage 
    
    
    func (*MetadataExchangeRequest) ProtoMessage()

### func (*MetadataExchangeRequest) ProtoReflect 
    
    
    func (x *MetadataExchangeRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MetadataExchangeRequest) Reset 
    
    
    func (x *MetadataExchangeRequest) Reset()

### func (*MetadataExchangeRequest) String 
    
    
    func (x *MetadataExchangeRequest) String() [string](https://pkg.go.dev/builtin#string)

## MetadataExchangeRequest_AuthType
    
    
    type MetadataExchangeRequest_AuthType [int32](https://pkg.go.dev/builtin#int32)

AuthType contains all supported authentication types.

### MetadataExchangeRequest_AUTH_TYPE_UNSPECIFIED, MetadataExchangeRequest_DB_NATIVE, MetadataExchangeRequest_AUTO_IAM
    
    
    const (
    	// Authentication type is unspecified and DB_NATIVE is used by default
    	MetadataExchangeRequest_AUTH_TYPE_UNSPECIFIED MetadataExchangeRequest_AuthType = 0
    	// Database native authentication (user/password)
    	MetadataExchangeRequest_DB_NATIVE MetadataExchangeRequest_AuthType = 1
    	// Automatic IAM authentication
    	MetadataExchangeRequest_AUTO_IAM MetadataExchangeRequest_AuthType = 2
    )

### func (MetadataExchangeRequest_AuthType) Descriptor 
    
    
    func (MetadataExchangeRequest_AuthType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MetadataExchangeRequest_AuthType) Enum 
    
    
    func (x MetadataExchangeRequest_AuthType) Enum() *MetadataExchangeRequest_AuthType

### func (MetadataExchangeRequest_AuthType) EnumDescriptor 
    
    
    func (MetadataExchangeRequest_AuthType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MetadataExchangeRequest_AuthType.Descriptor instead.

### func (MetadataExchangeRequest_AuthType) Number 
    
    
    func (x MetadataExchangeRequest_AuthType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MetadataExchangeRequest_AuthType) String 
    
    
    func (x MetadataExchangeRequest_AuthType) String() [string](https://pkg.go.dev/builtin#string)

### func (MetadataExchangeRequest_AuthType) Type 
    
    
    func (MetadataExchangeRequest_AuthType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MetadataExchangeResponse
    
    
    type MetadataExchangeResponse struct {
    
    	// Response code.
    	ResponseCode MetadataExchangeResponse_ResponseCode `protobuf:"varint,1,opt,name=response_code,json=responseCode,proto3,enum=google.cloud.alloydb.connectors.v1alpha.MetadataExchangeResponse_ResponseCode" json:"response_code,omitempty"`
    	// Optional. Error message.
    	Error [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=error,proto3" json:"error,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to metadata exchange request. The sole purpose of this message is for the use of AlloyDB connectors. Clients should not rely on this message directly as there can be breaking changes in the future.

### func (*MetadataExchangeResponse) Descriptor 
    
    
    func (*MetadataExchangeResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MetadataExchangeResponse.ProtoReflect.Descriptor instead.

### func (*MetadataExchangeResponse) GetError 
    
    
    func (x *MetadataExchangeResponse) GetError() [string](https://pkg.go.dev/builtin#string)

### func (*MetadataExchangeResponse) GetResponseCode 
    
    
    func (x *MetadataExchangeResponse) GetResponseCode() MetadataExchangeResponse_ResponseCode

### func (*MetadataExchangeResponse) ProtoMessage 
    
    
    func (*MetadataExchangeResponse) ProtoMessage()

### func (*MetadataExchangeResponse) ProtoReflect 
    
    
    func (x *MetadataExchangeResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MetadataExchangeResponse) Reset 
    
    
    func (x *MetadataExchangeResponse) Reset()

### func (*MetadataExchangeResponse) String 
    
    
    func (x *MetadataExchangeResponse) String() [string](https://pkg.go.dev/builtin#string)

## MetadataExchangeResponse_ResponseCode
    
    
    type MetadataExchangeResponse_ResponseCode [int32](https://pkg.go.dev/builtin#int32)

Response code.

### MetadataExchangeResponse_RESPONSE_CODE_UNSPECIFIED, MetadataExchangeResponse_OK, MetadataExchangeResponse_ERROR
    
    
    const (
    	// Unknown response code
    	MetadataExchangeResponse_RESPONSE_CODE_UNSPECIFIED MetadataExchangeResponse_ResponseCode = 0
    	// Success
    	MetadataExchangeResponse_OK MetadataExchangeResponse_ResponseCode = 1
    	// Failure
    	MetadataExchangeResponse_ERROR MetadataExchangeResponse_ResponseCode = 2
    )

### func (MetadataExchangeResponse_ResponseCode) Descriptor 
    
    
    func (MetadataExchangeResponse_ResponseCode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MetadataExchangeResponse_ResponseCode) Enum 
    
    
    func (x MetadataExchangeResponse_ResponseCode) Enum() *MetadataExchangeResponse_ResponseCode

### func (MetadataExchangeResponse_ResponseCode) EnumDescriptor 
    
    
    func (MetadataExchangeResponse_ResponseCode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MetadataExchangeResponse_ResponseCode.Descriptor instead.

### func (MetadataExchangeResponse_ResponseCode) Number 
    
    
    func (x MetadataExchangeResponse_ResponseCode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MetadataExchangeResponse_ResponseCode) String 
    
    
    func (x MetadataExchangeResponse_ResponseCode) String() [string](https://pkg.go.dev/builtin#string)

### func (MetadataExchangeResponse_ResponseCode) Type 
    
    
    func (MetadataExchangeResponse_ResponseCode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
