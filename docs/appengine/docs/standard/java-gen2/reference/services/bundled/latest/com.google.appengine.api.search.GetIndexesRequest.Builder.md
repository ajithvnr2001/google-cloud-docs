---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder
title: Class GetIndexesRequest.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:48:04.572747+00:00
---

# Class GetIndexesRequest.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class GetIndexesRequest.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class GetIndexesRequest.Builder

The builder of [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)s.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GetIndexesRequest.Builder

## Inherited Members

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

### build()
    
    
    public GetIndexesRequest build()

**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)` | builds and returns a brand new instance of a [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest) using values set on this builder  
  
### setAllNamespaces(boolean allNamespaces)
    
    
    public GetIndexesRequest.Builder setAllNamespaces(boolean allNamespaces)

Sets whether or not to fetch indexes from all namespaces.

**Parameter**  
---  
**Name** | **Description**  
`allNamespaces` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether or not to fetch indexes from all namespaces  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setIncludeStartIndex(boolean includeStartIndex)
    
    
    public GetIndexesRequest.Builder setIncludeStartIndex(boolean includeStartIndex)

Sets whether or not to include the index whose name is specified via the [#setStartIndexName(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder#com_google_appengine_api_search_GetIndexesRequest_Builder_setStartIndexName_java_lang_String_) method.

**Parameter**  
---  
**Name** | **Description**  
`includeStartIndex` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether or not to return the start index  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setIndexNamePrefix(String indexNamePrefix)
    
    
    public GetIndexesRequest.Builder setIndexNamePrefix(String indexNamePrefix)

Sets the prefix to be matched against the names of returned indexes. If the prefix is set to, say "a", only indexes with names starting with 'a' will be returned.

**Parameter**  
---  
**Name** | **Description**  
`indexNamePrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the prefix used to select returned indexes  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setLimit(Integer limit)
    
    
    public GetIndexesRequest.Builder setLimit(Integer limit)

Sets the maximum number of indexes to return.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
the number of indexes to return  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setNamespace(String namespace)
    
    
    public GetIndexesRequest.Builder setNamespace(String namespace)

Sets the namespace to use for this request. Only indexes defined within this namespace will be fetched.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The namespace for this request.  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setOffset(Integer offset)
    
    
    public GetIndexesRequest.Builder setOffset(Integer offset)

Sets the offset of the first index to return. This method comes with a performance penalty and if you just want to page through all indexes you should consider [#setStartIndexName(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder#com_google_appengine_api_search_GetIndexesRequest_Builder_setStartIndexName_java_lang_String_) method.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
the offset of the first returned index  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setSchemaFetched(boolean schemaFetched)
    
    
    public GetIndexesRequest.Builder setSchemaFetched(boolean schemaFetched)

Sets whether or not the schema is returned with indexes. An index schema is a map from field names to field types.

**Parameter**  
---  
**Name** | **Description**  
`schemaFetched` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether or not schemas are present in returned indexes  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
### setStartIndexName(String startIndexName)
    
    
    public GetIndexesRequest.Builder setStartIndexName(String startIndexName)

Sets the name of the first index to return. You may exclude this index by using the [#setIncludeStartIndex(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder#com_google_appengine_api_search_GetIndexesRequest_Builder_setIncludeStartIndex_boolean_) method.

**Parameter**  
---  
**Name** | **Description**  
`startIndexName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the first index to be returned  
**Returns**  
---  
**Type** | **Description**  
`[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)` | this builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
