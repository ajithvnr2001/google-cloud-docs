---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-conditional-delete-resource/
title: Conditional delete resource \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:35.348767+00:00
---

# Conditional delete resource  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-conditional-delete-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Conditional delete resource Stay organized with collections  Save and categorize content based on your preferences. 

Delete FHIR resources that match a search query.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	healthcare "google.golang.org/api/healthcare/v1beta1"
    )
    
    // queryParamOpt is a googleapi.Option (https://godoc.org/google.golang.org/api/googleapi#CallOption)
    // that adds query parameters to an API call.
    type queryParamOpt struct {
    	key, value string
    }
    
    func (qp queryParamOpt) Get() (string, string) { return qp.key, qp.value }
    
    // ConditionalDeleteFHIRResource conditionally deletes an FHIR resource.
    func ConditionalDeleteFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// fhirStoreID := "my-fhir-store"
    	// resourceType := "Patient"
    
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	call := fhirService.ConditionalDelete(parent, resourceType)
    
    	// Refine your search by appending tags to the request in the form of query
    	// parameters. This searches for resources updated in the last 48 hours.
    	twoDaysAgo := time.Now().Add(-48 * time.Hour).Format("2006-01-02")
    	lastUpdated := queryParamOpt{key: "_lastUpdated", value: "gt" + twoDaysAgo}
    
    	if _, err := call.Do(lastUpdated); err != nil {
    		return fmt.Errorf("ConditionalDelete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted %q", parent)
    
    	return nil
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def conditional_delete_resource(
        service_account_json, base_url, project_id, cloud_region, dataset_id, fhir_store_id
    ):
        """Deletes FHIR resources that match a search query."""
        url = f"{base_url}/projects/{project_id}/locations/{cloud_region}"
    
        # The search query in this request deletes all Observations
        # with a status of 'cancelled'.
        resource_path = "{}/datasets/{}/fhirStores/{}/fhir/Observation".format(
            url, dataset_id, fhir_store_id
        )
        # The search query is passed in as a query string parameter.
        params = {"status": "cancelled"}
    
        # Make an authenticated API request
        session = get_session(service_account_json)
    
        response = session.delete(resource_path, params=params)
        print(response.url)
        if response.status_code != 404:  # Don't consider missing to be error
            response.raise_for_status()
    
        print("Conditionally deleted all Observations with status='cancelled'.")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
