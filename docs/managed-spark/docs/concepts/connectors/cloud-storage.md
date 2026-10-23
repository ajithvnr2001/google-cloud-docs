---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage/
title: Cloud Storage connector \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:01.653816+00:00
---

# Cloud Storage connector  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cloud Storage connector Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage connector [open source Java library](https://github.com/GoogleCloudDataproc/hadoop-connectors/tree/master/gcs) lets you run [Apache Hadoop](https://hadoop.apache.org) or [Apache Spark](https://spark.apache.org) jobs directly on data in Cloud Storage.

[Lightning Engine](https://cloud.google.com/products/lightning-engine?e=48754) enhances connectivity to Cloud Storage to optimize the performance of its native engine. The improved Cloud Storage connector minimizes metadata operations to reduce costs, while an optimized file output committer unlocks performance and reliability for Spark workloads. Complete the [Early Access](https://docs.google.com/forms/d/e/1FAIpQLSdkNW13znxnwskYuEgZ-BWLmyxbwg4aMnAU-Z2f3FGzYhHHmg/viewform?usp=header) form to request early access to this private preview feature.

## Benefits of the Cloud Storage connector

  * **Direct data access:** Store your data in Cloud Storage and access it directly. You don't need to transfer it into HDFS first.
  * **HDFS compatibility:** You can access your data in Cloud Storage using the `gs://` prefix instead of `hdfs://`.
  * **Interoperability:** Storing data in Cloud Storage enables seamless interoperability between Spark, Hadoop, and Google services.
  * **Data accessibility:** When you shut down a Hadoop cluster, unlike HDFS, you continue to have access to your data in Cloud Storage.
  * **High data availability:** Data stored in Cloud Storage is highly available and globally replicated without a loss of performance.
  * **No storage management overhead:** Unlike HDFS, Cloud Storage requires no routine maintenance, such as checking the file system, or upgrading or rolling back to a previous version of the file system.
  * **Quick startup:** In HDFS, a MapReduce job can't start until the `NameNode` is out of safe mode, a process that can take from a few seconds to many minutes depending on the size and state of your data. With Cloud Storage, you can start your job as soon as the task nodes start, which leads to significant cost savings over time.



## Connector setup on Managed Service for Apache Spark clusters

The Cloud Storage connector is installed by default on all Managed Service for Apache Spark cluster nodes in the `/usr/local/share/google/managed-spark/lib/` directory. The following subsections describe steps you can take to complete connector setup on Managed Service for Apache Spark clusters.

**Note:** To set up the connector on other clusters, see Non-Managed Service for Apache Spark clusters.

### VM service account

When running the connector on Managed Service for Apache Spark cluster nodes and other Compute Engine VMs, the `google.cloud.auth.service.account.enable` property is set to `false` by default, which means you don't need to configure the [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) credentials for the connector—VM service account credentials are provided by the [VM metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview).

The Managed Service for Apache Spark [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) must have permission to access your Cloud Storage bucket.

**If you use a custom service account with a`2.2`\+ Spark job cluster**: If you select a [custom service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account) when creating a Managed Service for Apache Spark `2.2`\+ image version cluster that you submit Spark jobs to, and if your Spark jobs read from or write to Cloud Storage, to avoid permission problems that can cause job failures, add the following configuration (**shown in bold**) to your Spark session creation code:
    
    
    spark = SparkSession.builder \
    .appName(appName) \
    **.config("fs.gs.auth.type", "SERVICE_ACCOUNT_JSON_KEYFILE")** \
    **.config("fs.gs.auth.service.account.json.keyfile", " path/to/your/keyfile.json")** \
    .getOrCreate()
    

To verify that permission are set correctly, check to make sure that the custom service account has the `storage.objects.get` and `storage.objects.create` permissions:

  1. [View current access](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access) to list the roles granted to the custom service account.
  2. [Find a role or permission](https://docs.cloud.google.com/iam/docs/roles-permissions#find-role-or-permission) to lookup the permissions associated with a role.



### User-selected connector versions

The default Cloud Storage connector versions used in the latest images installed on Managed Service for Apache Spark clusters are listed in the [image version pages](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions). If your application depends on a non-default connector version deployed on your cluster, you can perform one of the following actions to use your selected connector version:

  * Create a cluster with the `--metadata=GCS_CONNECTOR_VERSION=x.y.z` flag, which updates the connector used by applications running on the cluster to the specified connector version.
  * Include and [relocate](https://maven.apache.org/plugins/maven-shade-plugin/examples/class-relocation.html) the connector classes and connector dependencies for the version you are using into your application's jar. Relocation is necessary to avoid a conflict between the your deployed connector version and the default connector version installed on the Managed Service for Apache Spark cluster. Also see the [Maven dependencies relocation example](https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/a839bd8f237197f98808944ca52d03de96518314/gcs/pom.xml#L242-L300).



## Connector setup on non-Managed Service for Apache Spark clusters

You can take the following steps to setup the Cloud Storage connector on a non-Managed Service for Apache Spark cluster, such as an Apache Hadoop or Spark cluster that you use to move on-premises HDFS data to Cloud Storage.

  1. Download the connector.

     * To download the Cloud Storage connector: 
       * To use a `latest` version located in Cloud Storage bucket (using a `latest` version is not recommended for production applications): 
         * [Cloud Storage connector for Hadoop 1.x](https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop1-latest.jar)
         * [Cloud Storage connector for Hadoop 2.x](https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop2-latest.jar)
         * [Cloud Storage connector for Hadoop 3.x](https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar)
       * To use a [specific version](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases) from your Cloud Storage bucket by substituting the Hadoop and Cloud Storage connector versions in the `gcs-connector-HADOOP_VERSION-CONNECTOR_VERSION.jar` name pattern, for example, `gs://hadoop-lib/gcs/gcs-connector-hadoop2-2.1.1.jar`.
       * To use a [specific version](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases) from the [Apache Maven repository](https://repo1.maven.org/maven2/com/google/cloud/bigdataoss/gcs-connector/), download a shaded jar that has `-shaded` suffix in the name.
  2. Install the connector.

Follow the [GitHub instructions](https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/master/gcs/INSTALL.md) to install, configure, and test the Cloud Storage connector.




## Connector usage

You can use the connector to access Cloud Storage data in the following ways:

  * In a Spark, PySpark, or Hadoop application with the `gs://` prefix
  * In a hadoop shell with `hadoop fs -ls gs://bucket/dir/file`
  * In the Cloud Storage [Browser](https://docs.cloud.google.com/storage/docs/gettingstarted-console) In the Google Cloud console
  * Using [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs) commands, such as: 
    * [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp)
    * [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync)



### Java usage

The Cloud Storage connector requires Java 8.

The following is a sample Maven POM dependency management section for the Cloud Storage connector. For additional information, see [Dependency Management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Management).
    
    
    <dependency>
        <groupId>com.google.cloud.bigdataoss</groupId>
        <artifactId>gcs-connector</artifactId>
        <version>hadoopX-X.X.X[CONNECTOR VERSION](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/)</version>
        <scope>provided</scope>
    </dependency>
    

For a shaded version: 
    
    
    <dependency>
        <groupId>com.google.cloud.bigdataoss</groupId>
        <artifactId>gcs-connector</artifactId>
        <version>hadoopX-X.X.X[CONNECTOR VERSION](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/)</version>
        <scope>provided</scope>
        <classifier>shaded</classifier>
    </dependency>
    

## Connector support

The Cloud Storage connector is supported by Google Cloud for use with Google Cloud products and use cases. When used with Managed Service for Apache Spark, it is supported at the same level as Managed Service for Apache Spark. For more information, see [Get support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support).

## Connect to Cloud Storage using gRPC

By default, the Cloud Storage connector on Managed Service for Apache Spark uses the [Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api). This section shows you how to enable the Cloud Storage connector to use [gRPC](https://grpc.io/).

### Usage considerations

Using the Cloud Storage connector with gRPC includes the following considerations:

  * **Regional bucket location:** The gRPC can improve read latencies only when Compute Engine VMs and Cloud Storage buckets are located in the same [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * **Read-intensive jobs:** gRPC can offer improved read latencies for long-running reads, and can help read-intensive workloads. It is not recommended for applications that create a gRPC channel, run a short computation, and then close the channel.
  * **Unauthenticated requests:** The gRPC does not support unauthenticated requests.



### Requirements

The following requirements apply when using gRPC with the Cloud Storage connector:

  * Your Managed Service for Apache Spark cluster [VPC network](https://docs.cloud.google.com/vpc/docs/overview) must support [direct connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#direct-connectivity). This means that the network's [routes](https://docs.cloud.google.com/vpc/docs/routes) and [firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) must allow egress traffic to reach `34.126.0.0/18` and `2001:4860:8040::/42`.

    * If your Managed Service for Apache Spark cluster uses IPv6 networking, you must set up an IPv6 subnet for VM instances. For more information, see [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).
  * When [creating a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster), you must use Cloud Storage connector version `2.2.23` or later with image version `2.1.56+` or Cloud Storage connector version v3.0.0 or later with image version 2.2.0+. The Cloud Storage connector version installed on each Managed Service for Apache Spark image version is listed in the [Managed Service for Apache Spark image version pages](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions).

    * If you create and use a [Managed Service for Apache Spark on GKE virtual cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/gke-quickstart-create-cluster#create_a_virtual_cluster) for your gRPC Cloud Storage requests, GKE version `1.28.5-gke.1199000` with `gke-metadata-server 0.4.285` is recommended. This combination supports direct connectivity.
  * You or your organization administrator must grant Identity and Access Management roles that include the permissions necessary to set up and make gRPC requests to the Cloud Storage connector. These roles can include the following:

    * User role: [Dataproc Editor](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc.editor) role granted to users to allow them to create clusters and submit jobs
    * Service account role: [Storage Object User](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) role granted to the Managed Service for Apache Spark [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) to allow applications running on cluster VMs to view, read, create, and write Cloud Storage objects.



### Enable gRPC on the Cloud Storage connector

You can enable gRPC on the Cloud Storage connector at the cluster or job level. Once enabled on the cluster, Cloud Storage conector read requests use gRPC. If enabled on a job instead of at the cluster level, Cloud Storage connector read requests use gRPC for the job only.

### Enable a cluster

To enable gRPC on the Cloud Storage connector at the cluster level, set the `core:fs.gs.client.type=STORAGE_CLIENT` property when you [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster). Once gRPC is enabled at the cluster level, Cloud Storage connector **read** requests made by jobs running on the cluster use gRPC.

gcloud CLI example:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --properties=core:fs.gs.client.type=STORAGE_CLIENT
    

Replace the following;

  * CLUSTER_NAME: Specify a name for your cluster.
  * PROJECT_NAME: The project ID of the project where the cluster is located. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
  * REGION: Specify a [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located.



### Enable a job

To enable gRPC on the Cloud Storage connector for a specific job, include `--properties=spark.hadoop.fs.gs.client.type=STORAGE_CLIENT` when you [submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#dataproc-submit-job-gcloud).

Example: Run a job on an existing cluster that uses gRPC to read from Cloud Storage.

  1. Create a local `/tmp/line-count.py` PySpark script that uses gRPC to read a Cloud Storage text file and output the number of lines in the file.
         
         cat <<EOF >"/tmp/line-count.py"
         #!/usr/bin/python
         import sys
         from pyspark.sql import SparkSession
         path = sys.argv[1]
         spark = SparkSession.builder.getOrCreate()
         rdd = spark.read.text(path)
         lines_counter = rdd.count()
         print("There are {} lines in file: {}".format(lines_counter,path))
         EOF
         

  2. Create a local `/tmp/line-count-sample.txt` text file.
         
         cat <<EOF >"/tmp/line-count-sample.txt"
         Line 1
         Line 2
         line 3
         EOF
         

  3. Upload local `/tmp/line-count.py` and `/tmp/line-count-sample.txt` to your bucket in Cloud Storage.
         
         gcloud storage cp /tmp/line-count* gs://BUCKET
         

  4. Run the `line-count.py` job on your cluster. Set `--properties=spark.hadoop.fs.gs.client.type=STORAGE_CLIENT` to enable gRPC for Cloud Storage connector read requests.
         
         gcloud dataproc jobs submit pyspark gs://BUCKET/line-count.py \
         --cluster=CLUSTER_NAME \
         --project=PROJECT_ID  \
         --region=REGION \
         --properties=spark.hadoop.fs.gs.client.type=STORAGE_CLIENT \
         -- gs://BUCKET/line-count-sample.txt
         

Replace the following;

     * CLUSTER_NAME: The name of an existing cluster.
     * PROJECT_NAME: Your project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
     * REGION: The Compute Engine region where the cluster is located.
     * BUCKET: Your Cloud Storage bucket.



### Generate gRPC client-side metrics

You can configure the Cloud Storage connector to generate gRPC related metrics in Cloud Monitoring. The gRPC related metrics can help you to do the following:

  * Monitor and optimize the performance of gRPC requests to Cloud Storage
  * Troubleshoot and debug issues
  * Gain insights into application usage and behavior



For information about how to configure the Cloud Storage connector to generate gRPC related metrics, see [Use gRPC client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics).

## Resources

  * See GitHub Cloud Storage connector [configuration properties](https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/master/gcs/CONFIGURATION.md#configuration-properties).
  * See [Connect to Cloud Storage using gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api) to use the Cloud Storage connector with client libraries, VPC Service Controls, and other scenarios.
  * Learn more about [Cloud Storage](https://docs.cloud.google.com/storage/docs).
  * See [Use the Cloud Storage connector with Apache Spark](https://docs.cloud.google.com/managed-spark/docs/tutorials/gcs-connector-spark-tutorial).
  * Understand the [Apache Hadoop file system ](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/filesystem/filesystem.html).
  * View the [Javadoc reference](http://www.javadoc.io/doc/com.google.cloud.bigdataoss/gcs-connector/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
