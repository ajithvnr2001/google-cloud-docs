---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/default-domain/
title: Using test domains \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:41.428454+00:00
---

# Using test domains  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/default-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using test domains Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to access the Knative serving services in your cluster for testing purposes before you choose to [map a custom domain](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains).

By default, the services that you deploy to your Knative serving clusters are set to the `nip.io` base domain. Therefore, if you use the recommended name for ingress gateway, you can immediately test your services and send requests without additional configuration. For example: `http://{SERVICE_NAME}.{NAMESPACE}.kuberun.{EXTERNAL_IP}.nip.io`.

**Important:** For production, you must [map a custom domain](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains), which is also required to enable HTTPS and [use automatic TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls).

Note that there can be [issues around the reliability of requests](https://en.wikipedia.org/wiki/Wildcard_DNS_record) when using DNS wildcards, including the [nip.io](http://nip.io/) domain, which is a free DNS wildcard service. In contrast, setting up and using a [custom domain](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) for testing can offer increased reliability.

Optionally, you can also access your services through the external IP address.

## Using the `nip.io` test domain

To access a service using the default `nip.io` base domain, you can locate the URL from within the Google Cloud console or you can construct the URL manually.

### Console

  1. In the Google Cloud console, go to the **Knative serving** page.

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. In the list, click the service for which you want to obtain the URL.

  3. Near the top of the page the **URL** is displayed.

For example: `http://my-service.default.kuberun.11.111.11.111.nip.io`

Where _my-service_ is the name of the Knative serving service, _default_ is the namespace, and _11.111.11.111_ is the IP address of your external load balancer.




### Manually

To manually construct the URL to your service, you use the name of the service, the namespace in which that service is running, and the IP address of your load balancer:
    
    
    http://SERVICE.NAMESPACE.kuberun.EXTERNAL_IP.nip.io
    

Replace:

  * SERVICE_NAME with the name of your service.
  * NAMESPACE with the namespace where you deployed the service. By default, services are deployed to the `default` namespace.
  * EXTERNAL_IP with the external IP address of your load balancer.



For example, if you have a service named `hello` in the `default` namespace and your external IP address is `12.345.67.890`, the URL might look like:

`http://hello.default.kuberun.12.345.67.890.nip.io`

## Using the external IP address

Optionally, you can use the external IP address of your load balancer to access your services through [cURL](https://curl.se/docs/manpage.html) commands or by manually configuring an alternative DNS wildcard service.

### Before you begin

  * Ensure that your Google Cloud CLI and kubectl command-line tools are installed and up-to-date:

    * [GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools)
    * [GKE clusters outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools)
  * You must have at least the [_Kubernetes Engine Developer_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles) Identity and Access Management role or equivalent permissions.




### Getting the external IP address

When your GKE Enterprise cluster is created, the Istio ingress controller creates a Google Cloud Network Load Balancer with a publicly available IP address.

To configure access to your service with cURL or a DNS service, you must first obtain the external IP address of the load balancer service:

### Console

To get the load balancer's external IP address from the Google Cloud console: 

  1. Go to the GKE page in the Google Cloud console:   
[Go to GKE](https://console.cloud.google.com/kubernetes)
  2. Click **Services and ingress**. 
  3. Identify the service that is your cluster's Istio ingress. The service's **Type** will be **External load balancer** , and the **Name** will be `istio-ingressgateway`. 
  4. Once you've found your cluster's Istio ingress service, copy its **Endpoint**. This will be the IP address without the port number. For example, you might see `00.000.000.000:11` listed as an endpoint, but you only need to copy `00.000.000.000`. 



### kubectl

To obtain the external IP for the Load Balancer, run the following command:
    
    
    kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
    
    
    NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
    istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

After obtaining the external IP address of your load balancer, you can use it to in cURL commands or with a DNS wildcard service to access your Knative serving services.

### Using `cURL`

You can use [cURL](https://curl.se/docs/manpage.html) commands with the default `nip.io` base domain to send requests to your service.

You specify the external IP address of your load balancer along with the names of your service and namespace in the cURL command:
    
    
    curl --header 'Host: SERVICE_NAME.NAMESPACE.kuberun.EXTERNAL_IP.nip.io' EXTERNAL_IP

Replace:

  * SERVICE_NAME with the name of your Knative serving service.
  * NAMESPACE with the namespace in which your service is running.
  * EXTERNAL_IP with the external IP address of your load balancer.



Example:

`curl --header 'Host: my-service.default.kuberun.12.345.67.890.nip.io' http://12.345.67.890`

### Using other DNS wildcard services

By default, your Knative serving services use the [nip.io](http://nip.io/) DNS wildcard service. However, you can choose to use other services like [sslip.io](https://sslip.io/). To configure other DNS wildcard services you must first obtain the external IP address of your load balancer and then use that IP address to configure the DNS wildcard service.

#### Configuring your cluster's domain

Knative serving uses the `config-domain` ConfigMap to define the base domain for which all your deployed Knative serving services use. You can update that ConfigMap through the Google Cloud console or with `kubectl` commands.

### Console

To change the default base domain from `nip.io` to one of the DNS wildcard services in the Google Cloud console:

  1. Go to the Knative serving **Domain mappings** page in the Google Cloud console:

[Go to Domain mappings](https://console.cloud.google.com/kubernetes/run/domains)

  2. Select **Add mapping > Add cluster default domain**

  3. Select the checkbox next to "Apply this domain mapping to all Knative serving services deployed to this cluster."

  4. Select your cluster from the drop-down menu.

  5. In the **Domain** field, enter the wildcard DNS site you want to use. For example: `sslip.io`




### kubectl

To change the default base domain from `nip.io` to one of the DNS wildcard sites, use the command:
    
    
    kubectl patch configmap config-domain --namespace knative-serving --patch \
      '{"data": {"kuberun.EXTERNAL_IP.nip.io": null, "DNS_SERVICE": ""}}'

Replace

  * EXTERNAL_IP with the Load Balancer external IP address.
  * DNS_SERVICE with the wildcard DNS site you are using. For example: `sslip.io`



Your service is now available at `http://{SERVICE_NAME}.{NAMESPACE}.kuberun.{EXTERNAL_IP}.{DNS_SERVICE}`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
