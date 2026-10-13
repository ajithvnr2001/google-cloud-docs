---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/global-vm-extension-policies/create/
title: gcloud beta compute global-vm-extension-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:05.418439+00:00
---

# gcloud beta compute global-vm-extension-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/global-vm-extension-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute global-vm-extension-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute global-vm-extension-policies create - create a Compute Engine global VM extension policy 
SYNOPSIS
    

`gcloud beta compute global-vm-extension-policies create` `NAME` `--extensions`=`EXTENSION_NAME`,[…] [`--config`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--config-from-file`=`KEY`=`FILE_PATH`,[…]] [`--description`=`DESCRIPTION`] [`--inclusion-labels`=`INCLUSION_LABELS`] [`--priority`=`PRIORITY`; default=1000] [`--rollout-conflict-behavior`=`ROLLOUT_CONFLICT_BEHAVIOR`] [`--rollout-custom-plan`=`ROLLOUT_CUSTOM_PLAN`] [`--rollout-predefined-plan`=`ROLLOUT_PREDEFINED_PLAN`] [`--version`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Compute Engine global VM extension policy. 
EXAMPLES
     To create a global VM extension policy, run: 
    
    
    gcloud beta compute global-vm-extension-policies create test-policy-name --description="test policy" --extensions=extension1,extension2 --version=extension1=version1,extension2=version2 --config=extension1="config1",extension2="config2" --inclusion-labels=env=prod --inclusion-labels=env=preprod,workload=load-test --rollout-predefined-plan=slow_rollout --priority=1000

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the global vm extension policy to create. 
REQUIRED FLAGS
    

`--extensions`=`EXTENSION_NAME`,[…]
     One or more extensions to be added to the policy. 
OPTIONAL FLAGS
    

`--config`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     A comma separated key:value list where the key is the extension name and the value is the desired config for the given extension. The extension name must be one of the extensions specified in the --extensions flag. 

E.g. --config=filestore='filestore config',ops-agent='ops agent config' 

Raises: ArgumentTypeError: If the extension name is not specified in the \--extensions flag. 

`--config-from-file`=`KEY`=`FILE_PATH`,[…]
     Same as --config except that the value for the entry will be read from a local file. The extension name must be one of the extensions specified in the \--extensions flag. 

It is an error to specify the same extension in both --config and \--config-from-file. 

`--description`=`DESCRIPTION`
     An optional text description for the extension policy. 
`--inclusion-labels`=`INCLUSION_LABELS`
     A list of inclusion labels to select the target VMs. 

The expected format for a single selector is "key1=value1,key2=value2". A VM is selected if it has ALL the inclusion labels. 

When the option is specified multiple times, it assumes a logical OR between the selectors. 

For example, if the inclusion labels are ["env=prod,workload=frontend", "workload=backend"], the following VMs will be selected: 

  * VM1: env=prod, workload=frontend, something=else 
  * VM2: env=prod, workload=backend But not: 
  * VM3: env=prod 



If not specified, ALL VMs in the project/folder will be selected. 

`--priority`=`PRIORITY`; default=1000
     The priority of the policy. Lower the number, higher the priority. When two policies try to apply the same extension to a VM, the policy with higher priority takes precedence. If the priorities are the same, the policy with the more recent update timestamp takes precedence. If a policy is deleted, the extension remains installed on the VM if a lower-priority policy still applies. 

Range from 0 to 65535. Default is 1000. 

`--rollout-conflict-behavior`=`ROLLOUT_CONFLICT_BEHAVIOR`
     Specifies the behavior of a rollout if a conflict is detected between a zonal policy and a global policy. See gcloud compute zone-vm-extension-policies for more details on zonal policies. 

The possible values are: 

  * `""`: The zonal policy value is used in case of a conflict. This is the default behavior. 
  * `overwrite`: The global policy overwrites the zonal policy. 



If you set `--rollout-conflict-behavior` to `overwrite` and want to revert to the default behavior, use the update command and omit the `--rollout-conflict-behavior` flag. 

`--rollout-custom-plan`=`ROLLOUT_CUSTOM_PLAN`
     Provide the name of a custom rollout plan to be used for the rollout. 

One of either --rollout-predefined-plan or --rollout-custom-plan must be specified, but not both. 

`--rollout-predefined-plan`=`ROLLOUT_PREDEFINED_PLAN`
     Provide the name of a predefined rollout plan from [fast_rollout, slow_rollout] to be used for the rollout. 

One of either --rollout-predefined-plan or --rollout-custom-plan must be specified, but not both. 

`ROLLOUT_PREDEFINED_PLAN` must be one of: `fast_rollout`, `slow_rollout`. 

`--version`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     A comma separated key:value list where the key is the extension name and the value is the desired version for the given extension. The extension name must be one of the extensions specified in the --extensions flag. If no version is specified for an extension, the latest version will be used and will be upgraded automatically. 

E.g. --version=filestore=123ABC,ops-agent=456DEF 

Raises: ArgumentTypeError: If the extension name is not specified in the \--extensions flag. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute global-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies/create)
    
    
    [gcloud alpha compute global-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/global-vm-extension-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
