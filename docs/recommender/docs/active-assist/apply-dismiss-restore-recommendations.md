---
url: https://docs.cloud.google.com/recommender/docs/active-assist/apply-dismiss-restore-recommendations/
title: Apply, dismiss, or restore recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:52.542900+00:00
---

# Apply, dismiss, or restore recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/active-assist/apply-dismiss-restore-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply, dismiss, or restore recommendations

You can apply, dismiss or restore a recommendation from the Active Assist.

## Before you begin

Ensure that you have the [necessary roles and permissions](https://docs.cloud.google.com/recommender/docs/active-assist/find-active-assist#before_you_begin) to view recommendations.

## Apply recommendations

**Warning:**

Before applying recommendations in the Google Cloud console or using the API, ensure that impacts are assessed by a reviewer within your organization. The reviewer should have the knowledge to assess impacts identified in recommendations, as well as impacts specific to your infrastructure and business. Applying recommendations without proper assessment could result in unexpected changes, such as issues with system performance, poor reliability, or loss of required permissions. If you choose to apply recommendations without human review, ensure that you have set up a rollback process before making any changes.

Depending on the Google Cloud service, you can apply some recommendations from Active Assist. For recommendations that are supported, the **Apply** button is shown in the recommendation details panel:

![One click apply](https://docs.cloud.google.com/static/recommender/docs/images/rec-hub-apply.png)

Some recommendations might be applied instantly, while others may take more time to complete. Note that some recommendations might not be directly applicable in the details panel. Follow the instructions listed in the details panel to apply them.

![Additional instructions in details panel](https://docs.cloud.google.com/static/recommender/docs/images/detail-panel.png)

## Dismiss a recommendation

Dismissing a recommendation prevents it from being shown in the [Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/getting-started) dashboard and list views for the current project. Additionally, to protect the underlying resources, after you dismiss a recommendation, it cannot be applied from Active Assist or the [Recommender API](https://docs.cloud.google.com/recommender/docs/using-api).

To dismiss a recommendation, select the recommendation and click **Dismiss** :

## Restore a recommendation

Restoring a recommendation that you dismissed marks the recommendation as active. Active recommendations will show in the Active Assist dashboard and category page.

Perform the following steps to restore a recommendation:

  1. Go to the **Applied and dismissed** page.

![Active Assist Dashboard](https://docs.cloud.google.com/static/recommender/docs/images/applied-dismissed-recs.png)

This recommendations table displays all applied and dismissed recommendations from the last 90 days.

     * To see only applied recommendations, use the table to filter for "applied" recommendations.

     * To see only dismissed recommendations, use the table to filter for "dismissed" recommendations.

  2. Next to the recommendation you want to restore, click **RESTORE**.

  3. Verify the information on the confirmation screen. If you are sure it is the recommendation and resource type you want to restore, click **RESTORE**.




For information about changing the state of recommendations, refer to the documentation for the appropriate [recommender](https://docs.cloud.google.com/recommender/docs/recommenders), or for the appropriate [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types).

## What's next

  * [Share recommendations](https://docs.cloud.google.com/recommender/docs/active-assist/share-recommendations)
  * [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
