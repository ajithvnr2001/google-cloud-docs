---
url: https://docs.cloud.google.com/ruby/rails/run/
title: Running Rails on the Cloud Run environment \u00a0|\u00a0 Ruby \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:12.540635+00:00
---

# Running Rails on the Cloud Run environment  |  Ruby  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/rails/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Guides ](https://docs.cloud.google.com/ruby/docs/setup)



Send feedback 

#  Running Rails on the Cloud Run environment Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to deploy a sample Rails application to Cloud Run and how to integrate managed databases, object storage, encrypted secrets, and build pipelines with serverless compute.

Deploying Rails applications involves integrating multiple services together to form a cohesive project. This tutorial assumes that you are familiar with Rails web development.

This tutorial requires [Ruby 3.0 or later](https://www.ruby-lang.org/) and [Rails 8 or later](https://rubyonrails.org).

![Diagram showing the architecture of the deployment.](https://docs.cloud.google.com/static/ruby/rails/images/rails-cloud-run.png) The Rails site is served from Cloud Run, which uses multiple backing services to store different data types (relational database information, media assets, configuration secrets, and container images). The backend services are updated by Cloud Build as part of a build and migrate task. 

## Objectives

  * Create and connect a Cloud SQL database to Active Record
  * Create and use Secret Manager to store and access a Rails master key securely
  * Host user-uploaded media and files on Cloud Storage from Active Storage
  * Use Cloud Build to automate build and database migrations
  * Deploy a Rails app to Cloud Run



## Costs

**Important:** In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)
  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Secret Manager](https://cloud.google.com/secret-manager/pricing)

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Run, Cloud SQL, Cloud Build, Secret Manager, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,secretmanager.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Run, Cloud SQL, Cloud Build, Secret Manager, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,secretmanager.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  14. Ensure sufficient permissions are available to the account used for this tutorial. **Note:** In cases where the Owner role can't be used, you need the following roles that contain the minimum permissions required to complete this tutorial: 
     * Cloud SQL Admin 
     * Cloud Storage Admin
     * Cloud Run Admin
     * Secret Manager Admin



## Prepare your environment

This tutorial uses several Google Cloud services to provide the database, media storage, and secret storage that support the deployed Rails application. Prepare your environment by configuring a region to deploy the services in and by cloning the Rails app.

### Set the default project and region

  1. Set the default project configuration for the gcloud CLI by running the following command:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID

  2. Configure your region:
         
         export REGION=REGION
         

Replace `REGION` with an appropriate location. For efficiency between services, all services should be deployed in the same region. For more information about the closest region to you, see [Products available by location](https://cloud.google.com/about/locations#products-available-by-location).




### Clone the Rails app

The code for the Rails sample app is in the [`GoogleCloudPlatform/ruby-docs-samples`](https://github.com/GoogleCloudPlatform/ruby-docs-samples) repository on GitHub.

  1. Clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples.git
         

  2. Go to the directory that contains the sample code and run the following commands to make sure that the application is properly set up with the required gems and dependencies:

### Linux/macOS
         
         cd ruby-docs-samples/run/rails
         bundle install
         

### Windows
         
         cd ruby-docs-samples\run\rails
         bundle install
         




## Prepare the backing services

This tutorial uses a number of Google Cloud services to provide the database, media storage, and secret storage that support the deployed Rails project. These services are deployed in a specific region. For efficiency between services, it is best that all services are deployed in the same region. For more information about the closest region to you, see [Products available by location](https://cloud.google.com/about/locations#products-available-by-location).

### Set up a Cloud SQL for PostgreSQL instance

Rails supports multiple relational databases, including several offered by Cloud SQL. This tutorial uses PostgreSQL, an open source database commonly used by Rails apps.

The following sections describe the creation of a PostgreSQL instance, database, and database user for your Rails app.

#### Create a PostgreSQL instance

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances?project=_)

  2. Click **Create Instance**.

  3. Click **Choose PostgreSQL**.

  4. In the **Instance ID** field, enter a name for the instance (`INSTANCE_NAME`).

  5. In the **Password** field, enter a password for the postgres user.

  6. Use the default values for the other fields.

  7. Click **Create Instance**.




### gcloud

  * Create the PostgreSQL instance:
        
        gcloud sql instances create INSTANCE_NAME \
            --database-version POSTGRES_12 \
            --tier db-f1-micro \
            --region REGION
        

Replace the following:

    * `INSTANCE_NAME`: your new Cloud SQL instance name

    * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/run/docs/locations)

It takes a few minutes to create the instance and for it to be ready for use.




#### Create a database

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances?project=_)

  2. Select the INSTANCE_NAME instance.

  3. Go to the **Databases** tab.

  4. Click **Create database**.

  5. In the **Database name** dialog, enter `DATABASE_NAME`.

  6. Click **Create**.




### gcloud

  * Create the database within the recently created instance:
        
        gcloud sql databases create DATABASE_NAME \
            --instance INSTANCE_NAME
        

Replace `DATABASE_NAME` with a name for the database inside the instance.




#### Create a user

Generate a random password for the database user, and write it to a file called `dbpassword`:
    
    
    cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1 > dbpassword
    

### Console

**Note:** Any users that are created by using Cloud SQL have the privileges associated with the [`cloudsqlsuperuser` role](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users): `CREATEROLE`, `CREATEDB`, and `LOGIN`.

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances?project=_)

  2. Select the INSTANCE_NAME instance.

  3. Go to the **Users** tab.

  4. Click **Add User Account**.

  5. Under the **Built-in Authentication** dialog:

     1. Enter the username `DATABASE_USERNAME`.
     2. Enter the content of the `dbpassword` file as the password `PASSWORD`.
  6. Click **Add**.




### gcloud

**Note:** Any users that are created by using Cloud SQL have the privileges associated with the [`cloudsqlsuperuser` role](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users): `CREATEROLE`, `CREATEDB`, and `LOGIN`.

  * Create the user within the recently created instance and set its password to be the content of dbpassword:
        
        gcloud sql users create DATABASE_USERNAME \
           --instance=INSTANCE_NAME --password=$(cat dbpassword)
        

Replace `DATABASE_USERNAME` with a name for the user inside the instance.




### Set up an Artifact Registry repository

Use Artifact Registry to create a repository to store your container image.

**Note:** This repository is automatically created when using [Cloud Run Source Deploys](https://docs.cloud.google.com/run/docs/deploying-source-code), and might already exist in your project.

### Console

  1. In the Google Cloud console, go to the **Artifact Registry** page.

[Go to Artifact Registry](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Enter the following:

     * For **Name** , enter "cloud-run-source-deploy".
     * For **Format** , select "Docker".
     * For **Region** , select REGION.
  4. Keep the default values for the other fields.

  5. Click **Create**.




### gcloud

  * Create an Artifact Registry repository:
        
        gcloud artifacts repositories create cloud-run-source-deploy \
            --repository-format docker \
            --location REGION
        




### Set up a Cloud Storage bucket

You can host Rails static assets and user-uploaded media in highly available object storage using Cloud Storage.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**. 
  3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. For **Location** , select the following: us-central1 
     3. In the **Choose how to store your data** section, do the following: 
        1. In the **Set a default class** section, select the following: **Standard**. 
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  4. Click **Create**. 



### gcloud

  * Create a Cloud Storage bucket. To create a unique Cloud Storage bucket name, use the PROJECT_ID and a suffix of your choice, `MEDIA_BUCKET_SUFFIX`. In Cloud Storage, bucket names must be globally unique.
        
        gcloud storage buckets create gs://PROJECT_ID-MEDIA_BUCKET_SUFFIX \
            --location=REGION
        




After creating a bucket, to make the uploaded images public, change the permissions of image objects to be readable by everyone.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the **Add members** button.

The _Add members_ dialog appears.

  5. In the **New members** field, enter `allUsers`.

  6. In the **Select a role** drop down, select the **Cloud Storage** sub-menu, and click the **Storage Object Viewer** option.

  7. Click **Save**.




Once shared publicly, a **link** icon appears for each object in the _public access_ column. You can click this icon to get the URL for the object.

To learn how to get detailed error information about failed Ruby operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### gcloud

  * Use the `gcloud storage buckets add-iam-policy-binding` command to make all objects public. Use the value for `MEDIA_BUCKET_SUFFIX` that you used when you created the bucket.
        
        gcloud storage buckets add-iam-policy-binding gs://PROJECT_ID-MEDIA_BUCKET_SUFFIX \
            --member=allUsers --role=roles/storage.objectViewer
        




### Store secret values in Secret Manager

Now that the backing services are configured, Rails needs secure information, such as passwords, to access these services. Instead of putting these values directly into the Rails source code, this tutorial uses [Rails Credentials](https://guides.rubyonrails.org/security.html#custom-credentials) and [Secret Manager](https://docs.cloud.google.com/secret-manager) to store this information securely.

#### Create encrypted credentials file and store key as Secret Manager secret

Rails stores secrets in an encrypted file called 'config/credentials.yml.enc'. The file can be decrypted with the local `config/master.key` or the environment variable `ENV["RAILS_MASTER_KEY"]`. In the credentials file, you can store the Cloud SQL instance database password and other access keys for external APIs.

You can store this key securely in Secret Manager. Then, you can grant Cloud Run and Cloud Build access to the key by granting access to their respective [service accounts](https://docs.cloud.google.com/iam/docs/overview#service_account). Service accounts are identified by an email address that contains the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  1. Generate the `config/credentials.yml.enc` file with the following command:
         
         bin/rails credentials:edit
         

The command will create a `config/master.key` if no master key is defined, and create a `config/credentials.yml.enc` file if the file does not exist. This will open a temporary file in your default `$EDITOR` with the decrypted contents for the secrets to be added.

**Note:** You can specify the editor by running the following command: `EDITOR="nano" bin/rails credentials:edit`
  2. Copy and paste the newly created PostgreSQL instance database password from the `dbpassword` file into the credentials file:
         
         secret_key_base: GENERATED_VALUE
         gcp:
             db_password: PASSWORD
         

Secrets can be accessed with `Rails.application.credentials`. For example, `Rails.application.credentials.secret_key_base` should return the application's secret key base and `Rails.application.credentials.gcp[:db_password]` should return your database password.

  3. The `config/credentials/yml.enc` is stored encrypted, but `config/master.key` can be stored in Secret Manager.

### Console

     1. In the Google Cloud console, go to the **Secret Manager page**.

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager?project=_)

     2. Click **Create secret**

     3. In the **Name** field, enter a name for the secret `RAILS_SECRET_NAME`.

     4. In the **Secret value** dialog, paste the mater.key value into the box.

     5. Click **Create secret**.

     6. On the Secret details page of your secret, note the project number:

projects/PROJECTNUM/secrets/RAILS_SECRET_NAME

     7. In the **Permissions** tab, click **Add Member**

     8. In the **New Members** field, enter `PROJECTNUM-compute@developer.gserviceaccount.com`, and then press `Enter`.

     9. In the **New Members** field, enter `PROJECTNUM@cloudbuild.gserviceaccount.com`, and then press `Enter`.

     10. In the **Role** drop-down menu, select **Secret Manager Secret Accessor**.

     11. Click **Save**.

### gcloud

     1. Create a new secret with the value of the config/master.key:
            
            gcloud secrets create RAILS_SECRET_NAME --data-file config/master.key
            

Replace `RAILS_SECRET_NAME` with a name for the new secret.

     2. To confirm the creation of the secret, check it:
            
            gcloud secrets describe RAILS_SECRET_NAME
            
            gcloud secrets versions access latest --secret RAILS_SECRET_NAME
            

     3. Get the value of the project number:
            
            gcloud projects describe PROJECT_ID --format='value(projectNumber)'
            

     4. [Grant access to the secret](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets#grant_access) to the Cloud Run service account:
            
            gcloud secrets add-iam-policy-binding RAILS_SECRET_NAME \
                --member serviceAccount:PROJECTNUM-compute@developer.gserviceaccount.com \
                --role roles/secretmanager.secretAccessor
            

Replace `PROJECTNUM` with the project number value.

     5. Grant access to the secret to the Cloud Build service account:
            
            gcloud secrets add-iam-policy-binding RAILS_SECRET_NAME \
                --member serviceAccount:PROJECTNUM@cloudbuild.gserviceaccount.com \
                --role roles/secretmanager.secretAccessor
            

In the output, confirm that `bindings` lists the two service accounts as members.




### Connect Rails app to production database and storage

This tutorial uses a PostgreSQL instance as the production database and Cloud Storage as the storage backend. For Rails to connect to the newly created database and storage bucket, you need to specify all the information needed to access them in the `.env` file. The `.env` file contains the configuration for the application environment variables. The application will read this file using the dotenv gem. Since the secrets are stored in `credentials.yml.enc` and Secret Manager, the `.env` doesn't have to be encrypted because it doesn't hold any sensitive credentials.

  1. To configure the Rails app to connect with the database and storage bucket, open the `.env` file.
  2. Modify the `.env` file configuration to the following. Use the value of `MEDIA_BUCKET_SUFFIX` that you used when you created the bucket.
         
         PRODUCTION_DB_NAME: DATABASE_NAME
         PRODUCTION_DB_USERNAME: DATABASE_USERNAME
         CLOUD_SQL_CONNECTION_NAME: PROJECT_ID:REGION:INSTANCE_NAME
         GOOGLE_PROJECT_ID: PROJECT_ID
         STORAGE_BUCKET_NAME: PROJECT_ID-MEDIA_BUCKET_SUFFIX
         

The Rails app is now set up to use Cloud SQL and Cloud Storage when deploying to Cloud Run.




## Deploy the app to Cloud Run

With the backing services set up, you can now deploy the app as a Cloud Run service.

  1. Using the supplied `cloudbuild.yaml`, use Cloud Build to build the image, run the database migrations, and populate the static assets:
         
         gcloud builds submit --config cloudbuild.yaml \
             --substitutions _SERVICE_NAME=SERVICE_NAME,_INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION,_SECRET_NAME=RAILS_SECRET_NAME
         

Replace `SERVICE_NAME` with the name for your service. This first build takes a few minutes to complete. If the build timed out, increase the timeout duration by inserting --timeout=2000s into the build command.

  2. When the build is successful, deploy the Cloud Run service for the first time, setting the service region, base image, and connected Cloud SQL instance:
         
         gcloud run deploy SERVICE_NAME \
                 --region REGION \
                 --image REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/SERVICE_NAME \
                 --add-cloudsql-instances PROJECT_ID:REGION:INSTANCE_NAME \
                 --allow-unauthenticated
         

You should see output that shows the deployment succeeded, with a service URL.

  3. To see the deployed service, go to the service URL.

![Cat album landing page.](https://docs.cloud.google.com/static/ruby/rails/images/cat-album-index-no-photo.png) If the service URL shows **Cat Photo Album** , you're on the homepage of the app. 

  4. Try to upload a new photo. If the photo successfully uploads, the Rails application has been successfully deployed.

![Example cat album item](https://docs.cloud.google.com/static/ruby/rails/images/cat-album-index-photo.png) If the service URL shows **Cat Photo Album** , you're on the homepage of the app. 




## Update the application

While the initial provisioning and deployment steps were complex, making updates is a simpler process:

  1. Run the Cloud Build build and migration script:
         
         gcloud builds submit --config cloudbuild.yaml \
                 --substitutions _SERVICE_NAME=SERVICE_NAME,_INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION,_SECRET_NAME=RAILS_SECRET_NAME
         

  2. Deploy the service, specifying only the region and image:
         
         gcloud run deploy SERVICE_NAME \
                 --region REGION \
                 --image REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/SERVICE_NAME
         




## Understand the code

The Rails sample app was created using standard Rails commands. The following commands create the cat_album app and use the scaffold command to generate a model, controller, and views for the Photo resource:
    
    
    rails new cat_album
    rails generate scaffold Photo caption:text
    

### Database connection

The `config/database.yml` file contains the configuration needed to access your databases in different environments (development, test, production). For example, the production database is configured to run in Cloud SQL for PostgreSQL. The database name and username are set through environment variables in the `.env` file, while the database password is stored inside the `config/credentials.yml.enc` file, which requires the `RAILS_MASTER_KEY` to decrypt.

When the app runs on Cloud Run (fully managed), it connects to the PostgreSQL instance using a socket provided by the Cloud Run environment. When the app runs on your local machine, it connects to the PostgreSQL instance using the Cloud SQL Auth proxy.
    
    
    production:
      <<: *default
      database: <%= ENV["PRODUCTION_DB_NAME"] %>
      username: <%= ENV["PRODUCTION_DB_USERNAME"] %>
      password: <%= Rails.application.credentials.gcp[:db_password] %>
      host: "<%= ENV.fetch("DB_SOCKET_DIR") { '/cloudsql' } %>/<%= ENV["CLOUD_SQL_CONNECTION_NAME"] %>"

### Cloud-stored user uploaded media

Rails uses [Active Storage](https://guides.rubyonrails.org/active_storage_overview.html) to upload files to storage providers. The `config/storage.yml` and `config/environments/production.rb` files specify Cloud Storage as the service provider in the production environment.
    
    
    google:
      service: GCS
      project: <%= ENV["GOOGLE_PROJECT_ID"] %>
      bucket: <%= ENV["STORAGE_BUCKET_NAME"] %>
    
    
    # Store uploaded files on the local file system (see config/storage.yml for options).
    config.active_storage.service = :google

### Automation with Cloud Build

The [cloudbuild.yaml file](https://docs.cloud.google.com/build/docs/build-config-file-schema) performs not only the typical image build steps (creating the container image and pushing that to Artifact Registry), but also the Rails database migrations. This migration is performed by using Cloud Run jobs, where a custom command is used so that the container performs the migration, rather than the default web server.
    
    
    steps:
      - id: "build image"
        name: "gcr.io/cloud-builders/docker"
        entrypoint: 'bash'
        args: ["-c", "docker build --build-arg MASTER_KEY=$$RAILS_KEY -t ${_IMAGE_NAME} . "]
        secretEnv: ["RAILS_KEY"]
    
      - id: "push image"
        name: "gcr.io/cloud-builders/docker"
        args: ["push", "${_IMAGE_NAME}"]
    
      - id: "apply migrations"
        name: "gcr.io/google.com/cloudsdktool/cloud-sdk"
        entrypoint: /bin/bash
        secretEnv: ["RAILS_KEY"]
        args:
          - "-c"
          - |
            gcloud run jobs create migrate-job \
              --region ${_REGION} \
              --image ${_IMAGE_NAME} \
              --set-cloudsql-instances ${_CLOUD_SQL_CONNECTION_NAME} \
              --set-env-vars RAILS_MASTER_KEY=$$RAILS_KEY \
              --command bundle \
              --args exec,rails,db:migrate \
              --execute-now --wait && \
              gcloud run jobs delete  migrate-job --region ${_REGION} -q
    
    options:
      dynamicSubstitutions: true
    
    substitutions:
      _REGION: us-central1
      _SERVICE_NAME: rails-cat-album
      _INSTANCE_NAME: cat-album
      _SECRET_NAME: rails-master-key
      _AR_REPO_NAME: cloud-run-source-deploy
      _IMAGE_NAME: ${_REGION}-docker.pkg.dev/${PROJECT_ID}/${_AR_REPO_NAME}/${_SERVICE_NAME}
      _CLOUD_SQL_CONNECTION_NAME: ${PROJECT_ID}:${_REGION}:${_INSTANCE_NAME}
    
    availableSecrets:
      secretManager:
      - versionName: projects/${PROJECT_ID}/secrets/${_SECRET_NAME}/versions/latest
        env: RAILS_KEY
    
    images:
      - "${_IMAGE_NAME}"

[Substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) are used in this configuration. Changing the values in the file directly means the `--substitutions` flag can be dropped at migration time.

In this configuration, only existing migrations in the `db/migrate` directory are applied. To create migration files, see [Active Record Migrations](https://guides.rubyonrails.org/active_record_migrations.html#migration-overview).

To build the image and apply migrations, the [Cloud Build configuration](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets#configuring_builds_to_access_the_secret_from) needs access to the `RAILS_MASTER_KEY` secret from Secret Manager. The `availableSecrets` field sets the secret version and environment variables to use for the secret. The master key secret is passed in as an argument in the build image step and then gets set to be the `RAILS_MASTER_KEY` in the Dockerfile when building the image.
    
    
    ARG MASTER_KEY
    ENV RAILS_MASTER_KEY=${MASTER_KEY}

To extend the Cloud Build configuration to include the deployment in the one configuration without having to run two commands, see [Continuous deployment from git using Cloud Build](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build). This requires IAM changes, as described.

### Cloud Logging and Error Reporting

By default, Rails logs to `stdout` in production when configured with `RAILS_LOG_TO_STDOUT`. When your application runs on Cloud Run, the environment automatically captures logs written to `stdout` and `stderr` and stores them in Cloud Logging.

To automatically capture unhandled exceptions and display formatted stack traces in Error Reporting, add the `google-cloud-error_reporting` gem to your `Gemfile`:
    
    
    gem "google-cloud-error_reporting"
    

When your Rails application starts in production mode, Bundler automatically loads the library and configures Error Reporting to capture exceptions from the Rack stack. For more information, see [Setting Up Error Reporting for Ruby](https://docs.cloud.google.com/error-reporting/docs/setup/ruby).

## Cleanup

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
