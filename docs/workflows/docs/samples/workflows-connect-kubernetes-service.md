---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-kubernetes-service/
title: Deploy a Kubernetes application using Workflows connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:47.528290+00:00
---

# Deploy a Kubernetes application using Workflows connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-kubernetes-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Deploy a Kubernetes application using Workflows connectors Stay organized with collections  Save and categorize content based on your preferences. 

Create a GKE cluster using the Kubernetes Engine API connector, and create a Kubernetes deployment and service using the Kubernetes API connector.

## Code sample

### YAML
    
    
    # This workflow demonstrates how to:
    # 1- Use the Kubernetes Engine API connector to create a GKE cluster.
    # 2- Use the Kubernetes API connector to create a Kubernetes deployment and
    # a service.
    
    main:
      steps:
        - init:
            assign:
              - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - cluster_location: "us-central1"
              - cluster_id: "workflows-cluster"
              - cluster_full_name: ${"projects/" + project_id + "/locations/" + cluster_location + "/clusters/" + cluster_id}
        - create_k8s_cluster:
            call: googleapis.container.v1.projects.locations.clusters.create
            args:
              body:
                cluster:
                  name: ${cluster_id}
                  initial_node_count: 1
                  autopilot:
                    enabled: true
              parent: ${"projects/" + project_id + "/locations/" + cluster_location}
        - assert_running:
            call: assert_cluster_status
            args:
              expected_status: "RUNNING"
              cluster_id: ${cluster_id}
              cluster_full_name: ${cluster_full_name}
        - create_deployment:
            call: gke.request
            args:
              project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              cluster_id: ${cluster_id}
              location: ${cluster_location}
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
            result: create_deployment_result
        - create_service:
            call: gke.request
            args:
              project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              cluster_id: ${cluster_id}
              location: ${cluster_location}
              method: "POST"
              path: "/api/v1/namespaces/default/services"
              body:
                kind: Service
                apiVersion: v1
                metadata:
                  name: nginx-service
                spec:
                  ports:
                  - name: http
                    port: 80
                    targetPort: 80
                  selector:
                    app: nginx
                  type: LoadBalancer
            result: create_service_result
        - return_multiple_values:
            return:
              create_deployment_result: ${create_deployment_result}
              create_service_result: ${create_service_result}
    
    assert_cluster_status:
      params:
        [expected_status, cluster_id, cluster_full_name]
      steps:
        - get_cluster:
            call: googleapis.container.v1.projects.locations.clusters.get
            args:
              clusterId: ${cluster_id}
              name: ${cluster_full_name}
            result: cluster
        - compare:
            switch:
              - condition: ${cluster.status == expected_status}
                next: end
        - fail:
            raise: ${"Expected VM status is " + expected_status + ". Got " + cluster.status + " instead."}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
