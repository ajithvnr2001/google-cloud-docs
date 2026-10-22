---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-automation/
title: Quickstart: Automate pipeline tasks \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:59.126459+00:00
---

# Quickstart: Automate pipeline tasks  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Automate release promotion and rollout advancement in Cloud Deploy

This page shows you how to use Cloud Deploy to automatically promote a release to a target and advance a rollout to its next phase.

In this quickstart, you'll do the following:

  1. Create two GKE clusters or two Cloud Run services.

  2. Create a [Skaffold](https://cloud.google.com/skaffold) configuration and either a Kubernetes manifest or a Cloud Run service definition.

  3. Define your Cloud Deploy delivery pipeline and deployment targets.

The pipeline will deploy to two targets: `dev` and `staging`. And the `staging` target uses a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary).

  4. Define two automation rules:

     * An automation to promote the release into the `staging` target on successful rollout to `dev`.

     * An automation to advance the rollout to the `stable` phase upon successful completion of the `canary-25`` phase.

  5. Instantiate your delivery pipeline by creating a release, which automatically deploys to the `dev` target.

  6. View the delivery pipeline and release in the Google Cloud console.

Because of the automated promotion, this release is promoted into the `staging` automatically.

Because the `staging` target uses a canary deployment strategy, and this is the first deployment into that runtime, the `canary-25` phase is skipped. See [Why phases are sometimes skipped](https://docs.cloud.google.com/deploy/docs/deployment-strategies#skip_phases) to understand more about why the canary phase is skipped the first time.

Because of the automated phase-advance, the rollout is advanced to the `stable` phase.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Deploy, Cloud Build, GKE, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-automation)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Deploy, Cloud Build, GKE, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-automation)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

If you already have the CLI installed, make sure you're running the latest version:
    
    gcloud components update
    

  14. Make sure the [default Compute Engine service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) has sufficient permissions. 

The service account might already have the necessary permissions. These steps are included for projects that disable automatic role grants for default service accounts.

     1. First add the `clouddeploy.jobRunner` role: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/clouddeploy.jobRunner"
            

     2. Add the `clouddeploy.releaser` role: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/clouddeploy.releaser"
            

     3. Add the developer role for your specific runtime.
        * For GKE: 
              
              gcloud projects add-iam-policy-binding PROJECT_ID \
                  --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                  --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                  --role="roles/container.developer"
              

        * For Cloud Run: 
              
              gcloud projects add-iam-policy-binding PROJECT_ID \
                  --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                  --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                  --role="roles/run.developer"
              

  15. Add the `iam.serviceAccountUser` role, which includes the `actAs` permission for the default service account to deploy to the runtime: 
         
         gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --role="roles/iam.serviceAccountUser" \
             --project=PROJECT_ID
         

  16. Add the `iam.serviceAccountUser` role, including `actAs` permission for yourself, to use the default service account: 
         
         gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
             --member=user:YOUR_EMAIL_ADDRESS \
             --role="roles/iam.serviceAccountUser" \
             --project=PROJECT_ID
         

In this case, YOUR_EMAIL_ADDRESS is the email address you use to access Google Cloud.




## Create your runtime environments

**If you're deploying to Cloud Run, you can skip this command**.

For GKE, create two clusters: `automation-quickstart-cluster-dev` and `automation-quickstart-cluster-staging`, with default settings. The clusters' Kubernetes API endpoints must be network-reachable from the public internet. GKE clusters are externally accessible by default.
    
    
    gcloud container clusters create-auto automation-quickstart-cluster-dev \
                     --project=PROJECT_ID \
                     --region=us-central1 \
                     && gcloud container clusters create-auto automation-quickstart-cluster-staging \
                     --project=PROJECT_ID \
                     --region=us-central1
    

## Get your project number.

You need your project number to identify the default service account. This is necessary for configuring the automation resource.

  1. Run the following command to get your project number:
         
         gcloud projects describe PROJECT_ID --format="value(projectNumber)"
         

  2. Copy the project number from the command-line output, and paste it here.

You don't need to run this as a command. Pasting it here populates the service account reference in the automation config later in this quickstart.
         
         PROJECT_NUMBER
         




## Prepare your Skaffold configuration and application manifest

Cloud Deploy uses [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) to provide the details for what to deploy and how to deploy it properly for your separate [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

In this quickstart, you create a `skaffold.yaml` file, which identifies the application manifest to be used to deploy the sample app.

  1. Open a terminal window.

  2. Create a new directory and navigate into it.

###  GKE 
         
         mkdir deploy-automation-gke-quickstart
         cd deploy-automation-gke-quickstart
         

###  Cloud Run 
         
         mkdir deploy-automation-run-quickstart
         cd deploy-automation-run-quickstart
         

  3. Create a file named `skaffold.yaml` with the following contents:

###  GKE 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         metadata:
           name: gke-automation
         manifests:
           rawYaml:
           - k8s-deployment.yaml
         deploy:
           kubectl: {}
         

###  Cloud Run 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         metadata:
           name: run-automation
         profiles:
         - name: dev
           manifests:
             rawYaml:
             - run-dev.yaml
         - name: staging
           manifests:
             rawYaml:
             - run-staging.yaml
         deploy:
           cloudrun: {}
         

This file is a minimal Skaffold config. For this quickstart, you create the file. But you can also [have Cloud Deploy create one for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#have_generate_your_skaffoldyaml), for simple, non-production applications.

See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this file.

  4. Create the definition for your application—a pair of service definitions for Cloud Run or a Kubernetes manifest for GKE.

###  GKE 

Create a file named `k8s-deployment.yaml`, with the following contents:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment
           labels:
             app: my-app
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               labels:
                 app: my-app
             spec:
               containers:
               - name: nginx
                 image: my-app-image
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: my-service
           namespace: default
         spec:
           selector:
             app: my-app
           ports:
             - protocol: TCP
               port: 80
         

This file is a simple Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Cloud Run 

     1. Create a file named `run-dev.yaml`, with the following contents:
            
            apiVersion: serving.knative.dev/v1
            kind: Service
            metadata:
              name: my-automation-run-service-dev
            spec:
              template:
                spec:
                  containers:
                  - image: my-app-image
            

     2. Create a file named `run-staging.yaml`, with the following contents:
            
            apiVersion: serving.knative.dev/v1
            kind: Service
            metadata:
              name: my-automation-run-service-staging
            spec:
              template:
                spec:
                  containers:
                  - image: my-app-image
            

These files are simple Cloud Run service definitions, which are used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.




## Create your delivery pipeline, targets, and automation

You can define your delivery pipeline and targets in one file or in separate files. You can also define an automation action in a separate file. This quickstart uses one file for the pipeline, targets, and automation.

  1. Create your delivery pipeline, target definitions, and automation action:

###  GKE 

In the `deploy-automation-gke-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-automation-demo-app-1
         description: Automation demonstration pipeline
         serialPipeline:
           stages:
           - targetId: automation-quickstart-dev
           - targetId: automation-quickstart-staging
             profiles: []
             strategy:
               canary:
                 runtimeConfig:
                   kubernetes:
                     serviceNetworking:
                       service: "my-service"
                       deployment: "my-deployment"
                 canaryDeployment:
                   percentages: [25]
                   verify: false
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: automation-quickstart-dev
         description: Dev cluster to demonstrate deploy automation
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/automation-quickstart-cluster-dev
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: automation-quickstart-staging
         description: Staging cluster to demonstrate deploy automation
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/automation-quickstart-cluster-staging
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Automation
         metadata:
           name: my-automation-demo-app-1/promote
         description: promotes a release
         suspended: false
         serviceAccount: PROJECT_NUMBER-compute@developer.gserviceaccount.com
         selector:
           targets:
           - id: automation-quickstart-dev
         rules:
         - promoteReleaseRule:
             id: "promote-release"
             wait: 1m
             destinationTargetId: "@next"
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Automation
         metadata:
           name: my-automation-demo-app-1/advance
         description: advances a rollout
         suspended: false
         serviceAccount: PROJECT_NUMBER-compute@developer.gserviceaccount.com
         selector:
           targets:
           - id: automation-quickstart-staging
         rules:
         - advanceRolloutRule:
             id: "advance-rollout"
             sourcePhases: ["canary-25"]
             wait: 1m
         

**Note:** In this file, the targets and the automations config are included with the delivery pipeline, but you can define targets in a separate file or multiple separate files, and automations in a separate file or files.

###  Cloud Run 

In the `deploy-automation-run-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-automation-demo-app-1
         description: Automation demonstration pipeline
         serialPipeline:
           stages:
           - targetId: automation-quickstart-dev
             profiles: [dev]
           - targetId: automation-quickstart-staging
             profiles: [staging]
             strategy:
               canary:
                 runtimeConfig:
                   cloudRun:
                     automaticTrafficControl: true
                 canaryDeployment:
                   percentages: [25]
                   verify: false
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: automation-quickstart-dev
         description: Dev cluster to demonstrate deploy automation
         run:
           location: projects/PROJECT_ID/locations/us-central1
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: automation-quickstart-staging
         description: Staging cluster to demonstrate deploy automation
         run:
           location: projects/PROJECT_ID/locations/us-central1
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Automation
         metadata:
           name: my-automation-demo-app-1/promote
         description: Promotes a release to the next target
         suspended: false
         serviceAccount: PROJECT_NUMBER-compute@developer.gserviceaccount.com
         selector:
           targets:
           - id: automation-quickstart-dev
         rules:
         - promoteReleaseRule:
             id: "promote-release"
             wait: 1m
             destinationTargetId: "@next"
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Automation
         metadata:
           name: my-automation-demo-app-1/advance
         description: advances a rollout
         suspended: false
         serviceAccount: PROJECT_NUMBER-compute@developer.gserviceaccount.com
         selector:
           targets:
           - id: automation-quickstart-staging
         rules:
         - advanceRolloutRule:
             id: "advance-rollout"
             sourcePhases: ["canary-25"]
             wait: 1m
         

**Note:** In this file, the targets and the automations config are included with the delivery pipeline, but you can define targets in a separate file or multiple separate files, and automations in a separate file or files.

  2. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a pipeline, with one multi-target comprising two GKE or Cloud Run targets, ready to deploy your application.

  3. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, with two targets listed in the **Targets** column.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-automations.png)

  4. Click the pipeline name to open the delivery pipeline visualization and details.

  5. Select the **Automations** tab, under **Delivery pipeline details**.

The two automations you created are shown.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipeline_details_automations.png)




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

###  GKE 

Run the following command from the `deploy-automation-gke-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-automation-demo-app-1 \
       --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the manifest with the specific, SHA-qualified image. Google recommends that you templatize your manifests this way, and that you use SHA-qualified image names at release creation.

###  Cloud Run 

Run the following command from the `deploy-automation-run-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-automation-demo-app-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the service definition with the specific, SHA-qualified image. Google recommends that you templatize your service and job definitions this way, and that you use SHA-qualified image names at release creation.

By default, when you create a release, a rollout is created automatically for the first target in your pipeline.

Because this quickstart includes two automations, two things happen automatically:

  * After a successful deployment in the first target, the release is automatically promoted to the second target.

There is a one-minute wait time on the promote automation.

  * In the second target, where there is a 25% canary configured, the second automation advances the rollout from `canary-25` to `stable`.

For this first release, the `canary-25` phase is skipped, because there is no pre-existing version of the app to canary against. And the rollout is automatically advanced to `stable`.

There is a one-minute delay on the advance automation.




When everything finishes, the application is deployed to successfully to both targets without you having to do anything further.

If you want to know more about running a canary deployment strategy, you can try the [canary quickstart](https://docs.cloud.google.com/deploy/docs/deploy-app-canary).

## View the results in Google Cloud console

You can view the results, including the automation runs, in the Google Cloud console.

  1. Navigate to the Cloud Deploy **Delivery pipelines** page to view your delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline "my-automation-demo-app-1".

The pipeline visualization shows the app's deployment status. If enough time has elapsed, both targets will show green.

![delivery pipeline visualization in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/automation_qs_pipeline_viz1.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the **Automation runs** tab.

There are two entries, one for each of the two automations you created. You can click either one to see the details of that automation run.

![automation run details shown in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/automation_run_details_promote.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the GKE clusters or Cloud Run services:

###  GKE 
         
         gcloud container clusters delete automation-quickstart-cluster-dev --region=us-central1 --project=PROJECT_ID \
         && gcloud container clusters delete automation-quickstart-cluster-staging --region=us-west1 --project=PROJECT_ID
         

###  Cloud Run 
         
         gcloud run services delete my-automation-run-service-dev --region=us-central1 --project=PROJECT_ID \
         && gcloud run services delete my-automation-run-service-staging --region=us-central1 --project=PROJECT_ID
         

  2. Delete the delivery pipeline, targets, automations, release, and rollouts:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  3. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * Try some other [automations](https://docs.cloud.google.com/deploy/docs/automation-rules).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
