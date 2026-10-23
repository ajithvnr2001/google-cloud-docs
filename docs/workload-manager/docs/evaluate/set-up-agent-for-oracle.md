---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle/
title: Set up the agent for Oracle workloads \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:59.539044+00:00
---

# Set up the agent for Oracle workloads  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Set up the agent for Oracle workloads Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to install, configure, and verify Agent for Compute Workloads on Compute Engine instances that run Oracle Database workloads.

The agent collects various Oracle metrics by querying Oracle Database performance views (such as `V$DATABASE`, `V$INSTANCE`, and `V$DATAGUARD_STATS`) and data dictionary views (such as `DBA_DATA_FILES` and `DBA_FREE_SPACE`). These metrics are then sent to Cloud Monitoring where they can be visualized and analyzed. See Supported metrics.

**Note:** You cannot use Agent for Compute Workloads to monitor Oracle workloads running on Compute Engine bare metal instances, such as X4.

## Before you begin

Before you install Agent for Compute Workloads to monitor your Oracle Database workloads, make sure that the following prerequisites are met:

  * Create a Compute Engine instance if you don't already have one. Configure [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) to `cloud-platform`.

  * [Set up root access on the Compute Engine instance](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

  * Review system requirements.

  * Grant IAM roles to the service account.

  * Enable connectivity to Google Cloud API endpoints, either through public network access or private network access.

  * If you want to enable metric collection, then [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) in Secret Manager to store the database password for the database user that is to be created later in this guide.

For the examples in this guide, we assume that it's `wlmagent-password`.




### Review system requirements

The following table lists the Oracle editions that you can use and the supported operating system versions:

Operating Systems | Oracle versions | Oracle editions | 

  * Red Hat Enterprise Linux versions 7, 8, and 9
  * Oracle Linux versions 7, 8, and 9

| 

  * Oracle Database 19c
  * Oracle Database 23ai* **Note:** The agent hasn't been tested on Oracle Database 23ai running on Red Hat Enterprise Linux 7 or Oracle Linux 7. 

| 

  * Enterprise Edition
  * Standard Edition
  * Express (Free) Edition

  
---|---|---  
  
### Grant IAM roles to the service account

Agent for Compute Workloads uses the service account attached to the compute instance for authentication and to access Google Cloud resources.

To improve security, we recommend that you use a [single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) rather than using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

To ensure that the service account has the necessary permissions to let Agent for Compute Workloads authenticate with Google Cloud and access Google Cloud resources, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the compute instance: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write data to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 
  * Send agent logs to Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 
  * If you are using Secret Manager to store the password to connect with the Oracle instance: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable access to Cloud APIs

Compute Engine recommends configuring your instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs, then the Agent for Compute Workloads requires at minimum the following Cloud APIs access scopes on the host compute instance:
    
    
    https://www.googleapis.com/auth/cloud-platform
    

For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

If you're running a Oracle workload on a compute instance that doesn't have an external IP address, then you need to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the instance's subnet so that the Agent for Compute Workloads can access the Google APIs and services. For information about how to enable Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). 

## Install and configure the agent by using package manager

This section shows you how to install the Agent for Compute Workloads on your compute instance, and configure it to connect with a Oracle instance, by using a package manager.

To install the Agent for Compute Workloads, complete the following steps:

  1. Create a repository configuration file.
         
         sudo tee /etc/yum.repos.d/google-cloud-workload-agent.repo << EOM
         [google-cloud-workload-agent]
         name=Google Cloud Workload Agent
         baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-workload-agent-\$basearch
         enabled=1
         gpgcheck=0
         repo_gpgcheck=1
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         

  2. Update the metadata of the package manager:
         
         sudo yum makecache
         

  3. Install `google-cloud-workload-agent` rpm package:
         
         sudo yum install google-cloud-workload-agent
         




After you install the agent for Oracle workloads, verify the installation of the agent.

## Install and manage the agent on a fleet of VMs by using VM Extension Manager

This section shows you how to install and manage the Agent for Compute Workloads on a fleet of VMs by using VM Extension Manager.

VM Extension Manager policy lets you perform tasks such as the following:

  * Fleet-wide installation: Install Agent for Compute Workloads on the following: 
    * All VMs in your Google Cloud project, or a subset of VMs identified by labels.
    * All VMs within a zone, or a subset of VMs identified by labels.
  * Configuration management: Apply a custom configuration to the agent on all VMs managed by a policy.



For more information about VM Extension Manager, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager). 

### Set up VM Extension Manager

To set up VM Extension Manager, complete the following steps:

  * In the VM Extension Manager documentation, review the [Before you begin](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#byb) section.
  * Set up the IAM roles needed to create and manage VM Extension Manager policies. For more information, see the following:

    * [Create VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#create-permissions)
    * [Update VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-iam-permissions)
    * [Delete VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#delete-iam-permissions)
    * [List and describe VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-iam-permissions)



### Install and configure the agent on a fleet of VMs

To install the latest version of Agent for Compute Workloads on your VM fleet by using a VM Extension Manager policy, see the appropriate section:

  * Install and configure the agent on VMs within your Google Cloud project
  * Install and configure the agent on VMs within a specific zone



#### Install and configure the agent on VMs within your Google Cloud project

To install the agent on all VMs in your Google Cloud project, or a subset of VMs identified by a label, by using a VM Extension Manager policy, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.

  3. In the **Name** field, enter a name for the policy.

  4. Optional: In the **Description** field, enter a description for the policy.

  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.

  6. In the **Scope** section, select **Global rollout**.

  7. In the **Manage extensions** section, click **Add extension** and then do the following:

     1. From the **Extension** list, select **Google Cloud's Extension for Compute Workloads**.
     2. Leave the **Version** field blank.

This directs the policy to install the latest version of Agent for Compute Workloads.

     3. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent for your Oracle workload, see Configuration parameters.

**Note:** If you apply a VM Extension Manager policy to VMs on which the Agent for Compute Workloads is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-workload-agent/` directory on the respective VMs. 

     4. Click **Done**.

     5. In the **Rollout** field, select the rollout plan option that you want to use: **Slow rollout (recommended)** or **Fast rollout**.

For information about rollout plans, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

  8. Optional: To limit the policy rollout to the required VMs, do the following:

     1. Click **Add labels** and include the labels that identify the required VMs.
     2. Click **Done**.
  9. Click **Create**.




###  gcloud 

In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/create) command:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
        --project=PROJECT_ID \
        --extensions=google-cloud-workload-extension  \
        --rollout-predefined-plan=ROLL_OUT_SPEED \
        [--description="<var>DESCRIPTION</var>" \]
        [--inclusion-labels=KEY1=VALUE1,KEY2=VALUE2 \]
        [--config-from-file=google-cloud-workload-extension="CONFIG_FILE_PATH" \]
        [--priority=PRIORITY]
    

Replace the following:

  * `POLICY_NAME`: a unique name for the VM extension policy.
  * `PROJECT_ID`: the project ID of the Google Cloud project for which you're creating the policy
  * `ROLL_OUT_SPEED`: how quickly you want to rollout the policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

  * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

  * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.

  * `DESCRIPTION`: an optional description for the policy.

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for Compute Workloads.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-workload-extension="CONFIG"`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters.
**Note:** If you apply a VM Extension Manager policy to VMs on which the Agent for Compute Workloads is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-workload-agent/` directory on the respective VMs. 

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the project.
  * `PRIORITY`: an integer from `0` to `65535` that defines the policy's priority. Lower numbers indicate higher priority. The default value is `1000`. For more information, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#policy-priority-resolution).




#### Install and configure the agent on VMs within a specific zone

To install and configure the latest version of Agent for Compute Workloads on your VM fleet within a specific zone by using a VM Extension Manager policy, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.

  3. In the **Name** field, enter a name for the policy.

  4. Optional: In the **Description** field, enter a description for the policy.

  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is `1000`.

  6. Using the **Region** and **Zone** lists, select the zone where you want to apply this policy.

  7. In the **Manage extensions** section, click **Add extension** and then do the following:

     1. From the **Extension** list, select **Google Cloud's Extension for Compute Workloads**.
     2. Leave the **Version** field blank.

This directs the policy to install the latest version of Agent for Compute Workloads.

     3. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent for your Oracle workload, see Configuration parameters.

**Note:** If you apply a VM Extension Manager policy to VMs on which the Agent for Compute Workloads is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-workload-agent/` directory on the respective VMs. 

     4. Click **Done**.

  8. Optional: To limit the policy rollout to the required VMs, do the following:

     1. Click **Add labels** and include the labels that identify the required VMs.
     2. Click **Done**.
  9. Click **Create**.




###  gcloud 
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
        --zone=ZONE \
        --extensions=google-cloud-workload-extension \
        --config-from-file=google-cloud-workload-extension=CONFIG_FILE_PATH \
        [--description="DESCRIPTION" \]
        [--inclusion-labels=KEY_1=VALUE_1 \]
        [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
        [--priority=PRIORITY]

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.

The command fails if a policy with the specified name already exists in the zone.

  * `ZONE`: the zone where you want to apply this policy.

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for Compute Workloads to connect with your Oracle workload.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-workload-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent for your Oracle workload, see Configuration parameters.
**Note:** If you apply a VM Extension Manager policy to VMs on which the Agent for Compute Workloads is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-workload-agent/` directory on the respective VMs. 

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
        --extensions=google-cloud-workload-extension \
        --config-file-path=google-cloud-workload-extension="/usr/agent-config.json"

### Manage the agent on a fleet of VMs

To change how a VM Extension Manager policy manages Agent for Compute Workloads, update the policy. When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, then Agent for Compute Workloads might be installed on new VMs or uninstalled from existing VMs based on whether the VMs match the updated labels.

The following sections show how to manage Agent for Compute Workloads to do the following:

  * Modify agent configuration on a fleet of VMs
  * Update a global policy to include new zones
  * Update a global policy to exclude zones



#### Modify agent configuration on a fleet of VMs

To modify the configuration of Agent for Compute Workloads instances that you've installed on your VM fleet by using a VM Extension Manager policy, you must edit that policy.

To modify agent configuration on your VM fleet, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click the policy that you want to modify.

  3. In the **Extension policy details** page, click **Edit**.

  4. In the **Manage extensions** section, toggle **Google Cloud's Extension for Compute Workloads**.

  5. In the **Configuration file content** field, enter the configuration that you want to apply to the agent.

For information about the configuration parameters supported by the agent, see Configuration parameters

  6. Click **Done**.

  7. Click **Save**.




###  gcloud 

To modify the configuration of Agent for Compute Workloads on your VM fleet, run the [`gcloud compute zone-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To modify the agent configuration:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
        --zone=ZONE \
        --extensions=google-cloud-workload-extension \
        --config-from-file=google-cloud-workload-extension="CONFIG_FILE_PATH" \
        [--inclusion-labels=KEY_1=VALUE_1 \]
        [--inclusion-labels=KEY_2=VALUE_2,KEY_3=VALUE_3 \]
        [--priority=PRIORITY_NUMBER \]
        [--description="DESCRIPTION"]

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to modify.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for Compute Workloads.

    * You can also provide the agent configuration as an inline string by using the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-workload-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent, see Configuration parameters
  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define the labels using which the policy targets VMs.

    * For a VM to be targeted by your policy, the VM must have all the specified labels.
    * If you specify `--inclusion-labels` multiple times, then the policy targets VMs that match _any_ of the provided selectors (logical `OR`). If you omit this flag, then the policy targets all VMs in the specified zone.
  * `PRIORITY_NUMBER`: the priority that you want to set for your policy. You can specify an integer from `0` to `65535`.

  * `DESCRIPTION`: a description of the VM extension policy.




#### Update a global policy to include new zones

When you create VMs in a new zone after you've created and rolled out a global policy, VM Extension Manager does not automatically apply the policy to the VMs in the new zones. To include the VMs in new zones, you must restart the global policy rollout.

To restart a global policy rollout, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/update) command and supply the `--rollout-entry-uuid` option as follows:
        
        gcloud compute global-vm-extension-policies update POLICY_NAME \
            --project=PROJECT_ID \
            --extensions=google-cloud-workload-extension  \
            --rollout-predefined-plan=ROLL_OUT_SPEED \
            --config-from-file=google-cloud-workload-extension="CONFIG_FILE_PATH" \
            --rollout-retry-uuid=UUID
        

Replace the following:

    * `UUID`: a universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).
    * `ROLL_OUT_SPEED`: how quickly you want to rollout the policy. The supported values are `slow_rollout` (recommended) and `fast_rollout`. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

    * Alternatively, you can use a custom rollout plan by specifying the `--rollout-custom-plan` option. For more information, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).

    * You can use either `--rollout-predefined-plan` or `--rollout-custom-plan`, but not both in the same command.




#### Update a global policy to exclude zones

To update a global policy to exclude zones, complete the following steps:

  * In your terminal or Cloud Shell, run the [`gcloud compute global-vm-extension-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/v1/compute/global-vm-extension-policies/update) command and supply a custom rollout plan that specifies the zones in which to apply the policy:
        
        gcloud compute global-vm-extension-policies update POLICY_NAME \
            --project=PROJECT_ID \
            --extensions=google-cloud-workload-extension  \
            --rollout-custom-plan=projects/PROJECT_ID/locations/global/rolloutPlans/NEW_CUSTOM_PLAN_NAME \
            --rollout-retry-uuid=UUID
        

Replace the following:

    * `NEW_CUSTOM_PLAN_NAME`: the name of the new custom rollout plan that identifies the zones in which to apply the policy. For information about creating custom rollout plans, see [About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans).
    * `UUID`: a universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Uninstall agent from a VM fleet

To uninstall Agent for Compute Workloads from your VM fleet, you must delete the VM Extension Manager policy that manages the VM fleet.

While deleting a policy, if another active, lower-priority policy applies to a VM and declares the Agent for Compute Workloads, then the agent remains installed on that VM based on the lower-priority policy.

VM Extension Manager removes the agent from all accessible VMs within one minute of policy deletion. If a VM is inaccessible because the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is removed or the VM is deleted, then VM Extension Manager skips deletion of the Agent for Compute Workloads. If such a VM becomes available again, then VM Extension Manager removes the Agent for Compute Workloads at that time.

To uninstall Agent for Compute Workloads from your VM fleet, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page.

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click the policy that manages the Agent for Compute Workloads on your VM fleet.

  3. In the **Extension policy details** page, click **Delete** and confirm the deletion.




###  gcloud 
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
        --project=PROJECT_ID \
        --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `PROJECT_ID`: the ID of the Google Cloud project where the policy is located.
  * `ZONE`: the Google Cloud zone where the policy is located.



## Verify agent installation

To verify that the agent is running as expected, complete the following steps:

  1. Establish an SSH connection with your compute instance.

  2. Check the status of the agent package:
         
         systemctl status google-cloud-workload-agent
         

If the agent package is running as expected, then the output contains `active (running)`. For example:
         
         google-cloud-workload-agent.service - Google Cloud Agent for Compute Workloads
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-workload-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Sun 2025-07-30 18:59:12 UTC; 10s ago
         Main PID: 14412 (google_cloud_sq)
           Tasks: 7
         Memory: 12.9M (max: 1.0G limit: 1.0G available: 1011.0M)
         CGroup: /system.slice/google-cloud-workload-agent.service
                 └─ 14412 /usr/bin/google_cloud_sql_server_agent --action=run

## Configuration parameters

Agent for Compute Workloads supports the following configuration parameters for Oracle:

Parameter | Description  
---|---  
`log_level` |  `String` To set the logging level of the agent, add the log levels. The available log levels are as follows:  

     * `DEBUG`
     * `INFO`
     * `WARNING`
     * `ERROR`
Default is `INFO`.   
`log_to_cloud` |  `Boolean` To redirect the agent's logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), specify `true`. Default is `true`.  
`oracle_configuration.enabled` |  `Boolean` Optional. Determines whether the Oracle service is active. When set to `true`, or if it's unset and the workload is present, you can configure discovery and metric collection. If set to `false`, the Oracle service and its related functionalities are disabled.  
The following child parameters are applicable only when you specify `oracle_configuration.enabled: true`.  
`oracle_configuration.oracle_discovery.enabled` |  `Boolean` Optional. Determines whether the Oracle Discovery is active. The default value is `true`.  
`oracle_configuration.oracle_discovery.update_frequency` |  `Int` Optional. Specify the sample interval, in seconds, which determines the frequency at which Agent for Compute Workloads runs the discovery process. The default value is 3600 seconds (1 hour). Make sure the value ends with a lowercase "s" to indicate seconds. For example: `30s`.  
`oracle_configuration.oracle_metrics.enabled` |  `Boolean` Optional. To enable Agent for Compute Workloads to collect the Oracle monitoring metrics, specify `true`. The default value is `false`.  
The following child parameters are applicable only when you specify `oracle_metrics.enabled: true`.  
`oracle_configuration.oracle_metrics.collection_frequency` |  `Int` Optional. Specify the sample interval, in seconds, which determines the frequency at which Agent for Compute Workloads queries your Oracle Database instances to collect the Oracle monitoring metrics. The default value is 60 seconds. Make sure the value ends with a lowercase "s" to indicate seconds. For example: `30s`.  
`oracle_configuration.oracle_metrics.query_timeout` |  `String` Optional. Specify the timeout for each query made to the Oracle Database instances. The default value is 10 seconds. Make sure the value ends with a lowercase "s" to indicate seconds. For example: `30s`.  
`oracle_configuration.oracle_metrics.connection_parameters.username` |  `String` Specifies the user account that is used to query the Oracle Database instance. Make sure that this user has the required premissins to read the performance views in your Oracle Database.  
`oracle_configuration.oracle_metrics.connection_parameters.host` |  `String` Specifies the identifier of the local machine hosting your database instance.  
`oracle_configuration.oracle_metrics.connection_parameters.port` |  `Int` Specifies the port on which your Oracle Database instance accepts queries.  
`oracle_configuration.oracle_metrics.connection_parameters.service_name` |  `String` Specifies the service name for your Oracle Database instance that you want the agent to monitor.  
`oracle_configuration.oracle_metrics.connection_parameters.secret.project_id` |  `String` Specifies the project ID of the Secret Manager to retrieve the password for the user making queries to the database.  
`oracle_configuration.oracle_metrics.connection_parameters.secret.secret_name` |  `String` Specifies the name of the secret in Secret Manager that stores the user account's password.  
  
## Collect and view Oracle metrics

You can enable collection of metrics for Oracle Database workloads. See Supported metrics.

### Enable metric collection

To enable the collection of Oracle metrics using the Agent for Compute Workloads, do the following:

     1. Use SSH to connect to your VM instance.

     2. As the Oracle OS user, run the `oraenv` tool to set the environment variables. We assume that you've already defined the `oracle` user and the `ORACLE_SID` in the `/etc/oratab` file.
            
            sudo su - oracle
            export PATH=$PATH:/usr/local/bin
            . oraenv
            sqlplus / as sysdba
            

     3. As `SYSDBA` or `SYSOPER` user, in Oracle Database, create a user for monitoring with a password matching the secret that you created in the **Prerequisites**.

**Note:** If you have an Oracle Multitenant container database, prefix the username with the `common_user_prefix`, usually `c##`, to create a common user. For example, `wlmagent` becomes `c##wlmagent`.
            
            CREATE USER wlmagent IDENTIFIED BY password;
            

     4. As `SYSDBA` or `SYSOPER` user, grant the following permissions to the monitoring user to query performance views:

        * `SESSION`
        * `SELECT_CATALOG_ROLE`
        * `SYSDG`
    
    GRANT CREATE SESSION,SELECT_CATALOG_ROLE,SYSDG TO wlmagent;
    

     5. Exit out of `sqlplus` and the `oracle` user.

     6. As the root user, edit the agent's configuration file using your preferred editor.
            
            sudo nano /etc/google-cloud-workload-agent/configuration.json
            

     7. In the configuration file, edit the `oracle_metrics` section to make the following updates:

        1. Set the parameter `enabled` to `true`.
        2. Set the `service_name` parameter to specify the service name of the Oracle instance that you want the agent to monitor.
        3. Specify the Oracle username for the agent to connect to your database.
        4. Set the `host` and `port` parameters for the agent to connect to your database.
        5. Set the `secret` parameter for the agent to retrieve a password for the username: 
           * `project_id`: The ID of the project which contains the Secret Manager data.
           * `secret_name`: The name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version).

Following is an example configuration file:
    
    {
      "log_level": "INFO",
      "common_discovery": {"collection_frequency": "3600s" },
      "oracle_configuration": {
        "enabled": true,
        "oracle_metrics": {
          "enabled": true,
          "collection_frequency": "30s",
          "connection_parameters": [
            {
              "host": "localhost",
              "port": 1521,
              "service_name": "orcl",
              "username": "wlmagent",
              "secret": {
                "project_id": "my-project",
                "secret_name": "wlmagent_password"
              }
            }
          ]
        }
      }
    }
    

     8. Save the configuration file.

     9. Restart the agent for the new settings to take effect.

### View the metrics

You can view the collected metrics and monitor the Oracle performance and status either using the Metrics Explorer or by importing a custom dashboard.

#### View Metrics in Metrics Explorer

To view the Oracle metrics in Metrics Explorer, do the following:

     1. In the Google Cloud console, go to **Monitoring**.
     2. Click **Metrics Explorer**.
     3. Under **Find resource type and metric** , do the following: 
        1. For **Resource type** , select **VM Instance**.
        2. For **Metric** , select the Oracle metrics that you want to view.

You can view real-time and historical data for the selected Oracle metrics, using filters and aggregation as needed.

#### Import a Custom Dashboard

To view the Oracle metrics collected by the agent, you can create custom Cloud Monitoring dashboards by following the instructions at [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

We provide an example dashboard `oracle-status-overview.json` and instructions for how to import it. The `oracle-status-overview.json` dashboard shows the following Oracle metrics charts:

     * Database time breakdown
     * Database memory usage
     * Average Active Sessions by Wait Class
     * Disk I/O
     * CPU utilization
     * Network Traffic

To import the `oracle-status-overview.json` dashboard, do the following:

     1. Verify that the gcloud CLI is installed and up to date. For instructions, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

     2. From the Agent for Compute Workloads GitHub repository, download the `oracle-status-overview.json` dashboard:
            
            $ curl -H "Accept: application/vnd.github.v3.raw" -o oracle-status-overview.json https://api.github.com/repos/GoogleCloudPlatform/workloadagent/contents/observability/dashboards/oracle-status-overview.json
            

     3. Run the following command to import the dashboard:
            
            gcloud alpha monitoring dashboards create --config-from-file=oracle-status-overview.json
            

After the command is run, the custom dashboard is created in Cloud Monitoring. To learn how to view a dashboard, see [Find and view a dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards#view-dashboard).

### Supported metrics

All Oracle metrics collected by the Agent for Compute Workloads are available under the `workload.googleapis.com/oracle` path.

Following is a list of supported Oracle metrics and their corresponding Cloud Monitoring paths:

     * [Process memory](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-PGASTAT.html#GUID-4666F72E-1E2F-4FFF-89C7-E8144657F78A__G2030180)

       * Process (PGA) memory in use, in bytes.

`process/pga_memory/total_used_size`

       * Process (PGA) memory allocated, in bytes

`process/pga_memory/total_allocated_size`

     * [Shared memory](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SGAINFO.html)

       * Size of shared memory (SGA) item, in bytes

`process/sga_memory/size`

     * [System wait events](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SYSTEM_WAIT_CLASS.html)

       * Total number of waits for a registered wait class

`sys_wait/count`

       * Aggregate time spent in this wait class, in seconds

`sys_wait/time`

       * Total foreground waits in this wait class

`sys_wait/foreground/count`

       * Aggregate foreground wait time for this wait class, in seconds

`sys_wait/foreground/time`

     * [System elapsed time](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SESS_TIME_MODEL.html#GUID-B5CF4362-325D-4F22-9A08-0873FA32A5C0__G2030340)

       * Elapsed time spent performing database user-level calls, in seconds

`sys_time/db_time`

       * CPU time spent on database user-level calls, in seconds

`sys_time/db_cpu`

       * Amount of elapsed time SQL statements are executing

`sys_time/sql_execute_elapsed_time`

       * Amount of elapsed time spent parsing SQL statements

`sys_time/parse_time_elapsed`

       * Amount of elapsed time spent running the PL/SQL interpreter

`sys_time/pl_sql_execution_elapsed_time`

       * Elapsed time consumed by database background processes, in seconds

`sys_time/background_elapsed_time`

     * [I/O statistics](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-IOSTAT_FUNCTION.html)

       * Total count of read operations (small + large)

`iostat/read_ops_count`

       * Total count of write operations (small + large)

`iostat/write_ops_count`

       * Total number of bytes read

`iostat/read_bytes_count`

       * Total number of bytes written

`iostat/write_bytes_count`

       * Average latency per I/O operation

`iostat/average_latency_seconds`

     * [Data files](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_DATA_FILES.html)

       * Allocated size of the data file, in bytes

`data_files/total_bytes`

       * Data file space in use, in bytes

`data_files/bytes_used`

       * Data file free space, in bytes

`data_files/available_bytes`

       * Data file auto-extension limit, in bytes

`data_files/max_bytes`

       * Percentage of the data file used

`data_files/percent_used`

     * [Database instance](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-INSTANCE.html)

       * Instance uptime, in seconds

`instance/uptime`

       * Instance status

`instance/status`

This metric can have the following values:

`UNKNOWN` | `0`  
---|---  
`STARTED` | `1`  
`MOUNTED` | `2`  
`OPEN` | `3`  
`OPEN MIGRATE` | `4`  
       * Open mode

`instance/db_open_mode`

This metric can have the following values:

`UNKNOWN` | `0`  
---|---  
`MOUNTED` | `1`  
`READ WRITE` | `2`  
`READ ONLY` | `3`  
`READ ONLY WITH APPLY` | `4`  
     * [Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-DATAGUARD_STATS.html)

       * Redo apply delay, in seconds

`dataguard/apply_lag`

       * Redo transport delay, in seconds

`dataguard/transport_lag`

## Manage the agent

### Restart the agent

If Agent for Compute Workloads stops working or you update its configuration, then restart the agent.

     1. Use SSH to connect to the VM instance.
     2. Run the following command:
            
            sudo systemctl restart google-cloud-workload-agent

### Check the version of the agent

To check the version of your agent, complete the following steps:

     1. Use SSH to connect to the VM instance.
     2. Run the following command:
            
            yum info google-cloud-workload-agent
            

### Check for updates

     1. Use SSH to connect to the VM instance.
     2. Run the following command:
            
            sudo yum check-update google-cloud-workload-agent

### Update the agent

To make sure that you have the latest version of the agent, check for updates periodically and update the agent:

     1. Use SSH to connect to the VM instance.
     2. Run the following command:
            
            sudo yum --nogpgcheck update google-cloud-workload-agent

### View agent logs

The Agent for Compute Workloads logs are available at `/var/log/google-cloud-workload-agent.log`.

Log verbosity is controlled by the `log_level` parameter. Setting `DEBUG` log level includes additional information for troubleshooting specific issues, but produces significantly larger logs.

By default, the logs for Agent for Compute Workloads are redirected from your VM instances to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

To view the agent's logs in Logging, follow these steps:

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs explorer](https://console.cloud.google.com/logs/query)

     2. Go the **Query** pane.

     3. From the **Resources** drop-down menu, select **Global** , and then click **Apply**.

     4. In the query editor, enter `google-cloud-workload-agent`.

     5. Click **Run query**.

You can view the logs generated by the agent running on all your VM instances. You can filter the logs for a specific instance.

### Configure agent logs in Cloud Logging

To disable the default redirection of agent's logs to Cloud Logging, follow these steps:

     1. Use SSH to connect to your VM instance.

     2. Open the agent's configuration file:
            
            /etc/google-cloud-workload-agent/configuration.json

     3. For the property `log_to_cloud`, update the value to `false`.

     4. Save the configuration file.

     5. [Restart the agent](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-compute-agent-for-sql#restart-compute-agent-for-sql) for this change to take effect.

## Troubleshooting

The following sections provide information about common issues related to using the agent for Oracle Database workloads, their causes and resolution.

### Insufficient IAM permissions

**Issue:** The Agent for Compute Workloads logs show insufficient IAM permissions error.
    
    googleapi: Error 403: The client is not authorized to make this request.
    

**Cause:** The service account used by the agent does not have the required IAM permissions to access the Google Cloud APIs or a password for the Oracle user in the Secret Manager.

**Resolution:** To resolve this issue, make sure that the VM service account has the IAM roles and permissions mentioned in Prerequisites.

### Insufficient authentication scopes

**Issue:** The Agent for Compute Workloads logs show insufficient authentication scopes.
    
    googleapi: Error 403: Request had insufficient authentication scopes.
    

**Cause:** The service account used by the agent does not have the required access scope.

**Resolution:** To resolve this issue, configure the [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) of the VM to `cloud-platform`.

### Metrics not showing up in Cloud Monitoring

**Issue:** Metrics from the Agent for Compute Workloads are not visible in Cloud Monitoring.

**Cause:**

Following are the possible causes of this issue:

     * The service account used by the Agent for Compute Workloads lacks necessary IAM permissions.
     * The Oracle user used by the agent does not have sufficient privileges to query performance views.
     * There are errors in the configuration of the agent.

**Resolution:**

     * To resolve the issue with the insufficient permissions for the service account, do the following:

       1. In the Google Cloud console, go to the **VM instance details** page and note the service account being used by the instance running the agent.
       2. Go to the **IAM & admin** page and make sure that the service account has the all the required roles and permissions mentioned in the Prerequisites. Grant any of the required missing roles to the service account.
     * To resolve the issue with the insufficient permissions for the Oracle user, do the following:

       1. Verify that the Oracle user has the following required permissions to query performance views:

          * `SESSION`
          * `SELECT_CATALOG_ROLE`
          * `SYSDG`
       2. Grant any of the missing permissions by running the following SQL command:
              
              -- Grant the "wlmagent" user the required permissions
              GRANT CREATE SESSION,SELECT_CATALOG_ROLE,SYSDG TO USERNAME;
              

     * To resolve the issue with the misconfiguration of the agent, do the following:

       1. Use SSH to connect to your VM instance.
       2. Review the agent's logs to identify any errors or issues preventing metric collection. You can find the logs at `/var/log/google-cloud-workload-agent.log`.

Look for permission errors, misconfigurations, or connectivity issues.

       3. Resolve any errors.

       4. Restart the agent and check if the metric collection starts.

### Failed to load configuration file

**Issue:** If the configuration file has invalid values, you see the following error. 
    
    "Failed to load configuration","pid":3524,"error":"proto: (line 19:42): unknown
    field "{field_name}"
    

**Resolution:** To resolve this issue, update the configuration file using the details in Configuration parameters.

### Failed to initialize data collection

**Issue:** After installing the agent if the configuration file is not updated, you see the following error: 
    
    "Failed to initialize guest collection","pid":2112,"error":"invalid value for "user_name" "secret_name"
    

**Resolution:** To resolve this issue, initialize the credential configuration using Configuration parameters.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
