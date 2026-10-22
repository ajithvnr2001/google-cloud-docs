---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-revoke-dataset-access/
title: Revoke access to a dataset \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:10.967061+00:00
---

# Revoke access to a dataset  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-revoke-dataset-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Revoke access to a dataset Stay organized with collections  Save and categorize content based on your preferences. 

Remove a user or group's permissions to access a BigQuery dataset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Control access to resources with IAM](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // revokeAccessToDataset creates a new ACL removing the dataset access to "example-analyst-group@google.com" entity
    // For more information on the types of ACLs available see:
    // https://cloud.google.com/storage/docs/access-control/lists
    func revokeAccessToDataset(w io.Writer, projectID, datasetID, entity string) error {
    	// TODO(developer): uncomment and update the following lines:
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// entity := "user@mydomain.com"
    
    	ctx := context.Background()
    
    	// Create BigQuery client.
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Get dataset handler
    	dataset := client.Dataset(datasetID)
    
    	// Get dataset metadata
    	meta, err := dataset.Metadata(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Create new access entry list by copying the existing and omiting the access entry entity value
    	var newAccessList []*bigquery.[AccessEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_AccessEntry)
    	for _, entry := range meta.Access {
    		if entry.Entity != entity {
    			newAccessList = append(newAccessList, entry)
    		}
    	}
    
    	// Only proceed with update if something in the access list was removed.
    	// Additionally, we use the ETag from the initial metadata to ensure no
    	// other changes were made to the access list in the interim.
    	if len(newAccessList) < len(meta.Access) {
    		update := bigquery.[DatasetMetadataToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DatasetMetadataToUpdate){
    			Access: newAccessList,
    		}
    		meta, err = dataset.Update(ctx, update, meta.ETag)
    		if err != nil {
    			return err
    		}
    	} else {
    		return fmt.Errorf("any access entry was revoked")
    	}
    
    	fmt.Fprintf(w, "Details for Access entries in dataset %v.\n", datasetID)
    
    	for _, access := range meta.Access {
    		fmt.Fprintln(w)
    		fmt.Fprintf(w, "Role: %s\n", access.Role)
    		fmt.Fprintf(w, "Entity: %v\n", access.Entity)
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html);
    import com.google.cloud.bigquery.[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Entity.html);
    import com.google.cloud.bigquery.[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.html).[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Group.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html);
    import com.google.cloud.bigquery.[DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html);
    import java.util.List;
    
    public class RevokeDatasetAccess {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        // Project and dataset from which to get the access policy.
        String projectId = "MY_PROJECT_ID";
        String datasetName = "MY_DATASET_NAME";
        // Group to remove from the ACL
        String entityEmail = "group-to-remove@example.com";
    
        revokeDatasetAccess(projectId, datasetName, entityEmail);
      }
    
      public static void revokeDatasetAccess(String projectId, String datasetName, String entityEmail) {
        try {
          // Initialize client that will be used to send requests. This client only needs
          // to be created once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          // Create datasetId with the projectId and the datasetName.
          [DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html) datasetId = [DatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetId.html).of(projectId, datasetName);
          [Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Dataset.html) dataset = bigquery.[getDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getDataset_com_google_cloud_bigquery_DatasetId_com_google_cloud_bigquery_BigQuery_DatasetOption____)(datasetId);
    
          // Create a new Entity with the corresponding type and email
          // "user-or-group-to-remove@example.com"
          // For more information on the types of Entities available see:
          // https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Entity
          // and
          // https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Entity.Type
          [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Entity.html) entity = new [Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl.Group.html)(entityEmail);
    
          // To revoke access to a dataset, remove elements from the Acl list.
          // Find more information about ACL and the Acl Class here:
          // https://cloud.google.com/storage/docs/access-control/lists
          // https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Acl
          // Remove the entity from the ACLs list.
          List<Acl> acls =
              dataset.[getAcl](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.DatasetInfo.html#com_google_cloud_bigquery_DatasetInfo_getAcl__)().stream().filter(acl -> !acl.getEntity().equals(entity)).toList();
    
          // Update the ACLs by setting the new list.
          bigquery.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_update_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(dataset.toBuilder().setAcl(acls).build());
          System.out.println("ACLs of \"" + datasetName + "\" updated successfully");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("ACLs were not updated \n" + e.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Update and un-comment below lines
     */
    
    // const datasetId = "my_project_id.my_dataset"
    
    // ID of the user or group from whom you are revoking access.
    // const entityId = "user-or-group-to-remove@example.com"
    
    const {BigQuery} = require('@google-cloud/bigquery');
    
    // Instantiate a client.
    const bigquery = new BigQuery();
    
    async function revokeDatasetAccess() {
      const [dataset] = await bigquery.dataset(datasetId).get();
    
      // To revoke access to a dataset, remove elements from the access list.
      //
      // See the BigQuery client library documentation for more details on access entries:
      // https://cloud.google.com/nodejs/docs/reference/bigquery/latest
    
      // Filter access entries to exclude entries matching the specified entity_id
      // and assign a new list back to the access list.
      dataset.metadata.access = dataset.metadata.access.filter(entry => {
        return !(
          entry.entity_id === entityId ||
          entry.userByEmail === entityId ||
          entry.groupByEmail === entityId
        );
      });
    
      // Update will only succeed if the dataset
      // has not been modified externally since retrieval.
      //
      // See the BigQuery client library documentation for more details on metadata updates:
      // https://cloud.google.com/bigquery/docs/updating-datasets
    
      // Update just the 'access entries' property of the dataset.
      await dataset.setMetadata(dataset.metadata);
    
      console.log(`Revoked access to '${entityId}' from '${datasetId}'.`);
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from google.api_core.exceptions import PreconditionFailed
    
    # TODO(developer): Update and uncomment the lines below.
    
    # ID of the dataset to revoke access to.
    # dataset_id = "my-project.my_dataset"
    
    # ID of the user or group from whom you are revoking access.
    # Alternatively, the JSON REST API representation of the entity,
    # such as a view's table reference.
    # entity_id = "user-or-group-to-remove@example.com"
    
    # Instantiate a client.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # Get a reference to the dataset.
    dataset = client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_dataset)(dataset_id)
    
    # To revoke access to a dataset, remove elements from the AccessEntry list.
    #
    # See the BigQuery client library documentation for more details on `access_entries`:
    # https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset#google_cloud_bigquery_dataset_Dataset_access_entries
    
    # Filter `access_entries` to exclude entries matching the specified entity_id
    # and assign a new list back to the AccessEntry list.
    dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries) = [
        entry for entry in dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)
        if entry.[entity_id](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html#google_cloud_bigquery_dataset_AccessEntry_entity_id) != entity_id
    ]
    
    # Update will only succeed if the dataset
    # has not been modified externally since retrieval.
    #
    # See the BigQuery client library documentation for more details on `update_dataset`:
    # https://cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_update_dataset
    try:
        # Update just the `access_entries` property of the dataset.
        dataset = client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_update_dataset)(
            dataset,
            ["access_entries"],
        )
    
        # Notify user that the API call was successful.
        full_dataset_id = f"{dataset.project}.{dataset.dataset_id}"
        print(f"Revoked dataset access for '{[entity_id](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html#google_cloud_bigquery_dataset_AccessEntry_entity_id)}' to ' dataset '{full_dataset_id}.'")
    except PreconditionFailed:  # A read-modify-write error.
        print(
            f"Dataset '{dataset.dataset_id}' was modified remotely before this update. "
            "Fetch the latest version and retry."
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
