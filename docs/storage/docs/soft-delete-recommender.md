---
url: https://docs.cloud.google.com/storage/docs/soft-delete-recommender/
title: Soft delete recommender \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:03:27.515277+00:00
---

# Soft delete recommender  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/soft-delete-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Soft delete recommender Stay organized with collections  Save and categorize content based on your preferences. 

The soft delete recommender helps you balance data protection and storage costs by identifying when to enable or disable soft delete on the buckets in your project. The recommender provides these suggestions based on your data usage and the assessed impact to billing and security.

## Criteria for receiving soft delete recommendations

The soft delete recommender provides recommendations for buckets when the following conditions are met:

  * **Recommendations on enabling soft delete** :

    * Buckets whose soft delete costs would increase by less than 10% of your total Cloud Storage costs.

    * Buckets whose costs total to at least $1.00 USD.

    * Buckets whose deleted bytes amount to less than 10% of the bucket's total cost per month.

  * **Recommendations on disabling soft delete**. Note that disabling soft delete increases the risk of data loss by accidental or malicious deletion.

    * Buckets whose soft delete costs equate to over 50% of your total Cloud Storage costs per month.

    * Buckets whose costs total to at least $20.00 USD.


**Note:** Costs are calculated based on the assumption that a bucket costs $0.02 per GB per month. A generic value is chosen because at runtime the true price calculated from the SKU is unknown.

## Pricing

For information on Recommender pricing, see the [Recommender pricing page](https://docs.cloud.google.com/recommender/pricing#recommender-pricing).

## Considerations

  * Soft delete recommender provides a maximum of 100 recommendations per project, covering both enabling and disabling soft delete.



## Before you begin

Before using Active Assist recommendations, complete the following requirements.

### Enable the Recommender API

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&_ga=2.205605267.1609030456.1726769609-1360967596.1726769609)

### Required roles

To get the permissions that you need to view recommendations in Active Assist, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. 

This predefined role contains the permissions required to view recommendations in Active Assist. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view recommendations in Active Assist:

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`
  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`



## View soft delete recommendations

You can view soft delete recommendations by using [Active Assist](https://docs.cloud.google.com/recommender/docs/recommendation-hub/find-recommnedation-hub). Cloud Storage provides recommendations to enable soft delete for buckets that don't yet have soft delete enabled, as well as recommendations to disable soft delete for buckets that have soft delete enabled.

  1. In the Google Cloud console, go to the **Recommendation Hub** page.

[Go to Recommendation Hub](https://console.cloud.google.com/home/recommendations)

  2. In the **All recommendations** menu, click **All recommendations**.

  3. On the **All recommendations** page, Active Assist displays the following soft delete recommendations:

     * **Disable Soft delete**

     * **Enable Soft delete**

Use the instructions in the following sections to disable or enable soft delete on buckets within your project based on Recommender recommendations.




### View recommendation to disable soft delete

To view the recommendation for disabling soft delete in Active Assist, use the following instructions.

  1. In Active Assist, on the **All recommendations** page, click **Disable Soft delete**.

  2. On the **Insight** page, the recommendation displays the following information:

     * **Bucket name** : the name of the bucket Recommender recommends disabling soft delete for.

     * **Current retention days** : the current soft delete retention duration of the bucket's soft delete policy.

     * **Recommended retention days** : the recommended retention duration to set your soft delete policy to. Any buckets that receive the recommendation to disable soft delete show the recommended retention days as **0 days**.

     * **Cost savings** : the estimated amount of savings per month on your project after disabling soft delete.

  3. To proceed with disabling the soft delete policy based on the Recommender's recommendations, click **View soft delete policy**.

The **Bucket details** page displays.

  4. In the **Protection** tab, under **soft delete policy (for data recovery)** , click **Disable** to disable soft delete on the bucket.

Cloud Storage disables soft delete policy on the bucket. To learn more about how to edit a bucket's soft delete policy, including re-enabling a soft delete policy, see [Edit a bucket's soft delete policy](https://docs.cloud.google.com/storage/docs/use-soft-delete#manage-policy).




### View recommendation to enable soft delete

To view the Recommender recommendation for enabling soft delete in Active Assist, use the following instructions:

  1. In Active Assist, on the **All recommendations** page, click **Enable Soft delete**.

  2. On the **Insight** page, the recommendation displays the following information:

     * **Bucket name** : the name of the bucket in your project Recommender recommends enabling soft delete for.

     * **Current retention days** : the current soft delete retention duration on your bucket. For buckets with soft delete already disabled, Active Assist displays **0 days**.

     * **Recommended retention days** : the recommended number of days to set your soft delete policy to. For enabling soft delete, Recommender recommends setting your bucket's soft delete policy to the minimum retention duration of **7 days**.

     * **Additional cost** : the projected cost for enabling soft delete, which is adjusted to increase by no more than 10% of your total monthly Cloud Storage costs.

  3. To proceed with enabling the soft delete policy based on the Recommender's recommendations, click **View soft delete policy**.

The **Bucket details** page displays.

  4. In the **Protection** tab, under **soft delete policy (for data recovery)** , click **Edit** and enter the recommended soft delete retention duration. Or, if the bucket has never had a soft delete configured before, click **Enable soft delete**.

The soft delete policy takes effect on the bucket. To learn more about how to edit a bucket's soft delete policy, including disabling a soft delete policy, see [Edit a bucket's soft delete policy](https://docs.cloud.google.com/storage/docs/use-soft-delete#manage-policy).




## Opt out of Recommender recommendations

You can opt out of receiving soft delete recommendations if needed. However, opting out of soft delete recommendations impacts all other product-specific recommendations, meaning in addition to no longer receiving soft delete recommendations, you would no longer receive any Cloud Storage-specific recommendations.

To proceed with opting out of soft delete Recommender recommendations, use the Recommender instructions for [opting out of data processing](https://docs.cloud.google.com/recommender/docs/opt-out) and select the **Cloud Storage** data processing group.

## What's next

  * Learn how to [dismiss or restore recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/apply-dismiss-restore-recommendations).

  * Read an [overview of soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).

  * Learn how to [use soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
