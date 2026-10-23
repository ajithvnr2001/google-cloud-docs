---
url: https://docs.cloud.google.com/sql/docs/postgres/recommender-set-password-policy/
title: Improve instance security by setting password policies \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:34.576610+00:00
---

# Improve instance security by setting password policies  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/recommender-set-password-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Improve instance security by setting password policies Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/recommender-set-password-policy "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes how to view and implement recommendations about setting a password policy for instances that don't have an instance password policy enabled for built-in authentication users. Password policies help prevent the creation of weak passwords and help with compliance. This [recommender](https://docs.cloud.google.com/recommender/docs/overview) is called **Enable instance password policy**.

Every day, this recommender proactively detects instances that don't have an instance password policy enabled and provides insights and recommendations to improve your instance security. You can view insights and detailed recommendations about these instances by using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the [Recommender API](https://docs.cloud.google.com/recommender/docs/using-api).

## Before you begin

Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

### Required roles and permissions

To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/postgres/project-access-control#roles). 

Tasks | Roles  
---|---  
View recommendations |  `recommender.cloudsqlViewer` or `cloudsql.admin`.   
Apply recommendations |  `cloudsql.editor` or `cloudsql.admin`.   
For more information about IAM roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

## List the recommendations

To list the recommendations, follow these steps:

###  Console 

To list recommendations about instance security, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. View the **Issues** column in the instance table.




Alternatively, follow these steps:

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Exploring recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **All recommendations** card, click **Security**.




###  gcloud 

Run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.SecurityRecommender \
    --filter=recommenderSubtype=ENABLE_INSTANCE_PASSWORD_POLICY
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: A region where your instances are located, such as us-central1.



###  API 

Call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.SecurityRecommender/recommendations?filter=recommenderSubtype=ENABLE_INSTANCE_PASSWORD_POLICY
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: A region where your instances are located, such as `us-central1`.



## View insights and detailed recommendations

To view insights and detailed recommendations, follow these steps:

###  Console 

After listing the recommendations, click a recommendation. The recommendation panel appears, which contains insights and detailed recommendations.

###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.SecurityInsight \
    --filter=insightSubtype=INSTANCE_PASSWORD_POLICY_NOT_ENABLED
    
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION : A region where your instances are located, such as `us-central1`.



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.SecurityInsight/insights?filter=insightSubtype=INSTANCE_PASSWORD_POLICY_NOT_ENABLED
    
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: A region where your instances are located, such as `us-central1`.



## Apply the recommendation

###  Console 

To implement the recommendation, click **Manage password policy** and [enable instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies) on your instance.

###  gcloud 

To implement the recommendation, [enable instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies) on your instance.

###  API 

To implement the recommendation, [enable instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies) on your instance.

## What's next

  * [Enable instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies)
  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [Blog: Maximize your Cloud ROI](https://cloud.google.com/blog/products/management-tools/active-assist-comes-to-google-cloud)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
