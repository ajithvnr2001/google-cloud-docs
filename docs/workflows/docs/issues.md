---
url: https://docs.cloud.google.com/workflows/docs/issues/
title: Known issues for Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:56.426089+00:00
---

# Known issues for Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Known issues for Workflows Stay organized with collections  Save and categorize content based on your preferences. 

Unexpected behaviors, operational limitations, and available workarounds can affect your Workflows executions and connectors. You can also check for existing issues or open new issues in the [public issue trackers](https://docs.cloud.google.com/support/docs/issue-trackers).

## Placement of `for` directly after `try`

Placing `for` directly after `try` causes an error. For example, a single step can be placed directly after `try`, like this:
    
    
    - try:
        try:
          call: sys.log
          args:
            data: works
        retry: ${http.default_retry}

However, if you position `for` after the `try`, the step fails, and you cannot deploy the workflow. For example:
    
    
    - try:
        **try :**
          **for :**
            value: v
            range: [1,2]
            steps:
              - log:
                  call: sys.log
                  args:
                    data: ${v}
        retry: ${http.default_retry}

The error message is as follows:

`Could not deploy workflow: failed to build: error in step try: loop step name should not be empty (Code: 3)`

The workaround is to add a named step after the `try`. For example:
    
    
    - try:
        try:
          **steps :**
            **- loopStep:**
                **for :**
                  value: v
                  range: [1,2]
                  steps:
                    - log:
                        call: sys.log
                        args:
                          data: ${v}
        retry: ${http.default_retry}

## Events larger than the maximum arguments size

If using Workflows as a destination for an Eventarc trigger, events larger than the maximum Workflows arguments size will fail to trigger workflow executions. For more information, see [Quotas and limits](https://docs.cloud.google.com/workflows/quotas).

## `HTTP request lost` message in logs

When executing a workflow that calls Cloud Build, your workflow fails and there is an `HTTP request lost` message in the logs similar to the following:
    
    
    [1500] HTTP request lost
    INTERNAL MESSAGE: HTTP request lost
    ...
    CAUSED BY:
    RPC::UNREACHABLE: RPC connection timed out: FDD 20s, last read 2022-10-14 16:39:04 -0700 PDT

If you encounter this error, try modifying your workflow by implementing either a [retry policy](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying) or through explicit [exception handling](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors#try-retry-except).

## Call logging and `accessString` method to retrieve secret data

If the [call logging level](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) is set to `log-all-calls` when [using the `accessString` helper method to retrieve secret data](https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/projects.secrets.versions/accessString), the secret value is not redacted, and is printed in plain text to the logs in `jsonPayload.succeeded.response`.

## Long-running operation exception when using Cloud Resource Manager connector

The Resource Manager connector method, [`googleapis.cloudresourcemanager.v3.projects.patch`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/projects/patch), doesn't return a long-running operation (LRO) name. Even for a successful request, an exception similar to the following might be raised:
    
    
    exception: "{"message":"Long-running operation returned unexpected response.",
    "operation":{"done":true,"response":{"@type":"type.googleapis.com/google.cloud.resourcemanager.v3.Project",
    ...
    "tags":["ResponseTypeError"]}"

To avoid an LRO polling error, set the `skip_polling` connector parameter to `true` so that the connector invocation call is non-blocking if the initial request succeeds. A successful request returns `"done":true`; otherwise, to catch any exceptions use a [`try/except` structure](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors). For more information, see the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

## HTTP requests to Google Kubernetes Engine (GKE)

Every GKE cluster has a control plane that handles Kubernetes API requests. The control plane has two kinds of endpoints for cluster access: _DNS-based endpoints_ and _IP-based endpoints_. For more information, see [Control plane access](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#control-plane-access).

Workflows no longer supports [HTTP requests](https://docs.cloud.google.com/workflows/docs/http-requests) to the [IP-based endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#ipendpointsconfig) of GKE cluster control planes. For more information about the scope and impact of this deprecation, see the [service announcement](https://docs.cloud.google.com/workflows/docs/service-announcements#2025-01-28).

To ensure that your workflow functions as expected, you must access [DNS-based endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#dnsendpointconfig). To access the DNS-based endpoints, we recommend that you use the Kubernetes API connector in a workflow. For more information, see [Access Kubernetes API objects using a connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api).

## What's next

Learn strategies helpful when [troubleshooting issues](https://docs.cloud.google.com/workflows/docs/troubleshooting). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
