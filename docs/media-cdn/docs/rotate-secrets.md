---
url: https://docs.cloud.google.com/media-cdn/docs/rotate-secrets/
title: Rotate secrets \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:07.289745+00:00
---

# Rotate secrets  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/rotate-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Rotate secrets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to update Media CDN keys used for signed requests. You can have up to three public keys and three validation shared keys, for a total of six keys per keyset. To prevent exceeding those limits during a key rotation, see the following instructions about how to delete a validation shared key and how to add a key.

## Before you begin

  1. [Configure your validation shared keys in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager).

  2. Grant the [Secret Manager Access role](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) (`roles/secretmanager.secretAccessor`) to the Media CDN service account.

### Console

     1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

     2. Select the secret.
     3. In the info panel, click **Add principal**.
     4. For **New principals** , enter the Media CDN service account as follows:  
`service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with your project number.

     5. For **Select a role** , select **Secret Manager** , and then select **Secret Manager Secret Accessor**.
     6. Click **Save**.

### gcloud

Use the [ `gcloud secrets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding):
    
    gcloud secrets add-iam-policy-binding projects/PROJECT_NUMBER/secrets/SECRET_ID \
           --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com" \
           --role="roles/secretmanager.secretAccessor"
        

Replace the following:

     * `PROJECT_NUMBER`: your project number
     * `SECRET_ID`: the ID of the secret




## Delete a secret

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Keysets** tab.

  3. Select the keyset that has the secret that you want to delete, and then click **Edit**.

  4. To delete a secret, in the **Keys > Validation shared keys** section, click delete **Delete** next to the secret name.

  5. Click **Update keyset**.




###  gcloud 

To delete a secret key from a keyset, use the [`gcloud edge-cache keysets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update). Omit the keyset that you want to delete and specify the keysets that you want to keep.

In the following example, `KEY_VERSION_1` isn't listed, while `KEY_VERSION_2` and `KEY_VERSION_3` are listed. Omitting `KEY_VERSION_1` deletes it from the keyset.
    
    
    gcloud edge-cache keysets update KEYSET_NAME \
        --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_2'
        --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_3'
    

Replace the following:

  * `KEYSET_NAME`: the name of the keyset
  * `PROJECT_NUMBER`: your project number
  * `SECRET_ID`: the ID of the secret that you're updating
  * `KEY_VERSION`: the key version



###  text editor 

  1. Export your keyset to a YAML file. Use the [`gcloud edge-cache keysets export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/export).
         
         gcloud edge-cache keysets export KEYSET_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `KEYSET_NAME`: the name of your keyset—for example, `prod-vod-keyset`
     * `FILENAME`: the YAML filename
  2. Edit the exported keyset configuration file to remove the secret key. The following example shows how to remove the oldest secret key, which ends in KEY_VERSION_1:
         
         name: projects/my-project/locations/global/edgeCacheKeysets/prod-vod-keyset
         validationSharedKeys:
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_1"
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_2"
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_3"
         

Replace the following:

     * `PROJECT_NUMBER`: your project number
     * `SECRET_ID`: the ID of the secret that you're updating
     * `KEY_VERSION`: the key version

The edited file looks similar to the following:
    
    name: projects/my-project/locations/global/edgeCacheKeysets/prod-vod-keyset
    validationSharedKeys:
        - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_2"
        - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_3"
    

  3. Import the edited keyset. Use the [`gcloud edge-cache keysets import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import):
         
         gcloud edge-cache keysets import KEYSET_NAME \
             --source=FILENAME.yaml
         




## Add a secret

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Keysets** tab.

  3. Select the keyset for which you want to add a secret, and then click **Edit**.

  4. To add a secret, in the **Keys > Validation shared keys** section, click **Secret**. Then, select a secret from the list, enter a secret manually by specifying its resource ID, or [create a new secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version) and then select it.

  5. Select a secret version from the list or [create a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version#add-secret-version), and then select it.

  6. Click **Update keyset**.




###  gcloud 

To add a secret key to a keyset, use the [`gcloud edge-cache keysets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update). Specify the keysets that you have and the keyset that you want to add.

In the following example, `KEY_VERSION_1` was previously deleted and `KEY_VERSION_4` is the keyset being added. Listing `KEY_VERSION_4` in addition to `KEY_VERSION_2` and `KEY_VERSION_3` adds it to the keyset.
    
    
    gcloud edge-cache keysets update KEYSET_NAME \
        --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_2'
        --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_3'
        --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_4'
    

Replace the following:

  * `KEYSET_NAME`: the name of the keyset
  * `PROJECT_NUMBER`: your project number
  * `SECRET_ID`: the ID of the secret that you're updating
  * `KEY_VERSION`: the key version



###  text editor 

  1. Export your keyset to a YAML file. Use the [`gcloud edge-cache keysets export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/export).
         
         gcloud edge-cache keysets export KEYSET_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `KEYSET_NAME`: the name of your keyset
     * `FILENAME`: the YAML filename
  2. In the exported keyset configuration file, add a new `secretVersion` line that includes a new key version, similar to the following:
         
         name: projects/my-project/locations/global/edgeCacheKeysets/prod-vod-keyset
         validationSharedKeys:
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_2"
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_3"
             - secretVersion: "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION_4"
         

  3. Import the edited keyset. Use the [`gcloud edge-cache keysets import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import):
         
         gcloud edge-cache keysets import KEYSET_NAME \
             --source=FILENAME.yaml
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
