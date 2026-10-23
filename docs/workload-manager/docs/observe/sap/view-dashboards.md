---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards/
title: View observability metrics for SAP \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:00:41.768842+00:00
---

# View observability metrics for SAP  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  View observability metrics for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view the system health status of your SAP workloads by using the observability service in Workload Manager. These metrics help you perform root cause analysis and troubleshoot issues with your workloads.

![Observability metrics](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/graphs.png)

## View system dashboard

To view the system dashboard for SAP workloads in a Google Cloud project, do the following:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/systems)

  2. Select a Google Cloud project.

  3. Select **Observability** from the left navigation menu.

If prompted, enable the required APIs for observability and configure the Workload Manager service agent properly. For more information, see [Prerequisites for SAP observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites).

If you have all the required permissions, you can see a table on the dashboard that lists all SAP systems in the project.

![System dashboard](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/system-dashboard.png)

For each SAP system, review the following information:

Field | Description  
---|---  
**System** |  This field displays the SAP system identifier (SID) of your SAP workload.
     * If the application and database SIDs are the same, then the table contains one entry for both.
     * If the application and database SIDs are different, then the table contains an entry in the format `\[APP_SID\]-\[DB_SID\]`.  
**Observability pre-reqs** |  This field indicates whether you've successfully completed the prerequisites required to observe your SAP workload by using the Workload Manager observability service.
     * The value **Enabled** means that you've successfully completed the observability prerequisites for all compute instances that are running your SAP workload.
     * The value **Error** means that the observability prerequisites are pending for at least one compute instance that is running your SAP workload. For information about what's missing, view the **Overview** , **Applications** , and **Databases** tabs of the observability dashboard.  
**Workload type** | This field displays the value **SAP** because the observability service of Workload Manager is available only for SAP workloads.  
**Health** |  The overall health of your SAP workload. You can expand the health status for a system to see the individual health status of the application, database, and central services (ASCS) layers of your SAP system. For more information, see Understand system health status.  
**Products** | This field displays the names and versions of the SAP products that are part of your SAP workload.  
**Region** | This field displays the Google Cloud region, like `us-central1`, where you've deployed the Compute Engine instances that are running your SAP workload.  
**Last backup state** |  This field indicates whether the last backup operation for the SAP HANA data volume was successful or not. This field is based on the value of the `sap/hanamonitoring/backups/data` metric that the Agent for SAP collects from the SAP HANA database of your SAP workload.
     * The value **Successful** means that the last backup operation of the data volume of your SAP HANA database was successful.
     * The value **Failed** means that the last backup operation of the data volume of your SAP HANA database was not successful.
This field displays no value if any of the following conditions are met:
     * Your workload doesn't include an SAP HANA database.
     * There are no backups available for the data volume of your SAP HANA database.
     * You've not correctly configured the [SAP HANA monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics) feature of the Agent for SAP.
     * The SAP HANA user that you've defined in the agent's configuration doesn't have the permissions required to query the database about data backups.  
**Last backup on** |  This field displays the date and time of the last backup operation for the SAP HANA data volume was performed. This field displays no value if any of the following conditions are met:
     * Your workload doesn't include an SAP HANA database.
     * There are no backups available for the data volume of your SAP HANA database.
     * You've not correctly configured the [SAP HANA monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics) feature of the Agent for SAP.
     * The SAP HANA user that you've defined in the agent's configuration doesn't have the permissions required to query the database about data backups.  

**Note:** If your SAP system includes a disaster recovery (DR) site, then the DR site is displayed as a secondary instance in the **Overview** tab of the Workload Manager observability dashboard.

## Understand system health status

Workload Manager uses a color state to describe the status of an SAP system and it helps you identify its layers and sublayers. The following table describes each status you see on the observability dashboard.

Status icon | Status | Description  
---|---|---  
![](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/status_info_gray.svg) | Gray (Unspecified) | 

  * The observability service in Workload Manager doesn't have enough values from the metric sources for the most important metrics in order to define the health of a system and therefore the status is being marked as _Unspecified_. These metrics are usually associated with availability of any of the elements of the SAP system such as application servers and SAP HANA database.
  * Metrics with an unknown or missing value causes the system status to be Unspecified. The specific item of the system is marked as Gray or Unspecified to show that the layer or sublayer health cannot be properly calculated as the Workload Manager observability service doesn't have all the required information.

  
![](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/green-checkmark.png) | Green (Healthy) | 

  * The reported values for each of the metrics are within the defined thresholds for a healthy system.
  * The system is healthy and has no issues from the perspective of the metrics monitored for SAP observability.

  
![](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/status_warning.svg) | Yellow (Caution) | 

  * The reported values for each of the metrics are within the defined thresholds for an unhealthy system.
  * The system has low priority issues that don't affect the availability of the system and the system administrator can verify the system when possible.
  * The Caution status is usually related to deterioration of the system performance but the impact doesn't represent a risk for the availability of the system. It might also be related to part of the system being unavailable without putting the whole system at risk.

  
![](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/red-exclamation.png) | Red (Critical) | 

  * The reported values for each of the metrics are within the defined thresholds for an unavailable system.
  * The system is experiencing availability and/or performance issues that are impacting the user experience and workloads potentially causing a disruption to the business operations. The system administrator should check the system as soon as possible.

  
  
The system health is calculated based on the report metric values for each system layer and sublayer. The following figure provides a general representation of the system layers and sublayers:

![SAP system layers and sublayers](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/layers.png)

The system layers used for evaluating SAP workloads are:

  * Central services
  * Application servers
  * Database servers



The number of sublayers depends on the architecture type of the SAP system that is being evaluated. For example, a centralized system has lesser number of sublayers than a distributed system and therefore the health status is tailored for the type of system that is displayed on the dashboard.

To get the overall status as _Healthy_ for the system, all of the layers and sublayers need to have a _Healthy_ status. Otherwise, the SAP system health status is marked as _Unspecified_. The following example shows a centralized system with the overall status as _Unspecified_ due to missing metric values:

  * Application servers: 
    * Application server 1 (Missing): Gray
    * **Application servers layer:** Gray
  * Central Services: 
    * Central Services: Green
    * **Central Services layer:** Green
  * Database Servers:

    * SAP HANA primary instance: Green
    * **Database Servers layer:** Green
  * **Overall Health:** Gray (Unspecified)




The following example shows a more complex scenario of a distributed deployment with high availability showing the overall health status as _Red (Critical)_ due to missing metric values:

  * Application servers: 
    * Application server 1: Red
    * Application server 2: Green
    * Application server N: Green
    * **Application servers layer:** Red
  * Central Services: 
    * Central Services: Green
    * ERS: Green
    * **Central Services layer:** Gray
  * Database Servers:

    * HANA primary instance: Green
    * HANA secondary instance: Green
    * **Database Servers layer:** Green
  * **Overall Health:** Red (Critical)




![System dashboard with critical status](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/application-critical.png)

## SAP observability metrics

Workload Manager calculates the system health status for your SAP workloads by using the following metrics:

  * Metrics from Compute Engine instances hosting the SAP workloads: 
    * Available by default, no external agent is required.
    * Metrics are located under [compute.googleapis.com](http://compute.googleapis.com).
  * Metrics collected by [OPS Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent):

    * Requires the OPS Agent to be installed and running on the VM to have the metrics reported to Cloud Monitoring.
    * Metrics are located under [agent.googleapis.com](https://console.cloud.google.com/monitoring/metrics-explorer). 
      * The required metrics using in observability for SAP are included in the non-chargeable tier.
  * Metrics collected by [Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning):

    * Requires the Agent for SAP to be installed and running on the VM to have the metrics reported to Cloud Monitoring.
    * Metrics are located under [workload.googleapis.com/sap](https://console.cloud.google.com/monitoring/metrics-explorer). The following metrics are used to calculate the health status:

      * `workload.googleapis.com/sap/hana/availability`
      * `workload.googleapis.com/sap/hana/ha/availability`
      * `workload.googleapis.com/sap/hanamonitoring/system/replication_data_latency/total_time`
      * `workload.googleapis.com/sap/hana/service`
      * `workload.googleapis.com/sap/cluster/nodes`
      * `workload.googleapis.com/sap/cluster/resources`
      * `workload.googleapis.com/sap/nw/instance/role`
      * `workload.googleapis.com/sap/nw/service`
      * `workload.googleapis.com/sap/nw/availability`



## System details page

You can click a System ID (SID) from the observability dashboard to see a detailed view of the system.

### Overview tab

The **Overview** tab shows high-level information about your SAP system, which is organized as follows:

  * The first section shows metadata about your SAP system such as SID, the architecture in use, the region where the system is deployed, whether it's a scale-up or scale-out system, and the SAP applications and databases that are part of your SAP system.

  * The next section shows a card for each layer of your SAP system, such as application servers, SAP Central Services instance, and database servers. You can view their overall health status and names of the compute instances that host them.

  * The **Health Insights** section lists the unhealthy compute instances that are part of your SAP system. This table provides the reasons for why the compute instances are deemed unhealthy.

  * The **Maintenance Events** section lists the compute instances in your SAP system that either have an upcoming scheduled host maintenance event, or recently completed one.

For more information, see [host maintenance](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) for a list of supported machine families.




### Applications and Databases tabs

The **Applications** and **Database** tabs show more detailed information about the respective layers of the system:

  * The **Applications** tab shows information about application servers and the SAP Central Services instance. The **Databases** tab shows information about the database servers running in your SAP system.

  * Both **Applications** and **Databases** tabs list the underlying compute instances and show the following information:

    * **VM Name** : the name of the compute instance
    * **VM Status** : indicates whether the compute instance is running or not
    * **SAP #** : the SAP instance number you've assigned to the app or database server while deploying your SAP system
    * **Role** : the role you've assigned to the compute instance in your SAP system, which includes the following: 
      * For instances used as application servers: **Application Server** , **Central Services** , **ERS**.
      * For instances used as database servers to run SAP HANA: **HANA Primary** , **HANA Secondary**
    * **Zone** : the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the compute instance is deployed
    * **Machine type** : the machine type of the compute instance, for example `n2-highmem-32` or `c4-highmem-48`
    * **Agent version** : information about the status and version of Google Cloud's Agent for SAP that is running on the compute instance

The agent's version is displayed only when the agent is installed and actively running on the compute instance. When you hover over the icon that is displayed in the field, you can view more information about the agent's status.

    * **Process metrics** : indicates whether or not you've correctly enabled the [process monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#process_monitoring_metrics) feature of the agent

    * **System discovery** : indicates whether or not you've correctly enabled the [SAP system discovery](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap-system-discovery) feature of the agent

    * **HANA monitoring** : this field is displayed only in the **Databases** tab and indicates whether or not you've correctly enabled the [SAP HANA monitoring](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics) feature of the agent

**Note:** If the agent setup is incomplete on even one compute instance that runs your SAP workload, then a red banner appears at the top of the **Overview** , **Applications** , and **Databases** tabs in the observability dashboard.
    * **Connect** : the options such as **SSH** using which you can connect to the compute instance. Your users might require additional permission to connect to the compute instance.
  * Both **Applications** and **Databases** tabs also include a variety of charts and metrics that are filtered to only include the applicable resources in the chosen layer of your SAP system.

    * You can switch between the predefined and custom dashboards.
    * The predefined dashboard in the **Applications** tab shows the following high-level sections:

      * Availability
      * Performance
      * Storage
      * Networking
      * Application server performance
      * Work process utilization
      * NetWeaver memory
      * Workload statistics
    * The dashboard in the **Databases** tab shows the following high-level sections:

      * Availability
      * Performance
      * Database Performance
      * Storage
      * Network
      * Database Utilization
      * Database Capacity
      * Database Backups



#### View SAP events on predefined dashboards

You can configure the predefined dashboards in the **Applications** and **Databases** tabs to view annotations for supported SAP event types.

Viewing SAP events as annotations on observability dashboards can help you correlate the events with issues that you might experience in your SAP systems. For more information about event annotations, see [About event annotations](https://docs.cloud.google.com/monitoring/dashboards/show-events#about_event_annotations).

For information about the SAP event types that you can view as annotations on predefined observability dashboards, see Supported SAP event types.

To view the supported SAP event types as annotations on your observability dashboard, complete the following steps:

  1. Make sure that the compute instances that are part of your SAP system run version 3.7 or later of Agent for SAP.

For information about how to update the agent instance, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

  2. In the Google Cloud console, go to the Workload Manager **Observability** page.

[Go to Observability](https://console.cloud.google.com/workload-manager/systems)

  3. To view SAP events in the application layer of your SAP system, go to the **Applications** tab. To view SAP events in the database layer, go to the **Databases** tab.

  4. Click **Annotations** , select the event types that you want to view on your dashboard, and then click **Apply**.

Occurrences of the selected SAP events start appearing in the charts of the predefined observability dashboard. The following image shows an example observability dashboard in the **Applications** tab, with annotations for the **SAP Availability** types of events:

![Workload Manager observability dashboard showing SAP events with annotations](https://docs.cloud.google.com/static/workload-manager/docs/observe/images/wlm-obs-sap-apps-tab-annotations.png)

  5. To view additional information about the event, hover over the event, and then click **View**.

The Logs Explorer appears, filtered to show information about the selected event.




##### Supported SAP event types

The following table describes the SAP event types that you can show as annotations on predefined observability dashboards. Each event type requires Agent for SAP to collect the required metrics.

Event type | Description  
---|---  
**SAP Availability** |  Provides information about the status of the following resources whenever they stop, start, or face any errors: SAP HANA, SAP NetWeaver, and the nodes and resources in Pacemaker-managed Linux high-availability (HA) clusters. Showing events of this type as annotations requires Agent for SAP to collect the following [ Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics):

  * `sap/hana/service`
  * `sap/hana/availability`
  * `sap/nw/service`
  * `sap/nw/availability`
  * `sap/cluster/nodes`
  * `sap/cluster/resources`

  
**SAP Backint** |  Provides information about Backint based backup and recovery operations. Showing events of this type as annotations requires Agent for SAP to collect the Backint metrics. For information about these metrics, see [ Backint metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#backint_metrics_collection).  
**SAP Operations** |  Provides information about the status of data replication in SAP HANA high-availability (HA) systems. Showing events of this type as annotations requires Agent for SAP to collect the following [ Process Monitoring metric](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics): `sap/hana/ha/replication`.  
  
## Remove workloads from the observability dashboard

To remove an SAP workload from the observability dashboard, complete the following steps:

  1. On the compute instances that run your SAP workload, disable the discovery feature in the configuration file of Google Cloud's Agent for SAP:

###  VM Extension Manager 

If you're using a VM Extension Manager policy to manage the agent on your compute instances, then complete the following steps:

     1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

     2. Select the policy that manages the Google Cloud's Agent for SAP for your SAP workload.

     3. Click **Edit**.

     4. In the **Manage extensions** section, edit the agent's configuration as follows:

        * In the `discovery_configuration` section, set the value of the `enable_discovery` parameter to `false`.
        * If you no longer want to use the process monitoring feature of the agent, then disable it by setting the value of the `collect_process_metrics` parameter to `false`.
        * If you no longer want to use the SAP HANA monitoring feature of the agent, then disable it by setting the value of the `enabled` parameter, in the `hana_monitoring_configuration` section, to `false`.
     5. Click **Save**.

###  Package manager 

If you're not using a VM Extension Manager policy to manage the agent on your compute instances, then you disable the discovery feature of Google Cloud's Agent for SAP by completing the following steps:

     1. Establish an SSH connection to a compute instance that runs your SAP workload.

     2. Disable the agent's discovery feature:
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=sap_discovery -disable
            

     3. If you no longer want to use the process monitoring feature of the agent, then disable it:
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -disable
            

     4. If you no longer want to use the SAP HANA monitoring feature of the agent, then disable it:
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -disable
            

     5. Repeat the preceding steps for all the compute instances that run the SAP workload that you want to remove from the observability dashboard.

It can take up to 48 hours for Workload Manager to delete the metrics collected from your SAP workload, following which your SAP workload is removed from the Workload Manager **Observability** page in the Google Cloud console.

  2. Optionally, to immediately remove the SAP workload from the Workload Manager **Observability** page in the Google Cloud console, run the following command:
         
         curl -X "DELETE" 'https://workloadmanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insights/SYSTEM_IDENTIFIER' -H "Authorization: Bearer $(gcloud auth print-access-token)"
         

Replace the following:

     * `PROJECT_ID`: the project ID of the Google Cloud project where you've deployed your SAP workload.
     * `LOCATION`: the Google Cloud region where you've deployed your SAP workload. For example: `us-central1`.
     * `SYSTEM_IDENTIFIER`: the identifier for your SAP workload in Workload Manager, which you can view in the URL in the Google Cloud console. For example:
           
           https://console.cloud.google.com/workload-manager/systems/**a1b2c3d4** /...

  3. Verify that your workload is no longer listed on the **Observability** page in Google Cloud console.

If you didn't run the `curl` command that immediately removes the workload from the **Observability** page, then it can take up to 48 hours for your SAP workload to disappear from that page.

[Go to Observability](https://console.cloud.google.com/workload-manager/systems)




## Create custom alerts

You can use the [alerting policies in Cloud Monitoring](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards/) and create custom alerts based on the displayed metrics on the observability dashboards. Once you create an alerting policy, you receive notifications based on the configured threshold for each of the available Cloud Monitoring metrics including metrics related to SAP workloads.

## What's next

  * [Modify observability dashboards](https://docs.cloud.google.com/workload-manager/docs/observe/sap/modify-dashboards).
  * [Troubleshoot observability issues for SAP](https://docs.cloud.google.com/workload-manager/docs/observe/sap/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
