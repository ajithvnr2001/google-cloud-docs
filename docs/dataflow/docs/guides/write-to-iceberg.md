---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg/
title: Write from Dataflow to Apache Iceberg \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:12.215268+00:00
---

# Write from Dataflow to Apache Iceberg  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to Apache Iceberg Stay organized with collections  Save and categorize content based on your preferences. 

To write from Dataflow to Apache Iceberg, use the [managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-iceberg).

Managed I/O supports the following capabilities for Apache Iceberg:

Catalogs | 

  * Hadoop
  * Hive
  * REST-based catalogs
  * [BigQuery metastore](https://docs.cloud.google.com/bigquery/docs/about-bqms) (requires Apache Beam SDK 2.62.0 or later if not using the Portable Runner) 

  
---|---  
Read capabilities | Batch read  
Write capabilities | 

  * Batch write
  * Streaming write
  * [ Dynamic destinations](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg#dynamic-destinations)
  * Dynamic table creation

  
  
For [BigQuery tables for Apache Iceberg](https://docs.cloud.google.com/bigquery/docs/iceberg-tables), use the [`BigQueryIO` connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/) with BigQuery Storage API. The table must already exist; dynamic table creation is not supported.

## Dependencies

Add the following dependencies to your project:

###  Java 
    
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-managed</artifactId>
      <version>${beam.version}</version>
    </dependency>
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-io-iceberg</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

## Dynamic destinations

Managed I/O for Apache Iceberg supports dynamic destinations. Instead of writing to a single fixed table, the connector can dynamically select a destination table based on field values within the incoming records.

To use dynamic destinations, provide a template for the `table` configuration parameter. For more information, see [Dynamic destinations](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#dynamic-destinations).

## Examples

The following examples show how to use Managed I/O to write to Apache Iceberg.

### Write to an Apache Iceberg table

The following example writes in-memory JSON data to an Apache Iceberg table.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.util.Arrays;
    import java.util.List;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.schemas.Schema;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.JsonToRow;
    import org.apache.beam.sdk.values.PCollectionRowTuple;
    
    public class ApacheIcebergWrite {
      static final List<String> TABLE_ROWS = Arrays.asList(
          "{\"id\":0, \"name\":\"Alice\"}",
          "{\"id\":1, \"name\":\"Bob\"}",
          "{\"id\":2, \"name\":\"Charles\"}"
      );
    
      static final String CATALOG_TYPE = "hadoop";
    
      // The schema for the table rows.
      public static final Schema SCHEMA = new Schema.Builder()
          .addStringField("name")
          .addInt64Field("id")
          .build();
    
      public interface Options extends PipelineOptions {
        @Description("The URI of the Apache Iceberg warehouse location")
        String getWarehouseLocation();
    
        void setWarehouseLocation(String value);
    
        @Description("The name of the Apache Iceberg catalog")
        String getCatalogName();
    
        void setCatalogName(String value);
    
        @Description("The name of the table to write to")
        String getTableName();
    
        void setTableName(String value);
      }
    
      public static void main(String[] args) {
    
        // Parse the pipeline options passed into the application. Example:
        //   --runner=DirectRunner --warehouseLocation=$LOCATION --catalogName=$CATALOG \
        //   --tableName= $TABLE_NAME
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        Pipeline pipeline = Pipeline.create(options);
    
        // Configure the Iceberg source I/O
        Map catalogConfig = ImmutableMap.<String, Object>builder()
            .put("warehouse", options.getWarehouseLocation())
            .put("type", CATALOG_TYPE)
            .build();
    
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("table", options.getTableName())
            .put("catalog_name", options.getCatalogName())
            .put("catalog_properties", catalogConfig)
            .build();
    
        // Build the pipeline.
        pipeline.apply(Create.of(TABLE_ROWS))
            .apply(JsonToRow.withSchema(SCHEMA))
            .apply(Managed.write(Managed.ICEBERG).withConfig(config));
    
        pipeline.run().waitUntilFinish();
      }
    }

### Write with dynamic destinations

The following example writes to different Apache Iceberg tables based on a field in the input data.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.util.Arrays;
    import java.util.List;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.schemas.Schema;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.JsonToRow;
    
    public class ApacheIcebergDynamicDestinations {
    
      // The schema for the table rows.
      public static final Schema SCHEMA = new Schema.Builder()
          .addInt64Field("id")
          .addStringField("name")
          .addStringField("airport")
          .build();
    
      // The data to write to table, formatted as JSON strings.
      static final List<String> TABLE_ROWS = List.of(
          "{\"id\":0, \"name\":\"Alice\", \"airport\": \"ORD\" }",
          "{\"id\":1, \"name\":\"Bob\", \"airport\": \"SYD\" }",
          "{\"id\":2, \"name\":\"Charles\", \"airport\": \"ORD\" }"
      );
    
      public interface Options extends PipelineOptions {
        @Description("The URI of the Apache Iceberg warehouse location")
        String getWarehouseLocation();
    
        void setWarehouseLocation(String value);
    
        @Description("The name of the Apache Iceberg catalog")
        String getCatalogName();
    
        void setCatalogName(String value);
      }
    
      // Write JSON data to Apache Iceberg, using dynamic destinations to determine the Iceberg table
      // where Dataflow writes each record. The JSON data contains a field named "airport". The
      // Dataflow pipeline writes to Iceberg tables with the naming pattern "flights-{airport}".
      public static void main(String[] args) {
        // Parse the pipeline options passed into the application. Example:
        //   --runner=DirectRunner --warehouseLocation=$LOCATION --catalogName=$CATALOG \
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        Pipeline pipeline = Pipeline.create(options);
    
        // Configure the Iceberg source I/O
        Map catalogConfig = ImmutableMap.<String, Object>builder()
            .put("warehouse", options.getWarehouseLocation())
            .put("type", "hadoop")
            .build();
    
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("catalog_name", options.getCatalogName())
            .put("catalog_properties", catalogConfig)
            // Route the incoming records based on the value of the "airport" field.
            .put("table", "flights-{airport}")
            // Specify which fields to keep from the input data.
            .put("keep", Arrays.asList("name", "id"))
            .build();
    
        // Build the pipeline.
        pipeline
            // Read in-memory JSON data.
            .apply(Create.of(TABLE_ROWS))
            // Convert the JSON records to Row objects.
            .apply(JsonToRow.withSchema(SCHEMA))
            // Write each Row to Apache Iceberg.
            .apply(Managed.write(Managed.ICEBERG).withConfig(config));
    
        // Run the pipeline.
        pipeline.run().waitUntilFinish();
      }
    }

## What's next

  * [Read from Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/read-from-iceberg).
  * [Streaming Write to Apache Iceberg with Lakehouse REST Catalog](https://docs.cloud.google.com/dataflow/docs/guides/streaming-write-to-iceberg-biglake).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
