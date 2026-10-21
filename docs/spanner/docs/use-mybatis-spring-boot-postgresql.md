---
url: https://docs.cloud.google.com/spanner/docs/use-mybatis-spring-boot-postgresql/
title: Integrate Spanner with MyBatis and Spring Boot (PostgreSQL) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:04.104538+00:00
---

# Integrate Spanner with MyBatis and Spring Boot (PostgreSQL)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-mybatis-spring-boot-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with MyBatis and Spring Boot (PostgreSQL) Stay organized with collections  Save and categorize content based on your preferences. 

[MyBatis](https://mybatis.org/mybatis-3/) is a persistence framework with support for custom SQL and advanced mappings. MyBatis eliminates most of the JDBC code and manual setting of parameters and retrieval of results in your application.

## Set up MyBatis for Spanner PostgreSQL-dialect databases

You can integrate Spanner PostgreSQL-dialect databases with MyBatis and Spring Boot using the Spanner JDBC driver.

You don't need to use [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter) for this integration.

### Dependencies

In your project, add Apache Maven dependencies for [MyBatis](https://mybatis.org/mybatis-3/), [Spring Boot](https://spring.io/projects/spring-boot), and the [Spanner JDBC driver](https://github.com/googleapis/java-spanner-jdbc).
    
    
    <dependencies>
      <!-- MyBatis and Spring Boot -->
      <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
      </dependency>
      <dependency>
        <groupId>org.mybatis.dynamic-sql</groupId>
        <artifactId>mybatis-dynamic-sql</artifactId>
      </dependency>
    
      <!-- Spanner JDBC driver -->
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-spanner-jdbc</artifactId>
      </dependency>
    <dependencies>
    

### Data source configuration

Configure `application.properties` to use the Spanner JDBC driver and to connect to a Spanner PostgreSQL-dialect database.
    
    
    # This profile uses a Spanner PostgreSQL database.
    
    spanner.project=my-project
    spanner.instance=my-instance
    spanner.database=mybatis-sample
    
    spring.datasource.driver-class-name=com.google.cloud.spanner.jdbc.JdbcDriver
    spring.datasource.url=jdbc:cloudspanner:/projects/${spanner.project}/instances/${spanner.instance}/databases/${spanner.database}
    

## Full sample application

To try this integration with a sample application, see [Spring Data MyBatis Sample Application with Spanner PostgreSQL](https://github.com/googleapis/java-spanner-jdbc/tree/main/samples/spring-data-mybatis/postgresql).

## What's next

  * Learn more about [MyBatis](https://mybatis.org/mybatis-3/).
  * Learn more about [MyBatis and Spring Boot](https://mybatis.org/spring-boot-starter/mybatis-spring-boot-autoconfigure/index.html).
  * Learn more about [Spring Boot](https://spring.io/projects/spring-boot).
  * [File a GitHub issue](https://github.com/googleapis/java-spanner-jdbc/issues) to report a bug or ask a question about the Spanner JDBC driver.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
