---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/iam/
title: Access control with IAM (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.745058+00:00
---

# Access control with IAM (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/iam/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM (1st gen)

You (that is, the user or service account deploying the function) can set access control using roles at the project level. Grant a role to a project member or service account to determine the level of access to your Google Cloud project and its resources. By default, all Google Cloud projects come with a single user: the original project creator. No other users have access to the project, and therefore, access to functions, until a user is added as a project team member.

## Access control for users

You can add users as team members to your project and grant them roles using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview).

Cloud Run functions supports the [basic roles](https://docs.cloud.google.com/iam/docs/understanding-roles#bas8c) of **Editor** , **Owner** , and **Viewer** , which give the following permissions:

  * **Editor** and **Owner** : Read and write access to all functions-related resources. Lets users deploy, update, and delete functions. Additional access to other resources in the project.
  * **Viewer** : Read-only access to functions and locations. Lets users list functions and see their details, but does not let them view the source code. Additional access to other resources in the project.



Cloud Run functions also supports the Cloud Run functions [predefined **Developer** and **Viewer** roles](https://docs.cloud.google.com/functions/docs/reference/iam/roles), which give the following permissions:

  * **Developer** : Read and write access to all functions-related resources. Lets users deploy, update, and delete functions. No access to other resources in the project.
  * **Viewer** : Read-only access to functions and locations. Lets users list functions and see their details, but does not let them view the source code. No access to other resources in the project.

**Note:** To write or access Cloud Run functions logs, a project member must also have the appropriate logging permissions. For more information, see the [Cloud Logging access control guide](https://docs.cloud.google.com/logging/docs/access-control).

## Access control for service accounts

A [service account](https://docs.cloud.google.com/iam/docs/service-account-types) is a special type of Google Cloud account that acts as an identity for a non-human user that needs to authenticate and be authorized to access data and perform various actions. Some of these accounts are [created and managed by Google itself](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) and are known as [_service agents_](https://docs.cloud.google.com/iam/docs/service-agents).

The following service accounts are used for Cloud Run functions:

Name | Member ID | Role  
---|---|---  
App Engine default service account | `PROJECT_ID@appspot.gserviceaccount.com` | Editor  
Google Cloud Run functions Service Agent | `service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com` | Cloud Run functions Service Agent  
— | `PROJECT_NUMBER@cloudbuild.gserviceaccount.com` | Cloud Build Service Account  
Cloud Build Service Account | `service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com` | Cloud Build Service Agent  
Google Container Registry Service Agent | `service-PROJECT_NUMBER@containerregistry.iam.gserviceaccount.com` | Container Registry Service Agent  
Artifact Registry Service Agent | `service-PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com` | Artifact Registry Service Agent  
  
### Runtime service accounts

At runtime, Cloud Run functions defaults to using the App Engine default service account (`PROJECT_ID@appspot.gserviceaccount.com`), which has the **Editor** role on the project. You can change the role of this service accounts to limit or extend the permissions for your running functions. You can also change which service account is used by [providing a non-default individual service account](https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity#individual).

To learn more about service accounts, see the [service accounts documentation](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).

**Note:** Authenticating as the runtime service account from inside your function might fail if you change the Cloud Run functions service account's permissions.

### Administrative service accounts

To perform administrative actions on your project during the creation, updating, or deletion of functions, all projects in Cloud Run functions require the Google Cloud Run functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`).

In addition, all runtimes carry out container image building and storage within your project. To support this, you also need to provision the following:

  * The basic [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) (`PROJECT_NUMBER@cloudbuild.gserviceaccount.com`)
  * The [Cloud Build Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-build-service-agent) (`service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com`)
  * The [Google Container Registry Service Agent service account](https://docs.cloud.google.com/container-registry/docs/overview#container_registry_service_account) (`service-PROJECT_NUMBER@containerregistry.iam.gserviceaccount.com`)



These service accounts should have the roles listed in the earlier table.

#### Google Cloud Run functions Service Agent service account

By default, the Google Cloud Run functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com` has the **cloudfunctions.serviceAgent** role on your project.

**Warning:** If you remove the default role binding or modify the permissions granted to the Cloud Run functions Service Agent service account on your Google Cloud project, the Cloud Run functions create, update, and delete operations might fail.

Here's a few of the notable permissions that the `cloudfunctions.serviceAgent` uses:

Permission | Description  
---|---  
`roles/artifactregistry.admin` | Manage repositories and store build images in Artifact Registry.  
`roles/cloudbuild.builds.editor` | Required to use Cloud Build to perform builds in user project.  
`roles/cloudbuild.customworkers.builder` | Create builds in Cloud Build custom workers.  
`cloudfunctions.functions.invoke` | Invoke an IAM-guarded HTTP function.  
`compute.globalOperations.get`,  
`compute.networks.access`,  
`vpcaccess.connectors.{get, use}` | Provision functions with access to the consumer projects VPC.  
`firebasedatabase.instances.{get, update}` | Create functions triggered by the Firebase Realtime Database.  
`iam.serviceAccounts.{actAs, getAccessToken, signBlob}` | Ability to get runtime service account credentials.  
`iam.serviceAccounts.getOpenIdToken` | Needed for the agent to get an OpenID token on a user-specified authority. OpenID token is used for invoking IAM-enabled functions.  
`pubsub.subscriptions` | Manage subscriptions in the user's project.  
`pubsub.topics` | Manage topics in the user's project.  
`storage.buckets.{get, update}` | Configure notifications on a Cloud Storage bucket that trigger a function.  
`storage.buckets.create`,  
`storage.objects.{delete, get, create, list}` | Required for storing source code in user project.  
  
You can see the entire set of permissions under the [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) or by running this command: 
    
    
    gcloud iam roles describe roles/cloudfunctions.serviceAgent

You can reset this service account to the default role by removing whatever role it has and adding the Cloud Run functions Service Agent role:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member serviceAccount:service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com \
      --role roles/cloudfunctions.serviceAgent

## Troubleshooting permission errors

If you get permission errors when you deploy, update, delete, or execute functions in your project, perform the following steps:

  1. Make sure that you have the **Editor** or **Owner** role on your project, or that you are using the **Cloud Run functions Developer** role.

If you are using the **Cloud Run functions Developer** role at the project level, also ensure that you have [granted the user the **IAM Service Account User** role](https://docs.cloud.google.com/functions/docs/reference/iam/roles#additional-configuration).

Only execution permissions are allowed at the per-function level.

  2. Verify that the Cloud Run functions Service Agent service account (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`) has the **cloudfunctions.serviceAgent** role for your project.

Make sure the **Include Google-provided role grants** box on the **Permissions** tab of the [Console IAM](https://console.cloud.google.com/iam-admin/iam/) page is checked to see this account. Or you can use `gcloud projects add-iam-policy-binding PROJECT_ID`.

  3. Ensure that you have permissions for trigger sources, such as [Pub/Sub](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) or [Cloud Storage](https://docs.cloud.google.com/functions/1stgendocs/calling/storage).




If you get an ”insufficient permissions” error, or have other authentication problems when you run your functions, make sure that the runtime service account has the correct permissions to access the resources your functions need. Then, repeat steps 2 and 3.

If you get a ”service unavailable” error during deployment, make sure that the runtime service account `PROJECT_ID@appspot.gserviceaccount.com` exists in your project. To recreate this service account if it was deleted, see [Undeleting a service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting).

See also [Troubleshooting Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
