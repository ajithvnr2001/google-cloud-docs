---
url: https://docs.cloud.google.com/bigtable/docs/samples-hbase-java-hello/
title: HBase APIs for Java hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:30.605450+00:00
---

# HBase APIs for Java hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-hbase-java-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HBase APIs for Java hello world

This example is a "hello world" application, using the Bigtable HBase client library for Java, that illustrates how to:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.

**Note:** The Cloud Bigtable HBase client for Java is for customers who are migrating to Bigtable from HBase and want to continue using the HBase API. In all other cases, Java developers should instead use the [Cloud Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), which calls the Bigtable APIs. 

## Set up authentication

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

The sample uses the [HBase](https://hbase.apache.org/) APIs to communicate with Bigtable. The code for this sample is in the GitHub repository [GoogleCloudPlatform/cloud-bigtable-examples](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/), in the directory [`java/hello-world`](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/master/java/hello-world).

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/master/java/hello-world).

## Using the HBase APIs

The sample application connects to Bigtable and demonstrates some simple operations.

### Installing and importing the client library

This sample uses the [Bigtable HBase client for Java](https://docs.cloud.google.com/bigtable/docs/hbase-bigtable), as well as Maven. See the [instructions for using the client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

The sample uses the following imports:
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import java.io.IOException;

### Connecting to Bigtable

Connect to Bigtable using the `BigtableConfiguration` class.
    
    
    // Create the Bigtable connection, use try-with-resources to make sure it gets closed
    try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
    
      // The admin API lets us create, manage and delete tables
      Admin admin = connection.getAdmin();

### Creating a table

Use the Admin API to create a table.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    // Create a table with a single column family
    HTableDescriptor descriptor = new HTableDescriptor(TableName.valueOf(TABLE_NAME));
    descriptor.addFamily(new HColumnDescriptor(COLUMN_FAMILY_NAME));
    
    System.out.println("HelloWorld: Create table " + descriptor.getNameAsString());
    admin.createTable(descriptor);

### Writing rows to a table

Use the `Table` class to put rows to the table. For better throughput, consider using the `BigtableBufferedMutator` class.
    
    
    // Retrieve the table we just created so we can do some reads and writes
    Table table = connection.getTable(TableName.valueOf(TABLE_NAME));
    
    // Write some rows to the table
    System.out.println("HelloWorld: Write some greetings to the table");
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

### Reading a row by its key

Get a row directly using its key.
    
    
    // Get the first greeting by row key
    String rowKey = "greeting0";
    Result getResult = table.get(new Get(Bytes.toBytes(rowKey)));
    String greeting = Bytes.toString(getResult.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME));
    System.out.println("Get a single greeting by row key");
    System.out.printf("\t%s = %s\n", rowKey, greeting);

### Scanning all table rows

Use the `Scan` class to get a range of rows.
    
    
    // Now scan across all rows.
    Scan scan = new Scan();
    
    System.out.println("HelloWorld: Scan for all greetings:");
    ResultScanner scanner = table.getScanner(scan);
    for (Result row : scanner) {
      byte[] valueBytes = row.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME);
      System.out.println('\t' + Bytes.toString(valueBytes));
    }

### Deleting a table

Delete a table using the Admin API.
    
    
    // Clean up by disabling and then deleting the table
    System.out.println("HelloWorld: Delete the table");
    admin.disableTable(table.getName());
    admin.deleteTable(table.getName());

## Putting it all together

Here is the full example without comments.
    
    
    package com.example.bigtable;
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import java.io.IOException;
    import java.util.UUID;
    import org.apache.hadoop.hbase.HColumnDescriptor;
    import org.apache.hadoop.hbase.HTableDescriptor;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Admin;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Get;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.client.Result;
    import org.apache.hadoop.hbase.client.ResultScanner;
    import org.apache.hadoop.hbase.client.Scan;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class HelloWorld {
    
      private static final byte[] TABLE_NAME =
          Bytes.toBytes("Hello-Bigtable-" + UUID.randomUUID().toString().substring(0, 19));
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("cf1");
      private static final byte[] COLUMN_NAME = Bytes.toBytes("greeting");
    
      private static final String[] GREETINGS = {
        "Hello World!", "Hello Cloud Bigtable!", "Hello HBase!"
      };
    
      protected static void doHelloWorld(String projectId, String instanceId) {
    
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
    
          Admin admin = connection.getAdmin();
    
          try {
            HTableDescriptor descriptor = new HTableDescriptor(TableName.valueOf(TABLE_NAME));
            descriptor.addFamily(new HColumnDescriptor(COLUMN_FAMILY_NAME));
    
            System.out.println("HelloWorld: Create table " + descriptor.getNameAsString());
            admin.createTable(descriptor);
    
            Table table = connection.getTable(TableName.valueOf(TABLE_NAME));
    
            System.out.println("HelloWorld: Write some greetings to the table");
            for (int i = 0; i < GREETINGS.length; i++) {
              String rowKey = "greeting" + i;
    
              Put put = new Put(Bytes.toBytes(rowKey));
              put.addColumn(COLUMN_FAMILY_NAME, COLUMN_NAME, Bytes.toBytes(GREETINGS[i]));
              table.put(put);
            }
    
            String rowKey = "greeting0";
            Result getResult = table.get(new Get(Bytes.toBytes(rowKey)));
            String greeting = Bytes.toString(getResult.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME));
            System.out.println("Get a single greeting by row key");
            System.out.printf("\t%s = %s\n", rowKey, greeting);
    
            Scan scan = new Scan();
    
            System.out.println("HelloWorld: Scan for all greetings:");
            ResultScanner scanner = table.getScanner(scan);
            for (Result row : scanner) {
              byte[] valueBytes = row.getValue(COLUMN_FAMILY_NAME, COLUMN_NAME);
              System.out.println('\t' + Bytes.toString(valueBytes));
            }
    
            System.out.println("HelloWorld: Delete the table");
            admin.disableTable(table.getName());
            admin.deleteTable(table.getName());
          } catch (IOException e) {
            if (admin.tableExists(TableName.valueOf(TABLE_NAME))) {
              System.out.println("HelloWorld: Cleaning up table");
              admin.disableTable(TableName.valueOf(TABLE_NAME));
              admin.deleteTable(TableName.valueOf(TABLE_NAME));
            }
            throw e;
          }
        } catch (IOException e) {
          System.err.println("Exception while running HelloWorld: " + e.getMessage());
          e.printStackTrace();
        }
      }
    
      public static void main(String[] args) {
        String projectId = requiredProperty("bigtable.projectID");
        String instanceId = requiredProperty("bigtable.instanceID");
    
        doHelloWorld(projectId, instanceId);
      }
    
      private static String requiredProperty(String prop) {
        String value = System.getProperty(prop);
        if (value == null) {
          throw new IllegalArgumentException("Missing required system property: " + prop);
        }
        return value;
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
