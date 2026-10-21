---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/manage-packages/
title: Manage packages \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:23.377315+00:00
---

# Manage packages  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Manage packages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage packages with Config Sync from the Google Cloud console.

**Key Term:** A **package** is a set of Kubernetes resource manifests that are managed together in a source of truth and synced to a cluster by Config Sync. Each package is defined by a `RootSync` or `RepoSync` object on the cluster. For more information about these objects, see [Config Sync architecture](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#rootsync-reposync). You can have multiple packages per cluster, for example, from different sources.

## Before you begin

  * [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).



## Deploy a package

After you have registered your clusters to a fleet and installed Config Sync, you can configure Config Sync to deploy a package to a cluster from a source of truth. You can deploy the same package to multiple clusters or deploy different packages to different clusters. You can edit a package after deploying it, except for some settings like package name and sync type. For more information, see [Manage packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/manage-packages).

**Note:** If you want Config Sync to render and apply a Helm chart, you must [configure Config Sync with the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configuring-config-sync) instead.

To deploy a package, complete the following steps:

  1. In the Google Cloud console, go to the **Config Sync dashboard**.

[Go to Config Sync dashboard](https://console.cloud.google.com/kubernetes/config_management)

  2. Click **Deploy Package**.

  3. In the **Select clusters for package deployment** table, select the cluster that you want to deploy a package to and then click **Continue**.

  4. Select either **Package hosted on Git** or **Package hosted on OCI** as your source type and then click **Continue**.

  5. In the **Package details** section, enter a **Package name** , which identifies the RootSync or RepoSync object.

  6. In the **Sync type** field, choose either **Cluster scoped sync** or **Namespace scoped sync** as the sync type.

Cluster scoped sync creates a RootSync object and Namespace scoped sync creates a RepoSync object. For more information about these objects, see [Config Sync architecture](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#rootsync-reposync).

  7. In the **Source** section, complete the following:

     * For sources hosted in a Git repository, enter the following fields:

       1. Enter the URL of the Git repository that you're using as a source of truth as the **Repository URL**.
       2. Optional: Update the **Revision** field to check out if you're not using the default `HEAD`.
       3. Optional: Update the **Path** field if you don't want to sync from the root repository.
       4. Optional: Update the **Branch** field if you're not using the default `main` branch.
     * For sources hosted in an OCI image, enter the following fields:

       1. Enter the URL of the OCI image that you're using as a source of truth as the **Image**.
       2. Enter the path of the directory to sync from, relative to the root directory, as the **Directory**.
  8. (Optional): Expand the **Advanced settings** section to complete the following:

     1. Select an **Authentication type**. Config Sync needs read-only access to your source of truth to read the configuration files in the source and apply them to your clusters. Unless your source requires no authentication, such as a public repository, ensure that you grant Config Sync read-only access to your [Git repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret), [OCI image](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#oci-access), or [Helm chart](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access) (gcloud CLI only). Choose the same authentication type that you configured when you installed Config Sync:

**Note:** for OCI, you can only select **Workload Identity** for authentication.
        * **None** : Use no authentication.
        * **SSH** : Authenticate by using an SSH key pair.
        * **Cookiefile** : Authenticate by using a `cookiefile`.
        * **Token** : Authenticate by using an access token or password.
        * **Google Cloud Repository** : Use a Google service account to access a Cloud Source Repositories repository. Only select this option if Workload Identity Federation for GKE is _not_ enabled in your cluster.
        * **Workload Identity** : Use a Google service account to access a Cloud Source Repositories repository.
     2. Enter a number in seconds to set the **Sync wait time** , which determines how long Config Sync waits between attempts to pull from the source of truth.

     3. Enter a **Git proxy** URL for the HTTPS proxy to be used when communicating with the source of truth.

  9. Click **Deploy Package**.

You are redirected to the Config Sync **Packages** page. After a few minutes, you should see **Synced** in the **Sync status** column for the cluster that you configured.




## Edit a package

To edit a package that you've already deployed, complete the following steps:

  1. In the Google Cloud console, go to the Config Sync **Packages** tab.

[Go to Packages](https://console.cloud.google.com/kubernetes/config_management/packages)

  2. (Optional): Expand the **Quick filters** menu and then select a filter to help find the package that you want to edit.

  3. Expand the package name that you want to edit and then, in the row that contains the cluster name, click the context menu _more_vert_ and then click _edit_ **Edit package**.

  4. Review and update the package settings that you want to change.

  5. Click **Save**.




## Uninstall a package

**Note:** The Google Cloud console uses the deletion propagation feature to delete package resources. If you don't manage your RootSync and RepoSync objects with the Google Cloud console, you can still use the deletion propagation feature to achieve a similar uninstall behavior, with `kubectl` or any other Kubernetes client. For more information, see [Bulk delete objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#bulk_delete_objects) ([Preview](https://cloud.google.com/products#product-launch-stages)).

To uninstall a package from the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the Config Sync **Packages** tab.

[Go to Packages](https://console.cloud.google.com/kubernetes/config_management/packages)

  2. (Optional): Expand the **Quick filters** menu and then select a filter to help find the package that you want to uninstall.

  3. Expand the package name that you want to uninstall and then, in the row that contains the cluster name, click the context menu _more_vert_ and then click _delete_ **Uninstall package**.

  4. In the confirmation dialog, select whether to uninstall only the RootSync or RepoSync object, or uninstall the RootSync or RepoSync **and** all of the resources managed by the RootSync or RepoSync.

  5. Type the confirmation message and then click **Uninstall**.




## What's next

  * [Monitor the status of Config Sync and packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard)
  * Use the [`nomos` command-line tool](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command)
  * [Troubleshoot Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
