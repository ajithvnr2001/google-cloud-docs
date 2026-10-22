---
url: https://docs.cloud.google.com/certificate-manager/docs/map-entries/
title: Manage certificate map entries \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:16.918682+00:00
---

# Manage certificate map entries  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/map-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage certificate map entries Stay organized with collections  Save and categorize content based on your preferences. 

A certificate map entry associates a certificate with a target hostname and a target [certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps). This page describes how to create and manage certificate map entries.

For more information, see [Certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/core-components#maps-entries).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [ Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a certificate map entry

You can create a certificate map entry and associate a maximum of four certificates with it. We recommend that you use a different key algorithm for each certificate when specifying multiple certificates for a hostname. For example, you can use ECDSA for one certificate and RSA for another. Associating multiple certificates with a single certificate map entry also helps when migrating self-managed certificates to Google-managed certificates.

For more information about how a load balancer selects certificates during a handshake, see [Certificate selection logic](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic#selection-logic).

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. For a [new certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps#create_a_certificate_map), click add_box**Create certificate map**.

For an [existing certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps#update_a_certificate_map), select the required certificate map from the list of certificate maps.

  3. On either the **Create certificate map** page or the **Edit certificate map** page, click add_box**Add map entry**. The **Add map entry** window opens.

  4. In the **Map entry name** field, enter a name for the certificate map entry, such as `my-cert-map-entry-01`.

  5. In the **Description** field, enter a description for the certificate map entry, such as `My new cert map entry`.

  6. To make the new certificate map entry the primary entry of your certificate map, select **Primary entry**. For more information, see [Create a primary certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create).

**Note** : You can associate only one primary certificate map entry with a certificate map.

  7. In the **Hostname** field, enter the hostname that you want to associate with the certificate map entry, such as `www.example.com`.

**Note** : For a primary certificate map entry, the hostname is specified as `<PRIMARY>` by default and you can't change its hostname.

  8. To associate a certificate with the certificate map entry, click **Select a certificate**. You can either select an existing certificate or click add_box**Add certificate** to [create a certificate](https://docs.cloud.google.com/certificate-manager/docs/certificates).

**Note** : You can associate a maximum of four certificates with a certificate map entry.

  9. To add a label and associate it with the certificate map entry, click add_box**Add label** and then enter a key and a value for your label.

  10. Click **Add**. The certificate map entry with its associated certificates is added to the certificate map.




###  gcloud 

To associate multiple certificates with a certificate map entry, provide a comma-delimited list of certificate names. For each subdomain, you must create a separate map entry.

To create a certificate map entry, use the [`gcloud certificate-manager maps entries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create):
    
    
    gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME" \
        --certificates="CERTIFICATE_NAMES" \
        --hostname="HOSTNAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_NAMES`: a comma-separated list of the names of the certificates that you want to associate with the certificate map entry
  * `HOSTNAME`: hostname that you want to associate with the certificate map entry



###  API 

To associate multiple certificates with a certificate map entry, provide a comma-delimited list of certificate names. For each subdomain, you must create a separate map entry.

To create a certificate map entry, make a `POST` request to the [`certificateMaps.certificateMapEntries.create` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/create):
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries?certificate_map_entry_id=CERTIFICATE_MAP_ENTRY_NAME
    {
     hostname: "HOSTNAME"
     certificates: ["projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME1","projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME2"]
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `HOSTNAME`: hostname that you want to associate with the certificate map entry
  * `CERTIFICATE_NAME1`: name of the first certificate that you want to associate with the certificate map entry
  * `CERTIFICATE_NAME2`: name of the second certificate that you want to associate with the certificate map entry



###  Terraform 

To create a certificate map entry, use a [`google_certificate_manager_certificate_map_entry` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map_entry).
    
    
    resource "google_certificate_manager_certificate_map_entry" "default" {
      name        = "${local.name}-first-entry-${random_id.tf_prefix.hex}"
      description = "example certificate map entry"
      map         = google_certificate_manager_certificate_map.default.name
      labels = {
        "terraform" : true
      }
      certificates = [google_certificate_manager_certificate.default.id]
      hostname     = local.domain
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Create a primary certificate map entry

You can specify a primary certificate map entry that a load balancer can serve if either the client doesn't provide a hostname or the load balancer isn't able to match the hostname to a configured certificate map entry.

**Note:** When using Certificate Manager with Identity-Aware Proxy (IAP), create a dedicated certificate map entry for each hostname. Primary certificate map entry is incompatible with IAP.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. For a [new certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps#create_a_certificate_map), click add_box**Create certificate map**.

For an [existing certificate map](https://docs.cloud.google.com/certificate-manager/docs/maps#update_a_certificate_map), select the required certificate map from the list of certificate maps.

  3. When adding a new certificate map entry, on the **Create certificate map** page, click add_box**Add map entry**.

To edit an existing certificate map entry, on the **Edit certificate map** page, under the **Actions** column of the map entry row, click the more_vert icon, and then select **Edit**.

  4. To make a certificate map entry the primary entry of your certificate map, in the **Add map entry** window, select **Primary entry**.

**Note** : You can associate only one primary certificate map entry with a certificate map.

  5. Click **Save**.




###  gcloud 

To create a primary certificate map entry, use the [`gcloud certificate-manager maps entries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create) with the `set-primary` flag:
    
    
    gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME" \
        --certificates="CERTIFICATE_NAMES" \
        --set-primary
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_NAMES`: a comma-separated list of the names of the certificates that you want to associate with the certificate map entry



###  API 

To create a certificate map entry, make a `POST` request to the [`certificateMaps.certificateMapEntries.create` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/create):
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries?certificate_map_entry_id=CERTIFICATE_MAP_ENTRY_NAME
    {
       matcher: "PRIMARY",
       certificates: ["projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME1","projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME2"]
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_NAME1`: name of the first certificate that you want to associate with the primary certificate map entry.
  * `CERTIFICATE_NAME2`: name of the second certificate that you want to associate with the primary certificate map entry.



For more information about how the load balancer selects certificates during a handshake, see [Certificate selection logic](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic#selection-logic).

## Update a certificate map entry

When you update an existing certificate map entry, you can do the following:

  * Assign or unassign certificates
  * Change the description
  * Change the labels



If you use the Google Cloud console to update a certificate map entry, then you can also do the following:

  * Change the name of a map entry.
  * If no other map entry is assigned as the primary entry, assign the map entry as the primary map entry of the certificate map.



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

  4. Under the **Actions** column of the map entry row, click the more_vert icon and then select **Edit**. The **Edit map entry** window opens.

  5. In the **Map entry name** field, change the name for the certificate map entry.

  6. In the **Description** field, change the description for the certificate map entry.

  7. To make the certificate map entry the primary entry of your certificate map, select **Primary entry**. For more information, see [Create a primary certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create).

**Note** : You can associate only one primary certificate map entry with a certificate map.

  8. In the **Hostname** field, change the hostname that you want to associate with the certificate map entry.

**Note** : For a primary certificate map entry, the hostname is specified as `<PRIMARY>` by default and you can't change its hostname.

  9. To associate a certificate with the certificate map entry, click **Select a certificate**. You can either select an existing certificate or click add_box**Add certificate** to [create a certificate](https://docs.cloud.google.com/certificate-manager/docs/certificates).

**Note** : You can associate a maximum of four certificates with a certificate map entry.

To move up or move down the order of a certificate, click either the arrow_upward icon or the arrow_downward icon for the required certificate.

To delete a certificate, click delete**Delete item** for the required certificate.

  10. To add a label and associate it with the certificate map entry, click add_box**Add label** and then enter a key and a value for your label.

To delete a label, click delete**Delete item** for the required label.

  11. Click **Save**.




###  gcloud 

To update a certificate map entry, use the [`gcloud certificate-manager maps entries update` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/update):
    
    
    gcloud certificate-manager maps entries update CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME" \
        --certificates="CERTIFICATE_NAME,CERTIFICATE_NAME" \
        --description="DESCRIPTION" \
        --update-labels="LABELS"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_NAME`: the name of the certificate you want to associate with the certificate map entry
  * `DESCRIPTION`: description for the certificate map entry
  * `LABELS`: list of labels applied to the certificate map entry



###  API 

To update the certificate map entry, make a `PATCH` request to the [`certificateMaps.certificateMapEntries.patch` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/patch):
    
    
    PATCH  /v1/projects/example-project/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries/CERTIFICATE_MAP_ENTRY_NAME?updateMask=labels,description,certificates
    {
      "certificates": ["projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME"],
      "description": "DESCRIPTION",
      "labels": { "LABEL_KEY": "LABEL_VALUE" }
    }
    
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_NAME`: the name of the certificate
  * `DESCRIPTION`: description for the certificate map entry
  * `LABEL_KEY`: a label key applied to the certificate map entry
  * `LABEL_VALUE`: a label value applied to the certificate map entry



## List certificate map entries

You can view, filter, and sort the list of all certificate map entries that you've associated with a certificate map.

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

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens with detailed information about the selected certificate map and its associated list of map entries.




###  gcloud 

To list the certificate map entries that are associated with a certificate map, use the [`gcloud certificate-manager maps entries list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/list)
    
    
    gcloud certificate-manager maps entries list --map=CERTIFICATE_MAP_NAME \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY"
    

Replace the following:

  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter the results by the following criteria:

    * Serving state: `--filter='state=ACTIVE'`
    * Matcher (set as primary): `--filter='-matcher=PRIMARY'`
    * Hostname: `--filter='hostname=example.com'`
    * Assigned certificates: `--filter='certificates:my-cert'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




###  API 

To list certificate map entries that are associated with a certificate map, make a `GET` request to the [`certificateMaps.certificateMapEntries.list` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/list):
    
    
    GET /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the target certificate map
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, you can filter the results by the following criteria:

    * Serving state: `--filter='state=ACTIVE'`
    * Matcher (set as primary): `--filter='-matcher=PRIMARY'`
    * Hostname: `--filter='hostname=example.com'`
    * Assigned certificates: `--filter='certificates:my-cert'`
    * Labels and creation time: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## View the state of a certificate map entry

You can view the details and state of a certificate map entry that's associated with a certificate map.

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

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens with detailed information about the selected certificate map and its associated list of map entries.

  3. In the **Map entries** section, click the name of the map entry that you want to view. The **Map entry details** page opens with detailed information about the selected map entry.




###  gcloud 

To view the state of a certificate map entry that's associated with a certificate map, use the [`gcloud certificate-manager maps entries describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/describe):
    
    
    gcloud certificate-manager maps entries describe CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated



The output is similar to the following:
    
    
    certificates:
    createTime: '2021-09-06T10:01:56.229472109Z'
    hostname: example.com
    name: projects/my-project/locations/global/certificateMaps/myCertMap/certificateMapEntries/myCertMapEntry
    state: ACTIVE
    updateTime: '2021-09-06T10:01:58.277031787Z'
    

###  API 

To view the state of a certificate map entry that's associated with a certificate map, make a `GET` request to the [`certificateMaps.certificateMapEntries.get` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/get):
    
    
    GET /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries/CERTIFICATE_MAP_ENTRY_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry



## Delete a certificate map entry

When you delete a certificate map entry, the certificates associated with the certificate map entry are detached from the target proxy. 

Deleting a certificate map entry doesn't delete the associated certificates from Google Cloud. You must [manually delete those certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates#delete-certificate).

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page and then click the **Certificate maps** tab.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificates)

  2. From the list of certificate maps, click the required certificate map. The **Certificate Map Details** page opens.

  3. Click edit**Edit**. The **Edit certificate map** page opens.

  4. Under the **Actions** column of the map entry row, click the more_vert icon, select delete**Delete** , and then click **Delete**.




###  gcloud 

To delete a certificate map entry that's associated with a certificate map, use the [`gcloud certificate-manager maps entries delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete):
    
    
    gcloud certificate-manager maps entries delete CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated



###  API 

To delete a certificate map entry that's associated with a certificate map, make a `DELETE` request to the [`certificateMaps.certificateMapEntries.delete` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries/delete):
    
    
    DELETE /v1/projects/PROJECT_ID/locations/global/certificateMaps/CERTIFICATE_MAP_NAME/certificateMapEntries/CERTIFICATE_MAP_ENTRY_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated
  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry



## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Manage certificate issuance configuration resources](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
