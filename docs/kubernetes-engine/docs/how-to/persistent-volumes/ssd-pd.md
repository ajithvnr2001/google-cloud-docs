---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/ssd-pd/
title: Using SSD persistent disks \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:02.490040+00:00
---

# Using SSD persistent disks  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/ssd-pd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Using SSD persistent disks Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to create dynamic [PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) resources that are backed by [SSD persistent disks](https://docs.cloud.google.com/compute/docs/disks).

## SSD persistent disks

By default, [dynamically provisioned PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) use the [default `StorageClass`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses) and are backed by standard hard disks. If you need faster SSDs, you can use the `premium-rwo` storage class from the [Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) to provision your volumes. This can be done by setting the `storageClassName` field to `premium-rwo` in your `PersistentVolumeClaim` as shown in the following example:
    
    
    # ssd-claim.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-volume
    spec:
      storageClassName: premium-rwo
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
    

To create the `my-volume` PersistentVolumeClaim object, use the following `kubectl apply` command:
    
    
    kubectl apply -f ssd-claim.yaml
    

When you create this `PersistentVolumeClaim` object with `kubectl apply`, Kubernetes dynamically creates a corresponding `PersistentVolume` object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
