---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vmem-policies/
title: Install the Ops Agent by using VM Extension Manager policies \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:08.516859+00:00
---

# Install the Ops Agent by using VM Extension Manager policies  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vmem-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Install the Ops Agent by using VM Extension Manager policies Stay organized with collections  Save and categorize content based on your preferences. 

VM Extension Manager policies let you install the Ops Agent on a fleet of Compute Engine VMs. An extension policy can install the Ops Agent globally across your Google Cloud project or within a specific zone, keep the agent version updated, and apply custom configuration to the agent.

## Before you begin

Before creating VM Extension Manager extension policies to manage the Ops Agent, do the following:

  * [Review general information about VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

  * [Review supported operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-vmem-policies#verify-os-support) to verify that both the Ops Agent and VM Extension Manager are supported on your operating systems.

  * Remove any observability agents already installed on your VMs.

  * Enable the APIs used by the Ops Agent and by VM Extension Manager.

  * Grant the roles used by the Ops Agent.

  * Grant the roles required to use VM Extension Manager.

  * If you want to use a command-line interface to create and manage extension policies, then [install the Google Cloud CLI](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-vmem-policies#install-gcloud).

You can create and manage zonal VM extension policies by using the Google Cloud console or the Google Cloud CLI, gcloud. You create and manage global VM extension policies by using gcloud.




### Remove existing observability agents

Before creating a VM Extension Manager policy for the Ops Agent, ensure that there are no instances of the Ops Agent or the legacy Monitoring agent and Logging agent already on the VM. Running the Ops Agent and the legacy agents on the same VM can cause ingestion of duplicate logs or conflicts in metrics ingestion.

If you use an extension policy to install the Ops Agent on a VM where another observability agent is already installed, then the policy installs the agent, but the agent fails to run because a conflict is detected.

How you remove existing agents depends on how those agents were installed.

  * Agents installed by a VM Manager OS Config policy, which includes the following:

    * Ops Agent installed by using the [Google Cloud console during VM creation](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation).
    * Ops Agent installed by a GA [VM Manager OS Config policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies).
    * Ops Agent, or legacy Monitoring agent or Logging agent installed by a beta [VM Manager OS Config policy](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/managing-agent-policies).

For information about identifying VMs using these policies, see [Find VMs covered by Ops Agent OS policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install#find_vms_covered_by_os_policies).

For information about uninstalling the agent and removing the OS Config policies, see [Uninstall the Ops Agent on VMs covered by Ops Agent OS policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-policies-auto-install#uninstall).

  * Agents installed manually by using an installation script. For information about uninstalling the agents, see the following:

    * Ops Agent: [Uninstall the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#uninstall).
    * Legacy Monitoring agent: [Uninstall the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring/installation#uninstall).
    * Legacy Logging agent: [Uninstall the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/installation#uninstall).



### Enable the APIs required to use the Ops Agent

To use the Ops Agent to write logs and metrics, you must enable the Cloud Logging API and Cloud Monitoring API on your Google Cloud project.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com,monitoring.googleapis.com)

### Grant roles required to use the Ops Agent

To get the permissions that you need to use the Ops Agent to write logs and metrics, ask your administrator to grant you the following IAM roles on your service account: 

  * To write logs: [Logging Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 
  * To write metrics: [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles and the Ops Agent, see [Authorize the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/authorization).

### Enable the API used by VM Extension Manager

VM Extension Manager uses the Compute Engine API. Enable this API in your Google Cloud project if it's not already enabled.

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

### Grant roles required to use VM Extension Manager

To get the permissions that you need to create VM extension policies, ask your administrator to grant you the following IAM roles on the project: 

  * To create extension policies: [VM Extension Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create VM extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VM extension policies:

  * To create extension policies: `compute.vmExtensionPolicies.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about IAM roles and permissions in Compute Engine, see [Compute Engine roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/compute).

### Install the Google Cloud CLI

You can create and manage VM extension policies by using the Google Cloud console or the Google Cloud CLI, gcloud. To use gcloud, you must first install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

To see the components you have installed, run the following command:
    
    
    gcloud components list
    

To verify that you have the latest version, run the following command:
    
    
    gcloud components update
    

## Policy conflicts and priorities

VM Extension Manager associates a priorty with each new policy, with lower numbers indicating higher priorities; the default priority is 1000\. A VM can be covered by multiple policies for an extension like the Ops Agent, but only one policy for the Ops Agent extension is effective on the VM.

VM Extension Manager uses priorities to resolve conflicts among policies applied to a VM. For more information about the resolution process, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#policy-priority-resolution).

## Policy rollout plans for global policies

VM Extension Manager global policies use a rollout plan to determine how a policy is distributed to target VMs. There are two types of rollout plans:

  * **Predefined** rollout plans. There are two predefined rollout plans, chosen by the value used with the `--rollout-predefined-plan` option for gcloud CLI commands.

    * Slow rollout, which deploys the Ops Agent gradually across different zones over a period of time. **This rollout plan is recommended**.

Specify this rollout plan by using the `--rollout-predefined-plan=slow_rollout` option.

    * Fast rollout, which deploys the Ops Agent to all targeted VMs across all zones and regions immediately.

Specify this rollout plan by using the `--rollout-predefined-plan=fast_rollout` option.

  * **Custom** rollout plans, specified by using the `--rollout-custom-plan` option for gcloud CLI commands.

Create custom rollout plans by adding them to the set of rollout plans in your Google Cloud project; for more information, see the Compute Engine API method [`rolloutPlans.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/rolloutPlans/insert).




For more information about rollout plans, see [ Rollout plans for global policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#rollout-global-policies).

## Create VM extension policies to install the Ops Agent

With VM Extension Manager, you create policies that declare which extensions you want to install on VMs. The Ops Agent is one of the available extensions. By defining a policy, you can ensure that supported extensions, including the Ops Agent, are installed and maintained on any VMs that match criteria you specify, such as VM labels.

You can use extension policies for the Ops Agent to perform tasks like the following:

  * Fleetwide installation: Install the Ops Agent on the following:

    * All VMs in one or more zones in your Google Cloud project.
    * All VMs globally (in your Google Cloud project).
    * A subset of VMs in a zone, identified by labels.
    * A subset of VMs across zones in your Google Cloud project, identified by labels.
  * Version control:

    * Keep the Ops Agent updated to the latest version.
    * Pin the Ops Agent version to a specific release.
  * Configuration management: Apply a custom configuration to the Ops Agent on all VMs managed by a policy.




The following sections provide examples of policies that install the Ops Agent according to specific criteria.

VM Extension Manager supports Ops Agent version 2.58.0 or newer, when the Ops Agent has been installed by an extension policy. VM Extension Manager can't manage earlier versions of the Ops Agent, Ops Agent instances installed by using other means, or the legacy [Monitoring agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring) or [Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging).

### Install the latest Ops Agent on all VMs

To create a policy that installs the latest version of the Ops Agent on all VMs in a zone or globally, and updates the Ops Agent when a new version is released, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Click **\+ Create**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Zone** list, select the zone where you want to apply this policy.
  7. In the **Manage extensions** section, click **Add extension** and do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. Leave the **Version** field blank.
  8. Click **Create**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the following [`gcloud compute zone-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create) command to create the policy:
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent 
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.



The `gcloud compute zone-vm-extension-policies` `create` command takes an option `--version` option. If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released.

###  Global 

Use the following [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command to create the policy:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.



The `gcloud compute global-vm-extension-policies` `create` command takes a `--version` option. If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released.

### Pin the Ops Agent to a specific version on all VMs

To create a policy that installs a specific version of the Ops Agent on all VMs in a zone or globally, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Click **\+ Create**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Zone** list, select the zone where you want to apply this policy.
  7. In the **Manage extensions** section, click **Add extension** and do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. From the **Version** list, select the version to install. Use version 2.58.0 or newer.
  8. Click **Create**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the following [`gcloud compute zone-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create) command to create the policy:
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent  \
      --version=ops-agent=VERSION
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * VERSION: The version of the Ops Agent to install. Use version 2.58.0 or newer. 

If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released, as shown in the example that installs the latest version.




###  Global 

Use the following [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command to create the policy:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout \
      --version=ops-agent=VERSION
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * VERSION: The version of the Ops Agent to install. Use version 2.58.0 or newer. 

If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released, as shown in the example that installs the latest version.




For a list of Ops Agent versions, see the Ops Agent [releases page on GitHub](https://github.com/GoogleCloudPlatform/ops-agent/releases).

### Install the Ops Agent on VMs that have a specific label

To create a policy that installs the latest version of Ops Agent on the VMs in a zone or globally that have a specific label, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Click **\+ Create**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Zone** list, select the zone where you want to apply this policy.
  7. In the **Manage extensions** section, click **Add extension** and do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. Leave the **Version** field blank.
  8. In the **Target VM instances** section, select the VMs for the policy. To select VMs with specific labels, click **Add labels** and add the key-value pair.
  9. Click **Create**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the `--inclusion-labels` option to the [`gcloud compute zone-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create) command to specify a comma-separated list of key-value pairs:
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent 
      --inclusion-labels=KEY1=VALUE1,KEY2=VALUE2
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * KEY1=VALUE1,KEY2=VALUE2: A comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all the labels specified in a selector (logical AND) to be included. If you specify the `--inclusion_labels` option multiple times, then the policy targets the VMs that match all the labels in any of the selectors (logical OR). If you omit this option, the policy targets all VMs in the specified zone.



###  Global 

Use the `--inclusion-labels` option to the [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command to specify a comma-separated list of key-value pairs:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout \
      --inclusion-labels=KEY1=VALUE1,KEY2=VALUE2
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * KEY1=VALUE1,KEY2=VALUE2: A comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all the labels specified in a selector (logical AND) to be included. If you specify the `--inclusion_labels` option multiple times, then the policy targets the VMs that match all the labels in any of the selectors (logical OR). If you omit this option, the policy targets all VMs in the specified zone.



### Install the Ops Agent with a custom configuration on all VMs

To create a policy that installs the latest version of the Ops Agent on all VMs in a zone or globally, and provides custom configuration for the Ops Agent, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Click **\+ Create**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Zone** list, select the zone where you want to apply this policy.
  7. In the **Manage extensions** section, click **Add extension** and do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. Leave the **Version** field blank.
     3. In the **Config file content** field, enter the [ YAML configuration string](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration) for the Ops Agent.
  8. Click **Create**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the `--config-from-file` option to the [`gcloud compute zone-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create) command to specify a configuration file:
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent 
      --config-from-file=ops-agent="OPS_AGENT_CONFIG_PATH"
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * OPS_AGENT_CONFIG_PATH: The path to a file containing the [YAML configuration string](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration) for the Ops Agent. This file must exist in the environment where you run the gcloud command. 

Configuration YAML for the Ops Agent can be lengthy. Putting the configuration into a file and passing the file to the gcloud CLI is much less error-prone than attempting to enter properly formatted YAML on the command line. Changing this file after creating the policy doesn't update the policy; to update a policy, use the [ `gcloud compute zone-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command.




###  Global 

Use the `--config-from-file` option to the [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command to specify a configuration file:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout \
      --config-from-file=ops-agent="OPS_AGENT_CONFIG_PATH"
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * OPS_AGENT_CONFIG_PATH: The path to a file containing the [YAML configuration string](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration) for the Ops Agent. This file must exist in the environment where you run the gcloud command. 

Configuration YAML for the Ops Agent can be lengthy. Putting the configuration into a file and passing the file to the gcloud CLI is much less error-prone than attempting to enter properly formatted YAML on the command line. Changing this file after creating the policy doesn't update the policy; to update a policy, use the [`gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command.




If you provide a custom configuration for the Ops Agent when creating or updating an extension policy, then the policy deploys the Ops Agent with the custom configuration. You don't need to manually restart the agent.

The configuration is stored with the extension policy, so don't include sensitive data like passwords in the configuration. Because the configuration is stored with the extension policy, modifying the configuration file does not change the configuration of the agent. You must update the configuration stored with the policy by using the appropriate `gcloud` command:

  * For zonal policies, use the [ `gcloud compute zone-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command.
  * For global policies, use the [ `gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command.



When you provide a custom configuration for the Ops Agent, VM Extension Manager copies the configuration to the location used by the Ops Agent for [ user-specified configuration files](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location) on the target VM:

  * Linux: `/etc/google-cloud-ops-agent/config.yaml`
  * Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml`



If there is a `config.yaml` file present on the VM, then the extension policy overwrites it.

For general information about using the Google Cloud console and the gcloud CLI to create VM extension policies, see [ Install VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy) .

### Install the Ops Agent with a fast rollout plan at higher priority (global only)

To create a global policy that installs the latest version of the Ops Agent on by using a higher-than-default priority and the [fast-rollout plan](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans), use the following [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=fast_rollout \
      --priority=500
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.



### Install the Ops Agent on a subset of zones in a Google Cloud project (global only)

To create a global policy that applies to only a subset of zones in a Google Cloud project, you must use a custom rollout plan that specifies the zones in which to apply the policy. For information about creating custom rollout plans, see [ About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans). To specify a set of zones, use the `locationSelector.includedLocations` field when creating the rollout plan.

To create an extension policy that uses a custom rollout plan, use the following [`gcloud compute global-vm-extension-policies` `create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) command:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-custom-plan=projects/PROJECT_ID/locations/global/rolloutPlans/CUSTOM_PLAN_NAME
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * CUSTOM_PLAN_NAME: The name associated with your custom rollout plan.



## Verify the installation of the Ops Agent

This section describes how to do the following:

  * Verify the status or version of an Ops Agent installation
  * Verify that the Ops Agent is collecting telemetry



### Verify the status or version of an Ops Agent installation

To determine the status or version of the Ops Agent, use one of the following Google Cloud console pages:

###  Compute Engine 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select a VM from the list.
  3. Click the **Observability** tab.



###  Cloud Monitoring 

  1. In the Google Cloud console, go to the **VM Instances** page: 

[Go to **VM Instances**](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **List** view.



When the Ops Agent has been installed on the VM and is collecting logs and metrics, the agent's status is marked with a green checkmark next to the **Ops Agent** label.

To determine the version of the installed agent, hover over the **Ops Agent** label on the Compute Engine or Monitoring dashboard.

### Verify that the Ops Agent is collecting telemetry

If the Ops Agent has been successfully installed and is running correctly, then it sends metrics to Cloud Monitoring and logs to Cloud Logging.

  * For information about verifying collection of metrics, see [Agent is running, but data is not ingested](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-run-ingest#data-not-ingested).
  * For information about verifying collection of logs, see [Verify successful log collection](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#log-ping-messages).



## What's next

  * [Modify the installation by updating your extension policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/manage-agent-vmem-policies).
  * [Troubleshoot problems in extension policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-agent-vmem-policies).
  * Learn more about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * View detailed information about [configuring the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
