---
url: https://docs.cloud.google.com/filestore/docs/gke-access-issues/
title: Troubleshoot file share access from GKE clusters \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:08.525890+00:00
---

# Troubleshoot file share access from GKE clusters  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/gke-access-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot file share access from GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address issues you might encounter while using Filestore with GKE.

## Unable to access file share from GKE clusters

For more troubleshooting information relating to Kubernetes or Google Kubernetes Engine, you can also refer to the official [Kubernetes troubleshooting guide](https://kubernetes.io/docs/tasks/debug-application-cluster/troubleshooting/) and the [GKE troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

### Error: Output: mount.nfs: access denied by server while mounting x.x.x.x:/file-share-name

Make sure that the values of the PV `spec.nfs.path` and `spec.nfs.server` match with the name of the file share and the IP address of the Filestore instance, respectively.

**Example:**

If your file share is named `vol1` and the IP address of the Filestore instance is `10.0.0.2`, the PV `spec.nfs.path` and `spec.nfs.server` must match those values:
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
     name: fileserver
    spec:
     capacity:
       storage: 2T
     accessModes:
     - ReadWriteMany
     nfs:
       **path : /vol1**
       **server : 10.0.0.2**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
