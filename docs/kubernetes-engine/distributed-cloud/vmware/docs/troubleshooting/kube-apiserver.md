---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/kube-apiserver/
title: Troubleshoot the Kubernetes API server \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:00.380279+00:00
---

# Troubleshoot the Kubernetes API server  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/kube-apiserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot the Kubernetes API server Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Kubernetes API server (`kube-apiserver`) for Google Distributed Cloud.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Webhook timeouts and failed webhook calls

These errors might be seen in a few different ways. If you experience any of the following symptoms, it's possible that webhook calls are failing:

  * **Connection refused:** If `kube-apiserver` reports timeout errors for calling the webhook, the following error is reported in the logs:
        
        failed calling webhook "server.system.private.gdc.goog":
        failed to call webhook: Post "https://root-admin-webhook.gpc-system.svc:443/mutate-system-private-gdc-goog-v1alpha1-server?timeout=10s":
        dial tcp 10.202.1.18:443: connect: connection refused
        

  * **Context deadline exceeded:** You might also see the following error reported in the logs:
        
        failed calling webhook "namespaces.hnc.x-k8s.io": failed to call webhook: Post
        "https://hnc-webhook-service.hnc-system.svc:443/validate-v1-namespace?timeout=10s\":
        context deadline exceeded"
        




If you think that you are experiencing webhook timeouts or failed webhook calls, use one of the following methods to confirm the issue:

  * Check the API server log to see if there is network issue.

    * Check the log for network-related errors like `TLS handshake error`.
    * Check if the IP/Port matches what the API server is configured to respond on.
  * Monitor webhook latency with the following steps:

    1. In the console, go to the Cloud Monitoring page.

[Go to the Cloud Monitoring page](https://console.cloud.google.com/monitoring/)

    2. Select **Metrics explorer**.

    3. Select the `apiserver_admission_webhook_admission_duration_seconds` metric.




To resolve this issue, review the following suggestions:

  * Additional firewall rules might be required for the webhook. For more information, see how to [add firewall rules for specific use cases](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules).

  * If the webhook requires more time to complete, you can [configure a custom timeout value](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#timeouts). The webhooks latency adds to API request latency, so should be evaluated as quickly as possible.

  * If the webhook error blocks cluster availability or the webhook is harmless to remove and mitigates the situation, check if it's possible to temporarily set the `failurePolicy` to `Ignore` or remove the offending webhook.




## API server dial failure or latency

This error might be seen in a few different ways:

  * **External name resolution errors:** An external client might return errors that contain `lookup` in the message, such as:
        
        dial tcp: lookup kubernetes.example.com on 127.0.0.1:53: no such host
        

This error doesn't apply to a client running within the cluster. The Kubernetes Service IP is injected, so no resolution is required.

  * **Network errors:** The client might print a generic network error when trying to dial the API server, like the following examples:
        
        dial tcp 10.96.0.1:443: connect: no route to host
        dial tcp 10.96.0.1:443: connect: connection refused
        dial tcp 10.96.0.1:443: connect: i/o timeout
        

  * **High latency connecting to API server:** The connection to API server might be successful, but the requests timeout on the client side. In this scenario, the client usually prints error messages containing `context deadline exceeded`.




If the connection to the API server fails completely, try the connection within the same environment where the client reports the error. [Kubernetes ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) can be used to inject a debugging container to the existing namespaces as follows:

  1. From where the problematic client runs, use `kubectl` to perform a request with high verbosity. For example, a `GET` request to `/healthz` usually requires no authentication:
         
         kubectl get -v999 --raw /healthz
         

  2. If the request fails or `kubectl` is unavailable, you can obtain the URL from the output and manually perform the request with `curl`. For example, if the service host obtained from the previous output was `https://192.0.2.1:36917/`, you can send a similar request as follows:
         
         # Replace "--ca-cert /path/to/ca.pem" to "--insecure" if you are accessing
         # a local cluster and you trust the connection cannot be tampered.
         # The output is always "ok" and thus contains no sensentive information.
         
         curl -v --cacert /path/to/ca.pem https://192.0.2.1:36917/healthz
         

The output from this command usually indicates the root cause of a failed connection.

**Note:** You can't use the `ping` or `traceroute` commands to the IP address. A Kubernetes Service IP doesn't accept ICMP or protocols outside the list defined in the Service resource.

If the connection is successful but is slow or times out, it indicates an overloaded API server. To confirm, in the console look at `API Server Request Rate` and request latency metrics in `Cloud Kubernetes > Anthos > Cluster > K8s Control Plane`.




To resolve these connection failures or latency problems, review the following remediation options:

  * If a network error occurs within the cluster, there might be problem with the Container Network Interface (CNI) plugin. This problem is usually transient and resolves itself after a Pod recreation or reschedule.

  * If the network error is from outside the cluster, check if the client is properly configured to access the cluster, or generate the client configuration again. If the connection goes through a proxy or gateway, check if another connection that goes through the same mechanism works.

  * If the API server is overloaded, it usually means that many clients access the API server at the same time. A single client can't overload an API server due to throttling and the [Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/) feature. Review the workload for the following areas:

    * Works at Pod level. It's more common to mistakenly create and forget Pods than higher level resources.
    * Adjust the number of replicas through erroneous calculation.
    * A webhook that loops back the request to itself or amplifies the load by creating more requests than it handles.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
