---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery/
title: Read from BigQuery to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:41.492544+00:00
---

# Read from BigQuery to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from BigQuery to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Apache Beam connectors let you read BigQuery tables and query results directly into Dataflow pipelines for batch or streaming processing. You can use Managed I/O for standard workloads or `BigQueryIO` for advanced tuning, using the BigQuery Storage Read API to project fields and filter rows.

## Overview

For most use cases, consider using [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-bigquery) to read from BigQuery. Managed I/O provides features such as [automatic upgrades](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#upgrades) and a consistent [configuration API](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#configuration). When reading from BigQuery, Managed I/O performs [direct table reads](https://docs.cloud.google.com/bigquery/docs/reference/storage) which offers the best read performance.

If you need more advanced performance tuning, consider using the `BigQueryIO` connector. The `BigQueryIO` connector supports both direct table reads and reading from BigQuery export jobs. It also offers more fine-grained control over deserializing of table records. For more information, see Use the `BigQueryIO` connector in this document.

## Column projection and filtering

To reduce the volume of data that your pipeline reads from BigQuery, you can use the following techniques:

  * **Column projection** specifies a subset of columns to read from the table. Use column projection when your table has a large number columns and you only need to read a subset of them.
  * **Row filtering** specifies a predicate to apply to the table. The BigQuery read operation only returns rows that match the filter, which can reduce the total amount of data ingested by the pipeline.



The following example reads the `"user_name"` and `"age"` columns from a table and filters out rows that don't match the predicate `"age > 18"`. This example uses Managed I/O.

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

## Read from a query result

The following example uses Managed I/O to read the result of a SQL query. It runs a query against a BigQuery public dataset. You can also use SQL queries to read from a BigQuery view or materialized view.

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

## Use the `BigQueryIO` connector

The [`BigQueryIO`](https://beam.apache.org/documentation/io/built-in/google-bigquery/) connector supports the following serialization methods:

  * Read the data as Avro-formatted records. Using this method, you provide a function that parses the Avro records into a custom data type.
  * Read the data as `TableRow` objects. This method is convenient because it doesn't require a custom data type. However, it generally has lower performance than reading Avro-formatted records.



The connector supports two options for reading data:

  * **Export job**. By default, the `BigQueryIO` connector runs a BigQuery [export job](https://docs.cloud.google.com/bigquery/docs/exporting-data) that writes the table data to Cloud Storage. The connector then reads the data from Cloud Storage.
  * **Direct table reads**. This option is the faster than export jobs, because it uses the [BigQuery Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage) and skips the export step. To use direct table reads, call `withMethod(Method.DIRECT_READ)` when you build the pipeline.



When choosing which option to use, consider the following points:

  * In general, we recommend using direct table reads. The Storage Read API is better suited to data pipelines than export jobs, because it doesn't need the intermediate step of exporting data.

  * If you use direct reads, you are charged for Storage Read API usage. See [Data extraction pricing](https://cloud.google.com/bigquery/pricing#data_extraction_pricing) in the BigQuery pricing page.

  * There is no additional cost for export jobs. However, export jobs have [limits](https://docs.cloud.google.com/bigquery/quotas#export_jobs). For large data movement, where timeliness is a priority and cost is adjustable, direct reads are recommended.

  * The Storage Read API has [quota limits](https://docs.cloud.google.com/bigquery/quotas#storage-limits). Use [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquerystorage) to monitor your quota usage.

  * If you use export jobs, set the `--tempLocation` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#basic_options) to specify a Cloud Storage bucket for the exported files.

  * When using the Storage Read API, you might see lease expiration and session timeout errors in the logs, such as:

    * `DEADLINE_EXCEEDED`
    * `Server Unresponsive`
    * `StatusCode.FAILED_PRECONDITION details = "there was an error operating on 'projects/<projectID>/locations/<location>/sessions/<sessionID>/streams/<streamID>': session``

These errors can occur when an operation takes longer than the timeout, usually in pipelines that run for longer than 6 hours. To mitigate this issue, switch to file exports.

  * The degree of parallelism depends on the read method:

    * Direct reads: The I/O connector produces a dynamic number of streams, based on the size of the export request. It reads these streams directly from BigQuery in parallel.

    * Export jobs: BigQuery determines how many files to write to Cloud Storage. The number of files depends on the query and the volume of data. The I/O connector reads the exported files in parallel.




The following table shows performance metrics for various BigQuery I/O read options. The workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.49.0 for Java. They did not use the Portable Runner.

100 M records | 1 kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Storage Read](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L223) | 120 MBps | 88,000 elements per second  
[Avro Export](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L194) | 105 MBps | 78,000 elements per second  
[Json Export](https://github.com/apache/beam/blob/release-2.50.0/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigquery/BigQueryIOLT.java#L201) | 110 MBps | 81,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

### Examples

The following code examples use the `BigQueryIO` connector with direct table reads. To use an export job instead, omit the call to `withMethod`.

#### Read Avro-formatted records

This example shows how to use the `BigQueryIO` connector to read Avro-formatted records.

To read BigQuery data into Avro-formatted records, use the [`read(SerializableFunction)`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.html#read-org.apache.beam.sdk.transforms.SerializableFunction-) method. This method takes an application-defined function that parses [`SchemaAndRecord`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/SchemaAndRecord.html) objects and returns a custom data type. The output from the connector is a `PCollection` of your custom data type.

The following code reads a `PCollection<MyData>` from a BigQuery table, where `MyData` is an application-defined class.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import org.apache.avro.generic.GenericRecord;
    import org.apache.avro.util.Utf8;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.DefaultCoder;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.TypedRead;
    import org.apache.beam.sdk.io.gcp.bigquery.SchemaAndRecord;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.SerializableFunction;
    import org.apache.beam.sdk.values.TypeDescriptor;
    
    public class BigQueryReadAvro {
    
      // A custom datatype to hold a record from the source table.
      @DefaultCoder(AvroCoder.class)
      public static class MyData {
        public String name;
        public Long age;
    
        // Function to convert Avro records to MyData instances.
        public static class FromSchemaAndRecord
                implements SerializableFunction<SchemaAndRecord, MyData> {
          @Override public MyData apply(SchemaAndRecord elem) {
            MyData data = new MyData();
            GenericRecord record = elem.getRecord();
            data.name = ((Utf8) record.get("user_name")).toString();
            data.age = (Long) record.get("age");
            return data;
          }
        }
      }
    
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
            // Read table data into Avro records, using an application-defined parsing function.
            .apply(BigQueryIO.read(new MyData.FromSchemaAndRecord())
                .from(String.format("%s:%s.%s",
                    options.getProjectId(),
                    options.getDatasetName(),
                    options.getTableName()))
                .withMethod(TypedRead.Method.DIRECT_READ))
            // The output from the previous step is a PCollection<MyData>.
            .apply(MapElements
                .into(TypeDescriptor.of(MyData.class))
                .via((MyData x) -> {
                  System.out.printf("Name: %s, Age: %d%n", x.name, x.age);
                  return x;
                }));
        pipeline.run().waitUntilFinish();
      }
    }

The `read` method takes a `SerializableFunction<SchemaAndRecord, T>` interface, which defines a function to convert from Avro records to a custom data class. In the previous code example, the `MyData.apply` method implements this conversion function. The example function parses the `name` and `age` fields from the Avro record and returns a `MyData` instance.

**Note:** This code fails if the parsing function doesn't match the actual schema of the BigQuery table. Specifically, the named columns must exist, and the data types must be compatible. Also, if any columns in the table are nullable, your code must handle null values.

To specify which BigQuery table to read, call the `from` method, as shown in the previous example. For more information, see [Table names](https://beam.apache.org/documentation/io/built-in/google-bigquery/#table-names) in the BigQuery I/O connector documentation.

#### Read `TableRow` objects

This example shows how to use the `BigQueryIO` connector to read `TableRow` objects.

The [`readTableRows`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.html#readTableRows--) method reads BigQuery data into a `PCollection` of [`TableRow`](https://developers.google.com/resources/api-libraries/documentation/bigquery/v2/java/latest/com/google/api/services/bigquery/model/TableRow.html) objects. Each `TableRow` is a map of key-value pairs that holds a single row of table data. Specify the BigQuery table to read by calling the `from` method.

The following code reads a `PCollection<TableRows>` from a BigQuery table.

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

This example also shows how to access the values from the `TableRow` dictionary. Integer values are encoded as strings to match BigQuery's exported JSON format.

**Note:** This code fails if the parsing function doesn't match the actual schema of the BigQuery table. Specifically, the named columns must exist, and the data types must be compatible. Also, if any columns in the table are nullable, your code must handle null values.

## What's next

  * [Managed I/O for BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-bigquery)
  * [Write to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
