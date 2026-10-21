---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-docker/
title: Connecting SQL Server client using the Cloud SQL Auth Proxy Docker image \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:55.672227+00:00
---

# Connecting SQL Server client using the Cloud SQL Auth Proxy Docker image  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)



Send feedback 

#  Connecting SQL Server client using the Cloud SQL Auth Proxy Docker image Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-docker "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-docker "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to connect a sqlcmd client to your Cloud SQL instance, from a client machine running Linux or Compute Engine Linux instance, using the Cloud SQL Auth Proxy Docker image.

## Before you begin

You must have:

  * Installed the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). [Learn more](https://docs.cloud.google.com/sdk/downloads).
  * Authorized the gcloud CLI. [Learn more](https://docs.cloud.google.com/sdk/docs/authenticate).
  * Set the default project for the gcloud CLI. [Learn more](https://docs.cloud.google.com/sdk/docs/managing-properties#setting_properties).
  * Configured a database user on your Cloud SQL instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/users).



## Connect a sqlcmd client using the Cloud SQL Auth Proxy Docker image

**To connect using the Cloud SQL Auth Proxy Docker image:**

  1. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. If you are using a Compute Engine instance, prepare the instance: 
     1. Display the Compute Engine instance properties: 
            
            gcloud compute instances describe [GCE_INSTANCE_NAME]

     2. Verify the scopes enabled on the instance. 

Authenticating using scopes requires both of the following scopes: 

        * `https://www.googleapis.com/auth/sqlservice.admin`
        * `https://www.googleapis.com/auth/devstorage.read_write`

Alternatively, the `https://www.googleapis.com/auth/cloud-platform` scope enables all Google Cloud Platform APIs.

If your Compute Engine instance does not have the proper scopes, you can update the instance to include them. For more information, see [ the Compute Engine documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes). 

     3. Open a terminal connection to the instance, using the instructions at [ Connecting to Linux Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). 
  3. Install the sqlcmd client on the Compute Engine instance or client machine, if it is not already installed. 

### Debian/Ubuntu

For Debian/Ubuntu, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#ubuntu). 

### CentOS/RHEL

For CentOS/RHEL, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#install-tools-on-rhel-7). 

### openSUSE

For openSUSE, [ install the applicable SQL Server command-line tools](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?view=sql-server-2017#tools). 

### Other platforms

See the [ landing page](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-database-engine?view=sql-server-2017) for installing SQL Server, as well as the [ SQL Server downloads page](https://www.microsoft.com/en-us/sql-server/sql-server-downloads). 

  4. If needed, install the Docker client: 
         
         curl https://get.docker.com | sh
         sudo usermod -aG docker $USER

If you are using a [ container-optimized](https://docs.cloud.google.com/compute/docs/containers/vm-image) Compute Engine instance, it already has the Docker client installed.

  5. Install the Cloud SQL Auth Proxy Docker image from the [Google Container Registry](https://docs.cloud.google.com/container-registry). 
         
         docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2

  6. If you are running the Cloud SQL Auth Proxy Docker image on a local machine (not a Compute Engine instance), or your Compute Engine instance does not have the proper scopes, create a Google Cloud Platform service account. If you are connecting from Compute Engine, make sure your VM has the proper `scope` to connect using the Cloud SQL Admin API. 

[ Configure the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) to have either of the following access scopes: 

     * https://www.googleapis.com/auth/sqlservice.admin
     * https://www.googleapis.com/auth/cloud-platform
     1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/)

     2. Select the project that contains your Cloud SQL instance. 
     3. Click **Create service account**. 
     4. In the **Service account name** field, enter a descriptive name for the service account. 
     5. Change the **Service account ID** to a unique, recognizable value and then click **Create and continue**. 
     6. Click the **Select a role** field and select one of the following roles: 
        * **Cloud SQL > Cloud SQL Client**
        * **Cloud SQL > Cloud SQL Editor**
        * **Cloud SQL > Cloud SQL Admin**

**Note:** To create a service account with the required permissions, you must have `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles.  
You must also have enabled the Cloud SQL Admin API. If you are using the legacy project roles (Viewer, Editor, Owner), the service account must have at least the Editor role.

     7. Click **Done** to finish creating the service account.
     8. Click the action menu for your new service account and then select **Manage keys**. 
     9. Click the **Add key** drop-down menu and then click **Create new key**. 
     10. Confirm that the key type is JSON and then click **Create**. 

The private key file is downloaded to your machine. You can move it to another location. Keep the key file secure. 

You provide the path to the key file as "PATH_TO_KEY_FILE" when you start the Cloud SQL Auth Proxy. 

  7. Go to the Cloud SQL Instances page in the Google Cloud console. 

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  8. Select the instance to open its _Instance details_ page and copy the **Instance connection name**. 

For example: `myproject:us-central1:myinstance`.

  9. Start the Cloud SQL Auth Proxy. 

### TCP sockets
         
         docker run -d   
           -v PATH_TO_KEY_FILE:/path/to/service-account-key.json   
           -p 127.0.0.1:1433:1433   
           gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2   
           --address 0.0.0.0 --port 1433   
           --credentials-file /path/to/service-account-key.json INSTANCE_CONNECTION_NAME

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line. 

Always specify the `127.0.0.1` prefix in `-p` so that the Cloud SQL Auth Proxy isn't exposed outside the local host. The `--address 0.0.0.0` flag is required to make the port accessible from outside of the Docker container. 

  10. Start the client: 

The connection string you use depends on whether you started the Cloud SQL Auth Proxy using a TCP socket or Docker.

### TCP sockets

     1. Start the sqlcmd client: 
            
            sqlcmd -S tcp:127.0.0.1,1433 -U USERNAME -P PASSWORD

When you connect using TCP sockets, the Cloud SQL Auth Proxy is accessed through `127.0.0.1`.

     2. If prompted, enter the password.
     3. The sqlcmd prompt appears. 


Need help? For help troubleshooting the proxy, see [Troubleshooting Cloud SQL Auth Proxy connections](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#troubleshooting), or see our [Cloud SQL Support](https://docs.cloud.google.com/sql/docs/sqlserver/getting-support) page. 

## Keep the Cloud SQL Auth Proxy Docker image up to date

The Cloud SQL Auth Proxy Docker image is based on a specific version of the Cloud SQL Auth Proxy. When a new version of the Cloud SQL Auth Proxy becomes available, pull the new version of the Cloud SQL Auth Proxy Docker image to keep your environment up to date. You can see the current version of the Cloud SQL Auth Proxy by checking the [ Cloud SQL Auth Proxy GitHub releases page](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases).

## What's next

  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy). 
  * Get help [ troubleshooting connection issues](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-proxy#troubleshooting) for the Cloud SQL Auth Proxy.
  * Create [users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases). 
  * Learn about [options for connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/sqlserver/external-connection-methods). 
  * Learn about [Docker](https://www.docker.com/).
  * Learn about the [Google Container Registry](https://docs.cloud.google.com/container-registry).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
