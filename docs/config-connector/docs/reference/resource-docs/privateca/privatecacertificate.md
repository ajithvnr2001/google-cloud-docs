---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/privateca/privatecacertificate/
title: PrivateCACertificate \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:16.151887+00:00
---

# PrivateCACertificate  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/privateca/privatecacertificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PrivateCACertificate

**Property** | **Value**  
---|---  
Google Cloud Service Name | Private CA  
Google Cloud Service Documentation | [/certificate-authority-service/docs/](https://docs.cloud.google.com/certificate-authority-service/docs)  
Google Cloud REST Resource Name | v1.projects.locations.caPools.certificates  
Google Cloud REST Resource Documentation | [/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates)  
Config Connector Resource Short Names | gcpprivatecacertificate  
gcpprivatecacertificates  
privatecacertificate  
Config Connector Service Name | privateca.googleapis.com  
Config Connector Resource Fully Qualified Name | privatecacertificates.privateca.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    caPoolRef:
      external: string
      name: string
      namespace: string
    certificateAuthorityRef:
      external: string
      name: string
      namespace: string
    certificateTemplateRef:
      external: string
      name: string
      namespace: string
    config:
      publicKey:
        format: string
        key: string
      subjectConfig:
        subject:
          commonName: string
          countryCode: string
          locality: string
          organization: string
          organizationalUnit: string
          postalCode: string
          province: string
          streetAddress: string
        subjectAltName:
          dnsNames:
          - string
          emailAddresses:
          - string
          ipAddresses:
          - string
          uris:
          - string
      x509Config:
        additionalExtensions:
        - critical: boolean
          objectId:
            objectIdPath:
            - integer
          value: string
        aiaOcspServers:
        - string
        caOptions:
          isCa: boolean
          maxIssuerPathLength: integer
          nonCa: boolean
          zeroMaxIssuerPathLength: boolean
        keyUsage:
          baseKeyUsage:
            certSign: boolean
            contentCommitment: boolean
            crlSign: boolean
            dataEncipherment: boolean
            decipherOnly: boolean
            digitalSignature: boolean
            encipherOnly: boolean
            keyAgreement: boolean
            keyEncipherment: boolean
          extendedKeyUsage:
            clientAuth: boolean
            codeSigning: boolean
            emailProtection: boolean
            ocspSigning: boolean
            serverAuth: boolean
            timeStamping: boolean
          unknownExtendedKeyUsages:
          - objectIdPath:
            - integer
        policyIds:
        - objectIdPath:
          - integer
    lifetime: string
    location: string
    pemCsr: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    subjectMode: string
    

Fields  
---  
`caPoolRef` _Required_ |  `object` Immutable. Required. The PrivateCACAPool that includes this Certificate.  
`caPoolRef.external` _Optional_ |  `string` A reference to an externally managed PrivateCACAPool resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/caPools/{{caPoolID}}".  
`caPoolRef.name` _Optional_ |  `string` The name of a PrivateCACAPool resource.  
`caPoolRef.namespace` _Optional_ |  `string` The namespace of a PrivateCACAPool resource.  
`certificateAuthorityRef` _Optional_ |  `object` Immutable. Optional. The PrivateCACertificateAuthority that issued this Certificate.  
`certificateAuthorityRef.external` _Optional_ |  `string` A reference to an externally managed PrivateCACertificateAuthority resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/caPools/{{caPool}}/certificateAuthorities/{{certificateAuthorityID}}".  
`certificateAuthorityRef.name` _Optional_ |  `string` The name of a PrivateCACertificateAuthority resource.  
`certificateAuthorityRef.namespace` _Optional_ |  `string` The namespace of a PrivateCACertificateAuthority resource.  
`certificateTemplateRef` _Optional_ |  `object` Immutable. Optional. The PrivateCACertificateTemplate used to issue this Certificate.  
`certificateTemplateRef.external` _Optional_ |  `string` A reference to an externally managed PrivateCACertificateTemplate resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/certificateTemplates/{{certificateTemplateID}}".  
`certificateTemplateRef.name` _Optional_ |  `string` The name of a PrivateCACertificateTemplate resource.  
`certificateTemplateRef.namespace` _Optional_ |  `string` The namespace of a PrivateCACertificateTemplate resource.  
`config` _Optional_ |  `object` Immutable. Optional. A description of the certificate and key that does not require X.509 or ASN.1.  
`config.publicKey` _Optional_ |  `object` Immutable. Optional. The public key that corresponds to this config.  
`config.publicKey.format` _Required*_ |  `string` Immutable. Required. The format of the public key. Possible values: KEY_FORMAT_UNSPECIFIED, PEM  
`config.publicKey.key` _Required*_ |  `string` Immutable. Required. A public key. The padding and encoding must match with the `KeyFormat` value specified for the `format` field.  
`config.subjectConfig` _Required*_ |  `object` Immutable. Required. Specifies some of the values in a certificate that are related to the subject.  
`config.subjectConfig.subject` _Required*_ |  `object` Immutable. Required. Contains distinguished name fields such as the common name, location and organization.  
`config.subjectConfig.subject.commonName` _Optional_ |  `string` The "common name" of the subject.  
`config.subjectConfig.subject.countryCode` _Optional_ |  `string` The country code of the subject.  
`config.subjectConfig.subject.locality` _Optional_ |  `string` The locality or city of the subject.  
`config.subjectConfig.subject.organization` _Optional_ |  `string` The organization of the subject.  
`config.subjectConfig.subject.organizationalUnit` _Optional_ |  `string` The organizational_unit of the subject.  
`config.subjectConfig.subject.postalCode` _Optional_ |  `string` The postal code of the subject.  
`config.subjectConfig.subject.province` _Optional_ |  `string` The province, territory, or regional state of the subject.  
`config.subjectConfig.subject.streetAddress` _Optional_ |  `string` The street address of the subject.  
`config.subjectConfig.subjectAltName` _Optional_ |  `object` Immutable. Optional. The subject alternative name fields.  
`config.subjectConfig.subjectAltName.dnsNames` _Optional_ |  `list (string)` Immutable. Optional. Contains only valid, fully-qualified host names.  
`config.subjectConfig.subjectAltName.dnsNames[]` _Optional_ |  `string`  
`config.subjectConfig.subjectAltName.emailAddresses` _Optional_ |  `list (string)` Immutable. Optional. Contains only valid RFC 2822 E-mail addresses.  
`config.subjectConfig.subjectAltName.emailAddresses[]` _Optional_ |  `string`  
`config.subjectConfig.subjectAltName.ipAddresses` _Optional_ |  `list (string)` Immutable. Optional. Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses.  
`config.subjectConfig.subjectAltName.ipAddresses[]` _Optional_ |  `string`  
`config.subjectConfig.subjectAltName.uris` _Optional_ |  `list (string)` Immutable. Optional. Contains only valid RFC 3986 URIs.  
`config.subjectConfig.subjectAltName.uris[]` _Optional_ |  `string`  
`config.x509Config` _Required*_ |  `object` Immutable. Required. Describes how some of the technical X.509 fields in a certificate should be populated.  
`config.x509Config.additionalExtensions` _Optional_ |  `list (object)` Immutable. Optional. Describes custom X.509 extensions.  
`config.x509Config.additionalExtensions[]` _Optional_ |  `object`  
`config.x509Config.additionalExtensions[].critical` _Optional_ |  `boolean` Immutable. Optional. Indicates whether or not this extension is critical.  
`config.x509Config.additionalExtensions[].objectId` _Required*_ |  `object` Immutable. Required. The OID for this X.509 extension.  
`config.x509Config.additionalExtensions[].objectId.objectIdPath` _Required*_ |  `list (integer)` Immutable. Required. The parts of an OID path. The most significant parts of the path come first.  
`config.x509Config.additionalExtensions[].objectId.objectIdPath[]` _Required*_ |  `integer`  
`config.x509Config.additionalExtensions[].value` _Required*_ |  `string` Immutable. Required. The value of this X.509 extension.  
`config.x509Config.aiaOcspServers` _Optional_ |  `list (string)` Immutable. Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.  
`config.x509Config.aiaOcspServers[]` _Optional_ |  `string`  
`config.x509Config.caOptions` _Optional_ |  `object` Immutable. Optional. Describes options in this X509Parameters that are relevant in a CA certificate.  
`config.x509Config.caOptions.isCa` _Optional_ |  `boolean` Immutable. Optional. When true, the "CA" in Basic Constraints extension will be set to true.  
`config.x509Config.caOptions.maxIssuerPathLength` _Optional_ |  `integer` Immutable. Optional. Refers to the "path length constraint" in Basic Constraints extension.  
`config.x509Config.caOptions.nonCa` _Optional_ |  `boolean` Immutable. Optional. When true, the "CA" in Basic Constraints extension will be set to false. If both `is_ca` and `non_ca` are unset, the extension will be omitted from the CA certificate.  
`config.x509Config.caOptions.zeroMaxIssuerPathLength` _Optional_ |  `boolean` Immutable. Optional. When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both max_issuer_path_length and zero_max_issuer_path_length are unset, the max path length will be omitted from the CA certificate.  
`config.x509Config.keyUsage` _Optional_ |  `object` Immutable. Optional. Indicates the intended use for keys that correspond to a certificate.  
`config.x509Config.keyUsage.baseKeyUsage` _Optional_ |  `object` Immutable. Optional. Describes high-level ways in which a key may be used.  
`config.x509Config.keyUsage.baseKeyUsage.certSign` _Optional_ |  `boolean` Immutable. Optional. The key may be used to sign certificates.  
`config.x509Config.keyUsage.baseKeyUsage.contentCommitment` _Optional_ |  `boolean` Immutable. Optional. The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".  
`config.x509Config.keyUsage.baseKeyUsage.crlSign` _Optional_ |  `boolean` Immutable. Optional. The key may be used sign certificate revocation lists.  
`config.x509Config.keyUsage.baseKeyUsage.dataEncipherment` _Optional_ |  `boolean` Immutable. Optional. The key may be used to encipher data.  
`config.x509Config.keyUsage.baseKeyUsage.decipherOnly` _Optional_ |  `boolean` Immutable. Optional. The key may be used to decipher only.  
`config.x509Config.keyUsage.baseKeyUsage.digitalSignature` _Optional_ |  `boolean` Immutable. Optional. The key may be used for digital signatures.  
`config.x509Config.keyUsage.baseKeyUsage.encipherOnly` _Optional_ |  `boolean` Immutable. Optional. The key may be used to encipher only.  
`config.x509Config.keyUsage.baseKeyUsage.keyAgreement` _Optional_ |  `boolean` Immutable. Optional. The key may be used in a key agreement protocol.  
`config.x509Config.keyUsage.baseKeyUsage.keyEncipherment` _Optional_ |  `boolean` Immutable. Optional. The key may be used to encipher other keys.  
`config.x509Config.keyUsage.extendedKeyUsage` _Optional_ |  `object` Immutable. Optional. Detailed scenarios in which a key may be used.  
`config.x509Config.keyUsage.extendedKeyUsage.clientAuth` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS.  
`config.x509Config.keyUsage.extendedKeyUsage.codeSigning` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".  
`config.x509Config.keyUsage.extendedKeyUsage.emailProtection` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".  
`config.x509Config.keyUsage.extendedKeyUsage.ocspSigning` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".  
`config.x509Config.keyUsage.extendedKeyUsage.serverAuth` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.  
`config.x509Config.keyUsage.extendedKeyUsage.timeStamping` _Optional_ |  `boolean` Immutable. Optional. Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".  
`config.x509Config.keyUsage.unknownExtendedKeyUsages` _Optional_ |  `list (object)` Immutable. Optional. Used to describe extended key usages that are not listed in the KeyUsage.ExtendedKeyUsageOptions message.  
`config.x509Config.keyUsage.unknownExtendedKeyUsages[]` _Optional_ |  `object`  
`config.x509Config.keyUsage.unknownExtendedKeyUsages[].objectIdPath` _Required*_ |  `list (integer)` Immutable. Required. The parts of an OID path. The most significant parts of the path come first.  
`config.x509Config.keyUsage.unknownExtendedKeyUsages[].objectIdPath[]` _Required*_ |  `integer`  
`config.x509Config.policyIds` _Optional_ |  `list (object)` Immutable. Optional. Describes the X.509 certificate policy object identifiers, per https://tools.ietf.org/html/rfc5280#section-4.2.1.4.  
`config.x509Config.policyIds[]` _Optional_ |  `object`  
`config.x509Config.policyIds[].objectIdPath` _Required*_ |  `list (integer)` Immutable. Required. The parts of an OID path. The most significant parts of the path come first.  
`config.x509Config.policyIds[].objectIdPath[]` _Required*_ |  `integer`  
`lifetime` _Required_ |  `string` Immutable. Required. The desired lifetime of a certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate.  
`location` _Required_ |  `string` Immutable. The location for the resource.  
`pemCsr` _Optional_ |  `string` Immutable. Optional. A pem-encoded X.509 certificate signing request (CSR).  
`projectRef` _Required_ |  `object` Immutable. Required. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`subjectMode` _Optional_ |  `string` Immutable. Optional. Specifies how the Certificate's identity fields are to be decided.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    certificateDescription:
      aiaIssuingCertificateUrls:
      - string
      authorityKeyId:
        keyId: string
      certFingerprint:
        sha256Hash: string
      crlDistributionPoints:
      - string
      publicKey:
        format: string
        key: string
      subjectDescription:
        hexSerialNumber: string
        lifetime: string
        notAfterTime: string
        notBeforeTime: string
        subject:
          commonName: string
          countryCode: string
          locality: string
          organization: string
          organizationalUnit: string
          postalCode: string
          province: string
          streetAddress: string
        subjectAltName:
          customSans:
          - critical: boolean
            objectId:
              objectIdPath:
              - integer
            value: string
          dnsNames:
          - string
          emailAddresses:
          - string
          ipAddresses:
          - string
          uris:
          - string
      subjectKeyId:
        keyId: string
      x509Description:
        additionalExtensions:
        - critical: boolean
          objectId:
            objectIdPath:
            - integer
          value: string
        aiaOcspServers:
        - string
        caOptions:
          isCa: boolean
          maxIssuerPathLength: integer
        keyUsage:
          baseKeyUsage:
            certSign: boolean
            contentCommitment: boolean
            crlSign: boolean
            dataEncipherment: boolean
            decipherOnly: boolean
            digitalSignature: boolean
            encipherOnly: boolean
            keyAgreement: boolean
            keyEncipherment: boolean
          extendedKeyUsage:
            clientAuth: boolean
            codeSigning: boolean
            emailProtection: boolean
            ocspSigning: boolean
            serverAuth: boolean
            timeStamping: boolean
          unknownExtendedKeyUsages:
          - objectIdPath:
            - integer
        policyIds:
        - objectIdPath:
          - integer
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    createTime: string
    issuerCertificateAuthority: string
    observedGeneration: integer
    pemCertificate: string
    pemCertificateChain:
    - string
    revocationDetails:
      revocationState: string
      revocationTime: string
    updateTime: string
    

Fields  
---  
`certificateDescription` |  `object` Output only. A structured description of the issued X.509 certificate.  
`certificateDescription.aiaIssuingCertificateUrls` |  `list (string)` Optional. Describes lists of issuer CA certificate URLs that appear in the "Authority Information Access" extension in the certificate.  
`certificateDescription.aiaIssuingCertificateUrls[]` |  `string`  
`certificateDescription.authorityKeyId` |  `object` Optional. Identifies the subject_key_id of the parent certificate, per https://tools.ietf.org/html/rfc5280#section-4.2.1.1.  
`certificateDescription.authorityKeyId.keyId` |  `string` Optional. The value of this KeyId encoded in lowercase hexadecimal. This is most likely the 160 bit SHA-1 hash of the public key.  
`certificateDescription.certFingerprint` |  `object` Optional. The hash of the x.509 certificate.  
`certificateDescription.certFingerprint.sha256Hash` |  `string` Optional. The SHA 256 hash, encoded in hexadecimal, of the DER x509 certificate.  
`certificateDescription.crlDistributionPoints` |  `list (string)` Optional. Describes a list of locations to obtain CRL information, i.e. the DistributionPoint.fullName described by https://tools.ietf.org/html/rfc5280#section-4.2.1.13.  
`certificateDescription.crlDistributionPoints[]` |  `string`  
`certificateDescription.publicKey` |  `object` Optional. The public key that corresponds to an issued certificate.  
`certificateDescription.publicKey.format` |  `string` Optional. The format of the public key. Possible values: KEY_FORMAT_UNSPECIFIED, PEM.  
`certificateDescription.publicKey.key` |  `string` Optional. A public key. The padding and encoding must match with the `KeyFormat` value specified for the `format` field.  
`certificateDescription.subjectDescription` |  `object` Optional. Describes some of the values in a certificate that are related to the subject and lifetime.  
`certificateDescription.subjectDescription.hexSerialNumber` |  `string` Optional. The serial number encoded in lowercase hexadecimal.  
`certificateDescription.subjectDescription.lifetime` |  `string` Optional. For convenience, the actual lifetime of an issued certificate.  
`certificateDescription.subjectDescription.notAfterTime` |  `string` Optional. The time after which the certificate is expired. Per RFC 5280, the validity period for a certificate is the period of time from not_before_time through not_after_time, inclusive. Corresponds to 'not_before_time' + 'lifetime' - 1 second.  
`certificateDescription.subjectDescription.notBeforeTime` |  `string` Optional. The time at which the certificate becomes valid.  
`certificateDescription.subjectDescription.subject` |  `object` Optional. Contains distinguished name fields such as the common name, location and / organization.  
`certificateDescription.subjectDescription.subject.commonName` |  `string` Optional. The "common name" of the subject.  
`certificateDescription.subjectDescription.subject.countryCode` |  `string` Optional. The country code of the subject.  
`certificateDescription.subjectDescription.subject.locality` |  `string` Optional. The locality or city of the subject.  
`certificateDescription.subjectDescription.subject.organization` |  `string` Optional. The organization of the subject.  
`certificateDescription.subjectDescription.subject.organizationalUnit` |  `string` Optional. The organizational_unit of the subject.  
`certificateDescription.subjectDescription.subject.postalCode` |  `string` Optional. The postal code of the subject.  
`certificateDescription.subjectDescription.subject.province` |  `string` Optional. The province, territory, or regional state of the subject.  
`certificateDescription.subjectDescription.subject.streetAddress` |  `string` Optional. The street address of the subject.  
`certificateDescription.subjectDescription.subjectAltName` |  `object` Optional. The subject alternative name fields.  
`certificateDescription.subjectDescription.subjectAltName.customSans` |  `list (object)` Optional. Contains additional subject alternative name values.  
`certificateDescription.subjectDescription.subjectAltName.customSans[]` |  `object`  
`certificateDescription.subjectDescription.subjectAltName.customSans[].critical` |  `boolean` Optional. Indicates whether or not this extension is critical.  
`certificateDescription.subjectDescription.subjectAltName.customSans[].objectId` |  `object` Optional. The OID for this X.509 extension.  
`certificateDescription.subjectDescription.subjectAltName.customSans[].objectId.objectIdPath` |  `list (integer)` Optional. The parts of an OID path. The most significant parts of the path come first.  
`certificateDescription.subjectDescription.subjectAltName.customSans[].objectId.objectIdPath[]` |  `integer`  
`certificateDescription.subjectDescription.subjectAltName.customSans[].value` |  `string` Optional. The value of this X.509 extension.  
`certificateDescription.subjectDescription.subjectAltName.dnsNames` |  `list (string)` Optional. Contains only valid, fully-qualified host names.  
`certificateDescription.subjectDescription.subjectAltName.dnsNames[]` |  `string`  
`certificateDescription.subjectDescription.subjectAltName.emailAddresses` |  `list (string)` Optional. Contains only valid RFC 2822 E-mail addresses.  
`certificateDescription.subjectDescription.subjectAltName.emailAddresses[]` |  `string`  
`certificateDescription.subjectDescription.subjectAltName.ipAddresses` |  `list (string)` Optional. Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses.  
`certificateDescription.subjectDescription.subjectAltName.ipAddresses[]` |  `string`  
`certificateDescription.subjectDescription.subjectAltName.uris` |  `list (string)` Optional. Contains only valid RFC 3986 URIs.  
`certificateDescription.subjectDescription.subjectAltName.uris[]` |  `string`  
`certificateDescription.subjectKeyId` |  `object` Optional. Provides a means of identifying certificates that contain a particular public key, per https://tools.ietf.org/html/rfc5280#section-4.2.1.2.  
`certificateDescription.subjectKeyId.keyId` |  `string` Optional. The value of this KeyId encoded in lowercase hexadecimal. This is most likely the 160 bit SHA-1 hash of the public key.  
`certificateDescription.x509Description` |  `object` Optional. Describes some of the technical X.509 fields in a certificate.  
`certificateDescription.x509Description.additionalExtensions` |  `list (object)` Optional. Describes custom X.509 extensions.  
`certificateDescription.x509Description.additionalExtensions[]` |  `object`  
`certificateDescription.x509Description.additionalExtensions[].critical` |  `boolean` Optional. Indicates whether or not this extension is critical.  
`certificateDescription.x509Description.additionalExtensions[].objectId` |  `object` Optional. The OID for this X.509 extension.  
`certificateDescription.x509Description.additionalExtensions[].objectId.objectIdPath` |  `list (integer)` Optional. The parts of an OID path. The most significant parts of the path come first.  
`certificateDescription.x509Description.additionalExtensions[].objectId.objectIdPath[]` |  `integer`  
`certificateDescription.x509Description.additionalExtensions[].value` |  `string` Optional. The value of this X.509 extension.  
`certificateDescription.x509Description.aiaOcspServers` |  `list (string)` Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.  
`certificateDescription.x509Description.aiaOcspServers[]` |  `string`  
`certificateDescription.x509Description.caOptions` |  `object` Optional. Describes options in this X509Parameters that are relevant in a CA certificate.  
`certificateDescription.x509Description.caOptions.isCa` |  `boolean` Optional. Refers to the "CA" X.509 extension, which is a boolean value. When this value is missing, the extension will be omitted from the CA certificate.  
`certificateDescription.x509Description.caOptions.maxIssuerPathLength` |  `integer` Optional. Refers to the path length restriction X.509 extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. If this value is missing, the max path length will be omitted from the CA certificate.  
`certificateDescription.x509Description.keyUsage` |  `object` Optional. Indicates the intended use for keys that correspond to a certificate.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage` |  `object` Optional. Describes high-level ways in which a key may be used.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.certSign` |  `boolean` Optional. The key may be used to sign certificates.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.contentCommitment` |  `boolean` Optional. The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.crlSign` |  `boolean` Optional. The key may be used sign certificate revocation lists.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.dataEncipherment` |  `boolean` Optional. The key may be used to encipher data.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.decipherOnly` |  `boolean` Optional. The key may be used to decipher only.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.digitalSignature` |  `boolean` Optional. The key may be used for digital signatures.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.encipherOnly` |  `boolean` Optional. The key may be used to encipher only.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.keyAgreement` |  `boolean` Optional. The key may be used in a key agreement protocol.  
`certificateDescription.x509Description.keyUsage.baseKeyUsage.keyEncipherment` |  `boolean` Optional. The key may be used to encipher other keys.  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage` |  `object` Optional. Detailed scenarios in which a key may be used.  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.clientAuth` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS.  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.codeSigning` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.emailProtection` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.ocspSigning` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.serverAuth` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.  
`certificateDescription.x509Description.keyUsage.extendedKeyUsage.timeStamping` |  `boolean` Optional. Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".  
`certificateDescription.x509Description.keyUsage.unknownExtendedKeyUsages` |  `list (object)` Optional. Used to describe extended key usages that are not listed in the KeyUsage.ExtendedKeyUsageOptions message.  
`certificateDescription.x509Description.keyUsage.unknownExtendedKeyUsages[]` |  `object`  
`certificateDescription.x509Description.keyUsage.unknownExtendedKeyUsages[].objectIdPath` |  `list (integer)` Optional. The parts of an OID path. The most significant parts of the path come first.  
`certificateDescription.x509Description.keyUsage.unknownExtendedKeyUsages[].objectIdPath[]` |  `integer`  
`certificateDescription.x509Description.policyIds` |  `list (object)` Optional. Describes the X.509 certificate policy object identifiers, per https://tools.ietf.org/html/rfc5280#section-4.2.1.4.  
`certificateDescription.x509Description.policyIds[]` |  `object`  
`certificateDescription.x509Description.policyIds[].objectIdPath` |  `list (integer)` Optional. The parts of an OID path. The most significant parts of the path come first.  
`certificateDescription.x509Description.policyIds[].objectIdPath[]` |  `integer`  
`conditions` |  `list (object)` Conditions represent the latest available observations of the PrivateCACertificate's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`createTime` |  `string` Output only. The time at which this Certificate was created.  
`issuerCertificateAuthority` |  `string` Output only. The resource name of the issuing CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`pemCertificate` |  `string` Output only. The pem-encoded, signed X.509 certificate.  
`pemCertificateChain` |  `list (string)` Output only. The chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246.  
`pemCertificateChain[]` |  `string`  
`revocationDetails` |  `object` Output only. Details regarding the revocation of this Certificate. This Certificate is considered revoked if and only if this field is present.  
`revocationDetails.revocationState` |  `string` Optional. Indicates why a Certificate was revoked. Possible values: REVOCATION_REASON_UNSPECIFIED, KEY_COMPROMISE, CERTIFICATE_AUTHORITY_COMPROMISE, AFFILIATION_CHANGED, SUPERSEDED, CESSATION_OF_OPERATION, CERTIFICATE_HOLD, PRIVILEGE_WITHDRAWN, ATTRIBUTE_AUTHORITY_COMPROMISE  
`revocationDetails.revocationTime` |  `string` Optional. The time at which this Certificate was revoked.  
`updateTime` |  `string` Output only. The time at which this Certificate was updated.  
  
## Sample YAML(s)

### Basic Certificate
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificate
    metadata:
      name: privatecacertificate-sample-basic
      labels:
        key: value
    spec:
      location: us-central1
      certificateAuthorityRef:
        name: privatecacertificate-dep-basic
      caPoolRef:
        name: privatecacertificate-dep-basic
      lifetime: 860s
      subjectMode: DEFAULT
      config:
        subjectConfig:
          subject:
            commonName: san1.example.com
          subjectAltName:
            dnsNames:
            - san1.example.com
            uris:
            - http://www.ietf.org/rfc/rfc3986.txt
            emailAddresses:
            - test_example@google.com
            ipAddresses:
            - 127.0.0.1
        x509Config:
          caOptions:
            isCa: false
          keyUsage:
            baseKeyUsage:
              crlSign: true
            extendedKeyUsage:
              serverAuth: true
        publicKey:
          format: PEM
          key: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUF2NndlQzFhVDE2bDJxUzZxZFljeQo3Qk9qelA3VHdUOXpVQWlGaFdwTDI1NkdScUM4eVFSZHFNc2k2OFEvLzc2MklVeXUvcWFIYkVnUThXUm1RZFZWCkdEbHhrQmZyQS9pWEIyZGd1anE4amgwSFdJVjJldjNUZXJWM2FVd3ZZVWxyb3docTAyN1NYOVUxaGJ1ZmRHQ00KdUtzSGlGMDVFcmdOdkV1UjhYQWtlSi9ZVjJEVjIrc1JxK1dnOXk0UndVWWJkY2hkRnR5MWQ1U1gvczBZcXN3Zwp5T0c5Vm9DZFI3YmFGMjJ1Z2hWUjQ0YVJtKzgzbWd0cUFaNE0rUnBlN0pHUnNVR1kvcFIzOTFUb2kwczhFbjE1CkpHaUFocVgyVzBVby9GWlpyeTN5dXFSZmRIWUVOQitBRHV5VE1UclVhS1p2N2V1YTBsVEJ6NW9vbTNqU0YzZ3YKSTdTUW9MZEsvamhFVk9PcTQxSWpCOEQ2MFNnZDY5YkQ3eVRJNTE2eXZaL3MzQXlLelc2ZjZLbmpkYkNjWktLVAowR0FlUE5MTmhEWWZTbEE5YndKOEhRUzJGZW5TcFNUQXJLdkdpVnJzaW5KdU5qYlFkUHVRSGNwV2Y5eDFtM0dSClRNdkYrVE5ZTS9scDdJTDJWTWJKUmZXUHkxaVd4bTlGMVlyNmRrSFZvTFA3b2NZa05SSG9QTHV0NUU2SUZKdEsKbFZJMk5uZVVZSkduWVNPKzF4UFY5VHFsSmVNTndyM3VGTUFOOE4vb0IzZjRXV3d1UllnUjBMNWcyQStMdngrZwpiYmRsK1RiLzBDTmZzbGZTdURyRlY4WjRuNmdWd2I5WlBHbE5IQ3ZucVJmTFVwUkZKd21SN1VZdnppL0U3clhKCkVEa0srdGNuUGt6Mkp0amRMS1I3cVZjQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ==
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACAPool
    metadata:
      labels:
        label-two: "value-two"
      name: privatecacertificate-dep-basic
      # PrivateCACertificateAuthority cannot be deleted immediately, and must wait
      # 30 days in a 'DELETED' status before it is fully deleted. Since a PrivateCACAPool
      # with a PrivateCACertificateAuthority in 'DELETED' status cannot be deleted
      # itself, we abandon this resource on deletion.
      annotations:
        cnrm.cloud.google.com/deletion-policy: "abandon"
    spec:
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
      location: us-central1
      tier: ENTERPRISE
      issuancePolicy:
        maximumLifetime: 43200s
        baselineValues:
          keyUsage:
            baseKeyUsage:
              digitalSignature: false
              contentCommitment: false
              keyEncipherment: false
              dataEncipherment: false
              keyAgreement: false
              certSign: false
              crlSign: false
              encipherOnly: false
              decipherOnly: false
            extendedKeyUsage:
              serverAuth: false
              clientAuth: false
              codeSigning: false
              emailProtection: false
              timeStamping: false
              ocspSigning: false
            unknownExtendedKeyUsages:
            - objectIdPath:
              - 1
              - 7
          caOptions:
            isCa: false
            maxIssuerPathLength: 7
          policyIds:
          - objectIdPath:
            - 1
            - 7
          aiaOcspServers:
          - string
          additionalExtensions:
          - objectId:
              objectIdPath:
              - 1
              - 7
            critical: false
            value: c3RyaW5nCg==
        passthroughExtensions:
          knownExtensions:
          - BASE_KEY_USAGE
          additionalExtensions:
          - objectIdPath:
            - 1
            - 7
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificateAuthority
    metadata:
      labels:
        label-two: "value-two"
      name: privatecacertificate-dep-basic
    spec:
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
      location: us-central1
      type: SELF_SIGNED
      caPoolRef:
        name: privatecacertificate-dep-basic
      lifetime: 86400s
      config:
        subjectConfig:
          subject:
            organization: Example
            commonName: my-certificate-authority
          subjectAltName:
            dnsNames:
            - example.com
        x509Config:
          caOptions:
            isCa: true
          keyUsage:
            baseKeyUsage:
              certSign: true
              crlSign: true
            extendedKeyUsage:
              serverAuth: true
      keySpec:
        algorithm: RSA_PKCS1_4096_SHA256
    

### Cert Sign Certificate
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificate
    metadata:
      name: privatecacertificate-sample-cert-sign
      labels:
        key: value
    spec:
      location: us-central1
      certificateAuthorityRef:
        name: privatecacertificate-dep-cert-sign
      caPoolRef:
        name: privatecacertificate-dep-cert-sign
      lifetime: "860s"
      config:
        subjectConfig:
          subject:
            commonName: "san1.example.com"
          subjectAltName:
            dnsNames:
            - "san1.example.com"
            uris:
            - "http://www.ietf.org/rfc/rfc3986.txt"
            emailAddresses:
            - test_example@google.com
            ipAddresses:
            - "127.0.0.1"
        x509Config:
          aiaOcspServers:
          - "www.example.com"
          caOptions:
            isCa: true
            maxIssuerPathLength: 100
          policyIds:
          - objectIdPath:
            - 1
            - 2
            - 3
            - 4
            - 5
            - 5
          additionalExtensions:
          - objectId:
              objectIdPath:
              - 1
              - 2
              - 3
              - 4
              - 5
              - 5
            critical: false
            value: "d3d3LmV4YW1wbGUuY29t"
          keyUsage:
            baseKeyUsage:
              digitalSignature: true
              contentCommitment: true
              keyEncipherment: true
              dataEncipherment: true
              keyAgreement: true
              crlSign: true
              encipherOnly: true
              certSign: true
            extendedKeyUsage:
              serverAuth: true
              clientAuth: true
              codeSigning: true
              emailProtection: true
              timeStamping: true
              ocspSigning: true
            unknownExtendedKeyUsages:
            - objectIdPath:
              - 1
              - 2
              - 3
              - 4
              - 5
              - 5
        publicKey:
          format: "PEM"
          key: "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUF2NndlQzFhVDE2bDJxUzZxZFljeQo3Qk9qelA3VHdUOXpVQWlGaFdwTDI1NkdScUM4eVFSZHFNc2k2OFEvLzc2MklVeXUvcWFIYkVnUThXUm1RZFZWCkdEbHhrQmZyQS9pWEIyZGd1anE4amgwSFdJVjJldjNUZXJWM2FVd3ZZVWxyb3docTAyN1NYOVUxaGJ1ZmRHQ00KdUtzSGlGMDVFcmdOdkV1UjhYQWtlSi9ZVjJEVjIrc1JxK1dnOXk0UndVWWJkY2hkRnR5MWQ1U1gvczBZcXN3Zwp5T0c5Vm9DZFI3YmFGMjJ1Z2hWUjQ0YVJtKzgzbWd0cUFaNE0rUnBlN0pHUnNVR1kvcFIzOTFUb2kwczhFbjE1CkpHaUFocVgyVzBVby9GWlpyeTN5dXFSZmRIWUVOQitBRHV5VE1UclVhS1p2N2V1YTBsVEJ6NW9vbTNqU0YzZ3YKSTdTUW9MZEsvamhFVk9PcTQxSWpCOEQ2MFNnZDY5YkQ3eVRJNTE2eXZaL3MzQXlLelc2ZjZLbmpkYkNjWktLVAowR0FlUE5MTmhEWWZTbEE5YndKOEhRUzJGZW5TcFNUQXJLdkdpVnJzaW5KdU5qYlFkUHVRSGNwV2Y5eDFtM0dSClRNdkYrVE5ZTS9scDdJTDJWTWJKUmZXUHkxaVd4bTlGMVlyNmRrSFZvTFA3b2NZa05SSG9QTHV0NUU2SUZKdEsKbFZJMk5uZVVZSkduWVNPKzF4UFY5VHFsSmVNTndyM3VGTUFOOE4vb0IzZjRXV3d1UllnUjBMNWcyQStMdngrZwpiYmRsK1RiLzBDTmZzbGZTdURyRlY4WjRuNmdWd2I5WlBHbE5IQ3ZucVJmTFVwUkZKd21SN1VZdnppL0U3clhKCkVEa0srdGNuUGt6Mkp0amRMS1I3cVZjQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACAPool
    metadata:
      labels:
        label-two: "value-two"
      name: privatecacertificate-dep-cert-sign
      # PrivateCACertificateAuthority cannot be deleted immediately, and must wait
      # 30 days in a 'DELETED' status before it is fully deleted. Since a PrivateCACAPool
      # with a PrivateCACertificateAuthority in 'DELETED' status cannot be deleted
      # itself, we abandon this resource on deletion.
      annotations:
        cnrm.cloud.google.com/deletion-policy: "abandon"
    spec:
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
      location: us-central1
      tier: ENTERPRISE
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificateAuthority
    metadata:
      name: privatecacertificate-dep-cert-sign
    spec:
      location: us-central1
      type: "SELF_SIGNED"
      caPoolRef:
        name: privatecacertificate-dep-cert-sign
      lifetime: "86400s"
      config:
        subjectConfig:
          subject:
            organization: "Example"
            commonName: "my-certificate-authority"
          subjectAltName:
            dnsNames:
            - "example.com"
        x509Config:
          caOptions:
            isCa: true
          keyUsage:
            baseKeyUsage:
              certSign: true
              crlSign: true
            extendedKeyUsage:
              serverAuth: true
      keySpec:
        algorithm: "RSA_PKCS1_4096_SHA256"
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
    

### Complex Certificate
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificate
    metadata:
      name: privatecacertificate-sample-complex
      labels:
        key: value
    spec:
      location: "us-central1"
      certificateAuthorityRef:
        name: privatecacertificate-dep-complex
      caPoolRef:
        name: privatecacertificate-dep-complex
      lifetime: "860s"
      config:
        subjectConfig:
          subject:
            commonName: "san1.example.com"
          subjectAltName:
            dnsNames:
            - "san1.example.com"
            uris:
            - "http://www.ietf.org/rfc/rfc3986.txt"
            emailAddresses:
            - test_example@google.com
            ipAddresses:
            - "127.0.0.1"
        x509Config:
          caOptions:
            isCa: false
          keyUsage:
            baseKeyUsage:
              digitalSignature: true
              contentCommitment: true
              keyEncipherment: true
              dataEncipherment: true
              keyAgreement: true
              crlSign: true
              encipherOnly: true
              decipherOnly: true
            extendedKeyUsage:
              serverAuth: true
              clientAuth: true
              codeSigning: true
              emailProtection: true
              timeStamping: true
              ocspSigning: true
        publicKey:
          format: "PEM"
          key: "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUF2NndlQzFhVDE2bDJxUzZxZFljeQo3Qk9qelA3VHdUOXpVQWlGaFdwTDI1NkdScUM4eVFSZHFNc2k2OFEvLzc2MklVeXUvcWFIYkVnUThXUm1RZFZWCkdEbHhrQmZyQS9pWEIyZGd1anE4amgwSFdJVjJldjNUZXJWM2FVd3ZZVWxyb3docTAyN1NYOVUxaGJ1ZmRHQ00KdUtzSGlGMDVFcmdOdkV1UjhYQWtlSi9ZVjJEVjIrc1JxK1dnOXk0UndVWWJkY2hkRnR5MWQ1U1gvczBZcXN3Zwp5T0c5Vm9DZFI3YmFGMjJ1Z2hWUjQ0YVJtKzgzbWd0cUFaNE0rUnBlN0pHUnNVR1kvcFIzOTFUb2kwczhFbjE1CkpHaUFocVgyVzBVby9GWlpyeTN5dXFSZmRIWUVOQitBRHV5VE1UclVhS1p2N2V1YTBsVEJ6NW9vbTNqU0YzZ3YKSTdTUW9MZEsvamhFVk9PcTQxSWpCOEQ2MFNnZDY5YkQ3eVRJNTE2eXZaL3MzQXlLelc2ZjZLbmpkYkNjWktLVAowR0FlUE5MTmhEWWZTbEE5YndKOEhRUzJGZW5TcFNUQXJLdkdpVnJzaW5KdU5qYlFkUHVRSGNwV2Y5eDFtM0dSClRNdkYrVE5ZTS9scDdJTDJWTWJKUmZXUHkxaVd4bTlGMVlyNmRrSFZvTFA3b2NZa05SSG9QTHV0NUU2SUZKdEsKbFZJMk5uZVVZSkduWVNPKzF4UFY5VHFsSmVNTndyM3VGTUFOOE4vb0IzZjRXV3d1UllnUjBMNWcyQStMdngrZwpiYmRsK1RiLzBDTmZzbGZTdURyRlY4WjRuNmdWd2I5WlBHbE5IQ3ZucVJmTFVwUkZKd21SN1VZdnppL0U3clhKCkVEa0srdGNuUGt6Mkp0amRMS1I3cVZjQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACAPool
    metadata:
      labels:
        label-two: "value-two"
      name: privatecacertificate-dep-complex
      # PrivateCACertificateAuthority cannot be deleted immediately, and must wait
      # 30 days in a 'DELETED' status before it is fully deleted. Since a PrivateCACAPool
      # with a PrivateCACertificateAuthority in 'DELETED' status cannot be deleted
      # itself, we abandon this resource on deletion.
      annotations:
        cnrm.cloud.google.com/deletion-policy: "abandon"
    spec:
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
      location: us-central1
      tier: ENTERPRISE
    ---
    apiVersion: privateca.cnrm.cloud.google.com/v1beta1
    kind: PrivateCACertificateAuthority
    metadata:
      name: privatecacertificate-dep-complex
    spec:
      location: us-central1
      type: "SELF_SIGNED"
      caPoolRef:
        name: privatecacertificate-dep-complex
      lifetime: "86400s"
      config:
        subjectConfig:
          subject:
            organization: "Example"
            commonName: "my-certificate-authority"
          subjectAltName:
            dnsNames:
            - "example.com"
        x509Config:
          caOptions:
            isCa: true
          keyUsage:
            baseKeyUsage:
              certSign: true
              crlSign: true
            extendedKeyUsage:
              serverAuth: true
      keySpec:
        algorithm: "RSA_PKCS1_4096_SHA256"
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: projects/${PROJECT_ID?}
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
