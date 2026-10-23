---
url: https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks/
title: Set up webhooks \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:16.726276+00:00
---

# Set up webhooks  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Set up webhooks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up webhooks in Secure Source Manager.

Webhooks are HTTP requests triggered by an event in Secure Source Manager, and sent to a user-specified URL.

## Before you begin

  1. [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).



### Required roles

To get the permissions that you need to create webhooks, ask your administrator to grant you the following IAM roles: 

  * Authenticate webhooks using a sensitive query string: 
    * [Secure Source Manager Repository Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on the Secure Source Manager repository
    * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * Authenticate webhooks using service account authorization: 
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Secure Source Managerrepository service account
    * [SSM service agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) on the Secure Source Manager repository service account
    * [Cloud Run Invoker ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`) on the destination service (required only if the destination is Cloud Run)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Set up a webhook

###  Console 

  1. In the Secure Source Manager web interface, navigate to the repository you want to create a webhook for.
  2. Click **Settings**.
  3. Click **Webhooks** , and then click **Add webhook**.
  4. In the **Hook ID** field, enter an ID for the webhook.

**Note:** Hook IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lower case letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the webhook.
  5. In the **Target URL** field, enter the Webhook URL. For example, if you want to trigger a build in Jenkins, you can [Set up a webhook trigger](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins#set_up_a_webhook_trigger), and then enter the Jenkins trigger URL here to trigger your build in Jenkins.

  6. In the **Trigger on** section, select one of the following:

     * **Push** : to trigger on a push to the repository.
     * **Pull request state changed** : to trigger on a change in the pull request state.
  7. Configure webhook authentication using either a sensitive query string or service account authentication:

     * **Sensitive query string** :

Your sensitive query string consists of the `key` and `secret` values from your webhook URL, including the `key=` and `secret=` prefixes. To configure sensitive query string authorization, you must remove these values from your webhook URL and add them to the **Sensitive Query String** field:

       1. Delete the `?` from your webhook URL.
       2. Copy the remaining portion of the URL, beginning with `key=`.
       3. Paste this portion into the **Sensitive Query String** field.
       4. Delete the same portion from your webhook URL.

For example, given the following URL: `https://cloudbuild.googleapis.com/v1/projects/my-project/triggers/test-trigger:webhook?key=eitIfKhYnv0LrkdsyHqIros8fbsheKRIslfsdngf&secret=My%20Secret%20`

Your sensitive query string would be: `key=eitIfKhYnv0LrkdsyHqIros8fbsheKRIslfsdngf&secret=My%20Secret%20`

**Note:** When you add or edit a webhook, the length of the `Sensitive Query String` might be inconsistent with the entered one, which is expected as placeholder strings are used to ensure security.
     * **Service account authentication** :

       1. Verify that your repository has a service account with the IAM roles defined for service account authentication in Required roles.
       2. Select **Enable service account authentication**.
  8. If you selected **Push** , then you can enter an allowlist for push events in the **Branch filter** field.

The **Branch filter** field uses the glob pattern and only operations on the matched branches will cause a build trigger. For example, `{main,dev}` triggers on push events to the `main` and `dev` branches. If the field is empty or `*`, then push events for all branches are reported. For information on syntax, see the [glob](https://pkg.go.dev/github.com/gobwas/glob) documentation.

  9. Click **Add webhook**.

  10. The webhook is displayed in the **Webhooks** page.




###  REST 

To create a webhook, invoke the [`hooks.create`](https://docs.cloud.google.com/securesource/reference/rest/v1/projects.locations.repositories.hooks/create) method by issuing a `POST` request to the `hooks` endpoint. You can authenticate your webhook using either a sensitive query string or service account authentication.

  * **Sensitive query string**
        
        curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
            "targetUri": "https://${SERVICE_NAME}.app/webhook?key=${KEY}&secret=${SECRET}",
            "events": ["PUSH"]
            "sensitiveQueryString": "${SENSITIVE_QUERY_STRING_VALUE}"
          }' \
          "https://securesourcemanager.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/repositories/${REPOSITORY}/hooks?hook_id=${HOOK_ID}"
        

Your `SENSITIVE_QUERY_STRING_VALUE` should be the value of `key` and `secret` in your webhook URL. For example, if your `key` is `eitIfKhYnv0LrkdsyHqIros8fbsheKRIslfsdngf` and your `secret` is `MySecret`, then your `SENSITIVE_QUERY_STRING_VALUE` should be `key=eitIfKhYnv0LrkdsyHqIros8fbsheKRIslfsdngf&secret=MySecret`.

**Note:** When you add or edit a webhook, the length of the `Sensitive Query String` might be inconsistent with the entered one, which is expected as placeholder strings are used to ensure security.
  * **Service account authentication**
        
        curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
            "targetUri": "https://${SERVICE_NAME}.app/webhook",
            "events": ["PUSH"],
            "serviceAccountAuth": true
          }' \
          "https://securesourcemanager.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/repositories/${REPOSITORY}/hooks?hook_id=${HOOK_ID}"
        




## Test your webhook

  1. In the Secure Source Manager **Webhooks** page, click the webhook you want to test.
  2. Go to the bottom of the page and click **Test delivery**.

A placeholder event is added to the delivery queue. It might take a few seconds before it shows up in the delivery history.

  3. You can also use a `git` command to push or merge a pull request to test the webhook.

  4. Check the status of the triggered build or event in the build history of the service where you configured your webhook trigger.

  5. You can also view the **Request** and **Response** to the test delivery in the **Recent deliveries** section of the Secure Source Manager webhook page after you send your first test delivery.




## Substitute Cloud Build YAML variables with payload data

If you're using webhooks to connect to Cloud Build, you can substitute Cloud Build YAML variables with Secure Source Manager webhook payload data.

  1. In the Secure Source Manager **Webhooks** page, in the **Recent deliveries** section, click the top row.

The **Request** header and content sent by the webhook payload is displayed.

  2. Navigate to the Cloud Build dashboard, and then click **Triggers**.

  3. Click the trigger you want to configure.

  4. In the **Advanced section** , under **Substitution variables** , click **\+ Add variable**.

  5. Enter the name and value of the variable. The value prefix is `body`.

For example, to substitute `_REPO_URL` with the payload data field `repository.clone_url` and `_COMMIT_SHA` with latest commit sha in Cloud Build YAML, enter the following names and values:

     * Variable 1: `_REPO_URL` Value 1: `$(body.repository.clone_url)`
     * Variable 2: `_COMMIT_SHA` Value 2: `$(body.after)`

The Cloud Build YAML file resembles the following:
    
    steps:
    - name: gcr.io/cloud-builders/git
      env:
      - '_REPO_URL=$_REPO_URL'
      - '_COMMIT_SHA=$_COMMIT_SHA'
      script: |
        #!/bin/sh
        git clone ${_REPO_URL} /workspace
        cd /workspace
        git reset --hard ${_COMMIT_SHA}
    




## What's next

  * [Connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
