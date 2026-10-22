---
url: https://docs.cloud.google.com/bigtable/docs/samples-java-appengine-standard/
title: Example: Java App Engine standard environment \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:02.985608+00:00
---

# Example: Java App Engine standard environment  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-java-appengine-standard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Example: Java App Engine standard environment

This example is an [App Engine](https://docs.cloud.google.com/appengine) application, written in Java, that writes some "hello world" greetings to a Bigtable table and reads them back. The application runs on Google Cloud in the App Engine [standard environment](https://docs.cloud.google.com/appengine/docs/standard). The application uses the [Java 8 runtime](https://docs.cloud.google.com/appengine/docs/standard/java/runtime-java8). The code for this application is in the GitHub repository [GoogleCloudPlatform/java-docs-samples](https://github.com/GoogleCloudPlatform/java-docs-samples), in the directory `appengine-java8/bigtable`.

## Overview of the code sample

The code sample includes the following classes:

  * [`BigtableHelper`](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/appengine-java8/bigtable/src/main/java/com/example/bigtable/BigtableHelper.java), which provides a connection to Bigtable.
  * [`BigtableHelloWorld`](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/appengine-java8/bigtable/src/main/java/com/example/bigtable/BigtableHelloWorld.java), which writes to and reads from Bigtable.



### BigtableHelper

`BigtableHelper` provides a method to create a connection to Bigtable. It also caches the connection and provides a method that will retrieve the cached connection if it exists. Creating a connection is a relatively expensive operation, so as a best practice you should always create a single connection and reuse it.
    
    
    public static void connect() throws IOException {
    
      if (PROJECT_ID == null || INSTANCE_ID == null) {
        if (sc != null) {
          sc.log("environment variables BIGTABLE_PROJECT, and BIGTABLE_INSTANCE need to be defined.");
        }
        return;
      }
    
      connection = BigtableConfiguration.connect(PROJECT_ID, INSTANCE_ID);
    }
    
    /**
     * Get the shared connection to Cloud Bigtable.
     *
     * @return the connection
     */
    public static Connection getConnection() {
      if (connection == null) {
        try {
          connect();
        } catch (IOException e) {
          if (sc != null) {
            sc.log("connect ", e);
          }
        }
      }
      if (connection == null) {
        if (sc != null) {
          sc.log("BigtableHelper-No Connection");
        }
      }
      return connection;
    }
    

### BigtableHelloWorld

`BigtableHelloWorld` is used to write a series of greetings to Bigtable, read the greetings, and then display them. The class gets a Bigtable connection from `BigtableHelper`, uses the connection to get a `Table` object, which lets you to read and write values, then uses the `Table` object to write to and read from the table.
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
