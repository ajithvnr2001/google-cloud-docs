---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceGrpc.AsyncService
title: Interface MetadataServiceGrpc.AsyncService (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:40.174939+00:00
---

# Interface MetadataServiceGrpc.AsyncService (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MetadataServiceGrpc.AsyncService (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface MetadataServiceGrpc.AsyncService

Service for reading and writing metadata entries.

## Methods 

### addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request, StreamObserver<AddContextArtifactsAndExecutionsResponse> responseObserver)
    
    
    public default void addContextArtifactsAndExecutions(AddContextArtifactsAndExecutionsRequest request, StreamObserver<AddContextArtifactsAndExecutionsResponse> responseObserver)

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse)>`  
  
  
### addContextChildren(AddContextChildrenRequest request, StreamObserver<AddContextChildrenResponse> responseObserver)
    
    
    public default void addContextChildren(AddContextChildrenRequest request, StreamObserver<AddContextChildrenResponse> responseObserver)

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AddContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddContextChildrenResponse)>`  
  
  
### addExecutionEvents(AddExecutionEventsRequest request, StreamObserver<AddExecutionEventsResponse> responseObserver)
    
    
    public default void addExecutionEvents(AddExecutionEventsRequest request, StreamObserver<AddExecutionEventsResponse> responseObserver)

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddExecutionEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AddExecutionEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddExecutionEventsResponse)>`  
  
  
### createArtifact(CreateArtifactRequest request, StreamObserver<Artifact> responseObserver)
    
    
    public default void createArtifact(CreateArtifactRequest request, StreamObserver<Artifact> responseObserver)

Creates an Artifact associated with a MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateArtifactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>`  
  
  
### createContext(CreateContextRequest request, StreamObserver<Context> responseObserver)
    
    
    public default void createContext(CreateContextRequest request, StreamObserver<Context> responseObserver)

Creates a Context associated with a MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateContextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>`  
  
  
### createExecution(CreateExecutionRequest request, StreamObserver<Execution> responseObserver)
    
    
    public default void createExecution(CreateExecutionRequest request, StreamObserver<Execution> responseObserver)

Creates an Execution associated with a MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>`  
  
  
### createMetadataSchema(CreateMetadataSchemaRequest request, StreamObserver<MetadataSchema> responseObserver)
    
    
    public default void createMetadataSchema(CreateMetadataSchemaRequest request, StreamObserver<MetadataSchema> responseObserver)

Creates a MetadataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataSchemaRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)>`  
  
  
### createMetadataStore(CreateMetadataStoreRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createMetadataStore(CreateMetadataStoreRequest request, StreamObserver<Operation> responseObserver)

Initializes a MetadataStore, including allocation of resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateMetadataStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteArtifact(DeleteArtifactRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteArtifact(DeleteArtifactRequest request, StreamObserver<Operation> responseObserver)

Deletes an Artifact.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteArtifactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteContext(DeleteContextRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteContext(DeleteContextRequest request, StreamObserver<Operation> responseObserver)

Deletes a stored Context.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteContextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteExecution(DeleteExecutionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteExecution(DeleteExecutionRequest request, StreamObserver<Operation> responseObserver)

Deletes an Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMetadataStore(DeleteMetadataStoreRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteMetadataStore(DeleteMetadataStoreRequest request, StreamObserver<Operation> responseObserver)

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteMetadataStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getArtifact(GetArtifactRequest request, StreamObserver<Artifact> responseObserver)
    
    
    public default void getArtifact(GetArtifactRequest request, StreamObserver<Artifact> responseObserver)

Retrieves a specific Artifact.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetArtifactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>`  
  
  
### getContext(GetContextRequest request, StreamObserver<Context> responseObserver)
    
    
    public default void getContext(GetContextRequest request, StreamObserver<Context> responseObserver)

Retrieves a specific Context.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetContextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>`  
  
  
### getExecution(GetExecutionRequest request, StreamObserver<Execution> responseObserver)
    
    
    public default void getExecution(GetExecutionRequest request, StreamObserver<Execution> responseObserver)

Retrieves a specific Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>`  
  
  
### getMetadataSchema(GetMetadataSchemaRequest request, StreamObserver<MetadataSchema> responseObserver)
    
    
    public default void getMetadataSchema(GetMetadataSchemaRequest request, StreamObserver<MetadataSchema> responseObserver)

Retrieves a specific MetadataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataSchemaRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MetadataSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataSchema)>`  
  
  
### getMetadataStore(GetMetadataStoreRequest request, StreamObserver<MetadataStore> responseObserver)
    
    
    public default void getMetadataStore(GetMetadataStoreRequest request, StreamObserver<MetadataStore> responseObserver)

Retrieves a specific MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetMetadataStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MetadataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetadataStore)>`  
  
  
### listArtifacts(ListArtifactsRequest request, StreamObserver<ListArtifactsResponse> responseObserver)
    
    
    public default void listArtifacts(ListArtifactsRequest request, StreamObserver<ListArtifactsResponse> responseObserver)

Lists Artifacts in the MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListArtifactsResponse)>`  
  
  
### listContexts(ListContextsRequest request, StreamObserver<ListContextsResponse> responseObserver)
    
    
    public default void listContexts(ListContextsRequest request, StreamObserver<ListContextsResponse> responseObserver)

Lists Contexts on the MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListContextsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListContextsResponse)>`  
  
  
### listExecutions(ListExecutionsRequest request, StreamObserver<ListExecutionsResponse> responseObserver)
    
    
    public default void listExecutions(ListExecutionsRequest request, StreamObserver<ListExecutionsResponse> responseObserver)

Lists Executions in the MetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListExecutionsResponse)>`  
  
  
### listMetadataSchemas(ListMetadataSchemasRequest request, StreamObserver<ListMetadataSchemasResponse> responseObserver)
    
    
    public default void listMetadataSchemas(ListMetadataSchemasRequest request, StreamObserver<ListMetadataSchemasResponse> responseObserver)

Lists MetadataSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMetadataSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMetadataSchemasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataSchemasResponse)>`  
  
  
### listMetadataStores(ListMetadataStoresRequest request, StreamObserver<ListMetadataStoresResponse> responseObserver)
    
    
    public default void listMetadataStores(ListMetadataStoresRequest request, StreamObserver<ListMetadataStoresResponse> responseObserver)

Lists MetadataStores for a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMetadataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMetadataStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListMetadataStoresResponse)>`  
  
  
### purgeArtifacts(PurgeArtifactsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void purgeArtifacts(PurgeArtifactsRequest request, StreamObserver<Operation> responseObserver)

Purges Artifacts.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeArtifactsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### purgeContexts(PurgeContextsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void purgeContexts(PurgeContextsRequest request, StreamObserver<Operation> responseObserver)

Purges Contexts.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeContextsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeContextsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### purgeExecutions(PurgeExecutionsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void purgeExecutions(PurgeExecutionsRequest request, StreamObserver<Operation> responseObserver)

Purges Executions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PurgeExecutionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request, StreamObserver<LineageSubgraph> responseObserver)
    
    
    public default void queryArtifactLineageSubgraph(QueryArtifactLineageSubgraphRequest request, StreamObserver<LineageSubgraph> responseObserver)

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryArtifactLineageSubgraphRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>`  
  
  
### queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request, StreamObserver<LineageSubgraph> responseObserver)
    
    
    public default void queryContextLineageSubgraph(QueryContextLineageSubgraphRequest request, StreamObserver<LineageSubgraph> responseObserver)

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryContextLineageSubgraphRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>`  
  
  
### queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request, StreamObserver<LineageSubgraph> responseObserver)
    
    
    public default void queryExecutionInputsAndOutputs(QueryExecutionInputsAndOutputsRequest request, StreamObserver<LineageSubgraph> responseObserver)

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryExecutionInputsAndOutputsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LineageSubgraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LineageSubgraph)>`  
  
  
### removeContextChildren(RemoveContextChildrenRequest request, StreamObserver<RemoveContextChildrenResponse> responseObserver)
    
    
    public default void removeContextChildren(RemoveContextChildrenRequest request, StreamObserver<RemoveContextChildrenResponse> responseObserver)

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveContextChildrenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RemoveContextChildrenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RemoveContextChildrenResponse)>`  
  
  
### updateArtifact(UpdateArtifactRequest request, StreamObserver<Artifact> responseObserver)
    
    
    public default void updateArtifact(UpdateArtifactRequest request, StreamObserver<Artifact> responseObserver)

Updates a stored Artifact.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateArtifactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateArtifactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Artifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Artifact)>`  
  
  
### updateContext(UpdateContextRequest request, StreamObserver<Context> responseObserver)
    
    
    public default void updateContext(UpdateContextRequest request, StreamObserver<Context> responseObserver)

Updates a stored Context.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateContextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Context)>`  
  
  
### updateExecution(UpdateExecutionRequest request, StreamObserver<Execution> responseObserver)
    
    
    public default void updateExecution(UpdateExecutionRequest request, StreamObserver<Execution> responseObserver)

Updates a stored Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Execution)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
