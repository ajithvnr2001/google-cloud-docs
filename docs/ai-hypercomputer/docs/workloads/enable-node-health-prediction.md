---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction/
title: Enable node health prediction in a GKE cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:01.014004+00:00
---

# Enable node health prediction in a GKE cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Enable node health prediction in a GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

After you create an AI-optimized Google Kubernetes Engine (GKE) cluster, you can enable _node health prediction_. If you plan to [schedule workloads by using Topology Aware Scheduling (TAS) and Kueue](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas), then enabling node health prediction lets the cluster's scheduler do the following:

  1. Identify nodes that are likely to degrade within the next five hours.

  2. Avoid scheduling new workloads on those nodes.




This approach helps you minimize interruptions on critical and interruption-sensitive workloads, such as large-scale training workloads.

This document explains how to enable node health prediction in a GKE cluster that uses [General GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) (A3 Edge, A2, G2, G4, N1) or [Clustered GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities) (A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High) nodes. To learn how to use the node health prediction metric in a Cloud Monitoring dashboard when, for example, you want to troubleshoot performance issues on a Slurm cluster, see instead [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).

## Limitations

Before you enable node health prediction in your GKE cluster, consider the following limitations:

  * The node must use General GPU (A3 Edge, A2, G2, G4, N1) or Clustered GPU (A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High) machine types.

  * The node must use the [reservation-bound provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound).

**Note:** If the nodes in your cluster use an A3 Mega or A3 High machine type, or you created the nodes by using a different provisioning model, then contact your account team.



## Understand node health prediction

When you enable node health prediction in a GKE cluster, the CronJob applies the `gke.google.com/recommended-to-run-large-training-workload` label to each node in your cluster. The CronJob sets the label values to the likelihood that a node's GPU health will degrade, and updates these values every 10 minutes. If the label value is `true`, then the node is healthy. Otherwise, if the label value is `false`, the node will likely degrade within the next five hours. The label value can change over time based on the node's GPU health.

If you see that a node is likely to degrade, then you can do one or both of the following:

  * **Avoid scheduling workloads on the node**. You can configure Kueue to avoid scheduling workloads on nodes that show a value of `false`, as described in this document.

  * **Report the node as faulty**. If the node is experiencing issues like high GPU temperature or slow performance, then you can report the node as faulty. This action starts a host maintenance event for the node, making it available again for running workloads after maintenance completes. For instructions, see [Report faulty hosts through GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters#report-faulty-hosts).




## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * To connect to your cluster, run the following command:
        
        gcloud container clusters get-credentials CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of your cluster.




## Enable node health prediction

After you've prepared to schedule workloads on your GKE cluster by using TAS, you can enable node health prediction by completing the following steps:

  1. Deploy automatic node labeling

  2. Update your Job configuration

  3. Verify node labeling




### Deploy automatic node labeling

To deploy automatic node labeling for node health prediction in your GKE cluster, complete the following steps:

  1. Clone the hardware accelerators in GKE git repository:
         
         git clone https://github.com/GoogleCloudPlatform/container-engine-accelerators.git
         

  2. Go to the `topology-scheduler` directory:
         
         cd container-engine-accelerators/gpudirect-tcpxo/topology-scheduler
         

  3. Create the Kubernetes ConfigMap containing the Python scripts, `schedule-daemon.py` and `label-nodes-daemon.py`, that query the health scores:

**Note:** These scripts query health prediction scores for both manually installed driver environments and managed driver installations (such as when using the `gpu-driver-version=LATEST` flag).
         
         kubectl create configmap predictor-scheduler-scripts \
             --namespace=kube-system \
             --from-file=schedule-daemon.py=schedule-daemon.py \
             --from-file=label-nodes-daemon.py=label-nodes-daemon.py
         

  4. Apply the service account configuration to grant the necessary permissions (reading Monitoring metrics and patching Node objects) to the CronJob:
         
         kubectl apply -f service-account.yaml
         

  5. Deploy the DaemonSet that schedules the node labeling job:
         
         kubectl apply -f label-nodes-daemon.yaml
         




### Update your Job configuration

To enable node health prediction when using Kueue, you must update your Job configuration to check for health prediction values and, if supported, topology requirements before starting a workload.

To update your Job configuration and enable node health prediction, in the `spec` field, add the following fields:
    
    
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: gke.google.com/recommended-to-run-large-training-workload
                operator: NotIn
                values:
                - "False"
    ...
    

### Verify node labeling

After the CronJob runs for the first time, which is approximately 10 minutes after deployment, verify whether it has applied the `gke.google.com/recommended-to-run-large-training-workload` label to your nodes.

View a list of nodes that have the `gke.google.com/recommended-to-run-large-training-workload` label applied to them:
    
    
    kubectl get nodes -L gke.google.com/recommended-to-run-large-training-workload
    

The label value can be one of the following:

  * **`true`** : the node is predicted to be healthy in the next five hours.

  * **`false`** : the node is likely to degrade within the next five hours. If you configured your Job configuration as described in this document, then Kueue avoids scheduling new workloads on the node.




## What's next

  * To learn about managing common events relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).

  * To learn more about scheduling jobs on GKE with Kueue, see [Deploy a batch system using Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
