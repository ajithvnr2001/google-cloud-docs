---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tf-serving/
title: TensorFlow Serving \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:27.994318+00:00
---

# TensorFlow Serving  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tf-serving/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  TensorFlow Serving Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from TensorFlow Serving. This document shows you how to do the following: 

  * Set up TF Serving to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [TF Serving documentation](https://www.tensorflow.org/tfx/serving/serving_config#monitoring_configuration) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about TensorFlow Serving, see [TF Serving](https://github.com/tensorflow/serving). For information about setting up TF Serving on Google Kubernetes Engine, see the GKE [ guide for TF Serving](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/online-ml-inference). 

## Prerequisites

To collect metrics from TF Serving by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).



TF Serving exposes Prometheus-format metrics when the `--monitoring_config_file` flag is used to specify a file containing a MonitoringConfig protocol buffer.

The following is an example of a MonitoringConfig protocol buffer:
    
    
    prometheus_config {
      enable: true,
      path: "/monitoring/prometheus/metrics"
    }
    

If you are following the Google Kubernetes Engine set-up guide, [Serve a model with a single GPU in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/online-ml-inference), then the MonitoringConfig protocol buffer is defined as part of the default setup.

If you are setting up TF Serving yourself, then do the following to specify the MonitoringConfig protocol buffer:

  1. Create a file named `monitoring_config.txt` containing the MonitoringConfig protocol buffer in the model directory, before uploading the directory to the Cloud Storage bucket.

  2. Upload the model directory to the Cloud Storage bucket:
         
         gcloud storage cp MODEL_DIRECTORY gs://CLOUD_STORAGE_BUCKET_NAME --recursive
         

  3. Set the environment variable `PATH_TO_MONITORING_CONFIG` to the path of the uploaded `monitoring_config.txt` file, for example:
         
         export PATH_TO_MONITORING_CONFIG=/data/tfserve-model-repository/monitoring_config.txt
         

  4. Add the following flag and value to the container's command in your container's deployment YAML file:
         
         "--monitoring_config=$PATH_TO_MONITORING_CONFIG"
         

For example, your command might look like the following:
         
         command: [ "tensorflow_model_server", "--model_name=$MODEL_NAME", "--model_base_path=/data/tfserve-model-repository/$MODEL_NAME", "--rest_api_port=8000", "--monitoring_config_file=$PATH_TO_MONITORING_CONFIG" ]
         




## Modify the TF Serving configuration

Modify the TF Serving configuration as shown in the following example:
    
    
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
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: tfserve-deployment
      labels:
        app: tfserve-server
    spec:
      selector:
        matchLabels:
          app: tfserve
      replicas: 1
      template:
        metadata:
          labels:
            app: tfserve
          annotations:
            gke-gcsfuse/volumes: 'true'
        spec:
          nodeSelector:
            cloud.google.com/gke-accelerator: nvidia-l4
          containers:
            - name: tfserve-server
              image: 'tensorflow/serving:2.13.1-gpu'
              command:
                - tensorflow_model_server
                - '--model_name=$MODEL_NAME'
                - '--model_base_path=/data/tfserve-model-repository/$MODEL_NAME'
                - '--rest_api_port=8000'
    +           - '--monitoring_config_file=$PATH_TO_MONITORING_CONFIG'
              ports:
                - name: http
                  containerPort: 8000
                - name: grpc
                  containerPort: 8500
              resources:
                ...
              volumeMounts:
                - name: gcs-fuse-csi-vol
                  mountPath: /data
                  readOnly: false
          serviceAccountName: $K8S_SA_NAME
          volumes:
            - name: gcs-fuse-csi-vol
              csi:
                driver: gcsfuse.csi.storage.gke.io
                readOnly: false
                volumeAttributes:
                  bucketName: $GSBUCKET
                  mountOptions: implicit-dirs
    

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

To verify that TF Serving is emitting metrics on the expected endpoints, do the following: 

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 8000
         

  2. Access the endpoint `localhost:8000/monitoring/prometheus/metrics` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to TF Serving in the same namespace.

You can use the following PodMonitoring configuration:
    
    
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
    kind: PodMonitoring
    metadata:
      name: tfserve
      labels:
        app.kubernetes.io/name: tfserve
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: 8000
        scheme: http
        interval: 30s
        path: /monitoring/prometheus/metrics
      selector:
        matchLabels:
          app: tfserve
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured TF Serving. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="tfserve", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **TensorFlow Serving Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **TensorFlow Serving Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the TensorFlow Serving integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
