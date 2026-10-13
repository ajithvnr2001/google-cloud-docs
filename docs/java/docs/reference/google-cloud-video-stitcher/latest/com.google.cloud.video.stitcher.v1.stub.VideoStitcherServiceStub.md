---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStub
title: Class VideoStitcherServiceStub (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:24.430526+00:00
---

# Class VideoStitcherServiceStub (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VideoStitcherServiceStub (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6  0.1.2 
    
    
    public abstract class VideoStitcherServiceStub implements BackgroundResource

Base stub class for the VideoStitcherService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VideoStitcherServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### VideoStitcherServiceStub()
    
    
    public VideoStitcherServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createCdnKeyCallable()
    
    
    public UnaryCallable<CreateCdnKeyRequest,Operation> createCdnKeyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCdnKeyOperationCallable()
    
    
    public OperationCallable<CreateCdnKeyRequest,CdnKey,OperationMetadata> createCdnKeyOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigCallable()
    
    
    public UnaryCallable<CreateLiveConfigRequest,Operation> createLiveConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLiveConfigOperationCallable()
    
    
    public OperationCallable<CreateLiveConfigRequest,LiveConfig,OperationMetadata> createLiveConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveSessionCallable()
    
    
    public UnaryCallable<CreateLiveSessionRequest,LiveSession> createLiveSessionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### createSlateCallable()
    
    
    public UnaryCallable<CreateSlateRequest,Operation> createSlateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSlateOperationCallable()
    
    
    public OperationCallable<CreateSlateRequest,Slate,OperationMetadata> createSlateOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigCallable()
    
    
    public UnaryCallable<CreateVodConfigRequest,Operation> createVodConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVodConfigOperationCallable()
    
    
    public OperationCallable<CreateVodConfigRequest,VodConfig,OperationMetadata> createVodConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodSessionCallable()
    
    
    public UnaryCallable<CreateVodSessionRequest,VodSession> createVodSessionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### deleteCdnKeyCallable()
    
    
    public UnaryCallable<DeleteCdnKeyRequest,Operation> deleteCdnKeyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCdnKeyOperationCallable()
    
    
    public OperationCallable<DeleteCdnKeyRequest,Empty,OperationMetadata> deleteCdnKeyOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigCallable()
    
    
    public UnaryCallable<DeleteLiveConfigRequest,Operation> deleteLiveConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLiveConfigOperationCallable()
    
    
    public OperationCallable<DeleteLiveConfigRequest,Empty,OperationMetadata> deleteLiveConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateCallable()
    
    
    public UnaryCallable<DeleteSlateRequest,Operation> deleteSlateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSlateOperationCallable()
    
    
    public OperationCallable<DeleteSlateRequest,Empty,OperationMetadata> deleteSlateOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigCallable()
    
    
    public UnaryCallable<DeleteVodConfigRequest,Operation> deleteVodConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVodConfigOperationCallable()
    
    
    public OperationCallable<DeleteVodConfigRequest,Empty,OperationMetadata> deleteVodConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### getCdnKeyCallable()
    
    
    public UnaryCallable<GetCdnKeyRequest,CdnKey> getCdnKeyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)>` |   
  
### getLiveAdTagDetailCallable()
    
    
    public UnaryCallable<GetLiveAdTagDetailRequest,LiveAdTagDetail> getLiveAdTagDetailCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest),[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)>` |   
  
### getLiveConfigCallable()
    
    
    public UnaryCallable<GetLiveConfigRequest,LiveConfig> getLiveConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)>` |   
  
### getLiveSessionCallable()
    
    
    public UnaryCallable<GetLiveSessionRequest,LiveSession> getLiveSessionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### getSlateCallable()
    
    
    public UnaryCallable<GetSlateRequest,Slate> getSlateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)>` |   
  
### getVodAdTagDetailCallable()
    
    
    public UnaryCallable<GetVodAdTagDetailRequest,VodAdTagDetail> getVodAdTagDetailCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest),[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)>` |   
  
### getVodConfigCallable()
    
    
    public UnaryCallable<GetVodConfigRequest,VodConfig> getVodConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)>` |   
  
### getVodSessionCallable()
    
    
    public UnaryCallable<GetVodSessionRequest,VodSession> getVodSessionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### getVodStitchDetailCallable()
    
    
    public UnaryCallable<GetVodStitchDetailRequest,VodStitchDetail> getVodStitchDetailCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest),[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)>` |   
  
### listCdnKeysCallable()
    
    
    public UnaryCallable<ListCdnKeysRequest,ListCdnKeysResponse> listCdnKeysCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest),[ListCdnKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysResponse)>` |   
  
### listCdnKeysPagedCallable()
    
    
    public UnaryCallable<ListCdnKeysRequest,VideoStitcherServiceClient.ListCdnKeysPagedResponse> listCdnKeysPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest),[ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)>` |   
  
### listLiveAdTagDetailsCallable()
    
    
    public UnaryCallable<ListLiveAdTagDetailsRequest,ListLiveAdTagDetailsResponse> listLiveAdTagDetailsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest),[ListLiveAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsResponse)>` |   
  
### listLiveAdTagDetailsPagedCallable()
    
    
    public UnaryCallable<ListLiveAdTagDetailsRequest,VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse> listLiveAdTagDetailsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest),[ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)>` |   
  
### listLiveConfigsCallable()
    
    
    public UnaryCallable<ListLiveConfigsRequest,ListLiveConfigsResponse> listLiveConfigsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest),[ListLiveConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsResponse)>` |   
  
### listLiveConfigsPagedCallable()
    
    
    public UnaryCallable<ListLiveConfigsRequest,VideoStitcherServiceClient.ListLiveConfigsPagedResponse> listLiveConfigsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest),[ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)>` |   
  
### listSlatesCallable()
    
    
    public UnaryCallable<ListSlatesRequest,ListSlatesResponse> listSlatesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest),[ListSlatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesResponse)>` |   
  
### listSlatesPagedCallable()
    
    
    public UnaryCallable<ListSlatesRequest,VideoStitcherServiceClient.ListSlatesPagedResponse> listSlatesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest),[ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)>` |   
  
### listVodAdTagDetailsCallable()
    
    
    public UnaryCallable<ListVodAdTagDetailsRequest,ListVodAdTagDetailsResponse> listVodAdTagDetailsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest),[ListVodAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsResponse)>` |   
  
### listVodAdTagDetailsPagedCallable()
    
    
    public UnaryCallable<ListVodAdTagDetailsRequest,VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse> listVodAdTagDetailsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest),[ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)>` |   
  
### listVodConfigsCallable()
    
    
    public UnaryCallable<ListVodConfigsRequest,ListVodConfigsResponse> listVodConfigsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest),[ListVodConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsResponse)>` |   
  
### listVodConfigsPagedCallable()
    
    
    public UnaryCallable<ListVodConfigsRequest,VideoStitcherServiceClient.ListVodConfigsPagedResponse> listVodConfigsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest),[ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)>` |   
  
### listVodStitchDetailsCallable()
    
    
    public UnaryCallable<ListVodStitchDetailsRequest,ListVodStitchDetailsResponse> listVodStitchDetailsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest),[ListVodStitchDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsResponse)>` |   
  
### listVodStitchDetailsPagedCallable()
    
    
    public UnaryCallable<ListVodStitchDetailsRequest,VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse> listVodStitchDetailsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest),[ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)>` |   
  
### updateCdnKeyCallable()
    
    
    public UnaryCallable<UpdateCdnKeyRequest,Operation> updateCdnKeyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCdnKeyOperationCallable()
    
    
    public OperationCallable<UpdateCdnKeyRequest,CdnKey,OperationMetadata> updateCdnKeyOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateLiveConfigCallable()
    
    
    public UnaryCallable<UpdateLiveConfigRequest,Operation> updateLiveConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLiveConfigOperationCallable()
    
    
    public OperationCallable<UpdateLiveConfigRequest,LiveConfig,OperationMetadata> updateLiveConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateSlateCallable()
    
    
    public UnaryCallable<UpdateSlateRequest,Operation> updateSlateCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSlateOperationCallable()
    
    
    public OperationCallable<UpdateSlateRequest,Slate,OperationMetadata> updateSlateOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateVodConfigCallable()
    
    
    public UnaryCallable<UpdateVodConfigRequest,Operation> updateVodConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVodConfigOperationCallable()
    
    
    public OperationCallable<UpdateVodConfigRequest,VodConfig,OperationMetadata> updateVodConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
