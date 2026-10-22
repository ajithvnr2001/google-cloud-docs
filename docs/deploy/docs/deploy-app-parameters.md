---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-parameters/
title: Quickstart: Use deploy parameters \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:15.338223+00:00
---

# Quickstart: Use deploy parameters  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use deploy parameters

This page shows you how to use Cloud Deploy to deliver a sample application to two [targets](https://docs.cloud.google.com/deploy/docs/terminology#target) at the same time (a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel)), while passing a different parameter value to each rendered manifest or service definition, using three different methods.

In this quickstart, you'll do the following:

  1. Create two GKE clusters or two Cloud Run services.

You can use GKE attached clusters too, but this quickstart uses GKE and Cloud Run only.

  2. Create a [Skaffold](https://cloud.google.com/skaffold) configuration and either a Kubernetes manifest or a Cloud Run service definition.

The manifest or service definition will be the same for both [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child_target), but at deploy time the rendered manifest or service definition for each child target will have different values for the specific parameters configured in this quickstart.

  3. Define your Cloud Deploy delivery pipeline and deployment targets.

This pipeline will have one [multi-target](https://docs.cloud.google.com/deploy/docs/terminology#multi-target), referencing two [child targets](https://docs.cloud.google.com/deploy/docs/terminology#child_target), to deliver your app to the two clusters or two services.

  4. Define [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) in three different places:

     * In the pipeline progression
     * On the child targets
     * On the command line, when creating the release
  5. Instantiate your delivery pipeline by creating a release, which automatically deploys to the two targets in parallel.

  6. View the "controller rollout" and child rollouts in Google Cloud console.




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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-gke)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-gke)

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
            

     2. Add the developer role for your specific runtime.
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
              

     3. Add the `iam.serviceAccountUser` role, which includes the `actAs`permission to deploy to the runtime: 
            
            gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/iam.serviceAccountUser" \
                --project=PROJECT_ID
            




## Create your runtime environments

**If you're deploying to Cloud Run, you can skip this command**.

For GKE, create two clusters: `deploy-params-cluster-prod1` and `deploy-params-cluster-prod2`, with default settings. The clusters' Kubernetes API endpoints must be network-reachable from the public internet. GKE clusters are externally accessible by default.
    
    
    gcloud container clusters create-auto deploy-params-cluster-prod1 \
                     --project=PROJECT_ID \
                     --region=us-central1 \
                     && gcloud container clusters create-auto deploy-params-cluster-prod2 \
                     --project=PROJECT_ID \
                     --region=us-west1
    

## Prepare your Skaffold configuration and manifests

Cloud Deploy uses [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) to provide the details for what to deploy and how to deploy it properly for your separate [targets](https://docs.cloud.google.com/deploy/docs/terminology#target).

In this quickstart, you create a `skaffold.yaml` file, which identifies the Kubernetes manifest or Cloud Run service definition to be used to deploy the sample app.

  1. Open a terminal window.

  2. Create a new directory and navigate into it.

###  GKE 
         
         mkdir deploy-params-gke-quickstart
         cd deploy-params-gke-quickstart
         

###  Cloud Run 
         
         mkdir deploy-params-run-quickstart
         cd deploy-params-run-quickstart
         

  3. Create a file named `skaffold.yaml` with the following contents:

###  GKE 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - kubernetes.yaml
         deploy:
           kubectl: {}
         

###  Cloud Run 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - service.yaml
         deploy:
           cloudrun: {}
         

This file is a minimal Skaffold config. For this quickstart, you create the file. But you can also [have Cloud Deploy create one for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#have_generate_your_skaffoldyaml), for simple, non-production applications.

See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this file.

  4. Create the definition for your application—a service definition for Cloud Run or a Kubernetes manifest for GKE.

###  GKE 

Create a file named `kubernetes.yaml`, with the following contents:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment
         spec:
           replicas: 1 # from-param: ${replicaCount}
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               labels:
                 app: my-app
               annotations:
                 commit: defaultShaValue # from-param: ${git-sha}
             spec:
               containers:
               - name: nginx
                 image: my-app-image
                 env:
                 - name: envvar1
                   value: default1 # from-param: ${application_env1}
                 - name: envvar2
                   value: default2 # from-param: ${application_env2}
         

This file is a Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is applied to the cluster to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Cloud Run 

Create a file named `service.yaml`, with the following contents:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: my-parallel-run-service
         spec:
           autoscaling.knative.dev/minScale: 1 # from-param: ${minInstances}
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               annotations:
                 commit: defaultShaValue # from-param: ${git-sha}
             spec:
               containers:
               - image: my-app-image
                 env:
                 - name: envvar1
                   value: defaultValue1 # from-param: ${application_env1}
                 - name: envvar2
                   value: defaultValue2 # from-param: ${application_env2}
         

This file is a basic Cloud Run service definition, which is used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.


**Note:** If you want to use different manifests per target, read [this article about managing manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to find out more about using Skaffold profiles.

## Create your delivery pipeline and targets

You can define your pipeline and targets in one file or in separate files. In this quickstart, we create a single file.

  1. Create your delivery pipeline and target definition:

###  GKE 

In the `deploy-params-gke-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-params-demo-app-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: params-prod-multi
             deployParameters:
             - values:
                 replicaCount: "2"
               # Apply the deploy parameter replicaCount: "2" to the target with this label
               matchTargetLabels:
                 label1: label1
             - values:
                 replicaCount: "3"
               # Apply the deploy parameter replicaCount: "3" to the target with this label
               matchTargetLabels:
                 label2: label2
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-multi
         description: production clusters
         multiTarget:
           targetIds: [params-prod-a, params-prod-b]
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-a
           labels:
             label1: label1
         description: production cluster 1
         deployParameters:
           application_env1: "sampleValue1"
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/deploy-params-cluster-prod1
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-b
           labels:
             label2: label2
         description: production cluster 2
         deployParameters:
           application_env2: "sampleValue2"
         gke:
           cluster: projects/PROJECT_ID/locations/us-west1/clusters/deploy-params-cluster-prod2
         

**Note:** In this file, targets are included with the delivery pipeline, but you can define targets in a separate file or multiple separate files.

###  Cloud Run 

In the `deploy-params-run-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: my-params-demo-app-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: params-prod-multi
             deployParameters:
             - values:
                 minInstances: "2"
               # Apply the deploy parameter minInstances: "2" to the target with this label
               matchTargetLabels:
                 label1: label1
             - values:
                 minInstances: "3"
               # Apply the deploy parameter minInstances: "3" to the target with this label
               matchTargetLabels:
                 label2: label2
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-multi
         description: production clusters
         multiTarget:
           targetIds: [params-prod-a, params-prod-b]
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-a
           labels:
             label1: label1
         description: production cluster 1
         deployParameters:
           application_env1: "sampleValue1"
         run:
           location: projects/PROJECT_ID/locations/us-central1
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: params-prod-b
           labels:
             label2: label2
         description: production cluster 2
         deployParameters:
           application_env2: "sampleValue2"
         run:
           location: projects/PROJECT_ID/locations/us-west1
         

**Note:** In this file, targets are included with the delivery pipeline, but you can define targets in a separate file or multiple separate files.

  2. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID 
         

You now have a pipeline, with one multi-target comprising two GKE or Cloud Run targets, ready to deploy your application.

  3. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown. Notice that there is one target listed in the **Targets** column even though you configured three targets (one multi-target and two child targets) in your `clouddeploy.yaml` file.

![delivery pipeline visualization in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-multiparms1.png)

Notice that the only target listed is the multi-target `params-prod-multi`. Child targets are not shown.




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

###  GKE 

Run the following command from the `deploy-gke-parallel-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-params-demo-app-1 \
       --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa \
       --deploy-parameters="git-sha=f787cac"
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the manifest with the specific, SHA-qualified image. Google recommends that you templatize your manifests this way, and that you use SHA-qualified image names at release creation.

###  Cloud Run 

Run the following command from the `deploy-run-parallel-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=my-params-demo-app-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a \
       --deploy-parameters="git-sha=f787cac"
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the service definition with the specific, SHA-qualified image. Google recommends that you templatize your service and job definitions this way, and that you use SHA-qualified image names at release creation.

As always, when you create a release, a rollout is created automatically for the first target in your pipeline (unless a specific target is specified using `--to-target=`). In this quickstart, this target is a multi-target, so the [`rollout`](https://docs.cloud.google.com/deploy/docs/terminology#rollout) is a "controller rollout" for two child targets, and there are no subsequent targets in the delivery pipeline. This means that your application is deployed everywhere upon rollout creation. 

## View the results in Google Cloud console

Now that you've created the release, and the controller rollout and child rollouts are created, those child rollouts are now deployed (or are in the process of being deployed) to their respective GKE clusters or Cloud Run services.

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your **my-parallel-demo-app-1** delivery pipeline.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline "my-parallel-demo-app-1".

The pipeline visualization shows the app's deployment status. Because there's only one stage in the pipeline, the visualization shows only one node.

![delivery pipeline visualization in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/parallel_qs_pipeline_viz1.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name, `test-release-001`.

Your rollouts appear under **Rollouts**. You can click a rollout to view its details, including the deployment log.

![rollouts in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/parallel_rollouts_success.png)

  4. Under **Release details** , select the **Artifacts** tab.

The **Deploy parameters** table lists all the parameters you configured in your manifest and the values you provided for those parameters:

###  GKE 

![deploy parameters and
values shown in the Google Cloud console](https://docs.cloud.google.com/static/deploy/images/deploy-params-table1.png)

###  Cloud Run 

![deploy parameters and
values shown in the Google Cloud console](https://docs.cloud.google.com/static/deploy/images/deploy-params-table1-cr.png)

In addition to the parameters and values, the table shows which target each parameter applies to.

  5. In the _Release inspector_ column, click on _View artifacts_ for either target.

  6. Click **Show diff** , then select `params-prod-a` for one target, and `params-prod-b` for the other.

A diff is shown, comparing the rendered manifests of the two targets, including the values you specified:

###  GKE 

![diff of the rendered manifests, with passed values](https://docs.cloud.google.com/static/deploy/images/deploy-params-rendered-gke.png)

###  Cloud Run 

![A target-specific rendered manifest, with passed values](https://docs.cloud.google.com/static/deploy/images/deploy-params-rendered-cr.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the GKE clusters or Cloud Run services:

###  GKE 
         
         gcloud container clusters delete deploy-params-cluster-prod1 --region=us-central1 --project=PROJECT_ID \
         && gcloud container clusters delete deploy-params-cluster-prod2 --region=us-west1 --project=PROJECT_ID
         

###  Cloud Run 
         
         gcloud run services delete my-parallel-run-service --region=us-central1 --project=PROJECT_ID \
         && gcloud run services delete my-parallel-run-service --region=us-west1 --project=PROJECT_ID
         

  2. Delete the delivery pipeline, multi-target, child targets, release, and rollouts:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  3. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * Learn more about [using deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters).

  * [Read more](https://docs.cloud.google.com/deploy/docs/parallel) about how to deploy to multiple targets at the same time.

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * Learn how to [manage your manifests](https://docs.cloud.google.com/deploy/docs/skaffold).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
