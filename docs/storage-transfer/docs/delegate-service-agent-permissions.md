---
url: https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions/
title: Delegate service agent permissions to a user-managed service account \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:32.553652+00:00
---

# Delegate service agent permissions to a user-managed service account  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Delegate service agent permissions to a user-managed service account Stay organized with collections  Save and categorize content based on your preferences. 

For agentless transfers, Storage Transfer Service by default uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to transfer your data between the source and the destination. You grant permissions to the service agent to access your Cloud Storage buckets.

Because the same Storage Transfer Service service agent is used by all transfers within a project, it necessarily has permissions on _all_ of the buckets involved in every transfer.

As an alternative, you can assign bucket permissions to multiple user-managed service accounts instead. These user-managed service accounts are granted permissions on specific source and destination buckets, and are also restricted to specific user accounts (the accounts creating or triggering the transfer job).

## Example scenarios

The following scenarios demonstrate different permission options using the service agent and user-managed service accounts.

Expand each section to see the details.

### Scenario 1: Service agent only

In this scenario, all permissions are granted to the service agent.

  * The service agent is granted write permissions on buckets A, B, C, and D.



Any user with the correct permissions to create a transfer job can transfer into or out of buckets A, B, C, and D.

This works well when the Storage Transfer Service user is a trusted user for the data in all buckets, and can configure transfer jobs correctly to avoid moving data into or out of the wrong bucket.

### Scenario 2: User-managed service agents only

In this scenario, all permissions are granted to user-managed service accounts.

  * User-managed service account #1 is granted permissions on buckets A and B.
  * User-managed service account #2 is granted permissions on buckets C and D.



Furthermore:

  * User Alpha is granted access to service account #1.
  * User Bravo is granted access to service account #2.
  * User Charlie is granted access to service accounts #1 and #2.



In this case:

  * Alpha can transfer between buckets A and B only.
  * Bravo can transfer between buckets C and D only.
  * Charlie can transfer between buckets A and B, and between C and D, only.
  * Charlie can **not** transfer between A and C, A and D, B and C, or B and D.



### Scenario 3: Mixed permissions

In this scenario, your project contains a mixture of service agent permissions and user-managed service account permissions.

  * The service agent is granted write permissions on buckets A and B. 
  * User-managed service account #1 is granted **read-only** permissions on bucket C and **write** permissions on bucket D.
  * User Alpha is granted access to user-managed service account #1.



In this case:

  * Any user with the correct permissions to create a transfer job can transfer into or out of buckets A and B. They cannot transfer into or out of bucket C or D.
  * User Alpha can transfer into or out of buckets A and B.
  * Alpha can transfer **out** of bucket C into bucket D.
  * Alpha can **not** transfer out of bucket C into bucket A or B.



## Implementation overview

The implementation is as follows:

  * You create a user-managed service account, or use an existing one.
  * You grant permissions: 
    * For a user to access the user-managed service account.
    * For the service agent to generate an [access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) from the user-managed service account.
    * For the user-managed service account to access your buckets.
  * The user creates a transfer job that specifies the user-managed service account.
  * Storage Transfer Service checks that the user has the correct permissions on the service account. If the correct permissions have not been granted, creation of the transfer job fails.
  * The service agent generates an OAuth token on behalf of the user-managed service account. The OAuth token allows Storage Transfer Service to access the buckets involved in the transfer.
  * The transfer job executes.
  * The OAuth token is short-lived and expires. If the transfer job is in progress when the token expires, Storage Transfer Service generates a new one and continues the transfer.



## Set up permission delegation

Follow the instructions to delegate service agent access to a user-managed service account.

### Requirements

  * To create a new user-managed service account, you require the Create Service Accounts (`roles/iam.serviceAccountCreator`) role on the project.
  * To grant access for the user and the service agent to the user-managed service account, you need the Service Account Admin (`roles/iam.serviceAccountAdmin`) role on the user-managed service account, or on the project.



### Create or identify a user-managed service account

You can create a new user-managed service account, or use an existing one.

  * To create a user-managed service account, follow the instructions in [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create#console).

  * To use an existing user-managed service account, you need its email address, which uses the following format:

`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`




If the service account is in a different project than the transfer job, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

### Grant access to the user

Grant the user account access to the new user-managed service account, and assign the **Service Account User** role (`roles/iam.serviceAccountUser`). The user account is the account being used to create or update the transfer job.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the user-managed service account.

  4. Select the **Principals with access** tab.

  5. Click person_add **Grant access**.

  6. Enter the user's email address. For example, `user1@example.com`.

  7. From the **Role** drop-down list, select **Service Account User**.

  8. Click **Save**. The principal is granted the role on the service account.




###  gcloud 

To grant a role to a principal, run the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    
    gcloud iam service-accounts add-iam-policy-binding USER_MANAGED_SERVICE_ACCOUNT_EMAIL \
      --member=PRINCIPAL --role=roles/iam.serviceAccountUser

Replace the following variables:

  * USER_MANAGED_SERVICE_ACCOUNT_EMAIL: The user-managed service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`.
  * PRINCIPAL: The email address of the user running the transfer job, in the format `user:name@example.com`.



### Grant access to the service agent

To enable the service agent to generate an [access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) from the user-managed service account, grant the service agent access to the user-managed service account, and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).

You need the email address of the service agent in order to grant access. To find the service agent's email:

  1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

An interactive panel opens, titled **Try this method**.

  2. In the panel, under **Request parameters** , enter your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). The project you specify here must be the project you're using to manage Storage Transfer Service.

  3. Click **Execute**.

Your service agent's email is returned as the value of `accountEmail`. It uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.




Then, to grant the service agent access to the user-managed service account:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the user-managed service account.

  4. Select the **Principals with access** tab.

  5. Click person_add **Grant access**.

  6. Enter the service agent's email address.

  7. From the **Role** drop-down list, select **Service Account Token Creator**.

  8. Click **Save**. The principal is granted the role on the service account.




###  gcloud 

To grant a role to a principal, run the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    
    gcloud iam service-accounts add-iam-policy-binding USER_MANAGED_SERVICE_ACCOUNT_EMAIL \
      --member=serviceAccount:SERVICE_AGENT_EMAIL --role=roles/iam.serviceAccountTokenCreator

Replace the following variables:

  * USER_MANAGED_SERVICE_ACCOUNT_EMAIL: The user-managed service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`.
  * SERVICE_AGENT_EMAIL: The email address of the service agent.



### Grant bucket permissions to the user-managed service account

Grant the permissions listed in [Service agent permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud#manually_assigning_roles) to the user-managed service account, instead of to the service agent.

## Create a transfer job using a user-managed service account

Once you've granted the correct permissions, you can specify the user-managed service account when creating a new transfer job.

###  Google Cloud console 

Follow the instructions to [create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers). Before finalizing the transfer job:

  1. On the **Choose settings** page, find the **Service account type** section.
  2. Select **User-managed service account**.
  3. Enter the user-managed service account email, using the format `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.
  4. Click **Create** to create the transfer job.



###  REST API 

Specify the user-managed service account as the value of the `serviceAccount` field in the `transferJobs.create` request.

Either the service account email (`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`) or the unique ID (`123456789012345678901`) are accepted.

For example:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
    "description": "A transfer using a user-managed service account for bucket permissions",
    "status": "ENABLED",
    "projectId": "PROJECT_ID",
    "serviceAccount": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
    "transferSpec": {
        ...
      }
    }
    

## Retrieve a service account's unique ID

When configuring federated access to AWS S3 or Microsoft Azure storage, or specifying a service account in REST API requests, you might need your user-managed service account's unique ID.

To retrieve the `uniqueId`:

###  Google Cloud console 

  1. Go to the **Service accounts** page in the Google Cloud console.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click the email address of the service account.

  3. Under the **Details** tab, locate the **Unique ID**.




###  gcloud CLI 

Use the following Google Cloud CLI command:
    
    
    gcloud iam service-accounts describe USER_MANAGED_SERVICE_ACCOUNT_EMAIL \
      --format='value(uniqueId)'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
