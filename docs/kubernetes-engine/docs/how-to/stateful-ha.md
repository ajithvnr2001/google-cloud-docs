---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha/
title: Increase stateful app availability with Stateful HA Operator \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:14.651534+00:00
---

# Increase stateful app availability with Stateful HA Operator  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Increase stateful app availability with Stateful HA Operator Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Stateful High Availability (HA) Operator allows you to use GKE's built-in integration with [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk) to automate and control the speed of [StatefulSet](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) Pod failover. During failover, the operator automatically handles detecting node failure, detaching a volume from a failed node, and ensuring safe volume attachment to the failover node.

## Why use Stateful HA Operator

A common stateful architecture for achieving high availability uses regional Persistent Disks as the storage layer. These disks provide synchronous replication of data between two zones in a region. During node or zonal network failures, this architecture lets your workloads _failover_ (by [force-attaching](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--force-attach)) replicas to storage on another node in a different zone.

Stateful HA Operator lets you make the following optimizations:

  * **Improve recovery time of single-replica applications** : If you use only one replica, you can use Stateful HA Operator and swap out zonal storage for regional storage when your application is provisioned, to increase data durability and availability in the event of a node failure.
  * **Reduce cross-zone networking costs** : Replicating data across multiple zones can be costly for high throughput applications. You can use Stateful HA Operator to run your application in a single zone, while maintaining a failover path to an alternate zone that fits your application's SLA.



### Limitations

  * The [gcePersistentDisk](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk) volume type is not supported. Use a `PersistentVolume` that uses the [persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).
  * With a single-replica Stateful HA Operator architecture, GKE persists your data in two zones through regional Persistent Disk but data is only accessible while your application replica is healthy. During a failover, your application will be temporarily unavailable while your replica reschedules to a new healthy node. If your application has a very low [recovery time objective](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) (RTO), we recommend using a multi-replica approach.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

  * When you use Stateful HA Operator, it automatically configures your linked StatefulSet to use regional Persistent Disks. However, you are responsible for ensuring that Pods are configured to use these disks, and capable of running in all zones associated with the underlying storage.
  * Make sure your application runs on [machine shapes](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#restrictions) that regional Persistent Disk supports: E2, N1, N2, N2D.
  * Make sure that the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) is enabled. The Persistent Disk CSI driver is enabled by default on new Autopilot and Standard clusters and cannot be disabled or edited when using Autopilot. If you need to manually add the Persistent Disk CSI driver from your cluster, see [Enabling the Persistent Disk CSI driver on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster).
  * If you are using a custom StorageClass, configure the Persistent Disk CSI driver with the `pd.csi.storage.gke.io` provisioner and these parameters: 
    * `availability-class: regional-hard-failover`
    * `replication-type: regional-pd`



## Set up and use Stateful HA Operator

Follow these steps to set up Stateful HA Operator for your stateful workloads:

  1. Enable the `StatefulHA` add-on.
  2. Install a HighAvailabilityApplication resource.
  3. Install a StatefulSet.
  4. Inspect the HighAvailabilityApplication resource.



### Enable the `StatefulHA` add-on

To use the Stateful HA Operator, the `StatefulHA` add-on must be enabled on your cluster.

  * **Autopilot clusters** : GKE automatically enables the `StatefulHA` add-on at cluster creation. If you want to use Stateful HA Operator on an existing workload, you need to manually enable the Compute Engine Persistent Disk CSI Driver. For more information, see [Enable the Persistent Disk CSI driver on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster).

  * **Standard clusters** :

    * New cluster creation: Follow the gcloud CLI instructions to [create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) and add the following flag: `--addons=StatefulHA=ENABLED`.
    * Existing Standard cluster: Follow the gcloud CLI instructions to [update a Standard cluster's settings](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update), and use the following flag to enable the add-on: `--update-addons=StatefulHA=ENABLED``.



GKE automatically installs a StorageClass named `standard-rwo-regional` for you when the add-on is enabled.

### Install a HighAvailabilityApplication resource

`HighAvailabilityApplication` is a Kubernetes resource that simplifies StatefulSet settings and increases Pod availability on GKE. Stateful HA Operator reconciles `HighAvailabilityApplication` resources on GKE.

In the `HighAvailabilityApplication` specification, you must set `HighAvailabilityApplication.spec.resourceSelection.resourceKind` to `StatefulSet`.

To learn how to configure the HighAvailability resource, refer to the `HighAvailabilityApplication` [reference documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/highavailabilityapplication).

See the following example for PostgreSQL:

  1. Save the following manifest in a file named `stateful-ha-example-resource.yaml`:
         
         kind: HighAvailabilityApplication
         apiVersion: ha.gke.io/v1
         metadata:
           name: APP_NAME
           namespace: APP_NAMESPACE
         spec:
           resourceSelection:
             resourceKind: StatefulSet
           policy:
             storageSettings:
               requireRegionalStorage: true
             failoverSettings:
               forceDeleteStrategy: AfterNodeUnreachable
               afterNodeUnreachable:
                 afterNodeUnreachableSeconds: 20
         

Replace the following:

     * APP_NAME: the name of an application in your cluster that you want to protect. This name must be shared by both the HighAvailabilityApplication and StatefulSet.
     * APP_NAMESPACE: the application namespace. This namespace must be shared by both the HighAvailabilityApplication and StatefulSet being protected.

In this example:

     * `HighAvailabilityApplication.spec.policy.storageSettings.requireRegionalSettings` is set to `true`. This enforces regional storage.
     * `HighAvailabilityApplication.spec.policy.failoverSettings` is set to `AfterNodeUnreachable`. This determines how force delete is triggered on node failure.
     * `HighAvailabilityApplication.spec.policy.failoverSettings.afterNodeUnreachable` is set to 20. This is the timeout to force delete a Pod after the node it's running in is marked as unreachable.
  2. Create the resource. The `HighAvailabilityApplication` resource identifies a StatefulSet with a matching namespace and name.
         
         kubectl apply -f stateful-ha-example-resource.yaml
         




### Install a StatefulSet

Install a StatefulSet. For example, you can install a PostgreSQL StatefulSet using [Helm](https://helm.sh/) (Helm comes pre-installed with [Cloud Shell](https://docs.cloud.google.com/shell)):
    
    
    helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql \
      --namespace=APP_NAMESPACE \
      --set fullnameOverride=APP_NAME
    

The `HighAvailabilityApplication` resource automatically modifies the StatefulSet's StorageClass to `standard-rwo-regional`, which uses regional Persistent Disk.

### Inspect the HighAvailabilityApplication resource

Run the following command to verify that the example application has automated failover enabled:
    
    
    kubectl describe highavailabilityapplication APP_NAME
    

The output should appear similar to the following:
    
    
    Status:
    Conditions:
      Last Transition Time:  2023-08-09T23:59:52Z
      Message:               Application is protected
      Observed Generation:   1
      Reason:                ApplicationProtected
      Status:                True
      Type:                  Protected
    

## Use existing Persistent Disks

If you are using an existing Persistent Disk and a statically defined PersistentVolume, configure the PersistentVolume with `force-attach: true` in `.spec.csi.volumeAttributes`. For example:
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: PV_NAME
    spec:
      storageClassName: "STORAGE_CLASS_NAME"
      capacity:
        storage: DISK_SIZE
      accessModes:
        - ReadWriteOnce
      claimRef:
        name: PV_CLAIM_NAME
        namespace: default
      csi:
        driver: pd.csi.storage.gke.io
        volumeHandle: DISK_ID
        fsType: FS_TYPE
        **volumeAttributes :
          force-attach: ¨true¨**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
