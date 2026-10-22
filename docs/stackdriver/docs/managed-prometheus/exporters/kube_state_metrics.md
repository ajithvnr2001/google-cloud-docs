---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics/
title: Kube State Metrics \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:28.372302+00:00
---

# Kube State Metrics  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Kube State Metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Kube State Metrics. This document shows you how to do the following: 

  * Set up Kube State Metrics to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/kubernetes/kube-state-metrics) for Kube State Metrics for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

## Prerequisites

To collect metrics from Kube State Metrics by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the integration, you must use `kube-state-metrics` version 2.4.2 or later. 

For more information about available dashboards, see Install dashboards. 




## Managed Kube State Metrics

GKE offers a fully managed deployment of kube state metrics as an alternative to configuring this integration. The installable package provides an opinionated, curated set of kube state metrics that requires less effort to set up. This integration provides additional metrics but also requires more effort to set up. To review the curated package before deciding which to use, see [ Package: Kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package). 

## Install Kube State Metrics

You can use the following configuration to install Kube State Metrics:
    
    
    # Copyright 2023 Google LLC
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
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/version: 2.12.0
      namespace: gmp-public
      name: kube-state-metrics
    spec:
      replicas: 1
      selector:
        matchLabels:
          app.kubernetes.io/name: kube-state-metrics
      serviceName: kube-state-metrics
      template:
        metadata:
          labels:
            app.kubernetes.io/name: kube-state-metrics
            app.kubernetes.io/version: 2.12.0
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: kubernetes.io/arch
                    operator: In
                    values:
                    - arm64
                    - amd64
                  - key: kubernetes.io/os
                    operator: In
                    values:
                    - linux
          containers:
          - name: kube-state-metric
            image: registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.12.0
            env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            args:
            - --pod=$(POD_NAME)
            - --pod-namespace=$(POD_NAMESPACE)
            - --port=8080
            - --telemetry-port=8081
            ports:
            - name: metrics
              containerPort: 8080
            - name: metrics-self
              containerPort: 8081
            resources:
              requests:
                cpu: 100m
                memory: 190Mi
              limits:
                memory: 250Mi
            securityContext:
              allowPrivilegeEscalation: false
              privileged: false
              capabilities:
                drop:
                - ALL
              runAsUser: 1000
              runAsGroup: 1000
            livenessProbe:
              httpGet:
                path: /healthz
                port: 8080
              initialDelaySeconds: 5
              timeoutSeconds: 5
            readinessProbe:
              httpGet:
                path: /
                port: 8081
              initialDelaySeconds: 5
              timeoutSeconds: 5
          serviceAccountName: kube-state-metrics
    ---
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/version: 2.12.0
      namespace: gmp-public
      name: kube-state-metrics
    spec:
      clusterIP: None
      ports:
      - name: metrics
        port: 8080
        targetPort: metrics
      - name: metrics-self
        port: 8081
        targetPort: metrics-self
      selector:
        app.kubernetes.io/name: kube-state-metrics
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      namespace: gmp-public
      name: kube-state-metrics
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/version: 2.12.0
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: gmp-public:kube-state-metrics
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/version: 2.12.0
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: gmp-public:kube-state-metrics
    subjects:
    - kind: ServiceAccount
      namespace: gmp-public
      name: kube-state-metrics
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: gmp-public:kube-state-metrics
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/version: 2.12.0
    rules:
    - apiGroups:
      - ""
      resources:
      - configmaps
      - secrets
      - nodes
      - pods
      - services
      - resourcequotas
      - replicationcontrollers
      - limitranges
      - persistentvolumeclaims
      - persistentvolumes
      - namespaces
      - endpoints
      verbs:
      - list
      - watch
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - get
    - apiGroups:
      - extensions
      resources:
      - daemonsets
      - deployments
      - replicasets
      - ingresses
      verbs:
      - list
      - watch
    - apiGroups:
      - apps
      resources:
      - statefulsets
      - daemonsets
      - deployments
      - replicasets
      verbs:
      - list
      - watch
    - apiGroups:
      - apps
      resources:
      - statefulsets
      verbs:
      - get 
    - apiGroups:
      - batch
      resources:
      - cronjobs
      - jobs
      verbs:
      - list
      - watch
    - apiGroups:
      - autoscaling
      resources:
      - horizontalpodautoscalers
      verbs:
      - list
      - watch
    - apiGroups:
      - authentication.k8s.io
      resources:
      - tokenreviews
      verbs:
      - create
    - apiGroups:
      - authorization.k8s.io
      resources:
      - subjectaccessreviews
      verbs:
      - create
    - apiGroups:
      - policy
      resources:
      - poddisruptionbudgets
      verbs:
      - list
      - watch
    - apiGroups:
      - certificates.k8s.io
      resources:
      - certificatesigningrequests
      verbs:
      - list
      - watch
    - apiGroups:
      - storage.k8s.io
      resources:
      - storageclasses
      - volumeattachments
      verbs:
      - list
      - watch
    - apiGroups:
      - admissionregistration.k8s.io
      resources:
      - mutatingwebhookconfigurations
      - validatingwebhookconfigurations
      verbs:
      - list
      - watch
    - apiGroups:
      - networking.k8s.io
      resources:
      - networkpolicies
      - ingresses
      verbs:
      - list
      - watch
    - apiGroups:
      - coordination.k8s.io
      resources:
      - leases
      verbs:
      - list
      - watch
    ---
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: kube-state-metrics
      namespace: gmp-public
    spec:
      maxReplicas: 10
      minReplicas: 1
      scaleTargetRef:
        apiVersion: apps/v1
        kind: StatefulSet
        name: kube-state-metrics
      metrics:
      - type: Resource
        resource:
          name: memory
          target:
            type: Utilization
            averageUtilization: 60
      behavior:
        scaleDown:
          policies:
          - type: Pods
            value: 1
            # Under-utilization needs to persist for `periodSeconds` before any action can be taken.
            # Current supported max from https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2beta2/.
            periodSeconds: 1800
          # Current supported max from https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2beta2/.
          stabilizationWindowSeconds: 3600
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: ClusterPodMonitoring
    metadata:
      name: kube-state-metrics
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: kube-state-metrics
      endpoints:
      - port: metrics
        interval: 30s
        metricRelabeling:
        - action: keep
          # Curated subset of metrics to reduce costs while populating default set of sample dashboards at
          # https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/dashboards/kubernetes
          # Change this regex to fit your needs for which objects you want to monitor    
          regex: kube_(daemonset|deployment|replicaset|pod|namespace|node|statefulset|persistentvolume|horizontalpodautoscaler|job_created)(_.+)?
          sourceLabels: [__name__]
      targetLabels:
        metadata: [] # explicitly empty so the metric labels are respected
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      namespace: gmp-public
      name: kube-state-metrics
      labels:
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: kube-state-metrics
      endpoints:
      - port: metrics-self
        interval: 30s
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your metrics:
    
    
    # Copyright 2022 Google LLC
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
    kind: Rules
    metadata:
      namespace: gmp-public
      name: kube-state-metrics-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: kube-state-metrics
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
        - name: kube-state-metrics
          interval: 30s
          rules:
          - alert: KubeStateMetricsListErrors
            annotations:
              description: kube-state-metrics is experiencing errors at an elevated rate in list operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all.
              summary: kube-state-metrics is experiencing errors in list operations.
            expr: |
              (sum(rate(kube_state_metrics_list_total{job="kube-state-metrics",result="error"}[5m]))
                /
              sum(rate(kube_state_metrics_list_total{job="kube-state-metrics"}[5m])))
              > 0.01
            for: 15m
            labels:
              severity: critical
          - alert: KubeStateMetricsWatchErrors
            annotations:
              description: kube-state-metrics is experiencing errors at an elevated rate in watch operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all.
              summary: kube-state-metrics is experiencing errors in watch operations.
            expr: |
              (sum(rate(kube_state_metrics_watch_total{job="kube-state-metrics",result="error"}[5m]))
                /
              sum(rate(kube_state_metrics_watch_total{job="kube-state-metrics"}[5m])))
              > 0.01
            for: 15m
            labels:
              severity: critical
          - alert: KubeStateMetricsShardingMismatch
            annotations:
              description: kube-state-metrics pods are running with different --total-shards configuration, some Kubernetes objects may be exposed multiple times or not exposed at all.
              summary: kube-state-metrics sharding is misconfigured.
            expr: |
              stdvar (kube_state_metrics_total_shards{job="kube-state-metrics"}) != 0
            for: 15m
            labels:
              severity: critical
          - alert: KubeStateMetricsShardsMissing
            annotations:
              description: kube-state-metrics shards are missing, some Kubernetes objects are not being exposed.
              summary: kube-state-metrics shards are missing.
            expr: |
              2^max(kube_state_metrics_total_shards{job="kube-state-metrics"}) - 1
                -
              sum( 2 ^ max by (shard_ordinal) (kube_state_metrics_shard_ordinal{job="kube-state-metrics"}) )
              != 0
            for: 15m
            labels:
              severity: critical
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

This `Rules` configuration was adapted from the rules and alerts contributed to the [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/blob/master/examples/prometheus-alerting-rules/alerts.yaml) repository. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured Kube State Metrics. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="kube-state-metrics", cluster="CLUSTER_NAME", namespace="gmp-public"}
         




## Install dashboards

Cloud Monitoring provides a library of sample dashboards for integrations. The sample library includes "Prometheus" dashboards, which you can install to view your data in the Google Cloud console.

Note that the **Kubernetes Cluster Prometheus Overview** dashboard requires [Node Exporter](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter) to be installed. The **Kubernetes Pod Prometheus Overview** dashboard requires [Node Exporter](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter) and [cAdvisor/Kubelet](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor) to be installed.

To install a dashboard from the sample library, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Sample Library** tab.
  3. Choose the **Other** category.
  4. (Optional) To view a static preview of a dashboard without installing it, click **Preview**.
  5. Select the dashboards you want to install, then click download **Import**.



For more information about installing dashboards, see [ Installing sample dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates#install-templates).

## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
