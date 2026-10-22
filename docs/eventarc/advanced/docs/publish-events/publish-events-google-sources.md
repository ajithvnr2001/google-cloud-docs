---
url: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources/
title: Publish events from Google sources \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:21.752523+00:00
---

# Publish events from Google sources  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Publish events from Google sources Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

You can enable the collecting and publishing of events from Google sources for a specific Eventarc Advanced bus by creating a `GoogleApiSource` resource.

Events from Google sources are directly triggered by an unmediated event such as the creation of a Cloud Run function or a status change to a Dataflow job. For more information, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/advanced/docs/event-types).

**Important:** Events from Google sources don't include events that are triggered when a log is produced through Cloud Audit Logs.

Note the following:

  * By default, events are collected from the Google Cloud project where the `GoogleApiSource` resource exists. You can also use the gcloud CLI to collect events from multiple projects that are in the same organization as the `GoogleApiSource` resource. For more information, in this document, see Publish events from multiple projects.
  * You can publish events to a bus that is in a different Google Cloud project from the one in which the `GoogleApiSource` resource exists. You can configure this by using the gcloud CLI or by sending a request to the Eventarc API (but not through the Google Cloud console).
  * There is a [limit](https://docs.cloud.google.com/eventarc/docs/quotas#limits) of one `GoogleApiSource` resource per Google Cloud project per region.



## Before you begin

Before you start, make sure that you have completed the following steps:

### Console

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com)




###  gcloud 

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




## Enable events from Google sources

To publish events from Google sources, you must create a [`GoogleApiSource`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources#resource:-googleapisource) resource. This resource represents a subscription to Google API events in a specific Google Cloud project for a particular Eventarc Advanced bus.

You can enable the publishing of events from Google sources in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API




### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. You can [create a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus) or, if you are updating a bus, click edit **Edit**.

  3. On the **Edit bus** page, to add a message source, click add **Add source**.

     1. In the **Add message source** pane, for the Google API message provider, accept the default of `google-api-source` or enter a different message source name.
     2. Click **Create**.
  4. Click **Save**.




###  gcloud 

  1. Open a terminal.

  2. You can enable events from Google sources by using the [`gcloud eventarc google-api-sources create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/create) command:
         
         gcloud eventarc google-api-sources create GOOGLE_API_SOURCE_NAME \
             --destination-message-bus=BUS_NAME \
             --destination-message-bus-project=BUS_PROJECT_ID

Replace the following:

     * `GOOGLE_API_SOURCE_NAME`: the ID or fully qualified identifier of your `GoogleApiSource` resource which represents a subscription to Google API events for a particular bus
     * `BUS_NAME`: the ID or fully qualified identifier of the bus for which you want to subscribe to Google API events
     * `BUS_PROJECT_ID`: the Google Cloud project ID for the bus

Optional: You can also use the following flags:

     * `--async` to return from the command immediately, without waiting for the operation in progress to complete.
     * `--crypto-key` to specify the fully qualified name of a [customer-managed encryption key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek); if unspecified, Google-owned and managed keys are used.
     * `--logging-config` to configure the logging level which must be one of the following: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).



### REST API

To enable events from Google sources, use the [`projects.locations.googleApiSources.create`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources/create) method.

Before using any of the request data, make the following replacements: 

  * `GOOGLE_API_SOURCE_NAME`: the display name of the `GoogleApiSource` resource which represents a subscription to Google API events for a particular bus—for example, `my_google_source`.
  * `LABEL_KEY` and `LABEL_VALUE`: optional. A map of label key and value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  * `ANNOTATION_KEY` and `ANNOTATION_VALUE`: optional. A map of annotation key and value pairs of free-form text. You can use them to attach arbitrary information associated with the resource. For more information, see [Annotations](https://google.aip.dev/148#annotations). 
  * `DESTINATION`: the fully qualified identifier of the Eventarc Advanced bus to which Google source events should be published in the format `projects/PROJECT_NAME/locations/LOCATION/messageBuses/BUS_NAME`. For more information, see [Create a bus to route messages](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).
  * `ENCRYPT_KEY`: optional. A Cloud KMS key that the `GoogleApiSource` resource should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek).
  * `PROJECT_ID`: the Google Cloud project ID in which to create the `GoogleApiSource` resource.
  * `LOCATION`: the supported [region](https://docs.cloud.google.com/eventarc/docs/locations) in which to create the `GoogleApiSource` resource—for example, `us-central1`.
  * `LOG_SEVERITY`: optional. The minimum severity of the event described in a log entry. One of: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. The default is `NONE`. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). 



Request JSON body: 
    
    
    {
      "displayName": "GOOGLE_API_SOURCE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "destination": "DESTINATION",
      "cryptoKeyName": "ENCRYPT_KEY",
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "displayName": "GOOGLE_API_SOURCE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "destination": "DESTINATION",
      "cryptoKeyName": "ENCRYPT_KEY",
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"}
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleApiSources?googleApiSourceId=GOOGLE_API_SOURCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "displayName": "GOOGLE_API_SOURCE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "destination": "DESTINATION",
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
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleApiSources?googleApiSourceId=GOOGLE_API_SOURCE_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/googleApiSources/GOOGLE_API_SOURCE_NAME",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Events from Google sources in the same Google Cloud project as the `GoogleApiSource` resource are now collected and published to the bus.

## Disable events from Google sources

To disable the publishing of events from Google sources in a specific Google Cloud project to an Eventarc Advanced bus, you must delete the [`GoogleApiSource`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources#resource:-googleapisource) resource.

You can disable the publishing of events from Google sources in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API




### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Bus details** page.

[Go to Bus details](https://console.cloud.google.com/eventarc/buses)

  2. Click edit **Edit**.

  3. On the **Edit bus** page, to delete the Google API message provider, click delete **Delete resource** for the **google-api-source** message source (or the name you have given it).

  4. At the **Delete resource** prompt, click **Confirm**.

  5. Click **Save**.




###  gcloud 

  1. Open a terminal.

  2. You can disable events from Google sources by using the [`gcloud eventarc google-api-sources delete`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/delete) command:
         
         gcloud eventarc google-api-sources delete GOOGLE_API_SOURCE_NAME \
             --location=REGION

Replace the following:

     * `GOOGLE_API_SOURCE_NAME`: the ID or fully qualified identifier of the `GoogleApiSource` resource
     * `REGION`: the [location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the `GoogleApiSource` resource



### REST API

To disable events from Google sources, use the [`projects.locations.googleApiSources.delete`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources/delete) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the Google Cloud project ID in which the `GoogleApiSource` resource is created.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the `GoogleApiSource` resource is created—for example, `us-central1`.
  * `GOOGLE_API_SOURCE_NAME`: the name of the `GoogleApiSource` resource you want to delete.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleApiSources/GOOGLE_API_SOURCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleApiSources/GOOGLE_API_SOURCE_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/googleApiSources/GOOGLE_API_SOURCE_NAME",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Events from Google sources in the same Google Cloud project as the deleted `GoogleApiSource` resource are no longer collected and published.

## Publish events from multiple projects

**Preview — Publish events from multiple projects**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To collect and publish Google source events from multiple Google Cloud projects, you must create a [`GoogleApiSource`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources#resource:-googleapisource) resource, and the projects must be in the same organization as the `GoogleApiSource` resource. For more information about organizations, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

Note the following:

  * Event publishing from multiple projects must be configured using the gcloud CLI and is not displayed in the Google Cloud console.
  * If the project containing the `GoogleApiSource` resource is moved to a different organization, publishing events from multiple projects will no longer function as expected. You must update or re-create the `GoogleApiSource` resource.



### 1\. Grant the Eventarc service agent the appropriate IAM role

To collect events at the organization level, use the [`gcloud organizations add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/add-iam-policy-binding) command to grant the Eventarc service agent the appropriate Identity and Access Management (IAM) role:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="SERVICE_AGENT_EMAIL" \
        --role="roles/eventarc.multiProjectEventCollector"

Replace the following:

  * `ORGANIZATION_ID`: your [organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * `SERVICE_AGENT_EMAIL`: the email address for the Eventarc [primary service agent](https://docs.cloud.google.com/iam/docs/service-account-types#primary) in the project where you are creating the `GoogleApiSource` resource. The email address is in the following format:
        
        service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com
        

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
        
        gcloud projects describe PROJECT_ID --format='value(projectNumber)'
        




### 2\. Publish from all projects or a list of projects

To publish events from Google sources in multiple projects, use the [`gcloud eventarc google-api-sources create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/create) command in either of the following ways:

  * Publish from **all Google Cloud projects** in the same organization as the `GoogleApiSource` resource:
        
        gcloud eventarc google-api-sources create GOOGLE_API_SOURCE_NAME \
            --location=REGION \
            --destination-message-bus=BUS_NAME \
            --destination-message-bus-project=BUS_PROJECT_ID \
            --organization-subscription

  * Publish from **a list of Google Cloud projects** in the same organization as the `GoogleApiSource` resource:
        
        gcloud eventarc google-api-sources create GOOGLE_API_SOURCE_NAME \
            --location=REGION \
            --destination-message-bus=BUS_NAME \
            --destination-message-bus-project=BUS_PROJECT_ID \
            --project-subscriptions=LIST_OF_PROJECTS

Replace the following:

    * `GOOGLE_API_SOURCE_NAME`: the ID or fully qualified identifier of the `GoogleApiSource` resource
    * `REGION`: the [location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the `GoogleApiSource` resource
    * `BUS_NAME`: the ID or fully qualified identifier of the bus for which you want to subscribe to Google API events
    * `BUS_PROJECT_ID`: the Google Cloud project ID for the bus
    * `LIST_OF_PROJECTS`: a comma-delimited list of Google Cloud [project IDs or project numbers](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). You can combine IDs and numbers in the same list. To publish events from the Google Cloud project containing the `GoogleApiSource` resource, you **must** explicitly include the project ID or number in the list.



## What's next

  * [Quickstart: Publish events from a Google source](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source)
  * [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format)
  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)
  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
