---
url: https://docs.cloud.google.com/tasks/docs/secure-queue-configuration/
title: Secure queue configuration \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:51.106341+00:00
---

# Secure queue configuration  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/secure-queue-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Secure queue configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides suggestions for securing queue creation and configuration. The key is to restrict queue management methods to a small set of people or entities. For large organizations, it might be necessary to use a service account to run software that enforces proper queue configuration.

The general idea is to separate users and other entities into three categories:

  1. **Queue Admins** \- Users in this group have permission to call Cloud Tasks queue management methods, or to upload `queue.yaml` files. This group is restricted to a very **small** set of users so as to reduce the risk of clobbering queue configuration, particularly by inadvertently mixing `queue.yaml` and Cloud Tasks queue management methods.
  2. **Cloud Tasks Workers** \- Users in this group have permission to perform common interactions with Cloud Tasks such as enqueuing and dequeuing tasks. They are **not** allowed to call Cloud Tasks queue management methods.
  3. **App Engine Deployers** \- For projects that have App Engine apps, users in this group have permission to deploy the app. They are **not** permitted to upload `queue.yaml` files or make any Cloud Tasks API calls, thus allowing the queue admins to enforce the proper policies.



In this scheme, users who are queue admins should not also be Cloud Tasks workers, since that would defeat the purpose of the separation.

If your project uses Cloud Tasks queue management methods exclusively, it might also make sense that queue admins should not also be App Engine deployers, since this would make it possible for an errant `queue.yaml` file to be uploaded.

## Small projects and organizations

Small projects and organizations can assign [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles) directly to users to place them into the groups above. This makes sense for teams who prefer configuration simplicity or who make queue configuration changes or App Engine app deployments by hand.

Add users to these groups as follows:

### Queue Admin

  1. As a project admin, grant the `cloudtasks.queueAdmin` role to users who are allowed to make Cloud Tasks queue management API calls or upload `queue.yaml` files.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member user:EMAIL \
         --role roles/cloudtasks.queueAdmin

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `EMAIL`: the email for the member user
  2. As a user with the `cloudtasks.queueAdmin` role, following the best practices above, choose **one** of the following methods for changing the queue configuration.

     1. Use Cloud Tasks API to change queue configuration.

     2. Upload `queue.yaml` with `gcloud`:
            
            gcloud app deploy queue.yaml




### Cloud Tasks Worker

As there are often many users allowed to interact with Cloud Tasks, you can assign roles to [Service Accounts](https://docs.cloud.google.com/iam/docs/service-accounts) instead of individual users. This type of usage is common in production. For more information, see Large projects and organizations.

  1. As a project admin, grant roles to users who are allowed to interact with Cloud Tasks but not change queue configuration:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.viewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.enqueuer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.dequeuer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.taskRunner
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.taskDeleter

Replace `PROJECT_ID` with the ID of your project.




As a user with one or more of the roles granted above, you can interact with the Cloud Tasks API.

### App Engine Deployer

  1. As a project admin, grant roles to users who are allowed to deploy App Engine apps but who are not allowed to modify queue configuration or interact with tasks:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member user:EMAIL \
         --role roles/appengine.deployer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member user:EMAIL \
         --role roles/appengine.serviceAdmin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member user:EMAIL \
         --role roles/storage.admin

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `EMAIL`: the email for the member user
  2. As a user with the roles granted above, deploy an App Engine app.
         
         gcloud app deploy app.yaml




## Large projects and organizations

Large projects and organizations can use [Service Accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to separate duties and responsibilities. This makes sense for teams with complex infrastructure for changing queue configuration and perhaps also deploying App Engine apps.

To follow the principle of least privilege and simplify access management, these instructions use service account impersonation. To learn more about this pattern, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) in the Google Cloud authentication documentation.

**Caution:** If queues are removed from `queue.yaml`, they enter the `DISABLED` state and only queue admins can delete them. Since there is no way to delete queues programmatically in the App Engine SDK, your tool would have to delete them via a Cloud Tasks `DeleteQueue` call.

Instructions for setting up these service accounts follow.

### Queue Admin

  1. As a project admin, create the service account.
         
         gcloud iam service-accounts create queue-admin \
         --display-name "Queue Admin"

  2. Grant the `cloudtasks.queueAdmin` role to the service account so that it can upload `queue.yaml` files and make Cloud Tasks queue management API calls.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:queue-admin@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.queueAdmin

Replace `PROJECT_ID` with the ID of your project.

  3. Selectively allow impersonation of the "Queue Admin" service account that you created.

This should usually be a small group of principals who act as queue administrators. Grant these principals the [`iam.serviceAccountTokenCreator`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role on the "Queue Admin" service account that you created. To learn how, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) in the IAM documentation.

  4. Following the best practices described in [Use Queue Management or queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml), choose one of the following methods for changing the queue configuration:

     * Use Cloud Tasks to change queue configuration.

     * Upload `queue.yaml` with the gcloud CLI




### Cloud Tasks Worker

  1. As a project admin, create the service account.
         
         gcloud iam service-accounts create cloud-tasks-worker \
         --display-name "Cloud Tasks Worker"

  2. Grant roles to the service account so that it can interact with Cloud Tasks but not change queue configuration.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.viewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.enqueuer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.dequeuer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.taskRunner
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/cloudtasks.taskDeleter

Replace `PROJECT_ID` with the ID of your project.

  3. Selectively allow impersonation of the "Cloud Tasks Worker" service account you created.

For principals who interact with Cloud Tasks, grant the [`iam.serviceAccountTokenCreator`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role on the "Cloud Tasks Worker" service account you created. To learn how, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) in the IAM documentation.




### App Engine Deployer

  1. As a project admin, create the service account.
         
         gcloud iam service-accounts create app-engine-deployer \
         --display-name "App Engine Deployer"

  2. Grant roles to the service account so that it can deploy App Engine apps but not `queue.yaml`.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:app-engine-deployer@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/appengine.deployer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:app-engine-deployer@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/appengine.serviceAdmin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:app-engine-deployer@PROJECT_ID.iam.gserviceaccount.com \
         --role roles/storage.admin

Replace `PROJECT_ID` with the ID of your project.

  3. Selectively allow impersonation of the "App Engine Deployer" service account that you created.

For principals who deploy App Engine services, grant the [`iam.serviceAccountTokenCreator`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role on the "App Engine Deployer" service account that you created. To learn how, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) in the IAM documentation.




## Limiting access to single queues

If you have multiple queues in a project and want to limit access to individual queues, you can use IAM policies at the queue level instead of the project level. To limit access by queue, use the [`gcloud tasks queues add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/add-iam-policy-binding) command. For example:
    
    
      gcloud tasks queues add-iam-policy-binding QUEUE_NAME --location=LOCATION \
      --member=serviceAccount:cloud-tasks-worker@PROJECT_ID.iam.gserviceaccount.com \
      --role=roles/cloudtasks.enqueuer

Replace the following:

  * `QUEUE_NAME`: the name of your queue
  * `LOCATION`: the location of your queue
  * `PROJECT_ID`: the ID of your project



## What's next

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Understanding service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)
  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts)
  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
