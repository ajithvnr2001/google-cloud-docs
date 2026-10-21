---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/troubleshooting/troubleshoot-webhook/
title: Resolving sidecar proxy/webhook issues in Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:05.138200+00:00
---

# Resolving sidecar proxy/webhook issues in Cloud Service Mesh  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/troubleshooting/troubleshoot-webhook/

You are viewing archived v1.23 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving sidecar proxy/webhook issues in Cloud Service Mesh

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.23/docs/getting-support).

**Note:** These instructions are only applicable to in-cluster Cloud Service Mesh.

Cloud Service Mesh contains two [webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/):

  * The validating webhook ensures applied Istio configuration is valid.
  * The mutating webhook sets automatic sidecar injection on new pods.



A configuration issue in one of these webhooks might cause new pods to fail start up, or `kubectl apply` generating error messages.

## Sidecar injection problems

If you have provisioned managed Cloud Service Mesh, then [contact support](https://docs.cloud.google.com/service-mesh/v1.23/docs/getting-support).

Sidecar injection is not working correctly if you see any of the following:

  * pods that are scheduling without sidecars
  * pods that should have sidecars injected never appear when using `kubectl get pods`, but the corresponding replica set from `kubectl get replicaset` exists.



Use the following steps to troubleshoot sidecar injection problems.

  1. Verify that your namespace or pod has the correct injection label.

If you are running single-revision Istio (the default), verify that your namespace or pod spec have the istio-injection=enabled label.

If you are running multiple-revision Istio (for zero-downtime migrations, multiple control planes, etc), verify that your namespace or pod spec have the appropriate `istio.io/rev=REVISION` label, where REVISION is the Cloud Service Mesh revision number on `istiod` that corresponds with your selected Cloud Service Mesh version. For more information about revision labels, see [Injecting sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies).

  2. Verify that your istio sidecar injection webhook is present and has a CA bundle.

The sidecar injector webhook (which is used for automatic sidecar injection) requires a CA bundle to establish secure connections with the API server and `istiod`. This CA bundle is patched into the configuration by `istiod`, but can sometimes be overwritten (for example, if you reapply the webhook configuration).

You can verify the presence of the CA bundle using the following command. The command includes `istio-sidecar-injector-asm-1236-11`, which is specific to this version of Cloud Service Mesh. Ensure you use your actual revision if it differs.
         
         kubectl get mutatingwebhookconfigurations.admissionregistration.k8s.io istio-sidecar-injector-asm-1236-11 -o=jsonpath='{.webhooks[0].clientConfig.caBundle}'

If the output is not empty, the CA bundle is configured. If the CA bundle is missing, restart `istiod` to cause it to rescan the webhook and reinstall the CA bundle.

  3. Check for sidecar injection failures.

If you have injection enabled, but are not seeing pods scheduling, check the status of the next higher level of abstraction. For example, if you are running a deployment but no pods are scheduling, check the status of the corresponding replica sets using the following command:
         
         kubectl -n my-namespace describe replicaset your-deployment-name

If the replica set is present, check the events log at the bottom of the description for errors. If the error relates to sidecar injection, check the `istiod` logs for an indication of what is causing the error.

  4. If the problem persists, the issue might be any of the following:

     * Bad configuration passed to the injector
     * Firewall configuration problems
     * A problem in the Istio code itself

See [Troubleshooting Istio](https://github.com/istio/istio/wiki/Troubleshooting-Istio#diagnostics) for additional diagnostic steps.




## Envoy proxies don't receive configuration from `istiod`

There are several issues that can prevent proxies from receiving configuration from `istiod`.

  1. `istiod` will not push configuration to the envoy proxies if it has problems, such as an RBAC issue preventing it from reading its configuration resource.

  2. Discovery address is incorrect ('no healthy upstream' errors)

  3. The discovery address provided to the sidecar injector being incorrect. If you see logs that mention `gRPC config stream closed, no healthy upstream`, check that the discovery address in the mesh [`ProxyConfig`](https://istio.io/v1.23/docs/reference/config/istio.mesh.v1alpha1/#ProxyConfig) is correct and points to your `istiod` service.

  4. Invalid configuration being pushed to the proxy. In this case, configuration is successfully pushed to the proxy, but the configuration is invalid. You will see repeating messages similar to the following:
         
         Envoy proxy is NOT ready: config not received from Pilot (is Pilot running?): cds updates: 1 successful, 0 rejected; lds updates: 0 successful, 1 rejected

In this example, `cds` is the Cluster Discovery Service (which reports 1 update pushed from `istiod`), and `lds` is the Listener Discovery Service (which reports 1 update rejected from `istiod`). Often you will see an earlier error message that explains the reason for the rejection, which usually starts with a warning about envoy configuration or similar.

To fix the issue, investigate the cause of the rejected configuration. One common cause is bad `EnvoyFilter` resources. If no reason is obvious, submit a bug report with a configuration dump of the proxy.




## Pod creation fails

If you observe that pods are not being created successfully, look for error messages that might give clues to the root problem, using the following command:
    
    
    kubectl describe replicaset YOUR_REPLICA_SET

## Common webhook error messages

Error messages output by the `kubectl apply` command can provide a hint about their root cause. See the following table for common error messages, their causes and potential resolutions.

**Error message** | **Cause** | **Resolution**  
---|---|---  
`net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)` | This might be a network connectivity issue. | Ensure that your firewall rules provide connectivity to `istiod` on port 15017.  
`no endpoints available for service 'istiod'` | This can occur if the `istiod` pod is not available or not ready. | Check the `istiod` pods to ensure they are running and ready.  
`Service "istiod" not found` | This can occur if the `istiod` service does not exist. | Verify that your Istio installation was successful and correct.  
`x509: certificate signed by unknown authority` | This might be a webhook certificate issue. | Check that `caBundle` is correctly set on the webhook.  
`Failed to update validatingwebhookconfiguration istio-validator-asm-[version-n]-istio-system (failurePolicy=Fail, resourceVersion=[version]): Operation cannot be fulfilled on validatingwebhookconfigurations.admissionregistration.k8s.io "istio-validator-asm-[version-n]-istio-system": the object has been modified; please apply your changes to the latest version and try again.` | A validating webhook from an old version of Istio or Cloud Service Mesh that has been uninstalled may be interfering with an upgrade or install. | Check that all webhooks still in the cluster and remove any webhook(s) that reference versions which are no longer installed.  
`Error from server (InternalError): Internal error occurred: failed calling webhook "rev.namespace.sidecar-injector.istio.io": Post "https://istiod-asm-1122-0.istio-system.svc:443/inject?timeout=10s": context deadline exceeded` | For private clusters, port 15017 must be open. This error message indicates that port 15017 may not be open. | Ensure that your firewall rules provide connectivity to Istiod on port 15017\. For more information, see [Opening a port on a private cluster](https://docs.cloud.google.com/service-mesh/v1.23/docs/private-cluster-open-port).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
