---
url: https://docs.cloud.google.com/datastream/docs/configure-workday/
title: Configure a Workday instance for data replication \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:08.560376+00:00
---

# Configure a Workday instance for data replication  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-workday/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Workday instance for data replication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To replicate data from a Workday instance to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations) such as BigQuery or Cloud Storage, you can connect Workday as a Datastream source. You authenticate the connection by creating an integration system user (ISU), granting security group permissions, and registering an API client for OAuth 2.0.

## Before you begin

Before you start configuring Workday for use with Datastream, you need to:

  * Have access to an active Workday instance.
  * Have knowledge of how to navigate and change settings in Workday.
  * Have knowledge of how to create integration system users and security groups in Workday.



## Configure a Workday instance for use with Datastream

To establish a connection between your Workday instance and Datastream, you need to provide the hostname and tenant name of your instance, as well as OAuth 2.0 client credentials, such as a client ID, a client secret, and a refresh token when you create a Workday connection profile.

### Identify the hostname and the tenant name

You can find the hostname and tenant name of your Workday instance in one of the following ways:

  * Using your sign-in URL address. The hostname and tenant name are part of the instance URL address that you use to sign in to Workday. For example, if your sign-in URL is `https://wd5-impl.workday.com/google/d/home.html`, then the `wd5-impl.workday.com` part is the hostname, and the short name or alias of your instance which appears immediately after the hostname in the URL is the tenant name (in this case, `google`).
  * Using your registered API client details. If you have already registered an API client, you can retrieve this information directly from the REST endpoint URL address:

    1. In Workday, search for and select the **View API Client** task.
    2. Under **Client Details** , find the **Workday REST API Endpoint** field, for example: `https://wd2-impl-services1.workday.com/ccx/api/v1/mytenant`.
    3. Find your credentials:

       * Hostname is the domain part of the URL, for example, `wd2-impl-services1.workday.com`.
       * Tenant name is the last path segment of the URL following `/v1/` (for example, `mytenant`).



For more information about finding your API endpoints, see the [Workday APIs documentation](https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html).

### Configure a user and a security group

To stream data from Workday, you must configure a dedicated Integration System User (ISU), assign it to an unconstrained security group, and grant the group the necessary domain permissions.

#### Create the Integration System User (ISU)

  1. In the Workday search bar, search for and select the **Create Integration System User** task.
  2. Configure the ISU account:

     1. Enter a username, for example, `datastream_isu`.
     2. Create a secure password.
     3. Enter `0` (no timeout) in the **Session Timeout Minutes** field.
     4. Clear the **Do Not Allow UI Sessions** checkbox.
**Note:** You must allow UI sessions initially for the ISU so that you can authenticate and authorize the OAuth 2.0 client. After completing the setup and generating the refresh token, we recommend that you select this checkbox for security.
  3. Click **OK** , and then click **Done**.




#### Create an Integration System Security Group

  1. Search for and select the **Create Security Group** task.
  2. Configure the security group options:

     1. From the **Type of Tenanted Security Group** drop-down, select **Integration System Security Group (Unconstrained)**.
     2. In the **Name** field, enter a name for the security group, for example, `datastream_sg`.
  3. Click **OK**.

  4. On the page that follows, in the **Integration System Users** field, search for and select the ISU that you created in the previous step.

  5. Click **OK**.




#### Grant Domain Security Policy permissions

To ensure full coverage of standard data domains, you must grant the security group **Get Only** permissions for the required Workday domains:

  1. From the security group's details page, click the **Related Actions** ellipsis icon `(...)` next to the security group name.
  2. Go to **Security Group** > **Maintain Domain Permissions for Security Group**.
  3. Under the **Domain Security Policy Permissions** table, add the following domains:

     * `Worker Data: Public Worker Reports`
     * `Workday Usage Metrics`
     * `Manage: Organization Integration`
     * `Worker Data: All Positions`
     * `Job Requisition Data`
     * `Manage: Evergreen Requisitions`
     * `Special OX Web Services`
     * `Prospects`
     * `Candidate Data: Job Application`
     * `Worker Data: Skills and Experience`
     * `Payroll Interface`
     * `Job Information`
     * `Staffing Organizations: Header`
     * `Staffing Organizations: Company`
     * `Staffing Organizations: Region`
     * `Staffing Organizations: Business Unit`
     * `Staffing Organizations: Custom Organization`
  4. For each added domain, select the checkbox in the **Get Only** access column.

  5. Click **OK** , and then click **Done**.




#### Exempt the ISU from password expiration

To prevent stream interruptions due to expired passwords, exempt the ISU from your tenant's standard password expiration rules:

  1. Search for and select the **Maintain Password Rules** task.
  2. In the **System Users exempt from password expiration** field, add the ISU you created.
  3. Click **OK** , and then click **Done**.



#### Activate security policy changes

Make sure that you explicitly activate the domain permission changes, otherwise they don't take effect:

  1. Search for and select the **Activate Pending Security Policy Changes** task.
  2. In the **Comment** field, enter a description for the changes, for example, `Grant permissions for Datastream Workday integration`.
  3. Click **OK**.
  4. On the confirmation page, select the **Confirm** checkbox.
  5. Click **OK** to activate the changes.



### Create and set up an API client

Use the following tasks in Workday to generate the credentials needed for your Datastream connection profile.

#### Register the API client

  1. In the Workday search bar, search for and select the **Register API Client for Integrations** task.
  2. Configure the API client:

     1. Enter a name for your Datastream integration.
     2. Under **Client Grant Type** , select **Authorization Code Grant**.
     3. Under **Access Token Type** , select **Bearer**.
     4. Select the **Enforce Customized Access Token Expiry** checkbox, and then specify an expiry time of your choice.
     5. Optionally, select the **Non-expiring refresh tokens** checkbox to prevent connection disruptions.

**Note:** If your organization security policy requires expiring refresh tokens, you must manually update the refresh token in your Datastream connection profile before or immediately after it expires.
     6. Under **Scopes** , we recommend that you include the following functional areas to ensure full coverage of standard data domains:

        * `Implementation`
        * `Jobs & Positions`
        * `Organizations and Roles`
        * `Payroll Interface`
        * `Pre-Hire Process`
        * `Recruiting`
        * `Staffing`
        * `System`
        * `Talent Pipeline`

The required scopes depend on the endpoints from which you want to stream data.

     7. Select the **Include Workday owned scope** checkbox.

  3. Click **OK**.

  4. Copy and save the generated client ID and client secret. You need these credentials to create the Datastream connection profile.




#### Manage refresh tokens for integrations

  1. After registering the client, click the **ellipsis** icon `(...)` next to the client name and select **Manage Refresh Tokens for Integrations**.
  2. Select the Integration System User (ISU) that you created earlier.
  3. Click **Generate New Refresh Token**.

**Note:** We recommend creating a non-expiring refresh token. If your organization's security policy requires tokens to expire, you must manually update the refresh token in your Datastream connection profile whenever it expires.**Important:** Copy and save the refresh token immediately, because it's displayed only once.



#### Edit API client security groups

  1. To ensure the API client can be used by your ISU, search for the **Edit API Client** task.
  2. Select your registered client and navigate to the security settings.
  3. Add the Integration System Security Group associated with your ISU to the list of allowed security groups for this client.



#### View API client

  1. To retrieve your client ID and client secret, search for the **View API Client** task or go to the API client details page.
  2. Under **Client Details** , locate and copy the **Client ID**.
  3. Click **Manage Consumer Details** to view and copy the **Client Secret**.



## What's next

  * Learn more about the [Workday source](https://docs.cloud.google.com/datastream/docs/sources-workday).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
