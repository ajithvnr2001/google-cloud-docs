---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects/
title: Manage existing cluster objects \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:47.435687+00:00
---

# Manage existing cluster objects  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Manage existing cluster objects Stay organized with collections  Save and categorize content based on your preferences. 

When Config Sync manages a cluster object, it watches the object and the set of configs in the repo that affect the object, and ensures that they are in sync. This topic describes how to start managing an existing object and how to stop managing an object that is currently managed without deleting the object.

An object in a cluster is managed by Config Sync if it has the `configmanagement.gke.io/managed: enabled` annotation, and its `configsync.gke.io/resource-id` annotation, which tracks the group, kind, namespace, and name information of the object, is correct.

The format of the `configsync.gke.io/resource-id` annotation is `GROUP_KIND_NAMESPACE_NAME` for a namespace-scoped object, and `GROUP_KIND_NAME` for a cluster-scoped object.

The following flow chart describes some situations that cause an object to become managed or unmanaged:

![How to manage or unmanage a Kubernetes object using Config Sync](https://docs.cloud.google.com/static/kubernetes-engine/config-sync/docs/img/resource_flow.svg)

The chart contains three separate flows: 1) start managing an object, 2) stop managing an object, and 3) delete a managed object.

  1. I want to start managing an object. Does the object have a manifest? Or in other words, does the object have a config in the repo? 
     * **No** : Create a config for the object. Config Sync sets the annotation `configmanagement.gke.io/managed: enabled`, sets the `configsync.gke.io/resource-id` annotation to match the object, and begins managing the object.
     * **Yes** : Does the config set the following annotation? `configmanagement.gke.io/managed: disabled`
       * **No** : The object is managed by default.
       * **Yes** : Edit the config to remove the `configmanagement.gke.io/managed: disabled` annotation. When the change is pushed to the source repo, Config Sync notices the change, applies the annotation `configmanagement.gke.io/managed: enabled` and the annotation `configsync.gke.io/resource-id`, and applies the config.
  2. I want to stop managing an object but not delete it. 
     * Edit the config for the object in the repo, and set the annotation `configmanagement.gke.io/managed: disabled`. When the config change is detected, Config Sync stops managing the object.
  3. I want to stop managing an object and delete it. 
     * Delete the object's config from the repo. When you delete a config for an object that was previously managed, Config Sync deletes the object from all clusters or namespaces the config applies to.



In addition to the `configmanagement.gke.io/managed: enabled` annotation and the `configsync.gke.io/resource-id` annotation, Config Sync applies the label `app.kubernetes.io/managed-by: configmanagement.gke.io` to all objects it manages. This label allows you to easily list all objects by Config Sync.

### Why not apply the annotation manually?

Config Sync uses a declarative model to apply configuration changes to your clusters by reading your desired configuration from your repo. If you attempt to apply the annotation manually (either using the `kubectl` command or the Kubernetes API), Config Sync overrides the manual automatically with the contents of your repo.

## Before you begin

The following examples build upon [Get started with Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo). Before you begin the following steps, follow the quickstart and complete all of the steps before [Explore and test the Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo#sync-status).

## List all managed objects

To list all objects managed by Config Sync on a given cluster or namespace, use a label selector like the following:
    
    
    kubectl get object-type -n namespace -l "app.kubernetes.io/managed-by=configmanagement.gke.io"
    

To list all objects **not** managed by Config Sync, use a label selector like this:
    
    
    kubectl get object-type -n namespace -l "app.kubernetes.io/managed-by!=configmanagement.gke.io"
    

For example, this command lists RoleBindings in the `gamestore` namespace that **are** managed by Config Sync:
    
    
    kubectl get rolebindings -n gamestore \
        -l "app.kubernetes.io/managed-by=configmanagement.gke.io"
    

The output is similar to the following:
    
    
    NAME                              ROLE                                          AGE
    configsync.gke.io:ns-reconciler   ClusterRole/configsync.gke.io:ns-reconciler   34h
    gamestore-admin                   ClusterRole/admin                             34h
    gamestore-webstore-admin          ClusterRole/webstore-admin                    34h
    

This command lists RoleBindings in the `kube-system` namespace that are **not** managed by Config Sync:
    
    
    kubectl get rolebindings -n kube-system \
        -l "app.kubernetes.io/managed-by!=configmanagement.gke.io"
    

The output is similar to the following:
    
    
    NAME                                             AGE
    fluentd-gcp-scaler-binding                       2d21h
    gce:cloud-provider                               2d21h
    heapster-binding                                 2d21h
    metrics-server-auth-reader                       2d21h
    system::leader-locking-kube-controller-manager   2d21h
    system::leader-locking-kube-scheduler            2d21h
    system:controller:bootstrap-signer               2d21h
    system:controller:cloud-provider                 2d21h
    system:controller:token-cleaner                  2d21h
    

## Start managing an existing object

You can create a config for an existing Kubernetes object, such as a namespace that already exists in your cluster before you install Config Sync. However, this config is ignored unless the object has the annotation `configmanagement.gke.io/managed: enabled` and has the correct `configsync.gke.io/resource-id` annotation. For an existing object, you need to apply the annotation manually.

For namespaces specifically, Config Sync **does** apply configs that create new objects within an unannotated namespace, and applies the `configmanagement.gke.io/managed: enabled` and `configsync.gke.io/resource-id` annotations to those objects. However, Config Sync refuses to modify or remove any unannotated cluster-scoped object from a cluster. This is illustrated in the diagram in [Working with configs over time](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs#config-flow).

The following example demonstrates how to manage an existing Role object. First, you create a Role manually, then begin managing it with Config Sync.

  1. Create the `myrole` Role in the `gamestore` namespace:
         
         kubectl create role -n gamestore myrole --verb=get --resource=pods

  2. View the permissions granted by the `myrole` Role:
         
         kubectl describe role -n gamestore myrole
         
         Name:         myrole
         Labels:       <none>
         Annotations:  <none>
         PolicyRule:
           Resources  Non-Resource URLs  Resource Names  Verbs
           ---------  -----------------  --------------  -----
           pods       []                 []              [get]
         

The Role only has permission to `get` Pods.

  3. At this point, the Role exists in the cluster, but Config Sync does not know about it.

     1. In a terminal, go to the local clone of your repo.
     2. Use the following command to create a YAML manifest for `myrole` and save the manifest to a new file called `gamestore-myrole.yaml`.
            
            kubectl get role myrole -n gamestore -o yaml > gamestore-myrole.yaml
            

     3. Edit the `gamestore-myrole.yaml` file.

        1. Remove all fields under the `metadata` key except for `name` and `namespace`.
        2. Add the `list` verb after `get` in the `rules.verbs` list field.

Save the changes. The resulting file has the following contents:
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: myrole
      namespace: gamestore
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - get
      **- list**
    

     4. Commit the change to the repo.

     5. Wait a few moments for the ConfigManagement Operator to notice the commit. To verify that the `myrole` Role is now managed by Config Sync, run `kubectl describe` again.
            
            kubectl describe role myrole -n gamestore
            




Notice the annotation `configmanagement.gke.io/managed: enabled`, which indicates that the object is managed by Config Sync, and the annotation `configsync.gke.io/resource-id`, which tracks the group, kind, namespace, and name information. Also notice the annotations that show the path and file name in the repo that caused the most recent configuration change to the object, and the Git hash that represents the commit.
    
    
    Name:         myrole
    Labels:       app.kubernetes.io/managed-by=configmanagement.gke.io
                  configsync.gke.io/declared-version=v1
    Annotations:  **config.k8s.io/owning-inventory: config-management-system_root-sync
                  configmanagement.gke.io/cluster-name: my-cluster
                  configmanagement.gke.io/managed: enabled
                  configmanagement.gke.io/source-path: config-sync-quickstart/multirepo/root/gamestore-myrole.yaml
                  configmanagement.gke.io/token: 747b843a7ddbd945c0616034a935cf648b58e7b5
                  configsync.gke.io/declared-fields: {"f:rules":{}}
                  configsync.gke.io/git-context: {"repo":"https://github.com/GoogleCloudPlatform/anthos-config-management-samples","branch":"main","rev":"HEAD"}
                  configsync.gke.io/manager: :root**
                  configsync.gke.io/resource-id: rbac.authorization.k8s.io_role_gamestore_myrole
    PolicyRule:
      Resources  Non-Resource URLs  Resource Names  Verbs
      ---------  -----------------  --------------  -----
      pods       []                 []              [get **list**]
    

## Stop managing a managed object

This example shows how to stop managing an object that Config Sync is currently managing, such as the `myrole` Role in Start managing an existing object.

**Note:** Before removing a namespace from management, be sure you understand what happens to objects within that namespace that are still managed.

  1. Edit the `config-sync-quickstart/multirepo/root/rolebinding-gamestore-webstore-admin.yaml` file in the local clone of your repo, and add an `annotations:` section that matches the bold text below:
         
         kind: RoleBinding
          apiVersion: rbac.authorization.k8s.io/v1
          metadata:
            **annotations :
              configmanagement.gke.io/managed: disabled**
            name: gamestore-webstore-admin
            namespace: gamestore
          subjects:
          - kind: ServiceAccount
            name: ns-reconciler-gamestore
            namespace: config-management-system
          roleRef:
            kind: ClusterRole
            name: webstore-admin
            apiGroup: rbac.authorization.k8s.io
         

Save the file.

  2. Create a Git commit with your changes, and push the commit to your repo.

  3. Wait a few moments for Config Sync to notice and apply the new commit.

  4. Use the following command to verify the annotations and labels of the `gamestore-webstore-admin` RoleBinding are both empty. Config Sync does not set the `configmanagement.gke.io/managed` annotation to `disabled` on the object.
         
         kubectl get rolebinding gamestore-webstore-admin -n gamestore -o yaml
         
         
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           annotations:
           name: gamestore-webstore-admin
           namespace: gamestore
         subjects:
         - kind: ServiceAccount
           name: ns-reconciler-gamestore
           namespace: config-management-system
         roleRef:
           kind: ClusterRole
           name: webstore-admin
           apiGroup: rbac.authorization.k8s.io
         




After verifying that the object is now disabled, you could remove the config from your repository and verify that the now-unmanaged object is **not** deleted from the namespace. If you want to manage the object again, you must add its config back into your repository. Because of this, you might want to unmanage objects and leave their configs in the repo.

Now that the object is not managed, it is not created or recreated on new or existing clusters, and it is not removed even if it exists. To resume managing an object that you previously stopped managing, see the next example, _Resume managing a previously unmanaged object_.

## Resume managing a previously unmanaged object

This example shows how to resume managing an object you previously removed from management, as in Stop managing an existing object. It assumes that you have **not** removed the config for the `gamestore-webstore-admin` RoleBinding.

  1. If you deleted the `gamestore-webstore-admin` RoleBinding from your repo in the last commit, perform the following steps.

     1. Use `git revert` to revert the last commit:
            
            git revert HEAD~1
            

You are asked to confirm the revert operation.

     2. Push the revert commit to your repo.
            
            git push
            

  2. Edit the `config-sync-quickstart/multirepo/root/rolebinding-gamestore-webstore-admin.yaml` file in the local clone of your repo and remove the `configmanagement.gke.io/managed: disabled` annotation. Save the file.

  3. Commit and push your change. Config Sync does the following:

     * Notices the change
     * Applies the `configmanagement.gke.io/managed: enabled` annotation and the `configsync.gke.io/resource-id` annotation; the object is now managed.
     * Applies the config, as would happen with any managed object.
  4. To verify that the object is now managed, list its annotations:
         
         kubectl get rolebinding gamestore-webstore-admin -n gamestore -o yaml
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           annotations:
             configmanagement.gke.io/cluster-name: my-cluster
             **configmanagement.gke.io/managed: enabled**
             **configsync.gke.io/resource-id: rbac.authorization.k8s.io_rolebinding_gamestore_gamestore-webstore-admin**
         ...
         




## Stop managing a namespace

You can stop managing a namespace in the same way as you stop managing any type of object. If you want to stop managing other resources within the namespace, perform the following steps:

  1. Add the `configmanagement.gke.io/managed:disabled` annotation to the namespace config and all configs in the same namespace. All objects in the namespace must have this annotation.

**Caution:** In a hierarchical source of truth, if the namespace is inherited from an [abstract namespace](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo#namespace-inheritance), it cannot be unmanaged.
  2. Commit and push your changes to the repo. Wait for the Operator to sync with the repo.

  3. Delete the unmanaged resources from the repository.

**Warning:** It is a known issue that if you're not using [RootSync and RepoSync APIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields), deleting the unmanaged namespace from the repository causes the namespace to be deleted from the live cluster. For the unmanaged resources that are accidentally deleted, you need to add them back manually in the cluster, such as using `kubectl apply`. To use RootSync and RepoSync APIs, you need to [migrate your ConfigManagement object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo).



If configs for managed configs exist within an unmanaged namespace directory, the reconciler logs errors, but other configs continue to sync normally.

## Delete managed resources

When you remove an individual resource from a source of truth, that object is deleted from the cluster when Config Sync next syncs from the source of truth. Alternatively, you can enable deletion propagation which lets you bulk delete objects.

### Delete individual objects

With Config Sync's default behaviour, when you remove an object from a source of truth, that object is deleted from the cluster when Config Sync syncs from the source of truth.

There are multiple ways to check the status of Config Sync or the status of specific objects:

  * [Use `nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install).
  * [Use `kubectl` to examine resources](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync#use_kubectl_to_examine_resources).
  * [Use the Config Sync dashboard](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard).



### Bulk delete objects

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, deleting a RootSync or RepoSync causes Config Sync to abandon the objects that were previously applied from the source of truth. Alternatively, you can enable deletion propagation to delete all previously-applied objects.

When you enable deletion propagation on a RootSync or RepoSync object, and then delete that object, Config Sync automatically deletes every object that was managed by that RootSync or RepoSync.

Deletion propagation can help make it easier to clean up resources, for example if you're migrating to a new namespace or cluster, cleaning up after a demo or experiment, or uninstalling an application.

#### Deletion propagation options

Deletion propagation is disabled by default. To enable deletion propagation, you add the `configsync.gke.io/deletion-propagation-policy: Foreground` annotation to your RootSync or RepoSync object, such as in the following example:
    
    
    # example-rootsync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: example-rootsync
      namespace: config-management-system
      **annotations :
        configsync.gke.io/deletion-propagation-policy: Foreground**
    spec:
      sourceType: git
      sourceFormat: unstructured
      git:
        repo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
        branch: main
        dir: config-sync-quickstart/multirepo/root
        auth: none
        period: 30s
    

Alternatively, you can update an existing RootSync or RepoSync to use deletion propagation by running the following command:

### RootSync
    
    
    kubectl patch RootSync ROOTSYNC_NAME \
      --namespace config-management-system \
      --type merge \
      --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Foreground"}}}'
    

Replace `ROOTSYNC_NAME` with the name of the RootSync that you want to update.

### RepoSync
    
    
    kubectl patch RepoSync REPOSYNC_NAME \
      --namespace config-management-system \
      --type merge \
      --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Foreground"}}}'
    

Replace `REPOSYNC_NAME` with the name of the RepoSync that you want to update.

To disable deletion propagation, remove the annotation or change the value to `configsync.gke.io/deletion-propagation-policy: Orphan`:

**Note:** Config Sync stops managing all objects when using the `Orphan` deletion propagation policy. This behavior ensures that the orphaned objects can be updated by other clients or adopted by a new RootSync or RepoSync object.

### RootSync
    
    
    kubectl patch RootSync ROOTSYNC_NAME \
      --namespace config-management-system \
      --type merge \
      --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Orphan"}}}'
    

Replace `ROOTSYNC_NAME` with the name of the RootSync that you want to update.

### RepoSync
    
    
    kubectl patch RepoSync REPOSYNC_NAME \
      --namespace config-management-system \
      --type merge \
      --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Orphan"}}}'
    

#### Propagate object deletion

This example shows how to apply deletion propagation to a RootSync or RepoSync object and then delete the RootSync or RepoSync to delete all objects that were managed by the RootSync or RepoSync.

**Caution:** for RepoSync objects, don't delete the Namespace that the RepoSync is in before the RepoSync finishes deleting. Doing so can cause the RoleBinding to be deleted before deletion propagation has completed, causing a deadlock which can block deletion of both the RepoSync and the Namespace.

### RootSync

  1. Apply the annotation to a RootSync object to enable deletion propagation:
         
         kubectl patch RootSync example-rootsync \
           --namespace config-management-system \
           --type merge \
           --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Foreground"}}}'
         

  2. Delete the RootSync object and wait for Config Sync to delete it:
         
         kubectl delete RootSync example-rootsync --namespace config-management-system --wait
         

Deleting the RootSync can take a few minutes to complete.




### RepoSync

  1. Apply the annotation to a RepoSync object to enable deletion propagation:
         
         kubectl patch RepoSync example-reposync \
           --namespace example-namespace \
           --type merge \
           --patch '{"metadata":{"annotations":{"configsync.gke.io/deletion-propagation-policy":"Foreground"}}}'
         

  2. Delete the RepoSync object and wait for Config Sync to delete it:
         
         kubectl delete RepoSync example-reposync --namespace example-namespace --wait
         

Deleting the RepoSync can take a few minutes to complete.




## Prevent deletion for Kubernetes objects

After you remove a Kubernetes object from a Git repository that is managed by Config Sync, this object is also deleted from the cluster when the new commit is synced to the cluster.

If you want to prevent Config Sync from deleting the object when its configuration is removed from the Git repository, you can take the following steps:

  1. Add the annotation `client.lifecycle.config.k8s.io/deletion: detach` to the object configuration in Git repository.

  2. Commit and push the change in Git repository.

  3. Wait for the change being synced to the cluster.




After you complete these steps, Config Sync won't delete this object from the cluster when its configuration is removed from the Git repository, but it can still be deleted by other clients.

## Ignore an object in the source of truth

You might want Config Sync to ignore an object in your source of truth. For example, a [kpt function](https://kpt.dev/book/02-concepts/#functions) configuration should never be applied to the cluster.

For objects you want Config Sync to ignore, add the [`config.kubernetes.io/local-config: "true"`](https://kubernetes.io/docs/reference/labels-annotations-taints/#config-kubernetes-io-local-config) annotation to the object. After you add this annotation, Config Sync ignores this object as if it is removed from the source of truth. Resources with the `local-config` annotation set to any value other than `"false"` are treated as if it's set to `"true"` and are ignored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
