---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:31.211062+00:00
---

# Troubleshooting  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting strategies as well as solutions for some common errors.

When troubleshooting Knative serving, first confirm that you can [run your container image locally](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/testing/local).

If your application is not running locally, you will need to diagnose and fix it. You should use [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging) to help debug a deployed project.

When troubleshooting Knative serving, consult the following sections for possible solutions to the problem.

## Checking command line output

If you use the Google Cloud CLI, check your command output to see if it succeeded or not. For example if your deployment terminated unsuccessfully, there should be an error message describing the reason for the failure.

Deployment failures are most likely due to either a misconfigured manifest or an incorrect command. For example, the following output says that you must configure route traffic percent to sum to 100.
    
    
    Error from server (InternalError): error when applying patch:</p><pre>{"metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"serving.knative.dev/v11\",\"kind\":\"Route\",\"metadata\":{\"annotations\":{},\"name\":\"route-example\",\"namespace\":\"default\"},\"spec\":{\"traffic\":[{\"configurationName\":\"configuration-example\",\"percent\":50}]}}\n"}},"spec":{"traffic":[{"configurationName":"configuration-example","percent":50}]}}
    to:
    &{0xc421d98240 0xc421e77490 default route-example STDIN 0xc421db0488 264682 false}
    for: "STDIN": Internal error occurred: admission webhook "webhook.knative.dev" denied the request: mutation failed: The route must have traffic percent sum equal to 100.
    ERROR: Non-zero return code '1' from command: Process exited with status 1
    

## Checking logs for your service

You can use Cloud Logging or the Knative serving page in the Google Cloud console to check request logs and container logs. For complete details, read [Logging and viewing logs](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging).

If you use Cloud Logging, the resource you need to filter on is **Kubernetes Container**.

## Checking Service status

Run the following command to get the status of a deployed Knative serving service:
    
    
    gcloud run services describe SERVICE

You can add `--format yaml(status)` or `--format json(status)` to get the full status, for example:
    
    
    gcloud run services describe SERVICE --format 'yaml(status)'

The conditions in `status` can help you locate the cause of failure. Conditions can include `True`, `False`, or `Unknown`:

  * **Ready** : `True` indicates that the service is configured and ready to receive traffic.
  * **ConfigurationReady** : `True` indicates that the underlying [Configuration](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md#configuration) is ready. For `False` or `Unknown`, you should view the status of the latest revision.
  * **RoutesReady** : `True` indicates the underlying [Route](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md#route) is ready. For `False` or `Unknown`, you should view the status of the route.



For additional details on status conditions, see [Knative Error Signaling](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md#error-signalling).

## Checking Route status

Each Knative serving Service manages a [Route](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md#route) that represents the current routing state against the service's revisions.

You can check the overall status of the Route by looking at the service's status:
    
    
    gcloud run services describe SERVICE --format 'yaml(status)'

The **RoutesReady** condition in `status` provides the status of the Route.

You can further diagnose the Route status by running the following command:
    
    
    kubectl get route SERVICE -o yaml

The conditions in `status` provide the reason for a failure. Namely,

  * **Ready** indicates whether the service is configured and has available backends. If this is `true`, the route is configured properly.

  * **AllTrafficAssigned** indicates whether the service is configured properly and has available backends. If this condition's `status` is not `True`:

    * Try checking if the traffic split between revisions for your service adds up to 100%:
          
          gcloud run services describe SERVICE

If not, adjust the traffic split using the [`gcloud run services update-traffic`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update-traffic) command.

    * Try checking the revision status for revisions receiving traffic.

  * **IngressReady** indicates whether the Ingress is ready. If this condition's `status` is not `True`, try checking the ingress status.

  * **CertificateProvisioned** indicates whether Knative certificates have been provisioned. If this condition's `status` is not `True`, try troubleshooting managed TLS issues.




For additional details on status conditions, see [Knative Error Conditions and Reporting](https://github.com/knative/specs/blob/main/specs/serving/knative-api-specification-1.0.md#error-signalling).

### Checking Ingress status

Knative serving uses a load balancer service called `istio-ingressgateway`, which is responsible for handling incoming traffic from outside the cluster.

To obtain the external IP for the Load Balancer, run the following command:
    
    
    kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
    
    
    NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
    istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

If the **EXTERNAL-IP** is `pending`, see EXTERNAL-IP is `pending` for a long time below.

## Checking Revision status

To get the latest revision for your Knative serving service, run the following command:
    
    
    gcloud run services describe SERVICE --format='value(status.latestCreatedRevisionName)'

Run the following command to get the status of a specific Knative serving revision:
    
    
    gcloud run revisions describe REVISION

You can add `--format yaml(status)` or `--format json(status)` to get the full status:
    
    
    gcloud run revisions describe REVISION --format yaml(status)

The conditions in `status` provide the reasons for a failure. Namely,

  * **Ready** indicates whether the runtime resources are ready. If this is `true`, the revision is configured properly.
  * **ResourcesAvailable** indicates whether underlying Kubernetes resources have been provisioned. If this condition's `status` is not `True`, try checking the Pod status.
  * **ContainerHealthy** indicates whether the revision readiness check has completed. If this condition's `status` is not `True`, try checking the Pod status.
  * **Active** indicates whether the revision is receiving traffic.



If any of these conditions' `status` is not `True` try checking the Pod status.

## Checking Pod status

To get the Pods for all your deployments:
    
    
    kubectl get pods

This should list all Pods with brief status. For example:
    
    
    NAME                                                      READY     STATUS             RESTARTS   AGE
    configuration-example-00001-deployment-659747ff99-9bvr4   2/2       Running            0          3h
    configuration-example-00002-deployment-5f475b7849-gxcht   1/2       CrashLoopBackOff   2          36s
    

Choose one and use the following command to see detailed information for its `status`. Some useful fields are `conditions` and `containerStatuses`:
    
    
    kubectl get pod POD-NAME -o yaml

## EXTERNAL-IP is `<pending>` for a long time

Sometimes, you may not get an external IP address immediately after you create a cluster, but instead see the external IP as `pending`. For example you could see this by invoking the command:

To obtain the external IP for the Load Balancer, run the following command:
    
    
    kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
    
    
    NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
    istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

This may mean that you have run out of external IP address quota in Google Cloud. You can check the possible cause by invoking:
    
    
    kubectl describe svc istio-ingressgateway -n INGRESS_NAMESPACE

where INGRESS_NAMESPACE is the namespace of ASM ingress which by default is `istio-system`. This yields output similar to the following: 
    
    
    Name:                     istio-ingressgateway
    Namespace:                INGRESS_NAMESPACE
    Labels:                   app=istio-ingressgateway
                              istio=ingressgateway
                              istio.io/rev=asm-1102-3
                              operator.istio.io/component=IngressGateways
                              operator.istio.io/managed=Reconcile
                              operator.istio.io/version=1.10.2-asm.3
                              release=istio
    Annotations:              kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"labels":{"addonmanager.kubernetes.io/mode":"Reconcile","app":"istio-ingressgateway","...
    Selector:                 app=istio-ingressgateway,istio=ingressgateway
    Type:                     LoadBalancer
    IP:                       10.XX.XXX.XXX
    LoadBalancer Ingress:     35.XXX.XXX.188
    Port:                     http2  80/TCP
    TargetPort:               80/TCP
    NodePort:                 http2  31380/TCP
    Endpoints:                XX.XX.1.6:80
    Port:                     https  443/TCP
    TargetPort:               443/TCP
    NodePort:                 https  3XXX0/TCP
    Endpoints:                XX.XX.1.6:XXX
    Port:                     tcp  31400/TCP
    TargetPort:               3XX00/TCP
    NodePort:                 tcp  3XX00/TCP
    Endpoints:                XX.XX.1.6:XXXXX
    Port:                     tcp-pilot-grpc-tls  15011/TCP
    TargetPort:               15011/TCP
    NodePort:                 tcp-pilot-grpc-tls  32201/TCP
    Endpoints:                XX.XX.1.6:XXXXX
    Port:                     tcp-citadel-grpc-tls  8060/TCP
    TargetPort:               8060/TCP
    NodePort:                 tcp-citadel-grpc-tls  31187/TCP
    Endpoints:                XX.XX.1.6:XXXX
    Port:                     tcp-dns-tls  853/TCP
    TargetPort:               XXX/TCP
    NodePort:                 tcp-dns-tls  31219/TCP
    Endpoints:                10.52.1.6:853
    Port:                     http2-prometheus  15030/TCP
    TargetPort:               XXXXX/TCP
    NodePort:                 http2-prometheus  30944/TCP
    Endpoints:                10.52.1.6:15030
    Port:                     http2-grafana  15031/TCP
    TargetPort:               XXXXX/TCP
    NodePort:                 http2-grafana  31497/TCP
    Endpoints:                XX.XX.1.6:XXXXX
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:
      Type    Reason                Age                  From                Message
      ----    ------                ----                 ----                -------
      Normal  EnsuringLoadBalancer  7s (x4318 over 15d)  service-controller  Ensuring load balancer

If your output contains an indication that the `IN_USE_ADDRESSES` quota was exceeded, you can request additional quota by navigating to the [IAM & Admin page](https://console.cloud.google.com/iam-admin/iam) in the Google Cloud console to request additional quota.

The gateway will continue to retry until an external IP address is assigned. This may take a few minutes.

## Troubleshooting custom domains and managed TLS issues

Use the troubleshooting steps listed below to resolve general issues for [custom domains](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) and the [managed TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls) feature.

### Custom domains for private, internal networks

If you mapped a custom domain to your Knative serving cluster or services within a [private, internal network](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup#setting_up_a_private_internal_network), you must [disable managed TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls#disable-for-cluster) otherwise your domain configuration will fail to achieve the `ready` state. By default, the internal load balancer is not able to communicate externally with the certificate authority.

### Check status of a specific domain mapping

To check the status of a specific domain mapping:

  1. Run the command:
         
         gcloud run domain-mappings describe --domain DOMAIN --namespace NAMESPACE

Replace

     * DOMAIN with the name of the domain you are using.
     * NAMESPACE with the namespace you use for the domain mapping.
  2. In the `yaml` results from this command, examine the condition of the `CertificateProvisioned` field to determine the nature of the error.

  3. If there is an error displayed, it should match one of the errors in the tables below. Follow the suggestions in the tables to resolve the issue.




#### User configuration errors

Error code | Details  
---|---  
DNSErrored  | **Message** : _DNS record is not configured correctly. Need to map domain [XXX] to IP XX.XX.XX.XX_ Follow the instructions provided to configure your DNS record correctly.   
RateLimitExceeded  | **Message** : _acme: urn:ietf:params:acme:error:rateLimited: Error creating new order_   
_:: too many certificates already issued for exact set of domains:_   
_test.your-domain.com:_   
_see https://letsencrypt.org/docs/rate-limits/_ The Let's Encrypt quota has been exceeded. You must increase your [Let's Encrypt](https://letsencrypt.org/docs/rate-limits/) certificate quota for that host.   
InvalidDomainMappingName  | **Message** : _DomainMapping name %s cannot be the same as Route URL host %s._ The DomainMapping name cannot be exactly the same as the host of the Route it maps to. Use a different domain for your DomainMapping name.   
ChallengeServingErrored  | **Message** : _System failed to serve HTTP01 request._ This error can occur if the `istio-ingressgateway` service is not able to serve the request from Let's Encrypt to validate domain ownership. 

  1. Make sure your `istio-ingressgateway` service is accessible from the public internet without using [Virtual Private Cloud](https://docs.cloud.google.com/vpc).
  2. Make sure your `istio-ingressgateway` service accepts requests from the URL `http://DOMAIN/.well-known/acme-challenge/...` where DOMAIN is the domain being validated.

  
  
#### System errors

Error code | Details  
---|---  
OrderErrored  AuthzErrored  ChallengeErrored  | These 3 types of errors occur if the verification of domain ownership by Let's Encrypt fails.  These errors usually are transient errors, and will be retried by Knative serving.  The retry delay is exponential with a minimum 8 seconds and maximum 8 hours.  If you want to manually retry the error, you can manually delete the failed Order.  `kubectl delete order **DOMAIN** -n **NAMESPACE**`  
ACMEAPIFailed  | This type of error occurs when Knative serving fails to call Let's Encrypt. This is usually a transient error, and will be retried by Knative serving.  If you want to manually retry the error, manually delete the failed Order.  `kubectl delete order **DOMAIN** -n **NAMESPACE**`  
UnknownErrored  | This error indicates an unknown system error, which should happen very rarely in the GKE cluster. If you see this, [contact Cloud support](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/support) for debugging help.   
  
### Check Order status

The Order status records the process of interacting with Let's Encrypt, and therefore can be used to debug the issues related to Let's Encrypt. If it is necessary, check the status of Order by running this command:
    
    
    kubectl get order DOMAIN -n NAMESPACE -oyaml

Replace

  * DOMAIN with the name of the domain you are using.
  * NAMESPACE with the namespace you use for the domain mapping.



The results will contain the certificates issued and other information if the order was successful.

### Order Timeout

An Order object will be timed out after 20 minutes if it still cannot get certificates.

  1. Check the domain mapping status. For a timeout, look for an error message such as this in the status output:
         
         order (test.your-domain.com) timed out (20.0 minutes)

  2. A common cause of the timeout issue is that your DNS record is not configured properly to map the domain you are using to the IP address of the ingress service. Run the following command to check the DNS record:
         
         host DOMAIN

  3. Check the external IP address of your ingress load balancer: 

To obtain the external IP for the Load Balancer, run the following command:
         
         kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
         
         NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
         istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

If the external IP address of your domain does not match the ingress IP address, then reconfigure your DNS record to map to the correct IP address.

  4. After the (updated) DNS record becomes effective, run the following command to delete the Order object in order to re-trigger the process of requesting a TLS certificate:
         
         kubectl delete order DOMAIN -n NAMESPACE

Replace

     * DOMAIN with the name of the domain you are using.
     * NAMESPACE with the namespace you use.



### Authorization Failures

Authorization failures can occur when a DNS record is not propagated globally in time. As a result, Let's Encrypt fails to verify the ownership of the domain.

  1. Check Order status. Find out the authz link under the `acmeAuthorizations` field of status. The URL should look like this:
         
         https://acme-v02.api.letsencrypt.org/acme/authz-v3/1717011827

  2. Open the link. If you see a message similar to: 
         
         urn:ietf:params:acme:error:dns

then the issue is due to incomplete DNS propagation.

  3. To resolve the DNS propagation error:

     1. Check the external IP address of your ingress load balancer: 

To obtain the external IP for the Load Balancer, run the following command:
            
            kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
            
            NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
            istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

     2. Check your DNS record for the domain by running the following command: 
            
            host DOMAIN

If the IP address of the DNS record does not match the external IP of the ingress load balancer, configure your DNS record to map the user's domain to the external IP.

     3. After the (updated) DNS record becomes effective, run the following command to delete the Order object to re-trigger the process of requesting a TLS certificate:
            
            kubectl delete order DOMAIN -n NAMESPACE

Replace

     * DOMAIN with the name of the domain you are using.
     * NAMESPACE with the namespace you use for the domain mapping.



## Deployment to private cluster failure: Failed calling webhook error

Your firewall may not be set up properly if your deployment to a private cluster fails with the message:
    
    
    Error: failed calling webhook "webhook.serving.knative.dev": Post
    https://webhook.knative-serving.svc:443/?timeout=30s: context deadline exceeded (Client.Timeout
    exceeded while awaiting headers)
    

For information on firewall changes required to support deployment to a private cluster, see [enabling deployments on a private cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup#enabling_deployments_on_a_private_cluster).

## Services report status of IngressNotConfigured

If `IngressNotConfigured` shows up in your service status, you may need to restart the `istiod` deployment in the `istio-system` namespace if you are using in-cluster control plane Cloud Service Mesh. This error, which has been observed more frequently on kubernetes `1.14`, can occur if the services are created before `istiod` is ready to begin its work of reconciling `VirtualServices` and pushing envoy configuration to the ingress gateways.

To fix this issue, scale the deployment in and then back out again using commands similar to the following:
    
    
    kubectl scale deployment istiod -n istio-system --replicas=0
    kubectl scale deployment istiod -n istio-system --replicas=1
    

## Missing request count and request latency metrics

Your service may not report revision request count and request latency metrics if you have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled and have not granted certain permissions to the service account used by your service.

You can fix this by following the steps in the [Enabling metrics on a cluster with Workload Identity Federation for GKE section](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/workload-identity#enabling_metrics_on_a_cluster_with_workload_identity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
