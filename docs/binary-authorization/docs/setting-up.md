---
url: https://docs.cloud.google.com/binary-authorization/docs/setting-up/
title: Set up for GKE \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:20.409448+00:00
---

# Set up for GKE  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/setting-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Set up for GKE Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to set up Binary Authorization enforcement in your environment for use with Google Kubernetes Engine (GKE). You can set up Binary Authorization by using the Google Cloud console or the Google Cloud CLI. You can also perform some setup steps by using the Binary Authorization [REST API](https://docs.cloud.google.com/binary-authorization/docs/reference/rest).

For an end-to-end tutorial that includes the following setup steps, see [Get started using the Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli) or [Get started using the Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console).

To set up Binary Authorization, perform the following steps:

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).

  2. [Create a cluster](https://docs.cloud.google.com/binary-authorization/docs/creating-cluster) with Binary Authorization enabled or [enable Binary Authorization on an existing cluster](https://docs.cloud.google.com/binary-authorization/docs/enable-cluster).

**Note:** Binary Authorization doesn't enforce init containers.
  3. Configure your Binary Authorization policy.

**Note:** Skip this step if you want to use attestations.

You can configure the following features in your policy:

     * [Default rule](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule).
     * [Cluster-specific rules](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#set_cluster_specific_rules).
     * [Specific rules for your Kubernetes service identity or namespace](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm).
     * [Exempt images](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#exempt_images). [Learn more about exempt images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images).
  4. Optional: If you have different Google Cloud projects that own your policy or your Container Registry repositories, grant the IAM roles required for cross-project access. For instructions, see [Configure cross-project access for Binary Authorization in GKE](https://docs.cloud.google.com/binary-authorization/docs/cross-project-access-gke).

  5. Optional: Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).

  6. Optional: [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

  7. [Deploy container images](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers).

  8. [View events in Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
