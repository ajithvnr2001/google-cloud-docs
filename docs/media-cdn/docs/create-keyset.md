---
url: https://docs.cloud.google.com/media-cdn/docs/create-keyset/
title: Create and update keysets \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:59.818511+00:00
---

# Create and update keysets  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/create-keyset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Create and update keysets Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to create and update keysets for Media CDN.

## Before you begin

The `EdgeCacheKeyset` that you configure for verifying signed request tokens must include the correct keys for the signature algorithm that you choose.

The following table describes each of the signature algorithms and their required keys.

Signature algorithm | Required keys in the keyset  
---|---  
Ed25519 | Public keys  
HMAC-SHA1 | Validation shared keys  
HMAC-SHA256 | Validation shared keys  
  
At a minimum, you must have either a public key or a validation shared key. You can have up to three public keys and three validation shared keys, for a total of six keys per keyset. For information on generating HMACs when using [dual-token authentication](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication), see [Generate tokens](https://docs.cloud.google.com/media-cdn/docs/generate-tokens).

## Create a keyset

To create a new keyset, do the following:

### Console

  1. In the Google Cloud console, go to the **Media CDN** page. 

[ Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Keysets** tab.
  3. Click add**Create keyset**.
  4. For **Name** , enter a unique keyset name—for example, `prod-vod-keyset`.
  5. Optional: For **Description** , enter a description for your keyset.
  6. Optional: Click **Add label** and enter one or more key-value pairs for your keyset.
  7. Specify at least one public key or one validation key. 

To specify a public key, click **Add public key** and then do the following:

     1. For **ID** , enter an alphanumeric ID.
     2. Select **Enter the value** and specify the base64-encoded value of your Ed25519 public key. Alternatively, select **Use Google-managed key for dual-token authentication**. 
  8. To specify a validation shared key, click **Add validation shared key** , and then do the following: 
     1. For **Secret** , select a secret from the list, enter a secret manually by specifying its resource ID, or [ create a new secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version) and then select it. 
     2. For **Secret version** , select a secret version from the list or [ create a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version#add-secret-version) and then select it. 
  9. Click **Create keyset**. 



### gcloud

Use the [ `gcloud edge-cache keysets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/create).
    
    
    gcloud edge-cache keysets create SHORT_KEYSET_NAME \
        --public-key='id=SSL_PUBLIC_KEY_NAME,value=SSL_PUBLIC_KEY_VALUE'
    

Replace the following:

  * `SHORT_KEYSET_NAME`: a unique name for the keyset—for example, `prod-vod-keyset`
  * `SSL_PUBLIC_KEY_NAME`: the name of your SSL public key
  * `SSL_PUBLIC_KEY_VALUE`: the value of your SSL public key



Review the keys associated with a keyset. Use the [ `gcloud edge-cache keysets describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/describe). 
    
    
    gcloud edge-cache keysets describe prod-vod-keyset
    

The output is similar to the following:
    
    
    name: prod-vod-keyset
    description: "Keyset for prod.example.com"
    publicKeys:
      - id: "key-20200918"
        value: "DThVLjhAKm3VYOvLBAwFZ5XbjVyF98Ias8NZU0WEM9w"
      - id: "key-20200808"
        value: "Lw7LDSaDUrbDdqpPA6JEmMF5BA5GPtd7sAjvsnh7uDA="
    

### Terraform
    
    
    resource "google_network_services_edge_cache_keyset" "default" {
      name        = "prod-vod-keyset"
      description = "Keyset for prod.example.com"
      public_key {
        id    = "key-20200918"
        value = "FHsTyFHNmvNpw4o7-rp-M1yqMyBF8vXSBRkZtkQ0RKY" # Update Ed25519 public key
      }
      public_key {
        id    = "key-20200808"
        value = "Lw7LDSaDUrbDdqpPA6JEmMF5BA5GPtd7sAjvsnh7uDA=" # Update Ed25519 public key
      }
    }

## Modify a keyset

To modify a keyset, do the following:

### Console

  1. In the Google Cloud console, go to the **Media CDN** page. 

[ Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Keysets** tab.
  3. Click the keyset name.
  4. To switch to the edit mode, click the **Edit** button.
  5. Make the changes that you need, and then click **Update keyset**.



### gcloud

Use the [`gcloud edge-cache keysets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update): 
    
    
    gcloud edge-cache keysets update KEYSET_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
