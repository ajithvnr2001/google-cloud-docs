---
url: https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy/
title: Security policies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:05.769300+00:00
---

# Security policies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains gateway security policies and how to create them.

## Gateway security policies

A gateway security policy acts as a centralized container for all security rules that govern traffic flow through your Secure Web Proxy instance. Policies let you effectively manage access control for the proxy's outbound web traffic.

You can define a policy and associate it with your Secure Web Proxy instance. This helps ensure that all outgoing web traffic from your network adheres to a consistent set of security standards.

Gateway security policies are based on the following three parameters:

  * **Traffic source** : Secure Web Proxy identifies the traffic source by using various attributes such as [service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts), [secure tags](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags), and [IP addresses](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic).

  * **Allowed destination** : Secure Web Proxy determine the allowed destinations by using a domain, a full URL path (if [TLS inspection is enabled](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection)), [URL lists](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list), or the destination port.

  * **Request details** : Secure Web Proxy evaluates request attributes such as the protocol, HTTP method, and request headers. To perform this analysis for encrypted traffic, you must [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).




### Source attributes

Secure Web Proxy policies identify the source of the traffic by using the following cloud identity and network location data:

  * [Service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts): unique identities that are assigned to your applications or workloads. Service accounts let you create policies based on an application's specific function.
  * [Secure tags](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags): labels that you can apply to your Google Cloud resources like virtual machine (VM) instances. Tags let you group workloads by function or environment. For example, "Allow all resources labeled `Production` to access approved domains."
  * [IP addresses](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic): network address of the sender. You can assign your enterprise or static Google Cloud IP addresses that Secure Web Proxy uses for outbound traffic.



#### Supported identities for source attributes

Secure Web Proxy uses source identity-based policies, such as service accounts and secure tags, to control web traffic. These policies let you apply rules based on the source identity of the traffic, rather than just the IP address.

The following table shows the Google Cloud services that support source identity-based policies:

Google Cloud services  | Service account support  | Secure tag support   
---|---|---  
[Compute Engine virtual machine (VM)](https://docs.cloud.google.com/compute/docs/overview) |  |   
[Google Kubernetes Engine (GKE) node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) |  |   
[Google Kubernetes Engine (GKE) container](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) | 1 | 1  
[Direct VPC for Cloud Run](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) |  | 1  
[Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) | 2 | 2  
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) | 1 | 1  
[Cloud Interconnect on premises](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) | 1 | 1  
[Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) |  |   
[Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer) |  |   
  
1 Not supported by Google Cloud.   
2 Source IP address is unique and can be used instead. 

The following table shows the Virtual Private Cloud (VPC) architectures that support source identity-based security policies:

VPC  | VPC architecture  | Support   
---|---|---  
Within VPC  | Cross project (Shared VPC)  |   
Cross VPC  | Cross peering link (peer VPC)  |   
Cross VPC  | Cross Private Service Connect  |   
Cross VPC  | Cross Network Connectivity Center spokes  |   
  
### Destination attributes

Secure Web Proxy policies determine whether a destination is approved by analyzing the following attributes of the target website or service:

  * **Destination domain** : the website address, such as `example.com`.

  * **URL lists** : predefined lists of approved or blocked URLs that simplify policy management.

  * **Destination port** : network port to which your Secure Web Proxy instance sends traffic. For example, `443` for HTTPS.

  * **Full URL path** : exact path of the website. You must enable TLS inspection to view the entire content on the specific web page.




For HTTP and HTTPS destination traffic, you can use the `host` destination attribute and various `request.*` destination-related attributes, like `request.method`, for your application.

For more information about the destination attributes that you can use for HTTP and HTTPS traffic, see [Attributes](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference#attributes).

## Create a security policy

Before creating a gateway security policy, make sure that you complete the following initial setup steps:

  * [Obtain Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#obtain-iam-roles-permissions)
  * [Create a Google Cloud project](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-project)
  * [Enable billing for your Google Cloud project](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#enable-billing)



After creating a policy, you can [create rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules#create-swp-rule) and add them to the policy. For more information about how to associate a policy with your Secure Web Proxy instance, see [Set up a web proxy](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-a-gateway).

### Console

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click add_box**Create a policy**.

  3. Enter a name for the policy that you want to create, such as `policy1`.

  4. Enter a description of the policy, such as `My new swp policy`.

  5. In the **Regions** list, select the region where you want to create the policy, such as `us-central1`.

  6. If you want to create rules for your policy, then click **Add rule**. For more information, see [Create a Secure Web Proxy rule](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules#create-swp-rule).

  7. Click **Create**.


**Important:** To create a policy with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

###  Cloud Shell 

  1. Use your preferred text editor to create a `policy.yaml` file.

  2. Add the following to the `policy.yaml` file that you created:
         
         description: basic Secure Web Proxy policy
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         

Replace the following:

     * `PROJECT_ID`: ID of your project
     * `REGION`: region where your policy is created, such as `us-central1`
**Important:** To create a policy with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).
  3. Create the Secure Web Proxy policy.
         
         gcloud network-security gateway-security-policies import policy1 \
             --source=policy.yaml \
             --location=REGION
         




## What's next

  * [Security rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules)
  * [Deploy Secure Web Proxy as a Private Service Connect service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)
  * [Deploy Secure Web Proxy as next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
