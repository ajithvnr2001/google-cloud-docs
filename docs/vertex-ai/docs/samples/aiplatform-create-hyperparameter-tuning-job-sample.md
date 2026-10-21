---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-hyperparameter-tuning-job-sample/
title: Create a hyperparameter tuning job \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:27.292521+00:00
---

# Create a hyperparameter tuning job  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-hyperparameter-tuning-job-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a hyperparameter tuning job Stay organized with collections  Save and categorize content based on your preferences. 

Creates a hyperparameter tuning job using the create_hyperparameter_tuning_job method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[AcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AcceleratorType.html);
    import com.google.cloud.aiplatform.v1.[ContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html);
    import com.google.cloud.aiplatform.v1.[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html);
    import com.google.cloud.aiplatform.v1.[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html);
    import com.google.cloud.aiplatform.v1.[WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html);
    import java.io.IOException;
    
    public class CreateHyperparameterTuningJobSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String displayName = "DISPLAY_NAME";
        String containerImageUri = "CONTAINER_IMAGE_URI";
        createHyperparameterTuningJobSample(project, displayName, containerImageUri);
      }
    
      static void createHyperparameterTuningJobSample(
          String project, String displayName, String containerImageUri) throws IOException {
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).MetricSpec metric0 =
              [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).MetricSpec.newBuilder()
                  .setMetricId("accuracy")
                  .setGoal([StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).MetricSpec.GoalType.MAXIMIZE)
                  .build();
          [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html).[DoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.DoubleValueSpec.html) doubleValueSpec =
              [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).ParameterSpec.DoubleValueSpec.newBuilder()
                  .setMinValue(0.001)
                  .setMaxValue(0.1)
                  .build();
          [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).[ParameterSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.html) parameter0 =
              [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).ParameterSpec.newBuilder()
                  // Learning rate.
                  .setParameterId("lr")
                  .[setDoubleValueSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.ParameterSpec.Builder.html#com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_Builder_setDoubleValueSpec_com_google_cloud_aiplatform_v1_StudySpec_ParameterSpec_DoubleValueSpec_)(doubleValueSpec)
                  .build();
          [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html) studySpec =
              [StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec.html).newBuilder().addMetrics(metric0).addParameters(parameter0).build();
          [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html) machineSpec =
              [MachineSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.html).newBuilder()
                  .[setMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setMachineType_java_lang_String_)("n1-standard-4")
                  .[setAcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setAcceleratorType_com_google_cloud_aiplatform_v1_AcceleratorType_)([AcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AcceleratorType.html).NVIDIA_TESLA_T4)
                  .[setAcceleratorCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MachineSpec.Builder.html#com_google_cloud_aiplatform_v1_MachineSpec_Builder_setAcceleratorCount_int_)(1)
                  .build();
          [ContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ContainerSpec.html) containerSpec =
              [ContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ContainerSpec.html).newBuilder().setImageUri(containerImageUri).build();
          [WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html) workerPoolSpec0 =
              [WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec.html).newBuilder()
                  .setMachineSpec(machineSpec)
                  .setReplicaCount(1)
                  .setContainerSpec(containerSpec)
                  .build();
          [CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html) trialJobSpec =
              [CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.html).newBuilder().[addWorkerPoolSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec.Builder.html#com_google_cloud_aiplatform_v1_CustomJobSpec_Builder_addWorkerPoolSpecs_com_google_cloud_aiplatform_v1_WorkerPoolSpec_)(workerPoolSpec0).build();
          [HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html) hyperparameterTuningJob =
              [HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.html).newBuilder()
                  .setDisplayName(displayName)
                  .setMaxTrialCount(2)
                  .[setParallelTrialCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob.Builder.html#com_google_cloud_aiplatform_v1_HyperparameterTuningJob_Builder_setParallelTrialCount_int_)(1)
                  .setMaxFailedTrialCount(1)
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
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * (Not necessary if passing values as arguments)
     */
    /*
    const displayName = 'YOUR HYPERPARAMETER TUNING JOB;
    const containerImageUri = 'TUNING JOB CONTAINER URI;
    const project = 'YOUR PROJECT ID';
    const location = 'us-central1';
      */
    // Imports the Google Cloud Pipeline Service Client library
    const {JobServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const jobServiceClient = new [JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function createHyperParameterTuningJob() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      // Create the hyperparameter tuning job configuration
      const hyperparameterTuningJob = {
        displayName,
        maxTrialCount: 2,
        parallelTrialCount: 1,
        maxFailedTrialCount: 1,
        studySpec: {
          metrics: [
            {
              metricId: 'accuracy',
              goal: 'MAXIMIZE',
            },
          ],
          parameters: [
            {
              parameterId: 'lr',
              doubleValueSpec: {
                minValue: 0.001,
                maxValue: 0.1,
              },
            },
          ],
        },
        trialJobSpec: {
          workerPoolSpecs: [
            {
              machineSpec: {
                machineType: 'n1-standard-4',
                acceleratorType: 'NVIDIA_TESLA_T4',
                acceleratorCount: 1,
              },
              replicaCount: 1,
              containerSpec: {
                imageUri: containerImageUri,
                command: [],
                args: [],
              },
            },
          ],
        },
      };
    
      const [response] = await jobServiceClient.createHyperparameterTuningJob({
        parent,
        hyperparameterTuningJob,
      });
    
      console.log('Create hyperparameter tuning job response:');
      console.log(`\tDisplay name: ${response.displayName}`);
      console.log(`\tTuning job resource name: ${response.name}`);
      console.log(`\tJob status: ${response.state}`);
    }
    
    createHyperParameterTuningJob();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def create_hyperparameter_tuning_job_sample(
        project: str,
        display_name: str,
        container_image_uri: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
        hyperparameter_tuning_job = {
            "display_name": display_name,
            "max_trial_count": 2,
            "parallel_trial_count": 1,
            "max_failed_trial_count": 1,
            "study_spec": {
                "metrics": [
                    {
                        "metric_id": "accuracy",
                        "goal": aiplatform.gapic.[StudySpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.StudySpec.html).MetricSpec.GoalType.MAXIMIZE,
                    }
                ],
                "parameters": [
                    {
                        # Learning rate.
                        "parameter_id": "lr",
                        "double_value_spec": {"min_value": 0.001, "max_value": 0.1},
                    },
                ],
            },
            "trial_job_spec": {
                "worker_pool_specs": [
                    {
                        "machine_spec": {
                            "machine_type": "n1-standard-4",
                            "accelerator_type": aiplatform.gapic.[AcceleratorType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.AcceleratorType.html).NVIDIA_TESLA_K80,
                            "accelerator_count": 1,
                        },
                        "replica_count": 1,
                        "container_spec": {
                            "image_uri": container_image_uri,
                            "command": [],
                            "args": [],
                        },
                    }
                ]
            },
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
