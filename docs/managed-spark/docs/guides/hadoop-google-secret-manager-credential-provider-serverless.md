---
url: https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider-serverless/
title: Secret Manager Credential Provider \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:47.097968+00:00
---

# Secret Manager Credential Provider  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Secret Manager Credential Provider Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Secret Manager as a credential store with Managed Service for Apache Spark to safely store and access sensitive data processed by serverless workloads.

## Overview

The [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) can safeguard your sensitive data, such as your API keys, passwords, and certificates. You can use it to manage, access, and audit your secrets across Google Cloud.

When you run a Managed Service for Apache Spark batch workload, you can configure it to use a Secret Manager secret by using the Managed Service for Apache Spark Secret Manager Credential Provider.

## Availability

This feature is available for Managed Service for Apache Spark runtime versions 1.2.29+, 2.2.29+, or later major [runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions).

**Note:** This feature is also available for use with Managed Service for Apache Spark on clusters created with image versions 2.0.97+, 2.1.41+, 2.2.6+, or later major [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions). For Managed Service for Apache Spark cluster deployment information, see [Secret Manager Credential Provider for Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider).

## Terminology

The following table describes the terms used in this document.

Term | Description  
---|---  
`Secret` | A [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret is a global project object that contains a collection of metadata and secret versions. You can store, manage, and access secrets as binary blobs or text strings.  
`Credential` | In Hadoop and other Managed Service for Apache Spark workloads, a credential consists of a credential name (ID) and credential value (password). A credential ID and value map to a [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret ID and secret value (secret version).  
  
## Permissions

Managed Service for Apache Spark checks if the following optional secrets exist:

  * fs-gs-encryption-key
  * fs-gs-encryption-key-hash
  * fs-gs-proxy-password
  * fs-gs-proxy-username



To make sure that the [Managed Service for Apache Spark VM Service Account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) has permission to check the `fs-gs` secrets, add the [Secret Manager Secret Accessor role](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) with the following condition to the service account, as follows:
    
    
    {
      "expression": "resource.name.startsWith(\"projects/PROJECT_NUMBER/secrets/fs-gs-\")",
      "title": "gsmkeycondition",
      "description": "Permission to access Dataproc secrets"
    }
    

## Usage

You can configure [supported Hadoop and other OSS components](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/CredentialProviderAPI.html#Usage_Overview) to work with the Secret Manager by setting the following properties when you submit a Managed Service for Apache Spark workload:

  * **Provider path** (required): The provider path property, `spark.hadoop.hadoop.security.credential.provider.path`, is a comma-separated list of one or more credential provider URIs that is traversed to resolve a credential.
        
        --properties=spark.hadoop.hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID
        

    * The `scheme` in the provider path indicates the credential provider type. Hadoop schemes include `jceks://`, `user://`,`localjceks://`. Use the `gsm://` scheme to search for credentials in Secret Manager.
  * **Substitute dot operator** : The Secret Manager service does not allow dots (`.`) in secret names. However, some open source software (OSS) components use dots in their credential keys. To fix this limitation, enable this property to replace dots (`.`) with hyphens (`-`) in credential names. This ensures that OSS credentials with dots in their names can be stored and retrieved correctly from Secret Manager.

For example, If an OSS credential key is `a.b.c`, you must modify it to `a-b-c` when storing it in Secret Manager.
        
        --properties=spark.hadoop.hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true
        

This is an optional property. By default, the value is `false`. For credentials keys that have no dot (`.`) operator in their credential name, this property can be safely ignored.

  * **Secret version** : Secrets in Secret Manager can have multiple versions (values). Use this property to access a specific secret version for stable access in production environments.
        
        --properties=spark.hadoop.hadoop.security.credstore.google-secret-manager.secret-version=1
        

This is an optional property. By default, Secret Manager accesses the `LATEST` version, which resolves to the latest value of the secret at runtime. If your use case is to always access the `LATEST` version of a secret, this property can be safely ignored.




### Run a batch workload with Secret Manager Credential Provider

To [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) that uses Secret Manager Credential Provider, run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell).
    
    
    gcloud dataproc batches submit spark \
        --region=REGION \
        --jars=JARS \
        --class=MAIN_CLASS \
        --properties="spark.hadoop.hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID,spark.hadoop.hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true" \
        ...other flags as needed...
    

Replace the following:

  * REGION: a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload runs
  * JARS: workload jar path
  * MAIN_CLASS: the Jar main class
  * PROJECT_ID: your project ID, listed in the **Project info** section of the [Google Cloud console dashboard](https://console.cloud.google.com/home/dashboard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
