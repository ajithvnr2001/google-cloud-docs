---
url: https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy/
title: Add certificate issuance policies \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:11:29.578453+00:00
---

# Add certificate issuance policies  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add certificate issuance policies

Adding certificate issuance policies in CA Service involves defining rules and restrictions that govern the types of certificates issued by a certificate authority (CA). To learn more about certificate issuance policies, see [About certificate issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#issuance-policies).

A certificate issuance policy lets you specify the subject and subject alternative names (SANs) that can be included in the issued certificates. You can specify the certificate issuance policy while creating a CA pool or you can update an existing CA pool to add an issuance policy.

For more information, see [Overview of templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#issuance-policies).

**Caution:** The issuance policy changes are effective immediately. Before using the issuance policy in production, we recommend that you try out the policy changes on a test CA pool instance.

## Before you begin

  * Make sure you have the CA Service Operation Manager (`roles/privateca.caManager`) or the CA Service Admin (`roles/privateca.admin`) IAM role. For information about granting an IAM to a principal, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

  * [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).




You can add a certificate issuance policy to a CA pool while creating a CA pool or when updating an existing CA pool.

Use one of the following methods:

### Console

  1. Go to the **Certificate Authority Service** page in the Google Cloud console. [Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. On the **CA pool manager** page, click the name of the CA pool for which you want to add a certificate issuance policy.

  3. On the **CA pool** page, click edit**Edit**.


**Define base key usage**

This setting refers to the `Key Usage` field within a digital certificate. It specifies how the certificate's private key can be used, such as for key encipherment, data encipherment, certificate signing, and CRL signing. For more information, see [Key usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3). 

  1. To select the base key usages, click the **Specify base key usages for certificates issued from this CA pool** toggle, and then select from the options listed.
  2. Click **Next**.

**Define extended key usage**

This setting refers to the `Extended Key Usage (EKU)` field in a digital certificate. It provides more specific and refined restrictions on how the key can be used, such as for server authentication, client authentication, code signing, and email protection. For more information, see [Extended key usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12). 

Extended key usages are defined using object identifiers (OIDs). If you don't configure the extended key usages, all key usage scenarios are allowed. 

  1. To select the extended key usages, click the **Write extended key usages for certificates issued from this CA pool** toggle, and then select from the options listed.
  2. Click **Next**.

**Define policy identifiers**

The certificate policies extension in the certificate expresses the policies that the issuing CA pool follows. This extension can include information about how identities are validated before certificate issuance, how certificates are revoked, and how the CA pool's integrity is ensured. This extension helps you verify the certificates that the CA pool issues and see how the certificates are used. 

For more information, see [Certificate policies](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.4). 

To specify the policy that defines the certificate usage, do the following: 

  1. Add the policy identifier in the **Policy identifiers** field. 
  2. Click **Next**. 

**Add Authority information access (AIA) OCSP servers**

The AIA extension in a certificate provides the following information: 

  * Address of the OCSP servers from where you can check the revocation status of the certificate. 
  * The access method for the issuer of the certificate. 



For more information, see [Authority information access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.1). 

To add the OCSP servers that appear in the AIA extension field in the certificates, do the following: 

  1. Click **Add item**. 
  2. In the **Server URL** field, add the URL of the OCSP server. 
  3. Click **Done**. 
  4. Click **Next**. 

**CA options**

The **CA options** field within a certificate template defines how the resulting certificate can be used in a certificate authority (CA) hierarchy. CA options determine if a certificate can be used to sign other certificates and, if so, the restrictions on the certificates it issues.

Choose from the following options:

  1. **Include the configs to describe the CA X.509 extensions** : Specify the settings within a certificate template that control the X.509 extensions.

  2. **Restrict issued certificates to be used only for CAs** : This option appears only if you select the checkbox mentioned in the previous step. This boolean value indicates whether the certificate is a CA certificate. If set to `true`, the certificate can be used to sign other certificates. If `false`, the certificate is an end-entity certificate and cannot sign other certificates. If you click this toggle, you are further prompted to define name constraints for the extension in CA certificates.

  3. **Include the configs to describe the path length restriction X.509 extensions** : Specify the settings that control how long a chain of certificates can be, stemming from a particular certificate. If the max issuer path length is set to `0`, then the CA can only issue end-entity certificates. If it's set to `1`, then the chain beneath this CA certificate can include only one subordinate CA. If a value isn't declared, then the number of subordinate CAs in the chain beneath this CA is unbounded.

  4. Click **Next**.

**Configure additional extensions**

To configure additional custom extensions to include in the certificates issued by the CA pool, do the following: 

  1. Click **Add item**. 
  2. In the **Object identifier** field, add a valid object identifier that is formatted as dot-separated digits. 
  3. In the **Value** field, add the base64-encoded value for the identifier. 
  4. If the extension is critical, select **Extension is critical**. 



To save all the baseline value configurations, click **Done**. 

### gcloud

To use the Google Cloud CLI to add a certificate issuance policy to a CA pool, you must create a YAML file that describes the restrictions on the certificates that the CA pool can issue. The content corresponds to an [IssuancePolicy](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy).

  1. Using the Cloud Shell Editor, create a file `policy.yaml` with the following content:
         
         identityConstraints:
           allowSubjectPassthrough: true
           allowSubjectAltNamesPassthrough: true
         

Where:

     * The `allowSubjectPassthrough` field is required. If the `allowSubjectPassthrough` field is set to `true`, the subject field is copied from a certificate request into the signed certificate. Otherwise, the requested Subject is discarded.
     * If the `allowSubjectAltNamesPassthrough` field is set to `true`, the SubjectAltNames extension is copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames is discarded.
  2. To update a CA pool's certificate issuance policy using the file created in the previous step, run the following command:
         
         gcloud privateca pools update POOL_NAME --location LOCATION --issuance-policy FILE_PATH
         

Replace the following:

     * POOL_NAME: the name of the CA pool
     * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
     * FILE_PATH: the path of the `policy.yaml` file

For more information about the `gcloud privateca pools update` command, see [gcloud privateca pools update](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/update).




## Supported restrictions

CA Service supports the following issuance policy restrictions. You can combine the following restrictions as necessary to build a custom certificate issuance policy.

### Restrict or force allowed X.509 values

A CA pool can restrict the allowed X.509 values in certificate requests by configuring the [passthrough_extensions](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.passthrough_extensions) field.

A CA pool can also explicitly specify X.509 values to be added to all its issued certificates, overwriting any requested values, by using the [baseline_values](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.baseline_values) field.

The [baseline_values](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.baseline_values) values of a CA pool allow specifying the following properties:

  * [Key Usage](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#KeyUsage)
  * [CA Options](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#CaOptions)
  * [AIA OCSP Servers](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters)
  * [Additional X.509 Extensions](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Extension)



You can also use these options together.

If you update any part of the `baseline_values` field, the update replaces the entire set of values in the `baseline_values` field.

  * **Example** : Restrict a CA to issue only end-entity certificates with X.509 values for mutual TLS (mTLS).

### policy.yaml
        
        baselineValues:
          caOptions:
            isCa: false
          keyUsage:
            baseKeyUsage:
              digitalSignature: true
              keyEncipherment: true
            extendedKeyUsage:
               clientAuth: true
               serverAuth: true
        

  * **Example** : Restrict a CA to issue only end-entity code signing certificates with a baseline AIA OCSP URL.

### policy.yaml
        
        baselineValues:
          caOptions:
            isCa: false
          keyUsage:
            baseKeyUsage:
              digitalSignature: true
            extendedKeyUsage:
              codeSigning: true
          aiaOcspServers:
            -   "http://foo.bar/revocation"
          additionalExtensions:
          -   objectId:
                objectIdPath:
                  -   1
                  -   2
                  -   3
              critical: false
              value: "base64 encoded extension value"
        




For more information about the certificate profile for end-entity mTLS, see [End-entity mTLS](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile#end-mtls).

### Restrict allowed identity fields

To restrict the identity of certificates issued through a CA pool, you can add a [Common Expression Language (CEL)][4]{: .external} expression to the issuance policy's [identity_constraints](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.identity_constraints) field. The CEL expressions allow arbitrary restrictions over the Subject Domain Name (including the common name) and the SANs of a certificate.

For more information about using a CEL expression to restrict Subject and SANs, see [Using CEL](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).

  * **Example** Allow the CA to issue only certificates matching a specified Subject.

### policy.yaml
        
        identityConstraints:
          allowSubjectPassthrough: true
          allowSubjectAltNamesPassthrough: false
          celExpression:
            expression: 'subject.organization == "Example LLC" && subject.country_code in ["US", "UK"]'
        

The `celExpression` field is optional. Use a Common Expression Language (CEL) expression to validate the resolved X.509 subject and SAN before a certificate is signed. For more information about using CEL expressions, see [Using CEL](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).

  * **Example** : Allow only SANs having DNS Names as `us.google.org` or ending in `.google.com`.

### policy.yaml
        
        identityConstraints:
          allowSubjectPassthrough: false
          allowSubjectAltNamesPassthrough: true
          celExpression:
            expression: 'subject_alt_names.all(san, san.type == DNS && (san.value == "us.google.org" || san.value.endsWith(".google.com")) )'
        

  * **Example** : Allow only SANs having URIs `https://google.com/webhp` or starting with `spiffe://example-trust-domain-1/ns/namespace1/sa/`.

### policy.yaml
        
        identityConstraints:
          allowSubjectPassthrough: false
          allowSubjectAltNamesPassthrough: true
          celExpression:
            expression: 'subject_alt_names.all(san, san.type == URI && (san.value == "https://google.com/webhp" || san.value.startsWith("spiffe://example-trust-domain-1/ns/namespace1/sa/")) )'
        

  * **Example** : Allow only SANs having email addresses `example@google.com` or ending with `@google.org`.

### policy.yaml
        
        identityConstraints:
          allowSubjectPassthrough: false
          allowSubjectAltNamesPassthrough: true
          celExpression:
            expression: 'subject_alt_names.all(san, san.type == EMAIL && (san.value == "example@google.com" || san.value.endsWith("@google.org")) )'
        

  * **Example** : Allow only custom SANs having a specific OID and a custom value.

### policy.yaml
        
        identityConstraints:
          allowSubjectPassthrough: false
          allowSubjectAltNamesPassthrough: true
          celExpression:
            expression: 'subject_alt_names.all(san, san.type == CUSTOM && san.oid == [1, 2, 3, 4] && san.value == "custom-data" )'
        




### Configure certificate backdating

You can configure backdating to set a past _not_before_time_ for issued certificates. There are two mutually exclusive ways to configure this in the issuance policy:

#### Option 1: Automatic pool-level backdating

All certificates issued from this CA pool are automatically backdated by a fixed duration.

Use the **[backdate_duration](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.backdate_duration)** field. Certificates have a _not_before_time_ equal to the issuance time minus the specified duration. The _not_after_time_ is adjusted to maintain the requested lifetime. The **backdate_duration** must be less than or equal to 48 hours.

**Example**

To backdate certificates by 1 hour:

### policy.yaml
    
    
    backdateDuration: 3600s
    

#### Option 2: Requester-specified custom backdating

Allows requesters to specify a custom `not_before_time` for each certificate request.

Use the **[allow_requester_specified_not_before_time](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.allow_requester_specified_not_before_time)** field. When set to `true`, requesters can provide a specific `requested_not_before_time` when creating a certificate.

**Limits:**

  * Cannot be in the future.
  * Must be less than or equal to 48 hours in the past.
  * Must be after or the same as the issuing CA's `not_before_time` (i.e., its creation time).



**Example**

To allow custom backdating:

### policy.yaml
    
    
    allowRequesterSpecifiedNotBeforeTime: true
    

After configuring this policy on the CA pool, requesters must then specify a start time (with the `requested_not_before_time` flag) in each certificate request (for example, using the `--requested-not-before-time` flag in `gcloud`).

### Restrict maximum lifetime of the issued certificates

To restrict the lifetime of the issued certificates, use the [maximum_lifetime](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.maximum_lifetime) field. If a certificate's requested lifetime is larger than the maximum lifetime, the certificate's lifetime is explicitly truncated.

**Note:** A certificate can never outlive its issuing CA. If a certificate request mentions a lifetime that exceeds the CA's `not_after_time` date, its lifetime is truncated to match the CA's `not_after_time` date. The certificate's lifetime is truncated even if the certificate issuance policy allows a longer lifetime.

#### Example

To allow a maximum lifetime of 30 days, use the following `policy.yaml` file:

### policy.yaml
    
    
    maximumLifetime: 2592000s
    

### Restrict allowed certificate issuance modes

You can request a certificate either through a Certificate Signing Request (CSR) or an inline description of the requested values. Some organizations might prefer to add limitations on the option that can be used because the latter method doesn't require a proof of possession of the associated private key. You can set these limitations using the [allowedIssuanceModes][1] field.

For more information about specifying the ways in which certificates can be requested from a CA pool, see [IssuanceModes][2].

For more information about requesting certificates, see [Create a certificate request](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).

  * **Example** : Allow only CSR issuance.




### policy.yaml
    
    
    allowedIssuanceModes:
      allowCsrBasedIssuance: True
      allowConfigBasedIssuance: False
    

### Restrict the public key algorithms of the certificate request

To restrict the minimum key length and the public key algorithms that certificates can use, you can use the [allowedKeyTypes][3] field in the certificate issuance policy YAML file. If this field is specified, then the certificate request's public key must match one of the key types listed in the YAML file. If this field isn't specified, then you can use any key, with the exception of RSA keys whose modulus size is less than 2048 bits. If you want to use a RSA key with modulus size less than 2048 bits, you must explicitly allow it using the certificate issuance policy.

**Example** : Allow RSA keys with a modulus size between 3072 bits and 4096 bits (inclusive), or Elliptic Curve Digital Signature Algorithm (ECDSA) keys over the NIST P-256 curve.

### policy.yaml
    
    
    allowedKeyTypes:
    -   rsa:
      minModulusSize: 3072
      maxModulusSize: 4096
    -   ellipticCurve:
          signatureAlgorithm: ECDSA_P256
    

You can choose one of the following elliptic curve signature algorithms:

  * `EC_SIGNATURE_ALGORITHM_UNSPECIFIED` \- Any signature algorithm may be used.
  * `ECDSA_P256` \- Elliptic Curve Digital Signature over the NIST P-256 curve.
  * `ECDSA_P384` \- Elliptic Curve Digital Signature over the NIST P-384 curve.
  * `EDDSA_25519` \- Edwards-curve Digital Signature Algorithm over curve 25519, as described in RFC 8410.



## What's next

  * Learn more about [certificate profiles](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile).
  * Learn more about [requesting certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).
  * Learn how to [configure IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).
  * Learn how to [use Common Expression Language (CEL)](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).
  * Learn how to [manage various policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls).



[1]: /certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.allowed_issuance_modes [2]: /certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuanceModes [3]: /certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#IssuancePolicy.FIELDS.allowed_key_types

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
