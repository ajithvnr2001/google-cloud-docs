---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-prometheus-horizontal-pod-autoscaler/
title: Custom metrics prometheus exporter HPA \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:45.845159+00:00
---

# Custom metrics prometheus exporter HPA  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-prometheus-horizontal-pod-autoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Custom metrics prometheus exporter HPA Stay organized with collections  Save and categorize content based on your preferences. 

Horizontal Pod Autoscaler for prometheus exporter to Cloud Monitoring.

## Code sample

### YAML
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: custom-metrics-gmp-hpa
      namespace: default
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: custom-metrics-gmp
      minReplicas: 1
      maxReplicas: 5
      metrics:
      - type: Pods
        pods:
          metric:
            name: prometheus.googleapis.com|custom_prometheus|gauge
          target:
            type: AverageValue
            averageValue: 20

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
