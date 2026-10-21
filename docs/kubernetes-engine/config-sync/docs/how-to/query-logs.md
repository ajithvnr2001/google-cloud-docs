---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/query-logs/
title: Query Config Sync logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:24.261799+00:00
---

# Query Config Sync logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/query-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Query Config Sync logs Stay organized with collections  Save and categorize content based on your preferences. 

This page contains queries that you can use with [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). You can use these queries to retrieve, view, and analyze log data. These logs can contain valuable historical data that isn't captured by `nomos bugreport` when the operator or reconciler Pods are restarted.

To find the most important logs, sort the issues by severity and then adjust the timestamp to control the time window.

Query/filter name | Expression | Notes  
---|---|---  
Check the reconciler-manager logs | 
    
    
    resource.type="k8s_container"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.namespace_name="config-management-system"
    resource.labels.container_name="reconciler-manager"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|   
Check the reconciler logs for a namespace repository | 
    
    
    resource.type="k8s_container"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.namespace_name="config-management-system"
    resource.labels.container_name="reconciler"
    resource.labels.pod_name:"ns-reconciler-NAMESPACE"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|  To view the `git-sync` logs, change `resource.laels.container_name` to `git-sync`. To view the root reconciler logs, change `resource.labels.pod_name` to `root-reconciler`.   
Check if a cluster was upgraded in a period | 
    
    
    resource.type="gke_cluster"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.location="LOCATION"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|  If the cluster you queried wasn't upgraded, the result is empty.   
Check if reconciler Pods failed to start | 
    
    
    resource.type="k8s_pod"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.location="LOCATION"
    resource.labels.pod_name:"ns-reconciler-NAMESPACE"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|  If you see an error for Config Sync related Pods, that means those Pods weren't able to start at the associated timestamp.   
Check the operation of a ConfigMap | 
    
    
    resource.type="k8s_cluster"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.location="LOCATION"
    protoPayload.methodName:"io.k8s.core.v1.configmaps"
    protoPayload.resourceName:"core/v1/namespaces/config-management-system/configmaps/ns-reconciler-cap-logging-service"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|   
Check the operation of a RepoSync | 
    
    
    resource.type="k8s_cluster"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.location="LOCATION"
    protoPayload.methodName:"reposyncs"
    protoPayload.resourceName:"namespaces/cap-logging-service/reposyncs"
    timestamp >= "START_TIME"
    timestamp <= "STOP_TIME"
            

|   
List all Git revisions synced by `git-sync` | 
    
    
    resource.type="k8s_container"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.location="LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.namespace_name="config-management-system"
    resource.labels.pod_name:"git-importer-" severity>=DEFAULT
    "adding worktree"
            

|   
  
Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `CLUSTER_NAME`: The name of the cluster that you want to query.
  * `START_TIME`: Set the time that you want to start collecting logs. You must use the following format when writing a query with a timestamp: YYYY-MM-DDT00:00:00Z.
  * `STOP_TIME`: Set the time that you want to stop collecting logs. You must use the following format when writing a query with a timestamp: YYYY-MM-DDT00:00:00Z.
  * `NAMESPACE`: The namespace that you created your namespace repository in.
  * `LOCATION`: The location that you created your cluster in.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
