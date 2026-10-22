---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-custom-target/
title: Quickstart: Define and use custom target type \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:58.762933+00:00
---

# Quickstart: Define and use custom target type  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-custom-target/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Define and use a custom target type

This quickstart shows you how to use Cloud Deploy to create a custom target type, then deploy to a custom target of that type.

In this quickstart, you'll do the following:

  1. Define a custom target type, where you will configure the behavior of the target. This configuration references container images plus shell commands to run on those images, which are the actions for render and deploy operations.

  2. Define a target that references the custom target type.

  3. Define your Cloud Deploy delivery pipeline.

This pipeline includes only one stage and uses only one target. In that stage, you'll reference the target you configured.

  4. Create a [Skaffold](https://cloud.google.com/skaffold) configuration, which is needed by the release.

  5. Create a release, which automatically creates a rollout, resulting in the custom render and deploy operations being performed.

As part of this release and rollout, the render and deploy operations defined in your custom target type configuration are both run.

  6. View the results of the custom operations. This includes a rendered configuration file uploaded to Cloud Storage, and a string written to that file, as well as a results file that includes the status of the operation.




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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-custom-target)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-custom-target)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

If you already have the Google Cloud CLI installed, make sure you're running the latest version:
    
    gcloud components update
    

  14. Make sure the [default Compute Engine service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) has sufficient permissions. 

The service account might already have the necessary permissions. These steps are included for projects that disable automatic role grants for default service accounts.

     1. First add the `clouddeploy.jobRunner` role: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/clouddeploy.jobRunner"
            

     2. Add the developer role for your specific runtime.
     3. Add the `iam.serviceAccountUser` role, which includes the `actAs`permission to deploy to the runtime: 
            
            gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --member=serviceAccount:$(gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
                --role="roles/iam.serviceAccountUser" \
                --project=PROJECT_ID
            




## Create your delivery pipeline, custom target type, and target

You can define your delivery pipeline, custom target type, and target in one file or in separate files. In this quickstart, you create a single file with all three.

  1. Open a terminal window.

  2. Create a new directory and navigate into it.
         
         mkdir custom-target-quickstart
         cd custom-target-quickstart
         

  3. In the custom-target-quickstart directory, create a new file, `clouddeploy.yaml`, with the following content:
         
         apiVersion: deploy.cloud.google.com/v1
         kind: DeliveryPipeline
         metadata:
           name: custom-targets-pipeline
         serialPipeline:
           stages:
           - targetId: sample-env
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: Target
         metadata:
           name: sample-env
         customTarget:
           customTargetType: basic-custom-target
         ---
         
         apiVersion: deploy.cloud.google.com/v1
         kind: CustomTargetType
         metadata:
           name: basic-custom-target
         tasks:
           render:
             type: 'container'
             image: gcr.io/google.com/cloudsdktool/google-cloud-cli@sha256:484e8266c1cfc84b283bc6d4eec1f6b61223115178cce76fb59f77b223f26e8e
             command: ['/bin/bash']
             args:
               - '-c'
               - |-
                 echo "Sample manifest rendered content" > manifest.txt
                 gcloud storage cp manifest.txt $CLOUD_DEPLOY_OUTPUT_GCS_PATH/manifest.txt
                 echo {\"resultStatus\": \"SUCCEEDED\", \"manifestFile\": \"$CLOUD_DEPLOY_OUTPUT_GCS_PATH/manifest.txt\"} > results.json
                 gcloud storage cp results.json $CLOUD_DEPLOY_OUTPUT_GCS_PATH/results.json
           deploy:
             type: 'container'
             image: gcr.io/google.com/cloudsdktool/google-cloud-cli@sha256:484e8266c1cfc84b283bc6d4eec1f6b61223115178cce76fb59f77b223f26e8e
             command: ['/bin/bash']
             args:
               - '-c'
               - |-
                 echo {\"resultStatus\": \"SUCCEEDED\"} > results.json
                 gcloud storage cp results.json $CLOUD_DEPLOY_OUTPUT_GCS_PATH/results.json
         

The custom target type definition includes the `tasks` [stanza](https://docs.cloud.google.com/deploy/docs/tasks), defining a render task and a deploy task. Each of these tasks references a container image to run, and commands to run on that container.

**Note:** The custom target type and the target are included with the delivery pipeline in this file, but you can define them in a separate file or multiple separate files.
  4. Register your pipeline and targets with the Cloud Deploy service:
         
         gcloud deploy apply --file=clouddeploy.yaml --region=us-central1 --project=PROJECT_ID
         

You now have a delivery pipeline, with one target. This is your target using the custom target type, and this pipeline doesn't deploy an application to a runtime.

  5. Confirm your pipeline and targets:

In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view of list of your available delivery pipelines.

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

The delivery pipeline you just created is shown, with one target listed in the **Targets** column.

![delivery pipeline page in Google Cloud console, showing your pipeline ](https://docs.cloud.google.com/static/deploy/images/pipelines-page-custom-targets.png)




## Create your Skaffold configuration file

The release in this quickstart requires a [Skaffold](https://docs.cloud.google.com/deploy/docs/using-skaffold) configuration file, but this file doesn't require meaningful configuration.

  1. Create a file named `skaffold.yaml` with the following contents:
         
         apiVersion: skaffold/v4beta7
         kind: Config
         




## Create a release

A release is the central Cloud Deploy resource representing the changes being deployed. The delivery pipeline defines the lifecycle of that release. See [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release) for details about that lifecycle.

Run the following command from the `custom-target-quickstart` directory to create a `release` resource that represents the custom action to deploy:
    
    
    gcloud deploy releases create test-release-001 \
      --project=PROJECT_ID \
      --region=us-central1 \
      --delivery-pipeline=custom-targets-pipeline
    

As with all releases (unless they include `--disable-initial-rollout`), Cloud Deploy automatically creates a [rollout](https://docs.cloud.google.com/deploy/docs/terminology#rollout) resource too. And all phases of that rollout are executed, including render and deploy.

## View the results in Google Cloud console

After a few minutes, your deployment is complete. In this case, because the two custom actions are commands to echo strings into a file and upload the file to Cloud Storage, nothing is deployed into any target runtime.

However, you can view the file and the strings in that file:

  1. In the Google Cloud console, navigate to the Cloud Deploy **Delivery pipelines** page to view your delivery pipeline (`custom-targets-pipeline`).

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click the name of your delivery pipeline (`custom-targets-pipeline`).

The pipeline visualization shows the app's deployment status. Because there's only one stage in the pipeline, the visualization shows only one node.

![Delivery pipeline visualization showing success](https://docs.cloud.google.com/static/deploy/images/pipeline_custom_targets.png)

And your release is listed on the **Releases** tab under **Delivery pipeline details**.

  3. Click the release name.

The **Release details** page is shown.

  4. Click the **Artifacts** tab.

  5. Under **Target artifacts** , click the **VIEW ARTIFACTS** link.

The rendered manifest file is shown. In this case, the file is the output of the custom render action you defined in your custom target type configuration, containing the string "Sample manifest rendered content".

![Output of the custom render action](https://docs.cloud.google.com/static/deploy/images/custom_target_render_output.png)

  6. Find the **Cloud Storage** buckets created by this release. 

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)

The **Buckets** page is displayed, showing two buckets created for this release. One bucket contains the delivery pipeline configuration file and the rendered `skaffold.yaml`. The other includes the output file our custom action is configured to create.

  7. Click the bucket whose name starts with `us-central1.deploy-artifacts`...

![List of Cloud Storage buckets](https://docs.cloud.google.com/static/deploy/images/buckets-for-custom-targets.png)

  8. Click the folder whose name starts with `custom-targets-pipeline-`, then click the `test-release-001` folder.

  9. Click the folder whose name is your rollout name, which should be `test-release-001-to-sample-env-0001`.

  10. Click the folder shown, which is a UUID, then click the `custom-output` folder.

  11. Click `results.json`, then click the hyperlinked URL in the **Authenticated URL** field.

This file contains the string you configured as output from the `custom-deploy` action, in your custom target type definition:

![Output from deploy custom action](https://docs.cloud.google.com/static/deploy/images/custom-target-deploy-results.png)


**Note:** you can also see the **render** results in the Cloud Storage bucket, but it's quicker to use the release inspector, as shown in the first steps of this procedure.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the delivery pipeline, target, release, and rollout:
         
         gcloud deploy delete --file=clouddeploy.yaml --force --region=us-central1 --project=PROJECT_ID
         

  2. Delete both of the Cloud Storage buckets that Cloud Deploy created.

[Open the Cloud Storage browser page](https://console.cloud.google.com/storage/browser)




That's it, you completed this quickstart!

## What's next

  * [Learn more about custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets).

  * See the available [sample custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets#custom_target_examples).

  * [Learn more about Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).

  * [Learn the basics of deploying applications](https://docs.cloud.google.com/deploy/docs/deploying-application).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
