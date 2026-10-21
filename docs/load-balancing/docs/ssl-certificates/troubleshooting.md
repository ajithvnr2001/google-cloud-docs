---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting/
title: Troubleshoot SSL certificates \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:35.716972+00:00
---

# Troubleshoot SSL certificates  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Troubleshoot SSL certificates Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to diagnose and resolve common problems with Google-managed and self-managed [SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates). Valid SSL certificates protect data in transit and help ensure service availability for your load-balancing deployments.

## Troubleshoot Google-managed certificates

For Google-managed certificates, there are two types of status:

  * Managed status
  * Domain status



### Managed status

To check the certificate status, run the following command:
    
    
    gcloud compute ssl-certificates describe CERTIFICATE_NAME \
        --global \
        --format="get(name,managed.status)"
    

Values for _managed status_ are as follows:

Managed status | Explanation  
---|---  
`PROVISIONING` |  The Google-managed certificate has been created and Google Cloud is working with the Certificate Authority to sign it.  Provisioning a Google-managed certificate might take up to _60 minutes_ from the moment your DNS and load balancer configuration changes have propagated across the internet. If you have updated your DNS configuration recently, it can take a significant amount of time for the changes to _fully propagate_. Sometimes propagation takes up to 72 hours worldwide, although it typically takes a few hours. For more information on DNS propagation, see [Propagation of changes](https://docs.cloud.google.com/dns/docs/overview#propagation_of_changes).  If the certificate remains in the `PROVISIONING` state, make sure that the correct certificate is associated with the target proxy. You can check this by running either the [`gcloud compute target-https-proxies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/describe) or the [`gcloud compute target-ssl-proxies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/describe) command.  
`ACTIVE` | The Google-managed SSL certificate is obtained from the Certificate Authority. It might take an _additional_ 30 minutes to be available for use by a load balancer.   
`PROVISIONING_FAILED` | You might briefly see `PROVISIONING_FAILED` even when your certificate is actually `ACTIVE`. Recheck the status.   
  
If the status remains `PROVISIONING_FAILED`, the Google-managed certificate has been created, but the Certificate Authority can't sign it. Ensure that you completed all steps in [Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).   
  
Google Cloud retries provisioning until successful or the status changes to `PROVISIONING_FAILED_PERMANENTLY`.   
`PROVISIONING_FAILED_PERMANENTLY` | The Google-managed certificate is created, but the Certificate Authority can't sign it because of a DNS or load balancer configuration issue. In this state, Google Cloud doesn't retry provisioning.  
  
[ Create a replacement Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#replace-ssl), and make sure that the replacement is associated with your load balancer's target proxy. Verify or complete all steps in [ Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs). Afterwards, you can [ delete the certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#delete-ssl) that permanently failed provisioning.   
`RENEWAL_FAILED` | The Google-managed certificate renewal failed because of an issue with the load balancer or DNS configuration. If any of the domains or subdomains in a managed certificate aren't pointing to the load balancer's IP address by using an A/AAAA record, the renewal process fails. The existing certificate continues to serve, but expires shortly. Check your configuration. If the status remains `RENEWAL_FAILED`, [ provision a new certificate, switch to using the new certificate, and delete the previous certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#replace-ssl). For more information about certificate renewal, see [ Google-managed SSL certificate renewal](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#renewal).  
  
### Domain status

To check the domain status, run the following command:
    
    
    gcloud compute ssl-certificates describe CERTIFICATE_NAME \
        --global \
        --format="get(managed.domainStatus)"
    

Values for _domain status_ are described in this table.

Domain status | Explanation  
---|---  
`PROVISIONING` | The Google-managed certificate is created for the domain. Google Cloud is working with the Certificate Authority to sign the certificate.   
`ACTIVE` |  The domain has been successfully validated for provisioning the certificate. If the SSL certificate is for _multiple domains_ , the certificate can only be provisioned once all the domains have an `ACTIVE` status and the [managed status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status) of the certificate is `ACTIVE` as well.   
`FAILED_NOT_VISIBLE` | Certificate provisioning hasn't completed for the domain. Any of the following might be the issue:

  * The domain's DNS record doesn't resolve to the IP address of the Google Cloud load balancer. To resolve this issue, [update the DNS A and AAAA records](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns) to point to your load balancer's IP address. DNS must _not_ resolve to any other IP address than the load balancer's. For example, if an A record resolves to the correct load balancer, but the AAAA resolves to something else, the domain status is `FAILED_NOT_VISIBLE`.
  * Newly updated DNS A and AAAA records can take a significant amount of time to be fully propagated. Sometimes propagation across the internet takes up to 72 hours worldwide, although it typically takes a few hours. The domain status continues to be `FAILED_NOT_VISIBLE` until propagation is complete.
  * The SSL certificate isn't [ attached to the load balancer's target proxy](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#verify-target-proxy). To resolve this issue, [ update your load balancer configuration.](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#load-balancer)
  * The frontend ports for the forwarding rule don't include port 443 for Application Load Balancers (Global or Classic) or External proxy Network Load Balancers. This can be resolved by adding a new forwarding rule with port 443.
  * A Certificate Manager certificate map is attached to the target proxy. The attached certificate map gets precedence and directly attached certificates are ignored. This can be resolved by [detaching the certificate map from the proxy](https://docs.cloud.google.com/certificate-manager/docs/maps#detach-proxy).
If the managed status is `PROVISIONING`, Google Cloud continues to retry provisioning, even if the domain status is `FAILED_NOT_VISIBLE`. 
  
`FAILED_CAA_CHECKING` | Certificate provisioning failed because of a configuration issue with your domain's CAA record. Ensure that you have [ followed the correct procedure](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa).   
`FAILED_CAA_FORBIDDEN` | Certificate provisioning failed because your domain's CAA record doesn't specify a CA that Google Cloud needs to use. Ensure that you have [followed the correct procedure](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa).   
`FAILED_RATE_LIMITED` | Certificate provisioning failed because a Certificate Authority has rate-limited certificate signing requests. You can [ provision a new certificate, switch to using the new certificate, and delete the previous certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#replace-ssl), or you can contact Google Cloud Support.   
**Important:** For Google-managed certificates, the provisioning process might get delayed if multiple certificates with overlapping domains are requested in a short span of time. Certificate requests with overlapping sets of domains aren't processed in parallel.   
Google Cloud only issues one managed certificate per domain at a time. Attempts for certificates with incorrectly configured domains time out after 30 minutes, whereas certificates with correctly set domains typically get issued in much less time.

### Managed certificate renewal

To help ensure that your certificates don't fail the domain validation step of the renewal process, review the [requirements for your DNS A and AAAA records](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns).

### Multi-perspective domain validation

Google Cloud periodically renews your Google-managed certificates by requesting them from certificate authorities (CAs). The CAs that Google Cloud works with to renew your certificates use a multi-perspective domain validation method known as [Multi-Perspective Issuance Corroboration (MPIC)](https://freedom-to-tinker.com/2024/02/13/announcing-the-open-multi-perspective-issuance-corroboration-project/). As part of this process, the certificate authorities verify domain control by checking the domain's DNS settings and attempting to contact the server behind the domain's IP address. These verifications are conducted from multiple vantage points across the internet. If the validation process fails, Google-managed certificates fail to renew. As a result, your load balancer serves an expired certificate to clients, causing browser users to encounter certificate errors and API clients to experience connection failures.

To prevent multi-perspective domain validation failures for misconfigured DNS records, note the following:

  * Your DNS A records (IPv4) and DNS AAAA (IPv6) records for your domains and any subdomains point _only_ to the IP address (or addresses) associated with the load balancer's forwarding rule (or rules). The existence of any other addresses in the record can cause validation to fail.
  * The CA, which performs validation of DNS records, queries DNS records from multiple locations. Ensure that your DNS provider responds consistently to all the global domain validation requests.
  * Using GeoDNS (returning different IP addresses based on the request location) or location-based DNS policies can lead to inconsistent responses and cause validation to fail. If your DNS provider uses GeoDNS, disable it, or ensure that all regions return the same load balancer's IP address.
  * You must explicitly specify the IP addresses of your load balancer in your DNS configuration. Intermediate layers, such as a CDN, can cause unpredictable behavior. The IP address needs to be directly accessible without any redirects, firewalls, or CDNs in the request path. To learn more, see the Load balancers behind a CDN section in this document.
  * We recommended that you use a DNS global propagation checker of your choice to verify that all the relevant DNS records resolve correctly and consistently across the globe.



#### Verify configuration changes

After you have configured your DNS records, you can verify that they are correct by creating a new certificate and connecting it to your load balancer along with the existing certificate. This step forces an immediate certificate provisioning check with the CA, letting you verify your configuration changes within minutes. Without this, automatic renewals of the existing certificate can take days or weeks, leaving uncertainty about your setup.

If the [certificate status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status) becomes `ACTIVE`, it indicates that the certificate has been issued, thereby confirming that your DNS configuration is correct. At this point, we recommend that you remove the earlier certificate to avoid having two separate certificates for the same domain. This process doesn't interrupt traffic to your load balancer.

The new certificate serves as a validation tool—its creation confirms that multi-perspective domain validation using MPIC works correctly for your setup.

#### Load balancers behind a CDN

For load balancers that have CDN enabled, some third-party CDN providers in the request path might prevent validation requests from succeeding. This can happen if the CDN provider is actively proxying HTTP(S) traffic.

In such cases, we recommend [migrating your certificates to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/migrate-lb#create_a_dns_authorization) and using the [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth) method to provision Google-managed certificates. The latter approach doesn't require the CA to contact your load balancer.

## Troubleshoot self-managed SSL certificates

This guide describes how to troubleshoot configuration issues for self-managed SSL certificates.

### Certificate cannot be parsed

Google Cloud requires certificates in [PEM format](http://ospkibook.sourceforge.net/docs/OSPKI-2.4.7/OSPKI-html/sample-ca-cert.htm). If the certificate is PEM formatted, check the following:

You can validate your certificate using the following OpenSSL command, replacing `CERTIFICATE_FILE` with the path to your certificate file:
    
    
    openssl x509 -in CERTIFICATE_FILE -text -noout
    

If OpenSSL is unable to parse your certificate:

  * Contact your CA for help.
  * [Create a new private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).



### Missing common name or subject alternative name

Google Cloud requires that your certificate have _either_ a common name (`CN`) or subject alternative name (`SAN`) attribute. See [Create a CSR](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-csr) for additional information.

When both attributes are absent, Google Cloud displays an error message like the following when you try to [create a self-managed certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#createresource):
    
    
    ERROR: (gcloud.compute.ssl-certificates.create) Could not fetch resource:
     -   The SSL certificate is missing a Common Name(CN) or Subject Alternative
       Name(SAN).
    

### Private key cannot be parsed

Google Cloud requires PEM-formatted private keys that meet the [private key criteria](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#private-key).

You can validate your private key using the following OpenSSL command, replacing `PRIVATE_KEY_FILE` with the path to your private key:
    
    
        openssl rsa -in PRIVATE_KEY_FILE -check
    

The following responses indicate a problem with your private key:

  * `unable to load Private Key`
  * `Expecting: ANY PRIVATE KEY`
  * `RSA key error: n does not equal p q`
  * `RSA key error: d e not congruent to 1`
  * `RSA key error: dmp1 not congruent to d`
  * `RSA key error: dmq1 not congruent to d`
  * `RSA key error: iqmp not inverse of q`



To fix the problem, you must [create a new private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

### Private keys with passphrases

If OpenSSL prompts for a passphrase, you'll need to remove the passphrase from your private key before you can use it with Google Cloud. You can use the following OpenSSL command:
    
    
    openssl rsa -in PRIVATE_KEY_FILE \
        -out REPLACEMENT_PRIVATE_KEY_FILE
    

Replace the placeholders with valid values:

  * `PRIVATE_KEY_FILE`: The path to your private key that's protected with a passphrase
  * `REPLACEMENT_PRIVATE_KEY_FILE`: The path where you'd like to save a copy of your plain text private key



### Expiring intermediate certificates

If an intermediate certificate expires before the server (leaf) certificate, this might indicate that your CA isn't following best practices.

When an intermediate certificate expires, your leaf certificate used in Google Cloud might become invalid. This depends on the SSL client, as follows:

  * Some SSL clients only look at the expire time of the leaf certificate and ignore expired intermediate certificates.
  * Some SSL clients treat a chain with any expired intermediate certificate(s) as invalid and display a warning.



To resolve this issue:

  1. Wait for the CA to switch to a new intermediate certificate.
  2. Request a new certificate from them.
  3. Re-upload the new certificate with the new keys.



Your CA might also allow cross-signing for intermediate certificates. Check with your CA to confirm.

### RSA public exponent is too large

The following error message appears when the RSA public exponent is larger than 65537\. Make sure to use `65537`, as specified in [RFC 4871](https://www.ietf.org/rfc/rfc4871.txt).
    
    
    ERROR: (gcloud.compute.ssl-certificates.create) Could not fetch resource:
     -   The RSA public exponent is too large.
    

### Remove SSL certificate from target-proxy

The following steps demonstrate how to remove a single SSL certificate attached to the target https proxy:

  1. Export the target-https-proxy to a temporary file.
         
         gcloud compute target-https-proxies export TARGET_PROXY_NAME > /tmp/proxy
         

  2. Edit `/tmp/proxy` file and remove the following lines:
         
         sslCertificates:
         -   https://www.googleapis.com/compute/v1/projects/...
         

  3. Import the `/tmp/proxy` file.
         
         gcloud compute target-https-proxies import TARGET_PROXY_NAME \
            --source=/tmp/proxy
         

  4. Optional: Delete the SSL certificate.
         
         gcloud compute ssl-certificates delete SSL_CERT_NAME
         




Replace the following:

  * `TARGET_PROXY_NAME`: the name of the target https proxy resource.
  * `SSL_CERT_NAME`: the name of the SSL certificate.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
