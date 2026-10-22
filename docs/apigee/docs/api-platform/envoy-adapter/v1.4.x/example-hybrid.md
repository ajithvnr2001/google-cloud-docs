---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/example-hybrid/
title: Using Apigee Adapter for Envoy with Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:37.326422+00:00
---

# Using Apigee Adapter for Envoy with Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/example-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using Apigee Adapter for Envoy with Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This example demonstrates how to use Apigee Adapter for Envoy with an Apigee hybrid deployment. 

## Prerequisites

Before you begin:  
---  
Download and install the Apigee Adapter for Envoy Remote Service and CLI as explained in [Getting started](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/getting-started).  
Be sure you have the [Google Cloud SDK](https://cloud.google.com/sdk/install) installed. The SDK includes the `gcloud` command-line tool.  
Be sure you have [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed.  
  
##  Overview 

This example explains how to use Apigee Adapter for Envoy with [ Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid). In this example, you will deploy a simple HTTP service in the same Kubernetes cluster where Apigee hybrid is deployed. Then, you will configure the Apigee Adapter for Envoy to manage API calls to this service with Apigee. 

The following figure shows the basic architecture for the Apigee hybrid integration: 

![A high-level
    view of the Envoy Adapter integrated into an Apigee hybrid environment, including the
    management plane, runtime plane, and GCP services](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/envoy-adapter-istio.png)

An Envoy proxy is deployed with the target HTTP service as an Istio sidecar in the Istio service mesh. The sidecar handles API traffic to and from the target service, and communicates with the Remote Service. The Remote Service also communicates with the hybrid management plane to retrieve API product and proxy information. 

##  Check your gcloud configuration 

  1. Check that your `gcloud` configuration is set to the GCP project associated with your hybrid organization. 

To list the current settings: 
         
         gcloud config list

If necessary, set the correct GCP project ID with this command: 
         
         gcloud config set project project-id

  2. You must be authenticated with Google Cloud SDK (gcloud) for your GCP project: 
         
         gcloud auth login




##  Provision Apigee hybrid 

In this step, you will use the Remote Service CLI to provision hybrid with the `remote-service` API proxy. The provisioning command also sets up a certificate on Apigee, and generates credentials the remote service will use to securely connect back to Apigee. 

  1. Go to the `$CLI_HOME` directory: 
         
         cd $CLI_HOME

  2. If you are not an owner of the GCP project associated with the Apigee hybrid organization, be sure that your GCP user account includes either the **Apigee Organization Admin** role, or both the **API Creator** and the **Deployer** roles. 

See [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

  3. Execute this command to get an access token: 
         
         TOKEN=$(gcloud auth print-access-token);echo $TOKEN

  4. Create the following environment variables. These variables will be used as parameters to the provisioning script: 
         
         export ORG=organization_name
         export ENV=environment_name
         export RUNTIME=host_alias_url
         export NAMESPACE=hybrid_runtime_namespace
         export AX_SERVICE_ACCOUNT=analytics_service_account

Where: 

Variable | Description  
---|---  
organization_name | The name of the Apigee organization for you Apigee hybrid installation.  
environment_name | The name of an environment in your Apigee hybrid organization.  
host_alias_url | A URL that includes the `hostAlias` for a virtual host defined in your hybrid configuration. The URL must start with `https://`. For example: `https://apitest.apigee-hybrid-docs.net`  
hybrid_runtime_namepace | The namespace in which the Hybrid runtime components are deployed. Note: The default namespace for a hybrid deployment is `apigee`.  
analytics_service_account | The path to a Google Cloud service account key JSON file that has the `Apigee Analytics Agent` role. For a detailed description of this parameter, see [Provision command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/reference#provision-command).  
  5. Execute the following command to provision the remote service proxy to Apigee hybrid: **NOTE:** If your hybrid runtime installation is configured using self-signed TLS certificates for the virtualhost, you must use the `--insecure` flag with the `provision` command shown below.**NOTE:** The command output is redirected to a config file that you will use in a later step.**IF YOU ARE UPGRADING:** If you are upgrading an existing Apigee Adapter for Envoy, you must add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy.

If you are not upgrading, use this command to provision Apigee: 
         
         ./apigee-remote-service-cli provision --organization $ORG --environment $ENV \
              --runtime $RUNTIME --namespace $NAMESPACE --analytics-sa $AX_SERVICE_ACCOUNT --token $TOKEN > config.yaml

If you are upgrading, use this command with the `--force-proxy-install` flag to provision Apigee: 
         
         ./apigee-remote-service-cli provision --force-proxy-install --organization $ORG --environment $ENV \
              --runtime $RUNTIME --namespace $NAMESPACE --analytics-sa $AX_SERVICE_ACCOUNT --token $TOKEN > config.yaml

  6. Check the contents of the `config.yaml` file. It should look something like this: 
         
         # Configuration for apigee-remote-service-envoy (platform: GCP)
         # generated by apigee-remote-service-cli provision on 2020-11-20 02:49:28
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: apigee-remote-service-envoy
           namespace: apigee
         data:
           config.yaml: |
             tenant:
               remote_service_api: https://apitest.example.com/remote-service
               org_name: hybrid-gke
               env_name: test
             analytics:
               collection_interval: 10s
             auth:
               jwt_provider_key: https://apitest.example.com/remote-service/token
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: hybrid-gke-new-test-policy-secret
           namespace: apigee
         type: Opaque
         data:
           remote-service.crt: eyJrZXlzIjpbeyJrdHkiOiJSU0EiLCJhbGci...
           remote-service.key: LS0tLS1CRUdJTiBSU0EgUFJJVkFURS...
           remote-service.properties: a2lkPTIwMjAtMDctMDZ...
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: hybrid-gke-new-test-analytics-secret
           namespace: apigee
         type: Opaque
         data:
           client_secret.json: ewogICJ0eXBlIjogInNlcnZ...
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: apigee-remote-service-envoy
           namespace: apigee

  7. Apply the service configuration (the file output by the provisioning command) to the cluster: 
         
         kubectl apply -f $CLI_HOME/config.yaml

  8. Verify your proxy and certificate. The following should return valid JSON: 
         
         curl -i $RUNTIME/remote-service/certs

**Note:** It can take some time for the provisioning to complete. If this command fails, wait for a minute and try again. 

The output looks something like this: 
         
         {
             "keys": [
                 {
                     "alg": "RS256",
                     "e": "AQAB",
                     "kid": "2020-05-11T11:32:26-06:00",
                     "kty": "RSA",
                     "n": "0v-nbTQyAmtVZ-wZRP0ZPIbrVaX91YO9JZ9xCQPb4mOdOSS7yKfTDJGg0KM130sGVYBvR76alN8
                     fhrrSDEG5VXG8YYMqPXarwRC7MRJWocCQ_ECYrjDD0_Q018M2HyXZYSd8fhAogi9mVUYsEmCKqJH53Dh1
                     jqsHOQzBLKsX0iDO9hEZNFtjbX0UCbSxsUlmBCub7Uj2S-PahA6DEQOMhQjZM7bBMtkTMpFmaJ_RZTmow
                     BHP57qMna17R8wHD4kUsO2u_-3HHs5PSj1NrEYoVU2dwLQw0GlkB__ZWeFgXTqot81vb-PmoM9YxwoZrm
                     TcHdljugWy_s7xROPzTod0uw"
                 }
             ]
         }




##  Create sample configuration files 

Use the `apigee-remote-service-cli samples create` command to generate sample configuration files. 

For this example, you need these generated files: 

  * `httpbin.yaml` \- A deployment configuration for an HTTP service.
  * `apigee-envoy-adapter.yaml` \- A deployment configuration for the Remote Service for Envoy.
  * `envoyfilter-sidecar.yaml` \- A configuration that installs an EnvoyFilter. to the default namespace.



To generate the samples: 

  1. Go to the `$CLI_HOME` directory.
  2. Execute this command to generate the files: 
         
         ./apigee-remote-service-cli samples create -c ./config.yaml

**Note:** By default, the command generates files using the Istio 1.6 template. For Istio 1.7, specify the flag `--template istio-1.7`

The following files are output the `./samples` directory: 
         
         ls samples
         apigee-envoy-adapter.yaml envoyfilter-sidecar.yaml httpbin.yaml request-authentication.yaml
         




For more information, see [Samples command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/reference#samples-command). 

##  Deploy a test service to the cluster 

In this step, you will deploy a simple HTTP request/response test service to the same cluster where Apigee hybrid is deployed. 

  1. Enable Istio injection in the `default` namespace of the cluster. In a later step, you will deploy an Envoy sidecar to this same cluster. Enabling Istio injection makes the sidecar deployment possible. This example uses the `default` namespace, and all subsequent instructions assume this is the case. 

If you are using open source Istio: 
         
         kubectl label namespace default istio-injection=enabled --overwrite

If you are using ASM: 
         
         kubectl label namespace default istio-injection- istio.io/rev=REVISION --overwrite

  2. Apply the simple [`httpbin`](https://httpbin.org/) service to the cluster in the default namespace: 
         
         kubectl apply -f $CLI_HOME/samples/httpbin.yaml

  3. Now, test the service. Start a `curl` service running in the cluster and open a terminal: 
         
         kubectl run -it curl --image=curlimages/curl --restart=Never -- sh

  4. Test the service by calling it from inside the cluster: 
         
         curl -i httpbin.default.svc.cluster.local/headers

On success, you will see a 200 status, and the service returns a list of headers. For example: 
         
         HTTP/1.1 200 OK
         server: envoy
         date: Tue, 12 May 2020 17:09:01 GMT
         content-type: application/json
         content-length: 328
         access-control-allow-origin: *
         access-control-allow-credentials: true
         x-envoy-upstream-service-time: 7
         
         {
           "headers": {
             "Accept": "*/*",
             "Content-Length": "0",
             "Host": "httpbin.default.svc.cluster.local",
             "User-Agent": "curl/7.70.0-DEV",
             "X-B3-Parentspanid": "69f88bc3e322e157",
             "X-B3-Sampled": "0",
             "X-B3-Spanid": "8dd725f30e393d8b",
             "X-B3-Traceid": "38093cd817ad30a569f88bc3e322e157"
           }
         }

**TIP:** Leave the `curl` client running and the shell open. You will use it in a later step.



##  Run the Remote Service for Envoy 

In this step, you start the Remote Service for Envoy client in the service mesh where Apigee hybrid is installed. This service provides the endpoints to the Istio sidecars that are installed on target services. You will also install a sidecar with the `httpbin` service. 

  1. Apply the Apigee Remote Service to the service mesh: 
         
         kubectl apply -f $CLI_HOME/samples/apigee-envoy-adapter.yaml

  2. Apply the `EnvoyFilter` to the Istio sidecars in the default namespace. The `EnvoyFilter` enables the `httpbin` sidecar to communicate with the Apigee Remote Service. 
         
         kubectl apply -f $CLI_HOME/samples/envoyfilter-sidecar.yaml




##  Test the installation 

  1. Now, go back to the curl shell you opened in the step  Deploy a test service to the cluster and call the `httpbin` service: 
         
         curl -i httpbin.default.svc.cluster.local/headers
         

The service is now being managed by Apigee, and because you did not supply an API key, returns the following error.
         
         curl -i httpbin.default.svc.cluster.local/headers
         HTTP/1.1 403 Forbidden
         date: Tue, 12 May 2020 17:51:36 GMT
         server: envoy
         content-length: 0
         x-envoy-upstream-service-time: 11

  2. Configure an API product and get an API key as explained in [How to obtain an API key](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/operation#how-to-obtain-an-api-key).
  3. Make an API call using the key: 
         
         export APIKEY=YOUR_API_KEY
         curl -i httpbin.default.svc.cluster.local/headers -H "x-api-key: $APIKEY"

The call should succeed with a 200 status and returning a list of headers in the response. For example: 
         
         curl -i httpbin.default.svc.cluster.local/headers -H "x-api-key: kyOTalNNLMPfOSy6rnVeclmVSL6pA2zS"
         HTTP/1.1 200 OK
         server: envoy
         date: Tue, 12 May 2020 17:55:34 GMT
         content-type: application/json
         content-length: 828
         access-control-allow-origin: *
         access-control-allow-credentials: true
         x-envoy-upstream-service-time: 301
         
         {
           "headers": {
             "Accept": "*/*",
             "Content-Length": "0",
             "Host": "httpbin.default.svc.cluster.local",
             "User-Agent": "curl/7.70.0-DEV",
             "X-Api-Key": "kyOTalNNLMPfOSy6rnVeclmVSL6pA2zS",
             "X-Apigee-Accesstoken": "",
             "X-Apigee-Api": "httpbin.default.svc.cluster.local",
             "X-Apigee-Apiproducts": "httpbin",
             "X-Apigee-Application": "httpbin",
             "X-Apigee-Authorized": "true",
             "X-Apigee-Clientid": "kyOTalNNLMPfOSy6rnVeclmVSL6pA2zS",
             "X-Apigee-Developeremail": "jdoe@example.com",
             "X-Apigee-Environment": "envoy",
             "X-Apigee-Organization": "acme-org",
             "X-Apigee-Scope": "",
             "X-B3-Parentspanid": "1476f9a2329bbdfa",
             "X-B3-Sampled": "0",
             "X-B3-Spanid": "1ad5c19bfb4bc96f",
             "X-B3-Traceid": "6f329a34e8ca07811476f9a2329bbdfa"
           }
         }




##  Next steps 

API traffic to the `httpbin` service is now managed by Apigee. Here are some features you can explore and try: 

  * If you configured your API product as explained in [How to obtain an API key](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/operation#how-to-obtain-an-api-key), the quota limit was set to 5 requests per minute. Try calling the `httpbin` service a few more times to trigger the quota. When the quota is depleted, an HTTP status 403 error is returned. 
  * Access Apigee Analytics in the Edge UI. Go to **Analyze > API Metrics > API Proxy Performance**.
  * Generate and use [JWT tokens](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/operation#using-jwt-based-authentication) to authenticate API calls.
  * Use the CLI to manage, create tokens, and control bindings. For CLI details, see the [Reference](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.4.x/reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
