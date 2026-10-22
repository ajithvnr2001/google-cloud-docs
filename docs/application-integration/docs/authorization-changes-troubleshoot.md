---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot/
title: Troubleshoot authorization errors \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:49.274027+00:00
---

# Troubleshoot authorization errors  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot authorization errors

This page is part of [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes). It explains the errors you might see and how to fix them.

A denied action has one of two causes, and they're worth telling apart:

  * **The run-as service account** — either you can't act as it, or it can't reach what a task needs. See Run-as service account errors.
  * **Your own IAM role** — you aren't allowed to perform the action at all. See IAM role errors.



Both checks apply, so fixing one doesn't fix the other.

## Run-as service account errors

Some of these checks are still rolling out, so you might not see every error yet. In the messages, PRINCIPAL is the account that was checked. It reads `The caller` when that account can't be named.

Situation | What you'll see | What to do  
---|---|---  
A person, automation, or trigger starts an integration but can't act as its run-as service account | The run is rejected with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to run this integration.`

  * An API call returns the error, and nothing appears in your execution logs.
  * A Cloud Pub/Sub, Eventarc, or Integration Connectors event trigger records a failed execution in your execution logs, and the event isn't delivered again.
  * A Cloud Scheduler job reports a `PERMISSION_DENIED` error.

| [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) to whoever starts it. For a trigger, that's the trigger's service account.  
An integration created on or after October 15, 2026, with a trigger other than API or Private, doesn't have a run-as service account. | Publishing and testing fail with the following error: `Set a run-as service account. These triggers run with no caller: TRIGGERS. Required for integrations created on or after October 15, 2026 (UTC).` | [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as)  
A run without user credentials doesn't have a run-as service account. | If integration governance is enabled for the region, publishing and testing fail with the following error, whatever the integration's creation date: `Your project requires a run-as service account. Set one before publish or test.` Governance is the **Enable governance** setting described in [Edit region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region). For regions without governance, the system doesn't reject these runs starting October 15, 2026. However, the following are planned to fail in a future release: 

  * Tasks without an identity, such as Connectors, Call REST Endpoint, or Cloud Run functions tasks.
  * Asynchronous runs, with the following error: `Integration NAME needs a run-as service account to run asynchronously via trigger TRIGGER_ID.`

| [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as)  
A Call Integration task can't start its sub-integration | The calling integration's Call Integration task fails, for one of these reasons: 

  * The sub-integration is called asynchronously and has no run-as service account, even if the calling integration has one: `Integration NAME needs a run-as service account to run asynchronously via trigger TRIGGER_ID.`
  * Whoever started the calling integration, or the calling integration's run-as service account, can't act as the sub-integration's run-as service account: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to run this integration.`

| [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on the sub-integration, or call it synchronously. Then [grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access#who_needs_it) on it.  
Someone publishes or tests an integration that uses an authentication profile whose service account they can't act as, or a run reaches a task that uses it | Publishing or testing fails, or the task fails, with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to use auth config "AUTH_PROFILE_NAME".` Whether the rest of the run continues depends on how the task handles errors. | [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the account named in the profile  
Someone creates or edits a **Service account** or **OIDC token** authentication profile without permission to act as its service account | Saving the profile fails with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to save this auth config.` | [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the account named in the profile to whoever manages it  
An approver can't act as the run-as service account | Approving or resuming the run fails with the following error: `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to resume this execution.` The run stays paused until it expires, so approvals can seem to have stopped working | [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) to everyone who might approve  
Someone publishes or tests an integration without permission to act as its run-as service account | `PRINCIPAL needs roles/iam.serviceAccountUser on SERVICE_ACCOUNT (or its project) to publish or test this integration.` Anything already published keeps running. If automation publishes for you, this surfaces in your deployment pipeline rather than in the console | [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) to publishers, testers, and automation  
A task runs as the person who triggered it, and that person can't reach the resource. In a new integration, and starting October 15, 2026, in a test of any integration, [JavaScript](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task), [Data Transformer Script](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task), and [Data Mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) tasks run this way | The run starts normally, then one task fails naming a resource, even though nothing about the integration changed | Give those people access to the resource, or move the integration onto a run-as service account that already has it — usually the better answer, since it stops the integration's access varying with whoever runs it  
  
For the full list of Application Integration error codes, see [Error codes](https://docs.cloud.google.com/application-integration/docs/error-codes).

## IAM role errors

In addition to the run-as service account, Application Integration verifies your user IAM permissions for each action. If you encounter a `PERMISSION_DENIED` error when interacting with an integration, or if execution logs fail to load, ensure you have a role that grants the required permissions: 

To do this | You need one of these roles  
---|---  
See and open integrations | `roles/integrations.integrationViewer`  
View execution logs and details | `roles/integrations.integrationViewer` or `roles/integrations.integrationInvoker`  
Run an integration | `roles/integrations.integrationInvoker` or `roles/integrations.integrationEditor`  
Create and edit integrations | `roles/integrations.integrationEditor`  
Publish an integration | `roles/integrations.integrationDeployer` or `roles/integrations.integrationEditor`  
Approve or resume a suspended run | `roles/integrations.suspensionResolver` or `roles/integrations.integrationAdmin`  
Full access to all integrations | `roles/integrations.integrationAdmin`  
**Note:** Approving or resuming a suspended run requires the `integrations.suspensions.resolve` permission, which the `roles/integrations.integrationEditor` role does not include. Approvers require the `roles/integrations.suspensionResolver` role, as well as the Service Account User role (`roles/iam.serviceAccountUser`) on the run-as service account.**Note:** None of these roles lets you change who has access. Granting the roles and permissions described on this page needs a separate role: 

  * `roles/iam.serviceAccountAdmin` to grant Service Account User on a service account.
  * `roles/resourcemanager.projectIamAdmin` to grant project-level Application Integration roles.

Project Owners hold both. If you can't make a grant yourself, ask an administrator who does.

To grant a role, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member='user:PRINCIPAL' \
        --role='ROLE'
    

For more information, see the following:

  * [Predefined IAM roles](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions), for the complete list of roles and the permissions each one contains.
  * [Access control](https://docs.cloud.google.com/application-integration/docs/access-control), for how Application Integration uses IAM.

**Caution:** If your organization scopes roles to individual integrations using [IAM conditions](https://docs.cloud.google.com/application-integration/docs/add-iam-conditions), the condition must match the specific integration you are accessing. A role binding that grants access to one integration might deny access to another. If you encounter permission errors despite having the correct role, verify the conditions attached to your role binding.

## A grant didn't fix the error

  * **The grant went to the wrong project.** It has to be made in the project that owns the _service account_ , which isn't necessarily the one that owns the integration.
  * **It hasn't taken effect yet.** Give it a few minutes. Authorization decisions are cached briefly, on top of the normal IAM propagation delay.
  * **There's a second service account involved.** Your run-as service account, each authentication profile's service account, and each sub-integration's run-as service account are separate, and each needs its own grant.
  * **The grant went to the wrong principal.** For a Cloud Scheduler, Cloud Pub/Sub, Eventarc, or Integration Connectors event trigger, the principal that needs the grant is the trigger's service account, not you. See [Who needs Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access#who_needs_it).
  * **The block is your own role, not the service account.** Service Account User is about whether you may act _as_ the run-as service account; a separate IAM role governs whether you're allowed to perform the action. See IAM role errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
