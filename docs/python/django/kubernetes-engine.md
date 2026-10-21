---
url: https://docs.cloud.google.com/python/django/kubernetes-engine/
title: Running Django on the Google Kubernetes Engine \u00a0|\u00a0 Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:10:56.597251+00:00
---

# Running Django on the Google Kubernetes Engine  |  Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/django/kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Running Django on the Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Django apps that run on [GKE](https://docs.cloud.google.com/gke) scale dynamically according to traffic.

This tutorial assumes that you're familiar with Django web development. If you're new to Django development, it's a good idea to work through [writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) before continuing.

While this tutorial demonstrates Django specifically, you can use this deployment process with other Django-based frameworks, such as [Wagtail](https://wagtail.org/) and [Django CMS](https://www.django-cms.org/en/).

This tutorial uses Django 5, [which requires at least Python 3.10](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django). 

You also need to have [Docker installed](https://docs.docker.com/engine/installation/).

## Objectives

In this tutorial, you will:

  * Create and connect a Cloud SQL database.
  * Create and use Kubernetes secret values.
  * Deploy a Django app to Google Kubernetes Engine.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)



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

  4. Enable the Cloud SQL, GKE and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,sql-component.googleapis.com,compute.googleapis.com,container.googleapis.com)

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

  10. Enable the Cloud SQL, GKE and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,sql-component.googleapis.com,compute.googleapis.com,container.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




## Prepare your environment

### Clone a sample app

The code for the Django sample app is in the [GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples) repository on GitHub.

  1. You can either [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a ZIP file and extract it or clone the repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Go to the directory that contains the sample code:

### Linux/macOS
         
         cd python-docs-samples/kubernetes_engine/django_tutorial
         

### Windows
         
         cd python-docs-samples\kubernetes_engine\django_tutorial
         




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

When deployed, your app uses the Cloud SQL Auth Proxy that is built into the Google Kubernetes Engine environment to communicate with your Cloud SQL instance. However, to test your app locally, you must install and use a local copy of the proxy in your development environment. For more details, refer to the [Cloud SQL Auth Proxy guide](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).

The Cloud SQL Auth Proxy uses the Cloud SQL API to interact with your SQL instance. To do this, it requires application authentication through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Authenticate and acquire credentials for the API:
         
         gcloud auth application-default login
         

  2. Download and install the Cloud SQL Auth Proxy to your local machine.

Before you begin, you must determine your machine's architecture.

If running on Linux or Mac, you can find this by running the following command:
         
         uname -a
           

### Linux 64-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.linux.amd64

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### Linux 32-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.linux.386

     2. If the `curl` command is not found, run `sudo apt install curl` and repeat the download command.
     3. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### macOS 64-bit

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.darwin.amd64

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy

### Mac M1

     1. Download the Cloud SQL Auth Proxy: 
            
            curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.darwin.arm64
              

     2. Make the Cloud SQL Auth Proxy executable: 
            
            chmod +x cloud-sql-proxy
              

### Windows 64-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.x64.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Windows 32-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.0/cloud-sql-proxy.x86.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Cloud SQL Auth Proxy Docker image

The Cloud SQL Auth Proxy has different container images, such as `distroless`, `alpine`, and `buster`. The default Cloud SQL Auth Proxy container image uses [`distroless`](https://github.com/GoogleContainerTools/distroless), which contains no shell. If you need a shell or related tools, then download an image based on `alpine` or `buster`. For more information, see [Cloud SQL Auth Proxy Container Images](https://github.com/GoogleCloudPlatform/cloudsql-proxy#container-images).

You can pull the latest image to your local machine using Docker by using the following command:
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.0
    

**Note** : The Cloud SQL Auth Proxy uses a repository that supports the `gcr.io` domain but serves images from Artifact Registry. For more information, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). 

### Other OS

For other operating systems not included here, you can [compile the Cloud SQL Auth Proxy from source](http://github.com/GoogleCloudPlatform/cloudsql-proxy). 

You can choose to move the download to somewhere common, such as a location on your `PATH`, or your home directory. If you choose to do this, when you start the Cloud SQL Auth Proxy later on in the tutorial, remember to reference your chosen location when using `cloud-sql-proxy` commands.




## Create backing services

This tutorial uses several Google Cloud services to provide the database, media storage, and secret storage that support the deployed Django project. These services are deployed in a specific region. For efficiency between services, all services should be deployed in the same region. For more information about the closest region to you, see [Products available by region](https://cloud.google.com/about/locations#products-available-by-location).

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




## Create a service account

The proxy requires a service account with Editor privileges for your Cloud SQL instance. For more information about service accounts, see the [Google Cloud authentication overview](https://docs.cloud.google.com/docs/authentication).

If you are connecting from Compute Engine, make sure your VM has the proper `scope` to connect using the Cloud SQL Admin API. 

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




## Configure the database settings

Use the following commands to set environment variables for database access. These environment variables are used for local testing.

### Linux/MacOS
    
    
    export DATABASE_NAME=DATABASE_NAME
    export DATABASE_USER=DATABASE_USERNAME
    export DATABASE_PASSWORD=DATABASE_PASSWORD
    

### Windows
    
    
    set DATABASE_USER=DATABASE_USERNAME
    set DATABASE_PASSWORD=DATABASE_PASSWORD
    

## Set up your GKE configuration

  1. This application is represented in a single Kubernetes configuration called `polls`. In `polls.yaml` replace `<your-project-id>` with your Google Cloud project ID (PROJECT_ID).

  2. Run the following command and note the value of `connectionName`:
         
         gcloud sql instances describe INSTANCE_NAME --format "value(connectionName)"
         

  3. In the `polls.yaml` file, replace `<your-cloudsql-connection-string>` with the `connectionName` value.




## Run the app on your local computer

With the backing services configured, you can now run the app on your computer. This setup allows for local development, creating a superuser, and applying database migrations. 

  1. In a separate terminal, start the Cloud SQL Auth Proxy:

### Linux/macOS
         
         ./cloud-sql-proxy PROJECT_ID:REGION:INSTANCE_NAME
         

### Windows
         
         cloud-sql-proxy.exe PROJECT_ID:REGION:INSTANCE_NAME
         

This step establishes a connection from your local computer to your Cloud SQL instance for local testing purposes. Keep the Cloud SQL Auth Proxy running the entire time you test your app locally. Running this process in a separate terminal allows you to keep working while this process runs.

  2. In the original terminal, set the Project ID locally:

### Linux/macOS
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         

### Windows
         
         set GOOGLE_CLOUD_PROJECT=PROJECT_ID
         

  3. Run the Django migrations to set up your models and assets:
         
         python manage.py makemigrations
         python manage.py makemigrations polls
         python manage.py migrate
         python manage.py collectstatic
         

  4. Start the Django web server:
         
         python manage.py runserver 8080
         

  5. In your browser, go to <http://localhost:8080>.

If you are in Cloud Shell, click the **Web Preview** button, and select **Preview on port 8080**.

The page displays the following text: "Hello, world. You're at the polls index." The Django web server running on your computer delivers the sample app pages.

  6. Press `Ctrl`/`Cmd`+`C` to stop the local web server.




## Use the Django admin console

In order to log into Django's admin console, you need to create a **superuser**. Since you have a locally accessible connection to the database, you can run management commands:

  1. Create a superuser. You will be prompted to enter a username, email, and password.
         
         python manage.py createsuperuser
         

  2. Start a local web server:
         
         python manage.py runserver
         

  3. In your browser, go to <http://localhost:8000/admin>.

  4. Log in to the admin site using the username and password you used when you ran `createsuperuser`.


**Note:** Since you are connected to your Cloud SQL database, you will log into your deployed Django application with the same credentials.

## Deploy the app to GKE

When the app is deployed to Google Cloud, it uses the Gunicorn server. Gunicorn doesn't serve static content, so the app uses Cloud Storage to serve static content.

### Collect and upload static resources

  1. Create a Cloud Storage bucket and make it publicly readable.
         
         gcloud storage buckets create gs://PROJECT_ID_MEDIA_BUCKET
         gcloud storage buckets add-iam-policy-binding gs://PROJECT_ID_MEDIA_BUCKET --member=allUsers --role=roles/storage.legacyObjectReader
         

  2. Gather all the static content locally into one folder:
         
         python manage.py collectstatic
         

  3. Upload the static content to Cloud Storage:
         
         gcloud storage rsync ./static gs://PROJECT_ID_MEDIA_BUCKET/static --recursive
         

  4. In `mysite/settings.py`, set the value of `STATIC_URL` to the following URL, replacing `[YOUR_GCS_BUCKET]` with your bucket name:
         
         http://storage.googleapis.com/PROJECT_ID_MEDIA_BUCKET/static/
         




### Set up GKE

  1. To initialize GKE, go to the **Clusters** page.

[Go to the Clusters page](https://console.cloud.google.com/kubernetes/list)

When you use GKE for the first time in a project, you need to wait for the "Kubernetes Engine is getting ready. This may take a minute or more" message to disappear.

  2. Create a GKE cluster: 
         
         gcloud container clusters create polls \
           --scopes "https://www.googleapis.com/auth/userinfo.email","cloud-platform" \
           --num-nodes 4 --zone "us-central1-a"
         

If an error message similar to `Project is not fully initialized with the default service accounts` appears, you might need to initialize Google Kubernetes Engine.

### Initialize GKE

If you received an error, go to the Google Cloud console to initialize GKE in your project.

[Go to the Clusters page](https://console.cloud.google.com/kubernetes/list)

Wait for the "Kubernetes Engine is getting ready. This can take a minute or more" message to disappear. 

OK

  3. After the cluster is created, use the `kubectl` command-line tool, which is integrated with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), to interact with your GKE cluster. Because `gcloud` and `kubectl` are separate tools, make sure `kubectl` is configured to interact with the right cluster.
         
         gcloud container clusters get-credentials polls --zone "us-central1-a"
         




### Set up Cloud SQL

  1. You need several [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to enable your GKE app to connect with your Cloud SQL instance. One is required for instance-level access (connection), while the other two are required for database access. For more information about the two levels of access control, see [Instance access control](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control).

     1. To create the secret for instance-level access, provide the location, `PATH_TO_CREDENTIAL_FILE`, of the JSON service account key that you downloaded when you created your service account (see Creating a service account):
            
            kubectl create secret generic cloudsql-oauth-credentials \
              --from-file=credentials.json=PATH_TO_CREDENTIAL_FILE
            

     2. To create the secrets for database access, use the SQL database, username, and password defined when you created backing services. See Set up a Cloud SQL for PostgreSQL instance:
            
            kubectl create secret generic cloudsql \
              --from-literal=database=DATABASE_NAME \
              --from-literal=username=DATABASE_USERNAME \
              --from-literal=password=DATABASE_PASSWORD
            

  2. Retrieve the public Docker image for the Cloud SQL proxy.
         
         docker pull b.gcr.io/cloudsql-docker/gce-proxy
         

  3. Build a Docker image, replacing `<your-project-id>` with your project ID.
         
         docker build -t gcr.io/PROJECT_ID/polls .
         

  4. Configure Docker to use `gcloud` as a credential helper, so that you can push the image to [Container Registry](https://docs.cloud.google.com/container-registry):
         
         gcloud auth configure-docker
         

  5. Push the Docker image. Replace `<your-project-id>` with your project ID.
         
         docker push gcr.io/PROJECT_ID/polls
         

**Note:** This command requires write access to Cloud Storage. If you run this tutorial on a Compute Engine instance, your access to Cloud Storage might be read-only. To get write access, [create a service account](https://console.cloud.google.com/project/_/iam-admin/serviceaccounts) and [use the service account to authenticate](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) on your instance.
  6. Create the GKE resource:
         
         kubectl create -f polls.yaml
         

**Note:** If you used different names _(other than**cloudsql-oauth-credentials** and **cloudsql**)_ when creating the secrets in the previous commands, then you need to update the `polls.yaml` file to match those new names.



### Deploy the app to GKE

After the resources are created, there are three `polls` pods on the cluster. Check the status of your pods:
    
    
    kubectl get pods
    

Wait a few minutes for the pod statuses to display as `Running`. If the pods aren't ready or if you see restarts, you can get the logs for a particular pod to figure out the issue. `[YOUR-POD-ID]` is a part of the output returned by the previous `kubectl get pods` command.
    
    
    kubectl logs [YOUR_POD_ID]
    

## See the app run in Google Cloud

After the pods are ready, you can get the external IP address of the load balancer:
    
    
    kubectl get services polls
    

Note the `EXTERNAL-IP` address, and go to `http://[EXTERNAL-IP]` in your browser to see the Django polls landing page and access the administrator console.

## Understand the code

### Sample application

The Django sample app was created using standard Django tooling. The following commands create the project and the polls app:
    
    
    django-admin startproject mysite
    python manage.py startapp polls
    

The base views, models, and route configurations were copied from [Writing your first Django app](https://docs.djangoproject.com/en/stable/#first-steps) ([Part 1](https://docs.djangoproject.com/en/stable/intro/tutorial01/) and [Part 2](https://docs.djangoproject.com/en/stable/intro/tutorial02/)).

### Database configuration

The `settings.py` contains the configuration for your SQL database:
    
    
    DATABASES = {
        "default": {
            # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
            # 'ENGINE': 'django.db.backends.mysql' instead of the following.
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }

### Kubernetes pod configurations

The `polls.yaml` file specifies two Kubernetes resources. The first is the [Service](http://kubernetes.io/docs/user-guide/services/), which defines a consistent name and internal IP address for the Django web app. The second is an [HTTP load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/load-balancer) with a public-facing external IP address.
    
    
    # The polls service provides a load-balancing proxy over the polls app
    # pods. By specifying the type as a 'LoadBalancer', Kubernetes Engine will
    # create an external HTTP load balancer.
    # For more information about Services see:
    #   https://kubernetes.io/docs/concepts/services-networking/service/
    # For more information about external HTTP load balancing see:
    #   https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
    apiVersion: v1
    kind: Service
    metadata:
      name: polls
      labels:
        app: polls
    spec:
      type: LoadBalancer
      ports:
      - port: 80
        targetPort: 8080
      selector:
        app: polls

The service provides a network name and IP address, and GKE pods run the app's code behind the service. The `polls.yaml` file specifies a [deployment](http://kubernetes.io/docs/user-guide/deployments/) that provides declarative updates for GKE pods. The service directs traffic to the deployment by matching the service's selector to the deployment's label. In this case, the selector `polls` is matched to the label `polls`.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: polls
      labels:
        app: polls
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: polls
      template:
        metadata:
          labels:
            app: polls
        spec:
          containers:
          - name: polls-app
            # Replace  with your project ID or use `make template`
            image: gcr.io/<your-project-id>/polls
            # This setting makes nodes pull the docker image every time before
            # starting the pod. This is useful when debugging, but should be turned
            # off in production.
            imagePullPolicy: Always
            env:
                - name: DATABASE_NAME
                  valueFrom:
                    secretKeyRef:
                      name: cloudsql
                      key: database
                - name: DATABASE_USER
                  valueFrom:
                    secretKeyRef:
                      name: cloudsql
                      key: username
                - name: DATABASE_PASSWORD
                  valueFrom:
                    secretKeyRef:
                      name: cloudsql
                      key: password
            ports:
            - containerPort: 8080
    
          - image: gcr.io/cloudsql-docker/gce-proxy:1.16
            name: cloudsql-proxy
            command: ["/cloud_sql_proxy", "--dir=/cloudsql",
                      "-instances=<your-cloudsql-connection-string>=tcp:5432",
                      "-credential_file=/secrets/cloudsql/credentials.json"]
            volumeMounts:
              - name: cloudsql-oauth-credentials
                mountPath: /secrets/cloudsql
                readOnly: true
              - name: ssl-certs
                mountPath: /etc/ssl/certs
              - name: cloudsql
                mountPath: /cloudsql
          volumes:
            - name: cloudsql-oauth-credentials
              secret:
                secretName: cloudsql-oauth-credentials
            - name: ssl-certs
              hostPath:
                path: /etc/ssl/certs
            - name: cloudsql
              emptyDir: {}

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



### Delete the individual resources

If you don't want to delete the project, delete the individual resources.

  1. Delete the Google Kubernetes Engine cluster:
         
         gcloud container clusters delete polls
         

  2. Delete the Docker image that you pushed to Container Registry:
         
         gcloud container images delete gcr.io/PROJECT_ID/polls
         

  3. Delete the Cloud SQL instance:
         
         gcloud sql instances delete INSTANCE_NAME
         




## What's next

  * Learn how to [configure PostgreSQL for production](https://docs.cloud.google.com/solutions/setting-up-cloud-sql-for-postgresql-for-production)
  * Learn more about [Django on Google Cloud](https://docs.cloud.google.com/python/django)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
