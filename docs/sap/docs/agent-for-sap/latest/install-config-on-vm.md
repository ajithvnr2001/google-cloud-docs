---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm/
title: Install and configure Google Cloud's Agent for SAP on a Compute Engine instance \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:49.602944+00:00
---

# Install and configure Google Cloud's Agent for SAP on a Compute Engine instance  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure Google Cloud's Agent for SAP on a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to install and configure **version 3.15 (latest)** of Google Cloud's Agent for SAP on a Compute Engine instance, including one based on the X4 or C3 series.

To install and configure the agent on a Bare Metal Solution server, see [Install Google Cloud's Agent for SAP on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms).

Google Cloud's Agent for SAP is required for SAP support of SAP systems running on Google Cloud, including SAP NetWeaver, SAP HANA, SAP ASE, SAP MaxDB, and others.

When you install Google Cloud's Agent for SAP on a Compute Engine instance, for SAP Host Agent metrics, the agent combines monitoring data from Cloud Monitoring and the Compute Engine APIs and provides that data to the SAP Host Agent.

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



For information about the operating systems supported by Google Cloud's Agent for SAP, see [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems).

## Installation overview

On Linux, you install Google Cloud's Agent for SAP by using standard operating system package management commands: on RHEL, the `yum` command; on SLES, the `zypper` command. The package management command completes the following tasks:

  * Downloads the latest version of Google Cloud's Agent for SAP.
  * Creates the agent as a Linux `systemd` service, named `google-cloud-sap-agent`.
  * Enables and starts the service, `google-cloud-sap-agent`.



On Windows, you install Google Cloud's Agent for SAP by using the GooGet package management command, `googet`. The package management command completes the following tasks:

  * Downloads the latest version of Google Cloud's Agent for SAP.
  * Creates a Windows service named `google-cloud-sap-agent` and a scheduled task that runs every minute to check if the service is still running and, if necessary, restart it.

**Warning:** Don't manually stop the Windows service or delete the scheduled task.



## Prerequisites for the agent

Before you install Google Cloud's Agent for SAP, you need to ensure that the following prerequisites are met.

#### Set the required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the Compute Engine instances that host your SAP workload: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Read the collected metrics from Cloud Monitoring: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * Write the collected metrics to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect metrics:

  * Collect the metrics from the host Compute Engine instance and write them to Cloud Monitoring and Workload Manager data warehouse: 
    * `compute.instances.get`
    * `compute.instances.list`
    * `monitoring.metricDescriptors.get`
    * `monitoring.metricDescriptors.list`
    * `monitoring.timeSeries.create`
    * `workloadmanager.insights.writer`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Enable access to Google Cloud APIs

Compute Engine recommends configuring your compute instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you do limit access to the Cloud APIs, then Google Cloud's Agent for SAP requires the following minimum Cloud API access scopes on the host Compute Engine instance:

  * **Cloud Platform** : **Enabled**
  * **Compute Engine** : **Read Only**
  * **Stackdriver Monitoring API** : **Read Only**



If you are running SAP applications on a compute instance that does not have an external IP address, then you need to enable [Private Google Access ](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet of the compute instance so that Google Cloud's Agent for SAP can access Google APIs and services. To enable Private Google Access on a subnet, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## Install the agent

To install Google Cloud's Agent for SAP on your Compute Engine instance, select your operating system, and then complete the following steps.

**Note:** To install the agent on a fleet of VMs globally or within a specific zone, you can use VM Extension Manager. For information about how to create a VM extension policy to install and manage the agent on your VM fleet, see [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet).

###  Linux 

To install the agent on a Compute Engine instance, follow these steps:

  1. Establish an SSH connection to your compute instance.
  2. In your terminal, install the agent by running the command that is specific to your operating system: 
     * (Recommended) To install version 3.15 (latest) of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

     * To install a specific version of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent).

For information about downgrading the agent to a specific version, see [ Downgrade Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-downgrade).




###  Windows 

To install the agent on a Compute Engine instance, follow these steps:

  1. Use RDP to connect to the compute instance.
  2. As an administrator, run the following command from PowerShell: 
         
         googet addrepo google-cloud-sap-agent https://packages.cloud.google.com/yuck/repos/google-cloud-sap-agent-windows
         googet install google-cloud-sap-agent




After you install Google Cloud's Agent for SAP and the SAP Host Agent, validate the installation of Google Cloud's Agent for SAP, as described in Validate your installation of the agent.

## Validate your installation of the agent

To verify that the agent is running, select your operating system, and then follow the steps:

###  Linux 

  1. Establish an SSH connection with your Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         

  3. On SLES images, to ensure you're using the latest version of Google Cloud's Agent for SAP, run the following commands.

**Note:** Google Cloud's Agent for SAP is bundled with all "for SAP" images of RHEL, and 15 SP4 and later versions of SLES. Because the SLES for SAP images are updated once a quarter, it is possible that the agent version bundled with those OS images isn't the latest one. The following commands update your agent instance to the latest version provided by Google Cloud.
         
         sudo zypper remove google-cloud-sap-agent
         sudo zypper addrepo -p 98 --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-\$basearch google-cloud-sap-agent
         sudo zypper install google-cloud-sap-agent




###  Windows 

  1. Use RDP to connect to the Compute Engine instance.

  2. As an administrator, run the following command from PowerShell: 
         
         $(Get-Service -Name 'google-cloud-sap-agent' -ErrorAction Ignore).Status

If the agent is running, then the status shows `Running`.



If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Configure Google Cloud's Agent for SAP on Linux

After you install Google Cloud's Agent for SAP, optionally, you can enable other features of the agent by performing the following configurations. By default, the collection of [SAP Host Agent metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_host_agent_metrics) and [Workload Manager evaluation metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#wlm_evaluation_metrics) is enabled.

The following features are supported only on Linux. They are not supported on Windows.

  * [Configure Process Monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring)
  * [Configure Workload Manager evaluation metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation)
  * [Configure SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring).
  * [Configure Backint based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery).
  * [Back up and recover SAP HANA by using a disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery).



### Default configuration file

The following snippet is an example of the default configuration of version 3.15 (latest) of Google Cloud's Agent for SAP:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": false,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
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

To view feature-specific example configuration files, see the configuration guide for that feature.

### Configuration parameters

The following table describes the configuration parameters of Google Cloud's Agent for SAP that is running on a Compute Engine instance, including the parameters related to the collection of metrics. For information about the configuration parameters related to the Backint feature of the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#configuration_parameters).

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
`cloud_properties.instance_name` |  `String` Specify the name of your Compute Engine instance. The agent automatically detects this upon installation.  
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
`hana_monitoring_configuration.enabled` |  `Boolean` Optional. To enable Google Cloud's Agent for SAP to collect the SAP HANA monitoring metrics, specify `true`. The default value is `false`. The following child parameters are applicable only when you specify `hana_monitoring_configuration.enabled: true`.   
`hana_monitoring_configuration.sample_interval_sec` |  `Int` Optional. Specify the sample interval, in seconds, which determines the frequency at which Google Cloud's Agent for SAP queries your SAP HANA instances to collect the SAP HANA monitoring metrics. The default value is 300 seconds. For each query defined in the configuration file of Google Cloud's Agent for SAP, you can overwrite the global sample interval by specifying the required interval to the parameter `sample_interval_sec`. Sample intervals must be 5 seconds or longer.  
`hana_monitoring_configuration.query_timeout_sec` |  `Int` Optional. Specify the timeout for each query made to the SAP HANA instances. The default value is 300 seconds.  
`hana_monitoring_configuration.execution_threads` |  `Int` Optional. Specify the number of threads used to send queries to the SAP HANA instances. Each query runs on its own thread. The default value is 10.  
`hana_monitoring_configuration.send_query_response_time` |  `Boolean` Optional. Specify `true` to have the agent capture the response time for every SAP HANA monitoring query defined in the agent's configuration file.  
`hana_monitoring_configuration.hana_instances.name` |  `String` Specify the name identifier for your SAP HANA instance.  
`hana_monitoring_configuration.hana_instances.sid` |  `String` Specify the SID of your SAP HANA instance. This string is added as a label to all the metrics resulting from querying your SAP HANA instances.  
`hana_monitoring_configuration.hana_instances.host` |  `String` Specify the identifier for the machine, either local or remote, that hosts your SAP HANA instance. The following are the supported values:

  * If the host is a local machine, then specify the string `localhost` or the localhost loopback IP address, like `127.0.0.1`.
  * If the host is a remote machine, then specify its internal or external IP address.

  
`hana_monitoring_configuration.hana_instances.port` |  `String` Specify the port on which your SAP HANA instance accepts queries. For the first or only tenant database instance, the port is `3NN15`, where `NN` is the instance number of the SAP HANA instance.  
`hana_monitoring_configuration.hana_instances.user` |  `String` Specify the user account that is used to query the SAP HANA instance. Make sure that this user has the privilege to read the monitoring views in your SAP HANA database. If this privilege is not granted, then the SAP HANA monitoring metrics related to the monitoring views contain no data.  
`hana_monitoring_configuration.hana_instances.password` |  `String` Optional. Specify the password, as plain text, that authenticates the user account for querying the SAP HANA instance. For authentication, you must specify one of the following:

  * The plain text password to the parameter `password`.
  * (Recommended) If you use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the password as a secret, then you must specify the corresponding secret name to the parameter `secret_name`.
  * (Recommended) An [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) to the parameter `hdbuserstore_key`.

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `password` parameter, which is preferred over the `secret_name` parameter. We recommend that you set only one authentication option in your configuration file.  
`hana_monitoring_configuration.hana_instances.secret_name` |  `String` Optional. Specify the name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) that stores the user account's password. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `password` parameter, which is preferred over the `secret_name` parameter. We recommend that you set only one authentication option in your configuration file.  
`hana_monitoring_configuration.hana_instances.hdbuserstore_key` |  `String` To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `hdbuserstore_key`, then you can skip specifying the `host` and `port` parameters.  
`hana_monitoring_configuration.hana_instances.is_local` |  `Boolean` For monitoring HA systems, specify `true` to tell the agent that the defined SAP HANA instance is hosted on the same Compute Engine instance as the agent. This then makes the agent check at runtime if the defined SAP HANA instance is the primary or the secondary node in that HA system. This awareness is required by the agent to run the SAP HANA monitoring queries on the SAP HANA instance type that you specify for the `queries.run_on` parameter. The default value for this parameter is `false`, which makes the agent run all the enabled SAP HANA monitoring queries on the corresponding SAP HANA instance. For more information, see [Monitoring for multi-tenant and HA systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#monitoring_for_multi-tenant_and_ha_systems). This parameter is supported from version 3.7 of the agent.  
`hana_monitoring_configuration.hana_instances.instance_num` |  `String` Specify the instance number that you've set for your SAP HANA instance. This information is required for the agent to discover your SAP HANA instance. This parameter is supported from version 3.7 of the agent.  
`hana_monitoring_configuration.hana_instances.queries_to_run.run_all` |  `Boolean` Optional. Specify `true` to run all the SAP HANA monitoring queries, default and custom, that are enabled in the agent's configuration file on the specified SAP HANA instance. The default value is `false`.  
`hana_monitoring_configuration.hana_instances.queries_to_run.query_name` |  `String` Optional. Specify the queries that you want to run on the specified SAP HANA instance. If you're running a multi-tenant SAP HANA database, then you can set up tenant specific monitoring by using this configuration parameter. In the following example configuration, two queries are run on `HANA_TENANT_1` and all queries defined in the configuration are run on `HANA_TENANT_2`:
    
    
        "hana_instances": [
          {
            "name": "HANA_TENANT_1,
            "queries_to_run": {
              "query_name": ["QUERY_NAME_1", "QUERY_NAME_2"]
            }
          },
          {
            "name": "HANA_TENANT_2,
            "queries_to_run": {
              "run_all": true
            }
          }
          ...
        ]  
  
`hana_monitoring_configuration.hana_instances.enable_ssl` |  `Boolean` Optional. Specifies whether or not SSL is enabled in your SAP HANA instance. The default value is `false`.  
`hana_monitoring_configuration.hana_instances.host_name_in_certificate` |  `String` If you specify `enable_ssl: true` for an SAP HANA instance, then you must specify the hostname that is set in the SSL certificate.  
`hana_monitoring_configuration.hana_instances.tls_root_ca_file` |  `String` If you specify `enable_ssl: true` for an SAP HANA instance, then you must specify the path for your security certificate.  
`hana_monitoring_configuration.queries.enabled` |  `Boolean` Optional. To enable a SQL query for all your SAP HANA instances, specify the value `true` for the parameter `enabled` for that SQL query.  
`hana_monitoring_configuration.queries.name` |  `String` If you have defined custom queries in your configuration file, then you must specify a unique name for each custom query. The query name must be unique because it is used to build the metric's default URL in Monitoring.  
`hana_monitoring_configuration.queries.run_on` |  `String` Optional. Specify this parameter if you're monitoring an SAP HANA HA system and want to run the SAP HANA monitoring queries on either the primary or the secondary node. Supported values: `PRIMARY`, `SECONDARY`, `ALL`. When you specify the value `ALL`, the agent runs the SAP HANA monitoring queries on both the primary and secondary nodes in your HA cluster. This parameter is supported from version 3.7 of the agent. Also, to run the queries on the secondary node, make sure that your HA system is deployed with the [Active/Active (Read Enabled)](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html) configuration.   
`hana_monitoring_configuration.queries.sql` |  `String` Specify the SQL statement that the agent issues to your SAP HANA instances. The SQL statement must conform to the SQL syntax defined by SAP in [SAP HANA SQL and System Views Reference](https://help.sap.com/viewer/4fe29514fd584807ac9f2a04f6754767/2.0.02).   
`hana_monitoring_configuration.queries.sample_interval_sec` |  `Int` Optional. Specify the sample interval for the SQL query. This overrides the global sample interval. The value must be 5 seconds or longer.  
`hana_monitoring_configuration.queries.columns.name` |  `String` Specify a name that uniquely identifies each column. The column name must be unique because it is used to build the metric's default URL in Monitoring.  
`hana_monitoring_configuration.queries.columns.metric_type` |  `String` For handling by Monitoring, specify one of the following metric types: `METRIC_LABEL`, `METRIC_GAUGE`, or `METRIC_CUMULATIVE`. Metrics of type `METRIC_LABEL` are appended as labels to all the `METRIC_GAUGE` and `METRIC_CUMULATIVE` metrics that are sent to Monitoring.  
`hana_monitoring_configuration.queries.columns.value_type` |  `String` For handling by Monitoring, specify a data type that is supported by the metric type. The supported data types are as follows: `VALUE_BOOL`, `VALUE_INT64`, `VALUE_STRING`, or `VALUE_DOUBLE`. For more information, see [Supported combination](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#kind-type-combos).  
`hana_monitoring_configuration.queries.columns.name_override` |  `String` Optional. For handling by Monitoring, specify the path that you want to show in the metric URL instead of the query and column names. For example:

  * Metric's default URL: `workload.googleapis.com/sap/hanamonitoring/QUERY_NAME/COLUMN_NAME`
  * Metric URL using custom path: `workload.googleapis.com/sap/hanamonitoring/CUSTOM_PATH`

  
  
## Troubleshooting

For information about diagnosing and resolving issues that you might encounter when you install and configure Google Cloud's Agent for SAP, see [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

## Get support

If you need help resolving problems with Google Cloud's Agent for SAP, then collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
