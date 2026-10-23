---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-helloapp-ingress/
title: Hello app ingress \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:23.776271+00:00
---

# Hello app ingress  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-helloapp-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Hello app ingress Stay organized with collections  Save and categorize content based on your preferences. 

Kubernetes ingress resource for GKE Hello app.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure domain names with static IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip)



## Code sample

### YAML
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: helloweb
      annotations:
        kubernetes.io/ingress.global-static-ip-name: helloweb-ip
      labels:
        app: hello
    spec:
      defaultBackend:
        service:
          name: helloweb-backend
          port:
            number: 8080
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloweb-backend
      labels:
        app: hello
    spec:
      type: NodePort
      selector:
        app: hello
        tier: web
      ports:
      - port: 8080
        targetPort: 8080

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
