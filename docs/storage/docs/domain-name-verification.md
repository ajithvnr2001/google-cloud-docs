---
url: https://docs.cloud.google.com/storage/docs/domain-name-verification/
title: Domain-named bucket verification \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:55.712254+00:00
---

# Domain-named bucket verification  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/domain-name-verification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Domain-named bucket verification Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the requirements and verification process for domain-named buckets in Cloud Storage.

Domain-named buckets are buckets named after registered domains such as, `example.com`. To create a domain-named bucket in Cloud Storage, you must verify domain ownership. You can use these buckets to host static websites or organize your data under your custom domains. For information about bucket naming, see the [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

## Requirements for domain-named buckets

Cloud Storage considers bucket names that contain dots to be domain names. As such, a bucket containing a dot in its name must:

  * Be a syntactically valid DNS name (for example, `bucket..example.com` is not valid because it contains two dots in a row).
  * End with a currently-recognized top-level domain, such as `.com`.
  * Be created by a user who is authorized to work with the domain name.



Examples of valid domain-named buckets include `example.com`, `buckets.example.com`, and `www.example.co.uk`.

## Who can create a domain-named bucket

To create a bucket that uses a domain name, you must establish that you are authorized to use the domain name. People authorized to use a domain name include:

  * Verified owners of the domain or parent domain
  * Delegated owners of the domain or parent domain
  * [Verified site owners](https://support.google.com/webmasters/answer/7687615#manage-owners) of the domain or parent domain



Site owners cannot create the bucket when a domain owner exists. This allows the domain owners to tightly control who can create domain-named buckets.

For example, say you have an IT staff member who owns the website that uses `http://reports.example.com`. Once they go through verification of that site, they can create buckets such as `reports.example.com` and `annual.reports.example.com`. However, if you later verify that you own the domain `example.com`, only you can then create these buckets. Since you verified the domain `example.com`, you can also create the bucket `example.com`. As the site owner, your IT staff member can no longer create buckets.

## Domain ownership verification

If your project intends to have a domain-named bucket, the team member creating the bucket must demonstrate that they are authorized to create a bucket in the given domain. When you intend to [host your domain's content](https://docs.cloud.google.com/storage/docs/hosting-static-website) in a Cloud Storage bucket, the recommended verification method is to verify domain ownership.

Cloud Storage uses the [Search Console](https://search.google.com/search-console) to verify domain ownership.

**To verify domain ownership:**

  1. Open Search Console. You must be signed in with the user account that you will use to manage ownership of your domain.

[Open Search Console](https://search.google.com/search-console)

**Note:** If you have previously verified a property in Search Console, click the drop-down associated with the previous property's name, and click **Add property**.
  2. In the **Domain** pane, enter the domain or sub-domain that you want to verify, and click **Continue**.

**Note:** Generally, the domain you verify should be the root-level that you own, without any prefixes such as `www`. An example of a root-level domain is `example.com`.
  3. Follow the instructions that appear in the pane **Verify domain ownership via DNS record**.




### Delegated owners

Once you have verified domain ownership, you can add additional _delegated owners_ , who can also create buckets under the verified domain name. These owners can include [service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).

**To add delegated owners to your domain:**

  1. Go to [Search Console's user management page](https://search.google.com/search-console/users). Make sure that the domain you want to manage is selected in the [property selector](https://support.google.com/webmasters/answer/10352053).
  2. Click **Add user**.
  3. In the dialog, enter the email of the new owner.
  4. For **Permission** select "Owner".
  5. Click **Add**.

**Note:** You can only add domain owners if you are also a domain owner.

## Troubleshooting

See the [Search Console help page](https://support.google.com/webmasters/answer/35179) for information on topics including:

  * Methods of verifying site ownership.
  * Verifying using a DNS TXT or CNAME record.
  * Troubleshooting common verification errors.



## What's next

  * [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * Learn how to [host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).
  * Learn about [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
