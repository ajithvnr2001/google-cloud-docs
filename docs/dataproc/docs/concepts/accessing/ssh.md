---
url: https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh/
title: Connect using SSH to a cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:41:42.380047+00:00
---

# Connect using SSH to a cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Connect using SSH to a cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can use SSH to connect to a Managed Service for Apache Spark cluster if SSH access to the cluster is enabled when you create the cluster.

See [Cluster web interfaces](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/cluster-web-interfaces) to establish a connection to a web interface running on a cluster master node.

## Enable or disable SSH access to a cluster

The ability to use SSH to connect to a cluster is enabled by default for image versions prior to `3.1` and is disabled by default for image versions `3.1` and later. The default behavior can be changed when creating clusters using image versions `2.3.30` and later.

### Google Cloud CLI

When creating a cluster with the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command, pass the `--enable-ssh` flag to enable SSH access or the `--no-ssh` flag to disable SSH access to the cluster.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --enable-ssh | --no-ssh \
        ... other args
    

### REST API

As part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request, set the [`IdentityConfig.enableSsh`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#identityconfig) field to `true` to enable and `false` to disable SSH access to the cluster.

## Connect to a cluster using SSH

### Console

  1. In the Google Cloud console, go to the [**VM Instances**](https://console.cloud.google.com/compute/instances) page.
  2. In the list of virtual machine instances, click **SSH** in the row of the Managed Service for Apache Spark VM instance that you want to connect to. ![A list of VM instances showing the SSH button for a cluster node.](https://docs.cloud.google.com/static/managed-spark/images/ssh-select-master.png)



A browser window opens in your home directory on the node.
    
    
    Connected, host fingerprint: ssh-rsa ...
    Linux cluster-1-m 3.16.0-0.bpo.4-amd64 ...
    ...
    user@cluster-1-m:~$
    

You can also connect using SSH to a Managed Service for Apache Spark cluster node from the **VM Instances** tab on the Managed Service for Apache Spark **Cluster details** page in the Google Cloud console.![The Cluster details page showing the VM Instances tab.](https://docs.cloud.google.com/static/managed-spark/images/dataproc-ssh.png)

### Google Cloud CLI

Run the [gcloud compute ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) command in a local terminal window or from [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) to connect using SSH to a cluster VM node.
    
    
    gcloud compute ssh VM_NAME\
        --zone=ZONE \
        --project=PROJECT_ID
    

Example (the default name for the master node is the cluster name followed by an `-m` suffix):
    
    
    gcloud compute ssh cluster-1-m \
      --zone=us-central-1-a \
      --project=my-project-id
    ...
    Linux cluster-1-m 4.9.0-8-amd64 #1 SMP Debian 4.9.110-3+deb9u6...
    ...
    user@cluster-1-m:~$
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
