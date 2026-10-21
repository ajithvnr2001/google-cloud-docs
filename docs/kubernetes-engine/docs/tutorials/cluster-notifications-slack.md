---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack/
title: Configure cluster notifications for third-party services \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:01:55.499349+00:00
---

# Configure cluster notifications for third-party services  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure cluster notifications for third-party services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to configure third-party messaging services to receive Google Kubernetes Engine (GKE) [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).

Services such as [Slack](https://slack.com) offer [_incoming webhooks_](https://api.slack.com/incoming-webhooks), a simple way to post messages from apps into Slack. [Cloud Run functions](https://docs.cloud.google.com/functions) is a lightweight Compute Engine solution to create single-purpose, stand-alone functions that respond to [Google Cloud events](https://docs.cloud.google.com/functions/docs/concepts/events-triggers), such as cluster notifications, without the need to manage a server or runtime environment. When GKE sends a cluster notification using Pub/Sub, a _trigger_ responds by executing an action, such as sending a Slack notification.

There are many third-party services built with cross-application messaging functionality, such as [IFTTT](https://ifttt.com/). You can use this tutorial as a template for connecting with these services.

In this tutorial, you use Cloud Run functions and Pub/Sub to send notifications about GKE cluster events to Slack.

## Objectives

  * Deploy a Slack application to receive external notifications from GKE.
  * Write a Cloud Run function that sends Pub/Sub notifications to Slack.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Run functions](https://cloud.google.com/functions/pricing-overview)
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE, Cloud Run functions, Cloud Build, Eventarc and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions.googleapis.com,pubsub.googleapis.com,container.googleapis.com,cloudbuild.googleapis.com,eventarc.googleapis.com&redirect=https%3A//docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install alpha beta

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the GKE, Cloud Run functions, Cloud Build, Eventarc and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions.googleapis.com,pubsub.googleapis.com,container.googleapis.com,cloudbuild.googleapis.com,eventarc.googleapis.com&redirect=https%3A//docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-slack)

  12. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  13. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  14. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  15. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install alpha beta

  16. [Enable GKE cluster notifications.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications)



### Required roles

To get the permissions that you need to set up Slack notifications for cluster notifications, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Functions Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)



To ensure that the Compute Engine default service account has the necessary permissions to invoke the Cloud Run function, ask your administrator to grant the [Cloud Functions Invoker ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.invoker) (`roles/cloudfunctions.invoker`) IAM role to the Compute Engine default service account on your project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Slack notifications

To set up Slack notifications, you must create a Slack application, activate Incoming Webhooks for the application, and install the application to a Slack workspace.

### Create the Slack application

  1. [Join a Slack workspace](https://slack.com/intl/en-ca/help/articles/212675257-Join-a-Slack-workspace), either by registering with your email or by using an invitation sent by a Workspace Admin.

**Note:** If you are not an Admin for your Slack workspace, you might need approval from a Workspace Admin before your app is deployed to your workspace.
  2. [Sign in to Slack](https://slack.com/signin) using your workspace name and your Slack account credentials.

  3. [Create a new Slack app](https://api.slack.com/apps?new_app=1)

     1. In the **Create an app** dialog, click **From scratch**.
     2. Specify an **App Name** and choose your Slack workspace.
     3. Click **Create App**.
     4. Under **Add features and functionality** , click **Incoming Webhooks**.
     5. Click the **Activate Incoming Webhooks** toggle.
     6. In the **Webhook URLs for Your Workspace** section, click **Add New Webhook to Workspace**.
     7. On the authorization page that opens, select a channel to receive notifications.
     8. Click **Allow**.
     9. A webhook for your Slack application is displayed in the **Webhook URLs for Your Workspace** section. Save the URL for later.



## Write the Cloud Run function

When GKE publishes a cluster notification to a Pub/Sub topic, the event triggers Cloud Run functions to send a Slack notification.

  1. Create a new directory named `gke_slack` and change directory into it:
         
         mkdir ~/gke_slack && cd $_
         

  2. Create the following files in the gke_slack directory:

**index.js**
         
         const functions = require('@google-cloud/functions-framework');
         const { IncomingWebhook } = require('@slack/webhook');
         
         const url = process.env.SLACK_WEBHOOK;
         
         const webhook = new IncomingWebhook(url);
         
         // Optionally filter what notification types to forward to Slack.
         // If empty, all types will be allowed.
         const allowedTypeURLs = [];
         
         // Register a CloudEvent callback with the Functions Framework that will
         // be executed when the Pub/Sub trigger topic receives a
         // message.
         functions.cloudEvent('slackNotifier', pubSubEvent => {
             const data = decode(pubSubEvent.data.message.data);
         
             // Send message to Slack.
             if (isAllowedType(pubSubEvent.data.message.attributes)) {
                 const message = createSlackMessage(data, pubSubEvent.data.message.attributes);
                 (async () => {
                   await webhook.send(message);
                 })().catch((e) => {
                     console.log(e);
                 });
             }
         });
         
         // decode decodes a pubsub event message from base64.
         const decode = (data) => {
             return Buffer.from(data, 'base64').toString();
         }
         
         // isAllowedType can be used to filter out messages that don't match the
         // allowed type URLs. If allowedTypeURLs is empty, it allows all types.
         const isAllowedType = (attributes) => {
             if (allowedTypeURLs.length == 0) {
                 return true;
             }
             for (var x in allowedTypeURLs) {
                 if (attributes['type_url'] == allowedTypeURLs[x]) {
                     return true;
                 }
             }
             return false;
         }
         
         // createSlackMessage creates a message from a data object.
         const createSlackMessage = (data, attributes) => {
             // Write the message data and attributes.
             text = `${data}`
             for (var key in attributes) {
                 if (attributes.hasOwnProperty(key)) {
                     text = text + `\n\t\`${key}: ${attributes[key]}\``
                 }
             }
             const message = {
                 text: text,
                 mrkdwn: true,
             };
             return message;
         }
         

`SLACK_WEBHOOK` is a Cloud Run functions environment variable specifying the webhook URL created for your Slack application. You define the environment variable when you deploy the function.

The webhook listens for and receives messages from Cloud Run functions. When GKE sends a cluster notification to Pub/Sub (the event), the function sends a message (the trigger) to the webhook URL, which in turn sends the message to the configured Slack workspace.

You can expand the message in the `createSlackMessage` function to include much more, including text formatting and images. The `isAllowedType` function is provided to enable basic filtering of notifications by the type URL. You can specify what type URLs to allow in `allowedTypeURLs`. This function isn't necessary if you already [filtered notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#filtering), either in GKE or in your Pub/Sub subscription.

**package.json**
         
         {
          "name": "gke-slack",
          "version": "0.0.1",
          "description": "Slack integration for GKE, using Cloud Run functions",
          "main": "index.js",
          "dependencies": {
            "@slack/webhook": "6.1.0",
            "@google-cloud/functions-framework": "^3.0.0"
          }
         }
         

`package.json` describes the following attributes of the program:

     * Name, version, and description
     * Primary runtime file(s)
     * Dependencies

You can add more dependencies, requirements, and other information as needed.




You should now have the `index.js` and `package.json` files in the `gke_slack` directory.

### Deploy the Cloud Run function

You can deploy the Cloud Run function using either the Google Cloud CLI or the Google Cloud console.

### gcloud

To deploy the function, run the following command in the gke_slack directory:
    
    
    gcloud functions deploy slackNotifier \
      --gen2 \
      --trigger-topic=TOPIC_NAME \
      --runtime=nodejs24 \
      --entry-point=slackNotifier \
      --region=REGION \
      --source=. \
      --set-env-vars="SLACK_WEBHOOK=WEBHOOK_URL"
    

Replace the following:

  * `TOPIC_NAME`: the name of the Pub/Sub topic you created when [enabling cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).
  * `REGION`: the Compute Engine region for the function.
  * `WEBHOOK_URL`: the webhook URL created for your Slack application in Create the Slack application.



The output is similar to the following:
    
    
    Deploying function…
    availableMemoryMb: 256
    entryPoint: slackNotifier
    environmentVariables:
      SLACK_WEBHOOK: https://hooks.slack.com/services/…
    eventTrigger:
      eventType: google.pubsub.topic.publish
      failurePolicy: {}
      resource: projects/PROJECT_ID/topics/TOPIC_NAME
      service: pubsub.googleapis.com
    labels:
      deployment-tool: cli-gcloud
    name: projects/PROJECT_ID/locations/us-central1/functions/slackNotifier
    runtime: nodejs24
    serviceAccountEmail: PROJECT_ID@appspot.gserviceaccount.com
    sourceUploadUrl: https://storage.googleapis.com/…
    status: ACTIVE
    timeout: 60s
    updateTime: 'YYYY-MM-DDThh:mm:ssZ'
    versionId: '1'
    

### Console

  1. Go to the **Cloud Run functions** page in the Google Cloud console.

[Go to Cloud Functions](https://console.cloud.google.com/functions/list)

  2. Click add_box **Create function**.

  3. On the **Configuration** page, perform the following steps:

     1. From the **Environment** drop-down list, select **2nd gen**.
     2. For **Function name** , specify **slackNotifier**.
     3. For **Region** , specify a Compute Engine region.
     4. In the **Trigger** section, click add_box**ADD EVENTARC TRIGGER**.
     5. In the opened window, check that the **Event provider** drop-down list, select **Cloud Pub/Sub**.
     6. Select the Pub/Sub topic you created when [enabling cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).
     7. For **Region** , specify the same Compute Engine region as for the function.
     8. Click **SAVE TRIGGER**.
     9. Expand the **Runtime, build, connections and security settings** section.
     10. Under **Runtime environment variables** , click add **Add Variable**.
     11. For **Name** , specify **SLACK_WEBHOOK**.
     12. For **Value** , specify the URL of the Internal Webhook created in Create the Slack application.
     13. Click **Next**.
  4. On the **Code** page, perform the following steps:

     1. Select **Node.js 24** from the **Runtime** drop-down list.
     2. For **Entry point** , specify **slackNotifier**.
     3. In the navigation pane, select **index.js** and replace the code with the sample code in Write the Cloud Function.
     4. In the navigation pane, select **package.json** and replace the code with the sample code in Write the Cloud Function.
     5. Click **Deploy**.



After you've completed deployment of the Cloud Run function, you will receive a Slack notification whenever GKE sends a cluster notification.

## Verify Slack notifications

If you used an Autopilot cluster, verify notifications as follows:

  1. [Start a control plane upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp).
  2. Wait for GKE to automatically upgrade your nodes to the new version. The time taken might vary based on configured maintenance windows and exclusions.
  3. After GKE upgrades your nodes, check Slack for a message.



If you used a Standard cluster, verify notifications as follows:

  1. [Upgrade a specific node pool to a new version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes). If you don't want to change the GKE version on your nodes, you can upgrade to the same version currently on the nodes.

**Caution:** Manually upgrading a Standard node pool ignores your configured [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) and might cause disruptions to running workloads.
  2. After GKE upgrades your nodes, check Slack for a message.




The Slack notification is similar to the following:
    
    
    Master is upgrading to version 1.20.10-gke.301.
        cluster_location: us-central1
        cluster_name: pubsub-cluster
        payload: {"resourceType":"MASTER", "operation":"operation-1632775054313-45128f4f", "operationStartTime":"2021-09-27T20:37:34.313742491Z", "currentVersion":"1.20.9-gke.1001", "targetVersion":"1.20.10-gke.301"}
        project_id: 729788050015
        type_url: type.googleapis.com/google.container.v1beta1.UpgradeEvent
    

**Note:** You will not receive a notification if you chose to ignore the `UpgradeEvent` notification type when setting up your cluster notifications. You cannot verify setup manually for the `SecurityBulletinEvent` or the `UpgradeAvailableEvent` notification types.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

  1. Delete the Cloud Run function you deployed in this tutorial:
         
         gcloud functions delete slackNotifier
         

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).

  2. [Delete the Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#deleting_a_topic).

  3. [Delete the Slack app](https://api.slack.com/apps).




## What's next

  * Learn about [the types of cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).
  * Check out the [Cloud Run functions](https://docs.cloud.google.com/functions/docs) and the [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) documentation.
  * Learn more about [building Slack apps](https://api.slack.com/slack-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
