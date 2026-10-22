---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-security-quota/
title: Enable security and quota enforcement \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:53.973396+00:00
---

# Enable security and quota enforcement  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-security-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enable security and quota enforcement Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to enable the default security and quota enforcement options available with Apigee Operator for Kubernetes.

## Before you begin

Before you begin this task, make sure to complete the following steps: 

  * Install the Apigee Operator for Kubernetes. See [Install Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install) for installation instructions.
  * Create a traffic service extension. To complete this step you can use the `ApigeeBackendService` or the `APIMExtensionPolicy`. See [Create an APIMExtensionPolicy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension) for more information on creating a traffic extension using the `APIMExtensionPolicy`. See [Create an ApigeeBackendService](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice) for more information on creating a traffic extension using the `ApigeeBackendService`.



Whether you created a traffic service extension for your GKE Gateway using the `ApigeeBackendService` or the `APIMExtensionPolicy`, you must complete the steps in this walkthrough to enable the default API key and Quota policies added to the backing `APIMExtensionPolicy`.

## Required roles

If you assigned the required roles to your service account as described in [Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#required-roles), no additional IAM roles or permissions are required to complete these tasks.

You can choose to authorize actions on resources in your Google Kubernetes Engine cluster using the built-in role-based access control (RBAC) mechanism in Kubernetes. For more information, see [ Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## Overview

The following sections describe how to enable the default security and quota enforcement options available with Apigee Operator for Kubernetes. In this walkthrough, you will: 

  1. Define the API product.
  2. Define the API operation set.
  3. Test the Apigee service extension.
  4. View Apigee API Analytics in the Google Cloud console.



The steps required to define the API product and API operation set vary slightly depending on whether you created a traffic extension for your GKE Gateway using the `ApigeeBackendService` or the `APIMExtensionPolicy`.

## Define the API Product

In this step, you will define the API product that will be used to manage the API key enforcement and quota policies.

### Using the `APIMExtensionPolicy`

Define the API product: 

  1. Create a new file named `api-product.yaml` in the `apim` namespace.
  2. Copy the following content into the new file: 
         
         # api-product.yaml
           apiVersion: apim.googleapis.com/v1
           kind: APIProduct
           metadata:
             name: api-product
             namespace: apim
           spec:
             approvalType: auto
             description: Http bin GET calls
             displayName: api-product
             enforcementRefs:
               - name: global-ext-lb1-apim-policy
                 kind: APIMExtensionPolicy
                 group: apim.googleapis.com
                 namespace: apim
             attributes:
               - name: access
                 value: private

  3. Apply the file to the Gateway using the following command:: 
         
         kubectl -n apim apply -f api-product.yaml




### Using the `ApigeeBackendService`

Define the API product: 

  1. Create a new file named `api-product.yaml` in the `apim` namespace.
  2. Copy the following content into the new file: 
         
         # api-product.yaml
           apiVersion: apim.googleapis.com/v1
           kind: APIProduct
           metadata:
             name: api-product
             namespace: apim
           spec:
             approvalType: auto
             description: Http bin GET calls
             displayName: api-product
             enforcementRefs:
               - name: global-ext-lb1-apim-policy
                 kind: ApigeeBackendService
                 group: apim.googleapis.com
                 namespace: default
             attributes:
               - name: access
                 value: private

  3. Apply the file to the Gateway using the following command:: 
         
         kubectl -n default apply -f api-product.yaml




## Define the API operation set

In this step, you will define the API operation set that will be used to manage the rest operations enforcement.

### Using the `APIMExtensionPolicy`

Define the API operation set for the API product created in the previous step: 

  1. Create a new file named `apim-policies.yaml` in the `apim` namespace.
  2. Copy the following content into the new file. This file defines a quota policy and the available rest operations for the API product defined in the previous step: 
         
         # apim-policies.yaml
           apiVersion: apim.googleapis.com/v1
           kind: APIOperationSet
           metadata:
             name: item-set
             namespace: apim
           spec:
             apiProductRefs:
               - name: api-product
                 kind: APIProduct
                 group: apim.googleapis.com
                 namespace: apim
             quota:
               limit: 10
               interval: 1
               timeUnit: minute
             restOperations:
               - name: GetItems
                 path: /get
                 methods:
                   - GET

  3. Apply the file to the Gateway: 
         
         kubectl -n apim apply -f apim-policies.yaml




### Using the `ApigeeBackendService`

Define the API operation set for the API product created in the previous step: 

  1. Create a new file named `apim-policies.yaml` in the `default` namespace.
  2. Copy the following content into the new file. This file defines a quota policy and the available rest operations for the API product defined in the previous step: 
         
         # apim-policies.yaml
           apiVersion: apim.googleapis.com/v1
           kind: APIOperationSet
           metadata:
             name: item-set
             namespace: default
           spec:
             apiProductRefs:
               - name: api-product
                 kind: APIProduct
                 group: apim.googleapis.com
                 namespace: default
             quota:
               limit: 10
               interval: 1
               timeUnit: minute
             restOperations:
               - name: GetItems
                 path: /get
                 methods:
                   - GET

  3. Apply the file to the Gateway: 
         
         kubectl -n default apply -f apim-policies.yaml




## Test the Apigee service extension

In this step, you will use the Apigee UI in Google Cloud console to test the Apigee service extension and the Apigee extension policy applied to your Gateway.

### Testing set up

Set up the API resources you need for testing: 

  1. Go to to the **Apigee API management** page in the Google Cloud console: 

[Apigee API management](https://console.cloud.google.com/apigee)

  2. Select the Apigee organization where you installed the Apigee Operator for Kubernetes. 
  3. Create a developer: 
     1. Select **Distribution > Developers**.
     2. On the **Developers** page, click **\+ Create**.
     3. In the **Add developer** page, complete the required fields using any values you wish.
     4. Click **Add**.
  4. Create an App: 
     1. Select **Distribution > Apps**.
     2. On the **Apps** page, click **\+ Create**
     3. On the **Create App** page, complete the required fields in the **App Details** section using the following values: 
        * **App name** : demo-app
        * **Developer** : Select the developer you created in the previous step, or another developer from the list.
     4. In the **App Credentials** section, click **\+ Add Credential**.
     5. In the **Credential** section, complete the required fields in the **Credential Details** section with the following values: 
        * **Credential name** : demo-credential
        * **Credential type** : Select **API Key**.
     6. Click **Create**.
     7. In the **Products** section, click **\+ Add products**.
     8. Select the `api-product-1` created in the previous step.
     9. Click **Add**.
     10. Click **Create**.
  5. In the **App Details** page, in the **Credential** section, click _visibility_off_ to display the value of the **Key**. 

Copy the `Key` value. You will use this key to make API calls to your service in a later step.

  6. In the **App Details** page, in the **Credential** section, click _visibility_off_ to display the value of the **App Secret**. 

Copy the **App secret** value. You will use this value to generate an access token in a later step.




### Test API key enforcement

Use the following command to send a request to your Gateway using the API key obtained in an earlier step: 
    
    
    curl http://GATEWAY_IP_ADDRESS/get -H "Host: HOST_NAME" -H "x-api-key: API_KEY"

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



The request should succeed and return a response similar to the following: 
    
    
    {
      "args": {},
      "headers": {
        "Accept": "*/*",
        "Host": "apigee-apim-operator-test.apigee.net",
        "User-Agent": "curl/8.7.1",
        "X-Api-Key": "f0N6sYYYclGYYYe0oP5YYYdA20PjgrP2x8YYYh7z4YYYKiYt",
        "X-Cloud-Trace-Context": "bb3a768787099bda628781188bfb318b/15554891713516675739"
      },
      "origin": "34.54.193.72",
      "url": "https://34.54.193.72/get"
    }
    

### Test quota enforcement

To test the quota enforcement defined in your `APIMExtensionPolicy`, send the request from the previous step to the Gateway ten times within the span of one minute.

You can run the following script to generate the requests: 
    
    
    #!/bin/sh
    for i in $(seq 1 11); do
        curl http://GATEWAY_IP_ADDRESS/get -H "Host: HOST_NAME" -H "x-api-key: API_KEY"
        sleep 1
    done

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



This action should trigger a quota violation and raise a fault similar to the following: 
    
    
    {"fault":{"faultstring":"Rate limit quota violation. Quota limit  exceeded. Identifier : _default","detail":{"errorcode":"policies.ratelimit.QuotaViolation"}}}

### Test rest operations enforcement

To test the rest operations enforcement, use the following command to send a request to the Gateway using a URL that is _not_ in the API operation set: 
    
    
    curl http://GATEWAY_IP_ADDRESS/post -H "Host: HOST_NAME" -H "x-api-key: API_KEY"

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



The request should fail with a response similar to the following: 
    
    
    {"fault":{"faultstring":"Invalid ApiKey for given resource","detail":{"errorcode":"oauth.v2.InvalidApiKeyForGivenResource"}}}

## View Apigee API Analytics in the Google Cloud console

You can view the API traffic handled by the GKE Gateway and the `APIMExtensionPolicy` using Apigee API Analytics in the Google Cloud console:

  1. Go to the **Apigee API management** page in the Google Cloud console: 

[Apigee API management](https://console.cloud.google.com/apigee)

  2. Select the Apigee organization where you installed the Apigee Operator for Kubernetes.
  3. Select **Analytics > API metrics** in the side navigation menu.
  4. In the **API Proxy Performance** tab, choose the environment you created in the optional installation step [ Create an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#create-apigee-environment), or the environment created by the Apigee Operator for Kubernetes during installation. The environment's name will begin with the prefix `apigee-ext-proc-enabled-env`.
  5. Observe the API traffic recorded.



## Troubleshoot

If you encounter issues when using API management policies with Apigee Operator for Kubernetes, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) for solutions to common errors.

## Next steps

To add additional policies, see [Add policies to the GKE Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
