---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.stub.CloudApiRegistryStub
title: Class CloudApiRegistryStub (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:22.181304+00:00
---

# Class CloudApiRegistryStub (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.stub.CloudApiRegistryStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudApiRegistryStub (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public abstract class CloudApiRegistryStub implements BackgroundResource

Base stub class for the CloudApiRegistry service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudApiRegistryStub

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

### CloudApiRegistryStub()
    
    
    public CloudApiRegistryStub()

## Methods 

### close()
    
    
    public abstract void close()

### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMcpServerCallable()
    
    
    public UnaryCallable<GetMcpServerRequest,McpServer> getMcpServerCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpServerRequest),[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)>` |   
  
### getMcpToolCallable()
    
    
    public UnaryCallable<GetMcpToolRequest,McpTool> getMcpToolCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMcpToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpToolRequest),[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,CloudApiRegistryClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListLocationsPagedResponse)>` |   
  
### listMcpServersCallable()
    
    
    public UnaryCallable<ListMcpServersRequest,ListMcpServersResponse> listMcpServersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest),[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersResponse)>` |   
  
### listMcpServersPagedCallable()
    
    
    public UnaryCallable<ListMcpServersRequest,CloudApiRegistryClient.ListMcpServersPagedResponse> listMcpServersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest),[ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpServersPagedResponse)>` |   
  
### listMcpToolsCallable()
    
    
    public UnaryCallable<ListMcpToolsRequest,ListMcpToolsResponse> listMcpToolsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest),[ListMcpToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsResponse)>` |   
  
### listMcpToolsPagedCallable()
    
    
    public UnaryCallable<ListMcpToolsRequest,CloudApiRegistryClient.ListMcpToolsPagedResponse> listMcpToolsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest),[ListMcpToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpToolsPagedResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
