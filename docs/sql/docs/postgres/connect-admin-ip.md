---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip/
title: Connect using a psql client \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:36.845879+00:00
---

# Connect using a psql client  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect using a psql client Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip "View this page for the SQL Server database engine")

You can use the PostgreSQL command-line client to connect to Cloud SQL. This page describes how to connect a [ `psql` client](https://www.postgresql.org/docs/current/static/app-psql.html) to your Cloud SQL instance, whether running locally on your client machine, on a Compute Engine VM, or in the Cloud Shell.

**Note:** On Windows, enter these commands before executing `psql` commands:   
`SET PGCLIENTENCODING=utf-8`   
`chcp 65001`

**Note:** For information about connecting a client to a Cloud SQL instance using the Cloud SQL Auth Proxy, see [ Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy). For information about connecting using private IP, see [ Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). 

## Before you begin

Before you can use a `psql` client to connect to your Cloud SQL instance, do the following:

  * Create a Cloud SQL instance, including configuring the default user.

See [ Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance) and [Set the password for the default user account](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#user-root). 

  * Optionally, create a Compute Engine VM instance and then connected to the instance using SSH.

See [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh), or [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  * Determine how you'll connect to your instance.

For the connection options and how to choose from among them, see [About connection options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview). 




## Use a PostgreSQL client on a local machine or a Compute Engine VM

Using a `psql` client to connect to your Cloud SQL instance involves three high-level tasks:

  1. Install the client. 
  2. Configure access to your Cloud SQL instance. 
  3. Connect to your Cloud SQL instance. 



### Install the client

To install the `psql` client, do the following:

### Debian/Ubuntu

Install the psql client from the package manager:
    
    
    sudo apt-get update
    sudo apt-get install postgresql-client

### CentOS/RHEL

Install the psql client from the package manager:
    
    
    sudo yum install postgresql

### openSUSE

Install the psql client from the package manager:
    
    
    sudo zypper install postgresql

### Other platforms

  1. Download the PostgreSQL Core Distribution for your platform from the [PostgreSQL Downloads page](https://www.postgresql.org/download/).   
The Core Distribution includes the psql client. 
  2. Install the PostgreSQL database, following the directions on the download page. 



### Configure access to your Cloud SQL instance

To configure access to your instance, do the following:

  1. From the client machine or Compute Engine VM instance, use [What's my IP](https://ip4.me) to see the IP address of the client machine.
  2. Copy that IP address.
  3. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  4. To open the **Overview** page of an instance, click the instance name. 
  5. Select **Connections** from the SQL navigation menu.
  6. Select the **Networking** tab.
  7. In the **Authorized networks** section, click **Add network** and enter the IP address of the machine where the client is installed. **Note:** The IP address of the instance and the `psql` client IP address you authorize must both be IPv4.
  8. Click **Done**. Then click **Save** at the bottom of the page to save your changes. 
  9. Connect to your instance, either using SSL/TLS or without encryption (without using SSL/TLS). 



### Connect to your Cloud SQL instance without encryption

**Caution:** This procedure configures an unencrypted connection to your database. If your database contains sensitive data, then connect to your instance using SSL/TLS.

To let you connect without encryption, the instance must have [SSL mode](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#enforcing-ssl) set to `ALLOW_UNENCRYPTED_AND_ENCRYPTED`. In the Google Cloud console, the equivalent configuration is **Allow unencrypted network traffic**. 

For more information about the SSL/TLS configuration of your instance, see [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance).

To connect to your instance, do the following:

  1. Confirm that you have installed the client and configured access to your instance. 
  2. Start the `psql` client: 
         
         psql "sslmode=disable dbname=postgres user=postgres hostaddr=INSTANCE_IP_ADDRESS"

  3. Enter your password. 
  4. The psql prompt appears. 



### Connect to your Cloud SQL instance using SSL/TLS

**Note** : If you are using IAM database authentication to log in to the instance, then use the procedure in [Log in using IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#logging-in-as-a-user) instead.

To connect to your instance using SSL/TLS and built-in authentication:

  1. Start the `psql` client: 
         
         psql "sslmode=require \
               hostaddr=INSTANCE_IP_ADDRESS \
               user=postgres dbname=DB_NAME"
            

For example:
         
         psql "sslmode=require \
               hostaddr=203.12.34.56 \
               user=postgres dbname=postgres"
            

You might also want to create a Connection Service File to manage your connection parameters, especially if you are connecting to more than one instance. For more information, see the [ PostgreSQL documentation](https://www.postgresql.org/docs/current/static/libpq-pgservice.html).

  2. Enter the password. The password is mandatory for Cloud SQL even though PostgreSQL supports passwordless connectivity while using SSL/TLS. 
  3. You can confirm that the connection is encrypted by looking for the cipher in the connection information: 
         
         SSL connection (cipher: ECDHE-RSA-AES128-GCM-SHA256, bits: 128)
         




#### Connect to your Cloud SQL instance using SSL/TLS and client certificate verification

If `ssl_mode` on your Cloud SQL instance is configured to `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`, then you must also provide a verified client identity when you log in.

To connect using SSL/TLS certificates with client verification, you need the following:

  * A client public key certificate in a **client-cert.pem** file.
  * A client private key in a **client-key.pem** file. 



In addition, to let the client verify the server's identity for mutual authentication, specify the server certificate **server-ca.pem**.

For example, to start the `psql` client: 
    
    
       psql "sslmode=verify-ca sslrootcert=server-ca.pem \
          sslcert=client-cert.pem sslkey=client-key.pem \
          hostaddr=INSTANCE_IP_ADDRESS \
          user=postgres dbname=DB_NAME"
       

If you do not have a client certificate and a corresponding private key, then [ create a new client certificate](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#new-client).

## Using the client in the Cloud Shell

To connect to a Cloud SQL instance (public IP only):

  1. Go to the Google Cloud console. 

[ Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Click the Cloud Shell icon  towards the right in the toolbar. 

The Cloud Shell takes a few moments to initialize.

  3. At the Cloud Shell prompt, use the built-in client to connect to your Cloud SQL instance: 
         
         gcloud sql connect INSTANCE_ID \
         --user=postgres

  4. Enter your password.



The `gcloud sql connect` command does not support connecting to a Cloud SQL instance using private IP, or using SSL/TLS. To connect with encryption, install and use the proxy in the Cloud Shell: 

  1. [Install the proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#install-the-cloud-sql-proxy) (Linux 64-bit) in the `/home/USER` directory.
  2. Start the proxy, using gcloud CLI authentication: 
         
         ./cloud-sql-proxy INSTANCE_CONNECTION_NAME &

  3. Connect to the database by using the TCP connection: 
         
         psql -U USERNAME --host=127.0.0.1




## What's next

  * Learn about [ configuring an instance with a private IP address](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). 
  * Learn about [ options for connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#external-connection-methods). 
  * Learn about how the [`psql` client works with SSL](https://www.postgresql.org/docs/current/static/libpq-ssl.html). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud SQL free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
