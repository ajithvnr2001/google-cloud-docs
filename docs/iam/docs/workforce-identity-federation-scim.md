---
url: https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim/
title: SCIM provisioning for Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:21.433701+00:00
---

# SCIM provisioning for Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  SCIM provisioning for Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

If your identity provider (IdP) supports [System for Cross-domain Identity Management (SCIM)](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management), you can configure it to provision and manage users and groups in Google Cloud.

**Important:** SCIM provisioning applies only to Gemini Enterprise and Looker ([Preview](https://cloud.google.com/products#product-launch-stages)).

## Capabilities

Workforce Identity Federation SCIM support provides the following capabilities:

  * **Identity synchronization:** Syncs users and groups from your external IdP to Google Cloud to maintain a holistic view of workforce identities.
  * **Primary source for claims:** When SCIM is enabled for a workforce provider, Google Cloud uses the synchronized SCIM users and groups as the source of truth for both user attributes and group memberships for IAM policy evaluation.
  * **Identity autocomplete:** Enables user and group autocomplete when granting access and sharing resources (such as Notebooks and Agents) in Gemini Enterprise.



## Considerations

**Important:** Because SCIM is push-based from your IdP, Google Cloud doesn't actively pull data or check connection health. If the connection between your IdP and Google Cloud breaks silently, identity data can become stale. 

In extended session length (ESL) workflows lasting up to 90 days, a deactivated user might retain access until the next successful sync or session expiration. To prevent unauthorized access, continuously monitor and audit your SCIM synchronization health. 

When you use Workforce Identity Federation SCIM support, the following considerations apply:

  * You must set up a workforce identity pool and provider before configuring a SCIM tenant.
  * Each workforce identity pool supports only one SCIM tenant, linked to a single provider. You cannot enable SCIM usage (`--scim-usage`) on any other provider in the same pool. To configure a new SCIM tenant in the same workforce identity pool, you must first delete the existing one. To delete a SCIM tenant, use one of the following methods: 
    * **Soft delete (default):** Deleting a SCIM tenant initiates a 30-day soft-delete period. During this time, the tenant is hidden and cannot be used, and you cannot create a new SCIM tenant in the same workforce identity pool.
    * **Hard delete:** To permanently and immediately delete a SCIM tenant, use the `--hard-delete` flag with the delete command. This action is irreversible and lets you create a new SCIM tenant in the same workforce identity pool immediately without waiting for the 30-day retention period. Alternatively, you can create a new workforce identity pool and a new SCIM tenant or use a workforce identity pool that hasn't previously been configured with a SCIM tenant.
  * **SCIM usage modes (`--scim-usage`):**
    * **`enabled-for-groups` (Gemini Enterprise):** Uses SCIM-synced groups for IAM authorization and policy evaluation. User attributes continue to be sourced from login tokens. Only `google.subject` and `google.group` mappings are evaluated.
    * **`enabled-for-users-groups` (Looker) ([Preview](https://cloud.google.com/products#product-launch-stages)):** Uses SCIM-synced user and group data as the source of claims for IAM authorization and OAuth sign-in workflows. Evaluates `google.subject`, `google.group`, and all configured user claims (such as `google.display_name`, `google.profile_photo`, `google.email`, `google.posix_username`, and custom `attribute.KEY`).
  * **Mutual exclusivity:** Setting `--scim-usage=enabled-for-users-groups` ([Preview](https://cloud.google.com/products#product-launch-stages)) is mutually exclusive with Extra Attributes (`extra_attributes_oauth2_client`) and Extended Attributes (`extended_attributes_oauth2_client`).
  * When you use SCIM, you map attributes in both the workforce identity pool provider and the SCIM tenant. The `google.subject` attribute must uniquely refer to the same identities. You specify `google.subject` in the workforce identity pool provider by using the `--attribute-mapping` flag and in the SCIM tenant using the `--claim-mapping` flag. Mapping non-unique identity values can cause Google Cloud to treat different IdP identities as the same identity. As a result, access that's granted to one user or group identity can extend to others, but revoking access from one might not remove it from all.
  * If you enable SCIM usage on a provider without an attached SCIM tenant, sign-in attempts fail because Google Cloud can't find a SCIM tenant for that provider.
  * **Uniqueness enforcement:** Google Cloud validates and enforces uniqueness on attributes mapped to `google.subject` (users) and `google.group` (groups) in a SCIM tenant. If the mapped attributes provisioned by your IdP result in duplicate values for `google.subject` or `google.group` during synchronization, then provisioning fails with an HTTP `409 Conflict` error. If a mapped attribute evaluates to null or empty, provisioning fails with an HTTP `400 Bad Request` error.
  * **Attribute size limits:** The maximum size for serialized mapped user attributes (excluding `google.group`) is 16 kB. If mapped attributes exceed this limit, sign-in attempts fail.
  * **SCIM token limit:** Each SCIM tenant supports a maximum of two SCIM tokens (for example, to support zero-downtime token rotation). If you have two tokens, delete an existing token before creating a new one.
  * The SCIM API (`iamscim.googleapis.com`) is subject to rate quotas that differ from standard IAM resource API quotas. By default, write and read requests are limited to 3,000 requests per SCIM tenant per organization per minute. For more information, see [Quotas and limits](https://docs.cloud.google.com/iam/quotas#quotas).



## Claim mapping

When you configure SCIM, you define claim mappings (`--claim-mapping`) in the SCIM tenant to map SCIM user and group attributes to Google attributes.

### Supported Google Cloud attributes for claim mapping

The following table lists the Google Cloud attributes that you can map in your SCIM tenant (`--claim-mapping`) using Common Expression Language (CEL): 

Google Cloud attribute | Requirement | Description | Supported expressions and limits  
---|---|---|---  
`google.subject` | Mandatory |  Unique identifier for the authenticating user. The underlying IdP attribute used to populate `google.subject` must be identical across both the provider mapping (`--attribute-mapping`) and the SCIM tenant (`--claim-mapping`). If these mappings are inconsistent, users might be able to sign in but won't be recognized as members of SCIM-provisioned groups. | Restricted to the following base expressions (or with `.lowerAscii()`): 

  * `user.externalId`
  * `user.userName`
  * `user.emails[0].value`

Maximum length: 127 bytes. **Note:** This mapping is immutable once the SCIM tenant is created; to update it, you must hard-delete and recreate the SCIM tenant.  
`google.group` | Mandatory for SCIM groups | Unique identifier for group membership synced using SCIM. | Restricted to the following base expressions (or with `.lowerAscii()`): 

  * `group.externalId`
  * `group.displayName`

**Note:** This mapping is immutable once the SCIM tenant is created; to update it, you must hard-delete and recreate the SCIM tenant.  
`google.display_name` | Optional | An attribute that sets the name of the signed-in user in the Google Cloud console. It can't be used in IAM allow policies. | Maps to a string attribute (such as `user.displayName` or `user.name.formatted`). Maximum length: 100 bytes.  
`google.profile_photo` | Optional | A URL of the user's thumbnail photo that is visible as their profile picture in the Google Cloud console. It can't be used in IAM allow policies. | Must evaluate to a valid URL string (such as `user.photos.filter(p, p.type == 'thumbnail')[0].value` or `user.photos[0].value`).  
`google.email` | Optional | An attribute used to map email addresses from the IdP to products integrated by using Workforce Identity Federation OAuth client integration. It can't be used in IAM allow policies. | Maps to an email attribute (such as `user.emails.filter(e, e.type == 'work')[0].value` or `user.emails[0].value`).  
`google.posix_username` | Optional | A unique POSIX-compliant username string used for SSH-in-browser and OS Login with Workforce Identity Federation. This attribute can't be used in IAM allow policies. | The maximum length is 32 characters.  
`attribute.KEY` | Optional |  Custom attributes from your IdP that you can use to define your authorization strategy in an IAM allow policy. Replace KEY with the attribute name you want to use. For example, you can define a custom attribute such as `costcenter = "1234"` and refer to it by using `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workforcePools/WORKFORCE_POOL_ID/attribute.costcenter/1234`. Granting access to this principal identifier gives access to all identities configured in the IdP with that cost center. | Up to 50 custom attribute mapping rules. Maximum size per rule: 256 characters.  
  
### Behavior based on provider SCIM usage (`--scim-usage`)

The evaluation of SCIM claim mappings depends on the `--scim-usage` mode configured on the workforce identity pool provider:

  * **`enabled-for-groups` (Gemini Enterprise):** Only `google.subject` and `google.group` mappings are evaluated. Any additional user claim mappings in `--claim-mapping` are ignored.
  * **`enabled-for-users-groups` (Looker) ([Preview](https://cloud.google.com/products#product-launch-stages)):** Evaluates `google.subject`, `google.group`, and all configured user claims (such as `google.display_name`, `google.profile_photo`, `google.email`, `google.posix_username`, and custom `attribute.<var>KEY</var>`).



### Example mappings for subject consistency

As described in Supported attributes for claim mapping, the underlying IdP attribute used to populate `google.subject` must be identical across both the provider mapping (`--attribute-mapping`) and the SCIM tenant (`--claim-mapping`). The following table shows reference examples:

Google attribute | Workforce identity pool provider mapping | SCIM tenant mapping (SCIM)  
---|---|---  
`google.subject` | `assertion.oid` (Entra ID) | `user.externalId`  
`google.subject` | `assertion.sub` (Okta) | `user.externalId`  
`google.subject` | `assertion.preferred_username` | `user.userName`  
`google.subject` | `assertion.preferred_username.lowerAscii()` | `user.userName.lowerAscii()`  
`google.subject` | `assertion.email` | `user.emails[0].value`  
`google.subject` | `assertion.email.lowerAscii()` | `user.emails[0].value.lowerAscii()`  
  
## Supported and unsupported endpoints

The IAM SCIM service (`iamscim.googleapis.com`) implements the [SCIM 2.0 protocol (RFC 7644)](https://datatracker.ietf.org/doc/html/rfc7644) and serves requests at your SCIM tenant's `baseUri`:
    
    
    https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID
    

In this URI, `SCIM_TENANT_UID` is the unique identifier of your SCIM tenant.

The IAM SCIM service supports the following standard SCIM protocol endpoints relative to the tenant `baseUri`:

  * `/Users`: manage user resources. Supported operations: `Create`, `Get`, `Update`, `Delete`, `Patch`, and `Put`.

  * `/Groups`: manage group resources. Supported operations: `Create`, `Get`, `Update`, `Delete`, and `Patch`. The `PUT` method isn't supported for groups.

  * `/Schemas`: retrieve schema information.

  * `/ServiceProviderConfig`: retrieve the service provider configuration.


**Note:** SCIM integration with Okta does not support `Import Users` and `Import Groups` features from Google Cloud to Okta.

The following SCIM protocol endpoints aren't supported:

  * `/Me`

  * `/Bulk`

  * `/Search`

  * `/ResourceTypes`




## Limitations

The following sections describe the limitations and deviations of the Workforce Identity Federation SCIM implementation from the SCIM specifications (RFC 7643 and 7644).

### Protocol feature limitations

  * **Filter support:** When you list users or groups using the `/Users` or `/Groups` endpoints, filter expressions only support the `eq` (equals) operator. You can combine multiple `eq` filters with `and`. Other SCIM filter operators, such as `co` (contains) or `sw` (starts with), aren't supported.

  * **Pagination:** The IAM SCIM API does not support standard pagination for listing users or groups.

    * `startIndex`: this parameter is always `1`. The API returns up to 100 results regardless of the value that you provide for `startIndex`.

    * `itemsPerPage`: the maximum number of resources that are returned in a single response is 100.

    * `totalResults`: the API does not return the actual total count of matching resources. The `totalResults` field in the response is always equal to the number of items that are returned in that response, with a maximum of 100.

  * **Get Group and list Groups without filter:** `GetGroup` and `ListGroups` APIs return an empty member list. To retrieve members for a specific group, use the `ListGroups` API with a member filter.

  * **Non-compliant JSON response with invalid tokens:** Requests that contain an invalid API token return an `HTTP 401` status code from Google Cloud. The response is not valid JSON as required by the SCIM specification.




### SCIM behavior limitations

  * **Immutable identifiers:** The values of SCIM attributes that are mapped to `google.subject` or `google.group` are treated as immutable identifiers within Google Cloud. If you need to change these values, you must permanently delete the user or group from your IdP and then recreate it with the new value.

  * **Unique and non-empty identifiers:** Google Cloud enforces uniqueness on values mapped to `google.subject` and `google.group` in a SCIM tenant. Syncing mapped attributes that result in duplicate values for `google.subject` or `google.group` fails with an HTTP `409 Conflict` error. Mapped attributes that evaluate to null or empty fail with an HTTP `400 Bad Request` error.

  * **Single email requirement:** For successful SCIM synchronization, each user must have exactly one email address of type `work`. Provisioning or updates will fail if your IdP sends multiple emails or if the single email provided is not of type `work`.

  * **Case-insensitive transformations:** Limited Common Expression Language (CEL) transformations are supported for SCIM claim mappings. Only `.lowerAscii()` is supported for case-insensitive comparisons for `user.userName` and `user.emails[0].value`.




### Attribute limitations

The following sections describe the attribute support for users, groups, and the enterprise user schema extension.

#### User attributes

The following table lists user attributes and their availability in Workforce Identity Federation claims:

Attribute | Sub-attributes | Supported in SCIM Provisioning | Limitations | Supported in `--claim-mapping`  
---|---|---|---|---  
`userName` | N/A | Yes | N/A | Yes  
`name` | `formatted`, `familyName`, `givenName`, `middleName`, `honorificPrefix`, `honorificSuffix` | Yes | N/A | Yes  
`displayName` | N/A | Yes | N/A | Yes  
`nickName` | N/A | Yes | N/A | Yes  
`profileUrl` | N/A | Yes | N/A | Yes  
`title` | N/A | Yes | N/A | Yes  
`userType` | N/A | Yes | N/A | Yes  
`preferredLanguage` | N/A | Yes | N/A | Yes  
`locale` | N/A | Yes | N/A | Yes  
`timezone` | N/A | Yes | N/A | Yes  
`active` | N/A | Yes | N/A | Yes  
`password` | N/A | No | N/A | No  
`emails` | `display`, `type`, `value`, `primary` | Yes | Only the `work` email type is supported. | Yes  
`phoneNumbers` | `display`, `type`, `value`, `primary` | Yes | N/A | Yes  
`ims` | `display`, `type`, `value` | Yes | N/A | Yes  
`photos` | `display`, `type`, `value` | Yes | N/A | Yes  
`addresses` | `formatted`, `streetAddress`, `locality`, `region`, `postalCode`, `country` | Yes | N/A | Yes  
`groups` | N/A | No | N/A | No  
`entitlements` | `display`, `type`, `value` | Yes | N/A | Yes  
`roles` | `type`, `value` | Yes | `display` isn't supported. | Yes  
`x509Certificates` | `type`, `value` | Yes | `display` isn't supported. | No  
  
#### Group attributes

The following table lists group attributes and their availability in Workforce Identity Federation claims:

Attribute | Supported sub-attributes | Supported in `--claim-mapping`  
---|---|---  
`displayName` | N/A | Yes  
`externalId` | N/A | Yes  
`members` | `value`, `type`, `$ref`, `display` | No  
  
#### Enterprise user schema extension attributes

The following table details the support for the enterprise user schema extension:

Attribute | Supported sub-attributes | Supported in `--claim-mapping`  
---|---|---  
`employeeNumber` | N/A | Yes  
`costCenter` | N/A | Yes  
`organization` | N/A | Yes  
`division` | N/A | Yes  
`department` | N/A | Yes  
`manager` | `value`, `$ref`, `displayName` | Yes (`$ref` is supported in SCIM provisioning only, not in `--claim-mapping`)  
  
## What's next

  * [Configure SCIM in Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra)
  * [Configure SCIM in Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta)
  * [Troubleshoot SCIM provisioning](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#scim-provisioning-errors)
  * [IAM SCIM audit logging](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-iamscim)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
