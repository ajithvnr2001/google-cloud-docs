---
url: https://docs.cloud.google.com/eventarc/docs/managing-triggers/
title: Manage triggers \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:27.164257+00:00
---

# Manage triggers  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/managing-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Manage triggers Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Eventarc triggers let you route events from event providers to target destinations. Viewing, updating, and deleting triggers helps you control event delivery and maintain your event-driven architectures. You can perform these tasks using the Google Cloud console, the Google Cloud CLI in your terminal or [Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true), or the Eventarc API.

## List triggers

You can list, filter, and sort through your triggers in all locations.

### Console

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

This lists all the triggers in your project for all locations, and includes details such as the trigger name, region, event provider, destination, and event type.

  2. To filter your triggers by a specific property:

     1. Click the filter_list **Filter** box.
     2. From the list of **Properties** , select an option to filter the triggers by—for example, **Name** or **Event channel**.

You can select a single property or use the logical operator `OR` to add more properties to filter by.

  3. To sort your triggers, click arrow_upward **Sort** beside the appropriate column heading.

Only some columns are sortable—for example, **Name** , **Region** , or **Event channel**.




### gcloud
    
    
    gcloud eventarc triggers list --location=-

This command lists your trigger name, type, destination, and status in all locations.

###  REST 

To list triggers in a given project and location, use the [`projects.locations.triggers.list`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the triggers are created—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers" | Select-Object -Expand Content

If successful, the response body contains instances of [`Trigger`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers#resource:-trigger) and the response should be similar to the following: 
    
    
    {
      "triggers": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME",
          "uid": "d700773a-698b-47b2-a712-2ee10b690062",
          "createTime": "2022-12-06T22:44:04.744001514Z",
          "updateTime": "2022-12-06T22:44:09.116459550Z",
          "eventFilters": [
            {
              "attribute": "type",
              "value": "google.cloud.pubsub.topic.v1.messagePublished"
            }
          ],
          "serviceAccount": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
          "destination": {
            "workflow": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME"
          },
          "transport": {
            "pubsub": {
              "topic": "projects/PROJECT_ID/topics/TOPIC_ID",
              "subscription": "projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID"
            }
          }
        },
        {
          object (Trigger)
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }
    

## Describe a trigger

You can describe a trigger in a specific location.

### Console

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. From the list of triggers, click the trigger you want to know the details about.




The **Trigger details** page displays the details of the trigger such as name, region, event provider, event type, event data content type, and destination.

If the event destination is Cloud Run, whether a [retry policy](https://docs.cloud.google.com/eventarc/docs/retry-events#run-targets) is enabled or disabled is indicated.

### gcloud
    
    
    gcloud eventarc triggers describe TRIGGER \
        --location=LOCATION

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger.



This command returns information about the trigger that is similar to the following:
    
    
      createTime: '2023-03-16T13:40:44.889670204Z'
      destination:
        cloudRun:
          path: /
          region: us-central1
          service: hello
      eventDataContentType: application/protobuf
      eventFilters:
      - attribute: serviceName
        value: cloudscheduler.googleapis.com
      - attribute: methodName
        value: google.cloud.scheduler.v1.CloudScheduler.DeleteJob
      - attribute: type
        value: google.cloud.audit.log.v1.written
      name: projects/project-name/locations/us-central1/triggers/name-of-trigger
      serviceAccount: project-number-compute@developer.gserviceaccount.com
      transport:
        pubsub:
          subscription: projects/project-name/subscriptions/eventarc-us-central1-name-of-trigger-sub-034
          topic: projects/project-name/topics/eventarc-us-central1-name-of-trigger-931
    

###  REST 

To describe a trigger in a given project and location, use the [`projects.locations.triggers.get`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers/get) method.

Before using any of the request data, make the following replacements: 

  * `TRIGGER_NAME`: the name of the trigger you want to describe.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the trigger is created—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME" | Select-Object -Expand Content

If successful, the response body contains an instance of [`Trigger`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers#Trigger) similar to the following: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME",
      "uid": "d700773a-698b-47b2-a712-2ee10b690062",
      "createTime": "2022-12-06T22:44:04.744001514Z",
      "updateTime": "2022-12-06T22:44:09.116459550Z",
      "eventFilters": [
        {
          "attribute": "type",
          "value": "google.cloud.pubsub.topic.v1.messagePublished"
        }
      ],
      "serviceAccount": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
      "destination": {
        "workflow": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME"
      },
      "transport": {
        "pubsub": {
          "topic": "projects/PROJECT_ID/topics/TOPIC_ID",
          "subscription": "projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID"
        }
      }
    }
    

If the condition of the trigger indicates an issue with the Pub/Sub topic, refer to [Trigger is not delivering events](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-stopped-working).

## Update a trigger

You can update a trigger for Cloud Run, Google Kubernetes Engine (GKE), and Workflows destinations. Depending on the destination, specific fields can be updated.

**Important:** If you update a trigger before its generated event is delivered, the event is routed according to the previous filtering and delivered to the original destination within three days of the event generation. The new filtering is applied to events generated _after_ your update.

### Console

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. From the list of triggers, click the trigger you want to know the details about.

  3. On the **Trigger details** page, click edit **Edit**.

  4. Edit fields as required and click **Save**.

Note that you can't update any unavailable fields such as the **Event provider** and **Event destination**. For more information about the fields, see the **Console** instructions for a [specific provider, event type, and destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).




### gcloud

### Cloud Run
    
    
    gcloud eventarc triggers update TRIGGER \
        --location=LOCATION \
        --event-filters=NEW_EVENT_FILTERS \
        --service-account=NEW_SERVICE_ACCOUNT \
        --destination-run-region=NEW_REGION \
        --destination-run-service=NEW_SERVICE \
        --destination-run-path=NEW_PATH \
        --event-data-content-type="NEW_EVENT_DATA_TYPE" \
        --max-retry-attempts=1

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger.



You can update any of the following:

  * `NEW_EVENT_FILTERS`: the filter used to configure the event routing of the trigger; for example, `methodName=storage.objects.create` can be updated to `methodName=storage.objects.delete`. Note that after a trigger is created, the `type` event filter can't be changed. For a different event type, you must create a new trigger.
  * `NEW_SERVICE_ACCOUNT`: the Identity and Access Management (IAM) service account email associated with the trigger.
  * `NEW_REGION`: the region in which the destination Cloud Run service can be found.
  * `NEW_SERVICE`: the name of the Cloud Run service that receives the events for the trigger.
  * `NEW_PATH`: the relative path on the destination Cloud Run service to which the events for the trigger should be sent.
  * `NEW_EVENT_DATA_TYPE`: the encoding of the event payload; depending on the event provider, this can be `application/json` or `application/protobuf`.
  * Optionally, you can use the `--max-retry-attempts` flag to specify a single delivery attempt of an event message with no retries. The only valid value is `1`. This flag applies only to Cloud Run destinations (including Cloud Run functions). To clear the setting, use the `--clear-max-retry-attempts` flag. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).



For example, to update the service account for a trigger:
    
    
    gcloud eventarc triggers update my-cloud-run-trigger \
        --service-account=new-serviceaccount@${PROJECT_ID}.iam.gserviceaccount.com
    

This command updates the service account of a trigger named `my-cloud-run-trigger` to `new-serviceaccount@PROJECT_ID.iam.gserviceaccount.com`.

### GKE

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Note that this section also applies to the public endpoints of private and public services running in a GKE cluster.
    
    
    gcloud eventarc triggers update TRIGGER \
        --location=LOCATION \
        --destination-gke-namespace=NEW_NAMESPACE \
        --destination-gke-service=NEW_SERVICE \
        --destination-gke-path=NEW_PATH \
        --event-data-content-type="NEW_EVENT_DATA_TYPE"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger.



You can update any of the following:

  * `NEW_NAMESPACE`: the namespace in which the destination GKE service is running.
  * `NEW_SERVICE`: the name of the GKE service that receives the events for the trigger.
  * `NEW_PATH`: the relative path on the destination GKE service to which the events for the trigger should be sent.
  * `NEW_EVENT_DATA_TYPE`: the encoding of the event payload; depending on the event provider, this can be `application/json` or `application/protobuf`.



For example, to update the event receiver service for a trigger:
    
    
    gcloud eventarc triggers update my-gke-trigger \
        --destination-gke-service=helloworld-events
    

This command updates the event receiver service for a trigger named `my-gke-trigger` to a GKE service named `helloworld-events`.

### Workflows
    
    
    gcloud eventarc triggers update TRIGGER \
        --location=LOCATION \
        --event-filters=NEW_EVENT_FILTERS \
        --service-account=NEW_SERVICE_ACCOUNT \
        --destination-workflow=NEW_DESTINATION_WORKFLOW \
        --destination-workflow-location=NEW_DESTINATION_WORKFLOW_LOCATION \
        --event-data-content-type="NEW_EVENT_DATA_TYPE"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
  * `LOCATION`: the location of the Eventarc trigger.



You can update any of the following:

  * `NEW_EVENT_FILTERS`: the filter used to configure the event routing of the trigger; for example, `methodName=storage.objects.create` can be updated to `methodName=storage.objects.delete`. Note that after a trigger is created, the `type` event filter can't be changed. For a different event type, you must create a new trigger.
  * `NEW_SERVICE_ACCOUNT`: the Identity and Access Management (IAM) service account email associated with the trigger.
  * `NEW_DESTINATION_WORKFLOW`: the ID of the deployed workflow that receives the events from the trigger.
  * `NEW_DESTINATION_WORKFLOW_LOCATION`: the location in which the destination workflow is deployed.
  * `NEW_EVENT_DATA_TYPE`: the encoding of the event payload; depending on the event provider, this can be `application/json` or `application/protobuf`.



For example, to update the service account for a trigger:
    
    
    gcloud eventarc triggers update my-workflows-trigger \
        --service-account=new-serviceaccount@${PROJECT_ID}.iam.gserviceaccount.com
    

This command updates the service account of a trigger named `my-workflows-trigger` to `new-serviceaccount@PROJECT_ID.iam.gserviceaccount.com`.

###  REST 

To update an existing trigger, use the [projects.locations.triggers.patch](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers/patch) method and optionally use the `updateMask` query parameter to specify a list of fields to be updated.

Before using any of the request data, make the following replacements: 

  * `TRIGGER_NAME`: the name of the trigger you want to update.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the trigger is created—for example, `us-central1`.
  * `SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com`: optional. The Identity and Access Management (IAM) service account email associated with the trigger.
  * `DESTINATION`: optional. Specifies the target where the event should be sent to and contains an instance of [`Destination`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers#destination). For example:

`{"destination": {"workflow": "projects/my-project/locations/us-central1/workflows/my-first-workflow"}}`

or

`{"destination": {"cloudRun": {"service": "hello-world", "region": "us-central1"}}}`

  * `EVENT_FILTER`: optional. The event attributes to filter on. Only updating the method type for Cloud Audit Logs triggers is supported. For example:

`{"eventFilters": [{"attribute": "methodName", "value": "storage.buckets.create"}, {"attribute": "type", "value": "google.cloud.audit.log.v1.written"}, {"attribute": "serviceName", "value": "storage.googleapis.com"}]}`

Note that you can't update method types for GKE destinations.

  * `CONTENT_TYPE`: optional. The encoding of the event payload; depending on the event provider, this can be `application/json` or `application/protobuf`.
  * `RETRY_POLICY`: optional. The maximum number of event delivery attempts. Valid value is `1`, indicating a single delivery attempt with no retries, and applies only to Cloud Run destinations (including Cloud Run functions). For example: 

`{"retryPolicy": {"maxAttempts": 1}}`

For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).
  * `UPDATE_FIELDS`: optional. A comma-separated list of fields to be updated. If not provided, all provided fields in the request are updated. For example: `serviceAccount,destination`



Request JSON body: 
    
    
    {
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "destination": DESTINATION,
      "eventFilters": EVENT_FILTER,
      "eventDataContentType": "CONTENT_TYPE",
      "retryPolicy": RETRY_POLICY
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "destination": DESTINATION,
      "eventFilters": EVENT_FILTER,
      "eventDataContentType": "CONTENT_TYPE",
      "retryPolicy": RETRY_POLICY
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME?updateMask="UPDATE_FIELDS""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "destination": DESTINATION,
      "eventFilters": EVENT_FILTER,
      "eventDataContentType": "CONTENT_TYPE",
      "retryPolicy": RETRY_POLICY
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME?updateMask="UPDATE_FIELDS"" | Select-Object -Expand Content

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

If the value of `"done"` is `false`, the operation is still in progress.

## Delete a trigger

**Important:** Deleting a trigger also deletes any new Pub/Sub topic that was initially created by Eventarc when the trigger was created.

You can delete a trigger.

### Console

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Select the trigger and click delete **Delete**.




### gcloud
    
    
    gcloud eventarc triggers delete TRIGGER

Replace `TRIGGER` with the ID of the trigger or a fully qualified identifier.

###  REST 

To delete a trigger with a specified name, use the [`projects.locations.triggers.delete`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers/delete) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the trigger is created—for example, `us-central1`.
  * `TRIGGER_NAME`: the name of the trigger you want to delete.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME" | Select-Object -Expand Content

If successful, the response body contains an instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-24T17:53:52.834876290Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_NAME",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

If the value of `"done"` is `false`, the operation is still in progress.

## What's next

  * [Create a trigger for a specific provider, event type, and destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
