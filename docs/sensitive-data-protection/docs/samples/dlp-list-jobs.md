---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-jobs/
title: List jobs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:35.485155+00:00
---

# List jobs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-jobs/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  List jobs Stay organized with collections  Save and categorize content based on your preferences. 

List all Cloud DLP jobs for the current project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class JobsList
    {
        public static PagedEnumerable<ListDlpJobsResponse, DlpJob> ListDlpJobs(string projectId, string filter, [DlpJobType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobType.html) jobType)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var response = dlp.ListDlpJobs(new [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Filter = filter,
                Type = jobType
            });
    
            // Uncomment to print jobs
            // foreach (var job in response)
            // {
            //     Console.WriteLine($"Job: {job.Name} status: {job.State}");
            // }
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"google.golang.org/api/iterator"
    )
    
    // listJobs lists jobs matching the given optional filter and optional jobType.
    func listJobs(w io.Writer, projectID, filter, jobType string) error {
    	// projectID := "my-project-id"
    	// filter := "`state` = FINISHED"
    	// jobType := "RISK_ANALYSIS_JOB"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Create a configured request.
    	req := &dlppb.ListDlpJobsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Filter: filter,
    		Type:   dlppb.[DlpJobType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_DlpJobType)(dlppb.[DlpJobType_value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_DlpJobType_name_DlpJobType_value)[jobType]),
    	}
    	// Send the request and iterate over the results.
    	it := client.ListDlpJobs(ctx, req)
    	for {
    		j, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    		fmt.Fprintf(w, "Job %v status: %v\n", j.GetName(), j.GetState())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[DlpJobType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJobType.html);
    import com.google.privacy.dlp.v2.[ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import java.io.IOException;
    
    public class JobsList {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        listJobs(projectId);
      }
    
      // Lists DLP jobs
      public static void listJobs(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Construct the request to be sent by the client.
          // For more info on filters and job types,
          // see https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/list
          [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html) listDlpJobsRequest =
              [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setFilter("state=DONE")
                  .setType([DlpJobType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJobType.html).valueOf("INSPECT_JOB"))
                  .build();
    
          // Send the request to list jobs and process the response
          [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).[ListDlpJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListDlpJobsPagedResponse.html) response =
              dlpServiceClient.listDlpJobs(listDlpJobsRequest);
    
          System.out.println("DLP jobs found:");
          for ([DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob : response.getPage().getValues()) {
            System.out.println(dlpJob.getName() + " -- " + dlpJob.getState());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The filter expression to use
    // For more information and filter syntax, see https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/list
    // const filter = `state=DONE`;
    
    // The type of job to list (either 'INSPECT_JOB' or 'RISK_ANALYSIS_JOB')
    // const jobType = 'INSPECT_JOB';
    async function listJobs() {
      // Construct request for listing DLP scan jobs
      const request = {
        parent: `projects/${projectId}/locations/global`,
        filter: filter,
        type: jobType,
      };
    
      // Run job-listing request
      const [jobs] = await dlp.listDlpJobs(request);
      jobs.forEach(job => {
        console.log(`Job ${job.name} status: ${job.state}`);
      });
    }
    
    listJobs();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\DlpJobType;
    use Google\Cloud\Dlp\V2\ListDlpJobsRequest;
    
    /**
     * List Data Loss Prevention API jobs corresponding to a given filter.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $filter            The filter expression to use
     */
    function list_jobs(string $callingProjectId, string $filter): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The type of job to list (either 'INSPECT_JOB' or 'REDACT_JOB')
        $jobType = DlpJobType::INSPECT_JOB;
    
        // Run job-listing request
        // For more information and filter syntax,
        // @see https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/list
        $parent = "projects/$callingProjectId/locations/global";
        $listDlpJobsRequest = (new ListDlpJobsRequest())
            ->setParent($parent)
            ->setFilter($filter)
            ->setType($jobType);
        $response = $dlp->listDlpJobs($listDlpJobsRequest);
    
        // Print job list
        $jobs = $response->iterateAllElements();
        foreach ($jobs as $job) {
            printf('Job %s status: %s' . PHP_EOL, $job->getName(), $job->getState());
            $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
    
            if ($job->getState() == JobState::DONE) {
                if (count($infoTypeStats) > 0) {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of type %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                } else {
                    print('  No findings.' . PHP_EOL);
                }
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    import google.cloud.dlp
    
    
    def list_dlp_jobs(
        project: str, filter_string: Optional[str] = None, job_type: Optional[str] = None
    ) -> None:
        """Uses the Data Loss Prevention API to lists DLP jobs that match the
            specified filter in the request.
        Args:
            project: The project id to use as a parent resource.
            filter: (Optional) Allows filtering.
                Supported syntax:
                * Filter expressions are made up of one or more restrictions.
                * Restrictions can be combined by 'AND' or 'OR' logical operators.
                A sequence of restrictions implicitly uses 'AND'.
                * A restriction has the form of '<field> <operator> <value>'.
                * Supported fields/values for inspect jobs:
                    - `state` - PENDING|RUNNING|CANCELED|FINISHED|FAILED
                    - `inspected_storage` - DATASTORE|CLOUD_STORAGE|BIGQUERY
                    - `trigger_name` - The resource name of the trigger that
                                       created job.
                * Supported fields for risk analysis jobs:
                    - `state` - RUNNING|CANCELED|FINISHED|FAILED
                * The operator must be '=' or '!='.
                Examples:
                * inspected_storage = cloud_storage AND state = done
                * inspected_storage = cloud_storage OR inspected_storage = bigquery
                * inspected_storage = cloud_storage AND
                                      (state = done OR state = canceled)
            type: (Optional) The type of job. Defaults to 'INSPECT'.
                Choices:
                DLP_JOB_TYPE_UNSPECIFIED
                INSPECT_JOB: The job inspected content for sensitive data.
                RISK_ANALYSIS_JOB: The job executed a Risk Analysis computation.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Job type dictionary
        job_type_to_int = {
            "DLP_JOB_TYPE_UNSPECIFIED": google.cloud.dlp.[DlpJobType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJobType.html).DLP_JOB_TYPE_UNSPECIFIED,
            "INSPECT_JOB": google.cloud.dlp.[DlpJobType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJobType.html).INSPECT_JOB,
            "RISK_ANALYSIS_JOB": google.cloud.dlp.[DlpJobType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJobType.html).RISK_ANALYSIS_JOB,
        }
        # If job type is specified, convert job type to number through enums.
        if job_type:
            job_type = job_type_to_int[job_type]
    
        # Call the API to get a list of jobs.
        response = dlp.list_dlp_jobs(
            request={"parent": parent, "filter": filter_string, "type_": job_type}
        )
    
        # Iterate over results.
        for job in response:
            print(f"Job: {job.name}; status: {job.state.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
