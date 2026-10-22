---
url: https://docs.cloud.google.com/storage/docs/public-access-prevention/
title: Public access prevention \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:20.015792+00:00
---

# Public access prevention  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/public-access-prevention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Public access prevention Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/using-public-access-prevention)

This page discusses the public access prevention bucket setting and the related public access prevention organization policy constraint. Using either the setting or constraint restricts the entities, such as anonymous users over the internet, that can be granted access to your data. For an overview of access control options, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).

## Overview

Public access prevention protects Cloud Storage buckets and objects from being accidentally exposed to the public. When you enforce public access prevention, no one can make data in applicable buckets public through IAM policies or ACLs. There are two ways to enforce public access prevention:

  * You can enforce public access prevention on individual buckets.

  * If your bucket is contained within an organization, you can enforce public access prevention by using the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy) constraint [`storage.publicAccessPrevention`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention) at the [project, folder, or organization level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).


**Note:** Public access prevention doesn't apply to the creation and sharing of [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) or to private buckets, because access for these features is granted through scoped service account permissions.

### Should you use public access prevention?

**Note:** Before using public access prevention, we recommend that you review [considerations](https://docs.cloud.google.com/storage/docs/public-access-prevention#enforcing).

Use public access prevention if you know your data should never be exposed on the public internet. To provide the most security to your resources, enforce public access prevention at the highest possible level of your organization.

You can use public access prevention in combination with private bucket access. Public access prevention lets you protect data from accidental public exposure, whereas private bucket access lets you host publicly-visible content while allowing access only through Cloud Load Balancing and Cloud CDN.

You shouldn't use public access prevention if you keep the bucket public for use cases such as [static website hosting](https://docs.cloud.google.com/storage/docs/hosting-static-website). To make exceptions for such buckets in organizations that otherwise enforce public access prevention, disable public access prevention on the specific project that contains the bucket.

## Behavior when enforced

Resources subject to public access prevention have the following behavior:

  * Requests to buckets and objects authorized using `allUsers` and `allAuthenticatedUsers` fail with an HTTP `401` or `403` status code.

  * Existing IAM policies and ACLs granting access to `allUsers` and `allAuthenticatedUsers` remain in place but are overridden by public access prevention.

  * Requests to create buckets or objects with `allUsers` and `allAuthenticatedUsers` in their IAM policies or ACLs fail, with the following exception:

    * If a bucket has a default object ACL containing `allUsers`, requests to create objects in that bucket succeed. The ACLs for such objects contain `allUsers`, but `allUsers` is overridden by public access prevention.
  * Requests to add `allUsers` and `allAuthenticatedUsers` to an IAM policy or ACL fail with `412 Precondition Failed`.




### Inheritance

Even if a bucket does not have public access prevention explicitly enforced in its settings, it might still [inherit](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) public access prevention, which occurs if the organization policy constraint [`storage.publicAccessPrevention`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention) is set on the project, folder, or organization that the bucket exists within. For this reason, the bucket state can only be set to `enforced` or `inherited`.

  * If a bucket's public access prevention metadata [is set to `enforced`](https://docs.cloud.google.com/storage/docs/using-public-access-prevention#bucket-set), then public access prevention applies for the bucket.

  * If a bucket's public access prevention metadata [is set to `inherited`](https://docs.cloud.google.com/storage/docs/using-public-access-prevention#bucket-set), then public access prevention is determined by the `storage.publicAccessPrevention` organization policy constraint:

    * If `storage.publicAccessPrevention` is set to `True` for the [project](https://docs.cloud.google.com/storage/docs/projects) that contains the bucket, then public access prevention applies to the bucket.

    * If `storage.publicAccessPrevention` is set to `False` for the project that contains the bucket, then public access prevention does not apply to the bucket.

    * If `storage.publicAccessPrevention` is not set for the project that contains the bucket, then public access prevention is determined by the `storage.publicAccessPrevention` value set by the folder, if any, that contains the project.

      * Similarly, if the folder containing the bucket also does not set any value for `storage.publicAccessPrevention`, then public access prevention is determined by the `storage.publicAccessPrevention` value set by the organization that contains the project.

      * If `storage.publicAccessPrevention` is not set for any resource, then public access prevention does not apply to the bucket.




## Behavior if disabled

When public access prevention no longer applies for a resource, the following occurs:

  * Existing IAM policies and ACLs that grant access to `allUsers` and `allAuthenticatedUsers` take effect and make data accessible to the public.

  * Requests to create IAM policies or ACLs that allow access to `allUsers` and `allAuthenticatedUsers` succeed.

  * An object created under public access prevention without public ACLs may become accessible to the public if it was created in a publicly accessible bucket.




You can disable public access prevention for a project, folder, or organization at any time. Buckets with an `enforced` setting continue to have public access prevention enforced, even if you disable it for a project, folder, or organization that contains the bucket.

## Considerations

  * When you enforce public access prevention on existing resources, all existing authorization and new additions of `allUsers` and `allAuthenticatedUsers` are blocked. This can affect your buckets in the following ways:

    * If an application depends on `allUsers` and `allAuthenticatedUsers` to access your data or create public resources, enabling public access prevention can break the application. For information about how to identify your public resources that other applications might be depending on, expand the following content:

#### How to identify public resources

Before you enforce public access prevention, we recommend that you take inventory of your public resources to make sure you don't break other workloads that have a dependency on your data being public. You can locate buckets, objects, and managed folders that are public by using the following methods:

      * To help identify workloads that might be accessing your public data, [set up usage logs](https://docs.cloud.google.com/storage/docs/access-logs#delivery), which can provide information about data access requests made to public resources.
      * To determine if a bucket might be accessible to the public, [check the bucket's IAM policies](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-view). Policies that grant roles to the principal `allUsers` or `allAuthenticatedUsers` make the bucket potentially accessible to the public. As an alternative to getting the IAM policy for individual buckets, you can use Cloud Asset Inventory to [view the policies for all buckets in a project, folder, or organization](https://docs.cloud.google.com/asset-inventory/docs/query-assets).

If there are [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) in your bucket, you might also want to [check the IAM policies of the managed folders](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders#managed-folder-view) to identify which managed folders might be accessible to the public.

      * To determine if individual objects might be accessible to the public, [check the object for ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#retrieving-acls). ACLs that grant access to the principal `allUsers` or `allAuthenticatedUsers` make the object potentially accessible to the public. **Note:** If [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled for your bucket, ACLs cannot be used to individually control access to objects, so you can skip this step. To check if uniform bucket-level access is enabled for your bucket, see [view status of uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#view-status). 
    * [Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/audit-logs) does not track access to objects that are public. If Data Access logs are enabled when you enforce public access prevention, you might see an increase in log generation, which count towards your log ingestion quota and can incur Cloud Audit Logs charges. This increase might occur because access that previously was public and unlogged could become associated with specific authorizations, which is logged.

  * [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls), which give time limited, narrowly-scoped access to anyone who uses them, are not affected by public access prevention.

  * Private bucket access, which lets you use a bucket as the backend to serve content only through Cloud Load Balancing and Cloud CDN, is not affected by public access prevention. See [private bucket access for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets#enable_private_bucket_access), [private bucket access for classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets#enable_private_bucket_access), and [private bucket access for Cloud CDN](https://docs.cloud.google.com/cdn/docs/configure-private-bucket-access).

  * Projects not associated with an organization cannot use organization policies. Buckets within such a project should use the bucket-level setting.

  * Public access prevention is [strongly consistent](https://docs.cloud.google.com/storage/docs/consistency) for reading-after-update, but enforcement can take up to 10 minutes to take effect.

  * After enforcement begins, your objects might still be publicly accessible through an internet cache for some amount of time, depending on the objects' [`Cache-Control` setting](https://docs.cloud.google.com/storage/docs/metadata#cache-control). For example, if the `Cache-Control:max-age` for an object is set to the default of 3600 seconds, the object might persist in an internet cache for that amount of time.




## What's next

  * Learn how to [use public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention).
  * Read more about [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
