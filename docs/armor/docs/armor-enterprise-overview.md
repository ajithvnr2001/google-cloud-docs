---
url: https://docs.cloud.google.com/armor/docs/armor-enterprise-overview/
title: Cloud Armor Enterprise overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:58.667089+00:00
---

# Cloud Armor Enterprise overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/armor-enterprise-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Cloud Armor Enterprise overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor Enterprise is the application protection service that helps protect your web applications and services from distributed denial-of-service (DDoS) attacks and other threats from the internet. Cloud Armor Enterprise helps protect applications deployed on Google Cloud, on-premises, or on other infrastructure providers.

## Google Cloud Armor Standard versus Cloud Armor Enterprise

**Note:** If you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project), both the frontend and backend service projects must be under the same billing account that is associated with the Cloud Armor Enterprise subscription and enrolled in Cloud Armor Enterprise.

Cloud Armor is offered in two service tiers, Standard and Cloud Armor Enterprise.

**Cloud Armor Standard** includes the following:

  * A pay-as-you go pricing model
  * Always-on protection from Layer 3 and Layer 4 (L3 and L4) volumetric and network protocol-based DDoS attacks. 
  * Automated application of your security policies against every request, in real time and with no latency impact across the following infrastructure types:

    * Global external Application Load Balancer (HTTP/HTTPS)
    * Classic Application Load Balancer (HTTP/HTTPS)
    * Regional external Application Load Balancer (HTTP/HTTPS)
    * Regional external passthrough Network Load Balancer
    * Global external proxy Network Load Balancer (TCP/SSL)
    * Cloud CDN
    * Media CDN
**Note:** Cloud Armor gives you additional access to protection from Layer 7 (Application layer) DDoS attacks, such as HTTP Floods, through user-configured security policies with proactive rules in place (See [Best Practices](https://docs.cloud.google.com/armor/docs/best-practices)).
  * Integration with Cloud CDN and Media CDN

  * Access to Cloud Armor web application firewall (WAF) rule capabilities, including [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) for OWASP Top 10 protection 

  * Optional add-on: [Cloud Armor managed rules](https://docs.cloud.google.com/armor/docs/managed-rules-overview) for automatically updated threat detection signatures 




**Cloud Armor Enterprise** includes the following:

  * All the features of Cloud Armor Standard
  * Choice of pricing models: [Cloud Armor Enterprise Annual or Paygo](https://cloud.google.com/armor/pricing)
  * Bundled Cloud Armor WAF usage, including rules, policy, and requests
  * [Third-party named IP address lists](https://docs.cloud.google.com/armor/docs/threat-intelligence#use-named-ip)
  * [Google Threat Intelligence for Cloud Armor](https://docs.cloud.google.com/armor/docs/threat-intelligence)
  * [Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) for Layer 7 endpoints
  * Advanced network DDoS protection for pass-through endpoints—regional external passthrough Network Load Balancers, protocol forwarding, and public IP addresses for virtual machine (VM) instances
  * Access to [DDoS attack visibility](https://docs.cloud.google.com/armor/docs/ddos-visibility)
  * [Hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview)
  * (Cloud Armor Enterprise Annual only): Access to DDoS bill protection and DDoS response team services (additional conditions apply, see Eligibility for DDoS response team) 
  * Optional add-on: [Cloud Armor managed rules](https://docs.cloud.google.com/armor/docs/managed-rules-overview) for automatically updated threat detection signatures 



All Google Cloud projects that include an external Application Load Balancer or an external proxy Network Load Balancer are automatically enrolled in Cloud Armor Standard. After subscribing to Cloud Armor Enterprise at the billing account level, users can choose to enroll individual projects attached to the billing account in Cloud Armor Enterprise.

The following table summarizes the service tiers.

| Cloud Armor Standard | Cloud Armor Enterprise  
---|---|---  
Paygo | Annual  
Billing method | Pay-as-you-go | Pay-as-you-go | Subscription with 12-month commitment  
Pricing | Per policy, per rule, per request (see [Pricing](https://docs.cloud.google.com/armor/pricing)) | 

  * $200/month per project
  * $200/month per protected resource after first 2 resources

| 

  * $3000/month per billing account
  * $30/month per protected resource after first 100 resources

  
DDoS attack protection | 

  * External Application Load Balancer
  * External proxy Network Load Balancer

| 

  * External Application Load Balancer
  * External proxy Network Load Balancer
  * Regional external passthrough Network Load Balancer
  * Protocol forwarding
  * Public IP addresses (VMs)

| 

  * External Application Load Balancer
  * External proxy Network Load Balancer
  * Regional external passthrough Network Load Balancer
  * Protocol forwarding
  * Public IP addresses (VMs)

  
Managed rules | Optional add-on (see [Pricing](https://docs.cloud.google.com/armor/pricing)) | Optional add-on (see [Pricing](https://docs.cloud.google.com/armor/pricing)) | Optional add-on (see [Pricing](https://docs.cloud.google.com/armor/pricing))  
Cloud Armor WAF | Per policy, per rule, per request (see [Pricing](https://docs.cloud.google.com/armor/pricing)) | Included with Paygo | Included with Annual  
Resource limits | Up to quota limit | Up to quota limit | Up to quota limit  
Time commitment |  |  | One year  
Adaptive Protection | Alerting only |  |   
Advanced network DDoS protection |  |  |   
Network edge security policies |  |  |   
Address Group |  |  |   
Google Threat Intelligence |  |  |   
Hierarchical security policies |  |  |   
DDoS attack visibility |  |  |   
DDoS response support |  |  | Eligibility requirements  
DDoS bill protection |  |  |   
**Note:** Customers who subscribed to Cloud Armor Enterprise after September 3, 2024 aren't eligible for DDoS Response Support until they have successfully completed a DDoS posture review. To schedule your review, [open a support ticket](https://docs.cloud.google.com/armor/docs/getting-support#posture-review).

## Global Front End

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Global Front End](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview) combines Cloud Armor, [global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer), [ Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview), and [ Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) into one solution to help deliver, scale, and secure your internet-facing applications. With the [ Global Front End Enterprise](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview#global-front-end-enterprise) billing tier, pricing for these products is consolidated under a [single pricing plan](https://docs.cloud.google.com/vpc/network-pricing?e=48754805#global-front-end-enterprise).

**Note:** You can [enable the Global Front End Enterprise billing tier in your Google Cloud project](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-manage). For more information, go to the [Global Front End](https://console.cloud.google.com/net-services/global-front-end/overview) page on the Google Cloud console.

Enabling Global Front End Enterprise in a project enables specific Cloud Armor Enterprise features for your global external Application Load Balancer, but doesn't change the Cloud Armor tier at the project level. Resources other than global external Application Load Balancers (such as internal load balancers or regional load balancers) within the same project continue under their current Cloud Armor pricing tiers (Cloud Armor Standard or Cloud Armor Enterprise). When you disable Global Front End Enterprise, active Cloud Armor protections are determined by the project-level tier. The Google Cloud console does not restore a previous tier automatically. You must immediately and manually designate a Cloud Armor billing tier (either Cloud Armor Standard or Cloud Armor Enterprise PayGo) to avoid security policy degradation or unexpected billing changes.

The following table summarizes how enabling Global Front End Enterprise affects resources depending on the project's Cloud Armor tier.

Resource type | Project tier: Cloud Armor Standard | Project tier: Cloud Armor Enterprise (Paygo or Annual)  
---|---|---  
**Global external Application Load Balancers** |  Enables specific Cloud Armor Enterprise features with consolidated billing: 

  * Cloud Armor preconfigured WAF rules
  * Adaptive Protection
  * Google Threat Intelligence
  * DDoS attack visibility
  * Address Groups

| Enables all Cloud Armor Enterprise features with consolidated billing  
**All other resources** (for example, regional external Application Load Balancers or internal load balancers) | Unaffected (Cloud Armor Standard features and pricing) | Unaffected (Cloud Armor Enterprise features and pricing)  
  
## Subscribe to Cloud Armor Enterprise

Subscribing to Cloud Armor Enterprise Annual requires a one-year (12-month) commitment. Only users with the billing account role and permissions can subscribe the billing account to Cloud Armor Enterprise Annual. Alternatively, you can enroll in Cloud Armor Enterprise Paygo with no commitment.

To use the additional services and capabilities in Cloud Armor Enterprise, you must first enroll in Cloud Armor Enterprise. You can subscribe to Cloud Armor Enterprise Annual and enroll individual projects, or you can enroll a project directly in Cloud Armor Enterprise Paygo.

We recommend that you enroll your projects in Cloud Armor Enterprise as soon as possible because activation can take up to one hour. Upgrading from Cloud Armor Standard to Enterprise typically won't disrupt your application's availability. However, when you make changes to your security policies you must carefully consider the billing implications.

**Note:** If you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project), both the frontend and backend service projects must be under the same billing account that is associated with the Cloud Armor Enterprise subscription and enrolled in Cloud Armor Enterprise.

### External Application Load Balancer and external proxy Network Load Balancer

After a project is enrolled in Cloud Armor Enterprise, the forwarding rules within the project are added to the enrollment. In addition, all backend services and backend buckets are counted as protected resources and are metered for the Cloud Armor Enterprise protected resources cost. The backend services and backend buckets in Cloud Armor Enterprise Annual are aggregated across all enrolled projects in a billing account, whereas the backend services and backend buckets in Cloud Armor Enterprise Paygo are aggregated within the project.

**Note:** Regional internal Application Load Balancer backends are counted as protected resources only if a security policy is attached.

_Always-on_ protection for forwarding rules, backend services, and backend buckets includes mitigation from L3 and L4 volumetric and network protocol-based DDoS attacks. Protection from application layer threats including L7 DDoS requires a user-created security policy with mitigating rules in place.

**Note:** For projects enrolled in Cloud Armor Enterprise, resources—such as regional external passthrough Network Load Balancer backend services, target pools, target instances, and VM instances with public IP addresses—are metered as _protected resources_ only when advanced network DDoS protection has been enabled for the region where the resources are located.

### Hierarchical security policies

When you attach a hierarchical security policy, each of the projects that inherit the hierarchical security policy must be enrolled in Cloud Armor Enterprise. This includes all of the projects in an organization or folder with a hierarchical security policy that aren't explicitly excluded, and all projects with a hierarchical security policy attached directly to the project.

  * Projects that are linked to a Cloud Billing account with a subscription to Cloud Armor Enterprise Annual are automatically enrolled in Cloud Armor Enterprise Annual if they aren't already enrolled.
  * Without a Cloud Armor Enterprise Annual subscription, projects are automatically enrolled in Cloud Armor Enterprise Paygo when they inherit a hierarchical security policy. If you subscribe the billing account to Cloud Armor Enterprise Annual after your project was automatically enrolled in Cloud Armor Enterprise Paygo, the project isn't automatically enrolled to Annual. For more information about Cloud Armor Enterprise Paygo, see [Cloud Armor Standard versus Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#standard_versus).
  * If you update a hierarchical security policy to exclude a project _after_ the project has been automatically enrolled in Cloud Armor Enterprise, the project isn't automatically unenrolled. To manually unenroll your project, see [Remove a project from Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#remove-project).
  * You can't remove a project from Cloud Armor Enterprise while it has any inherited hierarchical security policies.



Auto-enrollment can take up to the next business day to complete. During this time, your hierarchical security policies are effective and no Cloud Armor Enterprise costs are incurred. When your project is enrolled, audit logs are updated to reflect the project's Cloud Armor Enterprise status. You also see the new project tier in the Google Cloud console.

Projects are auto-enrolled only when at least one backend service for global external load balancers uses HTTP, HTTPS, HTTP2, H2C, or GRPC.

For more information about hierarchical security policies, see the [hierarchical security policies overview](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview).

## DDoS response support

**Note:** Customers who subscribed to Cloud Armor Enterprise after September 3, 2024 aren't eligible for DDoS Response Support until they have successfully completed a DDoS posture review. To schedule your review, [open a support ticket](https://docs.cloud.google.com/armor/docs/getting-support#posture-review).

DDoS Response support provides 24/7 help and potential custom mitigations from DDoS attacks from the same team that protects all Google services. You can engage response support during an attack to help mitigate the attack, or you can reach out proactively to plan for an upcoming high volume or potentially viral event (one which might attract an unusually high amount of visitors).

Proactive support is available for all Cloud Armor Enterprise customers, even if they haven't completed a DDoS posture review. Proactive support lets us apply preconfigured rules that target common DDoS attack types before the attack reaches Cloud Armor. To engage DDoS response support, see [Get support for a DDoS case](https://docs.cloud.google.com/armor/docs/getting-support#ddos-case).

### DDoS posture review

The goal of the DDoS posture review is to improve the efficiency and efficacy of the DDoS response process. During the review process we learn about your unique use case and architecture, and verify that your Cloud Armor security policies are configured according to our [best practices](https://docs.cloud.google.com/armor/docs/best-practices). This helps you increase your preemptive resilience to DDoS attacks.

The DDoS posture review is provided to customers who subscribe to Cloud Armor Enterprise Annual and have a [Premium account](https://docs.cloud.google.com/support/docs/premium) for Cloud Customer Care.

### Eligibility for DDoS response support

The following criteria qualify you to open a case and receive help from the Cloud Armor DDoS response support team:

  * Your billing account has an active Cloud Armor Enterprise Annual subscription.
  * Your billing account has a [Premium account](https://docs.cloud.google.com/support/docs/premium) for Cloud Customer Care.
  * The Google Cloud project with the workload that's under attack is enrolled in Cloud Armor Enterprise Annual. 
    * If you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project), both the frontend and backend service projects must be enrolled in Cloud Armor Enterprise Annual.
  * For customers who subscribed to Cloud Armor Enterprise Annual _after_ September 3, 2024: The project with the workload that is under attack must have undergone an annual DDoS posture review.



Even when customers don't qualify for support, our Cloud Customer Care team provides assistance during an attack by helping with rule debugging, behavior clarification, and specific concerns with existing policies.

To engage DDoS response support, see [Get support for a DDoS case](https://docs.cloud.google.com/armor/docs/getting-support#ddos-case).

## DDoS bill protection

Cloud Armor DDoS bill protection requires your project to be enrolled in Cloud Armor Enterprise Annual. It provides credits for future Google Cloud usage for some increases in the bills from Cloud Load Balancing, Cloud Armor, and network internet, inter-region, and inter-zone outbound data transfer as a result of a verified DDoS attack. If a claim is recognized and a credit is provided, the credit cannot be used to offset existing usage; the credit can only apply to future usage. The following table demonstrates what resources are covered by DDoS bill protection:

Endpoint Type | Covered Usage Increase |   
---|---|---  
  
  * External Application Load Balancer
  * External proxy Network Load Balancer

| Cloud Armor | Cloud Armor Enterprise data processing fee  
Network | Outbound data transfer  
Inter-region  
Inter-zone  
Carrier Peering  
Load balancer | Inbound data processing fee  
[Outbound data processing fee](https://docs.cloud.google.com/vpc/network-pricing#lb)  
Cloud CDN | Cloud CDN egress fee  
Cache data transfer out  
Cache fill  
HTTP/HTTPS cache lookup requests  
Media CDN | Media CDN egress fee  
Cache data transfer out  
  
  * Regional external passthrough Network Load Balancer
  * Protocol forwarding
  * Public IP addresses (VMs)

| Cloud Armor | Cloud Armor Enterprise data processing fee  
Network | Outbound data transfer  
Inter-region  
Inter-zone  
Carrier Peering  
Load balancer | Inbound data processing fee  
[Outbound data processing fee](https://docs.cloud.google.com/vpc/network-pricing#lb)  
  
To engage DDoS bill protection, see [Engaging DDoS bill protection](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#ddos-bill-protection).

## Migrating projects between billing accounts

Beginning September 3, 2024, if you migrate your project from one billing account to another while subscribed to Cloud Armor Enterprise Annual, but your new billing account isn't subscribed to Cloud Armor Enterprise Annual, your project reverts to Cloud Armor Standard after the migration completes—unless your project has effective hierarchical security policies, in which case your project is downgraded to Cloud Armor Enterprise Paygo. Therefore, if you want to keep your project in Cloud Armor Enterprise Annual without downtime, we recommend that you subscribe your new billing account to Cloud Armor Enterprise Annual _before_ you begin the migration process. You can also migrate your subscription from one billing account to the other by reaching out to [Cloud Billing support](https://docs.cloud.google.com/support/billing).

Projects enrolled in Cloud Armor Enterprise Paygo are not affected by billing account migration.

## Downgrading from Cloud Armor Enterprise

**Note:** You can't downgrade from Cloud Armor Enterprise while you have hierarchical security policies. To delete a hierarchical security policy, see [Delete a hierarchical security policy](https://docs.cloud.google.com/armor/docs/hierarchical-policies-using#delete-policy).

When you [remove a project from Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#remove-project), any security policies that use rules with Cloud Armor Enterprise-exclusive features (advanced rules) become frozen. Frozen security policies have the following properties:

  * Cloud Armor continues to evaluate traffic against rules in the policy, including any advanced rules.
  * You cannot attach the security policy to new targets.
  * You can only perform the following operations on the security policy: 
    * You can [delete security policy rules](https://docs.cloud.google.com/armor/docs/manage-security-policies#delete-rules).
    * If you don't change the rule priority, you can update advanced rules so that they no longer use Cloud Armor Enterprise-exclusive features. If you modify all advanced rules in this way, your policy is no longer frozen. For more information about updating security policy rules, see [Update a single rule in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policies#update-rules).



You can also re-enroll in Cloud Armor Enterprise Annual or Cloud Armor Enterprise Paygo to restore access to your frozen security policies.

### Disabling Global Front End Enterprise

When you disable Global Front End Enterprise in a project:

  * Active Cloud Armor protections revert to the tier active at the project level.
  * The Google Cloud console does not automatically restore a previous tier or designate a fallback tier.
  * To avoid security policy degradation or unexpected billing, you must manually and immediately select a Cloud Armor billing tier (either Cloud Armor Standard or Cloud Armor Enterprise PayGo).



### Advanced network DDoS protection

Advanced network DDoS protection is only available to projects enrolled in Cloud Armor Enterprise. When you remove a project with an active advanced network DDoS policy from Cloud Armor Enterprise, you are still billed for the feature based on [Cloud Armor Enterprise pricing](https://cloud.google.com/armor/pricing#google-cloud-armor-pricing).

We recommend that you delete any advanced network DDoS protection rules before you unenroll your project from Cloud Armor Enterprise, but you can also delete advanced network DDoS protection rules after downgrading.

## Terms and limitations

Cloud Armor Enterprise has the following terms and limitations:

  * **Generally** : If a Project enrolled in Cloud Armor Enterprise experiences a third-party denial of service attack on a protected endpoint ("Qualified Attack") and the conditions described in the next section are met, Google provides a credit equivalent to the Covered Fees, provided that the Covered Fees incurred exceed the Minimum Threshold. Load tests and security assessments performed by or on behalf of Customer are not Qualified Attacks.
  * **Conditions** : Customer must submit a request to Cloud Billing Support within 30 days after the end of the Qualified Attack. The request must include evidence of the Qualified Attack, such as logs or other telemetry indicating the timing of the attack and the Projects and resources that were attacked, and an estimate of the Covered Fees incurred. Google will reasonably determine whether credits are due and the appropriate amount. Other conditions for particular Cloud Armor features are included in the Documentation.
  * **Credits** : Any credits provided to Customer in connection with this Section have no cash value and can only be applied to offset future Fees for the Services. These credits expire 12 months after being issued or upon termination or expiration of the Agreement.
  * **Definitions** : 
    * **Covered Fees** : Any Fees incurred by Customer as a direct result of the Qualified Attack for the following: 
      * Ingress and outbound data processing for the Google Cloud Load Balancer Service.
      * Cloud Armor Enterprise data processing for the Cloud Armor Service.
      * Network egress, including inter-region, inter-zone, internet, and Carrier Peering egress.
    * **Minimum Threshold** : The minimum amount of Covered Fees that are eligible to be credited under this Section as determined by Google from time to time and disclosed to Customer on request.



## What's next

  * [Subscribe and enroll projects in Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Use the custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
