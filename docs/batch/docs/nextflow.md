---
url: https://docs.cloud.google.com/batch/docs/nextflow/
title: Orchestrate jobs by running Nextflow pipelines on Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:27.897604+00:00
---

# Orchestrate jobs by running Nextflow pipelines on Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/nextflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Orchestrate jobs by running Nextflow pipelines on Batch Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how to run a [Nextflow](https://www.nextflow.io/) pipeline on Batch. Specifically, this tutorial runs the [sample `rnaseq-nf` life sciences pipeline from Nextflow](https://github.com/nextflow-io/rnaseq-nf), which quantifies genomic features from short read data using [RNA-Seq](https://en.wikipedia.org/wiki/RNA-Seq).

This tutorial is intended for Batch users who want to use Nextflow with Batch.

Nextflow is open-source software for orchestrating bioinformatics workflows.

**Note** : This tutorial provides instructions for working with this app: Nextflowversion 23.04.1. The instructions might not represent newer versions of the app. For more information, see the documentation: [Nextflow](https://www.nextflow.io/docs/latest/overview.html). 

## Objectives

By completing this tutorial, you'll learn how to do the following:

  * Install Nextflow in Cloud Shell.
  * Create a Cloud Storage bucket.
  * Configure a Nextflow pipeline.
  * Run a sample pipeline using Nextflow on Batch.
  * View outputs of the pipeline.
  * Clean up to avoid incurring additional charges by doing one of the following: 
    * Delete a project.
    * Delete individual resources.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Batch
  * Cloud Storage



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

The resources created in this tutorial typically cost less than a dollar, assuming you complete all the steps—including the cleanup—in a timely manner.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Batch, Cloud Storage, Compute Engine, and Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com storage.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Batch, Cloud Storage, Compute Engine, and Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com storage.googleapis.com

  14. Make sure that your project has a Virtual Private Cloud (VPC) network with a valid networking configuration for this tutorial.

**Note:** No action is required for this step unless [your organization disables `default` network creation by enabling the `compute.skipDefaultNetworkCreation` policy constraint](https://docs.cloud.google.com/vpc/docs/vpc#org-policies) or your project has modified its `default` network. 

This tutorial assumes that you are using the [`default` network](https://docs.cloud.google.com/vpc/docs/vpc#default-network). By default, Google Cloud resources use the `default` network, which provides the network access required for this tutorial.

**Objective:** Optionally, if you want a Batch job for a Nextflow pipeline to use a different network, you can modify the `nextflow.config` file in this tutorial to also define the job's network and subnet by using the `google.batch.network` and `google.batch.subnetwork` Nextflow fields, respectively. However, you must also make sure that the network and subnet are correctly configured for your workload. For more information, see [Batch networking overview](https://docs.cloud.google.com/batch/docs/networking-overview). 

  15. Make sure that your project has at least one [service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with the permissions required for running the Batch job in this tutorial.

By default, jobs use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically granted the Editor (`roles/editor`) IAM role and already has all the permissions required for this tutorial.

**Note:** No action is required for this step unless [your organization disables automatic permissions for default service accounts by enabling the `iam.automaticIamGrantsForDefaultServiceAccounts` policy constraint](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#automatic-role-grants), your project has modified its Compute Engine default service account, or you want to use a different service account. 

To ensure that the job's service account has the necessary permissions to allow the Batch service agent to create and access resources for Batch jobs, ask your administrator to grant the following IAM roles to the job's service account: 

**Important:** You must grant these roles to the job's service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
     * [Batch Agent Reporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.agentReporter) (`roles/batch.agentReporter`) on the project
     * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project
     * (Recommended) Let jobs generate logs in Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the job's service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  16. Make sure that you have the permissions required for this tutorial.

**Note:** If you created the project that you plan to use for this tutorial, no action is required for this step. As the project creator, you are automatically granted the Owner (`roles/owner`) IAM role, which already has all the permissions required for this tutorial. 

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the job's service account
     * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the project

  17. Install Nextflow: 
         
         curl -s -L https://github.com/nextflow-io/nextflow/releases/download/v23.04.1/nextflow | bash
         

The output should be similar to the following:
         
         N E X T F L O W
         version 23.04.1 build 5866
         created 15-04-2023 06:51 UTC
         cite doi:10.1038/nbt.3820
         http://nextflow.io
         
         Nextflow installation completed. Please note:
         - the executable file `nextflow` has been created in the folder: ...
         - you may complete the installation by moving it to a directory in your $PATH
         




## Create a Cloud Storage bucket

To create a Cloud Storage bucket to store temporary work and output files from the Nextflow pipeline, use the Google Cloud console or the command-line.

### Console

To create a Cloud Storage bucket using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.

  3. On the **Create a bucket** page, enter a [globally unique name](https://docs.cloud.google.com/storage/docs/buckets#naming) for your bucket.

  4. Click **Create**.

  5. In the **Public access will be prevented** window, click **Confirm**.




### gcloud

To create a Cloud Storage bucket using the Google Cloud CLI, use the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
    
    
    gcloud storage buckets create gs://BUCKET_NAME
    

Replace `BUCKET_NAME` with a [globally unique name](https://docs.cloud.google.com/storage/docs/buckets#naming) for your bucket.

If the request is successful, the output should be similar to the following:
    
    
    Creating gs://BUCKET_NAME/...
       ```
    

## Configure Nextflow

To configure the Nextflow pipeline to run on Batch, follow these steps in the command-line:

  1. Clone the sample pipeline repository:
         
         git clone https://github.com/nextflow-io/rnaseq-nf.git
         

  2. Go to the `rnaseq-nf` folder:
         
         cd rnaseq-nf
         

  3. Open the `nextflow.config` file:
         
         nano nextflow.config
         

The file should contain the following `google-batch` section:
         
         'google-batch' {
             params.transcriptome = 'gs://rnaseq-nf/data/ggal/transcript.fa'
             params.reads = 'gs://rnaseq-nf/data/ggal/gut_{1,2}.fq'
             params.multiqc = 'gs://rnaseq-nf/multiqc'
             process.executor = 'google-batch'
             process.container = 'docker.io/nextflow/rnaseq-nf:v1.3.1'
             /*
              * replace with your own bucket!
              */
             workDir = 'gs://BUCKET_NAME/WORK_DIRECTORY'
             google.region  = 'REGION'
         }
         

  4. In the `google-batch` section, do the following:

     1. Replace `BUCKET_NAME` with the name of the Cloud Storage bucket you created in the previous steps.

     2. Replace `WORK_DIRECTORY` with the name for a new folder that the pipeline can use to store logs and outputs.

For example, enter `workDir`.

     3. Replace `REGION` with the region to use.

For example, enter `us-central1`.

     4. After the `google.region` field, add the following fields:

        1. Add the `google.project` field:
               
               google.project = 'PROJECT_ID'
               

Replace `PROJECT_ID` with the project ID of the current Google Cloud project.

        2. If you aren't using the Compute Engine default service account as the job's service account, add the `google.batch.serviceAccountEmail` field:
               
               google.batch.serviceAccountEmail = 'SERVICE_ACCOUNT_EMAIL'
               

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of the job's service account that you prepared for this tutorial.

**Objective:** To learn about all the fields that you can specify to configure the Batch job for a Nextflow pipeline, see the [Nextflow documentation for the Batch configuration scope](https://www.nextflow.io/docs/latest/google.html#google-batch).
  5. To save your edits, do the following:

     1. Press `Control+S`.

     2. Enter `Y`.

     3. Press `Enter`.




## Run the pipeline

Run the sample Nextflow pipeline using the command-line:
    
    
    ../nextflow run nextflow-io/rnaseq-nf -profile google-batch
    

The pipeline runs a small dataset using the settings you provided in the previous steps. This operation might take up to 10 minutes to complete.

After the pipeline finishes running, the output should be similar to the following:
    
    
    N E X T F L O W  ~  version 23.04.1
    Launching `https://github.com/nextflow-io/rnaseq-nf` [crazy_curry] DSL2 - revision: 88b8ef803a [master]
     R N A S E Q - N F   P I P E L I N E
     ===================================
     transcriptome: gs://rnaseq-nf/data/ggal/transcript.fa
     reads        : gs://rnaseq-nf/data/ggal/gut_{1,2}.fq
     outdir       : results
    
    Uploading local `bin` scripts folder to gs://example-bucket/workdir/tmp/53/2847f2b832456a88a8e4cd44eec00a/bin
    executor >  google-batch (4)
    [67/71b856] process > RNASEQ:INDEX (transcript)     [100%] 1 of 1 ✔
    [0c/2c79c6] process > RNASEQ:FASTQC (FASTQC on gut) [100%] 1 of 1 ✔
    [a9/571723] process > RNASEQ:QUANT (gut)            [100%] 1 of 1 ✔
    [9a/1f0dd4] process > MULTIQC                       [100%] 1 of 1 ✔
    
    Done! Open the following report in your browser --> results/multiqc_report.html
    
    Completed at: 20-Apr-2023 15:44:55
    Duration    : 10m 13s
    CPU hours   : (a few seconds)
    Succeeded   : 4
    

## View outputs of the pipeline

After the pipeline finishes running, it stores output files, logs, errors, or temporary files in the `results/qc_report.html` file within the `WORK_DIRECTORY` folder of your Cloud Storage bucket.

To check the pipeline's output files in the `WORK_DIRECTORY` folder of your Cloud Storage bucket, you can use the Google Cloud console or the command-line.

### Console

To check the pipeline's output files using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the **Name** column, click the name of the bucket you created in the previous steps.

  3. On the **Bucket details** page, open the `WORK_DIRECTORY` folder.




There is a folder for each separate tasks that the workflow run. Each folder contains the commands that were run, output files, and temporary files created by the pipeline.

### gcloud

To check the pipeline's output files using the gcloud CLI, use the [`gcloud storage ls` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls).
    
    
    gcloud storage ls gs://BUCKET_NAME/WORK_DIRECTORY
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket you created in the previous steps.

  * `WORK_DIRECTORY`: the directory you specified in the `nextflow.config` file.




The output lists a folder for each separate tasks that the pipeline run. Each folder contains the commands that were run, output files, and temporary files created by the pipeline.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the current project.

To delete the current project, use the Google Cloud console or the gcloud CLI.

### Console

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### gcloud

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

If you want to keep using the current project, then delete the individual resources used in this tutorial.

#### Delete the bucket

If you no longer need the bucket you used in this tutorial, then [delete the bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

#### Delete the output files in the bucket

After the pipeline finishes running, it creates and stores output files in the `WORK_DIRECTORY` folder of your Cloud Storage bucket.

To reduce Cloud Storage charges to the current current Google Cloud account, you can delete the folder containing the pipeline's output files by using the Google Cloud console or the command-line.

### Console

To delete the `WORK_DIRECTORY` folder, and all the output files, from your Cloud Storage bucket using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the **Name** column, click the name of the bucket you created in the previous steps.

  3. On the **Bucket details** page, select the row containing the `WORK_DIRECTORY` folder, and then do the following:

     1. Click **Delete**.

     2. To confirm, enter `DELETE`, and then click **Delete**.




### gcloud

To delete the `WORK_DIRECTORY` folder, and all the output files, from your Cloud Storage bucket using the gcloud CLI, use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) with the `--recursive` flag.
    
    
    gcloud storage rm gs://BUCKET_NAME/WORK_DIRECTORY \
          --recursive
    

Replace the following:

  * `BUCKET_NAME`: the name of the bucket you specified in the previous steps.

  * `WORK_DIRECTORY`: the directory to store the pipeline output files you specified in the previous steps.




## What's next

  * To learn more about deploying Nextflow workflows, see the [Nextflow GitHub repository](https://github.com/nextflow-io/nextflow).

  * To learn more about Nextflow processes, scripting, and configuration options, see the [Nextflow documentation](https://www.nextflow.io/docs/latest/index.html).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
