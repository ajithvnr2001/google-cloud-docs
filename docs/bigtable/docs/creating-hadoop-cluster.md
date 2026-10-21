---
url: https://docs.cloud.google.com/bigtable/docs/creating-hadoop-cluster/
title: Create a Hadoop cluster \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:19.138463+00:00
---

# Create a Hadoop cluster  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/creating-hadoop-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Hadoop cluster

You can use [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) to create one or more [Compute Engine instances](https://docs.cloud.google.com/compute) that can connect to a Bigtable instance and run [Hadoop jobs](https://docs.cloud.google.com/hadoop). This page explains how to use Managed Service for Apache Spark to automate the following tasks:

  * Installing Hadoop and the HBase client for Java
  * Configuring Hadoop and Bigtable
  * Setting the correct authorization scopes for Bigtable



After you create your Managed Service for Apache Spark cluster, you can use the cluster to run Hadoop jobs that read and write data to and from Bigtable.

This page assumes that you are already familiar with Hadoop. For additional information about Managed Service for Apache Spark, see the [Managed Service for Apache Spark documentation](https://docs.cloud.google.com/dataproc/docs).

## Before you begin

Before you begin, you'll need to complete the following tasks:

  * [Create a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-cluster). Be sure to note the project ID and Bigtable instance ID.
  * Enable the Cloud Bigtable API, Cloud Bigtable Admin API, Managed Service for Apache Spark, and Cloud Storage JSON APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigtable.googleapis.com,bigtableadmin.googleapis.com,dataproc.googleapis.com,storage-api.googleapis.com)

  * Verify that your user account is in a role that includes the permission [`storage.objects.get`](https://docs.cloud.google.com/storage/docs/access-control/iam-json). 

Open the IAM page in the Google Cloud console.

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  * Install the Google Cloud CLI. See the [gcloud CLI setup instructions](https://docs.cloud.google.com/sdk/docs) for details.
  * Install [Apache Maven](https://maven.apache.org/), which is used to run a sample Hadoop job.

On Debian GNU/Linux or Ubuntu, run the following command:
        
        sudo apt-get install maven

On RedHat Enterprise Linux or CentOS, run the following command:
        
        sudo yum install maven

On macOS, install [Homebrew](http://brew.sh/), then run the following command:
        
        brew install maven

  * Clone the GitHub repository [GoogleCloudPlatform/cloud-bigtable-examples](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/), which contains an example of a Hadoop job that uses Bigtable: 
        
        git clone https://github.com/GoogleCloudPlatform/cloud-bigtable-examples.git




## Create a Cloud Storage bucket

Managed Service for Apache Spark uses a [Cloud Storage](https://docs.cloud.google.com/storage) bucket to store temporary files. To prevent file-naming conflicts, create a new bucket for Managed Service for Apache Spark.

Cloud Storage bucket names must be globally unique across all buckets. Choose a bucket name that is likely to be available, such as a name that incorporates your Google Cloud project's name.

After you choose a name, use the following command to create a new bucket, replacing values in brackets with the appropriate values:
    
    
    gcloud storage buckets create gs://[BUCKET_NAME] --project=[PROJECT_ID]
    

## Create the Managed Service for Apache Spark cluster

Run the following command to create a Managed Service for Apache Spark cluster with four worker nodes, replacing values in brackets with the appropriate values:
    
    
    gcloud dataproc clusters create [DATAPROC_CLUSTER_NAME] --bucket [BUCKET_NAME] \
        --region [region] --num-workers 4 --master-machine-type n1-standard-4 \
        --worker-machine-type n1-standard-4
    

See the [`gcloud dataproc clusters create` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) for additional settings that you can configure. If you get an error message that includes the text `Insufficient 'CPUS' quota`, try setting the `--num-workers` flag to a lower value.

## Test the Managed Service for Apache Spark cluster

After you set up your Managed Service for Apache Spark cluster, you can test the cluster by running a [sample Hadoop job](https://docs.cloud.google.com/bigtable/docs/samples-map-reduce) that counts the number of times a word appears in a text file. The sample job uses Bigtable to store the results of the operation. You can use this sample job as a reference when you set up your own Hadoop jobs.

### Run the sample Hadoop job

  1. In the directory where you cloned the GitHub repository, change to the directory `java/dataproc-wordcount`.
  2. Run the following command to build the project, replacing values in brackets with the appropriate values:
         
         mvn clean package -Dbigtable.projectID=[PROJECT_ID] \
             -Dbigtable.instanceID=[BIGTABLE_INSTANCE_ID]
         

  3. Run the following command to start the Hadoop job, replacing values in brackets with the appropriate values:
         
         ./cluster.sh start [DATAPROC_CLUSTER_NAME]
         




When the job is complete, it displays the name of the output table, which is the word `WordCount` followed by a hyphen and a unique number:
    
    
    Output table is: WordCount-1234567890

### Verify the results of the Hadoop job

Optionally, after you run the Hadoop job, you can use the [ `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-overview) to verify that the job ran successfully:

  1. Open a terminal window in Cloud Shell.

[Open in Cloud Shell](https://docs.cloud.google.com/console?cloudshell=true)

  2. Install the `cbt` CLI : 
         
         gcloud components update
             gcloud components install cbt

  3. Scan the output table to view the results of the Hadoop job, replacing `[TABLE_NAME]` with the name of your output table: 
         
         cbt -instance [BIGTABLE_INSTANCE_ID] read [TABLE_NAME]
           




Now that you've verified that the cluster is set up correctly, you can use it to run your own Hadoop jobs.

## Delete the Managed Service for Apache Spark cluster

When you are done using the Managed Service for Apache Spark cluster, run the following command to shut down and delete the cluster, replacing `[DATAPROC_CLUSTER_NAME]` with the name of your Managed Service for Apache Spark cluster:
    
    
    gcloud dataproc clusters delete [DATAPROC_CLUSTER_NAME]
    

## What's next

  * Learn more about [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc).
  * Get started with the [HBase client for Java](https://docs.cloud.google.com/bigtable/docs/reference/libraries#client-libraries-usage-hbase-java).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
