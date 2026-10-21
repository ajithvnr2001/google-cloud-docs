---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-apache-iceberg-dynamic-destinations/
title: Write to Iceberg using dynamic destinations \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:14.590685+00:00
---

# Write to Iceberg using dynamic destinations  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-apache-iceberg-dynamic-destinations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Write to Iceberg using dynamic destinations Stay organized with collections  Save and categorize content based on your preferences. 

Write from Dataflow to Apache Iceberg, using the dynamic destinations feature to route incoming records to different Iceberg tables. (Note, currently this feature is only supported for Java)

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

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
