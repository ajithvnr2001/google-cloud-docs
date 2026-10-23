---
url: https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider/
title: Use Secret Manager credential provider \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:17.694018+00:00
---

# Use Secret Manager credential provider  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use Secret Manager credential provider Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:** Learn how to use the Secret Manager as a credential store with Managed Service for Apache Spark to safely store and access sensitive data processed by applications running on a Managed Service for Apache Spark cluster.

The [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) can safeguard your sensitive data, such as your API keys, passwords, and certificates. You can use it to manage, access, and audit your secrets across Google Cloud.

You can configure a Managed Service for Apache Spark cluster or job to use a Secret Manager secret by using the the Secret Manager credential provider.

## Availability

This feature is available for use with Managed Service for Apache Spark clusters created with image versions 2.0.97+, 2.1.41+, 2.2.6+, or later major [Managed Service for Apache Spark image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions).

**Note:** This feature is also available for use with Managed Service for Apache Spark runtime versions 1.2, 2.2, or later major [Managed Service for Apache Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). For Managed Service for Apache Spark information, see [Secret Manager credential provider for Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/hadoop-google-secret-manager-credential-provider).

## Terminology

The following table describes terms used in this document.

Term | Description  
---|---  
`Secret` | A [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret is a global project object that contains a collection of metadata and secret versions. You can store, manage, and access secrets as binary blobs or text strings.  
`Credential` | In Hadoop and other Managed Service for Apache Spark-hosted applications, a credential consists of a credential name (ID) and credential value (password). A credential ID and value map to a [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret ID and secret value (secret version).  
  
## Usage

You can configure [Hadoop and other OSS components](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/CredentialProviderAPI.html#Supported_Features) to work with the Secret Manager by setting the following properties when you create a Managed Service for Apache Spark cluster or submit a job.

  * **Provider path** : The provider path property, `hadoop.security.credential.provider.path`, is a comma-separated list of one or more credential provider URIs that is traversed to resolve a credential.
        
        --properties=hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID
        

    * The `scheme` in the provider path indicates the credential provider type. Hadoop schemes include `jceks://`, `user://`,`localjceks://`. Use the `gsm://` scheme to search for credentials in Secret Manager.
  * **Substitute dot operator** : The Secret Manager service does not allow dots (`.`) in secret names. However, some open source software (OSS) components use dots in their credential keys. To fix this limitation, enable this property to replace dots (`.`) with hyphens (`-`) in credential names. This ensures that OSS credentials with dots in their names can be stored and retrieved correctly from Secret Manager.

For example, If an OSS credential key is `a.b.c`, you must modify it to `a-b-c` when storing it in Secret Manager.
        
        --properties=hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true
        

This is an optional property. By default, the value is `false`. For credentials keys that have no dot (`.`) operator in their credential name, this property can be safely ignored.

  * **Secret version** : Secrets in Secret Manager can have multiple versions (values). Use this property to access a specific secret version for stable access in production environments.
        
        --properties=hadoop.security.credstore.google-secret-manager.secret-version=1
        

This is an optional property. By default, Secret Manager accesses the `LATEST` version, which resolves to the latest value of the secret at runtime. If your use case is to always access the `LATEST` version of a secret, this property can be safely ignored.




### Create a Managed Service for Apache Spark cluster with Secret Manager credential provider

  1. Run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell) to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster) with the required properties. 
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             --properties="hadoop:hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID,hadoop:hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true" \
             ...other flags as needed...
         




Notes:

  * CLUSTER_NAME: The name of the new cluster.
  * REGION: A [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload will run.
  * PROJECT_ID: Your project ID is listed in the **Project info** section of the [Google Cloud console dashboard](https://console.cloud.google.com/home/dashboard).



### Submit a Managed Service for Apache Spark with Secret Manager credential provider

  1. Run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell) to [submit a Managed Service for Apache Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#how_to_submit_a_job) with the required properties.
         
         gcloud dataproc jobs submit CLUSTER_NAME \
             --region=REGION \
             --properties="hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID,hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true" \
             ...other flags as needed... \
             -- job-args
         




Notes:

  * CLUSTER_NAME: the name of the cluster that will run the job.
  * REGION: a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload will run.
  * PROJECT_ID: your project ID is listed in the **Project info** section of the [Google Cloud console dashboard](https://console.cloud.google.com/home/dashboard).



### Use Secret Manager with Hive Metastore

The Hive Metastore property, `javax.jdo.option.ConnectionPassword`, contains the password used to authenticate access to the metastore database. The password is saved in text format in `hive-site.xml`, which represents a security risk. A production best-practice is to store the password in Secret Manager, then update the `hive-site.xml` config file to allow the Hive metastore service to read the password from Secret Manager.

The following examples show you how to use Secret Manager in different Hive Metastore scenarios.

**Create a cluster with a local metastore**

  1. Run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell) to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster). 
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             ...other flags as needed... \
         




Notes:

  * CLUSTER_NAME: The name of the new cluster.
  * REGION: A [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload will run.


  1. Create a secret using the Secret Manager or the `hadoop credential` command. Run `hadoop credential` and other commands listed in the following examples from the Managed Service for Apache Spark master node command line after [using SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to and open a terminal window on that node.

     * **Alternative 1:** [Use the Secret Manager to create a secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

       * Secret name: `/projects/PROJECT_ID/secrets/javax-jdo-option-ConnectionPassword/versions/1`
       * Secret value: `METASTORE_PASSWORD`.
     * **Alternative 2:** Use the `hadoop credential` command to create a secret. 
           
           sudo hadoop credential create javax-jdo-option-ConnectionPassword -provider gsm://projects/PROJECT_ID -v METASTORE_PASSWORD
           

       * METASTORE_PASSWORD: Since the Secret Manager does not support the dot(`.`) operator, substitute any dot(`.`)s in the password with hyphen(`-`)s.
  2. Verify that the secret exists. 
         
         sudo hadoop credential list -provider gsm://projects/PROJECT_ID
         

  3. Use a text editor to remove the `javax.jdo.option.ConnectionPassword` property from the `hive-site.xml` file, and then add the `hadoop.security.credential.provider.path` & `hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator` properties to the file.

Example properties: 
         
         hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID
         hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true
         

  4. Restart Hive Metastore. 
         
         sudo systemctl restart hive-metastore
         




**Create a cluster with an external Hive Metastore**

  1. Run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell) to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster) with the following cluster properties. Use this cluster as an external Hive metastore for Hive jobs that run from other Managed Service for Apache Spark clusters for Spark Hive workloads.
         
         gcloud dataproc clusters create METASTORE_CLUSTER_NAME \
             --region=REGION \
             --properties=core:fs.defaultFS=gs://METASTORE_CLUSTER_PROXY_BUCKET,dataproc:dataproc.components.deactivate="hdfs hive-server2 hive-metastore" \
             ...other flags as needed...
         

  2. Create a secret using the Secret Manager or the `hadoop credential` command. Run `hadoop credential` and other commands listed in the following examples from the Managed Service for Apache Spark master node command line after [using SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to and open a terminal window on that node.

     * **Alternative 1:** [Use the Secret Manager to create a secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). 
       * Secret name: `/projects/PROJECT_ID/secrets/javax-jdo-option-ConnectionPassword/versions/1`
       * Secret value: `METASTORE_PASSWORD`.
     * **Alternative 2:** Use the `hadoop credential` command to create a secret. 
           
           sudo hadoop credential create javax-jdo-option-ConnectionPassword -provider gsm://projects/PROJECT_ID -v METASTORE_PASSWORD
           

       * METASTORE_PASSWORD: Since the Secret Manager does not support the dot(`.`) operator, substitute dot(`.`)s in the password with hyphen(`-`)s.
  3. Verify that the secret exists. 
         
         sudo hadoop credential list -provider gsm://projects/PROJECT_ID
           




**Create a cluster to run Hive jobs that connect to an external metastore**

  1. Run the following command locally or in [Cloud Shell](https://docs.cloud.google.com/shell) to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster) with the following cluster properties. Use this cluster to run Hive jobs that connect to the external metastore on another Managed Service for Apache Spark cluster. 
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             --properties="hive:javax.jdo.option.ConnectionURL=jdbc:mysql://METASTORE_CLUSTER_NAME-m/metastore,hive:hadoop.security.credential.provider.path=gsm://projects/PROJECT_ID,hive:hadoop.security.credstore.google-secret-manager.secret-id.substitute-dot-operator=true" \
             ...other flags as needed...
         




### Hadoop credential commands

You can [use SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the Managed Service for Apache Spark master node to use `hadoop credential` command to create, list, and manage secrets.

`hadoop credential` commands use the following format: `hadoop credential SUBCOMMAND OPTIONS`. In the following examples, the `-provider` flag is added to specify the provider type and location (the provider store). The `gsm://` scheme specifies the Secret Manager.

  * Create a secret with the specified secret ID. The command doesn't create the secret if the specified secret ID exists. This behavior is consistent with the Hadoop `CredentialProvider` API. 
        
        hadoop credential create SECRET_ID -provider gsm://projects/PROJECT_ID -v VALUE
        

  * List secrets stored in a project. 
        
        hadoop credential list -provider gsm://projects/PROJECT_ID
        

  * Check if a secret exists in a project with a specified value. 
        
        hadoop credential check SECRET_ID -provider gsm://projects/PROJECT_ID -v VALUE
        

  * Check for a specific secret version in a config file.
        
        hadoop credential conf CONFIG_FILE check SECRET_ID -provider gsm://projects/PROJECT_ID -v VALUE
        

  * CONFIG_FILE: The XML file that sets `hadoop.security.credstore.google-secret-manager.secret-version`.

  * Delete all versions of a secret in a project. 
        
        hadoop credential delete SECRET_ID -provider gsm://projects/ PROJECT_ID
        




See the [Hadoop Commands Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/CommandsManual.html#credential) for more information.

## What's next

  * See the [Hive documentation](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Configuration#AdminManualConfiguration-RemovingHiveMetastorePasswordfromHiveConfiguration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
