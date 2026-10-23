---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap/
title: Set up the agent for SAP workloads \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:01.074130+00:00
---

# Set up the agent for SAP workloads  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Set up the agent for SAP workloads Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager for SAP solutions uses [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning) to detect and collect metadata for evaluating your SAP system configurations. The Agent for SAP, along with the SAP Host Agent, are required on all VM instances that run SAP systems for support and monitoring of your SAP systems running on Google Cloud, including SAP NetWeaver, SAP HANA, SAP ASE, and SAP MaxDB.

**Note:** The collection of Workload Manager evaluation metrics by Google Cloud's Agent for SAP is supported only on Linux. It is not supported on Windows.

## Before you begin

Before you install and configure Google Cloud's Agent for SAP, you need to make sure that the following prerequisites are met:

  * You've deployed an SAP workload on one or more compute instances.
  * You've reviewed the [supported regions](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) where you can create Workload Manager evaluations.
  * Your administrator has granted you [IAM roles required to create and run Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).
  * You've granted the required IAM roles for the agent.
  * You've enabled access to Cloud APIs.



### Required IAM roles for the agent

Agent for SAP uses the service account attached to the compute instance for authentication and to access Google Cloud resources.

To improve security, we recommend that you use a [single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) rather than using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

To ensure that the service account has the necessary permissions to let Agent for SAP authenticate with Google Cloud and access Google Cloud resources, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the compute instance: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write data to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 
  * Send agent logs to Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 
  * If you are using Secret Manager to store the password to connect with the SAP workload: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable access to Cloud APIs

Compute Engine recommends configuring your instances to allow all access scopes to all Cloud APIs. To control access to Google Cloud resources, use only the IAM permissions of the instance service account. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs, then the Agent for SAP requires at minimum the following Cloud APIs access scopes on the host compute instance:
    
    
    https://www.googleapis.com/auth/cloud-platform
    

For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

If you're running SAP applications on a compute instance that doesn't have an external IP address, then you need to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the instance's subnet so that Agent for SAP can access the Google APIs and services. For information about how to enable Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## Install and configure the agent by using package manager

This section shows you how to install the Agent for SAP on your compute instance, and configure it to connect with your SAP workload, by using a package manager.

If you want to install and configure the agent on a fleet of VMs, then you can use a VM Extension Manager policy instead. For more information, see Install and manage the agent on a fleet of VMs by using VM Extension Manager.

### Install the agent

If not already done, then install Google Cloud's Agent for SAP on all compute instances that run your SAP workload:

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




### Configure the collection of Workload Manager evaluation metrics

After you install Agent for SAP, you need to configure the agent for the collection of the Workload Manager evaluation metrics.

To configure Google Cloud's Agent for SAP, complete the following steps:

  1. To let the agent collect the [Workload Manager evaluation metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#wlm_evaluation_metrics):
         
         sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -enable

  2. Optional: To enable the collection of "SAP HANA Insights" and "SAP HANA Security Best Practices" metrics in Workload Manager, add the `workload_validation_db_metrics_config` section after `collect_workload_validation_metrics` in the agent's configuration file, and then specify the following parameters:

     * `hana_db_user`: specify the user account that is used to query the SAP HANA instance.
     * `hostname`: specify the identifier for the machine, either local or remote, that hosts your SAP HANA instance.
     * `port`: specify the port on which your SAP HANA instance accepts queries.
     * `hana_db_password_secret_name`: specify the name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) that stores the user account's password

As an alternative to the secret, you can use the `hdbuserstore_key` configuration parameter.

     * `hdbuserstore_key`: specify the [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) that authenticates the user you specified for `hana_db_user`

If you specify `hdbuserstore_key`, then you skip specifying the `hostname` and `port` parameters.

For information about these parameters, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

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

  3. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent

After the agent successfully restarts, the agent starts sending the Workload Manager evaluation metrics to Workload Manager.




## Install and manage the agent on a fleet of VMs by using VM Extension Manager

This section shows you how to install and manage the Agent for SAP on a fleet of VMs by using VM Extension Manager.

VM Extension Manager policy lets you perform tasks such as the following:

  * Fleet-wide installation: Install Agent for SAP on the following: 
    * All VMs in your Google Cloud project, or a subset of VMs identified by labels.
    * All VMs within a zone, or a subset of VMs identified by labels.
  * Configuration management: Apply a custom configuration to the agent on all VMs managed by a policy.



### Set up VM Extension Manager

To set up VM Extension Manager, complete the following steps:

  * In the VM Extension Manager documentation, review the [Before you begin](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#byb) section.
  * Set up the IAM roles needed to create and manage VM Extension Manager policies. For more information, see the following:

    * [Create VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#create-permissions)
    * [Update VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-iam-permissions)
    * [Delete VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#delete-iam-permissions)
    * [List and describe VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-iam-permissions)



### Install and configure the agent on a fleet of VMs

To install the latest version of Agent for SAP on your VM fleet by using a VM Extension Manager policy, see the appropriate section:

  * Install and configure the agent on VMs within your Google Cloud project
  * Install and configure the agent on VMs within a specific zone



#### Install and configure the agent on VMs within your Google Cloud project

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

For information about the configuration parameters supported by the agent for your SAP workload, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

     4. Click **Done**.

     5. In the **Rollout** field, select the rollout plan option that you want to use: **Slow rollout** (recommended) or **Fast rollout**.

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
    * For information about the configuration parameters supported by the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. For more information, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#policy-priority-resolution).




#### Install and configure the agent on a fleet of VMs within a specific zone

To install the latest version of Agent for SAP on your VM fleet within a specific zone by using a VM Extension Manager policy, complete the following steps:

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

     3. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent for your SAP workload, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

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
        --config-from-file=google-cloud-sap-extension=CONFIG_FILE_PATH \
        [--description="DESCRIPTION" \]
        [--inclusion-labels=KEY_1=VALUE_1 \]
        [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
        [--priority=PRIORITY]

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.

The command fails if a policy with the specified name already exists in the zone.

  * `ZONE`: the zone where you want to apply this policy.

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for SAP to connect with your SAP workload.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-sap-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent for your SAP workload, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

  * `DESCRIPTION`: an optional description for the policy.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the specified zone.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`.




**Example:**

The following command creates a policy named `test-agent-policy` in the Google Cloud project named `test-project`, which installs the latest version of Agent for Compute Workloads on all VMs deployed in the zone `us-centrail-f`. The configuration specified in the `agent-config.json` is applied to the agent.
    
    
    gcloud compute zone-vm-extension-policies create test-agent-policy  \
        --project=test-project \
        --zone=us-central1-f \
        --extensions=google-cloud-sap-extension \
        --config-from-file=google-cloud-sap-extension="/usr/agent-config.json"

### Manage the agent on a fleet of VMs

To change how a VM Extension Manager policy manages Agent for SAP, update the policy. When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, then Agent for SAP might be installed on new VMs or uninstalled from existing VMs based on whether the VMs match the updated labels.

The following sections show how to manage Agent for SAP to do the following:

  * Modify agent configuration on a fleet of VMs
  * Update a global policy to include new zones
  * Update a global policy to exclude zones



#### Modify agent configuration on a fleet of VMs

To modify the configuration of Agent for SAP instances that you've installed on your VM fleet by using a VM Extension Manager policy, you must edit that policy.

To modify agent configuration on your VM fleet, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. To update a zonal policy, go to the **Zonal policies** tab.

  3. Click the policy that you want to modify.

  4. In the **Extension policy details** page, click **Edit**.

  5. In the **Manage extensions** section, do the following:

     1. Select **Google Cloud's extension for SAP**.
     2. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

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
    * For information about the configuration parameters supported by the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).
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
    * For information about the configuration parameters supported by the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).
  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the project.
  * `PRIORITY_NUMBER`: the priority that you want to set for your policy. You can specify an integer from `0` to `65535`.

  * `DESCRIPTION`: a description of the VM extension policy.




#### Update a global policy to include new zones

When you create VMs in a new zone after you've created and rolled out a global policy, VM Extension Manager does not automatically apply the policy to the VMs in the new zones. To include the VMs in new zones, you must restart the global policy rollout.

To restart a global policy rollout, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/update) command and supply the `--rollout-entry-uuid` option as follows:
        
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



#### Update a global policy to exclude zones

To update a global policy to exclude zones, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/update) command and supply a custom rollout plan that specifies the zones in which to apply the policy:
        
        gcloud compute global-vm-extension-policies update POLICY_NAME \
            --project=PROJECT_ID \
            --extensions=google-cloud-sap-extension  \
            --rollout-custom-plan=projects/PROJECT_ID/locations/global/rolloutPlans/NEW_CUSTOM_PLAN_NAME \
            --rollout-retry-uuid=UUID
        

Replace the following:

    * `NEW_CUSTOM_PLAN_NAME`: the name of the new custom rollout plan that identifies the zones in which to apply the policy. For information about creating custom rollout plans, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * `UUID`: a universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Uninstall agent from a VM fleet

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

To delete a zonal VM Extension Manager policy, use the [`gcloud compute zone-vm-extension-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/zone-vm-extension-policies/delete) command:
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the zonal policy that you want to delete.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  Global 

To delete a global VM Extension Manager policy, use the [`gcloud compute global-vm-extension-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/delete) command:
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN_OPTION

Replace the following:

  * `POLICY_NAME`: the name of the zonal policy that you want to delete.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ROLLOUT_PLAN_OPTION`: the rollout option that you want to apply to your global policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`.

    * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.



## Verify the agent version

Google Cloud recommends that you install the latest version of Agent for SAP for accurate evaluation of your SAP workloads because periodic releases of the Agent for SAP might add or change metrics that are used for the evaluation.

To ensure that you have the latest version of Google Cloud's Agent for SAP, you need to check for updates periodically and update the agent.

### Check for updates

Select your operating system, and then follow these steps:

### RHEL

  1. Establish an SSH connection with your instance.
  2. Run the following command: 
         
         sudo yum check-update google-cloud-sap-agent




### SLES

  1. Establish an SSH connection with your instance.
  2. Run the following command: 
         
         sudo zypper list-updates -r google-cloud-sap-agent




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



## Example configuration file

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




For information about the configuration parameters that are supported by Agent for SAP, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

## What's next

  * Learn more [about workload evaluations](https://docs.cloud.google.com/workload-manager/docs/about-evaluations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
