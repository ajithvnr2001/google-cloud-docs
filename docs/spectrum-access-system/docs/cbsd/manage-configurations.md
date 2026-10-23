---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations/
title: Manage CBSD configuration \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:08.666084+00:00
---

# Manage CBSD configuration  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Manage CBSD configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Spectrum Access System (SAS) Portal to create, sign, and update multiple Citizens Broadband Radio Service Device (CBSD) configurations from a CSV file.

## Import the CBSD configuration

To import [CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/portal#cbsd-config), you must be an Administrator, Editor, or [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi). Learn more about [user roles](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal).

If you get an error when importing a CBSD configuration, it skips to the next row in the CSV file and continues. After the upload is complete, the importer generates an error report that identifies any lines that were not imported.

To start the import, follow these steps:

  1. Open the deployment. 
     1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
     2. Click **View deployments**.
     3. Optional: If you have access to multiple deployments or nodes, select the desired deployment or node, and then click **Open**.
  2. Import the CSV file.

     1. Click file_upload **Import** , and then click computer **Computer**.
     2. Select the custom CSV that you want to import, and then click **Open**. When you import your customized CSV, the SAS Portal tries to map your column headers to the required fields.

**Important:** If you use a custom CSV, make sure that the **Property** and **Label from files** fields match before importing.
  3. To save the new CBSD configurations, click **Upload**. 

  4. When the import is complete, review for any errors. When you are finished, you get a list of CBSD configurations.


**Important:** For CPIs, the imported files in the **Sign CBSD** column that are marked as **Yes** show a status of **Signed**. Files that are marked as **No** show a status of **Ready for CPI**.

## Edit a CBSD configuration

If you're an Administrator, Editor, or CPI, you can edit the CBSD configurations in the Google SAS Portal.

Edit the CBSD's configuration for the following:

  * When the CBSD configuration changes.
  * When the CBSD configuration details are incorrect.

**Important:** If you're a CPI, your certification requires you to make any needed changes to ensure that the SAS always has the correct CBSD parameters. This includes [re-registering the CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister).

To edit CBSD configurations, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Click **View deployments**.
  3. Optional: If you have access to multiple deployments, select a deployment from the **Deployments** list, and then click **Open**.
  4. On the left, click settings **Settings**.
  5. To select a CBSD, do one of the following: 
     * In map **Map view** , click the CBSD location marker.
     * In table_chart **Table view** , click the row of the CBSD.
  6. On the left, click settings_input_antenna **Device** , and then click lock **Unlock deployment settings**.
  7. Enter your changes, and then do the following: 
     * If you are an Administrator or Editor, click **Save** or **Ready for CPI**.
     * If you are a CPI, click **Sign**.

**Important:** If you edit an **Active** configuration, an inactive configuration is created. You need to sign and re-register it before it can take effect.

If the CBSD is already registered, on the CBSD configuration page, the **Pending changes** section shows a list of updated parameters. The configuration status changes to **Draft** to indicate that a new inactive CBSD configuration has been created. Because SAS is still using the active CBSD configuration from the last successful registration, the CBSD status hasn't changed.

To make the updated parameters take effect, do the following:

  * Ask a CPI to sign the new CBSD configuration.
  * Have the CBSD send a new registration request.



## Delete a CBSD configuration

To delete a CBSD configuration, you need **Edit** permissions. You can only delete CBSD configurations that have an unregistered status.

To delete a CBSD configuration, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments**.
  3. Optional: If you have access to multiple deployments, select a deployment from the **Deployments** list, and then click **Open**.
  4. On the left, click settings **Settings**.
  5. To select the CBSD, do the following: 
     * In map **Map view** , click the CBSD location marker.
     * In table_chart **Table view** , click the row of the CBSD.
  6. To find the device state, click the **Status** tab.
  7. If the device state is **Registered** , **Granted** , **Authorized** , or **Suspended** , you must deregister the CBSD before you delete the configuration.
  8. On the right, click more_vert**More** , and then click **Delete device**.



## Deregister a CBSD

Deregistering a CBSD immediately stops its transmissions. If you plan to re-register the CBSD, new grants for the same power and channel might be suspended until the next Coordinated Periodic Activities among SASs (CPAS) depending on nearby incumbent operators and PAL activity.

To deregister a CBSD, see [Register and deregister a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister).

## What's next

  * Learn how to [validate CPI certification](https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-certification).
  * Learn about [SAS sync](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
