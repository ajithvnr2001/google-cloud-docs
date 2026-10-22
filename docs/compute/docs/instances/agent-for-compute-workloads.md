---
url: https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads/
title: Agent for Compute Workloads overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:54.390938+00:00
---

# Agent for Compute Workloads overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Agent for Compute Workloads overview Stay organized with collections  Save and categorize content based on your preferences. 

The Agent for Compute Workloads lets you monitor and evaluate workloads running on Compute Engine.

Once you install the agent on the compute instances that host your workload, the agent collects metrics from your workload and instances, and sends them to Workload Manager. After this, you use the evaluation service of Workload Manager to evaluate your workload against industry best practices and those recommended by Google Cloud. For more information, see [About Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).

## Supported workloads

You can use the Agent for Compute Workloads for evaluating the following workloads running on Compute Engine:

  * Microsoft SQL Server
  * Oracle
  * MySQL
  * Redis
  * Red Hat OpenShift, through the [Cluster Services for OpenShift Telemetry operator](https://docs.cloud.google.com/openshift-cluster/automate-cluster-config-validation#about-cso-telemetry-operator) ([Preview](https://cloud.google.com/products#product-launch-stages))



You can configure the agent to collect metrics from multiple workloads running on the same Compute Engine instance. You do this by specifying each workload in the agent's configuration file.

## Supported OS versions

You can install and run the Agent for Compute Workloads on Linux and Windows supported by Compute Engine. For information about OS versions supported by Compute Engine, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

## Pricing

While you don't incur any charges for installing and running the Agent for Compute Workloads, you might be charged for the metrics or logs that the agent sends to your Google Cloud project.

For information about the cost you incur for sending logs to your Google Cloud project, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

## Agent codebase

To help you satisfy security requirements, you can view the source code of the Agent for Compute Workloads in the following read-only GitHub repository: [GoogleCloudPlatform/workloadagent](https://github.com/GoogleCloudPlatform/workloadagent).

## What's next

  * Learn [about Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations)
  * Learn how to [enable Workload Manager](https://docs.cloud.google.com/workload-manager/docs/enable)
  * Learn how to [set up the agent for Microsoft SQL Server workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sql-server)
  * Learn how to [set up the agent for Oracle workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle)
  * Learn how to [set up the agent for MySQL workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-mysql)
  * Learn how to [set up the agent for Redis workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis)
  * Learn how to [set up the Cluster Services for OpenShift Telemetry operator](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift) ([Preview](https://cloud.google.com/products#product-launch-stages))



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
