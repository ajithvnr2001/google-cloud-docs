---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResultsOrBuilder
title: Interface ProductSearchResultsOrBuilder (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:07.396757+00:00
---

# Interface ProductSearchResultsOrBuilder (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResultsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductSearchResultsOrBuilder (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.3  2.1.4  2.0.29 
    
    
    public interface ProductSearchResultsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIndexTime()
    
    
    public abstract Timestamp getIndexTime()

Timestamp of the index which provided these results. Products added to the product set and products removed from the product set after this time are not reflected in the current results.

`.google.protobuf.Timestamp index_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The indexTime.  
  
### getIndexTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getIndexTimeOrBuilder()

Timestamp of the index which provided these results. Products added to the product set and products removed from the product set after this time are not reflected in the current results.

`.google.protobuf.Timestamp index_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getProductGroupedResults(int index)
    
    
    public abstract ProductSearchResults.GroupedResult getProductGroupedResults(int index)

List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results.

` repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult product_grouped_results = 6; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchResults.GroupedResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult)` |   
  
### getProductGroupedResultsCount()
    
    
    public abstract int getProductGroupedResultsCount()

List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results.

` repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult product_grouped_results = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getProductGroupedResultsList()
    
    
    public abstract List<ProductSearchResults.GroupedResult> getProductGroupedResultsList()

List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results.

` repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult product_grouped_results = 6; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GroupedResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult)>` |   
  
### getProductGroupedResultsOrBuilder(int index)
    
    
    public abstract ProductSearchResults.GroupedResultOrBuilder getProductGroupedResultsOrBuilder(int index)

List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results.

` repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult product_grouped_results = 6; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchResults.GroupedResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResultOrBuilder)` |   
  
### getProductGroupedResultsOrBuilderList()
    
    
    public abstract List<? extends ProductSearchResults.GroupedResultOrBuilder> getProductGroupedResultsOrBuilderList()

List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results.

` repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult product_grouped_results = 6; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResultOrBuilder>` |   
  
### getResults(int index)
    
    
    public abstract ProductSearchResults.Result getResults(int index)

List of results, one for each product match.

`repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.Result results = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchResults.Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.Result)` |   
  
### getResultsCount()
    
    
    public abstract int getResultsCount()

List of results, one for each product match.

`repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.Result results = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResultsList()
    
    
    public abstract List<ProductSearchResults.Result> getResultsList()

List of results, one for each product match.

`repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.Result results = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.Result)>` |   
  
### getResultsOrBuilder(int index)
    
    
    public abstract ProductSearchResults.ResultOrBuilder getResultsOrBuilder(int index)

List of results, one for each product match.

`repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.Result results = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchResults.ResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchResults.ResultOrBuilder)` |   
  
### getResultsOrBuilderList()
    
    
    public abstract List<? extends ProductSearchResults.ResultOrBuilder> getResultsOrBuilderList()

List of results, one for each product match.

`repeated .google.cloud.vision.v1p4beta1.ProductSearchResults.Result results = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vision.v1p4beta1.ProductSearchResults.ResultOrBuilder>` |   
  
### hasIndexTime()
    
    
    public abstract boolean hasIndexTime()

Timestamp of the index which provided these results. Products added to the product set and products removed from the product set after this time are not reflected in the current results.

`.google.protobuf.Timestamp index_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the indexTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
