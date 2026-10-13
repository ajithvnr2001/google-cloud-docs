---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterClient.ListClustersPage
title: Class CloudRedisClusterClient.ListClustersPage (0.71.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:32.979066+00:00
---

# Class CloudRedisClusterClient.ListClustersPage (0.71.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterClient.ListClustersPage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudRedisClusterClient.ListClustersPage (0.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.71.0 (latest)  0.67.0  0.66.0  0.65.0  0.63.0  0.60.0  0.59.0  0.57.0  0.55.0  0.54.0  0.52.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static class CloudRedisClusterClient.ListClustersPage extends AbstractPage<ListClustersRequest,ListClustersResponse,Cluster,CloudRedisClusterClient.ListClustersPage>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html) > CloudRedisClusterClient.ListClustersPage

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

### createPage(@Nullable PageContext<ListClustersRequest,ListClustersResponse,Cluster> context, @Nullable ListClustersResponse response)
    
    
    protected CloudRedisClusterClient.ListClustersPage createPage(@Nullable PageContext<ListClustersRequest,ListClustersResponse,Cluster> context, @Nullable ListClustersResponse response)

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.PageContext<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersResponse),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.Cluster)>`  
  
`response` | `@org.jspecify.annotations.Nullable com.google.cloud.redis.cluster.v1beta1.ListClustersResponse`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudRedisClusterClient.ListClustersPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterClient.ListClustersPage)` |   
**Overrides**

[AbstractPage<RequestT,ResponseT,ResourceT,PageT>.createPage(PageContext<RequestT,ResponseT,ResourceT> context, ResponseT response)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPage_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__ResponseT_)

### createPageAsync(@Nullable PageContext<ListClustersRequest,ListClustersResponse,Cluster> context, ApiFuture<ListClustersResponse> futureResponse)
    
    
    public ApiFuture<CloudRedisClusterClient.ListClustersPage> createPageAsync(@Nullable PageContext<ListClustersRequest,ListClustersResponse,Cluster> context, ApiFuture<ListClustersResponse> futureResponse)

**Parameters**  
---  
**Name** | **Description**  
`context` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.PageContext<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersResponse),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.Cluster)>`  
  
`futureResponse` | `[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ListClustersResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListClustersPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.CloudRedisClusterClient.ListClustersPage)>` |   
**Overrides**

[AbstractPage<RequestT,ResponseT,ResourceT,PageT>.createPageAsync(PageContext<RequestT,ResponseT,ResourceT> context, ApiFuture<ResponseT> futureResponse)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AbstractPage.html#com_google_api_gax_paging_AbstractPage_createPageAsync_com_google_api_gax_rpc_PageContext_RequestT_ResponseT_ResourceT__com_google_api_core_ApiFuture_ResponseT__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
