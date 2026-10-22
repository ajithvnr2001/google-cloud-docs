---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-apache-iceberg-write/
title: Write to Apache Iceberg \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:45.141810+00:00
---

# Write to Apache Iceberg  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-apache-iceberg-write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Write to Apache Iceberg Stay organized with collections  Save and categorize content based on your preferences. 

Use the Dataflow managed I/O transform to write to Apache Iceberg

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write from Dataflow to Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
