---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-aggregate/
title: Add to an aggregate cell \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:18.210396+00:00
---

# Add to an aggregate cell  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-aggregate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Add to an aggregate cell Stay organized with collections  Save and categorize content based on your preferences. 

Add an integer to an aggregate cell. This type of write makes an AddToCell API request.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write examples](https://docs.cloud.google.com/bigtable/docs/writing-data)



## Code sample

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeAggregate(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    	columnFamilyName := "view_count"
    	viewTimestamp, err := time.Parse(time.RFC3339, "2024-03-13T12:41:34Z")
    	if err != nil {
    		return err
    	}
    	hourlyBucket := viewTimestamp.Truncate(time.Hour)
    
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[AddIntToCell](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_AddIntToCell)(columnFamilyName, "views", bigtable.[Time](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Time)(hourlyBucket), 1)
    
    	rowKey := "page#index.html"
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote row: %s\n", rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.common.primitives.Longs;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.time.Instant;
    import java.time.temporal.ChronoUnit;
    
    public class WriteAggregate {
      private static final String COUNT_COLUMN_FAMILY_NAME = "view_count";
      private static final long MICROS_PER_MILLI = 1000;
    
      public static void writeAggregate(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "page-view-counter";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
    
          String rowKey = "page#index.html";
          Instant viewTimestamp = Instant.parse("2024-03-13T12:41:34.123Z");
    
          // Bucket the views for an hour into a single count, giving us an hourly view count for a
          // given page.
          Instant hourlyBucket = viewTimestamp.truncatedTo(ChronoUnit.HOURS);
          long hourlyBucketMicros = hourlyBucket.toEpochMilli() * MICROS_PER_MILLI;
    
          [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create(tableId, rowKey)
                  .addToCell(COUNT_COLUMN_FAMILY_NAME, "views", hourlyBucketMicros, 1);
    
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during WriteAggregate: \n" + e.toString());
        }
      }
    
      public static void mergeAggregate(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "page-view-counter";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
    
          String rowKey = "page#index.html";
          Instant viewTimestamp = Instant.parse("2024-03-13T12:41:34.123Z");
    
          // Bucket the views for an hour into a single count, giving us an hourly view count for a
          // given page.
          Instant hourlyBucket = viewTimestamp.truncatedTo(ChronoUnit.HOURS);
          long hourlyBucketMicros = hourlyBucket.toEpochMilli() * MICROS_PER_MILLI;
    
          [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create(tableId, rowKey)
                  .mergeToCell(
                      COUNT_COLUMN_FAMILY_NAME,
                      "views",
                      hourlyBucketMicros,
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(Longs.toByteArray(1L)));
    
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during mergeAggregate: \n" + e.toString());
        }
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
