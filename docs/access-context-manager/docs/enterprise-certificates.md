---
url: https://docs.cloud.google.com/access-context-manager/docs/enterprise-certificates/
title: Configure enterprise certificate conditions \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:07.483235+00:00
---

# Configure enterprise certificate conditions  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enterprise-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configure enterprise certificate conditions Stay organized with collections  Save and categorize content based on your preferences. 

A key principle of Chrome Enterprise Premium is that access to services is granted based on contextual information about you and your device. Chrome Enterprise Premium dynamically infers the level of access given to a single user or device by evaluating multiple data sources, and uses this level of trust as part of its decision process.

Access Context Manager is the zero trust policy engine of Chrome Enterprise Premium. Access Context Manager lets you define fine-grained, attribute-based access control for applications and Google Cloud resources.

Use access levels to permit access to resources based on contextual information about the request. By using access levels, you can start to organize tiers of trust. For example, you might create an access level called `High_Level` that permits requests from a small group of highly-privileged individuals. You might also identify a more general group to trust, such as an IP address range that you want to permit requests from. In that case, you might create an access level called `Medium_Level` to permit those requests.

One of the key requirements for zero trust access is to only allow access when the device is managed or owned by the company. There are several ways to determine whether a device is corporate-owned. One way is to determine whether a valid certificate, issued by the company, is on the device. An enterprise certificate on a device can indicate that it's corporate-owned.

Enterprise certificates for Context-Aware Access is a feature of the overall Chrome Enterprise Premium certificate-based access solution. This feature uses device certificates as an alternative context-aware signal to determine whether a device is a corporate-owned asset. This feature is supported on Google Chrome browser version 110 or later.

Because a device can have more than one certificate, you can access enterprise certificates in the custom access level through the macro `.exists(e, p)`:
    
    
    device.certificates.exists(cert, predicate)
    

In the example, `cert` is an identifier used in `predicate`, which binds to the device certificate. The `exists()` macro combines per-element predicate results with the "or" (||) operator, meaning that macros return true if at least one certificate satisfies the `predicate` expression.

The certificate has the following attributes that can be checked together. Note that string comparisons are case-sensitive.

Attribute | Description | Example predicate expression (where `cert` is an identifier of macros)  
---|---|---  
`is_valid` | True if the certificate is valid and not expired (boolean). Checks whether the certificate is unexpired and signed by a trusted anchor. Note that Endpoint Verification doesn't check certificate revocation. | `cert.is_valid`  
`cert_fingerprint` | Fingerprint of the certificate (base64 unpadded SHA256).   
The fingerprint is the unpadded base64 encoded SHA256 digest, in binary format, of the DER-encoded certificate. You can generate the string from the certificate in PEM format using the following procedure with OpenSSL:  ` $ openssl x509 -in cert.pem -out cert.der -outform DER  
$ openssl dgst -sha256 -binary cert.der > digest.sha  
$ openssl base64 -in digest.sha | tr -d =  
` | `cert.cert_fingerprint == origin.clientCertFingerprint()`  
`root_ca_fingerprint` | Fingerprint of the Root CA certificate used to sign the certificate (base64 unpadded SHA256).  
The fingerprint is the unpadded base64-encoded SHA256 digest, in binary format, of the DER-encoded certificate. You can generate the string from the certificate in PEM format using the following procedure with OpenSSL:  ` $ openssl x509 -in cert.pem -out cert.der -outform DER  
$ openssl dgst -sha256 -binary cert.der > digest.sha  
$ openssl base64 -in digest.sha | tr -d =  
` | `cert.root_ca_fingerprint == "ROOT_CA_FINGERPRINT"`  
`issuer` | Issuer name (fully expanded names). To find the issuer name, you can use the following approach: Run the following command on the certificate: ` $ openssl x509 -in ca_1.crt -issuer issuer= /C=US/ST=CA/L=MTV/O=ExampleCorp/OU=ExampleUnit/CN=inter_1/emailAddress=admin@example.com ` To get the issuer string for the access level, reverse the output and replace each forward slash (/) with a comma (,): ` EMAILADDRESS=admin@example.com, CN=inter_1, OU=ExampleUnit, O=ExampleCorp, L=MTV, ST=CA, C=US ` | `cert.issuer == "EMAILADDRESS=admin@example.com, CN=inter_1, OU=ExampleUnit, O=ExampleCorp, L=MTV, ST=CA, C=US"`  
`subject` | Subject name of the certificate (fully expanded names).  | `cert.subject == "CA_SUB"`  
`serial_number` | Serial number of the certificate (string). | `cert.serial_number == "SERIAL_NUMBER"`  
`template_id` | Template ID of the X.509 extension Certificate Template for the certificate (string). | `cert.template_id == "TEMPLATE_ID"`  
  
The following table contains examples of policies that you can set:

Example policy | Expression  
---|---  
The device has a valid certificate signed by the company root certificate. | `device.certificates.exists(cert, cert.is_valid && cert.root_ca_fingerprint == "ROOT_CA_FINGERPRINT")`  
The device has a valid certificate issued by issuer `CA_ABC`. | `device.certificates.exists(cert, cert.is_valid && cert.issuer == "EMAILADDRESS=admin@example.com, CN=inter_1, OU=ExampleUnit, O=ExampleCorp, L=MTV, ST=CA, C=US")`  
**Important:** Endpoint Verification reports a single enterprise device certificate to the Google Admin console, even if multiple certificates are on a device. This means that, regardless of how many enterprise certificates your device has, the Admin console displays only one.

## Configure enterprise certificates

Before configuring enterprise certificates, make sure that you've configured custom access levels. For instructions, see [Creating a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).

You can use an Access Context Manager custom access level definition to set the appropriate policies. Custom access levels use boolean expressions written in a subset of [Common Expression Language (CEL)](https://opensource.google/projects/cel) to test the attributes of a client making a request.

**Important:** For Windows devices, install the client certificate in the user certificate store, not in the computer certificate store. If the client certificate is installed in the computer certificate store, authenticated users must be able to read but not export its private key container for mTLS signing.

### Upload trust anchors in the Admin console

For Chrome Enterprise Premium to collect and validate the device enterprise certificate, you must upload the trust anchors and any intermediary certificates that are used to issue the device certificate. The trust anchors are the self-signed root CA (Certification Authority) certificate and the relevant intermediate and subordinate certificates. Complete the following steps to upload the trust anchors:

  1. Go to the [Admin console](https://admin.google.com/) and navigate to **Devices > Networks > Certificates**.
  2. Select the appropriate organizational unit.
  3. Select **Add Certificate**.
  4. Enter the certificate name.
  5. Upload the certificate.
  6. Select the **Endpoint Verification** checkbox.
  7. Click **Add**.
  8. Ensure that users belong to the organizational unit for which you uploaded the trust anchors.



### Configure an AutoSelectCertificateForUrls policy

For Endpoint Verification to search the device certificate and collect it through Chrome, you must configure the `AutoSelectCertificateForUrls` policy by completing the following steps:

  1. Ensure that the Chrome browser is managed by Chrome Browser Cloud Management.

     * For Windows, macOS, and Linux, set up the cloud-managed Chrome browser using Chrome Enterprise Core. For instructions, see [Sign up for Chrome Enterprise Core](https://support.google.com/chrome/a/answer/9301420).
     * Enroll your device to allow your organization to centrally manage that device. For instructions, see [Enroll cloud-managed Chrome browsers](https://support.google.com/chrome/a/answer/9301891).
  2. In the Admin console, add the `AutoSelectCertificateForUrls` policy:

     1. Go to the [Admin console](https://admin.google.com/) and navigate to **Devices > Chrome > Settings > User & Browser Settings > Client certificates**.
     2. Select the appropriate organizational unit.
     3. Add a policy [AutoSelectCertificateForUrls](https://chromeenterprise.google/policies/?policy=AutoSelectCertificateForUrls), based on the following example:
            
            {"pattern":"https://[*.]clients6.google.com","filter":{"ISSUER":{"CN":"CERTIFICATE_ISSUER_NAME"}}}
            

Replace `CERTIFICATE_ISSUER_NAME` with the common name of the issuer CA. Don't modify the value of `pattern`.


**Note:** Make sure that the filter refers to the issuer certificate that you uploaded in the preceding steps.

To verify the policy configuration, complete the following steps:

  1. Navigate to `chrome://policy` in the browser.
  2. Verify the configured value for **AutoSelectCertificateForUrls**.
  3. Ensure that the policy **Applies to** value is set to **Machine**. On ChromeOS, the value applies to **Current User**.
  4. Ensure that the **Status** for the policy doesn't have a **Conflict**.



## What's next

  * [Troubleshoot enterprise certificate conditions](https://docs.cloud.google.com/access-context-manager/docs/troubleshooting#enterprise-certificate-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
