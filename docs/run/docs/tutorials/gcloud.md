---
url: https://docs.cloud.google.com/run/docs/tutorials/gcloud/
title: gcloud command line inside a Cloud Run service tutorial \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:00.334166+00:00
---

# gcloud command line inside a Cloud Run service tutorial  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  gcloud command line inside a Cloud Run service tutorial Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you create an inventory of Cloud Run services using the Google Cloud CLI inside a Cloud Run service. You can apply what you learn in this tutorial to your existing Cloud operations scripts or to build a proof-of-concept before using [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) to build a more robust service.

You use the gcloud CLI like any shell script inside a web service, for example, as shown in the [Shell quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-shell-service). On Cloud Run, both tools work with Google Cloud services by automatically authenticating with the Cloud Run [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity). Any permissions given to the service identity are available to the gcloud CLI.

The gcloud CLI is so broadly capable of information gathering and resource management across Google Cloud that the challenge of using it within a web service is minimizing the risk of a caller misusing these capabilities. Without security controls, you could create risk to other services or resources running in the same project by allowing accidental or intentional malicious activity. Examples of these risks include:

  * Enabling the discovery of IP addresses of private virtual machines
  * Enabling access to private data from a database in the same project
  * Enabling deletion of other running services



Several steps in this tutorial show how to impose controls to minimize risks, such as specifying the `gcloud` command to be run in the code, instead of leaving it open as a user input.

Scripting with the command line tool inside a Cloud Run service is similar to using the command line locally. The main difference is the additional restrictions you should add around the primary script logic.

## Objectives

  * Write and build a [custom container](https://www.docker.com/resources/what-container) with a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
  * Write, build, and [deploy](https://docs.cloud.google.com/run/docs/deploying) a Cloud Run service
  * Use the gcloud CLI safely in a web service
  * Generate a report of Cloud Run services and save to Cloud Storage



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Storage](https://cloud.google.com/storage)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Artifact Registry, Cloud Build, Cloud Run, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,run.googleapis.com,storage.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Set up gcloud defaults

To configure gcloud with defaults for your Cloud Run service:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this tutorial.

  2. Configure gcloud for your chosen region:
         
         gcloud config set run/region REGION

Replace REGION with the supported Cloud Run region of your choice.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

## Retrieving the code sample

To retrieve the code sample for use:

  1. Clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/cloud-run-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/cloud-run-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run sample code:
         
         cd cloud-run-samples/gcloud-report/




## Review the code

This section includes information about the code sample you retrieved.

### Generate a report and upload it to Cloud Storage

This shell script generates a report of Cloud Run services in the current project and region and uploads the result to Cloud Storage. It lists services whose name contains the provided string `search` argument.

The script uses the [`gcloud run services list`](https://docs.cloud.google.com/run/docs/managing/services#command-line) command, [`gcloud` advanced format options](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats), and [`gcloud` streaming transfer](https://docs.cloud.google.com/storage/docs/streaming-reads) copy mode.
    
    
    set -eo pipefail
    
    # Check for required environment variables.
    requireEnv() {
      test "${!1}" || (echo "gcloud-report: '$1' not found" >&2 && exit 1)
    }
    requireEnv GCLOUD_REPORT_BUCKET
    
    # Prepare formatting: Default search term to include all services.
    search=${1:-'.'}
    limits='spec.template.spec.containers.resources.limits.flatten("", "", " ")'
    format='table[box, title="Cloud Run Services"](name,status.url,metadata.annotations.[serving.knative.dev/creator],'${limits}')'
    
    # Create a specific object name that will not be overridden in the future.
    obj="gs://${GCLOUD_REPORT_BUCKET}/report-${search}-$(date +%s).txt"
    
    # Write a report containing the service name, service URL, service account or user that
    # deployed it, and any explicitly configured service "limits" such as CPU or Memory.
    gcloud run services list \
      --format "${format}" \
      --filter "metadata.name~${search}" | gcloud storage cp --gzip-in-flight-all - "${obj}"
    
    # /dev/stderr is sent to Cloud Logging.
    echo "gcloud-report: wrote to ${obj}" >&2
    echo "Wrote report to ${obj}"
    

This script is safe to run as a service because repeated invocations of it update the report without further costly churn. Other scripts using the gcloud CLI can be more costly when invoked repeatedly, such as creating new Cloud resources or performing expensive tasks. Idempotent scripts, which yield the same result on repeated invocations, are safer to run as a service.

### Invoke the script on HTTP request

This Go code sets up a web service that runs a shell script to generate a report. Since the search query is user input, the code validates it to ensure that it only contains letters, numbers, or hyphens to prevent malicious commands as input. This set of characters is narrow enough to prevent [command injection attacks](https://en.wikipedia.org/wiki/Code_injection#Shell_injection).

The web service passes the search parameter as an argument to the shell script.
    
    
    // Service gcloud-report is a Cloud Run shell-script-as-a-service.
    package main
    
    import (
    	"log"
    	"net/http"
    	"os"
    	"os/exec"
    	"regexp"
    )
    
    func main() {
    	http.HandleFunc("/", scriptHandler)
    
    	// Determine port for HTTP service.
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    		log.Printf("defaulting to port %s", port)
    	}
    
    	// Start HTTP server.
    	log.Printf("listening on port %s", port)
    	if err := http.ListenAndServe(":"+port, nil); err != nil {
    		log.Fatal(err)
    	}
    }
    
    func scriptHandler(w http.ResponseWriter, r *http.Request) {
    	search := r.URL.Query().Get("search")
    	re := regexp.MustCompile(`^[a-z]+[a-z0-9\-]*$`)
    	if !re.MatchString(search) {
    		log.Printf("invalid search criteria %q, using default", search)
    		search = "."
    	}
    
    	cmd := exec.CommandContext(r.Context(), "/bin/bash", "script.sh", search)
    	cmd.Stderr = os.Stderr
    	out, err := cmd.Output()
    	if err != nil {
    		log.Printf("Command.Output: %v", err)
    		http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
    		return
    	}
    	w.Write(out)
    }
    

**Note:** To see how to invoke a command in other languages, review the [System packages tutorial](https://docs.cloud.google.com/run/docs/tutorials/system-packages). The code shown in that tutorial is implemented in Go for fast performance and short cold starts: the business logic is in the shell script.

A `go.mod` file declares the application dependencies in a [go module](https://blog.golang.org/using-go-modules):
    
    
    module github.com/GoogleCloudPlatform/cloud-run-samples/gcloud-report
    
    go 1.19
    

### Define the container environment

The Dockerfile defines how the environment is put together for the service. It is similar to the Dockerfile from the [helloworld-shell quickstart](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-shell-service), except that the final container image is based on the `gcloud` Google Cloud CLI image. This allows your service to use `gcloud` without custom installation and configuration steps for the Google Cloud CLI.
    
    
    # Use the official golang image to create a binary.
    # This is based on Debian and sets the GOPATH to /go.
    # https://hub.docker.com/_/golang
    FROM golang:1.20-buster as builder
    
    # Create and change to the app directory.
    WORKDIR /app
    
    # Retrieve application dependencies.
    # This allows the container build to reuse cached dependencies.
    # Expecting to copy go.mod and if present go.sum.
    COPY go.* ./
    RUN go mod download
    
    # Copy local code to the container image.
    COPY invoke.go ./
    
    # Build the binary.
    RUN go build -mod=readonly -v -o server
    
    # Use a gcloud image based on debian:buster-slim for a lean production container.
    # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
    FROM gcr.io/google.com/cloudsdktool/cloud-sdk:slim
    
    WORKDIR /app
    
    # Copy the binary to the production image from the builder stage.
    COPY --from=builder /app/server /app/server
    COPY *.sh /app/
    RUN chmod +x /app/*.sh
    
    # Run the web service on container startup.
    CMD ["/app/server"]
    

## Create an Artifact Registry standard repository

Create an Artifact Registry standard repository to store your container image:
    
    
    gcloud artifacts repositories create REPOSITORY \
        --repository-format=docker \
        --location=REGION

Replace:

  * REPOSITORY with a unique name for the repository.
  * REGION with the Google Cloud region of the Artifact Registry.



## Set up the Cloud Storage bucket

Create a Cloud Storage bucket for uploading reports:
    
    
    gcloud storage buckets create gs://REPORT_ARCHIVE_BUCKET

Replace REPORT_ARCHIVE_BUCKET with a globally unique bucket name.

## Set up the service identity

In order to limit the privileges that the service has to other infrastructure, you create a service identity and customize the specific IAM permissions necessary to do the work.

In this case, the required privileges are permission to read Cloud Run services and permission to read from and write to the Cloud Storage bucket.

  1. Create a service account: 
         
         gcloud iam service-accounts create gcloud-report-identity

  2. Grant the service account permission to read Cloud Run services:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:gcloud-report-identity@PROJECT_ID.iam.gserviceaccount.com \
           --role roles/run.viewer

  3. Grant the service account permission to read from and write to the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://REPORT_ARCHIVE_BUCKET \
           --member=serviceAccount:gcloud-report-identity@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/storage.objectUser




The limited access of this customized service identity prevents the service from accessing other Google Cloud resources.

## Ship the service

Shipping code consists of three steps:

  * Building a container image with Cloud Build
  * Uploading the container image to Artifact Registry
  * Deploying the container image to Cloud Run.



To ship your code:

  1. Build your container and publish on Artifact Registry:
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/gcloud-report

Replace:

     * PROJECT_ID with your Google Cloud project ID
     * REPOSITORY with the name of the Artifact Registry repository.
     * REGION with the Google Cloud region of the Artifact Registry.

`gcloud-report` is the name of your service.

Upon success, a SUCCESS message displays the ID, creation time, and image name. The image is stored in Artifact Registry and can be reused if required.

  2. Run the following command to deploy your service:
         
         gcloud run deploy gcloud-report \
            --image REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/gcloud-report \
            --update-env-vars GCLOUD_REPORT_BUCKET=REPORT_ARCHIVE_BUCKET \
            --service-account gcloud-report-identity \
            --no-allow-unauthenticated

Replace:

     * PROJECT_ID with your Google Cloud project ID.
     * REPOSITORY with the name of the Artifact Registry repository.
     * REGION with the Google Cloud region of the service.

`gcloud-report` is part of the container name and the name of the service. The container image is deployed to the service and region (Cloud Run) that you configured previously under Setting up gcloud.

The `--no-allow-unauthenticated` flag restricts public access to the service. By keeping the service private you can rely on Cloud Run's built-in authentication to block unauthorized requests. For more details about authentication that is based on Identity and Access Management (IAM), see [Managing access using IAM](https://docs.cloud.google.com/run/docs/securing/managing-access).

Wait until the deployment is complete. This can take about half a minute. On success, the command line displays the service URL.

  3. If you want to deploy a code update to the service, repeat the previous steps. Each deployment to a service creates a new revision and automatically starts serving traffic when ready.




See [Managing access using IAM](https://docs.cloud.google.com/run/docs/securing/managing-access#adding_users) for how to grant Google Cloud users access to invoke this service. Project editors and owners automatically have this access.

## Generate a report

To generate a report of Cloud Run services:

  1. Use curl to send an authenticated request:
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL

Replace SERVICE_URL with the URL provided by Cloud Run after completing deployment.

If you created a new project and followed this tutorial, the output will be similar to:
         
         Wrote report to gs://REPORT_ARCHIVE_BUCKET/report-.-DATE.txt

The `.` in the filename is the default search argument as mentioned in the source code.

To use the search feature, add a `search` argument to the request:
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL?search=gcloud

This query will return output similar to:
         
         Wrote report to gs://REPORT_ARCHIVE_BUCKET/report-gcloud-DATE.txt

  2. Retrieve the file using the gcloud CLI locally:
         
         gcloud storage cp gs://REPORT_FILE_NAME .

The `.` in the command means the current working directory.

Replace REPORT_FILE_NAME with the Cloud Storage object name output in the previous step.




Open the file to see the report. It should look like this:

![Screenshot of the list of Cloud Run services in the project with columns for four service attributes.](https://docs.cloud.google.com/static/run/docs/tutorials/images/gcloud-report-output.png)The four columns are pulled from the service description. They include **Name** of the service, **URL** assigned on first deployment, the initial **Creator** of the service, and the service **Limits** of maximum CPU and memory.**Success:** You created an inventory of Cloud Run services using the Google Cloud CLI inside a Cloud Run service.

## Improve robustness for the future

If you intend to further develop this service, consider rewriting in a more robust programming language and using the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest) and the [Cloud Storage client library](https://docs.cloud.google.com/storage/docs/reference/libraries).

You can examine the API calls being made (and see some authentication details) by adding `--log-http` to gcloud CLI commands.

## Automate this operation

Now that the report of Cloud Run services can be triggered by an HTTP request, use automation to generate reports when you need them:

  * Run this service on a [schedule](https://docs.cloud.google.com/run/docs/triggering/using-scheduler) with Cloud Scheduler
  * Create the report as a [queued task or schedule in the future](https://docs.cloud.google.com/run/docs/triggering/using-tasks) with Google Tasks 



## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the Cloud Storage bucket REPORT_ARCHIVE_BUCKET](https://docs.cloud.google.com/storage/docs/deleting-objects)
     * [Delete your container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).
     * [Delete the invoker service account `gcloud-report-identity@PROJECT_ID.iam.gserviceaccount.com`](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-delete-gcloud)



## What's next

  * Reduce the dependencies of your service by replacing the gcloud CLI command with API calls: [Uploading Objects](https://docs.cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample), [Cloud Run Admin API Reference](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services/list)
  * Further enhance the security by using [network ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress)to limit access to your service.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
