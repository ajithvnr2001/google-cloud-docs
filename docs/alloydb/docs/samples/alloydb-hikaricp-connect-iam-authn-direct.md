---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-hikaricp-connect-iam-authn-direct/
title: Create a connection pool with IAM database authentication \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:27.897683+00:00
---

# Create a connection pool with IAM database authentication  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-hikaricp-connect-iam-authn-direct/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Create a connection pool with IAM database authentication Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to configure a HikariCP connection pool to connect to an instance's private IP address. It uses a custom data source that automatically manages OAuth2 tokens to enable passwordless authentication with an IAM database user.

## Code sample

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    
    public class AlloyDbJdbcDirectPathDataSourceFactory {
    
      public static final String ALLOYDB_DB = System.getenv("ALLOYDB_DB");
      public static final String ALLOYDB_USER = System.getenv("ALLOYDB_IAM_USER");
      public static final String ALLOYDB_INSTANCE_IP = System.getenv("ALLOYDB_INSTANCE_IP");
    
      static HikariDataSource createDataSource() {
        HikariConfig config = new HikariConfig();
    
        config.setJdbcUrl(String.format("jdbc:postgresql://%s/%s", ALLOYDB_INSTANCE_IP, ALLOYDB_DB));
        config.setUsername(ALLOYDB_USER); // e.g., "postgres"
        // No need to set password, as that's dynamically configured in the
        // AlloyDBDirectPathDataSource with a refreshed OAuth2 token.
    
        return new AlloyDBDirectPathDataSource(config);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
