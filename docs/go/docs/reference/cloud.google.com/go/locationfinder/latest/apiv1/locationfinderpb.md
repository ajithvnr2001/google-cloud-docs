---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/locationfinder/latest/apiv1/locationfinderpb/
title: Cloud Location Finder API v1 - Package cloud.google.com/go/locationfinder/apiv1/locationfinderpb (v1.1.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:00.288880+00:00
---

# Cloud Location Finder API v1 - Package cloud.google.com/go/locationfinder/apiv1/locationfinderpb (v1.1.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/locationfinder/latest/apiv1/locationfinderpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Location Finder API v1 - Package cloud.google.com/go/locationfinder/apiv1/locationfinderpb (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/locationfinder/apiv1/locationfinderpb). 

##  Constants 

### CloudLocationFinder_ListCloudLocations_FullMethodName, CloudLocationFinder_GetCloudLocation_FullMethodName, CloudLocationFinder_SearchCloudLocations_FullMethodName
    
    
    const (
    	CloudLocationFinder_ListCloudLocations_FullMethodName   = "/google.cloud.locationfinder.v1.CloudLocationFinder/ListCloudLocations"
    	CloudLocationFinder_GetCloudLocation_FullMethodName     = "/google.cloud.locationfinder.v1.CloudLocationFinder/GetCloudLocation"
    	CloudLocationFinder_SearchCloudLocations_FullMethodName = "/google.cloud.locationfinder.v1.CloudLocationFinder/SearchCloudLocations"
    )

## Variables 

### CloudLocation_CloudProvider_name, CloudLocation_CloudProvider_value
    
    
    var (
    	CloudLocation_CloudProvider_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CLOUD_PROVIDER_UNSPECIFIED",
    		1: "CLOUD_PROVIDER_GCP",
    		2: "CLOUD_PROVIDER_AWS",
    		3: "CLOUD_PROVIDER_AZURE",
    		4: "CLOUD_PROVIDER_OCI",
    	}
    	CloudLocation_CloudProvider_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CLOUD_PROVIDER_UNSPECIFIED": 0,
    		"CLOUD_PROVIDER_GCP":         1,
    		"CLOUD_PROVIDER_AWS":         2,
    		"CLOUD_PROVIDER_AZURE":       3,
    		"CLOUD_PROVIDER_OCI":         4,
    	}
    )

Enum value maps for CloudLocation_CloudProvider.

### CloudLocation_CloudLocationType_name, CloudLocation_CloudLocationType_value
    
    
    var (
    	CloudLocation_CloudLocationType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CLOUD_LOCATION_TYPE_UNSPECIFIED",
    		1: "CLOUD_LOCATION_TYPE_REGION",
    		2: "CLOUD_LOCATION_TYPE_ZONE",
    		3: "CLOUD_LOCATION_TYPE_REGION_EXTENSION",
    		4: "CLOUD_LOCATION_TYPE_GDCC_ZONE",
    	}
    	CloudLocation_CloudLocationType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CLOUD_LOCATION_TYPE_UNSPECIFIED":      0,
    		"CLOUD_LOCATION_TYPE_REGION":           1,
    		"CLOUD_LOCATION_TYPE_ZONE":             2,
    		"CLOUD_LOCATION_TYPE_REGION_EXTENSION": 3,
    		"CLOUD_LOCATION_TYPE_GDCC_ZONE":        4,
    	}
    )

Enum value maps for CloudLocation_CloudLocationType.

### CloudLocationFinder_ServiceDesc
    
    
    var CloudLocationFinder_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.locationfinder.v1.CloudLocationFinder",
    	HandlerType: (*CloudLocationFinderServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListCloudLocations",
    			Handler:    _CloudLocationFinder_ListCloudLocations_Handler,
    		},
    		{
    			MethodName: "GetCloudLocation",
    			Handler:    _CloudLocationFinder_GetCloudLocation_Handler,
    		},
    		{
    			MethodName: "SearchCloudLocations",
    			Handler:    _CloudLocationFinder_SearchCloudLocations_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/locationfinder/v1/service.proto",
    }

CloudLocationFinder_ServiceDesc is the grpc.ServiceDesc for CloudLocationFinder service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

### File_google_cloud_locationfinder_v1_cloud_location_proto
    
    
    var File_google_cloud_locationfinder_v1_cloud_location_proto protoreflect.FileDescriptor

### File_google_cloud_locationfinder_v1_service_proto
    
    
    var File_google_cloud_locationfinder_v1_service_proto protoreflect.FileDescriptor

## Functions 

### func RegisterCloudLocationFinderServer 
    
    
    func RegisterCloudLocationFinderServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv CloudLocationFinderServer)

## CloudLocation
    
    
    type CloudLocation struct {
    
    	// Identifier. Name of the cloud location. Unique name of the cloud location
    	// including project and location using the form:
    	// `projects/{project_id}/locations/{location}/cloudLocations/{cloud_location}`
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The containing cloud location in the strict nesting hierarchy.
    	// For example, the containing cloud location of a zone is a region.
    	ContainingCloudLocation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=containing_cloud_location,json=containingCloudLocation,proto3" json:"containing_cloud_location,omitempty"`
    	// Optional. The human-readable name of the cloud location. Example:
    	// us-east-2, us-east1.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Optional. The provider of the cloud location. Values can be Google Cloud or
    	// third-party providers, including AWS, Azure, or Oracle Cloud
    	// Infrastructure.
    	CloudProvider CloudLocation_CloudProvider `protobuf:"varint,4,opt,name=cloud_provider,json=cloudProvider,proto3,enum=google.cloud.locationfinder.v1.CloudLocation_CloudProvider" json:"cloud_provider,omitempty"`
    	// Optional. The two-letter ISO 3166-1 alpha-2 code of the cloud location.
    	// Examples: US, JP, KR.
    	TerritoryCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=territory_code,json=territoryCode,proto3" json:"territory_code,omitempty"`
    	// Optional. The type of the cloud location.
    	CloudLocationType CloudLocation_CloudLocationType `protobuf:"varint,6,opt,name=cloud_location_type,json=cloudLocationType,proto3,enum=google.cloud.locationfinder.v1.CloudLocation_CloudLocationType" json:"cloud_location_type,omitempty"`
    	// Optional. The carbon free energy percentage of the cloud location. This
    	// represents the average percentage of time customers' application will be
    	// running on carbon-free energy. See
    	// https://cloud.google.com/sustainability/region-carbon for more details.
    	// There is a difference between default value 0 and unset value. 0 means the
    	// carbon free energy percentage is 0%, while unset value means the carbon
    	// footprint data is not available.
    	CarbonFreeEnergyPercentage *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,7,opt,name=carbon_free_energy_percentage,json=carbonFreeEnergyPercentage,proto3,oneof" json:"carbon_free_energy_percentage,omitempty"`
    	// contains filtered or unexported fields
    }

Represents resource cloud locations.

### func (*CloudLocation) Descriptor 
    
    
    func (*CloudLocation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloudLocation.ProtoReflect.Descriptor instead.

### func (*CloudLocation) GetCarbonFreeEnergyPercentage 
    
    
    func (x *CloudLocation) GetCarbonFreeEnergyPercentage() [float32](https://pkg.go.dev/builtin#float32)

### func (*CloudLocation) GetCloudLocationType 
    
    
    func (x *CloudLocation) GetCloudLocationType() CloudLocation_CloudLocationType

### func (*CloudLocation) GetCloudProvider 
    
    
    func (x *CloudLocation) GetCloudProvider() CloudLocation_CloudProvider

### func (*CloudLocation) GetContainingCloudLocation 
    
    
    func (x *CloudLocation) GetContainingCloudLocation() [string](https://pkg.go.dev/builtin#string)

### func (*CloudLocation) GetDisplayName 
    
    
    func (x *CloudLocation) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*CloudLocation) GetName 
    
    
    func (x *CloudLocation) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*CloudLocation) GetTerritoryCode 
    
    
    func (x *CloudLocation) GetTerritoryCode() [string](https://pkg.go.dev/builtin#string)

### func (*CloudLocation) ProtoMessage 
    
    
    func (*CloudLocation) ProtoMessage()

### func (*CloudLocation) ProtoReflect 
    
    
    func (x *CloudLocation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CloudLocation) Reset 
    
    
    func (x *CloudLocation) Reset()

### func (*CloudLocation) String 
    
    
    func (x *CloudLocation) String() [string](https://pkg.go.dev/builtin#string)

## CloudLocationFinderClient
    
    
    type CloudLocationFinderClient interface {
    	// Lists cloud locations under a given project and location.
    	ListCloudLocations(ctx context.Context, in *ListCloudLocationsRequest, opts ...grpc.CallOption) (*ListCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves a resource containing information about a cloud location.
    	GetCloudLocation(ctx context.Context, in *GetCloudLocationRequest, opts ...grpc.CallOption) (*CloudLocation, [error](https://pkg.go.dev/builtin#error))
    	// Searches for cloud locations from a given source location.
    	SearchCloudLocations(ctx context.Context, in *SearchCloudLocationsRequest, opts ...grpc.CallOption) (*SearchCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CloudLocationFinderClient is the client API for CloudLocationFinder service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewCloudLocationFinderClient 
    
    
    func NewCloudLocationFinderClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) CloudLocationFinderClient

## CloudLocationFinderServer
    
    
    type CloudLocationFinderServer interface {
    	// Lists cloud locations under a given project and location.
    	ListCloudLocations(context.Context, *ListCloudLocationsRequest) (*ListCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Retrieves a resource containing information about a cloud location.
    	GetCloudLocation(context.Context, *GetCloudLocationRequest) (*CloudLocation, [error](https://pkg.go.dev/builtin#error))
    	// Searches for cloud locations from a given source location.
    	SearchCloudLocations(context.Context, *SearchCloudLocationsRequest) (*SearchCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))
    }

CloudLocationFinderServer is the server API for CloudLocationFinder service. All implementations should embed UnimplementedCloudLocationFinderServer for forward compatibility

## CloudLocation_CloudLocationType
    
    
    type CloudLocation_CloudLocationType [int32](https://pkg.go.dev/builtin#int32)

The type of the cloud location. This enum lists all possible categories of cloud locations.

### CloudLocation_CLOUD_LOCATION_TYPE_UNSPECIFIED, CloudLocation_CLOUD_LOCATION_TYPE_REGION, CloudLocation_CLOUD_LOCATION_TYPE_ZONE, CloudLocation_CLOUD_LOCATION_TYPE_REGION_EXTENSION, CloudLocation_CLOUD_LOCATION_TYPE_GDCC_ZONE
    
    
    const (
    	// Unspecified type.
    	CloudLocation_CLOUD_LOCATION_TYPE_UNSPECIFIED CloudLocation_CloudLocationType = 0
    	// CloudLocation type for region.
    	CloudLocation_CLOUD_LOCATION_TYPE_REGION CloudLocation_CloudLocationType = 1
    	// CloudLocation type for zone.
    	CloudLocation_CLOUD_LOCATION_TYPE_ZONE CloudLocation_CloudLocationType = 2
    	// CloudLocation type for region extension.
    	CloudLocation_CLOUD_LOCATION_TYPE_REGION_EXTENSION CloudLocation_CloudLocationType = 3
    	// CloudLocation type for Google Distributed Cloud Connected Zone.
    	CloudLocation_CLOUD_LOCATION_TYPE_GDCC_ZONE CloudLocation_CloudLocationType = 4
    )

### func (CloudLocation_CloudLocationType) Descriptor 
    
    
    func (CloudLocation_CloudLocationType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CloudLocation_CloudLocationType) Enum 
    
    
    func (x CloudLocation_CloudLocationType) Enum() *CloudLocation_CloudLocationType

### func (CloudLocation_CloudLocationType) EnumDescriptor 
    
    
    func (CloudLocation_CloudLocationType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloudLocation_CloudLocationType.Descriptor instead.

### func (CloudLocation_CloudLocationType) Number 
    
    
    func (x CloudLocation_CloudLocationType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CloudLocation_CloudLocationType) String 
    
    
    func (x CloudLocation_CloudLocationType) String() [string](https://pkg.go.dev/builtin#string)

### func (CloudLocation_CloudLocationType) Type 
    
    
    func (CloudLocation_CloudLocationType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## CloudLocation_CloudProvider
    
    
    type CloudLocation_CloudProvider [int32](https://pkg.go.dev/builtin#int32)

The type of the cloud provider. This enum lists all possible providers of cloud locations.

### CloudLocation_CLOUD_PROVIDER_UNSPECIFIED, CloudLocation_CLOUD_PROVIDER_GCP, CloudLocation_CLOUD_PROVIDER_AWS, CloudLocation_CLOUD_PROVIDER_AZURE, CloudLocation_CLOUD_PROVIDER_OCI
    
    
    const (
    	// Unspecified type.
    	CloudLocation_CLOUD_PROVIDER_UNSPECIFIED CloudLocation_CloudProvider = 0
    	// Cloud provider type for Google Cloud.
    	CloudLocation_CLOUD_PROVIDER_GCP CloudLocation_CloudProvider = 1
    	// Cloud provider type for AWS.
    	CloudLocation_CLOUD_PROVIDER_AWS CloudLocation_CloudProvider = 2
    	// Cloud provider type for Azure.
    	CloudLocation_CLOUD_PROVIDER_AZURE CloudLocation_CloudProvider = 3
    	// Cloud provider type for OCI.
    	CloudLocation_CLOUD_PROVIDER_OCI CloudLocation_CloudProvider = 4
    )

### func (CloudLocation_CloudProvider) Descriptor 
    
    
    func (CloudLocation_CloudProvider) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CloudLocation_CloudProvider) Enum 
    
    
    func (x CloudLocation_CloudProvider) Enum() *CloudLocation_CloudProvider

### func (CloudLocation_CloudProvider) EnumDescriptor 
    
    
    func (CloudLocation_CloudProvider) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CloudLocation_CloudProvider.Descriptor instead.

### func (CloudLocation_CloudProvider) Number 
    
    
    func (x CloudLocation_CloudProvider) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CloudLocation_CloudProvider) String 
    
    
    func (x CloudLocation_CloudProvider) String() [string](https://pkg.go.dev/builtin#string)

### func (CloudLocation_CloudProvider) Type 
    
    
    func (CloudLocation_CloudProvider) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GetCloudLocationRequest
    
    
    type GetCloudLocationRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a cloud location.

### func (*GetCloudLocationRequest) Descriptor 
    
    
    func (*GetCloudLocationRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCloudLocationRequest.ProtoReflect.Descriptor instead.

### func (*GetCloudLocationRequest) GetName 
    
    
    func (x *GetCloudLocationRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCloudLocationRequest) ProtoMessage 
    
    
    func (*GetCloudLocationRequest) ProtoMessage()

### func (*GetCloudLocationRequest) ProtoReflect 
    
    
    func (x *GetCloudLocationRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCloudLocationRequest) Reset 
    
    
    func (x *GetCloudLocationRequest) Reset()

### func (*GetCloudLocationRequest) String 
    
    
    func (x *GetCloudLocationRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCloudLocationsRequest
    
    
    type ListCloudLocationsRequest struct {
    
    	// Required. The parent, which owns this collection of cloud locations.
    	// Format: projects/{project}/locations/{location}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. The maximum number of cloud locations to return per page. The
    	// service might return fewer cloud locations than this value. If unspecified,
    	// server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	// Provide page token returned by a previous 'ListCloudLocations' call to
    	// retrieve the next page of results. When paginating, all other parameters
    	// provided to 'ListCloudLocations' must match the call that provided the page
    	// token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. A filter expression that filters resources listed in the
    	// response. The expression is in the form of field=value. For example,
    	// 'cloud_location_type=CLOUD_LOCATION_TYPE_REGION'. Multiple filter queries
    	// are space-separated. For example,
    	// 'cloud_location_type=CLOUD_LOCATION_TYPE_REGION territory_code="US"' By
    	// default, each expression is an AND expression. However, you can include AND
    	// and OR expressions explicitly.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting list of cloud locations..

### func (*ListCloudLocationsRequest) Descriptor 
    
    
    func (*ListCloudLocationsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCloudLocationsRequest.ProtoReflect.Descriptor instead.

### func (*ListCloudLocationsRequest) GetFilter 
    
    
    func (x *ListCloudLocationsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListCloudLocationsRequest) GetPageSize 
    
    
    func (x *ListCloudLocationsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListCloudLocationsRequest) GetPageToken 
    
    
    func (x *ListCloudLocationsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCloudLocationsRequest) GetParent 
    
    
    func (x *ListCloudLocationsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListCloudLocationsRequest) ProtoMessage 
    
    
    func (*ListCloudLocationsRequest) ProtoMessage()

### func (*ListCloudLocationsRequest) ProtoReflect 
    
    
    func (x *ListCloudLocationsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCloudLocationsRequest) Reset 
    
    
    func (x *ListCloudLocationsRequest) Reset()

### func (*ListCloudLocationsRequest) String 
    
    
    func (x *ListCloudLocationsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCloudLocationsResponse
    
    
    type ListCloudLocationsResponse struct {
    
    	// Output only. List of cloud locations.
    	CloudLocations []*CloudLocation `protobuf:"bytes,1,rep,name=cloud_locations,json=cloudLocations,proto3" json:"cloud_locations,omitempty"`
    	// Output only. The continuation token, used to page through large result
    	// sets. Provide this value in a subsequent request as page_token in
    	// subsequent requests to retrieve the next page. If this field is not
    	// present, there are no subsequent results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to listing cloud locations.

### func (*ListCloudLocationsResponse) Descriptor 
    
    
    func (*ListCloudLocationsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCloudLocationsResponse.ProtoReflect.Descriptor instead.

### func (*ListCloudLocationsResponse) GetCloudLocations 
    
    
    func (x *ListCloudLocationsResponse) GetCloudLocations() []*CloudLocation

### func (*ListCloudLocationsResponse) GetNextPageToken 
    
    
    func (x *ListCloudLocationsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCloudLocationsResponse) ProtoMessage 
    
    
    func (*ListCloudLocationsResponse) ProtoMessage()

### func (*ListCloudLocationsResponse) ProtoReflect 
    
    
    func (x *ListCloudLocationsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCloudLocationsResponse) Reset 
    
    
    func (x *ListCloudLocationsResponse) Reset()

### func (*ListCloudLocationsResponse) String 
    
    
    func (x *ListCloudLocationsResponse) String() [string](https://pkg.go.dev/builtin#string)

## SearchCloudLocationsRequest
    
    
    type SearchCloudLocationsRequest struct {
    
    	// Required. The parent, which owns this collection of cloud locations.
    	// Format: projects/{project}/locations/{location}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The source cloud location to search from.
    	// Example search can be searching nearby cloud locations from the source
    	// cloud location by latency.
    	SourceCloudLocation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=source_cloud_location,json=sourceCloudLocation,proto3" json:"source_cloud_location,omitempty"`
    	// Optional. The maximum number of cloud locations to return. The service
    	// might return fewer cloud locations than this value. If unspecified, server
    	// will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	// Provide Page token returned by a previous 'ListCloudLocations' call to
    	// retrieve the next page of results. When paginating, all other parameters
    	// provided to 'ListCloudLocations' must match the call that provided the page
    	// token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. The query string in search query syntax. While filter is used to
    	// filter the search results by attributes, query is used to specify the
    	// search requirements.
    	Query [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=query,proto3" json:"query,omitempty"`
    	// contains filtered or unexported fields
    }

Message for searching cloud locations from a given source location.

### func (*SearchCloudLocationsRequest) Descriptor 
    
    
    func (*SearchCloudLocationsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCloudLocationsRequest.ProtoReflect.Descriptor instead.

### func (*SearchCloudLocationsRequest) GetPageSize 
    
    
    func (x *SearchCloudLocationsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*SearchCloudLocationsRequest) GetPageToken 
    
    
    func (x *SearchCloudLocationsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCloudLocationsRequest) GetParent 
    
    
    func (x *SearchCloudLocationsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCloudLocationsRequest) GetQuery 
    
    
    func (x *SearchCloudLocationsRequest) GetQuery() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCloudLocationsRequest) GetSourceCloudLocation 
    
    
    func (x *SearchCloudLocationsRequest) GetSourceCloudLocation() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCloudLocationsRequest) ProtoMessage 
    
    
    func (*SearchCloudLocationsRequest) ProtoMessage()

### func (*SearchCloudLocationsRequest) ProtoReflect 
    
    
    func (x *SearchCloudLocationsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCloudLocationsRequest) Reset 
    
    
    func (x *SearchCloudLocationsRequest) Reset()

### func (*SearchCloudLocationsRequest) String 
    
    
    func (x *SearchCloudLocationsRequest) String() [string](https://pkg.go.dev/builtin#string)

## SearchCloudLocationsResponse
    
    
    type SearchCloudLocationsResponse struct {
    
    	// Output only. List of cloud locations.
    	CloudLocations []*CloudLocation `protobuf:"bytes,1,rep,name=cloud_locations,json=cloudLocations,proto3" json:"cloud_locations,omitempty"`
    	// Output only. The continuation token, used to page through large result
    	// sets. Provide this value in a subsequent request as page_token in
    	// subsequent requests to retrieve the next page. If this field is not
    	// present, there are no subsequent results.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Message for response to searching cloud locations.

### func (*SearchCloudLocationsResponse) Descriptor 
    
    
    func (*SearchCloudLocationsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SearchCloudLocationsResponse.ProtoReflect.Descriptor instead.

### func (*SearchCloudLocationsResponse) GetCloudLocations 
    
    
    func (x *SearchCloudLocationsResponse) GetCloudLocations() []*CloudLocation

### func (*SearchCloudLocationsResponse) GetNextPageToken 
    
    
    func (x *SearchCloudLocationsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*SearchCloudLocationsResponse) ProtoMessage 
    
    
    func (*SearchCloudLocationsResponse) ProtoMessage()

### func (*SearchCloudLocationsResponse) ProtoReflect 
    
    
    func (x *SearchCloudLocationsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SearchCloudLocationsResponse) Reset 
    
    
    func (x *SearchCloudLocationsResponse) Reset()

### func (*SearchCloudLocationsResponse) String 
    
    
    func (x *SearchCloudLocationsResponse) String() [string](https://pkg.go.dev/builtin#string)

## UnimplementedCloudLocationFinderServer
    
    
    type UnimplementedCloudLocationFinderServer struct {
    }

UnimplementedCloudLocationFinderServer should be embedded to have forward compatible implementations.

### func (UnimplementedCloudLocationFinderServer) GetCloudLocation 
    
    
    func (UnimplementedCloudLocationFinderServer) GetCloudLocation([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCloudLocationRequest) (*CloudLocation, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCloudLocationFinderServer) ListCloudLocations 
    
    
    func (UnimplementedCloudLocationFinderServer) ListCloudLocations([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListCloudLocationsRequest) (*ListCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedCloudLocationFinderServer) SearchCloudLocations 
    
    
    func (UnimplementedCloudLocationFinderServer) SearchCloudLocations([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *SearchCloudLocationsRequest) (*SearchCloudLocationsResponse, [error](https://pkg.go.dev/builtin#error))

## UnsafeCloudLocationFinderServer
    
    
    type UnsafeCloudLocationFinderServer interface {
    	// contains filtered or unexported methods
    }

UnsafeCloudLocationFinderServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to CloudLocationFinderServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
