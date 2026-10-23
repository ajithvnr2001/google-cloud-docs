---
url: https://docs.cloud.google.com/load-balancing/docs/access-control/
title: Roles and permissions \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:08.384886+00:00
---

# Roles and permissions  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

When you use Cloud Load Balancing, you make API requests. Each API request requires that the [Identity and Access Management (IAM) principal](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works) who makes the request has appropriate permission to create, modify, or delete the associated resources.

In IAM, permission to access a Google Cloud resource isn't granted directly to the end user. Instead, permissions are grouped into roles, and roles are granted to authenticated principals. Principals can be of the following types: a user, group, service account, or Google domain. An IAM policy defines and enforces what roles are granted to which principals, and this policy is then attached to a resource.

This page provides an overview of relevant IAM roles and permissions for Cloud Load Balancing. For a detailed description of IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

## Roles and permissions

To follow the examples in the load balancing [how-to guides](https://docs.cloud.google.com/load-balancing/docs/how-to), principals need to create instances, firewall rules, and VPC networks. You can provide the necessary permissions in one of the following ways:

  * Grant the [predefined roles](https://docs.cloud.google.com/compute/docs/access/iam) that are related to load balancing. To view the specific permissions included in the predefined roles, see the following sections:

    * Compute Load Balancer Admin role ([`roles/compute.loadBalancerAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerAdmin))
    * Compute Network Admin role ([`roles/compute.networkAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin))
    * Compute Security Admin role ([`roles/compute.securityAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin))
    * Compute Instance Admin role ([`roles/compute.instanceAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin))
  * [Create and grant custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that at least contain the permissions included in the predefined roles.

  * Use [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), making the principals project owners or editors. Whenever possible, avoid using the basic roles; they grant a large number of permissions, which violates the principle of least privilege.




## Role change latency

Cloud Load Balancing caches IAM permissions for five minutes, so it takes up to five minutes for a role change to become effective.

## Managing Access Control for Cloud Load Balancing using IAM

You can get and set IAM policies using the Google Cloud console, the IAM API, or the Google Cloud CLI. See [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for details.

## What's next

  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * [Grant IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn about [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions).
  * Learn about [organization policy constraints for Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
