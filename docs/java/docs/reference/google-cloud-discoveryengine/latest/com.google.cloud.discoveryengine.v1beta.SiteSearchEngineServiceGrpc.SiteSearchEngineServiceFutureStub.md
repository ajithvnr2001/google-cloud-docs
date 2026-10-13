---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub
title: Class SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:34.807698+00:00
---

# Class SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub extends AbstractFutureStub<SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service SiteSearchEngineService.

Service for managing site search related resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

### batchCreateTargetSites(BatchCreateTargetSitesRequest request)
    
    
    public ListenableFuture<Operation> batchCreateTargetSites(BatchCreateTargetSitesRequest request)

Creates TargetSite in a batch.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.BatchCreateTargetSitesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchVerifyTargetSites(BatchVerifyTargetSitesRequest request)
    
    
    public ListenableFuture<Operation> batchVerifyTargetSites(BatchVerifyTargetSitesRequest request)

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SiteSearchEngineServiceGrpc.SiteSearchEngineServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createSitemap(CreateSitemapRequest request)
    
    
    public ListenableFuture<Operation> createSitemap(CreateSitemapRequest request)

Creates a Sitemap.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CreateSitemapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTargetSite(CreateTargetSiteRequest request)
    
    
    public ListenableFuture<Operation> createTargetSite(CreateTargetSiteRequest request)

Creates a TargetSite.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CreateTargetSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSitemap(DeleteSitemapRequest request)
    
    
    public ListenableFuture<Operation> deleteSitemap(DeleteSitemapRequest request)

Deletes a Sitemap.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.DeleteSitemapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTargetSite(DeleteTargetSiteRequest request)
    
    
    public ListenableFuture<Operation> deleteTargetSite(DeleteTargetSiteRequest request)

Deletes a TargetSite.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.DeleteTargetSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disableAdvancedSiteSearch(DisableAdvancedSiteSearchRequest request)
    
    
    public ListenableFuture<Operation> disableAdvancedSiteSearch(DisableAdvancedSiteSearchRequest request)

Downgrade from advanced site search to basic site search.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enableAdvancedSiteSearch(EnableAdvancedSiteSearchRequest request)
    
    
    public ListenableFuture<Operation> enableAdvancedSiteSearch(EnableAdvancedSiteSearchRequest request)

Upgrade from basic site search to advanced site search.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### fetchDomainVerificationStatus(FetchDomainVerificationStatusRequest request)
    
    
    public ListenableFuture<FetchDomainVerificationStatusResponse> fetchDomainVerificationStatus(FetchDomainVerificationStatusRequest request)

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.FetchDomainVerificationStatusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.FetchDomainVerificationStatusResponse)>` |   
  
### fetchSitemaps(FetchSitemapsRequest request)
    
    
    public ListenableFuture<FetchSitemapsResponse> fetchSitemaps(FetchSitemapsRequest request)

Fetch Sitemaps in a DataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchSitemapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.FetchSitemapsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[FetchSitemapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.FetchSitemapsResponse)>` |   
  
### getSiteSearchEngine(GetSiteSearchEngineRequest request)
    
    
    public ListenableFuture<SiteSearchEngine> getSiteSearchEngine(GetSiteSearchEngineRequest request)

Gets the SiteSearchEngine.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSiteSearchEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.GetSiteSearchEngineRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SiteSearchEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SiteSearchEngine)>` |   
  
### getTargetSite(GetTargetSiteRequest request)
    
    
    public ListenableFuture<TargetSite> getTargetSite(GetTargetSiteRequest request)

Gets a TargetSite.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.GetTargetSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.TargetSite)>` |   
  
### listTargetSites(ListTargetSitesRequest request)
    
    
    public ListenableFuture<ListTargetSitesResponse> listTargetSites(ListTargetSitesRequest request)

Gets a list of TargetSites.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ListTargetSitesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ListTargetSitesResponse)>` |   
  
### recrawlUris(RecrawlUrisRequest request)
    
    
    public ListenableFuture<Operation> recrawlUris(RecrawlUrisRequest request)

Request on-demand recrawl for a list of URIs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecrawlUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.RecrawlUrisRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTargetSite(UpdateTargetSiteRequest request)
    
    
    public ListenableFuture<Operation> updateTargetSite(UpdateTargetSiteRequest request)

Updates a TargetSite.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UpdateTargetSiteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
