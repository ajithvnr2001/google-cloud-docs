---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/stopping-resuming-syncing/
title: Stop and resume syncing configs \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:23.502961+00:00
---

# Stop and resume syncing configs  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/stopping-resuming-syncing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Stop and resume syncing configs Stay organized with collections  Save and categorize content based on your preferences. 

In some situations, you might need to quickly stop Config Sync from syncing configs from your source of truth. One such scenario is if someone commits a syntactically valid but incorrect config to the source, and you want to limit its effects on your running clusters while the config is removed or fixed.

This page is only for manual installations of Config Sync using `kubectl`. For all other installation methods, use the gcloud CLI [`spec.configSync.stopSyncing` field](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields#config_sync) by setting `true` in your Config Sync configuration file. Then, to resume syncing, set the field to `false`.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Warning:** These steps won't work on Config Controller clusters. If you're experiencing an issue with Config Sync on your Config Controller cluster and need to stop Config Sync, reach out to [Google Cloud Support](https://docs.cloud.google.com/support/docs) to report and resolve the issue.

## Prerequisites

To use the commands in this document, you need the following Kubernetes RBAC permissions in the `config-management-system` namespaces on all clusters where you want to stop syncing:
    
    
    - apiGroups: ["extensions"]
      resources: ["deployments", "deployments/scale"]
      verbs: ["get", "update"]
    - apiGroups: [""]
      resources: ["pods"]
      verbs: ["list", "watch"]
    

## Stop and resume syncing from a source of truth

This section is for a single source of truth and it shows you how to quickly stop syncing, and how to resume syncing when the problem is fixed. To learn how to stop syncing for more than one source of truth, see stopping and resuming syncing from more than one source of truth.

### Stop syncing

To stop syncing for a single cluster, run the following command:
    
    
    kubectl scale -n config-management-system deployment --replicas=0 --all \
    && kubectl wait -n config-management-system --for=delete pods --all
    

The commands reduce the `replicas` count of all Deployments running in the `config-management-system` namespace to 0. The exact set of Deployments affected varies by product version.

All deployments are still in the cluster, but no replicas of the the processes responsible for syncing are available, so configs are not synced from the source of truth.

To verify that all processes have been stopped, use the following command and verify that all Deployments have zero replicas: 
    
    
    kubectl get -n config-management-system deployment
    

If you need to stop syncing on multiple clusters, run the preceding commands for each cluster.

### Resume syncing

To resume syncing for a single cluster, run the following command:
    
    
    kubectl -n config-management-system scale deployment reconciler-manager --replicas=1
    

This command scales the Reconciler Manager Deployment to 1 replica. The Reconciler Manager then notices that the Pods in the `config-management-system` namespace Deployments are scaled incorrectly and scales them to their appropriate replica count.

If you need to resume syncing on multiple clusters, run the preceding command for each cluster.

## Stop and resume syncing from more than one source of truth

The section is for more than one source of truth and shows you how to temporarily stop and resume syncing from more than one source of truth. To learn how to stop syncing for a single source of truth, see stopping and resuming syncing from a source of truth.

Only a central administrator can stop syncing in the root source of truth.

The ability to stop syncing in more than one source of truth depends on which [configuration method](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories) was used when you set up syncing from more than one source of truth:

  * If the **Control sources in a root source of truth** method was used, a central administrator is the only one who can stop and resume syncing.

  * If the **Control a source of truth with the Kubernetes API** method was used, application operators can stop and resume syncing from the namespace-scoped sources of truth that they work on.




### Stop syncing

The following sections show you how to stop syncing for the root source of truth and namespace-scoped sources of truth. To stop the Reconciler Manager from reverting the change, you need to stop the Reconciler Manager first by running the following commands:
    
    
    kubectl scale deployment -n config-management-system reconciler-manager --replicas=0 \
    && kubectl wait -n config-management-system --for=delete pods -l app=reconciler-manager
    

These commands reduce the `replicas` count in the Reconciler Manager Deployment to 0.

#### Stop syncing from the root source of truth

To stop a cluster syncing from the root source of truth, a central administrator can run the following command:
    
    
    kubectl -n config-management-system scale deployment root-reconciler --replicas=0
    

This command reduces the `replicas` count in the `root-reconciler` [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) to 0.

If you need to stop syncing on multiple clusters, run the preceding command for each cluster.

#### Stop syncing from namespace-scoped source of truth

Select the **Root source of truth method** or **Kubernetes API method** tab to view the relevant instructions.

### Root source of truth method

If the **Control namespace sources of truth in the root source of truth** method was used, central administrators can run the following commands to stop a cluster syncing from a namespace source of truth:
    
    
    kubectl -n config-management-system scale deployment ns-reconciler-NAMESPACE --replicas=0
    

The command reduces the replica count in the `ns-reconciler-NAMESPACE` Deployment to 0.

If you need to stop syncing on multiple clusters, run the preceding command for each cluster.

### Kubernetes API method

If the **Control namespace-scoped sources with the Kubernetes API** method was used, application operators can stop a cluster syncing by running the following commands:

  1. Retrieve the `RepoSync` configuration and save it to use it later when you want to resume syncing:
         
         kubectl -n NAMESPACE get reposyncs repo-sync -oyaml > repo-sync.yaml
         

Replace `NAMESPACE` with the namespace of your RepoSync object.

  2. Delete the `RepoSync` configuration:
         
         kubectl -n NAMESPACE delete reposyncs repo-sync
         

This command triggers the Reconciler Manager to remove the namespace reconciler (`ns-reconciler-NAMESPACE`) from NAMESPACE and stops syncing.

**Note:** Deleting the `RepoSync` configurations does not affect objects from the namespace-scoped sources that have already synced.

If you need to stop syncing on multiple clusters, run the preceding commands for each cluster.




#### Stop the admission webhook from blocking drifts (optional)

The Config Sync admission webhook is disabled by default, and you can [enable](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#enable) and [disable](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#disable) the drift prevention functionality provided by the admission webhook using Google Cloud CLI or `kubectl`.

#### Stop syncing from all sources of truth

To stop syncing from all sources of truth, including the root source of truth and namespace-scoped sources, run the following commands:
    
    
    kubectl scale deployment -n config-management-system -l app=reconciler --replicas=0 \
    && kubectl wait -n config-management-system --for=delete pods -l app=reconciler
    

The commands reduce the `replicas` count of all Reconciler Pods running in the `config-management-system` namespace to 0, and wait until all Reconciler Pods are deleted.

All Reconciler Deployments are still in the cluster, but no replicas of the Reconcilers or any of the processes responsible for syncing are available, so configs are not synced from the source of truth.

### Resume syncing

This section shows you how to resume syncing for the root source of truth and for namespace-scoped sources.

#### Resume syncing from the root source of truth

To resume syncing from a root source of truth, a central administrator can run the following command:
    
    
    kubectl -n config-management-system scale deployment root-reconciler --replicas=1
    

This command scales the `root-reconciler` Deployment to 1 replica.

#### Resume syncing from a namespace-scoped source

Select the **Root source of truth method** or **Kubernetes API method** tab to view the relevant instructions.

### Root source of truth method

If you used the **Control namespace-scoped sources in a root source of truth** method, a central administrator can run the following command:
    
    
    kubectl -n config-management-system scale deployment ns-reconciler-NAMESPACE --replicas=1
    

This command scales the ns-reconciler-NAMESPACE Deployment to 1 replica.

### Kubernetes API method

If you used the **Control namespace-scoped sources with the Kubernetes API** method, application operators can resume syncing by reapplying `repo-sync.yaml` which contains the `RepoSync` configuration:
    
    
    kubectl apply -f repo-sync.yaml
    

This command triggers tne Reconciler Manager to create a namespace reconciler process and create a `ns-reconciler-NAMESPACE` Deployment.

#### Enable and disable the admission webhook

The Config Sync admission webhook is disabled by default, and you can [enable](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#enable) and [disable](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#disable) the drift prevention functionality provided by the admission webhook using Google Cloud CLI or `kubectl`.

#### Resume syncing from all sources of truth

To resume syncing, run the following command:
    
    
    kubectl -n config-management-system scale deployment reconciler-manager --replicas=1
    

This command scales the Reconciler Manager Deployment to 1 replica. The Reconciler Manager then scales the root reconciler and namespace reconcilers to their corresponding replica count.

**Note:** If you used the **Control namespace-scoped sources with the Kubernetes API** method, application operators can resume syncing by reapplying `repo-sync.yaml` which contains the `RepoSync` configuration: `kubectl apply -f repo-sync.yaml`. This command triggers the Reconciler Manager to create a namespace reconciler process and create a `ns-reconciler-NAMESPACE` Deployment.

## What's next

  * [Use the `nomos` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
