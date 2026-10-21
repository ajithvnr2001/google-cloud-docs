---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-databases/
title: Read from databases to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:43.140430+00:00
---

# Read from databases to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from databases to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

You can read data from a relational database into Dataflow using the [managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-databases) to perform scalable data transformations and analytics.

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
      <artifactId>beam-sdks-java-io-jdbc</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

## Example

The following example reads from a PostgreSQL database and writes the data to text files. While this example uses PostgreSQL, configuring other supported databases is similar.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class PostgresRead {
    
      public interface Options extends PipelineOptions {
        @Description("The JDBC URL of the PostgreSQL database to read from.")
        String getJdbcUrl();
    
        void setJdbcUrl(String value);
    
        @Description("The PostgresSQL table to read from.")
        String getTable();
    
        void setTable(String value);
    
        @Description("The username for the PostgreSQL database.")
        String getUsername();
    
        void setUsername(String value);
    
        @Description("The password for the PostgreSQL database.")
        String getPassword();
    
        void setPassword(String value);
    
        @Description(
            "The path to write the output file. Can be a local file path, "
                + "a GCS path, or a path to any other supported file systems.")
        String getOutputPath();
    
        void setOutputPath(String value);
      }
    
      public static PipelineResult.State main(String[] args) {
        // Parse the pipeline options passed into the application. Example:
        //   --runner=DirectRunner --jdbcUrl=$JDBC_URL --table=$TABLE
        //   --username=$USERNAME --password=$PASSWORD --outputPath=$OUTPUT_FILE
        // For more information, see
        // https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        var options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        Pipeline pipeline = createPipeline(options);
        return pipeline.run().waitUntilFinish();
      }
    
      public static Pipeline createPipeline(Options options) {
    
        // Create configuration parameters for the Managed I/O transform.
        ImmutableMap<String, Object> config =
            ImmutableMap.<String, Object>builder()
                .put("jdbc_url", options.getJdbcUrl())
                .put("location", options.getTable())
                .put("username", options.getUsername())
                .put("password", options.getPassword())
                .build();
    
        // Build the pipeline.
        var pipeline = Pipeline.create(options);
        pipeline
            // Read data from a Postgres database using Managed I/O.
            .apply(Managed.read(Managed.POSTGRES).withConfig(config))
            .getSinglePCollection()
            // Convert each row to a string.
            .apply(
                MapElements.into(TypeDescriptors.strings())
                    .via((row -> String.format("%d,%s", row.getInt32("id"), row.getString("name")))))
            // Write strings to a text file.
            .apply(TextIO.write().to(options.getOutputPath()).withSuffix(".txt").withNumShards(1));
        return pipeline;
      }
    }

## What's next

  * [Write to Databases](https://docs.cloud.google.com/dataflow/docs/guides/write-to-databases).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
