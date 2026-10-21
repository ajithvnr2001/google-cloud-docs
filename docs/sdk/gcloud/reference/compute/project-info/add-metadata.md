---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata/
title: gcloud compute project-info add-metadata \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:01:40.159508+00:00
---

# gcloud compute project-info add-metadata  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute project-info add-metadata Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute project-info add-metadata - add or update project-wide metadata 
SYNOPSIS
    

`gcloud compute project-info add-metadata` [`--metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--metadata-from-file`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute project-info add-metadata` can be used to add or update project-wide metadata. Every instance has access to a metadata server that can be used to query metadata that has been set through this tool. Project-wide metadata entries are visible to all instances. To set metadata for individual instances, use `[gcloud compute instances add-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata)`. For information on metadata, see <https://cloud.google.com/compute/docs/metadata>

Only metadata keys that are provided are mutated. Existing metadata entries will remain unaffected. 

If you are using this command to manage SSH keys for your project, please note the [risks](https://docs.cloud.google.com/compute/docs/instances/access-overview#risks) of manual SSH key management as well as the required format for SSH key metadata, available at <https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys>

FLAGS
    

`--metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Metadata to be made available to the guest operating system running on the instances. Each metadata entry is a key/value pair separated by an equals sign. Each metadata key must be unique and have a max of 128 bytes in length. Each value must have a max of 256 KB in length. Multiple arguments can be passed to this flag, e.g., ``\--metadata key-1=value-1,key-2=value-2,key-3=value-3``. The combined total size for all metadata entries is 512 KB. 

In images that have Compute Engine tools installed on them, such as the [official images](https://cloud.google.com/compute/docs/images), the following metadata keys have special meanings: 

`startup-script`
     Specifies a script that will be executed by the instances once they start running. For convenience, ``\--metadata-from-file`` can be used to pull the value from a file. 
`startup-script-url`
     Same as ``startup-script`` except that the script contents are pulled from a publicly-accessible location on the web. For startup scripts on Windows instances, the following metadata keys have special meanings: ``windows-startup-script-url``, ``windows-startup-script-cmd``, ``windows-startup-script-bat``, ``windows-startup-script-ps1``, ``sysprep-specialize-script-url``, ``sysprep-specialize-script-cmd``, ``sysprep-specialize-script-bat``, and ``sysprep-specialize-script-ps1``. For more information, see [Running startup scripts](https://cloud.google.com/compute/docs/startupscript). At least one of [--metadata] or [--metadata-from-file] is required. 
`--metadata-from-file`=`KEY`=`LOCAL_FILE_PATH`,[…]
     Same as ``\--metadata`` except that the value for the entry will be read from a local file. A value can be read from standard input by specifying ``-´´ as the file path. This is useful for values that are too large such as ``startup-script`` contents. At least one of [--metadata] or [--metadata-from-file] is required. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute project-info add-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-info/add-metadata)
    
    
    [gcloud beta compute project-info add-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/project-info/add-metadata)
    
    
    [gcloud preview compute project-info add-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/project-info/add-metadata)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
