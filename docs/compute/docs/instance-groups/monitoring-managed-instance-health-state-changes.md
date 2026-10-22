---
url: https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes/
title: Monitor VM health state changes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:51.390325+00:00
---

# Monitor VM health state changes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor VM health state changes Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view and read health state change log entries of a VM in a managed instance group (MIG), and provides specific use cases to help you monitor the VMs in the group.

If you have configured application-based [health checking](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#setting_up_an_autohealing_policy) for MIG, Compute Engine writes a log entry whenever a managed instance's health state changes—for example, when the instance goes from `HEALTHY` to `UNHEALTHY` state. These log entries help you to monitor and debug the health state of each managed instance as well as the overall health of the MIG.

## Before you begin

  * Review [Setting up health checking and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Pricing

Compute Engine uses [Cloud Logging](https://docs.cloud.google.com/logging) to generate log entries for managed instance health state changes. Cloud Logging provides you with a free allotment per month after which log entries are priced by data volume. For more information, see the [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).

To avoid the logging costs, you can [disable](https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs#disabling_health_state_change_logs) the health state change logs.

## Viewing health state change logs

Provided the health state change logs remain [enabled](https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs#enabling_health_state_change_logs), then Compute Engine writes a log entry to [platform logs](https://docs.cloud.google.com/logging/docs/overview#categories) whenever the health state of a managed instance changes. You can view these logs for a project, for a specific MIG, or for a specific managed instance.

### Viewing logs for a project or a MIG

To view log entries for a project or for a specific MIG, use the Google Cloud console, gcloud CLI, or REST.

###  Console 

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Set the following query parameters:

     * **Resource** \- GCE Instance Group Manager
     * **Log name** \- `instance_group_manager_events`
  3. Alternatively, you can copy the following query in the **Query** builder.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:*
         

You can narrow down your search to a specific managed instance group using the following query.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         resource.labels.instance_group_manager_name="MIG_NAME"
         

  4. Click **Run query**. The **Query results** will display the logs.




###  gcloud 

Use the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view and read the log entries.

To view all health state change logs in your project, use the following command:
    
    
    gcloud logging read 'resource.type="gce_instance_group_manager" AND
        logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
        jsonPayload.instanceHealthStateChange:*'\
        --limit 10
    

To view all health state change logs for a specific managed instance group, use the following command:
    
    
    gcloud logging read 'resource.type="gce_instance_group_manager" AND
        logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
        jsonPayload.instanceHealthStateChange:* AND
        resource.labels.instance_group_manager_name="MIG_NAME"' \
        --limit 10
    

Replace the following:

  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the MIG for which you want to view the health state change logs.



###  REST 

To view the health state change logs, make a `POST` request to the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list).

To view all the health state change logs in your project, use the following command:
    
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer OAUTH2_TOKEN" -X POST -d \
    '{"filter":
        "resource.type=gce_instance_group_manager AND
        logName=projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events AND
        jsonPayload.instanceHealthStateChange:*",
        "orderBy": "timestamp desc",
        "pageSize": 10,
        "resourceNames": ["projects/PROJECT_ID"]
    }' https://logging.googleapis.com/v2/entries:list?alt=json
    

To view the health state change logs for a specific managed instance group, use the following command:
    
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer OAUTH2_TOKEN" -X POST -d \
    '{"filter":
        "resource.type=gce_instance_group_manager AND
        logName=projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events AND
        jsonPayload.instanceHealthStateChange:* AND
        resource.labels.instance_group_manager_name=MIG_NAME",
        "orderBy": "timestamp desc",
        "pageSize": 10,
        "resourceNames": ["projects/PROJECT_ID"]
    }' https://logging.googleapis.com/v2/entries:list?alt=json
    

Replace the following:

  * `OAUTH2_TOKEN`: your application's access token. For local testing, you can use the `gcloud auth print-access-token` command to generate a token.
  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the MIG for which you want to view the health state change logs.



For more information about each log entry, see Format of log entries.

Depending on whether you want to archive the logs, use the logs for analysis, stream the logs to other applications, or [trigger](https://docs.cloud.google.com/functions/docs/calling) a Cloud Function, you can export the logs to destinations such as Cloud Storage, BigQuery, or Pub/Sub. For more information about exporting logs, see [Overview of logs exports](https://docs.cloud.google.com/logging/docs/export).

### Viewing health state change logs for a specific VM

To view log entries for a specific managed instance, use the Google Cloud console, gcloud CLI, or REST.

###  Console 

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy the following query in the **Query** builder.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         labels."compute.googleapis.com/instance_name"="INSTANCE_NAME"
         

  3. Click **Run query**.




###  gcloud 

Use the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view and read the log entries.

To view the health state change logs of a managed instance, use the following command:
    
    
    gcloud logging read 'resource.type="gce_instance_group_manager" AND
        logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
        jsonPayload.instanceHealthStateChange:* AND
        labels."compute.googleapis.com/instance_name"="INSTANCE_NAME"' \
        --limit 10
    

Replace the following:

  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `INSTANCE_NAME`: the managed instance for which you want to view the health state change logs.



###  REST 

To view the health state change logs of a managed instance, make a `POST` request to the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list).
    
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer OAUTH2_TOKEN" -X POST -d \
    '{"filter":
        "resource.type=gce_instance_group_manager AND
            logName=projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events AND
            jsonPayload.instanceHealthStateChange:* AND
            labels.\"compute.googleapis.com/instance_name\"=\"INSTANCE_NAME\"",
        "orderBy": "timestamp desc",
        "pageSize": 10,
        "resourceNames": ["projects/PROJECT_ID"]
    }' https://logging.googleapis.com/v2/entries:list?alt=json
    

Replace the following:

  * `OAUTH2_TOKEN`: your application's access token. For local testing, you can use the `gcloud auth print-access-token` command to generate a token.
  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `INSTANCE_NAME`: the managed instance for which you want to view the health state change logs.



### Format of log entries

Instance health state change log entries contain information useful for monitoring and debugging the state of your managed instances.

The logs are written to [platform logs](https://docs.cloud.google.com/logging/docs/overview#categories) with the log name `instance_group_manager_events`. The platform logs help you to debug and troubleshoot issues.
    
    
    logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events"
    

Health state change log entries contain the following types of information:

  * General information shown in most logs, such as severity, project ID, MIG name and ID, project number, timestamp, and so on.
  * Fields specific to the instance's health state.



Within each health state change log entry, the `jsonPayload.instanceHealthStateChange` field contains the following information:

**Field** | **Description**  
---|---  
`instance` | URL for the instance, based on string project ID and instance name.  
`instanceWithId` | URL for the instance, based on its numeric project ID and instance ID.  
`ipAddress` | IP address of the instance, as probed by the health check.  
`network` | URL of the network resource for this instance, based on string project ID and network name.  
`networkWithId` | URL of the network resource for this instance, based on its numeric project ID and network ID.  
`healthCheck` | URL for the health check that's configured for the managed instance group.  
`previousDetailedHealthState` | Previous health state of the instance. For the list of possible states, see [ health states](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#health_states).  
`detailedHealthState` | Current health state of the instance. For the list of possible states, see [ health states](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#health_states).  
`notificationTime` | Timestamp of when the health state change occurred.  
  
Log fields of type boolean typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.

#### Log entry example

The following example shows a VM instance's health state change from `HEALTHY` to `UNHEALTHY`:
    
    
      {
        "logName": "projects/my-project/logs/compute.googleapis.com%2Finstance_group_manager_events",
        "resource": {
          "type": "gce_instance_group_manager",
          "labels": {
            "instance_group_manager_id": "3138236342290985981",
            "instance_group_manager_name": "my-mig",
            "project_id": "my-project",
            "location": "europe-west3"
          }
        },
        "labels": {
          "compute.googleapis.com/instance_id": "6498902454451155884",
          "compute.googleapis.com/instance_location": "europe-west3-a",
          "compute.googleapis.com/instance_name": "my-mig-a"
        },
        "timestamp": "2019-11-19T15:47:57.127Z",
        "severity": "INFO",
        "jsonPayload": {
          "@type": "type.googleapis.com/compute.InstanceGroupManagerEvent",
          "instanceHealthStateChange": {
            "instance": "projects/my-project/zones/europe-west3-a/instances/my-mig-a",
            "instanceWithId": "projects/123456/zones/europe-west3-a/instances/6498902454451155884",
            "ipAddress": "10.0.0.4",
            "network": "projects/my-project/global/networks/net-1",
            "networkWithId": "projects/123456/global/networks/456",
            "healthCheck": "projects/my-project/global/healthChecks/my-mig-health-check",
            "previousDetailedHealthState": "HEALTHY",
            "detailedHealthState": "UNHEALTHY",
            "notificationTime": "2019-11-19T15:47:56.444Z"
          }
        },
        "receiveTimestamp": "2019-11-19T15:47:57.296439184Z"
      }
      

## Use cases

You can use the health state change logs in the following monitoring or debugging scenarios:

  * Find out how often a particular VM instance changed health states over time.
  * Assess how often a MIG experienced health state changes of its instances.
  * Identify problematic VM instances that frequently go `UNHEALTHY`.
  * Find out what caused an autohealing attempt.
  * Find out whether an autohealing attempt succeeded for a specific VM instance.
  * Fine-tune health check configuration for an application by determining an appropriate initial delay for autohealing.



### Monitoring health state changes of a VM

You can monitor how often a VM instance's health state changes by creating a metric that tracks the health state changes of that particular VM.

To create the metric and monitor the changes, do the following:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and instance name.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         labels."compute.googleapis.com/instance_name"="INSTANCE_NAME"
         

  3. In the **Query results** section, click **Actions** and then click **Create metric**.

  4. On the **Create logs metric** page, do the following:

     1. Set the **Metric Type** as **Counter**.
     2. Enter a **Log metric name** , for example `health-mig-xyzq`.

The **Build filter** section displays the log query from the **Logs Explorer**. You can also configure the metric's filter to account for only disruptive states, such as `UNHEALTHY` and `TIMEOUT`, by adding `severity>=WARNING` to the filter.

     3. Under **Labels** , click **Add label**.

     4. Enter a **Label name** , for example`health_state`.

     5. Set the **Label type** as `STRING`.

     6. Set the **Field name** to `jsonPayload.instanceHealthStateChange.detailedHealthState`. This will allow you to distinguish between different health state changes.

     7. Click **Done** to add the label.

     8. Click **Create metric**.

  5. Go to the [**Logs-based Metrics**](https://console.cloud.google.com/logs/metrics) page and find the newly created metric.

  6. Click the menu _more_vert_ in the metric's row and select **View in Metrics Explorer**. The [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) opens and displays the graph that represents the health state changes of the VM instance which you specified in the query.




### Monitoring health state changes of all VMs in a MIG

You can monitor the health state changes of all managed instances by creating a metric that tracks the health state changes of the managed instances.

To create the metric and monitor the changes, do the following:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and managed instance group's name.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         resource.labels.instance_group_manager_name="MIG_NAME"
         

  3. In the **Query results** section, click **Actions** and then click **Create metric**.

  4. On the **Create logs metric** page, do the following:

     1. Set the **Metric Type** as **Counter**.
     2. Enter a **Log metric name** , for example `health-mig-xyzq`.
     3. Under **Labels** , click **Add label**.
     4. Enter a **Label name** , for example`health_state`.
     5. Set the **Label type** as `STRING`.
     6. Set the **Field name** to `jsonPayload.instanceHealthStateChange.detailedHealthState`. This will allow you to distinguish between different health state changes.
     7. Click **Done** to add the label.
     8. Click **Create metric**.
  5. Go to the [**Logs-based Metrics**](https://console.cloud.google.com/logs/metrics) page and find the newly created metric.

  6. Click the menu _more_vert_ in the metric's row and select **View in Metrics Explorer**. The [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) opens and displays the graph that represents the health state changes of all the VM instances in the managed instance group which you specified in the query.




### Identifying VMs that frequently go unhealthy

You can identify problematic VMs that frequently go `UNHEALTHY` by creating a metric that tracks the health state changes of all VM instances in your MIG and grouping the metric by instances.

To create the metric and group by instances, do the following:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and managed instance group's name.
         
         resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         resource.labels.instance_group_manager_name="MIG_NAME"
         

  3. In the **Query results** section, click **Actions** and then click **Create metric**.

  4. On the **Create logs metric** page, do the following:

     1. Set the **Metric Type** as **Counter**.
     2. Enter a **Log metric name** , for example `health-mig-xyzq`.
     3. Under **Labels** , click **Add label**.
     4. Enter a **Label name** , for example`health_state`.
     5. Set the **Label type** as `STRING`.
     6. Set the **Field name** to `jsonPayload.instanceHealthStateChange.detailedHealthState`. This will allow you to distinguish between different health state changes.
     7. Click **Done** to add the label.
     8. Similarly, add a second label, for example `instance`, with the **Field name** set to `jsonPayload.instanceHealthStateChange.instance`.
     9. Click **Create metric**.
  5. Go to the [**Logs-based Metrics**](https://console.cloud.google.com/logs/metrics) page and find the newly created metric.

  6. Click the menu _more_vert_ in the metric's row and select **View in Metrics Explorer**. The [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) opens and displays the graph that represents the health state changes of all the VM instances in the managed instance group which you specified in the query.

  7. Set the **Group By** to `instance` to see the aggregate number of health state changes for each instance.




The instances with the most health state changes in aggregate are the ones that most frequently go unhealthy.

### Checking what caused an autohealing attempt

You can find out what caused an autohealing attempt by filtering logs for `repair` operations for given VM instance.

To filter the repair operations, do the following:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and the instance's name.
         
         resource.type="gce_instance" AND
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event" AND
         protoPayload.methodName="compute.instances.repair.recreateInstance" AND
         protoPayload.resourceName=~"/INSTANCE_NAME$"
         

  3. Click **Run query**. The **Query results** will show all autohealing attempts on the VM with the reason of autohealing in `protoPayload.status.message`.




### Checking if autohealing succeeded for a VM

You can find out whether an autohealing attempt succeeded for a VM instance by filtering logs for `repair` operations and health changes by VM instance name. If the instance's health state changed to `HEALTHY` after a repair operation, you will see a corresponding health state change log. Follow the steps:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and the instance's name.
         
         (resource.type="gce_instance" AND
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event" AND
         protoPayload.methodName="compute.instances.repair.recreateInstance" AND
         protoPayload.resourceName=~"/INSTANCE_NAME$")
         OR
         (resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         labels."compute.googleapis.com/instance_name"="INSTANCE_NAME")
         

The first part of the query displays the instance repair operations, which indicate that recreation was triggered by MIG autohealing to make the instance healthy again. The second part of the query displays all health state changes of the VM instance.

In the **Query results** , the health state change event with `detailedHealthState` set to `HEALTHY` shortly after a repair operation shows that the autohealing attempt was successful.




### Determining initial delay value of a MIG

Determining an appropriate [initial delay](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#autohealing_behavior) value for MIG autohealing is easier with VM instance health state logging. You can use logs to observe the time between when the `instances.insert` operation finished and when the first healthy signal was received for a set of instances in a group. This time interval reveals how long instances take to fully boot up. As some VMs might boot up slower than others, Google recommends adding some margin to the observed initialization time (from insert operation to healthy state) when specifying the initial delay in the autohealing policy.

To measure the time between the instance insert operation and the instance becoming healthy, run a query for `insert` operations and health change logs by VM instance name. Use timestamps from both operations to calculate the instance's initialization time. Follow the steps:

  1. Go to the **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the **Query** builder, using your project ID and the instance's name.
         
         (resource.type="gce_instance" AND
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity" AND
         protoPayload.request.@type="type.googleapis.com/compute.instances.insert" AND
         operation.last="true" AND
         protoPayload.resourceName=~"/INSTANCE_NAME$") OR
         (resource.type="gce_instance_group_manager" AND
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:* AND
         labels."compute.googleapis.com/instance_name"="INSTANCE_NAME")
         

The first part of the query shows the completion of the VM insert operation. The second part shows all health state changes for the VM.

In the **Query results** , the timestamp of the health state change event with `detailedHealthState` set to `HEALTHY` shortly after the insert operation reveals the time needed for this VM to boot up.

  3. Repeat the steps for a few more VMs to get a better approximate value of the initial delay parameter.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
