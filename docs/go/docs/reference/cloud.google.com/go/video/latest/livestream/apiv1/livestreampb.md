---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1/livestreampb/
title: Live Stream API v1 - Package cloud.google.com/go/video/livestream/apiv1/livestreampb (v1.34.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:36.248156+00:00
---

# Live Stream API v1 - Package cloud.google.com/go/video/livestream/apiv1/livestreampb (v1.34.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1/livestreampb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Live Stream API v1 - Package cloud.google.com/go/video/livestream/apiv1/livestreampb (v1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.1  1.26.0  1.25.0  1.24.0  1.23.5  1.22.1  1.21.3  1.20.6  1.19.0  1.18.0  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/video/livestream/apiv1/livestreampb). 

##  Constants 

### LivestreamService_CreateChannel_FullMethodName, LivestreamService_ListChannels_FullMethodName, LivestreamService_GetChannel_FullMethodName, LivestreamService_DeleteChannel_FullMethodName, LivestreamService_UpdateChannel_FullMethodName, LivestreamService_StartChannel_FullMethodName, LivestreamService_StopChannel_FullMethodName, LivestreamService_StartDistribution_FullMethodName, LivestreamService_StopDistribution_FullMethodName, LivestreamService_CreateInput_FullMethodName, LivestreamService_ListInputs_FullMethodName, LivestreamService_GetInput_FullMethodName, LivestreamService_DeleteInput_FullMethodName, LivestreamService_UpdateInput_FullMethodName, LivestreamService_PreviewInput_FullMethodName, LivestreamService_CreateEvent_FullMethodName, LivestreamService_ListEvents_FullMethodName, LivestreamService_GetEvent_FullMethodName, LivestreamService_DeleteEvent_FullMethodName, LivestreamService_ListClips_FullMethodName, LivestreamService_GetClip_FullMethodName, LivestreamService_CreateClip_FullMethodName, LivestreamService_DeleteClip_FullMethodName, LivestreamService_CreateDvrSession_FullMethodName, LivestreamService_ListDvrSessions_FullMethodName, LivestreamService_GetDvrSession_FullMethodName, LivestreamService_DeleteDvrSession_FullMethodName, LivestreamService_UpdateDvrSession_FullMethodName, LivestreamService_CreateAsset_FullMethodName, LivestreamService_DeleteAsset_FullMethodName, LivestreamService_GetAsset_FullMethodName, LivestreamService_ListAssets_FullMethodName, LivestreamService_GetPool_FullMethodName, LivestreamService_UpdatePool_FullMethodName
    
    
    const (
    	LivestreamService_CreateChannel_FullMethodName     = "/google.cloud.video.livestream.v1.LivestreamService/CreateChannel"
    	LivestreamService_ListChannels_FullMethodName      = "/google.cloud.video.livestream.v1.LivestreamService/ListChannels"
    	LivestreamService_GetChannel_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/GetChannel"
    	LivestreamService_DeleteChannel_FullMethodName     = "/google.cloud.video.livestream.v1.LivestreamService/DeleteChannel"
    	LivestreamService_UpdateChannel_FullMethodName     = "/google.cloud.video.livestream.v1.LivestreamService/UpdateChannel"
    	LivestreamService_StartChannel_FullMethodName      = "/google.cloud.video.livestream.v1.LivestreamService/StartChannel"
    	LivestreamService_StopChannel_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/StopChannel"
    	LivestreamService_StartDistribution_FullMethodName = "/google.cloud.video.livestream.v1.LivestreamService/StartDistribution"
    	LivestreamService_StopDistribution_FullMethodName  = "/google.cloud.video.livestream.v1.LivestreamService/StopDistribution"
    	LivestreamService_CreateInput_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/CreateInput"
    	LivestreamService_ListInputs_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/ListInputs"
    	LivestreamService_GetInput_FullMethodName          = "/google.cloud.video.livestream.v1.LivestreamService/GetInput"
    	LivestreamService_DeleteInput_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/DeleteInput"
    	LivestreamService_UpdateInput_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/UpdateInput"
    	LivestreamService_PreviewInput_FullMethodName      = "/google.cloud.video.livestream.v1.LivestreamService/PreviewInput"
    	LivestreamService_CreateEvent_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/CreateEvent"
    	LivestreamService_ListEvents_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/ListEvents"
    	LivestreamService_GetEvent_FullMethodName          = "/google.cloud.video.livestream.v1.LivestreamService/GetEvent"
    	LivestreamService_DeleteEvent_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/DeleteEvent"
    	LivestreamService_ListClips_FullMethodName         = "/google.cloud.video.livestream.v1.LivestreamService/ListClips"
    	LivestreamService_GetClip_FullMethodName           = "/google.cloud.video.livestream.v1.LivestreamService/GetClip"
    	LivestreamService_CreateClip_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/CreateClip"
    	LivestreamService_DeleteClip_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/DeleteClip"
    	LivestreamService_CreateDvrSession_FullMethodName  = "/google.cloud.video.livestream.v1.LivestreamService/CreateDvrSession"
    	LivestreamService_ListDvrSessions_FullMethodName   = "/google.cloud.video.livestream.v1.LivestreamService/ListDvrSessions"
    	LivestreamService_GetDvrSession_FullMethodName     = "/google.cloud.video.livestream.v1.LivestreamService/GetDvrSession"
    	LivestreamService_DeleteDvrSession_FullMethodName  = "/google.cloud.video.livestream.v1.LivestreamService/DeleteDvrSession"
    	LivestreamService_UpdateDvrSession_FullMethodName  = "/google.cloud.video.livestream.v1.LivestreamService/UpdateDvrSession"
    	LivestreamService_CreateAsset_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/CreateAsset"
    	LivestreamService_DeleteAsset_FullMethodName       = "/google.cloud.video.livestream.v1.LivestreamService/DeleteAsset"
    	LivestreamService_GetAsset_FullMethodName          = "/google.cloud.video.livestream.v1.LivestreamService/GetAsset"
    	LivestreamService_ListAssets_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/ListAssets"
    	LivestreamService_GetPool_FullMethodName           = "/google.cloud.video.livestream.v1.LivestreamService/GetPool"
    	LivestreamService_UpdatePool_FullMethodName        = "/google.cloud.video.livestream.v1.LivestreamService/UpdatePool"
    )

## Variables 

### Manifest_ManifestType_name, Manifest_ManifestType_value
    
    
    var (
    	Manifest_ManifestType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "MANIFEST_TYPE_UNSPECIFIED",
    		1: "HLS",
    		2: "DASH",
    	}
    	Manifest_ManifestType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"MANIFEST_TYPE_UNSPECIFIED": 0,
    		"HLS":                       1,
    		"DASH":                      2,
    	}
    )

Enum value maps for Manifest_ManifestType.

### Distribution_State_name, Distribution_State_value
    
    
    var (
    	Distribution_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		5: "ERROR",
    		6: "NOT_READY",
    		7: "READY",
    		8: "AWAITING_INPUT",
    		9: "DISTRIBUTING",
    	}
    	Distribution_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ERROR":             5,
    		"NOT_READY":         6,
    		"READY":             7,
    		"AWAITING_INPUT":    8,
    		"DISTRIBUTING":      9,
    	}
    )

Enum value maps for Distribution_State.

### TimecodeConfig_TimecodeSource_name, TimecodeConfig_TimecodeSource_value
    
    
    var (
    	TimecodeConfig_TimecodeSource_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TIMECODE_SOURCE_UNSPECIFIED",
    		1: "MEDIA_TIMESTAMP",
    		2: "EMBEDDED_TIMECODE",
    	}
    	TimecodeConfig_TimecodeSource_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TIMECODE_SOURCE_UNSPECIFIED": 0,
    		"MEDIA_TIMESTAMP":             1,
    		"EMBEDDED_TIMECODE":           2,
    	}
    )

Enum value maps for TimecodeConfig_TimecodeSource.

### Input_Type_name, Input_Type_value
    
    
    var (
    	Input_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "RTMP_PUSH",
    		2: "SRT_PUSH",
    	}
    	Input_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"RTMP_PUSH":        1,
    		"SRT_PUSH":         2,
    	}
    )

Enum value maps for Input_Type.

### Input_Tier_name, Input_Tier_value
    
    
    var (
    	Input_Tier_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TIER_UNSPECIFIED",
    		1: "SD",
    		2: "HD",
    		3: "UHD",
    		4: "SD_H265",
    		5: "HD_H265",
    		6: "UHD_H265",
    	}
    	Input_Tier_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TIER_UNSPECIFIED": 0,
    		"SD":               1,
    		"HD":               2,
    		"UHD":              3,
    		"SD_H265":          4,
    		"HD_H265":          5,
    		"UHD_H265":         6,
    	}
    )

Enum value maps for Input_Tier.

### Channel_StreamingState_name, Channel_StreamingState_value
    
    
    var (
    	Channel_StreamingState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STREAMING_STATE_UNSPECIFIED",
    		1: "STREAMING",
    		2: "AWAITING_INPUT",
    		4: "STREAMING_ERROR",
    		5: "STREAMING_NO_INPUT",
    		6: "STOPPED",
    		7: "STARTING",
    		8: "STOPPING",
    	}
    	Channel_StreamingState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STREAMING_STATE_UNSPECIFIED": 0,
    		"STREAMING":                   1,
    		"AWAITING_INPUT":              2,
    		"STREAMING_ERROR":             4,
    		"STREAMING_NO_INPUT":          5,
    		"STOPPED":                     6,
    		"STARTING":                    7,
    		"STOPPING":                    8,
    	}
    )

Enum value maps for Channel_StreamingState.

### InputConfig_InputSwitchMode_name, InputConfig_InputSwitchMode_value
    
    
    var (
    	InputConfig_InputSwitchMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INPUT_SWITCH_MODE_UNSPECIFIED",
    		1: "FAILOVER_PREFER_PRIMARY",
    		3: "MANUAL",
    	}
    	InputConfig_InputSwitchMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INPUT_SWITCH_MODE_UNSPECIFIED": 0,
    		"FAILOVER_PREFER_PRIMARY":       1,
    		"MANUAL":                        3,
    	}
    )

Enum value maps for InputConfig_InputSwitchMode.

### LogConfig_LogSeverity_name, LogConfig_LogSeverity_value
    
    
    var (
    	LogConfig_LogSeverity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:   "LOG_SEVERITY_UNSPECIFIED",
    		1:   "OFF",
    		100: "DEBUG",
    		200: "INFO",
    		400: "WARNING",
    		500: "ERROR",
    	}
    	LogConfig_LogSeverity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"LOG_SEVERITY_UNSPECIFIED": 0,
    		"OFF":                      1,
    		"DEBUG":                    100,
    		"INFO":                     200,
    		"WARNING":                  400,
    		"ERROR":                    500,
    	}
    )

Enum value maps for LogConfig_LogSeverity.

### AutoTranscriptionConfig_DisplayTiming_name, AutoTranscriptionConfig_DisplayTiming_value
    
    
    var (
    	AutoTranscriptionConfig_DisplayTiming_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "DISPLAY_TIMING_UNSPECIFIED",
    		1: "ASYNC",
    		2: "SYNC",
    	}
    	AutoTranscriptionConfig_DisplayTiming_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"DISPLAY_TIMING_UNSPECIFIED": 0,
    		"ASYNC":                      1,
    		"SYNC":                       2,
    	}
    )

Enum value maps for AutoTranscriptionConfig_DisplayTiming.

### AutoTranscriptionConfig_QualityPreset_name, AutoTranscriptionConfig_QualityPreset_value
    
    
    var (
    	AutoTranscriptionConfig_QualityPreset_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "QUALITY_PRESET_UNSPECIFIED",
    		1: "LOW_LATENCY",
    		2: "BALANCED_QUALITY",
    		3: "IMPROVED_QUALITY",
    	}
    	AutoTranscriptionConfig_QualityPreset_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"QUALITY_PRESET_UNSPECIFIED": 0,
    		"LOW_LATENCY":                1,
    		"BALANCED_QUALITY":           2,
    		"IMPROVED_QUALITY":           3,
    	}
    )

Enum value maps for AutoTranscriptionConfig_QualityPreset.

### Event_State_name, Event_State_value
    
    
    var (
    	Event_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "SCHEDULED",
    		2: "RUNNING",
    		3: "SUCCEEDED",
    		4: "FAILED",
    		5: "PENDING",
    		6: "STOPPED",
    	}
    	Event_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"SCHEDULED":         1,
    		"RUNNING":           2,
    		"SUCCEEDED":         3,
    		"FAILED":            4,
    		"PENDING":           5,
    		"STOPPED":           6,
    	}
    )

Enum value maps for Event_State.

### Clip_State_name, Clip_State_value
    
    
    var (
    	Clip_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "PENDING",
    		2: "CREATING",
    		3: "SUCCEEDED",
    		4: "FAILED",
    	}
    	Clip_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"PENDING":           1,
    		"CREATING":          2,
    		"SUCCEEDED":         3,
    		"FAILED":            4,
    	}
    )

Enum value maps for Clip_State.

### Clip_OutputType_name, Clip_OutputType_value
    
    
    var (
    	Clip_OutputType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "OUTPUT_TYPE_UNSPECIFIED",
    		1: "MANIFEST",
    		2: "MP4",
    	}
    	Clip_OutputType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"OUTPUT_TYPE_UNSPECIFIED": 0,
    		"MANIFEST":                1,
    		"MP4":                     2,
    	}
    )

Enum value maps for Clip_OutputType.

### DvrSession_State_name, DvrSession_State_value
    
    
    var (
    	DvrSession_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0:  "STATE_UNSPECIFIED",
    		1:  "PENDING",
    		2:  "UPDATING",
    		3:  "SCHEDULED",
    		4:  "LIVE",
    		5:  "FINISHED",
    		6:  "FAILED",
    		7:  "DELETING",
    		8:  "POST_PROCESSING",
    		9:  "COOLDOWN",
    		10: "STOPPING",
    	}
    	DvrSession_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"PENDING":           1,
    		"UPDATING":          2,
    		"SCHEDULED":         3,
    		"LIVE":              4,
    		"FINISHED":          5,
    		"FAILED":            6,
    		"DELETING":          7,
    		"POST_PROCESSING":   8,
    		"COOLDOWN":          9,
    		"STOPPING":          10,
    	}
    )

Enum value maps for DvrSession_State.

### Asset_State_name, Asset_State_value
    
    
    var (
    	Asset_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "CREATING",
    		2: "ACTIVE",
    		3: "DELETING",
    		4: "ERROR",
    	}
    	Asset_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"CREATING":          1,
    		"ACTIVE":            2,
    		"DELETING":          3,
    		"ERROR":             4,
    	}
    )

Enum value maps for Asset_State.

### File_google_cloud_video_livestream_v1_outputs_proto
    
    
    var File_google_cloud_video_livestream_v1_outputs_proto protoreflect.FileDescriptor

### File_google_cloud_video_livestream_v1_resources_proto
    
    
    var File_google_cloud_video_livestream_v1_resources_proto protoreflect.FileDescriptor

### File_google_cloud_video_livestream_v1_service_proto
    
    
    var File_google_cloud_video_livestream_v1_service_proto protoreflect.FileDescriptor

### LivestreamService_ServiceDesc
    
    
    var LivestreamService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.video.livestream.v1.LivestreamService",
    	HandlerType: (*LivestreamServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateChannel",
    			Handler:    _LivestreamService_CreateChannel_Handler,
    		},
    		{
    			MethodName: "ListChannels",
    			Handler:    _LivestreamService_ListChannels_Handler,
    		},
    		{
    			MethodName: "GetChannel",
    			Handler:    _LivestreamService_GetChannel_Handler,
    		},
    		{
    			MethodName: "DeleteChannel",
    			Handler:    _LivestreamService_DeleteChannel_Handler,
    		},
    		{
    			MethodName: "UpdateChannel",
    			Handler:    _LivestreamService_UpdateChannel_Handler,
    		},
    		{
    			MethodName: "StartChannel",
    			Handler:    _LivestreamService_StartChannel_Handler,
    		},
    		{
    			MethodName: "StopChannel",
    			Handler:    _LivestreamService_StopChannel_Handler,
    		},
    		{
    			MethodName: "StartDistribution",
    			Handler:    _LivestreamService_StartDistribution_Handler,
    		},
    		{
    			MethodName: "StopDistribution",
    			Handler:    _LivestreamService_StopDistribution_Handler,
    		},
    		{
    			MethodName: "CreateInput",
    			Handler:    _LivestreamService_CreateInput_Handler,
    		},
    		{
    			MethodName: "ListInputs",
    			Handler:    _LivestreamService_ListInputs_Handler,
    		},
    		{
    			MethodName: "GetInput",
    			Handler:    _LivestreamService_GetInput_Handler,
    		},
    		{
    			MethodName: "DeleteInput",
    			Handler:    _LivestreamService_DeleteInput_Handler,
    		},
    		{
    			MethodName: "UpdateInput",
    			Handler:    _LivestreamService_UpdateInput_Handler,
    		},
    		{
    			MethodName: "PreviewInput",
    			Handler:    _LivestreamService_PreviewInput_Handler,
    		},
    		{
    			MethodName: "CreateEvent",
    			Handler:    _LivestreamService_CreateEvent_Handler,
    		},
    		{
    			MethodName: "ListEvents",
    			Handler:    _LivestreamService_ListEvents_Handler,
    		},
    		{
    			MethodName: "GetEvent",
    			Handler:    _LivestreamService_GetEvent_Handler,
    		},
    		{
    			MethodName: "DeleteEvent",
    			Handler:    _LivestreamService_DeleteEvent_Handler,
    		},
    		{
    			MethodName: "ListClips",
    			Handler:    _LivestreamService_ListClips_Handler,
    		},
    		{
    			MethodName: "GetClip",
    			Handler:    _LivestreamService_GetClip_Handler,
    		},
    		{
    			MethodName: "CreateClip",
    			Handler:    _LivestreamService_CreateClip_Handler,
    		},
    		{
    			MethodName: "DeleteClip",
    			Handler:    _LivestreamService_DeleteClip_Handler,
    		},
    		{
    			MethodName: "CreateDvrSession",
    			Handler:    _LivestreamService_CreateDvrSession_Handler,
    		},
    		{
    			MethodName: "ListDvrSessions",
    			Handler:    _LivestreamService_ListDvrSessions_Handler,
    		},
    		{
    			MethodName: "GetDvrSession",
    			Handler:    _LivestreamService_GetDvrSession_Handler,
    		},
    		{
    			MethodName: "DeleteDvrSession",
    			Handler:    _LivestreamService_DeleteDvrSession_Handler,
    		},
    		{
    			MethodName: "UpdateDvrSession",
    			Handler:    _LivestreamService_UpdateDvrSession_Handler,
    		},
    		{
    			MethodName: "CreateAsset",
    			Handler:    _LivestreamService_CreateAsset_Handler,
    		},
    		{
    			MethodName: "DeleteAsset",
    			Handler:    _LivestreamService_DeleteAsset_Handler,
    		},
    		{
    			MethodName: "GetAsset",
    			Handler:    _LivestreamService_GetAsset_Handler,
    		},
    		{
    			MethodName: "ListAssets",
    			Handler:    _LivestreamService_ListAssets_Handler,
    		},
    		{
    			MethodName: "GetPool",
    			Handler:    _LivestreamService_GetPool_Handler,
    		},
    		{
    			MethodName: "UpdatePool",
    			Handler:    _LivestreamService_UpdatePool_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/video/livestream/v1/service.proto",
    }

LivestreamService_ServiceDesc is the grpc.ServiceDesc for LivestreamService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterLivestreamServiceServer 
    
    
    func RegisterLivestreamServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv LivestreamServiceServer)

## Asset
    
    
    type Asset struct {
    
    	// The resource name of the asset, in the form of:
    	// `projects/{project}/locations/{location}/assets/{assetId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// The reference to the asset.
    	// The maximum size of the resource is 250 MB.
    	//
    	// Types that are valid to be assigned to Resource:
    	//
    	//	*Asset_Video
    	//	*Asset_Image
    	Resource isAsset_Resource `protobuf_oneof:"resource"`
    	// Based64-encoded CRC32c checksum of the asset file. For more information,
    	// see the crc32c checksum of the [Cloud Storage Objects
    	// resource](https://cloud.google.com/storage/docs/json_api/v1/objects).
    	// If crc32c is omitted or left empty when the asset is created, this field is
    	// filled by the crc32c checksum of the Cloud Storage object indicated by
    	// [VideoAsset.uri][google.cloud.video.livestream.v1.Asset.VideoAsset.uri] or
    	// [ImageAsset.uri][google.cloud.video.livestream.v1.Asset.ImageAsset.uri]. If
    	// crc32c is set, the asset can't be created if the crc32c value does not
    	// match with the crc32c checksum of the Cloud Storage object indicated by
    	// [VideoAsset.uri][google.cloud.video.livestream.v1.Asset.VideoAsset.uri] or
    	// [ImageAsset.uri][google.cloud.video.livestream.v1.Asset.ImageAsset.uri].
    	Crc32C [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=crc32c,proto3" json:"crc32c,omitempty"`
    	// Output only. The state of the asset resource.
    	State Asset_State `protobuf:"varint,8,opt,name=state,proto3,enum=google.cloud.video.livestream.v1.Asset_State" json:"state,omitempty"`
    	// Output only. Only present when `state` is `ERROR`. The reason for the error
    	// state of the asset.
    	Error *status.Status `protobuf:"bytes,9,opt,name=error,proto3" json:"error,omitempty"`
    	// contains filtered or unexported fields
    }

An asset represents a video or an image.

### func (*Asset) Descriptor 
    
    
    func (*Asset) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Asset.ProtoReflect.Descriptor instead.

### func (*Asset) GetCrc32C 
    
    
    func (x *Asset) GetCrc32C() [string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetCreateTime 
    
    
    func (x *Asset) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Asset) GetError 
    
    
    func (x *Asset) GetError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*Asset) GetImage 
    
    
    func (x *Asset) GetImage() *Asset_ImageAsset

### func (*Asset) GetLabels 
    
    
    func (x *Asset) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetName 
    
    
    func (x *Asset) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetResource 
    
    
    func (x *Asset) GetResource() isAsset_Resource

### func (*Asset) GetState 
    
    
    func (x *Asset) GetState() Asset_State

### func (*Asset) GetUpdateTime 
    
    
    func (x *Asset) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Asset) GetVideo 
    
    
    func (x *Asset) GetVideo() *Asset_VideoAsset

### func (*Asset) ProtoMessage 
    
    
    func (*Asset) ProtoMessage()

### func (*Asset) ProtoReflect 
    
    
    func (x *Asset) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Asset) Reset 
    
    
    func (x *Asset) Reset()

### func (*Asset) String 
    
    
    func (x *Asset) String() [string](https://pkg.go.dev/builtin#string)

## Asset_Image
    
    
    type Asset_Image struct {
    	// ImageAsset represents an image.
    	Image *Asset_ImageAsset `protobuf:"bytes,6,opt,name=image,proto3,oneof"`
    }

## Asset_ImageAsset
    
    
    type Asset_ImageAsset struct {
    
    	// Cloud Storage URI of the image. The format is `gs://my-bucket/my-object`.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// contains filtered or unexported fields
    }

Image represents an image. The supported formats are JPEG, PNG.

### func (*Asset_ImageAsset) Descriptor 
    
    
    func (*Asset_ImageAsset) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Asset_ImageAsset.ProtoReflect.Descriptor instead.

### func (*Asset_ImageAsset) GetUri 
    
    
    func (x *Asset_ImageAsset) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Asset_ImageAsset) ProtoMessage 
    
    
    func (*Asset_ImageAsset) ProtoMessage()

### func (*Asset_ImageAsset) ProtoReflect 
    
    
    func (x *Asset_ImageAsset) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Asset_ImageAsset) Reset 
    
    
    func (x *Asset_ImageAsset) Reset()

### func (*Asset_ImageAsset) String 
    
    
    func (x *Asset_ImageAsset) String() [string](https://pkg.go.dev/builtin#string)

## Asset_State
    
    
    type Asset_State [int32](https://pkg.go.dev/builtin#int32)

State of the asset resource.

### Asset_STATE_UNSPECIFIED, Asset_CREATING, Asset_ACTIVE, Asset_DELETING, Asset_ERROR
    
    
    const (
    	// State is not specified.
    	Asset_STATE_UNSPECIFIED Asset_State = 0
    	// The asset is being created.
    	Asset_CREATING Asset_State = 1
    	// The asset is ready for use.
    	Asset_ACTIVE Asset_State = 2
    	// The asset is being deleted.
    	Asset_DELETING Asset_State = 3
    	// The asset has an error.
    	Asset_ERROR Asset_State = 4
    )

### func (Asset_State) Descriptor 
    
    
    func (Asset_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Asset_State) Enum 
    
    
    func (x Asset_State) Enum() *Asset_State

### func (Asset_State) EnumDescriptor 
    
    
    func (Asset_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Asset_State.Descriptor instead.

### func (Asset_State) Number 
    
    
    func (x Asset_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Asset_State) String 
    
    
    func (x Asset_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Asset_State) Type 
    
    
    func (Asset_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Asset_Video
    
    
    type Asset_Video struct {
    	// VideoAsset represents a video.
    	Video *Asset_VideoAsset `protobuf:"bytes,5,opt,name=video,proto3,oneof"`
    }

## Asset_VideoAsset
    
    
    type Asset_VideoAsset struct {
    
    	// Cloud Storage URI of the video. The format is `gs://my-bucket/my-object`.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// contains filtered or unexported fields
    }

VideoAsset represents a video. The supported formats are MP4, MPEG-TS, and FLV. The supported video codec is H264. The supported audio codecs are AAC, AC3, MP2, and MP3.

### func (*Asset_VideoAsset) Descriptor 
    
    
    func (*Asset_VideoAsset) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Asset_VideoAsset.ProtoReflect.Descriptor instead.

### func (*Asset_VideoAsset) GetUri 
    
    
    func (x *Asset_VideoAsset) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Asset_VideoAsset) ProtoMessage 
    
    
    func (*Asset_VideoAsset) ProtoMessage()

### func (*Asset_VideoAsset) ProtoReflect 
    
    
    func (x *Asset_VideoAsset) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Asset_VideoAsset) Reset 
    
    
    func (x *Asset_VideoAsset) Reset()

### func (*Asset_VideoAsset) String 
    
    
    func (x *Asset_VideoAsset) String() [string](https://pkg.go.dev/builtin#string)

## AudioFormat
    
    
    type AudioFormat struct {
    
    	// Audio codec used in this audio stream.
    	Codec [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=codec,proto3" json:"codec,omitempty"`
    	// The number of audio channels.
    	ChannelCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=channel_count,json=channelCount,proto3" json:"channel_count,omitempty"`
    	// A list of channel names specifying the layout of the audio channels.
    	ChannelLayout [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=channel_layout,json=channelLayout,proto3" json:"channel_layout,omitempty"`
    	// contains filtered or unexported fields
    }

Properties of the audio format.

### func (*AudioFormat) Descriptor 
    
    
    func (*AudioFormat) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AudioFormat.ProtoReflect.Descriptor instead.

### func (*AudioFormat) GetChannelCount 
    
    
    func (x *AudioFormat) GetChannelCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioFormat) GetChannelLayout 
    
    
    func (x *AudioFormat) GetChannelLayout() [][string](https://pkg.go.dev/builtin#string)

### func (*AudioFormat) GetCodec 
    
    
    func (x *AudioFormat) GetCodec() [string](https://pkg.go.dev/builtin#string)

### func (*AudioFormat) ProtoMessage 
    
    
    func (*AudioFormat) ProtoMessage()

### func (*AudioFormat) ProtoReflect 
    
    
    func (x *AudioFormat) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AudioFormat) Reset 
    
    
    func (x *AudioFormat) Reset()

### func (*AudioFormat) String 
    
    
    func (x *AudioFormat) String() [string](https://pkg.go.dev/builtin#string)

## AudioStream
    
    
    type AudioStream struct {
    
    	// Specifies whether pass through (transmuxing) is enabled or not.
    	// If set to `true`, the rest of the settings, other than `mapping`, will be
    	// ignored. The default is `false`.
    	Transmux [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,8,opt,name=transmux,proto3" json:"transmux,omitempty"`
    	// The codec for this audio stream. The default is `aac`.
    	//
    	// Supported audio codecs:
    	//
    	// - `aac`
    	Codec [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=codec,proto3" json:"codec,omitempty"`
    	// Required. Audio bitrate in bits per second. Must be between 1 and
    	// 10,000,000.
    	BitrateBps [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=bitrate_bps,json=bitrateBps,proto3" json:"bitrate_bps,omitempty"`
    	// Number of audio channels. Must be between 1 and 6. The default is 2.
    	ChannelCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=channel_count,json=channelCount,proto3" json:"channel_count,omitempty"`
    	// A list of channel names specifying layout of the audio channels.
    	// This only affects the metadata embedded in the container headers, if
    	// supported by the specified format. The default is `[fl, fr]`.
    	//
    	// Supported channel names:
    	//
    	// - `fl` - Front left channel
    	// - `fr` - Front right channel
    	// - `sl` - Side left channel
    	// - `sr` - Side right channel
    	// - `fc` - Front center channel
    	// - `lfe` - Low frequency
    	ChannelLayout [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=channel_layout,json=channelLayout,proto3" json:"channel_layout,omitempty"`
    	// The mapping for the input streams and audio channels.
    	Mapping []*AudioStream_AudioMapping `protobuf:"bytes,5,rep,name=mapping,proto3" json:"mapping,omitempty"`
    	// The audio sample rate in Hertz. The default is 48000 Hertz.
    	SampleRateHertz [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=sample_rate_hertz,json=sampleRateHertz,proto3" json:"sample_rate_hertz,omitempty"`
    	// contains filtered or unexported fields
    }

Audio stream resource.

### func (*AudioStream) Descriptor 
    
    
    func (*AudioStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AudioStream.ProtoReflect.Descriptor instead.

### func (*AudioStream) GetBitrateBps 
    
    
    func (x *AudioStream) GetBitrateBps() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream) GetChannelCount 
    
    
    func (x *AudioStream) GetChannelCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream) GetChannelLayout 
    
    
    func (x *AudioStream) GetChannelLayout() [][string](https://pkg.go.dev/builtin#string)

### func (*AudioStream) GetCodec 
    
    
    func (x *AudioStream) GetCodec() [string](https://pkg.go.dev/builtin#string)

### func (*AudioStream) GetMapping 
    
    
    func (x *AudioStream) GetMapping() []*AudioStream_AudioMapping

### func (*AudioStream) GetSampleRateHertz 
    
    
    func (x *AudioStream) GetSampleRateHertz() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream) GetTransmux 
    
    
    func (x *AudioStream) GetTransmux() [bool](https://pkg.go.dev/builtin#bool)

### func (*AudioStream) ProtoMessage 
    
    
    func (*AudioStream) ProtoMessage()

### func (*AudioStream) ProtoReflect 
    
    
    func (x *AudioStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AudioStream) Reset 
    
    
    func (x *AudioStream) Reset()

### func (*AudioStream) String 
    
    
    func (x *AudioStream) String() [string](https://pkg.go.dev/builtin#string)

## AudioStreamProperty
    
    
    type AudioStreamProperty struct {
    
    	// Index of this audio stream.
    	Index [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=index,proto3" json:"index,omitempty"`
    	// Properties of the audio format.
    	AudioFormat *AudioFormat `protobuf:"bytes,2,opt,name=audio_format,json=audioFormat,proto3" json:"audio_format,omitempty"`
    	// contains filtered or unexported fields
    }

Properties of the audio stream.

### func (*AudioStreamProperty) Descriptor 
    
    
    func (*AudioStreamProperty) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AudioStreamProperty.ProtoReflect.Descriptor instead.

### func (*AudioStreamProperty) GetAudioFormat 
    
    
    func (x *AudioStreamProperty) GetAudioFormat() *AudioFormat

### func (*AudioStreamProperty) GetIndex 
    
    
    func (x *AudioStreamProperty) GetIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStreamProperty) ProtoMessage 
    
    
    func (*AudioStreamProperty) ProtoMessage()

### func (*AudioStreamProperty) ProtoReflect 
    
    
    func (x *AudioStreamProperty) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AudioStreamProperty) Reset 
    
    
    func (x *AudioStreamProperty) Reset()

### func (*AudioStreamProperty) String 
    
    
    func (x *AudioStreamProperty) String() [string](https://pkg.go.dev/builtin#string)

## AudioStream_AudioMapping
    
    
    type AudioStream_AudioMapping struct {
    
    	// Required. The `Channel`
    	// [InputAttachment.key][google.cloud.video.livestream.v1.InputAttachment.key]
    	// that identifies the input that this audio mapping applies to. If an
    	// active input doesn't have an audio mapping, the primary audio track in
    	// the input stream will be selected.
    	InputKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=input_key,json=inputKey,proto3" json:"input_key,omitempty"`
    	// Required. The zero-based index of the track in the input stream.
    	// All [mapping][google.cloud.video.livestream.v1.AudioStream.mapping]s in
    	// the same [AudioStream][google.cloud.video.livestream.v1.AudioStream] must
    	// have the same input track.
    	InputTrack [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=input_track,json=inputTrack,proto3" json:"input_track,omitempty"`
    	// Required. The zero-based index of the channel in the input stream.
    	InputChannel [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=input_channel,json=inputChannel,proto3" json:"input_channel,omitempty"`
    	// Required. The zero-based index of the channel in the output audio stream.
    	// Must be consistent with the
    	// [input_channel][google.cloud.video.livestream.v1.AudioStream.AudioMapping.input_channel].
    	OutputChannel [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=output_channel,json=outputChannel,proto3" json:"output_channel,omitempty"`
    	// Audio volume control in dB. Negative values decrease volume,
    	// positive values increase. The default is 0.
    	GainDb [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,5,opt,name=gain_db,json=gainDb,proto3" json:"gain_db,omitempty"`
    	// contains filtered or unexported fields
    }

The mapping for the input streams and audio channels.

### func (*AudioStream_AudioMapping) Descriptor 
    
    
    func (*AudioStream_AudioMapping) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AudioStream_AudioMapping.ProtoReflect.Descriptor instead.

### func (*AudioStream_AudioMapping) GetGainDb 
    
    
    func (x *AudioStream_AudioMapping) GetGainDb() [float64](https://pkg.go.dev/builtin#float64)

### func (*AudioStream_AudioMapping) GetInputChannel 
    
    
    func (x *AudioStream_AudioMapping) GetInputChannel() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream_AudioMapping) GetInputKey 
    
    
    func (x *AudioStream_AudioMapping) GetInputKey() [string](https://pkg.go.dev/builtin#string)

### func (*AudioStream_AudioMapping) GetInputTrack 
    
    
    func (x *AudioStream_AudioMapping) GetInputTrack() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream_AudioMapping) GetOutputChannel 
    
    
    func (x *AudioStream_AudioMapping) GetOutputChannel() [int32](https://pkg.go.dev/builtin#int32)

### func (*AudioStream_AudioMapping) ProtoMessage 
    
    
    func (*AudioStream_AudioMapping) ProtoMessage()

### func (*AudioStream_AudioMapping) ProtoReflect 
    
    
    func (x *AudioStream_AudioMapping) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AudioStream_AudioMapping) Reset 
    
    
    func (x *AudioStream_AudioMapping) Reset()

### func (*AudioStream_AudioMapping) String 
    
    
    func (x *AudioStream_AudioMapping) String() [string](https://pkg.go.dev/builtin#string)

## AutoTranscriptionConfig
    
    
    type AutoTranscriptionConfig struct {
    
    	// Optional. Whether auto-generated text streams are displayed synchronously
    	// or asynchronously with the original audio.
    	DisplayTiming AutoTranscriptionConfig_DisplayTiming `protobuf:"varint,1,opt,name=display_timing,json=displayTiming,proto3,enum=google.cloud.video.livestream.v1.AutoTranscriptionConfig_DisplayTiming" json:"display_timing,omitempty"`
    	// Optional. Tunes the latency and quality of auto-generated captions.
    	QualityPreset AutoTranscriptionConfig_QualityPreset `protobuf:"varint,2,opt,name=quality_preset,json=qualityPreset,proto3,enum=google.cloud.video.livestream.v1.AutoTranscriptionConfig_QualityPreset" json:"quality_preset,omitempty"`
    	// contains filtered or unexported fields
    }

Advanced configurations for auto-generated text streams.

### func (*AutoTranscriptionConfig) Descriptor 
    
    
    func (*AutoTranscriptionConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutoTranscriptionConfig.ProtoReflect.Descriptor instead.

### func (*AutoTranscriptionConfig) GetDisplayTiming 
    
    
    func (x *AutoTranscriptionConfig) GetDisplayTiming() AutoTranscriptionConfig_DisplayTiming

### func (*AutoTranscriptionConfig) GetQualityPreset 
    
    
    func (x *AutoTranscriptionConfig) GetQualityPreset() AutoTranscriptionConfig_QualityPreset

### func (*AutoTranscriptionConfig) ProtoMessage 
    
    
    func (*AutoTranscriptionConfig) ProtoMessage()

### func (*AutoTranscriptionConfig) ProtoReflect 
    
    
    func (x *AutoTranscriptionConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AutoTranscriptionConfig) Reset 
    
    
    func (x *AutoTranscriptionConfig) Reset()

### func (*AutoTranscriptionConfig) String 
    
    
    func (x *AutoTranscriptionConfig) String() [string](https://pkg.go.dev/builtin#string)

## AutoTranscriptionConfig_DisplayTiming
    
    
    type AutoTranscriptionConfig_DisplayTiming [int32](https://pkg.go.dev/builtin#int32)

Whether auto-generated text streams are displayed synchronously or asynchronously with the original audio.

### AutoTranscriptionConfig_DISPLAY_TIMING_UNSPECIFIED, AutoTranscriptionConfig_ASYNC, AutoTranscriptionConfig_SYNC
    
    
    const (
    	// Display timing is not specified. Caption display will be asynchronous by
    	// default.
    	AutoTranscriptionConfig_DISPLAY_TIMING_UNSPECIFIED AutoTranscriptionConfig_DisplayTiming = 0
    	// Caption will be displayed asynchronous with audio.
    	AutoTranscriptionConfig_ASYNC AutoTranscriptionConfig_DisplayTiming = 1
    	// Caption will be displayed synchronous with audio. This option increases
    	// overall media output latency, and reduces viewing latency between audio
    	// and auto-generated captions.
    	AutoTranscriptionConfig_SYNC AutoTranscriptionConfig_DisplayTiming = 2
    )

### func (AutoTranscriptionConfig_DisplayTiming) Descriptor 
    
    
    func (AutoTranscriptionConfig_DisplayTiming) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AutoTranscriptionConfig_DisplayTiming) Enum 
    
    
    func (x AutoTranscriptionConfig_DisplayTiming) Enum() *AutoTranscriptionConfig_DisplayTiming

### func (AutoTranscriptionConfig_DisplayTiming) EnumDescriptor 
    
    
    func (AutoTranscriptionConfig_DisplayTiming) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutoTranscriptionConfig_DisplayTiming.Descriptor instead.

### func (AutoTranscriptionConfig_DisplayTiming) Number 
    
    
    func (x AutoTranscriptionConfig_DisplayTiming) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AutoTranscriptionConfig_DisplayTiming) String 
    
    
    func (x AutoTranscriptionConfig_DisplayTiming) String() [string](https://pkg.go.dev/builtin#string)

### func (AutoTranscriptionConfig_DisplayTiming) Type 
    
    
    func (AutoTranscriptionConfig_DisplayTiming) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## AutoTranscriptionConfig_QualityPreset
    
    
    type AutoTranscriptionConfig_QualityPreset [int32](https://pkg.go.dev/builtin#int32)

Presets to tune the latency and quality of auto-generated captions.

### AutoTranscriptionConfig_QUALITY_PRESET_UNSPECIFIED, AutoTranscriptionConfig_LOW_LATENCY, AutoTranscriptionConfig_BALANCED_QUALITY, AutoTranscriptionConfig_IMPROVED_QUALITY
    
    
    const (
    	// Quality Preset is not specified. By default, BALANCED_QUALITY will be
    	// used.
    	AutoTranscriptionConfig_QUALITY_PRESET_UNSPECIFIED AutoTranscriptionConfig_QualityPreset = 0
    	// Reduce the latency of auto-generated captions. This may reduce the
    	// quality of the captions.
    	AutoTranscriptionConfig_LOW_LATENCY AutoTranscriptionConfig_QualityPreset = 1
    	// Default behavior when QualityPreset is not specified.
    	AutoTranscriptionConfig_BALANCED_QUALITY AutoTranscriptionConfig_QualityPreset = 2
    	// Increases the quality of the auto-generated captions at the cost of
    	// higher latency.
    	AutoTranscriptionConfig_IMPROVED_QUALITY AutoTranscriptionConfig_QualityPreset = 3
    )

### func (AutoTranscriptionConfig_QualityPreset) Descriptor 
    
    
    func (AutoTranscriptionConfig_QualityPreset) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AutoTranscriptionConfig_QualityPreset) Enum 
    
    
    func (x AutoTranscriptionConfig_QualityPreset) Enum() *AutoTranscriptionConfig_QualityPreset

### func (AutoTranscriptionConfig_QualityPreset) EnumDescriptor 
    
    
    func (AutoTranscriptionConfig_QualityPreset) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AutoTranscriptionConfig_QualityPreset.Descriptor instead.

### func (AutoTranscriptionConfig_QualityPreset) Number 
    
    
    func (x AutoTranscriptionConfig_QualityPreset) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AutoTranscriptionConfig_QualityPreset) String 
    
    
    func (x AutoTranscriptionConfig_QualityPreset) String() [string](https://pkg.go.dev/builtin#string)

### func (AutoTranscriptionConfig_QualityPreset) Type 
    
    
    func (AutoTranscriptionConfig_QualityPreset) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Channel
    
    
    type Channel struct {
    
    	// The resource name of the channel, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// A list of input attachments that this channel uses.
    	// One channel can have multiple inputs as the input sources. Only one
    	// input can be selected as the input source at one time.
    	InputAttachments []*InputAttachment `protobuf:"bytes,16,rep,name=input_attachments,json=inputAttachments,proto3" json:"input_attachments,omitempty"`
    	// Output only. The
    	// [InputAttachment.key][google.cloud.video.livestream.v1.InputAttachment.key]
    	// that serves as the current input source. The first input in the
    	// [input_attachments][google.cloud.video.livestream.v1.Channel.input_attachments]
    	// is the initial input source.
    	ActiveInput [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=active_input,json=activeInput,proto3" json:"active_input,omitempty"`
    	// Required. Information about the output (that is, the Cloud Storage bucket
    	// to store the generated live stream).
    	Output *Channel_Output `protobuf:"bytes,9,opt,name=output,proto3" json:"output,omitempty"`
    	// List of elementary streams.
    	ElementaryStreams []*ElementaryStream `protobuf:"bytes,10,rep,name=elementary_streams,json=elementaryStreams,proto3" json:"elementary_streams,omitempty"`
    	// List of multiplexing settings for output streams.
    	MuxStreams []*MuxStream `protobuf:"bytes,11,rep,name=mux_streams,json=muxStreams,proto3" json:"mux_streams,omitempty"`
    	// List of output manifests.
    	Manifests []*Manifest `protobuf:"bytes,12,rep,name=manifests,proto3" json:"manifests,omitempty"`
    	// Optional. List of multiplexing settings of streams for distributions.
    	DistributionStreams []*DistributionStream `protobuf:"bytes,28,rep,name=distribution_streams,json=distributionStreams,proto3" json:"distribution_streams,omitempty"`
    	// Optional. List of distributions.
    	Distributions []*Distribution `protobuf:"bytes,29,rep,name=distributions,proto3" json:"distributions,omitempty"`
    	// List of output sprite sheets.
    	SpriteSheets []*SpriteSheet `protobuf:"bytes,13,rep,name=sprite_sheets,json=spriteSheets,proto3" json:"sprite_sheets,omitempty"`
    	// Output only. State of the streaming operation.
    	StreamingState Channel_StreamingState `protobuf:"varint,14,opt,name=streaming_state,json=streamingState,proto3,enum=google.cloud.video.livestream.v1.Channel_StreamingState" json:"streaming_state,omitempty"`
    	// Output only. A description of the reason for the streaming error. This
    	// property is always present when
    	// [streaming_state][google.cloud.video.livestream.v1.Channel.streaming_state]
    	// is
    	// [STREAMING_ERROR][google.cloud.video.livestream.v1.Channel.StreamingState.STREAMING_ERROR].
    	StreamingError *status.Status `protobuf:"bytes,18,opt,name=streaming_error,json=streamingError,proto3" json:"streaming_error,omitempty"`
    	// Configuration of platform logs for this channel.
    	LogConfig *LogConfig `protobuf:"bytes,19,opt,name=log_config,json=logConfig,proto3" json:"log_config,omitempty"`
    	// Configuration of timecode for this channel.
    	TimecodeConfig *TimecodeConfig `protobuf:"bytes,21,opt,name=timecode_config,json=timecodeConfig,proto3" json:"timecode_config,omitempty"`
    	// Optional. Encryption configurations for this channel. Each configuration
    	// has an ID which is referred to by each MuxStream to indicate which
    	// configuration is used for that output.
    	Encryptions []*Encryption `protobuf:"bytes,24,rep,name=encryptions,proto3" json:"encryptions,omitempty"`
    	// The configuration for input sources defined in
    	// [input_attachments][google.cloud.video.livestream.v1.Channel.input_attachments].
    	InputConfig *InputConfig `protobuf:"bytes,25,opt,name=input_config,json=inputConfig,proto3" json:"input_config,omitempty"`
    	// Optional. Configuration for retention of output files for this channel.
    	RetentionConfig *RetentionConfig `protobuf:"bytes,26,opt,name=retention_config,json=retentionConfig,proto3" json:"retention_config,omitempty"`
    	// Optional. List of static overlay images. Those images display over the
    	// output content for the whole duration of the live stream.
    	StaticOverlays []*StaticOverlay `protobuf:"bytes,27,rep,name=static_overlays,json=staticOverlays,proto3" json:"static_overlays,omitempty"`
    	// Optional. Advanced configurations for auto-generated text streams.
    	AutoTranscriptionConfig *AutoTranscriptionConfig `protobuf:"bytes,30,opt,name=auto_transcription_config,json=autoTranscriptionConfig,proto3" json:"auto_transcription_config,omitempty"`
    	// contains filtered or unexported fields
    }

Channel resource represents the processor that does a user-defined "streaming" operation, which includes getting an input stream through an input, transcoding it to multiple renditions, and publishing output live streams in certain formats (for example, HLS or DASH) to the specified location.

### func (*Channel) Descriptor 
    
    
    func (*Channel) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Channel.ProtoReflect.Descriptor instead.

### func (*Channel) GetActiveInput 
    
    
    func (x *Channel) GetActiveInput() [string](https://pkg.go.dev/builtin#string)

### func (*Channel) GetAutoTranscriptionConfig 
    
    
    func (x *Channel) GetAutoTranscriptionConfig() *AutoTranscriptionConfig

### func (*Channel) GetCreateTime 
    
    
    func (x *Channel) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Channel) GetDistributionStreams 
    
    
    func (x *Channel) GetDistributionStreams() []*DistributionStream

### func (*Channel) GetDistributions 
    
    
    func (x *Channel) GetDistributions() []*Distribution

### func (*Channel) GetElementaryStreams 
    
    
    func (x *Channel) GetElementaryStreams() []*ElementaryStream

### func (*Channel) GetEncryptions 
    
    
    func (x *Channel) GetEncryptions() []*Encryption

### func (*Channel) GetInputAttachments 
    
    
    func (x *Channel) GetInputAttachments() []*InputAttachment

### func (*Channel) GetInputConfig 
    
    
    func (x *Channel) GetInputConfig() *InputConfig

### func (*Channel) GetLabels 
    
    
    func (x *Channel) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Channel) GetLogConfig 
    
    
    func (x *Channel) GetLogConfig() *LogConfig

### func (*Channel) GetManifests 
    
    
    func (x *Channel) GetManifests() []*Manifest

### func (*Channel) GetMuxStreams 
    
    
    func (x *Channel) GetMuxStreams() []*MuxStream

### func (*Channel) GetName 
    
    
    func (x *Channel) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Channel) GetOutput 
    
    
    func (x *Channel) GetOutput() *Channel_Output

### func (*Channel) GetRetentionConfig 
    
    
    func (x *Channel) GetRetentionConfig() *RetentionConfig

### func (*Channel) GetSpriteSheets 
    
    
    func (x *Channel) GetSpriteSheets() []*SpriteSheet

### func (*Channel) GetStaticOverlays 
    
    
    func (x *Channel) GetStaticOverlays() []*StaticOverlay

### func (*Channel) GetStreamingError 
    
    
    func (x *Channel) GetStreamingError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*Channel) GetStreamingState 
    
    
    func (x *Channel) GetStreamingState() Channel_StreamingState

### func (*Channel) GetTimecodeConfig 
    
    
    func (x *Channel) GetTimecodeConfig() *TimecodeConfig

### func (*Channel) GetUpdateTime 
    
    
    func (x *Channel) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Channel) ProtoMessage 
    
    
    func (*Channel) ProtoMessage()

### func (*Channel) ProtoReflect 
    
    
    func (x *Channel) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Channel) Reset 
    
    
    func (x *Channel) Reset()

### func (*Channel) String 
    
    
    func (x *Channel) String() [string](https://pkg.go.dev/builtin#string)

## ChannelOperationResponse
    
    
    type ChannelOperationResponse struct {
    	// contains filtered or unexported fields
    }

Response message for Start/Stop Channel long-running operations.

### func (*ChannelOperationResponse) Descriptor 
    
    
    func (*ChannelOperationResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ChannelOperationResponse.ProtoReflect.Descriptor instead.

### func (*ChannelOperationResponse) ProtoMessage 
    
    
    func (*ChannelOperationResponse) ProtoMessage()

### func (*ChannelOperationResponse) ProtoReflect 
    
    
    func (x *ChannelOperationResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ChannelOperationResponse) Reset 
    
    
    func (x *ChannelOperationResponse) Reset()

### func (*ChannelOperationResponse) String 
    
    
    func (x *ChannelOperationResponse) String() [string](https://pkg.go.dev/builtin#string)

## Channel_Output
    
    
    type Channel_Output struct {
    
    	// URI for the output file(s). For example, `gs://my-bucket/outputs/`.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// contains filtered or unexported fields
    }

Location of output file(s) in a Google Cloud Storage bucket.

### func (*Channel_Output) Descriptor 
    
    
    func (*Channel_Output) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Channel_Output.ProtoReflect.Descriptor instead.

### func (*Channel_Output) GetUri 
    
    
    func (x *Channel_Output) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Channel_Output) ProtoMessage 
    
    
    func (*Channel_Output) ProtoMessage()

### func (*Channel_Output) ProtoReflect 
    
    
    func (x *Channel_Output) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Channel_Output) Reset 
    
    
    func (x *Channel_Output) Reset()

### func (*Channel_Output) String 
    
    
    func (x *Channel_Output) String() [string](https://pkg.go.dev/builtin#string)

## Channel_StreamingState
    
    
    type Channel_StreamingState [int32](https://pkg.go.dev/builtin#int32)

State of streaming operation that the channel is running.

### Channel_STREAMING_STATE_UNSPECIFIED, Channel_STREAMING, Channel_AWAITING_INPUT, Channel_STREAMING_ERROR, Channel_STREAMING_NO_INPUT, Channel_STOPPED, Channel_STARTING, Channel_STOPPING
    
    
    const (
    	// Streaming state is not specified.
    	Channel_STREAMING_STATE_UNSPECIFIED Channel_StreamingState = 0
    	// Channel is getting the input stream, generating the live streams to the
    	// specified output location.
    	Channel_STREAMING Channel_StreamingState = 1
    	// Channel is waiting for the input stream through the input.
    	Channel_AWAITING_INPUT Channel_StreamingState = 2
    	// Channel is running, but has trouble publishing the live streams onto the
    	// specified output location (for example, the specified Cloud Storage
    	// bucket is not writable).
    	Channel_STREAMING_ERROR Channel_StreamingState = 4
    	// Channel is generating live streams with no input stream. Live streams are
    	// filled out with black screen, while input stream is missing.
    	// Not supported yet.
    	Channel_STREAMING_NO_INPUT Channel_StreamingState = 5
    	// Channel is stopped, finishing live streams.
    	Channel_STOPPED Channel_StreamingState = 6
    	// Channel is starting.
    	Channel_STARTING Channel_StreamingState = 7
    	// Channel is stopping.
    	Channel_STOPPING Channel_StreamingState = 8
    )

### func (Channel_StreamingState) Descriptor 
    
    
    func (Channel_StreamingState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Channel_StreamingState) Enum 
    
    
    func (x Channel_StreamingState) Enum() *Channel_StreamingState

### func (Channel_StreamingState) EnumDescriptor 
    
    
    func (Channel_StreamingState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Channel_StreamingState.Descriptor instead.

### func (Channel_StreamingState) Number 
    
    
    func (x Channel_StreamingState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Channel_StreamingState) String 
    
    
    func (x Channel_StreamingState) String() [string](https://pkg.go.dev/builtin#string)

### func (Channel_StreamingState) Type 
    
    
    func (Channel_StreamingState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Clip
    
    
    type Clip struct {
    
    	// The resource name of the clip, in the following format:
    	// `projects/{project}/locations/{location}/channels/{channelId}/clips/{clipId}`.
    	// `{clipId}` is a user-specified resource id that conforms to the following
    	// criteria:
    	//
    	// 1. 1 character minimum, 63 characters maximum
    	// 2. Only contains letters, digits, underscores, and hyphens
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation timestamp of the clip resource.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the clip request starts to be processed.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// Output only. The update timestamp of the clip resource.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// The labels associated with this resource. Each label is a key-value pair.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Output only. The state of the clip.
    	State Clip_State `protobuf:"varint,6,opt,name=state,proto3,enum=google.cloud.video.livestream.v1.Clip_State" json:"state,omitempty"`
    	// Specify the `output_uri` to determine where to place the clip segments and
    	// clip manifest files in Cloud Storage. The manifests specified in
    	// `clip_manifests` fields will be placed under this URI. The exact URI of the
    	// generated manifests will be provided in `clip_manifests.output_uri` for
    	// each manifest.
    	// Example:
    	// "output_uri": "gs://my-bucket/clip-outputs"
    	// "clip_manifests.output_uri": "gs://my-bucket/clip-outputs/main.m3u8"
    	OutputUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=output_uri,json=outputUri,proto3" json:"output_uri,omitempty"`
    	// Output only. An error object that describes the reason for the failure.
    	// This property only presents when `state` is `FAILED`.
    	Error *status.Status `protobuf:"bytes,9,opt,name=error,proto3" json:"error,omitempty"`
    	// The specified ranges of segments to generate a clip.
    	Slices []*Clip_Slice `protobuf:"bytes,10,rep,name=slices,proto3" json:"slices,omitempty"`
    	// Required. A list of clip manifests. Currently only one clip manifest is
    	// allowed.
    	ClipManifests []*Clip_ClipManifest `protobuf:"bytes,12,rep,name=clip_manifests,json=clipManifests,proto3" json:"clip_manifests,omitempty"`
    	// Optional. OutputType of the clip. If not specified, the default value is
    	// MANIFEST.
    	OutputType Clip_OutputType `protobuf:"varint,13,opt,name=output_type,json=outputType,proto3,enum=google.cloud.video.livestream.v1.Clip_OutputType" json:"output_type,omitempty"`
    	// contains filtered or unexported fields
    }

Clip is a sub-resource under channel. Each clip represents a clipping operation that generates a VOD playlist from its channel given a set of timestamp ranges.

### func (*Clip) Descriptor 
    
    
    func (*Clip) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip.ProtoReflect.Descriptor instead.

### func (*Clip) GetClipManifests 
    
    
    func (x *Clip) GetClipManifests() []*Clip_ClipManifest

### func (*Clip) GetCreateTime 
    
    
    func (x *Clip) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Clip) GetError 
    
    
    func (x *Clip) GetError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*Clip) GetLabels 
    
    
    func (x *Clip) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Clip) GetName 
    
    
    func (x *Clip) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Clip) GetOutputType 
    
    
    func (x *Clip) GetOutputType() Clip_OutputType

### func (*Clip) GetOutputUri 
    
    
    func (x *Clip) GetOutputUri() [string](https://pkg.go.dev/builtin#string)

### func (*Clip) GetSlices 
    
    
    func (x *Clip) GetSlices() []*Clip_Slice

### func (*Clip) GetStartTime 
    
    
    func (x *Clip) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Clip) GetState 
    
    
    func (x *Clip) GetState() Clip_State

### func (*Clip) GetUpdateTime 
    
    
    func (x *Clip) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Clip) ProtoMessage 
    
    
    func (*Clip) ProtoMessage()

### func (*Clip) ProtoReflect 
    
    
    func (x *Clip) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Clip) Reset 
    
    
    func (x *Clip) Reset()

### func (*Clip) String 
    
    
    func (x *Clip) String() [string](https://pkg.go.dev/builtin#string)

## Clip_ClipManifest
    
    
    type Clip_ClipManifest struct {
    
    	// Required. A unique key that identifies a manifest config in the parent
    	// channel. This key is the same as `channel.manifests.key` for the selected
    	// manifest.
    	ManifestKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=manifest_key,json=manifestKey,proto3" json:"manifest_key,omitempty"`
    	// Output only. The output URI of the generated clip manifest. This field
    	// will be populated when the CreateClip request is accepted. Current output
    	// format is provided below but may change in the future. Please read this
    	// field to get the uri to the generated clip manifest. Format:
    	// {clip.output_uri}/{channel.manifest.fileName} Example:
    	// gs://my-bucket/clip-outputs/main.m3u8
    	OutputUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=output_uri,json=outputUri,proto3" json:"output_uri,omitempty"`
    	// contains filtered or unexported fields
    }

ClipManifest identifies a source manifest for the generated clip manifest.

### func (*Clip_ClipManifest) Descriptor 
    
    
    func (*Clip_ClipManifest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip_ClipManifest.ProtoReflect.Descriptor instead.

### func (*Clip_ClipManifest) GetManifestKey 
    
    
    func (x *Clip_ClipManifest) GetManifestKey() [string](https://pkg.go.dev/builtin#string)

### func (*Clip_ClipManifest) GetOutputUri 
    
    
    func (x *Clip_ClipManifest) GetOutputUri() [string](https://pkg.go.dev/builtin#string)

### func (*Clip_ClipManifest) ProtoMessage 
    
    
    func (*Clip_ClipManifest) ProtoMessage()

### func (*Clip_ClipManifest) ProtoReflect 
    
    
    func (x *Clip_ClipManifest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Clip_ClipManifest) Reset 
    
    
    func (x *Clip_ClipManifest) Reset()

### func (*Clip_ClipManifest) String 
    
    
    func (x *Clip_ClipManifest) String() [string](https://pkg.go.dev/builtin#string)

## Clip_OutputType
    
    
    type Clip_OutputType [int32](https://pkg.go.dev/builtin#int32)

OutputType represents the output type of the clip.

### Clip_OUTPUT_TYPE_UNSPECIFIED, Clip_MANIFEST, Clip_MP4
    
    
    const (
    	// OutputType is not specified.
    	Clip_OUTPUT_TYPE_UNSPECIFIED Clip_OutputType = 0
    	// OutputType is a VOD manifest. This is the default value.
    	Clip_MANIFEST Clip_OutputType = 1
    	// OutputType is an MP4 file.
    	Clip_MP4 Clip_OutputType = 2
    )

### func (Clip_OutputType) Descriptor 
    
    
    func (Clip_OutputType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Clip_OutputType) Enum 
    
    
    func (x Clip_OutputType) Enum() *Clip_OutputType

### func (Clip_OutputType) EnumDescriptor 
    
    
    func (Clip_OutputType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip_OutputType.Descriptor instead.

### func (Clip_OutputType) Number 
    
    
    func (x Clip_OutputType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Clip_OutputType) String 
    
    
    func (x Clip_OutputType) String() [string](https://pkg.go.dev/builtin#string)

### func (Clip_OutputType) Type 
    
    
    func (Clip_OutputType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Clip_Slice
    
    
    type Clip_Slice struct {
    
    	// The allowlist forms of a slice.
    	//
    	// Types that are valid to be assigned to Kind:
    	//
    	//	*Clip_Slice_TimeSlice
    	Kind isClip_Slice_Kind `protobuf_oneof:"kind"`
    	// contains filtered or unexported fields
    }

Slice represents a slice of the requested clip.

### func (*Clip_Slice) Descriptor 
    
    
    func (*Clip_Slice) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip_Slice.ProtoReflect.Descriptor instead.

### func (*Clip_Slice) GetKind 
    
    
    func (x *Clip_Slice) GetKind() isClip_Slice_Kind

### func (*Clip_Slice) GetTimeSlice 
    
    
    func (x *Clip_Slice) GetTimeSlice() *Clip_TimeSlice

### func (*Clip_Slice) ProtoMessage 
    
    
    func (*Clip_Slice) ProtoMessage()

### func (*Clip_Slice) ProtoReflect 
    
    
    func (x *Clip_Slice) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Clip_Slice) Reset 
    
    
    func (x *Clip_Slice) Reset()

### func (*Clip_Slice) String 
    
    
    func (x *Clip_Slice) String() [string](https://pkg.go.dev/builtin#string)

## Clip_Slice_TimeSlice
    
    
    type Clip_Slice_TimeSlice struct {
    	// A slice in form of a tuple of Unix epoch time.
    	TimeSlice *Clip_TimeSlice `protobuf:"bytes,1,opt,name=time_slice,json=timeSlice,proto3,oneof"`
    }

## Clip_State
    
    
    type Clip_State [int32](https://pkg.go.dev/builtin#int32)

State of clipping operation.

### Clip_STATE_UNSPECIFIED, Clip_PENDING, Clip_CREATING, Clip_SUCCEEDED, Clip_FAILED
    
    
    const (
    	// State is not specified.
    	Clip_STATE_UNSPECIFIED Clip_State = 0
    	// The operation is pending to be picked up by the server.
    	Clip_PENDING Clip_State = 1
    	// The server admitted this create clip request, and
    	// outputs are under processing.
    	Clip_CREATING Clip_State = 2
    	// Outputs are available in the specified Cloud Storage bucket. For
    	// additional information, see the `outputs` field.
    	Clip_SUCCEEDED Clip_State = 3
    	// The operation has failed. For additional information, see the `error`
    	// field.
    	Clip_FAILED Clip_State = 4
    )

### func (Clip_State) Descriptor 
    
    
    func (Clip_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Clip_State) Enum 
    
    
    func (x Clip_State) Enum() *Clip_State

### func (Clip_State) EnumDescriptor 
    
    
    func (Clip_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip_State.Descriptor instead.

### func (Clip_State) Number 
    
    
    func (x Clip_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Clip_State) String 
    
    
    func (x Clip_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Clip_State) Type 
    
    
    func (Clip_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Clip_TimeSlice
    
    
    type Clip_TimeSlice struct {
    
    	// The mark-in Unix epoch time in the original live stream manifest.
    	MarkinTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=markin_time,json=markinTime,proto3" json:"markin_time,omitempty"`
    	// The mark-out Unix epoch time in the original live stream manifest.
    	MarkoutTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=markout_time,json=markoutTime,proto3" json:"markout_time,omitempty"`
    	// contains filtered or unexported fields
    }

TimeSlice represents a tuple of Unix epoch timestamps that specifies a time range.

### func (*Clip_TimeSlice) Descriptor 
    
    
    func (*Clip_TimeSlice) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Clip_TimeSlice.ProtoReflect.Descriptor instead.

### func (*Clip_TimeSlice) GetMarkinTime 
    
    
    func (x *Clip_TimeSlice) GetMarkinTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Clip_TimeSlice) GetMarkoutTime 
    
    
    func (x *Clip_TimeSlice) GetMarkoutTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Clip_TimeSlice) ProtoMessage 
    
    
    func (*Clip_TimeSlice) ProtoMessage()

### func (*Clip_TimeSlice) ProtoReflect 
    
    
    func (x *Clip_TimeSlice) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Clip_TimeSlice) Reset 
    
    
    func (x *Clip_TimeSlice) Reset()

### func (*Clip_TimeSlice) String 
    
    
    func (x *Clip_TimeSlice) String() [string](https://pkg.go.dev/builtin#string)

## CreateAssetRequest
    
    
    type CreateAssetRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The asset resource to be created.
    	Asset *Asset `protobuf:"bytes,2,opt,name=asset,proto3" json:"asset,omitempty"`
    	// Required. The ID of the asset resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	AssetId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=asset_id,json=assetId,proto3" json:"asset_id,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.CreateAsset".

### func (*CreateAssetRequest) Descriptor 
    
    
    func (*CreateAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateAssetRequest.ProtoReflect.Descriptor instead.

### func (*CreateAssetRequest) GetAsset 
    
    
    func (x *CreateAssetRequest) GetAsset() *Asset

### func (*CreateAssetRequest) GetAssetId 
    
    
    func (x *CreateAssetRequest) GetAssetId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAssetRequest) GetParent 
    
    
    func (x *CreateAssetRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAssetRequest) GetRequestId 
    
    
    func (x *CreateAssetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateAssetRequest) ProtoMessage 
    
    
    func (*CreateAssetRequest) ProtoMessage()

### func (*CreateAssetRequest) ProtoReflect 
    
    
    func (x *CreateAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateAssetRequest) Reset 
    
    
    func (x *CreateAssetRequest) Reset()

### func (*CreateAssetRequest) String 
    
    
    func (x *CreateAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateChannelRequest
    
    
    type CreateChannelRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The channel resource to be created.
    	Channel *Channel `protobuf:"bytes,2,opt,name=channel,proto3" json:"channel,omitempty"`
    	// Required. The ID of the channel resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	ChannelId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=channel_id,json=channelId,proto3" json:"channel_id,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.CreateChannel".

### func (*CreateChannelRequest) Descriptor 
    
    
    func (*CreateChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateChannelRequest.ProtoReflect.Descriptor instead.

### func (*CreateChannelRequest) GetChannel 
    
    
    func (x *CreateChannelRequest) GetChannel() *Channel

### func (*CreateChannelRequest) GetChannelId 
    
    
    func (x *CreateChannelRequest) GetChannelId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateChannelRequest) GetParent 
    
    
    func (x *CreateChannelRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateChannelRequest) GetRequestId 
    
    
    func (x *CreateChannelRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateChannelRequest) ProtoMessage 
    
    
    func (*CreateChannelRequest) ProtoMessage()

### func (*CreateChannelRequest) ProtoReflect 
    
    
    func (x *CreateChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateChannelRequest) Reset 
    
    
    func (x *CreateChannelRequest) Reset()

### func (*CreateChannelRequest) String 
    
    
    func (x *CreateChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateClipRequest
    
    
    type CreateClipRequest struct {
    
    	// Required. The parent resource name, in the following form:
    	// `projects/{project}/locations/{location}/channels/{channel}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The ID of the clip resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	ClipId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=clip_id,json=clipId,proto3" json:"clip_id,omitempty"`
    	// Required. The resource being created
    	Clip *Clip `protobuf:"bytes,3,opt,name=clip,proto3" json:"clip,omitempty"`
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

Request message for "LivestreamService.CreateClip".

### func (*CreateClipRequest) Descriptor 
    
    
    func (*CreateClipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateClipRequest.ProtoReflect.Descriptor instead.

### func (*CreateClipRequest) GetClip 
    
    
    func (x *CreateClipRequest) GetClip() *Clip

### func (*CreateClipRequest) GetClipId 
    
    
    func (x *CreateClipRequest) GetClipId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateClipRequest) GetParent 
    
    
    func (x *CreateClipRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateClipRequest) GetRequestId 
    
    
    func (x *CreateClipRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateClipRequest) ProtoMessage 
    
    
    func (*CreateClipRequest) ProtoMessage()

### func (*CreateClipRequest) ProtoReflect 
    
    
    func (x *CreateClipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateClipRequest) Reset 
    
    
    func (x *CreateClipRequest) Reset()

### func (*CreateClipRequest) String 
    
    
    func (x *CreateClipRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateDvrSessionRequest
    
    
    type CreateDvrSessionRequest struct {
    
    	// Required. The parent resource name, in the following form:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The ID of the DVR session resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	DvrSessionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=dvr_session_id,json=dvrSessionId,proto3" json:"dvr_session_id,omitempty"`
    	// Required. The resource being created
    	DvrSession *DvrSession `protobuf:"bytes,3,opt,name=dvr_session,json=dvrSession,proto3" json:"dvr_session,omitempty"`
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

Request message for "LivestreamService.CreateDvrSession".

### func (*CreateDvrSessionRequest) Descriptor 
    
    
    func (*CreateDvrSessionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateDvrSessionRequest.ProtoReflect.Descriptor instead.

### func (*CreateDvrSessionRequest) GetDvrSession 
    
    
    func (x *CreateDvrSessionRequest) GetDvrSession() *DvrSession

### func (*CreateDvrSessionRequest) GetDvrSessionId 
    
    
    func (x *CreateDvrSessionRequest) GetDvrSessionId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDvrSessionRequest) GetParent 
    
    
    func (x *CreateDvrSessionRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDvrSessionRequest) GetRequestId 
    
    
    func (x *CreateDvrSessionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDvrSessionRequest) ProtoMessage 
    
    
    func (*CreateDvrSessionRequest) ProtoMessage()

### func (*CreateDvrSessionRequest) ProtoReflect 
    
    
    func (x *CreateDvrSessionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateDvrSessionRequest) Reset 
    
    
    func (x *CreateDvrSessionRequest) Reset()

### func (*CreateDvrSessionRequest) String 
    
    
    func (x *CreateDvrSessionRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateEventRequest
    
    
    type CreateEventRequest struct {
    
    	// Required. The parent channel for the resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The event resource to be created.
    	Event *Event `protobuf:"bytes,2,opt,name=event,proto3" json:"event,omitempty"`
    	// Required. The ID of the event resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	EventId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.CreateEvent".

### func (*CreateEventRequest) Descriptor 
    
    
    func (*CreateEventRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateEventRequest.ProtoReflect.Descriptor instead.

### func (*CreateEventRequest) GetEvent 
    
    
    func (x *CreateEventRequest) GetEvent() *Event

### func (*CreateEventRequest) GetEventId 
    
    
    func (x *CreateEventRequest) GetEventId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateEventRequest) GetParent 
    
    
    func (x *CreateEventRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateEventRequest) GetRequestId 
    
    
    func (x *CreateEventRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateEventRequest) ProtoMessage 
    
    
    func (*CreateEventRequest) ProtoMessage()

### func (*CreateEventRequest) ProtoReflect 
    
    
    func (x *CreateEventRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateEventRequest) Reset 
    
    
    func (x *CreateEventRequest) Reset()

### func (*CreateEventRequest) String 
    
    
    func (x *CreateEventRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateInputRequest
    
    
    type CreateInputRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The input resource to be created.
    	Input *Input `protobuf:"bytes,2,opt,name=input,proto3" json:"input,omitempty"`
    	// Required. The ID of the input resource to be created.
    	//
    	// This value must be 1-63 characters, begin and end with a lower-case letter
    	// or a number, and consist of only lower-case letters, numbers, and hyphens.
    	// In other words, it must match the following regex:
    	// `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`.
    	InputId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=input_id,json=inputId,proto3" json:"input_id,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.CreateInput".

### func (*CreateInputRequest) Descriptor 
    
    
    func (*CreateInputRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateInputRequest.ProtoReflect.Descriptor instead.

### func (*CreateInputRequest) GetInput 
    
    
    func (x *CreateInputRequest) GetInput() *Input

### func (*CreateInputRequest) GetInputId 
    
    
    func (x *CreateInputRequest) GetInputId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateInputRequest) GetParent 
    
    
    func (x *CreateInputRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateInputRequest) GetRequestId 
    
    
    func (x *CreateInputRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateInputRequest) ProtoMessage 
    
    
    func (*CreateInputRequest) ProtoMessage()

### func (*CreateInputRequest) ProtoReflect 
    
    
    func (x *CreateInputRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateInputRequest) Reset 
    
    
    func (x *CreateInputRequest) Reset()

### func (*CreateInputRequest) String 
    
    
    func (x *CreateInputRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteAssetRequest
    
    
    type DeleteAssetRequest struct {
    
    	// Required. The name of the asset resource, in the form of:
    	// `projects/{project}/locations/{location}/assets/{assetId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteAsset".

### func (*DeleteAssetRequest) Descriptor 
    
    
    func (*DeleteAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteAssetRequest.ProtoReflect.Descriptor instead.

### func (*DeleteAssetRequest) GetName 
    
    
    func (x *DeleteAssetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAssetRequest) GetRequestId 
    
    
    func (x *DeleteAssetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAssetRequest) ProtoMessage 
    
    
    func (*DeleteAssetRequest) ProtoMessage()

### func (*DeleteAssetRequest) ProtoReflect 
    
    
    func (x *DeleteAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteAssetRequest) Reset 
    
    
    func (x *DeleteAssetRequest) Reset()

### func (*DeleteAssetRequest) String 
    
    
    func (x *DeleteAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteChannelRequest
    
    
    type DeleteChannelRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// If the `force` field is set to the default value of `false`, you must
    	// delete all of a channel's events before you can delete the channel itself.
    	// If the field is set to `true`, requests to delete a channel also delete
    	// associated channel events.
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteChannel".

### func (*DeleteChannelRequest) Descriptor 
    
    
    func (*DeleteChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteChannelRequest.ProtoReflect.Descriptor instead.

### func (*DeleteChannelRequest) GetForce 
    
    
    func (x *DeleteChannelRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteChannelRequest) GetName 
    
    
    func (x *DeleteChannelRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteChannelRequest) GetRequestId 
    
    
    func (x *DeleteChannelRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteChannelRequest) ProtoMessage 
    
    
    func (*DeleteChannelRequest) ProtoMessage()

### func (*DeleteChannelRequest) ProtoReflect 
    
    
    func (x *DeleteChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteChannelRequest) Reset 
    
    
    func (x *DeleteChannelRequest) Reset()

### func (*DeleteChannelRequest) String 
    
    
    func (x *DeleteChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteClipRequest
    
    
    type DeleteClipRequest struct {
    
    	// Required. The name of the clip resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}/clips/{clipId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteClip".

### func (*DeleteClipRequest) Descriptor 
    
    
    func (*DeleteClipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteClipRequest.ProtoReflect.Descriptor instead.

### func (*DeleteClipRequest) GetName 
    
    
    func (x *DeleteClipRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteClipRequest) GetRequestId 
    
    
    func (x *DeleteClipRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteClipRequest) ProtoMessage 
    
    
    func (*DeleteClipRequest) ProtoMessage()

### func (*DeleteClipRequest) ProtoReflect 
    
    
    func (x *DeleteClipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteClipRequest) Reset 
    
    
    func (x *DeleteClipRequest) Reset()

### func (*DeleteClipRequest) String 
    
    
    func (x *DeleteClipRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteDvrSessionRequest
    
    
    type DeleteDvrSessionRequest struct {
    
    	// Required. The name of the event resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteDvrSession".

### func (*DeleteDvrSessionRequest) Descriptor 
    
    
    func (*DeleteDvrSessionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteDvrSessionRequest.ProtoReflect.Descriptor instead.

### func (*DeleteDvrSessionRequest) GetName 
    
    
    func (x *DeleteDvrSessionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteDvrSessionRequest) GetRequestId 
    
    
    func (x *DeleteDvrSessionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteDvrSessionRequest) ProtoMessage 
    
    
    func (*DeleteDvrSessionRequest) ProtoMessage()

### func (*DeleteDvrSessionRequest) ProtoReflect 
    
    
    func (x *DeleteDvrSessionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteDvrSessionRequest) Reset 
    
    
    func (x *DeleteDvrSessionRequest) Reset()

### func (*DeleteDvrSessionRequest) String 
    
    
    func (x *DeleteDvrSessionRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteEventRequest
    
    
    type DeleteEventRequest struct {
    
    	// Required. The name of the event resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteEvent".

### func (*DeleteEventRequest) Descriptor 
    
    
    func (*DeleteEventRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteEventRequest.ProtoReflect.Descriptor instead.

### func (*DeleteEventRequest) GetName 
    
    
    func (x *DeleteEventRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteEventRequest) GetRequestId 
    
    
    func (x *DeleteEventRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteEventRequest) ProtoMessage 
    
    
    func (*DeleteEventRequest) ProtoMessage()

### func (*DeleteEventRequest) ProtoReflect 
    
    
    func (x *DeleteEventRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteEventRequest) Reset 
    
    
    func (x *DeleteEventRequest) Reset()

### func (*DeleteEventRequest) String 
    
    
    func (x *DeleteEventRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteInputRequest
    
    
    type DeleteInputRequest struct {
    
    	// Required. The name of the input resource, in the form of:
    	// `projects/{project}/locations/{location}/inputs/{inputId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.DeleteInput".

### func (*DeleteInputRequest) Descriptor 
    
    
    func (*DeleteInputRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteInputRequest.ProtoReflect.Descriptor instead.

### func (*DeleteInputRequest) GetName 
    
    
    func (x *DeleteInputRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteInputRequest) GetRequestId 
    
    
    func (x *DeleteInputRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteInputRequest) ProtoMessage 
    
    
    func (*DeleteInputRequest) ProtoMessage()

### func (*DeleteInputRequest) ProtoReflect 
    
    
    func (x *DeleteInputRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteInputRequest) Reset 
    
    
    func (x *DeleteInputRequest) Reset()

### func (*DeleteInputRequest) String 
    
    
    func (x *DeleteInputRequest) String() [string](https://pkg.go.dev/builtin#string)

## Distribution
    
    
    type Distribution struct {
    
    	// Required. A unique key for this distribution. The key must be 1-63
    	// characters in length. The key must begin and end with a letter (regardless
    	// of case) or a number, but can contain dashes or underscores in between.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
    	// Required. `DistributionStream`
    	// [key][google.cloud.video.livestream.v1.DistributionStream.key]s that should
    	// appear in this distribution output.
    	//
    	// - For SRT protocol, only `ts` distribution streams can be specified.
    	// - For RTMP protocol, only `flv` distribution streams can be specified.
    	DistributionStream [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=distribution_stream,json=distributionStream,proto3" json:"distribution_stream,omitempty"`
    	// Output only. State of the distribution.
    	State Distribution_State `protobuf:"varint,3,opt,name=state,proto3,enum=google.cloud.video.livestream.v1.Distribution_State" json:"state,omitempty"`
    	// Output only. Only present when the `state` is `ERROR`. The reason for the
    	// error state of the distribution.
    	Error *status.Status `protobuf:"bytes,4,opt,name=error,proto3" json:"error,omitempty"`
    	// Configurations for the output endpoint by streaming protocols.
    	//
    	// Types that are valid to be assigned to Endpoint:
    	//
    	//	*Distribution_SrtPush
    	//	*Distribution_RtmpPush
    	Endpoint isDistribution_Endpoint `protobuf_oneof:"endpoint"`
    	// contains filtered or unexported fields
    }

Distribution configuration.

### func (*Distribution) Descriptor 
    
    
    func (*Distribution) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Distribution.ProtoReflect.Descriptor instead.

### func (*Distribution) GetDistributionStream 
    
    
    func (x *Distribution) GetDistributionStream() [string](https://pkg.go.dev/builtin#string)

### func (*Distribution) GetEndpoint 
    
    
    func (x *Distribution) GetEndpoint() isDistribution_Endpoint

### func (*Distribution) GetError 
    
    
    func (x *Distribution) GetError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*Distribution) GetKey 
    
    
    func (x *Distribution) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*Distribution) GetRtmpPush 
    
    
    func (x *Distribution) GetRtmpPush() *RtmpPushOutputEndpoint

### func (*Distribution) GetSrtPush 
    
    
    func (x *Distribution) GetSrtPush() *SrtPushOutputEndpoint

### func (*Distribution) GetState 
    
    
    func (x *Distribution) GetState() Distribution_State

### func (*Distribution) ProtoMessage 
    
    
    func (*Distribution) ProtoMessage()

### func (*Distribution) ProtoReflect 
    
    
    func (x *Distribution) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Distribution) Reset 
    
    
    func (x *Distribution) Reset()

### func (*Distribution) String 
    
    
    func (x *Distribution) String() [string](https://pkg.go.dev/builtin#string)

## DistributionStream
    
    
    type DistributionStream struct {
    
    	// Required. A unique key for this distribution stream. The key must be 1-63
    	// characters in length. The key must begin and end with a letter (regardless
    	// of case) or a number, but can contain dashes or underscores in between.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
    	// Required. The container format.
    	//
    	// Supported container formats:
    	//
    	// - `ts`, must contain exactly one audio stream and up to one video stream.
    	// - `flv`, must contain at most one audio stream and at most one video
    	// stream.
    	Container [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=container,proto3" json:"container,omitempty"`
    	// Required. List of `ElementaryStream`
    	// [key][google.cloud.video.livestream.v1.ElementaryStream.key]s multiplexed
    	// in this stream. Must contain at least one audio stream and up to one video
    	// stream.
    	ElementaryStreams [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=elementary_streams,json=elementaryStreams,proto3" json:"elementary_streams,omitempty"`
    	// contains filtered or unexported fields
    }

Multiplexing settings for output streams used in [Distribution][google.cloud.video.livestream.v1.Distribution].

### func (*DistributionStream) Descriptor 
    
    
    func (*DistributionStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DistributionStream.ProtoReflect.Descriptor instead.

### func (*DistributionStream) GetContainer 
    
    
    func (x *DistributionStream) GetContainer() [string](https://pkg.go.dev/builtin#string)

### func (*DistributionStream) GetElementaryStreams 
    
    
    func (x *DistributionStream) GetElementaryStreams() [][string](https://pkg.go.dev/builtin#string)

### func (*DistributionStream) GetKey 
    
    
    func (x *DistributionStream) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*DistributionStream) ProtoMessage 
    
    
    func (*DistributionStream) ProtoMessage()

### func (*DistributionStream) ProtoReflect 
    
    
    func (x *DistributionStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DistributionStream) Reset 
    
    
    func (x *DistributionStream) Reset()

### func (*DistributionStream) String 
    
    
    func (x *DistributionStream) String() [string](https://pkg.go.dev/builtin#string)

## Distribution_RtmpPush
    
    
    type Distribution_RtmpPush struct {
    	// Output endpoint using RTMP_PUSH.
    	RtmpPush *RtmpPushOutputEndpoint `protobuf:"bytes,6,opt,name=rtmp_push,json=rtmpPush,proto3,oneof"`
    }

## Distribution_SrtPush
    
    
    type Distribution_SrtPush struct {
    	// Output endpoint using SRT_PUSH.
    	SrtPush *SrtPushOutputEndpoint `protobuf:"bytes,5,opt,name=srt_push,json=srtPush,proto3,oneof"`
    }

## Distribution_State
    
    
    type Distribution_State [int32](https://pkg.go.dev/builtin#int32)

State of this distribution.

### Distribution_STATE_UNSPECIFIED, Distribution_ERROR, Distribution_NOT_READY, Distribution_READY, Distribution_AWAITING_INPUT, Distribution_DISTRIBUTING
    
    
    const (
    	// State is not specified.
    	Distribution_STATE_UNSPECIFIED Distribution_State = 0
    	// Distribution has trouble to produce or deliver the output.
    	Distribution_ERROR Distribution_State = 5
    	// Distribution is not ready to be started.
    	Distribution_NOT_READY Distribution_State = 6
    	// Distribution is ready to be started.
    	Distribution_READY Distribution_State = 7
    	// Distribution is already started and is waiting for input.
    	Distribution_AWAITING_INPUT Distribution_State = 8
    	// Distribution is already started and is generating output.
    	Distribution_DISTRIBUTING Distribution_State = 9
    )

### func (Distribution_State) Descriptor 
    
    
    func (Distribution_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Distribution_State) Enum 
    
    
    func (x Distribution_State) Enum() *Distribution_State

### func (Distribution_State) EnumDescriptor 
    
    
    func (Distribution_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Distribution_State.Descriptor instead.

### func (Distribution_State) Number 
    
    
    func (x Distribution_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Distribution_State) String 
    
    
    func (x Distribution_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Distribution_State) Type 
    
    
    func (Distribution_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DvrSession
    
    
    type DvrSession struct {
    
    	// Identifier. The resource name of the DVR session, in the following format:
    	// `projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}`.
    	// `{dvrSessionId}` is a user-specified resource id that conforms to the
    	// following criteria:
    	//
    	// 1. 1 character minimum, 63 characters maximum
    	// 2. Only contains letters, digits, underscores, and hyphens
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Optional. User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Output only. The state of the clip.
    	State DvrSession_State `protobuf:"varint,5,opt,name=state,proto3,enum=google.cloud.video.livestream.v1.DvrSession_State" json:"state,omitempty"`
    	// Output only. An error object that describes the reason for the failure.
    	// This property only presents when `state` is `FAILED`.
    	Error *status.Status `protobuf:"bytes,6,opt,name=error,proto3" json:"error,omitempty"`
    	// Required. A list of DVR manifests. Currently only one DVR manifest is
    	// allowed.
    	DvrManifests []*DvrSession_DvrManifest `protobuf:"bytes,7,rep,name=dvr_manifests,json=dvrManifests,proto3" json:"dvr_manifests,omitempty"`
    	// Required. The specified ranges of segments to generate a DVR recording.
    	DvrWindows []*DvrSession_DvrWindow `protobuf:"bytes,8,rep,name=dvr_windows,json=dvrWindows,proto3" json:"dvr_windows,omitempty"`
    	// contains filtered or unexported fields
    }

DvrSession is a sub-resource under channel. Each DvrSession represents a DVR recording of the live stream for a specific time range.

### func (*DvrSession) Descriptor 
    
    
    func (*DvrSession) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DvrSession.ProtoReflect.Descriptor instead.

### func (*DvrSession) GetCreateTime 
    
    
    func (x *DvrSession) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*DvrSession) GetDvrManifests 
    
    
    func (x *DvrSession) GetDvrManifests() []*DvrSession_DvrManifest

### func (*DvrSession) GetDvrWindows 
    
    
    func (x *DvrSession) GetDvrWindows() []*DvrSession_DvrWindow

### func (*DvrSession) GetError 
    
    
    func (x *DvrSession) GetError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*DvrSession) GetLabels 
    
    
    func (x *DvrSession) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*DvrSession) GetName 
    
    
    func (x *DvrSession) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DvrSession) GetState 
    
    
    func (x *DvrSession) GetState() DvrSession_State

### func (*DvrSession) GetUpdateTime 
    
    
    func (x *DvrSession) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*DvrSession) ProtoMessage 
    
    
    func (*DvrSession) ProtoMessage()

### func (*DvrSession) ProtoReflect 
    
    
    func (x *DvrSession) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DvrSession) Reset 
    
    
    func (x *DvrSession) Reset()

### func (*DvrSession) String 
    
    
    func (x *DvrSession) String() [string](https://pkg.go.dev/builtin#string)

## DvrSession_DvrManifest
    
    
    type DvrSession_DvrManifest struct {
    
    	// Required. A unique key that identifies a manifest config in the parent
    	// channel. This key is the same as `channel.manifests.key` for the selected
    	// manifest.
    	ManifestKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=manifest_key,json=manifestKey,proto3" json:"manifest_key,omitempty"`
    	// Output only. The output URI of the DVR manifest. The DVR output will be
    	// placed in a directory named `dvr/dvrSessionId/` under the parent
    	// channel's output uri. Format:
    	// {channel.output.uri}/dvr/{dvrSessionId}/{channel.manifests.fileName}
    	// Example: gs://my-bucket/outputs/dvr/my-dvr-session/main.m3u8
    	OutputUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=output_uri,json=outputUri,proto3" json:"output_uri,omitempty"`
    	// contains filtered or unexported fields
    }

DvrManifest identifies a source manifest and specifies a file name for the generated DVR manifest.

### func (*DvrSession_DvrManifest) Descriptor 
    
    
    func (*DvrSession_DvrManifest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DvrSession_DvrManifest.ProtoReflect.Descriptor instead.

### func (*DvrSession_DvrManifest) GetManifestKey 
    
    
    func (x *DvrSession_DvrManifest) GetManifestKey() [string](https://pkg.go.dev/builtin#string)

### func (*DvrSession_DvrManifest) GetOutputUri 
    
    
    func (x *DvrSession_DvrManifest) GetOutputUri() [string](https://pkg.go.dev/builtin#string)

### func (*DvrSession_DvrManifest) ProtoMessage 
    
    
    func (*DvrSession_DvrManifest) ProtoMessage()

### func (*DvrSession_DvrManifest) ProtoReflect 
    
    
    func (x *DvrSession_DvrManifest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DvrSession_DvrManifest) Reset 
    
    
    func (x *DvrSession_DvrManifest) Reset()

### func (*DvrSession_DvrManifest) String 
    
    
    func (x *DvrSession_DvrManifest) String() [string](https://pkg.go.dev/builtin#string)

## DvrSession_DvrWindow
    
    
    type DvrSession_DvrWindow struct {
    
    	// The allowlist forms of a DVR window.
    	//
    	// Types that are valid to be assigned to Kind:
    	//
    	//	*DvrSession_DvrWindow_TimeInterval
    	Kind isDvrSession_DvrWindow_Kind `protobuf_oneof:"kind"`
    	// contains filtered or unexported fields
    }

DvrWindow represents a DVR window.

### func (*DvrSession_DvrWindow) Descriptor 
    
    
    func (*DvrSession_DvrWindow) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DvrSession_DvrWindow.ProtoReflect.Descriptor instead.

### func (*DvrSession_DvrWindow) GetKind 
    
    
    func (x *DvrSession_DvrWindow) GetKind() isDvrSession_DvrWindow_Kind

### func (*DvrSession_DvrWindow) GetTimeInterval 
    
    
    func (x *DvrSession_DvrWindow) GetTimeInterval() *TimeInterval

### func (*DvrSession_DvrWindow) ProtoMessage 
    
    
    func (*DvrSession_DvrWindow) ProtoMessage()

### func (*DvrSession_DvrWindow) ProtoReflect 
    
    
    func (x *DvrSession_DvrWindow) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DvrSession_DvrWindow) Reset 
    
    
    func (x *DvrSession_DvrWindow) Reset()

### func (*DvrSession_DvrWindow) String 
    
    
    func (x *DvrSession_DvrWindow) String() [string](https://pkg.go.dev/builtin#string)

## DvrSession_DvrWindow_TimeInterval
    
    
    type DvrSession_DvrWindow_TimeInterval struct {
    	// A time interval in the form of a tuple of Unix epoch time.
    	TimeInterval *TimeInterval `protobuf:"bytes,1,opt,name=time_interval,json=timeInterval,proto3,oneof"`
    }

## DvrSession_State
    
    
    type DvrSession_State [int32](https://pkg.go.dev/builtin#int32)

State of the DVR session.

### DvrSession_STATE_UNSPECIFIED, DvrSession_PENDING, DvrSession_UPDATING, DvrSession_SCHEDULED, DvrSession_LIVE, DvrSession_FINISHED, DvrSession_FAILED, DvrSession_DELETING, DvrSession_POST_PROCESSING, DvrSession_COOLDOWN, DvrSession_STOPPING
    
    
    const (
    	// State is not specified.
    	DvrSession_STATE_UNSPECIFIED DvrSession_State = 0
    	// The operation is pending to be picked up by the server.
    	DvrSession_PENDING DvrSession_State = 1
    	// The session is being updated.
    	DvrSession_UPDATING DvrSession_State = 2
    	// The session is scheduled and waiting for the start time.
    	DvrSession_SCHEDULED DvrSession_State = 3
    	// The session is currently in progress and the outputs are available in the
    	// specified Cloud Storage bucket. For additional information, see the
    	// `dvr_manifests.output_uri` field.
    	DvrSession_LIVE DvrSession_State = 4
    	// Outputs are available in the specified Cloud Storage bucket. For
    	// additional information, see the `dvr_manifests.output_uri` field.
    	DvrSession_FINISHED DvrSession_State = 5
    	// The operation has failed. For additional information, see the `error`
    	// field.
    	DvrSession_FAILED DvrSession_State = 6
    	// The session is being deleted.
    	DvrSession_DELETING DvrSession_State = 7
    	// The session is being post processed.
    	DvrSession_POST_PROCESSING DvrSession_State = 8
    	// The session is in cooldown. The cooldown period lasts for 60 seconds.
    	// When the DVR session is updated by the user to have a new end time that
    	// is likely already in the past, the DVR manifest will end as soon as
    	// possible and the DVR session will move to this state. This is done to
    	// prevent the players to receive a manifest update that removes a segment
    	// that has already been played. After the cooldown period ends, a new
    	// manifest is generated that honors the new end time.
    	DvrSession_COOLDOWN DvrSession_State = 9
    	// The session is being stopped. The session will move to STOPPING state, if
    	// the parent channel is updated.
    	DvrSession_STOPPING DvrSession_State = 10
    )

### func (DvrSession_State) Descriptor 
    
    
    func (DvrSession_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (DvrSession_State) Enum 
    
    
    func (x DvrSession_State) Enum() *DvrSession_State

### func (DvrSession_State) EnumDescriptor 
    
    
    func (DvrSession_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DvrSession_State.Descriptor instead.

### func (DvrSession_State) Number 
    
    
    func (x DvrSession_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (DvrSession_State) String 
    
    
    func (x DvrSession_State) String() [string](https://pkg.go.dev/builtin#string)

### func (DvrSession_State) Type 
    
    
    func (DvrSession_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ElementaryStream
    
    
    type ElementaryStream struct {
    
    	// A unique key for this elementary stream. The key must be 1-63
    	// characters in length. The key must begin and end with a letter (regardless
    	// of case) or a number, but can contain dashes or underscores in between.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=key,proto3" json:"key,omitempty"`
    	// Required. Encoding of an audio, video, or text track.
    	//
    	// Types that are valid to be assigned to ElementaryStream:
    	//
    	//	*ElementaryStream_VideoStream
    	//	*ElementaryStream_AudioStream
    	//	*ElementaryStream_TextStream
    	ElementaryStream isElementaryStream_ElementaryStream `protobuf_oneof:"elementary_stream"`
    	// contains filtered or unexported fields
    }

Encoding of an input element such as an audio, video, or text track. Elementary streams must be packaged before mapping and sharing between different output formats.

### func (*ElementaryStream) Descriptor 
    
    
    func (*ElementaryStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ElementaryStream.ProtoReflect.Descriptor instead.

### func (*ElementaryStream) GetAudioStream 
    
    
    func (x *ElementaryStream) GetAudioStream() *AudioStream

### func (*ElementaryStream) GetElementaryStream 
    
    
    func (x *ElementaryStream) GetElementaryStream() isElementaryStream_ElementaryStream

### func (*ElementaryStream) GetKey 
    
    
    func (x *ElementaryStream) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*ElementaryStream) GetTextStream 
    
    
    func (x *ElementaryStream) GetTextStream() *TextStream

### func (*ElementaryStream) GetVideoStream 
    
    
    func (x *ElementaryStream) GetVideoStream() *VideoStream

### func (*ElementaryStream) ProtoMessage 
    
    
    func (*ElementaryStream) ProtoMessage()

### func (*ElementaryStream) ProtoReflect 
    
    
    func (x *ElementaryStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ElementaryStream) Reset 
    
    
    func (x *ElementaryStream) Reset()

### func (*ElementaryStream) String 
    
    
    func (x *ElementaryStream) String() [string](https://pkg.go.dev/builtin#string)

## ElementaryStream_AudioStream
    
    
    type ElementaryStream_AudioStream struct {
    	// Encoding of an audio stream.
    	AudioStream *AudioStream `protobuf:"bytes,2,opt,name=audio_stream,json=audioStream,proto3,oneof"`
    }

## ElementaryStream_TextStream
    
    
    type ElementaryStream_TextStream struct {
    	// Encoding of a text stream. For example, closed captions or subtitles.
    	TextStream *TextStream `protobuf:"bytes,3,opt,name=text_stream,json=textStream,proto3,oneof"`
    }

## ElementaryStream_VideoStream
    
    
    type ElementaryStream_VideoStream struct {
    	// Encoding of a video stream.
    	VideoStream *VideoStream `protobuf:"bytes,1,opt,name=video_stream,json=videoStream,proto3,oneof"`
    }

## Encryption
    
    
    type Encryption struct {
    
    	// Required. Identifier for this set of encryption options. The ID must be
    	// 1-63 characters in length. The ID must begin and end with a letter
    	// (regardless of case) or a number, but can contain dashes or underscores in
    	// between.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// Defines where content keys are stored.
    	//
    	// Types that are valid to be assigned to SecretSource:
    	//
    	//	*Encryption_SecretManagerKeySource
    	SecretSource isEncryption_SecretSource `protobuf_oneof:"secret_source"`
    	// Required. Configuration for DRM systems.
    	DrmSystems *Encryption_DrmSystems `protobuf:"bytes,3,opt,name=drm_systems,json=drmSystems,proto3" json:"drm_systems,omitempty"`
    	// Encryption modes for HLS and MPEG-Dash.
    	//
    	// Types that are valid to be assigned to EncryptionMode:
    	//
    	//	*Encryption_Aes128
    	//	*Encryption_SampleAes
    	//	*Encryption_MpegCenc
    	EncryptionMode isEncryption_EncryptionMode `protobuf_oneof:"encryption_mode"`
    	// contains filtered or unexported fields
    }

Encryption settings.

### func (*Encryption) Descriptor 
    
    
    func (*Encryption) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption.ProtoReflect.Descriptor instead.

### func (*Encryption) GetAes128 
    
    
    func (x *Encryption) GetAes128() *Encryption_Aes128Encryption

### func (*Encryption) GetDrmSystems 
    
    
    func (x *Encryption) GetDrmSystems() *Encryption_DrmSystems

### func (*Encryption) GetEncryptionMode 
    
    
    func (x *Encryption) GetEncryptionMode() isEncryption_EncryptionMode

### func (*Encryption) GetId 
    
    
    func (x *Encryption) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*Encryption) GetMpegCenc 
    
    
    func (x *Encryption) GetMpegCenc() *Encryption_MpegCommonEncryption

### func (*Encryption) GetSampleAes 
    
    
    func (x *Encryption) GetSampleAes() *Encryption_SampleAesEncryption

### func (*Encryption) GetSecretManagerKeySource 
    
    
    func (x *Encryption) GetSecretManagerKeySource() *Encryption_SecretManagerSource

### func (*Encryption) GetSecretSource 
    
    
    func (x *Encryption) GetSecretSource() isEncryption_SecretSource

### func (*Encryption) ProtoMessage 
    
    
    func (*Encryption) ProtoMessage()

### func (*Encryption) ProtoReflect 
    
    
    func (x *Encryption) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption) Reset 
    
    
    func (x *Encryption) Reset()

### func (*Encryption) String 
    
    
    func (x *Encryption) String() [string](https://pkg.go.dev/builtin#string)

## EncryptionUpdate
    
    
    type EncryptionUpdate struct {
    
    	// Required. Identifier for the encryption option to be updated.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
    	// Defines where new content keys are stored.
    	//
    	// Types that are valid to be assigned to SecretSource:
    	//
    	//	*EncryptionUpdate_SecretManagerKeySource
    	SecretSource isEncryptionUpdate_SecretSource `protobuf_oneof:"secret_source"`
    	// contains filtered or unexported fields
    }

Encryption setting when updating encryption.

### func (*EncryptionUpdate) Descriptor 
    
    
    func (*EncryptionUpdate) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use EncryptionUpdate.ProtoReflect.Descriptor instead.

### func (*EncryptionUpdate) GetId 
    
    
    func (x *EncryptionUpdate) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*EncryptionUpdate) GetSecretManagerKeySource 
    
    
    func (x *EncryptionUpdate) GetSecretManagerKeySource() *Encryption_SecretManagerSource

### func (*EncryptionUpdate) GetSecretSource 
    
    
    func (x *EncryptionUpdate) GetSecretSource() isEncryptionUpdate_SecretSource

### func (*EncryptionUpdate) ProtoMessage 
    
    
    func (*EncryptionUpdate) ProtoMessage()

### func (*EncryptionUpdate) ProtoReflect 
    
    
    func (x *EncryptionUpdate) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*EncryptionUpdate) Reset 
    
    
    func (x *EncryptionUpdate) Reset()

### func (*EncryptionUpdate) String 
    
    
    func (x *EncryptionUpdate) String() [string](https://pkg.go.dev/builtin#string)

## EncryptionUpdate_SecretManagerKeySource
    
    
    type EncryptionUpdate_SecretManagerKeySource struct {
    	// For keys stored in Google Secret Manager.
    	SecretManagerKeySource *Encryption_SecretManagerSource `protobuf:"bytes,2,opt,name=secret_manager_key_source,json=secretManagerKeySource,proto3,oneof"`
    }

## Encryption_Aes128
    
    
    type Encryption_Aes128 struct {
    	// Configuration for HLS AES-128 encryption.
    	Aes128 *Encryption_Aes128Encryption `protobuf:"bytes,4,opt,name=aes128,proto3,oneof"`
    }

## Encryption_Aes128Encryption
    
    
    type Encryption_Aes128Encryption struct {
    	// contains filtered or unexported fields
    }

Configuration for HLS AES-128 encryption.

### func (*Encryption_Aes128Encryption) Descriptor 
    
    
    func (*Encryption_Aes128Encryption) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_Aes128Encryption.ProtoReflect.Descriptor instead.

### func (*Encryption_Aes128Encryption) ProtoMessage 
    
    
    func (*Encryption_Aes128Encryption) ProtoMessage()

### func (*Encryption_Aes128Encryption) ProtoReflect 
    
    
    func (x *Encryption_Aes128Encryption) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_Aes128Encryption) Reset 
    
    
    func (x *Encryption_Aes128Encryption) Reset()

### func (*Encryption_Aes128Encryption) String 
    
    
    func (x *Encryption_Aes128Encryption) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_Clearkey
    
    
    type Encryption_Clearkey struct {
    	// contains filtered or unexported fields
    }

Clearkey configuration.

### func (*Encryption_Clearkey) Descriptor 
    
    
    func (*Encryption_Clearkey) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_Clearkey.ProtoReflect.Descriptor instead.

### func (*Encryption_Clearkey) ProtoMessage 
    
    
    func (*Encryption_Clearkey) ProtoMessage()

### func (*Encryption_Clearkey) ProtoReflect 
    
    
    func (x *Encryption_Clearkey) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_Clearkey) Reset 
    
    
    func (x *Encryption_Clearkey) Reset()

### func (*Encryption_Clearkey) String 
    
    
    func (x *Encryption_Clearkey) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_DrmSystems
    
    
    type Encryption_DrmSystems struct {
    
    	// Optional. Widevine configuration.
    	Widevine *Encryption_Widevine `protobuf:"bytes,1,opt,name=widevine,proto3" json:"widevine,omitempty"`
    	// Optional. Fairplay configuration.
    	Fairplay *Encryption_Fairplay `protobuf:"bytes,2,opt,name=fairplay,proto3" json:"fairplay,omitempty"`
    	// Optional. Playready configuration.
    	Playready *Encryption_Playready `protobuf:"bytes,3,opt,name=playready,proto3" json:"playready,omitempty"`
    	// Optional. Clearkey configuration.
    	Clearkey *Encryption_Clearkey `protobuf:"bytes,4,opt,name=clearkey,proto3" json:"clearkey,omitempty"`
    	// contains filtered or unexported fields
    }

Defines configuration for DRM systems in use. If a field is omitted, that DRM system will be considered to be disabled.

### func (*Encryption_DrmSystems) Descriptor 
    
    
    func (*Encryption_DrmSystems) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_DrmSystems.ProtoReflect.Descriptor instead.

### func (*Encryption_DrmSystems) GetClearkey 
    
    
    func (x *Encryption_DrmSystems) GetClearkey() *Encryption_Clearkey

### func (*Encryption_DrmSystems) GetFairplay 
    
    
    func (x *Encryption_DrmSystems) GetFairplay() *Encryption_Fairplay

### func (*Encryption_DrmSystems) GetPlayready 
    
    
    func (x *Encryption_DrmSystems) GetPlayready() *Encryption_Playready

### func (*Encryption_DrmSystems) GetWidevine 
    
    
    func (x *Encryption_DrmSystems) GetWidevine() *Encryption_Widevine

### func (*Encryption_DrmSystems) ProtoMessage 
    
    
    func (*Encryption_DrmSystems) ProtoMessage()

### func (*Encryption_DrmSystems) ProtoReflect 
    
    
    func (x *Encryption_DrmSystems) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_DrmSystems) Reset 
    
    
    func (x *Encryption_DrmSystems) Reset()

### func (*Encryption_DrmSystems) String 
    
    
    func (x *Encryption_DrmSystems) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_Fairplay
    
    
    type Encryption_Fairplay struct {
    	// contains filtered or unexported fields
    }

Fairplay configuration.

### func (*Encryption_Fairplay) Descriptor 
    
    
    func (*Encryption_Fairplay) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_Fairplay.ProtoReflect.Descriptor instead.

### func (*Encryption_Fairplay) ProtoMessage 
    
    
    func (*Encryption_Fairplay) ProtoMessage()

### func (*Encryption_Fairplay) ProtoReflect 
    
    
    func (x *Encryption_Fairplay) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_Fairplay) Reset 
    
    
    func (x *Encryption_Fairplay) Reset()

### func (*Encryption_Fairplay) String 
    
    
    func (x *Encryption_Fairplay) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_MpegCenc
    
    
    type Encryption_MpegCenc struct {
    	// Configuration for MPEG-Dash Common Encryption (MPEG-CENC).
    	MpegCenc *Encryption_MpegCommonEncryption `protobuf:"bytes,6,opt,name=mpeg_cenc,json=mpegCenc,proto3,oneof"`
    }

## Encryption_MpegCommonEncryption
    
    
    type Encryption_MpegCommonEncryption struct {
    
    	// Required. Specify the encryption scheme, supported schemes:
    	// - `cenc` - AES-CTR subsample
    	// - `cbcs`- AES-CBC subsample pattern
    	Scheme [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=scheme,proto3" json:"scheme,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for MPEG-Dash Common Encryption (MPEG-CENC).

### func (*Encryption_MpegCommonEncryption) Descriptor 
    
    
    func (*Encryption_MpegCommonEncryption) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_MpegCommonEncryption.ProtoReflect.Descriptor instead.

### func (*Encryption_MpegCommonEncryption) GetScheme 
    
    
    func (x *Encryption_MpegCommonEncryption) GetScheme() [string](https://pkg.go.dev/builtin#string)

### func (*Encryption_MpegCommonEncryption) ProtoMessage 
    
    
    func (*Encryption_MpegCommonEncryption) ProtoMessage()

### func (*Encryption_MpegCommonEncryption) ProtoReflect 
    
    
    func (x *Encryption_MpegCommonEncryption) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_MpegCommonEncryption) Reset 
    
    
    func (x *Encryption_MpegCommonEncryption) Reset()

### func (*Encryption_MpegCommonEncryption) String 
    
    
    func (x *Encryption_MpegCommonEncryption) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_Playready
    
    
    type Encryption_Playready struct {
    	// contains filtered or unexported fields
    }

Playready configuration.

### func (*Encryption_Playready) Descriptor 
    
    
    func (*Encryption_Playready) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_Playready.ProtoReflect.Descriptor instead.

### func (*Encryption_Playready) ProtoMessage 
    
    
    func (*Encryption_Playready) ProtoMessage()

### func (*Encryption_Playready) ProtoReflect 
    
    
    func (x *Encryption_Playready) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_Playready) Reset 
    
    
    func (x *Encryption_Playready) Reset()

### func (*Encryption_Playready) String 
    
    
    func (x *Encryption_Playready) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_SampleAes
    
    
    type Encryption_SampleAes struct {
    	// Configuration for HLS SAMPLE-AES encryption.
    	SampleAes *Encryption_SampleAesEncryption `protobuf:"bytes,5,opt,name=sample_aes,json=sampleAes,proto3,oneof"`
    }

## Encryption_SampleAesEncryption
    
    
    type Encryption_SampleAesEncryption struct {
    	// contains filtered or unexported fields
    }

Configuration for HLS SAMPLE-AES encryption.

### func (*Encryption_SampleAesEncryption) Descriptor 
    
    
    func (*Encryption_SampleAesEncryption) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_SampleAesEncryption.ProtoReflect.Descriptor instead.

### func (*Encryption_SampleAesEncryption) ProtoMessage 
    
    
    func (*Encryption_SampleAesEncryption) ProtoMessage()

### func (*Encryption_SampleAesEncryption) ProtoReflect 
    
    
    func (x *Encryption_SampleAesEncryption) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_SampleAesEncryption) Reset 
    
    
    func (x *Encryption_SampleAesEncryption) Reset()

### func (*Encryption_SampleAesEncryption) String 
    
    
    func (x *Encryption_SampleAesEncryption) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_SecretManagerKeySource
    
    
    type Encryption_SecretManagerKeySource struct {
    	// For keys stored in Google Secret Manager.
    	SecretManagerKeySource *Encryption_SecretManagerSource `protobuf:"bytes,7,opt,name=secret_manager_key_source,json=secretManagerKeySource,proto3,oneof"`
    }

## Encryption_SecretManagerSource
    
    
    type Encryption_SecretManagerSource struct {
    
    	// Required. The name of the Secret Version containing the encryption key.
    	// `projects/{project}/secrets/{secret_id}/versions/{version_number}`
    	SecretVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=secret_version,json=secretVersion,proto3" json:"secret_version,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for secrets stored in Google Secret Manager.

### func (*Encryption_SecretManagerSource) Descriptor 
    
    
    func (*Encryption_SecretManagerSource) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_SecretManagerSource.ProtoReflect.Descriptor instead.

### func (*Encryption_SecretManagerSource) GetSecretVersion 
    
    
    func (x *Encryption_SecretManagerSource) GetSecretVersion() [string](https://pkg.go.dev/builtin#string)

### func (*Encryption_SecretManagerSource) ProtoMessage 
    
    
    func (*Encryption_SecretManagerSource) ProtoMessage()

### func (*Encryption_SecretManagerSource) ProtoReflect 
    
    
    func (x *Encryption_SecretManagerSource) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_SecretManagerSource) Reset 
    
    
    func (x *Encryption_SecretManagerSource) Reset()

### func (*Encryption_SecretManagerSource) String 
    
    
    func (x *Encryption_SecretManagerSource) String() [string](https://pkg.go.dev/builtin#string)

## Encryption_Widevine
    
    
    type Encryption_Widevine struct {
    	// contains filtered or unexported fields
    }

Widevine configuration.

### func (*Encryption_Widevine) Descriptor 
    
    
    func (*Encryption_Widevine) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Encryption_Widevine.ProtoReflect.Descriptor instead.

### func (*Encryption_Widevine) ProtoMessage 
    
    
    func (*Encryption_Widevine) ProtoMessage()

### func (*Encryption_Widevine) ProtoReflect 
    
    
    func (x *Encryption_Widevine) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Encryption_Widevine) Reset 
    
    
    func (x *Encryption_Widevine) Reset()

### func (*Encryption_Widevine) String 
    
    
    func (x *Encryption_Widevine) String() [string](https://pkg.go.dev/builtin#string)

## Event
    
    
    type Event struct {
    
    	// The resource name of the event, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Operation to be executed by this event.
    	//
    	// Types that are valid to be assigned to Task:
    	//
    	//	*Event_InputSwitch
    	//	*Event_AdBreak
    	//	*Event_ReturnToProgram
    	//	*Event_Slate
    	//	*Event_Mute
    	//	*Event_Unmute
    	//	*Event_UpdateEncryptions
    	Task isEvent_Task `protobuf_oneof:"task"`
    	// When this field is set to true, the event will be executed at the earliest
    	// time that the server can schedule the event and
    	// [execution_time][google.cloud.video.livestream.v1.Event.execution_time]
    	// will be populated with the time that the server actually schedules the
    	// event.
    	ExecuteNow [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,9,opt,name=execute_now,json=executeNow,proto3" json:"execute_now,omitempty"`
    	// The time to execute the event. If you set
    	// [execute_now][google.cloud.video.livestream.v1.Event.execute_now] to
    	// `true`, then do not set this field in the `CreateEvent` request. In
    	// this case, the server schedules the event and populates this field. If you
    	// set [execute_now][google.cloud.video.livestream.v1.Event.execute_now] to
    	// `false`, then you must set this field to at least 10 seconds in the future
    	// or else the event can't be created.
    	ExecutionTime *timestamppb.Timestamp `protobuf:"bytes,10,opt,name=execution_time,json=executionTime,proto3" json:"execution_time,omitempty"`
    	// Output only. The state of the event.
    	State Event_State `protobuf:"varint,11,opt,name=state,proto3,enum=google.cloud.video.livestream.v1.Event_State" json:"state,omitempty"`
    	// Output only. An error object that describes the reason for the failure.
    	// This property is always present when `state` is `FAILED`.
    	Error *status.Status `protobuf:"bytes,12,opt,name=error,proto3" json:"error,omitempty"`
    	// contains filtered or unexported fields
    }

Event is a sub-resource of a channel, which can be scheduled by the user to execute operations on a channel resource without having to stop the channel.

### func (*Event) Descriptor 
    
    
    func (*Event) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event.ProtoReflect.Descriptor instead.

### func (*Event) GetAdBreak 
    
    
    func (x *Event) GetAdBreak() *Event_AdBreakTask

### func (*Event) GetCreateTime 
    
    
    func (x *Event) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Event) GetError 
    
    
    func (x *Event) GetError() *[status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status).[Status](https://pkg.go.dev/google.golang.org/genproto/googleapis/rpc/status#Status)

### func (*Event) GetExecuteNow 
    
    
    func (x *Event) GetExecuteNow() [bool](https://pkg.go.dev/builtin#bool)

### func (*Event) GetExecutionTime 
    
    
    func (x *Event) GetExecutionTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Event) GetInputSwitch 
    
    
    func (x *Event) GetInputSwitch() *Event_InputSwitchTask

### func (*Event) GetLabels 
    
    
    func (x *Event) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Event) GetMute 
    
    
    func (x *Event) GetMute() *Event_MuteTask

### func (*Event) GetName 
    
    
    func (x *Event) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Event) GetReturnToProgram 
    
    
    func (x *Event) GetReturnToProgram() *Event_ReturnToProgramTask

### func (*Event) GetSlate 
    
    
    func (x *Event) GetSlate() *Event_SlateTask

### func (*Event) GetState 
    
    
    func (x *Event) GetState() Event_State

### func (*Event) GetTask 
    
    
    func (x *Event) GetTask() isEvent_Task

### func (*Event) GetUnmute 
    
    
    func (x *Event) GetUnmute() *Event_UnmuteTask

### func (*Event) GetUpdateEncryptions 
    
    
    func (x *Event) GetUpdateEncryptions() *Event_UpdateEncryptionsTask

### func (*Event) GetUpdateTime 
    
    
    func (x *Event) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Event) ProtoMessage 
    
    
    func (*Event) ProtoMessage()

### func (*Event) ProtoReflect 
    
    
    func (x *Event) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event) Reset 
    
    
    func (x *Event) Reset()

### func (*Event) String 
    
    
    func (x *Event) String() [string](https://pkg.go.dev/builtin#string)

## Event_AdBreak
    
    
    type Event_AdBreak struct {
    	// Inserts a new ad opportunity.
    	AdBreak *Event_AdBreakTask `protobuf:"bytes,6,opt,name=ad_break,json=adBreak,proto3,oneof"`
    }

## Event_AdBreakTask
    
    
    type Event_AdBreakTask struct {
    
    	// Duration of an ad opportunity. Must be greater than 0.
    	Duration *durationpb.Duration `protobuf:"bytes,1,opt,name=duration,proto3" json:"duration,omitempty"`
    	// contains filtered or unexported fields
    }

Inserts a new ad opportunity.

### func (*Event_AdBreakTask) Descriptor 
    
    
    func (*Event_AdBreakTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_AdBreakTask.ProtoReflect.Descriptor instead.

### func (*Event_AdBreakTask) GetDuration 
    
    
    func (x *Event_AdBreakTask) GetDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Event_AdBreakTask) ProtoMessage 
    
    
    func (*Event_AdBreakTask) ProtoMessage()

### func (*Event_AdBreakTask) ProtoReflect 
    
    
    func (x *Event_AdBreakTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_AdBreakTask) Reset 
    
    
    func (x *Event_AdBreakTask) Reset()

### func (*Event_AdBreakTask) String 
    
    
    func (x *Event_AdBreakTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_InputSwitch
    
    
    type Event_InputSwitch struct {
    	// Switches to another input stream.
    	InputSwitch *Event_InputSwitchTask `protobuf:"bytes,5,opt,name=input_switch,json=inputSwitch,proto3,oneof"`
    }

## Event_InputSwitchTask
    
    
    type Event_InputSwitchTask struct {
    
    	// The
    	// [InputAttachment.key][google.cloud.video.livestream.v1.InputAttachment.key]
    	// of the input to switch to.
    	InputKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=input_key,json=inputKey,proto3" json:"input_key,omitempty"`
    	// contains filtered or unexported fields
    }

Switches to another input stream. Automatic failover is then disabled.

### func (*Event_InputSwitchTask) Descriptor 
    
    
    func (*Event_InputSwitchTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_InputSwitchTask.ProtoReflect.Descriptor instead.

### func (*Event_InputSwitchTask) GetInputKey 
    
    
    func (x *Event_InputSwitchTask) GetInputKey() [string](https://pkg.go.dev/builtin#string)

### func (*Event_InputSwitchTask) ProtoMessage 
    
    
    func (*Event_InputSwitchTask) ProtoMessage()

### func (*Event_InputSwitchTask) ProtoReflect 
    
    
    func (x *Event_InputSwitchTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_InputSwitchTask) Reset 
    
    
    func (x *Event_InputSwitchTask) Reset()

### func (*Event_InputSwitchTask) String 
    
    
    func (x *Event_InputSwitchTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_Mute
    
    
    type Event_Mute struct {
    	// Mutes the stream.
    	Mute *Event_MuteTask `protobuf:"bytes,15,opt,name=mute,proto3,oneof"`
    }

## Event_MuteTask
    
    
    type Event_MuteTask struct {
    
    	// Duration for which the stream should be muted. If omitted, the stream
    	// will be muted until an UnmuteTask event is sent.
    	Duration *durationpb.Duration `protobuf:"bytes,1,opt,name=duration,proto3" json:"duration,omitempty"`
    	// contains filtered or unexported fields
    }

Mutes the stream.

### func (*Event_MuteTask) Descriptor 
    
    
    func (*Event_MuteTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_MuteTask.ProtoReflect.Descriptor instead.

### func (*Event_MuteTask) GetDuration 
    
    
    func (x *Event_MuteTask) GetDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Event_MuteTask) ProtoMessage 
    
    
    func (*Event_MuteTask) ProtoMessage()

### func (*Event_MuteTask) ProtoReflect 
    
    
    func (x *Event_MuteTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_MuteTask) Reset 
    
    
    func (x *Event_MuteTask) Reset()

### func (*Event_MuteTask) String 
    
    
    func (x *Event_MuteTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_ReturnToProgram
    
    
    type Event_ReturnToProgram struct {
    	// Stops any running ad break.
    	ReturnToProgram *Event_ReturnToProgramTask `protobuf:"bytes,13,opt,name=return_to_program,json=returnToProgram,proto3,oneof"`
    }

## Event_ReturnToProgramTask
    
    
    type Event_ReturnToProgramTask struct {
    	// contains filtered or unexported fields
    }

Stops any events which are currently running. This only applies to events with a duration.

### func (*Event_ReturnToProgramTask) Descriptor 
    
    
    func (*Event_ReturnToProgramTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_ReturnToProgramTask.ProtoReflect.Descriptor instead.

### func (*Event_ReturnToProgramTask) ProtoMessage 
    
    
    func (*Event_ReturnToProgramTask) ProtoMessage()

### func (*Event_ReturnToProgramTask) ProtoReflect 
    
    
    func (x *Event_ReturnToProgramTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_ReturnToProgramTask) Reset 
    
    
    func (x *Event_ReturnToProgramTask) Reset()

### func (*Event_ReturnToProgramTask) String 
    
    
    func (x *Event_ReturnToProgramTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_Slate
    
    
    type Event_Slate struct {
    	// Inserts a slate.
    	Slate *Event_SlateTask `protobuf:"bytes,14,opt,name=slate,proto3,oneof"`
    }

## Event_SlateTask
    
    
    type Event_SlateTask struct {
    
    	// Optional. Duration of the slate. Must be greater than 0 if specified.
    	// Omit this field for a long running slate.
    	Duration *durationpb.Duration `protobuf:"bytes,1,opt,name=duration,proto3" json:"duration,omitempty"`
    	// Slate asset to use for the duration. If its duration is less than the
    	// duration of the SlateTask, then the slate loops. The slate must be
    	// represented in the form of:
    	// `projects/{project}/locations/{location}/assets/{assetId}`.
    	Asset [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=asset,proto3" json:"asset,omitempty"`
    	// contains filtered or unexported fields
    }

Inserts a slate.

### func (*Event_SlateTask) Descriptor 
    
    
    func (*Event_SlateTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_SlateTask.ProtoReflect.Descriptor instead.

### func (*Event_SlateTask) GetAsset 
    
    
    func (x *Event_SlateTask) GetAsset() [string](https://pkg.go.dev/builtin#string)

### func (*Event_SlateTask) GetDuration 
    
    
    func (x *Event_SlateTask) GetDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Event_SlateTask) ProtoMessage 
    
    
    func (*Event_SlateTask) ProtoMessage()

### func (*Event_SlateTask) ProtoReflect 
    
    
    func (x *Event_SlateTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_SlateTask) Reset 
    
    
    func (x *Event_SlateTask) Reset()

### func (*Event_SlateTask) String 
    
    
    func (x *Event_SlateTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_State
    
    
    type Event_State [int32](https://pkg.go.dev/builtin#int32)

State of the event

### Event_STATE_UNSPECIFIED, Event_SCHEDULED, Event_RUNNING, Event_SUCCEEDED, Event_FAILED, Event_PENDING, Event_STOPPED
    
    
    const (
    	// Event state is not specified.
    	Event_STATE_UNSPECIFIED Event_State = 0
    	// Event is scheduled but not executed yet.
    	Event_SCHEDULED Event_State = 1
    	// Event is being executed.
    	Event_RUNNING Event_State = 2
    	// Event has been successfully executed.
    	Event_SUCCEEDED Event_State = 3
    	// Event fails to be executed.
    	Event_FAILED Event_State = 4
    	// Event has been created but not scheduled yet.
    	Event_PENDING Event_State = 5
    	// Event was stopped before running for its full duration.
    	Event_STOPPED Event_State = 6
    )

### func (Event_State) Descriptor 
    
    
    func (Event_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Event_State) Enum 
    
    
    func (x Event_State) Enum() *Event_State

### func (Event_State) EnumDescriptor 
    
    
    func (Event_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_State.Descriptor instead.

### func (Event_State) Number 
    
    
    func (x Event_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Event_State) String 
    
    
    func (x Event_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Event_State) Type 
    
    
    func (Event_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Event_Unmute
    
    
    type Event_Unmute struct {
    	// Unmutes the stream.
    	Unmute *Event_UnmuteTask `protobuf:"bytes,16,opt,name=unmute,proto3,oneof"`
    }

## Event_UnmuteTask
    
    
    type Event_UnmuteTask struct {
    	// contains filtered or unexported fields
    }

Unmutes the stream. The task fails if the stream is not currently muted.

### func (*Event_UnmuteTask) Descriptor 
    
    
    func (*Event_UnmuteTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_UnmuteTask.ProtoReflect.Descriptor instead.

### func (*Event_UnmuteTask) ProtoMessage 
    
    
    func (*Event_UnmuteTask) ProtoMessage()

### func (*Event_UnmuteTask) ProtoReflect 
    
    
    func (x *Event_UnmuteTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_UnmuteTask) Reset 
    
    
    func (x *Event_UnmuteTask) Reset()

### func (*Event_UnmuteTask) String 
    
    
    func (x *Event_UnmuteTask) String() [string](https://pkg.go.dev/builtin#string)

## Event_UpdateEncryptions
    
    
    type Event_UpdateEncryptions struct {
    	// Updates encryption settings.
    	UpdateEncryptions *Event_UpdateEncryptionsTask `protobuf:"bytes,17,opt,name=update_encryptions,json=updateEncryptions,proto3,oneof"`
    }

## Event_UpdateEncryptionsTask
    
    
    type Event_UpdateEncryptionsTask struct {
    
    	// Required. A list of
    	// [EncryptionUpdate][google.cloud.video.livestream.v1.EncryptionUpdate]s
    	// that updates the existing encryption settings.
    	Encryptions []*EncryptionUpdate `protobuf:"bytes,1,rep,name=encryptions,proto3" json:"encryptions,omitempty"`
    	// contains filtered or unexported fields
    }

Update encryption settings.

### func (*Event_UpdateEncryptionsTask) Descriptor 
    
    
    func (*Event_UpdateEncryptionsTask) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Event_UpdateEncryptionsTask.ProtoReflect.Descriptor instead.

### func (*Event_UpdateEncryptionsTask) GetEncryptions 
    
    
    func (x *Event_UpdateEncryptionsTask) GetEncryptions() []*EncryptionUpdate

### func (*Event_UpdateEncryptionsTask) ProtoMessage 
    
    
    func (*Event_UpdateEncryptionsTask) ProtoMessage()

### func (*Event_UpdateEncryptionsTask) ProtoReflect 
    
    
    func (x *Event_UpdateEncryptionsTask) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Event_UpdateEncryptionsTask) Reset 
    
    
    func (x *Event_UpdateEncryptionsTask) Reset()

### func (*Event_UpdateEncryptionsTask) String 
    
    
    func (x *Event_UpdateEncryptionsTask) String() [string](https://pkg.go.dev/builtin#string)

## GetAssetRequest
    
    
    type GetAssetRequest struct {
    
    	// Required. Name of the resource, in the following form:
    	// `projects/{project}/locations/{location}/assets/{asset}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetAsset".

### func (*GetAssetRequest) Descriptor 
    
    
    func (*GetAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAssetRequest.ProtoReflect.Descriptor instead.

### func (*GetAssetRequest) GetName 
    
    
    func (x *GetAssetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAssetRequest) ProtoMessage 
    
    
    func (*GetAssetRequest) ProtoMessage()

### func (*GetAssetRequest) ProtoReflect 
    
    
    func (x *GetAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAssetRequest) Reset 
    
    
    func (x *GetAssetRequest) Reset()

### func (*GetAssetRequest) String 
    
    
    func (x *GetAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetChannelRequest
    
    
    type GetChannelRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetChannel".

### func (*GetChannelRequest) Descriptor 
    
    
    func (*GetChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetChannelRequest.ProtoReflect.Descriptor instead.

### func (*GetChannelRequest) GetName 
    
    
    func (x *GetChannelRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetChannelRequest) ProtoMessage 
    
    
    func (*GetChannelRequest) ProtoMessage()

### func (*GetChannelRequest) ProtoReflect 
    
    
    func (x *GetChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetChannelRequest) Reset 
    
    
    func (x *GetChannelRequest) Reset()

### func (*GetChannelRequest) String 
    
    
    func (x *GetChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetClipRequest
    
    
    type GetClipRequest struct {
    
    	// Required. Name of the resource, in the following form:
    	// `projects/{project}/locations/{location}/channels/{channel}/clips/{clip}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetClip".

### func (*GetClipRequest) Descriptor 
    
    
    func (*GetClipRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetClipRequest.ProtoReflect.Descriptor instead.

### func (*GetClipRequest) GetName 
    
    
    func (x *GetClipRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetClipRequest) ProtoMessage 
    
    
    func (*GetClipRequest) ProtoMessage()

### func (*GetClipRequest) ProtoReflect 
    
    
    func (x *GetClipRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetClipRequest) Reset 
    
    
    func (x *GetClipRequest) Reset()

### func (*GetClipRequest) String 
    
    
    func (x *GetClipRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetDvrSessionRequest
    
    
    type GetDvrSessionRequest struct {
    
    	// Required. Name of the resource, in the following form:
    	// `projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetDvrSession".

### func (*GetDvrSessionRequest) Descriptor 
    
    
    func (*GetDvrSessionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetDvrSessionRequest.ProtoReflect.Descriptor instead.

### func (*GetDvrSessionRequest) GetName 
    
    
    func (x *GetDvrSessionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetDvrSessionRequest) ProtoMessage 
    
    
    func (*GetDvrSessionRequest) ProtoMessage()

### func (*GetDvrSessionRequest) ProtoReflect 
    
    
    func (x *GetDvrSessionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetDvrSessionRequest) Reset 
    
    
    func (x *GetDvrSessionRequest) Reset()

### func (*GetDvrSessionRequest) String 
    
    
    func (x *GetDvrSessionRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetEventRequest
    
    
    type GetEventRequest struct {
    
    	// Required. The name of the event resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetEvent".

### func (*GetEventRequest) Descriptor 
    
    
    func (*GetEventRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetEventRequest.ProtoReflect.Descriptor instead.

### func (*GetEventRequest) GetName 
    
    
    func (x *GetEventRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetEventRequest) ProtoMessage 
    
    
    func (*GetEventRequest) ProtoMessage()

### func (*GetEventRequest) ProtoReflect 
    
    
    func (x *GetEventRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetEventRequest) Reset 
    
    
    func (x *GetEventRequest) Reset()

### func (*GetEventRequest) String 
    
    
    func (x *GetEventRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetInputRequest
    
    
    type GetInputRequest struct {
    
    	// Required. The name of the input resource, in the form of:
    	// `projects/{project}/locations/{location}/inputs/{inputId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetInput".

### func (*GetInputRequest) Descriptor 
    
    
    func (*GetInputRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetInputRequest.ProtoReflect.Descriptor instead.

### func (*GetInputRequest) GetName 
    
    
    func (x *GetInputRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetInputRequest) ProtoMessage 
    
    
    func (*GetInputRequest) ProtoMessage()

### func (*GetInputRequest) ProtoReflect 
    
    
    func (x *GetInputRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetInputRequest) Reset 
    
    
    func (x *GetInputRequest) Reset()

### func (*GetInputRequest) String 
    
    
    func (x *GetInputRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetPoolRequest
    
    
    type GetPoolRequest struct {
    
    	// Required. The name of the pool resource, in the form of:
    	// `projects/{project}/locations/{location}/pools/{poolId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.GetPool".

### func (*GetPoolRequest) Descriptor 
    
    
    func (*GetPoolRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPoolRequest.ProtoReflect.Descriptor instead.

### func (*GetPoolRequest) GetName 
    
    
    func (x *GetPoolRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetPoolRequest) ProtoMessage 
    
    
    func (*GetPoolRequest) ProtoMessage()

### func (*GetPoolRequest) ProtoReflect 
    
    
    func (x *GetPoolRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPoolRequest) Reset 
    
    
    func (x *GetPoolRequest) Reset()

### func (*GetPoolRequest) String 
    
    
    func (x *GetPoolRequest) String() [string](https://pkg.go.dev/builtin#string)

## Input
    
    
    type Input struct {
    
    	// The resource name of the input, in the form of:
    	// `projects/{project}/locations/{location}/inputs/{inputId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Source type.
    	Type Input_Type `protobuf:"varint,5,opt,name=type,proto3,enum=google.cloud.video.livestream.v1.Input_Type" json:"type,omitempty"`
    	// Tier defines the maximum input specification that is accepted by the
    	// video pipeline. The billing is charged based on the tier specified here.
    	// See [Pricing](https://cloud.google.com/livestream/pricing) for more detail.
    	// The default is `HD`.
    	Tier Input_Tier `protobuf:"varint,14,opt,name=tier,proto3,enum=google.cloud.video.livestream.v1.Input_Tier" json:"tier,omitempty"`
    	// Output only. URI to push the input stream to.
    	// Its format depends on the input
    	// [type][google.cloud.video.livestream.v1.Input.type], for example:
    	//
    	// *  `RTMP_PUSH`: `rtmp://1.2.3.4/live/{STREAM-ID}`
    	// *  `SRT_PUSH`: `srt://1.2.3.4:4201?streamid={STREAM-ID}`
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Preprocessing configurations.
    	PreprocessingConfig *PreprocessingConfig `protobuf:"bytes,9,opt,name=preprocessing_config,json=preprocessingConfig,proto3" json:"preprocessing_config,omitempty"`
    	// Security rule for access control.
    	SecurityRules *Input_SecurityRule `protobuf:"bytes,12,opt,name=security_rules,json=securityRules,proto3" json:"security_rules,omitempty"`
    	// Output only. The information for the input stream. This field will be
    	// present only when this input receives the input stream.
    	InputStreamProperty *InputStreamProperty `protobuf:"bytes,15,opt,name=input_stream_property,json=inputStreamProperty,proto3" json:"input_stream_property,omitempty"`
    	// contains filtered or unexported fields
    }

Input resource represents the endpoint from which the channel ingests the input stream.

### func (*Input) Descriptor 
    
    
    func (*Input) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Input.ProtoReflect.Descriptor instead.

### func (*Input) GetCreateTime 
    
    
    func (x *Input) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Input) GetInputStreamProperty 
    
    
    func (x *Input) GetInputStreamProperty() *InputStreamProperty

### func (*Input) GetLabels 
    
    
    func (x *Input) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Input) GetName 
    
    
    func (x *Input) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Input) GetPreprocessingConfig 
    
    
    func (x *Input) GetPreprocessingConfig() *PreprocessingConfig

### func (*Input) GetSecurityRules 
    
    
    func (x *Input) GetSecurityRules() *Input_SecurityRule

### func (*Input) GetTier 
    
    
    func (x *Input) GetTier() Input_Tier

### func (*Input) GetType 
    
    
    func (x *Input) GetType() Input_Type

### func (*Input) GetUpdateTime 
    
    
    func (x *Input) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Input) GetUri 
    
    
    func (x *Input) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*Input) ProtoMessage 
    
    
    func (*Input) ProtoMessage()

### func (*Input) ProtoReflect 
    
    
    func (x *Input) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Input) Reset 
    
    
    func (x *Input) Reset()

### func (*Input) String 
    
    
    func (x *Input) String() [string](https://pkg.go.dev/builtin#string)

## InputAttachment
    
    
    type InputAttachment struct {
    
    	// A unique key for this input attachment. The key must be 1-63
    	// characters in length. The key must begin and end with a letter (regardless
    	// of case) or a number, but can contain dashes or underscores in between.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
    	// The resource name of an existing input, in the form of:
    	// `projects/{project}/locations/{location}/inputs/{inputId}`.
    	Input [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=input,proto3" json:"input,omitempty"`
    	// Automatic failover configurations.
    	AutomaticFailover *InputAttachment_AutomaticFailover `protobuf:"bytes,3,opt,name=automatic_failover,json=automaticFailover,proto3" json:"automatic_failover,omitempty"`
    	// contains filtered or unexported fields
    }

A group of information for attaching an input resource to this channel.

### func (*InputAttachment) Descriptor 
    
    
    func (*InputAttachment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InputAttachment.ProtoReflect.Descriptor instead.

### func (*InputAttachment) GetAutomaticFailover 
    
    
    func (x *InputAttachment) GetAutomaticFailover() *InputAttachment_AutomaticFailover

### func (*InputAttachment) GetInput 
    
    
    func (x *InputAttachment) GetInput() [string](https://pkg.go.dev/builtin#string)

### func (*InputAttachment) GetKey 
    
    
    func (x *InputAttachment) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*InputAttachment) ProtoMessage 
    
    
    func (*InputAttachment) ProtoMessage()

### func (*InputAttachment) ProtoReflect 
    
    
    func (x *InputAttachment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InputAttachment) Reset 
    
    
    func (x *InputAttachment) Reset()

### func (*InputAttachment) String 
    
    
    func (x *InputAttachment) String() [string](https://pkg.go.dev/builtin#string)

## InputAttachment_AutomaticFailover
    
    
    type InputAttachment_AutomaticFailover struct {
    
    	// The
    	// [InputAttachment.key][google.cloud.video.livestream.v1.InputAttachment.key]s
    	// of inputs to failover to when this input is disconnected. Currently, only
    	// up to one backup input is supported.
    	InputKeys [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=input_keys,json=inputKeys,proto3" json:"input_keys,omitempty"`
    	// contains filtered or unexported fields
    }

Configurations to follow when automatic failover happens.

### func (*InputAttachment_AutomaticFailover) Descriptor 
    
    
    func (*InputAttachment_AutomaticFailover) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InputAttachment_AutomaticFailover.ProtoReflect.Descriptor instead.

### func (*InputAttachment_AutomaticFailover) GetInputKeys 
    
    
    func (x *InputAttachment_AutomaticFailover) GetInputKeys() [][string](https://pkg.go.dev/builtin#string)

### func (*InputAttachment_AutomaticFailover) ProtoMessage 
    
    
    func (*InputAttachment_AutomaticFailover) ProtoMessage()

### func (*InputAttachment_AutomaticFailover) ProtoReflect 
    
    
    func (x *InputAttachment_AutomaticFailover) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InputAttachment_AutomaticFailover) Reset 
    
    
    func (x *InputAttachment_AutomaticFailover) Reset()

### func (*InputAttachment_AutomaticFailover) String 
    
    
    func (x *InputAttachment_AutomaticFailover) String() [string](https://pkg.go.dev/builtin#string)

## InputConfig
    
    
    type InputConfig struct {
    
    	// Input switch mode. Default mode is `FAILOVER_PREFER_PRIMARY`.
    	InputSwitchMode InputConfig_InputSwitchMode `protobuf:"varint,1,opt,name=input_switch_mode,json=inputSwitchMode,proto3,enum=google.cloud.video.livestream.v1.InputConfig_InputSwitchMode" json:"input_switch_mode,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for the input sources of a channel.

### func (*InputConfig) Descriptor 
    
    
    func (*InputConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InputConfig.ProtoReflect.Descriptor instead.

### func (*InputConfig) GetInputSwitchMode 
    
    
    func (x *InputConfig) GetInputSwitchMode() InputConfig_InputSwitchMode

### func (*InputConfig) ProtoMessage 
    
    
    func (*InputConfig) ProtoMessage()

### func (*InputConfig) ProtoReflect 
    
    
    func (x *InputConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InputConfig) Reset 
    
    
    func (x *InputConfig) Reset()

### func (*InputConfig) String 
    
    
    func (x *InputConfig) String() [string](https://pkg.go.dev/builtin#string)

## InputConfig_InputSwitchMode
    
    
    type InputConfig_InputSwitchMode [int32](https://pkg.go.dev/builtin#int32)

Input switch mode.

### InputConfig_INPUT_SWITCH_MODE_UNSPECIFIED, InputConfig_FAILOVER_PREFER_PRIMARY, InputConfig_MANUAL
    
    
    const (
    	// The input switch mode is not specified.
    	InputConfig_INPUT_SWITCH_MODE_UNSPECIFIED InputConfig_InputSwitchMode = 0
    	// Automatic failover is enabled. The primary input stream is always
    	// preferred over its backup input streams configured using the
    	// [AutomaticFailover][google.cloud.video.livestream.v1.InputAttachment.AutomaticFailover]
    	// field.
    	InputConfig_FAILOVER_PREFER_PRIMARY InputConfig_InputSwitchMode = 1
    	// Automatic failover is disabled. You must use the
    	// [inputSwitch][google.cloud.video.livestream.v1.Event.input_switch] event
    	// to switch the active input source for the channel to stream from. When
    	// this mode is chosen, the
    	// [AutomaticFailover][google.cloud.video.livestream.v1.InputAttachment.AutomaticFailover]
    	// field is ignored.
    	InputConfig_MANUAL InputConfig_InputSwitchMode = 3
    )

### func (InputConfig_InputSwitchMode) Descriptor 
    
    
    func (InputConfig_InputSwitchMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (InputConfig_InputSwitchMode) Enum 
    
    
    func (x InputConfig_InputSwitchMode) Enum() *InputConfig_InputSwitchMode

### func (InputConfig_InputSwitchMode) EnumDescriptor 
    
    
    func (InputConfig_InputSwitchMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InputConfig_InputSwitchMode.Descriptor instead.

### func (InputConfig_InputSwitchMode) Number 
    
    
    func (x InputConfig_InputSwitchMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (InputConfig_InputSwitchMode) String 
    
    
    func (x InputConfig_InputSwitchMode) String() [string](https://pkg.go.dev/builtin#string)

### func (InputConfig_InputSwitchMode) Type 
    
    
    func (InputConfig_InputSwitchMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## InputStreamProperty
    
    
    type InputStreamProperty struct {
    
    	// The time that the current input stream is accepted and the connection is
    	// established.
    	LastEstablishTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=last_establish_time,json=lastEstablishTime,proto3" json:"last_establish_time,omitempty"`
    	// Properties of the video streams.
    	VideoStreams []*VideoStreamProperty `protobuf:"bytes,2,rep,name=video_streams,json=videoStreams,proto3" json:"video_streams,omitempty"`
    	// Properties of the audio streams.
    	AudioStreams []*AudioStreamProperty `protobuf:"bytes,3,rep,name=audio_streams,json=audioStreams,proto3" json:"audio_streams,omitempty"`
    	// contains filtered or unexported fields
    }

Properties of the input stream.

### func (*InputStreamProperty) Descriptor 
    
    
    func (*InputStreamProperty) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InputStreamProperty.ProtoReflect.Descriptor instead.

### func (*InputStreamProperty) GetAudioStreams 
    
    
    func (x *InputStreamProperty) GetAudioStreams() []*AudioStreamProperty

### func (*InputStreamProperty) GetLastEstablishTime 
    
    
    func (x *InputStreamProperty) GetLastEstablishTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*InputStreamProperty) GetVideoStreams 
    
    
    func (x *InputStreamProperty) GetVideoStreams() []*VideoStreamProperty

### func (*InputStreamProperty) ProtoMessage 
    
    
    func (*InputStreamProperty) ProtoMessage()

### func (*InputStreamProperty) ProtoReflect 
    
    
    func (x *InputStreamProperty) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InputStreamProperty) Reset 
    
    
    func (x *InputStreamProperty) Reset()

### func (*InputStreamProperty) String 
    
    
    func (x *InputStreamProperty) String() [string](https://pkg.go.dev/builtin#string)

## Input_SecurityRule
    
    
    type Input_SecurityRule struct {
    
    	// At least one ip range must match unless none specified. The IP range is
    	// defined by CIDR block: for example, `192.0.1.0/24` for a range and
    	// `192.0.1.0/32` for a single IP address.
    	IpRanges [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=ip_ranges,json=ipRanges,proto3" json:"ip_ranges,omitempty"`
    	// contains filtered or unexported fields
    }

Security rules for access control. Each field represents one security rule. Only when the source of the input stream satisfies all the fields, this input stream can be accepted.

### func (*Input_SecurityRule) Descriptor 
    
    
    func (*Input_SecurityRule) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Input_SecurityRule.ProtoReflect.Descriptor instead.

### func (*Input_SecurityRule) GetIpRanges 
    
    
    func (x *Input_SecurityRule) GetIpRanges() [][string](https://pkg.go.dev/builtin#string)

### func (*Input_SecurityRule) ProtoMessage 
    
    
    func (*Input_SecurityRule) ProtoMessage()

### func (*Input_SecurityRule) ProtoReflect 
    
    
    func (x *Input_SecurityRule) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Input_SecurityRule) Reset 
    
    
    func (x *Input_SecurityRule) Reset()

### func (*Input_SecurityRule) String 
    
    
    func (x *Input_SecurityRule) String() [string](https://pkg.go.dev/builtin#string)

## Input_Tier
    
    
    type Input_Tier [int32](https://pkg.go.dev/builtin#int32)

Tier of the input specification.

### Input_TIER_UNSPECIFIED, Input_SD, Input_HD, Input_UHD, Input_SD_H265, Input_HD_H265, Input_UHD_H265
    
    
    const (
    	// Tier is not specified.
    	Input_TIER_UNSPECIFIED Input_Tier = 0
    	// Resolution < 1280x720.="" bitrate=""><= 6="" mbps.="" fps=""><= 60.="" input_sd="">Input_Tier = 1
    	// Resolution <= 1920x1080.="" bitrate=""><= 25="" mbps.="" fps=""><= 60.="" input_hd="">Input_Tier = 2
    	// Resolution <= 4096x2160.="" bitrate=""><= 50="" mbps.="" fps=""><= 60.="" input_uhd="">Input_Tier = 3
    	// Resolution <= 1280x720.="" bitrate=""><= 6="" mbps.="" fps=""><= 60.="" h265="" codec.="" input_sd_h265="">Input_Tier = 4
    	// Resolution <= 1920x1080.="" bitrate=""><= 25="" mbps.="" fps=""><= 60.="" h265="" codec.="" input_hd_h265="">Input_Tier = 5
    	// Resolution <= 4096x2160.="" bitrate=""><= 50="" mbps.="" fps=""><= 60.="" h265="" codec.="" input_uhd_h265="">Input_Tier = 6
    )

### func (Input_Tier) Descriptor 
    
    
    func (Input_Tier) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Input_Tier) Enum 
    
    
    func (x Input_Tier) Enum() *Input_Tier

### func (Input_Tier) EnumDescriptor 
    
    
    func (Input_Tier) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Input_Tier.Descriptor instead.

### func (Input_Tier) Number 
    
    
    func (x Input_Tier) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Input_Tier) String 
    
    
    func (x Input_Tier) String() [string](https://pkg.go.dev/builtin#string)

### func (Input_Tier) Type 
    
    
    func (Input_Tier) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Input_Type
    
    
    type Input_Type [int32](https://pkg.go.dev/builtin#int32)

The type of the input.

### Input_TYPE_UNSPECIFIED, Input_RTMP_PUSH, Input_SRT_PUSH
    
    
    const (
    	// Input type is not specified.
    	Input_TYPE_UNSPECIFIED Input_Type = 0
    	// Input will take an rtmp input stream.
    	Input_RTMP_PUSH Input_Type = 1
    	// Input will take an srt (Secure Reliable Transport) input stream.
    	Input_SRT_PUSH Input_Type = 2
    )

### func (Input_Type) Descriptor 
    
    
    func (Input_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Input_Type) Enum 
    
    
    func (x Input_Type) Enum() *Input_Type

### func (Input_Type) EnumDescriptor 
    
    
    func (Input_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Input_Type.Descriptor instead.

### func (Input_Type) Number 
    
    
    func (x Input_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Input_Type) String 
    
    
    func (x Input_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (Input_Type) Type 
    
    
    func (Input_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListAssetsRequest
    
    
    type ListAssetsRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
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

Request message for "LivestreamService.ListAssets".

### func (*ListAssetsRequest) Descriptor 
    
    
    func (*ListAssetsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAssetsRequest.ProtoReflect.Descriptor instead.

### func (*ListAssetsRequest) GetFilter 
    
    
    func (x *ListAssetsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetOrderBy 
    
    
    func (x *ListAssetsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetPageSize 
    
    
    func (x *ListAssetsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAssetsRequest) GetPageToken 
    
    
    func (x *ListAssetsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetParent 
    
    
    func (x *ListAssetsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) ProtoMessage 
    
    
    func (*ListAssetsRequest) ProtoMessage()

### func (*ListAssetsRequest) ProtoReflect 
    
    
    func (x *ListAssetsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAssetsRequest) Reset 
    
    
    func (x *ListAssetsRequest) Reset()

### func (*ListAssetsRequest) String 
    
    
    func (x *ListAssetsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAssetsResponse
    
    
    type ListAssetsResponse struct {
    
    	// The list of Assets
    	Assets []*Asset `protobuf:"bytes,1,rep,name=assets,proto3" json:"assets,omitempty"`
    	// The next_page_token value returned from a previous List request, if any.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListAssets".

### func (*ListAssetsResponse) Descriptor 
    
    
    func (*ListAssetsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAssetsResponse.ProtoReflect.Descriptor instead.

### func (*ListAssetsResponse) GetAssets 
    
    
    func (x *ListAssetsResponse) GetAssets() []*Asset

### func (*ListAssetsResponse) GetNextPageToken 
    
    
    func (x *ListAssetsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsResponse) GetUnreachable 
    
    
    func (x *ListAssetsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsResponse) ProtoMessage 
    
    
    func (*ListAssetsResponse) ProtoMessage()

### func (*ListAssetsResponse) ProtoReflect 
    
    
    func (x *ListAssetsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAssetsResponse) Reset 
    
    
    func (x *ListAssetsResponse) Reset()

### func (*ListAssetsResponse) String 
    
    
    func (x *ListAssetsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListChannelsRequest
    
    
    type ListChannelsRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of items to return. If unspecified, server
    	// will pick an appropriate default. Server may return fewer items than
    	// requested. A caller should only rely on response's
    	// [next_page_token][google.cloud.video.livestream.v1.ListChannelsResponse.next_page_token]
    	// to determine if there are more items left to be queried.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// The next_page_token value returned from a previous List request, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// The filter to apply to list results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Specifies the ordering of results following syntax at
    	// https://cloud.google.com/apis/design/design_patterns#sorting_order.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.ListChannels".

### func (*ListChannelsRequest) Descriptor 
    
    
    func (*ListChannelsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListChannelsRequest.ProtoReflect.Descriptor instead.

### func (*ListChannelsRequest) GetFilter 
    
    
    func (x *ListChannelsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsRequest) GetOrderBy 
    
    
    func (x *ListChannelsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsRequest) GetPageSize 
    
    
    func (x *ListChannelsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListChannelsRequest) GetPageToken 
    
    
    func (x *ListChannelsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsRequest) GetParent 
    
    
    func (x *ListChannelsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsRequest) ProtoMessage 
    
    
    func (*ListChannelsRequest) ProtoMessage()

### func (*ListChannelsRequest) ProtoReflect 
    
    
    func (x *ListChannelsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListChannelsRequest) Reset 
    
    
    func (x *ListChannelsRequest) Reset()

### func (*ListChannelsRequest) String 
    
    
    func (x *ListChannelsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListChannelsResponse
    
    
    type ListChannelsResponse struct {
    
    	// A list of channels.
    	Channels []*Channel `protobuf:"bytes,1,rep,name=channels,proto3" json:"channels,omitempty"`
    	// Token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListChannels".

### func (*ListChannelsResponse) Descriptor 
    
    
    func (*ListChannelsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListChannelsResponse.ProtoReflect.Descriptor instead.

### func (*ListChannelsResponse) GetChannels 
    
    
    func (x *ListChannelsResponse) GetChannels() []*Channel

### func (*ListChannelsResponse) GetNextPageToken 
    
    
    func (x *ListChannelsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsResponse) GetUnreachable 
    
    
    func (x *ListChannelsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListChannelsResponse) ProtoMessage 
    
    
    func (*ListChannelsResponse) ProtoMessage()

### func (*ListChannelsResponse) ProtoReflect 
    
    
    func (x *ListChannelsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListChannelsResponse) Reset 
    
    
    func (x *ListChannelsResponse) Reset()

### func (*ListChannelsResponse) String 
    
    
    func (x *ListChannelsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListClipsRequest
    
    
    type ListClipsRequest struct {
    
    	// Required. Parent value for ListClipsRequest
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

Request message for "LivestreamService.ListClips".

### func (*ListClipsRequest) Descriptor 
    
    
    func (*ListClipsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListClipsRequest.ProtoReflect.Descriptor instead.

### func (*ListClipsRequest) GetFilter 
    
    
    func (x *ListClipsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListClipsRequest) GetOrderBy 
    
    
    func (x *ListClipsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListClipsRequest) GetPageSize 
    
    
    func (x *ListClipsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListClipsRequest) GetPageToken 
    
    
    func (x *ListClipsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListClipsRequest) GetParent 
    
    
    func (x *ListClipsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListClipsRequest) ProtoMessage 
    
    
    func (*ListClipsRequest) ProtoMessage()

### func (*ListClipsRequest) ProtoReflect 
    
    
    func (x *ListClipsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListClipsRequest) Reset 
    
    
    func (x *ListClipsRequest) Reset()

### func (*ListClipsRequest) String 
    
    
    func (x *ListClipsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListClipsResponse
    
    
    type ListClipsResponse struct {
    
    	// The list of Clip
    	Clips []*Clip `protobuf:"bytes,1,rep,name=clips,proto3" json:"clips,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListClips".

### func (*ListClipsResponse) Descriptor 
    
    
    func (*ListClipsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListClipsResponse.ProtoReflect.Descriptor instead.

### func (*ListClipsResponse) GetClips 
    
    
    func (x *ListClipsResponse) GetClips() []*Clip

### func (*ListClipsResponse) GetNextPageToken 
    
    
    func (x *ListClipsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListClipsResponse) GetUnreachable 
    
    
    func (x *ListClipsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListClipsResponse) ProtoMessage 
    
    
    func (*ListClipsResponse) ProtoMessage()

### func (*ListClipsResponse) ProtoReflect 
    
    
    func (x *ListClipsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListClipsResponse) Reset 
    
    
    func (x *ListClipsResponse) Reset()

### func (*ListClipsResponse) String 
    
    
    func (x *ListClipsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListDvrSessionsRequest
    
    
    type ListDvrSessionsRequest struct {
    
    	// Required. Parent value for ListDvrSessionsRequest
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Optional. Requested page size. Server may return fewer items than
    	// requested. If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// Optional. A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. Filtering results
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Optional. Hint for how to order the results
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.ListDvrSessions".

### func (*ListDvrSessionsRequest) Descriptor 
    
    
    func (*ListDvrSessionsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDvrSessionsRequest.ProtoReflect.Descriptor instead.

### func (*ListDvrSessionsRequest) GetFilter 
    
    
    func (x *ListDvrSessionsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsRequest) GetOrderBy 
    
    
    func (x *ListDvrSessionsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsRequest) GetPageSize 
    
    
    func (x *ListDvrSessionsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListDvrSessionsRequest) GetPageToken 
    
    
    func (x *ListDvrSessionsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsRequest) GetParent 
    
    
    func (x *ListDvrSessionsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsRequest) ProtoMessage 
    
    
    func (*ListDvrSessionsRequest) ProtoMessage()

### func (*ListDvrSessionsRequest) ProtoReflect 
    
    
    func (x *ListDvrSessionsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDvrSessionsRequest) Reset 
    
    
    func (x *ListDvrSessionsRequest) Reset()

### func (*ListDvrSessionsRequest) String 
    
    
    func (x *ListDvrSessionsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListDvrSessionsResponse
    
    
    type ListDvrSessionsResponse struct {
    
    	// The list of DVR sessions
    	DvrSessions []*DvrSession `protobuf:"bytes,1,rep,name=dvr_sessions,json=dvrSessions,proto3" json:"dvr_sessions,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListDvrSessions".

### func (*ListDvrSessionsResponse) Descriptor 
    
    
    func (*ListDvrSessionsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDvrSessionsResponse.ProtoReflect.Descriptor instead.

### func (*ListDvrSessionsResponse) GetDvrSessions 
    
    
    func (x *ListDvrSessionsResponse) GetDvrSessions() []*DvrSession

### func (*ListDvrSessionsResponse) GetNextPageToken 
    
    
    func (x *ListDvrSessionsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsResponse) GetUnreachable 
    
    
    func (x *ListDvrSessionsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListDvrSessionsResponse) ProtoMessage 
    
    
    func (*ListDvrSessionsResponse) ProtoMessage()

### func (*ListDvrSessionsResponse) ProtoReflect 
    
    
    func (x *ListDvrSessionsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDvrSessionsResponse) Reset 
    
    
    func (x *ListDvrSessionsResponse) Reset()

### func (*ListDvrSessionsResponse) String 
    
    
    func (x *ListDvrSessionsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListEventsRequest
    
    
    type ListEventsRequest struct {
    
    	// Required. The parent channel for the resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of items to return. If unspecified, server
    	// will pick an appropriate default. Server may return fewer items than
    	// requested. A caller should only rely on response's
    	// [next_page_token][google.cloud.video.livestream.v1.ListEventsResponse.next_page_token]
    	// to determine if there are more items left to be queried.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// The next_page_token value returned from a previous List request, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// The filter to apply to list results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Specifies the ordering of results following syntax at
    	// https://cloud.google.com/apis/design/design_patterns#sorting_order.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.ListEvents".

### func (*ListEventsRequest) Descriptor 
    
    
    func (*ListEventsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListEventsRequest.ProtoReflect.Descriptor instead.

### func (*ListEventsRequest) GetFilter 
    
    
    func (x *ListEventsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListEventsRequest) GetOrderBy 
    
    
    func (x *ListEventsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListEventsRequest) GetPageSize 
    
    
    func (x *ListEventsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListEventsRequest) GetPageToken 
    
    
    func (x *ListEventsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListEventsRequest) GetParent 
    
    
    func (x *ListEventsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListEventsRequest) ProtoMessage 
    
    
    func (*ListEventsRequest) ProtoMessage()

### func (*ListEventsRequest) ProtoReflect 
    
    
    func (x *ListEventsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListEventsRequest) Reset 
    
    
    func (x *ListEventsRequest) Reset()

### func (*ListEventsRequest) String 
    
    
    func (x *ListEventsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListEventsResponse
    
    
    type ListEventsResponse struct {
    
    	// A list of events.
    	Events []*Event `protobuf:"bytes,1,rep,name=events,proto3" json:"events,omitempty"`
    	// Token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListEvents".

### func (*ListEventsResponse) Descriptor 
    
    
    func (*ListEventsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListEventsResponse.ProtoReflect.Descriptor instead.

### func (*ListEventsResponse) GetEvents 
    
    
    func (x *ListEventsResponse) GetEvents() []*Event

### func (*ListEventsResponse) GetNextPageToken 
    
    
    func (x *ListEventsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListEventsResponse) GetUnreachable 
    
    
    func (x *ListEventsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListEventsResponse) ProtoMessage 
    
    
    func (*ListEventsResponse) ProtoMessage()

### func (*ListEventsResponse) ProtoReflect 
    
    
    func (x *ListEventsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListEventsResponse) Reset 
    
    
    func (x *ListEventsResponse) Reset()

### func (*ListEventsResponse) String 
    
    
    func (x *ListEventsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListInputsRequest
    
    
    type ListInputsRequest struct {
    
    	// Required. The parent location for the resource, in the form of:
    	// `projects/{project}/locations/{location}`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of items to return. If unspecified, server
    	// will pick an appropriate default. Server may return fewer items than
    	// requested. A caller should only rely on response's
    	// [next_page_token][google.cloud.video.livestream.v1.ListInputsResponse.next_page_token]
    	// to determine if there are more items left to be queried.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// The next_page_token value returned from a previous List request, if any.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// The filter to apply to list results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Specifies the ordering of results following syntax at [Sorting
    	// Order](https://cloud.google.com/apis/design/design_patterns#sorting_order).
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.ListInputs".

### func (*ListInputsRequest) Descriptor 
    
    
    func (*ListInputsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInputsRequest.ProtoReflect.Descriptor instead.

### func (*ListInputsRequest) GetFilter 
    
    
    func (x *ListInputsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListInputsRequest) GetOrderBy 
    
    
    func (x *ListInputsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListInputsRequest) GetPageSize 
    
    
    func (x *ListInputsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListInputsRequest) GetPageToken 
    
    
    func (x *ListInputsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInputsRequest) GetParent 
    
    
    func (x *ListInputsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListInputsRequest) ProtoMessage 
    
    
    func (*ListInputsRequest) ProtoMessage()

### func (*ListInputsRequest) ProtoReflect 
    
    
    func (x *ListInputsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInputsRequest) Reset 
    
    
    func (x *ListInputsRequest) Reset()

### func (*ListInputsRequest) String 
    
    
    func (x *ListInputsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListInputsResponse
    
    
    type ListInputsResponse struct {
    
    	// A list of inputs.
    	Inputs []*Input `protobuf:"bytes,1,rep,name=inputs,proto3" json:"inputs,omitempty"`
    	// Token to retrieve the next page of results, or empty if there are no more
    	// results in the list.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.ListInputs".

### func (*ListInputsResponse) Descriptor 
    
    
    func (*ListInputsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListInputsResponse.ProtoReflect.Descriptor instead.

### func (*ListInputsResponse) GetInputs 
    
    
    func (x *ListInputsResponse) GetInputs() []*Input

### func (*ListInputsResponse) GetNextPageToken 
    
    
    func (x *ListInputsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListInputsResponse) GetUnreachable 
    
    
    func (x *ListInputsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListInputsResponse) ProtoMessage 
    
    
    func (*ListInputsResponse) ProtoMessage()

### func (*ListInputsResponse) ProtoReflect 
    
    
    func (x *ListInputsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListInputsResponse) Reset 
    
    
    func (x *ListInputsResponse) Reset()

### func (*ListInputsResponse) String 
    
    
    func (x *ListInputsResponse) String() [string](https://pkg.go.dev/builtin#string)

## LivestreamServiceClient
    
    
    type LivestreamServiceClient interface {
    	// Creates a channel with the provided unique ID in the specified
    	// region.
    	CreateChannel(ctx context.Context, in *CreateChannelRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all channels in the specified region.
    	ListChannels(ctx context.Context, in *ListChannelsRequest, opts ...grpc.CallOption) (*ListChannelsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified channel.
    	GetChannel(ctx context.Context, in *GetChannelRequest, opts ...grpc.CallOption) (*Channel, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified channel.
    	DeleteChannel(ctx context.Context, in *DeleteChannelRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified channel.
    	UpdateChannel(ctx context.Context, in *UpdateChannelRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Starts the specified channel. Part of the video pipeline will be created
    	// only when the StartChannel request is received by the server.
    	StartChannel(ctx context.Context, in *StartChannelRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Stops the specified channel. Part of the video pipeline will be released
    	// when the StopChannel request is received by the server.
    	StopChannel(ctx context.Context, in *StopChannelRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Starts distribution which delivers outputs to the destination indicated by
    	// the Distribution configuration.
    	StartDistribution(ctx context.Context, in *StartDistributionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Stops the specified distribution.
    	StopDistribution(ctx context.Context, in *StopDistributionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates an input with the provided unique ID in the specified region.
    	CreateInput(ctx context.Context, in *CreateInputRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all inputs in the specified region.
    	ListInputs(ctx context.Context, in *ListInputsRequest, opts ...grpc.CallOption) (*ListInputsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified input.
    	GetInput(ctx context.Context, in *GetInputRequest, opts ...grpc.CallOption) (*Input, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified input.
    	DeleteInput(ctx context.Context, in *DeleteInputRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified input.
    	UpdateInput(ctx context.Context, in *UpdateInputRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Preview the streaming content of the specified input.
    	PreviewInput(ctx context.Context, in *PreviewInputRequest, opts ...grpc.CallOption) (*PreviewInputResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an event with the provided unique ID in the specified channel.
    	CreateEvent(ctx context.Context, in *CreateEventRequest, opts ...grpc.CallOption) (*Event, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all events in the specified channel.
    	ListEvents(ctx context.Context, in *ListEventsRequest, opts ...grpc.CallOption) (*ListEventsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified event.
    	GetEvent(ctx context.Context, in *GetEventRequest, opts ...grpc.CallOption) (*Event, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified event.
    	DeleteEvent(ctx context.Context, in *DeleteEventRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all clips in the specified channel.
    	ListClips(ctx context.Context, in *ListClipsRequest, opts ...grpc.CallOption) (*ListClipsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified clip.
    	GetClip(ctx context.Context, in *GetClipRequest, opts ...grpc.CallOption) (*Clip, [error](https://pkg.go.dev/builtin#error))
    	// Creates a clip with the provided clip ID in the specified channel.
    	CreateClip(ctx context.Context, in *CreateClipRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified clip job resource. This method only deletes the clip
    	// job and does not delete the VOD clip stored in Cloud Storage.
    	DeleteClip(ctx context.Context, in *DeleteClipRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a DVR session with the provided unique ID in the specified channel.
    	CreateDvrSession(ctx context.Context, in *CreateDvrSessionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all DVR sessions in the specified channel.
    	ListDvrSessions(ctx context.Context, in *ListDvrSessionsRequest, opts ...grpc.CallOption) (*ListDvrSessionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified DVR session.
    	GetDvrSession(ctx context.Context, in *GetDvrSessionRequest, opts ...grpc.CallOption) (*DvrSession, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified DVR session.
    	DeleteDvrSession(ctx context.Context, in *DeleteDvrSessionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified DVR session.
    	UpdateDvrSession(ctx context.Context, in *UpdateDvrSessionRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a Asset with the provided unique ID in the specified
    	// region.
    	CreateAsset(ctx context.Context, in *CreateAssetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified asset if it is not used.
    	DeleteAsset(ctx context.Context, in *DeleteAssetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified asset.
    	GetAsset(ctx context.Context, in *GetAssetRequest, opts ...grpc.CallOption) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all assets in the specified region.
    	ListAssets(ctx context.Context, in *ListAssetsRequest, opts ...grpc.CallOption) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified pool.
    	GetPool(ctx context.Context, in *GetPoolRequest, opts ...grpc.CallOption) (*Pool, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified pool.
    	UpdatePool(ctx context.Context, in *UpdatePoolRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

LivestreamServiceClient is the client API for LivestreamService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewLivestreamServiceClient 
    
    
    func NewLivestreamServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) LivestreamServiceClient

## LivestreamServiceServer
    
    
    type LivestreamServiceServer interface {
    	// Creates a channel with the provided unique ID in the specified
    	// region.
    	CreateChannel(context.Context, *CreateChannelRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all channels in the specified region.
    	ListChannels(context.Context, *ListChannelsRequest) (*ListChannelsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified channel.
    	GetChannel(context.Context, *GetChannelRequest) (*Channel, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified channel.
    	DeleteChannel(context.Context, *DeleteChannelRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified channel.
    	UpdateChannel(context.Context, *UpdateChannelRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Starts the specified channel. Part of the video pipeline will be created
    	// only when the StartChannel request is received by the server.
    	StartChannel(context.Context, *StartChannelRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Stops the specified channel. Part of the video pipeline will be released
    	// when the StopChannel request is received by the server.
    	StopChannel(context.Context, *StopChannelRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Starts distribution which delivers outputs to the destination indicated by
    	// the Distribution configuration.
    	StartDistribution(context.Context, *StartDistributionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Stops the specified distribution.
    	StopDistribution(context.Context, *StopDistributionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates an input with the provided unique ID in the specified region.
    	CreateInput(context.Context, *CreateInputRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all inputs in the specified region.
    	ListInputs(context.Context, *ListInputsRequest) (*ListInputsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified input.
    	GetInput(context.Context, *GetInputRequest) (*Input, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified input.
    	DeleteInput(context.Context, *DeleteInputRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified input.
    	UpdateInput(context.Context, *UpdateInputRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Preview the streaming content of the specified input.
    	PreviewInput(context.Context, *PreviewInputRequest) (*PreviewInputResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an event with the provided unique ID in the specified channel.
    	CreateEvent(context.Context, *CreateEventRequest) (*Event, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all events in the specified channel.
    	ListEvents(context.Context, *ListEventsRequest) (*ListEventsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified event.
    	GetEvent(context.Context, *GetEventRequest) (*Event, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified event.
    	DeleteEvent(context.Context, *DeleteEventRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all clips in the specified channel.
    	ListClips(context.Context, *ListClipsRequest) (*ListClipsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified clip.
    	GetClip(context.Context, *GetClipRequest) (*Clip, [error](https://pkg.go.dev/builtin#error))
    	// Creates a clip with the provided clip ID in the specified channel.
    	CreateClip(context.Context, *CreateClipRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified clip job resource. This method only deletes the clip
    	// job and does not delete the VOD clip stored in Cloud Storage.
    	DeleteClip(context.Context, *DeleteClipRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a DVR session with the provided unique ID in the specified channel.
    	CreateDvrSession(context.Context, *CreateDvrSessionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all DVR sessions in the specified channel.
    	ListDvrSessions(context.Context, *ListDvrSessionsRequest) (*ListDvrSessionsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified DVR session.
    	GetDvrSession(context.Context, *GetDvrSessionRequest) (*DvrSession, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified DVR session.
    	DeleteDvrSession(context.Context, *DeleteDvrSessionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified DVR session.
    	UpdateDvrSession(context.Context, *UpdateDvrSessionRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a Asset with the provided unique ID in the specified
    	// region.
    	CreateAsset(context.Context, *CreateAssetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes the specified asset if it is not used.
    	DeleteAsset(context.Context, *DeleteAssetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified asset.
    	GetAsset(context.Context, *GetAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Returns a list of all assets in the specified region.
    	ListAssets(context.Context, *ListAssetsRequest) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Returns the specified pool.
    	GetPool(context.Context, *GetPoolRequest) (*Pool, [error](https://pkg.go.dev/builtin#error))
    	// Updates the specified pool.
    	UpdatePool(context.Context, *UpdatePoolRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

LivestreamServiceServer is the server API for LivestreamService service. All implementations should embed UnimplementedLivestreamServiceServer for forward compatibility

## LogConfig
    
    
    type LogConfig struct {
    
    	// The severity level of platform logging for this resource.
    	LogSeverity LogConfig_LogSeverity `protobuf:"varint,1,opt,name=log_severity,json=logSeverity,proto3,enum=google.cloud.video.livestream.v1.LogConfig_LogSeverity" json:"log_severity,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration of platform logs. See [Using and managing platform logs](https://cloud.google.com/logging/docs/api/platform-logs#managing-logs) for more information about how to view platform logs through Cloud Logging.

### func (*LogConfig) Descriptor 
    
    
    func (*LogConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LogConfig.ProtoReflect.Descriptor instead.

### func (*LogConfig) GetLogSeverity 
    
    
    func (x *LogConfig) GetLogSeverity() LogConfig_LogSeverity

### func (*LogConfig) ProtoMessage 
    
    
    func (*LogConfig) ProtoMessage()

### func (*LogConfig) ProtoReflect 
    
    
    func (x *LogConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*LogConfig) Reset 
    
    
    func (x *LogConfig) Reset()

### func (*LogConfig) String 
    
    
    func (x *LogConfig) String() [string](https://pkg.go.dev/builtin#string)

## LogConfig_LogSeverity
    
    
    type LogConfig_LogSeverity [int32](https://pkg.go.dev/builtin#int32)

The severity level of platform logging for this channel. Logs with a severity level higher than or equal to the chosen severity level will be logged and can be viewed through Cloud Logging. The severity level of a log is ranked as followed from low to high: DEBUG < INFO < NOTICE < WARNING < ERROR < CRITICAL < ALERT < EMERGENCY. See [LogSeverity](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) for more information.

### LogConfig_LOG_SEVERITY_UNSPECIFIED, LogConfig_OFF, LogConfig_DEBUG, LogConfig_INFO, LogConfig_WARNING, LogConfig_ERROR
    
    
    const (
    	// Log severity is not specified. This is the same as log severity is OFF.
    	LogConfig_LOG_SEVERITY_UNSPECIFIED LogConfig_LogSeverity = 0
    	// Log is turned off.
    	LogConfig_OFF LogConfig_LogSeverity = 1
    	// Log with severity higher than or equal to DEBUG are logged.
    	LogConfig_DEBUG LogConfig_LogSeverity = 100
    	// Logs with severity higher than or equal to INFO are logged.
    	LogConfig_INFO LogConfig_LogSeverity = 200
    	// Logs with severity higher than or equal to WARNING are logged.
    	LogConfig_WARNING LogConfig_LogSeverity = 400
    	// Logs with severity higher than or equal to ERROR are logged.
    	LogConfig_ERROR LogConfig_LogSeverity = 500
    )

### func (LogConfig_LogSeverity) Descriptor 
    
    
    func (LogConfig_LogSeverity) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (LogConfig_LogSeverity) Enum 
    
    
    func (x LogConfig_LogSeverity) Enum() *LogConfig_LogSeverity

### func (LogConfig_LogSeverity) EnumDescriptor 
    
    
    func (LogConfig_LogSeverity) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LogConfig_LogSeverity.Descriptor instead.

### func (LogConfig_LogSeverity) Number 
    
    
    func (x LogConfig_LogSeverity) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (LogConfig_LogSeverity) String 
    
    
    func (x LogConfig_LogSeverity) String() [string](https://pkg.go.dev/builtin#string)

### func (LogConfig_LogSeverity) Type 
    
    
    func (LogConfig_LogSeverity) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Manifest
    
    
    type Manifest struct {
    
    	// The name of the generated file. The default is `manifest` with the
    	// extension suffix corresponding to the `Manifest`
    	// [type][google.cloud.video.livestream.v1.Manifest.type]. If multiple
    	// manifests are added to the channel, each must have a unique file name.
    	FileName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=file_name,json=fileName,proto3" json:"file_name,omitempty"`
    	// Required. Type of the manifest, can be `HLS` or `DASH`.
    	Type Manifest_ManifestType `protobuf:"varint,2,opt,name=type,proto3,enum=google.cloud.video.livestream.v1.Manifest_ManifestType" json:"type,omitempty"`
    	// Required. List of `MuxStream`
    	// [key][google.cloud.video.livestream.v1.MuxStream.key]s that should appear
    	// in this manifest.
    	//
    	// - For HLS, either `fmp4` or `ts` mux streams can be specified but not
    	// mixed.
    	// - For DASH, only `fmp4` mux streams can be specified.
    	MuxStreams [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=mux_streams,json=muxStreams,proto3" json:"mux_streams,omitempty"`
    	// Maximum number of segments that this manifest holds. Once the manifest
    	// reaches this maximum number of segments, whenever a new segment is added to
    	// the manifest, the oldest segment will be removed from the manifest.
    	// The minimum value is 3 and the default value is 5.
    	MaxSegmentCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=max_segment_count,json=maxSegmentCount,proto3" json:"max_segment_count,omitempty"`
    	// How long to keep a segment on the output Google Cloud Storage bucket after
    	// it is removed from the manifest. This field should be large enough to cover
    	// the manifest propagation delay. Otherwise, a player could receive 404
    	// errors while accessing segments which are listed in the manifest that the
    	// player has, but were already deleted from the output Google Cloud Storage
    	// bucket. Default value is `60s`.
    	//
    	// If both segment_keep_duration and
    	// [RetentionConfig.retention_window_duration][google.cloud.video.livestream.v1.RetentionConfig.retention_window_duration]
    	// are set,
    	// [RetentionConfig.retention_window_duration][google.cloud.video.livestream.v1.RetentionConfig.retention_window_duration]
    	// is used and segment_keep_duration is ignored.
    	SegmentKeepDuration *durationpb.Duration `protobuf:"bytes,5,opt,name=segment_keep_duration,json=segmentKeepDuration,proto3" json:"segment_keep_duration,omitempty"`
    	// Whether to use the timecode, as specified in timecode config, when setting:
    	//
    	// - `availabilityStartTime` attribute in DASH manifests.
    	// - `#EXT-X-PROGRAM-DATE-TIME` tag in HLS manifests.
    	//
    	// If false, ignore the input timecode and use the time from system clock
    	// when the manifest is first generated. This is the default behavior.
    	UseTimecodeAsTimeline [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=use_timecode_as_timeline,json=useTimecodeAsTimeline,proto3" json:"use_timecode_as_timeline,omitempty"`
    	// Optional. A unique key for this manifest.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=key,proto3" json:"key,omitempty"`
    	// contains filtered or unexported fields
    }

Manifest configuration.

### func (*Manifest) Descriptor 
    
    
    func (*Manifest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Manifest.ProtoReflect.Descriptor instead.

### func (*Manifest) GetFileName 
    
    
    func (x *Manifest) GetFileName() [string](https://pkg.go.dev/builtin#string)

### func (*Manifest) GetKey 
    
    
    func (x *Manifest) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*Manifest) GetMaxSegmentCount 
    
    
    func (x *Manifest) GetMaxSegmentCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Manifest) GetMuxStreams 
    
    
    func (x *Manifest) GetMuxStreams() [][string](https://pkg.go.dev/builtin#string)

### func (*Manifest) GetSegmentKeepDuration 
    
    
    func (x *Manifest) GetSegmentKeepDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*Manifest) GetType 
    
    
    func (x *Manifest) GetType() Manifest_ManifestType

### func (*Manifest) GetUseTimecodeAsTimeline 
    
    
    func (x *Manifest) GetUseTimecodeAsTimeline() [bool](https://pkg.go.dev/builtin#bool)

### func (*Manifest) ProtoMessage 
    
    
    func (*Manifest) ProtoMessage()

### func (*Manifest) ProtoReflect 
    
    
    func (x *Manifest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Manifest) Reset 
    
    
    func (x *Manifest) Reset()

### func (*Manifest) String 
    
    
    func (x *Manifest) String() [string](https://pkg.go.dev/builtin#string)

## Manifest_ManifestType
    
    
    type Manifest_ManifestType [int32](https://pkg.go.dev/builtin#int32)

The manifest type can be either `HLS` or `DASH`.

### Manifest_MANIFEST_TYPE_UNSPECIFIED, Manifest_HLS, Manifest_DASH
    
    
    const (
    	// The manifest type is not specified.
    	Manifest_MANIFEST_TYPE_UNSPECIFIED Manifest_ManifestType = 0
    	// Create an `HLS` manifest. The corresponding file extension is `.m3u8`.
    	Manifest_HLS Manifest_ManifestType = 1
    	// Create a `DASH` manifest. The corresponding file extension is `.mpd`.
    	Manifest_DASH Manifest_ManifestType = 2
    )

### func (Manifest_ManifestType) Descriptor 
    
    
    func (Manifest_ManifestType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Manifest_ManifestType) Enum 
    
    
    func (x Manifest_ManifestType) Enum() *Manifest_ManifestType

### func (Manifest_ManifestType) EnumDescriptor 
    
    
    func (Manifest_ManifestType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Manifest_ManifestType.Descriptor instead.

### func (Manifest_ManifestType) Number 
    
    
    func (x Manifest_ManifestType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Manifest_ManifestType) String 
    
    
    func (x Manifest_ManifestType) String() [string](https://pkg.go.dev/builtin#string)

### func (Manifest_ManifestType) Type 
    
    
    func (Manifest_ManifestType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MuxStream
    
    
    type MuxStream struct {
    
    	// A unique key for this multiplexed stream. The key must be 1-63
    	// characters in length. The key must begin and end with a letter (regardless
    	// of case) or a number, but can contain dashes or underscores in between.
    	Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
    	// The container format. The default is `fmp4`.
    	//
    	// Supported container formats:
    	//
    	// - `fmp4` - the corresponding file extension is `.m4s`
    	// - `ts` - the corresponding file extension is `.ts`
    	Container [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=container,proto3" json:"container,omitempty"`
    	// List of `ElementaryStream`
    	// [key][google.cloud.video.livestream.v1.ElementaryStream.key]s multiplexed
    	// in this stream.
    	//
    	// - For `fmp4` container, must contain either one video or one audio stream.
    	// - For `ts` container, must contain exactly one audio stream and up to one
    	// video stream.
    	ElementaryStreams [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=elementary_streams,json=elementaryStreams,proto3" json:"elementary_streams,omitempty"`
    	// Segment settings for `fmp4` and `ts`.
    	SegmentSettings *SegmentSettings `protobuf:"bytes,5,opt,name=segment_settings,json=segmentSettings,proto3" json:"segment_settings,omitempty"`
    	// Identifier of the encryption configuration to use. If omitted, output
    	// will be unencrypted.
    	EncryptionId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=encryption_id,json=encryptionId,proto3" json:"encryption_id,omitempty"`
    	// contains filtered or unexported fields
    }

Multiplexing settings for output stream.

### func (*MuxStream) Descriptor 
    
    
    func (*MuxStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MuxStream.ProtoReflect.Descriptor instead.

### func (*MuxStream) GetContainer 
    
    
    func (x *MuxStream) GetContainer() [string](https://pkg.go.dev/builtin#string)

### func (*MuxStream) GetElementaryStreams 
    
    
    func (x *MuxStream) GetElementaryStreams() [][string](https://pkg.go.dev/builtin#string)

### func (*MuxStream) GetEncryptionId 
    
    
    func (x *MuxStream) GetEncryptionId() [string](https://pkg.go.dev/builtin#string)

### func (*MuxStream) GetKey 
    
    
    func (x *MuxStream) GetKey() [string](https://pkg.go.dev/builtin#string)

### func (*MuxStream) GetSegmentSettings 
    
    
    func (x *MuxStream) GetSegmentSettings() *SegmentSettings

### func (*MuxStream) ProtoMessage 
    
    
    func (*MuxStream) ProtoMessage()

### func (*MuxStream) ProtoReflect 
    
    
    func (x *MuxStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MuxStream) Reset 
    
    
    func (x *MuxStream) Reset()

### func (*MuxStream) String 
    
    
    func (x *MuxStream) String() [string](https://pkg.go.dev/builtin#string)

## NormalizedCoordinate
    
    
    type NormalizedCoordinate struct {
    
    	// Optional. Normalized x coordinate. Valid range is [0.0, 1.0]. Default is 0.
    	X [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=x,proto3" json:"x,omitempty"`
    	// Optional. Normalized y coordinate. Valid range is [0.0, 1.0]. Default is 0.
    	Y [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=y,proto3" json:"y,omitempty"`
    	// contains filtered or unexported fields
    }

2D normalized coordinates.

### func (*NormalizedCoordinate) Descriptor 
    
    
    func (*NormalizedCoordinate) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NormalizedCoordinate.ProtoReflect.Descriptor instead.

### func (*NormalizedCoordinate) GetX 
    
    
    func (x *NormalizedCoordinate) GetX() [float64](https://pkg.go.dev/builtin#float64)

### func (*NormalizedCoordinate) GetY 
    
    
    func (x *NormalizedCoordinate) GetY() [float64](https://pkg.go.dev/builtin#float64)

### func (*NormalizedCoordinate) ProtoMessage 
    
    
    func (*NormalizedCoordinate) ProtoMessage()

### func (*NormalizedCoordinate) ProtoReflect 
    
    
    func (x *NormalizedCoordinate) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NormalizedCoordinate) Reset 
    
    
    func (x *NormalizedCoordinate) Reset()

### func (*NormalizedCoordinate) String 
    
    
    func (x *NormalizedCoordinate) String() [string](https://pkg.go.dev/builtin#string)

## NormalizedResolution
    
    
    type NormalizedResolution struct {
    
    	// Optional. Normalized width. Valid range is [0.0, 1.0]. Default is 0.
    	W [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=w,proto3" json:"w,omitempty"`
    	// Optional. Normalized height. Valid range is [0.0, 1.0]. Default is 0.
    	H [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=h,proto3" json:"h,omitempty"`
    	// contains filtered or unexported fields
    }

Normalized resolution.

### func (*NormalizedResolution) Descriptor 
    
    
    func (*NormalizedResolution) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NormalizedResolution.ProtoReflect.Descriptor instead.

### func (*NormalizedResolution) GetH 
    
    
    func (x *NormalizedResolution) GetH() [float64](https://pkg.go.dev/builtin#float64)

### func (*NormalizedResolution) GetW 
    
    
    func (x *NormalizedResolution) GetW() [float64](https://pkg.go.dev/builtin#float64)

### func (*NormalizedResolution) ProtoMessage 
    
    
    func (*NormalizedResolution) ProtoMessage()

### func (*NormalizedResolution) ProtoReflect 
    
    
    func (x *NormalizedResolution) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NormalizedResolution) Reset 
    
    
    func (x *NormalizedResolution) Reset()

### func (*NormalizedResolution) String 
    
    
    func (x *NormalizedResolution) String() [string](https://pkg.go.dev/builtin#string)

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
    	// Output only. Identifies whether the user has requested cancellation
    	// of the operation. Operations that have successfully been cancelled
    	// have
    	// [google.longrunning.Operation.error][google.longrunning.Operation.error]
    	// value with a [google.rpc.Status.code][google.rpc.Status.code] of 1,
    	// corresponding to `Code.CANCELLED`.
    	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=requested_cancellation,json=requestedCancellation,proto3" json:"requested_cancellation,omitempty"`
    	// Output only. API version used to start the operation.
    	ApiVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=api_version,json=apiVersion,proto3" json:"api_version,omitempty"`
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

## Pool
    
    
    type Pool struct {
    
    	// The resource name of the pool, in the form of:
    	// `projects/{project}/locations/{location}/pools/{poolId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The update time.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-defined key/value metadata.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Network configuration for the pool.
    	NetworkConfig *Pool_NetworkConfig `protobuf:"bytes,5,opt,name=network_config,json=networkConfig,proto3" json:"network_config,omitempty"`
    	// contains filtered or unexported fields
    }

Pool resource defines the configuration of Live Stream pools for a specific location. Currently we support only one pool resource per project per location. After the creation of the first input, a default pool is created automatically at "projects/{project}/locations/{location}/pools/default".

### func (*Pool) Descriptor 
    
    
    func (*Pool) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Pool.ProtoReflect.Descriptor instead.

### func (*Pool) GetCreateTime 
    
    
    func (x *Pool) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Pool) GetLabels 
    
    
    func (x *Pool) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Pool) GetName 
    
    
    func (x *Pool) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Pool) GetNetworkConfig 
    
    
    func (x *Pool) GetNetworkConfig() *Pool_NetworkConfig

### func (*Pool) GetUpdateTime 
    
    
    func (x *Pool) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Pool) ProtoMessage 
    
    
    func (*Pool) ProtoMessage()

### func (*Pool) ProtoReflect 
    
    
    func (x *Pool) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Pool) Reset 
    
    
    func (x *Pool) Reset()

### func (*Pool) String 
    
    
    func (x *Pool) String() [string](https://pkg.go.dev/builtin#string)

## Pool_NetworkConfig
    
    
    type Pool_NetworkConfig struct {
    
    	// peered_network is the network resource URL of the network that is peered
    	// to the service provider network. Must be of the format
    	// projects/NETWORK_PROJECT_NUMBER/global/networks/NETWORK_NAME, where
    	// NETWORK_PROJECT_NUMBER is the project number of the Cloud project that
    	// holds your VPC network and NETWORK_NAME is the name of your VPC network.
    	// If peered_network is omitted or empty, the pool will use endpoints that
    	// are publicly available.
    	PeeredNetwork [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=peered_network,json=peeredNetwork,proto3" json:"peered_network,omitempty"`
    	// contains filtered or unexported fields
    }

Defines the network configuration for the pool.

### func (*Pool_NetworkConfig) Descriptor 
    
    
    func (*Pool_NetworkConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Pool_NetworkConfig.ProtoReflect.Descriptor instead.

### func (*Pool_NetworkConfig) GetPeeredNetwork 
    
    
    func (x *Pool_NetworkConfig) GetPeeredNetwork() [string](https://pkg.go.dev/builtin#string)

### func (*Pool_NetworkConfig) ProtoMessage 
    
    
    func (*Pool_NetworkConfig) ProtoMessage()

### func (*Pool_NetworkConfig) ProtoReflect 
    
    
    func (x *Pool_NetworkConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Pool_NetworkConfig) Reset 
    
    
    func (x *Pool_NetworkConfig) Reset()

### func (*Pool_NetworkConfig) String 
    
    
    func (x *Pool_NetworkConfig) String() [string](https://pkg.go.dev/builtin#string)

## PreprocessingConfig
    
    
    type PreprocessingConfig struct {
    
    	// Audio preprocessing configuration.
    	Audio *PreprocessingConfig_Audio `protobuf:"bytes,1,opt,name=audio,proto3" json:"audio,omitempty"`
    	// Specify the video cropping configuration.
    	Crop *PreprocessingConfig_Crop `protobuf:"bytes,2,opt,name=crop,proto3" json:"crop,omitempty"`
    	// Specify the video pad filter configuration.
    	Pad *PreprocessingConfig_Pad `protobuf:"bytes,3,opt,name=pad,proto3" json:"pad,omitempty"`
    	// contains filtered or unexported fields
    }

Preprocessing configurations.

### func (*PreprocessingConfig) Descriptor 
    
    
    func (*PreprocessingConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreprocessingConfig.ProtoReflect.Descriptor instead.

### func (*PreprocessingConfig) GetAudio 
    
    
    func (x *PreprocessingConfig) GetAudio() *PreprocessingConfig_Audio

### func (*PreprocessingConfig) GetCrop 
    
    
    func (x *PreprocessingConfig) GetCrop() *PreprocessingConfig_Crop

### func (*PreprocessingConfig) GetPad 
    
    
    func (x *PreprocessingConfig) GetPad() *PreprocessingConfig_Pad

### func (*PreprocessingConfig) ProtoMessage 
    
    
    func (*PreprocessingConfig) ProtoMessage()

### func (*PreprocessingConfig) ProtoReflect 
    
    
    func (x *PreprocessingConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreprocessingConfig) Reset 
    
    
    func (x *PreprocessingConfig) Reset()

### func (*PreprocessingConfig) String 
    
    
    func (x *PreprocessingConfig) String() [string](https://pkg.go.dev/builtin#string)

## PreprocessingConfig_Audio
    
    
    type PreprocessingConfig_Audio struct {
    
    	// Specify audio loudness normalization in loudness units relative to full
    	// scale (LUFS). Enter a value between -24 and 0 according to the following:
    	//
    	// - -24 is the Advanced Television Systems Committee (ATSC A/85)
    	// - -23 is the EU R128 broadcast standard
    	// - -19 is the prior standard for online mono audio
    	// - -18 is the ReplayGain standard
    	// - -16 is the prior standard for stereo audio
    	// - -14 is the new online audio standard recommended by Spotify, as well as
    	// Amazon Echo
    	// - 0 disables normalization. The default is 0.
    	Lufs [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=lufs,proto3" json:"lufs,omitempty"`
    	// contains filtered or unexported fields
    }

Audio preprocessing configuration.

### func (*PreprocessingConfig_Audio) Descriptor 
    
    
    func (*PreprocessingConfig_Audio) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreprocessingConfig_Audio.ProtoReflect.Descriptor instead.

### func (*PreprocessingConfig_Audio) GetLufs 
    
    
    func (x *PreprocessingConfig_Audio) GetLufs() [float64](https://pkg.go.dev/builtin#float64)

### func (*PreprocessingConfig_Audio) ProtoMessage 
    
    
    func (*PreprocessingConfig_Audio) ProtoMessage()

### func (*PreprocessingConfig_Audio) ProtoReflect 
    
    
    func (x *PreprocessingConfig_Audio) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreprocessingConfig_Audio) Reset 
    
    
    func (x *PreprocessingConfig_Audio) Reset()

### func (*PreprocessingConfig_Audio) String 
    
    
    func (x *PreprocessingConfig_Audio) String() [string](https://pkg.go.dev/builtin#string)

## PreprocessingConfig_Crop
    
    
    type PreprocessingConfig_Crop struct {
    
    	// The number of pixels to crop from the top. The default is 0.
    	TopPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=top_pixels,json=topPixels,proto3" json:"top_pixels,omitempty"`
    	// The number of pixels to crop from the bottom. The default is 0.
    	BottomPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=bottom_pixels,json=bottomPixels,proto3" json:"bottom_pixels,omitempty"`
    	// The number of pixels to crop from the left. The default is 0.
    	LeftPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=left_pixels,json=leftPixels,proto3" json:"left_pixels,omitempty"`
    	// The number of pixels to crop from the right. The default is 0.
    	RightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=right_pixels,json=rightPixels,proto3" json:"right_pixels,omitempty"`
    	// contains filtered or unexported fields
    }

Video cropping configuration for the input video. The cropped input video is scaled to match the output resolution.

### func (*PreprocessingConfig_Crop) Descriptor 
    
    
    func (*PreprocessingConfig_Crop) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreprocessingConfig_Crop.ProtoReflect.Descriptor instead.

### func (*PreprocessingConfig_Crop) GetBottomPixels 
    
    
    func (x *PreprocessingConfig_Crop) GetBottomPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Crop) GetLeftPixels 
    
    
    func (x *PreprocessingConfig_Crop) GetLeftPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Crop) GetRightPixels 
    
    
    func (x *PreprocessingConfig_Crop) GetRightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Crop) GetTopPixels 
    
    
    func (x *PreprocessingConfig_Crop) GetTopPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Crop) ProtoMessage 
    
    
    func (*PreprocessingConfig_Crop) ProtoMessage()

### func (*PreprocessingConfig_Crop) ProtoReflect 
    
    
    func (x *PreprocessingConfig_Crop) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreprocessingConfig_Crop) Reset 
    
    
    func (x *PreprocessingConfig_Crop) Reset()

### func (*PreprocessingConfig_Crop) String 
    
    
    func (x *PreprocessingConfig_Crop) String() [string](https://pkg.go.dev/builtin#string)

## PreprocessingConfig_Pad
    
    
    type PreprocessingConfig_Pad struct {
    
    	// The number of pixels to add to the top. The default is 0.
    	TopPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=top_pixels,json=topPixels,proto3" json:"top_pixels,omitempty"`
    	// The number of pixels to add to the bottom. The default is 0.
    	BottomPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=bottom_pixels,json=bottomPixels,proto3" json:"bottom_pixels,omitempty"`
    	// The number of pixels to add to the left. The default is 0.
    	LeftPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=left_pixels,json=leftPixels,proto3" json:"left_pixels,omitempty"`
    	// The number of pixels to add to the right. The default is 0.
    	RightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=right_pixels,json=rightPixels,proto3" json:"right_pixels,omitempty"`
    	// contains filtered or unexported fields
    }

Pad filter configuration for the input video. The padded input video is scaled after padding with black to match the output resolution.

### func (*PreprocessingConfig_Pad) Descriptor 
    
    
    func (*PreprocessingConfig_Pad) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreprocessingConfig_Pad.ProtoReflect.Descriptor instead.

### func (*PreprocessingConfig_Pad) GetBottomPixels 
    
    
    func (x *PreprocessingConfig_Pad) GetBottomPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Pad) GetLeftPixels 
    
    
    func (x *PreprocessingConfig_Pad) GetLeftPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Pad) GetRightPixels 
    
    
    func (x *PreprocessingConfig_Pad) GetRightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Pad) GetTopPixels 
    
    
    func (x *PreprocessingConfig_Pad) GetTopPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*PreprocessingConfig_Pad) ProtoMessage 
    
    
    func (*PreprocessingConfig_Pad) ProtoMessage()

### func (*PreprocessingConfig_Pad) ProtoReflect 
    
    
    func (x *PreprocessingConfig_Pad) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreprocessingConfig_Pad) Reset 
    
    
    func (x *PreprocessingConfig_Pad) Reset()

### func (*PreprocessingConfig_Pad) String 
    
    
    func (x *PreprocessingConfig_Pad) String() [string](https://pkg.go.dev/builtin#string)

## PreviewInputRequest
    
    
    type PreviewInputRequest struct {
    
    	// Required. The name of the input resource, in the form of:
    	// `projects/{project}/locations/{location}/inputs/{inputId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.PreviewInput"

### func (*PreviewInputRequest) Descriptor 
    
    
    func (*PreviewInputRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreviewInputRequest.ProtoReflect.Descriptor instead.

### func (*PreviewInputRequest) GetName 
    
    
    func (x *PreviewInputRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*PreviewInputRequest) ProtoMessage 
    
    
    func (*PreviewInputRequest) ProtoMessage()

### func (*PreviewInputRequest) ProtoReflect 
    
    
    func (x *PreviewInputRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreviewInputRequest) Reset 
    
    
    func (x *PreviewInputRequest) Reset()

### func (*PreviewInputRequest) String 
    
    
    func (x *PreviewInputRequest) String() [string](https://pkg.go.dev/builtin#string)

## PreviewInputResponse
    
    
    type PreviewInputResponse struct {
    
    	// URI to display the preview content.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// A bearer token used to authenticate connections that display the preview
    	// content. The token expires after one hour. For HTTP connections, this token
    	// should be included as a bearer token inside the Authorization header.
    	BearerToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=bearer_token,json=bearerToken,proto3" json:"bearer_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for "LivestreamService.PreviewInput"

### func (*PreviewInputResponse) Descriptor 
    
    
    func (*PreviewInputResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreviewInputResponse.ProtoReflect.Descriptor instead.

### func (*PreviewInputResponse) GetBearerToken 
    
    
    func (x *PreviewInputResponse) GetBearerToken() [string](https://pkg.go.dev/builtin#string)

### func (*PreviewInputResponse) GetUri 
    
    
    func (x *PreviewInputResponse) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*PreviewInputResponse) ProtoMessage 
    
    
    func (*PreviewInputResponse) ProtoMessage()

### func (*PreviewInputResponse) ProtoReflect 
    
    
    func (x *PreviewInputResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreviewInputResponse) Reset 
    
    
    func (x *PreviewInputResponse) Reset()

### func (*PreviewInputResponse) String 
    
    
    func (x *PreviewInputResponse) String() [string](https://pkg.go.dev/builtin#string)

## RetentionConfig
    
    
    type RetentionConfig struct {
    
    	// The minimum duration for which the output files from the channel will
    	// remain in the output bucket. After this duration, output files are
    	// deleted asynchronously.
    	//
    	// When the channel is deleted, all output files are deleted from the output
    	// bucket asynchronously.
    	//
    	// If omitted or set to zero, output files will remain in the output bucket
    	// based on
    	// [Manifest.segment_keep_duration][google.cloud.video.livestream.v1.Manifest.segment_keep_duration],
    	// which defaults to 60s.
    	//
    	// If both retention_window_duration and
    	// [Manifest.segment_keep_duration][google.cloud.video.livestream.v1.Manifest.segment_keep_duration]
    	// are set, retention_window_duration is used and
    	// [Manifest.segment_keep_duration][google.cloud.video.livestream.v1.Manifest.segment_keep_duration]
    	// is ignored.
    	RetentionWindowDuration *durationpb.Duration `protobuf:"bytes,1,opt,name=retention_window_duration,json=retentionWindowDuration,proto3" json:"retention_window_duration,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for retention of output files.

### func (*RetentionConfig) Descriptor 
    
    
    func (*RetentionConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RetentionConfig.ProtoReflect.Descriptor instead.

### func (*RetentionConfig) GetRetentionWindowDuration 
    
    
    func (x *RetentionConfig) GetRetentionWindowDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*RetentionConfig) ProtoMessage 
    
    
    func (*RetentionConfig) ProtoMessage()

### func (*RetentionConfig) ProtoReflect 
    
    
    func (x *RetentionConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RetentionConfig) Reset 
    
    
    func (x *RetentionConfig) Reset()

### func (*RetentionConfig) String 
    
    
    func (x *RetentionConfig) String() [string](https://pkg.go.dev/builtin#string)

## RtmpPushOutputEndpoint
    
    
    type RtmpPushOutputEndpoint struct {
    
    	// Required. The full URI of the remote RTMP server. For example:
    	// `rtmp://192.168.123.321/live/my-stream` or `rtmp://somedomain.com/someapp`.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Required. Stream key for RTMP protocol.
    	StreamKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=stream_key,json=streamKey,proto3" json:"stream_key,omitempty"`
    	// contains filtered or unexported fields
    }

Configurations for an output endpoint using RTMP_PUSH as the streaming protocol.

### func (*RtmpPushOutputEndpoint) Descriptor 
    
    
    func (*RtmpPushOutputEndpoint) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RtmpPushOutputEndpoint.ProtoReflect.Descriptor instead.

### func (*RtmpPushOutputEndpoint) GetStreamKey 
    
    
    func (x *RtmpPushOutputEndpoint) GetStreamKey() [string](https://pkg.go.dev/builtin#string)

### func (*RtmpPushOutputEndpoint) GetUri 
    
    
    func (x *RtmpPushOutputEndpoint) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*RtmpPushOutputEndpoint) ProtoMessage 
    
    
    func (*RtmpPushOutputEndpoint) ProtoMessage()

### func (*RtmpPushOutputEndpoint) ProtoReflect 
    
    
    func (x *RtmpPushOutputEndpoint) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RtmpPushOutputEndpoint) Reset 
    
    
    func (x *RtmpPushOutputEndpoint) Reset()

### func (*RtmpPushOutputEndpoint) String 
    
    
    func (x *RtmpPushOutputEndpoint) String() [string](https://pkg.go.dev/builtin#string)

## SegmentSettings
    
    
    type SegmentSettings struct {
    
    	// Duration of the segments in seconds. The default is `6s`. Note that
    	// `segmentDuration` must be greater than or equal to
    	// [gop_duration][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.gop_duration],
    	// and `segmentDuration` must be divisible by
    	// [gop_duration][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.gop_duration].
    	// Valid range is [2s, 20s].
    	//
    	// All [mux_streams][google.cloud.video.livestream.v1.Manifest.mux_streams] in
    	// the same manifest must have the same segment duration.
    	SegmentDuration *durationpb.Duration `protobuf:"bytes,1,opt,name=segment_duration,json=segmentDuration,proto3" json:"segment_duration,omitempty"`
    	// contains filtered or unexported fields
    }

Segment settings for `fmp4` and `ts`.

### func (*SegmentSettings) Descriptor 
    
    
    func (*SegmentSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SegmentSettings.ProtoReflect.Descriptor instead.

### func (*SegmentSettings) GetSegmentDuration 
    
    
    func (x *SegmentSettings) GetSegmentDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*SegmentSettings) ProtoMessage 
    
    
    func (*SegmentSettings) ProtoMessage()

### func (*SegmentSettings) ProtoReflect 
    
    
    func (x *SegmentSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SegmentSettings) Reset 
    
    
    func (x *SegmentSettings) Reset()

### func (*SegmentSettings) String 
    
    
    func (x *SegmentSettings) String() [string](https://pkg.go.dev/builtin#string)

## SpriteSheet
    
    
    type SpriteSheet struct {
    
    	// Format type. The default is `jpeg`.
    	//
    	// Supported formats:
    	//
    	// - `jpeg`
    	Format [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=format,proto3" json:"format,omitempty"`
    	// Required. File name prefix for the generated sprite sheets. If multiple
    	// sprite sheets are added to the channel, each must have a unique file
    	// prefix.
    	// Each sprite sheet has an incremental 10-digit zero-padded suffix starting
    	// from 0 before the extension, such as `sprite_sheet0000000123.jpeg`.
    	FilePrefix [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=file_prefix,json=filePrefix,proto3" json:"file_prefix,omitempty"`
    	// Required. The width of the sprite in pixels. Must be an even integer.
    	SpriteWidthPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=sprite_width_pixels,json=spriteWidthPixels,proto3" json:"sprite_width_pixels,omitempty"`
    	// Required. The height of the sprite in pixels. Must be an even integer.
    	SpriteHeightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=sprite_height_pixels,json=spriteHeightPixels,proto3" json:"sprite_height_pixels,omitempty"`
    	// The maximum number of sprites per row in a sprite sheet. Valid range is
    	// [1, 10] and the default value is 1.
    	ColumnCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=column_count,json=columnCount,proto3" json:"column_count,omitempty"`
    	// The maximum number of rows per sprite sheet. When the sprite sheet is full,
    	// a new sprite sheet is created. Valid range is [1, 10] and the default value
    	// is 1.
    	RowCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=row_count,json=rowCount,proto3" json:"row_count,omitempty"`
    	// Create sprites at regular intervals. Valid range is [1 second, 1 hour] and
    	// the default value is `10s`.
    	Interval *durationpb.Duration `protobuf:"bytes,7,opt,name=interval,proto3" json:"interval,omitempty"`
    	// The quality of the generated sprite sheet. Enter a value between 1
    	// and 100, where 1 is the lowest quality and 100 is the highest quality.
    	// The default is 100. A high quality value corresponds to a low image data
    	// compression ratio.
    	Quality [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,8,opt,name=quality,proto3" json:"quality,omitempty"`
    	// contains filtered or unexported fields
    }

Sprite sheet configuration.

### func (*SpriteSheet) Descriptor 
    
    
    func (*SpriteSheet) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SpriteSheet.ProtoReflect.Descriptor instead.

### func (*SpriteSheet) GetColumnCount 
    
    
    func (x *SpriteSheet) GetColumnCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*SpriteSheet) GetFilePrefix 
    
    
    func (x *SpriteSheet) GetFilePrefix() [string](https://pkg.go.dev/builtin#string)

### func (*SpriteSheet) GetFormat 
    
    
    func (x *SpriteSheet) GetFormat() [string](https://pkg.go.dev/builtin#string)

### func (*SpriteSheet) GetInterval 
    
    
    func (x *SpriteSheet) GetInterval() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*SpriteSheet) GetQuality 
    
    
    func (x *SpriteSheet) GetQuality() [int32](https://pkg.go.dev/builtin#int32)

### func (*SpriteSheet) GetRowCount 
    
    
    func (x *SpriteSheet) GetRowCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*SpriteSheet) GetSpriteHeightPixels 
    
    
    func (x *SpriteSheet) GetSpriteHeightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*SpriteSheet) GetSpriteWidthPixels 
    
    
    func (x *SpriteSheet) GetSpriteWidthPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*SpriteSheet) ProtoMessage 
    
    
    func (*SpriteSheet) ProtoMessage()

### func (*SpriteSheet) ProtoReflect 
    
    
    func (x *SpriteSheet) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SpriteSheet) Reset 
    
    
    func (x *SpriteSheet) Reset()

### func (*SpriteSheet) String 
    
    
    func (x *SpriteSheet) String() [string](https://pkg.go.dev/builtin#string)

## SrtPushOutputEndpoint
    
    
    type SrtPushOutputEndpoint struct {
    
    	// Required. The full URI of the remote SRT server.
    	Uri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
    	// Defines where SRT encryption passphrase are stored.
    	//
    	// Types that are valid to be assigned to PassphraseSource:
    	//
    	//	*SrtPushOutputEndpoint_PassphraseSecretVersion
    	PassphraseSource isSrtPushOutputEndpoint_PassphraseSource `protobuf_oneof:"passphrase_source"`
    	// contains filtered or unexported fields
    }

Configurations for an output endpoint using SRT_PUSH as the streaming protocol.

### func (*SrtPushOutputEndpoint) Descriptor 
    
    
    func (*SrtPushOutputEndpoint) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SrtPushOutputEndpoint.ProtoReflect.Descriptor instead.

### func (*SrtPushOutputEndpoint) GetPassphraseSecretVersion 
    
    
    func (x *SrtPushOutputEndpoint) GetPassphraseSecretVersion() [string](https://pkg.go.dev/builtin#string)

### func (*SrtPushOutputEndpoint) GetPassphraseSource 
    
    
    func (x *SrtPushOutputEndpoint) GetPassphraseSource() isSrtPushOutputEndpoint_PassphraseSource

### func (*SrtPushOutputEndpoint) GetUri 
    
    
    func (x *SrtPushOutputEndpoint) GetUri() [string](https://pkg.go.dev/builtin#string)

### func (*SrtPushOutputEndpoint) ProtoMessage 
    
    
    func (*SrtPushOutputEndpoint) ProtoMessage()

### func (*SrtPushOutputEndpoint) ProtoReflect 
    
    
    func (x *SrtPushOutputEndpoint) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SrtPushOutputEndpoint) Reset 
    
    
    func (x *SrtPushOutputEndpoint) Reset()

### func (*SrtPushOutputEndpoint) String 
    
    
    func (x *SrtPushOutputEndpoint) String() [string](https://pkg.go.dev/builtin#string)

## SrtPushOutputEndpoint_PassphraseSecretVersion
    
    
    type SrtPushOutputEndpoint_PassphraseSecretVersion struct {
    	// The name of the Secret Version containing the SRT encryption passphrase,
    	// which is stored in Google Secret Manager. It should be in the format of
    	// `projects/{project}/secrets/{secret_id}/versions/{version_number}`.
    	PassphraseSecretVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=passphrase_secret_version,json=passphraseSecretVersion,proto3,oneof"`
    }

## StartChannelRequest
    
    
    type StartChannelRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.StartChannel".

### func (*StartChannelRequest) Descriptor 
    
    
    func (*StartChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use StartChannelRequest.ProtoReflect.Descriptor instead.

### func (*StartChannelRequest) GetName 
    
    
    func (x *StartChannelRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*StartChannelRequest) GetRequestId 
    
    
    func (x *StartChannelRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*StartChannelRequest) ProtoMessage 
    
    
    func (*StartChannelRequest) ProtoMessage()

### func (*StartChannelRequest) ProtoReflect 
    
    
    func (x *StartChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*StartChannelRequest) Reset 
    
    
    func (x *StartChannelRequest) Reset()

### func (*StartChannelRequest) String 
    
    
    func (x *StartChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## StartDistributionRequest
    
    
    type StartDistributionRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A list of keys to identify the distribution configuration in the
    	// channel resource. If left empty, all the distributions in the channel
    	// specification will be started.
    	DistributionKeys [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=distribution_keys,json=distributionKeys,proto3" json:"distribution_keys,omitempty"`
    	// Optional. A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.StartDistribution".

### func (*StartDistributionRequest) Descriptor 
    
    
    func (*StartDistributionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use StartDistributionRequest.ProtoReflect.Descriptor instead.

### func (*StartDistributionRequest) GetDistributionKeys 
    
    
    func (x *StartDistributionRequest) GetDistributionKeys() [][string](https://pkg.go.dev/builtin#string)

### func (*StartDistributionRequest) GetName 
    
    
    func (x *StartDistributionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*StartDistributionRequest) GetRequestId 
    
    
    func (x *StartDistributionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*StartDistributionRequest) ProtoMessage 
    
    
    func (*StartDistributionRequest) ProtoMessage()

### func (*StartDistributionRequest) ProtoReflect 
    
    
    func (x *StartDistributionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*StartDistributionRequest) Reset 
    
    
    func (x *StartDistributionRequest) Reset()

### func (*StartDistributionRequest) String 
    
    
    func (x *StartDistributionRequest) String() [string](https://pkg.go.dev/builtin#string)

## StaticOverlay
    
    
    type StaticOverlay struct {
    
    	// Required. Asset to use for the overlaid image.
    	// The asset must be represented in the form of:
    	// `projects/{project}/locations/{location}/assets/{assetId}`.
    	// The asset's resource type must be image.
    	Asset [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=asset,proto3" json:"asset,omitempty"`
    	// Optional. Normalized image resolution, based on output video resolution.
    	// Valid values are [0.0, 1.0]. To respect the original image aspect ratio,
    	// set either `w` or `h` to 0. To use the original image resolution, set both
    	// `w` and `h` to 0. The default is {0, 0}.
    	Resolution *NormalizedResolution `protobuf:"bytes,2,opt,name=resolution,proto3" json:"resolution,omitempty"`
    	// Optional. Position of the image in terms of normalized coordinates of the
    	// upper-left corner of the image, based on output video resolution. For
    	// example, use the x and y coordinates {0, 0} to position the top-left corner
    	// of the overlay animation in the top-left corner of the output video.
    	Position *NormalizedCoordinate `protobuf:"bytes,3,opt,name=position,proto3" json:"position,omitempty"`
    	// Optional. Target image opacity. Valid values are from `1.0` (solid,
    	// default) to `0.0` (transparent), exclusive. Set this to a value greater
    	// than `0.0`.
    	Opacity [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,4,opt,name=opacity,proto3" json:"opacity,omitempty"`
    	// contains filtered or unexported fields
    }

Configuration for the static overlay.

### func (*StaticOverlay) Descriptor 
    
    
    func (*StaticOverlay) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use StaticOverlay.ProtoReflect.Descriptor instead.

### func (*StaticOverlay) GetAsset 
    
    
    func (x *StaticOverlay) GetAsset() [string](https://pkg.go.dev/builtin#string)

### func (*StaticOverlay) GetOpacity 
    
    
    func (x *StaticOverlay) GetOpacity() [float64](https://pkg.go.dev/builtin#float64)

### func (*StaticOverlay) GetPosition 
    
    
    func (x *StaticOverlay) GetPosition() *NormalizedCoordinate

### func (*StaticOverlay) GetResolution 
    
    
    func (x *StaticOverlay) GetResolution() *NormalizedResolution

### func (*StaticOverlay) ProtoMessage 
    
    
    func (*StaticOverlay) ProtoMessage()

### func (*StaticOverlay) ProtoReflect 
    
    
    func (x *StaticOverlay) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*StaticOverlay) Reset 
    
    
    func (x *StaticOverlay) Reset()

### func (*StaticOverlay) String 
    
    
    func (x *StaticOverlay) String() [string](https://pkg.go.dev/builtin#string)

## StopChannelRequest
    
    
    type StopChannelRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.StopChannel".

### func (*StopChannelRequest) Descriptor 
    
    
    func (*StopChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use StopChannelRequest.ProtoReflect.Descriptor instead.

### func (*StopChannelRequest) GetName 
    
    
    func (x *StopChannelRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*StopChannelRequest) GetRequestId 
    
    
    func (x *StopChannelRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*StopChannelRequest) ProtoMessage 
    
    
    func (*StopChannelRequest) ProtoMessage()

### func (*StopChannelRequest) ProtoReflect 
    
    
    func (x *StopChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*StopChannelRequest) Reset 
    
    
    func (x *StopChannelRequest) Reset()

### func (*StopChannelRequest) String 
    
    
    func (x *StopChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## StopDistributionRequest
    
    
    type StopDistributionRequest struct {
    
    	// Required. The name of the channel resource, in the form of:
    	// `projects/{project}/locations/{location}/channels/{channelId}`.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. A list of key to identify the distribution configuration in the
    	// channel resource. If left empty, all the distributions in the channel
    	// specification will be stopped.
    	DistributionKeys [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=distribution_keys,json=distributionKeys,proto3" json:"distribution_keys,omitempty"`
    	// Optional. A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.StopDistribution".

### func (*StopDistributionRequest) Descriptor 
    
    
    func (*StopDistributionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use StopDistributionRequest.ProtoReflect.Descriptor instead.

### func (*StopDistributionRequest) GetDistributionKeys 
    
    
    func (x *StopDistributionRequest) GetDistributionKeys() [][string](https://pkg.go.dev/builtin#string)

### func (*StopDistributionRequest) GetName 
    
    
    func (x *StopDistributionRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*StopDistributionRequest) GetRequestId 
    
    
    func (x *StopDistributionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*StopDistributionRequest) ProtoMessage 
    
    
    func (*StopDistributionRequest) ProtoMessage()

### func (*StopDistributionRequest) ProtoReflect 
    
    
    func (x *StopDistributionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*StopDistributionRequest) Reset 
    
    
    func (x *StopDistributionRequest) Reset()

### func (*StopDistributionRequest) String 
    
    
    func (x *StopDistributionRequest) String() [string](https://pkg.go.dev/builtin#string)

## TextStream
    
    
    type TextStream struct {
    
    	// Required. The codec for this text stream.
    	//
    	// Supported text codecs:
    	//
    	// - `cea608`
    	// - `cea708`
    	// - `webvtt`
    	Codec [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=codec,proto3" json:"codec,omitempty"`
    	// Optional. The BCP-47 language code, such as `en-US` or `sr-Latn`. For more
    	// information, see
    	// https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    	LanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=language_code,json=languageCode,proto3" json:"language_code,omitempty"`
    	// Optional. The name for this particular text stream that will be added to
    	// the HLS/DASH manifest.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Optional. The channel of the closed caption in the output stream.
    	// This field should only be set when textstream is used for partner
    	// distribution.
    	// Must be one of `CC1`, `CC2`, `CC3`, and `CC4`, if the
    	// [codec][google.cloud.video.livestream.v1.TextStream.codec] is `cea608`;
    	// Must be one between `SERVICE1` and `SERVICE63`, if the
    	// [codec][google.cloud.video.livestream.v1.TextStream.codec] is `cea708`.
    	OutputCeaChannel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=output_cea_channel,json=outputCeaChannel,proto3" json:"output_cea_channel,omitempty"`
    	// Optional. The mapping for the input streams and text tracks.
    	Mapping []*TextStream_TextMapping `protobuf:"bytes,3,rep,name=mapping,proto3" json:"mapping,omitempty"`
    	// contains filtered or unexported fields
    }

Encoding of a text stream. For example, closed captions or subtitles.

### func (*TextStream) Descriptor 
    
    
    func (*TextStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TextStream.ProtoReflect.Descriptor instead.

### func (*TextStream) GetCodec 
    
    
    func (x *TextStream) GetCodec() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream) GetDisplayName 
    
    
    func (x *TextStream) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream) GetLanguageCode 
    
    
    func (x *TextStream) GetLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream) GetMapping 
    
    
    func (x *TextStream) GetMapping() []*TextStream_TextMapping

### func (*TextStream) GetOutputCeaChannel 
    
    
    func (x *TextStream) GetOutputCeaChannel() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream) ProtoMessage 
    
    
    func (*TextStream) ProtoMessage()

### func (*TextStream) ProtoReflect 
    
    
    func (x *TextStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TextStream) Reset 
    
    
    func (x *TextStream) Reset()

### func (*TextStream) String 
    
    
    func (x *TextStream) String() [string](https://pkg.go.dev/builtin#string)

## TextStream_TextMapping
    
    
    type TextStream_TextMapping struct {
    
    	// Optional. The `Channel`
    	// [InputAttachment.key][google.cloud.video.livestream.v1.InputAttachment.key]
    	// that identifies the input that this text mapping applies to.
    	InputKey [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=input_key,json=inputKey,proto3" json:"input_key,omitempty"`
    	// Optional. The zero-based index of the track in the input stream.
    	InputTrack [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=input_track,json=inputTrack,proto3" json:"input_track,omitempty"`
    	// Optional. The channel of the closed caption in the input stream.
    	// If this field is set, the output
    	// [codec][google.cloud.video.livestream.v1.TextStream.codec] must be
    	// `webvtt`. Must be one of `CC1`, `CC2`, `CC3`, and `CC4`, if the codec of
    	// the input closed caption is `cea608`; Must be one between `SERVICE1` and
    	// `SERVICE64`, if the codec of the input closed caption is `cea708`.
    	InputCeaChannel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=input_cea_channel,json=inputCeaChannel,proto3" json:"input_cea_channel,omitempty"`
    	// Optional. The BCP-47 source language code, such as `en-US` or `sr-Latn`.
    	// If differ from the textStream's language code, enable translation. For
    	// more information on BCP-47 language codes, see
    	// https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    	FromLanguageCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=from_language_code,json=fromLanguageCode,proto3" json:"from_language_code,omitempty"`
    	// contains filtered or unexported fields
    }

The mapping for the input streams and text tracks.

### func (*TextStream_TextMapping) Descriptor 
    
    
    func (*TextStream_TextMapping) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TextStream_TextMapping.ProtoReflect.Descriptor instead.

### func (*TextStream_TextMapping) GetFromLanguageCode 
    
    
    func (x *TextStream_TextMapping) GetFromLanguageCode() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream_TextMapping) GetInputCeaChannel 
    
    
    func (x *TextStream_TextMapping) GetInputCeaChannel() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream_TextMapping) GetInputKey 
    
    
    func (x *TextStream_TextMapping) GetInputKey() [string](https://pkg.go.dev/builtin#string)

### func (*TextStream_TextMapping) GetInputTrack 
    
    
    func (x *TextStream_TextMapping) GetInputTrack() [int32](https://pkg.go.dev/builtin#int32)

### func (*TextStream_TextMapping) ProtoMessage 
    
    
    func (*TextStream_TextMapping) ProtoMessage()

### func (*TextStream_TextMapping) ProtoReflect 
    
    
    func (x *TextStream_TextMapping) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TextStream_TextMapping) Reset 
    
    
    func (x *TextStream_TextMapping) Reset()

### func (*TextStream_TextMapping) String 
    
    
    func (x *TextStream_TextMapping) String() [string](https://pkg.go.dev/builtin#string)

## TimeInterval
    
    
    type TimeInterval struct {
    
    	// Optional. The start time of the interval.
    	StartTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
    	// Optional. The end time of the interval.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// contains filtered or unexported fields
    }

TimeInterval represents a time interval.

### func (*TimeInterval) Descriptor 
    
    
    func (*TimeInterval) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TimeInterval.ProtoReflect.Descriptor instead.

### func (*TimeInterval) GetEndTime 
    
    
    func (x *TimeInterval) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TimeInterval) GetStartTime 
    
    
    func (x *TimeInterval) GetStartTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*TimeInterval) ProtoMessage 
    
    
    func (*TimeInterval) ProtoMessage()

### func (*TimeInterval) ProtoReflect 
    
    
    func (x *TimeInterval) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TimeInterval) Reset 
    
    
    func (x *TimeInterval) Reset()

### func (*TimeInterval) String 
    
    
    func (x *TimeInterval) String() [string](https://pkg.go.dev/builtin#string)

## TimecodeConfig
    
    
    type TimecodeConfig struct {
    
    	// The source of the timecode that will later be used in outputs/manifests.
    	// It determines the initial timecode/timestamp (first frame) of output
    	// streams.
    	Source TimecodeConfig_TimecodeSource `protobuf:"varint,1,opt,name=source,proto3,enum=google.cloud.video.livestream.v1.TimecodeConfig_TimecodeSource" json:"source,omitempty"`
    	// For EMBEDDED_TIMECODE source only.
    	// Used to interpret the embedded timecode (which contains only the time part
    	// and no date). We assume all inputs are live.
    	//
    	// Types that are valid to be assigned to TimeOffset:
    	//
    	//	*TimecodeConfig_UtcOffset
    	//	*TimecodeConfig_TimeZone
    	TimeOffset isTimecodeConfig_TimeOffset `protobuf_oneof:"time_offset"`
    	// contains filtered or unexported fields
    }

Timecode configuration.

### func (*TimecodeConfig) Descriptor 
    
    
    func (*TimecodeConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TimecodeConfig.ProtoReflect.Descriptor instead.

### func (*TimecodeConfig) GetSource 
    
    
    func (x *TimecodeConfig) GetSource() TimecodeConfig_TimecodeSource

### func (*TimecodeConfig) GetTimeOffset 
    
    
    func (x *TimecodeConfig) GetTimeOffset() isTimecodeConfig_TimeOffset

### func (*TimecodeConfig) GetTimeZone 
    
    
    func (x *TimecodeConfig) GetTimeZone() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[TimeZone](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#TimeZone)

### func (*TimecodeConfig) GetUtcOffset 
    
    
    func (x *TimecodeConfig) GetUtcOffset() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*TimecodeConfig) ProtoMessage 
    
    
    func (*TimecodeConfig) ProtoMessage()

### func (*TimecodeConfig) ProtoReflect 
    
    
    func (x *TimecodeConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*TimecodeConfig) Reset 
    
    
    func (x *TimecodeConfig) Reset()

### func (*TimecodeConfig) String 
    
    
    func (x *TimecodeConfig) String() [string](https://pkg.go.dev/builtin#string)

## TimecodeConfig_TimeZone
    
    
    type TimecodeConfig_TimeZone struct {
    	// Time zone e.g. "America/Los_Angeles".
    	TimeZone *datetime.TimeZone `protobuf:"bytes,3,opt,name=time_zone,json=timeZone,proto3,oneof"`
    }

## TimecodeConfig_TimecodeSource
    
    
    type TimecodeConfig_TimecodeSource [int32](https://pkg.go.dev/builtin#int32)

The source of timecode.

### TimecodeConfig_TIMECODE_SOURCE_UNSPECIFIED, TimecodeConfig_MEDIA_TIMESTAMP, TimecodeConfig_EMBEDDED_TIMECODE
    
    
    const (
    	// The timecode source is not specified.
    	TimecodeConfig_TIMECODE_SOURCE_UNSPECIFIED TimecodeConfig_TimecodeSource = 0
    	// Use input media timestamp.
    	TimecodeConfig_MEDIA_TIMESTAMP TimecodeConfig_TimecodeSource = 1
    	// Use input embedded timecode e.g. picture timing SEI message.
    	TimecodeConfig_EMBEDDED_TIMECODE TimecodeConfig_TimecodeSource = 2
    )

### func (TimecodeConfig_TimecodeSource) Descriptor 
    
    
    func (TimecodeConfig_TimecodeSource) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TimecodeConfig_TimecodeSource) Enum 
    
    
    func (x TimecodeConfig_TimecodeSource) Enum() *TimecodeConfig_TimecodeSource

### func (TimecodeConfig_TimecodeSource) EnumDescriptor 
    
    
    func (TimecodeConfig_TimecodeSource) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TimecodeConfig_TimecodeSource.Descriptor instead.

### func (TimecodeConfig_TimecodeSource) Number 
    
    
    func (x TimecodeConfig_TimecodeSource) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TimecodeConfig_TimecodeSource) String 
    
    
    func (x TimecodeConfig_TimecodeSource) String() [string](https://pkg.go.dev/builtin#string)

### func (TimecodeConfig_TimecodeSource) Type 
    
    
    func (TimecodeConfig_TimecodeSource) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## TimecodeConfig_UtcOffset
    
    
    type TimecodeConfig_UtcOffset struct {
    	// UTC offset. Must be whole seconds, between -18 hours and +18 hours.
    	UtcOffset *durationpb.Duration `protobuf:"bytes,2,opt,name=utc_offset,json=utcOffset,proto3,oneof"`
    }

## UnimplementedLivestreamServiceServer
    
    
    type UnimplementedLivestreamServiceServer struct {
    }

UnimplementedLivestreamServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedLivestreamServiceServer) CreateAsset 
    
    
    func (UnimplementedLivestreamServiceServer) CreateAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateAssetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) CreateChannel 
    
    
    func (UnimplementedLivestreamServiceServer) CreateChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateChannelRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) CreateClip 
    
    
    func (UnimplementedLivestreamServiceServer) CreateClip([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateClipRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) CreateDvrSession 
    
    
    func (UnimplementedLivestreamServiceServer) CreateDvrSession([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateDvrSessionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) CreateEvent 
    
    
    func (UnimplementedLivestreamServiceServer) CreateEvent([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateEventRequest) (*Event, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) CreateInput 
    
    
    func (UnimplementedLivestreamServiceServer) CreateInput([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateInputRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteAsset 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteAssetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteChannel 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteChannelRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteClip 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteClip([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteClipRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteDvrSession 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteDvrSession([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteDvrSessionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteEvent 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteEvent([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteEventRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) DeleteInput 
    
    
    func (UnimplementedLivestreamServiceServer) DeleteInput([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteInputRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetAsset 
    
    
    func (UnimplementedLivestreamServiceServer) GetAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetChannel 
    
    
    func (UnimplementedLivestreamServiceServer) GetChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetChannelRequest) (*Channel, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetClip 
    
    
    func (UnimplementedLivestreamServiceServer) GetClip([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetClipRequest) (*Clip, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetDvrSession 
    
    
    func (UnimplementedLivestreamServiceServer) GetDvrSession([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetDvrSessionRequest) (*DvrSession, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetEvent 
    
    
    func (UnimplementedLivestreamServiceServer) GetEvent([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetEventRequest) (*Event, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetInput 
    
    
    func (UnimplementedLivestreamServiceServer) GetInput([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetInputRequest) (*Input, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) GetPool 
    
    
    func (UnimplementedLivestreamServiceServer) GetPool([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPoolRequest) (*Pool, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListAssets 
    
    
    func (UnimplementedLivestreamServiceServer) ListAssets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAssetsRequest) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListChannels 
    
    
    func (UnimplementedLivestreamServiceServer) ListChannels([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListChannelsRequest) (*ListChannelsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListClips 
    
    
    func (UnimplementedLivestreamServiceServer) ListClips([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListClipsRequest) (*ListClipsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListDvrSessions 
    
    
    func (UnimplementedLivestreamServiceServer) ListDvrSessions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListDvrSessionsRequest) (*ListDvrSessionsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListEvents 
    
    
    func (UnimplementedLivestreamServiceServer) ListEvents([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListEventsRequest) (*ListEventsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) ListInputs 
    
    
    func (UnimplementedLivestreamServiceServer) ListInputs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListInputsRequest) (*ListInputsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) PreviewInput 
    
    
    func (UnimplementedLivestreamServiceServer) PreviewInput([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *PreviewInputRequest) (*PreviewInputResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) StartChannel 
    
    
    func (UnimplementedLivestreamServiceServer) StartChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *StartChannelRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) StartDistribution 
    
    
    func (UnimplementedLivestreamServiceServer) StartDistribution([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *StartDistributionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) StopChannel 
    
    
    func (UnimplementedLivestreamServiceServer) StopChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *StopChannelRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) StopDistribution 
    
    
    func (UnimplementedLivestreamServiceServer) StopDistribution([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *StopDistributionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) UpdateChannel 
    
    
    func (UnimplementedLivestreamServiceServer) UpdateChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateChannelRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) UpdateDvrSession 
    
    
    func (UnimplementedLivestreamServiceServer) UpdateDvrSession([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateDvrSessionRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) UpdateInput 
    
    
    func (UnimplementedLivestreamServiceServer) UpdateInput([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateInputRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedLivestreamServiceServer) UpdatePool 
    
    
    func (UnimplementedLivestreamServiceServer) UpdatePool([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdatePoolRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

## UnsafeLivestreamServiceServer
    
    
    type UnsafeLivestreamServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeLivestreamServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to LivestreamServiceServer will result in compilation errors.

## UpdateChannelRequest
    
    
    type UpdateChannelRequest struct {
    
    	// Field mask is used to specify the fields to be overwritten in the Channel
    	// resource by the update. You can only update the following fields:
    	//
    	// * [`inputAttachments`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputattachment)
    	// * [`inputConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig)
    	// * [`output`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output)
    	// * [`elementaryStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream)
    	// * [`muxStreams`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream)
    	// * [`manifests`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest)
    	// * [`spriteSheets`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet)
    	// * [`logConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig)
    	// * [`timecodeConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#timecodeconfig)
    	// * [`encryptions`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption)
    	//
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask.
    	//
    	// If the mask is not present, then each field from the list above is updated
    	// if the field appears in the request payload. To unset a field, add the
    	// field to the update mask and remove it from the request payload.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The channel resource to be updated.
    	Channel *Channel `protobuf:"bytes,2,opt,name=channel,proto3" json:"channel,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.UpdateChannel".

### func (*UpdateChannelRequest) Descriptor 
    
    
    func (*UpdateChannelRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateChannelRequest.ProtoReflect.Descriptor instead.

### func (*UpdateChannelRequest) GetChannel 
    
    
    func (x *UpdateChannelRequest) GetChannel() *Channel

### func (*UpdateChannelRequest) GetRequestId 
    
    
    func (x *UpdateChannelRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateChannelRequest) GetUpdateMask 
    
    
    func (x *UpdateChannelRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateChannelRequest) ProtoMessage 
    
    
    func (*UpdateChannelRequest) ProtoMessage()

### func (*UpdateChannelRequest) ProtoReflect 
    
    
    func (x *UpdateChannelRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateChannelRequest) Reset 
    
    
    func (x *UpdateChannelRequest) Reset()

### func (*UpdateChannelRequest) String 
    
    
    func (x *UpdateChannelRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateDvrSessionRequest
    
    
    type UpdateDvrSessionRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// DvrSession resource by the update. You can only update the following
    	// fields:
    	//
    	// * `dvrWindows`
    	//
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The DVR session resource to be updated.
    	DvrSession *DvrSession `protobuf:"bytes,2,opt,name=dvr_session,json=dvrSession,proto3" json:"dvr_session,omitempty"`
    	// Optional. A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.UpdateDvrSession".

### func (*UpdateDvrSessionRequest) Descriptor 
    
    
    func (*UpdateDvrSessionRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateDvrSessionRequest.ProtoReflect.Descriptor instead.

### func (*UpdateDvrSessionRequest) GetDvrSession 
    
    
    func (x *UpdateDvrSessionRequest) GetDvrSession() *DvrSession

### func (*UpdateDvrSessionRequest) GetRequestId 
    
    
    func (x *UpdateDvrSessionRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateDvrSessionRequest) GetUpdateMask 
    
    
    func (x *UpdateDvrSessionRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateDvrSessionRequest) ProtoMessage 
    
    
    func (*UpdateDvrSessionRequest) ProtoMessage()

### func (*UpdateDvrSessionRequest) ProtoReflect 
    
    
    func (x *UpdateDvrSessionRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateDvrSessionRequest) Reset 
    
    
    func (x *UpdateDvrSessionRequest) Reset()

### func (*UpdateDvrSessionRequest) String 
    
    
    func (x *UpdateDvrSessionRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateInputRequest
    
    
    type UpdateInputRequest struct {
    
    	// Field mask is used to specify the fields to be overwritten in the Input
    	// resource by the update. You can only update the following fields:
    	//
    	// * [`tier`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Tier)
    	// * [`preprocessingConfig`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#PreprocessingConfig)
    	// * [`securityRules`](https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule)
    	//
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask.
    	//
    	// If the mask is not present, then each field from the list above is updated
    	// if the field appears in the request payload. To unset a field, add the
    	// field to the update mask and remove it from the request payload.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The input resource to be updated.
    	Input *Input `protobuf:"bytes,2,opt,name=input,proto3" json:"input,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.UpdateInput".

### func (*UpdateInputRequest) Descriptor 
    
    
    func (*UpdateInputRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateInputRequest.ProtoReflect.Descriptor instead.

### func (*UpdateInputRequest) GetInput 
    
    
    func (x *UpdateInputRequest) GetInput() *Input

### func (*UpdateInputRequest) GetRequestId 
    
    
    func (x *UpdateInputRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateInputRequest) GetUpdateMask 
    
    
    func (x *UpdateInputRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateInputRequest) ProtoMessage 
    
    
    func (*UpdateInputRequest) ProtoMessage()

### func (*UpdateInputRequest) ProtoReflect 
    
    
    func (x *UpdateInputRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateInputRequest) Reset 
    
    
    func (x *UpdateInputRequest) Reset()

### func (*UpdateInputRequest) String 
    
    
    func (x *UpdateInputRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdatePoolRequest
    
    
    type UpdatePoolRequest struct {
    
    	// Field mask is used to specify the fields to be overwritten in the Pool
    	// resource by the update. You can only update the following fields:
    	//
    	// * `networkConfig`
    	//
    	// The fields specified in the update_mask are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The pool resource to be updated.
    	Pool *Pool `protobuf:"bytes,2,opt,name=pool,proto3" json:"pool,omitempty"`
    	// A request ID to identify requests. Specify a unique request ID
    	// so that if you must retry your request, the server will know to ignore
    	// the request if it has already been completed. The server will guarantee
    	// that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and the
    	// request times out. If you make the request again with the same request ID,
    	// the server can check if original operation with the same request ID was
    	// received, and if so, will ignore the second request. This prevents clients
    	// from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported `(00000000-0000-0000-0000-000000000000)`.
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for "LivestreamService.UpdatePool".

### func (*UpdatePoolRequest) Descriptor 
    
    
    func (*UpdatePoolRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdatePoolRequest.ProtoReflect.Descriptor instead.

### func (*UpdatePoolRequest) GetPool 
    
    
    func (x *UpdatePoolRequest) GetPool() *Pool

### func (*UpdatePoolRequest) GetRequestId 
    
    
    func (x *UpdatePoolRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdatePoolRequest) GetUpdateMask 
    
    
    func (x *UpdatePoolRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdatePoolRequest) ProtoMessage 
    
    
    func (*UpdatePoolRequest) ProtoMessage()

### func (*UpdatePoolRequest) ProtoReflect 
    
    
    func (x *UpdatePoolRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdatePoolRequest) Reset 
    
    
    func (x *UpdatePoolRequest) Reset()

### func (*UpdatePoolRequest) String 
    
    
    func (x *UpdatePoolRequest) String() [string](https://pkg.go.dev/builtin#string)

## VideoFormat
    
    
    type VideoFormat struct {
    
    	// Video codec used in this video stream.
    	Codec [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=codec,proto3" json:"codec,omitempty"`
    	// The width of the video stream in pixels.
    	WidthPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=width_pixels,json=widthPixels,proto3" json:"width_pixels,omitempty"`
    	// The height of the video stream in pixels.
    	HeightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=height_pixels,json=heightPixels,proto3" json:"height_pixels,omitempty"`
    	// The frame rate of the input video stream.
    	FrameRate [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,4,opt,name=frame_rate,json=frameRate,proto3" json:"frame_rate,omitempty"`
    	// contains filtered or unexported fields
    }

Properties of the video format.

### func (*VideoFormat) Descriptor 
    
    
    func (*VideoFormat) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VideoFormat.ProtoReflect.Descriptor instead.

### func (*VideoFormat) GetCodec 
    
    
    func (x *VideoFormat) GetCodec() [string](https://pkg.go.dev/builtin#string)

### func (*VideoFormat) GetFrameRate 
    
    
    func (x *VideoFormat) GetFrameRate() [float64](https://pkg.go.dev/builtin#float64)

### func (*VideoFormat) GetHeightPixels 
    
    
    func (x *VideoFormat) GetHeightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoFormat) GetWidthPixels 
    
    
    func (x *VideoFormat) GetWidthPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoFormat) ProtoMessage 
    
    
    func (*VideoFormat) ProtoMessage()

### func (*VideoFormat) ProtoReflect 
    
    
    func (x *VideoFormat) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VideoFormat) Reset 
    
    
    func (x *VideoFormat) Reset()

### func (*VideoFormat) String 
    
    
    func (x *VideoFormat) String() [string](https://pkg.go.dev/builtin#string)

## VideoStream
    
    
    type VideoStream struct {
    
    	// Codec settings.
    	//
    	// Types that are valid to be assigned to CodecSettings:
    	//
    	//	*VideoStream_H264
    	//	*VideoStream_H265
    	CodecSettings isVideoStream_CodecSettings `protobuf_oneof:"codec_settings"`
    	// contains filtered or unexported fields
    }

Video stream resource.

### func (*VideoStream) Descriptor 
    
    
    func (*VideoStream) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VideoStream.ProtoReflect.Descriptor instead.

### func (*VideoStream) GetCodecSettings 
    
    
    func (x *VideoStream) GetCodecSettings() isVideoStream_CodecSettings

### func (*VideoStream) GetH264 
    
    
    func (x *VideoStream) GetH264() *VideoStream_H264CodecSettings

### func (*VideoStream) GetH265 
    
    
    func (x *VideoStream) GetH265() *VideoStream_H265CodecSettings

### func (*VideoStream) ProtoMessage 
    
    
    func (*VideoStream) ProtoMessage()

### func (*VideoStream) ProtoReflect 
    
    
    func (x *VideoStream) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VideoStream) Reset 
    
    
    func (x *VideoStream) Reset()

### func (*VideoStream) String 
    
    
    func (x *VideoStream) String() [string](https://pkg.go.dev/builtin#string)

## VideoStreamProperty
    
    
    type VideoStreamProperty struct {
    
    	// Index of this video stream.
    	Index [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=index,proto3" json:"index,omitempty"`
    	// Properties of the video format.
    	VideoFormat *VideoFormat `protobuf:"bytes,2,opt,name=video_format,json=videoFormat,proto3" json:"video_format,omitempty"`
    	// contains filtered or unexported fields
    }

Properties of the video stream.

### func (*VideoStreamProperty) Descriptor 
    
    
    func (*VideoStreamProperty) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VideoStreamProperty.ProtoReflect.Descriptor instead.

### func (*VideoStreamProperty) GetIndex 
    
    
    func (x *VideoStreamProperty) GetIndex() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStreamProperty) GetVideoFormat 
    
    
    func (x *VideoStreamProperty) GetVideoFormat() *VideoFormat

### func (*VideoStreamProperty) ProtoMessage 
    
    
    func (*VideoStreamProperty) ProtoMessage()

### func (*VideoStreamProperty) ProtoReflect 
    
    
    func (x *VideoStreamProperty) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VideoStreamProperty) Reset 
    
    
    func (x *VideoStreamProperty) Reset()

### func (*VideoStreamProperty) String 
    
    
    func (x *VideoStreamProperty) String() [string](https://pkg.go.dev/builtin#string)

## VideoStream_H264
    
    
    type VideoStream_H264 struct {
    	// H264 codec settings.
    	H264 *VideoStream_H264CodecSettings `protobuf:"bytes,20,opt,name=h264,proto3,oneof"`
    }

## VideoStream_H264CodecSettings
    
    
    type VideoStream_H264CodecSettings struct {
    
    	// Required. The width of the video in pixels. Must be an even integer.
    	// Valid range is [320, 4096].
    	WidthPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=width_pixels,json=widthPixels,proto3" json:"width_pixels,omitempty"`
    	// Required. The height of the video in pixels. Must be an even integer.
    	// Valid range is [180, 2160].
    	HeightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=height_pixels,json=heightPixels,proto3" json:"height_pixels,omitempty"`
    	// Required. The target video frame rate in frames per second (FPS). Must be
    	// less than or equal to 60. Will default to the input frame rate if larger
    	// than the input frame rate. The API will generate an output FPS that is
    	// divisible by the input FPS, and smaller or equal to the target FPS. See
    	// [Calculating frame
    	// rate](https://cloud.google.com/transcoder/docs/concepts/frame-rate) for
    	// more information.
    	FrameRate [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=frame_rate,json=frameRate,proto3" json:"frame_rate,omitempty"`
    	// Required. The video bitrate in bits per second. Minimum value is 10,000.
    	//
    	// - For SD resolution (< 720p),="" must="" be=""><= 3,000,000="" (3="" mbps).="" -="" for="" hd="" resolution=""><= 1080p),="" must="" be=""><= 15,000,000="" (15="" mbps).="" -="" for="" uhd="" resolution=""><= 2160p),="" must="" be=""><= 25,000,000="" (25="" mbps).="" bitratebps="">[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=bitrate_bps,json=bitrateBps,proto3" json:"bitrate_bps,omitempty"`
    	// Specifies whether an open Group of Pictures (GOP) structure should be
    	// allowed or not. The default is `false`.
    	AllowOpenGop [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=allow_open_gop,json=allowOpenGop,proto3" json:"allow_open_gop,omitempty"`
    	// GOP mode can be either by frame count or duration.
    	//
    	// Types that are valid to be assigned to GopMode:
    	//
    	//	*VideoStream_H264CodecSettings_GopFrameCount
    	//	*VideoStream_H264CodecSettings_GopDuration
    	GopMode isVideoStream_H264CodecSettings_GopMode `protobuf_oneof:"gop_mode"`
    	// Size of the Video Buffering Verifier (VBV) buffer in bits. Must be
    	// greater than zero. The default is equal to
    	// [bitrate_bps][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.bitrate_bps].
    	VbvSizeBits [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,9,opt,name=vbv_size_bits,json=vbvSizeBits,proto3" json:"vbv_size_bits,omitempty"`
    	// Initial fullness of the Video Buffering Verifier (VBV) buffer in bits.
    	// Must be greater than zero. The default is equal to 90% of
    	// [vbv_size_bits][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.vbv_size_bits].
    	VbvFullnessBits [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,10,opt,name=vbv_fullness_bits,json=vbvFullnessBits,proto3" json:"vbv_fullness_bits,omitempty"`
    	// The entropy coder to use. The default is `cabac`.
    	//
    	// Supported entropy coders:
    	//
    	// - `cavlc`
    	// - `cabac`
    	EntropyCoder [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=entropy_coder,json=entropyCoder,proto3" json:"entropy_coder,omitempty"`
    	// Allow B-pyramid for reference frame selection. This may not be supported
    	// on all decoders. The default is `false`.
    	BPyramid [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,12,opt,name=b_pyramid,json=bPyramid,proto3" json:"b_pyramid,omitempty"`
    	// The number of consecutive B-frames. Must be greater than or equal to
    	// zero. Must be less than
    	// [gop_frame_count][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.gop_frame_count]
    	// if set. The default is 0.
    	BFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,13,opt,name=b_frame_count,json=bFrameCount,proto3" json:"b_frame_count,omitempty"`
    	// Specify the intensity of the adaptive quantizer (AQ). Must be between 0
    	// and 1, where 0 disables the quantizer and 1 maximizes the quantizer. A
    	// higher value equals a lower bitrate but smoother image. The default is 0.
    	AqStrength [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,14,opt,name=aq_strength,json=aqStrength,proto3" json:"aq_strength,omitempty"`
    	// Enforces the specified codec profile. The following profiles are
    	// supported:
    	//
    	// *   `baseline`
    	// *   `main` (default)
    	// *   `high`
    	//
    	// The available options are [FFmpeg-compatible Profile
    	// Options](https://trac.ffmpeg.org/wiki/Encode/H.264#Profile).
    	// Note that certain values for this field may cause the
    	// transcoder to override other fields you set in the
    	// [H264CodecSettings][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings]
    	// message.
    	Profile [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,15,opt,name=profile,proto3" json:"profile,omitempty"`
    	// Enforces the specified codec tune. The available options are
    	// [FFmpeg-compatible Encode
    	// Options](https://trac.ffmpeg.org/wiki/Encode/H.264#Tune)
    	// Note that certain values for this field may cause the transcoder to
    	// override other fields you set in the
    	// [H264CodecSettings][google.cloud.video.livestream.v1.VideoStream.H264CodecSettings]
    	// message.
    	Tune [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,16,opt,name=tune,proto3" json:"tune,omitempty"`
    	// contains filtered or unexported fields
    }

H264 codec settings.

### func (*VideoStream_H264CodecSettings) Descriptor 
    
    
    func (*VideoStream_H264CodecSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VideoStream_H264CodecSettings.ProtoReflect.Descriptor instead.

### func (*VideoStream_H264CodecSettings) GetAllowOpenGop 
    
    
    func (x *VideoStream_H264CodecSettings) GetAllowOpenGop() [bool](https://pkg.go.dev/builtin#bool)

### func (*VideoStream_H264CodecSettings) GetAqStrength 
    
    
    func (x *VideoStream_H264CodecSettings) GetAqStrength() [float64](https://pkg.go.dev/builtin#float64)

### func (*VideoStream_H264CodecSettings) GetBFrameCount 
    
    
    func (x *VideoStream_H264CodecSettings) GetBFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetBPyramid 
    
    
    func (x *VideoStream_H264CodecSettings) GetBPyramid() [bool](https://pkg.go.dev/builtin#bool)

### func (*VideoStream_H264CodecSettings) GetBitrateBps 
    
    
    func (x *VideoStream_H264CodecSettings) GetBitrateBps() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetEntropyCoder 
    
    
    func (x *VideoStream_H264CodecSettings) GetEntropyCoder() [string](https://pkg.go.dev/builtin#string)

### func (*VideoStream_H264CodecSettings) GetFrameRate 
    
    
    func (x *VideoStream_H264CodecSettings) GetFrameRate() [float64](https://pkg.go.dev/builtin#float64)

### func (*VideoStream_H264CodecSettings) GetGopDuration 
    
    
    func (x *VideoStream_H264CodecSettings) GetGopDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*VideoStream_H264CodecSettings) GetGopFrameCount 
    
    
    func (x *VideoStream_H264CodecSettings) GetGopFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetGopMode 
    
    
    func (x *VideoStream_H264CodecSettings) GetGopMode() isVideoStream_H264CodecSettings_GopMode

### func (*VideoStream_H264CodecSettings) GetHeightPixels 
    
    
    func (x *VideoStream_H264CodecSettings) GetHeightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetProfile 
    
    
    func (x *VideoStream_H264CodecSettings) GetProfile() [string](https://pkg.go.dev/builtin#string)

### func (*VideoStream_H264CodecSettings) GetTune 
    
    
    func (x *VideoStream_H264CodecSettings) GetTune() [string](https://pkg.go.dev/builtin#string)

### func (*VideoStream_H264CodecSettings) GetVbvFullnessBits 
    
    
    func (x *VideoStream_H264CodecSettings) GetVbvFullnessBits() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetVbvSizeBits 
    
    
    func (x *VideoStream_H264CodecSettings) GetVbvSizeBits() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) GetWidthPixels 
    
    
    func (x *VideoStream_H264CodecSettings) GetWidthPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H264CodecSettings) ProtoMessage 
    
    
    func (*VideoStream_H264CodecSettings) ProtoMessage()

### func (*VideoStream_H264CodecSettings) ProtoReflect 
    
    
    func (x *VideoStream_H264CodecSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VideoStream_H264CodecSettings) Reset 
    
    
    func (x *VideoStream_H264CodecSettings) Reset()

### func (*VideoStream_H264CodecSettings) String 
    
    
    func (x *VideoStream_H264CodecSettings) String() [string](https://pkg.go.dev/builtin#string)

## VideoStream_H264CodecSettings_GopDuration
    
    
    type VideoStream_H264CodecSettings_GopDuration struct {
    	// Select the GOP size based on the specified duration. The default is
    	// `2s`. Note that `gopDuration` must be less than or equal to
    	// [segment_duration][google.cloud.video.livestream.v1.SegmentSettings.segment_duration],
    	// and
    	// [segment_duration][google.cloud.video.livestream.v1.SegmentSettings.segment_duration]
    	// must be divisible by `gopDuration`. Valid range is [2s, 20s].
    	//
    	// All video streams in the same channel must have the same GOP size.
    	GopDuration *durationpb.Duration `protobuf:"bytes,8,opt,name=gop_duration,json=gopDuration,proto3,oneof"`
    }

## VideoStream_H264CodecSettings_GopFrameCount
    
    
    type VideoStream_H264CodecSettings_GopFrameCount struct {
    	// Select the GOP size based on the specified frame count.
    	// If GOP frame count is set instead of GOP duration, GOP duration will be
    	// calculated by `gopFrameCount`/`frameRate`. The calculated GOP duration
    	// must satisfy the limitations on `gopDuration` as well.
    	// Valid range is [60, 600].
    	GopFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=gop_frame_count,json=gopFrameCount,proto3,oneof"`
    }

## VideoStream_H265
    
    
    type VideoStream_H265 struct {
    	// H265 codec settings.
    	H265 *VideoStream_H265CodecSettings `protobuf:"bytes,21,opt,name=h265,proto3,oneof"`
    }

## VideoStream_H265CodecSettings
    
    
    type VideoStream_H265CodecSettings struct {
    
    	// Optional. The width of the video in pixels. Must be an even integer.
    	// When not specified, the width is adjusted to match the specified height
    	// and input aspect ratio. If both are omitted, the input width is used.
    	// Valid range is [320, 4096].
    	WidthPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=width_pixels,json=widthPixels,proto3" json:"width_pixels,omitempty"`
    	// Optional. The height of the video in pixels. Must be an even integer.
    	// When not specified, the height is adjusted to match the specified width
    	// and input aspect ratio. If both are omitted, the input height is used.
    	// Valid range is [180, 2160].
    	HeightPixels [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=height_pixels,json=heightPixels,proto3" json:"height_pixels,omitempty"`
    	// Required. The target video frame rate in frames per second (FPS). Must be
    	// less than or equal to 120. Will default to the input frame rate if larger
    	// than the input frame rate. The API will generate an output FPS that is
    	// divisible by the input FPS, and smaller or equal to the target FPS. See
    	// [Calculating frame
    	// rate](https://cloud.google.com/transcoder/docs/concepts/frame-rate) for
    	// more information.
    	FrameRate [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=frame_rate,json=frameRate,proto3" json:"frame_rate,omitempty"`
    	// Required. The video bitrate in bits per second. Minimum value is 10,000.
    	//
    	// - For SD resolution (< 720p),="" must="" be=""><= 3,000,000="" (3="" mbps).="" -="" for="" hd="" resolution=""><= 1080p),="" must="" be=""><= 15,000,000="" (15="" mbps).="" -="" for="" uhd="" resolution=""><= 2160p),="" must="" be=""><= 25,000,000="" (25="" mbps).="" bitratebps="">[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=bitrate_bps,json=bitrateBps,proto3" json:"bitrate_bps,omitempty"`
    	// GOP mode can be either by frame count or duration.
    	//
    	// Types that are valid to be assigned to GopMode:
    	//
    	//	*VideoStream_H265CodecSettings_GopFrameCount
    	//	*VideoStream_H265CodecSettings_GopDuration
    	GopMode isVideoStream_H265CodecSettings_GopMode `protobuf_oneof:"gop_mode"`
    	// Optional. Size of the Video Buffering Verifier (VBV) buffer in bits. Must
    	// be greater than zero. The default is equal to
    	// [bitrate_bps][google.cloud.video.livestream.v1.VideoStream.H265CodecSettings.bitrate_bps].
    	VbvSizeBits [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,9,opt,name=vbv_size_bits,json=vbvSizeBits,proto3" json:"vbv_size_bits,omitempty"`
    	// Optional. Initial fullness of the Video Buffering Verifier (VBV) buffer
    	// in bits. Must be greater than zero. The default is equal to 90% of
    	// [vbv_size_bits][google.cloud.video.livestream.v1.VideoStream.H265CodecSettings.vbv_size_bits].
    	VbvFullnessBits [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,10,opt,name=vbv_fullness_bits,json=vbvFullnessBits,proto3" json:"vbv_fullness_bits,omitempty"`
    	// Optional. Allow B-pyramid for reference frame selection. This may not be
    	// supported on all decoders. The default is `false`.
    	BPyramid [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,11,opt,name=b_pyramid,json=bPyramid,proto3" json:"b_pyramid,omitempty"`
    	// Optional. The number of consecutive B-frames. Must be greater than or
    	// equal to zero. Must be less than
    	// [gop_frame_count][google.cloud.video.livestream.v1.VideoStream.H265CodecSettings.gop_frame_count]
    	// if set. The default is 0.
    	BFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,12,opt,name=b_frame_count,json=bFrameCount,proto3" json:"b_frame_count,omitempty"`
    	// Optional. Specify the intensity of the adaptive quantizer (AQ). Must be
    	// between 0 and 1, where 0 disables the quantizer and 1 maximizes the
    	// quantizer. A higher value equals a lower bitrate but smoother image. The
    	// default is 0.
    	AqStrength [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,13,opt,name=aq_strength,json=aqStrength,proto3" json:"aq_strength,omitempty"`
    	// contains filtered or unexported fields
    }

H265 codec settings.

### func (*VideoStream_H265CodecSettings) Descriptor 
    
    
    func (*VideoStream_H265CodecSettings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VideoStream_H265CodecSettings.ProtoReflect.Descriptor instead.

### func (*VideoStream_H265CodecSettings) GetAqStrength 
    
    
    func (x *VideoStream_H265CodecSettings) GetAqStrength() [float64](https://pkg.go.dev/builtin#float64)

### func (*VideoStream_H265CodecSettings) GetBFrameCount 
    
    
    func (x *VideoStream_H265CodecSettings) GetBFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetBPyramid 
    
    
    func (x *VideoStream_H265CodecSettings) GetBPyramid() [bool](https://pkg.go.dev/builtin#bool)

### func (*VideoStream_H265CodecSettings) GetBitrateBps 
    
    
    func (x *VideoStream_H265CodecSettings) GetBitrateBps() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetFrameRate 
    
    
    func (x *VideoStream_H265CodecSettings) GetFrameRate() [float64](https://pkg.go.dev/builtin#float64)

### func (*VideoStream_H265CodecSettings) GetGopDuration 
    
    
    func (x *VideoStream_H265CodecSettings) GetGopDuration() *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration)

### func (*VideoStream_H265CodecSettings) GetGopFrameCount 
    
    
    func (x *VideoStream_H265CodecSettings) GetGopFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetGopMode 
    
    
    func (x *VideoStream_H265CodecSettings) GetGopMode() isVideoStream_H265CodecSettings_GopMode

### func (*VideoStream_H265CodecSettings) GetHeightPixels 
    
    
    func (x *VideoStream_H265CodecSettings) GetHeightPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetVbvFullnessBits 
    
    
    func (x *VideoStream_H265CodecSettings) GetVbvFullnessBits() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetVbvSizeBits 
    
    
    func (x *VideoStream_H265CodecSettings) GetVbvSizeBits() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) GetWidthPixels 
    
    
    func (x *VideoStream_H265CodecSettings) GetWidthPixels() [int32](https://pkg.go.dev/builtin#int32)

### func (*VideoStream_H265CodecSettings) ProtoMessage 
    
    
    func (*VideoStream_H265CodecSettings) ProtoMessage()

### func (*VideoStream_H265CodecSettings) ProtoReflect 
    
    
    func (x *VideoStream_H265CodecSettings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VideoStream_H265CodecSettings) Reset 
    
    
    func (x *VideoStream_H265CodecSettings) Reset()

### func (*VideoStream_H265CodecSettings) String 
    
    
    func (x *VideoStream_H265CodecSettings) String() [string](https://pkg.go.dev/builtin#string)

## VideoStream_H265CodecSettings_GopDuration
    
    
    type VideoStream_H265CodecSettings_GopDuration struct {
    	// Optional. Select the GOP size based on the specified duration. The
    	// default is `2s`. Note that `gopDuration` must be less than or equal to
    	// [segment_duration][google.cloud.video.livestream.v1.SegmentSettings.segment_duration],
    	// and
    	// [segment_duration][google.cloud.video.livestream.v1.SegmentSettings.segment_duration]
    	// must be divisible by `gopDuration`. Valid range is [2s, 20s].
    	//
    	// All video streams in the same channel must have the same GOP size.
    	GopDuration *durationpb.Duration `protobuf:"bytes,8,opt,name=gop_duration,json=gopDuration,proto3,oneof"`
    }

## VideoStream_H265CodecSettings_GopFrameCount
    
    
    type VideoStream_H265CodecSettings_GopFrameCount struct {
    	// Optional. Select the GOP size based on the specified frame count.
    	// If GOP frame count is set instead of GOP duration, GOP duration will be
    	// calculated by `gopFrameCount`/`frameRate`. The calculated GOP duration
    	// must satisfy the limitations on `gopDuration` as well.
    	// Valid range is [60, 600].
    	GopFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=gop_frame_count,json=gopFrameCount,proto3,oneof"`
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
