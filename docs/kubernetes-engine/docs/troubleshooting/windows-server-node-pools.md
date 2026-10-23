---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/windows-server-node-pools/
title: Troubleshoot Windows Server node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:23.496561+00:00
---

# Troubleshoot Windows Server node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/windows-server-node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot Windows Server node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When running [Windows Server node pools in Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows), you might encounter issues such as Pods failing to start, errors pulling Windows container images, network connectivity problems, or nodes that fail to start.

Use this document to diagnose and resolve these common issues and keep your Windows-based applications running reliably.

This information is important for Platform admins and operators who manage GKE clusters with Windows node pools, and for Application developers who deploy and run Windows-based applications on GKE. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For more general guidance, see the Kubernetes documentation on [debugging Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/#debugging-pods) and [Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/#debugging-services).

## Containerd node issues

For information about resolving issues if you use a containerd node image, see [Issues on Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime#issues-windows-server-node-pools).

## Windows Pods fail to start

Incompatibilities between the base image and Windows Server host OS versions can prevent Pods from starting.

#### Symptoms

  * Windows Pods fail to start.
  * The node reports the `NotReady` status.



#### Cause

The container image was built on an older base Windows image that is incompatible with the host node's Windows Server version.

#### Resolution

Build your container images by using [base Windows images](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-base-images) that include Windows Updates from March 2020 or later. For more information about Microsoft container compatibility, see [Microsoft's documentation for the February 2020 Windows Server container incompatibility issue](https://support.microsoft.com/en-us/help/4542617/you-might-encounter-issues-when-using-windows-server-containers-with-t).

## Image pull errors

Windows Server container images are often significantly larger than Linux images, which can lead to timeouts.

#### Symptoms

  * Error messages such as `Failed to pull image` or `context cancelled`.
  * Pods display the `ErrImagePull` status.



#### Cause

Windows Server container images, and the individual layers they are composed of, can be large. Their size can cause the `kubelet` agent to time out and fail when it downloads and extracts the container layers.

#### Resolution

To resolve these image pull failures, try the following solutions:

  * **Increase node CPU** : container extraction is executed in parallel across cores, so [machine types](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--machine-type) with more cores reduce the overall pull time.
  * **Optimize image layers** : to improve Docker layer caching and make image pull retries more likely to succeed, break your application layers into smaller layers. For more information, see [Images and layers](https://docs.docker.com/engine/storage/drivers/#images-and-layers) in the Docker storage driver documentation.
  * **Use manual pulls** : connect to your Windows Server nodes and manually execute the `docker pull` command on container images before creating your Pods.



For more general advice, see [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

## Image family reached end of life

GKE periodically deprecates older Windows Server image families when vendor support ends. This deprecation blocks the creation of node pools with those images.

#### Symptoms

When creating a node pool with a Windows image, you receive an error similar to the following:
    
    
    WINDOWS_SAC image family for 1.18.20-gke.501 has reached end of life, newer
    versions are still available.
    

#### Cause

The selected Windows Server image family is no longer supported in GKE.

#### Resolution

Choose a Windows image that is available and supported. You can find the support end date for GKE Windows node images by using the `gcloud container get-server-config` command as described in [Mapping GKE and Windows versions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#version_mapping).

## Timeout during node pool creation

Initializing a large number of Windows Server nodes simultaneously can cause timeouts.

#### Symptoms

Node pool creation operations time out before completing.

#### Cause

Node pool creation can time out if you are creating a large number of nodes (for example, 500) and it's the first node pool in the cluster that uses a Windows Server image.

#### Resolution

Reduce the initial node count when creating the node pool. After the node pool is created, you can increase the number of nodes.

## Windows nodes become `NotReady` with error: `PLEG is not healthy`

Rapidly scheduling multiple Windows containers on a single node can overwhelm the Pod Lifecycle Event Generator (PLEG).

#### Symptoms

  * Windows nodes enter a `NotReady` status.
  * Events or logs display a `PLEG is not healthy` error message.



#### Cause

A [known Kubernetes issue](https://github.com/kubernetes/kubernetes/issues/88153) occurs when multiple Pods are started very rapidly on a single Windows node.

#### Resolution

To recover from PLEG failures and prevent reoccurrence:

  * Restart the affected Windows Server node.
  * Limit Windows Pod creation to no more than one Pod every 30 seconds.



## Inconsistent `TerminationGracePeriod`

Differences between Windows container shutdown timers and Kubernetes grace period settings can cause containers to be terminated unexpectedly.

#### Symptoms

Containers are force-terminated by Windows before the duration configured in the `TerminationGracePeriodSeconds` field expires.

#### Cause

The internal Windows system timeout for the container differs from the grace period specified in the Kubernetes Pod manifest.

#### Resolution

Modify the Windows container timeout by editing container-local registry keys at image build time. Align the `TerminationGracePeriodSeconds` field in your Pod manifest accordingly.

## Network connectivity problems

Maximum Transmission Unit (MTU) size mismatches between Windows Server container networking and Google Cloud networks can cause dropped packets.

#### Symptoms

Applications running inside Windows Server containers experience network connectivity failures or dropped packets.

#### Cause

Windows Server container networking often assumes a network MTU of `1500`, which is incompatible with Google Cloud's MTU of `1460`.

#### Resolution

Configure both the container network interface MTU and the Windows Server node network interface MTU value to `1460` or lower. For more information, see [known issues for Windows containers](https://docs.cloud.google.com/compute/docs/containers#mtu_failures) in the Compute Engine documentation.

## Node startup issues

New Windows Server instances can fail to complete initialization scripts or register with the control plane.

#### Symptoms

Windows Server nodes fail to initialize or fail to join the cluster.

#### Cause

Errors during the node initialization prevent the node from starting or joining the cluster.

#### Resolution

To identify which startup errors could be causing the issue, review the node's [serial port](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) output:
    
    
    gcloud compute instances get-serial-port-output NODE_NAME \
        --zone=COMPUTE_ZONE
    

Replace the following:

  * `NODE_NAME`: the name of the node.
  * `COMPUTE_ZONE`: the [compute zone](https://docs.cloud.google.com/compute/docs/zones#available) for the node.



## Intermittently unreachable Services in Windows nodes with cluster running 1.24 or earlier

On clusters running version 1.24 or earlier, restarting the `kube-proxy` component creates temporary network routing delays while Host Network Service (HNS) Load Balancer rules are reprocessed.

#### Symptoms

Services are intermittently unreachable from Pods running on Windows nodes.

#### Cause

For GKE clusters running version 1.24 or earlier, if an event restarts the `kube-proxy` component on a Windows node—for example, node startup, node upgrade, or manual restart—the component must sync and re-create all HNS Load Balancer rules. If the cluster has a high number of these rules, there can be a significant delay in processing them, lasting around 30 seconds per rule. During this sync delay, Services are intermittently unreachable from Pods running on that node. For more information, see the [original issue in GitHub](https://github.com/kubernetes/kubernetes/issues/109162).

#### Resolution

Upgrade your cluster control plane to version 1.25 or later. This behavior is substantially improved in newer versions, as detailed in the [pull request in GitHub](https://github.com/kubernetes/kubernetes/pull/109124).

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
