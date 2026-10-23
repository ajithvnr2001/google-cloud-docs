---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dataset-set-iam-policy/
title: Set IAM policy \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:48.563743+00:00
---

# Set IAM policy  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dataset-set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Set IAM policy Stay organized with collections  Save and categorize content based on your preferences. 

Set the access control policy for a dataset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Controlling access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // setDatasetIAMPolicy sets an IAM policy for the dataset.
    func setDatasetIAMPolicy(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	policy, err := datasetsService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &healthcare.Binding{
    		Members: []string{"user:example@example.com"},
    		Role:    "roles/viewer",
    	})
    
    	req := &healthcare.SetIamPolicyRequest{
    		Policy: policy,
    	}
    
    	policy, err = datasetsService.SetIamPolicy(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v", policy.Etag)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Binding;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.api.services.healthcare.v1.model.SetIamPolicyRequest;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class DatasetSetIamPolicy {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetSetIamPolicy(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the IAMPolicy to apply to the dataset.
        // For more information on understanding IAM roles, see the following:
        // https://cloud.google.com/iam/docs/understanding-roles
        Binding binding =
            new Binding()
                .setRole("roles/healthcare.datasetViewer")
                .setMembers(Arrays.asList("domain:google.com"));
        Policy policy = new Policy().setBindings(Arrays.asList(binding));
        SetIamPolicyRequest policyRequest = new SetIamPolicyRequest().setPolicy(policy);
    
        // Create request and configure any parameters.
        Datasets.SetIamPolicy request =
            client.projects().locations().datasets().setIamPolicy(datasetName, policyRequest);
    
        // Execute the request and process the results.
        Policy updatedPolicy = request.execute();
        System.out.println("Dataset policy has been updated: " + updatedPolicy.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const setDatasetIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.datasetViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: member,
                role: role,
              },
            ],
          },
        },
      };
    
      const dataset =
        await healthcare.projects.locations.datasets.setIamPolicy(request);
      console.log(
        'Set dataset IAM policy:',
        JSON.stringify(dataset.data, null, 2)
      );
    };
    
    setDatasetIamPolicy();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Dict and Any types for runtime type hints.
    from typing import Any, Dict
    
    def set_dataset_iam_policy(
        project_id: str,
        location: str,
        dataset_id: str,
        member: str,
        role: str,
        etag: str = None,
    ) -> Dict[str, Any]:
        """Sets the IAM policy for the specified dataset.
    
            A single member will be assigned a single role. A member can be any of:
    
            - allUsers, that is, anyone
            - allAuthenticatedUsers, anyone authenticated with a Google account
            - user:email, as in 'user:somebody@example.com'
            - group:email, as in 'group:admins@example.com'
            - domain:domainname, as in 'domain:example.com'
            - serviceAccount:email,
                as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
    
            A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
            or 'roles/editor'
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#setIamPolicy
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The ID of the dataset containing the IAM policy to set.
          member: The principals to grant access for a Google Cloud resource.
          role: The role to assign to the list of 'members'.
          etag: The 'etag' returned in a previous getIamPolicy request to ensure that
            setIamPolicy changes apply to the same policy version.
    
        Returns:
          A dictionary representing an IAM policy.
        """
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports HttpError from the Google Python API client errors module.
        from googleapiclient.errors import HttpError
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-dataset'
        dataset_name = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # role = 'roles/viewer'
        # member = 'serviceAccount:group@example.com'
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .setIamPolicy(resource=dataset_name, body={"policy": policy})
        )
        try:
            response = request.execute()
            print("etag: {}".format(response.get("name")))
            print("bindings: {}".format(response.get("bindings")))
            return response
        except HttpError as err:
            raise err
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
