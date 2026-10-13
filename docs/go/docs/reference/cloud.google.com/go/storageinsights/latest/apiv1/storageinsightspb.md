---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storageinsights/latest/apiv1/storageinsightspb/
title: Storage Insights API v1 - Package cloud.google.com/go/storageinsights/apiv1/storageinsightspb (v1.9.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:47.319465+00:00
---

# Storage Insights API v1 - Package cloud.google.com/go/storageinsights/apiv1/storageinsightspb (v1.9.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storageinsights/latest/apiv1/storageinsightspb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Storage Insights API v1 - Package cloud.google.com/go/storageinsights/apiv1/storageinsightspb (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.6  1.0.12  0.2.2  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/storageinsights/apiv1/storageinsightspb). 

##  Constants 

### StorageInsights_ListReportConfigs_FullMethodName, StorageInsights_GetReportConfig_FullMethodName, StorageInsights_CreateReportConfig_FullMethodName, StorageInsights_UpdateReportConfig_FullMethodName, StorageInsights_DeleteReportConfig_FullMethodName, StorageInsights_ListReportDetails_FullMethodName, StorageInsights_GetReportDetail_FullMethodName, StorageInsights_ListDatasetConfigs_FullMethodName, StorageInsights_GetDatasetConfig_FullMethodName, StorageInsights_CreateDatasetConfig_FullMethodName, StorageInsights_UpdateDatasetConfig_FullMethodName, StorageInsights_DeleteDatasetConfig_FullMethodName, StorageInsights_LinkDataset_FullMethodName, StorageInsights_UnlinkDataset_FullMethodName
    
    
    const (
    	StorageInsights_ListReportConfigs_FullMethodName   = "/google.cloud.storageinsights.v1.StorageInsights/ListReportConfigs"
    	StorageInsights_GetReportConfig_FullMethodName     = "/google.cloud.storageinsights.v1.StorageInsights/GetReportConfig"
    	StorageInsights_CreateReportConfig_FullMethodName  = "/google.cloud.storageinsights.v1.StorageInsights/CreateReportConfig"
    	StorageInsights_UpdateReportConfig_FullMethodName  = "/google.cloud.storageinsights.v1.StorageInsights/UpdateReportConfig"
    	StorageInsights_DeleteReportConfig_FullMethodName  = "/google.cloud.storageinsights.v1.StorageInsights/DeleteReportConfig"
    	StorageInsights_ListReportDetails_FullMethodName   = "/google.cloud.storageinsights.v1.StorageInsights/ListReportDetails"
    	StorageInsights_GetReportDetail_FullMethodName     = "/google.cloud.storageinsights.v1.StorageInsights/GetReportDetail"
    	StorageInsights_ListDatasetConfigs_FullMethodName  = "/google.cloud.storageinsights.v1.StorageInsights/ListDatasetConfigs"
    	StorageInsights_GetDatasetConfig_FullMethodName    = "/google.cloud.storageinsights.v1.StorageInsights/GetDatasetConfig"
    	StorageInsights_CreateDatasetConfig_FullMethodName = "/google.cloud.storageinsights.v1.StorageInsights/CreateDatasetConfig"
    	StorageInsights_UpdateDatasetConfig_FullMethodName = "/google.cloud.storageinsights.v1.StorageInsights/UpdateDatasetConfig"
    	StorageInsights_DeleteDatasetConfig_FullMethodName = "/google.cloud.storageinsights.v1.StorageInsights/DeleteDatasetConfig"
    	StorageInsights_LinkDataset_FullMethodName         = "/google.cloud.storageinsights.v1.StorageInsights/LinkDataset"
    	StorageInsights_UnlinkDataset_FullMethodName       = "/google.cloud.storageinsights.v1.StorageInsights/UnlinkDataset"
    )

## Variables 

### FrequencyOptions_Frequency_name, FrequencyOptions_Frequency_value
    
    
    var (
    	FrequencyOptions_Frequency_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "FREQUENCY_UNSPECIFIED",
    		1: "DAILY",
    		2: "WEEKLY",
    	}
    	FrequencyOptions_Frequency_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FREQUENCY_UNSPECIFIED": 0,
    		"DAILY":                 1,
    		"WEEKLY":                2,
    	}
    )

Enum value maps for FrequencyOptions_Frequency.

### Identity_IdentityType_name, Identity_IdentityType_value
    
    
    var (
    	Identity_IdentityType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IDENTITY_TYPE_UNSPECIFIED",
    		1: "IDENTITY_TYPE_PER_CONFIG",
    		2: "IDENTITY_TYPE_PER_PROJECT",
    	}
    	Identity_IdentityType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IDENTITY_TYPE_UNSPECIFIED": 0,
    		"IDENTITY_TYPE_PER_CONFIG":  1,
    		"IDENTITY_TYPE_PER_PROJECT": 2,
    	}
    )

Enum value maps for Identity_IdentityType.

### DatasetConfig_ConfigState_name, DatasetConfig_ConfigState_value
    
    
    var (
    	DatasetConfig_ConfigState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CONFIG_STATE_UNSPECIFIED",
    		1: "CONFIG_STATE_ACTIVE",
    		2: "CONFIG_STATE_VERIFICATION_IN_PROGRESS",
    		3: "CONFIG_STATE_CREATED",
    		4: "CONFIG_STATE_PROCESSING",
    	}
    	DatasetConfig_ConfigState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CONFIG_STATE_UNSPECIFIED":              0,
    		"CONFIG_STATE_ACTIVE":                   1,
    		"CONFIG_STATE_VERIFICATION_IN_PROGRESS": 2,
    		"CONFIG_STATE_CREATED":                  3,
    		"CONFIG_STATE_PROCESSING":               4,
    	}
    )

Enum value maps for DatasetConfig_ConfigState.

### File_google_cloud_storageinsights_v1_storageinsights_proto
    
    
    var File_google_cloud_storageinsights_v1_storageinsights_proto protoreflect.FileDescriptor

### StorageInsights_ServiceDesc
    
    
    var StorageInsights_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.storageinsights.v1.StorageInsights",
    	HandlerType: (*StorageInsightsServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListReportConfigs",
    			Handler:    _StorageInsights_ListReportConfigs_Handler,
    		},
    		{
    			MethodName: "GetReportConfig",
    			Handler:    _StorageInsights_GetReportConfig_Handler,
    		},
    		{
    			MethodName: "CreateReportConfig",
    			Handler:    _StorageInsights_CreateReportConfig_Handler,
    		},
    		{
    			MethodName: "UpdateReportConfig",
    			Handler:    _StorageInsights_UpdateReportConfig_Handler,
    		},
    		{
    			MethodName: "DeleteReportConfig",
    			Handler:    _StorageInsights_DeleteReportConfig_Handler,
    		},
    		{
    			MethodName: "ListReportDetails",
    			Handler:    _StorageInsights_ListReportDetails_Handler,
    		},
    		{
    			MethodName: "GetReportDetail",
    			Handler:    _StorageInsights_GetReportDetail_Handler,
    		},
    		{
    			MethodName: "ListDatasetConfigs",
    			Handler:    _StorageInsights_ListDatasetConfigs_Handler,
    		},
    		{
    			MethodName: "GetDatasetConfig",
    			Handler:    _StorageInsights_GetDatasetConfig_Handler,
    		},
    		{
    			MethodName: "CreateDatasetConfig",
    			Handler:    _StorageInsights_CreateDatasetConfig_Handler,
    		},
    		{
    			MethodName: "UpdateDatasetConfig",
    			Handler:    _StorageInsights_UpdateDatasetConfig_Handler,
    		},
    		{
    			MethodName: "DeleteDatasetConfig",
    			Handler:    _StorageInsights_DeleteDatasetConfig_Handler,
    		},
    		{
    			MethodName: "LinkDataset",
    			Handler:    _StorageInsights_LinkDataset_Handler,
    		},
    		{
    			MethodName: "UnlinkDataset",
    			Handler:    _StorageInsights_UnlinkDataset_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/storageinsights/v1/storageinsights.proto",
    }

StorageInsights_ServiceDesc is the grpc.ServiceDesc for StorageInsights service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterStorageInsightsServer 
    
    
    func RegisterStorageInsightsServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv StorageInsightsServer)

## CSVOptions
    
    
    type CSVOptions struct {
    
    	// Record separator characters in CSV.
    	RecordSeparator [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=record_separator,json=recordSeparator,proto3" json:"record_separator,omitempty"`
    	// Delimiter characters in CSV.
    	Delimiter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=delimiter,proto3" json:"delimiter,omitempty"`
    	// If set, will include a header row in the CSV report.
    	HeaderRequired [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=header_required,json=headerRequired,proto3" json:"header_required,omitempty"`
    	// contains filtered or unexported fields
    }

Options to configure CSV formatted reports.

### func (*CSVOptions) Descriptor 
    
    
    func (*CSVOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CSVOptions.ProtoReflect.Descriptor instead.

### func (*CSVOptions) GetDelimiter 
    
    
    func (x *CSVOptions) GetDelimiter() [string](https://pkg.go.dev/builtin#string)

### func (*CSVOptions) GetHeaderRequired 
    
    
    func (x *CSVOptions) GetHeaderRequired() [bool](https://pkg.go.dev/builtin#bool)

### func (*CSVOptions) GetRecordSeparator 
    
    
    func (x *CSVOptions) GetRecordSeparator() [string](https://pkg.go.dev/builtin#string)

### func (*CSVOptions) ProtoMessage 
    
    
    func (*CSVOptions) ProtoMessage()

### func (*CSVOptions) ProtoReflect 
    
    
    func (x *CSVOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CSVOptions) Reset 
    
    
    func (x *CSVOptions) Reset()

### func (*CSVOptions) String 
    
    
    func (x *CSVOptions) String() [string](https://pkg.go.dev/builtin#string)

## CloudStorageDestinationOptions
    
    
    type CloudStorageDestinationOptions struct {
    
    	// Destination bucket.
    	Bucket [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=bucket,proto3" json:"bucket,omitempty"`
    	// Destination path is the path in the bucket where the report should be
    	// generated.
    	DestinationPath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=destination_path,json=destinationPath,proto3" json:"destination_path,omitempty"`
    	// contains filtered or unexported fields
    }

Options to store reports in storage systems. Next ID: 3

### func (*CloudStorageDestinationOptions) Descriptor 
    
    
    func (*CloudStorageDestinationOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloudStorageDestinationOptions.ProtoReflect.Descriptor instead.

### func (*CloudStorageDestinationOptions) GetBucket 
    
    
    func (x *CloudStorageDestinationOptions) GetBucket() [string](https://pkg.go.dev/builtin#string)

### func (*CloudStorageDestinationOptions) GetDestinationPath 
    
    
    func (x *CloudStorageDestinationOptions) GetDestinationPath() [string](https://pkg.go.dev/builtin#string)

### func (*CloudStorageDestinationOptions) ProtoMessage 
    
    
    func (*CloudStorageDestinationOptions) ProtoMessage()

### func (*CloudStorageDestinationOptions) ProtoReflect 
    
    
    func (x *CloudStorageDestinationOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CloudStorageDestinationOptions) Reset 
    
    
    func (x *CloudStorageDestinationOptions) Reset()

### func (*CloudStorageDestinationOptions) String 
    
    
    func (x *CloudStorageDestinationOptions) String() [string](https://pkg.go.dev/builtin#string)

## CloudStorageFilters
    
    
    type CloudStorageFilters struct {
    
    	// Bucket for which the report will be generated.
    	Bucket [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=bucket,proto3" json:"bucket,omitempty"`
    	// contains filtered or unexported fields
    }

Options to filter data on storage systems. Next ID: 2

### func (*CloudStorageFilters) Descriptor 
    
    
    func (*CloudStorageFilters) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloudStorageFilters.ProtoReflect.Descriptor instead.

### func (*CloudStorageFilters) GetBucket 
    
    
    func (x *CloudStorageFilters) GetBucket() [string](https://pkg.go.dev/builtin#string)

### func (*CloudStorageFilters) ProtoMessage 
    
    
    func (*CloudStorageFilters) ProtoMessage()

### func (*CloudStorageFilters) ProtoReflect 
    
    
    func (x *CloudStorageFilters) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CloudStorageFilters) Reset 
    
    
    func (x *CloudStorageFilters) Reset()

### func (*CloudStorageFilters) String 
    
    
    func (x *CloudStorageFilters) String() [string](https://pkg.go.dev/builtin#string)

## CreateDatasetConfigRequest
    
    
    type CreateDatasetConfigRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. ID of the requesting object.
    	// If auto-generating ID is enabled on the server-side, remove this field and
    	// `dataset_config_id` from the method_signature of Create RPC
    	// Note: The value should not contain any hyphens.
    	DatasetConfigId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=dataset_config_id,json=datasetConfigId,proto3" json:"dataset_config_id,omitempty"`
    	// Required. The resource being created
    	DatasetConfig *DatasetConfig `protobuf:"bytes,3,opt,name=dataset_config,json=datasetConfig,proto3" json:"dataset_config,omitempty"`
    	// Optional. A unique identifier for your request.
    	// Specify the request ID if you need to retry the request.
    	// If you retry the request with the same ID within 60 minutes, the server
    	// ignores the request if it has already completed the original request.
    	//
    	// For example, if your initial request times out and you retry the request
    	// using the same request ID, the server recognizes the original request and
    	// does not process the new request.
    	//
    	// The request ID must be a valid UUID and cannot be a zero UUID
    	// (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`CreateDatasetConfig`][google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig]

### func (*CreateDatasetConfigRequest) Descriptor 
    
    
    func (*CreateDatasetConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateDatasetConfigRequest.ProtoReflect.Descriptor instead.

### func (*CreateDatasetConfigRequest) GetDatasetConfig 
    
    
    func (x *CreateDatasetConfigRequest) GetDatasetConfig() *DatasetConfig

### func (*CreateDatasetConfigRequest) GetDatasetConfigId 
    
    
    func (x *CreateDatasetConfigRequest) GetDatasetConfigId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDatasetConfigRequest) GetParent 
    
    
    func (x *CreateDatasetConfigRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDatasetConfigRequest) GetRequestId 
    
    
    func (x *CreateDatasetConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDatasetConfigRequest) ProtoMessage 
    
    
    func (*CreateDatasetConfigRequest) ProtoMessage()

### func (*CreateDatasetConfigRequest) ProtoReflect 
    
    
    func (x *CreateDatasetConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateDatasetConfigRequest) Reset 
    
    
    func (x *CreateDatasetConfigRequest) Reset()

### func (*CreateDatasetConfigRequest) String 
    
    
    func (x *CreateDatasetConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateReportConfigRequest
    
    
    type CreateReportConfigRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The resource being created
    	ReportConfig *ReportConfig `protobuf:"bytes,3,opt,name=report_config,json=reportConfig,proto3" json:"report_config,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a ReportConfig

### func (*CreateReportConfigRequest) Descriptor 
    
    
    func (*CreateReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*CreateReportConfigRequest) GetParent 
    
    
    func (x *CreateReportConfigRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportConfigRequest) GetReportConfig 
    
    
    func (x *CreateReportConfigRequest) GetReportConfig() *ReportConfig

### func (*CreateReportConfigRequest) GetRequestId 
    
    
    func (x *CreateReportConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportConfigRequest) ProtoMessage 
    
    
    func (*CreateReportConfigRequest) ProtoMessage()

### func (*CreateReportConfigRequest) ProtoReflect 
    
    
    func (x *CreateReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateReportConfigRequest) Reset 
    
    
    func (x *CreateReportConfigRequest) Reset()

### func (*CreateReportConfigRequest) String 
    
    
    func (x *CreateReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig
    
    
    type DatasetConfig struct {
    
    	// Identifier. name of resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The UTC time at which the dataset configuration was created.
    	// This is auto-populated.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The UTC time at which the dataset configuration was last
    	// updated. This is auto-populated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Labels as key value pairs
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Output only. System generated unique identifier for the resource.
    	Uid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=uid,proto3" json:"uid,omitempty"`
    	// Optional. Organization resource ID that the source projects should belong
    	// to. Projects that do not belong to the provided organization are not
    	// considered when creating the dataset.
    	OrganizationNumber [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,22,opt,name=organization_number,json=organizationNumber,proto3" json:"organization_number,omitempty"`
    	// Defines the options for providing source identifiers for the dataset.
    	//
    	// Types that are valid to be assigned to SourceOptions:
    	//
    	//	*DatasetConfig_SourceProjects_
    	//	*DatasetConfig_SourceFolders_
    	//	*DatasetConfig_OrganizationScope
    	//	*DatasetConfig_CloudStorageObjectPath
    	SourceOptions isDatasetConfig_SourceOptions `protobuf_oneof:"source_options"`
    	// Cloud Storage locations to include or exclude.
    	//
    	// Types that are valid to be assigned to CloudStorageLocations:
    	//
    	//	*DatasetConfig_IncludeCloudStorageLocations
    	//	*DatasetConfig_ExcludeCloudStorageLocations
    	CloudStorageLocations isDatasetConfig_CloudStorageLocations `protobuf_oneof:"cloud_storage_locations"`
    	// Cloud Storage buckets to include or exclude.
    	//
    	// Types that are valid to be assigned to CloudStorageBuckets:
    	//
    	//	*DatasetConfig_IncludeCloudStorageBuckets
    	//	*DatasetConfig_ExcludeCloudStorageBuckets
    	CloudStorageBuckets isDatasetConfig_CloudStorageBuckets `protobuf_oneof:"cloud_storage_buckets"`
    	// If set to `true`, the request includes all the newly created buckets in the
    	// dataset that meet the inclusion and exclusion rules.
    	IncludeNewlyCreatedBuckets [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=include_newly_created_buckets,json=includeNewlyCreatedBuckets,proto3" json:"include_newly_created_buckets,omitempty"`
    	// Optional. If set to `false`, then all the permission checks must be
    	// successful before the system can start ingesting data. This field can only
    	// be updated before the system ingests data for the first time. Any attempt
    	// to modify the field after data ingestion starts results in an error.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.
    	SkipVerificationAndIngest [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,19,opt,name=skip_verification_and_ingest,json=skipVerificationAndIngest,proto3" json:"skip_verification_and_ingest,omitempty"`
    	// Number of days of history that must be retained.
    	RetentionPeriodDays [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,14,opt,name=retention_period_days,json=retentionPeriodDays,proto3" json:"retention_period_days,omitempty"`
    	// Details of the linked dataset.
    	Link *DatasetConfig_Link `protobuf:"bytes,15,opt,name=link,proto3" json:"link,omitempty"`
    	// Identity used by this `datasetConfig`.
    	Identity *Identity `protobuf:"bytes,16,opt,name=identity,proto3" json:"identity,omitempty"`
    	// Output only. Status of the `datasetConfig`.
    	Status *status.Status `protobuf:"bytes,17,opt,name=status,proto3" json:"status,omitempty"`
    	// Output only. State of the `datasetConfig`.
    	DatasetConfigState DatasetConfig_ConfigState `protobuf:"varint,18,opt,name=dataset_config_state,json=datasetConfigState,proto3,enum=google.cloud.storageinsights.v1.DatasetConfig_ConfigState" json:"dataset_config_state,omitempty"`
    	// Optional. A user-provided description for the dataset configuration.
    	//
    	// Maximum length: 256 characters.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,20,opt,name=description,proto3" json:"description,omitempty"`
    	// contains filtered or unexported fields
    }

Message describing the dataset configuration properties. For more information, see [Dataset configuration properties](https://cloud.google.com/storage/docs/insights/datasets#dataset-config).

### func (*DatasetConfig) Descriptor 
    
    
    func (*DatasetConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig.ProtoReflect.Descriptor instead.

### func (*DatasetConfig) GetCloudStorageBuckets 
    
    
    func (x *DatasetConfig) GetCloudStorageBuckets() isDatasetConfig_CloudStorageBuckets

### func (*DatasetConfig) GetCloudStorageLocations 
    
    
    func (x *DatasetConfig) GetCloudStorageLocations() isDatasetConfig_CloudStorageLocations

### func (*DatasetConfig) GetCloudStorageObjectPath 
    
    
    func (x *DatasetConfig) GetCloudStorageObjectPath() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig) GetCreateTime 
    
    
    func (x *DatasetConfig) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*DatasetConfig) GetDatasetConfigState 
    
    
    func (x *DatasetConfig) GetDatasetConfigState() DatasetConfig_ConfigState

### func (*DatasetConfig) GetDescription 
    
    
    func (x *DatasetConfig) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig) GetExcludeCloudStorageBuckets 
    
    
    func (x *DatasetConfig) GetExcludeCloudStorageBuckets() *DatasetConfig_CloudStorageBuckets

### func (*DatasetConfig) GetExcludeCloudStorageLocations 
    
    
    func (x *DatasetConfig) GetExcludeCloudStorageLocations() *DatasetConfig_CloudStorageLocations

### func (*DatasetConfig) GetIdentity 
    
    
    func (x *DatasetConfig) GetIdentity() *Identity

### func (*DatasetConfig) GetIncludeCloudStorageBuckets 
    
    
    func (x *DatasetConfig) GetIncludeCloudStorageBuckets() *DatasetConfig_CloudStorageBuckets

### func (*DatasetConfig) GetIncludeCloudStorageLocations 
    
    
    func (x *DatasetConfig) GetIncludeCloudStorageLocations() *DatasetConfig_CloudStorageLocations

### func (*DatasetConfig) GetIncludeNewlyCreatedBuckets 
    
    
    func (x *DatasetConfig) GetIncludeNewlyCreatedBuckets() [bool](https://pkg.go.dev/builtin#bool)

### func (*DatasetConfig) GetLabels 
    
    
    func (x *DatasetConfig) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig) GetLink 
    
    
    func (x *DatasetConfig) GetLink() *DatasetConfig_Link

### func (*DatasetConfig) GetName 
    
    
    func (x *DatasetConfig) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig) GetOrganizationNumber 
    
    
    func (x *DatasetConfig) GetOrganizationNumber() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig) GetOrganizationScope 
    
    
    func (x *DatasetConfig) GetOrganizationScope() [bool](https://pkg.go.dev/builtin#bool)

### func (*DatasetConfig) GetRetentionPeriodDays 
    
    
    func (x *DatasetConfig) GetRetentionPeriodDays() [int32](https://pkg.go.dev/builtin#int32)

### func (*DatasetConfig) GetSkipVerificationAndIngest 
    
    
    func (x *DatasetConfig) GetSkipVerificationAndIngest() [bool](https://pkg.go.dev/builtin#bool)

Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.

### func (*DatasetConfig) GetSourceFolders 
    
    
    func (x *DatasetConfig) GetSourceFolders() *DatasetConfig_SourceFolders

### func (*DatasetConfig) GetSourceOptions 
    
    
    func (x *DatasetConfig) GetSourceOptions() isDatasetConfig_SourceOptions

### func (*DatasetConfig) GetSourceProjects 
    
    
    func (x *DatasetConfig) GetSourceProjects() *DatasetConfig_SourceProjects

### func (*DatasetConfig) GetStatus 
    
    
    func (x *DatasetConfig) GetStatus() *[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*DatasetConfig) GetUid 
    
    
    func (x *DatasetConfig) GetUid() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig) GetUpdateTime 
    
    
    func (x *DatasetConfig) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*DatasetConfig) ProtoMessage 
    
    
    func (*DatasetConfig) ProtoMessage()

### func (*DatasetConfig) ProtoReflect 
    
    
    func (x *DatasetConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig) Reset 
    
    
    func (x *DatasetConfig) Reset()

### func (*DatasetConfig) String 
    
    
    func (x *DatasetConfig) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_BucketErrors
    
    
    type DatasetConfig_BucketErrors struct {
    
    	// Optional. Count of successfully validated buckets.
    	ValidatedCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=validated_count,json=validatedCount,proto3" json:"validated_count,omitempty"`
    	// Optional. Count of buckets with permission denied errors.
    	PermissionDeniedCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=permission_denied_count,json=permissionDeniedCount,proto3" json:"permission_denied_count,omitempty"`
    	// Optional. Subset of bucket names that have permission denied.
    	PermissionDeniedBucketIds [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=permission_denied_bucket_ids,json=permissionDeniedBucketIds,proto3" json:"permission_denied_bucket_ids,omitempty"`
    	// Optional. Count of buckets that are not subscribed to Storage
    	// Intelligence.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.
    	NonManagementHubEntitledCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=non_management_hub_entitled_count,json=nonManagementHubEntitledCount,proto3" json:"non_management_hub_entitled_count,omitempty"`
    	// Optional. Number of buckets that encountered internal errors during the
    	// validation process. These buckets are automatically retried in subsequent
    	// validation attempts.
    	InternalErrorCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=internal_error_count,json=internalErrorCount,proto3" json:"internal_error_count,omitempty"`
    	// Optional. Count of buckets that are not subscribed to Storage
    	// Intelligence.
    	NonStorageIntelligenceEntitledCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,7,opt,name=non_storage_intelligence_entitled_count,json=nonStorageIntelligenceEntitledCount,proto3" json:"non_storage_intelligence_entitled_count,omitempty"`
    	// Optional. Subset of bucket names that are not subscribed to Storage
    	// Intelligence.
    	NonStorageIntelligenceEntitledBucketIds [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,rep,name=non_storage_intelligence_entitled_bucket_ids,json=nonStorageIntelligenceEntitledBucketIds,proto3" json:"non_storage_intelligence_entitled_bucket_ids,omitempty"`
    	// contains filtered or unexported fields
    }

Provides a summary of the bucket level error statistics.

### func (*DatasetConfig_BucketErrors) Descriptor 
    
    
    func (*DatasetConfig_BucketErrors) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_BucketErrors.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_BucketErrors) GetInternalErrorCount 
    
    
    func (x *DatasetConfig_BucketErrors) GetInternalErrorCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_BucketErrors) GetNonManagementHubEntitledCount 
    
    
    func (x *DatasetConfig_BucketErrors) GetNonManagementHubEntitledCount() [int64](https://pkg.go.dev/builtin#int64)

Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.

### func (*DatasetConfig_BucketErrors) GetNonStorageIntelligenceEntitledBucketIds 
    
    
    func (x *DatasetConfig_BucketErrors) GetNonStorageIntelligenceEntitledBucketIds() [][string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_BucketErrors) GetNonStorageIntelligenceEntitledCount 
    
    
    func (x *DatasetConfig_BucketErrors) GetNonStorageIntelligenceEntitledCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_BucketErrors) GetPermissionDeniedBucketIds 
    
    
    func (x *DatasetConfig_BucketErrors) GetPermissionDeniedBucketIds() [][string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_BucketErrors) GetPermissionDeniedCount 
    
    
    func (x *DatasetConfig_BucketErrors) GetPermissionDeniedCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_BucketErrors) GetValidatedCount 
    
    
    func (x *DatasetConfig_BucketErrors) GetValidatedCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_BucketErrors) ProtoMessage 
    
    
    func (*DatasetConfig_BucketErrors) ProtoMessage()

### func (*DatasetConfig_BucketErrors) ProtoReflect 
    
    
    func (x *DatasetConfig_BucketErrors) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_BucketErrors) Reset 
    
    
    func (x *DatasetConfig_BucketErrors) Reset()

### func (*DatasetConfig_BucketErrors) String 
    
    
    func (x *DatasetConfig_BucketErrors) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_CloudStorageBuckets
    
    
    type DatasetConfig_CloudStorageBuckets struct {
    	CloudStorageBuckets []*DatasetConfig_CloudStorageBuckets_CloudStorageBucket `protobuf:"bytes,1,rep,name=cloud_storage_buckets,json=cloudStorageBuckets,proto3" json:"cloud_storage_buckets,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of Cloud Storage buckets.

### func (*DatasetConfig_CloudStorageBuckets) Descriptor 
    
    
    func (*DatasetConfig_CloudStorageBuckets) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_CloudStorageBuckets.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_CloudStorageBuckets) GetCloudStorageBuckets 
    
    
    func (x *DatasetConfig_CloudStorageBuckets) GetCloudStorageBuckets() []*DatasetConfig_CloudStorageBuckets_CloudStorageBucket

### func (*DatasetConfig_CloudStorageBuckets) ProtoMessage 
    
    
    func (*DatasetConfig_CloudStorageBuckets) ProtoMessage()

### func (*DatasetConfig_CloudStorageBuckets) ProtoReflect 
    
    
    func (x *DatasetConfig_CloudStorageBuckets) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_CloudStorageBuckets) Reset 
    
    
    func (x *DatasetConfig_CloudStorageBuckets) Reset()

### func (*DatasetConfig_CloudStorageBuckets) String 
    
    
    func (x *DatasetConfig_CloudStorageBuckets) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_CloudStorageBuckets_CloudStorageBucket
    
    
    type DatasetConfig_CloudStorageBuckets_CloudStorageBucket struct {
    
    	// Types that are valid to be assigned to CloudStorageBucket:
    	//
    	//	*DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketName
    	//	*DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketPrefixRegex
    	CloudStorageBucket isDatasetConfig_CloudStorageBuckets_CloudStorageBucket_CloudStorageBucket `protobuf_oneof:"cloud_storage_bucket"`
    	// contains filtered or unexported fields
    }

Defines the bucket by its name or a regex pattern to match buckets.

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) Descriptor 
    
    
    func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_CloudStorageBuckets_CloudStorageBucket.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetBucketName 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetBucketName() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetBucketPrefixRegex 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetBucketPrefixRegex() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetCloudStorageBucket 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) GetCloudStorageBucket() isDatasetConfig_CloudStorageBuckets_CloudStorageBucket_CloudStorageBucket

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) ProtoMessage 
    
    
    func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) ProtoMessage()

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) ProtoReflect 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) Reset 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) Reset()

### func (*DatasetConfig_CloudStorageBuckets_CloudStorageBucket) String 
    
    
    func (x *DatasetConfig_CloudStorageBuckets_CloudStorageBucket) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketName
    
    
    type DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketName struct {
    	// Cloud Storage bucket name.
    	BucketName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=bucket_name,json=bucketName,proto3,oneof"`
    }

## DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketPrefixRegex
    
    
    type DatasetConfig_CloudStorageBuckets_CloudStorageBucket_BucketPrefixRegex struct {
    	// A regex pattern for bucket names matching the regex. Regex should
    	// follow the syntax specified in `google/re2` on GitHub.
    	BucketPrefixRegex [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=bucket_prefix_regex,json=bucketPrefixRegex,proto3,oneof"`
    }

## DatasetConfig_CloudStorageLocations
    
    
    type DatasetConfig_CloudStorageLocations struct {
    	Locations [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=locations,proto3" json:"locations,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of Cloud Storage locations.

### func (*DatasetConfig_CloudStorageLocations) Descriptor 
    
    
    func (*DatasetConfig_CloudStorageLocations) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_CloudStorageLocations.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_CloudStorageLocations) GetLocations 
    
    
    func (x *DatasetConfig_CloudStorageLocations) GetLocations() [][string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_CloudStorageLocations) ProtoMessage 
    
    
    func (*DatasetConfig_CloudStorageLocations) ProtoMessage()

### func (*DatasetConfig_CloudStorageLocations) ProtoReflect 
    
    
    func (x *DatasetConfig_CloudStorageLocations) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_CloudStorageLocations) Reset 
    
    
    func (x *DatasetConfig_CloudStorageLocations) Reset()

### func (*DatasetConfig_CloudStorageLocations) String 
    
    
    func (x *DatasetConfig_CloudStorageLocations) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_CloudStorageObjectPath
    
    
    type DatasetConfig_CloudStorageObjectPath struct {
    	// Input only. Cloud Storage object path containing a list of
    	// project or folder numbers to include in the dataset;
    	// it cannot contain a mix of project and folders.
    	//
    	// The object must be a text file where each line has one of the following
    	// entries:
    	//
    	// - Project number, formatted as `projects/{project_number}`, for example,
    	// `projects/1234567890`.
    	// - Folder identifier, formatted as `folders/{folder_number}`, for example,
    	// `folders/9876543210`.
    	// Path must be in the format `gs://{bucket_name}/{object_name}`.
    	CloudStorageObjectPath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,21,opt,name=cloud_storage_object_path,json=cloudStorageObjectPath,proto3,oneof"`
    }

## DatasetConfig_ConfigState
    
    
    type DatasetConfig_ConfigState [int32](https://pkg.go.dev/builtin#int32)

State of the configuration.

### DatasetConfig_CONFIG_STATE_UNSPECIFIED, DatasetConfig_CONFIG_STATE_ACTIVE, DatasetConfig_CONFIG_STATE_VERIFICATION_IN_PROGRESS, DatasetConfig_CONFIG_STATE_CREATED, DatasetConfig_CONFIG_STATE_PROCESSING
    
    
    const (
    	// Unspecified state.
    	DatasetConfig_CONFIG_STATE_UNSPECIFIED DatasetConfig_ConfigState = 0
    	// Active configuration indicates that the configuration is
    	// actively ingesting data.
    	DatasetConfig_CONFIG_STATE_ACTIVE DatasetConfig_ConfigState = 1
    	// In this state, the configuration is being verified for various
    	// permissions.
    	DatasetConfig_CONFIG_STATE_VERIFICATION_IN_PROGRESS DatasetConfig_ConfigState = 2
    	// Configuration is created and further processing needs to happen.
    	DatasetConfig_CONFIG_STATE_CREATED DatasetConfig_ConfigState = 3
    	// Configuration is under processing
    	DatasetConfig_CONFIG_STATE_PROCESSING DatasetConfig_ConfigState = 4
    )

### func (DatasetConfig_ConfigState) Descriptor 
    
    
    func (DatasetConfig_ConfigState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (DatasetConfig_ConfigState) Enum 
    
    
    func (x DatasetConfig_ConfigState) Enum() *DatasetConfig_ConfigState

### func (DatasetConfig_ConfigState) EnumDescriptor 
    
    
    func (DatasetConfig_ConfigState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_ConfigState.Descriptor instead.

### func (DatasetConfig_ConfigState) Number 
    
    
    func (x DatasetConfig_ConfigState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (DatasetConfig_ConfigState) String 
    
    
    func (x DatasetConfig_ConfigState) String() [string](https://pkg.go.dev/builtin#string)

### func (DatasetConfig_ConfigState) Type 
    
    
    func (DatasetConfig_ConfigState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DatasetConfig_ExcludeCloudStorageBuckets
    
    
    type DatasetConfig_ExcludeCloudStorageBuckets struct {
    	ExcludeCloudStorageBuckets *DatasetConfig_CloudStorageBuckets `protobuf:"bytes,11,opt,name=exclude_cloud_storage_buckets,json=excludeCloudStorageBuckets,proto3,oneof"`
    }

## DatasetConfig_ExcludeCloudStorageLocations
    
    
    type DatasetConfig_ExcludeCloudStorageLocations struct {
    	ExcludeCloudStorageLocations *DatasetConfig_CloudStorageLocations `protobuf:"bytes,9,opt,name=exclude_cloud_storage_locations,json=excludeCloudStorageLocations,proto3,oneof"`
    }

## DatasetConfig_IncludeCloudStorageBuckets
    
    
    type DatasetConfig_IncludeCloudStorageBuckets struct {
    	IncludeCloudStorageBuckets *DatasetConfig_CloudStorageBuckets `protobuf:"bytes,10,opt,name=include_cloud_storage_buckets,json=includeCloudStorageBuckets,proto3,oneof"`
    }

## DatasetConfig_IncludeCloudStorageLocations
    
    
    type DatasetConfig_IncludeCloudStorageLocations struct {
    	IncludeCloudStorageLocations *DatasetConfig_CloudStorageLocations `protobuf:"bytes,8,opt,name=include_cloud_storage_locations,json=includeCloudStorageLocations,proto3,oneof"`
    }

## DatasetConfig_Link
    
    
    type DatasetConfig_Link struct {
    
    	// Output only. Dataset name for linked dataset.
    	Dataset [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=dataset,proto3" json:"dataset,omitempty"`
    	// Output only. State of the linked dataset.
    	Linked [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=linked,proto3" json:"linked,omitempty"`
    	// contains filtered or unexported fields
    }

Defines the details about the linked dataset.

### func (*DatasetConfig_Link) Descriptor 
    
    
    func (*DatasetConfig_Link) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_Link.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_Link) GetDataset 
    
    
    func (x *DatasetConfig_Link) GetDataset() [string](https://pkg.go.dev/builtin#string)

### func (*DatasetConfig_Link) GetLinked 
    
    
    func (x *DatasetConfig_Link) GetLinked() [bool](https://pkg.go.dev/builtin#bool)

### func (*DatasetConfig_Link) ProtoMessage 
    
    
    func (*DatasetConfig_Link) ProtoMessage()

### func (*DatasetConfig_Link) ProtoReflect 
    
    
    func (x *DatasetConfig_Link) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_Link) Reset 
    
    
    func (x *DatasetConfig_Link) Reset()

### func (*DatasetConfig_Link) String 
    
    
    func (x *DatasetConfig_Link) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_OrganizationScope
    
    
    type DatasetConfig_OrganizationScope struct {
    	// Defines the options for providing a source organization for the dataset.
    	OrganizationScope [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,25,opt,name=organization_scope,json=organizationScope,proto3,oneof"`
    }

## DatasetConfig_ProjectErrors
    
    
    type DatasetConfig_ProjectErrors struct {
    
    	// Optional. Count of successfully validated projects.
    	ValidatedCount *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=validated_count,json=validatedCount,proto3,oneof" json:"validated_count,omitempty"`
    	// Optional. Count of projects which are not in the same organization.
    	OutsideOrgErrorCount *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=outside_org_error_count,json=outsideOrgErrorCount,proto3,oneof" json:"outside_org_error_count,omitempty"`
    	// Optional. Subset of project numbers which are not in the same
    	// organization.
    	OutsideOrgProjectNumbers [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,rep,packed,name=outside_org_project_numbers,json=outsideOrgProjectNumbers,proto3" json:"outside_org_project_numbers,omitempty"`
    	// Optional. Count of projects that are not subscribed to Storage
    	// Intelligence.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.
    	NonManagementHubEntitledErrorCount *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,7,opt,name=non_management_hub_entitled_error_count,json=nonManagementHubEntitledErrorCount,proto3,oneof" json:"non_management_hub_entitled_error_count,omitempty"`
    	// Optional. Subset of project numbers that are not subscribed to Storage
    	// Intelligence.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.
    	NonManagementHubEntitledProjectNumbers [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,8,rep,packed,name=non_management_hub_entitled_project_numbers,json=nonManagementHubEntitledProjectNumbers,proto3" json:"non_management_hub_entitled_project_numbers,omitempty"`
    	// Optional. Count of projects that are not subscribed to Storage
    	// Intelligence.
    	NonStorageIntelligenceEntitledErrorCount *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,9,opt,name=non_storage_intelligence_entitled_error_count,json=nonStorageIntelligenceEntitledErrorCount,proto3,oneof" json:"non_storage_intelligence_entitled_error_count,omitempty"`
    	// Optional. Subset of project numbers that are not subscribed to Storage
    	// Intelligence.
    	NonStorageIntelligenceEntitledProjectNumbers [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,10,rep,packed,name=non_storage_intelligence_entitled_project_numbers,json=nonStorageIntelligenceEntitledProjectNumbers,proto3" json:"non_storage_intelligence_entitled_project_numbers,omitempty"`
    	// Optional. Number of projects that encountered internal errors during
    	// validation and are automatically retried.
    	InternalErrorCount *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=internal_error_count,json=internalErrorCount,proto3,oneof" json:"internal_error_count,omitempty"`
    	// The destination project check result. It indicates whether the project
    	// is in the correct organization or if an internal error occurred during
    	// the check.
    	//
    	// Types that are valid to be assigned to DestinationProjectCheckResult:
    	//
    	//	*DatasetConfig_ProjectErrors_DestinationProjectOrgError
    	//	*DatasetConfig_ProjectErrors_DestinationProjectCheckHasInternalError
    	DestinationProjectCheckResult isDatasetConfig_ProjectErrors_DestinationProjectCheckResult `protobuf_oneof:"destination_project_check_result"`
    	// contains filtered or unexported fields
    }

Provides a summary of the project level error statistics.

### func (*DatasetConfig_ProjectErrors) Descriptor 
    
    
    func (*DatasetConfig_ProjectErrors) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_ProjectErrors.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_ProjectErrors) GetDestinationProjectCheckHasInternalError 
    
    
    func (x *DatasetConfig_ProjectErrors) GetDestinationProjectCheckHasInternalError() [bool](https://pkg.go.dev/builtin#bool)

### func (*DatasetConfig_ProjectErrors) GetDestinationProjectCheckResult 
    
    
    func (x *DatasetConfig_ProjectErrors) GetDestinationProjectCheckResult() isDatasetConfig_ProjectErrors_DestinationProjectCheckResult

### func (*DatasetConfig_ProjectErrors) GetDestinationProjectOrgError 
    
    
    func (x *DatasetConfig_ProjectErrors) GetDestinationProjectOrgError() [bool](https://pkg.go.dev/builtin#bool)

### func (*DatasetConfig_ProjectErrors) GetInternalErrorCount 
    
    
    func (x *DatasetConfig_ProjectErrors) GetInternalErrorCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) GetNonManagementHubEntitledErrorCount 
    
    
    func (x *DatasetConfig_ProjectErrors) GetNonManagementHubEntitledErrorCount() [int64](https://pkg.go.dev/builtin#int64)

Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.

### func (*DatasetConfig_ProjectErrors) GetNonManagementHubEntitledProjectNumbers 
    
    
    func (x *DatasetConfig_ProjectErrors) GetNonManagementHubEntitledProjectNumbers() [][int64](https://pkg.go.dev/builtin#int64)

Deprecated: Marked as deprecated in google/cloud/storageinsights/v1/storageinsights.proto.

### func (*DatasetConfig_ProjectErrors) GetNonStorageIntelligenceEntitledErrorCount 
    
    
    func (x *DatasetConfig_ProjectErrors) GetNonStorageIntelligenceEntitledErrorCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) GetNonStorageIntelligenceEntitledProjectNumbers 
    
    
    func (x *DatasetConfig_ProjectErrors) GetNonStorageIntelligenceEntitledProjectNumbers() [][int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) GetOutsideOrgErrorCount 
    
    
    func (x *DatasetConfig_ProjectErrors) GetOutsideOrgErrorCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) GetOutsideOrgProjectNumbers 
    
    
    func (x *DatasetConfig_ProjectErrors) GetOutsideOrgProjectNumbers() [][int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) GetValidatedCount 
    
    
    func (x *DatasetConfig_ProjectErrors) GetValidatedCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_ProjectErrors) ProtoMessage 
    
    
    func (*DatasetConfig_ProjectErrors) ProtoMessage()

### func (*DatasetConfig_ProjectErrors) ProtoReflect 
    
    
    func (x *DatasetConfig_ProjectErrors) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_ProjectErrors) Reset 
    
    
    func (x *DatasetConfig_ProjectErrors) Reset()

### func (*DatasetConfig_ProjectErrors) String 
    
    
    func (x *DatasetConfig_ProjectErrors) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_ProjectErrors_DestinationProjectCheckHasInternalError
    
    
    type DatasetConfig_ProjectErrors_DestinationProjectCheckHasInternalError struct {
    	// Optional. Indicates whether the destination project check failed due to
    	// an internal error. If `true`, the system automatically retries the
    	// check.
    	DestinationProjectCheckHasInternalError [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=destination_project_check_has_internal_error,json=destinationProjectCheckHasInternalError,proto3,oneof"`
    }

## DatasetConfig_ProjectErrors_DestinationProjectOrgError
    
    
    type DatasetConfig_ProjectErrors_DestinationProjectOrgError struct {
    	// Optional. Indicates if the destination project resides within the same
    	// organization as the source project.
    	DestinationProjectOrgError [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=destination_project_org_error,json=destinationProjectOrgError,proto3,oneof"`
    }

## DatasetConfig_SourceFolders
    
    
    type DatasetConfig_SourceFolders struct {
    
    	// Optional. The list of folder numbers to include in the dataset.
    	FolderNumbers [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,rep,packed,name=folder_numbers,json=folderNumbers,proto3" json:"folder_numbers,omitempty"`
    	// contains filtered or unexported fields
    }

Specifies a set of folders to include in the dataset

### func (*DatasetConfig_SourceFolders) Descriptor 
    
    
    func (*DatasetConfig_SourceFolders) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_SourceFolders.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_SourceFolders) GetFolderNumbers 
    
    
    func (x *DatasetConfig_SourceFolders) GetFolderNumbers() [][int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_SourceFolders) ProtoMessage 
    
    
    func (*DatasetConfig_SourceFolders) ProtoMessage()

### func (*DatasetConfig_SourceFolders) ProtoReflect 
    
    
    func (x *DatasetConfig_SourceFolders) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_SourceFolders) Reset 
    
    
    func (x *DatasetConfig_SourceFolders) Reset()

### func (*DatasetConfig_SourceFolders) String 
    
    
    func (x *DatasetConfig_SourceFolders) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_SourceFolders_
    
    
    type DatasetConfig_SourceFolders_ struct {
    	// Defines the options for providing source folders for the dataset.
    	SourceFolders *DatasetConfig_SourceFolders `protobuf:"bytes,24,opt,name=source_folders,json=sourceFolders,proto3,oneof"`
    }

## DatasetConfig_SourceProjects
    
    
    type DatasetConfig_SourceProjects struct {
    	ProjectNumbers [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,rep,packed,name=project_numbers,json=projectNumbers,proto3" json:"project_numbers,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of project numbers

### func (*DatasetConfig_SourceProjects) Descriptor 
    
    
    func (*DatasetConfig_SourceProjects) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_SourceProjects.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_SourceProjects) GetProjectNumbers 
    
    
    func (x *DatasetConfig_SourceProjects) GetProjectNumbers() [][int64](https://pkg.go.dev/builtin#int64)

### func (*DatasetConfig_SourceProjects) ProtoMessage 
    
    
    func (*DatasetConfig_SourceProjects) ProtoMessage()

### func (*DatasetConfig_SourceProjects) ProtoReflect 
    
    
    func (x *DatasetConfig_SourceProjects) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_SourceProjects) Reset 
    
    
    func (x *DatasetConfig_SourceProjects) Reset()

### func (*DatasetConfig_SourceProjects) String 
    
    
    func (x *DatasetConfig_SourceProjects) String() [string](https://pkg.go.dev/builtin#string)

## DatasetConfig_SourceProjects_
    
    
    type DatasetConfig_SourceProjects_ struct {
    	// Defines the options for providing source projects for the dataset.
    	SourceProjects *DatasetConfig_SourceProjects `protobuf:"bytes,7,opt,name=source_projects,json=sourceProjects,proto3,oneof"`
    }

## DatasetConfig_ValidationErrorsBeforeIngestion
    
    
    type DatasetConfig_ValidationErrorsBeforeIngestion struct {
    
    	// Optional. Provides a summary of the bucket level error stats.
    	BucketErrors *DatasetConfig_BucketErrors `protobuf:"bytes,1,opt,name=bucket_errors,json=bucketErrors,proto3" json:"bucket_errors,omitempty"`
    	// Optional. Provides a summary of the project level error stats.
    	ProjectErrors *DatasetConfig_ProjectErrors `protobuf:"bytes,2,opt,name=project_errors,json=projectErrors,proto3" json:"project_errors,omitempty"`
    	// contains filtered or unexported fields
    }

Summary of validation errors that occurred during the verification phase.

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) Descriptor 
    
    
    func (*DatasetConfig_ValidationErrorsBeforeIngestion) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DatasetConfig_ValidationErrorsBeforeIngestion.ProtoReflect.Descriptor instead.

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) GetBucketErrors 
    
    
    func (x *DatasetConfig_ValidationErrorsBeforeIngestion) GetBucketErrors() *DatasetConfig_BucketErrors

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) GetProjectErrors 
    
    
    func (x *DatasetConfig_ValidationErrorsBeforeIngestion) GetProjectErrors() *DatasetConfig_ProjectErrors

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) ProtoMessage 
    
    
    func (*DatasetConfig_ValidationErrorsBeforeIngestion) ProtoMessage()

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) ProtoReflect 
    
    
    func (x *DatasetConfig_ValidationErrorsBeforeIngestion) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) Reset 
    
    
    func (x *DatasetConfig_ValidationErrorsBeforeIngestion) Reset()

### func (*DatasetConfig_ValidationErrorsBeforeIngestion) String 
    
    
    func (x *DatasetConfig_ValidationErrorsBeforeIngestion) String() [string](https://pkg.go.dev/builtin#string)

## DeleteDatasetConfigRequest
    
    
    type DeleteDatasetConfigRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A unique identifier for your request.
    	// Specify the request ID if you need to retry the request.
    	// If you retry the request with the same ID within 60 minutes, the server
    	// ignores the request if it has already completed the original request.
    	//
    	// For example, if your initial request times out and you retry the request
    	// using the same request ID, the server recognizes the original request and
    	// does not process the new request.
    	//
    	// The request ID must be a valid UUID and cannot be a zero UUID
    	// (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`DeleteDatasetConfig`][google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig]

### func (*DeleteDatasetConfigRequest) Descriptor 
    
    
    func (*DeleteDatasetConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteDatasetConfigRequest.ProtoReflect.Descriptor instead.

### func (*DeleteDatasetConfigRequest) GetName 
    
    
    func (x *DeleteDatasetConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteDatasetConfigRequest) GetRequestId 
    
    
    func (x *DeleteDatasetConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteDatasetConfigRequest) ProtoMessage 
    
    
    func (*DeleteDatasetConfigRequest) ProtoMessage()

### func (*DeleteDatasetConfigRequest) ProtoReflect 
    
    
    func (x *DeleteDatasetConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteDatasetConfigRequest) Reset 
    
    
    func (x *DeleteDatasetConfigRequest) Reset()

### func (*DeleteDatasetConfigRequest) String 
    
    
    func (x *DeleteDatasetConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteReportConfigRequest
    
    
    type DeleteReportConfigRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. If set, all ReportDetails for this ReportConfig will be deleted.
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=force,proto3" json:"force,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for deleting a ReportConfig

### func (*DeleteReportConfigRequest) Descriptor 
    
    
    func (*DeleteReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*DeleteReportConfigRequest) GetForce 
    
    
    func (x *DeleteReportConfigRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteReportConfigRequest) GetName 
    
    
    func (x *DeleteReportConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportConfigRequest) GetRequestId 
    
    
    func (x *DeleteReportConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportConfigRequest) ProtoMessage 
    
    
    func (*DeleteReportConfigRequest) ProtoMessage()

### func (*DeleteReportConfigRequest) ProtoReflect 
    
    
    func (x *DeleteReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteReportConfigRequest) Reset 
    
    
    func (x *DeleteReportConfigRequest) Reset()

### func (*DeleteReportConfigRequest) String 
    
    
    func (x *DeleteReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## FrequencyOptions
    
    
    type FrequencyOptions struct {
    
    	// Frequency of report generation.
    	Frequency FrequencyOptions_Frequency `protobuf:"varint,1,opt,name=frequency,proto3,enum=google.cloud.storageinsights.v1.FrequencyOptions_Frequency" json:"frequency,omitempty"`
    	// The date from which report generation should start.
    	// UTC time zone.
    	StartDate *date.Date `protobuf:"bytes,2,opt,name=start_date,json=startDate,proto3" json:"start_date,omitempty"`
    	// The date on which report generation should stop (Inclusive).
    	// UTC time zone.
    	EndDate *date.Date `protobuf:"bytes,3,opt,name=end_date,json=endDate,proto3" json:"end_date,omitempty"`
    	// contains filtered or unexported fields
    }

ReportConfig Resource:

Options to setup frequency of report generation.

### func (*FrequencyOptions) Descriptor 
    
    
    func (*FrequencyOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FrequencyOptions.ProtoReflect.Descriptor instead.

### func (*FrequencyOptions) GetEndDate 
    
    
    func (x *FrequencyOptions) GetEndDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*FrequencyOptions) GetFrequency 
    
    
    func (x *FrequencyOptions) GetFrequency() FrequencyOptions_Frequency

### func (*FrequencyOptions) GetStartDate 
    
    
    func (x *FrequencyOptions) GetStartDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*FrequencyOptions) ProtoMessage 
    
    
    func (*FrequencyOptions) ProtoMessage()

### func (*FrequencyOptions) ProtoReflect 
    
    
    func (x *FrequencyOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FrequencyOptions) Reset 
    
    
    func (x *FrequencyOptions) Reset()

### func (*FrequencyOptions) String 
    
    
    func (x *FrequencyOptions) String() [string](https://pkg.go.dev/builtin#string)

## FrequencyOptions_Frequency
    
    
    type FrequencyOptions_Frequency [int32](https://pkg.go.dev/builtin#int32)

This ENUM specifies possible frequencies of report generation.

### FrequencyOptions_FREQUENCY_UNSPECIFIED, FrequencyOptions_DAILY, FrequencyOptions_WEEKLY
    
    
    const (
    	// Unspecified.
    	FrequencyOptions_FREQUENCY_UNSPECIFIED FrequencyOptions_Frequency = 0
    	// Report will be generated daily.
    	FrequencyOptions_DAILY FrequencyOptions_Frequency = 1
    	// Report will be generated weekly.
    	FrequencyOptions_WEEKLY FrequencyOptions_Frequency = 2
    )

### func (FrequencyOptions_Frequency) Descriptor 
    
    
    func (FrequencyOptions_Frequency) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (FrequencyOptions_Frequency) Enum 
    
    
    func (x FrequencyOptions_Frequency) Enum() *FrequencyOptions_Frequency

### func (FrequencyOptions_Frequency) EnumDescriptor 
    
    
    func (FrequencyOptions_Frequency) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FrequencyOptions_Frequency.Descriptor instead.

### func (FrequencyOptions_Frequency) Number 
    
    
    func (x FrequencyOptions_Frequency) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (FrequencyOptions_Frequency) String 
    
    
    func (x FrequencyOptions_Frequency) String() [string](https://pkg.go.dev/builtin#string)

### func (FrequencyOptions_Frequency) Type 
    
    
    func (FrequencyOptions_Frequency) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GetDatasetConfigRequest
    
    
    type GetDatasetConfigRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`GetDatasetConfig`][google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig]

### func (*GetDatasetConfigRequest) Descriptor 
    
    
    func (*GetDatasetConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetDatasetConfigRequest.ProtoReflect.Descriptor instead.

### func (*GetDatasetConfigRequest) GetName 
    
    
    func (x *GetDatasetConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetDatasetConfigRequest) ProtoMessage 
    
    
    func (*GetDatasetConfigRequest) ProtoMessage()

### func (*GetDatasetConfigRequest) ProtoReflect 
    
    
    func (x *GetDatasetConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetDatasetConfigRequest) Reset 
    
    
    func (x *GetDatasetConfigRequest) Reset()

### func (*GetDatasetConfigRequest) String 
    
    
    func (x *GetDatasetConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetReportConfigRequest
    
    
    type GetReportConfigRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a ReportConfig

### func (*GetReportConfigRequest) Descriptor 
    
    
    func (*GetReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*GetReportConfigRequest) GetName 
    
    
    func (x *GetReportConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetReportConfigRequest) ProtoMessage 
    
    
    func (*GetReportConfigRequest) ProtoMessage()

### func (*GetReportConfigRequest) ProtoReflect 
    
    
    func (x *GetReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetReportConfigRequest) Reset 
    
    
    func (x *GetReportConfigRequest) Reset()

### func (*GetReportConfigRequest) String 
    
    
    func (x *GetReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetReportDetailRequest
    
    
    type GetReportDetailRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a ReportDetail

### func (*GetReportDetailRequest) Descriptor 
    
    
    func (*GetReportDetailRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetReportDetailRequest.ProtoReflect.Descriptor instead.

### func (*GetReportDetailRequest) GetName 
    
    
    func (x *GetReportDetailRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetReportDetailRequest) ProtoMessage 
    
    
    func (*GetReportDetailRequest) ProtoMessage()

### func (*GetReportDetailRequest) ProtoReflect 
    
    
    func (x *GetReportDetailRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetReportDetailRequest) Reset 
    
    
    func (x *GetReportDetailRequest) Reset()

### func (*GetReportDetailRequest) String 
    
    
    func (x *GetReportDetailRequest) String() [string](https://pkg.go.dev/builtin#string)

## Identity
    
    
    type Identity struct {
    
    	// Output only. Name of the identity.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Type of identity to use for the datasetConfig.
    	Type Identity_IdentityType `protobuf:"varint,2,opt,name=type,proto3,enum=google.cloud.storageinsights.v1.Identity_IdentityType" json:"type,omitempty"`
    	// contains filtered or unexported fields
    }

Identity lets the user provide the type of identity to use, and outputs the identity string that can be used for IAM policy changes.

### func (*Identity) Descriptor 
    
    
    func (*Identity) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Identity.ProtoReflect.Descriptor instead.

### func (*Identity) GetName 
    
    
    func (x *Identity) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Identity) GetType 
    
    
    func (x *Identity) GetType() Identity_IdentityType

### func (*Identity) ProtoMessage 
    
    
    func (*Identity) ProtoMessage()

### func (*Identity) ProtoReflect 
    
    
    func (x *Identity) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Identity) Reset 
    
    
    func (x *Identity) Reset()

### func (*Identity) String 
    
    
    func (x *Identity) String() [string](https://pkg.go.dev/builtin#string)

## Identity_IdentityType
    
    
    type Identity_IdentityType [int32](https://pkg.go.dev/builtin#int32)

Type of service account to use for the dataset configuration.

### Identity_IDENTITY_TYPE_UNSPECIFIED, Identity_IDENTITY_TYPE_PER_CONFIG, Identity_IDENTITY_TYPE_PER_PROJECT
    
    
    const (
    	// Default is unspecified and should not be used.
    	Identity_IDENTITY_TYPE_UNSPECIFIED Identity_IdentityType = 0
    	// Google managed service account per resource.
    	Identity_IDENTITY_TYPE_PER_CONFIG Identity_IdentityType = 1
    	// Google managed service account per project.
    	Identity_IDENTITY_TYPE_PER_PROJECT Identity_IdentityType = 2
    )

### func (Identity_IdentityType) Descriptor 
    
    
    func (Identity_IdentityType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Identity_IdentityType) Enum 
    
    
    func (x Identity_IdentityType) Enum() *Identity_IdentityType

### func (Identity_IdentityType) EnumDescriptor 
    
    
    func (Identity_IdentityType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Identity_IdentityType.Descriptor instead.

### func (Identity_IdentityType) Number 
    
    
    func (x Identity_IdentityType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Identity_IdentityType) String 
    
    
    func (x Identity_IdentityType) String() [string](https://pkg.go.dev/builtin#string)

### func (Identity_IdentityType) Type 
    
    
    func (Identity_IdentityType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## LinkDatasetRequest
    
    
    type LinkDatasetRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`LinkDataset`][google.cloud.storageinsights.v1.StorageInsights.LinkDataset]

### func (*LinkDatasetRequest) Descriptor 
    
    
    func (*LinkDatasetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkDatasetRequest.ProtoReflect.Descriptor instead.

### func (*LinkDatasetRequest) GetName 
    
    
    func (x *LinkDatasetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*LinkDatasetRequest) ProtoMessage 
    
    
    func (*LinkDatasetRequest) ProtoMessage()

### func (*LinkDatasetRequest) ProtoReflect 
    
    
    func (x *LinkDatasetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkDatasetRequest) Reset 
    
    
    func (x *LinkDatasetRequest) Reset()

### func (*LinkDatasetRequest) String 
    
    
    func (x *LinkDatasetRequest) String() [string](https://pkg.go.dev/builtin#string)

## LinkDatasetResponse
    
    
    type LinkDatasetResponse struct {
    	// contains filtered or unexported fields
    }

Response message for [`LinkDataset`][google.cloud.storageinsights.v1.StorageInsights.LinkDataset]

### func (*LinkDatasetResponse) Descriptor 
    
    
    func (*LinkDatasetResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LinkDatasetResponse.ProtoReflect.Descriptor instead.

### func (*LinkDatasetResponse) ProtoMessage 
    
    
    func (*LinkDatasetResponse) ProtoMessage()

### func (*LinkDatasetResponse) ProtoReflect 
    
    
    func (x *LinkDatasetResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LinkDatasetResponse) Reset 
    
    
    func (x *LinkDatasetResponse) Reset()

### func (*LinkDatasetResponse) String 
    
    
    func (x *LinkDatasetResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListDatasetConfigsRequest
    
    
    type ListDatasetConfigsRequest struct {
    
    	// Required. Parent value for ListDatasetConfigsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server might return fewer items than requested.
    	// If unspecified, server picks an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`ListDatasetConfigs`][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]

### func (*ListDatasetConfigsRequest) Descriptor 
    
    
    func (*ListDatasetConfigsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDatasetConfigsRequest.ProtoReflect.Descriptor instead.

### func (*ListDatasetConfigsRequest) GetFilter 
    
    
    func (x *ListDatasetConfigsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsRequest) GetOrderBy 
    
    
    func (x *ListDatasetConfigsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsRequest) GetPageSize 
    
    
    func (x *ListDatasetConfigsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListDatasetConfigsRequest) GetPageToken 
    
    
    func (x *ListDatasetConfigsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsRequest) GetParent 
    
    
    func (x *ListDatasetConfigsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsRequest) ProtoMessage 
    
    
    func (*ListDatasetConfigsRequest) ProtoMessage()

### func (*ListDatasetConfigsRequest) ProtoReflect 
    
    
    func (x *ListDatasetConfigsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDatasetConfigsRequest) Reset 
    
    
    func (x *ListDatasetConfigsRequest) Reset()

### func (*ListDatasetConfigsRequest) String 
    
    
    func (x *ListDatasetConfigsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListDatasetConfigsResponse
    
    
    type ListDatasetConfigsResponse struct {
    
    	// The list of `DatasetConfigs`
    	DatasetConfigs []*DatasetConfig `protobuf:"bytes,1,rep,name=dataset_configs,json=datasetConfigs,proto3" json:"dataset_configs,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for [`ListDatasetConfigs`][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]

### func (*ListDatasetConfigsResponse) Descriptor 
    
    
    func (*ListDatasetConfigsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDatasetConfigsResponse.ProtoReflect.Descriptor instead.

### func (*ListDatasetConfigsResponse) GetDatasetConfigs 
    
    
    func (x *ListDatasetConfigsResponse) GetDatasetConfigs() []*DatasetConfig

### func (*ListDatasetConfigsResponse) GetNextPageToken 
    
    
    func (x *ListDatasetConfigsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsResponse) GetUnreachable 
    
    
    func (x *ListDatasetConfigsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListDatasetConfigsResponse) ProtoMessage 
    
    
    func (*ListDatasetConfigsResponse) ProtoMessage()

### func (*ListDatasetConfigsResponse) ProtoReflect 
    
    
    func (x *ListDatasetConfigsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDatasetConfigsResponse) Reset 
    
    
    func (x *ListDatasetConfigsResponse) Reset()

### func (*ListDatasetConfigsResponse) String 
    
    
    func (x *ListDatasetConfigsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReportConfigsRequest
    
    
    type ListReportConfigsRequest struct {
    
    	// Required. Parent value for ListReportConfigsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`ListReportConfigs`][google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs]

### func (*ListReportConfigsRequest) Descriptor 
    
    
    func (*ListReportConfigsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportConfigsRequest.ProtoReflect.Descriptor instead.

### func (*ListReportConfigsRequest) GetFilter 
    
    
    func (x *ListReportConfigsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetOrderBy 
    
    
    func (x *ListReportConfigsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetPageSize 
    
    
    func (x *ListReportConfigsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReportConfigsRequest) GetPageToken 
    
    
    func (x *ListReportConfigsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetParent 
    
    
    func (x *ListReportConfigsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) ProtoMessage 
    
    
    func (*ListReportConfigsRequest) ProtoMessage()

### func (*ListReportConfigsRequest) ProtoReflect 
    
    
    func (x *ListReportConfigsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportConfigsRequest) Reset 
    
    
    func (x *ListReportConfigsRequest) Reset()

### func (*ListReportConfigsRequest) String 
    
    
    func (x *ListReportConfigsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReportConfigsResponse
    
    
    type ListReportConfigsResponse struct {
    
    	// The list of ReportConfig
    	ReportConfigs []*ReportConfig `protobuf:"bytes,1,rep,name=report_configs,json=reportConfigs,proto3" json:"report_configs,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing ReportConfigs

### func (*ListReportConfigsResponse) Descriptor 
    
    
    func (*ListReportConfigsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportConfigsResponse.ProtoReflect.Descriptor instead.

### func (*ListReportConfigsResponse) GetNextPageToken 
    
    
    func (x *ListReportConfigsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsResponse) GetReportConfigs 
    
    
    func (x *ListReportConfigsResponse) GetReportConfigs() []*ReportConfig

### func (*ListReportConfigsResponse) GetUnreachable 
    
    
    func (x *ListReportConfigsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsResponse) ProtoMessage 
    
    
    func (*ListReportConfigsResponse) ProtoMessage()

### func (*ListReportConfigsResponse) ProtoReflect 
    
    
    func (x *ListReportConfigsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportConfigsResponse) Reset 
    
    
    func (x *ListReportConfigsResponse) Reset()

### func (*ListReportConfigsResponse) String 
    
    
    func (x *ListReportConfigsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReportDetailsRequest
    
    
    type ListReportDetailsRequest struct {
    
    	// Required. Parent value for ListReportDetailsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of ReportDetails

### func (*ListReportDetailsRequest) Descriptor 
    
    
    func (*ListReportDetailsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportDetailsRequest.ProtoReflect.Descriptor instead.

### func (*ListReportDetailsRequest) GetFilter 
    
    
    func (x *ListReportDetailsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsRequest) GetOrderBy 
    
    
    func (x *ListReportDetailsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsRequest) GetPageSize 
    
    
    func (x *ListReportDetailsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReportDetailsRequest) GetPageToken 
    
    
    func (x *ListReportDetailsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsRequest) GetParent 
    
    
    func (x *ListReportDetailsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsRequest) ProtoMessage 
    
    
    func (*ListReportDetailsRequest) ProtoMessage()

### func (*ListReportDetailsRequest) ProtoReflect 
    
    
    func (x *ListReportDetailsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportDetailsRequest) Reset 
    
    
    func (x *ListReportDetailsRequest) Reset()

### func (*ListReportDetailsRequest) String 
    
    
    func (x *ListReportDetailsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReportDetailsResponse
    
    
    type ListReportDetailsResponse struct {
    
    	// The list of ReportDetail
    	ReportDetails []*ReportDetail `protobuf:"bytes,1,rep,name=report_details,json=reportDetails,proto3" json:"report_details,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing ReportDetails

### func (*ListReportDetailsResponse) Descriptor 
    
    
    func (*ListReportDetailsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportDetailsResponse.ProtoReflect.Descriptor instead.

### func (*ListReportDetailsResponse) GetNextPageToken 
    
    
    func (x *ListReportDetailsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsResponse) GetReportDetails 
    
    
    func (x *ListReportDetailsResponse) GetReportDetails() []*ReportDetail

### func (*ListReportDetailsResponse) GetUnreachable 
    
    
    func (x *ListReportDetailsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListReportDetailsResponse) ProtoMessage 
    
    
    func (*ListReportDetailsResponse) ProtoMessage()

### func (*ListReportDetailsResponse) ProtoReflect 
    
    
    func (x *ListReportDetailsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportDetailsResponse) Reset 
    
    
    func (x *ListReportDetailsResponse) Reset()

### func (*ListReportDetailsResponse) String 
    
    
    func (x *ListReportDetailsResponse) String() [string](https://pkg.go.dev/builtin#string)

## LocationMetadata
    
    
    type LocationMetadata struct {
    
    	// If true, `storageinsights.googleapis.com/ReportConfig` resource is
    	// available at the location.
    	ReportConfigAvailable [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=report_config_available,json=reportConfigAvailable,proto3" json:"report_config_available,omitempty"`
    	// If true, `storageinsights.googleapis.com/DatasetConfig` resource is
    	// available at the location.
    	DatasetConfigAvailable [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=dataset_config_available,json=datasetConfigAvailable,proto3" json:"dataset_config_available,omitempty"`
    	// contains filtered or unexported fields
    }

Metadata that helps discover which resources are available in a location.

### func (*LocationMetadata) Descriptor 
    
    
    func (*LocationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LocationMetadata.ProtoReflect.Descriptor instead.

### func (*LocationMetadata) GetDatasetConfigAvailable 
    
    
    func (x *LocationMetadata) GetDatasetConfigAvailable() [bool](https://pkg.go.dev/builtin#bool)

### func (*LocationMetadata) GetReportConfigAvailable 
    
    
    func (x *LocationMetadata) GetReportConfigAvailable() [bool](https://pkg.go.dev/builtin#bool)

### func (*LocationMetadata) ProtoMessage 
    
    
    func (*LocationMetadata) ProtoMessage()

### func (*LocationMetadata) ProtoReflect 
    
    
    func (x *LocationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LocationMetadata) Reset 
    
    
    func (x *LocationMetadata) Reset()

### func (*LocationMetadata) String 
    
    
    func (x *LocationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## ObjectMetadataReportOptions
    
    
    type ObjectMetadataReportOptions struct {
    
    	// Metadata fields to be included in the report.
    	MetadataFields [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=metadata_fields,json=metadataFields,proto3" json:"metadata_fields,omitempty"`
    	// Filter options for storage systems.
    	//
    	// Types that are valid to be assigned to Filter:
    	//
    	//	*ObjectMetadataReportOptions_StorageFilters
    	Filter isObjectMetadataReportOptions_Filter `protobuf_oneof:"filter"`
    	// Options on destination for storage systems.
    	//
    	// Types that are valid to be assigned to DestinationOptions:
    	//
    	//	*ObjectMetadataReportOptions_StorageDestinationOptions
    	DestinationOptions isObjectMetadataReportOptions_DestinationOptions `protobuf_oneof:"destination_options"`
    	// contains filtered or unexported fields
    }

Report specification for exporting object metadata. Next ID: 4

### func (*ObjectMetadataReportOptions) Descriptor 
    
    
    func (*ObjectMetadataReportOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ObjectMetadataReportOptions.ProtoReflect.Descriptor instead.

### func (*ObjectMetadataReportOptions) GetDestinationOptions 
    
    
    func (x *ObjectMetadataReportOptions) GetDestinationOptions() isObjectMetadataReportOptions_DestinationOptions

### func (*ObjectMetadataReportOptions) GetFilter 
    
    
    func (x *ObjectMetadataReportOptions) GetFilter() isObjectMetadataReportOptions_Filter

### func (*ObjectMetadataReportOptions) GetMetadataFields 
    
    
    func (x *ObjectMetadataReportOptions) GetMetadataFields() [][string](https://pkg.go.dev/builtin#string)

### func (*ObjectMetadataReportOptions) GetStorageDestinationOptions 
    
    
    func (x *ObjectMetadataReportOptions) GetStorageDestinationOptions() *CloudStorageDestinationOptions

### func (*ObjectMetadataReportOptions) GetStorageFilters 
    
    
    func (x *ObjectMetadataReportOptions) GetStorageFilters() *CloudStorageFilters

### func (*ObjectMetadataReportOptions) ProtoMessage 
    
    
    func (*ObjectMetadataReportOptions) ProtoMessage()

### func (*ObjectMetadataReportOptions) ProtoReflect 
    
    
    func (x *ObjectMetadataReportOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ObjectMetadataReportOptions) Reset 
    
    
    func (x *ObjectMetadataReportOptions) Reset()

### func (*ObjectMetadataReportOptions) String 
    
    
    func (x *ObjectMetadataReportOptions) String() [string](https://pkg.go.dev/builtin#string)

## ObjectMetadataReportOptions_StorageDestinationOptions
    
    
    type ObjectMetadataReportOptions_StorageDestinationOptions struct {
    	// Cloud Storage as the storage system.
    	StorageDestinationOptions *CloudStorageDestinationOptions `protobuf:"bytes,3,opt,name=storage_destination_options,json=storageDestinationOptions,proto3,oneof"`
    }

## ObjectMetadataReportOptions_StorageFilters
    
    
    type ObjectMetadataReportOptions_StorageFilters struct {
    	// Cloud Storage as the storage system.
    	StorageFilters *CloudStorageFilters `protobuf:"bytes,2,opt,name=storage_filters,json=storageFilters,proto3,oneof"`
    }

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

Represents the metadata of the long-running operation.

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

## ParquetOptions
    
    
    type ParquetOptions struct {
    	// contains filtered or unexported fields
    }

Options to configure Parquet formatted reports.

### func (*ParquetOptions) Descriptor 
    
    
    func (*ParquetOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ParquetOptions.ProtoReflect.Descriptor instead.

### func (*ParquetOptions) ProtoMessage 
    
    
    func (*ParquetOptions) ProtoMessage()

### func (*ParquetOptions) ProtoReflect 
    
    
    func (x *ParquetOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ParquetOptions) Reset 
    
    
    func (x *ParquetOptions) Reset()

### func (*ParquetOptions) String 
    
    
    func (x *ParquetOptions) String() [string](https://pkg.go.dev/builtin#string)

## ReportConfig
    
    
    type ReportConfig struct {
    
    	// name of resource. It will be of form
    	// projects/

Message describing ReportConfig object. ReportConfig is the configuration to generate reports. See <https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest> for more details on how to set various fields. Next ID: 12

### func (*ReportConfig) Descriptor 
    
    
    func (*ReportConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportConfig.ProtoReflect.Descriptor instead.

### func (*ReportConfig) GetCreateTime 
    
    
    func (x *ReportConfig) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ReportConfig) GetCsvOptions 
    
    
    func (x *ReportConfig) GetCsvOptions() *CSVOptions

### func (*ReportConfig) GetDisplayName 
    
    
    func (x *ReportConfig) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetFrequencyOptions 
    
    
    func (x *ReportConfig) GetFrequencyOptions() *FrequencyOptions

### func (*ReportConfig) GetLabels 
    
    
    func (x *ReportConfig) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetName 
    
    
    func (x *ReportConfig) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetObjectMetadataReportOptions 
    
    
    func (x *ReportConfig) GetObjectMetadataReportOptions() *ObjectMetadataReportOptions

### func (*ReportConfig) GetParquetOptions 
    
    
    func (x *ReportConfig) GetParquetOptions() *ParquetOptions

### func (*ReportConfig) GetReportFormat 
    
    
    func (x *ReportConfig) GetReportFormat() isReportConfig_ReportFormat

### func (*ReportConfig) GetReportKind 
    
    
    func (x *ReportConfig) GetReportKind() isReportConfig_ReportKind

### func (*ReportConfig) GetUpdateTime 
    
    
    func (x *ReportConfig) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ReportConfig) ProtoMessage 
    
    
    func (*ReportConfig) ProtoMessage()

### func (*ReportConfig) ProtoReflect 
    
    
    func (x *ReportConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportConfig) Reset 
    
    
    func (x *ReportConfig) Reset()

### func (*ReportConfig) String 
    
    
    func (x *ReportConfig) String() [string](https://pkg.go.dev/builtin#string)

## ReportConfig_CsvOptions
    
    
    type ReportConfig_CsvOptions struct {
    	// Options for CSV formatted reports.
    	CsvOptions *CSVOptions `protobuf:"bytes,6,opt,name=csv_options,json=csvOptions,proto3,oneof"`
    }

## ReportConfig_ObjectMetadataReportOptions
    
    
    type ReportConfig_ObjectMetadataReportOptions struct {
    	// Report for exporting object metadata.
    	ObjectMetadataReportOptions *ObjectMetadataReportOptions `protobuf:"bytes,8,opt,name=object_metadata_report_options,json=objectMetadataReportOptions,proto3,oneof"`
    }

## ReportConfig_ParquetOptions
    
    
    type ReportConfig_ParquetOptions struct {
    	// Options for Parquet formatted reports.
    	ParquetOptions *ParquetOptions `protobuf:"bytes,7,opt,name=parquet_options,json=parquetOptions,proto3,oneof"`
    }

## ReportDetail
    
    
    type ReportDetail struct {
    
    	// Name of resource. It will be of form
    	// projects/

Message describing ReportDetail object. ReportDetail represents metadata of generated reports for a ReportConfig. Next ID: 10

### func (*ReportDetail) Descriptor 
    
    
    func (*ReportDetail) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportDetail.ProtoReflect.Descriptor instead.

### func (*ReportDetail) GetLabels 
    
    
    func (x *ReportDetail) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*ReportDetail) GetName 
    
    
    func (x *ReportDetail) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportDetail) GetReportMetrics 
    
    
    func (x *ReportDetail) GetReportMetrics() *ReportDetail_Metrics

### func (*ReportDetail) GetReportPathPrefix 
    
    
    func (x *ReportDetail) GetReportPathPrefix() [string](https://pkg.go.dev/builtin#string)

### func (*ReportDetail) GetShardsCount 
    
    
    func (x *ReportDetail) GetShardsCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportDetail) GetSnapshotTime 
    
    
    func (x *ReportDetail) GetSnapshotTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ReportDetail) GetStatus 
    
    
    func (x *ReportDetail) GetStatus() *[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*ReportDetail) GetTargetDatetime 
    
    
    func (x *ReportDetail) GetTargetDatetime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*ReportDetail) ProtoMessage 
    
    
    func (*ReportDetail) ProtoMessage()

### func (*ReportDetail) ProtoReflect 
    
    
    func (x *ReportDetail) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportDetail) Reset 
    
    
    func (x *ReportDetail) Reset()

### func (*ReportDetail) String 
    
    
    func (x *ReportDetail) String() [string](https://pkg.go.dev/builtin#string)

## ReportDetail_Metrics
    
    
    type ReportDetail_Metrics struct {
    
    	// Count of Cloud Storage objects which are part of the report.
    	ProcessedRecordsCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=processed_records_count,json=processedRecordsCount,proto3" json:"processed_records_count,omitempty"`
    	// contains filtered or unexported fields
    }

Different metrics associated with the generated report.

### func (*ReportDetail_Metrics) Descriptor 
    
    
    func (*ReportDetail_Metrics) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportDetail_Metrics.ProtoReflect.Descriptor instead.

### func (*ReportDetail_Metrics) GetProcessedRecordsCount 
    
    
    func (x *ReportDetail_Metrics) GetProcessedRecordsCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportDetail_Metrics) ProtoMessage 
    
    
    func (*ReportDetail_Metrics) ProtoMessage()

### func (*ReportDetail_Metrics) ProtoReflect 
    
    
    func (x *ReportDetail_Metrics) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportDetail_Metrics) Reset 
    
    
    func (x *ReportDetail_Metrics) Reset()

### func (*ReportDetail_Metrics) String 
    
    
    func (x *ReportDetail_Metrics) String() [string](https://pkg.go.dev/builtin#string)

## StorageInsightsClient
    
    
    type StorageInsightsClient interface {
    	// Lists ReportConfigs in a given project and location.
    	ListReportConfigs(ctx context.Context, in *ListReportConfigsRequest, opts ...grpc.CallOption) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportConfig.
    	GetReportConfig(ctx context.Context, in *GetReportConfigRequest, opts ...grpc.CallOption) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new ReportConfig in a given project and location.
    	CreateReportConfig(ctx context.Context, in *CreateReportConfigRequest, opts ...grpc.CallOption) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single ReportConfig.
    	UpdateReportConfig(ctx context.Context, in *UpdateReportConfigRequest, opts ...grpc.CallOption) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single ReportConfig.
    	DeleteReportConfig(ctx context.Context, in *DeleteReportConfigRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists ReportDetails in a given project and location.
    	ListReportDetails(ctx context.Context, in *ListReportDetailsRequest, opts ...grpc.CallOption) (*ListReportDetailsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportDetail.
    	GetReportDetail(ctx context.Context, in *GetReportDetailRequest, opts ...grpc.CallOption) (*ReportDetail, [error](https://pkg.go.dev/builtin#error))
    	// Lists the dataset configurations in a given project for a given location.
    	ListDatasetConfigs(ctx context.Context, in *ListDatasetConfigsRequest, opts ...grpc.CallOption) (*ListDatasetConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the dataset configuration in a given project for a given location.
    	GetDatasetConfig(ctx context.Context, in *GetDatasetConfigRequest, opts ...grpc.CallOption) (*DatasetConfig, [error](https://pkg.go.dev/builtin#error))
    	// Creates a dataset configuration in a given project for a given location.
    	CreateDatasetConfig(ctx context.Context, in *CreateDatasetConfigRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates a dataset configuration in a given project for a given location.
    	UpdateDatasetConfig(ctx context.Context, in *UpdateDatasetConfigRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a dataset configuration in a given project for a given location.
    	DeleteDatasetConfig(ctx context.Context, in *DeleteDatasetConfigRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Links a dataset to BigQuery in a given project for a given location.
    	LinkDataset(ctx context.Context, in *LinkDatasetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Unlinks a dataset from BigQuery in a given project
    	// for a given location.
    	UnlinkDataset(ctx context.Context, in *UnlinkDatasetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

StorageInsightsClient is the client API for StorageInsights service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewStorageInsightsClient 
    
    
    func NewStorageInsightsClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) StorageInsightsClient

## StorageInsightsServer
    
    
    type StorageInsightsServer interface {
    	// Lists ReportConfigs in a given project and location.
    	ListReportConfigs(context.Context, *ListReportConfigsRequest) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportConfig.
    	GetReportConfig(context.Context, *GetReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new ReportConfig in a given project and location.
    	CreateReportConfig(context.Context, *CreateReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a single ReportConfig.
    	UpdateReportConfig(context.Context, *UpdateReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a single ReportConfig.
    	DeleteReportConfig(context.Context, *DeleteReportConfigRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Lists ReportDetails in a given project and location.
    	ListReportDetails(context.Context, *ListReportDetailsRequest) (*ListReportDetailsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportDetail.
    	GetReportDetail(context.Context, *GetReportDetailRequest) (*ReportDetail, [error](https://pkg.go.dev/builtin#error))
    	// Lists the dataset configurations in a given project for a given location.
    	ListDatasetConfigs(context.Context, *ListDatasetConfigsRequest) (*ListDatasetConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the dataset configuration in a given project for a given location.
    	GetDatasetConfig(context.Context, *GetDatasetConfigRequest) (*DatasetConfig, [error](https://pkg.go.dev/builtin#error))
    	// Creates a dataset configuration in a given project for a given location.
    	CreateDatasetConfig(context.Context, *CreateDatasetConfigRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates a dataset configuration in a given project for a given location.
    	UpdateDatasetConfig(context.Context, *UpdateDatasetConfigRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a dataset configuration in a given project for a given location.
    	DeleteDatasetConfig(context.Context, *DeleteDatasetConfigRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Links a dataset to BigQuery in a given project for a given location.
    	LinkDataset(context.Context, *LinkDatasetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Unlinks a dataset from BigQuery in a given project
    	// for a given location.
    	UnlinkDataset(context.Context, *UnlinkDatasetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

StorageInsightsServer is the server API for StorageInsights service. All implementations should embed UnimplementedStorageInsightsServer for forward compatibility

## UnimplementedStorageInsightsServer
    
    
    type UnimplementedStorageInsightsServer struct {
    }

UnimplementedStorageInsightsServer should be embedded to have forward compatible implementations.

### func (UnimplementedStorageInsightsServer) CreateDatasetConfig 
    
    
    func (UnimplementedStorageInsightsServer) CreateDatasetConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateDatasetConfigRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) CreateReportConfig 
    
    
    func (UnimplementedStorageInsightsServer) CreateReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) DeleteDatasetConfig 
    
    
    func (UnimplementedStorageInsightsServer) DeleteDatasetConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteDatasetConfigRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) DeleteReportConfig 
    
    
    func (UnimplementedStorageInsightsServer) DeleteReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteReportConfigRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) GetDatasetConfig 
    
    
    func (UnimplementedStorageInsightsServer) GetDatasetConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetDatasetConfigRequest) (*DatasetConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) GetReportConfig 
    
    
    func (UnimplementedStorageInsightsServer) GetReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) GetReportDetail 
    
    
    func (UnimplementedStorageInsightsServer) GetReportDetail([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetReportDetailRequest) (*ReportDetail, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) LinkDataset 
    
    
    func (UnimplementedStorageInsightsServer) LinkDataset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *LinkDatasetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) ListDatasetConfigs 
    
    
    func (UnimplementedStorageInsightsServer) ListDatasetConfigs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListDatasetConfigsRequest) (*ListDatasetConfigsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) ListReportConfigs 
    
    
    func (UnimplementedStorageInsightsServer) ListReportConfigs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReportConfigsRequest) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) ListReportDetails 
    
    
    func (UnimplementedStorageInsightsServer) ListReportDetails([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReportDetailsRequest) (*ListReportDetailsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) UnlinkDataset 
    
    
    func (UnimplementedStorageInsightsServer) UnlinkDataset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UnlinkDatasetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) UpdateDatasetConfig 
    
    
    func (UnimplementedStorageInsightsServer) UpdateDatasetConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateDatasetConfigRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStorageInsightsServer) UpdateReportConfig 
    
    
    func (UnimplementedStorageInsightsServer) UpdateReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))

## UnlinkDatasetRequest
    
    
    type UnlinkDatasetRequest struct {
    
    	// Required. Name of the resource
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`UnlinkDataset`][google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset]

### func (*UnlinkDatasetRequest) Descriptor 
    
    
    func (*UnlinkDatasetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UnlinkDatasetRequest.ProtoReflect.Descriptor instead.

### func (*UnlinkDatasetRequest) GetName 
    
    
    func (x *UnlinkDatasetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*UnlinkDatasetRequest) ProtoMessage 
    
    
    func (*UnlinkDatasetRequest) ProtoMessage()

### func (*UnlinkDatasetRequest) ProtoReflect 
    
    
    func (x *UnlinkDatasetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UnlinkDatasetRequest) Reset 
    
    
    func (x *UnlinkDatasetRequest) Reset()

### func (*UnlinkDatasetRequest) String 
    
    
    func (x *UnlinkDatasetRequest) String() [string](https://pkg.go.dev/builtin#string)

## UnsafeStorageInsightsServer
    
    
    type UnsafeStorageInsightsServer interface {
    	// contains filtered or unexported methods
    }

UnsafeStorageInsightsServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to StorageInsightsServer will result in compilation errors.

## UpdateDatasetConfigRequest
    
    
    type UpdateDatasetConfigRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `DatasetConfig` resource by the update.
    	// The fields specified in the `update_mask` are relative to the resource, not
    	// the full request. A field is overwritten if it is in the mask. If the
    	// user does not provide a mask then it returns an "Invalid Argument" error.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	DatasetConfig *DatasetConfig `protobuf:"bytes,2,opt,name=dataset_config,json=datasetConfig,proto3" json:"dataset_config,omitempty"`
    	// Optional. A unique identifier for your request.
    	// Specify the request ID if you need to retry the request.
    	// If you retry the request with the same ID within 60 minutes, the server
    	// ignores the request if it has already completed the original request.
    	//
    	// For example, if your initial request times out and you retry the request
    	// using the same request ID, the server recognizes the original request and
    	// does not process the new request.
    	//
    	// The request ID must be a valid UUID and cannot be a zero UUID
    	// (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for [`UpdateDatasetConfig`][google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig]

### func (*UpdateDatasetConfigRequest) Descriptor 
    
    
    func (*UpdateDatasetConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateDatasetConfigRequest.ProtoReflect.Descriptor instead.

### func (*UpdateDatasetConfigRequest) GetDatasetConfig 
    
    
    func (x *UpdateDatasetConfigRequest) GetDatasetConfig() *DatasetConfig

### func (*UpdateDatasetConfigRequest) GetRequestId 
    
    
    func (x *UpdateDatasetConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateDatasetConfigRequest) GetUpdateMask 
    
    
    func (x *UpdateDatasetConfigRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateDatasetConfigRequest) ProtoMessage 
    
    
    func (*UpdateDatasetConfigRequest) ProtoMessage()

### func (*UpdateDatasetConfigRequest) ProtoReflect 
    
    
    func (x *UpdateDatasetConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateDatasetConfigRequest) Reset 
    
    
    func (x *UpdateDatasetConfigRequest) Reset()

### func (*UpdateDatasetConfigRequest) String 
    
    
    func (x *UpdateDatasetConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateReportConfigRequest
    
    
    type UpdateReportConfigRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// ReportConfig resource by the update.
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask. If the
    	// user does not provide a mask then all fields will be overwritten.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	ReportConfig *ReportConfig `protobuf:"bytes,2,opt,name=report_config,json=reportConfig,proto3" json:"report_config,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for updating a ReportConfig

### func (*UpdateReportConfigRequest) Descriptor 
    
    
    func (*UpdateReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*UpdateReportConfigRequest) GetReportConfig 
    
    
    func (x *UpdateReportConfigRequest) GetReportConfig() *ReportConfig

### func (*UpdateReportConfigRequest) GetRequestId 
    
    
    func (x *UpdateReportConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateReportConfigRequest) GetUpdateMask 
    
    
    func (x *UpdateReportConfigRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateReportConfigRequest) ProtoMessage 
    
    
    func (*UpdateReportConfigRequest) ProtoMessage()

### func (*UpdateReportConfigRequest) ProtoReflect 
    
    
    func (x *UpdateReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateReportConfigRequest) Reset 
    
    
    func (x *UpdateReportConfigRequest) Reset()

### func (*UpdateReportConfigRequest) String 
    
    
    func (x *UpdateReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
