---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields/
title: ConfigManagement fields \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:18.909632+00:00
---

# ConfigManagement fields  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference)



Send feedback 

#  ConfigManagement fields Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the different fields that you can set in your `ConfigManagement` object. You can use this object when you are configuring Config Sync using `kubectl` commands.

**Note:** The gcloud CLI apply command uses a [different file format](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields) than the `ConfigManagement` object.**Caution:** Don't change configuration values outside the `spec` field.

## Configuration for Config Sync features

Key | Description  
---|---  
`spec.enableMultiRepo` | If `true`, enables the RootSync and RepoSync APIs. These APIs provide you with additional [Config Sync features](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields), such as syncing from multiple repositories. and [syncing Kustomize and Helm configurations](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-helm). Defaults to `false`.  
`spec.preventDrift` | If `true`, enables the Config Sync admission webhook to [prevent drifts](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) by rejecting conflicting changes from being pushed to live clusters. Defaults to `false`. Config Sync always remediates drifts no matter the value of this field.  
  
## Configuration for behavior of the ConfigManagement object

Key | Description  
---|---  
`spec.clusterName` | The user-defined name for the cluster used by [ClusterSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#configure_a_subset_of_clusters) to group clusters together. Unique within an Config Sync installation. You cannot configure this field in the Google Cloud console.  
  
## Example ConfigManagement object
    
    
    apiVersion: configmanagement.gke.io/v1
    kind: ConfigManagement
    metadata:
      name: config-management
    spec:
      clusterName: my-cluster
      enableMultiRepo: true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
