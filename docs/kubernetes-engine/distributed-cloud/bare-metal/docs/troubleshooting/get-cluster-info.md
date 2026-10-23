---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/get-cluster-info/
title: Retrieve cluster information \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:56.789882+00:00
---

# Retrieve cluster information  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/get-cluster-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Retrieve cluster information Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the `bmctl get` command to retrieve important configuration and credential information for your existing clusters. This information can be helpful in troubleshooting cluster problems.

## Get cluster configuration details

After you create [admin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/admin-cluster-creation), [hybrid](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/hybrid-cluster-creation), [standalone](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/standalone-cluster-creation), or [user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/user-cluster-creation) clusters you can use the `bmctl get config` command to retrieve the cluster configuration details.

Use the following command to retrieve all custom resources for a self-managing cluster, such as an admin cluster:
    
    
    bmctl get config --cluster CLUSTER_NAME \
        --kubeconfig ADMIN_KUBECONFIG_PATH
    

Replace the following:

  * `CLUSTER_NAME`: the name of the target cluster.

  * `ADMIN_KUBECONFIG_PATH`: the path to the admin cluster `kubeconfig` file.




Use the following command to retrieve all custom resources for a user cluster:

Note that `bmctl` supports the use of `--kubeconfig` as an alias for the `--admin-kubeconfig` flag.
    
    
    bmctl get config --cluster CLUSTER_NAME  \
        --admin-kubeconfig ADMIN_KUBECONFIG_PATH
    

Replace the following:

  * `CLUSTER_NAME`: the name of the target user cluster.

  * `ADMIN_KUBECONFIG_PATH`: the path to the admin cluster `kubeconfig` file.




For both commands, the custom resources are written to a YAML file named: `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-TIMESTAMP.yaml`. The TIMESTAMP in the filename indicates the date and time the file was created.

The YAML file produced by the `bmctl get config` command looks similar to the following example:
    
    
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
     name: cluster-admin1
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
     name: admin1
     namespace: cluster-admin1
    spec:
     clusterNetwork:
       services:
         cidrBlocks:
         - 10.96.0.0/20
       pods:
         cidrBlocks:
         - 192.168.0.0/16
     controlPlane:
       nodePoolSpec:
         nodes:
         - address: 172.18.0.13
     loadBalancer:
       mode: bundled
       ports:
         controlPlaneLBPort: 6443
       vips:
         controlPlaneVIP: 172.18.0.254
     storage:
       lvpShare:
         path: /mnt/localpv-share/
         storageclassname: standard
         numpvundersharedpath: 5
       lvpNodeMounts:
         path: /mnt/localpv-disk
         storageclassname: node-disk
     authentication:
       oidc:
         issuerURL: https://accounts.google.com
         kubectlRedirectURL: http://localhost:9879/callback
         clientID: 611080206796-9qq355g2q1coed5t78ckfmm1c6ini3et.apps.googleusercontent.com
         clientSecret: FTPbx3INYJcxBSQhMRlbk3tX
         username: email
         scopes: email
         extraParams: prompt=consent,access_type=offline
     clusterOperations:
       projectID: baremetal-test
       location: us-central1
     type: admin
     anthosBareMetalVersion: 0.0.0
     bypassPreflightCheck: false
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
     name: nodepool1
     namespace: cluster-admin1
    spec:
     clusterName: admin1
     nodes:
     - address: 172.18.0.9
    

## Get cluster credentials

Use the `bmctl get credentials` command to retrieve credentials for a given user cluster.

To retrieve all custom resources for a user cluster, use the following command:

Note that `bmctl` supports the use of `--kubeconfig` as an alias for the `--admin-kubeconfig` flag.
    
    
    bmctl get credentials --cluster CLUSTER_NAME  \
        --admin-kubeconfig ADMIN_KUBECONFIG_PATH
    

Replace the following:

  * CLUSTER_NAME: the name of the target user cluster.

  * ADMIN_KUBECONFIG_PATH: the path to the admin cluster `kubeconfig` file.




The cluster's credentials are written to a file, `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-TIMESTAMP-kubeconfig`. The TIMESTAMP in the filename indicates the date and time the file was created.

Because this file contains authentication credentials for your cluster, you should store it in a secure location with restricted access.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
