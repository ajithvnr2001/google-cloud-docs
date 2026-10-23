---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/observability/monitor-mesh-security/
title: Monitoring mesh security \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:37.203197+00:00
---

# Monitoring mesh security  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/observability/monitor-mesh-security/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring mesh security

The [GKE Enterprise Security dashboard](https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring) provides an at-a-glance view of your applications' current security features as well as a more detailed policy audit view to show you where you can add or enable features to make your application workloads more secure.

This page describes how to use the GKE Enterprise security dashboard to monitor Cloud Service Mesh features.

## Monitoring authorization policies

  1. To view status of authorization policies on the GKE Enterprise security dashboard, go to the Security page in the Google Cloud console.

[Go to GKE Enterprise Security](https://console.cloud.google.com/anthos/security/policy-summary)

  2. In the **Access control** card, click **Service access control** to view a per-cluster rundown.

This window lists every cluster in your project, their location, and whether or not authorization policies are in effect. If policies are in effect, you can also view the policy details and the number of blocked service requests. If none of your clusters have an authorization policy, see [Authorization policy overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/security/authorization-policy-overview) for more information.

  3. If any of your clusters have a policy in effect, click **Policy details** to view specific details on the Policy audit page.

This page displays the Workloads running in a single cluster, including the name, namespace, and service access control status. You can select another cluster from the cluster drop-down menu or filter Workloads by selecting a namespace from the namespace drop-down menu.

  4. In the **Service access controls** column, click **Enabled** to view the authorization policy for a specific Workload.

This page displays the authorization policy's name, scope, and creation date. You can also view the entire authorization policy YAML by clicking the down arrow icon or anywhere on the row.




## Monitoring mTLS policies

  1. To view the status of mTLS policies on the GKE Enterprise security dashboard, go to the Security page in the Google Cloud console.

[Go to GKE Enterprise Security](https://console.cloud.google.com/anthos/security/policy-summary)

  2. In the **Authentication** card, click **mutual TLS (mTLS)** to view a per-cluster rundown.

This window lists every cluster in your project, their location, and whether or not mTLS is enabled. If mTLS is enabled, you can also view the policy details.

If none of your clusters have mTLS enabled, see [Configuring mTLS](https://docs.cloud.google.com/service-mesh/v1.24/docs/security/configuring-mtls).

  3. If any of your clusters have mTLS enabled, click **Policy details** to view specific details on the Policy audit page.

This page displays the Workloads running in a single cluster, including the name, namespace, and mTLS details. You can select another cluster from the cluster drop-down menu or filter Workloads by selecting a namespace from the namespace drop-down menu.

  4. In the **mTLS details** column, click **Strict** , **Permissive** , or **Disabled** to view the mTLS details for a specific Workload.

This page displays the name, scope, mode, and creation date. You can also view the entire mTLS YAML by clicking the down arrow icon or anywhere on the row.




## What's next

  * [Learn more about security in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.24/docs/security/security-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
