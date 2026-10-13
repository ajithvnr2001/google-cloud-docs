---
url: https://docs.cloud.google.com/python/docs/reference/orgpolicy/latest/google.cloud.orgpolicy_v2.services.org_policy
title: Package org_policy (1.19.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:17.543195+00:00
---

# Package org_policy (1.19.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/orgpolicy/latest/google.cloud.orgpolicy_v2.services.org_policy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package org_policy (1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.1  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.0  1.5.0  1.4.1  1.3.3  1.2.1  1.1.0  1.0.2  0.3.0  0.2.0  0.1.2 

API documentation for `orgpolicy_v2.services.org_policy` package.

## Classes 

### [OrgPolicyAsyncClient](https://docs.cloud.google.com/python/docs/reference/orgpolicy/latest/google.cloud.orgpolicy_v2.services.org_policy.OrgPolicyAsyncClient)

An interface for managing organization policies.

The Organization Policy Service provides a simple mechanism for organizations to restrict the allowed configurations across their entire resource hierarchy.

You can use a policy to configure restrictions on resources. For example, you can enforce a policy that restricts which Google Cloud APIs can be activated in a certain part of your resource hierarchy, or prevents serial port access to VM instances in a particular folder.

Policies are inherited down through the resource hierarchy. A policy applied to a parent resource automatically applies to all its child resources unless overridden with a policy lower in the hierarchy.

A constraint defines an aspect of a resource's configuration that can be controlled by an organization's policy administrator. Policies are a collection of constraints that defines their allowable configuration on a particular resource and its child resources.

### [OrgPolicyClient](https://docs.cloud.google.com/python/docs/reference/orgpolicy/latest/google.cloud.orgpolicy_v2.services.org_policy.OrgPolicyClient)

An interface for managing organization policies.

The Organization Policy Service provides a simple mechanism for organizations to restrict the allowed configurations across their entire resource hierarchy.

You can use a policy to configure restrictions on resources. For example, you can enforce a policy that restricts which Google Cloud APIs can be activated in a certain part of your resource hierarchy, or prevents serial port access to VM instances in a particular folder.

Policies are inherited down through the resource hierarchy. A policy applied to a parent resource automatically applies to all its child resources unless overridden with a policy lower in the hierarchy.

A constraint defines an aspect of a resource's configuration that can be controlled by an organization's policy administrator. Policies are a collection of constraints that defines their allowable configuration on a particular resource and its child resources.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/orgpolicy/latest/google.cloud.orgpolicy_v2.services.org_policy.pagers)

API documentation for `orgpolicy_v2.services.org_policy.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
