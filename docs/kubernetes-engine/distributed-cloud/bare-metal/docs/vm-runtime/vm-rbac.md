---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-rbac/
title: Role-based access control (RBAC) for VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:12.169975+00:00
---

# Role-based access control (RBAC) for VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Role-based access control (RBAC) for VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VM Runtime on GDC manages a wide range of resources related to your VMs. These resources include GKE-defined resources, KubeVirt-defined resources, and Kubernetes resources. VM Runtime on GDC uses [role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) to set and enforce permissions for managed resources. To help you work with these resources and manage your VMs, we've provided four pre-configured ClusterRoles:

  * `kubevm.admin`
  * `kubevm.edit`
  * `kubevm.view`
  * `kubevm.cluster.view`



These built-in roles provide a generalized access model on the custom resources related to VM Runtime on GDC. Each role has pre-established permissions to operate on the resources. This document provides information about resources VM Runtime on GDC manages so that cluster administrators can customize their own access model.

## Predefined ClusterRoles

This section describes each of the predefined ClusterRoles. These ClusterRoles are only available when VM Runtime on GDC is enabled:

  * When VM Runtime on GDC is enabled, the four predefined ClusterRoles are automatically created.
  * When VM Runtime on GDC is disabled, the four predefined ClusterRoles are deleted.



The following table lists the cluster roles and their related permissions:

Cluster role | Description | Access verbs  
---|---|---  
`kubevm.admin` | Grants full access to all GKE resources. | 

  * `get`
  * `list`
  * `watch`
  * `delete`
  * `create`
  * `update`
  * `patch`
  * `deletecollection`

  
`kubevm.edit` | Grants read/write access to all GKE resources. | 

  * `get`
  * `list`
  * `watch`
  * `delete`
  * `create`
  * `update`
  * `patch`

  
`kubevm.view` | Grants read access to all GKE resources. | 

  * `get`
  * `list`
  * `watch`

  
`kubevm.cluster.view` | Grants read access to cluster-wise resources. This cluster role is necessary when the edit/view role is bound to a namespace while access to cluster-wise resources is needed. | 

  * `get`
  * `list`
  * `watch`

  
  
## Aggregated ClusterRoles

The `kubevm.admin`, `kubevm.view`, and `kubevm.edit` ClusterRoles aren't used directly. Instead, these three roles are aggregated to Kubernetes default `admin`, `view`, and `edit` ClusterRoles respectively. This aggregation extends the default Kubernetes roles so they can be used to manage GKE resources. With [aggregated ClusterRoles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles), you can use Kubernetes default roles to manage access to GKE resources or create your own roles based on the predefined ClusterRoles.

### Example aggregation label

The `kubevm.edit` ClusterRole has the label `rbac.authorization.k8s.io/aggregate-to-edit: "true"`, which aggregates it to the Kubernetes `edit` ClusterRole. The permissions in the `kubevm.edit` ClusterRole are granted to the Kubernetes default `edit` role. The `kubevm.admin` and the `kubevm.view` ClusterRoles are aggregated similarly with `aggregate-to-admin` or `aggregate-to-view` annotations.
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
        name: kubevm.edit
        labels:
          kubevm: kubevm.edit**      rbac.authorization.k8s.io/aggregate-to-edit: "true"**
    ...
    

## Typical User Scenarios

The following sections describe how to use [RoleBinding and ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) to grant the permissions specified in the predefined ClusterRoles to a user or set of users.

### Cluster admin

To grant admin permissions to a user or set of users, create a ClusterRoleBinding with the Kubernetes default `admin` ClusterRole.

#### Example ClusterRoleBinding

The following `admin-charlie` example ClusterRoleBinding gives user `charlie` admin permissions. The ClusterRoleBinding uses permissions from the default Kubernetes `admin` ClusterRole, which includes permissions from the predefined `kubevm.admin` ClusterRole through aggregation.
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: admin-charlie
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: charlie
    

### Cluster viewer

To grant viewer permissions to a user or set of users, create a ClusterRoleBinding with the Kubernetes default `view` ClusterRole. See Example ClusterRoleBinding for a similar ClusterRoleBinding example.

### Cluster editor

To grant editor permissions to a user or set of users, create a ClusterRoleBinding with the Kubernetes default `edit` ClusterRole. See Example ClusterRoleBinding for a similar ClusterRoleBinding example.

### Namespaced editor

To grant namespaced editor permissions to a user or set of users, you need to create two separate bindings:

  * Create a RoleBinding on the namespace and reference the default Kubernetes `edit` ClusterRole.

  * Create a ClusterRoleBinding that references the predefined `kubevm.cluster.view` ClusterRole. This ClusterRoleBinding is needed, because some resources, such as `virtualmachinetypes` and `storageclasses`, aren't namespaced.




#### Role binding examples (namespaced editor)

The following RoleBinding and ClusterRoleBinding examples give user `charlie` editor permissions for resources in the `default` namespace:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: edit-charlie
      namespace: default
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: edit
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: charlie
    
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: kubevm-cluster-view-charlie
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: kubevm.cluster.view
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: charlie
    

### Namespaced viewer

To grant namespaced viewer permissions to a user or set of users, you need to create two separate bindings:

  * Create a RoleBinding on the namespace and reference the default Kubernetes `view` ClusterRole.

  * Create a ClusterRoleBinding that references the predefined `kubevm.cluster.view` ClusterRole.




See Role binding examples (namespaced editor) for similar RoleBinding and ClusterRoleBinding examples.

## Resources used by VM Runtime on GDC

The following sections contain tables of resources used by VM Runtime on GDC. These sections are for informational purposes only. If you plan to use predefined roles in the typical user scenarios described in the preceding sections, there's no specific use for this information.

If, however, you don't want to use the predefined roles, you can use this resource information to create your own, customized roles.

### Google Kubernetes Engine-defined resources

The predefined ClusterRoles focus on access to GKE-defined resources. The following table lists the GKE resources and the access permissions granted by each of the predefined ClusterRoles.

Resource | Generated | Cluster-wise | `kubevm.admin` | `kubevm.view` | `kubevm.edit` | `kubevm.cluster.view`  
---|---|---|---|---|---|---  
`virtualmachineaccessrequests` | – | – | Full | Read | Read/Write | –  
`virtualmachinedisks` | – | – | Full | Read | Read/Write | –  
`virtualmachines` | – | – | Full | Read | Read/Write | –  
`gpuallocations` | – | – | Full | Read | Read/Write | –  
`guestenvironmentdata` | Yes | – | Full | Read | Read/Write | –  
`vmruntimes` | – | Yes | Full | Read | Read/Write | Read  
`virtualmachinetypes` | – | Yes | Full | Read | Read/Write | Read  
`vmhighavailabilitypolicies` | – | Yes | Full | Read | Read/Write | Read  
`networkinterfaces` | Yes | – | Full | Read | Read/Write | –  
`networks` | – | Yes | Full | Read | Read/Write | Read  
  
### KubeVirt resources

VM Runtime on GDC is based on the [KubeVirt open source project](https://kubevirt.io/). By default, the permissions for the KubeVirt resources are automatically aggregated to the default Kubernetes roles, similar to the GKE-managed resources. Use the resource information in the following table if you want to create your own, customized roles:

Resource | Generated | Cluster-wise  
---|---|---  
`virtualmachineinstances`/console | – | –  
`virtualmachineinstances`/vnc | – | –  
`virtualmachineinstances`/portforward | – | –  
`virtualmachineinstances`/start | – | –  
`virtualmachineinstances`/stop | – | –  
`virtualmachineinstances`/restart | – | –  
`virtualmachines` | Yes | –  
`virtualmachineinstances` | Yes | –  
`datavolumes` | – | –  
`storageprofiles` | – | Yes  
`cdiconfigs` | – | Yes  
  
### Kubernetes resources

When you work with VM Runtime on GDC and VMs, you may need to manage access to the following Kubernetes resources. Use the resource information in the following table if you want to create your own, customized roles:

Resource | Generated | Cluster-wise  
---|---|---  
`pods` | Yes | –  
`services` | – | –  
`persistentvolumeclaims` | – | –  
`secrets` | – | –  
`nodes` | – | Yes  
`storageclasses` | – | Yes  
`configmaps` | – | –  
  
## ClusterRole YAML examples

You can retrieve YAML for the ClusterRoles with the following `kubectl` command:
    
    
    kubectl get ClusterRole CLUSTERROLE_NAME -o yaml --kubeconfig KUBECONFIG_PATH
    

Replace the following:

  * `CLUSTERROLE_NAME`: the name of the ClusterRole, such as `kubevm.cluster.view`.
  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the cluster.



Here are examples of the command output for each of the four predefined ClusterRoles:

  * `kubevm.admin`
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          creationTimestamp: "2022-10-11T21:10:31Z"
          labels:
            kubevm: kubevm.admin
            rbac.authorization.k8s.io/aggregate-to-admin: "true"
          name: kubevm.admin
          resourceVersion: "16654950"
          uid: 3296c279-6e85-4ea6-b250-548bf0c3e935
        rules:
        - apiGroups:
          - vm.cluster.gke.io
          resources:
          - virtualmachineaccessrequests
          - virtualmachinedisks
          - virtualmachines
          - gpuallocations
          - guestenvironmentdata
          - vmruntimes
          - virtualmachinetypes
          - vmhighavailabilitypolicies
          verbs:
          - get
          - delete
          - create
          - update
          - patch
          - list
          - watch
          - deletecollection
        - apiGroups:
          - networking.gke.io
          resources:
          - networkinterfaces
          - networks
          verbs:
          - get
          - delete
          - create
          - update
          - patch
          - list
          - watch
          - deletecollection
        

  * `kubevm.edit`
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          creationTimestamp: "2022-10-11T21:10:31Z"
          labels:
            kubevm: kubevm.edit
            rbac.authorization.k8s.io/aggregate-to-edit: "true"
          name: kubevm.edit
          resourceVersion: "16654951"
          uid: 237bf9ae-b2c8-4303-94dc-e6425a2df331
        rules:
        - apiGroups:
          - vm.cluster.gke.io
          resources:
          - virtualmachineaccessrequests
          - virtualmachinedisks
          - virtualmachines
          - gpuallocations
          - guestenvironmentdata
          - vmruntimes
          - virtualmachinetypes
          - vmhighavailabilitypolicies
          verbs:
          - get
          - delete
          - create
          - update
          - patch
          - list
          - watch
        - apiGroups:
          - networking.gke.io
          resources:
          - networkinterfaces
          - networks
          verbs:
          - get
          - delete
          - create
          - update
          - patch
          - list
          - watch
        

  * `kubevm.view`
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          creationTimestamp: "2022-10-11T21:10:31Z"
          labels:
            kubevm: kubevm.view
            rbac.authorization.k8s.io/aggregate-to-view: "true"
          name: kubevm.view
          resourceVersion: "16654953"
          uid: b5b54e2d-0097-4698-abbd-aeac212d0a34
        rules:
        - apiGroups:
          - vm.cluster.gke.io
          resources:
          - virtualmachineaccessrequests
          - virtualmachinedisks
          - virtualmachines
          - gpuallocations
          - guestenvironmentdata
          - vmruntimes
          - virtualmachinetypes
          - vmhighavailabilitypolicies
          verbs:
          - get
          - list
          - watch
        - apiGroups:
          - networking.gke.io
          resources:
          - networkinterfaces
          - networks
          verbs:
          - get
          - list
          - watch
        

  * `kubevm.cluster.view`
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          creationTimestamp: "2022-10-11T21:10:31Z"
          labels:
            kubevm: kubevm.cluster.view
          name: kubevm.cluster.view
          resourceVersion: "16654956"
          uid: b25dde64-67da-488b-81d2-1a08f9a4a7c1
        rules:
        - apiGroups:
          - vm.cluster.gke.io
          resources:
          - vmruntimes
          - virtualmachinetypes
          - vmhighavailabilitypolicies
          verbs:
          - get
          - list
          - watch
        - apiGroups:
          - networking.gke.io
          resources:
          - networks
          verbs:
          - get
          - list
          - watch
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
