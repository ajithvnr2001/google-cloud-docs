---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/troubleshooting/troubleshoot-collect-logs/
title: Collecting Cloud Service Mesh logs \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:46.314727+00:00
---

# Collecting Cloud Service Mesh logs  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/troubleshooting/troubleshoot-collect-logs/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collecting Cloud Service Mesh logs

The following sections explains how to gather the various Cloud Service Mesh logs for troubleshooting issues or contacting [Google Support](https://cloud.google.com/support-hub).

## Collect logs using the bug report tool

Cloud Service Mesh provides an automated bug report tool that collects the relevant diagnostic logs and lets you attach the logs to a Google Support ticket.

Before you begin, ensure the kubeconfig context for your cluster is available in your kubeconfig file.

### Start the log collection

### Managed control plane

  1. [Download the troubleshooting tool](https://docs.cloud.google.com/service-mesh/v1.21/docs/downloading-istioctl#managed-control-plane).

  2. Run the bug-report tool to collect logs:
         
         gcloud beta container fleet mesh debug bug-report \
            --membership=MEMBERSHIP_NAME \
            --location=MEMBERSHIP_LOCATION \
            --project=PROJECT_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME`: the name of your membership.
     * `MEMBERSHIP_LOCATION`: the region for your membership.
     * `PROJECT_NAME`: the project name.



### In-cluster control plane

  1. [Download the troubleshooting tool](https://docs.cloud.google.com/service-mesh/v1.21/docs/downloading-istioctl#in-cluster-control-plane).

  2. Run the bug-report tool to collect logs:
         
         istioctl bug-report




### Upload your debug archive

The tool creates an archive of your mesh's logs and configuration in the working directory. You can unpack the archive and use the troubleshooting guides to attempt to perform troubleshooting yourself. However, if you have a support package, you can contact [Google Cloud Support](https://cloud.google.com/support-hub), who will provide you with further steps to securely upload your log archive.

**Important:** Archive logs might contain personally identifiable information (PII) or private information about your security certificates. Check your local laws and your organization's policies and procedures regarding how to handle or send such sensitive information externally.

## Manually collect Cloud Service Mesh logs

Instead of using the Cloud Service Mesh bug report tool, this section explains how to manually collect all the relevant logs.

### Envoy access logs

Envoy proxy access logs contain detailed information that is useful for troubleshooting. However, you must enable them and set the correct detail level.

For details about how to interpret the log contents, see [Interpret Envoy logs](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability/accessing-logs#Interpret_Envoy_logs).

#### Enable or disable Envoy logs

To enable the Envoy proxy access logs, configure an [overlay file](https://docs.cloud.google.com/service-mesh/v1.21/docs/unified-install/options/enable-optional-features#direct_envoy_to_stdout) for in-cluster Cloud Service Mesh or a [ConfigMap](https://docs.cloud.google.com/service-mesh/docs/managed/enable-managed-anthos-service-mesh-optional-features#envoy_access_logs) for managed Cloud Service Mesh.

#### Increase logging detail

To temporarily increase the detail level of the logs, use the following command. This setting is undone when the pod is recreated.
    
    
    kubectl -n NAMESPACE debug --image istio/base --target istio-proxy -it POD_NAME -- curl -X POST http://localhost:15000/logging?level=debug

To set the detail level of the logs back to default, use the following command:
    
    
    kubectl -n NAMESPACE debug --image istio/base --target istio-proxy -it POD_NAME -- curl -X POST http://localhost:15000/logging?level=info

#### Write Envoy logs to a folder

To collect the Envoy proxy access logs and store them in a folder, use the following command:
    
    
    kubectl logs -l app=APPLICATION_NAME -c istio-proxy > /FILE_PATH

See [Getting Envoy's Access Logs](https://istio.io/v1.21/docs/tasks/observability/logs/access-log/) for more information.

### Kubernetes logs

Kubernetes generates several logs that contain information about the behavior of Istio components, such as `istiod`, Ingress Gateway, and proxies. You can review these logs for errors, which might narrow the scope of possible causes of a problem.

(In-cluster control plane only) Capture `istiod` logs using the following command:
    
    
    kubectl -n istio-system logs $(kubectl -n istio-system get pods -lapp=istiod -oname) > ./LOGS_FOLDER/istiod.log

(In-cluster control plane only) Capture Istio Ingress Gateway logs using the following command:
    
    
    kubectl -n istio-system logs $(kubectl -n istio-system get pods -lapp=istio-ingressgateway -oname) > /FILE_PATH

Capture Istio Proxy logs using the following command:
    
    
    kubectl -n WORKLOAD_NAMESPACE logs POD_NAME -c istio-proxy > ./LOGS_FOLDER/proxy.log

### Kubernetes configuration dump

This information allows users without direct access to the cluster to view the state of various resources and identify possible configuration problems. The following command writes the Kubernetes configuration to a YAML file:
    
    
    for ns in `kubectl get namespaces -o=jsonpath='{.items[*].metadata.name}'` ; do echo "===NAMESPACE===" $ns >> ./LOGS_FOLDER/kubernetes.yaml ;kubectl get -oyaml -n $ns deploy,statefulset,job,ingress,endpoints,configmap,event,secret,service,istio-io >> ./LOGS_FOLDER/kubernetes.yaml; done

### Envoy core dump

Envoy core dumps are not typically useful to end users, however Google Support might request that you collect it as part of the troubleshooting process, using the following steps.

**Important:** Core dumps might contain personally identifiable information (PII) or private information about your security certificates. Check your local laws and your organization's policies and procedures regarding how to handle or send such sensitive information externally.**Warning:** Configuring an Envoy core dump is a node-wide setting. This feature should only be enabled to debug and then turned off when you are done debugging. Envoy core dumps should not be left on long-term.

To configure the kernel to write Envoy core dumps to a writable directory:

  1. Add the `sidecar.istio.io/enableCoreDump=true` label to a pod.

  2. Restart the pod to enable Envoy core dumps.

  3. Copy the core dump out of the pod.




### Configure Envoy proxy

The detailed Envoy proxy configuration contains additional detail that might be helpful for troubleshooting purposes. You can collect this information using the following command. In this example, ENDPOINT is one of the following (shown in order of importance):

  * /certs
  * /clusters
  * /listeners
  * /config_dump
  * /memory
  * /server_info
  * /stats/prometheus
  * /runtime


    
    
    kubectl debug --image istio/base --target istio-proxy -itq POD_NAME -n NAMESPACE -- curl 127.0.0.1:15000/ENDPOINT > out.log

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
