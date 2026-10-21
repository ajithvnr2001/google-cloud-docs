---
url: https://docs.cloud.google.com/workflows/docs/best-practice/
title: Best practices for Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:14.586190+00:00
---

# Best practices for Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/best-practice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Best practices for Workflows Stay organized with collections  Save and categorize content based on your preferences. 

Workflows lets you coordinate and automate services across Google Cloud. Applying recommended architectural practices helps you improve reliability, optimize execution costs, and build resilient, maintainable orchestrations.

This is not an exhaustive list of recommendations and doesn't teach you the basics of how to use Workflows. This document assumes that you already have a general understanding of the overall Google Cloud landscape and of Workflows. For more information, see the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) and the [Workflows overview](https://docs.cloud.google.com/workflows/docs/overview).

## Select an optimal communication pattern

When designing a microservices architecture for deploying multiple services, you can select from the following communication patterns:

  * Direct service-to-service communication

  * Indirect event-driven communication (also known as _choreography_)

  * Automated configuration, coordination, and management (also known as _orchestration_)




Make sure to consider the benefits and drawbacks of each of the preceding options and select an optimal pattern for your use case. For example, direct service-to-service communication might be simpler to implement than other options but it tightly couples your services. In contrast, an [event-driven architecture](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures) lets you loosely couple your services; however, monitoring and debugging might be more complicated. Finally, a central orchestrator like Workflows, while less flexible, lets you coordinate the communication between services without the tight coupling of direct service-to-service communication, or the intricacy of choreographed events.

You can also combine communication patterns. For example, in event-driven orchestration, closely-related services are managed in an orchestration that is [triggered by an event](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc). Similarly, you might design a system where one orchestration results in [a Pub/Sub message](https://docs.cloud.google.com/workflows/docs/publish-pubsub-message) to another orchestrated system.

## General tips

Once you've decided to use Workflows as your service orchestrator, keep in mind the following helpful tips.

### Avoid hardcoding URLs

You can support workflows that are portable across multiple environments and easier to maintain by avoiding hardcoded URLs. You can achieve this in the following ways:

  * Define URLs as [runtime arguments](https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args).

This can be helpful when your workflow is invoked through a client library or the API. (However, this won't work if your workflow is triggered by [an event from Eventarc](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc) and the only argument that can be passed is the event payload.)

#### Example
        
        main:
          params: [args]
          steps:
            - init:
                assign:
                  - url1: ${args.urls.url1}
                  - url2: ${args.urls.url2}

When you run the workflow, you can specify the URLs. For example:
        
        gcloud workflows run multi-env --data='{"urls":{"url1": "URL_ONE", "url2": "URL_TWO"}}'

  * [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables) and create a workflow that is dynamically configured depending on the environment to which it is deployed. Or, create a workflow that can be reused as a template and configured according to separately maintained environment variables.

  * Use a substitution technique that lets you create a single workflow definition file, but deploy variants by using a tool that replaces placeholders in your workflow. For example, you can [use Cloud Build](https://docs.cloud.google.com/workflows/docs/deploy-workflows-using-cloud-build) to deploy a workflow and in the Cloud Build configuration file, add a step to replace placeholder URLs in the workflow.

#### Example
        
        steps:
        ‐ id: 'replace-urls'
          name: 'gcr.io/cloud-builders/gcloud'
          entrypoint: bash
          args:
            - -c
            - |
              sed -i -e "s~REPLACE_url1~$_URL1~" workflow.yaml
              sed -i -e "s~REPLACE_url2~$_URL2~" workflow.yaml
        ‐ id: 'deploy-workflow'
          name: 'gcr.io/cloud-builders/gcloud'
          args: ['workflows', 'deploy', 'multi-env-$_ENV', '--source', 'workflow.yaml']

You can then [ substitute variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) at build time. For example:
        
        gcloud builds submit --config cloudbuild.yaml \
            --substitutions=_ENV=staging,_URL1="URL_ONE",_URL2="URL_TWO"

For more information, see [Submit a build via CLI and API](https://docs.cloud.google.com/build/docs/running-builds/submit-build-via-cli-api).

Or, you can [use Terraform](https://docs.cloud.google.com/workflows/docs/create-workflow-terraform) to provision your infrastructure and define a configuration file that creates workflows for each environment by using [input variables](https://developer.hashicorp.com/terraform/language/values/variables).

#### Example
        
        variable "project_id" {
          type = string
        }
        
        variable "url1" {
          type = string
        }
        
        variable "url2" {
          type = string
        }
        
        locals {
          env = ["staging", "prod"]
        }
        
        # Define and deploy staging and production workflows
        resource "google_workflows_workflow" "multi-env-workflows" {
          for_each = toset(local.env)
        
          name            = "multi-env-${each.key}"
          project         = var.project_id
          region          = "us-central1"
          source_contents = templatefile("${path.module}/workflow.yaml", { url1 : "${var.url1}-${each.key}", url2 : "${var.url2}-${each.key}" })
        }

When variables are declared in the root module of your configuration, they can be [assigned values](https://developer.hashicorp.com/terraform/language/values/variables#assigning-values-to-root-module-variables) in a number of ways. For example
        
        terraform apply -var="project_id=PROJECT_ID" -var="url1=URL_ONE" -var="url2=URL_TWO"

  * [Use the Secret Manager connector](https://docs.cloud.google.com/workflows/docs/use-secret-manager) to securely store URLs in Secret Manager and retrieve them.




### Use nested steps

Every workflow must have at least one [step](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps). By default, Workflows treats steps as if they are in an ordered list and executes them one at a time until all the steps have run. Logically, some steps should be grouped together and you can use a `steps` block to nest a series of steps. This is convenient as it lets you point to the correct atomic step to process a set of steps.

#### Example
    
    
    main:
        params: [input]
        steps:
        - callWikipedia:
            steps:
            - checkSearchTermInInput:
                switch:
                    - condition: ${"searchTerm" in input}
                      assign:
                        - searchTerm: ${input.searchTerm}
                      next: readWikipedia
            - getCurrentDate:
                call: http.get
                args:
                    url: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam
                result: currentDate
            - setFromCallResult:
                assign:
                    - searchTerm: ${currentDate.body.dayOfWeek}
            - readWikipedia:
                call: http.get
                args:
                    url: https://en.wikipedia.org/w/api.php
                    query:
                        action: opensearch
                        search: ${searchTerm}
                result: wikiResult
        - returnOutput:
                return: ${wikiResult.body[1]}

### Wrap expressions

All [expressions](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions) must begin with a `$` and be enclosed in curly brackets:
    
    
    ${EXPRESSION}

To avoid YAML parsing issues, you can wrap expressions in quotes. For example, [expressions containing colons](https://docs.cloud.google.com/workflows/docs/troubleshooting#expressions-colons) can cause unexpected behaviour when the colon is interpreted as defining a map. You can resolve this issue by wrapping the YAML expression in single quotes:

`'${"Name: " + myVar}'`

You can also use expressions that span several lines. For example, you might need to wrap a SQL query in quotes when using the Workflows BigQuery connector.

#### Example
    
    
    - runQuery:
        call: googleapis.bigquery.v2.jobs.query
        args:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            body:
                useLegacySql: false
                useQueryCache: false
                timeoutMs: 30000
                # Find top 100 titles with most views on Wikipedia
                query: ${
                    "SELECT TITLE, SUM(views)
                    FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                    WHERE LENGTH(TITLE) > 10
                    GROUP BY TITLE
                    ORDER BY SUM(VIEWS) DESC
                    LIMIT 100"
                    }
        result: queryResult

For the entire workflow definition, see [Run multiple BigQuery jobs in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs).

### Use declarative calls

Use Workflows to call services from the workflow itself and handle the results, and to execute simple tasks like [making an HTTP call](https://docs.cloud.google.com/workflows/docs/http-requests). Workflows can invoke services, parse responses, and [construct inputs for other connected services](https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service). Calling a service lets you avoid the complications of extra invocations, additional dependencies, and services calling services. Consider replacing services that are free of business logic with declarative API calls and use Workflows to abstract away complexity.

However, you should create services to do any work that is too complex for Workflows; for example, implementing reusable business logic, complex computations, or transformations that are not supported by [Workflows expressions and its standard library](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview). A complicated case is typically easier to implement in code, instead of using YAML or JSON and the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax).

### Store only what you need

Keep memory consumption under control so that you don't encounter [resource limits](https://docs.cloud.google.com/workflows/quotas#resource_limits) or an error that indicates this such as `ResourceLimitError`, `MemoryLimitExceededError`, or `ResultSizeLimitExceededError`.

Be selective about what you store in [variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables), filtering for and storing only what you need. If a service returns a payload that is too large, use a separate function to make the call for you and return only what is required.

You can free memory by clearing variables. For example, you might want to free up memory that is needed for subsequent steps. Or, you might have calls with results you don't care about, and you can omit those results altogether.

You can clear a variable by assigning `null`. In YAML, you can also assign an empty value or `~` to a variable. This identifies memory that can be safely reclaimed.

#### Example
    
    
      - step:
          assign:
            - bigVar:

### Use subworkflows and external workflows

You can use [subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows) to define a piece of logic or a set of steps that you want to call multiple times, simplifying the workflow definition. Subworkflows are similar to a function or routine in a programming language. They can accept parameters and return values, allowing you to create more complex workflows with a broader range of applications.

Note that subworkflows are local to your workflow definition and can't be reused in other workflows. However, you can [call workflows from other workflows](https://docs.cloud.google.com/workflows/docs/tutorials/execute-workflows-from-workflow). The Workflows connectors can help you with this. For more information, see the connector overviews for the [Workflow Executions API](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/Overview) and the [Workflows API](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflows/Overview).

## Use Workflows connectors

Workflows provides a number of _connectors_ that make it easier to access other Google Cloud products within a workflow. Connectors simplify calling services because they handle the formatting of requests for you, providing methods and arguments so that you don't need to know the details of a Google Cloud API. Connectors also have built-in behavior for handling [retries](https://docs.cloud.google.com/workflows/docs/connectors#retries) and [long-running operations](https://docs.cloud.google.com/workflows/docs/connectors#lro) so that you can avoid iterating and waiting for calls to complete; connectors take care of this for you.

If you need to call a Google Cloud API, first check to see if a Workflows connector for it exists. And if you don't see a connector for a Google Cloud product, you can [request it](https://docs.google.com/forms/d/e/1FAIpQLScdDRwFHcFuy28hvjGq0XCBMyiVuhHGq2c-7Gy_no1ZuqKAOg/viewform?resourcekey=0-0BRW58uzC8wnVntuOiM7AQ).

[Learn how to use a connector](https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service) and, for a detailed reference of available connectors, see the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

## Run workflow steps in parallel

While Workflows can run steps sequentially, you can also run independent steps in parallel. In some cases, this can significantly speed up your workflow execution. For more information, see [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps).

## Apply retries and the saga pattern

Design workflows that are resilient and can handle both transient and permanent service failures. Errors for Workflows might be raised, for example, by failed HTTP requests, functions, connectors, or generated by your own workflow code. Add error handling and retries so that a failure in one step doesn't cause the entire workflow to fail.

  * You can [raise custom errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors) using the `raise` syntax.
  * You can [catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors) using a `try/except` block.
  * You can [retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) using a `try/retry` block and define the maximum number of retry attempts.



Some business transactions span multiple services so you need a mechanism to implement transactions that span services. The saga design pattern is a way to manage data consistency across microservices in distributed transaction scenarios. A saga is a sequence of transactions that publishes an event for every transaction and which triggers the next transaction. If a transaction fails, the saga executes compensating transactions that counteract the preceding failures in the sequence. Try out the [Retries and Saga Pattern in Workflows tutorial](https://github.com/GoogleCloudPlatform/workflows-demos/tree/master/retries-and-saga) on GitHub.

## Use callbacks to wait

[Callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) allow workflow executions to wait for another service to make a request to the _callback endpoint_ ; that request resumes the execution of the workflow.

With callbacks, you can signal to your workflow that a specified event has occurred, and wait on that event without [polling](https://docs.cloud.google.com/workflows/docs/sleeping). For example, you can create a workflow that notifies you when a product is back in stock or when an item has shipped; or that [waits to allow human interaction](https://docs.cloud.google.com/workflows/docs/tutorials/callbacks-firestore) such as reviewing an order or validating a translation. You can also [wait for events using callbacks and Eventarc triggers](https://docs.cloud.google.com/workflows/docs/tutorials/create-wait-for-events-callbacks).

## Orchestrate long-running jobs

If you need to execute long-running [batch processing](https://en.wikipedia.org/wiki/Batch_processing) workloads, you can use [Batch](https://docs.cloud.google.com/batch) or [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs), and you can use Workflows to manage the services. This lets you combine advantages and efficiently provision and orchestrate the entire process.

Batch is a fully managed service that lets you schedule, queue, and execute batch workloads on Compute Engine virtual machine (VM) instances. You can use the [Workflows connector for Batch](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview) to schedule and run a Batch job. For details, try out [the tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/batch-and-workflows).

Cloud Run jobs are used to run code that performs work (a job) and quits when the work is done. Workflows lets you execute Cloud Run jobs as part of a workflow to perform more complex data processing or orchestrate a system of existing jobs. Try out [the tutorial](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs) which demonstrates how to use Workflows to execute a Cloud Run job.

## Containerize long-running tasks

You can automate the execution of a long-running container using Workflows and Compute Engine. For example, you can containerize a long-running task so that it can run anywhere, and then run the container on a Compute Engine VM for the maximum duration of a workflow execution (one year).

Using Workflows, you can automate the creation of the VM, the running of the container on the VM, and the deletion of the VM. This lets you use a server and run a container, but it abstracts away the complexity of managing both, and can be helpful if you run into time limitations when using a service such as Cloud Run functions or Cloud Run. Try out the [Long running containers with Workflows and Compute Engine](https://github.com/GoogleCloudPlatform/workflows-demos/tree/master/long-running-container) tutorial on GitHub.

## Run command-line tools from Workflows

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) is a service that executes your builds on Google Cloud as a series of build steps, where each build step is run in a Docker container. Executing build steps is analogous to executing commands in a script.

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) includes the `gcloud`, `bq`, and `kubectl` command-line tools but there is no direct way to run gcloud CLI commands from Workflows. However, Cloud Build provides container images that include the gcloud CLI. You can run gcloud CLI commands in those containers from a Cloud Build step, and you can create that step in Workflows using the [Cloud Build connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/Overview).

#### Example

Run `gcloud` in a workflow:
    
    
    # This example shows how to execute gcloud commands from Workflows
    # using Cloud Build and returns the output
    
    main:
      steps:
      - execute_command:
          call: gcloud
          args:
              args: "workflows list"
          result: result
      - return_result:
          return: ${result}
    
    gcloud:
      params: [args]
      steps:
      - create_build:
          call: googleapis.cloudbuild.v1.projects.builds.create
          args:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            parent: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/locations/global"}
            body:
              serviceAccount: ${sys.get_env("GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME")}
              options:
                logging: CLOUD_LOGGING_ONLY
              steps:
              - name: gcr.io/google.com/cloudsdktool/cloud-sdk
                entrypoint: /bin/bash
                args: ${["-c", "gcloud " + args + " > $$BUILDER_OUTPUT/output"]}
          result: result_builds_create
      - return_build_result:
          return: ${text.split(text.decode(base64.decode(result_builds_create.metadata.build.results.buildStepOutputs[0])), "\n")}

Run `kubectl` in a workflow:
    
    
    # This example shows how to execute kubectl commands from Workflows
    # using Cloud Build and returns the output
    
    main:
      steps:
      - execute_command:
          call: kubectl
          args:
              args: "--help"
          result: result
      - return_result:
          return: ${result}
    
    kubectl:
      params: [args]
      steps:
      - create_build:
          call: googleapis.cloudbuild.v1.projects.builds.create
          args:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            parent: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/locations/global"}
            body:
              serviceAccount: ${sys.get_env("GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME")}
              options:
                logging: CLOUD_LOGGING_ONLY
              steps:
              - name: gcr.io/cloud-builders/kubectl
                entrypoint: /bin/bash
                args: ${["-c", "kubectl " + args + " > $$BUILDER_OUTPUT/output"]}
          result: result_builds_create
      - return_build_result:
          return: ${text.split(text.decode(base64.decode(result_builds_create.metadata.build.results.buildStepOutputs[0])), "\n")}

## Use Terraform to create your workflow

[Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview) is an infrastructure-as-code tool that lets you predictably create, change, and improve your cloud infrastructure by using code.

You can define and deploy a workflow using the Terraform [`google_workflows_workflow`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workflows_workflow) resource. For more information, see [Create a workflow by using Terraform](https://docs.cloud.google.com/workflows/docs/create-workflow-terraform).

To help you manage and maintain large workflows, you can create your workflow in a separate YAML file and import that file into Terraform using the [`templatefile` function](https://developer.hashicorp.com/terraform/language/functions/templatefile) which reads a file at a given path and renders its content as a template.

#### Example
    
    
      # Define a workflow
      resource "google_workflows_workflow" "workflows_example" {
        name            = "sample-workflow"
        region          = var.region
        description     = "A sample workflow"
        service_account = google_service_account.workflows_service_account.id
        # Import main workflow YAML file
        source_contents = templatefile("${path.module}/workflow.yaml",{})
      }

Similarly, if you have a main workflow calling multiple subworkflows, you can define the main workflow and the subworkflows in separate files, and use the `templatefile` function to import them.

#### Example
    
    
      # Define a workflow
      resource "google_workflows_workflow" "workflows_example" {
        name            = "sample-workflow"
        region          = var.region
        description     = "A sample workflow"
        service_account = google_service_account.workflows_service_account.id
        # Import main workflow and subworkflow YAML files
        source_contents = join("", [
          templatefile(
            "${path.module}/workflow.yaml",{}
          ),
    
          templatefile(
            "${path.module}/subworkflow.yaml",{}
          )])
      }

Note that if you're referring to line numbers when debugging a workflow, all the YAML files imported through the Terraform configuration file are merged and deployed as a single workflow.

## Deploy a workflow from a Git repository

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) uses [build triggers](https://docs.cloud.google.com/build/docs/triggers) to enable CI/CD automation. You can configure triggers to listen for incoming events, such as when a new commit is pushed to a repository or when a pull request is initiated, and then automatically execute a build when new events come in.

You can use a Cloud Build trigger to automatically start a build and deploy a workflow from a Git repository. You can configure the trigger to deploy your workflow on any change to the source repository, or deploy the workflow only when the change matches specific criteria.

This approach can help you manage your deployment lifecycle. For example, you can deploy changes to a workflow in a staging environment, run tests against that environment, and then incrementally launch these changes to the production environment. For more information, see [Deploy a workflow from a Git repository using Cloud Build](https://docs.cloud.google.com/workflows/docs/deploy-workflows-using-cloud-build).

## Optimize usage

The [cost to run a workflow](https://cloud.google.com/workflows/pricing) is minimal. However, for high volume usage, apply the following guidelines to optimize usage and decrease cost:

  * Instead of using custom domains, ensure that any calls to Google Cloud services use `*.appspot.com`, `*.cloud.goog`, `*.cloudfunctions.net`, or `*.run.app` so that you are billed for internal and not external steps.

  * Apply a [custom retry policy](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying#custom-retry) that balances your latency and reliability needs with costs. More frequent retries lower latency and increase reliability, but can also increase costs.

  * When using connectors that wait for long-running operations, set a [custom polling policy](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call) that optimizes latency for cost. For example, if you expect an operation to take over an hour, you might want a policy that initially polls after one minute in case of an immediate failure, and then every 15 minutes after that.

  * Combine [assignments](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step) into one step.

  * Avoid excessive use of `sys.log` steps. Consider using [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) instead.

  * Understand which operations are considered a step. Operations that don't count as steps on their own are counted when used within an applicable step. For example, the following counts as one step:
        
        - type_check:
            return: if(get_type((int("6"))) == integer, 1, 2)
        

Key operations that count and don't count toward the [maximum steps limit](https://docs.cloud.google.com/workflows/quotas#step_limits) are categorized in the following table:

Category | Operation  
---|---  
**Counts as a step** | 
    * Data operations: Assigning, returning values 
    * Controlling flow: Jumps (`next`), switches, starting a `for` loop, and each iteration of a `for` loop 
    * Calls: Invoking `sys.get_env` or other standard library function, another workflow, or a connector 
    * Concurrency: Spawning threads and parallel execution
    * Error handling: Each `raise`, `try`, `retry`, and `except` block counts as a separate step, even if other operations are part of the same larger step. For example, a step that includes a `try` block with a call operation counts as three steps: one for the primary step, one for the try, and one for the call. Adding a `retry` block adds three more steps (one each for the retry, try, and call), making a total of six steps.  
**Doesn't count as a step** | 
    * Reading and writing to [lists](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists), [maps](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps), and [variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables) Although an individual lookup doesn't add an extra step, a step that contains the lookup—for example, an [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step) step—counts as one step.
    * Specific [ built-in expression helper functions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview): `len()`, `int()`, and `get_type()`
    * [ Comparison and arithmetic operations](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes#order-operations)
    * [String concatenation](https://docs.cloud.google.com/workflows/docs/reference/syntax/strings)
    * [ Boolean operations](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes#logical-operators)  



## Summary of best practices

The following table summarizes the general tips and best practices recommended in this document.

General tips  
---  
  
  * Avoid hardcoding URLs
  * Use nested steps
  * Wrap expressions
  * Use declarative calls
  * Store only what you need
  * Use subworkflows and external workflows

  
Best practices  
  
  * Use Workflows connectors
  * Run workflow steps in parallel
  * Apply retries and the saga pattern
  * Use callbacks to wait
  * Orchestrate long-running jobs
  * Containerize long-running tasks
  * Run command-line tools from Workflows
  * Use Terraform to create your workflow
  * Deploy a workflow from a Git repository
  * Optimize usage

  
  
## What's next

  * [Security best practices](https://docs.cloud.google.com/workflows/docs/security-best-practices)
  * [Debugging overview](https://docs.cloud.google.com/workflows/docs/debug)
  * [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting)
  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
