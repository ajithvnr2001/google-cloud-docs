---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing/
title: Troubleshoot load balancing in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:31.221766+00:00
---

# Troubleshoot load balancing in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot load balancing in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Load balancing issues in Google Kubernetes Engine (GKE) can lead to service disruptions, such as HTTP `502` errors, or prevent access to applications.

Use this document to learn how to troubleshoot `502` errors from external Ingress and how to use load balancer logs and diagnostic tools, such as `check-gke-ingress`, to identify problems.

This information is important for Platform admins and operators and Application developers who configure and maintain load-balanced services in GKE. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

### BackendConfig not found

This error occurs when a BackendConfig for a Service port is specified in the Service annotation, but the actual BackendConfig resource couldn't be found.

To evaluate a Kubernetes event, run the following command:
    
    
    kubectl get event
    

The following example output indicates your BackendConfig was not found:
    
    
    KIND    ... SOURCE
    Ingress ... loadbalancer-controller
    
    MESSAGE
    Error during sync: error getting BackendConfig for port 80 on service "default/my-service":
    no BackendConfig for service port exists
    

To resolve this issue, ensure you have not created the BackendConfig resource in the wrong namespace or misspelled its reference in the Service annotation.

### Ingress security policy not found

After the Ingress object is created, if the security policy isn't properly associated with the LoadBalancer Service, evaluate the Kubernetes event to see if there is a configuration mistake. If your BackendConfig specifies a security policy that does not exist, a warning event is periodically emitted.

To evaluate a Kubernetes event, run the following command:
    
    
    kubectl get event
    

The following example output indicates your security policy was not found:
    
    
    KIND    ... SOURCE
    Ingress ... loadbalancer-controller
    
    MESSAGE
    Error during sync: The given security policy "my-policy" does not exist.
    

To resolve this issue, specify the correct security policy name in your BackendConfig.

### Addressing 500 series errors with NEGs during workload scaling in GKE

**Symptom:**

When you use GKE provisioned NEGs for load balancing, you might experience 502 or 503 errors for the services during the workload scale down. 502 errors occur when Pods are terminated before existing connections close, while the 503 errors occur when traffic is directed to deleted Pods.

This issue can affect clusters if you are using GKE managed load balancing products that use NEGs, including Gateway, Ingress, and standalone NEGs. If you frequently scale your workloads, your cluster is at a higher risk of being affected.

**Diagnosis:**

Removing a Pod in Kubernetes without draining its endpoint and removing it from the NEG first leads to 500 series errors. To avoid issues during Pod termination, you must consider the order of operations. The following images display scenarios when `BackendService Drain Timeout` is unset and `BackendService Drain Timeout` is set with `BackendConfig`.

**Note:** The following resolution is not effective in resolving other 500 series errors resulting from Pod or node preemptions in GKE, particularly in the case of GKE with Spot VMs and preemptible VMs.

**Scenario 1** : `BackendService Drain Timeout` is unset.

The following image displays a scenario where the `BackendService Drain Timeout` is unset.

![BackendService Drain Timeout is unset.](https://docs.cloud.google.com/static/kubernetes-engine/images/neg-backend-servicedraintimeout-unset.png)

**Scenario 2** : `BackendService Drain Timeout` is set.

The following image displays a scenario where the `BackendService Drain Timeout` is set.

![BackendService Drain Timeout is set.](https://docs.cloud.google.com/static/kubernetes-engine/images/neg-backend-servicedraintimeout.png)

The exact time the 500 series errors occur depends on the following factors:

  * **NEG API detach latency** : The NEG API detach latency represents the current time taken for the detach operation to finalize in Google Cloud. This is influenced by a variety of factors outside Kubernetes, including the type of load balancer and the specific zone.

  * **Drain latency** : Drain latency is the time taken for the load balancer to start directing traffic away from a particular part of your system. After drain is initiated, the load balancer stops sending new requests to the endpoint, however there is still a latency in triggering drain (drain latency) which can cause temporary 503 errors if the Pod no longer exists.

  * **Health check configuration** : More sensitive health check thresholds mitigate the duration of 503 errors as it can signal the load balancer to stop sending requests to endpoints even if the detach operation has not finished.

  * **Termination grace period** : The termination grace period determines the maximum amount of time a Pod is given to exit. However, a Pod can exit before the termination grace period completes. If a Pod takes longer than this period, the Pod is forced to exit at the end of this period. This is a setting on the Pod and needs to be configured in the workload definition.




**Potential resolution:**

To prevent those 5XX errors, apply the following settings. The timeout values are suggestive and you might need to adjust them for your specific application. The following section guides you through the customization process.

The following image displays how to keep the Pod alive with a `preStop` hook:

![BackendService Drain Timeout is set.](https://docs.cloud.google.com/static/kubernetes-engine/images/preStopHooks.png)

To avoid 500 series errors, perform the following steps:

  1. Set the `BackendService Drain Timeout` for your service to 1 minute.

**Note:** If your average request time is more than 30 seconds, see the Customize timeouts to customize the `BackendService Drain Timeout`.
     * For Ingress Users, see [set the timeout on the BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#draining_timeout).

     * For Gateway Users, see [configure the timeout on the GCPBackendPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_connection_draining).

     * For those managing their BackendServices directly when using Standalone NEGs, see [set the timeout directly on the Backend Service](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining#enabling_connection_draining).

  2. Extend the `terminationGracePeriod` on the Pod.

Set the `terminationGracePeriodSeconds` on the Pod to 3.5 minutes. When combined with the recommended settings, this allows your Pods a 30 to 45 second window for a graceful shutdown after the Pod's endpoint has been removed from the NEG. If you require more time for the graceful shutdown, you can extend the grace period or follow the instructions mentioned in the Customize timeouts section.

The following Pod manifest specifies a connection draining timeout of 210 seconds (3.5 minutes):
         
         spec:
           terminationGracePeriodSeconds: 210
           containers:
           - name: my-app
             ...
           ...
         

  3. Apply a `preStop` hook to all containers.

Apply a `preStop` hook that will ensure the Pod is alive for 120 seconds longer while the Pod's endpoint is drained in the load balancer and the endpoint is removed from the NEG.

**Note:** Apply the `preStop` hook to every container in your Pod. Containers without the hook will exit as soon as the Pod is deleted. If you use a tool that injects containers, ensure that the injected containers will have the required `preStop` hook.
         
         spec:
           containers:
           - name: my-app
             ...
             lifecycle:
               preStop:
                 exec:
                   command: ["/bin/sh", "-c", "sleep 120s"]
           ...
         




#### Customize timeouts

To ensure Pod continuity and prevent 500 series errors, the Pod must be alive until the endpoint is removed from the NEG. Specifically to prevent 502 and 503 errors, consider implementing a combination of timeouts and a `preStop` hook.

**Note:** If the health check configuration is set to detect failures immediately, it may lead to load balancers ceasing to send requests sooner, potentially reducing the occurrence of 503 errors. However, note that 503 errors may still occur during the duration of the unhealthy threshold. It's essential to understand that configuring health checks won't prevent 502 errors, which occur when existing connections are prematurely terminated.

To keep the Pod alive longer during the shutdown process, add a `preStop` hook to the Pod. Run the `preStop` hook before a Pod is signaled to exit, so the `preStop` hook can be used to keep the Pod alive until its corresponding endpoint is removed from the NEG.

To extend the duration that a Pod remains active during the shutdown process, insert a `preStop` hook into the Pod configuration as follows:
    
    
    spec:
      containers:
      - name: my-app
        ...
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "sleep <latency time>"]
    

**Note:** In multi-container Pods, ensure that you add the `preStop` hook to each container to keep all containers active. Only containers with the hook run, and the rest stop. If you're using a tool that adds containers, make sure those added containers also have the necessary `preStop` hook.

You can configure timeouts and related settings to manage the graceful shutdown of Pods during workload scale downs. You can adjust timeouts based on specific use cases. We recommend that you start with longer timeouts and reduce the duration as necessary. You can customize the timeouts by configuring timeout-related parameters and the `preStop` hook in the following ways:

**Backend Service Drain Timeout**

The `Backend Service Drain Timeout` parameter is unset by default and has no effect. If you set the `Backend Service Drain Timeout` parameter and activate it, the load balancer stops routing new requests to the endpoint and waits the timeout before terminating existing connections.

You can set the `Backend Service Drain Timeout` parameter by using the `BackendConfig` with Ingress, the `GCPBackendPolicy` with Gateway or manually on the `BackendService` with standalone NEGs. The timeout should be 1.5 to 2 times longer than the time it takes to process a request. This helps ensure that if a request came in right before the drain was initiated, it will complete before the timeout completes. Setting the `Backend Service Drain Timeout` parameter to a value greater than 0 helps mitigate 503 errors because no new requests are sent to endpoints scheduled for removal. For this timeout to be effective, you must use it with the `preStop` hook to help ensure that the Pod remains active while the drain occurs. Without this combination, existing requests that didn't complete will receive a 502 error.

**`preStop` hook time**

The `preStop` hook must delay Pod shut down sufficiently for both drain latency and backend service drain timeout to complete, to help ensure proper connection drainage and endpoint removal from the NEG before the Pod is shut down.

For optimal results, ensure your `preStop` hook execution time is greater than or equal to the sum of the `Backend Service Drain Timeout` and drain latency.

Calculate your ideal `preStop` hook execution time with the following formula:
    
    
    preStop hook execution time >= BACKEND_SERVICE_DRAIN_TIMEOUT + DRAIN_LATENCY
    

Replace the following:

  * `BACKEND_SERVICE_DRAIN_TIMEOUT`: the time that you configured for the `Backend Service Drain Timeout`.
  * `DRAIN_LATENCY`: an estimated time for drain latency. We recommend that you use one minute as your estimate.



If 500 errors persist, estimate the total occurrence duration and add double that time to the estimated drain latency. This ensures that your Pod has enough time to drain gracefully before being removed from the service. You can adjust this value if it's too long for your specific use case.

Alternatively, you can estimate the timing by examining the deletion timestamp from the Pod and the timestamp when the endpoint was removed from the NEG in the Cloud Audit Logs.

**Termination Grace Period parameter**

You must configure the `terminationGracePeriod` parameter to allow sufficient time for the `preStop` hook to finish and for the Pod to complete a graceful shutdown.

By default, when not explicitly set, the `terminationGracePeriod` is 30 seconds. You can calculate the optimal `terminationGracePeriod` using the formula:

`terminationGracePeriod >= preStop hook time + Pod shutdown time`

To define `terminationGracePeriod` within the Pod's configuration as follows:
    
    
      spec:
        terminationGracePeriodSeconds: <terminationGracePeriod>
        containers:
        - name: my-app
          ...
        ...
    

### NEG not found when creating an Internal Ingress resource

The following error might occur when you create an internal Ingress in GKE:
    
    
    Error syncing: error running backend syncing routine: googleapi: Error 404: The resource 'projects/PROJECT_ID/zones/ZONE/networkEndpointGroups/NEG' was not found, notFound
    

This error occurs because Ingress for internal Application Load Balancers requires Network Endpoint Groups (NEGs) as backends.

In Shared VPC environments or clusters with Network Policies enabled, add the annotation `cloud.google.com/neg: '{"ingress": true}'` to the Service manifest.

### 504 Gateway Timeout: upstream request timeout

The following error might occur when you access a Service from an internal Ingress in GKE:
    
    
    HTTP/1.1 504 Gateway Timeout
    content-length: 24
    content-type: text/plain
    
    upstream request timeout
    

This error occurs because traffic sent to internal Application Load Balancers are proxied by [envoy proxies](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in the proxy-only subnet range.

To allow traffic from the proxy-only subnet range, [create a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#create_a_firewall_rule) on the `targetPort` of the Service.

### Error 400: Invalid value for field 'resource.target'

The following error might occur when you access a Service from an internal Ingress in GKE:
    
    
    Error syncing:LB_NAME does not exist: googleapi: Error 400: Invalid value for field 'resource.target': 'https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/REGION_NAME/targetHttpProxies/LB_NAME. A reserved and active subnetwork is required in the same region and VPC as the forwarding rule.
    

To resolve this issue, create a [proxy-only subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#prepare-environment).

### Error during sync: error running load balancer syncing routine: loadbalancer does not exist

One of the following errors might occur when the GKE control plane upgrades or when you modify an Ingress object:
    
    
    "Error during sync: error running load balancer syncing routine: loadbalancer
    INGRESS_NAME does not exist: invalid ingress frontend configuration, please
    check your usage of the 'kubernetes.io/ingress.allow-http' annotation."
    

Or:
    
    
    Error during sync: error running load balancer syncing routine: loadbalancer LOAD_BALANCER_NAME does not exist:
    googleapi: Error 400: Invalid value for field 'resource.IPAddress':'INGRESS_VIP'. Specified IP address is in-use and would result in a conflict., invalid
    

To resolve these issues, try the following steps:

  * Add the `hosts` field in the `tls` section of the Ingress manifest, then delete the Ingress. Wait five minutes for GKE to delete the unused Ingress resources. Then, recreate the Ingress. For more information, see [The hosts field of an Ingress object](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl#the_hosts_field_of_an_ingress_object).
  * Revert the changes you made to the Ingress. Then, add a certificate using an [annotation or Kubernetes Secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl#specifying_certificates_for_your_ingress).



## External Ingress produces HTTP 502 errors

Use the following guidance to troubleshoot HTTP 502 errors with external Ingress resources:

  1. [Enable logs](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#enabling_logging_on_an_existing_backend_service) for each backend service associated with each GKE Service that is referenced by the Ingress.
  2. Use [status details](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#failure-messages) to identify causes for HTTP 502 responses. Status details that indicate the HTTP 502 response originated from the backend require troubleshooting within the serving Pods, not the load balancer.



### Unmanaged instance groups

You might experience HTTP 502 errors with external Ingress resources if your external Ingress uses unmanaged instance group backends. This issue occurs when **all** of the following conditions are met:

  * The cluster has a large total number of nodes among all node pools.
  * The serving Pods for one or more Services that are referenced by the Ingress are located on only a few nodes.
  * Services referenced by the Ingress use `externalTrafficPolicy: Local`.



To determine if your external Ingress uses unmanaged instance group backends, do the following:

  1. Go to the **Ingress** page in the Google Cloud console.

[Go to Ingress](https://console.cloud.google.com/kubernetes/ingresses)

  2. Click the name of your external Ingress.

  3. Click the name of the **Load balancer**. The **Load balancing details** page displays.

  4. Check the table in the **Backend services** section to determine if your external Ingress uses NEGs or instance groups.




To resolve this issue, use one of the following solutions:

  * Use a VPC-native cluster.
  * Use `externalTrafficPolicy: Cluster` for each Service referenced by the external Ingress. This solution causes you to lose the original client IP address in the packet's sources.
  * Use the `node.kubernetes.io/exclude-from-external-load-balancers=true` annotation. Add the annotation to the nodes or node pools that don't run any serving Pod for any Service referenced by any external Ingress or `LoadBalancer` Service in your cluster.



## L4 load balancer logging configuration

This section provides troubleshooting information if you have enabled logging for your external passthrough Network Load Balancer or internal passthrough Network Load Balancer.

### Monitor status of logging configuration

The GKE L4LB controller provides feedback on the logging reconciliation status through the Service's `status.conditions` type. You can check this status by running the following command:
    
    
    kubectl get svc SERVICE_NAME -o yaml
    

Replace the following:

  * `SERVICE_NAME`: the name of the cluster.



In the output, look for the `LoggingConfigManaged` condition type. The following table describes the possible reasons for the condition:

Condition status | Reason | Description  
---|---|---  
True | Reconciled | The controller is actively enforcing the logging configuration defined in the L4LBConfig CRD.  
False | Unmanaged | The `logging` section is missing from the L4LBConfig CRD, or the annotation was removed. The controller has stopped management and left the backend service in its last known state.  
False | Missing | The L4LBConfig resource referenced in the Service annotation cannot be found.  
False | Invalid | The L4LBConfig resource failed the cross validation of the `optionalFields` parameter.  
False | Error | An error occurred during the reconciliation of the backend service.  
  
### Understand coast behavior

If the `networking.gke.io/l4lb-config` annotation is removed from the Service manifest, or the referenced L4LBConfig resource is deleted, the configuration enters a `Coast` state.

In this state, the GKE controller stops managing the logging settings but doesn't reset the Google Cloud backend service to its default settings. Instead, the backend service remains in its last known good state. A warning event is typically issued to notify you that Kubernetes is no longer controlling the configuration.

## Use load balancer logs to troubleshoot

You can use [internal passthrough Network Load Balancer logs](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#ilblb-logging) and [external passthrough Network Load Balancer logs](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring#netlb-logging) to troubleshoot issues with load balancers and correlate traffic from load balancers to GKE resources.

Logs are aggregated per-connection and exported in near real time. Logs are generated for each GKE node involved in the data path of a LoadBalancer Service, for both ingress and egress traffic. Log entries include additional fields for GKE resources, such as:

  * Cluster name
  * Cluster location
  * Service name
  * Service namespace
  * Pod name
  * Pod namespace



### Pricing

There are no additional charges for using logs. Based on how you ingest logs, standard pricing for [Cloud Logging](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing), BigQuery, or Pub/Sub apply. Enabling logs has no effect on the performance of the load balancer.

## Use diagnostic tools to troubleshoot

The `check-gke-ingress` diagnostic tool inspects Ingress resources for common misconfigurations. You can use the `check-gke-ingress` tool in the following ways:

  * Run the [`gcpdiag` command-line tool](https://gcpdiag.dev/docs/running/) on your cluster. Ingress results appear in the check rule `gke/ERR/2023_004` section.
  * Use the `check-gke-ingress` tool alone or as a kubectl plugin by following the instructions in [check-gke-ingress](https://github.com/kubernetes/ingress-gce/tree/master/cmd/check-gke-ingress).



## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
