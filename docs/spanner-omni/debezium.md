---
url: https://docs.cloud.google.com/spanner-omni/debezium/
title: Use Debezium to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:22.769625+00:00
---

# Use Debezium to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/debezium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use Debezium to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

[Debezium](https://debezium.io/) is an open source distributed platform for change data capture (CDC). The [Debezium connector for Spanner](https://github.com/debezium/debezium-connector-spanner) captures row-level changes from Spanner change streams and streams them to Apache Kafka topics.

The Debezium connector works with Spanner Omni in the same way it works with Spanner. This document shows you how to configure the Debezium connector to connect to Spanner Omni.

Spanner Omni Debezium connections support three security configurations: plain text, TLS, and mutual TLS (mTLS).

## Before you begin

To use the Debezium connector with Spanner Omni, ensure that you meet the following prerequisites:

  * Download and install the [Debezium connector for Spanner](https://github.com/debezium/debezium-connector-spanner) plugin version 3.7.0 or later in your Kafka Connect plugin directory.
  * Set up Apache Kafka and Kafka Connect. For more information, see the [Debezium installation guide](https://debezium.io/documentation/reference/stable/install.html).
  * Create a database and a change stream in Spanner Omni. For more information, see [Change streams](https://docs.cloud.google.com/spanner/docs/change-streams) in the Spanner documentation.



## Configure the Debezium connector

To connect the Debezium connector to Spanner Omni, specify the following properties in your Kafka Connect connector configuration:

  * `connector.class`: Set to `io.debezium.connector.spanner.SpannerConnector`.
  * `spanner.type`: Set to `OMNI`. When set to `OMNI`, `gcp.spanner.project.id` and `gcp.spanner.instance.id` are automatically set to `default` and are not required in the configuration.
  * `gcp.spanner.host`: The Spanner Omni endpoint, for example, `http://localhost:15000` for plain text or `https://localhost:15000` for TLS and mTLS.
  * `gcp.spanner.database.id`: The ID of your Spanner Omni database.
  * `gcp.spanner.change-stream.name`: The name of the change stream to capture.
  * `spanner.omni.use.plaintext`: Optional. Set to `true` to establish a plain-text connection.
  * `spanner.omni.client.cert.path`: Optional. The path to the client certificate file for mTLS connections.
  * `spanner.omni.client.key.path`: Optional. The path to the client private key file in PKCS#8 format for mTLS connections.



## Establish a connection

The following examples show how to configure the Debezium connector for each supported security configuration:

###  Plain text 

To establish a plain-text connection, set `spanner.type` to `OMNI`, specify the endpoint with `http://`, and set `spanner.omni.use.plaintext` to `true`:
    
    
    {
      "name": "CONNECTOR_NAME",
      "config": {
        "connector.class": "io.debezium.connector.spanner.SpannerConnector",
        "tasks.max": "1",
        "spanner.type": "OMNI",
        "gcp.spanner.host": "http://ENDPOINT",
        "gcp.spanner.database.id": "DATABASE_ID",
        "gcp.spanner.change-stream.name": "CHANGE_STREAM_NAME",
        "spanner.omni.use.plaintext": "true"
      }
    }
    

Replace the following:

  * `CONNECTOR_NAME`: the name for your Debezium connector instance, for example, `spanner-omni-connector`.

  * `ENDPOINT`: the endpoint of your Spanner Omni instance, for example, `localhost:15000`.

  * `DATABASE_ID`: the ID of your Spanner Omni database, for example, `test-db`.

  * `CHANGE_STREAM_NAME`: the name of the change stream in your database, for example, `my_change_stream`.




###  TLS 

To establish a TLS connection, add the Spanner Omni CA certificate to the Java truststore as described in [Configure the Java truststore](https://docs.cloud.google.com/spanner-omni/java#configure-truststore). Set `spanner.type` to `OMNI` and specify the endpoint using `https://`:
    
    
    {
      "name": "CONNECTOR_NAME",
      "config": {
        "connector.class": "io.debezium.connector.spanner.SpannerConnector",
        "tasks.max": "1",
        "spanner.type": "OMNI",
        "gcp.spanner.host": "https://ENDPOINT",
        "gcp.spanner.database.id": "DATABASE_ID",
        "gcp.spanner.change-stream.name": "CHANGE_STREAM_NAME"
      }
    }
    

Replace the following:

  * `CONNECTOR_NAME`: the name for your Debezium connector instance, for example, `spanner-omni-connector`.

  * `ENDPOINT`: the endpoint of your Spanner Omni instance, for example, `localhost:15000`.

  * `DATABASE_ID`: the ID of your Spanner Omni database, for example, `test-db`.

  * `CHANGE_STREAM_NAME`: the name of the change stream in your database, for example, `my_change_stream`.




###  mTLS 

To establish an mTLS connection, add the Spanner Omni CA certificate to the Java truststore as described in [Configure the Java truststore](https://docs.cloud.google.com/spanner-omni/java#configure-truststore). Set `spanner.type` to `OMNI`, specify the endpoint using `https://`, and specify the paths to your client certificate and client private key. The client private key must be in a Java-compliant PKCS#8 format, as described in the [Java SDK mTLS instructions](https://docs.cloud.google.com/spanner-omni/java#mtls):
    
    
    {
      "name": "CONNECTOR_NAME",
      "config": {
        "connector.class": "io.debezium.connector.spanner.SpannerConnector",
        "tasks.max": "1",
        "spanner.type": "OMNI",
        "gcp.spanner.host": "https://ENDPOINT",
        "gcp.spanner.database.id": "DATABASE_ID",
        "gcp.spanner.change-stream.name": "CHANGE_STREAM_NAME",
        "spanner.omni.client.cert.path": "PATH_TO_CLIENT_CERT",
        "spanner.omni.client.key.path": "PATH_TO_CLIENT_KEY"
      }
    }
    

Replace the following:

  * `CONNECTOR_NAME`: the name for your Debezium connector instance, for example, `spanner-omni-connector`.

  * `ENDPOINT`: the endpoint of your Spanner Omni instance, for example, `localhost:15000`.

  * `DATABASE_ID`: the ID of your Spanner Omni database, for example, `test-db`.

  * `CHANGE_STREAM_NAME`: the name of the change stream in your database, for example, `my_change_stream`.

  * `PATH_TO_CLIENT_CERT`: the path to your client certificate file.

  * `PATH_TO_CLIENT_KEY`: the path to your client private key file in PKCS#8 format.




## What's next

  * [Create and manage change streams](https://docs.cloud.google.com/spanner/docs/change-streams/manage).

  * Build [change streams connections to Kafka](https://docs.cloud.google.com/spanner/docs/change-streams/use-kafka).

  * Learn about [Spanner Omni authentication and authorization](https://docs.cloud.google.com/spanner-omni/authentication).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
