---
url: https://docs.cloud.google.com/iam/docs/use-workload-identity-federation-to-let-customers-access-their-cloud-resources/
title: Let customers access their Google Cloud resources from your product or service \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:49.715821+00:00
---

# Let customers access their Google Cloud resources from your product or service  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/use-workload-identity-federation-to-let-customers-access-their-cloud-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Let customers access their Google Cloud resources from your product or service Stay organized with collections  Save and categorize content based on your preferences. 

This document describes requirements and best practices that you can follow to let customers use your product to access their resources in Google Cloud without using [service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete). 

If you offer a product or operate a service that lets customers analyze or manage data or resources, then your customers might want to access data or other resources in their Google Cloud environment. Examples for such products and services include the following:

  * **Data analytics products** : Your customers might want to use such products to analyze their data in BigQuery.
  * **CI/CD products and services** : Your customers might use such services to deploy infrastructure and applications to their Google Cloud projects.
  * **Robotic process automation (RPA)** : Your customers might use RPA for workflows such as creating projects, managing access, or automating administrative tasks in Google Cloud.



To authenticate on-premises or software-as-a-service (SaaS) products to Google Cloud, customers have conventionally relied on service account keys, but these keys can be [challenging to manage and store securely](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

As a vendor of an on-premises or SaaS product, you can help your customers protect their Google Cloud resources by letting them use Workload Identity Federation to access their Google Cloud resources. Examples for services that already let their customers use Workload Identity Federation include [Terraform Cloud, GitHub](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines), and [GitLab](https://docs.gitlab.com/ee/ci/cloud_services/google_cloud/)

This document describes how you can extend your product to support Workload Identity Federation, and describes best practice that you can follow. This document assumes that you're familiar with [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and [OpenID Connect](https://openid.net/connect/).

## Architecture

The intent of Workload Identity Federation is to remove the need for service account keys by letting your customers federate your product or service with their Google Cloud environment. Your customers can then access their Google Cloud resources using an identity asserted by your product or service.

To let your customers use Workload Identity Federation, your product or service must implement a subset of OpenID Connect. In particular, you must allow workloads to obtain an ID token that meets the following criteria:

  * The token identifies the workload within your product or platform
  * The token identifies the instance, tenant, or installation of your product or platform
  * The token contains a cryptographic signature that Workload Identity Federation can use to verify the token's authenticity



## Requirements

To support Workload Identity Federation, you must ensure that your product or service meets the following requirements:

  1. Workloads have access to a valid ID token.

At any time during their lifecycle, a workload must have access to an ID token that asserts the identity of the workload and complies with the [requirements defined by OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

Because ID tokens have a limited lifespan, you must ensure that an ID token either outlives its workload, or that workloads can periodically obtain new ID tokens.

  2. ID tokens uniquely identify the workload.

The ID token must contain at least one claim that uniquely identifies the workload. The workload identifier must be immutable.

For products or services that support multi-tenancy, the token must also contain at least one claim that uniquely identifies the tenant. The tenant identifier must also be immutable.

  3. ID tokens are signed, but not encrypted.

  4. OpenID provider metadata is publicly accessible and can be discovered from ID tokens.

You must provide an OpenID provider configuration document on a publicly accessible endpoint that can be discovered using the [OpenID issuer discovery protocol](https://openid.net/specs/openid-connect-discovery-1_0.html#IssuerDiscovery). For example, if ID tokens contain an `iss` claim with the value `https://service.example.com/v1/`, then you must provide an OpenID provider configuration document on `https://service.example.com/v1/.well-known/openid-configuration`, and the endpoint must be publicly accessible over the internet from any IP address.

  5. Signing keys are publicly accessible and can be discovered from OpenID provider metadata.

You must provide a [JSON Web Key Set (JWKS)](https://datatracker.ietf.org/doc/html/rfc7517) document on a publicly accessible endpoint that can be discovered from the `jwks_uri` field in the OpenID provider metadata.




## Best practices

When extending your product or service to support Workload Identity Federation, consider the following best practices.

**Best practices** :

Distinguish between identity and access tokens.  
Expose ID tokens in a way that's compatible with client libraries.  
Use tenant-specific issuer URLs.  
Allow users to specify the ID token audience.  
Use immutable, non-reusable identifiers in ID token claims.  
Include context information in ID tokens.  
Limit ID token lifetime to 30-60 minutes.  


### Distinguish between identity and access tokens

Within the context of Workload Identity Federation, the purpose of an ID token is to assert the identity of the workload: The token must contain sufficient information for Workload Identity Federation to identify the workload, and to distinguish it from other workloads.

In contrast to ID tokens, access tokens typically serve a different purpose: They are used for making access decisions and might contain information about what permissions a workload has, or which APIs it is allowed to access.

If your product or service uses access tokens for purposes such as letting workloads call your product's API, then these access tokens might not be well suited for Workload Identity Federation. Instead of repurposing access tokens as ID tokens, consider introducing a second type of token that matches the definition of an ID token, and let workloads use the ID token for Workload Identity Federation.

### Expose ID tokens in a way that's compatible with client libraries

The Google Cloud client libraries can automatically obtain ID tokens from multiple sources, including the following:

  * An HTTP endpoint (URL-sourced credentials)
  * A local file (file-sourced credentials)



To obtain ID tokens from other sources, your customers might need to modify their code, or deploy additional tools or libraries. By exposing ID tokens in a way that's compatible with client libraries, you can avoid such extra complexity, and make it easier for your customers to adopt Workload Identity Federation.

### Use tenant-specific issuer URLs

The claims embedded in a workload's ID token might be unique within a specific instance of your product or service, but they might not be unique across multiple instances of your product or service. For example, two of your customers might use your product or service to deploy a workload and inadvertently assign those workloads the same name and ID.

Workload Identity Federation attempts to compensate for this possible lack of uniqueness by [verifying the issuer URL (`iss`) of ID tokens](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation), and by only allowing tokens from a single issuer per workload identity pool.

If your product or service supports multi-tenancy, then several of your customers might share a single instance of your product or service, and their workloads' ID tokens might use the same issuer URL. Using the same issuer URL across multiple tenants can expose your customers to spoofing attacks: For example, a bad actor might create a workload in their own tenant, assign it the same ID or name as a workload in the victim's tenant, and use their workload's ID token to spoof the identity of the victim's workload.

To help protect your customers from spoofing attacks, avoid using the same issuer URLs across multiple tenants and embed a unique tenant ID in the issuer URL, for example `https://saas.example.com/tenant-123/`.

### Allow users to specify the ID token audience

Some of your customer's workloads might need to access Google Cloud as well as other third-party services. When customers decide to federate your product or service with multiple relying parties, they might find themselves in a situation where a workload's ID token is inadvertently or maliciously used for the wrong relying party: For example, a bad actor might trick a workload into revealing an ID token that was intended for a third-party service, and then use that ID token for Workload Identity Federation.

To help prevent your customers from falling victim to such [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) attacks, avoid using a static audience (`aud` claim) in ID tokens. Instead, [let workloads specify an audience when they obtain an ID token](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#provider-audience) and, optionally, maintain an allow-list for audiences that workloads can request.

By default, Workload Identity Federation expects an ID token's audience to match the URL `https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID`. Make sure that workloads can use a URL as the audience for ID tokens, and that the length of the audience URL is less than 180 characters.

### Use immutable, non-reusable identifiers in ID token claims

When customers want to grant one of their workloads access to Google Cloud resources, they must create an IAM binding that references the workload's identity by subject, group, or a custom attribute. The workload's identity's subject, group, and custom attributes are derived from the claims in the workload's ID token.

If a customer creates an IAM binding that refers to a mutable claim, then their workload might accidentally lose access when the claim's value changes. For example, a customer might create an IAM binding that references the name of their workload. If they subsequently rename the workload, the IAM binding might not apply anymore.

Worse, bad actors might attempt to gain unauthorized access to other resources by deliberately renaming workloads or modifying a workload's environment to spoof another workload's identity.

To help customers [prevent such spoofing issues](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-immutable-attributes), make sure that ID tokens contain identifiers that are immutable [and can't be reused](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-non-reusable-attributes).

### Include context information in ID tokens

Instead of granting workloads unconditional access to Google Cloud resources, customers might want to restrict access so that a workload can only obtain Google credentials when certain additional criteria are met.

To let customers configure such restrictions, include additional claims in the ID token that contain context information. Examples for context information include:

  * information about the user that owns or started the workload
  * the reason and way the workload was started
  * the request that is currently being handled by the workload



Customers can use these claims to configure [attribute conditions](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions) or in [principal identifiers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#impersonation).

### Limit ID token lifetime to 60 minutes

ID tokens have a limited lifetime determined by the `exp` claim. When a workload uses an ID token to perform a token exchange, Workload Identity Federation validates the ID token's `exp` claim and issues an STS token that is valid for as long as the input token, but at most for 1 hour.

Using ID tokens that are valid for longer than one hour has no effect on Workload Identity Federation, but might increase risks if an ID token is accidentally leaked. Using a lifetime significantly below 1 hour can help reduce such risks, but might lead to frequent token exchanges and reduced performance.

## What's next

  * Read more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
