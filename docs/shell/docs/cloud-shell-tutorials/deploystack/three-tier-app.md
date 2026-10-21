---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/three-tier-app/
title: Three Tier App \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.921739+00:00
---

# Three Tier App  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/three-tier-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Three Tier App Stay organized with collections  Save and categorize content based on your preferences. 

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-todo.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/arch-todo.svg)

Three Tier App is a simple todo application architected as a vanilla 3 tier application:

  * Backend 
    * Database - MySQL - Cloud SQL
    * Caching - Redis - Cloud Memorystore
  * Middleware/API 
    * Container hosted API - Golang - Cloud Run
  * Front End/UI 
    * Container hosted UI - Nginx + HTML/JS/CSS - Cloud Run
  * Deployment 
    * Continuous Deployment - Cloud Build
    * Secret Management - Cloud Secret Manager



* * *

## Get Started

Click on the following link to a copy of the source code in Cloud Shell. Once there, a single command will spin up a working copy of the application in your project..

**Key Point:** Clicking on the following link will open a Cloud Shell session and download code from GitHub. You will have to authorize DeployStack to run. No actions will be taken until you do so. 

[ ![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/googlecloudplatform/deploystack-three-tier-app&shellonly=true&cloudshell_image=gcr.io/ds-artifacts-cloudshell/deploystack_custom_image)

[View source code on GitHub](https://github.com/googlecloudplatform/deploystack-three-tier-app)

* * *

## Three Tier App components

The Three Tier App architecture makes use of several products. The following lists the components, along with more information on the components, including links to related videos, product documentation, and interactive walkthroughs.  |  |  | Video | Docs | Walkthroughs  
---|---|---|---|---|---  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_sql.svg) | **Cloud SQL** |  Cloud SQL is managed SQL providing MySQL, SQL Server, or Postgres for the database layer of your applications.  |  [smart_display](https://www.youtube.com/watch?v=BQlQ-BTMR1U) |  [description](https://cloud.google.com/sql/docs/mysql/quickstart) |  [keyboard](https://console.cloud.google.com/?tutorial=sql--mysql--quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/memorystore.svg) | **Cloud Memorystore** |  Cloud Memorystore, managed Redis, provides the caching layer for your applications.  |  [smart_display](https://www.youtube.com/watch?v=sVpoAdbh2nU) |  [description](https://cloud.google.com/memorystore/docs/redis/) |  [keyboard](https://console.cloud.google.com/?tutorial=memorystore__memorystore_redis_gcloud_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_run.svg) | **Cloud Run** |  Cloud Run allows you to run applications in a container, but in a serverless way, no having to configure number of instances, processors, or memory. Upload a container, get a url.  |  [smart_display](https://www.youtube.com/watch?v=nhwYc4StHIc) |  [description](https://cloud.google.com/run/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_run_quickstart_index)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/cloud_build.svg) | **Cloud Build** |  Cloud Build is the tool that packages up the containers and deploys them to be available as Cloud Run services.  |  [smart_display](https://www.youtube.com/watch?v=w7dMHiEyGAs) |  [description](https://cloud.google.com/build/docs) |  [keyboard](https://console.cloud.google.com/?tutorial=cloud_build_quickstart)  
![](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/secret_manager.svg) | **Secret Manager** |  Cloud Secret Manager stores sensitive particulars about the application for the build process.  |  [smart_display](https://www.youtube.com/watch?v=JIE89dneaGo) |  [description](https://cloud.google.com/secret-manager/docs) |  [keyboard](https://console.cloud.google.com/?walkthrough_id=secret-manager__create_secret_secretmanager)  
  
* * *

## Scripts

The install script uses an executable written in `go` and Terraform CLI tools to take an empty project and install the application in it. The output should be a working application and a url for the load balancing IP address.

**Note:** The following is a breakdown of the commands that run when deploying Three Tier App. _You don't need to run each command individually; Click the Open in Cloud Shell button in the Getting Started section and run all commands._

### `./main.tf`

#### Enable services

Google Cloud Services are disabled in a project by default. ToDo requires you to enable the following services:

  * **Service Networking & Serverless VPC Access** \- allows Cloud Run to Communicate with SQL and Redis on private network, keeping these servers inaccessible from outside calls coming from the API.
  * **Cloud Build** \- creates container images and deploys to Cloud Run
  * **Cloud Memorystore** \- provides a caching layer for the application.
  * **Cloud Run** \- the serverless tool which will host the containers, and provide URLS from which to access the application.
  * **Cloud SQL** \- database storage for the application
  * **Cloud Storage** \- used by Cloud Build, and to load the schema in the database
  * **Cloud Secret Manager** \- used to inject the host ips for SQL and Redis into Cloud Build for Cloud Run.
  * **Artifact Registry** \- stores the Docker images for use with Cloud Build.


    
    
    variable "gcp_service_list" {
        description = "The list of apis necessary for the project"
        type        = list(string)
        default = [
            "compute.googleapis.com",
            "cloudapis.googleapis.com",
            "vpcaccess.googleapis.com",
            "servicenetworking.googleapis.com",
            "cloudbuild.googleapis.com",
            "sql-component.googleapis.com",
            "sqladmin.googleapis.com",
            "storage.googleapis.com",
            "secretmanager.googleapis.com",
            "run.googleapis.com",
            "artifactregistry.googleapis.com",
            "redis.googleapis.com"
        ]
    }
    
    resource "google_project_service" "all" {
        for_each                   = toset(var.gcp_service_list)
        project                    = var.project_number
        service                    = each.key
        disable_on_destroy = false
    }
    

#### Set permissions

The following command sets IAM Roles and Permissions that allow Cloud Build to deploy services.

  * Enable Cloud Build Service Account to deploy to Cloud Run
  * Enable Cloud Build Service Account to set VPN Access for Cloud Run
  * Enable Cloud Build Service Account to perform Service Account activities
  * Enable Cloud Build Service Account to act on behalf of Compute Service Account
  * Enable Cloud Build Service Account to publish to Cloud Run
  * Enable Cloud Build Service Account to consume secrets
  * Enable Cloud Build Service Account to store containers in Artifact Registry


    
    
    variable "build_roles_list" {
        description = "The list of roles that build needs for"
        type        = list(string)
        default = [
            "roles/run.developer",
            "roles/vpaccess.user",
            "roles/iam.serviceAccountUser",
            "roles/run.admin",
            "roles/secretmanager.secretAccessor",
            "roles/artifactregistry.admin",
        ]
    }
    resource "google_project_iam_member" "allbuild" {
        for_each   = toset(var.build_roles_list)
        project    = var.project_number
        role       = each.key
        member     = "serviceAccount:${local.sabuild}"
        depends_on = [google_project_service.all]
    }
    

#### Create networking for SQL instance

The following command allows Cloud SQL to be accessible from Cloud Run:
    
    
    resource "google_compute_global_address" "google_managed_services_vpn_connector" {
        name          = "google-managed-services-vpn-connector"
        purpose       = "VPC_PEERING"
        address_type  = "INTERNAL"
        prefix_length = 16
        network       = local.defaultnetwork
        project       = var.project_id
        depends_on    = [google_project_service.all]
    }
    resource "google_service_networking_connection" "vpcpeerings" {
        network                 = local.defaultnetwork
        service                 = "servicenetworking.googleapis.com"
        reserved_peering_ranges = [google_compute_global_address.google_managed_services_vpn_connector.name]
    }
    

#### Create VPC access connector

Connects Cloud Run to Database and Caching 
    
    
    resource "google_vpc_access_connector" "connector" {
        provider      = google-beta
        project       = var.project_id
        name          = "vpc-connector"
        ip_cidr_range = "10.8.0.0/28"
        network       = "default"
        region        = var.region
        depends_on    = [google_compute_global_address.google_managed_services_vpn_connector, google_project_service.all]
    }
    

#### Create Redis Server

Configures and initializes a Redis server instance. 
    
    
    resource "google_redis_instance" "todo_cache" {
        authorized_network      = local.defaultnetwork
        connect_mode            = "DIRECT_PEERING"
        location_id             = var.zone
        memory_size_gb          = 1
        name                    = "${var.basename}-cache"
        project                 = var.project_id
        redis_version           = "REDIS_6_X"
        region                  = var.region
        reserved_ip_range       = "10.137.125.88/29"
        tier                    = "BASIC"
        transit_encryption_mode = "DISABLED"
        depends_on              = [google_project_service.all]
    }
    

#### Create SQL server

The following command configures and initializes a SQL server instance.
    
    
    resource "google_sql_database_instance" "todo_database" {
        name="${var.basename}-db-${random_id.id.hex}"
        database_version = "MYSQL_5_7"
        region           = var.region
        project          = var.project_id
        settings {
            tier                  = "db-g1-small"
            disk_autoresize       = true
            disk_autoresize_limit = 0
            disk_size             = 10
            disk_type             = "PD_SSD"
            ip_configuration {
                ipv4_enabled    = false
                private_network = local.defaultnetwork
            }
            location_preference {
                zone = var.zone
            }
        }
        deletion_protection = false
        depends_on = [
            google_project_service.all,
            google_service_networking_connection.vpcpeerings
        ]
        # This handles loading the schema after the database installs.
        provisioner "local-exec" {
            working_dir = "${path.module}/code/database"
            command     = "./load_schema.sh ${var.project_id} ${google_sql_database_instance.todo_database.name}"
        }
    }
    

#### Create Artifact Registry repository

The following command stores Docker Images for use with Cloud Run.
    
    
    resource "google_artifact_registry_repository" "todo_app" {
        provider      = google-beta
        format        = "DOCKER"
        location      = var.region
        project       = var.project_id
        repository_id = "${var.basename}-app"
        depends_on    = [google_project_service.all]
    }
    

#### Create secrets

The following command stores Redis and SQL host data in Cloud Secrets.
    
    
    resource "google_secret_manager_secret" "redishost" {
        project = var.project_number
        replication {
            automatic = true
        }
        secret_id  = "redishost"
        depends_on = [google_project_service.all]
    }
    resource "google_secret_manager_secret_version" "redishost" {
        enabled     = true
        secret      = "projects/${var.project_number}/secrets/redishost"
        secret_data = google_redis_instance.todo_cache.host
        depends_on  = [google_project_service.all, google_redis_instance.todo_cache, google_secret_manager_secret.redishost]
    }
    resource "google_secret_manager_secret" "sqlhost" {
        project = var.project_number
        replication {
            automatic = true
        }
        secret_id  = "sqlhost"
        depends_on = [google_project_service.all]
    }
    resource "google_secret_manager_secret_version" "sqlhost" {
        enabled     = true
        secret      = "projects/${var.project_number}/secrets/sqlhost"
        secret_data = google_sql_database_instance.todo_database.private_ip_address
        depends_on  = [google_project_service.all, google_sql_database_instance.todo_database, google_secret_manager_secret.sqlhost]
    }
    
    

#### Create artifact for middleware

The following command creates the Docker image and hosts it on Artifact Registry: ./code/frontend/clouldbuild.yaml
    
    
    resource "null_resource" "cloudbuild_api" {
      provisioner "local-exec" {
        working_dir = "${path.module}/code/middleware"
        command     = "gcloud builds submit . --substitutions=_REGION=${var.region},_BASENAME=${var.basename}"
      }
      depends_on = [
        google_artifact_registry_repository.todo_app,
        google_secret_manager_secret_version.redishost,
        google_secret_manager_secret_version.sqlhost,
        google_project_service.all
      ]
    }
    

#### Deploy API container to Cloud Run

The following command uses Cloud Build to spin up a service on Cloud Run using the container you just built.
    
    
    resource "google_cloud_run_service" "api" {
        name     = "${var.basename}-api"
        location = var.region
        project  = var.project_id
    
        template {
            spec {
                containers {
                    image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.basename}-app/api"
                    env {
                        name = "REDISHOST"
                        value_from {
                            secret_key_ref {
                                name = google_secret_manager_secret.redishost.secret_id
                                key  = "latest"
                            }
                        }
                    }
                    env {
                        name = "todo_host"
                        value_from {
                            secret_key_ref {
                            name = google_secret_manager_secret.sqlhost.secret_id
                            key  = "latest"
                            }
                        }
                    }
                    env {
                        name  = "todo_user"
                        value = "todo_user"
                    }
                    env {
                        name  = "todo_pass"
                        value = "todo_pass"
                    }
                    env {
                        name  = "todo_name"
                        value = "todo"
                    }
                    env {
                        name  = "REDISPORT"
                        value = "6379"
                    }
                }
            }
            metadata {
                annotations = {
                    "autoscaling.knative.dev/maxScale"        = "1000"
                    "run.googleapis.com/cloudsql-instances"   = google_sql_database_instance.todo_database.connection_name
                    "run.googleapis.com/client-name"          = "terraform"
                    "run.googleapis.com/vpc-access-egress"    = "all"
                    "run.googleapis.com/vpc-access-connector" = google_vpc_access_connector.connector.id
                }
            }
        }
        autogenerate_revision_name = true
        depends_on = [
            null_resource.cloudbuild_api,
            google_project_iam_member.secretmanager_secretAccessor
        ]
    } 
    

#### Open Cloud Run API Service to be world readable.

This API layer of the application will be called by the user's browser, but by default Cloud Run services are not public. In order for users to consume this service, we have to open permissions on these services to be accessible to the world. 
    
    
    resource "google_cloud_run_service_iam_policy" "noauth_api" {
        location    = google_cloud_run_service.api.location
        project     = google_cloud_run_service.api.project
        service     = google_cloud_run_service.api.name
        policy_data = data.google_iam_policy.noauth.policy_data
    }
    

#### Create artifact for front end

The following command creates the Docker image and hosts it on Artifact Registry: ./code/frontend/clouldbuild.yaml
    
    
    resource "null_resource" "cloudbuild_fe" {
        provisioner "local-exec" {
            working_dir = "${path.module}/code/frontend"
            command     = "gcloud builds submit . --substitutions=_REGION=${var.region},_BASENAME=${var.basename}"
        }
        depends_on = [
            google_artifact_registry_repository.todo_app,
            google_cloud_run_service.api
        ]
    }
    
    

#### Deploy front end container to Cloud Run

The next command uses Cloud Build to spin up a service on Cloud Run using the container we just built
    
    
    resource "google_cloud_run_service" "fe" {
        name     = "${var.basename}-fe"
        location = var.region
        project  = var.project_id
        template {
            spec {
                containers {
                    image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.basename}-app/fe"
                    ports {
                        container_port = 80
                    }
                }
            }
        }
        depends_on = [null_resource.cloudbuild_fe]
    }
    
    

#### Open Cloud Run front end service to be world readable

This is the front end of the application, which will render the HTML/JS/CSS by which the user interacts with the application - by default Cloud Run services are not public. In order for this application to function we have to open permissions on these services to be accessible to the world. 
    
    
    resource "google_cloud_run_service_iam_policy" "noauth_fe" {
        location    = google_cloud_run_service.fe.location
        project     = google_cloud_run_service.fe.project
        service     = google_cloud_run_service.fe.name
        policy_data = data.google_iam_policy.noauth.policy_data
    }
    

### `./code/database/load_schema.sh`

#### Initialize database schema

This command makes a temporary Cloud Storage bucket to upload the schema to Cloud SQL.
    
    
    PROJECT=$1
    SQLNAME=$2
    
    SQLSERVICEACCOUNT=$(gcloud sql instances describe $SQLNAME --format="value(serviceAccountEmailAddress)" | xargs)
    gcloud storage buckets create gs://$PROJECT-temp
    gcloud storage cp schema.sql gs://$PROJECT-temp/schema.sql
    gcloud storage buckets add-iam-policy-binding gs://$PROJECT-temp/ --member=serviceAccount:$SQLSERVICEACCOUNT --role=roles/storage.objectViewer
    gcloud sql import sql $SQLNAME gs://$PROJECT-temp/schema.sql -q
    gcloud storage rm gs://$PROJECT-temp --recursive
    

### `./code/middleware/clouldbuild.yaml`

#### Build API container

This code makes a Docker image for the middleware layer.
    
    
    name: 'gcr.io/cloud-builders/docker'
    args: [ 'build', '-t', '$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/api', '.' ]
      ```
    #### Push API container to Artifact Registry
    Pushing the container to Artifact Registry makes it possible for Cloud Run to 
    get the image and serve it.
    
    ``` yaml
    name: 'gcr.io/cloud-builders/docker'
    args: ['push', '$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/api']  
    

#### Substitutions

The following code creates variables with default values so that these values can be changed at deploy time.
    
    
    substitutions:
      _REGION: us-central1
      _BASENAME: todo
    

### `./code/frontend/clouldbuild.yaml`

#### Massage code content

The front end is completely static HTML/JS/CSS. The app needs to point to the URL for the API service we just created, but Cloud Run services are assigned a url with a randomized string. This 'massage script' captures that randomized URL and injects it in to the code of the static JS in this container.

./code/frontend/massage.sh
    
    
    name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: bash
    args: [ './massage.sh', '$_REGION' ]
    

#### Build API container

The following code makes a Docker image for the middleware layer:
    
    
    name: 'gcr.io/cloud-builders/docker'
    args: [ 'build', '-t', '$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/fe', '.' ]
    

#### Push API container to Artifact Registry

Pushing the container to Artifact Registry makes it possible for Cloud Run to get the image and serve it.
    
    
    name: 'gcr.io/cloud-builders/docker'
    args: ['push', '$_REGION-docker.pkg.dev/$PROJECT_ID/$_BASENAME-app/fe']
    

#### Substitutions

Create a variable with a default so that these values can be changed a deploy time.
    
    
    substitutions:
      _REGION: us-central1
      _BASENAME: todo
    

### `./code/frontend/massage.sh`

#### Edit JavaScript

This command injects the endpoint for the Middleware into the JavaScript of the front end.
    
    
    API=$(gcloud run services describe todo-api --region=$1 --format="value(status.url)")
    stripped=$(echo ${API/https:\/\//})
    sed -i"" -e "s/127.0.0.1:9000/$stripped/" www/js/main.js
    

* * *

## Conclusion

You now have a simple 3 tier todo application running on Cloud Run in your project. You also have all of the code to modify or extend this solution to fit your environment.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
