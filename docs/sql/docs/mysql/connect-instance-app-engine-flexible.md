---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-app-engine-flexible/
title: Connect to Cloud SQL for MySQL from App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:12.088199+00:00
---

# Connect to Cloud SQL for MySQL from App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-app-engine-flexible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for MySQL from App Engine flexible environment

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-app-engine-flexible "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-app-engine-flexible "View this page for the SQL Server database engine")

Learn how to deploy a sample app on [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible) connected to a MySQL instance by using the Google Cloud console and a client app.

Assuming that you complete all the steps in a timely manner, the resources created in this quickstart typically cost less than one dollar (USD).

## Before you begin

**Note:** The name you use for your project must be between 4 and 30 characters. When you type the name, the form suggests a project ID, which you can edit. The project ID must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud APIs necessary to run a Cloud SQL sample app on App Engine flexible environment. 

### Console

Click the button below to enable the APIs required for this quickstart.

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=appengineflex.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com)

This enables the following APIs:

     * Cloud SQL Admin API
     * Compute Engine API
     * Cloud Build API
     * Cloud Logging API

By clicking the button, you also enable the Google App Engine Flexible Environment.

### gcloud

Click the following button to open Cloud Shell, which provides command-line access to your Google Cloud resources directly from the browser. Cloud Shell can be used to run the `gcloud` commands presented throughout this quickstart.

[Open Cloud Shell](https://docs.cloud.google.com/console/sql/instances?cloudshell=true)

Run the following `gcloud` command using Cloud Shell:
    
    gcloud services enable appengineflex.googleapis.com sqladmin.googleapis.com \
    compute.googleapis.com cloudbuild.googleapis.com logging.googleapis.com

This command enables the following APIs:

     * Cloud SQL Admin API
     * Compute Engine API
     * Cloud Build API
     * Cloud Logging API

By running the above command, you also enable the Google App Engine Flexible Environment.




## Set up Cloud SQL

### Create a Cloud SQL instance

#### Public IP

Take the following steps to set up a Cloud SQL instance that you connect to over public IP:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose MySQL**.
  5. Make sure that **Enterprise Plus** is selected as the Cloud SQL edition for your instance.
  6. In the **Instance ID** field, enter `quickstart-instance`.
  7. In the **Password** field, enter a password for the root user. Save this password for future use.
  8. In the **Choose region and zonal availability** section, select **Single zone**.
  9. Click the **Show configuration options** menu.
  10. Expand the **Machine configuration** node.
  11. From the **Machine shapes** region, select the **4 vCPU, 32 GB** shape.
  12. Click **Create instance** and then wait until the instance initializes and starts.



### gcloud

Before running the command as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

  * **\--database-version** : The database engine type and version. If left unspecified, the API default is used. See the [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) documentation to see the current available versions.
  * **\--cpu** : The number of cores desired in the machine.
  * **\--memory** : Whole number value indicating how much memory is desired in the machine. A size unit should be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
  * **\--region** : Regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central` is used. 



Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance. 
    
    
     gcloud sql instances create quickstart-instance \
    --database-version=MYSQL_8_0 \
    --cpu=1 \
    --memory=4GB \
    --region=us-central1 \
    --root-password=DB_ROOT_PASSWORD

#### Private IP

Take the following steps to set up a Cloud SQL instance that you connect to over private IP:

### Console

####  Allocate an IP address range and create a private connection to configure private services access for Cloud SQL 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks)

  2. Select the `default` VPC network.
  3. Select the **Private service connection** tab.
  4. Select the **Allocated IP ranges for services** tab.
  5. Click **Allocate IP range**.
  6. For the **Name** of the allocated range, specify `google-managed-services-default`.
  7. Select the **Automatic** option for IP range and specify the prefix length as `16`.
  8. Click **Allocate** to create the allocated range.
  9. Select the **Private connections to services** tab for the `default` VPC network.
  10. Click **Create connection** to create a private connection between your network and a service producer.
  11. For the **Assigned allocation** , select `google-managed-services-default`.
  12. Click **Connect** to create the connection.



####  Create an instance with private IP address and SSL enabled 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose MySQL**.
  5. Make sure that **Enterprise Plus** is selected as the Cloud SQL edition for your instance.
  6. In the **Instance ID** field, enter `quickstart-instance`.
  7. In the **Password** field, enter a password for the root user. Save this password for future use.
  8. In the **Choose region and zonal availability** section, select **Single zone**.
  9. Click the **Show configuration options** menu.
  10. Expand the **Machine configuration** node.
  11. From the **Machine shapes** region, select the **4 vCPU, 32 GB** shape.
  12. Expand the **Connections** node.
  13. Clear the **Public IP** checkbox to create an instance only with a private IP address.
  14. Select the **Private IP** checkbox.
  15. Select the **Private Service Access (PSA)** checkbox.
  16. In the **VPC Network *** dropdown, select **default**.
  17. In the **Security** section, make sure that **Allow only SSL connections** is selected to enable SSL connections.
  18. Click **Create instance** and then wait for the instance to initialize and start.



### gcloud

####  Allocate an IP address range and create a private connection to configure private services access for Cloud SQL 

  1. Run the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command to allocate an IP address range. 
         
         gcloud compute addresses create google-managed-services-default \
         --global --purpose=VPC_PEERING --prefix-length=16 \
         --description="peering range for Google" --network=default

  2. Run the [`gcloud services vpc-peerings connect`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) command to create a private connection to the allocated IP address range. Replace YOUR_PROJECT_ID with your project's project ID. 
         
         gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com \
         --ranges=google-managed-services-default --network=default \
         --project=YOUR_PROJECT_ID




####  Create an instance with private IP address and SSL enabled 

  1. Before running the command as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

     * **\--database-version** : The database engine type and version. If left unspecified, the API default is used. See the [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) documentation to see the current available versions.
     * **\--cpu** : The number of cores in the machine.
     * **\--memory** : A whole number value indicating how much memory to include in the machine. A size unit can be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
     * **\--region** : The regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central1` is used. See the full list of [regions](https://docs.cloud.google.com/sql/docs/instance-locations).

Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance with a Private IP address. 
    
    gcloud sql instances create quickstart-instance \
    --database-version=MYSQL_8_0 \
    --cpu=1 \
    --memory=4GB \
    --region=us-central1 \
    --root-password=DB_ROOT_PASSWORD \
    --no-assign-ip \
    --network=default

  2. Run the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command to enable **only allow SSL connections** for the instance. 
    
    gcloud sql instances patch quickstart-instance --require-ssl




### Create a database

Take the following steps to create a database:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select `quickstart-instance`.
  3. From the SQL navigation menu, select **Databases**.
  4. Click add_box **Create database**.
     1. In the **Database name** field of the **Create a database** dialog, enter `quickstart-db`. Leave the values for the character set and collation.
     2. Click **Create**.



### gcloud

Run the [`gcloud sql databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/create) command to create a database.
    
    
    gcloud sql databases create quickstart-db --instance=quickstart-instance

### Create a user

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the **quickstart-instance** MySQL instance that you created.
  3. From the SQL navigation menu, select **Users**.
  4. Click **Add user account**. 
  5. In the **Add a user account to instance quickstart-instance** page, add the following information: 
     1. In the **User name** field, enter `quickstart-user`.
     2. In the **Password** field, specify a password for your database user. Make a note of this password for use in a later step of this quickstart.
  6. Click **Add**.



### gcloud

Before running the following command, make the following replacements:

  1. PASSWORD with a password for your database user. Make a note of this for use in a later step of this quickstart. 



Run the [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command to create the user.
    
    
    gcloud sql users create quickstart-user \
    --instance=quickstart-instance \
    --password=PASSWORD

Username length limits are the same for Cloud SQL as for on-premises MySQL; 32 characters for MySQL 8.0 and later, 16 characters for earlier versions. 

## Deploy a sample app to App Engine flexible environment

### Create an App Engine app

Create an App Engine app in your Google Cloud project. This enables the App Engine service, creates a default App Engine app, and creates an App Engine service account that you use to connect to Cloud SQL. **Note:** You create an App Engine app only once per Google Cloud project. 

### Console

  1. In the Google Cloud console, go to the **App Engine** page.

[Go to App Engine](https://console.cloud.google.com/appengine)

  2. Click **Create application**.
  3. From the **Select a region** drop-down menu, select **us-central**.
  4. Click **Next**.
  5. After the **Get started** page appears, scroll to the bottom of the page.
  6. Click the **I'll do this later** link.



### gcloud

  1. Run the following [`gcloud app create`](https://docs.cloud.google.com/sdk/gcloud/reference/app/create) command to create an App Engine app: 
    
    gcloud app create

  2. When prompted to choose the region where you want your App Engine app located, enter the numeric choice for **us-central**.



### Configure the App Engine service account

Configure the service account used by App Engine so that it has the **Cloud SQL Client** role. By assigning the role to the service account, the account has permissions to connect to Cloud SQL. 

### Console

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. For the service account named **App Engine default service account** , click the pencil icon. **Note:** The name of the service account appears next to the principal for the account. The name of the principal is project-name@appspot.gserviceaccount.com. 
  3. Click **Add another role**.
  4. Add the **Role** named **Cloud SQL Client**.
  5. Click **Save**.



### gcloud

  1. Run the following `gcloud` command to get a list of your project's service accounts: 
         
         gcloud iam service-accounts list

  2. Copy the **EMAIL** of the **App Engine service account**.
  3. Run the following command to add the **Cloud SQL Client** role to **App Engine service account** : 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
           --role="roles/cloudsql.client"




### Configure and deploy a sample app for Cloud SQL

Now that you created a Cloud SQL instance and database, and you configured the App Engine service account so that it has permissions to connect to Cloud SQL, you can configure and deploy a sample app to connect to your Cloud SQL instance.

#### Public IP

For public IP paths, App Engine flexible environment provides encryption. This method uses a Unix socket and the Cloud SQL Auth Proxy to connect to your Cloud SQL instance. 

### Go

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/golang-samples&working_dir=cloudsql/mysql/database-sql)
  2. In the **Open in Cloud Shell** dialog box, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  5. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  6. Navigate to and open the `cloudshell_open/golang-samples/cloudsql/mysql/database-sql/app.flexible.yaml` file.
  7. Replace the placeholders for the environment variables in the `app.flexible.yaml` file with the following values: 
     * **< PROJECT-ID>** with your project ID.
     * **< INSTANCE-REGION>** with `us-central1`.
     * **< INSTANCE-NAME>** with `quickstart-instance`.
     * **< YOUR_DB_USER_NAME>** with `quickstart-user`.
     * **< YOUR_DB_PASSWORD>** with the password of the `quickstart-user` that you created in **Create a user**.
     * **< YOUR_DB_NAME>** with `quickstart-db`.
  8. At the Cloud Shell command prompt, in the `cloudshell_open/golang-samples/cloudsql/mysql/database-sql` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  9. When prompted with **Do you want to continue?** , enter `Y`.
  10. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  11. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Java

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=cloud-sql/mysql/servlet)
  2. In the **Open in Cloud Shell** dialog box, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  5. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  6. Navigate to and open the `cloudshell_open/java-docs-samples/cloud-sql/mysql/servlet/src/main/webapp/WEB-INF/appengine-web.xml` file.
  7. Replace the placeholders for the environment variables in the `appengine-web.xml` file with the following values: 
     * **my-project:region:instance** with your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **my-db-user** with `quickstart-user`.
     * **my-db-password** with the password of the `quickstart-user` that you created in **Create a user**.
     * **my_db** with `quickstart-db`.
  8. At the Cloud Shell command prompt, in the `cloudshell_open/java-docs-samples/cloud-sql/mysql/servlet` directory, run the following [Apache Maven](https://maven.apache.org/) `mvn clean package` command to deploy the sample app to App Engine flexible environment.
    
    mvn clean package appengine:deploy -DskipTests

  9. When prompted with **Do you want to continue?** , enter `Y`.
  10. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  11. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Node.js

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-docs-samples&working_dir=cloud-sql/mysql/mysql)
  2. In the **Open in Cloud Shell** dialog box, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  5. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  6. Navigate to and open the `cloudshell_open/nodejs-docs-samples/cloud-sql/mysql/mysql/app.flexible.yaml` file.
  7. Replace the placeholders for the environment variables in the `app.flexible.yaml` file with the following values: 
     * **< MY-PROJECT>** with your project ID.
     * **< INSTANCE-REGION>** with `us-central1`.
     * **< INSTANCE-NAME>** with `quickstart-instance`.
     * **MY_DB_USER** with `quickstart-user`.
     * **MY_DB_PASSWORD** with the password of the `quickstart-user` that you created in **Create a user**.
     * **MY_DATABASE** with `quickstart-db`.
  8. At the Cloud Shell command prompt, in the `cloudshell_open/nodejs-docs-samples/cloud-sql/mysql/mysql` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  9. When prompted with **Do you want to continue?** , enter `Y`.
  10. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  11. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Python

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&working_dir=cloud-sql/mysql/sqlalchemy)
  2. In the **Open in Cloud Shell** dialog box, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  5. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  6. Navigate to and open the `cloudshell_open/python-docs-samples/cloud-sql/mysql/sqlalchemy/app.flexible.yaml` file.
  7. Replace the placeholders for the environment variables in the `app.flexible.yaml` file with the following values: 
     * **< PROJECT-ID>** with your project ID.
     * **< INSTANCE-REGION>** with `quickstart-instance`.
     * **< YOUR_DB_USER_NAME>** with `quickstart-user`.
     * **< YOUR_DB_PASSWORD>** with the password of the `quickstart-user` that you created in **Create a user**.
     * **< YOUR_DB_NAME>** with `quickstart-db`.
  8. At the Cloud Shell command prompt, in the `cloudshell_open/python-docs-samples/cloud-sql/mysql/sqlalchemy` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  9. When prompted with **Do you want to continue?** , enter `Y`.
  10. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  11. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




#### Private IP

For private IP paths, make sure your App Engine flexible environment VM and the Cloud SQL instance are hosted on the same Virtual Private Cloud (VPC) network. When located on the same VPC network, your App Engine flexible environment app can connect directly to the Cloud SQL instance without using the Cloud SQL Auth Proxy. 

### Go

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build a sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/golang-samples&working_dir=cloudsql/mysql/database-sql)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  5. Upload SSL certs files to the **certs** folder. 
     1. From the Explorer navigation menu of Cloud Shell Editor, navigate to the `golang-samples/cloudsql/mysql/database-sql/certs` folder.
     2. Right-click the **certs** folder in Cloud Shell Editor and select **Upload Files**.
     3. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     4. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  6. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  7. Navigate to and open the `cloudshell_open/golang-samples/cloudsql/mysql/database-sql/app.flexible.yaml` file.
  8. Copy and paste the following code into the file, replacing the existing file content: 
    
    runtime: custom
    env: flex
    
    env_variables:
      DB_USER: quickstart-user
      DB_PASS: YOUR_DB_PASSWORD
      DB_NAME: quickstart-db
      DB_PORT: 3306
      INSTANCE_HOST: INSTANCE_HOST
      DB_ROOT_CERT: certs/server-ca.pem
      DB_CERT: certs/client-cert.pem
      DB_KEY: certs/client-key.pem
      PRIVATE_IP: TRUE
    
    vpc_access_connector:
      name: projects/PROJECT_ID/locations/us-central1/connectors/quickstart-connector

  9. Make the following variable replacements:
     * **YOUR_DB_PASSWORD** with the password of the `quickstart-user` that you created in **Create a user**.
     * **INSTANCE_HOST** with your instance's **Private IP address** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **PROJECT_ID** with your project ID.
  10. At the Cloud Shell command prompt, in the `cloudshell_open/golang-samples/cloudsql/mysql/database-sql` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  11. When prompted with **Do you want to continue?** , enter `Y`.
  12. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  13. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Java

####  Create and download SSL server and client certificates 

For Java users, the connector already provides a secure connection so that creating and downloading SSL server and client certificates is unnecessary. 

####  Build sample app 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=cloud-sql/mysql/servlet)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  5. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  6. Navigate to and open the `cloudshell_open/java-docs-samples/cloud-sql/mysql/servlet/src/main/webapp/WEB-INF/appengine-web.xml` file.
  7. Copy and paste the following code into the `appengine-web.xml` file, replacing the existing file content: 
    
    <runtime>java17</runtime>
      <env-variables>
        <env-var name="INSTANCE_CONNECTION_NAME" value="project-name:region-name:instance-name" />
        <env-var name="DB_PORT" value="3306" />
        <env-var name="DB_USER" value="quickstart-user" />
        <env-var name="DB_PASS" value="my-db-password" />
        <env-var name="DB_NAME" value="quickstart-db" />
      </env-variables>
    <vpc-access-connector>
      <name>projects/PROJECT_ID/locations/us-central1/connectors/quickstart-connector</name>
      <egress-setting>all-traffic</egress-setting>
    </vpc-access-connector>

  8. Make the following variable replacements:
     * **project-name:region-name:instance-name** with your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **my-db-password** with the password of the `quickstart-user` that you created in **Create a user**.
     * **PROJECT_ID** with your project ID.
  9. At the Cloud Shell command prompt, in the `cloudshell_open/java-docs-samples/cloud-sql/mysql/servlet` directory, run the following [Apache Maven](https://maven.apache.org/) `mvn clean package` command to deploy the sample app to App Engine flexible environment.
    
    mvn clean package appengine:deploy -DskipTests

  10. When prompted with **Do you want to continue?** , enter `Y`.
  11. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  12. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Node.js

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-docs-samples&working_dir=cloud-sql/mysql/mysql)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  5. Upload SSL certs files to **certs** folder. 
     1. From the Explorer navigation menu of Cloud Shell Editor, navigate to the `nodejs-docs-samples/cloud-sql/mysql/mysql/certs` folder.
     2. Right-click **certs** folder in Cloud Shell Editor and select **Upload Files**
     3. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     4. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  6. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  7. Navigate to and open the `cloudshell_open/nodejs-docs-samples/cloud-sql/mysql/mysql/app.flexible.yaml` file.
  8. Copy and paste the following code into the file, replacing the existing file content: 
    
    runtime: nodejs
    env: flex
    
    env_variables:
      DB_USER: quickstart-user
      DB_PASS: MY_DB_PASSWORD
      DB_NAME: quickstart-db
      DB_PORT: 3306
      INSTANCE_HOST: INSTANCE_HOST
      DB_ROOT_CERT: certs/server-ca.pem
      DB_CERT: certs/client-cert.pem
      DB_KEY: certs/client-key.pem
      PRIVATE_IP: TRUE
    
    vpc_access_connector:
      name: projects/PROJECT_ID/locations/us-central1/connectors/quickstart-connector

  9. Make the following variable replacements:
     * **MY_DB_PASSWORD** with the password of the `quickstart-user` that you created in **Create a user**.
     * **INSTANCE_HOST** with your instance's **Private IP address** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **PROJECT_ID** with your project ID.
  10. At the Cloud Shell command prompt, in the `cloudshell_open/nodejs-docs-samples/cloud-sql/mysql/mysql` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  11. When prompted with **Do you want to continue?** , enter `Y`.
  12. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  13. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Python

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&working_dir=cloud-sql/mysql/sqlalchemy)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. At the Cloud Shell command prompt, run the following command to activate your project: 
         
         gcloud config set project YOUR-PROJECT-ID

**Note:** Replace YOUR-PROJECT-ID with your project ID.
  4. If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  5. Upload SSL certs files to **certs** folder. 
     1. From the Explorer navigation menu of Cloud Shell Editor, navigate to the `python-docs-samples/cloud-sql/mysql/sqlalchemy/certs` folder.
     2. Right-click **certs** folder in Cloud Shell Editor and select **Upload Files**
     3. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     4. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  6. From the **Explorer** navigation menu of Cloud Shell Editor, click the expandable node that's the username of your Google Cloud account.
  7. Navigate to and open the `cloudshell_open/python-docs-samples/cloud-sql/mysql/sqlalchemy/app.flexible.yaml` file.
  8. Copy and paste the following code into the file, replacing the existing file content: 
    
    runtime: custom
    env: flex
    entrypoint: gunicorn -b :$PORT app:app
    
    env_variables:
      DB_USER: quickstart-user
      DB_PASS: YOUR_DB_PASSWORD
      DB_NAME: quickstart-db
      DB_PORT: 3306
      INSTANCE_HOST: INSTANCE_HOST
      DB_ROOT_CERT: certs/server-ca.pem
      DB_CERT: certs/client-cert.pem
      DB_KEY: certs/client-key.pem
      PRIVATE_IP: TRUE
    
    vpc_access_connector:
      name: projects/PROJECT_ID/locations/us-central1/connectors/quickstart-connector

  9. Make the following variable replacements:
     * **YOUR_DB_PASSWORD** with the password of the `quickstart-user` that you created in **Create a user**.
     * **INSTANCE_HOST** with your instance's **Private IP address** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **PROJECT_ID** with your project ID.
  10. At the Cloud Shell command prompt, in the `cloudshell_open/python-docs-samples/cloud-sql/mysql/sqlalchemy` directory, run the following [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command to deploy the sample app to App Engine flexible environment.
    
    gcloud app deploy app.flexible.yaml

  11. When prompted with **Do you want to continue?** , enter `Y`.
  12. After the actions performed by running the `gcloud app deploy` command complete, run the [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse) command:
    
    gcloud app browse

  13. Click the generated link to see the sample app running on App Engine flexible environment. This environment is connected to Cloud SQL.

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the `quickstart-instance` instance to open the **Instance details** page.
  3. In the icon bar at the top of the page, click **Delete**.
  4. In the **Delete instance** dialog box, type `quickstart-instance`, and then click **Delete** to delete the instance. Disabling your app stops it from running instances and serving requests. If your app is processing a request, your app completes the request before being disabled.



To disable an App Engine app and retain its data, do the following:

  1. In the Google Cloud console, go to the **Settings** page:

[Go to Settings](https://console.cloud.google.com/appengine/settings)

  2. In the **Application settings** tab, click **Disable application**.

  3. In the **App ID** field, enter the ID of the app you want to disable, and then click **Disable**. 




### Optional cleanup steps

If you're not using the **Cloud SQL client** role that you assigned to the Compute Engine service account, you can remove it.

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the edit icon (which looks like a pencil) for the IAM account named **Compute Engine default service account**.
  3. Delete the **Cloud SQL client** role.
  4. Click **Save**.



If you're not using the APIs that were enabled as part of this quickstart, you can disable them.

  * APIs that were enabled within this quickstart: 
    * Compute Engine API
    * Cloud SQL Admin API
    * Cloud Run API
    * Container Registry API
    * Cloud Build API


  1. In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

  2. Select any API that you would like to disable and then click the **Disable API** button.




## What's next

Based on your needs, you can learn more about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance). 

You also can learn about creating [MySQL users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) and [databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#create) for your Cloud SQL instance.

For more information about pricing, see [Cloud SQL for MySQL pricing](https://cloud.google.com/sql/pricing).

Learn more about:

  * Configuring your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) address.
  * Configuring your Cloud SQL instance with a [private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) address.



Additionally, you can learn about connecting to a Cloud SQL instance from other Google Cloud products:

  * [From an app running on App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine)
  * [From an app running on Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)
  * [From an app running on GKE](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine)
  * [From Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
