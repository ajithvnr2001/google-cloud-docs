---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-policy-logging/
title: Use network policy logging \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:28.183526+00:00
---

# Use network policy logging  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-policy-logging/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use network policy logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable network policy logging in an GKE cluster and how to export logs.

## Overview

[Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) are Pod-level firewalls; they specify the network traffic that Pods are allowed to send and receive. Network policy logs record network policy events. You can log all events or you can choose to log events based on the following criteria:

  * Allowed connections.
  * Denied connections.
  * Connections allowed by specific policies.
  * Connections denied to Pods in specific namespaces.



## Enabling logging

Network policy logging is not enabled by default. For information on enabling logging and selecting which events to log, see [Using network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) in the Google Kubernetes Engine documentation.

## Accessing logs

Network policy logs are automatically uploaded to [Cloud Logging](https://docs.cloud.google.com/logging/docs). You can access logs through the Logs Explorer or with the Google Cloud CLI. You can also [export logs from Cloud Logging](https://docs.cloud.google.com/logging/docs/export) to the sink of your choice.

### gcloud
    
    
    gcloud logging read --project "PROJECT_NAME" 'resource.type="k8s_node" \
        resource.labels.location="CLUSTER_LOCATION" \
        resource.labels.cluster_name="awsClusters/CLUSTER_NAME" \
        logName="projects/PROJECT_NAME/logs/policy-action"'
    

Replace the following:

  * `PROJECT_NAME`: your Google Cloud project
  * `CLUSTER_LOCATION`: the Google Cloud location your cluster is managed from
  * `CLUSTER_NAME`: the name of your cluster



### Cloud Logging

  1. Go to the **Logs Explorer** page in Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **Query builder**.

  3. Use the following query to find all network policy log records:
         
         resource.type="k8s_node"
         resource.labels.location="CLUSTER_LOCATION"
         resource.labels.cluster_name="awsClusters/CLUSTER_NAME"
         logName="projects/PROJECT_NAME/logs/policy-action"
         

Replace the following:

     * `CLUSTER_LOCATION`: the Google Cloud location your cluster is managed from
     * `CLUSTER_NAME`: the name of your cluster.
     * `PROJECT_NAME`: your Google Cloud project.



To learn how to use the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

You can also build a query using the **Query builder**. To query for network policy logs, select **policy-action** in the **Log name** drop-down list. If there are no logs available, **policy-action** does not appear in the drop- down list.

### Local access to network policy logs

If you have access to a node's file system, network policy logs are available on each node in the local file `/var/log/network/policy_action.log*`. Nodes rotate log files when the current log file reaches 10 MB. Up to five previous log files are stored.

## What's next

  * Learn [how to configure network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
