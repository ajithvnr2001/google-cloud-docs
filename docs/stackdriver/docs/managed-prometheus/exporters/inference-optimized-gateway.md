---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/inference-optimized-gateway/
title: GKE Inference Gateway \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:16.995465+00:00
---

# GKE Inference Gateway  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/inference-optimized-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from GKE Inference Gateway. This document shows you how to do the following: 

  * Set up GKE Inference Gateway to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [GKE Inference Gateway documentation](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/2d7613c9b2bebada4c212495326272137c5846db/site-src/guides/metrics-and-observability.md) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about GKE Inference Gateway, see [GKE Inference Gateway](https://github.com/kubernetes-sigs/gateway-api-inference-extension/). 

## Prerequisites

To collect metrics from the GKE Inference Gateway exporter by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

The GKE Inference Gateway exporter exposes Prometheus-format metrics automatically; you don't have to install it separately. 

To verify that the GKE Inference Gateway exporter is emitting metrics on the expected endpoints, do the following:

  1. Add a secret, ServiceAccount, ClusterRole, and ClusterBinding. The GKE Inference Gateway exporter observability endpoints are protected by the auth token. To obtain credentials, the client requires a Secret that maps to a service account with the connected ClusterRole, for the `nonResourceURLs: "/metrics", verbs: get` rule. For more information, see Create a secret for a service account.

  2. Set up port forwarding by using the following command:
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 9090
         

  3. In another window, do the following:

     1. Fetch the token by running the following command:
            
            TOKEN=$(kubectl -n default get secret inference-gateway-sa-metrics-reader-secret  -o jsonpath='{.secrets[0].name}' -o jsonpath='{.data.token}' | base64 --decode)
            

     2. Access the endpoint `localhost:9090/metrics` using the `curl` utility:
            
            curl -H "Authorization: Bearer $TOKEN" localhost:9090/metrics
            




## Create a secret for a service account

For the protected the GKE Inference Gateway exporter endpoint, the Managed Service for Prometheus Operator requires a secret for authorized metric collection in the `gmp-system` namespace.

If your cluster is using Autopilot mode, then replace `gmp-system` with `gke-gmp-system`.

You can use the following Secret, ServiceAccount, ClusterRole and ClusterRoleBinding configuration:
    
    
    # Copyright 2025 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: inference-gateway-metrics-reader
    rules:
    - nonResourceURLs:
      - /metrics
      verbs:
      - get
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: inference-gateway-sa-metrics-reader
      namespace: default
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: inference-gateway-sa-metrics-reader-role-binding
      namespace: default
    subjects:
    - kind: ServiceAccount
      name: inference-gateway-sa-metrics-reader
      namespace: default
    roleRef:
      kind: ClusterRole
      name: inference-gateway-metrics-reader
      apiGroup: rbac.authorization.k8s.io
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: inference-gateway-sa-metrics-reader-secret
      namespace: default
      annotations:
        kubernetes.io/service-account.name: inference-gateway-sa-metrics-reader
    type: kubernetes.io/service-account-token
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: inference-gateway-sa-metrics-reader-secret-read
    rules:
    - resources:
      - secrets
      apiGroups: [""]
      verbs: ["get", "list", "watch"]
      resourceNames: ["inference-gateway-sa-metrics-reader-secret"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: gmp-system:collector:inference-gateway-sa-metrics-reader-secret-read
      namespace: default
    roleRef:
      name: inference-gateway-sa-metrics-reader-secret-read
      kind: ClusterRole
      apiGroup: rbac.authorization.k8s.io
    subjects:
    - name: collector
      namespace: gmp-system
      kind: ServiceAccount
    

For more information, see the exporter's [Metric & Observability guide](https://github.com/kubernetes-sigs/gateway-api-inference-extension/blob/2d7613c9b2bebada4c212495326272137c5846db/site-src/guides/metrics-and-observability.md#scrape-metrics--pprof-profiles). 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a ClusterPodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a ClusterPodMonitoring resource that corresponds to the GKE Inference Gateway exporter in the same namespace.

You can use the following ClusterPodMonitoring configuration:
    
    
    # Copyright 2025 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: monitoring.googleapis.com/v1
    kind: ClusterPodMonitoring
    metadata:
      name: inference-optimized-gateway-monitoring
      labels:
        app.kubernetes.io/name: inference-optimized-gateway
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: metrics
        scheme: http
        interval: 5s
        path: /metrics
        authorization:
          type: Bearer
          credentials:
            secret:
              name: inference-gateway-sa-metrics-reader-secret
              key: token
              namespace: default
      selector:
        matchLabels:
          app: inference-gateway-ext-proc
    

GKE Inference Gateway uses the `ClusterPodMonitoring` resource instead of the `PodMonitoring` resource because it needs to access the secret from another namespace.

In the `matchLabels` selector of the `ClusterPodMonitoring` configuration, you can replace the `app` value of `inference-gateway-ext-proc` with labels from your GKE Inference Gateway deployment. Ensure that the values of the `port` and `matchLabels` fields match those of the GKE Inference Gateway pods you want to monitor.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the GKE Inference Gateway exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         inference_model_request_total{cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **GKE Inference Gateway Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **GKE Inference Gateway Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the GKE Inference Gateway integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
