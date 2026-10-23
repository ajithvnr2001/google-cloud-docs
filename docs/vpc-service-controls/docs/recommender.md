---
url: https://docs.cloud.google.com/vpc-service-controls/docs/recommender/
title: Optimize perimeters with recommender \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:43.724965+00:00
---

# Optimize perimeters with recommender  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Optimize perimeters with recommender Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The VPC Service Controls [recommender](https://docs.cloud.google.com/recommender/docs/key-concepts#recommenders) provides recommendations and insights for resources and perimeters on Google Cloud based on the perimeter configuration and historical traffic usage. You can use these recommendations to strengthen your exfiltration defense posture and optimal perimeter configurations with minimal manual discovery.

Each recommendation includes insights on identified risks and actionable next steps to apply the recommendation to your service perimeters.

Use the recommender to help protect your projects with perimeters and optimize your VPC accessible services configurations. For more information, see the [recommender documentation](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

## Recommendations and insights addressed by the recommender

The following table describes what the VPC Service Controls recommender detects and helps you address:

Vulnerability or misconfiguration type | Detected insight | Recommended action  
---|---|---  
**Critical resources at risk of exfiltration** | Sensitive services in a project aren't restricted by a service perimeter (either directly or through folder membership), exposing resources to exfiltration risks. The recommender flags your most used VPC Service Controls supported services (such as BigQuery, Cloud Storage, Spanner, or Bigtable) based on historical request counts. | Configure a new service perimeter that restricts the identified project and its active services, or add the project to an existing service perimeter.  
**Unconfigured VPC accessible services** | A service perimeter doesn't have [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) configured. By default, all supported APIs remain accessible from within the perimeter, increasing exfiltration risks from network endpoints inside the perimeter. | Enable the **VPC accessible services** restriction on the perimeter and limit access only to the set of services required by your workloads (minimally including the `RESTRICTED-SERVICES` value).  
**Misconfigured VPC accessible services** | A service perimeter has configured accessible services that aren't inhibited or restricted within the perimeter (they aren't restricted services). This configuration allows unsanctioned traffic boundary crossings and exposes assets. | To correct the misconfiguration, do the following: 

  * Removing the unrestricted services from the allowed VPC accessible services list.
  * Adding the services into the restricted services list for the perimeter to ensure consistent protection.

  
  
## Before you begin

Before you can view or retrieve recommendations, do the following:

  * Ensure that the **Recommender API** (`recommender.googleapis.com`) is enabled. For more information, see [Enabling the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).
  * Verify that you have the permissions required to view or retrieve recommendations.



### Required roles

To get the permissions that you need to view or update recommendations, ask your administrator to grant you the following IAM roles on the project, folder, or organization: 

  * View recommendations and insights: [Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) (`roles/recommender.viewer`) 
  * View, update, and dismiss recommendations: [Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.admin) (`roles/recommender.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view or update recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view or update recommendations:

  * View recommendations and insights: 
    * `recommender.vpcScRecommendations.get`
    * `recommender.vpcScRecommendations.list`
  * View, update, and dismiss recommendations: `recommender.vpcScRecommendations.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The recommender updates recommendations daily. If you create a new perimeter or resolve an outstanding issue, it takes up to 24 hours for the recommendations to update in Active Assist.

## View and apply recommendations

You can view and act on security recommendations for your projects and perimeters using the Google Cloud console, the Google Cloud CLI, or the Recommender API.

### Console

  1. In the Google Cloud console, go to the **Active Assist** page.  
[Go to Active Assist](https://console.cloud.google.com/home/recommendations)

  2. Filter by **Security** or search for **VPC Service Controls** recommendations.

  3. Click a VPC Service Controls recommendation card to open the details panel. The panel displays the underlying security insights, resources involved, and specific instructions.

  4. Follow the instructions in the panel to configure or update your perimeters.




### gcloud

To retrieve recommendations using the Google Cloud CLI, run the `gcloud recommender` command:
    
    
    gcloud recommender recommendations list \
      --recommender=google.accessContextManager.VpcScRecommender \
      --location=global
    

For more details about filtering and processing metadata using command-line tools, see the [gcloud recommender CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations).

### API and exports

For large-scale automation or custom reporting, you can use the following programmatic integrations:

  * **Recommender API** : Retrieve recommendations programmatically. For more information, see [Using the Recommender API](https://docs.cloud.google.com/recommender/docs/using-api).
  * **BigQuery export** : Set up automatic exports of all recommendations directly to a BigQuery dataset. This export is useful for creating custom visualization dashboards or piping data to a SIEM tool. For more information, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).



## Apply recommendations for VPC accessible services

If the recommender alerts you to an unconfigured or misconfigured allowed services list on a perimeter, you can resolve the issue using the Google Cloud CLI.

### Resolve unconfigured accessible services

To enable VPC accessible services and configure them with a secure minimum set of restricted APIs, run the following command:
    
    
    gcloud access-context-manager perimeters update PERIMETER_NAME \
      --enable-vpc-accessible-services \
      --add-vpc-allowed-services=RESTRICTED-SERVICES

Replace the following:

  * PERIMETER_NAME: The name of the service perimeter.



### Resolve misconfigured accessible services

If the allowed accessible services aren't aligned with your restricted services list, do one of the following to resolve the misconfiguration:

  1. To restrict the allowed accessible services to the standard restricted services list, run the following command: 
         
         gcloud access-context-manager perimeters update PERIMETER_NAME   
         
         --clear-vpc-allowed-services   
         
         --add-vpc-allowed-services=RESTRICTED-SERVICES

  2. Alternatively, to add a specific service (such as `bigquery.googleapis.com` or `storage.googleapis.com`) to the perimeter's restricted list so that it matches the accessible services list, run the following command: 
         
         gcloud access-context-manager perimeters update PERIMETER_NAME   
         
         --add-restricted-services=SERVICE_NAME




Replace the following:

  * PERIMETER_NAME: The name of the service perimeter.
  * SERVICE_NAME: The API identifier name of the service (such as `bigquery.googleapis.com` or `storage.googleapis.com`).



## What's next

  * Learn how to [set up a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter).
  * Understand how [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) can restrict the APIs accessible from within a perimeter.
  * Learn how to [troubleshoot service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
