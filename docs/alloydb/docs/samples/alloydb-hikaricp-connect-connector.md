---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-hikaricp-connect-connector/
title: Connect using HikariCP and the Java connector \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:27.197047+00:00
---

# Connect using HikariCP and the Java connector  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-hikaricp-connect-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect using HikariCP and the Java connector Stay organized with collections  Save and categorize content based on your preferences. 

This example initializes a HikariCP data source to create and manage a pool of database connections. Using the AlloyDB Java connector with a connection pool is the recommended way to manage database connections in production applications.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect using the AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors)



## Code sample

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    
    public class AlloyDbJdbcConnectorDataSourceFactory {
    
      public static final String ALLOYDB_DB = System.getenv("ALLOYDB_DB");
      public static final String ALLOYDB_USER = System.getenv("ALLOYDB_USER");
      public static final String ALLOYDB_PASS = System.getenv("ALLOYDB_PASS");
      public static final String ALLOYDB_INSTANCE_NAME = System.getenv("ALLOYDB_INSTANCE_NAME");
    
      static HikariDataSource createDataSource() {
        HikariConfig config = new HikariConfig();
    
        config.setJdbcUrl(String.format("jdbc:postgresql:///%s", ALLOYDB_DB));
        config.setUsername(ALLOYDB_USER); // e.g., "postgres"
        config.setPassword(ALLOYDB_PASS); // e.g., "secret-password"
        config.addDataSourceProperty("socketFactory", "com.google.cloud.alloydb.SocketFactory");
        // e.g., "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
        config.addDataSourceProperty("alloydbInstanceName", ALLOYDB_INSTANCE_NAME);
    
        return new HikariDataSource(config);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
