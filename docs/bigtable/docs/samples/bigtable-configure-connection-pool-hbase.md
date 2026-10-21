---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-configure-connection-pool-hbase/
title: Configure a connection pool (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:49.965322+00:00
---

# Configure a connection pool (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-configure-connection-pool-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Configure a connection pool (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Configures a connection pool.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure connection pools](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    import static com.google.cloud.bigtable.hbase.BigtableOptionsFactory.BIGTABLE_DATA_CHANNEL_COUNT_KEY;
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.hbase.client.Connection;
    
    public class ConfigureConnectionPool {
    
      public static void configureConnectionPool(String projectId, String instanceId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        Configuration config = BigtableConfiguration.configure(projectId, instanceId);
        config.setInt(BIGTABLE_DATA_CHANNEL_COUNT_KEY, 10);
        try (Connection connection = BigtableConfiguration.connect(config)) {
          int poolSize = connection.getConfiguration().getInt(BIGTABLE_DATA_CHANNEL_COUNT_KEY, 0);
    
          System.out.println(String.format("Connected with pool size of %d", poolSize));
        } catch (Exception e) {
          System.out.println("Error during ConfigureConnectionPool: \n" + e.toString());
        }
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
