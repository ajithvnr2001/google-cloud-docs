---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-update/
title: Update API management policies with the Apigee Operator for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:13.317133+00:00
---

# Update API management policies with the Apigee Operator for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Update API management policies with the Apigee Operator for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

As your API management needs grow and change, you may need to add new services to your cluster or update existing routes and ingress options. This page describes how to update your cluster to complete the following tasks: 

  * Add a new Gateway and HTTPRoute.
  * Update an API product.
  * Create a new API product.
  * Create a new API operation set.
  * Test the new Gateway configuration.



## Before you begin

Before you begin this task, make sure to complete the steps described in [Create an APIMExtensionPolicy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension). This page assumes that you have set up a Google Kubernetes Engine (GKE) cluster, installed the Apigee Operator for Kubernetes, created a Google Kubernetes Engine (GKE) Gateway, and applied at least one API management policy to the Gateway.

## Required roles

If you assigned the required roles to your service account as described in [ Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#required-roles), no additional IAM roles or permissions are required to complete these tasks.

You can choose to authorize actions on resources in your Google Kubernetes Engine cluster using the built-in role-based access control (RBAC) mechanism in Kubernetes. For more information, see [ Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## Add a new Gateway and HTTPRoute

In this section, you will add a new Gateway and HTTPRoute to your cluster. In previous task guides, the example configurations used an _external_ GKE Gateway. If multiple Gateways are deployed in the _same region_ they must be of the same type (both external or both internal). For this reason, the example configuration in this guide will also use an _external_ Gateway.

The Apigee Operator for Kubernetes can be used with either internal or external GKE gateways, but you can't deploy both types of gateways in the same region.

To add a new Gateway and HTTPRoute to your cluster, complete the following steps:

  1. Set up a new external GKE Gateway. For more information and steps, see [Deploy an external Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#external-gateway). 
  2. Create a Google-managed global `SslCertificate` resource: 
         
         gcloud compute ssl-certificates create CERT_NAME \
           --domains=HOST_NAME \
           --global

Where: 

     * `CERT_NAME` is the name of the certificate you want to create.
     * `HOST_NAME_2` is the hostname for the new Gateway.
  3. Create a new file named `gateway2.yaml` in the `apim` namespace.
  4. Copy the following content into the new file: 
         
         # gateway2.yaml
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: Gateway
         metadata:
           name: global-ext-lb2
           spec:
           gatewayClassName: gke-l7-global-external-managed
           listeners:
           - name: https
             protocol: HTTPS
             allowedRoutes:
               kinds:
               - kind: HTTPRoute
               namespaces:
                 from: All
             port: 443
             tls:
               options:
                 networking.gke.io/pre-shared-certs: CERT_NAME

  5. Add a new HTTPRoute for `/post` to the same file, as highlighted below: 
         
         # http-route2.yaml
           apiVersion: gateway.networking.k8s.io/v1beta1
           kind: HTTPRoute
           metadata:
             name: http-bin-route-post
             namespace: http
           spec:
             parentRefs:
               - kind: Gateway
                 name: global-ext-lb2
                 namespace: default
             hostnames:
               - HOST_NAME_2
             **rules :
             - matches:
               - path:
                   type: PathPrefix
                   value: "/post"**
               backendRefs:
               - name: httpbin
                 kind: Service
                 port: 80
                 namespace: http

  6. Apply the new Gateway and HTTPRoute: 
         
         kubectl apply -f gateway2.yaml

  7. Check the HTTPRoute status using the following command:: 
         
         kubectl -n http get HttpRoute

The output should be similar to the following:
         
         NAME             HOSTNAMES                                                  AGE
         http-bin-route   ["my-hostname-2"]   12d
         

  8. Check the Gateway status using the following command: 
         
         kubectl get gateway global-ext-lb2

The output should be similar to the following: 
         
         NAME             CLASS                            ADDRESS        PROGRAMMED   AGE
         global-ext-lb2   gke-l7-global-external-managed   **34.54.193.92**   True         11d
         

Confirm that the `Address` column contains a valid IP address and the status of `Programmed` is `True`.

  9. Describe the Gateway to make sure the route is attached: 
         
         kubectl describe gateway global-ext-lb2

  10. The output should be similar to the following: 
         
         ...
         Listeners:
           **Attached Routes:  1**
           Conditions:
             Last Transition Time:  2024-10-03T03:10:17Z
         ...

Confirm that the `Attached Routes` value is `1`.

  11. Send a request to the Gateway to verify that the route is working: 
         
         curl -k -X POST https://GATEWAY_IP_ADDRESS/post -H "Host: HOST_NAME_2"

Where: 

     * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway, as shown in the `Address` column of the response returned in Step 7.
     * `HOST_NAME_2` is the hostname defined in the Gateway's `HTTPRoute`.
  12. The output should be similar to the following: 
         
         {
             "args": {},
             "headers": {
               "Accept": "*/*",
               "Host": "apigee-apim-operator-test.apigee.net",
               "User-Agent": "curl/8.7.1",
               "X-Cloud-Trace-Context": "2bb8a80e29e80662ff9cb89971c447d9/13083106619927322701"
             },
             "origin": "67.164.1.10,34.54.193.72",
             "url": "https://apigee-apim-operator-test.apigee.net/post"
           }
           

  13. Create a new APIM Extension Policy that references the HTTPRoute of the new Gateway created in an earlier step: 
     1. Create a new file named `apim-policy2.yaml` in the `apim` namespace.
     2. Copy the following content into the new file: 
            
            # apim-policy2.yaml
            apiVersion: apim.googleapis.com/v1
            kind: APIMExtensionPolicy
            metadata:
              name: global-ext-lb2-apim-policy-2
              namespace: apim
            spec:
              location: global
              failOpen: false
              timeout: 1000ms
              defaultSecurityEnabled: true
              targetRef: # identifies the Gateway where the extension should be installed
                name: global-ext-lb2
                kind: Gateway
                namespace: default

     3. Apply the new APIM Extension Policy: 
            
            kubectl apply -f apim-policy2.yaml

Once the file is applied, the Apigee Operator for Kubernetes creates networking resources in the background.

     4. Check the status of the APIM Extension Policy: 
            
            kubectl -n apim get APIMExtensionPolicy

The output should be similar to the following: 
            
            NAME                           STATE        ERRORMESSAGE
            global-ext-lb2-apim-policy-2   RUNNING
            

Confirm that the `STATE` value is `RUNNING`.

     5. Wait five minutes to ensure the changes propagate to all the load balancer instances, then use the following command to verify that a request to the new Gateway fails: 
            
            curl -k -X POST https://GATEWAY_IP_ADDRESS/post -H "Host: HOST_NAME_2"

Where: 

        * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway obtained in  an earlier step.
        * `HOST_NAME_2` is the hostname defined in the Gateway's `HTTPRoute`.

The request should fail with a response similar to the following: 
    
    {
      "fault": {
        "faultstring": "Raising fault. Fault name : RF-insufficient-request-raise-fault",
        "detail": {
          "errorcode": "steps.raisefault.RaiseFault"
        }
      }
    }

This means the service extension to Apigee is active and API key and access token verification is enforced. For the steps required to create a Developer App, obtain an API key, and test your new Gateway with the key, see [Test the Apigee service extension](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-create#test-apim-policy).




## Update an API product

Modify an existing API product to reference the new APIM Extension Policy: 

  1. Create a new file named `api-product-2.yaml` in the `apim` namespace.
  2. Copy the following content into the new file: 
         
         # api-product-2.yaml
         apiVersion: apim.googleapis.com/v1
         kind: APIProduct
         metadata:
           name: api-product-2
           namespace: apim
         spec:
           name: api-product-2
           approvalType: auto
           description: Http bin GET calls
           displayName: api-product-2
         **EnforcementRefs :
           - name: global-ext-lb1-apim-policy
             kind: APIMExtensionPolicy
             group: apim.googleapis.com
             namespace: apim
           - name: global-ext-lb2-apim-policy
             kind: APIMExtensionPolicy
             group: apim.googleapis.com
             namespace: apim**
           attributes:
           - name: access
             value: private

  3. Apply the new API product file: 
         
         kubectl apply -f api-product-2.yaml

It will take approximately three minutes for the changes to be applied throughout the cluster.




In this example, the `EnforcementRefs` section of the API product `api-product-2` is updated to reference both `global-ext-lb1-apim-policy` and `global-ext-lb2-apim-policy`, as shown in the highlighted portions of the `yaml`. 

## Create a new API product

Create a new API product: 

  1. Create a new file named `api-product-2.yaml` in the `apim` namespace.
  2. Copy the following content into the new file: 
         
         # api-product-2.yaml
         apiVersion: apim.googleapis.com/v1
         kind: APIProduct
         metadata:
           name: api-product-2
           namespace: apim
         spec:
           name: api-product-2
           approvalType: auto
           description: Http bin GET calls
           displayName: api-product-2
           **enforcementRefs :
           - name: global-ext-lb2-apim-policy
             kind: APIMExtensionPolicy
             group: apim.googleapis.com
             namespace: apim**
           attributes:
           - name: access
             value: private

  3. Apply the new API product file: 
         
         kubectl apply -f api-product-2.yaml

It will take approximately three minutes for the changes to be applied throughout the cluster.




In this example, the `EnforcementRefs` section of the new API product `api-product-2` is created to reference `global-ext-lb2-apim-policy`, as shown in the highlighted portions of the `yaml`.

## Create a new API operation set

Create a new API operation set: 

  1. Create a new file named `item-set-post.yaml` in the `apim` namespace.
  2. Copy the following content into the new file: 
         
         # item-set-post.yaml
         apiVersion: apim.googleapis.com/v1
         kind: APIOperationSet
         metadata:
           name: item-set-post
           namespace: apim
         spec:
           apiProductRefs:
             - name: api-product-2
               kind: APIProduct
               group: apim.googleapis.com
               namespace: apim
           quota:
             limit: 1
             interval: 1
             timeUnit: minute
           **restOperations :
             - name: PostItems
               path: "/post"
               methods:
               - POST**

  3. Apply the new API operation set file: 
         
         kubectl apply -f item-set-post.yaml

It will take approximately three minutes for the changes to be applied throughout the cluster.




In this example, the `restOperations` value of the new API operation set `item-set-post` is created to reference the `/post` path, as shown in the highlighted portions of the file.

## Test the new Gateway configuration

To test the new Gateway configuration, send the following request to the new `/post` path: 
    
    
    curl -k -X POST https://GATEWAY_IP_ADDRESS/post -H "Host: HOST_NAME_2"

Where: 

  * GATEWAY_IP_ADDRESS is the IP address of the Gateway obtained in  an earlier step.
  * HOST_NAME is the hostname defined in the Gateway's `HTTPRoute`.



The request should succeed and return a response similar to the following: 
    
    
    {
      "args": {},
      "headers": {
        "Accept": "*/*",
        "Host": "apigee-apim-operator-test.apigee.net",
        "User-Agent": "curl/8.7.1",
        "X-Api-Key": "f0N6sXXXclGXXXe0oP5XXXdA20PjgrP2x8xXXh7z4XXXKiYt",
        "X-Cloud-Trace-Context": "bb3a768787099bda628781188bfb318b/15554891713516675739"
      },
      "origin": "34.54.193.72",
      "url": "https://34.54.193.72/post"
    }

## Troubleshoot

If you encounter issues when updating and extending the API management policies used with Apigee Operator for Kubernetes, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) for solutions to common errors.

## What's next

  * Learn how to [Uninstall the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-uninstall).
  * Learn more about options for [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
