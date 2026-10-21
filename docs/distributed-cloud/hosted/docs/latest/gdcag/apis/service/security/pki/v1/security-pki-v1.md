---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/v1/security-pki-v1/
title: KRM API pki.security.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:25.352606+00:00
---

# KRM API pki.security.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/security/pki/v1/security-pki-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API pki.security.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## pki.security.gdc.goog/v1

Contains API Schema definitions for the PKI v1 API group.

### ACMEConfig

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`enabled` _boolean_ | Whether to deploy and access CA via ACME protocol.  
  
### ACMEIssuerConfig

_Appears in:_ \- CertificateIssuerSpec

Field | Description  
---|---  
`rootCACertificate` _integer array_ | This contains the Root CA data of certificates issued by ACME server.  
`acme` _ACMEIssuer_ | ACME configures this issuer to communicate with a RFC 8555 (ACME) server to obtain signed certificates. ACME is an acme.cert-manager.io/v1 ACMEIssuer.  
  
### ACMEStatus

_Appears in:_ \- CertificateAuthorityStatus

Field | Description  
---|---  
`uri` _string_ | URI is the unique account identifier, which can also be used to retrieve account details from the CA  
  
### BYOCertIssuerConfig

BYOCertIssuerConfig defines an issuer based on the BYO-Cert model.

_Appears in:_ \- CertificateIssuerSpec

Field | Description  
---|---  
`fallbackCertificateAuthority` _CAReference_ | FallbackCertificateAuthority is the reference to a default CAaaS operated CA. API type: - Group: pki.security.gdc.goog - Kind: CertificateAuthority  
  
### BYOCertStatus

_Appears in:_ \- CertificateStatus

Field | Description  
---|---  
`csrStatus` _CSRStatus_ | Certificate Signing Request (CSR) status  
`signedCertStatus` _SignedCertStatus_ | Externally signed certificate status  
  
### BYOCertificate

Externally signed certificate

_Appears in:_ \- CertificateSpec

Field | Description  
---|---  
`certificate` _integer array_ | The PEM encoded x509 certificate uploaded by the customer.  
`ca` _integer array_ | The PEM encoded x509 certificate of the signer CA used to sign the certificate.  
  
### CACertificateConfig

CACertificateConfig defines how the CA certificate is going to be provisioned. Only one of them will be set at any point in time.

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`externalCA` _ExternalCAConfig_ | Get the certificate from an external root CA. If set, a CSR will be generated on the status and signed certificate can be upload using this field.  
`selfSignedCA` _SelfSignedCAConfig_ | Issue a self-signed certificate. (Root CA)  
`managedSubCA` _ManagedSubCAConfig_ | Issue a SubCA certificate from a GDC-managed CA. (Managed Sub CA)  
  
### CACertificateProfile

CACertificateProfile defines the profile for a CA certificate.

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`commonName` _string_ | The common name of the CA Certificate.  
`organizations` _string array_ | Organizations to be used on the Certificate.  
`countries` _string array_ | Countries to be used on the Certificate.  
`organizationalUnits` _string array_ | Organizational Units to be used on the Certificate.  
`localities` _string array_ | Cities to be used on the Certificate.  
`provinces` _string array_ | State/Provinces to be used on the Certificate.  
`streetAddresses` _string array_ | Street addresses to be used on the Certificate.  
`postalCodes` _string array_ | Postal codes to be used on the Certificate.  
`duration` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The requested 'duration' (i.e. lifetime) of the CA Certificate.  
`renewBefore` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | RenewBefore implies the rotation time before the CA certificate expires.  
`maxPathLength` _integer_ | The maximum path length of the CA certificate.  
  
### CAReference

CAReference represents a CertificateAuthority reference. It has information to retrieve a CA in any namespace.

_Appears in:_ \- BYOCertIssuerConfig \- CAaaSIssuerConfig \- CertificateRequestSpec \- ManagedSubCAConfig

Field | Description  
---|---  
`name` _string_ | Name is unique within a namespace to reference a CA resource.  
`namespace` _string_ | Namespace defines the space within which the CA name must be unique.  
  
### CAaaSIssuerConfig

CAaaSIssuerConfig defines an issuer that requests certificates from a CA created using the CAaaS service.

_Appears in:_ \- CertificateIssuerSpec

Field | Description  
---|---  
`certificateAuthorityRef` _CAReference_ | A reference to a CertificationAuthority which will sign the certificate. API type: - Group: pki.security.gdc.goog - Kind: CertificateAuthority  
  
### CRLConfig

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`enabled` _boolean_ | Whether to enable CRL or not. Defaults to true if not specified.  
`validity` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The validity of the CRL. Defaults to 7 days if not specified.  
`renewBefore` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | RenewBefore defines the period before the CRL expires when a new CRL is generated and published. If unset, this defaults to 1/3 of the CRL's validity period. Also, a new CRL is published immediately upon any certificate revocation.  
  
### CSRStatus

_Appears in:_ \- BYOCertStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of a BYO Certificate CSR - WaitingforSigning: Indicates that a new CSR has been generated to be signed by the customer. - Ready: Indicates that the CSR has been signed  
`csr` _integer array_ | Stores the CSR for the customer to sign.  
  
### Certificate

A Certificate represents a managed certificate.

_Appears in:_ \- CertificateList

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `Certificate`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CertificateSpec_ |   
`status` _CertificateStatus_ |   
  
### CertificateAuthority

CertificateAuthority represents the individual Certificate Authority that will be used to issue the certificates.

_Appears in:_ \- CertificateAuthorityList

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateAuthority`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CertificateAuthoritySpec_ |   
`status` _CertificateAuthorityStatus_ |   
  
### CertificateAuthorityList

CertificateAuthorityList represents a collection of certiifcate authorities.

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateAuthorityList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CertificateAuthority array_ |   
  
### CertificateAuthoritySpec

_Appears in:_ \- CertificateAuthority

Field | Description  
---|---  
`caProfile` _CACertificateProfile_ | The profile of the CertificateAuthority.  
`caCertificate` _CACertificateConfig_ | The CA Certificate provisioning configuration.  
`secretConfig` _SecretConfig_ | Configuration of the CA secret.  
`kmsKeyConfig` _KMSKeyConfig_ | Configuration of the CA private keys to be in KMS  
`certificateProfile` _CertificateProfile_ | Defines the profile of the certificates that will be issued.  
`acme` _ACMEConfig_ | Config related to enable ACME protocol.  
`crl` _CRLConfig_ | Configuration of the Certificate Revocation List (CRL).  
  
### CertificateAuthorityStatus

_Appears in:_ \- CertificateAuthority

Field | Description  
---|---  
`externalCA` _ExternalCAStatus_ | ExternalCA specifies status options for SunCA signed by External root CA.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of a Certification Authority. - Pending: CSR are pending to be signed by the customer. - Ready: Indicates that the certificate authority is ready to use.  
`acme` _ACMEStatus_ | ACME specific status options. This field should only be set if the Certificate Authority is configured with ACME enabled.  
`crl` _string_ | The URL of the certificate revocation list (CRL) for this CA.  
`certificate` _integer array_ | The PEM encoded X.509 ca certificate chain consisting of intermediate CA certificates and root CA certificate.  
  
### CertificateConfig

CertificateConfig represents the subject information in an issued certificate.

_Appears in:_ \- CertificateRequestSpec

Field | Description  
---|---  
`subjectConfig` _SubjectConfig_ | These values are used to create the distinguished name and subject alternative name fields in an X.509 certificate.  
`privateKeyConfig` _CertificatePrivateKey_ | Private key options. These include the key algorithm and size.  
  
### CertificateIssuer

CertificateIssuer represents an issuer for Certificate as a Service. You can mark a CertificateIssuer as the default issuer by adding/setting the label `pki.security.gdc.goog/is-default-issuer: true`.

_Appears in:_ \- CertificateIssuerList

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateIssuer`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CertificateIssuerSpec_ |   
`status` _CertificateIssuerStatus_ |   
  
### CertificateIssuerList

CertificateIssuerList represents a collection of certiifcate issuers.

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateIssuerList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CertificateIssuer array_ |   
  
### CertificateIssuerSpec

_Appears in:_ \- CertificateIssuer

Field | Description  
---|---  
`byoCertConfig` _BYOCertIssuerConfig_ | BYOCertConfig configures this issuer in BYO-Cert mode.  
`caaasConfig` _CAaaSIssuerConfig_ | CAaaSConfig configures this issuer to sign certificates using CA deployed by the CertificateAuthority API.  
`acmeConfig` _ACMEIssuerConfig_ | ACMEConfig configures this issuer to sign certificates using ACME server.  
  
### CertificateIssuerStatus

_Appears in:_ \- CertificateIssuer

Field | Description  
---|---  
`ca` _integer array_ | Stores the root CA used by the current certificate issuer.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of the CertificateIssuer. - Ready: Indicates that the CertificateIssuer is ready to use.  
  
### CertificateList

CertificateList represents a collection of certificates.

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Certificate array_ |   
  
### CertificatePrivateKey

_Appears in:_ \- CertificateConfig

Field | Description  
---|---  
`algorithm` _PrivateKeyAlgorithm_ | Algorithm is the private key algorithm of the corresponding private key for this certificate. If provided, allowed values are either `RSA`,`Ed25519` or `ECDSA` If `algorithm` is specified and `size` is not provided, key size of 384 will be used for `ECDSA` key algorithm and key size of 3072 will be used for `RSA` key algorithm. key size is ignored when using the `Ed25519` key algorithm. See github.com/cert-manager/cert-manager/pkg/apis/certmanager/v1/types_certificate.go for more information.  
`size` _integer_ | Size is the key bit size of the corresponding private key for this certificate. If `algorithm` is set to `RSA`, valid values are `2048`, `3072`, `4096` or `8192`, and will default to `3072` if not specified. If `algorithm` is set to `ECDSA`, valid values are `256`, `384` or `521`, and will default to `384` if not specified. If `algorithm` is set to `Ed25519`, Size is ignored. No other values are allowed. See github.com/cert-manager/cert-manager/pkg/apis/certmanager/v1/types_certificate.go for more information.  
  
### CertificateProfile

CertificateProfile defines the specification of the profile of an issued certificate.

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`keyUsage` _KeyUsageBits array_ | Allowed key usages for certificates issued under this profile.  
`extendedKeyUsage` _ExtendedKeyUsageBits array_ | Allowed extended key usages for certificates issued under this profile.  
  
### CertificateRequest

CertificateRequest represents a request to issue certificate from the referenced CertificateAuthority.

All fields within the CertificateRequest's `spec` are immutable after creation.

_Appears in:_ \- CertificateRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CertificateRequestSpec_ |   
`status` _CertificateRequestStatus_ |   
  
### CertificateRequestList

CertificateRequestList represents a collection of certiifcate requests.

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `CertificateRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CertificateRequest array_ |   
  
### CertificateRequestReference

_Appears in:_ \- RevokeCertificateRequestSpec

Field | Description  
---|---  
`name` _string_ | Name of the certificate.  
`namespace` _string_ | Namespace of the certificate.  
  
### CertificateRequestSpec

CertificateRequestSpec defines a request for the issuance of a certificate.

_Appears in:_ \- CertificateRequest

Field | Description  
---|---  
`csr` _integer array_ | Certificate Signing Request to sign using CA.  
`certificateConfig` _CertificateConfig_ | certificate config that will be use to create the CSR.  
`notBefore` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Validity start time of the certificate. If not set, we will use the current time of the request.  
`notAfter` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Validity end time of the certificate. If not set, we will use 90 days from the notBefore time as default.  
`signedCertificateSecret` _string_ | Name of the secret to store the signed certificate.  
`certificateAuthorityRef` _CAReference_ | A reference to a CertificateAuthority which will sign the certificate. API type: - Group: pki.security.gdc.goog - Kind: CertificateAuthority  
`certificateTemplate` _string_ | A template used to issue the certificate.  
`subjectOverride` _integer array_ | SubjectOverride is a raw, ASN.1 DER-encoded X.509 subject. If set, this raw subject will be used instead of the raw subject in the CSR.  
  
### CertificateRequestStatus

_Appears in:_ \- CertificateRequest

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of a certificate to be issued. - PENDING: CSR are pending to be signed. - Ready: Indicates that the certificateRequest is fulfilled.  
`autoGeneratedPrivateKey` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | If no CSR is provided, an auto-generated private key will be used. optional  
  
### CertificateSpec

_Appears in:_ \- Certificate

Field | Description  
---|---  
`issuer` _IssuerReference_ | A reference to the CertificateIssuer that will be used for the issuance of the certificate. If not set, a label named `pki.security.gdc.goog/use-default-issuer: true` needs to be set in order to issue the certificate using the default issuer. API type: - Group: pki.security.gdc.goog - Kind: CertificateIssuer  
`commonName` _string_ | Requested common name X509 certificate subject attribute. It should have a length of 64 characters or fewer. For backward compatibility, the behaviour is as follows: If nil, we use the current behavior to set commonName as first DNSName if length is 64 characters or fewer. if empty string, don't set it. if it is set, ensure it is a part of the SANs.  
`dnsNames` _string array_ | DNSNames is a list of fully-qualified host names to be set on the Certificate.  
`ipAddresses` _string array_ | IPAddresses is a list of IPAddress subjectAltNames to be set on the Certificate.  
`duration` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The requested 'duration' (i.e. lifetime) of the Certificate.  
`renewBefore` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | RenewBefore implies the rotation time before the certificate expires.  
`secretConfig` _SecretConfig_ | Configuration of the Certificate secret.  
`byoCertificate` _BYOCertificate_ | Contains the externally signed certificate  
  
### CertificateStatus

_Appears in:_ \- Certificate

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of the certificate. - Ready: Indicates that the certificate is ready to use.  
`issuedBy` _IssuerReference_ | A reference to the CertificateIssuer that is used for the issuance of the certificate. API type: - Group: pki.security.gdc.goog - Kind: CertificateIssuer  
`byoCertStatus` _BYOCertStatus_ | BYOCertStatus specifies status options for byo-certificates mode.  
`errorStatus` _ErrorStatus_ | ErrorStatus contain a list of current errors and the timestamp this field gets updated.  
  
### ExtendedKeyUsageBits

_Underlying type:_ `string` ExtendedKeyUsageBits defines the different allowed extended key usages according to RFC 5280 4.2.1.12. Many extended key usages have been defined by follow-up RFCs, and can be implemented as a later feature if issuance of such certificates is needed, for cases such as certificates used for personal authentication, code signing or IPSec.

_Appears in:_ \- CertificateProfile

### ExternalCAConfig

_Appears in:_ \- CACertificateConfig

Field | Description  
---|---  
`signedCertificate` _SignedCertificateConfig_ | Stores a signed certificate signed by external root CA.  
  
### ExternalCAStatus

_Appears in:_ \- CertificateAuthorityStatus

Field | Description  
---|---  
`csr` _integer array_ | A certificate signing request waiting to be signed by an external CA.  
  
### IssuerReference

IssuerReference represents an Issuer Reference. It has information to retrieve an issuer in any namespace.

_Appears in:_ \- CertificateSpec \- CertificateStatus

Field | Description  
---|---  
`name` _string_ | Name is unique within a namespace to reference an issuer resource.  
`namespace` _string_ | Namespace defines the space within which the issuer name must be unique.  
  
### KMSKeyConfig

_Appears in:_ \- CertificateAuthoritySpec

Field | Description  
---|---  
`signingKeyRef` _NamespacedName_ | A reference to a SigningKey acting as a CA private key.  
  
### KeyUsageBits

_Underlying type:_ `string` KeyUsageBits defines the different allowed key usages according to RFC 5280 4.2.1.3. Note that many of the key usages below are used for certificates outside the context of TLS, and the implementation of setting non-TLS bits can be implemented as a later feature.

_Appears in:_ \- CertificateProfile

### ManagedSubCAConfig

ManagedSubCAConfig defines the configuration for a SubCA CA certificate.

_Appears in:_ \- CACertificateConfig

Field | Description  
---|---  
`certificateAuthorityRef` _CAReference_ | A reference to a CertificateAuthority which will sign the SubCA certificate. API type: - Group: pki.security.gdc.goog - Kind: CertificateAuthority  
  
### PrivateKeyAlgorithm

_Underlying type:_ `string`

_Appears in:_ \- CertificatePrivateKey \- PrivateKeyConfig

### PrivateKeyConfig

PrivateKeyConfig defines the configuration of the certificate private key

_Appears in:_ \- SecretConfig

Field | Description  
---|---  
`algorithm` _PrivateKeyAlgorithm_ | Algorithm is the private key algorithm of the corresponding private key for this certificate. If provided, allowed values are either `RSA`,`Ed25519` or `ECDSA` If `algorithm` is specified and `size` is not provided, key size of 384 will be used for `ECDSA` key algorithm and key size of 3072 will be used for `RSA` key algorithm. key size is ignored when using the `Ed25519` key algorithm.  
`size` _integer_ | Size is the key bit size of the corresponding private key for this certificate. If `algorithm` is set to `RSA`, valid values are `2048`, `3072`, `4096` or `8192`, and will default to `3072` if not specified. If `algorithm` is set to `ECDSA`, valid values are `256`, `384` or `521`, and will default to `384` if not specified. If `algorithm` is set to `Ed25519`, Size is ignored. No other values are allowed.  
  
### RevocationReason

_Underlying type:_ `string`

_Appears in:_ \- RevokeCertificateRequestSpec

### RevokeCertificateRequest

RevokeCertificateRequest defines a request to revoke a certificate.

_Appears in:_ \- RevokeCertificateRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `RevokeCertificateRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RevokeCertificateRequestSpec_ |   
`status` _RevokeCertificateRequestStatus_ |   
  
### RevokeCertificateRequestList

RevokeCertificateRequestList represents a collection of revoke certificate requests.

Field | Description  
---|---  
`apiVersion` _string_ | `pki.security.gdc.goog/v1`  
`kind` _string_ | `RevokeCertificateRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _RevokeCertificateRequest array_ |   
  
### RevokeCertificateRequestSpec

RevokeCertificateRequestSpec defines a request for the revocation of a certificate.

_Appears in:_ \- RevokeCertificateRequest

Field | Description  
---|---  
`certificateRequestRef` _CertificateRequestReference_ | CertificateRequestRef references a GDC managed CertificateRequest object containing the certificate to revoke.  
`reason` _RevocationReason_ | Reason for revocation. keyCompromise;caCompromise,certificateHold,affiliationChanged; superseded;cessationOfOperation;privilegeWithdrawn;aACompromise  
  
### RevokeCertificateRequestStatus

_Appears in:_ \- RevokeCertificateRequest

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of a certificate to be revoked.  
  
### SecretConfig

SecretConfig defines the configuration for the certificate secret.

_Appears in:_ \- CertificateAuthoritySpec \- CertificateSpec

Field | Description  
---|---  
`secretName` _string_ | The name of the Secret that will hold the private key and signed certificate.  
`secretTemplate` _SecretTemplate_ | Defines annotations and labels to be copied to the Secret.  
`privateKeyConfig` _PrivateKeyConfig_ | Options for the certificate private key  
  
### SecretTemplate

SecretTemplate defines the default labels and annotations to be copied to the Kubernetes Secret resource named in `SecretConfig.SecretName`.

_Appears in:_ \- SecretConfig

Field | Description  
---|---  
`annotations` _object (keys:string, values:string)_ | Annotations is a key value map to be copied to the target Kubernetes Secret.  
`labels` _object (keys:string, values:string)_ | Labels is a key value map to be copied to the target Kubernetes Secret.  
  
### SelfSignedCAConfig

SelfSignedCAConfig defines the configuration for a Root CA certificate.

_Appears in:_ \- CACertificateConfig

### SignedCertStatus

_Appears in:_ \- BYOCertStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | List of status conditions to indicate the status of BYO certificate. - Rejected: Indicates that the certificate does not match with the csr - Ready: Indicates that the certificate is ready to use.  
  
### SignedCertificateConfig

_Appears in:_ \- ExternalCAConfig

Field | Description  
---|---  
`certificate` _integer array_ | The PEM encoded x509 certificate uploaded by the customer.  
`ca` _integer array_ | The PEM encoded x509 certificate of the signer CA used to sign the certificate.  
  
### SubjectConfig

_Appears in:_ \- CertificateConfig

Field | Description  
---|---  
`commonName` _string_ | The common name of the Certificate.  
`organization` _string_ | The organization of the Certificate.  
`locality` _string_ | The locality of the Certificate.  
`state` _string_ | The state of the Certificate.  
`country` _string_ | The country of the Certificate.  
`dnsNames` _string array_ | DNSNames is a list of dNSName subjectAltNames to be set on the Certificate.  
`ipAddresses` _string array_ | IPAddresses is a list of ipAddress subjectAltNames to be set on the Certificate.  
`rfc822Names` _string array_ | RFC822Names is a list of rfc822Name subjectAltNames to be set on the Certificate.  
`uris` _string array_ | URIs is a list of uniformResourceIdentifier subjectAltNames to be set on the Certificate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
