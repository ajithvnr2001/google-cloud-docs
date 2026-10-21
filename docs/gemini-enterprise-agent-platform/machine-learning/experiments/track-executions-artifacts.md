---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/track-executions-artifacts/
title: Track executions and artifacts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:44.348855+00:00
---

# Track executions and artifacts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/track-executions-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Track executions and artifacts Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform Experiments supports tracking both executions and artifacts. Executions are steps in an ML workflow that include but aren't limited to data preprocessing, training, and model evaluation. Executions can consume artifacts such as datasets and produce artifacts such as models.

### Create artifact

The following sample uses the `[create](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform#google_cloud_aiplatform_Artifact_create)` method of the Artifact Class. 

### Python
    
    
    from typing import Dict, Optional
    
    from google.cloud import aiplatform
    
    
    def create_artifact_sample(
        schema_title: str,
        project: str,
        location: str,
        uri: Optional[str] = None,
        resource_id: Optional[str] = None,
        display_name: Optional[str] = None,
        schema_version: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict] = None,
    ):
        artifact = aiplatform.Artifact.create(
            schema_title=schema_title,
            uri=uri,
            resource_id=resource_id,
            display_name=display_name,
            schema_version=schema_version,
            description=description,
            metadata=metadata,
            project=project,
            location=location,
        )
        return artifact
    

  * `schema_title`: Required. Identifies the schema title used by the resource.
  * `project`: . You can find these IDs in the Google Cloud console [welcome](https://console.cloud.google.com/welcome) page.
  * `location`: See [List of available locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations).
  * `uri`: Optional. URI of artifact's location.
  * `resource_id`: Optional. The `resource_id` portion of the Artifact name with the format. This is globally unique in a metadataStore:  
`projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id>`. 
  * `display_name`: Optional. The user-defined name of the resource.
  * `schema_version`: Optional. Specifies the version used by the resource. If not set, defaults to use the latest version.
  * `description`: Optional. Describes the purpose of the resource to be created.
  * `metadata`: Optional. Contains the metadata information that will be stored in the resource. 



### Start execution

The following sample uses the `[start_execution](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform#google_cloud_aiplatform_start_execution)` method.

### Python
    
    
    from typing import Any, Dict, List, Optional
    
    from google.cloud import aiplatform
    
    
    def start_execution_sample(
        schema_title: str,
        display_name: str,
        input_artifacts: List[aiplatform.Artifact],
        output_artifacts: List[aiplatform.Artifact],
        project: str,
        location: str,
        resource_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        schema_version: Optional[str] = None,
        resume: bool = False,
    ):
        aiplatform.init(project=project, location=location)
    
        with aiplatform.start_execution(
            schema_title=schema_title,
            display_name=display_name,
            resource_id=resource_id,
            metadata=metadata,
            schema_version=schema_version,
            resume=resume,
        ) as execution:
            execution.assign_input_artifacts(input_artifacts)
            execution.assign_output_artifacts(output_artifacts)
            return execution
    
    

  * `schema_title`: Identifies the schema title used by the resource.
  * `display_name`: The user-defined name of the resource.
  * `input_artifacts`: Artifacts to assign as input.
  * ` output_artifacts`: Artifacts as outputs to this Execution.
  * `project`: Your project ID. You can find these in the Google Cloud console [welcome](https://console.cloud.google.com/welcome) page.
  * `location`: See [List of available locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations).
  * `resource_id`: Optional. The `resource_id` portion of the Artifact name with the format. This is globally unique in a metadataStore: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id>.
  * `schema_version`: Optional. Specifies the version used by the resource. If not set, defaults to use the latest version.
  * `metadata`: Optional. Contains the metadata information that will be stored in the resource.
  * `resume`: bool. 

Note: When the optional `resume` parameter is specified as `TRUE`, the previously started run resumes. When not specified, `resume` defaults to `FALSE` and a new run is created. 




### Notebook samples

  * [Compare models trained and evaluated locally](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-compare-models)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
