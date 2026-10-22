---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-quickstart/
title: Demonstrate batch query translation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:24.181655+00:00
---

# Demonstrate batch query translation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerymigration-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Demonstrate batch query translation Stay organized with collections  Save and categorize content based on your preferences. 

Uses the BigQuery Migration service to translate queries stored in Cloud Storage

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // The bigquery_migration_quickstart application demonstrates basic usage of the
    // BigQuery migration API by executing a workflow that performs a batch SQL
    // translation task.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"time"
    
    	migration "cloud.google.com/go/bigquery/migration/apiv2"
    	"cloud.google.com/go/bigquery/migration/apiv2/migrationpb"
    )
    
    func main() {
    	// Define command line flags for controlling the behavior of this quickstart.
    	projectID := flag.String("project_id", "", "Cloud Project ID.")
    	location := flag.String("location", "us", "BigQuery Migration location used for interactions.")
    	outputPath := flag.String("output", "", "Cloud Storage path for translated resources.")
    	// Parse flags and do some minimal validation.
    	flag.Parse()
    	if *projectID == "" {
    		log.Fatal("empty --project_id specified, please provide a valid project ID")
    	}
    	if *location == "" {
    		log.Fatal("empty --location specified, please provide a valid location")
    	}
    	if *outputPath == "" {
    		log.Fatalf("empty --output specified, please provide a valid cloud storage path")
    	}
    
    	ctx := context.Background()
    	migClient, err := migration.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/migration/apiv2.html#cloud_google_com_go_bigquery_migration_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("migration.NewClient: %v", err)
    	}
    	defer migClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/migration/apiv2.html#cloud_google_com_go_bigquery_migration_apiv2_Client_Close)()
    
    	workflow, err := executeTranslationWorkflow(ctx, migClient, *projectID, *location, *outputPath)
    	if err != nil {
    		log.Fatalf("workflow execution failed: %v\n", err)
    	}
    
    	reportWorkflowStatus(workflow)
    }
    
    // executeTranslationWorkflow constructs a migration workflow that performs batch SQL translation.
    func executeTranslationWorkflow(ctx context.Context, client *migration.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/migration/apiv2.html#cloud_google_com_go_bigquery_migration_apiv2_Client), projectID, location, outPath string) (*migrationpb.MigrationWorkflow, error) {
    
    	// Construct the workflow creation request.  In this workflow, we have only a single translation task present.
    	req := &migrationpb.CreateMigrationWorkflowRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		MigrationWorkflow: &migrationpb.MigrationWorkflow{
    			DisplayName: "example SQL conversion",
    			Tasks: map[string]*migrationpb.MigrationTask{
    				"example_conversion": {
    					Type: "Translation_Teradata2BQ",
    					TaskDetails: &migrationpb.MigrationTask_TranslationConfigDetails{
    						TranslationConfigDetails: &migrationpb.TranslationConfigDetails{
    							SourceLocation: &migrationpb.TranslationConfigDetails_GcsSourcePath{
    								GcsSourcePath: "gs://cloud-samples-data/bigquery/migration/translation/input/",
    							},
    							TargetLocation: &migrationpb.TranslationConfigDetails_GcsTargetPath{
    								GcsTargetPath: outPath,
    							},
    							SourceDialect: &migrationpb.Dialect{
    								DialectValue: &migrationpb.Dialect_TeradataDialect{
    									TeradataDialect: &migrationpb.TeradataDialect{
    										Mode: migrationpb.[TeradataDialect_SQL](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/migration/apiv2/migrationpb.html#cloud_google_com_go_bigquery_migration_apiv2_migrationpb_TeradataDialect_MODE_UNSPECIFIED_TeradataDialect_SQL_TeradataDialect_BTEQ),
    									},
    								},
    							},
    							TargetDialect: &migrationpb.Dialect{
    								DialectValue: &migrationpb.Dialect_BigqueryDialect{},
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    
    	// Create the workflow using the request.
    	workflow, err := client.CreateMigrationWorkflow(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateMigrationWorkflow: %w", err)
    	}
    	fmt.Printf("workflow created: %s", workflow.GetName())
    
    	// This is an asyncronous process, so we now poll the workflow
    	// until completion or a suitable timeout has elapsed.
    	timeoutCtx, cancel := context.WithTimeout(ctx, 5*time.Minute)
    	defer cancel()
    	for {
    		select {
    		case <-timeoutCtx.Done():
    			return nil, fmt.Errorf("task %s didn't complete due to context expiring", workflow.GetName())
    		default:
    			polledWorkflow, err := client.GetMigrationWorkflow(timeoutCtx, &migrationpb.GetMigrationWorkflowRequest{
    				Name: workflow.GetName(),
    			})
    			if err != nil {
    				return nil, fmt.Errorf("polling ended in error: %w", err)
    			}
    			if polledWorkflow.GetState() == migrationpb.[MigrationWorkflow_COMPLETED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/migration/apiv2/migrationpb.html#cloud_google_com_go_bigquery_migration_apiv2_migrationpb_MigrationWorkflow_STATE_UNSPECIFIED_MigrationWorkflow_DRAFT_MigrationWorkflow_RUNNING_MigrationWorkflow_PAUSED_MigrationWorkflow_COMPLETED) {
    				// polledWorkflow contains the most recent metadata about the workflow, so we return that.
    				return polledWorkflow, nil
    			}
    			// workflow still isn't complete, so sleep briefly before polling again.
    			time.Sleep(5 * time.Second)
    		}
    	}
    }
    
    // reportWorkflowStatus prints information about the workflow execution in a more human readable format.
    func reportWorkflowStatus(workflow *migrationpb.MigrationWorkflow) {
    	fmt.Printf("Migration workflow %s ended in state %s.\n", workflow.GetName(), workflow.GetState().String())
    	for k, task := range workflow.GetTasks() {
    		fmt.Printf(" - Task %s had id %s", k, task.GetId())
    		if task.GetProcessingError() != nil {
    			fmt.Printf(" with processing error: %s", task.GetProcessingError().GetReason())
    		}
    		fmt.Println()
    	}
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
