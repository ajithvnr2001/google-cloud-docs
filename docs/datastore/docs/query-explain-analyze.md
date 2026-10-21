---
url: https://docs.cloud.google.com/datastore/docs/query-explain-analyze/
title: Use Query Explain \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:34.274378+00:00
---

# Use Query Explain  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/query-explain-analyze/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Use Query Explain Stay organized with collections  Save and categorize content based on your preferences. 

Query Explain lets you submit Datastore mode queries to the backend and receive detailed performance statistics on backend query execution in return. It functions like the `EXPLAIN ANALYZE` operation in many relational database systems.

You can send Query Explain requests using the [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries).

Query Explain results help you understand how your queries are executed, showing you inefficiencies and the location of likely server-side bottlenecks.

Query Explain:

  * Provides insights on planning phase so you can adjust your query indexes and boost efficiency.
  * Helps you understand your cost and performance on a per-query basis and lets you quickly iterate through different query patterns in order to optimize their usage.



## Understand Query Explain options: default and analyze

Query Explain operations can be performed using the _default_ option or _analyze_ option.

With the default option, Query Explain plans the query, but skips over the execution stage. This will return planner stage information. You can use this to check that a query has the necessary indexes and understand which indexes are used. This will help you verify, for example, that a particular query is using a composite index over having to intersect over many different indexes.

With the analyze option, Query Explain both plans and executes the query. This returns all the previously mentioned planner information along with statistics from the query execution runtime. This will include billing information along with system-level insights into the query execution. You can use this tooling to test various query and index configurations to optimize their cost and latency.

## What does Query Explain cost?

When a query is explained with the default option, no index or read operations are performed. Regardless of query complexity, one read operation is charged.

When a query is explained with the analyze option, index and read operations are performed, so you are charged for the query as usual. There is no additional charge for the analysis activity, only the usual charge for the query being executed.

## Execute a query with the default option

You can use a client library to submit a default option request.

Note that query explain results are authenticated with [Identity and Access Management](https://docs.cloud.google.com/datastore/docs/access/iam), using the same permissions for regular query operations.

**Note:** One query execution is analyzed at a time; therefore, query explain timing results may vary from request to request. The tool can help you spot significant structural inefficiencies, but is not intended to provide aggregate statistics on query performance.

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datastore.[Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html);
    import com.google.cloud.datastore.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html);
    import com.google.cloud.datastore.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html);
    import com.google.cloud.datastore.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html);
    import com.google.cloud.datastore.[QueryResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.QueryResults.html);
    import com.google.cloud.datastore.models.[ExplainMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html);
    import com.google.cloud.datastore.models.[ExplainOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainOptions.html);
    import com.google.cloud.datastore.models.[PlanSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html);
    import java.util.List;
    import java.util.Map;
    import java.util.Optional;
    
    public class QueryProfileExplain {
      public static void invoke() throws Exception {
        // Instantiates a client
        [Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html) datastore = [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html).getDefaultInstance().getService();
    
        // Build the query
        Query<Entity> query = [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html).[newEntityQueryBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html#com_google_cloud_datastore_Query_newEntityQueryBuilder__)().setKind("Task").build();
    
        // Set the explain options to get back *only* the plan summary
        QueryResults<Entity> results = datastore.[run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore__T_run_com_google_cloud_datastore_Query_T__com_google_cloud_datastore_DatastoreExecutionOptions_)(query, ExplainOptions.newBuilder().build());
    
        // Get the explain metrics
        Optional<ExplainMetrics> explainMetrics = results.getExplainMetrics();
        if (!explainMetrics.isPresent()) {
          throw new Exception("No explain metrics returned");
        }
        [PlanSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html) planSummary = explainMetrics.get().getPlanSummary();
        List<Map<String, Object>> indexesUsed = planSummary.[getIndexesUsed](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html#com_google_cloud_datastore_models_PlanSummary_getIndexesUsed__)();
        System.out.println("----- Indexes Used -----");
        indexesUsed.forEach(map -> map.forEach((key, val) -> System.out.println(key + ": " + val)));
      }
    }

See the `indexes_used` field in the response to learn about the indexes used in the query plan:
    
    
    "indexes_used": [
            {"query_scope": "Collection Group", "properties": "(__name__ ASC)"},
    ]

For more information about the report, see the [report reference](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference).

## Execute a query with the analyze option

You can use a client library to submit a default option request.

Note that query analyze results are authenticated with [Identity and Access Management (IAM)](https://docs.cloud.google.com/datastore/docs/access/iam), using the same permissions for regular query operations.

**Note:** One query execution is analyzed at a time; therefore, query timing results may vary from request to request. The tool can help you spot significant structural inefficiencies, but is not intended to provide aggregate statistics on query performance.

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datastore.[Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html);
    import com.google.cloud.datastore.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html);
    import com.google.cloud.datastore.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html);
    import com.google.cloud.datastore.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html);
    import com.google.cloud.datastore.[QueryResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.QueryResults.html);
    import com.google.cloud.datastore.models.[ExecutionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExecutionStats.html);
    import com.google.cloud.datastore.models.[ExplainMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html);
    import com.google.cloud.datastore.models.[ExplainOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainOptions.html);
    import com.google.cloud.datastore.models.[PlanSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html);
    import java.util.List;
    import java.util.Map;
    
    public class QueryProfileExplainAnalyze {
      public static void invoke() throws Exception {
        // Instantiates a client
        [Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html) datastore = [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html).getDefaultInstance().getService();
    
        // Build the query
        Query<Entity> query = [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html).[newEntityQueryBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html#com_google_cloud_datastore_Query_newEntityQueryBuilder__)().setKind("Task").build();
    
        // Set explain options with analzye = true to get back the query stats, plan info, and query
        // results
        QueryResults<Entity> results =
            datastore.[run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore__T_run_com_google_cloud_datastore_Query_T__com_google_cloud_datastore_DatastoreExecutionOptions_)(query, ExplainOptions.newBuilder().setAnalyze(true).build());
    
        // Get the result set stats
        if (!results.getExplainMetrics().isPresent()) {
          throw new Exception("No explain metrics returned");
        }
        [ExplainMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html) explainMetrics = results.getExplainMetrics().get();
    
        // Get the execution stats
        if (!explainMetrics.[getExecutionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html#com_google_cloud_datastore_models_ExplainMetrics_getExecutionStats__)().isPresent()) {
          throw new Exception("No execution stats returned");
        }
    
        [ExecutionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExecutionStats.html) executionStats = explainMetrics.[getExecutionStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html#com_google_cloud_datastore_models_ExplainMetrics_getExecutionStats__)().get();
        Map<String, Object> debugStats = executionStats.[getDebugStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExecutionStats.html#com_google_cloud_datastore_models_ExecutionStats_getDebugStats__)();
        System.out.println("----- Debug Stats -----");
        debugStats.forEach((key, val) -> System.out.println(key + ": " + val));
        System.out.println("----------");
    
        long resultsReturned = executionStats.[getResultsReturned](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExecutionStats.html#com_google_cloud_datastore_models_ExecutionStats_getResultsReturned__)();
        System.out.println("Results returned: " + resultsReturned);
    
        // Get the plan summary
        [PlanSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html) planSummary = explainMetrics.[getPlanSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.ExplainMetrics.html#com_google_cloud_datastore_models_ExplainMetrics_getPlanSummary__)();
        List<Map<String, Object>> indexesUsed = planSummary.[getIndexesUsed](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.models.PlanSummary.html#com_google_cloud_datastore_models_PlanSummary_getIndexesUsed__)();
        System.out.println("----- Indexes Used -----");
        indexesUsed.forEach(map -> map.forEach((key, val) -> System.out.println(key + ": " + val)));
    
        if (!results.hasNext()) {
          throw new Exception("query yielded no results");
        }
    
        // Get the query results
        System.out.println("----- Query Results -----");
        while (results.hasNext()) {
          [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html) entity = results.next();
          System.out.printf("Entity: %s%n", entity);
        }
      }
    }

See the `executionStats` object to find query profiling information such as:
    
    
    {
        "resultsReturned": "5",
        "executionDuration": "0.100718s",
        "readOperations": "5",
        "debugStats": {
                   "index_entries_scanned": "95000",
                   "documents_scanned": "5"
                   "billing_details": {
                         "documents_billable": "5",
                         "index_entries_billable": "0",
                         "small_ops": "0",
                         "min_query_cost": "0",
                   }
        }
    }

For more information about the report, see the [report reference](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference).

## Interpret results and make adjustments

The following example scenario queries movies by genre and country of production and demonstrates how to optimize the indexes used by the query.

**Note:** Query Explain is designed for useful ad hoc analysis; its report format will evolve to maximize ease of reading and understanding, not suitability for machine processing. Some returned metrics are expected to change as Datastore mode evolves (metrics may be added, removed, or updated) and are not covered by the same deprecation policy as other Datastore mode APIs.

For more information about the report, see the [Query Explain report reference](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference).

For illustration, assume the equivalent of this SQL query.
    
    
    SELECT *
    FROM movies
    WHERE category = 'Romantic' AND country = 'USA';

If we use the analyze option, the following report output shows the query runs on single-field indexes `(category ASC, __name__ ASC)` and `(country ASC, __name__ ASC)`. It scans 16500 index entries, but returns only 1200 documents.
    
    
    // Output query planning info
    "indexes_used": [
        {"query_scope": "Collection Group", "properties": "(category ASC, __name__ ASC)"},
        {"query_scope": "Collection Group", "properties": "(country ASC, __name__ ASC)"},
    ]
    
    // Output query status
    {
        "resultsReturned": "1200",
        "executionDuration": "0.118882s",
        "readOperations": "1200",
        "debugStats": {
                   "index_entries_scanned": "16500",
                   "documents_scanned": "1200"
                   "billing_details": {
                         "documents_billable": "1200",
                         "index_entries_billable": "0",
                         "small_ops": "0",
                         "min_query_cost": "0",
                   }
        }
    }

To optimize the performance of executing the query, you can create a fully-covered composite index (category ASC, country ASC, __name__ ASC).

Running the query in analyze mode again, we can see that the newly-created index is selected for this query, and the query runs much faster and more efficiently.
    
    
    // Output query planning info
        "indexes_used": [
            {"query_scope": "Collection Group", "properties": "(category ASC, country ASC, __name__ ASC)"}
            ]
    
    // Output query stats
    {
        "resultsReturned": "1200",
        "executionDuration": "0.026139s",
        "readOperations": "1200",
        "debugStats": {
                   "index_entries_scanned": "1200",
                   "documents_scanned": "1200"
                   "billing_details": {
                         "documents_billable": "1200",
                         "index_entries_billable": "0",
                         "small_ops": "0",
                         "min_query_cost": "0",
                   }
        }
    }

## What's next

  * [Learn more about the Query Explain report](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference)
  * [Learn more about optimizing queries and indexes](https://docs.cloud.google.com/datastore/docs/concepts/optimize-indexes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
