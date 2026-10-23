---
url: https://docs.cloud.google.com/apigee/docs/hybrid/shared-responsibility-model/
title: Apigee hybrid shared responsibility model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:38.011193+00:00
---

# Apigee hybrid shared responsibility model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/shared-responsibility-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee hybrid shared responsibility model Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the shared responsibilities between Google and Apigee hybrid customers with respect to management of Apigee hybrid installations and software. 

## Customer Responsibilities

Apigee hybrid customers are responsible for:

  * Maintaining connectivity between the Apigee hybrid data plane and the Google managed Apigee control plane. Maintain all network infrastructure like VPN, Interconnect etc. that's deployed to manage connectivity between the Google managed Apigee control plane and the Apigee hybrid data plane. 
  * Provisioning of the underlying compute, storage and network infrastructure as per Apigee's recommendations/documentation (see [Minimum cluster configurations](https://cloud.google.com/apigee/docs/hybrid/v1.9/cluster-overview.html)); that's hosting their Apigee hybrid installation on Anthos or third party Kubernetes platforms. This includes cross region network connectivity, DNS resolution, storage expansion and other day to day operations 
  * Keep the Kubernetes platform and underlying infrastructure up to date with latest software updates and patches along with ensuring compatibility with the Apigee hybrid platform. See [Apigee hybrid supported platforms](https://cloud.google.com/apigee/docs/hybrid/supported-platforms) for compatibility matrix. For non-Anthos installations, work with your vendor to resolve any issues related to your cluster installation and upgrade. For Anthos installations, please refer to [Anthos shared responsibility](https://cloud.google.com/anthos/docs/concepts/gke-shared-responsibility#:~:text=Customer's%20responsibilities,-Provide%20overall%20system&text=Operate%20and%20maintain%20the%20AWS,and%20respond%20to%20any%20incidents.) documentation. 
  * Provision and manage the load balancers that expose the APIs deployed on Apigee hybrid to their intended consumers. This includes managing the lifecycle of SSL certificates, scaling of the load balancers, failover capabilities etc. 
  * Maintain your workloads, including your application code, configuration files, container images, data, Role-based access control (RBAC)/IAM policy, and containers and pods that you are running. 
  * Overall system administration for your on-premises or multi-cloud Kubernetes clusters. Operate, maintain and patch and secure the infrastructure including compute, network, storage and ensuring connectivity to Google Cloud. Google recommends that you patch your on-premises or multi-cloud infrastructure in a timely manner to get latest security updates and bug fixes. 
  * Ensure the necessary telemetry (logging and monitoring) is set up for your Apigee hybrid deployment and the underlying infrastructure that's hosting the hybrid data plane 
  * Ensure business continuity through proper infrastructure deployment and corresponding deployment of Apigee hybrid using multi region deployments, setting up disaster recovery procedures etc. 
  * Achieving canary based migration of runtime traffic while onboarding to Apigee hybrid or migrating Apigee hybrid runtime from one Cloud to another. 



## Google Responsibilities

With respect to Apigee hybrid, Google is responsible to: 

  * Maintain and distribute the Apigee hybrid software package including runtime, mart, Cassandra and Kubernetes controllers, ingress gateway, logging, and monitoring agents, and the apigeectl command line tool 
  * Ensuring compatibility with the Google managed services in the Apigee API Management suite such as Apigee Management APIs, Management UI, Analytics etc. Google would also be responsible for rolling out regular updates to these services ensuring compatibility with customer's hybrid deployment for supported versions of Apigee hybrid 
  * Continually scan components with the [Container Analysis API](https://cloud.google.com/container-registry/docs/container-analysis) and patch known vulnerabilities. See Security patching for Apigee hybrid for more details 
  * Notify users of available upgrades for Apigee hybrid and provide upgrade steps and patches. Note that Apigee hybrid only supports sequential upgrades (1.6 → 1.7 → 1.8 only and not 1.6 → 1.8) 
  * Provide Google Cloud integrations for connecting to the management plane (via Apigee Connect) and Google Cloud Observability, which includes services such as Cloud Logging and Cloud Monitoring 
  * Troubleshoot, provide workarounds, and correct the root cause of any issues related to Google-provided components.



# Related Links

[Minimum cluster configurations](https://cloud.google.com/apigee/docs/hybrid/v1.9/cluster-overview.html)

[Configure Cassandra for production](https://cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production)

[Configuring dedicated node pool](https://cloud.google.com/apigee/docs/hybrid/v1.9/configure-dedicated-nodes)

[Scale and autoscale services](https://cloud.google.com/apigee/docs/hybrid/v1.9/scale-and-autoscale)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
