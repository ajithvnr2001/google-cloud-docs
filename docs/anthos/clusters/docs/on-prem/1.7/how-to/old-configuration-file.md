---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/old-configuration-file/
title: Old cluster configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:10.074847+00:00
---

# Old cluster configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/old-configuration-file/

**Version 1.7**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.7 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/overview)



Send feedback 

#  Old cluster configuration file Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the two versions of configuration files use in Google Distributed Cloud.

In Google Distributed Cloud version 1.4, the configuration files changed substantially. The new files are called v1 configuration files. The configuration files that were used in Google Distributed Cloud versions earlier than 1.4 are called v0 configuration files.

As of version 1.7 of Google Distributed Cloud, the v0 configuration files are no longer supported.

## Converting configuration files

To convert a v0 configuration file to a v1 admin cluster configuration file:
    
    
    gkectl create-config admin --from [OLD_CONFIG_PATH] --config [OUTPUT_PATH]
    

where:

  * [OLD_CONFIG_PATH] is the path of your v0 configuration file.

  * [OUTPUT_PATH] is a path of your choice for the generated v1 admin cluster configuration file. If you omit this flag, `gkectl` names the file `admin-cluster.yaml` and puts it in the current directory.




To convert a v0 configuration file to a v1 user cluster configuration file:
    
    
    gkectl create-config cluster --from [OLD_CONFIG_PATH] --config [OUTPUT_PATH]
    

  * [OLD_CONFIG_PATH] is the path of your v0 configuration file.

  * [OUTPUT_PATH] is a path of your choice for the generated v1 user cluster configuration file. If you omit this flag, `gkectl` names the file `user-cluster.yaml` and puts it in the current directory.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
