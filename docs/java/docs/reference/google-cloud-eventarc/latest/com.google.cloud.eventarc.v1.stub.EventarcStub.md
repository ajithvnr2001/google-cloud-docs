---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.stub.EventarcStub
title: Class EventarcStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:29.058453+00:00
---

# Class EventarcStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.stub.EventarcStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EventarcStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.2.4 
    
    
    public abstract class EventarcStub implements BackgroundResource

Base stub class for the Eventarc service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EventarcStub

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

### EventarcStub()
    
    
    public EventarcStub()

## Methods 

### close()
    
    
    public abstract void close()

### createChannelCallable()
    
    
    public UnaryCallable<CreateChannelRequest,Operation> createChannelCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createChannelConnectionCallable()
    
    
    public UnaryCallable<CreateChannelConnectionRequest,Operation> createChannelConnectionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createChannelConnectionOperationCallable()
    
    
    public OperationCallable<CreateChannelConnectionRequest,ChannelConnection,OperationMetadata> createChannelConnectionOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelConnectionRequest),[ChannelConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ChannelConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createChannelOperationCallable()
    
    
    public OperationCallable<CreateChannelRequest,Channel,OperationMetadata> createChannelOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createEnrollmentCallable()
    
    
    public UnaryCallable<CreateEnrollmentRequest,Operation> createEnrollmentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateEnrollmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEnrollmentOperationCallable()
    
    
    public OperationCallable<CreateEnrollmentRequest,Enrollment,OperationMetadata> createEnrollmentOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateEnrollmentRequest),[Enrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Enrollment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createGoogleApiSourceCallable()
    
    
    public UnaryCallable<CreateGoogleApiSourceRequest,Operation> createGoogleApiSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateGoogleApiSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoogleApiSourceOperationCallable()
    
    
    public OperationCallable<CreateGoogleApiSourceRequest,GoogleApiSource,OperationMetadata> createGoogleApiSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateGoogleApiSourceRequest),[GoogleApiSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleApiSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createMessageBusCallable()
    
    
    public UnaryCallable<CreateMessageBusRequest,Operation> createMessageBusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateMessageBusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMessageBusOperationCallable()
    
    
    public OperationCallable<CreateMessageBusRequest,MessageBus,OperationMetadata> createMessageBusOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateMessageBusRequest),[MessageBus](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.MessageBus),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createPipelineCallable()
    
    
    public UnaryCallable<CreatePipelineRequest,Operation> createPipelineCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreatePipelineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPipelineOperationCallable()
    
    
    public OperationCallable<CreatePipelineRequest,Pipeline,OperationMetadata> createPipelineOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreatePipelineRequest),[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Pipeline),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### createTriggerCallable()
    
    
    public UnaryCallable<CreateTriggerRequest,Operation> createTriggerCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateTriggerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTriggerOperationCallable()
    
    
    public OperationCallable<CreateTriggerRequest,Trigger,OperationMetadata> createTriggerOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateTriggerRequest),[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Trigger),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteChannelCallable()
    
    
    public UnaryCallable<DeleteChannelRequest,Operation> deleteChannelCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteChannelConnectionCallable()
    
    
    public UnaryCallable<DeleteChannelConnectionRequest,Operation> deleteChannelConnectionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteChannelConnectionOperationCallable()
    
    
    public OperationCallable<DeleteChannelConnectionRequest,ChannelConnection,OperationMetadata> deleteChannelConnectionOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelConnectionRequest),[ChannelConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ChannelConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteChannelOperationCallable()
    
    
    public OperationCallable<DeleteChannelRequest,Channel,OperationMetadata> deleteChannelOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteEnrollmentCallable()
    
    
    public UnaryCallable<DeleteEnrollmentRequest,Operation> deleteEnrollmentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteEnrollmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEnrollmentOperationCallable()
    
    
    public OperationCallable<DeleteEnrollmentRequest,Enrollment,OperationMetadata> deleteEnrollmentOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteEnrollmentRequest),[Enrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Enrollment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteGoogleApiSourceCallable()
    
    
    public UnaryCallable<DeleteGoogleApiSourceRequest,Operation> deleteGoogleApiSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteGoogleApiSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoogleApiSourceOperationCallable()
    
    
    public OperationCallable<DeleteGoogleApiSourceRequest,GoogleApiSource,OperationMetadata> deleteGoogleApiSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteGoogleApiSourceRequest),[GoogleApiSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleApiSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteMessageBusCallable()
    
    
    public UnaryCallable<DeleteMessageBusRequest,Operation> deleteMessageBusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteMessageBusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMessageBusOperationCallable()
    
    
    public OperationCallable<DeleteMessageBusRequest,MessageBus,OperationMetadata> deleteMessageBusOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteMessageBusRequest),[MessageBus](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.MessageBus),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deletePipelineCallable()
    
    
    public UnaryCallable<DeletePipelineRequest,Operation> deletePipelineCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeletePipelineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePipelineOperationCallable()
    
    
    public OperationCallable<DeletePipelineRequest,Pipeline,OperationMetadata> deletePipelineOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeletePipelineRequest),[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Pipeline),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### deleteTriggerCallable()
    
    
    public UnaryCallable<DeleteTriggerRequest,Operation> deleteTriggerCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteTriggerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTriggerOperationCallable()
    
    
    public OperationCallable<DeleteTriggerRequest,Trigger,OperationMetadata> deleteTriggerOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteTriggerRequest),[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Trigger),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### getChannelCallable()
    
    
    public UnaryCallable<GetChannelRequest,Channel> getChannelCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Channel)>` |   
  
### getChannelConnectionCallable()
    
    
    public UnaryCallable<GetChannelConnectionRequest,ChannelConnection> getChannelConnectionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetChannelConnectionRequest),[ChannelConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ChannelConnection)>` |   
  
### getEnrollmentCallable()
    
    
    public UnaryCallable<GetEnrollmentRequest,Enrollment> getEnrollmentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetEnrollmentRequest),[Enrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Enrollment)>` |   
  
### getGoogleApiSourceCallable()
    
    
    public UnaryCallable<GetGoogleApiSourceRequest,GoogleApiSource> getGoogleApiSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetGoogleApiSourceRequest),[GoogleApiSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleApiSource)>` |   
  
### getGoogleChannelConfigCallable()
    
    
    public UnaryCallable<GetGoogleChannelConfigRequest,GoogleChannelConfig> getGoogleChannelConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGoogleChannelConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetGoogleChannelConfigRequest),[GoogleChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleChannelConfig)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getIamPolicyCallable()
    
    
    public UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMessageBusCallable()
    
    
    public UnaryCallable<GetMessageBusRequest,MessageBus> getMessageBusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetMessageBusRequest),[MessageBus](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.MessageBus)>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### getPipelineCallable()
    
    
    public UnaryCallable<GetPipelineRequest,Pipeline> getPipelineCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetPipelineRequest),[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Pipeline)>` |   
  
### getProviderCallable()
    
    
    public UnaryCallable<GetProviderRequest,Provider> getProviderCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetProviderRequest),[Provider](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Provider)>` |   
  
### getTriggerCallable()
    
    
    public UnaryCallable<GetTriggerRequest,Trigger> getTriggerCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetTriggerRequest),[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Trigger)>` |   
  
### listChannelConnectionsCallable()
    
    
    public UnaryCallable<ListChannelConnectionsRequest,ListChannelConnectionsResponse> listChannelConnectionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelConnectionsRequest),[ListChannelConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelConnectionsResponse)>` |   
  
### listChannelConnectionsPagedCallable()
    
    
    public UnaryCallable<ListChannelConnectionsRequest,EventarcClient.ListChannelConnectionsPagedResponse> listChannelConnectionsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelConnectionsRequest),[ListChannelConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListChannelConnectionsPagedResponse)>` |   
  
### listChannelsCallable()
    
    
    public UnaryCallable<ListChannelsRequest,ListChannelsResponse> listChannelsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelsRequest),[ListChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelsResponse)>` |   
  
### listChannelsPagedCallable()
    
    
    public UnaryCallable<ListChannelsRequest,EventarcClient.ListChannelsPagedResponse> listChannelsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelsRequest),[ListChannelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListChannelsPagedResponse)>` |   
  
### listEnrollmentsCallable()
    
    
    public UnaryCallable<ListEnrollmentsRequest,ListEnrollmentsResponse> listEnrollmentsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListEnrollmentsRequest),[ListEnrollmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListEnrollmentsResponse)>` |   
  
### listEnrollmentsPagedCallable()
    
    
    public UnaryCallable<ListEnrollmentsRequest,EventarcClient.ListEnrollmentsPagedResponse> listEnrollmentsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListEnrollmentsRequest),[ListEnrollmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListEnrollmentsPagedResponse)>` |   
  
### listGoogleApiSourcesCallable()
    
    
    public UnaryCallable<ListGoogleApiSourcesRequest,ListGoogleApiSourcesResponse> listGoogleApiSourcesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoogleApiSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListGoogleApiSourcesRequest),[ListGoogleApiSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListGoogleApiSourcesResponse)>` |   
  
### listGoogleApiSourcesPagedCallable()
    
    
    public UnaryCallable<ListGoogleApiSourcesRequest,EventarcClient.ListGoogleApiSourcesPagedResponse> listGoogleApiSourcesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGoogleApiSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListGoogleApiSourcesRequest),[ListGoogleApiSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListGoogleApiSourcesPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,EventarcClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListLocationsPagedResponse)>` |   
  
### listMessageBusEnrollmentsCallable()
    
    
    public UnaryCallable<ListMessageBusEnrollmentsRequest,ListMessageBusEnrollmentsResponse> listMessageBusEnrollmentsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusEnrollmentsRequest),[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse)>` |   
  
### listMessageBusEnrollmentsPagedCallable()
    
    
    public UnaryCallable<ListMessageBusEnrollmentsRequest,EventarcClient.ListMessageBusEnrollmentsPagedResponse> listMessageBusEnrollmentsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusEnrollmentsRequest),[ListMessageBusEnrollmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListMessageBusEnrollmentsPagedResponse)>` |   
  
### listMessageBusesCallable()
    
    
    public UnaryCallable<ListMessageBusesRequest,ListMessageBusesResponse> listMessageBusesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessageBusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusesRequest),[ListMessageBusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusesResponse)>` |   
  
### listMessageBusesPagedCallable()
    
    
    public UnaryCallable<ListMessageBusesRequest,EventarcClient.ListMessageBusesPagedResponse> listMessageBusesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessageBusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusesRequest),[ListMessageBusesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListMessageBusesPagedResponse)>` |   
  
### listPipelinesCallable()
    
    
    public UnaryCallable<ListPipelinesRequest,ListPipelinesResponse> listPipelinesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListPipelinesRequest),[ListPipelinesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListPipelinesResponse)>` |   
  
### listPipelinesPagedCallable()
    
    
    public UnaryCallable<ListPipelinesRequest,EventarcClient.ListPipelinesPagedResponse> listPipelinesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListPipelinesRequest),[ListPipelinesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListPipelinesPagedResponse)>` |   
  
### listProvidersCallable()
    
    
    public UnaryCallable<ListProvidersRequest,ListProvidersResponse> listProvidersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListProvidersRequest),[ListProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListProvidersResponse)>` |   
  
### listProvidersPagedCallable()
    
    
    public UnaryCallable<ListProvidersRequest,EventarcClient.ListProvidersPagedResponse> listProvidersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListProvidersRequest),[ListProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListProvidersPagedResponse)>` |   
  
### listTriggersCallable()
    
    
    public UnaryCallable<ListTriggersRequest,ListTriggersResponse> listTriggersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListTriggersRequest),[ListTriggersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListTriggersResponse)>` |   
  
### listTriggersPagedCallable()
    
    
    public UnaryCallable<ListTriggersRequest,EventarcClient.ListTriggersPagedResponse> listTriggersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListTriggersRequest),[ListTriggersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcClient.ListTriggersPagedResponse)>` |   
  
### setIamPolicyCallable()
    
    
    public UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsCallable()
    
    
    public UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateChannelCallable()
    
    
    public UnaryCallable<UpdateChannelRequest,Operation> updateChannelCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateChannelOperationCallable()
    
    
    public OperationCallable<UpdateChannelRequest,Channel,OperationMetadata> updateChannelOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### updateEnrollmentCallable()
    
    
    public UnaryCallable<UpdateEnrollmentRequest,Operation> updateEnrollmentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateEnrollmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEnrollmentOperationCallable()
    
    
    public OperationCallable<UpdateEnrollmentRequest,Enrollment,OperationMetadata> updateEnrollmentOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateEnrollmentRequest),[Enrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Enrollment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### updateGoogleApiSourceCallable()
    
    
    public UnaryCallable<UpdateGoogleApiSourceRequest,Operation> updateGoogleApiSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateGoogleApiSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGoogleApiSourceOperationCallable()
    
    
    public OperationCallable<UpdateGoogleApiSourceRequest,GoogleApiSource,OperationMetadata> updateGoogleApiSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateGoogleApiSourceRequest),[GoogleApiSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleApiSource),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### updateGoogleChannelConfigCallable()
    
    
    public UnaryCallable<UpdateGoogleChannelConfigRequest,GoogleChannelConfig> updateGoogleChannelConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGoogleChannelConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateGoogleChannelConfigRequest),[GoogleChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleChannelConfig)>` |   
  
### updateMessageBusCallable()
    
    
    public UnaryCallable<UpdateMessageBusRequest,Operation> updateMessageBusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateMessageBusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMessageBusOperationCallable()
    
    
    public OperationCallable<UpdateMessageBusRequest,MessageBus,OperationMetadata> updateMessageBusOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateMessageBusRequest),[MessageBus](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.MessageBus),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### updatePipelineCallable()
    
    
    public UnaryCallable<UpdatePipelineRequest,Operation> updatePipelineCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdatePipelineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePipelineOperationCallable()
    
    
    public OperationCallable<UpdatePipelineRequest,Pipeline,OperationMetadata> updatePipelineOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdatePipelineRequest),[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Pipeline),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
### updateTriggerCallable()
    
    
    public UnaryCallable<UpdateTriggerRequest,Operation> updateTriggerCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateTriggerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTriggerOperationCallable()
    
    
    public OperationCallable<UpdateTriggerRequest,Trigger,OperationMetadata> updateTriggerOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateTriggerRequest),[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Trigger),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
