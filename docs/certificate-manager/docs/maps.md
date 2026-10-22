---
url: https://docs.cloud.google.com/certificate-manager/docs/maps/
title: Manage certificate maps \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:30.023328+00:00
---

# Manage certificate maps  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage certificate maps Stay organized with collections  Save and categorize content based on your preferences. 

A certificate map references one or more certificate map entries that assign specific certificates to specific hostnames. This page describes how to create and manage certificate maps.

For more information, see [Certificate maps](https://docs.cloud.google.com/certificate-manager/docs/core-components#cert-maps).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [ Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a certificate map

You can create a certificate map to refer to the certificate map entry associated with your certificate.

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

## Attach a certificate map to a proxy

After creating and configuring a certificate map with [certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries), attach the certificate map to the target proxy. Certificate Manager supports both target HTTPS and target SSL proxies with global scope. For more information about the differences between these proxy types, see [Use target proxies](https://docs.cloud.google.com/load-balancing/docs/target-proxies#use_target_proxies).

If you attach a TLS (SSL) certificate to the target proxy and also attach certificates through a certificate map, the proxy uses the certificates referenced in the certificate map and ignores the directly attached certificate.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To attach the certificate map to the target HTTPS proxy, use the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update):
    
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME"
    

To attach the certificate map to the target SSL proxy, use the [`gcloud compute target-ssl-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update):
    
    
    gcloud compute target-ssl-proxies update PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME"
    

Replace the following:

  * `PROXY_NAME`: name of the target proxy
  * `CERTIFICATE_MAP_NAME`: name of the certificate map that contains the map entries that reference the target certificates



###  API 

To attach the certificate map to the target HTTPS proxy, make a `POST` request to the [`targetHttpsProxies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies):
    
    
    POST /projects/PROJECT_ID/global/targetHttpsProxies/PROXY_NAME/setCertificateMap
    {
      certificateMap: "//certificatemanager.googleapis.com/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME",
    }
    

To attach the certificate map to the target SSL proxy, make a `POST` request to the [`targetSslProxies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies):
    
    
    POST /projects/PROJECT_ID/global/targetSslProxies/PROXY_NAME/setCertificateMap
    {
      certificateMap: "//certificatemanager.googleapis.com/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME",
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `PROXY_NAME`: name of the target proxy
  * `CERTIFICATE_MAP_NAME`: name of the certificate map that contains the map entries that reference the target certificates



## Detach a certificate map from a proxy

Before detaching a certificate map from a proxy, note the following:

  * If any TLS (SSL) certificates are attached directly to the proxy, detaching the certificate map causes the proxy to resume using them.

  * If no TLS (SSL) certificates are attached directly to the proxy, a certificate map can't be detached. Attach at least one TLS certificate directly to the proxy before detaching the certificate map.




#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Compute Load Balancer Admin role (`roles/compute.loadBalancerAdmin`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To detach any attached certificate map from the target HTTPS proxy, use the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update):
    
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --clear-certificate-map
    

To detach any attached certificate map from the target SSL proxy, use the [`gcloud compute target-ssl-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update):
    
    
    gcloud compute target-ssl-proxies update PROXY_NAME \
        --clear-certificate-map
    

Replace the following:

  * `PROXY_NAME`: name of the target proxy



###  API 

To detach any attached certificate map from the target HTTPS proxy, make a `POST` request to the [`targetHttpsProxies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies):
    
    
    POST /projects/PROJECT_ID/global/targetHttpsProxies/PROXY_NAME/setCertificateMap
    {
      certificateMap: "",
    }
    

To detach any attached certificate map from the target SSL proxy, make a `POST` request to the [`targetSslProxies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies):
    
    
    POST /projects/PROJECT_ID/global/targetSslProxies/PROXY_NAME/setCertificateMap
    {
      certificateMap: "",
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `PROXY_NAME`: name of the target proxy



## Update a certificate map

You can update a certificate map's description and labels. If you use the Google Cloud console, you can add a new map entry to a certificate map or edit or delete a map entry that's associated with a certificate map.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens.

  3. Click edit**Edit**. The **Edit certificate map** page opens.

  4. In the **Description** field, enter a new description for the certificate map.

  5. To add a new map entry to the certificate map, click add_box**Add map entry** and follow the steps mentioned in the [Create a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create) section.

To edit a map entry, under the **Actions** column of the map entry row, click the more_vert icon, select **Edit** , and then follow the steps mentioned in the [Update a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#update_a_certificate_map_entry) section.

To delete a map entry, under the **Actions** column of the map entry row, click the more_vert icon, select **Delete** , and then follow the steps mentioned in the [Delete a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-delete) section.

  6. You can add, delete, or update the labels associated with the certificate map.

To add a label, click add_box**Add label** , and then specify a key and a value for your label.

To delete a label, click delete**Delete item** for the required label.

  7. Click **Save**.




###  gcloud 

To update a certificate map, use the [`gcloud certificate-manager maps update` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/update):
    
    
    gcloud certificate-manager maps update CERTIFICATE_MAP_NAME \
        --description="DESCRIPTION"
        --update-labels="LABELS"
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map
  * `DESCRIPTION`: the new description for this certificate map
  * `LABELS`: a comma-separated list of labels applied to this certificate map



###  API 

To update a certificate map, make a `PATCH` request to the [`certificateMaps.patch` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps/patch):
    
    
    PATCH /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME?updateMask=labels,description
    {
      "description": "DESCRIPTION",
      "labels": {
        "LABEL_KEY": "LABEL_VALUE",
      }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map
  * `DESCRIPTION`: the new description for this certificate map
  * `LABEL_KEY`: a label key applied to this certificate map
  * `LABEL_VALUE`: a label applied to this certificate map



## List certificate maps

You can view, filter, and sort the list of all certificate maps that you've created.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)
  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. Click the **Certificate maps** tab. You can view, filter, and configure the display columns of all the certificate maps in the selected project.




###  gcloud 

To list certificate maps, use the [`gcloud certificate-manager maps list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/list):
    
    
    gcloud certificate-manager maps list \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY"
    

Replace the following:

  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`.

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




###  API 

To list configured certificate maps, make a `LIST` request to the [`certificateMaps.list` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps/list):
    
    
    GET /v1/projects/PROJECT_ID/locations/global/certificateMaps?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## View the details of a certificate map

You can view the details of an existing certificate map, such as its creation date-time, last update date-time, and description.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)
  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens with detailed information about the selected certificate map.




###  gcloud 

To view the details of a certificate map, use the [`gcloud certificate-manager maps describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/describe):
    
    
    gcloud certificate-manager maps describe CERTIFICATE_MAP_NAME
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map



###  API 

To view the details of the certificate map, make a `GET` request to the [`certificateMaps.get` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps/get):
    
    
    GET /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map



## Delete a certificate map

Before deleting a certificate map, do the following:

  * Detach the certificate map from the target proxy.
  * If any certificate map entries are assigned to the map, [delete the certificate map entries assigned to the certificate map](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-delete).



#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens.

  3. Click delete**Delete** , and then click **Delete**.




###  gcloud 

To delete a certificate map, use the [`gcloud certificate-manager maps delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/delete):
    
    
    gcloud certificate-manager maps delete CERTIFICATE_MAP_NAME
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map



###  API 

To delete the certificate map, make a `DELETE` request to the [`certificateMaps.delete` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps/delete):
    
    
    DELETE /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map



## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
