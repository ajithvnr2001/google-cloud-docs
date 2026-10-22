---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with/
title: Working with environment groups \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:18.770783+00:00
---

# Working with environment groups  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Working with environment groups Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes how to create and edit environment groups, which includes adding environments or host names to a group, or removing them, with Apigee. For more information about what an environment group is and how it works, see [Environments and environment group overview](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview).

## Creating environment groups

You can create new environment groups using the Apigee UI or the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). This section describes how to do both.

When you first create an environment group, it does not contain any environments. It does, however, define a default hostname: example.group-name. To add environments to an environment group, see Adding environments to an environment group.

**Apigee hybrid users:** Every environment group you create with an attached environment must be included in all override files where the environment is used.

### Apigee UI

To create a new environment group in the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, select **Environment Groups**.
  3. Click **\+ Create Environment Group**.
  4. Enter the following: 
     * **Environment group name** : A name for the environment group. The name must start and end with an alphanumeric character. It can have up to 63 characters consisting of alphanumeric characters and hyphens. The name must be different from any existing environment group name in your organization.
  5. **Hostnames** : A list of host names that can be used to call proxies. Each host name must be on a separate line.

**Note:** The names assigned to an environment group must be unique to that group: they can't be used by other environment groups.

You also have the option to click **Configure Google Load Balancer with these domains**. This opens the **Load balancing** page in the Cloud console, where you can configure load balancing for the host names.

  6. **Environments** : An optional list of environments to include in the environment group.
  7. Click **Create**.

**Note:** This operation may take up to five minutes to complete.

### Apigee API

To create a new environment group using the Apigee API, send a `POST` request to the [Create environment groups API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create). Before calling the API, be sure that you have a valid token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).

The following example `curl` command shows the syntax to create a new group:
    
    
    curl -i $TOKEN -X POST \
      https://apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups?name=new-group-name

When specifying the new group's name, you must use only lower case letters, numbers, and hyphens (`a-z`, `A-Z`, and `-`). You cannot use upper case letters or any special characters other than hyphens. You must also start the name with a lower case letter.

If you don't specify any additional parameters, this command creates a new group with no host names assigned to it.

You can also assign host names when you create the group by specifying them as an array in the body of the request.

The following example creates a new group `my-group` and assigns three new host names to the new group:
    
    
    curl -i $TOKEN -X POST \
      https://apigee.googleapis.com/v1/organizations/org_name/envgroups?name=my-group \
      -d '{ \
        "hostnames": ["server1.mycompany.com", "server2.mycompany.com", "10.1.142.8"] \
      }'

You can later change the host names in the list by sending a `PATCH` request to the [Patch environment groups API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/patch).

## Adding environments to an environment group

Environments that are not in a group cannot be accessed because there is no host name associated with them. Host names are defined on the environment group, not the environment. When you create an environment using the Apigee UI in Google Cloud console, you have the option to assign the environment to an existing environment group. For more information, see [ Creating a new environment in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#creating-a-new-environment-in-the-ui).

If you did not assign your environment to a group during environment creation, this section describes how to add an unassigned environment to an environment group using the Apigee UI or the Apigee API.

### Apigee UI

To add an environment to an environment group in the Apigee UI:

  1. Create the environment, as described in [Creating environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#create).
  2. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  3. In the **Environments** pane, select **Environment Groups**.
  4. In the environment group row, click  more_vert **Actions** , and select **Edit**.
  5. In the **Edit Environment Group** pane, under **Environments (Optional)** , select the environment you want to add to the environment group.
  6. Click **Update**.

**Note:** This operation may take up to five minutes to complete.

### Apigee API

To add a new environment to an environment group using the Apigee API, send a `POST` request to the [Environment group attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments), as the following example shows:
    
    
    curl -H "Authorization: Bearer $TOKEN" -X POST
      "https://apigee.googleapis.com/v1/organizations/my-org/envgroups/test-group/attachments"
      -d '{
        "name": "my-attachment",
        "environment": "test"
      }'

Where:

  * `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).
  * The body of the request contains the name of the attachment as well as the name of the new environment.



The body of the request contains an instance of an [EnvironmentGroupAttachment resource](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments#EnvironmentGroupAttachment), which is a simple wrapper around a single environment.

If successful, the response contains details about the new attachment, including the timestamp at which it was created; for example:
    
    
    {
      "name": "my-attachment",
      "environment": "test"
      "createdAt": "42"
    }

## Removing an environment from an environment group

You can remove an environment from an environment group with the Apigee UI or the Apigee API.

### Apigee UI

To remove an environment from an environment group in the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, select **Environment Groups**.
  3. In the environment group row, click  more_vert **Actions** , and select **Edit**.
  4. In the **Edit Environment Group** pane, under **Environments (Optional)** , deselect the environment you want to remove from the environment group.
  5. Click **Update**.

**Note:** This operation may take up to five minutes to complete.

### Apigee API

To remove an environment from an environment group using the Apigee API, use the `delete` method in the [ EnvironmentGroupAttachment](https://cloud.devsite.corp.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments) resource to delete the attachment corresponding to the environment.

## Deleting an environment group

You can delete an environment group using either the Apigee UI or the API.

### Apigee UI

To delete an environment group in the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, select **Environment Groups**.
  3. In the environment group row, click  more_vert **Actions** , and select **Edit**.

**Note:** This operation may take up to five minutes to complete.

### Apigee API

To delete an environment group using the Apigee API, use the `delete` method in the [ EnvironmentGroup](https://cloud.devsite.corp.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups) resource.

## Adding host names to a group

When you create a group, Apigee adds the default hostname `example.GROUP_NAME`. You can add your host names to the group using the instructions in this section.

The hostnames that you define on an environment group:

  * Must be unique across all environment groups in an organization; they cannot be used by more than one group
  * Do not support wildcards
  * Base paths must be unique within a host (no two proxies can have the same base path within a host)



### Apigee UI

To add a host name to an environment group in the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, select **Environment Groups**.
  3. In the environment group row, click  more_vert **Actions** , and select **Edit**.
  4. In the **Edit Environment Group** pane, under **Hostnames** , enter the host name name you want to add to the environment group.
  5. Click **Update**.

**Note:** This operation may take up to five minutes to complete.

### Apigee API

To add host names to an environment group using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest), send a `PATCH` request to the [Patch environment groups API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/patch). Be sure to set the `updateMask` parameter to `hostnames` and specify the entire list of host names that you want: the value of that field in your request _replaces_ the existing list.

The following example sets the host names for the test environment:
    
    
    curl -H "Authorization: Bearer $TOKEN" -X PATCH
      "https://apigee.googleapis.com/v1/organizations/my-org/envgroups/test-group?updateMask=hostnames"
      -d '{
        "name": "my-hostnames",
        "hostnames": [
          "test-1.example.com",
          "test-2.example.com",
          "test-3.example.com"
        ]
      }'

Where:

  * `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).
  * The payload of the request specifies a name for the array of hostname attachments, plus the array of names themselves.



If the request was successful, the response contains an [Operation resource](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations#Operation).

### Determining whether the Cloud Load Balancer is configured for a hostname

You can call a proxy with the following command:
    
    
    curl -v https://YOUR_ENV_GROUP_HOSTNAME/myproxy

where `YOUR_ENV_GROUP_HOSTNAME` is the hostname of an environment group that contains the environment in which the proxy is deployed. To do so, the [Cloud Load Balancer](https://cloud.google.com/load-balancing/docs/load-balancing-overview) must be configured for the environment group hostname. Usually, the Load Balancer is configured when Apigee is first [provisioned](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). To determine whether the Load Balancer is configured for the hostname:

  1. In the Google Cloud console, go to the **Apigee Management > Environments > Environment Groups** page.

[Go to Environment Groups](https://console.cloud.google.com/apigee/environments/groups)

  2. Click more_vert **More** , edit**Edit** next to an environment group. 
  3. Click **Configure Google Load Balancer with these domains** This opens the Google Cloud Platform Load balancing page. 

![Load balancing page in the Google Cloud Platform](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/cloud-load-balancer.png)

  4. Click the name of the load balancer in the **Name** column. If Apigee was provisioned with the [Provisioning Wizard](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview), the name of the load balancer will be `apigee-proxy-url-map`. If you don't see that name, contact the system administrator in your organization who provisioned Apigee.

When you click the name, the **Load balancer details** page is displayed:

![Load balancer details page in the Google Cloud Platform](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/load-balancer-details.png)

  5. In the **Frontend** table, click an SSL certificate in the **Certificate** column and look for an SSL certificate that matches the hostname: 
     * If the **Certificate type** is **MANAGED** , check whether the **DNS Hostnames** field of the certificate matches the hostname.
     * If the certificate is not managed, you may need to download the certificate and check whether its Common Name matches the hostname.



If you don't find the hostname in any certificate, contact your system administrator for further assistance. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
