---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets/
title: Set up notifications on a secret \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:17.095981+00:00
---

# Set up notifications on a secret  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Set up notifications on a secret Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure and use event notifications for your secrets in Secret Manager.

## Overview

Secret Manager integrates with Pub/Sub to provide event notifications for changes to both secrets and secret versions. You can use these notifications to initiate workflows, such as restarting an application when a new secret version is added, or notifying security engineers when a secret is deleted. For more information on how to use these notifications to start workflows, see the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs).

### How event notifications work in Secret Manager

Secrets can be configured with a list of up to 10 Pub/Sub topics. Whenever an operation is performed that modifies the secret or one of its versions, Secret Manager automatically publishes a message to each of the Pub/Sub topics on that secret. `Get`, `List`, and `Access` calls _don't_ result in message publications.

Pub/Sub messages have a set of attribute key-value pairs containing metadata about the event, as well as a [data](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage.FIELDS.bytes.google.pubsub.v1.PubsubMessage.data) field containing a full JSON serialization of the [`Secret`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) or [`SecretVersion`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions) resource which was created or modified. This JSON is a UTF-8 encoded string that represents the `Secret` or `SecretVersion` resource in exactly the form specified by the Secret Manager public API, encoded in JSON as specified in the [proto3 JSON Mapping](https://developers.google.com/protocol-buffers/docs/proto3#json).

## Event types

**Important:** Additional event types might be released later. You must write your code for consuming Secret Manager event notifications with the assumption that new event types can be added. 

The following is a list of event types supported by Secret Manager.

Event type | Description  
---|---  
`SECRET_CREATE` | Sent when a new secret is successfully created.  
`SECRET_UPDATE` | Sent when a new secret is successfully updated.  
`SECRET_DELETE` | Sent when a secret is deleted, either because of a user-initiated request or secret expiration.  
`SECRET_VERSION_ADD` | Sent when a new secret version is successfully added.  
`SECRET_VERSION_ENABLE` | Sent when a secret version is enabled.  
`SECRET_VERSION_DISABLE` | Sent when a secret version is disabled.  
`SECRET_VERSION_DESTROY` | Sent when a secret version is destroyed.  
`SECRET_VERSION_DESTROY_SCHEDULED` | Sent when a [destruction delay duration](https://docs.cloud.google.com/secret-manager/regional-secrets/delay-destroy-regional-secret-version) is configured on the secret and the user attempts to destroy a secret version.  
`SECRET_ROTATE` | Sent when it is time to rotate a secret. See [Create rotation schedules](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets) for more information.  
`TOPIC_CONFIGURED` |  This is a test message with no body or attributes other than `eventType: TOPIC_CONFIGURED`. This is sent when a secret is created or updated with a list of Pub/Sub topics, but does _not_ indicate that the operation was successful. A `SECRET_CREATE` or `SECRET_UPDATE` message is sent immediately afterwards if the operation was successful. Whenever topics are updated on a secret, a `TOPIC_CONFIGURED` message is sent to all topics on the secret, including ones that were already present.  
  
## Notification format

Notifications sent to the Pub/Sub topic consist of two parts:

  * **Attributes** : A set of key-value pairs describing the event.

  * **Data** : A string that contains the metadata of the changed object.




### Attributes

Attributes are key-value pairs contained in notifications sent by Secret Manager to your Pub/Sub topic. All notifications other than `TOPIC_CONFIGURED` test messages always contain the following set of key:value pairs, regardless of the notification's data:

Attribute name | Example | Description  
---|---|---  
`eventType` | `SECRET_CREATE` | The type of event that has just occurred. See [Event types](https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets#events) for a list of possible values.  
`dataFormat` | `JSON_API_V1` | The format of the object data.  
`secretId` | `projects/p/secrets/my-secret` | The full resource name of the secret on which the event occurred.  
`timestamp` | `2021-01-20T11:17:45.081104-08:00` | The time the event occurred.  
  
In addition, notifications sometimes contain the following set of key-value pairs:

Attribute name | Example | Description  
---|---|---  
`versionId` | `projects/p/secrets/my-secret/versions/456` |  The name of the secret version on which the event occurred. This is only present on `SECRET_VERSION_ADD`, `SECRET_VERSION_ENABLE`, `SECRET_VERSION_DISABLE`, and `SECRET_VERSION_DESTROY` event notifications.   
`deleteType` | `REQUESTED` |  Whether the delete was requested by a user (`REQUESTED`) or due to secret expiration (`EXPIRATION`). Only present on `SECRET_DELETE` event notifications.   
  
### Data

The data field is a UTF-8 string that contains the metadata of the changed object. Data is either a secret or secret version.

For `SECRET_DELETE` notifications, the metadata contained in the data field represents the object metadata as it was before the delete. For all other notifications, the metadata included in the data field represents the object metadata _after_ the change occurs.

## Limitations

  * Event notifications is available only in the Secret Manager [v1](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) API and Google Cloud CLI. 

  * You can't reliably use event notifications with Pub/Sub topics that have a [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction#message_storage_policy_overview) where `enforceInTransit` is set to `true`. 

Secret Manager publishes all event notifications from a global endpoint. If a Pub/Sub topic has `enforceInTransit` set to `true`, it restricts publishing to specific `allowedPersistenceRegions`. The regional restriction conflicts with the global publishing endpoint for Secret Manager, causing the publish request to fail with a `FAILED_PRECONDITION` error. 




## Before you begin

You may choose to store all resources in the same project or to store secrets and Pub/Sub topics in separate projects.

  1. To set up Secret Manager, complete the following:

     * Create or use an existing project to hold your Secret Manager resources.

     * If necessary, complete the steps mentioned in the [Enable the Secret Manager API](https://docs.cloud.google.com/secret-manager/regional-secrets/config-sm-rs) page.

  2. To set up Pub/Sub, complete the following:

     * Create or use an existing project to hold your Pub/Sub resources.

     * If necessary, [enable the Pub/Sub API](https://docs.cloud.google.com/pubsub/docs/create-topic-console#before-you-begin).

  3. Authenticate to Google Cloud using the following command:
         
         $ gcloud auth login --update-adc
             




## Create a service agent identity

To create a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) identity for each project that requires secrets with event notifications, follow these steps:

  1. To create a service identity with Google Cloud CLI, run the following command:
         
         $ gcloud beta services identity create \
                   --service "secretmanager.googleapis.com" \
                   --project "PROJECT_ID"
             

This command returns a service account name, with the following format:
         
         service-PROJECT_NUMBER@gcp-sa-secretmanager.iam.gserviceaccount.com
             

  2. Grant this service account permission to publish on the Pub/Sub topics configured on your secrets.

  3. Save the service account name as an environment variable using the following command:
         
         # This is from the output of the command above
             $ export SM_SERVICE_ACCOUNT="service-...."
             




The environment variables for the Secret Manager project, Pub/Sub project, and Secret Manager service account must be set the entire time you are following this procedure.

## Create Pub/Sub topics

Follow the [Pub/Sub quickstart](https://docs.cloud.google.com/pubsub/docs/create-topic-console) to create topics in your Pub/Sub project in the Google Cloud console. Alternatively, create topics in the Google Cloud CLI using the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * PUBSUB_PROJECT_ID: the ID of the project in which to create subscriptions
  * PUBSUB_TOPIC_NAME: the name of the topic



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

Repeat this multiple times if you want to create multiple Pub/Sub topics on the secret.

## Grant the service account for Secret Manager permission to publish on the topics

You can grant permissions to the Secret Manager service account through the Google Cloud console or through Google Cloud CLI.

**Note:** To grant the service account permission to publish on a topic, you must have the `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles. 

To grant the Pub/Sub Publisher role (`roles/pubsub.publisher`) on the Pub/Sub topic, use the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * PUBSUB_TOPIC_NAME: the name of the topic



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics add-iam-policy-binding PUBSUB_TOPIC_NAME \
        --member "serviceAccount:${SM_SERVICE_ACCOUNT}" \
        --role "roles/pubsub.publisher"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics add-iam-policy-binding PUBSUB_TOPIC_NAME `
        --member "serviceAccount:${SM_SERVICE_ACCOUNT}" `
        --role "roles/pubsub.publisher"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics add-iam-policy-binding PUBSUB_TOPIC_NAME ^
        --member "serviceAccount:${SM_SERVICE_ACCOUNT}" ^
        --role "roles/pubsub.publisher"

## Create Pub/Sub subscriptions

To view the messages published to a topic, you must also create a subscription to the topic. Follow the [Pub/Sub quickstart](https://docs.cloud.google.com/pubsub/docs/create-topic-console) to create subscriptions in your Pub/Sub project in the Google Cloud console. Alternatively, create topics in the Google Cloud CLI using the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * PUBSUB_PROJECT_ID: the ID of the project in which to create subscriptions
  * PUBSUB_SUBSCRIPTION_NAME: the name of the subscription
  * PUBSUB_TOPIC_NAME: the name of the topic



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub subscriptions create projects/PUBSUB_PROJECT_ID/subscriptions/PUBSUB_SUBSCRIPTION_NAME \
      --topic projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub subscriptions create projects/PUBSUB_PROJECT_ID/subscriptions/PUBSUB_SUBSCRIPTION_NAME `
      --topic projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub subscriptions create projects/PUBSUB_PROJECT_ID/subscriptions/PUBSUB_SUBSCRIPTION_NAME ^
      --topic projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME

## Create a secret with topics configured

Create a secret with a list of up to 10 topics configured. All topics configured on a secret receive event notifications when the secret or one of its versions changes.

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * PUBSUB_TOPIC_NAME: the name of the topic
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --topics PUBSUB_TOPIC_NAME --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --topics PUBSUB_TOPIC_NAME --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --topics PUBSUB_TOPIC_NAME --location=LOCATION

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TOPIC_NAME: the name of the topic



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {
      "topics":{
        "name": "TOPIC_NAME"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "/projects/my-project/locations/me-central2/secrets/my-drz-secret",
      "createTime": "2024-03-25T08:24:13.153705Z",
      "etag": "\"161477e6071da9\""
    }
    

## Update secret topics

Modify the Pub/Sub topics configured on a secret by updating the secret with the new Pub/Sub topic resource names. With Google Cloud CLI you can add or remove one or more topics from a secret, as well as clear all topics from the secret.

**Note:** When updating topics with the API, you must specify the full set of topics for the secret with each `PATCH` request. You can't specify particular topics to add or remove, but must provide the full list each time. 

### Add topics

To add one or more topics to a secret, use the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID that contains the secret
  * PUBSUB_PROJECT_ID: the ID of the project in which to create subscriptions
  * PUBSUB_TOPIC_1_NAME and PUBSUB_TOPIC_2_NAME: the names of the topics that you are adding to the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
      --project PROJECT_ID \
      --add-topics projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
      --project PROJECT_ID `
      --add-topics projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
      --project PROJECT_ID ^
      --add-topics projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2_NAME

### Remove topics

To remove one or more topics from a secret, use the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project that contains the secret
  * PUBSUB_PROJECT_ID: the ID of the project in which to create subscriptions
  * PUBSUB_TOPIC_1_NAME and PUBSUB_TOPIC_2_NAME: the names of the topics that you are removing from the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
      --project PROJECT_ID \
      --remove-topics "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2__NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
      --project PROJECT_ID `
      --remove-topics "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2__NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
      --project PROJECT_ID ^
      --remove-topics "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_1_NAME,projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_2__NAME

### Clear topics

To remove all topics from a secret, use the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * PROJECT_ID: the Google Cloud project that contains the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
      --project PROJECT_ID \
      --clear-topics

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
      --project PROJECT_ID `
      --clear-topics

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
      --project PROJECT_ID ^
      --clear-topics

## Consume event notifications with Cloud Run functions

Event notifications can be used to initiate workflows by creating Cloud Run functions to consume the Pub/Sub messages. See the [Cloud Run functions documentation](https://docs.cloud.google.com/functions/docs/tutorials/pubsub) for more information. The following sample code is for a Cloud Run function that prints `eventType`, `secretId`, and metadata whenever an event is published to the topic.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Secret Manager C# SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    // Triggered from a message on a Cloud Pub/Sub topic.
    // The printed value will be visible in Cloud Logging
    // (https://cloud.google.com/functions/docs/monitoring/logging).
    namespace PubSubSample
    {
        public class Function : ICloudEventFunction<MessagePublishedData>
        {
            public Task HandleAsync(CloudEvent cloudEvent, MessagePublishedData data, CancellationToken cancellationToken)
            {
              string eventType = data.Message.Attributes["eventType"];
              string secretId = data.Message.Attributes["secretId"];
              string secretMetadata = data.Message.TextData;
              Console.WriteLine($"Received {eventType} for {secretId}. New metadata: {secretMetadata}.");
              return Task.CompletedTask;
            }
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Secret Manager Go SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    type PubSubMessage struct {
    	Attributes PubSubAttributes `json:"attributes"`
    	Data       []byte           `json:"data"`
    }
    
    // PubSubAttributes are attributes from the Pub/Sub event.
    type PubSubAttributes struct {
    	SecretId  string `json:"secretId"`
    	EventType string `json:"eventType"`
    }
    
    // ConsumeEventNotification demonstrates how to consume and process the Pub/Sub
    // notification from Secret Manager.
    func ConsumeEventNotification(ctx context.Context, m PubSubMessage) (string, error) {
    	// The printed value will be visible in Cloud Logging:
    	//
    	//     https://cloud.google.com/functions/docs/monitoring/logging
    	//
    	eventType := m.Attributes.EventType
    	secretID := m.Attributes.SecretId
    	data := m.Data
    
    	return fmt.Sprintf("Received %s for %s. New metadata: %q.",
    		eventType, secretID, data), nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.Base64;
    import java.util.Map;
    import java.util.logging.Logger;
    import lombok.Data;
    
    // Demonstrates how to consume and process a Pub/Sub notification from Secret Manager. Triggered
    // by a message on a Cloud Pub/Sub topic.
    // Ideally the class should implement a background function that accepts a Pub/Sub message.
    // public class ConsumeEventNotification implements BackgroundFunction<PubSubMessage> { }
    public class ConsumeEventNotification {
    
      // You can configure the logs to print the message in Cloud Logging.
      private static final Logger logger = Logger.getLogger(ConsumeEventNotification.class.getName());
    
      // Accepts a message from a Pub/Sub topic and writes it to logger.
      public static String accept(PubSubMessage message) {
        String eventType = message.attributes.get("eventType");
        String secretId = message.attributes.get("secretId");
        String data = new String(Base64.getDecoder().decode(message.data));
        String log = String.format("Received %s for %s. New metadata: %s", eventType, secretId, data);
        logger.info(log);
        return log;
      }
    
      // Event payload. Mock of the actual Pub/Sub message.
      @Data
      public static class PubSubMessage {
    
        byte[] data;
        Map<String, String> attributes;
        String messageId;
        String publishTime;
        String orderingKey;
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
    * Triggered from a message on a Cloud Pub/Sub topic.
    * The printed value will be visible in Cloud Logging
    * (https://cloud.google.com/functions/docs/monitoring/logging).
    *
    * @param {!Object} event Event payload.
    * @param {!Object} context Metadata for the event.
    */
    exports.smEventsFunction = (event, context) => {
      const eventType = event.attributes.eventType;
      const secretID = event.attributes.secretId;
      const secretMetadata = Buffer.from(event.data, 'base64').toString();
      console.log(`Received ${eventType} for ${secretID}. New metadata: ${secretMetadata}.`);
    };

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import base64
    
    
    def consume_event_notification(event: dict, unused_context: None) -> str:
        """
        consume_event_notification demonstrates how to consume and process a
        Pub/Sub notification from Secret Manager.
        Args:
              event (dict): Event payload.
              unused_context (google.cloud.functions.Context): Metadata for the event.
        """
        event_type = event["attributes"]["eventType"]
        secret_id = event["attributes"]["secretId"]
        secret_metadata = base64.b64decode(event["data"]).decode("utf-8")
        event_notification = (
            f"Received {event_type} for {secret_id}. New metadata: {secret_metadata}"
        )
        print(event_notification)
        return event_notification
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Secret Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "functions_framework"
    require "base64"
    
    # Triggered from a message on a Cloud Pub/Sub topic.
    # The printed value will be visible in Cloud Logging
    # (https://cloud.google.com/functions/docs/monitoring/logging).
    FunctionsFramework.cloud_event "sm_events_function" do |event|
      message = event.data["message"]
      event_type = message["attributes"]["eventType"]
      secret_id = message["attributes"]["secretId"]
      message_data = Base64.decode64 message["data"]
      FunctionsFramework.logger.info "Received %s for %s. New metadata: %s." % [event_type, secret_id, message_data]
    end

For a list of all event types, see [Event Types](https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets#events).

## Misconfigured topics

If Pub/Sub topics are added to a secret in a Create or Update operation but Secret Manager cannot publish messages to the topic due to a misconfiguration, the operation fails with an error message indicating why the publish failed. This could happen, for example, if the topic does not exist, or if the Secret Manager service account does not have permission to publish.

If Pub/Sub topics are added to a secret and then afterwards the topic is changed so that Secret Manager can no longer publish messages (for instance, the topic is deleted, or the Secret Manager service account permissions are removed), Secret Manager writes logs to the Secret Manager [`Secret`](https://docs.cloud.google.com/monitoring/api/resources#tag_secretmanager.googleapis.com/Secret) with a message indicating why the publish failed.

## What's next

  * Learn how to [analyze secrets with Cloud Asset Inventory](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
