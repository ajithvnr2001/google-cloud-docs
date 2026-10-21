---
url: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-create-autoscaling-cluster/
title: Create autoscaling cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:56.169594+00:00
---

# Create autoscaling cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/samples/dataproc-create-autoscaling-cluster/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Samples ](https://docs.cloud.google.com/managed-spark/docs/samples)



#  Create autoscaling cluster Stay organized with collections  Save and categorize content based on your preferences. 

Creates a Dataproc cluster with an autoscaling policy.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/overview). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dataproc.v1.[AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingConfig.html);
    import com.google.cloud.dataproc.v1.[AutoscalingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicy.html);
    import com.google.cloud.dataproc.v1.[AutoscalingPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceClient.html);
    import com.google.cloud.dataproc.v1.[AutoscalingPolicyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceSettings.html);
    import com.google.cloud.dataproc.v1.[BasicAutoscalingAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicAutoscalingAlgorithm.html);
    import com.google.cloud.dataproc.v1.[BasicYarnAutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.html);
    import com.google.cloud.dataproc.v1.[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html);
    import com.google.cloud.dataproc.v1.[ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html);
    import com.google.cloud.dataproc.v1.[ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html);
    import com.google.cloud.dataproc.v1.[ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html);
    import com.google.cloud.dataproc.v1.[ClusterOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterOperationMetadata.html);
    import com.google.cloud.dataproc.v1.[InstanceGroupAutoscalingPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.html);
    import com.google.cloud.dataproc.v1.[InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html);
    import com.google.cloud.dataproc.v1.[RegionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.RegionName.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateClusterWithAutoscaling {
    
      public static void createClusterwithAutoscaling() throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String region = "your-project-region";
        String clusterName = "your-cluster-name";
        String autoscalingPolicyName = "your-autoscaling-policy";
        createClusterwithAutoscaling(projectId, region, clusterName, autoscalingPolicyName);
      }
    
      public static void createClusterwithAutoscaling(
          String projectId, String region, String clusterName, String autoscalingPolicyName)
          throws IOException, InterruptedException {
        String myEndpoint = String.format("%s-dataproc.googleapis.com:443", region);
    
        // Configure the settings for the cluster controller client.
        [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html) clusterControllerSettings =
            [ClusterControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Configure the settings for the autoscaling policy service client.
        [AutoscalingPolicyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceSettings.html) autoscalingPolicyServiceSettings =
            [AutoscalingPolicyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceSettings.html).newBuilder().setEndpoint(myEndpoint).build();
    
        // Create a cluster controller client and an autoscaling controller client with the configured
        // settings. The clients only need to be created once and can be reused for multiple requests.
        // Using a
        // try-with-resources closes the client, but this can also be done manually with the .close()
        // method.
        try ([ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html) clusterControllerClient =
                [ClusterControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html).create(clusterControllerSettings);
            [AutoscalingPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceClient.html) autoscalingPolicyServiceClient =
                [AutoscalingPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicyServiceClient.html).create(autoscalingPolicyServiceSettings)) {
    
          // Create the Autoscaling policy.
          [InstanceGroupAutoscalingPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.html) workerInstanceGroupAutoscalingPolicyConfig =
              [InstanceGroupAutoscalingPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.html).newBuilder()
                  .[setMinInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setMinInstances_int_)(2)
                  .[setMaxInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setMaxInstances_int_)(100)
                  .[setWeight](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setWeight_int_)(1)
                  .build();
          [InstanceGroupAutoscalingPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.html) secondaryWorkerInstanceGroupAutoscalingPolicyConfig =
              [InstanceGroupAutoscalingPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.html).newBuilder()
                  .[setMinInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setMinInstances_int_)(0)
                  .[setMaxInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setMaxInstances_int_)(100)
                  .[setWeight](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupAutoscalingPolicyConfig_Builder_setWeight_int_)(1)
                  .build();
          [BasicYarnAutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.html) basicYarnApplicationConfig =
              [BasicYarnAutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.html).newBuilder()
                  .[setScaleUpFactor](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.Builder.html#com_google_cloud_dataproc_v1_BasicYarnAutoscalingConfig_Builder_setScaleUpFactor_double_)(0.05)
                  .[setScaleDownFactor](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.Builder.html#com_google_cloud_dataproc_v1_BasicYarnAutoscalingConfig_Builder_setScaleDownFactor_double_)(1.0)
                  .[setScaleUpMinWorkerFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.Builder.html#com_google_cloud_dataproc_v1_BasicYarnAutoscalingConfig_Builder_setScaleUpMinWorkerFraction_double_)(0.0)
                  .[setScaleUpMinWorkerFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicYarnAutoscalingConfig.Builder.html#com_google_cloud_dataproc_v1_BasicYarnAutoscalingConfig_Builder_setScaleUpMinWorkerFraction_double_)(0.0)
                  .setGracefulDecommissionTimeout([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3600).build())
                  .build();
          [BasicAutoscalingAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicAutoscalingAlgorithm.html) basicAutoscalingAlgorithm =
              [BasicAutoscalingAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicAutoscalingAlgorithm.html).newBuilder()
                  .[setCooldownPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicAutoscalingAlgorithm.Builder.html#com_google_cloud_dataproc_v1_BasicAutoscalingAlgorithm_Builder_setCooldownPeriod_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(240).build())
                  .[setYarnConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.BasicAutoscalingAlgorithm.Builder.html#com_google_cloud_dataproc_v1_BasicAutoscalingAlgorithm_Builder_setYarnConfig_com_google_cloud_dataproc_v1_BasicYarnAutoscalingConfig_)(basicYarnApplicationConfig)
                  .build();
          [AutoscalingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicy.html) autoscalingPolicy =
              [AutoscalingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicy.html).newBuilder()
                  .setId(autoscalingPolicyName)
                  .setWorkerConfig(workerInstanceGroupAutoscalingPolicyConfig)
                  .setSecondaryWorkerConfig(secondaryWorkerInstanceGroupAutoscalingPolicyConfig)
                  .[setBasicAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingPolicy.Builder.html#com_google_cloud_dataproc_v1_AutoscalingPolicy_Builder_setBasicAlgorithm_com_google_cloud_dataproc_v1_BasicAutoscalingAlgorithm_)(basicAutoscalingAlgorithm)
                  .build();
          [RegionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.RegionName.html) parent = [RegionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.RegionName.html).of(projectId, region);
    
          // Policy is uploaded here.
          autoscalingPolicyServiceClient.createAutoscalingPolicy(parent, autoscalingPolicy);
    
          // Now the policy can be referenced when creating a cluster.
          String autoscalingPolicyUri =
              String.format(
                  "projects/%s/locations/%s/autoscalingPolicies/%s",
                  projectId, region, autoscalingPolicyName);
          [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingConfig.html) autoscalingConfig =
              [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingConfig.html).newBuilder().[setPolicyUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.AutoscalingConfig.Builder.html#com_google_cloud_dataproc_v1_AutoscalingConfig_Builder_setPolicyUri_java_lang_String_)(autoscalingPolicyUri).build();
    
          // Configure the settings for our cluster.
          [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) masterConfig =
              [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                  .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                  .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(1)
                  .build();
          [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html) workerConfig =
              [InstanceGroupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.html).newBuilder()
                  .[setMachineTypeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setMachineTypeUri_java_lang_String_)("n1-standard-2")
                  .[setNumInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Builder.html#com_google_cloud_dataproc_v1_InstanceGroupConfig_Builder_setNumInstances_int_)(2)
                  .build();
          [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html) clusterConfig =
              [ClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.html).newBuilder()
                  .[setMasterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setMasterConfig_com_google_cloud_dataproc_v1_InstanceGroupConfig_)(masterConfig)
                  .setWorkerConfig(workerConfig)
                  .[setAutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterConfig.Builder.html#com_google_cloud_dataproc_v1_ClusterConfig_Builder_setAutoscalingConfig_com_google_cloud_dataproc_v1_AutoscalingConfig_)(autoscalingConfig)
                  .build();
    
          // Create the cluster object with the desired cluster config.
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) cluster =
              [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html).newBuilder().setClusterName(clusterName).setConfig(clusterConfig).build();
    
          // Create the Dataproc cluster.
          OperationFuture<Cluster, ClusterOperationMetadata> createClusterAsyncRequest =
              clusterControllerClient.[createClusterAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ClusterControllerClient.html#com_google_cloud_dataproc_v1_ClusterControllerClient_createClusterAsync_com_google_cloud_dataproc_v1_CreateClusterRequest_)(projectId, region, cluster);
          [Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html) response = createClusterAsyncRequest.get();
    
          // Print out a success message.
          System.out.printf("Cluster created successfully: %s", response.[getClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.Cluster.html#com_google_cloud_dataproc_v1_Cluster_getClusterName__)());
    
        } catch (ExecutionException e) {
          // If cluster creation does not complete successfully, print the error message.
          System.err.println(String.format("createClusterWithAutoscaling: %s ", e.getMessage()));
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataproc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
