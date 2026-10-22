---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard/
title: Use the Config Sync dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:13.321008+00:00
---

# Use the Config Sync dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Use the Config Sync dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the Config Sync dashboard.

This dashboard provides you with a comprehensive overview of the packages that Config Sync manages and the status of the resources in these packages.

**Key Term:** A **package** is a set of Kubernetes resource manifests that are managed together in a source of truth and synced to a cluster by Config Sync. Each package is defined by a `RootSync` or `RepoSync` object on the cluster. For more information about these objects, see [Config Sync architecture](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#rootsync-reposync). You can have multiple packages per cluster, for example, from different sources.

## Before you begin

### IAM permissions

To access the Config Sync dashboard, the following IAM roles are required in the project:

  * `roles/container.clusterViewer`
  * `roles/gkehub.viewer`



### Role-based access control

The user also needs the relevant Kubernetes permissions in each cluster. If you don't want to grant users extensive permissions, such as those of the cluster admin, you can create a custom RBAC role that includes the minimum permissions required to use the Config Sync dashboard.

The `config-sync-dashboard-reader` `ClusterRole` grants the user `get` and `list` permissions on the resources needed by the dashboard.

  1. To create the `config-sync-dashboard-reader` `ClusterRole` and apply it to the cluster, run the following command:
         
         cat <<EOF > config-sync-dashboard-reader.yaml
         kind: ClusterRole
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: config-sync-dashboard-reader
         rules:
         - apiGroups: ["apiextensions.k8s.io"]
           resources: ["customresourcedefinitions"]
           verbs: ["get", "list"]
         - apiGroups: ["configmanagement.gke.io"]
           resources: ["configmanagements"]
           verbs: ["get", "list"]
         - apiGroups: ["configsync.gke.io"]
           resources: ["rootsyncs", "reposyncs"]
           verbs: ["get", "list"]
         - apiGroups: ["kpt.dev"]
           resources: ["resourcegroups"]
           verbs: ["get", "list"]
         - apiGroups: ["apps"]
           resources: ["deployments"]
           verbs: ["get", "list"]
         - apiGroups: [""]
           resources: ["pods", "services"]
           verbs: ["get", "list"]
         - apiGroups: ["anthos.cloud.google.com"]
           resources: ["canonicalservices"]
           verbs: ["get", "list"]
         - apiGroups: ["networking.istio.io"]
           resources: ["virtualservices"]
           verbs: ["get", "list"]
         
         EOF
         kubectl apply -f config-sync-dashboard-reader.yaml
         

  2. Follow the instructions for configuring [role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) on Google Kubernetes Engine clusters to set up the `ClusterRoleBinding`.




## Access the dashboard

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Select the project that you want to view.



## View the dashboard

The **dashboard** tab provides you an overview of the status of your Config Sync installations:

  * **Reconciliation status** shows you how many packages are reconciled. A package is reconciled if the state that you want, as expressed by the resources in the package, has been realized.

Your packages can have the following reconciliation statuses:

    * **Current** : the actual state of the package matches the state that you want. The reconcile process is considered complete until there are changes to either the state you want or the actual state.
    * **In progress** : the actual state of the package hasn't yet reached the state that you want (as expressed by the resources in the package). Newly created packages usually start with this status.
    * **Failed** : the process of reconciling the actual state with the state that you want has encountered an error or it has made insufficient progress.
    * **Unknown** : Config Sync couldn't determine the reconciliation status of a package.
  * **Synchronization status** shows you how many packages are synced. A package is synced when the latest observed state of the package in the source (for example, a Git repository) is reflected in the cluster.

Your packages can have the following synchronization statuses:

    * **Synced** : the package is synced to a cluster.
    * **Pending** : the package is pending synchronization.
    * **Reconciling** : the Deployment that syncs a package is being reconciled.
    * **Stalled** : the Deployment that syncs a package is stalled.
    * **Error** : the package encountered an error during syncing.
    * **Unknown** : Config Sync couldn't determine the synchronization status of a package.
  * **Config Sync status** shows you the installation status of Config Sync on your clusters.

Your clusters can have the following status related to Config Sync:

    * **Enabled** : clusters that have Config Sync enabled.
    * **Not enabled** : clusters that don't have Config Sync enabled.
    * **Pending** : clusters that have Config Sync enabled, but are undergoing changes. This status usually occurs during first-time configuration or when updating to a new version.
    * **Error** : clusters that have Config Sync enabled, but there's an issue and Config Sync isn't working.
    * **Unknown** : Config Sync's status can't be determined.



Additional tables show you issues grouped by package and cluster, provide links to install Config Sync and view settings, and resources for getting started.

## View package status

The **Packages** tab enables you to view in-depth details about individual packages and clusters. Use this tab to better understand potential causes behind sync errors and unhealthy resources.

## Edit a package

You can also use the **Packages** tab to edit your package configurations.

To edit a package, complete the following steps:

  1. Beside the name of the package that you want to edit, select _edit_ in the **Edit package** column
  2. In the **Package details** section, from the **Source type** drop-down list, select your source type.
  3. In the **Source** section, complete the following:

     * For sources hosted in a Git repository, enter the following fields:

       1. Enter the URL of the Git repository that you're using as a source of truth as the **Repository URL**.
       2. Optional: Update the **Revision** field to check out if you're not using the default `HEAD`.
       3. Optional: Update the **Path** field if you don't want to sync from the root repository.
       4. Optional: Update the **Branch** field if you're not using the default `main` branch.
     * For sources hosted in an OCI image, enter the following fields:

       1. Enter the URL of the OCI image that you're using as a source of truth as the **Image**.
       2. Enter the path of the directory to sync from, relative to the root directory, as the **Directory**.
  4. (Optional): Expand the **Advanced settings** section to complete the following:

     1. Select an **Authentication type** :

**Note:** for OCI, you can only select **Workload Identity** for authentication.
        * **None** : Use no authentication.
        * **SSH** : Use an SSH key pair.
        * **Cookiefile** : Use a `cookiefile`.
        * **Token** : Use a token.
        * **Google Cloud Repository** : Use a Google service account to access a Cloud Source Repositories repository. Only select this option if Workload Identity Federation for GKE is _not_ enabled in your cluster.
        * **Workload Identity** : Use a Google service account to access a Cloud Source Repositories repository.
     2. Enter a number in seconds to set the **Sync wait time** , which determines how long Config Sync waits between syncing from the source of truth.

     3. Enter a **Git proxy** URL for the HTTPS proxy to be used when communicating with the source of truth.

  5. When you are finished editing your package, click **Save**.

You are redirected to the Config Sync **Packages** page. After a few minutes, you should see **Synced** in the **Sync status** column for the package that you configured.




## View settings

The **Settings** tab shows you a list of clusters, along with information about their Config Sync settings and fleet settings.

You can also use this tab to upgrade Config Sync on a cluster:

  * Beside the name of the cluster that you want to upgrade, select the context menu _more_vert_ and then select _edit_ **Edit Config**.



For guidance on Config Sync settings, see [Configure Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configuring-config-sync).

## What's next

  * Learn about [using the nomos command-line tool](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) to monitor Config Sync.
  * Learn how to [Monitor Config Sync with metrics](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
