---
url: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-servlet-connect-tcp/
title: Create a TCP connection by using Java \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:26.771790+00:00
---

# Create a TCP connection by using Java  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-servlet-connect-tcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/postgres/samples)



#  Create a TCP connection by using Java Stay organized with collections  Save and categorize content based on your preferences. 

Open a TCP connection to Cloud SQL for PostgreSQL by using Java.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-flexible)
  * [Connect from App Engine standard environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-standard)
  * [Connect from Cloud Build](https://docs.cloud.google.com/sql/docs/postgres/connect-build)
  * [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)
  * [Connect from Cloud Run functions](https://docs.cloud.google.com/sql/docs/postgres/connect-functions)
  * [Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy)
  * [Manage database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections)



## Code sample

### Java

To authenticate to Cloud SQL for PostgreSQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class TcpConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      private static final String INSTANCE_HOST = System.getenv("INSTANCE_HOST");
      private static final String DB_PORT = System.getenv("DB_PORT");
    
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:postgresql://<INSTANCE_HOST>:<DB_PORT>/<DB_NAME>?user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:postgresql://%s:%s/%s", INSTANCE_HOST, DB_PORT, DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "postgres"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
