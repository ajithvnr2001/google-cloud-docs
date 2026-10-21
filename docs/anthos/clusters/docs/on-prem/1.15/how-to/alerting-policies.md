---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/alerting-policies/
title: Creating alerting policies \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:01.944151+00:00
---

# Creating alerting policies  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/alerting-policies/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Creating alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/alerting-policies)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/alerting-policies)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows how to create alerting policies for Google Distributed Cloud clusters.

## Before you begin

You must have the following permissions to create alerting policies:

  * monitoring.alertPolicies.create
  * monitoring.alertPolicies.delete
  * monitoring.alertPolicies.update



You'll have these permissions if you have any one of the following [roles](https://docs.cloud.google.com/monitoring/access-control#predefined_roles):

  * monitoring.alertPolicyEditor
  * monitoring.editor
  * Project editor
  * Project owner



To check your roles, go to the [IAM page](https://console.cloud.google.com/iam-admin/iam) in the Google Cloud console.

## Creating a policy: admin cluster API server unavailable

In this exercise, you create an alerting policy for Kubernetes API servers of admin clusters. With this policy in place, you can arrange to be notified whenever the API server of an admin cluster is unavailable.

  1. Download the policy configuration file: [admin-cluster-apiserver-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-apiserver-unavailable.json).

  2. Create the policy:
         
         gcloud alpha monitoring policies create --policy-from-file=POLICY_CONFIG
         

Replace POLICY_CONFIG with the path of the configuration file you just downloaded.

  3. View your alerting policies:

### Console

     1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

     2. On the left, select **Alerting**.

     3. Under **Policies** , you can see a list of your alerting policies.

In the list, select **GKE on-prem admin cluster API server unavailable (critical)** to see details about your new policy. Under **Conditions** , you can see a description of the policy. For example:
            
            Policy violates when ANY condition is met
            
            GKE on-prem admin cluster API server uptime is absent
            
            GKE on-prem admin cluster API server uptime is less than 99.99% per minute
            

### gcloud
    
    gcloud alpha monitoring policies list

The output shows detailed information about the policy. For example:
    
    combiner: OR
    conditions:
    - conditionAbsent:
        aggregations:
        - alignmentPeriod: 60s
          crossSeriesReducer: REDUCE_MEAN
          groupByFields:
          - resource.label.project_id
          - resource.label.location
          - resource.label.cluster_name
          - resource.label.namespace_name
          - resource.label.container_name
          perSeriesAligner: ALIGN_MAX
        duration: 300s
        filter: resource.type = "k8s_container" AND resource.labels.namespace_name = "kube-system"
          AND metric.type = "kubernetes.io/anthos/container/uptime" AND resource.label."container_name"=monitoring.regex.full_match("kube-apiserver")
        trigger:
          count: 1
      displayName: GKE on-prem admin cluster API server uptime is absent
      name: projects/…/alertPolicies/17065318077071152828/conditions/17065318077071154437
    - conditionThreshold:
        aggregations:
        - alignmentPeriod: 120s
          crossSeriesReducer: REDUCE_MEAN
          groupByFields:
          - resource.label.project_id
          - resource.label.location
          - resource.label.cluster_name
          - resource.label.namespace_name
          - resource.label.container_name
          perSeriesAligner: ALIGN_MAX
        comparison: COMPARISON_LT
        duration: 300s
        filter: resource.type = "k8s_container" AND resource.labels.namespace_name = "kube-system"
          AND metric.type = "kubernetes.io/anthos/container/uptime" AND resource.label."container_name"=monitoring.regex.full_match("kube-apiserver")
        thresholdValue: 119.0
        trigger:
          count: 1
      displayName: GKE on-prem admin cluster API server uptime is less than 99.99% per
        minute
      name: projects/…/alertPolicies/17065318077071152828/conditions/17065318077071151950
    creationRecord:
      mutateTime: …
      mutatedBy: …
    displayName: GKE on-prem admin cluster API server unavailable (critical)
    enabled: true
    mutationRecord:
      mutateTime: …
      mutatedBy: …
    name: projects/xxxxxx/alertPolicies/17065318077071152828
    




## Creating additional alerting policies

This section provides descriptions and configuration files for a set of recommended alerting policies.

To create a policy, follow the same steps that you used in the preceding exercise:

  1. Click the link in the right column to download the configuration file.

  2. Run `gcloud alpha monitoring policies create` to create the policy.




### Admin cluster control plane components availability

Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
GKE on-prem admin cluster API server unavailable (critical) | Admin cluster API server is not up or uptime is less than 99.99% per minute | [admin-cluster-apiserver-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-apiserver-unavailable.json)  
GKE on-prem admin cluster scheduler unavailable (critical) | Admin cluster scheduler is not up or uptime is less than 99.99% per minute | [admin-cluster-scheduler-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-scheduler-unavailable.json)  
GKE on-prem admin cluster controller manager unavailable (critical) | Admin cluster controller manager is not up or uptime is less than 99.99% per minute | [admin-cluster-controller-manager-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-controller-manager-unavailable.json)  
GKE on-prem admin cluster etcd unavailable (critical) | Admin cluster etcd is not up or uptime is less than 99.99% per minute | [admin-cluster-etcd-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-etcd-unavailable.json)  
  
### User cluster control plane components availability

The user cluster control plane alerts are based on metrics. For most cluster metrics, the `cluster_name` field is the name of the cluster itself. But for user cluster control plane metrics, the `cluster_name` field is the name of the admin cluster, and the `namespace_name` field is the name of the user cluster.

You can see this in a screenshot under [Create a control plane uptime dashboard](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#control_plane_uptime_dashboard).

Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
GKE on-prem user cluster API server unavailable (critical) | User cluster API server is not up or uptime is less than 99.99% per minute | [user-cluster-apiserver-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-apiserver-unavailable.json) | GKE on-prem user cluster scheduler unavailable (critical) | User cluster scheduler is not up or uptime is less than 99.99% per minute | [user-cluster-scheduler-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-scheduler-unavailable.json)|   
GKE on-prem user cluster controller manager unavailable (critical) | User cluster controller manager is not up or uptime is less than 99.99% per minute | [user-cluster-controller-manager-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-controller-manager-unavailable.json) | GKE on-prem user cluster etcd unavailable (critical) | User cluster etcd is not up or uptime is less than 99.99% per minute | [user-cluster-etcd-unavailable.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-etcd-unavailable.json)

### Kubernetes system

| Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
GKE on-prem pod crash looping (critical) | Pod is in a crash loop status | [pod-crash-looping.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/pod-crash-looping.json) | GKE on-prem pod not ready for more than one hour (critical) | Pod is in a non-ready state for more than one hour | [pod-not-ready-1h.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/pod-not-ready-1h.json)  
GKE on-prem persistent volume high usage (critical) | Persistent volume claimed is expected to fill up | [persistent-volume-usage-high.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/persistent-volume-usage-high.json) | GKE on-prem node not ready for more than one hour (critical) | Node is in a non-ready state for more than one hour | [node-not-ready-1h.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/node-not-ready-1h.json)

### Kubernetes performance

| Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
GKE on-prem admin cluster API server error count ratio exceeds 10 percent (critical) | Admin cluster API server is returning errors for more than 10% of requests | [admin-cluster-apiserver-error-ratio-10-percent.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-apiserver-error-ratio-10-percent.json) | GKE on-prem admin cluster API server error count ratio exceeds 5 percent (warning) | Admin cluster API server is returning errors for more than 5% of requests | [admin-cluster-apiserver-error-ratio-5-percent.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/admin-cluster-apiserver-error-ratio-5-percent.json)  
GKE on-prem user cluster API server error count ratio exceeds 10 percent (critical) | User cluster API server is returning errors for more than 10% of requests | [user-cluster-apiserver-error-ratio-10-percent.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-apiserver-error-ratio-10-percent.json) | GKE on-prem user cluster API server error count ratio exceeds 5 percent (warning) | User cluster API server is returning errors for more than 5% of requests | [user-cluster-apiserver-error-ratio-5-percent.json](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/samples/user-cluster-apiserver-error-ratio-5-percent.json)

## Getting notified

After you create an alerting policy, you can define one or more [notification channels](https://docs.cloud.google.com/monitoring/alerts) for the policy. There are several kinds of notification channels. For example, you could be notified by email, a Slack channel, or a mobile app. You can choose the channels that suit your needs. For instructions about how to configure notification channels, see [Managing notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-13 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
