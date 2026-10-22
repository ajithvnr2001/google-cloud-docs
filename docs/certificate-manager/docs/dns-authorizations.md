---
url: https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations/
title: Manage DNS authorizations \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:41.454388+00:00
---

# Manage DNS authorizations  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage DNS authorizations Stay organized with collections  Save and categorize content based on your preferences. 

DNS authorizations let you prove ownership of domains for [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates). When creating a Google-managed certificate, one or more DNS authorizations can be specified to use for provisioning and renewal.

This page describes how to create and manage DNS authorizations for use with Google-managed certificates.

For more information, see [Domain authorizations](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#domain-auth).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [ Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a DNS authorization

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

A DNS authorization only covers a single domain name. You must create a separate DNS authorization for each domain name that you want to use with the target certificate.

If you're creating a DNS authorization for a wildcard certificate, such as `*.myorg.example.com`, configure the DNS authorization for the parent domain—for example, `myorg.example.com`.

To independently manage certificates across multiple projects, you can use `PER_PROJECT_RECORD` DNS authorization. Certificate Manager can handle issuing and managing certificates for each project independently within Google Cloud. DNS authorizations and certificates that you use within a project are self-contained and don't interact with those in other projects.

**Note:** Due to ongoing IETF standardization efforts, Google uses a custom implementation of account-based DNS authorization for per-project DNS authorizations.

###  Console 

You can create a DNS authorization or attach an existing DNS authorization when creating a certificate. For more information, see Create a Google-managed certificate referencing the DNS authorization.

###  gcloud 

Depending on your requirements, you can create any of these two types of DNS authorizations: `FIXED_RECORD` or `PER_PROJECT_RECORD`. For more information, see [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth).

**FIXED_RECORD DNS authorization**

To create a `FIXED_RECORD` DNS authorization, use the following [`gcloud certificate-manager dns-authorizations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/create):
    
    
    gcloud certificate-manager dns-authorizations create AUTHORIZATION_NAME \
        --domain="DOMAIN_NAME" \
        --type=[FIXED_RECORD] \
        [--location="LOCATION"]
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `LOCATION`: the target Google Cloud location where you create the DNS authorization.



After creating the `FIXED_RECORD` DNS authorization, verify it with the [`gcloud certificate-manager dns-authorizations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/describe):
    
    
    gcloud certificate-manager dns-authorizations describe AUTHORIZATION_NAME
    

The output is similar to the following. In the output, find the `dnsResourceRecord` line and get the `CNAME` record (`data`,`name`, and `type`) to [add to your DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth#cname-record).
    
    
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
        --type=PER_PROJECT_RECORD \
        [--location="LOCATION"]
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.
  * `LOCATION`: the target Google Cloud location where you create the DNS authorization.



After creating the `PER_PROJECT_RECORD` DNS authorization, verify it with the [`gcloud certificate-manager dns-authorizations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/describe):
    
    
    gcloud certificate-manager dns-authorizations describe AUTHORIZATION_NAME
    

The output is similar to the following. In the output, find the `dnsResourceRecord` section. Locate the `CNAME` record and add the record's details (`data`,`name`, and `type`) to your [DNS configuration](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#cname-record).
    
    
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
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/dnsAuthorizations?dns_authorization_id=AUTHORIZATION_NAME
    {
      "domain": "DOMAIN_NAME",
      "type": "PER_PROJECT_RECORD" //optional
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location where you create the DNS authorization. For the global location, use `global`.
  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DOMAIN_NAME`: the name of the target domain for which you are creating this DNS authorization. The domain name must be a fully qualified domain name, such as `myorg.example.com`.



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

## Update a DNS authorization

When you update a DNS authorization, you can do the following:

  * Specify new labels
  * Specify a new description



#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To update a DNS authorization, use the [`certificate-manager dns-authorizations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/update):
    
    
    gcloud certificate-manager dns-authorizations update AUTHORIZATION_NAME \
        [--update-labels="LABELS"] \
        [--description="DESCRIPTION"] \
        [--location="LOCATION"]
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `LABELS`: labels for this DNS authorization. This flag is optional.
  * `DESCRIPTION`: description for this DNS authorization. This flag is optional.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.



###  API 

Update a DNS authorization by making a `PATCH` request to the `dnsAuthorizations.patch` method as follows:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/LOCATION/dnsAuthorizations/AUTHORIZATION_NAME?updateMask=labels,description
    {
        description: "DESCRIPTION",
        labels: { "LABEL_KEY": "LABEL_VALUE" }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.
  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `DESCRIPTION`: an optional field that specifies the description for this DNS authorization.
  * `LABEL_KEY`: a label key applied to this DNS authorization.
  * `LABEL_VALUE`: a label value applied to this DNS authorization.



## List DNS authorizations

You can see all DNS authorizations in your project and their details.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)
  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To list DNS authorizations, use the [`certificate-manager dns-authorizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/list):
    
    
    gcloud certificate-manager dns-authorizations list \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY" \
        [--location="LOCATION"]
    

Replace the following:

  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter results by the following criteria:

    * Domain: `--filter='domain=myorg.example.com'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).

  * `LOCATION`: the target Google Cloud location. To list DNS authorizations from all regions, use `-` as the value. The default is `-`. This flag is optional.




###  API 

List all configured DNS authorizations by making a `GET` request to the `dnsAuthorizations.list` method as follows:
    
    
    GET /v1/projects/PROJECT_ID/locations/LOCATION/dnsAuthorizations?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. To see all DNS authorizations across all locations, specify a single hyphen (`-`).
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter results by the following criteria:

    * Domain: `--filter='domain=myorg.example.com'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`
  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## Delete a DNS authorization

To delete a DNS authorization that is assigned to Google-managed certificates, [delete the certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates#delete-certificate) before you delete the DNS authorization.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To delete a DNS authorization, use the [`certificate-manager dns-authorizations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/dns-authorizations/delete):
    
    
    gcloud certificate-manager dns-authorizations delete AUTHORIZATION_NAME \
        [--location="LOCATION"]
    

Replace the following:

  * `AUTHORIZATION_NAME`: the name of the DNS authorization.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.



###  API 

Delete a DNS authorization by making a `DELETE` request to the `dnsAuthorizations.delete` method as follows:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/LOCATION/dnsAuthorizations/AUTHORIZATION_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.
  * `AUTHORIZATION_NAME`: the name of the DNS authorization.



## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
