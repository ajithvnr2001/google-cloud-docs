---
url: https://docs.cloud.google.com/identity/docs/how-to/manage-expirations/
title: Managing membership expirations \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:27:04.530369+00:00
---

# Managing membership expirations  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/manage-expirations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing membership expirations

This page explains how to update and retrieve expiration settings for group memberships, and the expiration notifications group owners receive.

**Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education, and Cloud Identity Premium accounts.

Membership expiration allows group owners, group managers, Google Workspace Super Admins, or Workspace Delegated Admins with group admin privileges to manage groups and groups-based access to resources. Access can be limited based on membership staleness or temporary need without manually removing members. The Groups API enables membership expiration for the following use cases:

  * Time-limited access to resources (for example, to allow someone to help troubleshoot a problem in production)
  * Temporary membership in a communications group (for example, to briefly include a person into a team group on a long-term project)



Expirations can be applied to all types of group members (including users, groups, and service accounts) if they have a `MEMBER` role. When you set an expiration for a member that is a group, that expiration becomes the default expiration for all child members of that group unless the child member has a direct membership in the parent group with an individual expiration already applied. The expiration also applies to all new members of the child group going forward.

## Before you begin

Set up authentication and install the client libraries. See [Setting up the Cloud Identity Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup) to learn how.

## Adding a membership with expiration

See [Managing Google Group memberships for Google Groups](https://docs.cloud.google.com/identity/docs/how-to/memberships-google-groups) or [Managing identity-mapped group memberships](https://docs.cloud.google.com/identity/docs/how-to/memberships-identity-groups) to learn how.

## Updating the expiration of a membership

To update the expiration of a membership, call [`groups.memberships.modifyMembershipRoles()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles) with the ID of the parent group, the ID of the membership, and an [`UpdateMembershipRolesParams`](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/modifyMembershipRoles#updatemembershiprolesparams) resource. Because members can have more than one [`MembershipRole`](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#MembershipRole) in a group, you must specify which role will have the expiration. Currently only the `MEMBER` role may have an expiration applied to it.

**Note:** To get the ID of the membership, call [groups.memberships.lookup()](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/lookup) with the ID of the parent group and the `memberKey` of the member.

**Sample request body**
    
    
    {
      "updateRolesParams": [
        {
          "fieldMask": "expiry_detail.expire_time",
          "membershipRole": {
            "expiryDetail": {
              "expireTime": "2021-10-02T15:01:23Z"
            },
            "name": "MEMBER"
          }
        }
      ]
    }
    

## Retrieving a membership expiration

To retrieve the membership expiration of a membership, call [`groups.memberships.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/get) with the ID of the parent group and the ID of the membership.

**Note:** To get the ID of the membership, call [`groups.memberships.lookup()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/lookup) with the ID of the parent group and the `memberKey` of the member.

## Email notifications

Email notifications are automatically sent to all group owners when memberships are about to expire. Notifications are sent 72 hours before expiration or immediately if the membership will expire before 72 hours when it is set. The notifications are sent in each group owner's preferred language, as defined by the domain administrator in the Google Admin console or by the group owner individually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
