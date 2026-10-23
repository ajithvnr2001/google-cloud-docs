---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example/
title: Put it all together: Example troubleshooting scenario \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:13.460325+00:00
---

# Put it all together: Example troubleshooting scenario  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Put it all together: Example troubleshooting scenario Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Understanding the individual troubleshooting tools for Google Kubernetes Engine (GKE) is helpful, but seeing them used together to solve a real-world problem can help solidify your knowledge.

Follow a guided example that combines using the Google Cloud console, the `kubectl` command-line tool, Cloud Logging, and Cloud Monitoring together to identify the root cause of an `OutOfMemory` (`OOMKilled`) error.

This example is beneficial for anyone wanting to see a practical application of the troubleshooting techniques described in this series, particularly Platform admins and operators and Application developers. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## The scenario

You are the on-call engineer for a web app named `product-catalog` that runs in GKE.

Your investigation begins when you receive an automated alert from Cloud Monitoring:
    
    
    Alert: High memory utilization for container 'product-catalog' in 'prod' cluster.
    

This alert tells you that a problem exists and indicates that the problem has something to do with the `product-catalog` workload.

## Confirm the problem in the Google Cloud console

You start with a high-level view of your workloads to confirm the issue.

  1. In the Google Cloud console, you navigate to the **Workloads** page and filter for your `product-catalog` workload.
  2. You look at the **Pods** status column. Instead of the healthy `3/3`, you see the value steadily showing an unhealthy status: `2/3`. This value tells you that one of your app's Pods doesn't have a status of `Ready`.
  3. You want to investigate further, so you click the name of the `product-catalog` workload to go to its details page.
  4. On the details page, you view the **Managed Pods** section. You immediately identify a problem: the `Restarts` column for your Pod shows `14`, an unusually high number.



This high restart count confirms the issue is causing app instability, and suggests that a container is failing its health checks or crashing.

## Find the reason with `kubectl` commands

Now that you know that your app is repeatedly restarting, you need to find out why. The `kubectl describe` command is a good tool for this.

  1. You get the exact name of the unstable Pod:
         
         kubectl get pods -n prod
         

The output is the following:
         
         NAME                             READY  STATUS            RESTARTS  AGE
         product-catalog-d84857dcf-g7v2x  0/1    CrashLoopBackOff  14        25m
         product-catalog-d84857dcf-lq8m4  1/1    Running           0         2h30m
         product-catalog-d84857dcf-wz9p1  1/1    Running           0         2h30m
         

  2. You describe the unstable Pod to get the detailed event history:
         
         kubectl describe pod product-catalog-d84857dcf-g7v2x -n prod
         

  3. You review the output and find clues under the `Last State` and `Events` sections:
         
         Containers:
           product-catalog-api:
             ...
             State:          Waiting
               Reason:       CrashLoopBackOff
             Last State:     Terminated
               Reason:       OOMKilled
               Exit Code:    137
               Started:      Mon, 23 Jun 2025 10:50:15 -0700
               Finished:     Mon, 23 Jun 2025 10:54:58 -0700
             Ready:          False
             Restart Count:  14
         ...
         Events:
           Type     Reason     Age                           From                Message
           ----     ------     ----                          ----                -------
           Normal   Scheduled  25m                           default-scheduler   Successfully assigned prod/product-catalog-d84857dcf-g7v2x to gke-cs-cluster-default-pool-8b8a777f-224a
           Normal   Pulled     8m (x14 over 25m)             kubelet             Container image "us-central1-docker.pkg.dev/my-project/product-catalog/api:v1.2" already present on machine
           Normal   Created    8m (x14 over 25m)             kubelet             Created container product-catalog-api
           Normal   Started    8m (x14 over 25m)             kubelet             Started container product-catalog-api
           Warning  BackOff    3m (x68 over 22m)             kubelet             Back-off restarting failed container
         

The output gives you two critical clues:

     * First, the `Last State` section shows that the container was terminated with `Reason: OOMKilled`, which tells you it ran out of memory. This reason is confirmed by the `Exit Code: 137`, which is the standard Linux exit code for a process that has been killed due to excessive memory consumption.
     * Second, the `Events` section shows a `Warning: BackOff` event with the message `Back-off restarting failed container`. This message confirms that the container is in a failure loop, which is the direct cause of the `CrashLoopBackOff` status that you saw earlier.



## Visualize the behavior with metrics

The `kubectl describe` command told you what happened, but Cloud Monitoring can show you the behavior of your environment over time.

  1. In the Google Cloud console, you go to **Metrics Explorer**.
  2. You select the `container/memory/used_bytes` metric.
  3. You filter the output down to your specific cluster, namespace, and Pod name.



The chart shows a distinct pattern: the memory usage climbs steadily, then abruptly drops to zero when the container is OOM killed and restarts. This visual evidence confirms either a memory leak or insufficient memory limit.

## Find the root cause in logs

You now know the container is running out of memory, but you still don't know exactly why. To discover the root cause, use Logs Explorer.

  1. In the Google Cloud console, you navigate to **Logs Explorer**.
  2. You write a query to filter for your specific container's logs from just before the time of the last crash (which you saw in the output of the `kubectl describe` command):
         
         resource.type="k8s_container"
         resource.labels.cluster_name="example-cluster"
         resource.labels.namespace_name="prod"
         resource.labels.pod_name="product-catalog-d84857dcf-g7v2x"
         timestamp >= "2025-06-23T17:50:00Z"
         timestamp < "2025-06-23T17:55:00Z"
         

  3. In the logs, you find a repeating pattern of messages right before each crash:
         
         {
           "message": "Processing large image file product-image-large.jpg",
           "severity": "INFO"
         },
         {
           "message": "WARN: Memory cache size now at 248MB, nearing limit.",
           "severity": "WARNING"
         }
         




These log entries tell you that the app is trying to process large image files by loading them entirely into memory, which eventually exhausts the container's memory limit.

## The findings

By using the tools together, you have a complete picture of the problem:

  * The monitoring alert notified you that there was a problem.
  * The Google Cloud console showed you that the issue was affecting users (restarts).
  * `kubectl` commands pinpointed the exact reason for the restarts (`OOMKilled`).
  * Metrics Explorer visualized the memory leak pattern over time.
  * Logs Explorer revealed the specific behavior causing the memory issue.



You're now ready to implement a solution. You can either optimize the app code to handle large files more efficiently or, as a short-term fix, increase the container's memory limit (specifically, the `spec.containers.resources.limits.memory` value) in the workload's YAML manifest.

## What's next

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
