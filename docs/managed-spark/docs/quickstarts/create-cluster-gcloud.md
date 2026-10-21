---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud/
title: Create a cluster by using the gcloud CLI \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:46.666709+00:00
---

# Create a cluster by using the gcloud CLI  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a cluster by using the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use the Google Cloud CLI [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc) command-line tool to create a Managed Service for Apache Spark cluster, run a [Apache Spark](http://spark.apache.org/) job in the cluster, then modify the number of workers in the cluster.

You can find out how to do the same or similar tasks with [Quickstarts Using the API Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template), the Google Cloud console in [Create a cluster by using the Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console), and using the client libraries in [Create a cluster by using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. Verify that you have the permissions required to complete this guide. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Dataproc API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataproc.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. Verify that you have the permissions required to complete this guide. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Dataproc API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataproc.googleapis.com




### Required roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the following IAM roles to the Compute Engine default service account on the project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * All: [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) 



## Create a cluster

To create a cluster called `example-cluster`, run the following [`gcloud Managed Service for Apache Spark clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command.

A convenient way to run the `gcloud` command-line tool is from [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which has the Google Cloud CLI pre-installed. Cloud Shell is free for Google Cloud customers. To use Cloud Shell, you need a Google Cloud project.
    
    
    gcloud dataproc clusters create example-cluster --region=REGION
    

Replace the following:

REGION: Specify a [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) where the cluster will be located.

## Submit a job

To submit a sample Spark job that calculates a rough value for `pi`, run the following [gcloud Managed Service for Apache Spark jobs submit spark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark) command:
    
    
    gcloud dataproc jobs submit spark --cluster example-cluster \
        --region=REGION \
        --class org.apache.spark.examples.SparkPi \
        --jars file:///usr/lib/spark/examples/jars/spark-examples.jar -- 1000
    

Notes:

Replace the following:

REGION: Specify the cluster region.

  * The job runs on the `example-cluster`.
  * The `class` contains the main method for the SparkPi, which calculates an approximate value of `pi` application.
  * The jar file contains the job code. Note: `file:///usr/lib/spark/examples/jars/spark-examples.jar` is a sample jar pre-installed on the cluster. For custom jobs, specify your jar file in Cloud Storage (see [Submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job)).

**Caution:** Don't copy custom JAR files directly into cluster system directories such as `/usr/lib/spark/jars/`. Placing custom JARs in system directories pollutes the Managed Service for Apache Spark agent classpath and can cause job cancellation failures and orphaned YARN applications.
  * `1000` is a job parameter. It specifies the number of tasks (iterations) the job performs to calculate the value of `pi`.


Parameters passed to the job must follow a double dash (`--`). For more information, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark). 

The job's running and final output is displayed in the terminal window:
    
    
    Waiting for job output...
    ...
    Pi is roughly 3.14118528
    ...
    Job finished successfully.
    

## Update a cluster

To change the number of workers in the cluster to five, run the following command:
    
    
    gcloud dataproc clusters update example-cluster \
        --region=REGION \
        --num-workers 5
    

The command output displays cluster details:
    
    
    workerConfig:
    ...
      instanceNames:
      -   example-cluster-w-0
      -   example-cluster-w-1
      -   example-cluster-w-2
      -   example-cluster-w-3
      -   example-cluster-w-4
      numInstances: 5
    statusHistory:
    ...
    -   detail: Add 3 workers.
    

To decrease the number of worker nodes to the original value of `2`, run the following command:
    
    
    gcloud dataproc clusters update example-cluster \
        --region=REGION \
        --num-workers 2
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

  1. To delete the `example-cluster`, run the [`clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/delete) command: 
         
         gcloud dataproc clusters delete example-cluster \
             --region=REGION
         




## What's next

  * Learn how to [write and run a Spark Scala job](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-scala).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
