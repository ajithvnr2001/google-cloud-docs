---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics/
title: Troubleshooting system metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:32.403135+00:00
---

# Troubleshooting system metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting system metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to resolve system metrics-related issues on your Google Kubernetes Engine (GKE) clusters.

## Metrics from your cluster not appearing in Cloud Monitoring

Ensure that you've [enabled the Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api) and the [Logging API](https://docs.cloud.google.com/logging/docs/api/enable-api) on your project. You should also confirm that you're able to view your project in the [Cloud Monitoring overview](https://console.cloud.google.com/monitoring) in the Google Cloud console.

If the issue persists, check the following potential causes:

  * _Have you enabled monitoring on your cluster?_

Monitoring is enabled by default for clusters created from the Google Cloud console and from the Google Cloud CLI, but you can verify by clicking into the cluster's details in [the Google Cloud console](https://console.cloud.google.com/) by running the following command:
        
        gcloud container clusters describe CLUSTER_NAME
        

The output from this command should include `SYSTEM_COMPONENTS` in the list of `enableComponents` in the `monitoringConfig` section, similar to the following example:
        
        monitoringConfig:
          componentConfig:
            enableComponents:
            - SYSTEM_COMPONENTS
        

If monitoring isn't enabled, run the following command to enable it:
        
        gcloud container clusters update CLUSTER_NAME --monitoring=SYSTEM
        

  * _How long has it been since your cluster was created or had monitoring enabled?_

It can take up to one hour for a new cluster's metrics to start appearing in Cloud Monitoring.

  * _Is a`heapster` or `gke-metrics-agent` (the OpenTelemetry Collector) running in your cluster in the `kube-system` namespace?_

This Pod might be failing to schedule workloads because your cluster is running low on resources. Check whether Heapster or OpenTelemetry is running by running `kubectl get pods --namespace=kube-system` and checking for Pods with `heapster` or `gke-metrics-agent` in the name.

  * _Is your cluster's control plane able to communicate with the nodes?_

Cloud Monitoring relies on that communication. You can check whether the control plane is communicating with the nodes by running the following command:
        
        kubectl logs POD_NAME
        

If this command returns an error, then the SSH tunnels might be causing the issue. For troubleshooting steps, see [Troubleshoot SSH issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kubectl#ssh).




### Identify and fix permissions issues for writing metrics

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

If your organization enforces the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account in your project might not automatically get the required permissions for GKE. 

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

  * To identify the issue, check for `401` errors in the system monitoring workload in your cluster:
        
        [[ $(kubectl logs -l k8s-app=gke-metrics-agent -n kube-system -c gke-metrics-agent | grep -cw "Received 401") -gt 0 ]] && echo "true" || echo "false"
        

If the output is `true`, then the system workload is experiencing 401 errors, which indicate a lack of permissions. If the output is `false`, skip the rest of these steps and try a different troubleshooting procedure.




To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

  1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the **Project number** field, click content_copy **Copy to clipboard**.
  3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click person_add **Grant access**.
  5. In the **New principals** field, specify the following value: 
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
  6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  7. Click **Save**.



### gcloud

  1. Find your Google Cloud project number: 
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
         
         12345678901
         

  2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




### Confirm that the metrics agent has sufficient memory

If you've tried the preceding troubleshooting steps and the metrics still aren't appearing, the metrics agent might have insufficient memory.

In most cases, the default allocation of resources to the GKE metrics agent is sufficient. However, if the DaemonSet crashes repeatedly, you can check the termination reason with the following instructions:

  1. Get the names of the GKE metrics agent Pods:
         
         kubectl get pods -n kube-system -l component=gke-metrics-agent
         

  2. Find the Pod with the status `CrashLoopBackOff`.

The output is similar to the following:
         
         NAME                    READY STATUS           RESTARTS AGE
         gke-metrics-agent-5857x 0/1   CrashLoopBackOff 6        12m
         

  3. Describe the Pod that has the status `CrashLoopBackOff`:
         
         kubectl describe pod POD_NAME -n kube-system
         

Replace `POD_NAME` with the name of the Pod from the previous step.

If the termination reason of the Pod is `OOMKilled`, the agent needs additional memory.

The output is similar to the following:
         
         containerStatuses:
           ...
           lastState:
             terminated:
               ...
               exitCode: 1
               finishedAt: "2021-11-22T23:36:32Z"
               reason: OOMKilled
               startedAt: "2021-11-22T23:35:54Z"
         

  4. Add a node label to the node with the failing metrics agent. You can use either a persistent or temporary node label. We recommend that you try adding an additional 20 MB. If the agent keeps crashing, you can run this command again, replacing the node label with one requesting a higher amount of additional memory.

To update a node pool with a persistent label, run the following command:
         
         gcloud container node-pools update NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --node-labels=ADDITIONAL_MEMORY_NODE_LABEL \
             --location=COMPUTE_LOCATION
         

Replace the following:

     * `NODEPOOL_NAME`: the name of the node pool.
     * `CLUSTER_NAME`: the name of the existing cluster.
     * `ADDITIONAL_MEMORY_NODE_LABEL`: one of the additional memory node labels; use one of the following values: 
       * To add 10 MB: `cloud.google.com/gke-metrics-agent-scaling-level=10`
       * To add 20 MB: `cloud.google.com/gke-metrics-agent-scaling-level=20`
       * To add 50 MB: `cloud.google.com/gke-metrics-agent-scaling-level=50`
       * To add 100 MB: `cloud.google.com/gke-metrics-agent-scaling-level=100`
       * To add 200 MB: `cloud.google.com/gke-metrics-agent-scaling-level=200`
       * To add 500 MB: `cloud.google.com/gke-metrics-agent-scaling-level=500`
     * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.

Alternatively, you can add a temporary node label that won't persist after an upgrade by using the following command:
    
    kubectl label node/NODE_NAME \
    ADDITIONAL_MEMORY_NODE_LABEL --overwrite
    

Replace the following:

     * `NODE_NAME`: the name of the node of the affected metrics agent.
     * `ADDITIONAL_MEMORY_NODE_LABEL`: one of the additional memory node labels; use one of the values from the preceding example.



## What's next

  * If you are having an issue related to the Cloud Logging agent, see its [troubleshooting documentation](https://docs.cloud.google.com/logging/docs/agent/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
