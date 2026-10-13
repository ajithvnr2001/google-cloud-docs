---
url: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-sql-queries/
title: Graphs within SQL \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:20.129825+00:00
---

# Graphs within SQL  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-sql-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Graphs within SQL Stay organized with collections  Save and categorize content based on your preferences. 

GoogleSQL for Spanner supports the following syntax to use graphs within SQL queries.

## Language list

Name | Summary  
---|---  
[`GRAPH_TABLE` operator](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-sql-queries#graph_table_operator) |  Performs an operation on a graph in the `FROM` clause of a SQL query and then produces a table with the results.   
  
## `GRAPH_TABLE` operator
    
    
    FROM GRAPH_TABLE (
      property_graph_name
      multi_linear_query_statement
    ) [ [ AS ] alias ]
    

#### Description

Performs an operation on a graph in the `FROM` clause of a SQL query and then produces a table with the results.

With the `GRAPH_TABLE` operator, you can use the [GQL syntax](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements) to query a property graph. The result of this operation is produced as a table that you can use in the rest of the query.

#### Definitions

  * `property_graph_name`: The name of the property graph to query for patterns.
  * `multi_linear_query_statement`: You can use GQL to query a property graph for patterns. For more information, see [Graph query language](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements).
  * `alias`: An optional alias, which you can use to refer to the table produced by the `GRAPH_TABLE` operator elsewhere in the query.



#### Examples

**Note:** The examples in this section reference a property graph called [`FinGraph`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-schema-statements#fin_graph).

You can use the `RETURN` statement to return specific node and edge properties. For example:
    
    
    SELECT name, id
    FROM GRAPH_TABLE(
      FinGraph
      MATCH (n:Person)
      RETURN n.name AS name, n.id AS id
    );
    
    /*-----------+
     | name | id |
     +-----------+
     | Alex | 1  |
     | Dana | 2  |
     | Lee  | 3  |
     +-----------*/
    

You can use the `RETURN` statement to produce output with graph pattern variables. These variables can be referenced outside `GRAPH_TABLE`. For example,
    
    
    SELECT n.name, n.id
    FROM GRAPH_TABLE(
      FinGraph
      MATCH (n:Person)
      RETURN n
    );
    
    /*-----------+
     | name | id |
     +-----------+
     | Alex | 1  |
     | Dana | 2  |
     | Lee  | 3  |
     +-----------*/
    

The following query produces an error because `id` isn't included in the `RETURN` statement, even though this property exists for element `n`:
    
    
    SELECT name, id
    FROM GRAPH_TABLE(
      FinGraph
      MATCH (n:Person)
      RETURN n.name
    );
    

The following query produces an error because directly outputting the graph element `n` is not supported. Convert `n` to its JSON representation using the `SAFE_TO_JSON` function for successful output.
    
    
    -- Error
    SELECT n
    FROM GRAPH_TABLE(
      FinGraph
      MATCH (n:Person)
      RETURN n
    );
    
    
    
    SELECT SAFE_TO_JSON(n) as json_node
    FROM GRAPH_TABLE(
      FinGraph
      MATCH (n:Person)
      RETURN n
    );
    
    /*---------------------------+
     | json_node                 |
     +---------------------------+
     | {"identifier":"mUZpbk...} |
     | {"identifier":"mUZpbk...} |
     | {"identifier":"mUZpbk...} |
     +--------------------------*/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
