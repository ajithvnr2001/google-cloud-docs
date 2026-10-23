---
url: https://docs.cloud.google.com/iam/docs/built-in-resource-identities/
title: Built-in identities for resources \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:35.517234+00:00
---

# Built-in identities for resources  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/built-in-resource-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Built-in identities for resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes built-in identities for resources, which let you grant roles to resources in your IAM allow policies.

## Built-in identities

Some resources have built-in identities. These identities let the resources act like [principals](https://docs.cloud.google.com/iam/docs/principals-overview). As a result, resources with built-in identities can do the following:

  * Be [granted IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) using the [resource's principal identifier](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities)
  * Access other resources without using [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)



For example, consider Parameter Manager parameters, which have built-in identities. Parameters sometimes need access to Secret Manager to function properly. To let a parameter access Secret Manager, you use its identifier to grant it the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`). Then, the parameter can access Secret Manager secrets on your behalf.

For a list of resources with built-in identities, see [Resources with built-in identities](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities).

You can't use a resource's built-in identity to authenticate customer-managed workloads, like workloads running on Compute Engine instances. If you need to authenticate a workload, use one of the methods described in [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication).

## Granting roles to resources with built-in identities

If a resource has a built-in identity, you can grant roles to the resource by including the resource's _principal identifier_ in your allow policies. To see what format to use for each resource's principal identifier, see [Principal identifiers for single resources](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities#single-resources).

IAM also offers identifiers for sets of resources with built-in identities that share certain characteristics, such as type or ancestor. You can use these identifiers in your allow policies to grant the same role to multiple resources. To see what formats are supported, see [Principal identifiers for sets of resources](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities#resource-sets).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
