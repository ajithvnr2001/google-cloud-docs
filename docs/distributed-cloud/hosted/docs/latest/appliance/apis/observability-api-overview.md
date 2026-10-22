---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/observability-api-overview/
title: Observability API overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:21.633695+00:00
---

# Observability API overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/observability-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Observability API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Observability API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM) for provisioning and managing logging and monitoring resources.

Use the Observability API to manage the lifecycle of Observability services in a given organization or custom project. The lifecycle of Observability services includes operations such as install, upgrade, and uninstall. You must deploy a custom resource to your project according to the Observability service you want to manage.

Many Observability services are available automatically for a provisioned project, for example, logging, monitoring, and alerting.

## Service endpoint

The following URLs are the API endpoints for the Observability KRM API:

  * **Logging group:**
        
        https://MANAGEMENT_API_SERVER_ENDPOINT/apis/logging.gdc.goog/v1
        

  * **Monitoring group:**
        
        https://MANAGEMENT_API_SERVER_ENDPOINT/apis/monitoring.gdc.goog/v1
        

  * **Observability group:**
        
        https://MANAGEMENT_API_SERVER_ENDPOINT/apis/observability.gdc.goog/v1
        




Replace `MANAGEMENT_API_SERVER_ENDPOINT` with the endpoint of the Management API server.

## Discovery document

Use the `kubectl proxy --port=8001` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at one of the following URLs:

  * `http://127.0.0.1:8001/apis/logging.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/monitoring.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/observability.gdc.goog/v1`



## Example resources

This section contains example resources that use the Observability KRM API.

### Logging group

The following is an example of a `LoggingTarget` custom resource to collect logs from specific services on the `project-1` project:
    
    
    # Configures a log scraping job
    apiVersion: logging.gdc.goog/v1
    kind: LoggingTarget
    metadata:
      # Choose a namespace that matches the namespace of the workload pods
      namespace: project-1
      name: my-service-logging-target
    spec:
      # Choose a matching pattern that identifies the pods for this job
      # Optional
      # Relationship between different selectors: 'AND'
      selector:
        # The clusters to collect logs from.
        # The default configuration is to collect logs from all clusters.
        # The relationship between different clusters is an 'OR' relationship.
        # For example, the value '["admin", "system"]' indicates to consider
        # the admin cluster 'OR' the system cluster.
        # Optional
        matchClusters:
        - cluster-1
        - cluster-2
    
        # The pod name prefixes to collect logs from.
        # The Observability platform scrapes all pods with names
        # that start with the specified prefixes.
        # The values must contain '[a-z0-9-]' characters only.
        # The relationship between different list elements is an 'OR' relationship.
        # Optional
        matchPodNames:
          - pod-1
          - pod-2
    
        # The container name prefixes to collect logs from.
        # The Observability platform scrapes all containers with names
        # that start with the specified prefixes.
        # The values must contain '[a-z0-9-]' characters only.
        # The relationship between different list elements is an 'OR' relationship.
        # Optional
        matchContainerNames:
          - container-1
          - container-2
    
      # Choose the predefined parser for log entries.
      # Use parsers to map the log output to labels and extract fields.
      # Specify the log format.
      # Optional
      # Options: klog_text, klog_json, klogr, gdch_json, json
      parser: klog_text
    
      # Specify an access level for log entries.
      # The default value is 'ao'.
      # Optional
      # Options: ao, pa, io
      logAccessLevel: ao
    
      # Specify a service name to be applied as a label
      # For user workloads consider this field as a workload name
      # Required
      serviceName: service-name
    
      # The additional static fields to apply to log entries.
      # The field is a key-value pair, where the field name is the key and
      # the field value is the value.
      # Optional
      additionalFields:
        app: workload2
        key: value
    

### Monitoring group

The following is an example of a `MonitoringTarget` custom resource to collect metrics from workloads on the `project-1` project:
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    metadata:
      # Choose the same namespace as the workload pods
      namespace: project-1
      name: string
    spec:
      # Choose matching pattern that identifies pods for this job
      # Optional
      # Relationship between different selectors: AND
      selector:
        # Choose clusters to consider for this job
        # Optional
        # List
        # Default: All clusters applicable to this project.
        # Relationship between different list elements: OR
        matchClusters:
          - string
    
        # Choose pod-labels to consider for this job
        # Optional: Map of key-value pairs.
        # Default: No filtering by label.
        # Relationship between different pairs: AND
        matchLabels:
          key1: value1
    
        # Choose annotations to consider for this job
        # Optional: Map of key-value pairs
        # Default: No filtering by annotation
        # Relationship between different pairs: AND
        matchAnnotations:
          key1: value1
    
      # Configure the endpoint exposed for this job
      podMetricsEndpoints:
        # Choose port either via static value or annotation
        # Optional
        # Annotation takes priority
        # Default: static port 80
        port:
          value: integer
          annotation: string
    
        # Choose path either via static value or annotation
        # Optional
        # Annotation takes priority
        # Default: static path /metrics
        path:
          value: string
          annotation: string
    
        # Choose scheme either via static value (http or https) or annotation
        # Optional
        # Annotation takes priority
        # Default: static scheme http
        scheme:
          value: string
          annotation: string
    
        # Choose the frequency to scrape the metrics endpoint defined in podMetricsEndpoints
        # Optional
        # Default: 60s
        scrapeInterval: string
    
        # Dynamically rewrite the label set of a target before it gets scraped.
        # https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config
        # Optional
        # Default: No filtering by label
        metricsRelabelings:
          - sourceLabels:
              - string
            separator: string
            regex: string
            action: string
            targetLabel: string
            replacement: string
    

### Observability group

The following is an example of the `ObservabilityPipeline` custom resource to update the storage size for dashboards in the `platform-obs` project namespace:
    
    
    # Configure observability pipeline
    apiVersion: observability.gdc.goog/v1
    kind: ObservabilityPipeline
    metadata:
      # Don't change the namespace or name.
      namespace: platform-obs
      name: observability-config
    spec:
      ...
      monitoring:
        grafana:
          storageSize: 1Gi # Configure the new storage size for dashboards in the project.
        ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
