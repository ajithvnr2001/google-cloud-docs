---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/config-sync-permissions/
title: Default Config Sync permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:56.387538+00:00
---

# Default Config Sync permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/config-sync-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference)



Send feedback 

#  Default Config Sync permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the default permissions that Config Sync and its components need to have correct access at the cluster level.

## Default permissions

The following table lists the permissions that Config Sync enables by default. You shouldn't disable these permissions while Config Sync is in use.

**Component** | **Namespace** | **Service account** | **Permissions** | **Description**  
---|---|---|---|---  
`reconciler-manager` | `config-management-system` | `reconciler-manager` | `[cluster-admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container)` | To provision the root reconcilers and create the ClusterRoleBinding for the root reconcilers, the `reconciler-manager` must have `cluster-admin` permission.  
`root reconcilers` | `config-management-system` | The name of root reconciler | `[cluster-admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container)` | To apply cluster-scoped and custom resources, the root reconcilers must have the `cluster-admin` permission.  
`namespace reconcilers` | `config-management-system` | The name of namespace reconciler | `configsync.gke.io:ns-reconciler` | To get and update the RepoSync and ResourceGroup objects and their statuses, the namespace reconcilers need the `configsync.gke.io:ns-reconciler` permission.  
`resource-group-controller-manager` | `config-management-system` | `resource-group-sa` | 

  * `resource-group-manager-role`
  * `resource-group-leader-election-role`

| To check the object status and enable the leader election, the `resource-group-controller-manager` needs the `resource-group-manager-role` and `resource-group-leader-election-role` roles.  
`admission-webhook` | `config-management-system` | `admission-webhook` | `[cluster-admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container)` | To deny requests to any object on the cluster, the admission webhook must have `cluster-admin` permissions.  
`importer` | `config-management-system` | `importer` | `[cluster-admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container)` | To set RBAC permissions, the `importer` must have cluster-admin permission.  
  
## Config Sync specific permissions

The following sections details the `configsync.gke.io:ns-reconciler` and `resource-group-manager-role resource-group-leader-election-role` permissions that were listed in the preceding table.

Config Sync automatically applies these permissions by including the following ClusterRoles in the Namespace Reconciler and Resource Group Controller manifests.

### RBAC for namespace reconcilers

The following ClusterRole shows the role-based access control permissions for namespace reconcilers:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: configsync.gke.io:ns-reconciler
      labels:
        configmanagement.gke.io/system: "true"
        configmanagement.gke.io/arch: "csmr"
    rules:
    - apiGroups: ["configsync.gke.io"]
      resources: ["reposyncs"]
      verbs: ["get"]
    - apiGroups: ["configsync.gke.io"]
      resources: ["reposyncs/status"]
      verbs: ["get","list","update"]
    - apiGroups: ["kpt.dev"]
      resources: ["resourcegroups"]
      verbs: ["*"]
    - apiGroups: ["kpt.dev"]
      resources: ["resourcegroups/status"]
      verbs: ["*"]
    - apiGroups:
      - policy
      resources:
      - podsecuritypolicies
      resourceNames:
      - acm-psp
      verbs:
      - use
    

### RBAC for Resource Group Controller

The following ClusterRole shows the role-based access control permissions for the Resource Group Controller:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      creationTimestamp: null
      labels:
        configmanagement.gke.io/arch: "csmr"
        configmanagement.gke.io/system: "true"
      name: resource-group-manager-role
    rules:
    # This permission is needed to get the status for managed resources
    - apiGroups:
      - '*'
      resources:
      - '*'
      verbs:
      - get
      - list
      - watch
    # This permission is needed to watch/unwatch types as they are registered or removed.
    - apiGroups:
      - apiextensions.k8s.io
      resources:
      - customresourcedefinitions
      verbs:
      - get
      - list
      - watch
    # This permission is needed so that the ResourceGroup Controller can reconcile a ResourceGroup CR
    - apiGroups:
      - kpt.dev
      resources:
      - resourcegroups
      verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
    # This permission is needed so that the ResourceGroup Controller can update the status of a ResourceGroup CR
    - apiGroups:
      - kpt.dev
      resources:
      - resourcegroups/status
      verbs:
      - get
      - patch
      - update
    # This permission is needed so that the ResourceGroup Controller can work on a cluster with PSP enabled
    - apiGroups:
      - policy
      resourceNames:
      - acm-psp
      resources:
      - podsecuritypolicies
      verbs:
      - use
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      labels:
        configmanagement.gke.io/arch: "csmr"
        configmanagement.gke.io/system: "true"
      name: resource-group-leader-election-role
      namespace: resource-group-system
    rules:  // The following permissions are needed so that the leader election can work
    - apiGroups:
      - ""
      resources:
      - configmaps
      verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
    - apiGroups:
      - ""
      resources:
      - configmaps/status
      verbs:
      - get
      - update
      - patch
    - apiGroups:
      - ""
      resources:
      - events
      verbs:
      - create
    - apiGroups:
      - coordination.k8s.io
      resources:
      - leases
      verbs:
      - '*'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
