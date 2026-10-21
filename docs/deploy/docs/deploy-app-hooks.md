---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-hooks/
title: Quickstart: Run hooks before and after deploying \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:48.071789+00:00
---

# Quickstart: Run hooks before and after deploying  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-hooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run hooks before and after deploying

This quickstart shows you how to run a deploy hook—an arbitrary program to run before or after you deploy using Cloud Deploy.

In this quickstart, you'll do the following:

  1. Create one GKE cluster or one Cloud Run service.

You can use GKE attached clusters for this too, but this quickstart uses GKE and Cloud Run only.

  2. Define your Cloud Deploy delivery pipeline and deployment target.

The delivery pipeline configuration includes the deploy hook definitions, as `tasks`.

This pipeline includes only one stage and uses only one target.

  3. Create a [Skaffold](https://cloud.google.com/skaffold) configuration and either a Kubernetes manifest or a Cloud Run service definition.

The Skaffold configuration file is where you identify the manifests you wish to deploy with Cloud Deploy.

  4. Create a release, which automatically deploys to the target.

One of the hooks is run before the application is deployed, and the other is run after.

  5. View the results of the pre- and post-deploy hooks in the Cloud Build logs, using the Cloud Deploy **Rollout details** page in Google Cloud console.




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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-hooks)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-hooks)

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
            




## Create your runtime environment

**If you're deploying to Cloud Run, you can skip this command**.

For GKE, create one cluster: `deploy-hooks-cluster`, with default settings. The cluster's Kubernetes API endpoint must be network-reachable from the public internet. GKE clusters are externally accessible by default.
    
    
    gcloud container clusters create-auto deploy-hooks-cluster \
                     --project=PROJECT_ID \
                     --region=us-central1
    

## Create your delivery pipeline and target

You can define your pipeline and target in one file or in separate files. In this quickstart, you create a single file.

  1. Open a terminal window.

  2. Create a new directory and navigate into it.

###  GKE 
         
         mkdir deploy-hooks-gke-quickstart
         cd deploy-hooks-gke-quickstart
         

###  Cloud Run 
         
         mkdir deploy-hooks-run-quickstart
         cd deploy-hooks-run-quickstart
         

  3. Create your delivery pipeline and target definition:

###  GKE 

In the `deploy-hooks-gke-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: deploy-hooks-demo-app-gke-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: hooks-staging
             profiles: []
             strategy:
               standard:
                 predeploy:
                   tasks:
                   - type: container
                     image: ubuntu
                     command: ["/bin/sh"]
                     args: ["-c", 'echo "this is a predeploy action"' ]
                 postdeploy:
                   tasks:
                   - type: container
                     image: ubuntu
                     command: ["/bin/sh"]
                     args: ["-c", 'echo "this is a postdeploy action"' ]
         ---
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: hooks-staging
         description: hooks staging cluster
         gke:
           cluster: projects/PROJECT_ID/locations/us-central1/clusters/deploy-hooks-cluster
         

###  Cloud Run 

In the `deploy-hooks-run-quickstart` directory, create a new file: `clouddeploy.yaml`, with the following contents:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: deploy-hooks-demo-app-run-1
         description: main application pipeline
         serialPipeline:
           stages:
           - targetId: hooks-staging
             profiles: []
             strategy:
               standard:
                 predeploy:
                   tasks:
                   - type: container
                     image: ubuntu
                     command: ["/bin/sh"]
                     args: ["-c", 'echo "this is a predeploy action"' ]
                 postdeploy:
                   tasks:
                   - type: container
                     image: ubuntu
                     command: ["/bin/sh"]
                     args: ["-c", 'echo "this is a postdeploy action"' ]
         ---
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: hooks-staging
         description: staging Run service
         run:
           location: projects/PROJECT_ID/locations/us-central1
         

**Note:** In this file, the target is included with the delivery pipeline, but you can define targets in a separate file or multiple separate files.
  4. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a delivery pipeline, with one target, ready to deploy your application and run your pre-deploy and post-deploy jobs.

  5. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, with one target listed in the **Targets** column.

![delivery pipeline page in Google Cloud console, showing your pipeline ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-hooks.png)




## Create your Skaffold configuration file and application manifest

Cloud Deploy uses [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) to identify the manifests used to deploy the sample app to your [target](https://docs.cloud.google.com/deploy/docs/terminology#target).

  1. Create a file named `skaffold.yaml` with the following contents:

###  GKE 
         
         apiVersion: skaffold/v4beta7
         kind: Config
         manifests:
           rawYaml:
           - k8s-pod.yaml
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
         

See the [`skaffold.yaml` reference](https://skaffold.dev/docs/references/yaml/) for more information about this configuration file.

  2. Create the definition for your application—a service definition for Cloud Run or a Kubernetes manifest for GKE.

###  GKE 

Create a file named `k8s-pod.yaml`, with the following contents:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-hooks-pod
         spec:
           containers:
           - name: nginx
             image: my-app-image
         

This file is a basic Kubernetes [manifest](https://kubernetes.io/docs/reference/glossary/?fundamental=true#term-manifest), which is applied to the cluster to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.

###  Cloud Run 

Create a file named `service.yaml`, with the following contents:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: my-hooks-run-service
         spec:
           template:
             spec:
               containers:
               - image: my-app-image
         

This file is a simple Cloud Run service definition, which is used to deploy the application. The container image to deploy is set here as a placeholder, `my-app-image`, which is replaced with the specific image when you create the release.


**Note:** If you want to use different manifests per target, read [this article about managing manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) to find out more about using Skaffold profiles.

## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

###  GKE 

Run the following command from the `deploy-hooks-gke-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=deploy-hooks-demo-app-gke-1 \
       --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the manifest with the specific, SHA-qualified image. Google recommends that you templatize your manifests this way, and that you use SHA-qualified image names at release creation.

###  Cloud Run 

Run the following command from the `deploy-hooks-run-quickstart` directory to create a `release` resource that represents the container image to deploy:
    
    
     gcloud deploy releases create test-release-001 \
       --project=PROJECT_ID \
       --region=us-central1 \
       --delivery-pipeline=deploy-hooks-demo-app-run-1 \
       --images=my-app-image=us-docker.pkg.dev/cloudrun/container/hello@sha256:95ade4b17adcd07623b0a0c68359e344fe54e65d0cb01b989e24c39f2fcd296a
    

Notice the [`--images=` flag](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images), which you use to replace the placeholder (`my-app-image`) in the service definition with the specific, SHA-qualified image. Google recommends that you templatize your service and job definitions this way, and that you use SHA-qualified image names at release creation.

As with all releases (unless they include `--disable-initial-rollout`), Cloud Deploy automatically creates a [rollout](https://docs.cloud.google.com/deploy/docs/terminology#rollout) resource too. The application is automatically deployed into the one target configured for this delivery pipeline.

Also, the pre-deploy job runs before the application is deployed, and the post-deploy job runs after.

## View the results in Google Cloud console

After a few minutes, your release is deployed into your target runtime.

The pre- and post-deploy hooks that we configured (for example purposes) print strings to the Cloud Build logs. We can view those logs to confirm that the hooks worked as expected.

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your delivery pipeline ("deploy-hooks-demo-app-gke-1" or "deploy-hooks-demo-app-run-1").

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline ("deploy-hooks-demo-app-gke-1" or "deploy-hooks-demo-app-run-1").

The pipeline visualization shows the app's deployment status. Because there's only one stage in the pipeline, the visualization shows only one node.

![Delivery pipeline visualization showing success](https://docs.cloud.google.com/static/deploy/images/pipeline_viz_hooks.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the **Rollouts** tab, under **Delivery pipeline details**.

  4. Click the rollout name to view the rollout details.

![rollouts in Google Cloud console](https://docs.cloud.google.com/static/deploy/images/hooks-rollout-details.png)

**Predeploy** and **Postdeploy** are listed as jobs.

  5. Click **Predeploy**

The job run log is displayed.

  6. Scroll down in the list of log entries to find `predeploy-echo`, and click it.

![Log for the Predeploy job](https://docs.cloud.google.com/static/deploy/images/hooks-predeploy-echo.png)

Notice the `textPayload`. That string is what was configured in the `predeploy-action` in your Delivery pipeline.

  7. Click the **Postdeploy** job, and find the `postdeploy-echo` log entry.

![Log for the Postdeploy job](https://docs.cloud.google.com/static/deploy/images/hooks-postdeploy-echo.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the GKE cluster or Cloud Run service:

###  GKE 
         
         gcloud container clusters delete deploy-hooks-cluster --region=us-central1 --project=PROJECT_ID
         

###  Cloud Run 
         
         gcloud run services delete my-hooks-run-service --region=us-central1 --project=PROJECT_ID
         

  2. Delete the delivery pipeline, target, release, and rollout:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  3. Delete the Cloud Storage buckets that Cloud Deploy created.

One ends with `_clouddeploy`, and the other is `[region].deploy-artifacts.[project].appspot.com`.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).

  * [Learn how to combine Google Cloud CI/CD tools to develop and deliver software effectively to GKE](https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
