---
url: https://docs.cloud.google.com/bigtable/docs/hbase-connecting/
title: Create a connection object \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:19.007137+00:00
---

# Create a connection object  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-connecting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a connection object

To connect to Bigtable using the Cloud Bigtable HBase client for Java, you'll need to set configuration properties, then create a [`Connection`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Connection.html) object. Creating a `Connection` object is a heavyweight operation, so create as few of these objects as possible:

  * If you use [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview), or if you use [app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) to identify different types of traffic to your instance, create one `Connection` object per app profile and share the objects among threads in your application.
  * If you don't use replication or app profiles, create a single `Connection` object and share it among threads in your application.



There are a few ways to specify the configuration settings for a `Connection` object:

  * **Include the settings in your code.** If your application uses multiple [app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) (for example, if it performs several different functions, with a separate app profile for each function), you must use this option.

You can also use this option if you prefer to keep configuration settings in your application's code, or if it's not practical to include an external configuration file as a resource in your application.

  * **Use an`hbase-site.xml` file to store settings.** Use this option if your application uses both HBase and Bigtable, or if you prefer to keep your Bigtable configuration settings in a standalone file.


**Note:** The Cloud Bigtable HBase client for Java is for customers who are migrating to Bigtable from HBase and want to continue using the HBase API. In all other cases, Java developers should instead use the [Cloud Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), which calls the Bigtable APIs. 

The following sections explain each way to configure and create a `Connection` object.

## Including settings in your code

The following example shows how you might create a `Connection` object in your own application. Replace `[VALUES_IN_BRACKETS]` with the correct values for your instance:
    
    
    package com.example.helloworld;
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import com.google.cloud.bigtable.hbase.BigtableOptionsFactory;
    import java.io.IOException;
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.hbase.client.Connection;
    
    public class BigtableHelper {
      private static final String PROJECT_ID = "[YOUR_PROJECT_ID]";
      private static final String INSTANCE_ID = "[YOUR_INSTANCE_ID]";
      // Include the following line if you are using app profiles.
      // If you do not include the following line, the connection uses the
      // default app profile.
      private static final STRING APP_PROFILE_ID = "[YOUR_APP_PROFILE_ID]";
    
      private static Connection connection = null;
    
      public static void connect() throws IOException {
        Configuration config = BigtableConfiguration.configure(PROJECT_ID, INSTANCE_ID);
        // Include the following line if you are using app profiles.
        // If you do not include the following line, the connection uses the
        // default app profile.
        config.set(BigtableOptionsFactory.APP_PROFILE_ID_KEY, APP_PROFILE_ID);
    
        connection = BigtableConfiguration.connect(config);
      }
    }
    

## Using an hbase-site.xml file

This section explains how to create a `Connection` object by including the configuration settings in an `hbase-site.xml` file.

### Sample code

The following example shows how you might configure and create a `Connection` object in your own application:
    
    
    package com.example.helloworld;
    
    import java.io.IOException;
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.hbase.HBaseConfiguration;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.ConnectionFactory;
    
    public class BigtableHelper {
      private static Connection connection = null;
    
      public static void connect() throws IOException {
        Configuration config = HBaseConfiguration.create();
        connection = ConnectionFactory.createConnection(config);
      }
    }
    

A separate `hbase-site.xml` file is included in the JAR file's resources. When you create the `Configuration` object, the Cloud Bigtable HBase client for Java automatically reads the settings from the `hbase-site.xml` file.

The following sections explain how to implement this method in your application.

### Creating the hbase-site.xml file

In your project's `src/main/resources` directory, create a file called `hbase-site.xml`. The file should contain all of the properties shown in the following example. Replace `[VALUES_IN_BRACKETS]` with the correct values for your instance:
    
    
    <configuration>
      <property>
        <name>hbase.client.connection.impl</name>
        <value>com.google.cloud.bigtable.hbase1_x.BigtableConnection</value>
      </property>
      <property>
        <name>google.bigtable.project.id</name>
        <value>[YOUR_PROJECT_ID]</value>
      </property>
      <property>
        <name>google.bigtable.instance.id</name>
        <value>[YOUR_INSTANCE_ID]</value>
      </property>
      <!--
        Include the following property if you are using app profiles.
        If you do not include the following property, the connection uses the
        default app profile.
      -->
      <property>
        <name>google.bigtable.app_profile.id</name>
        <value>[YOUR_APP_PROFILE_ID]</value>
      </property>
    </configuration>
    

### Adding hbase-site.xml to the JAR file

After you create the `hbase-site.xml` file, you'll need to update your build script to include the `src/main/resources` directory in your project's JAR file.

If you're using Maven, edit the `<build>` element of your `pom.xml` file to copy the resources to your JAR file:
    
    
    <build>
      <resources>
        <resource>
          <directory>src/main/resources</directory>
          <filtering>true</filtering>
        </resource>
      </resources>
    </build>
    

### Creating the Connection object

Now you can update your code to create a `Configuration` object. When you create this object, the Cloud Bigtable HBase client for Java automatically reads the settings from the `hbase-site.xml` file. You can then use these settings to create a `Connection` object:
    
    
    Configuration config = HBaseConfiguration.create();
    connection = ConnectionFactory.createConnection(config);
    

## What's next

  * [Learn more about the HBase client for Java](https://docs.cloud.google.com/bigtable/docs/hbase-bigtable).
  * [View a "hello world" example](https://docs.cloud.google.com/bigtable/docs/samples-java-hello).
  * [Find out how to use the client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
