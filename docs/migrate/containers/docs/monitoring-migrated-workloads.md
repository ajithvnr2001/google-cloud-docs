---
url: https://docs.cloud.google.com/migrate/containers/docs/monitoring-migrated-workloads/
title: Monitor migrated workloads \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:34.631352+00:00
---

# Monitor migrated workloads  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/monitoring-migrated-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor migrated workloads

You can view logs and metrics from your migrated workloads in the Google Cloud console. You can also view logs from the command line with [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/).

You can execute `bash` commands on the container with your migrated workload. For more, see the [Troubleshooting topic](https://docs.cloud.google.com/migrate/containers/docs/troubleshooting#executing-bash-commands).

## View metrics on the GKE console

The GKE console and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) provide a suite of tools to monitor your containers. To get started:

  1. [Open GKE Workloads](https://console.cloud.google.com/kubernetes/workload)
  2. Click the name of the workload you would like to monitor.



From here, you can see details about this workload, including aggregate graphs of performance across all Pods.

## View logs in Cloud Logging

Once you [enable monitoring](https://docs.cloud.google.com/monitoring/api/enable-api), you can view workload logs in the Cloud Monitoring user interface. 

You can use Cloud Logging to view logs for the following aspects of your migration:

  * Logs written to `stdout` by processes launched by `init`.
  * The content of var/log/syslog.
  * Optionally, application logs written to the file system.



You can view system logs that are in Cloud Logging from the Google Cloud console. To do so: 

  1. [Open GKE Workloads](https://console.cloud.google.com/kubernetes/workload). 
  2. Find your workload and click its **Name**. The **Deployment Details** page appears. 
  3. Find the row labeled **Logs** and click **Container logs**. 



This loads Cloud Logging, showing logs for this workload only. 

![Container logs in Cloud Logging](https://docs.cloud.google.com/static/migrate/anthos/docs/images/stackdriver-container-logs.png)

## View logs in kubectl

You can use `kubectl` to retrieve logs from a running container. You can also monitor the progress of export from short-term to long-term storage.

To view the logs for a pod:

  1. Find the name of your pod from the output of `kubectl get pods`. In the example below, the pod's name is `suitecrm-app-0`.
         
         kubectl get pods
         NAME                       READY     STATUS    RESTARTS   AGE
         csi-disk-controller-0   3/3       Running   4          4d
         csi-disk-node-5t922     3/3       Running   3          4d
         csi-disk-node-5tdcp     3/3       Running   3          4d
         csi-disk-node-86c2t     3/3       Running   3          4d
         csi-disk-node-8785n     3/3       Running   3          4d
         **suitecrm-app-0**       1/1       Running   0          17h

  2. View the logs from your pod with [`kubectl logs`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs).
         
         kubectl logs [POD_NAME]
         I0529 07:01:26.000000    12 hclog.py:48] [suitecrm-app-0] - Auto-detected template: centos
         D0529 07:01:26.000000    12 hclog.py:42] [util] - SHELL OUTPUT: UNIT FILE                                     STATE
         D0529 07:01:26.000000    12 hclog.py:42] [util] - SHELL OUTPUT: adservice.service                             enabled
         




The pod's recent logs are displayed.

For more information on logging and Kubernetes, see the [Kubernetes Logging documentation](https://kubernetes.io/docs/concepts/cluster-administration/logging/).

## What's next

  * Learn how to [upgrade container workloads for enhanced runtime](https://docs.cloud.google.com/migrate/containers/docs/convert-runtime).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
