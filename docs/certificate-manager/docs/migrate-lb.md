---
url: https://docs.cloud.google.com/certificate-manager/docs/migrate-lb/
title: Migrate load balancer certificates to Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:31.501914+00:00
---

# Migrate load balancer certificates to Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/migrate-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Migrate load balancer certificates to Certificate Manager Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to migrate Cloud Load Balancing certificates to Certificate Manager. For more information about Cloud Load Balancing certificates, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) in the Cloud Load Balancing documentation.

To migrate Cloud Load Balancing certificates with no downtime, first identify the certificates that you want to migrate. Then, create the same number of Google-managed certificates as your Cloud Load Balancing certificates. Next, consolidate the certificates into a single certificate map, and test the certificate map in another load balancer. If your tests are successful, attach the certificate map to the target load balancer that hosts your Cloud Load Balancing certificates.

**Note:** Google-managed certificates with load balancer authorization aren't suitable for migration with no downtime because you can't issue them in advance. Using such certificates can cause service interruptions during the migration process.

To find the list of supported load balancers, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

## Objectives

This tutorial shows you how to complete the following tasks:

  * Identify certificates from the target load balancer to migrate.
  * Create Google-managed certificates.
  * Create a certificate map and certificate map entries.
  * Test the certificate map in another load balancer.
  * Attach the certificate map to the target load balancer.



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

## Identify the certificates to migrate

To identify the certificates that you want to migrate, follow these steps:

  1. On the load balancer, identify the name of the target proxy.

  2. Identify the certificates that you want to migrate.

To find the certificates attached to a target proxy, run the following command:
         
         gcloud compute target-https-proxies describe TARGET_PROXY_NAME
         

Replace `TARGET_PROXY_NAME` with the name of the target proxy.

The output is similar to the following:
         
         creationTimestamp: '2021-10-06T04:05:07.520-07:00'
         fingerprint: c9Txdx6AfcM=
         id: '365692570234384780'
         kind: compute#targetHttpsProxy
         name: my-proxy
         selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/targetHttpsProxies/my-proxy
         sslCertificates:
         - https://www.googleapis.com/compute/v1/projects/my-project/global/sslCertificates/my-first-certificate
         - https://www.googleapis.com/compute/v1/projects/my-project/global/sslCertificates/my-second-certificate
         urlMap: https://www.googleapis.com/compute/v1/projects/my-project/global/urlMaps/my-map
         

Note the names of certificates listed in the `sslCertificates` field. For more information, see [Target proxies overview](https://docs.cloud.google.com/load-balancing/docs/target-proxies).

  3. Get the details of each certificate:
         
         gcloud compute ssl-certificates --project=PROJECT_ID describe LB_CERTIFICATE_NAME
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project.
     * `LB_CERTIFICATE_NAME`: the name of the load balancer certificate.

The output is similar to the following:
    
    certificate: |
         -----BEGIN CERTIFICATE-----
         MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBX
         MQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UE
         CxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYx
         OTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoT
         GUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIx
         MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63
         ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwS
         iV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351k
         KSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZ
         DrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zk
         j5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5
         cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esW
         CruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499
         iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35Ei
         Eua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbap
         sZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b
         9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAP
         BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAf
         BgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIw
         JQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUH
         MAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6Al
         oCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAy
         MAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIF
         AwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9
         NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9
         WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw
         9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy
         +qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvi
         d0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=
         -----END CERTIFICATE-----
       creationTimestamp: '2021-05-06T04:39:21.736-07:00'
       expireTime: '2022-06-07T01:10:34.000-07:00'
       id: '6422259403966690822'
       kind: compute#sslCertificate
       managed:
          domainStatus:
          a.my-domain1.example.com: ACTIVE
          b.my-domain2.example.com: ACTIVE
          domains:
          - a.my-domain1.example.com
          - b.my-domain2.example.com
          status: ACTIVE
       name: my-certificate
       selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/sslCertificates/my-certificate
       subjectAlternativeNames:
       - a. my-domain1.example.com
       - b. my-domain2.example.com
       type: MANAGED
    




## Create Google-managed certificates

Create the same number of Google-managed certificates as your load balancer certificates. For a global or a classic load balancer, create global certificates; for a regional load balancer, create regional certificates; and for a cross-region load balancer, create cross-region certificates. Before you create the certificates, create a DNS authorization and add the CNAME record to the authoritative DNS zone for your domain.

You can choose to create [Google-managed certificates with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth) (recommended) or [self-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates#cert-self).

This section lists steps and commands to create _global_ Google-managed certificates. To create regional or cross-region Google-managed certificate, see [Create a Google-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/certificates#create_a_google-managed_certificate).

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

To create a global Google-managed certificate that references the DNS authorization you created in the previous steps, do the following:

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

### Verify the status of the certificate

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

## Create the certificate map

To deploy a certificate to a global external Application Load Balancer, [create a certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps#create_a_certificate_map).

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. Click add_box**Create certificate map**.

  3. In the **Name** field, enter a name for the certificate map, such as `cert-map-8`.

  4. In the **Description** field, enter a description for the certificate map, such as `My new certificate map`.

  5. To create a certificate map entry and add it to your certificate map, click add_box**Add map entry** and follow the steps mentioned in the subsequent section.

  6. To add a label and associate it with the certificate map, click add_box**Add label** and then enter a key and a value for your label.

  7. Click **Create**.




###  gcloud 

To create a certificate map, use the [`gcloud certificate-manager maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/create):
    
    
    gcloud certificate-manager maps create CERTIFICATE_MAP_NAME
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map



###  API 

To create a certificate map, make a `POST` request to the [`certificateMaps.create` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps/create):
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificateMaps?certificate_map_id=CERTIFICATE_MAP_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map



###  Terraform 

To create a certificate map, use a [`google_certificate_manager_certificate_map` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map):
    
    
    resource "google_certificate_manager_certificate_map" "default" {
      name        = "${local.name}-certmap1-${random_id.tf_prefix.hex}"
      description = "${local.domain} certificate map"
      labels = {
        "terraform" : true
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Create the certificate map entries

To deploy a certificate to a global external Application Load Balancer, create a certificate map entry.

For each certificate you want to migrate, create certificate map entries referencing those certificates as follows:

  1. Get the details of the certificate.

  2. In the log, for each domain listed in the `subjectAlternativeNames` field, [create a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create) covering that domain. If more than one certificate covers a single domain, you only need to create one certificate map entry and use any valid certificate covering that domain.
         
         gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
             --map="CERTIFICATE_MAP_NAME" \
             --certificates="CERTIFICATE_NAMES" \
             --hostname="HOSTNAME"
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated.
     * `CERTIFICATE_NAMES`: a comma-separated list of the names of the certificates that you want to associate with the certificate map entry.
     * `HOSTNAME`: hostname that you want to associate with the certificate map entry.
  3. [Create a primary certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-primary) referencing the certificate that corresponds to the first certificate from the list of certificates originally attached to the proxy.

**Important:** If you don't configure a primary certificate map entry, clients that don't support Server Name Indication (SNI) will fail to connect. It's strongly recommended that you configure a primary certificate map entry to prevent service disruption.
         
         gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
            --map="CERTIFICATE_MAP_NAME" \
            --certificates="CERTIFICATE_NAMES" \
            --set-primary
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated.
     * `CERTIFICATE_NAMES`: a comma-separated list of the names of the certificates that you want to associate with the certificate map entry.
  4. To [verify the active state of each certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#view_the_state_of_a_certificate_map_entry) you have created, run the following command:
         
         gcloud certificate-manager maps entries describe CERTIFICATE_MAP_ENTRY_NAME \
              --map="CERTIFICATE_MAP_NAME"
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated.

The output is similar to the following:
    
    certificates:
       - projects/my-project/locations/global/certificates/my-certificate
       createTime: '2021-09-06T10:01:56.229472109Z'
       hostname: example.com
       name: projects/my-project/locations/global/certificateMaps/myCertMap/certificateMapEntries/my-map-entry
       state: ACTIVE
       updateTime: '2021-09-06T10:01:58.277031787Z'
    




## Optional: Test your configuration on a new load balancer

To minimize downtime, we recommend that you test your newly configured certificate maps on a new load balancer that is not serving production traffic. This lets you detect and resolve any errors before proceeding with the migration in your production environment.

Test your configuration as follows:

  1. Create a global load balancer with a new target proxy. To create a load balancer, see the following pages:

     * To create a global external Application Load Balancer, see [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

     * To create a Global external proxy Network Load Balancer (SSL proxy), see [Set up a global external proxy Network Load Balancer (SSL proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl).

     * To create a Global external proxy Network Load Balancer (TCP proxy), see [Set up a global external proxy Network Load Balancer (TCP proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp).

  2. [Attach the certificate map](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#attach_the_certificate_map_to_the_target_proxy) to the new load balancer's target proxy.
         
         gcloud compute target-https-proxies create TEST_PROXY_NAME \
             --certificate-map="CERTIFICATE_MAP_NAME" \
             --global
         

Replace the following:

     * `TEST_PROXY_NAME`: the name of the test target proxy.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map referencing the certificate map entry and the associated certificate.
  3. For each target domain included in your migration, test the connectivity to the domain on the new load balancer's IP address:
         
         openssl s_client -showcerts -servername DOMAIN_NAME -connect IP_ADDRESS:443
         

Replace the following:

     * `DOMAIN_NAME`: the name of the target domain.
     * `IP_ADDRESS`: the IP address of your new load balancer.

For more information about testing connectivity, see [Test with OpenSSL](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#step_5_test_with_openssl)




### Clean up the test environment

Clean up the test environment you created in the previous steps.

Delete the test load balancer as described in [Deleting the load balancer](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup#deleting_the_load_balancer).

Don't delete the certificates, certificate map, or certificate map entries you created in the previous steps.

## Apply the new certificate map to the target load balancer

After you've tested your new certificate configuration and confirmed that it's valid, apply the new certificate map to the target load balancer (the load balancer that hosts your certificates) by following these steps.

**Caution:** Attaching a certificate map to a target proxy makes the load balancer ignore all individual certificates from the old `sslCertificates` field, not just the ones for domains covered by certificates in the certificate map. Proceed with caution if multiple certificates are attached to the target proxy. Ensure that the certificate map covers all domains that were previously served by the individual certificates.

  1. If you're using a global load balancer, [attach the certificate map to the new load balancer's target proxy](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#attach_the_certificate_map_to_the_target_proxy):
         
         gcloud compute target-https-proxies update TARGET_PROXY_NAME \
             --certificate-map="CERTIFICATE_MAP_NAME" \
             --global
         

Replace the following:

     * `TARGET_PROXY_NAME`: the name of the target proxy.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map referencing the certificate map entry and the associated certificate.
  2. Wait until the configuration change has been applied and the load balancer has started serving the new certificate. This typically takes a few minutes but can take up to 30 minutes.




Your certificates are migrated. If you notice any problems with your traffic, [detach the new certificate map from the target proxy](https://docs.cloud.google.com/certificate-manager/docs/maps#detach-proxy). This reverts your load balancer to its original configuration.

## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
