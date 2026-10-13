---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataqna/latest/apiv1alpha/dataqnapb/
title: Data QnA API v1alpha - Package cloud.google.com/go/dataqna/apiv1alpha/dataqnapb (v0.14.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:42.958455+00:00
---

# Data QnA API v1alpha - Package cloud.google.com/go/dataqna/apiv1alpha/dataqnapb (v0.14.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataqna/latest/apiv1alpha/dataqnapb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Data QnA API v1alpha - Package cloud.google.com/go/dataqna/apiv1alpha/dataqnapb (v0.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.0 (latest)  0.13.0  0.12.0  0.11.0  0.10.0  0.9.8  0.8.12  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Alpha**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/dataqna/apiv1alpha/dataqnapb). 

##  Constants 

### QuestionService_GetQuestion_FullMethodName, QuestionService_CreateQuestion_FullMethodName, QuestionService_ExecuteQuestion_FullMethodName, QuestionService_GetUserFeedback_FullMethodName, QuestionService_UpdateUserFeedback_FullMethodName
    
    
    const (
    	QuestionService_GetQuestion_FullMethodName        = "/google.cloud.dataqna.v1alpha.QuestionService/GetQuestion"
    	QuestionService_CreateQuestion_FullMethodName     = "/google.cloud.dataqna.v1alpha.QuestionService/CreateQuestion"
    	QuestionService_ExecuteQuestion_FullMethodName    = "/google.cloud.dataqna.v1alpha.QuestionService/ExecuteQuestion"
    	QuestionService_GetUserFeedback_FullMethodName    = "/google.cloud.dataqna.v1alpha.QuestionService/GetUserFeedback"
    	QuestionService_UpdateUserFeedback_FullMethodName = "/google.cloud.dataqna.v1alpha.QuestionService/UpdateUserFeedback"
    )

### AutoSuggestionService_SuggestQueries_FullMethodName
    
    
    const (
    	AutoSuggestionService_SuggestQueries_FullMethodName = "/google.cloud.dataqna.v1alpha.AutoSuggestionService/SuggestQueries"
    )

## Variables 

### AnnotatedString_SemanticMarkupType_name, AnnotatedString_SemanticMarkupType_value
    
    
    var (
    	AnnotatedString_SemanticMarkupType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MARKUP_TYPE_UNSPECIFIED",
    		1: "METRIC",
    		2: "DIMENSION",
    		3: "FILTER",
    		4: "UNUSED",
    		5: "BLOCKED",
    		6: "ROW",
    	}
    	AnnotatedString_SemanticMarkupType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MARKUP_TYPE_UNSPECIFIED": 0,
    		"METRIC":                  1,
    		"DIMENSION":               2,
    		"FILTER":                  3,
    		"UNUSED":                  4,
    		"BLOCKED":                 5,
    		"ROW":                     6,
    	}
    )

Enum value maps for AnnotatedString_SemanticMarkupType.

### SuggestionType_name, SuggestionType_value
    
    
    var (
    	SuggestionType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SUGGESTION_TYPE_UNSPECIFIED",
    		1: "ENTITY",
    		2: "TEMPLATE",
    	}
    	SuggestionType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SUGGESTION_TYPE_UNSPECIFIED": 0,
    		"ENTITY":                      1,
    		"TEMPLATE":                    2,
    	}
    )

Enum value maps for SuggestionType.

### InterpretEntity_name, InterpretEntity_value
    
    
    var (
    	InterpretEntity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INTERPRET_ENTITY_UNSPECIFIED",
    		1: "DIMENSION",
    		2: "METRIC",
    	}
    	InterpretEntity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INTERPRET_ENTITY_UNSPECIFIED": 0,
    		"DIMENSION":                    1,
    		"METRIC":                       2,
    	}
    )

Enum value maps for InterpretEntity.

### InterpretError_InterpretErrorCode_name, InterpretError_InterpretErrorCode_value
    
    
    var (
    	InterpretError_InterpretErrorCode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INTERPRET_ERROR_CODE_UNSPECIFIED",
    		1: "INVALID_QUERY",
    		2: "FAILED_TO_UNDERSTAND",
    		3: "FAILED_TO_ANSWER",
    	}
    	InterpretError_InterpretErrorCode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INTERPRET_ERROR_CODE_UNSPECIFIED": 0,
    		"INVALID_QUERY":                    1,
    		"FAILED_TO_UNDERSTAND":             2,
    		"FAILED_TO_ANSWER":                 3,
    	}
    )

Enum value maps for InterpretError_InterpretErrorCode.

### ExecutionInfo_JobExecutionState_name, ExecutionInfo_JobExecutionState_value
    
    
    var (
    	ExecutionInfo_JobExecutionState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "JOB_EXECUTION_STATE_UNSPECIFIED",
    		1: "NOT_EXECUTED",
    		2: "RUNNING",
    		3: "SUCCEEDED",
    		4: "FAILED",
    	}
    	ExecutionInfo_JobExecutionState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"JOB_EXECUTION_STATE_UNSPECIFIED": 0,
    		"NOT_EXECUTED":                    1,
    		"RUNNING":                         2,
    		"SUCCEEDED":                       3,
    		"FAILED":                          4,
    	}
    )

Enum value maps for ExecutionInfo_JobExecutionState.

### InterpretationStructure_VisualizationType_name, InterpretationStructure_VisualizationType_value
    
    
    var (
    	InterpretationStructure_VisualizationType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "VISUALIZATION_TYPE_UNSPECIFIED",
    		1:  "TABLE",
    		2:  "BAR_CHART",
    		3:  "COLUMN_CHART",
    		4:  "TIMELINE",
    		5:  "SCATTER_PLOT",
    		6:  "PIE_CHART",
    		7:  "LINE_CHART",
    		8:  "AREA_CHART",
    		9:  "COMBO_CHART",
    		10: "HISTOGRAM",
    		11: "GENERIC_CHART",
    		12: "CHART_NOT_UNDERSTOOD",
    	}
    	InterpretationStructure_VisualizationType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"VISUALIZATION_TYPE_UNSPECIFIED": 0,
    		"TABLE":                          1,
    		"BAR_CHART":                      2,
    		"COLUMN_CHART":                   3,
    		"TIMELINE":                       4,
    		"SCATTER_PLOT":                   5,
    		"PIE_CHART":                      6,
    		"LINE_CHART":                     7,
    		"AREA_CHART":                     8,
    		"COMBO_CHART":                    9,
    		"HISTOGRAM":                      10,
    		"GENERIC_CHART":                  11,
    		"CHART_NOT_UNDERSTOOD":           12,
    	}
    )

Enum value maps for InterpretationStructure_VisualizationType.

### UserFeedback_UserFeedbackRating_name, UserFeedback_UserFeedbackRating_value
    
    
    var (
    	UserFeedback_UserFeedbackRating_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "USER_FEEDBACK_RATING_UNSPECIFIED",
    		1: "POSITIVE",
    		2: "NEGATIVE",
    	}
    	UserFeedback_UserFeedbackRating_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"USER_FEEDBACK_RATING_UNSPECIFIED": 0,
    		"POSITIVE":                         1,
    		"NEGATIVE":                         2,
    	}
    )

Enum value maps for UserFeedback_UserFeedbackRating.

### AutoSuggestionService_ServiceDesc
    
    
    var AutoSuggestionService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.dataqna.v1alpha.AutoSuggestionService",
    	HandlerType: (*AutoSuggestionServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "SuggestQueries",
    			Handler:    _AutoSuggestionService_SuggestQueries_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/dataqna/v1alpha/auto_suggestion_service.proto",
    }

AutoSuggestionService_ServiceDesc is the grpc.ServiceDesc for AutoSuggestionService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_dataqna_v1alpha_annotated_string_proto
    
    
    var File_google_cloud_dataqna_v1alpha_annotated_string_proto protoreflect.FileDescriptor

### File_google_cloud_dataqna_v1alpha_auto_suggestion_service_proto
    
    
    var File_google_cloud_dataqna_v1alpha_auto_suggestion_service_proto protoreflect.FileDescriptor

### File_google_cloud_dataqna_v1alpha_question_proto
    
    
    var File_google_cloud_dataqna_v1alpha_question_proto protoreflect.FileDescriptor

### File_google_cloud_dataqna_v1alpha_question_service_proto
    
    
    var File_google_cloud_dataqna_v1alpha_question_service_proto protoreflect.FileDescriptor

### File_google_cloud_dataqna_v1alpha_user_feedback_proto
    
    
    var File_google_cloud_dataqna_v1alpha_user_feedback_proto protoreflect.FileDescriptor

### QuestionService_ServiceDesc
    
    
    var QuestionService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.dataqna.v1alpha.QuestionService",
    	HandlerType: (*QuestionServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "GetQuestion",
    			Handler:    _QuestionService_GetQuestion_Handler,
    		},
    		{
    			MethodName: "CreateQuestion",
    			Handler:    _QuestionService_CreateQuestion_Handler,
    		},
    		{
    			MethodName: "ExecuteQuestion",
    			Handler:    _QuestionService_ExecuteQuestion_Handler,
    		},
    		{
    			MethodName: "GetUserFeedback",
    			Handler:    _QuestionService_GetUserFeedback_Handler,
    		},
    		{
    			MethodName: "UpdateUserFeedback",
    			Handler:    _QuestionService_UpdateUserFeedback_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/dataqna/v1alpha/question_service.proto",
    }

QuestionService_ServiceDesc is the grpc.ServiceDesc for QuestionService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterAutoSuggestionServiceServer 
    
    
    func RegisterAutoSuggestionServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv AutoSuggestionServiceServer)

### func RegisterQuestionServiceServer 
    
    
    func RegisterQuestionServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv QuestionServiceServer)

## AnnotatedString
    
    
    type AnnotatedString struct {
    
    	// Text version of the string.
    	TextFormatted [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=text_formatted,json=textFormatted,proto3" json:"text_formatted,omitempty"`
    	// HTML version of the string annotation.
    	HtmlFormatted [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=html_formatted,json=htmlFormatted,proto3" json:"html_formatted,omitempty"`
    	// Semantic version of the string annotation.
    	Markups []*AnnotatedString_SemanticMarkup `protobuf:"bytes,3,rep,name=markups,proto3" json:"markups,omitempty"`
    	// contains filtered or unexported fields
    }

Describes string annotation from both semantic and formatting perspectives. Example:

User Query:
    
    
    top countries by population in Africa
    
    0   4         14 17         28 31    37
    

Table Data:

  * "country" - dimension
  * "population" - metric
  * "Africa" - value in the "continent" column



text_formatted = `"top countries by population in Africa"`

html_formatted =
    
    
    `"top <b>countries</b> by <b>population</b> in <i>Africa</i>"`
    
    
    
    markups = [
    
        {DIMENSION, 4, 12}, // 'countries'
        {METRIC, 17, 26}, // 'population'
        {FILTER, 31, 36}  // 'Africa'
    
    ]
    

Note that html formattings for 'DIMENSION' and 'METRIC' are the same, while semantic markups are different.

### func (*AnnotatedString) Descriptor 
    
    
    func (*AnnotatedString) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotatedString.ProtoReflect.Descriptor instead.

### func (*AnnotatedString) GetHtmlFormatted 
    
    
    func (x *AnnotatedString) GetHtmlFormatted() [string](https://pkg.go.dev/builtin#string)

### func (*AnnotatedString) GetMarkups 
    
    
    func (x *AnnotatedString) GetMarkups() []*AnnotatedString_SemanticMarkup

### func (*AnnotatedString) GetTextFormatted 
    
    
    func (x *AnnotatedString) GetTextFormatted() [string](https://pkg.go.dev/builtin#string)

### func (*AnnotatedString) ProtoMessage 
    
    
    func (*AnnotatedString) ProtoMessage()

### func (*AnnotatedString) ProtoReflect 
    
    
    func (x *AnnotatedString) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AnnotatedString) Reset 
    
    
    func (x *AnnotatedString) Reset()

### func (*AnnotatedString) String 
    
    
    func (x *AnnotatedString) String() [string](https://pkg.go.dev/builtin#string)

## AnnotatedString_SemanticMarkup
    
    
    type AnnotatedString_SemanticMarkup struct {
    
    	// The semantic type of the markup substring.
    	Type AnnotatedString_SemanticMarkupType `protobuf:"varint,1,opt,name=type,proto3,enum=google.cloud.dataqna.v1alpha.AnnotatedString_SemanticMarkupType" json:"type,omitempty"`
    	// Unicode character index of the query.
    	StartCharIndex [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=start_char_index,json=startCharIndex,proto3" json:"start_char_index,omitempty"`
    	// The length (number of unicode characters) of the markup substring.
    	Length [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=length,proto3" json:"length,omitempty"`
    	// contains filtered or unexported fields
    }

Semantic markup denotes a substring (by index and length) with markup information.

### func (*AnnotatedString_SemanticMarkup) Descriptor 
    
    
    func (*AnnotatedString_SemanticMarkup) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotatedString_SemanticMarkup.ProtoReflect.Descriptor instead.

### func (*AnnotatedString_SemanticMarkup) GetLength 
    
    
    func (x *AnnotatedString_SemanticMarkup) GetLength() [int32](https://pkg.go.dev/builtin#int32)

### func (*AnnotatedString_SemanticMarkup) GetStartCharIndex 
    
    
    func (x *AnnotatedString_SemanticMarkup) GetStartCharIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*AnnotatedString_SemanticMarkup) GetType 
    
    
    func (x *AnnotatedString_SemanticMarkup) GetType() AnnotatedString_SemanticMarkupType

### func (*AnnotatedString_SemanticMarkup) ProtoMessage 
    
    
    func (*AnnotatedString_SemanticMarkup) ProtoMessage()

### func (*AnnotatedString_SemanticMarkup) ProtoReflect 
    
    
    func (x *AnnotatedString_SemanticMarkup) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AnnotatedString_SemanticMarkup) Reset 
    
    
    func (x *AnnotatedString_SemanticMarkup) Reset()

### func (*AnnotatedString_SemanticMarkup) String 
    
    
    func (x *AnnotatedString_SemanticMarkup) String() [string](https://pkg.go.dev/builtin#string)

## AnnotatedString_SemanticMarkupType
    
    
    type AnnotatedString_SemanticMarkupType [int32](https://pkg.go.dev/builtin#int32)

Semantic markup types.

### AnnotatedString_MARKUP_TYPE_UNSPECIFIED, AnnotatedString_METRIC, AnnotatedString_DIMENSION, AnnotatedString_FILTER, AnnotatedString_UNUSED, AnnotatedString_BLOCKED, AnnotatedString_ROW
    
    
    const (
    	// No markup type was specified.
    	AnnotatedString_MARKUP_TYPE_UNSPECIFIED AnnotatedString_SemanticMarkupType = 0
    	// Markup for a substring denoting a metric.
    	AnnotatedString_METRIC AnnotatedString_SemanticMarkupType = 1
    	// Markup for a substring denoting a dimension.
    	AnnotatedString_DIMENSION AnnotatedString_SemanticMarkupType = 2
    	// Markup for a substring denoting a filter.
    	AnnotatedString_FILTER AnnotatedString_SemanticMarkupType = 3
    	// Markup for an unused substring.
    	AnnotatedString_UNUSED AnnotatedString_SemanticMarkupType = 4
    	// Markup for a substring containing blocked phrases.
    	AnnotatedString_BLOCKED AnnotatedString_SemanticMarkupType = 5
    	// Markup for a substring that contains terms for row.
    	AnnotatedString_ROW AnnotatedString_SemanticMarkupType = 6
    )

### func (AnnotatedString_SemanticMarkupType) Descriptor 
    
    
    func (AnnotatedString_SemanticMarkupType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AnnotatedString_SemanticMarkupType) Enum 
    
    
    func (x AnnotatedString_SemanticMarkupType) Enum() *AnnotatedString_SemanticMarkupType

### func (AnnotatedString_SemanticMarkupType) EnumDescriptor 
    
    
    func (AnnotatedString_SemanticMarkupType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AnnotatedString_SemanticMarkupType.Descriptor instead.

### func (AnnotatedString_SemanticMarkupType) Number 
    
    
    func (x AnnotatedString_SemanticMarkupType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AnnotatedString_SemanticMarkupType) String 
    
    
    func (x AnnotatedString_SemanticMarkupType) String() [string](https://pkg.go.dev/builtin#string)

### func (AnnotatedString_SemanticMarkupType) Type 
    
    
    func (AnnotatedString_SemanticMarkupType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AutoSuggestionServiceClient
    
    
    type AutoSuggestionServiceClient interface {
    	// Gets a list of suggestions based on a prefix string.
    	// AutoSuggestion tolerance should be less than 1 second.
    	SuggestQueries(ctx context.Context, in *SuggestQueriesRequest, opts ...grpc.CallOption) (*SuggestQueriesResponse, [error](https://pkg.go.dev/builtin#error))
    }

AutoSuggestionServiceClient is the client API for AutoSuggestionService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewAutoSuggestionServiceClient 
    
    
    func NewAutoSuggestionServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) AutoSuggestionServiceClient

## AutoSuggestionServiceServer
    
    
    type AutoSuggestionServiceServer interface {
    	// Gets a list of suggestions based on a prefix string.
    	// AutoSuggestion tolerance should be less than 1 second.
    	SuggestQueries(context.Context, *SuggestQueriesRequest) (*SuggestQueriesResponse, [error](https://pkg.go.dev/builtin#error))
    }

AutoSuggestionServiceServer is the server API for AutoSuggestionService service. All implementations should embed UnimplementedAutoSuggestionServiceServer for forward compatibility

## BigQueryJob
    
    
    type BigQueryJob struct {
    
    	// The job ID.
    	JobId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=job_id,json=jobId,proto3" json:"job_id,omitempty"`
    	// The project ID of the job.
    	ProjectId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
    	// The location where the job is running.
    	Location [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=location,proto3" json:"location,omitempty"`
    	// contains filtered or unexported fields
    }

BigQuery job information. This can be used to query the BigQuery API and retrieve the current job's status (using [jobs.get](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get)).

### func (*BigQueryJob) Descriptor 
    
    
    func (*BigQueryJob) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BigQueryJob.ProtoReflect.Descriptor instead.

### func (*BigQueryJob) GetJobId 
    
    
    func (x *BigQueryJob) GetJobId() [string](https://pkg.go.dev/builtin#string)

### func (*BigQueryJob) GetLocation 
    
    
    func (x *BigQueryJob) GetLocation() [string](https://pkg.go.dev/builtin#string)

### func (*BigQueryJob) GetProjectId 
    
    
    func (x *BigQueryJob) GetProjectId() [string](https://pkg.go.dev/builtin#string)

### func (*BigQueryJob) ProtoMessage 
    
    
    func (*BigQueryJob) ProtoMessage()

### func (*BigQueryJob) ProtoReflect 
    
    
    func (x *BigQueryJob) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BigQueryJob) Reset 
    
    
    func (x *BigQueryJob) Reset()

### func (*BigQueryJob) String 
    
    
    func (x *BigQueryJob) String() [string](https://pkg.go.dev/builtin#string)

## CreateQuestionRequest
    
    
    type CreateQuestionRequest struct {
    
    	// Required. The name of the project this data source reference belongs to.
    	// Example: `projects/foo/locations/bar`
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The question to create.
    	Question *Question `protobuf:"bytes,2,opt,name=question,proto3" json:"question,omitempty"`
    	// contains filtered or unexported fields
    }

Request to create a question resource.

### func (*CreateQuestionRequest) Descriptor 
    
    
    func (*CreateQuestionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateQuestionRequest.ProtoReflect.Descriptor instead.

### func (*CreateQuestionRequest) GetParent 
    
    
    func (x *CreateQuestionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateQuestionRequest) GetQuestion 
    
    
    func (x *CreateQuestionRequest) GetQuestion() *Question

### func (*CreateQuestionRequest) ProtoMessage 
    
    
    func (*CreateQuestionRequest) ProtoMessage()

### func (*CreateQuestionRequest) ProtoReflect 
    
    
    func (x *CreateQuestionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateQuestionRequest) Reset 
    
    
    func (x *CreateQuestionRequest) Reset()

### func (*CreateQuestionRequest) String 
    
    
    func (x *CreateQuestionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DataQuery
    
    
    type DataQuery struct {
    
    	// The generated SQL query to be sent to the backend.
    	Sql [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=sql,proto3" json:"sql,omitempty"`
    	// contains filtered or unexported fields
    }

Representation of the data query for the backend. This is provided for informational purposes only. Clients should not use it to send it to the backend directly, but rather use the `execute` RPC to trigger the execution. Using the `execute` RPC is needed in order to track the state of a question and report on it correctly to the data administrators.

### func (*DataQuery) Descriptor 
    
    
    func (*DataQuery) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DataQuery.ProtoReflect.Descriptor instead.

### func (*DataQuery) GetSql 
    
    
    func (x *DataQuery) GetSql() [string](https://pkg.go.dev/builtin#string)

### func (*DataQuery) ProtoMessage 
    
    
    func (*DataQuery) ProtoMessage()

### func (*DataQuery) ProtoReflect 
    
    
    func (x *DataQuery) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DataQuery) Reset 
    
    
    func (x *DataQuery) Reset()

### func (*DataQuery) String 
    
    
    func (x *DataQuery) String() [string](https://pkg.go.dev/builtin#string)

## DebugFlags
    
    
    type DebugFlags struct {
    
    	// Whether to include the original VAQuery.
    	IncludeVaQuery [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=include_va_query,json=includeVaQuery,proto3" json:"include_va_query,omitempty"`
    	// Whether to include the original nested VAQuery.
    	IncludeNestedVaQuery [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=include_nested_va_query,json=includeNestedVaQuery,proto3" json:"include_nested_va_query,omitempty"`
    	// Whether to include the original human interpretation strings generated
    	// by Analyza.
    	IncludeHumanInterpretation [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=include_human_interpretation,json=includeHumanInterpretation,proto3" json:"include_human_interpretation,omitempty"`
    	// Whether to include the Aqua debug response.
    	IncludeAquaDebugResponse [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=include_aqua_debug_response,json=includeAquaDebugResponse,proto3" json:"include_aqua_debug_response,omitempty"`
    	// The time in milliseconds from Unix epoch to be used
    	// to process the query. This is useful for testing
    	// the queries at different time period.
    	// If not set or time_override <= 0,="" then="" the="" current="" time="" is="" used.="" timeoverride="">[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=time_override,json=timeOverride,proto3" json:"time_override,omitempty"`
    	// Set to true if request is initiated by an internal Google user.
    	IsInternalGoogleUser [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=is_internal_google_user,json=isInternalGoogleUser,proto3" json:"is_internal_google_user,omitempty"`
    	// Determines whether cache needs to be ignored. If set to
    	// true, cache won't be queried and updated.
    	IgnoreCache [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,7,opt,name=ignore_cache,json=ignoreCache,proto3" json:"ignore_cache,omitempty"`
    	// Whether to include the request/response pair from the call to the
    	// EntityIndex for SearchEntities.
    	IncludeSearchEntitiesRpc [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,8,opt,name=include_search_entities_rpc,json=includeSearchEntitiesRpc,proto3" json:"include_search_entities_rpc,omitempty"`
    	// Whether to include the request/response pair from the call to the
    	// Annotations service for ListColumnAnnotations.
    	IncludeListColumnAnnotationsRpc [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,9,opt,name=include_list_column_annotations_rpc,json=includeListColumnAnnotationsRpc,proto3" json:"include_list_column_annotations_rpc,omitempty"`
    	// Whether to include the entity list passed to Analyza.
    	IncludeVirtualAnalystEntities [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,10,opt,name=include_virtual_analyst_entities,json=includeVirtualAnalystEntities,proto3" json:"include_virtual_analyst_entities,omitempty"`
    	// Whether to include the table list.
    	IncludeTableList [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,11,opt,name=include_table_list,json=includeTableList,proto3" json:"include_table_list,omitempty"`
    	// Whether to include the domain list.
    	IncludeDomainList [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=include_domain_list,json=includeDomainList,proto3" json:"include_domain_list,omitempty"`
    	// contains filtered or unexported fields
    }

Configuriation of debug flags.

### func (*DebugFlags) Descriptor 
    
    
    func (*DebugFlags) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DebugFlags.ProtoReflect.Descriptor instead.

### func (*DebugFlags) GetIgnoreCache 
    
    
    func (x *DebugFlags) GetIgnoreCache() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeAquaDebugResponse 
    
    
    func (x *DebugFlags) GetIncludeAquaDebugResponse() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeDomainList 
    
    
    func (x *DebugFlags) GetIncludeDomainList() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeHumanInterpretation 
    
    
    func (x *DebugFlags) GetIncludeHumanInterpretation() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeListColumnAnnotationsRpc 
    
    
    func (x *DebugFlags) GetIncludeListColumnAnnotationsRpc() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeNestedVaQuery 
    
    
    func (x *DebugFlags) GetIncludeNestedVaQuery() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeSearchEntitiesRpc 
    
    
    func (x *DebugFlags) GetIncludeSearchEntitiesRpc() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeTableList 
    
    
    func (x *DebugFlags) GetIncludeTableList() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeVaQuery 
    
    
    func (x *DebugFlags) GetIncludeVaQuery() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIncludeVirtualAnalystEntities 
    
    
    func (x *DebugFlags) GetIncludeVirtualAnalystEntities() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetIsInternalGoogleUser 
    
    
    func (x *DebugFlags) GetIsInternalGoogleUser() [bool](https://pkg.go.dev/builtin#bool)

### func (*DebugFlags) GetTimeOverride 
    
    
    func (x *DebugFlags) GetTimeOverride() [int64](https://pkg.go.dev/builtin#int64)

### func (*DebugFlags) ProtoMessage 
    
    
    func (*DebugFlags) ProtoMessage()

### func (*DebugFlags) ProtoReflect 
    
    
    func (x *DebugFlags) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DebugFlags) Reset 
    
    
    func (x *DebugFlags) Reset()

### func (*DebugFlags) String 
    
    
    func (x *DebugFlags) String() [string](https://pkg.go.dev/builtin#string)

## ExecuteQuestionRequest
    
    
    type ExecuteQuestionRequest struct {
    
    	// Required. The unique identifier for the question.
    	// Example: `projects/foo/locations/bar/questions/1234`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Index of the interpretation to execute.
    	InterpretationIndex [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=interpretation_index,json=interpretationIndex,proto3" json:"interpretation_index,omitempty"`
    	// contains filtered or unexported fields
    }

Request to execute an interpretation.

### func (*ExecuteQuestionRequest) Descriptor 
    
    
    func (*ExecuteQuestionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExecuteQuestionRequest.ProtoReflect.Descriptor instead.

### func (*ExecuteQuestionRequest) GetInterpretationIndex 
    
    
    func (x *ExecuteQuestionRequest) GetInterpretationIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*ExecuteQuestionRequest) GetName 
    
    
    func (x *ExecuteQuestionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ExecuteQuestionRequest) ProtoMessage 
    
    
    func (*ExecuteQuestionRequest) ProtoMessage()

### func (*ExecuteQuestionRequest) ProtoReflect 
    
    
    func (x *ExecuteQuestionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ExecuteQuestionRequest) Reset 
    
    
    func (x *ExecuteQuestionRequest) Reset()

### func (*ExecuteQuestionRequest) String 
    
    
    func (x *ExecuteQuestionRequest) String() [string](https://pkg.go.dev/builtin#string)

## ExecutionInfo
    
    
    type ExecutionInfo struct {
    
    	// Status returned by the backend when the job was created.
    	JobCreationStatus *status.Status `protobuf:"bytes,1,opt,name=job_creation_status,json=jobCreationStatus,proto3" json:"job_creation_status,omitempty"`
    	// Status of the job execution.
    	JobExecutionState ExecutionInfo_JobExecutionState `protobuf:"varint,2,opt,name=job_execution_state,json=jobExecutionState,proto3,enum=google.cloud.dataqna.v1alpha.ExecutionInfo_JobExecutionState" json:"job_execution_state,omitempty"`
    	// Time when the execution was triggered.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// BigQuery job information.
    	// Future versions will have different backends. Hence, clients must make sure
    	// they can handle it when this field is not populated.
    	BigqueryJob *BigQueryJob `protobuf:"bytes,4,opt,name=bigquery_job,json=bigqueryJob,proto3" json:"bigquery_job,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the backend status (such as BigQuery) of the execution.

### func (*ExecutionInfo) Descriptor 
    
    
    func (*ExecutionInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExecutionInfo.ProtoReflect.Descriptor instead.

### func (*ExecutionInfo) GetBigqueryJob 
    
    
    func (x *ExecutionInfo) GetBigqueryJob() *BigQueryJob

### func (*ExecutionInfo) GetCreateTime 
    
    
    func (x *ExecutionInfo) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ExecutionInfo) GetJobCreationStatus 
    
    
    func (x *ExecutionInfo) GetJobCreationStatus() *[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*ExecutionInfo) GetJobExecutionState 
    
    
    func (x *ExecutionInfo) GetJobExecutionState() ExecutionInfo_JobExecutionState

### func (*ExecutionInfo) ProtoMessage 
    
    
    func (*ExecutionInfo) ProtoMessage()

### func (*ExecutionInfo) ProtoReflect 
    
    
    func (x *ExecutionInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ExecutionInfo) Reset 
    
    
    func (x *ExecutionInfo) Reset()

### func (*ExecutionInfo) String 
    
    
    func (x *ExecutionInfo) String() [string](https://pkg.go.dev/builtin#string)

## ExecutionInfo_JobExecutionState
    
    
    type ExecutionInfo_JobExecutionState [int32](https://pkg.go.dev/builtin#int32)

Enum of possible job execution statuses.

### ExecutionInfo_JOB_EXECUTION_STATE_UNSPECIFIED, ExecutionInfo_NOT_EXECUTED, ExecutionInfo_RUNNING, ExecutionInfo_SUCCEEDED, ExecutionInfo_FAILED
    
    
    const (
    	// No job execution was specified.
    	ExecutionInfo_JOB_EXECUTION_STATE_UNSPECIFIED ExecutionInfo_JobExecutionState = 0
    	// No job execution was requested, yet.
    	ExecutionInfo_NOT_EXECUTED ExecutionInfo_JobExecutionState = 1
    	// The job is running.
    	ExecutionInfo_RUNNING ExecutionInfo_JobExecutionState = 2
    	// The job completed successfully.
    	ExecutionInfo_SUCCEEDED ExecutionInfo_JobExecutionState = 3
    	// The job completed unsuccessfully.
    	ExecutionInfo_FAILED ExecutionInfo_JobExecutionState = 4
    )

### func (ExecutionInfo_JobExecutionState) Descriptor 
    
    
    func (ExecutionInfo_JobExecutionState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ExecutionInfo_JobExecutionState) Enum 
    
    
    func (x ExecutionInfo_JobExecutionState) Enum() *ExecutionInfo_JobExecutionState

### func (ExecutionInfo_JobExecutionState) EnumDescriptor 
    
    
    func (ExecutionInfo_JobExecutionState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExecutionInfo_JobExecutionState.Descriptor instead.

### func (ExecutionInfo_JobExecutionState) Number 
    
    
    func (x ExecutionInfo_JobExecutionState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ExecutionInfo_JobExecutionState) String 
    
    
    func (x ExecutionInfo_JobExecutionState) String() [string](https://pkg.go.dev/builtin#string)

### func (ExecutionInfo_JobExecutionState) Type 
    
    
    func (ExecutionInfo_JobExecutionState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GetQuestionRequest
    
    
    type GetQuestionRequest struct {
    
    	// Required. The unique identifier for the question.
    	// Example: `projects/foo/locations/bar/questions/1234`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The list of fields to be retrieved.
    	ReadMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=read_mask,json=readMask,proto3" json:"read_mask,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a previously created question.

### func (*GetQuestionRequest) Descriptor 
    
    
    func (*GetQuestionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetQuestionRequest.ProtoReflect.Descriptor instead.

### func (*GetQuestionRequest) GetName 
    
    
    func (x *GetQuestionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetQuestionRequest) GetReadMask 
    
    
    func (x *GetQuestionRequest) GetReadMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*GetQuestionRequest) ProtoMessage 
    
    
    func (*GetQuestionRequest) ProtoMessage()

### func (*GetQuestionRequest) ProtoReflect 
    
    
    func (x *GetQuestionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetQuestionRequest) Reset 
    
    
    func (x *GetQuestionRequest) Reset()

### func (*GetQuestionRequest) String 
    
    
    func (x *GetQuestionRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetUserFeedbackRequest
    
    
    type GetUserFeedbackRequest struct {
    
    	// Required. The unique identifier for the user feedback.
    	// User feedback is a singleton resource on a Question.
    	// Example: `projects/foo/locations/bar/questions/1234/userFeedback`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get user feedback.

### func (*GetUserFeedbackRequest) Descriptor 
    
    
    func (*GetUserFeedbackRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetUserFeedbackRequest.ProtoReflect.Descriptor instead.

### func (*GetUserFeedbackRequest) GetName 
    
    
    func (x *GetUserFeedbackRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetUserFeedbackRequest) ProtoMessage 
    
    
    func (*GetUserFeedbackRequest) ProtoMessage()

### func (*GetUserFeedbackRequest) ProtoReflect 
    
    
    func (x *GetUserFeedbackRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetUserFeedbackRequest) Reset 
    
    
    func (x *GetUserFeedbackRequest) Reset()

### func (*GetUserFeedbackRequest) String 
    
    
    func (x *GetUserFeedbackRequest) String() [string](https://pkg.go.dev/builtin#string)

## HumanReadable
    
    
    type HumanReadable struct {
    
    	// Generated query explaining the interpretation.
    	GeneratedInterpretation *AnnotatedString `protobuf:"bytes,1,opt,name=generated_interpretation,json=generatedInterpretation,proto3" json:"generated_interpretation,omitempty"`
    	// Annotations on the original query.
    	OriginalQuestion *AnnotatedString `protobuf:"bytes,2,opt,name=original_question,json=originalQuestion,proto3" json:"original_question,omitempty"`
    	// contains filtered or unexported fields
    }

Human readable interpretation.

### func (*HumanReadable) Descriptor 
    
    
    func (*HumanReadable) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HumanReadable.ProtoReflect.Descriptor instead.

### func (*HumanReadable) GetGeneratedInterpretation 
    
    
    func (x *HumanReadable) GetGeneratedInterpretation() *AnnotatedString

### func (*HumanReadable) GetOriginalQuestion 
    
    
    func (x *HumanReadable) GetOriginalQuestion() *AnnotatedString

### func (*HumanReadable) ProtoMessage 
    
    
    func (*HumanReadable) ProtoMessage()

### func (*HumanReadable) ProtoReflect 
    
    
    func (x *HumanReadable) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HumanReadable) Reset 
    
    
    func (x *HumanReadable) Reset()

### func (*HumanReadable) String 
    
    
    func (x *HumanReadable) String() [string](https://pkg.go.dev/builtin#string)

## InterpretEntity
    
    
    type InterpretEntity [int32](https://pkg.go.dev/builtin#int32)

Query entities of an interpretation.

### InterpretEntity_INTERPRET_ENTITY_UNSPECIFIED, InterpretEntity_DIMENSION, InterpretEntity_METRIC
    
    
    const (
    	// No interpret entity was specified.
    	InterpretEntity_INTERPRET_ENTITY_UNSPECIFIED InterpretEntity = 0
    	// A dimenstion entity.
    	InterpretEntity_DIMENSION InterpretEntity = 1
    	// A metric entity.
    	InterpretEntity_METRIC InterpretEntity = 2
    )

### func (InterpretEntity) Descriptor 
    
    
    func (InterpretEntity) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InterpretEntity) Enum 
    
    
    func (x InterpretEntity) Enum() *InterpretEntity

### func (InterpretEntity) EnumDescriptor 
    
    
    func (InterpretEntity) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretEntity.Descriptor instead.

### func (InterpretEntity) Number 
    
    
    func (x InterpretEntity) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InterpretEntity) String 
    
    
    func (x InterpretEntity) String() [string](https://pkg.go.dev/builtin#string)

### func (InterpretEntity) Type 
    
    
    func (InterpretEntity) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## InterpretError
    
    
    type InterpretError struct {
    
    	// Error message explaining why this question could not be interpreted.
    	Message [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
    	// The code for the error category why the interpretation failed.
    	Code InterpretError_InterpretErrorCode `protobuf:"varint,2,opt,name=code,proto3,enum=google.cloud.dataqna.v1alpha.InterpretError_InterpretErrorCode" json:"code,omitempty"`
    	// Details on interpretation failure.
    	Details *InterpretError_InterpretErrorDetails `protobuf:"bytes,3,opt,name=details,proto3" json:"details,omitempty"`
    	// contains filtered or unexported fields
    }

Details on the failure to interpret the question.

### func (*InterpretError) Descriptor 
    
    
    func (*InterpretError) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError.ProtoReflect.Descriptor instead.

### func (*InterpretError) GetCode 
    
    
    func (x *InterpretError) GetCode() InterpretError_InterpretErrorCode

### func (*InterpretError) GetDetails 
    
    
    func (x *InterpretError) GetDetails() *InterpretError_InterpretErrorDetails

### func (*InterpretError) GetMessage 
    
    
    func (x *InterpretError) GetMessage() [string](https://pkg.go.dev/builtin#string)

### func (*InterpretError) ProtoMessage 
    
    
    func (*InterpretError) ProtoMessage()

### func (*InterpretError) ProtoReflect 
    
    
    func (x *InterpretError) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretError) Reset 
    
    
    func (x *InterpretError) Reset()

### func (*InterpretError) String 
    
    
    func (x *InterpretError) String() [string](https://pkg.go.dev/builtin#string)

## InterpretError_InterpretAmbiguityDetails
    
    
    type InterpretError_InterpretAmbiguityDetails struct {
    	// contains filtered or unexported fields
    }

Details about a query that was too ambiguous. Currently, the message has no fields and its presence signals that there was ambiguity.

### func (*InterpretError_InterpretAmbiguityDetails) Descriptor 
    
    
    func (*InterpretError_InterpretAmbiguityDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError_InterpretAmbiguityDetails.ProtoReflect.Descriptor instead.

### func (*InterpretError_InterpretAmbiguityDetails) ProtoMessage 
    
    
    func (*InterpretError_InterpretAmbiguityDetails) ProtoMessage()

### func (*InterpretError_InterpretAmbiguityDetails) ProtoReflect 
    
    
    func (x *InterpretError_InterpretAmbiguityDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretError_InterpretAmbiguityDetails) Reset 
    
    
    func (x *InterpretError_InterpretAmbiguityDetails) Reset()

### func (*InterpretError_InterpretAmbiguityDetails) String 
    
    
    func (x *InterpretError_InterpretAmbiguityDetails) String() [string](https://pkg.go.dev/builtin#string)

## InterpretError_InterpretErrorCode
    
    
    type InterpretError_InterpretErrorCode [int32](https://pkg.go.dev/builtin#int32)

The interpret error code provides an error category why the interpretation failed.

### InterpretError_INTERPRET_ERROR_CODE_UNSPECIFIED, InterpretError_INVALID_QUERY, InterpretError_FAILED_TO_UNDERSTAND, InterpretError_FAILED_TO_ANSWER
    
    
    const (
    	// No interpret error code was specified.
    	InterpretError_INTERPRET_ERROR_CODE_UNSPECIFIED InterpretError_InterpretErrorCode = 0
    	// The query is not valid.
    	InterpretError_INVALID_QUERY InterpretError_InterpretErrorCode = 1
    	// The interpreter failed to understand the question. For example, because
    	// it was too ambiguous.
    	InterpretError_FAILED_TO_UNDERSTAND InterpretError_InterpretErrorCode = 2
    	// The interpreter could understand the question, but was not able to arrive
    	// at an answer. For example, because a requested operation is not
    	// supported.
    	InterpretError_FAILED_TO_ANSWER InterpretError_InterpretErrorCode = 3
    )

### func (InterpretError_InterpretErrorCode) Descriptor 
    
    
    func (InterpretError_InterpretErrorCode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InterpretError_InterpretErrorCode) Enum 
    
    
    func (x InterpretError_InterpretErrorCode) Enum() *InterpretError_InterpretErrorCode

### func (InterpretError_InterpretErrorCode) EnumDescriptor 
    
    
    func (InterpretError_InterpretErrorCode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError_InterpretErrorCode.Descriptor instead.

### func (InterpretError_InterpretErrorCode) Number 
    
    
    func (x InterpretError_InterpretErrorCode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InterpretError_InterpretErrorCode) String 
    
    
    func (x InterpretError_InterpretErrorCode) String() [string](https://pkg.go.dev/builtin#string)

### func (InterpretError_InterpretErrorCode) Type 
    
    
    func (InterpretError_InterpretErrorCode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## InterpretError_InterpretErrorDetails
    
    
    type InterpretError_InterpretErrorDetails struct {
    
    	// Populated if parts of the query are unsupported.
    	UnsupportedDetails *InterpretError_InterpretUnsupportedDetails `protobuf:"bytes,1,opt,name=unsupported_details,json=unsupportedDetails,proto3" json:"unsupported_details,omitempty"`
    	// Populated if the query is incomplete.
    	IncompleteQueryDetails *InterpretError_InterpretIncompleteQueryDetails `protobuf:"bytes,2,opt,name=incomplete_query_details,json=incompleteQueryDetails,proto3" json:"incomplete_query_details,omitempty"`
    	// Populated if the query was too ambiguous.
    	AmbiguityDetails *InterpretError_InterpretAmbiguityDetails `protobuf:"bytes,3,opt,name=ambiguity_details,json=ambiguityDetails,proto3" json:"ambiguity_details,omitempty"`
    	// contains filtered or unexported fields
    }

Details on interpretation failure.

### func (*InterpretError_InterpretErrorDetails) Descriptor 
    
    
    func (*InterpretError_InterpretErrorDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError_InterpretErrorDetails.ProtoReflect.Descriptor instead.

### func (*InterpretError_InterpretErrorDetails) GetAmbiguityDetails 
    
    
    func (x *InterpretError_InterpretErrorDetails) GetAmbiguityDetails() *InterpretError_InterpretAmbiguityDetails

### func (*InterpretError_InterpretErrorDetails) GetIncompleteQueryDetails 
    
    
    func (x *InterpretError_InterpretErrorDetails) GetIncompleteQueryDetails() *InterpretError_InterpretIncompleteQueryDetails

### func (*InterpretError_InterpretErrorDetails) GetUnsupportedDetails 
    
    
    func (x *InterpretError_InterpretErrorDetails) GetUnsupportedDetails() *InterpretError_InterpretUnsupportedDetails

### func (*InterpretError_InterpretErrorDetails) ProtoMessage 
    
    
    func (*InterpretError_InterpretErrorDetails) ProtoMessage()

### func (*InterpretError_InterpretErrorDetails) ProtoReflect 
    
    
    func (x *InterpretError_InterpretErrorDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretError_InterpretErrorDetails) Reset 
    
    
    func (x *InterpretError_InterpretErrorDetails) Reset()

### func (*InterpretError_InterpretErrorDetails) String 
    
    
    func (x *InterpretError_InterpretErrorDetails) String() [string](https://pkg.go.dev/builtin#string)

## InterpretError_InterpretIncompleteQueryDetails
    
    
    type InterpretError_InterpretIncompleteQueryDetails struct {
    
    	// List of missing interpret entities.
    	Entities []InterpretEntity `protobuf:"varint,1,rep,packed,name=entities,proto3,enum=google.cloud.dataqna.v1alpha.InterpretEntity" json:"entities,omitempty"`
    	// contains filtered or unexported fields
    }

Details about an incomplete query.

### func (*InterpretError_InterpretIncompleteQueryDetails) Descriptor 
    
    
    func (*InterpretError_InterpretIncompleteQueryDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError_InterpretIncompleteQueryDetails.ProtoReflect.Descriptor instead.

### func (*InterpretError_InterpretIncompleteQueryDetails) GetEntities 
    
    
    func (x *InterpretError_InterpretIncompleteQueryDetails) GetEntities() []InterpretEntity

### func (*InterpretError_InterpretIncompleteQueryDetails) ProtoMessage 
    
    
    func (*InterpretError_InterpretIncompleteQueryDetails) ProtoMessage()

### func (*InterpretError_InterpretIncompleteQueryDetails) ProtoReflect 
    
    
    func (x *InterpretError_InterpretIncompleteQueryDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretError_InterpretIncompleteQueryDetails) Reset 
    
    
    func (x *InterpretError_InterpretIncompleteQueryDetails) Reset()

### func (*InterpretError_InterpretIncompleteQueryDetails) String 
    
    
    func (x *InterpretError_InterpretIncompleteQueryDetails) String() [string](https://pkg.go.dev/builtin#string)

## InterpretError_InterpretUnsupportedDetails
    
    
    type InterpretError_InterpretUnsupportedDetails struct {
    
    	// Unsupported operators. For example: median.
    	Operators [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=operators,proto3" json:"operators,omitempty"`
    	// Unsupported intents.
    	Intent [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=intent,proto3" json:"intent,omitempty"`
    	// contains filtered or unexported fields
    }

Details about unsupported parts in a query.

### func (*InterpretError_InterpretUnsupportedDetails) Descriptor 
    
    
    func (*InterpretError_InterpretUnsupportedDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretError_InterpretUnsupportedDetails.ProtoReflect.Descriptor instead.

### func (*InterpretError_InterpretUnsupportedDetails) GetIntent 
    
    
    func (x *InterpretError_InterpretUnsupportedDetails) GetIntent() [][string](https://pkg.go.dev/builtin#string)

### func (*InterpretError_InterpretUnsupportedDetails) GetOperators 
    
    
    func (x *InterpretError_InterpretUnsupportedDetails) GetOperators() [][string](https://pkg.go.dev/builtin#string)

### func (*InterpretError_InterpretUnsupportedDetails) ProtoMessage 
    
    
    func (*InterpretError_InterpretUnsupportedDetails) ProtoMessage()

### func (*InterpretError_InterpretUnsupportedDetails) ProtoReflect 
    
    
    func (x *InterpretError_InterpretUnsupportedDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretError_InterpretUnsupportedDetails) Reset 
    
    
    func (x *InterpretError_InterpretUnsupportedDetails) Reset()

### func (*InterpretError_InterpretUnsupportedDetails) String 
    
    
    func (x *InterpretError_InterpretUnsupportedDetails) String() [string](https://pkg.go.dev/builtin#string)

## Interpretation
    
    
    type Interpretation struct {
    
    	// List of data sources used in the current understanding.
    	DataSources [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=data_sources,json=dataSources,proto3" json:"data_sources,omitempty"`
    	// The level of confidence that one of the interpretations is correct. This is
    	// a value in the range [0, 1] where a value of 0.5 or below is to be
    	// considered a low confidence.
    	Confidence [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=confidence,proto3" json:"confidence,omitempty"`
    	// A list of unused phrases. Clients should display a Did You Mean (DYM)
    	//
    	//	dialog if this is non-empty, even if this is the only interpretation.
    	UnusedPhrases [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unused_phrases,json=unusedPhrases,proto3" json:"unused_phrases,omitempty"`
    	// Human readable representation of the query.
    	HumanReadable *HumanReadable `protobuf:"bytes,4,opt,name=human_readable,json=humanReadable,proto3" json:"human_readable,omitempty"`
    	// Information about the interpretation structure that helps to understand and
    	// visualize the response.
    	InterpretationStructure *InterpretationStructure `protobuf:"bytes,5,opt,name=interpretation_structure,json=interpretationStructure,proto3" json:"interpretation_structure,omitempty"`
    	// Representation of the data query to be sent to the backend.
    	DataQuery *DataQuery `protobuf:"bytes,6,opt,name=data_query,json=dataQuery,proto3" json:"data_query,omitempty"`
    	// Information about the backend response. This is populated only if execution
    	// of an interpretation was requested.
    	ExecutionInfo *ExecutionInfo `protobuf:"bytes,7,opt,name=execution_info,json=executionInfo,proto3" json:"execution_info,omitempty"`
    	// contains filtered or unexported fields
    }

An interpretation of a natural language query.

### func (*Interpretation) Descriptor 
    
    
    func (*Interpretation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Interpretation.ProtoReflect.Descriptor instead.

### func (*Interpretation) GetConfidence 
    
    
    func (x *Interpretation) GetConfidence() [float64](https://pkg.go.dev/builtin#float64)

### func (*Interpretation) GetDataQuery 
    
    
    func (x *Interpretation) GetDataQuery() *DataQuery

### func (*Interpretation) GetDataSources 
    
    
    func (x *Interpretation) GetDataSources() [][string](https://pkg.go.dev/builtin#string)

### func (*Interpretation) GetExecutionInfo 
    
    
    func (x *Interpretation) GetExecutionInfo() *ExecutionInfo

### func (*Interpretation) GetHumanReadable 
    
    
    func (x *Interpretation) GetHumanReadable() *HumanReadable

### func (*Interpretation) GetInterpretationStructure 
    
    
    func (x *Interpretation) GetInterpretationStructure() *InterpretationStructure

### func (*Interpretation) GetUnusedPhrases 
    
    
    func (x *Interpretation) GetUnusedPhrases() [][string](https://pkg.go.dev/builtin#string)

### func (*Interpretation) ProtoMessage 
    
    
    func (*Interpretation) ProtoMessage()

### func (*Interpretation) ProtoReflect 
    
    
    func (x *Interpretation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Interpretation) Reset 
    
    
    func (x *Interpretation) Reset()

### func (*Interpretation) String 
    
    
    func (x *Interpretation) String() [string](https://pkg.go.dev/builtin#string)

## InterpretationStructure
    
    
    type InterpretationStructure struct {
    
    	// List of possible visualization types to apply for this interpretation. The
    	// order has no relevance.
    	VisualizationTypes []InterpretationStructure_VisualizationType `protobuf:"varint,1,rep,packed,name=visualization_types,json=visualizationTypes,proto3,enum=google.cloud.dataqna.v1alpha.InterpretationStructure_VisualizationType" json:"visualization_types,omitempty"`
    	// Information about the output columns, that is, the columns that will be
    	// returned by the backend.
    	ColumnInfo []*InterpretationStructure_ColumnInfo `protobuf:"bytes,2,rep,name=column_info,json=columnInfo,proto3" json:"column_info,omitempty"`
    	// contains filtered or unexported fields
    }

Information about the interpretation structure that helps to understand and visualize the response.

### func (*InterpretationStructure) Descriptor 
    
    
    func (*InterpretationStructure) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretationStructure.ProtoReflect.Descriptor instead.

### func (*InterpretationStructure) GetColumnInfo 
    
    
    func (x *InterpretationStructure) GetColumnInfo() []*InterpretationStructure_ColumnInfo

### func (*InterpretationStructure) GetVisualizationTypes 
    
    
    func (x *InterpretationStructure) GetVisualizationTypes() []InterpretationStructure_VisualizationType

### func (*InterpretationStructure) ProtoMessage 
    
    
    func (*InterpretationStructure) ProtoMessage()

### func (*InterpretationStructure) ProtoReflect 
    
    
    func (x *InterpretationStructure) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretationStructure) Reset 
    
    
    func (x *InterpretationStructure) Reset()

### func (*InterpretationStructure) String 
    
    
    func (x *InterpretationStructure) String() [string](https://pkg.go.dev/builtin#string)

## InterpretationStructure_ColumnInfo
    
    
    type InterpretationStructure_ColumnInfo struct {
    
    	// The alias of the output column as used by the backend. For example, the
    	// field name in the schema provided in the query response in BigQuery.
    	OutputAlias [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=output_alias,json=outputAlias,proto3" json:"output_alias,omitempty"`
    	// Human readable name of the output column.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// contains filtered or unexported fields
    }

Information about a column.

### func (*InterpretationStructure_ColumnInfo) Descriptor 
    
    
    func (*InterpretationStructure_ColumnInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretationStructure_ColumnInfo.ProtoReflect.Descriptor instead.

### func (*InterpretationStructure_ColumnInfo) GetDisplayName 
    
    
    func (x *InterpretationStructure_ColumnInfo) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*InterpretationStructure_ColumnInfo) GetOutputAlias 
    
    
    func (x *InterpretationStructure_ColumnInfo) GetOutputAlias() [string](https://pkg.go.dev/builtin#string)

### func (*InterpretationStructure_ColumnInfo) ProtoMessage 
    
    
    func (*InterpretationStructure_ColumnInfo) ProtoMessage()

### func (*InterpretationStructure_ColumnInfo) ProtoReflect 
    
    
    func (x *InterpretationStructure_ColumnInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InterpretationStructure_ColumnInfo) Reset 
    
    
    func (x *InterpretationStructure_ColumnInfo) Reset()

### func (*InterpretationStructure_ColumnInfo) String 
    
    
    func (x *InterpretationStructure_ColumnInfo) String() [string](https://pkg.go.dev/builtin#string)

## InterpretationStructure_VisualizationType
    
    
    type InterpretationStructure_VisualizationType [int32](https://pkg.go.dev/builtin#int32)

Enumeration of visualzation types to use for query response data.

### InterpretationStructure_VISUALIZATION_TYPE_UNSPECIFIED, InterpretationStructure_TABLE, InterpretationStructure_BAR_CHART, InterpretationStructure_COLUMN_CHART, InterpretationStructure_TIMELINE, InterpretationStructure_SCATTER_PLOT, InterpretationStructure_PIE_CHART, InterpretationStructure_LINE_CHART, InterpretationStructure_AREA_CHART, InterpretationStructure_COMBO_CHART, InterpretationStructure_HISTOGRAM, InterpretationStructure_GENERIC_CHART, InterpretationStructure_CHART_NOT_UNDERSTOOD
    
    
    const (
    	// No visualization type was specified.
    	InterpretationStructure_VISUALIZATION_TYPE_UNSPECIFIED InterpretationStructure_VisualizationType = 0
    	// Show a table.
    	InterpretationStructure_TABLE InterpretationStructure_VisualizationType = 1
    	// Show a [bar
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/barchart).
    	InterpretationStructure_BAR_CHART InterpretationStructure_VisualizationType = 2
    	// Show a [column
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/columnchart).
    	InterpretationStructure_COLUMN_CHART InterpretationStructure_VisualizationType = 3
    	// Show a
    	// [timeline](https://developers.google.com/chart/interactive/docs/gallery/timeline).
    	InterpretationStructure_TIMELINE InterpretationStructure_VisualizationType = 4
    	// Show a [scatter
    	// plot](https://developers.google.com/chart/interactive/docs/gallery/scatterchart).
    	InterpretationStructure_SCATTER_PLOT InterpretationStructure_VisualizationType = 5
    	// Show a [pie
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/piechart).
    	InterpretationStructure_PIE_CHART InterpretationStructure_VisualizationType = 6
    	// Show a [line
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/linechart).
    	InterpretationStructure_LINE_CHART InterpretationStructure_VisualizationType = 7
    	// Show an [area
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/areachart).
    	InterpretationStructure_AREA_CHART InterpretationStructure_VisualizationType = 8
    	// Show a [combo
    	// chart](https://developers.google.com/chart/interactive/docs/gallery/combochart).
    	InterpretationStructure_COMBO_CHART InterpretationStructure_VisualizationType = 9
    	// Show a
    	// [histogram](https://developers.google.com/chart/interactive/docs/gallery/histogram).
    	InterpretationStructure_HISTOGRAM InterpretationStructure_VisualizationType = 10
    	// This denotes queries when the user has not specified the particular type
    	// of chart and has mentioned only a generic chart name such as "Chart",
    	// "Plot", "Graph", etc. This will differentiate it from specific charting
    	// terms such as "Bar chart", "Pie chart", etc.
    	InterpretationStructure_GENERIC_CHART InterpretationStructure_VisualizationType = 11
    	// The user tried to specify a chart type, but the interpreter could not
    	// understand the type. The client should display a generic chart and may
    	// give a hint to the user that the requested type was not understood.
    	InterpretationStructure_CHART_NOT_UNDERSTOOD InterpretationStructure_VisualizationType = 12
    )

### func (InterpretationStructure_VisualizationType) Descriptor 
    
    
    func (InterpretationStructure_VisualizationType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InterpretationStructure_VisualizationType) Enum 
    
    
    func (x InterpretationStructure_VisualizationType) Enum() *InterpretationStructure_VisualizationType

### func (InterpretationStructure_VisualizationType) EnumDescriptor 
    
    
    func (InterpretationStructure_VisualizationType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InterpretationStructure_VisualizationType.Descriptor instead.

### func (InterpretationStructure_VisualizationType) Number 
    
    
    func (x InterpretationStructure_VisualizationType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InterpretationStructure_VisualizationType) String 
    
    
    func (x InterpretationStructure_VisualizationType) String() [string](https://pkg.go.dev/builtin#string)

### func (InterpretationStructure_VisualizationType) Type 
    
    
    func (InterpretationStructure_VisualizationType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Question
    
    
    type Question struct {
    
    	// Output only. Immutable. The unique identifier for the Question. The ID is server-generated.
    	// Example: `projects/foo/locations/bar/questions/123`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. Immutable. Scopes to be used for the question. A scope defines the relevant data set
    	// scope. It can be a reference to a specific data source or a collection of
    	// data sources. Currently, support is limited to a single BigQuery table.
    	// There must be exactly one `scopes` element.
    	//
    	// Example:
    	// `//bigquery.googleapis.com/projects/test-project/datasets/foo/tables/bar`
    	Scopes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=scopes,proto3" json:"scopes,omitempty"`
    	// Required. Immutable. The query in natural language.
    	Query [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=query,proto3" json:"query,omitempty"`
    	// A list of annotations to use instead of the default annotation of a data
    	// source (set in the data source reference resource). There must not be
    	// more than one annotation with the same data source reference.
    	DataSourceAnnotations [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=data_source_annotations,json=dataSourceAnnotations,proto3" json:"data_source_annotations,omitempty"`
    	// An error field explaining why interpretation failed. This is only populated
    	// if the interpretation failed.
    	//
    	// Note: This is different from getting a status error on the request itself.
    	// This is not a client or server error and the Question resource is still
    	// persisted, but the service could not interpret the question. Clients should
    	// present the error to the user so the user can rephrase the question.
    	InterpretError *InterpretError `protobuf:"bytes,5,opt,name=interpret_error,json=interpretError,proto3" json:"interpret_error,omitempty"`
    	// A list of interpretations for this question.
    	Interpretations []*Interpretation `protobuf:"bytes,6,rep,name=interpretations,proto3" json:"interpretations,omitempty"`
    	// Time when the question was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,7,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The e-mail address of the user that created this question.
    	UserEmail [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=user_email,json=userEmail,proto3" json:"user_email,omitempty"`
    	// Input only. Immutable. Flags to request additional information for debugging purposes.
    	DebugFlags *DebugFlags `protobuf:"bytes,9,opt,name=debug_flags,json=debugFlags,proto3" json:"debug_flags,omitempty"`
    	// Top level debug information.
    	// This will be stored as the type DebugInformation.
    	// Using Any so clients don't need to pull in anything
    	// inside the debug message.
    	DebugInfo *anypb.Any `protobuf:"bytes,10,opt,name=debug_info,json=debugInfo,proto3" json:"debug_info,omitempty"`
    	// contains filtered or unexported fields
    }

The question resource represents a natural language query, its settings, understanding generated by the system, and answer retrieval status. A question cannot be modified.

### func (*Question) Descriptor 
    
    
    func (*Question) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Question.ProtoReflect.Descriptor instead.

### func (*Question) GetCreateTime 
    
    
    func (x *Question) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Question) GetDataSourceAnnotations 
    
    
    func (x *Question) GetDataSourceAnnotations() [][string](https://pkg.go.dev/builtin#string)

### func (*Question) GetDebugFlags 
    
    
    func (x *Question) GetDebugFlags() *DebugFlags

### func (*Question) GetDebugInfo 
    
    
    func (x *Question) GetDebugInfo() *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any)

### func (*Question) GetInterpretError 
    
    
    func (x *Question) GetInterpretError() *InterpretError

### func (*Question) GetInterpretations 
    
    
    func (x *Question) GetInterpretations() []*Interpretation

### func (*Question) GetName 
    
    
    func (x *Question) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Question) GetQuery 
    
    
    func (x *Question) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*Question) GetScopes 
    
    
    func (x *Question) GetScopes() [][string](https://pkg.go.dev/builtin#string)

### func (*Question) GetUserEmail 
    
    
    func (x *Question) GetUserEmail() [string](https://pkg.go.dev/builtin#string)

### func (*Question) ProtoMessage 
    
    
    func (*Question) ProtoMessage()

### func (*Question) ProtoReflect 
    
    
    func (x *Question) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Question) Reset 
    
    
    func (x *Question) Reset()

### func (*Question) String 
    
    
    func (x *Question) String() [string](https://pkg.go.dev/builtin#string)

## QuestionServiceClient
    
    
    type QuestionServiceClient interface {
    	// Gets a previously created question.
    	GetQuestion(ctx context.Context, in *GetQuestionRequest, opts ...grpc.CallOption) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Creates a question.
    	CreateQuestion(ctx context.Context, in *CreateQuestionRequest, opts ...grpc.CallOption) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Executes an interpretation.
    	ExecuteQuestion(ctx context.Context, in *ExecuteQuestionRequest, opts ...grpc.CallOption) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Gets previously created user feedback.
    	GetUserFeedback(ctx context.Context, in *GetUserFeedbackRequest, opts ...grpc.CallOption) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))
    	// Updates user feedback. This creates user feedback if there was none before
    	// (upsert).
    	UpdateUserFeedback(ctx context.Context, in *UpdateUserFeedbackRequest, opts ...grpc.CallOption) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))
    }

QuestionServiceClient is the client API for QuestionService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewQuestionServiceClient 
    
    
    func NewQuestionServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) QuestionServiceClient

## QuestionServiceServer
    
    
    type QuestionServiceServer interface {
    	// Gets a previously created question.
    	GetQuestion(context.Context, *GetQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Creates a question.
    	CreateQuestion(context.Context, *CreateQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Executes an interpretation.
    	ExecuteQuestion(context.Context, *ExecuteQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))
    	// Gets previously created user feedback.
    	GetUserFeedback(context.Context, *GetUserFeedbackRequest) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))
    	// Updates user feedback. This creates user feedback if there was none before
    	// (upsert).
    	UpdateUserFeedback(context.Context, *UpdateUserFeedbackRequest) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))
    }

QuestionServiceServer is the server API for QuestionService service. All implementations should embed UnimplementedQuestionServiceServer for forward compatibility

## SuggestQueriesRequest
    
    
    type SuggestQueriesRequest struct {
    
    	// Required. The parent of the suggestion query is the resource denoting the project and
    	// location.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The scopes to which this search is restricted. The only supported scope
    	// pattern is
    	// `//bigquery.googleapis.com/projects/{GCP-PROJECT-ID}/datasets/{DATASET-ID}/tables/{TABLE-ID}`.
    	Scopes [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=scopes,proto3" json:"scopes,omitempty"`
    	// User query for which to generate suggestions. If the query is empty, zero
    	// state suggestions are returned. This allows UIs to display suggestions
    	// right away, helping the user to get a sense of what a query might look
    	// like.
    	Query [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=query,proto3" json:"query,omitempty"`
    	// The requested suggestion type. Multiple suggestion types can be
    	// requested, but there is no guarantee that the service will return
    	// suggestions for each type. Suggestions for a requested type might rank
    	// lower than suggestions for other types and the service may decide to cut
    	// these suggestions off.
    	SuggestionTypes []SuggestionType `protobuf:"varint,4,rep,packed,name=suggestion_types,json=suggestionTypes,proto3,enum=google.cloud.dataqna.v1alpha.SuggestionType" json:"suggestion_types,omitempty"`
    	// contains filtered or unexported fields
    }

Request for query suggestions.

### func (*SuggestQueriesRequest) Descriptor 
    
    
    func (*SuggestQueriesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuggestQueriesRequest.ProtoReflect.Descriptor instead.

### func (*SuggestQueriesRequest) GetParent 
    
    
    func (x *SuggestQueriesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*SuggestQueriesRequest) GetQuery 
    
    
    func (x *SuggestQueriesRequest) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SuggestQueriesRequest) GetScopes 
    
    
    func (x *SuggestQueriesRequest) GetScopes() [][string](https://pkg.go.dev/builtin#string)

### func (*SuggestQueriesRequest) GetSuggestionTypes 
    
    
    func (x *SuggestQueriesRequest) GetSuggestionTypes() []SuggestionType

### func (*SuggestQueriesRequest) ProtoMessage 
    
    
    func (*SuggestQueriesRequest) ProtoMessage()

### func (*SuggestQueriesRequest) ProtoReflect 
    
    
    func (x *SuggestQueriesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SuggestQueriesRequest) Reset 
    
    
    func (x *SuggestQueriesRequest) Reset()

### func (*SuggestQueriesRequest) String 
    
    
    func (x *SuggestQueriesRequest) String() [string](https://pkg.go.dev/builtin#string)

## SuggestQueriesResponse
    
    
    type SuggestQueriesResponse struct {
    
    	// A list of suggestions.
    	Suggestions []*Suggestion `protobuf:"bytes,1,rep,name=suggestions,proto3" json:"suggestions,omitempty"`
    	// contains filtered or unexported fields
    }

Response to SuggestQueries.

### func (*SuggestQueriesResponse) Descriptor 
    
    
    func (*SuggestQueriesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuggestQueriesResponse.ProtoReflect.Descriptor instead.

### func (*SuggestQueriesResponse) GetSuggestions 
    
    
    func (x *SuggestQueriesResponse) GetSuggestions() []*Suggestion

### func (*SuggestQueriesResponse) ProtoMessage 
    
    
    func (*SuggestQueriesResponse) ProtoMessage()

### func (*SuggestQueriesResponse) ProtoReflect 
    
    
    func (x *SuggestQueriesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SuggestQueriesResponse) Reset 
    
    
    func (x *SuggestQueriesResponse) Reset()

### func (*SuggestQueriesResponse) String 
    
    
    func (x *SuggestQueriesResponse) String() [string](https://pkg.go.dev/builtin#string)

## Suggestion
    
    
    type Suggestion struct {
    
    	// Detailed information about the suggestion.
    	SuggestionInfo *SuggestionInfo `protobuf:"bytes,1,opt,name=suggestion_info,json=suggestionInfo,proto3" json:"suggestion_info,omitempty"`
    	// The score of the suggestion. This can be used to define ordering in UI.
    	// The score represents confidence in the suggestion where higher is better.
    	// All score values must be in the range [0, 1).
    	RankingScore [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=ranking_score,json=rankingScore,proto3" json:"ranking_score,omitempty"`
    	// The type of the suggestion.
    	SuggestionType SuggestionType `protobuf:"varint,3,opt,name=suggestion_type,json=suggestionType,proto3,enum=google.cloud.dataqna.v1alpha.SuggestionType" json:"suggestion_type,omitempty"`
    	// contains filtered or unexported fields
    }

A suggestion for a query with a ranking score.

### func (*Suggestion) Descriptor 
    
    
    func (*Suggestion) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Suggestion.ProtoReflect.Descriptor instead.

### func (*Suggestion) GetRankingScore 
    
    
    func (x *Suggestion) GetRankingScore() [float64](https://pkg.go.dev/builtin#float64)

### func (*Suggestion) GetSuggestionInfo 
    
    
    func (x *Suggestion) GetSuggestionInfo() *SuggestionInfo

### func (*Suggestion) GetSuggestionType 
    
    
    func (x *Suggestion) GetSuggestionType() SuggestionType

### func (*Suggestion) ProtoMessage 
    
    
    func (*Suggestion) ProtoMessage()

### func (*Suggestion) ProtoReflect 
    
    
    func (x *Suggestion) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Suggestion) Reset 
    
    
    func (x *Suggestion) Reset()

### func (*Suggestion) String 
    
    
    func (x *Suggestion) String() [string](https://pkg.go.dev/builtin#string)

## SuggestionInfo
    
    
    type SuggestionInfo struct {
    
    	// Annotations for the suggestion. This provides information about which part
    	// of the suggestion corresponds to what semantic meaning (e.g. a metric).
    	AnnotatedSuggestion *AnnotatedString `protobuf:"bytes,1,opt,name=annotated_suggestion,json=annotatedSuggestion,proto3" json:"annotated_suggestion,omitempty"`
    	// Matches between user query and the annotated string.
    	QueryMatches []*SuggestionInfo_MatchInfo `protobuf:"bytes,2,rep,name=query_matches,json=queryMatches,proto3" json:"query_matches,omitempty"`
    	// contains filtered or unexported fields
    }

Detailed information about the suggestion.

### func (*SuggestionInfo) Descriptor 
    
    
    func (*SuggestionInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuggestionInfo.ProtoReflect.Descriptor instead.

### func (*SuggestionInfo) GetAnnotatedSuggestion 
    
    
    func (x *SuggestionInfo) GetAnnotatedSuggestion() *AnnotatedString

### func (*SuggestionInfo) GetQueryMatches 
    
    
    func (x *SuggestionInfo) GetQueryMatches() []*SuggestionInfo_MatchInfo

### func (*SuggestionInfo) ProtoMessage 
    
    
    func (*SuggestionInfo) ProtoMessage()

### func (*SuggestionInfo) ProtoReflect 
    
    
    func (x *SuggestionInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SuggestionInfo) Reset 
    
    
    func (x *SuggestionInfo) Reset()

### func (*SuggestionInfo) String 
    
    
    func (x *SuggestionInfo) String() [string](https://pkg.go.dev/builtin#string)

## SuggestionInfo_MatchInfo
    
    
    type SuggestionInfo_MatchInfo struct {
    
    	// Unicode character index of the string annotation.
    	StartCharIndex [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=start_char_index,json=startCharIndex,proto3" json:"start_char_index,omitempty"`
    	// Count of unicode characters of this substring.
    	Length [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=length,proto3" json:"length,omitempty"`
    	// contains filtered or unexported fields
    }

MatchInfo describes which part of suggestion matched with data in user typed query. This can be used to highlight matching parts in the UI. This is different from the annotations provided in annotated_suggestion. The annotated_suggestion provides information about the semantic meaning, while this provides information about how it relates to the input.

Example: user query: `top products`
    
    
        annotated_suggestion {
         text_formatted = "top product_group"
         html_formatted = "top <b>product_group</b>"
         markups {
          {type: TEXT, start_char_index: 0, length: 3}
          {type: DIMENSION, start_char_index: 4, length: 13}
         }
        }
    
        query_matches {
         { start_char_index: 0, length: 3 }
         { start_char_index: 4, length: 7}
        }
    

### func (*SuggestionInfo_MatchInfo) Descriptor 
    
    
    func (*SuggestionInfo_MatchInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuggestionInfo_MatchInfo.ProtoReflect.Descriptor instead.

### func (*SuggestionInfo_MatchInfo) GetLength 
    
    
    func (x *SuggestionInfo_MatchInfo) GetLength() [int32](https://pkg.go.dev/builtin#int32)

### func (*SuggestionInfo_MatchInfo) GetStartCharIndex 
    
    
    func (x *SuggestionInfo_MatchInfo) GetStartCharIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*SuggestionInfo_MatchInfo) ProtoMessage 
    
    
    func (*SuggestionInfo_MatchInfo) ProtoMessage()

### func (*SuggestionInfo_MatchInfo) ProtoReflect 
    
    
    func (x *SuggestionInfo_MatchInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SuggestionInfo_MatchInfo) Reset 
    
    
    func (x *SuggestionInfo_MatchInfo) Reset()

### func (*SuggestionInfo_MatchInfo) String 
    
    
    func (x *SuggestionInfo_MatchInfo) String() [string](https://pkg.go.dev/builtin#string)

## SuggestionType
    
    
    type SuggestionType [int32](https://pkg.go.dev/builtin#int32)

The type of suggestion.

### SuggestionType_SUGGESTION_TYPE_UNSPECIFIED, SuggestionType_ENTITY, SuggestionType_TEMPLATE
    
    
    const (
    	// No suggestiont type is specified.
    	SuggestionType_SUGGESTION_TYPE_UNSPECIFIED SuggestionType = 0
    	// Entity suggestion type. Suggestions are for single entities.
    	SuggestionType_ENTITY SuggestionType = 1
    	// Template suggestion type. Suggestions are for full sentences.
    	SuggestionType_TEMPLATE SuggestionType = 2
    )

### func (SuggestionType) Descriptor 
    
    
    func (SuggestionType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SuggestionType) Enum 
    
    
    func (x SuggestionType) Enum() *SuggestionType

### func (SuggestionType) EnumDescriptor 
    
    
    func (SuggestionType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SuggestionType.Descriptor instead.

### func (SuggestionType) Number 
    
    
    func (x SuggestionType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SuggestionType) String 
    
    
    func (x SuggestionType) String() [string](https://pkg.go.dev/builtin#string)

### func (SuggestionType) Type 
    
    
    func (SuggestionType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedAutoSuggestionServiceServer
    
    
    type UnimplementedAutoSuggestionServiceServer struct {
    }

UnimplementedAutoSuggestionServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedAutoSuggestionServiceServer) SuggestQueries 
    
    
    func (UnimplementedAutoSuggestionServiceServer) SuggestQueries([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SuggestQueriesRequest) (*SuggestQueriesResponse, [error](https://pkg.go.dev/builtin#error))

## UnimplementedQuestionServiceServer
    
    
    type UnimplementedQuestionServiceServer struct {
    }

UnimplementedQuestionServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedQuestionServiceServer) CreateQuestion 
    
    
    func (UnimplementedQuestionServiceServer) CreateQuestion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedQuestionServiceServer) ExecuteQuestion 
    
    
    func (UnimplementedQuestionServiceServer) ExecuteQuestion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ExecuteQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedQuestionServiceServer) GetQuestion 
    
    
    func (UnimplementedQuestionServiceServer) GetQuestion([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetQuestionRequest) (*Question, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedQuestionServiceServer) GetUserFeedback 
    
    
    func (UnimplementedQuestionServiceServer) GetUserFeedback([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetUserFeedbackRequest) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedQuestionServiceServer) UpdateUserFeedback 
    
    
    func (UnimplementedQuestionServiceServer) UpdateUserFeedback([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateUserFeedbackRequest) (*UserFeedback, [error](https://pkg.go.dev/builtin#error))

## UnsafeAutoSuggestionServiceServer
    
    
    type UnsafeAutoSuggestionServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeAutoSuggestionServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to AutoSuggestionServiceServer will result in compilation errors.

## UnsafeQuestionServiceServer
    
    
    type UnsafeQuestionServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeQuestionServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to QuestionServiceServer will result in compilation errors.

## UpdateUserFeedbackRequest
    
    
    type UpdateUserFeedbackRequest struct {
    
    	// Required. The user feedback to update. This can be called even if there is no
    	// user feedback so far.
    	// The feedback's name field is used to identify the user feedback (and the
    	// corresponding question) to update.
    	UserFeedback *UserFeedback `protobuf:"bytes,1,opt,name=user_feedback,json=userFeedback,proto3" json:"user_feedback,omitempty"`
    	// The list of fields to be updated.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request to updates user feedback.

### func (*UpdateUserFeedbackRequest) Descriptor 
    
    
    func (*UpdateUserFeedbackRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateUserFeedbackRequest.ProtoReflect.Descriptor instead.

### func (*UpdateUserFeedbackRequest) GetUpdateMask 
    
    
    func (x *UpdateUserFeedbackRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateUserFeedbackRequest) GetUserFeedback 
    
    
    func (x *UpdateUserFeedbackRequest) GetUserFeedback() *UserFeedback

### func (*UpdateUserFeedbackRequest) ProtoMessage 
    
    
    func (*UpdateUserFeedbackRequest) ProtoMessage()

### func (*UpdateUserFeedbackRequest) ProtoReflect 
    
    
    func (x *UpdateUserFeedbackRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateUserFeedbackRequest) Reset 
    
    
    func (x *UpdateUserFeedbackRequest) Reset()

### func (*UpdateUserFeedbackRequest) String 
    
    
    func (x *UpdateUserFeedbackRequest) String() [string](https://pkg.go.dev/builtin#string)

## UserFeedback
    
    
    type UserFeedback struct {
    
    	// Required. The unique identifier for the user feedback.
    	// User feedback is a singleton resource on a Question.
    	// Example: `projects/foo/locations/bar/questions/1234/userFeedback`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Free form user feedback, such as a text box.
    	FreeFormFeedback [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=free_form_feedback,json=freeFormFeedback,proto3" json:"free_form_feedback,omitempty"`
    	// The user feedback rating
    	Rating UserFeedback_UserFeedbackRating `protobuf:"varint,3,opt,name=rating,proto3,enum=google.cloud.dataqna.v1alpha.UserFeedback_UserFeedbackRating" json:"rating,omitempty"`
    	// contains filtered or unexported fields
    }

Feedback provided by a user.

### func (*UserFeedback) Descriptor 
    
    
    func (*UserFeedback) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UserFeedback.ProtoReflect.Descriptor instead.

### func (*UserFeedback) GetFreeFormFeedback 
    
    
    func (x *UserFeedback) GetFreeFormFeedback() [string](https://pkg.go.dev/builtin#string)

### func (*UserFeedback) GetName 
    
    
    func (x *UserFeedback) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*UserFeedback) GetRating 
    
    
    func (x *UserFeedback) GetRating() UserFeedback_UserFeedbackRating

### func (*UserFeedback) ProtoMessage 
    
    
    func (*UserFeedback) ProtoMessage()

### func (*UserFeedback) ProtoReflect 
    
    
    func (x *UserFeedback) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UserFeedback) Reset 
    
    
    func (x *UserFeedback) Reset()

### func (*UserFeedback) String 
    
    
    func (x *UserFeedback) String() [string](https://pkg.go.dev/builtin#string)

## UserFeedback_UserFeedbackRating
    
    
    type UserFeedback_UserFeedbackRating [int32](https://pkg.go.dev/builtin#int32)

Enumeration of feedback ratings.

### UserFeedback_USER_FEEDBACK_RATING_UNSPECIFIED, UserFeedback_POSITIVE, UserFeedback_NEGATIVE
    
    
    const (
    	// No rating was specified.
    	UserFeedback_USER_FEEDBACK_RATING_UNSPECIFIED UserFeedback_UserFeedbackRating = 0
    	// The user provided positive feedback.
    	UserFeedback_POSITIVE UserFeedback_UserFeedbackRating = 1
    	// The user provided negative feedback.
    	UserFeedback_NEGATIVE UserFeedback_UserFeedbackRating = 2
    )

### func (UserFeedback_UserFeedbackRating) Descriptor 
    
    
    func (UserFeedback_UserFeedbackRating) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (UserFeedback_UserFeedbackRating) Enum 
    
    
    func (x UserFeedback_UserFeedbackRating) Enum() *UserFeedback_UserFeedbackRating

### func (UserFeedback_UserFeedbackRating) EnumDescriptor 
    
    
    func (UserFeedback_UserFeedbackRating) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UserFeedback_UserFeedbackRating.Descriptor instead.

### func (UserFeedback_UserFeedbackRating) Number 
    
    
    func (x UserFeedback_UserFeedbackRating) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (UserFeedback_UserFeedbackRating) String 
    
    
    func (x UserFeedback_UserFeedbackRating) String() [string](https://pkg.go.dev/builtin#string)

### func (UserFeedback_UserFeedbackRating) Type 
    
    
    func (UserFeedback_UserFeedbackRating) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
