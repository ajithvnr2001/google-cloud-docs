---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-creating/
title: Creating and updating user consents \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:54.515019+00:00
---

# Creating and updating user consents  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-creating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and updating user consents Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, update, and revoke user consents.

Your application records the consent artifacts and consents separately. The Consent Management API stores sensitive data pertaining to a user's consent as a [`ConsentArtifact`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consentArtifacts). A `ConsentArtifact` can include signature timestamps and images of signatures or other documents that act as "proof" of consent.

The Consent Management API stores non-sensitive consent data as [`Consent`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents) objects. A `Consent` includes an opaque user ID, the consent policies granted by the user, and the status of the consent policies.

Because consents and consent artifacts have distinct resource paths, their permissions can be set independently to minimize access to sensitive consent data in consent artifacts.

Consents support an expiration duration that enables you to configure when a consent expires and is no longer valid. The expiration duration can be set to a specific date or a time period, such as one year.

During consent store creation, you can configure a default expiration duration for the consent store. During consent creation, you can configure an expiration duration for the consent. The expiration duration set during consent creation overrides the default duration set for the consent store.

Consents can be created in either `ACTIVE` or `DRAFT` states. Consents in the `ACTIVE` state are used by the Consent Management API to make access determinations. Consents in the `DRAFT` state are only used in access determinations if specified in an access determination request. You can change the state from `DRAFT` to `ACTIVE` or `REJECTED` by updating the consent.

To record a user consent, create a consent artifact using the [`projects.locations.datasets.consentStores.consentArtifacts.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consentArtifacts/create) method and then link the consent artifact to a consent created using the [`projects.locations.datasets.consentStores.consents.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/create) method.

The samples in this page assume that you have [created a consent store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-managing#creating_a_consent_store) and [configured consent policies](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-policies).

## Creating a consent artifact

A consent artifact stores sensitive data pertaining to a user's consent. A consent artifact can include a user's contact information, signature timestamps, and images of signatures or other documents that act as "proof" of consent.

To create a consent artifact, use the [`projects.locations.datasets.consentStores.consentArtifacts.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consentArtifacts/create) method. Make a `POST` request and specify the following information in the request:

  * The name of the parent consent store.
  * A unique and opaque user ID that represents the user who provided the consent.
  * The user's signature, optionally including the signature image, timestamp, and other metadata. This image can be specified as an image location in Cloud Storage or as a string of raw bytes.
  * An optional guardian or witness signature.
  * Optional images or documents acting as "proof" of consent, such as a signature image, images capturing the screens of a mobile consent flow, or a signed PDF document. These images can be specified as a location in Cloud Storage or as a string of raw bytes.
  * An identifier for the consent information that the user was shown.
  * Optional metadata related to the user's consent.
  * An access token.



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'user_id': 'USER_ID',
           'user_signature' : {
             'user_id': 'USER_ID',
             'image': {
               'gcs_uri': 'gs://IMG_URI' },
             'signature_time': {
               'seconds': EPOCH_SECONDS },
          },
           'consent_content_screenshots': [
             { 'raw_bytes': 'BASE_64_IMAGE' }],
           'consent_content_version': 'v1',
           'metadata': {'client': 'mobile'}
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_RESOURCE_ID",
      "userId": "USER_ID",
      "userSignature": {
        "userId": "USER_ID",
        "signatureTime": "SIGNATURE_TIME"
      },
      "consentContentVersion": "v1",
      "metadata": {
        "client": "mobile"
      }
    }
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'user_id': 'USER_ID',
           'user_signature' : {
             'user_id': 'USER_ID',
             'image': {
               'gcs_uri': 'gs://IMG_URI' },
             'signature_time': {
               'seconds': EPOCH_SECONDS }
          },
           'consent_content_screenshots': [
             { 'raw_bytes': 'BASE_64_IMAGE' }],
           'consent_content_version': 'v1',
           'metadata': {'client': 'mobile'}
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts" | Select-Object -Expand Content

If the request is successful, the server returns the following response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_RESOURCE_ID",
      "userId": "USER_ID",
      "userSignature": {
        "userId": "USER_ID",
        "signatureTime": "SIGNATURE_TIME"
      },
      "consentContentVersion": "v1",
      "metadata": {
        "client": "mobile"
      }
    }
    

## Creating a consent

A consent stores non-sensitive data, including opaque user IDs, the consent policies granted by the users, and whether the consent policies are currently valid.

To create a consent, use the [`projects.locations.datasets.consentStores.consents.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/create) method. Make a `POST` request and specify the following information in the request:

  * The name of the parent consent store.
  * A unique and opaque user ID that represents the user who provided the consent.
  * Up to 10 consent policies, each with a set of `RESOURCE` attribute values and an authorization rule expressed in [Common Expression Language](https://github.com/google/cel-spec/blob/master/doc/intro.md) (CEL) that describe the user's intent with previously created attribute definitions. The following restrictions to the CEL apply: 
    * You can only define a maximum of 10 logic operators per policy.
    * You can only use AND (&&), OR (||), and IN operators.
  * The REST path to the corresponding consent artifact (returned upon creation of the consent artifact).
  * An optional consent state, either `DRAFT` or `ACTIVE`. If you do not specify the state, the consent is created in the `ACTIVE` state.
  * An optional expiration duration for the consent, defined as either a date or a time period. This value must be provided in seconds and suffixed with the letter s. For example, `86000s`. This value overrides the expiration duration configured for the consent store. If you don't configure an expiration, the resource inherits the default expiration duration from the consent store. If an expiration duration isn't specified for either the resource or the store, the consent resource doesn't expire.
  * An access token.



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           \"user_id\": \"USER_ID\",
           \"policies\": [{
             \"resource_attributes\": [{
               \"attribute_definition_id\": \"data_identifiable\",
               \"values\": [\"identifiable\"]
             }],
             \"authorization_rule\": {
               \"expression\": \"requester_identity == 'clinical-admin'\",
            }
           },
           {
             \"resource_attributes\": [{
               \"attribute_definition_id\": \"data_identifiable\",
               \"values\": [\"de-identified\"]
             }],
             \"authorization_rule\": {
               \"expression\": \"requester_identity in ['internal-researcher', 'external-researcher']\"
              }
           }],
           \"consent_artifact\": \"projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID\",
           \"ttl\": \"EXPIRATION_DURATION\"
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents"

If the request is successful, the server returns a response similar to the following sample:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "CONSENT_STATE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'user_id': 'USER_ID',
           'policies': [{
             'resource_attributes': [{
               'attribute_definition_id': 'data_identifiable',
               'values': ['identifiable']
             }],
             'authorization_rule': {
               'expression': 'requester_identity == \'clinical-admin\'',
            }
           },{
             'resource_attributes': [{
               'attribute_definition_id': 'data_identifiable',
               'values': ['de-identified']
             }],
             'authorization_rule': {
               'expression': 'requester_identity in [\'internal-researcher\', \'external-researcher\']'
              }
           }],
           'consent_artifact': 'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID',
           'ttl': 'EXPIRATION_DURATION'
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "CONSENT_STATE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

## Getting a consent

The following samples show how to get a consent. For more information, see [`projects.locations.datasets.consentStores.consents.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/get).

To get a consent, make a `GET` request and specify the following information in the request:

  * The name of the parent dataset
  * The name of the consent store
  * The name of the consent
  * An access token



### curl

The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "CONSENT_STATE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "revisionCreateTime": "REVISION_CREATE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### PowerShell

The following sample shows a `GET` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID" | ConvertTo-Json

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": "",
          "authorizationRule": "@{expression=requester_identity == 'clinical-admin'}"
        },
        {
          "resourceAttributes": "",
          "authorizationRule": "@{expression=requester_identity in ['internal-researcher', 'external-researcher']}"
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "CONSENT_STATE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "revisionCreateTime": "REVISION_CREATE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

## Listing the consents in a consent store

The following samples show how to list the consents in a consent store.

To list the consents in a consent store, use the [`projects.locations.datasets.consentStores.consents.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/list) method.

### curl

To list the consents in a consent store, make a `GET` request and specify the following information:

  * The name of the parent consent store
  * An optional search filter to retrieve consents based on user ID, state, creation time, or consent artifact
  * An access token



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "consents": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
          "userId": "USER_ID",
          "policies": [
            {
              "resourceAttributes": [
                {
                  "attributeDefinitionId": "data_identifiable",
                  "values": [
                    "identifiable"
                  ]
                }
              ],
              "authorizationRule": {
                "expression": "requester_identity == 'clinical-admin'"
              }
            },
            {
              "resourceAttributes": [
                {
                  "attributeDefinitionId": "data_identifiable",
                  "values": [
                    "de-identified"
                  ]
                }
              ],
              "authorizationRule": {
                "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
              }
            }
          ],
          "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
          "state": "CONSENT_STATE",
          "stateChangeTime": "STATE_CHANGE_TIME",
          "revisionCreateTime": "REVISION_CREATE_TIME",
          "expireTime": "EXPIRE_TIME"
        },
        {
          ...
        }
      ]
    }
    

### PowerShell

To list the consents in a consent store, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * An optional search filter to retrieve consents based on user ID, state, creation time, or consent artifact
  * An access token



The following sample shows a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "consents": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
          "userId": "USER_ID",
          "policies": [
            {
              "resourceAttributes": [
                {
                  "attributeDefinitionId": "data_identifiable",
                  "values": [
                    "identifiable"
                  ]
                }
              ],
              "authorizationRule": {
                "expression": "requester_identity == 'clinical-admin'"
              }
            },
            {
              "resourceAttributes": [
                {
                  "attributeDefinitionId": "data_identifiable",
                  "values": [
                    "de-identified"
                  ]
                }
              ],
              "authorizationRule": {
                "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
              }
            }
          ],
          "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
          "state": "CONSENT_STATE",
          "stateChangeTime": "STATE_CHANGE_TIME",
          "revisionCreateTime": "REVISION_CREATE_TIME",
          "expireTime": "EXPIRE_TIME"
        },
        {
          ...
        }
      ]
    }
    

You can also list the revisions of a specific consent by using the [`projects.locations.datasets.consentStores.consents.listRevisions`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/listRevisions) method.

## Updating consents

You might need to update the state of consents over time. You can do this by changing the consent state. Every update and change of state generates a new revision of the consent. Previous revisions are accessible by appending `@{revision_id}` to the consent's resource name.

### Updating consents

To update an active or draft consent's `userId`, `policies`, `consentArtifact`, or `revokeConsentArtifact` fields, use the [`projects.locations.datasets.consentStores.consents.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/patch) method. A new revision is committed with the changes and set to the current state.

To update a consent, make a `PATCH` request and specify the following information in the request:

  * The REST path of the consent to update
  * The fields to update
  * An update mask
  * An access token



### curl

The following sample shows a `PATCH` request using `curl` that updates the consent artifact:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           \"consentArtifact\": \"projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID\"
           }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID?updateMask=consentArtifact"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "ACTIVE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "revisionCreateTime": "REVISION_CREATE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### PowerShell

The following sample shows a `PATCH` request using Windows PowerShell that updates the consent artifact:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Patch `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'consentArtifact': 'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID'
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID?updateMask=consentArtifact" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "ACTIVE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "revisionCreateTime": "REVISION_CREATE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### Activating consents

To change the state of a consent from `DRAFT` to `ACTIVE` after the user accepts the consent, use the [`projects.locations.datasets.consentStores.consents.activateConsent`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/activate) method. A new revision is committed with state `ACTIVE`. When the state of the consent is `ACTIVE`, the consent is included in access determination requests.

To activate a consent, make a `POST` request and specify the following information in the request:

  * The REST path of the consent to activate
  * The REST path to an optional artifact to document why the consent was activated
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'consent_artifact': 'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userConsentArtifacts/CONSENT_ARTIFACT_RESOURCE_ID' \
           }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID:activate"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "ACTIVE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'consent_artifact': '/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userConsentArtifacts/CONSENT_ARTIFACT_ID'
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID:activate" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "ACTIVE",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### Revoking and rejecting consents

To change the state of a consent from `DRAFT` to `REJECTED`, for example, if the user indicates that the consent is not acceptable, use the [`projects.locations.datasets.consentStores.consents.reject`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/reject) method. When the state of a consent is `REJECTED`, the consent isn't included in access determination requests.

To change the state of a consent from `ACTIVE` to `REVOKED`, for example if a user requests to void a previously granted consent, use the [`projects.locations.datasets.consentStores.consents.revoke`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.consents/revoke) method. A new revision is committed with state `REVOKED`. Consents with a state of `REVOKED` aren't included in access determination requests. You can create an optional artifact that is associated with the consent to document why the consent was revoked. Revoking a consent doesn't delete the consent.

To revoke a consent, make a `POST` request and specify the following information in the request:

  * The REST path of the consent to revoke
  * The REST path to an optional artifact to document why the consent was revoked
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{}" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID:revoke"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "REVOKED",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{}" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID:revoke" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID",
      "userId": "USER_ID",
      "policies": [
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "identifiable"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity == 'clinical-admin'"
          }
        },
        {
          "resourceAttributes": [
            {
              "attributeDefinitionId": "data_identifiable",
              "values": [
                "de-identified"
              ]
            }
          ],
          "authorizationRule": {
            "expression": "requester_identity in ['internal-researcher', 'external-researcher']"
          }
        }
      ],
      "consentArtifact": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consentArtifacts/CONSENT_ARTIFACT_ID",
      "state": "REVOKED",
      "stateChangeTime": "STATE_CHANGE_TIME",
      "expireTime": "EXPIRE_TIME"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
