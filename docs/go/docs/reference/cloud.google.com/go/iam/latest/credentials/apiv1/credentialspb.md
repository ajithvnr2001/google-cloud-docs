---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/credentials/apiv1/credentialspb/
title: IAM Service Account Credentials API v1 - Package cloud.google.com/go/iam/credentials/apiv1/credentialspb (v1.14.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:53.193302+00:00
---

# IAM Service Account Credentials API v1 - Package cloud.google.com/go/iam/credentials/apiv1/credentialspb (v1.14.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/credentials/apiv1/credentialspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  IAM Service Account Credentials API v1 - Package cloud.google.com/go/iam/credentials/apiv1/credentialspb (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.3  1.4.2  1.3.1  1.2.2  1.1.13  1.0.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/iam/credentials/apiv1/credentialspb). 

##  Constants 

### IAMCredentials_GenerateAccessToken_FullMethodName, IAMCredentials_GenerateIdToken_FullMethodName, IAMCredentials_SignBlob_FullMethodName, IAMCredentials_SignJwt_FullMethodName
    
    
    const (
    	IAMCredentials_GenerateAccessToken_FullMethodName = "/google.iam.credentials.v1.IAMCredentials/GenerateAccessToken"
    	IAMCredentials_GenerateIdToken_FullMethodName     = "/google.iam.credentials.v1.IAMCredentials/GenerateIdToken"
    	IAMCredentials_SignBlob_FullMethodName            = "/google.iam.credentials.v1.IAMCredentials/SignBlob"
    	IAMCredentials_SignJwt_FullMethodName             = "/google.iam.credentials.v1.IAMCredentials/SignJwt"
    )

## Variables 

### File_google_iam_credentials_v1_common_proto
    
    
    var File_google_iam_credentials_v1_common_proto protoreflect.FileDescriptor

### File_google_iam_credentials_v1_iamcredentials_proto
    
    
    var File_google_iam_credentials_v1_iamcredentials_proto protoreflect.FileDescriptor

### IAMCredentials_ServiceDesc
    
    
    var IAMCredentials_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.iam.credentials.v1.IAMCredentials",
    	HandlerType: (*IAMCredentialsServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GenerateAccessToken",
    			Handler:    _IAMCredentials_GenerateAccessToken_Handler,
    		},
    		{
    			MethodName: "GenerateIdToken",
    			Handler:    _IAMCredentials_GenerateIdToken_Handler,
    		},
    		{
    			MethodName: "SignBlob",
    			Handler:    _IAMCredentials_SignBlob_Handler,
    		},
    		{
    			MethodName: "SignJwt",
    			Handler:    _IAMCredentials_SignJwt_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/iam/credentials/v1/iamcredentials.proto",
    }

IAMCredentials_ServiceDesc is the grpc.ServiceDesc for IAMCredentials service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterIAMCredentialsServer 
    
    
    func RegisterIAMCredentialsServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv IAMCredentialsServer)

## GenerateAccessTokenRequest
    
    
    type GenerateAccessTokenRequest struct {
    
    	// Required. The resource name of the service account for which the credentials
    	// are requested, in the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The sequence of service accounts in a delegation chain. Each service
    	// account must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on its next service account in the chain. The last service account in the
    	// chain must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on the service account that is specified in the `name` field of the
    	// request.
    	//
    	// The delegates must have the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Delegates [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=delegates,proto3" json:"delegates,omitempty"`
    	// Required. Code to identify the scopes to be included in the OAuth 2.0 access token.
    	// See https://developers.google.com/identity/protocols/googlescopes for more
    	// information.
    	// At least one value required.
    	Scope [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=scope,proto3" json:"scope,omitempty"`
    	// The desired lifetime duration of the access token in seconds.
    	// Must be set to a value less than or equal to 3600 (1 hour). If a value is
    	// not specified, the token's lifetime will be set to a default value of one
    	// hour.
    	Lifetime *durationpb.Duration `protobuf:"bytes,7,opt,name=lifetime,proto3" json:"lifetime,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*GenerateAccessTokenRequest) Descriptor 
    
    
    func (*GenerateAccessTokenRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAccessTokenRequest.ProtoReflect.Descriptor instead.

### func (*GenerateAccessTokenRequest) GetDelegates 
    
    
    func (x *GenerateAccessTokenRequest) GetDelegates() [][string](https://pkg.go.dev/builtin#string)

### func (*GenerateAccessTokenRequest) GetLifetime 
    
    
    func (x *GenerateAccessTokenRequest) GetLifetime() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*GenerateAccessTokenRequest) GetName 
    
    
    func (x *GenerateAccessTokenRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAccessTokenRequest) GetScope 
    
    
    func (x *GenerateAccessTokenRequest) GetScope() [][string](https://pkg.go.dev/builtin#string)

### func (*GenerateAccessTokenRequest) ProtoMessage 
    
    
    func (*GenerateAccessTokenRequest) ProtoMessage()

### func (*GenerateAccessTokenRequest) ProtoReflect 
    
    
    func (x *GenerateAccessTokenRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateAccessTokenRequest) Reset 
    
    
    func (x *GenerateAccessTokenRequest) Reset()

### func (*GenerateAccessTokenRequest) String 
    
    
    func (x *GenerateAccessTokenRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateAccessTokenResponse
    
    
    type GenerateAccessTokenResponse struct {
    
    	// The OAuth 2.0 access token.
    	AccessToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=access_token,json=accessToken,proto3" json:"access_token,omitempty"`
    	// Token expiration time.
    	// The expiration time is always set.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=expire_time,json=expireTime,proto3" json:"expire_time,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*GenerateAccessTokenResponse) Descriptor 
    
    
    func (*GenerateAccessTokenResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateAccessTokenResponse.ProtoReflect.Descriptor instead.

### func (*GenerateAccessTokenResponse) GetAccessToken 
    
    
    func (x *GenerateAccessTokenResponse) GetAccessToken() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateAccessTokenResponse) GetExpireTime 
    
    
    func (x *GenerateAccessTokenResponse) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*GenerateAccessTokenResponse) ProtoMessage 
    
    
    func (*GenerateAccessTokenResponse) ProtoMessage()

### func (*GenerateAccessTokenResponse) ProtoReflect 
    
    
    func (x *GenerateAccessTokenResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateAccessTokenResponse) Reset 
    
    
    func (x *GenerateAccessTokenResponse) Reset()

### func (*GenerateAccessTokenResponse) String 
    
    
    func (x *GenerateAccessTokenResponse) String() [string](https://pkg.go.dev/builtin#string)

## GenerateIdTokenRequest
    
    
    type GenerateIdTokenRequest struct {
    
    	// Required. The resource name of the service account for which the credentials
    	// are requested, in the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The sequence of service accounts in a delegation chain. Each service
    	// account must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on its next service account in the chain. The last service account in the
    	// chain must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on the service account that is specified in the `name` field of the
    	// request.
    	//
    	// The delegates must have the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Delegates [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=delegates,proto3" json:"delegates,omitempty"`
    	// Required. The audience for the token, such as the API or account that this token
    	// grants access to.
    	Audience [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=audience,proto3" json:"audience,omitempty"`
    	// Include the service account email in the token. If set to `true`, the
    	// token will contain `email` and `email_verified` claims.
    	IncludeEmail [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=include_email,json=includeEmail,proto3" json:"include_email,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*GenerateIdTokenRequest) Descriptor 
    
    
    func (*GenerateIdTokenRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateIdTokenRequest.ProtoReflect.Descriptor instead.

### func (*GenerateIdTokenRequest) GetAudience 
    
    
    func (x *GenerateIdTokenRequest) GetAudience() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateIdTokenRequest) GetDelegates 
    
    
    func (x *GenerateIdTokenRequest) GetDelegates() [][string](https://pkg.go.dev/builtin#string)

### func (*GenerateIdTokenRequest) GetIncludeEmail 
    
    
    func (x *GenerateIdTokenRequest) GetIncludeEmail() [bool](https://pkg.go.dev/builtin#bool)

### func (*GenerateIdTokenRequest) GetName 
    
    
    func (x *GenerateIdTokenRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateIdTokenRequest) ProtoMessage 
    
    
    func (*GenerateIdTokenRequest) ProtoMessage()

### func (*GenerateIdTokenRequest) ProtoReflect 
    
    
    func (x *GenerateIdTokenRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateIdTokenRequest) Reset 
    
    
    func (x *GenerateIdTokenRequest) Reset()

### func (*GenerateIdTokenRequest) String 
    
    
    func (x *GenerateIdTokenRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateIdTokenResponse
    
    
    type GenerateIdTokenResponse struct {
    
    	// The OpenId Connect ID token.
    	Token [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*GenerateIdTokenResponse) Descriptor 
    
    
    func (*GenerateIdTokenResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateIdTokenResponse.ProtoReflect.Descriptor instead.

### func (*GenerateIdTokenResponse) GetToken 
    
    
    func (x *GenerateIdTokenResponse) GetToken() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateIdTokenResponse) ProtoMessage 
    
    
    func (*GenerateIdTokenResponse) ProtoMessage()

### func (*GenerateIdTokenResponse) ProtoReflect 
    
    
    func (x *GenerateIdTokenResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateIdTokenResponse) Reset 
    
    
    func (x *GenerateIdTokenResponse) Reset()

### func (*GenerateIdTokenResponse) String 
    
    
    func (x *GenerateIdTokenResponse) String() [string](https://pkg.go.dev/builtin#string)

## IAMCredentialsClient
    
    
    type IAMCredentialsClient interface {
    	// Generates an OAuth 2.0 access token for a service account.
    	GenerateAccessToken(ctx context.Context, in *GenerateAccessTokenRequest, opts ...grpc.CallOption) (*GenerateAccessTokenResponse, [error](https://pkg.go.dev/builtin#error))
    	// Generates an OpenID Connect ID token for a service account.
    	GenerateIdToken(ctx context.Context, in *GenerateIdTokenRequest, opts ...grpc.CallOption) (*GenerateIdTokenResponse, [error](https://pkg.go.dev/builtin#error))
    	// Signs a blob using a service account's system-managed private key.
    	SignBlob(ctx context.Context, in *SignBlobRequest, opts ...grpc.CallOption) (*SignBlobResponse, [error](https://pkg.go.dev/builtin#error))
    	// Signs a JWT using a service account's system-managed private key.
    	SignJwt(ctx context.Context, in *SignJwtRequest, opts ...grpc.CallOption) (*SignJwtResponse, [error](https://pkg.go.dev/builtin#error))
    }

IAMCredentialsClient is the client API for IAMCredentials service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewIAMCredentialsClient 
    
    
    func NewIAMCredentialsClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) IAMCredentialsClient

## IAMCredentialsServer
    
    
    type IAMCredentialsServer interface {
    	// Generates an OAuth 2.0 access token for a service account.
    	GenerateAccessToken(context.Context, *GenerateAccessTokenRequest) (*GenerateAccessTokenResponse, [error](https://pkg.go.dev/builtin#error))
    	// Generates an OpenID Connect ID token for a service account.
    	GenerateIdToken(context.Context, *GenerateIdTokenRequest) (*GenerateIdTokenResponse, [error](https://pkg.go.dev/builtin#error))
    	// Signs a blob using a service account's system-managed private key.
    	SignBlob(context.Context, *SignBlobRequest) (*SignBlobResponse, [error](https://pkg.go.dev/builtin#error))
    	// Signs a JWT using a service account's system-managed private key.
    	SignJwt(context.Context, *SignJwtRequest) (*SignJwtResponse, [error](https://pkg.go.dev/builtin#error))
    }

IAMCredentialsServer is the server API for IAMCredentials service. All implementations should embed UnimplementedIAMCredentialsServer for forward compatibility

## SignBlobRequest
    
    
    type SignBlobRequest struct {
    
    	// Required. The resource name of the service account for which the credentials
    	// are requested, in the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The sequence of service accounts in a delegation chain. Each service
    	// account must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on its next service account in the chain. The last service account in the
    	// chain must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on the service account that is specified in the `name` field of the
    	// request.
    	//
    	// The delegates must have the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Delegates [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=delegates,proto3" json:"delegates,omitempty"`
    	// Required. The bytes to sign.
    	Payload [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,5,opt,name=payload,proto3" json:"payload,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*SignBlobRequest) Descriptor 
    
    
    func (*SignBlobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SignBlobRequest.ProtoReflect.Descriptor instead.

### func (*SignBlobRequest) GetDelegates 
    
    
    func (x *SignBlobRequest) GetDelegates() [][string](https://pkg.go.dev/builtin#string)

### func (*SignBlobRequest) GetName 
    
    
    func (x *SignBlobRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SignBlobRequest) GetPayload 
    
    
    func (x *SignBlobRequest) GetPayload() [][byte](https://pkg.go.dev/builtin#byte)

### func (*SignBlobRequest) ProtoMessage 
    
    
    func (*SignBlobRequest) ProtoMessage()

### func (*SignBlobRequest) ProtoReflect 
    
    
    func (x *SignBlobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SignBlobRequest) Reset 
    
    
    func (x *SignBlobRequest) Reset()

### func (*SignBlobRequest) String 
    
    
    func (x *SignBlobRequest) String() [string](https://pkg.go.dev/builtin#string)

## SignBlobResponse
    
    
    type SignBlobResponse struct {
    
    	// The ID of the key used to sign the blob.
    	KeyId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key_id,json=keyId,proto3" json:"key_id,omitempty"`
    	// The signed blob.
    	SignedBlob [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,4,opt,name=signed_blob,json=signedBlob,proto3" json:"signed_blob,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*SignBlobResponse) Descriptor 
    
    
    func (*SignBlobResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SignBlobResponse.ProtoReflect.Descriptor instead.

### func (*SignBlobResponse) GetKeyId 
    
    
    func (x *SignBlobResponse) GetKeyId() [string](https://pkg.go.dev/builtin#string)

### func (*SignBlobResponse) GetSignedBlob 
    
    
    func (x *SignBlobResponse) GetSignedBlob() [][byte](https://pkg.go.dev/builtin#byte)

### func (*SignBlobResponse) ProtoMessage 
    
    
    func (*SignBlobResponse) ProtoMessage()

### func (*SignBlobResponse) ProtoReflect 
    
    
    func (x *SignBlobResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SignBlobResponse) Reset 
    
    
    func (x *SignBlobResponse) Reset()

### func (*SignBlobResponse) String 
    
    
    func (x *SignBlobResponse) String() [string](https://pkg.go.dev/builtin#string)

## SignJwtRequest
    
    
    type SignJwtRequest struct {
    
    	// Required. The resource name of the service account for which the credentials
    	// are requested, in the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The sequence of service accounts in a delegation chain. Each service
    	// account must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on its next service account in the chain. The last service account in the
    	// chain must be granted the `roles/iam.serviceAccountTokenCreator` role
    	// on the service account that is specified in the `name` field of the
    	// request.
    	//
    	// The delegates must have the following format:
    	// `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard
    	// character is required; replacing it with a project ID is invalid.
    	Delegates [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=delegates,proto3" json:"delegates,omitempty"`
    	// Required. The JWT payload to sign: a JSON object that contains a JWT Claims Set.
    	Payload [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=payload,proto3" json:"payload,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*SignJwtRequest) Descriptor 
    
    
    func (*SignJwtRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SignJwtRequest.ProtoReflect.Descriptor instead.

### func (*SignJwtRequest) GetDelegates 
    
    
    func (x *SignJwtRequest) GetDelegates() [][string](https://pkg.go.dev/builtin#string)

### func (*SignJwtRequest) GetName 
    
    
    func (x *SignJwtRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*SignJwtRequest) GetPayload 
    
    
    func (x *SignJwtRequest) GetPayload() [string](https://pkg.go.dev/builtin#string)

### func (*SignJwtRequest) ProtoMessage 
    
    
    func (*SignJwtRequest) ProtoMessage()

### func (*SignJwtRequest) ProtoReflect 
    
    
    func (x *SignJwtRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SignJwtRequest) Reset 
    
    
    func (x *SignJwtRequest) Reset()

### func (*SignJwtRequest) String 
    
    
    func (x *SignJwtRequest) String() [string](https://pkg.go.dev/builtin#string)

## SignJwtResponse
    
    
    type SignJwtResponse struct {
    
    	// The ID of the key used to sign the JWT.
    	KeyId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key_id,json=keyId,proto3" json:"key_id,omitempty"`
    	// The signed JWT.
    	SignedJwt [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=signed_jwt,json=signedJwt,proto3" json:"signed_jwt,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*SignJwtResponse) Descriptor 
    
    
    func (*SignJwtResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SignJwtResponse.ProtoReflect.Descriptor instead.

### func (*SignJwtResponse) GetKeyId 
    
    
    func (x *SignJwtResponse) GetKeyId() [string](https://pkg.go.dev/builtin#string)

### func (*SignJwtResponse) GetSignedJwt 
    
    
    func (x *SignJwtResponse) GetSignedJwt() [string](https://pkg.go.dev/builtin#string)

### func (*SignJwtResponse) ProtoMessage 
    
    
    func (*SignJwtResponse) ProtoMessage()

### func (*SignJwtResponse) ProtoReflect 
    
    
    func (x *SignJwtResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SignJwtResponse) Reset 
    
    
    func (x *SignJwtResponse) Reset()

### func (*SignJwtResponse) String 
    
    
    func (x *SignJwtResponse) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedIAMCredentialsServer
    
    
    type UnimplementedIAMCredentialsServer struct {
    }

UnimplementedIAMCredentialsServer should be embedded to have forward compatible implementations.

### func (UnimplementedIAMCredentialsServer) GenerateAccessToken 
    
    
    func (UnimplementedIAMCredentialsServer) GenerateAccessToken([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateAccessTokenRequest) (*GenerateAccessTokenResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedIAMCredentialsServer) GenerateIdToken 
    
    
    func (UnimplementedIAMCredentialsServer) GenerateIdToken([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateIdTokenRequest) (*GenerateIdTokenResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedIAMCredentialsServer) SignBlob 
    
    
    func (UnimplementedIAMCredentialsServer) SignBlob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SignBlobRequest) (*SignBlobResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedIAMCredentialsServer) SignJwt 
    
    
    func (UnimplementedIAMCredentialsServer) SignJwt([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SignJwtRequest) (*SignJwtResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeIAMCredentialsServer
    
    
    type UnsafeIAMCredentialsServer interface {
    	// contains filtered or unexported methods
    }

UnsafeIAMCredentialsServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to IAMCredentialsServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
