---
url: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-ip-allowlists/
title: Configure MongoDB Atlas using IP allowlists \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:07.925320+00:00
---

# Configure MongoDB Atlas using IP allowlists  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-ip-allowlists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure MongoDB Atlas using IP allowlists Stay organized with collections  Save and categorize content based on your preferences. 

To stream change data capture (CDC) updates from a MongoDB Atlas cluster to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations) over a public network, you can configure IP allowlists. To prepare your source, you create a MongoDB user with read privileges, add the Datastream public IP addresses to your MongoDB Atlas allowlist, and create a connection profile.

## Configure a MongoDB database user

To use Datastream with a MongoDB Atlas instance, you first need to create a database user and grant them access privileges:

  1. In the [MongoDB Atlas dashboard](https://www.mongodb.com/products/platform/cloud), under **Security** , click **Database access**.
  2. Click **New database user** and select the password authentication method for your user.
  3. Enter the username and password for your Datastream user.
  4. Under **Database user privileges** , select **Grant specific user privileges**.
  5. Under **Specific privileges** , add the following role: 
     * `readAnyDatabase`
  6. Click **Add user**.



## Retrieve Datastream public IP addresses

When you create a connection profile for your source database, you need to retrieve the public IP addresses for Datastream to authorize them in MongoDB Atlas.

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile** and select **MongoDB**.

  3. Enter the connection details, including the connection profile name, hostname or IP address, port, and database user credentials.

  4. In the **Define connection settings** section, locate the list of Datastream public IP addresses.

  5. Copy these IP addresses.




## Configure IP allowlists in MongoDB Atlas

Allow the Datastream public IP addresses in your MongoDB Atlas security settings:

  1. Sign in to your [MongoDB Atlas account](https://cloud.mongodb.com/).
  2. In the navigation menu, click **Security** , and then click **Network access**.
  3. Click **Add IP address**.
  4. Enter the first IP address that you copied from Datastream.
  5. Repeat this process for each IP address that you want to allowlist.
  6. Click **Confirm** and wait for the status to change to **Active**.



## Test and create the connection profile

After you activate the IP allowlists in MongoDB Atlas, you can verify the connection.

  1. Go back to the **Connection profiles** setup page in the Google Cloud console.
  2. Click **Run test** to test the connectivity to your database.
  3. Verify that the test succeeds, and then click **Create** to save the profile.



If the test fails, check that all Datastream IP addresses are active in the Atlas instance **Network access** list and that the database user has the correct privileges assigned.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
