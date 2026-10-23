---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-console/
title: IAM permissions for the Google Cloud console \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:10.572717+00:00
---

# IAM permissions for the Google Cloud console  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

The following page discusses the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions required to perform actions within the Cloud Storage portion of the Google Cloud console. IAM permissions are bundled together to make [roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles), and you [grant roles to users and groups](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Common permissions required for using the Google Cloud console

Certain permissions are broadly necessary in order to use the Google Cloud console:

  * All actions involving buckets should include `resourcemanager.projects.get` and `storage.buckets.list` permissions at the project level.

These permissions allow you to access the Buckets page, where you create, view, and update buckets.

  * All actions that include a billing project in the request require `serviceusage.services.use` permission for the project that's specified.

This permission ensures you are authorized to bill the project you specify. Including a billing project is used, for example, when accessing a bucket with [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled.




## Permissions required for specific actions

Action | Required IAM Permissions (in addition to those listed above)  
---|---  
Create a bucket | `storage.buckets.create``storage.buckets.enableObjectRetention`1  
Attach a tag to a bucket | `storage.buckets.createTagBinding`  
List or filter buckets | _No additional permissions_  
List tags directly attached to a bucket | `storage.buckets.listTagBindings`  
List both inherited tags and tags directly attached to a bucket | `storage.buckets.listEffectiveTags`  
View the following bucket information: 

  * Location, replication status, and default storage class
  * **Protection** settings
  * Bucket labels
  * Object lifecycle policies
  * Public access prevention status
  * Uniform bucket-level access status
  * Autoclass status
  * Website configuration

| `storage.buckets.get`  
Change the following bucket settings: 

  * **Protection** settings
  * Default storage class
  * Bucket labels
  * Object lifecycle policies
  * Uniform bucket-level access status
  * Autoclass status
  * Website configuration
  * Object retention configurations

| `storage.buckets.get`  
`storage.buckets.update`  
`storage.buckets.enableObjectRetention`1  
Enable the Requester Pays feature | `storage.buckets.get`  
`storage.buckets.update`  
Disable the Requester Pays feature | `storage.buckets.get`  
`storage.buckets.update`  
`resourcemanager.projects.createBillingAssignment`3  
Change the public access prevention setting | `storage.buckets.get`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
Change bucket permissions | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
Delete an empty bucket | `storage.buckets.delete`  
`storage.objects.list`  
Delete a non-empty bucket | `storage.buckets.delete`  
`storage.objects.delete`  
`storage.objects.list`  
Detach a tag from a bucket | `storage.buckets.deleteTagBinding`  
Create a folder | `storage.folders.create`  
Get the metadata of a folder | `storage.folders.get`  
List folders | `storage.folders.list`  
Rename folders | `storage.folders.rename` (for the source bucket)  
`storage.folders.create` (for the destination bucket)  
Delete folders | `storage.folders.delete`  
Upload an object or folder of objects | `storage.objects.create`  
`storage.objects.delete`2  
`storage.objects.setRetention`4  
View the details for an object5 | `storage.objects.get`  
`storage.objects.list`  
View the version history of an object | `storage.objects.get`  
`storage.objects.list`  
Download an object5 or folder of objects | `storage.objects.get`  
`storage.objects.list`  
List objects in a bucket, including noncurrent objects and soft-deleted objects | `storage.objects.list`  
Determine if an object is publicly accessible5 | `storage.buckets.getIamPolicy`  
`storage.objects.list`  
`storage.objects.getIamPolicy`7  
Rename an object or restore a noncurrent version of an object | `storage.objects.create`  
`storage.objects.delete`  
`storage.objects.get`  
`storage.objects.list`  
`storage.objects.getIamPolicy`7  
`storage.objects.setIamPolicy`7  
Copy an object | `storage.objects.create` (for the destination bucket)   
`storage.objects.delete`2 (for the destination bucket)   
`storage.objects.get` (for the source object)   
`storage.objects.list` (for the source bucket and destination bucket)   
`storage.objects.getIamPolicy`7,8 (for the source object)   
`storage.objects.setIamPolicy`7,8 (for the destination bucket)  
Move an object | `storage.objects.create` (for the destination bucket)   
`storage.objects.delete`2 (for the destination bucket)   
`storage.objects.delete` (for the source bucket)   
`storage.objects.get` (for the source object)   
`storage.objects.list` (for the source bucket and destination bucket)   
`storage.objects.getIamPolicy`7,8 (for the source object)   
`storage.objects.setIamPolicy`7,8 (for the destination bucket)  
View an object's access permissions5,6 | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.getIamPolicy`  
Edit an object's access permissions5,6 | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
Edit an object's metadata5 | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
Add, change, or remove a retention configuration on an object5 | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
`storage.objects.setRetention`  
`storage.objects.overrideUnlockedRetention`9  
Add or remove a hold on an object5 | `storage.objects.get`  
`storage.objects.list`  
`storage.objects.update`  
Delete an object5, a noncurrent version of an object, or a folder of objects | `storage.objects.delete`  
`storage.objects.list`  
Restore a deleted object | `storage.objects.create`  
`storage.objects.delete`2  
`storage.objects.list`  
`storage.objects.restore`  
Bulk restore deleted objects | `storage.objects.create`  
`storage.objects.delete`10  
`storage.objects.restore`  
`storage.buckets.restore`  
`storage.objects.setIamPolicy`7,11  
View the name of a project's Cloud Storage service agent | `resourcemanager.projects.get`  
View the service account HMAC keys for a project | `resourcemanager.projects.get`  
`storage.hmacKeys.list`  
Create an HMAC key for a service account | `resourcemanager.projects.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.create`  
Disable or re-enable an HMAC key for a service account | `resourcemanager.projects.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.update`  
Delete an HMAC key for a service account | `resourcemanager.projects.get`  
`storage.hmacKeys.list`  
`storage.hmacKeys.delete`  
Create, view, or delete an HMAC key for the user account you are logged in as | `resourcemanager.projects.get`  
Configure, update or disable the Storage Intelligence configuration on a project, a folder or an organization | `storage.intelligenceConfigs.update`  
View the Storage Intelligence configuration on a project, a folder or an organization | `storage.intelligenceConfigs.get`  
View Storage Intelligence advisor, findings, finding details, and bucket drill-down details on a project, a folder or an organization | `storage.buckets.viewIntelligenceDetails`  
Create a cache using Rapid Cache | `storage.anywhereCaches.create`  
List a cache using Rapid Cache | `storage.anywhereCaches.list`  
Update a cache using Rapid Cache | `storage.anywhereCaches.update`  
Pause a cache using Rapid Cache | `storage.anywhereCaches.pause`  
Resume a cache using Rapid Cache | `storage.anywhereCaches.resume`  
Get the metadata of a cache using Rapid Cache | `storage.anywhereCaches.get`  
Disable a cache using Rapid Cache | `storage.anywhereCaches.disable`  
  
1This permission is only required when enabling a bucket to support [object retention configurations](https://docs.cloud.google.com/storage/docs/object-lock).

2This permission is only required if an object with the same name already exists in the destination bucket.

3This permission is only required if you do not include a billing project in your request. See Requester Pays [Use and access requirements](https://docs.cloud.google.com/storage/docs/requester-pays#requirements) for more information.

4This permission is only required when adding a [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) as part of uploading the object.

5This action does not require `storage.objects.list` if it's performed on the details page for the relevant object and you don't access the details page from the overall list of objects for the bucket.

6This action does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

7This permission does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

8This permission is only required when keeping the permissions currently applied to the source object.

9This permission is required when changing an existing [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) such that the configuration becomes locked, reduced, or removed.

10This permission is only required if an object with the same name already exists in the destination bucket and you select the **Overwrite live objects** option.

11 This permission is only required when selecting the **Copy source access controls (ACLs)** option.

## What's next

  * For a list of roles and the permissions they contain, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

  * [Grant IAM roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) at the project and bucket level.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
