---
url: https://docs.cloud.google.com/deploy/docs/deploy-app-in-console/
title: Quickstart: Create a pipeline and release in the Google Cloud console \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:00.936297+00:00
---

# Quickstart: Create a pipeline and release in the Google Cloud console  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploy-app-in-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a pipeline and release in the Google Cloud console

This page shows you how to use the Google Cloud console to create a Cloud Deploy delivery pipeline, and then create a release for that pipeline.

In this quickstart, you'll do the following:

  1. Create two GKE clusters or configure two Cloud Run services.

  2. Create a [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology/delivery_pipeline) and two [targets](https://docs.cloud.google.com/deploy/docs/terminology/target) using the Google Cloud console.

  3. Instantiate your delivery pipeline by creating a release using the Google Cloud console.

After you create this release, the application is automatically deployed to the target.

  4. See the results in Google Cloud console.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Deploy, Cloud Build, GKE, Artifact Registry, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-in-console)

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

  10. Enable the Cloud Deploy, Cloud Build, GKE, Artifact Registry, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com,run.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/deploy/docs/deploy-app-in-console)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

If you already have the CLI installed, make sure you're running the latest version: 
    
    gcloud components update
    




## Create your runtime environment

**If you're deploying to Cloud Run, you can skip this command**. 

For GKE, create two clusters: `quickstart-cluster-for-console-staging` and `quickstart-cluster-for-console-prod`, with default settings. The clusters' Kubernetes API endpoints must be network-reachable from the public internet. GKE clusters are externally accessible by default.
    
    
    gcloud container clusters create-auto quickstart-cluster-for-console-staging \
                     --project=PROJECT_ID \
                     --region=us-central1 && \
    gcloud container clusters create-auto quickstart-cluster-for-console-prod \
                     --project=PROJECT_ID \
                     --region=us-central1
    

## Create a delivery pipeline and two targets

You can use Cloud Deploy to [create a delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets) based on configuration specified in one or more YAML files. But you can also create a delivery pipeline using the Google Cloud console. 

In this section, you use Google Cloud console to create a delivery pipeline and two targets. When you use Google Cloud console, you don't need to create any YAML files; Cloud Deploy creates your [skaffold.yaml](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold) and manifest for you.

  1. In the Google Cloud console, navigate to the Cloud Deploy main page. 

[Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines)

  2. Click **Create**

![Cloud Deploy main page in the Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/pipelines-empty-state-create.png)

The **Create a delivery pipeline** form is displayed.

  3. In the **Pipeline name** field, replace the default text with `in-console-quickstart-pipeline`.

  4. Optionally, enter a description for this delivery pipeline.

  5. In the **Region** drop-down, select `us-central1`.

  6. Select your runtime.

If you're deploying to GKE, select **Google Kubernetes Engine**. Otherwise, select **Cloud Run**.

  7. Create your targets:

###  GKE 

     1. Under **New target** , in the **Target name** field, replace the default text with `console-staging`.

     2. From the **Kubernetes Engine cluster** drop-down, select `quickstart-cluster-for-console-staging`.

     3. Click **Done**.

     4. Click **Add target**.

Replace the default text for **Target name** with `console-prod`.

     5. Select `quickstart-cluster-for-console-prod` from the **Kubernetes Engine cluster** drop-down.

     6. Select **Require approval for rollouts**.

For this quickstart, we're requiring approval on the second target but not on the first target.

     7. Click **Create** to create this delivery pipeline.

![Cloud Deploy main page in the Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/completed-create-pipeline-form-gke.png)

###  Cloud Run 

     1. Under **New target** , in the **Target name** field, replace the default text with `console-staging`.

     2. From the **Region** drop-down, select `us-central1`.

     3. Click **Done**.

     4. Click **Add target**.

     5. Replace the default text for **Target name** with `console-prod`.

     6. Activate the **Require approval for rollouts** checkbox for this target.

For this quickstart, we're requiring approval on the second target but not on the first target.

     7. Click **Create** to create this delivery pipeline.

![Cloud Deploy main page in the Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/completed-create-pipeline-form-run.png)

**Note:** If the default Compute Engine service account doesn't have the necessary permissions, you can click the **Grant** button to add them, when prompted.

You now have a delivery pipeline with two targets, ready to create a release.  
The pipeline's page is displayed, showing both targets, with no rollouts.

![New delivery pipeline, created in the Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/new-pipeline-created-in-console.png)




## Create a release

Now that you have a delivery pipeline, with two targets, pointing to two GKE clusters or two Cloud Run services, you can create a release to deploy your application to the first target.

  1. If you're not already on the delivery pipeline page, showing the new delivery pipeline `in-console-quickstart-pipeline`, navigate there now.

The pipeline visualization is shown, with no rollouts.

  2. Click the **Create release** button.

The **Create a release** dialog is shown. Most of the fields are pre-populated. Keep these default values.

![The **Create a Release** dialog](https://docs.cloud.google.com/static/deploy/images/create-release-initial.png)

You can click the **View manifest** button to view the manifest the automatically generated manifest, for either target, and you can click **View Skaffold file** to view the generated `skaffold.yaml`. You can also edit them, but for this quickstart leave them as they are.

  3. Optionally, add a description for this release, in the **Description** field.

  4. Click **Create** to start the release.

The rollout details page is shown, for the rollout to the first target, and you can watch the progress of this rollout. It will take a few minutes to complete. It may take a few seconds for the rollout to start.

  5. After the first rollout finishes, click the delivery pipeline name to go to the delivery pipeline page. 

![Click the pipeline name to view the visualization](https://docs.cloud.google.com/static/deploy/images/in-console-qs-click-pipeline-name.png)

The pipeline visualization is shown, with the rollout complete to the first target.

![Delivery pipeline visualization with first target complete](https://docs.cloud.google.com/static/deploy/images/in-console-pipeline-viz1.png)

  6. Click **Promote** to start the rollout to the next target.

The **Promote** dialog is shown.

  7. Keep the default values, add a **Rollout description** if you want, then click **Promote**.

Because we selected **Require approval for rollouts** when we created the second target, this promotion is waiting for approval.

  8. Click **Review** , in the delivery pipeline visualization.

The approval page is shown.

![Required approval for promotion to second target](https://docs.cloud.google.com/static/deploy/images/in-console-approval.png)

  9. Click **Review** again, and in the approval dialog, click **Approve**.

The rollout is started for the second target. You can click the delivery pipeline name again to watch the progress in the pipeline visualization.




When the second rollout is finished, the application is deployed in the second target, and your delivery pipeline has completed.

![Completed delivery pipeline.](https://docs.cloud.google.com/static/deploy/images/in-console-pipeline-complete.png)

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the GKE clusters or Cloud Run services:

###  GKE 
         
         gcloud container clusters delete quickstart-cluster-for-console-staging --region=us-central1 --project=PROJECT_ID \
         && gcloud container clusters delete quickstart-cluster-for-console-prod --region=us-central1 --project=PROJECT_ID
         

###  Cloud Run 
         
         gcloud run services delete in-console-quickstart-pipeline-target-1 --region=us-central1 --project=PROJECT_ID \
         && gcloud run services delete in-console-quickstart-pipeline-target-2 --region=us-central1 --project=PROJECT_ID
         

  2. From the delivery pipeline page, click **Delete** to delete the delivery pipeline, the release, and rollouts.

Type the pipeline name in the field provided, and click **Confirm** to finish deleting the resources.

![Confirmation dialog to delete pipeline and child resources. target](https://docs.cloud.google.com/static/deploy/images/in-console-confirm-delete-pipeline.png)

  3. Delete both targets:
         
         gcloud deploy targets delete console-staging --region=us-central1  && \
         gcloud deploy targets delete console-prod --region=us-central1
         

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
