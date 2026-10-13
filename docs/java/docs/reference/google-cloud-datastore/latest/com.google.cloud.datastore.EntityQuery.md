---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.EntityQuery
title: Class EntityQuery (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:08.513103+00:00
---

# Class EntityQuery (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.EntityQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EntityQuery (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public final class EntityQuery extends StructuredQuery<Entity>

An implementation of a Google Cloud Datastore entity query that can be constructed by providing all the specific query elements. See Also: [Datastore queries](https://cloud.google.com/appengine/docs/java/datastore/queries)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [Query<V>](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query) > [StructuredQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery) > EntityQuery

## Inherited Members

[Query.<V>newGqlQueryBuilder(Query.ResultType<V>,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query__V_newGqlQueryBuilder_com_google_cloud_datastore_Query_ResultType_V__java_lang_String_)

[Query.getNamespace()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_getNamespace__)

[Query.newAggregationQueryBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_newAggregationQueryBuilder__)

[Query.newEntityQueryBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_newEntityQueryBuilder__)

[Query.newGqlQueryBuilder(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_newGqlQueryBuilder_java_lang_String_)

[Query.newKeyQueryBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_newKeyQueryBuilder__)

[Query.newProjectionEntityQueryBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query#com_google_cloud_datastore_Query_newProjectionEntityQueryBuilder__)

[StructuredQuery.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_equals_java_lang_Object_)

[StructuredQuery.getDistinctOn()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getDistinctOn__)

[StructuredQuery.getEndCursor()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getEndCursor__)

[StructuredQuery.getFilter()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getFilter__)

[StructuredQuery.getKind()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getKind__)

[StructuredQuery.getLimit()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getLimit__)

[StructuredQuery.getOffset()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getOffset__)

[StructuredQuery.getOrderBy()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getOrderBy__)

[StructuredQuery.getProjection()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getProjection__)

[StructuredQuery.getStartCursor()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getStartCursor__)

[StructuredQuery.getType()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_getType__)

[StructuredQuery.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_hashCode__)

[StructuredQuery.nextQuery(RunQueryResponse)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_nextQuery_com_google_datastore_v1_RunQueryResponse_)

[StructuredQuery.populatePb(RunQueryRequest.Builder)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_populatePb_com_google_datastore_v1_RunQueryRequest_Builder_)

[StructuredQuery.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_toBuilder__)

[StructuredQuery.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### toBuilder()
    
    
    public EntityQuery.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[EntityQuery.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.EntityQuery.Builder)` |   
**Overrides**

[StructuredQuery<V>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery#com_google_cloud_datastore_StructuredQuery_toBuilder__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
