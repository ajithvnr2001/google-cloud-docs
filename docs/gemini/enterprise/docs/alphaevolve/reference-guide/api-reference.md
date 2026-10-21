---
url: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/reference-guide/api-reference/
title: AlphaEvolve API reference \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T21:27:14.526521+00:00
---

# AlphaEvolve API reference  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/reference-guide/api-reference/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ AlphaEvolve ](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview)



Send feedback 

#  AlphaEvolve API reference Stay organized with collections  Save and categorize content based on your preferences. 

This document serves as the authoritative, production-grade API reference and system specification for the AlphaEvolve Cloud API under the Google Cloud Discovery Engine conversational layers. It defines the precise nested resource hierarchies, REST and gRPC endpoints, field-level constraints, lifecycle state machines, error diagnostic matrixes, security sandboxing rules, and integration workflows necessary to engineer a fully automated client-side controller and evaluation loop.

## Unified lifecycle state machines

The AlphaEvolve agent coordinates two independent state machines to monitor experiment campaign progression and manage the delivery and execution of individual program mutations.

### Experiment lifecycle states

An experiment represents the overall optimization campaign. It is processed as a persistent server-side resource and transitions through the following states:

  * **`CREATED`:** The initialization state. The resource is declared and configured but has not yet populated initial generations or dispatched API calls.

  * **`RUNNING`:** The active evaluation state. The engine is concurrently sampling parent candidates, generating code mutations through the LLM mixture, and streaming tasks to evaluators.

  * **`PAUSED`:** A temporary holding state triggered manually or through an automated protective `idle_timeout`. Code generation stops, and existing workers pause metric delivery.

  * **`COMPLETED`:** A terminal state indicating that the search has successfully fulfilled its `max_programs` target allocation or reached its structural generation limit.

  * **`FAILED`:** A terminal error state indicating that systemic environment issues—such as uncaught API credential exceptions, data store corruption, or consecutive runner panics—halted processing execution.




### Program states

The runtime validation sequence is applied to individual candidate variants.

Every generated code mutation behaves as an isolated program entity that transitions through a sequence of granular operational states within the population database.

  1. **`INITIALIZED`:** The program entry is created in the database, tracking its ancestral pedigree and parent program linkages.

  2. **`GENERATING`:** A task is actively dispatched to the language model mixture backend to draft or mutate the specific functional code blocks.

  3. **`EVALUATING`:** The code payload is locked by an evaluation worker process and executed inside an isolated test harness environment.

  4. **`COMPLETED`:** The execution scores and descriptive structural insights are safely committed to the evolutionary database, and the program is added to the selection pool.




### Concurrency and locking mechanics

Programs are acquired by worker loops using an atomic lock token mechanism to prevent race conditions or duplicate scoring overhead across distributed topologies. The evaluator must submit the finalized scoring schema alongside the exact matching lock token to successfully commit results back to the database.

## Configuration and settings schemas

Overview of the core schema configurations, parameters, and defaults utilized by the AlphaEvolve engine runtime.

### `AlphaEvolveExperimentConfig`

Defines the core structural parameters and programmatic constraints of the evolutionary experiment run.

Field Name | Type | Default | Constraints / Value Bounds | Technical Description  
---|---|---|---|---  
`title` | string | _Required_ | Max 256 characters | Unique display name of the experiment.  
`problemDescription` | string | _Required_ | Max 5,000 characters | The formal specification of the problem. It is injected directly into prompt contexts to establish rules.  
`programLanguage` | string | _Required_ | Freeform value | Target language of the evolved codebase (for example, `"python"`, `"cpp"`, `"verilog"`, `"cuda"`, `"julia"`, `"java"`).  
`runSettings` | object | _Required_ | Maps to `RunSettings` schema | Pacing and timeout parameters.  
`generationSettings` | object | _Optional_ | Maps to `GenerationSettings` schema | Model selection and context parameters.  
`evolutionSettings` | object | _Optional_ | Maps to `EvolutionSettings` schema | Parent-selection and diversity parameters.  
  
### RunSettings

Governs throughput pacing, parallelization limits, and automatic system timeouts.

Field Name | Type | Default | Constraints / Value Bounds | Technical Description  
---|---|---|---|---  
`maxPrograms` | int32 | 100 | Min: 2, Max: 100000 | Total execution budget (programs to generate and evaluate). Must be greater than 1.  
`concurrency` | int32 | 1 | Min: 1, Max: 30 | Number of parallel program mutations active in the queue. Values >30 are not allowed.  
`maxDuration` | string | 24h (86400s) | ISO 8601 dayTimeDuration string  
Min: >0, Max: 7 Days | Total wall-clock time allowed before the experiment is stopped.  
`idleTimeout` | string | 5h (us/eu)  
2h (global) |  ISO 8601 dayTimeDuration string  
Min: >0  
Max: the location's default | Inactivity duration before automatic transition to `PAUSED`. Defaults to 2 hours in `global` and 5 hours in regional locations (`us`, `eu`). The duration is limited by the location's default, so specifying a value above the location default (for example, 12h in `global`) is ignored and the value is 2 hours (without error).  
  
## Generation settings

The `GenerationSettings` schema controls the prompt assembly, context windows, and model configurations for mutations:

  * **`context` (string):** Optional user-provided reference documentation, supplemental APIs, or rules. It is strictly recommended to stay under 200,000 tokens. Context sizes exceeding 200,000 tokens dilute the model's attention and degrade mutation quality.

  * **`includeFullProgramInPrompt` (bool):** Default `false`.

    * `true`: The mutation prompt includes the mutable `EVOLVE-BLOCK` and the surrounding immutable boilerplate (highly recommended for complex structural reasoning).

    * `false`: Only the mutable block is visible, saving token context.

  * **`models` (array of objects):** Optional. Each entry names a model and gives it an optional `weight`, which is that model's share of generation calls relative to the other entries. If you omit `models`, AlphaEvolve sets it to the default model when it creates the experiment. The default changes as newer Gemini models are released; Default model lists which model applies on which date. To choose the model yourself, or to keep the same model on every run, set `models`.

The following example sends about nine in ten generation calls to the first model and the rest to the second. Weights are ratios, so they don't have to add up to 1.
        
        "models": [
          {
            "name": "gemini-3.8-flash",
            "weight": 0.9
          },
          {
            "name": "gemini-3.1-pro-preview",
            "weight": 0.1
          }
        ]
        




### Supported models

Set `models[].name` to one of the following values. You can combine at most two models in a single experiment.

Model name | Serving regions  
---|---  
[`gemini-4-argon`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon) | `global`, `us`, `eu`  
[`gemini-3.8-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash) | `global`, `us`, `eu`  
[`gemini-3.7-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash) | `global`, `us`, `eu`  
[`gemini-3.5-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash) | `global`, `us`, `eu`  
[`gemini-3.1-pro-preview`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) | `global`  
  
AlphaEvolve validates `models` when it creates the experiment and returns `INVALID_ARGUMENT` for a model name that is not in this table or that is not available in the region you requested.

### Default model

The following table lists the model AlphaEvolve uses when you omit `models`, by experiment creation date.

Experiment created | Default model  
---|---  
On or after October 24, 2026 | `gemini-4-argon`  
September 29, 2026 through October 23, 2026 | `gemini-3.8-flash`  
June 30, 2026 through September 28, 2026 | `gemini-3.5-flash`  
Before June 30, 2026 | `gemini-2.5-flash`  
  
To identify the model assigned to an experiment, check `generationSettings.models` in the experiment configuration or the creation response. Because changes take effect throughout the transition day, experiments created on those dates may receive either the old or new default model. Experiments created without `models` before June 30, 2026 don't contain a value for this field.

Because the model is stored in each experiment, a change to the default doesn't affect experiments that already exist. To use a newer default model, create a new experiment.

## Evolution settings

The `EvolutionSettings` schema controls island-model reseeding and parent sampling probabilities:

  * **`parentSamplingConfig` → `paretoSamplingConfig` → `paretoSamplingProbability` (float):** The probability (0.0 to 1.0) of sampling parent programs directly from the active Pareto frontier rather than using standard fitness-based selection. This parameter must be set to `0.0` (disabled) if the optimized metrics return only a single scalar metric.



## Candidate program data models

This section outlines the data schemas and representations used to define and organize candidate code structures within the population database.

### AlphaEvolveProgramContent

Defines the files and structural makeup of the candidate program.

  * **`files` (array of `AlphaEvolveSourceFile`):** A list of all files comprising the candidate codebase. The payload must contain at least one source file. Google recommends keeping the total file count to 50 files per candidate program; this gives optimal model attention and context window efficiency.

  * **`description` (string):** An auto-generated summary outlining the programmatic changes suggested by the generation model (Max 1,000 characters).




### AlphaEvolveSourceFile

Represents an individual source code file in the codebase.

  * **`path` (string):** The workspace-relative path destination (Required, Max 256 characters). Each source file entry must specify a non-empty path. If configuring a Python workspace, the primary executable file entry point must be named exactly `"initial_program.py"`.

  * **`content` (string):** The raw source code string comprising the functional implementation blocks. Google recommends keeping the cumulative codebase size across all files to under 4,000 to 5,000 lines of code (LOC); this is optimal for model attention and mutation generation performance.

  * **`programLanguage` (string):** The language parser mapping tag. This string must explicitly match the language designated within the parent experiment configuration.

  * **`description` (string):** An optional summary outlining the file's individual architecture or purpose, which is exposed to the LLM during mutation passes (Max 500 characters).




### AlphaEvolveProgramEvaluation

The structured payload submitted by client runner instances back to the evolutionary database following runtime execution.

  * **`scores` (`AlphaEvolveScores`):** Standardized, objective numerical metric values. Best practices dictate restricting this to 3 to 5 distinct float metrics; excessive target dimensions degrade multi-objective Pareto comparator performance.

  * **`insights` (array of `AlphaEvolveEvaluationInsight`):** Diagnostic semantic labels and natural-language execution traces passed back to assist the LLM's subsequent mutation generation attempts (Recommended maximum of 10 items).




## Score formulation and ingestion formats

### The maximization rule

AlphaEvolve operates fundamentally as a monotonic hill-climbing algorithm and strictly maximizes all numerical metrics. If your evaluation pipeline tracks a minimization target (such as minimizing application latency in milliseconds or reducing memory usage), you must negate the value before submitting it back to the database: `submitted_score = -latency_ms`.

The scores should ideally be continuous. Boolean or highly discrete metrics don't provide a sufficient gradient signal for effective hill-climbing exploration.

### Single-objective ingestion schema

Use the following JSON when your evaluation harness optimizes against a single scalar objective function.
    
    
    {
      "scores": {
        "scores": [
          {
            "metric": "accuracy",
            "score": 0.95
          }
        ]
      },
      "insights": {
        "insights": [
          {
            "label": "validation",
            "text": "Passed syntax and basic compilation."
          }
        ]
      }
    }
    

### Multi-objective ingestion schema

Use the following JSON when passing independent multi-objective tracking parameters to activate server-side Pareto frontier optimization routines.
    
    
    {
      "scores": {
        "scores": [
          {
            "metric": "accuracy",
            "score": 0.95
          },
          {
            "metric": "latency",
            "score": -42.5
          }
        ]
      },
      "insights": {
        "insights": [
          {
            "label": "verification",
            "text": "Passed 5 out of 5 unit tests."
          },
          {
            "label": "latency_warning",
            "text": "Latency regression of 3% observed on large dataset."
          }
        ]
      }
    }
    

## Fetching and querying program data

The AlphaEvolve system logs the telemetry, execution metrics, and full source code of every generated mutation, allowing developers to query this historical datastore using the API or CLI to track optimization progress and extract the highest-performing code candidates.

### Program retrieval using REST API

Evaluated program resources can be queried from the database using the standard `ListAlphaEvolvePrograms` endpoint with filtering and sorting query parameters:

  * State filtering: Query programs matching a specific lifecycle state:
        
        GET /v1alpha/{parent}/alphaEvolvePrograms?state_filter=COMPLETED
        

  * Metric-based sorting: Retrieve sorted candidates based on optimized metrics:
        
        GET /v1alpha/{parent}/alphaEvolvePrograms?order_by=accuracy desc,latency&page_size=5
        


**Note:** If no explicit sort order is passed, the server applies an implicit tie-breaker of create_time descending.

### Program retrieval using CLI

To pull the top completed candidates directly from your terminal, run the following command:
    
    
    ae results best <experiment-nickname> --top 5
    

### Complete CLI usage examples

The AlphaEvolve CLI provides developers with quick administrative control and monitoring over campaigns directly from the shell:

  * List all experiments in a conversational session:
        
        ae experiment list
        

  * List all mutated candidate programs for a specific experiment:
        
        ae program list EXPERIMENT_NICKNAME \
          --state=COMPLETED \
          --order_by="accuracy desc"
        

Replace EXPERIMENT_NICKNAME with the name of your experiment.

  * Retrieve the top-performing completed code candidates:
        
        ae results best EXPERIMENT_NICKNAME --top 5
        

Replace EXPERIMENT_NICKNAME with the name of your experiment.

  * Resume a paused campaign:
        
        ae experiment resume EXPERIMENT_NICKNAME
        

Replace EXPERIMENT_NICKNAME with the name of your experiment.




## Core REST API endpoint directory

All endpoints are versioned under `v1alpha` of the Google Cloud Discovery Engine API.

### Parent resource path pattern

The true nested parent resource URI is structured as: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}`

  * AlphaEvolve is available in `global`, `us`, and `eu`. Creating experiments in other locations returns `FAILED_PRECONDITION`.
  * Assured Workloads projects are not supported.
  * A project is limited to 30 concurrently active (`STARTED` or `RUNNING`) AlphaEvolve experiments per location. Starting or resuming an experiment that exceeds this limit returns `RESOURCE_EXHAUSTED`.



### Create experiment (POST)

  * **Path:**
        
        POST v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*}/alphaEvolveExperiments
        

  * **Request body:** `AlphaEvolveExperimentConfig` (See Section 2.1)

  * **Response:** `AlphaEvolveExperiment` resource containing the initialized campaign.

  * **HTTP Status:** 200 OK




#### API payload examples

  1. Request body example (POST /alphaEvolveExperiments)
         
         {
           "config": {
             "title": "Sorting Optimization Campaign",
             "problemDescription": "Optimize the custom_heuristic function.",
             "programLanguage": "python",
             "runSettings": {
               "maxPrograms": 250,
               "concurrency": 8,
               "maxDuration": "86400s",
               "idleTimeout": "1800s"
             },
             "generationSettings": {
               "context": "Ensure custom_heuristic is in-place.",
               "includeFullProgramInPrompt": true,
               "models": [
                 {
                   "name": "gemini-3.8-flash",
                   "weight": 1.0
                 }
               ]
             },
             "evolutionSettings": {
               "parentSamplingConfig": {
                 "paretoSamplingConfig": {
                   "paretoSamplingProbability": 0.0
                 }
               }
             }
           }
         }
         

  2. Response body example (200 OK)
         
         {
           "name": "projects/.../sort-opt-01",
           "state": "CREATED",
           "createTime": "2026-06-23T13:30:00Z",
           "config": {
             "title": "Sorting Optimization Campaign",
             "problemDescription": "Optimize the custom_heuristic function.",
             "programLanguage": "python",
             "runSettings": {
               "maxPrograms": 250,
               "concurrency": 8,
               "maxDuration": "86400s",
               "idleTimeout": "1800s"
             },
             "generationSettings": {
               "context": "Ensure custom_heuristic is in-place.",
               "includeFullProgramInPrompt": true,
               "models": [
                 {
                   "name": "gemini-3.8-flash",
                   "weight": 1.0
                 }
               ]
             },
             "evolutionSettings": {
               "parentSamplingConfig": {
                 "paretoSamplingConfig": {
                   "paretoSamplingProbability": 0.0
                 }
               }
             }
           }
         }
         




### Start experiment (POST)

  * **Path:**
        
        POST v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}:start
        

  * **Request body:** `StartExperimentRequest`

  * **Deprecation warning:** The body field `initialProgram` is deprecated and ignored.

  * **Response:** `GoogleLongrunningOperation` (LRO).

  * **HTTP status:** 200 OK (Transitions state from `CREATED` to `RUNNING`)




#### API payload examples

  1. Request body example
         
         {
           "desiredProgramsCount": 1
         }
         

  2. Response body example (200 OK - long-running operation)
         
         {
           "name": "projects/.../operations/start-op-7788",
           "metadata": {
             "@type": "type.googleapis.com/.../AlphaEvolveStartExperimentMetadata",
             "createTime": "2026-06-23T13:31:00Z"
           },
           "done": false
         }
         




### Acquire programs (POST)

  * **Path:**
        
        POST v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}:acquirePrograms
        

  * **Request body:** `AcquireProgramsRequest`

    * `desiredProgramsCount` (`int32`): Optional batch count of mutated programs to retrieve (defaults to 1 when unset).
  * **Response statuses:**

    * `200 OK`: Returns response containing locked `AlphaEvolveProgram` resources.

    * `204 No Content`: The queue is empty or the campaign is paused. Runners must sleep (for example, 15 seconds) and retry.




#### API payload examples

  1. Request body example
         
         {
           "desiredProgramsCount": 1
         }
         

  2. Response body example (200 OK)
         
         {
           "programs": [
             {
               "name": "projects/.../alphaEvolvePrograms/prog-102",
               "lockToken": "token_uuid_8877_x99",
               "state": "EVALUATING",
               "createTime": "2026-06-23T13:32:00Z",
               "content": {
                 "description": "Mutated candidate program.",
                 "files": [
                   {
                     "path": "initial_program.py",
                     "programLanguage": "python",
                     "description": "Primary sorting executable.",
                     "content": "def custom_heuristic(arr, _):\n    ..."
                   }
                 ]
               }
             }
           ]
         }
         

  3. Response body example (204 No Content)




HTTP Status 204 returned with an empty payload context.

### Submit programs evaluations (POST)

  * **Path:**
        
        POST v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}:submitProgramsEvaluations
        

  * **Request body:** `SubmitProgramsEvaluationsRequest`

    * `evaluationSubmissions` (array): Contains matching `lockToken`, the qualified program resource path, and the evaluation payload (scores and insights). The API accepts **exactly one** evaluation submission per call. Batching multiple evaluations into a single request is rejected with `INVALID_ARGUMENT`. When evaluating multiple candidates, submit each program individually.
  * **Response:** `SubmitProgramsEvaluationsResponse` (empty).

  * **HTTP status:** 200 OK (Saves scores, releases active lock, and registers insights)




#### API payload examples

  1. Request body example
         
         {
           "evaluationSubmissions": [
             {
               "lockToken": "token_uuid_8877_x99",
               "program": "projects/.../alphaEvolvePrograms/prog-102",
               "evaluation": {
                 "scores": {
                   "scores": [
                     {
                       "metric": "latency_performance",
                       "score": evaluation_payload["score"]
                     }
                   ]
                 },
                 "insights": {
                   "insights": [
                     {
                       "label": "benchmark",
                       "text": "Completed test case in 12.45ms."
                     }
                   ]
                 }
               }
             }
           ]
         }
         

  2. Response body example (200 OK)
         
         {}
         




### Resume experiment (POST)

  * **Path:**
        
        POST v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}:resume
        

  * **Request body:** `ResumeExperimentRequest`

  * **Response:** `GoogleLongrunningOperation` (LRO).

  * **HTTP status:** 200 OK (Transitions state from `PAUSED` back to `RUNNING`)




#### API payload examples

  1. Request body example
         
         {}
         

  2. Response body example (200 OK - long-running operation)
         
         {
           "name": "projects/.../operations/resume-op-9900",
           "metadata": {
             "@type": "type.googleapis.com/.../AlphaEvolveResumeExperimentMetadata",
             "createTime": "2026-06-23T13:45:00Z"
           },
           "done": false
         }
         




### List programs (GET)

  * **Path:**
        
        GET v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}/alphaEvolvePrograms
        

  * **Query parameters:**

    * `stateFilter` (string): Optional. Standard list filter, for example, `stateFilter = 'COMPLETED'`.

    * `orderBy` (string): Optional. Metric-based sort, for example, `accuracy desc`.

  * **Response:** `ListAlphaEvolveProgramsResponse`.

  * **HTTP Status:** 200 OK




#### API payload examples

  1. Request query URL example
         
         GET v1alpha/projects/.../alphaEvolveExperiments/sort-opt-01/
           alphaEvolvePrograms?stateFilter=COMPLETED&orderBy=latency_performance%20desc
           &pageSize=1
         

  2. Response body example (200 OK)
         
         {
           "alphaEvolvePrograms": [
             {
               "name": "projects/.../alphaEvolvePrograms/prog-102",
               "state": "COMPLETED",
               "createTime": "2026-06-23T13:32:00Z",
               "evaluation": {
                 "scores": {
                   "scores": [
                     {
                       "metric": "latency_performance",
                       "score": -12.45
                     }
                   ]
                 },
                 "insights": {
                   "insights": [
                     {
                       "label": "benchmark",
                       "text": "Completed test case in 12.45ms."
                     }
                   ]
                 }
               }
             }
           ],
           "nextPageToken": "token_page_1_next"
         }
         




## Diagnostic code and troubleshooting reference

### API diagnostic code matrix

HTTP status | Error type | System cause | Workaround or mitigation action  
---|---|---|---  
**400** | `INVALID_ARGUMENT` | 

  * Malformed `EVOLVE-BLOCK-START` / `EVOLVE-BLOCK-END` markers (for example, content sharing the marker's line, nested blocks, or missing end marker).
  * Empty evolve block containing only comments or whitespace without editable code.
  * `maxPrograms` set to less than 2.
  * Unrecognized config fields.
  * Invalid model configuration (more than two models, duplicate entries, non-positive weights, or temperature outside `[0.0, 2.0]`).
  * Submitting multiple evaluations in a single `submitProgramsEvaluations` call.
  * Project is an Assured Workloads project.

|  Ensure markers are alone on their line and enclose at least one non-comment line of code. Set `maxPrograms` to 2 or more. Remove fields that are not part of the API, such as `notes` which was present in the preview version of the API. Submit evaluations individually, one at a time.   
**403** | `PERMISSION_DENIED` | 

  * The caller does not hold the Discovery Engine Editor role (`roles/discoveryengine.editor`) or Admin role (`roles/discoveryengine.admin`). Note: `roles/discoveryengine.user` does not grant AlphaEvolve permissions, and `roles/discoveryengine.viewer` cannot get experiments.
  * The caller lacks permission on the parent session resource.
  * No active Gemini Enterprise license is assigned.

|  Grant `roles/discoveryengine.editor` or `roles/discoveryengine.admin` at the project level and verify access to the parent session. Verify active Gemini Enterprise licenses. Configure application default credentials:  
  
`gcloud auth application-default login --project=PROJECT_ID`  
  
**Note:** Model Armor is not supported under AlphaEvolve configurations.   
**400** | `FAILED_PRECONDITION` | 

  * Stale or expired lock token, or program state mismatch (for example, candidate was re-acquired or finalized after lease lapsed).
  * Experiment created in an unsupported location (outside `global`, `us`, or `eu`).
  * The Vertex AI API (`aiplatform.googleapis.com`) is not enabled on the project.

|  Echo the exact `lockToken` returned by `:acquirePrograms`. Enforce client-side timeouts (recommended 30 minutes) and submit failure penalty scores upon timeout. Recreate experiment in a supported location. Enable the Vertex AI API: `gcloud services enable aiplatform.googleapis.com --project=PROJECT_ID`.   
**429** | `RESOURCE_EXHAUSTED` | 

  * Project has reached the limit of 30 concurrently active (`STARTED` / `RUNNING`) experiments per location.
  * Backend model generation token quota exhausted.

|  For active experiment limit: Complete or stop running experiments before starting a new one (lowering `concurrency` in `runSettings` does not affect this limit). For model token quota: Lower `concurrency` in `runSettings` and implement exponential backoff.   
**503** | `SERVICE_UNAVAILABLE` | Input safety classifier unavailable or backend service temporarily overloaded. | Implement a retry loop with randomized exponential backoff on the client side.  
  
### Common error messages and resolutions

The following reference lists common error messages returned by the API, their underlying causes, and resolution steps.

#### Initial program and EVOLVE-BLOCK parsing errors

Error message | System cause | Workaround or mitigation action  
---|---|---  
`Parsing error: Unexpected evolve block delimiters in line <line_number>. Cannot be in the same line.` | Both `EVOLVE-BLOCK-START` and `EVOLVE-BLOCK-END` markers appear on the same line. | Place start and end markers on separate lines.  
`Parsing error: Unexpected content on the same line as <marker> in line <line_number>.` | Code, text, or trailing characters share the line with an `EVOLVE-BLOCK-START` or `EVOLVE-BLOCK-END` marker. | Ensure the marker is alone on its line (preceded only by comment prefix, such as `# EVOLVE-BLOCK-START`).  
`Parsing error: Unexpected evolve block start delimiter in line <line_number>. Cannot nest evolve blocks.` | An `EVOLVE-BLOCK-START` marker appears inside an already opened evolve block. | Remove nested start markers; nested evolve blocks are not supported.  
`Parsing error: Unexpected evolve block end delimiter in line <line_number>. No block started.` | An `EVOLVE-BLOCK-END` marker appears without a preceding `EVOLVE-BLOCK-START`. | Ensure every end marker is preceded by a matching start marker.  
`Parsing error: Evolve block started but not ended.` | An `EVOLVE-BLOCK-START` marker was found without a matching closing `EVOLVE-BLOCK-END` marker. | Add a closing `EVOLVE-BLOCK-END` marker.  
  
#### Program content and structure errors

Error message | System cause | Workaround or mitigation action  
---|---|---  
`Program content must contain at least one source file.` | `program_content.source_files` is empty. | Provide at least one source file.  
`source_files entries must have a non-empty path.` | A source file entry has an empty `path` string. | Specify a valid relative path for every source file.  
`source_files entry has empty content; path: <path>` | A source file entry contains empty string content. | Populate the file content.  
`Program content must contain at least one EVOLVE-BLOCK-START / EVOLVE-BLOCK-END region with editable code between the markers (whitespace and comment-only regions don't count -- AlphaEvolve has nothing to mutate).` | Evolve blocks contain only comments, docstrings, or whitespace, with no editable code. | Include at least one line of editable code (such as function definitions or algorithm logic) inside the block.  
  
#### Configuration and model validation errors

Error message | System cause | Workaround or mitigation action  
---|---|---  
`unsupported model: <model_name>` | The requested model is not supported or not enabled for your project. | Use supported models. Refer to Generation settings.  
`model '<model_name>' is not served from domain shard '<location>'.` | The model is not available in the specified regional location. | Refer to Generation settings for supported models and locations.  
`generation_settings.models must contain at most 2 distinct models; got <count>.` | More than two model configurations were specified in `generation_settings.models`. | Specify at most two models in the mixture.  
`generation_settings.models contains duplicate entry: <model_name>` | The same model name appears more than once in `generation_settings.models`. | Remove duplicate model entries.  
`generation_settings.models weight for <model_name> must be finite and strictly positive; got <weight>. Remove the entry instead of setting weight to zero.` | Model sampling weight is negative, zero, or non-finite. | Set a positive weight or remove the entry.  
`generation_settings.models temperature for <model_name> must be in [0.0, 2.0]; got <temperature>.` | Model temperature is outside the valid range `[0.0, 2.0]`. | Adjust temperature to a value between `0.0` and `2.0`.  
`RunSettings.max_programs is required and must be greater than 1.` | `max_programs` was omitted or set to 1 or less. | Set `max_programs` to 2 or greater (a minimum of 2 is required to admit evolved candidates).  
`RunSettings.concurrency is required and must be positive.` | `concurrency` was omitted or set to 0 or less. | Set `concurrency` to a positive integer (typically 1–30).  
`EvolutionSettings.pareto_sampling_probability must be in [0, 1]; got <probability>.` | `pareto_sampling_probability` is outside `[0.0, 1.0]`. | Set a probability between `0.0` and `1.0`.  
  
#### Project prerequisites and experiment lifecycle errors

Error message | System cause | Workaround or mitigation action  
---|---|---  
`AlphaEvolve requires the Vertex AI API to be enabled in this project. Enable it with: gcloud services enable aiplatform.googleapis.com --project=<project_id>` | The Vertex AI API (`aiplatform.googleapis.com`) is not enabled on the Google Cloud project. | Run `gcloud services enable aiplatform.googleapis.com --project=PROJECT_ID`.  
`Project has reached the limit of 30 concurrently active AlphaEvolve experiments in location <location>. Stop or wait for a running experiment to finish before starting or resuming another.` | The project has reached the quota of 30 concurrently active (`STARTED` or `RUNNING`) experiments in that location. | Stop or complete existing experiments before starting or resuming a new experiment.  
`Cannot <action> experiment from state <current_state>` | Attempted an invalid state transition (for example, starting an already running experiment, or resuming a newly created experiment). | Ensure experiments follow standard lifecycle transitions: `CREATED` → `START`, `PAUSED`/`COMPLETED` → `RESUME`, `STARTED`/`RUNNING` → `STOP`.  
`Cannot resume experiment: a start or watchdog message is already pending. Stop the experiment first to drain it, or wait for the pending delivery to complete.` | A previous start or resume operation is still in flight. | Wait for pending delivery to complete, or call `STOP` to drain pending messages.  
`AlphaEvolve is not available for this project.` | The project is blocked or is an unsupported compliance profile. | Refer to [Compliance and security profile](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/compliance-security-profile).  
  
#### Program acquisition and evaluation errors

Error message | System cause | Workaround or mitigation action  
---|---|---  
`Exactly one evaluation submission is required.` | Multiple evaluation submissions were batched in a single `submitProgramsEvaluations` request. | Submit evaluations individually, one per API call.  
`Program is required for each evaluation submission.` / `submission.program is required.` | The `program` resource path was not provided in the evaluation submission. | Pass the full program resource path.  
`Lock token is required for each evaluation submission.` / `submission.lock_token is required.` | The `lock_token` returned during `acquirePrograms` was omitted. | Pass the exact `lock_token` string returned when the program was acquired.  
`Program <program_name> has unexpected lock token. Expected token: '<expected>', actual token: '<actual>'` | The lock token sent in the submission does not match the active server lease (for example, the lease expired and another worker acquired it, or an incorrect token was provided). | Echo the exact `lockToken` from `acquirePrograms` and submit results before client timeouts.  
`Program <program_name> is not in expected state. Expected state: EVALUATION_IN_PROGRESS, actual state: <actual_state>` | The program has already been evaluated, cancelled, or transitioned out of `EVALUATION_IN_PROGRESS`. | Discard the stale evaluation or re-acquire the candidate if available.  
`The request was rejected by a safety policy.` | The input problem description, initial code, or evaluation metrics triggered safety classification policies. | Sanitize prompt text and problem descriptions to remove sensitive keywords or traces.  
`The input safety classifier is currently unavailable.` | The safety classification service is temporarily unreachable or overloaded (fails closed). | Implement exponential backoff retry logic.  
  
### Remediating "silent drops"

A safety filter intercept (silent drop) occurs when server-side language models flag and drop mutated candidate prompts due to sensitive phrasing or safety rule triggers. The server silences the output, causing the queue to return empty responses, and client runners may wait indefinitely.

**Workaround remediation:**

  * **Sanitize context:** Remove emotionally charged or security-sensitive phrases from the `problemDescription`.

  * **Filter insights:** Parse and truncate raw exception traces or terminal stderr logs in the `insights` payload to prevent echoing unsafe system content that triggers downstream filters.

  * **Localize datasets:** Do not place training records or large text corpora within prompts; load them locally in the client environment during the evaluation loop execution.




## Client-side evaluation best practices

### The "spaghetti code" bottleneck

Suboptimal source formatting degrades optimization quality: _"Spaghetti code == Noisy search space"_. Before placing `EVOLVE-BLOCK` markers:

  * Refactor code blocks so that variables and function signatures are clearly named.

  * Add descriptive, concise docstrings explaining what each function or variable does and why. Ensure docstrings reside alongside actual functional code; placing _only_ a docstring or comments inside an `EVOLVE-BLOCK` is rejected as an empty block.

  * Ensure that `EVOLVE-BLOCK-START` and `EVOLVE-BLOCK-END` comment markers are placed alone on their respective lines, except for leading whitespace and comment prefixes (such as `#` or `//`).

  * Ensure that any external, immutable dependencies (like importing helper modules or loading static data) live outside the `EVOLVE-BLOCK`.




### Context window allocation

To maximize mutation creativity, limit the code payload sent to the API. The total program context should remain under 150,000 to 200,000 tokens. Large blocks of static, immutable boilerplate consume model attention and degrade performance. Move utility scripts, data ingestion pipelines, and heavy validation libraries entirely to the client-side evaluator.

### Prime the initial program first

Before running AlphaEvolve, use a standard coding agent to debug both your seed codebase and your evaluator:

  * **Prime the seed:** Fix obvious syntax bugs, compile issues, and edge-cases.

  * **Verify the starting score:** Verify that the baseline score is reasonable and that the evaluator is fully deterministic (same code + same input = same score).

  * **Test with invalid inputs:** Run the evaluator with intentionally broken functions to confirm it catches compiler issues, handles infinite loops gracefully, and returns high negative penalty scores.




### Avoid over-optimized baselines

Don't pass an already highly optimized baseline program as a seed. If your initial program is already near-optimal, AlphaEvolve will have difficulty hill-climbing because there is very little room to improve. Start with a reasonable but not maximally optimized baseline. This gives AlphaEvolve space to explore and hill-climb.

## Client-side runner safeguards

Client-side evaluators must enforce strict safeguards to prevent malicious, resource-intensive, or irresponsive candidates from stalling parallel workers:

  * **Strict timeouts:** Enforce a strict execution cutoff of 30 minutes (or less depending on the search space structure).

  * **Timeout penalty submission:** If a candidate program variant exceeds the timeout limit, terminate its execution thread immediately. Don't allow the candidate process to fail. Instead, instantly compile and submit a severe failure penalty score (for example, `-100000.0`) along with a descriptive debug insight back to the server to release the program's queue lock.

  * **AST security filters:** Always run an Abstract Syntax Tree (AST) inspection check on the incoming source code payload before compilation. Immediately abort execution and apply a severe failure penalty if restricted reflection or execution primitives (such as `eval`, `exec`, `getattr`, or `setattr`) are detected.




## Further resources

For more information, see the following resources:

  * [AlphaEvolve on Google Cloud GitHub repository](https://github.com/Google-Cloud-AI/alphaevolve-on-googlecloud)
  * [AlphaEvolve REST API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest#rest-resource:-v1alpha.projects.locations.collections.engines.sessions.alphaevolveexperiments)
  * [AlphaEvolve RPC API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc#google.cloud.discoveryengine.v1alpha.alphaevolveservice)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
