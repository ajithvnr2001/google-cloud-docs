---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis/
title: Set up the agent for Redis workloads \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:15.779013+00:00
---

# Set up the agent for Redis workloads  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Set up the agent for Redis workloads Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to install Agent for Compute Workloads on Compute Engine instances, and configure the agent to connect with a Redis workload running on those compute instances.

After you install and configure the agent, it collects metrics from your Redis workload and the underlying compute instances and sends them to Workload Manager. You can then use [Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations) to scan your Redis workloads for deviations from best practices for infrastructure, operating system, and workload configurations.

## Before you begin

Before you install and configure Agent for Compute Workloads, you need to make sure that the following prerequisites are met:

  * You've deployed a Redis workload on one or more compute instances.
  * You've reviewed the [supported regions](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) where you can create Workload Manager evaluations.
  * Your administrator has granted you [IAM roles required to create and run Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).
  * You've granted the required IAM roles for the agent.
  * You've enabled access to Cloud APIs.



### Required IAM roles for the agent

Agent for Compute Workloads uses the service account attached to the compute instance for authentication and to access Google Cloud resources.

To improve security, we recommend that you use a [single-purpose service account](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose) rather than using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

To ensure that the service account has the necessary permissions to let Agent for Compute Workloads authenticate with Google Cloud and access Google Cloud resources, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect metrics from the compute instance: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write data to Workload Manager data warehouse: [Workload Manager Insights Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.insightWriter) (`roles/workloadmanager.insightWriter`) 
  * Send agent logs to Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 
  * If you are using Secret Manager to store the password to connect with the Redis instance: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable access to Cloud APIs

Compute Engine recommends configuring your instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the instance service account to control access to Google Cloud resources. For more information, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

If you limit access to the Cloud APIs, then the Agent for Compute Workloads requires at minimum the following Cloud APIs access scopes on the host compute instance:
    
    
    https://www.googleapis.com/auth/cloud-platform
    

For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

If you're running a Redis workload on a compute instance that doesn't have an external IP address, then you need to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the instance's subnet so that the Agent for Compute Workloads can access the Google APIs and services. For information about how to enable Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). 

## Install and configure the agent by using package manager

This section shows you how to install the Agent for Compute Workloads on your compute instance, and configure it to connect with a Redis instance, by using a package manager.

To install the Agent for Compute Workloads, complete the following steps:

###  RHEL 

On Red Hat Enterprise Linux (RHEL), you install Agent for Compute Workloads by using the `yum` package management command. This command completes the following tasks:

  * Downloads the latest version of the agent.
  * Creates a `systemd` service for the agent, named `google-cloud-workload-agent`.
  * Enables and starts the `google-cloud-workload-agent` service.



To install and configure Agent for Compute Workloads on a RHEL based compute instance, complete the following steps:

  1. Establish an SSH connection with your compute instance.

  2. In your terminal, install the agent:
         
         sudo tee /etc/yum.repos.d/google-cloud-workload-agent.repo << EOM
         [google-cloud-workload-agent]
         name=Google Cloud Agent for Compute Workloads
         baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-workload-agent-$basearch
         enabled=1
         gpgcheck=0
         repo_gpgcheck=1
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         sudo yum install google-cloud-workload-agent
         

  3. Open the agent's configuration file:
         
         /etc/google-cloud-workload-agent/configuration.json
         

  4. Specify values for all mandatory parameters, as described in Configuration parameters.

  5. Save the configuration file

  6. Restart the agent for the changes to take effect.




###  SLES 

On SUSE Linux Enterprise Server (SLES), you install Agent for Compute Workloads by using the `zypper` package management command. This command completes the following tasks:

  * Downloads the latest version of the agent.
  * Creates a `systemd` service for the agent, named `google-cloud-workload-agent`.
  * Enables and starts the `google-cloud-workload-agent` service.



To install and configure Agent for Compute Workloads on a SLES based compute instance, complete the following steps:

  1. Establish an SSH connection with your compute instance.

  2. In your terminal, install the agent:
         
         sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-workload-agent-$basearch
         google-cloud-workload-agent
         sudo zypper install google-cloud-workload-agent
         

  3. Open the agent's configuration file:
         
         /etc/google-cloud-workload-agent/configuration.json
         

  4. Specify values for all mandatory parameters, as described in Configuration parameters.

  5. Save the configuration file

  6. Restart the agent for the changes to take effect.




###  Debian 

On Debian, you install Agent for Compute Workloads by using the `apt` package management command. This command completes the following tasks:

  * Downloads the latest version of the agent.
  * Creates a `systemd` service for the agent, named `google-cloud-workload-agent`.
  * Enables and starts the `google-cloud-workload-agent` service.



To install and configure Agent for Compute Workloads on a Debian based compute instance, complete the following steps:

  1. Establish an SSH connection with your compute instance.

  2. In your terminal, install the agent:
         
         echo 'deb https://packages.cloud.google.com/apt google-cloud-workload-agent-x86-64-apt main' | sudo tee -a /etc/apt/sources.list.d/google-cloud-workload-agent.list
         sudo apt-get update
         sudo apt-get install google-cloud-workload-agent
         

  3. Open the agent's configuration file:
         
         /etc/google-cloud-workload-agent/configuration.json
         

  4. Specify values for all mandatory parameters, as described in Configuration parameters.

  5. Save the configuration file

  6. Restart the agent for the changes to take effect.




###  Windows 

On Windows, you install Agent for Compute Workloads by using the `googet` package management command. This command completes the following tasks:

  * Downloads the latest version of the agent.
  * Creates a Windows service named `google-cloud-workload-agent`.
  * Creates a scheduled task that runs every minute to check if the service is running and if necessary, restart the service.

**Warning:** Don't stop the `google-cloud-workload-agent` Windows service manually or delete its scheduled task.

To install and configure Agent for Compute Workloads on a Windows based compute instance, complete the following steps:

  1. Establish a connection with your compute instance by using RDP.

For information about how to do this, see [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. As an administrator, run the following commands from PowerShell:
         
         googet addrepo google-cloud-workload-agent  https://packages.cloud.google.com/yuck/repos/google-cloud-workload-agent-windows-x86_64
         googet install google-cloud-workload-agent
         

  3. Open the agent's configuration file:
         
         %ProgramFiles%\Google\google-cloud-workload-agent\conf\configuration.json
         

  4. Specify values for all mandatory parameters, as described in Configuration parameters.

  5. Save the configuration file

  6. Restart the agent for the changes to take effect.




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

For information about the configuration parameters supported by the agent for your Redis workload, see Configuration parameters.

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

For information about the configuration parameters supported by the agent for your Redis workload, see Configuration parameters.

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

  * `CONFIG_FILE_PATH`: the local path to the JSON file that contains the configuration for the Agent for Compute Workloads to connect with your Redis workload.

    * Alternatively, to provide configuration as an inline string, use the `--config` flag instead of `--config-from-file`. For example, `--config=google-cloud-workload-extension="CONFIG"`. Google Cloud recommends that you use `--config-from-file`.
    * You can use either `--config-from-file` or `--config`, but not both in the same command.
    * For information about the configuration parameters supported by the agent for your Redis workload, see Configuration parameters.
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

###  RHEL 

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




###  SLES 

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




###  Debian 

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




###  Windows 

  1. Establish a connection with your compute instance by using RDP.

For information about how to do this, see [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. As an administrator, run the following command from PowerShell:
         
         $(Get-Service -Name 'google-cloud-workload-agent' -ErrorAction Ignore).Status
         

If the agent is running as expected, then you see the status as `Running`. 




## Example configuration file

The following is an example configuration that lets Agent for Compute Workloads connect with a Redis instance. For authentication, a Secret Manager secret is used, which is stored in the same Google Cloud project where the Redis instance is running.
    
    
    {
      "log_level": "INFO",
      "common_discovery": {
        "collection_frequency": "10800s"
      },
      "redis_configuration": {
        "enabled": true,
        "connection_parameters": {
          "username": "db_user_name",
          "secret": {
            "secret_name": "db_pwd_secret_name",
            "project_id": ""
          },
          "host": "localhost",
          "port": 1433
        }
      }
    }
    

## Configuration parameters

The following table describes the configuration parameters of Agent for Compute Workloads that support evaluations for Redis workloads:

Parameters  
---  
`log_level` |  `String` To set the logging level of the agent, set the required value. The available log levels are as follows:

  * `DEBUG`
  * `INFO`
  * `WARNING`
  * `ERROR`

The default log level is `INFO`. Don't change the logging level unless you are directed by Cloud Customer Care.  
`log_to_cloud` |  `Boolean` To redirect the agent's logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), specify `true`. The default value is `true`.  
`agent_properties.log_usage_metrics` |  `Boolean` To enable logging of the agent's health metrics, set the value to `true`. The default value is `false`.  
`common_discovery.collection_frequency` |  `Duration` Specify the frequency, in seconds, at which the agent's workload discovery service runs. The default value is `10800s`. Make sure that this parameter's value ends with a lowercase `s`.  
`redis_configuration.enabled` |  `Boolean` To let the agent collect metrics from the Redis instance, set the value to `true`. The default value is `false`. **Important:** For the other Redis specific agent parameters to work, you must set `redis_configuration.enabled` to `true`.  
`redis_configuration.connection_parameters.username` |  `String` Specify the user account that the agent uses to query the Redis instance.  
`redis_configuration.connection_parameters.password` |  `String` Specify the plain text password for the user account that the agent uses to query the Redis instance. Instead of specifying a plain text password, we recommend that you use the `secret.name` and `secret.project_id` parameters. For authentication, the agent uses the following order of preference: if specified, the `secret` set of parameters are preferred over the `password` parameter. We recommend that you set only one authentication option in the agent's configuration file.  
`redis_configuration.connection_parameters.secret.secret_name` |  `String` Optional. To securely provide the password for the user account that the agent uses to query the Redis instance, specify the name of the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret that contains the password. For authentication, the agent uses the following order of preference: if specified, the `secret` set of parameters are preferred over the `password` parameter. We recommend that you set only one authentication option in the agent's configuration file.  
`redis_configuration.connection_parameters.secret.project_id` |  `String` Optional. To use the `secret.secret_name` parameter for authenticating the specified user account, specify the project ID of the Google Cloud project where the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secret is stored. If the secret and the workload are in the same Google Cloud project, then set the value of this parameter to an empty string (`""`).  
`redis_configuration.connection_parameters.host` |  `String` Specify the Redis hostname.  
`redis_configuration.connection_parameters.port` |  `Int` Specify the port at which your Redis instance accepts queries.  
  
## What's next

  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)
  * Learn about the [Workload Manager best practices for Redis](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general#redis-general)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
