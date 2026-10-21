---
url: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-python/
title: Create a Dataflow pipeline using Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:37.049273+00:00
---

# Create a Dataflow pipeline using Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Dataflow pipeline using Python

This document shows you how to use the Apache Beam SDK for Python to build a program that defines a pipeline. Then, you run the pipeline by using a direct local runner or a cloud-based runner such as Dataflow. For an introduction to the WordCount pipeline, see the [How to use WordCount in Apache Beam](https://www.youtube.com/watch?v=RTIOW1fIhkM) video.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com//?walkthrough_id=dataflow--quickstart-beam--quickstart-beam-python)

* * *

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

  7. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Cloud Pub/Sub, Cloud Datastore, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api bigquery pubsub datastore.googleapis.com cloudresourcemanager.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.supportUser, roles/datastream.admin, roles/monitoring.metricsScopesViewer, roles/cloudaicompanion.settingsAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Cloud Pub/Sub, Cloud Datastore, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api bigquery pubsub datastore.googleapis.com cloudresourcemanager.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.supportUser, roles/datastream.admin, roles/monitoring.metricsScopesViewer, roles/cloudaicompanion.settingsAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Grant roles to your Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.objectAdmin`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

     * Replace `PROJECT_ID` with your project ID.
     * Replace `PROJECT_NUMBER` with your project number. To find your project number, see [Identify projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) or use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.
     * Replace `SERVICE_ACCOUNT_ROLE` with each individual role.
  19. Create a Cloud Storage bucket and configure it as follows:
     * Set the storage class to `S` (Standard). 
     * Set the storage location to the following: `US` (United States). 
     * Replace `BUCKET_NAME` with a unique bucket name. Don't include sensitive information in the bucket name because the bucket namespace is global and publicly visible. 
    
    gcloud storage buckets create gs://BUCKET_NAME --default-storage-class STANDARD --location US

  20. Copy the Google Cloud project ID and the Cloud Storage bucket name. You need these values later in this document.



## Set up your environment

Dataflow no longer supports pipelines using Python 2. For more information, see [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page. For details about supported versions, see [Apache Beam runtime support](https://docs.cloud.google.com/dataflow/docs/support/beam-runtime-support).

In this section, use the command prompt to set up an isolated Python virtual environment to run your pipeline project by using [venv](https://docs.python.org/3/library/venv.html). This process lets you isolate the dependencies of one project from the dependencies of other projects.

If you don't have a command prompt readily available, you can use [Cloud Shell](https://console.cloud.google.com/?cloudshell=true). Cloud Shell already has the package manager for Python 3 installed, so you can skip to creating a [virtual environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv).

To install Python and then create a virtual environment, follow these steps:

  1. Check that you have Python 3 and `pip` running in your system: 
         
         python --version
         python -m pip --version

  2. If required, install Python 3 and then set up a Python virtual environment: follow the instructions provided in the _Installing Python_ and _Setting up venv_ sections of the [ Setting up a Python development environment page](https://docs.cloud.google.com/python/docs/setup#installing_python). 



After you complete the quickstart, you can deactivate the virtual environment by running `deactivate`.

## Get the Apache Beam SDK

The Apache Beam SDK is an open source programming model for data pipelines. You define a pipeline with an Apache Beam program and then choose a runner, such as Dataflow, to run your pipeline. 

To download and install the Apache Beam SDK, follow these steps:

  1. Verify that you are in the Python virtual environment that you created in the preceding section. Ensure that the prompt starts with `<env_name>`, where `env_name` is the name of the virtual environment.
  2. Install the latest version of the Apache Beam SDK for Python:
    
    pip install apache-beam[gcp]




## Run the pipeline locally

To see how a pipeline runs locally, use a ready-made Python module for the `wordcount` example that is included with the `apache_beam` package.

The `wordcount` pipeline example does the following:

  1. Takes a text file as input.

This text file is located in a Cloud Storage bucket with the resource name `gs://dataflow-samples/shakespeare/kinglear.txt`.

  2. Parses each line into words.
  3. Performs a frequency count on the tokenized words.



To stage the `wordcount` pipeline locally, follow these steps:

  1. From your local terminal, run the `wordcount` example: 
         
         python -m apache_beam.examples.wordcount \
           --output outputs

  2. View the output of the pipeline: 
         
         more outputs*

  3. To exit, press `q`.

Running the pipeline locally lets you test and debug your Apache Beam program. You can view the `wordcount.py` source code on [Apache Beam GitHub](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py). 

## Run the pipeline on the Dataflow service

In this section, run the `wordcount` example pipeline from the `apache_beam` package on the Dataflow service. This example specifies `DataflowRunner` as the parameter for `--runner`. 

  * Run the pipeline: 
        
        python -m apache_beam.examples.wordcount \
            --region DATAFLOW_REGION \
            --input gs://dataflow-samples/shakespeare/kinglear.txt \
            --output gs://BUCKET_NAME/results/outputs \
            --runner DataflowRunner \
            --project PROJECT_ID \
            --temp_location gs://BUCKET_NAME/tmp/

Replace the following:

    * `DATAFLOW_REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job—for example, `europe-west1`

The `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.

    * `BUCKET_NAME`: the Cloud Storage bucket name that you copied earlier
    * `PROJECT_ID`: the Google Cloud project ID that you copied earlier

**Note:** To specify a [user-managed worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#user-managed), include the `--service_account_email` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options). User-managed worker service accounts are recommended for production workloads. If you don't specify a worker service account when you create a job, Dataflow uses the [Compute Engine default service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#default-service-account).

## View your results

When you run a pipeline using Dataflow, your results are stored in a Cloud Storage bucket. In this section, verify that the pipeline is running by using either the Google Cloud console or the local terminal.

### Google Cloud console

To view your results in Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Dataflow **Jobs** page. 

[Go to Jobs](https://console.cloud.google.com/dataflow)

The **Jobs** page displays details of your `wordcount` job, including a status of **Running** at first, and then **Succeeded**.

  2. Go to the Cloud Storage **Buckets** page. 

[ Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. From the list of buckets in your project, click the storage bucket that you created earlier.

In the `wordcount` directory, the output files that your job created are displayed.




### Local terminal

View the results from your terminal or by using Cloud Shell.

  1. To list the output files, use the [`gcloud storage ls` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls): 
         
         gcloud storage ls gs://BUCKET_NAME/results/outputs* --long

Replace `BUCKET_NAME` with the name of the Cloud Storage bucket used in the pipeline program.

  2. To view the results in the output files, use the [`gcloud storage cat` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat): 
         
         gcloud storage cat gs://BUCKET_NAME/results/outputs*




## Modify the pipeline code

The `wordcount` pipeline in the previous examples distinguishes between uppercase and lowercase words. The following steps show how to modify the pipeline so that the `wordcount` pipeline is not case-sensitive. 

  1. On your local machine, download the latest copy of the [`wordcount` code](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py) from the Apache Beam GitHub repository.
  2. From the local terminal, run the pipeline: 
         
         python wordcount.py --output outputs

  3. View the results: 
         
         more outputs*

  4. To exit, press `q`.
  5. In an editor of your choice, open the `wordcount.py` file.
  6. Inside the `run` function, examine the pipeline steps: 
         
         counts = (
                 lines
                 | 'Split' >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
                 | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
                 | 'GroupAndSum' >> beam.CombinePerKey(sum))

After `split`, the lines are split into words as strings.

  7. To lowercase the strings, modify the line after `split`: 
         
         counts = (
                 lines
                 | 'Split' >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
                 | 'lowercase' >> beam.Map(str.lower)
                 | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
                 | 'GroupAndSum' >> beam.CombinePerKey(sum)) 

This modification maps the `str.lower` function onto every word. This line is equivalent to `beam.Map(lambda word: str.lower(word))`.
  8. Save the file and run the modified `wordcount` job: 
         
         python wordcount.py --output outputs

  9. View the results of the modified pipeline: 
         
         more outputs*

  10. To exit, press `q`.
  11. Run the modified pipeline on the Dataflow service: 
         
         python wordcount.py \
             --region DATAFLOW_REGION \
             --input gs://dataflow-samples/shakespeare/kinglear.txt \
             --output gs://BUCKET_NAME/results/outputs \
             --runner DataflowRunner \
             --project PROJECT_ID \
             --temp_location gs://BUCKET_NAME/tmp/

Replace the following:

     * `DATAFLOW_REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job 
     * `BUCKET_NAME`: your Cloud Storage bucket name
     * `PROJECT_ID`: you Google Cloud project ID



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Note:** If you followed this quickstart in a new project, then you can [delete the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects). 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 
  4. If you keep your project, revoke the roles that you granted to the Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.objectAdmin`
    
    gcloud projects remove-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --role=SERVICE_ACCOUNT_ROLE

  5. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  6. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * [Read about the Apache Beam programming model](https://docs.cloud.google.com/dataflow/model/programming-model-beam).
  * [Interactively develop a pipeline using an Apache Beam notebook](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development).
  * [Learn how to design and create your own pipeline](https://docs.cloud.google.com/dataflow/pipelines/creating-a-pipeline-beam).
  * [Work through the WordCount and Mobile Gaming examples](https://docs.cloud.google.com/dataflow/examples/examples-beam).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
