---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access/
title: Grant Service Account User for run-as service accounts \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:49.642894+00:00
---

# Grant Service Account User for run-as service accounts  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Grant Service Account User for run-as service accounts

This page is part of [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes). It lists who needs Service Account User (`roles/iam.serviceAccountUser`) and shows how to grant it.

**Warning:** Grant the role before you [set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as). Setting one means publishing the integration, and publishing requires this role. If you set the service account first, the publish that would have saved your fix can be rejected.

## Who needs Service Account User

The following principals need Service Account User on the listed service account:

Principal | Service account  
---|---  
Anyone who publishes or tests the integration, including deployment automation | The integration's run-as service account  
Anyone who runs the integration through the API or the Google Cloud console, synchronously or asynchronously | The integration's run-as service account  
The service account that a trigger uses to start the integration: the **Service account email** of a [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger), or the **Service account** of a [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger), an [Eventarc trigger](https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger), or an [Integration Connectors event trigger](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks#event_triggers). Not needed if that account is the run-as service account itself. | The integration's run-as service account  
Anyone who approves or resumes a suspended run | The integration's run-as service account  
Whoever starts an integration that calls a sub-integration with the [Call Integration](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task) task. For an integration that a trigger with a service account starts, this is the trigger's service account. | The sub-integration's run-as service account, in addition to the calling integration's  
The calling integration's run-as service account, when it calls a sub-integration asynchronously. Not needed if both integrations use the same service account. | The sub-integration's run-as service account  
Anyone who creates or edits an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles) of type **Service account** or **OIDC token** | The service account named in the profile  
Anyone who publishes or tests an integration that uses that profile | The service account named in the profile  
Whoever runs an integration that reaches a task using that profile. For an asynchronous or scheduled run, this is the integration's run-as service account, or the Application Integration service agent, `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`, if the integration doesn't have one. Setting a run-as service account is the better fix in that case. | The service account named in the profile  
  
Saving a draft doesn't require Service Account User. The checks on publishing, testing, and saving authentication profiles already apply. The checks on running, approving, calling sub-integrations, and running tasks that use an authentication profile take effect as the rollout proceeds, so grant every row now to keep your integrations running when they do.

**Note:** The Application Integration roles, including `roles/integrations.integrationInvoker`, don't grant `iam.serviceAccounts.actAs`. Service Account User is always a separate grant.

## Grant the role

To grant the role to someone, run the following command:
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
        --project=SERVICE_ACCOUNT_PROJECT_ID \
        --member='user:PRINCIPAL' \
        --role='roles/iam.serviceAccountUser'
    

Replace the following:

  * `SERVICE_ACCOUNT`: the email address of the run-as service account, or of the account named in an authentication profile
  * `SERVICE_ACCOUNT_PROJECT_ID`: the ID of the project that _owns the service account_
  * `PRINCIPAL`: the email address of the user



For other principal types, use the corresponding `--member` prefix:

  * **Groups:** Use `group:`. We recommend using Google groups rather than individual user accounts to simplify access management as team members change.
  * **Service accounts:** Use `serviceAccount:` for automated processes, applications, and trigger service accounts.

**Caution:** The `--project` flag has to name the project that owns the service account. If your run-as service account lives in a different project from the integration, the grant belongs in the service account's project — granting it in the integration's project won't do anything. This is the most common mistake when making this change. A project-level grant also works, as long as it's in the project that owns the service account.

To do the same in the Google Cloud console:

  1. Go to **IAM & Admin** > **Service Accounts**.
  2. Select the service account.
  3. Click **Permissions** > **Grant access**.



To make the grant, you need `roles/iam.serviceAccountAdmin` on the service account. Project Owners have it. For more, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## What's next

  * [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on integrations that run without a person.
  * If a grant doesn't seem to work, see [Troubleshoot authorization errors](https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
