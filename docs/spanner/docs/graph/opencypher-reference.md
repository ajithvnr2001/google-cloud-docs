---
url: https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference/
title: Spanner Graph reference for openCypher users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:31.002697+00:00
---

# Spanner Graph reference for openCypher users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Spanner Graph reference for openCypher users Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This document compares openCypher and Spanner Graph in the following ways:

  * Terminology
  * Data model
  * Schema
  * Query
  * Mutation



This document assumes you're familiar with [openCypher v9](https://opencypher.org/resources/).

## Before you begin

[Set up and query Spanner Graph using the Google Cloud console](https://docs.cloud.google.com/spanner/docs/graph/set-up).

## Terminology

openCypher | Spanner Graph  
---|---  
nodes | nodes  
relationships | edges  
node labels | node labels  
relationship types | edge labels  
clauses | Spanner Graph uses the term `statement` for a complete unit of execution, and `clause` for a modifier to statements.  
  
For example, `MATCH` is a statement whereas `WHERE` is a clause.  
relationship uniqueness  
  
openCypher doesn't return results with repeating edges in a single match. | `TRAIL` path  
  
When uniqueness is desired in Spanner Graph, use [ `TRAIL` mode](https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference#relationship-uniqueness-and-trail-mode) to return unique edges in a single match.   
  
## Standards compliance

Spanner Graph adopts ISO [Graph Query Language](https://www.iso.org/standard/76120.html) (GQL) and [SQL/Property Graph Queries](https://www.iso.org/standard/79473.html) (SQL/PGQ) standards.

## Data model

Both Spanner Graph and openCypher adopt the property graph data model with some differences.

openCypher | Spanner Graph  
---|---  
Each relationship has exactly one relationship type.  
|  Both nodes and edges have one or more labels.  
  
## Schema

openCypher | Spanner Graph  
---|---  
A graph has no predefined schema. | A graph schema must be explicitly defined by using the [`CREATE PROPERTY GRAPH` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-schema-statements#gql_create_graph).  
Labels are statically defined in the schema. To update labels, you need to update the schema.  
For more information, see [Create, update, or drop a Spanner Graph schema](https://docs.cloud.google.com/spanner/docs/graph/create-update-drop-schema).  
  
## Query

Spanner Graph query capabilities are similar to those of openCypher. The differences between Spanner Graph and openCypher are described in this section.

### Specify the graph

In openCypher, there is one default graph, and queries operate on the default graph. In Spanner Graph, you can define more than one graph and a query must start with the `GRAPH` clause to specify the graph to query. For example:
    
    
       GRAPH FinGraph
       MATCH (p:Person)
       RETURN p.name;
    

For more information, see the [graph query syntax](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements).

### Graph pattern matching

Spanner Graph supports graph pattern matching capabilities similar to openCypher. The differences are explained in the following sections.

#### Relationship uniqueness and TRAIL mode

openCypher doesn't return results with repeating edges in a single match; this is called _relationship uniqueness_ in openCypher. In Spanner Graph, repeating edges are returned by default. When uniqueness is desired, use `TRAIL` mode to ensure no repeating edge exists in the single match. For detailed semantics of `TRAIL` and other different path modes, see [Path mode](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-patterns#path_mode).

The following example shows how the results of a query change with `TRAIL` mode:

  * The openCypher and Spanner Graph `TRAIL` mode queries return empty results because the only possible path is to repeat `t1` twice.
  * By default, the Spanner Graph query returns a valid path.



![Example graph](https://docs.cloud.google.com/static/spanner/docs/images/spanner-graph-opencypher-image.png)

openCypher | Spanner Graph (TRAIL mode) | Spanner Graph (default mode)  
---|---|---  
      
    
    MATCH
      (src:Account)-[t1:Transfers]->
      (dst:Account)-[t2:Transfers]->
      (src)-[t1]->(dst)
    WHERE src.id = 16
    RETURN src.id AS src_id, dst.id AS dst_id;
          

| 
    
    
    GRAPH FinGraph
    MATCH TRAIL
      (src:Account)-[t1:Transfers]->
      (dst:Account)-[t2:Transfers]->
      (src)-[t1]->(dst)
    WHERE src.id = 16
    RETURN src.id AS src_id, dst.id AS dst_id;
          

| 
    
    
    GRAPH FinGraph
    MATCH
      (src:Account)-[t1:Transfers]->
      (dst:Account)-[t2:Transfers]->
      (src)-[t1]-> (dst)
    WHERE src.id = 16
    RETURN src.id AS src_id, dst.id AS dst_id;
            
  
**Empty result.** | **Empty result.** | **Result:**  
|  src_id | dst_id  
---|---  
16 | 20  
  
#### Return graph elements as query results

openCypher | Spanner Graph  
---|---  
      
    
    MATCH (account:Account)
    WHERE account.id = 16
    RETURN account;

| 
    
    
    GRAPH FinGraph
    MATCH (account:Account)
    WHERE account.id = 16
    RETURN TO_JSON(account) AS account;  
  
In Spanner Graph, query results don't return graph elements. Use the `TO_JSON` function to return graph elements as JSON.

#### Variable-length pattern matching and pattern quantification

Variable-length pattern matching in openCypher is called _path quantification_ in Spanner Graph. Path quantification uses a different syntax, as shown in the following example. For more information, see [Quantified path pattern](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-patterns#quantified_paths).

openCypher | Spanner Graph  
---|---  
      
    
    MATCH (src:Account)-[:Transfers*1..2]->(dst:Account)
    WHERE src.id = 16
    RETURN dst.id
    ORDER BY dst.id;
         

| 
    
    
    GRAPH FinGraph
    MATCH (src:Account)-[:Transfers]->{1,2}(dst:Account)
    WHERE src.id = 16
    RETURN dst.id
    ORDER BY dst.id;
            
  
#### Variable-length pattern: list of elements

Spanner Graph lets you directly access the variables used in path quantifications. In the following example, `e` in Spanner Graph is the same as `edges(p)` in openCypher.

openCypher | Spanner Graph  
---|---  
      
    
    MATCH p=(src:Account)-[:Transfers*1..3]->(dst:Account)
    WHERE src.id = 16
    RETURN edges(p);
          

| 
    
    
    GRAPH FinGraph
    MATCH (src:Account) -[e:Transfers]->{1,3} (dst:Account)
    WHERE src.id = 16
    RETURN TO_JSON(e) AS e;
           
  
#### Shortest path

openCypher has two built-in functions to find the shortest path between nodes: `shortestPath` and `allShortestPath`.

  * `shortestPath` finds a single shortest path between nodes.
  * `allShortestPath` finds all the shortest paths between nodes. There can be multiple paths of the same length.



Spanner Graph uses a different syntax to find a single shortest path between nodes: `ANY SHORTEST` for `shortestPath.` The `allShortestPath` function isn't supported in Spanner Graph.

openCypher | Spanner Graph  
---|---  
      
    
    MATCH
      (src:Account {id: 7}),
      (dst:Account {id: 20}),
      p = shortestPath((src)-[*1..10]->(dst))
    RETURN length(p) AS path_length;
          

| 
    
    
    GRAPH FinGraph
    MATCH ANY SHORTEST
      (src:Account {id: 7})-[e:Transfers]->{1, 3}
      (dst:Account {id: 20})
    RETURN ARRAY_LENGTH(e) AS path_length;
            
  
### Statements and clauses

The following table lists the openCypher clauses, and indicates whether or not they're supported in Spanner Graph.

openCypher  | Spanner Graph  
---|---  
`MATCH` |  Supported. For more information, see [graph pattern matching](https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference#graph-pattern-matching).  
`OPTIONAL MATCH` |  Supported. For more information, see [graph pattern matching](https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference#graph-pattern-matching).  
`RETURN / WITH` |  Supported. For more information, see the [ `RETURN` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_return) and the [ `WITH` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_with).   
Spanner Graph requires explicit aliasing for complicated expressions.  
  
Supported. | 
    
    
    GRAPH FinGraph
    MATCH (p:Person)
    RETURN EXTRACT(YEAR FROM p.birthday) AS birthYear;  
  
  
Not supported. | 
    
    
    GRAPH FinGraph
    MATCH (p:Person)
    RETURN EXTRACT(YEAR FROM p.birthday); -- No aliasing  
  
`WHERE` |  Supported. For more information, see the definition for [ graph pattern](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-patterns#graph_pattern_definition).  
`ORDER BY` |  Supported. For more information, see the [ `ORDER BY` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_order_by).  
`SKIP / LIMIT` |  Supported. For more information, see the [ `SKIP` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_skip) and the [ `LIMIT` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_limit).  
  
Spanner Graph requires a constant expression for the offset and the limit.   
  
Supported. | 
    
    
    GRAPH FinGraph
    MATCH (n:Account)
    RETURN n.id
    SKIP @offsetParameter
    LIMIT 3;  
  
  
Not supported. | 
    
    
    GRAPH FinGraph
    MATCH (n:Account)
    RETURN n.id
    LIMIT VALUE {
      MATCH (m:Person)
      RETURN COUNT(*) AS count
    } AS count; -- Not a constant expression  
  
`UNION` |  Supported. For more information, see [Composite graph query](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-intro#composite_graph_query).   
`UNION ALL` |  Supported. For more information, see [Composite graph query](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-intro#composite_graph_query).  
`UNWIND` |  Supported by [`FOR` statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-query-statements#gql_for).  
| 
    
    
    GRAPH FinGraph
    LET arr = [1, 2, 3]
    FOR num IN arr
    RETURN num;  
  
`MANDATORY MATCH` |  Not supported.  
`CALL[YIELD...]` |  Not supported.  
`CREATE`, `DELETE`, `SET`, `REMOVE`, `MERGE` |  To learn more, see the [Mutation](https://docs.cloud.google.com/spanner/docs/graph/opencypher-reference#mutation) section and [Insert, update, or delete data in Spanner Graph](https://docs.cloud.google.com/spanner/docs/graph/insert-update-delete-data).   
  
### Data types

Spanner Graph supports all GoogleSQL data types. For more information, see [Data types in GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types).

The following sections compare openCypher data types with Spanner Graph data types.

#### Structural type

openCypher | Spanner Graph  
---|---  
Node | [Node](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-data-types#graph_element_type)  
Edge | [Edge](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-data-types#graph_element_type)  
Path | [Path](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-data-types#graph_path_type)  
  
#### Property type

openCypher | Spanner Graph  
---|---  
`INT` | [`INT64`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#integer_types)  
`FLOAT` | [`FLOAT64`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#floating_point_types)  
`STRING` | [`STRING`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#string_type)  
`BOOLEAN` | [`BOOL`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#boolean_type)  
`LIST`   
A homogeneous list of simple types.  
For example, List of `INT`, List of `STRING`.  
You can't mix `INT` and `STRING` in a single list. | [`ARRAY`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#array_type)  
  
#### Composite type

openCypher | Spanner Graph  
---|---  
`LIST` | [`ARRAY`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#array_type) or [`JSON`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#json_type)  
  
`MAP` | [`STRUCT`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#struct_type) or [`JSON`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#json_type)  
  
  
Spanner Graph doesn't support heterogeneous lists of different types or maps of a dynamic key list and heterogeneous element value types. Use JSON for these use cases.

#### Type Coercion

openCypher | Spanner Graph  
---|---  
`INT` -> `FLOAT` | Supported.  
  
For more information about type conversion rules, see [Conversion rules in GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/conversion_rules).

### Functions and expressions

Besides graph functions and expressions, Spanner Graph also supports all GoogleSQL built-in functions and expressions.

This section lists openCypher functions and expressions and their equivalents in Spanner Graph.

**Note:** For a complete list of functions, see [GoogleSQL functions](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/functions-all). For a complete list of operators, see [GoogleSQL operators](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/operators). For a complete list of conditional expressions, see [GoogleSQL conditional expressions](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/conditional_expressions).

#### Structural type functions and expressions

Type | openCypher  
function or expression | Spanner Graph  
function or expression  
  
---|---|---  
  
Node and Edge | `exists(n.prop)` | [`PROPERTY_EXISTS(n, prop)`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-operators#property_exists_predicate)  
`id` (returns integer) | Not supported.  
`properties` | [`TO_JSON`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/json_functions#to_json)  
  
`keys`  
(property type names, but not property values) | [`PROPERTY_NAMES`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-gql-functions#property_names)  
  
`labels` | [`LABELS`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-gql-functions#labels)  
Edge | `endNode` | Not supported.  
`startNode` | Not supported.  
`type` | `LABELS`  
Path | `length` | Not supported.  
`nodes` | Not supported.  
`relationships` | Not supported.  
Node and Edge | `.   
property reference` | `.`  
`[]   
dynamic property reference  
| 
    
    
    MATCH (n)
    RETURN n[n.name]  
  
---  
  
` Not supported.  
Pattern As Expression | `size(pattern)` | Not supported. Use a subquery as following  
| 
    
    
    VALUE {
      MATCH pattern
      RETURN COUNT(*) AS count;
    }  
  
---  
  
#### Property type functions and expressions

Type | openCypher  
function or expression | Spanner Graph  
function or expression  
  
---|---|---  
Scalar | `coalesce` | `COALESCE`  
`head` | `ARRAY_FIRST`  
`last` | `ARRAY_LAST`  
`size(list)` | `ARRAY_LENGTH`  
`size(string)` | `LENGTH`  
`timestamp` | `UNIX_MILLIS(CURRENT_TIMESTAMP())`  
`toBoolean`/`toFloat`/`toInteger` | `CAST(expr AS type)`  
Aggregate | `avg` | `AVG`  
`collect` | `ARRAY_AGG`  
`count | `COUNT` `  
`max` | `MAX`  
`min` | `MIN`  
`percentileCont` | `PERCENTILE_CONT`  
`percentileDisc` | `PERCENTILE_DISC`  
`stDev` | `STDDEV`  
`stDevP` | Not supported.  
`sum` | `SUM`  
List | `range` | `GENERATE_ARRAY`  
`reverse` | `ARRAY_REVERSE`  
`tail` | Spanner Graph doesn't support `tail`.  
Use `ARRAY_SLICE` and `ARRAY_LENGTH` instead.  
Mathematical | `abs` | `ABS`  
`ceil` | `CEIL`  
`floor` | `FLOOR`  
`rand` | `RAND`  
`round` | `ROUND`  
`sign` | `SIGN`  
`e` | `EXP(1)`  
`exp` | `EXP`  
`log` | `LOG`  
`log10` | `LOG10`  
`sqrt` | `SQRT`  
`acos` | `ACOS`  
`asin` | `ASIN`  
`atan` | `ATAN`  
`atan2` | `ATAN2`  
`cos` | `COS`  
`cot` | `COT`  
`degrees` | `r * 90 / ASIN(1)`  
`pi` | `ACOS(-1)`  
`radians` | `d * ASIN(1) / 90`  
`sin` | `SIN`  
`tan` | `TAN`  
String | `left` | `LEFT`  
`ltrim` | `LTRIM`  
`replace` | `REPLACE`  
`reverse` | `REVERSE`  
`right` | `RIGHT`  
`rtrim` | `RTRIM`  
`split` | `SPLIT`  
`substring` | `SUBSTR`  
`tolower` | `LOWER`  
`tostring` | `CAST(expr AS STRING)`  
`toupper` | `UPPER`  
`trim` | `TRIM`  
DISTINCT | `DISTINCT` | `DISTINCT`  
Mathematical | `+` | `+`  
`-` | `-`  
`*` | `*`  
`/` | `/`  
`%` | `MOD`  
`^` | `POW`  
Comparison | `=` | `=`  
`<>` | `<>`  
`<` | `<`  
`>` | `>`  
`<=` | `<=`  
`>=` | `>=`  
`IS [NOT] NULL` | `IS [NOT] NULL`  
Chain of comparison  
| 
    
    
    a < b < c  
  
---  
  
Spanner Graph doesn't support a chain of comparison. This is equivalent to comparisons conjuncted with `AND`.   
For example:   
| 
    
    
          a < b AND b < C
            
  
---  
  
Boolean | `AND` | `AND`  
`OR` | `OR`  
`XOR`  
| Spanner Graph doesn't support `XOR`. Write the query with `<>`.  
  
For example:  
| 
    
    
          boolean_1 <> boolean_2
            
  
---  
  
`NOT` | `NOT`  
String | `STARTS WITH` | `STARTS_WITH`  
`ENDS WITH` | `ENDS_WITH`  
`CONTAINS` | `REGEXP_CONTAINS`  
`+` | `CONCAT`  
List | `+` | `ARRAY_CONCAT`  
`IN` | `ARRAY_INCLUDES`  
`[]` | `[]`  
  
#### Other expressions

openCypher | Spanner Graph  
---|---  
Case expression | Supported.  
Exists subquery | Supported.  
Map projection | Not supported.  
`STRUCT` types provide similar functionalities.  
List comprehension | Not supported.  
[`GENERATE_ARRAY`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/array_functions#generate_array) and [`ARRAY_TRANSFORM`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/array_functions#array_transform) cover the majority of use cases.  
  
### Query parameter

The following queries show the difference between using parameters in openCypher and in Spanner Graph.

| openCypher | Spanner Graph  
---|---|---  
Parameter | 
    
    
    MATCH (n:Person)
    WHERE n.id = $id
    RETURN n.name;

| 
    
    
    GRAPH FinGraph
    MATCH (n:Person)
    WHERE n.id = @id
    RETURN n.name;  
  
## Mutation

Spanner Graph uses [GoogleSQL DML](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/dml-syntax) to mutate the node and edge input tables. For more information, see [Insert, update, or delete Spanner Graph data](https://docs.cloud.google.com/spanner/docs/graph/insert-update-delete-data).

### Create node and edge

| openCypher | Spanner Graph  
---|---|---  
Create nodes and edges | 
    
    
    CREATE (:Person {id: 100, name: 'John'});
    CREATE (:Account {id: 1000, is_blocked: FALSE});
      
    MATCH (p:Person {id: 100}),
          (a:Account {id: 1000})
    CREATE (p)-[:Owns {create_time: timestamp()}]->(a);

| 
    
    
    INSERT INTO
    Person (id, name)
    VALUES (100, "John");
      
    INSERT INTO
    Account (id, is_blocked)
    VALUES (1000, FALSE);
      
    INSERT INTO PersonOwnAccount (id, account_id, create_time)
    VALUES (100, 1000, CURRENT_TIMESTAMP());  
  
Create nodes and edges with query results  
| 
    
    
    MATCH (a:Account {id: 1}), (oa:Account)
    WHERE oa <> a
    CREATE (a)-[:Transfers {amount: 100, create_time: timestamp()}]->(oa);

| 
    
    
    INSERT INTO AccountTransferAccount(id, to_id, create_time, amount)
    SELECT a.id, oa.id, CURRENT_TIMESTAMP(), 100
    FROM GRAPH_TABLE(
      FinGraph
      MATCH
        (a:Account {id:1000}),
        (oa:Account)
      WHERE oa <> a
    );  
  
In Spanner Graph, the labels are statically assigned according to the `CREATE PROPERTY GRAPH` DDL statement.

### Update node and edge

| openCypher | Spanner Graph  
---|---|---  
Update properties | 
    
    
    MATCH (p:Person {id: 100})
    SET p.country = 'United States';

| 
    
    
    UPDATE Person AS p
    SET p.country = 'United States'
    WHERE p.id = 100;  
  
To update Spanner Graph labels, see [Create, update, or drop a Spanner Graph schema](https://docs.cloud.google.com/spanner/docs/graph/create-update-drop-schema).

### Merge node and edge

| openCypher | Spanner Graph  
---|---|---  
Insert new element or update properties | 
    
    
    MERGE (p:Person {id: 100, country: 'United States'});

| 
    
    
    INSERT OR UPDATE INTO Person
    (id, country)
    VALUES (100, 'United States');  
  
### Delete node and edge

Deleting edges is the same as deleting the input table.

| openCypher | Spanner Graph  
---|---|---  
Delete nodes and edges | 
    
    
    MATCH (p:Person {id:100}), (a:Account {id:1000})
    DELETE (p)-[:Owns]->(a);

| 
    
    
    DELETE PersonOwnAccount
    WHERE id = 100 AND account_id = 1000;  
  
Deleting nodes requires handling potential dangling edges. When `DELETE CASCADE` is specified, `DELETE` removes the associated edges of nodes like `DETACH DELETE` in openCypher. For more information, see Spanner [schema overview](https://docs.cloud.google.com/spanner/docs/schema-and-data-model).

| openCypher | Spanner Graph  
---|---|---  
Delete nodes and associated edges | 
    
    
    DETACH DELETE (:Account {id: 1000});

| 
    
    
    DELETE Account
    WHERE id = 1000;  
  
### Return mutation results

| openCypher | Spanner Graph  
---|---|---  
Return results after insertion or update | 
    
    
    MATCH (p:Person {id: 100})
    SET p.country = 'United States'
    RETURN p.id, p.name;

| 
    
    
    UPDATE Person AS p
    SET p.country = 'United States'
    WHERE p.id = 100
    THEN RETURN id, name;  
  
Return results after deletion | 
    
    
    DELETE (p:Person {id: 100})
    RETURN p.country;

| 
    
    
    DELETE FROM Person
    WHERE id = 100
    THEN RETURN country;  
  
## What's next

  * [Spanner Graph overview](https://docs.cloud.google.com/spanner/docs/graph/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
