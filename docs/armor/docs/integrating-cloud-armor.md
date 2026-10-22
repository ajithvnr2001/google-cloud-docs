---
url: https://docs.cloud.google.com/armor/docs/integrating-cloud-armor/
title: Integrate with other Google products \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:25.407351+00:00
---

# Integrate with other Google products  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/integrating-cloud-armor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Integrate with other Google products Stay organized with collections  Save and categorize content based on your preferences. 

To help protect your services and applications from denial-of-service (DoS) and web attacks, you can integrate Google Cloud Armor with other Google Cloud products. This document explains how Cloud Armor interacts with VPC firewall rules, Identity-Aware Proxy (IAP), Google Kubernetes Engine (GKE), Cloud CDN, and Global Front End.

## Cloud Armor and VPC firewall rules

Cloud Armor security policies and [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) have different functions:

  * Cloud Armor security policies provide edge security and act on client traffic to Google Front Ends (GFEs).
  * VPC firewall rules allow or deny traffic to and from your backends. You must create ingress allow firewall rules, whose targets are the load-balanced backend VMs, and whose sources are [IP ranges used by global external Application Load Balancers or classic Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https#firewall_rules). These rules allow GFEs and the health check systems to communicate with your backend VMs.



For example, consider a scenario in which you want to allow traffic only from CIDR range 100.1.1.0/24 and CIDR range 100.1.2.0/24 to access your global external Application Load Balancer or classic Application Load Balancer. Your goal is to block traffic from directly reaching the backend load balanced instances. In other words, only external traffic proxied through the global external Application Load Balancer or the classic Application Load Balancer with an associated security policy can reach the instances.

[ ![Using Cloud Armor security policy with ingress firewalls
       to restrict access.](https://docs.cloud.google.com/static/armor/images/ip-bl-wl-5.svg)](https://docs.cloud.google.com/static/armor/images/ip-bl-wl-5.svg) Using Cloud Armor security policy with ingress firewalls to restrict access (click to enlarge).

The previous diagram shows the following deployment configuration:

  1. Create two instance groups, one in the `us-west1` region and another in the `europe-west1` region.
  2. Deploy backend application instances to the VMs in the instance groups.
  3. Create a global external Application Load Balancer or a classic Application Load Balancer in Premium Tier. Configure a URL map and a single backend service whose backends are the two instance groups that you created in the previous step. The load balancer's forwarding rule must use the `120.1.1.1` external IP address.
  4. Configure a Cloud Armor security policy that allows traffic from 100.1.1.0/24 and 100.1.2.0/24 and denies all other traffic.
  5. Associate this policy with the load balancer's backend service. For instructions, see [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies). External HTTP(S) load balancers with more complex URL maps can reference multiple backend services. You can associate the security policy with one or more of the backend services as needed.
  6. Configure ingress allow firewall rules to permit traffic from the global external Application Load Balancer or the classic Application Load Balancer. For more information, see [Firewall rules](https://docs.cloud.google.com/load-balancing/docs/https#firewall-rules).



## Cloud Armor with external Application Load Balancers and IAP

IAP verifies a user's identity and then determines whether that user can access an application. To enable IAP for the global external Application Load Balancer or the classic Application Load Balancer, use the load balancer backend services. Similarly, edge Cloud Armor security policies are attached to the backend services of a global external Application Load Balancer or a classic Application Load Balancer.

If Cloud Armor security policies and IAP are both enabled for a backend service, the order of their evaluation depends on the type of the load balancer:

  * For a backend service of a global external Application Load Balancer, Cloud Armor evaluation happens first. If Cloud Armor blocks a request, IAP doesn't evaluate the request. If Cloud Armor allows a request, IAP then evaluates the request. The request is blocked if IAP doesn't authenticate the request.

  * For a backend service of a classic Application Load Balancer, IAP evaluation happens first. If IAP authenticates a request, then Cloud Armor evaluates the request. If a request fails IAP authentication, then Cloud Armor doesn't evaluate the request.


[ ![Using IP address denylists and allowlists with IAP.](https://docs.cloud.google.com/static/armor/images/ip-bl-wl-6.svg)](https://docs.cloud.google.com/static/armor/images/ip-bl-wl-6.svg) Using IP address denylists and allowlists with IAP (click to enlarge).

For more information about IAP and related configurations, see the [Identity-Aware Proxy](https://docs.cloud.google.com/iap) documentation. 

## Cloud Armor with hybrid deployments

In a hybrid deployment, a global external Application Load Balancer or a classic Application Load Balancer needs access to an application or content source that runs outside Google Cloud—for example, in another cloud provider's infrastructure. You can use Cloud Armor to help protect such deployments.

In the following diagram, the load balancer has two backend services. One has an instance group as its backend. The other backend service has an internet NEG as its backend, and the internet NEG is associated with an application that is running in a third-party provider's data center.

[ ![Cloud Armor for hybrid deployments.](https://docs.cloud.google.com/static/armor/images/ca-hybrid.svg)](https://docs.cloud.google.com/static/armor/images/ca-hybrid.svg) Cloud Armor for hybrid deployments (click to enlarge).

When you attach a Cloud Armor security policy to the backend service that has an internet NEG as the backend, Cloud Armor inspects every Layer 7 request that arrives at the global external Application Load Balancer or classic Application Load Balancer that is destined for that backend service.

Cloud Armor protection for hybrid deployments is subject to the same [limitations that apply to internet NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#limitations). 

## Cloud Armor with GKE

The following sections describe how Cloud Armor works with GKE.

### GKE Ingress

After you configure a Cloud Armor security policy, you can use [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to enable it with GKE.

You can reference your security policy with a `BackendConfig` resource by adding the name of your security policy to the `BackendConfig`. The following `BackendConfig` manifest specifies a security policy named `example-security-policy`:
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      namespace: cloud-armor-how-to
      name: my-backendconfig
    spec:
      securityPolicy:
        name: "example-security-policy"
    

For more information about Ingress features, see [Ingress configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).

### GKE Gateway

After you configure a Cloud Armor security policy, you can use the [Kubernetes Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) to enable it with GKE.

You can reference your security policy by adding the name of your security policy to a `GCPBackendPolicy` policy resource. The following `GCPBackendPolicy` policy resource manifest specifies a backend security policy named `example-security-policy`:

### Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        securityPolicy: example-security-policy
      targetRef:
        group: ""
        kind: Service
        name: lb-service
    

### Multi-cluster Service
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: my-backend-policy
      namespace: lb-service-namespace
    spec:
      default:
        securityPolicy: example-security-policy
      targetRef:
        group: net.gke.io
        kind: ServiceImport
        name: lb-service
    

For more information about configuring Cloud Armor backend security policies, see [Configure Cloud Armor backend security policy to help secure your backend services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor). 

## Cloud Armor with Cloud CDN

To help protect CDN origin servers, you can use Cloud Armor with Cloud CDN. Cloud Armor helps protect your CDN origin server from application attacks, mitigates OWASP Top 10 risks, and enforces Layer 7 filtering policies. There are two types of security policies that affect how Cloud Armor works with Cloud CDN: edge security policies and backend security policies.

### Edge security policies

You can use edge security policies for Cloud CDN-enabled backend services and Cloud Storage backend buckets behind the global external Application Load Balancer or the classic Application Load Balancer. Use edge security policies to filter requests before content is served from cache.

### Backend security policies

When Cloud Armor backend security policies are applied to backend services with Cloud CDN enabled, they apply only to requests routed to the backend service. These requests include dynamic content requests and cache misses—that is, requests that miss or bypass the Cloud CDN cache.

When edge security policies and backend security policies are attached to the same backend service, backend security policies are enforced only for cache miss requests that have passed edge security policies.

The following diagram shows exclusively how backend security policies work with Cloud CDN origins, after the requests have been allowed by the edge security policies.

[ ![Using Cloud Armor backend security policies with Cloud CDN.](https://docs.cloud.google.com/static/armor/images/ca-cdn-origins.svg)](https://docs.cloud.google.com/static/armor/images/ca-cdn-origins.svg) Using Cloud Armor backend security policies with Cloud CDN (click to enlarge).

For more information about Cloud CDN, see the [Cloud CDN documentation](https://docs.cloud.google.com/cdn/docs). 

## Cloud Armor with Cloud Run, App Engine, or Cloud Run functions

You can use Cloud Armor security policies with a serverless NEG backend that points to a [Cloud Run](https://docs.cloud.google.com/run/docs), [App Engine](https://docs.cloud.google.com/appengine/docs), or [Cloud Run functions](https://docs.cloud.google.com/functions/docs) service.

However, when you use Cloud Armor with serverless NEGs, Cloud Run, or Cloud Run functions, all access to the serverless endpoint must be filtered through a Cloud Armor security policy.

Users who have the default URL for a serverless application can bypass the load balancer and go directly to the service URL. This bypasses Cloud Armor security policies. To address this, [disable the default URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) that Google Cloud automatically assigns to Cloud Run services or Cloud Run functions (2nd gen) functions. To help protect App Engine applications, you can use [ingress controls](https://docs.cloud.google.com/appengine/docs/standard/go/application-security#ingress_controls).

If you're using ingress controls to apply your access controls to all incoming traffic, you can use the `internal-and-gclb` ingress setting when you configure [Cloud Run functions](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) or [Cloud Run](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy). The `internal-and-gclb` ingress setting allows only internal traffic and traffic sent to an external IP address exposed by the global external Application Load Balancer or the classic Application Load Balancer. Traffic that is sent to these default URLs _from outside of your private network_ is blocked. This helps prevent users from circumventing any access controls (such as Cloud Armor security policies) set up through the global external Application Load Balancer or classic Application Load Balancer.

For more information about serverless NEGs, see [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) and [Setting up serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs).

## Cloud Armor with Cloud Service Mesh

**Note:** The `fairshare` rate limiting action is only available for rules in internal service security policies.

You can configure internal service security policies for your service mesh to enforce global server-side rate limiting per client, helping you fairly share your service's available capacity and mitigating the risk of malicious or misbehaving clients overloading your services. You attach a security policy to a Cloud Service Mesh endpoint policy to enforce rate limiting on inbound traffic on the server-side. However, you can't configure a Cloud Armor security policy if you are using TCP traffic routing. For more information about using Cloud Armor with Cloud Service Mesh, see [Configure rate limiting with Cloud Armor](https://docs.cloud.google.com/service-mesh/docs/service-routing/rate-limiting-overview).

## Cloud Armor and service rate limiting

Service rate limiting manages trusted but potentially misbehaving clients on an internal Application Load Balancer and a Secure Web Proxy to maximize service availability for your most important traffic.

For more information, see [Service rate limiting overview](https://docs.cloud.google.com/load-balancing/docs/srl-policy/service-rate-limiting-overview).

## Cloud Armor and Global Front End

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Global Front End](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#global-front-end) combines Cloud Armor, [global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer), [ Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview), and [ Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) into one solution to help deliver, scale, and secure your internet-facing applications. With the Global Front End Enterprise billing tier, pricing for these products is consolidated under a [single pricing plan](https://docs.cloud.google.com/vpc/network-pricing?e=48754805#global-front-end-enterprise).

You can [enable the Global Front End Enterprise billing tier in your Google Cloud project](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-manage). For more information, go to the [Global Front End](https://console.cloud.google.com/net-services/global-front-end/overview) page on the Google Cloud console.

## What's next

  * [Create and view security policies, rules, and expressions](https://docs.cloud.google.com/armor/docs/configure-security-policies)
  * [Learn about the features in Cloud Armor Enterprise tiers](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
