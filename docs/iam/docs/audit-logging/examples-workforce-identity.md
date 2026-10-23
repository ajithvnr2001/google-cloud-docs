---
url: https://docs.cloud.google.com/iam/docs/audit-logging/examples-workforce-identity/
title: Example logs for Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:18.532930+00:00
---

# Example logs for Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/examples-workforce-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Example logs for Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This page shows examples of the audit logs that are generated when you use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation). With Workforce Identity Federation, you can allow third-party identities to access Google Cloud resources, without using a service account key.

**Note:** Each example shows only the most relevant fields in the log entries.

For more information about enabling and viewing audit logs, see [IAM audit logging](https://docs.cloud.google.com/iam/docs/audit-logging).

IAM can generate audit logs when you create and manage workforce pools. To enable audit logs when managing workforce pools, you must [enable audit logs for Data Access activity](https://docs.cloud.google.com/iam/docs/audit-logging#enabling_audit_logging) for the following API:

  * Identity and Access Management (IAM) API (enable log type "Admin Read")



To configure audit logs for the token exchange process or Google Cloud console (federated) sign-in, you must also [enable audit logs for Data Access activity](https://docs.cloud.google.com/iam/docs/audit-logging#enabling_audit_logging) for the following APIs:

  * Security Token Service (enable log type "Admin Read")
  * Cloud OAuth API (enable log type "Admin Read")

**Note:** The audit logs are generated at the organization level.

## Logs for creating a workforce pool

The following example shows a log entry for creating a workforce pool. In this example, the user `sam@example.com` created a workforce pool with the ID `my-pool` under the organization with the ID `123456789012`.
    
    
    {
      "logName": "organizations/123456789012/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "sam@example.com",**
        },
        "methodName": "google.iam.admin.v1.WorkforcePools.CreateWorkforcePool",
        **"resourceName" : "locations/global/workforcePools/my-pool",**
        "serviceName": "iam.googleapis.com",
        "request": {
          "@type": "type.googleapis.com/google.iam.admin.v1.CreateWorkforcePoolRequest",
          **"workforcePool" : {
            "parent": "organizations/123456789012"
          },
          "workforcePoolId": "my-pool"**
        }
      },
      "resource": {
        "type": "audited_resource"
      }
    }

## Logs for exchanging an IdP token for a federated token

After you set up your workforce identity pool and workforce identity pool provider, you can create a token for your identity provider (IdP) and exchange it for a federated token.

After you enable Cloud Audit Logs for Data Access activity, IAM generates an audit log entry each time a principal exchanges a token. The log entry includes the following fields:

  * `protoPayload.authenticationInfo.principalSubject`: The subject of the IdP token. 
    * For OIDC IdPs, this field contains the value of the `sub`, or subject, claim from the OIDC token.
    * For SAML IdPs, this field contains the value of the `NameID` sub-attribute of the `Subject` attribute in the SAML assertion.
  * `protoPayload.metadata.mapped_principal`: The subject of the token, using IAM syntax to identify the principal:
        
        principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/IDENTIFIER
        

  * `protoPayload.resourceName`: The workforce pool provider that the token is associated with.




### Successful token exchange with Security Token Service

The following example shows an audit log entry for a request to exchange a token using Security Token Service (`sts.googleapis.com`). In this example, an OIDC token is exchanged for a federated token:
    
    
    {
      "logName": "organizations/123456789012/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        **"authenticationInfo" : {
          "principalSubject": "b6112abb-5791-4507-adb5-7e8cc306eb2e"
        },
        "metadata": {
          "mapped_principal": "principal://iam.googleapis.com/locations/global/workforcePools/oidc-pool/subject/a1234bcd-5678-9012-efa3-4b5cd678ef9a"
        },**
        "methodName": "google.identity.sts.v1.SecurityTokenService.ExchangeToken",
        **"resourceName" : "locations/global/workforcePools/oidc-pool/providers/oidc-provider",**
        "serviceName": "sts.googleapis.com",
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.v1.SecurityTokenService.ExchangeTokenRequest",
          "audience": "//iam.googleapis.com/locations/global/workforcePools/oidc-pool/providers/oidc-provider",
          "grantType": "urn:ietf:params:oauth:grant-type:token-exchange",
          "requestedTokenType": "urn:ietf:params:oauth:token-type:access_token",
          "subjectTokenType": "urn:ietf:params:oauth:token-type:id_token"
        }
      },
      "resource": {
        "type": "audited_resource"
      }
    }

### Failed token exchange: Too many groups

The following example log describes a token exchange that failed because the number of groups exceeded the maximum of 400.

To log attributes that are received by Workforce Identity Federation, you must enable detailed audit logging when you create your workforce identity pool provider.

To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors).

In the following example, `mappedAttributes` contains attributes that were received from the IdP, including a list of groups. In this case, the number of groups exceeded the Workforce Identity Federation limit.
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "code": 3,
          "message": "The current count of 800 mapped attribute google.groups exceeds the 400 count limit. Either modify your attribute mapping or the incoming assertion to produce a mapped attribute that is less than 400."
        },
        "authenticationInfo": {
          "principalSubject": "3Kn-kJQal4N-WXVjxMqcOF1tQcCdBliu97lV-2P-Khc"
        },
        "requestMetadata": {
          "callerIp": "2601:647:4680:9140:9d68:88c9:cab9:a908",
          "callerSuppliedUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
          "requestAttributes": {
            "time": "2025-04-09T18:32:34.979311Z",
            "auth": {}
          },
          "destinationAttributes": {}
        },
        "serviceName": "sts.googleapis.com",
        "methodName": "google.identity.sts.SecurityTokenService.WebSignIn",
        "authorizationInfo": [
          {
            "permission": "sts.identityProviders.checkLogging",
            "granted": false,
            "permissionType": "ADMIN_READ"
          }
        ],
        "resourceName": "locations/global/workforcePools/my-pool/providers/my-provider",
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.SecurityTokenService.WebSignInRequest",
          "provider": "//iam.googleapis.com/locations/global/workforcePools/my-pool/providers/my-provider",
          "host": "auth-staging.corp.cloud.google"
        },
        "metadata": {
          "mappedAttributes": {
            "google.subject": "3Nk-kJQal4N-WXVjxMqcOF1tQcCdBliu97lV-2P-Khc",
            "google.providerId": "my-provider-id",
            "google.groups": "[group-claim-1, group-claim-2, ..., group-claim-800]"
          }
        }
      },
      "insertId": "-llnhbmck3a",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "sts.googleapis.com",
          "method": "google.identity.sts.SecurityTokenService.WebSignIn"
        }
      },
      "timestamp": "2025-04-09T18:32:34.208412Z",
      "severity": "ERROR",
      "logName": "organizations/123456789012/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2025-04-09T18:32:35.059811619Z"
    }
    

## Logs for signed and encrypted SAML assertions

This section describes the Cloud Audit Logs log entries that Security Token Service creates when it attempts to verify signed SAML assertions or decrypt encrypted assertions that are sent from your IdP.

For Workforce Identity Federation, the pertinent log entry looks similar to the following:
    
    
    "keyInfo": [
      {
        "use": "verify"
        **"fingerprint": "3C:B2:47:F8:A5:9A:8A:52:BD:1C:BC:96:B5:45:C1:8D:A7:F1:73:2D"**
      },
      {
        "use": "decrypt"
        **"resourceName": "//iam.googleapis.com/locations/global/workforcePools/ WORKFORCE_POOL_NAME/providers/PROVIDER_NAME/keys/KEY_NAME"**
      }
    ]
    

This output includes the following values:

  * `fingerprint`: the hexadecimal representation of the SHA-256 hash of the X.509 certificate that was used to verify the signature on the SAML credential. The X.509 certificate is extracted from the SAML XML metadata that is attached to the workforce identity pool provider.
  * `resourceName`: the resource name of the workforce identity pool provider key that was used to decrypt the encrypted SAML assertion. This field is present only if identity federation receives an encrypted SAML response from your IdP.



## Logs for calling Google Cloud APIs with the federated token

After you exchange the IdP's token for a federated token, you can use the federated token to call Google Cloud APIs. Some of the methods you call might generate audit logs.

The following example shows an audit log entry for a request to list the Cloud Storage buckets in a project using a federated token.
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalSubject" : "principal://iam.googleapis.com/locations/global/workforcePools/oidc-pool/subject/kalani@altostrat.com"**
        },
        "methodName": "storage.buckets.list",
        "serviceName": "storage.googleapis.com",
      },
      "resource": {
        "type": "gcs_bucket"
      }
    }

## Logs for Google Cloud console (federated) sign-in

After you [set up your workforce identity pools](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers) and their IdPs, users can sign in to Google Cloud using [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso).

### Logs for successful sign-in

This section provides an example Cloud Audit Logs entry that is logged as a result of a successful sign-in. In this example, the user, `user@example.com`, signs in using a provider `locations/global/workforcePools/my-pool/providers/my-provider`. In this case, the following Cloud Audit Logs entry is generated:
    
    
    {
      "logName": "organizations/my-organization-id/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalSubject" : "user@example.com",**
        },
        "serviceName": "sts.googleapis.com",
        **"methodName" : "google.identity.sts.SecurityTokenService.WebSignIn",**
        **"resourceName" : "locations/global/workforcePools/my-pool/providers/my-provider",**
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.SecurityTokenService.WebSignInRequest",
          **"provider" : "//iam.googleapis.com/locations/global/workforcePools/my-pool/providers/my-provider",**
          "continueUrl": "https://console.cloud.google",
          "host": "http://auth.cloud.google",
        },
        "metadata": {
           **"mappedPrincipal" : "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",**
        }
      },
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "sts.googleapis.com",
          "method": "google.identity.sts.SecurityTokenService.WebSignIn",
        }
      },
    }

The Cloud Audit Logs entry for SAML providers can additionally contain signing key information in the metadata field.
    
    
    {
      "metadata": {
        "mappedPrincipal": "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",
        **"keyInfo" : [
          {
            "use": "verify",
            "fingerprint": "AE:CK:LM:EF:LK:OG:EH:IJ:KN:AL:OM:AD:NO",
          }
        ],**
      }
    }

### Logs for failed sign-in

This section provides an example Cloud Audit Logs entry that is logged as a result of a failed sign-in. In this example, the user, `user@example.com` attempts to sign-in using a provider `locations/global/workforcePools/my-pool/providers/my-provider` but is denied access due to an attribute condition not being satisfied. In this case, the following Cloud Audit Logs entry is generated:
    
    
    {
      "logName": "organizations/my-organization-id/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalSubject" : "user@example.com",**
        },
        **"status" : {
          "code": 3,
          "message": "The given credential is rejected by the attribute condition.",
        },**
        "serviceName": "sts.googleapis.com",
        **"methodName" : "google.identity.sts.SecurityTokenService.WebSignIn",**
        **"resourceName" : "locations/global/workforcePools/my-pool/subject/user@example.com",**
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.SecurityTokenService.WebSignInRequest",
          **"provider" : "//iam.googleapis.com/locations/global/workforcePools/my-pool/providers/my-provider",**
          "host": "http://auth.cloud.google",
        },
        "metadata": {
          **"mappedPrincipal" : "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",**
        }
      },
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "sts.googleapis.com",
          "method": "google.identity.sts.SecurityTokenService.WebSignIn",
        }
      },
    }

**Note:** Failed sign-in attempts are logged only for the cases where we were able to parse your Identity provider's response.

### Logs for sign-out

This section provides an example Cloud Audit Logs entry that is logged as a result of a sign-out event. In this example, the user, `user@example.com`, who is signed in using a provider `locations/global/workforcePools/my-pool/providers/my-provider` initiates a sign-out. In this case, the following Cloud Audit Logs entry is generated:

**Note:** The Cloud Audit Logs entry is written only for the initiator of the sign-out action.
    
    
    {
      "logName": "organizations/my-organization-id/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalSubject" : "user@example.com",**
        },
        "serviceName": "sts.googleapis.com",
        **"methodName" : "google.identity.sts.SecurityTokenService.WebSignOut",**
        **"resourceName" : "locations/global/workforcePools/my-pool/providers/my-provider",**
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.SecurityTokenService.WebSignOutRequest",
          **"provider" : "//iam.googleapis.com/locations/global/workforcePools/my-pool/providers/my-provider",**
          "host": "http://auth.cloud.google"
        },
        "metadata": {
          **"mappedPrincipal" : "principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com",**
        }
      },
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "sts.googleapis.com",
          "method": "google.identity.sts.SecurityTokenService.WebSignOut"
        }
      },
    }

## Logs for signing in with OAuth flow

After you set up your workforce identity pool and workforce identity pool provider, you can access Google Cloud resources by using the OAuth flow.

After you enable Cloud Audit Logs for Data Access audit logs activity, IAM generates an audit log entry each time a principal uses the OAuth flow to sign in. The log entry includes the following fields:

  * `protoPayload.authenticationInfo.principalSubject`: The subject of the IdP token. 
    * For OIDC IdPs, this field contains the value of the `sub`, or subject, claim from the OIDC token.
    * For SAML IdPs, this field contains the value of the `NameID` sub-attribute of the `Subject` attribute in the SAML assertion.
  * `protoPayload.metadata.mapped_principal`: The subject of the token, using IAM syntax to identify the principal:
        
        principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/IDENTIFIER
        

  * `protoPayload.resourceName`: The workforce pool provider that the token is associated with.




The following example shows an audit log entry for a request to exchange a token. In this example, the principal is federated by using an OIDC provider:
    
    
    {
      "logName": "organizations/123456789012/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        **"authenticationInfo" : {
          "principalSubject": "b6112abb-5791-4507-adb5-7e8cc306eb2e"
        },
        "metadata": {
          "mapped_principal": "principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/IDENTIFIER"
        },**
        "methodName": "google.identity.sts.v1.SecurityTokenService.ExchangeOauthToken",
        **"resourceName" : "locations/global/workforcePools/POOL_ID/providers/WORKFORCE_PROVIDER_ID",**
        "serviceName": "sts.googleapis.com",
        "request": {
          "@type": "type.googleapis.com/google.identity.sts.v1.SecurityTokenService.ExchangeOauthTokenRequest",
          "grantType": "authorization_code",
        }
      },
      "resource": {
        "type": "audited_resource"
      }
    }

## What's next

  * [Configure and view the audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) for IAM.
  * Get more information about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * Set up [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation) using workforce identity pools.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
