---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-projection-and-filtering/
title: Read with projection and filtering \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:32:49.259157+00:00
---

# Read with projection and filtering  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-projection-and-filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Read with projection and filtering Stay organized with collections  Save and categorize content based on your preferences. 

Use the BigQueryIO connector in DIRECT_READ mode with column projection and filtering.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read from BigQuery to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.Row;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class BigQueryReadWithProjectionAndFiltering {
      public static void main(String[] args) {
        // Parse the pipeline options passed into the application. Example:
        //   --projectId=$PROJECT_ID --datasetName=$DATASET_NAME --tableName=$TABLE_NAME
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        PipelineOptionsFactory.register(ExamplePipelineOptions.class);
        ExamplePipelineOptions options = PipelineOptionsFactory.fromArgs(args)
            .withValidation()
            .as(ExamplePipelineOptions.class);
    
        String tableSpec = String.format("%s:%s.%s",
            options.getProjectId(),
            options.getDatasetName(),
            options.getTableName());
    
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("table", tableSpec)
            .put("row_restriction", "age > 18")
            .put("fields", List.of("user_name", "age"))
            .build();
    
        // Create a pipeline and apply transforms.
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            .apply(Managed.read(Managed.BIGQUERY).withConfig(config)).getSinglePCollection()
            .apply(MapElements
                .into(TypeDescriptors.strings())
                // Access individual fields in the row.
                .via((Row row) -> {
                  String output = String.format("Name: %s, Age: %s%n",
                      row.getString("user_name"),
                      row.getInt64("age"));
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
