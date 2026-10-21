---
url: https://docs.cloud.google.com/build/docs/securing-builds/set-service-account-permissions/
title: Configure access for the default Cloud Build service account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:14:39.325606+00:00
---

# Configure access for the default Cloud Build service account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/set-service-account-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Configure access for the default Cloud Build service account Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We have introduced changes to the default service account used to run builds. As a best practice, we recommend that you [specify your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run your builds. For more information see [Cloud Build default service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

This page explains how to grant permissions to and revoke permissions from the [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

Note that the legacy Cloud Build service account is automatically granted the Cloud Build Service Account role for the project. The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) doesn't include this role. You can grant more permissions to whatever service account you're using.

## Before you begin

  * Understand [Cloud Build roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).
  * Read [Default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).



## Grant a role to the default Cloud Build service account using the Settings page

You can grant certain commonly used IAM roles to the default Cloud Build service account using the Cloud Build Settings page in the Google Cloud console:

  1. Open the Cloud Build Settings page:

[ Open the Cloud Build Settings page](https://console.cloud.google.com/cloud-build/settings)

You'll see the **Service account permissions** page:

![Screenshot of the Service account permissions page](https://docs.cloud.google.com/build/images/service-account-permissions.png)

  2. Use the drop-down menu to select the service account you want to update.

  3. Set the status of the role you want to add to **Enable**.




## Grant a role to the default Cloud Build service account using the IAM page

If the role you want to grant is not listed in the Cloud Build Settings page in the Google Cloud console, use the IAM page to grant the role:

  1. Open the IAM page:

[ Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select your Google Cloud project.

  3. Above the permissions table, select the **Include Google-provided role grants** checkbox.

You'll see that more rows appear in the permissions table.

  4. In the permissions table, find your default Cloud Build service account.

  5. Click the pencil icon.

  6. Select the role you want to grant to the Cloud Build service account.

  7. Click **Save**.




## Revoke a role from the Cloud Build service account

  1. Open the IAM page:

[ Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select your Google Cloud project.

  3. Above the permissions table, select the **Include Google-provided role grants** checkbox.

You'll see that more rows appear in the permissions table.

  4. In the permissions table, find your default Cloud Build service account.

  5. Click the pencil icon.

  6. Locate the role you want to revoke and click the delete trash can next to the role.




## Grant a role to the Cloud Build service agent

In addition to the Cloud Build default service account, Cloud Build has a _Cloud Build service agent_ that allows other Google Cloud services to access your resources. After you enable the Cloud Build API, the service agent is automatically created in the Google Cloud project. The service agent has the following format, where `PROJECT_NUMBER` is your project number.
    
    
         service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com
    

You can view the service agent for a project by going to the [IAM page in the Google Cloud console](https://console.cloud.google.com/iam-admin/iam) page and selecting the **Show google managed service accounts** checkbox.

If you've accidentally revoked the Cloud Build service agent's role on your project, you can grant it manually using the following steps:

###  Console 

  1. Open the **IAM** page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant access**.

  3. Add the following principal, where `PROJECT_NUMBER` is your project number:
         
         service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com
         

  4. Select **Service Agents** > **Cloud Build Service Agent** as your role.

  5. Click **Save**.




###  gcloud 

Grant `roles/cloudbuild.serviceAgent` IAM role to the Cloud Build service agent:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com" \
        --role="roles/cloudbuild.serviceAgent"
    

Replace the placeholder values in the command with the following:

  * `PROJECT_ID`: The project ID
  * `PROJECT_NUMBER`: The project number



## What's next

  * Learn about [user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).
  * Learn about [service accounts in depth](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).
  * Learn about [configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).
  * Learn about [the permissions required to view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
