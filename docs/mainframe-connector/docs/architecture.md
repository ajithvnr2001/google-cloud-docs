---
url: https://docs.cloud.google.com/mainframe-connector/docs/architecture/
title: Mainframe Connector architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:21.249595+00:00
---

# Mainframe Connector architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Mainframe Connector architecture Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector is typically deployed as a Java application. As the application is self contained, you need to only install [IBM JRE version 8](https://www.ibm.com/support/pages/java-sdk-downloads-version-80) or [IBM JRE version 17](https://www.ibm.com/support/pages/ibm-semeru-runtime-certified-edition-version-17-websphere-liberty-using-archives) to deploy Mainframe Connector. A job control language (JCL) procedure is the frontend that you can use to call Mainframe Connector. The following image gives an overview of Mainframe Connector architecture.

![Mainframe Connector architecture](https://docs.cloud.google.com/static/mainframe-connector/docs/images/mainframe-connector-architecture.png)Mainframe Connector architecture 

When uploading data files to [Cloud Storage](https://docs.cloud.google.com/storage/docs), Mainframe Connector communicates directly with the [Cloud Storage API](https://docs.cloud.google.com/storage/docs/apis) using either [IBM z Integrated Information Processor (zIIP)](https://www.ibm.com/products/z-integrated-information-processor) or general processor (GP). You can also deploy a [remote service to offload some of the computation to Google Cloud](https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding).

After a data file is uploaded to Cloud Storage, Mainframe Connector sends a remote procedure call (RPC) to the gRPC service indicating the location of the file, the record layout, and the output location. The gRPC service reads the file from Cloud Storage, transcodes the data, and writes a multi-part [Optimized Row Columnar (ORC)](https://orc.apache.org/) file to the Cloud Storage output location. Mainframe Connector then communicates directly with the [BigQuery API](https://docs.cloud.google.com/bigquery/docs/reference/libraries-overview) to register the ORC file as an external table or load the ORC file into a table.

Alternately, you can deploy a hardware device in your data center to transfer data directly from the mainframe storage system to Cloud Storage using a virtual tape library (VTL). This approach uses neither [zIIP](https://www.ibm.com/products/z-integrated-information-processor) or GP during the data transfer to Cloud Storage because the hardware device receives the data directly from the mainframe storage system using a VTL and does not use the mainframe at all. This frees up the mainframe for business-critical tasks.

### Data encryption

IBM provides a [Java Cryptography Extension (JCE)](https://www.ibm.com/docs/en/i/7.6.0?topic=security-java-cryptography-extension) implementation with the JVM called Java Cryptography Extension Common Cryptographic Architecture (IBMJCECCA) ([Java 8](https://www.ibm.com/docs/en/sdk-java-technology/8?topic=components-ibmjcecca) or [Java 17](https://www.ibm.com/docs/en/semeru-runtime-ce-z/17.0.0?topic=guide-ibmjcecca)) that uses the hardware cryptography system on [IBM z/OS](https://www.ibm.com/products/zos). The transport layer security (TLS) connection between the JVM and Google Cloud API endpoints use JCE and hardware cryptography to secure data during the extract, transform, and load (ETL) operations.

### JCL procedure

To use JCL procedures, you must install a BQSH shell interpreter in your mainframe [procedure libraries (PROCLIB)](https://www.ibm.com/docs/en/zos/3.1.0?topic=libraries-procedure-proclib). The standard environment (STDENV) data in the JCL procedure is used to set environment variables, JVM arguments, and Java classpath before launching the Java application. A JCL procedure launches the JVM and main class `com.google.cloud.bqsh.Bqsh` using [IBM JVMLDM86 JVM launcher](https://public.dhe.ibm.com/software/Java/Java80/JZOS/jzos_users_guide_v8.pdf).

### BQSH shell interpreter

The BQSH main class acts as a shell interpreter. It reads stream input from a JCL procedure, splits lines of input, and attempts to interpret each line as a command.

### Java application

The Mainframe Connector uses [Java Cloud Client Libraries](https://docs.cloud.google.com/java/docs/reference), [Apache ORC](https://orc.apache.org/), and other open source libraries. It uses [IBM proprietary JZOS SDK](https://www.ibm.com/docs/en/semeru-runtime-ce-z/17?topic=sdk-user-guide) to interact with the IBM z/OS storage system and runs on the JVM on IBM z/OS and [OpenJDK on Linux](https://openjdk.org/).

## What's Next

  * [Mainframe Connector configurations](https://docs.cloud.google.com/mainframe-connector/docs/configurations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
