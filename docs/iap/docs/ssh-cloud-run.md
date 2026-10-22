---
url: https://docs.cloud.google.com/iap/docs/ssh-cloud-run/
title: Use SSH for Cloud Run \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:21.460325+00:00
---

# Use SSH for Cloud Run  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/ssh-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Use SSH for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — SSH support for Cloud Run**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use SSH to connect to Cloud Run services through Identity-Aware Proxy (IAP) TCP forwarding.

By securing your SSH connections with IAP, you can debug individual container instances in a secure environment.

## Before you begin

  1. Make sure that your Cloud Run service is running in a second-generation execution environment and includes any debugging tools that you need to execute commands once connected. For more information, see [execution environments](https://docs.cloud.google.com/run/docs/configuring/execution-environments).
  2. To ensure that you are using the latest version of the Google Cloud CLI, run the following command:
         
         gcloud components update
         

  3. Enable the Cloud Run, Cloud Resource Manager API, Cloud OS Login API, and Identity-Aware Proxy APIs in your project.

To enable the APIs, run the following command:
         
         gcloud services enable \
             cloudresourcemanager.googleapis.com \
             oslogin.googleapis.com \
             iap.googleapis.com \
             run.googleapis.com
         




### Required roles

To get the permissions that you need to configure policies and connect to workloads, ask your administrator to grant you the following IAM roles: 

  * Configure policies: 
    * [IAP Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`) on the project
    * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the project
  * Connect to workloads: 
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account
    * [Cloud Run SSH Root Access ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sshRoot) (`roles/run.sshRoot`) on the service
    * [IAP-secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) on the service
    * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the service
    * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) on the project
    * [Browser ](https://docs.cloud.google.com/iam/docs/roles-permissions/browser#browser) (`roles/browser`) on the project
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

SSH for Cloud Run has the following limitations:

  * Only Cloud Run services and instances are supported.
  * For services, only the second generation execution environment is supported.
  * Cloud Run jobs aren't supported.
  * Worker pools aren't supported.
  * When using SSH, host keys in the image are overwritten. The keys remain overwritten after the SSH session ends, until the service is restarted.
  * Windows: PuTTY is not supported. Use the OpenSSH client.



## Configure IAP authorization policies

You can manage access to Cloud Run resources at the project, region, or service level using either the gcloud CLI or the IAP REST API.

You can configure policies for the following Cloud Identity API identifiers:

  * _Cloud Identity_ : for example, `user:EMAIL@example.com`
  * _Workforce Identity Federation_ : for example: `principal://iam.googleapis.com/locations/global/workforcePools/` `<var>POOL_ID</var>/subject/<var>SUBJECT_ATTRIBUTE_VALUE</var>`



For more information and examples of principal types, see the [principal identifiers list](https://docs.cloud.google.com/iam/docs/principal-identifiers).

### Update an existing Cloud Run service

To update the service to enable SSH, run the following command:
    
    
    gcloud beta run services update \
        SERVICE_NAME \
        --region=LOCATION \
        --ssh
    

Replace the following:

  * `SERVICE_NAME`: the name of your Cloud Run service.
  * `LOCATION`: the Google Cloud region where the service is deployed (for example, `us-central1`).



You can also deploy a Cloud Run service by adding `--ssh` to [`gcloud beta run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy).

**Note:** If your project is part of an organization, you can grant service access to users who are outside of your organization by using the [Compute OS Login External User (roles/compute.osLoginExternalUser)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLoginExternalUser) role or by using a custom role with the `compute.oslogin.updateExternalUser` permission.

### Grant access to all Cloud Run resources in a project

To manage access for all resources within a project, apply the IAM policy binding at the project level.

###  gcloud 

Run the following command:
    
    
    gcloud beta iap tcp add-iam-policy-binding \
        --member='USER' \
        --role='roles/iap.tunnelResourceAccessor' \
        --resource-type=cloud-run
    

Replace `USER` with the principal identifier of the user—for example, `user:user@example.com` or the Workforce Identity Federation principal.

### REST API

Send a `POST` request to the project policy endpoint:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "policy": {
            "bindings": [
              {
                "role": "roles/iap.tunnelResourceAccessor",
                "members": ["USER"]
              }
            ]
          }
        }' \
        "https://iap.googleapis.com/v1/projects/\
    PROJECT_NUMBER/iap_tunnel/cloudRun:setIamPolicy"
    

Replace the following:

  * `USER`: the principal identifier of the user.
  * `PROJECT_NUMBER`: the Google Cloud project number where the resources are hosted.



### Grant access to all Cloud Run resources in a specific location

To restrict access to all resources within a specific region (for example, `us-central1`), apply the policy binding at the location level.

###  gcloud 

Run the following command:
    
    
    gcloud beta iap tcp add-iam-policy-binding \
        --member='USER' \
        --role='roles/iap.tunnelResourceAccessor' \
        --resource-type=cloud-run \
        --region=LOCATION
    

Replace the following:

  * `USER`: the principal identifier of the user.
  * `LOCATION`: the Google Cloud region where the resources are deployed (for example, `us-central1`).



### REST API

Send a `POST` request to the location policy endpoint:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "policy": {
            "bindings": [
              {
                "role": "roles/iap.tunnelResourceAccessor",
                "members": ["USER"]
              }
            ]
          }
        }' \
        "https://iap.googleapis.com/v1/projects/\
    PROJECT_NUMBER/iap_tunnel/cloudRun/locations/\
    LOCATION:setIamPolicy"
    

Replace the following:

  * `USER`: the principal identifier of the user
  * `PROJECT_NUMBER`: the Google Cloud project number
  * `LOCATION`: the Google Cloud region



### Grant access to a specific Cloud Run service

To restrict access to a single named service in your project, apply the policy binding at the service level.

###  gcloud 

Run the following command:
    
    
    gcloud beta iap tcp add-iam-policy-binding \
        --member='USER' \
        --role='roles/iap.tunnelResourceAccessor' \
        --resource-type=cloud-run \
        --service=SERVICE_NAME \
        --region=LOCATION
    

Replace the following:

  * `USER`: the principal identifier of the user
  * `SERVICE_NAME`: the name of the service logic to connect to
  * `LOCATION`: the Google Cloud region where the service is deployed



###  REST API

Send a `POST` request to the service policy endpoint:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "policy": {
            "bindings": [
              {
                "role": "roles/iap.tunnelResourceAccessor",
                "members": ["USER"]
              }
            ]
          }
        }' \
        "https://iap.googleapis.com/v1/projects/\
        PROJECT_NUMBER/iap_tunnel/cloudRun/locations/\
        LOCATION/services/\
        SERVICE_NAME:setIamPolicy"
    

Replace the following:

  * `USER`: the principal identifier of the user
  * `PROJECT_NUMBER`: the Google Cloud project number
  * `LOCATION`: the Google Cloud region
  * `SERVICE_NAME`: the name of the service



## Connect using SSH

To establish an SSH tunnel to a Cloud Run resource, you must use the gcloud CLI CLI.

### Connect to a service

Run the following command:
    
    
    gcloud beta run services ssh SERVICE_NAME \
        --region=LOCATION \
        --project=PROJECT_ID
    

Replace the following:

  * `SERVICE_NAME`: the name of the service to connect to
  * `LOCATION`: the Google Cloud region where the service resides
  * `PROJECT_ID`: the ID of your Google Cloud project



### Exit the session

To end your SSH session, type `exit`.

Any modifications you make to the container persist only for as long as the container is kept alive. Exiting your session doesn't automatically stop or restart the container.

## Use a local OpenSSH client

To use a local OpenSSH client for connections:

  1. To initiate the SSH tunnel and generate the necessary certificate, run the following command:
         
         gcloud beta run services ssh SERVICE_NAME \
             --region=LOCATION \
             --project=PROJECT_ID
         

Replace the following:

     * `SERVICE_NAME`: the name of the service
     * `LOCATION`: the Google Cloud region
     * `PROJECT_ID`: your Google Cloud project ID
  2. Add the following configuration code to your local `~/.ssh/config` file:
         
         Host cloud-run-ssh
             HostName cloud-run-default
             User root
             IdentityFile ~/.ssh/google_compute_engine
             CertificateFile ~/.ssh/google_compute_engine_cert/PROJECT_ID_LOCATION_SERVICE_NAME-cert.pub
             CheckHostIP no
             HashKnownHosts no
             HostKeyAlias cloud-run-default
             IdentitiesOnly yes
             StrictHostKeyChecking no
             UserKnownHostsFile /dev/null
             ProxyUseFdpass no
             ProxyCommand /usr/local/bin/python3 -S ~/google-cloud-sdk/lib/gcloud.py beta run start-iap-tunnel --project_number=PROJECT_NUMBER --project_id=PROJECT_ID --workload_type=service --deployment_name=SERVICE_NAME --region=LOCATION
         

If your `gcloud` installation path is different, update the prefix in the `ProxyCommand` path.

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID
     * `LOCATION`: the Google Cloud region
     * `SERVICE_NAME`: the name of the service
     * `PROJECT_NUMBER`: your Google Cloud project number
  3. Connect to the service using OpenSSH:
         
         ssh cloud-run-ssh
         


**Important:** The SSH certificate generated by the tunnel expires after **five minutes**. If you reconnect after this limit, you must run the `gcloud beta run services ssh` command again to generate a new certificate.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
