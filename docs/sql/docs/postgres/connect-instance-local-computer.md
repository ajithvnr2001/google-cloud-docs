---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-local-computer/
title: Quickstart: Connect to Cloud SQL for PostgreSQL from your local computer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:10.463605+00:00
---

# Quickstart: Connect to Cloud SQL for PostgreSQL from your local computer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-local-computer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for PostgreSQL from your local computer

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-local-computer "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-local-computer "View this page for the SQL Server database engine")

Learn how to deploy a sample app on your Linux, macOS, or Windows-based local computer connected to a PostgreSQL instance by using the Google Cloud console and a client application.

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

  6. Verify that you have the permissions required to complete this quickstart.
  7. Enable the Cloud APIs necessary to run a Cloud SQL sample app on your local computer. 

### Console

Click the **Enable APIs** button to enable the APIs required for this quickstart.

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,iam.googleapis.com)

This enables the following APIs:

     * Cloud SQL Admin API
     * IAM API

### gcloud

[Install the ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) which provides command-line access to your Google Cloud resources. The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) is used to run the `gcloud CLI` commands presented throughout this quickstart. All the commands are formatted to be run in a Linux/macOS terminal or in Windows Powershell.

Open the terminal and run the following `gcloud` command:
    
    gcloud services enable sqladmin.googleapis.com iam.googleapis.com

This command enables the following APIs:

     * Cloud SQL Admin API
     * IAM API




### Required roles

To get the permissions that you need to set up Cloud SQL from your local computer, ask your administrator to grant you the following IAM roles on the project that you want to create and connect to: 

  * Create or delete an instance, database, and user: Cloud SQL administrator role (`roles/cloudsql.admin`). 
  * Create or delete an IAM service account: IAM Service Account administrator role (`roles/iam.serviceAccountAdmin`). 
  * Add or remove an IAM policy binding: Project IAM administrator role (`roles/resourcemanager.projectIamAdmin`). 
  * Create, manage and rotate service account keys: Service Account Key Admin (roles/iam.serviceAccountKeyAdmin). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up Cloud SQL

To create an Cloud SQL instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the PostgreSQL tab and click **Create Sandbox instance** in the **Sandbox** box. Alternatively, you can click**Create Instance** and complete the following steps:
     1. Click **Choose PostgreSQL**.
     2. Select the **Enterprise** edition.
     3. Choose the **Sandbox** preset.
  3. If you're prompted to enable the **Compute API** , click the **Enable API** button.
  4. In the **Instance info** section, enter `quickstart-instance` as the **Instance ID**.
  5. Enter a password for the postgres user. Take note of the password you create, because you'll need it later.
  6. In the **Choose region and zonal availability** section, select the **Single zone** option.
  7. Click **Create instance**.



### Create a database

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select `quickstart-instance`.
  3. Open the **Databases** tab.
  4. Click **Create database**.
     1. In the **New database** dialog box, enter `quickstart_db` as the name of the database.  

     2. Click **Create**.



### gcloud

Run the [`gcloud sql databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/create) command to create a database.
    
    
    gcloud sql databases create quickstart_db --instance=quickstart-instance

### Create a user

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the **SQL** navigation menu.
  4. Click **Add user account**. 
  5. On the **Add a user account to instance _instance_name_** page, add the following information: 
     * In the **Username** field, enter `quickstart-user`
     * In the **Password** field, specify a password for your database user. Make a note of this for use in a later step of this quickstart.
  6. Click **Add**.



### gcloud

Replace the following:

  1. PASSWORD with a password for your database user. Make a note of this for use in a later step of this quickstart. 



Run the [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command to create the user.
    
    
    gcloud sql users create quickstart-user --instance=quickstart-instance --password=PASSWORD

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

## Set up a service account

Create and configure a Google Cloud service account that has the **Cloud SQL Client** role with permissions to connect to Cloud SQL. After you create a service account, you might need to wait for 60 seconds or more before you use the service account. 

### Console

#### Create a service account

  1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create)

  2. Select a Google Cloud project.
  3. Enter a `quickstart-service-account` as the service account name.
  4. Optional: Enter a description of the service account.
  5. Click **Create and continue** and continue to the next step.
  6. Choose the Cloud SQL Client role to grant to the service account on the project.
  7. Click **Continue**.
  8. Click **Done** to finish creating the service account.



#### Create and download the service account key file

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.
  3. Click the email address of the `quickstart-service-account` service account that you want to create a key for.
  4. Click the **Keys** tab.
  5. Click the **Add key** drop-down menu, then select **Create new key**.
  6. Select **JSON** as the **Key type** and click **Create**.



Clicking **Create** downloads a service account key file. After you download the key file, you cannot download it again.

Make sure to store the key file securely, because it can be used to authenticate as your service account. You can move and rename this file however you would like.

### gcloud

#### Create a service account

  1. To create the service account, run the [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command:
    
    gcloud iam service-accounts create quickstart-service-account --description="DESCRIPTION" --display-name="quickstart-service-account"

Replace the following value:

     * `DESCRIPTION`: An optional description of the service account
  2. To grant your service account the Cloud SQL Client role on your project, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. Replace PROJECT_ID with your Google Cloud project ID: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:quickstart-service-account@PROJECT_ID.iam.gserviceaccount.com" --role="roles/cloudsql.client"




#### Create and download the service account key file

To use the service account you just created from your local computer you need a service account key file to authenticate the sample application as the service account. To create and download the service account key file, run the [`gcloud iam service-accounts keys create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create) command:
    
    
    gcloud iam service-accounts keys create KEY_FILE --iam-account=quickstart-service-account@PROJECT_ID.iam.gserviceaccount.com

Replace the following values:

  * `KEY_FILE`: The path to a new output file for the private key — for example, `~/sa-private-key.json`. 
  * `PROJECT_ID`: Your Google Cloud project ID. 



The service account key file is now downloaded to your local computer. After you download the key file, you cannot download it again.

Make sure to store the key file securely, because anyone can use it to authenticate as your service account. You can move and rename this file however you would like.

## Setup development environment for programming language

Set up your local computer's development environment for your preferred programming language.

### Go

Complete the following steps to set up your development environment to run the Go sample app. 

  1. Go to the [setup guide for a Go development environment](https://docs.cloud.google.com/go/docs/setup). 
  2. Complete the instructions in the **Install Go** section. 



### Java

Complete the following steps to set up your development environment to run the Java sample app. 

  1. Go to the [setup guide for a Java development environment](https://docs.cloud.google.com/java/docs/setup). 
  2. Complete the instructions in the **Install a JDK (Java Development Kit)** section. 
  3. Complete the instructions in the **Install a build automation tool** to set up Apache Maven. 



### Node.js

Complete the following steps to set up your development environment to run the Node.js sample app. 

  1. Go to [setup guide for a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup). 
  2. Complete the instructions in the **Installing Node.js and npm** section. 



### Python

Complete the following steps to set up your development environment to run the Python sample app. 

  1. Go to [setup guide for a Python development environment](https://docs.cloud.google.com/python/docs/setup). 
  2. Complete the instructions in the **Installing Python** section. 



## Install Git

Install [Git](https://git-scm.com/), an open source version control system. 

#### Linux

Follow the official [Git installation documentation for Linux](https://git-scm.com/download/linux). 

#### macOS

Follow the official [Git installation documentation for macOS](https://git-scm.com/download/mac). 

#### Windows

Follow the official [Git installation documentation for Windows](https://git-scm.com/download/win). 

## Clone a sample app

Clone a sample app to your local computer using the [`git clone`](https://git-scm.com/docs/git-clone) command.

### Go

Run the following commands to clone the Go sample app to your local computer and change directory to the directory containing the sample app. 

  1. Clone the sample app. 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples

  2. Change directory to the directory containing the sample app. 
         
         cd golang-samples/cloudsql/postgres/database-sql




### Java

Run the following commands to clone the Java sample app to your local computer and change directory to the directory containing the sample app. 

  1. Clone the sample app. 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples

  2. Change directory to the directory containing the sample app. 
         
         cd java-docs-samples/cloud-sql/postgres/servlet




### Node.js

Run the following commands to clone the Node.js sample app to your local computer and change directory to the directory containing the sample app. 

  1. Clone the sample app. 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples

  2. Change directory to the directory containing the sample app. 
         
         cd nodejs-docs-samples/cloud-sql/postgres/knex




### Python

Run the following commands to clone the Python sample app to your local computer and change directory to the directory containing the sample app. 

  1. Clone the sample app. 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples

  2. Change directory to the directory containing the sample app. 
         
         cd python-docs-samples/cloud-sql/postgres/sqlalchemy




## Configure and run sample app

Configure and run the sample app. 

#### Linux/macOS

### Go

Open the terminal and run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `/path/to/service/account/key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    export GOOGLE_APPLICATION_CREDENTIALS=CREDENTIALS_JSON_FILE
    export INSTANCE_CONNECTION_NAME='INSTANCE_CONNECTION_NAME'
    export DB_PORT='5432'
    export DB_NAME='quickstart_db'
    export DB_USER='quickstart-user'
    export DB_PASS='YOUR_DB_PASSWORD'

Run the following commands to get the Go sample app's dependencies on your local computer and run the sample app. 

  1. Get the dependencies required to run the sample app. 
         
         go get ./...

  2. Run the sample app. 
         
         go run cmd/app/main.go

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the terminal window where you started the sample app. 



### Java

Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `/path/to/service/account/key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    export GOOGLE_APPLICATION_CREDENTIALS=CREDENTIALS_JSON_FILE
    export INSTANCE_CONNECTION_NAME='INSTANCE_CONNECTION_NAME'
    export DB_PORT='5432'
    export DB_NAME='quickstart_db'
    export DB_USER='quickstart-user'
    export DB_PASS='YOUR_DB_PASSWORD'

  1. Run the following command to get the Java sample app's dependencies on your local computer and run the sample app. 
         
         mvn jetty:run

  2. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  3. To stop the sample app, press `Control+C` in the terminal window where you started the sample app. 



### Node.js

  1. Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

     * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `/path/to/service/account/key.json`.
     * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.
    
    export GOOGLE_APPLICATION_CREDENTIALS=CREDENTIALS_JSON_FILE
    export INSTANCE_HOST='127.0.0.1'
    export DB_PORT='5432'
    export DB_NAME='quickstart_db'
    export DB_USER='quickstart-user'
    export DB_PASS='YOUR_DB_PASSWORD'

  2. Download the Cloud SQL Auth Proxy. 
         
         curl -o cloud-sql-proxy \
         https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.0.0/cloud-sql-proxy.linux.amd64

  3. Run the Cloud SQL Auth Proxy as a background process. Replace INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page. 
         
         ./cloud-sql-proxy \
         --credentials-file $GOOGLE_APPLICATION_CREDENTIALS \
         INSTANCE_CONNECTION_NAME &


**Note:** The process running the Cloud SQL Auth Proxy in the background can be stopped using the `fg` command in your Terminal window where you started the sample app. This should bring the running Cloud SQL Auth Proxy job to the terminal foreground. Then press `Control+C` to stop the proxy job. 

Run the following commands to get the required Node.js packages on to your local computer and run the sample app. 

  1. Install the Node.js packages necessary to run the app locally. 
         
         npm install

  2. Run the sample app. 
         
         npm start

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the terminal window where you started the sample app. 



### Python

Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `/path/to/service/account/key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    export GOOGLE_APPLICATION_CREDENTIALS=CREDENTIALS_JSON_FILE
    export INSTANCE_CONNECTION_NAME='INSTANCE_CONNECTION_NAME'
    export DB_PORT='5432'
    export DB_NAME='quickstart_db'
    export DB_USER='quickstart-user'
    export DB_PASS='YOUR_DB_PASSWORD'

Run the following commands to get the Python sample app's requirements on to your local computer and run the sample app. 

  1. Initialize a virtual environment and install the requirements to run the sample app. 
         
         python3 -m venv env
         source env/bin/activate
         pip install -r requirements.txt

  2. Run the sample app. 
         
         python app.py

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the terminal window where you started the sample app. 



#### Windows

### Go

Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `C:\Users\Your-Username\Downloads\key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="CREDENTIALS_JSON_FILE"
    $env:INSTANCE_CONNECTION_NAME="INSTANCE_CONNECTION_NAME"
    $env:DB_PORT="5432"
    $env:DB_NAME="quickstart_db"
    $env:DB_USER="quickstart-user"
    $env:DB_PASS="YOUR_DB_PASSWORD"

Run the following commands to get the Go sample app's dependencies on your local computer and run the sample app. 

  1. Get the dependencies required to run the sample app. 
         
         go get ./...

  2. Run the sample app. 
         
         go run cmd\app\main.go

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the Powershell window where you started the sample app. 



### Java

Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `C:\Users\Your-Username\Downloads\key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="CREDENTIALS_JSON_FILE"
    $env:INSTANCE_CONNECTION_NAME="INSTANCE_CONNECTION_NAME"
    $env:DB_PORT="5432"
    $env:DB_NAME="quickstart_db"
    $env:DB_USER="quickstart-user"
    $env:DB_PASS="YOUR_DB_PASSWORD"

  1. Run the following command to get the Java sample app's dependencies on your local computer and run the sample app. 
         
         mvn jetty:run

  2. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  3. To stop the sample app, press `Control+C` in the Powershell window where you started the sample app. 



### Node.js

  1. Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

     * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `C:\Users\Your-Username\Downloads\key.json`.
     * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="CREDENTIALS_JSON_FILE"
    $env:INSTANCE_HOST="127.0.0.1"
    $env:DB_PORT="5432"
    $env:DB_NAME="quickstart_db"
    $env:DB_USER="quickstart-user"
    $env:DB_PASS="YOUR_DB_PASSWORD"

  2. Download the Cloud SQL Auth Proxy. 
         
         wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.0.0/cloud-sql-proxy.x64.exe 
         -O cloud-sql-proxy.exe

  3. Run the Cloud SQL Auth Proxy as a background process. Replace INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page. 
         
         Start-Process -filepath  ".\cloud-sql-proxy.exe" -ArgumentList `
         "--credentials-file $env:GOOGLE_APPLICATION_CREDENTIALS" INSTANCE_CONNECTION_NAME


**Note:** The process running the Cloud SQL Auth Proxy in the background can be stopped by selecting the **cmd.exe** window that was spawned by the `Start-Process` command. Close the window to stop the proxy job. 

Run the following commands to get the required Node.js packages on your local computer and run the sample app. 

  1. Install the Node.js packages necessary to run the app locally. 
         
         npm install

  2. Run the sample app. 
         
         npm start

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the Powershell window where you started the sample app. 



### Python

Run the following commands to initialize environment variables required to run the sample app. Before running the commands, make the following replacements: 

  * CREDENTIALS_JSON_FILE with the file path of your service account's JSON credentials key file using a format like `C:\Users\Your-Username\Downloads\key.json`.
  * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the Cloud SQL instance **Overview** page.
  * YOUR_DB_PASSWORD with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.


    
    
    $env:GOOGLE_APPLICATION_CREDENTIALS="CREDENTIALS_JSON_FILE"
    $env:INSTANCE_CONNECTION_NAME="INSTANCE_CONNECTION_NAME"
    $env:DB_PORT="5432"
    $env:DB_NAME="quickstart_db"
    $env:DB_USER="quickstart-user"
    $env:DB_PASS="YOUR_DB_PASSWORD"

Run the following commands to get the Python sample app's requirements on your local computer and run the sample app. 

  1. Initialize a virtual environment and install the requirements to run the sample app. 
         
         virtualenv --python python3 env
         .\env\Scripts\activate
         pip install -r requirements.txt

  2. Run the sample app. 
         
         python app.py

  3. View the running sample app. Open a browser window and go to `http://127.0.0.1:8080`. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)

  4. To stop the sample app, press `Control+C` in the Powershell window where you started the sample app. 



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the `quickstart-instance` instance to open the **Instance details** page.
  3. In the icon bar at the top of the page, click **Delete**.
  4. In the **Delete instance** dialog box, type `quickstart-instance`, and then click **Delete** to delete the instance.



### Optional cleanup steps

If you're not using the **Cloud SQL client** role that you assigned to the `quickstart-service-account` service account, you can remove it.

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the edit icon (which looks like a pencil) for the IAM account named **quickstart-service-account**.
  3. Delete the **Cloud SQL client** role.
  4. Click **Save**.



If you're not using the APIs that were enabled as part of this quickstart, you can disable them.

  * APIs that were enabled within this quickstart: 
    * Cloud SQL Admin API
    * Identity and Access Management API


  1. In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

  2. Select any API that you would like to disable and then click the **Disable API** button.




## What's next

Based on your needs, you can learn more about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance). 

You also can learn about creating [PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) and [databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create) for your Cloud SQL instance.

For more information about pricing, see [Cloud SQL for PostgreSQL pricing](https://cloud.google.com/sql/pricing).

Learn more about:

  * Configuring your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) address.
  * Configuring your Cloud SQL instance with a [private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) address.



Additionally, you can learn about connecting to a Cloud SQL instance from other Google Cloud applications:

  * [From an application running on App Engine standard environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine)
  * [From an application running on Compute Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine)
  * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)
  * [From Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
