---
url: https://docs.cloud.google.com/migration-center/docs/service-perimeter/
title: Secure your data with a service perimeter \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:25.803534+00:00
---

# Secure your data with a service perimeter  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Secure your data with a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls helps you reduce the risk of unauthorized copying or transfer of data from your Google-managed services.

With VPC Service Controls, you can configure service perimeters around the resources of your Google-managed services and control the movement of data across the perimeter boundary.

## Create a service perimeter

To create a service perimeter, follow the [VPC Service Controls guide to creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

When you design the service perimeter, include the following services:

  * Migration Center API (`migrationcenter.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Resource Manager API (`cloudresourcemanager.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)



## Allow traffic with inbound data transfer rules

By default, the service perimeter is designed to prevent inbound data transfer from services outside of the perimeter. If you plan to use data import to upload data from outside the perimeter, or use the discovery client to collect your infrastructure data, configure data access rules to allow this.

### Enable data import

To enable data import, specify the [inbound data transfer rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) using the following syntax:
    
    
    - ingressFrom:
        identities:
        - serviceAccount: SERVICE_ACCOUNT
        sources:
        - accessLevel: \"*\"
    - ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: google.storage.buckets.testIamPermissions
          - method: google.storage.objects.create
        resources:
        - projects/PROJECT_ID
    

Replace the following:

  * `SERVICE_ACCOUNT`: the per-product, per-project service account that you use to upload data to Migration Center, with the following format: `service-PROJECT_NUMBER@gcp-sa-migcenter.iam.gserviceaccount.com.`

Here `PROJECT_NUMBER` is the unique identifier of the Google Cloud project where you enabled the Migration Center API. For more information on project numbers, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * `PROJECT_ID`: the ID of the project inside the perimeter that you want to upload the data to.




You can't use [`ANY_SERVICE_ACCOUNT` and `ANY_USER_ACCOUNT`](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#unsupported-features) identity types with signed URLs. For more information, see [Allow access to protected resources from outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

### Enable data collection with discovery client

To enable data collection with the discovery client, specify the inbound data transfer rules with the following syntax:
    
    
    - ingressFrom:
        identities:
        - serviceAccount: SERVICE_ACCOUNT
        sources:
        - accessLevel: \"*\"
    - ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: \"*\"
        resources:
        - projects/PROJECT_ID
    

Replace the following:

  * `SERVICE_ACCOUNT`: the service account that you used to create the discovery client. For more information, review the [discovery client installation process](https://docs.cloud.google.com/migration-center/docs/installation-process#create_a_service_account).

  * `PROJECT_ID`: the ID of the project inside the perimeter that you want to upload the data to.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
