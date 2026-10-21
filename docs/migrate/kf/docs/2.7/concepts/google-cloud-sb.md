---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/google-cloud-sb/
title: Install the GCP Service Broker \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:34:43.105963+00:00
---

# Install the GCP Service Broker  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/google-cloud-sb/

Version 2.7

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)



Send feedback 

#  Install the GCP Service Broker Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The GCP Service Broker is not an officially supported Google product and is not a supported component of Kf.

This document is a modified version of the documentation found on the GitHub repository for the [GCP Service Broker](https://github.com/GoogleCloudPlatform/gcp-service-broker/tree/master/deployments/helm/gcp-service-broker).

## Prerequisites

  1. A cluster with Kf installed.
  2. **`gcloud`** : Follow [these instructions](https://docs.cloud.google.com/sdk/install) to install the `gcloud` CLI.
  3. **`kubectl`** : Once `gcloud` is installed, run `gcloud components install kubectl`.
  4. **`helm`** : Follow [these instructions](https://helm.sh/docs/intro/install/) to install the `helm` CLI.
  5. **`git`** : Git is required to clone a repository.



## Configuration

### Select a project

Choose the Google Cloud project you want to use for the rest of this tutorial. It should be the same project used by your Kf cluster.

You must be an owner of the project you choose. Optionally change the values below to reflect your environment, then set these environment variables in your terminal:
    
    
    export PROJECT_ID=$(gcloud config get-value project)
    export SERVICE_ACCOUNT_NAME=kf-gcp-broker

### Create a service account for the broker

  1. Create the service account:
         
         gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME

  2. Create new credentials to let the broker authenticate, and download the credential to `key.json`:
         
         gcloud iam service-accounts keys create key.json --iam-account $SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com

  3. Grant project owner permissions to the broker:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com --role "roles/owner"

**Note:** Instead of using owner permissions, you can add admin permissions to the broker for each individual service you want to provision with the broker.



### Enable required APIs

Now you need to enable APIs to let the broker provision resources.

The broker has a few APIs that are required for it to run, and a few that are optional but must be enabled to provision resources of a particular type.

The Cloud Resource Manager and Identity and Access Management APIs are required for the broker to run. To enable them:
    
    
    gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com --project $PROJECT_ID

### Enable APIs

In order to provision Cloud services on your project, Kf recommends enabling at least the following APIs:

  1. [CloudSQL API](https://console.cloud.google.com/apis/library/sql-component.googleapis.com)
  2. [CloudSQL Admin API](https://console.cloud.google.com/apis/library/sqladmin.googleapis.com)
  3. [Pub/Sub API](https://console.cloud.google.com/apis/api/pubsub/overview)
  4. [Redis API](https://console.cloud.google.com/apis/api/redis.googleapis.com/overview)
  5. [Storage API](https://console.cloud.google.com/apis/api/storage_component/overview)



The GCP Service Broker also supports a variety of other services you can add support for by enablig the APIs [listed here](https://github.com/GoogleCloudPlatform/gcp-service-broker/blob/master/docs/installation.md).

## Install the service broker

  1. Clone the GCP Service Broker to your local workstation and `cd` to it:
         
         git clone --depth=1 "https://github.com/GoogleCloudPlatform/gcp-service-broker"
         cd gcp-service-broker/deployments/helm/gcp-service-broker

  2. Update the dependencies of the Helm chart:
         
         helm dependency update

  3. Edit the file `values.yaml` and set the value of `broker.service_account_json` to be a string containing the entire contents of `key.json`.

**Optional:** read through the rest of the properties and change any you need to fit your environment.
         
         # ...
         broker:
           # ...
           **service_account_json : "contents of key.json go here"**
         # ...

  4. If running in a production environment, set `mysql.embedded` to false and provide credentials for an external MySQL database that has automatic backups and failover.

**Note:** The built-in database can get you running quickly, but should not be used as a production ready solution.
  5. Create a Kubernetes namespace for the GCP Service Broker:
         
         kubectl create namespace gcp-service-broker

  6. Install the broker:
         
         helm install gcp-service-broker --set svccat.register=false --namespace gcp-service-broker .

**Note:** If you get an error about invalid YAML in `secrets.yaml`, make sure the `broker.service_account_json` field in `values.yaml` was formatted as a string.
  7. Register the broker with Kf:
         
         kf create-service-broker gcp-service-broker \
           "$(kubectl get secret gcp-service-broker-auth -n gcp-service-broker -o jsonpath='{.data.username}' | base64 --decode)" \
           "$(kubectl get secret gcp-service-broker-auth -n gcp-service-broker -o jsonpath='{.data.password}' | base64 --decode)" \
           "http://gcp-service-broker.gcp-service-broker.svc.cluster.local"

**Note:** It may take several minutes for the broker to be reachable.



## Confirm broker installation

Run `kf marketplace`. You should see output similar to:
    
    
    Broker              Name                          Space       Status  Description
    gcp-service-broker  google-stackdriver-profiler               Active  Continuous CPU and heap profiling to improve performance and reduce costs.
    gcp-service-broker  google-stackdriver-monitoring             Active  Stackdriver Monitoring provides visibility into the performance, uptime, and overall health of cloud
    gcp-service-broker  google-dataflow                           Active  A managed service for executing a wide variety of data processing patterns built on Apache Beam.
    gcp-service-broker  google-cloudsql-mysql                     Active  Google CloudSQL for MySQL is a fully-managed MySQL database service.
    gcp-service-broker  google-spanner                            Active  The first horizontally scalable, globally consistent, relational database service.
    gcp-service-broker  google-ml-apis                            Active  Machine Learning APIs including Vision, Translate, Speech, and Natural Language.
    gcp-service-broker  google-pubsub                             Active  A global service for real-time and reliable messaging and streaming data.
    gcp-service-broker  google-datastore                          Active  Google Cloud Datastore is a NoSQL document database service.
    gcp-service-broker  google-stackdriver-debugger               Active  Stackdriver Debugger is a feature of the Google Cloud Platform that lets you inspect the state of an
    gcp-service-broker  google-firestore                          Active  Cloud Firestore is a fast, fully managed, serverless, cloud-native NoSQL document database that simp
    gcp-service-broker  google-bigtable                           Active  A high performance NoSQL database service for large analytical and operational workloads.
    gcp-service-broker  google-storage                            Active  Unified object storage for developers and enterprises. Cloud Storage allows world-wide storage and r
    gcp-service-broker  google-stackdriver-trace                  Active  Stackdriver Trace is a distributed tracing system that collects latency data from your applications
    gcp-service-broker  google-cloudsql-postgres                  Active  Google CloudSQL for PostgreSQL is a fully-managed PostgreSQL database service.
    gcp-service-broker  google-dialogflow                         Active  Dialogflow is an end-to-end, build-once deploy-everywhere development suite for creating conversatio
    gcp-service-broker  google-bigquery                           Active  A fast, economical and fully managed data warehouse for large-scale data analytics.
    

The GCP Service Broker is installed and can be used to create services and bind them to apps you deploy with Kf.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
