---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs/
title: Use Google-managed SSL certificates \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:35.612676+00:00
---

# Use Google-managed SSL certificates  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use Google-managed SSL certificates Stay organized with collections  Save and categorize content based on your preferences. 

Use Compute Engine Google-managed SSL certificates to simplify securing your domains by automating the acquisition, management, and renewal of Domain Validation (DV) certificates. These certificates support multiple hostnames and Google Cloud automatically renews the certificate.

Compute Engine Google-managed certificates are supported with the following load balancers:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * External proxy Network Load Balancer (with a target SSL proxy)



Compute Engine Google-managed SSL certificates aren't supported for regional external Application Load Balancers, regional internal Application Load Balancers, or cross-region internal Application Load Balancers. For these load balancers, you can use [Compute Engine self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs). Alternatively, you can use [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy), which supports both self-managed and Google-managed certificates for most load balancers.

You can also use managed SSL certificates with Google Kubernetes Engine. For more information, see [Using Google-managed SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs).

You can create a Google-managed certificate before, during, or after creating your load balancer. This page assumes that you're creating the Compute Engine certificate before or after creating the load balancer, not during. To create the certificate while creating your load balancer, see the load balancer how-to pages.

## Before you begin

  * Make sure that you are familiar with the [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).
  * Make sure that you have the domain names that you want to use for your Google-managed SSL certificate. If you're using Cloud Domains, see [Register a domain](https://docs.cloud.google.com/domains/docs/register-domain).
  * Make sure that you've enabled the Compute Engine API for your project.

[Enable the Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)




## Permissions

To follow this guide, you must be able to create and modify SSL certificates in your project. You can do this if one of the following is true:

  * You are a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`).
  * You have both the [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`compute.securityAdmin`) and the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`compute.networkAdmin`) in the project.
  * You have a custom role for the project that includes the `compute.sslCertificates.*` permissions and one or both of `compute.targetHttpsProxies.*` and `compute.targetSslProxies.*`, depending on the type of load balancer that you are using.



## Step 1. Create a Google-managed SSL certificate

**Note:** For Google-managed certificates for GKE Ingress, see [Using Google-managed SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs).

You can create a Google-managed certificate before, during, or after creating your load balancer. During the process of creating a load balancer in the Google Cloud console, you can use the Google Cloud console to create your certificate. Alternatively, you can create your certificate before or after creating your load balancer. This step shows you how to create a certificate that you can later add to one or more load balancers.

If you have already created your Google-managed SSL certificate, you can skip this step.

###  Console 

You can work with global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page.

**Note:** The following procedure takes you directly to the **Classic Certificates** tab. You can find the **Classic Certificates** tab in the **Certificate Manager** page linked from the top-level [**Security**](https://console.cloud.google.com/security/) page.

  1. Go to the **Classic Certificates** tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. Click **Create SSL certificate**.
  3. Enter a name and an optional description for the certificate.
  4. Select **Create Google-managed certificate**.
  5. Add the domains.
  6. Click **Create**.



###  gcloud 

To create a global Google-managed SSL certificate for a global external Application Load Balancer or external proxy Network Load Balancer, use the [`gcloud compute ssl-certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command:
    
    
    gcloud compute ssl-certificates create CERTIFICATE_NAME \
        --description=DESCRIPTION \
        --domains=DOMAIN_LIST \
        --global
    

Replace the following:

  * `CERTIFICATE_NAME`: a name for the global SSL certificate
  * `DESCRIPTION`: a description for the global SSL certificate
  * `DOMAIN_LIST`: a single domain name or a comma-delimited list of domain names to use for this certificate 



###  Terraform 

To create the Google-managed SSL certificate, use the [`google_compute_managed_ssl_certificate`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_managed_ssl_certificate) resource.
    
    
    resource "google_compute_managed_ssl_certificate" "lb_default" {
      provider = google-beta
      name     = "myservice-ssl-cert"
    
      managed {
        domains = ["example.com"]
      }
    }

###  api 

Create the Google-managed certificate resource [`sslCertificates.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/global/sslCertificates
    {
      "name": "ssl-certificate-name",
      "managed": {
        "domains": [
          "www.example.com"
        ]
      },
      "type": "MANAGED"
    }
    

### Check the status of a Google-managed SSL certificate

###  Console 

You can check the status of your global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page.

  1. Go to the **Classic Certificates** tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. Optional: Filter the list of SSL certificates.
  3. Check the **Status** column.
  4. To view more details, click the certificate name.



###  gcloud 

To determine the status of your Google-managed certificate, you can use `gcloud compute` commands. After running the appropriate command, note the following:

  * The _managed status_.
  * The _domain status_.



To list your Google-managed SSL certificates, use the [`gcloud compute ssl-certificates list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/list) command with the `--global` flag .
    
    
    gcloud compute ssl-certificates list \
       --global
    

You can use the [`gcloud compute ssl-certificates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe) command, replacing `CERTIFICATE_NAME`:
    
    
    gcloud compute ssl-certificates describe CERTIFICATE_NAME \
       --global \
       --format="get(name,managed.status, managed.domainStatus)"
    

At this point, the certificate status and the domain status are `PROVISIONING`. After you complete the steps on this page, the statuses change to `ACTIVE`.

For more information about the statuses, see the [troubleshooting page](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting).

## Step 2: Create or update your load balancer

To become `ACTIVE`, the Google-managed SSL certificate must be associated with a load balancer, specifically the load balancer's target proxy.

After you've created your SSL certificate and it's in the `PROVISIONING` state, you can use it during the creation of your load balancer, as described in the following how-to guides:

  * [Set up a global external Application Load Balancer with a Compute Engine backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Set up a classic Application Load Balancer with a Compute Engine backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)
  * [Set up an external proxy Network Load Balancer with an SSL proxy](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl)



Or you can use it to update an existing load balancer, as described here:

###  Console 

When you update a global external Application Load Balancer or external proxy Network Load Balancer using the Google Cloud console, Google Cloud automatically associates your SSL certificate with the correct target proxy.

  1. Go to the **Load balancing** page in the Google Cloud console.   
[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)
  2. Click the name of your load balancer.
  3. Click **Edit** edit.
  4. Click **Frontend configuration**.
  5. Click the correct front end (must be HTTPS, HTTP/2, SSL).
  6. Click **Additional certificates** , and select your Google-managed certificate from the drop-down list.
  7. Click **Create**.



###  gcloud 

To associate an SSL certificate with the target HTTPS proxy for a global external Application Load Balancer, use the [`gcloud compute target-https-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update) command with the `--global-ssl-certificates` and `--global` flags:
    
    
    gcloud compute target-https-proxies update TARGET_PROXY_NAME \
        --ssl-certificates SSL_CERTIFICATE_LIST \
        --global-ssl-certificates \
        --global
    

To associate an SSL certificate with the target SSL proxy for an external proxy Network Load Balancer, use the [`gcloud compute target-ssl-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update) command:
    
    
    gcloud compute target-ssl-proxies update TARGET_PROXY_NAME \
        --ssl-certificates SSL_CERTIFICATE_LIST
    

Replace the following:

  * `TARGET_PROXY_NAME`: the name of the load balancer's target proxy
  * `SSL_CERTIFICATE_LIST`: a comma-delimited list of SSL certificate resources

Make sure that the list of referenced certificates includes all older valid SSL certificates as well as the new SSL certificate. The `gcloud compute target-ssl-proxies update` command overrides the original values for `--ssl-certificates` with the new value. 




###  Terraform 

To create the target HTTPS proxy, use the [`google_compute_target_https_proxy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy) resource.

To create the target SSL proxy, use the [`google_compute_target_ssl_proxy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_ssl_proxy) resource.
    
    
    resource "google_compute_target_https_proxy" "lb_default" {
      provider = google-beta
      name     = "myservice-https-proxy"
      url_map  = google_compute_url_map.lb_default.id
      ssl_certificates = [
        google_compute_managed_ssl_certificate.lb_default.name
      ]
      depends_on = [
        google_compute_managed_ssl_certificate.lb_default
      ]
    }

Each target HTTPS proxy or target SSL proxy must reference at least one SSL certificate. A target proxy can reference more than one SSL certificate. For details, see [Target pools and target proxies](https://docs.cloud.google.com/load-balancing/docs/quotas#target_pools_and_target_proxies) in the load balancing resource quotas and limits.

**Important:** Your load balancer's forwarding rule must use TCP port 443 for the Google-managed certificate to be initially provisioned and automatically renewed.

## Step 3: Verify the target proxy association

After you've created or updated your load balancer, you can make sure that the SSL certificate is associated with your load balancer's target proxy.

If you don't already know the name of the target proxy, use the [`gcloud compute target-https-proxies list`](https://docs.cloud.google.com/load-balancing/docs/target-proxies#list-for-l7-xlb) and [`gcloud compute target-ssl-proxies list`](https://docs.cloud.google.com/load-balancing/docs/target-proxies#list-for-ssl-xlb) commands to list the target proxies in your project.

Verify association between the SSL certificate and the target proxy by running the following command.

**For global external Application Load Balancers:**
    
    
    gcloud compute target-https-proxies describe TARGET_HTTPS_PROXY_NAME \
        --global \
        --format="get(sslCertificates)"
    

**For external proxy Network Load Balancers:**
    
    
    gcloud compute target-ssl-proxies describe TARGET_SSL_PROXY_NAME \
        --format="get(sslCertificates)"
    

At this point, your Google-managed certificate status might still be `PROVISIONING`. Google Cloud is working with the Certificate Authority to issue the certificate. Provisioning a Google-managed certificate might take up to 60 minutes.

## Step 4: Update the DNS A and AAAA records to point to the load balancer's IP address

Your DNS records might be managed at your registrar's site, DNS host, or ISP.

While managing your records, note the following:

  * Ensure that DNS A records (for IPv4) and DNS AAAA records (for IPv6) for your domains and any subdomains point to the IP address associated with the load balancer's forwarding rule or rules.

To provision SSL certificates, ensure that A and AAAA records point to the load balancer's IP address at a public DNS.

  * If you're using [Cloud DNS](https://docs.cloud.google.com/dns/docs), [set up your domains](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#set-up-domain) and [update your name servers](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#update-nameservers).

  * If you have multiple domains in a Google-managed certificate, add or update DNS records for all domains and subdomains to point to your load balancer's IP address. The certificate validation fails if the domains and subdomains in a Google-managed certificate point to another IP than the load balancer's forwarding rule IP address.

  * Ensure that your DNS provider responds consistently to all the global domain validation requests.




Managed certificates provision successfully when the following are true:

  * Your domain's DNS records use a CNAME record that points to another domain.
  * The other domain contains an A or AAAA record that points to your load balancer's IP address.

**Important:** It's best to ensure that your domains are pointed directly at your load balancer's IP address. For load balancers that have Cloud CDN enabled, some third-party CDN providers might prevent validation requests from succeeding. This can happen if the CDN provider is actively proxying HTTP(S) traffic.

You can verify your setup by running the `dig` command. For example, suppose your domain is `www.example.com`. Run the following `dig` command:
    
    
    dig www.example.com
    
    
    
    ; <<>> DiG 9.10.6 <<>> www.example.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31748
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
    
    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;www.example.com.           IN  A
    
    ;; ANSWER SECTION:
    www.example.com. 1742    IN      CNAME   example.net.
    example.net.      12     IN      A       34.95.64.10
    
    ;; Query time: 43 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Wed Jun 03 16:54:44 PDT 2020
    ;; MSG SIZE  rcvd: 193
    

In this example, `34.95.64.10` is your load balancer's IP address.

DNS resolvers on the internet are outside the control of Google Cloud. They cache your resource record sets according to their time to live (TTL), which means that a `dig` or `nslookup` command might return a cached value. If you are using Cloud DNS, see [Propagation of changes](https://docs.cloud.google.com/dns/docs/overview#propagation_of_changes).

**Note:** DNS _domain validation_ is an automated process that periodically checks a domain's A and AAAA records for the matching IP address of a Google Cloud load balancer. This process has an automated exponential backoff for the wait time between validation checks. If a deployment is prepared ahead of time and a service cutover time is planned during a specific maintenance window a day or more after the initial deployment, Google recommends that you create or recreate the certificates shortly before or during the maintenance window than to rely on domain validation running during a certain time (due to the timer backoff).

### DNS record propagation time

Newly updated DNS A and AAAA records can take a significant amount of time to be fully propagated. Sometimes propagation across the internet takes up to 72 hours worldwide, although it typically takes a few hours.

Rerun the following command:
    
    
    gcloud compute ssl-certificates describe CERTIFICATE_NAME \
        --format="get(managed.domainStatus)"
    

If your domain status is `FAILED_NOT_VISIBLE`, it might be because propagation isn't complete.

For detailed information, see the [Google-managed SSL certificate domain status section on the Troubleshooting page](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#domain-status).

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

## Step 5: Test with OpenSSL

After the certificate and domain statuses are active, it can take up to 30 minutes for your load balancer to begin using your Google-managed SSL certificate.

To test, run the following OpenSSL command, replacing `DOMAIN` with your DNS name and `IP_ADDRESS` with the IP address of your load balancer.
    
    
    echo | openssl s_client -showcerts -servername DOMAIN -connect IP_ADDRESS:443 -verify 99 -verify_return_error
    

This command outputs the certificates that the load balancer presents to the client. Along with other detailed information, the output should include the certificate chain and `Verify return code: 0 (ok)`.

## Additional procedures

This section contains additional procedures for managing your certificates.

### Support multiple domains with a Google-managed SSL certificate

Multiple subject alternative names are supported. Each Google-managed SSL certificate supports up to [the maximum number of domains per Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/quotas#ssl_certificates).

If you have more than the maximum number of domains, you must request multiple Google-managed certificates. For example, if you try to create a Google-managed certificate with ([the maximum](https://docs.cloud.google.com/load-balancing/docs/quotas#ssl_certificates) \+ 1) domains, Google doesn't issue any certificates. Instead, you must create two or more Google-managed certificates and explicitly state which domains are associated with each certificate.

Google Cloud implements Server Name Indication (SNI), as defined in [RFC 6066](https://tools.ietf.org/html/rfc6066).

To help ensure that your certificates don't fail the domain validation step of the renewal process, review the [requirements for your DNS A and AAAA records](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns).

You cannot modify the list of domain names on an existing Google-managed SSL certificate. If you need to add or remove a domain, you must create a new certificate that includes all the domains you want to secure, and then use the replacement process described in this document.

### Renew a Google-managed SSL certificate

Google Cloud provisions managed certificates valid for 90 days. About one month before expiry, the process to renew your certificate automatically begins. For this, a Certificate Authority (CA) is chosen that's both in your domain's Certification Authority Authorization (CAA) DNS record and in the list of CAs.

The CA used for renewal might be different from the CA used to issue a previous version of your Google-managed certificate. You can control the CA that Google Cloud uses for renewal by ensuring that your domain's CAA DNS record specifies a single CA from the list of CAs that Google-managed certificates use.

To help ensure that your certificates don't fail the domain validation step of the renewal process, review the [requirements for your DNS A and AAAA records](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns).

### Specify the CAs that can issue your Google-managed certificate

In your DNS software, we recommend that you explicitly authorize the CAs that you want to allow to issue your Google-managed certificate. While not required in every scenario, this is necessary in certain situations.

For example, if you're using an external DNS service and your Google-managed certificate is revoked, the service might only validate a new certificate issued by one or more specific CAs.

To do this, create or modify a CAA record to include `pki.goog` or `letsencrypt.org` or both. If you don't have a CAA record, the default behavior is to allow both `pki.goog` and `letsencrypt.org`.
    
    
    DOMAIN. CAA 0 issue "pki.goog"
    DOMAIN. CAA 0 issue "letsencrypt.org"
    

Support for `letsencrypt.org` certificates is provided on a best-effort basis. For best reliability, allow both `pki.goog` and `letsencrypt.org`. If you specify just one of the CAs, only that CA is used to create and renew your certificate. This approach isn't recommended.

When you first create your certificate, Google Cloud selects either `pki.goog` or `letsencrypt.org` and uses it to issue your certificate. When Google renews your certificate, your certificate might be issued by the other CA, depending on the CAs that you have specified in the CAA record (if you created one). Your certificate might be renewed by a different CA in either of the following cases:

  * You don't have a DNS CAA record for your domain.
  * You have included both the CAs in the DNS CAA record.



For more information, see the RFC, [CAA DNS record](https://tools.ietf.org/html/rfc8659).

`letsencrypt.org` issues [Internationalized Domain Names (IDNs)](https://tools.ietf.org/html/rfc3490). `pki.goog` doesn't currently support IDNs.

If you're using Cloud DNS, learn how to [add a record](https://docs.cloud.google.com/dns/records#adding_or_removing_a_record), and make sure to set the `--type` flag to `CAA`.

**Note:** When you add a CA in the CAA record, it may take a significant amount of time for the DNS to propagate that change and make it visible to the CA. As a result, the certificate renewal process might initially fail, but eventually succeeds. For more information, see [Troubleshooting SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting).

### Replace an existing SSL certificate

To replace an existing SSL certificate:

  1. Start the process for creating the replacement Google-managed SSL certificate. This certificate does not become ACTIVE at this point.

  2. Update the target proxy so that the list of referenced certificates includes the replacement SSL certificate along with the current SSL certificates. The steps to update the target proxy vary, as follows:

     * [Update a target HTTPS proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies#update_target_proxies)
     * [Update a target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl#update_the_ssl_certificate_resource_for_the_target_ssl_proxy)
**Note:** To keep serving traffic, the target proxy must continue referencing the current SSL certificates. For the replacement certificate to complete its provisioning process, the target proxy must reference the replacement certificate as well.
  3. Wait for the replacement SSL certificate to complete provisioning. Provisioning might take up to 60 minutes. When provisioning is complete, the [certificate status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status) becomes `ACTIVE`.

**Note:** Provisioning a Google-managed certificate might take up to _60 minutes_ from the moment your DNS and load balancer configuration changes have propagated across the internet. If you have updated your DNS configuration recently, it can take a significant amount of time for the changes to _fully propagate_. Sometimes propagation takes up to 72 hours worldwide, although it typically takes a few hours. For more information on DNS propagation, see [Propagation of changes](https://docs.cloud.google.com/dns/docs/overview#propagation_of_changes).
  4. Wait an additional 30 minutes to ensure that the replacement certificate is available to all Google Front Ends (GFEs).

  5. Update the target proxy to remove the SSL certificate that you're replacing from the list of referenced certificates. The steps to update a target proxy vary, as follows:

     * [Update a target HTTPS proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies#update_the_ssl_certificate_resource_for_an_https_target_proxy)
     * [Update a target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl#update_the_ssl_certificate_resource_for_the_target_ssl_proxy)
  6. Wait 10 minutes, and confirm that the load balancer is using the replacement SSL certificate instead of the old one.

  7. Update the target proxy again, removing the old SSL certificate resource. You can delete the SSL certificate resource if it's no longer referenced by any target proxy.




If you don't delete the old SSL certificate, it remains ACTIVE until it expires.

### Migrate from self-managed SSL certificates to Google-managed SSL certificates

When you migrate a load balancer from using self-managed SSL certificates to Google-managed SSL certificates, you must perform the following steps in this sequence:

  1. Create a new Google-managed certificate.
  2. Associate new Google-managed certificate with the correct target proxy while maintaining the target proxy's association with the existing self-managed certificate.
  3. Wait until the [Google-managed certificate status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status) is `ACTIVE`.
  4. Wait 30 minutes to allow the new certificate to propagate to serving Google Front Ends (GFEs)
  5. Update the target proxy again, removing the self-managed certificate resource. You can [delete the self-managed SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#delete-ssl-cert-resource) if it's no longer referenced by any target proxy.

**Important:** Only remove your self-managed certificate from the target proxy _after_ your new certificate is provisioned, `ACTIVE`, and associated with the target proxy. If you delete your self-managed certificate too soon, your load balancer doesn't have a valid SSL certificate, and clients can't use it.

### Delete an SSL certificate

Before deleting an SSL certificate, make sure that no HTTPS or SSL target proxy references this certificate. You can do this in two ways:

  * [Delete the target proxies that reference this certificate](https://docs.cloud.google.com/load-balancing/docs/target-proxies#delete_a_target_proxy).

  * Update the target proxies that reference this certificate to exclude it. The steps vary, as follows:

    * [Update an HTTPS target proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies#update_the_ssl_certificate_resource_for_an_https_target_proxy).
    * [Update an SSL target proxy](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl#update_the_ssl_certificate_resource_for_the_target_ssl_proxy).



To delete one or more SSL certificates:

###  Console 

You can delete global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page.

  1. Go to the **Classic Certificates** tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. Select the SSL certificate that you want to delete.
  3. Click delete**Delete**.
  4. To confirm, click delete**Delete** again.



###  gcloud 

To delete a global SSL certificate (for global external Application Load Balancers or external proxy Network Load Balancers), use the [`gcloud compute ssl-certificates delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete) command with the `--global` command:
    
    
    gcloud compute ssl-certificates delete CERTIFICATE_NAME \
        --global
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the SSL certificate 



## What's next

  * To troubleshoot SSL certificates, see [Troubleshooting SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting).
  * To use a Terraform script that creates a Google-managed certificate, see the [Cloud Run example](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples#cloud-run) on the _Terraform module examples for external Application Load Balancer_ page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
