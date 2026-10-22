---
url: https://docs.cloud.google.com/apigee/docs/hybrid/release-notes/hybrid-v1160-hotfix1/
title: Apigee hybrid 1.16.0-hotfix.1 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:10.517218+00:00
---

# Apigee hybrid 1.16.0-hotfix.1 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/release-notes/hybrid-v1160-hotfix1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Apigee hybrid 1.16.0-hotfix.1 release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** See [Apigee hybrid release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes) for hybrid v1.16.0 and prior release notes. 

## February 06, 2026

v1.16.0-hotfix.1

Announcement

### hybrid 1.16.0-hotfix.1

On February 6, 2026 we released Apigee hybrid 1.16.0-hotfix.1.

**Important:** If your installation is already on Apigee hybrid v1.16.0, use the following procedure to apply this hotfix. For new installations, see [The big picture](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/big-picture) and then apply the hotfix to the new installation with the following instructions.

#### Apply this hotfix with the following steps:

**Note:** This hotfix installs the `apigee-mart-server` container images. All other container images are unchanged from Hybrid v1.16.0.

  1. In your overrides file, update the `image.url` and `image.tag` properties of `ao` and `mart` to version `1.16.0-hotfix.1`: 
         
         ao:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-operators"
             tag: "1.16.0-hotfix.1"
         
         mart:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-mart-server"
             tag: "1.16.0-hotfix.1"
         

  2. Install the hotfix release for Apigee operators, beginning with a dry run: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml \
           --dry-run=server
         

  3. If the dry run is successful, install the hotfix release for Apigee operators: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

  4. Install the hotfix release for your organization, beginning with a dry run: 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml \
           --dry-run=server
         

  5. If the dry run is successful, install the hotfix release for your organization: 
         
         helm upgrade $ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

  6. Verify the organization chart by checking the state: 
         
         kubectl -n APIGEE_NAMESPACE get apigeeorg
         

  7. Install the hotfix release for your environment, beginning with a dry run: 
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml \
           --dry-run=server
         

  8. If the dry run is successful, install the hotfix release for your environment: 
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml
         

  9. Verify the environment chart by checking the state: 
         
         kubectl -n APIGEE_NAMESPACE get apigeeenv
         




v1.16.0-hotfix.1

Fixed

#### Fixed in this release

Bug ID | Description  
---|---  
**479872706** | **An issue that prevented loading API products, apps, and developers after migrating data to Apigee hybrid 1.16.0 in certain configurations has been resolved.**  
**481793880** | **An issue that prevented upgrading an existing organization when monetization was enabled has been fixed.**  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
