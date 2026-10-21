---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies/
title: Manage the Ops Agent by using VM Extension Manager policies \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:14.556122+00:00
---

# Manage the Ops Agent by using VM Extension Manager policies  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Manage the Ops Agent by using VM Extension Manager policies Stay organized with collections  Save and categorize content based on your preferences. 

You can change how a policy manages the Ops Agent by updating the policy. When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. Based on how a policy is changed, the Ops Agent might be installed on new VMs or uninstalled from existing VMs.

## Before you begin

Before starting to using VM Extension Manager extension policies, do the following:

  * Grant the roles required to manage VM Extension Manager policies.

  * If you want to use a command-line interface to create and manage extension policies and you haven't already installed Google Cloud CLI, then [install the gcloud](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies#install-gcloud).

You can create and manage zonal VM extension policies by using the Google Cloud console or the Google Cloud CLI, gcloud. You create and manage global VM extension policies by using gcloud.




### Grant roles required to manage VM Extension Manager policies

To get the permissions that you need to view, modify, and delete VM extension policies, ask your administrator to grant you the following IAM roles on the project: 

  * To view extension policies: 
    * [VM Extension Policy Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyViewer) (`roles/compute.vmExtensionPolicyViewer`)
    * [VM Extension Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`)
  * To modify extension policies: [VM Extension Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) 
  * To delete extension policies: [VM Extension Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view, modify, and delete VM extension policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view, modify, and delete VM extension policies:

  * To view extension policies: `compute.vmExtensionPolicies.list`
  * To view details of an extension policy: `compute.vmExtensionPolicies.get`
  * To modify extension policies: `compute.vmExtensionPolicies.update`
  * To delete extension policies: `compute.vmExtensionPolicies.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about IAM roles and permissions in Compute Engine, see [Compute Engine roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/compute).

## Modify extensions policies that manage the Ops Agent

To change how a policy manages the Ops Agent, update the policy. When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, then the Ops Agent might be installed on new VMs or uninstalled from existing VMs based on whether the VMs match the updated labels.

The following sections show how to change a policy to do the following:

  * Update the pinned version of the agent on all VMs
  * Modify the configuration of the Ops Agent on all VMs



### Update the pinned version of the Ops Agent on all VMs in a zone

To change the pinned version of the Ops Agent on all VMs in a zone, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the policy that you want to update.
  3. Click **Edit**.
  4. In the **Manage extensions** section, do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. Modify the **Version** field. Use version 2.58.0 or newer.
     3. Click **Done**.
  5. Click **Save**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the [`gcloud compute zone-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command with the `--version` option to modify the pinned agent version.

When you update a policy by using gcloud, the request acts as a complete replacement. Any [optional fields](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) that you omit from the request therefore revert to their default values instead of retaining existing values from the modified policy. 

To change the version of the Ops Agent installed on all VMs in a zone by a policy, use the following command:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent 
      --version=ops-agent=VERSION
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * VERSION: The version of the Ops Agent to install. Use version 2.58.0 or newer. For a list of versions, see the Ops Agent [releases page on GitHub](https://github.com/GoogleCloudPlatform/ops-agent/releases). 

If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released, as shown in the example that installs the latest version.




###  Global 

Use the [`gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command with the `--version` option to modify the pinned agent version.

When you update a policy by using gcloud, the request acts as a complete replacement. Any [optional fields](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) that you omit from the request therefore revert to their default values instead of retaining existing values from the modified policy. 

To change the version of the Ops Agent installed on all VMs by a global policy, use the following command:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout \
      --version=ops-agent=VERSION
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * VERSION: The version of the Ops Agent to install. Use version 2.58.0 or newer. For a list of versions, see the Ops Agent [releases page on GitHub](https://github.com/GoogleCloudPlatform/ops-agent/releases). 

If you omit the `--version` option, then the policy installs the latest version and updates the Ops Agent when a new version is released, as shown in the example that installs the latest version.




### Modify the configuration of the Ops Agent on all VMs

To modify the configuration of the Ops Agent, do the following:

###  Console 

To create a zonal policy, you can use the Google Cloud console.

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the policy that you want to update.
  3. Click **Edit**.
  4. In the **Manage extensions** section, do the following: 
     1. From the **Extension** list, select `Google Cloud's Extension for Ops Agent`.
     2. In the **Config file content** field, enter the [ YAML configuration string](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) for the Ops Agent.
     3. Click **Done**.
  5. Click **Save**.



###  gcloud 

To create a zonal or global policy, you can use the gcloud CLI.

###  Zonal 

Use the [`gcloud compute zone-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command with the `--config-from-file` option or the `--config` option to specify a new configuration.

When you update a policy by using gcloud, the request acts as a complete replacement. Any [optional fields](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) that you omit from the request therefore revert to their default values instead of retaining existing values from the modified policy. 

To change the configuration of the Ops Agent installed on all VMs in a zone by a policy, use the following command:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE \
      --extensions=ops-agent 
      --config-from-file=ops-agent="OPS_AGENT_CONFIG_PATH"
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * OPS_AGENT_CONFIG_PATH: The path to a file containing the [YAML configuration string](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) for the Ops Agent. This file must exist in the environment where you run the gcloud command. 

Configuration YAML for the Ops Agent can be lengthy. Putting the configuration into a file and passing the file to the gcloud CLI is much less error-prone than attempting to enter properly formatted YAML on the command line.




###  Global 

Use the [`gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command with the `--config-from-file` option or the `--config` option to specify a new configuration.

When you update a policy by using gcloud, the request acts as a complete replacement. Any [optional fields](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) that you omit from the request therefore revert to their default values instead of retaining existing values from the modified policy. 

To change the configuration of the Ops Agent installed on all VMs by a policy, use the following command:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-predefined-plan=slow_rollout \
      --config-from-file=ops-agent="OPS_AGENT_CONFIG_PATH"
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * OPS_AGENT_CONFIG_PATH: The path to a file containing the [YAML configuration string](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration) for the Ops Agent. This file must exist in the environment where you run the gcloud command. 

Configuration YAML for the Ops Agent can be lengthy. Putting the configuration into a file and passing the file to the gcloud CLI is much less error-prone than attempting to enter properly formatted YAML on the command line.




If you provide a custom configuration for the Ops Agent when creating or updating an extension policy, then the policy deploys the Ops Agent with the custom configuration. You don't need to manually restart the agent.

The configuration is stored with the extension policy, so don't include sensitive data like passwords in the configuration. Because the configuration is stored with the extension policy, modifying the configuration file does not change the configuration of the agent. You must update the configuration stored with the policy by using the appropriate `gcloud` command:

  * For zonal policies, use the [ `gcloud compute zone-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) command.
  * For global policies, use the [ `gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command.



When you provide a custom configuration for the Ops Agent, VM Extension Manager copies the configuration to the location used by the Ops Agent for [ user-specified configuration files](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location) on the target VM:

  * Linux: `/etc/google-cloud-ops-agent/config.yaml`
  * Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml`



If there is a `config.yaml` file present on the VM, then the extension policy overwrites it.

For general information about using the Google Cloud console and the gcloud CLI to manage VM extension policies, see [Modify extensions by updating a VM extension policy](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-vm-ext-policy).

### Extend an existing global policy to include new zones (global only)

When VMs are created in new zones after a global policy has been created and rolled out, VM Extension Manager does not automatically apply the policy to the VMs in the new zones. To include the VMs in new zones, you must restart the global policy rollout.

To restart a global policy rollout, use the [`gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command and supply the `--rollout-retry-uuid=UUID` option.

For example, suppose you created and rolled out a global policy by using the following command:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --version=ops-agent=2.61.0 \
      --rollout-predefined-plan=slow_rollout \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml"
    

To extend the policy to VMs created in previously unused zones, restart the rollout by using the following command:
    
    
    gcloud compute global-vm-extension-policies update test-policy POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --version=ops-agent=2.61.0 \
      --rollout-predefined-plan=slow_rollout \
      --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
      --rollout-retry-uuid=UUID
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * UUID: A universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [ Retry a rollout ](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



### Update a global policy to exclude a set of zones (global only)

To update the zones to which a global policy that excludes some zones in a Google Cloud project, you must use a new custom rollout plan that specifies the zones in which to apply the policy. For information about creating custom rollout plans, see [ About rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#rollout-plans). To specify a set of zones, use the `locationSelector.includedLocations` field when creating the rollout plan.

To update an extension policy that uses a custom rollout plan, use the following [`gcloud compute global-vm-extension-policies` `update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) command:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --rollout-custom-plan=projects/PROJECT_ID/locations/global/rolloutPlans/NEW_CUSTOM_PLAN_NAME \
      --rollout-retry-uuid=UUID
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * NEW_CUSTOM_PLAN_NAME: The name associated with your updated custom rollout plan.
  * UUID: A universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [ Retry a rollout ](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



## Uninstall the Ops Agent by deleting VM extension policies

To uninstall the Ops Agent, delete the VM extension policy that manages the agent. If another active, lower-priority policy applies to a VM and also manages the Ops Agent, then the agent remains installed on that VM based on the lower-priority policy.

VM Extension Manager removes the Ops Agent from all accessible VMs within one minute of policy deletion. If a VM is inaccessible, then VM Extension Manager skips deletion of the agent. If the VM becomes available again, then VM Extension Manager removes the agent at that time.

###  Console 

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Select the policy that you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, click **Delete**.



###  gcloud 

###  Zonal 

To delete the VM extension policy that manages the Ops Agent, use the [`gcloud compute zone-vm-extension-policies` `delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/delete) command:
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.



###  Global 

To delete the global VM extension policy that manages the Ops Agent, use the [`gcloud compute global-vm-extension-policies` `delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete) command:
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=slow_rollout
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.



To accelerate an already started deletion rollout, issue a new deletion command that uses the `fast_rollout` plan. You must also specify the \--rollout-retry-uuid=UUID option:
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=fast_rollout \
      --rollout-retry-uuid=UUID
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * UUID: A universally unique identifier (UUID) that identifies the retry request. You can use any UUID generator to create one. For more information, see [ Retry a rollout ](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



## Retrieve information about VM extension policies

You can retrieve the following information about existing VM extension policies:

  * A list of all policies in your Google Cloud project.
  * Configuration information about a specific policy.



###  Console 

  1. In the Google Cloud console, go to the **Extension policies** page: 

[Go to **Extension policies**](https://console.cloud.google.com/compute/extensionManager/policies)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

This page lists all the VM extension policies in your project.
  2. To view details of a specific extension policy, click the name of the policy.



###  gcloud 

###  Zonal 

## List VM extension policies

To list information about all VM extension policies in a zone, use the [`gcloud compute zone-vm-extension-policies` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/list) command:
    
    
    gcloud compute zone-vm-extension-policies list \
      --project=PROJECT_ID \
      --zone=ZONE \
      --page-size=PAGE_SIZE_INTEGER
    

Replace the following variables in the command:

  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.
  * PAGE_SIZE_INTEGER: The number of policies to list per page; for example, `2`. For more information about sorting and filtering options, see [`gcloud compute zone-vm-extension-policies` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/list) .



## Describe a named VM extension policy

To retrieve the configuration of a named policy in a zone, use the [`gcloud compute zone-vm-extension-policies` `describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/describe) command:
    
    
    gcloud compute zone-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.
  * ZONE: The target zone; for example, `us-central1-f`.



###  Global 

## List global VM extension policies

To list information about global VM extension policies, use the [`gcloud compute global-vm-extension-policies` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/list) command:
    
    
    gcloud compute global-vm-extension-policies list \
      --project=PROJECT_ID \
      --page-size=PAGE_SIZE_INTEGER
    

Replace the following variables in the command:

  * PROJECT_ID: The identifier of the project.
  * PAGE_SIZE_INTEGER: The number of policies to list per page; for example, `2`. For more information about sorting and filtering options, see [`gcloud compute global-vm-extension-policies` `list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/list) .



## Describe a named global VM extension policy

To retrieve the configuration of a named policy in a zone, use the [`gcloud compute global-vm-extension-policies` `describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/describe) command:
    
    
    gcloud compute global-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID
    

Replace the following variables in the command:

  * POLICY_NAME: A name for the VM extension policy.
  * PROJECT_ID: The identifier of the project.



For general information about using the Google Cloud console and the gcloud CLI to retrieve information about VM extension policies, see [ View extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-ext-policies).

## Restart an Ops Agent installed by an extension policy

When the Ops Agent is installed and managed by VM Extension Manager, the Ops Agent isn't managed by the system-management service of the operating system, that is, `systemd` on Linux or the Windows Service Manager on Windows. Therefore, Linux `systemctl` commands and Windows `*-Service` commands don't work with an Ops Agent installed by an extension policy.

To restart an Ops Agent that was installed by an extension policy, do one of the following:

  * Recreate the policy.

    1. Delete the policy. Deleting the policy stops and uninstalls the Ops Agent.

    2. [Create](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vmem-policies#vmem-create) a new policy. The new policy installs the Ops Agent and starts it.

  * Use a temporary, higher-priority policy. If the original policy affects a large number of VMs but you only want to restart the Ops Agent on a small number, add a label to those VMs and configure the new policy to filter on the label.

For example, if a policy with priority 1000 failed to start the Ops Agent on a VM, you could add a label like `status=failed` to the VM. Then [create a new policy](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vmem-policies#labelled-vms) with a higher priority, like 500. For example, a Google Cloud CLI command might look like the following:

###  Zonal 
        
        gcloud compute zone-vm-extension-policies create POLICY_NAME \
          --project=PROJECT_ID \
          --zone=ZONE \
          --extensions=ops-agent  \
          --inclusion-labels=status=failed \
          --priority=500 \
          --config-from-file=ops-agent=/usr/ops-agent-config.yaml
        

Replace the following variables in the command:

    * POLICY_NAME: A name for the VM extension policy.
    * PROJECT_ID: The identifier of the project.
    * ZONE: The target zone; for example, `us-central1-f`.

###  Global 
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --project=PROJECT_ID \
      --extensions=ops-agent  \
      --inclusion-labels=status=failed \
      --priority=500 \
      --config-from-file=ops-agent=/usr/ops-agent-config.yaml \
      --rollout-predefined-plan=fast_rollout
    

Replace the following variables in the command:

    * POLICY_NAME: A name for the VM extension policy.
    * PROJECT_ID: The identifier of the project.

After the new policy successfully installs the Ops Agent, delete the policy and remove the label from the VMs. The Ops Agent remains installed on the VM because the original policy is still active.




## Enable guest agent debug log on the VM

VM Extension Manager policies use the [Compute Engine guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment#guest-agent) to manage the Ops Agent as a VM extension. For information about enabling debug logging for the guest agent, see [View debug logs for the guest agent](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#debug-guest-agent).

## What's next

  * [Troubleshoot problems in extension policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-agent-vmem-policies).
  * View detailed information about [configuring the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).
  * Learn more about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
