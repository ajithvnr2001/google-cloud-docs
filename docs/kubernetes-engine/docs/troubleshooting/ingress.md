---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress/
title: Troubleshoot GKE Ingress \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:19.402434+00:00
---

# Troubleshoot GKE Ingress  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot GKE Ingress Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Issues with Ingress in Google Kubernetes Engine (GKE) can prevent external or internal traffic from reaching your services.

Use this document to find solutions for errors related to the Ingress class, static IP annotations, certificate key sizes, and interactions with network tiers.

This information is for Platform admins and operators and Application developers who deploy and manage applications exposed using Ingress in GKE. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Incorrect annotation for the Ingress class

**Symptom**

When you create an Ingress, you might see the following error:
    
    
    Missing one or more resources. If resource creation takes longer than expected, you might have an invalid configuration.
    

**Potential causes**

When creating the Ingress, you might have incorrectly configured the Ingress class in the manifest.

**Resolution**

To specify an Ingress class, you must use the `kubernetes.io/ingress.class` annotation. You cannot specify a GKE Ingress using `spec.ingressClassName`.

  * To deploy an internal Application Load Balancer, use the `kubernetes.io/ingress.class: gce-internal` annotation.
  * To deploy an external Application Load Balancer, use the `kubernetes.io/ingress.class: gce` annotation.



## Incorrect annotation for the static IP address

**Symptom**

When you configure an external Ingress to use a static IP address, you might see the following error:
    
    
    Error syncing to GCP: error running load balancer syncing routine: loadbalancer <Name of load balancer> does not exist: the given static IP name <Static IP> doesn't translate to an existing static IP.
    

**Potential causes**

  * You didn't create a static external IP address before you deployed the Ingress.
  * You're not using the correct annotation for your type of Load Balancer.



**Resolution**

If you're configuring an external Ingress:

  * [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) before you deploy the Ingress.
  * Use the annotation `kubernetes.io/ingress.global-static-ip-name` on your Ingress resource.



If you're configuring an internal Ingress:

  * Reserve a regional static internal IP address before you deploy the Ingress.
  * Use the annotation `kubernetes.io/ingress.regional-static-ip-name` on your Ingress resource.



## Static IP address is already in use

**Symptom**

You might see the following error when you specify a static IP address to provision your internal or external Ingress resource:
    
    
    Error syncing to GCP: error running load balancer syncing
    routine: loadbalancer <LB name> does not exist:
    googleapi: Error 409: IP_IN_USE_BY_ANOTHER_RESOURCE - IP ''<IP address>'' is already being used by another resource.
    

**Potential causes**

The static IP address is already being used by another resource.

## Error when disabling HTTP and using a Google-managed certificate

**Symptom**

If you are configuring a Google-managed SSL certificate and disabling HTTP traffic on your Ingress, you see the following error:
    
    
    Error syncing to GCP: error running load balancer syncing
    routine: loadbalancer <Load Balancer name> does not exist:
    googleapi: Error 404: The resource ''projects/<Project>/global/sslPolicies/<Policy name>' was not found, notFound
    

**Potential causes**

You can't use the following annotations together when you configure the Ingress:

  * `networking.gke.io/managed-certificates` (for associating the Google-managed certificate to an Ingress)
  * `kubernetes.io/ingress.allow-http: false` (for disabling HTTP traffic)



**Resolution**

Disable HTTP traffic only after the external Application Load Balancer is fully programmed. You can update the Ingress and add the annotation `kubernetes.io/ingress.allow-http: false` to the manifest.

## Proxy-only subnet is missing for an internal Ingress

**Symptom**

When you deploy an Ingress for an internal Application Load Balancer, you might see the following error:
    
    
    Error syncing to GCP: error running load balancer syncing routine:
    loadbalancer <LB name> does not exist: googleapi: Error 400: Invalid value for field 'resource.target': 'https://www.googleapis.com/compute/v1/projects/<Project ID>/regions/<Region>/targetHttpsProxies/<Target proxy>'.
    An active proxy-only subnetwork is required in the same region and VPC as
    the forwarding rule.
    

**Potential causes**

You didn't create a proxy-only subnet before you created the Ingress resource. A proxy-only subnet is required for internal Application Load Balancers.

**Resolution**

[Create a proxy-only subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#prepare-environment) before you deploy the internal Ingress.

## SSL certificate key is too large

**Symptom**

If the key size of the SSL certificate of your load balancer is too large, you might see the following error:
    
    
    Error syncing to GCP: error running load balancer syncing routine: loadbalancer gky76k70-load-test-trillian-api-ingress-fliismmb does not exist: Cert creation failures - k8s2-cr-gky76k70-znz6o1pfu3tfrguy-f9be3a4abbe573f7 Error:googleapi: Error 400: The SSL key is too large., sslCertificateKeyTooLarge
    

**Potential causes**

Google Cloud has a limit of 2,048 bits for SSL certificate keys.

**Resolution**

Reduce the size of the SSL certificate key to 2,048 bits or fewer.

## Error creating an Ingress in Standard Tier

**Symptom**

If you are deploying an Ingress in a project with the [project default network tier](https://docs.cloud.google.com/network-tiers/docs/set-network-tier#setting_the_tier_for_all_resources_in_a_project) set to Standard, the following error message appears:
    
    
    Error syncing to GCP: error running load balancer syncing routine: load balancer <LB Name> does not exist: googleapi: Error 400: STANDARD network tier (the project''s default network tier) is not supported: STANDARD network tier is not supported for global forwarding rule., badRequest
    

**Resolution**

Configure the project default network tier to Premium.

## Expected 'Not Found' Error for `k8s-ingress-svc-acct-permission-check-probe`

The Ingress controller performs periodic checks of service account permissions by fetching a test resource from your Google Cloud project. You will see this as a `GET` of the (non-existent) global `BackendService` with the name `k8s-ingress-svc-acct-permission-check-probe`. As this resource shouldn't normally exist, the `GET` request will return "not found". This is expected; the controller is checking that the API call is not rejected due to authorization issues. If you create a BackendService with the same name, then the `GET` will succeed instead of returning "not found".

## Errors using container-native load balancing

Use the following techniques to verify your networking configuration. The following sections explain how to resolve specific issues related to container-native load balancing.

  * See the [load balancing documentation](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#listing-negs) for how to list your network endpoint groups.

  * You can find the name and zones of the NEG that corresponds to a service in the `neg-status` annotation of the service. Get the Service specification with:
        
        kubectl get svc SVC_NAME -o yaml
        

The `metadata:annotations:cloud.google.com/neg-status` annotation lists the name of service's corresponding NEG and the zones of the NEG.

  * You can check the health of the backend service that corresponds to a NEG with the following command:
        
        gcloud compute backend-services --project PROJECT_NAME \
            get-health BACKEND_SERVICE_NAME --global
        

The backend service has the same name as its NEG.

  * To print a service's event logs:
        
        kubectl describe svc SERVICE_NAME
        

The service's name string includes the name and namespace of the corresponding GKE Service.




### Cannot create a cluster with alias IPs

Symptoms
    

When you attempt to create a cluster with alias IPs, you might encounter the following error:
    
    
    ResponseError: code=400, message=IP aliases cannot be used with a legacy network.
    

Potential causes
    

You encounter this error if you attempt to create a cluster with alias IPs that also uses a legacy network.

Resolution
    

Ensure that you don't create a cluster with alias IPs and a legacy network enabled simultaneously. For more information about using alias IPs, refer to [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

### Traffic does not reach endpoints

Symptoms
    502/503 errors or rejected connections.
Potential causes
    

New endpoints generally become reachable after attaching them to the load balancer, provided that they respond to health checks. You might encounter 502 errors or rejected connections if traffic cannot reach the endpoints.

    

502 errors and rejected connections can also be caused by a container that doesn't handle `SIGTERM`. If a container doesn't explicitly handle `SIGTERM`, it immediately terminates and stops handling requests. The load balancer continues to send incoming traffic to the terminated container, leading to errors.

    

The container-native load balancer only has one backend endpoint. During a rolling update, the old endpoint gets deprogrammed before the new endpoint gets programmed.

    

Backend Pod(s) are deployed into a new zone for the first time after a container-native load balancer is provisioned. Load balancer infrastructure is programmed in a zone when there is at least one endpoint in the zone. When a new endpoint is added to a zone, load balancer infrastructure is programmed and causes service disruptions.

Resolution
    

Configure containers to handle `SIGTERM` and continue responding to requests throughout the termination grace period (30 seconds by default). Configure Pods to begin failing health checks when they receive `SIGTERM`. This signals the load balancer to stop sending traffic to the Pod while endpoint deprogramming is in progress.

    

If your application does not gracefully shut down and stops responding to requests when receiving a `SIGTERM`, the [preStop hook](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#hook-details) can be used to handle `SIGTERM` and keep serving traffic while endpoint deprogramming is in progress.
    
    
    lifecycle:
      preStop:
        exec:
          # if SIGTERM triggers a quick exit; keep serving traffic instead
          command: ["sleep","60"]
    

    

See the [documentation on Pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods).

    

If your load balancer backend only has one instance, configure the rollout strategy to avoid tearing down the only instance before the new instance is fully programmed. For application pods managed by `Deployment` workload, this can be achieved by configuring rollout [strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy) with `maxUnavailable` parameter equal to `0`.
    
    
    strategy:
      rollingUpdate:
        maxSurge: 1
        maxUnavailable: 0
    

    

To troubleshoot traffic not reaching the endpoints, verify that firewall rules allow incoming TCP traffic to your endpoints in the `130.211.0.0/22` and `35.191.0.0/16` ranges. To learn more, refer to [Adding Health Checks](https://docs.cloud.google.com/load-balancing/docs/health-checks) in the Cloud Load Balancing documentation.

    

View the backend services in your project. The name string of the relevant backend service includes the name and namespace of the corresponding GKE Service:
    
    
    gcloud compute backend-services list
    

    

Retrieve the backend health status from the backend service:
    
    
    gcloud compute backend-services get-health BACKEND_SERVICE_NAME
    

    

If all backends are unhealthy, your firewall, Ingress, or Service might be misconfigured.

    

If some backends are unhealthy for a short period of time, network programming latency might be the cause.

    

If some backends don't appear in the list of backend services, programming latency might be the cause. You can verify this by running the following command, where `NEG_NAME` is the name of the backend service. (NEGs and backend services share the same name):
    
    
    gcloud compute network-endpoint-groups list-network-endpoints NEG_NAME
    

    

Check if all the expected endpoints are in the NEG.

    

If you have a small number of backends (for example, 1 Pod) selected by a container-native load balancer, consider increasing the number of replicas and distribute the backend Pods across all zones that the GKE cluster spans. This will ensure the underlying load balancer infrastructure is fully programmed. Otherwise, consider restricting the backend Pods to a single zone.

    

If you configure a network policy for the endpoint, make sure that ingress from Proxy-only subnet is allowed.

### Stalled rollout

Symptoms
    Rolling out an updated Deployment stalls, and the number of up-to-date replicas does not match the chosen number of replicas.
Potential causes
    

The deployment's health checks are failing. The container image might be bad or the health check might be misconfigured. The rolling replacement of Pods waits until the newly started Pod passes its [Pod readiness gate](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate). This only occurs if the Pod is responding to load balancer health checks. If the Pod does not respond, or if the health check is misconfigured, the readiness gate conditions can't be met and the rollout can't continue.

    

If you're using `kubectl` 1.13 or higher, you can check the status of a Pod's readiness gates with the following command:
    
    
    kubectl get pod POD_NAME -o wide
    

    

Check the `READINESS GATES` column.

    

This column doesn't exist in `kubectl` 1.12 and lower. A Pod that is marked as being in the `READY` state may have a failed readiness gate. To verify this, use the following command:
    
    
    kubectl get pod POD_NAME -o yaml
    

    

The readiness gates and their status are listed in the output.

Resolution
    

Verify that the container image in your Deployment's Pod specification is functioning correctly and is able to respond to health checks. Verify that the health checks are correctly configured.

### Degraded mode errors

Symptoms
    

Starting from GKE version 1.29.2-gke.1643000, you might get the following warnings on your service in the **Logs Explorer** when NEGs are updated:
    
    
    Entering degraded mode for NEG <service-namespace>/<service-name>-<neg-name>... due to sync err: endpoint has missing nodeName field
    

Potential causes
    

These warnings indicate GKE has detected endpoint misconfigurations during an NEG update based on `EndpointSlice` objects, triggering a more in-depth calculation process called degraded mode. GKE continues to update NEGs on a best-effort basis, by either correcting the misconfiguration or excluding the invalid endpoints from the NEG updates.

    

Some common errors are:

  * `endpoint has missing pod/nodeName field`
  * `endpoint corresponds to an non-existing pod/node`
  * `endpoint information for attach/detach operation is incorrect`


Resolution
    

Typically, transitory states cause these events and they are fixed on their own. However, events caused by misconfigurations in custom `EndpointSlice` objects remain unresolved. To understand the misconfiguration, examine the `EndpointSlice` objects corresponding to the service:
    
    
    kubectl get endpointslice -l kubernetes.io/service-name=<service-name>
    

Validate each endpoint based on the error in the event.

To resolve the issue, you must manually modify the `EndpointSlice` objects. The update triggers NEGs to update again. Once the misconfiguration no longer exists, the output is similar to the following:
    
    
    NEG <service-namespace>/<service-name>-<neg-name>... is no longer in degraded mode
    

**Note:** You must not manually edit `EndpointSlice` objects generated by the `EndpointSlice` Controller.

## Errors using Google-managed SSL certificates

This section provides information on how to resolve issues with Google-managed certificates.

### Check events on `ManagedCertificate` and Ingress resources

If you exceed the number of allowed certificates, an event with a `TooManyCertificates` reason is added to the `ManagedCertificate`. You can check the events on a `ManagedCertificate` object using the following command:
    
    
    kubectl describe managedcertificate CERTIFICATE_NAME
    

Replace `CERTIFICATE_NAME` with the name of your `ManagedCertificate`.

If you attach a non-existent `ManagedCertificate` to an Ingress, an event with a `MissingCertificate` reason is added to the Ingress. You can check the events on an Ingress by using the following command:
    
    
    kubectl describe ingress INGRESS_NAME
    

Replace `INGRESS_NAME` with the name of your Ingress.

### Managed certificate not provisioned when domain resolves to IP addresses of multiple load balancers

When your domain resolves to IP addresses of multiple load balancers (multiple Ingress objects), you should create a single `ManagedCertificate` object and attach it to all the Ingress objects. If you instead create many `ManagedCertificate` objects and attach each of them to a separate Ingress, the Certificate Authority might not be able to verify the ownership of your domain and some of your certificates might not be provisioned. For the verification to be successful, the certificate must be visible under all the IP addresses to which your domain resolves to.

Specifically, when your domain resolves to an IPv4 and an IPv6 addresses which are configured with different Ingress objects, you should create a single `ManagedCertificate` object and attach it to both Ingresses.

### Disrupted communication between Google-managed certificates and Ingress

Managed certificates communicate with Ingress using the [`ingress.gcp.kubernetes.io/pre-shared-cert` annotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress#ingress_annotations). You can disrupt this communication if you, for example:

  * Run an automated process that clears the `ingress.gcp.kubernetes.io/pre-shared-cert` annotation.
  * Store a snapshot of Ingress then delete and restore the Ingress from the snapshot. In the meantime, an `SslCertificate` resource listed in the `ingress.gcp.kubernetes.io/pre-shared-cert` annotation might have been deleted. Ingress does not work if any certificates attached to it are missing.



If communication between Google-managed certificates and Ingress is disrupted, delete the contents of the `ingress.gcp.kubernetes.io/pre-shared-cert` annotation and wait for the system to reconcile. To prevent recurrence, ensure that the annotation is not inadvertently modified or deleted.

### Validation errors when creating a Google-managed certificate

`ManagedCertificate` definitions are validated before the `ManagedCertificate` object is created. If validation fails, the `ManagedCertificate` object is not created and an error message is printed. The different error messages and reasons are explained as follows:

#### `spec.domains in body should have at most 100 items`

Your `ManagedCertificate` manifest lists more than 100 domains in the `spec.domains` field. Google-managed certificates support only up to 100 domains.

#### `spec.domains in body should match '^(([a-zA-Z0-9]+|[a-zA-Z0-9][-a-zA-Z0-9]*[a-zA-Z0-9])\.)+[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\.?$'`

You specified an invalid domain name or a wildcard domain name in the `spec.domains` field. The `ManagedCertificate` object does not support wildcard domains (for example, `*.example.com`).

#### `spec.domains in body should be at most 63 chars long`

You specified a domain name that is too long. Google-managed certificates support domain names with at most 63 characters.

### Manually updating a Google-managed certificate

To manually update the certificate so that the certificate for the old domain continues to work until the certificate for the new domain is provisioned, follow these steps:

  1. Create a `ManagedCertificate` for the new domain.
  2. Add the name of the `ManagedCertificate` to the `networking.gke.io/managed-certificates` annotation on the Ingress using a comma-separated list. Don't remove the old certificate name.
  3. Wait until the `ManagedCertificate` becomes Active.
  4. Detach the old certificate from the Ingress and delete it.



When you create a `ManagedCertificate`, Google Cloud creates a Google-managed SSL certificate. You cannot update this certificate. If you update the `ManagedCertificate`, Google Cloud deletes and recreates the Google-managed SSL certificate.

**Warning:** If you update an existing `ManagedCertificate` without first creating and attaching a new certificate to the Ingress, you'll experience a service disruption when Google Cloud deletes and recreates the load balancer and certificate. Attaching a new `ManagedCertificate` prevents disruption because the Ingress has a fallback certificate that it can use with the load balancer.

To provide secure HTTPS encrypted Ingress for your GKE clusters, see example [Secure Ingress](https://github.com/GoogleCloudPlatform/gke-networking-recipes/tree/main/ingress/single-cluster/ingress-https).

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
