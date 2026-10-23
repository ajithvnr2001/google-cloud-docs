---
url: https://docs.cloud.google.com/spanner/docs/use-hibernate-postgresql/
title: Integrate Spanner with Hibernate ORM (PostgreSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:13.026799+00:00
---

# Integrate Spanner with Hibernate ORM (PostgreSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-hibernate-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with Hibernate ORM (PostgreSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

Hibernate is an object-relational mapping tool for the Java programming language. It provides a framework for mapping an object-oriented domain model to a relational database.

You can integrate PostgreSQL-dialect databases with Hibernate using the open source Spanner JDBC driver. [Hibernate ORM 7.4](https://hibernate.org/orm/) is supported with PostgreSQL-dialect databases.

## Set up Hibernate with PostgreSQL

In your Google Cloud project, add Apache Maven dependencies for the Hibernate ORM core and Spanner JDBC driver.
    
    
    <!-- Hibernate core dependency -->
    <dependency>
      <groupId>org.hibernate.orm</groupId>
      <artifactId>hibernate-core</artifactId>
      <version>7.4.0.Final</version>
    </dependency>
    
    <!-- Spanner JDBC Driver dependency -->
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-spanner-jdbc</artifactId>
      <version>2.40.0</version>
    </dependency>
    

## Set up Hibernate properties

Configure `hibernate.properties` to use the `SpannerPostgreSQLDialect`, Spanner JDBC driver, and required connection properties in the URL.
    
    
    hibernate.dialect=org.hibernate.dialect.SpannerPostgreSQLDialect
    hibernate.connection.driver_class=com.google.cloud.spanner.jdbc.JdbcDriver
    
    hibernate.connection.url=jdbc:cloudspanner:/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID?defaultsequencekind=bit_reversed_positive
    
    hibernate.show_sql=true
    hibernate.format_sql=true
    
    # hibernate.hbm2ddl.auto validate
    hibernate.hbm2ddl.auto=update
    

## Use Hibernate

For more information about the features and recommendations for integrating Hibernate with PostgreSQL-dialect databases, please consult the [reference documentation](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate/blob/main/README.md) on GitHub.

## What's next

  * Learn more about [Spanner JDBC driver](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner-jdbc).
  * Learn more about [Hibernate ORM](https://hibernate.org/orm/).
  * For more information about Spanner JDBC driver connection options, see [JDBC Connection Options](https://github.com/googleapis/google-cloud-java/blob/main/java-spanner-jdbc/documentation/connection_properties.md) in the Google Cloud Java GitHub repository.
  * Learn more about [Integrate Spanner with Hibernate ORM (GoogleSQL dialect)](https://docs.cloud.google.com/spanner/docs/use-hibernate).
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
