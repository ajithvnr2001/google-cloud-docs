---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryGrpc.AsyncService
title: Interface CloudApiRegistryGrpc.AsyncService (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:19.909740+00:00
---

# Interface CloudApiRegistryGrpc.AsyncService (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudApiRegistryGrpc.AsyncService (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public static interface CloudApiRegistryGrpc.AsyncService

The Cloud API Registry service provides a central registry for managing API Data.

## Methods 

### getMcpServer(GetMcpServerRequest request, StreamObserver<McpServer> responseObserver)
    
    
    public default void getMcpServer(GetMcpServerRequest request, StreamObserver<McpServer> responseObserver)

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpServerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)>`  
  
  
### getMcpTool(GetMcpToolRequest request, StreamObserver<McpTool> responseObserver)
    
    
    public default void getMcpTool(GetMcpToolRequest request, StreamObserver<McpTool> responseObserver)

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpToolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)>`  
  
  
### listMcpServers(ListMcpServersRequest request, StreamObserver<ListMcpServersResponse> responseObserver)
    
    
    public default void listMcpServers(ListMcpServersRequest request, StreamObserver<ListMcpServersResponse> responseObserver)

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersResponse)>`  
  
  
### listMcpTools(ListMcpToolsRequest request, StreamObserver<ListMcpToolsResponse> responseObserver)
    
    
    public default void listMcpTools(ListMcpToolsRequest request, StreamObserver<ListMcpToolsResponse> responseObserver)

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMcpToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
