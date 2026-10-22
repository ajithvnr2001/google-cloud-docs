---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/create-project/
title: Create your first project \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:09.896858+00:00
---

# Create your first project  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/create-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Create your first project Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a project. To learn more about projects, see [Project overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/project-management) in the Google Distributed Cloud air-gapped documentation.

## Sign in as Platform Admin

To create a project, you will need an account with the necessary permissions. Make sure you have followed the steps in [Set up the Platform Admin account](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/platform-admin) to assign the necessary roles to the administrator account, and [connect](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect) to the instance using that account.

## Create a project

To create a project in your GDC Sandbox instance, perform the following steps. These steps include some specific values that you must use when creating a project in your GDC Sandbox instance.

  1. In the navigation menu, click **Projects**.
  2. Click **Add project**.
  3. In the **Project name** field, enter a project name. Take note of the project name you specify: it will be used in commands. For example, this name is used as the `namespace` parameter for `kubectl` commands.
  4. Optional: Configure your project's networking capabilities. Clear the **Enable data exfiltration protection** checkbox to enable all egress traffic to other projects inside your organization.
  5. Click **Create**.
  6. To verify the new project is available, a message is displayed in the console: `Project PROJECT_NAME successfully created`.



For more details about project creation, refer to the Google Distributed Cloud air-gapped documentation, [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/create-a-project).

## Add the Platform Admin to the project

  1. Wait 30 seconds and refresh the page to see your project in the Projects page.
  2. Click the project name in the project list.
  3. In the Project Access section, click **Go to Identity Access Management**.
  4. Click **Add member**.
  5. In the **Identity provider** list, select **fake-oidc-provider**.
  6. In the **Member type** list, click **User**.
  7. In the **Username or group alias** field, enter `platform-admin@example.com`.
  8. In the **Role** list, select **Project IAM Admin**.
  9. Click **Add**. The Platform Admin is added to the project and appears in the list of users, as `fop-platform-admin@example.com` .
  10. To add another project role, find the `fop-platform-admin@example.com` user in the list and click more_vert > **Edit Roles**. For example, if you want to add permissions for generative AI development, you might add the following roles: 
     * Dashboard Editor
     * Harbor Instance Admin
     * KMS Admin
     * MonitoringRule Editor
     * Project Grafana Viewer
     * Global PNP
  11. Click **Save**.



If you see a permissions error message during your GDC Sandbox experience in the Console, API, or CLI, copy the error message to determine the required role. Review both **Identity & Access** and **Project Access** to locate and apply desired role permissions for your use case.

## Add more users

Optional: Create more users that have more granular access using the GDC console.

  1. Click **Add member**.
  2. In the **Identity provider** list, select **fake-oidc-provider**.
  3. In the **Member type** list, click **User**.
  4. In the **Username or group alias** field, enter your username.
  5. In the **Role** list, select the role that you want to assign to the user, such as **Project Creator**.
  6. Click **Add**.
  7. Click logout **Logout** in the menu bar to return to the Fake OIDC Provider page. ![](https://docs.cloud.google.com/static/distributed-cloud/sandbox/latest/images/logout.png)
  8. Select **Custom User**.
  9. Enter a custom username.
  10. Click **Submit**.

**Note:** The custom username is automatically created with a 'fop-' prefix, but it should not be included when logging in.



### Attach clusters (optional)

Optionally, you can attach a Kubernetes cluster to your project. Your instance comes with two clusters for container-based workloads, `user-vm-1` and `user-vm-2`, as described in [Working with clusters](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters).

To attach a cluster to your project, see [Attach projects to a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/pa-ao-operations/cluster#attach-project-to-cluster) in the Distributed Cloud documentation.

## What's next

You completed your first sign in, configured user roles, and created a project. You can review [Manage identity and access](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/iam) to learn more about role definitions, or proceed to the following sections to begin working with resources such as containers and virtual machines. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
