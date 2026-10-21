---
url: https://docs.cloud.google.com/datastore/docs/multiple-range-optimize-indexes/
title: Optimize queries with range and inequality filters on multiple properties \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:40.303640+00:00
---

# Optimize queries with range and inequality filters on multiple properties  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/multiple-range-optimize-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Optimize queries with range and inequality filters on multiple properties Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples of indexing strategies that you can use for queries with range and inequality filters on multiple fields to create an efficient query experience.

Before you optimize your queries, read about [range and inequality filters on multiple properties](https://docs.cloud.google.com/datastore/docs/multiple-range-fields) concepts .

## Optimize queries with Query Explain

To determine if the query and indexes used are optimal, you can create a query using [Query Explain](https://docs.cloud.google.com/datastore/docs/query-explain-analyze) and review the execution summary.

### Java
    
    
    ...
    // Build the query
    Query<Entity> query =
        Query.newEntityQueryBuilder()
            .setKind("employees")
            .setFilter(
                CompositeFilter.and(
                    PropertyFilter.gt("salary", 100000), PropertyFilter.gt("experience", 0)))
            .setOrderBy(OrderBy("experience"), OrderBy("salary"))
            .build();
    
    // Set the explain options to get back *only* the plan summary
    QueryResults<Entity> results = datastore.run(query, ExplainOptions.newBuilder().build());
    
    // Get the explain metrics
    Optional<ExplainMetrics> explainMetrics = results.getExplainMetrics();
    if (!explainMetrics.isPresent()) {
      throw new Exception("No explain metrics returned");
    }
    
    // Get the plan summary
    PlanSummary planSummary = explainMetrics.get().getPlanSummary();
    List<Map<String, Object>> indexesUsed = planSummary.getIndexesUsed();
    System.out.println("----- Indexes Used -----");
    indexesUsed.forEach(map -> map.forEach((s, o) -> System.out.println(s + ": " + o)));
    
    // Get the execution stats
    if (!explainMetrics.getExecutionStats().isPresent()) {
      throw new Exception("No execution stats returned");
    }
    
    ExecutionStats queryStats = explainMetrics.getExecutionStats().get();
    Map<String, Object> debugStats = queryStats.getDebugStats();
    System.out.println("----- Debug Stats -----");
    debugStats.forEach((s, o) -> System.out.println(s + ": " + o));
    

The following example shows how the use of correct index ordering saves the number of entities that Firestore in Datastore mode scans.

### Simple queries

With the [earlier example](https://docs.cloud.google.com/datastore/docs/multiple-range-fields#indexing_considerations) of a collection of employees, the simple query that runs with the `(salary, experience)` index is as follows:

### GQL
    
    
    SELECT *
    FROM /employees
    WHERE salary > 100000 AND experience > 0
    ORDER BY experience, salary;
    

### Java
    
    
    Query<Entity> query =
       Query.newEntityQueryBuilder()
        .setKind("employees")
        .setFilter(
            CompositeFilter.and(
                PropertyFilter.gt("salary", 100000), PropertyFilter.gt("experience", 0)))
        .setOrderBy(OrderBy("experience"), OrderBy("salary"))
        .build();
    

The query scans 95000 index entries only to return 5 entities. A large number of index entries were read but filtered out because they did not satisfy the query predicate.
    
    
    // Output query planning info
    {
            "indexesUsed": [
                {
                    "query_scope": "Collection Group",
                    "properties": "(experience ASC, salary ASC, __name__ ASC)"
                }
            ]
        },
        // Output Query Execution Stats
        {
            "resultsReturned": "5",
            "executionDuration": "2.5s",
            "readOperations": "100",
            "debugStats": {
                "index_entries_scanned": "95000",
                "documents_scanned": "5",
                "billing_details": {
                    "documents_billable": "5",
                    "index_entries_billable": "95000",
                    "small_ops": "0",
                    "min_query_cost": "0"
                }
            }
        }

As per the earlier example, we can infer that the `salary` constraint is more selective than the `experience` constraint.

### GQL
    
    
    SELECT *
    FROM /employees
    WHERE salary > 100000 AND experience > 0
    ORDER BY salary, experience;
    

### Java
    
    
    Query<Entity> query =
       Query.newEntityQueryBuilder()
        .setKind("employees")
        .setFilter(
            CompositeFilter.and(
                PropertyFilter.gt("salary", 100000), PropertyFilter.gt("experience", 0)))
        .setOrderBy(OrderBy("salary"), OrderBy("experience"))
        .build();
    

When you explicitly use the `orderBy()` clause to add the predicates in the earlier order, Firestore in Datastore mode uses the `(salary, experience)` index to run the query. Since the selection of the first range filter is better than the earlier query, the query runs faster and is cost-efficient.
    
    
        // Output query planning info
    {
        "indexesUsed": [
            {
                "query_scope": "Collection Group",
                "properties": "(salary ASC, experience ASC, __name__ ASC)"
            }
        ],
        // Output Query Execution Stats
            "resultsReturned": "5",
            "executionDuration": "0.2s",
            "readOperations": "6",
            "debugStats": {
                "index_entries_scanned": "1000",
                "documents_scanned": "5",
                "billing_details": {
                    "documents_billable": "5",
                    "index_entries_billable": "1000",
                    "small_ops": "0",
                    "min_query_cost": "0"
                }
            }
        }

## What's next

  * Learn about [Query Explain](https://docs.cloud.google.com/datastore/docs/query-explain-analyze).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
