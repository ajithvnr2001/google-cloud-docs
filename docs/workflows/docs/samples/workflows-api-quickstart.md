---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-api-quickstart/
title: Use client libraries to execute a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:02.600310+00:00
---

# Use client libraries to execute a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-api-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use client libraries to execute a workflow Stay organized with collections  Save and categorize content based on your preferences. 

Use client libraries to execute a workflow. Polls the workflow's execution using exponential backoff until the execution terminates and then prints the results.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Execute a workflow using the Cloud Client Libraries](https://docs.cloud.google.com/workflows/docs/execute-workflow-client-libraries)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/overview). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    
    import com.google.cloud.workflows.executions.v1.[CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.CreateExecutionRequest.html);
    import com.google.cloud.workflows.executions.v1.[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html);
    import com.google.cloud.workflows.executions.v1.[ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.ExecutionsClient.html);
    import com.google.cloud.workflows.executions.v1.[WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.WorkflowName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class WorkflowsQuickstart {
    
      private static final String PROJECT = System.getenv("GOOGLE_CLOUD_PROJECT");
      private static final String LOCATION = System.getenv().getOrDefault("LOCATION", "us-central1");
      private static final String WORKFLOW =
          System.getenv().getOrDefault("WORKFLOW", "myFirstWorkflow");
    
      public static void main(String... args)
          throws IOException, InterruptedException, ExecutionException {
        if (PROJECT == null) {
          throw new IllegalArgumentException(
              "Environment variable 'GOOGLE_CLOUD_PROJECT' is required to run this quickstart.");
        }
        workflowsQuickstart(PROJECT, LOCATION, WORKFLOW);
      }
    
      private static volatile boolean finished;
    
      public static void workflowsQuickstart(String projectId, String location, String workflow)
          throws IOException, InterruptedException, ExecutionException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created once, and can be reused for multiple requests. After completing all of your
        // requests, call the "close" method on the client to safely clean up any remaining background
        // resources.
        try ([ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.ExecutionsClient.html) executionsClient = [ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.ExecutionsClient.html).create()) {
          // Construct the fully qualified location path.
          [WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.WorkflowName.html) parent = [WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.WorkflowName.html).of(projectId, location, workflow);
    
          // Creates the execution object.
          [CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.CreateExecutionRequest.html) request =
              [CreateExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.CreateExecutionRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.WorkflowName.html#com_google_cloud_workflows_executions_v1_WorkflowName_toString__)())
                  .setExecution([Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html).newBuilder().build())
                  .build();
          [Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html) response = executionsClient.createExecution(request);
    
          String executionName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html#com_google_cloud_workflows_executions_v1_Execution_getName__)();
          System.out.printf("Created execution: %s%n", executionName);
    
          long backoffTime = 0;
          long backoffDelay = 1_000; // Start wait with delay of 1,000 ms
          final long backoffTimeout = 10 * 60 * 1_000; // Time out at 10 minutes
          System.out.println("Poll for results...");
    
          // Wait for execution to finish, then print results.
          while (!finished && backoffTime < backoffTimeout) {
            [Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html) execution = executionsClient.getExecution(executionName);
            finished = execution.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html#com_google_cloud_workflows_executions_v1_Execution_getState__)() != [Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html).State.ACTIVE;
    
            // If we haven't seen the results yet, wait.
            if (!finished) {
              System.out.println("- Waiting for results");
              Thread.sleep(backoffDelay);
              backoffTime += backoffDelay;
              backoffDelay *= 2; // Double the delay to provide exponential backoff.
            } else {
              System.out.println("Execution finished with state: " + execution.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html#com_google_cloud_workflows_executions_v1_Execution_getState__)().name());
              System.out.println("Execution results: " + execution.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflow-executions/latest/com.google.cloud.workflows.executions.v1.Execution.html#com_google_cloud_workflows_executions_v1_Execution_getResult__)());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {ExecutionsClient} = require('@google-cloud/workflows');
    const client = new ExecutionsClient();
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const location = 'us-central1';
    // const workflow = 'myFirstWorkflow';
    // const searchTerm = '';
    
    /**
     * Executes a Workflow and waits for the results with exponential backoff.
     * @param {string} projectId The Google Cloud Project containing the workflow
     * @param {string} location The workflow location
     * @param {string} workflow The workflow name
     * @param {string} searchTerm Optional search term to pass to the Workflow as a runtime argument
     */
    async function executeWorkflow(projectId, location, workflow, searchTerm) {
      /**
       * Sleeps the process N number of milliseconds.
       * @param {Number} ms The number of milliseconds to sleep.
       */
      function sleep(ms) {
        return new Promise(resolve => {
          setTimeout(resolve, ms);
        });
      }
      const runtimeArgs = searchTerm ? {searchTerm: searchTerm} : {};
      // Execute workflow
      try {
        const createExecutionRes = await client.createExecution({
          parent: client.workflowPath(projectId, location, workflow),
          execution: {
            // Runtime arguments can be passed as a JSON string
            argument: JSON.stringify(runtimeArgs),
          },
        });
        const executionName = createExecutionRes[0].name;
        console.log(`Created execution: ${executionName}`);
    
        // Wait for execution to finish, then print results.
        let executionFinished = false;
        let backoffDelay = 1000; // Start wait with delay of 1,000 ms
        console.log('Poll every second for result...');
        while (!executionFinished) {
          const [execution] = await client.getExecution({
            name: executionName,
          });
          executionFinished = execution.state !== 'ACTIVE';
    
          // If we haven't seen the result yet, wait a second.
          if (!executionFinished) {
            console.log('- Waiting for results...');
            await sleep(backoffDelay);
            backoffDelay *= 2; // Double the delay to provide exponential backoff.
          } else {
            console.log(`Execution finished with state: ${execution.state}`);
            console.log(execution.result);
            return execution.result;
          }
        }
      } catch (e) {
        console.error(`Error executing workflow: ${e}`);
      }
    }
    
    executeWorkflow(projectId, location, workflowName, searchTerm).catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {ExecutionsClient} from '@google-cloud/workflows';
    const client: ExecutionsClient = new ExecutionsClient();
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const location = 'us-central1';
    // const workflow = 'myFirstWorkflow';
    // const searchTerm = '';
    
    /**
     * Executes a Workflow and waits for the results with exponential backoff.
     * @param {string} projectId The Google Cloud Project containing the workflow
     * @param {string} location The workflow location
     * @param {string} workflow The workflow name
     * @param {string} searchTerm Optional search term to pass to the Workflow as a runtime argument
     */
    async function executeWorkflow(
      projectId: string,
      location: string,
      workflow: string,
      searchTerm: string
    ) {
      /**
       * Sleeps the process N number of milliseconds.
       * @param {Number} ms The number of milliseconds to sleep.
       */
      function sleep(ms: number): Promise<unknown> {
        return new Promise(resolve => {
          setTimeout(resolve, ms);
        });
      }
      const runtimeArgs = searchTerm ? {searchTerm: searchTerm} : {};
      // Execute workflow
      try {
        const createExecutionRes = await client.createExecution({
          parent: client.workflowPath(projectId, location, workflow),
          execution: {
            // Runtime arguments can be passed as a JSON string
            argument: JSON.stringify(runtimeArgs),
          },
        });
        const executionName = createExecutionRes[0].name;
        console.log(`Created execution: ${executionName}`);
    
        // Wait for execution to finish, then print results.
        let executionFinished = false;
        let backoffDelay = 1000; // Start wait with delay of 1,000 ms
        console.log('Poll every second for result...');
        while (!executionFinished) {
          const [execution] = await client.getExecution({
            name: executionName,
          });
          executionFinished = execution.state !== 'ACTIVE';
    
          // If we haven't seen the result yet, wait a second.
          if (!executionFinished) {
            console.log('- Waiting for results...');
            await sleep(backoffDelay);
            backoffDelay *= 2; // Double the delay to provide exponential backoff.
          } else {
            console.log(`Execution finished with state: ${execution.state}`);
            console.log(execution.result);
            return execution.result;
          }
        }
      } catch (e) {
        console.error(`Error executing workflow: ${e}`);
      }
    }
    
    executeWorkflow(projectId, location, workflowName, searchTerm).catch(
      (err: Error) => {
        console.error(err.message);
        process.exitCode = 1;
      }
    );

### Python

Before trying this sample, follow the Python setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.cloud import [workflows](https://docs.cloud.google.com/python/docs/reference/workflows/latest)_v1
    from google.cloud.workflows import executions_v1
    
    from google.cloud.workflows.executions_v1.types import executions
    
    # TODO(developer): Update and uncomment the following lines.
    # project_id = "MY_PROJECT_ID"
    # location = "MY_LOCATION"  # For example: us-central1
    # workflow_id = "MY_WORKFLOW_ID"  # For example: myFirstWorkflow
    
    # Initialize API clients.
    execution_client = executions_v1.ExecutionsClient()
    workflows_client = workflows_v1.[WorkflowsClient](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html)()
    
    # Construct the fully qualified location path.
    parent = workflows_client.[workflow_path](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html#google_cloud_workflows_v1_services_workflows_WorkflowsClient_workflow_path)(project_id, location, workflow_id)
    
    # Execute the workflow.
    response = execution_client.[create_execution](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.ExecutionsClient.html#google_cloud_workflows_executions_v1_services_executions_ExecutionsClient_create_execution)(request={"parent": parent})
    print(f"Created execution: {response.name}")
    
    # Wait for execution to finish, then print results.
    execution_finished = False
    backoff_delay = 1  # Start wait with delay of 1 second.
    print("Poll for result...")
    
    while not execution_finished:
        execution = execution_client.[get_execution](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.ExecutionsClient.html#google_cloud_workflows_executions_v1_services_executions_ExecutionsClient_get_execution)(
            request={"name": response.name}
        )
        execution_finished = execution.state != executions.Execution.State.ACTIVE
    
        # If we haven't seen the result yet, keep waiting.
        if not execution_finished:
            print("- Waiting for results...")
            time.sleep(backoff_delay)
            # Double the delay to provide exponential backoff.
            backoff_delay *= 2
        else:
            print(f"Execution finished with state: {execution.state.name}")
            print(f"Execution results: {execution.result}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
