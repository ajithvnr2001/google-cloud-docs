---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods/
title: Run fault-tolerant workloads at lower costs in Spot Pods \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:34.938268+00:00
---

# Run fault-tolerant workloads at lower costs in Spot Pods  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run fault-tolerant workloads at lower costs in Spot Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page shows you how to run fault-tolerant workloads at lower costs by using _Spot Pods_ in your Google Kubernetes Engine (GKE) [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters.

## Overview

In GKE Autopilot clusters, Spot Pods are Pods that run on nodes backed by Compute Engine [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot). Spot Pods are priced lower than standard Autopilot Pods, but can be evicted by GKE whenever compute resources are required to run standard Pods.

Spot Pods are ideal for running stateless, batch, or fault-tolerant workloads at lower costs compared to running those workloads as standard Pods. To use Spot Pods in Autopilot clusters, modify the manifest with your Pod specification to request Spot Pods.

You can run Spot Pods on the default general-purpose Autopilot compute class as well as on specialized compute classes that meet specific hardware requirements. For information about these compute classes, refer to [Compute classes in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).

**Caution:** Spot Pods can be evicted at any time based on compute resource needs. Do not use Spot Pods to run critical workloads that might be sensitive to the ephemeral nature of Spot Pods.

To learn more about the pricing for Spot Pods in Autopilot clusters, see [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

Spot Pods are excluded from the [Autopilot Service Level Agreement](https://cloud.google.com/kubernetes-engine/sla).

## Benefits

Using Spot Pods in your Autopilot clusters provides you with the following benefits:

  * Lower pricing than running the same workloads on standard Autopilot Pods.
  * GKE automatically manages autoscaling and scheduling.
  * GKE automatically [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) nodes that run Spot Pods to ensure that standard Pods, like your critical workloads, aren't scheduled on those nodes. Your deployments that do use Spot Pods are automatically updated with a corresponding [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Request Spot Pods in your Autopilot workloads

To request that your Pods run as Spot Pods, use the `cloud.google.com/gke-spot=true` label in a [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) or [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) in your Pod specification. GKE automatically provisions nodes that can run Spot Pods.

**Note:** You cannot use the `cloud.google.com/gke-provisioning=spot` label, which is added to nodes running GKE version 1.25.5-gke.2500 or later, to schedule workloads on Spot Pods.

Spot Pods can be evicted and terminated at any time, for example if the compute resources are required elsewhere in Google Cloud. When a termination occurs, Spot Pods on the terminating node can request up to a 15 second grace period before termination, which is granted on a best effort basis, by specifying the `terminationGracePeriodSeconds` field.

The maximum grace period given to Spot Pods **during preemption** is 15 seconds. Requesting more than 15 seconds in `terminationGracePeriodSeconds` doesn't grant more than 15 seconds during preemption. On eviction, your Pod is sent the [SIGTERM signal](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination), and should take steps to shutdown during the grace period.

For Autopilot, GKE also automatically taints the nodes created to run Spot Pods and modifies those workloads with the corresponding toleration. The taint prevents standard Pods from being scheduled on nodes that run Spot Pods.

### Use a nodeSelector to require Spot Pods

You can use a nodeSelector to require Spot Pods in a Deployment. Add the `cloud.google.com/gke-spot=true` label to your Deployment, such as in the following example:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: pi
    spec:
      template:
        metadata:
          labels:
            app: pi
        spec:
          **nodeSelector :
            cloud.google.com/gke-spot: "true"
          terminationGracePeriodSeconds: 15**
          containers:
          - name: pi
            image: perl:5.34.0
            command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
          restartPolicy: Never
      backoffLimit: 4
    

### Use node affinity to request Spot Pods

Alternatively, you can use [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) to request Spot Pods. Node affinity provides you with a more extensible way to select nodes to run your workloads. For example, you can combine several selection criteria to get finer control over where your Pods run. When you use node affinity to request Spot Pods, you can specify the type of node affinity to use, as follows:

  * `requiredDuringSchedulingIgnoredDuringExecution`: Must use Spot Pods.
  * `preferredDuringSchedulingIgnoredDuringExecution`: Use Spot Pods on a best-effort basis.



To use node affinity to _require_ Spot Pods in a Deployment, add the following `nodeAffinity` rule to your Deployment manifest:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: pi
    spec:
      template:
        metadata:
          labels:
            app: pi
        spec:
          **terminationGracePeriodSeconds : 15
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: cloud.google.com/gke-spot
                    operator: In
                    values:
                    - "true"**
          containers:
          - name: pi
            image: perl:5.34.0
            command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
          restartPolicy: Never
      backoffLimit: 4
    

#### Requesting Spot Pods on a best-effort basis

To use node affinity to request Spot Pods on a best-effort basis, use [`preferredDuringSchedulingIgnoredDuringExecution`](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity). When you request Spot Pods on a preferred basis, GKE schedules your Pods based on the following order:

  1. Existing nodes that can run Spot Pods that have available allocatable capacity.
  2. Existing standard nodes that have available allocatable capacity.
  3. New nodes that can run Spot Pods, if the compute resources are available.
  4. New standard nodes.



Because GKE prefers existing standard nodes that have allocatable capacity over creating new nodes for Spot Pods, you might notice more Pods running as standard Pods than as Spot Pods, which prevents you from taking full advantage of the lower pricing of Spot Pods.

**Note:** We recommend that, for all workloads that can tolerate disruptions well, you require Spot Pods using either a `nodeSelector` or the `requiredDuringSchedulingIgnoredDuringExecution` node affinity. Requiring Spot Pods helps ensure that you take full advantage of the lower pricing of Spot Pods.

### Requests for preemptible Pods

Autopilot clusters support requests for _preemptible Pods_ using the `cloud.google.com/gke-preemptible` selector. Pods that use this selector are automatically migrated to Spot Pods, and the selector is changed to `cloud.google.com/gke-spot`.

## Find and delete terminated Pods

**Note:** Starting in GKE version 1.25.7-gke.1000 and 1.26.2-gke.1000, GKE automatically deletes Pods that were evicted during node termination. The following instructions to manually delete terminated Pods only apply to earlier GKE versions.

During graceful Pod termination, the kubelet assigns a `Failed` status and a `Shutdown` reason to the terminated Pods. When the number of terminated Pods reaches a threshold of 1000, [garbage collection](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) cleans up the Pods. You can also delete shutdown Pods manually using the following command:
    
    
    kubectl get pods --all-namespaces | grep -i shutdown | awk '{print $1, $2}' | xargs -n2 kubectl delete pod -n
    

## Stop workloads from using Spot Pods

If you have existing Spot Pods that you want to update to run as standard Pods, you can use one of the following methods:

  * **Recreate the workload** : Delete the Deployment, remove the lines in the manifest that select Spot Pods, and then apply the updated Deployment manifest to the cluster.
  * **Edit the workload** : Edit the Deployment specification while the Pods are running in the cluster.



With both of these methods, you might experience minor workload disruptions.

### Recreate the workload

The following steps show you how to delete the existing Deployment and apply an updated manifest to the cluster. You can also use these steps for other types of Kubernetes workloads, like Jobs.

To ensure that GKE places the updated Pods on the correct type of node, you must export the existing state of the workload from the Kubernetes API server to a file and edit that file.

  1. Write the workload specification to a YAML file:
         
         kubectl get deployment DEPLOYMENT_NAME -o yaml > DEPLOYMENT_NAME-on-demand.yaml
         

Replace `DEPLOYMENT_NAME` with the name of your deployment. For other types of workloads, like Jobs or Pods, use the corresponding resource name in your `kubectl get` command, like `kubectl get pod`.

  2. Open the YAML file in a text editor:
         
         vi DEPLOYMENT_NAME-on-demand.yaml
         

  3. Remove the nodeSelector for Spot Pods **and** the toleration that GKE added for Spot Pods from the file:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           annotations:
           # lines omitted for clarity
         spec:
           progressDeadlineSeconds: 600
           replicas: 6
           revisionHistoryLimit: 10
           selector:
             matchLabels:
               pod: nginx-pod
           strategy:
             rollingUpdate:
               maxSurge: 25%
               maxUnavailable: 25%
             type: RollingUpdate
           template:
             metadata:
             # lines omitted for clarity
             spec:
               containers:
               - image: nginx
                 imagePullPolicy: Always
                 name: web-server
                 resources:
                   limits:
                     ephemeral-storage: 1Gi
                   requests:
                     cpu: 500m
                     ephemeral-storage: 1Gi
                     memory: 2Gi
                 securityContext:
                   capabilities:
                     drop:
                     - NET_RAW
                 terminationMessagePath: /dev/termination-log
                 terminationMessagePolicy: File
               dnsPolicy: ClusterFirst
               **nodeSelector :
                 cloud.google.com/gke-spot: "true"**
               restartPolicy: Always
               schedulerName: default-scheduler
               securityContext:
                 seccompProfile:
                   type: RuntimeDefault
               terminationGracePeriodSeconds: 15
               tolerations:
               - effect: NoSchedule
                 key: kubernetes.io/arch
                 operator: Equal
                 value: amd64
               **- effect: NoSchedule
                 key: cloud.google.com/gke-spot
                 operator: Equal
                 value: "true"**
         status:
           #lines omitted for clarity
         

You must remove both the toleration and the nodeSelector to indicate to GKE that the Pods must run on on-demand nodes instead of on Spot nodes.

  4. Save the updated manifest.

  5. Delete and re-apply the Deployment manifest to the cluster:
         
         kubectl replace -f DEPLOYMENT_NAME-on-demand.yaml
         

The duration of this operation depends on the number of Pods that GKE needs to terminate and clean up.




### Edit the workload in-place

The following steps show you how to edit a running Deployment in-place to indicate to GKE that the Pods must run on on-demand nodes. You can also use these steps for other types of Kubernetes workloads, like Jobs.

You must edit the workload object in the Kubernetes API because GKE automatically adds a toleration for Spot Pods to the workload specification during workload admission.

  1. Open your workload manifest for editing in a text editor:
         
         kubectl edit deployment/DEPLOYMENT_NAME
         

Replace `DEPLOYMENT_NAME` with the name of the Deployment. For other types of workloads, like Jobs or Pods, use the corresponding resource name in your `kubectl edit` command, like `kubectl edit pod/POD_NAME`.

  2. In your text editor, delete the node selector or node affinity rule for Spot Pods and the toleration that GKE added to the manifest, like in the following example:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-deployment
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               type: dev
           template:
             metadata:
               labels:
                 type: dev
             spec:
               **nodeSelector :
                 cloud.google.com/gke-spot: "true"
               tolerations:
               - effect: NoSchedule
                 key: cloud.google.com/gke-spot
                 operator: Equal
                 value: "true"**
               containers:
               - name: nginx
                 image: nginx
                 ports:
                 - containerPort: 80
         

  3. Save the updated manifest and close the text editor. The updated object configuration indicates to GKE that the Pods must run on on-demand nodes. GKE recreates the Pods to place them on new on-demand nodes.




### Verify that workloads run on on-demand nodes

To verify that your updated workloads no longer run on Spot Pods, inspect the workload and look for the toleration for Spot Pods:

  * Inspect the workload:
        
        kubectl describe deployment DEPLOYMENT_NAME
        




The output doesn't display an entry for `cloud.google.com/gke-spot` in the `spec.tolerations` field.

## What's next

  * [Learn more about Autopilot cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-architecture).
  * [Learn about the lifecycle of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
  * [Read about Spot VMs in GKE Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
