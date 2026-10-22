---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging/
title: Use network policy logging \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:37.303084+00:00
---

# Use network policy logging  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Use network policy logging Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to use network policy logging for Google Kubernetes Engine (GKE). Kubernetes [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) specify network traffic that Pods are allowed to send and receive. Network policy logging lets you record when a connection is allowed or denied by a network policy. Network policy logging can help you troubleshoot issues with network policies.

## Overview

Using network policy logging, you can:

  * Verify that your network policies are working as expected.
  * Understand which Pods in your cluster are communicating with the internet.
  * Understand which [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) are communicating with each other.
  * Recognize a Denial of Service attack.



Network policy logs are uploaded to [Cloud Logging](https://docs.cloud.google.com/logging) for storage, search, analysis, and alerting if Cloud Logging is enabled. Cloud Logging is enabled by default in new clusters. See [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing) for more.

### Requirements

  * Network policy logging is only available for clusters that use [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).
  * Network policy logging requires the Google Cloud CLI 303.0.0 or higher.
  * Network policy logging is not supported with Windows Server node pools.



### Pricing

  * There are no log generation charges for network policy logging.


  * If you store your logs in Cloud Logging, standard [Cloud Logging charges](https://cloud.google.com/stackdriver/pricing) apply.


  * Logs can be further routed to Pub/Sub, Cloud Storage, or BigQuery. Pub/Sub, Cloud Storage, or BigQuery charges may apply. For more information, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).



## Configuring network policy logging

You configure network policy logging settings by editing the `NetworkLogging` object in your cluster. GKE automatically creates a `NetworkLogging` object named `default` in new [Dataplane V2 clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2). There can only be one NetworkLogging object per cluster and it can't be renamed.

You can configure the logging of allowed connections and the logging of denied connections separately. You can also selectively enable logging for some network policies. The following is an example of the `NetworkLogging` specification, with settings specified to log all allowed and denied connections:
    
    
    kind: NetworkLogging
    apiVersion: networking.gke.io/v1alpha1
    metadata:
      name: default
    spec:
      cluster:
        allow:
          log: true
          delegate: false
        deny:
          log: true
          delegate: false
    

Use `kubectl` to edit your configuration:
    
    
    kubectl edit networklogging default
    

**Note:** If you use network policies to restrict traffic within Cloud Service Mesh, deploy your network policies before you activate Cloud Service Mesh in a namespace. Otherwise, long-running connections between Pods in the mesh might already have been established, and activating new network policies does not close existing connections.

### NetworkLogging spec

The NetworkLogging object specification is in a YAML format. This format is described in the following table:

Field| Type| Description  
---|---|---  
`**cluster.allow**`| `struct` |  Settings for logging allowed connections. | Field| Type| Description  
---|---|---  
`**log**` | `bool` |  If set to `true`, allowed connections in the cluster are logged; otherwise, allowed connections are not logged. Network policies that select the Pod and have a rule that matches the connection are listed in the log message.  
`**delegate**` | `bool` |  If `false`, all allowed connections are logged. If multiple network policies allow a connection, all matching policies are listed in the log message. If `true`, allowed connections are only logged if they are allowed by a network policy with the logging annotation `policy.network.gke.io/enable-logging: "true"`. If multiple network policies allow a connection, all matching policies with the `enable-logging` annotation are listed in the log message. A configuration error occurs if you set `spec.cluster.allow.delegate` to `true` and `spec.cluster.allow.log` to `false`.  
  
`**cluster.deny**` | `struct` |  Settings for logging denied connections. | Field| Type| Description  
---|---|---  
`**log**` | `bool` |  If set to `true`, denied connections in the cluster are logged; otherwise, denied connections are not logged.  
`**delegate**` | `bool` |  If `false`, all denied connections are logged. If `true`, denied connections are only logged if the Pod where the connection was denied is in a namespace with the annotation `policy.network.gke.io/enable-deny-logging: "true"`. A configuration error occurs if you set `spec.cluster.deny.delegate` to `true` and `spec.cluster.deny.log` to `false`.  
  
## Accessing network policy logs

Network policy logs are automatically uploaded to [Cloud Logging](https://docs.cloud.google.com/logging/docs). You can access logs through the Logs Explorer or with the Google Cloud CLI. You can also [route logs](https://docs.cloud.google.com/logging/docs/routing/overview) to a sink.

### Cloud Logging

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **Query builder**.

  3. Use the following query to find all network policy log records:
         
         resource.type="k8s_node"
         resource.labels.location="CLUSTER_LOCATION"
         resource.labels.cluster_name="CLUSTER_NAME"
         logName="projects/PROJECT_NAME/logs/policy-action"
         

Replace the following:

     * `CLUSTER_LOCATION`: The [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.
     * `CLUSTER_NAME`: The name of your cluster.
     * `PROJECT_NAME`: The name of your Google Cloud project.



See [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to learn how to use the Logs Explorer.

You can also build a query using the **Query builder**. To create a query for network policy logs, select **policy-action** in the **Log name** drop-down list. If there are no available logs, **policy-action** does not appear in the drop-down list.

### gcloud

Find all network policy log records:
    
    
    gcloud logging read --project "PROJECT_NAME" 'resource.type="k8s_node"
        resource.labels.location="CLUSTER_LOCATION"
        resource.labels.cluster_name="CLUSTER_NAME"
        logName="projects/PROJECT_NAME/logs/policy-action"'
    

Replace the following:

  * `PROJECT_NAME`: The name of your Google Cloud project.
  * `CLUSTER_LOCATION`: The [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.
  * `CLUSTER_NAME`: The name of your cluster.



You can add further conditions to filter the results. For example:

  * Show logs in a certain timeframe:
        
        timestamp>="2020-06-22T06:30:51.128Z"
        timestamp<="2020-06-23T06:30:51.128Z"
        

  * Show logs for denied connections:
        
        jsonPayload.disposition="deny"
        

  * Show logs to a deployment named "redis":
        
        jsonPayload.dest.pod_name=~"redis"
        jsonPayload.dest.pod_namespace="default"
        

  * Show logs for cluster-external connections:
        
        jsonPayload.dest.instance != ""
        

  * Show logs that match a certain network policy, in this case "allow-frontend-to-db":
        
        jsonPayload.policies.name="allow-frontend-to-db"
        jsonPayload.policies.namespace="default"
        




If you use a Standard cluster, you can also find the network policy logs generated on each cluster node locally at `/var/log/network/policy_action.log*`. A new numbered log file is created when the current log file reaches 10 MB. Up to five previous log files are stored.

## Network policy log format

Network policy log records are in a JSON format. This format is described in the following table:

Field| Type| Description  
---|---|---  
`**connection**`| `struct` |  Connection information: | Field| Type| Description  
---|---|---  
`**src_ip**`| `string`| Source IP address of the connection.  
`**src_port**`| `int`| Source port of the connection.  
`**dest_ip**`| `string`| Destination IP address of the connection.  
`**dest_port**`| `int`| Destination port of the connection.  
`**protocol**`| `string`| Protocol of the connection, which can be one of `tcp`, `udp`, or `icmp`.  
`**direction**`| `string`| Direction of the connection, which can be `ingress`, or `egress`.  
`**src**`| `struct` |  Endpoint information of the source: | Field| Type| Description  
---|---|---  
`**pod_name**`| `string`| Name of the Pod, if the source is a Pod.  
`**pod_namespace (deprecated)**`| `string`| Namespace of the Pod, if the source is a Pod. **`pod_namespace` is deprecated, use `namespace` instead.**  
`**namespace**`| `string`| Namespace of the Pod, if the source is a Pod.  
`**workload_name**`| `string`| Name of the workload, if the source workload is available.  
`**workload_kind**`| `string`| Kind of the workload, if the source workload is available.  
`**instance**`| `string`| IP address of the source, if the source is not a Pod.  
`**dest**`| `struct` |  Endpoint information of the destination: | Field| Type| Description  
---|---|---  
`**pod_name**`| `string`| Name of the Pod, if the destination is a Pod.  
`**pod_namespace (deprecated)**`| `string`| Namespace of the Pod, if the destination is a Pod. **`pod_namespace` is deprecated, use `namespace` instead.**  
`**namespace**`| `string`| Namespace of the Pod, if the destination is a Pod.  
`**workload_name**`| `string`| Name of the workload, if the destination workload is available.  
`**workload_kind**`| `string`| Kind of the workload, if the destination workload is available.  
`**instance**`| `string`| IP address of the source, if the destination is not a Pod.  
`**disposition**`| `string`| Disposition of the connection, which can be `allow` or `deny`.  
`**policies**`| `list of structs` |  Matched policies for the allowed connections from the enforced Pod's view. For ingress connection, the enforced Pod is the destination Pod. For egress connection, the enforced Pod is the source Pod. Multiple policies are logged if a connection is matched by all of them. This field is only included in logs of allowed connections. | Field| Type| Description  
---|---|---  
`**name**`| `string`| Name of the matching network policy.  
`**namespace**`| `string`| Namespace of the matching network policy.  
`**count**`| `int`| Used for log aggregation of denied queries. The value is always 1 for allowed connection.  
`**node_name**`| `string`| The node that runs the Pod that generated this log message.  
`**timestamp**`| `string`| When the connection attempt occurred.  
**Note:** `namespace`, `workload_name`, and `workload_kind` are available in the following versions: 

  * 1.20.10-gke.2200 to 1.21 
  * 1.21.4-gke.2300 to 1.22 
  * 1.22.1-gke.1700 and later 



### Definition of connection

For connection-oriented protocols like TCP, a log is created for each allowed or denied connection. For protocols like UDP and ICMP that aren't connection-oriented, packets are grouped into time-window based connections.

### Policy logs for denied connections

The log records for denied connections don't include the `policies` field because the Kubernetes network policy API does not have explicit deny policies. A connection is denied if a Pod is covered by one or more network policies, but none of the policies allow the connection. This means that no policy is individually responsible for a blocked connection.

### Log aggregation for denied connections

It is common for a client to retry a connection that was denied. To prevent excessive logging, repeated denied connections within a five-second window are aggregated into a single log message using the `count` field.

Subsequent denied connections are aggregated with a previous log message if the connection's `src_ip, dest_ip, dest_port, protocol,`and `direction` match the first denied connection. Note that the `src_port` of subsequent connections does not have to match because retried connections might come from a different port. The aggregated log message includes the `src_prt` of the first denied connection at the beginning of the aggregation window.

### Example log records

The following example network policy named `allow-green` applied to `test-service` allows connections to `test-service` from a Pod named `client-green`. Implicitly, this policy denies all other ingress traffic to `test-service` including from the Pod `client-red`.
    
    
      apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      metadata:
        name: allow-green
        namespace: default
        annotations:
          policy.network.gke.io/enable-logging: "true"
      spec:
        podSelector:
          matchLabels:
            app: test-service
        ingress:
        - from:
          - podSelector:
              matchLabels:
                app: client-green
        policyTypes:
        - Ingress
    

This diagram shows the effect of the `allow-green` policy on two connections to `test-service`. The `allow-green` policy allows the connection from `client-green`. Because no policy allows the connection from `client-red` the connection is denied.

![image](https://docs.cloud.google.com/static/kubernetes-engine/images/network-policy-logging-diagram.svg)

The log for the allowed connection from `client-green` looks like this:
    
    
    {
       "connection":{
          "src_ip":"10.84.0.252",
          "dest_ip":"10.84.0.165",
          "src_port":52648,
          "dest_port":8080,
          "protocol":"tcp",
          "direction":"ingress"
       },
       "disposition":"allow",
       "policies":[
          {
             "name":"allow-green",
             "namespace":"default"
          }
       ],
       "src":{
          "pod_name":"client-green-7b78d7c957-68mv4",
          "pod_namespace":"default",
          "namespace":"default",
          "workload_name":"client-green-7b78d7c957",
          "workload_kind":"ReplicaSet"
       },
       "dest":{
          "pod_name":"test-service-745c798fc9-sfd9h",
          "pod_namespace":"default",
          "namespace":"default",
          "workload_name":"test-service-745c798fc9",
          "workload_kind":"ReplicaSet"
       },
       "count":1,
       "node_name":"gke-demo-default-pool-5dad52ed-k0h1",
       "timestamp":"2020-06-16T03:10:37.993712906Z"
    }
    

The log for the denied connection from `client-red` looks like this:
    
    
    {
       "connection":{
          "src_ip":"10.84.0.180",
          "dest_ip":"10.84.0.165",
          "src_port":39610,
          "dest_port":8080,
          "protocol":"tcp",
          "direction":"ingress"
       },
       "disposition":"deny",
       "src":{
          "pod_name":"client-red-5689846f5b-b5ccx",
          "pod_namespace":"default",
          "namespace":"default",
          "workload_name":"client-red-5689846f5b",
          "workload_kind":"ReplicaSet"
       },
       "dest":{
          "pod_name":"test-service-745c798fc9-sfd9h",
          "pod_namespace":"default",
          "namespace":"default",
          "workload_name":"test-service-745c798fc9",
          "workload_kind":"ReplicaSet"
       },
       "count":3,
       "node_name":"gke-demo-default-pool-5dad52ed-k0h1",
       "timestamp":"2020-06-15T22:38:32.189649531Z"
    }
    

Note that the denied connection log does not include the `policies` field. This is described in the preceding section, Policy logs for denied connections.

The denied connection log includes a `count` field for aggregating denied connections.

## Troubleshooting issues with network policy logs

  1. Check for error events in the `NetworkLogging` object:
         
         kubectl describe networklogging default
         

If the logging configuration is invalid, the configuration won't take effect and an error will be reported in the events section:
         
         Name:         default
         Namespace:
         Labels:       addonmanager.kubernetes.io/mode=EnsureExists
         Annotations:  API Version:  networking.gke.io/v1alpha1
         Kind:         NetworkLogging
         Metadata:
           Creation Timestamp:  2020-06-20T05:54:08Z
           Generation:          8
           Resource Version:    187864
           Self Link:           /apis/networking.gke.io/v1alpha1/networkloggings/default
           UID:                 0f1ddd6e-4193-4295-9172-baa6a52aa6e6
         Spec:
           Cluster:
             Allow:
               Delegate:  true
               Log:       false
             Deny:
               Delegate:  false
               Log:       false
         Events:
           Type     Reason                 Age                From                                                               Message
           ----     ------                 ----               ----                                                               -------
           Warning  InvalidNetworkLogging  16s (x3 over 11h)  network-logging-controller, gke-anthos-default-pool-cee49209-0t09  cluster allow log action is invalid: delegate cannot be true when log is false
           Warning  InvalidNetworkLogging  16s (x3 over 11h)  network-logging-controller, gke-anthos-default-pool-cee49209-80fx  cluster allow log action is invalid: delegate cannot be true when log is false
         

  2. To limit CPU utilization spent on logging, a node can log up to 500 connections per second before it starts dropping logs. The network policies on the node are still being enforced. You can see if there are dropped policy logs by checking if any error counters are incrementing:
         
         kubectl exec ANETD_POD_NAME -n kube-system -- curl -s http://localhost:9990/metrics |grep policy_logging
         

Replace `ANETD_POD_NAME` with the name of an anetd Pod. Check each node. anetd is the networking controller for Dataplane V2.




### Logs with no name appear for Pods with default deny policies

[Liveness, readiness, and startup probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) require that the Pod accept Ingress connections made by the probes from kubelet. To ensure that these probes function correctly, GKE automatically permits probe traffic to the selected Pod as configured for the Pod regardless of any network policies applied to the Pod. You cannot change this behavior.

Logs for probe connections are similar to the following:
    
    
    {
       "connection":{
          "src_ip":"10.88.1.1",
          "dest_ip":"10.88.1.4",
          "src_port":35848,
          "dest_port":15021,
          "protocol":"tcp",
          "direction":"ingress"
       },
       "disposition":"allow",
       "src":{
          "instance":"10.88.1.1"
       },
       "dest":{
          "pod_name":"testpod-745c798fc9-sfd9h",
          "pod_namespace":"default",
          "namespace":"default",
          "workload_name":"testpod-745c798fc9",
          "workload_kind":"ReplicaSet"
       },
       "count":1,
       "policies": [
         {
           "name":""
         }
        ],
       "node_name":"gke-demo-default-pool-5dad52ed-k0h1",
       "timestamp":"2021-04-01T12:42:32.1898720941Z"
    }
    

The log has the following characteristics:

  * The value of `policies.name` is empty because there is no associated network policy to permit the connection.
  * The value of `connection.src_ip` does not correspond to any Pods or nodes.



## What's next

  * Learn how to [view and analyze logs with Cloud Logging](https://docs.cloud.google.com/logging/docs/how-to).
  * Implement [common approaches to restrict traffic using network policies](https://github.com/GoogleCloudPlatform/anthos-security-blueprints/tree/master/restricting-traffic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
