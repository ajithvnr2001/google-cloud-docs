---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-conditional-patch-resource/
title: Conditional patch resource \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:25:56.340378+00:00
---

# Conditional patch resource  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-conditional-patch-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Conditional patch resource Stay organized with collections  Save and categorize content based on your preferences. 

Update parts of a resource if the resource exists based on meeting the search criteria specified by using query parameters.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
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
    
    // ConditionalPatchFHIRResource conditionally patches an FHIR resource.
    func ConditionalPatchFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType string, active bool) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// fhirStoreID := "my-fhir-store"
    	// resourceType := "Patient"
    	// active := true
    
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	payload := []map[string]interface{}{
    		{
    			"op":    "replace",
    			"path":  "/active",
    			"value": active,
    		},
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	call := fhirService.ConditionalPatch(parent, resourceType, bytes.NewReader(jsonPayload))
    
    	call.Header().Set("Content-Type", "application/json-patch+json")
    
    	// Refine your search by appending tags to the request in the form of query
    	// parameters. This searches for resources updated in the last 48 hours.
    	twoDaysAgo := time.Now().Add(-48 * time.Hour).Format("2006-01-02")
    	lastUpdated := queryParamOpt{key: "_lastUpdated", value: "gt" + twoDaysAgo}
    
    	resp, err := call.Do(lastUpdated)
    	if err != nil {
    		return fmt.Errorf("ConditionalPatch: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("ConditionalPatch: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	fmt.Fprintf(w, "%s", respBytes)
    
    	return nil
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def conditional_patch_resource(
        service_account_json, base_url, project_id, cloud_region, dataset_id, fhir_store_id
    ):
        """
        If a resource is found based on the search criteria specified in
        the query parameters, updates part of that resource by
        applying the operations specified in a JSON Patch document.
        """
        url = f"{base_url}/projects/{project_id}/locations/{cloud_region}"
    
        # The search query in this request updates all Observations
        # if the subject of the Observation is a particular patient.
        resource_path = "{}/datasets/{}/fhirStores/{}/fhir/Observation".format(
            url, dataset_id, fhir_store_id
        )
    
        # Make an authenticated API request
        session = get_session(service_account_json)
    
        headers = {"Content-Type": "application/json-patch+json"}
    
        body = json.dumps(
            [
                {
                    "op": "replace",
                    "path": "/valueQuantity/value",
                    # Sets the BPM for all matching Observations to 80. This
                    # is the portion of the request being patched.
                    "value": 80,
                }
            ]
        )
    
        # The search query is passed in as a query string parameter.
        params = {"identifier": "my-code-system|ABC-12345"}
    
        response = session.patch(resource_path, headers=headers, params=params, data=body)
        response.raise_for_status()
    
        print(response.url)
    
        resource = response.json()
    
        print(
            "Conditionally patched all Observations with the "
            "identifier 'my-code-system|ABC-12345' to use a BPM of 80."
        )
        print(json.dumps(resource, indent=2))
    
        return resource
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
