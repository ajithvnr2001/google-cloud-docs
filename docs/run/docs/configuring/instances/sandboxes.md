---
url: https://docs.cloud.google.com/run/docs/configuring/instances/sandboxes/
title: Configure sandboxes for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:44.230126+00:00
---

# Configure sandboxes for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/sandboxes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure sandboxes for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run sandboxes**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run sandboxes provide a fast, secure, and isolated environment to run untrusted code execution tools or browser automation software for agents hosted on your existing instance. Sandboxes are highly optimized for latency and run within the same instance as your container, sharing its allocated CPU and memory.

This page describes how to configure sandboxes on your container. For details about writing code to interact with the sandbox using the CLI, see [Code execution in Cloud Run](https://docs.cloud.google.com/run/docs/code-execution).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI. 
  7. Deploy a Cloud Run [instance](https://docs.cloud.google.com/run/docs/instances/create-and-manage-instances). 



## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable sandboxes

To enable sandboxes in Cloud Run instances, use the Google Cloud CLI or a YAML configuration:

###  gcloud 

To create or update the instance, specify the `--sandbox-launcher` flag:

  * To create a new instance, run the following command:
        
        gcloud beta run instances create INSTANCE --image IMAGE_URL --sandbox-launcher

Replace the following:

    * INSTANCE: the name of your Cloud Run instance.
    * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * To update an existing instance, run the following command:
        
        gcloud beta run instances update INSTANCE --sandbox-launcher




###  YAML 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Update your YAML file to include the `sandboxLauncher` attribute set to `true` inside your container configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER
             image: IMAGE_URL
             sandboxLauncher: true
         

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * CONTAINER: the name of your container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




Sandboxes share the CPU and memory allocated to the host container. Make sure your main container limits for CPU and memory are sufficient to accommodate both your application and any active sandboxes you run at the same time.

## Disable sandboxes

To disable the ability to launch a sandbox in your instance, use the Google Cloud CLI or a YAML configuration:

###  gcloud 

Update the instance using the `--no-sandbox-launcher` flag by running the following command:
    
    
    gcloud beta run instances update INSTANCE --no-sandbox-launcher

Replace INSTANCE with the name of your instance.

###  YAML 

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Update your YAML file to remove the `sandboxLauncher` attribute inside your container configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
         spec:
           containers:
           - name: CONTAINER
             image: IMAGE_URL
         

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * CONTAINER: the name of your container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




## View sandbox settings

To view the current sandbox settings for your Cloud Run instance:

###  gcloud 

  1. Use the following command:
         
         gcloud beta run instances describe INSTANCE

Replace INSTANCE with the name of your instance.

  2. Locate the `sandboxLauncher: true` attribute in the returned configuration.




To run untrusted code in a sandbox from your instance, see [Code execution in Cloud Run](https://docs.cloud.google.com/run/docs/code-execution).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
