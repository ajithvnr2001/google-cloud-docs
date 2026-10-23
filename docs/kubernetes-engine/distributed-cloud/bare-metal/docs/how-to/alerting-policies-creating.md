---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/alerting-policies-creating/
title: Create alerting policies \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:08.860902+00:00
---

# Create alerting policies  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/alerting-policies-creating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create metric-based alerting policies for Google Distributed Cloud clusters. For more information about metric-based alerting policies, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) in Google Cloud observability documentation.

## Before you begin

You must have the following permissions to create alerting policies:

  * `monitoring.alertPolicies.create`
  * `monitoring.alertPolicies.delete`
  * `monitoring.alertPolicies.update`



You have these permissions if you have any one of the following [roles](https://docs.cloud.google.com/monitoring/access-control#predefined_roles):

  * `monitoring.alertPolicyEditor`
  * `monitoring.editor`
  * Project editor
  * Project owner



To create a [log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) by using the Google Cloud CLI, you must also have the `serviceusage.serviceUsageConsumer` role. For instructions to set up log-based alerting policies, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in Google Cloud Observability documentation.

To check your roles, go to the [IAM page](https://console.cloud.google.com/iam-admin/iam) in the Google Cloud console.

## Creating an example policy: API server unavailable

In this exercise, you create an alerting policy for Kubernetes API servers. With this policy in place, you can arrange to be notified whenever the API server of a cluster is unavailable.

  1. Download the policy configuration file: [apiserver-unavailable.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/apiserver-unavailable.json)
  2. Create the policy: 
         
         gcloud monitoring policies create --policy-from-file=POLICY_CONFIG
             

Replace POLICY_CONFIG with the path of the configuration file you just downloaded.

  3. View your alerting policies: 

### Console

     1. In the Google Cloud console, go to the **Monitoring** page. 

[Go to Monitoring](https://console.cloud.google.com/monitoring)

     2. On the left, select **Alerting**.
     3. Under **Policies** , you can see a list of your alerting policies. 

In the list, select **Anthos cluster API server unavailable (critical)** to see details about your new policy. Under **Conditions** , you can see a description of the policy. For example:
            
            Policy violates when ANY condition is met
            Anthos cluster API server uptime is absent for 5m

### gcloud
    
    gcloud monitoring policies list

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
          - resource.label.pod_name
          perSeriesAligner: ALIGN_MAX
        duration: 300s
        filter: resource.type = "k8s_container" AND metric.type = "kubernetes.io/anthos/container/uptime"
          AND resource.label."container_name"=monitoring.regex.full_match("kube-apiserver")
        trigger:
          count: 1
      displayName: Anthos cluster API server uptime is absent for 5m
      name: projects/…/alertPolicies/…/conditions/…
    displayName: Anthos cluster API server unavailable (critical)
    enabled: true
    mutationRecord:
      mutateTime: …
      mutatedBy: …
    name: projects/…/alertPolicies/…




## Creating additional alerting policies

This section provides descriptions and configuration files for a set of recommended alerting policies.

To create a policy, follow the same steps that you used in the preceding exercise:

  1. To download the configuration file, click the link in the right column.
  2. Optionally, tune the conditions to better fit your specific needs, for example, you can add additional filters for a subset of clusters, or adjust the threshold values to balance between noisiness and criticality.
  3. Run `gcloud monitoring policies create` to create the policy.



You can download and install all of the alert policy samples described in this document with the following script:
    
    
    # 1. Create a directory named alert_samples:
    
    mkdir alert_samples && cd alert_samples
    declare -a alerts=("apiserver-unavailable.json" "controller-manager-unavailable.json" "scheduler-unavailable.json" \
      "pod-crash-looping.json" "pod-not-ready-1h.json" "container-cpu-usage-high-reaching-limit.json" \
      "container-memory-usage-high-reaching-limit.json" "persistent-volume-usage-high.json" "node-cpu-usage-high.json" \
      "node-disk-usage-high.json" "node-memory-usage-high.json" "node-not-ready-1h.json" "apiserver-error-ratio-high.json" \
      "etcd-leader-changes-or-proposal-failures-frequent.json" "etcd-server-not-in-quorum.yaml" "etcd-storage-usage-high.json")
    
    # 2. Download all alert samples into the alert_samples/ directory:
    
    for x in "${alerts[@]}"
    do
      wget https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/${x}
    done
    
    # 3. (optional) Uncomment and provide your project ID to set the default project
    # for gcloud commands:
    
    # gcloud config set project <PROJECT_ID>
    
    # 4. Create alert policies for each of the downloaded samples:
    
    for x in "${alerts[@]}"
    do
      gcloud monitoring policies create --policy-from-file=${x}
    done
    

### Control plane components availability

Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
API server unavailable (critical) | API server uptime metric is unavailable | [apiserver-unavailable.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/apiserver-unavailable.json)  
Scheduler unavailable (critical) | Scheduler uptime metric is unavailable | [scheduler-unavailable.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/scheduler-unavailable.json)  
Controller manager unavailable (critical) | Controller manager uptime metric is unavailable | [controller-manager-unavailable.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/controller-manager-unavailable.json)  
  
### Kubernetes system

Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
Pod crash looping (warning) | Pod keeps restarting and might be in a crash loop status | [pod-crash-looping.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/pod-crash-looping.json)  
Pod not ready for more than one hour (critical) | Pod is in a non-ready state for more than one hour | [pod-not-ready-1h.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/pod-not-ready-1h.json)  
Container cpu usage exceeds 80 percent (warning) | Container cpu usage is over 80% of limit | [container-cpu-usage-high-reaching-limit.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/container-cpu-usage-high-reaching-limit.json)  
Container memory usage exceeds 85 percent (warning) | Container memory usage is over 85% of limit | [container-memory-usage-high-reaching-limit.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/container-memory-usage-high-reaching-limit.json)  
Persistent volume high usage (critical) | Claimed persistent volume has less than 3 percent of free space | [persistent-volume-usage-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/persistent-volume-usage-high.json)  
Node cpu usage exceeds 80 percent (warning) | Node cpu usage is over 80% of total allocatable for 5m | [node-cpu-usage-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/node-cpu-usage-high.json)  
Node disk usage exceeds 85 percent (warning) | Less than 15 percent is free per disk mountpoint for 10 mins | [node-disk-usage-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/node-disk-usage-high.json)  
Node memory usage exceeds 80 percent (warning) | Node memory usage is over 80% of total allocatable for 5m | [node-memory-usage-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/node-memory-usage-high.json)  
Node not ready for more than one hour (critical) | Node is in a non-ready state for more than one hour | [node-not-ready-1h.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/node-not-ready-1h.json)  
  
### Kubernetes performance

Alert name | Description | Alerting policy definition in Cloud Monitoring  
---|---|---  
API server error ratio exceeds 20 percent (critical) | API server gives 5xx or 429 errors on more than 20% of all requests per verb for 15m | [apiserver-error-ratio-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/apiserver-error-ratio-high.json)  
ETCD leader change or proposal failure too frequent (warning) | The `etcd` leader changes or proposal failures happen too frequently | [etcd-leader-changes-or-proposal-failures-frequent.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/etcd-leader-changes-or-proposal-failures-frequent.json)  
ETCD server is not in quorum (critical) | No `etcd` server proposals committed for 5 min, so they might have lost quorum | [etcd-server-not-in-quorum.yaml](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/etcd-server-not-in-quorum.yaml)  
ETCD storage exceeds 90 percent limit (warning) | The `etcd` storage usage is more than 90% of limit | [etcd-storage-usage-high.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/etcd-storage-usage-high.json)  
  
## Alert Policies with PromQL

The queries in alert policies can also be expressed in PromQL instead of MQL. For example, the PromQL version of the `API server error ratio exceeds 20 percent (critical)` policy is available to download: [apiserver-error-ratio-high-promql.json](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/samples/apiserver-error-ratio-high-promql.json).

For more information, see [Use Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#using-managed-service-for-prometheus) for Google Distributed Cloud documentation and the [Alerting policies with PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting) for Cloud Monitoring documentation.

## Getting notified

After you create an alerting policy, you can define one or more [notification channels](https://docs.cloud.google.com/monitoring/alerts#how_does_alerting_work) for the policy. There are several kinds of notification channels. For example, you can be notified by email, a Slack channel, or a mobile app. You can choose the channels that suit your needs.

For instructions about how to configure notification channels, see [Managing notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
