---
url: https://docs.cloud.google.com/run/docs/manually-set-up-continuous-deployment/
title: Manual setup continuous deployment using Cloud Build \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:03.610384+00:00
---

# Manual setup continuous deployment using Cloud Build  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/manually-set-up-continuous-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)



Send feedback 

#  Manual setup continuous deployment using Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

The following instructions assume you have a git repository with a `Dockerfile` at its root. 

To automate deployment from Git with Cloud Build:

  1. Construct a Cloud Build configuration that:

     * Builds the container image
     * Pushes the image to the Container Registry [(Deprecated)](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)
     * Deploys a new revision to the Cloud Run service

To do this, add a file named `cloudbuild.yaml` _at the root of your repository_ with this content:
    
    steps:
     # build the container image
     - name: 'gcr.io/cloud-builders/docker'
       args: ['build', '-t', 'gcr.io/$PROJECT_ID/[SERVICE-NAME]:$COMMIT_SHA', '.']
     # push the container image to Container Registry
     - name: 'gcr.io/cloud-builders/docker'
       args: ['push', 'gcr.io/$PROJECT_ID/[SERVICE-NAME]:$COMMIT_SHA']
     # Deploy container image to Cloud Run
     - name: 'gcr.io/cloud-builders/gcloud'
       args:
       - 'run'
       - 'deploy'
       - '[SERVICE-NAME]'
       - '--image'
       - 'gcr.io/$PROJECT_ID/[SERVICE-NAME]:$COMMIT_SHA'
       - '--region'
       - '[REGION]'
     images:
     - 'gcr.io/$PROJECT_ID/[SERVICE-NAME]:$COMMIT_SHA'
    

Replace

     * [SERVICE-NAME] with the name of the Cloud Run service.
     * [REGION] with the region of the Cloud Run service you are deploying.

The use of the `$COMMIT_SHA` substitution variable is populated by Cloud Build when triggered from a Git repository.

  2. Grant the _Cloud Run Admin_ and _Service Account User_ roles to the Cloud Build service account:

     1. Open the Cloud Build settings page in the Google Cloud console:

[Visit the Cloud Build settings page](https://console.cloud.google.com/cloud-build/settings)

     2. In the Service account permissions panel, set the status of the _Cloud Run Admin_ role to **Enable** :

![Screenshot of the Service account permissions page](https://docs.cloud.google.com/build/images/service-account-permissions.png)

     3. Select **GRANT ACCESS TO ALL SERVICE ACCOUNTS** to grant the **Service Account User** role on all service accounts in the project on your page.

**Note:** For stronger security, only allow Cloud Build to act as a specific Cloud Run service.
  3. Click **Triggers** in the left navigation panel to open the _Triggers_ page:

[Visit the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

     1. Click **Create Trigger**.
     2. In the **Name** field, enter a name for your trigger.
     3. Under **Event** , select the repository event to start your trigger.
     4. Under **Source** , select your repository and the branch or tag name that will start your trigger. For more information on specifying which branches to autobuild, see [Creating a build trigger](https://docs.cloud.google.com/build/docs/running-builds/automate-builds#build_trigger).
     5. Under **Cloud Build configuration file (yaml or json)** , select **Cloud Build configuration file**.
     6. In the **Cloud Build configuration file location** field, type `cloudbuild.yaml` after the `/`.
     7. Click **Create** to save your build trigger.
  4. You are finished! From now on, whenever you push to your repository, a build and a deployment to your Cloud Run service is automatically invoked.


**Note:** To make the deployed service public, make a one-time change to the [service IAM settings](https://docs.cloud.google.com/run/docs/securing/managing-access#making_a_service_public).

## Continuous deployment with minimal IAM permissions

When a container is deployed to a Cloud Run service, it runs with the identity of the Runtime Service Account of this Cloud Run service. Because Cloud Build can deploy new containers automatically, Cloud Build needs to be able to _act as_ the [Runtime Service Account of your Cloud Run service](https://docs.cloud.google.com/run/docs/securing/service-identity).

To grant limited access to Cloud Build to deploy to a Cloud Run service:

### Console UI

  1. Go to the **Service accounts** page of the Google Cloud console: 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click the email address of your Cloud Run service's Runtime Service Account of your Cloud Run (by default, it is `PROJECT_NUMBER-compute@developer.gserviceaccount.com`).

  3. Click the **Principals with access** tab.

  4. Click person_add **Grant access**.

  5. Enter the Cloud Build Service Account (`PROJECT_NUMBER@cloudbuild.gserviceaccount.com`)

  6. In the **Select a role** dropdown, select the **Service Accounts** > **Service Account User** role.

  7. Click **Save**.




###  gcloud 

Use the `gcloud iam service-accounts add-iam-policy-binding` command:
    
    
    gcloud iam service-accounts add-iam-policy-binding \
      PROJECT_NUMBER-compute@developer.gserviceaccount.com \
      --member="serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com" \
      --role="roles/iam.serviceAccountUser"

Replace PROJECT_NUMBER with the numeric ID of your project.

If using Cloud Run using a [customized service identity](https://docs.cloud.google.com/run/docs/securing/service-identity#per-service-identity), replace `PROJECT_NUMBER-compute@developer.gserviceaccount.com` with your service account address.

See [Deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) for more information.

## What's Next

  * Learn how deploy or publish a container image to a private registry in another project in [Setting service account permissions](https://docs.cloud.google.com/build/docs/securing-builds/set-service-account-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
