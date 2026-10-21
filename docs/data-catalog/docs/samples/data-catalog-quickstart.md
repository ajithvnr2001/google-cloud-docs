---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-quickstart/
title: Quickstart: Attach tag to BigQuery table \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:32.579104+00:00
---

# Quickstart: Attach tag to BigQuery table  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-quickstart/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Quickstart: Attach tag to BigQuery table Stay organized with collections  Save and categorize content based on your preferences. 

Create a tag template and attach a tag to a BigQuery table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Tag a BigQuery table using Data Catalog](https://docs.cloud.google.com/data-catalog/docs/tag-bigquery-dataset)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Go API reference documentation](https://godoc.org/cloud.google.com/go/datacatalog). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // The datacatalog_quickstart application demonstrates how to define a tag
    // template, populate values in the template, and attach a tag based on the
    // template to a BigQuery table.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"strings"
    	"time"
    
    	datacatalog "cloud.google.com/go/datacatalog/apiv1"
    	"cloud.google.com/go/datacatalog/apiv1/datacatalogpb"
    	"github.com/googleapis/gax-go/v2"
    )
    
    func main() {
    	projectID := flag.String("project_id", "", "Cloud Project ID, used for session creation.")
    	location := flag.String("location", "us-central1", "data catalog region to use for the quickstart")
    	table := flag.String("table", "myproject.mydataset.mytable", "bigquery table to tag in project.dataset.table format")
    
    	flag.Parse()
    
    	ctx := context.Background()
    	client, err := datacatalog.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1.html#cloud_google_com_go_datacatalog_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("datacatalog.NewClient: %v", err)
    	}
    	defer client.Close()
    
    	// Create the tag template.
    	tmpl, err := createQuickstartTagTemplate(ctx, client, *projectID, *location)
    	if err != nil {
    		log.Fatalf("createQuickstartTagTemplate: %v", err)
    	}
    	fmt.Printf("Created tag template: %s\n", tmpl.GetName())
    
    	// Convert a BigQuery resource identifier into the equivalent datacatalog
    	// format.
    	resource, err := convertBigQueryResourceRepresentation(*table)
    	if err != nil {
    		log.Fatalf("couldn't parse --table flag (%s): %v", *table, err)
    	}
    
    	// Lookup the entry metadata for the BQ table resource.
    	entry, err := LookupEntry(ctx, client, &datacatalogpb.LookupEntryRequest{
    		TargetName: &datacatalogpb.LookupEntryRequest_LinkedResource{
    			LinkedResource: resource,
    		},
    	})
    	if err != nil {
    		log.Fatalf("LookupEntry: %v", err)
    	}
    	fmt.Printf("Successfully looked up table entry: %s\n", entry.GetName())
    
    	// Create a tag based on the template, and apply it to the entry.
    	tag, err := createQuickstartTag(ctx, client, "my-quickstart-tag", tmpl.GetName(), entry.GetName())
    	if err != nil {
    		log.Fatalf("couldn't create tag: %v", err)
    	}
    	fmt.Printf("Created tag: %s", tag.GetName())
    }
    
    // createQuickstartTagTemplate registers a tag template in datacatalog.
    func createQuickstartTagTemplate(ctx context.Context, client *datacatalog.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1.html#cloud_google_com_go_datacatalog_apiv1_Client), projectID, location string) (*datacatalogpb.TagTemplate, error) {
    	loc := fmt.Sprintf("projects/%s/locations/%s", projectID, location)
    
    	// Define the tag template.
    	template := &datacatalogpb.TagTemplate{
    		DisplayName: "Quickstart Tag Template",
    		Fields: map[string]*datacatalogpb.TagTemplateField{
    			"source": {
    				DisplayName: "Source of data asset",
    				Type: &datacatalogpb.FieldType{
    					TypeDecl: &datacatalogpb.FieldType_PrimitiveType_{
    						PrimitiveType: datacatalogpb.[FieldType_STRING](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1/datacatalogpb.html#cloud_google_com_go_datacatalog_apiv1_datacatalogpb_FieldType_PRIMITIVE_TYPE_UNSPECIFIED_FieldType_DOUBLE_FieldType_STRING_FieldType_BOOL_FieldType_TIMESTAMP_FieldType_RICHTEXT),
    					},
    				},
    			},
    			"num_rows": {
    				DisplayName: "Number of rows in data asset",
    				Type: &datacatalogpb.FieldType{
    					TypeDecl: &datacatalogpb.FieldType_PrimitiveType_{
    						PrimitiveType: datacatalogpb.[FieldType_DOUBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1/datacatalogpb.html#cloud_google_com_go_datacatalog_apiv1_datacatalogpb_FieldType_PRIMITIVE_TYPE_UNSPECIFIED_FieldType_DOUBLE_FieldType_STRING_FieldType_BOOL_FieldType_TIMESTAMP_FieldType_RICHTEXT),
    					},
    				},
    			},
    			"has_pii": {
    				DisplayName: "Has PII",
    				Type: &datacatalogpb.FieldType{
    					TypeDecl: &datacatalogpb.FieldType_PrimitiveType_{
    						PrimitiveType: datacatalogpb.[FieldType_BOOL](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1/datacatalogpb.html#cloud_google_com_go_datacatalog_apiv1_datacatalogpb_FieldType_PRIMITIVE_TYPE_UNSPECIFIED_FieldType_DOUBLE_FieldType_STRING_FieldType_BOOL_FieldType_TIMESTAMP_FieldType_RICHTEXT),
    					},
    				},
    			},
    			"pii_type": {
    				DisplayName: "PII Type",
    				Type: &datacatalogpb.FieldType{
    					TypeDecl: &datacatalogpb.FieldType_EnumType_{
    						EnumType: &datacatalogpb.FieldType_EnumType{
    							AllowedValues: []*datacatalogpb.FieldType_EnumType_EnumValue{
    								{DisplayName: "EMAIL"},
    								{DisplayName: "SOCIAL SECURITY NUMBER"},
    								{DisplayName: "NONE"},
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    
    	//Construct the creation request using the template definition.
    	req := &datacatalogpb.CreateTagTemplateRequest{
    		Parent:        loc,
    		TagTemplateId: "quickstart_tag_template",
    		TagTemplate:   template,
    	}
    
    	return client.CreateTagTemplate(ctx, req)
    
    }
    
    // createQuickstartTag populates tag values according to the template, and attaches
    // the tag to the designeated entry.
    func createQuickstartTag(ctx context.Context, client *datacatalog.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1.html#cloud_google_com_go_datacatalog_apiv1_Client), tagID, templateName, entryName string) (*datacatalogpb.Tag, error) {
    	tag := &datacatalogpb.Tag{
    		Name:     fmt.Sprintf("%s/tags/%s", entryName, tagID),
    		Template: templateName,
    		Fields: map[string]*datacatalogpb.TagField{
    			"source": {
    				Kind: &datacatalogpb.TagField_StringValue{StringValue: "Copied from tlc_yellow_trips_2018"},
    			},
    			"num_rows": {
    				Kind: &datacatalogpb.TagField_DoubleValue{DoubleValue: 113496874},
    			},
    			"has_pii": {
    				Kind: &datacatalogpb.TagField_BoolValue{BoolValue: false},
    			},
    			"pii_type": {
    				Kind: &datacatalogpb.TagField_EnumValue_{
    					EnumValue: &datacatalogpb.TagField_EnumValue{
    						DisplayName: "NONE",
    					},
    				},
    			},
    		},
    	}
    
    	req := &datacatalogpb.CreateTagRequest{
    		Parent: entryName,
    		Tag:    tag,
    	}
    	return client.CreateTag(ctx, req)
    }
    
    // convertBigQueryResourceRepresentation converts a table identifier in standard sql form
    // (project.datadata.table) into the representation used within data catalog.
    func convertBigQueryResourceRepresentation(table string) (string, error) {
    	parts := strings.Split(table, ".")
    	if len(parts) != 3 {
    		return "", fmt.Errorf("specified table string is not in expected project.dataset.table format: %s", table)
    	}
    	return fmt.Sprintf("//bigquery.googleapis.com/projects/%s/datasets/%s/tables/%s", parts[0], parts[1], parts[2]), nil
    }
    
    // LookupEntry provides a simple retry wrapper around the LookupEntry RPC.
    //
    // There's a potential propagation delay from when an entity is created until it appears in data catalog,
    // so we wrap the lookup in a retry with a short context deadline to avoid unnecessary waiting for datacatalog
    // to pick up new resources.
    func LookupEntry(ctx context.Context, client *datacatalog.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1.html#cloud_google_com_go_datacatalog_apiv1_Client), req *datacatalogpb.LookupEntryRequest) (*datacatalogpb.Entry, error) {
    
    	cCtx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	// gax provides a basic backoff implementation for retries.
    	bo := gax.Backoff{
    		Initial: time.Second,
    	}
    
    	var entry *datacatalogpb.Entry
    	var err error
    
    	for {
    		entry, err = client.LookupEntry(cCtx, req)
    		if err != nil {
    			if err = gax.Sleep(cCtx, bo.Pause()); err != nil {
    				return nil, err
    			}
    			continue
    		}
    		return entry, err
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagRequest.html);
    import com.google.cloud.datacatalog.v1.[CreateTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateRequest.html);
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html);
    import com.google.cloud.datacatalog.v1.[FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html);
    import com.google.cloud.datacatalog.v1.[FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).[EnumType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.html);
    import com.google.cloud.datacatalog.v1.[FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).[EnumType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.html).EnumValue;
    import com.google.cloud.datacatalog.v1.[FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).[PrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.PrimitiveType.html);
    import com.google.cloud.datacatalog.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html);
    import com.google.cloud.datacatalog.v1.[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LookupEntryRequest.html);
    import com.google.cloud.datacatalog.v1.[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag.html);
    import com.google.cloud.datacatalog.v1.[TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html);
    import com.google.cloud.datacatalog.v1.[TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate.html);
    import com.google.cloud.datacatalog.v1.[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html);
    import java.io.IOException;
    
    public class Quickstart {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String tagTemplateId = "my_tag_template";
        createTags(projectId, tagTemplateId);
      }
    
      public static void createTags(String projectId, String tagTemplateId) throws IOException {
        // Currently, Data Catalog stores metadata in the us-central1 region.
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) dataCatalogClient = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
    
          // -------------------------------
          // Create a Tag Template.
          // -------------------------------
          [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html) sourceField =
              [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html).newBuilder()
                  .setDisplayName("Source of data asset")
                  .setType([FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).newBuilder().[setPrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_Builder_setPrimitiveType_com_google_cloud_datacatalog_v1_FieldType_PrimitiveType_)([PrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.PrimitiveType.html).STRING).build())
                  .build();
    
          [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html) numRowsField =
              [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html).newBuilder()
                  .setDisplayName("Number of rows in data asset")
                  .setType([FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).newBuilder().[setPrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_Builder_setPrimitiveType_com_google_cloud_datacatalog_v1_FieldType_PrimitiveType_)([PrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.PrimitiveType.html).DOUBLE).build())
                  .build();
    
          [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html) hasPiiField =
              [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html).newBuilder()
                  .setDisplayName("Has PII")
                  .setType([FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).newBuilder().[setPrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_Builder_setPrimitiveType_com_google_cloud_datacatalog_v1_FieldType_PrimitiveType_)([PrimitiveType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.PrimitiveType.html).BOOL).build())
                  .build();
    
          [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html) piiTypeField =
              [TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField.html).newBuilder()
                  .setDisplayName("PII type")
                  .setType(
                      [FieldType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.html).newBuilder()
                          .[setEnumType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_Builder_setEnumType_com_google_cloud_datacatalog_v1_FieldType_EnumType_)(
                              [EnumType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.html).newBuilder()
                                  .[addAllowedValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_EnumType_Builder_addAllowedValues_com_google_cloud_datacatalog_v1_FieldType_EnumType_EnumValue_)(
                                      EnumValue.newBuilder().setDisplayName("EMAIL").build())
                                  .[addAllowedValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_EnumType_Builder_addAllowedValues_com_google_cloud_datacatalog_v1_FieldType_EnumType_EnumValue_)(
                                      EnumValue.newBuilder()
                                          .setDisplayName("SOCIAL SECURITY NUMBER")
                                          .build())
                                  .[addAllowedValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.FieldType.EnumType.Builder.html#com_google_cloud_datacatalog_v1_FieldType_EnumType_Builder_addAllowedValues_com_google_cloud_datacatalog_v1_FieldType_EnumType_EnumValue_)(
                                      EnumValue.newBuilder().setDisplayName("NONE").build())
                                  .build())
                          .build())
                  .build();
    
          [TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate.html) tagTemplate =
              [TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate.html).newBuilder()
                  .setDisplayName("Demo Tag Template")
                  .putFields("source", sourceField)
                  .putFields("num_rows", numRowsField)
                  .putFields("has_pii", hasPiiField)
                  .putFields("pii_type", piiTypeField)
                  .build();
    
          [CreateTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateRequest.html) createTagTemplateRequest =
              [CreateTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateRequest.html).newBuilder()
                  .setParent(
                      [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html).newBuilder()
                          .setProject(projectId)
                          .setLocation(location)
                          .build()
                          .toString())
                  .[setTagTemplateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateRequest.Builder.html#com_google_cloud_datacatalog_v1_CreateTagTemplateRequest_Builder_setTagTemplateId_java_lang_String_)(tagTemplateId)
                  .setTagTemplate(tagTemplate)
                  .build();
    
          // Create the Tag Template.
          tagTemplate = dataCatalogClient.createTagTemplate(createTagTemplateRequest);
    
          // -------------------------------
          // Lookup Data Catalog's Entry referring to the table.
          // -------------------------------
          String linkedResource =
              String.format(
                  "//bigquery.googleapis.com/projects/%s/datasets/test_dataset/tables/test_table",
                  projectId);
          [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LookupEntryRequest.html) lookupEntryRequest =
              [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LookupEntryRequest.html).newBuilder().setLinkedResource(linkedResource).build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html) tableEntry = dataCatalogClient.lookupEntry(lookupEntryRequest);
    
          // -------------------------------
          // Attach a Tag to the table.
          // -------------------------------
          [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html) sourceValue =
              [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.Builder.html#com_google_cloud_datacatalog_v1_TagField_Builder_setStringValue_java_lang_String_)("Copied from tlc_yellow_trips_2017").build();
          [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html) numRowsValue = [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html).newBuilder().[setDoubleValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.Builder.html#com_google_cloud_datacatalog_v1_TagField_Builder_setDoubleValue_double_)(113496874).build();
          [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html) hasPiiValue = [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html).newBuilder().[setBoolValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.Builder.html#com_google_cloud_datacatalog_v1_TagField_Builder_setBoolValue_boolean_)(false).build();
          [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html) piiTypeValue =
              [TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html).newBuilder()
                  .[setEnumValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.Builder.html#com_google_cloud_datacatalog_v1_TagField_Builder_setEnumValue_com_google_cloud_datacatalog_v1_TagField_EnumValue_)([TagField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.html).EnumValue.newBuilder().setDisplayName("NONE").build())
                  .build();
    
          [Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag.html) tag =
              [Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag.html).newBuilder()
                  .[setTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag.Builder.html#com_google_cloud_datacatalog_v1_Tag_Builder_setTemplate_java_lang_String_)(tagTemplate.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate.html#com_google_cloud_datacatalog_v1_TagTemplate_getName__)())
                  .putFields("source", sourceValue)
                  .putFields("num_rows", numRowsValue)
                  .putFields("has_pii", hasPiiValue)
                  .putFields("pii_type", piiTypeValue)
                  .build();
    
          [CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagRequest.html) createTagRequest =
              [CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagRequest.html).newBuilder().setParent(tableEntry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html#com_google_cloud_datacatalog_v1_Entry_getName__)()).setTag(tag).build();
    
          dataCatalogClient.createTag(createTagRequest);
          System.out.printf("Tag created successfully");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library and create a client.
    const {DataCatalogClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const datacatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function quickstart() {
      // Common fields.
      let request;
      let responses;
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project'; // Google Cloud Platform project
      // const datasetId = 'demo_dataset';
      // const tableId = 'trips';
    
      // Currently, Data Catalog stores metadata in the
      // us-central1 region.
      const location = 'us-central1';
    
      // Create Fields.
      const fieldSource = {
        displayName: 'Source of data asset',
        type: {
          primitiveType: 'STRING',
        },
      };
    
      const fieldNumRows = {
        displayName: 'Number of rows in data asset',
        type: {
          primitiveType: 'DOUBLE',
        },
      };
    
      const fieldHasPII = {
        displayName: 'Has PII',
        type: {
          primitiveType: 'BOOL',
        },
      };
    
      const fieldPIIType = {
        displayName: 'PII type',
        type: {
          enumType: {
            allowedValues: [
              {
                displayName: 'EMAIL',
              },
              {
                displayName: 'SOCIAL SECURITY NUMBER',
              },
              {
                displayName: 'NONE',
              },
            ],
          },
        },
      };
    
      // Create Tag Template.
      const tagTemplateId = 'demo_tag_template';
    
      const tagTemplate = {
        displayName: 'Demo Tag Template',
        fields: {
          source: fieldSource,
          num_rows: fieldNumRows,
          has_pii: fieldHasPII,
          pii_type: fieldPIIType,
        },
      };
    
      const tagTemplatePath = datacatalog.tagTemplatePath(
        projectId,
        location,
        tagTemplateId
      );
    
      // Delete any pre-existing Template with the same name.
      try {
        request = {
          name: tagTemplatePath,
          force: true,
        };
        await datacatalog.deleteTagTemplate(request);
        console.log(`Deleted template: ${tagTemplatePath}`);
      } catch (error) {
        console.log(`Cannot delete template: ${tagTemplatePath}`);
      }
    
      // Create the Tag Template request.
      const locationPath = datacatalog.locationPath(projectId, location);
    
      request = {
        parent: locationPath,
        tagTemplateId: tagTemplateId,
        tagTemplate: tagTemplate,
      };
    
      // Execute the request.
      responses = await datacatalog.createTagTemplate(request);
      const createdTagTemplate = responses[0];
      console.log(`Created template: ${createdTagTemplate.name}`);
    
      // Lookup Data Catalog's Entry referring to the table.
      responses = await datacatalog.lookupEntry({
        linkedResource:
          '//bigquery.googleapis.com/projects/' +
          `${projectId}/datasets/${datasetId}/tables/${tableId}`,
      });
      const entry = responses[0];
      console.log(`Entry name: ${entry.name}`);
      console.log(`Entry type: ${entry.type}`);
      console.log(`Linked resource: ${entry.linkedResource}`);
    
      // Attach a Tag to the table.
      const tag = {
        name: entry.name,
        template: createdTagTemplate.name,
        fields: {
          source: {
            stringValue: 'copied from tlc_yellow_trips_2017',
          },
          num_rows: {
            doubleValue: 113496874,
          },
          has_pii: {
            boolValue: false,
          },
          pii_type: {
            enumValue: {
              displayName: 'NONE',
            },
          },
        },
      };
    
      request = {
        parent: entry.name,
        tag: tag,
      };
    
      // Create the Tag.
      await datacatalog.createTag(request);
      console.log(`Tag created for entry: ${entry.name}`);
    }
    quickstart();

### Python

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import required modules.
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    
    # TODO: Set these values before running the sample.
    # Google Cloud Platform project.
    project_id = "my_project"
    # Set dataset_id to the ID of existing dataset.
    dataset_id = "demo_dataset"
    # Set table_id to the ID of existing table.
    table_id = "trips"
    # Tag template to create.
    tag_template_id = "example_tag_template"
    
    # For all regions available, see:
    # https://cloud.google.com/data-catalog/docs/concepts/regions
    location = "us-central1"
    
    # Use Application Default Credentials to create a new
    # Data Catalog client. GOOGLE_APPLICATION_CREDENTIALS
    # environment variable must be set with the location
    # of a service account key file.
    datacatalog_client = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html)()
    
    # Create a Tag Template.
    tag_template = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagTemplate](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplate.html)()
    
    tag_template.display_name = "Demo Tag Template"
    
    tag_template.fields["source"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagTemplateField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplateField.html)()
    tag_template.fields["source"].display_name = "Source of data asset"
    tag_template.fields[
        "source"
    ].type_.primitive_type = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[FieldType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.html).[PrimitiveType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.PrimitiveType.html).STRING
    
    tag_template.fields["num_rows"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagTemplateField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplateField.html)()
    tag_template.fields["num_rows"].display_name = "Number of rows in data asset"
    tag_template.fields[
        "num_rows"
    ].type_.primitive_type = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[FieldType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.html).[PrimitiveType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.PrimitiveType.html).DOUBLE
    
    tag_template.fields["has_pii"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagTemplateField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplateField.html)()
    tag_template.fields["has_pii"].display_name = "Has PII"
    tag_template.fields[
        "has_pii"
    ].type_.primitive_type = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[FieldType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.html).[PrimitiveType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.PrimitiveType.html).BOOL
    
    tag_template.fields["pii_type"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagTemplateField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplateField.html)()
    tag_template.fields["pii_type"].display_name = "PII type"
    
    for display_name in ["EMAIL", "SOCIAL SECURITY NUMBER", "NONE"]:
        enum_value = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[FieldType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.html).[EnumType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.FieldType.EnumType.html).EnumValue(
            display_name=display_name
        )
        tag_template.fields["pii_type"].type_.enum_type.allowed_values.append(
            enum_value
        )
    
    expected_template_name = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html).tag_template_path(
        project_id, location, tag_template_id
    )
    
    # Create the Tag Template.
    try:
        tag_template = datacatalog_client.[create_tag_template](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_tag_template)(
            parent=f"projects/{project_id}/locations/{location}",
            tag_template_id=tag_template_id,
            tag_template=tag_template,
        )
        print(f"Created template: {tag_template.name}")
    except OSError as e:
        print(f"Cannot create template: {expected_template_name}")
        print(f"{e}")
    
    # Lookup Data Catalog's Entry referring to the table.
    resource_name = (
        f"//bigquery.googleapis.com/projects/{project_id}"
        f"/datasets/{dataset_id}/tables/{table_id}"
    )
    table_entry = datacatalog_client.[lookup_entry](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_lookup_entry)(
        request={"linked_resource": resource_name}
    )
    
    # Attach a Tag to the table.
    tag = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[Tag](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.Tag.html)()
    
    tag.template = tag_template.name
    tag.name = "my_super_cool_tag"
    
    tag.fields["source"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagField.html)()
    tag.fields["source"].string_value = "Copied from tlc_yellow_trips_2018"
    
    tag.fields["num_rows"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagField.html)()
    tag.fields["num_rows"].double_value = 113496874
    
    tag.fields["has_pii"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagField.html)()
    tag.fields["has_pii"].bool_value = False
    
    tag.fields["pii_type"] = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[TagField](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagField.html)()
    tag.fields["pii_type"].enum_value.display_name = "NONE"
    
    tag = datacatalog_client.[create_tag](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_tag)(parent=table_entry.name, tag=tag)
    print(f"Created tag: {tag.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
