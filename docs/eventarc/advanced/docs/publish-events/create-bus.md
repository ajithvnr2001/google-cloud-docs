---
url: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus/
title: Create a bus to route messages \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:14.242461+00:00
---

# Create a bus to route messages  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Create a bus to route messages Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

An Eventarc Advanced bus lets you centralize, monitor, and trace the flow of messages through your system, and acts as a router. It receives events from a message source or published by a provider, and evaluates them according to an _enrollment_. An enrollment identifies a subscription to a particular bus, and defines the matching criteria for messages, causing them to be routed accordingly. For more information, see [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment).

A bus can be used by event providers and destinations in your project or in other projects. For more information, see [Project layouts](https://docs.cloud.google.com/eventarc/advanced/docs/overview#layouts).

## Required roles

An Identity and Access Management (IAM) role contains a set of permissions that lets you perform specific actions on Google Cloud resources. The following roles and permissions are required when creating a bus to route messages:

  * To get the permission that you need to **create a bus** , ask your administrator to grant you either the [Eventarc Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`) or the [Eventarc Message Bus Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusAdmin) (`roles/eventarc.messageBusAdmin`) IAM role on your bus project. These predefined roles contain the `eventarc.messageBuses.create` permission, which is required to create a bus.
  * To get the permission that you need to **use a bus** , ask your administrator to grant you the [Eventarc Message Bus User](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusUser) (`roles/eventarc.messageBusUser`) IAM role on your bus project. This predefined role contains the `eventarc.buses.use` permission, which is required to use a bus.
  * To create a pipeline and an enrollment, additional permissions are required. For more information, see the [required roles when creating an enrollment](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#required-roles).



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Create a bus

You can create a bus in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API

**Note:** You can create one bus per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. Click add_box **Create bus**.

  3. On the **Create a bus** page, do the following:

     1. Enter a **Bus name**. This is the ID for your bus.
     2. Optional: Enter a **Bus display name** which is displayed on the **Bus details** page.
     3. In the **Region** list, select a [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) to deploy your bus in.
     4. In the **Log severity** list, select the minimum severity for events described in log entries. The default is **None**. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).
     5. For **Encryption** , accept the default **Google-managed encryption key** or select **Cloud KMS key**. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek).
     6. If you select **Cloud KMS key** , do the following:

        1. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the **Cloud KMS with Autokey** option is disabled, it isn't yet integrated with the current resource type.

        2. In the **Select a Cloud KMS key** , select a key.

Note that you must select a region before you can view your customer-managed keys.

        3. Optional: To manually enter the resource name of the key, in the **Select a customer-managed key** list, click **Enter key manually** , and enter the key name in the specified format.

        4. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

     7. Optional: To add a message source, click add **Add source**.

        1. In the **Add message source** pane, for the Google API message provider, accept the default of `google-api-source` or enter a different source name.
        2. Click **Create**.

This enables the automatic collection of events coming directly from Google sources.

Note that only events from resources in the same Google Cloud project as the bus are published. For more information, see [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).

     8. Optional: To add labels, click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)

  4. Click **Create**.




###  gcloud 

  1. Open a terminal.

  2. Create a bus by using the [`gcloud eventarc message-buses create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/create) command.
         
         gcloud eventarc message-buses create BUS_NAME \
             --location=REGION
         

Replace the following:

     * `BUS_NAME`: the ID or fully qualified identifier of the bus
     * `REGION`: a [supported location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) for the bus

Alternatively, you can set the Google Cloud CLI location property:
           
           gcloud config set eventarc/location REGION
           

Optional: You can also use the following flags:

     * `--async` to return from the command immediately, without waiting for the operation in progress to complete.
     * `--crypto-key` to specify the fully qualified name of a [customer-managed encryption key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek); if unspecified, Google-owned and managed keys are used.
     * `--logging-config` to configure the minimum severity for events described in log entries. Must be one of the following: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. The default is `NONE`. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).



### REST API

To create a bus, use the [`projects.locations.messageBuses.create`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses/create) method.

Before using any of the request data, make the following replacements: 

  * `BUS_NAME`: the display name of your bus—for example, `my_bus`.
  * `LABEL_KEY` and `LABEL_VALUE`: optional. A map of label key and value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  * `ANNOTATION_KEY` and `ANNOTATION_VALUE`: optional. A map of annotation key and value pairs of free-form text. You can use them to attach arbitrary information associated with the resource. For more information, see [Annotations](https://google.aip.dev/148#annotations). 
  * `ENCRYPT_KEY`: optional. A Cloud KMS key that the bus should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which to create the bus—for example, `us-central1`.
  * `LOG_SEVERITY`: optional. The minimum severity of the event described in a log entry. One of: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. The default is `NONE`. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). 



Request JSON body: 
    
    
    {
      "display_name": "BUS_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "cryptoKeyName": "ENCRYPT_KEY",
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "display_name": "BUS_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "cryptoKeyName": "ENCRYPT_KEY",
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"}
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses?messageBusId=BUS_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "display_name": "BUS_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "cryptoKeyName": "ENCRYPT_KEY",
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"}
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
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses?messageBusId=BUS_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Delete a bus

You can delete a bus in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API

**Note:** Prior to deleting a bus, you must [delete any associated enrollents](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#delete-enrollment). If you delete a bus, any message sources configured to use it will no longer be able to.

### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

The **Bus details** page opens.

  2. Click delete **Delete**.

  3. When prompted to delete the bus, to acknowledge that any message sources configured to use the bus will no longer be able to, select the **Do you want to proceed?** checkbox.

  4. To confirm the deletion, enter `Delete`.

  5. Click **Delete**.




###  gcloud 

  1. Open a terminal.

  2. Delete a bus by using the [`gcloud eventarc message-buses delete`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/delete) command.
         
         gcloud eventarc message-buses delete BUS_NAME \
             --location=REGION
         

Replace the following:

     * `BUS_NAME`: the ID or fully qualified identifier of the bus
     * `REGION`: the [supported location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) for the bus



### REST API

To delete a bus, use the [`projects.locations.messageBuses.delete`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses/delete) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the bus is created—for example, `us-central1`.
  * `BUS_NAME`: the name of the bus you want to delete.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## What's next

  * [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources)
  * [Publish events directly in a supported format](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
