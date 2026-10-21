---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings/
title: LDAPSSettings \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:41.945769+00:00
---

# LDAPSSettings  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  LDAPSSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Certificate
    * JSON representation
  * State



LDAPSSettings represents the ldaps settings for domain resource. LDAP is the Lightweight Directory Access Protocol, defined in <https://tools.ietf.org/html/rfc4511>. The settings object configures LDAP over SSL/TLS, whether it is over port 636 or the StartTLS operation. If LDAPSSettings is being changed, it will be placed into the UPDATING state, which indicates that the resource is being reconciled. At this point, Get will reflect an intermediate state.

JSON representation  
---  
      
    
    {
      "name": string,
      "certificate": {
        object ([Certificate](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#Certificate))
      },
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#State)),
      "certificatePfx": string,
      "certificatePassword": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` The resource name of the LDAPS settings. Uses the form: `projects/{project}/locations/{location}/domains/{domain}`.  
`certificate` |  `object (`[Certificate](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#Certificate)`)` Output only. The certificate used to configure LDAPS. Certificates can be chained with a maximum length of 15.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#State)`)` Output only. The current state of this LDAPS settings.  
`certificatePfx` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Input only. The uploaded PKCS12-formatted certificate to configure LDAPS with. It will enable the domain controllers in this domain to accept LDAPS connections (either LDAP over SSL/TLS or the StartTLS operation).A valid certificate chain must form a valid x.509 certificate chain (or be comprised of a single self-signed certificate. It must be encrypted with either: 1) PBES2 + PBKDF2 + AES256 encryption and SHA256 PRF; or 2) pbeWithSHA1And3-KeyTripleDES-CBC Private key must be included for the leaf / single self-signed certificate.Note: For a fqdn your-example-domain.com, the wildcard fqdn is *.your-example-domain.com. Specifically the leaf certificate must have: - Either a blank subject or a subject with CN matching the wildcard fqdn. - Exactly two SANs - the fqdn and wildcard fqdn. - Encipherment and digital key signature key usages. - Server authentication extended key usage (OID=1.3.6.1.5.5.7.3.1) - Private key must be in one of the following formats: RSA, ECDSA, ED25519. - Private key must have appropriate key length: 2048 for RSA, 256 for ECDSA - Signature algorithm of the leaf certificate cannot be MD2, MD5 or SHA1.A base64-encoded string.  
`certificatePassword` |  `string` Input only. The password used to encrypt the uploaded pfx certificate.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Last update time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Certificate

Certificate used to configure LDAPS.

JSON representation  
---  
      
    
    {
      "subject": string,
      "thumbprint": string,
      "subjectAlternativeName": [
        string
      ],
      "issuingCertificate": {
        object ([Certificate](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#Certificate))
      },
      "expireTime": string
    }  
  
Fields  
---  
`subject` |  `string` The certificate subject.  
`thumbprint` |  `string` The certificate thumbprint which uniquely identifies the certificate.  
`subjectAlternativeName[]` |  `string` The additional hostnames for the domain.  
`issuingCertificate` |  `object (`[Certificate](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/LDAPSSettings#Certificate)`)` The issuer of this certificate.  
`expireTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The certificate expire time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## State

Represents the different states of a LDAPS Setting.

Enums  
---  
`STATE_UNSPECIFIED` | Not Set  
`UPDATING` | The LDAPS setting is being updated.  
`ACTIVE` | The LDAPS setting is ready.  
`FAILED` | The LDAPS setting is not applied correctly.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
