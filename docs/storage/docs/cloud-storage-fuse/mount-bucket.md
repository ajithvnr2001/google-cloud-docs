---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket/
title: Mount Cloud Storage buckets by using Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:36.797313+00:00
---

# Mount Cloud Storage buckets by using Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Mount Cloud Storage buckets by using Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Storage FUSE CLI options](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options)

Mounting a bucket to your local file system lets you access your data in Cloud Storage through standard file system semantics. This document describes how to mount Cloud Storage buckets to your local file system by using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).

## Before you begin

To mount and access buckets, you must first complete the following tasks. You cannot use Cloud Shell to mount Cloud Storage buckets. Instead, run the commands provided in this document in the terminal of your Debian or Ubuntu machine.

### Get the required roles for mounting and accessing a bucket

To mount, access, and perform read and write operations in a bucket, ask the bucket owner to grant you the Storage Object User (`roles/storage.objectUser`) role on the bucket.

This [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles) contains the permissions required to read from a mounted bucket and write to a mounted bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`
  * `storage.objects.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other predefined roles.

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

**Note:** The minimum required role to mount and view a bucket is the Storage Object Viewer (`roles/storage.objectViewer`) role, which contains the `storage.objects.list` permission, but doesn't allow you to perform read or write operations.

### Install Cloud Storage FUSE

If you haven't already, [install Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install) on your machine.

### Authenticate Cloud Storage FUSE requests

To authenticate Cloud Storage FUSE requests to Cloud Storage, you must [set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc). By default, Cloud Storage FUSE automatically loads existing Application Default Credentials without any further configuration.

To use the Google Cloud CLI to set up Application Default Credentials, complete the following steps:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




When you create a Compute Engine virtual machine (VM), its service account can also be used to authenticate access to Cloud Storage FUSE.

## Mount a bucket

To mount buckets to your local file system, run the following command on your local machine:
    
    
    gcsfuse GLOBAL_OPTIONS BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `GLOBAL_OPTIONS` are the options you can include to control how the mount is set up. For more information about options and how to use them, see [Cloud Storage FUSE CLI reference](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options) or the [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file) pages.

    * `BUCKET_NAME` is the name of the bucket you want to mount. For example, `my-bucket`. If you want to perform dynamic mounting, exclude a bucket name from the command.

    * `MOUNT_POINT` is the local directory where the bucket gets mounted. For example, `/path/to/mount/point`.




Optional: to create implicitly-defined directories that allow you to navigate to folders that only contain objects nested deeper within, include the `--implicit-dirs` flag in your `gcsfuse` command. To learn more about implicitly-defined directories, see [Directory semantics](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#directory-semantics).

After Cloud Storage FUSE exits, you can access your mounted buckets by running `ls` on the bucket mount point. If you'd prefer Cloud Storage FUSE to stay in the foreground (for example, for debug logging), you can run the `gcsfuse` command with the [`foreground` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#foreground) or the [`--foreground` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#foreground).

**Note:** If you reboot your machine, you'll need to remount the bucket. To enable automatic mounting upon reboot, use Persistent mounting.

## Examples of mounting

This section describes different example commands for mounting buckets.

### Static mounting

Static mounting refers to mounting a specific bucket. For example, to mount a bucket named `my-bucket` to the directory `/path/to/mount/point`, run the following commands:
    
    
    mkdir /path/to/mount/point
    gcsfuse my-bucket /path/to/mount/point

### Dynamic mounting

Dynamic mounting refers to mounting all buckets a user has access to as subdirectories.

When you perform dynamic mounting, you exclude bucket names from the command. For example, say you have access to buckets named `my-bucket-1`, `my-bucket-2`, and `my-bucket-3`. To mount all buckets to the directory `/path/to/mount/point`, run the following commands:
    
    
    mkdir /path/to/mount/point
    gcsfuse /path/to/mount/point

You can then access the buckets as subdirectories:
    
    
    ls /path/to/mount/point/my-bucket-1/
    ls /path/to/mount/point/my-bucket-2/
    ls /path/to/mount/point/my-bucket-3/

Dynamically mounted buckets cannot be listed from the root mount point. Instead, the bucket name must be specified as part of the list operation.

### Mounting a bucket as read-only

To mount a bucket as read-only, pass the `-o ro` option to your `gcsfuse` command. For example, to mount a bucket named `my-bucket` as read-only to the directory `/path/to/mount/point`, run the following command:
    
    
    gcsfuse -o ro my-bucket  /path/to/mount/point

### Mount a directory within a bucket

By default, Cloud Storage FUSE mounts buckets in entirety, which includes all the bucket's contents and directory structures. To mount a specific directory within a bucket, pass the [`--only-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#only-dir) option to the `gcsfuse` CLI or the [`only-dir` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#only-dir) in a Cloud Storage FUSE configuration file. For example, to mount the directory `my-bucket/a/b` to the directory `/path/to/mount/point`, run the following command:
    
    
    gcsfuse --only-dir a/b my-bucket /path/to/mount/point

### Mount by using the Linux `mount` command

The Cloud Storage FUSE install includes a helper that's understood by the Linux `mount` command, which lets you use the `mount` command to mount buckets. The `mount` command must be run from root if you're using Linux. For example, the following command mounts a bucket named `my-bucket` to the path `/path/to/mount/point`:
    
    
    sudo mount -t gcsfuse -o rw,user my-bucket /path/to/mount/point

When mounting by using the Linux `mount` command, [`gcsfuse` options](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) can be passed as an argument to the [`-o` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#o), but hyphens (`-`) in them should be replaced with underscores (`_`). For example, `implicit_dirs` instead of `implicit-dirs`.
    
    
    sudo mount -t gcsfuse -o implicit_dirs my-bucket /path/to/mount/point

### Persistent mounting

The Cloud Storage FUSE installation includes a helper that's installed to your system at the path `/sbin/mount.gcsfuse`. This helper lets you create mount points by using the `/etc/fstab` file, so you can persist your mounts.

For example, when added to your `/etc/fstab` file, the following line defines a mount point for a bucket named `my-bucket` at the path `/mount/point`:
    
    
    my-bucket /mount/point gcsfuse rw,noauto,user

Where:

  * The `rw` option specifies that the mount point be created with read and write permissions.

  * The `noauto` option specifies that the file system shouldn't be mounted at boot time.

  * The `user` option allows anybody to create the mount point specified in the `/etc/fstab` file. After the sample line is added to the `/etc/fstab` file, you can run `mount /mount/point` as a non-root user.




If you want to mount the bucket automatically at boot, you might need to include the `_netdev` option in your `/etc/fstab` entry, to ensure that Cloud Storage FUSE waits for the network system to be ready prior to mounting. For example:
    
    
    my-bucket /mount/point gcsfuse rw,_netdev,user

You can mount a bucket automatically as a specific non-root user by including the options `uid`, `gid`, or both in your `/etc/fstab` entry. For example:
    
    
    my-bucket /mount/point gcsfuse rw,_netdev,allow_other,uid=1001,gid=1001

Similar to the Linux `mount` command, the flags used for mounting in the `/etc/fstab` file must use underscores (`_`) instead of hyphens (`-`). For example, `implicit_dirs` instead of `implicit-dirs`.

### Mount a bucket with folders

You can mount buckets with multiple folder types.

#### Mount a bucket with managed folders

To mount a bucket including its [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders), include the [`--implicit-dirs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#implicit-dirs) option or the [`implicit-dirs` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#implicit-dirs) in your command.

For example, to mount a bucket named `my-bucket` and its managed folders to the directory `/path/to/mount/point`, run the following commands:
    
    
    gcsfuse --implicit-dirs my-bucket /path/to/mount/point

When mounting a bucket with managed folders, keep the following limitations and considerations in mind:

  * Empty managed folders don't appear in mounted buckets.

  * You cannot set or manage IAM permissions on a managed folder by using Cloud Storage FUSE. To set or manage IAM permissions on a managed folder, see [Use IAM with managed folders](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders).

  * You can copy and move a managed folder in a mounted bucket by using the `cp` and `mv` commands. When you copy or move a managed folder, the IAM policies on the original managed folder don't persist onto the new managed folder. You must set new IAM policies on the new managed folder.




#### Mount a bucket with implicitly defined folders

You can mount implicitly defined folders using the [`--implicit-dirs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#implicit-dirs) `gcsfuse` option in the `gcsfuse` CLI or the [`implicit-dirs` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#implicit-dirs) in a Cloud Storage FUSE configuration file. Implicitly defined folders are folders that aren't explicitly created as objects in Cloud Storage. The `--implicit-dirs` option lets you see folders when mounting a bucket.

For example, to mount a bucket named `my-bucket` to the directory `/path/to/mount/point` with implicitly defined folders, run the following command:
    
    
    gcsfuse --implicit-dirs my-bucket /path/to/mount/point

#### Mount a hierarchical namespace-enabled bucket with folders

You can mount a bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled, including its [folders](https://docs.cloud.google.com/storage/docs/folders-overview). When mounting a bucket with hierarchical namespace, you don't need to specify the `--implicit-dirs` `gcsfuse` option or `implicit-dirs` field in order for the folders to appear in your mounted bucket.

For example, to mount a bucket named `my-bucket` with folders to the directory `/path/to/mount/point`, run the following command:
    
    
    gcsfuse my-bucket /path/to/mount/point

## Control access permissions to the mount point

By default, Cloud Storage FUSE creates bucket mount points with permissions that only allow the invoking user to access the contents of the mounted buckets. This is a security measure that's implemented within the FUSE kernel.

To mount a bucket and allow others to access the bucket mount point, you can run the command `mount` as root with the option `-o allow_other`:
    
    
    mount -t gcsfuse -o allow_other my-bucket /path/to/mount/point

If you want to avoid mounting the bucket as root, you must add `user_allow_other` to the `/etc/fuse.conf` file to allow others to access the bucket mount point.

## Unmount a bucket

To unmount a bucket, use the `fusermount` tool:
    
    
    fusermount -u /path/to/mount/point

## What's next

  * Learn about [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance), such as how to control caching behavior or log activity.

  * Learn about [directory semantics in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#directory-semantics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
