---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks/
title: Troubleshoot Ingress health checks \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:17.220567+00:00
---

# Troubleshoot Ingress health checks  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot Ingress health checks Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Failing Ingress health checks in Google Kubernetes Engine (GKE) can prevent traffic from reaching your application, even if the Pods are running.

Use this document to learn how Ingress health checks work, understand `BackendConfig` and readiness probe considerations, and diagnose problems like unresponsive applications or missing firewall rules.

This information is important for Platform admins and operators and Application developers who configure and manage Ingress resources and need to ensure their applications are correctly reporting as healthy to the load balancer. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand how Ingress health checks work

Before you proceed to the troubleshooting steps, it can be helpful to understand how health checks work in GKE and what considerations to keep in mind to ensure successful health checks.

When you expose one or more Services through an Ingress using the default Ingress controller, GKE creates a [classic Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb) or an [internal Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb). Both of these load balancers support multiple [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) on a single [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts). Each of the backend services corresponds to a Kubernetes Service, and each backend service must reference a [Google Cloud health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts). This health check is _different_ from a Kubernetes liveness or readiness probe because the health check is implemented outside of the cluster.

Load balancer health checks are specified _per backend service_. While it's possible to use the same health check for all backend services of the load balancer, the health check reference isn't specified for the whole load balancer (at the Ingress object itself).

GKE creates health checks based on one of the following methods:

  * **`BackendConfig` CRD**: A custom resource definition (CRD) that gives you precise control over how your Services interact with the load balancer. `BackendConfig` CRDs allow you to specify custom settings for the health check associated with the corresponding backend service. These custom settings provide greater flexibility and control over health checks for both the classic Application Load Balancer and internal Application Load Balancer created by an Ingress.
  * **Readiness probe** : A diagnostic check that determines if a container within a Pod is ready to serve traffic. The GKE Ingress controller creates the health check for the Service's backend service based on the readiness probe used by that Service's serving Pods. You can derive the health check parameters such as path, port, and protocol from the readiness probe definition.
  * **Default values** : The parameters used when you don't configure a `BackendConfig` CRD or define attributes for the readiness probe.

**Best practice** : 

Use a `BackendConfig` CRD to have the most control over the load balancer health check settings.

GKE uses the following procedure to create a health check for each backend service corresponding to a Kubernetes Service:

  * If the Service references [a `BackendConfig` CRD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#direct_hc) with `healthCheck` information, GKE uses that to create the health check. Both the GKE Enterprise Ingress controller and the GKE Ingress controller support creating health checks this way.

  * If the Service does _not_ reference a `BackendConfig` CRD:

    * GKE can infer some or all of the parameters for a health check if the Serving Pods use a Pod template with a container whose readiness probe has attributes that can be interpreted as health check parameters. See [Parameters from a readiness probe](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#interpreted_hc) for implementation details and [Default and inferred parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#def_inf_hc) for a list of attributes that can be used to create health check parameters. Only the GKE Ingress controller supports inferring parameters from a readiness probe.

    * If the Pod template for the Service's serving Pods does **not** have a container with a readiness probe whose attributes can be interpreted as health check parameters, [the default values](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#def_inf_hc) are used to create the health check. Both the GKE Enterprise Ingress controller and the GKE Ingress controller can create a health check using only the default values.




### Considerations

This section outlines some considerations to keep in mind when you configure a `BackendConfig` CRD or use a readiness probe.

#### `BackendConfig` CRD

When you configure `BackendConfig` CRDs, keep the following considerations in mind:

  * If you're using [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing), ensure that the health check port in the `BackendConfig` manifest matches the `containerPort` of a serving Pod.
  * For instance group backends, ensure that the health check port in the `BackendConfig` manifest matches the `nodePort` exposed by the Service.
  * Ingress does not support [gRPC](https://www.grpc.io/) for custom health check configurations. The `BackendConfig` only supports creating health checks using the HTTP, HTTPS, or HTTP2 protocols. For an example of how to use the protocol in a `BackendConfig` CRD, see [gke-networking-recipes](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-custom-grpc-health-check).



For more information, see [When to use `BackendConfig` CRDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#direct_hc_instead).

#### Readiness probe

When you use GKE Ingress with HTTP or HTTPS load balancing, GKE sends the health check probes to determine if your application is running properly. These health check probes are sent to the specific port on your Pods that you defined in the `spec.containers[].readinessProbe.httpGet.port` section of your Pod's YAML configuration, as long as the following conditions are met:

  * The readiness probe's port number specified in `spec.containers[].readinessProbe.httpGet.port` must match the actual port your application is listening on within the container, which is defined in the `containers[].spec.ports.containerPort` field of your Pod configuration.
  * The serving Pod's `containerPort` must match the Service's `targetPort`. This ensures that traffic is directed from the Service to the correct port on your Pods.
  * The Ingress _service backend port specification_ must reference a valid port from `spec.ports[]` section of the Service configuration. This can be done in one of two ways: 
    * `spec.rules[].http.paths[].backend.service.port.name` in the Ingress matches `spec.ports[].name` defined in the corresponding Service.
    * `spec.rules[].http.paths[].backend.service.port.number` in the Ingress matches `spec.ports[].port` defined in the corresponding Service.



## Troubleshoot common health check problems

Use the following troubleshooting flowchart to help identify any health check problems:

![Troubleshooting Ingress health checks.](https://docs.cloud.google.com/static/kubernetes-engine/images/ingress-health-checks.svg)**Figure:** Troubleshoot health checks

In this flowchart, the following troubleshooting guidance helps determine where the issue is:

  1. **Investigate Pod health** : If the health check is failing, examine the status of your Service's serving Pods. If the Pods are not running and healthy:

     * Check the Pod logs for any errors or issues preventing them from running.
     * Check the status of readiness and liveness probes.
  2. **Health check logging** : Ensure that you've enabled health check logging.

  3. **Verify firewall configuration** : Ensure that your firewall rules allow health check probes to reach your Pods. If not:

     * Check your firewall rules to confirm they allow incoming traffic from the health check probe IP address ranges.
     * Adjust firewall rules as needed to accommodate these IP address ranges.
  4. **Analyze packet capture** : If the firewall is correctly configured, perform a packet capture to see if your application is responding to the health checks. If the packet capture shows a successful response, contact Google Cloud support for further assistance.

  5. **Troubleshoot application** : If the packet capture doesn't show a successful response, investigate why your application is not responding correctly to health check requests. Verify that the health check is targeting the correct path and port on the Pods and examine application logs, configuration files, and dependencies. If you can't find the error, contact Google Cloud support.




### Application unresponsive to health checks

The application doesn't respond with the expected status code (200 OK for HTTP or SYN, ACK for TCP) during the health checks on the configured path and port.

If your application doesn't respond correctly to the health checks, it might be due to one of the following reasons:

  * **Network Endpoint Groups(NEGs):**
    * The application is not running correctly within the Pod.
    * The application is not listening on the configured port or path.
    * There are network connectivity issues preventing the health check from reaching the Pod.
  * **Instance Group:**
    * The nodes in the instance group are not healthy.
    * The application is not running correctly on the nodes.
    * The health check requests are not reaching the nodes.



If your health checks are failing, based on your setup, troubleshoot the issue as follows:

**For NEGs** :

  1. Access a Pod using `kubectl exec`:
         
         kubectl exec -it pod-name -- command
         

The flag `-it` provides an interactive terminal session (i for interactive, t for TTY).

Replace the following:

     * `pod-name`: the name of your Pod.
     * `command`: the command you want to run inside the Pod. The most common command is `bash` or `sh` to get an interactive shell.
  2. Run `curl` commands to test connectivity and application responsiveness:

     * `curl localhost:<Port>/<Path>`
     * `curl -v http://<POD_IP>/[Path configured in HC]`
     * `curl http://localhost/[Path configured in HC]`



**For Instance Groups** :

  1. Ensure nodes are healthy and responding to default health check probes.
  2. If nodes are healthy but the application Pod is not responding, investigate the application further.
  3. If requests aren't reaching the Pods, it might be a GKE networking issue. Contact Google Cloud support for assistance.



### Error when editing readiness probe on Pod

When you attempt to edit the readiness probe on a Pod to change health check parameters, it results in an error similar to the following:
    
    
    Pod "pod-name" is invalid: spec: Forbidden: pod updates may not change fields
    

If you modify the readiness probe of Pods associated with a Service that's already linked to an Ingress (and its corresponding load balancer), GKE doesn't automatically update the health check configuration on the load balancer. This leads to a mismatch between the Pod's readiness check and the health check of the load balancer, causing the health check to fail.

To resolve this, redeploy the Pods and the Ingress resource. This forces GKE to recreate the load balancer and its health checks, and incorporate the new readiness probe settings.

### Deployment and load balancer fail to start

If your deployment fails to start and the backend services behind the load balancer of your Ingress controller are marked unhealthy, a readiness probe failure might be the reason.

You might see the following error message mentioning a readiness probe failure:
    
    
    Readiness probe failed: connection refused
    

The application within the Pod doesn't respond correctly to the readiness probe configured in the Pod's YAML configuration. This can be due to various reasons such as the application not starting up properly, listening on the wrong port, or encountering an error during initialization.

To resolve this, investigate and correct any discrepancies in your application's configuration or behavior by doing the following:

  * Ensure that the application is correctly configured and responding on the path and port specified in the readiness probe parameters.
  * Review application logs and troubleshoot any startup issues or errors.
  * Verify that the `containerPort` in the Pod configuration matches the `targetPort` in the Service and the backend port specified in the Ingress.



### Missing automatic Ingress firewall rules

You created an Ingress resource but traffic doesn't reach the backend service.

The automatic Ingress firewall rules, which typically GKE creates when an Ingress resource is created, are missing or have been inadvertently deleted.

To restore connectivity to your backend service, do the following steps:

  * Verify the existence of the automatic Ingress firewall rules in your VPC network.
  * If the rules are missing, you can recreate them manually or delete and recreate the Ingress resource to trigger their automatic creation.
  * Ensure that the firewall rules allow traffic on the appropriate ports and protocols as defined in your Ingress resource.



### Incorrect protocol used in the `BackendConfig` manifest

If you configure a `BackendConfig` CRD with a TCP-type protocol, you will see the following error:
    
    
    Error syncing to GCP: error running backend syncing routine:
    error ensuring health check: Protocol "TCP" is not valid, must be one of ["HTTP","HTTPS","HTTP2"]'
    

The `BackendConfig` supports creating health checks using only the HTTP, HTTPS, or HTTP/2 protocols. For more information, see [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http).

## What's next

  * To set up custom health checks for Ingress in a single cluster, see [GKE networking recipes](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
