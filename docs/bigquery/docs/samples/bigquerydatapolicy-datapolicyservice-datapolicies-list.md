---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicies-list/
title: List data policies \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:58.692944+00:00
---

# List data policies  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicies-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List data policies Stay organized with collections  Save and categorize content based on your preferences. 

Lists all data policies in a specified project.

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
     * Lists all data policies in a given project and location.
     *
     * Data policies define rules for data masking, row-level security, or column-level security.
     *
     * @param {string} projectId The Google Cloud project ID. (for example, 'example-project-id')
     * @param {string} location The Google Cloud location of the data policies. (For example, 'us')
     */
    async function listDataPolicies(projectId, location) {
      const parent = `projects/${projectId}/locations/${location}`;
    
      const request = {
        parent,
      };
    
      try {
        console.log(
          `Listing data policies for project: ${projectId} in location: ${location}`,
        );
        const [dataPolicies] = await client.listDataPolicies(request);
    
        if (dataPolicies.length === 0) {
          console.log(
            `No data policies found in location ${location} for project ${projectId}.`,
          );
          return;
        }
    
        console.log('Data Policies:');
        for (const dataPolicy of dataPolicies) {
          console.log(`  Data Policy Name: ${dataPolicy.name}`);
          console.log(`    ID: ${dataPolicy.dataPolicyId}`);
          console.log(`    Type: ${dataPolicy.dataPolicyType}`);
          if (dataPolicy.policyTag) {
            console.log(`    Policy Tag: ${dataPolicy.policyTag}`);
          }
          if (dataPolicy.grantees && dataPolicy.grantees.length > 0) {
            console.log(`    Grantees: ${dataPolicy.grantees.join(', ')}`);
          }
          if (dataPolicy.dataMaskingPolicy) {
            if (dataPolicy.dataMaskingPolicy.predefinedExpression) {
              console.log(
                `    Data Masking Predefined Expression: ${dataPolicy.dataMaskingPolicy.predefinedExpression}`,
              );
            } else if (dataPolicy.dataMaskingPolicy.routine) {
              console.log(
                `    Data Masking Routine: ${dataPolicy.dataMaskingPolicy.routine}`,
              );
            }
          }
        }
    
        console.log(`Successfully listed ${dataPolicies.length} data policies.`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: The project or location '${location}' for project '${projectId}' was not found. ` +
              'Make sure the project ID and location are correct and that the BigQuery Data Policy API is enabled.',
          );
        } else if (err.code === status.PERMISSION_DENIED) {
          console.error(
            `Error: Permission denied when listing data policies for project '${projectId}' in location '${location}'. ` +
              'Make sure the authenticated account has the necessary permissions (For example, bigquery.datapolicies.list).',
          );
        } else {
          console.error(`Error listing data policies: ${err.message}`);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import bigquery_datapolicies_v2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def list_data_policies(project_id: str, location: str) -> None:
        """Lists all data policies in a specified project.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the data policies (for example, "us", "us-central1").
        """
    
        parent = f"projects/{project_id}/locations/{location}"
    
        try:
            request = bigquery_datapolicies_v2.ListDataPoliciesRequest(parent=parent)
    
            print(
                f"Listing data policies for project '{project_id}' in location '{location}':"
            )
            page_result = client.[list_data_policies](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_list_data_policies)(request=request)
    
            found_policies = False
            for data_policy in page_result:
                found_policies = True
                print(f"  Data Policy Name: {data_policy.name}")
                print(f"  Data Policy ID: {data_policy.data_policy_id}")
                print(f"  Data Policy Type: {data_policy.data_policy_type.name}")
                if data_policy.policy_tag:
                    print(f"  Policy Tag: {data_policy.policy_tag}")
                if data_policy.grantees:
                    print(f"  Grantees: {', '.join(data_policy.grantees)}")
                print("-" * 20)
    
            if not found_policies:
                print("No data policies found.")
    
        except google.api_core.exceptions.NotFound as e:
            print(f"Error: The specified project or location was not found or accessible.")
            print(f"Details: {e}")
            print(
                "Make sure the project ID and location are correct and you have the necessary permissions."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
