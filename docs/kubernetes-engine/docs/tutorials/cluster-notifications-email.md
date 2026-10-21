---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-email/
title: Configure clusters to receive notifications via email \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:32.453766+00:00
---

# Configure clusters to receive notifications via email  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure clusters to receive notifications via email Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to configure [Application Integration](https://docs.cloud.google.com/application-integration/docs) to receive Google Kubernetes Engine (GKE) [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications) via email.

You create an integration with a Pub/Sub trigger to listen to an existing topic that receives notifications from a GKE cluster. You can then use the Data Mapping and Data Transformer tasks to transform the Pub/Sub message and build a plain text email body.

## Objectives

  * Create an Application Integration application to receive and transform external notifications from GKE.
  * Write a Send Email task that sends Pub/Sub notifications to email.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)
  * [Application Integration](https://cloud.google.com/application-integration/pricing)



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

  4. Enable the GKE, Application Integration and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub.googleapis.com,container.googleapis.com,integrations.googleapis.com&redirect=https%3A//docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-email)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE, Application Integration and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub.googleapis.com,container.googleapis.com,integrations.googleapis.com&redirect=https%3A//docs.cloud.google.com/kubernetes-engine/docs/tutorials/cluster-notifications-email)

  8. [Enable receiving GKE cluster notifications through Pub/Sub.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications)
  9. If you are using Application Integration in your project for the first time, you must [set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration#quick) by navigating to the Application Integration page in the console and clicking **Provision**.



### Required roles

**Important:** To get the permissions that you need to set up email notifications for cluster notifications, ask your administrator to grant `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com` the following IAM roles on your project. Don't attempt to grant IAM roles to this service agent until you have opened the Application Integration console and provisioned the service. The service agent account doesn't exist until provisioning is complete.

To ensure that service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com has the necessary permissions to set up email notifications for cluster notifications, ask your administrator to grant the following IAM roles to service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com on your project: 

  * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)
  * [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)
  * [Application Integration Invoker ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)



## Setup cluster notifications for your GKE cluster

To use Pub/Sub to receive notifications about your GKE cluster, follow [Receive cluster notifications through Pub/Sub](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).

## Create new integration

To create a new integration, perform the following steps:

  1. Go to the **Application Integration** page in the Google Cloud console.

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. The **Integrations** page appears.

  3. Click **Create integration**.

  4. In **Integration name** , enter a name for the integration you are creating.

  5. If you have multiple regions enabled, a drop-down option will show for you to select a region for the integration. When only one region has been enabled, it will default to that region and the drop-down won't be displayed.

**Note:** The **Regions** drop-down only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region** that is displayed at the bottom of the box.

  6. Click **Create** to open the integration editor.




### Add and configure Pub/Sub trigger

To add a Pub/Sub trigger to the integration, follow these steps:

  1. In the integration editor, select **Triggers** to display a list of available triggers.

  2. Click and place the **Pub/Sub** trigger element to the designer.

  3. Click the **Pub/Sub trigger** element in the integration editor to view the trigger configuration pane.

  4. Specify the topic the trigger should listen to in the **Pub/Sub topic** field in the following format:
         
         projects/PROJECT_ID/topics/TOPIC_ID
         

Replace the following:



  * `PROJECT_ID`: the Google Cloud project where your topic was created.

  * `TOPIC_ID`: the ID of the Pub/Sub topic you created in Setup your environment.

For example, if your project is named `my-project` and you named your topic `gke-notifications`, enter:
        
        projects/my-project/topics/gke-notifications
        

To view all the available topics in your Google Cloud project, see the **Topic name** column in [Topics](https://console.cloud.google.com/cloudpubsub/topic/list). The **Pub/Sub** trigger configuration pane will automatically populate the **Trigger Output** field with a variable to hold the Pub/Sub message.




### Add and configure the Data Mapping task

The Data Mapping task helps to extract relevant variables from the Pub/Sub notification. It takes the Pub/Sub message JSON file as input and extracts variables as output.

To configure the Data Mapping task:

  1. Select **Tasks** to display a list of available tasks.

  2. Click and place the **Data Mapping** element in the integration editor.

  3. Click the **Data Mapping** task on the designer to open the configuration pane for the task.

  4. To add an edge connection from Pub/Sub trigger to Data Mapping, hold the pointer over a control point on the Pub/Sub trigger, then drag a line to a control point on the Data Mapping task. The edge denotes the flow of control from the Pub/Sub trigger to the Data Mapping task.

  5. Click **Open Data Mapping Editor**. The Data Mapping Editor lets you map input variables to the selected output variables, using the available transform functions. The output is then available as a variable to any other integration task or trigger. For more information about variables in Application Integration, see [Variables](https://docs.cloud.google.com/application-integration/docs/variables-overview).

For this tutorial, follow these steps to create a mapping using the `CloudPubSubMessage` as input:

     1. Expand the `CloudPubSubMessage` JSON variable in the **Variables** list and drag the `CloudPubSubMessage.data` variable to the first **Input** row.
     2. To create a new output variable to hold the value of the transformed data, click the first row in the **Output** column. Then, do the following: 
        1. In the **Name** field, enter `message_data`.
        2. From the **Variable Type** list, select **Output from integration**.
        3. From the **Data Type** list, select **String**.
        4. Click **Create**. The `message_data` variable appears in **Output**.
     3. Drag the `CloudPubSubMessage.attributes` variable from the **Variables** list to the second row in the Input column.
     4. Click the second row in the **Output** column to create a new output variable to hold the value of the JSON payload with the cluster attributes. Complete the following fields:

        1. In the **Name** field, enter `attributes`.
        2. From the **Variable Type** list, select **None**.
        3. From the **Data Type** list, select **JSON**.
        4. Select **Enter a JSON schema** from the **JSON schema options** , and paste the following payload:
               
               {
                 "$schema": "http://json-schema.org/draft-07/schema#",
                 "type": "object",
                 "properties": {
                   "cluster_name": {
                     "type": "string"
                   },
                   "payload": {
                     "type": "string"
                   },
                   "project_id": {
                     "type": "string"
                   },
                   "cluster_location": {
                     "type": "string"
                   },
                   "type_url": {
                     "type": "string"
                   }
                 }
               }
               

        5. Click **Create**. The `attributes` variable appears in **Output**. Make sure the attributes variable looks similar to the following:

![Application Integration Local Variables](https://docs.cloud.google.com/static/kubernetes-engine/images/gke_pubsub_email_attributes.png)

     5. Click the third row in the **Input** column and select `attributes.cluster_name` from the **Variables** pane. You might need to start typing _attributes_ to see all 5 attributes defined from the schema entered in previous step.

     6. Click the corresponding row from the **Output** column to create a new output variable that'd hold the value of the cluster name attribute. Complete the following fields:

        1. In the **Name** field, enter `cluster_name`.
        2. From the **Variable Type** list, select **Output from integration**.
        3. From the **Data Type** list, select **String**.
        4. Click **Create**. The `cluster_name` variable appears in **Output**.
     7. Repeat steps **e** and **f** for `project_id`, `cluster_location`, `type_url` and `payload`.

     8. Close the Data Mapping Editor once your mapping is complete. Any changes will be autosaved.




### Add and configure the Data Transformer (Script) task

The Data Transformer task takes variables extracted from the Data Mapping task as input and transforms it into a message body for end user consumption.

To configure the Data Transformer task:

  1. Select **Tasks** to display a list of available tasks.
  2. Click and place the **Data Transformer (Script)** element in the integration editor.
  3. Click the **Data Transformer** task on the designer to open the configuration pane for the task.
  4. To add an edge connection from Data Mapping task to Data Transformer task, hold the pointer over a control point on the Data Mapping, then drag a line to a control point on the Data Transformer task. The edge denotes the flow of control from the Data Mapping task to the Data Transformer task.
  5. Click **Open Data Transformer Editor**. The **Data Transformer Editor** lets you write, edit, and evaluate custom [Jsonnet](https://jsonnet.org/) templates to perform data mapping in your integration. The output is then available as a variable to any other integration task or trigger. For more details on this transformer task, see [Data Transformer Task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task). For this quickstart, follow these steps to create a script:

     1. Click add_box **Create** in the **Variables** left panel. This will open a **Create variable** panel on the right side. Complete the following fields:

        * **Name:** Enter `full_message`.
        * Select `Output from integration` in the **Variable Type** drop-down box.
        * Select `String` in the **Data Type** drop-down box.
        * Click **Create** to create the variable and close the pane. The new `full_message` variable will appear in the **Variables** list.
     2. Select **Script**.

     3. Use the following example script as a template for the message body when notifications are sent from your cluster:
            
            local message_data = std.extVar("message_data");
            local cluster_name = std.extVar("cluster_name");
            local project_id = std.extVar("project_id");
            local cluster_location = std.extVar("cluster_location");
            local type_url = std.extVar("type_url");
            local payload = std.extVar("payload");
            
            {full_message: "Project ID: " + project_id + "\n" +
                          "Cluster Name: " + cluster_name + "\n" +
                          "Location: " + cluster_location + "\n" +
                          "Event Type: " + type_url + "\n" +
                          "Message: " + message_data + "\n" +
                          "Payload: " + std.manifestJson(std.parseJson(payload))}
            

     4. Close the Data Mapping Editor once your mapping is complete. Any changes will be autosaved.




### Add and configure the Send Email task

To configure the Send Email task:

  1. Select **Tasks** in the integration editor to display the list of available tasks.
  2. Click and place the **Send Email** element in the integration editor.
  3. To add an edge connection from Data Transformer task to Send email task, hold the pointer over a control point on the Data Transformer task, then drag a line to a control point on the Send email task. The edge denotes the flow of control from the Data Transformer task to the Send email task.
  4. Click the **Send Email** element on the designer to open the configuration pane of the task. Set the following properties: 
     1. **To Recipient(s)** : Enter an email address. You will use this email to confirm the successful completion of the integration.
     2. **Subject** : Enter `GKE Notifications`.
     3. **Body in Plain Text** : Select the `full_message` variable created earlier in the **Data Transformer** task.
     4. The remaining options can be left in the default configuration.



Your changes to the properties are saved automatically and your canvas should look similar to the following:

![Application Integration canvas](https://docs.cloud.google.com/static/kubernetes-engine/images/canvas_gke_send_email.png)

### Test integration

To test the new integration, go to the navigation bar at the top of your Integration diagram, and click **Test**. It will open a panel on the right side. You can use the following sample Pub/Sub message in the **Add a json value** section:
    
    
    {
      "data": "Node pool projects/my-project/locations/us-central1-c/clusters/cluster-1/nodePools/default-pool is upgrading to version 1.29.1-gke.1589017.",
      "attributes": {
        "cluster_location": "us-central1-c",
        "cluster_name": "cluster-1",
        "payload": "{\"resourceType\":\"NODE_POOL\",\"operation\":\"operation-upgrade\",\"operationStartTime\":\"2024-05-07T20:09:35.528855756Z\",\"currentVersion\":\"1.28.7-gke.1026000\",\"targetVersion\":\"1.29.1-gke.1589017\",\"resource\":\"projects/my-project/locations/us-central1-c/clusters/cluster-1/nodePools/default-pool\"}",
        "project_id": "my-project",
        "type_url": "type.googleapis.com/google.container.v1beta1.UpgradeEvent"
      }
    }
    

An email is sent to the email address that you have configured in the Send Email task after clicking the **Test Integration** button.

### Publish your integration

After you test this integration successfully, click **Publish** for your integration to start processing the messages.

You can edit only a `DRAFT` version of the integration, and execute only the `ACTIVE` version of the integration. If you want to edit your integration, click **Enable Editing** on the integration designer page and then create a draft version. For more information, see [Integration edit locks](https://docs.cloud.google.com/application-integration/docs/view-integration-details#integration-edit-locks).

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

  1. [Delete your Application Integration](https://docs.cloud.google.com/application-integration/docs/view-integration-details#delete-integrations).

  2. [Delete your Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#deleting_a_topic).




## What's next

  * Learn about [the types of cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).
  * Check out the [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
