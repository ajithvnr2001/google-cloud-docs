---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.GroupAssetsResponseOrBuilder
title: Interface GroupAssetsResponseOrBuilder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:48.890811+00:00
---

# Interface GroupAssetsResponseOrBuilder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.GroupAssetsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GroupAssetsResponseOrBuilder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public interface GroupAssetsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getGroupByResults(int index)
    
    
    public abstract GroupResult getGroupByResults(int index)

Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.

`repeated .google.cloud.securitycenter.v1beta1.GroupResult group_by_results = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroupResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.GroupResult)` |   
  
### getGroupByResultsCount()
    
    
    public abstract int getGroupByResultsCount()

Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.

`repeated .google.cloud.securitycenter.v1beta1.GroupResult group_by_results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGroupByResultsList()
    
    
    public abstract List<GroupResult> getGroupByResultsList()

Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.

`repeated .google.cloud.securitycenter.v1beta1.GroupResult group_by_results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GroupResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.GroupResult)>` |   
  
### getGroupByResultsOrBuilder(int index)
    
    
    public abstract GroupResultOrBuilder getGroupByResultsOrBuilder(int index)

Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.

`repeated .google.cloud.securitycenter.v1beta1.GroupResult group_by_results = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroupResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.GroupResultOrBuilder)` |   
  
### getGroupByResultsOrBuilderList()
    
    
    public abstract List<? extends GroupResultOrBuilder> getGroupByResultsOrBuilderList()

Group results. There exists an element for each existing unique combination of property/values. The element contains a count for the number of times those specific property/values appear.

`repeated .google.cloud.securitycenter.v1beta1.GroupResult group_by_results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.securitycenter.v1beta1.GroupResultOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

Token to retrieve the next page of results, or empty if there are no more results.

`string next_page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

Token to retrieve the next page of results, or empty if there are no more results.

`string next_page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getReadTime()
    
    
    public abstract Timestamp getReadTime()

Time used for executing the groupBy request.

`.google.protobuf.Timestamp read_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The readTime.  
  
### getReadTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getReadTimeOrBuilder()

Time used for executing the groupBy request.

`.google.protobuf.Timestamp read_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasReadTime()
    
    
    public abstract boolean hasReadTime()

Time used for executing the groupBy request.

`.google.protobuf.Timestamp read_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
