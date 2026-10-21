---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps/
title: Deploying a stateful application \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:21:48.888497+00:00
---

# Deploying a stateful application  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploying a stateful application Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to deploy a stateful application using Google Kubernetes Engine (GKE).

## Overview

Stateful applications save data to [persistent disk storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) for use by the server, by clients, and by other applications. An example of a stateful application is a database or key-value store to which data is saved and retrieved by other applications.

Persistent storage can be [dynamically provisioned](https://kubernetes.io/docs/tutorials/object-management-kubectl/imperative-object-management-configuration/), so that the underlying volumes are created on demand. In Kubernetes, you configure dynamic provisioning by creating a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). In GKE, a default StorageClass allows you to dynamically provision [Compute Engine](https://docs.cloud.google.com/compute) persistent disks.

Kubernetes uses the [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) controller to deploy stateful applications as StatefulSet objects. Pods in StatefulSets are not interchangeable: each Pod has a unique identifier that is maintained no matter where it is scheduled.

Stateful applications are different from [stateless applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps), in which client data is not saved to the server between sessions.

You can learn more about [persistent storage in multi-zonal and regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters#pd).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure your containerized application is stored in an image registry, such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).



You can follow the [quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster), to enable the GKE API, create a cluster, and learn more about GKE.

## Requesting persistent storage in a StatefulSet

Applications can request persistent storage with a [PersistentVolumeClaim](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).

Typically, you must create PersistentVolumeClaim objects in addition to creating the Pod. However, StatefulSet objects include a `volumeClaimTemplates` array, which automatically generates the PersistentVolumeClaim objects. Each StatefulSet replica gets its own PersistentVolumeClaim object.

You can also [use a preexisting disk in a StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd#using_a_preexisting_disk_in_a_statefulset).

## Creating a StatefulSet

To create a StatefulSet resource, use the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command.

The `kubectl apply` command uses manifest files to create, update, and delete resources in your cluster. This is a [declarative method](https://kubernetes.io/docs/tutorials/object-management-kubectl/imperative-object-management-configuration/) of object configuration. This method retains writes made to live objects without merging the changes back into the object configuration files.

### Linux

The following manifest file is an example of a Headless Service and the StatefulSet it governs:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: SERVICE_NAME
      labels:
        app: APP_NAME
    spec:
      ports:
      - port: 80
        name: PORT_NAME
      clusterIP: None
      selector:
        app: APP_NAME
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: STATEFULSET_NAME
    spec:
      selector:
        matchLabels:
          # Selects Pods with this label.
          app: APP_NAME
      # Headless Service for network identity.
      serviceName: "SERVICE_NAME"
      replicas: 3
      updateStrategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: APP_NAME
        spec:
          containers:
          - name: CONTAINER_NAME
            image: IMAGE
            ports:
            - containerPort: 80
              name: PORT_NAME
            volumeMounts:
            - name: PVC_NAME
              mountPath: MOUNT_PATH
      volumeClaimTemplates:
      - metadata:
          name: PVC_NAME
          annotations:
            KEY: VALUE
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
    

Replace the following:

  * `STATEFULSET_NAME`: the name of the StatefulSet, for example, `web`.
  * `SERVICE_NAME`: the name of the Service, for example, `nginx`.
  * `APP_NAME`: the name of the application run in the Pods, for example, `nginx`.
  * `CONTAINER_NAME`: the name of the containers in the Pods, for example, `nginx`.
  * `IMAGE`: your container image, for example, `nginx:stable`.
  * `PORT_NAME`: the name of the port opened by the StatefulSet, for example, `web`.
  * `PVC_NAME`: the name of the PersistentVolumeClaim, for example, `www`.
  * `MOUNT_PATH`: the path in the container where storage is mounted, for example, `/usr/share/nginx/html`.
  * `KEY` and `VALUE`: an annotation key-value pair to apply to the PersistentVolumeClaim metadata. You can use annotations to attach arbitrary non-identifying metadata to objects that can be retrieved by clients such as tools and libraries. To learn more, see [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).



In this file, the `kind` field specifies that a StatefulSet object should be created with the specifications defined in the file. This example StatefulSet produces three replicated Pods, and opens port 80 for exposing the StatefulSet to the internet.

### Windows

When using [clusters with Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows), you must create a StorageClass because the default StorageClass uses `ext4` as the file system type, which only works for Linux containers. If you are using a Compute Engine persistent disk, you must use `NTFS` as the file storage type as shown in the following example:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      # Defines a name for this StorageClass.
      name: STORAGECLASS_NAME
    parameters:
      # Specifies the type of Google Compute Engine persistent disk.
      type: pd-standard
      # Uses NTFS file system, which is crucial for Windows nodes
      fstype: NTFS
    # The provisioner for Google Compute Engine persistent disks.
    provisioner: kubernetes.io/gce-pd
    # Specifies that the PersistentVolume will be deleted if the PersistentVolumeClaim is deleted.
    reclaimPolicy: Delete
    # Delays volume binding until a Pod using the PVC is scheduled.
    volumeBindingMode: WaitForFirstConsumer
    

The following StatefulSet manifest uses the StorageClass defined above. It creates four PersistentVolume and PersistentVolumeClaim pairs to represent four Compute Engine persistent disks. Each Pod in the StatefulSet consumes one persistent disk.

To ensure your Pods are correctly scheduled onto Windows Server nodes, you must add a node selector to your Pod specification.
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: STATEFULSET_NAME
    spec:
      replicas: 4
      selector:
        matchLabels:
          # Selects Pods with this label.
          app: APP_NAME
      template:
        metadata:
          labels:
            # Labels applied to the Pods created by the StatefulSet.
            app: APP_NAME
          name: CONTAINER_NAME
        spec:
          nodeSelector:
            # Ensures Pods are scheduled on Windows nodes.
            kubernetes.io/os: windows
          containers:
          - name: CONTAINER_NAME
            image: IMAGE
            ports:
            - containerPort: 80
              name: PORT_NAME
            volumeMounts:
            - name: PVC_NAME
              mountPath: MOUNT_PATH
      volumeClaimTemplates:
      - metadata:
          name: PVC_NAME
        spec:
          # Specifies the StorageClass to use, which is crucial for Windows nodes.
          storageClassName: STORAGECLASS_NAME
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
    

Replace the following:

  * `STATEFULSET_NAME`: the name of the StatefulSet, for example, `web-windows`.
  * `APP_NAME`: the name of the application run in the Pods, for example, `iis`.
  * `CONTAINER_NAME`: the name of the containers in the Pods, for example, `iis`.
  * `IMAGE`: your container image, for example, `mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019`.
  * `PORT_NAME`: the name of the port opened by the StatefulSet, for example, `http`.
  * `PVC_NAME`: the name of the PersistentVolumeClaim, for example, `iis-state`.
  * `MOUNT_PATH`: the path in the container where storage is mounted, for example, `C:\mnt\state`.
  * `STORAGECLASS_NAME`: the name of the StorageClass, for example, `my-storage-class`.



To create a StatefulSet resource, run the following command replacing `STATEFULSET_FILE` with the manifest file name:
    
    
    kubectl apply -f STATEFULSET_FILE
    

You can also use `kubectl apply -f DIRECTORY/` to create all objects (except existing ones) defined in configuration files stored in a directory.

**Note:** `kubectl apply` fails if you do not have an active cluster.

## Inspecting a StatefulSet

### kubectl

To inspect the StatefulSet, run the following command:
    
    
    kubectl get statefulset STATEFULSET_NAME -o yaml
    

This command displays the live configuration of the StatefulSet resource in YAML format.

To list the Pods created by the StatefulSet, run the following command:
    
    
    kubectl get pods -l app=APP_NAME
    

In this command, the `-l` flag instructs `kubectl` to get all Pods _labeled_ for the `APP_NAME`.

The output is similar to the following:
    
    
    NAME                                READY     STATUS    RESTARTS   AGE
    pod-name                            1/1       Running   0          1m
    pod-name                            1/1       Running   0          1m
    

To get detailed information about the StatefulSet, run the following command:
    
    
    kubectl describe statefulset STATEFULSET_NAME
    

To get information about a specific Pod, run the following command:
    
    
    kubectl describe pod POD_NAME
    

To list the PersistentVolumeClaim objects that were created, run the following command:
    
    
    kubectl get pvc
    

The output is similar to the following:
    
    
    NAME                            STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS    AGE
    STATEFULSET_NAME-PVC_NAME-0     Bound     pvc-bdff4e1e-183e-11e8-bf6d-42010a800002   1G         RWO            standard        9s
    STATEFULSET_NAME-PVC_NAME-1     Bound     pvc-bdff4e1e-183e-11e8-bf6d-42010a800003   1G         RWO            standard        9s
    STATEFULSET_NAME-PVC_NAME-2     Bound     pvc-bdff4e1e-183e-11e8-bf6d-42010a800004   1G         RWO            standard        9s
    

To get information about a specific PersistentVolumeClaim, run the following command:
    
    
    kubectl describe pvc STATEFULSET_NAME-PVC_NAME-0
    

To get information about a specific PersistentVolume, run the following command:
    
    
    kubectl describe pv PV_NAME
    

### Console

To inspect a StatefulSet, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the StatefulSet you want to inspect.

  3. On the **Stateful Set details** page, do any of the following:

     * Click the **Revision History** tab to see the StatefulSet's revision history.
     * Click the **Events** tab to see all events related to the StatefulSet.
     * Click the **Logs** tab to see container logs for the StatefulSet.
     * Click the **YAML** tab to see, copy, or download the configuration YAML for the StatefulSet.



## Updating a StatefulSet

There are multiple ways of updating StatefulSets. The common, declarative method is `kubectl apply`. To update the StatefulSet directly from your shell or in a preferred editor, you can use `kubectl edit`. You can also use the YAML editor from the GKE Workloads menu in the Google Cloud console.

You can roll out updates to the [Pods specification](https://kubernetes.io/docs/tutorials/object-management-kubectl/imperative-object-management-configuration/) for a StatefulSet resource, such as its image, resource usage/requests, or configuration.

### kubectl apply

You can update the StatefulSet by _applying_ a new or updated manifest file. This is useful for making various changes to your StatefulSet, such as when scaling or for specifying a new version of your application.

**Note:** To update a resource with `kubectl apply`, the resource would need to have been created using either `kubectl apply` or `kubectl create --save-config`.

To update a StatefulSet, run the following command:
    
    
    kubectl apply -f STATEFULSET_FILE
    

Replace `STATEFULSET_FILE` with the updated manifest file.

The `kubectl apply` command applies a manifest file to a resource. If the specified resource does not exist, it is created by the command.

For more information about `kubectl apply`, see the [`kubectl` reference documentation](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply).

### Console

To edit the live configuration of a StatefulSet, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the StatefulSet you want to modify.

  3. Click _edit_ **Edit**.

  4. Change the configuration YAML as desired.

  5. Click **Save**.




**Note:** While it is possible to specify a different PersistentVolume, it is not possible to update existing PersistentVolume resources.

### Inspecting update rollout

To inspect the rollout of the StatefulSet, run the following command:
    
    
    kubectl rollout status statefulset STATEFULSET_NAME
    

To see the StatefulSet's rollout history, run the following command:
    
    
    kubectl rollout history statefulset STATEFULSET_NAME
    

To undo a rollout, run the following command:
    
    
    kubectl rollout undo statefulset STATEFULSET_NAME
    

### Update strategies

StatefulSet’s `updateStrategy` field allows you to configure and disable automated rolling updates for containers, labels, resource requests, limits, and annotations for the Pods in a StatefulSet.

You can learn more about [Update Strategies](https://kubernetes.io/docs/tutorials/object-management-kubectl/imperative-object-management-configuration/) for StatefulSets in the Kubernetes documentation.

## Scaling a StatefulSet

### kubectl

The `kubectl scale` command can be used at any time to scale your StatefulSet.

To manually scale a StatefulSet, run the following command:
    
    
    kubectl scale statefulset STATEFULSET_NAME --replicas NUMBER_OF_REPLICAS
    

Replace `NUMBER_OF_REPLICAS` with the desired number of replicated Pods.

### Console

To scale a StatefulSet, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, click the name of the StatefulSet you want to modify.

  3. Click _list_ **Actions > Scale > Edit replicas**.

  4. Enter the new number of **Replicas** for the StatefulSet.

  5. Click **Scale**.




## Deleting a StatefulSet

### kubectl

To delete a StatefulSet, run the following command:
    
    
    kubectl delete statefulset STATEFULSET_NAME
    

### Console

To delete a StatefulSet, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the workloads list, select one or more StatefulSets you want to delete.

  3. Click _delete_ **Delete**.

  4. When prompted to confirm, click **Delete**.




## What's next

  * [Learn how to deploy a MySQL cluster on GKE for high availability](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql)
  * [Learn about deploying stateless applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps).
  * [Take a tutorial about upgrading a cluster running a stateful workload](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/upgrading-stateful-workload).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
