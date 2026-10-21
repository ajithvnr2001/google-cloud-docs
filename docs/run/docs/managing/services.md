---
url: https://docs.cloud.google.com/run/docs/managing/services/
title: Manage Cloud Run services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:45.452340+00:00
---

# Manage Cloud Run services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage Cloud Run services Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run lets you deploy and run containerized applications with automated scaling and permanent endpoints. Within a project, you can create, view, copy, disable, and delete services to maintain your workloads.

Each service receives a unique, permanent `run.app` URL that persists across new revisions. Functions deployed to Cloud Run are also treated as services and assigned a `run.app` address containing the service name and a hash.

### Required roles

To get the permissions that you need to manage Cloud Run services and revisions, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run service. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a service

You create a new service by deploying a container image to it for the first time. [Deploying a new service](https://docs.cloud.google.com/run/docs/deploying#service) has more instructions.

## View the list of services in your project

You can view a list of the available services in your project using the Google Cloud console or the Google Cloud CLI:

### Console

To view the services list:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Examine the displayed list of services for your project.




###  gcloud 

To list the services in your project:
    
    
    gcloud run services list
    

Note that each service has an associated URL.

You can filter this list by properties of the service definition, such as an [assigned label](https://docs.cloud.google.com/run/docs/configuring/services/labels#label-listing).

### Cloud Code

To view the services list with [Cloud Code](https://docs.cloud.google.com/code/docs), read the Cloud Run Explorer guides for [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/cloud-run-explorer) and [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/cloud-run-explorer).

### Client libraries

To view the list of services from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ServicesClient_ListServices)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ServicesClient#com_google_cloud_run_v2_ServicesClient_listServices_com_google_cloud_run_v2_ListServicesRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.servicesclient#_google_cloud_run_v2_ServicesClient_listServices_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.services.ServicesClient#google_cloud_run_v2_services_services_ServicesClient_list_services)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Client#Google__Cloud__Run__V2__Services__Client_list_services_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ServicesClient#_Google_Cloud_Run_V2_Client_ServicesClient__listServices__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ServicesClient#Google_Cloud_Run_V2_ServicesClient_ListServices_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view the list of services in your project, send a `GET` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/list).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to view services](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



### View the list of functions in your project

You can view a list of the available functions in your project using the Google Cloud console:

### Console

To filter for functions in your service list:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select **Filter services** > **Deployment type** > **Function**.

If you previously deployed your function using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis), the **Deployed by** column will show _Cloud Functions_.




## Copy a service

You can make a copy of an existing service using Google Cloud console or YAML. You can change anything you want in the copy, including name and region.

### Console

To copy a service:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select the checkbox next to the service you want to copy from the displayed list of services for your project.

  3. Click **Copy**.

  4. In the service copy page, set or change any values you want to change, such as region, etc. If you are keeping the same region, you must provide a new name for the service.

  5. Click **Create** to make a copy and deploy it using the new service name.




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Make the following configuration changes to the service.
         
         apiVersion: serving.knative.dev/v1
          kind: Service
          metadata:
            annotations:
              ...
            name: SERVICE
            ...
          spec:
            template:
              metadata:
                annotations:
                ...
                name: REVISION
         

     * If you are _not_ deploying the copy to a different region, replace SERVICE with the name you want to use for the copy. If you are deploying the copy to a different region, you can use the old name.
     * Replace `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Copy the service using the following command:
         
         gcloud run services replace service.yaml

Use the [`--region`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/services/replace#--region) flag to deploy the copy to a different region.




## View more details about a service

You can view more details about a service using the Google Cloud console, the Google Cloud CLI, YAML file, or REST API:

### Console

To view a service's details:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service in the displayed list of services to open the service details view.




###  gcloud 

To view details about a service: 
    
    
    gcloud run services describe SERVICE

Replace SERVICE with the name of the service. 

You can use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to format the output. For example as YAML:
    
    
    gcloud run services describe SERVICE --region REGION --format yaml

Replace:

  * SERVICE with the name of the service.
  * REGION with the Google Cloud region of the service.



You can use `--format export` to export as YAML without automatically generated labels or status:
    
    
    gcloud run services describe SERVICE --region REGION --format export

You can also use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to get the URL of the service: 
    
    
    gcloud run services describe SERVICE --region REGION --format='value(status.url)'

### Cloud Code

To view a services details with [Cloud Code](https://docs.cloud.google.com/code/docs), read the Cloud Run Explorer guides for [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/cloud-run-explorer) and [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/cloud-run-explorer).

For more details on service revisions, see [Managing Revisions](https://docs.cloud.google.com/run/docs/managing/revisions).

### Client libraries

To view details about a service from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ServicesClient_GetService)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ServicesClient#com_google_cloud_run_v2_ServicesClient_getService_com_google_cloud_run_v2_GetServiceRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.servicesclient#_google_cloud_run_v2_ServicesClient_getService_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.services.ServicesClient#google_cloud_run_v2_services_services_ServicesClient_get_service)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Client#Google__Cloud__Run__V2__Services__Client_get_service_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ServicesClient#_Google_Cloud_Run_V2_Client_ServicesClient__getService__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ServicesClient#Google_Cloud_Run_V2_ServicesClient_GetService_System_String_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view details about a service, send a `GET` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/get).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE-NAME

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to view service details](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE-NAME with the name of the service.
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



## Disable an existing service

To get the permissions that you need to disable an existing Cloud Run service and revision, ask your administrator to grant you the [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) IAM role on your project. 

When you disable a service, any requests that are currently being processed will be allowed to complete. However, any further requests to the service URL will fail with a `Service unavailable` or `Service disabled` error.

Requests to service revisions that are only active due to traffic tags are not impacted because those revisions are not disabled.

To disable a service, you set scaling to zero. You can disable a service using the Google Cloud console, the Google Cloud CLI, YAML file, or API:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you want to disable to display its detail panel, then click the **Scaling** tab.

  3. Select **Manual scaling**.

  4. Enter the value `0` (zero) in the field labelled **Number of instances**.

  5. Click **View diff & deploy**, then **Deploy changes**.




###  gcloud 

To disable a service, use the following command to set scaling to zero:
    
    
    gcloud run services update SERVICE --scaling=0

Replace SERVICE with the name of your service.

### YAML

  1. Download your service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Set the `manualInstanceCount` attribute to zero (`0`):
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
           run.googleapis.com/scalingMode: manual
           run.googleapis.com/manualInstanceCount: `0`

Replace SERVICE with the name of your Cloud Run service.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml




###  REST API

To disable a service, send a `PATCH` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/patch).

For example, using `curl`:
    
    
        curl -H "Content-Type: application/json" \
        -H "Authorization: Bearer ACCESS_TOKEN" \
        -X PATCH \
        -d '{"scaling":{"manualInstanceCount":0 }}' \
        https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE?update_mask=scaling.manualInstanceCount

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to update a service](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into `gcloud`, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE: the name of the service.
  * REGION: the Google Cloud region that the service is deployed in.
  * PROJECT_ID: the Google Cloud project ID.



### Terraform

To disable a service, set the `manual_instance_count` attribute to zero (`0`):
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
      scaling {
        scaling_mode = "MANUAL"
        manual_instance_count = "0"
      }
    }
    

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`



## Delete existing services

The following considerations apply to deleting a service:

  * Deleting a service deletes all resources related to this service, including all revisions of this service whether they are serving traffic or not.
  * Deleting a service does not automatically remove container images from Artifact Registry. To delete container images used by the deleted revisions from Artifact Registry, refer to [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).
  * Deleting a service with one or more Eventarc triggers does not automatically delete these triggers. To delete the triggers refer to [Manage triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).
  * After deletion, the service remains visible in the Google Cloud console and in the command line interface until the deletion is fully complete. However, you cannot update the service.
  * Deleting a service is permanent: there is no undo or restore. However, if after deleting a service, you deploy a new service with the same name in the same region, it will have the same endpoint URL.
  * When you delete a Cloud Run function, it stops accepting new requests. However, Cloud Run doesn't immediately terminate any running instances. Instead, the function runs until task completion within your configured timeout. This might cause the function to appear active in logs for a short period after you delete it.



You can delete a service or a function using the Google Cloud console, the Google Cloud CLI, YAML file, or REST API:

### Console

To delete a service:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service you want to delete in the services list, and click its checkbox to select it.

  3. Click **Delete**. This deletes all revisions of the service.




###  gcloud 

To delete a service, use the command:
    
    
    gcloud run services delete SERVICE --region REGION

Replace

  * SERVICE with the name of your service.
  * REGION with the Google Cloud region of the service.



### Client libraries

To delete a service from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ServicesClient_DeleteService)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ServicesClient#com_google_cloud_run_v2_ServicesClient_deleteServiceAsync_com_google_cloud_run_v2_DeleteServiceRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.servicesclient#_google_cloud_run_v2_ServicesClient_deleteService_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.services.ServicesClient#google_cloud_run_v2_services_services_ServicesClient_delete_service)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Client#Google__Cloud__Run__V2__Services__Client_delete_service_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ServicesClient#_Google_Cloud_Run_V2_Client_ServicesClient__deleteService__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ServicesClient#Google_Cloud_Run_V2_ServicesClient_DeleteService_Google_Cloud_Run_V2_DeleteServiceRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To delete a service, send a `DELETE` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/delete).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X DELETE \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE-NAME

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to delete a service](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE-NAME with the name of the service.
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
