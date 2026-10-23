---
url: https://docs.cloud.google.com/iam/docs/choose-predefined-roles/
title: Find the right predefined roles \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:05.280668+00:00
---

# Find the right predefined roles  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/choose-predefined-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Find the right predefined roles Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) provides multiple [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) for most Google Cloud services. Each predefined role contains the permissions that are needed to perform a task, or a group of related tasks. This document helps you choose the right predefined roles for a given task.

For some tasks, finding an appropriate predefined role is often straightforward. For example, if a principal needs to view objects in a Cloud Storage bucket, then the Storage Object Viewer role (`roles/storage.objectViewer`) is likely to be a good fit.

However, there are hundreds of predefined roles, which can make it difficult to identify the most appropriate roles to grant to your principals. It can also be challenging to find roles that follow the principle of least privilege, which states that principals should have no more permissions than they actually need.

**Note:** If you're getting started with Google Cloud, you can identify and grant core IAM roles as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

This page walks you through the process of manually choosing the most appropriate predefined roles:

  1. Identify the necessary permissions.
  2. Find roles that contain the permissions.
  3. Choose the most appropriate roles.
  4. Decide where to grant the roles.
  5. Grant the roles to a principal.



Alternatively, you can ask Gemini to suggest the predefined roles that a principal needs to perform a given task. For more information about this feature, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

## Identify the necessary permissions

To identify the permissions that a principal needs, start by listing the tasks that they need to perform, and the Google Cloud services that they'll use for those tasks. For example, a principal might need to use Compute Engine to create virtual machine instances.

After you identify the tasks and services, there are a few strategies you can use to identify the necessary permissions for each task:

  * Check the documentation for the Google Cloud services.

For some services, the task-oriented how-to guides list the roles or permissions that you need for each task, either in a "Before you begin" section or with the instructions for each task. For example, see the Compute Engine [prerequisites for importing and exporting VM images](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images).

Some other services identify required roles and permissions on a page about access control. For example, see the Pub/Sub [required permissions for calling Pub/Sub methods](https://docs.cloud.google.com/pubsub/docs/access-control#required_permissions).

  * Identify the REST or RPC API methods that you would use to complete the tasks, and check the API reference documentation for the required IAM permissions.

For some services, the REST and RPC API documentation lists the permissions that each method requires. For example, see the Compute Engine documentation for the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get#iam-permissions).

  * Look at the list of permissions for each service, and use your judgment to find the relevant permissions.

In most cases, the name of each permission also describes what the permission lets you do with it. For example, the permission for creating a Compute Engine VM instance is named `compute.instances.create`.

To help you understand each permission name, remember that permission names use the format `SERVICE.RESOURCE_TYPE.ACTION`.




In general, you don't need to identify every permission that's required for every task. Instead, focus on identifying the most relevant permission for each task. If a predefined role contains that permission, it's likely to contain related permissions as well.

As part of this process, you should also try to identify which of the required permissions are the most powerful. In general, more powerful permissions are included in a smaller number of predefined roles. As a result, if you focus on these permissions, you'll have a shorter list of potential roles to choose from.

For example, the following types of permissions are especially powerful:

  * Permissions to create and delete resources
  * Permissions to access sensitive data, such as encryption keys or personally identifiable information (PII)
  * Permissions to set the allow policy or deny policy for a resource
  * Permissions to update organizations, folders, and projects, which can cause other resources to inherit the updates



In contrast, the following types of permissions are less powerful:

  * Permissions to list resources
  * Permissions to access data that is not sensitive
  * Permissions to update settings that have limited risk, such as the minimum CPU platform for Compute Engine virtual machine instances



## Find roles that contain the permissions

**Note:** Identity and Access Management (IAM) offers predefined roles that are tailored to specific job functions. If you want to give a user the necessary permissions to perform a specific job function in your organization, consider granting one of these predefined roles. To determine if IAM offers a predefined role for your use case, see [Predefined roles for job functions](https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions). 

After you identify the required permissions, you can search for predefined roles that contain those permissions and make a list of roles that might be a good fit. The easiest way to find these roles is by searching the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions) for a permission and clicking on the permission name. The reference for each permission tells you the roles that contain the permission.

To follow the principle of least privilege, you might need to identify more than one predefined role to grant, especially if the required permissions belong to multiple Google Cloud services. For example, if a principal needs to view Cloud Storage objects and administer Cloud SQL databases, it's unlikely that a single predefined role contains the appropriate permissions for both services. If such a role exists, it might also include a large number of unrelated permissions that the principal doesn't need. To reduce risk, look for one role that contains the required permissions for Cloud Storage, and another role that contains the required permissions for Cloud SQL.

## Choose the most appropriate roles

Now that you have a list of predefined roles that might be a good fit, you can choose the most appropriate roles from the list.

Start by eliminating the following types of roles:

  * For production environments: Basic roles, including Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`).

Basic roles include thousands of permissions across all Google Cloud services. In production environments, do not grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles or custom roles that meet your needs.

  * Service agent roles, which typically have titles that end in "Service Agent" and names that end in `serviceAgent`.

These roles are intended for [service agents](https://docs.cloud.google.com/iam/docs/service-agents), which are a special type of service account that a Google Cloud service uses to access your resources. Service agent roles tend to contain permissions for multiple services, which might include services that your principal doesn't need to access.




Next, use the [predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions) or the [**Roles** page in the Google Cloud console](https://console.cloud.google.com/iam-admin/roles) to list the permissions that each role contains. We recommend choosing predefined roles that contain all of the permissions that a user is likely to need for a given use case. Each service provides broad Admin, Editor, and Viewer roles that serve this purpose. For example, the Bigtable Admin role provides administrative permissions to create new instances and access to all table data in a project, and the Bigtable Viewer role provides view-only access to the Bigtable in the Google Cloud console.

Optionally, check each role for permissions that you don't want the principal to have, and eliminate any roles that contain unwanted permissions. If this process eliminates all of the predefined roles, consider creating a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to fit your use case.

Choosing roles based on the permissions that a user is likely to need balances the principle of least privilege with the need to anticipate users' future access requirements. However, if you want to strictly adhere to least privilege, select the role or roles that contain the fewest permissions.

## Decide where to grant the roles

When you grant a role, you always grant it on a specific Google Cloud _resource_ , which belongs to a [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy). Lower-level resources, such as Compute Engine VM instances, inherit the roles granted on higher-level resources, such as projects, folders, and organizations.

**Note:** Granting a role is also known as creating a _role binding_ in an _allow policy_. Lower-level resources inherit the allow policies and role bindings of higher-level resources.

Choose where to grant the predefined roles that you identified:

  * If the principal needs access to specific lower-level resources, grant the roles on those resources.
  * If the principal needs access to many resources within a project, folder, or organization, grant the roles on the project, folder, or organization. Choose the lowest-level resource that meets the principal's needs.

Also, consider using IAM Conditions to [grant the roles only on specific resources](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access) within the project, folder, or organization.




If you identified multiple predefined roles, consider whether you should grant the roles at different levels of the resource hierarchy. For example, if a principal needs access to a single Cloud SQL database, but many different Compute Engine VM instances, you might want to grant the role for Cloud SQL on the database and the role for Compute Engine on the project.

## Grant the roles to a principal

Now you're ready to grant the roles to your principal. To learn how to grant roles, see the following:

  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)
  * [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)
  * [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources)

After you grant the roles, you can use the [Policy Analyzer and Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/overview) to check which resources the principal can access and troubleshoot access issues. 

If the principal has the intended permissions on the correct resources, but they are unable to complete their tasks, it's possible that you overlooked a permission that the principal needs. Iterate on your previous attempt by adding required permissions to the list; finding roles that contain those permissions; and choosing the most appropriate roles.

If you accidentally grant a role with too many permissions, then a [role recommendation](https://docs.cloud.google.com/iam/docs/recommender-overview) might suggest a less permissive role that would meet the principal's needs. Some role bindings [don't get role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#role-recommendation-availability). 

## What's next

  * Learn how the [Policy Simulator](https://docs.cloud.google.com/iam/docs/understanding-simulator) can help you test changes to a principal's roles.


  * Find out how the [Policy Analyzer](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy) can tell you what access a principal has to a resource.


  * Get details about [troubleshooting access issues](https://docs.cloud.google.com/iam/docs/troubleshoot-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
