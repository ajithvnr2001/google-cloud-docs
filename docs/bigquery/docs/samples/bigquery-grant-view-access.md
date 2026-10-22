---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-grant-view-access/
title: Grant view access \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:20.084879+00:00
---

# Grant view access  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-grant-view-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Grant view access Stay organized with collections  Save and categorize content based on your preferences. 

Authorize and grant access to a view.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // updateViewDelegated demonstrates the setup of an authorized view, which allows access to a view's results
    // without the caller having direct access to the underlying source data.
    func updateViewDelegated(projectID, srcDatasetID, viewDatasetID, viewID string) error {
    	// projectID := "my-project-id"
    	// srcDatasetID := "sourcedata"
    	// viewDatasetID := "views"
    	// viewID := "myview"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	srcDataset := client.Dataset(srcDatasetID)
    	viewDataset := client.Dataset(viewDatasetID)
    	view := viewDataset.Table(viewID)
    
    	// First, we'll add a group to the ACL for the dataset containing the view.  This will allow users within
    	// that group to query the view, but they must have direct access to any tables referenced by the view.
    	vMeta, err := viewDataset.Metadata(ctx)
    	if err != nil {
    		return err
    	}
    	vUpdateMeta := bigquery.[DatasetMetadataToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DatasetMetadataToUpdate){
    		Access: append(vMeta.Access, &bigquery.[AccessEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_AccessEntry){
    			Role:       bigquery.[ReaderRole](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_OwnerRole_ReaderRole_WriterRole),
    			EntityType: bigquery.[GroupEmailEntity](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DomainEntity_GroupEmailEntity_UserEmailEntity_SpecialGroupEntity_ViewEntity_IAMMemberEntity_RoutineEntity_DatasetEntity),
    			Entity:     "example-analyst-group@google.com",
    		}),
    	}
    	if _, err := viewDataset.Update(ctx, vUpdateMeta, vMeta.ETag); err != nil {
    		return err
    	}
    
    	// Now, we'll authorize a specific view against a source dataset, delegating access enforcement.
    	// Once this has been completed, members of the group previously added to the view dataset's ACL
    	// no longer require access to the source dataset to successfully query the view.
    	srcMeta, err := srcDataset.Metadata(ctx)
    	if err != nil {
    		return err
    	}
    	srcUpdateMeta := bigquery.[DatasetMetadataToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DatasetMetadataToUpdate){
    		Access: append(srcMeta.Access, &bigquery.[AccessEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_AccessEntry){
    			EntityType: bigquery.[ViewEntity](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DomainEntity_GroupEmailEntity_UserEmailEntity_SpecialGroupEntity_ViewEntity_IAMMemberEntity_RoutineEntity_DatasetEntity),
    			View:       view,
    		}),
    	}
    	if _, err := srcDataset.Update(ctx, srcUpdateMeta, srcMeta.ETag); err != nil {
    		return err
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html);
    import com.google.cloud.bigquery.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html);
    import java.util.ArrayList;
    import java.util.List;
    
    // Sample to grant view access on dataset
    public class GrantViewAccess {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String srcDatasetId = "MY_DATASET_ID";
        String viewDatasetId = "MY_VIEW_DATASET_ID";
        String viewId = "MY_VIEW_ID";
        grantViewAccess(srcDatasetId, viewDatasetId, viewId);
      }
    
      public static void grantViewAccess(String srcDatasetId, String viewDatasetId, String viewId) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html) srcDataset = bigquery.[getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getDataset_com_google_cloud_bigquery_DatasetId_com_google_cloud_bigquery_BigQuery_DatasetOption____)(srcDatasetId);
          [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html) viewDataset = bigquery.[getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getDataset_com_google_cloud_bigquery_DatasetId_com_google_cloud_bigquery_BigQuery_DatasetOption____)(viewDatasetId);
          [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html) view = viewDataset.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html#com_google_cloud_bigquery_Dataset_get_java_lang_String_com_google_cloud_bigquery_BigQuery_TableOption____)(viewId);
          // First, we'll add a group to the ACL for the dataset containing the view. This will allow
          // users within that group to query the view, but they must have direct access to any tables
          // referenced by the view.
          List<Acl> viewAcl = new ArrayList<>(viewDataset.[getAcl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html#com_google_cloud_bigquery_DatasetInfo_getAcl__)());
          viewAcl.add([Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).of(new [Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Group.html)("example-analyst-group@google.com"), [Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).Role.READER));
          viewDataset.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html#com_google_cloud_bigquery_Dataset_toBuilder__)().setAcl(viewAcl).build().update();
          // Now, we'll authorize a specific view against a source dataset, delegating access
          // enforcement. Once this has been completed, members of the group previously added to the
          // view dataset's ACL no longer require access to the source dataset to successfully query the
          // view
          List<Acl> srcAcl = new ArrayList<>(srcDataset.[getAcl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html#com_google_cloud_bigquery_DatasetInfo_getAcl__)());
          srcAcl.add([Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).of(new [Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).[View](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.View.html)(view.getTableId())));
          srcDataset.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html#com_google_cloud_bigquery_Dataset_toBuilder__)().setAcl(srcAcl).build().update();
          System.out.println("Grant view access successfully");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Grant view access was not success. \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # To use a view, the analyst requires ACLs to both the view and the source
    # table. Create an authorized view to allow an analyst to use a view
    # without direct access permissions to the source table.
    view_dataset_id = "my-project.my_view_dataset"
    # Make an API request to get the view dataset ACLs.
    view_dataset = client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_dataset)(view_dataset_id)
    
    analyst_group_email = "example-analyst-group@google.com"
    access_entries = view_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)
    [access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries).append(
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[AccessEntry](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html)("READER", "groupByEmail", analyst_group_email)
    )
    view_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries) = access_entries
    
    # Make an API request to update the ACLs property of the view dataset.
    view_dataset = client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_update_dataset)(view_dataset, ["access_entries"])
    print(f"Access to view: {view_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)}")
    
    # Group members of "data_analysts@example.com" now have access to the view,
    # but they require access to the source table to use it. To remove this
    # restriction, authorize the view to access the source dataset.
    source_dataset_id = "my-project.my_source_dataset"
    # Make an API request to set the source dataset ACLs.
    source_dataset = client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_dataset)(source_dataset_id)
    
    view_reference = {
        "projectId": "my-project",
        "datasetId": "my_view_dataset",
        "tableId": "my_authorized_view",
    }
    access_entries = source_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)
    [access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries).append([bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[AccessEntry](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html)(None, "view", view_reference))
    source_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries) = access_entries
    
    # Make an API request to update the ACLs property of the source dataset.
    source_dataset = client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_update_dataset)(source_dataset, ["access_entries"])
    print(f"Access to source: {source_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
