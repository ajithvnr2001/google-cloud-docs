---
url: https://docs.cloud.google.com/profiler/docs/downloading-profiles/
title: Download profile data \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:51.919429+00:00
---

# Download profile data  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/downloading-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Download profile data

This document describes how you can download your profile data to your local system, and how you can programmatically retrieve profile data by using a Go application.

## Download profiles by using the Google Cloud console

To download the profile displayed in the flame graph, click **Download** _get_app_.

Profiler uses the following naming convention for the downloaded file:
    
    
    profiler_[SERVICE_NAME]_[PROFILE_TYPE]_[FROM_DATE]_[TO_DATE]_[ZONE]_[VERSION].pb.gz
    

In this expression:

  * `SERVICE_NAME` contains your **Service** selection
  * `PROFILE_TYPE` contains your **Profile type** selection
  * `FROM_DATE` and `TO_DATE` contains your time-range specifications
  * `ZONE` contains your **Zone** selection
  * `VERSION` contains your **Version** selection



Example: `profiler_docdemo-service_HEAP_2018-04-22T20_25_31Z_2018-05-22T20_25_31Z_us-east1-c.pb.gz`

## Download profiles programmatically

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To retrieve profile data, use the `ListProfiles` API method. The following sample Go program demonstrates the use of this API.

The sample program creates a folder in the directory from where it is run, and generates a set of numbered [`pprof`](https://github.com/google/pprof) files. Each file has a naming convention similar to `profile000042.pb.gz`. Each directory contains profile data and a metadata file - `metadata.csv`, which contains information about the downloaded files.
    
    
    // Sample export shows how ListProfiles API can be used to download
    // existing pprof profiles for a given project from GCP.
    package main
    
    import (
    	"bytes"
    	"context"
    	"encoding/csv"
    	"encoding/json"
    	"flag"
    	"fmt"
    	"io"
    	"log"
    	"os"
    	"time"
    
    	cloudprofiler "cloud.google.com/go/cloudprofiler/apiv2"
    	pb "cloud.google.com/go/cloudprofiler/apiv2/cloudprofilerpb"
    	"google.golang.org/api/iterator"
    )
    
    var project = flag.String("project", "", "GCP project ID from which profiles should be fetched")
    var pageSize = flag.Int("page_size", 100, "Number of profiles fetched per page. Maximum 1000.")
    var pageToken = flag.String("page_token", "", "PageToken from a previous ListProfiles call. If empty, the listing will start from the begnning. Invalid page tokens result in error.")
    var maxProfiles = flag.Int("max_profiles", 1000, "Maximum number of profiles to fetch across all pages. If this is <= 0, will fetch all available profiles")
    
    const ProfilesDownloadedSuccessfully = "Read max allowed profiles"
    
    // This function reads profiles for a given project and stores them into locally created files.
    // The profile metadata gets stored into a 'metdata.csv' file, while the individual pprof files
    // are created per profile.
    func downloadProfiles(ctx context.Context, w io.Writer, project, pageToken string, pageSize, maxProfiles int) error {
    	client, err := cloudprofiler.[NewExportClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudprofiler/latest/apiv2.html#cloud_google_com_go_cloudprofiler_apiv2_ExportClient_NewExportClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    	log.Printf("Attempting to fetch %v profiles with a pageSize of %v for %v\n", maxProfiles, pageSize, project)
    
    	// Initial request for the ListProfiles API
    	request := &pb.ListProfilesRequest{
    		Parent:    fmt.Sprintf("projects/%s", project),
    		PageSize:  int32(pageSize),
    		PageToken: pageToken,
    	}
    
    	// create a folder for storing profiles & metadata
    	profilesDirName := fmt.Sprintf("profiles_%v", time.Now().Unix())
    	if err := os.Mkdir(profilesDirName, 0750); err != nil {
    		log.Fatal(err)
    	}
    	// create a file for storing profile metadata
    	metadata, err := os.Create(fmt.Sprintf("%s/metadata.csv", profilesDirName))
    	if err != nil {
    		return err
    	}
    	defer metadata.Close()
    
    	writer := csv.NewWriter(metadata)
    	defer writer.Flush()
    
    	writer.Write([]string{"File", "Name", "ProfileType", "Target", "Duration", "Labels"})
    
    	profileCount := 0
    	// Keep calling ListProfiles API till all profile pages are fetched or max pages reached
    	profilesIterator := client.ListProfiles(ctx, request)
    	for {
    		// Read individual profile - the client will automatically make API calls to fetch next pages
    		profile, err := profilesIterator.[Next](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudprofiler/latest/apiv2.html#cloud_google_com_go_cloudprofiler_apiv2_ProfileIterator_Next)()
    
    		if err == iterator.Done {
    			log.Println("Read all available profiles")
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("error reading profile from response: %w", err)
    		}
    		profileCount++
    
    		filename := fmt.Sprintf("%s/profile%06d.pb.gz", profilesDirName, profileCount)
    		err = os.WriteFile(filename, profile.ProfileBytes, 0640)
    
    		if err != nil {
    			return fmt.Errorf("unable to write file %s: %w", filename, err)
    		}
    		fmt.Fprintf(w, "deployment target: %v\n", profile.Deployment.Labels)
    
    		labelBytes, err := json.Marshal(profile.Labels)
    		if err != nil {
    			return err
    		}
    
    		err = writer.Write([]string{filename, profile.Name, profile.Deployment.Target, profile.Duration.String(), string(labelBytes)})
    		if err != nil {
    			return err
    		}
    
    		if maxProfiles > 0 && profileCount >= maxProfiles {
    			fmt.Fprintf(w, "result: %v", ProfilesDownloadedSuccessfully)
    			break
    		}
    
    		if profilesIterator.PageInfo().Remaining() == 0 {
    			// This signifies that the client will make a new API call internally
    			log.Printf("next page token: %v\n", profilesIterator.[PageInfo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudprofiler/latest/apiv2.html#cloud_google_com_go_cloudprofiler_apiv2_ProfileIterator_PageInfo)().Token)
    		}
    	}
    	return nil
    }
    
    func main() {
    	flag.Parse()
    	// validate project ID
    	if *project == "" {
    		log.Fatalf("No project ID provided, please provide the GCP project ID via '-project' flag")
    	}
    	var writer bytes.Buffer
    	if err := downloadProfiles(context.Background(), &writer, *project, *pageToken, *pageSize, *maxProfiles); err != nil {
    		log.Fatal(err)
    	}
    	log.Println("Finished reading all profiles")
    }
    

The sample program accepts the following command line arguments:

  * `project`: The project from which the profiles are retrieved. Required.
  * `page_size`: The maximum number of profiles retrieved per API call. The maximum value of `page_size` is 1000. When not specified, this field is set to 100.
  * `page_token`: A string token generated by a previous run of the program to resume downloads. Optional.
  * `max_profiles`: The maximum number of profiles to retrieve. If a non-positive integer is provided, then the program attempts to retrieve all profiles.  
Optional.



### Run the sample application

**Note:** To successfully run the program, it must be authenticated to Profiler. Authentication can be set up using Application Default Credentials (ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

To run the sample application, do the following:

  1. Clone the repository:
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git
         

  2. Change to the directory that contains the sample program:
         
         cd golang-samples/profiler/export
         

  3. Run the program after you replace YOUR_GCP_PROJECT with the ID of your Google Cloud project:
         
         go run main.go -project YOUR_GCP_PROJECT -page_size 1000 -max_profiles 10000
         




The program might take considerable time to complete. The program outputs a token for the next page after retrieving the current page. You can use the token to resume the process if the program is interrupted.

## View the downloaded profiles

To read a downloaded file, which is written in the [serialized protocol buffer](https://github.com/google/pprof/tree/master/proto) format, use the open source [`pprof`](https://github.com/google/pprof) tool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
