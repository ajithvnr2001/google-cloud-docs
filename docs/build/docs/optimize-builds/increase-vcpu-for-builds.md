---
url: https://docs.cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds/
title: Increase vCPU for builds \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:45:00.315247+00:00
---

# Increase vCPU for builds  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Increase vCPU for builds Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build lets you increase build speed by running your builds on [high-CPU virtual machine (VM) types](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype) instead of the default standard VM. Although a high-vCPU machine runs builds faster, it can increase startup time for default pools because Cloud Build starts non-standard machines only on demand.

If you need more vCPU options than default pools offer, then you can run your builds on [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), which provide additional high-CPU machine types.

To learn more about all available machine types, see the [Pricing page](https://cloud.google.com/build/pricing).

## Before you begin

To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

  * If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.



## Increase vCPU for default pools

You can increase the vCPU for running builds in a default pool either by passing the value directly to the `gcloud builds submit` command or by specifying the value in the build config file.

**Pass the value directly to the`gcloud builds submit` command:**

To specify a custom VM size directly in the `gcloud builds submit` command, add the `--machine-type` argument to the command:
    
    
        gcloud builds submit --config=cloudbuild.yaml \
            --machine-type=E2_HIGHCPU_8
    

**Specify the value in the build config file:**

###  YAML 

  1. Open your [build config file](https://docs.cloud.google.com/build/docs/build-config-file-schema).

  2. Update the [`machineType`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype) field to an enum value corresponding to one of the [supported machine types for default pools](https://cloud.google.com/build/pricing). The following example shows how to add the `machineType` option to a build config file:
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: ['build', '-t', 'gcr.io/my-project/image1', '.']
         options:
           machineType: 'E2_HIGHCPU_8'
         

  3. Start the build using the [gcloud CLI](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




###  JSON 

  1. Open your [build config file](https://docs.cloud.google.com/build/docs/build-config-file-schema).

  2. Update the [`machineType`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype) field to an enum value corresponding to one of the [supported machine types for default pools](https://cloud.google.com/build/pricing). The following example shows how to add the `machineType` option to a build config file:
         
         {
             "steps": [
             {
                 "name": "gcr.io/cloud-builders/docker",
                 "args": ["build", "-t", "gcr.io/my-project/image1", "."]
             },
             "options": {
                 "machineType": "E2_HIGHCPU_8"
             }
         }
         

  3. Start the build using the [gcloud CLI](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




**Important:** The machine-type configuration options described on this page apply only to builds you run directly using `gcloud builds submit` or through Cloud Build triggers that you configure with your own build config file. If you deploy an application to Cloud Run directly from source code, Cloud Run automatically initiates and manages the build process, and the `machineType` option specified in a local `cloudbuild.yaml` file is not honored. 

To ensure that a specific machine type is used for building your Cloud Run service's container:

  1. Build and push your container image using a dedicated Cloud Build build, configuring the desired `machineType` in the `cloudbuild.yaml`.

  2. Deploy your service to Cloud Run by referencing the image URL in Artifact Registry:
         
         gcloud run deploy SERVICE_NAME --image IMAGE_URL
         




## Increase vCPU for private pools

###  Console 

  1. Open the **Worker pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Select the project in which you created the private pool.

  3. Click the private pool name.

  4. In the **Edit private pool** side panel, use the **Machine type** drop-down to select a larger machine type.

  5. Click **Save**.




###  gcloud 

You can increase the vCPU for running builds in a private pool either by passing the value directly to the `gcloud builds worker-pools update` command or by specifying the value in the private pool config file.

**Specify the value in the private pool config file:**

  1. Open your [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema).

  2. Update the value of `machineType` field to one of the supported [machine types](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#machinetype).

  3. Run the following command, where `PRIVATEPOOL_ID` is the unique identifier for your private pool, `REGION` is the region where your private pool is located, and `PRIVATEPOOL_CONFIG_FILE` is the name of your private pool config file:
         
         gcloud builds worker-pools update PRIVATEPOOL_ID \
             --region=REGION \
             --config-from-file=PRIVATEPOOL_CONFIG_FILE
         




**Pass the value directly to the`gcloud builds worker-pools update` command:**
    
    
       gcloud builds worker-pools update PRIVATEPOOL_ID  \
           --region=REGION \
           --worker-machine-type=PRIVATEPOOL_MACHINE_TYPE
    

Replace the placeholder values in the preceding commands with the following:

  * `PRIVATEPOOL_ID`: the ID of your existing private pool. You cannot update this value; you must specify an existing private pool ID.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.
  * `PRIVATEPOOL_DISK_SIZE`: the updated disk size.
  * `PRIVATEPOOL_MACHINE_TYPE` is the updated machine type.

Cloud Build uses the updated machine type anytime you run builds using corresponding private pool.




## What's next

  * Learn about more best practices to [speed up builds](https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
