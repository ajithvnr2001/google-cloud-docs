---
url: https://docs.cloud.google.com/gemini/enterprise/docs/identity-mapping/
title: Map external identities \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:10.112209+00:00
---

# Map external identities  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/identity-mapping/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Map external identities Stay organized with collections  Save and categorize content based on your preferences. 

Enterprises typically manage identities (users and user groups) using an identity provider (IDP). But, custom applications that an enterprise has built in-house can allow customers to create new user groups that are defined locally within that application. These application-specific user groups or secondary user IDs are referred to as _external identities_.

## Why set up identity mapping?

To make sure that Google can enforce access control correctly, map your IDP identities to any external identities from the custom applications that you plan to use with Gemini Enterprise.

To apply access control to app results, Google uses the IDP as the source of truth to determine which data your users have access to. Enterprises often connect their IDP to other SaaS solutions so that an employee can use a single set of corporate credentials to sign into and access all company resources.

If you have external identities defined through applications that you plan to connect to your app such as custom applications, then your IDP isn't the only source of truth for access control.

For example, say that "JaneDoe" exists within Example Organization, with domain "example.com". The ID in the IDP is defined as "JaneDoe@example.com". The same user has a separate ID within a custom application as "JDoe". The IDP might not be aware of this ID. Because of this, Gemini Enterprise does not receive information about the custom application IDs through the IDP.

In Gemini Enterprise, identity mappings are stored in an _identity mapping store_ that you create and import the mappings into. If you plan to use a custom connector, you can bind the identity mapping store to the custom connector data store and then update your data store's ACL metadata with information about your external identities.

## Before you begin

Before you set up identity mapping, [connect your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider#connect_idp) to your Google Cloud project.

## Prepare identity mapping entries

Prepare the identity mapping entries for import. Identity mappings should be formatted as in the following example:
    
    
    {
      "identity_mapping_entries": [
        {
          "external_identity": "u1",
          "user_id": "user1@example.com"
        },
        {
          "external_identity": "u2",
          "user_id": "user2@example.com"
        },
        {
          "external_identity": "gABC",
          "group_id": "groupABC@example.com"
        }
      ]
    }
    

For example, the following chart represents an example user-group membership, where `Ext` represents external groups. This chart shows an example relationship between external groups to IDP users and groups.

![External identity relationship to IDP users and groups.](https://docs.cloud.google.com/gemini/enterprise/images/membership.png)

This user-group membership graph would have following mapping:
    
    
    {
      "identity_mapping_entries": [
        {
          "external_identity": "Ext1",
          "user_id": "IDPUser1@example.com"
        },
        {
          "external_identity": "Ext2",
          "user_id": "IDPUser1@example.com"
        },
        {
          "external_identity": "Ext2",
          "user_id": "IDPUser2@example.com"
        },
        {
          "external_identity": "Ext3",
          "user_id": "IDPUser2@example.com"
        },
        {
          "external_identity": "Ext3",
          "group_id": "IDPGroup1@example.com"
        },
        {
          "external_identity": "Ext3",
          "group_id": "IDPGroup2@example.com"
        }
      ]
    }
    

Nested identity memberships, where external identities have child identities, must be flattened.

Google assumes that the connector sends a primary ID for an external identity. For example, import the group ID instead of the group name, because the name could be changed over the lifetime of the group within the custom application.

## Set up identity mapping

Use the following procedures to set up identity mapping in Gemini Enterprise between your IDP and your external identities. In the following steps, you will create an identity mapping store, import the identity mappings that you prepared. If you plan to use a custom connector, you will also create a new data store that is bound to the identity mapping store.

### Create an identity mapping store

The first step is to set up an identity mapping store. This is the parent resource in which all identity mappings are stored.

When you create the identity mapping store, it automatically fetches the IDP configuration from the IDP that you connected to your Gemini Enterprise project.

  1. To create an identity mapping store, run the following command using the [`identityMappingStores.create`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/create) method:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores?identityMappingStoreId=IDENTITY_MAPPING_STORE_ID" \
         -d '{
           "name": "projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID for the identity mapping store. For example, `test-id-mapping-store`.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: example-project" \
    "https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores?identityMappingStoreId=test-id-mapping-store" \
    -d '{
      "name": "projects/example-project/locations/global/identityMappingStores/test-id-mapping-store"
    }'
    
    
    * * *
    
    
    {
      "name": "projects/12345/locations/global/identityMappingStores/test-id-mapping-store",
      "idpConfig": {
        "idpType": "GSUITE"
      }
    }
    




### Import identity mappings

After creating the identity mapping store, import the identity mapping entries that you prepared. You can import identity mappings using an inline source (Option 1) or from Cloud Storage (Option 2).

When importing from Cloud Storage, the following formats and constraints apply:

  * **Allowed formats** : The input files must be in NDJSON (`.ndjson`) or JSON Lines (`.jsonl`) format, with each line representing a single identity mapping entry.
  * **File size constraints** : Each file should not exceed 2 GB.
  * **Number of identity mappings constraints** : You can import up to `500,000` external identity mappings in an import operation.
  * **File count constraints** : You can specify up to `2,000` files in the `inputUris` list. If you use wildcards, the limit applies to the total number of files after wildcard expansion.



#### Option 1: Import using inline source

  1. To import your identity mappings using an inline source, run the following command using the [`importIdentityMappings`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/importIdentityMappings) method:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" -H "x-goog-user-project: PROJECT_ID" \
         "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/identityMappingStores/IDENTITY_MAPPING_STORE_ID:importIdentityMappings" \
         -d '{"inline_source" : IDENTITY_MAPPINGS_JSON}'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `IDENTITY_MAPPINGS_JSON`: the prepared identity mappings in JSON format.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" -H "x-goog-user-project: example-project" \
    "https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores/test-id-mapping-store:importIdentityMappings" \
    -d '{"inline_source" : { identity_mapping_entries: { external_identity: "external_id_1", user_id: "testuser1@example.com" } , identity_mapping_entries: { external_identity: "external_id_2", user_id: "testuser2@example.com" }, identity_mapping_entries: { external_identity: "external_id2", group_id: "testgroup1@example.com" } }}'
    
    
    * * *
    
    
    {
      "name": "projects/862721868538/locations/global/identityMappingStores/test-id-mapping-store/operations/import-identity-mappings-14869487418543288420",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata",
        "successCount": "2",
        "failureCount": "1",
        "totalCount": "3"
      },
      "done": true
    }
    

  2. If you plan to build a custom connector and use external identities, go to Bind custom data stores to the identity mapping store. Otherwise, skip to Update ACL metadata.




#### Option 2: Import from Cloud Storage

  1. To import your identity mappings from Cloud Storage, run the following command using the [`importIdentityMappings`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/importIdentityMappings) method:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" -H "x-goog-user-project: PROJECT_ID" \
         "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/identityMappingStores/IDENTITY_MAPPING_STORE_ID:importIdentityMappings" \
         -d '{
           "gcsSource": {
             "inputUris": ["gs://BUCKET_NAME/FILE_PATH"]
           },
           "errorConfig": {
             "gcsPrefix": "gs://BUCKET_NAME/ERROR_DIR"
           },
           "reconciliationMode": "FULL"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `FILE_PATH`: the path to your identity mappings file in Cloud Storage.
     * `ERROR_DIR`: the directory in Cloud Storage where error logs will be stored.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" -H "x-goog-user-project: example-project" \
    "https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores/test-id-mapping-store:importIdentityMappings" \
    -d '{
      "gcsSource": {
        "inputUris": ["gs://example-bucket/identity_mappings.json"]
      },
      "errorConfig": {
        "gcsPrefix": "gs://example-bucket/errors"
      },
      "reconciliationMode": "FULL"
    }'
    
    
    * * *
    
    
    {
      "name": "projects/12345/locations/global/identityMappingStores/test-id-mapping-store/operations/import-identity-mappings-14869487418543288420",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata",
        "successCount": "2",
        "failureCount": "1",
        "totalCount": "3"
      },
      "done": true
    }
    

  2. If you plan to build a custom connector and use external identities, go to Bind custom data stores to the identity mapping store. Otherwise, skip to Update ACL metadata.




### Bind custom data stores to the identity mapping store

This procedure is only necessary if you build a custom connector. If you are not building a custom connector, skip this step.

For custom connectors, the identity mapping store needs to be bound to the data store before an external identity can be associated with its documents. Setting this field is allowed only during data store creation.

  1. To bind a data store to the identity mapping store, specify `identity_mapping_store` during data store creation using the [`Datastores.create`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores/create) method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json"  \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID \
         -d '{
             ...
             "identity_mapping_store": "IDENTITY_MAPPING_STORE_NAME"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of the data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `IDENTITY_MAPPING_STORE_NAME`: the full resource name of the identity mapping store. For example, `projects/exampleproject/locations/global/identityMappingStores/test-id-mapping-store`. After creating a data store, this name can't be updated.



### Add ACL metadata

Include ACL metadata in the [`AclInfo`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#aclinfo) object for your documents.

When a user sends a search request and documents whose ACL metadata include external identities are fetched, then those external identities are evaluated. If the user's identity (`groupID` or `userID`) is mapped to an external identity (`externalEntityId`) that is associated with a document, then the user gets access to that document.

For example, say that you have created a custom connector for Jira. A given Jira issue is accessible by certain IDP users, certain IDP groups, and an administrator role. To allow that issue to be accessible by those people in search results, you can create an identity mapping store and map IDP users and groups to Jira-specific external identities. Bind the identity mapping store to your Jira data store. Then, create documents in your Jira data stores with `aclInfo` configured with the IDP users, IDP groups, and external identities who should have access to those documents.

To update your ACL metadata with information about your external identities, use the following format to specify the external identities and associated user and group IDs.
    
    
    {
      "aclInfo": {
        "readers": [
          {
            "principals": [
              {
                "groupId": "group_1"
              },
              {
                "userId": "user_1"
              },
              {
                "externalEntityId": "external_id1"
              }
    
            ]
          }
        ]
      }
    }
    

For more information about updating ACL metadata, see [Configure a data source with access control](https://docs.cloud.google.com/gemini/enterprise/docs/identity#configure-data-source).

## Manage identity mappings

You can list identity mappings in an identity store, or you can purge an identity store by defining them through an inline source or by using a filter condition.

Management tasks available for identity mapping are:

  * List identity mappings
  * Purge using inline source
  * Purge using a filter condition



### List identity mappings

  1. To list identity mappings, run the following command using the [`listIdentityMappings`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/listIdentityMappings) method:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H  "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID:listIdentityMappings?page_size=PAGE_SIZE&page_token=PAGE_TOKEN"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `PAGE_SIZE`: maximum number of identity mapping stores to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values higher than 1000 will be coerced to 1000.
     * `PAGE_TOKEN`: a page token, received from a previous `ListIdentityMappingStores` call. Provide this to retrieve the subsequent page.

#### Example command and result
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H  "Content-Type: application/json" \
    -H "x-goog-user-project: example-project" \
    https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores/test-id-mapping-store:listIdentityMappings
    
    
    * * *
    
    
    {
      "identityMappingEntries": [
        {
          "externalIdentity": "external_group2",
          "groupId": "example-group@google.com"
        },
        {
          "externalIdentity": "external_id_1",
          "userId": "example-user@google.com"
        }
      ],
      "nextPageToken": "gNiNWOiRTMxEWMwATLmNDMh1CO0IjMtADMwATLkRWYkZTZ3YDJawB2h-LEG8ro3XLCLIBZ2YmNz"
    }
    




### Purge using inline source

You can purge specified entries from an identity mapping store by providing a JSON file of which identities to purge.

  1. To purge identity mappings using inline source, run the following command using the [`purgeIdentityMappings`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/purgeIdentityMappings) method:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID:purgeIdentityMappings" \
         -d '{"inline_source" : IDENTITY_MAPPINGS_JSON}'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `IDENTITY_MAPPING_STORE_NAME`: the identity mapping store name.
     * `IDENTITY_MAPPINGS_JSON`: the identity mappings to be purged.



### Purge using a filter condition

You can purge specified entries from an identity mapping store by filtering for entries by update time, external identity, or all entries.

  1. To purge identity mappings using a filter condition, run the following command using the [`purgeIdentityMappings`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/purgeIdentityMappings) method:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID:purgeIdentityMappings" \
         -d '{"identity_mapping_store":"IDENTITY_MAPPING_STORE_NAME", "filter": "FILTER_CONDITION"}'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `IDENTITY_MAPPING_STORE_NAME`: the identity mapping store name.
     * `FILTER_CONDITION`: one of the following filter types:
       * Update time. For example, `update_time > "2012-04-23T18:25:43.511Z" AND update_time < "2012-04-23T18:30:43.511Z">`
       * External Identity. For example, `external_id = "id1"`
       * All identity mappings. For example, `*`

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "x-goog-user-project: ucs-ga-fishfood-1" \
    "https://discoveryengine.googleapis.com/v1/projects/ucs-ga-fishfood-1/locations/global/identityMappingStores/test-id-mapping-store:purgeIdentityMappings" \
    -d '{"identity_mapping_store":"test-id-mapping-store", "filter": "*"}'
    
    
    * * *
    
    
    {
      "name": "projects/12345/locations/global/identityMappingStores/test-id-mapping-store/operations/purge-identity-mappings-200445172458892000",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata"
      }
    }
    




## Manage identity mapping stores

You can get, delete, list, and purge identity mapping stores.

### Get identity mapping store

  1. To get an identity mapping store, run the following command using the [`identityMappingStores.get`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/get) method:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `IDENTITY_MAPPING_STORE_NAME`: the identity mapping store name.

#### Example command and result
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: example-project" \
    "https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores/test-id-mapping-store"
    
    
    * * *
    
    
    {
      "name": "projects/12345/locations/global/identityMappingStores/test-id-mapping-store",
      "idpConfig": {
        "idpType": "GSUITE"
      }
    }
    




### List identity mapping stores

  1. To list identity mapping stores, run the following command using the [`identityMappingStores.list`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/list) method:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H  "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores?page_size=PAGE_SIZE&page_token=PAGE_TOKEN"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `PAGE_SIZE`: maximum number of identity mapping stores to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values higher than 1000 will be coerced to 1000.
     * `PAGE_TOKEN`: a page token, received from a previous `ListIdentityMappingStores` call. Provide this to retrieve the subsequent page.

#### Example command and result
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H  "Content-Type: application/json" \
    -H "x-goog-user-project: ucs-ga-fishfood-1" \
    "https://discoveryengine.googleapis.com/v1/projects/example-project/locations/global/identityMappingStores"
    
    
    * * *
    
    
    {
      "identityMappingStores": [
        {
          "name": "projects/12345/locations/global/identityMappingStores/test-id-mapping-store",
          "idpConfig": {
            "idpType": "GSUITE"
          }
        }
      ]
    }
    




### Delete identity mapping stores

To delete an identity mapping store, it must not be bound to a data store, and no identity mappings can be present in the identity mapping store.

  1. To delete an identity mapping store, run the following command using the [`identityMappingStores.delete`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/delete) method:
         
         curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/identityMappingStores/IDENTITY_MAPPING_STORE_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `IDENTITY_MAPPING_STORE_ID`: the unique ID of the identity mapping store.
     * `IDENTITY_MAPPING_STORE_NAME`: the identity mapping store name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
