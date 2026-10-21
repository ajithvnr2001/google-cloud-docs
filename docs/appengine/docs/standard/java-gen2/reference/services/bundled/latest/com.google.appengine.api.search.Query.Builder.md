---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder
title: Class Query.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:42:41.687337+00:00
---

# Class Query.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Query.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class Query.Builder

A builder which constructs Query objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Query.Builder

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

## Constructors 

### Builder()
    
    
    protected Builder()

## Methods 

### addFacetRefinement(FacetRefinement refinement)
    
    
    public Query.Builder addFacetRefinement(FacetRefinement refinement)

Adds a facet refinement. There will be disjunction between refinements for the same facet and conjunction between refinements for different facets. For example if the refinements are (name=wine_type,value=red), (name=wine_type,value=white) and (name=year, Range(2000,2010)), the result will be refined according to:

((wine_type is red) OR (wine_type is white)) AND (year in Range.closedOpen(2000,2010))

**Parameter**  
---  
**Name** | **Description**  
`refinement` | `[FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)`  
a [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement) object.  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### addFacetRefinementFromToken(String token)
    
    
    public Query.Builder addFacetRefinementFromToken(String token)

Adds a facet refinement token. The token is returned by each FacetResultValue. There will be disjunction between tokens for the same facet and conjunction between tokens for different facets. For example if the refinement tokens are (name=wine_type,value=red), (name=wine_type,value=white) and (name=year, Range(2000,2010)), the result will be refined according to:

((wine_type is red) OR (wine_type is white)) AND (year in Range(2000,2010))

**Parameter**  
---  
**Name** | **Description**  
`token` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the token returned by [FacetResultValue#getRefinementToken](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue#com_google_appengine_api_search_FacetResultValue_getRefinementToken_) or [FacetRefinement#toTokenString](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement#com_google_appengine_api_search_FacetRefinement_toTokenString_).  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### addReturnFacet(FacetRequest facet)
    
    
    public Query.Builder addReturnFacet(FacetRequest facet)

Requests a facet to be returned with search results. The facet will be included in the result regardless of the number of values it has.

**Parameter**  
---  
**Name** | **Description**  
`facet` | `[FacetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest)`  
the [FacetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest) to be added to return facets.  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### addReturnFacet(FacetRequest.Builder builder)
    
    
    public Query.Builder addReturnFacet(FacetRequest.Builder builder)

Adds a facet request from a builder.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[FacetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest.Builder)`  
the [FacetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest.Builder) build a [FacetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRequest) to be added to return facets.  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### addReturnFacet(String facetName)
    
    
    public Query.Builder addReturnFacet(String facetName)

Adds a facet request by its name only.

**Parameter**  
---  
**Name** | **Description**  
`facetName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet to be added to return facets.  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### build()
    
    
    public Query build()

Construct the message.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))` | the Query built from the parameters entered on this Builder  
  
### build(String queryString)
    
    
    public Query build(String queryString)

Build a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) from the query string and the parameters set on the Builder. A query string can be as simple as a single term ("foo"), or as complex as a boolean expression, including field names ("title:hello OR body:important -october").

**Parameter**  
---  
**Name** | **Description**  
`queryString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the query string to parse and apply to an index  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))` | the Query built from the parameters entered on this Builder including the queryString  
  
### setEnableFacetDiscovery(boolean value)
    
    
    public Query.Builder setEnableFacetDiscovery(boolean value)

Sets enable facet discovery flag.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### setFacetOptions(FacetOptions options)
    
    
    public Query.Builder setFacetOptions(FacetOptions options)

Sets the facet options.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions)`  
the [FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions) to apply to the facet results  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### setFacetOptions(FacetOptions.Builder builder)
    
    
    public Query.Builder setFacetOptions(FacetOptions.Builder builder)

Sets the facet options from a builder.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[FacetOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions.Builder)`  
the [FacetOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions.Builder) build a [FacetOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetOptions) to apply to the facet results  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### setOptions(QueryOptions options)
    
    
    public Query.Builder setOptions(QueryOptions options)

Sets the query options.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions)`  
the [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions) to apply to the search results  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### setOptions(QueryOptions.Builder optionsBuilder)
    
    
    public Query.Builder setOptions(QueryOptions.Builder optionsBuilder)

Sets the query options from a builder.

**Parameter**  
---  
**Name** | **Description**  
`optionsBuilder` | `[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)`  
the [QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder) build a [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions) to apply to the search results  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this builder  
  
### setQueryString(String query)
    
    
    protected Query.Builder setQueryString(String query)

Sets the query string used to construct the query.

**Parameter**  
---  
**Name** | **Description**  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a query string used to construct the query  
**Returns**  
---  
**Type** | **Description**  
`[Query.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder)` | this Builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
