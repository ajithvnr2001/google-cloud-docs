---
url: https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust/
title: Implement zero trust \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:25.367128+00:00
---

# Implement zero trust  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement zero trust Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-05 UTC

This principle in the security pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) helps you ensure comprehensive security across your cloud workloads. The principle of zero trust emphasizes the following practices:

  * Eliminating implicit trust
  * Applying the principle of least privilege to access control
  * Enforcing explicit validation of all access requests
  * Adopting an _assume-breach_ mindset to enable continuous verification and security posture monitoring



## Principle overview

The _zero-trust_ model shifts the security focus from perimeter-based security to an approach where no user or device is considered to be inherently trustworthy. Instead, every access request must be verified, regardless of its origin. This approach involves authenticating and authorizing every user and device, validating their context (location and device posture), and granting least privilege access to only the necessary resources.

Implementing the zero-trust model helps your organization enhance its security posture by minimizing the impact of potential breaches and protecting sensitive data and applications against unauthorized access. The zero-trust model helps you ensure confidentiality, integrity, and availability of data and resources in the cloud.

## Recommendations

To implement the zero-trust model for your cloud workloads, consider the recommendations in the following sections:

  * Secure your network
  * Verify every access attempt explicitly
  * Monitor and maintain your network



### Secure your network

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Infrastructure security.

Transitioning from conventional perimeter-based security to a zero-trust model requires multiple steps. Your organization might have already integrated certain zero-trust controls into its security posture. However, a zero-trust model isn't a singular product or solution. Instead, it's a holistic integration of multiple security layers and best practices. This section describes recommendations and techniques to implement zero trust for network security.

  * **Access control** : Enforce access controls based on user identity and context by using solutions like [Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/) and [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview). By doing this, you shift security from the network perimeter to individual users and devices. This approach enables granular access control and reduces the attack surface.
  * **Network security** : Secure network connections between your on-premises, Google Cloud, and multicloud environments. 
    * Use the private connectivity methods from [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [IPsec VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
    * To help secure access to Google Cloud services and APIs, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
    * To help secure outbound access from workloads deployed on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and related products, use [Cloud Service Mesh egress gateways](https://docs.cloud.google.com/service-mesh/docs/security/egress-gateways-best-practices).
  * **Network design** : Prevent potential security risks by deleting default networks in existing projects and disabling the creation of default networks in new projects. 
    * To avoid conflicts, plan your network and IP address allocation carefully.
    * To enforce effective access control, limit the number of Virtual Private Cloud (VPC) networks per project.
  * **Segmentation** : Isolate workloads but maintain centralized network management. 
    * To segment your network environments, use multiple VPC networks and define firewall policies and rules at the organization, folder, and VPC network levels.
    * To centralize network administration for resources that are in separate projects, use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). For example, administrators of a service project can create Compute Engine instances that use approved subnets from the project that hosts a centrally administered Shared VPC network.
    * To prevent [data exfiltration](https://en.wikipedia.org/wiki/Data_exfiltration), establish secure perimeters around sensitive Google Cloud APIs and services by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), and use strict egress firewall rules to restrict internet-bound traffic.
  * **Perimeter security** : Protect against DDoS attacks and web application threats. 
    * To protect against threats, use [Google Cloud Armor](https://docs.cloud.google.com/armor/docs).
    * Configure security policies to allow, deny, or redirect traffic at the Google Cloud edge.
  * **Automation** : Automate infrastructure provisioning by embracing infrastructure as code (IaC) principles and by using tools like Terraform, Jenkins, and [Cloud Build](https://docs.cloud.google.com/build/docs/overview). IaC helps to ensure consistent security configurations, simplified deployments, and rapid rollbacks in case of issues.
  * **Secure foundation** : Establish a secure application environment by using the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). This blueprint provides prescriptive guidance and automation scripts to help you implement security best practices and configure your Google Cloud resources securely.



### Verify every access attempt explicitly

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Identity and access management
  * Security operations (SecOps)
  * Logging, auditing, and monitoring



Implement strong authentication and authorization mechanisms for any user, device, or service that attempts to access your cloud resources. Don't rely on location or network perimeter as a security control. Don't automatically trust any user, device, or service, even if they are already inside the network. Instead, every attempt to access resources must be rigorously authenticated and authorized. You must implement strong identity verification measures, such as multi-factor authentication (MFA). You must also ensure that access decisions are based on granular policies that consider various contextual factors like user role, device posture, and location.

To implement this recommendation, use the following methods, tools, and technologies:

  * **Unified identity management** : Ensure consistent identity management across your organization by using a single identity provider (IdP). 
    * Google Cloud supports federation with most IdPs, including on-premises [Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction). Federation lets you extend your existing identity management infrastructure to Google Cloud and enable single sign-on (SSO) for users.
    * If you don't have an existing IdP, consider using [Cloud Identity Premium](https://docs.cloud.google.com/identity/docs/editions) or [Google Workspace](https://workspace.google.com/).
  * **Limited service account permissions** : Use [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) carefully, and adhere to the principle of least privilege. 
    * Grant only the necessary permissions required for each service account to perform its designated tasks.
    * Use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identities) for applications that run on Google Kubernetes Engine (GKE) or run outside Google Cloud to access resources securely.
  * **Robust processes** : Update your identity processes to align with cloud security best practices. 
    * To help ensure compliance with regulatory requirements, implement identity governance to track access, risks, and policy violations.
    * Review and update your existing processes for granting and auditing access-control roles and permissions.
  * **Strong authentication** : Implement SSO for user authentication and implement MFA for privileged accounts. 
    * Google Cloud supports various MFA methods, including [Titan Security Keys](https://cloud.google.com/security/products/titan-security-key), for enhanced security.
    * For workload authentication, use OAuth 2.0 or signed JSON Web Tokens (JWTs).
  * **Least privilege** : Minimize the risk of unauthorized access and data breaches by enforcing the principles of least privilege and separation of duties. 
    * Avoid overprovisioning user access.
    * Consider implementing just-in-time privileged access for sensitive operations.
  * **Logging** : Enable audit logging for administrator and data access activities. 
    * For analysis and threat detection, scan the logs by using [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/service-tiers#enterprise-tier) or [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview).
    * Configure appropriate log retention policies to balance security needs with storage costs.



### Monitor and maintain your network

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Logging, auditing, and monitoring
  * Application security
  * Security operations (SecOps)
  * Infrastructure security



When you plan and implement security measures, assume that an attacker is already inside your environment. This proactive approach involves using the following multiple tools and techniques to provide visibility into your network:

  * **Centralized logging and monitoring** : Collect and analyze security logs from all of your cloud resources through centralized [logging and monitoring](https://docs.cloud.google.com/stackdriver/docs).

    * Establish baselines for normal network behavior, detect anomalies, and identify potential threats.
    * Continuously analyze network traffic flows to identify suspicious patterns and potential attacks.
  * **Insights into network performance and security** : Use tools like [Network Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview). Monitor traffic for unusual protocols, unexpected connections, or sudden spikes in data transfer, which could indicate malicious activity.

  * **Vulnerability scanning and remediation** : Regularly scan your network and applications for vulnerabilities.

    * Use [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings), which can automatically identify vulnerabilities in your Compute Engine instances, containers, and GKE clusters.
    * Prioritize remediation based on the severity of vulnerabilities and their potential impact on your systems.
  * **Intrusion detection** : Monitor network traffic for malicious activity and automatically block or get alerts for suspicious events by using [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/overview) and [Cloud NGFW intrusion prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention).

  * **Security analysis** : Consider implementing [Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) to correlate security events from various sources, provide real-time analysis of security alerts, and facilitate incident response.

  * **Consistent configurations** : Ensure that you have consistent security configurations across your network by using configuration management tools.




[ Previous arrow_back  Implement security by design  ](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design)

[ Next Implement shift-left security  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-05 UTC."],[],[]] 
