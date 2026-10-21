---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group/
title: Virtual host missing environment group \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:20.866383+00:00
---

# Virtual host missing environment group  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Virtual host missing environment group Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

An `ApigeeIssue` with `Reason` `AIS_VIRTUALHOST_MISSING_ENVGROUP` is shown when viewing resources in the `apigee` namespace. 

## Error messages

After running `kubectl -n apigee get apigeeissues`, the following error is displayed: 
    
    
    NAME                     SEVERITY   REASON                             DOCUMENTATION                                                                                  AGE
    vhost-missing-eg-my-eg   ERROR      AIS_VIRTUALHOST_MISSING_ENVGROUP   https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group   5h18m

## Cause: Virtualhost missing environment group

One of the `virtualhosts` defined in `overrides.yaml` is missing its corresponding `EnvironmentGroup`. 

### Diagnosis

Run the following command: 
    
    
    kubectl -n apigee describe apigeeissue ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-eg-my-eg`. 

Something similar to the following is returned: 
    
    
    Name:         vhost-missing-eg-my-eg
    Namespace:    apigee
    Labels:       ais-reason=AIS_VIRTUALHOST_MISSING_ENVGROUP
    Annotations:  <none>
    API Version:  apigee.cloud.google.com/v1alpha1
    Kind:         ApigeeIssue
    Metadata:
      Creation Timestamp:  2023-04-05T14:29:38Z
      Generation:          1
      Managed Fields:
        API Version:  apigee.cloud.google.com/v1alpha1
        Fields Type:  FieldsV1
        fieldsV1:
          f:spec:
            .:
            f:details:
            f:documentation:
            f:reason:
            f:severity:
        Manager:         apigeewatcher
        Operation:       Update
        Time:            2023-04-05T14:29:38Z
      Resource Version:  28195
      UID:               f7b62eb3-3f84-4a37-9ba8-9a0e1e9c3454
    Spec:
      Details:        Expected EnvironmentGroup "my-eg" in ApigeeOrganization "my-org" for ApigeeRouteConfig "my-org-my-eg"
      Documentation:  https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-env-group
      Reason:         AIS_VIRTUALHOST_MISSING_ENVGROUP
      Severity:       ERROR
    Events:           <none>
    
    
    Spec:
      Details:        Expected EnvironmentGroup "my-eg" in ApigeeOrganization "my-org" for ApigeeRouteConfig "my-org-my-eg"

The contents of `Spec.Details` explains the name of the `EnvironmentGroup` that is expected to exist. 

### Resolution

  1. Use the `describe ApigeeIssue` command to display the name of the `EnvironmentGroup` which is expected to exist: 
         
         kubectl -n apigee describe apigeeissues ISSUE_NAME

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-eg-my-eg`. 

In this example, the environment group `my-eg` is expected in the `my-org` Apigee organization. 

  2. Use one of the following methods to correct the problem: 
     1. Create the environment group: 
        1. [Create an environment group](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#groups).
        2. [Add an environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#adding).
        3. [Create a proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy).
        4. [Deploy a proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) to that environment.
     2. Delete the environment group: 
        1. Open `overrides.yaml` in a text editor.
        2. Delete the removed environment group from the `virtualhosts`.
        3. Save the `overrides.yaml` file.
        4. Reapply the `overrides.yaml` file using the [Helm command](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 

Dry run:
               
               helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
                 --namespace APIGEE_NAMESPACE \
                 --atomic \
                 --set envgroup=ENV_GROUP \
                 -f overrides.yaml \
                 --dry-run=server
               

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Your installation may or may not have been set up using an ENV_GROUP_RELEASE_NAME that differs from ENV_GROUP. For information on the settings, see [Install Apigee hybrid using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-helm-charts).

Install the chart:
               
               helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
                 --namespace APIGEE_NAMESPACE \
                 --atomic \
                 --set envgroup=ENV_GROUP \
                 -f overrides.yaml
               

Retry and verify that the error message is no longer returned.




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The `Spec.Details` field of the `ApigeeIssue`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
