---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-ingress-gateway/
title: Migrate Ingress to Gateway API \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:44.526948+00:00
---

# Migrate Ingress to Gateway API  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-ingress-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Migrate Ingress to Gateway API Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to migrate your traffic management on Google Kubernetes Engine (GKE) from the Ingress API to Gateway API. Gateway API provides a fully-managed, Google Cloud solution for handling your application traffic.

To minimize downtime and mitigate risk, the most effective approach to migrate to Gateway API is to run both your existing Ingress API and the new Gateway API configurations simultaneously. This method allows for thorough testing of the new Gateway configuration in a live environment without impacting your current services. After you validate the new Gateway configuration, you can perform a quick DNS cutover to redirect traffic to Gateway API, and help ensure a smooth and low-risk transition.

At a high level, the migration strategy involves the following phases:

  1. Configure the new load balancer.
  2. Define rules for handling incoming traffic.
  3. Deploy the new configuration and test traffic flow to the new Gateway IP address.
  4. Switch over production traffic to Gateway API.
  5. Clean up remaining Ingress resources.



## Configure the new load balancer

In this phase, you deploy a Kubernetes Gateway resource to load balance traffic to your GKE cluster. When you deploy a Gateway resource, GKE configures a Layer 7 Application Load Balancer to expose HTTP(S) traffic to applications that run in the cluster. You deploy one Gateway resource for every cluster or for every load balancer that you require.

In the following example, you configure a Global external Application Load Balancer. To create a Gateway, save the following manifest as `gateway.yaml`:
    
    
    kind: Gateway
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: external-http-gateway
    spec:
      gatewayClassName: gke-l7-global-external-managed # GKE's managed external Application Load Balancer
      listeners:
      - name: http
        protocol: HTTP
        port: 80
        allowedRoutes:
          namespaces:
            from: Same # Only allow HTTPRoutes from the same namespace
    

The preceding manifest describes a Gateway that includes the following fields:

  * `gatewayClassName: gke-l7-global-external-managed`: specifies the GatewayClass for this Gateway. This Gateway class uses a global external Application Load Balancer.
  * `protocol: HTTP` and `port: 80`: specify that the Gateway exposes port 80 for HTTP traffic.



## Define traffic rules for incoming traffic

Route resources define protocol-specific rules for mapping traffic from a Gateway to backend Services.

In this phase, you translate your Ingress manifest into an HTTPRoute resource. To convert the Ingress manifest, follow the steps in the [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) tool.

This example assumes that you have the following Ingress resource:
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: cafe-ingress
    spec:
      ingressClassName: nginx
      rules:
      - host: cafe.example.com
        http:
          paths:
          - path: /tea
            pathType: Prefix
            backend:
              service:
                name: tea-svc
                port:
                  number: 80
          - path: /coffee
            pathType: Prefix
            backend:
              service:
                name: coffee-svc
                port:
                  number: 80
    

After you convert the manifest by using the `ingress2gateway` tool, the output is the translated HTTPRoute manifest.

Save the following sample manifest as `httproute.yaml`:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: cafe-route
    spec:
      # This route attaches to our new Gateway
      parentRefs:
      - name: external-http-gateway
      # The hostname is the same as before
      hostnames:
      - "cafe.example.com"
      # The routing rules are now more explicit
      rules:
      - matches:
        - path:
            type: PathPrefix
            value: /tea
        backendRefs:
        - name: tea-svc
          port: 80
      - matches:
        - path:
            type: PathPrefix
            value: /coffee
        backendRefs:
        - name: coffee-svc
          port: 80
    

Note that the `rules` field in the HTTPRoute manifest directly corresponds to the routing rules defined in the original Ingress manifest.

## Deploy and test the new configuration

In this phase, you apply the Gateway and HTTPRoute manifests that you created in the preceding two phases and test that traffic flows to the new IP address of the Gateway.

  1. Apply the Gateway and HTTPRoute manifests:
         
         kubectl apply -f gateway.yaml
         kubectl apply -f httproute.yaml
         

  2. Get the IP address of the Gateway. It might take a few minutes to allocate the IP address:
         
         kubectl get gateway external-http-gateway -o=jsonpath="{.status.addresses[0].value}" --watch
         

The output is the external IP address of the Gateway, for example, `203.0.113.90`.

  3. Test the new Gateway IP address. Use the following `curl` command to send a request to the IP address and specify the `cafe.example.com` hostname. For example:
         
         curl --resolve cafe.example.com:80:203.0.113.90 http://cafe.example.com/tea
         curl --resolve cafe.example.com:80:203.0.113.90 http://cafe.example.com/coffee
         

Replace `203.0.113.90` with the external IP address that you obtained from the preceding step. The output confirms that the new Gateway IP address correctly routes traffic for `cafe.example.com` without performing a DNS lookup.




## Direct traffic to the new Gateway IP address

In this phase, you cut over live traffic from your previous Ingress to the new Gateway by updating your DNS records to point to the new Gateway IP address. The exact steps to update DNS records vary depending on your DNS provider.

For example, if you configured `cafe.example.com` in Ingress, you would locate the `A` record for `cafe.example.com` with your DNS provider and change the value of the old Ingress IP address to `203.0.113.90`, which is the new Gateway IP address.

After you update the DNS record, traffic begins to shift from Ingress to Gateway, but the cutover does not occur immediately for all clients. DNS resolvers that have the previous record cached wait for the record's time to live (TTL) value to expire before they query for the record again and receive the updated IP address. Because of this, you should continue to run your existing Ingress and new Gateway in tandem until you verify that traffic to the Ingress has ceased, which indicates that DNS propagation is complete and clients are no longer being directed to the old IP address. You can verify this by monitoring traffic on your load balancer or Ingress controller. For more information, see [Checking DNS propagation](https://docs.cloud.google.com/dns/docs/monitoring#checking-propagation).

If you use Cloud DNS, you can use target weights to incrementally shift traffic from the old IP address to the new IP address. For more information, see [Configure DNS routing policies and health checks](https://docs.cloud.google.com/dns/docs/configure-routing-policies).

## Clean up remaining Ingress resources

After you confirm that your new Gateway runs successfully, clean up the old Ingress resources.

  1. Delete the Ingress resource:
         
         kubectl delete ingress cafe-ingress
         

  2. Uninstall the `ingress-nginx` controller. For example, if you used Helm to install the controller, run the following command:
         
         helm uninstall ingress-nginx -n ingress-nginx
         


**Note:** To secure the Gateway using either Google-managed certificates (recommended) or a Kubernetes Secret, see [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).

## Feature comparison between Ingress NGINX and GKE Gateway

Gateway API provides a more standardized way to configure ingress, and has feature parity for most common features like routing, headers, and traffic splitting.

The following table compares the configuration used for common features in the Ingress controller and Gateway API.

Feature | Annotation in Ingress | Configuration in GKE Gateway | Parity  
---|---|---|---  
Host-based routing | The `spec.rules.host` field in the Ingress object. | The `hostnames` field in the HTTPRoute object. | Full parity.  
Path-based routing | The `spec.rules.http.paths` field in the Ingress object. | The `rules.matches.path` field in the HTTPRoute object. | Full parity.  
Traffic splitting | `nginx.ingress.kubernetes.io/canary ` annotations. | HTTPRoute with the weighted `backendRefs` field. | Full parity. In addition, you can split traffic with fine-grained control.  
Session affinity | `nginx.ingress.kubernetes.io/affinity` and `nginx.ingress.kubernetes.io/affinity-mode` annotations. | GCPTrafficDistributionPolicy with the `sessionAffinity` field. | Full parity. GKE Gateway supports multiple session affinity types, including cookie-based affinity types (`HTTP_COOKIE`, `GENERATED_COOKIE`, and stateful `STRONG_COOKIE_AFFINITY`), header-based affinity (`HEADER_FIELD`), and client IP-based affinity (`CLIENT_IP`).  
CORS (Cross-Origin Resource Sharing) | `nginx.ingress.kubernetes.io/enable-cors` | HTTPRoute with a `CORS` filter. | Full parity. Note: GKE Gateway imposes limits on the number of wildcard patterns you can define per listener or hostname  
URL rewrites | `nginx.ingress.kubernetes.io/rewrite-target` | HTTPRoute with a `urlRewrite` filter. | Partial parity. GKE Gateway supports only prefix replacements.  
Header manipulation | `nginx.ingress.kubernetes.io/proxy-set-headers` or `add-headers` | HTTPRoute with a `requestHeaderModifier` modifier or `responseHeaderModifier` filter. | Full parity.  
Authentication | `nginx.ingress.kubernetes.io/auth-url` for external authentication. | 

  * Identity-Aware Proxy (IAP): GCPBackendPolicy custom resource.
  * Other: Requires a more custom approach, possibly with service mesh or custom filters.

| Partial parity. Identity-Aware Proxy is the recommended way to secure your Gateway and is configured on the backend.  
  
## What's next

  * Learn how to [secure your Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).
  * Read how [Gateway traffic management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management) works.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
