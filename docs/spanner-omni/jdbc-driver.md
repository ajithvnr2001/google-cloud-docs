---
url: https://docs.cloud.google.com/spanner-omni/jdbc-driver/
title: Use the JDBC driver to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:42.829090+00:00
---

# Use the JDBC driver to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/jdbc-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use the JDBC driver to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use the Spanner JDBC driver to connect your Java applications to Spanner Omni and execute SQL statements.

Java Database Connectivity (JDBC) is a standard Java API that provides a consistent way for applications to interact with relational databases. The Spanner JDBC driver works with Spanner Omni in the same way it works with Spanner.

By using the JDBC driver, you can leverage standard JDBC-compatible tools and libraries with Spanner Omni.

Spanner Omni JDBC connections support plain text, TLS, TLS with credentials, and mTLS.

For more information, see [Get started with Spanner in JDBC](https://docs.cloud.google.com/spanner/docs/getting-started/jdbc) in the Spanner documentation.

## Before you begin

To use Spanner Omni with the JDBC driver, use the Spanner JDBC driver version 2.41.0 or later.

If you use Maven without the Bill of Materials (BOM), add the following to the `pom.xml` file dependencies:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-spanner-jdbc</artifactId>
      <version>2.41.0</version>
    </dependency>
    

## Connection URL considerations

Because Spanner Omni is not directly connected to a Google Cloud project, the `projects/name` component is not required in the JDBC connection URL. Similarly, because each Spanner Omni deployment has a single, already-created instance (`instances/default`), the `instances/name` component is optional.

To connect the JDBC driver to Spanner Omni instead of Spanner, append the `;type=omni` property to the connection URL.

## Establish a Spanner Omni connection

The following examples show how to establish a connection with Spanner Omni using the Spanner JDBC driver for each supported security configuration:

###  Plain text 

To establish a plain-text connection, use a connection URL similar to the following:
    
    
    String url = "jdbc:spanner://HOST_ADDRESS:PORT/databases/DATABASE_ID;usePlainText=true;type=omni";
    try (java.sql.Connection connection = DriverManager.getConnection(url)) {
      try (ResultSet rs = connection.createStatement().executeQuery("SELECT * FROM Singers")) {
        while (rs.next()) {
          System.out.print(rs.getLong(1) + "\t");
          System.out.println(rs.getString(2));
        }
      }
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
    

###  TLS 

To establish a TLS connection, add the CA certificate to the Java truststore or specify a custom truststore when you run the application, as described in [Configure the Java truststore](https://docs.cloud.google.com/spanner-omni/java#configure-truststore). The JDBC URL does not require any additional authentication parameters:
    
    
    String url = "jdbc:spanner://HOST_ADDRESS:PORT/databases/DATABASE_ID;type=omni";
    

###  TLS with credentials 

To establish a TLS connection with username and password authentication, add the CA certificate to the Java truststore as described in [Configure the Java truststore](https://docs.cloud.google.com/spanner-omni/java#configure-truststore), and specify the `username` and `password` properties in the JDBC URL:
    
    
    String url = "jdbc:spanner://HOST_ADDRESS:PORT/databases/DATABASE_ID;type=omni;username=USERNAME;password=PASSWORD";
    

###  mTLS 

To establish an mTLS connection, add the CA certificate to the Java truststore as described in [Configure the Java truststore](https://docs.cloud.google.com/spanner-omni/java#configure-truststore), and specify the `clientCertificate` and `clientKey` parameters in the JDBC URL. The client private key must be in a Java-compliant PKCS#8 format, as described in the [Java SDK mTLS instructions](https://docs.cloud.google.com/spanner-omni/java#mtls):
    
    
    String url = "jdbc:spanner://HOST_ADDRESS:PORT/databases/DATABASE_ID;type=omni;clientCertificate=PATH_TO_CLIENT_CERT;clientKey=PATH_TO_CLIENT_KEY";
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
