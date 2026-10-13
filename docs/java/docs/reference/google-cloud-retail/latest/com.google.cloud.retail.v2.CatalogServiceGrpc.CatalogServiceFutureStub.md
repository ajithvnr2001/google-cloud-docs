---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceGrpc.CatalogServiceFutureStub
title: Class CatalogServiceGrpc.CatalogServiceFutureStub (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:06.876460+00:00
---

# Class CatalogServiceGrpc.CatalogServiceFutureStub (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceGrpc.CatalogServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CatalogServiceGrpc.CatalogServiceFutureStub (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public static final class CatalogServiceGrpc.CatalogServiceFutureStub extends AbstractFutureStub<CatalogServiceGrpc.CatalogServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service CatalogService.

Service for managing catalog configuration.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > CatalogServiceGrpc.CatalogServiceFutureStub

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

### addCatalogAttribute(AddCatalogAttributeRequest request)
    
    
    public ListenableFuture<AttributesConfig> addCatalogAttribute(AddCatalogAttributeRequest request)

Adds the specified CatalogAttribute to the AttributesConfig. If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddCatalogAttributeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected CatalogServiceGrpc.CatalogServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceGrpc.CatalogServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceGrpc.CatalogServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### getAttributesConfig(GetAttributesConfigRequest request)
    
    
    public ListenableFuture<AttributesConfig> getAttributesConfig(GetAttributesConfigRequest request)

Gets an AttributesConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetAttributesConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### getCompletionConfig(GetCompletionConfigRequest request)
    
    
    public ListenableFuture<CompletionConfig> getCompletionConfig(GetCompletionConfigRequest request)

Gets a CompletionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetCompletionConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)>` |   
  
### getDefaultBranch(GetDefaultBranchRequest request)
    
    
    public ListenableFuture<GetDefaultBranchResponse> getDefaultBranch(GetDefaultBranchRequest request)

Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchResponse)>` |   
  
### listCatalogs(ListCatalogsRequest request)
    
    
    public ListenableFuture<ListCatalogsResponse> listCatalogs(ListCatalogsRequest request)

Lists all the Catalogs associated with the project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsResponse)>` |   
  
### removeCatalogAttribute(RemoveCatalogAttributeRequest request)
    
    
    public ListenableFuture<AttributesConfig> removeCatalogAttribute(RemoveCatalogAttributeRequest request)

Removes the specified CatalogAttribute from the AttributesConfig. If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveCatalogAttributeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### replaceCatalogAttribute(ReplaceCatalogAttributeRequest request)
    
    
    public ListenableFuture<AttributesConfig> replaceCatalogAttribute(ReplaceCatalogAttributeRequest request)

Replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key. If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ReplaceCatalogAttributeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### setDefaultBranch(SetDefaultBranchRequest request)
    
    
    public ListenableFuture<Empty> setDefaultBranch(SetDefaultBranchRequest request)

Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default. For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`. Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch. CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one. More specifically:

  * PredictionService will only return product IDs from branch {newBranch}.
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set).
  * UserEventService will only join events with products from branch {newBranch}.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetDefaultBranchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### updateAttributesConfig(UpdateAttributesConfigRequest request)
    
    
    public ListenableFuture<AttributesConfig> updateAttributesConfig(UpdateAttributesConfigRequest request)

Updates the AttributesConfig. The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateAttributesConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### updateCatalog(UpdateCatalogRequest request)
    
    
    public ListenableFuture<Catalog> updateCatalog(UpdateCatalogRequest request)

Updates the Catalogs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Catalog)>` |   
  
### updateCompletionConfig(UpdateCompletionConfigRequest request)
    
    
    public ListenableFuture<CompletionConfig> updateCompletionConfig(UpdateCompletionConfigRequest request)

Updates the CompletionConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCompletionConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
