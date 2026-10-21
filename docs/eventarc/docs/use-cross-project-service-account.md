---
url: https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/
title: Support a cross-project service account \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:52.727196+00:00
---

# Support a cross-project service account  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Support a cross-project service account Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Every Eventarc trigger is associated with an Identity and Access Management (IAM) service account at the time the trigger is created. The trigger uses the service account as its default identity.

By default, you can't create an IAM service account in one Google Cloud project and attach it to a resource in another project. However, you might have centralized the service accounts for your organization in separate projects, which can make the service accounts easier to manage. This document outlines the steps required to support attaching a service account in one project to an Eventarc trigger in another project.

If you don't have the permissions to perform these steps, ask an administrator to complete them.

**Note:** Cross-project triggers are not supported. The service that receives the events from the trigger must be in the same Google Cloud project as the trigger. If the events that are sent to your service are triggered by messages published to a Pub/Sub topic, the topic must also be in the same project as the trigger. For more information, see [Route events across Google Cloud projects](https://docs.cloud.google.com/eventarc/docs/cross-project-triggers).

## Enable cross-project service account usage

Complete the following steps in the service account project.

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. If the **Disable Cross-Project Service Account Usage** policy is enforced, you must [disable it](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

For more information, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

  3. [Create your service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) and note its name.




## Grant permissions for service account authentication

Principals can use service accounts to authenticate in a few different ways. Each type of authentication requires the principal to have specific IAM permissions on the service account. For more information, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).

**Note:** When managing access for users in [external identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), replace instances of Google Account principal identifiers—like `user:kiran@example.com`, `group:support@example.com`, and `domain:example.com`—with appropriate [Workforce Identity Federation principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 

  1. Grant the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role to the Eventarc service agent of the Google Cloud project that contains the trigger. This permits the service agent to manage the cross-project access for the service account. A service agent is the identity of a given Google Cloud service for a particular project. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).

### Console

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the project that owns the service account that you will attach to the Eventarc trigger.

     3. Click the email address of the service account that you previously created.

     4. Click the **Principals with access** tab.

     5. Click person_add **Grant access**.

     6. In the **New principals** field, enter the email address of the Eventarc service agent:
            
            service-EVENTARC_PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com

Replace `EVENTARC_PROJECT_NUMBER` with the Google Cloud project number of the project that contains the trigger.

     7. Click **Add another role**.

     8. In the **Select a role** list, filter for **Service Account Token Creator** , and then select the role.

     9. Click **Save**.

### gcloud

Run the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    gcloud iam service-accounts add-iam-policy-binding \
        SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
        --member='serviceAccount:service-EVENTARC_PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com' \
        --role='roles/iam.serviceAccountTokenCreator'

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID of the project that owns the service account
     * `EVENTARC_PROJECT_NUMBER`: the Google Cloud project number of the project that contains the trigger

  2. Grant the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) IAM role to all principals who create triggers—for example, the Eventarc service agent of the Google Cloud project that contains the trigger. This predefined role contains the `iam.serviceAccounts.actAs` permission, which is required to attach a service account to a resource.

### Console

Grant the role on the project to allow the principal to impersonate multiple service accounts:

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Select the project that owns the service account.

     3. Click person_add **Grant access**.

     4. In the **New principals** field, enter the email address of the principal.

     5. In the **Select a role** list, filter for **Service Account User** , and then select the role.

     6. Click **Save**.

Or, grant the role on the service account to allow the principal to impersonate only a specific service account:

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the project that owns the service account.

     3. Click the email address of the service account that you previously created.

     4. Click the **Permissions** tab.

     5. In the **Principals with access to this service account** section, click person_add **Grant access**.

     6. In the **New principals** field, enter the email address of the principal.

     7. Click **Add another role**.

     8. In the **Select a role** list, filter for **Service Account User** , and then select the role.

     9. Click **Save**.

### gcloud

Run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command and grant the role on the project to allow the principal to impersonate multiple service accounts:
    
    gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
        --member=PRINCIPAL \
        --role='roles/iam.serviceAccountUser'

Or, run the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command and grant the role on the service account to allow the principal to impersonate only a specific service account:
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_RESOURCE_NAME \
        --member=PRINCIPAL \
        --role='roles/iam.serviceAccountUser'

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID of the project that owns the service account
     * `PRINCIPAL`: an identifier for the trigger creator in the format `user|group|serviceAccount:email` or `domain:domain`. For example: 
       * `user:test-user@gmail.com`
       * `group:admins@example.com`
       * `serviceAccount:test123@example.domain.com`
       * `domain:example.domain.com` m
     * `SERVICE_ACCOUNT_RESOURCE_NAME`: the full resource name of the service account. For example:

`projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com`

Where:

       * `SERVICE_ACCOUNT_PROJECT_ID` is the Google Cloud project ID that owns the service account
       * `SERVICE_ACCOUNT_NAME` is the name of your service account




## Grant permissions to support event routing

Before creating an Eventarc trigger, you must grant other IAM permissions to support routing events using Eventarc.

  1. Grant the appropriate permissions based on what resources the Eventarc trigger must access to do its work, and the event provider and destination. For more information see [All roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions).

  2. [Create your trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) using the cross-project service account.

**Note:** You can't use the Google Cloud console to attach a cross-project service account when creating a trigger. Instead, use the [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) command or the [`projects.locations.triggers.create`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers/create) method to create your trigger.



## What's next

  * [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview)
  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
