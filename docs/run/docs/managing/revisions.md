---
url: https://docs.cloud.google.com/run/docs/managing/revisions/
title: Manage revisions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:52.311497+00:00
---

# Manage revisions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage revisions Stay organized with collections  Save and categorize content based on your preferences. 

When you deploy to a service or change the configuration of a service, an immutable revision is created.

The following considerations apply to revisions:

  * You can specify whether a new revision receives all, none, or some of the traffic, you can gradually roll out a new revision, you can split traffic between several revisions, and you can roll back from a revision. For more information, refer to [Rollbacks, gradual rollouts, and traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).
  * You can optionally use [revision tags](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags) to test a revision that is not serving traffic.
  * You don't need to manually delete revisions, although you can if you want.
  * Revisions that are not receiving requests don't consume any resources and are not billed. However, if your revision has minimum instances configured, there are [billing considerations](https://docs.cloud.google.com/run/docs/configuring/min-instances#billing) to keep in mind.
  * There is a maximum of 1000 revisions per service: If you exceed that limit, older revisions are automatically deleted.
  * The revision suffix is assigned automatically. If you want to use your own version suffix, you can do so using the gcloud CLI parameter [`--revision-suffix`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--revision-suffix).



## Required roles

To get the permissions that you need to manage Cloud Run services and revisions, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run service. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View the list of revisions for a service

### Console

To view the list of revisions in your project:

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service in the services list, and click it.

  3. Click the **Revision history** tab to show the list of current revisions for that service.




###  gcloud 

To view the list of revisions for a given service:

  1. Find your service name from the list of services available in your project:
         
         gcloud run services list

  2. Use the following command to get all the revisions for the service you just looked up:
         
         gcloud run revisions list --service SERVICE --region REGION

Replace

     * SERVICE with the name of your service.
     * REGION with the Google Cloud region of the service.



### Cloud Code

To view the list of revisions with [Cloud Code](https://docs.cloud.google.com/code/docs), read the Cloud Run Explorer guides for [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/cloud-run-explorer) and [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/cloud-run-explorer).

### Client libraries

To view the list of revisions from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_RevisionsClient_ListRevisions)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.RevisionsClient#com_google_cloud_run_v2_RevisionsClient_listRevisions_com_google_cloud_run_v2_ListRevisionsRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.revisionsclient#_google_cloud_run_v2_RevisionsClient_listRevisions_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.revisions.RevisionsClient#google_cloud_run_v2_services_revisions_RevisionsClient_list_revisions)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Revisions-Client#Google__Cloud__Run__V2__Revisions__Client_list_revisions_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.RevisionsClient#_Google_Cloud_Run_V2_Client_RevisionsClient__listRevisions__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.RevisionsClient#Google_Cloud_Run_V2_RevisionsClient_ListRevisions_Google_Cloud_Run_V2_ListRevisionsRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view the list of revisions, send a `GET` HTTP request to the Cloud Run Admin API [`revisions` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services.revisions/list).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE-NAME/revisions

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to view revisions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE-NAME with the name of the service.
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



## View revision details

### Console

To view the details for a revision in your project:

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select your service in the services list.

  3. Click the **Revision history** tab to show the list of current revisions for that service.

  4. Select the service revision you are interested in.

  5. Examine the details panel at the far right for revision-specific information such as the URL of the deployed container image, amount of memory allocated, environment variables, and possibly build and source repository information.




###  gcloud 

To view the details for a revision in your project:

  1. Find your service name from the list of services available in your project:
         
         gcloud run services list

  2. Use the following command to get all the revisions for the service you just looked up: 
         
         gcloud run revisions list --service SERVICE --region REGION

Replace

     * SERVICE with the name of your service.
     * REGION with the Google Cloud region of the service.
  3. Use the following command to see more details about a specific revision: 
         
         gcloud run revisions describe REVISION --region REGION

Replace 
     * REVISION with the name of the revision you want to learn more about.
     * REGION with the Google Cloud region of the service.

You can use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to format the output. For example as YAML: 
    
    gcloud run revisions describe REVISION --region REGION --format yaml




### Cloud Code

To view the details of a revision with [Cloud Code](https://docs.cloud.google.com/code/docs), read the Cloud Run Explorer guides for [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/cloud-run-explorer) and [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/cloud-run-explorer).

### Client libraries

To view the details of a revision from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_RevisionsClient_GetRevision)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.RevisionsClient#com_google_cloud_run_v2_RevisionsClient_getRevision_com_google_cloud_run_v2_GetRevisionRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.revisionsclient#_google_cloud_run_v2_RevisionsClient_getRevision_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.revisions.RevisionsClient#google_cloud_run_v2_services_revisions_RevisionsClient_get_revision)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Revisions-Client#Google__Cloud__Run__V2__Revisions__Client_get_revision_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.RevisionsClient#_Google_Cloud_Run_V2_Client_RevisionsClient__getRevision__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.RevisionsClient#Google_Cloud_Run_V2_RevisionsClient_GetRevision_Google_Cloud_Run_V2_GetRevisionRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view details about a revision, send a `GET` HTTP request to the Cloud Run Admin API [`revisions` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services.revisions/get).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X GET \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE-NAME/revisions/REVISION-NAME

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to view service details](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE-NAME with the name of the service.
  * REVISION-NAME with the name of the revision.
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



Note that a non-current revision may have the status of `RETIRED`, which means that Cloud Run has retired the infrastructure needed for that particular revision.

### About build and source repository information in the _Details_ panel

If the [Artifact Analysis API](https://docs.cloud.google.com/container-registry/docs/container-analysis) is enabled and the container was built with [Cloud Build](https://cloud.google.com/build), build information is displayed in the _Details_ panel.

Additionally, if a [Cloud Build trigger](https://docs.cloud.google.com/build/docs/running-builds/create-manage-triggers) was used to build the container, source repository information is also displayed in the _Details_ panel.

## Delete revisions

A common use case for deleting a revision is when you want to make sure a particular revision won't be accidentally used.

You cannot delete a revision if:

  * it is able to receive traffic,
  * it is the only revision of the service,
  * it is the latest revision of the service.



When you delete a revision, the container image used by this revision is not deleted automatically from Container Registry or Artifact Registry. To delete a container image from a registry, see the deletion instructions for [Container Registry](https://docs.cloud.google.com/container-registry/docs/managing#deleting_images) or [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

You cannot undo a revision deletion.

You can use either the console or the command line:

### Console

To delete a revision:

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service in the services list, and click it.

  3. Click the **Revision history** tab to show the list of current revisions for that service.

  4. Locate the service revision you want to delete.

  5. Click the three-dot vertical ellipse to the left of the revision, then click **Delete** to delete the revision.




###  gcloud 

To delete a revision, use the following command:
    
    
    gcloud run revisions delete REVISION --region REGION

Replace

  * REVISION with the name of the revision you want to delete.
  * REGION with the Google Cloud region of the service.



### Client libraries

To delete a revision from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_RevisionsClient_DeleteOperation)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.RevisionsClient#com_google_cloud_run_v2_RevisionsClient_deleteRevisionAsync_com_google_cloud_run_v2_DeleteRevisionRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.revisionsclient#_google_cloud_run_v2_RevisionsClient_deleteRevision_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.revisions.RevisionsClient#google_cloud_run_v2_services_revisions_RevisionsClient_delete_revision)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Revisions-Client#Google__Cloud__Run__V2__Revisions__Client_delete_revision_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.RevisionsClient#_Google_Cloud_Run_V2_Client_RevisionsClient__deleteRevision__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.RevisionsClient#Google_Cloud_Run_V2_RevisionsClient_DeleteRevision_Google_Cloud_Run_V2_DeleteRevisionRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To delete a revision, send a `DELETE` HTTP request to the Cloud Run Admin API [`revisions` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services.revisions/delete).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X DELETE \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE-NAME/revisions/REVISION-NAME

Replace:

  * ACCESS_TOKEN with a valid access token for an account that has the [IAM permissions to delete a service](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE-NAME with the name of the service.
  * REVISION-NAME with the name of the revision.
  * REGION with the Google Cloud region of the service.
  * PROJECT-ID with the Google Cloud project ID.



## What's next

After you deploy a revision, you can do the following:

  * [Gradual rollouts, rollback revisions, traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
