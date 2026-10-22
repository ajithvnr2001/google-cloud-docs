---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery/
title: Write from Dataflow to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:02.648381+00:00
---

# Write from Dataflow to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write data from Dataflow to BigQuery.

## Overview

For most use cases, consider using [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-bigquery) to write to BigQuery. Managed I/O provides features such as [automatic upgrades](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#upgrades) and a consistent [configuration API](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#configuration). When writing to BigQuery, Managed I/O automatically chooses the best write method for batch or streaming jobs.

If you need more advanced performance tuning, consider using the [`BigQueryIO`](https://beam.apache.org/documentation/io/built-in/google-bigquery/) connector. For more information, see Use the `BigQueryIO` connector in this document.

## Performance

The following table shows performance metrics for various workloads. These workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.49.0 for Java. They did not use Runner v2.

100 M records | 1 kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Storage Write](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L223) | 55 MBps | 54,000 elements per second  
[Avro Load](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L194) | 78 MBps | 77,000 elements per second  
[Json Load](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L201) | 54 MBps | 53,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

## Use the `BigQueryIO` connector

The [BigQuery I/O connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/) supports the following methods for writing to BigQuery:

  * `STORAGE_WRITE_API`. In this mode, the connector performs direct writes to BigQuery storage, using the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api). The Storage Write API (gRPC) combines streaming ingestion and batch loading into a single high-performance API. This mode guarantees exactly-once semantics.
  * `STORAGE_API_AT_LEAST_ONCE`. This mode also uses the Storage Write API (gRPC), but provides at-least-once semantics. This mode results in lower latency for most pipelines. However, duplicate writes are possible.
  * `FILE_LOADS`. In this mode, the connector writes the input data to staging files in Cloud Storage. Then it runs a BigQuery [load job](https://docs.cloud.google.com/bigquery/docs/batch-loading-data) to load the data into BigQuery. The mode is the default for bounded `PCollections`, which are most commonly found in batch pipelines.
  * `STREAMING_INSERTS`. In this mode, the connector uses the [legacy streaming API](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery). This mode uses [best-effort deduplication](https://docs.cloud.google.com/bigquery/docs/write-api-rest#dataconsistency), which can result in some duplicates. This mode is the default for unbounded `PCollections`, but is not recommended for new projects.



When choosing a write method, consider the following points:

  * For streaming jobs, consider using `STORAGE_WRITE_API` or `STORAGE_API_AT_LEAST_ONCE`, because these modes write directly to BigQuery storage, without using intermediate staging files.
  * If you run the pipeline using [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes), set the write mode to `STORAGE_API_AT_LEAST_ONCE`. This setting is more efficient and matches the semantics of at-least-once streaming mode. The `FILE_LOADS` write method is incompatible with at-least-once streaming mode.
  * File loads and Storage Write API (gRPC) have different [quotas and limits](https://docs.cloud.google.com/bigquery/quotas).
  * Load jobs use either the shared BigQuery slot pool or reserved slots. To use reserved slots, run the load job in a project with a reservation assignment of type `PIPELINE`. Load jobs are free if you use the shared BigQuery slot pool. However, BigQuery does not make guarantees about the available capacity of the shared pool. For more information, see [Introduction to reservations](https://docs.cloud.google.com/bigquery/docs/reservations-intro).



### Parallelism

  * For `FILE_LOADS` and `STORAGE_WRITE_API` in streaming pipelines, the connector shards the data to a number of files or streams. In general, we recommend calling [`withAutoSharding`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withAutoSharding--) to enable auto-sharding.

  * For `FILE_LOADS` in batch pipelines, the connector writes data to partitioned files, which are then loaded into BigQuery in parallel.

  * For `STORAGE_WRITE_API` in batch pipelines, each worker creates one or more streams to write to BigQuery, determined by the total number of shards.

  * For `STORAGE_API_AT_LEAST_ONCE`, there is a single [default write stream](https://docs.cloud.google.com/bigquery/docs/write-api#default_stream). Multiple workers append to this stream.




### Best practices

  * The Storage Write API (gRPC) has [quota limits](https://docs.cloud.google.com/bigquery/quotas#write-api-limits). The connector handles these limits for most pipelines. However, some scenarios can exhaust the available Storage Write API (gRPC) streams. For example, this issue might happen in a pipeline that uses auto-sharding and autoscaling with a large number of destinations, especially in long-running jobs with highly variable workloads. If this problem occurs, consider using `STORAGE_WRITE_API_AT_LEAST_ONCE`, which avoids the issue.

  * Use [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquerystorage) to monitor your Storage Write API (gRPC) quota usage.

  * When using file loads, Avro typically outperforms JSON. To use Avro, call [`withAvroFormatFunction`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withAvroFormatFunction-org.apache.beam.sdk.transforms.SerializableFunction-).

  * By default, load jobs run in the same project as the Dataflow job. To specify a different project, call [`withLoadJobProjectId`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withLoadJobProjectId-java.lang.String-).

  * When using the Java SDK, consider creating a class that represents the schema of the BigQuery table. Then call [`useBeamSchema`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#useBeamSchema--) in your pipeline to automatically convert between Apache Beam `Row` and BigQuery `TableRow` types. For an example of a schema class, see [`ExampleModel.java`](https://github.com/GoogleCloudPlatform/cloud-code-samples/blob/v1/java/java-dataflow-samples/read-pubsub-write-bigquery/src/main/java/com/cloudcode/dataflow/ExampleModel.java).

  * If you load tables with complex schemas containing thousands of fields, consider calling [`withMaxBytesPerPartition`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withMaxBytesPerPartition-long-) to set a smaller maximum size for each load job.

  * By default, `BigQueryIO` uses Storage Write API (gRPC) settings that are reasonable for most pipelines. However, if you see performance issues, you can set pipeline options to tune these settings. For more information, see [Tune the Storage Write API (gRPC)](https://beam.apache.org/documentation/io/built-in/google-bigquery/#tune-the-storage-write-api) in the Apache Beam documentation.




#### Streaming pipelines

The following recommendations apply to streaming pipelines.

  * For streaming pipelines, we recommend using the Storage Write API (gRPC) (`STORAGE_WRITE_API` or `STORAGE_API_AT_LEAST_ONCE`).

  * A streaming pipeline can use file loads, but this approach has disadvantages:

    * It requires [windowing](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model#advanced_concepts) in order to write the files. You can't use the global window.
    * BigQuery loads files on a best-effort basis when using the [shared slot pool](https://cloud.google.com/bigquery/pricing#free). There can be a significant delay between when a record is written and when it's available in BigQuery.
    * If a load job fails — for example, due to bad data or a schema mismatch — the entire pipeline fails.
  * Consider using `STORAGE_WRITE_API_AT_LEAST_ONCE` when possible. It can result in duplicate records being written to BigQuery, but is less expensive and more scalable than `STORAGE_WRITE_API`.

  * In general, avoid using `STREAMING_INSERTS`. Streaming inserts are more expensive than Storage Write API (gRPC), don't perform as well, and use [best-effort deduplication](https://docs.cloud.google.com/bigquery/docs/write-api-rest#dataconsistency), which can result in some duplicates.

  * Data sharding can improve performance in streaming pipelines. For most pipelines, auto-sharding is a good starting point. However, you can tune sharding as follows:

    * For `STORAGE_WRITE_API`, call [`withNumStorageWriteApiStreams`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withNumStorageWriteApiStreams-int-) to set the number of write streams.
    * For `FILE_LOADS`, call [`withNumFileShards`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withNumFileShards-int-) to set the number of file shards.
  * If you use streaming inserts, we recommend setting [`retryTransientErrors`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/InsertRetryPolicy.html#retryTransientErrors--) as the [retry policy](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withFailedInsertRetryPolicy-org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy-).




#### Batch pipelines

The following recommendations apply to batch pipelines.

  * For most large batch pipelines, we recommend first trying `FILE_LOADS`. A batch pipeline can use `STORAGE_WRITE_API`, but it's likely to exceed quota limits at large scale (1,000+ vCPUs) or if concurrent pipelines are running. Apache Beam doesn't throttle the maximum number of write streams for batch `STORAGE_WRITE_API` jobs, so the job eventually reaches BigQuery Storage API limits.

  * When using `FILE_LOADS`, you might exhaust either the shared BigQuery slot pool or your pool of reserved slots. If you encounter this kind of failure, try the following approaches:

    * Reduce the maximum number of workers or worker size for the job.
    * Purchase more [reserved slots](https://docs.cloud.google.com/bigquery/docs/reservations-get-started).
    * Consider using `STORAGE_WRITE_API`.
  * Small to medium pipelines (<1,000 vCPUs) might benefit from using `STORAGE_WRITE_API`. For these smaller jobs, consider using `STORAGE_WRITE_API` if you want a [dead letter queue](https://beam.apache.org/documentation/patterns/bigqueryio/#bigqueryio-deadletter-pattern) or when the `FILE_LOADS` shared slot pool is not enough.

  * If you can tolerate duplicate data, consider using `STORAGE_WRITE_API_AT_LEAST_ONCE`. This mode can result in duplicate records being written to BigQuery, but might be less expensive than the `STORAGE_WRITE_API` option.

  * Different write modes might perform differently based on the characteristics of your pipeline. Experiment to find the best write mode for your workload.




### Handle row-level errors

This section describes how to handle errors that might happen at the row level, for example because of badly formed input data or schema mismatches.

For Storage Write API (gRPC), any rows that can't be written are placed into a separate `PCollection`. To get this collection, call [`getFailedStorageApiInserts`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/WriteResult.html#getFailedStorageApiInserts--) on the `WriteResult` object. For an example of this approach, see Stream data to BigQuery.

It's a good practice to send the errors to a dead-letter queue or table, for later processing. For more information about this pattern, see [`BigQueryIO` dead letter pattern](https://beam.apache.org/documentation/patterns/bigqueryio/#bigqueryio-deadletter-pattern).

For `FILE_LOADS`, if an error occurs while loading the data, the load job fails and the pipeline throws a runtime exception. You can view the error in the Dataflow logs or look at the BigQuery job history. The I/O connector does not return information about individual failed rows.

For more information about troubleshooting errors, see [BigQuery connector errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#connector_errors).

## Examples

The following examples show how to use Dataflow to write to BigQuery. These examples use the `BigQueryIO` connector.

### Write to an existing table

The following example creates a batch pipeline that writes a `PCollection<MyData>` to BigQuery, where `MyData` is a custom data type.

The [`BigQueryIO.write()`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.html#write--) method returns a [`BigQueryIO.Write<T>`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html) type, which is used to configure the write operation. For more information, see [Writing to a table](https://beam.apache.org/documentation/io/built-in/google-bigquery/#writing-to-a-table) in the Apache Beam documentation. This code example writes to an existing table (`CREATE_NEVER`) and appends the new rows to the table (`WRITE_APPEND`).

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.services.bigquery.model.TableRow;
    import java.util.Arrays;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.DefaultCoder;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    
    public class BigQueryWrite {
      // A custom datatype for the source data.
      @DefaultCoder(AvroCoder.class)
      public static class MyData {
        public String name;
        public Long age;
    
        public MyData() {}
    
        public MyData(String name, Long age) {
          this.name = name;
          this.age = age;
        }
      }
    
      public static void main(String[] args) {
        // Example source data.
        final List<MyData> data = Arrays.asList(
            new MyData("Alice", 40L),
            new MyData("Bob", 30L),
            new MyData("Charlie", 20L)
        );
    
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
            // Create an in-memory PCollection of MyData objects.
            .apply(Create.of(data))
            // Write the data to an exiting BigQuery table.
            .apply(BigQueryIO.<MyData>write()
                .to(String.format("%s:%s.%s",
                    options.getProjectId(),
                    options.getDatasetName(),
                    options.getTableName()))
                .withFormatFunction(
                    (MyData x) -> new TableRow().set("user_name", x.name).set("age", x.age))
                .withCreateDisposition(CreateDisposition.CREATE_NEVER)
                .withWriteDisposition(WriteDisposition.WRITE_APPEND)
                .withMethod(Write.Method.STORAGE_WRITE_API));
        pipeline.run().waitUntilFinish();
      }
    }

### Write to a new or existing table

The following example creates a new table if the destination table does not exist, by setting the [create disposition](https://beam.apache.org/documentation/io/built-in/google-bigquery/#create-disposition) to `CREATE_IF_NEEDED`. When you use this option, you must provide a table schema. The connector uses this schema if it creates a new table.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.services.bigquery.model.TableFieldSchema;
    import com.google.api.services.bigquery.model.TableRow;
    import com.google.api.services.bigquery.model.TableSchema;
    import java.util.Arrays;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.DefaultCoder;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    
    public class BigQueryWriteWithSchema {
      // A custom datatype for the source data.
      @DefaultCoder(AvroCoder.class)
      public static class MyData {
        public String name;
        public Long age;
    
        public MyData() {}
    
        public MyData(String name, Long age) {
          this.name = name;
          this.age = age;
        }
      }
    
      public static void main(String[] args) {
        // Example source data.
        final List<MyData> data = Arrays.asList(
            new MyData("Alice", 40L),
            new MyData("Bob", 30L),
            new MyData("Charlie", 20L)
        );
    
        // Define a table schema. A schema is required for write disposition CREATE_IF_NEEDED.
        TableSchema schema = new TableSchema()
            .setFields(
                Arrays.asList(
                    new TableFieldSchema()
                        .setName("user_name")
                        .setType("STRING")
                        .setMode("REQUIRED"),
                    new TableFieldSchema()
                        .setName("age")
                        .setType("INT64") // Defaults to NULLABLE
                )
            );
    
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
            // Create an in-memory PCollection of MyData objects.
            .apply(Create.of(data))
            // Write the data to a new or existing BigQuery table.
            .apply(BigQueryIO.<MyData>write()
                .to(String.format("%s:%s.%s",
                    options.getProjectId(),
                    options.getDatasetName(),
                    options.getTableName()))
                .withFormatFunction(
                    (MyData x) -> new TableRow().set("user_name", x.name).set("age", x.age))
                .withCreateDisposition(CreateDisposition.CREATE_IF_NEEDED)
                .withSchema(schema)
                .withMethod(Write.Method.STORAGE_WRITE_API)
            );
        pipeline.run().waitUntilFinish();
      }
    }

### Stream data to BigQuery

The following example shows how to stream data using exactly-once semantics, by setting the write mode to `STORAGE_WRITE_API`

Not all streaming pipelines require exactly-once semantics. For example, you might be able to [manually remove duplicates](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery#manually_removing_duplicates) from the destination table. If the possibility of duplicate records is acceptable for your scenario, consider using at-least-once semantics by setting the write method to `STORAGE_API_AT_LEAST_ONCE`. This method is generally more efficient and results in lower latency for most pipelines.

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

  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).
  * Learn about [Pub/Sub to BigQuery best practices](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-best-practices).
  * Understand [performance characteristics of Pub/Sub to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
