---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/gkectl/
title: gkectl \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:31.560681+00:00
---

# gkectl  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/gkectl/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  gkectl Stay organized with collections  Save and categorize content based on your preferences. 

You can use the `gkectl` command line interface for a for a variety tasks, including the following:

  * Generate a template for a cluster configuration file.
  * Validate a cluster configuration file.
  * Prepare a vSphere environment.
  * Create a cluster.
  * Upgrade a cluster.
  * Update a cluster.
  * Resize a cluster.
  * Diagnose cluster issues.



To list all commands:
    
    
    gkectl help
    

To get help for a specific command:
    
    
    gkectl COMMAND --help
    

## Environment variable for the admin cluster kubeconfig file

Several `gkectl` commands require the path of the admin cluster kubeconfig file. You can specify the path by exporting a `GKECTL_KUBECONFIG` environment variable. For example:
    
    
    export GKECTL_KUBECONFIG=/path/to/my-admin-cluster-kubeconfig
    

If you do not export the `GKECTL_KUBECONFIG` environment variable, then you must use the `--kubeconfig` flag when you run the command.

## Download `gkectl`

For information on downloading `gkectl`, see [Downloads](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/downloads).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
