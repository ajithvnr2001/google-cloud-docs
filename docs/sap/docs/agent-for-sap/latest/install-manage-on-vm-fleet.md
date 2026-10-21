---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet/
title: Install and manage Agent for SAP on a fleet of VMs \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:49.358531+00:00
---

# Install and manage Agent for SAP on a fleet of VMs  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and manage Agent for SAP on a fleet of VMs Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to install and manage **version 3.15 (latest)** of Google Cloud's Agent for SAP on a fleet of Compute Engine VMs globally or within a specific zone by using [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

VM Extension Manager policy lets you perform tasks such as the following:

  * Fleet-wide installation: Install Google Cloud's Agent for SAP on the following: 
    * All VMs in your Google Cloud project, or a subset of VMs identified by labels.
    * All VMs within a zone, or a subset of VMs identified by labels.
  * Configuration management: Apply a custom configuration to the agent on all VMs managed by a policy.



To install and configure the agent on a Compute Engine instance by using a package manager, see [Install Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm).

## Before you begin

Before you install Google Cloud's Agent for SAP on your VM fleet by using VM Extension Manager, make sure that the following prerequisites are met:

  * The Linux or Windows operating system (OS) version running on your VM fleet satisfies the following criteria: 
    * The OS version is certified by SAP for use with your target SAP application or database. For more information, see [OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support) and [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support).
    * The OS version is compatible with VM Extension Manager. For information about the OS versions that VM Extension Manager supports, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-os).
  * You've set up VM Extension Manager.
  * You've granted the required IAM roles for the agent.
  * You've enabled access to Google Cloud APIs.



### Set up VM Extension Manager

To set up VM Extension Manager, complete the following steps:

  * In the VM Extension Manager documentation, review the [Before you begin](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#byb) section.
  * Set up the IAM roles needed to create and manage VM Extension Manager policies. For more information, see the following:

    * [Create VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#create-permissions)
    * [Update VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-iam-permissions)
    * [Delete VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#delete-iam-permissions)
    * [List and describe VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-iam-permissions)



### Required IAM roles for the agent

To access Google Cloud resources, the Agent for SAP uses the service account attached to the VM hosting the agent.

To ensure that this service account has the necessary permissions to let Google Cloud's Agent for SAP send metrics to the SAP Host Agent, ask your administrator to grant the service account the following IAM roles on your project:

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors.

  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer): to collect metrics from the Compute Engine instance that hosts your SAP system.
  * (Recommended) [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter): to send agent logs to Cloud Logging
  * [Monitoring Viewer (`roles/monitoring.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) to view the metrics collected in Cloud Monitoring.
  * [Workload Manager Insights Writer (`roles/workloadmanager.insightWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter): to write the collected metrics to Workload Manager data warehouse.



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP send metrics to the SAP Host Agent. Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

### Enable access to Google Cloud APIs

Compute Engine recommends configuring your compute instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs, then Google Cloud's Agent for SAP requires the following minimum access scopes on the host Compute Engine instance:

  * **Cloud Platform** : **Enabled**
  * **Compute Engine** : **Read Only**
  * **Stackdriver Monitoring API** : **Read Only**



If you are running SAP applications on a compute instance that does not have an external IP address, then you need to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet of the compute instance so that Google Cloud's Agent for SAP can access Google APIs and services. To enable Private Google Access on a subnet, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## Install and configure the agent on a fleet of VMs

To install the latest version of Google Cloud's Agent for SAP on your VM fleet by using a VM Extension Manager policy, see the appropriate section:

  * Install and configure the agent on VMs within your Google Cloud project
  * Install and configure the agent on VMs within a specific zone



### Install and configure the agent on VMs within your Google Cloud project

To install the agent on all VMs in your Google Cloud project, or a subset of VMs identified by labels, by using a VM Extension Manager policy, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.

  3. In the **Name** field, enter a name for the policy.

  4. Optional: In the **Description** field, enter a description for the policy.

  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.

  6. In the **Scope** section, select **Global rollout**.

  7. In the **Manage extensions** section, click **Add extension** and then do the following:

     1. From the **Extension** list, select **Google Cloud's extension for SAP**.
     2. Leave the **Version** field selection as is.

This directs the policy to install the latest version of Google Cloud's Agent for SAP on your VM fleet.

     3. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent for your SAP workload, see Configuration parameters.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

     4. Click **Done**.

     5. In the **Rollout** field, select the rollout plan option that you want to use: **Slow rollout** (recommended) or **Fast rollout**.

For information about rollout plans, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

  8. Optional: To limit the policy rollout to the required VMs, in the **Target VM instances** , do the following:

     1. Click **Add labels** and include the labels that identify the required VMs.
     2. Click **Done**.
  9. Click **Create**.




###  gcloud 

In your terminal of Cloud Shell, run the [gcloud compute global-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
        --project=PROJECT_ID \
        --extensions=google-cloud-sap-extension  \
        --rollout-predefined-plan=ROLLOUT_PLAN_OPTION \
        [--description="<var>DESCRIPTION</var>" \]
        [--inclusion-labels=KEY1=VALUE1,KEY2=VALUE2 \]
        [--config-from-file=google-cloud-sap-extension="CONFIG_FILE_PATH" \]
        [--priority=PRIORITY]
    

Replace the following:

  * `POLICY_NAME`: a unique name for the VM extension policy.
  * `PROJECT_ID`: the project ID of the Google Cloud project for which you're creating the policy
  * `ROLLOUT_PLAN_OPTION`: the rollout option that you want to apply to your global policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`.

    * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.
  * `DESCRIPTION`: an optional description for the policy.

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for SAP.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-sap-extension="CONFIG"`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. For more information, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#policy-priority-resolution).




### Install and configure the agent on VMs within a specific zone

To install the agent on VMs within a specific zone by using a VM Extension Manager policy, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.

  3. In the **Name** field, enter a name for the policy.

  4. Optional: In the **Description** field, enter a description for the policy.

  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.

  6. In the **Scope** section, select **Zonal rollout** and then select the **Region** and **Zone** where you want to apply this policy.

  7. In the **Manage extensions** section, click **Add extension** and then do the following:

     1. From the **Extension** list, select **Google Cloud's extension for SAP**.
     2. Leave the **Version** field blank.

This directs the policy to install the latest version of Google Cloud's Agent for SAP.

     3. Optional: In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent, see Configuration parameters.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

     4. Click **Done**.

  8. Optional: To limit the policy rollout to the required VMs, in the **Target VM instances** , do the following:

     1. Click **Add labels** and include the labels that identify the required VMs.
     2. Click **Done**.
  9. Click **Create**.




###  gcloud 

In your terminal or Cloud Shell, run the [gcloud compute zone-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create) command:
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
       --zone=ZONE \
       --extensions=google-cloud-sap-extension \
       [--description="DESCRIPTION" \]
       [--config-from-file=google-cloud-sap-extension=CONFIG_FILE_PATH \]
       [--inclusion-labels=KEY_1=VALUE_1 \]
       [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
       [--priority=PRIORITY]

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.

The command fails if a policy with the specified name already exists in the zone.

  * `ZONE`: the zone where you want to apply this policy.

  * `DESCRIPTION`: an optional description for the policy.

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for SAP.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-sap-extension="CONFIG"`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the specified zone.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. For more information, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#policy-priority-resolution).




**Example:**

The following command creates a policy named `test-sap-agent-policy` in the Google Cloud project named `test-project`, which installs the latest version of Google Cloud's Agent for SAP on all VMs deployed in the zone `us-centrail-f`. The configuration specified in the `agent-config.json` is applied to the agent.
    
    
    gcloud compute zone-vm-extension-policies create test-sap-agent-policy  \
       --project=test-project \
       --zone=us-central1-f \
       --extensions=google-cloud-sap-extension \
       --config-from-file=google-cloud-sap-extension="/usr/agent-config.json"

### Default configuration file

The following snippet is an example of the default configuration of version 3.15 (latest) of Google Cloud's Agent for SAP:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": ,
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

The following table describes the configuration parameters of Google Cloud's Agent for SAP that is running on a Compute Engine VM, including the parameters related to the collection of metrics. For information about the configuration parameters related to the Backint feature of the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#configuration_parameters).

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

  
  
## Manage the agent on a fleet of VMs

To change how a VM Extension Manager policy manages Google Cloud's Agent for SAP, update the policy. When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, then Google Cloud's Agent for SAP might be installed on new VMs or uninstalled from existing VMs based on whether the VMs match the updated labels.

The following sections show how to manage Google Cloud's Agent for SAP to do the following:

  * Modify agent configuration on a fleet of VMs
  * Update a global policy to include new zones
  * Update a global policy to exclude zones



### Modify agent configuration on a fleet of VMs

To modify the configuration of Agent for SAP instances that you've installed on your VM fleet by using a VM Extension Manager policy, you must edit that policy.

To modify agent configuration on your VM fleet, complete the following steps:

###  Console 

To update a zonal policy, complete the following steps. To update a global policy, see the `gcloud` tab.

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click the policy that you want to modify.

  3. In the **Extension policy details** page, click **Edit**.

  4. In the **Manage extensions** section, toggle **Google Cloud's extension for SAP**.

  5. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent, see Configuration parameters.

  6. Click **Done**.

  7. Click **Save**.




###  gcloud 

###  Zonal 

To modify the configuration of Agent for SAP on VMs within a specific zone, run the [`gcloud compute zone-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To modify agent configuration:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
      --zone=ZONE \
      --extensions=google-cloud-sap-extension \
      --config-from-file=google-cloud-sap-extension="CONFIG_FILE_PATH" \
      [--inclusion-labels=KEY_1=VALUE_1 \]
      [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
      [--priority=PRIORITY_NUMBER \]
      [--description="DESCRIPTION"]

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to modify.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for SAP.

    * You can also provide the agent configuration as an inline string by using the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-sap-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters.
  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the specified zone.
  * `PRIORITY_NUMBER`: the priority that you want to set for your policy. You can specify an integer from `0` to `65535`.

  * `DESCRIPTION`: a description of the VM extension policy.




###  Global 

To modify the configuration of Agent for SAP on VMs in your Google Cloud project, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To modify agent configuration:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=google-cloud-sap-extension \
      --rollout-predefined-plan=ROLLOUT_PLAN_OPTION \
      --config-from-file=google-cloud-sap-extension="CONFIG_FILE_PATH" \
      [--inclusion-labels=KEY_1=VALUE_1 \]
      [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
      [--priority=PRIORITY_NUMBER \]
      [--description="DESCRIPTION"]

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to modify.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ROLLOUT_PLAN_OPTION`: the rollout option that you want to apply to your global policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`.

    * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.
  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for SAP.

    * You can also provide the agent configuration as an inline string by using the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-sap-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters.
  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the project.
  * `PRIORITY_NUMBER`: the priority that you want to set for your policy. You can specify an integer from `0` to `65535`.

  * `DESCRIPTION`: a description of the VM extension policy.




### Update a global policy to include new zones

When you create VMs in a new zone after you've created and rolled out a global policy, VM Extension Manager does not automatically apply the policy to the VMs in the new zones. To include the VMs in new zones, you must restart the global policy rollout.

To restart a global policy rollout, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command and supply the `--rollout-entry-uuid` option as follows:
        
        gcloud compute global-vm-extension-policies update POLICY_NAME \
            --project=PROJECT_ID \
            --extensions=google-cloud-sap-extension  \
            --rollout-predefined-plan=ROLLOUT_PLAN_OPTION \
            --config-from-file=google-cloud-sap-extension="CONFIG_FILE_PATH" \
            --rollout-retry-uuid=UUID
        

Replace the following:

    * `UUID`: a universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).
    * `ROLLOUT_PLAN_OPTION`: the rollout option that you want to apply to your global policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`.

      * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
      * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.



### Update a global policy to exclude zones

To update a global policy to exclude zones, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command and supply a custom rollout plan that specifies the zones in which to apply the policy:
        
        gcloud compute global-vm-extension-policies update POLICY_NAME \
            --project=PROJECT_ID \
            --extensions=google-cloud-sap-extension  \
            --rollout-custom-plan=projects/PROJECT_ID/locations/global/rolloutPlans/NEW_CUSTOM_PLAN_NAME \
            --rollout-retry-uuid=UUID
        

Replace the following:

    * `NEW_CUSTOM_PLAN_NAME`: the name of the new custom rollout plan that identifies the zones in which to apply the policy. For information about creating custom rollout plans, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * `UUID`: a universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



## Uninstall agent from a VM fleet

To uninstall Agent for SAP from your VM fleet, you must delete the VM Extension Manager policy that manages the VM fleet.

While deleting a policy, if another active, lower-priority policy applies to a VM and declares the Agent for SAP, then the agent remains installed on that VM based on the lower-priority policy.

VM Extension Manager removes the agent from all accessible VMs within one minute of policy deletion. If a VM is inaccessible because the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is removed or the VM is deleted, then VM Extension Manager skips deletion of the Agent for SAP. If such a VM becomes available again, then VM Extension Manager removes the Agent for SAP at that time.

To uninstall Agent for SAP from your VM fleet, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click the policy that manages the Agent for SAP on your VM fleet.

  3. In the **Extension policy details** page, click **Delete** and confirm the deletion.




###  gcloud 

###  Zonal 

To delete a zonal VM Extension Manager policy, use the [`gcloud compute zone-vm-extension-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/delete) command:
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the zonal policy that you want to delete.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  Global 

To delete a global VM Extension Manager policy, use the [`gcloud compute global-vm-extension-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete)) command:
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN_OPTION

Replace the following:

  * `POLICY_NAME`: the name of the zonal policy that you want to delete.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ROLLOUT_PLAN_OPTION`: the rollout option that you want to apply to your global policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`.

    * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.



## Troubleshooting

For information about diagnosing and resolving issues that you might encounter when you install and configure Google Cloud's Agent for SAP, see [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

## Get support

If you need help resolving problems with Google Cloud's Agent for SAP, then collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
