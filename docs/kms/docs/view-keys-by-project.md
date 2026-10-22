---
url: https://docs.cloud.google.com/kms/docs/view-keys-by-project/
title: View keys by project \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:29.099885+00:00
---

# View keys by project  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/view-keys-by-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  View keys by project Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to view key rings and keys in your Google Cloud [project resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).

## Before you begin

Before you can view key rings and keys, complete the setup steps described in this section.

### Enable APIs

To view key rings and keys using an API, enable the Cloud KMS Inventory API. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=kmsinventory.googleapis.com)

### Required roles

To get the permissions that you need to view keys, ask your administrator to grant you the [Cloud KMS Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.viewer) (`roles/cloudkms.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view keys. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view keys:

  * `cloudkms.keyRings.list`
  * `cloudkms.cryptoKeys.list`
  * `cloudkms.locations.list`
  * `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View key rings

###  Console 

  1. In the Google Cloud console, go to the **Key rings** page.

[Go to Key rings](https://console.cloud.google.com/security/kms/keyrings)

  2. Optional: To filter your list of key rings, enter your search terms in the filter_list **Filter** box and then press Enter.

  3. Optional: To sort the list by the values in a column, click the column heading.




While viewing your key rings, you can select a key ring to view details about the associated keys and import jobs.

## View keys

Use the Google Cloud console to view the keys created in your project resource.

###  Console 

  1. In the Google Cloud console, go to the **Key inventory** page.

[Go to Key inventory](https://console.cloud.google.com/security/kms/keys)

  2. Optional: To filter your list of keys, enter your search terms in the filter_list **Filter** box and then press Enter.

  3. Optional: To sort the list by the values in a column, click the column heading.




###  gcloud 

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms inventory list-keys --project PROJECT_ID
    

Replace `PROJECT_ID` with the name of the project for which you want to view the list of keys.

For information on all flags and possible values, run the command with the `--help` flag.

###  REST 

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 
    
    
    curl "https://kmsinventory.googleapis.com/v1/projects/PROJECT_ID/cryptoKeys"
        --request "GET" \
        --header "x-goog-user-project: CALLING_PROJECT_ID"
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer TOKEN"

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `CALLING_PROJECT_ID`: the ID of the project from which you are calling the KMS Inventory API.



This method returns up to 1,000 keys. To see fewer results, you can specify the `pageSize` query parameter. To get the next page of results, you can specify the `pageToken` parameter. Pages after the first can take longer to load. For more information, see [Method: projects.cryptoKeys.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list).

While viewing your keys, you can select a key to view details about the key, including its associated key versions.

### Key details

The key inventory provides comprehensive information about the cryptographic keys in your project. Properties in the key inventory include the following:

  * **Key name** : The name of the key.
  * **Status** : The current key status based on the [state](https://docs.cloud.google.com/kms/docs/key-states) of the primary key version. This field applies to symmetric keys only. 
    * **Available** : The primary key version is enabled. The key is available for use to encrypt and decrypt data.
    * **Not available** : The primary key version is disabled or empty. The key isn't available for use to encrypt data.
    * **Available in GCP** : For externally managed keys, the key (not necessarily the externally managed key itself) is available for use.
  * **Key ring** : Name of the parent key ring.
  * **Location** : Location where key material resides.
  * **Current rotation** : The date and time the key was last rotated. This field shows when the current key version was created.
  * **Rotation frequency** : The current rotation frequency of the key.
  * **Next rotation** : The date of the next scheduled key rotation. A new key version will be created automatically on this date.
  * **Protection level** : The [protection level](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) of the key, for example, HSM or Software.
  * **EKM via VPC connection** : For external keys accessed over VPC, the name of the [EKM via VPC connection](https://docs.cloud.google.com/kms/docs/create-ekm-connection#terminology) that the key uses. This field is hidden by default and is blank for keys with protection levels other than `External via VPC`.
  * **Purpose** : The scenario in which the key may be used.
  * **Labels** : Labels applied on the key.



## Limitations

  * The **Key ring** tab can display at most 1,000 resources (including key rings, keys, and key versions) per [location](https://docs.cloud.google.com/kms/docs/locations). To view key rings for a project and location with more than 1,000 resources, use the [keyRings.list method](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list) in the Cloud KMS API.

  * The **Key inventory** tab can display at most 50,000 resources (including key rings, keys, and key versions) per project. To view keys for a project with more than 50,000 resources, use the [keyRings.cryptoKeys.list method](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list) in the Cloud KMS API or the [projects.cryptoKeys.list method](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys/list) in the Cloud Key Management Service Inventory API.

  * When you use the [keyRings.cryptoKeys.list method](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list) in the Cloud KMS API or the [projects.cryptoKeys.list method](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys/list) in the Cloud Key Management Service Inventory API in projects with more than 1,000 keys, subsequent pages can take longer to load than the first.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
