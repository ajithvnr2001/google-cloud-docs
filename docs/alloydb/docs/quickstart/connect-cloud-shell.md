---
url: https://docs.cloud.google.com/alloydb/docs/quickstart/connect-cloud-shell/
title: Quickstart: Connect to AlloyDB from Cloud Shell using the Auth Proxy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:28.016242+00:00
---

# Quickstart: Connect to AlloyDB from Cloud Shell using the Auth Proxy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/quickstart/connect-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to AlloyDB from Cloud Shell using the Auth Proxy

To connect to your AlloyDB for PostgreSQL instance and run SQL queries from a pre-configured browser terminal without installing local client tools, you can use Cloud Shell and the AlloyDB Auth Proxy.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. Verifying billing enables all necessary services.

  3. Make sure that you have an AlloyDB instance [configured for public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#enable-ip). Cloud Shell can't connect to a private IP address.




### Required roles

To use the Auth Proxy, your user account must have the following Identity and Access Management (IAM) roles:

  * AlloyDB Client ([`roles/alloydb.client`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles))
  * Service Usage Consumer ([`roles/serviceusage.serviceUsageConsumer`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer))



If you don't have the required roles, ask your administrator to grant the roles or follow these steps to grant them to your user account:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Find your user account in the list of principals.

  3. Click **Edit principal**.

  4. Click **Add another role**.

  5. Search for and select the **AlloyDB Client** role.

  6. Click **Apply**.

  7. Click **Add another role**.

  8. Search for and select the **Service Usage Consumer** role.

  9. Click **Apply**.

  10. Click **Save**.


**Note:** It can take a few minutes for new IAM permissions to become active.

## Connect to your AlloyDB instance

The Cloud Shell environment includes the Auth Proxy (`alloydb-auth-proxy`) and `psql`, the PostgreSQL interactive terminal.

  1. Activate Cloud Shell.

[Activate Cloud Shell](https://shell.cloud.google.com)

  2. Click **Authorize Cloud Shell**. You only need to do this the first time you use Cloud Shell.

  3. Confirm your user identity in the Cloud Shell Editor. Verify that you're signed in with the user account that has the required IAM roles.
         
         gcloud config list
         

  4. Get the connection URI for your instance:

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. Select your cluster and find your primary instance.

     3. Click **View connectivity configuration**.

     4. Copy the **Connection URI**.

  5. Start the Auth Proxy. In the Cloud Shell terminal, use the copied URI and specify the `--public-ip` flag:
         
         alloydb-auth-proxy CONNECTION_URI --public-ip
         

Replace the following:

     * `CONNECTION_URI`: the **Connection URI** that you copied from the Google Cloud console.

The Auth Proxy starts and displays a message confirming that it's listening on `127.0.0.1:5432`.

  6. Open a new Cloud Shell tab, and connect to the database using `psql`:
         
         psql "host=localhost user=POSTGRES_USERNAME dbname=POSTGRES_DATABASE port=5432"
         

To open a new terminal pane in the existing Cloud Shell window, press `Control+b`+`"` or click ![Add](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add**. This lets you keep the Auth Proxy running in one pane while you run connection commands in the second pane.

To switch between panes, press `Control+b`+keyboard_arrow_up or `Control+b`+keyboard_arrow_down.

Replace the following:

     * `POSTGRES_USERNAME`: your AlloyDB user, typically `postgres`.
     * `POSTGRES_DATABASE`: your AlloyDB database name, typically `postgres`.
  7. When prompted, enter the password for your PostgreSQL user.

  8. Verify the connection by running a SQL query:
         
         SELECT now();
         

  9. To stop `psql`, enter `\q`.

  10. To stop Cloud Shell, enter `exit`.

  11. To stop the Auth Proxy, press `Control+c`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the cluster that you created.

  3. Click **Delete cluster**.

  4. In the confirmation dialog, enter the ID of the cluster and click **Delete** to delete the cluster and its instances.




## What's next

  * Learn about other [ways to connect to AlloyDB](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
