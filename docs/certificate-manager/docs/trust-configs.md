---
url: https://docs.cloud.google.com/certificate-manager/docs/trust-configs/
title: Manage trust configs \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:57.848249+00:00
---

# Manage trust configs  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/trust-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage trust configs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage trust configs for use in various mutual TLS authentication (mTLS) scenarios.

For more information about mTLS, see the following resources:

  * To understand the concepts of trust configs, trust anchors, and intermediate certificates, see [Trust configs](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-configs).

  * To learn more about mTLS, see [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls) in the Cloud Load Balancing documentation.

  * To use a trust config to configure mTLS on your target proxy, see the following pages in the Cloud Load Balancing documentation:

    * [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
    * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)

**Note:** The Google Cloud CLI instructions on this page assume that you are using [ Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a trust config

When you create a trust config, you must specify the trust anchors that are used to validate the certificate.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

To create a trust config, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Trust configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/trustConfigs)

  2. Click **Add Trust Config**. The **Create Trust Config** page appears.

  3. In the **Name** field, enter a name for the configuration.

The name must be unique for the project. Also, it must start with a lowercase letter, followed by up to 62 lowercase letters, numbers, or hyphens, and must not end with a hyphen.

  4. Optional: In the **Description** field, enter a description for the configuration. This description helps you identify a specific configuration later.

  5. Optional: In the **Labels** field, specify labels to associate to the trust config. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  6. For **Location** , select **Global** or **Regional**.

If you selected **Regional** , select the **Region**.

  7. In the **Trust store** section, add trust anchors and intermediate CAs.

You can specify multiple trust anchors and intermediate certificates by using multiple instances of the complete PEM payload for the certificate, one certificate per instance.

     1. In the **Trust anchors** section , click **Add trust anchor** and upload the PEM-encoded certificate file, or copy the contents of the certificate. When you have finished, click **Add**.

     2. Optional: In the **Intermediate CAs** section, click **Add intermediate CA** and upload the PEM-encoded intermediate certificate file, or copy the contents of the intermediate certificate. When you have finished, click **Add**.

This step lets you add another level of trust between the root certificate and your server certificate.

     3. Optional: In the **Allowlisted certificates** section, click **Add certificate** and upload the PEM-encoded certificate file, or copy the contents of the certificate. This adds the certificate to an allowlist. When you have finished, click **Add**.

To specify multiple trust anchors or intermediate certificates within the trust config resource specification, use multiple instances of the `pemCertificate` field. Each instance of the field contains a single certificate.

The trust config always considers a certificate on an allowlist as valid. To encapsulate multiple certificates on an allowlist, use multiple instances of the `pemCertificate` field, one certificate per instance. You don't need a trust store when using certificates added to an allowlist.

The trust config always considers a certificate on an allowlist valid if it fulfills specific conditions: it must be parseable, possess proof of private key ownership, and adhere to constraints on the certificate's SAN field. Expired certificates are also considered valid when they are added to an allowlist. For more information about the PEM-encoded format, see [RFC 7468](https://tools.ietf.org/html/rfc7468).

  8. Click **Create**.




Verify that the new trust config appears in the list of configurations.

###  gcloud 

  1. Create a trust config YAML file that specifies the trust config parameters.

The file has the following format:
         
         name: "TRUST_CONFIG_ID"
         trustStores:
         - trustAnchors:
           - pemCertificate: "CERTIFICATE_PEM_PAYLOAD"
           intermediateCas:
           - pemCertificate: "INTER_CERT_PEM_PAYLOAD"
         allowlistedCertificates:
         - pemCertificate: "ALLOWLISTED_CERT1"
         - pemCertificate: "ALLOWLISTED_CERT2"
         

Replace the following:

     * `TRUST_CONFIG_ID`: the ID of the trust config resource.
     * `CERTIFICATE_PEM_PAYLOAD`: the complete PEM payload for the certificate to use for the trust config resource.
     * `INTER_CERT_PEM_PAYLOAD`: the complete PEM payload for the intermediate certificate to use for the trust config resource.
     * `ALLOWLISTED_CERT1` and `ALLOWLISTED_CERT2`: the certificates that are added to an allowlist to use for this trust config resource.

To specify multiple trust anchors or intermediate certificates within the trust config resource specification, use multiple instances of the `pemCertificate` field. Each instance of the field contains a single certificate.

The trust config always considers a certificate on an allowlist as valid. To encapsulate multiple certificates on an allowlist, use multiple instances of the `pemCertificate` field, one certificate per instance. You don't need a trust store when using certificates added to an allowlist.

The trust config always considers a certificate on an allowlist valid if it fulfills specific conditions: it must be parseable, possess proof of private key ownership, and adhere to constraints on the certificate's SAN field. Expired certificates are also considered valid when they are added to an allowlist. For more information about the PEM-encoded format, see [RFC 7468](https://tools.ietf.org/html/rfc7468).

  2. To import the trust config YAML file, use the `gcloud certificate-manager trust-configs import` command:
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_ID \
           --project=PROJECT_ID \
           --source=TRUST_CONFIG_FILE \
           --location=LOCATION
         

Replace the following:

     * `TRUST_CONFIG_ID`: the ID of the trust config resource.
     * `PROJECT_ID`: ID of your Google Cloud project.
     * `TRUST_CONFIG_FILE`: the full path and name of the trust config YAML file that you created in step 1.
     * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.



###  API 

Make a `POST` request to the `trustConfigs.create` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/trustConfigs?trust_config_id=TRUST_CONFIG_ID
    {
      "description": "DESCRIPTION",
      "trust_stores": [{
        "trust_anchors": [{
          "pem_certificate": "CERTIFICATE_PEM_PAYLOAD"
        }],
        "intermediate_cas": [{
          "pem_certificate": "INTER_CERT_PEM_PAYLOAD"
        }],
      }],
      "allowlistedCertificates": [{
        "pem_certificate": "ALLOWLISTED_CERT"
      }],
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.
  * `TRUST_CONFIG_ID`: the ID of the trust config resource.
  * `DESCRIPTION`: a meaningful description for this trust config resource. This value is optional.
  * `CERTIFICATE_PEM_PAYLOAD`: the complete PEM payload for the certificate to use for the trust config resource.
  * `INTER_CERT_PEM_PAYLOAD`: the complete PEM payload for the intermediate certificate to use for the trust config resource. This value is optional.
  * `ALLOWLISTED_CERT`: the certificate that is added to an allowlist to use for this trust config resource. This value is optional.



## Update a trust config

To update a trust config, you create another trust config YAML file that specifies the new trust config parameters and import this file into Certificate Manager.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Trust configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/trustConfigs)

  2. Locate and select the trust config that you want to update.

  3. In the **More Options** column, click more_vert**More actions** for the config you want to update, and then select **Edit**.

  4. Make the required changes.

  5. Click **Save**.




Verify that the configuration changes are updated.

###  gcloud 

  1. Export the trust config YAML file.
         
         gcloud certificate-manager trust-configs export TRUST_CONFIG_ID \
             --project=PROJECT_ID \
             --destination=TRUST_CONFIG_FILE \
             --location=LOCATION
         

Replace the following:

     * `TRUST_CONFIG_ID`: the ID of the trust config resource.
     * `PROJECT_ID`: ID of your Google Cloud project.
     * `TRUST_CONFIG_FILE`: the full path and name of the trust config YAML file.
     * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.
  2. Edit the trust config YAML file.

The file has the following format:
         
         name: "TRUST_CONFIG_ID"
         trustStores:
         - trustAnchors:
           - pemCertificate: "CERTIFICATE_PEM_PAYLOAD"
           intermediateCas:
           - pemCertificate: "INTER_CERT_PEM_PAYLOAD"
         allowlistedCertificates:
         - pemCertificate: "ALLOWLISTED_CERT1"
         - pemCertificate: "ALLOWLISTED_CERT2"
         

Replace the following:

     * `TRUST_CONFIG_ID`: the ID of the trust config resource.
     * `CERTIFICATE_PEM_PAYLOAD`: the complete PEM payload for the certificate to use for the trust config resource.
     * `INTER_CERT_PEM_PAYLOAD`: the complete PEM payload for the intermediate certificate to use for the trust config resource. This value is optional.
     * `ALLOWLISTED_CERT1` and `ALLOWLISTED_CERT2`: the certificates that are added to an allowlist to use for this trust config resource. This value is optional.
  3. Import the new trust config file into Certificate Manager against the existing trust config resource name.
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_ID \
             --project=PROJECT_ID \
             --source=TRUST_CONFIG_FILE \
             --location=LOCATION
         

Replace the following:

     * `TRUST_CONFIG_ID`: the ID of the trust config resource.
     * `PROJECT_ID`: ID of your Google Cloud project.
     * `TRUST_CONFIG_FILE`: the full path and name of the trust config YAML file.
     * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.



###  API 

Make a `PATCH` request to the `trustConfigs.update` method:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/LOCATION/trustConfigs/TRUST_CONFIG_ID?update_mask=*
      {
        "description": "DESCRIPTION",
        "trust_stores": [{
          "trust_anchors": [{
            "pem_certificate": "CERTIFICATE_PEM_PAYLOAD"
          }],
          "intermediate_cas": [{
            "pem_certificate": "INTER_CERT_PEM_PAYLOAD"
          }],
        }],
        "allowlistedCertificates": [{
          "pem_certificate": "ALLOWLISTED_CERT"
      }],
      }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.
  * `TRUST_CONFIG_ID`: the ID of the trust config resource.
  * `DESCRIPTION`: a meaningful description for this trust config resource. This description is optional.
  * `CERTIFICATE_PEM_PAYLOAD`: the complete PEM payload for the certificate to use for the trust config resource.
  * `INTER_CERT_PEM_PAYLOAD`: the complete PEM payload for the intermediate certificate to use for the trust config resource. This value is optional.
  * `ALLOWLISTED_CERT`: the certificate that is added to an allowlist to use for this trust config resource. This value is optional.



## List trust configs

You can see all configured trust configs of your project.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)
  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

### Console

  1. In the Google Cloud console, go to the **Trust configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/trustConfigs)

  2. On the **Trust configs** tab, you can view a list of all the configured trust config resources in the selected project.




###  gcloud 

Use the `gcloud certificate-manager trust-configs list` command:
    
    
    gcloud certificate-manager trust-configs list \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY" \
        --location=LOCATION
    

Replace the following:

  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).

  * `LOCATION`: the region where the trust config resource is stored. To list trust configs from all regions, use `-` as the value. The default is `-`. This flag is optional.




###  API 

Make a `GET` request to the `trustConfigs.list` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/LOCATION/trustConfigs?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the region where the trust config resource is stored. To see all trust configs across all locations, specify a single hyphen (`-`).
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## View trust configs

You can see details of a specific trust config.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)
  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

### Console

  1. In the Google Cloud console, go to the **Trust configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/trustConfigs)

  2. Click the trust config resource that you want to view. The **Trust Config details** page displays detailed information about the selected trust config resource.




###  gcloud 

Use the `gcloud certificate-manager trust-configs describe` command:
    
    
    gcloud certificate-manager trust-configs describe TRUST_CONFIG_ID \
        --location=LOCATION
    

Replace the following:

  * `TRUST_CONFIG_ID`: the ID of the trust config resource.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.



###  API 

Make a `GET` request to the `trustConfigs.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/LOCATION/trustConfigs/TRUST_CONFIG_ID
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.
  * `TRUST_CONFIG_ID`: the ID of the trust config resource.



## Delete a trust config

Before deleting a trust config, detach the trust config from the Client Authentication (`ServerTlsPolicy`) resource.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Trust configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/trustConfigs)

  2. Select the checkbox of the trust config that you want to delete.

  3. Click **Delete**.

  4. In the dialog that appears, click **Delete** to confirm.




###  gcloud 

Use the `gcloud certificate-manager trust-configs delete` command:
    
    
    gcloud certificate-manager trust-configs delete TRUST_CONFIG_ID \
        --location=LOCATION
    

Replace the following:

  * `TRUST_CONFIG_ID`: the ID of the trust config resource.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.



###  API 

Make a `DELETE` request to the `trustConfigs.delete` method:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/LOCATION/trustConfigs/TRUST_CONFIG_ID
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the region where the trust config resource is stored. The default location is `global`.
  * `TRUST_CONFIG_ID`: the ID of the trust config resource.



## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
