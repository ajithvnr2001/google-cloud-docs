---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-beam-helloworld-read/
title: Read data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:59.969068+00:00
---

# Read data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-beam-helloworld-read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read data Stay organized with collections  Save and categorize content based on your preferences. 

Read data from Cloud Bigtable with Apache Beam.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Bigtable HBase Beam connector](https://docs.cloud.google.com/bigtable/docs/hbase-dataflow-java)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigtable.beam.CloudBigtableIO;
    import com.google.cloud.bigtable.beam.CloudBigtableScanConfiguration;
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.Read;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.hadoop.hbase.client.Result;
    import org.apache.hadoop.hbase.client.Scan;
    import org.apache.hadoop.hbase.filter.FirstKeyOnlyFilter;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class HelloWorldRead {
      public static void main(String[] args) {
        BigtableOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(BigtableOptions.class);
        Pipeline p = Pipeline.create(options);
    
        Scan scan = new Scan();
        scan.setCacheBlocks(false);
        scan.setFilter(new FirstKeyOnlyFilter());
    
        CloudBigtableScanConfiguration config =
            new CloudBigtableScanConfiguration.Builder()
                .withProjectId(options.getBigtableProjectId())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId())
                .withScan(scan)
                .build();
    
        p.apply(Read.from(CloudBigtableIO.read(config)))
            .apply(
                ParDo.of(
                    new DoFn<Result, Void>() {
                      @ProcessElement
                      public void processElement(@Element Result row, OutputReceiver<Void> out) {
                        System.out.println(Bytes.toString(row.getRow()));
                      }
                    }));
    
        p.run().waitUntilFinish();
      }
    
      public interface BigtableOptions extends DataflowPipelineOptions {
        @Description("The Bigtable project ID, this can be different than your Dataflow project")
        @Default.String("bigtable-project")
        String getBigtableProjectId();
    
        void setBigtableProjectId(String bigtableProjectId);
    
        @Description("The Bigtable instance ID")
        @Default.String("bigtable-instance")
        String getBigtableInstanceId();
    
        void setBigtableInstanceId(String bigtableInstanceId);
    
        @Description("The Bigtable table ID in the instance.")
        @Default.String("mobile-time-series")
        String getBigtableTableId();
    
        void setBigtableTableId(String bigtableTableId);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
