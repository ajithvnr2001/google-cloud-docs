---
url: https://docs.cloud.google.com/filestore/docs/access-control/
title: Access control \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:18.458931+00:00
---

# Access control  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Access control Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to control access to Filestore instances.

  * With the [NFSv4.1 protocol](https://docs.cloud.google.com/filestore/docs/configure-nfsv4), you can use Kerberos for securing access to Filestore instances. For more information, see [About supported protocols](https://docs.cloud.google.com/filestore/docs/about-supported-protocols).

  * Alternatively, you can use the Linux options to control NFS access and [Identity and Access Management (IAM)](https://docs.cloud.google.com/filestore/docs/iam) to control access to instance operations, such as creating, editing, viewing, and deleting instances. The following guide walks you through how to complete each of these tasks.




## File share export settings

A Filestore file share is assigned the following default [`/etc/exports`](https://linux.die.net/man/5/exports) settings:

  * The client list—which identifies the clients allowed to connect to the file share—contains every internal IP address in the VPC network you selected for the Filestore instance. Internal IP addresses can be any range listed in [subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges). However, if you have clients on non-[RFC 1918](https://tools.ietf.org/html/rfc1918) subnet ranges, you must explicitly grant them access to the Filestore instance using [IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control).
  * The `rw` option is used, so the file share allows both read and write operations.
  * The user ID mapping option `no_root_squash` is used, so all users and groups, including the root user, are expected to be the same on both the Filestore instance and the client.
  * All other options use the [`/etc/exports`](https://linux.die.net/man/5/exports) defaults.



### Basic-tier instances

Basic SSD and basic HDD instances create an exported share labeled `/config/google-prober`, used to help support internal probing processes, which in turn verify access, durability, or performance. The share is exported to a client list made accessible to the instance IP address only, using the same settings as indicated in the previous section. The share is accessible to probers hosted on or originating from the instance only and is inaccessible outside of the instance. The instance exports the share regardless of whether [IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control) is applied. Users can see the exported share using the `showmount -e` command.

### IP-based access control

You can change these export settings by creating access control rules using the Google Cloud console or by specifying a JSON configuration file during instance creation using the gcloud CLI. For details, see [Configuring IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control).

You can also add new access control rules or modify existing ones after an instance is created. For details, see [Editing instances](https://docs.cloud.google.com/filestore/docs/editing-instances).

## File share permissions

When you create a Filestore instance, the file share for that instance has default POSIX file permissions of `rwxr-xr-x`. These permissions mean that on a Filestore instance, only root users on connected clients have read and write access to the file share. Other users have only read access by default. Client root users can change permissions and owners.

### Configuring access on a file share

When mounting a file share, you can use [mount options](https://linux.die.net/man/8/mount) and [`/etc/fstab`](https://linux.die.net/man/5/fstab) settings to determine whether the file share is writable and if files can be executed on it. After mounting the file share, you can use standard Linux commands like [`chmod`](https://linux.die.net/man/1/chmod), and [`setfacl`](https://linux.die.net/man/1/setfacl) to set file and file share permissions. Only basic tiers support `setfacl`.

### Setting consistent permissions

We strongly recommend that you set consistent permissions for each user on all clients that connect to the same Filestore instance to prevent privilege escalation. If a file share is mounted on more than one client and a user has root privileges on one client but not the others, then the following privilege escalation scenario is possible:

  * A user sets the `setuid` attribute on an executable file from the client where the user has root access.
  * The user then uploads the executable file to the file share.
  * The user executes the uploaded file as root on any client where the user has at least read permission.



This scenario is possible because the `setuid` bit allows the user to execute a file using the permissions of the file owner, which in this case is root.

### Overlapping permissions

Zonal, regional, and enterprise instances now support overlapping permissions.

If two separate access control rules are defined for overlapping IP address subnets, the rule defined for the smaller subnet takes priority.

For example, if a JSON configuration file contains a rule granting read and write access for the IPv4 address subnet `10.0.0.0/24`, and a separate rule grants read-only access for the IPv4 address subnet `10.0.0.0/28`, Filestore recognizes and applies the rule for the smaller subnet first. The other rule is then applied to the remaining portions of the defined IP address subnet. In this example, a client using the IPv4 address `10.0.0.20` is granted read and write permissions, while a client using `10.0.0.12` is granted read-only permissions:
    
    
       {
      "--file-share":
        {
          "capacity": "2048",
          "name": "my_vol",
          "nfs-export-options": [
            {
              "access-mode": "READ_WRITE",
              "ip-ranges": [
                "10.0.0.0/24"
              ],
              "squash-mode": "ROOT_SQUASH",
              "anon_uid": 1003,
              "anon_gid": 1003
            },
             {
              "access-mode": "READ_ONLY",
              "ip-ranges": [
                "10.0.0.0/28"
              ],
              "squash-mode": "NO_ROOT_SQUASH"
            }
          ]
        }
    }
    

Some restrictions apply:

  * Overlapping permissions for identical IPv4 subnets are not supported and return an error.

  * Overlapping permissions are not supported for basic SSD or basic HDD instances.




## What's next

  * [Configure IP-based access control](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control) or see an [example](https://docs.cloud.google.com/filestore/docs/creating-instances#example_2).
  * [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * [Edit instances](https://docs.cloud.google.com/filestore/docs/editing-instances).
  * [Troubleshoot common Filestore networking or connection issues](https://docs.cloud.google.com/filestore/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
