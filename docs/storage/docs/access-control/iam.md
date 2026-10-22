---
url: https://docs.cloud.google.com/storage/docs/access-control/iam/
title: Identity and Access Management \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:35.192424+00:00
---

# Identity and Access Management  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Identity and Access Management Stay organized with collections  Save and categorize content based on your preferences. 

[Usage](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

This page provides an overview of Identity and Access Management (IAM) and its use with controlling access to the buckets, managed folders, and objects resources in Cloud Storage.

  * To learn about other ways of controlling access in Cloud Storage, see [Overview of Access Control](https://docs.cloud.google.com/storage/docs/access-control).

  * For a detailed discussion of IAM and its features generally, see [Identity and Access Management](https://docs.cloud.google.com/iam).




## Overview

IAM allows you to control who has access to the _resources_ in your Google Cloud project. Resources include Cloud Storage buckets, the managed folders within buckets, and objects stored within buckets, as well as other Google Cloud entities such as [Compute Engine instances](https://docs.cloud.google.com/compute).

_Principals_ are the "who" of IAM. Principals can be individual users, groups, domains, or even the public as a whole. Principals are granted _roles_, which give them the ability to perform actions in Cloud Storage as well as Google Cloud more generally. Each role is a collection of one or more _permissions_. Permissions are the basic units of IAM: each permission lets you perform a certain action.

For example, the `storage.objects.create` permission lets you create objects. This permission is found in roles such as Storage Object Creator (`roles/storage.objectCreator`), which grants the permissions useful for creating objects in a bucket, and Storage Object Admin (`roles/storage.objectAdmin`), which grants a wide range of permissions for working with objects.

The collection of IAM roles that you set on a resource is called an IAM _policy_. The access granted by these roles apply to both the resource on which the policy is set and any resources contained within that resource. For example, you can set an IAM policy on a bucket that gives a user administrative control of that bucket and its objects. You can also set an IAM policy on the overall project that gives another user the ability to view objects in any bucket within that project.

You can also use [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to deny access to resources. When a deny policy is attached to a resource, the principal in the policy can't use the specified permission to access the resource or any sub-resource within it, regardless of the roles they're granted. Deny policies override any IAM allow policies.

**Note:** While you can set IAM policies on buckets, managed folders, and projects in order to control access to objects within them, you cannot set IAM policies directly on individual objects. In addition, you can't set IAM deny policies on buckets, managed folders, or individual objects.

## Permissions

Permissions allow principals to perform specific actions on buckets, managed folders, or objects in Cloud Storage. For example, the `storage.buckets.list` permission allows a principal to list the buckets in your project. You don't directly give principals permissions; instead, you grant roles, which have one or more permissions bundled within them.

For a reference list of the IAM permissions that apply to Cloud Storage, see [IAM Permissions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions).

## Roles

Roles are a bundle of one or more permissions. For example, the Storage Object Viewer (`roles/storage.objectViewer`) role contains the permissions `storage.objects.get` and `storage.objects.list`. You grant roles to principals, which allows them to perform actions on the buckets, managed folders, and objects in your project.

For a reference list of the IAM roles that apply to Cloud Storage, see [IAM Roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

### Granting roles at the project level, bucket level, or managed folder level

You can grant roles to principals at the project level, bucket level, or managed folder level. The permissions granted by those roles apply additively throughout the resource hierarchy. You can grant roles at different levels of the resource hierarchy for more granularity in your permissions model.

For example, say you want to give a user permission to read objects in any bucket within a project but create objects only in bucket A. To achieve this, you can give the user the Storage Object Viewer (`roles/storage.objectViewer`) role for the project, which allows the user to read any object stored in any bucket within your project, and the Storage Object Creator (`roles/storage.objectCreator`) role for bucket A, which allows the user to create objects only in that bucket.

Some roles can be used at all levels of the resource hierarchy. When used at the project level, the permissions they contain apply to all buckets, folders, and objects in the project. When used at the bucket level, the permissions only apply to a specific bucket and the folders and objects within it. Examples of such roles are the Storage Admin (`roles/storage.admin`) role, the Storage Object Viewer (`roles/storage.objectViewer`) role, and the Storage Object Creator (`roles/storage.objectCreator`) role.

Some roles can only be applied at one level. For example, you can only apply the Storage Legacy Object Owner (`roles/storage.legacyObjectOwner`) role at the bucket level or at the managed folder level. The [IAM roles](https://docs.cloud.google.com/iam/docs/deny-access#required-roles) that allow you to control IAM deny policies can only be applied at the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) level.

**Caution:** Setting IAM policies at project, bucket, and managed folder levels potentially allow users access to objects that they did not have previously. Carefully evaluate your policies before setting them.**Note:** When you view the IAM policy for a project, you don't see the IAM policies that exist for individual buckets. If you view the IAM policy for an individual bucket using the [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console), you do see project-level permissions that apply to that bucket; however, other Cloud Storage tools, such as [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) and the [Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries) only return the policy of the bucket and don't include information inherited from the project-level policy. Be sure to consult both project and bucket policies when evaluating access levels for principals.

### Relation to ACLs

In addition to IAM, your buckets and objects can use a legacy access control system called [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) if the [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) feature is not enabled for your bucket. Generally, [you should avoid using ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#iam-vs-acl), and you should enable uniform bucket-level access for your bucket. This section discusses what you should keep in mind if you allow ACL usage for a bucket and the objects within it.

_Legacy Bucket_ IAM roles work in tandem with [bucket ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#permissions): when you add or remove a Legacy Bucket role, the ACLs associated with the bucket reflect your changes. Similarly, changing a bucket-specific ACL updates the corresponding Legacy Bucket IAM role for the bucket.

Legacy Bucket role | Equivalent ACL  
---|---  
Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) | Bucket Reader  
Storage Legacy Bucket Writer (`roles/storage.legacyBucketWriter`) | Bucket Writer  
Storage Legacy Bucket Owner (`roles/storage.legacyBucketOwner`) | Bucket Owner  
  
All other bucket-level IAM roles, including _Legacy Object_ IAM roles, work independently from ACLs. Similarly, all project-level IAM roles work independently from ACLs. For example, if you give a user the Storage Object Viewer (`roles/storage.objectViewer`) role, the ACLs remain unchanged.

Because object ACLs work independently from IAM roles, they don't appear in the hierarchy of IAM policies. When evaluating who has access to one of your objects, make sure you [check the ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#retrieving-acls) for the object, in addition to checking your project-level and bucket-level IAM policies.

#### IAM deny policies versus ACLs

[IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) apply to access granted by ACLs. For example, if you create a deny policy that denies a principal the `storage.objects.get` permission on a project, the principal cannot view objects in that project, even if they are granted the `READER` permission to individual objects.

#### IAM permission for changing ACLs

You can use IAM to give principals the permission needed to change ACLs on objects. The following `storage.buckets` permissions together allow users to work with bucket ACLs and default object ACLs: `.get`, `.getIamPolicy`, `.setIamPolicy`, and `.update`.

Similarly, the following `storage.objects` permissions together allow users to work with object ACLs: `.get`, `.getIamPolicy`, `.setIamPolicy`, and `.update`.

### Custom roles

While IAM has many predefined roles that cover common use cases, you may want to define your own roles which contain bundles of permissions that you specify. To support this, IAM offers [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Principal types

There are a number of different types of principals. For example, Google Cloud accounts represent a general type, while `allAuthenticatedUsers` and `allUsers` are two specialized types. For a list of principal types in IAM, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). For more information about principals in general, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview).

### Convenience values

Cloud Storage supports _convenience values_ , which are a special set of principals that can be applied specifically to your IAM bucket policies. You should generally avoid using convenience values in production environments, because they require granting [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), a practice which is discouraged in production environments.

A convenience value is a two-part identifier consisting of a [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) and a project ID:

  * `projectOwner:PROJECT_ID`
  * `projectEditor:PROJECT_ID`
  * `projectViewer:PROJECT_ID`



A convenience value acts as a bridge between the principals granted the basic role and an IAM role: the IAM role granted to the convenience value is, in effect, also granted to all principals of the specified basic role for the specified project ID.

For example, say jane@example.com and john@example.com have the Viewer (`roles/viewer`) basic role for a project named `my-example-project`, and say you have a bucket in that project named `my-bucket`. If you grant the Storage Object Creator (`roles/storage.objectCreator`) role for `my-bucket` to the convenience value `projectViewer:my-example-project`, then both jane@example.com and john@example.com gain the permissions associated with the Storage Object Creator role for `my-bucket`.

You can grant and revoke access to convenience values for your buckets, but note that Cloud Storage automatically applies them in certain circumstances. See [modifiable behavior for basic roles in Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#basic-roles-modifiable) for more information.

## Conditions

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) lets you set conditions that control how permissions are granted or denied to principals. Cloud Storage supports the following types of condition attributes:

  * [`resource.name`](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcename_attribute): Grant or deny access to buckets and objects based on the bucket or object name. You can also use [`resource.type`](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcetype_attribute) to grant access to either buckets or objects, but doing so is mostly redundant with using `resource.name`. The following example condition applies an IAM setting to all objects with the same prefix: 
        
        resource.name.startsWith('projects/_/buckets/BUCKET_NAME/objects/OBJECT_PREFIX')

  * [Date/time](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time): Set an expiration date for the permission. 
        
        request.time < timestamp('2019-01-01T00:00:00Z')




These conditional expressions are logic statements that use a subset of the [Common Expression Language](https://github.com/google/cel-spec) (CEL). You specify conditions in the role bindings of a bucket's IAM policy.

**Note:** You can also use double quotes in your conditional expressions, but they should be properly escaped when you are using Google Cloud CLI commands and HTTP/REST requests to update a conditional policy. For example, `request.time < timestamp(\"2019-01-01T00:00:00Z\")`.

Keep these restrictions in mind:

  * You must enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) on a bucket before adding conditions at the bucket level. Although conditions are allowed at the project level, you should migrate all buckets in the project to uniform bucket-level access to prevent Cloud Storage ACLs from overriding project-level IAM conditions. You can apply a [uniform bucket-level access constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access) to enable uniform bucket-level access for all new buckets in your project.
  * Managed folders can be specified as a resource in IAM allow policy conditions. Managed folders can't be specified as a resource in IAM deny policy conditions. IAM deny policy conditions can only be set by using tags, and tags don't support managed folders.
  * IAM deny policies can only be applied to project, folder, and organization resources. They can't be applied to buckets or managed folders.
  * When using the JSON API to call [`getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) and [`setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) on buckets with conditions, you must set the [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions) to 3.
  * Since the `storage.objects.list` permission is granted at the bucket level, you cannot use the `resource.name` condition attribute to restrict object listing access to a subset of objects in the bucket.
  * Expired conditions remain in your IAM policy until you remove them.



## Using with Cloud Storage tools

Although IAM permissions cannot be set through the XML API, users granted IAM permissions can still use the XML API, as well as any other tool for accessing Cloud Storage.

For references on which IAM permissions allow users to perform actions with different Cloud Storage tools, see [IAM references for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-reference).

## What's next

  * [Learn how to use IAM with Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  * [Review the IAM reference table for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-reference).
  * Learn about [best practices for using IAM](https://docs.cloud.google.com/storage/docs/access-control#best-practices).
  * [Manage IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for all of your Google Cloud resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
