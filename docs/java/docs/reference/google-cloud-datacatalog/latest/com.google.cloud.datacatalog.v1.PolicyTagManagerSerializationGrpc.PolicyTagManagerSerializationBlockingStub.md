---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub
title: Class PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:14.220386+00:00
---

# Class PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public static final class PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub extends AbstractBlockingStub<PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service PolicyTagManagerSerialization.

Policy Tag Manager Serialization API service allows you to manipulate your policy tags and taxonomies in a serialized format. Taxonomy is a hierarchical group of policy tags.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.PolicyTagManagerSerializationGrpc.PolicyTagManagerSerializationBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### exportTaxonomies(ExportTaxonomiesRequest request)
    
    
    public ExportTaxonomiesResponse exportTaxonomies(ExportTaxonomiesRequest request)

Exports taxonomies in the requested type and returns them, including their policy tags. The requested taxonomies must belong to the same project. This method generates `SerializedTaxonomy` protocol buffers with nested policy tags that can be used as input for `ImportTaxonomies` calls.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ExportTaxonomiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExportTaxonomiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ExportTaxonomiesResponse)` |   
  
### importTaxonomies(ImportTaxonomiesRequest request)
    
    
    public ImportTaxonomiesResponse importTaxonomies(ImportTaxonomiesRequest request)

Creates new taxonomies (including their policy tags) in a given project by importing from inlined or cross-regional sources. For a cross-regional source, new taxonomies are created by copying from a source in another region. For an inlined source, taxonomies and policy tags are created in bulk using nested protocol buffer structures.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportTaxonomiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImportTaxonomiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportTaxonomiesResponse)` |   
  
### replaceTaxonomy(ReplaceTaxonomyRequest request)
    
    
    public Taxonomy replaceTaxonomy(ReplaceTaxonomyRequest request)

Replaces (updates) a taxonomy and all its policy tags. The taxonomy and its entire hierarchy of policy tags must be represented literally by `SerializedTaxonomy` and the nested `SerializedPolicyTag` messages. This operation automatically does the following:

  * Deletes the existing policy tags that are missing from the `SerializedPolicyTag`.
  * Creates policy tags that don't have resource names. They are considered new.
  * Updates policy tags with valid resources names accordingly.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReplaceTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ReplaceTaxonomyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Taxonomy)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
