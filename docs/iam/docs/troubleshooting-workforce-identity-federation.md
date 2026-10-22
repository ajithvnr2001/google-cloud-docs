---
url: https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation/
title: Troubleshoot Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:00.329309+00:00
---

# Troubleshoot Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Troubleshoot Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve common issues with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

## Inspect the IdP response

This section shows you how to inspect the response from your identity provider (IdP) to troubleshoot issues listed in this document.

### Browser-based sign-in

To inspect the response returned by your IdP, generate a [HAR file](https://en.wikipedia.org/wiki/HAR_\(file_format\)) using a tool of your choice. For example, you can use [Google Admin Toolbox HAR Analyzer](https://toolbox.googleapps.com/apps/har_analyzer/), which provides instructions for generating a HAR file and the tools to upload and analyze it.

**Important:** If you are requesting the HAR file from your users, request that they clean up any personally identifiable information (PII) and cookies from the HAR file before sending it.

### SAML

To inspect the SAML IdP response, perform the following steps:

  1. Locate the value of the `SAMLResponse` request parameter in the HAR file that is logged against the URL with path `/signin-callback`.
  2. Decode it using a tool of your choice—for example, you can use [Google Admin Toolbox Encode/Decode](https://toolbox.googleapps.com/apps/encode_decode/).



### OIDC

To inspect the OIDC IdP response, perform the following steps. This approach doesn't work with code flow.

  1. Look for the `id_token` request parameter in the HAR file that is logged against a URL with the path `/signin-callback`.
  2. Decode it using a JWT debugging tool of your choice.



###  gcloud CLI 

To inspect the response from your IdP when using the gcloud CLI, copy the contents of the file that you passed in the `--credential-source-file` flag when running the `gcloud iam workforce-pools create-cred-config` command, then perform the following steps:

### SAML

Decode the SAML IdP response using a tool of your choice—for example, you can use [Google Admin Toolbox Encode/Decode](https://toolbox.googleapps.com/apps/encode_decode/).

### OIDC

Decode the OIDC IdP response using a JWT debugging tool of your choice.

## Review logs

To determine whether Google Cloud is communicating with your IdP and review transaction information, you can inspect the Cloud Audit Logs logs.

To see log examples, see [Example audit logs](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workforce-identity).

## Workforce pool and provider management errors

This section provides suggestions to fix common errors that you might encounter when managing pools and providers.

### General attribute mapping errors

To troubleshoot workforce identity pool provider attribute mapping issues, do the following:

  * Inspect the attributes, otherwise known as claims, in your IdP configuration. Verify how your attribute mappings convert IdP attributes into Google Cloud attributes and how your conditions evaluate those attributes to allow or deny access in the Google Cloud console.

    1. Ensure that you have the **IAM Workforce Pool Editor** (`roles/iam.workforcePoolEditor`) role.
    2. To enable the browser-based sign-in flow for Workforce Identity Federation, add `https://auth.cloud.google/signin-callback/locations/global/workforcePools/POOL_ID/providers/PROVIDER_ID` to your IdP's list of allowed redirect URIs.
    3. In the Google Cloud console, go to **Workforce Identity Pools**.

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)
    4. From the list of pools, click the name of the pool you want to verify.
    5. In the **Workforce pool details** page, click the name of the IdP you want to verify. 
    6. In the **Provider Details** page, click **Debug IdP token**.
    7. In the **Sign in** dialog, sign in to your IdP as a test user.

The **Validate your provider attributes** page displays the mapped attributes and the result of your attribute condition. 

The **Mapped attributes from your IdP token** section displays how Google attributes, such as `google.subject`, are populated from your IdP's token based on your mapping configuration. An error icon appears if a mapping is incorrect. 

The **Attribute condition** section shows the boolean result of your condition. If the condition evaluates to `false`, the sign-in is blocked. 

To view the full assertion token, click **View full token**. This shows the raw JSON object from your IdP. Reference a top-level property in your mappings using the format `assertion.PROPERTY_NAME`. 

To correct any errors, you can edit the configuration: 

    1. In the **Validate your provider attributes** page, click ** edit  Edit**. 
    2. Make the necessary changes.
    3. To start a new test and see the updated results, click **Save and refetch token**. 
  * Inspect tokens that are generated from your IdP. To learn how to generate a token from your IdP, consult your IdP's documentation.

  * Review Workforce Identity Federation detailed audit logging in Cloud Audit Logs.




Detailed audit logging logs authentication and authorization errors alongside claims that were received by Workforce Identity Federation.

You can enable detailed audit logging when you create your workforce identity pool provider. To enable detailed audit logging, add the `--detailed-audit-logging` flag when you create your workforce identity pool provider.

### Permission denied

This error occurs when the user attempting to configure Workforce Identity Federation doesn't have the role IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`).

### INVALID_ARGUMENT: Missing OIDC web single sign-on config

The following error occurs when the `web-sso-response-type` and `web-sso-assertion-claims-behavior` fields are not set when creating an OIDC workforce identity pool provider:
    
    
    ERROR: (gcloud.iam.workforce-pools.providers.create-oidc) INVALID_ARGUMENT: Missing OIDC web single sign-on config.
    

To resolve this error, follow the steps in the [Create a provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#create_a_provider) section to set the fields appropriately when you create the OIDC workforce identity pool provider.

### Rate limit exceeded, please try again later

This error occurs when you have reached your quota limit for workforce pool resources. Contact your Google Cloud account representative to request a quota increase.

## Sign-in errors

This section provides suggestions to fix common errors that a Workforce Identity Federation user might encounter when they sign in.

### Common sign-in errors

#### The given credential is rejected by the attribute condition

This error occurs when the [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) that is set on the workforce identity pool provider was not met.

For example, consider the following attribute condition:

### SAML
    
    
    'gcp-users' in assertion.attributes.groups
    

### OIDC
    
    
    'gcp-users' in assertion.groups
    

In this case, you see the error if the list of groups sent in the `groups` attribute by your IdP doesn't contain `gcp-users`.

To resolve this error, perform the following steps:

  1. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider) that was used to sign in, and check that the `attributeCondition` is correct. For information on operations that are supported in conditions, see the [Language Definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

  2. Follow the steps in inspect the IdP response to see the attributes that are returned by the IdP, and confirm if the attribute condition is well-formed and accurate.

  3. Sign in to your IdP's admin console, and check if the IdP attributes referenced in the attribute condition are set up correctly. If necessary, consult your IdP's documentation.




#### The mapped attribute must be of type STRING

This error occurs for a SAML workforce identity pool provider when the attribute specified in the error message is expected to be a single-valued STRING, but it is mapped to a list in the [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).

For example, consider a SAML workforce identity pool provider that has the attribute mapping, `attribute.role=assertion.attributes.userRole`. In a SAML assertion, an `Attribute` can have multiple `AttributeValue` tags as shown in the example that follows. Thus, all SAML attributes are considered lists, so `assertion.attributes.userRole` is a list.
    
    
    <saml:Attribute Name="userRole">
        <saml:AttributeValue>
          security-admin
        </saml:AttributeValue>
        <saml:AttributeValue>
          user
        </saml:AttributeValue>
    </saml:Attribute>
    

In this example, you might see the following error:
    
    
    The mapped attribute 'attribute.role' must be of type STRING
    

To resolve this issue, perform the following steps:

  1. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider) that was used to sign in, and identify the IdP attribute that is set in the `attributeMapping`. Check the attribute against the attribute presented in the error message. In the previous example, an IdP attribute called `userRole` is mapped to the `role` attribute and the `role` attribute appears in the error sample.

  2. When updating the attribute mapping, consider the following:

**Note:** Only `google.groups` accepts a list.
     * If the attribute that causes the error is list valued, identify an alternative, stable, string-valued attribute. Then, update the attribute mapping to use it by referencing its first item. For the previous example, if `myRole` was identified as the alternative single-valued IdP attribute, then the attribute mapping is the following:
           
           attribute.role=assertion.attributes.myRole[0]
           

     * Alternatively, if the attribute is known to be single-valued, update the attribute mapping to use the first item from the list. For the previous example, if `userRole` contains only one role, you can use the following mapping:
           
           attribute.role=assertion.attributes.userRole[0]
           

     * To derive a single-valued, stable identifier from the list, see [Language Definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md) and update your attribute mapping accordingly.




See the inspect the IdP response section to see the response that is returned by the IdP.

#### Could not obtain a value for google.subject from the given credential

This error occurs when the required claim `google.subject` couldn't be mapped using the [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) that you set in your workforce identity pool provider configuration.

To resolve this error, perform the following steps:

  1. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider), and inspect the `attributeMapping`. Identify the mapping that is configured for `google.subject`. If the mapping is not correct, update the workforce identity pool provider.

  2. See the inspect the IdP response section to see the response returned by the IdP. Inspect the value of the attribute from IdP response that is mapped to `google.subject` in your attribute mappings.

If the value is empty or incorrect, log in to your IdP's admin console, and inspect the configured attributes. For the attributes, check if your affected user has corresponding data in your IdP. Update your IdP configuration to correct the attributes or user information accordingly.

  3. Retry sign-in.




#### Size of mapped attributes exceeds the limit

The following error occurs when a federated user attempts to sign in:
    
    
    The size of the entire mapped attributes exceeds the 16 KB limit.
    

To resolve this issue, ask your IdP administrator to reduce the number of attributes that your IdP emits. Your IdP only needs to emit attributes that are needed to federate users to Google Cloud. To learn more about attribute mapping limits, see [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).

For example, if your IdP emits a large number of `google.groups` that are mapped attributes in your workforce identity pool provider, a sign-in attempt can fail. Ask your administrator to restrict the number of groups that your IdP emits.

#### Count of groups exceeds the limit

The following error occurs when a federated user attempts to sign in:
    
    
    The current count of GROUPS_COUNT mapped attribute google.groups exceeds the GROUPS_COUNT_LIMIT count limit. Either modify your attribute mapping or the incoming assertion to produce a mapped attribute that has fewer than GROUPS_COUNT_LIMIT groups.
    

This error includes the following values:

  * `GROUPS_COUNT`: the count of groups that the IdP emits

  * `GROUPS_COUNT_LIMIT`: Google Cloud's count limit for groups




This error occurs when the number of groups emitted by the IdP exceeds Google Cloud's limit. Groups are mapped to Google Cloud using the attribute `google.groups`.

To resolve this issue, ask your administrator to reduce the number of groups that your IdP emits. Your IdP only needs to emit groups that are used to federate users to Google Cloud. Learn more about groups-related limits in [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).

#### 400\. That's an error

This error occurs when either the request wasn't received as expected or it was malformed.

To resolve this error, perform the following steps:

  1. Follow the steps in [Inform your users how to sign in](https://docs.cloud.google.com/iam/docs/workforce-console-sso#inform-users) section to verify if you are following the correct steps to sign in.

  2. Compare your workforce identity pool provider configuration with your IdP configuration.




### Extra attributes sign-in errors

This section provides suggestions to fix errors when using [extra attributes](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups#extra-attributes).

#### Login fails when extra attributes are configured

If you have configured extra attributes, any configuration issue—such as an incorrect client ID, client secret, or issuer URI—causes the sign-in attempt to fail.

To resolve this error, perform the following steps:

  1. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider) and verify that the client ID and issuer URI are correct.
  2. Verify that the client secret is valid and hasn't expired.
  3. In your IdP, verify that the application has the [required permissions](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups#extra-attributes).



#### Groups from SAML or OIDC assertion are ignored

When extra attributes are configured, Workforce Identity Federation ignores any group information provided directly in the SAML or OIDC claims. Instead, it only uses the groups fetched using the backchannel (for example, using the Microsoft Graph API).

If your users aren't seeing the expected groups, ensure that the groups are correctly retrieved using the backchannel and that any [attribute filters](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups#extra-attributes) are configured correctly.

### OIDC sign-in errors

This section provides suggestions to fix OIDC specific errors that a Workforce Identity Federation user might encounter when they sign in.

#### Error connecting to the given credential's issuer

This error occurs when an OIDC workforce identity pool provider is unable to reach the OIDC discovery document or JWKS URI.

To resolve this error, perform the following steps:

  1. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider), and inspect the configured `issuerUri`. Construct the discovery document URL by appending `/.well-known/openid-configuration` to your issuer URI. For example, if your `issuerUri` is `https://example.com`, the discovery document URL would be `https://example.com/.well-known/openid-configuration`.

  2. Open the discovery document URL in an incognito browsing window.

     1. If the URL doesn't open or the browser displays a `404` error, consult your IdP's documentation to identify the correct issuer URI. If necessary, update the `issuerUri` in your workforce identity pool provider.

If your IdP is running on premises, consult your IdP's documentation to provision it for access over the internet.

     2. If the URL opens, check for the following conditions:

        1. Check that the URL doesn't redirect too many times before serving the discovery document. If it does, consult with your IdP's administrator to remedy the issue.
        2. Check the IdP response time. Consult with your IdP administrator to reduce the response latency.
        3. The opened discovery document should be in the [JSON](https://en.wikipedia.org/wiki/JSON) format.
        4. Look for a `jwks_uri` field in the JSON.

           1. Verify that the associated URL value also opens.
           2. Verify that the URL satisfies the conditions as described earlier in this guide.
     3. Retry sign-in.




### SAML sign-in errors

This section provides suggestions to fix SAML specific errors that a Workforce Identity Federation user might encounter when they sign in.

#### Failed to verify the signature in SAMLResponse

This error occurs for a SAML workforce identity pool provider when the signature on the IdP response cannot be verified using any of the X.509 certificates provided in the IdP metadata XML that you configured in your workforce identity pool provider. A common cause of this error is that the verification certificate on your IdP was rotated, but you did not update the workforce identity pool provider configuration with the latest IdP metadata XML file.

To resolve this error, perform the following steps:

  1. Optional: follow the steps in inspect the IdP response to see the response returned by the IdP and locate the `X509Certificate` field in it. [Describe the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#describe_a_provider) that you used to sign in, and inspect the `X509Certificate` field present in the `idpMetadataXml` value that is set on the workforce identity pool provider. Compare the certificate with the one seen in the response returned by your IdP. The certificates must match.

  2. Log in to your IdP's admin console, and download the latest metadata XML.

  3. Update the workforce identity pool provider with the downloaded IdP metadata XML.

  4. Retry sign-in.




#### Recipient in SAML assertion is not set to the correct ACS URL

This error occurs for a SAML workforce identity pool provider when the IdP response contains an incorrect value for the `Recipient` field on the `SubjectConfirmationData` tag.

To resolve this error, update the `Recipient URL` / `Redirect URL` or the equivalent field in your IdP's configuration to use the redirect URL described in the [Set up redirect URLs in your IdP](https://docs.cloud.google.com/iam/docs/workforce-console-sso#set-up-redirect), and retry sign-in.

Follow the steps in inspect the IdP response to see the response returned by the IdP, and confirm that the `Recipient` field is correct.

For example, for the workforce identity pool provider `locations/global/workforcePools/example-pool/providers/example-provider`, the `Recipient` containing the redirect URL appears in the IdP's SAML response as follows:
    
    
    <SubjectConfirmationData Recipient="https://auth.cloud.google/signin-callback/locations/global/workforcePools/example-pool/providers/example-provider"
    

#### SAMLResponse destination does not match RP callback URL

This error occurs for a SAML workforce identity pool provider when the IdP response contains an incorrect value for the `Destination` field on the `Response` tag.

To resolve this error, update the `Destination URL` / `Redirect URL` or the equivalent field in your IdP's configuration to use the redirect URL described in [Set up redirect URLs in your IdP](https://docs.cloud.google.com/iam/docs/workforce-console-sso#set-up-redirect).

Follow the steps in inspect the IdP response to see the response returned by the IdP and confirm that the `Destination` field is correct.

For example, for a workforce identity pool provider `locations/global/workforcePools/example-pool/providers/example-provider`, the `Destination` containing redirect URL would appear in the IdP's SAML response as follows:
    
    
    <Response Destination="https://auth.cloud.google/signin-callback/locations/global/workforcePools/example-pool/providers/example-provider"
    

#### Invalid assertion: missing or empty NameID

This error occurs when the SAML response received from your IdP doesn't contain the `NameId` field or it has an empty value.

To resolve this error, consult your IdP documentation to configure it to send the `NameID` which is the subject of a SAML assertion, typically the user who is being authenticated.

**Note:** `NameID` is required even if you decide to map a different attribute to `google.subject` in the attribute mapping.

Follow the steps in inspect the IdP response to see the response returned by the IdP and the `NameID` that is set on it.

#### All `<AudienceRestriction>`s should contain the SAML RP entity ID

This error occurs when the `AudienceRestriction` tags in the SAML response from your IdP doesn't set an `Audience` tag with a value that represents the entity ID of the workforce identity pool provider.

To resolve this error, perform the following steps:

  1. Consult your IdP documentation on how to configure the audience in the `AudienceRestriction` tags that it sends in the SAML response. Typically, the audience is configured by setting up the `Entity ID` or `Audience` field in your IdP configuration. See [Create a workforce identity pool provider's](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#saml) SAML section to see the value `SP Entity ID` that should be set.

  2. After updating your IdP configuration, retry sign-in.




Follow the steps in inspect the IdP response to see the response returned by the IdP and the `AudienceRestriction`s that are set on it.

### SCIM sign-in errors

This section describes how to resolve SCIM-specific errors that a Workforce Identity Federation user might encounter when they sign in.

#### SCIM tenant couldn't be found

This error occurs when a user tries to sign in using a workforce identity pool provider that's configured to use SCIM, but no SCIM tenant is configured for that provider.

When this occurs, users get the following error when they try to sign in:

`There was an issue signing in with your identity provider.`

To resolve this error, do the following for your identity provider:

  1. Configure a SCIM tenant and token on Google Cloud ([Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra#configure-scim-tenant-token-gcp) | [Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta#configure-scim-tenant-token-gcp)).
  2. Link the provider to a SCIM tenant ([Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra#update-provider-enable-scim) | [Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta#update-provider-enable-scim)).



#### Sign-in fails when SCIM usage is enabled for users and groups ([Preview](https://cloud.google.com/products#product-launch-stages))

When `--scim-usage` is set to `enabled-for-users-groups`, sign-in attempts might fail with specific error messages:

  * **SCIM user not found or inactive:**

    * **Error:** `The workforce identity pool provider is configured to use identity information that is provided using SCIM, but a SCIM User could not be associated with the google.subject from the given credential.` or `... the SCIM User associated with the google.subject from the given credential is not active.`
    * **Cause:** The user hasn't synced to Google Cloud by using SCIM, the mapped `google.subject` in the provider does not match the SCIM user mapping, or the user is marked `active: false` in the IdP.
    * **Resolution:** In your IdP, verify that the user is provisioned by using SCIM, ensure their status is active, and verify that the provider attribute mapping and SCIM tenant claim mapping for `google.subject` refer to the same identity.
  * **CEL evaluation or claim mapping error:**

    * **Error:** `Failed to map attributes from the given credential with SCIM Tenant config.`
    * **Cause:** A CEL expression in `--claim-mapping` is invalid or failed during evaluation.
    * **Resolution:** Review your SCIM tenant's `--claim-mapping` expressions to ensure valid CEL syntax and supported attribute names.
  * **Mapped attribute size limits exceeded:**

    * **Error:** `The size of SCIM mapped attribute google.display_name exceeds the 100 bytes limit.` or `The size of entire SCIM mapped attributes exceeds the 16 kB limit.`
    * **Cause:** An individual mapped attribute exceeded its size limit (for example, 100 bytes for `google.display_name`, 32 bytes for `google.posix_username`, 127 bytes for `google.subject`), or the total serialized mapped claims exceeded 16 kB.
    * **Resolution:** Adjust your SCIM tenant claim mappings or update IdP attribute values to remain within the allowed limits.



## SCIM provisioning and synchronization errors

This section describes how to resolve issues with SCIM provisioning and synchronization in Workforce Identity Federation.

### SCIM token authentication failure (HTTP 401 or 403)

This error occurs when identity provider (IdP) logs report authentication failures (`HTTP 401 Unauthorized` or `HTTP 403 Forbidden`). Common causes include the following:

  * The SCIM token is missing, invalid, or expired.
  * The SCIM token contains extra spaces.
  * The request lacks the `Authorization: Bearer <TOKEN>` header.
  * The SCIM token has insufficient permissions.



To resolve this issue, do the following:

  1. In your IdP provisioning configuration, verify that the SCIM token matches the secret token generated in Google Cloud without extra whitespace.
  2. If the token is lost or invalid, generate a new SCIM token:

**Note:** Each SCIM tenant supports a maximum of two SCIM tokens. If you already have two tokens, you must delete an existing token before creating a new one. For more information, see SCIM token creation fails.
         
         gcloud iam workforce-pools providers scim-tenants tokens create SCIM_TOKEN_ID \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --provider="PROVIDER_ID" \
             --scim-tenant="SCIM_TENANT_ID" \
             --location="global"
         

Replace the following:

     * `SCIM_TOKEN_ID`: an ID for the new SCIM token.
     * `WORKFORCE_POOL_ID`: the ID of the workforce identity pool.
     * `PROVIDER_ID`: the ID of the workforce pool provider.
     * `SCIM_TENANT_ID`: the ID of the SCIM tenant.
  3. Update the secret token in your IdP configuration.




### Rate limit exceeded (HTTP 429 Too Many Requests)

This error occurs when IdP request rates exceed the SCIM tenant quota. By default, write and read requests are limited to 3,000 requests per SCIM tenant per organization per minute, which is equivalent to 50 queries per second (QPS). For more information, see [Quotas and limits](https://docs.cloud.google.com/iam/quotas#quotas).

To resolve this issue, do the following:

  1. Check that your IdP synchronization request rate is within quota limits.
  2. In the Google Cloud console, go to **IAM & Admin** > **Quotas** and filter for `iamscim.googleapis.com` to monitor quota usage.
  3. If you need higher throughput, request a quota increase in the Google Cloud console.



### SCIM tenant creation fails

This error occurs when the `gcloud iam workforce-pools providers scim-tenants create` command fails.

Common causes include the following:

  * A SCIM tenant already exists in the workforce pool. Each workforce pool supports only one SCIM tenant.
  * A recently deleted SCIM tenant is still in its 30-day soft-delete period.
  * You don't have the IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`) role.
  * The `--claim-mapping` flag contains unsupported Common Expression Language (CEL) expressions.



To resolve this issue, do the following:

  1. Verify that you have the IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`) role.
  2. List existing SCIM tenants to check if a tenant already exists:
         
         gcloud iam workforce-pools providers scim-tenants list \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --provider="PROVIDER_ID" \
             --location="global"
         

Replace the following:

     * `WORKFORCE_POOL_ID`: the ID of the workforce identity pool.
     * `PROVIDER_ID`: the ID of the workforce pool provider.
  3. If a previously deleted tenant is soft-deleted, permanently delete it using the `--hard-delete` flag:
         
         gcloud iam workforce-pools providers scim-tenants delete SCIM_TENANT_ID \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --provider="PROVIDER_ID" \
             --location="global" \
             --hard-delete
         

Replace `SCIM_TENANT_ID` with the ID of the SCIM tenant.

  4. Ensure that `--claim-mapping` uses only supported CEL expressions. For more information, see [Claim mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim#mapping-examples).




### SCIM token creation fails

This error occurs when the `gcloud iam workforce-pools providers scim-tenants tokens create` command fails.

Common causes include the following:

  * The SCIM tenant already has the maximum of two SCIM tokens.
  * You don't have the IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`) role.



To resolve this issue, do the following:

  1. Verify that you have the IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`) role.
  2. List existing SCIM tokens to check if the limit of two tokens has been reached:
         
         gcloud iam workforce-pools providers scim-tenants tokens list \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --provider="PROVIDER_ID" \
             --scim-tenant="SCIM_TENANT_ID" \
             --location="global"
         

Replace the following:

     * `WORKFORCE_POOL_ID`: the ID of the workforce identity pool.
     * `PROVIDER_ID`: the ID of the workforce pool provider.
     * `SCIM_TENANT_ID`: the ID of the SCIM tenant.
  3. If the SCIM tenant already has two tokens, delete an unused or invalid token:
         
         gcloud iam workforce-pools providers scim-tenants tokens delete SCIM_TOKEN_ID \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --provider="PROVIDER_ID" \
             --scim-tenant="SCIM_TENANT_ID" \
             --location="global"
         

Replace `SCIM_TOKEN_ID` with the ID of the SCIM token to delete.

  4. After deleting the token, retry creating the new SCIM token.




### Duplicate attribute mapping conflict (HTTP 409 Conflict)

This error occurs when identity provider (IdP) logs report an `HTTP 409 Conflict` during synchronization because the IdP sends duplicate values for `google.subject` or `google.group`, or non-unique `userName` or `displayName` values.

To resolve this issue, do the following:

  1. In your IdP administrator console, verify that attributes mapped to `google.subject` and `google.group` produce non-overlapping values.
  2. Ensure that every user has a unique `userName` and every group has a unique `displayName`.



### Microsoft Entra ID PATCH requests fail

This error occurs when user updates or PATCH requests from Microsoft Entra ID fail because the **Tenant URL** is missing the `?aadOptscim062020` query parameter, which is required for RFC-compliant PATCH requests.

To resolve this issue, do the following:

  1. In Microsoft Entra ID, go to your enterprise application and select **Provisioning** > **Manage provisioning** > **Admin Credentials**.
  2. In the **Tenant URL** field, append `?aadOptscim062020` to the base URI:
         
         https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID?aadOptscim062020
         

Replace `SCIM_TENANT_UID` with the unique ID of your SCIM tenant.

  3. Click **Test Connection** , and then save the configuration.




### User or group-based access or sharing not working

This issue occurs when synchronized users can't access Google Cloud resources, or when sharing notebooks in Gemini Notebook Enterprise or agents in the Gemini Enterprise app fails.

Common causes include the following:

  * Silent synchronization failures or delays from the IdP.
  * Inconsistent claim mappings between the provider (`--attribute-mapping`) and the SCIM tenant (`--claim-mapping`).
  * Changes in the IdP to attributes mapped to `google.subject` or `google.group`. Google Cloud expects values mapped to these attributes to be immutable.
  * SCIM usage isn't enabled for groups on the provider.



To resolve this issue, do the following:

  1. **Verify synchronization and membership** : Confirm that users, groups, and group memberships synced successfully to Google Cloud:

     * **Verify user sync** :
           
           curl -G -H "Authorization: Bearer SCIM_TOKEN" \
             "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Users" \
             --data-urlencode 'filter=userName eq "USER_NAME"'
           

     * **Verify group sync** :
           
           curl -G -H "Authorization: Bearer SCIM_TOKEN" \
             "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Groups" \
             --data-urlencode 'filter=displayName eq "GROUP_NAME"'
           

     * **Verify group membership** : Confirm that a user is a member of a group:
           
           curl -G -H "Authorization: Bearer SCIM_TOKEN" \
             "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Groups" \
             --data-urlencode 'filter=id eq "GROUP_ID" and members eq "USER_ID"'
           

If the user is a member of the group, the response returns `totalResults: 1`. If the user is not a member, the response returns `totalResults: 0`.

Replace the following:

     * `SCIM_TOKEN`: your SCIM secret token.
     * `SCIM_TENANT_UID`: the unique ID of your SCIM tenant.
     * `USER_NAME`: the username of the synchronized user.
     * `GROUP_NAME`: the display name of the synchronized group.
     * `GROUP_ID`: the SCIM ID of the synchronized group, returned in the `id` field of the group query response.
     * `USER_ID`: the SCIM ID of the synchronized user, returned in the `id` field of the user query response.
  2. **Check claim mappings** : Ensure that the attribute mapped to `google.subject` in the provider (for example, `google.subject=assertion.email.lowerAscii()`) matches the identity mapped in the SCIM tenant (for example, `google.subject=user.emails[0].value.lowerAscii()`). Because claim mappings are immutable, if mappings are inconsistent, you must [hard-delete the SCIM tenant](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim#considerations) and recreate it with the correct mapping.

  3. **Ensure identifier immutability** : Verify that the IdP attributes mapped to `google.subject` and `google.group` haven't changed. Google Cloud treats values mapped to these attributes as [immutable identifiers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim#behavior-limitations). If an attribute value changed in your IdP, revert the change in your IdP, or permanently delete the affected user or group from your IdP and recreate it with the new value so that the identifier matches what Google Cloud expects.

  4. **Enable SCIM group usage** : Update your provider to enable SCIM for groups:
         
         gcloud iam workforce-pools providers update-oidc PROVIDER_ID \
             --workforce-pool="WORKFORCE_POOL_ID" \
             --location="global" \
             --scim-usage="enabled-for-groups"
         

Replace the following:

     * `PROVIDER_ID`: the ID of the workforce pool provider.
     * `WORKFORCE_POOL_ID`: the ID of the workforce identity pool.



### Changes made in the IdP are delayed or not reflecting

This issue occurs when IdP updates to users, group memberships, or deletions don't immediately appear in Google Cloud.

Because SCIM is push-based, updates depend on your IdP sync schedule. For example, Microsoft Entra ID synchronizes approximately every 40 minutes.

To resolve this issue, do the following:

  1. Wait for the next scheduled sync cycle from your IdP.
  2. To apply changes immediately, trigger an on-demand sync in your IdP administrator console.



### User provisioning fails due to email format

This error occurs when specific users fail to sync to Google Cloud, and your identity provider (IdP) logs report an HTTP `400 Bad Request` with an `invalidValue` SCIM error.

Google Cloud SCIM requires exactly one work email per user. Provisioning fails if the IdP sends multiple emails or the email is not of type `work`.

To resolve this issue, configure your IdP attribute mapping to send only the primary work email.

### Group updates fail (HTTP PUT not supported)

This error occurs when group updates fail because the client uses HTTP `PUT`, which isn't supported. The Google Cloud SCIM API supports only HTTP `PATCH` for group updates.

To resolve this issue, configure your IdP or custom client to use HTTP `PATCH` for group updates.

### Provider update fails with mutually exclusive configurations

This error occurs when provider creation or update fails with one of the following messages:

  * `Select one of scim_usage - ENABLED_FOR_USERS_GROUPS or extra_attributes_oauth2_client, but not both.`
  * `Select one of scim_usage or extended_attributes_oauth2_client, but not both.`



Setting `--scim-usage=enabled-for-users-groups` ([Preview](https://cloud.google.com/products#product-launch-stages)) is mutually exclusive with Extra Attributes (`extra_attributes_oauth2_client`) and Extended Attributes (`extended_attributes_oauth2_client`).

To resolve this issue, remove the conflicting Extra or Extended Attributes configuration from the provider, or change the `--scim-usage` setting.

## Cloud OAuth API token exchange errors

When a token exchange request fails, the Cloud OAuth API returns an HTTP `400 Bad Request` or `401 Unauthorized` status with an OAuth 2.0 error JSON response (RFC 6749). The `error` field indicates one of the following error codes:

Error code | Description | Remediation  
---|---|---  
`invalid_request` |  The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.  |  Verify that all required URL-encoded parameters (`grant_type`, `code` or `refresh_token`, `redirect_uri`) are provided.   
`invalid_client` |  Client authentication failed.  |  Verify that your registered OAuth `client_id` and `client_secret` match, that the OAuth client is enabled for your workforce identity pool, and that your `Authorization: Basic` header is Base64-encoded correctly.   
`invalid_grant` |  The provided authorization code or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.  |  Ensure the code or token has not expired or been exchanged previously.   
`unauthorized_client` |  The authenticated OAuth client is not authorized to use the requested `grant_type`.  |  Verify that your OAuth client registration allows authorization code or refresh token grants.   
`unsupported_grant_type` |  The authorization grant type is not supported by the authorization server.  |  Set `grant_type` to `authorization_code` or `refresh_token`.   
`invalid_scope` |  The requested scope is invalid, unknown, malformed, or exceeds the scopes granted by the resource owner.  |  Verify that the requested scopes match those configured on the OAuth client and are valid for your application.   
`resource_exhausted` |  The request exceeded the Cloud OAuth API token exchange quota.  |  Check your API usage in the Google Cloud console or request a quota increase.   
  
## Cloud OAuth user info and groups errors

When a request to the `/userinfo` or `/groups` endpoint fails, the Cloud OAuth API returns an HTTP `400 Bad Request`, `401 Unauthorized`, or `403 Forbidden` status with an OAuth 2.0 Bearer token error response (RFC 6750 / OpenID Connect Core). The `error` field indicates one of the following error codes:

Error code | HTTP status | Description | Remediation  
---|---|---|---  
`invalid_request` | `400 Bad Request` / `401 Unauthorized` |  The request is missing the required `Authorization` header or the header is malformed (for example, it does not start with `Bearer`).  |  Verify that the `Authorization: Bearer ACCESS_TOKEN` header is formatted correctly.   
`invalid_token` | `401 Unauthorized` |  The provided access token is invalid, expired, or revoked.  |  Refresh the access token using the `refresh_token` grant or repeat the authorization code flow.   
`insufficient_scope` | `403 Forbidden` |  The access token lacks the required `openid` scope, or the token's tenant does not match the organization specified in the organization-scoped endpoint URL.  |  Verify that the token was requested with the required `openid` scope and that you are calling the correct endpoint.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
