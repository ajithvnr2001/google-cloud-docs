---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs/
title: Route audit log events to Cloud Run \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:53.841266+00:00
---

# Route audit log events to Cloud Run  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Route audit log events to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

An Eventarc trigger declares your interest in a certain event or set of events. You can configure event routing by specifying filters for the trigger, including the event source, and the target Cloud Run service.

Eventarc delivers events to the event receiver in a [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents) through an HTTP request.

These instructions show you how to configure routing to your Cloud Run service that is triggered when an audit log is created that matches the trigger's filter criteria. For a list of the audit log events supported by Eventarc, including `serviceName` and `methodName` values, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs).

For more information about capturing events that are triggered when an audit log is created that matches the trigger's filter criteria, see [Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal).

**Note:** If both direct and audit log events are supported for a Google provider, we recommend that you create a trigger that filters for the direct event. Direct events offer a number of advantages over audit log events. For more information, see [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options).

## Prepare to create a trigger

Before you create a trigger, complete these prerequisites:

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Cloud Logging, Eventarc, and Eventarc Publishing APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com,logging.googleapis.com)

  3. If applicable, enable the API related to the Cloud Audit Logs events. For example, for Cloud Run functions audit logs, enable the Cloud Functions API. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for your target service.

     1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for event trigger`.

     4. Click **Create and continue**.

     5. To provide appropriate access, in the **Select a role** list, select the required Identity and Access Management (IAM) roles to grant to your service account for authenticated or unauthenticated invocations. For more information, see [Roles and permissions for Cloud Run targets](https://docs.cloud.google.com/eventarc/docs/roles-permissions).

For additional roles, click add **Add another role** and add each additional role.

**Important:** To accept authenticated invocations to your Cloud Run service, you must associate your trigger with a service account that has the `roles/run.invoker` role. When creating or updating your trigger, select that service account.
     6. Click **Continue**.

     7. To finish creating the account, click **Done**. 




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Cloud Logging, Eventarc, and Eventarc Publishing APIs.
         
         gcloud services enable logging.googleapis.com \
           eventarc.googleapis.com \
           eventarcpublishing.googleapis.com

  3. If applicable, enable the API related to the Cloud Audit Logs events. For example, for Cloud Run functions audit logs, enable `cloudfunctions.googleapis.com`. 

  4. If you don't already have one, create a user-managed service account, then grant it the roles and permissions necessary so that Eventarc can manage events for your target service.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     2. Grant the required Identity and Access Management (IAM) roles or permissions for authenticated or unauthenticated invocations. For more information, see [Roles and permissions for Cloud Run targets](https://docs.cloud.google.com/eventarc/docs/roles-permissions).

**Important:** To accept authenticated invocations to your Cloud Run service, you must associate your trigger with a service account that has the `roles/run.invoker` role. When creating or editing your trigger, use the `--service-account` flag to associate that service account with the trigger. 



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
  5. Select an **Event provider**. 

This is the Google service that is the source of events through its audit logs. For example, select **BigQuery**. 

Note that the event provider name used in the associated [Google Cloud documentation](https://docs.cloud.google.com/docs) might not have a prefix of _Cloud_ or _Google Cloud_. For example, on the console, _Memorystore for Redis_ is referred to as **Google Cloud Memorystore for Redis**.

  6. In the **Event type** list, from the _via Cloud Audit Logs_ events, select an event type. 
  7. Select one of the following: 
     * **Any resource** —This is the default and includes dynamically created resources that have identifiers generated at creation time. 
     * **Specific resource** —You must provide the full resource name. 
     * **Path pattern** —You can [filter for resources using a path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns). For example, type `projects/_/buckets/eventarc-bucket/objects/random.txt` or type `projects/_/buckets/**/r*.txt`. 
  8. To specify the encoding of the event payload, in the **Event data content type** list, select **application/json** or **application/protobuf**. 

Note that an event payload formatted in JSON is larger than one formatted in Protobuf. This might impact reliability depending on your event destination and its limits on event size. For more information, see [Known issues](https://docs.cloud.google.com/eventarc/docs/issues).

  9. In the **Region** list, select a region. 

Cloud Audit Logs triggers for Eventarc are available in specific regions and in the global region, but are not available in dual-region and multi-region locations. To avoid any performance and data residency issues caused by a global trigger, Google recommends that the location match that of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

If you specify the global location, you will receive events from all locations yielding matches for the event filters. For example, by creating a global Eventarc trigger, you can receive events from resources in the EU and US multi-regions.

Note that there is a known issue with [Cloud Audit Logs triggers for Compute Engine](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#compute-engine) that results in events originating from a single region: `us-central1`. This is regardless of where the virtual machine instance is actually located. When creating your trigger, set the trigger location to either `us-central1` or `global`.

  10. Select the **Service account** that will invoke your service or workflow. 

Or, you can create a new service account.

This specifies the Identity and Access Management (IAM) service account email associated with the trigger and to which you previously granted [specific roles](https://docs.cloud.google.com/eventarc/standard/docs/access-control) required by Eventarc. 

  11. In the **Event destination** list, select **Cloud Run**. 
  12. Select a service.  


This is the name of the service that receives the events for the trigger. The service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated.

  13. Optionally, you can specify the **Service URL path** to send the incoming request to. 

This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, `route/subroute`.

  14. Optionally, to specify a single delivery attempt with no retries, clear the **Enable retry on failure** checkbox; otherwise, the default behavior is retries if the delivery attempt fails. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
  15. Optionally, to add a label, you can click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  16. Click **Create**. 

After a trigger is created, the event source filters can't be modified. Instead, create a new trigger and delete the old one. For more information, see [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers). 




###  gcloud 

You can create a trigger by running [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) along with required and optional flags.
    
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-run-service=DESTINATION_RUN_SERVICE \
        --destination-run-region=DESTINATION_RUN_REGION \
        --event-filters="type=google.cloud.audit.log.v1.written" \
        --event-filters="serviceName=SERVICE_NAME" \
        --event-filters="methodName=METHOD_NAME" \
        --event-data-content-type="EVENT_DATA_CONTENT_TYPE" \
        --max-retry-attempts=1 \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following:

  * `TRIGGER`: the ID of the trigger or a fully qualified identifier. 
  * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example `gcloud config set eventarc/location us-central1`. 

Cloud Audit Logs triggers for Eventarc are available in specific regions and in the global region, but are not available in dual-region and multi-region locations. To avoid any performance and data residency issues caused by a global trigger, Google recommends that the location match that of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

If you specify the global location, you will receive events from all locations yielding matches for the event filters. For example, by creating a global Eventarc trigger, you can receive events from resources in the EU and US multi-regions.

Note that there is a known issue with [Cloud Audit Logs triggers for Compute Engine](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#compute-engine) that results in events originating from a single region: `us-central1`. This is regardless of where the virtual machine instance is actually located. When creating your trigger, set the trigger location to either `us-central1` or `global`.

  * `DESTINATION_RUN_SERVICE`: the name of the Cloud Run service that receives the events for the trigger. The service can be in any of the Cloud Run supported locations and doesn't need to be in the same location as the trigger. However, the service must be in the same project as the trigger and will receive events as HTTP POST requests sent to its root URL path (`/`), whenever the event is generated. 
  * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run service can be found. If not specified, it is assumed that the service is in the same region as the trigger. 


  * `SERVICE_NAME`: the identifier of the Google Cloud service
  * `METHOD_NAME`: the identifier of the operation


  * `EVENT_DATA_CONTENT_TYPE`: (optional) the [encoding of the event payload](https://docs.cloud.google.com/eventarc/standard/docs/overview#event-format). This can be `application/json` or `application/protobuf`. The default encoding is `application/json`. 

Note that an event payload formatted in JSON is larger than one formatted in Protobuf. This might impact reliability depending on your event destination and its limits on event size. For more information, see [Known issues](https://docs.cloud.google.com/eventarc/docs/issues).

  * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
  * `PROJECT_ID`: your Google Cloud project ID. 



Notes:

  * These flags are required:

    * `--event-filters="type=google.cloud.audit.log.v1.written"`
    * `--event-filters="serviceName=VALUE"`
    * `--event-filters="methodName=VALUE"`
  * Optionally, filter events for a specific resource by using the `--event-filters="resourceName=VALUE"` flag and specifying the complete path to the resource. Omit the flag for dynamically created resources that have identifiers generated at creation time. Or, filter events for a set of resources by using the `--event-filters-path-pattern="resourceName=VALUE"` flag and specifying the [resource path pattern](https://docs.cloud.google.com/eventarc/docs/path-patterns).



  * Each trigger can have multiple event filters, comma delimited in one `--event-filters`=[`ATTRIBUTE`=`VALUE`,...] flag, or you can repeat the flag to add more filters. Only events that match all the filters are sent to the destination. Wildcards and regular expressions are not supported. 
  * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger. 
  * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
  * The `--service-account` flag is used to specify the Identity and Access Management (IAM) service account email associated with the trigger. 
  * Optionally, to specify a relative path on the destination Cloud Run service to which the events for the trigger should be sent, use the `--destination-run-path` flag. 



Example:
    
    
      gcloud eventarc triggers create helloworld-trigger \
          --location=us-central1 \
          --destination-run-service=helloworld-events \
          --destination-run-region=us-central1 \
          --event-filters="type=google.cloud.audit.log.v1.written" \
          --event-filters="serviceName=bigquery.googleapis.com" \
          --event-filters="methodName=google.cloud.bigquery.v2.JobService.InsertJob" \
          --service-account=${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
    

This creates a trigger called `helloworld-trigger` for audit logs that are written by `bigquery.googleapis.com` and for the operation identified as `google.cloud.bigquery.v2.JobService.InsertJob`.

###  Terraform 

You can create a trigger for a Cloud Run destination using Terraform. For details, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform). 

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
