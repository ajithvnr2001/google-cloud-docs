---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-intro/
title: Troubleshoot Cloud Service Mesh step-by-step \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:21.001960+00:00
---

# Troubleshoot Cloud Service Mesh step-by-step  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-intro/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Service Mesh step-by-step

This section explains how to troubleshoot and resolve problems when using Cloud Service Mesh. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.28/docs/getting-support).

## Troubleshooting steps

Follow these general steps to troubleshoot Cloud Service Mesh:

  1. Use the automated configuration validation tools.
  2. Check if you have a common problem with a known solution.
  3. Narrow the scope of the problem.
  4. Review relevant logs and information.
  5. Gather diagnostic logs and seek help.

**Note:** If you are unable to troubleshoot manually, see [Gather diagnostic logs and seek help](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-collect-logs) for next steps.

The Cloud Service Mesh diagnostic tool can detect common configuration problems. Install the troubleshooting tool using these [instructions](https://docs.cloud.google.com/service-mesh/v1.28/docs/downloading-istioctl).

## Before you begin

  1. Make sure the kubeconfig context for your cluster is available in your kubeconfig file. If not, then run the following command: 
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CLUSTER_LOCATION --project=PROJECT_NAME
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CLUSTER_LOCATION`: the zone or region for your cluster.
     * `PROJECT_NAME`: the project name.
  2. Verify that the [Application Default Credentials](https://docs.cloud.google.com/authentication/provide-credentials-adc) are created. If they are not, run one of the following commands:
         
         gcloud auth application-default login --billing-project=PROJECT_NAME
         
         
         gcloud auth application-default set-quota-project PROJECT_NAME
         

Replacing `PROJECT_NAME` with the your project name.




## View control plane status

The following commands can help you understand the status of the Cloud Service Mesh control plane:

### Managed

  * Get the list of clients connection status to the Cloud Service Mesh control plane:
        
        gcloud beta container fleet mesh debug proxy-status \
            --membership=MEMBERSHIP_NAME \
            --location=MEMBERSHIP_LOCATION \
            --project=PROJECT_NAME
        

Replace the following:

    * `MEMBERSHIP_NAME`: the name of your membership.
    * `MEMBERSHIP_LOCATION`: the region for your membership. You can check your membership's location with `gcloud container fleet memberships list --project FLEET_PROJECT_ID` replacing `FLEET_PROJECT_ID` with the fleet project ID.
    * `PROJECT_NAME`: the project name.

The following table describes the possible responses.

UNKNOWN | (Default) ⁣Status information is not available or is unknown.  
---|---  
SYNCED | Control plane sent the configuration to the client and received an ACK from the client.  
ERROR | ⁣Control plane sent the configuration to the client and received a NACK from the client.  
STALE | Control plane sent the configuration to the client but did not receive an ACK or a NACK from the client.  
NOT SENT | The configuration was not sent.  
N/A | Not applicable.  
Not supported | Sync status is not supported by our troubleshooting API.  



### In-cluster

  * `kubectl get pods -n istio-system`
  * `kubectl describe -n istio-system`
  * For all pods in istio-system: `kubectl logs -n istio-system -l istio --all-containers`
  * `istioctl version`
  * `istioctl proxy-status`
  * `kubectl get configmap istio -o yaml && kubectl get configmap istio-sidecar-injector -o yaml`
  * `kubectl top pods -n istio-system`



Use the following commands to understand the scale of the deployment:

  * `kubectl get nodes`
  * `kubectl get services --all-namespaces`
  * `kubectl get pods --all-namespaces`



## View proxy configurations

The following command can help you understand the Cloud Service Mesh proxy configurations:

### Managed
    
    
    gcloud beta container fleet mesh debug proxy-config POD_NAME.NAMESPACE \ 
        --type=TYPE \
        --membership=MEMBERSHIP_NAME \
        --location=MEMBERSHIP_LOCATION \
        --project=PROJECT_NAME
    

  * `POD_NAME`: the name of your Pod.
  * `NAMESPACE`: the namespace of your Pod.
  * `TYPE`: One of the following: 
    * bootstrap
    * cluster
    * clusters
    * endpoint
    * endpoints
    * listener
    * listeners
    * log
    * route
    * routes
    * secret
    * secrets
  * `MEMBERSHIP_NAME`: the name of your membership.
  * `MEMBERSHIP_LOCATION`: the region for your membership. You can check your membership's location with `gcloud container fleet memberships list --project FLEET_PROJECT_ID` replacing `FLEET_PROJECT_ID` with the fleet project ID.
  * `PROJECT_NAME`: the project name.



### In-cluster

Use the `istioctl proxy-config` to see proxy configurations for in-cluster control planes. For more information, see [Debugging Envoy and istiod](https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/).

If the problem persists, see the next section to check if your problem is already known.

## Check for common problems and solutions

You can save time by checking if your symptoms match an issue in these common problems and resolutions sections, grouped by Cloud Service Mesh functional area:

  * [Installation issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-installation)
  * [Managed control plane issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/managed/troubleshoot-managed-anthos-service-mesh)
  * [Observability issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-observability)
  * [Off-Google Cloud deployment issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-off-gcp)
  * [Proxy issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-proxy)
  * [Resource issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-resources)
  * [Scaling issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-scaling)
  * [Security issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-security)
  * [Traffic management issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-traffic)
  * [Webhook issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-webhook)
  * [Sidecar proxies issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-sidecar-proxies)



If this does not resolve your issue, see the next section.

## Narrow the scope of the problem

Cloud Service Mesh consists of several technologies working together, which means that certain types of problems are associated with particular functional areas or components. Each of these components generate helpful logs of their own. Before you attempt to manually analyze the volume of information they provide, narrow the scope of your troubleshooting by answering the following questions:

  * Does the issue occur within the control plane or the data plane, for example `istiod` or Envoy proxies?
  * In which functional area are you experiencing the issue, for example Networking, Telemetry, Security, etc.?
  * Is there service-mesh wide traffic loss or in a specific deployment?
  * Does the problem appear or worsen due to lack of ability to scale traffic in service mesh?
  * Does the issue cause latency or other performance issues?
  * Can you reproduce the issue on demand?
  * Did the problem begin after a recent configuration change in Istio, GKE, etc.?
  * Is there an increase or spike in traffic within the service mesh?
  * Does this cluster have any noticeable features enabled or non-typical deployments?
  * Do you observe high CPU or memory utilization? If so, what is the expected usaged at scale?
  * Are there quota restrictions to consider?



## Review relevant logs and information

After you narrow the scope of the problem, you can focus on certain logs and information more effectively. To learn about the logs that Cloud Service Mesh generates and how to interpret the information they contain, see [Interpreting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/accessing-logs#interpret_anthos_service_mesh_logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
