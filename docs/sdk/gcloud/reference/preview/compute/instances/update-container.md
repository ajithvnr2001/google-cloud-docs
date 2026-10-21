---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/update-container/
title: gcloud preview compute instances update-container \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:51:35.376036+00:00
---

# gcloud preview compute instances update-container  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/update-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instances update-container Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instances update-container - updates Compute Engine virtual machine instances running container images 
SYNOPSIS
    

`gcloud preview compute instances update-container` `INSTANCE_NAME` [`--container-image`=`CONTAINER_IMAGE`] [`--container-mount-disk`=[`mode`=`MODE`],[`mount-path`=`MOUNT-PATH`],[`name`=`NAME`],[`partition`=`PARTITION`]] [`--container-privileged`] [`--container-restart-policy`=`POLICY`] [`--container-stdin`] [`--container-tty`] [`--[no-]shielded-integrity-monitoring`] [`--shielded-learn-integrity-policy`] [`--[no-]shielded-secure-boot`] [`--[no-]shielded-vtpm`] [`--zone`=`ZONE`] [`--clear-container-args` | `--container-arg`=`CONTAINER_ARG`] [`--clear-container-command` | `--container-command`=`CONTAINER_COMMAND`] [`--container-env`=[`KEY`=`VALUE`, …,…] `--container-env-file`=`CONTAINER_ENV_FILE` `--remove-container-env`=[`KEY`,…]] [`--container-mount-host-path`=[`host-path`=`HOSTPATH`,`mount-path`=`MOUNTPATH`[,`mode`=`MODE`],…] `--container-mount-tmpfs`=[`mount-path`=`MOUNTPATH`,…] `--remove-container-mounts`=[`MOUNTPATH`[,`MOUNTPATH`,…],…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `(DEPRECATED)` The option to deploy a container during VM creation using the container startup agent is deprecated. Use alternative services to run containers on your VMs. Learn more at <https://cloud.google.com/compute/docs/containers/migrate-containers>. 

`gcloud preview compute instances update-container` updates Compute Engine virtual machines that runs a Docker image. For example: 
    
    
    gcloud preview compute instances update-container instance-1 --zone us-central1-a         --container-image=gcr.io/google-containers/busybox

updates an instance called instance-1, in the us-central1-a zone, to run the 'busybox' image. 

For more examples, refer to the `EXAMPLES` section below. 

EXAMPLES
     To run the gcr.io/google-containers/busybox image on an instance named 'instance-1' that executes 'echo "Hello world"' as a run command, run: 
    
    
    gcloud preview compute instances update-container instance-1 --container-image=gcr.io/google-containers/busybox --container-command='echo "Hello world"'

To run the gcr.io/google-containers/busybox image in privileged mode, run: 
    
    
    gcloud preview compute instances update-container instance-1 --container-image=gcr.io/google-containers/busybox --container-privileged

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to update. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--container-image`=`CONTAINER_IMAGE`
     Sets container image in the declaration to the specified value. 

Empty string is not allowed. 

`--container-mount-disk`=[`mode`=`MODE`],[`mount-path`=`MOUNT-PATH`],[`name`=`NAME`],[`partition`=`PARTITION`]
     Mounts a disk to the container by using mount-path or updates how the volume is mounted if the same mount path has already been declared. The disk must already be attached to the instance with a device-name that matches the disk name. Multiple flags are allowed. 

`name`
     Name of the disk. Can be omitted if exactly one additional disk is attached to the instance. The name of the single additional disk will be used by default. 
`mount-path`
     Path on container to mount to. Mount paths with spaces and commas (and other special characters) are not supported by this command. 
`partition`
     Optional. The partition of the disk to mount. Multiple partitions of a disk can be mounted. 
`mode`
     Volume mount mode: `rw` (read/write) or `ro` (read-only). Defaults to `rw`. Fails if the disk mode is `ro` and volume mount mode is `rw`. 
`--container-privileged`
     Sets permission to run container to the specified value. 
`--container-restart-policy`=`POLICY`
     Sets container restart policy to the specified value. `POLICY` must be one of: `never`, `on-failure`, `always`. 
`--container-stdin`
     Sets configuration whether to keep container `STDIN` always open to the specified value. 
`--container-tty`
     Sets configuration whether to allocate a pseudo-TTY for the container to the specified value. 
`--[no-]shielded-integrity-monitoring`
     Enables monitoring and attestation of the boot integrity of the instance. The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created. This baseline can be updated by using `gcloud compute instances update-container --shielded-learn-integrity-policy`. On Shielded VM instances, integrity monitoring is enabled by default. For information about how to modify Shielded VM options, see <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>. For information about monitoring integrity on Shielded VM instances, see https://cloud.google.com/compute/docs/instances/integrity-monitoring." Changes to this setting with the update command only take effect after stopping and starting the instance. Use `--shielded-integrity-monitoring` to enable and `--no-shielded-integrity-monitoring` to disable. 
`--shielded-learn-integrity-policy`
     Causes the instance to re-learn the integrity policy baseline using the current instance configuration. Use this flag after any planned boot-specific changes in the instance configuration, like kernel updates or kernel driver installation. 
`--[no-]shielded-secure-boot`
     The instance boots with secure boot enabled. On Shielded VM instances, Secure Boot is not enabled by default. For information about how to modify Shielded VM options, see <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>. Changes to this setting with the update command only take effect after stopping and starting the instance. Use `--shielded-secure-boot` to enable and `--no-shielded-secure-boot` to disable. 
`--[no-]shielded-vtpm`
     The instance boots with the TPM (Trusted Platform Module) enabled. A TPM is a hardware module that can be used for different security operations such as remote attestation, encryption, and sealing of keys. On Shielded VM instances, vTPM is enabled by default. For information about how to modify Shielded VM options, see <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>. Changes to this setting with the update command only take effect after stopping and starting the instance. Use `--shielded-vtpm` to enable and `--no-shielded-vtpm` to disable. 
`--zone`=`ZONE`
     Zone of the instance to update. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--clear-container-args`
     Removes the list of arguments from container declaration. 

Cannot be used in the same command with `--container-arg`. 

`--container-arg`=`CONTAINER_ARG`
     Completely replaces the list of arguments with the new list. Each argument must have a separate --container-arg flag. Arguments are appended the new list in the order of flags. 

Cannot be used in the same command with `--clear-container-arg`. 

At most one of these can be specified: 

`--clear-container-command`
     Removes command from container declaration. 

Cannot be used in the same command with `--container-command`. 

`--container-command`=`CONTAINER_COMMAND`
     Sets command in the declaration to the specified value. Empty string is not allowed. 

Cannot be used in the same command with `--clear-container-command`. 

`--container-env`=[`KEY`=`VALUE`, …,…]
     Update environment variables `KEY` with value `VALUE` passed to container. 

  * Sets `KEY` to the specified value. 
  * Adds `KEY` = `VALUE`, if `KEY` is not yet declared. 
  * Only the last value of `KEY` is taken when `KEY` is repeated more than once. 



Values, declared with `--container-env` flag override those with the same `KEY` from file, provided in `--container-env-file`. 

`--container-env-file`=`CONTAINER_ENV_FILE`
     Update environment variables from a file. Same update rules as for `--container-env` apply. Values, declared with `--container-env` flag override those with the same `KEY` from file. 

File with environment variables declarations in format used by docker (almost). This means: 

  * Lines are in format KEY=VALUE 
  * Values must contain equality signs. 
  * Variables without values are not supported (this is different from docker format). 
  * If # is first non-whitespace character in a line the line is ignored as a comment. 


`--remove-container-env`=[`KEY`,…]
     Removes environment variables `KEY` from container declaration Does nothing, if a variable is not present. 
`--container-mount-host-path`=[`host-path`=`HOSTPATH`,`mount-path`=`MOUNTPATH`[,`mode`=`MODE`],…]
     Mounts a volume by using host-path. 

  * Adds a volume, if `mount-path` is not yet declared. 
  * Replaces a volume, if `mount-path` is declared. All parameters (`host-path`, `mount-path`, `mode`) are completely replaced. 



`host-path`
     Path on host to mount from. 
`mount-path`
     Path on container to mount to. Mount paths with spaces and commas (and other special characters) are not supported by this command. 
`mode`
     Volume mount mode: rw (read/write) or ro (read-only). 

Default: rw. 

`--container-mount-tmpfs`=[`mount-path`=`MOUNTPATH`,…]
     Mounts empty tmpfs into container at MOUNTPATH. 

`mount-path`
     Path on container to mount to. Mount paths with spaces and commas (and other special characters) are not supported by this command. 
`--remove-container-mounts`=[`MOUNTPATH`[,`MOUNTPATH`,…],…]
     Removes volume mounts (`host-path`, `tmpfs`, `disk`) with `mountPath: MOUNTPATH` from container declaration. 

Does nothing, if a volume mount is not declared. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances update-container](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-container)
    
    
    [gcloud alpha compute instances update-container](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-container)
    
    
    [gcloud beta compute instances update-container](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/update-container)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
