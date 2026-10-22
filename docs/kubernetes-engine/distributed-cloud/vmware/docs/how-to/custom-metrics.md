---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/custom-metrics/
title: Enabling user-defined custom metrics for Horizontal Pod autoscaling \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:51.837876+00:00
---

# Enabling user-defined custom metrics for Horizontal Pod autoscaling  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/custom-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Enabling user-defined custom metrics for Horizontal Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure user-defined metrics for Horizontal Pod autoscaling (HPA) in Google Distributed Cloud.

This page is for Admins, Architects, and Operators who optimize systems architecture and resources to ensure the lowest total cost of ownership for their company or business unit, and plan capacity and infrastructure needs. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Deploy Prometheus and Metrics Adapter

In this section you deploy [Prometheus](https://prometheus.io/) to scrape user-defined metrics and the [prometheus-adapter](https://github.com/kubernetes-sigs/prometheus-adapter) to fulfil the Kubernetes Custom Metrics API with Prometheus as its backend.

Save the following manifests to a file named `custom-metrics-adapter.yaml`.

#### Manifest file content for Prometheus and Metrics Adapter
    
    
    # Copyright 2018 Google Inc
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: stackdriver-prometheus
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: stackdriver-prometheus
      namespace: kube-system
    rules:
    - apiGroups:
      - ""
      resources:
      - nodes
      - services
      - endpoints
      - pods
      verbs:
      - get
      - list
      - watch
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: stackdriver-prometheus
      namespace: kube-system
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: stackdriver-prometheus
    subjects:
    - kind: ServiceAccount
      name: stackdriver-prometheus
      namespace: kube-system
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: stackdriver-prometheus-app
      namespace: kube-system
      labels:
        app: stackdriver-prometheus-app
    spec:
      clusterIP: "None"
      ports:
        - name: http
          port: 9090
          protocol: TCP
          targetPort: 9090
      sessionAffinity: ClientIP
      selector:
        app: stackdriver-prometheus-app
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: stackdriver-prometheus-app
      namespace: kube-system
      labels:
        app: stackdriver-prometheus-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: stackdriver-prometheus-app
      template:
        metadata:
          labels:
            app: stackdriver-prometheus-app
        spec:
          serviceAccount: stackdriver-prometheus
          containers:
          - name: prometheus-server
            image: prom/prometheus:v2.45.0
            args:
            - "--config.file=/etc/prometheus/config/prometheus.yaml"
            - "--storage.tsdb.path=/data"
            - "--storage.tsdb.retention.time=2h"
            ports:
            - name: prometheus
              containerPort: 9090
            readinessProbe:
              httpGet:
                path: /-/ready
                port: 9090
              periodSeconds: 5
              timeoutSeconds: 3
              # Allow up to 10m on startup for data recovery
              failureThreshold: 120
            livenessProbe:
              httpGet:
                path: /-/healthy
                port: 9090
              periodSeconds: 5
              timeoutSeconds: 3
              failureThreshold: 6
            resources:
              requests:
                cpu: 250m
                memory: 500Mi
            volumeMounts:
            - name: config-volume
              mountPath: /etc/prometheus/config
            - name: stackdriver-prometheus-app-data
              mountPath: /data
          volumes:
          - name: config-volume
            configMap:
              name: stackdriver-prometheus-app
          - name: stackdriver-prometheus-app-data
            emptyDir: {}
          terminationGracePeriodSeconds: 300
          nodeSelector:
            kubernetes.io/os: linux
    ---
    apiVersion: v1
    data:
      prometheus.yaml: |
        global:
          scrape_interval: 1m
        rule_files:
        - /etc/config/rules.yaml
        - /etc/config/alerts.yaml
        scrape_configs:
        - job_name: prometheus-io-endpoints
          kubernetes_sd_configs:
          - role: endpoints
          relabel_configs:
          - action: keep
            regex: true
            source_labels:
            - __meta_kubernetes_service_annotation_prometheus_io_scrape
          - action: replace
            regex: (.+)
            source_labels:
            - __meta_kubernetes_service_annotation_prometheus_io_path
            target_label: __metrics_path__
          - action: replace
            regex: (https?)
            source_labels:
            - __meta_kubernetes_service_annotation_prometheus_io_scheme
            target_label: __scheme__
          - action: replace
            regex: ([^:]+)(?::\d+)?;(\d+)
            replacement: $1:$2
            source_labels:
            - __address__
            - __meta_kubernetes_service_annotation_prometheus_io_port
            target_label: __address__
          - action: replace
            source_labels:
            - __meta_kubernetes_namespace
            target_label: namespace
          - action: replace
            source_labels:
            - __meta_kubernetes_pod_name
            target_label: pod
          - action: keep
            regex: (.+)
            source_labels:
            - __meta_kubernetes_endpoint_port_name
        - job_name: prometheus-io-services
          kubernetes_sd_configs:
          - role: service
          metrics_path: /probe
          params:
            module:
            - http_2xx
          relabel_configs:
          - action: replace
            source_labels:
            - __address__
            target_label: __param_target
          - action: replace
            replacement: blackbox
            target_label: __address__
          - action: keep
            regex: true
            source_labels:
            - __meta_kubernetes_service_annotation_prometheus_io_probe
          - action: replace
            source_labels:
            - __meta_kubernetes_namespace
            target_label: namespace
          - action: replace
            source_labels:
            - __meta_kubernetes_pod_name
            target_label: pod
        - job_name: prometheus-io-pods
          kubernetes_sd_configs:
          - role: pod
          relabel_configs:
          - action: keep
            regex: true
            source_labels:
            - __meta_kubernetes_pod_annotation_prometheus_io_scrape
          - action: replace
            regex: (.+)
            source_labels:
            - __meta_kubernetes_pod_annotation_prometheus_io_path
            target_label: __metrics_path__
          - action: replace
            regex: ([^:]+)(?::\d+)?;(\d+)
            replacement: $1:$2
            source_labels:
            - __address__
            - __meta_kubernetes_pod_annotation_prometheus_io_port
            target_label: __address__
          - action: replace
            source_labels:
            - __meta_kubernetes_namespace
            target_label: namespace
          - action: replace
            source_labels:
            - __meta_kubernetes_pod_name
            target_label: pod
    kind: ConfigMap
    metadata:
      name: stackdriver-prometheus-app
      namespace: kube-system
    ---
    
    # The main section of custom metrics adapter.
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      name: custom-metrics-apiserver
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: custom-metrics:system:auth-delegator
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: system:auth-delegator
    subjects:
    - kind: ServiceAccount
      name: custom-metrics-apiserver
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: custom-metrics-server-resources
    rules:
    - apiGroups:
      - custom.metrics.k8s.io
      resources: ["*"]
      verbs: ["*"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: custom-metrics-resource-reader
    rules:
    - apiGroups:
      - ""
      resources:
      - nodes
      - namespaces
      - pods
      - services
      verbs:
      - get
      - watch
      - list
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: custom-metrics-resource-reader
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: custom-metrics-resource-reader
    subjects:
    - kind: ServiceAccount
      name: custom-metrics-apiserver
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: custom-metrics-auth-reader
      namespace: kube-system
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: extension-apiserver-authentication-reader
    subjects:
    - kind: ServiceAccount
      name: custom-metrics-apiserver
      namespace: kube-system
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: adapter-config
      namespace: kube-system
    data:
      config.yaml: |
        rules:
        default: false
          # fliter all metrics
        - seriesQuery: '{pod=~".+"}'
          seriesFilters: []
          resources:
            # resource name is mapped as it is. ex. namespace -> namespace
            template: <<.Resource>>
          name:
            matches: ^(.*)$
            as: ""
          # Aggregate metric on resource level
          metricsQuery: sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: custom-metrics-apiserver
      name: custom-metrics-apiserver
      namespace: kube-system
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: custom-metrics-apiserver
      template:
        metadata:
          labels:
            app: custom-metrics-apiserver
          name: custom-metrics-apiserver
        spec:
          serviceAccountName: custom-metrics-apiserver
          containers:
          - name: custom-metrics-apiserver
            resources:
              requests:
                cpu: 15m
                memory: 20Mi
              limits:
                cpu: 100m
                memory: 150Mi
            image: registry.k8s.io/prometheus-adapter/prometheus-adapter:v0.11.0
            args:
            - /adapter
            - --cert-dir=/var/run/serving-cert
            - --secure-port=6443
            - --prometheus-url=http://stackdriver-prometheus-app.kube-system.svc:9090/
            - --metrics-relist-interval=1m
            - --config=/etc/adapter/config.yaml
            ports:
            - containerPort: 6443
            volumeMounts:
            - name: serving-cert
              mountPath: /var/run/serving-cert
            - mountPath: /etc/adapter/
              name: config
              readOnly: true
          nodeSelector:
            kubernetes.io/os: linux
          volumes:
          - name: serving-cert
            emptyDir:
              medium: Memory
          - name: config
            configMap:
              name: adapter-config
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: custom-metrics-apiserver
      namespace: kube-system
    spec:
      ports:
      - port: 443
        targetPort: 6443
      selector:
        app: custom-metrics-apiserver
    ---
    apiVersion: apiregistration.k8s.io/v1
    kind: APIService
    metadata:
      name: v1beta1.custom.metrics.k8s.io
    spec:
      service:
        name: custom-metrics-apiserver
        namespace: kube-system
      group: custom.metrics.k8s.io
      version: v1beta1
      insecureSkipTLSVerify: true
      groupPriorityMinimum: 100
      versionPriority: 100
    ---
    apiVersion: apiregistration.k8s.io/v1
    kind: APIService
    metadata:
      name: v1beta2.custom.metrics.k8s.io
    spec:
      service:
        name: custom-metrics-apiserver
        namespace: kube-system
      group: custom.metrics.k8s.io
      version: v1beta2
      insecureSkipTLSVerify: true
      groupPriorityMinimum: 100
      versionPriority: 100
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: hpa-controller-custom-metrics
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: custom-metrics-server-resources
    subjects:
    - kind: ServiceAccount
      name: horizontal-pod-autoscaler
      namespace: kube-system
    

Create the Deployment and the Service:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f custom-metrics-adapter.yaml
    

The next step is to annotate the user application for metrics collection.

## Annotate a user application for metrics collection

To annotate a user application to be scraped and the logs sent to Cloud Monitoring, you must add corresponding `annotations` to the metadata for the service, Pod, and endpoints.
    
    
      metadata:
        name: "example-monitoring"
        namespace: "default"
        annotations:
          prometheus.io/scrape: "true"
          prometheus.io/path: "" - Overriding metrics path (default "/metrics")
      

## Deploy an example user application

In this section, you deploy a sample application with both logs and Prometheus-compatible metrics.

  1. Save the following Service and Deployment manifests to a file named `my-app.yaml`. Notice that the Service has the annotation `prometheus.io/scrape: "true"`:
         
         kind: Service
         apiVersion: v1
         metadata:
           name: "example-monitoring"
           namespace: "default"
           annotations:
             prometheus.io/scrape: "true"
         spec:
           selector:
             app: "example-monitoring"
           ports:
             - name: http
               port: 9090
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: "example-monitoring"
           namespace: "default"
           labels:
             app: "example-monitoring"
         spec:
           replicas: 1
           selector: 
             matchLabels:
               app: "example-monitoring"
           template: 
             metadata: 
               labels:
                 app: "example-monitoring"
             spec:
               containers:
               - image: gcr.io/google-samples/prometheus-dummy-exporter:v0.2.0
                 name: prometheus-example-exporter
                 command:
                 - ./prometheus-dummy-exporter
                 args:
                 - --metric-name=example_monitoring_up
                 - --metric-value=1
                 - --port=9090
                 resources:
                   requests:
                     cpu: 100m
         

  2. Create the Deployment and the Service:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f my-app.yaml
         




## Use the custom metrics in HPA

Deploy the HPA object to use the metric exposed in the previous step. See [Autoscaling on multiple metrics and custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) for more advanced information about different type of custom metrics.
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: example-monitoring-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: example-monitoring
      minReplicas: 1
      maxReplicas: 5
      metrics:
      - type: Pods
        pods:
          metric:
            name: example_monitoring_up
          target:
            type: AverageValue
            averageValue: 20
    

The Pods type metric has a default metric selector for the labels of the target Pods, which is how kube-controller-manager works. In this example, you cna query the example_monitoring_up metric with a selector of `{matchLabels: {app: example-monitoring}}` as they are available in the target Pods. Any other selector specified is added to the list. To avoid the default selector, you canremove any labels on the target Pod or use the Object type metric.

## Check that the user-defined application metrics are used by HPA

Check that the user defined application metrics are used by HPA:
    
    
    kubectl --kubeconfig=USER_CLUSTER_KUBECONFIG describe hpa example-monitoring-hpa

The output will look like this:
    
    
      Name:               example-monitoring-hpa
      Namespace:          default
      Labels:             
      Annotations:        autoscaling.alpha.kubernetes.io/conditions:
                            [{"type":"AbleToScale","status":"True","lastTransitionTime":"2023-08-23T22:07:24Z","reason":"ReadyForNewScale","message":"recommended size...
                          autoscaling.alpha.kubernetes.io/current-metrics: [{"type":"Pods","pods":{"metricName":"example_monitoring_up","currentAverageValue":"1"}}]
                          autoscaling.alpha.kubernetes.io/metrics: [{"type":"Pods","pods":{"metricName":"example_monitoring_up","targetAverageValue":"20"}}]
      CreationTimestamp:  Wed, 23 Aug 2023 22:07:09 +0000
      Reference:          Deployment/example-monitoring
      Min replicas:       1
      Max replicas:       5
      Deployment pods:    1 current / 1 desired
      

## Costs

Using custom metrics for HPA does not incur any additional Cloud Monitoring charges. The Pods for enabling custom metrics consume additional CPU and memory based on the amount of metrics it scrapes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
