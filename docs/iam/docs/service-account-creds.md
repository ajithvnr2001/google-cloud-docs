---
url: https://docs.cloud.google.com/iam/docs/service-account-creds/
title: Service account credentials \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:06.386394+00:00
---

# Service account credentials  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/service-account-creds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Service account credentials Stay organized with collections  Save and categorize content based on your preferences. 

Like any principal, a service account can authenticate itself to Google, obtain an OAuth 2.0 access token, and call Google APIs. However, this process works differently for service accounts than for users.

Service accounts authenticate by doing one of the following:

  * Obtaining short-lived credentials
  * Using a service account key to sign a JSON Web Token (JWT) and exchange it for an access token



## Short-lived service account credentials

The most secure way to authenticate as a service account is to obtain short-lived credentials for the service account in the form of an OAuth 2.0 access token. By default, these tokens expire after 1 hour.

Short-lived service account credentials are useful for scenarios where you need to grant limited access to resources for trusted service accounts. They also create less risk than long-lived credentials, such as service account keys.

In many cases, these credentials are obtained automatically—you don't need to create or manage them yourself. Here are some examples:

  * If you run a Google Cloud CLI command, and you include the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account), then the gcloud CLI creates short-lived credentials for the service account and runs the command with those credentials.
  * If you [attach a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts) to a Compute Engine virtual machine (VM) instance, then workloads on that instance can use the Cloud Client Libraries to access Google Cloud services. The Cloud Client Libraries use Application Default Credentials (ADC) to obtain short-lived credentials for the service account.

For details about this process, see [Authenticating applications using service account credentials](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#authenticate-with-service-account).

  * If you configured [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), then the Cloud Client Libraries can use credentials from your identity provider to generate short-lived service account credentials.




You can also use the Service Account Credentials API to [create short-lived credentials manually](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct). For example, you could create a service that gives users short-lived service account credentials to let them temporarily access Google Cloud resources.

The Service Account Credentials API can create the following types of credentials:

  * OAuth 2.0 access tokens
  * OpenID Connect (OIDC) ID tokens
  * Self-signed JSON Web Tokens (JWTs)
  * Self-signed binary blobs



For more information, see [Creating short-lived service account credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).

### Interpreting audit logs

Cloud Audit Logs help you answer the questions "who did what, where, and when?" for your Google Cloud resources.

When you use short-lived credentials to impersonate a service account, most Google Cloud services create log entries that show the following identities:

  * The service account that the short-lived credentials are impersonating
  * The identity that created the short-lived credentials



You can use these log entries to identify the principal that created the short-lived credentials, as well as the service account that the principal impersonated.

**Note:** Some Google Cloud services, including App Engine and Google Kubernetes Engine, do not log the identity that created the short-lived credentials. 

For examples of audit log entries that show service account impersonation, see [Impersonating a service account to access Google Cloud](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#auth-as-service-account).

### Self-impersonation

_Self-impersonation_ is when you use a service account's own credentials to generate a new credential for the service account.

The Service Account Credentials API prohibits the following kinds of self-impersonation:

  * Using a short-lived credential for a service account to generate a new [access token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) for the service account.

[Self-signed JSON Web Tokens (JWTs)](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) are the exception to this rule—you can use a self-signed JWT for a service account to generate a new access token for the service account.

  * Using a short-lived credential for a service account to sign a binary object (blob) or JWT that can be used to call the following APIs:

    * [Identity and Access Management API](https://docs.cloud.google.com/iam/docs/reference/rest)
    * [Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest)
    * [OAuth 2.0 API](https://developers.google.com/identity/protocols/oauth2)



Google Cloud prohibits this kind of self-impersonation because it lets malicious actors refresh stolen tokens indefinitely.

If you try to use self-impersonation in one of the prohibited ways, you might encounter the following error:
    
    
    FAILED_PRECONDITION: You can't create a token for the same service account that
    you used to authenticate the request.
    

If you encounter this error, try using different credentials to generate the new short-lived credential for your service account—for example, your end-user credentials or a different service account's credentials.

## Service account keys

Each service account is associated with a public/private RSA key pair. The Service Account Credentials API uses this internal key pair to create short-lived service account credentials, and to sign blobs and JSON Web Tokens (JWTs). This key pair is known as the _Google-owned and managed key pair_.

In addition, you can create multiple public/private RSA key pairs, known as _user-managed key pairs_ , and use the private key to authenticate with Google APIs. This private key is known as a _service account key_.

Always store your service account keys in a secure location. If you don't store your keys securely, then bad actors can find the keys and use them to access the resources that the service account can access. We strongly recommend storing your keys in a hardware-based or software-based key store. For more guidance on storing service account keys securely, see [Protecting against privilege escalation](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#privilege-escalation). 

### Google-owned and managed key pairs

Google-owned and managed key pairs are used by the Service Account Credentials API, and by Google Cloud services such as App Engine and Compute Engine, to generate short-lived credentials for service accounts.

Google-owned and managed keys that are actively used for signing are rotated regularly according to [security best practices](https://docs.cloud.google.com/iam/docs/key-rotation#timing). The rotation process is probabilistic; usage of the new key will gradually ramp up and down over the key's lifetime.

The private key in a Google-owned and managed key pair is always held in escrow, and you can never access it directly.

The public key in a Google-owned and managed key pair is publicly accessible, so that anyone can verify signatures that are created with the private key. You can access the public key in several different formats:

  * X.509 certificate: `https://www.googleapis.com/service_accounts/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL`
  * JSON Web Key (JWK): `https://www.googleapis.com/service_accounts/v1/jwk/SERVICE_ACCOUNT_EMAIL`
  * Raw format: `https://www.googleapis.com/service_accounts/v1/metadata/raw/SERVICE_ACCOUNT_EMAIL`



If you download and cache the public key, we recommend caching it for at most 24 hours to ensure that you always have the current key. Regardless of when you retrieve the public key, it will be valid for at least 24 hours after you retrieve it.

### User-managed key pairs

You can create user-managed key pairs for a service account, then use the private key from each key pair to authenticate with Google APIs. This private key is known as a _service account key_.

The Cloud Client Libraries can use service account keys to obtain an OAuth 2.0 access token automatically. You can also use a service account key to sign a JWT manually, then use the signed JWT to request an access token. For details, see [Using OAuth 2.0 for server to server applications](https://developers.google.com/identity/protocols/oauth2/service-account).

**Caution:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

Each service account can have up to 10 service account keys. Google stores only the public portion of a user-managed key pair.

There are a few different ways to create a user-managed key pair for a service account:

  * Use the IAM API to [create a user-managed key pair automatically](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating). Google generates a public/private key pair; stores only the public key; and returns the private key to you.
  * Create a user-managed key pair yourself, then [upload only the public key](https://docs.cloud.google.com/iam/docs/keys-upload). Google never sees the private key.



User-managed keys are extremely powerful credentials. To limit the use of user-managed keys, you can enforce the following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) in an organization, project, or folder:

  * `constraints/iam.disableServiceAccountKeyCreation`: Prevents principals from creating user-managed service account keys.
  * `constraints/iam.disableServiceAccountKeyUpload`: Prevents principals from uploading a public key for a service account.



**Note** : If your organization was created on or after May 3, 2024, these constraints are enforced by default. 

If you enforce these constraints because you are using [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), consider using the [organization policy constraints for workload identity federation](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#constraints) to specify which identity providers are allowed.

#### Expiry times for user-managed keys

By default, when you create a user-managed service account key, the key never expires. You can change this default by setting an expiry time for all newly created keys in your project, folder, or organization. An expiry time specifies the number of hours for which a newly created key is valid.

Use expiry times when you need temporary access to a system that requires a service account key. For example, use expiry times when you're doing the following:

  * Developing code in a non-production environment for an application that can only authenticate with service account keys
  * Using a third-party tool that can only authenticate with service account keys



Avoid using expiry times for these scenarios:

  * Production workloads. In production, an expired service account key could cause an accidental outage. Instead, use keys that do not expire, and manage their lifecycle with key rotation.
  * Non-production workloads that need permanent access, such as a continuous integration (CI) pipeline.
  * Key-rotation systems that prevent a key from being used after a specified amount of time. To learn about recommended key rotation strategies, see [Service account key rotation](https://docs.cloud.google.com/iam/docs/key-rotation).



To help prevent outages, we recommend that you do not set an expiry time unless the `constraints/iam.disableServiceAccountKeyCreation` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) has been in place for an extended period of time. When you set an expiry time, you must also stop enforcing the `constraints/iam.disableServiceAccountKeyCreation` constraint. For details about this constraint, see [Limit lifetime of service account keys](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#limit_key_expiry).

**Important:** If the `constraints/iam.disableServiceAccountKeyCreation` constraint was not in place, you must work closely with the users of the project, folder, or organization to confirm that none of their existing resources require permanent service account keys. If a resource requires permanent service account keys, and you set an expiry time, you are likely to cause an outage.

To set an expiry time, do the following:

  1. Identify the project, folder, or organization where you want to set an expiry time for service account keys.
  2. [Add an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints) that enforces the [`constraints/iam.serviceAccountKeyExpiryHours` constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#limit_key_expiry). After you enforce this constraint for your project, folder, or organization, the expiry time applies to all newly created service account keys within that parent resource. Existing keys are not affected.



Expiry times are measured in hours. As a best practice, use short expiry times, such as 8 hours; 24 hours (1 day); or 168 hours (7 days). Short expiry times help ensure that your team has a well-tested process for updating keys. Start with the shortest expiry time that meets your needs, and increase it only if necessary.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
