---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/migration/
title: Migrate Config Controller resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:09.460097+00:00
---

# Migrate Config Controller resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Migrate Config Controller resources Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to migrate [Config Connector resources](https://docs.cloud.google.com/config-connector/docs/reference/overview) from one Config Controller cluster to another. You might need to migrate a resource if your primary Config Controller cluster fails and needs to be replaced, or you need to change an immutable cluster configuration.

This page uses the following terminology:

  * **Source cluster** : The cluster that contains the Config Connector resources that you need to migrate.
  * **Destination cluster** : The cluster that you are going to migrate resources to.



## Recommendations

  * Before you make changes in production, complete these steps in a test environment.
  * If you need to migrate multiple Config Controller clusters, migrate each one separately starting with the least critical cluster.
  * If the Config Sync cluster syncs from more than one source of truth, migrate all resources from each source at once.



## Migration steps for various scenarios

**Caution:** [Some Config Connector resources can't be migrated](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#resources_that_cannot_be_acquired) because they don't have support for acquiring existing Google Cloud resources.

### Migrate all resources

To migrate all resources, complete the following steps:

  1. Create the destination cluster.

  2. Stop pushing changes to the source of truth that the source cluster is configured to sync from. Config Sync should continue to sync from the source of truth. Only changes that the source cluster syncs from should be stopped.

  3. Ensure that any recent changes to the source of truth have synced in the cluster and all resources are up to date in the source cluster.

If there are errors for some resources, you might need to analyze the resources individually. If a resource has not yet been created due to an error, it's later created using the Config Connector running in the destination cluster. These errors can usually be ignored. However, for most errors, the root causes should be found and fixed before attempting migration.

  4. Set up Config Sync in the destination cluster to read from the same source of truth that the source cluster is configured from. If multiple syncs are set up to synchronize from more than one source of truth, then do this for each sync.

  5. Use the `nomos status` command to ensure that the destination cluster has synced all resources from the source of truth.

  6. Once the resources are synced, remove the [RootSync or RepoSync](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields) from the source cluster.

  7. Once each source of truth has been migrated, delete the source Config Controller cluster.

**Note:** Config Connector doesn't delete any resources when the Config Controller cluster is deleted. This means that if the Config Controller cluster is deleted, there is no need to set `cnrm.cloud.google.com/deletion-policy: abandon` on individual resources before deleting the cluster.



### Migrate some resources

To migrate some resources, complete the following steps:

  1. Complete steps 1-6 from the preceding Migrate all resources section.

  2. Annotate the resources that should be migrated to the destination cluster with the `cnrm.cloud.google.com/deletion-policy: abandon` annotation. This annotation prevents Config Connector from deleting the underlying resources when the Config Connector resource is deleted from the Config Controller cluster.

  3. Delete the resources that have been marked as abandoned from the source cluster. This deletion only works if these resources are removed from the source of truth as well before resuming Config Sync.

  4. Move these resources to a different source of truth or a different folder within the same source of truth.

  5. Set up the destination cluster to sync from the location that you moved the resources to. The destination cluster can now acquire these resources and start managing them.




### Migrate individual resources

When a Config Controller cluster cannot be deleted (for example, when only migrating a subset of resources to a different cluster) you can delete individual resources. To delete individual resources, disable Config Sync and then set the annotation `cnrm.cloud.google.com/deletion-policy: abandon` on the individual resources that you need to delete.

### Migrate resources that have a service generated `resourceID`

For resources where the `resourceID` field has not been explicitly provided, the `resourceID` doesn't need to be specified for resource acquisition by another Config Connector instance. However, there are [resources that have a service-generated resource ID](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#service-generated-resource-id) which need additional steps. Even though the `resourceID` is service generated, it needs to be provided to acquire these resources from another Config Connector instance. For these resources, the `resourceID`s should be added to the source of truth before trying to acquire resources from the destination cluster.

### Migrate resources using conflict prevention policy

By default, the [conflict prevention policy](https://docs.cloud.google.com/config-connector/docs/concepts/managing-conflicts#modifying_conflict_prevention) is turned off for resources. You can enable it on a resource by setting the following annotation:

`cnrm.cloud.google.com/management-conflict-prevention-policy: "resource"`

Once set, Config Connector has to acquire a lease on the underlying resource before making any changes to it. This means that the destination cluster is not able to acquire the lease immediately since the lease is held by Config Connector in the source cluster. The lease is granted for 40 minutes. However, after 20 minutes Config Connector proactively tries to renew the lease. Because of this behavior, if Config Connector in the source cluster is healthy and running, the destination cluster is not able to acquire the lease. The source cluster needs to release its lease before the destination cluster can acquire it. This can be accomplished either by deleting the source cluster, or by deleting the resource in the source cluster.

**Caution:** The Config Connector resource needs to be marked as abandoned before you delete it in the source cluster. Otherwise, the actual resource is deleted if it's deleted from the cluster. For instructions on how to safely accomplish this task, see migrate only some resources.

Once the source cluster has released the lease, the destination cluster is able to acquire the lease. The destination cluster can acquire the lease after at most 40 minutes and can start managing the resources. No changes should be made to the Config Connector resources until the lease has been acquired by the destination cluster.

## What's next

  * [Troubleshoot Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot).
  * [Manual failover to a second Config Controller instance](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/availability#second-config-controller-manual-failover).
  * [Managing resources with the `resourceID` field](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids).
  * [Stop and resume syncing configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/stopping-resuming-syncing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
