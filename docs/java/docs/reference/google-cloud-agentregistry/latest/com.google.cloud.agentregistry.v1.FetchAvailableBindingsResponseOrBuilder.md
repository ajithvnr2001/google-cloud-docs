---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsResponseOrBuilder
title: Interface FetchAvailableBindingsResponseOrBuilder (0.6.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:37.915235+00:00
---

# Interface FetchAvailableBindingsResponseOrBuilder (0.6.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FetchAvailableBindingsResponseOrBuilder (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.2.0  0.1.0 
    
    
    public interface FetchAvailableBindingsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBindings(int index)
    
    
    public abstract Binding getBindings(int index)

The list of Bindings.

`repeated .google.cloud.agentregistry.v1.Binding bindings = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)` |   
  
### getBindingsCount()
    
    
    public abstract int getBindingsCount()

The list of Bindings.

`repeated .google.cloud.agentregistry.v1.Binding bindings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBindingsList()
    
    
    public abstract List<Binding> getBindingsList()

The list of Bindings.

`repeated .google.cloud.agentregistry.v1.Binding bindings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)>` |   
  
### getBindingsOrBuilder(int index)
    
    
    public abstract BindingOrBuilder getBindingsOrBuilder(int index)

The list of Bindings.

`repeated .google.cloud.agentregistry.v1.Binding bindings = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.BindingOrBuilder)` |   
  
### getBindingsOrBuilderList()
    
    
    public abstract List<? extends BindingOrBuilder> getBindingsOrBuilderList()

The list of Bindings.

`repeated .google.cloud.agentregistry.v1.Binding bindings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.agentregistry.v1.BindingOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
