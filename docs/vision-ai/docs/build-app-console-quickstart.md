---
url: https://docs.cloud.google.com/vision-ai/docs/build-app-console-quickstart/
title: Quickstart: Build an app in the console \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:23.244880+00:00
---

# Quickstart: Build an app in the console  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/build-app-console-quickstart/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build an app in the console

Learn how to create a simple Gemini Enterprise Agent Platform Vision object detector app in the Google Cloud console.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=vertex-ai-vision--build-app-console-quickstart)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vision AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=visionai.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vision AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=visionai.googleapis.com)




## Create an object detector application

After you have set up your environment, you can create your app.

In the Google Cloud console, an app is represented as a graph. Additionally, in Gemini Enterprise Agent Platform Vision, an app graph must have at least two nodes: a video source node (stream), and _at least_ one more node (a processing model or output destination).

### Create an empty app

Before you can populate the app graph, you must first create an empty app.

### Console

Create an app in the Google Cloud console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Click the add**Create** button.

  3. Enter `quickstart-app` as the app name and choose your region.

  4. Click **Create**.




### Add app component nodes

After you have created the empty application, you can then add the three nodes to the app graph: the **ingestion node** that can receive stream data, the **processing node** that performs a computer image task on data, and a **data destination node** , a warehouse storage destination in this example.

### Console

Add component nodes to your app in the console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `quickstart-app` application in the list, select schema**View app**. This takes you to the graph visualization of the processing pipeline.




**Add a data ingestion node**

  1. To add an input stream node, select the **Streams** option in the **Connectors** section of the side menu.

  2. In the **Source** section of the **Stream** menu that opens, select add**Add streams**.

  3. In the **Add streams** menu, choose radio_button_checked**Register new streams** and add `quickstart-stream` as the stream name.

  4. To add the stream to the app graph, click **Add streams**.




**Add a data processing node**

  1. To add the object detector model node, select the **Object detector** option in the **Pre-trained models** section of the side menu.

![Add object detector model in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/add-object-detector-node.png)




**Add a data storage node**

  1. To add the output destination (storage) node, select the **Gemini Enterprise Agent Platform Vision's Media Warehouse** option in the **Connectors** section of the side menu.

  2. In the **Gemini Enterprise Agent Platform Vision's Media Warehouse** menu, click **Connect warehouse**.

  3. In the **Connect warehouse** menu, select radio_button_checked**Create new warehouse**. Name the warehouse `quickstart-warehouse`, and leave the TTL duration at 14 days.

  4. Click the **Create** button to add the warehouse.

![Object detector app graph in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-app-graph.png)




## Deploy your app for use

After you have built your end-to-end app with all the necessary components, the last step to using the app is to deploy it. 

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `quickstart-app` application in the list, select schema**View app**.

  3. From the application graph builder page, click the play_arrow**Deploy** button.

  4. In the following confirmation dialog, select **Deploy**.

The deploy operation might take several minutes to complete. After deployment finishes, green check marks appear next to the nodes.

![Deployed app in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/deployed-object-detector-app.png)




Congratulations! You've just created and deployed your first Gemini Enterprise Agent Platform Vision app. Creating and deploying an app are the first steps in ingesting and using processed media data with Gemini Enterprise Agent Platform Vision.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, either delete the project that contains the resources, or keep the project and delete the individual resources.

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

#### Delete a warehouse

  1. In the Google Cloud console, go to the **Warehouses** page. 

[Go to the Warehouses tab](https://console.cloud.google.com/ai/vision-ai/media-warehouse)

  2. Locate your `quickstart-warehouse` warehouse. 
  3. To delete the warehouse, click more_vert **Actions** , click **Delete warehouse** , and then follow the instructions. 



#### Delete a stream

  1. In the Google Cloud console, go to the **Streams** page. 

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Locate your `quickstart-stream` stream. 
  3. To delete the stream, click more_vert **Actions** , click **Delete stream** , and then follow the instructions. 



#### Delete an app

  1. In the Google Cloud console, go to the **Applications** page. 

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

**Note:** You must first undeploy your app before you can delete it. 
  2. Locate your `quickstart-app` app. 
  3. To delete the app, click more_vert **Actions** , click **Delete application** , and then follow the instructions. 



## What's next

  * Read [Set up a project and a development environment](https://docs.cloud.google.com/vision-ai/docs/cloud-environment) before you use the command line tools.
  * Learn how to [ingest data](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos) into your new app and read about other components you can add in [Build an app](https://docs.cloud.google.com/vision-ai/docs/build-app).
  * Learn about other output storage and processing options in [Connect app output to a data destination ](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination).
  * Read about how to [Search Warehouse data in the console](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse).
  * Read more about [Responsible AI practices](https://ai.google/responsibilities/responsible-ai-practices/).



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/vision-ai/docs/overview)

[ Next Set up a project and a development environment  arrow_forward  ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
