---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-jdbc-batch-transaction/
title: JDBC batch transaction \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:43.268521+00:00
---

# JDBC batch transaction  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-jdbc-batch-transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  JDBC batch transaction Stay organized with collections  Save and categorize content based on your preferences. 

Make a batch transaction by using JDBC.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect JDBC to a GoogleSQL-dialect database](https://docs.cloud.google.com/spanner/docs/use-oss-jdbc)



## Code sample

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableList;
    import java.math.BigDecimal;
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.PreparedStatement;
    import java.sql.SQLException;
    import java.util.Arrays;
    
    class BatchDmlExample {
      static class Singer {
        final long singerId;
        final String firstName;
        final String lastName;
        final BigDecimal revenues;
    
        Singer(long singerId, String firstName, String lastName, BigDecimal revenues) {
          this.singerId = singerId;
          this.firstName = firstName;
          this.lastName = lastName;
          this.revenues = revenues;
        }
      }
    
      static void batchDml() throws SQLException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        batchDml(projectId, instanceId, databaseId);
      }
    
      // This example shows how to execute a batch of DML statements with the JDBC driver.
      static void batchDml(String projectId, String instanceId, String databaseId) throws SQLException {
        String connectionUrl =
            String.format(
                "jdbc:cloudspanner:/projects/%s/instances/%s/databases/%s",
                projectId, instanceId, databaseId);
    
        ImmutableList<Singer> singers = ImmutableList.of(
            new Singer(10, "Marc", "Richards", BigDecimal.valueOf(10000)),
            new Singer(11, "Amirah", "Finney", BigDecimal.valueOf(195944.10d)),
            new Singer(12, "Reece", "Dunn", BigDecimal.valueOf(10449.90))
        );
    
        try (Connection connection = DriverManager.getConnection(connectionUrl)) {
          connection.setAutoCommit(false);
          // Use prepared statements for the lowest possible latency when executing the same SQL string
          // multiple times.
          try (PreparedStatement statement = connection.prepareStatement(
              "INSERT INTO Singers (SingerId, FirstName, LastName, Revenues)\n" 
                  + "VALUES (?, ?, ?, ?)")) {
            for (Singer singer : singers) {
              statement.setLong(1, singer.singerId);
              statement.setString(2, singer.firstName);
              statement.setString(3, singer.lastName);
              statement.setBigDecimal(4, singer.revenues);
              // Add the current parameter values to the batch.
              statement.addBatch();
            }
            // Execute the batched statements.
            int[] updateCounts = statement.executeBatch();
            connection.commit();
            System.out.printf("Batch insert counts: %s%n", Arrays.toString(updateCounts));
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
