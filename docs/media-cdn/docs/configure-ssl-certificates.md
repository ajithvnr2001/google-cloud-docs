---
url: https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates/
title: Configure SSL (TLS) certificates \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:48:19.354043+00:00
---

# Configure SSL (TLS) certificates  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configure SSL (TLS) certificates Stay organized with collections  Save and categorize content based on your preferences. 

After you have [created a Media CDN service](https://docs.cloud.google.com/media-cdn/docs/configuration) (or services), you can issue and attach SSL (TLS) certificates to support secure connectivity in browsers and mobile applications.

## Issue a managed certificate

To create a managed certificate and attach it to your Media CDN service, you must do the following:

  1. Demonstrate ownership ("authorization") of the domains that you want to issue certificates for by creating a challenge token and adding a DNS record.
  2. Create a certificate of type `EDGE_CACHE` with one or more domain names based on that authorization.
  3. Attach that certificate to one or more Edge Cache services.



You must have the following Identity and Access Management permissions to authorize, create, and attach certificates to an Edge Cache service:

  * `certificatemanager.certs.create`
  * `certificatemanager.certs.get`
  * `certificatemanager.certs.list`
  * `certificatemanager.certs.use`
  * `certificatemanager.dnsauthorizations.create`
  * `certificatemanager.dnsauthorizations.get`
  * `certificatemanager.dnsauthorizations.list`
  * `certificatemanager.dnsauthorizations.use`



Users who need to attach an _existing_ certificate to an Media CDN service require the `certificatemanager.certs.get`, `certificatemanager.certs.list`, and `certificatemanager.certs.use` IAM permissions.

### Before you begin

  * You must have a registered domain name that you can update public DNS records on.
  * Read the [SSL certificates overview](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates).



### Create a DNS authorization

First, you must create a DNS authorization to demonstrate ownership of the domain before you can issue certificates for it. The DNS authorization uses the [DNS-01 ACME](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) challenge, and lets you issue a certificate before directing user-facing traffic to your Edge Cache service.

Set the value of `domain` to the domain name you intend to create a certificate for, as follows:

**Note:** The Google Cloud CLI support for Certificate Manager requires gcloud CLI version 392.0.0 (version 327.0.0 for `gcloud beta` support) or later. Use `gcloud version` and `gcloud components update` to check the version and update your installed Google Cloud CLI.

###  gcloud 

Use the `gcloud certificate-manager dns-authorizations` command:
    
    
    gcloud certificate-manager dns-authorizations create DOMAIN_NAME_AUTH \
        --domain="DOMAIN_NAME"
    gcloud certificate-manager dns-authorizations describe DOMAIN_NAME_AUTH
    

The gcloud CLI returns a response with the details of the DNS record that you need to add.
    
    
    createTime: '2022-01-14T13:35:00.258409106Z'
    dnsResourceRecord:
      data: 0e40fc77-a37d-4eb8-8fe1-eea2e18d12d9.4.authorize.certificatemanager.goog.
      name: _acme-challenge.example.com.
      type: CNAME
    domain: example.com
    name: projects/myProject/locations/global/dnsAuthorizations/myAuthorization
    updateTime: '2022-01-14T13:35:01.571086137Z'
    

###  Terraform 
    
    
    resource "google_certificate_manager_dns_authorization" "default" {
      name        = "example-dns-auth"
      description = "example dns authorization "
      domain      = "test.example.com"
    }

**Key Point:** The record must be added at the authoritative DNS provider for your domain. Certificate Manager regularly polls the domain for the record and updates the status of the authorization after the (valid) record is found.

If you are using Cloud DNS for your domain, see [the steps for adding a new record](https://docs.cloud.google.com/dns/docs/records#console) to your hosted domain. If you are using another DNS provider, consult their documentation for adding a CNAME record.

  * You can repeat this step for each domain you need to issue a certificate for.
  * Certificates can contain multiple domains, or you can choose to issue a certificate per domain, as needed. After you have an authorization for a domain, you can use it to issue certificates.
  * We recommend creating fewer total certificates, each with all of the domain names used for your service. This improves client performance when using multiple domains because clients can benefit from TLS resumption more often.
  * Each Edge Cache service can reference up to five certificates. By issuing fewer certificates, you can stay within this limit.

**Note:** Ensure that the DNS record used for domain control validation (DCV) is not deleted, even after the certificate is issued. Certificate Manager requires this record to renew certificates. If you delete this record, Certificate Manager can't renew your certificates, which can result in downtime for your service.

If you need to retrieve the DNS record values at a later date, make a request for the `authorizationName` that you provided when creating the DNS authorization:

### Create a certificate

After you have added the DNS record demonstrating ownership of the domain(s) you want to create a certificate for, you can issue a certificate creation request.

The list of `dnsAuthorizations` must match the names of existing authorizations you created earlier in the process. If you want to add multiple domains to the same certificate, provide a list of `domains[]` and matching `dnsAuthorizations[]` when making the request.

To create a certificate using an authorization for `test.example.com` called `test-example-com`:

###  gcloud 

Use the `gcloud certificate-manager certificates` command:
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --domains="DOMAIN_NAME" \
        --dns-authorizations="DOMAIN_NAME_AUTH" \
        --scope=EDGE_CACHE
    

This creates a certificate with each DNS authorization in the`AUTHORIZING` state and the certificate in the `PROVISIONING` state:
    
    
    Create request issued for: [DOMAIN_NAME]
    Waiting for operation [projects/my-project/locations/global/operations/operatio
    n-1613425627385-5bb66ed644e91-3e2a2f1f-71979cf8] to complete...done.
    Created certificate [CERTIFICATE_NAME].
    

###  Terraform 
    
    
    resource "google_certificate_manager_certificate" "default" {
      name        = "example-dns-cert"
      description = "example dns certificate"
      scope       = "EDGE_CACHE"
      managed {
        domains = [
          google_certificate_manager_dns_authorization.default.domain,
        ]
        dns_authorizations = [
          google_certificate_manager_dns_authorization.default.id,
        ]
      }
    }

It might take a few minutes (and up to an hour) for the certificate creation to complete, depending on the following:

  * How fast your DNS provider propagates configuration changes.
  * How many domains you are attempting to validate and create certificates for.



The `state` field displays the current status of the certificate:

  * **PROVISIONING** \- the certificate is still being provisioned. This is likely because the certificate creation request was only recently made.
  * **FAILED** \- returned after multiple attempts to validate the domain or issue the certificate. For details, see the `provisioning_issue`, `authorization_attempt_info` and `failure_reason` fields.
  * **ACTIVE** \- the domain was successfully validated and the certificate has been provisioned.



To check the status of the certificate:

###  gcloud 

Use the `gcloud certificate-manager certificates` command:
    
    
    gcloud certificate-manager certificates describe CERTIFICATE_NAME
    

In this example, the DNS authorization is `AUTHORIZED` and the certificate state is `ACTIVE`:
    
    
    createTime: '2021-02-07T20:03:39.867762684Z'
    expireTime: '2021-03-09T19:20:41Z'
    managed:
      authorizationAttemptInfo:
      - domain: DOMAIN_NAME
        state: AUTHORIZED
      dnsAuthorizations:
      - projects/111111111111/locations/global/dnsAuthorizations/test-example-com
      domains:
      - DOMAIN_NAME
      state: ACTIVE
    name: projects/my-project/locations/global/certificates/test-example-com
    scope: EDGE_CACHE
    subjectAlternativeNames:
    - DOMAIN_NAME
    updateTime: '2021-02-07T20:03:40.297242738Z'

After the certificate is `ACTIVE`, you can attach it to an Edge Cache service.

**Note:** All certificates issued by Google Cloud (as well as most other certificate providers) are logged to public [Certificate Transparency](https://www.certificate-transparency.org/) (CT) logs.

### Attach a certificate to a service

After you have created a managed certificate, you can associate it with one or more of your Edge Cache services. Certificates can be attached to both existing and new services by updating the list of `edgeSslCertificates` in the service.

You must have the following IAM permissions to attach certificates to an Edge Cache service:

  * `certificatemanager.certs.get`
  * `certificatemanager.certs.list`
  * `certificatemanager.certs.use`
  * `networkservices.edgeCacheServices.get`
  * `networkservices.edgeCacheServices.list`
  * `networkservices.edgeCacheServices.update`

**Note:** Ensure that you have a `routing.hostRules[].hosts[]` entry that matches at least one of the domains on an attached certificate. Without a hostname to match against, Media CDN returns an HTTP 404 to the client.

To attach a certificate to a service, complete the following steps.

###  gcloud 

Run the `gcloud edge-cache services export` command to export your service's YAML file:
    
    
    gcloud edge-cache services export SERVICE_NAME \
        --destination=my-service.yaml
    

Edit the exported YAML file to add your certificate:
    
    
    name: SERVICE_NAME
    edgeSslCertificates:
    - projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME
    

Run the `gcloud edge-cache services import` command:
    
    
    gcloud edge-cache services import SERVICE_NAME \
        --source=my-service.yaml
    

Output: 
    
    
    Request issued for: [SERVICE_NAME]
    Updated service [SERVICE_NAME]
    

The command returns a description of your service, including the list of `edgeSslCertificates` now attached:
    
    
      name: SERVICE_NAME
      edgeSslCertificates:
      - projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME
    

After you update the configuration, the certificate propagates to all edge locations within minutes. To test that the certificate is associated with your Edge Cache service before making DNS changes, you can issue a request against the IPv4 or IPv6 address associated with your service.

### Replace and remove certificates

Certificates can be added and removed by updating the list of certificates.

When using the gcloud CLI's `--edge-ssl-certificate` flag, certificates are only appended to the list of existing certificates, and not replaced. This prevents you from accidentally removing a valid, active certificate accidentally.

To remove the `test-example-com` certificate from our service in the following example, you can export your service to YAML using the [import and export commands](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export)
    
    
      name: my-service
      edgeSslCertificates:
      - projects/PROJECT_ID/locations/global/certificates/test-example-com
      - projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME

The following commands show how to export the service, remove the certificate reference, and import the updated service.

###  gcloud 

Use the `gcloud edge-cache services` command:
    
    
    gcloud edge-cache services export SERVICE_NAME --destination=my-service.yaml
    
    
    
    Exported [projects/my-project/locations/global/edgeCacheServices/SERVICE_NAME] to 'my-service.yaml'.
    

Remove the certificates you no longer want the service to use by using your preferred text editor:
    
    
      name: SERVICE_NAME
      edgeSslCertificates:
      - projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME
    

Save the modified file, and then import the updated service:

###  gcloud 

Use the `gcloud edge-cache services` command:
    
    
    gcloud edge-cache services import SERVICE_NAME --source=my-service.yaml
    
    
    
    Request issued for: [SERVICE_NAME]
    Updated service [SERVICE_NAME].
    

There is no limit to the number of services a certificate can be associated with, and each Edge Cache service can reference up to five certificates.

## Self-managed certificates

**Note:** We strongly recommend using [managed certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates#certificate-types), to avoid the risk of a certificate accidentally expiring.

You can upload your own certificates to Media CDN if you have specific use-cases that require it.

To upload a certificate and its associated key to Certificate Manager:

###  gcloud 

Use the `gcloud certificate-manager certificates` command. Make sure you specify `--scope=EDGE_CACHE` for certificates associated with Media CDN.
    
    
    gcloud certificate-manager certificates create stream-example-com \
        --certificate-file=CERT.pem \
        --private-key-file=PRIVATE_KEY.pem \
        --scope=EDGE_CACHE
    
    
    
    Create request issued for: [stream-example-com]
    Created certificate [stream-example-com].
    

After the certificate has been uploaded, you can [attach it to an EdgeCacheService](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates#attach-cert) as you would a managed certificate.

## Troubleshoot certificate issuance

See the [troubleshooting guide](https://docs.cloud.google.com/media-cdn/docs/troubleshooting-certificate-issuance) on how to resolve common certificate authorization and issuance errors.

## What's next

  * [Redirect all HTTP requests to HTTPS](https://docs.cloud.google.com/media-cdn/docs/routing#https-redirect) to encrypt communications by default
  * [View request logs](https://docs.cloud.google.com/media-cdn/docs/logging) with Logging
  * [Configure signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) to protect your content
  * [Optimize cache keys and TTLs](https://docs.cloud.google.com/media-cdn/docs/caching) to improve cache hit rates
  * Configure [advanced route matching](https://docs.cloud.google.com/media-cdn/docs/routing) and add additional origins



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
