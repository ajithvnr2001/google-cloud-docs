---
url: https://docs.cloud.google.com/certificate-manager/docs/issuance-configs/
title: Manage certificate issuance configuration resources \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:18.015377+00:00
---

# Manage certificate issuance configuration resources  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/issuance-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage certificate issuance configuration resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage a certificate issuance configuration resource.

For more information about certificate issuance configuration resources, see [Certificate issuance configs](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#issuance-configs).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [ Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed. For more information about the gcloud CLI commands used on this page, see the [Certificate Manager CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager).

## Create a certificate issuance configuration resource

Before you create the issuance configuration resource, [configure CA Service integration with Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas#configure-integration).

To create a certificate issuance configuration resource, specify the certificate's lifetime, rotation window percentage, key algorithm, and the CA pool to use.

Even though you use a regional CA pool to issue a Google-managed TLS certificate, the certificate can be used globally.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Issuance configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificateIssuanceConfigs)

  2. Click **Create**. The **Create a Certificate Issuance Config** page appears.

  3. In the **Name** field, enter a unique name for the certificate issuance configuration resource.

  4. Optional: In the **Description** field, enter a description for the issuance configuration.

  5. For **Location** , select **Global** or **Regional**. If you selected **Regional** , select the same **Region** as your certificate and CA pool.

  6. In the **Lifetime** field, specify the lifetime of issued certificate in days. The value must be between 21 to 30 days (inclusive).

  7. For **Rotation window percentage** , specify the percentage of the certificate's lifetime when its renewal process begins. To find the range of valid values, see Lifetime and rotation window percentage.

  8. From the **Key algorithm** list, select the key algorithm to use when generating the private key.

  9. From the **CA pool** list, select the name of the CA pool to assign to this certificate issuance configuration resource.

  10. In the **Labels** field, specify labels to associate to the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  11. Click **Create**.




###  gcloud 

To create a certificate issuance configuration resource, use the [`certificate-manager issuance-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create):
    
    
    gcloud certificate-manager issuance-configs create ISSUANCE_CONFIG_NAME \
        --ca-pool=CA_POOL \
        --lifetime=CERTIFICATE_LIFETIME \
        --rotation-window-percentage=ROTATION_WINDOW_PERCENTAGE \
        --key-algorithm=KEY_ALGORITHM
        [--location=LOCATION]
    

Replace the following:

  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `CA_POOL`: the full resource path and name of the CA pool that you want to assign to the certificate issuance configuration resource in this format: `projects/PROJECT_ID/locations/LOCATION/caPools/CA_POOL_ID`. The project and location of the CA pool can be different from the project and location of the certificate issuance configuration.
  * `CERTIFICATE_LIFETIME`: the certificate lifetime in days. Valid values are from 21 to 30 days in the [ISO 8601 duration format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes); for example, `P30D`. The default value is 30 days (`P30D`). This flag is optional.
  * `ROTATION_WINDOW_PERCENTAGE`: the percentage of the certificate's remaining lifetime before renewal. The default value is 66%. To find the range of valid values, see Lifetime and rotation window percentage. This flag is optional.
  * `KEY_ALGORITHM`: the encryption algorithm that you can use to generate the private key. Valid values are `ecdsa-p256` or `rsa-2048`. The default value is `rsa-2048`. This flag is optional.
  * `LOCATION`: the target Google Cloud location.



###  API 

Create the certificate issuance configuration resource by making a `POST` request to the `certificateIssuanceConfigs.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/certificateIssuanceConfigs?issuanceConfig_id=ISSUANCE_CONFIG_NAME
    {
      "description": "DESCRIPTION",
      "certificateAuthorityConfig": {
        "certificateAuthorityServiceConfig": {
          "caPool": "CA_POOL"
        }
      },
      "lifetime": "CERTIFICATE_LIFETIME",
      "rotationWindowPercentage": ROTATION_WINDOW_PERCENTAGE,
      "keyAlgorithm": "KEY_ALGORITHM"
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `DESCRIPTION`: a meaningful description for the certificate issuance configuration resource.
  * `CA_POOL`: the full resource path and name of the CA pool that you want to assign to the certificate issuance configuration resource in this format: `projects/PROJECT_ID/locations/LOCATION/caPools/CA_POOL_ID`. The project and location of the CA pool can be different from the project and location of the certificate issuance configuration.
  * `CERTIFICATE_LIFETIME`: the certificate lifetime in seconds ending with `s`; for example, `2592000s` for 30 days. Valid values are from 21 to 30 days (`1814400s` to `2592000s`).
  * `ROTATION_WINDOW_PERCENTAGE`: the percentage of the certificate's remaining lifetime before renewal. To find the range of valid values, see Lifetime and rotation window percentage.
  * `KEY_ALGORITHM`: the encryption algorithm that you can use to generate the private key. Valid values are `ECDSA_P256` or `RSA_2048`.



### Lifetime and rotation window percentage

When you create a certificate issuance configuration resource, you also define the certificate's lifetime in the **Lifetime** field, and when the certificate's renewal process begins before it expires in the **Rotation window percentage** field.

To make sure that the certificate renews at least seven days before its expiry and seven days after its issuance, set the rotation window percentage relative to the certificate's lifetime. To calculate the allowed range for the rotation window percentage, use the following formulas:

  * Minimum value: Rotation window percentage ≥ (7 / Lifetime) * 100
  * Maximum value: Rotation window percentage ≤ ( (Lifetime - 7) / Lifetime) * 100



In the previous formulas, `7` is seven days.

If the minimum value is a decimal value, round it _up_ to the nearest whole number. If the maximum value is a decimal value, round it _down_ to the nearest whole number.

## Update a certificate issuance configuration

When you update a certificate issuance configuration, you can do the following:

  * Specify new labels
  * Specify a new description



#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  gcloud 

To update a certificate issuance configuration resource, use the [`certificate-manager issuance-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/update):
    
    
    gcloud certificate-manager issuance-configs update ISSUANCE_CONFIG_NAME
        [--update-labels="LABELS"] \
        [--description="DESCRIPTION"]
    

Replace the following:

  * `ISSUANCE_CONFIG_NAME`: the name of the target certificate issuance configuration that you want to update.
  * `LABELS`: labels that you want to specify for the certificate issuance configuration. Labels must be specified in a comma-delimited list as `KEY=VALUE` pairs. This field is optional.
  * `DESCRIPTION`: the description of the certificate issuance configuration. This field is optional.



###  API 

Use the [`certificateIssuanceConfigs.patch`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateIssuanceConfigs/patch) method to update a certificate issuance configuration:
    
    
    PATCH /v1/projects/PROJECT_ID/locations/global/certificateIssuanceConfigs/ISSUANCE_CONFIG_NAME?updateMask=labels,description
    {
      labels: { "LABEL_KEY": "LABEL_VALUE" },
      description: "DESCRIPTION"
    }
    
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `ISSUANCE_CONFIG_NAME`: the name of the target certificate issuance configuration that you want to update.
  * `LABEL_KEY`: the label key. This field is optional.
  * `LABEL_VALUE`: the value of the label. This field is optional.
  * `DESCRIPTION`: the certificate issuance configuration.



## List certificate issuance configurations

You can see all certificate issuance configuration resources of your project and their details.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)
  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Issuance configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificateIssuanceConfigs)

On the **Issuance configs** tab, all certificate issuance configuration resources managed by Certificate Manager in the selected project are displayed.




###  gcloud 

To list certificate issuance configuration resources, use the [`certificate-manager issuance-configs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/list):
    
    
    gcloud certificate-manager issuance-configs list \
        --filter="FILTER" \
        --page-size="PAGE_SIZE" \
        --limit="LIMIT" \
        --sort-by="SORT_BY" \
        [--location=LOCATION]
    

Replace the following:

  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `LIMIT`: maximum number of results that you want to return

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).

  * `LOCATION`: the target Google Cloud location.




###  API 

List configured certificate issuance configuration resources by making a `LIST` request to the `certificateIssuanceConfigs.list` method as follows:
    
    
    GET /v1/projects/PROJECT_ID/locations/global/certificateIssuanceConfigs?filter=FILTER&pageSize=PAGE_SIZE&sortBy=SORT_BY
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `FILTER`: an expression that constrains the returned results to specific values.

For example, to filter results by the labels and creation time, you can specify: `--filter='labels.key:value AND create_time > "2021-09-01T00:00:00Z"'`

For more filtering examples that you can use with Certificate Manager, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering) in the Cloud Key Management Service documentation.

  * `PAGE_SIZE`: number of results that you want to return per page

  * `SORT_BY`: a comma-separated list of `name` fields by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the field with a tilde (`~`).




## View the state of a certificate issuance configuration resource

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Viewer role (`roles/certificatemanager.viewer`)
  * Certificate Manager Editor role (`roles/certificatemanager.editor`)
  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Issuance configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificateIssuanceConfigs)

  2. Click the name of the certificate issuance configuration resource that you want to view. The **Certificate Issuance Config** page displays detailed information about the certificate issuance configuration resource.




###  gcloud 

To view the state of a certificate issuance configuration resource, use the [`certificate-manager issuance-configs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/describe):
    
    
    gcloud certificate-manager issuance-configs describe ISSUANCE_CONFIG_NAME
    

Replace `ISSUANCE_CONFIG_NAME` with the name of the certificate issuance configuration resource that references the target CA pool.

###  API 

View the state of the certificate issuance configuration resource by making a `GET` request to the `certificateIssuanceConfigs.get` method as follows:
    
    
      GET /v1/projects/PROJECT_ID/locations/global/certificateIssuanceConfigs/ISSUANCE_CONFIG_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.



## Delete a certificate issuance configuration resource

Before deleting a certificate issuance configuration resource, you must first [delete the Google-managed certificate that references it](https://docs.cloud.google.com/certificate-manager/docs/certificates#delete-certificate).

To disable the last CA that you enabled within a CA pool referenced in the certificate issuance configuration resource, or to delete the CA pool entirely, you must first delete all certificate issuance configuration resources that reference the CA pool.

#### Roles required for this task

To perform this task, you must have one of the following IAM roles on the target Google Cloud project.

  * Certificate Manager Owner role (`roles/certificatemanager.owner`)



For more information, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

**Note:** If you aren't assigned the required roles, contact the IAM Administrator who has the [Project IAM Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles. 

###  Console 

  1. In the Google Cloud console, go to the **Issuance configs** tab on the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list/certificateIssuanceConfigs)

  2. Select the checkbox of the issuance configuration that you want to delete.

  3. Click **Delete**.

  4. In the dialog that appears, click **Delete** to confirm.




###  gcloud 

To delete a certificate issuance configuration resource, use the [`certificate-manager issuance-configs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/delete):
    
    
    gcloud certificate-manager issuance-configs delete ISSUANCE_CONFIG_NAME
        [--location=LOCATION]
    

Replace the following:

  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.
  * `LOCATION`: the target Google Cloud location.



###  API 

Delete the certificate issuance configuration resource by making a `DELETE` request to the `certificateIssuanceConfigs.delete` method as follows:
    
    
      DELETE /v1/projects/PROJECT_ID/locations/global/certificateIssuanceConfigs/ISSUANCE_CONFIG_NAME
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `ISSUANCE_CONFIG_NAME`: the name of the certificate issuance configuration resource that references the target CA pool.



## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)
  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
