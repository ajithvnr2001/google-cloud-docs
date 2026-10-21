---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/serverless-e2e-photo-sharing-app/
title: Serverless End-To-End Photo Sharing Application \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.589264+00:00
---

# Serverless End-To-End Photo Sharing Application  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/serverless-e2e-photo-sharing-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Serverless End-To-End Photo Sharing Application Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-e2e-serverless-photo-sharing-app.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-e2e-serverless-photo-sharing-app.svg)

Serverless End-To-End Photo Sharing Application creates a scalable end-to-end photo-sharing application with 11 Google Cloud products, Terraform, and Django.

This stack will configure and create these following components: 

  * Cloud Run - which will run the app as the main server
  * Cloud SQL - To store relational database such as user info, posts
  * Cloud Storage - To store non-relational database such as post media 
  * Cloud Load Balancer - To server traffic with multiple regions 
  * Cloud DNS - To map custom domain
  * Cloud Build - To automatically deploy your app from gcloud
  * Secret Manager - To improve the security of the app
  * Cloud VPC - To connect Cloud SQL with Cloud Run via Private improve
  * Cloud DNS - to store static cache for faster connections 
  * Translation API - to translate the post caption if it is in another language



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-serverless-e2e-photo-sharing-app&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-serverless-e2e-photo-sharing-app)

* * *

## Serverless End-To-End Photo Sharing Application components

The Serverless End-To-End Photo Sharing Application architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/identity_and_access_management.svg) | **Cloud IAM** |  Identity and Access Management (IAM) gives admins fine-grained access control and visibility for centrally managing enterprise cloud resources.  |  [smart_display](https://www.youtube.com/watch?v=LznrFv7iRNI) |  [description](https://cloud.google.com/iam/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=iam--quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_run.svg) | **Cloud Run** |  Cloud Run allows you to run applications in a container, but in a serverless way, no having to configure number of instances, processors, or memory. Upload a container, get a url.  |  [smart_display](https://www.youtube.com/watch?v=nhwYc4StHIc) |  [description](https://cloud.google.com/run/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_run_quickstart_index)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_sql.svg) | **Cloud SQL** |  Cloud SQL is managed SQL providing MySQL, SQL Server, or Postgres for the database layer of your applications.  |  [smart_display](https://www.youtube.com/watch?v=BQlQ-BTMR1U) |  [description](https://cloud.google.com/sql/docs/mysql/quickstart) |  [keyboard](https://console.cloud.google.com/?tutorial=sql--mysql--quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_storage.svg) | **Cloud Storage** |  Cloud Storage provides file storage and public serving of images over http(s).  |  [smart_display](https://www.youtube.com/watch?v=zvqJ-pcQChE) |  [description](https://cloud.google.com/storage/docs/quickstart-console) |  [keyboard](https://console.cloud.google.com/?tutorial=storage--quickstart-basic-tasks)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/compute_engine.svg) | **Compute Engine** |  Compute Engine is Google Cloud's Virtual technology. With it you can spin up many different configurations of VM to fit the shape of whatever computing needs you have.  |  [smart_display](https://www.youtube.com/watch?v=1XH0gLlGDdk) |  [description](https://cloud.google.com/compute/docs/quickstart-linux) |  [keyboard](https://console.cloud.google.com/?tutorial=compute_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/secret_manager.svg) | **Secret Manager** |  Cloud Secret Manager stores sensitive particulars about the application for the build process.  |  [smart_display](https://www.youtube.com/watch?v=JIE89dneaGo) |  [description](https://cloud.google.com/secret-manager/docs) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=secret-manager__create_secret_secretmanager)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Serverless End-To-End Photo Sharing Application. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable Services

Google Cloud Services are disabled in a project by default. In order to use any of the solutions here, we have to activate the following:

  * **Cloud Run** — the serverless tool which will host the containers, and provide URLS from which to access the application.
  * **Cloud SQL** — database storage for the application
  * **Compute Engine** — virtual machines and networking
  * **Cloud Build** — creates container images and deploys to Cloud Run
  * **Cloud Secret Manager** \- used to inject the host ips for SQL and Redis into Cloud Build for Cloud Run.
  * **Service Networking & Serverless VPC Access** \- allows Cloud Run to Communicate with SQL and Redis on private network, keeping these servers inaccessible from outside calls coming from the API.
  * **Cloud IAM** — the tool for managing access and permissions to Google Cloud Resources


    
    
    # Step 2: Activate service APIs
    resource "google_project_service" "run" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "sql-component" {
      service            = "sql-component.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "sqladmin" {
      service            = "sqladmin.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "compute" {
      service            = "compute.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "cloudbuild" {
      service            = "cloudbuild.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "secretmanager" {
      service            = "secretmanager.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "vpcaccess" {
      service            = "vpcaccess.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "servicenetworking" {
      service            = "servicenetworking.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "iam" {
      service            = "iam.googleapis.com"
      disable_on_destroy = false
    }
    

#### Create a private network

The following command creates a private network for all of the resources to use to communicate securely within the application. 
    
    
    resource "google_compute_network" "main" {
      provider   = google
      name       = "social-media-network-${random_id.name.hex}"
      depends_on = [google_project_iam_member.serviceagent]
    }
    

#### Create networking for SQL instance

The following command allows Cloud SQL to be accessible from Cloud Run:
    
    
    resource "google_compute_global_address" "private_ip_address" {
      provider      = google-beta
      project       = var.project
      name          = local.private_ip_name
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 16
      network       = google_compute_network.main.id
      depends_on    = [google_project_service.vpcaccess, google_project_iam_member.serviceagent]
    }
    
    resource "google_service_networking_connection" "private_vpc_connection" {
      provider = google-beta
    
      network                 = google_compute_network.main.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
      depends_on              = [google_project_service.vpcaccess, google_project_iam_member.serviceagent]
    }
    

#### Allow Service Agent access to the project

This command allows the service agent to access to the project to enable configation of the VPC connector. 
    
    
    resource "google_project_iam_member" "serviceagent" {
      project = data.google_project.project.number
      role    = "roles/editor"
      member  = local.serviceagent_serviceaccount
    }
    

#### Create VPC access connector

This command connects Cloud Run to Database 
    
    
    resource "google_vpc_access_connector" "connector" {
      for_each      = { "us-west1" : 8, "us-central1" : 9, "us-east1" : 10 }
      name          = "vpc-con-${each.key}"
      ip_cidr_range = "10.${each.value}.0.0/28"
      region        = each.key
      network       = google_compute_network.main.name
      depends_on    = [google_project_service.vpcaccess, google_project_iam_member.serviceagent]
    }
    

#### Create Service Account

This command creates a service account for the application to use to authenticate to all of the resources it needs to serve the app.
    
    
    # Step 4: Create a custom Service Account
    resource "google_service_account" "django" {
      account_id = "django"
      depends_on = [
        google_project_service.iam
      ]
    }
    

#### Create SQL server

The following set of commands configures and initializes a SQL server instance.
    
    
    resource "random_string" "random" {
      length  = 4
      special = false
    }
    
    resource "random_password" "database_password" {
      length  = 32
      special = false
    }
    
    resource "random_id" "name" {
      byte_length = 2
    }
    
    resource "random_id" "db_name_suffix" {
      byte_length = 4
    }
    
    resource "google_sql_database_instance" "instance" {
      name             = local.sql_database_name
      database_version = "MYSQL_8_0"
      region           = var.region
      project          = var.project
      depends_on       = [google_vpc_access_connector.connector]
      settings {
        tier = "db-f1-micro"
        ip_configuration {
          ipv4_enabled    = "true"
          private_network = google_compute_network.main.id
        }
      }
      deletion_protection = false
    }
    
    resource "google_sql_database" "database" {
      name     = "django"
      instance = google_sql_database_instance.instance.name
    }
    
    resource "google_sql_user" "django" {
      name     = "django"
      instance = google_sql_database_instance.instance.name
      password = random_password.database_password.result
    }
    

#### Create Storage buckets

Creates the Storage location for the media for the application to be stored and served to users.
    
    
    resource "google_storage_bucket" "media" {
      name     = "${var.project}-bucket"
      location = "US"
    }
    
    resource "google_storage_bucket_iam_binding" "main" {
      bucket = google_storage_bucket.media.name
      role   = "roles/storage.objectViewer"
      members = [
        "allUsers",
      ]
    }
    

#### Create secrets

The following set of commands creates sensitive application settings and resources to store them in Cloud Secrets.
    
    
    resource "google_secret_manager_secret_version" "django_settings" {
      secret = google_secret_manager_secret.django_settings.id
    
      secret_data = templatefile("etc/env.tpl", {
        bucket     = google_storage_bucket.media.name
        secret_key = random_password.django_secret_key.result
        user       = google_sql_user.django
        instance   = google_sql_database_instance.instance
        database   = google_sql_database.database
      })
    }
    
    resource "random_password" "django_secret_key" {
      special = false
      length  = 50
    }
    
    resource "google_secret_manager_secret" "django_settings" {
      secret_id = "django_settings"
    
      replication {
        automatic = true
      }
      depends_on = [google_project_service.secretmanager]
    
    }
    

#### Set Service Account permissions

This command allows the Cloud Build and Application Service account to access content in Cloud Secrets. 
    
    
    resource "google_secret_manager_secret_iam_binding" "django_settings" {
      secret_id = google_secret_manager_secret.django_settings.id
      role      = "roles/secretmanager.admin"
      members   = [local.cloudbuild_serviceaccount, local.django_serviceaccount]
    }
    

#### Populate secrets

The following set of commands creates stores application secrets in Cloud Secrets.
    
    
    resource "google_secret_manager_secret" "main" {
      for_each = {
        "DATABASE_PASSWORD" : google_sql_user.django.password,
        "DATABASE_USER" : google_sql_user.django.name,
        "DATABASE_NAME" : google_sql_database.database.name,
        "DATABASE_HOST_PROD" : google_sql_database_instance.instance.private_ip_address,
        "DATABASE_PORT_PROD" : 3306,
        "PROJECT_ID" : var.project,
        "GS_BUCKET_NAME" : var.project,
      }
      secret_id = each.key
      replication {
        automatic = true
      }
    
      depends_on = [google_sql_user.django, google_sql_database.database, google_sql_database_instance.instance]
    
    }
    
    resource "google_secret_manager_secret" "network" {
      for_each = {
        "EXTERNAL_IP" : module.lb-http.external_ip,
      }
      secret_id = each.key
      replication {
        automatic = true
      }
      depends_on = [module.lb-http, google_compute_network.main, google_cloud_run_service.service]
    }
    
    resource "google_secret_manager_secret" "url" {
      for_each = {
        "WEBSITE_URL_US_CENTRAL1" : google_cloud_run_service.service["us-central1"].status[0].url,
        "WEBSITE_URL_US_WEST1" : google_cloud_run_service.service["us-west1"].status[0].url,
        "WEBSITE_URL_US_EAST1" : google_cloud_run_service.service["us-east1"].status[0].url,
      }
      secret_id = each.key
      replication {
        automatic = true
      }
      depends_on = [google_cloud_run_service.service]
    }
    
    resource "google_secret_manager_secret_version" "main" {
      for_each = { "DATABASE_PASSWORD" : google_sql_user.django.password,
        "DATABASE_USER" : google_sql_user.django.name,
        "DATABASE_NAME" : google_sql_database.database.name,
        "DATABASE_HOST_PROD" : google_sql_database_instance.instance.private_ip_address,
        "DATABASE_PORT_PROD" : 3306,
        "PROJECT_ID" : var.project,
        "GS_BUCKET_NAME" : var.project,
      }
      secret      = google_secret_manager_secret.main[each.key].id
      secret_data = each.value
    }
    
    resource "google_secret_manager_secret_version" "network" {
      for_each = {
        "EXTERNAL_IP" : module.lb-http.external_ip,
      }
      secret      = google_secret_manager_secret.network[each.key].id
      secret_data = each.value
    }
    
    resource "google_secret_manager_secret_version" "url" {
      for_each = {
        "WEBSITE_URL_US_CENTRAL1" : google_cloud_run_service.service["us-central1"].status[0].url,
        "WEBSITE_URL_US_WEST1" : google_cloud_run_service.service["us-west1"].status[0].url,
        "WEBSITE_URL_US_EAST1" : google_cloud_run_service.service["us-east1"].status[0].url,
      }
      secret      = google_secret_manager_secret.url[each.key].id
      secret_data = each.value
    }
    
    resource "google_secret_manager_secret_iam_binding" "main" {
      for_each = { "DATABASE_PASSWORD" : google_sql_user.django.password,
        "DATABASE_USER" : google_sql_user.django.name,
        "DATABASE_NAME" : google_sql_database.database.name,
        "DATABASE_HOST_PROD" : google_sql_database_instance.instance.private_ip_address,
        "DATABASE_PORT_PROD" : 3306,
        "PROJECT_ID" : var.project,
        "GS_BUCKET_NAME" : var.project,
      }
      secret_id = google_secret_manager_secret.main[each.key].id
      role      = "roles/secretmanager.secretAccessor"
      members   = [local.cloudbuild_serviceaccount]
    }
    
    resource "google_secret_manager_secret_iam_binding" "network" {
      for_each = {
        "EXTERNAL_IP" : module.lb-http.external_ip,
      }
      secret_id = google_secret_manager_secret.network[each.key].id
      role      = "roles/secretmanager.secretAccessor"
      members   = [local.cloudbuild_serviceaccount]
    }
    
    resource "google_secret_manager_secret_iam_binding" "url" {
      for_each = {
        "WEBSITE_URL_US_CENTRAL1" : google_cloud_run_service.service["us-central1"].status[0].url,
        "WEBSITE_URL_US_WEST1" : google_cloud_run_service.service["us-west1"].status[0].url,
        "WEBSITE_URL_US_EAST1" : google_cloud_run_service.service["us-east1"].status[0].url,
      }
      secret_id = google_secret_manager_secret.url[each.key].id
      role      = "roles/secretmanager.secretAccessor"
      members   = [local.cloudbuild_serviceaccount]
    }
    
    resource "random_password" "SUPERUSER_PASSWORD" {
      length  = 32
      special = false
    }
    
    resource "google_secret_manager_secret" "SUPERUSER_PASSWORD" {
      secret_id = "SUPERUSER_PASSWORD"
      replication {
        automatic = true
      }
      depends_on = [google_project_service.secretmanager]
    }
    
    resource "google_secret_manager_secret_version" "SUPERUSER_PASSWORD" {
      secret      = google_secret_manager_secret.SUPERUSER_PASSWORD.id
      secret_data = random_password.SUPERUSER_PASSWORD.result
    }
    
    resource "google_secret_manager_secret_iam_binding" "SUPERUSER_PASSWORD" {
      secret_id = google_secret_manager_secret.SUPERUSER_PASSWORD.id
      role      = "roles/secretmanager.secretAccessor"
      members   = [local.cloudbuild_serviceaccount]
    }
    

#### Create a Container Registry record

Creates a record in Container Registry to allow for deploying a container image to Cloud Run
    
    
    resource "google_container_registry" "main" {
      project  = var.project
      location = "US"
    }
    

#### Make Container Registry Storage location public

Grants world readable access to the Container Registry location so that anyone can use the container image. 
    
    
    resource "google_storage_bucket_iam_member" "repo_public" {
      bucket = google_container_registry.main.id
      role   = "roles/storage.objectViewer"
      member = "allUsers"
    }
    

#### Create container image

The following command creates the Docker image and hosts it on Container Registry:
    
    
    resource "null_resource" "cloudbuild_api" {
      provisioner "local-exec" {
        working_dir = path.module
        command     = "gcloud builds submit . "
      }
    
      depends_on = [
        google_container_registry.main
      ]
    }
    

#### Deploy container to Cloud Run

The following command uses Cloud Build to spin up a service on Cloud Run using the container you just built.
    
    
    resource "google_cloud_run_service" "service" {
      for_each                   = toset([for location in local.runlocations : location if can(regex("us-(?:west|central|east)1", location))])
      name                       = var.project
      location                   = each.value
      project                    = var.project
      autogenerate_revision_name = true
      depends_on = [
        # google_sql_database_instance.instance,
        google_service_account.django,
        google_sql_database_instance.instance,
        google_vpc_access_connector.connector,
      ]
    
      template {
        spec {
          service_account_name = google_service_account.django.email
          containers {
            image = "gcr.io/${var.project}/${var.service}:latest"
            env {
              name  = "PROJECT_ID"
              value = var.project
            }
          }
        }
    
        metadata {
          annotations = {
            "autoscaling.knative.dev/maxScale"        = "100"
            "run.googleapis.com/cloudsql-instances"   = google_sql_database_instance.instance.connection_name
            "run.googleapis.com/client-name"          = "terraform"
            "run.googleapis.com/vpc-access-connector" = google_vpc_access_connector.connector[each.key].name
            "run.googleapis.com/vpc-access-egress"    = "all-traffic"
          }
        }
      }
    
      traffic {
        percent         = 100
        latest_revision = true
      }
    }
    

#### Open Cloud Run API Service to be world readable.

This API layer of the application will be called by the user's browser, but by default Cloud Run services are not public. In order for users to consume this service, we have to open permissions on these services to be accessible to the world. 
    
    
    resource "google_cloud_run_service_iam_policy" "noauth" {
      for_each = toset([for location in local.runlocations : location if can(regex("us-(?:west|central|east)1", location))])
      location = google_cloud_run_service.service[each.key].location
      project  = google_cloud_run_service.service[each.key].project
      service  = google_cloud_run_service.service[each.key].name
    
      policy_data = data.google_iam_policy.noauth.policy_data
    }
    

#### Create load balancer

The following command creates a load balancer and implements health checks and backend services. It configures the load balancer to connect to the Cloud Run service.
    
    
    # Step 11: Create Load Balancer to handle traffics from multiple regions 
    resource "google_compute_region_network_endpoint_group" "default" {
      for_each              = toset([for location in local.runlocations : location if can(regex("us-(?:west|central|east)1", location))])
      name                  = "${var.project}--neg--${each.key}"
      network_endpoint_type = "SERVERLESS"
      region                = google_cloud_run_service.service[each.key].location
      cloud_run {
        service = google_cloud_run_service.service[each.key].name
      }
      depends_on = [google_cloud_run_service.service]
    }
    
    module "lb-http" {
      source  = "GoogleCloudPlatform/lb-http/google//modules/serverless_negs"
      version = "~> 4.5"
    
      project = var.project
      name    = var.project
    
      ssl                             = false
      https_redirect                  = true
      managed_ssl_certificate_domains = []
      use_ssl_certificates            = false
      backends = {
        default = {
          description            = null
          enable_cdn             = true
          custom_request_headers = null
    
          log_config = {
            enable      = true
            sample_rate = 1.0
          }
    
          groups = [
            for neg in google_compute_region_network_endpoint_group.default :
            {
              group = neg.id
            }
          ]
    
          iap_config = {
            enable               = false
            oauth2_client_id     = null
            oauth2_client_secret = null
          }
          security_policy = null
        }
      }
    }
    

#### Grant various permissions

The following set of commands grants permissions to the database accounts, and the Cloud Build service accounts.
    
    
    # Step 12: Grant access to the database
    resource "google_project_iam_member" "service_permissions_cb_django" {
      for_each = toset([
        "run.admin", "cloudsql.client", "editor", "secretmanager.admin"
      ])
    
    
    
      role   = "roles/${each.key}"
      member = local.django_serviceaccount
    }
    
    resource "google_project_iam_member" "service_permissions_cb" {
      for_each = toset([
        "run.admin", "cloudsql.client", "editor", "secretmanager.admin"
      ])
    
    
    
      role   = "roles/${each.key}"
      member = local.cloudbuild_serviceaccount
    }
    
    resource "google_service_account_iam_binding" "cloudbuild_sa" {
      service_account_id = google_service_account.django.name
      role               = "roles/editor"
    
      members = [local.cloudbuild_serviceaccount]
    }
    

* * *

## Conclusion

Once run you should now have a completely installed application running in several regions that allows for social media sharing. Additionally you should have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
