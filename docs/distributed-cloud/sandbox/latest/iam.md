---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/iam/
title: Manage identity and access \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:44.837043+00:00
---

# Manage identity and access  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Manage identity and access Stay organized with collections  Save and categorize content based on your preferences. 

By default, GDC Sandbox comes with a pre-configured, fake OpenID Connect (OIDC) identity provider and a user account to test your workflow lifecycles. For details on identity providers, see [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/iam/connect-identity).

The first page upon accessing the GDC console is the fake OIDC Provider, and you can return there at any time by selecting **Logout** in the banner. From this screen, you can select any user account in your instance and sign in as that user.

For all tasks you perform in GDC Sandbox, you can use the default platform administrator account, associated with the email `fop-platform-admin@example.com`. You can select this account when you sign into the GDC console, assign yourself roles and permissions, and manage your projects.

While you are signed on to the instance using this account, you can create additional users. The [project creation](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/create-project) instructions on a later page describe how to add new users as part of the project setup process.

The fake OIDC identity provider simplifies the GDC Sandbox experience. Some differences between this provider and a real one:

  * This provider does not check for passwords or other authentication. Any user who can [connect](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect) to the instance can select any of the existing accounts managed by the fake OIDC identity provider, and sign into the instance using that account.
  * The accounts managed by this provider don't have a direct connection to the Google Cloud accounts of the users who have access to your instance. You can create fake OIDC provider accounts with the same username as your team members who are using the instance, and this may be a useful convention, but the system does not enforce that specific individuals use specific accounts in the instance. Anyone who can connect to the instance can choose any account to sign in.
  * These accounts also don't have any connection to the "gateway accounts" that are used when you [connect](https://docs.cloud.google.com/distributed-cloud/sandbox/latest//connect) to the gateway VM from your personal computer.



Don't remove the Platform Admin account `fop-platform-admin@example.com`, or remove the Organization IAM Admin role from that account.

## Roles and permissions

For each operation you test on a service, you must have the required roles and permissions. For a list of all available required roles, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/iam/role-definitions).

You can grant the necessary roles to yourself using the default user account GDC Sandbox provides you. Before granting a yourself a role to test a service, you must have the Project IAM Admin (`project-iam-admin`) role. To grant yourself a role, [install `gdcloud`](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud) if you plan to use the command line, and review the GDC console and gdcloud CLI instructions in [Set up role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/iam/set-up-role-bindings#set-up-role-bindings). Replace all instances of `USER_EMAIL` with `fop-platform-admin@example.com`.

To see a list of all roles you've assigned to yourself, do the following:

  1. In the Console menu, click **org-1 > Select project**.
  2. Click your preferred project.
  3. In the **Projects** page, you see a list of all assigned roles by the default user email.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
