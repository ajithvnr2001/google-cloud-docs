---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/streetview/latest/publish/apiv1/publishpb/
title: Street View Publish API v1 - Package cloud.google.com/go/streetview/publish/apiv1/publishpb (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:05.202735+00:00
---

# Street View Publish API v1 - Package cloud.google.com/go/streetview/publish/apiv1/publishpb (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/streetview/latest/publish/apiv1/publishpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Street View Publish API v1 - Package cloud.google.com/go/streetview/publish/apiv1/publishpb (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.5 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/streetview/publish/apiv1/publishpb). 

##  Constants 

### StreetViewPublishService_StartUpload_FullMethodName, StreetViewPublishService_CreatePhoto_FullMethodName, StreetViewPublishService_GetPhoto_FullMethodName, StreetViewPublishService_BatchGetPhotos_FullMethodName, StreetViewPublishService_ListPhotos_FullMethodName, StreetViewPublishService_UpdatePhoto_FullMethodName, StreetViewPublishService_BatchUpdatePhotos_FullMethodName, StreetViewPublishService_DeletePhoto_FullMethodName, StreetViewPublishService_BatchDeletePhotos_FullMethodName, StreetViewPublishService_StartPhotoSequenceUpload_FullMethodName, StreetViewPublishService_CreatePhotoSequence_FullMethodName, StreetViewPublishService_GetPhotoSequence_FullMethodName, StreetViewPublishService_ListPhotoSequences_FullMethodName, StreetViewPublishService_DeletePhotoSequence_FullMethodName
    
    
    const (
    	StreetViewPublishService_StartUpload_FullMethodName              = "/google.streetview.publish.v1.StreetViewPublishService/StartUpload"
    	StreetViewPublishService_CreatePhoto_FullMethodName              = "/google.streetview.publish.v1.StreetViewPublishService/CreatePhoto"
    	StreetViewPublishService_GetPhoto_FullMethodName                 = "/google.streetview.publish.v1.StreetViewPublishService/GetPhoto"
    	StreetViewPublishService_BatchGetPhotos_FullMethodName           = "/google.streetview.publish.v1.StreetViewPublishService/BatchGetPhotos"
    	StreetViewPublishService_ListPhotos_FullMethodName               = "/google.streetview.publish.v1.StreetViewPublishService/ListPhotos"
    	StreetViewPublishService_UpdatePhoto_FullMethodName              = "/google.streetview.publish.v1.StreetViewPublishService/UpdatePhoto"
    	StreetViewPublishService_BatchUpdatePhotos_FullMethodName        = "/google.streetview.publish.v1.StreetViewPublishService/BatchUpdatePhotos"
    	StreetViewPublishService_DeletePhoto_FullMethodName              = "/google.streetview.publish.v1.StreetViewPublishService/DeletePhoto"
    	StreetViewPublishService_BatchDeletePhotos_FullMethodName        = "/google.streetview.publish.v1.StreetViewPublishService/BatchDeletePhotos"
    	StreetViewPublishService_StartPhotoSequenceUpload_FullMethodName = "/google.streetview.publish.v1.StreetViewPublishService/StartPhotoSequenceUpload"
    	StreetViewPublishService_CreatePhotoSequence_FullMethodName      = "/google.streetview.publish.v1.StreetViewPublishService/CreatePhotoSequence"
    	StreetViewPublishService_GetPhotoSequence_FullMethodName         = "/google.streetview.publish.v1.StreetViewPublishService/GetPhotoSequence"
    	StreetViewPublishService_ListPhotoSequences_FullMethodName       = "/google.streetview.publish.v1.StreetViewPublishService/ListPhotoSequences"
    	StreetViewPublishService_DeletePhotoSequence_FullMethodName      = "/google.streetview.publish.v1.StreetViewPublishService/DeletePhotoSequence"
    )

## Variables 

### ProcessingState_name, ProcessingState_value
    
    
    var (
    	ProcessingState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PROCESSING_STATE_UNSPECIFIED",
    		1: "PENDING",
    		2: "PROCESSING",
    		3: "PROCESSED",
    		4: "FAILED",
    	}
    	ProcessingState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PROCESSING_STATE_UNSPECIFIED": 0,
    		"PENDING":                      1,
    		"PROCESSING":                   2,
    		"PROCESSED":                    3,
    		"FAILED":                       4,
    	}
    )

Enum value maps for ProcessingState.

### ProcessingFailureReason_name, ProcessingFailureReason_value
    
    
    var (
    	ProcessingFailureReason_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "PROCESSING_FAILURE_REASON_UNSPECIFIED",
    		1:  "LOW_RESOLUTION",
    		2:  "DUPLICATE",
    		3:  "INSUFFICIENT_GPS",
    		4:  "NO_OVERLAP_GPS",
    		5:  "INVALID_GPS",
    		6:  "FAILED_TO_REFINE_POSITIONS",
    		7:  "TAKEDOWN",
    		8:  "CORRUPT_VIDEO",
    		9:  "INTERNAL",
    		10: "INVALID_VIDEO_FORMAT",
    		11: "INVALID_VIDEO_DIMENSIONS",
    		12: "INVALID_CAPTURE_TIME",
    		13: "GPS_DATA_GAP",
    		14: "JUMPY_GPS",
    		15: "INVALID_IMU",
    		21: "INSUFFICIENT_IMU",
    		22: "INSUFFICIENT_OVERLAP_TIME_SERIES",
    		16: "IMU_DATA_GAP",
    		17: "UNSUPPORTED_CAMERA",
    		18: "NOT_OUTDOORS",
    		19: "INSUFFICIENT_VIDEO_FRAMES",
    		20: "INSUFFICIENT_MOVEMENT",
    		27: "MAST_DOWN",
    		28: "CAMERA_COVERED",
    	}
    	ProcessingFailureReason_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PROCESSING_FAILURE_REASON_UNSPECIFIED": 0,
    		"LOW_RESOLUTION":                        1,
    		"DUPLICATE":                             2,
    		"INSUFFICIENT_GPS":                      3,
    		"NO_OVERLAP_GPS":                        4,
    		"INVALID_GPS":                           5,
    		"FAILED_TO_REFINE_POSITIONS":            6,
    		"TAKEDOWN":                              7,
    		"CORRUPT_VIDEO":                         8,
    		"INTERNAL":                              9,
    		"INVALID_VIDEO_FORMAT":                  10,
    		"INVALID_VIDEO_DIMENSIONS":              11,
    		"INVALID_CAPTURE_TIME":                  12,
    		"GPS_DATA_GAP":                          13,
    		"JUMPY_GPS":                             14,
    		"INVALID_IMU":                           15,
    		"INSUFFICIENT_IMU":                      21,
    		"INSUFFICIENT_OVERLAP_TIME_SERIES":      22,
    		"IMU_DATA_GAP":                          16,
    		"UNSUPPORTED_CAMERA":                    17,
    		"NOT_OUTDOORS":                          18,
    		"INSUFFICIENT_VIDEO_FRAMES":             19,
    		"INSUFFICIENT_MOVEMENT":                 20,
    		"MAST_DOWN":                             27,
    		"CAMERA_COVERED":                        28,
    	}
    )

Enum value maps for ProcessingFailureReason.

### Photo_TransferStatus_name, Photo_TransferStatus_value
    
    
    var (
    	Photo_TransferStatus_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TRANSFER_STATUS_UNKNOWN",
    		1: "NEVER_TRANSFERRED",
    		2: "PENDING",
    		3: "COMPLETED",
    		4: "REJECTED",
    		5: "EXPIRED",
    		6: "CANCELLED",
    		7: "RECEIVED_VIA_TRANSFER",
    	}
    	Photo_TransferStatus_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TRANSFER_STATUS_UNKNOWN": 0,
    		"NEVER_TRANSFERRED":       1,
    		"PENDING":                 2,
    		"COMPLETED":               3,
    		"REJECTED":                4,
    		"EXPIRED":                 5,
    		"CANCELLED":               6,
    		"RECEIVED_VIA_TRANSFER":   7,
    	}
    )

Enum value maps for Photo_TransferStatus.

### Photo_MapsPublishStatus_name, Photo_MapsPublishStatus_value
    
    
    var (
    	Photo_MapsPublishStatus_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "UNSPECIFIED_MAPS_PUBLISH_STATUS",
    		1: "PUBLISHED",
    		2: "REJECTED_UNKNOWN",
    	}
    	Photo_MapsPublishStatus_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"UNSPECIFIED_MAPS_PUBLISH_STATUS": 0,
    		"PUBLISHED":                       1,
    		"REJECTED_UNKNOWN":                2,
    	}
    )

Enum value maps for Photo_MapsPublishStatus.

### PhotoSequence_GpsSource_name, PhotoSequence_GpsSource_value
    
    
    var (
    	PhotoSequence_GpsSource_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PHOTO_SEQUENCE",
    		1: "CAMERA_MOTION_METADATA_TRACK",
    	}
    	PhotoSequence_GpsSource_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PHOTO_SEQUENCE":               0,
    		"CAMERA_MOTION_METADATA_TRACK": 1,
    	}
    )

Enum value maps for PhotoSequence_GpsSource.

### PhotoView_name, PhotoView_value
    
    
    var (
    	PhotoView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "BASIC",
    		1: "INCLUDE_DOWNLOAD_URL",
    	}
    	PhotoView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"BASIC":                0,
    		"INCLUDE_DOWNLOAD_URL": 1,
    	}
    )

Enum value maps for PhotoView.

### CreatePhotoSequenceRequest_InputType_name, CreatePhotoSequenceRequest_InputType_value
    
    
    var (
    	CreatePhotoSequenceRequest_InputType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INPUT_TYPE_UNSPECIFIED",
    		1: "VIDEO",
    		2: "XDM",
    	}
    	CreatePhotoSequenceRequest_InputType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INPUT_TYPE_UNSPECIFIED": 0,
    		"VIDEO":                  1,
    		"XDM":                    2,
    	}
    )

Enum value maps for CreatePhotoSequenceRequest_InputType.

### File_google_streetview_publish_v1_resources_proto
    
    
    var File_google_streetview_publish_v1_resources_proto protoreflect.FileDescriptor

### File_google_streetview_publish_v1_rpcmessages_proto
    
    
    var File_google_streetview_publish_v1_rpcmessages_proto protoreflect.FileDescriptor

### File_google_streetview_publish_v1_streetview_publish_proto
    
    
    var File_google_streetview_publish_v1_streetview_publish_proto protoreflect.FileDescriptor

### StreetViewPublishService_ServiceDesc
    
    
    var StreetViewPublishService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.streetview.publish.v1.StreetViewPublishService",
    	HandlerType: (*StreetViewPublishServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "StartUpload",
    			Handler:    _StreetViewPublishService_StartUpload_Handler,
    		},
    		{
    			MethodName: "CreatePhoto",
    			Handler:    _StreetViewPublishService_CreatePhoto_Handler,
    		},
    		{
    			MethodName: "GetPhoto",
    			Handler:    _StreetViewPublishService_GetPhoto_Handler,
    		},
    		{
    			MethodName: "BatchGetPhotos",
    			Handler:    _StreetViewPublishService_BatchGetPhotos_Handler,
    		},
    		{
    			MethodName: "ListPhotos",
    			Handler:    _StreetViewPublishService_ListPhotos_Handler,
    		},
    		{
    			MethodName: "UpdatePhoto",
    			Handler:    _StreetViewPublishService_UpdatePhoto_Handler,
    		},
    		{
    			MethodName: "BatchUpdatePhotos",
    			Handler:    _StreetViewPublishService_BatchUpdatePhotos_Handler,
    		},
    		{
    			MethodName: "DeletePhoto",
    			Handler:    _StreetViewPublishService_DeletePhoto_Handler,
    		},
    		{
    			MethodName: "BatchDeletePhotos",
    			Handler:    _StreetViewPublishService_BatchDeletePhotos_Handler,
    		},
    		{
    			MethodName: "StartPhotoSequenceUpload",
    			Handler:    _StreetViewPublishService_StartPhotoSequenceUpload_Handler,
    		},
    		{
    			MethodName: "CreatePhotoSequence",
    			Handler:    _StreetViewPublishService_CreatePhotoSequence_Handler,
    		},
    		{
    			MethodName: "GetPhotoSequence",
    			Handler:    _StreetViewPublishService_GetPhotoSequence_Handler,
    		},
    		{
    			MethodName: "ListPhotoSequences",
    			Handler:    _StreetViewPublishService_ListPhotoSequences_Handler,
    		},
    		{
    			MethodName: "DeletePhotoSequence",
    			Handler:    _StreetViewPublishService_DeletePhotoSequence_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/streetview/publish/v1/streetview_publish.proto",
    }

StreetViewPublishService_ServiceDesc is the grpc.ServiceDesc for StreetViewPublishService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterStreetViewPublishServiceServer 
    
    
    func RegisterStreetViewPublishServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv StreetViewPublishServiceServer)

## BatchDeletePhotosRequest
    
    
    type BatchDeletePhotosRequest struct {
    
    	// Required. IDs of the [Photos][google.streetview.publish.v1.Photo]. HTTP
    	// GET requests require the following syntax for the URL query parameter:
    	// `photoIds=

Request to delete multiple [Photos][google.streetview.publish.v1.Photo].

### func (*BatchDeletePhotosRequest) Descriptor 
    
    
    func (*BatchDeletePhotosRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchDeletePhotosRequest.ProtoReflect.Descriptor instead.

### func (*BatchDeletePhotosRequest) GetPhotoIds 
    
    
    func (x *BatchDeletePhotosRequest) GetPhotoIds() [][string](https://pkg.go.dev/builtin#string)

### func (*BatchDeletePhotosRequest) ProtoMessage 
    
    
    func (*BatchDeletePhotosRequest) ProtoMessage()

### func (*BatchDeletePhotosRequest) ProtoReflect 
    
    
    func (x *BatchDeletePhotosRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchDeletePhotosRequest) Reset 
    
    
    func (x *BatchDeletePhotosRequest) Reset()

### func (*BatchDeletePhotosRequest) String 
    
    
    func (x *BatchDeletePhotosRequest) String() [string](https://pkg.go.dev/builtin#string)

## BatchDeletePhotosResponse
    
    
    type BatchDeletePhotosResponse struct {
    
    	// The status for the operation to delete a single
    	// [Photo][google.streetview.publish.v1.Photo] in the batch request.
    	Status []*status.Status `protobuf:"bytes,1,rep,name=status,proto3" json:"status,omitempty"`
    	// contains filtered or unexported fields
    }

Response to batch delete of one or more [Photos][google.streetview.publish.v1.Photo].

### func (*BatchDeletePhotosResponse) Descriptor 
    
    
    func (*BatchDeletePhotosResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchDeletePhotosResponse.ProtoReflect.Descriptor instead.

### func (*BatchDeletePhotosResponse) GetStatus 
    
    
    func (x *BatchDeletePhotosResponse) GetStatus() []*[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*BatchDeletePhotosResponse) ProtoMessage 
    
    
    func (*BatchDeletePhotosResponse) ProtoMessage()

### func (*BatchDeletePhotosResponse) ProtoReflect 
    
    
    func (x *BatchDeletePhotosResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchDeletePhotosResponse) Reset 
    
    
    func (x *BatchDeletePhotosResponse) Reset()

### func (*BatchDeletePhotosResponse) String 
    
    
    func (x *BatchDeletePhotosResponse) String() [string](https://pkg.go.dev/builtin#string)

## BatchGetPhotosRequest
    
    
    type BatchGetPhotosRequest struct {
    
    	// Required. IDs of the [Photos][google.streetview.publish.v1.Photo]. For HTTP
    	// GET requests, the URL query parameter should be
    	// `photoIds=

Request to get one or more [Photos][google.streetview.publish.v1.Photo]. By default

  * does not return the download URL for the photo bytes.



Parameters:

  * `view` controls if the download URL for the photo bytes is returned.



### func (*BatchGetPhotosRequest) Descriptor 
    
    
    func (*BatchGetPhotosRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchGetPhotosRequest.ProtoReflect.Descriptor instead.

### func (*BatchGetPhotosRequest) GetLanguageCode 
    
    
    func (x *BatchGetPhotosRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*BatchGetPhotosRequest) GetPhotoIds 
    
    
    func (x *BatchGetPhotosRequest) GetPhotoIds() [][string](https://pkg.go.dev/builtin#string)

### func (*BatchGetPhotosRequest) GetView 
    
    
    func (x *BatchGetPhotosRequest) GetView() PhotoView

### func (*BatchGetPhotosRequest) ProtoMessage 
    
    
    func (*BatchGetPhotosRequest) ProtoMessage()

### func (*BatchGetPhotosRequest) ProtoReflect 
    
    
    func (x *BatchGetPhotosRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchGetPhotosRequest) Reset 
    
    
    func (x *BatchGetPhotosRequest) Reset()

### func (*BatchGetPhotosRequest) String 
    
    
    func (x *BatchGetPhotosRequest) String() [string](https://pkg.go.dev/builtin#string)

## BatchGetPhotosResponse
    
    
    type BatchGetPhotosResponse struct {
    
    	// List of results for each individual
    	// [Photo][google.streetview.publish.v1.Photo] requested, in the same order as
    	// the requests in
    	// [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos].
    	Results []*PhotoResponse `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
    	// contains filtered or unexported fields
    }

Response to batch get of [Photos][google.streetview.publish.v1.Photo].

### func (*BatchGetPhotosResponse) Descriptor 
    
    
    func (*BatchGetPhotosResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchGetPhotosResponse.ProtoReflect.Descriptor instead.

### func (*BatchGetPhotosResponse) GetResults 
    
    
    func (x *BatchGetPhotosResponse) GetResults() []*PhotoResponse

### func (*BatchGetPhotosResponse) ProtoMessage 
    
    
    func (*BatchGetPhotosResponse) ProtoMessage()

### func (*BatchGetPhotosResponse) ProtoReflect 
    
    
    func (x *BatchGetPhotosResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchGetPhotosResponse) Reset 
    
    
    func (x *BatchGetPhotosResponse) Reset()

### func (*BatchGetPhotosResponse) String 
    
    
    func (x *BatchGetPhotosResponse) String() [string](https://pkg.go.dev/builtin#string)

## BatchUpdatePhotosRequest
    
    
    type BatchUpdatePhotosRequest struct {
    
    	// Required. List of
    	// [UpdatePhotoRequests][google.streetview.publish.v1.UpdatePhotoRequest].
    	UpdatePhotoRequests []*UpdatePhotoRequest `protobuf:"bytes,1,rep,name=update_photo_requests,json=updatePhotoRequests,proto3" json:"update_photo_requests,omitempty"`
    	// contains filtered or unexported fields
    }

Request to update the metadata of photos. Updating the pixels of photos is not supported.

### func (*BatchUpdatePhotosRequest) Descriptor 
    
    
    func (*BatchUpdatePhotosRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchUpdatePhotosRequest.ProtoReflect.Descriptor instead.

### func (*BatchUpdatePhotosRequest) GetUpdatePhotoRequests 
    
    
    func (x *BatchUpdatePhotosRequest) GetUpdatePhotoRequests() []*UpdatePhotoRequest

### func (*BatchUpdatePhotosRequest) ProtoMessage 
    
    
    func (*BatchUpdatePhotosRequest) ProtoMessage()

### func (*BatchUpdatePhotosRequest) ProtoReflect 
    
    
    func (x *BatchUpdatePhotosRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchUpdatePhotosRequest) Reset 
    
    
    func (x *BatchUpdatePhotosRequest) Reset()

### func (*BatchUpdatePhotosRequest) String 
    
    
    func (x *BatchUpdatePhotosRequest) String() [string](https://pkg.go.dev/builtin#string)

## BatchUpdatePhotosResponse
    
    
    type BatchUpdatePhotosResponse struct {
    
    	// List of results for each individual
    	// [Photo][google.streetview.publish.v1.Photo] updated, in the same order as
    	// the request.
    	Results []*PhotoResponse `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
    	// contains filtered or unexported fields
    }

Response to batch update of metadata of one or more [Photos][google.streetview.publish.v1.Photo].

### func (*BatchUpdatePhotosResponse) Descriptor 
    
    
    func (*BatchUpdatePhotosResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchUpdatePhotosResponse.ProtoReflect.Descriptor instead.

### func (*BatchUpdatePhotosResponse) GetResults 
    
    
    func (x *BatchUpdatePhotosResponse) GetResults() []*PhotoResponse

### func (*BatchUpdatePhotosResponse) ProtoMessage 
    
    
    func (*BatchUpdatePhotosResponse) ProtoMessage()

### func (*BatchUpdatePhotosResponse) ProtoReflect 
    
    
    func (x *BatchUpdatePhotosResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchUpdatePhotosResponse) Reset 
    
    
    func (x *BatchUpdatePhotosResponse) Reset()

### func (*BatchUpdatePhotosResponse) String 
    
    
    func (x *BatchUpdatePhotosResponse) String() [string](https://pkg.go.dev/builtin#string)

## Connection
    
    
    type Connection struct {
    
    	// Required. The destination of the connection from the containing photo to
    	// another photo.
    	Target *PhotoId `protobuf:"bytes,1,opt,name=target,proto3" json:"target,omitempty"`
    	// contains filtered or unexported fields
    }

A connection is the link from a source photo to a destination photo.

### func (*Connection) Descriptor 
    
    
    func (*Connection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Connection.ProtoReflect.Descriptor instead.

### func (*Connection) GetTarget 
    
    
    func (x *Connection) GetTarget() *PhotoId

### func (*Connection) ProtoMessage 
    
    
    func (*Connection) ProtoMessage()

### func (*Connection) ProtoReflect 
    
    
    func (x *Connection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Connection) Reset 
    
    
    func (x *Connection) Reset()

### func (*Connection) String 
    
    
    func (x *Connection) String() [string](https://pkg.go.dev/builtin#string)

## CreatePhotoRequest
    
    
    type CreatePhotoRequest struct {
    
    	// Required. Photo to create.
    	Photo *Photo `protobuf:"bytes,1,opt,name=photo,proto3" json:"photo,omitempty"`
    	// contains filtered or unexported fields
    }

Request to create a [Photo][google.streetview.publish.v1.Photo].

### func (*CreatePhotoRequest) Descriptor 
    
    
    func (*CreatePhotoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreatePhotoRequest.ProtoReflect.Descriptor instead.

### func (*CreatePhotoRequest) GetPhoto 
    
    
    func (x *CreatePhotoRequest) GetPhoto() *Photo

### func (*CreatePhotoRequest) ProtoMessage 
    
    
    func (*CreatePhotoRequest) ProtoMessage()

### func (*CreatePhotoRequest) ProtoReflect 
    
    
    func (x *CreatePhotoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreatePhotoRequest) Reset 
    
    
    func (x *CreatePhotoRequest) Reset()

### func (*CreatePhotoRequest) String 
    
    
    func (x *CreatePhotoRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreatePhotoSequenceRequest
    
    
    type CreatePhotoSequenceRequest struct {
    
    	// Required. [PhotoSequence][google.streetview.publish.v1.PhotoSequence] to
    	// create.
    	PhotoSequence *PhotoSequence `protobuf:"bytes,1,opt,name=photo_sequence,json=photoSequence,proto3" json:"photo_sequence,omitempty"`
    	// Required. The input form of
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence].
    	InputType CreatePhotoSequenceRequest_InputType `protobuf:"varint,2,opt,name=input_type,json=inputType,proto3,enum=google.streetview.publish.v1.CreatePhotoSequenceRequest_InputType" json:"input_type,omitempty"`
    	// contains filtered or unexported fields
    }

Request to create a [PhotoSequence][google.streetview.publish.v1.PhotoSequence] from a video.

### func (*CreatePhotoSequenceRequest) Descriptor 
    
    
    func (*CreatePhotoSequenceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreatePhotoSequenceRequest.ProtoReflect.Descriptor instead.

### func (*CreatePhotoSequenceRequest) GetInputType 
    
    
    func (x *CreatePhotoSequenceRequest) GetInputType() CreatePhotoSequenceRequest_InputType

### func (*CreatePhotoSequenceRequest) GetPhotoSequence 
    
    
    func (x *CreatePhotoSequenceRequest) GetPhotoSequence() *PhotoSequence

### func (*CreatePhotoSequenceRequest) ProtoMessage 
    
    
    func (*CreatePhotoSequenceRequest) ProtoMessage()

### func (*CreatePhotoSequenceRequest) ProtoReflect 
    
    
    func (x *CreatePhotoSequenceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreatePhotoSequenceRequest) Reset 
    
    
    func (x *CreatePhotoSequenceRequest) Reset()

### func (*CreatePhotoSequenceRequest) String 
    
    
    func (x *CreatePhotoSequenceRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreatePhotoSequenceRequest_InputType
    
    
    type CreatePhotoSequenceRequest_InputType [int32](https://pkg.go.dev/builtin#int32)

Input forms of [PhotoSequence][google.streetview.publish.v1.PhotoSequence].

### CreatePhotoSequenceRequest_INPUT_TYPE_UNSPECIFIED, CreatePhotoSequenceRequest_VIDEO, CreatePhotoSequenceRequest_XDM
    
    
    const (
    	// Not specified. Server will return
    	// [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT].
    	CreatePhotoSequenceRequest_INPUT_TYPE_UNSPECIFIED CreatePhotoSequenceRequest_InputType = 0
    	// 360 Video.
    	CreatePhotoSequenceRequest_VIDEO CreatePhotoSequenceRequest_InputType = 1
    	// Extensible Device Metadata, http://www.xdm.org
    	CreatePhotoSequenceRequest_XDM CreatePhotoSequenceRequest_InputType = 2
    )

### func (CreatePhotoSequenceRequest_InputType) Descriptor 
    
    
    func (CreatePhotoSequenceRequest_InputType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CreatePhotoSequenceRequest_InputType) Enum 
    
    
    func (x CreatePhotoSequenceRequest_InputType) Enum() *CreatePhotoSequenceRequest_InputType

### func (CreatePhotoSequenceRequest_InputType) EnumDescriptor 
    
    
    func (CreatePhotoSequenceRequest_InputType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreatePhotoSequenceRequest_InputType.Descriptor instead.

### func (CreatePhotoSequenceRequest_InputType) Number 
    
    
    func (x CreatePhotoSequenceRequest_InputType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CreatePhotoSequenceRequest_InputType) String 
    
    
    func (x CreatePhotoSequenceRequest_InputType) String() [string](https://pkg.go.dev/builtin#string)

### func (CreatePhotoSequenceRequest_InputType) Type 
    
    
    func (CreatePhotoSequenceRequest_InputType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DeletePhotoRequest
    
    
    type DeletePhotoRequest struct {
    
    	// Required. ID of the [Photo][google.streetview.publish.v1.Photo].
    	PhotoId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=photo_id,json=photoId,proto3" json:"photo_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request to delete a [Photo][google.streetview.publish.v1.Photo].

### func (*DeletePhotoRequest) Descriptor 
    
    
    func (*DeletePhotoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletePhotoRequest.ProtoReflect.Descriptor instead.

### func (*DeletePhotoRequest) GetPhotoId 
    
    
    func (x *DeletePhotoRequest) GetPhotoId() [string](https://pkg.go.dev/builtin#string)

### func (*DeletePhotoRequest) ProtoMessage 
    
    
    func (*DeletePhotoRequest) ProtoMessage()

### func (*DeletePhotoRequest) ProtoReflect 
    
    
    func (x *DeletePhotoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeletePhotoRequest) Reset 
    
    
    func (x *DeletePhotoRequest) Reset()

### func (*DeletePhotoRequest) String 
    
    
    func (x *DeletePhotoRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeletePhotoSequenceRequest
    
    
    type DeletePhotoSequenceRequest struct {
    
    	// Required. ID of the
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence].
    	SequenceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=sequence_id,json=sequenceId,proto3" json:"sequence_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request to delete a [PhotoSequence][google.streetview.publish.v1.PhotoSequence].

### func (*DeletePhotoSequenceRequest) Descriptor 
    
    
    func (*DeletePhotoSequenceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletePhotoSequenceRequest.ProtoReflect.Descriptor instead.

### func (*DeletePhotoSequenceRequest) GetSequenceId 
    
    
    func (x *DeletePhotoSequenceRequest) GetSequenceId() [string](https://pkg.go.dev/builtin#string)

### func (*DeletePhotoSequenceRequest) ProtoMessage 
    
    
    func (*DeletePhotoSequenceRequest) ProtoMessage()

### func (*DeletePhotoSequenceRequest) ProtoReflect 
    
    
    func (x *DeletePhotoSequenceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeletePhotoSequenceRequest) Reset 
    
    
    func (x *DeletePhotoSequenceRequest) Reset()

### func (*DeletePhotoSequenceRequest) String 
    
    
    func (x *DeletePhotoSequenceRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetPhotoRequest
    
    
    type GetPhotoRequest struct {
    
    	// Required. ID of the [Photo][google.streetview.publish.v1.Photo].
    	PhotoId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=photo_id,json=photoId,proto3" json:"photo_id,omitempty"`
    	// Required. Specifies if a download URL for the photo bytes should be
    	// returned in the [Photo][google.streetview.publish.v1.Photo] response.
    	View PhotoView `protobuf:"varint,2,opt,name=view,proto3,enum=google.streetview.publish.v1.PhotoView" json:"view,omitempty"`
    	// The BCP-47 language code, such as "en-US" or "sr-Latn". For more
    	// information, see
    	// http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    	// If language_code is unspecified, the user's language preference for Google
    	// services is used.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get a [Photo][google.streetview.publish.v1.Photo].

# By default

  * does not return the download URL for the photo bytes.



Parameters:

  * `view` controls if the download URL for the photo bytes is returned.



### func (*GetPhotoRequest) Descriptor 
    
    
    func (*GetPhotoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPhotoRequest.ProtoReflect.Descriptor instead.

### func (*GetPhotoRequest) GetLanguageCode 
    
    
    func (x *GetPhotoRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*GetPhotoRequest) GetPhotoId 
    
    
    func (x *GetPhotoRequest) GetPhotoId() [string](https://pkg.go.dev/builtin#string)

### func (*GetPhotoRequest) GetView 
    
    
    func (x *GetPhotoRequest) GetView() PhotoView

### func (*GetPhotoRequest) ProtoMessage 
    
    
    func (*GetPhotoRequest) ProtoMessage()

### func (*GetPhotoRequest) ProtoReflect 
    
    
    func (x *GetPhotoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPhotoRequest) Reset 
    
    
    func (x *GetPhotoRequest) Reset()

### func (*GetPhotoRequest) String 
    
    
    func (x *GetPhotoRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetPhotoSequenceRequest
    
    
    type GetPhotoSequenceRequest struct {
    
    	// Required. ID of the photo sequence.
    	SequenceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=sequence_id,json=sequenceId,proto3" json:"sequence_id,omitempty"`
    	// Specifies if a download URL for the photo sequence should be returned in
    	// `download_url` of individual photos in the
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] response.
    	// > Note: Currently not implemented.
    	//
    	// Deprecated: Marked as deprecated in google/streetview/publish/v1/rpcmessages.proto.
    	View PhotoView `protobuf:"varint,2,opt,name=view,proto3,enum=google.streetview.publish.v1.PhotoView" json:"view,omitempty"`
    	// Optional. The filter expression. For example: `published_status=PUBLISHED`.
    	//
    	// The filters supported are: `published_status`.  See
    	// https://google.aip.dev/160 for more information.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request to get a [PhotoSequence][google.streetview.publish.v1.PhotoSequence].

# By default

  * does not return the download URL for the [PhotoSequence][google.streetview.publish.v1.PhotoSequence].



Parameters:

  * `view` controls if the download URL for the [PhotoSequence][google.streetview.publish.v1.PhotoSequence] is

returned.




### func (*GetPhotoSequenceRequest) Descriptor 
    
    
    func (*GetPhotoSequenceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPhotoSequenceRequest.ProtoReflect.Descriptor instead.

### func (*GetPhotoSequenceRequest) GetFilter 
    
    
    func (x *GetPhotoSequenceRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*GetPhotoSequenceRequest) GetSequenceId 
    
    
    func (x *GetPhotoSequenceRequest) GetSequenceId() [string](https://pkg.go.dev/builtin#string)

### func (*GetPhotoSequenceRequest) GetView 
    
    
    func (x *GetPhotoSequenceRequest) GetView() PhotoView

Deprecated: Marked as deprecated in google/streetview/publish/v1/rpcmessages.proto.

### func (*GetPhotoSequenceRequest) ProtoMessage 
    
    
    func (*GetPhotoSequenceRequest) ProtoMessage()

### func (*GetPhotoSequenceRequest) ProtoReflect 
    
    
    func (x *GetPhotoSequenceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPhotoSequenceRequest) Reset 
    
    
    func (x *GetPhotoSequenceRequest) Reset()

### func (*GetPhotoSequenceRequest) String 
    
    
    func (x *GetPhotoSequenceRequest) String() [string](https://pkg.go.dev/builtin#string)

## GpsDataGapFailureDetails
    
    
    type GpsDataGapFailureDetails struct {
    
    	// The duration of the gap in GPS data that was found.
    	GapDuration *durationpb.Duration `protobuf:"bytes,1,opt,name=gap_duration,json=gapDuration,proto3,oneof" json:"gap_duration,omitempty"`
    	// Relative time (from the start of the video stream) when the gap started.
    	GapStartTime *durationpb.Duration `protobuf:"bytes,2,opt,name=gap_start_time,json=gapStartTime,proto3,oneof" json:"gap_start_time,omitempty"`
    	// contains filtered or unexported fields
    }

Details related to ProcessingFailureReason#GPS_DATA_GAP. If there are multiple GPS data gaps, only the one with the largest duration is reported here.

### func (*GpsDataGapFailureDetails) Descriptor 
    
    
    func (*GpsDataGapFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GpsDataGapFailureDetails.ProtoReflect.Descriptor instead.

### func (*GpsDataGapFailureDetails) GetGapDuration 
    
    
    func (x *GpsDataGapFailureDetails) GetGapDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*GpsDataGapFailureDetails) GetGapStartTime 
    
    
    func (x *GpsDataGapFailureDetails) GetGapStartTime() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*GpsDataGapFailureDetails) ProtoMessage 
    
    
    func (*GpsDataGapFailureDetails) ProtoMessage()

### func (*GpsDataGapFailureDetails) ProtoReflect 
    
    
    func (x *GpsDataGapFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GpsDataGapFailureDetails) Reset 
    
    
    func (x *GpsDataGapFailureDetails) Reset()

### func (*GpsDataGapFailureDetails) String 
    
    
    func (x *GpsDataGapFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## Imu
    
    
    type Imu struct {
    
    	// The accelerometer measurements in meters/sec^2 with increasing timestamps
    	// from devices.
    	AccelMpsps []*Imu_Measurement3D `protobuf:"bytes,1,rep,name=accel_mpsps,json=accelMpsps,proto3" json:"accel_mpsps,omitempty"`
    	// The gyroscope measurements in radians/sec with increasing timestamps from
    	// devices.
    	GyroRps []*Imu_Measurement3D `protobuf:"bytes,2,rep,name=gyro_rps,json=gyroRps,proto3" json:"gyro_rps,omitempty"`
    	// The magnetometer measurements of the magnetic field in microtesla (uT) with
    	// increasing timestamps from devices.
    	MagUt []*Imu_Measurement3D `protobuf:"bytes,3,rep,name=mag_ut,json=magUt,proto3" json:"mag_ut,omitempty"`
    	// contains filtered or unexported fields
    }

IMU data from the device sensors.

### func (*Imu) Descriptor 
    
    
    func (*Imu) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Imu.ProtoReflect.Descriptor instead.

### func (*Imu) GetAccelMpsps 
    
    
    func (x *Imu) GetAccelMpsps() []*Imu_Measurement3D

### func (*Imu) GetGyroRps 
    
    
    func (x *Imu) GetGyroRps() []*Imu_Measurement3D

### func (*Imu) GetMagUt 
    
    
    func (x *Imu) GetMagUt() []*Imu_Measurement3D

### func (*Imu) ProtoMessage 
    
    
    func (*Imu) ProtoMessage()

### func (*Imu) ProtoReflect 
    
    
    func (x *Imu) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Imu) Reset 
    
    
    func (x *Imu) Reset()

### func (*Imu) String 
    
    
    func (x *Imu) String() [string](https://pkg.go.dev/builtin#string)

## ImuDataGapFailureDetails
    
    
    type ImuDataGapFailureDetails struct {
    
    	// The duration of the gap in IMU data that was found.
    	GapDuration *durationpb.Duration `protobuf:"bytes,1,opt,name=gap_duration,json=gapDuration,proto3,oneof" json:"gap_duration,omitempty"`
    	// Relative time (from the start of the video stream) when the gap started.
    	GapStartTime *durationpb.Duration `protobuf:"bytes,2,opt,name=gap_start_time,json=gapStartTime,proto3,oneof" json:"gap_start_time,omitempty"`
    	// contains filtered or unexported fields
    }

Details related to ProcessingFailureReason#IMU_DATA_GAP. If there are multiple IMU data gaps, only the one with the largest duration is reported here.

### func (*ImuDataGapFailureDetails) Descriptor 
    
    
    func (*ImuDataGapFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImuDataGapFailureDetails.ProtoReflect.Descriptor instead.

### func (*ImuDataGapFailureDetails) GetGapDuration 
    
    
    func (x *ImuDataGapFailureDetails) GetGapDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*ImuDataGapFailureDetails) GetGapStartTime 
    
    
    func (x *ImuDataGapFailureDetails) GetGapStartTime() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*ImuDataGapFailureDetails) ProtoMessage 
    
    
    func (*ImuDataGapFailureDetails) ProtoMessage()

### func (*ImuDataGapFailureDetails) ProtoReflect 
    
    
    func (x *ImuDataGapFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ImuDataGapFailureDetails) Reset 
    
    
    func (x *ImuDataGapFailureDetails) Reset()

### func (*ImuDataGapFailureDetails) String 
    
    
    func (x *ImuDataGapFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## Imu_Measurement3D
    
    
    type Imu_Measurement3D struct {
    
    	// The timestamp of the IMU measurement.
    	CaptureTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=capture_time,json=captureTime,proto3" json:"capture_time,omitempty"`
    	// The sensor measurement in the x axis.
    	X [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,2,opt,name=x,proto3" json:"x,omitempty"`
    	// The sensor measurement in the y axis.
    	Y [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,3,opt,name=y,proto3" json:"y,omitempty"`
    	// The sensor measurement in the z axis.
    	Z [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,4,opt,name=z,proto3" json:"z,omitempty"`
    	// contains filtered or unexported fields
    }

A Generic 3d measurement sample.

### func (*Imu_Measurement3D) Descriptor 
    
    
    func (*Imu_Measurement3D) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Imu_Measurement3D.ProtoReflect.Descriptor instead.

### func (*Imu_Measurement3D) GetCaptureTime 
    
    
    func (x *Imu_Measurement3D) GetCaptureTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Imu_Measurement3D) GetX 
    
    
    func (x *Imu_Measurement3D) GetX() [float32](https://pkg.go.dev/builtin#float32)

### func (*Imu_Measurement3D) GetY 
    
    
    func (x *Imu_Measurement3D) GetY() [float32](https://pkg.go.dev/builtin#float32)

### func (*Imu_Measurement3D) GetZ 
    
    
    func (x *Imu_Measurement3D) GetZ() [float32](https://pkg.go.dev/builtin#float32)

### func (*Imu_Measurement3D) ProtoMessage 
    
    
    func (*Imu_Measurement3D) ProtoMessage()

### func (*Imu_Measurement3D) ProtoReflect 
    
    
    func (x *Imu_Measurement3D) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Imu_Measurement3D) Reset 
    
    
    func (x *Imu_Measurement3D) Reset()

### func (*Imu_Measurement3D) String 
    
    
    func (x *Imu_Measurement3D) String() [string](https://pkg.go.dev/builtin#string)

## InsufficientGpsFailureDetails
    
    
    type InsufficientGpsFailureDetails struct {
    
    	// The number of GPS points that were found in the video.
    	GpsPointsFound *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=gps_points_found,json=gpsPointsFound,proto3,oneof" json:"gps_points_found,omitempty"`
    	// contains filtered or unexported fields
    }

Details related to ProcessingFailureReason#INSUFFICIENT_GPS.

### func (*InsufficientGpsFailureDetails) Descriptor 
    
    
    func (*InsufficientGpsFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsufficientGpsFailureDetails.ProtoReflect.Descriptor instead.

### func (*InsufficientGpsFailureDetails) GetGpsPointsFound 
    
    
    func (x *InsufficientGpsFailureDetails) GetGpsPointsFound() [int32](https://pkg.go.dev/builtin#int32)

### func (*InsufficientGpsFailureDetails) ProtoMessage 
    
    
    func (*InsufficientGpsFailureDetails) ProtoMessage()

### func (*InsufficientGpsFailureDetails) ProtoReflect 
    
    
    func (x *InsufficientGpsFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsufficientGpsFailureDetails) Reset 
    
    
    func (x *InsufficientGpsFailureDetails) Reset()

### func (*InsufficientGpsFailureDetails) String 
    
    
    func (x *InsufficientGpsFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## LatLngBounds
    
    
    type LatLngBounds struct {
    
    	// The southwest corner of these bounds.
    	Southwest *latlng.LatLng `protobuf:"bytes,1,opt,name=southwest,proto3" json:"southwest,omitempty"`
    	// The northeast corner of these bounds.
    	Northeast *latlng.LatLng `protobuf:"bytes,2,opt,name=northeast,proto3" json:"northeast,omitempty"`
    	// contains filtered or unexported fields
    }

A rectangle in geographical coordinates.

### func (*LatLngBounds) Descriptor 
    
    
    func (*LatLngBounds) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LatLngBounds.ProtoReflect.Descriptor instead.

### func (*LatLngBounds) GetNortheast 
    
    
    func (x *LatLngBounds) GetNortheast() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*LatLngBounds) GetSouthwest 
    
    
    func (x *LatLngBounds) GetSouthwest() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*LatLngBounds) ProtoMessage 
    
    
    func (*LatLngBounds) ProtoMessage()

### func (*LatLngBounds) ProtoReflect 
    
    
    func (x *LatLngBounds) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LatLngBounds) Reset 
    
    
    func (x *LatLngBounds) Reset()

### func (*LatLngBounds) String 
    
    
    func (x *LatLngBounds) String() [string](https://pkg.go.dev/builtin#string)

## Level
    
    
    type Level struct {
    
    	// Optional. Floor number, used for ordering. 0 indicates the ground level, 1
    	// indicates the first level above ground level, -1 indicates the first level
    	// under ground level. Non-integer values are OK.
    	Number [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=number,proto3" json:"number,omitempty"`
    	// Required. A name assigned to this Level, restricted to 3 characters.
    	// Consider how the elevator buttons would be labeled for this level if there
    	// was an elevator.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Level information containing level number and its corresponding name.

### func (*Level) Descriptor 
    
    
    func (*Level) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Level.ProtoReflect.Descriptor instead.

### func (*Level) GetName 
    
    
    func (x *Level) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Level) GetNumber 
    
    
    func (x *Level) GetNumber() [float64](https://pkg.go.dev/builtin#float64)

### func (*Level) ProtoMessage 
    
    
    func (*Level) ProtoMessage()

### func (*Level) ProtoReflect 
    
    
    func (x *Level) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Level) Reset 
    
    
    func (x *Level) Reset()

### func (*Level) String 
    
    
    func (x *Level) String() [string](https://pkg.go.dev/builtin#string)

## ListPhotoSequencesRequest
    
    
    type ListPhotoSequencesRequest struct {
    
    	// Optional. The maximum number of photo sequences to return.
    	// `pageSize` must be non-negative. If `pageSize` is zero or is not
    	// provided, the default page size of 100 is used.
    	// The number of photo sequences returned in the response may be less than
    	// `pageSize` if the number of matches is less than `pageSize`.
    	// This is currently unimplemented but is in process.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The
    	// [nextPageToken][google.streetview.publish.v1.ListPhotosResponse.next_page_token]
    	// value returned from a previous
    	// [ListPhotoSequences][google.streetview.publish.v1.StreetViewPublishService.ListPhotoSequences]
    	// request, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. The filter expression. For example: `imagery_type=SPHERICAL`.
    	//
    	// The filters supported are: `imagery_type`, `processing_state`,
    	// `min_latitude`, `max_latitude`, `min_longitude`, `max_longitude`,
    	// `filename_query`, `min_capture_time_seconds`, `max_capture_time_seconds.
    	// See https://google.aip.dev/160 for more information. Filename queries
    	// should sent as a Phrase in order to support multiple words and special
    	// characters by adding escaped quotes. Ex: filename_query="example of a
    	// phrase.mp4"
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

Request to list all photo sequences that belong to the user sending the request.

Parameters:

  * `pageSize` determines the maximum number of photo sequences to return.
  * `pageToken` is the next page token value returned from a previous [ListPhotoSequences][google.streetview.publish.v1.StreetViewPublishService.ListPhotoSequences]

request, if any.




### func (*ListPhotoSequencesRequest) Descriptor 
    
    
    func (*ListPhotoSequencesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPhotoSequencesRequest.ProtoReflect.Descriptor instead.

### func (*ListPhotoSequencesRequest) GetFilter 
    
    
    func (x *ListPhotoSequencesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotoSequencesRequest) GetPageSize 
    
    
    func (x *ListPhotoSequencesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListPhotoSequencesRequest) GetPageToken 
    
    
    func (x *ListPhotoSequencesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotoSequencesRequest) ProtoMessage 
    
    
    func (*ListPhotoSequencesRequest) ProtoMessage()

### func (*ListPhotoSequencesRequest) ProtoReflect 
    
    
    func (x *ListPhotoSequencesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPhotoSequencesRequest) Reset 
    
    
    func (x *ListPhotoSequencesRequest) Reset()

### func (*ListPhotoSequencesRequest) String 
    
    
    func (x *ListPhotoSequencesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListPhotoSequencesResponse
    
    
    type ListPhotoSequencesResponse struct {
    
    	// List of photo sequences via [Operation][google.longrunning.Operation]
    	// interface.
    	//
    	// The maximum number of items returned is based on the
    	// [pageSize][google.streetview.publish.v1.ListPhotoSequencesRequest.page_size]
    	// field in the request.
    	//
    	// Each item in the list can have three possible states,
    	//
    	//   - `Operation.done` = false, if the processing of
    	//     [PhotoSequence][google.streetview.publish.v1.PhotoSequence] is not
    	//     finished yet.
    	//   - `Operation.done` = true and `Operation.error` is populated, if there was
    	//     an error in processing.
    	//   - `Operation.done` = true and `Operation.response` contains a
    	//     [PhotoSequence][google.streetview.publish.v1.PhotoSequence] message,
    	//     In each sequence, only
    	//     [Id][google.streetview.publish.v1.PhotoSequence.id] is populated.
    	PhotoSequences []*longrunningpb.Operation `protobuf:"bytes,1,rep,name=photo_sequences,json=photoSequences,proto3" json:"photo_sequences,omitempty"`
    	// Token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to list all photo sequences that belong to a user.

### func (*ListPhotoSequencesResponse) Descriptor 
    
    
    func (*ListPhotoSequencesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPhotoSequencesResponse.ProtoReflect.Descriptor instead.

### func (*ListPhotoSequencesResponse) GetNextPageToken 
    
    
    func (x *ListPhotoSequencesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotoSequencesResponse) GetPhotoSequences 
    
    
    func (x *ListPhotoSequencesResponse) GetPhotoSequences() []*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation)

### func (*ListPhotoSequencesResponse) ProtoMessage 
    
    
    func (*ListPhotoSequencesResponse) ProtoMessage()

### func (*ListPhotoSequencesResponse) ProtoReflect 
    
    
    func (x *ListPhotoSequencesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPhotoSequencesResponse) Reset 
    
    
    func (x *ListPhotoSequencesResponse) Reset()

### func (*ListPhotoSequencesResponse) String 
    
    
    func (x *ListPhotoSequencesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListPhotosRequest
    
    
    type ListPhotosRequest struct {
    
    	// Required. Specifies if a download URL for the photos bytes should be
    	// returned in the Photos response.
    	View PhotoView `protobuf:"varint,1,opt,name=view,proto3,enum=google.streetview.publish.v1.PhotoView" json:"view,omitempty"`
    	// Optional. The maximum number of photos to return.
    	// `pageSize` must be non-negative. If `pageSize` is zero or is not provided,
    	// the default page size of 100 is used.
    	// The number of photos returned in the response may be less than `pageSize`
    	// if the number of photos that belong to the user is less than `pageSize`.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. The
    	// [nextPageToken][google.streetview.publish.v1.ListPhotosResponse.next_page_token]
    	// value returned from a previous
    	// [ListPhotos][google.streetview.publish.v1.StreetViewPublishService.ListPhotos]
    	// request, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. The filter expression. For example:
    	// `placeId=ChIJj61dQgK6j4AR4GeTYWZsKWw`.
    	//
    	// The filters supported are: `placeId`, `min_latitude`, `max_latitude`,
    	// `min_longitude`, `max_longitude`. See https://google.aip.dev/160 for more
    	// information.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. The BCP-47 language code, such as "en-US" or "sr-Latn". For more
    	// information, see
    	// http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    	// If language_code is unspecified, the user's language preference for Google
    	// services is used.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

Request to list all photos that belong to the user sending the request.

# By default

  * does not return the download URL for the photo bytes.



Parameters:

  * `view` controls if the download URL for the photo bytes is returned.
  * `pageSize` determines the maximum number of photos to return.
  * `pageToken` is the next page token value returned from a previous [ListPhotos][google.streetview.publish.v1.StreetViewPublishService.ListPhotos]

request, if any.

  * `filter` allows filtering by a given parameter. 'placeId' is the only parameter supported at the moment.




### func (*ListPhotosRequest) Descriptor 
    
    
    func (*ListPhotosRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPhotosRequest.ProtoReflect.Descriptor instead.

### func (*ListPhotosRequest) GetFilter 
    
    
    func (x *ListPhotosRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotosRequest) GetLanguageCode 
    
    
    func (x *ListPhotosRequest) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotosRequest) GetPageSize 
    
    
    func (x *ListPhotosRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListPhotosRequest) GetPageToken 
    
    
    func (x *ListPhotosRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotosRequest) GetView 
    
    
    func (x *ListPhotosRequest) GetView() PhotoView

### func (*ListPhotosRequest) ProtoMessage 
    
    
    func (*ListPhotosRequest) ProtoMessage()

### func (*ListPhotosRequest) ProtoReflect 
    
    
    func (x *ListPhotosRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPhotosRequest) Reset 
    
    
    func (x *ListPhotosRequest) Reset()

### func (*ListPhotosRequest) String 
    
    
    func (x *ListPhotosRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListPhotosResponse
    
    
    type ListPhotosResponse struct {
    
    	// List of photos. The
    	// [pageSize][google.streetview.publish.v1.ListPhotosRequest.page_size] field
    	// in the request determines the number of items returned.
    	Photos []*Photo `protobuf:"bytes,1,rep,name=photos,proto3" json:"photos,omitempty"`
    	// Token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response to list all photos that belong to a user.

### func (*ListPhotosResponse) Descriptor 
    
    
    func (*ListPhotosResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPhotosResponse.ProtoReflect.Descriptor instead.

### func (*ListPhotosResponse) GetNextPageToken 
    
    
    func (x *ListPhotosResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPhotosResponse) GetPhotos 
    
    
    func (x *ListPhotosResponse) GetPhotos() []*Photo

### func (*ListPhotosResponse) ProtoMessage 
    
    
    func (*ListPhotosResponse) ProtoMessage()

### func (*ListPhotosResponse) ProtoReflect 
    
    
    func (x *ListPhotosResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPhotosResponse) Reset 
    
    
    func (x *ListPhotosResponse) Reset()

### func (*ListPhotosResponse) String 
    
    
    func (x *ListPhotosResponse) String() [string](https://pkg.go.dev/builtin#string)

## NoOverlapGpsFailureDetails
    
    
    type NoOverlapGpsFailureDetails struct {
    
    	// Time of first recorded GPS point.
    	GpsStartTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=gps_start_time,json=gpsStartTime,proto3,oneof" json:"gps_start_time,omitempty"`
    	// Time of last recorded GPS point.
    	GpsEndTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=gps_end_time,json=gpsEndTime,proto3,oneof" json:"gps_end_time,omitempty"`
    	// Start time of video.
    	VideoStartTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=video_start_time,json=videoStartTime,proto3,oneof" json:"video_start_time,omitempty"`
    	// End time of video.
    	VideoEndTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=video_end_time,json=videoEndTime,proto3,oneof" json:"video_end_time,omitempty"`
    	// contains filtered or unexported fields
    }

Details related to PhotoSequenceProcessingFailureReason#NO_OVERLAP_GPS.

### func (*NoOverlapGpsFailureDetails) Descriptor 
    
    
    func (*NoOverlapGpsFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NoOverlapGpsFailureDetails.ProtoReflect.Descriptor instead.

### func (*NoOverlapGpsFailureDetails) GetGpsEndTime 
    
    
    func (x *NoOverlapGpsFailureDetails) GetGpsEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*NoOverlapGpsFailureDetails) GetGpsStartTime 
    
    
    func (x *NoOverlapGpsFailureDetails) GetGpsStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*NoOverlapGpsFailureDetails) GetVideoEndTime 
    
    
    func (x *NoOverlapGpsFailureDetails) GetVideoEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*NoOverlapGpsFailureDetails) GetVideoStartTime 
    
    
    func (x *NoOverlapGpsFailureDetails) GetVideoStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*NoOverlapGpsFailureDetails) ProtoMessage 
    
    
    func (*NoOverlapGpsFailureDetails) ProtoMessage()

### func (*NoOverlapGpsFailureDetails) ProtoReflect 
    
    
    func (x *NoOverlapGpsFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NoOverlapGpsFailureDetails) Reset 
    
    
    func (x *NoOverlapGpsFailureDetails) Reset()

### func (*NoOverlapGpsFailureDetails) String 
    
    
    func (x *NoOverlapGpsFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## NotOutdoorsFailureDetails
    
    
    type NotOutdoorsFailureDetails struct {
    
    	// Relative time (from the start of the video stream) when an indoor frame was
    	// found.
    	StartTime *durationpb.Duration `protobuf:"bytes,1,opt,name=start_time,json=startTime,proto3,oneof" json:"start_time,omitempty"`
    	// contains filtered or unexported fields
    }

Details related to ProcessingFailureReason#NOT_OUTDOORS. If there are multiple indoor frames found, the first frame is recorded here.

### func (*NotOutdoorsFailureDetails) Descriptor 
    
    
    func (*NotOutdoorsFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NotOutdoorsFailureDetails.ProtoReflect.Descriptor instead.

### func (*NotOutdoorsFailureDetails) GetStartTime 
    
    
    func (x *NotOutdoorsFailureDetails) GetStartTime() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*NotOutdoorsFailureDetails) ProtoMessage 
    
    
    func (*NotOutdoorsFailureDetails) ProtoMessage()

### func (*NotOutdoorsFailureDetails) ProtoReflect 
    
    
    func (x *NotOutdoorsFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NotOutdoorsFailureDetails) Reset 
    
    
    func (x *NotOutdoorsFailureDetails) Reset()

### func (*NotOutdoorsFailureDetails) String 
    
    
    func (x *NotOutdoorsFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## Photo
    
    
    type Photo struct {
    
    	// Required. Output only. Required when updating a photo. Output only when
    	// creating a photo. Identifier for the photo, which is unique among all
    	// photos in Google.
    	PhotoId *PhotoId `protobuf:"bytes,1,opt,name=photo_id,json=photoId,proto3" json:"photo_id,omitempty"`
    	// Input only. Required when creating a photo. Input only. The resource URL
    	// where the photo bytes are uploaded to.
    	UploadReference *UploadRef `protobuf:"bytes,2,opt,name=upload_reference,json=uploadReference,proto3" json:"upload_reference,omitempty"`
    	// Output only. The download URL for the photo bytes. This field is set only
    	// when
    	// [GetPhotoRequest.view][google.streetview.publish.v1.GetPhotoRequest.view]
    	// is set to
    	// [PhotoView.INCLUDE_DOWNLOAD_URL][google.streetview.publish.v1.PhotoView.INCLUDE_DOWNLOAD_URL].
    	DownloadUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=download_url,json=downloadUrl,proto3" json:"download_url,omitempty"`
    	// Output only. The thumbnail URL for showing a preview of the given photo.
    	ThumbnailUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=thumbnail_url,json=thumbnailUrl,proto3" json:"thumbnail_url,omitempty"`
    	// Output only. The share link for the photo.
    	ShareLink [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=share_link,json=shareLink,proto3" json:"share_link,omitempty"`
    	// Optional. Pose of the photo.
    	Pose *Pose `protobuf:"bytes,4,opt,name=pose,proto3" json:"pose,omitempty"`
    	// Optional. Connections to other photos. A connection represents the link
    	// from this photo to another photo.
    	Connections []*Connection `protobuf:"bytes,5,rep,name=connections,proto3" json:"connections,omitempty"`
    	// Optional. Absolute time when the photo was captured.
    	// When the photo has no exif timestamp, this is used to set a timestamp in
    	// the photo metadata.
    	CaptureTime *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=capture_time,json=captureTime,proto3" json:"capture_time,omitempty"`
    	// Output only. Time when the image was uploaded.
    	UploadTime *timestamppb.Timestamp `protobuf:"bytes,14,opt,name=upload_time,json=uploadTime,proto3" json:"upload_time,omitempty"`
    	// Optional. Places where this photo belongs.
    	Places []*Place `protobuf:"bytes,7,rep,name=places,proto3" json:"places,omitempty"`
    	// Output only. View count of the photo.
    	ViewCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,10,opt,name=view_count,json=viewCount,proto3" json:"view_count,omitempty"`
    	// Output only. Status of rights transfer on this photo.
    	TransferStatus Photo_TransferStatus `protobuf:"varint,12,opt,name=transfer_status,json=transferStatus,proto3,enum=google.streetview.publish.v1.Photo_TransferStatus" json:"transfer_status,omitempty"`
    	// Output only. Status in Google Maps, whether this photo was published or
    	// rejected.
    	MapsPublishStatus Photo_MapsPublishStatus `protobuf:"varint,13,opt,name=maps_publish_status,json=mapsPublishStatus,proto3,enum=google.streetview.publish.v1.Photo_MapsPublishStatus" json:"maps_publish_status,omitempty"`
    	// contains filtered or unexported fields
    }

Photo is used to store 360 photos along with photo metadata.

### func (*Photo) Descriptor 
    
    
    func (*Photo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Photo.ProtoReflect.Descriptor instead.

### func (*Photo) GetCaptureTime 
    
    
    func (x *Photo) GetCaptureTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Photo) GetConnections 
    
    
    func (x *Photo) GetConnections() []*Connection

### func (*Photo) GetDownloadUrl 
    
    
    func (x *Photo) GetDownloadUrl() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetMapsPublishStatus 
    
    
    func (x *Photo) GetMapsPublishStatus() Photo_MapsPublishStatus

### func (*Photo) GetPhotoId 
    
    
    func (x *Photo) GetPhotoId() *PhotoId

### func (*Photo) GetPlaces 
    
    
    func (x *Photo) GetPlaces() []*Place

### func (*Photo) GetPose 
    
    
    func (x *Photo) GetPose() *Pose

### func (*Photo) GetShareLink 
    
    
    func (x *Photo) GetShareLink() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetThumbnailUrl 
    
    
    func (x *Photo) GetThumbnailUrl() [string](https://pkg.go.dev/builtin#string)

### func (*Photo) GetTransferStatus 
    
    
    func (x *Photo) GetTransferStatus() Photo_TransferStatus

### func (*Photo) GetUploadReference 
    
    
    func (x *Photo) GetUploadReference() *UploadRef

### func (*Photo) GetUploadTime 
    
    
    func (x *Photo) GetUploadTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Photo) GetViewCount 
    
    
    func (x *Photo) GetViewCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*Photo) ProtoMessage 
    
    
    func (*Photo) ProtoMessage()

### func (*Photo) ProtoReflect 
    
    
    func (x *Photo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Photo) Reset 
    
    
    func (x *Photo) Reset()

### func (*Photo) String 
    
    
    func (x *Photo) String() [string](https://pkg.go.dev/builtin#string)

## PhotoId
    
    
    type PhotoId struct {
    
    	// A unique identifier for a photo.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// contains filtered or unexported fields
    }

Identifier for a [Photo][google.streetview.publish.v1.Photo].

### func (*PhotoId) Descriptor 
    
    
    func (*PhotoId) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoId.ProtoReflect.Descriptor instead.

### func (*PhotoId) GetId 
    
    
    func (x *PhotoId) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*PhotoId) ProtoMessage 
    
    
    func (*PhotoId) ProtoMessage()

### func (*PhotoId) ProtoReflect 
    
    
    func (x *PhotoId) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PhotoId) Reset 
    
    
    func (x *PhotoId) Reset()

### func (*PhotoId) String 
    
    
    func (x *PhotoId) String() [string](https://pkg.go.dev/builtin#string)

## PhotoResponse
    
    
    type PhotoResponse struct {
    
    	// The status for the operation to get or update a single photo in the batch
    	// request.
    	Status *status.Status `protobuf:"bytes,1,opt,name=status,proto3" json:"status,omitempty"`
    	// The [Photo][google.streetview.publish.v1.Photo] resource, if the request
    	// was successful.
    	Photo *Photo `protobuf:"bytes,2,opt,name=photo,proto3" json:"photo,omitempty"`
    	// contains filtered or unexported fields
    }

Response payload for a single [Photo][google.streetview.publish.v1.Photo] in batch operations including [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos] and [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos].

### func (*PhotoResponse) Descriptor 
    
    
    func (*PhotoResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoResponse.ProtoReflect.Descriptor instead.

### func (*PhotoResponse) GetPhoto 
    
    
    func (x *PhotoResponse) GetPhoto() *Photo

### func (*PhotoResponse) GetStatus 
    
    
    func (x *PhotoResponse) GetStatus() *[status](https://pkg.go.dev/google.golang.org/grpc/status).[Status](https://pkg.go.dev/google.golang.org/grpc/status#Status)

### func (*PhotoResponse) ProtoMessage 
    
    
    func (*PhotoResponse) ProtoMessage()

### func (*PhotoResponse) ProtoReflect 
    
    
    func (x *PhotoResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PhotoResponse) Reset 
    
    
    func (x *PhotoResponse) Reset()

### func (*PhotoResponse) String 
    
    
    func (x *PhotoResponse) String() [string](https://pkg.go.dev/builtin#string)

## PhotoSequence
    
    
    type PhotoSequence struct {
    
    	// Output only. Unique identifier for the photo sequence.
    	// This also acts as a long running operation ID if uploading is performed
    	// asynchronously.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// Output only. Photos with increasing timestamps.
    	Photos []*Photo `protobuf:"bytes,2,rep,name=photos,proto3" json:"photos,omitempty"`
    	// Input only. Required when creating photo sequence. The resource name
    	// where the bytes of the photo sequence (in the form of video) are uploaded.
    	UploadReference *UploadRef `protobuf:"bytes,3,opt,name=upload_reference,json=uploadReference,proto3" json:"upload_reference,omitempty"`
    	// Optional. Absolute time when the photo sequence starts to be captured.
    	// If the photo sequence is a video, this is the start time of the video.
    	// If this field is populated in input, it overrides the capture time in the
    	// video or XDM file.
    	CaptureTimeOverride *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=capture_time_override,json=captureTimeOverride,proto3" json:"capture_time_override,omitempty"`
    	// Output only. The time this photo sequence was created in uSV Store service.
    	UploadTime *timestamppb.Timestamp `protobuf:"bytes,18,opt,name=upload_time,json=uploadTime,proto3" json:"upload_time,omitempty"`
    	// Input only. Raw GPS measurements with increasing timestamps from the device
    	// that aren't time synced with each photo. These raw measurements will be
    	// used to infer the pose of each frame. Required in input when InputType is
    	// VIDEO and raw GPS measurements are not in Camera Motion Metadata Track
    	// (CAMM). User can indicate which takes precedence using gps_source if raw
    	// GPS measurements are provided in both raw_gps_timeline and Camera Motion
    	// Metadata Track (CAMM).
    	RawGpsTimeline []*Pose `protobuf:"bytes,7,rep,name=raw_gps_timeline,json=rawGpsTimeline,proto3" json:"raw_gps_timeline,omitempty"`
    	// Input only. If both raw_gps_timeline and
    	// the Camera Motion Metadata Track (CAMM) contain GPS measurements,
    	// indicate which takes precedence.
    	GpsSource PhotoSequence_GpsSource `protobuf:"varint,8,opt,name=gps_source,json=gpsSource,proto3,enum=google.streetview.publish.v1.PhotoSequence_GpsSource" json:"gps_source,omitempty"`
    	// Input only. Three axis IMU data for the collection.
    	// If this data is too large to put in the request, then it should be put in
    	// the CAMM track for the video. This data always takes precedence over the
    	// equivalent CAMM data, if it exists.
    	Imu *Imu `protobuf:"bytes,11,opt,name=imu,proto3" json:"imu,omitempty"`
    	// Output only. The processing state of this sequence.
    	ProcessingState ProcessingState `protobuf:"varint,12,opt,name=processing_state,json=processingState,proto3,enum=google.streetview.publish.v1.ProcessingState" json:"processing_state,omitempty"`
    	// Output only. If this sequence has processing_state = FAILED, this will
    	// contain the reason why it failed. If the processing_state is any other
    	// value, this field will be unset.
    	FailureReason ProcessingFailureReason `protobuf:"varint,13,opt,name=failure_reason,json=failureReason,proto3,enum=google.streetview.publish.v1.ProcessingFailureReason" json:"failure_reason,omitempty"`
    	// Output only. If this sequence has `failure_reason` set, this may contain
    	// additional details about the failure.
    	FailureDetails *ProcessingFailureDetails `protobuf:"bytes,23,opt,name=failure_details,json=failureDetails,proto3" json:"failure_details,omitempty"`
    	// Output only. The computed distance of the photo sequence in meters.
    	DistanceMeters [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,16,opt,name=distance_meters,json=distanceMeters,proto3" json:"distance_meters,omitempty"`
    	// Output only. A rectangular box that encapsulates every image in this photo
    	// sequence.
    	SequenceBounds *LatLngBounds `protobuf:"bytes,20,opt,name=sequence_bounds,json=sequenceBounds,proto3" json:"sequence_bounds,omitempty"`
    	// Output only. The total number of views that all the published images in
    	// this PhotoSequence have received.
    	ViewCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,21,opt,name=view_count,json=viewCount,proto3" json:"view_count,omitempty"`
    	// Output only. The filename of the upload. Does not include the directory
    	// path. Only available if the sequence was uploaded on a platform that
    	// provides the filename.
    	Filename [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,22,opt,name=filename,proto3" json:"filename,omitempty"`
    	// contains filtered or unexported fields
    }

A sequence of 360 photos along with metadata.

### func (*PhotoSequence) Descriptor 
    
    
    func (*PhotoSequence) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoSequence.ProtoReflect.Descriptor instead.

### func (*PhotoSequence) GetCaptureTimeOverride 
    
    
    func (x *PhotoSequence) GetCaptureTimeOverride() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*PhotoSequence) GetDistanceMeters 
    
    
    func (x *PhotoSequence) GetDistanceMeters() [float64](https://pkg.go.dev/builtin#float64)

### func (*PhotoSequence) GetFailureDetails 
    
    
    func (x *PhotoSequence) GetFailureDetails() *ProcessingFailureDetails

### func (*PhotoSequence) GetFailureReason 
    
    
    func (x *PhotoSequence) GetFailureReason() ProcessingFailureReason

### func (*PhotoSequence) GetFilename 
    
    
    func (x *PhotoSequence) GetFilename() [string](https://pkg.go.dev/builtin#string)

### func (*PhotoSequence) GetGpsSource 
    
    
    func (x *PhotoSequence) GetGpsSource() PhotoSequence_GpsSource

### func (*PhotoSequence) GetId 
    
    
    func (x *PhotoSequence) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*PhotoSequence) GetImu 
    
    
    func (x *PhotoSequence) GetImu() *Imu

### func (*PhotoSequence) GetPhotos 
    
    
    func (x *PhotoSequence) GetPhotos() []*Photo

### func (*PhotoSequence) GetProcessingState 
    
    
    func (x *PhotoSequence) GetProcessingState() ProcessingState

### func (*PhotoSequence) GetRawGpsTimeline 
    
    
    func (x *PhotoSequence) GetRawGpsTimeline() []*Pose

### func (*PhotoSequence) GetSequenceBounds 
    
    
    func (x *PhotoSequence) GetSequenceBounds() *LatLngBounds

### func (*PhotoSequence) GetUploadReference 
    
    
    func (x *PhotoSequence) GetUploadReference() *UploadRef

### func (*PhotoSequence) GetUploadTime 
    
    
    func (x *PhotoSequence) GetUploadTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*PhotoSequence) GetViewCount 
    
    
    func (x *PhotoSequence) GetViewCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*PhotoSequence) ProtoMessage 
    
    
    func (*PhotoSequence) ProtoMessage()

### func (*PhotoSequence) ProtoReflect 
    
    
    func (x *PhotoSequence) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PhotoSequence) Reset 
    
    
    func (x *PhotoSequence) Reset()

### func (*PhotoSequence) String 
    
    
    func (x *PhotoSequence) String() [string](https://pkg.go.dev/builtin#string)

## PhotoSequence_GpsSource
    
    
    type PhotoSequence_GpsSource [int32](https://pkg.go.dev/builtin#int32)

Primary source of GPS measurements.

### PhotoSequence_PHOTO_SEQUENCE, PhotoSequence_CAMERA_MOTION_METADATA_TRACK
    
    
    const (
    	// GPS in raw_gps_timeline takes precedence if it exists.
    	PhotoSequence_PHOTO_SEQUENCE PhotoSequence_GpsSource = 0
    	// GPS in Camera Motion Metadata Track (CAMM) takes precedence if it exists.
    	PhotoSequence_CAMERA_MOTION_METADATA_TRACK PhotoSequence_GpsSource = 1
    )

### func (PhotoSequence_GpsSource) Descriptor 
    
    
    func (PhotoSequence_GpsSource) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PhotoSequence_GpsSource) Enum 
    
    
    func (x PhotoSequence_GpsSource) Enum() *PhotoSequence_GpsSource

### func (PhotoSequence_GpsSource) EnumDescriptor 
    
    
    func (PhotoSequence_GpsSource) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoSequence_GpsSource.Descriptor instead.

### func (PhotoSequence_GpsSource) Number 
    
    
    func (x PhotoSequence_GpsSource) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PhotoSequence_GpsSource) String 
    
    
    func (x PhotoSequence_GpsSource) String() [string](https://pkg.go.dev/builtin#string)

### func (PhotoSequence_GpsSource) Type 
    
    
    func (PhotoSequence_GpsSource) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## PhotoView
    
    
    type PhotoView [int32](https://pkg.go.dev/builtin#int32)

Specifies which view of the [Photo][google.streetview.publish.v1.Photo] to include in the response.

### PhotoView_BASIC, PhotoView_INCLUDE_DOWNLOAD_URL
    
    
    const (
    	// Server responses do not include the download URL for the photo bytes.
    	// The default value.
    	PhotoView_BASIC PhotoView = 0
    	// Server responses include the download URL for the photo bytes.
    	PhotoView_INCLUDE_DOWNLOAD_URL PhotoView = 1
    )

### func (PhotoView) Descriptor 
    
    
    func (PhotoView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PhotoView) Enum 
    
    
    func (x PhotoView) Enum() *PhotoView

### func (PhotoView) EnumDescriptor 
    
    
    func (PhotoView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhotoView.Descriptor instead.

### func (PhotoView) Number 
    
    
    func (x PhotoView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PhotoView) String 
    
    
    func (x PhotoView) String() [string](https://pkg.go.dev/builtin#string)

### func (PhotoView) Type 
    
    
    func (PhotoView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Photo_MapsPublishStatus
    
    
    type Photo_MapsPublishStatus [int32](https://pkg.go.dev/builtin#int32)

Publication status of the photo in Google Maps.

### Photo_UNSPECIFIED_MAPS_PUBLISH_STATUS, Photo_PUBLISHED, Photo_REJECTED_UNKNOWN
    
    
    const (
    	// The status of the photo is unknown.
    	Photo_UNSPECIFIED_MAPS_PUBLISH_STATUS Photo_MapsPublishStatus = 0
    	// The photo is published to the public through Google Maps.
    	Photo_PUBLISHED Photo_MapsPublishStatus = 1
    	// The photo has been rejected for an unknown reason.
    	Photo_REJECTED_UNKNOWN Photo_MapsPublishStatus = 2
    )

### func (Photo_MapsPublishStatus) Descriptor 
    
    
    func (Photo_MapsPublishStatus) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Photo_MapsPublishStatus) Enum 
    
    
    func (x Photo_MapsPublishStatus) Enum() *Photo_MapsPublishStatus

### func (Photo_MapsPublishStatus) EnumDescriptor 
    
    
    func (Photo_MapsPublishStatus) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Photo_MapsPublishStatus.Descriptor instead.

### func (Photo_MapsPublishStatus) Number 
    
    
    func (x Photo_MapsPublishStatus) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Photo_MapsPublishStatus) String 
    
    
    func (x Photo_MapsPublishStatus) String() [string](https://pkg.go.dev/builtin#string)

### func (Photo_MapsPublishStatus) Type 
    
    
    func (Photo_MapsPublishStatus) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Photo_TransferStatus
    
    
    type Photo_TransferStatus [int32](https://pkg.go.dev/builtin#int32)

Status of rights transfer.

### Photo_TRANSFER_STATUS_UNKNOWN, Photo_NEVER_TRANSFERRED, Photo_PENDING, Photo_COMPLETED, Photo_REJECTED, Photo_EXPIRED, Photo_CANCELLED, Photo_RECEIVED_VIA_TRANSFER
    
    
    const (
    	// The status of this transfer is unspecified.
    	Photo_TRANSFER_STATUS_UNKNOWN Photo_TransferStatus = 0
    	// This photo has never been in a transfer.
    	Photo_NEVER_TRANSFERRED Photo_TransferStatus = 1
    	// This photo transfer has been initiated, but the receiver has not yet
    	// responded.
    	Photo_PENDING Photo_TransferStatus = 2
    	// The photo transfer has been completed, and this photo has been
    	// transferred to the recipient.
    	Photo_COMPLETED Photo_TransferStatus = 3
    	// The recipient rejected this photo transfer.
    	Photo_REJECTED Photo_TransferStatus = 4
    	// The photo transfer expired before the recipient took any action.
    	Photo_EXPIRED Photo_TransferStatus = 5
    	// The sender cancelled this photo transfer.
    	Photo_CANCELLED Photo_TransferStatus = 6
    	// The recipient owns this photo due to a rights transfer.
    	Photo_RECEIVED_VIA_TRANSFER Photo_TransferStatus = 7
    )

### func (Photo_TransferStatus) Descriptor 
    
    
    func (Photo_TransferStatus) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Photo_TransferStatus) Enum 
    
    
    func (x Photo_TransferStatus) Enum() *Photo_TransferStatus

### func (Photo_TransferStatus) EnumDescriptor 
    
    
    func (Photo_TransferStatus) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Photo_TransferStatus.Descriptor instead.

### func (Photo_TransferStatus) Number 
    
    
    func (x Photo_TransferStatus) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Photo_TransferStatus) String 
    
    
    func (x Photo_TransferStatus) String() [string](https://pkg.go.dev/builtin#string)

### func (Photo_TransferStatus) Type 
    
    
    func (Photo_TransferStatus) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Place
    
    
    type Place struct {
    
    	// Place identifier, as described in
    	// https://developers.google.com/places/place-id.
    	PlaceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=place_id,json=placeId,proto3" json:"place_id,omitempty"`
    	// Output only. The name of the place, localized to the language_code.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The language_code that the name is localized with. This should
    	// be the language_code specified in the request, but may be a fallback.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// contains filtered or unexported fields
    }

Place metadata for an entity.

### func (*Place) Descriptor 
    
    
    func (*Place) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Place.ProtoReflect.Descriptor instead.

### func (*Place) GetLanguageCode 
    
    
    func (x *Place) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetName 
    
    
    func (x *Place) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Place) GetPlaceId 
    
    
    func (x *Place) GetPlaceId() [string](https://pkg.go.dev/builtin#string)

### func (*Place) ProtoMessage 
    
    
    func (*Place) ProtoMessage()

### func (*Place) ProtoReflect 
    
    
    func (x *Place) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Place) Reset 
    
    
    func (x *Place) Reset()

### func (*Place) String 
    
    
    func (x *Place) String() [string](https://pkg.go.dev/builtin#string)

## Pose
    
    
    type Pose struct {
    
    	// Latitude and longitude pair of the pose, as explained here:
    	// https://cloud.google.com/datastore/docs/reference/rest/Shared.Types/LatLng
    	// When creating a [Photo][google.streetview.publish.v1.Photo], if the
    	// latitude and longitude pair are not provided, the geolocation from the
    	// exif header is used. A latitude and longitude pair not provided in the
    	// photo or exif header causes the photo process to fail.
    	LatLngPair *latlng.LatLng `protobuf:"bytes,1,opt,name=lat_lng_pair,json=latLngPair,proto3" json:"lat_lng_pair,omitempty"`
    	// Altitude of the pose in meters above WGS84 ellipsoid.
    	// NaN indicates an unmeasured quantity.
    	Altitude [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=altitude,proto3" json:"altitude,omitempty"`
    	// The following pose parameters pertain to the center of the photo. They
    	// match https://developers.google.com/streetview/spherical-metadata.
    	// Compass heading, measured at the center of the photo in degrees clockwise
    	// from North. Value must be >=0 and <360. nan="" indicates="" an="" unmeasured="" quantity.="" heading="">[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=heading,proto3" json:"heading,omitempty"`
    	// Pitch, measured at the center of the photo in degrees. Value must be >=-90
    	// and <= 90.="" a="" value="" of="" -90="" means="" looking="" directly="" down,="" and="" a="" value="" of="" 90="" means="" looking="" directly="" up.="" nan="" indicates="" an="" unmeasured="" quantity.="" pitch="">[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,4,opt,name=pitch,proto3" json:"pitch,omitempty"`
    	// Roll, measured in degrees. Value must be >= 0 and <360. a="" value="" of="" 0="" means="" level="" with="" the="" horizon.="" nan="" indicates="" an="" unmeasured="" quantity.="" roll="">[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,5,opt,name=roll,proto3" json:"roll,omitempty"`
    	// Time of the GPS record since UTC epoch.
    	GpsRecordTimestampUnixEpoch *timestamppb.Timestamp `protobuf:"bytes,6,opt,name=gps_record_timestamp_unix_epoch,json=gpsRecordTimestampUnixEpoch,proto3" json:"gps_record_timestamp_unix_epoch,omitempty"`
    	// Level (the floor in a building) used to configure vertical navigation.
    	Level *Level `protobuf:"bytes,7,opt,name=level,proto3" json:"level,omitempty"`
    	// The estimated horizontal accuracy of this pose in meters with 68%
    	// confidence (one standard deviation). For example, on Android, this value is
    	// available from this method:
    	// https://developer.android.com/reference/android/location/Location#getAccuracy().
    	// Other platforms have different methods of obtaining similar accuracy
    	// estimations.
    	AccuracyMeters [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,9,opt,name=accuracy_meters,json=accuracyMeters,proto3" json:"accuracy_meters,omitempty"`
    	// contains filtered or unexported fields
    }

Raw pose measurement for an entity.

### func (*Pose) Descriptor 
    
    
    func (*Pose) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Pose.ProtoReflect.Descriptor instead.

### func (*Pose) GetAccuracyMeters 
    
    
    func (x *Pose) GetAccuracyMeters() [float32](https://pkg.go.dev/builtin#float32)

### func (*Pose) GetAltitude 
    
    
    func (x *Pose) GetAltitude() [float64](https://pkg.go.dev/builtin#float64)

### func (*Pose) GetGpsRecordTimestampUnixEpoch 
    
    
    func (x *Pose) GetGpsRecordTimestampUnixEpoch() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Pose) GetHeading 
    
    
    func (x *Pose) GetHeading() [float64](https://pkg.go.dev/builtin#float64)

### func (*Pose) GetLatLngPair 
    
    
    func (x *Pose) GetLatLngPair() *[latlng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng).[LatLng](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/latlng#LatLng)

### func (*Pose) GetLevel 
    
    
    func (x *Pose) GetLevel() *Level

### func (*Pose) GetPitch 
    
    
    func (x *Pose) GetPitch() [float64](https://pkg.go.dev/builtin#float64)

### func (*Pose) GetRoll 
    
    
    func (x *Pose) GetRoll() [float64](https://pkg.go.dev/builtin#float64)

### func (*Pose) ProtoMessage 
    
    
    func (*Pose) ProtoMessage()

### func (*Pose) ProtoReflect 
    
    
    func (x *Pose) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Pose) Reset 
    
    
    func (x *Pose) Reset()

### func (*Pose) String 
    
    
    func (x *Pose) String() [string](https://pkg.go.dev/builtin#string)

## ProcessingFailureDetails
    
    
    type ProcessingFailureDetails struct {
    
    	// Only one set of details will be set, and must match the corresponding enum
    	// in ProcessingFailureReason.
    	//
    	// Types that are valid to be assigned to Details:
    	//
    	//	*ProcessingFailureDetails_InsufficientGpsDetails
    	//	*ProcessingFailureDetails_GpsDataGapDetails
    	//	*ProcessingFailureDetails_ImuDataGapDetails
    	//	*ProcessingFailureDetails_NotOutdoorsDetails
    	//	*ProcessingFailureDetails_NoOverlapGpsDetails
    	Details isProcessingFailureDetails_Details `protobuf_oneof:"details"`
    	// contains filtered or unexported fields
    }

Additional details to accompany the ProcessingFailureReason enum. This message is always expected to be used in conjunction with ProcessingFailureReason, and the oneof value set in this message should match the FailureReason.

### func (*ProcessingFailureDetails) Descriptor 
    
    
    func (*ProcessingFailureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ProcessingFailureDetails.ProtoReflect.Descriptor instead.

### func (*ProcessingFailureDetails) GetDetails 
    
    
    func (x *ProcessingFailureDetails) GetDetails() isProcessingFailureDetails_Details

### func (*ProcessingFailureDetails) GetGpsDataGapDetails 
    
    
    func (x *ProcessingFailureDetails) GetGpsDataGapDetails() *GpsDataGapFailureDetails

### func (*ProcessingFailureDetails) GetImuDataGapDetails 
    
    
    func (x *ProcessingFailureDetails) GetImuDataGapDetails() *ImuDataGapFailureDetails

### func (*ProcessingFailureDetails) GetInsufficientGpsDetails 
    
    
    func (x *ProcessingFailureDetails) GetInsufficientGpsDetails() *InsufficientGpsFailureDetails

### func (*ProcessingFailureDetails) GetNoOverlapGpsDetails 
    
    
    func (x *ProcessingFailureDetails) GetNoOverlapGpsDetails() *NoOverlapGpsFailureDetails

### func (*ProcessingFailureDetails) GetNotOutdoorsDetails 
    
    
    func (x *ProcessingFailureDetails) GetNotOutdoorsDetails() *NotOutdoorsFailureDetails

### func (*ProcessingFailureDetails) ProtoMessage 
    
    
    func (*ProcessingFailureDetails) ProtoMessage()

### func (*ProcessingFailureDetails) ProtoReflect 
    
    
    func (x *ProcessingFailureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ProcessingFailureDetails) Reset 
    
    
    func (x *ProcessingFailureDetails) Reset()

### func (*ProcessingFailureDetails) String 
    
    
    func (x *ProcessingFailureDetails) String() [string](https://pkg.go.dev/builtin#string)

## ProcessingFailureDetails_GpsDataGapDetails
    
    
    type ProcessingFailureDetails_GpsDataGapDetails struct {
    	// See GpsDataGapFailureDetails.
    	GpsDataGapDetails *GpsDataGapFailureDetails `protobuf:"bytes,2,opt,name=gps_data_gap_details,json=gpsDataGapDetails,proto3,oneof"`
    }

## ProcessingFailureDetails_ImuDataGapDetails
    
    
    type ProcessingFailureDetails_ImuDataGapDetails struct {
    	// See ImuDataGapFailureDetails.
    	ImuDataGapDetails *ImuDataGapFailureDetails `protobuf:"bytes,3,opt,name=imu_data_gap_details,json=imuDataGapDetails,proto3,oneof"`
    }

## ProcessingFailureDetails_InsufficientGpsDetails
    
    
    type ProcessingFailureDetails_InsufficientGpsDetails struct {
    	// See InsufficientGpsFailureDetails.
    	InsufficientGpsDetails *InsufficientGpsFailureDetails `protobuf:"bytes,1,opt,name=insufficient_gps_details,json=insufficientGpsDetails,proto3,oneof"`
    }

## ProcessingFailureDetails_NoOverlapGpsDetails
    
    
    type ProcessingFailureDetails_NoOverlapGpsDetails struct {
    	// See NoOverlapGpsFailureDetails.
    	NoOverlapGpsDetails *NoOverlapGpsFailureDetails `protobuf:"bytes,5,opt,name=no_overlap_gps_details,json=noOverlapGpsDetails,proto3,oneof"`
    }

## ProcessingFailureDetails_NotOutdoorsDetails
    
    
    type ProcessingFailureDetails_NotOutdoorsDetails struct {
    	// See NotOutdoorsFailureDetails.
    	NotOutdoorsDetails *NotOutdoorsFailureDetails `protobuf:"bytes,4,opt,name=not_outdoors_details,json=notOutdoorsDetails,proto3,oneof"`
    }

## ProcessingFailureReason
    
    
    type ProcessingFailureReason [int32](https://pkg.go.dev/builtin#int32)

The possible reasons this [PhotoSequence] [google.streetview.publish.v1.PhotoSequence] failed to process.

### ProcessingFailureReason_PROCESSING_FAILURE_REASON_UNSPECIFIED, ProcessingFailureReason_LOW_RESOLUTION, ProcessingFailureReason_DUPLICATE, ProcessingFailureReason_INSUFFICIENT_GPS, ProcessingFailureReason_NO_OVERLAP_GPS, ProcessingFailureReason_INVALID_GPS, ProcessingFailureReason_FAILED_TO_REFINE_POSITIONS, ProcessingFailureReason_TAKEDOWN, ProcessingFailureReason_CORRUPT_VIDEO, ProcessingFailureReason_INTERNAL, ProcessingFailureReason_INVALID_VIDEO_FORMAT, ProcessingFailureReason_INVALID_VIDEO_DIMENSIONS, ProcessingFailureReason_INVALID_CAPTURE_TIME, ProcessingFailureReason_GPS_DATA_GAP, ProcessingFailureReason_JUMPY_GPS, ProcessingFailureReason_INVALID_IMU, ProcessingFailureReason_INSUFFICIENT_IMU, ProcessingFailureReason_INSUFFICIENT_OVERLAP_TIME_SERIES, ProcessingFailureReason_IMU_DATA_GAP, ProcessingFailureReason_UNSUPPORTED_CAMERA, ProcessingFailureReason_NOT_OUTDOORS, ProcessingFailureReason_INSUFFICIENT_VIDEO_FRAMES, ProcessingFailureReason_INSUFFICIENT_MOVEMENT, ProcessingFailureReason_MAST_DOWN, ProcessingFailureReason_CAMERA_COVERED
    
    
    const (
    	// The failure reason is unspecified, this is the default value.
    	ProcessingFailureReason_PROCESSING_FAILURE_REASON_UNSPECIFIED ProcessingFailureReason = 0
    	// Video frame's resolution is too small.
    	ProcessingFailureReason_LOW_RESOLUTION ProcessingFailureReason = 1
    	// This video has been uploaded before.
    	ProcessingFailureReason_DUPLICATE ProcessingFailureReason = 2
    	// Too few GPS points.
    	ProcessingFailureReason_INSUFFICIENT_GPS ProcessingFailureReason = 3
    	// No overlap between the time frame of GPS track and the time frame of
    	// video.
    	ProcessingFailureReason_NO_OVERLAP_GPS ProcessingFailureReason = 4
    	// GPS is invalid (e.x. all GPS points are at (0,0))
    	ProcessingFailureReason_INVALID_GPS ProcessingFailureReason = 5
    	// The sequence of photos could not be accurately located in the world.
    	ProcessingFailureReason_FAILED_TO_REFINE_POSITIONS ProcessingFailureReason = 6
    	// The sequence was taken down for policy reasons.
    	ProcessingFailureReason_TAKEDOWN ProcessingFailureReason = 7
    	// The video file was corrupt or could not be decoded.
    	ProcessingFailureReason_CORRUPT_VIDEO ProcessingFailureReason = 8
    	// A permanent failure in the underlying system occurred.
    	ProcessingFailureReason_INTERNAL ProcessingFailureReason = 9
    	// The video format is invalid or unsupported.
    	ProcessingFailureReason_INVALID_VIDEO_FORMAT ProcessingFailureReason = 10
    	// Invalid image aspect ratio found.
    	ProcessingFailureReason_INVALID_VIDEO_DIMENSIONS ProcessingFailureReason = 11
    	// Invalid capture time. Timestamps were from the future.
    	ProcessingFailureReason_INVALID_CAPTURE_TIME ProcessingFailureReason = 12
    	// GPS data contains a gap greater than 5 seconds in duration.
    	ProcessingFailureReason_GPS_DATA_GAP ProcessingFailureReason = 13
    	// GPS data is too erratic to be processed.
    	ProcessingFailureReason_JUMPY_GPS ProcessingFailureReason = 14
    	// IMU (Accelerometer, Gyroscope, etc.) data are not valid. They may be
    	// missing required fields (x, y, z or time), may not be formatted correctly,
    	// or any other issue that prevents our systems from parsing it.
    	ProcessingFailureReason_INVALID_IMU ProcessingFailureReason = 15
    	// Too few IMU points.
    	ProcessingFailureReason_INSUFFICIENT_IMU ProcessingFailureReason = 21
    	// Insufficient overlap in the time frame between GPS, IMU, and other time
    	// series data.
    	ProcessingFailureReason_INSUFFICIENT_OVERLAP_TIME_SERIES ProcessingFailureReason = 22
    	// IMU (Accelerometer, Gyroscope, etc.) data contain gaps greater than 0.1
    	// seconds in duration.
    	ProcessingFailureReason_IMU_DATA_GAP ProcessingFailureReason = 16
    	// The camera is not supported.
    	ProcessingFailureReason_UNSUPPORTED_CAMERA ProcessingFailureReason = 17
    	// Some frames were indoors, which is unsupported.
    	ProcessingFailureReason_NOT_OUTDOORS ProcessingFailureReason = 18
    	// Not enough video frames.
    	ProcessingFailureReason_INSUFFICIENT_VIDEO_FRAMES ProcessingFailureReason = 19
    	// Not enough moving data.
    	ProcessingFailureReason_INSUFFICIENT_MOVEMENT ProcessingFailureReason = 20
    	// Mast is down.
    	ProcessingFailureReason_MAST_DOWN ProcessingFailureReason = 27
    	// Camera is covered.
    	ProcessingFailureReason_CAMERA_COVERED ProcessingFailureReason = 28
    )

### func (ProcessingFailureReason) Descriptor 
    
    
    func (ProcessingFailureReason) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ProcessingFailureReason) Enum 
    
    
    func (x ProcessingFailureReason) Enum() *ProcessingFailureReason

### func (ProcessingFailureReason) EnumDescriptor 
    
    
    func (ProcessingFailureReason) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ProcessingFailureReason.Descriptor instead.

### func (ProcessingFailureReason) Number 
    
    
    func (x ProcessingFailureReason) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ProcessingFailureReason) String 
    
    
    func (x ProcessingFailureReason) String() [string](https://pkg.go.dev/builtin#string)

### func (ProcessingFailureReason) Type 
    
    
    func (ProcessingFailureReason) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ProcessingState
    
    
    type ProcessingState [int32](https://pkg.go.dev/builtin#int32)

The processing state of the sequence. The states move as follows:
    
    
            +-------------------------+
            |                         |
        +---v---+  +----------+  +----+----+
        |PENDING+-->PROCESSING+-->PROCESSED|
        +---+---+  +----+-----+  +----+----+
            |           |             |
            |        +--v---+         |
            +-------->FAILED<---------+
                     +------+
    

The sequence may move to FAILED from any state. Additionally, a processed sequence may be re-processed at any time.

### ProcessingState_PROCESSING_STATE_UNSPECIFIED, ProcessingState_PENDING, ProcessingState_PROCESSING, ProcessingState_PROCESSED, ProcessingState_FAILED
    
    
    const (
    	// The state is unspecified, this is the default value.
    	ProcessingState_PROCESSING_STATE_UNSPECIFIED ProcessingState = 0
    	// The sequence has not yet started processing.
    	ProcessingState_PENDING ProcessingState = 1
    	// The sequence is currently in processing.
    	ProcessingState_PROCESSING ProcessingState = 2
    	// The sequence has finished processing including refining position.
    	ProcessingState_PROCESSED ProcessingState = 3
    	// The sequence failed processing. See FailureReason for more details.
    	ProcessingState_FAILED ProcessingState = 4
    )

### func (ProcessingState) Descriptor 
    
    
    func (ProcessingState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ProcessingState) Enum 
    
    
    func (x ProcessingState) Enum() *ProcessingState

### func (ProcessingState) EnumDescriptor 
    
    
    func (ProcessingState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ProcessingState.Descriptor instead.

### func (ProcessingState) Number 
    
    
    func (x ProcessingState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ProcessingState) String 
    
    
    func (x ProcessingState) String() [string](https://pkg.go.dev/builtin#string)

### func (ProcessingState) Type 
    
    
    func (ProcessingState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## StreetViewPublishServiceClient
    
    
    type StreetViewPublishServiceClient interface {
    	// Creates an upload session to start uploading photo bytes.  The method uses
    	// the upload URL of the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef] to upload the bytes for
    	// the [Photo][google.streetview.publish.v1.Photo].
    	//
    	// In addition to the photo requirements shown in
    	// https://support.google.com/maps/answer/7012050?ref_topic=6275604,
    	// the photo must meet the following requirements:
    	//
    	// * Photo Sphere XMP metadata must be included in the photo metadata. See
    	// https://developers.google.com/streetview/spherical-metadata for the
    	// required fields.
    	// * The pixel size of the photo must meet the size requirements listed in
    	// https://support.google.com/maps/answer/7012050?ref_topic=6275604, and
    	// the photo must be a full 360 horizontally.
    	//
    	// After the upload completes, the method uses
    	// [UploadRef][google.streetview.publish.v1.UploadRef] with
    	// [CreatePhoto][google.streetview.publish.v1.StreetViewPublishService.CreatePhoto]
    	// to create the [Photo][google.streetview.publish.v1.Photo] object entry.
    	StartUpload(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*UploadRef, [error](https://pkg.go.dev/builtin#error))
    	// After the client finishes uploading the photo with the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef],
    	// [CreatePhoto][google.streetview.publish.v1.StreetViewPublishService.CreatePhoto]
    	// publishes the uploaded [Photo][google.streetview.publish.v1.Photo] to
    	// Street View on Google Maps.
    	//
    	// Currently, the only way to set heading, pitch, and roll in CreatePhoto is
    	// through the [Photo Sphere XMP
    	// metadata](https://developers.google.com/streetview/spherical-metadata) in
    	// the photo bytes. CreatePhoto ignores the  `pose.heading`, `pose.pitch`,
    	// `pose.roll`, `pose.altitude`, and `pose.level` fields in Pose.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed or if the uploaded photo is not a 360 photo.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the upload
    	// reference does not exist.
    	// * [google.rpc.Code.RESOURCE_EXHAUSTED][google.rpc.Code.RESOURCE_EXHAUSTED]
    	// if the account has reached the storage limit.
    	CreatePhoto(ctx context.Context, in *CreatePhotoRequest, opts ...grpc.CallOption) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [Photo][google.streetview.publish.v1.Photo].
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested
    	// [Photo][google.streetview.publish.v1.Photo].
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// [Photo][google.streetview.publish.v1.Photo] does not exist.
    	// * [google.rpc.Code.UNAVAILABLE][google.rpc.Code.UNAVAILABLE] if the
    	// requested [Photo][google.streetview.publish.v1.Photo] is still being
    	// indexed.
    	GetPhoto(ctx context.Context, in *GetPhotoRequest, opts ...grpc.CallOption) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [Photo][google.streetview.publish.v1.Photo] batch.
    	//
    	// Note that if
    	// [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchGetPhotosResponse.results][google.streetview.publish.v1.BatchGetPhotosResponse.results].
    	// See
    	// [GetPhoto][google.streetview.publish.v1.StreetViewPublishService.GetPhoto]
    	// for specific failures that can occur per photo.
    	BatchGetPhotos(ctx context.Context, in *BatchGetPhotosRequest, opts ...grpc.CallOption) (*BatchGetPhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the [Photos][google.streetview.publish.v1.Photo] that belong to
    	// the user.
    	//
    	// > Note: Recently created photos that are still
    	// being indexed are not returned in the response.
    	ListPhotos(ctx context.Context, in *ListPhotosRequest, opts ...grpc.CallOption) (*ListPhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates the metadata of a [Photo][google.streetview.publish.v1.Photo], such
    	// as pose, place association, connections, etc. Changing the pixels of a
    	// photo is not supported.
    	//
    	// Only the fields specified in the
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// field are used. If `updateMask` is not present, the update applies to all
    	// fields.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo.
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// photo does not exist.
    	// * [google.rpc.Code.UNAVAILABLE][google.rpc.Code.UNAVAILABLE] if the
    	// requested [Photo][google.streetview.publish.v1.Photo] is still being
    	// indexed.
    	UpdatePhoto(ctx context.Context, in *UpdatePhotoRequest, opts ...grpc.CallOption) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Updates the metadata of [Photos][google.streetview.publish.v1.Photo], such
    	// as pose, place association, connections, etc. Changing the pixels of photos
    	// is not supported.
    	//
    	// Note that if
    	// [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchUpdatePhotosResponse.results][google.streetview.publish.v1.BatchUpdatePhotosResponse.results].
    	// See
    	// [UpdatePhoto][google.streetview.publish.v1.StreetViewPublishService.UpdatePhoto]
    	// for specific failures that can occur per photo.
    	//
    	// Only the fields specified in
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// field are used. If `updateMask` is not present, the update applies to all
    	// fields.
    	//
    	// The number of
    	// [UpdatePhotoRequest][google.streetview.publish.v1.UpdatePhotoRequest]
    	// messages in a
    	// [BatchUpdatePhotosRequest][google.streetview.publish.v1.BatchUpdatePhotosRequest]
    	// must not exceed 20.
    	//
    	// > Note: To update
    	// [Pose.altitude][google.streetview.publish.v1.Pose.altitude],
    	// [Pose.latLngPair][google.streetview.publish.v1.Pose.lat_lng_pair] has to be
    	// filled as well. Otherwise, the request will fail.
    	BatchUpdatePhotos(ctx context.Context, in *BatchUpdatePhotosRequest, opts ...grpc.CallOption) (*BatchUpdatePhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a [Photo][google.streetview.publish.v1.Photo] and its metadata.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the photo ID
    	// does not exist.
    	DeletePhoto(ctx context.Context, in *DeletePhotoRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a list of [Photos][google.streetview.publish.v1.Photo] and their
    	// metadata.
    	//
    	// Note that if
    	// [BatchDeletePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchDeletePhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchDeletePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchDeletePhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchDeletePhotosResponse.results][google.streetview.publish.v1.BatchDeletePhotosResponse.status].
    	// See
    	// [DeletePhoto][google.streetview.publish.v1.StreetViewPublishService.DeletePhoto]
    	// for specific failures that can occur per photo.
    	BatchDeletePhotos(ctx context.Context, in *BatchDeletePhotosRequest, opts ...grpc.CallOption) (*BatchDeletePhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an upload session to start uploading photo sequence data.
    	// The upload URL of the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef] is used to upload the
    	// data for the `photoSequence`.
    	//
    	// After the upload is complete, the
    	// [UploadRef][google.streetview.publish.v1.UploadRef] is used with
    	// [CreatePhotoSequence][google.streetview.publish.v1.StreetViewPublishService.CreatePhotoSequence]
    	// to create the [PhotoSequence][google.streetview.publish.v1.PhotoSequence]
    	// object entry.
    	StartPhotoSequenceUpload(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*UploadRef, [error](https://pkg.go.dev/builtin#error))
    	// After the client finishes uploading the
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] with the
    	// returned [UploadRef][google.streetview.publish.v1.UploadRef],
    	// [CreatePhotoSequence][google.streetview.publish.v1.StreetViewPublishService.CreatePhotoSequence]
    	// extracts a sequence of 360 photos from a video or Extensible Device
    	// Metadata (XDM, http://www.xdm.org/) to be published to Street View on
    	// Google Maps.
    	//
    	// `CreatePhotoSequence` returns an [Operation][google.longrunning.Operation],
    	// with the [PhotoSequence][google.streetview.publish.v1.PhotoSequence] Id set
    	// in the `Operation.name` field.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the upload
    	// reference does not exist.
    	CreatePhotoSequence(ctx context.Context, in *CreatePhotoSequenceRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] via the
    	// [Operation][google.longrunning.Operation] interface.
    	//
    	// This method returns the following three types of responses:
    	//
    	//   - `Operation.done` = false, if the processing of
    	//     [PhotoSequence][google.streetview.publish.v1.PhotoSequence] is not
    	//     finished yet.
    	//   - `Operation.done` = true and `Operation.error` is populated, if there was
    	//     an error in processing.
    	//   - `Operation.done` = true and `Operation.response` is poulated, which
    	//     contains a [PhotoSequence][google.streetview.publish.v1.PhotoSequence]
    	//     message.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence].
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] does not exist.
    	GetPhotoSequence(ctx context.Context, in *GetPhotoSequenceRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the [PhotoSequences][google.streetview.publish.v1.PhotoSequence]
    	// that belong to the user, in descending CreatePhotoSequence timestamp order.
    	ListPhotoSequences(ctx context.Context, in *ListPhotoSequencesRequest, opts ...grpc.CallOption) (*ListPhotoSequencesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a [PhotoSequence][google.streetview.publish.v1.PhotoSequence] and
    	// its metadata.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo sequence.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the photo
    	// sequence ID does not exist.
    	// * [google.rpc.Code.FAILED_PRECONDITION][google.rpc.Code.FAILED_PRECONDITION] if the photo sequence ID is not
    	// yet finished processing.
    	DeletePhotoSequence(ctx context.Context, in *DeletePhotoSequenceRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

StreetViewPublishServiceClient is the client API for StreetViewPublishService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewStreetViewPublishServiceClient 
    
    
    func NewStreetViewPublishServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) StreetViewPublishServiceClient

## StreetViewPublishServiceServer
    
    
    type StreetViewPublishServiceServer interface {
    	// Creates an upload session to start uploading photo bytes.  The method uses
    	// the upload URL of the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef] to upload the bytes for
    	// the [Photo][google.streetview.publish.v1.Photo].
    	//
    	// In addition to the photo requirements shown in
    	// https://support.google.com/maps/answer/7012050?ref_topic=6275604,
    	// the photo must meet the following requirements:
    	//
    	// * Photo Sphere XMP metadata must be included in the photo metadata. See
    	// https://developers.google.com/streetview/spherical-metadata for the
    	// required fields.
    	// * The pixel size of the photo must meet the size requirements listed in
    	// https://support.google.com/maps/answer/7012050?ref_topic=6275604, and
    	// the photo must be a full 360 horizontally.
    	//
    	// After the upload completes, the method uses
    	// [UploadRef][google.streetview.publish.v1.UploadRef] with
    	// [CreatePhoto][google.streetview.publish.v1.StreetViewPublishService.CreatePhoto]
    	// to create the [Photo][google.streetview.publish.v1.Photo] object entry.
    	StartUpload(context.Context, *emptypb.Empty) (*UploadRef, [error](https://pkg.go.dev/builtin#error))
    	// After the client finishes uploading the photo with the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef],
    	// [CreatePhoto][google.streetview.publish.v1.StreetViewPublishService.CreatePhoto]
    	// publishes the uploaded [Photo][google.streetview.publish.v1.Photo] to
    	// Street View on Google Maps.
    	//
    	// Currently, the only way to set heading, pitch, and roll in CreatePhoto is
    	// through the [Photo Sphere XMP
    	// metadata](https://developers.google.com/streetview/spherical-metadata) in
    	// the photo bytes. CreatePhoto ignores the  `pose.heading`, `pose.pitch`,
    	// `pose.roll`, `pose.altitude`, and `pose.level` fields in Pose.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed or if the uploaded photo is not a 360 photo.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the upload
    	// reference does not exist.
    	// * [google.rpc.Code.RESOURCE_EXHAUSTED][google.rpc.Code.RESOURCE_EXHAUSTED]
    	// if the account has reached the storage limit.
    	CreatePhoto(context.Context, *CreatePhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [Photo][google.streetview.publish.v1.Photo].
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested
    	// [Photo][google.streetview.publish.v1.Photo].
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// [Photo][google.streetview.publish.v1.Photo] does not exist.
    	// * [google.rpc.Code.UNAVAILABLE][google.rpc.Code.UNAVAILABLE] if the
    	// requested [Photo][google.streetview.publish.v1.Photo] is still being
    	// indexed.
    	GetPhoto(context.Context, *GetPhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [Photo][google.streetview.publish.v1.Photo] batch.
    	//
    	// Note that if
    	// [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchGetPhotosResponse.results][google.streetview.publish.v1.BatchGetPhotosResponse.results].
    	// See
    	// [GetPhoto][google.streetview.publish.v1.StreetViewPublishService.GetPhoto]
    	// for specific failures that can occur per photo.
    	BatchGetPhotos(context.Context, *BatchGetPhotosRequest) (*BatchGetPhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the [Photos][google.streetview.publish.v1.Photo] that belong to
    	// the user.
    	//
    	// > Note: Recently created photos that are still
    	// being indexed are not returned in the response.
    	ListPhotos(context.Context, *ListPhotosRequest) (*ListPhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Updates the metadata of a [Photo][google.streetview.publish.v1.Photo], such
    	// as pose, place association, connections, etc. Changing the pixels of a
    	// photo is not supported.
    	//
    	// Only the fields specified in the
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// field are used. If `updateMask` is not present, the update applies to all
    	// fields.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo.
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// photo does not exist.
    	// * [google.rpc.Code.UNAVAILABLE][google.rpc.Code.UNAVAILABLE] if the
    	// requested [Photo][google.streetview.publish.v1.Photo] is still being
    	// indexed.
    	UpdatePhoto(context.Context, *UpdatePhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))
    	// Updates the metadata of [Photos][google.streetview.publish.v1.Photo], such
    	// as pose, place association, connections, etc. Changing the pixels of photos
    	// is not supported.
    	//
    	// Note that if
    	// [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchUpdatePhotosResponse.results][google.streetview.publish.v1.BatchUpdatePhotosResponse.results].
    	// See
    	// [UpdatePhoto][google.streetview.publish.v1.StreetViewPublishService.UpdatePhoto]
    	// for specific failures that can occur per photo.
    	//
    	// Only the fields specified in
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// field are used. If `updateMask` is not present, the update applies to all
    	// fields.
    	//
    	// The number of
    	// [UpdatePhotoRequest][google.streetview.publish.v1.UpdatePhotoRequest]
    	// messages in a
    	// [BatchUpdatePhotosRequest][google.streetview.publish.v1.BatchUpdatePhotosRequest]
    	// must not exceed 20.
    	//
    	// > Note: To update
    	// [Pose.altitude][google.streetview.publish.v1.Pose.altitude],
    	// [Pose.latLngPair][google.streetview.publish.v1.Pose.lat_lng_pair] has to be
    	// filled as well. Otherwise, the request will fail.
    	BatchUpdatePhotos(context.Context, *BatchUpdatePhotosRequest) (*BatchUpdatePhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a [Photo][google.streetview.publish.v1.Photo] and its metadata.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the photo ID
    	// does not exist.
    	DeletePhoto(context.Context, *DeletePhotoRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a list of [Photos][google.streetview.publish.v1.Photo] and their
    	// metadata.
    	//
    	// Note that if
    	// [BatchDeletePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchDeletePhotos]
    	// fails, either critical fields are missing or there is an authentication
    	// error. Even if
    	// [BatchDeletePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchDeletePhotos]
    	// succeeds, individual photos in the batch may have failures.
    	// These failures are specified in each
    	// [PhotoResponse.status][google.streetview.publish.v1.PhotoResponse.status]
    	// in
    	// [BatchDeletePhotosResponse.results][google.streetview.publish.v1.BatchDeletePhotosResponse.status].
    	// See
    	// [DeletePhoto][google.streetview.publish.v1.StreetViewPublishService.DeletePhoto]
    	// for specific failures that can occur per photo.
    	BatchDeletePhotos(context.Context, *BatchDeletePhotosRequest) (*BatchDeletePhotosResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an upload session to start uploading photo sequence data.
    	// The upload URL of the returned
    	// [UploadRef][google.streetview.publish.v1.UploadRef] is used to upload the
    	// data for the `photoSequence`.
    	//
    	// After the upload is complete, the
    	// [UploadRef][google.streetview.publish.v1.UploadRef] is used with
    	// [CreatePhotoSequence][google.streetview.publish.v1.StreetViewPublishService.CreatePhotoSequence]
    	// to create the [PhotoSequence][google.streetview.publish.v1.PhotoSequence]
    	// object entry.
    	StartPhotoSequenceUpload(context.Context, *emptypb.Empty) (*UploadRef, [error](https://pkg.go.dev/builtin#error))
    	// After the client finishes uploading the
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] with the
    	// returned [UploadRef][google.streetview.publish.v1.UploadRef],
    	// [CreatePhotoSequence][google.streetview.publish.v1.StreetViewPublishService.CreatePhotoSequence]
    	// extracts a sequence of 360 photos from a video or Extensible Device
    	// Metadata (XDM, http://www.xdm.org/) to be published to Street View on
    	// Google Maps.
    	//
    	// `CreatePhotoSequence` returns an [Operation][google.longrunning.Operation],
    	// with the [PhotoSequence][google.streetview.publish.v1.PhotoSequence] Id set
    	// in the `Operation.name` field.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] if
    	// the request is malformed.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the upload
    	// reference does not exist.
    	CreatePhotoSequence(context.Context, *CreatePhotoSequenceRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the metadata of the specified
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] via the
    	// [Operation][google.longrunning.Operation] interface.
    	//
    	// This method returns the following three types of responses:
    	//
    	//   - `Operation.done` = false, if the processing of
    	//     [PhotoSequence][google.streetview.publish.v1.PhotoSequence] is not
    	//     finished yet.
    	//   - `Operation.done` = true and `Operation.error` is populated, if there was
    	//     an error in processing.
    	//   - `Operation.done` = true and `Operation.response` is poulated, which
    	//     contains a [PhotoSequence][google.streetview.publish.v1.PhotoSequence]
    	//     message.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence].
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the requested
    	// [PhotoSequence][google.streetview.publish.v1.PhotoSequence] does not exist.
    	GetPhotoSequence(context.Context, *GetPhotoSequenceRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the [PhotoSequences][google.streetview.publish.v1.PhotoSequence]
    	// that belong to the user, in descending CreatePhotoSequence timestamp order.
    	ListPhotoSequences(context.Context, *ListPhotoSequencesRequest) (*ListPhotoSequencesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a [PhotoSequence][google.streetview.publish.v1.PhotoSequence] and
    	// its metadata.
    	//
    	// This method returns the following error codes:
    	//
    	// * [google.rpc.Code.PERMISSION_DENIED][google.rpc.Code.PERMISSION_DENIED] if
    	// the requesting user did not create the requested photo sequence.
    	// * [google.rpc.Code.NOT_FOUND][google.rpc.Code.NOT_FOUND] if the photo
    	// sequence ID does not exist.
    	// * [google.rpc.Code.FAILED_PRECONDITION][google.rpc.Code.FAILED_PRECONDITION] if the photo sequence ID is not
    	// yet finished processing.
    	DeletePhotoSequence(context.Context, *DeletePhotoSequenceRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    }

StreetViewPublishServiceServer is the server API for StreetViewPublishService service. All implementations should embed UnimplementedStreetViewPublishServiceServer for forward compatibility

## UnimplementedStreetViewPublishServiceServer
    
    
    type UnimplementedStreetViewPublishServiceServer struct {
    }

UnimplementedStreetViewPublishServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedStreetViewPublishServiceServer) BatchDeletePhotos 
    
    
    func (UnimplementedStreetViewPublishServiceServer) BatchDeletePhotos([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *BatchDeletePhotosRequest) (*BatchDeletePhotosResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) BatchGetPhotos 
    
    
    func (UnimplementedStreetViewPublishServiceServer) BatchGetPhotos([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *BatchGetPhotosRequest) (*BatchGetPhotosResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) BatchUpdatePhotos 
    
    
    func (UnimplementedStreetViewPublishServiceServer) BatchUpdatePhotos([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *BatchUpdatePhotosRequest) (*BatchUpdatePhotosResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) CreatePhoto 
    
    
    func (UnimplementedStreetViewPublishServiceServer) CreatePhoto([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreatePhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) CreatePhotoSequence 
    
    
    func (UnimplementedStreetViewPublishServiceServer) CreatePhotoSequence([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreatePhotoSequenceRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) DeletePhoto 
    
    
    func (UnimplementedStreetViewPublishServiceServer) DeletePhoto([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeletePhotoRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) DeletePhotoSequence 
    
    
    func (UnimplementedStreetViewPublishServiceServer) DeletePhotoSequence([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeletePhotoSequenceRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) GetPhoto 
    
    
    func (UnimplementedStreetViewPublishServiceServer) GetPhoto([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) GetPhotoSequence 
    
    
    func (UnimplementedStreetViewPublishServiceServer) GetPhotoSequence([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPhotoSequenceRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) ListPhotoSequences 
    
    
    func (UnimplementedStreetViewPublishServiceServer) ListPhotoSequences([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListPhotoSequencesRequest) (*ListPhotoSequencesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) ListPhotos 
    
    
    func (UnimplementedStreetViewPublishServiceServer) ListPhotos([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListPhotosRequest) (*ListPhotosResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) StartPhotoSequenceUpload 
    
    
    func (UnimplementedStreetViewPublishServiceServer) StartPhotoSequenceUpload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty)) (*UploadRef, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) StartUpload 
    
    
    func (UnimplementedStreetViewPublishServiceServer) StartUpload([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty)) (*UploadRef, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedStreetViewPublishServiceServer) UpdatePhoto 
    
    
    func (UnimplementedStreetViewPublishServiceServer) UpdatePhoto([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdatePhotoRequest) (*Photo, [error](https://pkg.go.dev/builtin#error))

## UnsafeStreetViewPublishServiceServer
    
    
    type UnsafeStreetViewPublishServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeStreetViewPublishServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to StreetViewPublishServiceServer will result in compilation errors.

## UpdatePhotoRequest
    
    
    type UpdatePhotoRequest struct {
    
    	// Required. [Photo][google.streetview.publish.v1.Photo] object containing the
    	// new metadata.
    	Photo *Photo `protobuf:"bytes,1,opt,name=photo,proto3" json:"photo,omitempty"`
    	// Required. Mask that identifies fields on the photo metadata to update.
    	// If not present, the old [Photo][google.streetview.publish.v1.Photo]
    	// metadata is entirely replaced with the
    	// new [Photo][google.streetview.publish.v1.Photo] metadata in this request.
    	// The update fails if invalid fields are specified. Multiple fields can be
    	// specified in a comma-delimited list.
    	//
    	// The following fields are valid:
    	//
    	// * `pose.heading`
    	// * `pose.lat_lng_pair`
    	// * `pose.pitch`
    	// * `pose.roll`
    	// * `pose.level`
    	// * `pose.altitude`
    	// * `connections`
    	// * `places`
    	//
    	// > Note: When
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// contains repeated fields, the entire set of repeated values get replaced
    	// with the new contents. For example, if
    	// [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.update_mask]
    	// contains `connections` and `UpdatePhotoRequest.photo.connections` is empty,
    	// all connections are removed.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request to update the metadata of a [Photo][google.streetview.publish.v1.Photo]. Updating the pixels of a photo is not supported.

### func (*UpdatePhotoRequest) Descriptor 
    
    
    func (*UpdatePhotoRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdatePhotoRequest.ProtoReflect.Descriptor instead.

### func (*UpdatePhotoRequest) GetPhoto 
    
    
    func (x *UpdatePhotoRequest) GetPhoto() *Photo

### func (*UpdatePhotoRequest) GetUpdateMask 
    
    
    func (x *UpdatePhotoRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdatePhotoRequest) ProtoMessage 
    
    
    func (*UpdatePhotoRequest) ProtoMessage()

### func (*UpdatePhotoRequest) ProtoReflect 
    
    
    func (x *UpdatePhotoRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdatePhotoRequest) Reset 
    
    
    func (x *UpdatePhotoRequest) Reset()

### func (*UpdatePhotoRequest) String 
    
    
    func (x *UpdatePhotoRequest) String() [string](https://pkg.go.dev/builtin#string)

## UploadRef
    
    
    type UploadRef struct {
    
    	// Required.
    	//
    	// Types that are valid to be assigned to FileSource:
    	//
    	//	*UploadRef_UploadUrl
    	FileSource isUploadRef_FileSource `protobuf_oneof:"file_source"`
    	// contains filtered or unexported fields
    }

Upload reference for media files.

### func (*UploadRef) Descriptor 
    
    
    func (*UploadRef) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UploadRef.ProtoReflect.Descriptor instead.

### func (*UploadRef) GetFileSource 
    
    
    func (x *UploadRef) GetFileSource() isUploadRef_FileSource

### func (*UploadRef) GetUploadUrl 
    
    
    func (x *UploadRef) GetUploadUrl() [string](https://pkg.go.dev/builtin#string)

### func (*UploadRef) ProtoMessage 
    
    
    func (*UploadRef) ProtoMessage()

### func (*UploadRef) ProtoReflect 
    
    
    func (x *UploadRef) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UploadRef) Reset 
    
    
    func (x *UploadRef) Reset()

### func (*UploadRef) String 
    
    
    func (x *UploadRef) String() [string](https://pkg.go.dev/builtin#string)

## UploadRef_UploadUrl
    
    
    type UploadRef_UploadUrl struct {
    	// An upload reference should be unique for each user. It follows
    	// the form:
    	// "https://streetviewpublish.googleapis.com/media/user/{account_id}/photo/{upload_reference}"
    	UploadUrl [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=upload_url,json=uploadUrl,proto3,oneof"`
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
