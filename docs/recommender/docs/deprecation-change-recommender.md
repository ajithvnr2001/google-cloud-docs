---
url: https://docs.cloud.google.com/recommender/docs/deprecation-change-recommender/
title: Cloud deprecation and breaking changes general recommender \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:50.581236+00:00
---

# Cloud deprecation and breaking changes general recommender  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/deprecation-change-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud deprecation and breaking changes general recommender

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Cloud deprecation and breaking changes general recommender** provides you with recommendations about Cloud deprecations and breaking changes. It identifies Cloud resources that will be affected by upcoming deprecations and breaking changes while providing guidelines on how to manage them. Recommendations are viewable through Google Cloud CLI, the API, and BigQuery export.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)


**Note:** You only need to enable the API on a single billing project. You can then use this same billing project to retrieve recommendations and insights for other projects, the entire organization or the billing account, using the [`--billing-project` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project).

  4. Ensure that you have the following roles:

Description | Roles  
---|---  
View recommendations |  `recommender.cloudDeprecationRecommendationViewer`  
View and update recommendations |  `recommender.cloudDeprecationRecommendationAdmin`  
  
### Required roles

This section describes the roles and necessary permissions to use the **Cloud deprecation and breaking changes general recommender**.

Role | Included permissions  
---|---  
roles/recommender.cloudDeprecationRecommendationViewer | 

  * `recommender.cloudDeprecationGeneralInsights.get`
  * `recommender.cloudDeprecationGeneralInsights.list`
  * `recommender.cloudDeprecationGeneralRecommendations.get`
  * `recommender.cloudDeprecationGeneralRecommendations.list`

  
roles/recommender.cloudDeprecationRecommendationAdmin | 

  * `recommender.cloudDeprecationGeneralInsights.update`
  * `recommender.cloudDeprecationGeneralRecommendations.update`

  
  
For more information about roles and about granting access, see the following:

  * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [Managing access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



## Pricing

**Cloud deprecation and breaking changes general recommender** is offered at no charge. For information about other pricing tiers, see [Recommender pricing](https://cloud.google.com/recommender/pricing).

## View cloud deprecation recommendations

You can list recommendations by using the Console, the Google Cloud CLI, the Recommender API, or through BigQuery export.

###  Console 

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/active-assist/list/manageability/recommendations?pageState=\(%22AaRecommendationTable%22:\(%22f%22:%22%255B%255D%22\)\))

  2. Set the **Filter field** to `Recommender:google.cloud.deprecation.GeneralRecommender`.

**Note:** You must have the have the correct IAM permissions (listed above) in order to see recommendations. If you have the correct permissions and the page does not show any recommendations, then the project does not have any deprecations or breaking changes that meet the criteria for a recommendation.



###  Google Cloud CLI 

This tab shows the commands to list recommendations and insights with Google Cloud CLI.

  * List recommendations
        
        gcloud recommender recommendations list \
          --billing-project=BILLING_PROJECT_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --recommender=google.cloud.deprecation.GeneralRecommender \
          --format=yaml
        

  * List Insights
        
        gcloud recommender insights list \
          --billing-project=BILLING_PROJECT_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
          --insight-type=google.cloud.deprecation.GeneralInsight \
          --format=yaml
        




Replace the following:

  * BILLING_PROJECT_ID with ID of the project that you've enabled with the Recommender API.
  * PROJECT_ID with the identifier for your Google Cloud project.
  * LOCATION with the Google Cloud location where resources associated with the recommendations are located (for example, global or us-central1-a).



### API

This tabs shows your the commands to list recommendations and insights with the Recommender API.

  * List Recommendations
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "x-goog-user-project: BILLING_PROJECT_ID" \
          "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloud.deprecation.GeneralRecommender/recommendations"
        

  * List Insights
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "x-goog-user-project: BILLING_PROJECT_ID" \
          "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloud.deprecation.GeneralInsight/insights"
        




Replace the following:

  * BILLING_PROJECT_ID with ID of the project that you've enabled with the Recommender API.
  * PROJECT_ID with the identifier for your Google Cloud project.
  * LOCATION with the Google Cloud location where resources associated with the recommendations are located (for example, global or us-central1-a).



###  BigQuery export

This tab shows the commands to list recommendations with BigQuery export.

Cloud deprecation recommendations are also included in [BigQuery export](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq). With the BigQuery export, you can view daily snapshots of recommendations for your organization.

  1. Follow the [BigQuery export documentation](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq) to export recommendations to BigQuery.

  2. Query all deprecation recommendations:
         
         SELECT *
         FROM `<project>.<dataset>.recommendations_export`
         WHERE DATE(_PARTITIONTIME) = "<date>"
         and recommender = "google.cloud.deprecation.GeneralRecommender"
         




## Available recommendation subtypes

The following table describes the available and disclosable recommendation subtypes.

Subtype | Deprecation or breaking change?  
---|---  
GCE_METADATA_SERVER_HEADER_WHITESPACE |  Compute Engine will enforce HTTP request formatting checks in the Compute Engine Metadata Service to align with [RFC 7230 Section 3.2](https://notifications.google.com/g/proof/p/ACUgQrFssFgdw4g2yK_7w7qobXnvLrQZOs89s_ihubt3tSBi1OMNl5EJps2mShFQrZ-BwZrhY1l9bnzTv0-Ygnv6Dltvq1V88-nyIQysUeTTX8CinzMuiE81iXEiAiuX-uNp13At7NKmFwgL4H6VfsrnycFOpI_UQuiIk_ljFAVSqeVxJ4YDNfRGrg-52-qHzzROdKQGQm2J_-Ip_4O8Lj6HURq1cgrFjUXeog), as accepting incorrectly formatted requests might lead to security vulnerabilities.   
**Warning:** Dismissed recommendations are not regenerated and will hide the deprecation recommendation for the instance on all surfaces. Instead, mark it as succeeded once you've applied the recommendation.

Note that this table is not comprehensive and may intentionally omit security-sensitive deprecations or breaking changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
