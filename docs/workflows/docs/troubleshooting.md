---
url: https://docs.cloud.google.com/workflows/docs/troubleshooting/
title: Troubleshoot issues \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:47.481640+00:00
---

# Troubleshoot issues  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues that you might encounter when using Workflows.

For more information, refer to [monitoring](https://docs.cloud.google.com/workflows/docs/monitor) and [debugging](https://docs.cloud.google.com/workflows/docs/debug) Workflows.

## Deployment errors

When a workflow is deployed, Workflows checks that the source code is free from errors and matches the [language syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax). Workflows returns an error if one is found. The most common types of deployment errors are:

  * Referencing an undefined variable, step, or subworkflow
  * Incorrect syntax 
    * Incorrect indentation
    * Missing or extraneous `{`, `}`, `"`, `-`, or `:`



For example, the following source code throws a deployment error because the return statement references an undefined variable, `varC`:
    
    
    - step1:
        assign:
        - varA: "Hello"
        - varB: "World"
    - step2:
        return: ${varC + varB}

This incorrect source code is used in the following Google Cloud console and gcloud CLI examples.

### Console

When a deployment error occurs, Workflows displays the error message in a banner on the **Edit workflow** page: ![Deployment error](https://docs.cloud.google.com/workflows/images/deployment-error.png) The error message flags the problem in the source code, specifying the origin of the error when possible:
    
    
    Could not deploy workflow: failed to build: error in step step2: error
    evaluating return value: symbol 'varC' is neither a variable nor a
    sub-workflow name (Code: 3)
    

### gcloud

When you run the `gcloud workflows deploy` command, Workflows returns an error message to the command line if the deployment fails. The error message flags the problem in the source code, specifying the origin of the error when possible:
    
    
    ERROR: (gcloud.workflows.deploy) [INVALID_ARGUMENT] failed to build:
    error in step step2: error evaluating return value: symbol 'varC' is neither
    a variable nor a sub-workflow name
    

To resolve the issue, edit the workflow's source code. In this case, refer to `varA` instead of `varC`.

## HTTP `403` service account permission errors

Your workflow execution fails when an HTTP server responds with an error code of `403`. For example:
    
    
    Permission 'iam.serviceaccounts.actAs' denied on service
    account PROJECT_NUMBER-compute@developer.gserviceaccount.com (or it may not exist).

or
    
    
    SERVICE_ACCOUNT does not have storage.objects.create access to the Google Cloud
    Storage object. Permission 'storage.objects.create' denied on resource (or it may not exist).

Every workflow is associated with an IAM service account at the time the workflow is created. To resolve this issue, you must grant the service account one or more IAM roles that contain the minimum permissions required to manage your workflow. For example, if you want to let your workflow send logs to Cloud Logging, make sure the service account executing the workflow has been granted a role that includes the `logging.logEntries.create` permission. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

## HTTP `404 No such object` or `Not found` errors

When using the [Cloud Storage connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/Overview), your workflow execution fails when an HTTP server responds with an error code of `404`. For example:
    
    
    HTTP server responded with error code 404
    in step "read_input_file", routine "main", line: 13
    {
      "body": "Not Found",
      "code": 404,
      ...
    }

You should URL-encode object names to be path safe. You can use the [`url_encode`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode) and [`url_encode_plus`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode_plus) functions to encode applicable characters when they appear in either the object name or query string of a request URL. For example:
    
    
    - init:
        assign:
            - source_bucket: "my-bucket"
            - file_name: "my-folder/my-file.json"
    - list_objects:
        call: googleapis.storage.v1.objects.get
        args:
            bucket: ${source_bucket}
            object: ${text.url_encode(file_name)}
            alt: media
        result: r
    - returnStep:
        return: ${r}

If you don't url-encode your object name and your storage bucket has [folders](https://docs.cloud.google.com/storage/docs/folders), the request will fail. For more information, see [Encoding URL path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding) and [Cloud Storage naming considerations](https://docs.cloud.google.com/storage/docs/objects#naming).

## HTTP `429 Too many requests` errors

There is a [maximum number](https://docs.cloud.google.com/workflows/quotas#quotas) of active workflow executions that can run concurrently. Once this quota is exhausted, and if execution backlogging is disabled, or if the quota for backlogged executions is reached, any new executions fail with an HTTP `429 Too many requests` status code.

Execution backlogging lets you queue workflow executions once the concurrent executions quota is reached. By default, execution backlogging is enabled for all requests (including those triggered by Cloud Tasks) with the following exceptions:

  * When creating an execution using an [`executions.run`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1/projects.locations.workflows.executions/run) or [`executions.create`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1/projects.locations.workflows.executions/create) connector in a workflow, execution backlogging is disabled by default. You can configure it by explicitly setting the execution's `disableConcurrencyQuotaOverflowBuffering` field to `false`.
  * For executions triggered by Pub/Sub, execution backlogging is disabled and _can't_ be configured.



For more information, see [Manage execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#manage_execution_backlogging).

You can also [enable a Cloud Tasks queue to execute child workflows](https://docs.cloud.google.com/workflows/docs/tutorials/buffer-workflows-executions) at a rate that you define and achieve a better execution rate; in that case, you might want to explicitly [disable execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#disable_execution_backlogging).

## Cross-project service account permission errors

If you receive a `PERMISSION_DENIED` error when attempting to use a cross-project service account to deploy a workflow, ensure that the `iam.disableCrossProjectServiceAccountUsage` boolean constraint is not enforced for your project and that you have correctly set up the service account. For more information, see [Deploy a workflow with a cross-project service account](https://docs.cloud.google.com/workflows/docs/authentication#deploy_a_workflow_with_a_cross-project_service_account).

## Resource name must conform to RFC 1123

Your workflow execution fails when an HTTP server responds with an error code of `400`. For example:
    
    
    "description": "must conform to RFC 1123: only lowercase, digits, hyphens,
    and periods are allowed, must begin and end with letter or digit, and less
    than 64 characters."

To resolve this issue, make sure that your resource name follows the DNS label standard as defined in [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123), and that when assigning variables, you are concatenating [strings](https://docs.cloud.google.com/workflows/docs/reference/syntax/strings) and [expressions](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions) correctly.

For example, you can't assign a variable like this: `- string: hello-${world}`. Instead, do the following:

### YAML
    
    
      - assign_vars:
          assign:
              - string: "hello"
              - string: ${string+" "+"world"}

### JSON
    
    
      [
        {
          "assign_vars": {
            "assign": [
              {
                "string": "hello"
              },
              {
                "string": "${string+" "+"world"}"
              },
            ]
          }
        }
      ]

## Expressions containing colons

In YAML, expressions containing colons can cause unexpected behaviour when the colon is interpreted as defining a map. Although it can be possible to deploy and execute the workflow, the output won't be as expected.

If creating a workflow using the Google Cloud console, the workflow can't be visually rendered in the Google Cloud console, and you might receive a warning similar to the following:

![Workflow creation warning](https://docs.cloud.google.com/workflows/images/string-parsing-warning.png)

You can resolve this issue by wrapping the YAML expression in single quotes:

Recommended: `'${"a: " +string(a)}'`

Not recommended: `${"a: " +string(a)}`

## Map keys using non-alphanumeric characters

When accessing map keys with non-alphanumeric characters (for example, the exclamation point in `"special!key": value`), you must wrap the key name in quotes. If the key name is not wrapped in quotes, the workflow can't be deployed. For example, if you try to deploy the following source code, a `token recognition error` is thrown:
    
    
    - init:
        assign:
        - var:
            key:
                "special!key": bar
    - returnOutput:
        return: '${"foo" + var.key[special!key]}'

To resolve this, use the following code instead to return the output:

`'${"foo" + var.key["special!key"]}'`

## Multiple expressions in a list

Using multiple expressions inside a list like the following [iteration range](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-range) example is not valid YAML:

`[${rangeStart}, ${rangeEnd}])`

You can resolve this issue by doing one of the following:

  * Place the list inside an expression:

`${[rangeStart, rangeEnd]}`

  * Wrap each expression in single quotes:

`['${rangeStart}', '${rangeEnd}']`




The result is then a list of two values, as expected.

## Customer-managed encryption keys (CMEK)

You might encounter errors when using Cloud KMS with Workflows. The following table describes different issues and how to resolve them.

Issue | Description  
---|---  
Permission `cloudkms.cryptoKeyVersions.useToEncrypt` is denied | Either the provided Cloud KMS key does not exist or the permission is not properly configured. Solution: 

  * Check that the Cloud KMS key exists. [List the keys for a specified key ring](https://docs.cloud.google.com/workflows/docs/use-cmek#retrieve-id) and [verify its usage](https://docs.cloud.google.com/workflows/docs/use-cmek#verify-cmek).
  * Ensure that the Workflows service agent has [ access to the key](https://docs.cloud.google.com/workflows/docs/use-cmek#key-access) and has been granted the `cloudkms.cryptoKeyEncrypterDecrypter` role.

  
Key version is not enabled | The provided Cloud KMS key version has been disabled. Solution: [Re-enable the Cloud KMS key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable).  
Key ring region does not match the resource to be protected | The provided KMS key ring region is different from the region of the workflow. Solution: Use a Cloud KMS key ring and protected workflow from the same region. (Note that they can be in different projects.) For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) and [Workflows locations](https://docs.cloud.google.com/workflows/docs/locations).   
Cloud KMS quota limit is exceeded | Your quota limit for Cloud KMS requests has been reached. Solution: Limit the number of Cloud KMS calls or increase the quota limit. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).  
  
## Requested entity not found when using the Cloud Run connector

Your workflow execution fails when an HTTP server responds with an error code of `404` when trying to use the connector method, [`googleapis.run.v1.namespaces.jobs.create`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/create).

This method requires that you specify the location of the HTTP endpoint. For example, `us-central1` or `asia-southeast1`. If you don't specify a location, the global endpoint `https://run.googleapis.com` is used; however, this location supports list methods only.

To resolve this issue, make sure to specify a `location` argument when [calling the connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call). For Cloud Run Admin API location options, see [service endpoints](https://docs.cloud.google.com/run/docs/reference/rest#service-endpoint).

## Resource limits

If you encounter [resource limits](https://docs.cloud.google.com/workflows/quotas#resource_limits) or an error such as `ResourceLimitError`, `MemoryLimitExceededError` or `ResultSizeLimitExceededError`, you can free memory by [clearing variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#clear). For example, you might want to free up memory that is needed for subsequent steps. Or, you might have calls with results you don't care about, and you can omit those results altogether.

## YAML indentation

YAML indentation is meaningful and should be at least two spaces per indentation level. Insufficient indentation can cause errors, and a new level should be at least two spaces in from the _start of the text_ in the previous line. 

For example, the following incorrectly specifies a list item containing a map with `stepName` and `call` items:
    
    
    - stepName:
      call: sys.log

Instead, you should indent the subsequent line by two spaces to nest `call` within `stepName`:
    
    
    - stepName:
        call: sys.log

Make sure that you use spaces, rather than tab characters, to indent lines.

## What's next

  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
