---
url: https://docs.cloud.google.com/storage/docs/bypass-ip-filter/
title: Bypass bucket IP filtering rules \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.195453+00:00
---

# Bypass bucket IP filtering rules  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bypass-ip-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bypass bucket IP filtering rules Stay organized with collections  Save and categorize content based on your preferences. 

You can allow users or service accounts to perform certain operations on buckets without any IP filtering restrictions, while still enforcing restrictions for other operations. To do this, you bypass IP filtering rules.

It's crucial to have a way to regain access to your bucket if you inadvertently block your own IP address. This can happen due to the following reasons:

  * **Bucket lockout** : When you accidentally add a rule that blocks your own IP address or the IP range of your entire network.

  * **Unexpected IP change** : In some cases, your IP address might change unexpectedly due to network changes, and you might find yourself locked out.




For background information about bucket IP filtering, see [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

## Supported operations

When you bypass IP filtering, the following operations are exempt from IP filtering restrictions:

  * Getting a bucket's metadata ([`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get))
  * Updating a bucket ([`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch))
  * Deleting a bucket ([`DELETE` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/delete))



## Bypass bucket IP filtering rules

To enable specific users or service accounts to bypass IP filtering restrictions on a bucket, grant them the `storage.buckets.exemptFromIpFilter` permission using a custom role. This permission exempts the user or service account from IP filtering rules for supported bucket-level operations. To do so, complete the following steps:

  1. Identify the user or service account that needs to bypass the IP filtering restrictions on specific buckets.

  2. Create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  3. Add the `storage.buckets.exemptFromIpFilter` permission to the role.

  4. Grant the custom role to the identified user or service account at the project level. For information about granting roles, see [Grant a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role).




After you grant the users or service accounts these permissions, they can perform supported operations without any IP filtering restrictions. Requiring explicit permissions ensures that bypassing IP filtering rules is a deliberate and authorized action by providing granular control over the exceptions to the rules.

## Bypass IP filtering rules for Google Cloud service agents

You can let Google Cloud service agents bypass IP filtering rules for your bucket. The service agent and the bucket must be in the same project.

When enabled, services such as Compute Engine or Cloud Run within the bucket's project can access the bucket freely, regardless of their IP addresses. Service agents from different projects can't use this bypass. If you need to grant access to services in other projects while maintaining IP-based restrictions, consider using features like [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) or [IAM](https://docs.cloud.google.com/iam/docs/overview) conditions.

For information about how to allow Google Cloud service agents to access your bucket, see [Manage service agent access](https://docs.cloud.google.com/storage/docs/update-ip-filter#manage-service-agent-access).

## Bypass IP filtering rules for cross-organization VPC networks

You can let resources from a different organization's VPC network access the bucket without restrictions from your existing IP filtering configuration. For information about how to allow cross-organization VPC networks to access your bucket, see [Manage cross-organization VPC access](https://docs.cloud.google.com/storage/docs/update-ip-filter#manage-vpc-access).

## What's next

  * [Disable IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).
  * [Get IP filtering rules on a bucket](https://docs.cloud.google.com/storage/docs/get-ip-filter).
  * [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
