---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/ssl-certificates/
title: Use SSL certificates with templates \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:38.437502+00:00
---

# Use SSL certificates with templates  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/ssl-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use SSL certificates with templates Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to stage files on Dataflow worker VMs to use SSL certificates with the Google-provided Java Database Connectivity (JDBC) templates. You can also use the steps in this page to stage files dynamically on the worker VM before processing begins.

## Stage files on worker VMs

With some templates, you can stage files on Dataflow worker VMs by using the `extraFilesToStage` template parameter. Use this parameter to stage files dynamically on the worker VM before data processing begins. You might use this parameter in the following cases:

  * Store certificate and key files on each worker for SSL connections.
  * Because Dataflow doesn't include built-in support for Secret Manager, use this parameter to configure templates to store and access Secret Manager secrets.



This parameter is available in some but not all templates. To see if the parameter is available with the template that you're using, see the template parameters table for your template in [Google-provided Dataflow streaming templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates#streaming-templates) or [Google-provided Dataflow batch templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates#batch-templates).

When you use this parameter, comma separated Cloud Storage paths or Secret Manager secrets are passed to the worker and saved in the `/extra_files` directory on each worker. When the files are saved in the `/extra_files` directory, other parameters can reference them. To reference the files, in the configuration properties, specify file paths relative to the `/extra_files` directory.

All Cloud Storage files passed using this parameter are stored in the `/extra_files` directory with the same filename. Secret Manager secrets are stored in the `/extra_files` directory with the secret name used as the filename.

For example, when you set `extraFilesToStage` to the following path, the files are stored in the `/extra_files` directory of each worker with the filenames `file.txt` and SECRET_ID.
    
    
    gs://BUCKET_NAME/file.txt,projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID
    

## Configure SSL certificates

With templates that use JDBC to read or write, you can use the `extraFilesToStage` template parameter to stage certificates as local files on worker VMs, and then reference the local filename in the JDBC connection URL or in the connection properties.

JDBC SSL connections differ based on the database. This section provides examples for PostgreSQL and MySQL databases.

If you need to set Java system properties, use [`JvmInitializer`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/harness/JvmInitializer.html). You can use `JvmInitializer` to perform one-time initialization on all Dataflow Java workers.

### PostgreSQL

For SSL connections in PostgreSQL databases, the following parameters are available: `ssl`, `sslmode`, `sslcert`, `sslkey`, and `sslrootcert`.

  * To specify that the connection should use SSL and what mode to use, use the `ssl` and `sslmode` parameters.
  * For client validation, use the `sslcert` and `sslkey` parameters.
  * For server validation, use the `sslrootcert` parameter.



When you connect to PostgreSQL, set the following parameters:
    
    
    extraFilesToStage=gs://BUCKET_NAME/root_cert.crt,gs://BUCKET_NAME/cert.crt,gs://BUCKET_NAME/key.key
    
    connectionUrl=jdbc:postgresql://HOST/DATABASE?ssl=true&sslrootcert=/extra_files/root_cert.crt&sslcert=/extra_files/cert.crt&sslkey=/extra_files/key.key&OTHER_PARAMETERS...
    

For additional PostgreSQL JDBC configuration parameters and more details about the parameters, see [Connection Parameters](https://jdbc.postgresql.org/documentation/use/#connection-parameters) in the JDBC PostgreSQL documentation.

### MySQL

For SSL connections in MySQL databases, the following parameters are available: `sslmode`, `trustCertificateKeyStoreUrl`, and `clientCertificateKeyStoreUrl`.

  * To specify that the connection should use SSL and what mode to use, use the `sslmode` parameter.
  * For client validation, use the `clientCertificateKeyStoreUrl` parameter.
  * For server validation, use the `trustCertificateKeyStoreUrl` parameter.



When you connect to MySQL, set the following parameters:
    
    
    extraFilesToStage=gs://BUCKET_NAME/truststore.jks,gs://BUCKET_NAME/cert.crt,gs://BUCKET_NAME/keystore.jks
    
    connectionUrl=jdbc:mysql://HOST/DATABASE?sslmode=REQUIRED&trustCertificateKeyStoreUrl=file:/extra_files/truststore.jks&sslcert=file:/extra_files/keystore.jks&OTHER_PARAMETERS...
    

For additional MySQL JDBC configuration parameters and more details about the parameters, see the [security connectors](https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-connp-props-security.html) page in the MySQL documentation.

### SSL connection example

The following example demonstrates how to run the [Pub/Sub to JDBC](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-jdbc) template with SSL connections in a MySQL database.
    
    
    #!/bin/bash
    
    gcloud config set project PROJECT_ID
    
    echo "Running template ..."
    gcloud dataflow flex-template run my-job \
            --template-file-gcs-location="gs://dataflow-templates/latest/flex/Pubsub_to_Jdbc" \
    --region="REGION" \
    --parameters= \
    driverClassName="com.mysql.jdbc.Driver",\
    connectionUrl="jdbc:mysql://HOST/DATABASE?sslmode=REQUIRED&trustCertificateKeyStoreUrl=file:/extra_files/truststore.jks&sslcert=file:/extra_files/keystore.jks",\
    driverJars="gs://BUCKET_NAME/mysql.jar",\
    statement="INSERT INTO tableName (column1, column2) VALUES (?,?)",\
    inputSubscription="projects/PROJECT_ID/subscriptions/subscription",\
    outputDeadletterTopic="projects/PROJECT_ID/topics/topic",\
    extraFilesToStage="gs://BUCKET_NAME/truststore.jks,gs://BUCKET_NAME/cert.crt,gs://BUCKET_NAME/keystore.jks"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
