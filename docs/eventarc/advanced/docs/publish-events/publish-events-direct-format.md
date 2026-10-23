---
url: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format/
title: Publish events directly \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:50.118547+00:00
---

# Publish events directly  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Publish events directly Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

You can publish a CloudEvents event directly to an Eventarc Advanced bus in a supported format using the Google Cloud CLI or by sending a request to the Eventarc Publishing REST API. You can also use the [Eventarc client libraries](https://docs.cloud.google.com/eventarc/docs/reference/libraries) to access the Eventarc APIs from a supported language.

## Before you begin

Before you start, make sure that you have completed the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable eventarc.googleapis.com eventarcpublishing.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable eventarc.googleapis.com eventarcpublishing.googleapis.com




## Publish directly

The event message you publish directly must conform to the [CloudEvents specification](https://docs.cloud.google.com/eventarc/advanced/docs/event-format).

###  gcloud 

  1. Open a terminal.

  2. You can publish events to a bus by using the [`gcloud eventarc message-buses publish`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/publish) command. For example:
         
         gcloud eventarc message-buses publish BUS_NAME \
             --avro-message=AVRO_MESSAGE

Or: 
         
         gcloud eventarc message-buses publish BUS_NAME \
             --json-message=JSON_MESSAGE

Or: 
         
         gcloud eventarc message-buses publish BUS_NAME \
             --event-data=DATA_PAYLOAD \
             --event-id=EVENT_ID \
             --event-source=EVENT_SOURCE \
             --event-type=EVENT_TYPE \
             --event-attributes=EVENT_ATTRIBUTE

Replace the following:

     * `BUS_NAME`: the ID or fully qualified identifier of the bus to which to publish the event.

You must use only _one_ of the following:

     * `AVRO_MESSAGE`: the event message in an Avro format according to this [specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/avro-format.md).
     * `JSON_MESSAGE`: the event message in a JSON format according to this [specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/json-format.md).
     * `DATA_PAYLOAD`: the data of a published event.

If using the `--event-data` flag, you must also use the following:

     * `EVENT_ID`: the event identifier. Event producers must ensure that `source` \+ `id` is unique for each distinct event.
     * `EVENT_SOURCE`: the event source of a published event.
     * `EVENT_TYPE`: the type of event related to the originating occurrence.

If using the `--event-data` flag, you can optionally use the following:

     * `EVENT_ATTRIBUTE`: the attributes of a published event. You can repeat the `--event-attributes` flag to add more attributes.

Note that events might include any number of additional custom CloudEvents attributes with distinct names (also known as [extension attributes](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#extension-context-attributes)).




### Examples:
    
    
    gcloud eventarc message-buses publish my-bus \
        --event-data='{"key": "hello-world-data"}' \
        --event-id=hello-world-id-1234 \
        --event-source=hello-world-source \
        --event-type=hello-world-type \
        --event-attributes="datacontenttype=application/json"
    
    
    gcloud eventarc message-buses publish my-bus --json-message='{
        "specversion" : "1.0",
        "type" :"com.example.someevent",
        "source" : "google.cloud.storage.object.v1.finalized",
        "id" : "A234-1234-1234",
        "time" : "2024-04-05T17:31:00Z",
        "bucket" : "bucketName",
        "datacontenttype" : "application/json",
        "data":{"key": "value"}
    }'

### REST API

To publish an event to a bus, use the [`projects.locations.messageBuses.publish`](https://docs.cloud.google.com/eventarc/docs/reference/publishing/rest/v1/projects.locations.messageBuses/publish) method.

**Note:** In the `ProtoMessage` of the request body, the `protoData` field only functions as expected when the payload is specifically a `CloudEvent` message type, and can't be used for arbitrary protocol buffer messages. For any other protocol buffer type, you must serialize your proto message into bytes, and use the `binaryData` field instead.

Before using any of the request data, make the following replacements: 

  * The full resource name of the bus in the format `projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME`

Replace the following:

    * `PROJECT_ID`: the Google Cloud project ID for the bus project.
    * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the bus is deployed—for example, `us-central1`.
    * `BUS_NAME`: the name of the bus to which to publish the event.
  * `SPEC_VERSION`: the version of the CloudEvents specification which the event uses—for example, `1.0`.
  * `EVENT_TYPE`: the type of event related to the originating occurrence.
  * `EVENT_SOURCE`: the event source of a published event.
  * `EVENT_ID`: the event identifier. Producers must ensure that `source` \+ `id` is unique for each distinct event.
  * `CONTENT_TYPE` (optional): the content type of `data` value. If a JSON format event has no `datacontenttype` attribute, then it is assumed that the data is a JSON value conforming to the `application/json` media type.
  * `DATA_PAYLOAD` (optional): the event payload encoded into the media format specified by `datacontenttype` and adhering to `dataschema` when those attributes are present.



Request JSON body: 
    
    
    {
    "jsonMessage":
      "{\"specversion\":\"SPEC_VERSION\",
      \"type\":\"EVENT_TYPE\",
      \"source\":\"EVENT_SOURCE\",
      \"id\":\"EVENT_ID\",
      \"datacontenttype\":\"CONTENT_TYPE\",
      \"data\":\"DATA_PAYLOAD\"}"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
    "jsonMessage":
      "{\"specversion\":\"SPEC_VERSION\",
      \"type\":\"EVENT_TYPE\",
      \"source\":\"EVENT_SOURCE\",
      \"id\":\"EVENT_ID\",
      \"datacontenttype\":\"CONTENT_TYPE\",
      \"data\":\"DATA_PAYLOAD\"}"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarcpublishing.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME:publish"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
    "jsonMessage":
      "{\"specversion\":\"SPEC_VERSION\",
      \"type\":\"EVENT_TYPE\",
      \"source\":\"EVENT_SOURCE\",
      \"id\":\"EVENT_ID\",
      \"datacontenttype\":\"CONTENT_TYPE\",
      \"data\":\"DATA_PAYLOAD\"}"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarcpublishing.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME:publish" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/publishing/rest/v1/projects.locations.messageBuses/publish). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the server returns an HTTP `200 OK` status code and the empty response body in JSON format: 
    
    
    200 OK
    
    {}
    

## What's next

  * [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources)
  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)
  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
