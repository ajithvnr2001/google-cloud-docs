---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor/
title: cAdvisor/Kubelet \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:34.737653+00:00
---

# cAdvisor/Kubelet  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  cAdvisor/Kubelet Stay organized with collections  Save and categorize content based on your preferences. 

The Kubelet exposes metrics about itself as well as cAdvisor metrics about containers running on its node. 

Cloud Monitoring offers an out-of-the-box managed collection of cAdvisor/Kubelet metrics as an alternative to configuring this integration. The fully managed collection option provides an opinionated, curated set of metrics that is set up in new clusters by default. 

The integration described in this document offers all of the cAdvisor metrics, many of which you are unlikely to need and will probably want to filter out, and it is available to Google Kubernetes Engine and other Kubernetes environments. The managed set of cAdvisor/Kubelet metrics has been curated to provide only the most useful metrics and is available only to GKE. For more information, see [ Package: cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#cadvisor-kubelet-package).

If you set up collection of cAdvisor metrics as described in this document, the configuration supersedes the GKE-managed cAdvisor configuration. The configuration described in this document enables a superset of the managed cAdvisor metrics.

When you use the approach described in this document, instead of using a custom PodMonitoring config, you can configure [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) to automatically scrape cAdvisor and Kubelet metrics by editing the [OperatorConfig](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#operatorconfig). You can install manifests by copying them to a local file and then running `kubectl apply -f FILE_NAME`. You can also [install manifests by using Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape).

  1. Open the OperatorConfig resource for editing:
         
         kubectl -n gmp-public edit operatorconfig config
         

  2. Add the following `collection` section, shown in bold type, to the resource:
         
         apiVersion: monitoring.googleapis.com/v1
         kind: OperatorConfig
         metadata:
           namespace: gmp-public
           name: config
         **collection:
           kubeletScraping:
             interval: 30s**
         

  3. Save the file and close the editor.




After a short time, the Kubelet metric endpoints will be scraped and the metrics become available for querying in Managed Service for Prometheus.

Kubelet scraping comes with some default filters that exclude deprecated metrics. You can use the **Metrics Management** page to [exclude any other unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics).

## Tips for advanced cAdvisor setups

If you self-deploy cAdvisor or provide advanced configuration to your Kubelet with cAdvisor, be aware that additional labels can be attached by using advanced [cAdvisor settings](https://github.com/google/cadvisor/blob/master/docs/runtime_options.md).

Particularly avoid attaching Kubernetes container labels or environment variables to your metrics, and if you do, strictly control these labels by using an allowlist pattern (for example, using PodMonitoring's [`metricRelabeling` section](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#filter-metrics)).

Controlling the number of labels added to your metrics can help you avoid exceeding the limit on the [number of labels](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#descriptor-label-limit).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
