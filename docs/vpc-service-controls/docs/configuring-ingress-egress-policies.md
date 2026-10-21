---
url: https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies/
title: Configuring ingress and egress policies \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:32.904297+00:00
---

# Configuring ingress and egress policies  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Configuring ingress and egress policies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure [ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for your VPC Service Controls perimeter.

Ingress and egress policies can be configured for existing perimeters or included when a perimeter is created.

## Updating ingress and egress policies for a service perimeter

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. Select an existing service perimeter.

  3. Click **Edit**.

  4. On the **Edit service perimeter** page, click **Ingress policy** or **Egress policy**.

  5. Expand the ingress or egress rule that you want to edit.

  6. In the **From** and **To** sections, edit the ingress or egress rule attributes that you want to change.

     * For the list of ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).
**Note:** If you select **All sources** in the **Sources** list of the ingress rule, the ingress policy allows access from any network origin.
     * For the list of egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

The YAML attribute reference describes the same attributes that are found in the Google Cloud console, however the Google Cloud console uses slightly different names.

  7. Click **Save**.




### gcloud

**Note:** the following gcloud commands assume that a default access policy has been configured. For more details, see [Get the name and etag of an access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy)

To update a perimeter policy, run one of the following commands replacing variables with appropriate values:
    
    
    gcloud access-context-manager perimeters update PERIMETER_NAME --set-ingress-policies=INGRESS-FILENAME.yaml
    
    gcloud access-context-manager perimeters update PERIMETER_NAME --set-egress-policies=EGRESS-FILENAME.yaml
    

For example:
    
    
    gcloud access-context-manager perimeters update my-perimeter --set-ingress-policies=my-ingress-rule.yaml
    

For information about configuring ingress and egress rules as YAML files, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress_rules_reference) and [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress_rules_reference).

## Setting ingress and egress policies during perimeter creation

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. Click **New perimeter**.

For information about the other service perimeter configurations, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#console).

  3. On the **Create a service perimeter** page, click **Ingress policy** or **Egress policy**.

  4. Click **Add rule**.

  5. In the **From** and **To** sections, specify the ingress or egress rule attributes that you want to configure.

     * For the list of ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).
**Note:** If you select **All sources** in the **Sources** list of the ingress rule, the ingress policy allows access from any network origin.
     * For the list of egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

The YAML attribute reference describes the same attributes that are found in the Google Cloud console, however the Google Cloud console uses slightly different names.

  6. Click **Create**.




### gcloud

**Note:** the following gcloud commands assume that a default access policy has been configured. For more details, see [Get the name and etag of an access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy)

Run the following command during the creation of a perimeter to create an ingress/egress policy:
    
    
    gcloud access-context-manager perimeters create PERIMETER_NAME --title=TITLE --ingress-policies=INGRESS-FILENAME.yaml --restricted-services=SERVICE --resources="projects/PROJECT"
    
    gcloud access-context-manager perimeters create PERIMETER_NAME --title=TITLE --egress-policies=-EGRESS-FILENAME.yaml --restricted-services=SERVICE --resources="projects/PROJECT"
    

For example:
    
    
    gcloud access-context-manager perimeters create my-perimeter --title=perimeter-for-project-1 --ingress-policies=my-ingress-rule.yaml --restricted-services=storage.googelapis.com --resources="projects/myproject"
    

For information about configuring ingress and egress rules as YAML files, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress_rules_reference) and [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress_rules_reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
