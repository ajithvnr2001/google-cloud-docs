---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-gke/
title: Quickstart: Deploy an app to GKE using Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:59.295497+00:00
---

# Quickstart: Deploy an app to GKE using Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an app to GKE using Cloud Deploy

This page shows you how to use Cloud Deploy to deliver a sample application image named `nginx` to a sequence of two Google Kubernetes Engine clusters.

In this quickstart, you'll do the following:

  1. Create the two clusters.

  2. Create a [Skaffold](https://cloud.google.com/skaffold) configuration and a Kubernetes manifest to specify the (pre-built) container image to deploy.

  3. Define your Cloud Deploy delivery pipeline and deployment [targets](https://docs.cloud.google.com/deploy/docs/terminology#target), which point to the two clusters.

  4. Instantiate your delivery pipeline by creating a release, which automatically deploys to the first target.

  5. Promote the release to the second target.

  6. View both rollouts in Google Cloud console.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Deploy, Cloud Build, GKE, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-gke)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Cloud Deploy, Cloud Build, GKE, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-gke)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




### Required roles

To ensure that the Cloud Deploy service account has the necessary permissions to run Cloud Deploy operations and deploy to Cloud Run, ask your administrator to grant the following IAM roles to the Cloud Deploy service account on your project: 

**Important:** You must grant these roles to the Cloud Deploy service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Google Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`)
  * [IAM Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Cloud Deploy Job Runner ](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Cloud Deploy service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create your Google Kubernetes Engine clusters

Create two clusters: `qsdev` and `qsprod`, with default settings. The clusters' Kubernetes API endpoints must be network-reachable from the public internet. GKE clusters are externally accessible by default.
    
    
    gcloud container clusters create-auto quickstart-cluster-qsdev --project=PROJECT_ID --region=us-central1 && gcloud container clusters create-auto quickstart-cluster-qsprod --project=PROJECT_ID --region=us-central1
    

## Prepare your Skaffold configuration and Kubernetes manifest

Cloud Deploy uses [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) to provide the details for what to deploy and how to deploy it properly for your separate [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

In this quickstart, you create a `skaffold.yaml` file, which identifies the Kubernetes manifest to be used to deploy the sample app.

  1. Open a terminal window.

  2. Create a new directory, named `deploy-gke-quickstart` and navigate into it.
         
         mkdir deploy-gke-quickstart
         cd deploy-gke-quickstart
         

  3. Create a file named `skaffold.yaml` with the following contents:
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - k8s-*
         deploy:
           kubectl: {}
         

This file is a minimal Skaffold config, identifying your manifest. For this quickstart, you create the file. But you can also [have Cloud Deploy create one for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#have_generate_your_skaffoldyaml), for simple, non-production applications.

See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this file.

  4. Create a file named `k8s-pod.yaml`, with the following contents:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: getting-started
         spec:
           containers:
           - name: nginx
             image: my-app-image
         

This file is a basic Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is applied to the cluster to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.


**Note:** If you want to use different manifests per target, read [this article about managing manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to find out more about using Skaffold profiles.

## Create your delivery pipeline and targets

You can define your pipeline and targets in one file or in separate files. In this quickstart, you create a single file.

  1. In the `deploy-gke-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-gke-demo-app-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: qsdev
             profiles: []
           - targetId: qsprod
             profiles: []
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: qsdev
         description: development cluster
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/quickstart-cluster-qsdev
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: qsprod
         description: production cluster
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/quickstart-cluster-qsprod
         

  2. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a pipeline, with targets, ready to deploy your application to your first target.

  3. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, and the two targets are listed in the **Targets** column.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-1.png)




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

Run the following command from the `deploy-gke-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
    gcloud deploy releases create test-release-001 \
      --project=PROJECT_ID \
      --region=us-central1 \
      --delivery-pipeline=my-gke-demo-app-1 \
      --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the manifest with the specific, SHA-qualified image. Google recommends that you templatize your manifests this way, and that you use SHA-qualified image names at release creation.

As with all releases (unless they include `--disable-initial-rollout`), Cloud Deploy automatically creates a [rollout](https://docs.cloud.google.com/deploy/docs/terminology#rollout) resource too. The application is automatically deployed into the first target in the progression.

## Promote the release

**Note:** after you create the release, you might need wait a few minutes before you continue with this step.

  1. From the **Delivery pipelines** page, click the `my-gke-demo-app-1` pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress. In this case, it shows that the release was deployed to the `qsdev` target.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipeline_viz0.png)

  2. On the first target in the delivery pipeline visualization, click **Promote**.

The **Promote release** dialog is shown. It shows the details of the target you're promoting to.

  3. Click **Promote**.

The release is now queued for deployment into `qsprod`. When deployment is complete, the delivery pipeline visualization shows it as deployed:

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipeline_viz1.png)




## View the results in Google Cloud console

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your **my-gke-demo-app-1** delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline "my-gke-demo-app-1".

The pipeline visualization shows the app's progress through the pipeline.

![delivery pipeline visualization in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/pipeline_viz1.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name, `test-release-001`.

Your rollouts appear under **Rollouts**. You can click a rollout to view its details, including the deployment log.

![rollouts in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/rollouts_success.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the `qsdev` cluster:
         
         gcloud container clusters delete quickstart-cluster-qsdev --region=us-central1 --project=PROJECT_ID
         

  2. Delete the `qsprod` cluster:
         
         gcloud container clusters delete quickstart-cluster-qsprod --region=us-central1 --project=PROJECT_ID
         

  3. Delete the delivery pipeline, targets, release and rollouts:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  4. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * Learn how to [manage your manifests](https://docs.cloud.google.com/deploy/docs/skaffold).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
