---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction/
title: Introduction to exporter configuration \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:19.473656+00:00
---

# Introduction to exporter configuration  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Introduction to exporter configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can use exporters in conjunction with Google Cloud Managed Service for Prometheus to ingest metrics from third-party applications or from other components of the Prometheus infrastructure.

This set of documents includes configuration instructions for a number of common exporters. These instructions apply only if you are using [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, see the relevant exporter documentation for information about where to find the exporter's source repository.

This document is not an exhaustive list of the exporters supported by Managed Service for Prometheus. You can configure managed collection to scrape any exporter that you can set up. This list provides instructions for some of the most commonly used exporters.

## Application exporters

You can use application exporters with Managed Service for Prometheus to collect metrics from third-party applications. These exporters are typically set up as standalone workloads or as sidecars to your existing GKE deployments.

For more information, see the following documents:

  * [Aerospike](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/aerospike)
  * [Apache ActiveMQ](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/activemq)
  * [Apache Airflow](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/airflow)
  * [Apache CouchDB](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/couchdb)
  * [Apache Flink](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/flink)
  * [Apache Hadoop](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/hadoop)
  * [Apache HBase](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/hbase)
  * [Apache Kafka](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kafka)
  * [Apache Solr](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/solr)
  * [Apache Tomcat](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tomcat)
  * [Apache Web Server (httpd)](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/apache)
  * [Apache Zookeeper](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/zookeeper)
  * [Argo Workflows](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/argo-workflows)
  * [Elasticsearch](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/elasticsearch)
  * [etcd](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/etcd)
  * [HAProxy](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/haproxy)
  * [HashiCorp Consul](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/consul)
  * [GKE Inference Gateway](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/inference-optimized-gateway)
  * [Ingress NGINX Controller](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/ingress-nginx)
  * [Jenkins](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jenkins)
  * [Jetty](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetty)
  * [JetStream](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetstream)
  * [Kibana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kibana)
  * [KubeRay](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kuberay)
  * [llm-d](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/llm-d)
  * [Memcached](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/memcached)
  * [MongoDB](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/mongodb)
  * [MySQL](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/mysql)
  * [Nginx](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nginx)
  * [NVIDIA Triton](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-triton)
  * [PostgreSQL](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/postgresql)
  * [RabbitMQ](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/rabbitmq)
  * [Redis](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/redis)
  * [ScyllaDB](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/scylladb)
  * [SGLang](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/sglang)
  * [TensorFlow Serving](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tf-serving)
  * [Text Generation Inference](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tgi)
  * [TorchServe](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/torchserve)
  * [Varnish](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/varnish)
  * [Velero](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/velero)
  * [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm)



## Infrastructure exporters

The documents in this section contain example YAML manifests and other configuration that you can use to install and scrape infrastructure [exporters](https://prometheus.io/docs/instrumenting/exporters/). For example, to replicate the experience of using the [`kube-prometheus` repository](https://github.com/prometheus-operator/kube-prometheus), you can set up the [Kube State Metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics) and [Node Exporter](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter) exporters, and configure managed collection to scrape the [cAdvisor/Kubelet](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor) metrics.

For more information, see the following documents:

  * [GKE control-plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#control-plane-metrics)
  * [Hubble (GKE Dataplane V2)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability)
  * [Istio](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/istio)
  * [Kube State Metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics)
  * [cAdvisor/Kubelet](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor)
  * [Node Exporter](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/node_exporter)
  * [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-dcgm)
  * [Prometheus (self-monitoring)](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/prometheus)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
