---
url: https://docs.cloud.google.com/iam/docs/troubleshooting-workload-identity-federation/
title: Troubleshoot Workload Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:21.126431+00:00
---

# Troubleshoot Workload Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/troubleshooting-workload-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Troubleshoot Workload Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes resolutions for common [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) errors.

## Google Cloud API does not accept the credential issued from `SecurityTokenService`

Access tokens returned by the [`SecurityTokenService`](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token) API are [federated access tokens](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens). Although most Google Cloud APIs support identity federation, certain API methods might have limitations. For a list of limitations, see [Identity federation: products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

If you encounter the following error, you might be attempting to use a federated access token with a service that doesn't support them.
    
    
    {
      "error": {
        "code": 401,
        "message": "Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.",
        "status": "UNAUTHENTICATED",
      }
    }
    

To resolve this error, exchange the federated access token for an unrestricted access token by calling [`GenerateAccessToken`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken). For more information, see [Obtaining short-lived credentials with identity federation](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation).

## Allowlist an identity provider for use with Workload Identity Federation

If you attempt to configure a disallowed identity provider as a workload identity pool provider, you encounter the following error:
    
    
    FAILED_PRECONDITION: Precondition check failed.
    - '@type': type.googleapis.com/google.rpc.PreconditionFailure
      violations:
      - description: "Org Policy violated for value: '{PROVIDER}'."
        subject: orgpolicy:projects/{PROJECT}/locations/global/workloadIdentityPools/{POOL}
        type: constraints/iam.workloadIdentityPoolProviders
    

To resolve this issue, follow the directions on [Restrict identity provider configuration](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#restrict) to allowlist the identity provider for use with Workload Identity Federation.

## Input JWK is not in a valid json format

If you are configuring an OIDC provider and you receive the error `Input JWK is not in a valid json format`, it can be because endpoints that are secured with self-signed certificates aren't supported by Google Cloud. Specifically, the `x5c` and `x5t` fields aren't supported and must be removed from the OIDC JWK.

To resolve issues with your JWK, do the following:

  1. Edit your JWK and remove the `x5c` (X.509 Certificate Chain) and `x5t` (X.509 Certificate SHA-1 Thumbprint) fields.
         
         {
           "kty": "RSA",
           "use": "sig",
           "kid": "example-key-id",
           "alg": "RS256",
           "n": "base64url-modulus",
           "e": "AQAB"
         }
         

  2. Verify that the remaining JWK fields are properly formatted as described in the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html#JWKS).

  3. Configure the OIDC provider with the updated JWK.




## Error connecting to the given credential's issuer

If you receive the following error, it might be because Google Cloud is unable to fetch your IdP's OIDC metadata document or JWKS:
    
    
    {
      "error": "invalid_grant",
      "error_description":"Error connecting to the given credential's issuer."
     }
    

This error usually occurs because the endpoints aren't configured to be reachable from the public internet. To resolve this error, check that the OIDC endpoint is publicly available and compliant with the OIDC specification. For more information, see [Preparing the external identity provider](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation#oidc).

If you still receive the error, check that the token issuer, the `iss` claim in the token correct.

## The given AWS request doesn't contain all the required headers

If you receive the following error while requesting a token from the [`SecurityTokenService`](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token) API, it's because the `headers` field in your AWS `GetCallerIdentity` token is missing a required header or includes unsupported headers:
    
    
    {
      "error": "invalid_grant",
      "error_description": "The given AWS request doesn't contain all the required headers."
    }
    

The `headers` field of a `GetCallerIdentity` token must include only the following HTTP request headers:

  * `Authorization`: The [request signature](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).
  * `host`: The hostname of the `url` field; for example, `sts.amazonaws.com`.
  * `x-amz-date`: The time that you send the request, formatted as an [ISO 8601 Basic](https://docs.aws.amazon.com/general/latest/gr/sigv4_elements.html#sigv4_elements_date) string.
  * `x-goog-cloud-target-resource`: The full resource name of the workload identity pool provider.
  * `x-amz-security-token`: The session token. Only required if you are using [temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html).



This error also occurs if your Signature Version 4 signer includes additional headers, such as `x-amz-content-sha256`, in the signed request. To resolve this issue, make sure that your `GetCallerIdentity` request has an empty body and that both the `headers` field and the `SignedHeaders` field of the signed request include only the supported headers. For more information, see [Authenticate a workload using the REST API](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#rest).

## Mapped google.subject claim exceeds the 127 bytes limit

If you receive the following error, it's because the incoming credentials received by the [`SecurityTokenService`](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token) API generate a `google.subject` claim that exceeds the character limit:
    
    
    {
      "error": "invalid_request",
      "error_description":"The size of mapped attribute google.subject exceeds the 127 bytes limit. Either modify your attribute mapping or the incoming assertion to produce a mapped attribute that is less than 127 bytes."
     }
    

To resolve this issue, use the [`extract` function](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#extract) to remove unnecessary characters and extract a unique subject identifier from a longer claim, for example:
    
    
    google.subject=assertion.sub.extract('/users/{sub_claim}')
    

## Error 429 Too Many Requests

If you receive the error `429 Too Many Requests`, while requesting a token from the [`SecurityTokenService`](https://docs.cloud.google.com/iam/docs/reference/sts/rest/v1/TopLevel/token) API, it means that your Google Cloud project has exceeded its rate quota limit for the API.

The error includes a message similar to the following:
    
    
    {
      "error": "quota_exceeded",
      "error_description":"The request was throttled due to rate limit: sts.googleapis.com/requests. Please retry after a few seconds."
     }
    

To resolve this issue, identify the `sts.googleapis.com/requests` metric name provided in the error message, locate the corresponding metric name in the [IAM Quota page](https://console.cloud.google.com/iam-admin/quotas), confirm that the usage percentage exceeds the quota, and then request a quota increase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
