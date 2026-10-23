---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/how-to-hybrid-jobs/
title: Inspect data from external sources using hybrid jobs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:31.425825+00:00
---

# Inspect data from external sources using hybrid jobs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/how-to-hybrid-jobs/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Inspect data from external sources using hybrid jobs Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to use hybrid jobs and hybrid job triggers to inspect external data for sensitive information. To learn more about hybrid jobs and hybrid job triggers—including examples of hybrid environments—see [Hybrid jobs and hybrid job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs).

## Introduction to hybrid jobs and hybrid job triggers

Hybrid jobs and hybrid job triggers let you broaden the scope of protection that Sensitive Data Protection provides beyond [simple content inspection requests](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text) and [Google Cloud storage repository scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage). Using hybrid jobs and hybrid job triggers, you can stream data from virtually any source—including outside Google Cloud—directly to Sensitive Data Protection, and let Sensitive Data Protection inspect the data for sensitive information. Sensitive Data Protection automatically saves and aggregates the scan results for further analysis.

## Comparison of hybrid jobs and hybrid job triggers

When you create hybrid jobs, they run until you stop them. They accept all incoming data as long as the data is properly routed and formatted.

Hybrid job triggers work in a similar manner to hybrid jobs, but you don't need to explicitly stop a job within a hybrid job trigger. Sensitive Data Protection automatically stops jobs within hybrid job triggers at the end of each day.

In addition, with a hybrid job trigger, you can stop and start new jobs within the trigger without having to reconfigure your `hybridInspect` requests. For example, you can send data to a hybrid job trigger, then stop the active job, change its configuration, start a new job within that trigger, and then continue to send data to the same trigger.

For more guidance about which option fits your use case, see Typical hybrid inspection scenarios on this page.

## Definition of terms

This topic uses the following terms:

  * **External data** : data stored outside Google Cloud or data that Sensitive Data Protection doesn't natively support.

  * **Hybrid job** : an inspection job that is configured to scan data from virtually any source.

  * **Hybrid job trigger** : a job trigger that is configured to scan data from virtually any source.

  * **`hybridInspect` request**: a request that contains the external data that you want to inspect. When sending this request, you specify the hybrid job or hybrid job trigger to send the request to.




For general information about jobs and job triggers, see [Jobs and job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers).

## Hybrid inspection process

There are three steps in the hybrid inspection process.

  1. Choose the data that you want to send to Sensitive Data Protection.

The data can originate from within Google Cloud or outside it. For example, you can configure a custom script or application to send data to Sensitive Data Protection, enabling you to inspect data in flight, from another cloud service, an on-premises data repository, or virtually any other data source.

  2. Set up a hybrid job or hybrid job trigger in Sensitive Data Protection from scratch or using [an inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect).

After you set up a hybrid job or hybrid job trigger, Sensitive Data Protection actively listens for data sent to it. When your custom script or application sends data to this hybrid job or hybrid job trigger, the data is inspected and its results stored according to the configuration.

When you set up the hybrid job or hybrid job trigger, you can specify where you want to save or publish the findings. [Options](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) include saving to BigQuery and publishing notifications to Pub/Sub, Cloud Monitoring, or email.

  3. Send a `hybridInspect` request to the hybrid job or hybrid job trigger.

A `hybridInspect` request contains the data to be scanned. In the request, include metadata (also referred to as _labels_ and _table identifiers_) that describes the content and lets Sensitive Data Protection identify the information you want to track. For example, if you're scanning related data across several requests (such as rows in the same database table), you can use the same metadata in those related requests. You can then, collect, tally, and analyze findings for that database table.




As the hybrid job runs and inspects requests, inspection results are available when Sensitive Data Protection generates them. In contrast, actions, like Pub/Sub notifications, don't occur until your application ends the hybrid job.

**Note:** If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. [ ![Diagram depicting the hybrid job inspection process](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/how-to-hybrid-jobs.svg)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/how-to-hybrid-jobs.svg)

## Considerations

When working with hybrid jobs and job triggers, consider the following points:

  * Hybrid jobs and hybrid job triggers don't support filtering and sampling.
  * Jobs and job triggers aren't subject to service level objectives (SLO), but there are steps you can take to reduce latency. For more information, see [Job latency](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers#job-latency).



## Before you begin

Before setting up and using hybrid jobs or hybrid job triggers, be sure you've done the following:

### Create a new project, enable billing, and enable Sensitive Data Protection

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

  6. Enable the Sensitive Data Protection API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)




### Configure the data source

Before Sensitive Data Protection can inspect your data, you must send the data to Sensitive Data Protection. Regardless of what method you use to configure the hybrid job or hybrid job trigger, you must set up your external source to send data to the DLP API.

For information about the required format for hybrid inspection requests, see Hybrid content item formatting. For information about the types of metadata that you can include with the data in your request, see [Types of metadata you can provide](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs#types).

## Create a hybrid job or hybrid job trigger

To let Sensitive Data Protection inspect the data that you send to it, you must first set up a hybrid job or hybrid job trigger. For information about which one to create, see Typical hybrid inspection scenarios on this page.

### Console

In the Google Cloud console, go to the **Create job or job trigger** page:

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

The following sections describe how to fill in the sections of the **Create job or job trigger** page that are relevant to hybrid inspection operations.

### Choose input data

In this section, you specify the input data for Sensitive Data Protection to inspect.

  1. Optional: For **Name** , name the job by entering a value in the **Job ID** field. Leaving this field blank causes Sensitive Data Protection to auto-generate an identifier.
  2. Optional: From the **Resource location** menu, choose the region where you want to store the hybrid job or hybrid job trigger. For more information, see [Specifying processing locations](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location).
  3. For **Storage type** , select **Hybrid**.

  4. Optional: For **Description** , describe the hybrid job or hybrid job trigger that you're creating. For example, you can include information about the source of the data to be inspected.

  5. Optional: For **Required labels** , click **Add label** , and enter a label that you want to require from `hybridInspect` requests. A `hybridInspect` request that doesn't specify this label isn't processed by this hybrid job or hybrid job trigger. You can add up to 10 required labels. For more information, see Require labels from `hybridInspect` requests on this page.

  6. Optional: For **Optional labels** , enter any key-value pairs that you want to attach to the results of all `hybridInspect` requests sent to this job or job trigger. You can add up to 10 optional labels. For more information, see [Optional labels](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs#optional-labels).

  7. Optional: For **Tabular data options** , enter the field name of the primary key column if you plan to send tabular data in your `hybridInspect` requests. For more information, see [Tabular data options](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs#tabular-data-options).

  8. Click **Continue**.




### Configure detection

In this section, you specify the types of sensitive data that Sensitive Data Protection will inspect the input data for. Your choices are:

  * **Template** : If you've already [created a template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect) in the current project that you want to use to define the Sensitive Data Protection detection parameters, click the **Template name** field, and then choose the template from the list that appears.
  * **InfoTypes** : Sensitive Data Protection selects the most common built-in infoTypes to detect. To change the infoTypes, or to choose a custom infoType to use, click **Manage infoTypes**. You can also fine-tune the detection criteria in the **Inspection rulesets** and **Confidence threshold** sections. For more details, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#configure-detection).



After configuring detection parameters, click **Continue**.

### Add actions

For **Add actions** , select one or more actions for Sensitive Data Protection to take after the job completes. For more information, see [Enable inspection or risk analysis actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions). 

After you select actions, click **Continue**. 

### Schedule

This section is where you specify whether to create a single job that runs immediately or a job trigger that runs every time properly routed and formatted data is received by Sensitive Data Protection.

Do one of the following:

  * To run the hybrid job immediately, choose **None (run the one-off job immediately upon creation)**.

  * To configure the job so that data received from the source triggers the job, choose **Create a trigger to run the job on a periodic schedule**.

Hybrid job triggers aggregate API calls, letting you see finding results and trends over time.




For more information, see Comparison of hybrid jobs and hybrid job triggers.

### Review

You can review a JSON summary of the scan here. Be sure to note the name of the hybrid ob or hybrid job trigger; you need this information when sending data to Sensitive Data Protection for inspection.

After reviewing the JSON summary, click **Create**.

Sensitive Data Protection starts the hybrid job or hybrid job trigger immediately. An inspection scan is started when you send a `hybridInspect` request to this hybrid job or hybrid job trigger.

### API

A job is represented in the DLP API by the [`DlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. To create a hybrid job, you call the [`projects.locations.dlpJobs.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/create) method.

A job trigger is represented in the DLP API by the [`JobTrigger`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers) resource. To create a hybrid job trigger, you call the [`projects.locations.jobTriggers.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/create) method.

The `DlpJobs` or `JobTrigger` object that you create must have the following settings:

  1. In the `inspectJob` field, set an [`InspectJobConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig) object.
  2. In the `InspectJobConfig` object, in the `storageConfig` field, set a [`StorageConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#StorageConfig) object.
  3. In the `StorageConfig` object, in the `hybridOptions` field, set a [`HybridOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#HybridOptions) object. This object contains metadata about the data that you want to inspect.
  4. In the `InspectJobConfig` object, in the `actions` field, add any actions ([`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action)) that you want Sensitive Data Protection to perform at the end of each job.

The `publishSummaryToCscc` and `publishFindingsToCloudDataCatalog` actions aren't supported for this operation. For more information about actions, see [Actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions).

  5. Specify what to scan for and how to scan by doing one or both of the following:

     * Set the `inspectTemplateName` field to the full resource name of an inspection template that you want to use, if available.

     * Set the [`inspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) field.

If you set both `inspectTemplateName` and `inspectConfig` fields, their settings are combined.




### About the JSON examples

The following tabs contain JSON examples that you can send to Sensitive Data Protection to create a hybrid job or a hybrid job trigger. These hybrid job and hybrid job trigger examples are configured to do the following:

  * Process any `hybridInspect` request if the request has the label `appointment-bookings-comments`.
  * Scan the content in the `hybridInspect` request for email addresses.
  * Attach the `"env": "prod"` label to findings.
  * For tabular data, get the value of the cell in the `booking_id` column (the primary key) that's in the same row as the cell where the sensitive data was found. Sensitive Data Protection attaches this identifier to the finding, so that you can trace the finding to the specific row it came from.
  * Send an email when the job stops. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).
  * Send the findings to Cloud Monitoring when the job is stopped.



To view the JSON examples, see the following tabs.

### Hybrid job

This tab contains a JSON example that you can use to create a hybrid job.

To create a hybrid job, send a `POST` request to the following endpoint.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/dlpJobs
    

Replace the following:

  * PROJECT_ID: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) where you want to store the hybrid job.
  * REGION: the geographic [region](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location) where you want to store the hybrid job.



**JSON input**
    
    
    {
      "jobId": "postgresql-table-comments",
      "inspectJob": {
        "actions": [
          {
            "jobNotificationEmails": {}
          },
          {
            "publishToStackdriver": {}
          }
        ],
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "EMAIL_ADDRESS"
            }
          ],
          "minLikelihood": "POSSIBLE",
          "includeQuote": true
        },
        "storageConfig": {
          "hybridOptions": {
            "description": "Hybrid job for data from the comments field of a table that contains customer appointment bookings",
            "requiredFindingLabelKeys": [
              "appointment-bookings-comments"
            ],
            "labels": {
              "env": "prod"
            },
            "tableOptions": {
              "identifyingFields": [
                {
                  "name": "booking_id"
                }
              ]
            }
          }
        }
      }
    }
    

**JSON output**
    
    
    {
    "name": "projects/PROJECT_ID/locations/REGION/dlpJobs/i-postgresql-table-comments",
    "type": "INSPECT_JOB",
    "state": "ACTIVE",
    "inspectDetails": {
      "requestedOptions": {
        "snapshotInspectTemplate": {},
        "jobConfig": {
          "storageConfig": {
            "hybridOptions": {
              "description": "Hybrid job for data from the comments field of a table that contains customer appointment bookings",
              "requiredFindingLabelKeys": [
                "appointment-bookings-comments"
              ],
              "labels": {
                "env": "prod"
              },
              "tableOptions": {
                "identifyingFields": [
                  {
                    "name": "booking_id"
                  }
                ]
              }
            }
          },
          "inspectConfig": {
            "infoTypes": [
              {
                "name": "EMAIL_ADDRESS"
              }
            ],
            "minLikelihood": "POSSIBLE",
            "limits": {},
            "includeQuote": true
          },
          "actions": [
            {
              "jobNotificationEmails": {}
            },
            {
              "publishToStackdriver": {}
            }
          ]
        }
      },
      "result": {
        "hybridStats": {}
      }
    },
    "createTime": "JOB_CREATION_DATETIME",
    "startTime": "JOB_START_DATETIME"
    }
    

Sensitive Data Protection creates the hybrid job and generates a job ID. In this example, the job ID is `i-postgresql-table-comments`. Take note of the job ID. You need it in your `hybridInspect` request.

To stop a hybrid job, you must call the [`projects.locations.dlpJobs.finish`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish) method explicitly. The DLP API doesn't automatically stop hybrid jobs. In contrast, the DLP API automatically stops jobs within hybrid job triggers at the end of each day.

### Hybrid job trigger

This tab contains a JSON example that you can use to create a hybrid job trigger.

To create a hybrid job trigger, send a `POST` request to the following endpoint.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobTriggers
    

Replace the following:

  * PROJECT_ID: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) where you want to store the hybrid job trigger.
  * REGION: the geographic [region](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location) where you want to store the hybrid job trigger.



**JSON input**
    
    
    {
        "triggerId": "postgresql-table-comments",
        "jobTrigger": {
          "triggers": [
            {
              "manual": {}
            }
          ],
          "inspectJob": {
            "actions": [
              {
                "jobNotificationEmails": {}
              },
              {
                "publishToStackdriver": {}
              }
            ],
            "inspectConfig": {
              "infoTypes": [
                  {
                    "name": "EMAIL_ADDRESS"
                  }
              ],
              "minLikelihood": "POSSIBLE",
              "limits": {},
              "includeQuote": true
            },
            "storageConfig": {
              "hybridOptions": {
                "description": "Hybrid job trigger for data from the comments field of a table that contains customer appointment bookings",
                "requiredFindingLabelKeys": [
                    "appointment-bookings-comments"
                  ],
                "labels": {
                  "env": "prod"
                },
                "tableOptions": {
                  "identifyingFields": [
                    {
                      "name": "booking_id"
                    }
                  ]
                }
              }
            }
          }
        }
      }
    

**JSON output**
    
    
    {
    "name": "projects/PROJECT_ID/locations/REGION/jobTriggers/postgresql-table-comments",
    "inspectJob": {
      "storageConfig": {
        "hybridOptions": {
          "description": "Hybrid job trigger for data from the comments field of a table that contains customer appointment bookings",
          "requiredFindingLabelKeys": [
            "appointment-bookings-comments"
          ],
          "labels": {
            "env": "prod"
          },
          "tableOptions": {
            "identifyingFields": [
              {
                "name": "booking_id"
              }
            ]
          }
        }
      },
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "EMAIL_ADDRESS"
          }
        ],
        "minLikelihood": "POSSIBLE",
        "limits": {},
        "includeQuote": true
      },
      "actions": [
        {
          "jobNotificationEmails": {}
        },
        {
          "publishToStackdriver": {}
        }
      ]
    },
    "triggers": [
      {
        "manual": {}
      }
    ],
    "createTime": ""JOB_CREATION_DATETIME",
    "updateTime": "TRIGGER_UPDATE_DATETIME",
    "status": "HEALTHY"
    }
    

Sensitive Data Protection creates the hybrid job trigger. The output contains the name of the hybrid job trigger. In this example, that is `postgresql-table-comments`. Take note of the name. You need it in your `hybridInspect` request.

Unlike with hybrid jobs, the DLP API automatically stops jobs within hybrid job triggers at the end of each day. Thus, you don't need to explicitly call the [`projects.locations.dlpJobs.finish`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish) method.

When creating a hybrid job or hybrid job trigger, you can use the APIs Explorer on the following API reference pages, respectively:

  * [`projects.locations.dlpJobs.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/create)
  * [`projects.locations.jobTriggers.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/create)



In the **Request parameters** field, enter `projects/PROJECT_ID/locations/REGION`. Then, in the **Request body** field, paste the sample JSON for the object you're trying to create.

A successful request, even one created in APIs Explorer, creates a hybrid job or hybrid job trigger.

For general information about using JSON to send requests to the DLP API, see the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api).

## Send data to the hybrid job or hybrid job trigger

To inspect data, you must send a `hybridInspect` request, in the correct format, to either a hybrid job or hybrid job trigger.

### Hybrid content item formatting

The following is a simple example of a `hybridInspect` request sent to Sensitive Data Protection for processing by a hybrid job or hybrid job trigger. Note the structure of the JSON object, including the `hybridItem` field, which contains the following fields:

  * `item`: contains the actual content to inspect.
  * `findingDetails`: contains metadata to associate with the content.


    
    
    {
      "hybridItem": {
        "item": {
          "value": "My email is test@example.org"
        },
        "findingDetails": {
          "containerDetails": {
            "fullPath": "10.0.0.2:logs1:app1",
            "relativePath": "app1",
            "rootPath": "10.0.0.2:logs1",
            "type": "logging_sys",
            "version": "1.2"
          },
          "labels": {
            "env": "prod",
            "appointment-bookings-comments": ""
          }
        }
      }
    }
    

For comprehensive information about the contents of hybrid inspection items, see the API reference content for the [`HybridContentItem` object](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/HybridContentItem).

### Hybrid inspection endpoints

For data to be inspected using a hybrid job or hybrid job trigger, you must send a `hybridInspect` request to the correct endpoint.

**HTTP method and URL for hybrid jobs**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/dlpJobs/JOB_ID:hybridInspect
    

For more information about this endpoint, see the API reference page for the [`projects.locations.dlpJobs.hybridInspect` method](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/hybridInspect).

**HTTP method and URL for hybrid job triggers**
    
    
    https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobTriggers/TRIGGER_NAME:hybridInspect
    

For more information about this endpoint, see the API reference page for the [`projects.locations.jobTriggers.hybridInspect` method](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/hybridInspect).

Replace the following:

  * PROJECT_ID: your [project identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * REGION: the geographical [region](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location) where you want to store the `hybridInspect` request. This region must be the same as the hybrid job's region.
  * JOB_ID: the ID that you gave the hybrid job, prefixed with `i-`.

To look up the job ID, in [Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7), click **Inspection > Inspect jobs**.

  * TRIGGER_NAME: the name that you gave the hybrid job trigger.

To look up the name of the job trigger, in [Sensitive Data Protection](https://console.cloud.google.com/security/sensitive-data-protection;source=7), click **Inspection > Job triggers**.




## Require labels from `hybridInspect` requests

If you want to control which `hybridInspect` requests can be processed by a hybrid job or hybrid job trigger, you can set required labels. Any `hybridInspect` requests for that hybrid job or hybrid job trigger that don't include these required labels are rejected.

To set a required label, do the following:

  1. When creating the hybrid job or hybrid job trigger, set the `requiredFindingLabelKeys` field to a list of required labels.

The following example sets `appointment-bookings-comments` as a required label in a hybrid job or hybrid job trigger.
         
         "hybridOptions": {
           ...
           "requiredFindingLabelKeys": [
             "appointment-bookings-comments"
           ],
           "labels": {
             "env": "prod"
           },
           ...
         }
         

  2. In the [`hybridInspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/how-to-hybrid-jobs#sending-data) request, in the `labels` field, add each required label as a key in a key-value pair. The corresponding value can be an empty string.

The following example sets the required label, `appointment-bookings-comments`, in a `hybridInspect` request.
         
         {
           "hybridItem": {
             "item": {
               "value": "My email is test@example.org"
             },
             "findingDetails": {
               "containerDetails": {...},
               "labels": {
                 "appointment-bookings-comments": ""
               }
             }
           }
         }
         




If you don't include the required label in your `hybridInspect` request, you get an error like the following:
    
    
    {
      "error": {
        "code": 400,
        "message": "Trigger required labels that were not included: [appointment-bookings-comments]",
        "status": "INVALID_ARGUMENT"
      }
    }
    

## Code sample: Create a hybrid job trigger and send data to it

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    
    public class SendDataToTheHybridJobTrigger
    {
        public static DlpJob SendToHybridJobTrigger(
           string projectId,
           string jobTriggerId,
           string text = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the hybrid finding details which will be used as metadata with the content.
            // Refer to this for more information: https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Container
            var findingDetails = new [HybridFindingDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridFindingDetails.html)
            {
                ContainerDetails = new [Container](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Container.html)
                {
                    FullPath = "10.0.0.2:logs1:aap1",
                    RelativePath = "app1",
                    RootPath = "10.0.0.2:logs1",
                    Type = "System Logs"
                }
            };
    
            // Construct the hybrid content item using the finding details and text to be inspected.
            var hybridContentItem = new [HybridContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridContentItem.html)
            {
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text ?? "My email is ariel@example.org and name is Ariel." },
                FindingDetails = findingDetails
            };
    
            var jobTriggerName = new [JobTriggerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName.html)(projectId, jobTriggerId);
    
            // Construct the request to activate the Job Trigger.
            var activate = new [ActivateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ActivateJobTriggerRequest.html)
            {
                JobTriggerName = jobTriggerName
            };
    
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) triggerJob = null;
    
            try
            {
                // Call the API to activate the trigger.
                triggerJob = dlp.ActivateJobTrigger(activate);
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html))
            {
                [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest.html) listJobsRequest = new [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest.html)
                {
                    ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                    Filter = $"trigger_name={jobTriggerName}"
                };
    
                PagedEnumerable<ListDlpJobsResponse, DlpJob> res = dlp.ListDlpJobs(listJobsRequest);
                foreach ([DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) j in res)
                {
                    triggerJob = j;
                }
            }
    
            // Construct the request using hybrid content item.
            var request = new [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectJobTriggerRequest.html)
            {
                HybridItem = hybridContentItem,
                JobTriggerName = jobTriggerName
            };
    
            // Call the API.
            [HybridInspectResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectResponse.html) _ = dlp.HybridInspectJobTrigger(request);
    
            Console.WriteLine($"Hybrid job created successfully. Job name: {triggerJob.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html#Google_Cloud_Dlp_V2_DlpJob_Name)}");
    
            return triggerJob;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectDataToHybridJobTrigger uses the Data Loss Prevention API to inspect sensitive
    // information using Hybrid jobs trigger that scans payloads of data sent from
    // virtually any source and stores findings in Google Cloud.
    func inspectDataToHybridJobTrigger(w io.Writer, projectID, textToDeIdentify, jobTriggerName string) error {
    	// projectId := "your-project-id"
    	// jobTriggerName := "your-job-trigger-name"
    	// textToDeIdentify := "My email is test@example.org"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: textToDeIdentify,
    		},
    	}
    
    	// Contains metadata to associate with the content.
    	// Refer to https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#container for specifying the paths in container object.
    	container := &dlppb.Container{
    		Type:         "logging_sys",
    		FullPath:     "10.0.0.2:logs1:app1",
    		RelativePath: "app1",
    		RootPath:     "10.0.0.2:logs1",
    		Version:      "1.2",
    	}
    
    	// Set the required label.
    	labels := map[string]string{
    		"env":                           "prod",
    		"appointment-bookings-comments": "",
    	}
    
    	hybridFindingDetails := &dlppb.HybridFindingDetails{
    		ContainerDetails: container,
    		Labels:           labels,
    	}
    
    	hybridContentItem := &dlppb.HybridContentItem{
    		Item:           contentItem,
    		FindingDetails: hybridFindingDetails,
    	}
    
    	// Activate the job trigger.
    	activateJobreq := &dlppb.ActivateJobTriggerRequest{
    		Name: jobTriggerName,
    	}
    
    	dlpJob, err := client.ActivateJobTrigger(ctx, activateJobreq)
    	if err != nil {
    		log.Printf("Error from return part %v", err)
    		return err
    	}
    	// Build the hybrid inspect request.
    	req := &dlppb.HybridInspectJobTriggerRequest{
    		Name:       jobTriggerName,
    		HybridItem: hybridContentItem,
    	}
    
    	// Send the hybrid inspect request.
    	_, err = client.HybridInspectJobTrigger(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	getDlpJobReq := &dlppb.GetDlpJobRequest{
    		Name: dlpJob.Name,
    	}
    
    	var result *dlppb.DlpJob
    	for i := 0; i < 5; i++ {
    		// Get DLP job
    		result, err = client.GetDlpJob(ctx, getDlpJobReq)
    		if err != nil {
    			fmt.Printf("Error getting DLP job: %v\n", err)
    			return err
    		}
    
    		// Check if processed bytes is greater than 0
    		if result.GetInspectDetails().GetResult().GetProcessedBytes() > 0 {
    			break
    		}
    
    		// Wait for 5 seconds before checking again
    		time.Sleep(5 * time.Second)
    		i++
    	}
    
    	fmt.Fprintf(w, "Job Name: %v\n", result.Name)
    	fmt.Fprintf(w, "Job State: %v\n", result.State)
    
    	inspectionResult := result.GetInspectDetails().GetResult()
    	fmt.Fprint(w, "Findings: \n")
    	for _, v := range inspectionResult.GetInfoTypeStats() {
    		fmt.Fprintf(w, "Infotype: %v\n", v.InfoType.Name)
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetCount())
    	}
    
    	fmt.Fprint(w, "successfully inspected data using hybrid job trigger ")
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html);
    import com.google.privacy.dlp.v2.[HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html);
    import com.google.privacy.dlp.v2.[HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html);
    import com.google.privacy.dlp.v2.[ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html);
    
    public class InspectDataToHybridJobTrigger {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The job trigger id used to for processing a hybrid job trigger.
        String jobTriggerId = "your-job-trigger-id";
        // The string to de-identify.
        String textToDeIdentify = "My email is test@example.org and my name is Gary.";
        inspectDataToHybridJobTrigger(textToDeIdentify, projectId, jobTriggerId);
      }
    
      // Inspects data using a hybrid job trigger.
      // Hybrid jobs trigger allows to scan payloads of data sent from virtually any source for
      // sensitive information and then store the findings in Google Cloud.
      public static void inspectDataToHybridJobTrigger(
          String textToDeIdentify, String projectId, String jobTriggerId) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Contains metadata to associate with the content.
          // Refer to https://cloud.google.com/dlp/docs/reference/rest/v2/Container for specifying the
          // paths in container object.
          [Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html) container =
              [Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html).newBuilder()
                  .[setFullPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setFullPath_java_lang_String_)("10.0.0.2:logs1:app1")
                  .[setRelativePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setRelativePath_java_lang_String_)("app1")
                  .[setRootPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setRootPath_java_lang_String_)("10.0.0.2:logs1")
                  .setType("logging_sys")
                  .setVersion("1.2")
                  .build();
    
          [HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html) hybridFindingDetails =
              [HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html).newBuilder().[setContainerDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.Builder.html#com_google_privacy_dlp_v2_HybridFindingDetails_Builder_setContainerDetails_com_google_privacy_dlp_v2_Container_)(container).build();
    
          [HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html) hybridContentItem =
              [HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html).newBuilder()
                  .setItem(contentItem)
                  .[setFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.Builder.html#com_google_privacy_dlp_v2_HybridContentItem_Builder_setFindingDetails_com_google_privacy_dlp_v2_HybridFindingDetails_)(hybridFindingDetails)
                  .build();
    
          // Activate the job trigger.
          [ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html) activateJobTriggerRequest =
              [ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html).newBuilder()
                  .setName([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                  .build();
    
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob;
    
          try {
            dlpJob = dlpClient.activateJobTrigger(activateJobTriggerRequest);
          } catch ([InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) e) {
            [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html) request =
                [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html).newBuilder()
                    .setParent([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                    .setFilter("trigger_name=" + [JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                    .build();
    
            // Retrieve the DLP jobs triggered by the job trigger
            [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).[ListDlpJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListDlpJobsPagedResponse.html) response = dlpClient.listDlpJobs(request);
            dlpJob = response.getPage().getResponse().getJobs(0);
          }
    
          // Build the hybrid inspect request.
          [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html) request =
              [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html).newBuilder()
                  .setName([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                  .setHybridItem(hybridContentItem)
                  .build();
    
          // Send the hybrid inspect request.
          dlpClient.hybridInspectJobTrigger(request);
    
          // Build a request to get the completed job
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) getDlpJobRequest =
              [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
    
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) result = null;
    
          do {
            result = dlpClient.getDlpJob(getDlpJobRequest);
            Thread.sleep(5000);
          } while (result.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult().getProcessedBytes() <= 0);
    
          System.out.println("Job status: " + result.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          // Parse the response and process results.
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) inspectionResult = result.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : inspectionResult.getInfoTypeStatsList()) {
            System.out.println("\tInfoType: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount() + "\n");
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
    const dlpClient = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // The string to de-identify
    // const string = 'My email is test@example.org';
    
    // Job Trigger ID
    // const jobTriggerId = 'your-job-trigger-id';
    
    async function inspectDataToHybridJobTrigger() {
      // Contains metadata to associate with the content.
      const container = {
        full_path: '10.0.0.2:logs1:app1',
        relative_path: 'app1',
        root_path: '10.0.0.2:logs1',
        type: 'logging_sys',
        version: '1.2',
      };
    
      const labels = {env: 'prod', 'appointment-bookings-comments': ''};
    
      // Build the hybrid content item.
      const hybridContentItem = {
        item: {value: string},
        findingDetails: {
          containerDetails: container,
          labels,
        },
      };
      let jobName;
      const fullTriggerName = `projects/${projectId}/jobTriggers/${jobTriggerId}`;
      // Activate the job trigger.
      try {
        const response = await dlpClient.activateJobTrigger({
          name: fullTriggerName,
        });
        jobName = response[0].name;
      } catch (err) {
        console.log(err);
        if (err.code === 3) {
          const response = await dlpClient.listDlpJobs({
            parent: fullTriggerName,
            filter: `trigger_name=${fullTriggerName}`,
          });
          jobName = response[0][0].name;
        }
        // Ignore error related to job trigger already active
        if (err.code !== 3) {
          console.log(err.message);
          return;
        }
      }
      // Build the hybrid inspect request.
      const request = {
        name: `projects/${projectId}/jobTriggers/${jobTriggerId}`,
        hybridItem: hybridContentItem,
      };
      // Send the hybrid inspect request.
      await dlpClient.hybridInspectJobTrigger(request);
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlpClient.getDlpJob({name: jobName});
    
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Check if the job has completed.
        if (job.inspectDetails.result.processedBytes > 0) {
          break;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
      // Finish the job once the inspection is complete.
      await dlpClient.finishDlpJob({name: jobName});
    
      // Print out the results.
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.length > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectDataToHybridJobTrigger();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Dlp\V2\ActivateJobTriggerRequest;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\Container;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\HybridContentItem;
    use Google\Cloud\Dlp\V2\HybridFindingDetails;
    use Google\Cloud\Dlp\V2\HybridInspectJobTriggerRequest;
    use Google\Cloud\Dlp\V2\ListDlpJobsRequest;
    
    /**
     * Inspect data hybrid job trigger.
     * Send data to the hybrid job or hybrid job trigger.
     *
     * @param string $callingProjectId  The Google Cloud project id to use as a parent resource.
     * @param string $string            The string to inspect (will be treated as text).
     */
    
    function inspect_send_data_to_hybrid_job_trigger(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $jobTriggerId,
        string $string
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $content = (new ContentItem())
            ->setValue($string);
    
        $container = (new Container())
            ->setFullPath('10.0.0.2:logs1:app1')
            ->setRelativePath('app1')
            ->setRootPath('10.0.0.2:logs1')
            ->setType('logging_sys')
            ->setVersion('1.2');
    
        $findingDetails = (new HybridFindingDetails())
            ->setContainerDetails($container)
            ->setLabels([
                'env' => 'prod',
                'appointment-bookings-comments' => ''
            ]);
    
        $hybridItem = (new HybridContentItem())
            ->setItem($content)
            ->setFindingDetails($findingDetails);
    
        $parent = "projects/$callingProjectId/locations/global";
        $name = "projects/$callingProjectId/locations/global/jobTriggers/" . $jobTriggerId;
    
        $triggerJob = null;
        try {
            $activateJobTriggerRequest = (new ActivateJobTriggerRequest())
                ->setName($name);
            $triggerJob = $dlp->activateJobTrigger($activateJobTriggerRequest);
        } catch (ApiException $e) {
            $listDlpJobsRequest = (new ListDlpJobsRequest())
                ->setParent($parent)
                ->setFilter('trigger_name=' . $name);
            $result = $dlp->listDlpJobs($listDlpJobsRequest);
            foreach ($result as $job) {
                $triggerJob = $job;
            }
        }
        $hybridInspectJobTriggerRequest = (new HybridInspectJobTriggerRequest())
            ->setName($name)
            ->setHybridItem($hybridItem);
    
        $dlp->hybridInspectJobTrigger($hybridInspectJobTriggerRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($triggerJob->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() != JobState::RUNNING) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    import google.cloud.dlp
    
    
    def inspect_data_to_hybrid_job_trigger(
        project: str,
        trigger_id: str,
        content_string: str,
    ) -> None:
        """
        Uses the Data Loss Prevention API to inspect sensitive information
        using Hybrid jobs trigger that scans payloads of data sent from
        virtually any source and stores findings in Google Cloud.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            trigger_id: The job trigger identifier for hybrid job trigger.
            content_string: The string to inspect.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `item` to inspect.
        item = {"value": content_string}
    
        # Construct the container details that contains metadata to be
        # associated with the content. For more details, please refer to
        # https://cloud.google.com/dlp/docs/reference/rest/v2/Container
        container_details = {
            "full_path": "10.0.0.2:logs1:app1",
            "relative_path": "app1",
            "root_path": "10.0.0.2:logs1",
            "type_": "logging_sys",
            "version": "1.2",
        }
    
        # Construct hybrid inspection configuration.
        hybrid_config = {
            "item": item,
            "finding_details": {
                "container_details": container_details,
                "labels": {
                    "env": "prod",
                    "appointment-bookings-comments": "",
                },
            },
        }
    
        # Convert the trigger id into a full resource id.
        trigger_id = f"projects/{project}/jobTriggers/{trigger_id}"
    
        # Activate the job trigger.
        dlp_job = dlp.[activate_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_activate_job_trigger)(request={"name": trigger_id})
    
        # Call the API.
        dlp.[hybrid_inspect_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_hybrid_inspect_job_trigger)(
            request={
                "name": trigger_id,
                "hybrid_item": hybrid_config,
            }
        )
    
        # Get inspection job details.
        job = dlp.get_dlp_job(request={"name": dlp_job.name})
    
        # Wait for dlp job to get finished.
        while job.inspect_details.result.processed_bytes <= 0:
            time.sleep(5)
            job = dlp.get_dlp_job(request={"name": dlp_job.name})
    
        # Print the results.
        print(f"Job name: {dlp_job.name}")
        if job.inspect_details.result.info_type_stats:
            for finding in job.inspect_details.result.info_type_stats:
                print(f"Info type: {finding.info_type.name}; Count: {finding.count}")
        else:
            print("No findings.")
    
    

## Typical hybrid inspection scenarios

The following sections describe typical uses for hybrid inspection and their corresponding workflows.

### Perform a one-off scan

Execute a one-off scan of a database outside of Google Cloud as part of a quarterly spot check of databases.

  1. Create a hybrid job using the Google Cloud console or the DLP API.

  2. Send data to the job by calling [`projects.locations.dlpJobs.hybridInspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/hybridInspect). If you want to inspect more data, repeat this step as many times as needed.

  3. After sending data for inspection, call the [`projects.locations.dlpJobs.finish`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish) method.

Sensitive Data Protection performs the actions specified in your `projects.locations.dlpJobs.create` request.




### Configure continuous monitoring

Monitor all new content added daily to a database that Sensitive Data Protection does not natively support.

  1. Create a hybrid job trigger using the Google Cloud console or the DLP API.

  2. Activate the job trigger by calling the [`projects.locations.jobTriggers.activate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/activate) method.

  3. Send data to the job trigger by calling [`projects.locations.jobTriggers.hybridInspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/hybridInspect). If you want to inspect more data, repeat this step as many times as needed.




In this case, you don't need to call the `projects.locations.dlpJobs.finish` method. Sensitive Data Protection auto-partitions the data that you send. As long as the job trigger is active, at the end of each day, Sensitive Data Protection performs the actions you specified when you created your hybrid job trigger.

### Scan data coming into a database

Scan data coming into a database, while controlling how the data is partitioned. Each job in a job trigger is a single partition.

  1. Create a hybrid job trigger using the Google Cloud console or the DLP API.

  2. Activate the job trigger by calling the [`projects.locations.jobTriggers.activate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/activate) method.

The system returns the job ID of a single job. You need this job ID in the next step.

  3. Send data to the job by calling [`projects.locations.dlpJobs.hybridInspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/hybridInspect).

In this case, you send the data to the job instead of the job trigger. This approach lets you control how the data that you send for inspection is partitioned. If you want to add more data for inspection in the current partition, repeat this step.

  4. After sending data to the job, call the [`projects.locations.dlpJobs.finish`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish) method.

Sensitive Data Protection performs the actions specified in your `projects.locations.jobTriggers.create` request.

  5. If you want to create another job for the next partition, activate the job trigger again, and then send the data to the resulting job.




### Monitor traffic from a proxy

Monitor traffic from a proxy installed between two custom applications.

  1. Create a hybrid job trigger using the Google Cloud console or the DLP API.

  2. Activate the job trigger by calling the [`projects.locations.jobTriggers.activate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/activate) method.

  3. Send data to the job trigger by calling [`projects.locations.jobTriggers.hybridInspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/hybridInspect). If you want to inspect more data, repeat this step as many times as needed.

You can call this request indefinitely for all network traffic. Make sure you include [metadata](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs#types) in each request.




In this case, you don't need to call the `projects.locations.dlpJobs.finish` method. Sensitive Data Protection auto-partitions the data that you send. As long as the job trigger is active, at the end of each day, Sensitive Data Protection performs the actions you specified when you created your hybrid job trigger.

## What's next

  * Learn more about how [hybrid jobs and hybrid job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs) work.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
