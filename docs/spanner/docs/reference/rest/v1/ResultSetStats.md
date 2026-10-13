---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats/
title: ResultSetStats \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:21.813975+00:00
---

# ResultSetStats  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  ResultSetStats Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * QueryPlan
    * JSON representation
  * PlanNode
    * JSON representation
  * Kind
  * ChildLink
    * JSON representation
  * ShortRepresentation
    * JSON representation
  * QueryAdvisorResult
    * JSON representation
  * IndexAdvice
    * JSON representation



Additional statistics about a `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` or `[PartialResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartialResultSet)`.

JSON representation  
---  
      
    
    {
      "queryPlan": {
        object ([QueryPlan](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryPlan))
      },
      "queryStats": {
        object
      },
    
      // Union field row_count can be only one of the following:
      "rowCountExact": string,
      "rowCountLowerBound": string
      // End of list of possible types for union field row_count.
    }  
  
Fields  
---  
`queryPlan` |  `object (`[QueryPlan](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryPlan)`)` `[QueryPlan](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryPlan)` for the query associated with this result.  
`queryStats` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Aggregated statistics from the execution of the query. Only present when the query is profiled. For example, a query could return the statistics as follows:
    
    
    {
      "rows_returned": "3",
      "elapsed_time": "1.22 secs",
      "cpu_time": "1.19 secs"
    }
      
  
Union field `row_count`. The number of rows modified by the DML statement. `row_count` can be only one of the following:  
`rowCountExact` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Standard DML returns an exact count of rows that were modified.  
`rowCountLowerBound` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Partitioned DML doesn't offer exactly-once semantics, so it returns a lower bound of the rows modified.  
  
## QueryPlan

Contains an ordered list of nodes appearing in the query plan.

JSON representation  
---  
      
    
    {
      "planNodes": [
        {
          object ([PlanNode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode))
        }
      ],
      "queryAdvice": {
        object ([QueryAdvisorResult](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryAdvisorResult))
      }
    }  
  
Fields  
---  
`planNodes[]` |  `object (`[PlanNode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode)`)` The nodes in the query plan. Plan nodes are returned in pre-order starting with the plan root. Each `[PlanNode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode)`'s `id` corresponds to its index in `planNodes`.  
`queryAdvice` |  `object (`[QueryAdvisorResult](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryAdvisorResult)`)` Optional. The advise/recommendations for a query. Currently this field will be serving index recommendations for a query.  
  
## PlanNode

Node information for nodes appearing in a `[QueryPlan.plan_nodes](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryPlan.FIELDS.plan_nodes)`.

JSON representation  
---  
      
    
    {
      "index": integer,
      "kind": enum ([Kind](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#Kind)),
      "displayName": string,
      "childLinks": [
        {
          object ([ChildLink](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#ChildLink))
        }
      ],
      "shortRepresentation": {
        object ([ShortRepresentation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#ShortRepresentation))
      },
      "metadata": {
        object
      },
      "executionStats": {
        object
      }
    }  
  
Fields  
---  
`index` |  `integer` The `PlanNode`'s index in `[node list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#QueryPlan.FIELDS.plan_nodes)`.  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#Kind)`)` Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a `[SCALAR](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#Kind.ENUM_VALUES.SCALAR)` node, it will have a condensed representation which can be used to directly embed a description of the node in its parent.  
`displayName` |  `string` The display name for the node.  
`childLinks[]` |  `object (`[ChildLink](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#ChildLink)`)` List of child node `index`es and their relationship to this parent.  
`shortRepresentation` |  `object (`[ShortRepresentation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#ShortRepresentation)`)` Condensed representation for `[SCALAR](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#Kind.ENUM_VALUES.SCALAR)` nodes.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:
    
    
    {
      "parameter_reference": "param1",
      "parameterType": "array"
    }
      
  
`executionStats` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc.  
  
## Kind

The kind of `[PlanNode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode)`. Distinguishes between the two different kinds of nodes that can appear in a query plan.

Enums  
---  
`KIND_UNSPECIFIED` | Not specified.  
`RELATIONAL` | Denotes a Relational operator node in the expression tree. Relational operators represent iterative processing of rows during query execution. For example, a `TableScan` operation that reads rows from a table.  
`SCALAR` | Denotes a Scalar node in the expression tree. Scalar nodes represent non-iterable entities in the query plan. For example, constants or arithmetic operators appearing inside predicate expressions or references to column names.  
  
## ChildLink

Metadata associated with a parent-child relationship appearing in a `[PlanNode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode)`.

JSON representation  
---  
      
    
    {
      "childIndex": integer,
      "type": string,
      "variable": string
    }  
  
Fields  
---  
`childIndex` |  `integer` The node to which the link points.  
`type` |  `string` The type of the link. For example, in Hash Joins this could be used to distinguish between the build child and the probe child, or in the case of the child being an output variable, to represent the tag associated with the output variable.  
`variable` |  `string` Only present if the child node is `[SCALAR](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#Kind.ENUM_VALUES.SCALAR)` and corresponds to an output variable of the parent node. The field carries the name of the output variable. For example, a `TableScan` operator that reads rows from a table will have child links to the `SCALAR` nodes representing the output variables created for each column that is read by the operator. The corresponding `variable` fields will be set to the variable names assigned to the columns.  
  
## ShortRepresentation

Condensed representation of a node and its subtree. Only present for `SCALAR` `[PlanNode(s)](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#PlanNode)`.

JSON representation  
---  
      
    
    {
      "description": string,
      "subqueries": {
        string: integer,
        ...
      }
    }  
  
Fields  
---  
`description` |  `string` A string representation of the expression subtree rooted at this node.  
`subqueries` |  `map (key: string, value: integer)` A mapping of (subquery variable name) -> (subquery node id) for cases where the `description` string of this node references a `SCALAR` subquery contained in the expression subtree rooted at this node. The referenced `SCALAR` subquery may not necessarily be a direct child of this node.  
  
## QueryAdvisorResult

Output of query advisor analysis.

JSON representation  
---  
      
    
    {
      "indexAdvice": [
        {
          object ([IndexAdvice](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#IndexAdvice))
        }
      ]
    }  
  
Fields  
---  
`indexAdvice[]` |  `object (`[IndexAdvice](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats#IndexAdvice)`)` Optional. Index Recommendation for a query. This is an optional field and the recommendation will only be available when the recommendation guarantees significant improvement in query performance.  
  
## IndexAdvice

Recommendation to add new indexes to run queries more efficiently.

JSON representation  
---  
      
    
    {
      "ddl": [
        string
      ],
      "improvementFactor": number
    }  
  
Fields  
---  
`ddl[]` |  `string` Optional. DDL statements to add new indexes that will improve the query.  
`improvementFactor` |  `number` Optional. Estimated latency improvement factor. For example if the query currently takes 500 ms to run and the estimated latency with new indexes is 100 ms this field will be 5.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
