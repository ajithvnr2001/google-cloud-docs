---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-stream-exactly-once/
title: Stream to BigQuery with exactly-once processing \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:13.402384+00:00
---

# Stream to BigQuery with exactly-once processing  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-bigquery-stream-exactly-once/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Stream to BigQuery with exactly-once processing Stay organized with collections  Save and categorize content based on your preferences. 

Use the Storage Write API to stream from Dataflow to BigQuery with exactly-once processing

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write from Dataflow to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery)



## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.services.bigquery.model.TableRow;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.testing.TestStream;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TimestampedValue;
    import org.apache.beam.sdk.values.TypeDescriptor;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.Duration;
    import org.joda.time.Instant;
    
    public class BigQueryStreamExactlyOnce {
      // Create a PTransform that sends simulated streaming data. In a real application, the data
      // source would be an external source, such as Pub/Sub.
      private static TestStream<String> createEventSource() {
        Instant startTime = new Instant(0);
        return TestStream.create(StringUtf8Coder.of())
            .advanceWatermarkTo(startTime)
            .addElements(
                TimestampedValue.of("Alice,20", startTime),
                TimestampedValue.of("Bob,30",
                    startTime.plus(Duration.standardSeconds(1))),
                TimestampedValue.of("Charles,40",
                    startTime.plus(Duration.standardSeconds(2))),
                TimestampedValue.of("Dylan,Invalid value",
                    startTime.plus(Duration.standardSeconds(2))))
            .advanceWatermarkToInfinity();
      }
    
      public static PipelineResult main(String[] args) {
        // Parse the pipeline options passed into the application. Example:
        //   --projectId=$PROJECT_ID --datasetName=$DATASET_NAME --tableName=$TABLE_NAME
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        PipelineOptionsFactory.register(ExamplePipelineOptions.class);
        ExamplePipelineOptions options = PipelineOptionsFactory.fromArgs(args)
            .withValidation()
            .as(ExamplePipelineOptions.class);
        options.setStreaming(true);
    
        // Create a pipeline and apply transforms.
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            // Add a streaming data source.
            .apply(createEventSource())
            // Map the event data into TableRow objects.
            .apply(MapElements
                .into(TypeDescriptor.of(TableRow.class))
                .via((String x) -> {
                  String[] columns = x.split(",");
                  return new TableRow().set("user_name", columns[0]).set("age", columns[1]);
                }))
            // Write the rows to BigQuery
            .apply(BigQueryIO.writeTableRows()
                .to(String.format("%s:%s.%s",
                    options.getProjectId(),
                    options.getDatasetName(),
                    options.getTableName()))
                .withCreateDisposition(CreateDisposition.CREATE_NEVER)
                .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                .withMethod(Write.Method.STORAGE_WRITE_API)
                // For exactly-once processing, set the triggering frequency.
                .withTriggeringFrequency(Duration.standardSeconds(5)))
            // Get the collection of write errors.
            .getFailedStorageApiInserts()
            .apply(MapElements.into(TypeDescriptors.strings())
                // Process each error. In production systems, it's useful to write the errors to
                // another destination, such as a dead-letter table or queue.
                .via(
                    x -> {
                      System.out.println("Failed insert: " + x.getErrorMessage());
                      System.out.println("Row: " + x.getRow());
                      return "";
                    }));
        return pipeline.run();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
