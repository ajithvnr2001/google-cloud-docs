---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability/
title: Set up GKE Dataplane V2 observability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:02.897461+00:00
---

# Set up GKE Dataplane V2 observability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-dpv2-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Set up GKE Dataplane V2 observability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows how to configure Google Kubernetes Engine (GKE) clusters with GKE Dataplane V2 observability, starting in GKE versions **1.32** or later. For more information on the benefits and requirements of GKE Dataplane V2 observability, see [About GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).

**Note:** You can enable GKE Dataplane V2 metrics and GKE Dataplane V2 observability tools independent of each other.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Configure GKE Dataplane V2 metrics

To collect metrics, you must configure GKE Dataplane V2 metrics. You can configure GKE Dataplane V2 metrics when you create a cluster or update a cluster running with GKE Dataplane V2. You can enable or disable GKE Dataplane V2 metrics using the gcloud CLI.

We recommend enabling GKE Dataplane V2 metrics and Google Cloud Managed Service for Prometheus on your GKE cluster. Once both are enabled, GKE Dataplane V2 metrics are sent to Google Cloud Managed Service for Prometheus.

### Create an Autopilot cluster with GKE Dataplane V2 metrics enabled

When you create new GKE Autopilot clusters, GKE enables GKE Dataplane V2 metrics by default on the cluster without requiring a specific flag.

To use the GKE Autopilot cluster GKE Dataplane V2 metrics with Google Cloud Managed Service for Prometheus, configure the `ClusterPodMonitoring` resource to scrape the metrics and send them to Google Cloud Managed Service for Prometheus.

  1. Create a `ClusterPodMonitoring` manifest:
         
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
         
         apiVersion: monitoring.googleapis.com/v1
         kind: ClusterPodMonitoring
         metadata:
           name: advanced-datapath-observability-metrics
         spec:
           selector:
             matchLabels:
               k8s-app: cilium
           endpoints:
           - port: flowmetrics
             interval: 60s
             metricRelabeling:
             # only keep denormalized pod flow metrics
             - sourceLabels: [__name__]
               regex: 'pod_flow_(ingress|egress)_flows_count'
               action: keep
             # extract pod name
             - sourceLabels: [__name__, destination]
               regex: 'pod_flow_ingress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${2}'
               targetLabel: pod_name
               action: replace
             - sourceLabels: [__name__, source]
               regex: 'pod_flow_egress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${2}'
               targetLabel: pod_name
               action: replace
             # extract workload name by removing 2 last "-XXX" parts
             - sourceLabels: [pod_name]
               regex: '([a-zA-Z0-9-\.]+)((-[a-zA-Z0-9\.]+){2})'
               replacement: '${1}'
               targetLabel: workload_name
               action: replace
             # extract workload name by removing one "-XXX" part when pod name has only 2 parts (eg. daemonset)
             - sourceLabels: [pod_name]
               regex: '([a-zA-Z0-9\.]+)((-[a-zA-Z0-9\.]+){1})'
               replacement: '${1}'
               targetLabel: workload_name
               action: replace
             # extract pod namespace
             - sourceLabels: [__name__, destination]
               regex: 'pod_flow_ingress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${1}'
               targetLabel: namespace_name
               action: replace
             - sourceLabels: [__name__, source]
               regex: 'pod_flow_egress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${1}'
               targetLabel: namespace_name
               action: replace
             # extract remote workload name
             - sourceLabels: [__name__, source]
               regex: 'pod_flow_ingress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${2}'
               targetLabel: remote_workload
               action: replace
             - sourceLabels: [__name__, destination]
               regex: 'pod_flow_egress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${2}'
               targetLabel: remote_workload
               action: replace
             # extract remote workload namespace
             - sourceLabels: [__name__, source]
               regex: 'pod_flow_ingress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${1}'
               targetLabel: remote_namespace
               action: replace
             - sourceLabels: [__name__, destination]
               regex: 'pod_flow_egress_flows_count;([a-zA-Z0-9-\.]+)/([a-zA-Z0-9-\.]+)'
               replacement: '${1}'
               targetLabel: remote_namespace
               action: replace
             # default remote workload class to "pod"
             - replacement: 'pod'
               targetLabel: remote_class
               action: replace
             # extract remote workload class from reserved identity
             - sourceLabels: [__name__, source]
               regex: 'pod_flow_ingress_flows_count;reserved:([^/]*)'
               replacement: '${1}'
               targetLabel: remote_class
               action: replace
             - sourceLabels: [__name__, destination]
               regex: 'pod_flow_egress_flows_count;reserved:([^/]*)'
               replacement: '${1}'
               targetLabel: remote_class
               action: replace
           targetLabels:
             metadata: []
         

  2. Apply the `ClusterPodMonitoring` manifest:
         
         kubectl apply -f ClusterPodMonitoring.yaml
         


**Note:** By default, Google Cloud Managed Service for Prometheus is not configured to collect GKE Dataplane V2 metrics on Autopilot clusters. After you configure the `ClusterPodMonitoring` resource, GKE charges an [ingestion cost](https://cloud.google.com/stackdriver/pricing) based on the metric volume.

### Create a Standard cluster with GKE Dataplane V2 metrics enabled

To enable GKE Dataplane V2 metrics, create a cluster with the `--enable-dataplane-v2-metrics` flag:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-dataplane-v2 \
        --enable-ip-alias \
        --enable-managed-prometheus \
        --enable-dataplane-v2-metrics
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.



The `--enable-managed-prometheus` flag instructs GKE to use the metrics with Google Cloud Managed Service for Prometheus.

### Enable GKE Dataplane V2 metrics on an existing cluster

To enable GKE Dataplane V2 metrics on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-dataplane-v2-metrics
    

Replace `CLUSTER_NAME` with the name of your cluster.

### Disable GKE Dataplane V2 metrics

To disable GKE Dataplane V2 metrics:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --disable-dataplane-v2-metrics
    

Replace `CLUSTER_NAME` with the name of your cluster.

## Configure GKE Dataplane V2 observability tools

You can use a private endpoint to access the GKE Dataplane V2 observability troubleshooting tools. To enable GKE Dataplane V2 observability tools, you must have a cluster configured with GKE Dataplane V2. You can enable GKE Dataplane V2 observability tools on a new cluster or an existing cluster.

### Create an Autopilot cluster with observability enabled

To create a GKE Autopilot cluster with GKE Dataplane V2 observability enabled:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-dataplane-v2-flow-observability \
        --location COMPUTE_LOCATION
    

Replace the following: * **`CLUSTER_NAME`** : the name of your cluster. * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.

### Create a Standard cluster with observability enabled

To create a GKE Standard cluster with GKE Dataplane V2 observability enabled:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-dataplane-v2 \
        --enable-ip-alias \
        --enable-dataplane-v2-flow-observability \
        --location COMPUTE_LOCATION
    

Replace the following: * **`CLUSTER_NAME`** : the name of your cluster. * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.

### Enable GKE Dataplane V2 observability tools on an existing cluster

To enable GKE Dataplane V2 observability on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-dataplane-v2-flow-observability \
        --location COMPUTE_LOCATION
    

Replace the following:

  * **`CLUSTER_NAME`** : the name of your cluster.
  * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.



### Disable GKE Dataplane V2 observability tools

To disable GKE Dataplane V2 observability tools on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --disable-dataplane-v2-flow-observability
    

Replace `CLUSTER_NAME` with the name of your cluster.

## How to use Hubble CLI

Use the Hubble CLI tool on the cluster after you enable the GKE Dataplane V2 observability feature.

  1. Define alias for `hubble-cli` binary:
         
         alias hubble="kubectl exec -it -n gke-managed-dpv2-observability deployment/hubble-relay -c hubble-cli -- hubble"
         

  2. To check the Hubble status, with the GKE Dataplane V2 observability feature enabled, use the Hubble CLI in all Autopilot clusters:
         
         hubble status
         

  3. To view current traffic, use the Hubble CLI as follows:
         
         hubble observe
         


**Note:** This image is deployed as a single Pod deployment on Standard clusters that have GKE Dataplane V2 observability enabled. The deployed Pod has an IP address, port, and the TLS certificate of Hubble preconfigured. You don't need to specify them when you use the Hubble CLI.

## How to deploy the Hubble UI binary distribution

After GKE Dataplane V2 observability is enabled, you can deploy the open source Hubble UI.

  1. Enable observability in your GKE cluster:

     1. Create a GKE cluster with observability enabled:
            
            gcloud container clusters create-auto hubble-rc-auto \
                --location COMPUTE_LOCATION \
                --cluster-version VERSION \
                --enable-dataplane-v2-flow-observability
            

Replace the following:

        * **`VERSION`** : the version of your cluster.
        * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
     2. Alternatively, enable observability in an existing cluster:
            
            gcloud container clusters update CLUSTER_NAME \
                --location COMPUTE_LOCATION \
                --enable-dataplane-v2-flow-observability
            

Replace the following:

        * **`CLUSTER_NAME`** : the name of your cluster.
        * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  2. Configure `kubectl` to connect to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location COMPUTE_LOCATION
         

Replace

     * **`CLUSTER_NAME`** : the name of your cluster.
     * **`COMPUTE_LOCATION`** : the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.
  3. Deploy Hubble UI:
         
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
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: hubble-ui
           namespace: gke-managed-dpv2-observability
         ---
         kind: ClusterRole
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: hubble-ui
           labels:
             app.kubernetes.io/part-of: cilium
         rules:
           - apiGroups:
               - networking.k8s.io
             resources:
               - networkpolicies
             verbs:
               - get
               - list
               - watch
           - apiGroups:
               - ""
             resources:
               - componentstatuses
               - endpoints
               - namespaces
               - nodes
               - pods
               - services
             verbs:
               - get
               - list
               - watch
           - apiGroups:
               - apiextensions.k8s.io
             resources:
               - customresourcedefinitions
             verbs:
               - get
               - list
               - watch
           - apiGroups:
               - cilium.io
             resources:
               - "*"
             verbs:
               - get
               - list
               - watch
         ---
         kind: ClusterRoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: hubble-ui
           labels:
             app.kubernetes.io/part-of: cilium
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: hubble-ui
         subjects:
           - kind: ServiceAccount
             name: hubble-ui
             namespace: gke-managed-dpv2-observability
         ---
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: hubble-ui-nginx
           namespace: gke-managed-dpv2-observability
         data:
           nginx.conf: |
             server {
                 listen       8081;
                 # uncomment for IPv6
                 # listen       [::]:8081;
                 server_name  localhost;
                 root /app;
                 index index.html;
                 client_max_body_size 1G;
                 location / {
                     proxy_set_header Host $host;
                     proxy_set_header X-Real-IP $remote_addr;
                     # CORS
                     add_header Access-Control-Allow-Methods "GET, POST, PUT, HEAD, DELETE, OPTIONS";
                     add_header Access-Control-Allow-Origin *;
                     add_header Access-Control-Max-Age 1728000;
                     add_header Access-Control-Expose-Headers content-length,grpc-status,grpc-message;
                     add_header Access-Control-Allow-Headers range,keep-alive,user-agent,cache-control,content-type,content-transfer-encoding,x-accept-content-transfer-encoding,x-accept-response-streaming,x-user-agent,x-grpc-web,grpc-timeout;
                     if ($request_method = OPTIONS) {
                         return 204;
                     }
                     # /CORS
                     location /api {
                         proxy_http_version 1.1;
                         proxy_pass_request_headers on;
                         proxy_hide_header Access-Control-Allow-Origin;
                         proxy_pass http://127.0.0.1:8090;
                     }
                     location / {
                         # double `/index.html` is required here
                         try_files $uri $uri/ /index.html /index.html;
                     }
                 }
             }
         ---
         kind: Deployment
         apiVersion: apps/v1
         metadata:
           name: hubble-ui
           namespace: gke-managed-dpv2-observability
           labels:
             k8s-app: hubble-ui
             app.kubernetes.io/name: hubble-ui
             app.kubernetes.io/part-of: cilium
         spec:
           replicas: 1
           selector:
             matchLabels:
               k8s-app: hubble-ui
           template:
             metadata:
               labels:
                 k8s-app: hubble-ui
                 app.kubernetes.io/name: hubble-ui
                 app.kubernetes.io/part-of: cilium
             spec:
               securityContext:
                 fsGroup: 1000
                 seccompProfile:
                   type: RuntimeDefault
               serviceAccount: hubble-ui
               serviceAccountName: hubble-ui
               containers:
                 - name: frontend
                   image: quay.io/cilium/hubble-ui:v0.13.2
                   ports:
                     - name: http
                       containerPort: 8081
                   volumeMounts:
                     - name: hubble-ui-nginx-conf
                       mountPath: /etc/nginx/conf.d/default.conf
                       subPath: nginx.conf
                     - name: tmp-dir
                       mountPath: /tmp
                   terminationMessagePolicy: FallbackToLogsOnError
                   securityContext:
                     allowPrivilegeEscalation: false
                     readOnlyRootFilesystem: true
                     runAsUser: 1000
                     runAsGroup: 1000
                     capabilities:
                       drop:
                         - all
                 - name: backend
                   image: quay.io/cilium/hubble-ui-backend:v0.13.2
                   env:
                     - name: EVENTS_SERVER_PORT
                       value: "8090"
                     - name: FLOWS_API_ADDR
                       value: "hubble-relay.gke-managed-dpv2-observability.svc:443"
                     - name: TLS_TO_RELAY_ENABLED
                       value: "true"
                     - name: TLS_RELAY_SERVER_NAME
                       value: relay.gke-managed-dpv2-observability.svc.cluster.local
                     - name: TLS_RELAY_CA_CERT_FILES
                       value: /var/lib/hubble-ui/certs/hubble-relay-ca.crt
                     - name: TLS_RELAY_CLIENT_CERT_FILE
                       value: /var/lib/hubble-ui/certs/client.crt
                     - name: TLS_RELAY_CLIENT_KEY_FILE
                       value: /var/lib/hubble-ui/certs/client.key
                   ports:
                     - name: grpc
                       containerPort: 8090
                   volumeMounts:
                     - name: hubble-ui-client-certs
                       mountPath: /var/lib/hubble-ui/certs
                       readOnly: true
                   terminationMessagePolicy: FallbackToLogsOnError
                   securityContext:
                     allowPrivilegeEscalation: false
                     readOnlyRootFilesystem: true
                     runAsUser: 1000
                     runAsGroup: 1000
                     capabilities:
                       drop:
                         - all
               volumes:
                 - configMap:
                     defaultMode: 420
                     name: hubble-ui-nginx
                   name: hubble-ui-nginx-conf
                 - emptyDir: {}
                   name: tmp-dir
                 - name: hubble-ui-client-certs
                   projected:
                     # note: the leading zero means this number is in octal representation: do not remove it
                     defaultMode: 0400
                     sources:
                       - secret:
                           name: hubble-relay-client-certs
                           items:
                             - key: ca.crt
                               path: hubble-relay-ca.crt
                             - key: tls.crt
                               path: client.crt
                             - key: tls.key
                               path: client.key
         ---
         kind: Service
         apiVersion: v1
         metadata:
           name: hubble-ui
           namespace: gke-managed-dpv2-observability
           labels:
             k8s-app: hubble-ui
             app.kubernetes.io/name: hubble-ui
             app.kubernetes.io/part-of: cilium
         spec:
           type: ClusterIP
           selector:
             k8s-app: hubble-ui
           ports:
             - name: http
               port: 80
               targetPort: 8081
         

  4. Apply the `hubble-ui-132.yaml` manifest:
         
         kubectl apply -f hubble-ui-132.yaml
         

  5. Expose Service with port forwarding:
         
         kubectl -n gke-managed-dpv2-observability port-forward service/hubble-ui 16100:80 --address='0.0.0.0'
         

  6. Access the Hubble UI in your web browser:

<http://localhost:16100/>

**Note:** If you're using `kubectl` on VM, use `http://<VM_IP>:16100/` instead.



## What's next

  * [Observe your traffic using GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/observe-your-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
