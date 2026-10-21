---
url: https://docs.cloud.google.com/recommender/docs/gmp-project-management-recommender/
title: Google Maps Platform project management recommender \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:14.795464+00:00
---

# Google Maps Platform project management recommender  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/gmp-project-management-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Maps Platform project management recommender

The project management recommender helps you improve the health of your Google Maps Platform project. For example, if your project doesn't have secure API keys, the recommender can help restrict these keys in order to secure your account.

Here is one example of a recommendation:

  * If your project has unsecured API keys the recommender will help you restrict them to secure your account.



## Recommender ID

The project management recommender ID is:

  * google.gmp.project.ManagementRecommender



## Required IAM permissions

To access the list of project management recommendations, the following permissions are required:

  * `recommender.gmpProjectManagementRecommendations.list`
  * `recommender.gmpProjectManagementRecommendations.get`



To update the list of project management recommendations, the following permissions are required:

  * `recommender.gmpProjectManagementRecommendations.update`

**Note:** Granting your users these permissions might give them a partial view of the resource for which the recommendation is generated. For more information, see the Recommender [Overview](https://docs.cloud.google.com/recommender/docs/overview). 

### Granting permissions

To grant the required IAM permissions, assign one of the following roles:

  * To access the list of recommendations, assign the **Recommender Viewer** (`roles/recommender.gmpViewer`) role.
  * To update the list of recommendations, assign the **Recommender Admin** (`roles/recommender.gmpAdmin`) role.



For more information, refer to [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Viewing recommendations

Recommendations are available through the [Google Maps Platform Console](https://developers.google.com/maps/gmp-get-started). The following steps show how to view recommendations:

  1. Sign in to Google Cloud console.

[Sign in to Google Cloud console](https://console.cloud.google.com/)

  2. From the menu, click the **Google Maps Platform** item.

  3. You will be taken to the **Overview** page.

  4. In the **Restrict API keys** card, click **Secure your account** to view the list of unrestricted API key recommendations. If you can't find the card, then you either don't have the [permission to view the recommendations](https://docs.cloud.google.com/recommender/docs/gmp-project-management-recommender#permissions), or there aren't any recommendations for the current project.

  5. On the screen which follows, click each recommendation to view its details and restrict your API keys.


**Note:** You can also use the [Credentials page](https://console.cloud.google.com/project/_/google/maps-apis/credentials) to view and manage API key settings.

## Restoring dismissed recommendations

You can restore recommendations that have been dismissed. To do this, visit the [Active Assist Dashboard](https://console.cloud.google.com/active-assist), and click **History** on the top right of the page. Learn more about [Recommendation History](https://docs.cloud.google.com/recommender/docs/active-assist/apply-dismiss-restore-recommendations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
