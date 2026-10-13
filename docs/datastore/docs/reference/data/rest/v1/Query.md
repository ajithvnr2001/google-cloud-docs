---
url: https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query/
title: Query \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:08.902133+00:00
---

# Query  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Reference ](https://docs.cloud.google.com/datastore/docs/apis)



Send feedback 

#  Query Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Projection
    * JSON representation
  * KindExpression
    * JSON representation
  * Filter
    * JSON representation
  * CompositeFilter
    * JSON representation
  * Operator
  * PropertyFilter
    * JSON representation
  * Operator
  * PropertyOrder
    * JSON representation
  * Direction



A query for entities.

The query stages are executed in the following order: 1. kind 2. filter 3. projection 4. order + startCursor + endCursor 5. offset 6. limit 7. findNearest

JSON representation  
---  
      
    
    {
      "projection": [
        {
          object ([Projection](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Projection))
        }
      ],
      "kind": [
        {
          object ([KindExpression](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#KindExpression))
        }
      ],
      "filter": {
        object ([Filter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Filter))
      },
      "order": [
        {
          object ([PropertyOrder](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#PropertyOrder))
        }
      ],
      "distinctOn": [
        {
          object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference))
        }
      ],
      "startCursor": string,
      "endCursor": string,
      "offset": integer,
      "limit": integer
    }  
  
Fields  
---  
`projection[]` |  `object (`[Projection](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Projection)`)` The projection to return. Defaults to returning all properties.  
`kind[]` |  `object (`[KindExpression](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#KindExpression)`)` The kinds to query (if empty, returns entities of all kinds). Currently at most 1 kind may be specified.  
`filter` |  `object (`[Filter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Filter)`)` The filter to apply.  
`order[]` |  `object (`[PropertyOrder](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#PropertyOrder)`)` The order to apply to the query results (if empty, order is unspecified).  
`distinctOn[]` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference)`)` The properties to make distinct. The query results will contain the first result for each distinct combination of values for the given properties (if empty, all results are returned).Requires:

  * If `order` is specified, the set of distinct on properties must appear before the non-distinct on properties in `order`.

  
`startCursor` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A starting point for the query results. Query cursors are returned in query result batches and [can only be used to continue the same query](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets).A base64-encoded string.  
`endCursor` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` An ending point for the query results. Query cursors are returned in query result batches and [can only be used to limit the same query](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets).A base64-encoded string.  
`offset` |  `integer` The number of results to skip. Applies before limit, but after all other constraints. Optional. Must be >= 0 if specified.  
`limit` |  `integer` The maximum number of results to return. Applies after all other constraints. Optional. Unspecified is interpreted as no limit. Must be >= 0 if specified.  
  
## Projection

A representation of a property in a projection.

JSON representation  
---  
      
    
    {
      "property": {
        object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference))
      }
    }  
  
Fields  
---  
`property` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference)`)` The property to project.  
  
## KindExpression

A representation of a kind.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` The name of the kind.  
  
## Filter

A holder for any type of filter.

JSON representation  
---  
      
    
    {
    
      // Union field filter_type can be only one of the following:
      "compositeFilter": {
        object ([CompositeFilter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#CompositeFilter))
      },
      "propertyFilter": {
        object ([PropertyFilter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#PropertyFilter))
      }
      // End of list of possible types for union field filter_type.
    }  
  
Fields  
---  
Union field `filter_type`. The type of filter. `filter_type` can be only one of the following:  
`compositeFilter` |  `object (`[CompositeFilter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#CompositeFilter)`)` A composite filter.  
`propertyFilter` |  `object (`[PropertyFilter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#PropertyFilter)`)` A filter on a property.  
  
## CompositeFilter

A filter that merges multiple other filters using the given operator.

JSON representation  
---  
      
    
    {
      "op": enum ([Operator](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Operator)),
      "filters": [
        {
          object ([Filter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Filter))
        }
      ]
    }  
  
Fields  
---  
`op` |  `enum (`[Operator](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Operator)`)` The operator for combining multiple filters.  
`filters[]` |  `object (`[Filter](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Filter)`)` The list of filters to combine.Requires:

  * At least one filter is present.

  
  
## Operator

A composite filter operator.

Enums  
---  
`OPERATOR_UNSPECIFIED` | Unspecified. This value must not be used.  
`AND` | The results are required to satisfy each of the combined filters.  
`OR` | Documents are required to satisfy at least one of the combined filters.  
  
## PropertyFilter

A filter on a specific property.

JSON representation  
---  
      
    
    {
      "property": {
        object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference))
      },
      "op": enum ([Operator](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Operator_1)),
      "value": {
        object ([Value](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value))
      }
    }  
  
Fields  
---  
`property` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference)`)` The property to filter by.  
`op` |  `enum (`[Operator](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Operator_1)`)` The operator to filter by.  
`value` |  `object (`[Value](https://docs.cloud.google.com/datastore/docs/reference/data/rest/Shared.Types/Value)`)` The value to compare the property to.  
  
## Operator

A property filter operator.

Enums  
---  
`OPERATOR_UNSPECIFIED` | Unspecified. This value must not be used.  
`LESS_THAN` | The given `property` is less than the given `value`.Requires:

  * That `property` comes first in `order_by`.

  
`LESS_THAN_OR_EQUAL` | The given `property` is less than or equal to the given `value`.Requires:

  * That `property` comes first in `order_by`.

  
`GREATER_THAN` | The given `property` is greater than the given `value`.Requires:

  * That `property` comes first in `order_by`.

  
`GREATER_THAN_OR_EQUAL` | The given `property` is greater than or equal to the given `value`.Requires:

  * That `property` comes first in `order_by`.

  
`EQUAL` | The given `property` is equal to the given `value`.  
`IN` | The given `property` is equal to at least one value in the given array.Requires:

  * That `value` is a non-empty `ArrayValue`, subject to disjunction limits.
  * No `NOT_IN` is in the same query.

  
`NOT_EQUAL` | The given `property` is not equal to the given `value`.Requires:

  * No other `NOT_EQUAL` or `NOT_IN` is in the same query.
  * That `property` comes first in the `order_by`.

  
`HAS_ANCESTOR` | Limit the result set to the given entity and its descendants.Requires:

  * That `value` is an entity key.
  * All evaluated disjunctions must have the same `HAS_ANCESTOR` filter.

  
`NOT_IN` | The value of the `property` is not in the given array.Requires:

  * That `value` is a non-empty `ArrayValue` with at most 10 values.
  * No other `OR`, `IN`, `NOT_IN`, `NOT_EQUAL` is in the same query.
  * That `field` comes first in the `order_by`.

  
  
## PropertyOrder

The desired order for a specific property.

JSON representation  
---  
      
    
    {
      "property": {
        object ([PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference))
      },
      "direction": enum ([Direction](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Direction))
    }  
  
Fields  
---  
`property` |  `object (`[PropertyReference](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/PropertyReference)`)` The property to order by.  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/datastore/docs/reference/data/rest/v1/Query#Direction)`)` The direction to order by. Defaults to `ASCENDING`.  
  
## Direction

The sort direction.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified. This value must not be used.  
`ASCENDING` | Ascending.  
`DESCENDING` | Descending.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-08 UTC."],[],[]] 
