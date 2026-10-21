---
url: https://docs.cloud.google.com/iam/docs/managed-workload-identity/
title: Managed workload identities overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:02.474224+00:00
---

# Managed workload identities overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/managed-workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Managed workload identities overview Stay organized with collections  Save and categorize content based on your preferences. 

Managed workload identities lets you bind strongly attested identities to your Google Kubernetes Engine (GKE) and Compute Engine workloads. This also includes agent identities, which are designed for agentic workloads.

Google Cloud provisions X.509 credentials and trust anchors that are issued from [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service). The credentials and trust anchors can be used to reliably authenticate your workload with other workloads through [mutual TLS (mTLS)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/understand-mtls) authentication.

The following features are available:

  * Managed workload identities for GKE ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Managed workload identities for Compute Engine
  * Agent identities



## SPIFFE interoperability

To enable interoperability across dynamic and heterogeneous environments, managed workload identities is based on [Secure Production Identity Framework For Everyone (SPIFFE)](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/). SPIFFE defines a framework and set of standards for identifying, authenticating, and securing communications between workloads. SPIFFE workloads are identified by a unique SPIFFE ID. In Google Cloud, a SPIFFE ID has the following formats:

  * Compute Engine workloads:

`spiffe://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID`

  * GKE workloads:

`spiffe://PROJECT_ID.svc.id.goog/ns/KUBERNETES_NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT`

  * Agent identity workloads:

`spiffe://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/LOCATION/reasoningEngines/AGENT_NAME`




## Resource hierarchy

This section describes managed workload identity resources.

### Workload identity pools

Managed workload identities are defined within a _workload identity pool_ , which acts as a trust boundary for all identities within the pool. The workload identity pool forms the trust domain component of the managed workload identity's SPIFFE identifier. We recommend creating a new pool for each logical environment in your organization, such as development, staging, or production.

### Namespaces

Within a workload identity pool, managed workload identities are organized into administrative boundaries called _namespaces_. Namespaces help you organize and grant access to related workload identities.

### Attestation policies

Managed workload identity for Compute Engine requires that you configure _attestation policies_.

Managed workload identity for GKE manages attestation policies for you.

Workload attestation policies let you define which workload can be issued a credential for a managed workload identity based on the workload's verifiable attributes, such as project ID or resource name. A workload attestation policy ensures that only trusted workloads can use the managed identity.

## What's next

  * [Configure managed workload identity authentication for Compute Engine](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities).

  * [Configure managed workload identity authentication for GKE](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke).

  * Learn more about [using managed workload identities with Compute Engine workloads](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).

  * Learn more about [using agent identity with Vertex AI Agent Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity).




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
