---
url: https://docs.cloud.google.com/spanner/docs/use-spring-data-jdbc-googlesql/
title: Integrate Spanner with Spring Data JDBC (GoogleSQL) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:45.941873+00:00
---

# Integrate Spanner with Spring Data JDBC (GoogleSQL)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-spring-data-jdbc-googlesql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with Spring Data JDBC (GoogleSQL) Stay organized with collections  Save and categorize content based on your preferences. 

[Spring Data JDBC](https://spring.io/projects/spring-data-jdbc), part of the larger Spring Data family, makes it easier to implement JDBC based repositories in your application. It adds an abstraction layer between your application and your database that makes your application easier to port from one database system to another.

## Set up Spring Data JDBC for Spanner GoogleSQL-dialect databases

You can integrate Spanner GoogleSQL-dialect databases with Spring Data JDBC by adding a dialect for Spanner GoogleSQL to your application.

### Dialect configuration

Spring Data JDBC selects the database dialect it uses based on the JDBC driver that has been configured as a data source in Spring Data. You must add an additional dialect provider to your application to instruct Spring Data JDBC to use the GoogleSQL dialect when the Spanner JDBC driver is used:
    
    
    public class SpannerDialectProvider implements DialectResolver.JdbcDialectProvider {
      @Override
      public Optional<Dialect> getDialect(JdbcOperations operations) {
        return Optional.ofNullable(
            operations.execute((ConnectionCallback<Dialect>) SpannerDialectProvider::getDialect));
      }
    
      @Nullable
      private static Dialect getDialect(Connection connection) throws SQLException {
        DatabaseMetaData metaData = connection.getMetaData();
        String name = metaData.getDatabaseProductName().toLowerCase(Locale.ENGLISH);
        if (name.contains("spanner")) {
          return SpannerDialect.INSTANCE;
        }
        return null;
      }
    }
    

This dialect provider must be added to the `spring.factories` file in your application:
    
    
    org.springframework.data.jdbc.repository.config.DialectResolver$JdbcDialectProvider=org.springframework.data.jdbc.repository.config.DialectResolver.DefaultDialectProvider,com.google.cloud.spanner.sample.SpannerDialectProvider
    

To see an example, refer to the full [working sample application](https://github.com/googleapis/java-spanner-jdbc/tree/main/samples/spring-data-jdbc/googlesql) on GitHub.

### Dependencies

In your project, add Apache Maven dependencies for [Spring Data JDBC](https://spring.io/projects/spring-data-jdbc) and the [Spanner JDBC driver](https://github.com/googleapis/java-spanner-jdbc).
    
    
    <dependencies>
      <!-- Spring Data JDBC -->
      <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jdbc</artifactId>
      </dependency>
    
      <!-- Spanner JDBC driver -->
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-spanner-jdbc</artifactId>
      </dependency>
    <dependencies>
    

### Data source configuration

Configure `application.properties` to use the Spanner JDBC driver and connect to a Spanner GoogleSQL-dialect database.
    
    
    spanner.project=my-project
    spanner.instance=my-instance
    spanner.database=spring-data-jdbc
    
    spring.datasource.driver-class-name=com.google.cloud.spanner.jdbc.JdbcDriver
    spring.datasource.url=jdbc:cloudspanner:/projects/${spanner.project}/instances/${spanner.instance}/databases/${spanner.database}
    

## Full Sample Application

To try this integration with a sample application, see [Spring Data JDBC Sample Application with Spanner GoogleSQL](https://github.com/googleapis/java-spanner-jdbc/tree/main/samples/spring-data-jdbc/googlesql).

## What's next

  * Learn more about [Spring Data JDBC](https://spring.io/projects/spring-data-jdbc).
  * [File a GitHub issue](https://github.com/googleapis/java-spanner-jdbc/issues) to report a bug or ask a question about the Spanner JDBC driver.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
