---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-quickstart-hbase/
title: Bigtable quickstart (HBase) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:03.150023+00:00
---

# Bigtable quickstart (HBase)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-quickstart-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Bigtable quickstart (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Quickstart for Cloud Bigtable which shows connecting to an instance and reading a row from a table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package com.example.cloud.bigtable.quickstart;
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    
    import java.io.IOException;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Get;
    import org.apache.hadoop.hbase.client.Result;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.util.Bytes;
    
    /**
     * A quickstart application that shows connecting to a Cloud Bigtable instance
     * using the native HBase API to read a row from a table.
     */
    public class Quickstart {
    
      public static void main(String... args) {
    
        String projectId = args[0];  // my-gcp-project-id
        String instanceId = args[1]; // my-bigtable-instance-id
        String tableId = args[2];    // my-bigtable-table-id
    
        // Create a connection to the Cloud Bigtable instance.
        // Use try-with-resources to make sure the connection is closed correctly
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
    
          System.out.println("--- Connection established with Bigtable Instance ---");
          // Create a connection to the table that already exists
          // Use try-with-resources to make sure the connection to the table is closed correctly
          try (Table table = connection.getTable(TableName.valueOf(tableId))) {
    
            // Read a row
            String rowKey = "r1";
            System.out.printf("--- Reading for row-key: %s for provided table: %s ---\n",
                rowKey, tableId);
    
            // Retrieve the result
            Result result = table.get(new Get(Bytes.toBytes(rowKey)));
    
            // Convert row data to string
            String rowValue = Bytes.toString(result.value());
    
            System.out.printf("Scanned value for Row r1: %s \n", rowValue);
    
            System.out.println(" --- Finished reading row --- ");
    
          }  catch (IOException e) {
            // handle exception while connecting to a table
            throw e;
          }
        } catch (IOException e) {
          System.err.println("Exception while running quickstart: " + e.getMessage());
          e.printStackTrace();
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
