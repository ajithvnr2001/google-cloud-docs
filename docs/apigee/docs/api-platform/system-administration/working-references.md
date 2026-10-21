---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/working-references/
title: Working with References \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:51:20.279755+00:00
---

# Working with References  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/working-references/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Working with References Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When configuring a TargetServer to support TLS, you specify a keystore or truststore by using a reference. A reference is a variable that contains the name of the keystore or truststore, rather than specifying the keystore or truststore name directly.

A reference can be represented by an XML object like the one below:
    
    
      <reference>
        <name>ReferenceName</name>
        <description>ReferencDescription</description>
        <resourceType>ReferredResourceType<resourceType>
        <refers>ReferredResource<refers>
      </reference>

The advantage to using a reference is that you can change the value of the reference to change the keystore used by the target server, usually because the cert in the current keystore is expiring in the near future.

You can only use a reference to the keystore and truststore; you cannot use a reference to the alias. When you change the reference to a keystore, ensure that the alias name of the cert is the same as in the old keystore.

#### Restrictions on using references to keystores and truststore

If you have a load balancer and terminate TLS on the load balancer, then you cannot use keystore and truststore references in the target server.

## Create a reference

You can use the Apigee UI or API to create a new reference.

### Apigee UI

To create a reference using the Google Cloud console:

  1. In the Google Cloud console, go to the **Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the desired environment where you want to create the reference.

  3. Click the **References** tab.

  4. Click **Create Reference**.

  5. In the **Create Reference** pane, enter the following details: 
     * **Name** : The name of the reference.
     * **Keystore** : The keystore to which the reference points.
  6. Click **Create**.




### API

To create a reference using the [Create Reference](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/create) API call:
    
    
          curl -H "Authorization: Bearer $TOKEN" \
            -X POST \
            -d '{
                "reference": {
                  "name": MyReferenceName",
                  "resourceType": "KeyStore",
                  "refers": "KeyStoreID"
                }
               }' \
            https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/references

## Modify a reference

You can use the Apigee UI or API to modify an existing reference.

### Apigee UI

To modify a reference using the Google Cloud console:

  1. In the Google Cloud console, go to the **Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the desired environment where you want to modify the reference.

  3. Click the **References** tab.

  4. In the displayed list, select the reference that you want to modify.

  5. Click more_vert **Actions** > **Edit**.

  6. In the **Edit Reference** pane, update the reference to specify the new keystore.
  7. Click **Update**.




### API

To change the reference to point to a different keystore, ensuring that the alias in the new keystore has the same name as the alias in the old keystore, use the [ Update Reference](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/update) API:
    
    
            curl -H "Authorization: Bearer $TOKEN" \
              -X PUT \
              -d '{
                  "name": "MyReferenceName",
                  "resourceType": "KeyStore",
                  "refers": "KeyStoreID"
                  }' \
            https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/references/*}
          

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
