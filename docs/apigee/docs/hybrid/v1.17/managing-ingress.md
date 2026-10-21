---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress/
title: Managing Apigee ingress gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:29:17.220109+00:00
---

# Managing Apigee ingress gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing Apigee ingress gateway Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/managing-ingress.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/managing-ingress.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/managing-ingress.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/managing-ingress.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/managing-ingress.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/managing-ingress.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/managing-ingress.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/managing-ingress.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/managing-ingress.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/managing-ingress.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/managing-ingress.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/managing-ingress.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/managing-ingress.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/managing-ingress.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/managing-ingress.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/managing-ingress.html)



##  Configuring Apigee ingress gateway 

You can configure your ingress gateways in your `overrides.yaml`. For example:

### Syntax
    
    
    ingressGateways:
    - name: INGRESS_NAME
      replicaCountMin: REPLICAS_MIN
      replicaCountMax: REPLICAS_MAX
      resources:
        requests:
          cpu: CPU_COUNT_REQ
          memory: MEMORY_REQ
        limits:
          cpu: CPU_COUNT_LIMIT
          memory: MEMORY_LIMIT
      svcAnnotations:  # optional.
        SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
      svcLoadBalancerIP: SVC_LOAD_BALANCER_IP # optional

### Example
    
    
    ingressGateways:
    - name: prod1
      replicaCountMin: 2
      replicaCountMax: 100
      resources:
        requests:
          cpu: 1
          memory: 1Gi
        limits:
          cpu: 2
          memory: 2Gi
      svcAnnotations:  # optional. See [Known issue 243599452](https://docs.cloud.google.com/apigee/docs/release/known-issues#243599452).
        networking.gke.io/load-balancer-type: "Internal"
      svcLoadBalancerIP: 198.252.0.123 

  * INGRESS_NAME is the name of the ingress gateway deployment. This can be any name that meets the following requirements: 
    * Have a maximum length of 17 characters
    * Contain only lowercase alphanumeric characters, '-' or '.'
    * Start with an alphanumeric character
    * End with an alphanumeric character

See [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-name) in the Configuration property reference 

  * REPLICAS_MIN and REPLICAS_MAX The minimum and maximum replica counts for Apigee ingress gateway in your installation. See [`ingressGateways[].replicaCountMin`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-replicacountmin) and [`ingressGateways[].replicaCountMax`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-replicacountmax) in the Configuration property reference.
  * CPU_COUNT_REQ and MEMORY_REQ The CPU and memory request for each replica of Apigee ingress gateway in your installation. Set these properties if you had previously set them for your Cloud Service Mesh ingress gateway in Apigee hybrid version 1.8 or earlier, for example in your `overlay.yaml` file.

See [`ingressGateways[].resources.requests.cpu`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-resources-requests-cpu) and [`ingressGateways[].resources.requests.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-resources-requests-memory) in the Configuration property reference. 

  * CPU_COUNT_LIMIT and MEMORY_LIMIT The maximum CPU and memory limits for each replica of Apigee ingress gateway in your installation. Set these properties if you had previously set them for your Cloud Service Mesh ingress gateway in Apigee hybrid version 1.8 or earlier, for example in your `overlay.yaml` file.

See [`ingressGateways[].resources.limits.cpu`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-resources-limits-cpu) and [`ingressGateways[].resources.limits.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-resources-limits-memory) in the Configuration property reference.

  * SVC_ANNOTATIONS_KEY SVC_ANNOTATIONS_VALUE (optional): **Note:** The `ingressGateways[].svcAnnotations` field in `overrides.yaml` is not working as expected. See [Known issue 243599452](https://docs.cloud.google.com/apigee/docs/release/known-issues#243599452)

This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. For example: 
        
        ingressGateways:
          svcAnnotations:
            networking.gke.io/load-balancer-type: "Internal"

Annotations vary from platform to platform. See your platform documentation for required and suggested annotations.

**Note:** You do not need to set `Annotations` here if you are creating your own Kubernetes service for ingress gateway deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress).  See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-svcannotations) in the Configuration property reference.
  * SVC_LOAD_BALANCER_IP (optional). On platforms that support specifying the load balancer IP address, the load balancer will be created with this IP address. On platforms that do not allow you to specify the load balancer IP address, this property is ignored. **Caution:** Make sure not to specify the same IP address as the current istio-ingressgateway. This could cause problems while that service is still on the cluster. **Note:** You do not need to set `LoadBalancerIP` if you are creating your own Kubernetes service for ingress gateway deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress).  See [`ingressGateways[].svcLoadBalancerIP`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-svcloadbalancerip) in the Configuration property reference.



### Apply the Apigee ingress gateway configuration

Apply changes to the organization scope: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ORG_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

##  Management tasks 

Some common management tasks for the Apigee ingress gateway:

###  Scaling Apigee ingress gateway: 

Update the following properties in your overrides file. 

  * `ingressGateways[].replicaCountMax`
  * `ingressGateways[].replicaCountMin`



See [`ingressGateways`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways) in the Configuration properties reference for details. 

Apply the changes: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

###  Updating resource allocation 

Update the following properties in your overrides file. 

  * `ingressGateways[].resources.limits.cpu`
  * `ingressGateways[].resources.limits.memory`
  * `ingressGateways[].resources.requests.cpu`
  * `ingressGateways[].resources.requests.memory`



See [`ingressGateways`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways) in the Configuration properties reference for details. 

Apply the changes: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

###  Updating the Apigee ingress gateway service 

Update the following properties in your overrides file. 

  * `ingressGateways[].svcAnnotations`
  * `ingressGateways[].svcLoadBalancerIP`



See [`ingressGateways`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways) in the Configuration properties reference for details. 

Apply the changes: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

###  Disable the loadbalancer for the default Apigee ingress gateway service: 

If you create a [custom Kubernetes service](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress#customservice) for your ingress gateway deployment, you can disable creation of a load balancer on the default Kubernetes service. Update the [`ingressGateways[].svcType`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways-svctype) property to `ClusterIP` in your overrides file. For example: 
    
    
    ingressGateways:
      - name: my-ingress-gateway
        replicaCountMin: 2
        replicaCountMax: 10
        **svcType: ClusterIP**

Apply the changes: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

###  Configure TLS and mTLS 

See [Configuring TLS and mTLS on the ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/ingress-tls). 

###  Enabling non-SNI clients 

See [Enable non-SNI and HTTP clients](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-non-sni). 

### Installing additional Apigee ingress gateways

In the `overrides.yaml` file you can add multiple ingress gateways. The `ingressGateways` configuration property is an array. For more information, see [ingressGateways](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways) in the Configuration properties reference. 

For example: 
    
    
    ingressGateways:
    - name: **fruit**
      replicaCountMin: 2
      replicaCountMax: 10
    
    - name: **meat**
      replicaCountMin: 2
      replicaCountMax: 10

Apply the changes: 
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace apigee \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

### Mapping virtual hosts to Apigee ingress gateway deployments

You can use selector labels to map a virtual host to an Apigee ingress gateway deployment. In the following example, the virtual host `spam-vh` is configured to run on the ingress gateway labeled `meat` and the other two virtual hosts run on the `fruit` ingress gateway. The ingress gateways must be properly labeled, as explained in Installing additional Cloud Service Mesh gateways. **Note:** You must specify both of the selectors: `selector:app` and `selector:ingress_name` to properly apply an ingress gateway to a virtual host.**Tip:** For security purposes, it is best practice to have a separate TLS cert/key pair for each virtual host. If you are using a Subject Alternative Name (SAN ) certificate, this TLS cert/key pair should be used on one virtual host that is shared across the domain. 
    
    
    virtualhosts:
    - name: spam-vh
      sslCertPath: cert-spam.crt
      sslKeyPath: cert-spam.key
      **selector:
        app: apigee-ingressgateway
        ingress_name: meat**
    - name: banana-vh
      sslCertPath: cert-banana.crt
      sslKeyPath: cert-banana.key
      **selector:
        app: apigee-ingressgateway
        ingress_name: fruit**
    - name: plum-vh
      sslCertPath: cert-plum.crt
      sslKeyPath: cert-plum.key
      **selector:
        app: apigee-ingressgateway
        ingress_name: fruit**
    
        

### Adding custom ciphersuites to Apigee ingress gateway deployments

You can add custom ciphersuites to your Apigee ingress gateway deployment with the [`virtualhosts.cipherSuites`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-ciphersuites) property in your overrides file. 

See [`virtualhosts.cipherSuites`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-ciphersuites) for the default ciphersuites enabled in Apigee hybrid. 

You can enable older versions of TLS with the [`virtualhosts.minTLSProtocolVersion`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-mintlsprotocolversion) property and add custom ciphersuites to your Apigee ingress gateway deployment with the [`virtualhosts.cipherSuites`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#virtualhosts-ciphersuites) property in your overrides file. 

For example, to enable TLS v.1.1:
    
    
    virtualhosts:
    - name: ENV_GROUP_NAME
      minTLSProtocolVersion: "1.1"
      cipherSuites:
      - "ECDHE-ECDSA-AES128-GCM-SHA256"
      - "ECDHE-RSA-AES128-GCM-SHA256"
      - "ECDHE-ECDSA-AES256-GCM-SHA384"
      - "ECDHE-RSA-AES256-GCM-SHA384"
      - "ECDHE-ECDSA-CHACHA20-POLY1305"
      - "ECDHE-RSA-CHACHA20-POLY1305"
      - "ECDHE-ECDSA-AES128-SHA"
      - "ECDHE-RSA-AES128-SHA"
      - "ECDHE-ECDSA-AES256-SHA"
      - "ECDHE-RSA-AES256-SHA"
      ...
    

**Note:** This property overrides the list of cipher suites supported by Envoy, and does not append to it.

### Customize Ingress access logs

You can customize the Apigee ingress gateway access log destination and format with the [`istiod.accessLogFile`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#istiod-accesslogfile) and [`istiod.accessLogFormat`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#istiod-accesslogformat) configuration properties. In the following example, the output will be sent to `/dev/stdout`, which is the default value for `istiod.accessLogFile`: 
    
    
    istiod:
      accessLogFormat: '{"request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","status":"%RESPONSE_CODE%"}'
    

You can disable Apigee ingress gateway access logging by assigning [`istiod.accessLogFile`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/onfig-prop-ref#istiod-accesslogfile) and empty value. For example: 
    
    
    istiod:
      accessLogFile: ''
    

## FAQ

How does this work with my existing Cloud Service Mesh/Istio installation in another namespace? 
     As long as Apigee is installed in a dedicated namespace - Apigee ingress gateway can be run alongside an already existing Cloud Service Mesh/Istio installation in the cluster. Apigee ingress gateway doesn't store any configuration in apiserver hence there won't be any conflict. 
Who is responsible for upgrading Apigee ingress gateway components? 
     Apigee takes care of upgrades to Apigee ingress gateway components Apigee ingress gateway which happens during regular hybrid upgrades and patch releases. 
How do I expose port 80 in Apigee ingress gateway? 
     Port 80 is not supported by Apigee ingress gateway. If you are migrating from Cloud Service Mesh to Apigee ingress gateway, and you followed the instructions in [the community post](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Apigee-hybrid-ingress-Three-different-options-to-expose-your/ta-p/79149) to enable Port 80, it will not work with Apigee Ingress gateway. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
