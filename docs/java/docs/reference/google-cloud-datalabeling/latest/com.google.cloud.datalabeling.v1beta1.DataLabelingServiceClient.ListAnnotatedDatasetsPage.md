---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.DataLabelingServiceClient.ListAnnotatedDatasetsPage
title: Class DataLabelingServiceClient.ListAnnotatedDatasetsPage (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:12.276481+00:00
---

# Class DataLabelingServiceClient.ListAnnotatedDatasetsPage (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.DataLabelingServiceClient.ListAnnotatedDatasetsPage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataLabelingServiceClient.ListAnnotatedDatasetsPage (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public static class DataLabelingServiceClient.ListAnnotatedDatasetsPage extends AbstractPage<ListAnnotatedDatasetsRequest,ListAnnotatedDatasetsResponse,AnnotatedDataset,DataLabelingServiceClient.ListAnnotatedDatasetsPage>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html) > DataLabelingServiceClient.ListAnnotatedDatasetsPage

## Inherited Members

[AbstractPage.createPage(PageContext<RequestT,ResponseT,ResourceT>,ResponseT)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPage_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__ResponseT_)

[AbstractPage.createPageAsync(PageContext<RequestT,ResponseT,ResourceT>,ApiFuture<ResponseT>)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPageAsync_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__com_google_api_core_ApiFuture_ResponseT__)

[AbstractPage.getNextPage()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getNextPage__)

[AbstractPage.getNextPage(int)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getNextPage_int_)

[AbstractPage.getNextPageAsync()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getNextPageAsync__)

[AbstractPage.getNextPageToken()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getNextPageToken__)

[AbstractPage.getPageElementCount()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getPageElementCount__)

[AbstractPage.getRequest()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getRequest__)

[AbstractPage.getResponse()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getResponse__)

[AbstractPage.getValues()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_getValues__)

[AbstractPage.hasNextPage()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_hasNextPage__)

[AbstractPage.iterateAll()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_iterateAll__)

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

### createPage(@Nullable PageContext<ListAnnotatedDatasetsRequest,ListAnnotatedDatasetsResponse,AnnotatedDataset> context, @Nullable ListAnnotatedDatasetsResponse response)
    
    
    protected DataLabelingServiceClient.ListAnnotatedDatasetsPage createPage(@Nullable PageContext<ListAnnotatedDatasetsRequest,ListAnnotatedDatasetsResponse,AnnotatedDataset> context, @Nullable ListAnnotatedDatasetsResponse response)

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.PageContext<[ListAnnotatedDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsRequest),[ListAnnotatedDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse),[AnnotatedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDataset)>`  
  
`response` | `@org.jspecify.annotations.Nullable com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingServiceClient.ListAnnotatedDatasetsPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.DataLabelingServiceClient.ListAnnotatedDatasetsPage)` |   
**Overrides**

[AbstractPage<RequestT,ResponseT,ResourceT,PageT>.createPage(PageContext<RequestT,ResponseT,ResourceT> context, ResponseT response)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPage_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__ResponseT_)

### createPageAsync(@Nullable PageContext<ListAnnotatedDatasetsRequest,ListAnnotatedDatasetsResponse,AnnotatedDataset> context, ApiFuture<ListAnnotatedDatasetsResponse> futureResponse)
    
    
    public ApiFuture<DataLabelingServiceClient.ListAnnotatedDatasetsPage> createPageAsync(@Nullable PageContext<ListAnnotatedDatasetsRequest,ListAnnotatedDatasetsResponse,AnnotatedDataset> context, ApiFuture<ListAnnotatedDatasetsResponse> futureResponse)

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.PageContext<[ListAnnotatedDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsRequest),[ListAnnotatedDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse),[AnnotatedDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.AnnotatedDataset)>`  
  
`futureResponse` | `[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListAnnotatedDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListAnnotatedDatasetsPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.DataLabelingServiceClient.ListAnnotatedDatasetsPage)>` |   
**Overrides**

[AbstractPage<RequestT,ResponseT,ResourceT,PageT>.createPageAsync(PageContext<RequestT,ResponseT,ResourceT> context, ApiFuture<ResponseT> futureResponse)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPageAsync_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__com_google_api_core_ApiFuture_ResponseT__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
