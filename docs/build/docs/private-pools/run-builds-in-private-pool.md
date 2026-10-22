---
url: https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool/
title: Run builds in a private pool \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:47.645225+00:00
---

# Run builds in a private pool  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Run builds in a private pool Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to run builds in private pools. If you're new to private pools, read the [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## Before you begin

  * Make sure you've created a private pool using the steps in [Creating and managing private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

  * To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://cloud.google.com/sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * You can either use the same Google Cloud project to create your private pool and your Cloud Build builds or use different projects. If your builds are in a different project from your private pool, set the default project in the gcloud CLI to the project where your builds originate:
        
        gcloud config set project BUILD_ORIGIN_PROJECT_ID
        




### IAM permissions

  * To run builds via the gcloud CLI or the Cloud Build API, grant the **WorkerPool User** role in the private pool project to the user or service account that requests the build.

  * To run automated builds using triggers:

    * If the project in which you're starting the build is the same as the project in which your private pool exists, you don't need to grant any permissions.
    * If the project in which you're starting the build is different from the project in which your private pool exists, grant the **WorkerPool User** role to the service account you are using with your trigger on the workerpool project where your builds are created:

###  Console 

    1. Open the **IAM** page in the Google Cloud console.

[Open the IAM Permissions page](https://console.cloud.google.com/iam-admin/iam)

    2. In the project selector drop-down menu at the top of the page, select the project that contains your private pool.

    3. Click **Grant access**.

    4. Enter the following principal and role settings:

       * **Add principals** : Enter email address of the service account that you are using with your trigger.

       * **Assign roles** : Select the Cloud Build WorkerPool User role.

    5. Click **Save** to save your new IAM permissions.

###  gcloud 

**To add the build service account from the trigger project to the workerpool project with the cloudbuild.workerPoolUser role** :
    
    gcloud projects add-iam-policy-binding PRIVATEPOOL_PROJECT_ID \
          --member=serviceAccount:SERVICE_ACCOUNT \
          --role=roles/cloudbuild.workerPoolUser
    

Replace the placeholder values in the command above with the following:

    * `PRIVATEPOOL_PROJECT_ID` is the ID of the project with the private pool running the build.
    * `SERVICE_ACCOUNT` is the email of the service account you are using with the trigger executing the build.




## Running builds

You can submit builds from the same Google Cloud project where you created the private pool or from a different Google Cloud project. You can specify the private pool either in your build config file or direcly in the `gcloud` command:

**Specifying the private pool in the build config file:**

  1. In your [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config), add a `pool` option and specify the full resource name of the private pool to run the build:

###  YAML 
         
         steps:
         - name: 'bash'
           args: ['echo', 'I am running in a private pool!']
         options:
           pool:
             name: 'projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID'
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "bash",
             "args": [
               "echo",
               "I am running in a private pool!"
             ]
           }
           ],
           "options": {
             "pool" : {
               "name" : "projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID"
             }
           }
         }
         

Replace the placeholder values in the config file above with the following:

     * `PRIVATEPOOL_PROJECT_ID`: the Google Cloud project where your private pool is located.
     * `REGION`: the region where you created your private pool.
     * `PRIVATEPOOL_ID`: the unique private pool ID that you specified when creating the private pool.
  2. Use the build config file created above to run your build via [`gcloud` or API](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or using [triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds). If your instance is hosted on-premises, Cloud Build also provides trigger functionality support for several external source code management systems such as [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github-enterprise) or [Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-server).




**Specifying the private pool in the gcloud command:**

You can specify the private pool in the `gcloud` command instead of in the build config file. For example, consider you have the following build config file:

###  YAML 
    
    
      steps:
      - name: 'bash'
        args: ['echo', 'I am running in a private pool!']
    

###  JSON 
    
    
      {
        "steps": [
        {
          "name": "bash",
          "args": [
            "echo",
            "I am running in a private pool!"
          ]
        }
        ],
      }
    

The following command builds using the build config file and specifies the worker pool in the command:
    
    
    gcloud builds submit --config=CONFIG_FILE
      --worker-pool=projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID
    

Replace the placeholder values in the above commands with the following:

  * `CONFIG_FILE`: path to your build config file.
  * `PRIVATEPOOL_ID`: the unique private pool ID that you specified when creating the private pool.
  * `PRIVATEPOOL_PROJECT_ID`: the Google Cloud project where your private pool is located.
  * `REGION`: the region where you created your private pool.



## What's next?

  * Learn how to [create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).
  * Learn how to [use VPC Service Controls with private pools](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).
  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [build repositories from GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github-enterprise).
  * Learn how to [build repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-server).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
