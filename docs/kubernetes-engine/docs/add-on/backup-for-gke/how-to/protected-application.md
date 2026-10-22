---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application/
title: Define custom backup and restore logic \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:39.017045+00:00
---

# Define custom backup and restore logic  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Define custom backup and restore logic Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

When you enable the Backup for GKE agent in your Google Kubernetes Engine cluster, Backup for GKE provides a `CustomResourceDefinition` that introduces a new kind of Kubernetes resource: the `ProtectedApplication`.

Composing a `ProtectedApplication` involves three activities:

  * Selecting the set of resources that you want to backup and restore as part of the application.

  * Defining detailed orchestration rules for a subset of those resources.

  * Validating the `ProtectedApplication` to check if it is ready for backup.




`ProtectedApplication` resources provide you with these capabilities when customizing backup and restore logic at the application level:

  * More fine-grained backup and restore operations. Without `ProtectedApplications`, the scope of your backups must be defined at the `Namespace` level (either by selecting [allNamespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.all_namespaces) or [selectedNamespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.selected_namespaces)). Similar logic applies to namespaced resource restoration. Creating `ProtectedApplication` resources allows you to supply a name to a subset of the resources in a `Namespace`. You can then backup and restore that subset by listing [selectedApplications](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.selected_applications) in your backup scope (and similarly, for [restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#FIELDS.selected_applications)).

  * Orchestrating fine-grained details of the backup or restore process, including:

    * Skipping selected volumes during backup.

    * Incorporating application topology into backup and restore (for example, only backing up one instance of a replicated database and using it to restore multiple instances).

    * Executing user-defined _hooks_ before and after volumes are snapshotted. These can be used, for example, to flush and quiesce a workload before snapshotting and unquiesce it afterwards.




You create `ProtectedApplication` by using `kubectl` like other Kubernetes resources. They are completely optional. If `ProtectedApplication` resources are not present, Backup for GKE creates volume backups for all volumes within the scope of a backup and the resulting volume backups will be _crash consistent_ \- all writes flushed to the disk at a particular point in time will be captured (i.e., no partial writes). However, some applications may keep data in memory that isn't flushed to disk, so whether or not an application can recover successfully from a crash consistent backup depends upon the application logic.

## Selecting resources

The first step in building your `ProtectedApplication` resource is to identify the other resources in the same `Namespace` that you want to include as part of the application. This is the set of resources that will be backed up or restored if you supply the [selectedApplications](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.selected_applications) scope option in your `BackupPlan` configuration.

Resources are identified using a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). This requires that you label all your resources (using the `metadata.label` field in each resource) with the same label. Note that this also applies to resources that are automatically created by controllers. These auto-created resources are labeled using their corresponding template. Note that it is common to re-use the same label you are already using to associate generated `Pods` and `PersistentVolumeClaims` with their parent resource.

Usage considerations include the following:

  * If you want to protect resources that create child resources, then both parent resources (like `StatefulSet`, `Deployment`, or `DaemonSet`) and child resources (like `Pod` or `PersistentVolumeClaim`) must both have the label that is used in the `Selector` field of the `ProtectedApplication`.
  * If some of the resources referenced by your `ProtectedApplication` are created automatically by an operator, you should also include the operator's custom resources in your `ProtectedApplication` selector. This will help avoid a restore-time race condition that can occur when the operator attempts to create a resource while it is simultaneously being restored from backup.



The following example shows how you can apply the `app: nginx` label to the other resources in addition to the `Deployment`.
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: nginx-vars
      namespace: webserver
      labels:
        app: nginx
      data:
        ...
    ---
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: nginx-logs
      namespace: webserver
      labels:
        app: nginx
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 50Mi
      storageClassName: standard-rwo
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
      namespace: webserver
      labels:
        app: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          volumes:
            - name: nginx-logs
              persistentVolumeClaim:
               claimName: nginx-logs
          containers:
          ...
    

Once you have your selected label applied to all your target resources (and the templates from which additional resources are generated), then you can reference those resources from a `ProtectedApplication`. For example:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: nginx
      namespace: webserver
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: nginx
      ...
    

## Define orchestration rules

Once you have all the resources in your `ProtectedApplication` identified, you can choose to define detailed orchestration rules for a subset of these resources. These rules may only apply to two kinds of resources: [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) and are referenced in the `components` section of the `ProtectedApplication`.

### Component overview

Configuring a component involves the following:

  * Selecting a fundamental _strategy_ for how backup and restore will work for this component. There are three strategies available:

    * `BackupAllRestoreAll` \- backup the volumes associated with all instances of the component and restore them all from the backups.

    * `BackupOneRestoreAll` \- backup the volumes from only one instance of the component and use those backups to restore all instances.

    * `DumpAndLoad` \- export data from the application to a single volume at backup time and import that data into the application at restore time.

  * Defining execution hooks to run during backup (and possibly restore, depending on the strategy). A hook is a command that is executed in specific containers.

  * Selecting a subset of volumes to backup.




### Execution hooks

A hook is a shell command that Backup for GKE executes in a container at particular phase of the backup or restore process.

There are four different types of hooks:

  * `pre hooks` \- these commands are executed right before volumes are backed up and are generally expected to flush any data in memory to disk and then quiesce the application so that no new disk writes are occurring. These hooks are used in the `BackupAllRestoreAll` and `BackupOneRestoreAll` strategies.

  * `post hooks` \- these commands are executed during the volume backup process right after the SNAPSHOTTING step of the volume backup process (before the UPLOADING step). Generally, the SNAPSHOTTING step takes just a few seconds. They are generally expected to unquiesce the application (i.e. allow normal processing and disk writes to proceed). These hooks are used in the `BackupAllRestoreAll`, `BackupOneRestoreAll`, and `DumpAndLoad` strategies.

  * `dump hooks` \- these commands are executed before the volume is backed up in the `DumpAndLoad` strategy and are generally expected to export data from the application into the designated backup volume.

  * `load hooks` \- these commands are executed at restore time after the backup volume is restored in `DumpAndLoad` strategy cases. They are generally expected to import the data from the backup volume into the application.




You may provide more than one hook for each type and Backup for GKE will execute them in the order you define them.

You define hooks as part of the component section of the `ProtectedApplication` specification. All hook definitions have the same available fields:

  * `name` \- a name you assign to the hook.

  * `container` \- (optional) name of container to run command in. If you don't supply the container, Backup for GKE will run the hook in the first container defined for the target `Pod`(s).

  * `command` \- this is the actual command sent into the container, constructed as an array of words. The first word in the array is the path to the command and subsequent words are the arguments to be passed to the command.

  * `timeoutSeconds` \- (optional) time before hook execution is aborted. If you don't supply this, then it defaults to 30 seconds.

  * `onError` \- (optional) behavior taken when the hook fails. May be set to `Ignore` or `Fail` (default). If you set this to `Fail`, then when a hook fails, the volume backup will fail. If you set this to `Ignore`, failures of this hook are ignored.




Before applying `ProtectedApplication` hooks to your application, you should test the command by using [`kubectl exec`](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/#running-individual-commands-in-a-container) to ensure that the hooks behave as expected:
    
    
    kubectl exec POD_NAME -- COMMAND
    

Replace the following:

  * `POD_NAME`: the name of the Pod that contains the `ProtectedApplication` resource.
  * `COMMAND`: the array containing the command that you want to run in the container.



### Selecting a subset of volumes to backup

Sometimes, applications write to volumes that are not interesting to restore (for example, certain log or scratch volumes). You can suppress the backup of these volumes by using a _volume selector_.

To use this feature, you must first apply a common label to the `PersistentVolumeClaim` resources of volumes you want to backup. You must also leave this label **off** of the `PersistentVolumeClaim` resources of volumes you do **not** want backed up. Then, you include a `volumeSelector` clause in your component definition as follows:
    
    
    spec:
      ...
      components:
      ...
        strategy:
          ...
          volumeSelector:
            matchLabels:
              label_name: label_value
    

If you supply a `volumeSelector` for a component, then only the volumes whose `PersistentVolumeClaim` resources have the given label are backed up and restored. At restore time, any other volumes are provisioned as empty instead of restored from a volume backup.

### Strategy: BackupAllRestoreAll

This is the simplest strategy and backs up all the component's volumes at backup time and restores them all from their volume backups at restore time. It is your best choice when your application has no replication between `Pods`.

This strategy supports the following parameters:

  * `backupPreHooks` \- (optional) an ordered list of hooks that are executed right before volumes are backed up. These commands are executed on all `Pods` in the component.

  * `backupPostHooks` \- (optional) an ordered list of hooks that are executed after volume backups have reached the UPLOADING phase. These commands are executed on all `Pods` in the component.

  * `volumeSelector` \- (optional) logic for matching a subset of volumes to backup.




This example creates a `ProtectedApplication` resource that quiesces the file system before backing up the logs volume and unquiesces after the backup:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: nginx
      namespace: sales
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: nginx
      components:
      - name: nginx-app
        resourceKind: Deployment
        resourceNames: ["nginx-deployment"]
        strategy:
          type: BackupAllRestoreAll
          backupAllRestoreAll:
            backupPreHooks:
            - name: freeze
              container: nginx
              command:
              - bash
              - "-c"
              - |
                # Add application logic to flush data to disk before snapshot
                # and freeze the application from further changes.
                echo "Freezing the application"
    
                # Return 0 on successful freeze of application, and non-zero
                # for errors
                exit 0
            backupPostHooks:
            - name: unfreeze
              container: nginx
              command:
              - bash
              - "-c"
              - |
                # Add application logic to unfreeze the application.
                echo "Unfreezing the application"
    
                # Return 0 on successful freeze of application, and non-zero
                # for errors
                exit 0
    

### Strategy: BackupOneAndRestoreAll

This strategy backs up one copy of a selected Pod. This single copy is the source for restoring all Pods during a restore. This method can help reduce storage cost and backup time. This strategy works in a [high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability) when a component is deployed with one primary `PersistentVolumeClaim` and multiple secondary `PersistentVolumeClaims`.

This strategy supports the following parameters:

  * `backupTargetName` \- (required) specifies which Deployment or StatefulSet that you want to use to back up the data. The best Pod to back up is automatically selected. In a high availability configuration, we recommend that you set this to one of your application replicas.

  * `backupPreHooks` \- (optional) an ordered list of hooks that are executed right before volumes are backed up. These commands are executed only on the selected backup `Pod`.

  * `backupPostHooks` \- (optional) an ordered list of hooks that are executed after volume backups have reached the UPLOADING phase. These commands are executed only on the selected backup `Pod`.

  * `volumeSelector` \- (optional) logic for matching a subset of volumes to backup.




If a component is configured with multiple Deployments or StatefulSets, all resources must have the same PersistentVolume structure, meaning they must follow these rules:

  * The number of `PersistentVolumeClaims` used by all Deployments or StatefulSets must be the same.
  * The purpose of `PersistentVolumeClaims` in the same index must be the same. For StatefulSets, the index is defined in the `volumeClaimTemplate`. For Deployments, the index is defined in `Volumes` and any non-persistent volumes are skipped.
  * If the application component consists of Deployments, each Deployment must have exactly one replica.



Given these considerations, multiple volume sets can be selected for backup, but only one volume from each volume set will be selected.

This example, assuming an architecture of one primary StatefulSet and a secondary StatefulSet, shows a backup of volumes of one Pod in secondary StatefulSet, and then a restore to all other volumes:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: mariadb
      namespace: mariadb
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: mariadb
      components:
      - name: mariadb
        resourceKind: StatefulSet
        resourceNames: ["mariadb-primary", "mariadb-secondary"]
        strategy:
          type: BackupOneRestoreAll
          backupOneRestoreAll:
            backupTargetName: mariadb-secondary
            backupPreHooks:
            - name: quiesce
              container: mariadb
              command: [...]
            backupPostHooks:
            - name: unquiesce
              container: mariadb
              command: [...]
    

### Strategy: DumpAndLoad

This strategy uses a dedicated volume for backup and restore processes and requires a dedicated `PersistentVolumeClaim` attached to a component that stores dump data.

This strategy supports the following parameters:

  * `dumpTarget` \- (required) specifies which Deployment or StatefulSet that you want to use to back up the data. The best Pod to back up is automatically selected. In a high availability configuration, we recommend that you set this to one of your application replicas.

  * `loadTarget` \- (required) specifies which Deployment or StatefulSet should be used to load the data. The best Pod to back up is automatically selected. The load target does not have to be the same as the dump target.

  * `dumpHooks` \- (required) an ordered list of hooks that are executed to populate the dedicated backup volume. These commands are only executed on the selected dump `Pod`.

  * `backupPostHooks` \- (optional) an ordered list of hooks that are executed after volume backups have reached the UPLOADING phase. These commands are executed only on the selected dump `Pod`.

  * `loadHooks` \- (required) an ordered list of hooks that are executed to load the data from the restored volume after the application starts. These commands are executed only on the selected load `Pod`.

  * `volumeSelector` \- (required) logic for matching a single volume to backup and restore (the "dump" volume). Though it must only match a single volume, you configure this the same way you do the subset of volumes to backup used by other strategies.




If the application consists of Deployments, each Deployment must have exactly one replica.

This example, assuming an architecture of one primary StatefulSet and a secondary StatefulSet with dedicated `PersistentVolumeClaims` for both primary and secondary StatefulSets, shows a `DumpAndLoad` strategy:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: mariadb
      namespace: mariadb
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: mariadb
      components:
      - name: mariadb-dump
        resourceKind: StatefulSet
        resourceNames: ["mariadb-primary", "mariadb-secondary"]
        strategy:
          type: DumpAndLoad
          dumpAndLoad:
            loadTarget: mariadb-primary
            dumpTarget: mariadb-secondary
            dumpHooks:
            - name: db_dump
              container: mariadb
              command:
              - bash
              - "-c"
              - |
                mysqldump -u root --all-databases > /backup/mysql_backup.dump
            loadHooks:
            - name: db_load
              container: mariadb
              command:
              - bash
              - "-c"
              - |
                mysql -u root < /backup/mysql_backup.sql
            volumeSelector:
              matchLabels:
                gkebackup.gke.io/backup: dedicated-volume
    

## Check if a `ProtectedApplication` is ready for backup

You can check whether a `ProtectedApplication` is ready for a backup by running the following command:
    
    
    kubectl describe protectedapplication APPLICATION_NAME
    

Replace `APPLICATION_NAME` with the name of your application.

If ready, the application description will show `Ready to backup` status as `true`, such as in this example:
    
    
    % kubectl describe protectedapplication nginx
    Name:         nginx
    Namespace:    default
    API Version:  gkebackup.gke.io/v1
    Kind:         ProtectedApplication
    Metadata:
      UID:               90c04a86-9dcd-48f2-abbf-5d84f979b2c2
    Spec:
      Components:
        Name:           nginx
        Resource Kind:  Deployment
        Resource Names:
          nginx
        Strategy:
          Backup All Restore All:
            Backup Pre Hooks:
              Command:
                 /sbin/fsfreeze
                 -f
                 /var/log/nginx
              Container:         nginx
              Name:              freeze
            Backup Post Hooks:
              Command:
                 /sbin/fsfreeze
                 -u
                 /var/log/nginx
              Container:         nginx
              Name:              unfreeze
          Type:                  BackupAllRestoreAll
      Resource Selection:
        Selector:
          Match Labels:
            app:        nginx
        Type:           Selector
    ** Status:
      Ready To Backup:  true **
    Events:             <none>
    

## What's next

  * Learn more about [planning a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
