---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/zone-vm-extension-policies/create/
title: gcloud alpha compute zone-vm-extension-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:41.079024+00:00
---

# gcloud alpha compute zone-vm-extension-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/zone-vm-extension-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute zone-vm-extension-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute zone-vm-extension-policies create - create a Compute Engine zone VM extension policy 
SYNOPSIS
    

`gcloud alpha compute zone-vm-extension-policies create` `NAME` `--extensions`=`EXTENSION_NAME`,[…] [`--config`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--config-from-file`=`KEY`=`FILE_PATH`,[…]] [`--description`=`DESCRIPTION`] [`--inclusion-labels`=`INCLUSION_LABELS`] [`--priority`=`PRIORITY`; default=1000] [`--version`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Compute Engine zone VM extension policy. 
EXAMPLES
     To create a zone VM extension policy, run: 
    
    
    gcloud alpha compute zone-vm-extension-policies create test-policy-name --description="test policy" --extensions=extension1,extension2 --version=extension1=version1,extension2=version2 --config=extension1="config1",extension2="config2" --inclusion-labels=env=prod --inclusion-labels=env=preprod,workload=load-test --priority=1000
    
    
    Available extensions:
      ops-agent
      google-cloud-sap-extension
      google-cloud-workload-extension

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the zone vm extension policy to create. 
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



If not specified, ALL VMs in the zone will be selected. 

`--priority`=`PRIORITY`; default=1000
     The priority of the policy. Lower the number, higher the priority. When two policies try to apply the same extension to a VM, the policy with higher priority takes precedence. If the priorities are the same, the policy with the more recent update timestamp takes precedence. If a policy is deleted, the extension remains installed on the VM if a lower-priority policy still applies. 

Range from 0 to 65535. Default is 1000. 

`--version`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     A comma separated key:value list where the key is the extension name and the value is the desired version for the given extension. The extension name must be one of the extensions specified in the --extensions flag. If no version is specified for an extension, the latest version will be used and will be upgraded automatically. 

E.g. --version=filestore=123ABC,ops-agent=456DEF 

Raises: ArgumentTypeError: If the extension name is not specified in the \--extensions flag. 

`--zone`=`ZONE`
     Zone of the zone vm extension policy to create. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

The container that owns the policy. Defaults to the project of the active configuration. 

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder that owns the policy, either as a bare ID, `123456`, or as a qualified ID, `folders/123456`. 
`--organization`=`ORGANIZATION`
     Organization that owns the policy, either as a bare ID, `123456`, or as a qualified ID, `organizations/123456`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute zone-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies/create)
    
    
    [gcloud beta compute zone-vm-extension-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/zone-vm-extension-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
