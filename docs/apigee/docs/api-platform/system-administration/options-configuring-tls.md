---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls/
title: Options for configuring TLS \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:42.972775+00:00
---

# Options for configuring TLS  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Options for configuring TLS Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section shows how to configure TLS for traffic from a proxy to a target.

**Unsupported TLS versions:** Apigee does not support the use of TLS 1.0 or TLS1.1. If you use these protocols in your target endpoint configuration, the Apigee target endpoint throws the error `messaging.adaptors.http.flow.SslHandshakeFailed`.

## About setting TLS options in a target endpoint or target server

A target can be represented by an XML object like the one below:
    
    
    <HTTPTargetConnection>
        <Properties/>
        <URL>https:myTargetAddress</URL>
    ** <SSLInfo>
            <Enabled>true</Enabled>
            <Enforce>true</Enforce>
            <ClientAuthEnabled>true</ClientAuthEnabled>
            <KeyStore>ref://myKeystoreRef</KeyStore>
            <KeyAlias>myKeyAlias</KeyAlias>
            <TrustStore>ref://myTruststoreRef</TrustStore>
            <IgnoreValidationErrors>false</IgnoreValidationErrors>
            <Protocols>myProtocols</Protocols>
            <Ciphers>myCipher</Ciphers>
        </SSLInfo>
    **</HTTPTargetConnection>

The area of the target endpoint configuration that you modify to configure TLS is defined by the `<SSLInfo>` tag. You use the same `<SSLInfo>` tag to configure a target endpoint or target server.

For information about the child elements of `<SSLInfo>`, see [ TLS/SSL TargetEndpoint configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#tlsssltargetendpointconfiguration).

The following table describes the TLS configuration elements used by the `<SSLInfo>` tag:

**Element** | **Description**  
---|---  
`<Enabled>` |  The `<SSLInfo>` block can be used for both one-way and two-way TLS/SSL. If set to `true`, `<Enabled>` specifies that the `<SSLInfo>` block should be used. When set to `false`, the `<SSLInfo>` block is ignored. The default value of `<Enabled>` is `true` if `<URL>` specifies the HTTPS protocol, and `false` if `<URL>` specifies HTTP.  
`<Enforce>` |  Enforces strict SSL between Apigee and the target backend. If set to `true`, connections will fail for targets with invalid certs, expired certs, self-signed certs, certs with a hostname mismatch, and certs with an untrusted root. A failure code of `4xx` or `5xx` is returned. If unset, or set to `false`, the result of connections to target backends with problematic certs depends upon the setting of `<IgnoreValidationErrors>` (see below). A success response (`2xx`) can occur under certain conditions, if `<IgnoreValidationErrors>` is set to `true`.  
`<ClientAuthEnabled>` |  Enables two-way TLS (also known as mutual TLS or mTLS) between Apigee and the API client, or between Apigee and the target backend. Enabling two-way TLS typically requires that you set up a truststore on Apigee and a truststore.  
`<KeyStore>` | A keystore containing private keys used for outbound client authentication  
`<KeyAlias>` | The alias specified when you uploaded a cert and private key to the keystore.  
`<TrustStore>` | A keystore containing trusted server certificates.  
`<IgnoreValidationErrors>` | Indicates whether validation errors are ignored. If the backend system uses SNI and returns a cert with a subject Distinguished Name (DN) that does not match the hostname, there is no way to ignore the error and the connection fails. **Note** : If `<Enforce>` is set to `true`, the value of `<IgnoreValidationErrors>` is ignored.  
`<Ciphers>` |  Supported ciphers for outbound TLS/SSL. If no ciphers are specified, then all ciphers available for the JVM will be permitted. To restrict ciphers, add the following elements listing the supported ciphers:
    
    
    <Ciphers>
     <Cipher>TLS_RSA_WITH_3DES_EDE_CBC_SHA</Cipher>
     <Cipher>TLS_RSA_WITH_DES_CBC_SHA</Cipher>
    </Ciphers>  
  
`<Protocols>` |  Supported protocols for outbound TLS/SSL. If no protocols are specified, then all protocols available for the JVM will be permitted. To restrict protocols, specify them explicitly. For example, to allow only TLS v1.2 or TLS v1.3:
    
    
    <Protocols>
     <Protocol>TLSv1.2</Protocol>
     <Protocol>TLSv1.3</Protocol>
    </Protocols>  
  
## About setting the <KeyStore> and <TrustStore> elements

In the example above, the keystore and truststore are specified by using **references** , in the form:
    
    
    <KeyStore>**ref://myKeystoreRef** </KeyStore>
    <TrustStore>**ref://myTruststoreRef** </TrustStore>

**Warning:** Apigee strongly recommends that you always use references to the keystore and truststore. A reference is a variable that contains the name of the keystore or truststore, rather than specifying the keystore name directly. If you upload a new certificate that does not use a reference but instead specifies the keystore name directly, the runtime Message Processors will **not** automatically detect the change. To resolve this, you must contact Google Cloud Support to restart your Message Processors, which may cause temporary service degradation. 

In this example:

  * **`myKeystoreRef`** is a reference that contains the name of the keystore. In this example, the name of the keystore is **myKeystore**.
  * **`myTruststoreRef`** is a reference that contains the name of the truststore. In this example, the name of the truststore is **myTruststore**.



When a cert expires, you must update the target endpoint/target server to specify the keystore or truststore that contains the new cert. However, if you use references, you can modify the value of the _references_ to reflect the new keystore or truststore names instead of modifying the target endpoint/target server. Changing the value of the reference does not require you to contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/). 

Alternatively, you can specify the keystore name and truststore name directly:
    
    
    <KeyStore>**myKeystore** </KeyStore>
    <TrustStore>**myTruststore** </TrustStore>

If you directly specify the name of the keystore or truststore, then you must contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/).

A third option is to use flow variables:
    
    
    <KeyStore>{**ssl.keystore**}</KeyStore>
    <TrustStore>{**ssl.truststore**}</TrustStore>

You can use flow variables to dynamically specify a keystore or truststore, with an effect similar to using a reference. For more information, see [ Using flow variables to set TLS/SSL values dynamically](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#tlsssltargetendpointconfiguration-usingflowvariablestosettlssslvaluesdynamically).

## About configuring TLS

All Apigee customers, both paid and evaluation, have complete control over the configuration of target endpoints/target servers. In addition, paid Apigee customers have complete control over TLS properties.

### Handling expired certificates

If a TLS certificate expires, or if your system configuration changes such that the certificate is no longer valid, then you need to update the certificate. When configuring TLS for a target endpoint/target server, you should decide how you are going to perform that update before you perform any configuration.

**Note:** You cannot update an existing keystore or truststore to add a new certificate. You must create a new keystore/truststore when updating a certificate. Typically, you create the new keystore/truststore and upload the new cert before the cert in the old keystore/truststore expires. This lets you test the new keystore/truststore and rollback to the old keystore/truststore if there are any issues.

### When a cert expires

On Apigee, you store certs in one of two places:

  * **Keystore** \- Contains the TLS certificate and private key used to identify the entity during TLS handshaking.
  * **Truststore** \- Contains trusted certificates on a TLS client used to validate a TLS server's certificate presented to the client. These certificates are typically self-signed certificates, certificates signed by a trusted CA, or certs used as part of two-way TLS (also known as mutual TLS or mTLS).



The method you use to specify the keystore and truststore in the target endpoint or target server determines how you perform the certificate update. You can use references, direct names, or flow variables. Each method has different repercussions on the update process, as described in the following table:

**Config type** | **How to update/replace cert** | **Usage / Impact**  
---|---|---  
Reference (Recommended) |  **Keystore:** Create a new keystore with a **new name** and an alias with the **same name** as the old alias. **Truststore:** Create a truststore with a **new name**. The alias name does not matter. **Note:** If a certificate is part of a chain, you must either create a single file containing all the certs and upload that file to a single alias, or upload all certs in the chain separately to the truststore using a different alias for each cert. |  Update the reference to point to the new store. No need to contact Apigee Support. No downtime.  
Flow variable |  **Keystore:** Create a new keystore with a **new name** and an alias with the same or new name. **Truststore:** Create a truststore with a **new name**. |  Pass the updated flow variable on each request with the name of the new store. No need to contact Apigee Support. No downtime.  
Direct |  **Method 1: Create a new store (Recommended to avoid downtime)** Create a new keystore or truststore with a **new name** and upload the new cert (and private key if creating a keystore). |  Update your target endpoint or target server configuration to specify the new store name directly, then **redeploy the API proxy**. No need to contact Apigee Support.  
Direct |  **Method 2a: In-place update (Delete & Recreate)** Delete the keystore or truststore and recreate it with the same name. |  API requests will fail during the deletion and recreation window. Because Message Processors cache directly-specified stores, they will not automatically detect the updated certificate. You **must contact[Google Cloud Customer Care](https://cloud.google.com/support-hub/)** to restart the Message Processors.  
Direct |  **Method 2b: In-place update (Truststore upload)** For **truststores only** , upload a new cert directly to the existing truststore. |  Because Message Processors cache directly-specified stores, they will not automatically detect the new certificate. You **must contact[Google Cloud Customer Care](https://cloud.google.com/support-hub/)** to restart the Message Processors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
