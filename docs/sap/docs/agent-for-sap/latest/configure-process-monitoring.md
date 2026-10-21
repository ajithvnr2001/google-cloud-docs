---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring/
title: Configure Process Monitoring metrics collection \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:50.898443+00:00
---

# Configure Process Monitoring metrics collection  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure Process Monitoring metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud's Agent for SAP to collect the Process Monitoring metrics from your SAP systems.

For information about this feature, see [Process Monitoring using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring).

**Note:** The collection of Process Monitoring metrics is supported only on Linux. It is not supported on Windows.

## Before you begin

  * Validate your installation of Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).
  * If you have installed the agent on a Bare Metal Solution server, then make sure that you have completed the required prerequisites and set up a service account. For instructions, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).



### Required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect Process Monitoring metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect the Process Monitoring metrics from the Compute Engine instance that hosts your SAP system: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write the collected metrics to Cloud Monitoring: [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) 
  * If you are using Secret Manager to store the password to connect to the SAP HANA database: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect Process Monitoring metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect Process Monitoring metrics:

  * Collect the Process Monitoring metrics from the host Compute Engine instance and write them to Cloud Monitoring: 
    * `monitoring.timeSeries.create`
    * `compute.instances.get`
    * `compute.nodeGroups.list`
    * `compute.nodeGroups.get`
  * If you are using Secret Manager to store the password to connect to the SAP HANA database, then to access the secret: `secretmanager.versions.access`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required SAP HANA roles

To let the agent collect metrics from your SAP HANA database, make sure that the SAP HANA user that you specify in the agent's configuration file has the `MONITORING` role.

For information about this role, see the SAP document [Standard Database Roles](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/de421861bb571014846288086be76719.html).

## Enable Process Monitoring metrics collection

To enable the collection of Process Monitoring metrics using Google Cloud's Agent for SAP, follow these steps:

  1. Establish an SSH connection with your host Compute Engine instance.

  2. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

Alternatively, you can also perform this configuration by running commands. For more information, see [Configuration commands for Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands).

  3. In the `collection_configuration` section, perform the following:

     * For the parameter `collect_process_metrics`, specify the value `true`.
     * To enable the collection of process monitoring metrics related to your SAP HANA database instances, you need to configure additional parameters in the `hana_metrics_config` section. For information about these parameters, see Configuration parameters.
  4. Optionally, under the `cloud_properties` section, you can update the parameter values that are set automatically. To do so, add the `cloud_properties` section to your configuration file, and then specify the required parameters and their values.

  5. Save the configuration file.

  6. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you don't need to restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent




### Example configuration files

### Compute Engine instance

The following examples are completed configuration files of Google Cloud's Agent for SAP, running on a Compute Engine instance, where the collection of Process Monitoring metrics is enabled:

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file. 

  * The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": false,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 30,
            "slow_process_metrics_frequency": 120,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hdbuserstore_key": "user_store_key"
            }
          },
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }

  * The following example uses a username and Secret Manager secret for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": false,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 30,
            "slow_process_metrics_frequency": 120,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hana_db_password_secret_name": "db_pwd_secret_name"
            }
          },
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }

  * The following example uses a username and password for SAP HANA authentication. We recommend that you instead use a Secret Manager secret or [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication. 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": false,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 5,
            "slow_process_metrics_frequency": 30,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hana_db_password": "TempPa55word"
            }
          },
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }




### Bare Metal Solution server

The following examples are completed configuration files of Google Cloud's Agent for SAP, running on a Bare Metal Solution server, where the collection of Process Monitoring metrics is enabled:

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file. 

  * The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": true,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 30,
            "slow_process_metrics_frequency": 120,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hdbuserstore_key": "user_store_key"
            }
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1",
            "image": "rhel-8"
          },  
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }

  * The following example uses a username and Secret Manager secret for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": true,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 30,
            "slow_process_metrics_frequency": 120,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hana_db_password_secret_name": "db_pwd_secret_name"
            }
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1",
            "image": "rhel-8"
          },  
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }

  * The following example uses a username and password for SAP HANA authentication. We recommend that you instead use a Secret Manager secret or [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication. 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": true,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "collect_process_metrics": true,
            "process_metrics_frequency": 5,
            "slow_process_metrics_frequency": 30,
            "hana_metrics_config": {
              "hana_db_user": "db_user_name",
              "sid": "DEH",
              "hana_db_password": "TempPa55word"
            }
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1",
            "image": "rhel-8"
          },  
          "discovery_configuration": {
            "enable_discovery": true,
            "enable_workload_discovery": true
          },
          "hana_monitoring_configuration": {
            "enabled": false
          }
        }




### Configuration parameters

The following table explains the configuration parameters of Google Cloud's Agent for SAP that are specific to the collection of the Process Monitoring metrics.

Parameters  
---  
`provide_sap_host_agent_metrics` |  `Boolean` To enable the collection of the metrics required by the SAP Host Agent, specify `true`. Default is `true`.   
Don't set `provide_sap_host_agent_metrics` to `false` unless you are directed by Cloud Customer Care or SAP Support.   
`bare_metal` |  `Boolean` When the agent is installed on a Bare Metal Solution server, specify `true`. Default is `false`.  
`log_level` |  `String` To set the logging level of the agent, set the required value. The available log levels are as follows:

  * `DEBUG`
  * `INFO`
  * `WARNING`
  * `ERROR`

Default is `INFO`. Don't change the logging level unless you are directed by Cloud Customer Care.  
`log_to_cloud` |  `Boolean` To redirect the agent's logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), specify `true`. The default is `true`.  
`cloud_properties.project_id` | `String` If your SAP system is running on a Bare Metal Solution server, then specify the project ID of the Google Cloud project that you are using with Bare Metal Solution.  
  
When the agent runs on a Compute Engine instance, by default, the agent detects the project ID automatically.  
`cloud_properties.instance_name` |  `String` If your SAP system is running on a Compute Engine instance, then specify the name that compute instance. The agent automatically detects the compute instance name upon installation. If your SAP system is running on a Bare Metal Solution server, then specify the name of that server.  
`cloud_properties.region` | `String` If your SAP system is running on a Bare Metal Solution server, then specify the region where you've deployed the Bare Metal Solution server.  
  
When the agent runs on a compute instance, by default, the agent uses the region where the compute instance is deployed. | `cloud_properties.zone` | `String` When the agent runs on a compute instance, by default, the agent uses the zone where the compute instance is deployed.  
`cloud_properties.image` | `String` Specify the OS image name of the instance.  
  
When the agent runs on a compute instance, by default, the agent automatically detects the OS image used by the compute instance.  
`cloud_properties.numeric_project_id` | `String` Specify the numeric ID of the Google Cloud project where the SAP system is running.  
  
When the agent runs on a compute instance, by default, the agent automatically detects project number.  
`discovery_configuration.enable_workload_discovery` |  `Boolean` To let the agent collect the names and versions of the SAP products running on the host, specify `true`. The default value is `true`. For more information, see the agent's codebase in the `google-cloud-sap-agent` GitHub repository under [GoogleCloudPlatform/sapagent](https://github.com/GoogleCloudPlatform/sapagent).   
`discovery_configuration.enable_discovery` |  `Boolean` To send to Cloud Logging the information that the agent collects about the SAP products running on the host, specify `true`. The default value is `true`. If you specify the value `false`, then the agent stores the collected information on the host and doesn't send it to Cloud Logging.   
`collection_configuration.collect_process_metrics` |  `Boolean` To enable Process Monitoring metrics collection, specify `true`. Default is `false`.  
This parameter is applicable only for Linux.  
  
If you enable Process metrics collection for SAP HANA, then you need to set up additional parameters listed under `hana_metrics_config`.  
`collection_configuration.process_metrics_frequency` |  `Int` From version 2.6, this parameter determines the collection frequency of the [fast-changing Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#pm_metric_types), in seconds. Fast-changing Process Monitoring metrics are: `sap/hana/availability`, `sap/hana/ha/availability`, and `sap/nw/availability`.  The default value for this parameter is `30` seconds. We recommend that you use this default value.  All other (_slow-changing_) Process Monitoring metrics are collected at a default frequency of 120 seconds. To change the collection frequency of the slow-changing Process Monitoring metrics, use the parameter `slow_process_metrics_frequency`.  
`collection_configuration.slow_process_metrics_frequency` |  `Int` Specify the collection frequency of the [slow-changing Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#pm_metric_types), in seconds.  The default value for this parameter is `120` seconds.  
`collection_configuration.process_metrics_to_skip` |  `Array` Specify the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics) that you don't want the agent to collect. This parameter accepts a comma-separated value of Process Monitoring metric names. For example: `"process_metrics_to_skip": ["/sap/nw/abap/sessions", "/sap/nw/abap/rfc"]`.   
`collection_configuration.hana_metrics_config.hana_db_user` | `String` Specify the database user account that the agent uses to query SAP HANA. Default is `SYSTEM`.  
`collection_configuration.hana_metrics_config.hana_db_password` | `String` Specify the plain text password for the database user account that the agent uses to query SAP HANA. Instead of specifying a plain text password, we recommend that you use one of the following options:

  * `hana_db_password_secret_name`, for which you specify a secret stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).
  * `hdbuserstore_key`, for which you specify an [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html).

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.hana_metrics_config.hana_db_password_secret_name` | `String` To securely provide the password for the database user account that the agent uses to query SAP HANA, specify the name of the [secret](https://docs.cloud.google.com/secret-manager/docs/overview#secret) that contains the security credentials for the database user account. **Important:** The secret and the host Compute Engine instance must exist in the same Google Cloud project. The agent collects the SAP HANA related metrics only when you specify either `hana_db_password_secret_name`, `hdbuserstore_key`, or `hana_db_password`. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.hana_metrics_config.hdbuserstore_key` |  `String` To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.hana_metrics_config.sid` |  `String` Specify the SID of your SAP HANA instance. If you're using an `hdbuserstore` key to authenticate to SAP HANA, then refer to the `hdbuserstore_key` section.  
  
## Validate the setup for Process Monitoring metrics collection

You can validate if you have the correct Google Cloud setup for the collection of the Process Monitoring metrics by running the agent's `status` command. This command is supported from version 3.7 of the agent.

To do this, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  2. Run the following command:
         
         sudo /usr/bin/google_cloud_sap_agent status -f="process_metrics"
         

If your Google Cloud setup for Process Monitoring metrics collection is correct, then the output includes the following. Your configuration might have values other than the **`default`** ones.
         
         Agent Status:
             ...
             Systemd Service Enabled: True
             Systemd Service Running: True
             Cloud API Full Scopes: True
             Configuration File: /etc/google-cloud-sap-agent/configuration.json
             Configuration Valid: True
         ...
         ----------------------------------------------------------------------------
         Process Metrics: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 collect_process_metrics:        true (configuration file)
                 process_metrics_frequency:      30    (default)
                 process_metrics_to_skip:        []   (default)
                 slow_process_metrics_frequency: 120   (default)
         ...
         

  3. If your output conveys that some setup is missing, then review the information provided in the preceding sections, perform the required actions, and then re-run the `status` command to re-validate the setup.




## View the collected metrics

To visualize the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#process_monitoring_metrics) that the agent collects, you can use the following custom dashboards that Google Cloud provides:

  * **Agent for SAP - HANA Overview** : This dashboard provides charts that display status overview for the following metrics: SAP HANA Availability, SAP HANA HA Availability, SAP HANA HA Replication, SAP HANA Service Status, HA Cluster - Node State, and HA Cluster - Resource State for SAP Instances.

The JSON file for this dashboard is `sap-agent-status-overview.json`.

  * **Agent for SAP - HANA Raw Metrics** : This dashboard provides charts that display raw metric values for the following metrics: SAP HANA Availability, SAP HANA HA Availability, SAP HANA HA Replication, SAP HANA Service Status, HA Cluster - Node State, and HA Cluster - Resource State for SAP Instances.

The JSON file for this dashboard is `sap-agent-raw-metrics.json`.




### Install dashboards

To install a custom dashboard, complete the following steps:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Monitoring** page:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation panel, click **Dashboards**.

  3. Click the **Sample library** tab.

![Display of the sample library tab selected.](https://docs.cloud.google.com/static/sap/docs/images/dashboard-select-sample-library.png)

  4. To filter the agent-specific custom dashboards, in the **Filter** field, type `Agent for SAP`.

  5. (Optional) To view details about a dashboard or to preview its contents, click **Preview**.

  6. Select the dashboard that you want to install.

  7. Click **Import** , and then click **Confirm**.

The dashboard is added to the available dashboards in your Google Cloud project. To see your dashboard, follow the instructions in View the installed dashboard.




###  Google Cloud CLI 

  1. Open the Cloud Shell:

[Open Cloud Shell](https://console.cloud.google.com/monitoring?cloudshell=true)

  2. In the Cloud Shell, clone or download the repository:
         
         git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/

  3. In the Cloud Shell, install the required dashboard using the corresponding JSON file:
         
         gcloud monitoring dashboards create --config-from-file=CONFIG_FROM_FILE

Replace `CONFIG_FROM_FILE` with the path to the JSON file that contains the dashboard configuration. Dashboard configuration files can be located at path: `monitoring-dashboard-samples/dashboards/google-cloud-agent-for-sap`.

The dashboard is added to the available dashboards in your Google Cloud project. To see your dashboard, follow the instructions in View the installed dashboard.




### View the installed dashboards

To view the installed dashboards, follow these steps:

  1. In the Google Cloud console, go to the **Monitoring** page:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation panel, click **Dashboards**.

  3. Click the dashboard name in the list.




If you have a lot of dashboards, then you can filter for custom dashboards or for the name of the new dashboard. For information on filtering this list, see [View custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#view-dashboard).

The following image is an example that shows a part of the custom dashboard for SAP HANA metrics in Monitoring.

![Screen capture shows the custom dashboard for SAP HANA metrics
in Monitoring](https://docs.cloud.google.com/static/sap/docs/images/agent-for-sap-hana-raw-metrics.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
