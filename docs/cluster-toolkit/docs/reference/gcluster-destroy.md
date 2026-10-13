---
url: https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy/
title: gcluster destroy \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:35.206200+00:00
---

# gcluster destroy  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Reference ](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster)



Send feedback 

#  gcluster destroy Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

`gcluster destroy` \- destroys all resources in a Cluster Toolkit deployment directory.

## SYNOPSIS
    
    
    gcluster destroy DEPLOYMENT_DIRECTORY [FLAGS]
    

## DESCRIPTION

The `gcluster destroy` command destroys all resources managed by the specified deployment directory. It typically tears down infrastructure in the reverse order of creation. For more information about deploying resources, see [`gcluster deploy`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy).

## FLAGS

  * `-a`, `--artifacts ARTIFACTS_DIR`: The directory where deployment artifacts are stored. This directory is automatically configured if not set.
  * `--auto-approve`: Automatically approve destruction without prompting.
  * `--skip`: A comma-separated list of group names to skip during destruction.
  * `--only`: A comma-separated list of group names to destroy exclusively. This value can't be used with `--skip`.
  * `--robust`: Perform a robust destroy, including firewall rule cleanup and retries on GKE cluster reachability issues.



## EXAMPLES

To destroy all resources in a deployment directory:
    
    
    gcluster destroy ./my-deployment
    

To automatically approve and destroy resources without prompting:
    
    
    gcluster destroy ./my-deployment --auto-approve
    

To destroy only a specific group within the deployment directory:
    
    
    gcluster destroy ./my-deployment --only=primary-cluster
    

To perform a robust destroy, cleaning up residual firewall rules:
    
    
    gcluster destroy ./my-deployment --robust --auto-approve
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
