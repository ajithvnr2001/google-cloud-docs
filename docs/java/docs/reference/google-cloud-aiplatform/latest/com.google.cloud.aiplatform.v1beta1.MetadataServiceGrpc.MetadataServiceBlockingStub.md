---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataServiceGrpc.MetadataServiceBlockingStub
title: Class MetadataServiceGrpc.MetadataServiceBlockingStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:38.245301+00:00
---

# Class MetadataServiceGrpc.MetadataServiceBlockingStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataServiceGrpc.MetadataServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetadataServiceGrpc.MetadataServiceBlockingStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class MetadataServiceGrpc.MetadataServiceBlockingStub extends AbstractBlockingStub<MetadataServiceGrpc.MetadataServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service MetadataService.

Service for reading and writing metadata entries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > MetadataServiceGrpc.MetadataServiceBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request)
    
    
    public AddContextArtifactsAndExecutionsResponse addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request)

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextArtifactsAndExecutionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextArtifactsAndExecutionsResponse)` |   
  
### addContextChildren(AddContextChildrenRequest request)
    
    
    public AddContextChildrenResponse addContextChildren(AddContextChildrenRequest request)

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextChildrenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddContextChildrenResponse)` |   
  
### addExecutionEvents(AddExecutionEventsRequest request)
    
    
    public AddExecutionEventsResponse addExecutionEvents(AddExecutionEventsRequest request)

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddExecutionEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddExecutionEventsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.AddExecutionEventsResponse)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected MetadataServiceGrpc.MetadataServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataServiceGrpc.MetadataServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataServiceGrpc.MetadataServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createArtifact(CreateArtifactRequest request)
    
    
    public Artifact createArtifact(CreateArtifactRequest request)

Creates an Artifact associated with a MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateArtifactRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Artifact)` |   
  
### createContext(CreateContextRequest request)
    
    
    public Context createContext(CreateContextRequest request)

Creates a Context associated with a MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateContextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Context)` |   
  
### createExecution(CreateExecutionRequest request)
    
    
    public Execution createExecution(CreateExecutionRequest request)

Creates an Execution associated with a MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateExecutionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Execution)` |   
  
### createMetadataSchema(CreateMetadataSchemaRequest request)
    
    
    public MetadataSchema createMetadataSchema(CreateMetadataSchemaRequest request)

Creates a MetadataSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateMetadataSchemaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataSchema)` |   
  
### createMetadataStore(CreateMetadataStoreRequest request)
    
    
    public Operation createMetadataStore(CreateMetadataStoreRequest request)

Initializes a MetadataStore, including allocation of resources.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateMetadataStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteArtifact(DeleteArtifactRequest request)
    
    
    public Operation deleteArtifact(DeleteArtifactRequest request)

Deletes an Artifact.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteArtifactRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteContext(DeleteContextRequest request)
    
    
    public Operation deleteContext(DeleteContextRequest request)

Deletes a stored Context.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteContextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteExecution(DeleteExecutionRequest request)
    
    
    public Operation deleteExecution(DeleteExecutionRequest request)

Deletes an Execution.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteExecutionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteMetadataStore(DeleteMetadataStoreRequest request)
    
    
    public Operation deleteMetadataStore(DeleteMetadataStoreRequest request)

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteMetadataStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getArtifact(GetArtifactRequest request)
    
    
    public Artifact getArtifact(GetArtifactRequest request)

Retrieves a specific Artifact.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetArtifactRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Artifact)` |   
  
### getContext(GetContextRequest request)
    
    
    public Context getContext(GetContextRequest request)

Retrieves a specific Context.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetContextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Context)` |   
  
### getExecution(GetExecutionRequest request)
    
    
    public Execution getExecution(GetExecutionRequest request)

Retrieves a specific Execution.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetExecutionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Execution)` |   
  
### getMetadataSchema(GetMetadataSchemaRequest request)
    
    
    public MetadataSchema getMetadataSchema(GetMetadataSchemaRequest request)

Retrieves a specific MetadataSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetMetadataSchemaRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataSchema)` |   
  
### getMetadataStore(GetMetadataStoreRequest request)
    
    
    public MetadataStore getMetadataStore(GetMetadataStoreRequest request)

Retrieves a specific MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetMetadataStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.MetadataStore)` |   
  
### listArtifacts(ListArtifactsRequest request)
    
    
    public ListArtifactsResponse listArtifacts(ListArtifactsRequest request)

Lists Artifacts in the MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListArtifactsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListArtifactsResponse)` |   
  
### listContexts(ListContextsRequest request)
    
    
    public ListContextsResponse listContexts(ListContextsRequest request)

Lists Contexts on the MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListContextsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListContextsResponse)` |   
  
### listExecutions(ListExecutionsRequest request)
    
    
    public ListExecutionsResponse listExecutions(ListExecutionsRequest request)

Lists Executions in the MetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListExecutionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListExecutionsResponse)` |   
  
### listMetadataSchemas(ListMetadataSchemasRequest request)
    
    
    public ListMetadataSchemasResponse listMetadataSchemas(ListMetadataSchemasRequest request)

Lists MetadataSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListMetadataSchemasRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMetadataSchemasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListMetadataSchemasResponse)` |   
  
### listMetadataStores(ListMetadataStoresRequest request)
    
    
    public ListMetadataStoresResponse listMetadataStores(ListMetadataStoresRequest request)

Lists MetadataStores for a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListMetadataStoresRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMetadataStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListMetadataStoresResponse)` |   
  
### purgeArtifacts(PurgeArtifactsRequest request)
    
    
    public Operation purgeArtifacts(PurgeArtifactsRequest request)

Purges Artifacts.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.PurgeArtifactsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### purgeContexts(PurgeContextsRequest request)
    
    
    public Operation purgeContexts(PurgeContextsRequest request)

Purges Contexts.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.PurgeContextsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### purgeExecutions(PurgeExecutionsRequest request)
    
    
    public Operation purgeExecutions(PurgeExecutionsRequest request)

Purges Executions.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.PurgeExecutionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request)
    
    
    public LineageSubgraph queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request)

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.QueryArtifactLineageSubgraphRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.LineageSubgraph)` |   
  
### queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request)
    
    
    public LineageSubgraph queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request)

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.QueryContextLineageSubgraphRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.LineageSubgraph)` |   
  
### queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request)
    
    
    public LineageSubgraph queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request)

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.QueryExecutionInputsAndOutputsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.LineageSubgraph)` |   
  
### removeContextChildren(RemoveContextChildrenRequest request)
    
    
    public RemoveContextChildrenResponse removeContextChildren(RemoveContextChildrenRequest request)

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RemoveContextChildrenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RemoveContextChildrenResponse)` |   
  
### updateArtifact(UpdateArtifactRequest request)
    
    
    public Artifact updateArtifact(UpdateArtifactRequest request)

Updates a stored Artifact.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateArtifactRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Artifact)` |   
  
### updateContext(UpdateContextRequest request)
    
    
    public Context updateContext(UpdateContextRequest request)

Updates a stored Context.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateContextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Context)` |   
  
### updateExecution(UpdateExecutionRequest request)
    
    
    public Execution updateExecution(UpdateExecutionRequest request)

Updates a stored Execution.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateExecutionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Execution)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
