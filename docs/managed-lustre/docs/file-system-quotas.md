---
url: https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas/
title: File system quotas \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:57.643581+00:00
---

# File system quotas  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  File system quotas Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Lustre file systems support user, group, and project quotas, allowing administrators to manage storage consumption and ensure fair resource allocation. This document explains how to configure, view, and manage these quotas.

**Note:** File system quota is different than Managed Lustre storage capacity quota (the maximum total capacity of the instances that can be created in the project). To learn about storage capacity quota, see [Quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas).

## What are file system quotas?

Quotas in Managed Lustre allow you to set limits on the amount of disk space and the number of files that users, groups, or projects can consume within your file system.

Quotas are applied to different entities:

  * **User quotas** limit the storage consumed by an individual non-root user.
  * **Group quotas** limit the storage consumed by all non-root members of a specific group.
  * **Project quotas** limit the storage consumed by files and directories associated with a particular project ID. This project ID is a Lustre file system identifier, defined using `lfs project`, and is not your Google Cloud project ID. See Set a project quota for more information.



Quotas are configured for two resource types:

  * **Block limits** are a limit on the amount of disk space that can be used.
  * **Inode limits** are a limit on the number of files and directories that can be created.



Each resource type can have two levels of limits:

  * A **soft limit** is a quota threshold that triggers a configurable grace period when exceeded. During this grace period, users, groups, or projects can temporarily exceed the soft limit, up to the hard limit if one exists, giving them time to reduce usage before being blocked. Once the grace period expires, if the usage is still above the soft limit, the soft limit is enforced as a hard limit, blocking all new writes until the disk space or inode count falls below the soft limit.

By default, the grace period is one week.

  * A **hard limit** defines the absolute maximum. If this limit is reached, any further write operations fail, returning a "Disk quota exceeded" error.




## Administering users and groups

Lustre relies on the client's POSIX attributes for user and group names and IDs.

When a client makes a file system request, it sends the local UID and GID to the Lustre servers. The servers use these POSIX attributes to enforce standard file permissions and track quota usage.

For consistent behavior in a multi-user environment, all clients mounting the Lustre file system must have synchronized UID and GID mappings, typically managed through a centralized service like LDAP or NIS.

Root users are not subject to quotas. Commands run with `sudo` also bypass quota checks.

## Before you begin

To manage Lustre quotas, you need:

  * Client access to an active Google Cloud Managed Lustre file system.
  * `sudo` or root privileges on the client system to execute `lfs` commands.



## Set quotas

Use the `lfs setquota` command to configure block and inode limits. You can specify just block limits, just inode limits, or both; likewise you can specify hard limits, soft limits, or both.
    
    
    sudo lfs setquota -u | g | p | U | G | P UGP_VALUE \
          -b SOFT_BLOCK_LIMIT -B HARD_BLOCK_LIMIT \
          -i SOFT_INODE_LIMIT -I HARD_INODE_LIMIT \
          MOUNT_DIR
    

Where:

  * `-u` specifies a user by username or UID. Lustre resolves usernames using the client's POSIX attributes.
  * `-g` specifies a group by group name or GID. Lustre resolves group names using the client's POSIX attributes.
  * `-p` specifies a project by project name or project ID. If specifying a project name, it must be mapped to a project ID using a mapping file such as `/etc/projid` on the client.
  * `U`, `G`, and `P` set the default quota for any users, groups, or projects that have no specific quota set.
  * UGP_VALUE is the username, group name, project name, UID, GID, or project ID. IDs must be integers between `0` and `4294967295`. Omit this value if you're specifying default user, group, or project quotas.
  * `-b` and `-B` are soft and hard limits for block usage, respectively. Soft limits should be smaller than hard limits. Values can be specified in bytes (`B`), kilobytes (`K`), megabytes (`M`), gigabytes (`G`), or terabytes (`T`). The default unit is kilobytes.
  * `-i` and `-I` are soft and hard limits for inode usage. Soft limits should be smaller than hard limits.
  * MOUNT_DIR is the mount point of the Managed Lustre file system.



Note that you cannot configure the grace period at the same time as creating a quota. The default grace period for soft limits is one week. To update the grace period, see Configure grace periods.

### Examples

#### Set a user quota

Set a soft block limit of 100 GB, a hard block limit of 120 GB, a soft inode limit of 10,000, and a hard inode limit of 12,000 for `user1` on `/mnt/lustre`:
    
    
    sudo lfs setquota -u user1 -b 100G -B 120G -i 10000 -I 12000 /mnt/lustre
    

#### Set a group quota

Set a hard block limit of 50 TB for `groupA` on `/mnt/lustre`:
    
    
    sudo lfs setquota -g groupA -B 50T /mnt/lustre
    

#### Set a project quota

Project quotas require an additional step to associate directories and files with a project ID:

  1. Use the `lfs project` command to assign a project ID. This ID is an arbitrary integer that identifies the project.
         
         sudo lfs project -spr LFS_PROJECT_ID PATH/TO/DIR/OR/FILE
         

Where:

     * `-s` sets inheritance, so that new files and directories created in the specified directory inherit the project ID.
     * `-p` tells the command to set the given project ID on the specified file or directory.
     * `-r` applies the project ID recursively to all child directories and files.
     * PATH/TO/DIR/OR/FILE is the path to a directory or file on which to set the project ID. Only one path or file can be specified.

For additional flags and information, run `man lfs project` from your client.

For example, to assign project `101` to `/mnt/lustre/my-project` and all children new and existing:
    
    sudo lfs project -spr 101 /mnt/lustre/my-project
    

  2. Set the quota using `lfs setquota`:
         
         sudo lfs setquota -p LFS_PROJECT_ID \
           -b SOFT_BLOCK_LIMIT -B HARD_BLOCK_LIMIT \
           -i SOFT_INODE_LIMIT -I HARD_INODE_LIMIT \
           MOUNT_DIR
         




#### Set a default quota

Set a hard block limit of 50 TB for all users without a specific quota setting:
    
    
    sudo lfs setquota -U -B 50T /mnt/lustre
    

## Modify quotas

To modify an existing quota, run `lfs setquota` again with the new values. The command overwrites the previous settings for the specified user, group, or project.

## Configure grace periods

Grace periods define how long a user, group, or project can exceed a soft limit before the soft limit acts as a hard limit. By default, this value is one week. Grace periods are set on all users, groups, or projects; they cannot be set on specific IDs.

To update a grace period, use the `lfs setquota -t` command:
    
    
    sudo lfs setquota -t -u | g | p \
      -b BLOCK_GRACE_PERIOD -i INODE_GRACE_PERIOD \
      MOUNT_DIR
    

Where:

  * `-u` applies the grace period to user quotas.
  * `-g` applies the grace period to group quotas.
  * `-p` applies the grace period to project quotas.
  * `-b` and `-i` specify the block and inode grace periods, respectively. The default unit is seconds. You can use other units with the format: `XwXdXhXmXs` (weeks, days, hours, minutes, seconds). You can set limits for either or both quota types.

Specify `'notify'` instead of a time value to mark the output of `lfs quota` with an asterisk when the soft limit has been exceeded. New writes are not blocked when `'notify'` is specified until the hard limit is reached.




For example, to set a block grace period of 7 days for all user quotas:
    
    
    sudo lfs setquota -t -u -b 7d /mnt/lustre
    

To set an inode grace period of 24 hours for project quotas:
    
    
    sudo lfs setquota -t -p -i 24h /mnt/lustre
    

To notify when a block soft limit is exceeded:
    
    
    sudo lfs setquota -t -u -b 'notify' /mnt/lustre
    

## View existing quotas

The `lfs quota` command displays usage and limits for the current user:
    
    
    lfs quota MOUNT_DIR
    

For a full list of options, run `man lfs quota` from your client.

For example, to view `user1`'s quota on `/mnt/lustre`:
    
    
    sudo lfs quota -u user1 /mnt/lustre
    

Note that viewing another user's quota and usage requires running the command with `sudo`.

The output shows:

  * `Filesystem`: The Lustre mount point.
  * `kbytes`: Current disk usage in kilobytes.
  * `bquota`: Soft block limit in kilobytes.
  * `blimit`: Hard block limit in kilobytes.
  * `bgrace`: Remaining grace period if the block soft limit is exceeded. An asterisk (`*`) indicates the soft limit is exceeded.
  * `files`: Number of inodes used.
  * `iquota`: Soft inode limit.
  * `ilimit`: Hard inode limit.
  * `igrace`: Remaining grace period if the inode soft limit is exceeded. An asterisk (`*`) indicates the soft limit is exceeded.



To view the configured grace periods for all user quotas:
    
    
    lfs quota -t -u /mnt/lustre
    

## Monitor quotas in Cloud Monitoring

In addition to using the `lfs quota` command on a client, you can view file system quota usage and limits through Cloud Monitoring. This lets you monitor storage consumption by user, group, or project from the Google Cloud console.

Quota metrics are associated with the **Lustre Quota Entity** monitored resource. Available metrics include:

  * **Bytes:** Used bytes, soft limit, and hard limit.
  * **Inodes:** Used inodes, soft limit, and hard limit.



To view these metrics:

  1. In the Google Cloud console, go to the **Monitoring** > **Metrics Explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Select a metric** field, search for and select the **Lustre Quota Entity** resource.

  3. Select the specific quota metric you want to view (for example, **Quota Used Bytes** or **Quota Hard Limit Inodes**).

  4. Optionally, use the **Filter** options to view specific entities by filtering on the `accounting_type` label (e.g., `user`, `group`, `project`) or the `id` label (e.g., the specific UID, GID, or project ID).




## Remove quotas

To remove a quota, set its soft and hard limits to `0`.
    
    
    sudo lfs setquota -u | g | p | U | G | P UGP_VALUE -b 0 -B 0 -i 0 -I 0 MOUNT_DIR
    

For example, to remove `user1`'s block and inode quotas:
    
    
    sudo lfs setquota -u user1 -b 0 -B 0 -i 0 -I 0 /mnt/lustre
    

To remove the default project block limit:
    
    
    sudo lfs setquota -P -b 0 -B 0 /mnt/lustre
    

## Common issues

When working with Lustre quotas, be aware of the following common issues:

  * **Granted cache** : [Granted cache](https://doc.lustre.org/lustre_manual.xhtml#granted_cache_and_quota_limits) is a Lustre feature that allows clients to receive a block of storage as a "grant" from the Object Storage Target (OST) for writing data. When a client has this granted cache, it can immediately return a success message to the user for a write operation, even while the data is still in the client's local cache and before the data is physically written to the disk. This is a performance optimization that minimizes latency.

Granted cache introduces the potential for quota overruns. Because the granted cache allows clients to continue writing data to their cache even if their server-side quota has in the meantime been exhausted, it's possible for a user to exceed their hard limit.

  * **Incorrect project ID assignment** : For project quotas to work, directories and files must be correctly assigned a project ID using `lfs project -spr`. Omitting `-r` means the project ID is not applied to existing files and subdirectories. Omitting `-s` means new files and directories created later won't inherit the project ID.

  * **Multiple quotas and "most restrictive wins"** : A user can be subject to a user quota, one or more group quotas, and one or more project quotas simultaneously. Lustre enforces the most restrictive of these limits. This means a user could have a large personal quota but be restricted by a smaller project quota for files within that project's directory.

  * **Root user quota bypass** : A `root` user's writes bypass quota enforcement. This can lead to the file system being filled by administrative tasks, even when quotas are in place for other users.

  * **`fallocate` does not respect quotas**: Users can use `fallocate` to reserve space on the file system that exceeds the hard limit.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
