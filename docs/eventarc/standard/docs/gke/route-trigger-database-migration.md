---
url: https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-database-migration/
title: Route Database Migration events to GKE \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:00.831557+00:00
---

# Route Database Migration events to GKE  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-database-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Route Database Migration events to GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Eventarc for GKE destinations**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

An Eventarc trigger declares your interest in a certain event or set of events. You can configure event routing by specifying filters for the trigger, including the event source, and the target Google Kubernetes Engine (GKE) service running in a GKE cluster. Note that targets can only include services running in (public or private) GKE clusters with public endpoints. To target services in GKE clusters with private endpoints, route events to [internal HTTP endpoints](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events).

Eventarc delivers events to the event receiver in a [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) through an HTTP request.

These instructions show you how to configure event routing to your GKE service that is triggered by a direct Database Migration event. For more details, see the list of [supported direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source).

**Note:** If both direct and audit log events are supported for a Google provider, we recommend that you create a trigger that filters for the direct event. Direct events offer a number of advantages over audit log events. For more information, see [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options).

## Before you begin

You must enable _Workload Identity Federation for GKE_ on the GKE cluster **and** node pool that the destination service is running on. Workload Identity Federation for GKE is required to properly set up the _event forwarder_ and is the recommended way to access Google Cloud services from applications running within GKE due to its improved security properties and manageability.

![Eventarc events to GKE targets architecture](https://docs.cloud.google.com/static/eventarc/images/eventarc-gke-arch.svg)

### Workload Identity Federation for GKE

Applications running on GKE might need access to Google Cloud APIs. Workload Identity Federation for GKE allows a Kubernetes service account in your GKE cluster to act as an [IAM service account](https://docs.cloud.google.com/iam/docs/service-accounts). Pods that use the configured Kubernetes service account automatically authenticate as the IAM service account when accessing Google Cloud APIs. Using Workload Identity Federation for GKE lets you assign distinct, fine-grained identities and authorization for each application in your cluster. Note that specific permissions must be granted to the Eventarc trigger's service account. In this document, see the steps to create a service account.

For more information on enabling and configuring Workload Identity Federation for GKE on your GKE clusters, refer to [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

### Event forwarder

Eventarc's event forwarder pulls new events from Eventarc and forwards them to the GKE destination. This component acts as a mediator between the Pub/Sub transport layer and the GKE service. It works on existing services and also supports signaling services (including those not exposed outside of the fully-managed cluster) while simplifying setup and maintenance. At a networking level, to receive events in a GKE service, you don't need to open the service to external traffic as all events are delivered from an origin that resides within the same GKE cluster.

Note that the event forwarder's lifecycle is managed by Eventarc, and if you accidentally delete the event forwarder, Eventarc will restore this component.

For each trigger pointing to a GKE destination, the event forwarder (a specifically configured `gke-forwarder` pod) does the following:

  1. It uses the Pub/Sub API to open a [`StreamingPull` connection](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#streamingpullrequest) to the trigger transporter (a Pub/Sub topic and subscription) and receives events as they become available.

  2. It transforms events to the correct [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) and encodes and delivers them as an `HTTP POST` request to the target GKE service.




The Eventarc service agent needs the permission to run and regularly update the `gke-forwarder` instance. This permission must be granted once per project. For details, in this document, see Enable GKE destinations.

### Troubleshooting

To resolve issues that you might encounter when using Eventarc for GKE, see [Troubleshoot Eventarc for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting).

## Prepare to create a trigger

For each trigger that targets a GKE service, Eventarc creates an event forwarder component. Eventarc requires permissions to install the component and manage resources in the GKE cluster. Before creating an Eventarc trigger for GKE destinations, ensure that you complete the following tasks.

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Eventarc, Eventarc Publishing, Google Kubernetes Engine, and Resource Manager APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com,cloudresourcemanager.googleapis.com,container.googleapis.com)

  3. If applicable, enable the API related to the direct events. For example, for Database Migration events, enable the Database Migration API. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for your target service.

     1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for event trigger`.

     4. Click **Create and continue**.

     5. To provide appropriate access, in the **Select a role** list, select the required Identity and Access Management (IAM) roles to grant to your service account. For more information, see [Roles and permissions for GKE targets](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions).

For additional roles, click add **Add another role** and add each additional role.

     6. Click **Continue**.

     7. To finish creating the account, click **Done**. 




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Eventarc, Eventarc Publishing, Google Kubernetes Engine, and Resource Manager APIs.
         
         gcloud services enable eventarc.googleapis.com \
             eventarcpublishing.googleapis.com \
             container.googleapis.com \
             cloudresourcemanager.googleapis.com

  3. If applicable, enable the API related to the direct events. For example, for Database Migration events, enable `datamigration.googleapis.com`. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for your target GKE destination.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     2. Grant the required Identity and Access Management (IAM) roles or permissions. For more information, see [Roles and permissions for GKE targets](https://docs.cloud.google.com/eventarc/standard/docs/gke/roles-permissions). 




## Enable GKE destinations

To allow Eventarc to manage resources in the GKE cluster, enable GKE destinations, and bind the Eventarc service agent with the required roles.

  1. Enable GKE destinations for Eventarc:
         
         gcloud eventarc gke-destinations init

  2. At the prompt to bind the required roles, enter `y`.

The following roles are bound:

     * `roles/compute.viewer`
     * `roles/container.developer`
     * `roles/iam.serviceAccountAdmin`



## Create a trigger

You can create an Eventarc trigger using the Google Cloud CLI or through the Google Cloud console.

**Note:** Filtering is done through an exact match and does not support wildcards or regular expressions. However, you can use the `--event-filters-path-pattern` flag in the following gcloud CLI command, or define a path pattern through the console. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns). 

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page. 

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click add_box **Create trigger**. 
  3. Type a **Trigger name**. 

This is the ID of the trigger and it must start with a letter. It can contain up to 63 lowercase letters, numbers, or hyphens.

  4. For the **Trigger type** , select **Google sources**. 
  5. In the **Event provider** list, select **Database Migration**. 

Note that the event provider name used in the associated [Google Cloud documentation](https://docs.cloud.google.com/docs) might not have a prefix of _Cloud_ or _Google Cloud_. For example, on the console, _Memorystore for Redis_ is referred to as **Google Cloud Memorystore for Redis**.

  6. In the **Event type** list, from the _Direct_ events, select an event type. 
  7. To specify the encoding of the event payload, in the **Event data content type** list, select **application/json** or **application/protobuf**. 

Note that an event payload formatted in JSON is larger than one formatted in Protobuf. This might impact reliability depending on your event destination and its limits on event size. For more information, see [Known issues](https://docs.cloud.google.com/eventarc/docs/issues).

  8. In the **Region** list, select the same region as the Google Cloud service that is generating events. 

For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  9. If applicable to the event provider, click **Add filter** and specify the following: 
     1. In the **Attribute 1** field, depending on the direct event you chose, select a [resource ID](https://docs.cloud.google.com/apis/design/resource_names) that can act as an event filter.
     2. Select an operator: 
        * **Equal**
        * **Path pattern**

For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).

     3. In the **Attribute value 1** field, depending on the operator that you chose, type the exact value or apply a path pattern.
     4. If more attribute filters are applicable, click **Add filter** and specify the appropriate values.
  10. Select the **Service account** that will invoke your service or workflow. 

Or, you can create a new service account.

This specifies the Identity and Access Management (IAM) service account email associated with the trigger and to which you previously granted [specific roles](https://docs.cloud.google.com/eventarc/standard/docs/access-control) required by Eventarc. 

  11. In the **Event destination** list, select **Kubernetes Engine**. 
  12. Select a service.  


This is the name of the service that receives the events for the trigger. The service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated.

  13. Optionally, you can specify the **Service URL path** to send the incoming request to. 

This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, `route/subroute`.

  14. Optionally, to add a label, you can click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  15. Click **Create**. 

After a trigger is created, the event source filters can't be modified. Instead, create a new trigger and delete the old one. For more information, see [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers). 




###  gcloud 

You can create a trigger by running a `gcloud eventarc triggers create` command along with required and optional flags.
    
    
      gcloud eventarc triggers create TRIGGER \
          --location=LOCATION \
          --destination-gke-cluster=DESTINATION_GKE_CLUSTER \
          --destination-gke-location=DESTINATION_GKE_LOCATION \
          --destination-gke-namespace=DESTINATION_GKE_NAMESPACE \
          --destination-gke-service=DESTINATION_GKE_SERVICE \
          --destination-gke-path=DESTINATION_GKE_PATH \
          --event-filters="type=EVENT_FILTER_TYPE" \
          --event-filters="COLLECTION_ID=RESOURCE_ID" \
          --event-filters-path-pattern="COLLECTION_ID=PATH_PATTERN" \
          --event-data-content-type="EVENT_DATA_CONTENT_TYPE" \
          --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier 
  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

  * `DESTINATION_GKE_CLUSTER`: the name of the GKE cluster in which the target GKE service that receives events is running. 
  * `DESTINATION_GKE_LOCATION`: (optional) the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the GKE cluster in which the destination GKE service is running. If not specified, it is assumed that the cluster is a regional cluster and is in the same region as the trigger. 
  * `DESTINATION_GKE_NAMESPACE`: (optional) the namespace in which the destination GKE service is running. If not specified, the `default` namespace is used. 
  * `DESTINATION_GKE_SERVICE`: the name of the GKE service that receives the events for the trigger. The service can be in any of the GKE-supported locations and does not need to be in the same location as the trigger. However, the service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated. 
  * `DESTINATION_GKE_PATH`: (optional) the relative path you specify on the destination GKE service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, `route/subroute`. 
  * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 


  * `COLLECTION_ID` (optional): the [resource](https://docs.cloud.google.com/apis/design/resource_names) component that can act as an event filter, and is one of the following: 
    * `connectionprofile`
    * `migrationjob`
  * `RESOURCE_ID`: the identifier of the resource used as the filtering value for the associated collection. For more information, see [Resource ID](https://docs.cloud.google.com/apis/design/resource_names#resource_id). 
  * `PATH_PATTERN`: the [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns) to apply when filtering for the resource. 
  * `EVENT_DATA_CONTENT_TYPE`: (optional) the [encoding of the event payload](https://docs.cloud.google.com/eventarc/standard/docs/overview#event-format). This can be `application/json` or `application/protobuf`. The default encoding is `application/json`. 

Note that an event payload formatted in JSON is larger than one formatted in Protobuf. This might impact reliability depending on your event destination and its limits on event size. For more information, see [Known issues](https://docs.cloud.google.com/eventarc/docs/issues).

  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
  * `PROJECT_ID`: your Google Cloud project ID. 



Notes:

  * The `--event-filters="type=EVENT_FILTER_TYPE"` flag is required. If no other event filter is set, events for all resources are matched. 
  * `EVENT_FILTER_TYPE` cannot be changed after creation. To change `EVENT_FILTER_TYPE`, create a new trigger and delete the old one. 
  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported; however, when using the `--event-filters-path-pattern` flag, you can define a resource [path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns). 
  * The `--service-account` flag is used to specify the Identity and Access Management (IAM) service account email associated with the trigger. 



Example:
    
    
      gcloud eventarc triggers create helloworld-trigger \
          --location=us-central1 \
          --destination-gke-cluster=gke-events-cluster \
          --destination-gke-location=us-central1-a \
          --destination-gke-namespace=default \
          --destination-gke-service=helloworld-events \
          --destination-gke-path=/ \
          --event-filters="type=google.cloud.clouddms.migrationJob.v1.updated" \
          --event-filters-path-pattern="migrationjob=my-migrationjob-*" \
          --service-account=${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com

This command creates a trigger called `helloworld-trigger` for the event identified as `google.cloud.clouddms.migrationJob.v1.updated` and matches events for `migrationjob` IDs starting with `my-migrationjob-`.

###  Terraform 

You can create a trigger for a GKE destination using Terraform. For details, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform). 

**Note:** Although your trigger is created immediately, it can take up to two minutes for a trigger to propagate and filter events.

## List a trigger

You can confirm the creation of a trigger by listing Eventarc triggers using the Google Cloud CLI or through the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the Eventarc **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

This page lists your triggers in all locations, and includes details such as names, regions, event providers, destinations, and more.

  2. To filter your triggers:

     1. Click filter_list **Filter** or the **Filter triggers** field.
  3. In the **Properties** list, select an option to filter the triggers by.



You can select a single property or use the logical operator `OR` to add more properties.

* To sort your triggers, beside any supported column heading, click arrow_upward **Sort**.

###  gcloud 

Run the following command to list your triggers:
    
    
    gcloud eventarc triggers list --location=-

This command lists your triggers in all locations, and includes details such as names, types, destinations, and statuses.

## What's next

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview).
  * [Learn how to manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
