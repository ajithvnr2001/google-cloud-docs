---
url: https://docs.cloud.google.com/oracle/database/docs/create-instances/
title: Create Exadata Infrastructure instances \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:49.031615+00:00
---

# Create Exadata Infrastructure instances  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create Exadata Infrastructure instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an Exadata Infrastructure instance in Google Cloud.

In Oracle Database@Google Cloud, you can create an Exadata Infrastructure instance in Google Cloud using Google Cloud console or the Oracle Database@Google Cloud API. You need to create an instance before you can create a Exadata VM Cluster.

For a list of available regions where you can create an instance, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).

## Before you begin

  * [Set up gcloud CLI and enable the API](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Confirm you have an active marketplace order for Oracle Database@Google Cloud.

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * Confirm that you have the required roles necessary to create an instance: `cloudExadataInfrastructureAdmin`.

For more information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create an Exadata Infrastructure instance

You must create your Exadata Infrastructure in the same region and zone as your ODB Network. This ensures optimal performance and seamless communication.

To create an instance, do the following:

### Console

  1. Go to the **Exadata Database Service** page in the Google Cloud console.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. In the **Exadata Infrastructure** section, click **Create**.

  3. In the **Instance details** section, complete the following:

     1. Enter an **Infrastructure display name** to display in the Google Cloud console. The name must be unique within your Google Cloud project.

     2. Enter an **Infrastructure ID** to display in the Google Cloud project. This identifier is permanent.

     3. Select a **Region** and a **GCP Oracle zone**.

The region and zone choice is permanent and can't be changed later.

  4. In the **Machine configuration** section, complete the following:

**Note:** The availability of machine configurations might vary depending on the region and zone you selected.
     1. Select an **Exadata Infrastructure model** for your instance. The list shows infrastructure models available based on the region you selected.

     2. Select the values for the following configurations:

        * **Database server type** (applicable only to `X11M`)
        * **Storage server type** (applicable only to `X11M`)
        * **Database servers** (minimum 2, maximum 32)
        * **Storage servers** (minimum 3, maximum 64)
  5. In the **Maintenance** section, click **Change** to open the **Edit Maintenance** window and configure your instance's maintenance settings.

     1. Under **Maintenance method** , click one of the following:

        * **Rolling** : the system updates the servers one at a time with no downtime.

        * **Non-rolling** : the system shuts down and updates the servers in parallel. This method minimizes maintenance time, but incurs a full system shutdown.

If you want to perform custom actions outside of Oracle's purview before starting maintenance on your servers, select the checkbox for the **Enable custom action** setting.

     2. Under **Maintenance schedule** , select one of the following:

        * **No preference** : the system assigns a date and start time for your instance maintenance.

        * **Specify a schedule** : choose your preferred month, week, weekday, and start time for the instance's maintenance.

To learn more about how maintenance works for Exadata Infrastructure resources, see [Oracle-managed Exadata Cloud Infrastructure Maintenance](https://docs.oracle.com/en-us/iaas/exadatacloud/exacs/exa-conf-oracle-man-infra.html#ECSCM-GUID-C4301E26-E809-438F-96D7-9C6BB02FEA7F).

     3. Under **Maintenance contacts** , you can add up to 10 unique maintenance contacts. To add a contact, click **Add contact** , enter the email address of the contact, and then click **Add**.

Contacts must be added one at a time.

Once you have completed all maintenance fields, click **Save** to save the maintenance settings for your instance.

  6. Click **Create** to create the instance.




### gcloud

Use the `gcloud oracle-database cloud-exadata-infrastructures create` command to create an instance using gcloud CLI.
    
    
    gcloud oracle-database cloud-exadata-infrastructures create INSTANCE_ID
    --location=REGION_ID
    --display-name=DISPLAY_NAME
    --properties-shape="Exadata.X9M"
    --properties-compute-count=COMPUTE_COUNT
    --properties-storage-count=STORAGE_COUNT
    

Replace the following:

  * INSTANCE_ID: a permanent identifier for your instance. The instance ID can't be changed once set.
  * REGION_ID: the region for your instance. The region is permanent and can't be changed later. For a list of available regions, see [Available configurations](https://docs.cloud.google.com/oracle/database/docs/available-configurations).
  * DISPLAY_NAME: a name to identify your instance and is displayed Google Cloud console. The name must be unique within your Google Cloud project.
  * COMPUTE_COUNT: the compute capacity is the number of database servers for your instance and can range from 2 to 32.
  * STORAGE_COUNT: the storage capacity for your instance and can range from 3 to 64.



### C#
    
    
    using [Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedOracleDatabaseClientSnippets
    {
        /// <summary>Snippet for CreateCloudExadataInfrastructureAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task CreateCloudExadataInfrastructureAsync()
        {
            // Create client
            [OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html) oracleDatabaseClient = await [OracleDatabaseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html#Google_Cloud_OracleDatabase_V1_OracleDatabaseClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            string parent = "projects/[PROJECT]/locations/[LOCATION]";
            [CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure.html) cloudExadataInfrastructure = new [CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure.html)();
            string cloudExadataInfrastructureId = "";
            // Make the request
            Operation<CloudExadataInfrastructure, OperationMetadata> response = await oracleDatabaseClient.[CreateCloudExadataInfrastructureAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html#Google_Cloud_OracleDatabase_V1_OracleDatabaseClient_CreateCloudExadataInfrastructureAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_OracleDatabase_V1_CloudExadataInfrastructure_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, cloudExadataInfrastructure, cloudExadataInfrastructureId);
    
            // Poll until the returned long-running operation is complete
            Operation<CloudExadataInfrastructure, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
            // Retrieve the operation result
            [CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<CloudExadataInfrastructure, OperationMetadata> retrievedResponse = await oracleDatabaseClient.[PollOnceCreateCloudExadataInfrastructureAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OracleDatabaseClient.html#Google_Cloud_OracleDatabase_V1_OracleDatabaseClient_PollOnceCreateCloudExadataInfrastructureAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [CloudExadataInfrastructure](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CloudExadataInfrastructure.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateCloudExadataInfrastructureRequest.
    	}
    	op, err := c.CreateCloudExadataInfrastructure(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.oracledatabase.v1.[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure.html);
    import com.google.cloud.oracledatabase.v1.[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest.html);
    import com.google.cloud.oracledatabase.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.LocationName.html);
    import com.google.cloud.oracledatabase.v1.[OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    
    public class AsyncCreateCloudExadataInfrastructure {
    
      public static void main(String[] args) throws Exception {
        asyncCreateCloudExadataInfrastructure();
      }
    
      public static void asyncCreateCloudExadataInfrastructure() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html) oracleDatabaseClient = [OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html).create()) {
          [CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest.html) request =
              [CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[setCloudExadataInfrastructureId](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest.Builder.html#com_google_cloud_oracledatabase_v1_CreateCloudExadataInfrastructureRequest_Builder_setCloudExadataInfrastructureId_java_lang_String_)("cloudExadataInfrastructureId975345409")
                  .setCloudExadataInfrastructure([CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure.html).newBuilder().build())
                  .setRequestId("requestId693933066")
                  .build();
          ApiFuture<Operation> future =
              oracleDatabaseClient.[createCloudExadataInfrastructureCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.html#com_google_cloud_oracledatabase_v1_OracleDatabaseClient_createCloudExadataInfrastructureCallable__)().futureCall(request);
          // Do something.
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = future.get();
        }
      }
    }

### Node.js
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The parent value for CloudExadataInfrastructure in the following
     *  format: projects/{project}/locations/{location}.
     */
    // const parent = 'abc123'
    /**
     *  Required. The ID of the Exadata Infrastructure to create. This value is
     *  restricted to (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$) and must be a maximum of
     *  63 characters in length. The value must start with a letter and end with a
     *  letter or a number.
     */
    // const cloudExadataInfrastructureId = 'abc123'
    /**
     *  Required. Details of the Exadata Infrastructure instance to create.
     */
    // const cloudExadataInfrastructure = {}
    /**
     *  Optional. An optional ID to identify the request. This value is used to
     *  identify duplicate requests. If you make a request with the same request ID
     *  and the original request is still in progress or completed, the server
     *  ignores the second request. This prevents clients from
     *  accidentally creating duplicate commitments.
     *  The request ID must be a valid UUID with the exception that zero UUID is
     *  not supported (00000000-0000-0000-0000-000000000000).
     */
    // const requestId = 'abc123'
    
    // Imports the Oracledatabase library
    const {OracleDatabaseClient} = require('[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)').v1;
    
    // Instantiates a client
    const oracledatabaseClient = new [OracleDatabaseClient](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)();
    
    async function callCreateCloudExadataInfrastructure() {
      // Construct request
      const request = {
        parent,
        cloudExadataInfrastructureId,
        cloudExadataInfrastructure,
      };
    
      // Run request
      const [operation] = await oracledatabaseClient.createCloudExadataInfrastructure(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateCloudExadataInfrastructure();

### PHP
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\OperationResponse;
    use Google\Cloud\OracleDatabase\V1\Client\OracleDatabaseClient;
    use Google\Cloud\OracleDatabase\V1\CloudExadataInfrastructure;
    use Google\Cloud\OracleDatabase\V1\CreateCloudExadataInfrastructureRequest;
    use Google\Rpc\Status;
    
    /**
     * Creates a new Exadata Infrastructure in a given project and location.
     *
     * @param string $formattedParent              The parent value for CloudExadataInfrastructure in the following
     *                                             format: projects/{project}/locations/{location}. Please see
     *                                             {@see OracleDatabaseClient::locationName()} for help formatting this field.
     * @param string $cloudExadataInfrastructureId The ID of the Exadata Infrastructure to create. This value is
     *                                             restricted to (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$) and must be a maximum of
     *                                             63 characters in length. The value must start with a letter and end with a
     *                                             letter or a number.
     */
    function create_cloud_exadata_infrastructure_sample(
        string $formattedParent,
        string $cloudExadataInfrastructureId
    ): void {
        // Create a client.
        $oracleDatabaseClient = new OracleDatabaseClient();
    
        // Prepare the request message.
        $cloudExadataInfrastructure = new CloudExadataInfrastructure();
        $request = (new CreateCloudExadataInfrastructureRequest())
            ->setParent($formattedParent)
            ->setCloudExadataInfrastructureId($cloudExadataInfrastructureId)
            ->setCloudExadataInfrastructure($cloudExadataInfrastructure);
    
        // Call the API and handle any network failures.
        try {
            /** @var OperationResponse $response */
            $response = $oracleDatabaseClient->createCloudExadataInfrastructure($request);
            $response->pollUntilComplete();
    
            if ($response->operationSucceeded()) {
                /** @var CloudExadataInfrastructure $result */
                $result = $response->getResult();
                printf('Operation successful with response data: %s' . PHP_EOL, $result->serializeToJsonString());
            } else {
                /** @var Status $error */
                $error = $response->getError();
                printf('Operation failed with error data: %s' . PHP_EOL, $error->serializeToJsonString());
            }
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedParent = OracleDatabaseClient::locationName('[PROJECT]', '[LOCATION]');
        $cloudExadataInfrastructureId = '[CLOUD_EXADATA_INFRASTRUCTURE_ID]';
    
        create_cloud_exadata_infrastructure_sample($formattedParent, $cloudExadataInfrastructureId);
    }

### Python
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest)
    
    
    def sample_create_cloud_exadata_infrastructure():
        # Create a client
        client = [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest).[OracleDatabaseClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.OracleDatabaseClient.html)()
    
        # Initialize request argument(s)
        request = [oracledatabase_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest).[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.CreateCloudExadataInfrastructureRequest.html)(
            parent="parent_value",
            cloud_exadata_infrastructure_id="cloud_exadata_infrastructure_id_value",
        )
    
        # Make the request
        operation = client.[create_cloud_exadata_infrastructure](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.OracleDatabaseClient.html#google_cloud_oracledatabase_v1_services_oracle_database_OracleDatabaseClient_create_cloud_exadata_infrastructure)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby
    
    
    require "google/cloud/oracle_database/v1"
    
    ##
    # Snippet for the create_cloud_exadata_infrastructure call in the OracleDatabase service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::OracleDatabase::V1::OracleDatabase::Client#create_cloud_exadata_infrastructure.
    #
    def create_cloud_exadata_infrastructure
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::OracleDatabase::V1::OracleDatabase::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::OracleDatabase::V1::CreateCloudExadataInfrastructureRequest.new
    
      # Call the create_cloud_exadata_infrastructure method.
      result = client.create_cloud_exadata_infrastructure request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

After creating an Exadata Infrastructure instance, you can configure Exascale Storage on it. For more information, see [Create Exascale Storage](https://docs.cloud.google.com/oracle/database/docs/create-exadata-storage-vaults) and [Configure Exascale Storage](https://docs.cloud.google.com/oracle/database/docs/configure-exascale-storage).

## What's next

  * Learn how to [manage](https://docs.cloud.google.com/oracle/database/docs/manage-instances) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-instances) an instance.
  * [Create a Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters) for your Exadata Infrastructure instance.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
