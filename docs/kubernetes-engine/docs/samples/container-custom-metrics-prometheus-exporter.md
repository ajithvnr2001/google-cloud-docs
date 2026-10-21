---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-prometheus-exporter/
title: Custom metrics prometheus exporter source code \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:28:26.179814+00:00
---

# Custom metrics prometheus exporter source code  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-prometheus-exporter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Custom metrics prometheus exporter source code Stay organized with collections  Save and categorize content based on your preferences. 

Source code for custom prometheus exporter to Cloud Monitoring.

## Code sample

### Go

To authenticate to GKE, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    metric := prometheus.NewGauge(
    	prometheus.GaugeOpts{
    		Name: *metricName,
    		Help: "Custom metric",
    	},
    )
    prometheus.MustRegister(metric)
    metric.Set(float64(*metricValue))
    
    http.Handle("/metrics", promhttp.Handler())
    log.Printf("Starting to listen on :%d", *port)
    err := http.ListenAndServe(fmt.Sprintf(":%d", *port), nil)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
