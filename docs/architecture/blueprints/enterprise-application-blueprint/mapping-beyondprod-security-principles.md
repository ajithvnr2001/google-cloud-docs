---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/mapping-beyondprod-security-principles/
title: Mapping BeyondProd security principles to the blueprint \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:40.375108+00:00
---

# Mapping BeyondProd security principles to the blueprint  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/mapping-beyondprod-security-principles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Mapping BeyondProd security principles to the blueprint Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

[BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod) refers to the services and controls in Google's infrastructure that work together to help protect workloads. BeyondProd helps protect the application services that Google runs in its own environment, including how Google changes code and how Google ensures service isolation. Although the BeyondProd paper refers to specific technologies that Google uses to manage its own infrastructure that aren't exposed to customers, the security principles of BeyondProd can be applied to customer applications as well.

BeyondProd includes several key security principles that apply to the blueprint. The following table maps the BeyondProd principles to the blueprint.

Security principle | Mapping to blueprint | Security capability  
---|---|---  
Network edge protection | Cloud Load Balancing | Helps protect against various DDoS attack types such as UDP floods and SYN floods.  
Cloud Armor | Helps provide protection against web application attacks, DDoS attacks, and bots through always-on protection and customizable security policies.  
Cloud CDN | Helps provide DDoS attack mitigation through taking load away from exposed services by directly serving content.  
GKE clusters with Private Service Connect access to the control plane and private node pools for clusters that use private IP addresses only | Helps protect against public internet threats and helps provide more granular control over access to the clusters.  
Firewall policy | Narrowly defines an allowlist for inbound traffic to GKE services from Cloud Load Balancing.  
No inherent mutual trust between services | Cloud Service Mesh | Enforces authentication and authorization to help ensure only approved services can communicate with one another.  
Workload Identity Federation for GKE | Enhances security by reducing the risk of credential theft through automating the authentication and authorization process for workloads, eliminating the need for you to manage and store credentials.  
Firewall policy | Helps ensure only approved communication channels are allowed within the Google Cloud network to GKE clusters.  
Trusted machines that run code with known provenance | Binary Authorization | Helps ensure only trusted images are deployed to GKE by enforcing imaging signing and signature validation during deployment.  
Consistent policy enforcement across services | Policy Controller | Lets you define and enforce policies that govern your GKE clusters.  
Simple, automated, and standardized change rollout | 

  * Foundation infrastructure pipeline
  * Multi-tenant infrastructure pipeline
  * Fleet-scope pipeline
  * Application factory pipeline
  * Application CI/CD pipeline

| Provides an automated and controlled deployment process with built-in compliance and validation to build out resources and applications.  
Config Sync | Helps improve cluster security by providing centralized configuration management and automated configuration reconciliation.  
Isolation between workloads that share an operating system | Container-Optimized OS | Container-Optimized OS contains only essential components required for running Docker containers, making it less vulnerable to exploits and malware.  
Trusted hardware and attestation | Shielded GKE nodes | Ensures only trusted software is loaded when a node boots up. Continually monitors the node's software stack, alerting you if any changes are detected.  
  
## What's next

  * Read about [deploy the blueprint](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
