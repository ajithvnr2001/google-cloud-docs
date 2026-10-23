---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics/
title: View TPU metrics on the Ray Dashboard \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:52.711604+00:00
---

# View TPU metrics on the Ray Dashboard  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  View TPU metrics on the Ray Dashboard Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to view TPU metrics on the Ray Dashboard with KubeRay on Google Kubernetes Engine (GKE). In a GKE cluster with the Ray GKE add-on, TPU metrics are available in Cloud Monitoring.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * You have a GKE cluster that meets the following conditions:

    * A node pool configured to use TPUs.
    * The Ray on GKE add-on must _not_ be enabled on this cluster.
    * A serving or training workload on GKE using Ray and TPUs.

If you need to create a cluster with these conditions, choose an example TPU workload such as [Train an LLM using JAX, Ray Train, and TPU Trillium on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu) or the [Serve an LLM using TPUs on GKE with KubeRay](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray) and follow the setup steps to configure a cluster.




## Prepare your environment

In this tutorial you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and `kubectl` command-line tool. The gcloud CLI provides the primary command-line interface for Google Cloud, and `kubectl` provides the primary command-line interface for running commands against Kubernetes clusters.

Launch Cloud Shell:

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the upper-right corner of the console, click the **Activate Cloud Shell** button: ![](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` and `kubectl` commands. Before you run commands, set your default project in the Google Cloud CLI using the following command:
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

## View TPU metrics on the Ray Dashboard

To view TPU metrics on the Ray Dashboard, do the following:

  1. In your shell, enable metrics in the Ray Dashboard by installing the Kubernetes Prometheus Stack.
         
         ./install/prometheus/install.sh --auto-load-dashboard true
         kubectl get all -n prometheus-system
         

The output is similar to the following:
         
         NAME                                                  READY   UP-TO-DATE   AVAILABLE   AGE
         deployment.apps/prometheus-grafana                    1/1     1            1           46s
         deployment.apps/prometheus-kube-prometheus-operator   1/1     1            1           46s
         deployment.apps/prometheus-kube-state-metrics         1/1     1            1           46s
         

This installation uses a Helm chart to add the Custom Resource Definitions (CRDs), a Pod Monitor, and a Service Monitor for Ray Pods to your cluster.

  2. Install KubeRay operator v1.5.0 or later with metrics scraping enabled. To view TPU metrics in Grafana with the default dashboards provided in KubeRay, you must install KubeRay v1.5.0 or later.
         
         helm repo add kuberay https://ray-project.github.io/kuberay-helm/
         helm install kuberay-operator kuberay/kuberay-operator --version 1.5.0-rc.0 \
             --set metrics.serviceMonitor.enabled=true \
             --set metrics.serviceMonitor.selector.release=prometheus
         

  3. Install the KubeRay TPU webhook. This webhook sets an environment variable `TPU_DEVICE_PLUGIN_HOST_IP` that Ray uses to poll TPU metrics from the `tpu-device-plugin` DaemonSet.
         
         helm install kuberay-tpu-webhook \
         oci://us-docker.pkg.dev/ai-on-gke/kuberay-tpu-webhook-helm/kuberay-tpu-webhook \
             --set tpuWebhook.image.tag=v1.2.6-gke.0
         

  4. To prepare your workload to log the metrics, set the following ports and environment variables within the RayCluster spec:
         
         headGroupSpec:
         ...
         ports:
         ...
         - containerPort: 44217
           name: as-metrics
         - containerPort: 44227
           name: dash-metrics
         env:
         - name: RAY_GRAFANA_IFRAME_HOST
           value: http://127.0.0.1:3000
         - name: RAY_GRAFANA_HOST
           value: http://prometheus-grafana.prometheus-system.svc:80
         - name: RAY_PROMETHEUS_HOST
           value: http://prometheus-kube-prometheus-prometheus.prometheus-system.svc:9090
         

  5. Run a workload with TPUs by using Ray. You can use an example TPU workload such as [Train an LLM using JAX, Ray Train, and TPU Trillium on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu) or the [Serve an LLM using TPUs on GKE with KubeRay](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray).




## View the metrics in the Ray Dashboard or Grafana

  1. To connect to the RayCluster, port-forward the Ray head service:
         
         kubectl port-forward service/RAY_CLUSTER_NAME-head-svc 8265:8265
         

Replace `RAY_CLUSTER_NAME` with the name of your RayCluster. If your workload is from the [Train an LLM using JAX, Ray Train, and TPU Trillium on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu) tutorial, then this value is `maxtext-tpu-cluster`.

  2. To view the Ray Dashboard, navigate to `http://localhost:8265/` on your local machine.

  3. Port forward the Grafana web UI. You need to port-forward Grafana to view TPU metrics which are displayed on Grafana dashboards embedded in the Ray Dashboard.
         
         kubectl port-forward -n prometheus-system service/prometheus-grafana 3000:http-web
         

  4. In the Ray Dashboard, open the **Metrics** tab and find the **TPU Utilization by Node** tab. When TPUs are running, per-node metrics for Tensor Core utilization, HBM utilization, TPU duty cycle, and memory usage are streamed to the dashboard. These metrics are viewable in Grafana by navigating to **View Tab in Grafana**.

![Graph showing metrics in the Ray Dashboard or Grafana](https://docs.cloud.google.com/static/kubernetes-engine/docs/add-on/ray-on-gke/images/metrics-in-ray-dashboard.png)

  5. To view `libtpu` logs, navigate to the **Logs** tab on the Ray Dashboard and select the TPU node. Libtpu logs are written to the `/tpu_logs` directory.




For more information on configuring TPU logging, see [Debugging TPU VM logs](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-tf#debug_logs).

## What's next

  * Learn how to [collect and view logs and metrics for Ray clusters on Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).
  * Learn how to [view Ray Operator logs](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-ray-operator-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
