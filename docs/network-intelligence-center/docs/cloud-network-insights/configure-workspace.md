---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-workspace/
title: Configure Google Workspace \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:22.842065+00:00
---

# Configure Google Workspace  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Configure Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses Google Workspace and restricts what apps you can install, a Google Workspace administrator might need to adjust API access control settings. This prevents users from encountering an `Access Blocked: admin_policy_enforced` error when accessing AppNeta in the embedded AppNeta UI using Google Single Sign-On.

For more information, see [Control which apps access Google Workspace data](https://support.google.com/a/answer/7281227)

## Enable access

To allow the identity and permission verification flow, enable AppNeta access:

  1. Copy the **AppNeta OAuth Client ID** :
         
         499105906135-qg4b9i5v59rv2qgde5dp3qn3hhd6k4uv.apps.googleusercontent.com
         

  2. Open the[ Google Admin Console](https://admin.google.com) and navigate to **Security** > **Access and data control** > **API controls**.

  3. Click **Manage Third-Party App Access**.

  4. Add the `appneta.com` app.

     1. Click **Configure new app**.
     2. Paste the **OAuth Client ID** into the search bar.
     3. Select the `appneta.com` application from the results.
     4. Check the box for the specific client ID and click **Select**.
  5. Define access scope.

     1. Select the organization scope you want to configure access for and click **Continue**.
     2. Under **Access to Google Data** , select **Specific Google data**.
     3. Verify that `Google Cloud` and `Google Sign-in` are included in the permitted services list. This lets you explicitly choose which Google data the app can request.
  6. Verify that the requested scopes match the following:

     * `https://www.googleapis.com/auth/userinfo.email`
     * `https://www.googleapis.com/auth/userinfo.profile`
     * `openid`
  7. Click **Finish**.




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
