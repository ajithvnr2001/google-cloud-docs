---
url: https://docs.cloud.google.com/data-catalog/docs/quickstart-tagging/
title: Tag a BigQuery table using Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:54.857665+00:00
---

# Tag a BigQuery table using Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/quickstart-tagging/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tag a BigQuery table by using Data Catalog

This quickstart helps you complete the following tasks:

  1. Create a BigQuery dataset and table.

  2. Create a tag template with a schema that defines five tag fields of distinct types. These are `string`, `double`, `boolean`, `enumerated`, and `richtext`.

  3. Lookup the Data Catalog entry for your table.

  4. In the Google Cloud console, create business metadata for your entry that includes an overview, data steward, and a tag.




Data Catalog lets you search and tag entries such as BigQuery tables with metadata. Some examples of metadata that you can use for tagging include public and private tags, data stewards, and rich text overview.

## Before you begin

  1. Set up your project. 

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. Enable the Data Catalog and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datacatalog.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)

     4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

     7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     8. Enable the Data Catalog and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datacatalog.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)

     9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




## Add a public data entry to your project

Data Catalog entries include data resources such as a BigQuery dataset or a Pub/Sub topic.

  * Add a public dataset to your project.

    1. In Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

    2. In the **Explorer** section, click **Add data** and select **Public datasets** from the list.

    3. In the **Marketplace** panel, search for `New York taxi trips` and click the relevant search result.

    4. Click **View Dataset**.




## Create a dataset and a table

  1. Create a dataset.

     1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

     2. In the **Explorer** panel, select the project where you want to create the dataset.

     3. Click the more_vert**Actions** icon and click **Create dataset**.

     4. In the **Create dataset** page, fill in the following details:

        * For **Dataset ID** , enter `demo_dataset`.
        * For **Data location** , select `us (multiple regions in United States)`.
        * Enable table expiration and specify the number of days.
        * For **Encryption** , leave the **Google-managed encryption key** option selected.
        * Click **Create dataset**.

**Note:** You cannot add a description or a label when you create a dataset using the Google Cloud console. After the dataset is created, you can [add a description](https://docs.cloud.google.com/bigquery/docs/updating-datasets#update-dataset-description), and you can [add a label](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_a_label_to_a_dataset).
  2. Copy a publicly accessible table to `demo_dataset`.

     1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

     2. In the **Explorer** pane, search for `tlc_yellow_trips` tables (click **Broaden search to all projects** if required) and select one of them, such as `tlc_yellow_trips_2017`. Then click **Copy**.

     3. In the **Copy table** pane, fill in the following information:

        1. In the **Project name** drop-down list, select your project.
        2. In the **Dataset name** drop-down list, select `demo_dataset`.
        3. For the **Table name** , enter `trips`, then click **Copy**.
     4. In the **Explorer** pane, confirm that the `trips` table is listed in `demo_dataset`.




You add Data Catalog tags to the table in the next section.

## Create a public tag template and attach a tag for your entry

You must be the dataset owner to attach a tag to a table in the dataset. For more information about public and private tags, see [Public and private tags](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates?nocache=117221#public_and_private_tags).

In a tag template, tag fields are optional. You don't have to provide a value for a field when attaching a tag to a Data Catalog entry. However, if a template defines a field as required, you must provide a value for the field. If the value is not provided, an error is generated.

You can use lower case letters and underscores to define field names. The tag template fields created in this example are demo fields and aren't auto-updated or synced with BigQuery.

###  Console 

  1. Go to the Knowledge Catalog **Tag Templates** page.

[Go to Tag templates](https://console.cloud.google.com/dataplex/templates)

  2. Click **Create tag template** and enter the following details:

     1. Enter the **Template name** as `Demo Tag Template`.
     2. Retain the default location.
     3. Retain the tag template visibility as **Public**.
     4. Click **Add field** to add 5 fields. Use the following table and keep **Field description** empty.

Field display name | Field ID | Required field | Type  
---|---|---|---  
Source of data asset | source | Yes | String  
Rows in the asset | num_rows | No | Double  
Has PII | has_pii | No | Boolean  
PII type  | pii_type  | No  | Enumerated Add values `EMAIL_ADDRESS`, `US_SOCIAL_SECURITY_NUMBER`, and `NONE`.  
Context | context | No | Richtext  
  3. Click **Create**.

The **Template details** page lists all the information about the tag template.

  4. To attach a tag to `demo_dataset`, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/search)

  5. For **Choose search platform** , select **Data Catalog** as the search mode.

  6. In the search box, enter `demo_dataset`. In the search result, you see the `demo_dataset` dataset and the `trips` table.

  7. Click the `trips` table. A **BigQuery table details** page opens.

  8. Click **Attach tags**.

  9. In the **Attach tags** panel, enter the following details:

     1. Select the target as `trips`.
     2. Select the tag template as `Demo Tag Template`.
     3. For tag values, enter the following details: 
        * Source of data asset: `Copied from tlc_yellow_trips_2017`
        * Number of rows in the data asset: `113496874`
        * Has PII: `FALSE`
        * PII type: `NONE`
     4. Click **Save**.

The tag fields are now listed in the **Tags** section in the BigQuery table details.




###  gcloud 

Run the [gcloud data-catalog tag-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/tag-templates/create) command shown below to create a tag template with the following five tag fields:

  1. `display_name:` Source of data asset   
`id:` source   
`required:` TRUE   
`type:` String 
  2. `display_name:` Number of rows in the data asset   
`id:` num_rows   
`required:` FALSE   
`type:` Double 
  3. `display_name:` Has PII   
`id:` has_pii   
`required:` FALSE   
`type:` Boolean 
  4. `display_name:` PII type   
`id:` pii_type   
`required:` FALSE   
`type:` Enumerated   
`values:`
     1. EMAIL_ADDRESS
     2. US_SOCIAL_SECURITY_NUMBER
     3. NONE


    
    
    
    # -------------------------------
    # Create a Tag Template.
    # -------------------------------
    
    gcloud data-catalog tag-templates create demo_template \
        --location=us-central1 \
        --display-name="Demo Tag Template" \
        --field=id=source,display-name="Source of data asset",type=string,required=TRUE \
        --field=id=num_rows,display-name="Number of rows in the data asset",type=double \
        --field=id=has_pii,display-name="Has PII",type=bool \
        --field=id=pii_type,display-name="PII type",type='enum(EMAIL_ADDRESS|US_SOCIAL_SECURITY_NUMBER|NONE)'
    
    # -------------------------------
    # Lookup the Data Catalog entry for the table.
    # -------------------------------
    
    ENTRY_NAME=$(gcloud data-catalog entries lookup '//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET/tables/TABLE' --format="value(name)")
    
    # -------------------------------
    # Attach a Tag to the table.
    # -------------------------------
    
    # Create the Tag file.
    cat > tag_file.json << EOF
      {
        "source": "BigQuery",
        "num_rows": 1000,
        "has_pii": true,
        "pii_type": "EMAIL_ADDRESS"
      }
    EOF
    
    gcloud data-catalog tags create --entry=${ENTRY_NAME} \
        --tag-template=demo_template --tag-template-location=us-central1 --tag-file=tag_file.json
    

The location parameter specifies the Compute Engine resource [region](https://docs.cloud.google.com/compute/docs/regions-zones#available). Currently, Data Catalog supports only the `us-central1 region`. 

###  Go 

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
    

###  Java 

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

###  Node.js 

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

###  Python 

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

###  REST & CMD LINE 

### REST

If you do not have access to Cloud Client libraries for your language or want to test the API using REST requests, see the following examples and refer to the [Data Catalog REST API](https://docs.cloud.google.com/data-catalog/docs/reference/rest) documentation.

### Create a tag template.

Before using any of the request data, make the following replacements: 

  * project-id: your Google Cloud project ID



HTTP method and URL: 
    
    
    POST https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/tagTemplates?tagTemplateId=demo_tag_template

Request JSON body: 
    
    
    
    {
      "displayName":"Demo Tag Template",
      "fields":{
        "source":{
          "displayName":"Source of data asset",
          "isRequired": "true",
          "type":{
            "primitiveType":"STRING"
          }
        },
        "num_rows":{
          "displayName":"Number of rows in data asset",
          "isRequired": "false",
          "type":{
            "primitiveType":"DOUBLE"
          }
        },
        "has_pii":{
          "displayName":"Has PII",
          "isRequired": "false",
          "type":{
            "primitiveType":"BOOL"
          }
        },
        "pii_type":{
          "displayName":"PII type",
          "isRequired": "false",
          "type":{
            "enumType":{
              "allowedValues":[
                {
                  "displayName":"EMAIL_ADDRESS"
                },
                {
                  "displayName":"US_SOCIAL_SECURITY_NUMBER"
                },
                {
                  "displayName":"NONE"
                }
              ]
            }
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/tagTemplates?tagTemplateId=demo_tag_template"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/tagTemplates?tagTemplateId=demo_tag_template" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/project-id/locations/us-central1/tagTemplates/demo_tag_template",
      "displayName":"Demo Tag Template",
      "fields":{
        "num_rows":{
          "displayName":"Number of rows in data asset",
          "isRequired": "false",
          "type":{
            "primitiveType":"DOUBLE"
          }
        },
        "has_pii":{
          "displayName":"Has PII",
          "isRequired": "false",
          "type":{
            "primitiveType":"BOOL"
          }
        },
        "pii_type":{
          "displayName":"PII type",
          "isRequired": "false",
          "type":{
            "enumType":{
              "allowedValues":[
                {
                  "displayName":"EMAIL_ADDRESS"
                },
                {
                  "displayName":"NONE"
                },
                {
                  "displayName":"US_SOCIAL_SECURITY_NUMBER"
                }
              ]
            }
          }
        },
        "source":{
          "displayName":"Source of data asset",
          "isRequired":"true",
          "type":{
            "primitiveType":"STRING"
          }
        }
      }
    }
    

### Lookup the Data Catalog `entry-id` for your BigQuery table

Before using any of the request data, make the following replacements: 

  * project-id: Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://datacatalog.googleapis.com/v1/entries:lookup?linkedResource=//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/trips

Request JSON body: 
    
    
    Request body is empty.
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/entries:lookup?linkedResource=//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/trips"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/entries:lookup?linkedResource=//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/trips" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-id/locations/US/entryGroups/@bigquery/entries/entry-id",
      "type": "TABLE",
      "schema": {
        "columns": [
          {
            "type": "STRING",
            "description": "A code indicating the TPEP provider that provided the record. 1= ",
            "mode": "REQUIRED",
            "column": "vendor_id"
          },
          ...
        ]
      },
      "sourceSystemTimestamps": {
        "createTime": "2019-01-25T01:45:29.959Z",
        "updateTime": "2019-03-19T23:20:26.540Z"
      },
      "linkedResource": "//bigquery.googleapis.com/projects/project-id/datasets/demo_dataset/tables/trips",
      "bigqueryTableSpec": {
        "tableSourceType": "BIGQUERY_TABLE"
      }
    }
    

### Create a tag from the template and attach it to your BigQuery table

Before using any of the request data, make the following replacements: 

  * project-id: Google Cloud project ID
  * entry-id: Data Catalog entry ID for the Demo Dataset trips table (returned in the lookup results in the previous step).



HTTP method and URL: 
    
    
    POST https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups/@bigquery/entries/entry-id/tags

Request JSON body: 
    
    
    {
      "template":"projects/project-id/locations/us-central1/tagTemplates/demo_tag_template",
      "fields":{
        "source":{
          "stringValue":"Copied from tlc_yellow_trips_2017"
        },
        "num_rows":{
          "doubleValue":113496874
        },
        "has_pii":{
          "boolValue":false
        },
        "pii_type":{
          "enumValue":{
            "displayName":"NONE"
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups/@bigquery/entries/entry-id/tags"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups/@bigquery/entries/entry-id/tags" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/project-id/locations/US/entryGroups/@bigquery/entries/entry-id/tags/tag-id",
      "template":"projects/project-id/locations/us-central1/tagTemplates/demo_tag_template",
      "fields":{
        "pii_type":{
          "displayName":"PII type",
          "enumValue":{
            "displayName":"NONE"
          }
        },
        "has_pii":{
          "displayName":"Has PII",
          "boolValue":false
        },
        "source":{
          "displayName":"Source of data asset",
          "stringValue":"Copied from tlc_yellow_trips_2017"
        },
        "num_rows":{
          "displayName":"Number of rows in data asset",
          "doubleValue":113496874
        }
      },
      "templateDisplayName":"Demo Tag Template"
    }
    

**Caution:** [Renaming the table in BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#alter_table_rename_to_statement) deletes all the tags attached to it and its columns.

## Create an overview for your entry

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Within Google Cloud console, you can use rich text to describe an entry in your Data Catalog project.

  1. To create an overview for the `trips` table, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/search)

  2. For **Choose search platform** , select **Data Catalog** as the search mode.

  3. In the search box, enter `demo_dataset`.

In the search result, you see the `demo_dataset` dataset and the `trips` table.

  4. Click the `trips` table.

A **BigQuery table details** page opens.

  5. Click **Add overview** and enter some text. You can additionally include images and rich formatted text.

  6. Click **Save**.




## Add a data steward for your entry

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Within Google Cloud console, you can add one or more data stewards to an entry in your Data Catalog project. A data steward for a data entry can be contacted to request more information about the data entry.

  1. To create an overview for the `trips` table, repeat the first 3 steps from the previous section.

  2. Click the **Edit Steward** icon and add in one or more email addresses.

You can add a user with a non-Google email account.

  3. Click **Save**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the dataset

  1. If necessary, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, search for the `demo_dataset` dataset you created.

  3. Click the more_vert**Actions** option and click **Delete dataset**.

  4. Confirm your delete action.




### Delete the tag template

  1. Go to the **Data Catalog** > **Templates** page.

[Go to Data Catalog templates](https://console.cloud.google.com/datacatalog/templates)

  2. Select **Demo Tag Template**.

  3. In the row, click the more_vert**Actions** option and click **Delete this template**.

  4. Confirm your delete action.




## What's next

  * Learn more about [Data Catalog](https://docs.cloud.google.com/data-catalog/docs/concepts/introduction-data-catalog).

  * Learn about [technical metadata](https://docs.cloud.google.com/data-catalog/docs/concepts/metadata#types_of_technical_metadata) and [business metadata](https://docs.cloud.google.com/data-catalog/docs/concepts/metadata#types_of_business_metadata).

  * Learn about tag templates, public tags, and private tags in [Tags and tag templates](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates).

  * Browse the [Overview of APIs and Client Libraries](https://docs.cloud.google.com/data-catalog/docs/api-libraries-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
