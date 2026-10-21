---
url: https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting/
title: Troubleshoot SAS issues \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:04.326511+00:00
---

# Troubleshoot SAS issues  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Troubleshoot SAS issues Stay organized with collections  Save and categorize content based on your preferences. 

Use these instructions to troubleshoot issues with the [Spectrum Access System (SAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas) Portal.

To troubleshoot issues with interoperability testing between SAS and a [Citizens Broadband Radio Service Device (CBSD)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd), see [Troubleshoot interoperability testing issues](https://docs.cloud.google.com/spectrum-access-system/docs/topics/iot-troubleshoot).

## SAS Portal login issue

If you log in to the [SAS Portal](https://wirelessconnectivity.google.com/sas) and get an error message such as `You need permission to use the SAS Portal`, do the following:

  1. [Create a Google Account](https://support.google.com/accounts/answer/27441).
  2. Optional: If you have a personal Gmail account, create a new Google Account with your business email address: 
     1. Open the [Google Accounts sign up page](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp).
     2. Select **Use my current email address** , and then enter your work email.



If the issue is not resolved, do the following:

  1. Contact the [SAS Portal administrator](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) to add your Google Account to the SAS Portal.
  2. Open the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  3. [Sign in to Google](https://accounts.google.com/accountchooser/signinchooser?flowName=GlifWebSignIn&flowEntry=AccountChooser) with the account that your SAS Portal administrator provided.
  4. If you have multiple Google Accounts, the SAS Portal automatically logs you in with your default Google Account.
  5. If the account is different from the one that your SAS Portal administrator created, click the **switch to another Google Account** option in the SAS Portal error message.



There are four different user roles in the SAS Portal. [Learn more about user roles](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal).

## CBSD registration issue

The SAS Portal provides information about registration errors in your CBSD. An alert appears when a CBSD fails to register with SAS. For more information about SAS response codes returned to the CBSD or [Domain Proxy (DP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dp), see the [SAS error code troubleshooting matrix](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/errors-grant-suspension#troubleshooting-matrix).

### Review error details

To review the registration errors in your CBSD, do the following:

  1. Open the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. Click _table_chart_ **Table view**.
  5. On the **Device table** page, select a CBSD that displays an alert _warning_.
  6. On the right, click the **Status** tab. 
     1. To review the error code, in the **Device state** section, click **Learn more**.
     2. To view the error details again, click _refresh_**Refresh**.



## Grant suspension issue

An administrator receives email notifications when the [grants](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#grant) are suspended. In the SAS Portal, you can verify if a grant is suspended and learn why a grant was suspended.

To resolve a grant suspension issue, do the following:

  1. Open the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. Click _table_chart_ **Table view**.
  5. On the **Device table** page, select a CBSD that displays _pause_circle_outline_ **Suspended grant**.
  6. On the right, click the **Status** tab.
  7. For **Active grants** , click _expand_more_**Expand** .
  8. For **Suspension reason** , view the reason for the suspension.



## Missing CPI ID in the CPI database

When you verify your [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) identity and get an error message that states `Can't find your CPI-ID in the CPI database`, it's because your CPI certificate was issued recently. New CPI credentials are retrieved once every 24 hours. If the issue still exists after 24 hours, contact the organization that conducted your CPI training. Only your original training program can fix this issue. You can see a list of organizations that offer CPI training on the [WInnForum website](https://cbrs.wirelessinnovation.org/cpi-program-administrator).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
