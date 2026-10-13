---
url: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription/
title: CertificateDescription \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:37.529443+00:00
---

# CertificateDescription  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback 

#  CertificateDescription Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SubjectDescription
    * JSON representation
  * KeyId
    * JSON representation
  * CertificateFingerprint
    * JSON representation



A `[CertificateDescription](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription)` describes an X.509 certificate or CSR that has been issued, as an alternative to using ASN.1 / X.509.

JSON representation  
---  
      
    
    {
      "subjectDescription": {
        object ([SubjectDescription](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#SubjectDescription))
      },
      "x509Description": {
        object ([X509Parameters](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters))
      },
      "publicKey": {
        object ([PublicKey](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/PublicKey))
      },
      "subjectKeyId": {
        object ([KeyId](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#KeyId))
      },
      "authorityKeyId": {
        object ([KeyId](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#KeyId))
      },
      "crlDistributionPoints": [
        string
      ],
      "aiaIssuingCertificateUrls": [
        string
      ],
      "certFingerprint": {
        object ([CertificateFingerprint](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#CertificateFingerprint))
      },
      "tbsCertificateDigest": string
    }  
  
Fields  
---  
`subjectDescription` |  `object (`[SubjectDescription](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#SubjectDescription)`)` Describes some of the values in a certificate that are related to the subject and lifetime.  
`x509Description` |  `object (`[X509Parameters](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters)`)` Describes some of the technical X.509 fields in a certificate.  
`publicKey` |  `object (`[PublicKey](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/PublicKey)`)` The public key that corresponds to an issued certificate.  
`subjectKeyId` |  `object (`[KeyId](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#KeyId)`)` Provides a means of identifiying certificates that contain a particular public key, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.2>.  
`authorityKeyId` |  `object (`[KeyId](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#KeyId)`)` Identifies the subjectKeyId of the parent certificate, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.1>  
`crlDistributionPoints[]` |  `string` Describes a list of locations to obtain CRL information, i.e. the DistributionPoint.fullName described by <https://tools.ietf.org/html/rfc5280#section-4.2.1.13>  
`aiaIssuingCertificateUrls[]` |  `string` Describes lists of issuer CA certificate URLs that appear in the "Authority Information Access" extension in the certificate.  
`certFingerprint` |  `object (`[CertificateFingerprint](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#CertificateFingerprint)`)` The hash of the x.509 certificate.  
`tbsCertificateDigest` |  `string` The hash of the pre-signed certificate, which will be signed by the CA. Corresponds to the TBS Certificate in <https://tools.ietf.org/html/rfc5280#section-4.1.2>. The field will always be populated.  
  
## SubjectDescription

These values describe fields in an issued X.509 certificate such as the distinguished name, subject alternative names, serial number, and lifetime.

JSON representation  
---  
      
    
    {
      "subject": {
        object ([Subject](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject))
      },
      "subjectAltName": {
        object ([SubjectAltNames](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/SubjectAltNames))
      },
      "hexSerialNumber": string,
      "lifetime": string,
      "notBeforeTime": string,
      "notAfterTime": string
    }  
  
Fields  
---  
`subject` |  `object (`[Subject](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject)`)` Contains distinguished name fields such as the common name, location and / organization.  
`subjectAltName` |  `object (`[SubjectAltNames](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/SubjectAltNames)`)` The subject alternative name fields.  
`hexSerialNumber` |  `string` The serial number encoded in lowercase hexadecimal.  
`lifetime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` For convenience, the actual lifetime of an issued certificate.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`notBeforeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the certificate becomes valid.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`notAfterTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time after which the certificate is expired. Per RFC 5280, the validity period for a certificate is the period of time from notBeforeTime through notAfterTime, inclusive. Corresponds to 'notBeforeTime' + 'lifetime' - 1 second.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## KeyId

A KeyId identifies a specific public key, usually by hashing the public key.

JSON representation  
---  
      
    
    {
      "keyId": string
    }  
  
Fields  
---  
`keyId` |  `string` Optional. The value of this KeyId encoded in lowercase hexadecimal. This is most likely the 160 bit SHA-1 hash of the public key.  
  
## CertificateFingerprint

A group of fingerprints for the x509 certificate.

JSON representation  
---  
      
    
    {
      "sha256Hash": string
    }  
  
Fields  
---  
`sha256Hash` |  `string` The SHA 256 hash, encoded in hexadecimal, of the DER x509 certificate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
