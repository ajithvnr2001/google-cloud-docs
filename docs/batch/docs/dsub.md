---
url: https://docs.cloud.google.com/batch/docs/dsub/
title: Orchestrate jobs by running dsub pipelines on Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:29.773045+00:00
---

# Orchestrate jobs by running dsub pipelines on Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/dsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Orchestrate jobs by running dsub pipelines on Batch Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how to run a [`dsub`](https://github.com/databiosphere/dsub) pipeline on Batch. Specifically, the example `dsub` pipeline processes DNA sequencing data in a [Binary Alignment Map (BAM) file](https://en.wikipedia.org/wiki/Binary_Alignment_Map) to create a BAM index (BAI) file.

This tutorial is intended for Batch users who want to use `dsub` with Batch. `dsub` is an open source job scheduler for orchestrating batch-processing workflows on Google Cloud. To learn more about how to use Batch with `dsub`, see the [`dsub` documentation for Batch](https://github.com/DataBiosphere/dsub/blob/google-batch/docs/batch/README.md).

## Objectives

  * Run a `dsub` pipeline on Batch that reads and writes files in Cloud Storage buckets.
  * View the output files in a Cloud Storage bucket.



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

  14. Make sure that your project has at least one [service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with the permissions required for this tutorial.

**Note:** If you are using a new project, this step is not required [unless your organization prevents automatic role grants for default service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#automatic-role-grants). By default, the Compute Engine default service account is automatically granted the Editor (`roles/editor`) IAM role, which already has all the permissions required for this tutorial. 

Each job requires a service account that allows the Batch service agent to create and access the resources required to run the job. For this tutorial, the job's service account is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

To ensure that the Compute Engine default service account has the necessary permissions to allow the Batch service agent to create and access resources for Batch jobs, ask your administrator to grant the following IAM roles to the Compute Engine default service account: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
     * [Batch Agent Reporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.agentReporter) (`roles/batch.agentReporter`) on the project
     * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project
     * (Recommended) Let jobs generate logs in Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  15. Make sure that you have the permissions required for this tutorial.

**Note:** If you created this project, this step is not required. As the project creator, you are automatically granted the Owner (`roles/owner`) IAM role, which already has all the permissions required for this tutorial. 

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the job's service account, which for this tutorial is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the project

  16. Install `dsub` and its dependencies. For more information, see the [`dsub` installation documentation](https://github.com/databiosphere/dsub#getting-started).

     1. Make sure you have installed versions of [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/) that are supported by the latest version of `dsub`. To view the currently installed versions, run the following command:
            
            pip --version
            

If you need to install or update `pip` or Python, follow the [steps for installing Python](https://docs.cloud.google.com/python/docs/setup#installing_python).

     2. Recommended: To prevent dependency-conflict errors when installing `dsub`, create and activate a [Python virtual environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv):
            
            python -m venv dsub_libs && source dsub_libs/bin/activate
            

     3. Clone the `dsub` GitHub repository using [`git`](https://github.com/git-guides/install-git) and open it:
            
            git clone https://github.com/databiosphere/dsub.git && cd dsub
            

     4. Install `dsub` and its dependencies:
            
            python -m pip install .
            

The output is similar to the following:
            
            ...
            Successfully installed cachetools-5.3.1 certifi-2023.7.22 charset-normalizer-3.3.1 dsub-0.4.9 funcsigs-1.0.2 google-api-core-2.11.0 google-api-python-client-2.85.0 google-auth-2.17.3 google-auth-httplib2-0.1.0 google-cloud-batch-0.10.0 googleapis-common-protos-1.61.0 grpcio-1.59.0 grpcio-status-1.59.0 httplib2-0.22.0 idna-3.4 mock-4.0.3 parameterized-0.8.1 proto-plus-1.22.3 protobuf-4.24.4 pyasn1-0.4.8 pyasn1-modules-0.2.8 pyparsing-3.1.1 python-dateutil-2.8.2 pytz-2023.3 pyyaml-6.0 requests-2.31.0 rsa-4.9 six-1.16.0 tabulate-0.9.0 tenacity-8.2.2 uritemplate-4.1.1 urllib3-2.0.7
            




## Create a Cloud Storage bucket

To create a Cloud Storage bucket for storing the output files from the sample `dsub` pipeline using the gcloud CLI, run the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create):
    
    
    gcloud storage buckets create gs://BUCKET_NAME \
        --project PROJECT_ID
    

Replace the following:

  * `BUCKET_NAME`: a [globally unique name](https://docs.cloud.google.com/storage/docs/buckets#naming) for your bucket.

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.




The output is similar to the following:
    
    
    Creating gs://BUCKET_NAME/...
    

## Run the `dsub` pipeline

The sample `dsub` pipeline indexes a BAM file from the [1,000 Genomes Project](https://www.internationalgenome.org/) and outputs the results to a Cloud Storage bucket.

To run the sample `dsub` pipeline, run the following `dsub` command:
    
    
    dsub \
        --provider google-batch \
        --project PROJECT_ID \
        --logging gs://BUCKET_NAME/WORK_DIRECTORY/logs \
        --input BAM=gs://genomics-public-data/1000-genomes/bam/HG00114.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam \
        --output BAI=gs://BUCKET_NAME/WORK_DIRECTORY/HG00114.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam.bai \
        --image quay.io/cancercollaboratory/dockstore-tool-samtools-index \
        --command 'samtools index ${BAM} ${BAI}' \
        --wait
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.

  * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created.

  * `WORK_DIRECTORY`: the name for a new directory that the pipeline can use to store logs and outputs. For example, enter `workDir`.




The `dsub` pipeline runs a Batch job that writes the BAI file and logs to specified directory in your Cloud Storage bucket. Specifically, the `dsub` repository contains a prebuilt Docker image that uses [`samtools`](http://www.htslib.org/) to index the BAM file that you specified in the `--input` flag.

The command doesn't finish until the `dsub` pipeline finishes running, which might vary based on when the Batch job is scheduled. Usually, this takes about 10 minutes: Batch usually starts running the job within a few minutes, and the job's runtime is about 8 minutes.

At first, the command is still running and the output is similar to the following:
    
    
    Job properties:
      job-id: JOB_NAME
      job-name: samtools
      user-id: USERNAME
    Provider internal-id (operation): projects/PROJECT_ID/locations/us-central1/jobs/JOB_NAME
    Launched job-id: JOB_NAME
    To check the status, run:
      dstat --provider google-batch --project PROJECT_ID --location us-central1 --jobs 'JOB_NAME' --users 'USERNAME' --status '*'
    To cancel the job, run:
      ddel --provider google-batch --project PROJECT_ID --location us-central1 --jobs 'JOB_NAME' --users 'USERNAME'
    Waiting for job to complete...
    Waiting for: JOB_NAME.
    

Then, after the job has successfully finished, the command ends and the output is similar to the following:
    
    
      JOB_NAME: SUCCESS
    JOB_NAME
    

This output includes the following values:

  * `JOB_NAME`: the name of the job.

  * `USERNAME`: your Google Cloud username.

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.




## View the output files

To view the output files created by the sample `dsub` pipeline using the gcloud CLI, run the [`gcloud storage ls` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls):
    
    
    gcloud storage ls gs://BUCKET_NAME/WORK_DIRECTORY \
        --project PROJECT_ID
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created.

  * `WORK_DIRECTORY`: the directory that you specified in the `dsub` command.

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.




The output is similar to the following:
    
    
    gs://BUCKET_NAME/WORK_DIRECTORY/HG00114.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam.bai
    gs://BUCKET_NAME/WORK_DIRECTORY/logs/
    

This output includes the BAI file and a directory containing the job's logs.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the current project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

If you want to keep using the current project, then delete the individual resources used in this tutorial.

#### Delete the bucket

After the pipeline finishes running, it creates and stores output files in the `WORK_DIRECTORY` directory of your Cloud Storage bucket.

To reduce Cloud Storage charges to the current current Google Cloud account, do one of the following:

  * If you no longer need the bucket you used in this tutorial, then use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) with the `--recursive` flag to delete the bucket and all of its contents:
        
        gcloud storage rm gs://BUCKET_NAME \
            --recursive \
            --project PROJECT_ID
        

Replace the following:

    * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created.

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.

  * Otherwise, if you still need the bucket, then use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) with the `--recursive` flag to delete only the `WORK_DIRECTORY` directory and all of its contents:
        
        gcloud storage rm gs://BUCKET_NAME/WORK_DIRECTORY \
            --recursive \
            --project PROJECT_ID
        

Replace the following:

    * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created.

    * `WORK_DIRECTORY`: the directory that you specified in the `dsub` command.

    * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.




#### Delete the job

To delete a job using the gcloud CLI, run the [`gcloud batch jobs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/delete).
    
    
    gcloud batch jobs delete JOB_NAME \
        --location us-central1 \
        --project PROJECT_ID
    

Replace the following:

  * `JOB_NAME`: the name of the job.
  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project.



## What's next

  * Learn more about [`dsub`](https://github.com/databiosphere/dsub) and [`dsub` for Batch](https://github.com/DataBiosphere/dsub/blob/google-batch/docs/batch/README.md).
  * Learn more about [using storage volumes with Batch](https://docs.cloud.google.com/batch/docs/create-run-job-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
