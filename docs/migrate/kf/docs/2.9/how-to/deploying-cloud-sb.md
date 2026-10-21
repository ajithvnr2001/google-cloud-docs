---
url: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/deploying-cloud-sb/
title: Deploy Kf Cloud Service Broker \u00a0|\u00a0 Kf 2.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:57.543429+00:00
---

# Deploy Kf Cloud Service Broker  |  Kf 2.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/deploying-cloud-sb/

Version 2.9

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
  * [ 2.9 ](https://docs.cloud.google.com/migrate/kf/docs/2.9)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.9/getting-started)



Send feedback 

#  Deploy Kf Cloud Service Broker Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to deploy Kf Cloud Service Broker for Google Cloud and use it to provision or deprovision backing resources. Read about the [concepts and architecture](https://docs.cloud.google.com/migrate/kf/docs/2.9/concepts/cloud-sb-overview) to learn more about the Kf Cloud Service Broker.

## Create environment variables

### Linux
    
    
    export PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_PROJECT_ID=YOUR_PROJECT_ID
    export CLUSTER_NAME=kf-cluster
    export INSTANCE_NAME=cloud-service-broker
    export COMPUTE_REGION=us-central1
    

### Windows PowerShell
    
    
    Set-Variable -Name PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_PROJECT_ID -Value YOUR_PROJECT_ID
    Set-Variable -Name CLUSTER_NAME -Value kf-cluster
    Set-Variable -Name INSTANCE_NAME -Value cloud-service-broker
    Set-Variable -Name COMPUTE_REGION -Value us-central1
    

## Set up the Kf Cloud Service Broker database

  1. Create a Cloud SQL for MySQL instance.

**Note:** Read [Creating and managing MySQL users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) for Cloud SQL for MySQL and set a secure password for the default `root` user.
         
         gcloud sql instances create ${INSTANCE_NAME} --cpu=2 --memory=7680MB --require-ssl --region=${COMPUTE_REGION}

  2. Create a database named `servicebroker` in the Cloud SQL for MySQL instance.

**Note:** Document the database name since it is used in later steps.
         
         gcloud sql databases create servicebroker -i ${INSTANCE_NAME}

  3. Create a username and password to be used by Kf Cloud Service Broker.

**Note:** Document these values since they will be used in later steps.
         
         gcloud sql users create csbuser -i ${INSTANCE_NAME} --password=csbpassword




## Set up a Google Service Account for Kf Cloud Service Broker

  1. Create a Google Service Account.
         
         gcloud iam service-accounts create csb-${CLUSTER_NAME}-sa \
           --project=${CLUSTER_PROJECT_ID} \
           --description="GSA for CSB at ${CLUSTER_NAME}" \
           --display-name="csb-${CLUSTER_NAME}"

  2. Grant `roles/cloudsql.client` permissions to the Service Account. This is required to connect the Kf Cloud Service Broker pod to the Cloud SQL for MySQL instance through Cloud SQL Auth proxy.
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/cloudsql.client"

  3. Grant additional Google Cloud permissions to the Service Account.

**Note:** In the example below, we grant IAM roles required to provision an instance of Cloud SQL for MySQL and [Memorystore](https://docs.cloud.google.com/memorystore). You must grant this service account the appropriate roles to provision instances of other Google Cloud managed services listed in `kf marketplace`.
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/compute.networkUser"
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/cloudsql.admin"
         
         gcloud projects add-iam-policy-binding ${CLUSTER_PROJECT_ID} \
           --member="serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/redis.admin"

  4. Verify the permissions.

**Warning:** Replace the `CSB_SERVICE_ACCOUNT_NAME` variable in the YAML below with the full service account resolved from `csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com`
         
         gcloud projects get-iam-policy ${CLUSTER_PROJECT_ID} \
           --filter='bindings.members:serviceAccount:"CSB_SERVICE_ACCOUNT_NAME"' \
           --flatten="bindings[].members"




## Set up Workload Identity for Kf Cloud Service Broker

  1. Bind the Google Service Account with the Kubernetes Service Account.
         
         gcloud iam service-accounts add-iam-policy-binding "csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --project=${CLUSTER_PROJECT_ID} \
           --role="roles/iam.workloadIdentityUser" \
           --member="serviceAccount:${CLUSTER_PROJECT_ID}.svc.id.goog[kf-csb/csb-user]"

  2. Verify the binding.
         
         gcloud iam service-accounts get-iam-policy "csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com" \
           --project=${CLUSTER_PROJECT_ID}




## Set up a Kubernetes Secret to share configuration with Kf Cloud Service Broker

  1. Create a config.yml file.

**Note:** Replace the default user/password if desired. Ensure you have set the `CLUSTER_PROJECT_ID` in the Create environment variables step.
         
         cat << EOF >> ./config.yml
         gcp:
           credentials: ""
           project: ${CLUSTER_PROJECT_ID}
         db:
           host: 127.0.0.1
           password: csbpassword
           user: csbuser
           tls: false
         api:
           user: servicebroker
           password: password
         EOF

  2. Create the `kf-csb` namespace.
         
         kubectl create ns kf-csb

  3. Create the Kubernetes Secret.
         
         kubectl create secret generic csb-secret --from-file=config.yml -n kf-csb




## Install Kf Cloud Service Broker

  1. Download the `kf-csb.yml`.
         
         gcloud storage cp gs://kf-releases/csb/v1.1.0/kf-csb.yaml /tmp/kf-csb.yaml

  2. Edit `/tmp/kf-csb.yaml` and replace placeholders with final values. In the example below, `sed` is used.
         
         sed -i "s|<GSA_NAME>|csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com|g" /tmp/kf-csb.yaml
         sed -i "s|<INSTANCE_CONNECTION_NAME>|${CLUSTER_PROJECT_ID}:${COMPUTE_REGION}:${INSTANCE_NAME}|g" /tmp/kf-csb.yaml
         sed -i "s|<DB_PORT>|3306|g" /tmp/kf-csb.yaml

  3. Apply yaml for Kf Cloud Service Broker.
         
         kubectl apply -f /tmp/kf-csb.yaml

  4. Verify the Kf Cloud Service Broker installation status.
         
         kubectl get pods -n kf-csb




## Create a service broker

**Note:** The user/password must match what you entered in the Kubernetes secret step earlier.
    
    
      kf create-service-broker cloud-service-broker servicebroker password http://csb-controller.kf-csb/

## Validate installation

Check for available services in the marketplace.
    
    
      kf marketplace

If everything is installed and configured correctly, you should see the following:
    
    
      $ kf marketplace
    
      Broker                Name                          Namespace  Description
      cloud-service-broker  csb-google-bigquery                      A fast, economical and fully managed data warehouse for large-scale data analytics.
      cloud-service-broker  csb-google-dataproc                      Dataproc is a fully-managed service for running Apache Spark and Apache Hadoop clusters in a simpler, more cost-efficient way.
      cloud-service-broker  csb-google-mysql                         Mysql is a fully managed service for the Google Cloud Platform.
      cloud-service-broker  csb-google-postgres                      PostgreSQL is a fully managed service for the Google Cloud Platform.
      cloud-service-broker  csb-google-redis                         Cloud Memorystore for Redis is a fully managed Redis service for the Google Cloud Platform.
      cloud-service-broker  csb-google-spanner                       Fully managed, scalable, relational database service for regional and global application data.
      cloud-service-broker  csb-google-stackdriver-trace             Distributed tracing service
      cloud-service-broker  csb-google-storage-bucket                Google Cloud Storage that uses the Terraform back-end and grants service accounts IAM permissions directly on the bucket.
    

## Clean up

  1. Delete cloud-service-broker.
         
         kf delete-service-broker cloud-service-broker

  2. Delete CSB components.
         
         kubectl delete ns kf-csb

  3. Delete the Kf Cloud Service Broker Cloud SQL for MySQL instance.
         
         gcloud sql instances delete ${INSTANCE_NAME} --project=${CLUSTER_PROJECT_ID}

  4. Remove the IAM policy bindings.
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
         --member='serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com' \
         --role=roles/cloudsql.client
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
         --member='serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com' \
         --role=roles/compute.networkUser
         
         gcloud projects remove-iam-policy-binding ${CLUSTER_PROJECT_ID} \
         --member='serviceAccount:csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com' \
         --role=roles/redis.admin

  5. Remove the GSA.
         
         gcloud iam service-accounts delete csb-${CLUSTER_NAME}-sa@${CLUSTER_PROJECT_ID}.iam.gserviceaccount.com \
           --project=${CLUSTER_PROJECT_ID}




## What's next?

  * Test Kf Cloud Service Broker with our [Spring Music guide](https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/spring-music). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
