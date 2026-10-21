---
url: https://docs.cloud.google.com/secret-manager/docs/secret-rotation/
title: Create rotation schedules in Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:32.443823+00:00
---

# Create rotation schedules in Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/secret-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Create rotation schedules in Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager lets you schedule periodic rotations of your secrets. Secret Manager does this by sending notifications to Pub/Sub topics associated with your secrets, based on the rotation frequency and time that you specify. This page describes how to set up these rotation schedules.

## How secret rotation notifications work

Secret Manager triggers a `SECRET_ROTATE` message to the designated Pub/Sub topics at the secret's `next_rotation_time`. There are two ways to determine this timestamp:

  1. User-defined: You can specify the `next_rotation_time` when you create or update the secret.

  2. Rotation period: If you define a `rotation_period`, Secret Manager automatically calculates the `next_rotation_time`. Secret Manager sends the `SECRET_ROTATE` message after the specified `rotation_period` has elapsed, and then updates the `next_rotation_time` to schedule the next rotation.




You must configure a Pub/Sub subscriber to receive and act on the `SECRET_ROTATE` messages. You might also need to set up additional workflows in response to these notifications, such as creating a new version of the secret and deploying the changes to your applications.

## Requirements and considerations for secret rotation schedules

  * Pub/Sub topics must be configured on the secret. To learn how to create a Pub/Sub topic and subscription, see the [Pub/Sub quickstart](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud). To learn how to configure topics on a secret, see [Event Notifications for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/event-notifications).

  * `next_rotation_time` must be set if `rotation_period` is specified.

  * `next_rotation_time` can't be set to less than five minutes in the future.

  * The `rotation_period` can't be less than one hour long. For timestamp formatting guidance, see the [Google Cloud datetime reference](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)

  * While Secret Manager automatically retries failed message delivery attempts, we can't guarantee successful delivery if there are misconfigurations related to the secret, topic configuration, permissions, or quotas.

  * In-flight rotations must complete before another rotation can be started in order to prevent concurrent rotations from yielding unexpected behavior. Notifications are considered in-flight while Secret Manager is attempting to send the message to Pub/Sub. Scheduled rotations are skipped if there is an in-flight rotation. Secret Manager automatically retries failed attempts to send a message for up to seven days, after which the rotation is canceled.




## Configure rotation on a secret

You can configure a rotation schedule using the Google Cloud console, the Google Cloud CLI, or the Secret Manager API.

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create secret**.

  3. On the **Create secret** page, enter a name for the secret in the **Name** field.

  4. Enter a value for the secret (for example, `abcd1234`). You can also upload a text file containing the secret value using the **Upload file** option. This action automatically creates the secret version.

  5. Go to the **Rotation** section, and then select the **Set rotation period** checkbox.

  6. In the **Rotation period** list, select from the default options or select **Custom** to configure your own rotation schedule.

  7. In the **Starting on** field, enter the rotation period start date and time.

  8. Click **Create secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret.
  * NEXT_ROTATION_TIME: the timestamp at which to complete the first rotation in ISO 8601 format, for example `2021-06-01T09:00:00Z`.
  * ROTATION_PERIOD: the interval, in seconds, to rotate the key. For example to rotate the key every 2592000s, you'll set a value of `2592000s`.
  * FULL_TOPIC_NAME: the full name of your Pub/Sub topic in the format `projects/your-project-id/topics/your-topic-name`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID \
      --replication-policy "automatic" \
      --next-rotation-time="NEXT_ROTATION_TIME" \
      --rotation-period="ROTATION_PERIOD" \
      --topics="FULL_TOPIC_NAME"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID `
      --replication-policy "automatic" `
      --next-rotation-time="NEXT_ROTATION_TIME" `
      --rotation-period="ROTATION_PERIOD" `
      --topics="FULL_TOPIC_NAME"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID ^
      --replication-policy "automatic" ^
      --next-rotation-time="NEXT_ROTATION_TIME" ^
      --rotation-period="ROTATION_PERIOD" ^
      --topics="FULL_TOPIC_NAME"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TOPIC_NAME: the topic name



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {
      "replication":{
        "automatic":{}
      },
      "topics": {"name" : "projects/$PROJECT_ID/topics/$TOPIC_NAME"},
      "rotation":
        {
          "next_rotation_time": "2021-06-01T09:00:00Z",
          "rotation_period" : '2592000s'
        },
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID"

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
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T04:06:00.660420Z",
      "topics": [
        {
          "name": "projects/PROJECT_ID/topics/TOPIC_NAME"
        }
      ],
      "etag": "\"1621434abc8dc4\"",
      "rotation": {
        "nextRotationTime": "2024-09-10T09:00:00Z",
        "rotationPeriod": "2592000s"
      }
    }
    

## Update a secret's rotation settings

You can update the following rotation settings when making an update request:

  * `rotation`: This refers to the entire rotation configuration of the secret.

  * `rotation.next_rotation_time`: This specifically targets the timestamp indicating when the next rotation might occur.

  * `rotation.rotation_period`: This specifies the duration between each rotation. 



To update the secret's rotation settings, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Locate the secret that you want to edit and click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

  3. Go to the **Rotation** section. Update the rotation period as required, and click **Update secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret.
  * NEXT_ROTATION_TIME: the timestamp at which to complete the first rotation in ISO 8601 format, for example `2021-06-01T09:00:00Z`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID \
      --next-rotation-time="NEXT_ROTATION_TIME"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID `
      --next-rotation-time="NEXT_ROTATION_TIME"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID ^
      --next-rotation-time="NEXT_ROTATION_TIME"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * NEXT_ROTATION_TIME: the timestamp at which to complete the first rotation in ISO 8601 format, for example `2021-06-01T09:00:00Z`.



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time

Request JSON body: 
    
    
    {
      "rotation": {"next_rotation_time": "NEXT_ROTATION_TIME"}
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T04:06:00.660420Z",
      "topics": [
        {
          "name": "projects/PROJECT_ID/topics/TOPIC_NAME"
        }
      ],
      "etag": "\"1621434abc8dc4\"",
      "rotation": {
        "nextRotationTime": "2024-09-10T09:00:00Z",
        "rotationPeriod": "2592000s"
      }
    }
    
    

## Disable rotation on a secret

To disable the secret rotation, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Locate the secret that you want to edit and click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

  3. Go to the **Rotation** section. Clear the **Set rotation period** checkbox, and then click **Update secret**.




### gcloud

#### Remove a secret's `next_rotation_time`

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID \
        --remove-next-rotation-time

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID `
        --remove-next-rotation-time

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID ^
        --remove-next-rotation-time

#### Remove a secret's rotation schedule. This removes both the `next_rotation_time` and `rotation_period`.

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID \
        --remove-rotation-schedule

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID `
        --remove-rotation-schedule

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID ^
        --remove-rotation-schedule

### REST

#### Remove a secret's next rotation time

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation.next_rotation_time" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T04:06:00.660420Z",
      "topics": [
        {
          "name": "projects/PROJECT_ID/topics/TOPIC_NAME"
        }
      ],
      "etag": "\"16214530fa18d3\""
    }
    
    

#### Remove a secret's rotation schedule. This removes both the next rotation time and rotation period.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/$PROJECT_ID/secrets/$SECRET_ID?updateMask=rotation" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T04:06:00.660420Z",
      "topics": [
        {
          "name": "projects/PROJECT_ID/topics/TOPIC_NAME"
        }
      ],
      "etag": "\"16214530fa18d3\""
    }
    
    

## What's next

  * Learn how to [enable Customer-Managed Encryption Keys (CMEK) for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).
  * Learn how to [use ETags for optimistic concurrency control](https://docs.cloud.google.com/secret-manager/docs/etags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
