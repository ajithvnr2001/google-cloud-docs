---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies/
title: Add policies to the GKE Gateway \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:12.828244+00:00
---

# Add policies to the GKE Gateway  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Add policies to the GKE Gateway Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to add Apigee runtime policies and a Google token injection policy to the Google Kubernetes Engine (GKE) Gateway with the Apigee Operator for Kubernetes. Adding an available set of policies to the Gateway allows you to extend the functionality of the Gateway beyond API product enforcement to include additional security and business rules. 

The Apigee Operator for Kubernetes can be used to add the following policies to the Gateway: 

  * [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy)
  * [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy)
  * [Google token injection policy](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview)
  * [GenerateJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy)
  * [KVM policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/kvm-policy)
  * [OASValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy)
  * [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy)
  * [OAuthv2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy)
  * [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy)
  * [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy)



## Overview

The following sections describe how to: 

  * Add policies to the GKE Gateway.
  * Create a template rule to enforce usage of the policies.
  * Create an Apigee template to use the template rule.
  * Deploy the Apigee Gateway policy with the template.
  * Validate policy enforcement.



## Before you begin

To modify your GKE Gateway with the complete set of policies used as an example in this guide, you must have a service account with the roles required to create tokens within Apigee and deploy proxies and extensions. If you choose _not_ to create Google tokens, you do not need to add the additional roles to your service account and you can skip to the next section.

To create a service account with the required permissions: 

  1. If you created a service account named `apigee-apim-gsa` in the Apigee Operator for Kubernetes [installation guide](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install), you can skip this step and proceed to the next step. Otherwise, create the service account: 
         
         gcloud iam service-accounts create apigee-apim-gsa --project=$PROJECT_ID

  2. Grant the service account the necessary role to create tokens: 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
           --role "roles/iam.serviceAccountTokenCreator"

  3. Grant the `apigee-apim-gsa` service account the necessary role to deploy proxies and extensions: 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
           --role "roles/iam.serviceAccountUser"




## Modify your GKE Gateway with policies

You can choose to modify your GKE Gateway with one or more policies to extend its functionality. This example walkthrough applies a `yaml` file to the Gateway that includes the specifications for two Apigee policies and a Google token injection policy.

Each one of the policies applied to the Gateway using the following `yaml` file performs a different role when evaluating requests sent to the Gateway: 

  * The SpikeArrest policy controls the peak message rate by defining a maximum rate of allowed requests over a unit of time. In this example, the maximum rate is set to five per minute. To learn more about how the SpikeArrest policy is used to smooth out sudden spikes in traffic, see [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy).
  * The JavaScript policy lets you add custom JavaScript code to the Gateway requests. In this example, the policy is used to add a custom header to the request. For more on how the JavaScript policy is used to add custom code, see [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy).
  * The Google token injection policy is used to inject a Google authentication access token into the Gateway requests, using the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). Apigee supports using Google OAuth tokens or OpenID Connect tokens to authenticate with Google services. To learn more about authentication tokens, see [Using Google authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview).



Add the policies to the Gateway: 

  1. Create a new file named `apigee-policies.yaml` in the `apim` namespace.
  2. Copy the contents of the following file into the new file you created: 
         
         # apigee-policies.yaml
         apiVersion: apim.googleapis.com/v1
         kind: SpikeArrest
         metadata:
           name: spike-arrest
           namespace: apim
         spec:
           identifier:
             ref: request.header.name
           useEffectiveCount: true
           peakMessageRate:
             value: "5pm"
         ---
         apiVersion: apim.googleapis.com/v1
         kind: Javascript
         metadata:
           name: js-add-headers
           namespace: apim
         spec:
           timeLimit: 2000
           source: |
             var sum = 1+1;
             context.setVariable("request.header.first", 1);
             context.setVariable("request.header.second", 1);
             context.setVariable("request.header.sum", sum);
         ---
         apiVersion: apim.googleapis.com/v1
         kind: AssignMessage
         metadata:
           name: google-token-policy
           namespace: apim
         spec:
           setActions:
             - authentication:
                 googleAccessToken:
                   scopes:
                     - 'https://www.googleapis.com/auth/cloud-platform'
           AssignTo:
             createNew: false
             type: request
         ---
         apiVersion: apim.googleapis.com/v1
         kind: KVM
         metadata:
           name: kvm-1
           namespace: apim
         spec:
           delete:
           - keys:
             - value: mykey
           exclusiveCache: true
           expiryTimeInSecs: 3600
           get:
           - assignTo: response.header.mykvm
             keys:
             - value: mykey
           initialEntries:
           - keys:
             - key1
             values:
             - val1
           - keys:
             - mykey
             values:
             - initvalue
           isEncrypted: false
           put:
           - keys:
             - value: mykey
             values:
             - value: request.header.mykvm
           scope: environment
         ---
         apiVersion: apim.googleapis.com/v1
         kind: OASValidation
         metadata:
           name: oas-validation-1
           namespace: apim
         spec:
           openApiSpec: |
             openapi: 3.0.4
             info:
               title: Sample API
               description: Optional multi/single line description.
               version: 0.1.9
             servers:
               - url: http://apigee-apim-operator-test.apigee.net
                 description: Optional server description, our main host in httproute
             paths:
               /get:
                 get:
                   summary: just for test
                   description: Optional extended description in CommonMark or HTML.
                   parameters:
                     - name: X-Request-Type
                       in: header
                       description: Must be 'internal' or 'external'.
                       required: true
                       schema:
                         type: string
                         enum:
                           - internal
                           - external
                   responses:
                     '200': # status code
                       description: A JSON object
                       content:
                         application/json:
                           schema:
                             type: object
                             properties:
                               headers:
                                 type: object
           source: request
         ---
         apiVersion: apim.googleapis.com/v1
         kind: ServiceCallout
         metadata:
           name: service-callout-1
           namespace: apim
         spec:
           request:
             clearPayload: true
             variable: myRequest
             ignoreUnresolvedVariables: true
             removeActions:
               - payload: true
               - queryParams:
                 - name: rq-param1
                 - name: rq-param2
             copyActions:
               - version: true
               - verb: true
             addActions:
               - headers:
                 - name: X-header1
                   value: value1
                 - name: X-header2
                   value: value2
               - queryParams:
                 - name: q-param1
                   value: value1
                 - name: q-param2
                   value: value2
             setActions:
               - verb: PUT
               - formParams:
                 - name: f-param1
                   value: value1
                 - name: f-param2
                   value: value2
           response: calloutResponse
           timeout: 30000
           httpTargetConnection:
             URL: https://httpbin.org/put
             properties:
               - name: success.codes
                 value: 1xx,2xx,3xx,400
               - name: supports.http11
                 value: "true"

  3. Apply the `yaml` file to the Gateway using the following command: 
         
         kubectl -n apim apply -f apigee-policies.yaml




## Create a TemplateRule as a SharedFlow template

In this step, you will create a `TemplateRule` to enforce the policies you have added to the Gateway. A _template rule_ is a rule for SharedFlows created by organization administrators to ensure that only _approved_ policies are applied to Gateway traffic by service developers. A template rule ensures that developers understand which policies are available to them, which policies are required for specific use cases, and which policies can't be used by service developers.

### Create a template rule

Create a template rule to enforce usage of the AssignMessage policy: 

  1. Create a new `yaml` file named `template-rule.yaml` in the `apim` namespace.
  2. Copy the contents of the following file into the new file you created: 
         
         # template-rule.yaml
         apiVersion: apim.googleapis.com/v1
         kind: ApimTemplateRule
         metadata:
           name: template-rule
           namespace: apim
         spec:
           allowList: [SpikeArrest, Javascript, GenerateJWT, KVM, OASValidation, OAuthv2, ServiceCallout]
           requiredList: [AssignMessage]
           denyList: []

In this example, the template rule tells developers that the AssignMessage policy describing the Google token injection policy is required. It also tells developers that they can use the SpikeArrest, JavaScript, GenerateJWT, KVM, OASValidation, OAuthv2, and ServiceCallout policies in their API management. There are no policies specified in the deny list. 




### Apply the template rule

Apply the template rule using the following command: 
    
    
    kubectl apply -f template-rule.yaml

## Create an Apigee template to use the template rule

Create an Apigee template to include the template rule you created in the previous section: 

  1. Create a new `yaml` file named `new-admin-template.yaml` in the `apim` namespace.
  2. Copy the contents of the following file into the new file you created: 
         
         # new-admin-template.yaml
         apiVersion: apim.googleapis.com/v1
         kind: ApimTemplate
         metadata:
           name: new-admin-template
           namespace: apim
         spec:
           apimTemplateRule:
             group: apim.googleapis.com
             kind: ApimTemplateRule
             name: template-rule
             namespace: apim
           templates:
           - mode: REQUEST
             flows:
             - name: preflow
               policies:
               - group: apim.googleapis.com
                 kind: OASValidation
                 name: oas-validation-1
                 namespace: apim
               - group: apim.googleapis.com
                 kind: SpikeArrest
                 name: spike-arrest
                 namespace: apim
             - name: ConditionalGetFlow
               policies:
               - group: apim.googleapis.com
                 kind: Javascript
                 name: js-add-headers
                 namespace: apim
               condition: request.verb="GET"
             - name: postflow
               policies:
               - group: apim.googleapis.com
                 kind: AssignMessage
                 name: google-token-policy
                 namespace: apim
               - group: apim.googleapis.com
                 kind: ServiceCallout
                 name: service-callout-1
                 namespace: apim
           - mode: RESPONSE
             flows:
             - name: postflow
               policies:
               - group: apim.googleapis.com
                 kind: KVM
                 name: kvm-1
                 namespace: apim

  3. Apply the new template using the following command: 
         
         kubectl apply -f new-admin-template.yaml




## Deploy the Apigee Gateway policy

In this step, you will apply a new file to your Gateway that includes the specifications for an `ApigeeGatewayPolicy`. This policy is used to deploy the Apigee template to the Gateway. 

Deploy the Apigee Gateway policy: 

  1. Create a new `yaml` file named `apigee-gateway-policy-withSA.yaml` in the `apim` namespace.
  2. Copy the contents of the following file into the new file you created: 
         
         # apigee-gateway-policy-withSA.yaml
         apiVersion: apim.googleapis.com/v1
         kind: ApigeeGatewayPolicy
         metadata:
           name: apim-template-injection
           namespace: apim
         spec:
           serviceAccount: apigee-apim-gsa@PROJECT_ID.iam.gserviceaccount.com
           ref:
             group: apim.googleapis.com
             kind: ApimTemplate
             name: new-admin-template
             namespace: apim
           targetRef:
             group: apim.googleapis.com
             kind: APIMExtensionPolicy
             name: APIMEXTENSION_POLICY_NAME
             namespace: apim

Replace PROJECT_ID with your Google Cloud project ID.

Replace APIMEXTENSION_POLICY_NAME with the name of the APIMExtensionPolicy that you want to use to enforce the Apigee Gateway policy. If you created an APIMExtensionPolicy to create a traffic extension, use the name of the policy you created. If you used an ApigeeBackendService to create a traffic extension, use the name of the ApigeeBackendService. When you create an ApigeeBackendService, the Apigee Operator for Kubernetes creates an APIMExtensionPolicy with the same name and namespace as the BackendService.

  3. Apply the policy: 
         
         kubectl apply -f apigee-gateway-policy-withSA.yaml

  4. Verify the deployment status of the new Gateway policy: 
         
         kubectl -n apim get ApigeeGatewayPolicy

Once deployed, the policy `STATUS` should display `CREATED`.




After the new Gateway policy is deployed, wait two minutes before sending a request to the Gateway to allow the policy to propagate to the cluster.

## Validate policy enforcement

To confirm that the Apigee Gateway policies are working as expected, send requests to the Gateway as described in the following sections. 

### AssignMessage policy enforcement

To confirm that the {company_name} token is injected into the request using the AssignMessage policy, send a request to the Gateway using the following command: 
    
    
    curl http://GATEWAY_IP_ADDRESS/get -H "Host: HOST_NAME" -H "x-api-key: API_KEY"

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command: 
        
        kubectl get gateway GATEWAY_NAME

  * `HOST_NAME` is the name of the host.
  * `API_KEY` is the API key value.



A successful response should include an `Authorization` header with the generated bearer token, similar to the following: 
    
    
    {
      "args": {},
      "headers": {
        "Accept": "*/*",
        **"Authorization" : "Bearer ya29.c.c0ASRK0Gbw03y9cfvxL11DxaRYBQUU18SmUP4Vu63OckHI5cX7wJ4DmGMG2vbDDS69HXJHqMj-lak4tcqOsJGmE65crn2gNuJLanXidwM8"**,
        "First": "1.0",
        "Host": "apigee-apim-operator-test.apigee.net",
        "Second": "1.0",
        "Sum": "2",
        "User-Agent": "curl/8.7.1",
        "X-Api-Key": "McYcHGR3PTSGLXExvKADwQ1JJeCjgPDUvAakCl0rJKCFaX0Y",
        "X-Cloud-Trace-Context": "0fd3dadc2a3c328fa968d5f5f1434c29/18300783092696918345"
      },
      "origin": "34.54.108.129",
      "url": "apigee-apim-operator-test.apigee.net/get"
    }

### SpikeArrest policy enforcement

You can test enforcement of the SpikeArrest policy by sending a request to the Gateway ten times within the span of one minute.

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



The response will appear similar to the following: 
    
    
    "fault":{"faultstring":"Spike arrest violation. Allowed rate : MessageRate{capacity=5, period=Minutes}","detail":{"errorcode":"policies.ratelimit.SpikeArrestViolation"}}}

### JavaScript policy enforcement

To confirm that the JavaScript policy is working as expected, send a request to the Gateway using the following command: 
    
    
    curl http://GATEWAY_IP_ADDRESS/get \
      -H "Host: HOST_NAME" \
      -H "x-api-key: API_KEY" \
      -H "X-Request-Type: external" -i

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



The JavaScript policy sets three request headers: `First`, `Second`, and `Sum`, as seen in the response: 
    
    
    HTTP/1.1 200 OK
    ...
    {
      "args": {},
      **"headers" : {
        ...
        "First": "1.0",
        ...
        "Second": "1.0",
        "Sum": "2",**
        ...
      },
      ...
    }

### OASValidation policy enforcement

To confirm that the OASValidation policy is working as expected, send a request to the Gateway using the following command: 
    
    
    curl "http://GATEWAY_IP_ADDRESS/get"  \
      -H "Host: HOST_NAME" \
      -H "x-api-key: API_KEY" \
      -H "X-Request-Type: badvalue"

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



The command includes an invalid value for the `X-Request-Type` header. The request will fail with a response similar to the following: 
    
    
    {"fault":{"faultstring":"OASValidation oas-validation-1 with resource \"oas:\/\/oas-validation-1.yaml\": failed with reason: \"[ERROR - Instance value (\"badvalue\") not found in enum (possible values: [\"internal\",\"external\"]): []]\"","detail":{"errorcode":"steps.oasvalidation.Failed"}}}

Sending the same request with a valid value for the `X-Request-Type` header will succeed. For example: 
    
    
    curl "http://GATEWAY_IP_ADDRESS/get"  \
      -H "Host: HOST_NAME" \
      -H "x-api-key: API_KEY" \
      -H "X-Request-Type: external" -i

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateways.gateway.networking.k8s.io GATEWAY_NAME -o=jsonpath="{.status.addresses[0].value}"

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



### ServiceCallout policy enforcement

You can verify enforcement of the ServiceCallout policy by opening a debug session and sending a few valid requests to the proxy.

To open a debug session, follow these steps:

  1. In the Google Cloud console, go to the **API Proxies** page. 

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the `global-ext-lb1-apim-policy` proxy you deployed to the environment created for the Apigee Operator for Kubernetes.
  3. Click the **Debug** tab.
  4. In the **Debug session** window, click **Start Debug Session**.
  5. In the **Debug session** pane, make the following selections: 
     * **Environment** : Select the environment you created for the Apigee Operator for Kubernetes from the list of available environments.
     * **Filter** : Select **None (All transaction)**.
  6. Click **Start**.



Once the session is started, you can send valid requests to the proxy: 
    
    
    curl "GATEWAY_IP_ADDRESSget"  \
      -H "Host: HOST_NAME" \
      -H "x-api-key: API_KEY" \
      -H "X-Request-Type: external" -i

Where: 

  * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
        
        kubectl get gateway GATEWAY_NAME

  * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
  * `API_KEY` is the API key value obtained in Testing set up.



The request and response transactions are displayed in the **Transactions** pane. Select a successful transaction from the list to display the flow. You should be able to see that `ServiceCallout` policy executed successfully.

### KVM policy enforcement

When the KVM policy executes successfully, it initializes the KVM with a starting value for the key `mykey`. When there is a response transaction, the KVM policy retrieves the value of `mykey` and stores it in the response header `mykvm`. When the KVM policy executes again, it inserts the new value for `mykey` obtained from the request header `mykvm`.

You can check the headers for each transaction to confirm that the policy is storing a value in the KVM in one transaction and retrieving the same value in the next transaction, as shown in the following example. **Note** : Make sure to use `curl` with the command line option `-i` to see the response headers.

Test the KVM policy: 

  1. Send a request to the Gateway: 
         
         curl -i "http://GATEWAY_IP_ADDRESS/get" \
           -H "Host: HOST_NAME" \
           -H "x-api-key: API_KEY" \
           -H "X-Request-Type: external" \
           -H "KVM_NAME: next-value1" -i

Where: 

     * `GATEWAY_IP_ADDRESS` is the IP address of the Gateway. You can retrieve the Gateway IP address using the following command, where `GATEWAY_NAME` is the name of the Gateway: 
           
           kubectl get gateway GATEWAY_NAME

     * `HOST_NAME` is the hostname defined in the Gateway's `HTTPRoute`.
     * `API_KEY` is the API key value obtained in Testing set up.
     * `KVM_NAME` is the name of the KVM.
  2. Check the response headers to confirm that the KVM policy executed successfully and that an initial value was stored for `mykvm`. The response should appear similar to the following: 
         
         HTTP/1.1 200 OK
         access-control-allow-credentials: true
         access-control-allow-origin: *
         Content-Length: 517
         content-type: application/json
         date: ...
         server: gunicorn/19.9.0
         **mykvm: initvalue**
         via: 1.1 google
         {
           "args": {
           ...
           "url": "http://apigee-apim-operator-test.apigee.net/get"
           }
         }

  3. Send another request to the Gateway: 
         
         curl -i "http://GATEWAY_IP_ADDRESS/get" \
           -H "Host: HOST_NAME" \
           -H "x-api-key: API_KEY" \
           -H "mykvm: next"X-Request-Type: external" -H "mykvm: next-value2" -i

The response should be similar to the following: 
         
         HTTP/1.1 200 OK
         access-control-allow-credentials: true
         access-control-allow-origin: *
         Content-Length: 517
         content-type: application/json
         date: ...
         server: gunicorn/19.9.0
         **mykvm: next-value2**
         via: 1.1 google
         {
           "args": {
           ...
           "url": "http://apigee-apim-operator-test.apigee.net/get?rq-param2=rq-val1&x-param1=xval1"
           }
         }

You can see that the KVM policy executed successfully because the value of the `mykvm` header is updated to the value of the request header `mykvm`.

  4. Send one more request: 
         
         curl -i "http://GATEWAY_IP_ADDRESS/get" \
           -H "Host: HOST_NAME" \
           -H "x-api-key: API_KEY" \
           -H "X-Request-Type: external" -H "mykvm: next-value3" -i

The response should be similar to the following: 
         
         HTTP/1.1 200 OK
         access-control-allow-credentials: true
         access-control-allow-origin: *
         Content-Length: 517
         content-type: application/json
         date: ...
         server: gunicorn/19.9.0
         **mykvm: next-value2**
         via: 1.1 google
         {
           "args": {
           ...
           "url": "http://apigee-apim-operator-test.apigee.net/get?rq-param2=rq-val1&x-param1=xval1"
           }
         }

The value of the `mykvm` header is updated again, showing that the value displayed in the response is the values stored in the previous transaction.




## Troubleshoot

If you encounter issues when adding policies to the GKE Gateway, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) for solutions to common errors.

## What's next

  * Learn more about the [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy).
  * Learn more about the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
