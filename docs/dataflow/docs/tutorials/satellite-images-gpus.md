---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/satellite-images-gpus/
title: Processing Landsat satellite images with GPUs \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:48.398354+00:00
---

# Processing Landsat satellite images with GPUs  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/satellite-images-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Processing Landsat satellite images with GPUs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use GPUs on Dataflow to process Landsat 8 satellite images and render them as JPEG files. The tutorial is based on the example [Processing Landsat satellite images with GPUs](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/gpu-examples/tensorflow-landsat).

## Objectives

  * Build a Docker image for Dataflow that has TensorFlow with GPU support.
  * Run a Dataflow job with GPUs.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Cloud Storage
  * Dataflow
  * Artifact Registry



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

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

  7. Enable the Dataflow, Cloud Build, and Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow cloudbuild.googleapis.com artifactregistry.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
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

  15. Enable the Dataflow, Cloud Build, and Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow cloudbuild.googleapis.com artifactregistry.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Grant roles to your Compute Engine default service account. Run the following command once for each of the following IAM roles: `roles/dataflow.admin`, `roles/dataflow.worker`, `roles/bigquery.dataEditor`, `roles/pubsub.editor`, `roles/storage.objectAdmin`, and `roles/artifactregistry.reader`.
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

     * Replace `PROJECT_ID` with your project ID.
     * Replace `PROJECT_NUMBER` with your project number. To find your project number, see [Identify projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * Replace `SERVICE_ACCOUNT_ROLE` with each individual role.
  19. To store the output JPEG image files from this tutorial, create a Cloud Storage bucket: 
     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
        1. For **Name your bucket** , enter a unique bucket name. Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible. 
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
           1. In the **Set a default class** section, select the following: **Standard**. 
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



## Prepare your working environment

Download the starter files, and then create your Artifact Registry repository.

### Download the starter files

Download the starter files and then change directories.

  1. Clone the `python-docs-samples` repository.
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Navigate to the [sample code directory](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/dataflow/gpu-examples/tensorflow-landsat).
         
         cd python-docs-samples/dataflow/gpu-examples/tensorflow-landsat
         




### Configure Artifact Registry

Create an Artifact Registry repository so that you can upload artifacts. Each repository can contain artifacts for a single supported format.

All repository content is encrypted using either Google-owned and Google-managed encryption keys or customer-managed encryption keys. Artifact Registry uses Google-owned and Google-managed encryption keys by default and no configuration is required for this option.

You must have at least [Artifact Registry Writer access](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the repository.

Run the following command to create a new repository. The command uses the `--async` flag and returns immediately, without waiting for the operation in progress to complete.
    
    
    gcloud artifacts repositories create REPOSITORY \
        --repository-format=docker \
        --location=LOCATION \
        --async
    

Replace REPOSITORY with a name for your repository. For each repository location in a project, repository names must be unique.

Before you can push or pull images, configure Docker to authenticate requests for Artifact Registry. To set up authentication to Docker repositories, run the following command:
    
    
    gcloud auth configure-docker LOCATION-docker.pkg.dev
    

The command updates your Docker configuration. You can now connect with Artifact Registry in your Google Cloud project to push images.

## Build the Docker image

Cloud Build lets you build a Docker image using a Dockerfile and save it into Artifact Registry, where the image is accessible to other Google Cloud products.

Build the container image by using the [`build.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dataflow/gpu-examples/tensorflow-landsat/build.yaml) config file.
    
    
    gcloud builds submit --config build.yaml
    

## Run the Dataflow job with GPUs

The following code block demonstrates how to launch this Dataflow pipeline with GPUs.

We run the Dataflow pipeline using the [`run.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dataflow/gpu-examples/tensorflow-landsat/run.yaml) config file.

**Note:** We launch the job using the container image to make sure the job launches with the same Python version as the workers and with all the dependencies installed.
    
    
    export PROJECT=PROJECT_NAME
    export BUCKET=BUCKET_NAME
    
    export JOB_NAME="satellite-images-$(date +%Y%m%d-%H%M%S)"
    export OUTPUT_PATH="gs://$BUCKET/samples/dataflow/landsat/output-images/"
    export REGION="us-central1"
    export GPU_TYPE="nvidia-tesla-t4"
    
    gcloud builds submit \
        --config run.yaml \
        --substitutions _JOB_NAME=$JOB_NAME,_OUTPUT_PATH=$OUTPUT_PATH,_REGION=$REGION,_GPU_TYPE=$GPU_TYPE \
        --no-source
    

Replace the following:

  * PROJECT_NAME: the Google Cloud project name
  * BUCKET_NAME: the Cloud Storage bucket name (without the `gs://` prefix)



After you run this pipeline, wait for the command to finish. If you exit your shell, you might lose the environment variables that you've set.

To avoid sharing the GPU between multiple worker processes, this sample uses a machine type with 1 vCPU. The memory requirements of the pipeline are addressed by using 13 GB of extended memory. For more information, read [GPUs and worker parallelism](https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus#parallelism).

## View your results

The pipeline in [`tensorflow-landsat/main.py`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dataflow/gpu-examples/tensorflow-landsat/main.py) processes Landsat 8 satellite images and renders them as JPEG files. Use the following steps to view these files.

  1. List the output JPEG files with details by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls).
         
         gcloud storage ls "gs://$BUCKET/samples/dataflow/landsat/" --long --readable-sizes
         

  2. Copy the files into your local directory.
         
         mkdir outputs
         gcloud storage cp "gs://$BUCKET/samples/dataflow/landsat/*" outputs/
         

  3. Open these image files with the image viewer of your choice.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

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



## What's next

  * Look at a [minimal GPU-enabled TensorFlow example](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/dataflow/gpu-examples/tensorflow-minimal)
  * Look at a [minimal GPU-enabled PyTorch example](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/dataflow/gpu-examples/pytorch-minimal)
  * Learn more about [GPU support on Dataflow](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support).
  * Look through tasks for [Using GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
