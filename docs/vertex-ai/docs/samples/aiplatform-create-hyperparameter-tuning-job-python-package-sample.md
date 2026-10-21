---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-hyperparameter-tuning-job-python-package-sample/
title: Create a hyperparameter tuning job for python package \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:25.494772+00:00
---

# Create a hyperparameter tuning job for python package  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-hyperparameter-tuning-job-python-package-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a hyperparameter tuning job for python package Stay organized with collections  Save and categorize content based on your preferences. 

Creates a hyperparameter tuning job for python package using the create_hyperparameter_tuning_job method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a hyperparameter tuning job](https://docs.cloud.google.com/vertex-ai/docs/training/using-hyperparameter-tuning)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[AcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AcceleratorType.html);
    import com.google.cloud.aiplatform.v1.[CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html);
    import com.google.cloud.aiplatform.v1.[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html);
    import com.google.cloud.aiplatform.v1.[PythonPackageSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).MetricSpec;
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).MetricSpec.GoalType;
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html).[DiscreteValueCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[DiscreteValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DiscreteValueSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[DoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[ScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ScaleType.html);
    import com.google.cloud.aiplatform.v1.[WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html);
    import java.io.IOException;
    import java.util.Arrays;
    
    public class CreateHyperparameterTuningJobPythonPackageSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String displayName = "DISPLAY_NAME";
        String executorImageUri = "EXECUTOR_IMAGE_URI";
        String packageUri = "PACKAGE_URI";
        String pythonModule = "PYTHON_MODULE";
        createHyperparameterTuningJobPythonPackageSample(
            project, displayName, executorImageUri, packageUri, pythonModule);
      }
    
      static void createHyperparameterTuningJobPythonPackageSample(
          String project,
          String displayName,
          String executorImageUri,
          String packageUri,
          String pythonModule)
          throws IOException {
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          // study spec
          MetricSpec metric =
              MetricSpec.newBuilder().setMetricId("val_rmse").setGoal(GoalType.MINIMIZE).build();
    
          // decay
          [DoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpec.html) doubleValueSpec =
              [DoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpec.html).newBuilder().setMinValue(1e-07).setMaxValue(1).build();
          [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html) parameterDecaySpec =
              [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).newBuilder()
                  .setParameterId("decay")
                  .[setDoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setDoubleValueSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_DoubleValueSpec_)(doubleValueSpec)
                  .[setScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setScaleType_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ScaleType_)([ScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE)
                  .build();
          Double[] decayValues = {32.0, 64.0};
          [DiscreteValueCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition.html) discreteValueDecay =
              [DiscreteValueCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition.html).newBuilder().addAllValues(Arrays.asList(decayValues)).build();
          [ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html) conditionalParameterDecay =
              [ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html).newBuilder()
                  .[setParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_Builder_setParameterSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_)(parameterDecaySpec)
                  .[setParentDiscreteValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_Builder_setParentDiscreteValues_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_DiscreteValueCondition_)(discreteValueDecay)
                  .build();
    
          // learning rate
          [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html) parameterLearningSpec =
              [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).newBuilder()
                  .setParameterId("learning_rate")
                  .[setDoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setDoubleValueSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_DoubleValueSpec_)(doubleValueSpec) // Use the same min/max as for decay
                  .[setScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setScaleType_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ScaleType_)([ScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE)
                  .build();
    
          Double[] learningRateValues = {4.0, 8.0, 16.0};
          [DiscreteValueCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition.html) discreteValueLearning =
              [DiscreteValueCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.DiscreteValueCondition.html).newBuilder()
                  .addAllValues(Arrays.asList(learningRateValues))
                  .build();
          [ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html) conditionalParameterLearning =
              [ConditionalParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.html).newBuilder()
                  .[setParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_Builder_setParameterSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_)(parameterLearningSpec)
                  .[setParentDiscreteValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ConditionalParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_Builder_setParentDiscreteValues_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_DiscreteValueCondition_)(discreteValueLearning)
                  .build();
    
          // batch size
          Double[] batchSizeValues = {4.0, 8.0, 16.0, 32.0, 64.0, 128.0};
    
          [DiscreteValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DiscreteValueSpec.html) discreteValueSpec =
              [DiscreteValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DiscreteValueSpec.html).newBuilder().addAllValues(Arrays.asList(batchSizeValues)).build();
          [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html) parameter =
              [ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).newBuilder()
                  .setParameterId("batch_size")
                  .[setDiscreteValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setDiscreteValueSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_DiscreteValueSpec_)(discreteValueSpec)
                  .[setScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setScaleType_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ScaleType_)([ScaleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE)
                  .[addConditionalParameterSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_addConditionalParameterSpecs_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_)(conditionalParameterDecay)
                  .[addConditionalParameterSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_addConditionalParameterSpecs_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_ConditionalParameterSpec_)(conditionalParameterLearning)
                  .build();
    
          // trial_job_spec
          [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html) machineSpec =
              [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html).newBuilder()
                  .[setMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setMachineType_java_lang_String_)("n1-standard-4")
                  .[setAcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setAcceleratorType_com_google_cloud_aiplatform_v1_AcceleratorType_)([AcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AcceleratorType.html).NVIDIA_TESLA_T4)
                  .[setAcceleratorCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setAcceleratorCount_int_)(1)
                  .build();
    
          [PythonPackageSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.html) pythonPackageSpec =
              [PythonPackageSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.html).newBuilder()
                  .[setExecutorImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.Builder.html#com_google_cloud_aiplatform_v1_PythonPackageSpec_Builder_setExecutorImageUri_java_lang_String_)(executorImageUri)
                  .[addPackageUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.Builder.html#com_google_cloud_aiplatform_v1_PythonPackageSpec_Builder_addPackageUris_java_lang_String_)(packageUri)
                  .[setPythonModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PythonPackageSpec.Builder.html#com_google_cloud_aiplatform_v1_PythonPackageSpec_Builder_setPythonModule_java_lang_String_)(pythonModule)
                  .build();
    
          [WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html) workerPoolSpec =
              [WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html).newBuilder()
                  .setMachineSpec(machineSpec)
                  .setReplicaCount(1)
                  .[setPythonPackageSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.Builder.html#com_google_cloud_aiplatform_v1_WorkerPoolSpec_Builder_setPythonPackageSpec_com_google_cloud_aiplatform_v1_PythonPackageSpec_)(pythonPackageSpec)
                  .build();
    
          [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html) studySpec =
              [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).newBuilder()
                  .addMetrics(metric)
                  .addParameters(parameter)
                  .[setAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_Builder_setAlgorithm_com_google_cloud_aiplatform_v1_StudySpec_Algorithm_)([StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).Algorithm.RANDOM_SEARCH)
                  .build();
          [CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html) trialJobSpec =
              [CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html).newBuilder().[addWorkerPoolSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.Builder.html#com_google_cloud_aiplatform_v1_CustomJobSpec_Builder_addWorkerPoolSpecs_com_google_cloud_aiplatform_v1_WorkerPoolSpec_)(workerPoolSpec).build();
          // hyperparameter_tuning_job
          [HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html) hyperparameterTuningJob =
              [HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html).newBuilder()
                  .setDisplayName(displayName)
                  .setMaxTrialCount(4)
                  .[setParallelTrialCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.Builder.html#com_google_cloud_aiplatform_v1_HyperparameterTuningJob_Builder_setParallelTrialCount_int_)(2)
                  .setStudySpec(studySpec)
                  .[setTrialJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.Builder.html#com_google_cloud_aiplatform_v1_HyperparameterTuningJob_Builder_setTrialJobSpec_com_google_cloud_aiplatform_v1_CustomJobSpec_)(trialJobSpec)
                  .build();
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html) response =
              client.createHyperparameterTuningJob(parent, hyperparameterTuningJob);
          System.out.format("response: %s\n", response);
          System.out.format("Name: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html#com_google_cloud_aiplatform_v1_HyperparameterTuningJob_getName__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def create_hyperparameter_tuning_job_python_package_sample(
        project: str,
        display_name: str,
        executor_image_uri: str,
        package_uri: str,
        python_module: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
    
        # study_spec
        metric = {
            "metric_id": "val_rmse",
            "goal": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).MetricSpec.GoalType.MINIMIZE,
        }
    
        conditional_parameter_decay = {
            "parameter_spec": {
                "parameter_id": "decay",
                "double_value_spec": {"min_value": 1e-07, "max_value": 1},
                "scale_type": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.html).[ScaleType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE,
            },
            "parent_discrete_values": {"values": [32, 64]},
        }
        conditional_parameter_learning_rate = {
            "parameter_spec": {
                "parameter_id": "learning_rate",
                "double_value_spec": {"min_value": 1e-07, "max_value": 1},
                "scale_type": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.html).[ScaleType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE,
            },
            "parent_discrete_values": {"values": [4, 8, 16]},
        }
        parameter = {
            "parameter_id": "batch_size",
            "discrete_value_spec": {"values": [4, 8, 16, 32, 64, 128]},
            "scale_type": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.html).[ScaleType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.ParameterSpec.ScaleType.html).UNIT_LINEAR_SCALE,
            "conditional_parameter_specs": [
                conditional_parameter_decay,
                conditional_parameter_learning_rate,
            ],
        }
    
        # trial_job_spec
        machine_spec = {
            "machine_type": "n1-standard-4",
            "accelerator_type": aiplatform.gapic.[AcceleratorType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.AcceleratorType.html).NVIDIA_TESLA_K80,
            "accelerator_count": 1,
        }
        worker_pool_spec = {
            "machine_spec": machine_spec,
            "replica_count": 1,
            "python_package_spec": {
                "executor_image_uri": executor_image_uri,
                "package_uris": [package_uri],
                "python_module": python_module,
                "args": [],
            },
        }
    
        # hyperparameter_tuning_job
        hyperparameter_tuning_job = {
            "display_name": display_name,
            "max_trial_count": 4,
            "parallel_trial_count": 2,
            "study_spec": {
                "metrics": [metric],
                "parameters": [parameter],
                "algorithm": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).[Algorithm](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.Algorithm.html).RANDOM_SEARCH,
            },
            "trial_job_spec": {"worker_pool_specs": [worker_pool_spec]},
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_hyperparameter_tuning_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1_services_job_service_JobServiceClient_create_hyperparameter_tuning_job)(
            parent=parent, hyperparameter_tuning_job=hyperparameter_tuning_job
        )
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
