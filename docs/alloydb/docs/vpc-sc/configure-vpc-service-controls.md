---
url: https://docs.cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:32.162853+00:00
---

# Configure VPC Service Controls  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of VPC Service Controls, a Google Cloud feature that integrates with AlloyDB to secure data and resources.

VPC Service Controls helps mitigate the risk of data exfiltration from AlloyDB instances. You can use VPC Service Controls to create service perimeters that protect the resources and data of services that you explicitly specify.

For a general overview of VPC Service Controls, its security benefits, and its capabilities across Google Cloud products, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  1. In the Google Cloud console, go to the **Project Selector** page. 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). **Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project. 
  3. Make sure that billing is enabled for your Google Cloud project. Learn how to [ check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  4. Enable the Compute Engine API. 

[Enable the Compute Engine API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. Enable the Service Networking API. 

[Enable the Service Networking API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com)

  6. Add the [ Identity and Access Management (IAM) roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control#required_roles) to the user or service account that you're using to set up and administer VPC Service Controls. For more information, see [ IAM roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).
  7. Review [ limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_alloydb_api) when you use VPC Service Controls with AlloyDB.

**Note:** If you use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), both the [host project and the service project](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#shared_vpc) should be included in the service perimeter. 

## How to secure AlloyDB service using VPC Service Controls

Before you begin, review [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [AlloyDB limitations when using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_alloydb_api).

Configuring VPC Service Controls for an AlloyDB project includes the following steps:

  1. Create and manage a service perimeter.

First, you select the AlloyDB project that you want the VPC service perimeter to protect, and then you create and manage the service perimeter.

  2. Create and manage access levels.

Optionally, to permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter. You can't use access levels to give protected resources or VMs permission to access data and services outside the perimeter.




## Create and manage a service perimeter

To create and manage a service perimeter, complete the following steps:

  1. Select the AlloyDB project that you want the VPC service perimeter to protect.

  2. Create a service perimeter by following the instructions in [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  3. Add more instances to the service perimeter. To add existing AlloyDB instances to the perimeter, follow the instructions in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#updating_a_service_perimeter).

  4. Add APIs to the service perimeter. To mitigate the risk of your data being exfiltrated from AlloyDB, you must restrict AlloyDB API, Compute Engine API, Cloud Storage API, Container Registry API, Certificate Authority Service API, and Cloud KMS API. For more information, see [access-context-manager perimeters update](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update).

To add APIs as restricted services:

### Console

     1. In the Google Cloud console, go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter)

     2. In the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.
     3. Click **Edit**.
     4. In the **Edit VPC Service Perimeter** page, click **Add Services**.
     5. Add **AlloyDB API** , **Compute Engine API** , **Cloud Storage API** , **Container Registry API** , **Certificate Authority Service API** , and **Cloud KMS API**.
     6. Click **Save**.

### gcloud
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --policy=POLICY_ID \
    --add-restricted-services=alloydb.googleapis.com,compute.googleapis.com,storage.googleapis.com,
      containerregistry.googleapis.com,privateca.googleapis.com,cloudkms.googleapis.com
    

     * PERIMETER_ID: The ID of the perimeter or the fully qualified identifier for the perimeter.
     * POLICY_ID: The ID of the access policy.

  5. If you [enabled advanced query insights features](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights#enable-advanced-features), add the `databaseinsights.googleapis.com` API to the service perimeter as a restricted service:

### Console

     1. In the Google Cloud console, go to the **VPC Service Controls** page. 

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter)

     2. In the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.
     3. Click **Edit**.
     4. In the **Edit VPC Service Perimeter** page, click **Add Services**.
     5. Add **databaseinsights.googleapis.com**.
     6. Click **Save**.

### gcloud
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --policy=POLICY_ID \
    --add-restricted-services=databaseinsights.googleapis.com
    

     * PERIMETER_ID: The ID of the perimeter or the fully qualified identifier for the perimeter.
     * POLICY_ID: The ID of the access policy.




## Create and manage access levels

To create and manage access levels, follow the instructions in [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
