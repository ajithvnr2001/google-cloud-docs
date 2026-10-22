---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil/
title: IAM permissions for gsutil commands \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:23.886258+00:00
---

# IAM permissions for gsutil commands  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for gsutil commands Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions required to run each Cloud Storage [gsutil command](https://docs.cloud.google.com/storage/docs/gsutil) on a given resource. IAM permissions are bundled together to make [roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). You [grant roles to users and groups](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

On this page, you can also find information about the following:

  * Using [additional commands](https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil#extended) that only apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled

  * Using [wildcards and recursive flags](https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil#wildcards)

  * Using the [`-u` flag](https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil#u-flag) to specify projects for billing

  * Using the [`-m` flag](https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil#m-flag) to run operations in parallel


Command | Sub-command | Required IAM Permissions  
---|---|---  
`autoclass` | `get` | `storage.buckets.get`  
`autoclass` | `set` | `storage.buckets.update`  
`cat` |  | `storage.objects.get`  
`compose` |  | `storage.objects.get`  
`storage.objects.create`  
`storage.objects.delete`1  
`config` |  | None  
`cors` | `get` | `storage.buckets.get`  
`cors` | `set` | `storage.buckets.update`  
`cp` |  | `storage.objects.list`2 (for the destination bucket)   
`storage.objects.get` (for the source objects)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete`3 (for the destination bucket)  
`defstorageclass` | `get` | `storage.buckets.get`  
`defstorageclass` | `set` | `storage.buckets.update`  
`du` |  | `storage.objects.get`  
`hash` |  | `storage.objects.get`  
`help` |  | None  
`hmacKeys` | `create` | `storage.hmacKeys.create`  
`hmacKeys` | `delete` | `storage.hmacKeys.delete`  
`hmacKeys` | `get` | `storage.hmacKeys.get`  
`hmacKeys` | `list` | `storage.hmacKeys.list`  
`hmacKeys` | `update` | `storage.hmacKeys.update`  
`iam` | `get` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`iam` | `set` or `ch` | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`kms` | `authorize` | `resourceManager.projects.get`  
`iam.serviceAccounts.create`4  
`cloudkms.cryptoKeys.setIamPolicy` (for the Cloud KMS key being authorized)  
`kms` | `encryption` | `storage.buckets.get`  
`kms` | `encryption -d` | `storage.buckets.get`  
`storage.buckets.update`  
`kms` | `encryption -k` | `storage.buckets.get`  
`storage.buckets.update`  
`resourceManager.projects.get`5  
`cloudkms.cryptoKeys.setIamPolicy`5  
`kms` | `serviceaccount` | `resourceManager.projects.get`  
`label` | `get` | `storage.buckets.get`  
`label` | `set/ch` | `storage.buckets.update`  
`lifecycle` | `get` | `storage.buckets.get`  
`lifecycle` | `set/ch` | `storage.buckets.update`  
`logging` | `get` | `storage.buckets.get`  
`logging` | `set` | `storage.buckets.update`  
`ls` (listing buckets) |  | `storage.buckets.list`  
`storage.buckets.getIamPolicy`6  
`ls` (listing objects) |  | `storage.objects.list`  
`storage.objects.getIamPolicy`7  
`ls -b` |  | `storage.buckets.get`  
`storage.buckets.getIamPolicy`6  
`mb` |  | `storage.buckets.create`  
`mv` |  | `storage.objects.list`2 (for the destination bucket)  
`storage.objects.get` (for the source objects)  
`storage.objects.create` (for the destination bucket)  
`storage.objects.delete` (for the source bucket)  
`storage.objects.delete`3 (for the destination bucket)  
`notification` | `create` | `storage.buckets.update`  
`pubsub.topics.get` (for the project containing the Pub/Sub topic)  
`pubsub.topics.create`8 (for the project containing the Pub/Sub topic)  
`pubsub.topics.getIamPolicy` (for Pub/Sub topic receiving notifications)  
`pubsub.topics.setIamPolicy`8 (for Pub/Sub topic receiving notifications)  
`notification` | `create -s` | `storage.buckets.update`  
`notification` | `delete` | `storage.buckets.get`  
`storage.buckets.update`  
`notification` | `list` | `storage.buckets.get`  
`pap` | `get` | `storage.buckets.get`  
`pap` | `set` | `storage.buckets.get`  
`storage.buckets.update`  
`storage.buckets.setIamPolicy`10  
`perfdiag` |  | `storage.buckets.get`  
`storage.objects.create`  
`storage.objects.delete`  
`storage.objects.list`  
`storage.objects.get`  
`rb` |  | `storage.buckets.delete`  
`requesterpays` | `get` | `storage.buckets.get`  
`requesterpays` | `set on` | `storage.buckets.update`  
`requesterpays` | `set off` | `storage.buckets.update`  
`resourcemanager.projects.createBillingAssignment`9  
`retention` | `clear`, `event-default`, `lock`, or `set` | `storage.buckets.update`  
`retention` | `event` or `temp` | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
`retention` | `get` | `storage.buckets.get`  
`rewrite -k` |  | `storage.objects.list`  
`storage.objects.get`  
`storage.objects.create`  
`storage.objects.delete`  
`rewrite -s` |  | `storage.objects.list`  
`storage.objects.get`  
`storage.objects.create`  
`storage.objects.delete`  
`storage.objects.update`  
`rm` |  | `storage.objects.delete`  
`rm -a` |  | `storage.objects.delete`  
`storage.objects.list`  
`rm -r` (deleting a bucket) |  | `storage.buckets.delete`  
`storage.objects.delete`  
`storage.objects.list`  
`rpo` | `get` | `storage.buckets.get`  
`rpo` | `set` | `storage.buckets.get`  
`storage.buckets.update`  
`rsync` |  | `storage.objects.get` (for the source objects and destination bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete`11 (for the destination bucket)   
`storage.objects.list` (for the source and destination buckets)  
`rsync -n` |  | `storage.objects.list` (for the source and destination buckets)  
`setmeta` |  | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
`signurl` |  | None; however, the service account whose key is used as part of this command must have permission to perform the request being encoded into the signed URL.  
`stat` |  | `storage.objects.get`  
`test` |  | None  
`ubla` | `set` | `storage.buckets.get`  
`storage.buckets.update`  
`ubla` | `get` | `storage.buckets.get`  
`update` |  | None  
`version` |  | None  
`versioning` | `get` | `storage.buckets.get`  
`versioning` | `set` | `storage.buckets.update`  
`web` | `get` | `storage.buckets.get`  
`web` | `set` | `storage.buckets.update`  
  
1This permission is only required if the composed object has the same name as an object that already exists in the bucket.

2 This permission is only required when the destination in the command contains an object path.

3This permission is only required if you use [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads) or if you don't use the `-n` flag but insert an object that has the same name as an object that already exists in the bucket.

4This permission is only required if you do not have an existing Cloud Storage service account associated with the project.

5If you use `gsutil kms encryption -k` and your project's service account does not have permission to access the requested Cloud KMS key, gsutil runs `gsutil kms authorize` in order to grant your service account the required permission.

6This permission is only required if you want IAM policies included in the details.

7This permission is only required if you want IAM policies included in the details, and it does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

8These permissions are not required if the topic already exists and the relevant service account has access to it.

9This permission is only required if you do not include a billing project in your request. See Requester Pays [Use and access requirements](https://docs.cloud.google.com/storage/docs/requester-pays#requirements) for more information.

10This permission is not required if the command does not change the bucket setting.

11This permission is only required if you use the `-d` flag or if you insert an object that has the same name as, but [different data](https://docs.cloud.google.com/storage/docs/data-validation#rsync) than, an object that already exists in the bucket.

**Note:** The permissions listed in the above table allow you to use the commands. Some commands set bucket configurations that won't work without additional permissions. For example, `gsutil notification create` requires only `storage.buckets.update` to use, but you must have [additional permissions](https://docs.cloud.google.com/storage/docs/reporting-changes#get-required-roles) for the feature to work properly.

#### ACL-related methods

The following table lists the IAM permissions required to run gsutil commands that apply specifically to the management of ACLs. These commands only apply to buckets that have [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled.

Command | Subcommand | Resource Acted On | Required IAM Permissions  
---|---|---|---  
`acl` | `get` | Buckets | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`acl` | `set` or `ch` | Buckets | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`acl` | `get` | Objects | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`acl` | `set` or `ch` | Objects | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`cp -a` or `cp -p` |  | Objects | `storage.objects.list`a (for the destination bucket)   
`storage.objects.get` (for the source objects)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete`b (for the destination bucket)   
`storage.objects.getIamPolicy` (for the source objects)   
`storage.objects.setIamPolicy` (for the destination bucket)  
`defacl` | `get` | Buckets | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`defacl` | `set` or `ch` | Buckets | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`iam` | `get` | Objects | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`iam` | `set` or `ch` | Objects | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`mv -a` or `mv -p` |  | Objects | `storage.objects.list`a (for the destination bucket)   
`storage.objects.get` (for the source objects)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete` (for the source bucket)   
`storage.objects.delete`b (for the destination bucket)   
`storage.objects.getIamPolicy` (for the source objects)   
`storage.objects.setIamPolicy` (for the destination bucket)  
`rsync -a` or `rsync -p` |  | Objects | `storage.objects.get` (for the source objects and destination bucket)   
`storage.objects.create` (for the destination bucket)   
`storage.objects.delete`c (for the destination bucket)   
`storage.objects.list` (for the source and destination buckets)   
`storage.objects.getIamPolicy` (for the source objects)   
`storage.objects.setIamPolicy` (for the destination bucket)  
  
a This permission is only required when the destination in the command contains an object path.

bThis permission is only required if you use [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads) or if you don't use the `-n` flag but insert an object that has the same name as an object that already exists in the bucket.

cThis permission is only required if you use the `-d` flag or if you insert an object that has the same name as, but [different data](https://docs.cloud.google.com/storage/docs/data-validation#rsync) than, an object that already exists in the bucket.

## The `-u` top-level flag

If you use the `-u` global flag to specify a project that should be billed for your request, you must have `serviceusage.services.use` permission for the project you specify. The `-u` flag is used, for example, when accessing a bucket with [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled.

## Wildcards and recursive flags

If you use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) to select multiple objects in a command, you must have `storage.objects.list` permission for the bucket containing the objects. Similarly, if you use URI wildcards to select multiple buckets in a command, you must have `storage.buckets.list` permission for the project(s) containing the buckets.

If you use the recursive flags (`-r` and `-R`), you must have `storage.objects.list` permission for the relevant bucket, in addition to the permissions required for the specific command you are using.

## The `-m` top-level flag

Normally, if you use a gsutil command that acts over multiple objects or buckets, the command fails at the first error. However, when you use the `-m` global flag, gsutil records any errors it encounters and continues with the operation.

For example, say you try to perform an `acl set` command on a series of objects, but you only have permission to do so on some of the objects. If you do not use the `-m` flag, gsutil applies the ACLs successfully until it reaches an object you do not have permission to apply an ACL to. At that point, gsutil fails. If you use the `-m` flag, gsutil records the errors that arise when it attempts to apply an ACL to an object for which you don't have permission, but otherwise continues with the operation.

## What's next

  * [Assign IAM roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) at the project and bucket level.
  * Review [IAM roles that contain Cloud Storage permissions](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
