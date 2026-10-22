---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-tablerows/
title: Read into TableRow objects \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:43.862896+00:00
---

# Read into TableRow objects  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-read-tablerows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Read into TableRow objects Stay organized with collections  Save and categorize content based on your preferences. 

Use the BigQueryIO connector to read into TableRow objects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read from BigQuery to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.services.bigquery.model.TableRow;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.TypedRead.Method;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptor;
    
    public class BiqQueryReadTableRows {
      public static void main(String[] args) {
        // Parse the pipeline options passed into the application. Example:
        //   --projectId=$PROJECT_ID --datasetName=$DATASET_NAME --tableName=$TABLE_NAME
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        PipelineOptionsFactory.register(ExamplePipelineOptions.class);
        ExamplePipelineOptions options = PipelineOptionsFactory.fromArgs(args)
            .withValidation()
            .as(ExamplePipelineOptions.class);
    
        // Create a pipeline and apply transforms.
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            // Read table data into TableRow objects.
            .apply(BigQueryIO.readTableRows()
                .from(String.format("%s:%s.%s",
                    options.getProjectId(),
                    options.getDatasetName(),
                    options.getTableName()))
                .withMethod(Method.DIRECT_READ)
            )
            // The output from the previous step is a PCollection<TableRow>.
            .apply(MapElements
                .into(TypeDescriptor.of(TableRow.class))
                // Use TableRow to access individual fields in the row.
                .via((TableRow row) -> {
                  var name = (String) row.get("user_name");
                  var age = (String) row.get("age");
                  System.out.printf("Name: %s, Age: %s%n", name, age);
                  return row;
                }));
        pipeline.run().waitUntilFinish();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
