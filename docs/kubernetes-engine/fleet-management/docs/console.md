---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console/
title: Work with clusters from the Google Cloud console \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:03:04.665039+00:00
---

# Work with clusters from the Google Cloud console  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Work with clusters from the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

All clusters that have been [added to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) appear in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

The Google Cloud console offers a central user interface for managing all your Kubernetes clusters and their resources, no matter where they are running. All your resources are shown in a single dashboard, which gives you visibility into your workloads across multiple Kubernetes clusters. You can find out more about working with Google Cloud clusters in the Google Cloud console in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards).

For GKE clusters on Google Cloud, you see cluster details such as nodes and workloads, provided that you have the relevant permissions. The permissions are listed in the subsequent section, [Required roles](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#required_roles).

If your fleet includes clusters outside Google Cloud, you need to log in to these clusters and view their details in the Google Cloud console. For details, see the following section Log in to clusters.

## Required roles

If you are not a project owner, you must have the following Identity and Access Management roles at minimum to view clusters in the Google Cloud console:

  * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the Google Cloud console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view clusters outside Google Cloud in the Google Cloud console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.

  * `roles/gkeonprem.viewer`. For Google Distributed Cloud users, this role is required in addition to `roles/gkehub.viewer` to view on-premises clusters on bare metal or VMware in the Google Cloud console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.




## View registered clusters

After you register a cluster to your project fleet, it appears in the Google Cloud console in the [GKE **Clusters** list](https://console.cloud.google.com/kubernetes/list). However, to see more details such as nodes and workloads for any cluster outside Google Cloud, you need to log in and authenticate to the cluster. Clusters that require login show an orange warning triangle and prompt you to log in. The following example shows the GKE **Clusters** page with two clusters outside Google Cloud that require login.

![Screenshot of Google Kubernetes Engine clusters list](https://docs.cloud.google.com/static/anthos/images/cluster-login-prompt.png)

After you log in to the cluster, you can select the cluster and view cluster details. These are the same details that you can see for a GKE on Google Cloud cluster.

## Log in to clusters

If your fleet includes clusters outside Google Cloud, your platform administrator needs to set up authentication so that you can log in to these clusters and view their details in the Google Cloud console.

You need to know which authentication method your platform administrator has set up so that you can log in to the Google Cloud console. Ask your platform administrator which of the following authentication methods have been configured:

  * [Google identity](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup)
  * Third-party identity: 
    * [GKE Identity Service with OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster)
    * [GKE Identity Service with Microsoft Entra ID (Azure AD)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster#azure-ad-advanced)
    * [Third-party identity with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party)
  * [Bearer token](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth)



Then, follow the instructions in the following sections to log in to your clusters using the relevant authentication method.

### Log in using your Google Cloud identity

If your cluster is configured to use your [Google Cloud identity](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup), follow these steps to log in:

  1. Open the **GKE Clusters** page in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

  2. Select the checkbox for the one or more clusters that you want to log in to. If you are selecting multiple clusters:

     * To select all of the clusters displayed on the page, select the checkbox in the table header row.

     * To select all of the clusters in the project that are not logged in, select the **Log in** option that accompanies the warning that you're not logged in to a certain number of clusters.

  3. In the menu bar, click **Log in**.

  4. Select **Use your Google identity to log in**.

  5. Click **Log in**.




### Log in using OpenID Connect (OIDC)

Note that while GKE Identity Service also supports LDAP identity providers, logging in using the Google Cloud console is supported for OIDC providers only.

If Microsoft Entra ID (Azure AD) is configured as an OIDC identity provider for your cluster using the `azuread` anchor in the ClientConfig, follow the instruction in [Log in using Microsoft Entra ID (Azure AD)](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#log-in-azure-ad) instead.

If your cluster is configured to use an [OIDC identity provider](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster) with GKE Identity Service, follow these steps to log in:

  1. Open the **GKE Clusters** page in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

  2. Select the checkbox for the one or more clusters that you want to log in to. If you are selecting multiple clusters:

     * To select all of the clusters displayed on the page, select the checkbox in the table header row.

     * To select all of the clusters in the project that are not logged in, select the **Log in** option that accompanies the warning that you're not logged in to a certain number of clusters.

  3. In the menu bar, click **Log in**.

  4. Select **Authenticate with identity provider configured for the cluster**. You are redirected to your identity provider, where you might need to log in or consent to the Google Cloud console accessing your account.

  5. Click **Log in**.




### Log in using Microsoft Entra ID (Azure AD)

If your cluster is configured to use [Microsoft Entra ID (Azure ID)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster) with GKE Identity Service [using the `azuread` anchor](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster#azure-ad-advanced) (also referred to as Azure AD advanced configuration), follow these steps to log in:

  1. Open the **GKE Clusters** page in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

  2. Select the checkbox for the one or more clusters that you want to log in to. If you are selecting multiple clusters:

     * To select all of the clusters displayed on the page, select the checkbox in the table header row.

     * To select all of the clusters in the project that are not logged in, select the **Log in** option that accompanies the warning that you're not logged in to a certain number of clusters.

  3. In the menu bar, click **Log in**.

  4. Select **Authenticate with Microsoft Entra ID (formerly Azure AD)**. You are redirected to your identity provider, where you might need to log in or consent to the Google Cloud console accessing your account.

  5. Click **Log in**.




### Log in using a third-party identity and the Connect gateway

If your cluster is configured to use [third-party identity with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party), you can log in to the cluster with your third-party identity in the [Google Cloud workforce identity federation console](https://console.cloud.google), also known as the console (federated). Log in from the regular Google Cloud console is not supported.

Follow these steps to log in:

  1. Go to the [Google Cloud workforce identity federation console](https://console.cloud.google), enter your provider ID, and sign in using your identity provider. Your platform administrator should provide you with all the details you need to sign in. To learn more about how this is set up, see [Set up user access to the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso).
  2. Open the **GKE Clusters** page in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

  3. Select the checkbox for the one or more clusters that you want to log in to. If you are selecting multiple clusters:

     * To select all of the clusters displayed on the page, select the checkbox in the table header row.

     * To select all of the clusters in the project that are not logged in, select the **Log in** option that accompanies the warning that you're not logged in to a certain number of clusters.

  4. In the menu bar, click **Log in**.

  5. Select **Use your third-party identity provider to log in**.

  6. Click **Log in**.




### Log in using a bearer token

If your cluster is configured to use a [Kubernetes service account's bearer token](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth), follow these steps:

  1. Open the **GKE Clusters** page in the Google Cloud console.

[Go to GKE Clusters](https://console.cloud.google.com/kubernetes/list)

  2. Select the checkbox for the one or more clusters that you want to log in to. If you are selecting multiple clusters:

     * To select all of the clusters displayed on the page, select the checkbox in the table header row.

     * To select all of the clusters in the project that are not logged in, select the **Log in** option that accompanies the warning that you're not logged in to a certain number of clusters.

  3. In the menu bar, click **Log in**.

  4. Select **Token** , and then fill in the **Token** field with the KSA's bearer token.

  5. Click **Log in**.




## Auditing

Accesses via the Google Cloud console are [audit logged](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) on the cluster's API server.

## What's next

Learn more about:

  * Working with clusters in the Google Cloud console in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards)
  * Viewing cluster status and resource utilization in the Google Cloud console with the [GKE Enterprise overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard)
  * Setting up authentication to fleet clusters in [Secure your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure#manage_identity)
  * Connecting to fleet clusters from the command line:

    * [Setting up the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
    * [Accessing clusters with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing).
  * [Managing fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
