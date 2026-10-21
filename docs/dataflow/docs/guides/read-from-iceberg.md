---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-iceberg/
title: Read from Apache Iceberg to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:40.072478+00:00
---

# Read from Apache Iceberg to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-iceberg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from Apache Iceberg to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

To read from Apache Iceberg to Dataflow, use the [managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-iceberg).

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
    

## Example

The following example reads from an Apache Iceberg table and writes the data to text files.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.PCollectionRowTuple;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class ApacheIcebergRead {
    
      static final String CATALOG_TYPE = "hadoop";
    
      public interface Options extends PipelineOptions {
        @Description("The URI of the Apache Iceberg warehouse location")
        String getWarehouseLocation();
    
        void setWarehouseLocation(String value);
    
        @Description("Path to write the output file")
        String getOutputPath();
    
        void setOutputPath(String value);
    
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
        //   --tableName= $TABLE_NAME --outputPath=$OUTPUT_FILE
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
        pipeline.apply(Managed.read(Managed.ICEBERG).withConfig(config))
            .getSinglePCollection()
            // Format each record as a string with the format 'id:name'.
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via((row -> {
                  return String.format("%d:%s",
                      row.getInt64("id"),
                      row.getString("name"));
                })))
            // Write to a text file.
            .apply(
                TextIO.write()
                    .to(options.getOutputPath())
                    .withNumShards(1)
                    .withSuffix(".txt"));
    
        pipeline.run().waitUntilFinish();
      }
    }

## What's next

  * [Write to Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg).
  * [Streaming Write to Apache Iceberg with Lakehouse REST Catalog](https://docs.cloud.google.com/dataflow/docs/guides/streaming-write-to-iceberg-biglake).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
