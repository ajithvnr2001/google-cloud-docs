---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-pubsub-deployment/
title: Pub/Sub deployment \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:13.272094+00:00
---

# Pub/Sub deployment  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-pubsub-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Pub/Sub deployment Stay organized with collections  Save and categorize content based on your preferences. 

Kubernetes deployment for Pub/Sub sample application.

## Code sample

### YAML
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: pubsub
    spec:
      selector:
        matchLabels:
          app: pubsub
      template:
        metadata:
          labels:
            app: pubsub
        spec:
          containers:
          - name: subscriber
            image: us-docker.pkg.dev/google-samples/containers/gke/pubsub-sample:v2

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
