---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension/
title: Create an APIMExtensionPolicy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:21.001074+00:00
---

# Create an APIMExtensionPolicy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create an APIMExtensionPolicy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to apply Apigee policies to traffic passing through a Kubernetes Gateway by creating an `APIMExtensionPolicy` custom resource. The Apigee Operator for Kubernetes watches for `APIMExtensionPolicy` resources and configures the gateway accordingly.

### Apigee

Follow these steps if you are using Apigee.

## Before you begin

Before you begin this task, complete the following steps:

  * Confirm that your GKE cluster has Workload Identity configured. See [Configure Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for the required steps.
  * Confirm that your cluster has a GKE Gateway configured and working. See [Deploying gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) for more details.
  * Install the Apigee Operator for Kubernetes. See [Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install) for installation instructions.



## Create the `APIMExtensionPolicy`

In this step, create the `APIMExtensionPolicy` and apply it to the GKE Gateway running in your cluster. This policy governs all traffic going through the Gateway and its associated `HTTPRoutes`, operating similarly to a flowhook at the environment level in Apigee today.

**Note:** When the `APIMExtensionPolicy` is applied to a gateway, the Apigee Operator for Kubernetes creates the required traffic extension. This traffic extension is not compatible with any other traffic extensions that may be present on the gateway. If you have multiple traffic extensions, or prefer to manage the ordering of the traffic extensions yourself, use the `ApigeeBackendService` instead. Using the `ApigeeBackendService` allows you to integrate Apigee into a `GCPTrafficExtension` resource alongside other extensions. See [Create an `ApigeeBackendService`](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice) for more information.

To create the `APIMExtensionPolicy`:

  1. Create a file named `global-ext-lb1-apim-policy.yaml` with the following content: 
         
         # global-ext-lb1-apim-policy.yaml
         apiVersion: apim.googleapis.com/v1
         kind: APIMExtensionPolicy
         metadata:
           name: global-ext-lb1-apim-policy
           namespace: apim
         spec:
           apigeeenv: ENV_NAME # optional
           location: global
           failOpen: false
           timeout: 1000ms
           defaultSecurityEnabled: true
           targetRef: # identifies the Gateway where the extension should be applied
             name: global-ext-lb1
             kind: Gateway
             namespace: default
             

  2. Replace `ENV_NAME` with the name of the Apigee environment created in the installation step [Create an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#create-apigee-environment). 

**Note:** If you install the Apigee Operator for Kubernetes using the `generateEnv=TRUE` flag, the `apigeeenv` field is not required.

You can view all available environments in the [Environments page in the Google Cloud console](https://console.cloud.google.com/apigee/environments/overview).

  3. Apply the policy: 
         
         kubectl -n apim apply -f global-ext-lb1-apim-policy.yaml
             

Once the policy is applied, the Apigee Operator for Kubernetes creates networking resources in the background.

  4. Check the status of the `APIMExtensionPolicy` using the following command: 
         
         kubectl -n apim get APIMExtensionPolicy
             

The output should look similar to the following, with a `STATE` of `RUNNING`:
         
         NAME                         STATE      ERRORMESSAGE
         global-ext-lb1-apim-policy   RUNNING
             

**Note:** It may take up to five minutes for the policy to propagate to all load balancer instances.



## Test the policy

Use the following command to send a request to the Gateway:

  1. Get the Gateway IP address: 
         
         export GATEWAY_IP=$(kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -n default -o=jsonpath='{.status.addresses[0].value}')
               
         
         echo $GATEWAY_IP
               

Replace `GATEWAY_NAME` with the name of the Gateway, for example `global-ext-lb1`.

  2. Send a request to an endpoint configured in your `HTTPRoute`: 
         
         curl http://$GATEWAY_IP/get -H "Host: HOST_NAME"
               

Replace `HOST_NAME` with the hostname defined in the Gateway's `HTTPRoute`, for example `example.httpbin.com`.

  3. The request should fail because `defaultSecurityEnabled: true` was set in the `APIMExtensionPolicy` resource, which enables API key and access token verification. You should see a response similar to the following: 
         
         {"fault":{"faultstring":"Raising fault. Fault name : RF-insufficient-request-raise-fault","detail":{"errorcode":"steps.raisefault.RaiseFault"}}}
             

This indicates that the Apigee extension policy is active and that API key enforcement and access token verification is active.




## What's next

  * Learn how to [Add policies to the GKE Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies).
  * Learn how to [Uninstall the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-uninstall).



### Apigee hybrid

Follow these steps if you are using Apigee hybrid.

**Preview — Apigee Operator for Kubernetes for Apigee hybrid**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

This procedure assumes you have installed the Apigee Operator for Kubernetes by following the steps in [Install the Apigee Operator for Kubernetes for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install-hybrid).

## Create a TLS certificate secret

The `APIMExtensionPolicy` requires the base64-encoded public certificate associated with the environment group hostname. You created this certificate in [Install the Apigee Hybrid Environment using helm](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install-hybrid#install-the-apigee-hybrid-environment-using-helm). Provide this certificate to the operator by creating a Kubernetes secret in the `apim` namespace.

  1. Get the base64 encoded certificate string from the file you created during installation: 
         
         cat $APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs/keystore_ENV_GROUP.pem.base64
             

  2. Create a file named `secret-cert.yaml` with the following content: 
         
         # secret-cert.yaml
         apiVersion: v1
         kind: Secret
         metadata:
           name: apigee-conf
           namespace: apim
         data:
           ca.crt: BASE64_ENCODED_CERT_STRING
             

  3. Replace `BASE64_ENCODED_CERT_STRING` with the output from the `cat` command in step 1.
  4. Apply the secret to your cluster: 
         
         kubectl apply -f secret-cert.yaml
             




## Define and apply the `APIMExtensionPolicy`

Define an `APIMExtensionPolicy` resource and apply it to the Istio Gateway running in your cluster. This policy extension intercepts traffic managed by the Gateway and its associated `HTTPRoutes` and applies Apigee policies before forwarding requests to the backend target.

  1. Create a file named `istio-gateway-apim-policy.yaml` with the following content: 
         
         # istio-gateway-apim-policy.yaml
         apiVersion: apim.googleapis.com/v1
         kind: APIMExtensionPolicy
         metadata:
           name: istio-gateway-apim-policy
           namespace: apim
         spec:
           apigeeenv: ENV_NAME
           ingressCertSecret: apigee-conf
           apigeeAuthority: HOST_NAME
           apigeeIngressIP: INGRESS_IP_ADDRESS
           location: global
           failOpen: false
           timeout: 1000ms
           defaultSecurityEnabled: true
           targetRef: # identifies the Gateway where the extension should be applied
             group: gateway.networking.k8s.io
             kind: Gateway
             name: istio-gateway
             namespace: default
             

  2. Replace the following variables: 
     * `ENV_NAME`: The name of the Apigee hybrid environment you created with service extensions enabled, for example `my-hybrid-env`.
     * `HOST_NAME`: The domain name used for the Environment group, for example `my-proxies.example.com`.
     * `INGRESS_IP_ADDRESS`: The ingress IP address for Apigee Hybrid runtime ingress. See [Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-expose-apigee-ingress) for details on retrieving this IP.
  3. Apply the policy to your cluster: 
         
         kubectl -n apim apply -f istio-gateway-apim-policy.yaml
             

  4. Once the resource is applied, the Apigee Operator for Kubernetes begins configuring the gateway networking resources. Check the status of the `APIMExtensionPolicy`: 
         
         kubectl -n apim get APIMExtensionPolicy
             

  5. Wait until the `STATE` shows `RUNNING`. The output should look similar to the following: 
         
         NAME                         STATE      ERRORMESSAGE
         istio-gateway-apim-policy    RUNNING
             




## Test the policy

In the `APIMExtensionPolicy` created in the previous step, `defaultSecurityEnabled` was set to `true`. This automatically enables API Key and OAuth2 token verification policies for traffic matching this gateway. Test this by sending an unauthenticated request to the sample `httpbin` service you configured when verifying the Istio Gateway setup in [Verify the Istio Gateway setup](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install-hybrid#verify-the-istio-gateway-setup-optional).

  1. Get the Gateway IP address: 
         
         export GATEWAY_IP=$(kubectl get gateways.gateway.networking.k8s.io istio-gateway -n default -o=jsonpath='{.status.addresses[0].value}')
             
         
         echo $GATEWAY_IP
             

  2. Send a request to the `/get` endpoint configured in your HTTPRoute: 
         
         curl http://$GATEWAY_IP/get -H "Host: example.httpbin.com" -v
             

  3. Because `defaultSecurityEnabled: true` requires authentication (such as a valid API key), Apigee should reject the request with an authentication error. The response should be similar to the following: 
         
         {"fault":{"faultstring":"Raising fault. Fault name : RF-insufficient-request-raise-fault","detail":{"errorcode":"steps.raisefault.RaiseFault"}}}
             

This output confirms that the `APIMExtensionPolicy` is active and Apigee policies are being enforced by the Istio Gateway.




## What's next

Learn how to create API products, developers, and apps to obtain API keys for authenticated requests:

  * [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products)
  * [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products)
  * [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product)
  * [Managing access to your APIs using API keys](https://docs.cloud.google.com/apigee/docs/api-platform/publish/manage-api-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
