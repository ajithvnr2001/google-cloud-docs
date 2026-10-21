---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/create-instance/
title: gcloud beta compute instance-groups managed create-instance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:28:42.128741+00:00
---

# gcloud beta compute instance-groups managed create-instance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instance-groups managed create-instance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instance-groups managed create-instance - create a new virtual machine instance in a managed instance group with a defined name and optionally its stateful configuration 
SYNOPSIS
    

`gcloud beta compute instance-groups managed create-instance` `NAME` `--instance`=`INSTANCE` [`--stateful-disk`=[`auto-delete`=`AUTO-DELETE`],[`device-name`=`DEVICE-NAME`],[`mode`=`MODE`],[`source`=`SOURCE`]] [`--stateful-external-ip`=[`address`=`ADDRESS`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`--stateful-internal-ip`=[`address`=`ADDRESS`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]] [`--stateful-metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instance-groups managed create-instance` creates a virtual machine instance with a defined name and optionally its stateful configuration: stateful disk, stateful metadata key-values, and stateful IP addresses. Stateful configuration is stored in the corresponding newly created per-instance config. An instance with a per-instance config will preserve its given name, specified disks, specified metadata key-values, and specified internal and external IPs during instance recreation, auto-healing, updates, and any other lifecycle transitions of the instance. 

For regional managed instance groups, if only the name is provided, the instance will be created in the default zone (REGION-a) of the region. To specify a different zone, use the partial URI in the `--instance` flag (e.g., 'zones/ZONE/instances/INSTANCE_NAME'). 

EXAMPLES
     To create an instance `instance-1` in `my-group` (in region europe-west4) with metadata `my-key: my-value`, a disk `disk-1` attached to it as the device `device-1`, stateful internal IP `192.168.0.10` on the default interface (nic0), and existing address reservation `my-address` for stateful external IP on interface `nic1`, run: 
    
    
    gcloud beta compute instance-groups managed create-instance my-group --region=europe-west4 --instance=instance-1 --stateful-disk='device-name=foo,source=https://compute.googleapis.com/compute/alpha/projects/my-project/zones/europe-west4/disks/disk-1,mode=rw,auto-delete=on-permanent-instance-deletion' --stateful-metadata='my-key=my-value' --stateful-internal-ip=address=192.168.0.10,auto-delete=on-permanent-instance-deletion --stateful-external-ip=address=/projects/example-project/regions/europe-west4/addresses/my-address,interface-name=nic1

To create an instance `instance-1` in `my-group` (in region europe-west4) in a specific zone `europe-west4-b`, run: 
    
    
    gcloud beta compute instance-groups managed create-instance my-group --region=europe-west4 --instance=zones/europe-west4-b/instances/instance-1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the managed instance group to create instance in. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`
     Name of the new instance to create. 

For regional managed instance groups, if only the name is provided, the instance will be created in the default zone (REGION-a) of the region. To specify a different zone, use the partial URI (e.g. 'zones/ZONE/instances/INSTANCE_NAME'). 

OPTIONAL FLAGS
    

`--stateful-disk`=[`auto-delete`=`AUTO-DELETE`],[`device-name`=`DEVICE-NAME`],[`mode`=`MODE`],[`source`=`SOURCE`]
     Disks considered stateful by the instance group. Managed instance groups preserve and reattach stateful disks on VM autohealing, update, and recreate events. 

You can also attach and preserve disks, not defined in the group's instance template, to a given instance. 

The same disk can be attached to more than one instance but only in read-only mode. 

`--stateful-external-ip`=[`address`=`ADDRESS`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]
     Managed instance groups preserve stateful IPs on VM autohealing, update, and recreate events. 

Use this argument multiple times to update more IPs. 

If a stateful external IP with the given interface name already exists in the current instance configuration, its properties are replaced by the newly provided ones. Otherwise, a new stateful external IP definition is added to the instance configuration. 

`interface-name`
     (Optional) Network interface name. If omitted, the default network interface named ``nic0`` is assumed. 
    
    
    *address*::: Static IP address to assign to the instance in one of
    the following formats:

\+ Address: URL of a static IP address reservation. For example: ``projects/example-project/regions/us-east1/addresses/example-ip-name``. 

\+ Literal: For example: ``130.211.181.55``. 

If the provided IP address is not yet reserved, the managed instance group automatically creates the corresponding IP address reservation. If the provided IP address is reserved, the group assigns the reservation to the instance. 

`auto-delete`
     (Optional) Prescribes what should happen to an associated static Address resource when a VM instance is permanently deleted. Regardless of the value of the delete rule, stateful IP addresses are always preserved on instance autohealing, update, and recreation operations. The following options are available: 

  * ``never``: (Default) Never delete the static IP address. Instead, unassign the address when its instance is permanently deleted and keep the address reserved. 
  * ``on-permanent-instance-deletion``: Delete the static IP address reservation when the instance that it's assigned to is permanently deleted from the instance group; for example, when the instance is deleted manually or when the group size is decreased. 


`--stateful-internal-ip`=[`address`=`ADDRESS`],[`auto-delete`=`AUTO-DELETE`],[`interface-name`=`INTERFACE-NAME`]
     Managed instance groups preserve stateful IPs on VM autohealing, update, and recreate events. 

Use this argument multiple times to update more IPs. 

If a stateful internal IP with the given interface name already exists in the current instance configuration, its properties are replaced by the newly provided ones. Otherwise, a new stateful internal IP definition is added to the instance configuration. 

`interface-name`
     (Optional) Network interface name. If omitted, the default network interface named ``nic0`` is assumed. 
    
    
    *address*::: Static IP address to assign to the instance in one of
    the following formats:

\+ Address: URL of a static IP address reservation. For example: ``projects/example-project/regions/us-east1/addresses/example-ip-name``. 

\+ Literal: For example: ``130.211.181.55``. 

If the provided IP address is not yet reserved, the managed instance group automatically creates the corresponding IP address reservation. If the provided IP address is reserved, the group assigns the reservation to the instance. 

`auto-delete`
     (Optional) Prescribes what should happen to an associated static Address resource when a VM instance is permanently deleted. Regardless of the value of the delete rule, stateful IP addresses are always preserved on instance autohealing, update, and recreation operations. The following options are available: 

  * ``never``: (Default) Never delete the static IP address. Instead, unassign the address when its instance is permanently deleted and keep the address reserved. 
  * ``on-permanent-instance-deletion``: Delete the static IP address reservation when the instance that it's assigned to is permanently deleted from the instance group; for example, when the instance is deleted manually or when the group size is decreased. 


`--stateful-metadata`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Additional metadata to be made available to the guest operating system in addition to the metadata defined in the instance template. 

Stateful metadata may be used to define a key/value pair specific for the one given instance to differentiate it from the other instances in the managed instance group. 

Stateful metadata key/value pairs are preserved on instance recreation, autohealing, updates, and any other lifecycle transitions of the instance. 

Stateful metadata have priority over the metadata defined in the instance template. This means that stateful metadata that is defined for a key that already exists in the instance template overrides the instance template value. 

Each metadata entry is a key/value pair separated by an equals sign. Metadata keys must be unique and less than 128 bytes in length. Multiple entries can be passed to this flag, e.g., ``\--stateful-metadata key-1=value-1,key-2=value-2,key-3=value-3``. 

At most one of these can be specified: 

`--region`=`REGION`
     Region of the managed instance group to create instance in. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the managed instance group. This flag is only applicable for zonal managed instance groups. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instance-groups managed create-instance](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance)
    
    
    [gcloud alpha compute instance-groups managed create-instance](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/create-instance)
    
    
    [gcloud preview compute instance-groups managed create-instance](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/create-instance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
