---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip/
title: Connect using a SQL Server client \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:07.088939+00:00
---

# Connect using a SQL Server client  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Connect using a SQL Server client Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip "View this page for the PostgreSQL database engine") | SQL Server

You can use the SQL Server command-line client to connect to Cloud SQL. This page describes how to connect a SQL Server client, whether running locally on your client machine or on a Compute Engine VM, to your Cloud SQL instance.

**Note:** For information about connecting a client to a Cloud SQL instance using the Cloud SQL Auth Proxy, see [ Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy). For information about connecting using private IP, see [ Configure private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip). 

## Before you begin

Before you can use a `sqlcmd` client to connect to your Cloud SQL instance, do the following:

  * Create a Cloud SQL instance, including configuring the default user.

See [ Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) and [Set the password for the default user account](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#user-root). 

  * Optionally, create a Compute Engine VM instance and then connected to the instance using SSH.

See [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh), or [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  * Determine how you'll connect to your instance.

For the connection options and how to choose from among them, see [About connection options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview). 

  * Install the [SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017). 



## Use a SQL Server client on a local machine or a Compute Engine VM

Using a `sqlcmd` client to connect to your Cloud SQL instance involves three high-level tasks:

  1. Install the client. 
  2. Configure access to your Cloud SQL instance. 
  3. Connect to your Cloud SQL instance. 



### Install the client

To install the `sqlcmd` client, do the following:

### Debian/Ubuntu

For Debian/Ubuntu, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#ubuntu). 

### CentOS/RHEL

For CentOS/RHEL, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#install-tools-on-rhel-7). 

### openSUSE

For openSUSE, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?view=sql-server-2017#tools). 

### Other platforms

See the [ landing page](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-database-engine?view=sql-server-2017) for installing SQL Server, as well as the [ SQL Server downloads page](https://www.microsoft.com/en-us/sql-server/sql-server-downloads). 

### Configure access to your Cloud SQL instance

To configure access to your instance, do the following:

  1. From the client machine or Compute Engine VM instance, use [What's my IP](https://ip4.me) to see the IP address of the client machine.
  2. Copy that IP address.
  3. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  4. To open the **Overview** page of an instance, click the instance name. 
  5. Select **Connections** from the SQL navigation menu.
  6. Select the **Networking** tab.
  7. In the **Authorized networks** section, click **Add network** and enter the IP address of the machine where the client is installed. **Note:** The IP addresses must be IPv4. That is, the IP addresses of the instance, and of the client machine that you authorize, both must be IPv4.
  8. Click **Done**. Then click **Save** at the bottom of the page to save your changes. 
  9. Connect to your instance.



### Connect to your Cloud SQL instance

To let you connect without encryption, the instance must have `requireSsl` set to **`false`**. In the Google Cloud console, the **Allow only SSL connections** checkbox must be cleared. 

For more information about the SSL/TLS configuration of your instance, see [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).

To connect to your instance, do the following:

  1. Confirm that you have installed the client and configured access to your instance. 
  2. Use the `sqlcmd` command to connect, by following steps similar to those in the examples on the [ SQL Server quickstart](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-2017#connect-locally) and [Use the utility](https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-use-the-utility?view=sql-server-2017) pages. 



### Connect to your Cloud SQL instance using SSL/TLS

Use the instructions in the [ Client Initiated Encryption](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-encrypted-connections?view=sql-server-2017#client-initiated-encryption) section, and related sections, of the [ Encrypting Connections to SQL Server on Linux](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-encrypted-connections?view=sql-server-2017) page. 

## What's next

  * Learn about [ configuring an instance with a private IP address](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip). 
  * Learn [more about SQL Server](https://docs.microsoft.com/sql/sql-server/sql-server-technical-documentation). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud SQL free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
