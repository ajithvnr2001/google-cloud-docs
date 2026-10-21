---
url: https://docs.cloud.google.com/docs/get-started/authorization-access-control/
title: Authorization and access control \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:26.931499+00:00
---

# Authorization and access control  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/authorization-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Authorization and access control Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) is a tool that lets you control who can do what in your Google Cloud environment.

Access is controlled with IAM permissions, which are required to work with any resource in a Google Cloud environment. When you're given the permissions to work with a resource, you are _authorized_ to access that resource. Without the proper authorization, you can't access Google Cloud resources.

## Permissions and roles

To work with a resource, your user account must have the relevant permissions to access that resource.

Typically, your IAM administrator is responsible for controlling access to resources. Your administrator can give you permissions to access a single resource or all the resources in a project, folder, or organization. Administrators grant the relevant permissions to your user account in bundles called _roles_. As long as your user account has a role with the appropriate permissions, you can use that role to access Google Cloud resources.

Generally, the workflow to perform an action on any resource in your Google Cloud environment looks like this:

  1. You want to perform an action on a resource—for example, upload an object to a Cloud Storage bucket—but you don't have the appropriate permissions. Without the permissions, you can't perform the action.
  2. You can request the permissions you need from your IAM administrator through your preferred request management system or directly from the permission error message in the Google Cloud console.
  3. Your IAM administrator grants a role that contains the appropriate permissions to your user account. You can now perform the action.



## Using IAM as an administrator

Administrators are typically responsible for granting roles to users so they can access Google Cloud resources. Users are represented by authenticated identities known as _principals_.

Granting roles to a principal on a resource involves editing the _allow policy_ that's attached to the resource. Allow policies list which principals have access to the resource and what actions they can perform on the resource. IAM uses allow policies to determine whether a principal has the required permissions to access the resource. Therefore, to grant a principal access to a particular resource, you must update the allow policy for the resource with the principal and the roles that you want to grant.

Administrators can grant roles to principals on the following types of resources:

  * **Projects, folders, and organizations** : These resources are the container resources used to structure your [resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). Roles that you grant on these container resources apply to all of the service-specific resources they contain.
  * **Service-specific resources** : These resources are the features or components offered by a service. For example, Compute Engine has resources like instances, disks, and subnetworks. Granting roles on a service-specific resource provides more granular access control than granting roles on a container resource, because it limits a user's access to just that resource.



## Advanced access control with IAM

Allow policies are the most common method for controlling access to a Google Cloud environment with IAM. But IAM also offers other options for access control, including the following:

  * Additional policy types, like deny and principal access boundary policies
  * Conditional attribute-based access controls
  * Temporary access controls like Privileged Access Manager (PAM)



## Other forms of access control

Although IAM is the primary method of access control for Google Cloud, there are other Google Cloud services that can affect a user's access to resources.

The following are some examples of other services that can affect a user's access:

  * [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview): Access Context Manager lets you define fine-grained, attribute-based access control for projects and resources in Google Cloud.
  * [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview): IAP uses an application-level access control model where you establish a central authorization layer for applications accessed by HTTPS.
  * [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview): Organization Policy lets you configure constraints across your resource hierarchy to give you centralized and programmatic control over your organization's cloud resources.
  * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview): VPC Service Controls lets you define perimeters that help protect the Google Cloud resources and data of Google Cloud services that you explicitly specify.



## What's next

  * For a more in-depth description of the IAM system and how it works, see the [IAM overview page](https://docs.cloud.google.com/iam/docs/overview) in the IAM documentation.
  * For information on IAM error messages, see [Permission error messages](https://docs.cloud.google.com/iam/docs/permission-error-messages) in the IAM documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
