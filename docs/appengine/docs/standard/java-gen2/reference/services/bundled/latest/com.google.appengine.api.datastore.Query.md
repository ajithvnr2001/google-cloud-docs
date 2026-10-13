---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query
title: Class Query (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:00.455391+00:00
---

# Class Query (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Query (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Query implements Serializable

[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) encapsulates a request for zero or more [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects out of the datastore. It supports querying on zero or more properties, querying by ancestor, and sorting. [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects which match the query can be retrieved in a single list, or with an unbounded iterator.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Query

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

## Static Fields 

### KIND_METADATA_KIND
    
    
    public static final String KIND_METADATA_KIND

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### NAMESPACE_METADATA_KIND
    
    
    public static final String NAMESPACE_METADATA_KIND

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### PROPERTY_METADATA_KIND
    
    
    public static final String PROPERTY_METADATA_KIND

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Constructors 

### Query()
    
    
    public Query()

Create a new kindless [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) that finds [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects. Note that kindless queries are not yet supported in the Java dev appserver.

Currently the only operations supported on a kindless query are filter by **key** , ancestor, and order by **key** ascending.

### Query(Key ancestor)
    
    
    public Query(Key ancestor)

Create a new [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) that finds [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects with the specified `Key` as an ancestor.

**Parameter**  
---  
**Name** | **Description**  
`ancestor` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
the ancestor key or null  
  
### Query(@Nullable String kind, @Nullable Key ancestor)
    
    
    public Query(@Nullable String kind, @Nullable Key ancestor)

Create a new [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) that finds [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects with the specified `kind` and the specified `ancestor`. Note that kindless queries are not yet supported in the Java dev appserver.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
the kind or null to create a kindless query  
`ancestor` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the ancestor key or null  
  
### Query(String kind)
    
    
    public Query(String kind)

Create a new [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) that finds [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects with the specified `kind`. Note that kindless queries are not yet supported in the Java dev appserver.

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind or null to create a kindless query  
  
## Methods 

### addFilter(String propertyName, Query.FilterOperator operator, Object value) (deprecated)
    
    
    public Query addFilter(String propertyName, Query.FilterOperator operator, Object value)

**Deprecated.** _Use[#setFilter(Filter)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setFilter_)_

Add a [FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate) on the specified property.

All [FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate)s added using this message are combined using CompositeFilterOperator#AND.

Cannot be used in conjunction with [#setFilter(Filter)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setFilter_) which sets a single Filter instead of many [FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate)s.

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the property to which the filter applies.  
`operator` | `[Query.FilterOperator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterOperator)`  
The filter operator.  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
An instance of a supported datastore type. Note that entities with multi-value properties identified by `propertyName` will match this filter if the multi-value property has at least one value that matches the condition expressed by `operator` and `value`. For more information on multi-value property filtering please see the [datastore documentation](http://cloud.google.com/appengine/docs/java/datastore/).  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### addProjection(Projection projection)
    
    
    public Query addProjection(Projection projection)

Adds a projection for this query.

Projections are limited in the following ways:

  * Un-indexed properties cannot be projected and attempting to do so will result in no entities being returned. 
  * Projection [names](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Projection#com_google_appengine_api_datastore_Projection_getName__) must be unique. 
  * Properties that have an equality filter on them cannot be projected. This includes the operators FilterOperator#EQUAL and FilterOperator#IN. 

See Also: [#getProjections()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_getProjections__)

**Parameter**  
---  
**Name** | **Description**  
`projection` | `[Projection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Projection)`  
the projection to add  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### addSort(String propertyName)
    
    
    public Query addSort(String propertyName)

Specify how the query results should be sorted.

The first call to addSort will register the property that will serve as the primary sort key. A second call to addSort will set a secondary sort key, etc.

This method will always sort in ascending order. To control the order of the sort, use [#addSort(String,SortDirection)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_addSort_).

Note that entities with multi-value properties identified by `propertyName` will be sorted by the smallest value in the list. For more information on sorting properties with multiple values please see the [datastore documentation](http://cloud.google.com/appengine/docs/java/datastore/).

**Parameter**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### addSort(String propertyName, Query.SortDirection direction)
    
    
    public Query addSort(String propertyName, Query.SortDirection direction)

Specify how the query results should be sorted.

The first call to addSort will register the property that will serve as the primary sort key. A second call to addSort will set a secondary sort key, etc.

Note that if `direction` is SortDirection#ASCENDING, entities with multi-value properties identified by `propertyName` will be sorted by the smallest value in the list. If `direction` is SortDirection#DESCENDING, entities with multi-value properties identified by `propertyName` will be sorted by the largest value in the list. For more information on sorting properties with multiple values please see the [datastore documentation](http://cloud.google.com/appengine/docs/java/datastore/).

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`direction` | `[Query.SortDirection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.SortDirection)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### clearKeysOnly()
    
    
    public Query clearKeysOnly()

Clears the keys only flag. See Also: [#setKeysOnly()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setKeysOnly__)

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### equals(@Nullable Object o)
    
    
    public boolean equals(@Nullable Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAncestor()
    
    
    public Key getAncestor()

Gets the current ancestor for this query, or null if there is no ancestor specified.

**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### getAppId()
    
    
    public String getAppId()

Returns the appId for this [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDistinct()
    
    
    public boolean getDistinct()

Returns whether this query is distinct. See Also: [#setDistinct(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setDistinct_boolean_)

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFilter()
    
    
    public Query.@Nullable Filter getFilter()

Returns the filter for this query, or `null`. See Also: [#setFilter(Filter)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setFilter_)

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.Query.@org.jspecify.annotations.Nullable Filter` |   
  
### getFilterPredicates() (deprecated)
    
    
    public List<Query.FilterPredicate> getFilterPredicates()

**Deprecated.** _Use[#setFilter(Filter)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_setFilter_) and [#getFilter()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_getFilter__) instead_

Returns a mutable list of the current filter predicates. See Also: [#addFilter(String, FilterOperator, Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_addFilter_)

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate)>` |   
  
### getKind()
    
    
    public @Nullable String getKind()

Only [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects whose kind matches this value will be returned.

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### getNamespace()
    
    
    public String getNamespace()

Returns the namespace for this [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getProjections()
    
    
    public Collection<Projection> getProjections()

Returns a mutable collection properties included in the projection for this query.

If empty, the full or keys only entities are returned. Otherwise partial entities are returned. A non-empty projection is not compatible with setting keys-only. In this case a IllegalArgumentException will be thrown when the query is prepared.

Projection queries are similar to SQL statements of the form:
    
    
    SELECT prop1, prop2, ... 

As they return partial entities, which only contain the properties specified in the projection. However, these entities will only contain a single value for any multi-valued property and, if a multi-valued property is specified in the order, an inequality property, or the projected properties, the entity will be returned multiple times. Once for each unique combination of values.

Specifying a projection:

  * May change the type of any property returned in a projection. 
  * May change the index requirements for the given query. 
  * Will cause a partial entity to be returned. 
  * Will cause only entities that contain those properties to be returned. 



However, projection queries are significantly faster than normal queries. See Also: [#addProjection(Projection)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_addProjection_com_google_appengine_api_datastore_Projection_)

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Projection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Projection)>` | a mutable collection properties included in the projection for this query  
  
### getSortPredicates()
    
    
    public List<Query.SortPredicate> getSortPredicates()

Returns a mutable list of the current sort predicates.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SortPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.SortPredicate)>` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isKeysOnly()
    
    
    public boolean isKeysOnly()

Returns true if this query will fetch and return keys only, false if it will fetch and return full entities.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### reverse()
    
    
    public Query reverse()

Creates a query sorted in the exact opposite direction as the current one.

This function requires a sort order on [Entity#KEY_RESERVED_PROPERTY](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity#com_google_appengine_api_datastore_Entity_KEY_RESERVED_PROPERTY) to guarantee that each entity is uniquely identified by the set of properties used in the sort (which is required to exactly reverse the order of a query). Advanced users can reverse the sort orders manually if they know the set of sorted properties meets this requirement without a order on [Entity#KEY_RESERVED_PROPERTY](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity#com_google_appengine_api_datastore_Entity_KEY_RESERVED_PROPERTY).

The results of the reverse query will be the same as the results of the forward query but in reverse direction.

[Cursors](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor) from the original query may also be used in the reverse query.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | A new query with the sort order reversed.  
  
### setAncestor(Key ancestor)
    
    
    public Query setAncestor(Key ancestor)

Sets an ancestor for this query.

This restricts the query to only return result entities that are descended from a given entity. In other words, all of the results will have the ancestor as their parent, or parent's parent, or etc.

If null is specified, unsets any previously-set ancestor. Passing `null` as a parameter does not query for entities without ancestors (this type of query is not currently supported).

**Parameter**  
---  
**Name** | **Description**  
`ancestor` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### setDistinct(boolean distinct)
    
    
    public Query setDistinct(boolean distinct)

Sets whether to return only results with distinct values of the properties being projected.

**Parameter**  
---  
**Name** | **Description**  
`distinct` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
if this query should be distinct. This may only be used when the query has a projection.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### setFilter(Query.@Nullable Filter filter)
    
    
    public Query setFilter(Query.@Nullable Filter filter)

Sets the filter to use for this query. See Also: CompositeFilter, [FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate)

**Parameter**  
---  
**Name** | **Description**  
`filter` | `com.google.appengine.api.datastore.Query.@org.jspecify.annotations.Nullable Filter`  
the filter to use for this query, or `null`  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### setKeysOnly()
    
    
    public Query setKeysOnly()

Makes this query fetch and return only keys, not full entities.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)` | `this` (for chaining)  
  
### toString()
    
    
    public String toString()

Outputs a SQL like string representing the query.

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
