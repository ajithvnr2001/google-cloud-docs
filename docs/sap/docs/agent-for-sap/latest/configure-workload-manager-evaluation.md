---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation/
title: Configure Workload Manager evaluation metrics collection \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:42.070693+00:00
---

# Configure Workload Manager evaluation metrics collection  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure Workload Manager evaluation metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud's Agent for SAP to collect the Workload Manager evaluation metrics from your SAP systems.

For information about this feature, see [Workload Manager evaluation using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/workload-manager-evaluation).

**Note:** The collection of Workload Manager evaluation metrics is supported only on Linux. It is not supported on Windows.

## Before you begin

  * Validate your installation of Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).
  * If you have installed the agent on a Bare Metal Solution server, then make sure that you have completed the required prerequisites and set up a service account. For instructions, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).
  * Make sure that the Workload Manager API is enabled for your Google Cloud project.

[Enable the Workload Manager API](https://console.cloud.google.com/apis/library/workloadmanager.googleapis.com)




### Required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect Workload Manager evaluation metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect the Workload Manager evaluation metrics from the Compute Engine instance that hosts your SAP system: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write the collected metrics to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 
  * If you are using Secret Manager to store the password to connect to the SAP HANA database: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect Workload Manager evaluation metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect Workload Manager evaluation metrics:

  * Collect the Workload Manager evaluation metrics from the host Compute Engine instance and write them to Workload Manager data warehouse: 
    * `monitoring.timeSeries.create`
    * `compute.zoneOperations.list`
    * `compute.disks.list`
    * `compute.nodeGroups.get`
    * `workloadmanager.insights.write`
  * If you are using Secret Manager to store the password to connect to the SAP HANA database, then to access the secret: `secretmanager.versions.access`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required SAP HANA roles

To let the agent collect metrics from your SAP HANA database, make sure that the SAP HANA user that you specify in the agent's configuration file has the `MONITORING` role.

For information about this role, see the SAP document [Standard Database Roles](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/de421861bb571014846288086be76719.html).

## Verify the agent version

Google Cloud recommends that you install the latest version of Agent for SAP for accurate evaluation of your SAP workloads because periodic releases of the Agent for SAP might add or change metrics that are used for the evaluation.

To ensure that you have the latest version of Google Cloud's Agent for SAP, you need to check for updates periodically and update the agent.

### Install an update

Select your operating system, and then follow the steps:

### RHEL

  1. Establish an SSH connection with your instance.
  2. Update your agent instance: 
     * (Recommended) To update to version 3.15 (latest) of the agent: 
           
           sudo yum --nogpgcheck update google-cloud-sap-agent

     * To update to a specific version of the agent: 
           
           sudo yum install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent). 




### SLES

  1. Establish an SSH connection with your instance.
  2. Update your agent instance: 
     * (Recommended) To update to version 3.15 (latest) of the agent: 
           
           sudo zypper --no-gpg-checks update google-cloud-sap-agent

     * To update to a specific version of the agent: 
           
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent). 




## Enable Workload Manager evaluation metrics collection

From version 3.2, new installations of Google Cloud's Agent for SAP are enabled by default to collect the Workload Manager evaluation metrics. If you're updating to version 3.2 from a previous version, you can also explicitly enable the feature. To do so, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.

  2. To let the agent collect the [Workload Manager evaluation metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#wlm_evaluation_metrics): 
         
         sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -enable

  3. To enable the collection of the "SAP HANA Insights" and "SAP HANA Security Best Practices" metrics:

     1. Open the agent's configuration file:
            
            /etc/google-cloud-sap-agent/configuration.json

Alternatively, you can also perform this configuration by running commands. For more information, see [Configuration commands for Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands).

     2. Add the `workload_validation_db_metrics_config` section after `collect_workload_validation_metrics`, and then specify the following parameters:

        * `hana_db_user`: specify the SAP HANA database user account that is used to query the SAP HANA instance.
        * `hostname`: specify the identifier for the machine, either local or remote, that hosts your SAP HANA instance.
        * `port`: specify the database port on which your SAP HANA instance accepts queries. For example, enter `30015` if your tenant database is listening on port `30015`.
        * `sid`: specify the SID of your SAP HANA instance
        * `hana_db_password_secret_name`: specify the name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) that stores the user account's password

As an alternative to the secret, you can use the `hdbuserstore_key` configuration parameter.

        * `hdbuserstore_key`: specify the [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) that authenticates the user you specified for `hana_db_user`

If you specify `hdbuserstore_key`, then you skip specifying the `hostname` and `port` parameters.

For information about these parameters, see Configuration parameters.

  4. Optionally, under the `cloud_properties` section, you can update the parameter values that are set automatically. To do so, add the `cloud_properties` section to your configuration file, and then specify the required parameters and their values.

  5. Save the configuration file.

  6. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent




### Example configuration files

### Compute Engine instance

The following examples are completed configuration files of Google Cloud's Agent for SAP running on a Compute Engine instance, where the collection of Workload Manager evaluation metrics is enabled.

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file. 

  * The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": false,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hdbuserstore_key": "user_store_key"
            },
            "collect_process_metrics": false
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
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hana_db_password_secret_name": "instance-id-hana-db-password-secret",
              "hostname": "localhost",
              "port": "30015"
            },
            "collect_process_metrics": false
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
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hana_db_password": "TempPa55word",
              "hostname": "localhost",
              "port": "30015"
            },
            "collect_process_metrics": false
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

The following examples are completed configuration files of Google Cloud's Agent for SAP running on a Bare Metal Solution server, where the collection of Workload Manager evaluation metrics is enabled.

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file. 

  * The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication: 
        
        {
          "provide_sap_host_agent_metrics": true,
          "bare_metal": true,
          "log_level": "INFO",
          "log_to_cloud": true,
          "collection_configuration": {
            "collect_workload_validation_metrics": true,
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hdbuserstore_key": "user_store_key"
            },
            "collect_process_metrics": false
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1"
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
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hana_db_password_secret_name": "instance-id-hana-db-password-secret",
              "hostname": "localhost",
              "port": "30015"
            },
            "collect_process_metrics": false
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1"
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
            "workload_validation_db_metrics_frequency": 3600,
            "workload_validation_db_metrics_config": {
              "hana_db_user": "system",
              "sid": "DEH",
              "hana_db_password": "TempPa55word",
              "hostname": "localhost",
              "port": "30015"
            },
            "collect_process_metrics": false
          },
          "cloud_properties": {
            "project_id": "my-project",
            "instance_name": "bms-machine-1",
            "region": "us-central1"
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

The following table explains the configuration parameters of Google Cloud's Agent for SAP that are specific to the collection of the Workload Manager evaluation metrics.

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
`collection_configuration.collect_workload_validation_metrics` |  `Boolean` To enable Workload Manager evaluation metrics collection, specify `true`. From version 3.2, the default value is `true`.  
This parameter is applicable only for Linux.  
`collection_configuration.workload_validation_metrics_frequency` | `Int` The collection frequency of the Workload Manager evaluation metrics in seconds. The default value is `300` seconds. We recommend that you don't modify the default collection frequency as it might impact the entire feature itself.If you need to modify the collection frequency of the Workload Manager metrics, then add the `workload_validation_metrics_frequency` parameter under the `collection_configuration` section and provide the required value.  
`collection_configuration.workload_validation_collection_definition.fetch_latest_config` |  `Boolean` Optional. The default value is `true`, which enables the agent to collect the latest set of Workload Manager evaluation metrics without requiring you to update the agent. If you want to turn off this behavior, then specify this parameter in your configuration file and set its value to `false`.  
`collection_configuration.workload_validation_db_metrics_config.hana_db_user` |  `String` Specify the user account that is used to query the SAP HANA instance. The user account must have the read permission to the SAP HANA database.  
`collection_configuration.workload_validation_db_metrics_config.hana_db_password` |  `String` Specify the password for the user account that is used to query the SAP HANA instance. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.workload_validation_db_metrics_config.hana_db_password_secret_name` |  `String` Specify the name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) that stores the user account's password. Alternatively, you can specify the `hdbuserstore_key` configuration parameter to authenticate the specified SAP HANA user. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.workload_validation_db_metrics_config.hdbuserstore_key` |  `String` To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `hdbuserstore_key`, then you can skip specifying the `hostname` and `port` parameters. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `hana_db_password` parameter, which is preferred over the `hana_db_password_secret_name` parameter. We recommend that you set only one authentication option in your configuration file.   
`collection_configuration.workload_validation_db_metrics_config.sid` |  `String` Specify the SID of your SAP HANA instance.  
`collection_configuration.workload_validation_db_metrics_config.hostname` |  `String` Specify the identifier for the machine, either local or remote, that hosts your SAP HANA instance. The following are the supported values:

  * If the host is a local machine, then specify the string `localhost` or the localhost loopback IP address, like `127.0.0.1`.
  * If the host is a remote machine, then specify its internal or external IP address.

  
`collection_configuration.workload_validation_db_metrics_config.port` |  `String` Specify the port on which your SAP HANA instance accepts queries. For the first or only tenant database instance, the port is `3NN15`, where `NN` is the instance number of the SAP HANA instance.  
`collection_configuration.workload_validation_db_metrics_frequency` | `Int` The collection frequency of the SAP HANA database metrics, in seconds, for Workload Manager evaluation. Default is `3600` seconds.  
  
Although you can update the collection frequency of the SAP HANA database metrics, we recommend that you use the default value. If you need to modify the default value, then add the `workload_validation_db_metrics_frequency` parameter under the `collection_configuration` section and provide the required value. Make sure that you don't set a collection frequency greater than `3600` seconds.  
  
## Validate the setup for Workload Manager evaluation metrics collection

You can validate if you have the correct Google Cloud setup for the collection of the Workload Manager evaluation metrics by running the agent's `status` command. This command is supported from version 3.7 of the agent.

To validate the Google Cloud setup, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance.
  2. Run the following command: 
         
         sudo /usr/bin/google_cloud_sap_agent status -f="workload_manager,sap_discovery"

If your Google Cloud setup for Workload Manager evaluation metrics collection is correct, then the output includes the following. Your configuration might have values other than the **`default`** ones.
         
         Agent Status:
                 ...
                 Systemd Service Enabled: True
                 Systemd Service Running: True
                 Cloud API Full Scopes: True
                 Configuration File: /etc/google-cloud-sap-agent/configuration.json
                 Configuration Valid: True
             ...
             ----------------------------------------------------------------------------
             System Discovery: Enabled
                 Status: Fully Functional
                 IAM Permissions: All granted
                 Configuration:
                     enable_discovery:                  true  (default)
                     enable_workload_discovery:         true  (default)
                     sap_instances_update_frequency:    60    (default)
                     system_discovery_update_frequency: 14400 (default)
             ----------------------------------------------------------------------------
             Workload Manager Evaluation: Enabled
                 Status: Fully Functional
                 IAM Permissions: All granted
                 Configuration:
                     collect_workload_validation_metrics:      true       (default)
                     config_target_environment:                PRODUCTION (default)
                     fetch_latest_config:                      true       (default)
                     workload_validation_db_metrics_frequency: 3600       (default)
                     workload_validation_metrics_frequency:    300        (default)
             ...
             

  3. If your output conveys that some setup is missing, then review the information provided in the preceding sections, perform the required actions, and then re-run the `status` command to re-validate the setup.



## View the collected metrics

To view the Workload Manager evaluation metrics that the agent collects, you can do the following:

  * See the agent's log file:

    1. Set the agent's log level to `DEBUG`:
           
           sudo /usr/bin/google_cloud_sap_agent configure -loglevel=debug

    2. After the agent restarts to effect the new log level, see the agent's log file:
           
           /var/log/google-cloud-sap-agent.log

    3. In the log file, look for entries that contain the following:
           
           workload.googleapis.com/sap/validation/

The following is an example that shows Workload Manager evaluation metrics in the agent's log file:
           
           {"level":"debug","timestamp":"2024-05-31T20:13:39.439Z",..."context":"WorkloadManagerMetrics",  
           **"metric":"workload.googleapis.com/sap/validation/system","value":1**}
           {"level":"debug","timestamp":"2024-05-31T20:13:39.439Z",..."context":"WorkloadManagerMetrics",  
           **"key":"instance_name","value":"n1-hana-sles15"**}
           {"level":"debug","timestamp":"2024-05-31T20:13:39.439Z",..."context":"WorkloadManagerMetrics",  
           **"key":"os","value":"sles-15-SP4"**}
           ...
           {"level":"debug","timestamp":"2024-05-31T20:13:39.439Z",..."context":"WorkloadManagerMetrics",  
           **"metric":"workload.googleapis.com/sap/validation/corosync","value":0**}
           ...

  * If your agent instance is configured to send logs to Cloud Logging, then you can [view the agent's logs in Cloud Logging](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#view_agent_logs_in_cloud_logging).

  * Create and run an evaluation for your SAP workload in Workload Manager. For more information, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

For information about the best practices that Workload Manager supports for evaluating SAP workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
