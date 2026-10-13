---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.CaseServiceClient.SearchCaseClassificationsFixedSizeCollection
title: Class CaseServiceClient.SearchCaseClassificationsFixedSizeCollection (0.83.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:03.136431+00:00
---

# Class CaseServiceClient.SearchCaseClassificationsFixedSizeCollection (0.83.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.CaseServiceClient.SearchCaseClassificationsFixedSizeCollection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CaseServiceClient.SearchCaseClassificationsFixedSizeCollection (0.83.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.83.0 (latest)  0.79.0  0.78.0  0.77.0  0.75.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.54.0  0.52.0  0.51.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static class CaseServiceClient.SearchCaseClassificationsFixedSizeCollection extends AbstractFixedSizeCollection<SearchCaseClassificationsRequest,SearchCaseClassificationsResponse,CaseClassification,CaseServiceClient.SearchCaseClassificationsPage,CaseServiceClient.SearchCaseClassificationsFixedSizeCollection>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractFixedSizeCollection](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html) > CaseServiceClient.SearchCaseClassificationsFixedSizeCollection

## Inherited Members

[AbstractFixedSizeCollection.createCollection(List<PageT>,int)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_createCollection_java_util_List_PageT__int_)

[AbstractFixedSizeCollection.getCollectionSize()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_getCollectionSize__)

[AbstractFixedSizeCollection.getNextCollection()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_getNextCollection__)

[AbstractFixedSizeCollection.getNextPageToken()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_getNextPageToken__)

[AbstractFixedSizeCollection.getValues()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_getValues__)

[AbstractFixedSizeCollection.hasNextCollection()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_hasNextCollection__)

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

### createCollection(@Nullable List<CaseServiceClient.SearchCaseClassificationsPage> pages, int collectionSize)
    
    
    protected CaseServiceClient.SearchCaseClassificationsFixedSizeCollection createCollection(@Nullable List<CaseServiceClient.SearchCaseClassificationsPage> pages, int collectionSize)

**Parameters**  
---  
**Name** | **Description**  
`pages` | `@org.jspecify.annotations.Nullable java.util.List<[SearchCaseClassificationsPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.CaseServiceClient.SearchCaseClassificationsPage)>`  
  
`collectionSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaseServiceClient.SearchCaseClassificationsFixedSizeCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.CaseServiceClient.SearchCaseClassificationsFixedSizeCollection)` |   
**Overrides**

[AbstractFixedSizeCollection<RequestT,ResponseT,ResourceT,PageT,CollectionT>.createCollection(List<PageT> pages, int collectionSize)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractFixedSizeCollection.html#com_google_api_gax_paging_AbstractFixedSizeCollection_createCollection_java_util_List_PageT__int_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
