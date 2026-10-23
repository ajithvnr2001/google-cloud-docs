---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/linux-auditd-logging/
title: Enable linux auditd logs on GKE nodes \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:44.931810+00:00
---

# Enable linux auditd logs on GKE nodes  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/linux-auditd-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Enable linux auditd logs on GKE nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to enable verbose operating system audit logs on Google Kubernetes Engine nodes running [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#container-optimized_os). This page also explains how to configure a fluent-bit logging agent to send logs to Cloud Logging. Enabling verbose logs can provide valuable information about the state of your cluster and workloads, such as error messages, login attempts, and binary executions. You can use this information to debug problems or investigate security incidents.

Enabling Linux auditd logging is not supported in GKE Autopilot clusters, because Google manages the nodes and underlying virtual machines (VMs).

This page is for Security specialists who review and analyze security logs. Use this information to understand the requirements and limitations of verbose OS logs and guide your implementation when enabling them on your GKE nodes. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [Linux operating system audit logs](http://man7.org/linux/man-pages/man7/audit.rules.7.html).

Operating system audit logging is distinct from [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) and [Kubernetes Audit Logs](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/).

## Overview

To collect logs from each node in a cluster, use a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) which runs exactly one Pod on each cluster node where the DaemonSet is eligible to be scheduled. This Pod configures the `auditd` logging daemon on the host and configures the logging agent to send the logs to Logging or any other log-ingestion service.

By definition, auditing occurs after an event and is a retrospective security measure. auditd logs alone are probably not sufficient for conducting forensics on your cluster. Consider how to best use auditd logging as part of your overall security strategy.

**Note:** Increased logging activity on a node increases resource usage on that node, which may affect the performance of your workload and may incur additional resource costs. Audit logs sent to Logging consume log quota from the project. You might need to [increase your log quota and storage](https://console.cloud.google.com/iam-admin/quotas?project=_&service=logging.googleapis.com) to accommodate the additional logs.

## Limitations

The logging mechanisms described on this page work only on nodes running Container-Optimized OS in GKE Standard clusters.

## How the logging DaemonSet works

This section describes how the [example logging DaemonSet](https://github.com/GoogleCloudPlatform/k8s-node-tools/blob/master/troubleshooting/os-audit/cos-auditd-logging.yaml) works so that you can configure it to suit your needs. The next section explains how to deploy the DaemonSet.

The example manifest defines a DaemonSet, a ConfigMap, and a Namespace to contain them.

The DaemonSet deploys a Pod to each node in the cluster. The Pod contains two containers. The first is an [init container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) that starts the cloud-audit-setup systemd service available on Container-Optimized OS nodes. The second container, `cos-auditd-fluent-bit`, contains an instance of [fluent-bit](https://docs.fluentbit.io/manual/) which is configured to collect the Linux audit logs from the node journal and export them to Cloud Logging.

The example logging DaemonSet logs the following events:

  * `auditd` system configuration modifications
  * AppArmor permission checks
  * `execve()`, `socket()`, `setsockopt()`, and `mmap()` executions
  * network connections
  * user logins
  * SSH session and all other TTYs (including `kubectl exec -t` sessions)

**Note:** We recommend you create the DaemonSet immediately after creating your cluster. Logs are only generated for events that occur after the DaemonSet is deployed. The DaemonSet automatically configures `auditd` logging on all new nodes that are added to the cluster.

## Configure the logging DaemonSet

You configure the logging DaemonSet using a ConfigMap, `cos-auditd-fluent-bit-config`. The example provided sends audit logs to Logging, but you can configure it to send logs to other destinations.

The volume of logs produced by `auditd` can be very large and may incur additional costs because it consumes system resources and sends more logs than the default logging configuration. You can set up filters to manage the logging volume:

  * You can set up filters in the `cos-auditd-fluent-bit-config` ConfigMap so that certain data isn't logged. Refer to the [fluent-bit documentation for the Grep, Modify, Record Modifier, and other filters](https://docs.fluentbit.io/manual/pipeline/filters).
  * You can also configure Logging to filter incoming logs. For more details, see [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks).



## Deploy the logging DaemonSet

  1. You can use an existing cluster or [create a new one](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster).

  2. Download the example manifests:
         
         curl https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-node-tools/master/troubleshooting/os-audit/cos-auditd-logging.yaml > cos-auditd-logging.yaml
         

  3. Edit the example manifests to suit your needs. Refer to the previous section for details about how the DaemonSet works. Note that the `fluent-bit` image used in this sample manifest is for demonstration purposes only. As a best practice, replace the image with an image from a controlled source with SHA-256 digest.

  4. Initialize common variables:
         
         export CLUSTER_NAME=CLUSTER_NAME
         export CLUSTER_LOCATION=COMPUTE_REGION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `COMPUTE_REGION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster. For zonal clusters, use the zone instead.
  5. Deploy the logging Namespace, DaemonSet, and ConfigMap:
         
         envsubst '$CLUSTER_NAME,$CLUSTER_LOCATION' < cos-auditd-logging.yaml \
         | kubectl apply -f -
         

  6. Verify that the logging Pods have started. If you defined a different Namespace in your manifests, replace cos-auditd with the name of the namespace you're using.
         
         kubectl get pods --namespace=cos-auditd
         

If the Pods are running, the output looks like this:
         
         NAME                                             READY   STATUS    RESTARTS   AGE
         cos-auditd-logging-g5sbq                         1/1     Running   0          27s
         cos-auditd-logging-l5p8m                         1/1     Running   0          27s
         cos-auditd-logging-tgwz6                         1/1     Running   0          27s
         

One Pod is deployed on each node in the cluster, in this case the cluster has three nodes.

  7. You can now access the audit logs in Logging. In the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), filter the results using the following query:
         
         LOG_ID("linux-auditd")
         resource.labels.cluster_name = "CLUSTER_NAME"
         resource.labels.location = "COMPUTE_REGION"
         

**Note:** The `LOG_ID("linux-auditd")` is part of the resource.type="k8s_node". Ensure that the resource.type="k8s_node" is not excluded in your LogSink configuration if you want `LOG_ID("linux-auditd")` logs to be shipped to the Cloud Logging.

Alternatively, you can use gcloud CLI (use `--limit` because the result set can be very large):
         
         gcloud logging read --limit=100 "LOG_ID("linux-auditd") AND resource.labels.cluster_name = "${CLUSTER_NAME}" AND resource.labels.location = "${CLUSTER_LOCATION}""
         




## Export logs

To learn how to route your logs to supported destinations, see [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Disable logs

To disable `auditd` logging on your nodes, delete the logging DaemonSet, and then deploy the [`cos-auditd-logging-disable`](https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-node-tools/master/troubleshooting/os-audit/cos-auditd-logging-disable.yaml) DaemonSet to revert the systemd service changes on each node. After you deploy this DaemonSet, you can't enable `auditd` logging unless the nodes are re-created.

  1. Delete the original logging DaemonSet and its related resources:
         
         kubectl delete daemonset cos-auditd-logging -n cos-auditd
         kubectl delete configmap fluent-bit-config -n cos-auditd
         # The namespace will be deleted by the cleanup daemonset's namespace definition
         

  2. Apply the [cos-auditd-logging-disable](https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-node-tools/master/troubleshooting/os-audit/cos-auditd-logging-disable.yaml) cleanup DaemonSet:
         
         kubectl apply -f 'https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-node-tools/master/troubleshooting/os-audit/cos-auditd-logging-disable.yaml'
         

  3. Verify that the `cleanup-auditd` Pods are running on all of your nodes:
         
         kubectl get pods -n cos-auditd -l name=cleanup-auditd -w
         

Wait until all Pods show `Running`.

  4. After the cleanup Pods are running, confirm that new `linux-auditd` logs aren't generated by running the queries from the Deploying the logging DaemonSet section. For example, you can use the following gcloud CLI command:
         
         gcloud logging read --limit=10 --freshness="5m" \
           "LOG_ID(\"linux-auditd\") AND \
           resource.labels.cluster_name = \"${CLUSTER_NAME}\" AND \
           resource.labels.location = \"${CLUSTER_LOCATION}\""
         

This command checks for logs in the last five minutes. If the cleanup was successful, the output is empty.

Similarly, when using the [Cloud Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) with the same filter, you should see no new log entries appearing after the cleanup time.

  5. Delete the cleanup DaemonSet and namespace:
         
         kubectl delete -f cleanup-auditd-daemonset.yaml
         

This command will delete both the DaemonSet and the `cos-auditd` namespace.




## What's next

  * Watch [Cloud Forensics 101](https://www.youtube.com/watch?v=OkjTqlETgMA) to get started with cloud forensics.
  * Learn about [Kubernetes Audit Logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) and [audit policy](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/#audit-policy).
  * Read the [Kubernetes Engine Security Overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Learn about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
