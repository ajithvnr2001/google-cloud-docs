---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-jdbc-query/
title: JDBC query \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:42.456435+00:00
---

# JDBC query  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-jdbc-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  JDBC query Stay organized with collections  Save and categorize content based on your preferences. 

Run a query by using JDBC.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect JDBC to a GoogleSQL-dialect database](https://docs.cloud.google.com/spanner/docs/use-oss-jdbc)



## Code sample

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Statement;
    
    public class SingleUseReadOnlyExample {
    
      static void singleUseReadOnly() throws SQLException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        singleUseReadOnly(projectId, instanceId, databaseId);
      }
    
      static void singleUseReadOnly(String projectId, String instanceId, String databaseId)
          throws SQLException {
        String connectionUrl =
            String.format(
                "jdbc:cloudspanner:/projects/%s/instances/%s/databases/%s",
                projectId, instanceId, databaseId);
        try (Connection connection = DriverManager.getConnection(connectionUrl);
            Statement statement = connection.createStatement()) {
          // When the connection is in autocommit mode, any query that is executed will automatically
          // be executed using a single-use read-only transaction, even if the connection itself is in
          // read/write mode.
          try (ResultSet rs =
              statement.executeQuery(
                  "SELECT SingerId, FirstName, LastName, Revenues FROM Singers ORDER BY LastName")) {
            while (rs.next()) {
              System.out.printf(
                  "%d %s %s %s%n",
                  rs.getLong(1), rs.getString(2), rs.getString(3), rs.getBigDecimal(4));
            }
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
