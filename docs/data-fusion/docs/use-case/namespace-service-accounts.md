---
url: https://docs.cloud.google.com/data-fusion/docs/use-case/namespace-service-accounts/
title: Use case: Access control with namespace service accounts \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:37.169645+00:00
---

# Use case: Access control with namespace service accounts  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/use-case/namespace-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Use case: Access control with namespace service accounts Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the use case where you control access to Google Cloud resources at the namespace level when you migrate data from Cloud Storage to BigQuery.

To control access to Google Cloud resources, namespaces in Cloud Data Fusion use the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) by default.

For better data isolation, you can associate a customized IAM service account (known as a _Per Namespace Service Account_) with each namespace. The customized IAM service account, which can be different for different namespaces, lets you control access to Google Cloud resources between namespaces for pipeline design-time operations in Cloud Data Fusion, such as pipeline preview, Wrangler, and pipeline validation.

For more information, see [Access control with namespace service accounts](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace).

## Scenario

In this use case, your marketing department migrates data from Cloud Storage to BigQuery using Cloud Data Fusion.

![Data pipeline showing Cloud Storage source, Wrangler transform, and BigQuery sink.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/use-case-pipeline.png)

The marketing department has three teams: A, B, and C. Your objective is to establish a structured approach to control data access in Cloud Storage through Cloud Data Fusion namespaces corresponding to each team—A, B, and C, respectively.

## Solution

The following steps show how you control access to Google Cloud resources with namespace service accounts, preventing unauthorized access between the datastores of different teams.

### Associate an Identity and Access Management service account to each namespace

Configure an IAM service account in the namespace for each team (see [Configure a namespace service account](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace#configure)):

  1. Set up the access control by adding a customized service account for Team A—for example, `team-a@pipeline-design-time-project.iam.gserviceaccount.com`.

![Configure a service account for Team A.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/namespace-sa-team-a.png)**Figure 1** : Add a customized service account for Team A.
  2. Repeat the configuration steps for Teams B and C to set up access control with similar customized service accounts.




### Limit access to the Cloud Storage buckets

Limit the access to Cloud Storage buckets by giving appropriate permissions:

  1. Give the IAM service account the `storage.buckets.list` permission, required to list Cloud Storage buckets in the project. For more information, see [Listing buckets](https://docs.cloud.google.com/storage/docs/listing-buckets#console-list-buckets).
  2. Give the IAM service account permission to access the objects in particular buckets.

For example, grant the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) role to the IAM service account associated with the namespace `team_A` on the bucket `team_a1`. This permission lets Team A view and list objects and managed folders, along with their metadata, in that bucket in an isolated design time environment.

![Grant the role on the Bucket details page.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/grant-access-to-team-a1.png)**Figure 2** : On the Cloud Storage **Buckets** page, add the team as a principal and assign the Storage Object User role. 



### Create the Cloud Storage connection in the respective namespaces

Create Cloud Storage connection in each team's namespace:

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page and open an instance in the Cloud Data Fusion web interface.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **System admin > Configuration > Namespaces**.

  3. Click the namespace you want to use—for example, the namespace for Team A.

  4. Click the **Connections** tab, and then click **Add connection**.

  5. Select **GCS** and configure the connection.

![Create the Cloud Storage connection in Cloud Data Fusion](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/create-cloud-storage-connection.png)**Figure 3** : Configure the Cloud Storage connection for the namespace.
  6. Create a Cloud Storage connection for every namespace by repeating the preceding steps. Each team can then interact with an isolated copy of that resource for their design time operations.




### Validate design time isolation for each namespace

Team A can validate the isolation at design by accessing Cloud Storage buckets in their respective namespaces:

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page and open an instance in the Cloud Data Fusion web interface.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **System admin > Configuration > Namespaces**.

  3. Select a namespace—for example the Team A namespace, `team_A`.

  4. Click menu **Menu > Wrangler**.

  5. Click **GCS**.

  6. In the bucket list, click the `team_a1` bucket. 

     * You can view the list of buckets because the Team A namespace has `storage.buckets.list` permission.

     * When you click the bucket, you can view its contents because the Team A namespace has the Storage Object Viewer role.

![Validate the Cloud Storage connection for Team A.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/cloud-storage-connections-team-a.png)![Validate the buckets can be accessed by Team A.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/select-data-team-a1.png)**Figures 4 and 5** : Check that Team A can access the appropriate storage bucket.
  7. Go back to the bucket list and click the `team_b1` or `team_c1` bucket. The access is restricted, as you isolated this design time resource for Team A using its namespace service account.

![Validate that Team A cannot access restricted resources.](https://docs.cloud.google.com/static/data-fusion/docs/images/use-case/team-a-cannot-access-team-b-resource.png)**Figure 6** : Check that Team A cannot access Team B and C storage buckets.



## What's next

  * Learn more about [security](https://docs.cloud.google.com/data-fusion/docs/concepts/security) features in Cloud Data Fusion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
