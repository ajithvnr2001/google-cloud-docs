---
url: https://docs.cloud.google.com/dataflow/docs/guides/streaming-write-to-iceberg-biglake/
title: Streaming Write to Apache Iceberg with Lakehouse REST Catalog \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:10.921405+00:00
---

# Streaming Write to Apache Iceberg with Lakehouse REST Catalog  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/streaming-write-to-iceberg-biglake/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Streaming Write to Apache Iceberg with Lakehouse REST Catalog Stay organized with collections  Save and categorize content based on your preferences. 

The Dataflow [managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-iceberg) lets you ingest real-time data into Apache Iceberg tables through a REST catalog. This approach provides low-latency streaming writes and dynamic destination routing while maintaining open table format interoperability across your lakehouse analytics stack.

Managed I/O supports multiple catalog backends, including Hadoop, Hive, and BigQuery metastore, but this document focuses on streaming pipelines that target a Lakehouse REST catalog. If you write to [BigQuery tables for Apache Iceberg](https://docs.cloud.google.com/bigquery/docs/iceberg-tables), use the [`BigQueryIO` connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/) with the BigQuery Storage API instead, as target tables must exist before ingestion.

## Prerequisites

**Set up Lakehouse.** Configure your Google Cloud project with the required permissions by following [Use the Lakehouse runtime catalog with the Iceberg REST catalog](https://docs.cloud.google.com/bigquery/docs/blms-rest-catalog). Make sure that you understand the limitations of Lakehouse Iceberg REST Catalog described on that page.

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
    
    <dependency>
      <groupId>org.apache.iceberg</groupId>
      <artifactId>iceberg-gcp</artifactId>
      <version>${iceberg.version}</version>
    </dependency>
    

## Example

The following example demonstrates a streaming pipeline that writes data to an Apache Iceberg table using the REST catalog, backed by the Lakehouse runtime catalog.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.common.collect.ImmutableMap;
    import java.io.IOException;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.RowCoder;
    import org.apache.beam.sdk.extensions.gcp.options.GcpOptions;
    import org.apache.beam.sdk.io.GenerateSequence;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.schemas.Schema;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.Row;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.Duration;
    
    /**
     * A streaming pipeline that writes data to an Iceberg table using the REST catalog.
     *
     * <p>This example demonstrates writing to an Iceberg table backed by the BigLake Metastore. For
     * more information on BigLake, see the documentation at
     * https://cloud.google.com/bigquery/docs/blms-rest-catalog.
     */
    public class ApacheIcebergRestCatalogStreamingWrite {
    
      // The schema for the generated records.
      public static final Schema SCHEMA =
          Schema.builder().addStringField("user_id").addInt64Field("click_count").build();
    
      /** Pipeline options for this example. */
      public interface Options extends GcpOptions, StreamingOptions {
        @Description(
            "Warehouse location where the table's data will be written to. "
                + "BigLake only supports Single Region buckets")
        @Validation.Required
        String getWarehouse();
    
        void setWarehouse(String warehouse);
    
        @Description("The URI for the REST catalog")
        @Validation.Required
        @Default.String("https://biglake.googleapis.com/iceberg/v1beta/restcatalog")
        String getCatalogUri();
    
        void setCatalogUri(String value);
    
        @Description("The name of the table to write to")
        @Validation.Required
        String getIcebergTable();
    
        void setIcebergTable(String value);
    
        @Description("The name of the Apache Iceberg catalog")
        @Validation.Required
        String getCatalogName();
    
        void setCatalogName(String catalogName);
      }
    
      /**
       * The main entry point for the pipeline.
       *
       * @param args Command-line arguments
       * @throws IOException If there is an issue with Google Credentials
       */
      public static void main(String[] args) throws IOException {
        Options options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        options.setStreaming(true);
    
        // Note: The token expires in 1 hour. Users may need to re-run the pipeline.
        // Future updates to Iceberg and the BigLake Metastore will support token refreshing.
        Map<String, String> catalogProps =
            ImmutableMap.<String, String>builder()
                .put("type", "rest")
                .put("uri", options.getCatalogUri())
                .put("warehouse", options.getWarehouse())
                .put("header.x-goog-user-project", options.getProject())
                .put(
                    "header.Authorization",
                    "Bearer "
                        + [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)()
                            .createScoped("https://www.googleapis.com/auth/cloud-platform")
                            .refreshAccessToken()
                            .getTokenValue())
                .put("rest-metrics-reporting-enabled", "false")
                .build();
    
        Map<String, Object> icebergWriteConfig =
            ImmutableMap.<String, Object>builder()
                .put("table", options.getIcebergTable())
                .put("catalog_properties", catalogProps)
                .put("catalog_name", options.getCatalogName())
                .put("triggering_frequency_seconds", 20)
                .build();
    
        Pipeline p = Pipeline.create(options);
    
        p.apply(
                "GenerateSequence",
                GenerateSequence.from(0).withRate(1, Duration.standardSeconds(5)))
            .apply(
                "ConvertToRows",
                MapElements.into(TypeDescriptors.rows())
                    .via(
                        i ->
                            Row.withSchema(SCHEMA)
                                .withFieldValue("user_id", "user-" + (i % 10))
                                .withFieldValue("click_count", i % 100)
                                .build()))
            .setCoder(RowCoder.[of](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ClientId.html#com_google_auth_oauth2_ClientId_of_java_lang_String_java_lang_String_)(SCHEMA))
            .apply("WriteToIceberg", Managed.write(Managed.ICEBERG).withConfig(icebergWriteConfig));
    
        p.run();
      }
    }

## What's next

  * [CDC Read from Apache Iceberg with Lakehouse REST Catalog](https://docs.cloud.google.com/dataflow/docs/guides/cdc-read-from-iceberg-biglake).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).
  * Learn more about [Lakehouse REST Catalog](https://docs.cloud.google.com/bigquery/docs/blms-rest-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
