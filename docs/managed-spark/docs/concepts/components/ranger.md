---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger/
title: Managed Service for Apache Spark optional Ranger component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:36.984530+00:00
---

# Managed Service for Apache Spark optional Ranger component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Ranger component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Ranger when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes the Ranger component.

The [Apache Ranger](https://ranger.apache.org/) component is an open source framework to manage permission and auditing for the Hadoop ecosystem. The Ranger `admin` server and Web UI are available on port `6080` on the cluster's first master node.

**Also see:**

  * [Using Ranger with Kerberos](https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger-w-kerberos)

  * [Back up and restore a Ranger schema](https://docs.cloud.google.com/managed-spark/docs/concepts/components/backup-ranger-schema)

  * [Best practices to use Apache Ranger on Dataproc](https://cloud.google.com/blog/products/data-analytics/running-cloud-managed-spark-and-hadoop-using-ranger)




## Install the component

Note: Before running the gcloud CLI commands on this page, either: 

  1. [set the gcloud CLI project ID](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#EXAMPLES) or
  2. add the [`--project PROJECT_ID`](https://docs.cloud.google.com/sdk/gcloud/reference#--project) flag to each gcloud command



Install the component when you create a Managed Service for Apache Spark cluster. Components can be added to clusters created with Managed Service for Apache Spark [version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later. The Ranger component requires the installation of the [Solr](https://docs.cloud.google.com/managed-spark/docs/concepts/components/solr) component.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Installation steps:

  1. Set up your Ranger `admin` password:

     1. Grant the [Cloud Key Management Service CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) to the cluster [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_cloud_dataproc). By default, the cluster service account is set as the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which has following form: 
            
            project-number-compute@developer.gserviceaccount.com
            

You can [specify a different cluster service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#using_service_accounts) when you create the cluster. 
        1. **Example:** Grant the Cloud KMS CryptoKey Encrypter/Decrypter role to the Compute Engine default service account: 
               
               gcloud projects add-iam-policy-binding project-id \
                   --member=serviceAccount:project-number-compute@developer.gserviceaccount.com \
                   --role=roles/cloudkms.cryptoKeyDecrypter
               

     2. Encrypt your Ranger `admin` password using a [Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) key. For pre-2.2 image version clusters, the password must consist of at least 8 characters, with at least one alphabetic and one numeric character. For 2.2 and later image version clusters, the password must consist of at least 8 characters, with at least one uppercase letter, one lowercase letter, and one numeric character. 
        1. **Example** : 
           1. Create the key ring: 
                  
                  gcloud kms keyrings create my-keyring --location=global
                  

           2. Create the key: 
                  
                  gcloud kms keys create my-key \
                      --location=global \
                      --keyring=my-keyring \
                      --purpose=encryption
                  

           3. Encrypt your Ranger `admin` user password: 
                  
                  echo 'my-ranger-admin-password' | \
                    gcloud kms encrypt \
                      --location=global \
                      --keyring=my-keyring \
                      --key=my-key \
                      --plaintext-file=- \
                      --ciphertext-file=admin-password.encrypted
                  

     3. Upload the encrypted password to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your project. 
        1. **Example** : 
               
               gcloud storage cp admin-password.encrypted gs://my-bucket
               

  2. Create your cluster:

     1. When installing the Ranger component, the [Solr component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/solr) must also be installed. 
        1. The Ranger component relies on the Solr component to store and query its audit logs, which by default uses HDFS as storage. This HDFS data is deleted when the cluster is deleted. To configure the Solr component to store data, including the Ranger audit logs, on Cloud Storage, use the `dataproc:solr.gcs.path=gs://<bucket>` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) when you create your cluster. Cloud Storage data persists after the cluster is deleted.
     2. Pass the KMS key and password Cloud Storage URIs to the cluster creation command by setting the `dataproc:ranger.kms.key.uri` and `dataproc:ranger.admin.password.uri` [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties).
     3. Optionally, you can pass in the Ranger database's `admin` user password through an encrypted Cloud Storage file URI by setting the `dataproc:ranger.db.admin.password.uri` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties).
     4. By default, the Ranger component uses the MySql database instance running on the cluster's first master node. To persist the Ranger database after cluster deletion, you can configure the cluster to use an external [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql) instance. To use an external Cloud SQL instance, do the following:

        1. Prior to cluster creation, you must [configure the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/flags) to enable the `log_bin_trust_function_creators` database flag by setting it to `on`. This allows the Ranger schema setup scripts to run during cluster creation. After successful cluster creation, you can reset this flag to `off`.
        2. Set the `dataproc:ranger.cloud-sql.instance.connection.name` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties) to the Cloud SQL instance.
        3. Set the `dataproc:ranger.cloud-sql.root.password.uri` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties) to the Cloud Storage URI of the KMS-key encrypted root password of the Cloud SQL instance.
        4. Set the `dataproc:ranger.cloud-sql.use-private-ip` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties) to indicate whether the connection to the Cloud SQL instance is over private IP.

When using an external Cloud SQL instance, the Ranger component uses the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) to connect to the Cloud SQL instance. To use the proxy:

        1. Set the `sqlservice.admin` API scope when you create the cluster (see [Authorizing requests with OAuth 2.0](https://docs.cloud.google.com/sql/docs/mysql/admin-api#OAuth2Authorizing)). If using the `gcloud dataproc cluster create` command, add the `--scopes=default,sql-admin` parameter.
        2. Enable [the SQL Admin API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com) in your project.
        3. Make sure the cluster service account has the [Cloud SQL Editor](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles) role.
        4. Since the Cloud SQL Auth Proxy on the master node creates egress connections to the Cloud SQL instance over port **3307** , make sure that egress TCP connections from the master node to the Cloud SQL instance over port **3307** are allowed. For more information, see [How the Cloud SQL Auth Proxy works](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#how-works).

### Google Cloud console

     1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
     2. Click **Additional configuration** to expand that section.
     3. Edit **Optional components**.
     4. In the panel that opens, select the checkboxes for **Ranger** and **Solr** , then click **Save**.

### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Ranger component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.

When creating the cluster, use [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--enable-component-gateway` flag, as shown in the following example, to enable connecting to the Ranger Admin Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=SOLR,RANGER \
        --region=region \
        --enable-component-gateway \
        --properties="dataproc:ranger.kms.key.uri=projects/project-id/locations/global/keyRings/my-keyring/cryptoKeys/my-key,dataproc:ranger.admin.password.uri=gs://my-bucket/admin-password.encrypted" \
        ... other flags
    

### REST API

Specify the Ranger and Solr components in the [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) field as part of a Dataproc API [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. You must also set the following [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) in the [SoftwareConfig.Component.properties](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties) field:

     1. `dataproc:ranger.kms.key.uri`: "projects/project-id/locations/global/keyRings/my-keyring/cryptoKeys/my-key"
     2. `dataproc:ranger.admin.password.uri` : "gs://my-bucket/admin-password.encrypted"
Using the [Dataproc `v1` API](https://docs.cloud.google.com/managed-spark/docs/reference/rest#rest-resource:-v1.projects.regions.clusters), set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#EndpointConfig) property to `true` as part of the clusters.create request to enable connecting to the Jupyter notebook Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). 




Click the _Web interfaces_ tab. Under _Component gateway_ , click **Ranger** to open the Ranger web interface. Login with the Ranger admin username (for example, "admin") and password.

## Ranger Admin logs

Ranger `admin` logs are available in [Logging](https://console.cloud.google.com/logs) as `ranger-admin-root` logs.

![](https://docs.cloud.google.com/static/managed-spark/images/ranger-logs.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
