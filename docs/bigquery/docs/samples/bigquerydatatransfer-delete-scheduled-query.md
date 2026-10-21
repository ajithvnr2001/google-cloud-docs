---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-delete-scheduled-query/
title: Delete a scheduled query \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:12.305886+00:00
---

# Delete a scheduled query  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-delete-scheduled-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Delete a scheduled query Stay organized with collections  Save and categorize content based on your preferences. 

Delete the configuration for a scheduled query, stopping any future runs.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	datatransfer "cloud.google.com/go/bigquery/datatransfer/apiv1"
    	"cloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb"
    )
    
    // deleteScheduledQuery delete a scheduled query based on
    // the config ID, stopping any future runs.
    // transferConfigID follows the format:
    //
    //	`projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`
    //	or `projects/{project_id}/transferConfigs/{config_id}`
    func deleteScheduledQuery(transferConfigID string) error {
    	// transferConfigID := "projects/{project_id}/transferConfigs/{config_id}"
    	ctx := context.Background()
    	dtc, err := datatransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/datatransfer/apiv1.html#cloud_google_com_go_bigquery_datatransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("datatransfer.NewClient: %w", err)
    	}
    	defer dtc.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/datatransfer/apiv1.html#cloud_google_com_go_bigquery_datatransfer_apiv1_Client_Close)()
    
    	req := &datatransferpb.DeleteTransferConfigRequest{
    		Name: transferConfigID,
    	}
    	err = dtc.DeleteTransferConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("dtc.DeleteTransferConfig: %w", err)
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DeleteTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DeleteTransferConfigRequest.html);
    import java.io.IOException;
    
    // Sample to delete a scheduled query
    public class DeleteScheduledQuery {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // i.e projects/{project_id}/transferConfigs/{config_id}` or
        // `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`
        String name = "MY_CONFIG_ID";
        deleteScheduledQuery(name);
      }
    
      public static void deleteScheduledQuery(String name) throws IOException {
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) dataTransferServiceClient = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          [DeleteTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DeleteTransferConfigRequest.html) request =
              [DeleteTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DeleteTransferConfigRequest.html).newBuilder().setName(name).build();
          dataTransferServiceClient.deleteTransferConfig(request);
          System.out.print("Scheduled query deleted successfully.\n");
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
          System.out.print("Scheduled query was not deleted." + ex.toString());
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
