---
url: https://docs.cloud.google.com/application-design-center/docs/grant-roles-service-account/
title: Grant roles to your service account \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:07.952045+00:00
---

# Grant roles to your service account  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/grant-roles-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Grant roles to your service account Stay organized with collections  Save and categorize content based on your preferences. 

When developers [preview and deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-from-console), they can use an existing [service account](https://docs.cloud.google.com/iam/docs/service-account-overview), or App Design Center can automatically create a new service account.

To deploy using your own service account, you must grant the necessary Identity and Access Management roles and permissions. This document shows you how to grant roles and configure your service account, including the following:

  * Add IAM policy bindings to the service account and user account.
  * Grant the service account the [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) required to deploy each resource.
  * Add permissions to the service account to deploy outside of the project where the service account was created.
  * Update your organization policies to allow service accounts to be used across projects.



## Configure your service account

To configure your service accounts, do the following:

  1. Add an IAM policy binding for the `roles/iam.serviceAccountUser` role for the service agent to your service account:
         
         gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
             --member="serviceAccount:service-SERVICE_ACCOUNT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
             --role="roles/iam.serviceAccountUser"
         

Replace the following:

     * `SERVICE_ACCOUNT_EMAIL`: Your service account email. For example, `my-service-account@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`.
     * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your service account.
     * `SERVICE_ACCOUNT_PROJECT_NUMBER`: The project number of the project that contains your service account.
  2. Add an IAM policy binding for the role of `roles/iam.serviceAccountUser` for a user to your service account:
         
         gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
             --member="user:USER_EMAIL" \
             --role="roles/iam.serviceAccountUser"
         

Replace the following:

     * `SERVICE_ACCOUNT_EMAIL`: Your service account email. For example, `my-service-account@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`.
     * `USER_EMAIL`: The user email for the user who performs the deployment.
  3. In the project that has your service account, add IAM policy bindings for the required service agent roles on the [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) that contains your space:
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:service-MANAGEMENT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
             --role="roles/apphub.editor"
         
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:service-MANAGEMENT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
             --role="roles/config.agent"
         
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:service-MANAGEMENT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
             --role="roles/serviceusage.serviceUsageAdmin"
         

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your service account.
     * `MANAGEMENT_PROJECT_NUMBER`: The project number of the [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) that contains your space.
  4. In the project that has your service account, ensure that the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint is not enforced. This constraint is enforced by default.

To disable enforcement of the organization policy constraint, run the following command:
         
         gcloud resource-manager org-policies disable-enforce \
            iam.disableCrossProjectServiceAccountUsage \
            --project=SERVICE_ACCOUNT_PROJECT_ID
         

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your service account.
  5. Grant your service account the roles required to deploy resources in projects. The required roles are displayed when developers [deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-from-console).

For example, to grant the `roles/run.admin` role, add the following policy binding:
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:service-DEPLOYMENT_PROJECT_NUMBER@gcp-sa-designcenter.iam.gserviceaccount.com" \
             --role="roles/run.admin"
         

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your service account.
     * `DEPLOYMENT_PROJECT_NUMBER`: The project number of the project where you're deploying resources.
  6. App Design Center uses Infrastructure Manager to deploy applications in the console. To use your own service account to deploy with Infrastructure Manager, complete the steps in [Grant access across multiple projects](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account#grant_access_across_multiple_projects).

  7. If the application you're deploying contains private components that you imported through a Developer Connect connection, do the following:

Grant your service account the `roles/iam.serviceAccountTokenCreator` role on the project where you created the service account.
         
         gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role="roles/iam.serviceAccountTokenCreator"
         

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: The project ID of the project that contains your service account.
     * `SERVICE_ACCOUNT_EMAIL`: Your service account email. For example, `my-service-account@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`.



## What's next

  * Learn how to update, scale, and delete your resources by [managing applications](https://docs.cloud.google.com/application-design-center/docs/manage-applications).
  * Provision your infrastructure with the console or the command line by [deploying applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
