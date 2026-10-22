---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-simple-hbase/
title: Perform a simple write (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:10.096758+00:00
---

# Perform a simple write (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-simple-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Perform a simple write (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Performing a simple write API call: MutateRow. Make sure samples use multiple SetCells (mutations).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write examples](https://docs.cloud.google.com/bigtable/docs/writing-data)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class WriteSimple {
    
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("stats_summary");
    
      public static void writeSimple(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
          final Table table = connection.getTable(TableName.valueOf(Bytes.toBytes(tableId)));
          long timestamp = System.currentTimeMillis();
          byte[] one = new byte[]{0, 0, 0, 0, 0, 0, 0, 1};
    
          String rowKey = "phone#4c410523#20190501";
          Put put = new Put(Bytes.toBytes(rowKey));
    
          put.addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_cell"), timestamp, one);
          put.addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_wifi"), timestamp, one);
          put.addColumn(
              COLUMN_FAMILY_NAME,
              Bytes.toBytes("os_build"),
              timestamp,
              Bytes.toBytes("PQ2A.190405.003"));
          table.put(put);
    
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during WriteSimple: \n" + e.toString());
        }
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
