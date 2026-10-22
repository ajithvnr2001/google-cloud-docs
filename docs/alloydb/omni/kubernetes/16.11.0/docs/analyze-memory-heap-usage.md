---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/analyze-memory-heap-usage/
title: Analyze AlloyDB Omni Kubernetes operator memory heap usage \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:28:44.039075+00:00
---

# Analyze AlloyDB Omni Kubernetes operator memory heap usage  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/analyze-memory-heap-usage/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)



Send feedback 

#  Analyze AlloyDB Omni Kubernetes operator memory heap usage Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/analyze-memory-heap-usage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/analyze-memory-heap-usage)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/analyze-memory-heap-usage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/analyze-memory-heap-usage)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/analyze-memory-heap-usage)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/analyze-memory-heap-usage)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/analyze-memory-heap-usage)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/analyze-memory-heap-usage)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/analyze-memory-heap-usage)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/analyze-memory-heap-usage)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/analyze-memory-heap-usage)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/analyze-memory-heap-usage)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/analyze-memory-heap-usage)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/analyze-memory-heap-usage)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/analyze-memory-heap-usage)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/analyze-memory-heap-usage)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/analyze-memory-heap-usage)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/analyze-memory-heap-usage)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/analyze-memory-heap-usage)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/analyze-memory-heap-usage)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/analyze-memory-heap-usage)

This document describes how you can get a snapshot of the memory heap of AlloyDB Omni operator to help diagnose and debug potential memory issues. Use the following steps to get a memory heap for analysis: 

  1. Determine which AlloyDB Omni operator deployment to analyze. The AlloyDB Omni operator includes two deployments, and you can analyze the memory heap for either one. To identify the two deployments, run the following command:
         
         kubectl get deployment -n alloydb-omni-system

The output shows you the two deployments in the `alloydb-omni-system` namespace:

     * `fleet-controller-manager`
     * `local-controller-manager`

You can get the memory heap of either deployment. For demonstration purposes, these steps show how to get the memory heap for the `local-controller-manager` deployment.

  2. Turn on memory analysis by specifying an available port to use. After the port is specified, the pod restarts. To specify an available port, use the `pprof-address` argument in the deployment:

     1. Open the deployment in a text editor by running the following command:
            
            kubectl edit -n alloydb-omni-system deploy local-controller-manager

     2. Specify the port in the `args` of the `container` section in the template `spec`:
            
            apiVersion: apps/v1
            kind: Deployment
            spec:
              ...
              template:
              ...
                spec:
                  containers:
                  - args
                    - --pprof-address=:PORT
            

**Important:** To prevent malicious use of the feature, turn off memory analysis by removing this port argument when you finish analyzing the memory heap.
     3. Save the deployment file. After you save the deployment file, the pod restarts.

  3. Wait for the pod to restart before continuing to the next step.

To make sure the pod restarted, run the following command:
         
         kubectl get pod -n alloydb-omni-system

Verify that the output value in the pod's `STATUS` column is `Running` and the output value in its `AGE` column is a short duration. For example, if the `STATUS` column is `Running` and the value in the `AGE` column is `50s`, then the pod has been running for 50 seconds after the restart.

  4. Turn on port forwarding using the following command:
         
         kubectl port-forward -n alloydb-omni-system DEPLOYMENT_POD_NAME PORT:PORT

Replace DEPLOYMENT_POD_NAME with the name of your deployment as it appears in the `NAME` column of the output of the following command:
         
         kubectl get pod -n alloydb-omni-system

  5. In a different terminal, run the following command to create a file with a snapshot of the memory heap of the deployment:
         
         curl http://localhost:PORT/debug/pprof/heap > heap.out

  6. Save the `heap.out` file and use it to view the memory heap of the AlloyDB Omni operator deployment you chose to analyze.

  7. Turn off memory analysis by removing the `pprof-address` argument with the port you used from the deployment:

     1. Open the deployment in a text editor:
            
            kubectl edit -n alloydb-omni-system deploy local-controller-manager

     2. Remove the port `--pprof-address=:PORT` line from the `args` of the `container` section in template `spec` that you added earlier.




## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/run-connect)
  * [Generate and diagnose AlloyDB Omni dump files](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/manage-dump-files)
  * [Learn about automatic memory management](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/automatic-memory-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
