---
url: https://docs.cloud.google.com/python/django/run/
title: Running Django on the Cloud Run environment \u00a0|\u00a0 Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:47.906159+00:00
---

# Running Django on the Cloud Run environment  |  Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/django/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Running Django on the Cloud Run environment Stay organized with collections  Save and categorize content based on your preferences. 

Deploying stateful applications to Cloud Run like Django involves integrating services to interact with each other to form a cohesive project.

This tutorial assumes that you're familiar with Django web development. If you're new to Django development, it's a good idea to work through [writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) before continuing.

While this tutorial demonstrates Django specifically, you can use this deployment process with other Django-based frameworks, such as [Wagtail](https://wagtail.org/) and [Django CMS](https://www.django-cms.org/en/).

This tutorial uses Django 5, [which requires at least Python 3.10](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django).

## Objectives

In this tutorial, you will:

  * Create and connect a Cloud SQL database.
  * Create and use Secret Manager secret values.
  * Deploy a Django app to Cloud Run.

  * Host static files on Cloud Storage.

  * Use Cloud Build to automate deployment.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
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

  4. Enable the Cloud Run, Cloud SQL, Cloud Build, Secret Manager, Artifact Registry, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,secretmanager.googleapis.com,artifactregistry.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Run, Cloud SQL, Cloud Build, Secret Manager, Artifact Registry, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,cloudbuild.googleapis.com,secretmanager.googleapis.com,artifactregistry.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  14. Ensure sufficient permissions are available to the account used for this tutorial. **Note:** In cases where the `Owner` role cannot be used, the following minimum roles are required to complete the tutorial: Cloud SQL Admin, Storage Admin, Cloud Run Admin, Artifact Registry Admin, and Secret Manager Admin. 



## Prepare your environment

### Clone a sample app

The code for the Django sample app is in the [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples) repository on GitHub.

  1. You can either [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a ZIP file and extract it or clone the repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Go to the directory that contains the sample code:

### Linux/macOS
         
         cd python-docs-samples/run/django
         

### Windows
         
         cd python-docs-samples\run\django
         




### Confirm your Python setup

This tutorial relies on Python to run the sample application on your machine. The sample code also requires installing dependencies

For more details, refer to the [Python development environment guide](https://docs.cloud.google.com/python/docs/setup).

  1. Confirm your Python is at least version 3.10.
         
         python -V
         

You should see `Python 3.10.0` or higher.

**Note:** If you see a version number starting with "2", you may need to run `python3` instead of `python`. If so, remember to reference your chosen Python installation when running `python` commands.
  2. Create a Python virtual environment and install dependencies:

### Linux/macOS
         
         python -m venv venv
         source venv/bin/activate
         pip install --upgrade pip
         pip install -r requirements.txt
         

### Windows
         
         python -m venv venv
         venv\scripts\activate
         pip install --upgrade pip
         pip install -r requirements.txt
         




### Download Cloud SQL Auth Proxy to connect to Cloud SQL from your local machine

**Note:** If you are completing this tutorial from Cloud Shell, this section is not required.

When deployed, your app uses the Cloud SQL Auth Proxy that is built into the Cloud Run environment to communicate with your Cloud SQL instance. However, to test your app locally, you must install and use a local copy of the proxy in your development environment. For more details, refer to the [Cloud SQL Auth Proxy guide](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).

The Cloud SQL Auth Proxy uses the Cloud SQL API to interact with your SQL instance. To do this, it requires application authentication through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Authenticate and acquire credentials for the API:
         
         gcloud auth application-default login
         

  2. Download and install the Cloud SQL Auth Proxy to your local machine.

Before you begin, you must determine your machine's architecture.

If running on Linux or Mac, you can find this by running the following command:
         
         uname -a
           

### Linux 64-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.amd64

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### Linux 32-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.386

     2. If the `curl` command is not found, run `sudo apt install curl` and repeat the download command.
     3. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### macOS 64-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.amd64

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### Mac M1

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.arm64
              

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy
              

### Windows 64-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x64.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Windows 32-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x86.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Cloud SQL Auth Proxy Docker image

The Cloud SQL Auth Proxy has different container images, such as `distroless`, `alpine`, and `buster`. The default Cloud SQL Auth Proxy container image uses [`distroless`](https://github.com/GoogleContainerTools/distroless), which contains no shell. If you need a shell or related tools, then download an image based on `alpine` or `buster`. For more information, see [Cloud SQL Auth Proxy Container Images](https://github.com/GoogleCloudPlatform/cloudsql-proxy#container-images).

You can pull the latest image to your local machine using Docker by using the following command:
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2
    

**Note** : The Cloud SQL Auth Proxy uses a repository that supports the `gcr.io` domain but serves images from Artifact Registry. For more information, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). 

### Other OS

For other operating systems not included here, you can [compile the Cloud SQL Auth Proxy from source](http://github.com/GoogleCloudPlatform/cloudsql-proxy). 

You can choose to move the download to somewhere common, such as a location on your `PATH`, or your home directory. If you choose to do this, when you start the Cloud SQL Auth Proxy later on in the tutorial, remember to reference your chosen location when using `cloud-sql-proxy` commands.




## Create backing services

This tutorial uses several Google Cloud services to provide the database, media storage, and secret storage that support the deployed Django project. These services are deployed in a specific region. For efficiency between services, all services should be deployed in the same region. For more information about the closest region to you, see [Products available by region](https://cloud.google.com/about/locations#products-available-by-location).

This tutorial uses the integrated static asset hosting mechanisms in Cloud Run. 

### Set up a Cloud SQL for PostgreSQL instance

Django officially supports multiple relational databases, but offers the most support for PostgreSQL. PostgreSQL is supported by Cloud SQL, so this tutorial chooses to use that type of database.

The following section describes the creation of a PostgreSQL instance, database, and database user for the app.

  1. Create the PostgreSQL instance:

### Console

     1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)

     2. Click **Create Instance**.

     3. Click **Choose PostgreSQL**.

     4. For **SQL Edition** , choose "Enterprise".

     5. For **Edition Preset** , choose "Sandbox".

     6. In the **Instance ID** field, enter `INSTANCE_NAME`.

     7. Enter a password for the postgres user.

     8. Keep the default values for the other fields.

     9. Click **Create Instance**.

It takes a few minutes for the instance to be ready for use.

### gcloud

     * Create the PostgreSQL instance:
           
           gcloud sql instances create INSTANCE_NAME \
               --project PROJECT_ID \
               --database-version POSTGRES_16 \
               --tier db-n1-standard-2 \
               --region REGION
           

Replace the following:

     * `INSTANCE_NAME`: the Cloud SQL instance name
     * `PROJECT_ID`: the Google Cloud project ID
     * `REGION`: the [Google Cloud region](https://cloud.google.com/run/docs/locations)

It takes a few minutes to create the instance and for it to be ready for use.

  2. Within the created instance, create a database:

### Console

     1. Within your instance page, go to the **Databases** tab.
     2. Click **Create database**.
     3. In the **Database Name** dialog, enter `DATABASE_NAME`.
     4. Click **Create**.

### gcloud

     * Create the database within the recently created instance:
           
           gcloud sql databases create DATABASE_NAME \
               --instance INSTANCE_NAME
           

Replace `DATABASE_NAME` with a name for the database inside the instance.

  3. Create a database user:

**Note:** Users created this way get additional database rights. See Limit the database user privileges for an alternative method.

### Console

     1. Within your instance page, go to the **Users** tab.
     2. Click **Add User Account**.
     3. In the **Choose how to authenticate** dialog under "Built-in Authentication":
     4. Enter the username `DATABASE_USERNAME`.
     5. Enter the password `DATABASE_PASSWORD`
     6. Click **Add**.

### gcloud

     * Create the user within the recently created instance:
           
           gcloud sql users create DATABASE_USERNAME \
               --instance INSTANCE_NAME \
               --password DATABASE_PASSWORD
           

Replace `PASSWORD` with a secure password.




### Set up Artifact Registry

Use Artifact Registry to create a registry to store your container image.

**Note:** This repository is automatically created when using [Cloud Run Source Deploys](https://docs.cloud.google.com/run/docs/deploying-source-code), and may already exist in your project.

### Console

  1. In the Google Cloud console, go to the **Artifact Registry** page.

[Go to the Artifact Registry page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Enter the following:

     * For **Name** , enter "cloud-run-source-deploy".
     * For **Format** , select "Docker".
     * For **Region** , select REGION.
  4. Keep the default values for the other fields.

  5. Click **Create**.




### gcloud

  * Create an Artifact Registry:


    
    
    gcloud artifacts repositories create cloud-run-source-deploy \
        --repository-format docker \
        --location REGION
    

### Set up a Cloud Storage bucket

You can store Django's included static assets, as well as user-uploaded media, in highly-available object storage using Cloud Storage. The [`django-storages[google]`](https://django-storages.readthedocs.io/) package handles Django's interaction with this storage backend.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage** page.

[Go to the Cloud Storage page](https://console.cloud.google.com/storage)

  2. Click **Create Bucket**.

  3. Enter the following (clicking "Continue" where needed):

     * For **Name** , enter "PROJECT_ID_MEDIA_BUCKET".
     * For **Region** , select REGION.
     * For **Storage Class** , keep the defaults.
     * For **Prevent public access** , clear "Enforce public access prevention".
     * For **Access Control** , select "Fine-grained".
  4. Keep the default values for the other fields.

  5. Click **Create**.




### gcloud

  * Create a Cloud Storage bucket:
        
        gcloud storage buckets create gs://PROJECT_ID_MEDIA_BUCKET --location=REGION
        

Replace `MEDIA_BUCKET` with a suffix for the media bucket. Combined with the project ID, this creates a unique bucket name.




### Store secret values in Secret Manager

Now that the backing services are configured, Django needs information about these services. Instead of putting these values directly into the Django source code, this tutorial uses Secret Manager to store this information securely.

#### Create Django environment file as a Secret Manager secret

You store the settings required to start Django in a secured env file. The sample app uses the Secret Manager API to retrieve the secret value, and the [`django-environ`](https://django-environ.readthedocs.io/) package to load the values into the Django environment. The secret is configured to be accessible by Cloud Run and Cloud Build.

  1. Create a file called `.env`, defining the database connection string, the media bucket name, and a new [`SECRET_KEY`](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY) value:
         
         echo DATABASE_URL=postgres://DATABASE_USERNAME:DATABASE_PASSWORD@//cloudsql/PROJECT_ID:REGION:INSTANCE_NAME/DATABASE_NAME > .env
         echo GS_BUCKET_NAME=PROJECT_ID_MEDIA_BUCKET >> .env
         echo SECRET_KEY=$(cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1) >> .env
         

  2. Store the secret in Secret Manager:

### Console

     1. In the Google Cloud console, go to the **Secret Manager page**.

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager?project=_)

     2. Click **Create secret**

     3. In the **Name** field, enter `django_settings`.

     4. In the **Secret value** dialog, paste the contents of your `.env` file.

     5. Click **Create secret**.

     6. Delete the local file to prevent local setting overrides.

### gcloud

     1. Create a new secret, `django_settings`, with the value of the `.env` file:
            
            gcloud secrets create django_settings --data-file .env
            

     2. Delete the local file to prevent local setting overrides:
            
            rm .env
            

  3. Configure access to the secret:

### Console

Before configuring access to the secret, note the project number in **Secret: django_settings** :
         
         projects/PROJECTNUM/secrets/django_settings
         

     1. Click the **Permissions** tab.
     2. Click **Grant access**.
     3. In the **New Members** field, enter `PROJECTNUM-compute@developer.gserviceaccount.com`, and then press `Enter`.
     4. In the **Role** drop-down menu, select **Secret Manager Secret Accessor**.
     5. Click **Save**.

### gcloud

[Grant access to the secret](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets#grant_access) to the Cloud Run service account:
    
    gcloud secrets add-iam-policy-binding django_settings \
          --member serviceAccount:PROJECTNUM-compute@developer.gserviceaccount.com \
          --role roles/secretmanager.secretAccessor
    

You can get the value of the project number (`PROJECTNUM`) using the following command:
    
    gcloud projects describe PROJECT_ID --format='value(projectNumber)'
    

In the output, confirm that `bindings` lists the new service account.




#### Create secret for Django's admin password

The Django admin user is normally created by running the interactive management command `createsuperuser`.

This tutorial uses a data migration to create the admin user, retrieving the admin password from Secret Manager.

### Console

  1. In the Google Cloud console, go to the **Secret Manager page**.
  2. Click **Create secret**.

  3. In the **Name** field, enter `superuser_password`.

  4. In the **Secret value** field, enter a random, unique password.

  5. Click **Create secret**.

  6. In **Details for`superuser_password`**, make a note of the project number (`projects/PROJECTNUM/secrets/superuser_password`).

  7. Click the **Permissions** tab.

  8. Click **Add**.

  9. In the **New Members** field, enter `PROJECTNUM-compute@developer.gserviceaccount.com`, and then press `Enter`.

  10. In the **Role** drop-down menu, select **Secret Manager Secret Accessor**.

  11. Click **Save**




### gcloud

  1. Create a new secret, `superuser_password`, from a randomly generated password:
         
         echo -n "$(cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 30 | head -n1)" | gcloud secrets create superuser_password --data-file -
         

  2. Grant access to the secret to Cloud Build:
         
         gcloud secrets add-iam-policy-binding superuser_password \
             --member serviceAccount:PROJECTNUM-compute@developer.gserviceaccount.com \
             --role roles/secretmanager.secretAccessor
         

In the output, confirm that `bindings` lists only the Cloud Build as a member.




## Run the app on your local computer

With the backing services configured, you can now run the app on your computer. This setup allows for local development, and applying database migrations. Note that database migrations are also applied in Cloud Build, but you will need to have this local setup in order to `makemigrations`.

  1. In a separate terminal, start the Cloud SQL Auth Proxy:

### Linux/macOS
         
         ./cloud-sql-proxy PROJECT_ID:REGION:INSTANCE_NAME
         

### Windows
         
         cloud-sql-proxy.exe PROJECT_ID:REGION:INSTANCE_NAME
         

This step establishes a connection from your local computer to your Cloud SQL instance for local testing purposes. Keep the Cloud SQL Auth Proxy running the entire time you test your app locally. Running this process in a separate terminal allows you to keep working while this process runs.

  2. In the original terminal, set the Project ID locally (used by the Secret Manager API):

### Linux/macOS
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         

### Windows
         
         set GOOGLE_CLOUD_PROJECT=PROJECT_ID
         

  3. Set an environment variable to indicate you are using Cloud SQL Auth Proxy (this value is recognised in the code):

### Linux/macOS
         
         export USE_CLOUD_SQL_AUTH_PROXY=true
         

### Windows
         
         set USE_CLOUD_SQL_AUTH_PROXY=true
         

  4. Run the Django migrations to set up your models and assets:
         
         python manage.py makemigrations
         python manage.py makemigrations polls
         python manage.py migrate
         python manage.py collectstatic
         

  5. Start the Django web server:
         
         python manage.py runserver 8080
         

  6. In your browser, go to <http://localhost:8080>.

If you are in Cloud Shell, click the **Web Preview** button, and select **Preview on port 8080**.

The page displays the following text: "Hello, world. You're at the polls index." The Django web server running on your computer delivers the sample app pages.

  7. Press `Ctrl`/`Cmd`+`C` to stop the local web server.




## Deploy the app to Cloud Run

With the backing services setup, you can now deploy the Cloud Run service.

  1. Using the supplied `cloudmigrate.yaml`, use Cloud Build to build the image, run the database migrations, and populate the static assets:
         
         gcloud builds submit --config cloudmigrate.yaml \
             --substitutions _INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION
         

This first build takes a few minutes to complete.

  2. When the build is successful, deploy the Cloud Run service for the first time, setting the service region, base image, and connected Cloud SQL instance:
         
         gcloud run deploy polls-service \
             --region REGION \
             --image REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/polls-service \
             --add-cloudsql-instances PROJECT_ID:REGION:INSTANCE_NAME \
             --allow-unauthenticated
         

You should see output that shows the deployment succeeded, with a service URL:
         
         Service [polls-service] revision [polls-service-00001-tug] has been deployed
         and is serving 100 percent of traffic.
         Service URL: https://polls-service-PROJECT_ID.REGION.run.app
         

  3. Update the service to the service URLs as an environment variable.
         
         CLOUDRUN_SERVICE_URLS=$(gcloud run services describe polls-service \
             --region $REGION  \
             --format "value(metadata.annotations[\"run.googleapis.com/urls\"])" | tr -d '"[]')
         
         gcloud run services update polls-service \
             --region REGION \
             --update-env-vars "^##^CLOUDRUN_SERVICE_URLS=$CLOUDRUN_SERVICE_URLS"
         

**Note:** This configures CSRF.
  4. To see the deployed service, go to the service URL.

  5. To log into the Django admin, append `/admin` to the URL, and login with the username `admin`, and the password set earlier.

To retrieve the superuser password from Secret Manager:
         
         gcloud secrets versions access latest --secret superuser_password && echo ""
         




## Updating the application

While the initial provisioning and deployment steps were complex, making updates is a simpler process:

  1. Run the Cloud Build build and migration script:
         
         gcloud builds submit --config cloudmigrate.yaml \
             --substitutions _INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION
         

  2. Deploy the service, specifying only the region and image:
         
         gcloud run deploy polls-service \
             --region REGION \
             --image REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/polls-service
         




## Configuring for production

You now have a working Django deployment, but there are further steps you can take to ensure that your application is production-ready.

### Disable debugging

Confirm that the `DEBUG` variable in `mysite/settings.py` is set to `False`. This will prevent detailed error pages from being displayed to the user, which can [leak information about the configurations](https://docs.djangoproject.com/en/stable/howto/error-reporting/#error-reporting).

### Limit the database user privileges

Any users that are created by using Cloud SQL have the privileges associated with the [`cloudsqlsuperuser` role](https://cloud.google.com/sql/docs/postgres/users#other_postgresql_users): `CREATEROLE`, `CREATEDB`, and `LOGIN`.

To prevent the Django database user from having these permissions, manually create the user in PostgreSQL. You will need to have the [`psql` interactive terminal](https://www.postgresql.org/docs/current/app-psql.html) installed, or use Cloud Shell which has this tool pre-installed.

### Console

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In Cloud Shell, use the built-in terminal to connect to your `INSTANCE_NAME` instance:
         
         gcloud sql connect INSTANCE_NAME --user postgres
         

  3. Enter the postgres user password.

You are now using `psql`. You should see the `postgres=>` prompt.

  4. Create a user:
         
         CREATE USER DATABASE_USERNAME WITH PASSWORD 'DATABASE_PASSWORD';
         

Replace `PASSWORD` with a random, unique password.

  5. Grant full rights on the new database to the new user:
         
         GRANT ALL PRIVILEGES ON DATABASE DATABASE_NAME TO DATABASE_USERNAME;
         

  6. Exit `psql`:
         
         \q
         




### gcloud

**Note:** Any users that are created by using Cloud SQL have the privileges associated with the [`cloudsqlsuperuser` role](https://cloud.google.com/sql/docs/postgres/users#other_postgresql_users): `CREATEROLE`, `CREATEDB`, and `LOGIN`. This tutorial creates the user directly in PostgreSQL.

  1. Start a connection to the SQL instance:
         
         gcloud sql connect INSTANCE_NAME --user postgres
         

Replace `INSTANCE_NAME` with the created Cloud SQL instance.

  2. Enter the postgres user password.

You are now using `psql`. You should see the `postgres=>` prompt.

  3. Create a user:
         
         CREATE USER DATABASE_USERNAME WITH PASSWORD 'DATABASE_PASSWORD';
         

  4. Grant full rights on the new database to the new user:
         
         GRANT ALL PRIVILEGES ON DATABASE DATABASE_NAME TO DATABASE_USERNAME;
         

  5. Exit `psql`:
         
         \q
         




### Setting minimum permissions

By default, this service is deployed with the [default compute service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). However, in some cases, using the default service account can provide too many permissions. If you want to be more restrictive, you need to create your own service account and assign only the permissions that are required by your service. The permissions required can vary from service to service, depending on the resources used by a particular service.

The minimum project roles required by this service are the following:

  * Cloud Run Invoker
  * Cloud SQL Client
  * Storage Admin, on the media bucket
  * Secret Manager Accessor, on the Django settings secret. (Access to the Django admin secret is not required by the service itself.)



To create a service account with the required permissions, and assign it to the service, run the following:

  1. In the gcloud CLI, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) with the required roles:
         
         gcloud iam service-accounts create polls-service-account
         SERVICE_ACCOUNT=polls-service-account@PROJECT_ID.iam.gserviceaccount.com
         
         # Cloud SQL Client
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member serviceAccount:${SERVICE_ACCOUNT} \
             --role roles/cloudsql.client
         
         # Storage Admin, on the media bucket
         gcloud storage buckets add-iam-policy-binding gs://MEDIA_BUCKET \
             --member=serviceAccount:${SERVICE_ACCOUNT} \
             --role=roles/storage.objectAdmin
         
         # Secret Accessor, on the Django settings secret.
         gcloud secrets add-iam-policy-binding django_settings \
             --member serviceAccount:${SERVICE_ACCOUNT} \
             --role roles/secretmanager.secretAccessor
         
         # Secret Accessor, on the Django super user password.
         gcloud secrets add-iam-policy-binding superuser_password \
             --member serviceAccount:${SERVICE_ACCOUNT} \
             --role roles/secretmanager.secretAccessor
         

  2. Deploy the service, associating it with the new service account:
         
         gcloud run services update polls-service \
             --region REGION \
             --service-account ${SERVICE_ACCOUNT}
         

  3. Update the Cloud Run jobs in `cloudmigrate.yaml` to also have this `--service-account` setting.




## Understand the code

### Sample application

The Django sample app was created using standard Django tooling. The following commands create the project and the polls app:
    
    
    django-admin startproject mysite
    python manage.py startapp polls
    

The base views, models, and route configurations were copied from [Writing your first Django app](https://docs.djangoproject.com/en/stable/#first-steps) ([Part 1](https://docs.djangoproject.com/en/stable/intro/tutorial01/) and [Part 2](https://docs.djangoproject.com/en/stable/intro/tutorial02/)).

### Secrets from Secret Manager

The `settings.py` file contains code that uses the Secret Manager Python API to retrieve the latest version of the named secret, and pull it into the environment (using [`django-environ`](https://django-environ.readthedocs.io/)):
    
    
    # SECURITY WARNING: don't run with debug turned on in production!
    # Change this to "False" when you are ready for production
    env = environ.Env(DEBUG=(bool, True))
    env_file = os.path.join(BASE_DIR, ".env")
    
    # Attempt to load the Project ID into the environment, safely failing on error.
    try:
        _, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()
    except google.auth.exceptions.DefaultCredentialsError:
        pass
    
    if os.path.isfile(env_file):
        # Use a local secret file, if provided
    
        env.read_env(env_file)
    # ...
    elif os.environ.get("GOOGLE_CLOUD_PROJECT", None):
        # Pull secrets from Secret Manager
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    
        client = secretmanager.SecretManagerServiceClient()
        settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
        name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
        payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
    
        env.read_env(io.StringIO(payload))
    else:
        raise Exception("No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.")

The secret is used to store multiple secret values to reduce the number of different secrets that needed to be configured.

### CSRF configurations

Django has built-in protection against [Cross Site Request Forgery (CSRF)](https://docs.djangoproject.com/en/stable/ref/csrf/#how-it-works). Starting in Django 4.0, changes to the way this works mean that it's important to tell Django what it's hosted URL is, so it can offer the best protections for users submitting data.

You supply the app's URL as an environment variable in the `settings.py` file This is the value that Django uses for the relevant settings.
    
    
    # SECURITY WARNING: It's recommended that you use this when
    # running in production. The URLs will be known once you first deploy
    # to Cloud Run. This code takes the URLs and converts it to both these settings formats.
    CLOUDRUN_SERVICE_URLS = env("CLOUDRUN_SERVICE_URLS", default=None)
    if CLOUDRUN_SERVICE_URLS:
        CSRF_TRUSTED_ORIGINS = env("CLOUDRUN_SERVICE_URLS").split(",")
        # Remove the scheme from URLs for ALLOWED_HOSTS
        ALLOWED_HOSTS = [urlparse(url).netloc for url in CSRF_TRUSTED_ORIGINS]
    
        SECURE_SSL_REDIRECT = True
        SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    else:
        ALLOWED_HOSTS = ["*"]

### Local secret overrides

If a `.env` file is found on the local filesystem, it is used instead of the value from Secret Manager. Creating a `.env` file locally can help with local testing (e.g. local development against a SQLite database, or other local settings). 

### Database connection

The `settings.py` file contains the configuration for your SQL database. It uses the `env.db()` helper from `django-environ` to load the connection string set in `DATABASE_URL` into the `DATABASES` setting.

When running the application locally and using the Cloud SQL Auth Proxy to access the hosted database, the `USE_CLOUD_SQL_AUTH_PROXY` flag adjusts the database settings to use the proxy.
    
    
    # Use django-environ to parse the connection string
    DATABASES = {"default": env.db()}
    
    # If the flag as been set, configure to use proxy
    if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
        DATABASES["default"]["HOST"] = "127.0.0.1"
        DATABASES["default"]["PORT"] = 5432
    

### Cloud-stored static

The `settings.py` file also uses [`django-storages`](https://django-storages.readthedocs.io/en/latest/backends/gcloud.html) to integrate the Cloud Storage media bucket directly into the project:
    
    
    # Define static storage via django-storages[google]
    GS_BUCKET_NAME = env("GS_BUCKET_NAME")
    STATIC_URL = "/static/"
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        },
        "staticfiles": {
            "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        },
    }
    GS_DEFAULT_ACL = "publicRead"

### Automation with Cloud Build

The `cloudmigrate.yaml` handles all the steps required to create a new container image, and use it to apply database migrations.

This tutorial opts to use buildpacks to build the container image, and [custom entry points in the `Procfile`](https://docs.cloud.google.com/docs/buildpacks/overview#use_to_containerize_your_code) to handle management commands. These can then be referenced by Cloud Run jobs to perform the commands.
    
    
    steps:
      - id: "Build Container Image"
        name: gcr.io/k8s-skaffold/pack
        args: ["build", "${_IMAGE_NAME}", "--builder=gcr.io/buildpacks/builder"]
    
      - id: "Push Container Image"
        name: "gcr.io/cloud-builders/docker"
        args: ["push", "${_IMAGE_NAME}"]
    
      - id: "Migrate database"
        name: "gcr.io/google.com/cloudsdktool/cloud-sdk"
        entrypoint: /bin/bash
        args:
          - "-c"
          - |
            gcloud run jobs create migrate-job \
              --region ${_REGION} \
              --image ${_IMAGE_NAME} \
              --set-cloudsql-instances ${_CLOUD_SQL_CONNECTION_NAME} \
              --set-env-vars SETTINGS_NAME=${_SECRET_SETTINGS_NAME} \
              --command migrate \
              --execute-now
    
      - id: "Create superuser"
        name: "gcr.io/google.com/cloudsdktool/cloud-sdk"
        entrypoint: /bin/bash
        args:
          - "-c"
          - |
            gcloud run jobs create superuser-job \
              --region ${_REGION} \
              --image ${_IMAGE_NAME} \
              --set-cloudsql-instances ${_CLOUD_SQL_CONNECTION_NAME} \
              --set-env-vars SETTINGS_NAME=${_SECRET_SETTINGS_NAME} \
              --set-env-vars DJANGO_SUPERUSER_EMAIL=${_ADMIN_EMAIL} \
              --set-secrets DJANGO_SUPERUSER_PASSWORD=${_ADMIN_PASSWORD_NAME}:latest \
              --command createsuperuser \
              --execute-now
    
    options:
      dynamicSubstitutions: true
    
    substitutions:
      _INSTANCE_NAME: django-instance
      _CLOUD_SQL_CONNECTION_NAME: ${PROJECT_ID}:${_REGION}:${_INSTANCE_NAME}
      _REGION: us-central1
      _SERVICE_NAME: polls-service
      _SECRET_SETTINGS_NAME: django_settings
      _ARTIFACT_REGISTRY: cloud-run-source-deploy
      _IMAGE_NAME: ${_REGION}-docker.pkg.dev/${PROJECT_ID}/${_ARTIFACT_REGISTRY}/${_SERVICE_NAME}
      _ADMIN_EMAIL: example@example.com
      _ADMIN_PASSWORD_NAME: superuser_password
    
    images:
      - "${_IMAGE_NAME}"

[Substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) are used in this configuration.

### Superuser creation with Cloud Run Jobs

The Django management command [`createsuperuser`](https://docs.djangoproject.com/en/stable/ref/django-admin/#createsuperuser) can be run non-interactively by setting `DJANGO_SUPERUSER_EMAIL` and `DJANGO_SUPERUSER_PASSWORD`.

This tutorial opts to use Cloud Run Jobs to run this command. This is done by adding a custom entry into the `Procfile` which runs `createsuperuser`.
    
    
    # Create superuser (requires DJANGO_SUPERUSER_PASSWORD and DJANGO_SUPERUSER_EMAIL envvars)
    createsuperuser: python manage.py createsuperuser --username admin --noinput || echo "User already exists."

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [configure PostgreSQL for production](https://docs.cloud.google.com/solutions/setting-up-cloud-sql-for-postgresql-for-production)
  * Learn more about [Django on Google Cloud](https://docs.cloud.google.com/python/django)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
