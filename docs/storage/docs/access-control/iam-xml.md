---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-xml/
title: IAM permissions for XML requests \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:45.130158+00:00
---

# IAM permissions for XML requests  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-xml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for XML requests Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) permissions required to run each Cloud Storage [XML method](https://docs.cloud.google.com/storage/docs/xml-api/reference-methods) on a given resource.

**Note:** IAM policies cannot be managed using the XML API. See [Using IAM Permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) for available management options.Method | Resource | Subresource | Required IAM Permissions1  
---|---|---|---  
`DELETE` | `bucket` |  | `storage.buckets.delete`  
`DELETE` | `object` |  | `storage.objects.delete`  
`DELETE` | `object` | `uploadId` | `storage.multipartUploads.abort`  
`GET` |  |  | `storage.buckets.list`  
`GET` | `bucket` |  | `storage.objects.list`  
`GET` | `bucket` | `acls`3 | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`GET` | `bucket` | Non-ACL metadata | `storage.buckets.get`  
`GET` | `bucket` | `uploads` | `storage.multipartUploads.list`  
`GET` | `object` |  | `storage.objects.get`  
`GET` | `object` | `acls`3 | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`GET` | `object` | `encryption` | `storage.objects.get`  
`GET` | `object` | `retention` | `storage.objects.get`  
`GET` | `object` | `uploadId` | `storage.multipartUploads.listParts`  
`HEAD` | `bucket` |  | `storage.buckets.get`  
`HEAD` | `object` |  | `storage.objects.get`  
`POST` | `object` |  | `storage.objects.create`  
`storage.objects.delete`4  
`storage.objects.setRetention`5  
`POST` | `object` | `uploadId` | `storage.multipartUploads.create`  
`storage.objects.create`  
`storage.objects.delete`4  
`POST` | `object` | `uploads` | `storage.multipartUploads.create`  
`storage.objects.create`  
`storage.objects.setRetention`5  
`PUT` | `bucket` |  | `storage.buckets.create`  
`storage.buckets.enableObjectRetention`6  
`PUT` | `bucket` | `acls`3 | `storage.buckets.get`  
`storage.buckets.getIamPolicy`  
`storage.buckets.setIamPolicy`  
`storage.buckets.update`  
`PUT` | `bucket` | Non-ACL metadata | `storage.buckets.update`  
`PUT`7 | `object` |  | `storage.objects.create`  
`storage.objects.get`2  
`storage.objects.delete`4  
`storage.objects.setRetention`5  
`PUT` | `object` | `acls`3 | `storage.objects.get`  
`storage.objects.getIamPolicy`  
`storage.objects.setIamPolicy`  
`storage.objects.update`  
`PUT` | `object` | `compose` | `storage.objects.create`  
`storage.objects.get`  
`storage.objects.delete`4  
`storage.objects.setRetention`5  
`PUT` | `object` | `retention` | `storage.objects.setRetention`  
`storage.objects.update`  
`storage.objects.overrideUnlockedRetention`8  
`PUT` | `object` | `uploadId` | `storage.multipartUploads.create`  
`storage.objects.create`  
`GET` | `Projects.hmacKeys` |  | `storage.hmacKeys.get`  
`POST` | `Projects.hmacKeys` |  | `storage.hmacKeys.create`  
`storage.hmacKeys.update`  
`storage.hmacKeys.delete`  
  
1 If you use the [`x-goog-user-project` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject) or [`userProject` query string parameter](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#userProject) in your request, you must have `serviceusage.services.use` permission for the project ID that you specify, in addition to the normal IAM permissions required to make the request.

2 This permission is required for the source bucket when the request includes the [`x-goog-copy-source` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopy).

3 This subresource does not apply to buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

4 This permission is only required when the inserted object has the same name as an object that already exists in the bucket.

5 This permission is only required when the request includes the [`x-goog-object-lock-mode`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode) and [`x-goog-object-lock-retain-until-date`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate) headers.

6 This permission is only required when the request includes a [`x-goog-bucket-object-lock-enabled`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogbucketobjectlockenabled) header set to `true`.

7 No permissions are required to make `PUT` requests associated with a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads).

8 This permission is only required when the request includes a [`x-goog-bypass-governance-retention`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogbypassgovernanceretention) header set to `true`.

## What's next

  * For a list of roles and the permissions they contain, see [IAM Roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
