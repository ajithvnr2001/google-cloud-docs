---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsResponseOrBuilder
title: Interface ListToolsetsResponseOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:11.092418+00:00
---

# Interface ListToolsetsResponseOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListToolsetsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListToolsetsResponseOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ListToolsetsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token that can be sent as ListToolsetsRequest.page_token to retrieve the next page. Absence of this field indicates there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token that can be sent as ListToolsetsRequest.page_token to retrieve the next page. Absence of this field indicates there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getToolsets(int index)
    
    
    public abstract Toolset getToolsets(int index)

The list of toolsets.

`repeated .google.cloud.ces.v1beta.Toolset toolsets = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)` |   
  
### getToolsetsCount()
    
    
    public abstract int getToolsetsCount()

The list of toolsets.

`repeated .google.cloud.ces.v1beta.Toolset toolsets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getToolsetsList()
    
    
    public abstract List<Toolset> getToolsetsList()

The list of toolsets.

`repeated .google.cloud.ces.v1beta.Toolset toolsets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Toolset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Toolset)>` |   
  
### getToolsetsOrBuilder(int index)
    
    
    public abstract ToolsetOrBuilder getToolsetsOrBuilder(int index)

The list of toolsets.

`repeated .google.cloud.ces.v1beta.Toolset toolsets = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ToolsetOrBuilder)` |   
  
### getToolsetsOrBuilderList()
    
    
    public abstract List<? extends ToolsetOrBuilder> getToolsetsOrBuilderList()

The list of toolsets.

`repeated .google.cloud.ces.v1beta.Toolset toolsets = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.ces.v1beta.ToolsetOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
