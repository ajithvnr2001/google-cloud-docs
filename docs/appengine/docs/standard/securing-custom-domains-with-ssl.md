---
url: https://docs.cloud.google.com/appengine/docs/standard/securing-custom-domains-with-ssl/
title: Securing custom domains with SSL \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:52.134845+00:00
---

# Securing custom domains with SSL  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/securing-custom-domains-with-ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Securing custom domains with SSL Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in March 2025, support for TLS version 1.1 and earlier is deprecated. Upgrade your applications to use TLS version 1.2 and later. For more information, see [Secure your app with minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

App Engine SSL support offers globally distributed SSL endpoints and built-in load balancing to serve your app securely, reliably, and quickly to a worldwide audience.

By default, HTTPS connections on your custom domain are enabled automatically using managed SSL certificates. After [mapping a custom domain to your application and updating your DNS records](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains), App Engine provisions a managed SSL certificate, renews the certificate, and revokes it when you remove the custom domain from your application.

## Before you begin

  * Make sure you have already [set up your custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains) in your App Engine project.

  * If you use Cloud Load Balancing and [serverless network endpoint group (NEGS)](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to route traffic to your App Engine app, we recommend that you map your custom domain to the load balancer instead of directly to your app, and use Google-managed SSL certificates that are created for the load balancer. This eliminates the need to manage separate SSL certificates for each serverless app. With Cloud Load Balancing, you can set SSL policies that control the features of SSL that your load balancer negotiates with clients.

For more information, see the following pages:

    * [Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)
    * [Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
    * [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)

Note the following limitation:

    * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/standard/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.

**Note:** These instructions describe using the Google Cloud console to secure custom domains. If you prefer, you can use [gcloud commands](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings) or the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings).

## Verify a managed certificate

After you [set up your custom domain and update the DNS records](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains), a managed SSL certificate is automatically provided within a few minutes. Selection of the certificate authority is automatic; the managed certificate is signed either by Google Trust Services (GTS) or [Let's Encrypt](https://letsencrypt.org/).

To verify that the certificate was provisioned:

  1. In the Google Cloud console, go to **App Engine** > **Settings** > **Custom Domains** :

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  2. The **SSL security** displays as **Google-managed**.




## Troubleshoot managed SSL certificates

  * You might need to [update the DNS records for your custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains#dns_update) to verify your domain name. App Engine cannot provision certificates for unverified domains.

  * You can check the status of your certificate with the Admin API by using an [AuthorizedCertificate.GET request](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/get).

  * If a managed certificate has not been provisioned because the DNS records are not available, the [`ManagedCertificate.ManagementStatus`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates#managementstatus) field might be `FAILED_RETRYING_NOT_VISIBLE`. Verify that your DNS records are up to date, wait a few minutes, then try again. It can take up to 24 hours for DNS records to become available.

  * If the status is `FAILED_PERMANENT`, then all renewal attempts have failed. Check your DNS settings then update your custom domain mapping by following the steps to update to managed SSL certificates.




## Upgrade to managed SSL certificates

Before you upgrade to Google-managed SSL certificates, note that managed certificates **do not support** wildcard mappings.

If you are using subdomains and the certificate is issued by Let's Encrypt, there is a limit of [50 managed certificates](https://letsencrypt.org/docs/rate-limits/) per week for each base domain. If you encounter the limit, App Engine keeps trying to issue managed certificates until all requests have been fulfilled.

To move from your own SSL certificates to Google-managed SSL certificates, or to add managed SSL certificates to an existing app with a custom domain, update your domain mapping:

  1. In the Google Cloud console, go to **App Engine** > **Settings** > **Custom Domains** :

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  2. Select the domain you want to secure, and click **Enable managed security**.




## Disable managed SSL certificates

To disable managed SSL certificates:

  1. In the Google Cloud console, go to **App Engine** > **Settings** > **Custom Domains** :

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  2. Select the domain and click **Disable managed security**.




## Use your own SSL certificates

Instead of using managed SSL certificates, you can use your own certificate. If your certificate does not have a [transparency proof](https://www.certificate-transparency.org/getting-started), your app may show SSL warnings in Chrome due to certificate transparency proof enforcement. For more information on certificate transparency proofs and how to comply, read [Enforcing Certificate Transparency](https://groups.google.com/a/chromium.org/forum/#!msg/ct-policy/sz_3W_xKBNY/6jq2ghJXBAAJ).

To use and manage your own SSL certificates instead of Google-managed certificates:

  1. Make sure you have already [set up your custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains#mapping_a_custom_domain_to_your_app) in your App Engine project.

  2. Disable the default Google-managed certificates.

  3. Get a certificate for your domain from the certificate authority (CA) of your choice. The exact procedure can vary depending on the authority.

  4. Convert your private key and SSL certificate files into formats that are supported by App Engine. Before you can upload your files, your private key must be converted to an RSA private key and your SSL certificates must be concatenated into a single file.

  5. Ensure you have the right permissions in the [Google Cloud console](https://console.cloud.google.com/appengine/settings/domains) and [verified ownership](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains#mapping_a_custom_domain_to_your_app) (step 3) of all related domains or their parent domains. For example:

     * If the certificate is for `www.example.com` you can verify ownership of either `www.example.com` or `example.com`.
     * If the certificate is for `www.example.com` and `sub.example.com` you can either verify ownership of both `www.example.com` and `sub.example.com`, or of `example.com`.
     * If the certificate is for `*.example.com` you must verify ownership of `example.com`.
  6. Upload your private key and SSL certificate, and then map your domain to your app: 

     1. In the Google Cloud console, go to **App Engine** > **Settings** > **SSL certificates** : 

[Go to SSL Certificates](https://console.cloud.google.com/appengine/settings/certificates)

     2. Click **Upload a new certificate**. 

     3. Upload your concatenated SSL certificate under `PEM encoded X.509 public key certificate`, for example `concat.crt`, and then upload your RSA private key under **Unencrypted PEM encoded RSA private key** , for example `myserver.key.pem`. 
     4. Click **Upload**. Each SSL certificate that you upload is visible and available for use by all of your other Google Cloud projects so you don't have to upload the same certificate repeatedly. **Note** : If you upload an SSL certificate but never assign it to a domain, that certificate is automatically deleted after 30 days. 
     5. Select the certificate that you want to assign to a domain and then click **Save** to use SSL for that domain. 
  7. Test your changes by visiting your domain in your browser, using `https`, for example, `https://www.example.com`.

**Note:** Once the private key is uploaded, it is stored securely at Google and cannot be viewed.



### Transfer mappings from a serving certificate to a new certificate

**Important:** The instructions that follow apply to certificates serving in [SNI](https://wikipedia.org/wiki/Server_Name_Indication) serving mode only.

When a certificate nears its expiration date, you'll need to upload a new certificate and transfer the old certificate's existing mappings to that new certificate. The following procedure assumes that the existing certificate has not yet expired and is currently serving your custom domain.

To transfer mappings from an actively serving certificate:

  1. Get a new certificate for your domain from the certificate authority (CA) of your choice.

  2. Convert your private key and SSL certificate files into formats that are supported by App Engine.

  3. Upload your RSA private key and concatenated SSL certificate:

     1. Upload the SSL certificate in the **SSL certificates** page.

[Go to SSL Certificates](https://console.cloud.google.com/appengine/settings/certificates)
        1. Click **Upload a new certificate**.

        2. Upload your concatenated SSL certificate under **PEM encoded X.509 public key certificate** , for example `concat.crt`, and then upload your RSA private key under **Unencrypted PEM encoded RSA private key** , for example `myserver.key.pem`. 
        3. Click **Upload**. 
     2. Select the new certificate you just added from the certificate list, then select the domain being served by the old certificate. 
     3. Click **Save** to transfer the mappings from the old certificate to the new one. 



### Obtain a certificate

The process for getting an SSL certificate will vary depending on the certificate authority that you use. The instructions provided here might need to be adjusted slightly. Typically, each certificate authority provides instructions to assist you through the process.

To obtain a certificate for use with your App Engine app:

  1. Generate your private key and a certificate signing request (CSR) by using the [openssl](https://www.openssl.org/source/) tool:

     1. Run the following command from a directory where you want to create the `server.csr` file:
            
            openssl req -nodes -newkey rsa:2048 -keyout [MY_PRIVATE_KEY].key -out [MY_CSR].csr
            

where:

        * `[MY_PRIVATE_KEY].key` is the generated file where your private key is stored. Example: `myserver.key`
        * `[MY_CSR].csr` is the generated file for your certificate signing request. Example: `server.csr`
     2. When prompted, enter the following information:

        * Your 2-digit country code, for example, `US` for United States.
        * Your city name.
        * Your company name. You can use your own name if you don't have a company.
        * Your organizational unit or `NA` if you don't have this.
        * A common name that represents your domain, for example: `www.example.com`
        * Your email address.

You don't need to provide any of the other values, they are all optional.

  2. Determine which certificate authority works for you and then purchase a certificate. For example, you can use: [SSLMate](https://www.sslmate.com), [Thawte](https://www.thawte.com), [Comodo](https://www.comodo.com), or any other certificate authority.

For details about the types of supported certificates, see SSL certificate types.

  3. When your CA requests the contents of your CSR file, follow their instructions for copying and pasting contents from your `.csr` file that you generated earlier, for example `server.csr`.

  4. Follow the prompts when your CA requests domain owner approval.

**Tip:** You might find it easiest to use the email approval method. You will need to configure an email address in your domain account, for example `admin@example.com`, so that you can receive and respond to the CA's approval request.**Note:** After you submit the request for your certificate, it can take a few days before you receive the actual certificate from your CA.
  5. After you provide domain owner approval, the CA sends the certificate to you, which is typically a zip file. Unzip that file to a working directory to concatenate those certificates for upload to App Engine.




### Convert private keys and concatenating SSL certificates

You must convert your private key into an RSA private key and concatenate all of your SSL certificates, before uploading your private key and SSL certificates to App Engine.

  1. Convert the private key file that you generated earlier, into an unencrypted RSA private key. For example, you can run the following `openssl rsa` command:
         
         openssl rsa -in [MY_PRIVATE_KEY].key -out [MY_RSA_KEY].key.pem
         

where:

     * `[MY_PRIVATE_KEY].key` is the generated file that contains your private key is stored. Example: `myserver.key`
     * `[MY_RSA_KEY].key` is the generated file that contains unencrypted RSA private key. Example: `myserver.key.pem`

Example:
           
           openssl rsa -in myserver.key -out myserver.key.pem
           

  2. Concatenate all of the `.crt` files from your CA into one file, using the following command:
         
         cat [MY_DOMAIN_CERT].crt [MY_SecureServerCA].crt [MY_TrustCA].crt [MY_TrustExternalCARoot].crt > [MY_CONCAT_CERT].crt
         

where

     * `[MY_DOMAIN_CERT].crt` is the certificate for your domain. Example: `www_example_com.crt`
     * `[MY_SecureServerCA].crt`, `[MY_TrustCA].crt`, and `[MY_TrustExternalCARoot].crt` are the other certificate files that are provided by your CA.
     * `[MY_CONCAT_CERT].crt` is the concatenated file that contains all of your `.crt` certificate files from your CA. Example: `concat.crt`

Example:
           
           cat www_example_com.crt AddTrustExternalCARoot.crt RSADomainValidationSecureServerCA.crt RSAAddTrustCA.crt > concat.crt
           

  3. Verify your SSL certificate and private key:

     1. To verify that the private key and certificate [match](http://httpd.apache.org/docs/2.0/ssl/ssl_faq.html#verify), you can use the `openssl x509` and `openssl rsa` commands. Examples:
            
            openssl x509 -noout -modulus -in concat.crt | openssl md5
            openssl rsa -noout -modulus -in myserver.key.pem | openssl md5
            

Both the [openssl x509](https://www.openssl.org/docs/manmaster/man1/x509.html) and [openssl rsa](https://www.openssl.org/docs/manmaster/man1/rsa.html) commands should return the same output.

     2. To verify that a certificate and its CA chain are valid, you can use the [openssl verify](https://www.openssl.org/docs/manmaster/man1/verify.html) command. For example:
            
            openssl verify -verbose -CAfile concat.crt concat.crt
            

  4. When you are ready, you can upload your RSA private key and concatenated certificates to App Engine.




### SSL certificate types

App Engine supports the following certificate types:

  * Single Domain/Hostname
  * Self-signed
  * Wildcard
  * Subject Alternative Name (SAN) / Multi Domain



It requires some things of your certificates and keys:

  * Private Key and Certificate should be uploaded in PEM format.
  * Private Keys must not be encrypted.
  * A certificate file can contain at most five certificates; this number includes chained and intermediate certificates.
  * All subject names on the host certificate should match or be subdomains of the user's verified domains.
  * Private keys must use RSA encryption.
  * Maximum allowed key modulus: 2048 bits



If the host certificate requires an intermediate or chained certificate, as many Certificate Authorities (CAs) issue, you must append the intermediate or chained certificates to the end of the public certificate file.

Some App Engine features use [special subdomains](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed). For example, an application can use subdomains to address application services, or to address different versions of your application. To use these with SSL, it makes sense to set up a SAN or wildcard certificate. Wildcard certificates only support one level of subdomain.

### Remove custom SSL certificates

To stop using a custom SSL certificate, perform the following steps:

  1. In the Google Cloud console, go to the App Engine **SSL certificates** settings page.

[Go to SSL certificate settings](https://console.cloud.google.com/appengine/settings/certificates)

  2. Click the certificate that you want to remove from your domain.

  3. Unselect the domain name that you no longer want to use the SSL certificate for, then click **Save**.




## Use Strict-Transport-Security headers

For security reasons, all applications should encourage clients to use `https` connections. To instruct the browser to prefer `https` over `http`, [use the `Strict-Transport-Security` header](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#http_strict_transport_security).

## What's next

  * To upgrade existing apps to only allow secure traffic for TLS versions 1.2 and later, see [Secure your app with minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

  * If you want Cloud Load Balancing to manage incoming requests to your custom domain, see [Migrate App Engine custom domain to Cloud Load Balancing](https://docs.cloud.google.com/appengine/docs/standard/custom-domain-to-cloud-load-balancing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
