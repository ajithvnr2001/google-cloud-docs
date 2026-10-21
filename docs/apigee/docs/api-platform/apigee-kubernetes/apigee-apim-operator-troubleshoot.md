---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot/
title: Troubleshoot the Apigee Operator for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:13.728176+00:00
---

# Troubleshoot the Apigee Operator for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Troubleshoot the Apigee Operator for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to troubleshoot the Apigee Operator for Kubernetes. There are a number of tools available to resolve any issues you may encounter. This page describes how to check the status of the custom resources, use Logs Explorer, and troubleshoot issues with Apigee runtime traffic. 

## Check custom resource status

Every [custom resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-reference) used in the Apigee Operator for Kubernetes contains a status object with two fields: 

  * **STATE** : Describes the state of the resource. Values include `running` and `created`.
  * **ERRORMESSAGE** : If the resource operation fails, then the error message field is populated with an explanatory message.



When a custom resource `yaml` file is applied to the cluster, Kubernetes makes the corresponding changes to the underlying infrastructure. Checking the custom resource's status object can provide information on the state of the resource and surface any resulting errors if the underlying infrastructure operations fail.

You can check the custom resource status with the following command: 
    
    
    kubectl -n NAMESPACE get CUSTOM_RESOURCE_KIND CUSTOM_RESOURCE_NAME

Where: 

  * `NAMESPACE`: The namespace where the custom resource is deployed.
  * `CUSTOM_RESOURCE_KIND`: The [kind](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-reference) of the custom resource.
  * `CUSTOM_RESOURCE_NAME`: The name of the custom resource.



For example, the following command checks the status of the `APIMExtensionPolicy` custom resource named `apim-extension-policy` in the `apim` namespace: 
    
    
    kubectl -n **apim** get **APIMExtensionPolicy** **apim-extension-policy-1**

The output is similar to the following:
    
    
    NAME                      STATE                  ERRORMESSAGE
    apim-extension-policy     Create_Update_Failed   Permission denied

## View logs

This section describes how to use logs to troubleshoot the Google Kubernetes Engine (GKE) Gateway resource and the Apigee Operator for Kubernetes resource.

### GKE Gateway logs

When you [apply the APIMExtensionPolicy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension#create-apim-policy), or the [ApigeeBackendService](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice#create-apigeebackendservice) and `GCPTrafficExtension`, the GKE Gateway you created in your cluster is configured with a [traffic extension](https://cloud.google.com/service-extensions/docs/configure-traffic-extensions). The extension uses Kubernetes external processing ([`ext-proc`](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ext_proc/v3/external_processor.proto)) to call the Apigee runtime and process policies. The logs related to the `ext-proc` traffic can be useful when troubleshooting issues. 

#### View logs for `ext-proc` callouts

To view logs for the `ext-proc` callout traffic: 

  1. Get the ID of the backend service created for the Apigee runtime: 
         
         kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME
           -o=jsonpath="{.metadata.annotations.networking\.gke\.io/backend-services}"

Where `GATEWAY_NAME` is the name of the GKE Gateway.

The backend service will contain `apigee-service-extension-backend-service`in the ID.

  2. Follow the steps in [ Enable logging on a backend service](https://docs.cloud.google.com/service-extensions/docs/view-callout-log-messages#enable-extension-logs) to enable logging.
  3. To view logs in the Google Cloud console, go to the **Logs Explorer** page: 

[Logs Explorer](https://console.cloud.google.com/logs)

  4. Review [ Log messages for a backend service](https://docs.cloud.google.com/service-extensions/docs/view-callout-log-messages#what_is_logged_for_callout_extensions) to see available callout log entry information, including the JSON payload structure for the `service_extension_info` load balancer log entry. You can use the **Search** field in Logs Explorer to filter for the relevant information. 

The following example is a log entry you might see for a failed `ext-proc` callout: 
         
         {
           "insertId": "s14dmrf10g6hi",
           "jsonPayload": {
             "serviceExtensionInfo": [
               {
                 "extension": "ext11",
                 "perProcessingRequestInfo": [
                   {
                     "eventType": "REQUEST_HEADERS",
                     "latency": "0.001130s"
                   }
                 ],
                 "backendTargetType": "BACKEND_SERVICE",
                 "grpcStatus": "ABORTED",
                 "backendTargetName": "gkegw1-2y13-apigee-service-extension-backend-service-443-yhsnrauznpwh",
                 "chain": "chain1",
                 "resource": "projects/$PROJECT_ID/locations/us-west1/lbTrafficExtensions/apim-extension"
               }
             ],
             "backendTargetProjectNumber": "projects/763484362408",
             "@type": "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
           },
           "httpRequest": {
             ...
           },
           "resource": {
             "type": "internal_http_lb_rule",
             "labels": {
               ...
             }
           },
           "timestamp": "2024-04-01T20:15:15.182137Z",
           "severity": "INFO",
           "logName": "projects/$PROJECT_ID/logs/loadbalancing.googleapis.com%2Frequests",
           "receiveTimestamp": "2024-04-01T20:15:18.209706689Z"
         }

Note that the `grpcStatus` field shows `ABORTED`. 




### APIM Operator logs

The APIM Operator is a Kubernetes operator that processes APIM custom resource events (such as create, read, update, and delete), and translates those events in the appropriate Apigee configuration.

To view logs for the APIM Operator: 

  1. To view logs in the Google Cloud console, go to the **Logs Explorer** page: 

[Logs Explorer](https://console.cloud.google.com/logs)

  2. In the **Query pane** , enter a query similar to the following: 
         
         resource.type="k8s_container"
         resource.labels.namespace_name="apim"
         labels.k8s-pod/app="apigee-apim-operator" severity>=DEFAULT
         

  3. Click **Run query**.
  4. The filtered log entries are displayed in the **Query results** pane.
  5. Make a note of any issues with creating, updating, or deleting the `APIMExtensionPolicy` in Google Cloud networks services or issues with API Products in Apigee management planes. 

An example error would look similar to the following: 
         
         ApimExtensionPolicy creation status400
         response body:{
           "error": {
             "code": 400,
             "message": "The request was invalid: backend service https://www.googleapis.com/compute/v1/projects/... must use HTTP/2 as the protocol",
             "status": "INVALID_ARGUMENT",
             "details": [
               {
                 "@type": "type.googleapis.com/google.rpc.BadRequest",
                 "fieldViolations": [
                   {
                     "field": "lb_traffic_extension.extension_chains[0].extensions[0].service"
                   }
                 ]
               },
               {
                 "@type": "type.googleapis.com/google.rpc.RequestInfo",
                 "requestId": "d4e6f00ab5d367ec"
               }
             ]
           }
         }




## Troubleshoot 403 access errors in the APIM Operator

If you discover status code `403` errors indicating access issues, confirm the following: 

  * Your GKE cluster has workload identity federation enabled. Workload identity federation is enabled by default for created with autopilot mode. If you created a cluster using standard mode, In case you are using a standard cluster, enable workload identity federation as described in [ Enable Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools").
  * The Kubernetes service account (`apim-ksa`) is correctly annotated by the Helm install. You can confirm this with the following command: 
        
        kubectl describe serviceaccount apim-ksa -n NAMESPACE

Where NAMESPACE is the namespace where the APIM Operator is deployed.

Confirm that `apigee-apim-gsa@$PROJECT.iam.gserviceaccount.com` appears in the **Annotations** field of the output. 

For example: 
        
        kubectl describe serviceaccount apim-ksa -n **apim**

The output is similar to the following: Name: apim-ksa Namespace: apim Labels: ... Annotations: iam.gke.io/gcp-service-account: apigee-apim-gsa@apigee-product-demo.iam.gserviceaccount.com ... Image pull secrets:  Mountable secrets:  Tokens:  Events: 

  * The `apigee-apim-gsa` service account has the correct IAM roles and permissions. You can confirm this with the following command: 
        
        gcloud iam service-accounts get-iam-policy \
        apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com

The service account must have the `roles/iam.workloadIdentityUser` role.

For example, the following output shows the `roles/iam.workloadIdentityUser` role: 
        
        bindings:
        - members:
          - serviceAccount:$PROJECT_ID.svc.id.goog[/apim-ksa]
          role: roles/iam.workloadIdentityUser
        etag: BwYUpeaM7XQ=
        version: 1
        

  * No special [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) are present on the required roles, which would prevent access for the operator.



## Troubleshoot issues with Apigee runtime traffic

This section describes how to troubleshoot issues with Apigee runtime traffic. The following sections describe how to troubleshoot issues with valid and invalid requests.

### Valid requests fail

If you are unable to send valid requests to your Apigee runtime, then the following issues may be present: 

  * The GKE Gateway cannot reach the Apigee runtime. 
  * Your API Key or JWT credentials are invalid. 
  * The Apigee API Product is not configured for the correct target and environment. 
  * The Apigee runtime is not aware of Apigee API Product.



#### Troubleshooting steps

To troubleshoot issues with valid requests: 

  * Enable load balancer logs for the GKE Gateway and review the logs to determine the cause of failures from the extension callout. See the GKE Gateway logs for more detail.
  * Confirm that the backend service referenced from the ext-proc service is healthy.
  * Review the API Product configuration on Apigee: 
    * Confirm that the API product is enabled for the correct environment (for example, `test` or `prod`).
    * Confirm that the resource path matches your request. A path like `/` or `/**` will match any path. You can also use `*` or `**` wildcards for matching.
    * Confirm that you have a Developer App configured for the API Product. The API Product must be bound to a Developer App to validate its API keys.
  * Review your request to the Gateway: 
    * Confirm that the Consumer Key is passed in the `x-api-key` header.
    * Make sure that the Consumer Key is valid. The credentials from the Developer App must be approved for your API Product.



### Invalid requests succeed

If invalid requests to your Apigee runtime are successful, then the following issues may be present: 

  * `FailOpen` is set to `true` in your APIMExtensionPolicy.
  * There is no [traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) set for your GKE Gateway's load balancer.



#### Troubleshooting steps

To troubleshoot issues with invalid requests: 

  * Confirm that a service extension exists and references the correct backend services and forwarding rule for your GKE Gateway. 

Use the following command to view the service extension: 
        
        gcloud beta service-extensions lb-traffic-extensions describe NAME_OF_APIM_EXTENSION_POLICY --location=LOCATION  --project=PROJECT

Where: 

    * `NAME_OF_APIM_EXTENSION_POLICY`: The `APIMExtensionPolicy` custom resource name.
    * `PROJECT`: The project ID.
    * `LOCATION`: The location of the GKE cluster where your Gateway is deployed.

The output will be similar to the following: 
    
    ...
    extensionChains:
    - extensions:
      - authority: ext11.com
        failOpen: false  # make sure this is false
        name: ext11
        service: https://www.googleapis.com/compute/v1/projects/**my-project** /regions/**us-west1** /backendServices/gkegw1-2y13-apigee-service-extension-backend-service-443-yhsnrauznpwh # Confirm this is correct
        supportedEvents:
        - REQUEST_HEADERS
        - RESPONSE_HEADERS
        - REQUEST_BODY
        - RESPONSE_BODY
        - REQUEST_TRAILERS
        - RESPONSE_TRAILERS
        timeout: 0.100s
      matchCondition:
        celExpression: 'true' # Confirm this is set
      name: chain1
    forwardingRules:
    - https://www.googleapis.com/compute/v1/projects/**my-project** /regions/us-west1/forwardingRules/gkegw1-2y13-default-internal-http-h6c1hhp1ce6q # Confirm this is the correct forwarding rule for your application load balancer
    loadBalancingScheme: INTERNAL_MANAGED
    name: projects/**my-project** /locations/**us-west1** /lbTrafficExtensions/**apim-extension-policy-1**
    

### Missing analytics

If you are unable to view Apigee API Analytics for the Apigee Operator for Kubernetes in the Google Cloud console, note that Apigee intake can be delayed by a few minutes.

## Additional resources

The following resources can also be used to troubleshoot issues with Apigee Operator for Kubernetes and Apigee runtime traffic: 

    * [Apigee API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring)
    * [Apigee API Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview)
    * [Distributed tracing](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace)
    * [Apigee debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
