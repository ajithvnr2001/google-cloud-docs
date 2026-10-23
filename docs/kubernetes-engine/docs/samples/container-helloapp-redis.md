---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-helloapp-redis/
title: Hello app redistribution deployment \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:49.877812+00:00
---

# Hello app redistribution deployment  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-helloapp-redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Hello app redistribution deployment Stay organized with collections  Save and categorize content based on your preferences. 

Kubernetes deployment for GKE Hello app redistibution.

## Code sample

### YAML
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: hello-web
      name: hello-web
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: hello-web
      template:
        metadata:
          labels:
            app: hello-web
        spec:
          # Pod anti affinity config START
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchExpressions:
                  - key: app
                    operator: In
                    values:
                    - hello-web
                topologyKey: kubernetes.io/hostname
          # Pod anti affinity config END
          containers:
          - image: us-docker.pkg.dev/google-samples/containers/gke/hello-app-redis:1.0  # change to the image name you built
            name: hello-app
            # Readiness probe config START
            readinessProbe:
              failureThreshold: 1
              httpGet:
                path: /healthz
                port: 8080
                scheme: HTTP
              initialDelaySeconds: 1
              periodSeconds: 1
              successThreshold: 1
              timeoutSeconds: 1

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
