---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/create/
title: gcloud alpha compute migration machine-image-imports create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:56:48.008680+00:00
---

# gcloud alpha compute migration machine-image-imports create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute migration machine-image-imports create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute migration machine-image-imports create - import machine images to Google Compute Engine 
SYNOPSIS
    

`gcloud alpha compute migration machine-image-imports create` (`IMAGE_IMPORT_NAME` : `--location`=`LOCATION`) `--source-file`=`SOURCE_FILE` [`--additional-licenses`=[`ADDITIONAL_LICENSES`,…]] [`--description`=`DESCRIPTION`] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--machine-image-name`=`MACHINE_IMAGE_NAME`] [`--machine-type`=`MACHINE_TYPE`] [`--network-interface`=[`network`=`NETWORK`],[`networkTier`=`NETWORKTIER`],[`subnetwork`=`SUBNETWORK`]] [`--single-region-storage`] [`--tags`=[`TAGS`,…]] [`--target-project`=`TARGET_PROJECT`] [`--enable-integrity-monitoring` `--enable-vtpm` `--secure-boot`=`SECURE_BOOT`] [`--scopes`=[`SCOPES`,…] `--service-account`=`SERVICE_ACCOUNT`] [`--skip-os-adaptation` | `--adaptation-modifiers`=`ADAPTATION_MODIFIERS` `--boot-conversion`=`BOOT_CONVERSION` `--generalize` `--license-type`=`LICENSE_TYPE` `--rootfs-uuid`=`ROOTFS_UUID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha compute migration machine-image-imports create Imports machine images such as OVA and OVF files, from a Google Cloud Storage file (gs://…) to Google Compute Engine, using the Migrate to Virtual Machines service API. This command creates an Image Import resource with a nested Image Import Job resource. The Image Import Job resource tracks the image import progress. To use this command, you must enable VM Migration API in your project. 
EXAMPLES
     To import ub-14.04.5.ova from my-images-bucket to my-target-project in us-central1, create my-image-import resource in my-project in us-central1. Run:
    
    
    gcloud alpha compute migration machine-image-imports create my-machine-image-import --source-file=gs://my-images-bucket/ub-14.04.5.ova --image-name=my-ubuntu-machine-image --location=us-central1 --target-project=projects/my-project/locations/global/targetProjects/my-target-project --project=my-project

POSITIONAL ARGUMENTS
    

Image import resource - The Image Import resource you want to create. This would be the machine image name if --machine-image-name is not given. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `image_import_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`IMAGE_IMPORT_NAME`
     ID of the image_import or fully qualified identifier for the image_import. 

To set the `image_import_name` attribute: 

  * provide the argument `image_import_name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Resource location. 

To set the `location` attribute: 

  * provide the argument `image_import_name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

`--source-file`=`SOURCE_FILE`
     The path to the Google Cloud Storage file from which the image should be imported. 
OPTIONAL FLAGS
    

`--additional-licenses`=[`ADDITIONAL_LICENSES`,…]
     Comma-separated list of the additional licenses to assign to the machine image. 
`--description`=`DESCRIPTION`
     A description of the machine image. 
`--kms-key`=`KMS_KEY`
     Fully qualified identifier for the Cloud KMS (Key Management Service) cryptokey that will be used to protect the image. 
`--labels`=[`KEY`=`VALUE`,…]
     A map of labels to associate with the machine image. 
`--machine-image-name`=`MACHINE_IMAGE_NAME`
     The name of the machine image that will be imported to Google Compute Engine. Default is the Image Import name. 
`--machine-type`=`MACHINE_TYPE`
     The machine type to create the machine image with. If not provided, the service will choose a relevant machine type series based on the information from the source image. 
`--network-interface`=[`network`=`NETWORK`],[`networkTier`=`NETWORKTIER`],[`subnetwork`=`SUBNETWORK`]
     The network interface to use for the instance created by the machine image. This is a dicionary with the following keys: 

  * network: The network to use for this network interface. 
  * subnetwork: The subnetwork to use for this network interface. 
  * network-tier: The network tier to use for this network interface. This argument can be specified multiple times in case of multiple nics. 


`--single-region-storage`
     If true, the location of the imported machine image will be the region of the import job. Otherwise the closest multi-region is selected. Default is false. 
`--tags`=[`TAGS`,…]
     The tags to apply to the instance created by the machine image. 
`--target-project`=`TARGET_PROJECT`
     The target project resource path to which the machine image will be imported. Default is the host project. To get a list of the target projects run the gcloud alpha migration vms target-projects list command. 
Shielded instance configuration. 
`--enable-integrity-monitoring`
     Defines whether the instance created by the machine image has integrity monitoring enabled. This can be set to true only if the image boot option is EFI, and vTPM is enabled. 
`--enable-vtpm`
     Defines whether the instance created by the machine image has vTPM enabled. This can be set to true only if the image boot option is EFI. 
`--secure-boot`=`SECURE_BOOT`
     Defines whether the instance created by the machine image has Secure Boot enabled. This can be set to true only if the image boot option is EFI. If not specified we will use the configuration of the source. `SECURE_BOOT` must be one of: `false`, `secure-boot-unspecified`, `true`. 
The service account to assign to the instance created by the machine image. 
`--scopes`=[`SCOPES`,…]
     The list of scopes to be made available for the service account. 
`--service-account`=`SERVICE_ACCOUNT`
     The email address of the service account. 
OS adaptation parameters. 

At most one of these can be specified: 

`--skip-os-adaptation`
     If true, skip OS adaptation. Default false. 
Or at least one of these can be specified: 

`--adaptation-modifiers`=`ADAPTATION_MODIFIERS`
     A map of flags to pass to the OS adaptation process. The actual value depends on the modifier and can also be empty. e.g. \--adaptation-modifiers=flag1=value1,flag2 
`--boot-conversion`=`BOOT_CONVERSION`
     This property will trigger an internal process which will convert the image from using the existing boot option to another. The size of the boot disk might be increased to allow the conversion. Currently only support BIOS_TO_EFI. `BOOT_CONVERSION` must be one of: `bios-to-efi`, `boot-conversion-unspecified`, `none`. 
`--generalize`
     If true, generalize the imported machine image. Default false. The generalization process enables co-existence of multiple VMs created from the same machine image. For Windows, generalizing the machine image removes computer-specific information such as installed drivers and the computer security identifier (SID). 
`--license-type`=`LICENSE_TYPE`
     The license to use post migration. `LICENSE_TYPE` must be one of: `compute-engine-license-type-byol`, `compute-engine-license-type-default`, `compute-engine-license-type-payg`. 
`--rootfs-uuid`=`ROOTFS_UUID`
     Identifies the file system to adapt. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vmmigration/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/migrate/virtual-machines>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud compute migration machine-image-imports create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/migration/machine-image-imports/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
