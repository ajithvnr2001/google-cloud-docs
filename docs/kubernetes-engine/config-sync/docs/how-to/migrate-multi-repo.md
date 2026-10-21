---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo/
title: Migrate your ConfigManagement object \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:23.685471+00:00
---

# Migrate your ConfigManagement object  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Migrate your ConfigManagement object Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The `spec.git` fields of the `ConfigManagement` object are shutdown. You can't create new configurations that use the `spec.git` fields to manage a Git repository. If you are still using the `spec.git` fields, this page can be used to migrate your Git configuration to a `RootSync`. If you used `spec.enableLegacyFields` to bootstrap a RootSync, you must remove both the `spec.git` and `spec.enableLegacyFields` fields.

This page shows you how to migrate your Git configuration from a `ConfigManagement` object to a [`RootSync`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields) object. The migration enables the `RootSync` and `RepoSync` APIs, which lets you use additional features:

  * [Sync from more than one source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories)
  * [Use the Config Sync dashboard](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard)
  * [Monitor Config Sync using Cloud Monitoring, Prometheus, or custom monitoring system](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync)
  * [Render Kustomize configurations and Helm charts](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-helm)
  * [Sync OCI artifacts from Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry)
  * [Sync Helm charts from Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry)
  * Override system values such as [changing resource limits](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#override-resources) and [updating the number of Git commits to fetch](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#override-resources)



You can enable these APIs even if you only want to use a root repository and don't want to use any namespace repositories.

## Migrate your ConfigManagement settings

If you are using `RootSync` with `spec.enableLegacyFields`, follow the instructions to Stop using legacy fields.

If your ConfigManagement object is using `spec.git` but `spec.enableMultiRepo` is set to false, follow the instructions to Migrate to RootSync.

### Stop using legacy fields

The `spec.enableLegacyFields` field is not supported in Config Sync. Having this field present causes errors. If you are on an earlier version of Config Sync that specifies this field, complete the following steps to remove the legacy fields:

**Note:** After removing the legacy fields from the ConfigManagement object, you can modify your RootSync objects directly instead.

  1. Open your [ConfigManagement object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields).

  2. In the ConfigManagement object, remove the `spec.enableLegacyFields` and `spec.git` fields. Your ConfigManagement object should resemble the following:
         
         # config-management.yaml
         apiVersion: configmanagement.gke.io/v1
         kind: ConfigManagement
         metadata:
           name: config-management
         spec:
           enableMultiRepo: true
         

  3. Apply the changes:
         
         kubectl apply -f config-management.yaml
         




Legacy fields are now disabled without affecting the `RootSync` object generated from the `spec.git` fields of your ConfigManagement object. The migration has completed and you can now use the git fields in the `RootSync` object directly.

### Migrate to RootSync

If your ConfigManagement object is using `spec.git` but `spec.enableMultiRepo` is set to false, follow this guide to enable the `RootSync` and `RepoSync` APIs.

#### Use `nomos migrate`

Starting from version 1.10.0, `nomos` provides the `nomos migrate` command to enable the `RootSync` and `RepoSync` APIs. You need to [update `nomos`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#installing) to 1.10.0 and later.

For more details about how to run the command, follow [Migrate from a ConfigManagement object to a RootSync object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#migrate). Ensure your ConfigManagement object isn't checked into your source of truth and managed by Config Sync. If it is, you should modify your ConfigManagement object in your source of truth following the steps in [Manual migration](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo#manual-migration).

#### Manual migration

If your `nomos` version is earlier than 1.10.0, you can manually migrate your settings. You need to set `spec.enableMultiRepo` to `true` in your ConfigManagement object and create a RootSync object that syncs your root repository to the cluster.

To configure the root repository by migrating the configuration, complete the following tasks:

  1. Open your [ConfigManagement object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields).
  2. Make a copy of the values in the `spec.git` fields. You use these values when you create the RootSync object.
  3. Remove all of the `spec.git` fields (including `git:`) from the ConfigManagement object.
  4. In the ConfigManagement object, set the `spec.enableMultiRepo` field to `true`:
         
         # config-management.yaml
         apiVersion: configmanagement.gke.io/v1
         kind: ConfigManagement
         metadata:
           name: config-management
         spec:
           **enableMultiRepo : true**
         

  5. Apply the changes:
         
         kubectl apply -f config-management.yaml
         

  6. Wait for the RootSync CRD to be created.
         
         kubectl wait --for=condition=established crd rootsyncs.configsync.gke.io
         

  7. Using the values you copied from the ConfigManagement object, create the RootSync object. For example:
         
         # root-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: root-sync
           namespace: config-management-system
         spec:
           sourceFormat: unstructured
           git:
             repo: ROOT_REPOSITORY
             revision: ROOT_REVISION
             branch: ROOT_BRANCH
             dir: "ROOT_DIRECTORY"
             auth: ROOT_AUTH_TYPE
             gcpServiceAccountEmail: ROOT_EMAIL
             # secretRef should be omitted if the auth type is none, gcenode, or gcpserviceaccount.
             secretRef:
               name: git-creds
         

Replace the following:

     * `ROOT_REPOSITORY`: add the URL of the Git repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. If you don't enter a protocol, the URL is treated as an HTTPS URL. This field is required.
     * `ROOT_REVISION`: add the Git revision (tag or hash) to check out. This field is optional and the default value is `HEAD`.
     * `ROOT_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`.
     * `ROOT_DIRECTORY`: add the path in the Git repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a repository in Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a repository in Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

  8. Apply the changes:
         
         kubectl apply -f root-sync.yaml
         




## ConfigManagement and RootSync comparison table

The following table provides an overview of how the fields in your ConfigMangent object map to the fields in a RootSync object.

**ConfigManagement field** | **RootSync field**  
---|---  
`spec.git.gcpServiceAccountEmail` | `spec.git.gcpServiceAccountEmail`  
`spec.git.syncRepo` | `spec.git.repo`  
`spec.git.syncBranch` | `spec.git.branch`  
`spec.git.policyDir` | `spec.git.dir`  
`spec.git.syncWait` | `spec.git.period`  
`spec.git.syncRev` | `spec.git.revision`  
`spec.git.secretType` | `spec.git.auth`  
`git-creds` (this is a fixed value in ConfigManagement objects) | `spec.git.secretRef.name`  
`spec.sourceFormat` | `spec.sourceFormat`  
`spec.git.proxy.httpProxy` or `spec.git.proxy.httpsProxy` | `spec.git.proxy`  
  
## What's next

  * [Configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
