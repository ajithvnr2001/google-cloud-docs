---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta2/generativelanguagepb/
title: Generative Language API v1beta2 - Package cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:54.501319+00:00
---

# Generative Language API v1beta2 - Package cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta2/generativelanguagepb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Generative Language API v1beta2 - Package cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1  0.10.2  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.4  0.2.0  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb). 

##  Constants 

### DiscussService_GenerateMessage_FullMethodName, DiscussService_CountMessageTokens_FullMethodName
    
    
    const (
    	DiscussService_GenerateMessage_FullMethodName    = "/google.ai.generativelanguage.v1beta2.DiscussService/GenerateMessage"
    	DiscussService_CountMessageTokens_FullMethodName = "/google.ai.generativelanguage.v1beta2.DiscussService/CountMessageTokens"
    )

### ModelService_GetModel_FullMethodName, ModelService_ListModels_FullMethodName
    
    
    const (
    	ModelService_GetModel_FullMethodName   = "/google.ai.generativelanguage.v1beta2.ModelService/GetModel"
    	ModelService_ListModels_FullMethodName = "/google.ai.generativelanguage.v1beta2.ModelService/ListModels"
    )

### TextService_GenerateText_FullMethodName, TextService_EmbedText_FullMethodName
    
    
    const (
    	TextService_GenerateText_FullMethodName = "/google.ai.generativelanguage.v1beta2.TextService/GenerateText"
    	TextService_EmbedText_FullMethodName    = "/google.ai.generativelanguage.v1beta2.TextService/EmbedText"
    )

## Variables 

### HarmCategory_name, HarmCategory_value
    
    
    var (
    	HarmCategory_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HARM_CATEGORY_UNSPECIFIED",
    		1: "HARM_CATEGORY_DEROGATORY",
    		2: "HARM_CATEGORY_TOXICITY",
    		3: "HARM_CATEGORY_VIOLENCE",
    		4: "HARM_CATEGORY_SEXUAL",
    		5: "HARM_CATEGORY_MEDICAL",
    		6: "HARM_CATEGORY_DANGEROUS",
    	}
    	HarmCategory_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HARM_CATEGORY_UNSPECIFIED": 0,
    		"HARM_CATEGORY_DEROGATORY":  1,
    		"HARM_CATEGORY_TOXICITY":    2,
    		"HARM_CATEGORY_VIOLENCE":    3,
    		"HARM_CATEGORY_SEXUAL":      4,
    		"HARM_CATEGORY_MEDICAL":     5,
    		"HARM_CATEGORY_DANGEROUS":   6,
    	}
    )

Enum value maps for HarmCategory.

### ContentFilter_BlockedReason_name, ContentFilter_BlockedReason_value
    
    
    var (
    	ContentFilter_BlockedReason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "BLOCKED_REASON_UNSPECIFIED",
    		1: "SAFETY",
    		2: "OTHER",
    	}
    	ContentFilter_BlockedReason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"BLOCKED_REASON_UNSPECIFIED": 0,
    		"SAFETY":                     1,
    		"OTHER":                      2,
    	}
    )

Enum value maps for ContentFilter_BlockedReason.

### SafetyRating_HarmProbability_name, SafetyRating_HarmProbability_value
    
    
    var (
    	SafetyRating_HarmProbability_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HARM_PROBABILITY_UNSPECIFIED",
    		1: "NEGLIGIBLE",
    		2: "LOW",
    		3: "MEDIUM",
    		4: "HIGH",
    	}
    	SafetyRating_HarmProbability_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HARM_PROBABILITY_UNSPECIFIED": 0,
    		"NEGLIGIBLE":                   1,
    		"LOW":                          2,
    		"MEDIUM":                       3,
    		"HIGH":                         4,
    	}
    )

Enum value maps for SafetyRating_HarmProbability.

### SafetySetting_HarmBlockThreshold_name, SafetySetting_HarmBlockThreshold_value
    
    
    var (
    	SafetySetting_HarmBlockThreshold_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
    		1: "BLOCK_LOW_AND_ABOVE",
    		2: "BLOCK_MEDIUM_AND_ABOVE",
    		3: "BLOCK_ONLY_HIGH",
    	}
    	SafetySetting_HarmBlockThreshold_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HARM_BLOCK_THRESHOLD_UNSPECIFIED": 0,
    		"BLOCK_LOW_AND_ABOVE":              1,
    		"BLOCK_MEDIUM_AND_ABOVE":           2,
    		"BLOCK_ONLY_HIGH":                  3,
    	}
    )

Enum value maps for SafetySetting_HarmBlockThreshold.

### DiscussService_ServiceDesc
    
    
    var DiscussService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.ai.generativelanguage.v1beta2.DiscussService",
    	HandlerType: (*DiscussServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GenerateMessage",
    			Handler:    _DiscussService_GenerateMessage_Handler,
    		},
    		{
    			MethodName: "CountMessageTokens",
    			Handler:    _DiscussService_CountMessageTokens_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/ai/generativelanguage/v1beta2/discuss_service.proto",
    }

DiscussService_ServiceDesc is the grpc.ServiceDesc for DiscussService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_ai_generativelanguage_v1beta2_citation_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_citation_proto protoreflect.FileDescriptor

### File_google_ai_generativelanguage_v1beta2_discuss_service_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_discuss_service_proto protoreflect.FileDescriptor

### File_google_ai_generativelanguage_v1beta2_model_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_model_proto protoreflect.FileDescriptor

### File_google_ai_generativelanguage_v1beta2_model_service_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_model_service_proto protoreflect.FileDescriptor

### File_google_ai_generativelanguage_v1beta2_safety_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_safety_proto protoreflect.FileDescriptor

### File_google_ai_generativelanguage_v1beta2_text_service_proto
    
    
    var File_google_ai_generativelanguage_v1beta2_text_service_proto protoreflect.FileDescriptor

### ModelService_ServiceDesc
    
    
    var ModelService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.ai.generativelanguage.v1beta2.ModelService",
    	HandlerType: (*ModelServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetModel",
    			Handler:    _ModelService_GetModel_Handler,
    		},
    		{
    			MethodName: "ListModels",
    			Handler:    _ModelService_ListModels_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/ai/generativelanguage/v1beta2/model_service.proto",
    }

ModelService_ServiceDesc is the grpc.ServiceDesc for ModelService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### TextService_ServiceDesc
    
    
    var TextService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.ai.generativelanguage.v1beta2.TextService",
    	HandlerType: (*TextServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GenerateText",
    			Handler:    _TextService_GenerateText_Handler,
    		},
    		{
    			MethodName: "EmbedText",
    			Handler:    _TextService_EmbedText_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/ai/generativelanguage/v1beta2/text_service.proto",
    }

TextService_ServiceDesc is the grpc.ServiceDesc for TextService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterDiscussServiceServer 
    
    
    func RegisterDiscussServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv DiscussServiceServer)

### func RegisterModelServiceServer 
    
    
    func RegisterModelServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv ModelServiceServer)

### func RegisterTextServiceServer 
    
    
    func RegisterTextServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv TextServiceServer)

## CitationMetadata
    
    
    type CitationMetadata struct {
    
    	// Citations to sources for a specific response.
    	CitationSources []*CitationSource `protobuf:"bytes,1,rep,name=citation_sources,json=citationSources,proto3" json:"citation_sources,omitempty"`
    	// contains filtered or unexported fields
    }

A collection of source attributions for a piece of content.

### func (*CitationMetadata) Descriptor 
    
    
    func (*CitationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CitationMetadata.ProtoReflect.Descriptor instead.

### func (*CitationMetadata) GetCitationSources 
    
    
    func (x *CitationMetadata) GetCitationSources() []*CitationSource

### func (*CitationMetadata) ProtoMessage 
    
    
    func (*CitationMetadata) ProtoMessage()

### func (*CitationMetadata) ProtoReflect 
    
    
    func (x *CitationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CitationMetadata) Reset 
    
    
    func (x *CitationMetadata) Reset()

### func (*CitationMetadata) String 
    
    
    func (x *CitationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## CitationSource
    
    
    type CitationSource struct {
    
    	// Optional. Start of segment of the response that is attributed to this
    	// source.
    	//
    	// Index indicates the start of the segment, measured in bytes.
    	StartIndex *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=start_index,json=startIndex,proto3,oneof" json:"start_index,omitempty"`
    	// Optional. End of the attributed segment, exclusive.
    	EndIndex *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=end_index,json=endIndex,proto3,oneof" json:"end_index,omitempty"`
    	// Optional. URI that is attributed as a source for a portion of the text.
    	Uri *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=uri,proto3,oneof" json:"uri,omitempty"`
    	// Optional. License for the GitHub project that is attributed as a source for
    	// segment.
    	//
    	// License info is required for code citations.
    	License *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=license,proto3,oneof" json:"license,omitempty"`
    	// contains filtered or unexported fields
    }

A citation to a source for a portion of a specific response.

### func (*CitationSource) Descriptor 
    
    
    func (*CitationSource) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CitationSource.ProtoReflect.Descriptor instead.

### func (*CitationSource) GetEndIndex 
    
    
    func (x *CitationSource) GetEndIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*CitationSource) GetLicense 
    
    
    func (x *CitationSource) GetLicense() [string](https://pkg.go.dev/builtin#string)

### func (*CitationSource) GetStartIndex 
    
    
    func (x *CitationSource) GetStartIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*CitationSource) GetUri 
    
    
    func (x *CitationSource) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*CitationSource) ProtoMessage 
    
    
    func (*CitationSource) ProtoMessage()

### func (*CitationSource) ProtoReflect 
    
    
    func (x *CitationSource) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CitationSource) Reset 
    
    
    func (x *CitationSource) Reset()

### func (*CitationSource) String 
    
    
    func (x *CitationSource) String() [string](https://pkg.go.dev/builtin#string)

## ContentFilter
    
    
    type ContentFilter struct {
    
    	// The reason content was blocked during request processing.
    	Reason ContentFilter_BlockedReason `protobuf:"varint,1,opt,name=reason,proto3,enum=google.ai.generativelanguage.v1beta2.ContentFilter_BlockedReason" json:"reason,omitempty"`
    	// A string that describes the filtering behavior in more detail.
    	Message *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=message,proto3,oneof" json:"message,omitempty"`
    	// contains filtered or unexported fields
    }

Content filtering metadata associated with processing a single request.

ContentFilter contains a reason and an optional supporting string. The reason may be unspecified.

### func (*ContentFilter) Descriptor 
    
    
    func (*ContentFilter) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContentFilter.ProtoReflect.Descriptor instead.

### func (*ContentFilter) GetMessage 
    
    
    func (x *ContentFilter) GetMessage() [string](https://pkg.go.dev/builtin#string)

### func (*ContentFilter) GetReason 
    
    
    func (x *ContentFilter) GetReason() ContentFilter_BlockedReason

### func (*ContentFilter) ProtoMessage 
    
    
    func (*ContentFilter) ProtoMessage()

### func (*ContentFilter) ProtoReflect 
    
    
    func (x *ContentFilter) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ContentFilter) Reset 
    
    
    func (x *ContentFilter) Reset()

### func (*ContentFilter) String 
    
    
    func (x *ContentFilter) String() [string](https://pkg.go.dev/builtin#string)

## ContentFilter_BlockedReason
    
    
    type ContentFilter_BlockedReason [int32](https://pkg.go.dev/builtin#int32)

A list of reasons why content may have been blocked.

### ContentFilter_BLOCKED_REASON_UNSPECIFIED, ContentFilter_SAFETY, ContentFilter_OTHER
    
    
    const (
    	// A blocked reason was not specified.
    	ContentFilter_BLOCKED_REASON_UNSPECIFIED ContentFilter_BlockedReason = 0
    	// Content was blocked by safety settings.
    	ContentFilter_SAFETY ContentFilter_BlockedReason = 1
    	// Content was blocked, but the reason is uncategorized.
    	ContentFilter_OTHER ContentFilter_BlockedReason = 2
    )

### func (ContentFilter_BlockedReason) Descriptor 
    
    
    func (ContentFilter_BlockedReason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ContentFilter_BlockedReason) Enum 
    
    
    func (x ContentFilter_BlockedReason) Enum() *ContentFilter_BlockedReason

### func (ContentFilter_BlockedReason) EnumDescriptor 
    
    
    func (ContentFilter_BlockedReason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ContentFilter_BlockedReason.Descriptor instead.

### func (ContentFilter_BlockedReason) Number 
    
    
    func (x ContentFilter_BlockedReason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ContentFilter_BlockedReason) String 
    
    
    func (x ContentFilter_BlockedReason) String() [string](https://pkg.go.dev/builtin#string)

### func (ContentFilter_BlockedReason) Type 
    
    
    func (ContentFilter_BlockedReason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CountMessageTokensRequest
    
    
    type CountMessageTokensRequest struct {
    
    	// Required. The model's resource name. This serves as an ID for the Model to
    	// use.
    	//
    	// This name should match a model name returned by the `ListModels` method.
    	//
    	// Format: `models/{model}`
    	Model [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=model,proto3" json:"model,omitempty"`
    	// Required. The prompt, whose token count is to be returned.
    	Prompt *MessagePrompt `protobuf:"bytes,2,opt,name=prompt,proto3" json:"prompt,omitempty"`
    	// contains filtered or unexported fields
    }

Counts the number of tokens in the `prompt` sent to a model.

Models may tokenize text differently, so each model may return a different `token_count`.

### func (*CountMessageTokensRequest) Descriptor 
    
    
    func (*CountMessageTokensRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CountMessageTokensRequest.ProtoReflect.Descriptor instead.

### func (*CountMessageTokensRequest) GetModel 
    
    
    func (x *CountMessageTokensRequest) GetModel() [string](https://pkg.go.dev/builtin#string)

### func (*CountMessageTokensRequest) GetPrompt 
    
    
    func (x *CountMessageTokensRequest) GetPrompt() *MessagePrompt

### func (*CountMessageTokensRequest) ProtoMessage 
    
    
    func (*CountMessageTokensRequest) ProtoMessage()

### func (*CountMessageTokensRequest) ProtoReflect 
    
    
    func (x *CountMessageTokensRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CountMessageTokensRequest) Reset 
    
    
    func (x *CountMessageTokensRequest) Reset()

### func (*CountMessageTokensRequest) String 
    
    
    func (x *CountMessageTokensRequest) String() [string](https://pkg.go.dev/builtin#string)

## CountMessageTokensResponse
    
    
    type CountMessageTokensResponse struct {
    
    	// The number of tokens that the `model` tokenizes the `prompt` into.
    	//
    	// Always non-negative.
    	TokenCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=token_count,json=tokenCount,proto3" json:"token_count,omitempty"`
    	// contains filtered or unexported fields
    }

A response from `CountMessageTokens`.

It returns the model's `token_count` for the `prompt`.

### func (*CountMessageTokensResponse) Descriptor 
    
    
    func (*CountMessageTokensResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CountMessageTokensResponse.ProtoReflect.Descriptor instead.

### func (*CountMessageTokensResponse) GetTokenCount 
    
    
    func (x *CountMessageTokensResponse) GetTokenCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*CountMessageTokensResponse) ProtoMessage 
    
    
    func (*CountMessageTokensResponse) ProtoMessage()

### func (*CountMessageTokensResponse) ProtoReflect 
    
    
    func (x *CountMessageTokensResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CountMessageTokensResponse) Reset 
    
    
    func (x *CountMessageTokensResponse) Reset()

### func (*CountMessageTokensResponse) String 
    
    
    func (x *CountMessageTokensResponse) String() [string](https://pkg.go.dev/builtin#string)

## DiscussServiceClient
    
    
    type DiscussServiceClient interface {
    	// Generates a response from the model given an input `MessagePrompt`.
    	GenerateMessage(ctx context.Context, in *GenerateMessageRequest, opts ...grpc.CallOption) (*GenerateMessageResponse, [error](https://pkg.go.dev/builtin#error))
    	// Runs a model's tokenizer on a string and returns the token count.
    	CountMessageTokens(ctx context.Context, in *CountMessageTokensRequest, opts ...grpc.CallOption) (*CountMessageTokensResponse, [error](https://pkg.go.dev/builtin#error))
    }

DiscussServiceClient is the client API for DiscussService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewDiscussServiceClient 
    
    
    func NewDiscussServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) DiscussServiceClient

## DiscussServiceServer
    
    
    type DiscussServiceServer interface {
    	// Generates a response from the model given an input `MessagePrompt`.
    	GenerateMessage(context.Context, *GenerateMessageRequest) (*GenerateMessageResponse, [error](https://pkg.go.dev/builtin#error))
    	// Runs a model's tokenizer on a string and returns the token count.
    	CountMessageTokens(context.Context, *CountMessageTokensRequest) (*CountMessageTokensResponse, [error](https://pkg.go.dev/builtin#error))
    }

DiscussServiceServer is the server API for DiscussService service. All implementations should embed UnimplementedDiscussServiceServer for forward compatibility

## EmbedTextRequest
    
    
    type EmbedTextRequest struct {
    
    	// Required. The model name to use with the format model=models/{model}.
    	Model [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=model,proto3" json:"model,omitempty"`
    	// Required. The free-form input text that the model will turn into an
    	// embedding.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=text,proto3" json:"text,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get a text embedding from the model.

### func (*EmbedTextRequest) Descriptor 
    
    
    func (*EmbedTextRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EmbedTextRequest.ProtoReflect.Descriptor instead.

### func (*EmbedTextRequest) GetModel 
    
    
    func (x *EmbedTextRequest) GetModel() [string](https://pkg.go.dev/builtin#string)

### func (*EmbedTextRequest) GetText 
    
    
    func (x *EmbedTextRequest) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*EmbedTextRequest) ProtoMessage 
    
    
    func (*EmbedTextRequest) ProtoMessage()

### func (*EmbedTextRequest) ProtoReflect 
    
    
    func (x *EmbedTextRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EmbedTextRequest) Reset 
    
    
    func (x *EmbedTextRequest) Reset()

### func (*EmbedTextRequest) String 
    
    
    func (x *EmbedTextRequest) String() [string](https://pkg.go.dev/builtin#string)

## EmbedTextResponse
    
    
    type EmbedTextResponse struct {
    
    	// Output only. The embedding generated from the input text.
    	Embedding *Embedding `protobuf:"bytes,1,opt,name=embedding,proto3,oneof" json:"embedding,omitempty"`
    	// contains filtered or unexported fields
    }

The response to a EmbedTextRequest.

### func (*EmbedTextResponse) Descriptor 
    
    
    func (*EmbedTextResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EmbedTextResponse.ProtoReflect.Descriptor instead.

### func (*EmbedTextResponse) GetEmbedding 
    
    
    func (x *EmbedTextResponse) GetEmbedding() *Embedding

### func (*EmbedTextResponse) ProtoMessage 
    
    
    func (*EmbedTextResponse) ProtoMessage()

### func (*EmbedTextResponse) ProtoReflect 
    
    
    func (x *EmbedTextResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EmbedTextResponse) Reset 
    
    
    func (x *EmbedTextResponse) Reset()

### func (*EmbedTextResponse) String 
    
    
    func (x *EmbedTextResponse) String() [string](https://pkg.go.dev/builtin#string)

## Embedding
    
    
    type Embedding struct {
    
    	// The embedding values.
    	Value [][float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,rep,packed,name=value,proto3" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

A list of floats representing the embedding.

### func (*Embedding) Descriptor 
    
    
    func (*Embedding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Embedding.ProtoReflect.Descriptor instead.

### func (*Embedding) GetValue 
    
    
    func (x *Embedding) GetValue() [][float32](https://pkg.go.dev/builtin#float32)

### func (*Embedding) ProtoMessage 
    
    
    func (*Embedding) ProtoMessage()

### func (*Embedding) ProtoReflect 
    
    
    func (x *Embedding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Embedding) Reset 
    
    
    func (x *Embedding) Reset()

### func (*Embedding) String 
    
    
    func (x *Embedding) String() [string](https://pkg.go.dev/builtin#string)

## Example
    
    
    type Example struct {
    
    	// Required. An example of an input `Message` from the user.
    	Input *Message `protobuf:"bytes,1,opt,name=input,proto3" json:"input,omitempty"`
    	// Required. An example of what the model should output given the input.
    	Output *Message `protobuf:"bytes,2,opt,name=output,proto3" json:"output,omitempty"`
    	// contains filtered or unexported fields
    }

An input/output example used to instruct the Model.

It demonstrates how the model should respond or format its response.

### func (*Example) Descriptor 
    
    
    func (*Example) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Example.ProtoReflect.Descriptor instead.

### func (*Example) GetInput 
    
    
    func (x *Example) GetInput() *Message

### func (*Example) GetOutput 
    
    
    func (x *Example) GetOutput() *Message

### func (*Example) ProtoMessage 
    
    
    func (*Example) ProtoMessage()

### func (*Example) ProtoReflect 
    
    
    func (x *Example) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Example) Reset 
    
    
    func (x *Example) Reset()

### func (*Example) String 
    
    
    func (x *Example) String() [string](https://pkg.go.dev/builtin#string)

## GenerateMessageRequest
    
    
    type GenerateMessageRequest struct {
    
    	// Required. The name of the model to use.
    	//
    	// Format: `name=models/{model}`.
    	Model [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=model,proto3" json:"model,omitempty"`
    	// Required. The structured textual input given to the model as a prompt.
    	//
    	// Given a
    	// prompt, the model will return what it predicts is the next message in the
    	// discussion.
    	Prompt *MessagePrompt `protobuf:"bytes,2,opt,name=prompt,proto3" json:"prompt,omitempty"`
    	// Optional. Controls the randomness of the output.
    	//
    	// Values can range over `[0.0,1.0]`,
    	// inclusive. A value closer to `1.0` will produce responses that are more
    	// varied, while a value closer to `0.0` will typically result in
    	// less surprising responses from the model.
    	Temperature *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,3,opt,name=temperature,proto3,oneof" json:"temperature,omitempty"`
    	// Optional. The number of generated response messages to return.
    	//
    	// This value must be between
    	// `[1, 8]`, inclusive. If unset, this will default to `1`.
    	CandidateCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=candidate_count,json=candidateCount,proto3,oneof" json:"candidate_count,omitempty"`
    	// Optional. The maximum cumulative probability of tokens to consider when
    	// sampling.
    	//
    	// The model uses combined Top-k and nucleus sampling.
    	//
    	// Nucleus sampling considers the smallest set of tokens whose probability
    	// sum is at least `top_p`.
    	TopP *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,5,opt,name=top_p,json=topP,proto3,oneof" json:"top_p,omitempty"`
    	// Optional. The maximum number of tokens to consider when sampling.
    	//
    	// The model uses combined Top-k and nucleus sampling.
    	//
    	// Top-k sampling considers the set of `top_k` most probable tokens.
    	TopK *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=top_k,json=topK,proto3,oneof" json:"top_k,omitempty"`
    	// contains filtered or unexported fields
    }

Request to generate a message response from the model.

### func (*GenerateMessageRequest) Descriptor 
    
    
    func (*GenerateMessageRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateMessageRequest.ProtoReflect.Descriptor instead.

### func (*GenerateMessageRequest) GetCandidateCount 
    
    
    func (x *GenerateMessageRequest) GetCandidateCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*GenerateMessageRequest) GetModel 
    
    
    func (x *GenerateMessageRequest) GetModel() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateMessageRequest) GetPrompt 
    
    
    func (x *GenerateMessageRequest) GetPrompt() *MessagePrompt

### func (*GenerateMessageRequest) GetTemperature 
    
    
    func (x *GenerateMessageRequest) GetTemperature() [float32](https://pkg.go.dev/builtin#float32)

### func (*GenerateMessageRequest) GetTopK 
    
    
    func (x *GenerateMessageRequest) GetTopK() [int32](https://pkg.go.dev/builtin#int32)

### func (*GenerateMessageRequest) GetTopP 
    
    
    func (x *GenerateMessageRequest) GetTopP() [float32](https://pkg.go.dev/builtin#float32)

### func (*GenerateMessageRequest) ProtoMessage 
    
    
    func (*GenerateMessageRequest) ProtoMessage()

### func (*GenerateMessageRequest) ProtoReflect 
    
    
    func (x *GenerateMessageRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateMessageRequest) Reset 
    
    
    func (x *GenerateMessageRequest) Reset()

### func (*GenerateMessageRequest) String 
    
    
    func (x *GenerateMessageRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateMessageResponse
    
    
    type GenerateMessageResponse struct {
    
    	// Candidate response messages from the model.
    	Candidates []*Message `protobuf:"bytes,1,rep,name=candidates,proto3" json:"candidates,omitempty"`
    	// The conversation history used by the model.
    	Messages []*Message `protobuf:"bytes,2,rep,name=messages,proto3" json:"messages,omitempty"`
    	// A set of content filtering metadata for the prompt and response
    	// text.
    	//
    	// This indicates which `SafetyCategory`(s) blocked a
    	// candidate from this response, the lowest `HarmProbability`
    	// that triggered a block, and the HarmThreshold setting for that category.
    	Filters []*ContentFilter `protobuf:"bytes,3,rep,name=filters,proto3" json:"filters,omitempty"`
    	// contains filtered or unexported fields
    }

The response from the model.

This includes candidate messages and conversation history in the form of chronologically-ordered messages.

### func (*GenerateMessageResponse) Descriptor 
    
    
    func (*GenerateMessageResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateMessageResponse.ProtoReflect.Descriptor instead.

### func (*GenerateMessageResponse) GetCandidates 
    
    
    func (x *GenerateMessageResponse) GetCandidates() []*Message

### func (*GenerateMessageResponse) GetFilters 
    
    
    func (x *GenerateMessageResponse) GetFilters() []*ContentFilter

### func (*GenerateMessageResponse) GetMessages 
    
    
    func (x *GenerateMessageResponse) GetMessages() []*Message

### func (*GenerateMessageResponse) ProtoMessage 
    
    
    func (*GenerateMessageResponse) ProtoMessage()

### func (*GenerateMessageResponse) ProtoReflect 
    
    
    func (x *GenerateMessageResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateMessageResponse) Reset 
    
    
    func (x *GenerateMessageResponse) Reset()

### func (*GenerateMessageResponse) String 
    
    
    func (x *GenerateMessageResponse) String() [string](https://pkg.go.dev/builtin#string)

## GenerateTextRequest
    
    
    type GenerateTextRequest struct {
    
    	// Required. The model name to use with the format name=models/{model}.
    	Model [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=model,proto3" json:"model,omitempty"`
    	// Required. The free-form input text given to the model as a prompt.
    	//
    	// Given a prompt, the model will generate a TextCompletion response it
    	// predicts as the completion of the input text.
    	Prompt *TextPrompt `protobuf:"bytes,2,opt,name=prompt,proto3" json:"prompt,omitempty"`
    	// Controls the randomness of the output.
    	// Note: The default value varies by model, see the `Model.temperature`
    	// attribute of the `Model` returned the `getModel` function.
    	//
    	// Values can range from [0.0,1.0],
    	// inclusive. A value closer to 1.0 will produce responses that are more
    	// varied and creative, while a value closer to 0.0 will typically result in
    	// more straightforward responses from the model.
    	Temperature *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,3,opt,name=temperature,proto3,oneof" json:"temperature,omitempty"`
    	// Number of generated responses to return.
    	//
    	// This value must be between [1, 8], inclusive. If unset, this will default
    	// to 1.
    	CandidateCount *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=candidate_count,json=candidateCount,proto3,oneof" json:"candidate_count,omitempty"`
    	// The maximum number of tokens to include in a candidate.
    	//
    	// If unset, this will default to 64.
    	MaxOutputTokens *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=max_output_tokens,json=maxOutputTokens,proto3,oneof" json:"max_output_tokens,omitempty"`
    	// The maximum cumulative probability of tokens to consider when sampling.
    	//
    	// The model uses combined Top-k and nucleus sampling.
    	//
    	// Tokens are sorted based on their assigned probabilities so that only the
    	// most liekly tokens are considered. Top-k sampling directly limits the
    	// maximum number of tokens to consider, while Nucleus sampling limits number
    	// of tokens based on the cumulative probability.
    	//
    	// Note: The default value varies by model, see the `Model.top_p`
    	// attribute of the `Model` returned the `getModel` function.
    	TopP *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,6,opt,name=top_p,json=topP,proto3,oneof" json:"top_p,omitempty"`
    	// The maximum number of tokens to consider when sampling.
    	//
    	// The model uses combined Top-k and nucleus sampling.
    	//
    	// Top-k sampling considers the set of `top_k` most probable tokens.
    	// Defaults to 40.
    	//
    	// Note: The default value varies by model, see the `Model.top_k`
    	// attribute of the `Model` returned the `getModel` function.
    	TopK *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=top_k,json=topK,proto3,oneof" json:"top_k,omitempty"`
    	// A list of unique `SafetySetting` instances for blocking unsafe content.
    	//
    	// that will be enforced on the `GenerateTextRequest.prompt` and
    	// `GenerateTextResponse.candidates`. There should not be more than one
    	// setting for each `SafetyCategory` type. The API will block any prompts and
    	// responses that fail to meet the thresholds set by these settings. This list
    	// overrides the default settings for each `SafetyCategory` specified in the
    	// safety_settings. If there is no `SafetySetting` for a given
    	// `SafetyCategory` provided in the list, the API will use the default safety
    	// setting for that category.
    	SafetySettings []*SafetySetting `protobuf:"bytes,8,rep,name=safety_settings,json=safetySettings,proto3" json:"safety_settings,omitempty"`
    	// The set of character sequences (up to 5) that will stop output generation.
    	// If specified, the API will stop at the first appearance of a stop
    	// sequence. The stop sequence will not be included as part of the response.
    	StopSequences [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,rep,name=stop_sequences,json=stopSequences,proto3" json:"stop_sequences,omitempty"`
    	// contains filtered or unexported fields
    }

Request to generate a text completion response from the model.

### func (*GenerateTextRequest) Descriptor 
    
    
    func (*GenerateTextRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateTextRequest.ProtoReflect.Descriptor instead.

### func (*GenerateTextRequest) GetCandidateCount 
    
    
    func (x *GenerateTextRequest) GetCandidateCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*GenerateTextRequest) GetMaxOutputTokens 
    
    
    func (x *GenerateTextRequest) GetMaxOutputTokens() [int32](https://pkg.go.dev/builtin#int32)

### func (*GenerateTextRequest) GetModel 
    
    
    func (x *GenerateTextRequest) GetModel() [string](https://pkg.go.dev/builtin#string)

### func (*GenerateTextRequest) GetPrompt 
    
    
    func (x *GenerateTextRequest) GetPrompt() *TextPrompt

### func (*GenerateTextRequest) GetSafetySettings 
    
    
    func (x *GenerateTextRequest) GetSafetySettings() []*SafetySetting

### func (*GenerateTextRequest) GetStopSequences 
    
    
    func (x *GenerateTextRequest) GetStopSequences() [][string](https://pkg.go.dev/builtin#string)

### func (*GenerateTextRequest) GetTemperature 
    
    
    func (x *GenerateTextRequest) GetTemperature() [float32](https://pkg.go.dev/builtin#float32)

### func (*GenerateTextRequest) GetTopK 
    
    
    func (x *GenerateTextRequest) GetTopK() [int32](https://pkg.go.dev/builtin#int32)

### func (*GenerateTextRequest) GetTopP 
    
    
    func (x *GenerateTextRequest) GetTopP() [float32](https://pkg.go.dev/builtin#float32)

### func (*GenerateTextRequest) ProtoMessage 
    
    
    func (*GenerateTextRequest) ProtoMessage()

### func (*GenerateTextRequest) ProtoReflect 
    
    
    func (x *GenerateTextRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateTextRequest) Reset 
    
    
    func (x *GenerateTextRequest) Reset()

### func (*GenerateTextRequest) String 
    
    
    func (x *GenerateTextRequest) String() [string](https://pkg.go.dev/builtin#string)

## GenerateTextResponse
    
    
    type GenerateTextResponse struct {
    
    	// Candidate responses from the model.
    	Candidates []*TextCompletion `protobuf:"bytes,1,rep,name=candidates,proto3" json:"candidates,omitempty"`
    	// A set of content filtering metadata for the prompt and response
    	// text.
    	//
    	// This indicates which `SafetyCategory`(s) blocked a
    	// candidate from this response, the lowest `HarmProbability`
    	// that triggered a block, and the HarmThreshold setting for that category.
    	// This indicates the smallest change to the `SafetySettings` that would be
    	// necessary to unblock at least 1 response.
    	//
    	// The blocking is configured by the `SafetySettings` in the request (or the
    	// default `SafetySettings` of the API).
    	Filters []*ContentFilter `protobuf:"bytes,3,rep,name=filters,proto3" json:"filters,omitempty"`
    	// Returns any safety feedback related to content filtering.
    	SafetyFeedback []*SafetyFeedback `protobuf:"bytes,4,rep,name=safety_feedback,json=safetyFeedback,proto3" json:"safety_feedback,omitempty"`
    	// contains filtered or unexported fields
    }

The response from the model, including candidate completions.

### func (*GenerateTextResponse) Descriptor 
    
    
    func (*GenerateTextResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenerateTextResponse.ProtoReflect.Descriptor instead.

### func (*GenerateTextResponse) GetCandidates 
    
    
    func (x *GenerateTextResponse) GetCandidates() []*TextCompletion

### func (*GenerateTextResponse) GetFilters 
    
    
    func (x *GenerateTextResponse) GetFilters() []*ContentFilter

### func (*GenerateTextResponse) GetSafetyFeedback 
    
    
    func (x *GenerateTextResponse) GetSafetyFeedback() []*SafetyFeedback

### func (*GenerateTextResponse) ProtoMessage 
    
    
    func (*GenerateTextResponse) ProtoMessage()

### func (*GenerateTextResponse) ProtoReflect 
    
    
    func (x *GenerateTextResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenerateTextResponse) Reset 
    
    
    func (x *GenerateTextResponse) Reset()

### func (*GenerateTextResponse) String 
    
    
    func (x *GenerateTextResponse) String() [string](https://pkg.go.dev/builtin#string)

## GetModelRequest
    
    
    type GetModelRequest struct {
    
    	// Required. The resource name of the model.
    	//
    	// This name should match a model name returned by the `ListModels` method.
    	//
    	// Format: `models/{model}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request for getting information about a specific Model.

### func (*GetModelRequest) Descriptor 
    
    
    func (*GetModelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetModelRequest.ProtoReflect.Descriptor instead.

### func (*GetModelRequest) GetName 
    
    
    func (x *GetModelRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetModelRequest) ProtoMessage 
    
    
    func (*GetModelRequest) ProtoMessage()

### func (*GetModelRequest) ProtoReflect 
    
    
    func (x *GetModelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetModelRequest) Reset 
    
    
    func (x *GetModelRequest) Reset()

### func (*GetModelRequest) String 
    
    
    func (x *GetModelRequest) String() [string](https://pkg.go.dev/builtin#string)

## HarmCategory
    
    
    type HarmCategory [int32](https://pkg.go.dev/builtin#int32)

The category of a rating.

These categories cover various kinds of harms that developers may wish to adjust.

### HarmCategory_HARM_CATEGORY_UNSPECIFIED, HarmCategory_HARM_CATEGORY_DEROGATORY, HarmCategory_HARM_CATEGORY_TOXICITY, HarmCategory_HARM_CATEGORY_VIOLENCE, HarmCategory_HARM_CATEGORY_SEXUAL, HarmCategory_HARM_CATEGORY_MEDICAL, HarmCategory_HARM_CATEGORY_DANGEROUS
    
    
    const (
    	// Category is unspecified.
    	HarmCategory_HARM_CATEGORY_UNSPECIFIED HarmCategory = 0
    	// Negative or harmful comments targeting identity and/or protected attribute.
    	HarmCategory_HARM_CATEGORY_DEROGATORY HarmCategory = 1
    	// Content that is rude, disrepspectful, or profane.
    	HarmCategory_HARM_CATEGORY_TOXICITY HarmCategory = 2
    	// Describes scenarios depictng violence against an individual or group, or
    	// general descriptions of gore.
    	HarmCategory_HARM_CATEGORY_VIOLENCE HarmCategory = 3
    	// Contains references to sexual acts or other lewd content.
    	HarmCategory_HARM_CATEGORY_SEXUAL HarmCategory = 4
    	// Promotes unchecked medical advice.
    	HarmCategory_HARM_CATEGORY_MEDICAL HarmCategory = 5
    	// Dangerous content that promotes, facilitates, or encourages harmful acts.
    	HarmCategory_HARM_CATEGORY_DANGEROUS HarmCategory = 6
    )

### func (HarmCategory) Descriptor 
    
    
    func (HarmCategory) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (HarmCategory) Enum 
    
    
    func (x HarmCategory) Enum() *HarmCategory

### func (HarmCategory) EnumDescriptor 
    
    
    func (HarmCategory) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HarmCategory.Descriptor instead.

### func (HarmCategory) Number 
    
    
    func (x HarmCategory) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (HarmCategory) String 
    
    
    func (x HarmCategory) String() [string](https://pkg.go.dev/builtin#string)

### func (HarmCategory) Type 
    
    
    func (HarmCategory) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListModelsRequest
    
    
    type ListModelsRequest struct {
    
    	// The maximum number of `Models` to return (per page).
    	//
    	// The service may return fewer models.
    	// If unspecified, at most 50 models will be returned per page.
    	// This method returns at most 1000 models per page, even if you pass a larger
    	// page_size.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListModels` call.
    	//
    	// Provide the `page_token` returned by one request as an argument to the next
    	// request to retrieve the next page.
    	//
    	// When paginating, all other parameters provided to `ListModels` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request for listing all Models.

### func (*ListModelsRequest) Descriptor 
    
    
    func (*ListModelsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListModelsRequest.ProtoReflect.Descriptor instead.

### func (*ListModelsRequest) GetPageSize 
    
    
    func (x *ListModelsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListModelsRequest) GetPageToken 
    
    
    func (x *ListModelsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListModelsRequest) ProtoMessage 
    
    
    func (*ListModelsRequest) ProtoMessage()

### func (*ListModelsRequest) ProtoReflect 
    
    
    func (x *ListModelsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListModelsRequest) Reset 
    
    
    func (x *ListModelsRequest) Reset()

### func (*ListModelsRequest) String 
    
    
    func (x *ListModelsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListModelsResponse
    
    
    type ListModelsResponse struct {
    
    	// The returned Models.
    	Models []*Model `protobuf:"bytes,1,rep,name=models,proto3" json:"models,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	//
    	// If this field is omitted, there are no more pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response from `ListModel` containing a paginated list of Models.

### func (*ListModelsResponse) Descriptor 
    
    
    func (*ListModelsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListModelsResponse.ProtoReflect.Descriptor instead.

### func (*ListModelsResponse) GetModels 
    
    
    func (x *ListModelsResponse) GetModels() []*Model

### func (*ListModelsResponse) GetNextPageToken 
    
    
    func (x *ListModelsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListModelsResponse) ProtoMessage 
    
    
    func (*ListModelsResponse) ProtoMessage()

### func (*ListModelsResponse) ProtoReflect 
    
    
    func (x *ListModelsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListModelsResponse) Reset 
    
    
    func (x *ListModelsResponse) Reset()

### func (*ListModelsResponse) String 
    
    
    func (x *ListModelsResponse) String() [string](https://pkg.go.dev/builtin#string)

## Message
    
    
    type Message struct {
    
    	// Optional. The author of this Message.
    	//
    	// This serves as a key for tagging
    	// the content of this Message when it is fed to the model as text.
    	//
    	// The author can be any alphanumeric string.
    	Author [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=author,proto3" json:"author,omitempty"`
    	// Required. The text content of the structured `Message`.
    	Content [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
    	// Output only. Citation information for model-generated `content` in this
    	// `Message`.
    	//
    	// If this `Message` was generated as output from the model, this field may be
    	// populated with attribution information for any text included in the
    	// `content`. This field is used only on output.
    	CitationMetadata *CitationMetadata `protobuf:"bytes,3,opt,name=citation_metadata,json=citationMetadata,proto3,oneof" json:"citation_metadata,omitempty"`
    	// contains filtered or unexported fields
    }

The base unit of structured text.

A `Message` includes an `author` and the `content` of the `Message`.

The `author` is used to tag messages when they are fed to the model as text.

### func (*Message) Descriptor 
    
    
    func (*Message) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Message.ProtoReflect.Descriptor instead.

### func (*Message) GetAuthor 
    
    
    func (x *Message) GetAuthor() [string](https://pkg.go.dev/builtin#string)

### func (*Message) GetCitationMetadata 
    
    
    func (x *Message) GetCitationMetadata() *CitationMetadata

### func (*Message) GetContent 
    
    
    func (x *Message) GetContent() [string](https://pkg.go.dev/builtin#string)

### func (*Message) ProtoMessage 
    
    
    func (*Message) ProtoMessage()

### func (*Message) ProtoReflect 
    
    
    func (x *Message) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Message) Reset 
    
    
    func (x *Message) Reset()

### func (*Message) String 
    
    
    func (x *Message) String() [string](https://pkg.go.dev/builtin#string)

## MessagePrompt
    
    
    type MessagePrompt struct {
    
    	// Optional. Text that should be provided to the model first to ground the
    	// response.
    	//
    	// If not empty, this `context` will be given to the model first before the
    	// `examples` and `messages`. When using a `context` be sure to provide it
    	// with every request to maintain continuity.
    	//
    	// This field can be a description of your prompt to the model to help provide
    	// context and guide the responses. Examples: "Translate the phrase from
    	// English to French." or "Given a statement, classify the sentiment as happy,
    	// sad or neutral."
    	//
    	// Anything included in this field will take precedence over message history
    	// if the total input size exceeds the model's `input_token_limit` and the
    	// input request is truncated.
    	Context [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=context,proto3" json:"context,omitempty"`
    	// Optional. Examples of what the model should generate.
    	//
    	// This includes both user input and the response that the model should
    	// emulate.
    	//
    	// These `examples` are treated identically to conversation messages except
    	// that they take precedence over the history in `messages`:
    	// If the total input size exceeds the model's `input_token_limit` the input
    	// will be truncated. Items will be dropped from `messages` before `examples`.
    	Examples []*Example `protobuf:"bytes,2,rep,name=examples,proto3" json:"examples,omitempty"`
    	// Required. A snapshot of the recent conversation history sorted
    	// chronologically.
    	//
    	// Turns alternate between two authors.
    	//
    	// If the total input size exceeds the model's `input_token_limit` the input
    	// will be truncated: The oldest items will be dropped from `messages`.
    	Messages []*Message `protobuf:"bytes,3,rep,name=messages,proto3" json:"messages,omitempty"`
    	// contains filtered or unexported fields
    }

All of the structured input text passed to the model as a prompt.

A `MessagePrompt` contains a structured set of fields that provide context for the conversation, examples of user input/model output message pairs that prime the model to respond in different ways, and the conversation history or list of messages representing the alternating turns of the conversation between the user and the model.

### func (*MessagePrompt) Descriptor 
    
    
    func (*MessagePrompt) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MessagePrompt.ProtoReflect.Descriptor instead.

### func (*MessagePrompt) GetContext 
    
    
    func (x *MessagePrompt) GetContext() [string](https://pkg.go.dev/builtin#string)

### func (*MessagePrompt) GetExamples 
    
    
    func (x *MessagePrompt) GetExamples() []*Example

### func (*MessagePrompt) GetMessages 
    
    
    func (x *MessagePrompt) GetMessages() []*Message

### func (*MessagePrompt) ProtoMessage 
    
    
    func (*MessagePrompt) ProtoMessage()

### func (*MessagePrompt) ProtoReflect 
    
    
    func (x *MessagePrompt) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MessagePrompt) Reset 
    
    
    func (x *MessagePrompt) Reset()

### func (*MessagePrompt) String 
    
    
    func (x *MessagePrompt) String() [string](https://pkg.go.dev/builtin#string)

## Model
    
    
    type Model struct {
    
    	// Required. The resource name of the `Model`.
    	//
    	// Format: `models/{model}` with a `{model}` naming convention of:
    	//
    	// * "{base_model_id}-{version}"
    	//
    	// Examples:
    	//
    	// * `models/chat-bison-001`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The name of the base model, pass this to the generation request.
    	//
    	// Examples:
    	//
    	// * `chat-bison`
    	BaseModelId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=base_model_id,json=baseModelId,proto3" json:"base_model_id,omitempty"`
    	// Required. The version number of the model.
    	//
    	// This represents the major version
    	Version [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=version,proto3" json:"version,omitempty"`
    	// The human-readable name of the model. E.g. "Chat Bison".
    	//
    	// The name can be up to 128 characters long and can consist of any UTF-8
    	// characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A short description of the model.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// Maximum number of input tokens allowed for this model.
    	InputTokenLimit [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=input_token_limit,json=inputTokenLimit,proto3" json:"input_token_limit,omitempty"`
    	// Maximum number of output tokens available for this model.
    	OutputTokenLimit [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=output_token_limit,json=outputTokenLimit,proto3" json:"output_token_limit,omitempty"`
    	// The model's supported generation methods.
    	//
    	// The method names are defined as Pascal case
    	// strings, such as `generateMessage` which correspond to API methods.
    	SupportedGenerationMethods [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,rep,name=supported_generation_methods,json=supportedGenerationMethods,proto3" json:"supported_generation_methods,omitempty"`
    	// Controls the randomness of the output.
    	//
    	// Values can range over `[0.0,1.0]`, inclusive. A value closer to `1.0` will
    	// produce responses that are more varied, while a value closer to `0.0` will
    	// typically result in less surprising responses from the model.
    	// This value specifies default to be used by the backend while making the
    	// call to the model.
    	Temperature *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,9,opt,name=temperature,proto3,oneof" json:"temperature,omitempty"`
    	// For Nucleus sampling.
    	//
    	// Nucleus sampling considers the smallest set of tokens whose probability
    	// sum is at least `top_p`.
    	// This value specifies default to be used by the backend while making the
    	// call to the model.
    	TopP *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,10,opt,name=top_p,json=topP,proto3,oneof" json:"top_p,omitempty"`
    	// For Top-k sampling.
    	//
    	// Top-k sampling considers the set of `top_k` most probable tokens.
    	// This value specifies default to be used by the backend while making the
    	// call to the model.
    	TopK *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,11,opt,name=top_k,json=topK,proto3,oneof" json:"top_k,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a Generative Language Model.

### func (*Model) Descriptor 
    
    
    func (*Model) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Model.ProtoReflect.Descriptor instead.

### func (*Model) GetBaseModelId 
    
    
    func (x *Model) GetBaseModelId() [string](https://pkg.go.dev/builtin#string)

### func (*Model) GetDescription 
    
    
    func (x *Model) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Model) GetDisplayName 
    
    
    func (x *Model) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Model) GetInputTokenLimit 
    
    
    func (x *Model) GetInputTokenLimit() [int32](https://pkg.go.dev/builtin#int32)

### func (*Model) GetName 
    
    
    func (x *Model) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Model) GetOutputTokenLimit 
    
    
    func (x *Model) GetOutputTokenLimit() [int32](https://pkg.go.dev/builtin#int32)

### func (*Model) GetSupportedGenerationMethods 
    
    
    func (x *Model) GetSupportedGenerationMethods() [][string](https://pkg.go.dev/builtin#string)

### func (*Model) GetTemperature 
    
    
    func (x *Model) GetTemperature() [float32](https://pkg.go.dev/builtin#float32)

### func (*Model) GetTopK 
    
    
    func (x *Model) GetTopK() [int32](https://pkg.go.dev/builtin#int32)

### func (*Model) GetTopP 
    
    
    func (x *Model) GetTopP() [float32](https://pkg.go.dev/builtin#float32)

### func (*Model) GetVersion 
    
    
    func (x *Model) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*Model) ProtoMessage 
    
    
    func (*Model) ProtoMessage()

### func (*Model) ProtoReflect 
    
    
    func (x *Model) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Model) Reset 
    
    
    func (x *Model) Reset()

### func (*Model) String 
    
    
    func (x *Model) String() [string](https://pkg.go.dev/builtin#string)

## ModelServiceClient
    
    
    type ModelServiceClient interface {
    	// Gets information about a specific Model.
    	GetModel(ctx context.Context, in *GetModelRequest, opts ...grpc.CallOption) (*Model, [error](https://pkg.go.dev/builtin#error))
    	// Lists models available through the API.
    	ListModels(ctx context.Context, in *ListModelsRequest, opts ...grpc.CallOption) (*ListModelsResponse, [error](https://pkg.go.dev/builtin#error))
    }

ModelServiceClient is the client API for ModelService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewModelServiceClient 
    
    
    func NewModelServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) ModelServiceClient

## ModelServiceServer
    
    
    type ModelServiceServer interface {
    	// Gets information about a specific Model.
    	GetModel(context.Context, *GetModelRequest) (*Model, [error](https://pkg.go.dev/builtin#error))
    	// Lists models available through the API.
    	ListModels(context.Context, *ListModelsRequest) (*ListModelsResponse, [error](https://pkg.go.dev/builtin#error))
    }

ModelServiceServer is the server API for ModelService service. All implementations should embed UnimplementedModelServiceServer for forward compatibility

## SafetyFeedback
    
    
    type SafetyFeedback struct {
    
    	// Safety rating evaluated from content.
    	Rating *SafetyRating `protobuf:"bytes,1,opt,name=rating,proto3" json:"rating,omitempty"`
    	// Safety settings applied to the request.
    	Setting *SafetySetting `protobuf:"bytes,2,opt,name=setting,proto3" json:"setting,omitempty"`
    	// contains filtered or unexported fields
    }

Safety feedback for an entire request.

This field is populated if content in the input and/or response is blocked due to safety settings. SafetyFeedback may not exist for every HarmCategory. Each SafetyFeedback will return the safety settings used by the request as well as the lowest HarmProbability that should be allowed in order to return a result.

### func (*SafetyFeedback) Descriptor 
    
    
    func (*SafetyFeedback) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SafetyFeedback.ProtoReflect.Descriptor instead.

### func (*SafetyFeedback) GetRating 
    
    
    func (x *SafetyFeedback) GetRating() *SafetyRating

### func (*SafetyFeedback) GetSetting 
    
    
    func (x *SafetyFeedback) GetSetting() *SafetySetting

### func (*SafetyFeedback) ProtoMessage 
    
    
    func (*SafetyFeedback) ProtoMessage()

### func (*SafetyFeedback) ProtoReflect 
    
    
    func (x *SafetyFeedback) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SafetyFeedback) Reset 
    
    
    func (x *SafetyFeedback) Reset()

### func (*SafetyFeedback) String 
    
    
    func (x *SafetyFeedback) String() [string](https://pkg.go.dev/builtin#string)

## SafetyRating
    
    
    type SafetyRating struct {
    
    	// Required. The category for this rating.
    	Category HarmCategory `protobuf:"varint,3,opt,name=category,proto3,enum=google.ai.generativelanguage.v1beta2.HarmCategory" json:"category,omitempty"`
    	// Required. The probability of harm for this content.
    	Probability SafetyRating_HarmProbability `protobuf:"varint,4,opt,name=probability,proto3,enum=google.ai.generativelanguage.v1beta2.SafetyRating_HarmProbability" json:"probability,omitempty"`
    	// contains filtered or unexported fields
    }

Safety rating for a piece of content.

The safety rating contains the category of harm and the harm probability level in that category for a piece of content. Content is classified for safety across a number of harm categories and the probability of the harm classification is included here.

### func (*SafetyRating) Descriptor 
    
    
    func (*SafetyRating) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SafetyRating.ProtoReflect.Descriptor instead.

### func (*SafetyRating) GetCategory 
    
    
    func (x *SafetyRating) GetCategory() HarmCategory

### func (*SafetyRating) GetProbability 
    
    
    func (x *SafetyRating) GetProbability() SafetyRating_HarmProbability

### func (*SafetyRating) ProtoMessage 
    
    
    func (*SafetyRating) ProtoMessage()

### func (*SafetyRating) ProtoReflect 
    
    
    func (x *SafetyRating) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SafetyRating) Reset 
    
    
    func (x *SafetyRating) Reset()

### func (*SafetyRating) String 
    
    
    func (x *SafetyRating) String() [string](https://pkg.go.dev/builtin#string)

## SafetyRating_HarmProbability
    
    
    type SafetyRating_HarmProbability [int32](https://pkg.go.dev/builtin#int32)

The probability that a piece of content is harmful.

The classification system gives the probability of the content being unsafe. This does not indicate the severity of harm for a piece of content.

### SafetyRating_HARM_PROBABILITY_UNSPECIFIED, SafetyRating_NEGLIGIBLE, SafetyRating_LOW, SafetyRating_MEDIUM, SafetyRating_HIGH
    
    
    const (
    	// Probability is unspecified.
    	SafetyRating_HARM_PROBABILITY_UNSPECIFIED SafetyRating_HarmProbability = 0
    	// Content has a negligible chance of being unsafe.
    	SafetyRating_NEGLIGIBLE SafetyRating_HarmProbability = 1
    	// Content has a low chance of being unsafe.
    	SafetyRating_LOW SafetyRating_HarmProbability = 2
    	// Content has a medium chance of being unsafe.
    	SafetyRating_MEDIUM SafetyRating_HarmProbability = 3
    	// Content has a high chance of being unsafe.
    	SafetyRating_HIGH SafetyRating_HarmProbability = 4
    )

### func (SafetyRating_HarmProbability) Descriptor 
    
    
    func (SafetyRating_HarmProbability) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SafetyRating_HarmProbability) Enum 
    
    
    func (x SafetyRating_HarmProbability) Enum() *SafetyRating_HarmProbability

### func (SafetyRating_HarmProbability) EnumDescriptor 
    
    
    func (SafetyRating_HarmProbability) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SafetyRating_HarmProbability.Descriptor instead.

### func (SafetyRating_HarmProbability) Number 
    
    
    func (x SafetyRating_HarmProbability) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SafetyRating_HarmProbability) String 
    
    
    func (x SafetyRating_HarmProbability) String() [string](https://pkg.go.dev/builtin#string)

### func (SafetyRating_HarmProbability) Type 
    
    
    func (SafetyRating_HarmProbability) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SafetySetting
    
    
    type SafetySetting struct {
    
    	// Required. The category for this setting.
    	Category HarmCategory `protobuf:"varint,3,opt,name=category,proto3,enum=google.ai.generativelanguage.v1beta2.HarmCategory" json:"category,omitempty"`
    	// Required. Controls the probability threshold at which harm is blocked.
    	Threshold SafetySetting_HarmBlockThreshold `protobuf:"varint,4,opt,name=threshold,proto3,enum=google.ai.generativelanguage.v1beta2.SafetySetting_HarmBlockThreshold" json:"threshold,omitempty"`
    	// contains filtered or unexported fields
    }

Safety setting, affecting the safety-blocking behavior.

Passing a safety setting for a category changes the allowed proability that content is blocked.

### func (*SafetySetting) Descriptor 
    
    
    func (*SafetySetting) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SafetySetting.ProtoReflect.Descriptor instead.

### func (*SafetySetting) GetCategory 
    
    
    func (x *SafetySetting) GetCategory() HarmCategory

### func (*SafetySetting) GetThreshold 
    
    
    func (x *SafetySetting) GetThreshold() SafetySetting_HarmBlockThreshold

### func (*SafetySetting) ProtoMessage 
    
    
    func (*SafetySetting) ProtoMessage()

### func (*SafetySetting) ProtoReflect 
    
    
    func (x *SafetySetting) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SafetySetting) Reset 
    
    
    func (x *SafetySetting) Reset()

### func (*SafetySetting) String 
    
    
    func (x *SafetySetting) String() [string](https://pkg.go.dev/builtin#string)

## SafetySetting_HarmBlockThreshold
    
    
    type SafetySetting_HarmBlockThreshold [int32](https://pkg.go.dev/builtin#int32)

Block at and beyond a specified harm probability.

### SafetySetting_HARM_BLOCK_THRESHOLD_UNSPECIFIED, SafetySetting_BLOCK_LOW_AND_ABOVE, SafetySetting_BLOCK_MEDIUM_AND_ABOVE, SafetySetting_BLOCK_ONLY_HIGH
    
    
    const (
    	// Threshold is unspecified.
    	SafetySetting_HARM_BLOCK_THRESHOLD_UNSPECIFIED SafetySetting_HarmBlockThreshold = 0
    	// Content with NEGLIGIBLE will be allowed.
    	SafetySetting_BLOCK_LOW_AND_ABOVE SafetySetting_HarmBlockThreshold = 1
    	// Content with NEGLIGIBLE and LOW will be allowed.
    	SafetySetting_BLOCK_MEDIUM_AND_ABOVE SafetySetting_HarmBlockThreshold = 2
    	// Content with NEGLIGIBLE, LOW, and MEDIUM will be allowed.
    	SafetySetting_BLOCK_ONLY_HIGH SafetySetting_HarmBlockThreshold = 3
    )

### func (SafetySetting_HarmBlockThreshold) Descriptor 
    
    
    func (SafetySetting_HarmBlockThreshold) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SafetySetting_HarmBlockThreshold) Enum 
    
    
    func (x SafetySetting_HarmBlockThreshold) Enum() *SafetySetting_HarmBlockThreshold

### func (SafetySetting_HarmBlockThreshold) EnumDescriptor 
    
    
    func (SafetySetting_HarmBlockThreshold) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SafetySetting_HarmBlockThreshold.Descriptor instead.

### func (SafetySetting_HarmBlockThreshold) Number 
    
    
    func (x SafetySetting_HarmBlockThreshold) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SafetySetting_HarmBlockThreshold) String 
    
    
    func (x SafetySetting_HarmBlockThreshold) String() [string](https://pkg.go.dev/builtin#string)

### func (SafetySetting_HarmBlockThreshold) Type 
    
    
    func (SafetySetting_HarmBlockThreshold) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## TextCompletion
    
    
    type TextCompletion struct {
    
    	// Output only. The generated text returned from the model.
    	Output [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=output,proto3" json:"output,omitempty"`
    	// Ratings for the safety of a response.
    	//
    	// There is at most one rating per category.
    	SafetyRatings []*SafetyRating `protobuf:"bytes,2,rep,name=safety_ratings,json=safetyRatings,proto3" json:"safety_ratings,omitempty"`
    	// Output only. Citation information for model-generated `output` in this
    	// `TextCompletion`.
    	//
    	// This field may be populated with attribution information for any text
    	// included in the `output`.
    	CitationMetadata *CitationMetadata `protobuf:"bytes,3,opt,name=citation_metadata,json=citationMetadata,proto3,oneof" json:"citation_metadata,omitempty"`
    	// contains filtered or unexported fields
    }

Output text returned from a model.

### func (*TextCompletion) Descriptor 
    
    
    func (*TextCompletion) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TextCompletion.ProtoReflect.Descriptor instead.

### func (*TextCompletion) GetCitationMetadata 
    
    
    func (x *TextCompletion) GetCitationMetadata() *CitationMetadata

### func (*TextCompletion) GetOutput 
    
    
    func (x *TextCompletion) GetOutput() [string](https://pkg.go.dev/builtin#string)

### func (*TextCompletion) GetSafetyRatings 
    
    
    func (x *TextCompletion) GetSafetyRatings() []*SafetyRating

### func (*TextCompletion) ProtoMessage 
    
    
    func (*TextCompletion) ProtoMessage()

### func (*TextCompletion) ProtoReflect 
    
    
    func (x *TextCompletion) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TextCompletion) Reset 
    
    
    func (x *TextCompletion) Reset()

### func (*TextCompletion) String 
    
    
    func (x *TextCompletion) String() [string](https://pkg.go.dev/builtin#string)

## TextPrompt
    
    
    type TextPrompt struct {
    
    	// Required. The prompt text.
    	Text [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
    	// contains filtered or unexported fields
    }

Text given to the model as a prompt.

The Model will use this TextPrompt to Generate a text completion.

### func (*TextPrompt) Descriptor 
    
    
    func (*TextPrompt) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TextPrompt.ProtoReflect.Descriptor instead.

### func (*TextPrompt) GetText 
    
    
    func (x *TextPrompt) GetText() [string](https://pkg.go.dev/builtin#string)

### func (*TextPrompt) ProtoMessage 
    
    
    func (*TextPrompt) ProtoMessage()

### func (*TextPrompt) ProtoReflect 
    
    
    func (x *TextPrompt) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TextPrompt) Reset 
    
    
    func (x *TextPrompt) Reset()

### func (*TextPrompt) String 
    
    
    func (x *TextPrompt) String() [string](https://pkg.go.dev/builtin#string)

## TextServiceClient
    
    
    type TextServiceClient interface {
    	// Generates a response from the model given an input message.
    	GenerateText(ctx context.Context, in *GenerateTextRequest, opts ...grpc.CallOption) (*GenerateTextResponse, [error](https://pkg.go.dev/builtin#error))
    	// Generates an embedding from the model given an input message.
    	EmbedText(ctx context.Context, in *EmbedTextRequest, opts ...grpc.CallOption) (*EmbedTextResponse, [error](https://pkg.go.dev/builtin#error))
    }

TextServiceClient is the client API for TextService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewTextServiceClient 
    
    
    func NewTextServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) TextServiceClient

## TextServiceServer
    
    
    type TextServiceServer interface {
    	// Generates a response from the model given an input message.
    	GenerateText(context.Context, *GenerateTextRequest) (*GenerateTextResponse, [error](https://pkg.go.dev/builtin#error))
    	// Generates an embedding from the model given an input message.
    	EmbedText(context.Context, *EmbedTextRequest) (*EmbedTextResponse, [error](https://pkg.go.dev/builtin#error))
    }

TextServiceServer is the server API for TextService service. All implementations should embed UnimplementedTextServiceServer for forward compatibility

## UnimplementedDiscussServiceServer
    
    
    type UnimplementedDiscussServiceServer struct {
    }

UnimplementedDiscussServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedDiscussServiceServer) CountMessageTokens 
    
    
    func (UnimplementedDiscussServiceServer) CountMessageTokens([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CountMessageTokensRequest) (*CountMessageTokensResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedDiscussServiceServer) GenerateMessage 
    
    
    func (UnimplementedDiscussServiceServer) GenerateMessage([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateMessageRequest) (*GenerateMessageResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedModelServiceServer
    
    
    type UnimplementedModelServiceServer struct {
    }

UnimplementedModelServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedModelServiceServer) GetModel 
    
    
    func (UnimplementedModelServiceServer) GetModel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetModelRequest) (*Model, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedModelServiceServer) ListModels 
    
    
    func (UnimplementedModelServiceServer) ListModels([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListModelsRequest) (*ListModelsResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedTextServiceServer
    
    
    type UnimplementedTextServiceServer struct {
    }

UnimplementedTextServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedTextServiceServer) EmbedText 
    
    
    func (UnimplementedTextServiceServer) EmbedText([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *EmbedTextRequest) (*EmbedTextResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedTextServiceServer) GenerateText 
    
    
    func (UnimplementedTextServiceServer) GenerateText([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GenerateTextRequest) (*GenerateTextResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeDiscussServiceServer
    
    
    type UnsafeDiscussServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeDiscussServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to DiscussServiceServer will result in compilation errors.

## UnsafeModelServiceServer
    
    
    type UnsafeModelServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeModelServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ModelServiceServer will result in compilation errors.

## UnsafeTextServiceServer
    
    
    type UnsafeTextServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeTextServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to TextServiceServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
