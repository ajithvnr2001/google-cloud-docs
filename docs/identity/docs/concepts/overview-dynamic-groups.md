---
url: https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups/
title: Dynamic groups overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:05.847645+00:00
---

# Dynamic groups overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dynamic groups overview

A _dynamic group_ is a Google Group whose memberships are automatically managed using a membership query or a query on employee attributes, such as job role or building location. For example, a membership query might be "all users whose job role is Technical Writer in my organization."

**Note:** Dynamic groups are only available to Google Workspace Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity premium accounts. You can create up to 500 dynamic groups per customer. This limit can be increased on a case-by-case basis—contact [Google Workspace Support](https://support.google.com/a/answer/1047213) with your specific use case to request an increase.

As part of the group's definition, you supply the query and Google systems ensure that all matching users in your organization are members of the group. Membership queries are written using [_Common Expression Language (CEL)_](https://opensource.google.com/projects/cel) which is the standard language used to write expressions for Google Cloud APIs.

Though dynamic groups are created and maintained differently than Google Groups, they are used for the same purposes. Namely, dynamic groups are used as email groups (to send email to a specific set of people) and for managing Identity and Access Management (IAM) and Google Workspace policies. For further information on IAM policies, see [IAM](https://docs.cloud.google.com/iam). For further information on Google Workspace policies, see [Customize access to Google Workspace services using access groups](https://support.google.com/a/answer/9050643) and [Customize service settings with configuration groups](https://support.google.com/a/answer/9224126).

For introductory information on policies, refer to [Understanding policies](https://docs.cloud.google.com/iam/docs/policies).

**Note:** You cannot add a dynamic group as a member of a regular Google Group.

## Technologies used to create a dynamic group

You can create and manage dynamic groups using the REST API or client libraries.

## What's next

Here are a few next steps you might take:

  * [Formulate and test a membership query](https://docs.cloud.google.com/identity/docs/how-to/test-query-dynamic-groups).
  * [Create a dynamic group](https://docs.cloud.google.com/identity/docs/how-to/create-dynamic-groups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
