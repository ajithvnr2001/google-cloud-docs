---
url: https://docs.cloud.google.com/apigee/docs/support/best-practices/
title: Best practices for Google Cloud Apigee support cases \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:49.668321+00:00
---

# Best practices for Google Cloud Apigee support cases  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/support/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Best practices for Google Cloud Apigee support cases Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/best-practices) documentation._

Providing detailed and required information in the support case makes it easier for the Google Cloud Support team to respond to you quickly and efficiently. When your support case is missing critical details, we need to ask for more information, which may involve going back and forth multiple times. This takes more time and can lead to delays in resolution of issues. This **Best Practices Guide** lets you know the information we need to resolve your technical support case faster. 

## Describing the issue

An issue should contain information explaining the details about what happened versus what was expected to happen, as well as when and how it happened. A good support case should contain the following key information for each of the Apigee products: 

**Note:** For more information about the different Apigee products, see [ Compare Apigee products](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-apigee-products). Key information | Description | Apigee on Google Cloud | Apigee hybrid  
---|---|---|---  
**Product** | Specific Apigee product in which the problem is being observed, including version information where applicable. |  | 

  * Hybrid version

  
**Problem details** | Clear and detailed problem description which outlines the issue, including the complete error message, if any. | 

  * Error message
  * Debug tool output
  * Steps to reproduce problem
  * Complete API request/command

| 

  * Error message
  * Debug tool output
  * Steps to reproduce problem
  * Complete API request/command
  * Component diagnostic logs
  * Cloud Monitoring metrics

  
**Time** | The specific timestamp when the issue started and how long it lasted. | 

  * Date, time, and timezone of problem occurrence
  * Duration of the problem

| 

  * Date, time, and timezone of problem occurrence
  * Duration of the problem

  
**Setup** | Detailed information where the problem is being observed. | 

  * Org name
  * Env name
  * API proxy name
  * Revision

| 

  * Network topology
  * Google Cloud project name
  * Hybrid org name
  * Hybrid env name
  * [ Hybrid runtime platform and its version](https://cloud.google.com/apigee/docs/hybrid/v1.3/install-before-begin)
  * Kubernetes cluster name and region

  
  
The following sections describe these concepts in greater detail. 

### Product

There are different Apigee products, **Apigee on Google Cloud** and **Apigee hybrid** , so we need specific information about which particular product is having the issue. 

The following table provides some examples showing complete information in the **DOs** column, and incomplete information in the **DON'Ts** column: 

DOs |  DON'Ts  
---|---  
Deployment of API proxy `OAuth2` failed on our **Apigee on Google Cloud** org ... |  Deployment of API proxy failed  (We need to know Apigee product in which you are seeing the issue.)   
We are getting the following error while accessing Cassandra using `cqlsh` on **Apigee hybrid version 1.3**... |  We are unable to access Cassandra using `cqlsh`.  (Hybrid version information is missing)   
  
### Problem details

Provide the precise information about the issue being observed including the error message (if any) and expected and actual behaviour observed. 

The following table provides some examples showing complete information in the **DOs** column, and incomplete information in the **DON'Ts** column: 

DOs |  DON'Ts  
---|---  
New `edgemicro` proxy `edgemicro_auth` is failing with the following error: 
    
    
    {"error":"missing_authorization","error_description":"Missing Authorization header"}

|  New `edgemicro` proxy created today not working  (The proxy name is unknown. It is not clear whether the proxy is returning an error or any unexpected response.)   
Our clients are getting `500` errors with the following error message while making requests to API proxy: 
    
    
    {"fault":{"faultstring":"Execution of JSReadResponse failed with error: Javascript runtime error: \"TypeError: Cannot read property \"content\" from undefined. (JSReadResponse.js:23)","detail":{"errorcode":"steps.javascript.ScriptExecutionFailed"}}}

|  Our clients are getting `500` Errors while making requests to API proxy.  (Just conveying `500` Errors doesn't provide adequate information for us to investigate the issue. We need to know the actual error message and error code that is being observed.)   
  
### Time

Time is a very critical piece of information. It is important for the Support Engineer to know when you first noticed this issue, how long it lasted, and if the issue is still going on. 

The Support Engineer resolving the issue may not be in your timezone, so relative statements about time make the problem harder to diagnose. Hence, it is recommended to use the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format for the date and time stamp to provide the exact time information on when the issue was observed. 

The following table provides some examples showing accurate time and duration for which the problem occurred in the **DOs** column, and ambiguous or unclear information on when the problem occurred in the **DON'Ts** column: 

DOs |  DON'Ts  
---|---  
Huge number of `503s` were observed yesterday between **2020-11-06 17:30 PDT** and **2020-11-06 17:35 PDT**... |  Huge number of `503s` were observed yesterday at 5:30pm for 5 mins.  (We are forced to use the implied date and it is also unclear in which timezone this issue was observed.)   
High latencies were observed on the following API Proxies from **2020-11-09 15:30 IST** to**2020-11-09 18:10 IST** ... |  High latencies were observed on some API Proxies last week.  (It is unclear which day and duration this issue was observed in the last week.)   
  
### Setup

We need to know the details about where exactly you are seeing the issue. Depending on the product you are using, we need the following information: 

  * If you are using **Apigee on Google Cloud** , you may have more than one organization, so we need to know the specific org and other details where you are observing the issue: 
    * Organization and Environment names
    * API proxy name and revision numbers (for API request failures)
  * If you are using **hybrid** , you may be using one of the many supported [ hybrid platforms](https://cloud.google.com/apigee/docs/hybrid/v1.3/install-before-begin) and installation topologies. So we need to know what hybrid platform and topology you are using, including the details such as number of data centres and nodes. 



The following table provides some examples showing complete information in the **DOs** column, and incomplete information in the **DON'Ts** column: 

DOs |  DON'Ts  
---|---  
`401` Errors have increased on **Apigee on Google Cloud** since **2020-11-06 09:30 CST**.  **Apigee setup details:** Details of the failing API are as follows:   
Org names: `myorg`   
Env names: `test`   
API proxy names: `myproxy`   
Revision numbers: `3` **Error:**
    
    
    {"fault":{"faultstring":"Failed to resolve API Key variable request.header.X-APP-API_KEY","detail":{"errorcode":"steps.oauth.v2.FailedToResolveAPIKey"}}}

|  `401` Errors have increased.  (It does not give any information on the product being used, since when the issue is being observed or any setup details.)   
Debug is failing with the following error on **Apigee hybrid version 1.3** **Error:** `Error while Creating trace session for corp-apigwy-discovery, revision 3, environment dev. ` `Failed to create DebugSession {apigee-hybrid-123456 dev corp-apigwy-discovery 3 ca37384e-d3f4-4971-9adb-dcc36c392bb1}` **Apigee hybrid setup details:**

  * **Apigee hybrid platform:**   
Anthos GKE on-prem version 1.4.0 
  * **Google Cloud project, hybrid organization and environment**   
Google Cloud Project ID: `apigee-hybrid-123456`   
Apigee hybrid org: `apigee-hybrid-123456`   
Apigee hybrid env: `dev`
  * **Kubernetes cluster name details**   
k8sCluster:   
name: `user-cluster-1`   
region: `us-east1`
  * **Network topology**   
Attached the file `network-topology.png`. 

| Debug is failing on **Apigee hybrid.**  
  
### Useful artifacts

Providing us with artifacts related to the issue will speed up the resolution, as it helps us understand the exact behavior you are observing and get more insights into it. 

**Caution:** Do not share any confidential or sensitive information such as username, password, API Keys, OAuth tokens, or private key associated with your TLS certificates in the case description, updates or file attachments. 

This section describes some useful artifacts that are helpful for all Apigee products: 

#### Common artifacts for all Apigee products 

The following artifacts are useful for all Apigee products: **Apigee on Google Cloud** and **Apigee hybrid** : 

Artifact | Description  
---|---  
[Debug tool output](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) | The Debug tool output contains detailed information about the API requests flowing through Apigee products. This is useful for any runtime errors such as `4XX`, `5XX`, and latency issues.  
Screenshots | Screenshots help relay the context of the actual behaviour or error being observed. It is helpful for any errors or issues observed, such as in the UI or Analytics.  
[HAR (Http ARchive)](https://toolbox.googleapps.com/apps/har_analyzer/) | HAR is a file that is captured by HTTP session tools for debugging any UI related issues. This can be captured using browsers such as Chrome, Firefox, or Internet Explorer.  
[ `tcpdumps`](https://docs.apigee.com/api-platform/troubleshoot/diagnostic-tools-and-logs#tcpippacketsniffertcpdumputility) | The `tcpdump` tool captures TCP/IP packets transferred or received over the network. This is useful for any network-related issues such as TLS handshake failures, `502` errors, and latency issues, etc.  
  
#### Additional artifacts for hybrid

For hybrid, we may need some additional artifacts that will facilitate faster diagnosis of issues. 

Artifact | Description  
---|---  
Apigee hybrid platform | Specify any of the following [ supported hybrid platforms](https://cloud.google.com/apigee/docs/hybrid/v1.3/install-before-begin#supported-platforms) that are used: 

  * GKE
  * GKE on-prem
  * AKS (Azure Kubernetes Service)
  * Amazon EKS
  * GKE on AWS

  
Apigee hybrid and dependent component versions | 

  * **Apigee hybrid CLI version:**   
`apigeectl` version
  * **Apigee Connect Agent version:**   
`kubectl -n=apigee get pods -l app=apigee-connect-agent -o=json | jq '.items[].spec.containers[].image'`
  * **Apigee MART version:**   
`kubectl -n=apigee get pods -l app=apigee-mart -o=json | jq '.items[].spec.containers[].image'`
  * **Apigee Synchronizer version:**   
`kubectl -n=apigee get pods -l app=apigee-synchronizer -o=json | jq '.items[].spec.containers[].image'`
  * **Apigee Cassandra version:**   
`kubectl -n=apigee get pods -l app=apigee-cassandra -o=json | jq '.items[].spec.containers[].image'`
  * **Apigee Runtime version:**   
`kubectl -n=apigee get pods -l app=apigee-runtime -o=json | jq '.items[].spec.containers[].image'`
  * **Kubernetes CLI and server versions:**   
`kubectl` version
  * **Istio CLI and server versions:**   
`istioctl` version

  
Network topology | The Apigee installation topology diagram describing your hybrid setup including all the data centers, Kubernetes clusters, namespaces, and pods.  
Overrides YAML File  | The `overrides.yaml` file used in each data center for installing Apigee hybrid runtime plane.   
Status of Apigee hybrid deployment |  The output of the following commands in each data center/Kubernetes cluster: `kubectl get pods -A`   
`kubectl get services -A`  
Apigee hybrid component logs |  Provide links to Cloud Operations (StackDriver) logs for the hybrid components OR You can fetch the Apigee hybrid component logs using the following commands in each data center/Kubernetes cluster and share them with us: `kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {pod-name}`

  * **Apigee Connect Agent logs:**   
`kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {apigee-connect-agent-pod-name}`
  * **[MART logs](https://cloud.google.com/apigee/docs/hybrid/v1.3/mart-logs):**   
`kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {apigee-mart-pod-name}`
  * **Synchronizer logs:**   
`kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {synchronizer-pod-name}`
  * **Apigee Cassandra logs:**   
`kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {apigee-cassandra-pod-name}`
  * **[MP/Apigee Runtime logs](https://cloud.google.com/apigee/docs/hybrid/v1.3/ts-message-processor) (of all apigee-runtime pods):**   
`kubectl -n {namespace} get pods`   
`kubectl -n {namespace} logs {apigee-runtime-pod-name}`

  
Describe logs |  Detailed information about the pod. This is useful especially if you are observing issues such as pods getting stuck in the `CrashLoopBackoff` state. `kubectl -n apigee describe pod {pod-name}`  
Cloud Monitoring | 

  * Link to your metrics Dashboard
  * Snapshots of any dashboards related to Cloud Monitoring Metrics.

  
  
###  Apigee hybrid must-gather 

You can also execute the **Must-Gather** script based on the commands listed below; 
    
    
    ###--- "kubectl config" commands to get the config details of the whole Apigee Hybrid cluster ---####
    
    kubectl config get-clusters 2>&1 | tee /tmp/k_config_get_clusters_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl config get-contexts 2>&1 | tee /tmp/k_config_get_contexts_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl config get-users 2>&1 | tee /tmp/k_config_get_users_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl config view 2>&1 | tee /tmp/k_config_view_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ### --- Collect all details of all nodes in the Kubernetes cluster.---###
    
    kubectl describe node 2>&1 |  tee /tmp/k_describe_node_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###--- "kubectl get -A " commands to get CRD details for the whole Apigee Hybrid setup ---####
    
    kubectl get clusterissuers -A -o wide 2>&1 | tee /tmp/k_get_clusterissuers_all$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get certificate -A -o wide 2>&1 | tee /tmp/k_get_certificate_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get certificaterequest -A -o wide 2>&1 | tee /tmp/k_get_certificaterequest_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get crd -A -o yaml 2>&1 | tee /tmp/k_get_crd_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ConfigMap -A 2>&1 | tee /tmp/k_get_ConfigMap_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ClusterRole -A -o wide 2>&1 | tee /tmp/k_get_clusterrole_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ClusterRoleBinding -A -o wide 2>&1 | tee /tmp/k_get_clusterrole_binding_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get Deployments -A -o wide >&1 | tee /tmp/k_get_deployments_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get events -A -o wide 2>&1 | tee /tmp/k_get_events_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get endpoints -A  2>&1 | tee /tmp/k_get_endpoints_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get issuers -A -o wide 2>&1 | tee /tmp/k_get_issuers_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get mutatingwebhookconfigurations  2>&1 | tee /tmp/k_get_mutatingwebhookconfigurations_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get nodes -o wide --show-labels 2>&1 | tee /tmp/k_get_nodes_labels_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ns 2>&1 | tee /tmp/k_get_namespace_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get PriorityClass -A -o wide 2>&1 | tee /tmp/k_get_PriorityClass_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get pv -A -o wide 2>&1 | tee /tmp/k_get_pv_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get pvc -A -o wide 2>&1 | tee /tmp/k_get_pvc_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get Role -A -o wide 2>&1 | tee /tmp/k_get_role_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get RoleBinding -A -o wide 2>&1 | tee /tmp/k_get_Role_Binding_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get replicaset -A -o wide 2>&1 | tee /tmp/k_get_replicaset_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get sa -A -o wide 2>&1 | tee /tmp/k_get_service_accounts_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get services -A -o wide 2>&1 | tee /tmp/k_get_services_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get svc -A 2>&1 | tee /tmp/k_get_svc_all$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get secrets -A 2>&1 | tee /tmp/k_get_secrets_all_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get validatingwebhookconfigurations -A  2>&1  | tee /tmp/k_get_validatingwebhookconfigurations_all$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get validatingwebhookconfigurations apigee-validating-webhook-configuration 2>&1  | tee /tmp/k_get_apigee-validating-webhook-configuration_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ### --- List top resource consuming nodes and pods ---####
    
    kubectl top nodes 2>&1 | tee /tmp/k_top_nodes_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl top pod -A --containers 2>&1 | tee /tmp/k_top_pod_all_containers_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###----- "kubectl get" commands to fetch list of all CRD for "apigee" namespace ----- #####
    
    kubectl get all -n apigee -o wide 2>&1 | tee /tmp/k_get_all_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ad -n apigee 2>&1 | tee /tmp/k_get_ad_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get apigeeorganization -n apigee 2>&1 | tee /tmp/k_get_apigeeorganization_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get apigeeenv -n apigee  2>&1 | tee /tmp/k_get_apigeeenv_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get apigeeds -n apigee  2>&1 | tee /tmp/k_get_apigeeds_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get apigeedatastore -n apigee 2>&1 | tee /tmp/k_get_apigeedatastore_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ApigeeDeployment -n apigee 2>&1 | tee /tmp/k_get_apigeedeployment_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ApigeeRedis -n apigee 2>&1 | tee /tmp/k_get_ApigeeRedis_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ApigeeRoute -n apigee 2>&1 | tee /tmp/k_get_ApigeeRoute_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ApigeeRouteConfig -n apigee 2>&1 | tee /tmp/k_get_ApigeeRoutesconfig_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get Apigeetelemetry -n apigee 2>&1 | tee /tmp/k_get_Apigeetelemetry_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get apigeeissues -n apigee 2>&1 | tee /tmp/k_get_apigeeissues_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get ControllerRevision -n apigee -o wide 2>&1 | tee /tmp/k_get_ControllerRevision_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get cronjob -n apigee -o wide 2>&1 | tee /tmp/k_get_cronjob_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get gateway -n apigee 2>&1 | tee /tmp/k_get_gateway_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get PodDisruptionBudget -n apigee -o wide 2>&1 | tee /tmp/k_get_PodDisruptionBudget_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get sc -n apigee -o wide 2>&1 | tee /tmp/k_get_storageclass_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get sr -n apigee -o wide 2>&1 | tee /tmp/k_get_sr_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get sts -n apigee 2>&1 | tee /tmp/k_get_sts_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get volumesnapshot -n apigee -o wide 2>&1 | tee /tmp/k_get_volumesnapshot_n_apigee_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###----- "kubectl describe" commands to fetch details of all CRD for "apigee" namespace ----- #####
    
    for p in $(kubectl -n apigee get apigeeorganization --no-headers -o custom-columns=":metadata.name") ; do kubectl describe apigeeorganization ${p} -n apigee 2>&1 | tee /tmp/k_desc_apigeeorganization_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get apigeeenv --no-headers -o custom-columns=":metadata.name") ; do kubectl describe apigeeenv ${p} -n apigee 2>&1 | tee /tmp/k_desc_apigeeenv_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get apigeeds --no-headers -o custom-columns=":metadata.name") ; do kubectl describe apigeeds ${p} -n apigee 2>&1 | tee /tmp/k_desc_apigeeds_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get apigeedatastore --no-headers -o custom-columns=":metadata.name") ; do kubectl describe apigeedatastore ${p} -n apigee 2>&1 | tee /tmp/k_desc_apigeedatastore_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get ApigeeDeployment --no-headers -o custom-columns=":metadata.name") ; do kubectl describe ApigeeDeployment ${p} -n apigee 2>&1 | tee /tmp/k_desc_ApigeeDeployment_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get ApigeeRedis --no-headers -o custom-columns=":metadata.name") ; do kubectl describe ApigeeRedis ${p} -n apigee 2>&1 | tee /tmp/k_desc_ApigeeRedis_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get ApigeeRoute --no-headers -o custom-columns=":metadata.name") ; do kubectl describe ApigeeRoute ${p} -n apigee 2>&1 | tee /tmp/k_desc_ApigeeRoute_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get ApigeeRouteConfig --no-headers -o custom-columns=":metadata.name") ; do kubectl describe ApigeeRouteConfig ${p} -n apigee 2>&1 | tee /tmp/k_desc_ApigeeRouteConfig_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get Apigeetelemetry --no-headers -o custom-columns=":metadata.name") ; do kubectl describe Apigeetelemetry ${p} -n apigee 2>&1 | tee /tmp/k_desc_Apigeetelemetry_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get apigeeissues --no-headers -o custom-columns=":metadata.name") ; do kubectl describe apigeeissues ${p} -n apigee 2>&1 | tee /tmp/k_desc_apigeeissues_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get ControllerRevision --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe ControllerRevision ${p} 2>&1 | tee /tmp/k_desc_ControllerRevision_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get certificate --no-headers -o custom-columns=":metadata.name") ; do kubectl describe certificate ${p} -n apigee 2>&1 | tee /tmp/k_desc_certificate_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get cronjob --no-headers -o custom-columns=":metadata.name") ; do kubectl describe cronjob ${p} -n apigee 2>&1 | tee /tmp/k_desc_cronjob_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get daemonset --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe daemonset ${p} 2>&1 | tee /tmp/k_desc_daemonset_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get deployments --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe deployments ${p} 2>&1 | tee /tmp/k_desc_deployment_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get hpa --no-headers -o custom-columns=":metadata.name") ; do kubectl describe hpa ${p} -n apigee 2>&1 | tee /tmp/k_desc_hpa_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get jobs --no-headers -o custom-columns=":metadata.name") ; do kubectl describe jobs ${p} -n apigee 2>&1 | tee /tmp/k_desc_jobs_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe po ${p} 2>&1 | tee /tmp/k_desc_pod_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get PodDisruptionBudget --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe PodDisruptionBudget ${p} 2>&1 | tee /tmp/k_desc_PodDisruptionBudget_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get pv --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe pv ${p} 2>&1 | tee /tmp/k_desc_pv_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt; done
    for p in $(kubectl -n apigee get pvc --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe pvc ${p} 2>&1 | tee /tmp/k_desc_pvc_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt; done
    for p in $(kubectl -n apigee get rs --no-headers -o custom-columns=":metadata.name") ; do kubectl describe rs ${p} -n apigee 2>&1 | tee /tmp/k_desc_replicaset_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get sc --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe sc ${p} 2>&1 | tee /tmp/k_desc_storageclass_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt; done
    for p in $(kubectl -n apigee get sts --no-headers -o custom-columns=":metadata.name") ; do kubectl describe sts ${p} -n apigee 2>&1 | tee /tmp/k_desc_sts_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get secrets --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee describe secrets ${p} 2>&1 | tee /tmp/k_desc_secrets_n_apigee${p}_$(date +%Y.%m.%d_%H.%M.%S).txt; done
    for p in $(kubectl -n apigee get services --no-headers -o custom-columns=":metadata.name") ; do kubectl describe service ${p} -n apigee 2>&1 | tee /tmp/k_desc_services_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get sa --no-headers -o custom-columns=":metadata.name") ; do kubectl describe sa ${p} -n apigee 2>&1 | tee /tmp/k_desc_service_account_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee get svc --no-headers -o custom-columns=":metadata.name") ; do kubectl describe svc ${p} -n apigee 2>&1 | tee /tmp/k_desc_svc_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    
    ###----- "kubectl logs" command to fetch logs of all containers in the "apigee" namespace ----- #####
    
    for p in $(kubectl -n apigee get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee logs ${p} --all-containers 2>&1 | tee /tmp/k_logs_n_apigee_${p}_$(date +%Y.%m.%d_%H.%M.%S).log ; done
    
    ###----- "kubectl get" commands for "apigee-system" namespace ----- #####
    
    kubectl get all -n apigee-system -o wide 2>&1 | tee /tmp/k_get_all_n_apigee_system_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get jobs -o wide -n apigee-system 2>&1 | tee /tmp/k_get_jobs_n_apigee_system_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###----- "kubectl describe" commands for "apigee-system" namespace ----- #####
    
    for p in $(kubectl -n apigee-system get certificate --no-headers -o custom-columns=":metadata.name") ; do kubectl describe certificate ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_certificate_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get deployment --no-headers -o custom-columns=":metadata.name") ; do kubectl describe deployment ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_deployment_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get jobs --no-headers -o custom-columns=":metadata.name") ; do kubectl describe jobs ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_jobs_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee-system describe po ${p} 2>&1 | tee /tmp/k_desc_pod_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get rs --no-headers -o custom-columns=":metadata.name") ; do kubectl describe rs ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_replicaset_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get rolebinding --no-headers -o custom-columns=":metadata.name") ; do kubectl describe rolebinding ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_rolebinding_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get services --no-headers -o custom-columns=":metadata.name") ; do kubectl describe service ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_services_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get sa --no-headers -o custom-columns=":metadata.name") ; do kubectl describe sa ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_serviceaccount_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n apigee-system get secrets --no-headers -o custom-columns=":metadata.name") ; do kubectl describe secrets ${p} -n apigee-system 2>&1 | tee /tmp/k_desc_secrets_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    
    ###----- "kubectl logs" command for "apigee-system" namespace ----- #####
    
    for p in $(kubectl -n apigee-system get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n apigee-system logs ${p} --all-containers 2>&1 | tee /tmp/k_logs_n_apigee_system_${p}_$(date +%Y.%m.%d_%H.%M.%S).log ; done
    
    ###----- "kubectl get" command for "cert-manager" namespace ----- #####
    
    kubectl get all -n cert-manager -o wide 2>&1 | tee /tmp/k_get_all_n_cert_manager_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl get crd -n cert-manager 2>&1 | tee /tmp/k_get_crd_n_cert_manager_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###----- "kubectl describe" command for "cert-manager" namespace ----- #####
    
    for p in $(kubectl -n cert-manager get deployment  --no-headers -o custom-columns=":metadata.name") ; do kubectl -n cert-manager describe deployment $(p) 2>&1 | tee /tmp/k_desc_deployment_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get endpoints --no-headers -o custom-columns=":metadata.name") ; do kubectl describe endpoints ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_endpoints_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n cert-manager describe po ${p} 2>&1 | tee /tmp/k_desc_po_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get rs --no-headers -o custom-columns=":metadata.name") ; do kubectl describe rs ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_replicaset_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get sa --no-headers -o custom-columns=":metadata.name") ; do kubectl describe sa ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_serviceaccount_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get secrets --no-headers -o custom-columns=":metadata.name") ; do kubectl describe secrets ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_secrets_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get services --no-headers -o custom-columns=":metadata.name") ; do kubectl describe service ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_service_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    for p in $(kubectl -n cert-manager get svc --no-headers -o custom-columns=":metadata.name") ; do kubectl describe svc ${p} -n cert-manager 2>&1 | tee /tmp/k_desc_svc_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt ; done
    
    ###----- "kubectl logs" command for "cert-manager" namespace ----- #####
    
    for p in $(kubectl -n cert-manager get po --no-headers -o custom-columns=":metadata.name") ; do kubectl -n cert-manager logs ${p} --all-containers 2>&1 | tee /tmp/k_logs_n_cert_manager_${p}_$(date +%Y.%m.%d_%H.%M.%S).log ; done

Once logs are generated compress all the output file in a single tar ball using the below command; 
    
    
    	# tar -cvzf /tmp/apigee_hybrid_logs_$(date +%Y.%m.%d_%H.%M).tar.gz /tmp/k_*

In case the size of the tar file is larger than 25MB you can upload it to google drive and share the link with us. Or you can use the split command to break the large files into 25MB chunks that can be uploaded to the Support portal. 
    
    
    	# split -b 25M diagnostic.tar.gz "diagnostic.tar.gz.part"

### Apigee hybrid Cassandra must-gather

#### Collect basic data

Provide the following information:

  * Apigee hybrid platform (GKE, GKE on-prem, AKS, EKS, etc.)
  * Apigee hybrid version
  * Google Cloud project ID
  * Apigee hybrid organization
  * Apigee hybrid environment
  * Is this a single or multi-region deployment?
  * The `overrides.yaml` file (one for each cluster)
  * How many Apigee hybrid organizations are installed on one cluster?
  * Have there been any recent changes?

**Important:** The overrides YAML file is essential for troubleshooting. 

#### Gather Cassandra debugging information
    
    
    Run the below script to capture Cassandra debugging information from an Apigee hybrid cluster:
    
    
    # Create a temporary directory to store the Cassandra debugging information.
    mkdir /tmp/apigee-cassandra-debug-info/
    
    # Loop through all Cassandra pods
    for APIGEE_CASSANDRA_POD in $(kubectl -n apigee get pods -l app=apigee-cassandra --no-headers -o custom-columns=":metadata.name") ; do
    
      # Get Cassandra version
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD version' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_version_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get Cassandra datacenter status
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD status' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_status_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get Cassandra cluster information
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD describecluster' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_describecluster_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get current ring/token status across the datacenter
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD ring' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_ring_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get more information about heap usage, uptime, exceptions, etc
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD info' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_info_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get gossip info
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD gossipinfo' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_gossipinfo_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get Cassandra compaction details
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD compactionstats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_compactionstats_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD compactionhistory' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_compactionhistory_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD getcompactionthroughput' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_getcompactionthroughput_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD getconcurrentcompactors' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_getconcurrentcompactors_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get status of current Cassandra operations
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD tablestats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_tablestats_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD tpstats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_tpstats_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD netstats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_netstat_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD tablestats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_tablestats_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD gcstats' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_gcstats_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
      # Get proxy histograms (shows the full request latency recorded by the coordinator)
      kubectl -n apigee exec $APIGEE_CASSANDRA_POD -- bash -c 'nodetool -u $APIGEE_JMX_USER -pw $APIGEE_JMX_PASSWORD proxyhistograms' 2>&1 | tee /tmp/apigee-cassandra-debug-info/nodetool_proxyhistograms_$APIGEE_CASSANDRA_POD-$(date +%Y.%m.%d_%H.%M.%S).txt
    
    done
    
    # compress all collected data
    tar -czvf apigee-cassandra-debug-info-$(date +%Y.%m.%d_%H.%M.%S).tar.gz -C /tmp apigee-cassandra-debug-info

### Apigee hybrid MCP must-gather

Run the following script when opening a support case that involves the Apigee hybrid Model Context Protocol (MCP) data plane. The script collects MCP pod state, sidecar and data plane container logs, MCP resources (`ApigeeDeployment`, `Service`, `HPA`, `ApigeeRoute`), and the Message Processor `hostAliases` that route MCP tool traffic to the MCP data plane.

**Note:** Also run the general Apigee hybrid must-gather script alongside this one. This MCP-focused script only collects MCP-specific resources; the general script covers the broader cluster state that support needs to correlate MCP behavior with the rest of the Apigee hybrid installation. 
    
    
    # Create a temporary directory to store the MCP debugging information.
    mkdir -p /tmp/apigee-mcp-debug-info/
    
    ###--- MCP pod state ---###
    
    kubectl -n apigee get pod -l app=apigee-mcp-server -o wide 2>&1 | tee /tmp/apigee-mcp-debug-info/k_get_pod_mcp_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl -n apigee describe pod -l app=apigee-mcp-server 2>&1 | tee /tmp/apigee-mcp-debug-info/k_desc_pod_mcp_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###--- MCP resources: ApigeeDeployment (CRD, not vanilla Deployment), Service, HPA ---###
    
    kubectl -n apigee get apigeedeployment -l app=apigee-mcp-server -o yaml 2>&1 | tee /tmp/apigee-mcp-debug-info/k_get_apigeedeployment_mcp_$(date +%Y.%m.%d_%H.%M.%S).yaml
    kubectl -n apigee describe apigeedeployment -l app=apigee-mcp-server 2>&1 | tee /tmp/apigee-mcp-debug-info/k_desc_apigeedeployment_mcp_$(date +%Y.%m.%d_%H.%M.%S).txt
    kubectl -n apigee get svc -l app=apigee-mcp-server -o yaml 2>&1 | tee /tmp/apigee-mcp-debug-info/k_get_svc_mcp_$(date +%Y.%m.%d_%H.%M.%S).yaml
    kubectl -n apigee get hpa 2>&1 | grep apigee-mcp-server | tee /tmp/apigee-mcp-debug-info/k_get_hpa_mcp_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    ###--- MCP data plane container logs (apigee-mcp-server) ---###
    ###--- MCP sidecar container logs (apigee-mcp-server-config) ---###
    
    for p in $(kubectl -n apigee get pods -l app=apigee-mcp-server --no-headers -o custom-columns=":metadata.name"); do
      kubectl -n apigee logs $p -c apigee-mcp-server --tail=2000 2>&1 | tee /tmp/apigee-mcp-debug-info/k_logs_${p}_apigee-mcp-server_$(date +%Y.%m.%d_%H.%M.%S).log
      kubectl -n apigee logs $p -c apigee-mcp-server-config --tail=2000 2>&1 | tee /tmp/apigee-mcp-debug-info/k_logs_${p}_apigee-mcp-server-config_$(date +%Y.%m.%d_%H.%M.%S).log
    done
    
    ###--- Ingress routing state (ApigeeRoute + ApigeeRouteConfig for the MCP-serving envgroup) ---###
    
    kubectl -n apigee get apigeeroute -o yaml 2>&1 | tee /tmp/apigee-mcp-debug-info/k_get_apigeeroute_$(date +%Y.%m.%d_%H.%M.%S).yaml
    kubectl -n apigee get apigeerouteconfig -o yaml 2>&1 | tee /tmp/apigee-mcp-debug-info/k_get_apigeerouteconfig_$(date +%Y.%m.%d_%H.%M.%S).yaml
    
    ###--- Message Processor hostAliases (verifies MCP injection into MP pods) ---###
    ###--- Every MP pod must show one entry with two hostnames: mcp.apigee.internal and .mcp.apigee.internal ---###
    
    for p in $(kubectl -n apigee get pods -l app=apigee-runtime --no-headers -o custom-columns=":metadata.name"); do
      kubectl -n apigee get pod $p -o jsonpath='{.spec.hostAliases}{"\n"}' 2>&1 | tee /tmp/apigee-mcp-debug-info/k_mp_hostaliases_${p}_$(date +%Y.%m.%d_%H.%M.%S).txt
    done
    
    ###--- Recent events in the apigee namespace filtered for MCP resources ---###
    ###--- (matches on the resource-name prefix, not the substring "mcp", to  ---###
    ###--- avoid false positives when your organization name contains "mcp".) ---###
    
    kubectl -n apigee get events --sort-by='.lastTimestamp' 2>&1 | grep -iE 'apigee-mcp-server' | tee /tmp/apigee-mcp-debug-info/k_events_mcp_$(date +%Y.%m.%d_%H.%M.%S).txt
    
    # compress all collected data
    tar -czvf apigee-mcp-debug-info-$(date +%Y.%m.%d_%H.%M.%S).tar.gz -C /tmp apigee-mcp-debug-info

If the tar file is larger than 25 MiB, split it into 25 MiB chunks for upload to the Support portal using the same procedure documented in the Apigee hybrid must-gather section above.

## Case templates and sample cases

This section provides case templates and sample cases for different products based on the best practices described in this document:

### Apigee Cloud

#### Template

This section provides a sample template for **Apigee on Google Cloud**.

**Problem:**

<Provide detailed description of the problem or the behaviour being observed at your end. Include the product name and version where applicable.>

**Error message:**

<Include the complete error message observed (if any)>

**Problem start time**(ISO 8601 format):

**Problem end time**(ISO 8601 format):

**Apigee setup details:**   
Org names:   
Env names:   
API proxy names:   
Revision numbers:

**Steps to reproduce:**

<Provide steps to reproduce the issue where possible>

**Diagnostic information:**

<List of files attached>

#### Sample case

This section provides a sample case for **Apigee on Google Cloud**.

**Problem:**

We are seeing a high number of 503 Service Unavailable errors in our **Public Cloud** org. Can you please look into the issue and resolve it or advise us how to resolve it?

**Error message:**

`{"fault":{"faultstring":"The Service is temporarily available", "detail":{"errorcode":"messaging.adaptors.http.flow.ServiceUnavailable"}}}`

**Problem start time**(ISO 8601 format): 2020-10-04 06:30 IST

**Problem end time**(ISO 8601 format): The issue is still happening.

**Apigee Cloud setup details:**   
Org names: `myorg`   
Env names: `dev`   
API proxy names: `myproxy`   
Revision numbers: `3`

**Steps to reproduce:**

Run the following `curl` command to reproduce the issue:
    
    
    curl -X GET 'https://myorg-dev.apigee.net/v1/myproxy'

**Diagnostic information:**

Debug tool output (`trace-503.xml`)

### Hybrid

#### Template

This section provides a sample template for Apigee hybrid.

**Problem:**

<Provide detailed description of the problem or the behaviour being observed at your end. Include the product name and version where applicable.>

**Error message:**

<Include the complete error message observed (if any)>

**Problem start time**(ISO 8601 format):

**Problem end time**(ISO 8601 format):

**Apigee hybrid setup details:**

  * **Apigee hybrid platform:**

<Provide the information about the Platform where you have installed hybrid and its version.>

  * **Google Cloud project, hybrid Organization and Environment:**   
Google Cloud project ID:   
<If you are using Google Kubernetes Engine (GKE), ensure you provide the project ID where the clusters are located. If you are using GKE on-prem, Azure Kubernetes Service or Amazon EKS, then provide the project ID where you are sending the logs.>   
Apigee hybrid org:   
Apigee hybrid env: 
  * **Apigee hybrid and other CLI versions:**   
Apigee hybrid CLI (`apigeectl`) version:   
Kubectl version:
  * **Kubernetes cluster name details:**   
k8sCluster:   
name:   
region:
  * **Network topology:**   
<Attach the network topology describing the setup of your Apigee hybrid including data centers, Kubernetes clusters, namespaces, and pods.>
  * **Overrides YAML File:**   
<Attach the Overrides YAML file.>



**Steps to reproduce**

<Provide steps to reproduce the issue where possible>

**Diagnostic information:**

<List of files attached>

#### Sample case

This section provides a sample case for Apigee hybrid.

**Problem:**

We are getting errors when executing management APIs on **Apigee hybrid version 1.3**.

**Error message:**
    
    
    [ERROR] 400 Bad Request
    {
    "error": {
    "code": 400,
    "message": "Error processing MART request: INTERNAL_ERROR",
    "errors": [
    {
    "message": "Error processing MART request: INTERNAL_ERROR",
    "domain": "global",
    "reason": "failedPrecondition"
    }
    ],
    "status": "FAILED_PRECONDITION"
    }
    }
    

**Problem start time**(ISO 8601 format): Since**** 2020-10-24 10:30 PDT

**Problem end time**(ISO 8601 format): Continuing to observe the issue.

**Apigee hybrid setup details:**

  * **Apigee hybrid platform**   
GKE version 1.15.1
  * **Google Cloud project, hybrid Organization and Environment**   
Google Cloud project ID: `apigee-hybrid-123456`   
**Note:** This is the project ID where the clusters are located.   
Apigee hybrid org: `apigee-hybrid-123456`   
Apigee hybrid env: `dev`
  * **Apigee hybrid and other CLI versions:**   
Apigee hybrid CLI (`apigeectl`) version:   
Version: `1.2.0`   
Commit: `ac09109`   
Build ID: `214`   
Build Time: `2020-03-30T20:23:36Z`   
Go Version: `go1.12`   
  
Kubectl version:   
Client Version: 
        
        version.Info{Major:"1", Minor:"15", GitVersion:"v1.15.0", GitCommit:"e8462b5b5dc2584fdcd18e6bcfe9f1e4d970a529", GitTreeState:"clean", BuildDate:"2019-06-19T16:40:16Z", GoVersion:"go1.12.5", Compiler:"gc", Platform:"darwin/amd64"}

  
Server Version: 
        
        version.Info{Major:"1", Minor:"14+", GitVersion:"v1.14.10-gke.36", GitCommit:"34a615f32e9a0c9e97cdb9f749adb392758349a6", GitTreeState:"clean",

  * **Kubernetes cluster name details:**   
k8sCluster:   
name: `user-cluster-1`   
region: `us-east1`
  * **Network topology**   
Attached the file `network-topology.png`
  * **Overrides YAML File**   
Attached the file `overrides.yaml` file



**Steps to reproduce:**

Run the following management API to observe the error:
    
    
    curl -X GET --header "Authorization: Bearer <TOKEN>" "https://apigee.googleapis.com/v1/organizations/apigee-hybrid-123456/environments/dev/keyvaluemaps"

**Diagnostic Information:**

Attached the following files:

  * `network-topology.png`
  * `overrides.yaml file`
  * MART logs
  * Synchronizer logs



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
