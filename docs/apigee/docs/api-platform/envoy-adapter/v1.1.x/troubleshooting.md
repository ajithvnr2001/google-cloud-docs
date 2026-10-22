---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:43.613868+00:00
---

# Troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

##  Istio 404 (Not Found) error 

Debugging a 404 (Not Found) error on Istio can be frustrating. Hopefully this will give you a place to start tracking down where things may be going wrong.

### Wildcard Gateway conflict

There can be only one Gateway definition that uses a wildcard "*" hosts value. If you've deployed anything else that includes a wildcard Gateway, client calls will fail with a 404 status.

Example:
    
    
    $ istioctl get gateways
    GATEWAY NAME         HOSTS     NAMESPACE   AGE
    bookinfo-gateway     *         default     20s
    httpbin-gateway      *         default     3s

If so, you'll need to delete or change one of the conflicting gateways.

## Search for where the route is failing

Istio is like an onion (or, perhaps, an Ogre), it has layers. A systematic way to debug a 404 is to work outward from the target.

### The backend workload

Verify you can access the workload from the sidecar:
    
    
    kubectl exec $WORKLOAD_POD -c istio-proxy -- curl localhost:80/headers

### The backend sidecar

Set your service address and get the IP address of the workload pod.
    
    
    SERVICE=httpbin.default.svc.cluster.local:80
      POD_IP=$(kubectl get pod $WORKLOAD_POD -o jsonpath='{.status.podIP}')

Access the workload through the sidecar:
    
    
    kubectl exec $WORKLOAD_POD -c istio-proxy -- curl -v http://$SERVICE/headers --resolve "$SERVICE:$POD_IP"

Or, if Istio mTLS is enabled:
    
    
    kubectl exec $WORKLOAD_POD -c istio-proxy -- curl -v https://$SERVICE/headers --resolve "$SERVICE:$POD_IP" --key /etc/certs/key.pem --cert /etc/certs/cert-chain.pem --cacert /etc/certs/root-cert.pem --insecure

### The gateway (or a frontend sidecar)

Access the service from the gateway:
    
    
    kubectl -n istio-system exec $GATEWAY_POD -- curl -v http://$SERVICE/header

Or, if Istio mTLS is enabled:
    
    
    kubectl -n istio-system exec $GATEWAY_POD -- curl -v https://$SERVICE/headers --key /etc/certs/key.pem --cert /etc/certs/cert-chain.pem --cacert /etc/certs/root-cert.pem --insecure

##  Missing analytics 

If you aren't seeing analytics in the Analytics UI, consider these possible causes: 

  * Apigee intake can be delayed a few minutes
  * Envoy gRPC Access Log not configured correctly
  * Envoy cannot reach Remote Service
  * Remote Service is failing upload



##  Missing or bad API key not being rejected 

If API key validation is not working properly, consider these possible causes: 

**Direct proxy**

Check the `ext-authz` configuration. 

**Sidecar**

  * Be sure listener is configured for intercept.
  * Check the `ext-authz` configuration.



**Invalid requests are being checked and allowed**

  * Remote Service configured for fail open
  * Envoy not configured for RBAC checks



For information on how to address these issues, refer to the following Envoy documentation topic: [External Authorization](https://www.envoyproxy.io/docs/envoy/v1.15.0/api-v3/extensions/filters/http/ext_authz/v3/ext_authz.proto.html), and refer to information about the `failure_mode_allow` property. This property allows you to change the filter's behavior on errors. 

##  Missing or bad JWT not being rejected 

The probable cause is that the Envoy JWT filter is not configured. 

##  Valid API key fails 

### Probable causes

  * Envoy cannot reach the remote service
  * Your credentials are not valid
  * Apigee API Product not configured for target and env



###  Troubleshooting steps 

#### Check your API Product on Apigee

  * _Is it enabled for your environment (test vs prod)?_

The product must be bound to the same environment as your Remote Service.

  * _Is it bound to the target you're accessing?_

Check the **Apigee remote service targets** section. Remember, the service name must be a fully qualified host name. If it's an Istio service, the name will be something like `helloworld.default.svc.cluster.local`code> \- which represents the `helloworld` service in the `default` namespace.

  * _Does the Resource Path match your request?_

Remember, a path like `/` or `/**` will match any path. You may also use '*' or '**' wildcards for matching.

  * _Do you have a Developer App?_

The API Product must be bound to a Developer App to check its keys.




#### Check your request

  * _Are you passing the Consumer Key in the`x-api-key header`_

Example:
        
        curl http://localhost/hello -H "x-api-key: wwTcvmHvQ7Dui2qwj43GlKJAOwmo"

  * _Are you using a good Consumer Key?_

Ensure the Credentials from the App you're using are approved for your API Product.




#### Check the Remote Service logs

  * _Start the Remote Service with logging at the`debug level`_

Use `-l debug` option on the command line.

  * _Attempt to access your target and check the logs_

Check the logs for a line that looks something like this:
        
        Resolve api: helloworld.default.svc.cluster.local, path: /hello, scopes: []
        Selected: [helloworld]
        Eliminated: [helloworld2 doesn't match path: /hello]
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
