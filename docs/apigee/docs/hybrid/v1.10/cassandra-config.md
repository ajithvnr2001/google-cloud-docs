---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-config/
title: StorageClass configuration \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:19:09.767455+00:00
---

# StorageClass configuration  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  StorageClass configuration Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-config.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-config.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-config.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-config.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-config.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-config.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-config.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-config.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-config.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-config.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-config.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-config.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-config.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-config.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-config.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-config.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-config.html)



The Cassandra database uses [ dynamically created](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic) persistent volumes to store data. For proper database functioning, Apigee requires you to configure a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes) definition that is backed by a solid-state drive (SSD). 

If you do not currently have SSD configured for Cassandra, this topic explains how to create a new StorageClass that uses SSD and make it the default class. When Cassandra starts, it will use this default StorageClass. 

**KEY POINT:** Apigee requires the use of SSD for Cassandra. 

The steps outlined in this topic for StorageClass configuration are only applicable to a _new_ Cassandra installation. If you already have a Cassandra class installed, you must decommission the existing cluster in order to configure the StorageClass definition. Changes to the StorageClass definition of an existing Cassandra cluster after installation are not supported.

Apigee recommends deploying hybrid in [two or more regions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/multi-region), in order to decommission and re-install one region while preserving data in the secondary region. Alternatively, you can use a [non-CSI hybrid backup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview#how-to-take-backups) to restore data in a single-region installation, after decommissioning and configuring the required StorageClass definition.

##  Change the default StorageClass 

The following steps explain how to create a StorageClass and make it the default class. For more information, see [ Change the default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) in the Kubernetes documentation. 

  1. Get the name of the current default StorageClass: 
         
         kubectl get sc

For example: 
         
         kubectl get sc
             NAME                    PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
             premium-rwo             pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
             standard                kubernetes.io/gce-pd    Delete          Immediate              true                   15h
             **standard-rwo (default)  pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h**
           

  2. Describe the StorageClass named `standard-rwo`. Note that its type is `pd-balanced`: 
         
         kubectl describe sc standard-rwo

For example: 
         
         kubectl describe sc standard-rwo
         
         Name:                  standard-rwo
         IsDefaultClass:        Yes
         Annotations:           components.gke.io/layer=addon,storageclass.kubernetes.io/is-default-class=false
         Provisioner:           pd.csi.storage.gke.io
         Parameters:            type=pd-balanced
         AllowVolumeExpansion:  True
         MountOptions:          <none>
         ReclaimPolicy:         Delete
         VolumeBindingMode:     WaitForFirstConsumer
         Events:                <none>

  3. Create a new file called `storageclass.yaml`.
  4. Add this code to the file. Note that the name of the new class is `apigee-sc`. You can use any name you like. Also, note that the storage type is `pd-ssd`: 
         
         ---
         kind: StorageClass
         apiVersion: storage.k8s.io/v1
         metadata:
           name: "apigee-sc"
         provisioner: pd.csi.storage.gke.io
         parameters:
           type: pd-ssd
           replication-type: none
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true

  5. Apply the new StorageClass to your Kubernetes cluster: 
         
         kubectl apply -f storageclass.yaml

  6. Execute the following two commands to change the default StorageClass: 
         
         kubectl patch storageclass standard-rwo \
           -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
         
         kubectl patch storageclass apigee-sc \
           -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

  7. Execute this command to verify that the new default StorageClass is called `apigee-sc`: 
         
         kubectl get sc

For example: 
         
         NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
             **apigee-sc (default)   pd.csi.storage.gke.io    Delete          WaitForFirstConsumer   true                   14h**
             premium-rwo           pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
             standard              kubernetes.io/gce-pd    Delete          Immediate              true                   15h
             standard-rwo          pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
           

  8. Describe both the StorageClass to verify the value of **IsDefaultClass**. 
         
         kubectl describe sc apigee-sc
         
         Name:            apigee-sc
             IsDefaultClass:  Yes
             Annotations:     kubectl.kubernetes.io/last-applied-configuration={"allowVolumeExpansion":true,"apiVersion":"storage.k8s.io/v1","kind":"StorageClass","metadata":{"annotations":{},"name":"apigee-sc"},"parameters":{"replication-type":"none","type":"pd-ssd"},"provisioner":"pd.csi.storage.gke.io","volumeBindingMode":"WaitForFirstConsumer"},storageclass.kubernetes.io/is-default-class=true
             Provisioner:           pd.csi.storage.gke.io
             Parameters:            replication-type=none,type=pd-ssd
             AllowVolumeExpansion:  True
             MountOptions:          
             ReclaimPolicy:         Delete
             VolumeBindingMode:     WaitForFirstConsumer
             Events:                
         
         kubectl describe sc standard-rwo
         
         Name:                  standard-rwo
             IsDefaultClass:        No
             Annotations:           components.gke.io/layer=addon,storageclass.kubernetes.io/is-default-class=false
             Provisioner:           pd.csi.storage.gke.io
             Parameters:            type=pd-balanced
             AllowVolumeExpansion:  True
             MountOptions:          
             ReclaimPolicy:         Delete
             VolumeBindingMode:     WaitForFirstConsumer
             Events:                




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
