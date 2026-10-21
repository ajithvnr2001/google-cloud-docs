---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/gcs-connector-spark-tutorial/
title: Use the Cloud Storage connector with Apache Spark \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:41.014311+00:00
---

# Use the Cloud Storage connector with Apache Spark  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/gcs-connector-spark-tutorial/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use the Cloud Storage connector with Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial show you how to run example code that uses the [Cloud Storage connector](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage#clusters) with [Apache Spark](https://spark.apache.org "Apache Spark"). 

[Lightning Engine](https://cloud.google.com/products/lightning-engine?e=48754) enhances connectivity to Cloud Storage to optimize the performance of its native engine. The improved Cloud Storage connector minimizes metadata operations to reduce costs, while an optimized file output committer unlocks performance and reliability for Spark workloads. Complete the [Early Access](https://docs.google.com/forms/d/e/1FAIpQLSdkNW13znxnwskYuEgZ-BWLmyxbwg4aMnAU-Z2f3FGzYhHHmg/viewform?usp=header) form to request early access to this private preview feature. 

## Objectives

Write a simple wordcount Spark job in Java, Scala, or Python, then run the job on a Managed Service for Apache Spark cluster. All Managed Service for Apache Spark cluster image versions have the Spark components needed for this tutorial already installed.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine
  * Managed Service for Apache Spark
  * Cloud Storage



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Run the steps below to prepare to run the code in this tutorial.

  1. **Set up your project.** If necessary, set up a project with the Managed Service for Apache Spark, Compute Engine, and Cloud Storage APIs enabled and the Google Cloud CLI installed on your local machine. 

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     4. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com&redirect=https%3A//console.cloud.google.com)

     5. Create a service account: 

        1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
        3. Select your project. 
        4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

        5. Click **Create and continue**. 
        6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
        7. Click **Continue**. 
        8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

     6. Create a service account key: 

        1. In the Google Cloud console, click the email address for the service account that you created. 
        2. Click **Keys**. 
        3. Click **Add key** , and then click **Create new key**. 
        4. Click **Create**. A JSON key file is downloaded to your computer. 
        5. Click **Close**. 
     7. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
            
            export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
            
            export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
            
            $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
            
            $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
            
            set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

     8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

     11. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     13. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com&redirect=https%3A//console.cloud.google.com)

     14. Create a service account: 

        1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
        3. Select your project. 
        4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

        5. Click **Create and continue**. 
        6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
        7. Click **Continue**. 
        8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

     15. Create a service account key: 

        1. In the Google Cloud console, click the email address for the service account that you created. 
        2. Click **Keys**. 
        3. Click **Add key** , and then click **Create new key**. 
        4. Click **Create**. A JSON key file is downloaded to your computer. 
        5. Click **Close**. 
     16. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
            
            export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
            
            export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
            
            $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
            
            $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
            
            set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

     17. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     18. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     19. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

  2. **Create a Cloud Storage bucket.** You need a Cloud Storage to hold tutorial data. If you do not have one ready to use, create a new bucket in your project. 

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
        1. In the **Get started** section, do the following: 
           * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
           * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
        2. In the **Choose where to store your data** section, do the following: 
           1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
           2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
              * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
           3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

              1. In the **Bucket** menu, select a bucket.
              2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

                 * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
                 * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
                 * Click **Done**.

        3. In the **Choose how to store your data** section, do the following: 
           1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
           2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
        4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
        5. In the **Choose how to protect object data** section, do the following: 
           * Select any of the options under **Data protection** that you want to set for your bucket. 
             * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
             * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
             * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
               * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
               * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
           * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
     4. Click **Create**. 
  3. **Set local environment variables.** Set environment variables on your local machine. Set your Google Cloud project-id and the name of the Cloud Storage bucket you will use for this tutorial. Also provide the name and [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of an existing or new Managed Service for Apache Spark cluster. You can create a cluster to use in this tutorial in the next step. 
         
         PROJECT=project-id
         
         
         BUCKET_NAME=bucket-name
         
         
         CLUSTER=cluster-name
         
         
         REGION=cluster-region Example: "us-central1"
         

  4. **Create a Managed Service for Apache Spark cluster.** Run the command, below, to create a [single-node](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) Managed Service for Apache Spark cluster in the specified [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones). 
         
         gcloud dataproc clusters create ${CLUSTER} \
             --project=${PROJECT} \
             --region=${REGION} \
             --single-node
         

The above command installs the default [cluster image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions). You can use the [`--image-version`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--image) flag to select an image version for your cluster. Each image version installs specific versions of Spark and Scala library components. If you prepare the Spark wordcount job in Java or Scala, you will reference the Spark and Scala versions installed on your cluster when you prepare the job package.
  5. **Copy public data to your Cloud Storage bucket.** Copy a public data Shakespeare text snippet into the `input` folder of your Cloud Storage bucket: 
         
         gcloud storage cp gs://pub/shakespeare/rose.txt \
             gs://${BUCKET_NAME}/input/rose.txt
         

  6. **Set up a[Java (Apache Maven)](https://docs.cloud.google.com/java/docs/setup#install_a_build_automation_tool), [Scala (SBT)](https://www.scala-sbt.org/), or [Python](https://docs.cloud.google.com/python/docs/setup#installing_python) development environment.** **Use Cloud Shell**. [Cloud Shell](https://docs.cloud.google.com/shell/docs/features#tools) includes tools used in this tutorial, including Apache Maven, Python, and the Google Cloud CLI.




## Prepare the Spark wordcount job

Select a tab, below, to follow the steps to prepare a job package or file to submit to your cluster. You can prepare one of the following job types;

  * **[Spark job in Java](https://spark.apache.org/)** using [Apache Maven](https://maven.apache.org/) to build a [JAR](https://en.wikipedia.org/wiki/JAR) package
  * **[Spark job in Scala](https://www.scala-lang.org/)** using [SBT](https://www.scala-sbt.org/) to build a [JAR](https://en.wikipedia.org/wiki/JAR) package
  * **[Spark job in Python (PySpark)](https://archive.apache.org/dist/spark/docs/3.5.4/api/python/getting_started/index.html)**



### Java

  1. **Copy`pom.xml` file to your local machine.** The following `pom.xml` file specifies Scala and Spark library dependencies, which are given a `provided` scope to indicate that the Managed Service for Apache Spark cluster will provide these libraries at runtime. The `pom.xml` file does not specify a Cloud Storage dependency because the connector implements the standard HDFS interface. When a Spark job accesses Cloud Storage cluster files (files with URIs that start with `gs://`), the system automatically uses the Cloud Storage connector to access the files in Cloud Storage **Check your cluster image version.** Replace the version placeholders in the file to show the Spark and Scala library versions used by your cluster's [image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions). Note that the `spark-core_` artifact number is the Scala `major.minor` version number.
         
         <?xml version="1.0" encoding="UTF-8"?>
         <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
           <modelVersion>4.0.0</modelVersion>
         
           <groupId>dataproc.codelab</groupId>
           <artifactId>word-count</artifactId>
           <version>1.0</version>
         
           <properties>
             <maven.compiler.source>1.8</maven.compiler.source>
             <maven.compiler.target>1.8</maven.compiler.target>
           </properties>
         
           <dependencies>
             <dependency>
               <groupId>org.scala-lang</groupId>
               <artifactId>scala-library</artifactId>
               <version>Scala version, for example, 2.11.8</version>
               <scope>provided</scope>
             </dependency>
             <dependency>
               <groupId>org.apache.spark</groupId>
               <artifactId>spark-core_Scala major.minor.version, for example, 2.11</artifactId>
               <version>Spark version, for example, 2.3.1</version>
               <scope>provided</scope>
             </dependency>
           </dependencies>
         </project>

  2. **Copy the`WordCount.java` code listed, below, to your local machine.**
     1. Create a set of directories with the path `src/main/java/managed-spark/codelab`: 
            
            mkdir -p src/main/java/managed-spark/codelab
            

     2. Copy `WordCount.java` to your local machine into `src/main/java/managed-spark/codelab`: 
            
            cp WordCount.java src/main/java/managed-spark/codelab
            

`WordCount.java` is a Spark job in Java that reads text files from Cloud Storage, performs a word count, then writes the text file results to Cloud Storage.
    
    package dataproc.codelab;
    
    import java.util.Arrays;
    import org.apache.spark.SparkConf;
    import org.apache.spark.api.java.JavaPairRDD;
    import org.apache.spark.api.java.JavaRDD;
    import org.apache.spark.api.java.JavaSparkContext;
    import scala.Tuple2;
    
    public class WordCount {
      public static void main(String[] args) {
        if (args.length != 2) {
          throw new IllegalArgumentException("Exactly 2 arguments are required: <inputUri> <outputUri>");
        }
        String inputPath = args[0];
        String outputPath = args[1];
        JavaSparkContext sparkContext = new JavaSparkContext(new SparkConf().setAppName("Word Count"));
        JavaRDD<String> lines = sparkContext.textFile(inputPath);
        JavaRDD<String> words = lines.flatMap(
            (String line) -> Arrays.asList(line.split(" ")).iterator()
        );
        JavaPairRDD<String, Integer> wordCounts = words.mapToPair(
            (String word) -> new Tuple2<>(word, 1)
        ).reduceByKey(
            (Integer count1, Integer count2) -> count1 + count2
        );
        wordCounts.saveAsTextFile(outputPath);
      }
    }

  3. **Build the package.**
         
         mvn clean package
         

If the build is successful, a `target/word-count-1.0.jar` is created.
  4. **Stage the package to Cloud Storage.**
         
         gcloud storage cp target/word-count-1.0.jar \
             gs://${BUCKET_NAME}/java/word-count-1.0.jar
         




### Scala

  1. **Copy`build.sbt` file to your local machine.** The following `build.sbt` file specifies Scala and Spark library dependencies, which are given a `provided` scope to indicate that the Managed Service for Apache Spark cluster will provide these libraries at runtime. The `build.sbt` file does not specify a Cloud Storage dependency because the connector implements the standard HDFS interface. When a Spark job accesses Cloud Storage cluster files (files with URIs that start with `gs://`), the system automatically uses the Cloud Storage connector to access the files in Cloud Storage **Check your cluster image verison.** Replace the version placeholders in the file to show the Spark and Scala library versions used by your cluster's [image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions).
         
         scalaVersion := "Scala version, for example, 2.11.8"
         
         name := "word-count"
         organization := "dataproc.codelab"
         version := "1.0"
         
         libraryDependencies ++= Seq(
           "org.scala-lang" % "scala-library" % scalaVersion.value % "provided",
           "org.apache.spark" %% "spark-core" % "Spark version, for example, 2.3.1" % "provided"
         )

  2. **Copy`word-count.scala` to your local machine.** This is a Spark job in Java that reads text files from Cloud Storage, performs a word count, then writes the text file results to Cloud Storage. 
         
         package dataproc.codelab
         
         import org.apache.spark.SparkContext
         import org.apache.spark.SparkConf
         
         object WordCount {
           def main(args: Array[String]) {
             if (args.length != 2) {
               throw new IllegalArgumentException(
                   "Exactly 2 arguments are required: <inputPath> <outputPath>")
             }
         
             val inputPath = args(0)
             val outputPath = args(1)
         
             val sc = new SparkContext(new SparkConf().setAppName("Word Count"))
             val lines = sc.textFile(inputPath)
             val words = lines.flatMap(line => line.split(" "))
             val wordCounts = words.map(word => (word, 1)).reduceByKey(_ + _)
             wordCounts.saveAsTextFile(outputPath)
           }
         }

  3. **Build the package.**
         
         sbt clean package
         

If the build is successful, a `target/scala-2.11/word-count_2.11-1.0.jar` is created.
  4. **Stage the package to Cloud Storage.**
         
         gcloud storage cp target/scala-2.11/word-count_2.11-1.0.jar \
             gs://${BUCKET_NAME}/scala/word-count_2.11-1.0.jar
         




### Python

  1. **Copy`word-count.py` to your local machine.** This is a Spark job in Python using PySpark that reads text files from Cloud Storage, performs a word count, then writes the text file results to Cloud Storage. 
         
         #!/usr/bin/env python
         
         import pyspark
         import sys
         
         if len(sys.argv) != 3:
           raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")
         
         inputUri=sys.argv[1]
         outputUri=sys.argv[2]
         
         sc = pyspark.SparkContext()
         lines = sc.textFile(sys.argv[1])
         words = lines.flatMap(lambda line: line.split())
         wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1 + count2)
         wordCounts.saveAsTextFile(sys.argv[2])




## Submit the job

Run the following `gcloud` command to submit the wordcount job to your Managed Service for Apache Spark cluster.

### Java
    
    
    gcloud dataproc jobs submit spark \
        --cluster=${CLUSTER} \
        --class=dataproc.codelab.WordCount \
        --jars=gs://${BUCKET_NAME}/java/word-count-1.0.jar \
        --region=${REGION} \
        -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
    

### Scala
    
    
    gcloud dataproc jobs submit spark \
        --cluster=${CLUSTER} \
        --class=dataproc.codelab.WordCount \
        --jars=gs://${BUCKET_NAME}/scala/word-count_2.11-1.0.jar \
        --region=${REGION} \
        -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
    

### Python
    
    
    gcloud dataproc jobs submit pyspark word-count.py \
        --cluster=${CLUSTER} \
        --region=${REGION} \
        -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
    

## View the output

After the job finishes, run the following gcloud CLI command to view the wordcount output.
    
    
    gcloud storage cat gs://${BUCKET_NAME}/output/*
    

The wordcount output should be similar to the following: 
    
    
    (a,2)
    (call,1)
    (What's,1)
    (sweet.,1)
    (we,1)
    (as,1)
    (name?,1)
    (any,1)
    (other,1)
    (rose,1)
    (smell,1)
    (name,1)
    (would,1)
    (in,1)
    (which,1)
    (That,1)
    (By,1)
    

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Managed Service for Apache Spark cluster

Instead of deleting your project, you might want to only [delete your cluster](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#deleting_a_cluster) within the project.

### Delete the Cloud Storage bucket

### Google Cloud console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 



### Command line

Delete the bucket: 
    
    gcloud storage buckets delete BUCKET_NAME

**Important:** Your bucket must be empty before you can delete it.


## What's next

  * See [Spark job tuning tips](https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
