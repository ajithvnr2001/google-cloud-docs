---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/external-targets-probe/
title: Configure external probe targets \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:36.123737+00:00
---

# Configure external probe targets  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/external-targets-probe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure external probe targets Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure external targets for probing in Google Distributed Cloud (GDC) air-gapped. The system discovers and monitors these targets by reading a specific Kubernetes ConfigMap.

## Before you begin

To apply a ConfigMap to the `gpc-system` namespace, you must have access to the cluster and permissions to create or modify ConfigMaps in that namespace. You also need the path to the kubeconfig file for the Management API server cluster. External target probes can only be configured in root-admin or org-admin clusters.

## Understanding ConfigMap details

The prober looks for a ConfigMap with the following characteristics:

  * **Name:** `pnet-external-probe-targets-config`
  * **Namespace:** `gpc-system`
  * **Data Key:** The ConfigMap must contain a key named `targets.yaml` within its `data` field. The value associated with this key must be a YAML string defining the probe targets.



## Understanding `targets.yaml` structure

The `targets.yaml` content must be a YAML list of objects. Each object represents a single external probe target and follows this structure:
    
    
    - name: <unique-probe-name>
      spec:
        target: <hostname-or-ip>
        probeType: <TCP or ICMP>
        port: <port-number> # Required for TCP, ignored for ICMP
        interval: <duration> # e.g., "10s", "1m"
        timeout: <duration>  # Optional, e.g., "5s". Defaults to 5s if not set.
    

Here's a breakdown of the fields:

  * **`name` (string):** A unique identifier for this specific probe target.
  * **`spec`:** Defines the probing parameters: 
    * **`target` (string):** The hostname or IP address of the external target to probe.
    * **`probeType` (string):** The type of probe to perform. Supported values are: 
      * `TCP`: Performs a TCP connection attempt to the specified `target` and `port`.
      * `ICMP`: Sends an ICMP echo request (ping) to the `target`.
    * **`port` (int32):** The port number to use for TCP probes. This field is required when `probeType` is `TCP` and is ignored for `ICMP` probes.
    * **`interval` (string):** The frequency at which the probe should run. This must be a valid Kubernetes `metav1.Duration` string (e.g., `"5s"`, `"1m30s"`).
    * **`timeout` (string, optional):** The maximum time to wait for a single probe attempt to complete. This is also a `metav1.Duration` string. If not specified, a default timeout of `5s` is used.



## Create and apply the ConfigMap

To create or update the ConfigMap, follow these steps:

  1. Create a YAML file named `external-probe-configmap.yaml`. The following example defines three probe targets:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: pnet-external-probe-targets-config
           namespace: gpc-system
         data:
           targets.yaml: |
             - name: "example-tcp-server"
               spec:
                 target: "192.0.2.1"
                 probeType: "TCP"
                 port: 80
                 interval: "10s"
                 timeout: "3s"
             - name: "example-icmp-host"
               spec:
                 target: "8.8.8.8"
                 probeType: "ICMP"
                 interval: "30s"
             - name: "another-tcp-service"
               spec:
                 target: "my-service.example.com"
                 probeType: "TCP"
                 port: 443
                 interval: "1m"
                 # Using default timeout of 5s
         

  2. Apply the ConfigMap to your cluster:
         
         kubectl apply -f external-probe-configmap.yaml -n gpc-system --kubeconfig=MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the Management API server.




The prober automatically detects changes to this ConfigMap and starts, stops, or updates probe processes based on the defined targets.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
