---
url: https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template/
title: Create a certificate template \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:05:59.309435+00:00
---

# Create a certificate template  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a certificate template

This page describes the attributes of a certificate template and explains how you can create a certificate template. To learn more about certificate templates, see [About certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#certificate-template).

## Required roles

To get the permissions that you need to create a certificate template, ask your administrator to grant you the [CA Service Operation Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.caManager) (`roles/privateca.caManager`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a certificate template

To create a certificate template, use one of the following methods:

### Console

  1. Go to the **Certificate Authority Service** page in the Google Cloud console.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **Template manager** tab, and then click **Create template**.

  3. Select a location for the certificate template using the **Region** list. This must be the same location as the CA pool that you intend to use with the certificate template.

  4. Enter a unique identifier for the certificate template in the **Certificate template ID** field. Optionally, provide a description for the certificate template.

  5. Click **Next**.

  6. If you want to configure default x.509 values for certificates that use this template, click the **Include predefined values in certificates issued using this certificate template** toggle. Then, click **Configure predefined values**.

  7. Set up the predefined values using the following information:

**Define base key usage**

This setting refers to the `Key Usage` field within a digital certificate. It specifies how the certificate's private key can be used, such as for key encipherment, data encipherment, certificate signing, and CRL signing. For more information, see [Key usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3). 

     1. To select the base key usages, click the **Specify base key usages for certificates issued from this CA pool** toggle, and then select from the options listed.
     2. Click **Next**.

**Define extended key usage**

This setting refers to the `Extended Key Usage (EKU)` field in a digital certificate. It provides more specific and refined restrictions on how the key can be used such as for server authentication, client authentication, code signing, email protection, and more. For more information, see [Extended key usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12). 

Extended key usages are defined using object identifiers (OIDs). If you don't configure the extended key usages, all key usage scenarios are allowed. 

     1. To select the extended key usages, click the **Write extended key usages for certificates issued from this CA pool** toggle, and then select from the options listed.
     2. Click **Next**.

**Define policy identifiers**

The certificate policies extension in the certificate expresses the policies that the issuing CA pool follows. This extension can include information about how identities are validated before certificate issuance, how certificates are revoked, and how the CA pool's integrity is ensured. This extension helps you verify the certificates that the CA pool issues and see how the certificates are used.

For more information, see [Certificate policies](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.4). 

To specify the policy that defines the certificate usage, do the following:

     1. Optional: Add the policy identifier in the **Policy identifiers** field.
     2. Click **Next**.

**Add Authority information access (AIA) OCSP servers**

The AIA extension in a certificate provides the following information:

     * Address of the OCSP servers from where you can check the revocation status of the certificate.
     * The access method for the issuer of the certificate.

For more information, see [Authority information access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.1).

Adding OCSP servers is optional. To add the OCSP servers that appear in the AIA extension field in the certificates, do the following:

     1. Click **Add item**.
     2. In the **Server URL** field, add the URL of the OCSP server.
     3. Click **Done**.
     4. Click **Next**.

**CA options**

The **CA options** field within a certificate template defines how the resulting certificate can be used in a Certificate Authority (CA) hierarchy. It essentially determines if a certificate can be used to sign other certificates, and if so, any restrictions on the certificates it issues.

Choose from the following options:

     1. **Include the configs to describe the CA X.509 extensions** : Specify the settings within a certificate template that control the X.509 extensions.

     2. **Restrict issued certificates to be used only for CAs** : This option appears only if you select the checkbox mentioned in the previous step. This boolean value indicates whether the certificate is a CA certificate. If set to `true`, the certificate can be used to sign other certificates. If `false`, it's an end-entity certificate and cannot sign other certificates. If you click this toggle, you are further prompted to define name constraints for the extension in CA certificates.

     3. **Include the configs to describe the path length restriction X.509 extensions** : Specify the settings that control how long a chain of certificates can be, stemming from a particular certificate.It specifies the maximum number of CAs that can be chained up to this CA certificate. If the max issuer path length is set to `0`, then the CA can only issue end-entity certificates. If it's set to `1`, then the chain beneath this CA certificate can include only one subordinate CA. If a value isn't declared, then the number of subordinate CAs in the chain beneath this CA is unbounded.

     4. Click **Next**.

**Configure additional extensions**

Optional: You can configure additional custom extensions to include in the certificates issued by the CA pool. Do the following:

     1. Click **Add item**.
     2. In the **Object identifier** field, add a valid object identifier that is formatted as dot-separated digits.
     3. In the **Value** field, add the base64-encoded value for the identifier.
     4. If the extension is critical, select **Extension is critical**.
  8. To save all the predefined values, click **Done**.

  9. Next, go to the **Configure extension constraints** section. Select any one of the following options: 

     * **Copy all the extensions from certificate requests to the certificate**
     * **Drop all extensions from certificate requests**
     * **Copy specific extensions from certificate requests to the certificate**
  10. If you choose to copy specific extensions, you can do the following:
     * Click the **Known certificate extensions** field, and clear the unrequired extensions from the list.
     * In the **Custom extensions** field, add the object identifiers for extensions you want to be included in the certificates that the CA pool issues.
  11. Click **Next** , and go to the **Configure identity constraints** section. To configure constraints on the subject and SANs in the certificates that the CA pool issues, select one or both of the following options: 

     * **Copy subject from the certificate requests to the certificate**
     * **Copy subject alternative names (SAN) from the certificate requests to the certificate**
Optional: In the **Configure identity constraints** section, add a Common Expression Language (CEL) expression to define restrictions on certificate subjects. For more information, see [Using CEL](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).
  12. Click **Next** , and then click, **Done**.




### gcloud
    
    
    gcloud privateca templates create TEMPLATE_ID \
      --copy-subject \
      --copy-sans \
      --identity-cel-expression <expr> \
      --predefined-values-file FILE_PATH \
      --copy-all-requested-extensions \
      --copy-extensions-by-oid <1.2.3.4,5.6.7.8> \
      --copy-known-extensions <ext1,ext2>
    

Replace the following:

  * TEMPLATE_ID: the unique identifier of the certificate template
  * FILE_PATH: the YAML file that describes the X.509 values set by the certificate template



The `--copy-sans` flag allows the Subject Alternative Name (SAN) extension from the certificate request to be copied into the signed certificate. You can alternatively specify `--no-copy-sans` to drop any caller specified SANs from the certificate request.

The `--copy-subject` flag allows the Subject from the certificate request to be copied into the signed certificate. You can alternatively specify `--no-copy-subject` to drop any caller specified subjects from the certificate request.

**Note:** If you want to ensure that a template must be used with identity reflection, specify the `--no-copy-subject` and `--no-copy-sans` flags together. For more information about identity reflection, see [Identity reflection](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).

The `--identity-cel-expression` flag takes a CEL expression that is evaluated against the Subject and Subject Alternative Name of the certificate before it is issued, and returns a boolean signifying whether the request should be allowed. For information about using a Common Expression Language (CEL) expression for a certificate template, see [Using CEL for certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#templates).

The `--predefined-values-file` flag specifies the path to a YAML file describing any predefined X.509 values set by this template. The provided extensions are copied over to any certificate requests that use this template, taking precedence over any allowed extensions in the certificate request. If you update any part of the predefined X.509 values, the update replaces the entire set of the predefined X.509 values.

If the `--copy-all-requested-extensions` flag is set, all the extensions specified in the certificate request are copied into the signed certificate. 

If the `--copy-extensions-by-oid` flag is set, specific OIDs are copied from the certificate request into the signed certificate.

If the `--copy-known-extensions` flag is set, specific extensions are copied from the certificate request into the signed certificate. These known extensions can be one of the following: `base-key-usage`, `extended-key-usage`, `ca-options`, `policy-ids`, or `aia-ocsp-servers`.

**Note:** The tag `--copy-all-requested-extensions` flag is mutually exclusive from `--copy-known-extensions` and `--copy-extensions-by-oid` flags.

Remove the `--copy-all-requested-extensions` flag to ignore all X.509 extensions in the certificate request, but still keep predefined values defined in this template.

**Note:** If you delete resources such as CA pools, certificate authorities, and certificate templates, you will not be able to create a new resource of that type with the same name in the same project and location.

Here's a sample certificate template configuration:
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        keyEncipherment: true
        contentCommitment: false
        dataEncipherment: false
        keyAgreement: false
        certSign: false
        crlSign: false
        encipherOnly: false
        decipherOnly: false
      extendedKeyUsage:
        serverAuth: true
        clientAuth: false
        codeSigning: false
        emailProtection: false
        timeStamping: false
        ocspSigning: false
    caOptions:
      isCa: true
      maxIssuerPathLength: 1
    policyIds:
    - objectIdPath:
      - 1
      - 2
      - 3
    additionalExtensions:
    - objectId:
        objectIdPath:
        - 1
        - 2
        - 3
      critical: false
      value: "base64 encoded extension value"
    

Values not specified in the YAML are either omitted or defaulted to `false`.

The following extensions are omitted if a value isn't specified:

  * `keyUsage`
  * `policyIds`
  * `additionalExtensions`
  * `maxIssuerPathLength` field in the `caOptions` extension



The following extensions default to `false` if a value isn't specified:

  * `isCa` field in the `caOptions` extension



## Create a certificate template for common scenarios

This section provides `gcloud` commands for creating a certificate template for common use cases.

### DNS server TLS certificates for any domain

To create a certificate template for issuing server TLS certificates that allow any domain, use the following instructions:

  1. Create a file with the name `leaf_server_tls_values.yaml` and add the following end-entity server TLS configuration to it:

### leaf_server_tls_values.yaml
         
         keyUsage:
           baseKeyUsage:
             digitalSignature: true
             keyEncipherment: true
           extendedKeyUsage:
             serverAuth: true
         caOptions:
           isCa: false
         

  2. To only allow certificates with `DNS`-type SANs, execute following `gcloud` command:

### gcloud
         
         gcloud privateca templates create server-tls \
           --predefined-values-file leaf_server_tls_values.yaml \
           --copy-sans --no-copy-subject \
           --identity-cel-expression "subject_alt_names.all(san, san.type == DNS)"
         

For more information about the `gcloud privateca templates create` command, see [gcloud privateca templates create](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/create).




### DNS server TLS certificates with only test domains

To create a certificate template for issuing server TLS certificates with DNS SANs limited to test domains, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca templates create server-tls \
      --predefined-values-file leaf_server_tls_values.yaml \
      --copy-sans --no-copy-subject \
      --identity-cel-expression "subject_alt_names.all(san, san.type == DNS && san.value.endsWith('.test.example.com'))"
    

The contents of the `leaf_server_tls_values.yaml` file must be the same as the previous example.

For more information about using CEL expressions to ensure DNS names start or end with a particular string, see [CEL example expressions](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#template-examples).

### Workload identity certificates

To create a certificate template for issuing mutual TLS (mTLS) certificates, use the following instructions:

  1. Create a file with the name `leaf_mtls_values.yaml` and add the following end-entity mutual TLS configuration to it.

### leaf_mtls_values.yaml
         
         keyUsage:
           baseKeyUsage:
             digitalSignature: true
             keyEncipherment: true
           extendedKeyUsage:
             serverAuth: true
             clientAuth: true
         caOptions:
           isCa: false
         

  2. To only allow certificates with [SPIFFE](https://spiffe.io/) URI SANs, use the following `gcloud` command:

### gcloud
         
         gcloud privateca templates create workload-spiffe \
           --predefined-values-file leaf_mtls_values.yaml \
           --copy-sans --no-copy-subject \
           --identity-cel-expression "subject_alt_names.all(san, san.type == URI && san.value.startsWith('spiffe://'))"
         

For more information about the `gcloud privateca templates create` command, see [gcloud privateca templates create](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/create).




For more information about using CEL expressions to ensure DNS names start or end with a particular string, see [CEL example expressions](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#examples).

## Grant access to the certificate template

You can use a certificate template if you have the CA Service Certificate Template User (`roles/privateca.templateUser`) role. We recommend that the authors of a certificate template grant the CA Service Certificate Template User role to the members in the organization who might use that certificate template.

To grant the CA Service Certificate Template User (`roles/privateca.templateUser`) role to everyone in the `example.com` domain, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca templates add-iam-policy-binding TEMPLATE_ID \
      --member "domain:example.com" \
      --role "roles/privateca.templateUser"
    

Replace the following:

  * TEMPLATE_ID: the unique identifier of the certificate template



For more information about the `gcloud privateca templates add-iam-policy-binding` command, see [gcloud privateca templates add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/add-iam-policy-binding).

For more information about IAM roles for CA Service, and their associated permissions, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

## What's next

  * Learn about [Common Expression Language](https://github.com/google/cel-spec).
  * Learn how to [use Common Expression Language](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).
  * Learn about [certificate profiles](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
