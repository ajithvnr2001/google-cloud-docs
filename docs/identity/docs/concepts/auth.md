---
url: https://docs.cloud.google.com/identity/docs/concepts/auth/
title: Authentication and authorization \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:36.023275+00:00
---

# Authentication and authorization  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authentication and authorization

Most Google Cloud APIs grant permissions to users, groups, or service accounts based on their [IAM roles](https://cloud.google.com/iam/docs/understanding-roles). However, the Cloud Identity Groups API grants permissions based on these three authorization modes:

  * Admin authorization
  * Non-admin authorization
  * Namespace authorization



This guide explains each of these authorization modes.

## Admin authorization

The _Admin authorization_ mode grants a user full access to all Google Groups in a domain. Any user who has the [_groups administrator privilege_](https://support.google.com/a/answer/1219251) has Admin authorization. Only the [super administrator](https://support.google.com/a/answer/2405986) for the domain can grant a user the groups administrator privilege.

For more information on granting groups administrator privilege, refer to [Assign administrator roles to a user](https://support.google.com/a/answer/172176).

## Non-admin authorization

_Non-admin authorization_ is an authorization mode for Google Groups that grants non-administrator users access to Google Groups based on the domain settings, group's settings and, in the case of permissions on an individual group, their [membership roles](https://docs.cloud.google.com/identity/docs/groups) in that groups.

By default, all users are able to create groups in that domain. However, domain administrators can modify the domain settings for Google Groups using the Admin Console. For information on modifying domain settings, refer to [Set Groups for Business sharing options](https://support.google.com/a/answer/167097).

The owners are able to set the permissions for each membership role for a group. Default settings are as follows:

  * Non-members can see the group and its details when calling read-only `GroupsService` APIs. They can also see memberships and their details when calling read-only `MembershipsService` APIs.

  * Members have the same permissions as non-members.

  * Managers have all the permissions of members, plus the permission to manage memberships and membership roles for non-owner members.

  * Owners have all the permissions of managers, plus the permissions to modify the group's metadata, delete a group, and manage all memberships and membership roles.




To modify group settings, [Create a group and choose group settings](https://support.google.com/groups/answer/2464926).

## Namespace authorization

_Namespace authorization_ is an authorization mode for identity groups that grants service accounts access to identity groups synced from the same identity source. Namespace authorization can only be granted by [Cloud Search](https://developers.google.com/cloud-search).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
