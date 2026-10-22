---
url: https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth/
title: Deploy a global Google-managed certificate with DNS authorization \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:06.104040+00:00
---

# Deploy a global Google-managed certificate with DNS authorization  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Deploy a global Google-managed certificate with DNS authorization Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Certificate Manager to deploy a global Google-managed certificate with [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth).

The following global load balancers support Google-managed certificates with DNS authorization:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Global external proxy Network Load Balancer
  * Classic proxy Network Load Balancer



If you want to deploy to cross-region load balancers or regional load balancers, see the following:

  * [Deploy a cross-region Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth-cross-reg)
  * [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional)



## Objectives

This tutorial shows you how to complete the following tasks:

  * Create a Google-managed certificate issued by a publicly trusted certificate authority with DNS authorization by using Certificate Manager.


  * Deploy the certificate to a supported load balancer by using a target HTTPS proxy.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Compute Engine, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Create a [public DNS zone](https://docs.cloud.google.com/dns/docs/zones#create-pub-zone)



### Required roles

Make sure that you have the following roles to complete the tasks in this tutorial:

  * Certificate Manager Owner (`roles/certificatemanager.owner`)

Required to create and manage Certificate Manager resources.

  * Compute Load Balancer Admin (`roles/compute.loadBalancerAdmin`) or Compute Network Admin (`roles/compute.networkAdmin`)

Required to create and manage HTTPS target proxy.



  * DNS Administrator (`roles/dns.admin`)

Required if you want to use Cloud DNS as your DNS solution.




For more information, see the following:

  * [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions) for Certificate Manager.
  * [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam) for Compute Engine.


  * [Roles and permissions](https://docs.cloud.google.com/dns/docs/access-control) for Cloud DNS.

**Note:** If you aren't assigned the permissions or roles, request the missing roles from the Identity and Access Management (IAM) administrator who has the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`).

### Domain names

To create certificates, get the fully qualified domain names (FQDNs) of the domains you own. If you don't have a domain, you can use Cloud Domains to [register a domain](https://docs.cloud.google.com/domains/docs/register-domain).

### Create the load balancer

This tutorial assumes that you've already created and configured the load balancer's backends, health checks, backend services, and URL maps. If you've created an external Application Load Balancer, note the name of the URL map because you need it later in this tutorial.

If you haven't created the load balancer, see the following pages to create one:

  * To create a global external Application Load Balancer, see [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

  * To create a classic Application Load Balancer, see [Set up a classic Application Load Balancer with a managed instance group backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple).

  * To create a Global external proxy Network Load Balancer (SSL proxy), see [Set up a global external proxy Network Load Balancer (SSL proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl).

  * To create a Classic proxy Network Load Balancer (SSL proxy), see [Set up a classic proxy Network Load Balancer (SSL proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl).




## Create a Google-managed certificate with DNS authorization

Before you create the certificate, create a public DNS zone. Then, create a DNS authorization and add the CNAME record to the target DNS zone.

### Create a DNS authorization

A DNS authorization only covers a single domain name. You must create a separate DNS authorization for each domain name that you want to use with the target certificate.

If you're creating a DNS authorization for a wildcard certificate, such as `*.myorg.example.com`, configure the DNS authorization for the parent domain—for example, `myorg.example.com`.

###  Console 

You can create a DNS authorization or attach an existing DNS authorization when creating a certificate. For more information, see Create a Google-managed certificate referencing the DNS authorization.

###  gcloud 

You can create two types of DNS authorizations: `FIXED_RECORD` or `PER_PROJECT_RECORD`. For more information, see [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth).

**Note:** Global Google-managed certificates use `FIXED_RECORD` as the default DNS authorization type.

**FIXED_RECORD DNS authorization**

To create a `FIXED_RECORD` DNS authorization, use the following [`gcloud certificate-manager dns-authorizations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/create):
    
    
    gcloud certificate-manager dns-authorizations create AUTHORIZATION_NAME \
        --domain="DOMAIN_NAME" \
        --type=[FIXED_RECORD]
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.



After creating the `FIXED_RECORD` DNS authorization, verify it with the [`gcloud certificate-manager dns-authorizations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/describe):
    
    
    gcloud certificate-manager dns-authorizations describe AUTHORIZATION_NAME
    

The output is similar to the following. In the output, find the `dnsResourceRecord` section. Locate the `CNAME` record and add the record's details (`data`,`name`, and `type`) to your [DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#cname-record).
    
    
    createTime: '2022-01-14T13:35:00.258409106Z'
    dnsResourceRecord:
      data: 0e40fc77-a37d-4eb8-8fe1-eea2e18d12d9.4.authorize.certificatemanager.goog.
      name: _acme-challenge.myorg.example.com.
      type: CNAME
    domain: myorg.example.com
    name: projects/myProject/locations/global/dnsAuthorizations/myAuthorization
    updateTime: '2022-01-14T13:35:01.571086137Z'
    

**PER_PROJECT_RECORD DNS authorization**

To create a `PER_PROJECT_RECORD` DNS authorization, use the following [`gcloud certificate-manager dns-authorizations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/create):
    
    
    gcloud certificate-manager dns-authorizations create AUTHORIZATION_NAME \
        --domain="DOMAIN_NAME" \
        --type=PER_PROJECT_RECORD
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.



After creating the `PER_PROJECT_RECORD` DNS authorization, verify it with the [`gcloud certificate-manager dns-authorizations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/describe):
    
    
    gcloud certificate-manager dns-authorizations describe AUTHORIZATION_NAME
    

The output is similar to the following. In the output, find the `dnsResourceRecord` section. Locate the `CNAME` record and add the record's details (`data`,`name`, and `type`) to your [DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#cname-record).
    
    
    createTime: '2022-01-14T13:35:00.258409106Z'
    dnsResourceRecord:
      data: 0e40fc77-a37d-4eb8-8fe1-eea2e18d12d9.4.authorize.certificatemanager.goog.
      name: _acme-challenge_ujmmovf2vn55tgye.myorg.example.com
      type: CNAME
    domain: myorg.example.com
    name: projects/myProject/locations/global/dnsAuthorizations/myAuthorization
    updateTime: '2022-01-14T13:35:01.571086137Z'
    

**Note:** For `PER_PROJECT_RECORD` DNS authorization, Certificate Manager supports only the certificates issued by [Google Trust Services](https://pki.goog). Certificates issued by other authorities, such as Let's Encrypt CA, aren't supported.

###  Terraform 

To create a DNS authorization, you can use a [`google_certificate_manager_dns_authorization` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_dns_authorization).
    
    
    resource "google_certificate_manager_dns_authorization" "default" {
      name        = "${local.name}-dnsauth-${random_id.tf_prefix.hex}"
      description = "The default dns auth"
      domain      = local.domain
      labels = {
        "terraform" : true
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

To create a DNS authorization, make a `POST` request to the `dnsAuthorizations.create` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/global/dnsAuthorizations?dns_authorization_id=AUTHORIZATION_NAME
    {
      "domain": "DOMAIN_NAME",
      "type": "PER_PROJECT_RECORD" //optional
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.



### Create a Google-managed certificate referencing the DNS authorization

To create a Google-managed certificate that references the DNS authorization you created in the previous steps, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate. 

  5. For **Location** , select **Global**.

  6. For **Scope** , select **Default**. 

  7. For **Certificate type** , select **Create Google-managed certificate**.

  8. For **Certificate Authority type** , select **Public**.

  9. In the **Domain Names** field, specify a comma-separated list of domain names of the certificate. Each domain name must be a fully qualified domain name, such as `myorg.example.com`. The domain name can also be a wildcard domain name, such as `*.example.com`.

  10. For **Authorization type** , select **DNS authorization**.

The page lists DNS authorizations of the domain names. If a domain name doesn't have an associated DNS authorization, follow these steps to create one:

     1. Click **Create missing DNS authorization**.
     2. In the **DNS authorization name** field, specify the name of the DNS authorization. The default DNS authorization type is `FIXED_RECORD`. To independently manage certificates across multiple projects, select the **Per project authorization** checkbox. 
     3. Click **Create DNS authorization**.
  11. In the **Labels** field, specify labels to associate to the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  12. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a global Google-managed certificate with DNS authorization, run the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create) with the `dns-authorizations` flag:
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --domains="DOMAIN_NAME,*.DOMAIN_NAME" \
        --dns-authorizations="AUTHORIZATION_NAMES"
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`, or a wildcard domain, such as `*.myorg.example.com`. The asterisk dot prefix `(*.)` signifies a wildcard certificate.
  * `AUTHORIZATION_NAMES`: a comma-separated list of the names of DNS authorizations you created for the certificate.



###  Terraform 

Use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate).
    
    
    resource "google_certificate_manager_certificate" "root_cert" {
      name        = "${local.name}-rootcert-${random_id.tf_prefix.hex}"
      description = "The wildcard cert"
      managed {
        domains = [local.domain, "*.${local.domain}"]
        dns_authorizations = [
          google_certificate_manager_dns_authorization.default.id
        ]
      }
      labels = {
        "terraform" : true
      }
    }

###  API 

Create the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificates?certificate_id=CERTIFICATE_NAME
    {
     "managed": {
      "domains": ["DOMAIN_NAME"],
      "dnsAuthorizations": [
       "projects/PROJECT_ID/locations/global/dnsAuthorizations/AUTHORIZATION_NAME",
      ],
     }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `DOMAIN_NAME`: the name of the target domain. The domain name must be a fully qualified domain name, such as `myorg.example.com`, or a wildcard domain, such as `*.myorg.example.com`. The asterisk dot prefix (*.) signifies a wildcard certificate.
  * `AUTHORIZATION_NAMES`: a comma-separated list of the names of DNS authorizations.

**Note:** To specify multiple domains or DNS authorizations, provide a comma-separated list of values in their respective fields.

### Add the CNAME record to your DNS configuration

If you're using a third-party DNS solution to manage your DNS, refer to its documentation to add the CNAME record to the DNS configuration. If you're using Google Cloud to manage your DNS, complete the steps in this section.

**Important:** You must ensure that your `CNAME` is the _only_ resource record for a specific DNS name. Although some DNS providers allow you to configure both `CNAME` and `TXT` resource records for the same DNS name, this type of configuration is incorrect and can lead to conflicts, preventing reliable certificate issuance or renewal. If such a conflict occurs, then you can either delete your `TXT` records or use the [per-project DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#gcloud) method.

###  Console 

To create a record set, follow these steps:

  1. In the Google Cloud console, go to the **DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/)

  2. Click the name of the DNS zone where you want to add the record.

  3. On the **Zone details** page, click **Add standard**.

  4. On the **Create record set** page, in the **DNS name** field, enter the subdomain of the DNS zone.

When entering the subdomain name, make sure that the subdomain name, including the greyed-out text displayed in the **DNS name** field, matches the full value of the `dnsResourceRecord.name` field as displayed in the output of the `gcloud certificate-manager dns-authorizations describe` command.

See the following examples:

     * If the `dnsResourceRecord.name` field value is `_acme-challenge.myorg.example.com.`, and the greyed-out text in the **DNS name** field is `.example.com.`, then enter `_acme-challenge.myorg`.

     * If the `dnsResourceRecord.name` field value is `_acme-challenge.myorg.example.com.` , and the greyed-out text in the **DNS name** field is `.myorg.example.com.`, then enter `_acme-challenge`.

     * If the value of the `dnsResourceRecord.name` field is `_acme-challenge_ujmmovf2vn55tgye.myorg.example.com.`, and the greyed-out text in the **DNS name** field is `.myorg.example.com.`, then enter `_acme-challenge_ujmmovf2vn55tgye`.

**Note:** Adding the @ symbol in this field causes the record to fail.
  5. In the **Resource record type** field, select **CNAME**.

  6. In the **TTL** field, enter a positive numeric value for the resource record's time to live, which is the amount of time that it can be cached.

  7. From the **TTL unit** list, select the unit of time—for example, `30 minutes`.

  8. In the **Canonical name** field, enter the full value of the `dnsResourceRecord.data` field as displayed in the output of the `gcloud certificate-manager dns-authorizations describe` command.

  9. To enter additional information, click **Add item**.

  10. Click **Create**.




###  gcloud 

When you create a DNS authorization, the gcloud CLI command returns the corresponding CNAME record. To add the CNAME record to your DNS configuration in the DNS zone of the target domain, follow these steps:

  1. Initiate the DNS record transaction:
         
         gcloud dns record-sets transaction start --zone="DNS_ZONE_NAME"
         

Replace `DNS_ZONE_NAME` with the name of the target DNS zone.

  2. Add the CNAME record to the target DNS zone:
         
         gcloud dns record-sets transaction add CNAME_RECORD \
             --name="VALIDATION_SUBDOMAIN_NAME.DOMAIN_NAME." \
             --ttl="30" \
             --type="CNAME" \
             --zone="DNS_ZONE_NAME"
         

Replace the following:

     * `CNAME_RECORD`: the full data value of the CNAME record returned by the Google Cloud CLI command that created the corresponding DNS authorization.
     * `VALIDATION_SUBDOMAIN_NAME`: the prefix subdomain of the DNS zone, such as `_acme-challenge`. You can copy the name from the `gcloud certificate-manager dns-authorizations describe` command log, as described in Create a DNS authorization.
     * `DOMAIN_NAME`: the name of the target domain.The domain name must be a fully qualified domain name, such as `myorg.example.com`. You must also include the trailing period after the target domain name.
     * `DNS_ZONE_NAME`: the name of the target DNS zone.

For more information about the difference between `FIXED_RECORD` and `PER_PROJECT_RECORD` DNS authorizations, see the following examples. The only difference between the two examples is the value of the `--name` flag.

**FIXED_RECORD DNS authorization**
    
    gcloud dns record-sets transaction add 0e40fc77-a37d-4eb8-8fe1-eea2e18d12d9.4.authorize.certificatemanager.goog. \
        --name="_acme-challenge.myorg.example.com." \
        --ttl="30" \
        --type="CNAME" \
        --zone="myorg-example-com"
    

**PER_PROJECT_RECORD DNS authorization**
    
    gcloud dns record-sets transaction add 0e40fc77-a37d-4eb8-8fe1-eea2e18d12d9.4.authorize.certificatemanager.goog. \
        --name="_acme-challenge_ujmmovf2vn55tgye.myorg.example.com." \
        --ttl="30" \
        --type="CNAME" \
        --zone="myorg-example-com"
    

  3. Run the DNS record transaction to save your changes:
         
         gcloud dns record-sets transaction execute --zone="DNS_ZONE_NAME"
         

Replace `DNS_ZONE_NAME` with the name of the target DNS zone.




###  Terraform 

To add the CNAME record to your DNS configuration, you can use a [`google_dns_record_set` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dns_record_set).
    
    
    resource "google_dns_record_set" "cname" {
      name         = google_certificate_manager_dns_authorization.default.dns_resource_record[0].name
      managed_zone = google_dns_managed_zone.default.name
      type         = google_certificate_manager_dns_authorization.default.dns_resource_record[0].type
      ttl          = 300
      rrdatas      = [google_certificate_manager_dns_authorization.default.dns_resource_record[0].data]
    }

## Verify the status of the certificate

Before deploying a certificate to a load balancer, verify that it's active. It can take several minutes for the certificate state to change to `ACTIVE`.

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, check the **Status** column for the certificate.




###  gcloud 

To verify the status of the certificate, run the following command:
    
    
    gcloud certificate-manager certificates describe CERTIFICATE_NAME
    

Replace `CERTIFICATE_NAME` with the name of the target Google-managed certificate.

The output is similar to the following:
    
    
    createTime: '2021-10-20T12:19:53.370778666Z'
    expireTime: '2022-05-07T05:03:49Z'
    managed:
      authorizationAttemptInfo:
      - domain: myorg.example.com
        state: AUTHORIZED
      dnsAuthorizations:
        - projects/myProject/locations/global/dnsAuthorizations/myCert
      domains:
      - myorg.example.com
      state: ACTIVE
    name: projects/myProject/locations/global/certificates/myCert
    pemCertificate: |
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
    sanDnsnames:
      -   myorg.example.com
    updateTime: '2021-10-20T12:19:55.083385630Z'
    

If the certificate state is not `ACTIVE` after several hours, check that you correctly added the `CNAME` record to your DNS configuration.

For more troubleshooting steps, see [Troubleshoot Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting).

## Deploy the certificate to a load balancer

To deploy a global Google-managed certificate, deploy the certificate by using a certificate map.

### Create a certificate map

Create a certificate map that references the certificate map entry associated with your certificate:

###  gcloud 

To create a certificate map, use the [`gcloud certificate-manager maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/create):
    
    
    gcloud certificate-manager maps create CERTIFICATE_MAP_NAME
    

Replace `CERTIFICATE_MAP_NAME` with the name of the target certificate map.

###  Terraform 

To create a certificate map, you can use a [`google_certificate_manager_certificate_map` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map).
    
    
    resource "google_certificate_manager_certificate_map" "certificate_map" {
      name        = "${local.name}-certmap-${random_id.tf_prefix.hex}"
      description = "${local.domain} certificate map"
      labels = {
        "terraform" : true
      }
    }

### Create a certificate map entry

Create a certificate map entry and associate it with your certificate and certificate map:

###  gcloud 

To create a certificate map entry, use the [`gcloud certificate-manager maps entries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create):
    
    
    gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME" \
        --certificates="CERTIFICATE_NAME" \
        --hostname="HOSTNAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated.
  * `CERTIFICATE_NAME`: the name of the certificate you want to associate with the certificate map entry.
  * `HOSTNAME`: hostname that you want to associate with the certificate map entry.

If you want to create a certificate that covers both a wildcard domain and a root domain, then specify the hostname with a root and a wildcard, such as `example.com` and `*.example.com`. In addition, you must specify two certificate map entries - one for `example.com` and the other for `*.example.com`.




###  Terraform 

To create a certificate map entry with a root domain, use a [`google_certificate_manager_certificate_map_entry` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map_entry).
    
    
    resource "google_certificate_manager_certificate_map_entry" "first_entry" {
      name        = "${local.name}-first-entry-${random_id.tf_prefix.hex}"
      description = "example certificate map entry"
      map         = google_certificate_manager_certificate_map.certificate_map.name
      labels = {
        "terraform" : true
      }
      certificates = [google_certificate_manager_certificate.root_cert.id]
      hostname     = local.domain
    }

To create a certificate map entry with a wildcard domain, use a [`google_certificate_manager_certificate_map_entry` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map_entry).
    
    
    resource "google_certificate_manager_certificate_map_entry" "second_entry" {
      name        = "${local.name}-second-entity-${random_id.tf_prefix.hex}"
      description = "example certificate map entry"
      map         = google_certificate_manager_certificate_map.certificate_map.name
      labels = {
        "terraform" : true
      }
      certificates = [google_certificate_manager_certificate.root_cert.id]
      hostname     = "*.${local.domain}"
    }

### Verify that the certificate map entry is active

Verify that the certificate map entry is active before attaching its corresponding certificate map to the target proxy.

To verify the certificate map entry, use the [`gcloud certificate-manager maps entries describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/describe):
    
    
    gcloud certificate-manager maps entries describe CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
  * `CERTIFICATE_NAME`: the name of the certificate you want to associate with the certificate map entry.



The output is similar to the following:
    
    
    certificates:
    createTime: '2021-09-06T10:01:56.229472109Z'
    hostname: example.com
    name: projects/my-project/locations/global/certificateMaps/myCertMap/certificateMapEntries/myCertMapEntry
    state: ACTIVE
    updateTime: '2021-09-06T10:01:58.277031787Z'
    

### Attach the certificate map to the target proxy

You can attach the certificate map to a new target proxy or an existing target proxy.

###  gcloud 

To attach the certificate map to a new target proxy, use the [`gcloud compute target-https-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create):
    
    
    gcloud compute target-https-proxies create PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME" \
        --url-map="URL_MAP" \
        --global
    

Replace the following:

  * `PROXY_NAME`: name of the target proxy.
  * `CERTIFICATE_MAP_NAME`: name of the certificate map referencing the certificate map entry and the associated certificate.
  * `URL_MAP`: the name of the URL map



To attach the certificate map to an existing target HTTPS proxy, use the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update). If you don't know the name of the existing target proxy, go to the [**Target proxies**](https://console.cloud.google.com/net-services/loadbalancing/advanced/targetProxies/list) page and note the name of the target proxy.
    
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME" \
        --global
    

After creating or updating the target proxy, run the following command to verify it:
    
    
    gcloud compute target-https-proxies list
    

###  Terraform 

To attach the certificate map to the target proxy, you can use a [`google_compute_target_https_proxy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy).

When configuring a target proxy, if you attach TLS (SSL) certificates directly and also through a certificate map, the proxy uses the certificates referenced by the certificate map and ignores the directly attached TLS (SSL) certificates.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete them.

  1. Delete the load balancer and its resources.

See [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).

  2. Delete or detach the certificate map from the proxy.

To delete the certificate map, run the following command:
         
         gcloud compute target-https-proxies delete PROXY_NAME
         

If you want to keep the target HTTPS proxy, then detach the certificate map from the proxy. 

**Caution:** Before you detach the certificate map, note the following considerations.
     * If there are any TLS (SSL) certificates attached directly to the proxy, then detaching the certificate map causes the proxy to resume using those directly attached TLS (SSL) certificates.
     * If there are no TLS (SSL) certificates attached directly to the proxy, then the certificate map can't be detached from the proxy. You must first attach at least one TLS (SSL) certificate directly to the proxy before you can detach the certificate map.

To detach the certificate map, run the following command:
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --clear-certificate-map
    

Replace `PROXY_NAME` with the name of the target proxy.

  3. Delete the certificate map entry from the certificate map:
         
         gcloud certificate-manager maps entries delete CERTIFICATE_MAP_ENTRY_NAME \
             --map="CERTIFICATE_MAP_NAME"
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map.
  4. Delete the certificate map:
         
         gcloud certificate-manager maps delete CERTIFICATE_MAP_NAME
         

Replace `CERTIFICATE_MAP_NAME` with the name of the certificate map.

  5. Delete the Google-managed certificate:

###  Console 

     1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

     2. On the **Certificates** tab, select the checkbox of the certificate.

     3. Click **Delete**.

     4. In the dialog that appears, click **Delete** to confirm.

###  gcloud 
    
    gcloud certificate-manager certificates delete CERTIFICATE_NAME
    

Replace `CERTIFICATE_NAME` with the name of the target certificate.

  6. Delete the DNS authorization:
         
         gcloud certificate-manager dns-authorizations delete AUTHORIZATION_NAME
         

Replace `AUTHORIZATION_NAME` with the name of the DNS authorization.




## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
