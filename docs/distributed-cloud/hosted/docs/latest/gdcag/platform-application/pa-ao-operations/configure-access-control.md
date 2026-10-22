---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-access-control/
title: Configure access control \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:12.701827+00:00
---

# Configure access control  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure access control Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage access control in the Managed Harbor Service registry while adhering to the principles of least privilege. Google Distributed Cloud (GDC) air-gapped Organization IAM Administrators control who can be authenticated and authorized to use Managed Harbor Service APIs. For authorizing APIs and access in a Harbor instance, use Harbor's built-in role-based access control in each Harbor project. For more information, see <https://goharbor.io/docs/2.8.0/administration/managing-users/>.

## Configure access for Managed Harbor Service APIs

Every GDC Managed Harbor Service API requires that the principal making the request has the required permissions to use the API resource. Permissions are given to principals by setting policies that grant the principal a predefined role on the resource.

### Predefined Managed Harbor Service roles

Managed Harbor Service provides predefined roles that grant access to related API resources and prevent unauthorized access to other resources.

Use the following predefined roles for managing the Harbor Instance resources and creating Harbor Project resources:

  * Harbor Instance Viewer: views and gets the Harbor instance. Ask your IAM Org Admin to grant you the Harbor Instance Viewer (`harbor-instance-viewer`) role.
  * Harbor Instance Admin: creates and manages the Harbor instance, and creates Harbor projects in the Harbor instance. Ask your IAM Org Admin to grant you the Harbor Instance Admin (`harbor-instance-admin`) role.
  * Harbor Project Creator: creates Harbor projects in the Harbor instance. Ask your IAM Org Admin to grant you the Harbor Project Creator (`harbor-project-creator`) role.



## Configure access for APIs and within a Harbor instance

Within a Harbor instance, use Harbor's built-in role-based access control in each Harbor project to control who is authorized to use the APIs and access resources in the Harbor project. For more information, see <https://goharbor.io/docs/2.8.0/administration/managing-users/>.

The user that creates the Harbor project is automatically assigned the `ProjectAdmin` role for the Harbor project. The `ProjectAdmin` user can assign roles for the Harbor project to other users. For all of the available roles, see <https://goharbor.io/docs/2.8.0/administration/managing-users/user-permissions-by-role/>.

## Use service accounts to interact with MHS

You can use service accounts to interact with MHS. Using a project service account integrates your automation directly into the GDC IAM authentication flow, allowing your workloads to generate short-lived tokens automatically without manually managing static credentials.

To set up, activate the identity, and grant project permission to automate authentication for MHS, follow the steps in [Manage service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities).

After completing these setup steps, your service account identity can securely interact with your Harbor instances and manage container repositories.

## What's next

After configuring your command-line tools and access controls for the project service account, review standard practices for rotating keys and managing long-term service account security:

  * [Secure service account keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/secure-service-account-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
