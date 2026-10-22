---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy/
title: Install VM extensions by creating extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:18.135930+00:00
---

# Install VM extensions by creating extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install VM extensions by creating extension policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create VM extension policies, which let you automatically install and manage extensions on a fleet of Compute Engine virtual machines (VMs). By defining a policy, you can ensure that specific extensions are installed and maintained on any VMs that match criteria you specify, such as VM labels.

## Before you begin

  * Review the basics about [VM Extension Manager](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * Review [VM Extension Manager quotas](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#quotas).
  * Enable the Compute Engine API in your Google Cloud project if it's not already enabled. 

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

  * Ensure that your VM runs [the guest agent version `20241209.01` or later](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages).
  * To view debug logs for VM Extension Manager events, [configure the log settings for the guest agent](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#debug-guest-agent).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required IAM roles

To get the permission that you need to create an extension policy, ask your administrator to grant you the [VM Extension Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.vmExtensionPolicyAdmin) (`roles/compute.vmExtensionPolicyAdmin`) IAM role. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.vmExtensionPolicies.create` permission, which is required to create an extension policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about IAM roles and permissions in Compute Engine, see [Compute Engine roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam).

## Policy priority and conflict resolution

When multiple policies apply to the same VM, VM Extension Manager uses policy priority to resolve conflicts.

When two policies conflict for the same extension, the policy with the higher priority takes precedence. Priority values range from 0 to 65535, where a lower number signifies a higher priority. The default priority is 1000. If multiple policies have the same priority, VM Extension Manager applies the most recently updated policy to the VMs. Deleting a policy does not remove the extension if a lower-priority policy still applies to the VM.

## Create a global VM extension policy

You can create a global VM extension policy to install extensions on VMs across multiple zones within your project according to a rollout plan. A global VM extension policy isn't directly applied to VMs; instead, as the policy rolls out, VM Extension Manager creates policies in each zone based on the rollout plan. These policies then manage extension installation on VMs within their respective zones.

You can either use the gcloud or the [`globalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/insert) to create global extension policies.

### About rollout plans

Global VM extension policies use rollout plans to manage the deployment of extensions across different locations. You can use one of the predefined rollout plans or create a custom rollout plan.

**Predefined rollout plans**

  * `slow_rollout`: Rolls out the policy over five days. Slow rollout is the default rollout plan.
  * `fast_rollout`: Rolls out the policy immediately to all zones.



**Custom rollout plans**

You can create custom rollout plans by using the [`rolloutPlans.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/rolloutPlans/insert). For example, the following JSON defines a rollout plan named `test-rollout-plan` that targets two zones:
    
    
    {
      "name": "test-rollout-plan",
      "waves": [
        {
          "selectors": [
            {
              "locationSelector": {
                "includedLocations": [
                  "us-central1-a",
                  "us-west1-a"
                ]
              }
            }
          ],
          "validation": {
            "type": "time",
            "timeBasedValidationMetadata": {
              "waitDuration": "0s"
            }
          },
          "orchestrationOptions": {
            "maxConcurrentResourcesPerLocation": "10",
            "maxConcurrentLocations": "10"
          }
        }
      ]
    }

You can then use this custom rollout plan when creating a global policy, as shown in Example 2.

### Create a global policy

Use one of the following methods to create a global VM extension policy.

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Scope** section, select **Global rollout**.
  7. In the **Manage extensions** section, click **Add extension** and do the following for each extension that you want to install on the target VMs: 
     1. From the **Extension** list, select an extension.
     2. From the **Version** list, specify the version number or leave blank for the latest version.
  8. In the **Rollout plan** field, select a rollout plan from the following options:

     * **Slow rollout** : installs extensions gradually across your fleet of VMs over a period of time. This is the default option.
     * **Fast rollout** : installs extensions to all targeted VMs across all zones and regions immediately.

For more information about rollout plans, see [Rollout plans](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies#rollout-global-policies).

**Note:** The Google Cloud console doesn't support selecting a custom rollout plan. To use a custom rollout plan, use either the gcloud CLI or REST API.
  9. In the **Target VM instances** section, select the VMs for the policy. To select VMs with specific labels, click **Add labels** and add the key-value pair.

  10. Click **Create**.




###  gcloud 

Use the [`gcloud compute global-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create) to create a global VM extension policy:
    
    
    gcloud compute global-vm-extension-policies create POLICY_NAME \
      --description="DESCRIPTION" \
      --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
      --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
      --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
      --inclusion-labels=KEY_1=VALUE_1 \
      --priority=PRIORITY \
      --rollout-predefined-plan=ROLLOUT_PLAN \
      --rollout-conflict-behavior=ROLLOUT_CONFLICT_BEHAVIOR
    

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. Valid values for the extensions are: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available.

**Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, only the latest version is supported.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This file is located on the VM where you run the `gcloud` command, not on the VM where you install the extension.

Alternatively, to provide the configuration as an inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in your project across all zones.

  * `PRIORITY`: an integer that defines the policy's priority. Larger numbers indicate higher priority. The default value is 1000. If multiple policies have the same priority, the policy that was most recently updated is applied to the VMs.

  * `ROLLOUT_PLAN`: specify `slow_rollout` or `fast_rollout`. If you need to use a custom rollout plan, use the `--rollout-custom-plan` flag instead of `--rollout-predefined-plan` and specify the plan name, for example:
        
        --rollout-custom-plan=projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME
        

Replace the following:

    * `PROJECT_NUMBER`: the project where the rollout plan is defined.
    * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. If no rollout plan flag is specified, `slow_rollout` is used.
  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when a conflict is detected between a zonal and a global policy. Possible values are:

    * `""` (empty string): the global policy does not overwrite conflicting zonal policies with the same name. This is the default behavior.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more details, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).




**Example 1**

The following command creates a policy named `global-test-extension-policy` that installs the `ops-agent` extension for project `test-project`. The `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent, and `--rollout-predefined-plan` specifies the `slow_rollout` plan.
    
    
    gcloud compute global-vm-extension-policies create global-test-extension-policy \
        --project=test-project \
        --extensions=ops-agent \
        --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
        --rollout-predefined-plan=slow_rollout

**Example 2**

The following command creates a policy named `global-test-extension-policy-2` that installs the `ops-agent` extension for project `test-project` on VMs with label `env=prod`. The policy priority is set to `500`, and the `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent. The `--rollout-custom-plan` flag specifies a custom rollout plan.
    
    
     gcloud compute global-vm-extension-policies create global-test-extension-policy-2 \
        --project=test-project \
        --extensions=ops-agent \
        --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
        --priority=500 \
        --inclusion-labels=env=prod \
        --rollout-custom-plan=projects/12345678/locations/global/rolloutPlans/test-rollout-plan

###  REST 

To create a global VM extension policy, make a `POST` request to the [`globalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalVmExtensionPolicies/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/vmExtensionPolicies
    
    {
      "name": "POLICY_NAME",
      "description": "DESCRIPTION",
      "extensionPolicies": {
         "EXTENSION_NAME_1": {
           "stringConfig": "EXTENSION_NAME_1_CONFIG",
           "pinnedVersion": "EXTENSION_NAME_1_VERSION"
        },
         "EXTENSION_NAME_2": {
           "stringConfig": "EXTENSION_NAME_2_CONFIG",
           "pinnedVersion": "EXTENSION_NAME_2_VERSION"
        }
      },
      "instanceSelectors": [
        {
          "labelSelector": {
             "inclusionLabels": {
               "KEY_1": "VALUE_1"
             }
          }
        }
      ],
      "priority": "PRIORITY",
      "rolloutOperation": {
        "rolloutInput": {
          "conflictBehavior": "ROLLOUT_CONFLICT_BEHAVIOR",
          "name": "projects/PROJECT_NUMBER/locations/global/rolloutPlans/ROLLOUT_PLAN_NAME"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. Valid values for extensions are: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available.

**Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, only the latest version is supported.
  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in your project across all zones.

  * `PRIORITY`: an integer that defines the policy's priority. Larger numbers indicate higher priority. The default value is 1000. If multiple policies have the same priority, the policy that was most recently updated is applied to the VMs.

  * `ROLLOUT_CONFLICT_BEHAVIOR`: specifies the behavior when a conflict is detected between a zonal and a global policy. Possible values are:

    * `""` (empty string): the global policy does not overwrite conflicting zonal policies with the same name. This is the default behavior.
    * `overwrite`: the global policy overwrites any zonal policy that has the same name, and then the global policy manages the policy rollouts in the zone.

For more details, see the [`--rollout-conflict-behavior` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create#--rollout-conflict-behavior).

  * `PROJECT_NUMBER`: the project where the custom rollout plan is defined.

  * `ROLLOUT_PLAN_NAME`: the name of the custom rollout plan you defined. To use a predefined rollout plan, replace the `name` field with `predefinedRolloutPlan` and specify one of the following values:

    * `SLOW_ROLLOUT`: rolls out the policy over five days. This is the default rollout plan if no plan is specified.
    * `FAST_ROLLOUT`: rolls out the policy immediately to all zones.



**Example**

The following example creates a policy named `global-test-extension-policy` that installs the `ops-agent` extension for project `12345678` on VMs with label `env=prod`. The policy priority is set to `500`, and it uses rollout plan `test-rollout-plan`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/12345678/global/vmExtensionPolicies
    
    {
      "name": "global-test-extension-policy",
      "description": "Test extension policy for Ops Agent",
      "extensionPolicies": {
         "ops-agent": {
           "stringConfig": "logging:
            receivers:
              systemd_logs:
                type: systemd_journald
            service:
              pipelines:
                systemd_pipeline:
                  receivers: [systemd_logs]",
           "pinnedVersion": "2.58.0"
            },
      "instanceSelectors": [
        {
          "labelSelector": {
             "inclusionLabels": {
             "env": "prod"
             }
          }
        }
      ],
      "priority": "500",
      "rolloutOperation": {
        "rolloutInput": {
          "name": "projects/12345678/locations/global/rolloutPlans/test-rollout-plan"
        }
      }
    }

## Create a zonal VM extension policy

Use one of the following methods to create a zonal VM extension policy. This zonal policy defines which extensions to install and on which VMs in a specific zone.

###  Console 

  1. In the Google Cloud console, go to the **VM extension policies** page. 

[Go to VM extension policies](https://console.cloud.google.com/compute/extensionManager/policies)

  2. Click **Create extension policy**.
  3. In the **Name** field, enter a name for the policy.
  4. Optional: In the **Description** field, enter a description for the policy.
  5. In the **Priority** field, specify a priority number to resolve conflicts between policies. Lower numbers indicate higher priority. The default value is 1000.
  6. In the **Scope** section, select **Zonal rollout**.
  7. In the **Region** and **Zone** lists, select the region and zone where your VMs are located. VM Extension Manager applies the policy to the VMs in the selected region and zone.
  8. In the **Extensions** section, click **Add extension** and do the following for each extension that you want to install on the target VMs: 
     1. From the **Extension** list, select an extension. See [Supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions).
     2. From the **Version** list, specify the version number of the extension. Leave blank to select the latest version. 
        * For Ops Agent, you can specify version `2.58.0` or later.
        * For Extension for SAP and Extension for Compute workloads, leave the field blank to select the latest version.
     3. Optional: In the **Config file content** field, enter configuration parameters for the extension.
  9. In the **Target VM instances** section, select the VMs for the policy. To select VMs with specific labels, click **Add labels** and add the key-value pair.
  10. Click **Create**.



###  gcloud 

To create a zonal VM extension policy and to roll out the policy to VMs in a specific zone, use the [`gcloud compute zone-vm-extension-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create):
    
    
    gcloud compute zone-vm-extension-policies create POLICY_NAME \
        --zone=ZONE \
        --description="DESCRIPTION" \
        --extensions=EXTENSION_NAME_1,EXTENSION_NAME_2 \
        --version=EXTENSION_NAME_1=VERSION_1,EXTENSION_NAME_2=VERSION_2 \
        --config-from-file=EXTENSION_NAME_1=CONFIG_FILE_PATH_1,EXTENSION_NAME_2=CONFIG_FILE_PATH_2 \
        --inclusion-labels=KEY_1=VALUE_1 \
        --priority=PRIORITY

Replace the following:

  * `POLICY_NAME`: a name for the VM extension policy.
  * `ZONE`: the zone where this policy applies.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`,`EXTENSION_NAME_2`: a comma-separated list of extensions to add to the policy. You must specify at least one extension. Valid values for the extensions are: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1=VERSION_1`,`EXTENSION_NAME_2=VERSION_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available.

**Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, only the latest version is supported.
  * `EXTENSION_NAME_1=CONFIG_FILE_PATH_1`,`EXTENSION_NAME_2=CONFIG_FILE_PATH_2`: a comma-separated list of key-value pairs where the key is the extension name and value is the path to the configuration file for that extension. This path is on the VM where you run the `gcloud` command, not on the VM where you install the extension.

Alternatively, to provide configuration as inline string, use the `--config` flag instead of `--config-from-file`—for example, `EXTENSION_NAME_1="CONFIG_1"`. You can use either `--config-from-file` or `--config`, but not both in the same command.

  * `KEY_1=VALUE_1`: a comma-separated list of key-value pairs that define inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify `--inclusion-labels` multiple times, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit this flag, the policy targets all VMs in the specified zone.

  * `PRIORITY`: an integer from 0 to 65535 that defines the policy's priority. Lower numbers indicate higher priority. The default value is 1000.

The command fails if a policy with the specified name already exists in the zone.




**Example 1**

The following command creates a policy named `test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for project `test-project`. The `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent.
    
    
    gcloud compute zone-vm-extension-policies create test-extension-policy \
        --project=test-project \
        --zone=us-central1-f \
        --extensions=ops-agent \
        --config-from-file=ops-agent="/usr/ops-agent-config.yaml"

**Example 2**

The following command creates a policy named `test-extension-policy-2` that installs the `ops-agent` extension in zone `us-central1-f` for project `test-project` on VMs with label `env=prod`. The policy priority is set to `500`, and the `--config-from-file` flag specifies the path to a local file containing a YAML configuration for the Ops Agent.
    
    
    gcloud compute zone-vm-extension-policies create test-extension-policy-2 \
        --project=test-project \
        --zone=us-central1-f \
        --extensions=ops-agent \
        --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
        --priority=500 \
        --inclusion-labels=env=prod

###  REST 

To create a zonal VM extension policy, make a `POST` request to the [`zoneVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneVmExtensionPolicies/insert). This method defines which extensions to install and on which VMs in a specific zone.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/vmExtensionPolicies
    
    {
      "name": "POLICY_NAME",
      "description": "DESCRIPTION",
      "extensionPolicies": {
         "EXTENSION_NAME_1": {
           "stringConfig": "EXTENSION_NAME_1_CONFIG"
           "pinnedVersion": "EXTENSION_NAME_1_VERSION"
        },
         "EXTENSION_NAME_2": {
           "stringConfig": "EXTENSION_NAME_2_CONFIG"
           "pinnedVersion": "EXTENSION_NAME_2_VERSION"
        },
      "instanceSelectors": [
        {
          "labelSelector": {
             "inclusionLabels": {
             "KEY_1": "VALUE_1"
             }
          }
        }
      ],
      "priority": "PRIORITY"
    }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where this policy applies.
  * `POLICY_NAME`: a name for the VM extension policy.
  * `DESCRIPTION`: an optional description for the policy.
  * `EXTENSION_NAME_1`, `EXTENSION_NAME_2`: the name of the extension to add to the policy. You must specify at least one extension. Valid values for extensions are: 
    * `ops-agent`
    * `google-cloud-sap-extension`
    * `google-cloud-workload-extension`
  * `EXTENSION_NAME_1_VERSION`, `EXTENSION_NAME_2_VERSION`: the extension version. If you don't specify a version for an extension, VM Extension Manager uses the latest available version and automatically upgrades it when new versions become available.

**Note:** For `ops-agent`, VM Extension Manager supports installing version `2.58.0` or newer versions. For `google-cloud-sap-extension` and `google-cloud-workload-extension`, only the latest version is supported.
  * `EXTENSION_NAME_1_CONFIG`, `EXTENSION_NAME_2_CONFIG`: the configuration for the extension, provided as an inline string.

  * `KEY_1`: `VALUE_1`: a key-value pair that defines inclusion labels for a selector. VMs must have all specified labels in a selector to be targeted. If you specify multiple `instanceSelectors`, the policy targets VMs that match _any_ of the provided selectors (logical OR). If you omit `instanceSelectors`, the policy targets all VMs in the specified zone.

  * `PRIORITY`: an integer from 0 to 65535 that defines the policy's priority. Lower numbers indicate higher priority. The default value is 1000.




**Example**

The following example creates a policy named `test-extension-policy` that installs the `ops-agent` extension in zone `us-central1-f` for `my-project`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/vmExtensionPolicies
    
    {
      "name": "test-extension-policy",
      "description": "Test extension policy for Ops Agent",
      "extensionPolicies": {
         "ops-agent": {
           "stringConfig": "logging:
            receivers:
              systemd_logs:
                type: systemd_journald
            service:
              pipelines:
                systemd_pipeline:
                  receivers: [systemd_logs]",
           "pinnedVersion": "2.58.0"
            },
      "instanceSelectors": [
        {
          "labelSelector": {
             "inclusionLabels": {
             "env": "test"
             }
          }
        }
      ],
      "priority": "500"
    }
    }
    

## What's next

  * Learn how to [manage VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).
  * [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
