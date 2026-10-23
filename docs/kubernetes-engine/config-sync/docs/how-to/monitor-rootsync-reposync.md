---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync/
title: Monitor RootSync and RepoSync objects \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:10.125182+00:00
---

# Monitor RootSync and RepoSync objects  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Monitor RootSync and RepoSync objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you different ways that you can monitor your [`RootSync` and `RepoSync` objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields). For example, you might want to verify if your latest commit in a source of truth is applied to a cluster and reconciled successfully.

## View synced commits

You can check which commit is synced to the cluster by checking the `.status.sync` field in the `RootSync` or `RepoSync` object.

  * To view synced commits for a `RootSync`object, run the following command:
        
        kubectl get rootsync ROOT_SYNC_NAME -n config-management-system
        

Replace `ROOT_SYNC_NAME` with the name of the `RootSync`object.

  * To view synced commits for a `RepoSync` object, run the following command:
        
        kubectl get reposync REPO_SYNC_NAME -n REPO_SYNC_NAMESPACE
        

Replace the following:

    * `REPO_SYNC_NAME`: the name of the `RepoSync` object.
    * `REPO_SYNC_NAMESPACE`: the namespace that you created your namespace repository in.



The output for these commands show you the value of the source commit and the synced commit. For example, if you ran the command for the RepoSync, you would see output similar to the following:
    
    
    NAME        RENDERINGCOMMIT                            SOURCECOMMIT                               SYNCCOMMIT
    root-sync   66882815f0ef5517df27e864fb1315e97756ab72   66882815f0ef5517df27e864fb1315e97756ab72   66882815f0ef5517df27e864fb1315e97756ab72
    

The value in the `RENDERINGCOMMIT` column is the commit that is processed by the `hydration-controller`. If no rendering is needed, the value is the same as the `SOURCECOMMIT` column. The value in the `SOURCECOMMIT` column is the commit from the source of truth that should be synced to the cluster. The value in the `SYNCCOMMIT` column is the commit that is deployed to the cluster. If the two values in the `SOURCECOMMIT` and `SYNCCOMMIT` columns are the same, the expected commit has been deployed to the cluster.

## Confirm resources in the commit are reconciled

Because ResourceGroups capture the reconciliation status of the managed resources declared in the source of truth, you can examine them to confirm if resources in the commit are reconciled.

The ResourceGroup object has the same namespace and name as the `RootSync`or `RepoSync` object. For example, for the `RootSync` object with the name `root-sync` in the namespace `config-management-system`, the corresponding ResourceGroup object is also `root-sync` in the namespace `config-management-system`.

  * To get the ResourceGroup object for a `RootSync`object:
        
        kubectl get resourcegroup ROOT_SYNC_NAME -n config-management-system -o yaml
        

  * To get the ResourceGroup object for a `RepoSync` object:
        
        kubectl get resourcegroup REPO_SYNC_NAME -n REPO_SYNC_NAMESPACE -o yaml
        

Replace the following:

    * `ROOT_SYNC_NAME`: the name of the ResourceGroup object that you want to look up.
    * `REPO_SYNC_NAME`: the name of the ResourceGroup object that you want to look up.
    * `REPO_SYNC_NAMESPACE`: the name of the ResourceGroup object that you want to look up.



To confirm that the resources in the commit are reconciled, look for the following in the output:

  * The `.status.observedGeneration` equals the value of the field `.metadata.generation` in the ResourceGroup object.
  * The `Stalled` condition has a `status` of `"False"`.
  * Each item under `.status.resourceStatuses` has an an `actuation` of `Succeeded`, a `reconcile` of `Succeeded`, and a `status` of `Current`.

**Note:** The `Reconciling` condition on the ResourceGroup object is deprecated and can be ignored.

## View errors

`RootSync`and `RepoSync` objects use the `status` field to track errors encountered when syncing the configs from the source of truth to a cluster.

  * To view the status of a `RootSync`object, run the following command:
        
        kubectl get rootsync ROOT_SYNC_NAME -n config-management-system -o yaml
        

Replace the `ROOT_SYNC_NAME` with the name of the `RootSync`object.

  * To view the status of a `RepoSync` object, run the following command:
        
        kubectl get reposync REPO_SYNC_NAME -n NAMESPACE -o yaml
        

Replace the following:

    * `REPO_SYNC_NAME`: the name of the `RepoSync` object.
    * `NAMESPACE`: the namespace that you created your namespace repository in.



To learn more about the subfields under the `status` field, see [Status of the objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#status_of_the_objects).

## View object details

To view details of the `RootSync`and `RepoSync` objects and to discover further information about potential errors, use the `kubectl describe` command.

The output of this command includes events, which can be particularly helpful for debugging issues such as containers facing memory constraints (OOMKilled), scheduling failures, or image pull errors.

For a more readable format, convert the output to YAML by appending `-o yaml` to the following commands. This format is especially helpful when you need to examine specific parameters, annotations, or resource specifications.

  * To view details for a `RootSync` object, run the following command:
        
        kubectl describe rootsync ROOT_SYNC_NAME -n config-management-system
        

Replace the `ROOT_SYNC_NAME` with the name of the `RootSync` object.

  * To view details for a `RepoSync` object, run the following command:
        
        kubectl describe reposync REPO_SYNC_NAME -n NAMESPACE
        

Replace the following:

    * `REPO_SYNC_NAME`: the name of the `RepoSync` object.
    * `NAMESPACE`: the namespace that you created your namespace repository in.



## View if a resource is ready

To learn if the resources synced to the cluster are ready, view the reconciliation status. For example, viewing the reconciliation status can show you if a synced Deployment is ready to serve traffic.

For a source of truth synced to the cluster, the reconciliation statuses of all resources are aggregated in a resource called ResourceGroup. For each `RootSync` or `RepoSync` object, a ResourceGroup is generated to capture the set of resources applied to the cluster and aggregate their statuses.

  * To view the reconciliation status for the `RootSync` object, run the following command:
        
        kubectl get resourcegroup.kpt.dev ROOT_SYNC_NAME -n config-management-system -o yaml
        

Replace the `ROOT_SYNC_NAME` with the name of the `RootSync` object.

  * To view the reconciliation status for the `RepoSync` object, run the following command:
        
        kubectl get resourcegroup.kpt.dev REPO_SYNC_NAME -n NAMESPACE -o yaml
        

Replace the following:

    * `REPO_SYNC_NAME`: the name of the `RepoSync` object.
    * `NAMESPACE`: the namespace that you created your namespace repository in.



In the output, you see all of the ResourceGroup resource statuses. For example, the following output shows that a Deployment named `nginx-deployment` is ready:
    
    
    resourceStatuses:
    - group: apps
      kind: Deployment
      name: nginx-deployment
      namespace: default
      status: Current
    

## View logs

For each `RootSync` and `RepoSync` object you create, Config Sync creates a reconciler Deployment to perform syncing. This section explains how to view the logs for these reconcilers. Viewing the logs can help when debugging an issue by providing additional information about progress, warnings, and errors beyond what is available in the `RootSync` and `RepoSync` object status.

  * To view the logs for the `RootSync` or `RepoSync` reconciler, run the following command:
        
        kubectl logs -n config-management-system deployment/RECONCILER_NAME CONTAINER_NAME
        

Replace the following:

    * `RECONCILER_NAME`: the reconciler name of the `RootSync` or `RepoSync` object.

      * For `RootSync`, the reconciler name is `root-reconciler-ROOT_SYNC_NAME` or `root-reconciler` if the name of `RootSync` is `root-sync`.

      * For `RepoSync`, the reconciler name is `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH` or `ns-reconciler-NAMESPACE` if the name of `RepoSync` is `repo-sync`, where `NAMESPACE` is the namespace you created your `RepoSync` object in.

    * `CONTAINER_NAME`: the container name must be one of the following values: `reconciler`, `git-sync`, `hydration-controller`, `oci-sync`, or `helm-sync`. To learn more about these containers, see [Reconciler containers](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#reconciler-containers).




## Configure RootSync or RepoSync reconciler log level

To include more information in the container logs, configure the log verbosity. By default, most containers have a default value of `0` for log verbosity. The exceptions to this are the `git-sync` and `otel-agent` containers that have a default value of `5`.

When changing log verbosity, keep in mind that increasing log verbosity results in higher logging costs because there's a greater volume of data recorded.

To change log verbosity, use the `.spec.override.logLevels` field as shown in the following example:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-management-system
    spec:
      override:
        logLevels:
        - containerName: "reconciler"
          logLevel: 0
        - containerName: "git-sync"
           logLevel: 10
    

The value in the `containerName` field must be one of the following: `reconciler`, `git-sync`, `hydration-controller`, `oci-sync`, or `helm-sync`.

To confirm log verbosity is configured, run the following command:
    
    
    kubectl get deployment.apps/root-reconciler -n config-management-system -o yaml
    

The log verbosity can be found as one of the `args` within `spec.template.spec.containers[]` and looks like `-v=0`, where 0 is the current log verbosity. In this example, a log verbosity value of 0 would log only critical events.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
