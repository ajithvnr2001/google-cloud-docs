---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-app-engine-standard-hw/
title: App Engine \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:11.146565+00:00
---

# App Engine  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-app-engine-standard-hw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  App Engine Stay organized with collections  Save and categorize content based on your preferences. 

Samples related to using Cloud Bigtable with App Engine.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Example: Java App Engine standard environment](https://docs.cloud.google.com/bigtable/docs/samples-java-appengine-standard)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * A minimal application that connects to Cloud Bigtable using the native HBase API and performs
     * some basic operations.
     */
    public class BigtableHelloWorld {
    
      // Refer to table metadata names by byte array in the HBase API
      private static final byte[] TABLE_NAME = Bytes.toBytes("Hello-Bigtable");
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("cf1");
      private static final byte[] COLUMN_NAME = Bytes.toBytes("greeting");
    
      // Write some friendly greetings to Cloud Bigtable
      private static final String[] GREETINGS = {
        "Hello World!", "Hello Cloud Bigtable!", "Hello HBase!"
      };
    
      /**
       * Create a table -- first time only.
       *
       * @param connection to Bigtable
       * @return the status
       */
      public static String create(Connection connection) {
        try {
          // The admin API lets us create, manage and delete tables
          Admin admin = connection.getAdmin();
    
          // Create a table with a single column family
          HTableDescriptor descriptor = new HTableDescriptor(TableName.valueOf(TABLE_NAME));
          descriptor.addFamily(new HColumnDescriptor(COLUMN_FAMILY_NAME));
    
          admin.createTable(descriptor);
        } catch (IOException e) {
          return "Table exists.";
        }
        return "Create table " + Bytes.toString(TABLE_NAME);
      }
    
      /** Connects to Cloud Bigtable, runs some basic operations and prints the results. */
      public static String doHelloWorld() {
    
        StringBuilder result = new StringBuilder();
    
        // Create the Bigtable connection, use try-with-resources to make sure it gets closed
        Connection connection = BigtableHelper.getConnection();
        result.append(create(connection));
        result.append("<br><br>");
        try (Table table = connection.getTable(TableName.valueOf(TABLE_NAME))) {
    
          // Retrieve the table we just created so we can do some reads and writes
    
          // Write some rows to the table
          result.append("Write some greetings to the table<br>");
          for (int i = 0; i < GREETINGS.length; i++) {
            // Each row has a unique row key.
            //
            // Note: This example uses sequential numeric IDs for simplicity, but
            // this can result in poor performance in a production application.
            // Since rows are stored in sorted order by key, sequential keys can
            // result in poor distribution of operations across nodes.
            //
            // For more information about how to design a Bigtable schema for the
            // best performance, see the documentation:
            //
            //     https://cloud.google.com/bigtable/docs/schema-design
            String rowKey = "greeting" + i;
    
            // Put a single row into the table. We could also pass a list of Puts to write a batch.
            Put put = new Put(Bytes.toBytes(rowKey));
            put.addColumn(COLUMN_FAMILY_NAME, COLUMN_NAME, Bytes.toBytes(GREETINGS[i]));
            table.put(put);
          }
    
          // Get the first greeting by row key
          String rowKey = "greeting0";
          Result getResult = table.get(new Get(Bytes.toBytes(rowKey)));
          String greeting = Bytes.toString(getResult.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME));
          result.append("Get a single greeting by row key<br>");
    
          result.append("     ");
          result.append(rowKey);
          result.append("= ");
          result.append(greeting);
          result.append("<br>");
    
          // Now scan across all rows.
          Scan scan = new Scan();
    
          result.append("Scan for all greetings:");
          ResultScanner scanner = table.getScanner(scan);
          for (Result row : scanner) {
            byte[] valueBytes = row.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME);
            result.append("    ");
            result.append(Bytes.toString(valueBytes));
            result.append("<br>");
          }
    
        } catch (IOException e) {
          result.append("Exception while running HelloWorld: " + e.getMessage() + "<br>");
          result.append(e.toString());
          return result.toString();
        }
    
        return result.toString();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
