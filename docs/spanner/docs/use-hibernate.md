---
url: https://docs.cloud.google.com/spanner/docs/use-hibernate/
title: Integrate Spanner with Hibernate ORM (GoogleSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:44.949119+00:00
---

# Integrate Spanner with Hibernate ORM (GoogleSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-hibernate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with Hibernate ORM (GoogleSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

Hibernate is an object-relational mapping tool for the Java programming language. It provides a framework for mapping an object-oriented domain model to a relational database.

You can integrate GoogleSQL-dialect databases with Hibernate. Spanner is compatible with [Hibernate ORM 6.x and 7.x](https://hibernate.org/orm/). Hibernate ORM has a built-in Spanner dialect, and there is also a Google-maintained Hibernate dialect available [on GitHub](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate). Both dialects produce SQL, DML, and DDL statements for most common entity types and relationships using standard Hibernate and Java Persistence annotations.

## Use built-in Hibernate integration (Hibernate ORM 7.4+)

Starting with Hibernate ORM 7.4, Hibernate includes a built-in dialect for Spanner (`org.hibernate.dialect.SpannerDialect`).

We recommend that new projects use this built-in dialect, as it does not require adding the external `google-cloud-spanner-hibernate-dialect` dependency. The built-in dialect supports standard Hibernate features. If your application requires advanced Spanner-specific features, we recommend using the Google-maintained external dialect instead.

To use the built-in dialect, add the Maven dependencies for Hibernate ORM core and the Spanner JDBC driver to your project's `pom.xml` file. To find the latest versions of these dependencies, see the [Hibernate ORM releases](https://github.com/hibernate/hibernate-orm) and the [Spanner JDBC driver releases](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner-jdbc):
    
    
    <dependencies>
      <!-- Hibernate ORM Core -->
      <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>7.4.0.Final</version>
      </dependency>
    
      <!-- Cloud Spanner JDBC Driver -->
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-spanner-jdbc</artifactId>
        <version>2.40.0</version>
      </dependency>
    </dependencies>
    

Configure your project's `hibernate.properties` file (typically located in the `src/main/resources` directory) to use the built-in Spanner Dialect:
    
    
    hibernate.dialect=org.hibernate.dialect.SpannerDialect
    hibernate.connection.driver_class=com.google.cloud.spanner.jdbc.JdbcDriver
    hibernate.connection.url=jdbc:cloudspanner:/projects/YOUR-PROJECT/instances/YOUR-INSTANCE/databases/YOUR-DATABASE
    

To authenticate with Spanner, the JDBC driver requires credentials. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your [service account JSON credentials file](https://docs.cloud.google.com/docs/authentication/getting-started). Otherwise, the driver uses the default credentials set in the Google Cloud CLI `gcloud` application.

## Use Google-maintained Spanner dialect

For projects using earlier versions of Hibernate (6.x or 7.x prior to 7.4), or if you need advanced Spanner-specific features that are not yet supported by the built-in dialect, you can use the [Google-maintained Spanner Dialect](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate).

Advanced features supported by the Google-maintained dialect include:

  * Interleaved table hierarchies (`@Interleaved`)
  * Query, index, and scan hints
  * DDL schema batching
  * Transaction tagging (`@TransactionTag`)
  * Pooled sequences (`@PooledBitReversedSequenceGenerator`)



To use the Google-maintained dialect, add the Maven dependencies to your project's `pom.xml` file:
    
    
    <dependencies>
      <!-- The Spanner JDBC driver dependency -->
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-spanner-jdbc</artifactId>
      </dependency>
    
      <!-- Hibernate core dependency -->
      <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>6.4.4.Final</version>
      </dependency>
    </dependencies>

Configure your project's `hibernate.properties` file to use the Google-maintained Spanner Dialect and JDBC Driver:
    
    
    hibernate.dialect=com.google.cloud.spanner.hibernate.SpannerDialect
    hibernate.connection.driver_class=com.google.cloud.spanner.jdbc.JdbcDriver
    hibernate.connection.url=jdbc:cloudspanner:/projects/YOUR-PROJECT/instances/YOUR-INSTANCE/databases/YOUR-DATABASE
    

For more information about the features and recommendations for Hibernate when using this dialect, consult the [reference documentation](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate/blob/-/README.adoc) on GitHub.

## What's next

  * Checkout [code examples](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate/blob/-/google-cloud-spanner-hibernate-samples) using Hibernate with Spanner.
  * Try the Spanner with Hibernate ORM [codelab](https://codelabs.developers.google.com/codelabs/cloud-spanner-hibernate).
  * Learn more about [Hibernate ORM](https://hibernate.org/orm/).
  * View the repository for [Spanner Dialect](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate) on GitHub.
  * [File a GitHub issue](https://github.com/GoogleCloudPlatform/google-cloud-spanner-hibernate/issues) to report a bug or ask a question about Hibernate.
  * Learn more about [Apache Maven](https://maven.apache.org/).
  * Learn more about [Integrate Spanner with Hibernate ORM (PostgreSQL dialect)](https://docs.cloud.google.com/spanner/docs/use-hibernate-postgresql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
