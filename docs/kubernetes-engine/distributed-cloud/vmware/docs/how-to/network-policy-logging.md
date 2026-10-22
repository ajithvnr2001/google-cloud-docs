---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/network-policy-logging/
title: Logging network policy events \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:51.926132+00:00
---

# Logging network policy events  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/network-policy-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Logging network policy events Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable network policy logging in a Google Distributed Cloud user cluster and how to export logs. See [Using network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to learn how to configure which events are logged and how logs are formatted.

## Overview

[Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) are Pod-level firewalls; they specify network traffic that Pods are allowed to send and receive. Network policy logs record network policy events. You can log all events or you can [configure logging selectively](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging#configuring_network_policy_logging) based on the following criteria:

  * Allowed connections.
  * Denied connections.
  * Connections allowed by specific policies.
  * Denied connections to Pods in specific namespaces.



## Before you begin

Network policy logging is supported in user clusters that use [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2). You can enable Dataplane V2 when creating a new user cluster by using the [`enableDataplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) field in the user cluster configuration file.

## Enabling logging

Network policy logging is not enabled by default. For information on enabling logging and selecting which events to log, see [Configuring network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging#configuring_network_policy_logging).

## Accessing logs

The network policy logs generated on each cluster node are available locally on the cluster nodes at `/var/log/network/policy_actiontimestamp.log`. A new timestamped log file is created when the current log file reaches 10 MB. Up to five previous log files are stored.

## Exporting logs

We recommend you use [Fluent Bit](https://fluentbit.io/) to export logs from your cluster nodes. Fluent Bit is an open source log processor and forwarder that supports exporting to Cloud Logging and many [other data sinks](https://docs.fluentbit.io/manual/pipeline/outputs).

## What's next

  * Learn [how to configure network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging)
  * Learn how to [create a network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
