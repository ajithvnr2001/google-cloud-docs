---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query(class)
title: Class Query (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:48:47.804351+00:00
---

# Class Query (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query(class)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Query (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class Query

A query to search an index for documents which match, restricting the document fields returned to those given, and scoring and sorting the results, whilst supporting pagination. 

For example, the following query will search for documents where the tokens 'good' and 'story' occur in some fields, returns up to 20 results including the fields 'author' and 'date-sent' as well as snippeted fields 'subject' and 'body'. The results are sorted by 'author' in descending order, getting the next 20 results from the responseCursor in the previously returned results, giving back a single cursor in the [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) to get the next batch of results after this. 
    
    
     QueryOptions options = QueryOptions.newBuilder()
         .setLimit(20)
         .setFieldsToSnippet("subject", "body")
         .setScorer(CustomScorer.newBuilder()
             .addSortExpression(SortExpression.newBuilder()
                 .setExpression("author")
                 .setDirection(SortDirection.DESCENDING)
                 .setDefaultValue("")))
         .setCursor(responseCursor)
         .build();
     Query query = Query.newBuilder()
         .setOptions(options)
         .build("good story");
     
     

The following query will return facet information with the query result:

Query query = Query.newBuilder() .setOptions(options) .setEnableFacetDiscovery(true) .build("tablet");

To customize returned facet or refine the result using a previously returned [FacetResultValue#getRefinementToken](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue#com_google_appengine_api_search_FacetResultValue_getRefinementToken_):

Query query = Query.newBuilder() .setOptions(options) .setEnableFacetDiscovery(true) .setFacetOptions(FacetOptions.newBuilder().setDiscoveryLimit(5).build()) .addReturnFacet("shipping") .addReturnFacet(FacetRequest.newBuilder().setName("department") .addValueConstraint("Computers") .addValueConstraint("Electronics") .build()) .addRefinementToken(refinementToken1) .addRefinementToken(refinementToken2) .build("tablet");

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Query

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

## Static Methods 

### newBuilder()
    
    
    public static Query.Builder newBuilder()

Creates and returns a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) builder. Set the query parameters and use the Builder#build() method to create a concrete instance of Query.

**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | a Builder which can construct a query  
  
### newBuilder(Query query)
    
    
    public static Query.Builder newBuilder(Query query)

Creates a builder from the given query.

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))`  
the query for the builder to use to build another query  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | a new builder with values based on the given request  
  
## Constructors 

### Query(Query.Builder builder)
    
    
    protected Query(Query.Builder builder)

Creates a query from the builder.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)`  
the query builder to populate with  
  
## Methods 

### getEnableFacetDiscovery()
    
    
    public boolean getEnableFacetDiscovery()

Returns true if facet discovery is enabled.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFacetOptions()
    
    
    public FacetOptions getFacetOptions()

Returns the [FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions) for controlling faceted search or null if unset.

**Returns**  
---  
**Type** | **Description**  
`[FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions)` |   
  
### getOptions()
    
    
    public QueryOptions getOptions()

Returns the [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions) for controlling the what is returned in the result set matching the query

**Returns**  
---  
**Type** | **Description**  
`[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions)` |   
  
### getQueryString()
    
    
    public String getQueryString()

The query can be as simple as a single term ("foo"), or as complex as a boolean expression, including field names ("title:hello OR body:important -october").

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the query  
  
### getRefinements()
    
    
    public ImmutableList<FacetRefinement> getRefinements()

Returns an unmodifiable list of facet refinements for the search.

**Returns**  
---  
**Type** | **Description**  
`com.google.common.collect.ImmutableList<[FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)>` |   
  
### getReturnFacets()
    
    
    public ImmutableList<FacetRequest> getReturnFacets()

Returns an unmodifiable list of requests for facets to be returned with the search results.

**Returns**  
---  
**Type** | **Description**  
`com.google.common.collect.ImmutableList<[FacetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest)>` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
