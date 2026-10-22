---
url: https://docs.cloud.google.com/certificate-manager/docs/troubleshooting/
title: Troubleshooting Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:37.702243+00:00
---

# Troubleshooting Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Troubleshooting Certificate Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the most common errors you might encounter when using Certificate Manager. It also provides steps to diagnose and resolve those errors.

## Problems related to TLS (SSL) certificates

For help with resolving issues related to TLS (SSL) certificates, see [Troubleshoot SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting).

## Errors related to Certificate Manager certificates

This section provides troubleshooting information for errors related to the `authorizationAttemptInfo` field of Google-managed Certificate Manager certificates. The errors are displayed in the `managed.authorizationAttemptInfo.troubleshooting` section only when the following fields have these values:

  * `managed.authorizationAttemptInfo.state = FAILED`
  * `managed.authorizationAttemptInfo.failureReason = CONFIG`

**Note:** The `managed.authorizationAttemptInfo.attemptTime` field provides the time when the latest authorization attempt was started.

For more information about the errors and how to resolve them, see the following table:

Error | Description  
---|---  
`CNAME_MISMATCH` | This error occurs only for [DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#cname-record) when the value of the expected `CNAME` record doesn't match the value of the resolved `CNAME` record.  To fix this issue, add the expected CNAME record to your DNS configuration. For more information, see the [Add the CNAME record to your DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#cname-record) section.  
`RESOLVED_TO_NOT_SERVING` | This error occurs when the domain contains DNS `A` and `AAAA` records that point to certain IP addresses where the certificate isn't attached to any load balancer.  The error applies only to certificates with load balancer authorizations. You can provision certificates by using [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) only after you configure the load balancer. To resolve this issue, [update the domain's DNS A and AAAA records to point to your load balancer's IP address](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns). The IP addresses that are resolved from the domain's DNS `A` and `AAAA` records are stored in the `ips.resolved` parameter, and the load balancer's IP addresses where this certificate is attached are stored in the `ips.serving` parameter. The domain's DNS `A` and `AAAA` records must point only to the load balancer's IP address. For example, if a DNS `A` record points to the load balancer's IP address but the DNS `AAAA` record points to a different IP address, then the `RESOLVED_TO_NOT_SERVING` error occurs. You must also ensure that the domain's DNS `A` and `AAAA` records resolve correctly and consistently around the world. For more information, see the [Multi-perspective domain validation failures](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting#multi-perspective-domain-validation) section.  
`NO_RESOLVED_IPS` | This error occurs when the domain doesn't contain any DNS `A` and `AAAA` records.  The error applies only to certificates with load balancer authorizations. You can provision certificates by using [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) only after you configure the load balancer. To resolve this issue, add DNS `A` and `AAAA` records for this domain and make sure that the records point to the IP address of the target HTTPS proxy or Media CDN edge cache service. You must also ensure that the domain's DNS `A` and `AAAA` records resolve correctly and consistently around the world. For more information, see the [Multi-perspective domain validation failures](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting#multi-perspective-domain-validation) section.  
`RESOLVED_TO_SERVING_ON_ALT_PORTS` | This error occurs when the domain that contains DNS `A` and `AAAA` records points to a load balancer's IP addresses where this certificate is attached, but port `443` isn't open on those IP addresses.  The error applies only to certificates with load balancer authorizations. You can provision certificates by using [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) only after you configure the load balancer. To resolve this issue, make sure that the load balancer with the attached certificate is listening on port `443`. The `ips.serving_on_alt_ports` parameter stores the list of load balancer IP addresses for which port `443` isn't open. You must also ensure that the domain's DNS `A` and `AAAA` records resolve correctly and consistently around the world. For more information, see the [Multi-perspective domain validation failures](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting#multi-perspective-domain-validation) section.  
`CERTIFICATE_NOT_ATTACHED` | This error occurs when the certificate isn't attached to a load balancer. To resolve this issue, make sure that the certificate is attached to a load balancer. For more information, see the [Deploy the certificate to a load balancer](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth#deploy_the_certificate_to_a_load_balancer) section.  This error also occurs when a certificate is part of a certificate map that's attached to a target HTTPS proxy, but the proxy isn't attached to a forwarding rule. To resolve this issue, attach the target HTTPS proxy to the appropriate forwarding rule. For more information, see [Target proxies overview](https://docs.cloud.google.com/load-balancing/docs/target-proxies) and [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). The error applies only to certificates with load balancer authorizations. You can provision certificates by using [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) only after you configure the load balancer.  
  
## Error when detaching a certificate map from a target proxy

When [detaching a certificate map from a target proxy](https://docs.cloud.google.com/certificate-manager/docs/maps#detach-proxy), you receive the following error:

`"There must be at least one certificate configured for a target proxy."`

This error occurs when there are no certificates assigned to the target proxy aside from those specified in the certificate map that you are trying to detach. To detach the map, first assign one or more certificates directly to the proxy.

## Error when associating a certificate map entry with a certificate

When associating a certificate map entry with a certificate, you receive the following error:

`"certificate can't be used more than 100 times"`

This error occurs when you try to associate a certificate map entry with a certificate that is already associated with 100 certificate map entries. To resolve the issue, do the following:

  * For Google-managed certificates, create another certificate. Associate the new certificate map entries with this new certificate, and attach the new certificate to the load balancer.
  * For self-managed certificates, upload the certificate again with a new name. Associate the new certificate map entries with this new certificate, and attach the new certificate to the load balancer.



## Problems related to certificates issued by a CA Service instance

This section lists the most common errors you might encounter when using Certificate Manager to deploy Google-managed certificates issued by your CA Service instance and their possible causes.

If you receive the `Failed to create Certificate Issuance Config resources` error, check the following:

  * **The lifetime**. Valid certificate lifetime values are from 21 to 30 days.
  * **The rotation window percentage**. Valid rotation window percentages are from 1 to 99 percent. You must set the rotation window percentage in relation to the certificate lifetime so that certificate renewal occurs at least 7 days after the certificate has been issued and at least 7 days before it expires.
  * **The key algorithm**. Valid key algorithm values are: `RSA_2048` and `ECDSA_P256`.
  * **The CA pool**. The CA pool either doesn't exist or is misconfigured. The CA pool must contain at least one enabled CA and the caller must have the `privateca.capools.use` permission on the target Google Cloud project. For regional certificates, the certificate issuance configuration resource must be created in the same location as the CA pool.



If you receive a `Failed to create a managed certificate` error, check the following:

  * The certificate issuance configuration resource you specified when creating the certificate exists.
  * The caller has the `certificatemanager.certissuanceconfigs.use` permission on the certificate issuance Configuration resource you specified when creating the certificate.
  * The certificate is in the same location as the certificate issuance configuration resource.



If you receive a `Failed to renew certificate` or a `Failed to provision certificate` error, check the following:

  * The Certificate Manager service account has the `roles/privateca.certificateRequester` permission on the CA pool specified in the certificate issuance configuration resource used for this certificate.

Use the following command to check permissions on the target CA pool:
        
        gcloud privateca pools get-iam-policy CA_POOL
        --location REGION
        

Replace the following:

    * `CA_POOL`: the full resource path and name of the target CA pool
    * `REGION`: the target Google Cloud region
  * A [certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy) is in effect. For more information, see Problems related to issuance policy restrictions.




## Problems related to issuance policy restrictions

If Certificate Manager doesn't support the changes to a certificate made by the certificate issuance policy, certificate provisioning fails and the state of the managed certificate changes to `Failed`. To resolve the issue, confirm the following:

  * The [identity constraints](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy) of the certificate allow for subject and subject alternative name (SAN) passthrough.
  * The [maximum lifetime](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy) constraint of the certificate is greater than the lifetime of the certificate issuance configuration resource.
  * The certificate issuance policy is configured to allow [end-entity (leaf) server TLS certificates](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile#end-server-tls).



For the previous issues, because CA Service already issued the certificate, you're billed according to [CA Service pricing](https://cloud.google.com/certificate-authority-service/pricing).

If you receive the error `Rejected for issuing certificates from the configured CA Pool`, it indicates that the certificate issuance policy has blocked the requested certificate. To resolve the error, check the following:

  * The issuance mode of the certificate allows certificate signing requests (CSRs).
  * The [allowed key types](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy) are compatible with the [key algorithm](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateIssuanceConfigs#keyalgorithm) of the certificate issuance configuration resource being used.



For the previous issues, because CA Service hasn't issued the certificate, you're not billed by CA Service.

## Problems related to IAP hostname matching

If you unexpectedly get the error, `The host name provided does not match the SSL certificate on the server`, when using Certificate Manager with Identity-Aware Proxy (IAP), check that you are using a certificate that is valid for that hostname. Also [list certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries#list_certificate_map_entries) that you have configured on your certificate map. Every hostname or wildcard hostname that you intend to use with IAP must have a dedicated entry. If the certificate map entry for your hostname is missing, [create a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create).

Requests that fall back onto the primary certificate map entry during [certificate selection](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic#selection-logic) are always rejected by IAP.

## Multi-perspective domain validation failures

Google Cloud periodically renews your Google-managed certificates by requesting them from certificate authorities (CAs). The CAs that Google Cloud works with to renew your certificates use a multi-perspective domain validation method known as [Multi-Perspective Issuance Corroboration (MPIC)](https://freedom-to-tinker.com/2024/02/13/announcing-the-open-multi-perspective-issuance-corroboration-project/). As part of this process, the certificate authorities verify domain control by checking the domain's DNS settings, and in the case of [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/core-components#domain-auth), by attempting to contact the server behind the domain's IP address. These verifications are conducted from multiple vantage points across the internet. If the validation process fails, Google-managed certificates fail to renew. As a result, your load balancer serves an expired certificate to clients, causing browser users to encounter certificate errors and API clients to experience connection failures.

To prevent multi-perspective domain validation failures for misconfigured DNS records, note the following:

  * Your DNS A records (IPv4) and DNS AAAA (IPv6) records for your domains and any subdomains point _only_ to the IP address (or addresses) associated with the load balancer's forwarding rule (or rules). The existence of any other addresses in the record can cause validation to fail.
  * The CA, which performs validation of DNS records, queries DNS records from multiple locations. Ensure that your DNS provider responds consistently to all the global domain validation requests.
  * Using GeoDNS (returning different IP addresses based on the request location) or location-based DNS policies can lead to inconsistent responses and cause validation to fail. If your DNS provider uses GeoDNS, disable it, or ensure that all regions return the same load balancer's IP address.
  * If you are using the [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) method to provision Google-managed certificates, you must explicitly specify the IP addresses of your load balancer in your DNS configuration. Intermediate layers, such as a CDN, can cause unpredictable behavior. The IP address needs to be directly accessible without any redirects, firewalls, or CDNs in the request path. To learn more, see the Load balancers behind a CDN section in this document.
  * We recommended that you use a DNS global propagation checker of your choice to verify that all the relevant DNS records resolve correctly and consistently across the globe.



#### Verify configuration changes

After you have configured your DNS records, you can verify that they are correct by creating a new certificate and connecting it to your load balancer along with the existing certificate. This step forces an immediate certificate provisioning check with the CA, letting you verify your configuration changes within minutes. Without this, automatic renewals of the existing certificate can take days or weeks, leaving uncertainty about your setup.

If the [certificate status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status) becomes `ACTIVE`, it indicates that the certificate has been issued, thereby confirming that your DNS configuration is correct. At this point, we recommend that you remove the earlier certificate to avoid having two separate certificates for the same domain. This process doesn't interrupt traffic to your load balancer.

The new certificate serves as a validation tool—its creation confirms that multi-perspective domain validation using MPIC works correctly for your setup.

#### Load balancers behind a CDN

For load balancers that have CDN enabled, some third-party CDN providers in the request path might prevent validation requests from succeeding. This can happen if the CDN provider is actively proxying HTTP(S) traffic.

In such cases, we recommend using the [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth) method to provision Google-managed certificates. The latter approach doesn't require the CA to contact your load balancer.

## What's next

  * [Certificate Manager release notes](https://docs.cloud.google.com/certificate-manager/docs/release-notes)
  * [Certificate Manager support ](https://docs.cloud.google.com/certificate-manager/docs/support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
