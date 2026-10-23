---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/workforce-identity-federation/
title: Workforce access to Managed Service for Apache Spark Component Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:33.222157+00:00
---

# Workforce access to Managed Service for Apache Spark Component Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/workforce-identity-federation/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Workforce access to Managed Service for Apache Spark Component Gateway Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:** This document show you how to allow external identity users to click Managed Service for Apache Spark [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) URL links in the Google Cloud console to connect to component web interfaces running on the first master node of a Managed Service for Apache Spark cluster.

## Background

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you use an external identity provider (IdP) to authenticate and authorize workforce employees, partners, and contractors to Google Cloud services.

If Workforce Identity Federation is [configured in your project](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#configure_workforce_identity_federation), external identity users can use the Google Cloud console, Google Cloud CLI, and the Managed Service for Apache Spark API to access most Managed Service for Apache Spark resources and features, except the following:

  * [Managed Service for Apache Spark on GKE](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/dataproc-gke-overview)
  * [Managed Service for Apache Spark Personal Authentication](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/personal-auth)
  * [Managed Service for Apache Spark Service Account Based Secure Multi-tenancy](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy)
  * The **Output** section in the Batch and Job details pages and the **Recommended Alerts** section in the Cluster and Job list pages in the Google Cloud console.



## Use workforce identify federation with the Managed Service for Apache Spark Component Gateway

  1. Configure workforce identify federation by following the [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#configure_workforce_identity_federation) guide.

  2. Grant external identity users the [`dataproc.clusters.use`](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#clusters_methods_required_permissions) role to allow access the Managed Service for Apache Spark Component Gateway (see [Grant IAM roles to principals](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant_roles_to_principals)).

     * For instructions on how to represent external identities in IAM policies, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).
  3. [Create a Managed Service for Apache Spark cluster with Component Gateway enabled](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways#rest-api).




## Access cluster web interfaces

See [Viewing and Accessing Component Gateway URLs](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways#viewing_and_accessing_component_gateway_urls), and note the following differences for external identity users:

  1. Only users that are authenticated with external identities can access the URL for external identities. If a user visits the URL for external identities while not logged in, they are redirected to the authentication portal where they specify their workforce pool provider name. Next, they are redirected to their identity provider to sign in. Then, they are redirected to the component web interface.

  2. External identities URLs have the following format:
         
         https://UNIQUE_ID-dot-dataproc.byoid.googleusercontent.com
         




## What's next

  * Create a cluster with [Managed Service for Apache Spark components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
