---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-get/
title: Get a data policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:55.148948+00:00
---

# Get a data policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a data policy Stay organized with collections  Save and categorize content based on your preferences. 

Gets a specific data policy from the BigQuery Data Policy API by its name.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Mask column data](https://docs.cloud.google.com/bigquery/docs/column-data-masking)
  * [Restrict access with column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security)



## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {DataPolicyServiceClient} =
      require('[@google-cloud/bigquery-datapolicies](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)').v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)();
    
    /**
     * Gets a specific data policy from the BigQuery Data Policy API by its name.
     *
     * This sample demonstrates how to fetch the details of an existing data policy.
     * Data policies are used to define rules for data masking or row-level security
     * on BigQuery tables.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id')
     * @param {string} [location='us'] The Google Cloud location of the data policy (For example, 'us', 'europe-west2').
     * @param {string} [dataPolicyId='example-data-policy'] The ID of the data policy to retrieve.
     */
    async function getDataPolicy(
      projectId,
      location = 'us',
      dataPolicyId = 'example-data-policy',
    ) {
      const name = client.dataPolicyPath(projectId, location, dataPolicyId);
    
      const request = {
        name,
      };
    
      try {
        const [dataPolicy] = await client.getDataPolicy(request);
        console.log('Successfully retrieved data policy:');
        console.log(`  Name: ${dataPolicy.name}`);
        console.log(`  Type: ${dataPolicy.dataPolicyType}`);
        if (dataPolicy.dataMaskingPolicy) {
          console.log(
            `  Data Masking Policy: ${dataPolicy.dataMaskingPolicy.predefinedExpression || dataPolicy.dataMaskingPolicy.routine}`,
          );
        }
        if (dataPolicy.grantees && dataPolicy.grantees.length > 0) {
          console.log(`  Grantees: ${dataPolicy.grantees.join(', ')}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: Data policy '${dataPolicyId}' not found in location '${location}' for project '${projectId}'.`,
          );
          console.error(
            'Make sure the data policy ID, project ID, and location are correct.',
          );
        } else {
          console.error('Error retrieving data policy:', err.message);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import bigquery_datapolicies_v2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def get_data_policy(
        project_id: str,
        location: str,
        data_policy_id: str,
    ) -> None:
        """Gets a specific data policy from the BigQuery Data Policy API by its name.
    
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the data policy (for example, "us", "eu").
            data_policy_id: The user-assigned ID of the data policy.
        """
        client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
        data_policy_name = client.[data_policy_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)(
            project=project_id,
            location=location,
            data_policy=data_policy_id,
        )
    
        try:
            response = client.[get_data_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_data_policy)(name=data_policy_name)
    
            print(f"Successfully retrieved data policy: {response.name}")
            print(f"  Data Policy ID: {response.data_policy_id}")
            print(f"  Data Policy Type: {response.data_policy_type.name}")
            if response.policy_tag:
                print(f"  Policy Tag: {response.policy_tag}")
            if response.grantees:
                print(f"  Grantees: {', '.join(response.grantees)}")
            if response.data_masking_policy:
                masking_policy = response.data_masking_policy
                if masking_policy.predefined_expression:
                    print(
                        f"  Data Masking Predefined Expression: {masking_policy.predefined_expression.name}"
                    )
                elif masking_policy.routine:
                    print(f"  Data Masking Routine: {masking_policy.routine}")
    
        except exceptions.NotFound:
            print(f"Error: Data policy '{data_policy_name}' not found.")
            print("Make sure the data policy ID, project ID, and location are correct.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
