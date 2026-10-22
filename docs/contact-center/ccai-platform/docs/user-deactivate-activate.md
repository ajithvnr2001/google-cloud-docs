---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-deactivate-activate/
title: Deactivate and activate users \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:47.978172+00:00
---

# Deactivate and activate users  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-deactivate-activate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Deactivate and activate users Stay organized with collections  Save and categorize content based on your preferences. 

Employees in contact centers often need to be removed from systems quickly and also frequently need to be re-added, without losing important data. The CCAI Platform portal allows administrators to deactivate and reactivate users.

**Note:** It is not possible to delete a user from CCAI Platform, use the deactivation feature instead.

**Deactivated user**

Deactivating a user disables the user from the CCAI Platform portal and the agent adapter in the CRM. The user is also placed in an offline status.

In particular, the user will no longer be able to:

  * Login:

    * Cannot sign in to the CCAI Platform portal or agent adapter in the CRM.

    * The user is logged out and placed in offline status.

  * Data:

    * Data about this user can be accessed in reports and API data.
  * Assignments:

    * User is removed from assigned teams.

    * If assigned individually, the user will be removed from queue assignments.




**Reactivated user**

Reactivating a user enables the user to access the CCAI Platform portal and the agent adapter in the CRM.

In particular, the user will be able to:

  * Login:

    * No activation email will be sent.

    * The previous password can be used to login to access the agent adapter in the CRM and the CCAI Platform portal.

**Note:** If the user doesn't have the previous password, direct the user to click the reset password button on the sign in screen.
  * Data:

    * Previous call data still can be accessed in reports and API.
  * Assignments:

    * User needs to be re-added to teams.

    * User needs to be re-added to queues if assigned individually.




## Deactivate an individual user

![The deactivate a user options and filters are shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/deactivate-user.png)

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams**.

  2. Search for the name of the user you would like to deactivate.

  3. Mark the checkbox next to the user's name.

  4. Click **Deactivate**.

  5. Click **Deactivate** again in the dialog to confirm the action.

  6. For multiple users, mark the checkbox for more than one user at a time.




## Deactivate multiple users

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams.**

  2. Click a user list (ex. All Users, Agents).

  3. Mark the checkbox(s) next to the names of the users you would like to deactivate.

  4. Click **Deactivate**.




## Reactivate individual users

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams.**

  2. Search for the name of the user you would like to reactivate.

**OR** Click a user list (ex. All Users, Agents).

  3. Click the checkbox next to **Show deactivated**.

  4. Click **Activate** next to the user's name;

**OR** Mark the checkbox(s) next to the names of the users you would like to reactivate.

  5. Click **Reactivate**.




## Reactivate multiple users

  1. In the CCAI Platform portal, go to **Setting** > **Users & Teams**.

  2. Click a user list (ex. All Users, Agents).

  3. Click the checkbox next to **Show deactivated**.

  4. Mark the checkbox(s) next to the names of the users you would like to reactivate.

  5. Click **Activate**.




## Filter user lists for deactivated users

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams.**

  2. Click a user list (ex. All Users, Agents).

  3. Click the filter drop-down and select **Deactivated agents**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
