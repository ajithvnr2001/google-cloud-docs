---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-instantiate-inline-workflow-template/
title: Instantiate inline workflow template \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:41.606318+00:00
---

# Instantiate inline workflow template  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-instantiate-inline-workflow-template/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Instantiate inline workflow template Stay organized with collections  Save and categorize content based on your preferences. 

Instantiates an inline workflow template using Cloud Client Libraries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use inline workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/inline-workflows)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataproc/apiv1?tab=doc). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dataproc "cloud.google.com/go/dataproc/apiv1"
    	"cloud.google.com/go/dataproc/apiv1/dataprocpb"
    	"google.golang.org/api/option"
    )
    
    func instantiateInlineWorkflowTemplate(w io.Writer, projectID, region string) error {
    	// projectID := "your-project-id"
    	// region := "us-central1"
    
    	ctx := context.Background()
    
    	// Create the cluster client.
    	endpoint := region + "-dataproc.googleapis.com:443"
    	workflowTemplateClient, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/latest/apiv1.html#cloud_google_com_go_dataproc_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("dataproc.NewWorkflowTemplateClient: %w", err)
    	}
    	defer workflowTemplateClient.Close()
    
    	// Create jobs for the workflow.
    	teragenJob := &dataprocpb.OrderedJob{
    		JobType: &dataprocpb.OrderedJob_HadoopJob{
    			HadoopJob: &dataprocpb.HadoopJob{
    				Driver: &dataprocpb.HadoopJob_MainJarFileUri{
    					MainJarFileUri: "file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
    				},
    				Args: []string{
    					"teragen",
    					"1000",
    					"hdfs:///gen/",
    				},
    			},
    		},
    		StepId: "teragen",
    	}
    
    	terasortJob := &dataprocpb.OrderedJob{
    		JobType: &dataprocpb.OrderedJob_HadoopJob{
    			HadoopJob: &dataprocpb.HadoopJob{
    				Driver: &dataprocpb.HadoopJob_MainJarFileUri{
    					MainJarFileUri: "file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
    				},
    				Args: []string{
    					"terasort",
    					"hdfs:///gen/",
    					"hdfs:///sort/",
    				},
    			},
    		},
    		StepId: "terasort",
    		PrerequisiteStepIds: []string{
    			"teragen",
    		},
    	}
    
    	// Create the cluster placement.
    	clusterPlacement := &dataprocpb.WorkflowTemplatePlacement{
    		Placement: &dataprocpb.WorkflowTemplatePlacement_ManagedCluster{
    			ManagedCluster: &dataprocpb.ManagedCluster{
    				ClusterName: "my-managed-cluster",
    				Config: &dataprocpb.ClusterConfig{
    					GceClusterConfig: &dataprocpb.GceClusterConfig{
    						// Leave "ZoneUri" empty for "Auto Zone Placement"
    						// ZoneUri: ""
    						ZoneUri: "us-central1-a",
    					},
    				},
    			},
    		},
    	}
    
    	// Create the Instantiate Inline Workflow Template Request.
    	req := &dataprocpb.InstantiateInlineWorkflowTemplateRequest{
    		Parent: fmt.Sprintf("projects/%s/regions/%s", projectID, region),
    		Template: &dataprocpb.WorkflowTemplate{
    			Jobs: []*dataprocpb.OrderedJob{
    				teragenJob,
    				terasortJob,
    			},
    			Placement: clusterPlacement,
    		},
    	}
    
    	// Create the cluster.
    	op, err := workflowTemplateClient.InstantiateInlineWorkflowTemplate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("InstantiateInlineWorkflowTemplate: %w", err)
    	}
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("InstantiateInlineWorkflowTemplate.Wait: %w", err)
    	}
    
    	// Output a success message.
    	fmt.Fprintf(w, "Workflow created successfully.")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dataproc.v1.[ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html);
    import com.google.cloud.dataproc.v1.[GceClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GceClusterConfig.html);
    import com.google.cloud.dataproc.v1.[HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html);
    import com.google.cloud.dataproc.v1.[ManagedCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ManagedCluster.html);
    import com.google.cloud.dataproc.v1.[OrderedJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.OrderedJob.html);
    import com.google.cloud.dataproc.v1.[RegionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.RegionName.html);
    import com.google.cloud.dataproc.v1.[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata.html);
    import com.google.cloud.dataproc.v1.[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate.html);
    import com.google.cloud.dataproc.v1.[WorkflowTemplatePlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplatePlacement.html);
    import com.google.cloud.dataproc.v1.[WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.html);
    import com.google.cloud.dataproc.v1.[WorkflowTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class InstantiateInlineWorkflowTemplate {
    
      public static void instantiateInlineWorkflowTemplate() throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String region = "your-project-region";
        instantiateInlineWorkflowTemplate(projectId, region);
      }
    
      public static void instantiateInlineWorkflowTemplate(String projectId, String region)
          throws IOException, InterruptedException {
        String myEndpoint = String.format("%s-dataproc.googleapis.com:443", region);
    
        // Configure the settings for the workflow template service client.
        [WorkflowTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings.html) workflowTemplateServiceSettings =
            [WorkflowTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Create a workflow template service client with the configured settings. The client only
        // needs to be created once and can be reused for multiple requests. Using a try-with-resources
        // closes the client, but this can also be done manually with the .close() method.
        try ([WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.html) workflowTemplateServiceClient =
            [WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.html).create(workflowTemplateServiceSettings)) {
    
          // Configure the jobs within the workflow.
          [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html) teragenHadoopJob =
              [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html).newBuilder()
                  .setMainJarFileUri("file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar")
                  .addArgs("teragen")
                  .addArgs("1000")
                  .addArgs("hdfs:///gen/")
                  .build();
          [OrderedJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.OrderedJob.html) teragen =
              [OrderedJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.OrderedJob.html).newBuilder().setHadoopJob(teragenHadoopJob).setStepId("teragen").build();
    
          [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html) terasortHadoopJob =
              [HadoopJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.HadoopJob.html).newBuilder()
                  .setMainJarFileUri("file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar")
                  .addArgs("terasort")
                  .addArgs("hdfs:///gen/")
                  .addArgs("hdfs:///sort/")
                  .build();
          [OrderedJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.OrderedJob.html) terasort =
              [OrderedJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.OrderedJob.html).newBuilder()
                  .setHadoopJob(terasortHadoopJob)
                  .addPrerequisiteStepIds("teragen")
                  .setStepId("terasort")
                  .build();
    
          // Configure the cluster placement for the workflow.
          // Leave "ZoneUri" empty for "Auto Zone Placement".
          // GceClusterConfig gceClusterConfig =
          //     GceClusterConfig.newBuilder().setZoneUri("").build();
          [GceClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GceClusterConfig.html) gceClusterConfig =
              [GceClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GceClusterConfig.html).newBuilder().[setZoneUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GceClusterConfig.Builder.html#com_google_cloud_dataproc_v1_GceClusterConfig_Builder_setZoneUri_java_lang_String_)("us-central1-a").build();
          [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) clusterConfig =
              [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html).newBuilder().[setGceClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setGceClusterConfig_com_google_cloud_dataproc_v1_GceClusterConfig_)(gceClusterConfig).build();
          [ManagedCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ManagedCluster.html) managedCluster =
              [ManagedCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ManagedCluster.html).newBuilder()
                  .setClusterName("my-managed-cluster")
                  .setConfig(clusterConfig)
                  .build();
          [WorkflowTemplatePlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplatePlacement.html) workflowTemplatePlacement =
              [WorkflowTemplatePlacement](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplatePlacement.html).newBuilder().[setManagedCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplatePlacement.Builder.html#com_google_cloud_dataproc_v1_WorkflowTemplatePlacement_Builder_setManagedCluster_com_google_cloud_dataproc_v1_ManagedCluster_)(managedCluster).build();
    
          // Create the inline workflow template.
          [WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate.html) workflowTemplate =
              [WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate.html).newBuilder()
                  .addJobs(teragen)
                  .addJobs(terasort)
                  .setPlacement(workflowTemplatePlacement)
                  .build();
    
          // Submit the instantiated inline workflow template request.
          String parent = [RegionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.RegionName.html).format(projectId, region);
          OperationFuture<Empty, WorkflowMetadata> instantiateInlineWorkflowTemplateAsync =
              workflowTemplateServiceClient.[instantiateInlineWorkflowTemplateAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.html#com_google_cloud_dataproc_v1_WorkflowTemplateServiceClient_instantiateInlineWorkflowTemplateAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataproc_v1_LocationName_com_google_cloud_dataproc_v1_WorkflowTemplate_)(
                  parent, workflowTemplate);
          [instantiateInlineWorkflowTemplateAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.html#com_google_cloud_dataproc_v1_WorkflowTemplateServiceClient_instantiateInlineWorkflowTemplateAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataproc_v1_LocationName_com_google_cloud_dataproc_v1_WorkflowTemplate_).get();
    
          // Print out a success message.
          System.out.printf("Workflow ran successfully.");
    
        } catch (ExecutionException e) {
          System.err.println(String.format("Error running workflow: %s ", e.getMessage()));
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const dataproc = require('[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)');
    
    // TODO(developer): Uncomment and set the following variables
    // projectId = 'YOUR_PROJECT_ID'
    // region = 'YOUR_REGION'
    
    // Create a client with the endpoint set to the desired region
    const client = new dataproc.v1.[WorkflowTemplateServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)({
      apiEndpoint: `${region}-dataproc.googleapis.com`,
      projectId: projectId,
    });
    
    async function instantiateInlineWorkflowTemplate() {
      // Create the formatted parent.
      const parent = client.regionPath(projectId, region);
    
      // Create the template
      const template = {
        jobs: [
          {
            hadoopJob: {
              mainJarFileUri:
                'file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar',
              args: ['teragen', '1000', 'hdfs:///gen/'],
            },
            stepId: 'teragen',
          },
          {
            hadoopJob: {
              mainJarFileUri:
                'file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar',
              args: ['terasort', 'hdfs:///gen/', 'hdfs:///sort/'],
            },
            stepId: 'terasort',
            prerequisiteStepIds: ['teragen'],
          },
        ],
        placement: {
          managedCluster: {
            clusterName: 'my-managed-cluster',
            config: {
              gceClusterConfig: {
                // Leave 'zoneUri' empty for 'Auto Zone Placement'
                // zoneUri: ''
                zoneUri: 'us-central1-a',
                internalIpOnly: false,
              },
            },
          },
        },
      };
    
      const request = {
        parent: parent,
        template: template,
      };
    
      // Submit the request to instantiate the workflow from an inline template.
      const [operation] = await client.instantiateInlineWorkflowTemplate(request);
      await operation.promise();
    
      // Output a success message
      console.log('Workflow ran successfully.');

### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import dataproc_v1 as dataproc
    
    
    def instantiate_inline_workflow_template(project_id, region):
        """This sample walks a user through submitting a workflow
        for a Cloud Dataproc using the Python client library.
    
        Args:
            project_id (string): Project to use for running the workflow.
            region (string): Region where the workflow resources should live.
        """
    
        # Create a client with the endpoint set to the desired region.
        workflow_template_client = dataproc.WorkflowTemplateServiceClient(
            client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
        )
    
        parent = f"projects/{project_id}/regions/{region}"
    
        template = {
            "jobs": [
                {
                    "hadoop_job": {
                        "main_jar_file_uri": "file:///usr/lib/hadoop-mapreduce/"
                        "hadoop-mapreduce-examples.jar",
                        "args": ["teragen", "1000", "hdfs:///gen/"],
                    },
                    "step_id": "teragen",
                },
                {
                    "hadoop_job": {
                        "main_jar_file_uri": "file:///usr/lib/hadoop-mapreduce/"
                        "hadoop-mapreduce-examples.jar",
                        "args": ["terasort", "hdfs:///gen/", "hdfs:///sort/"],
                    },
                    "step_id": "terasort",
                    "prerequisite_step_ids": ["teragen"],
                },
            ],
            "placement": {
                "managed_cluster": {
                    "cluster_name": "my-managed-cluster",
                    "config": {
                        "gce_cluster_config": {
                            # Leave 'zone_uri' empty for 'Auto Zone Placement'
                            # 'zone_uri': ''
                            "zone_uri": "us-central1-a"
                        }
                    },
                }
            },
        }
    
        # Submit the request to instantiate the workflow from an inline template.
        operation = workflow_template_client.instantiate_inline_workflow_template(
            request={"parent": parent, "template": template}
        )
        operation.result()
    
        # Output a success message.
        print("Workflow ran successfully.")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
