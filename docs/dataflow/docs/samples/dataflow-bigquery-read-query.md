---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-query/
title: Read from a query \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:44.233895+00:00
---

# Read from a query  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Read from a query Stay organized with collections  Save and categorize content based on your preferences. 

Use the BigQueryIO connector to read from a query result.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read from BigQuery to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.Row;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class BigQueryReadFromQuery {
      public static void main(String[] args) {
        // The SQL query to run inside BigQuery.
        final String queryString =
            "SELECT repo_name as repo, COUNT(*) as count "
                + "FROM `bigquery-public-data.github_repos.sample_commits` "
                + "GROUP BY repo_name";
    
        // Parse the pipeline options passed into the application.
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        PipelineOptions options = PipelineOptionsFactory.fromArgs(args)
            .withValidation().create();
    
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("query", queryString)
            .build();
    
        // Create a pipeline and apply transforms.
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            .apply(Managed.read(Managed.BIGQUERY).withConfig(config)).getSinglePCollection()
            .apply(MapElements
                .into(TypeDescriptors.strings())
                // Access individual fields in the row.
                .via((Row row) -> {
                  String output = String.format("Repo: %s, commits: %d%n",
                      row.getString("repo"),
                      row.getInt64("count"));
                  System.out.println(output);
                  return output;
                }));
        pipeline.run().waitUntilFinish();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
