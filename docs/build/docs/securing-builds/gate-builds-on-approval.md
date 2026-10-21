---
url: https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval/
title: Gate builds on approval \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.680065+00:00
---

# Gate builds on approval  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Gate builds on approval Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build enables you to configure triggers that do not immediately execute a build but instead mark a build as pending until approved. If a user with permissions approves a pending build, the build will start. If the approval is denied, the build will not start.

This page explains how you can manually approve or reject builds. To learn how to configure a trigger that requires approval, see [Creating a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#console).

**Note:** You can't approve or reject pending builds older than 2 months. For details, see [Troubleshooting](https://docs.cloud.google.com/build/docs/troubleshooting#pending_build).

## Before you begin

  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/approve-builds)



  * Install [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've already installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * If you have not already, [create a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#console) configured to require approval.




### Granting permissions

If a user has the **Cloud Build Editor role** , the user has permissions to update a trigger to require or not require approval. To learn more about Cloud Build permissions, see [IAM and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions). In order to grant a user permission to approve builds within your project, the user must have the **Cloud Build Approver** role.

To add the **Cloud Build Approver** role:

  1. Open the **IAM** page in the Google Cloud console.

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant access**.

You will see the **Grant access** panel.

  3. In the **Add principals** section, add users to give them permission to grant approval for pending builds within your project.

You _must_ add one or more principals in this section. If you add yourself as a principal, note that you will still need to manually approve a pending build if your trigger is gated by an approval.

  4. In the **Assign roles** section, select **Cloud Build** > **Cloud Build Approver**.




The users you specified now have access to approve or reject pending builds.

## Approving builds

###  Console 

To approve a pending build in the Google Cloud console:

  1. Open the **Cloud Build Dashboard** page in the Google Cloud console.

[Open the Cloud Build Dashboard page](https://console.cloud.google.com/cloud-build/dashboard)

  2. If you have builds to approve, you will see a message at the top of the page with the number of builds awaiting your approval. To the right of the message, click **View Builds** to view the list of builds awaiting your approval.

  3. Click on the checkboxes of the builds you'd like to approve. You can select multiple builds to approve or one individual build to approve.

  4. At the top of the page, click **Approve** to approve your selected builds.

  5. Before the build starts, you will see the **Approve build** dialog box. In the dialog box, you can add an optional message and a URL to be displayed along with the build's approval. To include a URL, click **Show additional options** to enter a URL.

  6. In the dialog box, click **Approve** to approve the build.




Once you approve, the build will start immediately. If the organization policy (`constraints/cloudbuild.allowedIntegrations`) denies access to the connected repository, the policy will override the approval. To learn more, see [Gate builds on organization policy](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-organization-policy).

###  gcloud 

To approve a pending build using `gcloud commands`, run the following command in your terminal window:
    
    
    gcloud builds approve BUILD_ID \
      --project=PROJECT_ID \
      --url=URL \
      --comment=COMMENT
    

Replace the placeholder values in the above commands with the following:

  * `BUILD_ID` is the ID of the build you'd like to approve.
  * `PROJECT_ID` is your project ID.
  * [Optional] `URL` is the URL containing information about the approval, such as a link to a JIRA ticket.
  * [Optional] `COMMENT` is the message you want displayed upon approval of the build.



Once you approve, the build will start immediately. If the organization policy to define builds for allowed integrations (`constraints/cloudbuild.allowedIntegrations`) is set, the policy will override the approval. To learn more, see [Applying organization policy to build triggers](https://docs.cloud.google.com/build/docs/securing-builds/apply-organization-policy-triggers).

## Rejecting builds

###  Console 

To reject a pending build in the Google Cloud console:

  1. Open the **Cloud Build Dashboard** page in the Google Cloud console.

[Open the Cloud Build Dashboard page](https://console.cloud.google.com/cloud-build/dashboard)

  2. If you have builds to approve, you will see a message at the top of the page with the number of builds awaiting your approval. To the right of the message, click **View Builds** to view the list of builds awaiting your approval.

  3. You can select multiple builds to reject or one individual build to reject. Click on the checkboxes of the builds you'd like to reject.

  4. Click **Reject** at the top of the page to reject the build.




If you reject a build, the build will not start.

###  gcloud 

To reject a pending build using `gcloud commands`, run the following command in your terminal window:
    
    
    gcloud builds reject BUILD_ID \
      --project=PROJECT_ID \
      --url=URL \
      --comment=COMMENT
    

Replace the placeholder values in the above commands with the following:

  * `BUILD_ID` is the ID of the build you'd like to reject.
  * `PROJECT_ID` is your project ID.
  * [Optional] `URL` is the URL containing information about the rejection, such as a link to a JIRA ticket.
  * [Optional] `COMMENT` is the message you want displayed upon rejection of the build.



If you reject a build, the build will never start.

## Receiving notifications for builds waiting for approval

You can use Cloud Build notifiers to receive notifications about pending builds using a Cloud Build maintained notifier, such as [Slack](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack) or [SMTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp) server, or by [creating your own notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/create-notifier).

To configure notifications:

  1. Follow the instructions on one of following pages to configure notifications for your desired service:

     * [BigQuery](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery)
     * [HTTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-http)
     * [Slack](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack)
     * [SMTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp)
     * [Creating your own notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/create-notifier)
  2. When configuring notifications using one of the pages above, you must configure your notifier to filter builds with a _PENDING_ status. This will send you notifications on builds waiting for approval. In the following example SMTP notifier configuration file, the filter field uses [Common Expression Language](https://github.com/google/cel-spec) (CEL) to filter build events with a PENDING status:
         
         apiVersion: cloud-build-notifiers/v1
         kind: SMTPNotifier
         metadata:
           name: example-smtp-notifier
         spec:
           notification:
             filter: build.status == Build.Status.PENDING
             delivery:
               server: example.gmail.com
               port: 0000
               sender: sender@example.com
               ...
         

To view the full example, see the [notifier configuration file for the SMTP notifier](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/smtp/smtp.yaml.example).

  3. To deploy your notifier, run the `gcloud run` command in your terminal. The following example deploys the SMTP notifier using Cloud Run.
         
         gcloud run deploy example.gmail.com \
           --image=us-east1-docker.pkg.dev/gcb-release/cloud-build-notifiers/smtp:latest \
           --update-env-vars=CONFIG_PATH=smtp.yaml, PROJECT_ID=my-project
         




You should now receive notifications for pending builds to your service.

## What's next

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [view build results for build triggers](https://docs.cloud.google.com/build/docs/view-build-results#viewing_build_results_for_build_triggers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
