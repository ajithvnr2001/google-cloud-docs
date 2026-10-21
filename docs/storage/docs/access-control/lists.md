---
url: https://docs.cloud.google.com/storage/docs/access-control/lists/
title: Access control lists (ACLs) \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:58.402297+00:00
---

# Access control lists (ACLs)  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/lists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Access control lists (ACLs) Stay organized with collections  Save and categorize content based on your preferences. 

[Usage](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists)

This page provides an overview of access control lists (ACLs), which let you control access to individual buckets or objects. To learn about other ways of controlling access to buckets and objects, read [Overview of Access Control](https://docs.cloud.google.com/storage/docs/access-control).

## Should you use access control lists?

In most cases, you should avoid using ACLs, and you should [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set) for your buckets, which prevents ACL usage:

  * ACLs can't be used exclusively to control access to your Google Cloud resources, because ACLs can't be set on the overall project or resources outside Cloud Storage.
  * Enabling uniform bucket-level access creates a simpler access control surface and lets you use additional Google Cloud features. For more information, see [should you use uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#should-you-use).
  * The [domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) organization policy and [custom organization policies](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints) don't prevent access granted by ACLs, potentially leading to unintended access.
  * Unexpected behaviors and access can occur when using ACLs in projects that have [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) set at or above the project level.



You most likely want to use ACLs in the following cases:

  * You need to customize access to individual objects within a bucket, such as if you want the uploader of an object to have full control over that object, but less access to other objects in your bucket.
  * You are exclusively using the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) or require [interoperability](https://docs.cloud.google.com/storage/docs/interoperability) with Amazon S3.



## What is an access control list?

An access control list (ACL) is a mechanism you can use to define who has access to your buckets and objects, as well as what level of access they have. In Cloud Storage, you apply ACLs to individual buckets and objects. Each ACL consists of one or more _entries_. An entry gives a specific user (or group) the ability to perform specific actions. Each entry consists of two pieces of information:

  * A **permission** , which defines _what_ actions can be performed (for example, read or write).

  * A **scope** (sometimes referred to as a _grantee_), which defines _who_ can perform the specified actions (for example, a specific user or group of users).




As an example, suppose you have a bucket that you want anyone to be able to access objects from, but you also want your collaborator to be able to add or remove objects from the bucket. In this case, your ACL would consist of two entries:

  * In one entry, you would give `READER` permission to a scope of `allUsers`.

  * In the other entry, you would give `WRITER` permission to the scope of your collaborator (there are several ways to specify this person, such as by their email).




The maximum number of ACL entries you can create for a bucket or object is 100. When the entry scope is a group or domain, it counts as one ACL entry regardless of how many users are in the group or domain.

When a user requests access to a bucket or object, the Cloud Storage system reads the bucket or object ACL and determines whether to allow or reject the access request. If the ACL grants the user permission for the requested operation, the request is allowed. If the ACL does not grant the user permission for the requested operation, the request fails and a `403 Forbidden` error is returned.

Note that while ACLs can be used to manage most actions involving buckets and objects, the ability to _create_ a bucket comes from having the appropriate [project permission](https://docs.cloud.google.com/storage/docs/access-control/iam).

### Permissions

_Permissions_ describe _what_ can be done to a given object or bucket.

Cloud Storage lets you assign the following concentric permissions for your buckets and objects, as shown in the following table: 

| Buckets | Objects  
---|---|---  
`READER` | Allows a user to list a bucket's contents. Also allows a user to read bucket metadata, excluding ACLs. | Allows a user to download an object's data.  
`WRITER` | Gives a user all access that's granted by the `READER` permission. Additionally allows a user to create, replace, and delete objects in a bucket, including creating objects using multipart uploads. | N/A. You cannot apply this permission to objects.  
`OWNER` | Gives a user all access that's granted by the `WRITER` permission. Also allows a user to read and write bucket metadata, including ACLs, and to work with tags on the bucket. | Gives a user all access that's granted by the `READER` permission. Also allows a user to read and write object metadata, including ACLs.  
Default | Buckets have the predefined project-private ACL applied when they are created. Buckets are always owned by the `project-owners` group. | Objects have the predefined project-private ACL applied when they are uploaded. Objects are always owned by the original requester who uploaded the object.  
**Note:** You cannot grant discrete permissions for reading or writing ACLs or other metadata. To allow someone to read and write ACLs, you must grant them `OWNER` permission.

In this page, we generally refer to the permissions as `READER`, `WRITER`, and `OWNER`, which are how they are specified in the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) and the [Google Cloud console](https://console.cloud.google.com/). If you are using the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), the equivalent permissions are `READ`, `WRITE`, and `FULL_CONTROL`, respectively.

### Scopes

_Scopes_ specify _who_ it is that has a given permission.

An ACL consists of one or more entries, where each entry grants permissions to a scope. You can specify an ACL scope using any of the following entities:

Scope ("grantee") | Entity Type(s) | Example  
---|---|---  
**Special identifier for all entities** | User | `allUsers`  
**Special identifier for all valid accounts** | User | `allAuthenticatedUsers`  
**User account email address** | User | `jeffersonloveshiking@gmail.com`  
**Service account email address** | User | `my-service-account@my-project.iam.gserviceaccount.com`  
**Google group email address** | Group | `work-group@googlegroups.com`  
**Convenience values for projects** | Project | `owners-123456789012`  
**Google Workspace domain** | Domain | `dana@example.com`  
**Cloud Identity domain** | Domain | `dana@example.com`  
  
  * **Special identifier for all entities** :

The special scope identifier `allUsers` represents any entity on the Internet. Note that while this identifier is a `User` entity type, when using the Google Cloud console it's labeled as a `Public` entity type.

  * **Special identifier for all valid accounts** :

The special scope identifier `allAuthenticatedUsers` represents most authenticated accounts, including service accounts. For more information, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers). Note that while this identifier is a `User` entity type, when using the Google Cloud console it's labeled as a `Public` entity type.

  * **User account email address** :

Every user who has a user account must have a unique email address associated with that account. You can specify a scope by using any email address that is associated with a user account.

Cloud Storage remembers email addresses as they are provided in ACLs until the entries are removed or replaced. If a user changes email addresses, you should update ACL entries to reflect these changes.

  * **Service account email address** :

Every [service account](https://docs.cloud.google.com/iam/docs/service-account-types) has a unique email address associated with it. You can specify a scope by using the email address that is associated with the service account.

  * **Google group email address** :

Every [Google group](https://support.google.com/groups/answer/46601) has a unique email address that is associated with the group. For example, the [Cloud Storage Announce](https://groups.google.com/forum/#!aboutgroup/gs-announce) group has the following email address: gs-announce@googlegroups.com. You can find the email address that is associated with a Google group by clicking **About** on the homepage of every Google group.

Like user account email addresses, Cloud Storage remembers group email addresses as they are provided in ACLs until the entries are removed. You don't need to worry about updating Google Group email addresses, because Google Group email addresses are permanent and unlikely to change.

  * **Convenience values for projects** :

[Convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values) allow you to grant bulk access to your project's viewers, editors, and owners. Convenience values combine a project role and an associated project number. For example, in project `867489160491`, editors are identified as `editors-867489160491`. You can find your project number on the homepage of the [Google Cloud console](https://console.cloud.google.com/).

You should generally avoid using convenience values in production environments, because they require granting [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), a practice which is discouraged in production environments.

  * **Google Workspace or Cloud Identity** :

[Google Workspace](https://workspace.google.com/) and [Cloud Identity](https://support.google.com/cloudidentity/answer/7319251) customers can associate their email accounts with an Internet domain name. When you do this, each email account takes the form USERNAME@YOUR_DOMAIN.com. You can specify a scope by using any Internet domain name that is associated with Google Workspace or Cloud Identity.




### Concentric permissions and scopes

When specifying ACLs in Cloud Storage, you do not need to list multiple scopes to grant multiple permissions. Cloud Storage uses concentric permissions, so when you grant `WRITER` permission, you also grant `READER` permission, and if you grant `OWNER` permission, you also grant `READER` and `WRITER` permission.

When specifying an ACL, most tools allow you to specify multiple scopes for the same entry. The most permissive permission is the access granted to the scope. For example, if you provide two entries for a user, one with `READER` permission and one with `WRITER` permission on a bucket, the user will have `WRITER` permission on the bucket.

In the XML API, it is not possible to provide two ACL entries with the same scope. For example, granting a user `READ` permission and `WRITE` permission on a bucket results in an error. Instead, grant the user `WRITE` permission, which also grants the user `READ` permission.

### ACLs and IAM

[Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) and ACLs work in tandem to grant access to your buckets and objects, which means a user only needs the relevant permission from either of these systems in order to access a bucket or object. In general, permissions granted by IAM policies don't appear in ACLs, and permissions granted by ACLs don't appear in IAM policies. See [IAM relation to ACLs](https://docs.cloud.google.com/storage/docs/access-control/iam#acls) for more information.

#### Behavior with IAM deny

An [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) overrides any applicable access that would otherwise be granted by an ACL you've set, when the deny policy and the ACL target the same permission.

For example, if a project has a deny policy that prevents a user from having the `storage.objects.get` permission, and you create an ACL that grants the user the `READER` role on an object within a bucket in that project, the user won't be able to view the object in the bucket. However, if the deny policy specifies the `storage.buckets.get` permission and the ACL grants the `WRITER` role on the bucket, the user won't be able to retrieve the bucket's metadata, but can still list, create, and delete objects in the bucket.

## Predefined ACLs

A predefined ACL, also sometimes known as a canned ACL, is an alias for a set of specific ACL entries that you can use to quickly apply many ACL entries at once to a bucket or object.

**Caution:** By applying a predefined ACL to an existing bucket or object, you completely replace the existing bucket or object ACL with the predefined ACL. This change might cause you to lose access to the bucket or object ACL in some cases. For example, if you are in the project owners group but are not the owner of an object with `projectPrivate` ACL, then after you apply the predefined ACL `publicRead` to the object, you lose `OWNER` permission and thus no longer can access the object ACL. If this occurs, you can use the [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam#acls) role `storage.objectAdmin` so that you have the permission necessary to update the object's ACL and correct the change.

The following table lists predefined ACLs and shows which ACL entries are applied for each predefined ACL. When using the table, note that:

  * The project owners group has ownership of buckets in the project, and the user that creates an object has ownership of that object. If an object was created by an anonymous user, then the project owners group has ownership of the object.

  * In the table, the JSON API descriptions of permissions, `OWNER`, `WRITER`, and `READER`, are used. The equivalent XML API scopes are `FULL_CONTROL`, `WRITE`, and `READ`.

JSON API/`gcloud storage` | XML API | Description  
---|---|---  
`private` | `private` |  Gives the bucket or object owner `OWNER` permission for a bucket or object.   
`bucketOwnerRead` | `bucket-owner-read` |  Gives the object owner `OWNER` permission, and gives the bucket owner `READER` permission. **This is used only with objects**.   
`bucketOwnerFullControl` | `bucket-owner-full-control` |  Gives the object and bucket owners `OWNER` permission. **This is used only with objects**.   
`projectPrivate` | `project-private` |  Gives permission to the project team based on their roles. Anyone who is part of the team has `READER` permission. Project owners and project editors have `OWNER` permission. This is the default ACL for newly created buckets. This is also the default ACL for newly created objects unless the default object ACL for that bucket has been changed.   
`authenticatedRead` | `authenticated-read` |  Gives the bucket or object owner `OWNER` permission, and gives all authenticated user account holders `READER` permission.   
`publicRead` | `public-read` |  Gives the bucket or object owner `OWNER` permission, and gives all users, both authenticated and anonymous, `READER` permission. When you apply this to an object, anyone on the Internet can read the object without authenticating. When you apply this to a bucket, anyone on the Internet can list objects without authenticating. * See the note at the end of the table regarding caching.  
`publicReadWrite` | `public-read-write` |  Gives the bucket owner `OWNER` permission, and gives all users, both authenticated and anonymous, `READER` and `WRITER` permission. This ACL applies only to buckets. When you apply this to a bucket, anyone on the Internet can list, create, replace, and delete objects without authenticating.   
**Important** : Setting a bucket to `publicReadWrite` allows anyone on the Internet to upload anything to your bucket. You are responsible for this content.* See the note at the end of the table regarding caching.  



* By default, publicly readable objects are served with a `Cache-Control` header that allows the objects to be cached for 3600 seconds. If you need to ensure that updates become visible immediately, you should [set the `Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata) for the objects to `Cache-Control:private, max-age=0, no-transform`.

## Default ACLs

When buckets are created or objects are uploaded, if you do not explicitly assign an ACL to them, they are given the default ACL. You can change the default ACL given to an object; the process to do so is described in [Changing default object ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects). Note that when you change the default ACL, the ACLs of objects that already exist in the bucket or buckets that already exist in the project remain unchanged.

### Default bucket ACLs

All buckets are owned by the project owners group. Additionally, project owners are granted `OWNER` permission for any buckets inside their project that use a predefined ACL.

If you create a bucket with the default bucket ACL—that is, you do not specify a predefined ACL when you create the bucket—your bucket has the predefined `projectPrivate` ACL applied to it.

### Default object ACLs

By default, anyone who has `OWNER` permission or `WRITER` permission on a bucket can upload objects into that bucket. When you upload an object, you can provide a predefined ACL or not specify an ACL at all. If you don't specify an ACL, Cloud Storage applies the bucket's default object ACL to the object. Every bucket has a default object ACL, and this ACL is applied to all objects uploaded to that bucket without a predefined ACL or an ACL specified in the request (JSON API only). The initial value for the default object ACL of every bucket is `projectPrivate`.

Based on how objects are uploaded, object ACLs are applied accordingly:

  * **Authenticated Uploads**

If you make an authenticated request to upload an object and do not specify any object ACLs when you upload it, then you are listed as the owner of the object and the predefined `projectPrivate` ACL is applied to the object by default. This means:

    * You (the person who uploaded the object) are listed as the object owner. Object ownership cannot be changed by modifying ACLs. You can change object ownership only by replacing an object.

    * You (the object owner) are granted `OWNER` permission on the object. If you attempt to give less than `OWNER` permission to the owner, Cloud Storage automatically escalates the permission to `OWNER`.

    * The project owners and project editors group have `OWNER` permission on the object.

    * The project team members group has `READER` permission on the object.

  * **Anonymous Uploads**

If an unauthenticated (anonymous) user uploads an object, which is possible if a bucket grants the `allUsers` group `WRITER` or `OWNER` permission, then the default bucket ACLs are applied to the object as described previously.

Anonymous users cannot specify a predefined ACL during object upload.


**Important:** If you change the default object ACL for a bucket, the change may take time to propagate, and new objects created in the bucket may still get the old default object ACL for a short period of time (see [Consistency](https://docs.cloud.google.com/storage/docs/consistency)). In order to make sure that new objects created in the bucket will get the updated default object ACL, you should wait at least 30 seconds between changing the default object ACL and creating new objects.

## ACL behavior

Cloud Storage helps you adhere to [best practices](https://docs.cloud.google.com/storage/docs/access-control#best-practices) by enforcing some ACL modification rules, which prevent you from setting ACLs that make data inaccessible:

  * **You cannot apply an ACL that specifies a different bucket or object owner.**

Bucket and object ownership cannot be changed by modifying ACLs. If you apply a new ACL to a bucket or object, be sure that the bucket or object owner remains unchanged in the new ACL.

  * **The bucket or object owner always has`OWNER` permission of the bucket or object.**

The owner of a bucket is the project owners group, and the owner of an object is either the user who uploaded the object, or the project owners group if the object was uploaded by an anonymous user.

When you apply a new ACL to a bucket or object, Cloud Storage respectively adds `OWNER` permission to the bucket or object owner if you omit the grants. It does _not_ grant the project owners group `OWNER` permission for an object (unless the object was created by an anonymous user), so you must explicitly include it.




You cannot apply ACLs that change the _ownership_ of a bucket or object (which should not be confused with the `OWNER` permission). Once created in Cloud Storage, bucket and object ownership are permanent. You can, however, effectively change the ownership of objects (but not buckets) by replacing them. Replacement is basically a delete operation followed immediately by an upload operation. During an upload operation, the person who is performing the upload becomes the owner of the object. Keep in mind that to replace an object, the person performing the replacement (and gaining ownership of the object by doing so) must have `WRITER` or `OWNER` permission on the bucket in which the object is being uploaded.

**Note:** You can disable **all** ownership properties of a bucket and the objects within it by [enabling uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set). Doing so also removes all use of ACLs in the bucket, making [IAM policies](https://docs.cloud.google.com/storage/docs/access-control/iam) the only access control system used by the bucket.

## What's next

  * Learn how to [use ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).
  * Learn how to simplify your access control using [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
  * Learn about [best practices for using ACLs](https://docs.cloud.google.com/storage/docs/access-control#best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
