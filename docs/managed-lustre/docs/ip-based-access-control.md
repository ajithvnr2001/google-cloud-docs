---
url: https://docs.cloud.google.com/managed-lustre/docs/ip-based-access-control/
title: IP-based access control \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:29.342166+00:00
---

# IP-based access control  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/ip-based-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  IP-based access control Stay organized with collections  Save and categorize content based on your preferences. 

Managed Lustre provides IP-based access control through the root squash feature.

Root squash is a security feature that prevents a root user on a client VM from having root privileges on a Managed Lustre file system. When a root user accesses the Managed Lustre file system, their privileges are "squashed" down to those of a less-privileged user.

Root squash can be configured for a new Managed Lustre instance or for an existing one. You can apply a default root squash setting to all clients, or specify custom rules for certain clients.

By default, root squash is not configured on a Managed Lustre instance.

## Security limitations and recommendations

### Restrict root access on client VMs

The best mechanism to restrict root access is to disallow users from being root in the first place. Granting users root privileges on a VM can expose you to persistence risks: users might abuse these privileges to create new user accounts or install backdoors to maintain persistent access to the VM. See [Best practices for controlling SSH login access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access#limit-root-privileges) for instructions on how to restrict root access.

If you're unable to prevent users from having root privileges on VMs, Managed Lustre's IP-based access control feature can restrict root user privileges when accessing Managed Lustre instances. However, these access checks are best effort and this feature is not intended to be a security guarantee. You should rely on [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) as your primary security perimeter and ensure only trusted client VMs using trusted VM images have network access to your Managed Lustre instances. See [Google Cloud security best practices](https://cloud.google.com/security/best-practices) for more information.

### Disable IP forwarding

The default Compute Engine configuration allows instances to enable IP forwarding. To prevent users from circumventing root squash policies by impersonating a different source IP address, you should disable IP forwarding using the `constraints/compute.vmCanIpForward` organization policy. See [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) for instructions.

## Configure default root squash

To apply root squash to all clients that connect to the instance, specify a default squash UID and GID, and set the squash mode to `ROOT_SQUASH`. A commonly used value for UID and GID is `65534`, which translates to the `nobody` user.

Note that by default a `nobody` user is limited to read and execute access only. Only root users and members of the `Owner` group have write access to the file system.

### Create instance

To create an instance with default root squash:

###  gcloud 

Use the `--default-squash-mode`, `--default-squash-uid`, and `--default-squash-gid` flags to set the default values:
    
    
    gcloud lustre instances create INSTANCE_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --network=NETWORK_NAME \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY \
      --filesystem=FS_NAME \
      --default-squash-mode=ROOT_SQUASH \
      --default-squash-uid=UID \
      --default-squash-gid=GID
    

Where:

  * `--default-squash-mode` is `ROOT_SQUASH`.
  * `--default-squash-uid` and `--default-squash-gid` specify the default IDs to which to convert root users.



For a full list and description of available fields when creating an instance, see the [`gcloud lustre instances create` reference](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/create).

###  REST 

To create an instance using the REST API, send a request to the following endpoint and include an `accessRulesOptions` object:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances?instanceId=INSTANCE_NAME
    Authorization: Bearer AUTH_TOKEN
    {
      "filesystem": "FS_NAME",
      "perUnitStorageThroughput": "PER_UNIT_STORAGE_THROUGHPUT",
      "capacityGib": "CAPACITY_GIB",
      "network": "NETWORK",
      "accessRulesOptions": {
        "defaultSquashMode": "SQUASH_MODE",
        "defaultSquashUid": UID,
        "defaultSquashGid": GID
      }
    }
    

Where:

  * `defaultSquashMode` is `ROOT_SQUASH`.
  * `defaultSquashUid` and `defaultSquashGid` are the user and group ID values to which to convert root users.



For details on creating an instance using the REST API, see the [`projects.locations.instances.create` API reference](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/create).

###  Google Cloud console 

Root squash cannot be configured using the Google Cloud console.

### Update instance

To update an existing instance to use default root squash:

###  gcloud 

Use the `--default-squash-mode`, `--default-squash-uid`, and `--default-squash-gid` flags to set the default values:
    
    
    gcloud lustre instances update INSTANCE_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --default-squash-mode=ROOT_SQUASH \
      --default-squash-uid=UID \
      --default-squash-gid=GID
    

Where:

  * `--default-squash-mode` is `ROOT_SQUASH`.
  * `--default-squash-uid` and `--default-squash-gid` specify the default IDs to which to squash root users.



###  REST 

To update an instance using the REST API, send a PATCH request to its specific endpoint. You must specify `accessRulesOptions` in the `updateMask`:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME?updateMask=accessRulesOptions
    Authorization: Bearer AUTH_TOKEN
    
    {
      "accessRulesOptions": {
        "defaultSquashMode": "ROOT_SQUASH",
        "defaultSquashUid": UID,
        "defaultSquashGid": GID
      }
    }
    

Where:

  * `defaultSquashMode` is `ROOT_SQUASH`.
  * `defaultSquashUid` and `defaultSquashGid` are the user and group ID values to which to convert root users.



For more information about updating an instance, see [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  Google Cloud console 

Root squash cannot be configured using the Google Cloud console.

## Configure root squash with exceptions

To apply root squash to all clients except a specific set of trusted clients, specify an **access rule**. This rule specifies the default UID and GID to squash root users to, plus a rule that exempts certain clients from being squashed based on their IP address or address ranges.

A commonly used value for the squash UID and GID is `65534`, which translates to the `nobody` user. Note that the `nobody` user does not have write access to the file system. Only root users and members of the `Owner` group have read, write and execute access. Other users are limited to read and execute access only.

### Create an instance

###  gcloud 

To create an instance:
    
    
    gcloud lustre instances create INSTANCE_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --network=NETWORK_NAME \
      --per-unit-storage-throughput=PER_UNIT_STORAGE_THROUGHPUT \
      --capacity-gib=CAPACITY \
      --filesystem=FS_NAME \
      --default-squash-mode=ROOT_SQUASH \
      --default-squash-uid=UID \
      --default-squash-gid=GID \
      --access-rules=name="ACCESS_RULE_NAME",ipAddressRanges="IP_ADDRESS_OR_CIDR_RANGE",squashMode=NO_SQUASH
    

Where:

  * `--default-squash-mode` is `ROOT_SQUASH`.
  * `--default-squash-uid` and `--default-squash-gid` specify the default IDs to which to squash root users.
  * `--access-rules` specifies the exceptions to root squash. The following values must be specified: 
    * `name` is the name for this access rule.
    * `ipAddressRanges` is a comma-separated list of one or more IP addresses or CIDR ranges that don't overlap. Ranges are specified in the following format: `192.168.0.0/24`.
    * `squashMode` must be `NO_SQUASH`.



For a full list and description of available fields, see [Create a Managed Lustre instance](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/create).

###  REST 

To create an instance using the REST API, send a request to the following endpoint and include an `accessRulesOptions` object:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances?instanceId=INSTANCE_NAME
    Authorization: Bearer AUTH_TOKEN
    {
      "filesystem": "FS_NAME",
      "perUnitStorageThroughput": "PER_UNIT_STORAGE_THROUGHPUT",
      "capacityGib": "CAPACITY_GIB",
      "network": "NETWORK",
      "accessRulesOptions": {
        "accessRules": [
          {
            "name": "ACCESS_RULE_NAME",
            "ipAddressRanges": [
              "IP_ADDRESS_OR_CIDR_RANGE_1",
              "IP_ADDRESS_OR_CIDR_RANGE_2"
            ],
            "squashMode": "NO_SQUASH"
          }
        ],
        "defaultSquashMode": "SQUASH_MODE",
        "defaultSquashUid": UID,
        "defaultSquashGid": GID
      }
    }
    

When setting a specific access rule, the following fields are required:

  * `name` is a user-defined name for this rule. It must use only alphanumeric characters and underscores (`_`) and be 16 characters or less.

  * `ipAddressRanges` is a list of one or more IP addresses or CIDR ranges that don't overlap. Ranges are specified in the following format: `192.168.0.0/24`.

  * `squashMode` is always `NO_SQUASH`.

  * `defaultSquashMode` is `ROOT_SQUASH`.

  * `defaultSquashUid` and `defaultSquashGid` are the user and group ID values to which to convert root users who don't match any specific access rules.




For example, to set a default root squash with an exception for root users from a specific range of IP addresses and a particular IP address, the `accessRulesOptions` object looks like the following:
    
    
    {
      "accessRulesOptions": {
        "accessRules": [
          {
            "name": "dont_squash",
            "ipAddressRanges": [
              "192.100.1.10",
              "192.168.0.0/24"
            ],
            "squashMode": "NO_SQUASH"
          }
        ],
        "defaultSquashMode": "ROOT_SQUASH",
        "defaultSquashUid": 65534,
        "defaultSquashGid": 65534
      }
    }
    

For details on creating an instance using the REST API, see [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/create).

###  Google Cloud console 

Root squash cannot be configured using the Google Cloud console.

### Update an instance

###  gcloud 

To update an instance:
    
    
    gcloud lustre instances update INSTANCE_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --default-squash-mode=ROOT_SQUASH \
      --default-squash-uid=UID \
      --default-squash-gid=GID \
      --access-rules=name="ACCESS_RULE_NAME",ipAddressRanges="IP_ADDRESS_OR_CIDR_RANGE",squashMode=NO_SQUASH
    

Where:

  * `--default-squash-mode` is `ROOT_SQUASH`.
  * `--default-squash-uid` and `--default-squash-gid` specify the default IDs to which to squash root users.
  * `--access-rules` specifies the exceptions to root squash. The following values must be specified: 
    * `name` is the name for this access rule.
    * `ipAddressRanges` is a comma-separated list of one or more IP addresses or CIDR ranges that don't overlap. Ranges are specified in the following format: `192.168.0.0/24`.
    * `squashMode` must be `NO_SQUASH`.



For more information about updating an instance, see [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  REST 

To update an instance using the REST API, send a PATCH request to its specific endpoint. You must specify `accessRulesOptions` as the value of `updateMask` in the endpoint URL:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME?updateMask=accessRulesOptions
    Authorization: Bearer AUTH_TOKEN
    
    {
      "accessRulesOptions": {
        "accessRules": [
          {
            "name": "ACCESS_RULE_NAME",
            "ipAddressRanges": [
              "IP_ADDRESS_OR_CIDR_RANGE_1",
              "IP_ADDRESS_OR_CIDR_RANGE_2"
            ],
            "squashMode": "NO_SQUASH"
          }
        ],
        "defaultSquashMode": "SQUASH_MODE",
        "defaultSquashUid": UID,
        "defaultSquashGid": GID
      }
    }
    

For more information about updating an instance, see [Manage instances](https://docs.cloud.google.com/managed-lustre/docs/instances#update_an_instance).

###  Google Cloud console 

Root squash cannot be configured using the Google Cloud console.

## Remove root squash from an instance

To remove all root squash settings from an instance, update the instance to clear the access rules and set the default mode to `NO_SQUASH`.

###  gcloud 
    
    
    gcloud lustre instances update INSTANCE_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --default-squash-mode=NO_SQUASH \
      --clear-access-rules \
      --default-squash-uid=0 --default-squash-gid=0
    

###  REST 
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME?updateMask=accessRulesOptions
    Authorization: Bearer AUTH_TOKEN
    
    {
      "accessRulesOptions": {
        "defaultSquashMode": "NO_SQUASH"
      }
    }
    

###  Google Cloud console 

Root squash cannot be configured using the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
