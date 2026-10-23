---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip/
title: Connect using a MySQL client \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:39.370079+00:00
---

# Connect using a MySQL client  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Connect using a MySQL client Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip "View this page for the SQL Server database engine")

You can use the MySQL command-line client to connect to Cloud SQL. This page describes how to connect a [ `mysql` client](https://dev.mysql.com/doc/refman/8.4/en/mysql.html) to your Cloud SQL instance, whether running locally on your client machine, on a Compute Engine VM, or in the Cloud Shell.

**Note:** For information about connecting a client to a Cloud SQL instance using the Cloud SQL Auth Proxy, see [ Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy). For information about connecting using private IP, see [ Configure private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip). 

## Before you begin

Before you can use a `mysql` client to connect to your Cloud SQL instance, do the following:

  * Create a Cloud SQL instance, including configuring the default user.

See [ Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance) and [Set the password for the default user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root). 

  * Optionally, create a Compute Engine VM instance and then connected to the instance using SSH.

See [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh), or [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  * Determine how you'll connect to your instance.

For the connection options and how to choose from among them, see [About connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview). 




## Use a MySQL client on a local machine or a Compute Engine VM

Using a `mysql` client to connect to your Cloud SQL instance involves three high-level tasks:

  1. Install the client. 
  2. Configure access to your Cloud SQL instance. 
  3. Connect to your Cloud SQL instance. 



### Install the client

To install the `mysql` client, do the following:

  1. Download the MySQL Community Server for your platform from the [MySQL Community Server download page](http://dev.mysql.com/downloads/mysql/).   
The Community Server includes the MySQL client. 
  2. Install the Community Server, following the directions on the download page. 



For more information about installing MySQL, see [Installing and Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/installing.html).

### Configure access to your Cloud SQL instance

To configure access to your instance, do the following:

  1. From the client machine or Compute Engine VM instance, use [What's my IP](https://ip4.me) to see the IP address of the client machine.
  2. Copy that IP address.
  3. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  4. To open the **Overview** page of an instance, click the instance name. 
  5. Select **Connections** from the SQL navigation menu.
  6. Select the **Networking** tab.
  7. In the **Authorized networks** section, click **Add network** and enter the IP address of the machine where the client is installed. **Note:** The IP address of the instance and the `mysql` client IP address you authorize must be the _same_ IP version: either IPv4 or IPv6.
  8. Click **Done**. Then click **Save** at the bottom of the page to save your changes. 
  9. Connect to your instance, either using SSL/TLS or without encryption (without using SSL/TLS). 



### Connect to your Cloud SQL instance without encryption

**Caution:** This procedure configures an unencrypted connection to your database. If your database contains sensitive data, then connect to your instance using SSL/TLS.

To let you connect without encryption, the instance must have [SSL mode](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl) set to `ALLOW_UNENCRYPTED_AND_ENCRYPTED`. In the Google Cloud console, the equivalent configuration is **Allow unencrypted network traffic**. 

For more information about the SSL/TLS configuration of your instance, see [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance).

To connect to your instance, do the following:

  1. Confirm that you have installed the client and configured access to your instance. 
  2. Start the `mysql` client: 
         
         mysql --ssl-mode=DISABLED --host=INSTANCE_IP_ADDRESS --user=root --password

  3. Enter your password. 
  4. The mysql prompt appears. 



### Connect to your Cloud SQL instance using SSL/TLS

**Note** : If you are using IAM database authentication to log in to the instance, then use the procedure in [Log in using IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-logins#logging-in-as-a-user) instead.

To connect to your instance using SSL/TLS and built-in authentication:

Before you begin, confirm that you have installed the client and configured access to your instance. 

  1. Start the `mysql` client: 
         
         mysql --ssl-mode=REQUIRED \
            --host=INSTANCE_IP_ADDRESS \
            --user=root --password

**Warning:** Don't include the `--ssl-mode` flag in the command if you are using a MariaDB client to connect to the MySQL instance. Use the client from the [MySQL community server](http://dev.mysql.com/downloads/mysql/) instead. 
  2. Enter the password. 
  3. At the MySQL prompt, enter the `\s` command to verify that your connection is using SSL/TLS. 
  4. Look for the output line with **SSL:**. 
         
         ...
         SSL:                     Cipher in use is DHE-RSA-AES256-SHA
         ...
         

**Warning:** MySQL client versions prior to 5.7.3 consider the `--ssl` options as advisory, and silently fall back to unencrypted connections if the server does not accept an encrypted connection. For more information, see [ Using Encrypted Connections](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connections.html) in the MySQL Reference Manual. To avoid this issue, you can configure the instance so that only SSL/TLS connections can connect to it (for more information, see [Configuring SSL for Instances](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance)). 

For information about troubleshooting connection issues, see [Debug connection issues](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity).




#### Connect to your Cloud SQL instance using SSL/TLS and client certificate verification

If `ssl_mode` on your Cloud SQL instance is configured to `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`, then you must also provide a verified client identity when you log in.

To connect using SSL/TLS certificates with client verification, you need the following:

  * A client public key certificate in a **client-cert.pem** file.
  * A client private key in a **client-key.pem** file. 



In addition, to let the client verify the server's identity for mutual authentication, specify the server certificate **server-ca.pem**.

For example, to start the `mysql` client: 
    
    
        mysql --ssl-mode=VERIFY_CA \
          --ssl-ca=server-ca.pem \
          --ssl-cert=client-cert.pem \
          --ssl-key=client-key.pem \
          --host=INSTANCE_IP_ADDRESS \
          --user=root --password
       

If you do not have a client certificate and a corresponding private key, then [ create a new client certificate](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#new-client).

## Using the client in the Cloud Shell

To connect to a Cloud SQL instance (public IP only):

  1. Go to the Google Cloud console. 

[ Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Click the Cloud Shell icon  towards the right in the toolbar. 

The Cloud Shell takes a few moments to initialize.

  3. At the Cloud Shell prompt, use the built-in client to connect to your Cloud SQL instance: 
         
         gcloud sql connect INSTANCE_ID \
         --user=root

  4. Enter your password.



The `gcloud sql connect` command does not support connecting to a Cloud SQL instance using private IP, or using SSL/TLS. To connect with encryption, install and use the proxy in the Cloud Shell: 

  1. [Install the proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#install-the-cloud-sql-proxy) (Linux 64-bit) in the `/home/USER` directory.
  2. Start the proxy, using gcloud CLI authentication: 
         
         ./cloud-sql-proxy INSTANCE_CONNECTION_NAME &

  3. Connect to the database by using the TCP connection: 
         
         mysql -u USERNAME -p --host=127.0.0.1




## What's next

  * Learn about [ configuring an instance with a private IP address](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip). 
  * Learn about [ options for connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#external-connection-methods). 
  * Learn about the [`mysql` client](https://dev.mysql.com/doc/refman/8.4/en/mysql.html). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud SQL free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
