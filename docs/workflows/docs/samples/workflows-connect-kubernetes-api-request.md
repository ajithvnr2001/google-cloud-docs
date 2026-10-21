---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-kubernetes-api-request/
title: Connector for Kubernetes API \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:49.885989+00:00
---

# Connector for Kubernetes API  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-kubernetes-api-request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Kubernetes API Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access the Kubernetes API within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access Kubernetes API objects using a connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api)



## Code sample

### YAML
    
    
    main:
      steps:
        - create_deployment:
            call: gke.request
            args:
              cluster_id: "CLUSTER_NAME"
              project: "PROJECT_ID"
              location: "LOCATION"
              method: "POST"
              path: "/apis/apps/v1/namespaces/default/deployments"
              body:
                kind: Deployment
                metadata:
                  name: nginx-deployment
                  labels:
                    app: nginx
                spec:
                  replicas: 3
                  selector:
                    matchLabels:
                      app: nginx
                  template:
                    metadata:
                      labels:
                        app: nginx
                    spec:
                      containers:
                        - name: nginx
                          image: nginx:1.14.2
                          ports:
                            - containerPort: 80
            result: result
        - returnResult:
            return: '${result}'

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
