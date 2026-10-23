---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-create-observation/
title: Create Observation \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:44.775512+00:00
---

# Create Observation  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-create-observation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Create Observation Stay organized with collections  Save and categorize content based on your preferences. 

Create a FHIR Observation resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    def create_observation(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        patient_id: str,
        encounter_id: str,
    ) -> Dict[str, Any]:
        """Creates a new Observation resource in a FHIR store that references an Encounter and Patient resource.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#create
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          patient_id: The "logical id" of the referenced Patient resource. The ID is
            assigned by the server.
          encounter_id: The "logical id" of the referenced Encounter resource. The ID
            is assigned by the server.
    
        Returns:
          A dict representing the created Observation resource.
        """
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
    
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-dataset'
        # fhir_store_id = 'my-fhir-store'
        # patient_id = 'b682d-0e-4843-a4a9-78c9ac64'  # replace with the associated Patient resource's ID
        # encounter_id = 'a7602f-ffba-470a-a5c1-103f993c6  # replace with the associated Encounter resource's ID
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_observation_path = (
            f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/Observation"
        )
    
        observation_body = {
            "resourceType": "Observation",
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8867-4",
                        "display": "Heart rate",
                    }
                ]
            },
            "status": "final",
            "subject": {"reference": f"Patient/{patient_id}"},
            "effectiveDateTime": "2019-01-01T00:00:00+00:00",
            "valueQuantity": {"value": 80, "unit": "bpm"},
            "context": {"reference": f"Encounter/{encounter_id}"},
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .create(
                parent=fhir_observation_path,
                type="Observation",
                body=observation_body,
            )
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
        print(f"Created Observation resource with ID {response['id']}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
