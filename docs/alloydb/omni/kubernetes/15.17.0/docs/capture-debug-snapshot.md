---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/capture-debug-snapshot/
title: Capture a debug snapshot \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:23.877005+00:00
---

# Capture a debug snapshot  |  AlloyDB Omni using the container orchestrator: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/capture-debug-snapshot/

This page documents AlloyDB Omni version **15.17.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)



Send feedback 

#  Capture a debug snapshot Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/capture-debug-snapshot)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/capture-debug-snapshot)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/capture-debug-snapshot)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/capture-debug-snapshot)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/capture-debug-snapshot)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/capture-debug-snapshot)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/capture-debug-snapshot)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/capture-debug-snapshot)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/capture-debug-snapshot)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/capture-debug-snapshot)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/capture-debug-snapshot)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/capture-debug-snapshot)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/capture-debug-snapshot)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/capture-debug-snapshot)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/capture-debug-snapshot)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/capture-debug-snapshot)

To help you diagnose and debug issues, you can create a snapshot of the container orchestrator environment running AlloyDB Omni operator. Include this snapshot when you open a case with [Google Support](https://cloud.google.com/support?e=48754805). 

## Capture a debug snapshot

  1. Make sure that you have the [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) utility installed and configured.

  2. Open the [AlloyDB Omni GitHub sample repository](https://github.com/GoogleCloudPlatform/alloydb-omni-samples/tree/main/debug-snapshot) and download the `snapshot.sh` script.

  3. Run the script.
         
         ./snapshot.sh DB_CLUSTER_NAME DB_CLUSTER_NAMESPACE

Make the following replacements:

     * `DB_CLUSTER_NAME`: the name of your database cluster.
     * `DB_CLUSTER_NAMESPACE`: the name of your database cluster's namespace.

The script creates a new `snapshot` folder.

  4. Review the snapshot for sensitive information before you submit it. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
