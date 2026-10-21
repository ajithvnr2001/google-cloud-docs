---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-scc/
title: Send Sensitive Data Protection inspection job results to Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:27.073500+00:00
---

# Send Sensitive Data Protection inspection job results to Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-scc/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Send Sensitive Data Protection inspection job results to Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through inspecting data in Cloud Storage, Firestore in Datastore mode (Datastore), or BigQuery and sending the inspection results to Security Command Center.

To use this feature, your project must belong to an organization, and Security Command Center must be activated at the organization level. Otherwise, Sensitive Data Protection findings won't appear in Security Command Center. For more information, see [Check the activation level of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level).

For BigQuery data, you can additionally perform [profiling](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), which is different from an inspection operation. You can also send data profiles to Security Command Center. For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## Overview

Security Command Center enables you to gather data about, identify, and act on security threats before they can cause business damage or loss. With Security Command Center, you can perform several security-related actions from a single centralized dashboard.

Sensitive Data Protection has built-in integration with Security Command Center. When you use a Sensitive Data Protection [action](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) to inspect your Google Cloud storage repositories for sensitive data, it can send results directly to the Security Command Center dashboard. They display next to other security metrics.

By completing the steps in this guide, you do the following:

  * Enable Security Command Center and Sensitive Data Protection.
  * Set up Sensitive Data Protection to inspect a Google Cloud storage repository—either a Cloud Storage bucket, BigQuery table, or Datastore kind.
  * Configure a Sensitive Data Protection scan to send the inspection job results to Security Command Center.



For more information about Security Command Center, see the [Security Command Center documentation](https://docs.cloud.google.com/security-command-center/docs).

If you want to send the results of discovery scans—not inspection jobs—to Security Command Center, see the documentation for [profiling an organization, folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder), or [project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project) instead.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * Sensitive Data Protection
  * Cloud Storage
  * BigQuery
  * Datastore



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Before you can send Sensitive Data Protection scan results to Security Command Center, you must do each of the following:

  * Step 1: Set Google Cloud storage repositories.
  * Step 2: Set Identity and Access Management (IAM) roles.
  * Step 3: Enable Security Command Center.
  * Step 4: Enable Sensitive Data Protection.
  * Step 5: Enable Sensitive Data Protection as a security source for Security Command Center.



The steps to set up these components are described in the following sections.

### Step 1: Set Google Cloud storage repositories

Choose whether you want to scan your own Google Cloud storage repository or an example one. This topic provides instructions for both scenarios.

#### Scan your own data

If you want to scan your own existing Cloud Storage bucket, BigQuery table, or Datastore kind, first open the project that the repository is in. In subsequent steps, you'll enable both Security Command Center and Sensitive Data Protection for this project and its organization.

After you open the project you want to use, proceed to Step 2 to set up some IAM roles.

#### Scan sample data

If you want to scan a test set of data, first make sure that you have a billing account set up, and then create a new project. To complete this step, you must have the IAM **Project Creator** role. Learn more about [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  1. If you don't already have billing configured, set up a billing account. 

[Learn how to enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  2. Go to the **New Project** page in the Google Cloud console. 

[Go to New Project](https://console.cloud.google.com/projectcreate)

  3. On the **Billing account** drop-down list, select the billing account that the project should be billed to.
  4. On the **Organization** drop-down list, select the organization that you want to create the project in.
  5. On the **Location** drop-down list, select the organization or folder that you want to create the project in.



Next, download and store the sample data:

  1. Go to the [Cloud Run functions tutorials repository on GitHub](https://github.com/GoogleCloudPlatform/dlp-cloud-functions-tutorials/).
  2. Click **Clone or download** , and then click **Download ZIP**.
  3. Extract the zip file that you downloaded.
  4. Go to the [Storage Browser](https://console.cloud.google.com/storage/browser/) page in the Google Cloud console. 

[Go to Cloud Storage](https://console.cloud.google.com/storage/browser/)

  5. Click **Create bucket**.
  6. On the **Create a bucket** page, give the bucket a unique name, and then click **Create**.
  7. On the **Bucket details** page, click **Upload folder**.
  8. Go to the **`dlp-cloud-functions-tutorials-master`** folder that you extracted, open it, and then select the **`sample_data`** folder. Click **Upload** to upload the folder's contents to Cloud Storage.



Note the name that you gave the Cloud Storage bucket for later. After the file upload completes, you're ready to continue.

### Step 2: Set IAM roles

To use Sensitive Data Protection to send scan results to Security Command Center, you need the **Security Center Admin** and **Sensitive Data Protection Jobs Editor** IAM roles. This section describes how to add the roles. To complete this section, you must have the **Organization Administrator** IAM role.

  1. Go to the IAM page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. On the **View by principals** tab, find your Google Account and click _edit_**Edit principal**. 

**Note:** If you can't find your account, make sure that you're looking at an organization and not a project. To select the correct organization, use the project selector drop-down list.

If an alert message displays that "You do not have sufficient permissions to view this page," make sure that you have the **Organization Administrator** IAM role. For more information, see [IAM documentation](https://docs.cloud.google.com/iam/docs/overview).

  3. Add the **Security Center Admin** and **Sensitive Data Protection Jobs Editor** roles:

     1. In the **Edit access** panel, click **Add another role**.
     2. In the **Select a role** list, search for **Security Center Admin** , and select it.
     3. Click **Add another role**.
     4. In the **Select a role** list, search for **DLP Jobs Editor** , and select it.
     5. Click **Save**.



You now have Sensitive Data Protection Jobs Editor and Security Center Admin roles for your organization. These roles let you complete the tasks in the remainder of this topic.

### Step 3: Enable Security Command Center

  1. Go to the [Security Command Center](https://console.cloud.google.com/security/command-center/welcome) page in the Google Cloud console.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/welcome)

  2. On the **Organization** drop-down list, select the organization for which you want to enable Sensitive Data Protection, and then click **Select**.

  3. On the **Enable asset discovery** page that appears, select **All current and future projects** , and then click **Enable**. A message should display that Sensitive Data Protection is beginning asset discovery.




After asset discovery is complete, Sensitive Data Protection will display your supported Google Cloud assets. Asset discovery might take a few minutes, and you might need to refresh the page to display the assets.

For more information about enabling Security Command Center, see the [Security Command Center documentation](https://docs.cloud.google.com/security-command-center/docs).

### Step 4: Enable Sensitive Data Protection

Enable Sensitive Data Protection for the project you want to scan. The project must be within the same organization for which you've enabled Security Command Center. To enable Sensitive Data Protection using the Google Cloud console:

  1. In the Google Cloud console, go to the **Enable access to API** page. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  2. On the toolbar, select the project from Step 1 of this guide. The project must contain the Cloud Storage bucket, BigQuery table, or Datastore kind you want to scan.
  3. Click **Next**.
  4. Click **Enable**.



Sensitive Data Protection is now enabled for your project.

### Step 5: Enable Sensitive Data Protection as an integrated service for Security Command Center

To view Sensitive Data Protection scan findings in Security Command Center, enable **Sensitive Data Protection** as an integrated service. For more information, see [Add a Google Cloud integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-source) in the Security Command Center documentation.

Findings for Sensitive Data Protection are displayed on the **Findings** page in Security Command Center.

## Configure and run a Sensitive Data Protection inspection scan

In this section, you configure and run a Sensitive Data Protection inspection job.

**Note:** These instructions use [APIs Explorer](https://developers.google.com/apis-explorer) to send requests that contain JSON to Sensitive Data Protection. This tool is for learning, demonstration, and experimentation purposes only, and you should never use APIs Explorer for production work. You can use `gcloud`, `curl`, or `httplib2` to send these requests instead. You can also use one of the available Sensitive Data Protection [client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries) to access the API using Java, Python, Go, and more.

The _inspection job_ that you configure here instructs Sensitive Data Protection to scan either the sample data stored in Cloud Storage or your own data stored in Cloud Storage, Datastore, or BigQuery. The job configuration that you specify is also where you instruct Sensitive Data Protection to save its scan results to Security Command Center.

### Step 1: Note your project identifier

  1. Go to the Google Cloud console. 

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard/)

  2. Click **Select**.
  3. On the **Select from** drop-down list, select the organization for which you enabled Security Command Center.
  4. Under **ID** , copy the project ID for the project that contains the data you want to scan.
  5. Under **Name** , click the project to select it.



### Step 2: Open APIs Explorer and configure the job

  1. Go to APIs Explorer on the reference page for the `dlpJobs.create` method by clicking the following button: 

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create?apix=true)

  2. In the **parent** box, enter the following, where PROJECT_ID is the project ID you noted in Step 1: 
         
         projects/PROJECT_ID




Replace the contents of the **Request body** field with the following JSON for the kind of data you want to use: sample data in a Cloud Storage bucket, or your own data stored in Cloud Storage, Datastore, or BigQuery.

### Sample data

If you created a Cloud Storage bucket to store sample data, copy the following JSON and then paste it into the **Request body** field. Replace `BUCKET_NAME` with the name that you gave your Cloud Storage bucket:
    
    
    {
      "inspectJob":{
        "storageConfig":{
          "cloudStorageOptions":{
            "fileSet":{
              "url":"gs://BUCKET_NAME/**"
            }
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            },
            {
              "name":"PERSON_NAME"
            },
            {
              "name": "LOCATION"
            },
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "includeQuote":true,
          "minLikelihood":"UNLIKELY",
          "limits":{
            "maxFindingsPerRequest":100
          }
        },
        "actions":[
          {
            "publishSummaryToCscc":{
    
            }
          }
        ]
      }
    }
    

### Cloud Storage data

To scan your own Cloud Storage bucket, copy the following JSON and paste it into the **Request body** field.

Replace `PATH_NAME` with the path to the location that you want to scan. To scan recursively, end the path with two asterisks, for example, `gs://path_to_files/**`. To scan a specific directory and no deeper, end the path with one asterisk, for example, `gs://path_to_files/*`.
    
    
    {
      "inspectJob":{
        "storageConfig":{
          "cloudStorageOptions":{
            "fileSet":{
              "url":"gs://PATH_NAME"
            }
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            },
            {
              "name":"PERSON_NAME"
            },
            {
              "name": "LOCATION"
            },
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "includeQuote":true,
          "minLikelihood":"UNLIKELY",
          "limits":{
            "maxFindingsPerRequest":100
          }
        },
        "actions":[
          {
            "publishSummaryToCscc":{
    
            }
          }
        ]
      }
    }
    

To learn more about the available scan options, see [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

### Datastore data

To scan your own data kept in Datastore, copy the following JSON and paste it into the **Request body** field.

Replace `DATASTORE_KIND` with the name of the Datastore kind. You can also replace `NAMESPACE_ID` and `PROJECT_ID` with the namespace and project identifiers, repectively, or you can remove the `"partitionID"` completely if you want.
    
    
    {
      "inspectJob":{
        "storageConfig":{
          "datastoreOptions":{
            "kind":{
              "name":"DATASTORE_KIND"
            },
            "partitionId":{
              "namespaceId":"NAMESPACE_ID",
              "projectId":"PROJECT_ID"
            }
          }
        },
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            },
            {
              "name":"PERSON_NAME"
            },
            {
              "name": "LOCATION"
            },
            {
              "name":"PHONE_NUMBER"
            }
          ],
          "includeQuote":true,
          "minLikelihood":"UNLIKELY",
          "limits":{
            "maxFindingsPerRequest":100
          }
        },
        "actions":[
          {
            "publishSummaryToCscc":{
    
            }
          }
        ]
      }
    }
    

To learn more about the available scan options, see [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

### BigQuery data

To scan your own BigQuery table, copy the following JSON and paste it into the **Request body** field.

Replace `PROJECT_ID`, `BIGQUERY_DATASET_NAME`, and `BIGQUERY_TABLE_NAME` with the project ID and BigQuery dataset and table names, repectively.
    
    
    {
      "inspectJob":
      {
        "storageConfig":
        {
          "bigQueryOptions":
          {
            "tableReference":
            {
              "projectId": "PROJECT_ID",
              "datasetId": "BIGQUERY_DATASET_NAME",
              "tableId": "BIGQUERY_TABLE_NAME"
            }
          }
        },
        "inspectConfig":
        {
          "infoTypes":
          [
            {
              "name": "EMAIL_ADDRESS"
            },
            {
              "name": "PERSON_NAME"
            },
            {
              "name": "LOCATION"
            },
            {
              "name": "PHONE_NUMBER"
            }
          ],
          "includeQuote": true,
          "minLikelihood": "UNLIKELY",
          "limits":
          {
            "maxFindingsPerRequest": 100
          }
        },
        "actions":
        [
          {
            "publishSummaryToCscc":
            {
            }
          }
        ]
      }
    }
    

To learn more about the available scan options, see [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

**Note:** For a full list of information types that Sensitive Data Protection can scan for and detect, see [InfoTypes reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

### Step 3: Execute the request to start the inspection job

After you configure the job by following the preceding steps, click **Execute** to send the request. If the request is successful, a response appears below the request with a success code and a JSON object that indicates the status of the Sensitive Data Protection job that you created.

**Important:** Keep the page open or copy the response JSON so that you have it for the remainder of the tasks in this topic.

## Check the status of the Sensitive Data Protection inspection scan

The response to your scan request includes the job ID of your inspection scan job as the `"name"` key, and the current state of the inspection job as the `"state"` key. Immediately after you submit the request, the job's state is `"PENDING"`.

After you submit the scan request, the scan of your content begins immediately.

To check the status of the inspection job:

  1. Go to APIs Explorer on the reference page for the `dlpJobs.get` method by clicking the following button: 

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get?apix=true)

  2. In the **name** box, type the name of the job from the JSON response to the scan request in the following form: 
         
         projects/PROJECT_ID/dlpJobs/JOB_ID

The job ID is in the form of `i-1234567890123456789`.
  3. To submit the request, click **Execute**.



If the response JSON object's `"state"` key indicates that the job is `"DONE"`, then the inspection job has finished.

**Note:** You can instruct Sensitive Data Protection to send you a notification when a job is done. To learn more, see the [Actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) conceptual page.

To view the rest of the response JSON, scroll down the page. Under `"result"` > `"infoTypeStats"`, each information type listed should have a corresponding `"count"`. If not, make sure that you entered the JSON accurately, and that the path or location to your data is correct.

After the inspection job is done, you can continue to the next section of this guide to view scan results in Security Command Center.

## Code samples: inspect a Cloud Storage bucket

This example demonstrates how to use the DLP API to create an inspection job that inspects a Cloud Storage bucket and sends findings to Security Command Center.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectStorageWithSCCIntegration
    {
        public static DlpJob SendGcsData(
            string projectId,
            string gcsPath,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely),
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the GCS file to be inspected.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                {
                    FileSet = new CloudStorageOptions.Types.FileSet
                    {
                        Url = gcsPath
                    }
                }
            };
    
            // Specify the type of info to be inspected and construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "LOCATION" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" }
                    }
                },
                IncludeQuote = true,
                MinLikelihood = minLikelihood,
                Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                {
                    MaxFindingsPerRequest = 100
                }
            };
    
            // Construct the SCC action which will be performed after inspecting the storage.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PublishSummaryToCscc = new Action.Types.PublishSummaryToCscc()
                }
            };
    
            // Construct the inspect job config using storage config, inspect config and action.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Construct the request.
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectJob = inspectJob
            };
    
            // Call the API.
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) response = dlp.CreateDlpJob(request);
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectGCSFileSendToScc inspects sensitive data in a Google Cloud Storage (GCS) file
    // and sends the inspection results to Google Cloud Security Command Center (SCC) for further analysis.
    func inspectGCSFileSendToScc(w io.Writer, projectID, gcsPath string) error {
    	// projectID := "my-project-id"
    	// gcsPath := "gs://" + "your-bucket-name" + "path/to/file.txt"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the GCS file to be inspected.
    	cloudStorageOptions := &dlppb.CloudStorageOptions{
    		FileSet: &dlppb.CloudStorageOptions_FileSet{
    			Url: gcsPath,
    		},
    	}
    
    	// storageCfg represents the configuration for data inspection in various storage types.
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_CloudStorageOptions{
    			CloudStorageOptions: cloudStorageOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "PERSON_NAME"},
    		{Name: "LOCATION"},
    		{Name: "PHONE_NUMBER"},
    	}
    
    	// The minimum likelihood required before returning a match.
    	minLikelihood := dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY)
    
    	// The maximum number of findings to report (0 = server maximum).
    	findingLimits := &dlppb.InspectConfig_FindingLimits{
    		MaxFindingsPerItem: 100,
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:     infoTypes,
    		MinLikelihood: minLikelihood,
    		Limits:        findingLimits,
    		IncludeQuote:  true,
    	}
    
    	// Specify the action that is triggered when the job completes.
    	action := &dlppb.Action{
    		Action: &dlppb.Action_PublishSummaryToCscc_{
    			PublishSummaryToCscc: &dlppb.Action_PublishSummaryToCscc{},
    		},
    	}
    
    	// Configure the inspection job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Send the request.
    	resp, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "Job created successfully: %v", resp.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectGcsFileSendToScc {
    
      private static final int TIMEOUT_MINUTES = 15;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The name of the file in the Google Cloud Storage bucket.
        String gcsPath = "gs://" + "your-bucket-name" + "path/to/file.txt";
        createJobSendToScc(projectId, gcsPath);
      }
    
      // Creates a DLP Job to scan the sample data stored in a Cloud Storage and save its scan results
      // to Security Command Center.
      public static void createJobSendToScc(String projectId, String gcsPath)
          throws IOException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify the GCS file to be inspected.
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder()
                  .[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).FileSet.newBuilder().setUrl(gcsPath))
                  .build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder()
                  .[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions)
                  .build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("EMAIL_ADDRESS", "PERSON_NAME", "LOCATION", "PHONE_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // The minimum likelihood required before returning a match.
          // See: https://cloud.google.com/dlp/docs/likelihood
          [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).UNLIKELY;
    
          // The maximum number of findings to report (0 = server maximum)
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).[FindingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.html) findingLimits =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).FindingLimits.newBuilder().[setMaxFindingsPerItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.Builder.html#com_google_privacy_dlp_v2_InspectConfig_FindingLimits_Builder_setMaxFindingsPerItem_int_)(100).build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood(minLikelihood)
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setLimits_com_google_privacy_dlp_v2_InspectConfig_FindingLimits_)(findingLimits)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishSummaryToCscc.html) publishSummaryToCscc =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishSummaryToCscc.getDefaultInstance();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPublishSummaryToCscc_com_google_privacy_dlp_v2_Action_PublishSummaryToCscc_)(publishSummaryToCscc).build();
    
          // Configure the inspection job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .addActions(action)
                  .build();
    
          // Construct the job creation request to be sent by the client.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Send the job creation request and process the response.
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) response = dlpServiceClient.createDlpJob(createDlpJobRequest);
          // Get the current time.
          long startTime = System.currentTimeMillis();
    
          // Check if the job state is DONE.
          while (response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)() != [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html).JobState.DONE) {
            // Sleep for 30 second.
            Thread.sleep(30000);
    
            // Get the updated job status.
            response = dlpServiceClient.getDlpJob(response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
            // Check if the timeout duration has exceeded.
            long elapsedTime = System.currentTimeMillis() - startTime;
            if (TimeUnit.MILLISECONDS.toMinutes(elapsedTime) >= TIMEOUT_MINUTES) {
              System.out.printf("Job did not complete within %d minutes.%n", TIMEOUT_MINUTES);
              break;
            }
          }
          // Print the results.
          System.out.println("Job status: " + response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = response.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlpClient = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'your-project-id';
    
    // The name of the file in the bucket
    // const gcsPath = 'gcs-file-path';
    
    async function inspectGCSSendToScc() {
      // Specify the storage configuration object with GCS URL.
      const storageConfig = {
        cloudStorageOptions: {
          fileSet: {
            url: gcsPath,
          },
        },
      };
    
      // Construct the info types to look for in the GCS file.
      const infoTypes = [
        {name: 'EMAIL_ADDRESS'},
        {name: 'PERSON_NAME'},
        {name: 'LOCATION'},
        {name: 'PHONE_NUMBER'},
      ];
    
      // Construct the inspection configuration.
      const inspectConfig = {
        infoTypes,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        limits: {
          maxFindingsPerItem: 100,
        },
      };
    
      // Specify the action that is triggered when the job completes.
      const action = {
        publishSummaryToCscc: {},
      };
    
      // Configure the inspection job we want the service to perform.
      const jobConfig = {
        inspectConfig,
        storageConfig,
        actions: [action],
      };
    
      // Construct the job creation request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: jobConfig,
      };
    
      // Send the job creation request and process the response.
      const [jobsResponse] = await dlpClient.createDlpJob(request);
      const jobName = jobsResponse.name;
    
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlpClient.getDlpJob({name: jobName});
    
        // Check if the job has completed.
        if (job.state === 'DONE') {
          break;
        }
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
    
      // Print out the results.
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.length > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectGCSSendToScc();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishSummaryToCscc;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    
    /**
     * (GCS) Send Cloud DLP scan results to Security Command Center.
     * Using Cloud Data Loss Prevention to scan specific Google Cloud resources and send data to Security Command Center.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $gcsUri            GCS file to be inspected.
     */
    function inspect_gcs_send_to_scc(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $gcsUri = 'gs://GOOGLE_STORAGE_BUCKET_NAME/dlp_sample.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Construct the items to be inspected.
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet((new FileSet())
                ->setUrl($gcsUri));
    
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions(($cloudStorageOptions));
    
        // Specify the type of info the inspection will look for.
        $infoTypes = [
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('PERSON_NAME'),
            (new InfoType())->setName('LOCATION'),
            (new InfoType())->setName('PHONE_NUMBER')
        ];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood(likelihood::UNLIKELY)
            ->setLimits((new FindingLimits())
                ->setMaxFindingsPerRequest(100))
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Specify the action that is triggered when the job completes.
        $action = (new Action())
            ->setPublishSummaryToCscc(new PublishSummaryToCscc());
    
        // Construct inspect job config to run.
        $inspectJobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Send the job creation request and process the response.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJobConfig);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($job->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() == JobState::DONE) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    from typing import List
    
    import google.cloud.dlp
    
    
    def inspect_gcs_send_to_scc(
        project: str,
        bucket: str,
        info_types: List[str],
        max_findings: int = 100,
    ) -> None:
        """
        Uses the Data Loss Prevention API to inspect Google Cloud Storage
        data and send the results to Google Security Command Center.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bucket: The name of the GCS bucket containing the file, as a string.
            info_types: A list of strings representing infoTypes to inspect for.
                A full list of infoType categories can be fetched from the API.
            max_findings: The maximum number of findings to report; 0 = no maximum.
        """
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY,
            "limits": {"max_findings_per_request": max_findings},
            "include_quote": True,
        }
    
        # Construct a cloud_storage_options dictionary with the bucket's URL.
        url = f"gs://{bucket}"
        storage_config = {"cloud_storage_options": {"file_set": {"url": url}}}
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"publish_summary_to_cscc": {}}]
    
        # Construct the job definition.
        job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.create_dlp_job(
            request={
                "parent": parent,
                "inspect_job": job,
            }
        )
        print(f"Inspection Job started : {response.name}")
    
        job_name = response.name
    
        # Waiting for maximum 15 minutes for the job to get complete.
        no_of_attempts = 30
        while no_of_attempts > 0:
            # Get the DLP job status.
            job = dlp.get_dlp_job(request={"name": job_name})
            # Check if the job has completed.
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
                break
            elif job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).FAILED:
                print("Job Failed, Please check the configuration.")
                return
    
            # Sleep for a short duration before checking the job status again.
            time.sleep(30)
            no_of_attempts -= 1
    
        # Print out the results.
        print(f"Job name: {job.name}")
        result = job.inspect_details.result
        print("Processed Bytes: ", result.processed_bytes)
        if result.info_type_stats:
            for stats in result.info_type_stats:
                print(f"Info type: {stats.info_type.name}")
                print(f"Count: {stats.count}")
        else:
            print("No findings.")
    
    

## Code samples: inspect a BigQuery table

This example demonstrates how to use the DLP API to create an inspection job that inspects a BigQuery table and sends findings to Security Command Center.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectBigQueryWithSCCIntegration
    {
        public static DlpJob SendBigQueryData(
            string projectId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely),
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the storage config by providing the table to be inspected.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                BigQueryOptions = new [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.html)
                {
                    TableReference = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                    {
                        ProjectId = "bigquery-public-data",
                        DatasetId = "usa_names",
                        TableId = "usa_1910_current",
                    }
                }
            };
    
            // Construct the inspect config by specifying the type of info to be inspected.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" }
                    }
                },
                IncludeQuote = true,
                MinLikelihood = minLikelihood,
                Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                {
                    MaxFindingsPerRequest = 100
                }
            };
    
            // Construct the SCC action which will be performed after inspecting the source.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PublishSummaryToCscc = new Action.Types.PublishSummaryToCscc()
                }
            };
    
            // Construct the inspect job config using storage config, inspect config and action.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Construct the request.
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectJob = inspectJob
            };
    
            // Call the API.
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) response = dlp.CreateDlpJob(request);
    
            System.Console.WriteLine($"Job created successfully. Job name: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html#Google_Cloud_Dlp_V2_DlpJob_Name)}");
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectBigQuerySendToScc configures the inspection job that instructs Cloud DLP to scan data stored in BigQuery,
    // and also instructs Cloud DLP to save its scan results to Security Command Center.
    func inspectBigQuerySendToScc(w io.Writer, projectID, bigQueryDatasetId, bigQueryTableId string) error {
    	// projectID := "my-project-id"
    	// bigQueryDatasetId := "your-project-bigquery-dataset"
    	// bigQueryTableId := "your-project-bigquery_table"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the BigQuery table to be inspected.
    	tableReference := &dlppb.BigQueryTable{
    		ProjectId: projectID,
    		DatasetId: bigQueryDatasetId,
    		TableId:   bigQueryTableId,
    	}
    
    	bigQueryOptions := &dlppb.BigQueryOptions{
    		TableReference: tableReference,
    	}
    
    	// Specify the type of storage that you have configured.
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_BigQueryOptions{
    			BigQueryOptions: bigQueryOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "PERSON_NAME"},
    		{Name: "LOCATION"},
    		{Name: "PHONE_NUMBER"},
    	}
    
    	// The minimum likelihood required before returning a match.
    	minLikelihood := dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY)
    
    	// The maximum number of findings to report (0 = server maximum).
    	findingLimits := &dlppb.InspectConfig_FindingLimits{
    		MaxFindingsPerItem: 100,
    	}
    
    	// Specify how the content should be inspected.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:     infoTypes,
    		MinLikelihood: minLikelihood,
    		Limits:        findingLimits,
    		IncludeQuote:  true,
    	}
    
    	// Specify the action that is triggered when the job completes.
    	action := &dlppb.Action{
    		Action: &dlppb.Action_PublishSummaryToCscc_{
    			PublishSummaryToCscc: &dlppb.Action_PublishSummaryToCscc{},
    		},
    	}
    
    	// Configure the inspection job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Send the request.
    	resp, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result
    	fmt.Fprintf(w, "Job created successfully: %v", resp.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectBigQuerySendToScc {
    
      private static final int TIMEOUT_MINUTES = 15;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The BigQuery dataset id to be used and the reference table name to be inspected.
        String bigQueryDatasetId = "your-project-bigquery-dataset";
        String bigQueryTableId = "your-project-bigquery_table";
        inspectBigQuerySendToScc(projectId, bigQueryDatasetId, bigQueryTableId);
      }
    
      // Inspects a BigQuery Table to send data to Security Command Center.
      public static void inspectBigQuerySendToScc(
          String projectId, String bigQueryDatasetId, String bigQueryTableId) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify the BigQuery table to be inspected.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) tableReference =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setDatasetId(bigQueryDatasetId)
                  .setTableId(bigQueryTableId)
                  .build();
    
          [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html) bigQueryOptions =
              [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryOptions.html).newBuilder().setTableReference(tableReference).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setBigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setBigQueryOptions_com_google_privacy_dlp_v2_BigQueryOptions_)(bigQueryOptions).build();
    
          // Specify the type of info the inspection will look for.
          List<InfoType> infoTypes =
              Stream.of("EMAIL_ADDRESS", "PERSON_NAME", "LOCATION", "PHONE_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // The minimum likelihood required before returning a match.
          [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).UNLIKELY;
    
          // The maximum number of findings to report (0 = server maximum)
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).[FindingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.html) findingLimits =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).FindingLimits.newBuilder().[setMaxFindingsPerItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.Builder.html#com_google_privacy_dlp_v2_InspectConfig_FindingLimits_Builder_setMaxFindingsPerItem_int_)(100).build();
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood(minLikelihood)
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setLimits_com_google_privacy_dlp_v2_InspectConfig_FindingLimits_)(findingLimits)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishSummaryToCscc.html) publishSummaryToCscc =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishSummaryToCscc.getDefaultInstance();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPublishSummaryToCscc_com_google_privacy_dlp_v2_Action_PublishSummaryToCscc_)(publishSummaryToCscc).build();
    
          // Configure the inspection job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .addActions(action)
                  .build();
    
          // Construct the job creation request to be sent by the client.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Send the job creation request and process the response.
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) response = dlpServiceClient.createDlpJob(createDlpJobRequest);
    
          // Get the current time.
          long startTime = System.currentTimeMillis();
    
          // Check if the job state is DONE.
          while (response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)() != [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html).JobState.DONE) {
            // Sleep for 30 second.
            Thread.sleep(30000);
    
            // Get the updated job status.
            response = dlpServiceClient.getDlpJob(response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
            // Check if the timeout duration has exceeded.
            long elapsedTime = System.currentTimeMillis() - startTime;
            if (TimeUnit.MILLISECONDS.toMinutes(elapsedTime) >= TIMEOUT_MINUTES) {
              System.out.printf("Job did not complete within %d minutes.%n", TIMEOUT_MINUTES);
              break;
            }
          }
          // Print the results.
          System.out.println("Job status: " + response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = response.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    async function inspectBigQuerySendToScc() {
      // Specify the storage configuration object with big query table.
      const storageItem = {
        bigQueryOptions: {
          tableReference: {
            projectId: dataProjectId,
            datasetId: datasetId,
            tableId: tableId,
          },
        },
      };
    
      // Specify the type of info the inspection will look for.
      const infoTypes = [
        {name: 'EMAIL_ADDRESS'},
        {name: 'PERSON_NAME'},
        {name: 'LOCATION'},
        {name: 'PHONE_NUMBER'},
      ];
    
      // Construct inspect configuration.
      const inspectConfig = {
        infoTypes: infoTypes,
        includeQuote: true,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        limits: {
          maxFindingsPerItem: 100,
        },
      };
    
      // Specify the action that is triggered when the job completes.
      const action = {
        publishSummaryToCscc: {
          enable: true,
        },
      };
    
      // Configure the inspection job we want the service to perform.
      const inspectJobConfig = {
        inspectConfig: inspectConfig,
        storageConfig: storageItem,
        actions: [action],
      };
    
      // Construct the job creation request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: inspectJobConfig,
      };
    
      // Send the job creation request and process the response.
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
    
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlp.getDlpJob({name: jobName});
    
        // Check if the job has completed.
        if (job.state === 'DONE') {
          break;
        }
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
    
      // Print out the results.
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.length > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectBigQuerySendToScc();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishSummaryToCscc;
    use Google\Cloud\Dlp\V2\BigQueryOptions;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    
    /**
     * (BIGQUERY) Send Cloud DLP scan results to Security Command Center.
     * Using Cloud Data Loss Prevention to scan specific Google Cloud resources and send data to Security Command Center.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $projectId         The ID of the Project.
     * @param string $datasetId         The ID of the BigQuery Dataset.
     * @param string $tableId           The ID of the BigQuery Table to be inspected.
     */
    function inspect_bigquery_send_to_scc(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $projectId,
        string $datasetId,
        string $tableId
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Construct the items to be inspected.
        $bigqueryTable = (new BigQueryTable())
            ->setProjectId($projectId)
            ->setDatasetId($datasetId)
            ->setTableId($tableId);
        $bigQueryOptions = (new BigQueryOptions())
            ->setTableReference($bigqueryTable);
    
        $storageConfig = (new StorageConfig())
            ->setBigQueryOptions(($bigQueryOptions));
    
        // Specify the type of info the inspection will look for.
        $infoTypes = [
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('PERSON_NAME'),
            (new InfoType())->setName('LOCATION'),
            (new InfoType())->setName('PHONE_NUMBER')
        ];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood(likelihood::UNLIKELY)
            ->setLimits((new FindingLimits())
                ->setMaxFindingsPerRequest(100))
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Specify the action that is triggered when the job completes.
        $action = (new Action())
            ->setPublishSummaryToCscc(new PublishSummaryToCscc());
    
        // Configure the inspection job we want the service to perform.
        $inspectJobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Send the job creation request and process the response.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJobConfig);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($job->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() == JobState::DONE) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    from typing import List
    
    import google.cloud.dlp
    
    
    def inspect_bigquery_send_to_scc(
        project: str,
        info_types: List[str],
        max_findings: int = 100,
    ) -> None:
        """
        Uses the Data Loss Prevention API to inspect public bigquery dataset
        and send the results to Google Security Command Center.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            info_types: A list of strings representing infoTypes to inspect for.
                A full list of infoType categories can be fetched from the API.
            max_findings: The maximum number of findings to report; 0 = no maximum
        """
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY,
            "limits": {"max_findings_per_request": max_findings},
            "include_quote": True,
        }
    
        # Construct a Cloud Storage Options dictionary with the big query options.
        storage_config = {
            "big_query_options": {
                "table_reference": {
                    "project_id": "bigquery-public-data",
                    "dataset_id": "usa_names",
                    "table_id": "usa_1910_current",
                }
            }
        }
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"publish_summary_to_cscc": {}}]
    
        # Construct the job definition.
        job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.create_dlp_job(
            request={
                "parent": parent,
                "inspect_job": job,
            }
        )
        print(f"Inspection Job started : {response.name}")
    
        job_name = response.name
    
        # Waiting for a maximum of 15 minutes for the job to get complete.
        no_of_attempts = 30
        while no_of_attempts > 0:
            # Get the DLP job status.
            job = dlp.get_dlp_job(request={"name": job_name})
            # Check if the job has completed.
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
                break
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).FAILED:
                print("Job Failed, Please check the configuration.")
                return
    
            # Sleep for a short duration before checking the job status again.
            time.sleep(30)
            no_of_attempts -= 1
    
        # Print out the results.
        print(f"Job name: {job.name}")
        result = job.inspect_details.result
        if result.info_type_stats:
            for stats in result.info_type_stats:
                print(f"Info type: {stats.info_type.name}")
                print(f"Count: {stats.count}")
        else:
            print("No findings.")
    
    

## Code samples: inspect a Datastore kind

This example demonstrates how to use the DLP API to create an inspection job that inspects a Datastore kind and sends findings to Security Command Center.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectDataStoreJobWithSCCIntegration
    {
        public static DlpJob SendInspectDatastoreToSCC(
            string projectId,
            string kindName,
            string namespaceId,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely),
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the Datastore entity to be inspected and construct the storage
            // config. The NamespaceId is to be used for partition entity and the datastore kind defining
            // a data set.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                DatastoreOptions = new [DatastoreOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatastoreOptions.html)
                {
                    Kind = new [KindExpression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KindExpression.html) { Name = kindName },
                    PartitionId = new [PartitionId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PartitionId.html)
                    {
                        NamespaceId = namespaceId,
                        ProjectId = projectId
                    }
                }
            };
    
            // Specify the type of info to be inspected and construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "LOCATION" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" }
                    }
                },
                IncludeQuote = true,
                MinLikelihood = minLikelihood,
                Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                {
                    MaxFindingsPerRequest = 100
                }
            };
    
            // Construct the SCC action which will be performed after inspecting the datastore.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    PublishSummaryToCscc = new Action.Types.PublishSummaryToCscc()
                }
            };
    
            // Construct the inspect job config using storage config, inspect config and action.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Construct the request.
            var request = new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectJob = inspectJob
            };
    
            // Call the API.
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) response = dlp.CreateDlpJob(request);
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectDataStoreSendToScc inspects sensitive data in a Datastore
    // and sends the results to Google Cloud Security Command Center (SCC).
    func inspectDataStoreSendToScc(w io.Writer, projectID, datastoreNamespace, datastoreKind string) error {
    	// projectID := "my-project-id"
    	// datastoreNamespace := "your-datastore-namespace"
    	// datastoreKind := "your-datastore-kind"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the Datastore entity to be inspected.
    	partitionId := &dlppb.PartitionId{
    		ProjectId:   projectID,
    		NamespaceId: datastoreNamespace,
    	}
    
    	// kindExpr represents an expression specifying a kind or range of kinds for data inspection in DLP.
    	kindExpression := &dlppb.KindExpression{
    		Name: datastoreKind,
    	}
    
    	// Specify datastoreOptions so that It holds the configuration options for inspecting data in
    	// Google Cloud Datastore.
    	datastoreOptions := &dlppb.DatastoreOptions{
    		PartitionId: partitionId,
    		Kind:        kindExpression,
    	}
    
    	// Specify the storageConfig to represents the configuration settings for inspecting data
    	// in different storage types, such as BigQuery and Cloud Storage.
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_DatastoreOptions{
    			DatastoreOptions: datastoreOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "PERSON_NAME"},
    		{Name: "LOCATION"},
    		{Name: "PHONE_NUMBER"},
    	}
    
    	// The minimum likelihood required before returning a match.
    	minLikelihood := dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY)
    
    	// The maximum number of findings to report (0 = server maximum).
    	findingLimits := &dlppb.InspectConfig_FindingLimits{
    		MaxFindingsPerItem: 100,
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:     infoTypes,
    		MinLikelihood: minLikelihood,
    		Limits:        findingLimits,
    		IncludeQuote:  true,
    	}
    
    	// Specify the action that is triggered when the job completes.
    	action := &dlppb.Action{
    		Action: &dlppb.Action_PublishSummaryToCscc_{
    			PublishSummaryToCscc: &dlppb.Action_PublishSummaryToCscc{},
    		},
    	}
    
    	// Configure the inspection job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Create the request for the job configured above.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Send the request.
    	resp, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result
    	fmt.Fprintf(w, "Job created successfully: %v", resp.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectDatastoreSendToScc {
    
      private static final int TIMEOUT_MINUTES = 15;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The namespace specifier to be used for the partition entity.
        String datastoreNamespace = "your-datastore-namespace";
        // The datastore kind defining a data set.
        String datastoreKind = "your-datastore-kind";
        inspectDatastoreSendToScc(projectId, datastoreNamespace, datastoreKind);
      }
    
      // Creates a DLP Job to scan the sample data stored in a DataStore table and save its scan results
      // to Security Command Center.
      public static void inspectDatastoreSendToScc(
          String projectId, String datastoreNamespace, String datastoreKind)
          throws IOException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify the Datastore entity to be inspected.
          [PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html) partitionId =
              [PartitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.html).newBuilder()
                  .setProjectId(projectId)
                  .[setNamespaceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PartitionId.Builder.html#com_google_privacy_dlp_v2_PartitionId_Builder_setNamespaceId_java_lang_String_)(datastoreNamespace)
                  .build();
    
          [KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html) kindExpression = [KindExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KindExpression.html).newBuilder().setName(datastoreKind).build();
    
          [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html) datastoreOptions =
              [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DatastoreOptions.html).newBuilder().setKind(kindExpression).setPartitionId(partitionId).build();
    
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setDatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setDatastoreOptions_com_google_privacy_dlp_v2_DatastoreOptions_)(datastoreOptions).build();
    
          // Specify the type of info the inspection will look for.
          List<InfoType> infoTypes =
              Stream.of("EMAIL_ADDRESS", "PERSON_NAME", "LOCATION", "PHONE_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // The minimum likelihood required before returning a match.
          [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).UNLIKELY;
    
          // The maximum number of findings to report (0 = server maximum)
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).[FindingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.html) findingLimits =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).FindingLimits.newBuilder().[setMaxFindingsPerItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.Builder.html#com_google_privacy_dlp_v2_InspectConfig_FindingLimits_Builder_setMaxFindingsPerItem_int_)(100).build();
    
          // Specify how the content should be inspected.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood(minLikelihood)
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setLimits_com_google_privacy_dlp_v2_InspectConfig_FindingLimits_)(findingLimits)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishSummaryToCscc.html) publishSummaryToCscc =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishSummaryToCscc.getDefaultInstance();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPublishSummaryToCscc_com_google_privacy_dlp_v2_Action_PublishSummaryToCscc_)(publishSummaryToCscc).build();
    
          // Configure the inspection job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .addActions(action)
                  .build();
    
          // Construct the job creation request to be sent by the client.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Send the job creation request and process the response.
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) response = dlpServiceClient.createDlpJob(createDlpJobRequest);
          // Get the current time.
          long startTime = System.currentTimeMillis();
    
          // Check if the job state is DONE.
          while (response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)() != [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html).JobState.DONE) {
            // Sleep for 30 second.
            Thread.sleep(30000);
    
            // Get the updated job status.
            response = dlpServiceClient.getDlpJob(response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
            // Check if the timeout duration has exceeded.
            long elapsedTime = System.currentTimeMillis() - startTime;
            if (TimeUnit.MILLISECONDS.toMinutes(elapsedTime) >= TIMEOUT_MINUTES) {
              System.out.printf("Job did not complete within %d minutes.%n", TIMEOUT_MINUTES);
              break;
            }
          }
          // Print the results.
          System.out.println("Job status: " + response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = response.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // Datastore namespace
    // const datastoreNamespace = 'datastore-namespace';
    
    // Datastore kind
    // const datastoreKind = 'datastore-kind';
    
    async function inspectDatastoreSendToScc() {
      // Specify the storage configuration object with datastore.
      const storageConfig = {
        datastoreOptions: {
          kind: {
            name: datastoreKind,
          },
          partitionId: {
            projectId: projectId,
            namespaceId: datastoreNamespace,
          },
        },
      };
    
      // Construct the info types to look for in the datastore.
      const infoTypes = [
        {name: 'EMAIL_ADDRESS'},
        {name: 'PERSON_NAME'},
        {name: 'LOCATION'},
        {name: 'PHONE_NUMBER'},
      ];
    
      // Construct the inspection configuration.
      const inspectConfig = {
        infoTypes: infoTypes,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        limits: {
          maxFindingsPerItem: 100,
        },
        includeQuote: true,
      };
    
      // Specify the action that is triggered when the job completes
      const action = {
        publishSummaryToCscc: {enable: true},
      };
    
      // Configure the inspection job we want the service to perform.
      const inspectJobConfig = {
        inspectConfig: inspectConfig,
        storageConfig: storageConfig,
        actions: [action],
      };
    
      // Construct the job creation request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: inspectJobConfig,
      };
    
      // Send the job creation request and process the response.
      const [jobsResponse] = await dlp.createDlpJob(request);
      const jobName = jobsResponse.name;
    
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlp.getDlpJob({name: jobName});
    
        // Check if the job has completed.
        if (job.state === 'DONE') {
          break;
        }
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
    
      // Print out the results.
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.length > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectDatastoreSendToScc();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishSummaryToCscc;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DatastoreOptions;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\KindExpression;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\PartitionId;
    use Google\Cloud\Dlp\V2\StorageConfig;
    
    /**
     * (DATASTORE) Send Cloud DLP scan results to Security Command Center.
     * Using Cloud Data Loss Prevention to scan specific Google Cloud resources and send data to Security Command Center.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $kindName          Datastore kind name to be inspected.
     * @param string $namespaceId       Namespace Id to be inspected.
     */
    function inspect_datastore_send_to_scc(
        string $callingProjectId,
        string $kindName,
        string $namespaceId
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Construct the items to be inspected.
        $datastoreOptions = (new DatastoreOptions())
            ->setKind((new KindExpression())
                ->setName($kindName))
            ->setPartitionId((new PartitionId())
                ->setNamespaceId($namespaceId)
                ->setProjectId($callingProjectId));
    
        $storageConfig = (new StorageConfig())
            ->setDatastoreOptions(($datastoreOptions));
    
        // Specify the type of info the inspection will look for.
        $infoTypes = [
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('PERSON_NAME'),
            (new InfoType())->setName('LOCATION'),
            (new InfoType())->setName('PHONE_NUMBER')
        ];
    
        // Specify how the content should be inspected.
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood(likelihood::UNLIKELY)
            ->setLimits((new FindingLimits())
                ->setMaxFindingsPerRequest(100))
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true);
    
        // Specify the action that is triggered when the job completes.
        $action = (new Action())
            ->setPublishSummaryToCscc(new PublishSummaryToCscc());
    
        // Construct inspect job config to run.
        $inspectJobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Send the job creation request and process the response.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJobConfig);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($job->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() == JobState::DONE) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    from typing import List
    
    import google.cloud.dlp
    
    
    def inspect_datastore_send_to_scc(
        project: str,
        datastore_project: str,
        kind: str,
        info_types: List[str],
        namespace_id: str = None,
        max_findings: int = 100,
    ) -> None:
        """
        Uses the Data Loss Prevention API to inspect Datastore data and
        send the results to Google Security Command Center.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            datastore_project: The Google Cloud project id of the target Datastore.
            kind: The kind of the Datastore entity to inspect, e.g. 'Person'.
            info_types: A list of strings representing infoTypes to inspect for.
                A full list of infoType categories can be fetched from the API.
            namespace_id: The namespace of the Datastore document, if applicable.
            max_findings: The maximum number of findings to report; 0 = no maximum
    
        """
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY,
            "limits": {"max_findings_per_request": max_findings},
            "include_quote": True,
        }
    
        # Construct a cloud_storage_options dictionary with datastore options.
        storage_config = {
            "datastore_options": {
                "partition_id": {
                    "project_id": datastore_project,
                    "namespace_id": namespace_id,
                },
                "kind": {"name": kind},
            }
        }
    
        # Tell the API where to send a notification when the job is complete.
        actions = [{"publish_summary_to_cscc": {}}]
    
        # Construct the job definition.
        job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API
        response = dlp.create_dlp_job(
            request={
                "parent": parent,
                "inspect_job": job,
            }
        )
        print(f"Inspection Job started : {response.name}")
    
        job_name = response.name
    
        # Waiting for a maximum of 15 minutes for the job to get complete.
        no_of_attempts = 30
        while no_of_attempts > 0:
            # Get the DLP job status.
            job = dlp.get_dlp_job(request={"name": job_name})
            # Check if the job has completed.
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
                break
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).FAILED:
                print("Job Failed, Please check the configuration.")
                return
    
            # Sleep for a short duration before checking the job status again.
            time.sleep(30)
            no_of_attempts -= 1
    
        # Print out the results.
        print(f"Job name: {job.name}")
        result = job.inspect_details.result
        if result.info_type_stats:
            for stats in result.info_type_stats:
                print(f"Info type: {stats.info_type.name}")
                print(f"Count: {stats.count}")
        else:
            print("No findings.")
    
    

## View Sensitive Data Protection scan results in Security Command Center

Because you instructed Sensitive Data Protection to send its inspection job results to Security Command Center, you can now view the results of the inspection job in Security Command Center:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select the organization for which you enabled Security Command Center.
  3. In the **Query editor** field, enter the following to query for findings from Sensitive Data Protection.
         
         state="ACTIVE"
         AND NOT mute="MUTED"
         AND (parent_display_name="Sensitive Data Protection" OR parent_display_name="Cloud Data Loss Prevention")
         

For more information about the query editor, see [Edit a findings query in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).

If any findings were sent from Sensitive Data Protection, the findings appear in the findings list. The list includes all findings from Sensitive Data Protection, which can include findings from inspection jobs and discovery (data profiling) operations.




The instructions provided in this guide only turn on some of Sensitive Data Protection's built-in detectors. 

  * For more information about what else Sensitive Data Protection can detect, see the [ InfoTypes reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference). 
  * For information about configuring your own custom infoType detectors, see [ Creating custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes). 



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this topic:

### Delete the project

The easiest way to eliminate billing is to delete the project you created while following the instructions provided in this topic.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



If you delete your project using this method, the Sensitive Data Protection job and Cloud Storage bucket you created were also deleted. It's not necessary to follow the instructions in the following sections.

### Delete the Sensitive Data Protection job

If you scanned your own data, you need to delete only the inspection job that you created:

  1. Go to APIs Explorer on the reference page for the `dlpJobs.delete` method by clicking the following button: 

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/delete?apix=true)

  2. In the **name** box, type the name of the job from the JSON response to the scan request, which has the following form: 
         
         projects/PROJECT_ID/dlpJobs/JOB_ID

The job ID is in the form of `i-1234567890123456789`.



If you created additional inspection jobs or if you want to make sure you've deleted the job successfully, you can list all existing jobs:

  1. Go to APIs Explorer on the reference page for the `dlpJobs.list` method by clicking the following button: 

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list?apix=true)

  2. In the **parent** box, type the project identifier in the following form: 
         
         projects/PROJECT_ID

  3. Click **Execute**.



If there are no jobs listed in the response, you've deleted all jobs. If jobs are listed in the response, repeat the deletion procedure for those jobs.

### Delete the Cloud Storage bucket

If you created a new Cloud Storage bucket to hold sample data, delete the bucket:

  1. Open the [Cloud Storage browser](https://console.cloud.google.com/storage/browser). 

[Open Cloud Storage](https://console.cloud.google.com/storage/browser)

  2. In the Cloud Storage browser, select the checkbox next to the name of the bucket you created, and then click **Delete**.



## What's next

  * Learn more about the [`publishSummaryToCscc` action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#publishsummarytocscc) in Sensitive Data Protection.
  * Learn more about [scanning storage repositories for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) using Sensitive Data Protection.
  * Learn how to use [Security Command Center](https://docs.cloud.google.com/security-command-center/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
