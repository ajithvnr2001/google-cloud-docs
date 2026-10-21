---
url: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-servlet-connection/
title: PostgreSQL servlet connection \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:21.436659+00:00
---

# PostgreSQL servlet connection  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-servlet-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/postgres/samples)



#  PostgreSQL servlet connection Stay organized with collections  Save and categorize content based on your preferences. 

Run a SQL INSERT statement to open and close a connection to Cloud SQL for PostgreSQL by using the HikariCP JDBC connection pool library.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections)



## Code sample

### Java

To authenticate to Cloud SQL for PostgreSQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Using a try-with-resources statement ensures that the connection is always released back
    // into the pool at the end of the statement (even if an error occurs)
    try (Connection conn = pool.getConnection()) {
    
      // PreparedStatements can be more efficient and project against injections.
      String stmt = "INSERT INTO votes (time_cast, candidate) VALUES (?, ?);";
      try (PreparedStatement voteStmt = conn.prepareStatement(stmt);) {
        voteStmt.setTimestamp(1, now);
        voteStmt.setString(2, team);
    
        // Finally, execute the statement. If it fails, an error will be thrown.
        voteStmt.execute();
      }
    } catch (SQLException ex) {
      // If something goes wrong, handle the error in this section. This might involve retrying or
      // adjusting parameters depending on the situation.
      // ...
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
