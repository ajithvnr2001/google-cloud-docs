---
url: https://docs.cloud.google.com/workflows/docs/use-iam-for-access/
title: Use IAM to control access \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:01.582214+00:00
---

# Use IAM to control access  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-iam-for-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Use IAM to control access Stay organized with collections  Save and categorize content based on your preferences. 

Workflows uses Identity and Access Management (IAM) to control which authenticated users and service accounts can perform which actions.

Before you begin authenticating and authorizing access to your Workflows resources, make sure you understand the [basic concepts of IAM](https://docs.cloud.google.com/iam/docs/overview).

This page details the permissions required to access Workflows resources, including the ability to invoke workflow executions.

For information on granting permissions to workflows to access other services, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

## Access control

Regardless of how you implement authentication, it's important to understand access control and the available Workflows roles. A role is a collection of permissions that grant access to resources in Google Cloud. When building a production application, only grant a service account the roles it needs to interact with the applicable Google Cloud APIs, features, or resources.

For more information about the available Workflows roles, see [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control).

## Invoke Workflows

A service account is both an identity and a resource that accepts IAM policies. As a result, you can grant roles to the service account, then let other principals impersonate the service account by granting them a role on the service account or on one of the service account's parent resources.

For example, you can grant a service account the [workflows.invoker](https://docs.cloud.google.com/workflows/docs/access-control#roles) role so that the account has permission to trigger your workflow execution. You could then allow a principal to impersonate, or act as, your service account. Note that the workflow service account does not require the `workflows.invoker` role, unless the workflow invokes itself or other workflows.

For more information on service account impersonation, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

To grant the service account of the service calling Workflows the Workflows Invoker role (`roles/workflows.invoker`) so that the service has permission to execute workflows and manage the executions, do the following:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page:   
[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project and then click **Create service account**.

  3. In the **Service account name** field, enter a name, such as `sa-name`.

  4. Click **Create and continue**.

  5. In the **Select a role** list, select **Workflows** > **Workflows Invoker**.

  6. Click **Done**.




### gcloud

  1. Open a terminal.

  2. Enter the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
            --role roles/workflows.invoker

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `SERVICE_ACCOUNT_NAME`: the name of the service account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
