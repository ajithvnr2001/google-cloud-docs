---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-run/
title: Quickstart: Deploy an app to Cloud Run using Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:58.768062+00:00
---

# Quickstart: Deploy an app to Cloud Run using Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an app to Cloud Run using Cloud Deploy

This page shows you how to use Cloud Deploy to deliver a sample application image named `hello` to a sequence of two Cloud Run services, two Cloud Run jobs, or two Cloud Run worker pools.

In this quickstart, you'll do the following:

  1. Create a [Skaffold](https://cloud.google.com/skaffold) configuration

  2. Create configuration files for two Cloud Run services, two jobs, or two worker pools.

These files define the services or jobs, and specify the (pre-built) container images to deploy.

  3. Define your Cloud Deploy delivery pipeline and deployment [targets](https://docs.cloud.google.com/deploy/docs/terminology#target), which point to the two services, the two jobs, or the two worker pools.

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

  5. Enable the Cloud Deploy, Cloud Build, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-run)

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

  12. Enable the Cloud Deploy, Cloud Build, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-run)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




### Required roles

To ensure that the Cloud Deploy service account has the necessary permissions to run Cloud Deploy operations and deploy to Cloud Run, ask your administrator to grant the following IAM roles to the Cloud Deploy service account on your project: 

**Important:** You must grant these roles to the Cloud Deploy service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`)
  * [IAM Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Cloud Deploy Job Runner ](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddeploy#clouddeploy.jobRunner) (`roles/clouddeploy.jobRunner`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Cloud Deploy service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare your Skaffold configuration

Cloud Deploy uses [Skaffold](https://cloud.google.com/skaffold) to provide the details for what to deploy and how to deploy it properly for your separate [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

For this quickstart, you create a `skaffold.yaml` file, which identifies the Cloud Run service or job definition to be used to deploy the sample app.

  1. Open a terminal window.

  2. Create a new directory, named `deploy-run-quickstart` and navigate into it.
         
         mkdir deploy-run-quickstart
         cd deploy-run-quickstart
         

  3. Create a file named `skaffold.yaml` with the following contents:

###  Services 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         metadata: 
           name: deploy-run-quickstart
         profiles:
         - name: dev
           manifests:
             rawYaml:
             - run-service-dev.yaml
         - name: prod
           manifests:
             rawYaml:
             - run-service-prod.yaml
         deploy:
           cloudrun: {}
         

###  Jobs 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         metadata: 
           name: deploy-run-quickstart
         profiles:
         - name: dev
           manifests:
             rawYaml:
             - run-job-dev.yaml
         - name: prod
           manifests:
             rawYaml:
             - run-job-prod.yaml
         deploy:
           cloudrun: {}
         

###  Worker pools 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         metadata:
           name: deploy-run-quickstart
         profiles:
         - name: dev
           manifests:
             rawYaml:
             - run-worker-pool-dev.yaml
         - name: prod
           manifests:
             rawYaml:
             - run-worker-pool-prod.yaml
         deploy:
           cloudrun: {}
         

This file is a minimal Skaffold config, identifying your Cloud Run services, jobs, or worker pools. See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this file.




## Prepare your Cloud Run services, jobs, or worker pools

For this quickstart, you'll create either two different Cloud Run services, two Cloud Run jobs, or two Cloud Run worker pools, in the same project. Cloud Deploy also supports deploying across multiple projects. Also, we use [Skaffold profiles](https://skaffold.dev/docs/environment/profiles/) to make it possible to have two services, jobs, or worker pools in the same project. When you use different projects, you might not need to use Skaffold profiles.

###  Services 

  1. Create a file named `run-service-dev.yaml` with the following contents:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: deploy-run-service-dev
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file defines a Cloud Run service. As the name `deploy-run-service-dev` implies, this is your `dev` service, and corresponds to the first target in your delivery pipeline progression.

  2. Create a file named `run-service-prod.yaml` with the following contents:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: deploy-run-service-prod
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file defines another Cloud Run service, and as the name `deploy-run-service-prod` implies, this is your `prod` service, and corresponds to the second target in your delivery pipeline progression.




These files are Cloud Run service definitions, which are used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Jobs 

  1. Create a file named `run-job-dev.yaml` with the following contents:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: deploy-run-job-dev
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: my-app-image
         

This file defines a Cloud Run job. As the name `deploy-run-job-dev` implies, this is your `dev` job, and corresponds to the first target in your delivery pipeline progression.

  2. Create a file named `run-job-prod.yaml` with the following contents:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: deploy-run-job-prod
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: my-app-image
         

This file defines another Cloud Run job. As the name `deploy-run-job-prod` implies, this is your `prod` job, and corresponds to the second target in your delivery pipeline progression.




These files are Cloud Run job definitions, which are used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Worker pools 

  1. Create a file named `run-worker-pool-dev.yaml` with the following contents:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: deploy-run-worker-pool-dev
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file defines a Cloud Run worker pool. As the name `deploy-run-worker-pool-dev` implies, this is your `dev` worker pool, and corresponds to the first target in your delivery pipeline progression.

  2. Create a file named `run-worker-pool-prod.yaml` with the following contents:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: deploy-run-worker-pool-prod
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file defines another Cloud Run worker pool. As the name `deploy-run-worker-pool-prod` implies, this is your `prod` worker pool, and corresponds to the second target in your delivery pipeline progression.




These files are Cloud Run worker pool definitions, which are used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

## Create your delivery pipeline and targets

You can define your pipeline and targets in one file or in separate files. In this quickstart, you create a single file.

  1. In the `deploy-run-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-run-demo-app-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: run-qsdev
             profiles: [dev]
           - targetId: run-qsprod
             profiles: [prod]
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: run-qsdev
         description: Cloud Run development service
         run:
           location: projects/PROJECT_ID/locations/us-central1
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: run-qsprod
         description: Cloud Run production service
         run:
           location: projects/PROJECT_ID/locations/us-central1
         

**Note:** In this file, targets are included with the delivery pipeline, but you can define targets in a separate file or multiple separate files.
  2. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a pipeline, with targets, ready to deploy your application to your first target.

  3. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, and the two targets are listed in the **Targets** column.

![Delivery pipeline shown in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/new-pipeline-for-cloud-run.png)




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

Run the following command from the `deploy-run-quickstart` directory to create a `release` resource that represents the container image to deploy:

###  Services 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-run-demo-app-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
    

###  Jobs 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-run-demo-app-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/job@sha256:8eb3f5e72586de6375abe95aa67511c57c61d35fb37d5670e4d68624a68ef916
    

###  Worker pools 
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-run-demo-app-1 \
       --skaffold-version=2.17.0 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the service, job, or worker pool definition with the specific, SHA-qualified image. Google recommends that you templatize your service and job definitions this way, and that you use SHA-qualified image names at release creation.

The [`--skaffold-version=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--skaffold-version) specifies the Skaffold version to use for deployment. For Cloud Run worker pool support, you must use Skaffold version `2.17` or later.

As with all releases (unless they include `--disable-initial-rollout`), Cloud Deploy automatically creates a [rollout](https://docs.cloud.google.com/deploy/docs/terminology#rollout) resource too. The application is automatically deployed into the first target in the progression.

## Promote the release

**Note:** after you create the release, you might need wait a few minutes before you continue with this step.

  1. From the **Delivery pipelines** page, click the `my-run-demo-app-1` pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress. In this case, it shows that the release was deployed to the `run-qsdev` target.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipeline-viz-run-ready-to-promote.png)

  2. On the first target in the delivery pipeline visualization, click **Promote**.

The **Promote release** dialog is shown. It shows the details of the target you're promoting to.

  3. Click **Promote**.

The release is now queued for deployment into `run-qsprod`. When deployment is complete, the delivery pipeline visualization shows it as deployed:

![delivery pipeline visualization in Google Cloud console, showing release deployed to prod.](https://docs.cloud.google.com/static/deploy/images/pipeline_viz_run_done.png)




## View the results in Google Cloud console

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your **my-run-demo-app-1** delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline "my-run-demo-app-1".

The pipeline visualization shows the app's progress through the pipeline.

![delivery pipeline visualization in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/pipeline_viz_run_done.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name, `test-release-001`.

Your rollouts appear under **Rollouts**. You can click a rollout to view its details, including the deployment log.

![rollouts in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/run_rollouts_success.png)




## Accessing your Cloud Run service

By default, you must be authenticated in order to access newly created Cloud Run services or worker pools. See the Cloud Run [Authentication overview](https://docs.cloud.google.com/run/docs/authenticating/overview) to learn how to provide credentials and to find out what Identity and Access Management configuration is required in order access the service without authentication. This doesn't apply to Cloud Run jobs.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the `deploy-qs-dev` Cloud Run service, job, or worker pool:

###  Services 
         
         gcloud run services delete deploy-run-service-dev --region=us-central1 --project=PROJECT_ID
         

###  Jobs 
         
         gcloud run jobs delete deploy-run-job-dev --region=us-central1 --project=PROJECT_ID
         

###  Worker pools 
         
         gcloud run worker-pools delete deploy-run-worker-pool-dev --region=us-central1 --project=PROJECT_ID
         

  2. Delete the `deploy-qs-prod` service, job, or worker pool:

###  Services 
         
         gcloud run services delete deploy-run-service-prod --region=us-central1 --project=PROJECT_ID
         

###  Jobs 
         
         gcloud run jobs delete deploy-run-job-prod --region=us-central1 --project=PROJECT_ID
         

###  Worker pools 
         
         gcloud run worker-pools delete deploy-run-worker-pool-prod --region=us-central1 --project=PROJECT_ID
         

  3. Delete the delivery pipeline, targets, release and rollouts:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  4. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * Read the [how-to article for deploying to Cloud Run](https://docs.cloud.google.com/deploy/docs/run-targets)

  * Learn how to [manage your manifests](https://docs.cloud.google.com/deploy/docs/skaffold).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
