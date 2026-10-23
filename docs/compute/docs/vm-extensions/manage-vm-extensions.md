---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions/
title: Manage VM extensions by using extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:26.791588+00:00
---

# Manage VM extensions by using extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage VM extensions by using extension policies Stay organized with collections  Save and categorize content based on your preferences. 

VM Extension Manager uses extension policies to manage your VM extensions at scale. For more information, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager). This document describes how to view, update, and delete VM extension policies.

**Note:** By using Google Cloud console, you can manage only the zonal extension policies.

### IAM roles and permissions

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

## View extension policies

You can view a list of VM extension policies in your project, or view the details of a specific policy by using the Google Cloud console or the Google Cloud CLI.

###  Global 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies**. This tab lists all the global VM extension policies in your project.



###  gcloud 

To view all global extension policies in a project, use the [`gcloud compute global-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/list):
    
    
    gcloud compute global-vm-extension-policies list \
      --project=PROJECT_ID \
      --page-size=PAGE_SIZE

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific global extension policy, use the [`gcloud compute global-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/describe):
    
    
    gcloud compute global-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to describe.
  * `PROJECT_ID`: your Google Cloud project ID.



###  REST 

To view all global extension policies in a project, make a `GET` request to the [`globalVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies
    

To view details of a specific global extension policy, make a `GET` request to the [`globalVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: your Google Cloud project ID.



###  Zonal 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

This page lists all the VM extension policies in your project.
  2. To view details of a specific extension policy, click the name of the policy.



###  gcloud 

To view all extension policies in a zone, use the [`gcloud compute zone-vm-extension-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/list):
    
    
    gcloud compute zone-vm-extension-policies list \
      --project=PROJECT_ID \
      --zone=ZONE \
      --page-size=PAGE_SIZE

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the name of the zone where you want to list VM extension policies.
  * `PAGE_SIZE`: the maximum number of results to return per page.



To view details of a specific extension policy, use the [`gcloud compute zone-vm-extension-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/describe):
    
    
    gcloud compute zone-vm-extension-policies describe POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to describe.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



###  REST 

To view all zonal extension policies in a project, make a `GET` request to the [`zoneVmExtensionPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies
    

To view details of a specific zonal extension policy, make a `GET` request to the [`zoneVmExtensionPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to view.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.



## Modify extensions by updating a VM extension policy

When you update a policy, VM Extension Manager rolls out the changes to all applicable VMs, typically within one minute. If you modify inclusion labels, extensions might be installed on new VMs or uninstalled from existing VMs based on whether they match the updated labels.

###  Global 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies** , and then select the policy that you want to edit.
  3. Click **Edit**.
  4. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  5. In the **Manage extensions** section, do the following: 
     * To add more extensions, click **Add extension** and select the extension and version.
     * To delete an extension managed by this policy, click the **Delete** button next to the extension name. 
     * If you want to apply labels, add labels for the target VMs in the **Target VM instances** section.

     * Click **Save**.


**Note:** The Google Cloud console doesn't support editing a rollout. To edit a rollout, use either the gcloud CLI or REST API.

###  gcloud 

Use the [`gcloud compute global-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update) to modify an existing global VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a global VM extension policy, run the following command:
    
    
    gcloud compute global-vm-extension-policies update POLICY_NAME \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --description="DESCRIPTION" \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY_NUMBER \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-retry-uuid=RETRY_UUID \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR

Replace the following:

  * `POLICY_NAME`: a name of the VM extension policy to update.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the names of the extensions to update. You must specify at least one extension.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `VERSION_1`: the version of the first VM extension.
  * `VERSION_2`: the version of the second VM extension.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This path is on the VM where you run the `gcloud` command, not on the VM where you install the extension.

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in all zones in the project.

  * `PRIORITY_NUMBER`: the priority number for the VM extension policy.

  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, use the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` and specify the plan name, for example:
        
        --rollout-custom-plan=projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME
        

Replace the following:

    * `PROJECT_NUMBER`: the project where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan that you defined.

If no rollout plan flag is specified, `slow_rollout` is used.

  * `ROLLOUT_CONFLICT_BEHAVIOR`: Specifies the behavior when a conflict is detected between a zonal and a global policy. Possible values are:

  * `""` (empty string): the global policy does not overwrite conflicting zonal policies with the same name. This is the default behavior.

  * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more details, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/update#--rollout-conflict-behavior).

  * `RETRY_UUID`: A UUID that identifies a retry attempt for a policy update rollout. It lets you retry an update without changes. An error occurs if you set this flag and the policy is modified. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).




###  Zonal 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Select the policy that you want to update.
  3. Click **Edit**.
  4. Modify the **Description** , **Priority** , **Extensions** , or **Target VM instances**.
  5. Click **Save**.



###  gcloud 

Use the [`gcloud compute zone-vm-extension-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/update) to modify an existing VM extension policy. When you update a policy by using gcloud, the request acts as a complete replacement. Any optional fields you omit revert to their default values instead of retaining existing values from the modified policy.

To update a VM extension policy, run the following command:
    
    
    gcloud compute zone-vm-extension-policies update POLICY_NAME \
      --zone=ZONE \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --description="DESCRIPTION" \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY_NUMBER

Replace the following:

  * `POLICY_NAME`: a name of the VM extension policy to update.
  * `ZONE`: the Google Cloud zone where the policy applies.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the names of the extensions to update. You must specify at least one extension.
  * `DESCRIPTION`: an optional description for the VM extension policy.
  * `VERSION_1`: the version of the first VM extension.
  * `VERSION_2`: the version of the second VM extension.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This path is on the VM where you run the `gcloud` command, not on the VM where you install the extension.

Alternatively, to provide configuration as inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in the specified zone.

  * `PRIORITY_NUMBER`: the priority number for the VM extension policy.




###  REST 

To update a zonal extension policy, make a `PATCH` request to the [`zoneVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/update). When you update a policy by using REST, you only need to provide the fields that you want to update. Any fields that you omit retain their existing values.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    
    {
    "description": "DESCRIPTION",
    "extensionPolicies": {
      "EXTENSION_NAME": {
        "pinnedVersion": "EXTENSION_NAME_VERSION",
        "stringConfig": "EXTENSION_NAME_CONFIG"
      }
    },
    "instanceSelectors": [
      {
        "labelSelector": {
          "inclusionLabels": {
            "KEY_1": "VALUE_1",
            "KEY_2": "VALUE_2"
          }
        }
      }
    ],
    "priority": PRIORITY_NUMBER
    }
    

Replace the following: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the VM extension policy is located.
  * `POLICY_NAME`: a name of the VM extension policy to update.
  * `DESCRIPTION`: a description of the VM extension policy.
  * `EXTENSION_NAME`: The name of the extension to update, used as a key in `extensionPolicies` map. To update multiple extensions, include multiple entries in the `extensionPolicies` map.
  * `EXTENSION_NAME_VERSION`: the version of the VM extension.
  * `EXTENSION_NAME_CONFIG`: configuration settings for the VM extension, as an inline string.
  * `KEY_1:VALUE_1`, `KEY_2:VALUE_2`: key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. To specify multiple selectors, include multiple objects in the `instanceSelectors` array, each with a `labelSelector` field. In that case, VM Extension Manager targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone.
  * `PRIORITY_NUMBER`: the priority number for the VM extension policy.



## Uninstall extensions by deleting a VM extension policy

When you delete a policy, VM Extension Manager uninstalls the extensions from any VMs managed by that policy. However, if another active, lower-priority policy applies to a VM and declares the same extension, the extension remains installed on that VM based on the lower-priority policy.

VM Extension Manager removes extensions from all accessible VMs within one minute of policy deletion. If a VM is inaccessible because the guest agent is removed or the VM is deleted, VM Extension Manager skips deletion of the extension. If such a VM becomes available again, VM Extension Manager removes the extensions at that time.

###  Global 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Global policies** , and then select the policy you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, enter the policy name, and then click **Delete**.



###  gcloud 

Use the [`gcloud compute global-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/delete) to delete an existing global VM extension policy.
    
    
    gcloud compute global-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-retry-uuid=RETRY_UUID

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, use the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` and specify the plan name, for example:
        
        --rollout-custom-plan=projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME
        

Replace the following:

    * `PROJECT_NUMBER`: The project where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: The name of the custom rollout plan you defined.

If no rollout plan flag is specified, `slow_rollout` is used.

  * `RETRY_UUID`: A UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).




###  REST 

To delete a global extension policy, make a `POST` request to the [`globalVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/delete).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies/POLICY_NAME
    
    {
    "retryUuid": "RETRY_UUID",
    "predefinedRolloutPlan": "ROLLOUT_PLAN"
    }
    

Replace the following: 

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`.
  * `RETRY_UUID`: a UUID to retry deleting an extension policy. Set this field only when retrying a delete request for an existing policy that is in the `DELETING` state. Setting this field when the policy is not in the `DELETING` state causes an error. For more information, see [Retry a rollout](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#retry-rollout).



###  Zonal 

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Select the policy that you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, click **Delete**.



###  gcloud 

Use the [`gcloud compute zone-vm-extension-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/delete) to delete an existing VM extension policy.
    
    
    gcloud compute zone-vm-extension-policies delete POLICY_NAME \
      --project=PROJECT_ID \
      --zone=ZONE

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy you want to delete.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ZONE`: the Google Cloud zone where the policy is located.



###  REST 

To delete a zonal extension policy, make a `DELETE` request to the [`zoneVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies/POLICY_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the VM extension policy that you want to delete.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the Google Cloud zone where the policy is located.



## Troubleshoot VM extensions

This section describes how to troubleshoot issues with VM extensions.

When troubleshooting, review the event logs by using [Cloud Logging](https://docs.cloud.google.com/logging/docs). For details, see [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs).

### Verify that an extension is installed

You can verify that an extension is installed by checking the following on the VM:

  * [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/ssh) and check for running processes.

The following table lists the process names for each extension:

Extension name | Extension process name  
---|---  
`google-cloud-sap-extension` | `google_cloud_sap_agent`  
`google-cloud-workload-extension` | `google_cloud_workload_agent`  
`ops-agent` | `ops_agent`  
  
###  Linux 
        
        ps aux | grep 'EXTENSION_PROCESS_NAME'

Replace `EXTENSION_PROCESS_NAME` with the process name of the extension. For example, to check the Ops Agent process, run the following command: 
        
        ps aux | grep 'ops_agent'

###  Windows 
        
        tasklist | findstr "EXTENSION_PROCESS_NAME"

Replace `EXTENSION_PROCESS_NAME` with the process name of the extension. For example, to check the Ops Agent process, run the following command: 
        
        tasklist | findstr "ops_agent"

The output of the `ps` command on a Linux VM for the Ops Agent might show an entry similar to the following:
        
        ....
        /var/lib/google-guest-agent/931374772276853249/plugins/ops-agent_baddabb3dac3
        ....

  * Enable and review guest agent logs. The guest agent logs show when an extension is installed and started.

The following is an example of the output you might see in the guest agent logs when an Ops Agent extension is installed:
        
        my-instance google_guest_agent [14972]: Installing plugin "ops-agent", revision "2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (client.go:181) Sent message [[type.googleapis.com/agent_controlplane.PluginEventMessage: (revision_id:"2dfa648c1892da87)]]
        my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "DownloadPluginStep" on plugin "ops-agent_2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (pluginengine.go:316) Successfully downloaded "https://storage.googleapis.com/acp-gcs-bucket-us-central1-a/ops-agent
        my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "UnpackPluginArchiveStep" on plugin "ops-agent_2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (pluginengine.go:361) Successfully unpacked "/var/lib/google-guest-agent/ops-agent.tar.gz" to "/google-guest-agent/ops-agent_2dfa648c1892da87
        my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "LaunchPluginStep" on plugin "ops-agent_2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (run_linux.go:32) Attempting process start: (OutputType:0 Name:/var/lib/google-guest-agent/plugins/ops-agent_2dfa648c1892da87)
        my-instance google_guest_agent [14972]: (pluginlauncher.go:132) Launched a plugin process from "/var/lib/google-guest-agent/plugins/ops-agent_2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (plugin.go:136) Dialing in on plugin "ops-agent 2dfa648c1892da87"
        my-instance google_guest_agent [14972]: (plugin.go:51) Executing start request on plugin "ops-agent_2dfa648c1892da87"




### Troubleshoot installation issues

If an extension isn't installed on a VM after you create a policy, use the following steps to troubleshoot the issue:

  1. Wait for policy enforcement. It can take up to an hour for a policy to be applied, including any retries.
  2. Check that the inclusion labels specified in the policy match the labels on the VM.
  3. To identify potential installation errors, enable debug logging for the guest agent.
  4. After you fix the underlying issue, retry the installation by using one of the following methods:

     * Recreate the policy: [Delete the policy](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#uninstall-ext-policy) and then [create a new policy](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#create-vm-ext-policy).
     * Use a temporary high-priority policy: If you want to avoid recreating a policy that affects many VMs, use a temporary, higher-priority policy to retry the installation on specific VMs:

       1. [Add a new label to the VMs](https://docs.cloud.google.com/compute/docs/labeling-resources#add_or_update_labels_to_existing_resources) for which the installation failed. For example, add a `status=failed` label.
       2. Create a policy with a higher priority that targets the new label. For example, if the original policy that failed had the default priority of `1000`, create a policy with a higher priority, such as `500`.
              
              gcloud compute zone-vm-extension-policies create temp-policy \
                  --project=test-project \
                  --zone=us-central1-f \
                  --extensions=ops-agent \
                  --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
                  --priority=500 \
                  --inclusion-labels=status=failed
              

       3. After the extension is installed successfully, delete the temporary policy and [remove the label from the VMs](https://docs.cloud.google.com/compute/docs/labeling-resources#remove_a_label). The extension remains installed because the original policy is still active.




## View debug logs for the guest agent

To enable debug logging, add log level and verbosity settings to the [`Core`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#core) section of the guest agent configuration file as follows:

###  Linux 

  1. Open the guest agent configuration file located at `/etc/default/instance_configs.cfg`.
  2. Add the following lines to the file. If the `[Core]` section already exists, add the `log_level` and `log_verbosity` settings to it.
         
         [Core]
         log_level = 4
         log_verbosity = 4
         

  3. Restart the guest agent manager by running the following command:
         
         sudo systemctl restart google-guest-agent-manager
         

  4. To view logs for guest agent activity during extension installation, run the following command:
         
         journalctl -u google-guest-agent-manager
         




###  Windows 

  1. Open the guest agent configuration file located at `C:\Program Files\Google\Compute Engine\instance_configs.cfg`.
  2. Add the following lines to the file. If the `[Core]` section already exists, add the `log_level` and `log_verbosity` settings to it.
         
         [Core]
         log_level = 4
         log_verbosity = 4
         

  3. Restart the guest agent manager by running the following command as Windows administrator:
         
         net stop GCEAgentManager
          net start GCEAgentManager
         

  4. To view logs for guest agent activity during extension installation, run the following command in PowerShell:
         
         Get-Eventlog -Source google_guest_agent_manager -LogName Application
         




After enabling debug logs, check for the following common errors:

  * Not enough disk space: If the logs report insufficient disk space, free up space on the disk or resize the disk to add more space.
  * Excessive resource usage: If the logs indicate the guest agent stopped the extension due to excessive memory or CPU usage, change the VM's machine type to one with more resources.



## What's next

  * Learn more about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
