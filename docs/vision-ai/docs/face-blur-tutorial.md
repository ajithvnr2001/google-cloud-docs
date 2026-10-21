---
url: https://docs.cloud.google.com/vision-ai/docs/face-blur-tutorial/
title: Create a face blur app with warehouse storage \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:33.611258+00:00
---

# Create a face blur app with warehouse storage  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/face-blur-tutorial/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Create a face blur app with warehouse storage Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To complete this tutorial you need access to video data with human faces, either Real Time Streaming Protocol ([RTSP](https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol)) video data from a live Internet Protocol ([IP](https://en.wikipedia.org/wiki/IP_camera)) camera, or a local video file.

Gemini Enterprise Agent Platform Vision is an AI-powered platform you can use to ingest, analyze, and store video data. Gemini Enterprise Agent Platform Vision lets you build and deploy AI applications. You can build end-to-end Gemini Enterprise Agent Platform Vision solutions by leveraging Gemini Enterprise Agent Platform Vision's integration with other product components.

To start implementing solutions using the Gemini Enterprise Agent Platform Vision platform, review the following Agent Platform Vision concepts and components:

  * **Streams** : Represent a video streaming layer from your solution. The stream source can be a live video (for example, an IP camera) or a video file (for example, an MP4 file).

  * **Applications** : Enable the connection between a stream and an AI processor to perform a machine learning operation on the video. For example, you can connect a camera stream to an AI model that counts people passing in front of it. 

  * **Media warehouses** : Store the video ingested by streams out to Google Cloud storage. Storing data out to this destination lets you query analysis output and metadata from the AI processors used on data from the ingested streams. 




## Objectives

This tutorial shows you how to do the following:

  * Create a data input stream resource.
  * Begin streaming video data into this stream resource.
  * Create an empty application.
  * Add nodes to your application to stream data, modify data, and store data.
  * Deploy your app for you to use.
  * View processed data output in the Google Cloud console.



Before you begin this tutorial, you must have a streaming video resource to send data to your Gemini Enterprise Agent Platform Vision app. This resource can be either a local video or an RTSP feed. This video data must contain human faces that the sample app can then blur.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Agent Platform Vision](https://docs.cloud.google.com/vision-ai/pricing) (Streams - Data ingested, Streams - Data consumed, Models - Person / face blur, Warehouse - Video storage) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Get the location of your streaming video source, either locally (for example, `./sample_video.mp4`) or IP address of the live RTSP feed (for example, `rtsp://192.168.1.180:540`). You need this information to begin ingesting data into a stream after you create the stream resource. 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Vision AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=visionai.googleapis.com)

  6. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Vision AI > Vision AI Editor** role to the service account. 

To grant the role, find the **Select a role** list, then select **Vision AI > Vision AI Editor**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  7. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  8. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Vision AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=visionai.googleapis.com)

  15. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Vision AI > Vision AI Editor** role to the service account. 

To grant the role, find the **Select a role** list, then select **Vision AI > Vision AI Editor**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  16. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  17. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  18. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  19. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  20. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  21. Installing the `vaictl` tool to ingest data into a stream (OS: Debian GNU/Linux, CPU architecture: x86_64): **Note** : You can also get a Docker image that has the Gemini Enterprise Agent Platform Vision SDK and all its dependencies already pre-installed. For information about getting a Docker image with the Gemini Enterprise Agent Platform Vision SDK, [Set up a project and a development environment](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#get-docker). 
     1. Download the required package: 
            
            wget https://github.com/google/visionai/releases/download/v0.0.5/visionai_0.0-5_amd64.deb

     2. After downloading the package, run the following command in the directory you downloaded the file: 
            
            sudo apt install ./visionai_0.0-5_amd64.deb

     3. Verify installation: 
            
            vaictl --help




## Create a stream

To create a streaming video analysis app, you must first create and register a stream resource. As the resource that receives the video data from the users, the stream is required on any scenario you build using Gemini Enterprise Agent Platform Vision. 

###  Console 

To create a new stream in the Google Cloud console, use the following steps.

  1. Open the **Streams** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Click add**Register**.

  3. Enter `input-stream` as the stream name and select the region where you want to create your stream.

  4. Click **Register** to create one or more streams.

![Register streams options in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/register-streams.png)




## Ingest video into the stream

After you create a stream resource, you can use the `vaictl` command-line tool to send video data to the stream.

**Note:** If you installed the `vaictl` tool using the Docker container option, you must [run your container](https://docs.docker.com/engine/reference/commandline/container_run/) and sign in before proceeding with the next steps.

### IP camera

If you're testing using a live IP camera, you need to get the IP address of the camera. You must provide this information with the request, along with other variable substitutions: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. For more information, see [Cloud locations](https://cloud.google.com/about/locations). 
  * RTSP_ADDRESS: The address of your Real Time Streaming Protocol ([RTSP](https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol)) feed. For example, `rtsp://192.168.1.180:540`. 



This command sends an RTSP feed into the stream. You must run this command in the network that has direct access to the RTSP feed. 
    
    
    vaictl -p PROJECT_ID \
           -l LOCATION_ID \
           -c application-cluster-0 \
           --service-endpoint visionai.googleapis.com \
    send rtsp to streams input-stream --rtsp-uri RTSP_ADDRESS
          

If the command runs successfully, you get the following output:
    
    
    [...]
    Waiting for long running operation projects/your-project/locations/us-central1/operations/operation-1651364156981-5dde82db7e4a9-dfb17ca5-1051eb20 ⠙
    I20220430 21:16:28.024988 211449 gstvaisink.cc:417] cluster-id=application-cluster-0
    I20220430 21:16:28.025032 211449 gstvaisink.cc:418] cluster-endpoint=c8khq35ftg78mn61ef50.us-central1.visionai.goog
    I20220430 21:16:28.025040 211449 gstvaisink.cc:419] event-id=ev-1651364114183255223
    I20220430 21:16:28.025048 211449 gstvaisink.cc:420] stream-id=input-stream
    I20220430 21:16:28.025053 211449 gstvaisink.cc:421] series-id=ev-1651364114183255223--input-stream**I20220430 21:16:28.025060 211449 gstvaisink.cc:422] Sending data**
    

### Local video file

You can also send video file data to a stream instead of a live video feed. This option can be useful if you don't have access to an IP camera. 

The only difference in this option is the `vaictl` command parameters. Instead of passing the IP camera information, pass the path for the local video file. Make the following variable substitutions: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [More information](https://cloud.google.com/about/locations). 
  * LOCAL_FILE.EXT: The filename of a local video file. For example, `my-video.mp4`. 
  * `--loop` flag: Optional. Loops file data to simulate streaming. 



This command streams a video file to a stream. If using the `--loop` flag, the video is looped into the stream until you stop the command: 
    
    
    vaictl -p PROJECT_ID \
           -l LOCATION_ID \
           -c application-cluster-0 \
           --service-endpoint visionai.googleapis.com \
    send video-file to streams 'input-stream' --file-path LOCAL_FILE.EXT --loop
    

It might take ~100 seconds between starting the `vaictl` ingest operation and the video appearing in the dashboard.

After the stream ingestion is available, you can see the video feed in the **Streams** tab of the Gemini Enterprise Agent Platform Vision dashboard by selecting the `input-stream` stream.

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

![View of live video being streamed in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/video-ingested-to-stream-UI_mods.png)_Live view of video being ingested into the stream in the Google Cloud console. Video credit:_ [Tima Miroshnichenko](https://www.pexels.com/video/young-women-reading-books-while-sitting-on-the-bed-6860996/) on [Pexels](https://www.pexels.com/) (_pixelation added_). 

## Create a face blur application

After you create a stream and ingest data into the stream, it's time to create a Gemini Enterprise Agent Platform Vision app to process the data. An app can be thought of as an automated pipeline that connects the following:

  * **Data ingestion** : A video feed is ingested into a stream.
  * **Data analysis** : An AI model can be added after the ingestion. Any computer vision operation can be performed on the ingested video information.
  * **Data storage** : The two versions of the video feed (the original stream and the stream processed by the AI model) can be stored in a media warehouse.



In the Google Cloud console an app is represented as a graph. Additionally, in Gemini Enterprise Agent Platform Vision an app graph must have at least two nodes: a video source node (stream), and _at least_ one more node (a processing model or output destination).

### Create an empty application

Before you can populate the app graph, you must first create an empty app. 

### Console

Create an app in the Google Cloud console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Click the add**Create** button.

  3. Enter `person-blur-app` as the app name and choose your region.

  4. Click **Create**.

![Create a new app dialog in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/create-empty-app.png)




### Add app component nodes

After you have created the empty application, you can then add the three nodes to the app graph:

  1. **Ingestion node** : The stream resource that's already ingesting data.
  2. **Processing node** : The person blur model that acts on ingested data.
  3. **Storage node** : The media warehouse that stores processed videos, and also serves as a metadata store. The warehouse allows analytics information to be generated about ingested video data, as well as stores information inferred about the data by the AI models.



### Console

Add component nodes to your app in the console.

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `person-blur-app` application in the list, select schema**View app**. This takes you to the graph visualization of the processing pipeline.




**Add a data ingestion node**

  1. To add the input stream node, select the **Streams** option in the **Connectors** section of the side menu.

  2. In the **Source** section of the **Stream** menu that opens, select add**Add streams**.

  3. In the **Add streams** menu, choose radio_button_checked**Select from existing streams** and select `person-blur-app` from the list of stream resources.

![Add streams menu in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/add-input-stream.png)

  4. To add the stream to the app graph, click **Add streams**.




**Add a data processing node**

  1. To add the person blur model node, select the **Person blur** option in the **General processors** section of the side menu.

  2. In the "Person blur" option menu that opens, leave radio_button_checked**Full occlusion** selected and enable the check_box**Blur faces only** option.

![Add face blur model in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/add-face-blur-node.png)




**Add a data storage node**

  1. To add the output destination (storage) node, select the **Gemini Enterprise Agent Platform Vision's Media Warehouse** option in the **Connectors** section of the side menu.

  2. In the **Gemini Enterprise Agent Platform Vision's Media Warehouse** menu, click **Connect warehouse**.

  3. In the **Connect warehouse** menu, select radio_button_checked**Create new warehouse**. Name the warehouse `person-blur-app`, and leave the TTL duration at 14 days.

  4. To add the warehouse, click **Create**.

![Add warehouse node in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/add-blur-warehouse-node.png)




## Deploy your application

After you have built your end-to-end app with all the necessary components, the last step to using the app is to deploy it. 

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Next to the name of your `person-blur-app` application in the list, select schema**View app**.

  3. From the application graph builder page, click the play_arrow**Deploy** button.

  4. In the following confirmation dialog, select **Deploy**.

The deploy operation might take several minutes to complete. After deployment finishes, green check marks appear next to the nodes.

![Deployed app in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/deployed-blur-app.png)




## View processed output data

###  Console 

  1. Open the **Warehouses** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Warehouses tab](https://console.cloud.google.com/ai/vision-ai/media-warehouse)

  2. Find the `person-blur-output-storage` warehouse in the list, and click widgets**View assets**.

![View app output in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/view-output-placeholder3.png)




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

#### Delete a warehouse

  1. In the Google Cloud console, go to the **Warehouses** page. 

[Go to the Warehouses tab](https://console.cloud.google.com/ai/vision-ai/media-warehouse)

  2. Locate your `person-blur-output-storage` warehouse. 
  3. To delete the warehouse, click more_vert **Actions** , click **Delete warehouse** , and then follow the instructions. 



#### Delete a stream

  1. In the Google Cloud console, go to the **Streams** page. 

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Locate your `input-stream` stream. 
  3. To delete the stream, click more_vert **Actions** , click **Delete stream** , and then follow the instructions. 



#### Delete an app

  1. In the Google Cloud console, go to the **Applications** page. 

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

**Note:** You must first undeploy your app before you can delete it. 
  2. Locate your `person-blur-app` app. 
  3. To delete the app, click more_vert **Actions** , click **Delete application** , and then follow the instructions. 



## What's next

  * Read more about [Responsible AI practices](https://ai.google/responsibilities/responsible-ai-practices/).
  * Learn about other components you can add to an app in [Build an app](https://docs.cloud.google.com/vision-ai/docs/build-app).
  * Learn about other output storage and processing options in [Connect app output to a data destination ](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination).
  * Read about how to [Search Warehouse data in the console](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
