---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.SearchBlueprintRevisionsResponseOrBuilder
title: Interface SearchBlueprintRevisionsResponseOrBuilder (0.69.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:47.804547+00:00
---

# Interface SearchBlueprintRevisionsResponseOrBuilder (0.69.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.SearchBlueprintRevisionsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchBlueprintRevisionsResponseOrBuilder (0.69.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.69.0 (latest)  0.65.0  0.64.0  0.63.0  0.61.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.50.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface SearchBlueprintRevisionsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBlueprints(int index)
    
    
    public abstract Blueprint getBlueprints(int index)

The list of requested blueprint revisions.

`repeated .google.cloud.telcoautomation.v1alpha1.Blueprint blueprints = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Blueprint](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.Blueprint)` |   
  
### getBlueprintsCount()
    
    
    public abstract int getBlueprintsCount()

The list of requested blueprint revisions.

`repeated .google.cloud.telcoautomation.v1alpha1.Blueprint blueprints = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBlueprintsList()
    
    
    public abstract List<Blueprint> getBlueprintsList()

The list of requested blueprint revisions.

`repeated .google.cloud.telcoautomation.v1alpha1.Blueprint blueprints = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Blueprint](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.Blueprint)>` |   
  
### getBlueprintsOrBuilder(int index)
    
    
    public abstract BlueprintOrBuilder getBlueprintsOrBuilder(int index)

The list of requested blueprint revisions.

`repeated .google.cloud.telcoautomation.v1alpha1.Blueprint blueprints = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlueprintOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-telcoautomation/latest/com.google.cloud.telcoautomation.v1alpha1.BlueprintOrBuilder)` |   
  
### getBlueprintsOrBuilderList()
    
    
    public abstract List<? extends BlueprintOrBuilder> getBlueprintsOrBuilderList()

The list of requested blueprint revisions.

`repeated .google.cloud.telcoautomation.v1alpha1.Blueprint blueprints = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.telcoautomation.v1alpha1.BlueprintOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
