---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-query-filter-or/
title: Create a union of two filters (OR operator) \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:23.728164+00:00
---

# Create a union of two filters (OR operator)  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-query-filter-or/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Create a union of two filters (OR operator) Stay organized with collections  Save and categorize content based on your preferences. 

This snippet creates the union (logical OR) of two queries, where the results of each query is combined in the final results.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Datastore queries](https://docs.cloud.google.com/datastore/docs/concepts/queries)



## Code sample

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datastore.[Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html);
    import com.google.cloud.datastore.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html);
    import com.google.cloud.datastore.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html);
    import com.google.cloud.datastore.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html);
    import com.google.cloud.datastore.[QueryResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.QueryResults.html);
    import com.google.cloud.datastore.[StructuredQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.html).[CompositeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.CompositeFilter.html);
    import com.google.cloud.datastore.[StructuredQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.html).[Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.Filter.html);
    import com.google.cloud.datastore.[StructuredQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.html).[PropertyFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.PropertyFilter.html);
    
    public class OrFilterQuery {
      public static void invoke() throws Exception {
    
        // Instantiates a client
        [Datastore](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html) datastore = [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DatastoreOptions.html).getDefaultInstance().getService();
        String propertyName = "description";
    
        // Create the two filters
        [Filter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.Filter.html) orFilter =
            [CompositeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.CompositeFilter.html).[or](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.CompositeFilter.html#com_google_cloud_datastore_StructuredQuery_CompositeFilter_or_com_google_cloud_datastore_StructuredQuery_Filter_com_google_cloud_datastore_StructuredQuery_Filter____)(
                [PropertyFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.PropertyFilter.html).[eq](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.PropertyFilter.html#com_google_cloud_datastore_StructuredQuery_PropertyFilter_eq_java_lang_String_boolean_)(propertyName, "Feed cats"),
                [PropertyFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.PropertyFilter.html).[eq](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.PropertyFilter.html#com_google_cloud_datastore_StructuredQuery_PropertyFilter_eq_java_lang_String_boolean_)(propertyName, "Buy milk"));
    
        // Build the query
        Query<Entity> query = [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html).[newEntityQueryBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Query.html#com_google_cloud_datastore_Query_newEntityQueryBuilder__)().setKind("Task").[setFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StructuredQuery.Builder.html#com_google_cloud_datastore_StructuredQuery_Builder_setFilter_com_google_cloud_datastore_StructuredQuery_Filter_)(orFilter).build();
    
        // Get the results back from Datastore
        QueryResults<Entity> results = datastore.[run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Datastore.html#com_google_cloud_datastore_Datastore__T_run_com_google_cloud_datastore_Query_T__com_google_cloud_datastore_DatastoreExecutionOptions_)(query);
    
        if (!results.hasNext()) {
          throw new Exception("query yielded no results");
        }
    
        while (results.hasNext()) {
          [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Entity.html) entity = results.next();
          System.out.printf("Entity: %s%n", entity);
        }
      }
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    from google.cloud.datastore import query
    
    
    def query_filter_or(project_id: str) -> None:
        """Builds a union of two queries (OR) filter.
    
        Arguments:
            project_id: your Google Cloud Project ID
        """
        client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)(project=project_id)
    
        or_query = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="Task")
        or_filter = query.[Or](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.Or.html)(
            [
                query.[PropertyFilter](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.PropertyFilter.html)("description", "=", "Buy milk"),
                query.[PropertyFilter](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.PropertyFilter.html)("description", "=", "Feed cats"),
            ]
        )
    
        or_query.[add_filter](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.Query.html#google_cloud_datastore_query_Query_add_filter)(filter=or_filter)
    
        results = list(or_query.fetch())
        for result in results:
            print(result["description"])
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
