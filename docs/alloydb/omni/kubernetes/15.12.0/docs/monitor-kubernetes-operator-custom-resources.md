---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/monitor-kubernetes-operator-custom-resources/
title: Monitor AlloyDB Omni Kubernetes operator custom resources \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.12.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:44.310531+00:00
---

# Monitor AlloyDB Omni Kubernetes operator custom resources  |  AlloyDB Omni for Kubernetes: 15.12.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/monitor-kubernetes-operator-custom-resources/

This page documents AlloyDB Omni version **15.12.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/overview)



Send feedback 

#  Monitor AlloyDB Omni Kubernetes operator custom resources Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.12.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/monitor-kubernetes-operator-custom-resources)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/monitor-kubernetes-operator-custom-resources)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/monitor-kubernetes-operator-custom-resources)

This page describes how to monitor the status of AlloyDB Omni Kubernetes operator custom resources using [kube-state-metrics](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/) (KSM). **Note:** These metrics are only available on AlloyDB Omni Kubernetes operator version 1.3.0 and later.

Running KSM with the Kubernetes operator lets you do the following:

  * Monitor custom resource status in real time on your Prometheus-compatible observability stack, together with [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/omni-metrics).
  * Build dashboards and alerts on top of the custom resource metrics for better operational visibility and proactive issue detection.



For more information about kube-state-metrics, see [Overview](https://github.com/kubernetes/kube-state-metrics/tree/main?tab=readme-ov-file#overview). To learn how kube-state-metrics monitors Kubernetes custom resources, see [Custom Resource State Metrics](https://github.com/kubernetes/kube-state-metrics/blob/main/docs/metrics/extend/customresourcestate-metrics.md#custom-resource-state-metrics).

## How AlloyDB Omni Kubernetes operator custom resources work

By default, custom resource metrics aren't enabled. You can enable custom resource metrics using the AlloyDB Omni Kubernetes operator Helm chart. When you enable custom resource metrics, a KSM deployment is created with a `configmap` that defines the custom resource metrics and a service of type ClusterIP to expose the metrics endpoint of the KSM deployment. Your [Prometheus](https://prometheus.io/) collector can collect the metrics, and you can visualize these metrics with other AlloyDB Omni metrics. For more information, see [Custom resources metrics for the AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/custom-resource-metrics-kubernetes-operator).

## Before you begin

Make sure that you have the following:

  * A [Prometheus](https://prometheus.io/)-compatible metrics scraper running in your Kubernetes cluster.
  * Access to the kube-state-metrics image hosted at `registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.14.0`. You can pre-pull the image to your private registry.
  * [The `helm` package manager](https://helm.sh/docs/intro/install/). You run Helm commands in a Linux command-line terminal.



## Install the Kubernetes operator with custom resource metrics enabled

You use the following variables in the AlloyDB Omni Kubernetes operator Helm chart to control the installation and removal of custom resource metrics:

**Variable** | **Type** | **Description** | **Default**  
---|---|---|---  
` crdMetrics.enabled ` | Boolean (true/false) | Enables and disables custom resource metrics | false (disable)  
` crdMetrics.ksmImage ` | String | Full path of the `ksmImage` | ` registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.14.0 `  
  
If you haven't installed the operator Helm chart yet, set the variables when you run the Helm install.

To install Kubernetes operator with custom resource metrics enabled, follow these steps:

  1. Open a Linux command-line terminal.
  2. Define the following environment variables by running the following commands:
         
         export GCS_BUCKET=alloydb-omni-operator
         export HELM_PATH=$(gcloud storage cat gs://$GCS_BUCKET/latest)
         export OPERATOR_VERSION="${HELM_PATH%%/*}"
         

  3. Download the AlloyDB Omni Kubernetes operator:
         
         gcloud storage cp gs://$GCS_BUCKET/$HELM_PATH ./ --recursive
         

  4. If you pre-pull the public KSM image at `registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.14.0` to your private registry, skip this step and proceed to the next step. Otherwise, install the AlloyDB Omni Kubernetes operator with custom resource metrics, and then proceed to the final step in this procedure.
         
         helm install alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --create-namespace \
         --namespace alloydb-omni-system \
         --set crdMetrics.enabled=true \
         --atomic \
         --timeout 5m
         

  5. Export the environment variable:
         
         export KSM_IMAGE=<full path to your KSM image>
         

  6. To install the AlloyDB Omni Kubernetes operator with custom resource metrics and your own KSM image location, run the following command:
         
         helm install alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --create-namespace \
         --namespace alloydb-omni-system \
         --set crdMetrics.enabled=true,crdMetrics.ksmImage=${KSM_IMAGE} \
         --atomic \
         --timeout 5m
         

A successful installation returns the following output:
         
         NAME: alloydbomni-operator
         LAST DEPLOYED: CURRENT_TIMESTAMP
         NAMESPACE: alloydb-omni-system
         STATUS: deployed
         REVISION: 1
         TEST SUITE: None
         

**Note:** If you use Red Hat OpenShift 4.12 or later, then after you install the AlloyDB Omni Kubernetes operator you must perform the [Red Hat OpenShift reconciliation steps](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/deploy-kubernetes#rhel-openshift).
  7. Clean up the installation by deleting the downloaded AlloyDB Omni Kubernetes operator installation file. The file is named `alloydbomni-operator-VERSION_NUMBER.tgz`, and is located in your current working directory.




## Enable custom resource metrics on an existing Kubernetes operator

If you already have the AlloyDB Omni Kubernetes operator version 1.3.0 (or later) installed, you can enable custom resource metrics by upgrading the existing operator.

  1. Open a Linux command-line terminal.
  2. Find your current AlloyDB Omni Kubernetes operator version and define the environment variables by running the following commands:
         
         export OPERATOR_VERSION=$(helm ls -n alloydb-omni-system  -o json | jq -r 'map(select(.name == "alloydbomni-operator") | .chart)| .[0]')
         
         OPERATOR_VERSION=${OPERATOR_VERSION#"alloydbomni-operator-"}
         
         echo $OPERATOR_VERSION
         
         export GCS_BUCKET=alloydb-omni-operator
         
         export HELM_PATH=$OPERATOR_VERSION/alloydbomni-operator-$OPERATOR_VERSION.tgz
         

The output is your installed AlloyDB Omni Kubernetes operator version, for example, `1.3.0`.

  3. Download the specified version operator:
         
         gcloud storage cp gs://$GCS_BUCKET/$HELM_PATH ./ --recursive
         

  4. Upgrade the AlloyDB Omni Kubernetes operator by running the following commands, and then go to the final step in this procedure. If you pre-pull the public KSM image at `registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.14.0` to your private registry, then skip this step and proceed directly to the next step.
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --reuse-values \
         --set crdMetrics.enabled=true \
         --atomic \
         --timeout 5m
         

  5. Export the environment variable:
         
         export KSM_IMAGE=<full path to your KSM image>
         

  6. To perform the upgrade, run the following command:
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --reuse-values \
         --set crdMetrics.enabled=true,crdMetrics.ksmImage=${KSM_IMAGE} \
         --atomic \
         --timeout 5m
         

**Note:** Performing this upgrade doesn't cause a database restart.

A successful upgrade returns the following output:
         
         NAME: alloydbomni-operator
         LAST DEPLOYED: CURRENT_TIMESTAMP
         NAMESPACE: alloydb-omni-system
         STATUS: deployed
         REVISION: 2
         TEST SUITE: None
         




## Disable custom resource metrics on an existing Kubernetes operator

  1. Open a Linux command-line terminal.
  2. Run the following command:
         
         export OPERATOR_VERSION=$(helm ls -n alloydb-omni-system  -o json | jq -r 'map(select(.name == "alloydbomni-operator") | .chart)| .[0]')
         
         OPERATOR_VERSION=${OPERATOR_VERSION#"alloydbomni-operator-"}
         

  3. To disable custom resource metrics, run the following command:
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --reuse-values \
         --set crdMetrics.enabled=false \
         --atomic \
         --timeout 5m
         




## View metrics using the Prometheus API

To view your metrics, see [View metrics using the Prometheus API](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/manage#kubernetes).

## What's next

  * Learn about [custom resources definition metrics for the AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/custom-resource-metrics-kubernetes-operator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
