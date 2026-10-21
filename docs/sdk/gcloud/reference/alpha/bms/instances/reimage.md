---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage/
title: gcloud alpha bms instances reimage \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:23:44.786103+00:00
---

# gcloud alpha bms instances reimage  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/reimage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bms instances reimage Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bms instances reimage - reimage a Bare Metal Solution instance 
SYNOPSIS
    

`gcloud alpha bms instances reimage` (`INSTANCE` : `--region`=`REGION`) `--os-image`=`OS_IMAGE` [`--async`] [`--kms-crypto-key-version`=`KMS_CRYPTO_KEY_VERSION`] [`--ssh-keys`=[`SSH_KEYS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Reimage a Bare Metal Solution instance. 

This call returns immediately, but the reimage operation may take several minutes to complete. To check if the operation is complete, use the `describe` command for the instance. 

EXAMPLES
     To reimage an instance called ``my-instance`` in region ``us-central1`` with the OS image code ``RHEL9x``, run: 
    
    
    gcloud alpha bms instances reimage my-instance --region=us-central1 --os-image=RHEL9x

To set KMS key and ssh keys in order to connect the instance. Please use corresponding flags: 
    
    
    gcloud alpha bms instances reimage my-instance --region=us-central1 --os-image=RHEL9x --ssh-keys=ssh-key-1,ssh-key-2 --kms-key-version=sample-kms-key-version

POSITIONAL ARGUMENTS
    

Instance resource - instance. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Region of the resource. 

To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--os-image`=`OS_IMAGE`
     OS image to install on the server. 

To list all OS image codes supported by BMS, run: 
    
    
    [gcloud bms os-images list](https://docs.cloud.google.com/sdk/gcloud/reference/bms/os-images/list)

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--kms-crypto-key-version`=`KMS_CRYPTO_KEY_VERSION`
     Resource ID of a KMS CryptoKeyVersion used to encrypt the initial password. 

<https://cloud.google.com/kms/docs/resource-hierarchy#key_versions>

SSH key resource - ssh_key. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--ssh-keys` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--ssh-keys` on the command line with a fully specified name; 
  * global is the only supported location. 


`--ssh-keys`=[`SSH_KEYS`,…]
     IDs of the SSH keys or fully qualified identifiers for the SSH keys. 

To set the `ssh_key` attribute: 

  * provide the argument `--ssh-keys` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
