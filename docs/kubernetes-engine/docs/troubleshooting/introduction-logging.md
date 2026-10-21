---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging/
title: Conduct historical analysis with Cloud Logging \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:07:00.871118+00:00
---

# Conduct historical analysis with Cloud Logging  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Conduct historical analysis with Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When a Pod fails or a service doesn't work as expected in Google Kubernetes Engine (GKE), understanding the sequence of events leading up to the issue is critical. Inspecting the current state isn't always enough to find the root cause, making historical log data invaluable.

Use this page to learn how to use Cloud Logging to investigate past failures (such as why a Pod failed to start or who deleted a critical Deployment) by querying and analyzing GKE logs.

This information is important for Platform admins and operators who need to perform root cause analysis on cluster-wide issues, audit changes, and understand system behavior trends. It's also essential for Application developers for debugging application-specific errors, tracing request paths, and understanding how their code behaves in the GKE environment over time. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand key log types for troubleshooting

To help you troubleshoot, Cloud Logging automatically collects and aggregates several key log types from your GKE clusters, containerized apps, and other Google Cloud services:

  * **Node and runtime logs (`kubelet`, `containerd`)**: the logs from the underlying node services. Because the `kubelet` manages the lifecycle of all Pods on the node, its logs are essential for troubleshooting issues like container startups, Out of Memory (OOM) events, probe failures, and volume mount errors. These logs are also crucial for diagnosing node-level problems, such as a node that has a `NotReady` status.

Because containerd manages the lifecycle of your containers, including pulling images, its logs are crucial for troubleshooting issues that happen before the kubelet can start the container. The containerd logs help you diagnose node-level problems in GKE, because they document the specific activities and potential errors of the container runtime.

  * **App logs (`stdout`, `stderr`)**: the standard output and error streams from your containerized processes. These logs are essential for debugging app-specific issues like crashes, errors, or unexpected behavior.

  * **Audit logs** : these logs answer "who did what, where, and when?" for your cluster. They track administrative actions and API calls made to the Kubernetes API server, which is useful for diagnosing issues caused by configuration changes or unauthorized access.




## Common troubleshooting scenarios

After you identify an issue, you can query these logs to find out what happened. To help get you started, reviewing logs can help you with these issues:

  * If a node has a `NotReady` status, review its node logs. The `kubelet` and `containerd` logs often reveal the underlying cause, such as network problems or resource constraints.
  * If a new node fails to provision and join the cluster, review the node's [serial port logs](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output). These logs capture early boot and kubelet startup activity before the node's logging agents are fully active.
  * If a Pod failed to start in the past, review the app logs for that Pod to check for crashes. If the logs are empty or the Pod can't be scheduled, check the audit logs for relevant events or the node logs on the target node for clues about resource pressure or image pull errors.
  * If a critical Deployment was deleted and no one knows why, query the Admin Activity audit logs. These logs can help you identify which user or service account issued the delete API call, providing a clear starting point for your investigation.



## How to access logs

Use Logs Explorer to query, view, and analyze GKE logs in the Google Cloud console. Logs Explorer provides powerful filtering options that help you to isolate your issue.

To access and use Logs Explorer, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the **query pane** , enter a query. Use the Logging query language to write targeted queries. Here are some common filters to get you started:

Filter type | Description | Example value  
---|---|---  
`resource.type` | The type of Kubernetes resource. | `k8s_cluster`, `k8s_node`, `k8s_pod`, `k8s_container`  
`log_id` | The log stream from the resource. | `stdout`, `stderr`  
`resource.labels.RESOURCE_TYPE.name` | Filter for resources with a specific name.  
Replace `RESOURCE_TYPE` with the name of the resource that you want to query. For example, `namespace` or `pod`. | `example-namespace-name`, `example-pod-name`  
`severity` | The log severity level. | `DEFAULT`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`  
`jsonPayload.message=~` | A regular expression search for text within the log message. | `scale.down.error.failed.to.delete.node.min.size.reached`  
  
For example, to troubleshoot a specific Pod, you might want to isolate its error logs. To see only logs with an `ERROR` severity for that Pod, use the following query:
         
         resource.type="k8s_container"
         resource.labels.pod_name="POD_NAME"
         resource.labels.namespace_name="NAMESPACE_NAME"
         severity=ERROR
         

Replace the following:

     * `POD_NAME`: the name of the Pod experiencing issues.
     * `NAMESPACE_NAME`: the namespace that the Pod is in. If you're not sure what the namespace is, review the `Namespace` column from the output of the `kubectl get pods` command.

For more examples, see [Kubernetes-related queries](https://docs.cloud.google.com/logging/docs/view/query-library#kubernetes-filters) in the Google Cloud Observability documentation.

  3. Click **Run query**.

  4. To see the full log message, including the JSON payload, metadata, and timestamp, click the log entry.




For more information about GKE logs, see [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).

## What's next

  * Read [Perform proactive monitoring with Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring) (the next page in this series).

  * See these concepts applied in the [example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
