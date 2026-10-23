---
url: https://docs.cloud.google.com/openshift-cluster/automate-cluster-config-validation/
title: Automate cluster configuration validation \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:18.212041+00:00
---

# Automate cluster configuration validation  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/automate-cluster-config-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Automate cluster configuration validation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Automatic configuration validation tooling**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use Cluster Services for OpenShift to automate cluster configuration validation for self-managed OpenShift clusters that run on Google Cloud.

Continuous validation of cluster configuration is critical for ensuring that your OpenShift clusters adhere to best practices and don't drift from operational standards over time. You can address this requirement by using the _automatic configuration validation tooling_ feature of this service.

This document is intended for cloud architects and IT admins who help you manage enterprise-grade applications on your OpenShift clusters that run on Google Cloud.

## How it works

Automatic configuration validation tooling of Cluster Services for OpenShift uses the following components to evaluate your OpenShift clusters that run on Google Cloud:

  * The Cluster Services for OpenShift Telemetry operator.
  * The Workload Manager evaluation service.



The following steps describe how this tooling works and helps you validate the configuration of your OpenShift cluster:

  1. You set up the telemetry operator on the target cluster.

Every 30 minutes, this operator collects information about your OpenShift cluster as metrics, and sends them to Workload Manager. This periodic and continuous metrics collection lets Workload Manager monitor for any changes.

For information about this operator, see About Cluster Services for OpenShift Telemetry operator.

  2. You create and run an evaluation in Workload Manager.

While creating an evaluation, you must select the best practices against which Workload Manager must evaluate your OpenShift cluster. You can also set the frequency for running this evaluation.

For information about Workload Manager evaluations, see [About Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).

  3. Workload Manager evaluates your OpenShift cluster against the selected best practices.

Workload Manager detects deviations and assigns them a severity level that indicates how far your cluster resource is out of compliance.

  4. You review the evaluation report, which includes information about deviation-specific remediation, and then you perform necessary actions.




## Pricing

For information about Workload Manager evaluation pricing, see [Workload Manager pricing](https://cloud.google.com/products/workload-manager/pricing).

## Supported validations

For information about the best practices that Workload Manager supports for evaluating OpenShift clusters running on Google Cloud, see [Workload Manager best practices for OpenShift](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices-openshift).

## About Cluster Services for OpenShift Telemetry operator

To scan your self-managed OpenShift cluster that runs on Google Cloud, you must set up the Cluster Services for OpenShift Telemetry operator in that cluster.

This is a certified operator available on the [OperatorHub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.4/html/operators/olm-understanding-operatorhub) on the Red Hat OpenShift Container Platform. This operator manages the Agent for Compute Workloads, which collects information from your OpenShift cluster as metrics and sends them to Workload Manager. For information about the metrics that the operator collects, see Metrics collected by the telemetry operator.

To help you satisfy security requirements, you can view the source code of the Agent for Compute Workloads in the following read-only GitHub repository: [GoogleCloudPlatform/workloadagent](https://github.com/GoogleCloudPlatform/workloadagent).

### Metrics collected by the telemetry operator

For information about the metrics that the operator collects from your OpenShift cluster, see the [`GoogleCloudPlatform/workloadagent`](https://github.com/GoogleCloudPlatform/workloadagent/blob/main/protos/openshiftmetrics/openshiftmetrics.proto) GitHub repository.

## What's next

  * [Set up the Cluster Services for OpenShift Telemetry operator](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
