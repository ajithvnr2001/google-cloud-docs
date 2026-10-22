---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images/
title: Confidential Space images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:26.626250+00:00
---

# Confidential Space images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  Confidential Space images Stay organized with collections  Save and categorize content based on your preferences. 

[ Workload operator ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles)

A Confidential Space image is a minimal, single-purpose OS that's run on a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance. It's designed to run a single [workload](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads) only once, without persistent storage. That workload is layered on top of the Confidential Space image using [Docker](https://www.docker.com/).

Confidential Space images are built on the existing security enhancements of [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) and add the following benefits:

  * Encrypted disk partitions with integrity protection

  * Authenticated, encrypted network connections

  * Various boot measurements

  * Disabled remote access and cloud-specific tooling




## Types of images

Confidential Space images are available in two variants:

  * **Production** : The production image is used for running real production workloads with real production data. It is locked down to prevent the workload operator from accessing the processed data. For more information, see [Confidential Space security overview](https://docs.cloud.google.com/docs/security/confidential-space).

  * **Debug** : The debug image is used for [testing your workload](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/monitor-debug) on non-production data. SSH is enabled on the debug image, and the operator has root access to the VM that runs the workload. The VM running the debug image doesn't stop after the workload is complete.




You can set which image type to use when you [deploy the workload](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads).

## View Confidential Space images

You can view the available Confidential Space images with the following `gcloud` command:
    
    
    gcloud compute images list \
        --project=confidential-space-images \
        --no-standard-images
    

The following flags can change the returned images in the results:

  * Add the `--filter="family~'confidential-space$'"` flag to show production images.

  * Add the `--filter="family~'confidential-space-debug$'"` flag to show debug images.




### View deprecated images

Run the following command to include deprecated images in the results, along with additional fields that can help inform decision making:
    
    
    gcloud compute images list \
        --project=confidential-space-images \
        --no-standard-images \
        --show-deprecated \
        --filter="name ~ '^confidential-space-[0-9]{6}$'" \
        --format="table(
          name,
          creationTimestamp.date('%Y-%m-%d'):label=CREATION_DATE,
          status,
          description.sub('.*COS: ', '').sub(',.*', ''):label=COS_VERSION,
          deprecated.state:label=STATE,
          deprecated.deprecated:label=DEPRECATE_ON,
          deprecated.obsolete:label=OBSOLETE_ON,
          deprecated.replacement
        )"
    

A successful response is similar to the following:
    
    
    NAME                       CREATION_DATE  STATUS  COS_VERSION               STATE       DEPRECATE_ON  OBSOLETE_ON  REPLACEMENT
    confidential-space-230600  2023-06-09     READY   cos-dev-109-17637-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-230901
    confidential-space-230900  2023-09-17     READY   cos-dev-109-17637-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-230600
    confidential-space-230901  2023-10-02     READY   cos-dev-113-17877-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-231001
    confidential-space-231001  2023-11-01     READY   cos-dev-113-17965-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-231100
    confidential-space-231100  2023-11-17     READY   cos-dev-113-18026-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-231200
    confidential-space-231200  2023-12-04     READY   cos-dev-113-18054-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-231201
    confidential-space-231201  2023-12-15     READY   cos-dev-113-18059-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-240200
    confidential-space-240200  2024-02-28     READY   cos-dev-113-18146-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-240402
    confidential-space-240402  2024-04-22     READY   cos-dev-117-18342-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-240500
    confidential-space-240500  2024-05-30     READY   cos-dev-117-18374-0-0     DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-240700
    confidential-space-240700  2024-07-30     READY   cos-113-18244-85-54       DEPRECATED                             https://www.googleapis.com/compute/v1/projects/confidential-space-images/global/images/confidential-space-240800
    confidential-space-240800  2024-09-03     READY   cos-113-18244-151-14
    confidential-space-240900  2024-10-01     READY   cos-113-18244-151-80
    confidential-space-241000  2024-10-18     READY   cos-113-18244-151-96
    ...
    

## Confidential Space image lifecycle

When you create a Confidential VM using a Confidential Space image family, the latest version of the Confidential Space image is used. If you always delete your Confidential VM when your workload is done and create a new one each time you run the workload, then you can be sure the image is up to date.

However, long-running workloads or running a workload on a VM created in the past opens you up to the risk of using an outdated Confidential Space image, which might introduce security vulnerabilities.

To mitigate this, a data collaborator can [use support attributes](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=image-assertions#support_attributes) to check if a production Confidential Space image version running on a VM is recent, and deny it access to their data if it doesn't pass. Debug Confidential Space images have no support attribute set.

The following table describes the support attributes found on production Confidential Space images. 

Support attribute | Description  
---|---  
`LATEST` `LATEST` images also have the following support attributes:

  * `STABLE`
  * `USABLE`

|  **Image lifetime** : Approximately one month. After this, the `LATEST` support attribute is removed.  This is the latest version of the Confidential Space image, and is supported and monitored for vulnerabilities.  For long-running workloads, we recommend that you don't specify `LATEST` as part of your attestation policy. This is because the Confidential Space image might be updated while your workload is running, making the Confidential Space image you're using no longer `LATEST`, and causing your workload to fail attestation when the Confidential Space default token is next refreshed.   
`STABLE` `STABLE` images also have the following support attributes:

  * `USABLE`

|  **Image lifetime** : Approximately six months. Starting April 1, 2027, the `STABLE` support attribute is removed after the image lifetime expires.  Images with the `STABLE` attribute are supported and monitored for vulnerabilities for a period of six months. We recommend writing attestation policy based on the `STABLE` attribute.  In rare cases, the `STABLE` attribute can be removed during the normal six-month support period, such as when critical vulnerabilities are discovered.   
`USABLE` |  Images with only the `USABLE` attribute are still available to use, but are considered deprecated. Deprecated images aren't supported, and are over six months old. Use them at your own risk.  `USABLE` images have a `deprecated.deprecated` property. Its value is the timestamp of when the image is expected to be deprecated. An image's properties can be viewed with the [ `gcloud compute images describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe) command, or with the [`images.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get) REST method. For example: 
    
    
    gcloud compute images describe confidential-space-240800 \
        --format=json \
        --project=confidential-space-images  
  
`EXPERIMENTAL` |  Images with only this attribute make use of preview features. `EXPERIMENTAL` images are for testing purposes only, and should never be used in production.  An `EXPERIMENTAL` image never has the attributes `LATEST`, `STABLE`, or `USABLE`.   
  
We recommend keeping your Confidential Space image up to date. To learn how to update your Confidential Space image, see [ Update Confidential Space images](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images#update-images). 

**Important:** Confidential Space images can be revoked due to events such as critical vulnerabilities being discovered. When an image is revoked, the `swname` claim in the [attestation token](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/token-claims) is set to `GCE`, or your workload receives a `RIMS_VALIDATION_FAILED` message when requesting the token. 

## Monitor for deprecated images

To monitor for VM instances that are running deprecated or soon-to-be-deprecated Confidential Space images, you can deploy a Cloud Run function that's run regularly with a Cloud Scheduler job. You can then set up Cloud Logging notifications to alert you when images have been deprecated.

### Deploy a Cloud Run function to check for deprecated images

To set up the Cloud Run function, complete the following instructions:

  1. In Cloud Run, go to the **Services** page.

[Go to Services](https://console.cloud.google.com/run/services)

  2. Click **Write a function**.

  3. In the **Service name** box, enter a name for the function.

  4. Select a region to run the function in.

  5. Set the **Runtime** to a recent version of **Go**.

  6. Set **Authentication** to **Require authentication**.

  7. Set **Ingress** to **Internal**.

  8. Expand the **Containers, Networking, Security** section.

  9. In the **Containers** tab, set **Memory** to **128 MiB**.

  10. In the **Security** tab, click the **Service account** box.

  11. Click **Create new service account**.

  12. Enter a name in the **Service account name** box.

  13. Click **Create**.

  14. Add the **Compute Viewer** role, and then click **Done**.

  15. Click **Create**.

  16. After your function loads, in the **Source** tab set the **Function entry point** to `DeprecationCheck`.

  17. Overwrite the contents in `function.go` with the following code:
         
         // Package imagechecker provides a function to check for deprecated CS images.
         package imagechecker
         
         import (
         	"context"
         	"encoding/json"
         	"fmt"
         	"log"
         	"log/slog"
         	"net/http"
         	"regexp"
         	"strings"
         	"time"
         
         	"cloud.google.com/go/compute/metadata"
         	"google.golang.org/api/compute/v1"
         	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
         )
         
         const (
         	sourceImageProject  = "confidential-space-images"
         	deprecationValueFmt = "2006-01-02"
         )
         
         // CS Images have the format confidential-space-.*.
         var prodImageNameRegex = regexp.MustCompile(`^confidential-space-.*`)
         
         // VMInfo represents the information logged about an VM instance of note.
         type VMInfo struct {
         	Name            string `json:"instance_name"`
         	Zone            string `json:"instance_zone"`
         	ImageName       string `json:"image_name"`
         	DeprecationDate string `json:"image_deprecation_date,omitempty"`
         	ObsoleteDate    string `json:"image_obsolete_date,omitempty"`
         }
         
         // VMList represents a list of notable VMs and their relevance.
         type VMList struct {
         	Description string   `json:"description"`
         	Instances   []VMInfo `json:"instances"`
         }
         
         // LogPayload is the payload for Cloud Logs written by this job.
         type LogPayload struct {
         	Message            string  `json:"message"`
         	Obsolete           *VMList `json:"vms_obsolete"`
         	ObsoleteWarning    *VMList `json:"vms_obsolete_warning"`
         	Deprecated         *VMList `json:"vms_deprecated"`
         	DeprecationWarning *VMList `json:"vms_deprecation_warning"`
         }
         
         // LogEntry represents a Cloud Logging entry.
         type LogEntry struct {
         	Message   string      `json:"message"`
         	Severity  string      `json:"severity"` // Special field for Cloud Logging.
         	Payload   *LogPayload `json:"payload,omitempty"`
         	ProjectID string      `json:"projectId"`
         }
         
         func init() {
         	log.SetFlags(0)
         	functions.HTTP("DeprecationCheck", checkForDeprecations)
         }
         
         func checkForDeprecations(w http.ResponseWriter, r *http.Request) {
         	ctx := context.Background()
         
         	// Retrieve project ID.
         	projectID, err := metadata.[ProjectIDWithContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/metadata/latest/index.html#cloud_google_com_go_compute_metadata_ProjectIDWithContext)(ctx)
         	if err != nil {
         		errMsg := fmt.Sprintf("Failed to get project ID from metadata server: %v", err)
         		logError(projectID, errMsg)
         		http.Error(w, errMsg, http.StatusInternalServerError)
         		return
         	}
         	slog.Info(fmt.Sprintf("Checking for project: %s", projectID))
         
         	// Configure compute service.
         	computeService, err := compute.NewService(ctx)
         	if err != nil {
         		msg := fmt.Sprintf("Failed to create compute service: %v", err)
         		logError(projectID, msg)
         		http.Error(w, msg, http.StatusInternalServerError)
         		return
         	}
         
         	var obsoleteVMs []VMInfo           // Will contain VMs whose images are obsolete.
         	var obsoleteWarningVMs []VMInfo    // Will contain VMs using an image that will be obsolete within a month.
         	var deprecatedVMs []VMInfo         // Will contain VMs whose images are deprecated.
         	var deprecationWarningVMs []VMInfo // Will contain VMs using an image that will be deprecated within a month.
         	now := time.Now()
         
         	pageFunc := instancesPageFunc(ctx, projectID, &obsoleteVMs, &obsoleteWarningVMs, &deprecatedVMs, &deprecationWarningVMs, now, computeService)
         	if err = computeService.Instances.AggregatedList(projectID).Pages(ctx, pageFunc); err != nil {
         		msg := fmt.Sprintf("Failed to list instances: %v", err)
         		logError(projectID, msg)
         		http.Error(w, msg, http.StatusInternalServerError)
         		return
         	}
         
         	if len(obsoleteVMs) == 0 && len(obsoleteWarningVMs) == 0 && len(deprecatedVMs) == 0 && len(deprecationWarningVMs) == 0 {
         		returnmsg := "No VMs using obsolete or deprecated images found."
         		logEntry := LogEntry{
         			Message:   "Confidential Space Image Deprecation Alert - No Issues Detected",
         			Severity:  "INFO",
         			ProjectID: projectID,
         			Payload:   &LogPayload{Message: returnmsg},
         		}
         		writeLog(logEntry)
         
         		w.WriteHeader(http.StatusOK)
         		_, err := w.Write([]byte(returnmsg))
         		if err != nil {
         			http.Error(w, fmt.Sprintf("Failed to write HTTP response: %v", err), http.StatusInternalServerError)
         		}
         		return
         	}
         
         	respPayload := &LogPayload{
         		Message: "The following instances are using Confidential Space images that are obsolete, deprecated, or will be obsolete/deprecated soon. Obsolete and deprecated images are no longer maintained and scanned for vulnerabilities. Please review these instances and update their boot images as needed.",
         	}
         
         	if len(obsoleteVMs) > 0 {
         		respPayload.Obsolete = &VMList{
         			Description: "Instances using CS images that are obsolete.",
         			Instances:   obsoleteVMs,
         		}
         	}
         	if len(obsoleteWarningVMs) > 0 {
         		respPayload.ObsoleteWarning = &VMList{
         			Description: "Instances using CS images that will be obsolete within a month.",
         			Instances:   obsoleteWarningVMs,
         		}
         	}
         	if len(deprecatedVMs) > 0 {
         		respPayload.Deprecated = &VMList{
         			Description: "Instances using CS images that are deprecated.",
         			Instances:   deprecatedVMs,
         		}
         	}
         	if len(deprecationWarningVMs) > 0 {
         		respPayload.DeprecationWarning = &VMList{
         			Description: "Instances using CS images that will be deprecated within a month.",
         			Instances:   deprecationWarningVMs,
         		}
         	}
         
         	entry := LogEntry{
         		Message:   "Confidential Space Image Deprecation Alert",
         		Severity:  "WARNING",
         		ProjectID: projectID,
         		Payload:   respPayload,
         	}
         
         	writeLog(entry)
         
         	w.Header().Set("Content-Type", "application/json")
         	w.WriteHeader(http.StatusOK)
         	err = json.NewEncoder(w).Encode(respPayload)
         	if err != nil {
         		http.Error(w, fmt.Sprintf("Failed to write HTTP response: %v", err), http.StatusInternalServerError)
         		return
         	}
         }
         
         func instancesPageFunc(ctx context.Context, projectID string, obsoleteVMs *[]VMInfo, obsoleteWarningVMs *[]VMInfo, deprecatedVMs *[]VMInfo, deprecationWarningVMs *[]VMInfo, now time.Time, computeService *compute.Service) func(list *compute.InstanceAggregatedList) error {
         	return func(list *compute.InstanceAggregatedList) error {
         		for _, instanceList := range list.Items {
         			for _, instances := range instanceList.Instances {
         				sourceImage, err := getSourceImage(ctx, projectID, instances, computeService)
         				if err != nil {
         					slog.Warn(fmt.Sprintf("Failed to get source image for instance %s: %v", instances.Name, err))
         					continue
         				}
         
         				// Skip instance if not using a CS prod image.
         				imageProject, imageName := parseImage(sourceImage)
         				if imageProject != sourceImageProject || !prodImageNameRegex.MatchString(imageName) {
         					continue
         				}
         
         				// Get deprecation status ("deprecate-on" / "obsolete-on" / state settings).
         				depStatus, err := getDeprecationStatus(ctx, imageProject, imageName, computeService)
         				if err != nil {
         					slog.Error(fmt.Sprintf("Failed to get deprecation status for image %s in project %s: %v", imageName, imageProject, err))
         					continue
         				}
         				if depStatus == nil {
         					continue
         				}
         
         				vm := VMInfo{
         					Name:      instances.Name,
         					Zone:      getResourceName(instances.Zone),
         					ImageName: imageName,
         				}
         
         				var depTime, obsTime time.Time
         				if depStatus.Deprecated != "" {
         					depTime, err = parseDeprecationDate(depStatus.Deprecated)
         					if err != nil {
         						slog.Error(fmt.Sprintf("Failed to parse deprecation date %s for image %s in project %s: %v", depStatus.Deprecated, imageName, imageProject, err))
         						continue
         					}
         					vm.DeprecationDate = depTime.Format(deprecationValueFmt)
         				}
         
         				if depStatus.Obsolete != "" {
         					obsTime, err = parseDeprecationDate(depStatus.Obsolete)
         					if err != nil {
         						slog.Error(fmt.Sprintf("Failed to parse obsolete date %s for image %s in project %s: %v", depStatus.Obsolete, imageName, imageProject, err))
         						continue
         					}
         					vm.ObsoleteDate = obsTime.Format(deprecationValueFmt)
         				}
         
         				// Determine whether instance image is obsolete, upcoming obsolete, deprecated, or upcoming deprecated.
         				if depStatus.State == "OBSOLETE" || (!obsTime.IsZero() && isPast(obsTime, now)) {
         					*obsoleteVMs = append(*obsoleteVMs, vm)
         				} else if !obsTime.IsZero() && isWarning(obsTime, now) {
         					*obsoleteWarningVMs = append(*obsoleteWarningVMs, vm)
         				} else if depStatus.State == "DEPRECATED" || (!depTime.IsZero() && isPast(depTime, now)) {
         					*deprecatedVMs = append(*deprecatedVMs, vm)
         				} else if !depTime.IsZero() && isWarning(depTime, now) {
         					*deprecationWarningVMs = append(*deprecationWarningVMs, vm)
         				}
         			}
         		}
         
         		return nil
         	}
         }
         
         func getSourceImage(ctx context.Context, projectID string, instance *compute.Instance, service *compute.Service) (string, error) {
         	for _, disk := range instance.Disks {
         		// Only check boot disk.
         		if disk.Boot {
         			// Retrieve source image for disk.
         			diskName := getResourceName(disk.Source)
         			zone := getResourceName(instance.Zone)
         
         			d, err := service.Disks.Get(projectID, zone, diskName).Context(ctx).Do()
         			if err != nil {
         				slog.Warn(fmt.Sprintf("Failed to get details for disk %s in zone %s: %v", diskName, zone, err))
         				continue
         			}
         
         			if d.SourceImage != "" {
         				return d.SourceImage, nil
         			}
         		}
         	}
         
         	return "", fmt.Errorf("no suitable source image name found for instance %s", instance.Name)
         }
         
         func getDeprecationStatus(ctx context.Context, imageProject, imageName string, service *compute.Service) (*compute.DeprecationStatus, error) {
         	image, err := service.Images.Get(imageProject, imageName).Context(ctx).Do()
         	if err != nil {
         		slog.Warn(fmt.Sprintf("Failed to get details for image %s in project %s: %v", imageName, imageProject, err))
         		return nil, err
         	}
         
         	if image.Deprecated == nil || (image.Deprecated.Deprecated == "" && image.Deprecated.Obsolete == "" && image.Deprecated.State == "") {
         		// Skip if no deprecation/obsolete setting.
         		slog.Warn(fmt.Sprintf("Image %s in project %s has no deprecate-on or obsolete-on setting", imageName, imageProject))
         		return nil, nil
         	}
         
         	return image.Deprecated, nil
         }
         
         func parseDeprecationDate(dateStr string) (time.Time, error) {
         	formats := []string{
         		time.RFC3339,
         		time.RFC3339Nano,
         		"2006-01-02T15:04:05",
         		"2006-01-02",
         		"2006-01",
         	}
         	for _, format := range formats {
         		if t, err := time.Parse(format, dateStr); err == nil {
         			return t, nil
         		}
         	}
         	return time.Time{}, fmt.Errorf("unable to parse %q as a valid deprecation date", dateStr)
         }
         
         func isPast(obsTime time.Time, now time.Time) bool {
         	return !obsTime.After(now)
         }
         
         func isWarning(targetTime time.Time, now time.Time) bool {
         	warningWindowEnd := now.AddDate(0, 1, 0)
         	return targetTime.After(now) && !targetTime.After(warningWindowEnd)
         }
         
         func parseImage(image string) (string, string) {
         	parts := strings.Split(image, "/")
         
         	var project, imageName string
         	for i, part := range parts {
         		if part == "projects" && i+1 < len(parts) {
         			project = parts[i+1]
         		} else if part == "images" && i+1 < len(parts) {
         			imageName = parts[i+1]
         		}
         	}
         
         	slog.Info(fmt.Sprintf("Source image project: %s, name: %s", project, imageName))
         
         	return project, imageName
         }
         
         // getResourceName extracts the last part of a GCP resource URL.
         func getResourceName(url string) string {
         	parts := strings.Split(url, "/")
         	return parts[len(parts)-1]
         }
         
         func writeLog(entry LogEntry) {
         	jsonData, err := json.Marshal(entry)
         	if err != nil {
         		slog.Warn(fmt.Sprintf("Error marshaling final log: %v", err))
         		slog.Warn(fmt.Sprintf("Log contents: %v", entry))
         		return
         	}
         
         	fmt.Println(string(jsonData))
         }
         
         func logError(projectID, errMsg string) {
         	entry := LogEntry{
         		Message:   "Confidential Space Image Deprecation Alert - Job Failed",
         		Severity:  "ERROR",
         		ProjectID: projectID,
         		Payload: &LogPayload{
         			Message: errMsg,
         		},
         	}
         
         	writeLog(entry)
         }
         
         

  18. Overwrite the contents in `go.mod` with the following code:
         
         module example.com/imagechecker
         
         require (
             cloud.google.com/go/compute/metadata v0.5.0
             github.com/GoogleCloudPlatform/functions-framework-go v1.9.0
             google.golang.org/api v0.264.0
         )
         
         

  19. Click **Save and redeploy**.

  20. After the service successfully deploys, note its **URL** —found near the name of the function—for later use.




### Set up a Cloud Scheduler job

To set up the Cloud Scheduler job that runs the Cloud Run function, complete the following instructions:

  1. First, create a service account to run the scheduled job. To do so, go to the **Create a Service Account** page:

[Go to Create a Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/create)

  2. In the **Service account name** box, add a service account name.

  3. Note the service account ID for later use.

  4. Click **Create and continue**.

  5. Add the **Cloud Run Invoker** role.

  6. Click **Done**.

  7. If you haven't already, [enable the Cloud Scheduler API](https://docs.cloud.google.com/scheduler/docs/setup#enable-api).

  8. In Cloud Scheduler, go to the **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/cloudscheduler)

  9. Click **Create job**.

  10. In the **Name** field, enter a name for the job.

  11. Select a region to run the scheduled job in.

  12. Add a cron schedule to the **Frequency** field. For example, `0 9 1 * *` runs the job at 9 AM on the first of each month.

  13. Set a time zone for the schedule.

  14. Click **Continue**.

  15. Set the **Target type** to **HTTP**.

  16. Set the **URL** to the URL of the Cloud Run function that you created.

  17. In the **Auth header** box, select **Add OIDC token**.

  18. Click the **Service account** box, and enter the ID of the service account you created earlier.

  19. Set the audience to the URL of the Cloud Run function that you created

  20. Click **Create**.

  21. To test the job, click more_vert **Actions** , and then click **Force run**.




### Set up log-based alerting

To set up [log-based alerting](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) about deprecated images, complete the following instructions:

  1. Go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enable **Show query**.

  3. In the query box, enter one of the following Logging Query Language queries:

     * VMs found with upcoming deprecations:
           
           resource.type="cloud_run_revision"
           severity="WARNING"
           jsonPayload.message="Confidential Space Image Deprecation Alert"
           

     * Deprecation checking failures:
           
           resource.type="cloud_run_revision"
           severity="ERROR"
           jsonPayload.message="Confidential Space Image Deprecation Alert - Job Failed"
           

     * No deprecated images detected in your VM fleet:
           
           resource.type="cloud_run_revision"
           severity="INFO"
           jsonPayload.message="Confidential Space Image Deprecation Alert - No Issues Detected"
           

  4. Click **Run query**.

  5. Near the results, click **Actions**.

  6. Click **Create log alert** , and then complete the process to create an alert policy based on the query you entered.

**Note:** Log alerts create [incidents](https://docs.cloud.google.com/logging/docs/alerting/log-based-incidents). To reduce noise, we recommend only creating alerts for results with `WARNING` and `ERROR` severities.



## Update Confidential Space images

To help keep your Confidential Space image up to date and avoid interruptions, we recommend creating a new Confidential VM instance each time you launch a Confidential Space workload. Each time you create a new instance based on the Confidential Space image, the latest Confidential Space image is provisioned.

If you can't create a new Confidential VM instance for each Confidential Space workload run, we recommend that you define a maintenance window to recreate your Confidential VM instance based on the support attribute that your relying party has set in its attestation policy:

  * If you've set an attestation policy that requires the `LATEST` support attribute, you must update the Confidential Space image at least monthly.

  * If you've set an attestation policy that requires the `STABLE` support attribute, you must update the Confidential Space image at least every six months.




You can make recreation of VMs easier by using one or more of the following:

  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)

  * [Auto-repairing managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair)

  * [One-click OS-image upgrades](https://docs.cloud.google.com/compute/docs/instance-groups/upgrading-images-in-migs)




To learn how to set these features up, see [Deploying a Confidential Space workload with MIGs using autoscaling, autohealing, and image updates](https://codelabs.developers.google.com/codelabs/confidential-space-mig).

### Long-running workloads

A Confidential Space image might become deprecated or be revoked during a long-running workload. If you've set an attestation policy to require the `STABLE` Confidential Space support attribute and the Confidential Space image your workload is using is deprecated or revoked, the Confidential VM instance running the workload won't pass attestation. To avoid interruptions, long-running workloads should be designed with resuming in mind, with their state managed securely.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
