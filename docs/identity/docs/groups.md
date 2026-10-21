---
url: https://docs.cloud.google.com/identity/docs/groups/
title: Groups API overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:23.976037+00:00
---

# Groups API overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Groups API overview

The Cloud Identity Groups API allows you to create and manage different types of groups, each of which supports different features, as well as their memberships.

**Note:** The Cloud Identity Groups API only works with [Google Groups for Business](https://support.google.com/a/answer/33329). If you want to create and manage non-business Google Groups, you can use the [Google Groups web interface](https://groups.google.com).

## Group types

A _group_ is a collection of _entities_ , where each entity can be either another group or a user. The Cloud Identity Groups API supports the following group types:

_Google Groups_
    Google Groups have an email address and are frequently used as mailing lists. Google Groups can also be used across many Google products. For example. you can share a Google Doc with a group, invite a group to a Google Calendar event, or use a group for access management in IAM. A Google Group is the default group type.
_Dynamic groups_
    

Dynamic groups are Google Groups whose memberships are automatically managed using a membership query or a query on employee attributes, such as job role or building location. For example, a membership query might be "all users whose job role is Technical Writer in my organization."

    **Note:** Dynamic groups are only available to Google Workspace Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity premium accounts. You can create up to 500 dynamic groups per customer. This limit can be increased on a case-by-case basis—contact [Google Workspace Support](https://support.google.com/a/answer/1047213) with your specific use case to request an increase.
_Security groups_
    

A security group is similar to a Google Group, but is used specifically for controlling access to organizational resources. A security group is created by updating a Google Group to a security group.

**Warning:** A security group cannot be changed back to a Google Group.
_Locked groups_
    

A [locked](https://support.google.com/a?p=locked-groups) group is a Google Group that administrators have locked to prevent it from getting out of synchronization with an external source, such as an identity provider. Administrators can also lock a Google Group to increase security for sensitive groups. When you lock a Google Group, edits to core attributes and memberships are restricted to a subset of administrators.

While standard group owners, managers, and members can still update settings like message moderation or posting permissions, modifications to the following attributes are limited to authorized administrators. Authorized administrators are typically those with specific roles or conditions like `Groups Admin` or `Groups Editor` with a condition that includes locked groups.

_POSIX groups_ (Deprecated)
    **Caution:** POSIX groups are [deprecated](https://docs.cloud.google.com/identity/docs/deprecations). As of September 26, 2024, you can no longer create new POSIX groups. For more information, see [POSIX groups deprecation](https://docs.cloud.google.com/identity/docs/deprecations/posix-groups).
    

A POSIX group is a Google Group that is used to manage group membership in LDAP environments. A POSIX group is created by updating a Google Group with POSIX data. The POSIX group data includes a group name and group ID (GID).

POSIX groups are integrated with Google Cloud and are used by VMs in your organization that have OS Login enabled.

    **Note:** You must use the beta version of the Cloud Identity Groups API to create and manage POSIX groups.
_Identity-mapped groups_
    

An identity-mapped group is a group containing users and groups synced from a non-Google identity source, such as Active Directory. Identity-mapped groups allow [Google Cloud Search](https://developers.google.com/cloud-search) to recognize users and groups, and their permissions to searched documents, stored in an external identity source. For example, you might have a user `example_user_org@your_domain.com` who has certain permissions to documents. This user can be synced to `example_user@your_domain.com` so that Google Cloud Search recognizes their same permissions to the same documents.

Cloud Identity Groups API group creation requests are permitted only from service accounts.
    

To sync identity-mapped groups in Google Cloud Search, you must create an identity connector. If you are using Java, you can create an identity connector using the Google Cloud Search Java SDK. If you want to use a REST API, you can use the Cloud Identity Groups API. For further information on identity connectors, refer to [Sync different identity systems](https://developers.google.com/cloud-search/docs/guides/identity-mapping) in the Cloud Search documentation.

**Note:** Identity-mapped groups can only be created and accessed through the Groups API. For example, you cannot view identity groups in the Google Admin console.

## Group properties

Each group, regardless of type, has the following properties:

_Label_
    The label identifies the type of group: 

  * **Google Groups:** `cloudidentity.googleapis.com/groups.discussion_forum`
  * **Dynamic groups:** `cloudidentity.googleapis.com/groups.dynamic`
  * **Security groups:** `cloudidentity.googleapis.com/groups.security` (this label is in addition to `cloudidentity.googleapis.com/groups.discussion_forum`, because security groups are based on Google Groups)
  * **Locked groups:** `cloudidentity.googleapis.com/groups.locked` (this label is in addition to `cloudidentity.googleapis.com/groups.discussion_forum`, because locked groups are based on Google Groups)
  * **POSIX groups:** `cloudidentity.googleapis.com/groups.posix` (this label is in addition to `cloudidentity.googleapis.com/groups.discussion_forum`, because POSIX groups are based on Google Groups)
  * **Identity-mapped groups:** `system/groups/external`


_Entity key_
    

An entity key is a human-readable unique identifier for the group:

  * **Google Groups, dynamic groups, and security groups:** the email address of the group
  * **Identity-mapped groups:** a string qualified with a namespace. The namespace is established when you create an identity source in Google Cloud Search. For further information on identity sources, refer to [Sync different identity systems](https://developers.google.com/cloud-search/docs/guides/identity-mapping) in the Cloud Search documentation.


_Parent_
    

A parent is the resource to which the group belongs. For Google Groups, dynamic groups, and security groups, the parent is the customer who owns the domain. For an identity-mapped group, the parent is the identity source from which the group is synced.

_Display name_
    

The display name is the name of the group as it appears in Google products.

## Memberships and membership properties

An entity that belongs to a group is referred to as a _member_ and its relationship with that group is referred to as a _membership_. Entities can be users, groups, or service accounts. A membership has the following properties:

_Preferred member key_
    A preferred member key is a human-readable unique identifier for the member. For a Google Group or an individual user, the preferred member key is the email address of the group or user. For an identity-mapped group, the preferred member key is a string qualified with a namespace.
_Membership roles_
    

Membership roles represent the permissions that the member has in the group. The supported roles are as follows:

  * `MEMBER`, which has no special permissions. Every membership must have at least the `MEMBER` membership role.

  * `OWNER`, which has broad permissions, such as managing other `OWNER`s or deleting the group.

  * `MANAGER`, which has fewer permissions than an `OWNER`, but more than a `MEMBER`, such as managing other `MANAGER`s.




The permissions that a specific membership role has in a group can be customized in the [Google Groups web interface](https://groups.google.com) or in the [Google Admin console](https://admin.google.com). For more information, see [Set who can view, post & moderate](https://support.google.com/groups/answer/2464975).

You can import users and groups that aren't already in Cloud Identity as an external identity source. You must first create an [identity source](https://docs.cloud.google.com/identity/docs/overview) for your organization, then import user and group information into Cloud Identity.

**Note:** The Google Groups web interface supports other membership roles such as `BANNED`. These memberships will not appear and cannot be managed in Cloud Identity Groups API.

## Next steps

Here are a few next steps you might take:

  * To set up the API, refer to [Setting up the Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup).

  * To create and manage Google Groups, see the [Creating and searching for Google Groups](https://docs.cloud.google.com/identity/docs/how-to/create-google-groups).

  * To learn more about dynamic groups, see the [Dynamic groups overview](https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups).

  * To update a Google Group to a security group, see [Update a Google Group to a security group](https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group).

  * To create and manage identity-mapped groups, see [Creating and searching for identity-mapped groups](https://docs.cloud.google.com/identity/docs/how-to/create-identity-groups).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
