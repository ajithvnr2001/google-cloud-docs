---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-container/
title: Connector for Kubernetes Engine \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:25.095215+00:00
---

# Connector for Kubernetes Engine  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access a Kubernetes Engine container-based application within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Kubernetes Engine API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Google Kubernetes Engine (GKE) connector:
    # Create a GKE cluster and then delete it
    # Each step waits until the long-running operation of creating or deleting the cluster completes
    # Expected output: "SUCCESS"
    main:
      params: []
      steps:
        - init:
            assign:
              - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - cluster_zone: "us-central1-a"
              - cluster_id: "CLUSTER_ID"  # replace CLUSTER_ID placeholder
              - cluster_full_name: ${"projects/" + project_id + "/locations/" + cluster_zone + "/clusters/" + cluster_id}
        - create_gke_cluster:
            call: googleapis.container.v1.projects.zones.clusters.create
            args:
              projectId: ${project_id}
              zone: ${cluster_zone}
              body:
                cluster:
                  name: ${cluster_id}
                  initial_node_count: 1
                parent: ${"projects/" + project_id + "/locations/" + cluster_zone}
        - assert_running:
            call: assert_cluster_status
            args:
              expected_status: "RUNNING"
              project_id: ${project_id}
              cluster_zone: ${cluster_zone}
              cluster_id: ${cluster_id}
              cluster_full_name: ${cluster_full_name}
        - delete_gke_cluster:
            call: googleapis.container.v1.projects.zones.clusters.delete
            args:
              projectId: ${project_id}
              zone: ${cluster_zone}
              clusterId: ${cluster_id}
              name: ${cluster_full_name}
        - the_end:
            return: "SUCCESS"
    
    assert_cluster_status:
      params:
        [expected_status, project_id, cluster_zone, cluster_id, cluster_full_name]
      steps:
        - get_cluster:
            call: googleapis.container.v1.projects.zones.clusters.get
            args:
              projectId: ${project_id}
              zone: ${cluster_zone}
              clusterId: ${cluster_id}
              name: ${cluster_full_name}
            result: cluster
        - compare:
            switch:
              - condition: ${cluster.status == expected_status}
                next: end
        - fail:
            raise: ${"Expected VM status is " + expected_status + ". Received " + cluster.status + " instead."}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
