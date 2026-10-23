---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/resizing/
title: Troubleshoot cluster resizing \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:18.357491+00:00
---

# Troubleshoot cluster resizing  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/resizing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot cluster resizing Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with resizing clusters.

## Resizing a user cluster fails

If a resizing of a user cluster fails, complete the following steps:

  1. Find the names of the MachineDeployments and the Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machinedeployments --all-namespaces
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machines --all-namespaces
         

  2. Describe a MachineDeployment to view its logs:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machinedeployment MACHINE_DEPLOYMENT_NAME
         

  3. Check for errors on newly-created Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machine MACHINE_NAME
         




## No addresses can be allocated for cluster resize

This issue occurs if there are not enough IP addresses available to resize a user cluster.

`kubectl describe machine` displays the following error:
    
    
    Events:
    Type     Reason  Age                From                    Message
    ----     ------  ----               ----                    -------
    Warning  Failed  9s (x13 over 56s)  machineipam-controller  ipam: no addresses can be allocated
    

To resolve this issue, [Allocate more IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster) for the cluster. Then, delete the affected Machine:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete machine MACHINE_NAME
    

Google Distributed Cloud creates a new Machine and assigns it one of the newly available IP addresses.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
