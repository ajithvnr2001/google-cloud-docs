---
url: https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto/
title: Setting up context-aware access with Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:45.625327+00:00
---

# Setting up context-aware access with Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Setting up context-aware access with Identity-Aware Proxy Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to extend Identity-Aware Proxy (IAP) access policies using [access levels](https://docs.cloud.google.com/access-context-manager/docs) and the [Identity and Access Management (IAM) Conditions Framework](https://docs.cloud.google.com/iam/docs/conditions-overview). Access levels allow access restrictions to resources based on IP address and end-user device attributes. IAM conditions allow access restrictions based on URL hosts, paths, date, and time.

For example, depending on the policy configuration, your sensitive app can:

  * Grant access to all employees if they're using a trusted corporate device from your corporate network.
  * Grant access to employees in the **Remote Access** group if they're using a trusted corporate device with a secure password and up-to-date patch level, from any network.
  * Only grant access to employees in the **Privileged Access** group if the URL path starts with `/admin`. 



## Before you begin

Before you begin, you'll need the following:

  * A IAP-secured app to which you want to add individual or group access.
  * User or group names that you want to grant access to.



## Set up an access level

To limit access based on [IP address](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#corporate-network-example) or [end-user device attributes](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#device-example), create an access level. Some attributes, such as device attributes, require a Chrome Enterprise Premium license. License validation only occurs when you configure access levels and does not affect runtime access. To learn how to create an access level, see the [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) guide. IAP uses the access level name to associate it with a IAP-secured app. 

The use of scoped policies is not supported by IAP. Access levels must be set in the organizational access policy. For more information, see [Create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy#scoped-access-policy).

## Edit the IAM policy

A IAP-secured app has an IAM policy that binds the IAP role to the app.

By adding an [IAM conditional binding](https://docs.cloud.google.com/iam/docs/conditions-overview) to the IAM policy, access to your resources is further restricted based on [request attributes](https://docs.cloud.google.com/iam/docs/conditions-overview#request_attributes). These request attributes include:

  * Access levels
  * URL Host/Path
  * Date/Time



Note that request values being compared to `request.host` and `request.path` specified in an IAM conditional binding must be exact. For example, if you restrict access to paths starting with `/internal admin`, one can bypass the restriction by going to `/internal%20admin`. For more information about hostname and path conditions, see Use hostname and path conditions.

Add and edit conditional bindings on your IAM policy by following the process below.

###  Console 

To add a conditional binding using the Google Cloud console:

  1. Go to the [IAP admin page](https://console.cloud.google.com/security/iap). 

[Go to the IAP admin page](https://console.cloud.google.com/security/iap)

  2. Select the checkbox next to the resources that you want to update IAM permissions for.

  3. On the right side **Info panel** , click **Add principal**.

  4. In the **New principal** box, enter the principals that you want to assign a role to.

  5. In the **Select a role** drop-down list, select the **IAP-secured Web App User** role and specify access level conditions that the principals will need to meet to access the resource.

     * To specify existing access levels, select them from the **Access levels** drop-down list. You need to select the **IAP-secured Web App User** role and have organization level permissions to view existing access levels. You must be [granted](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) one of the following roles: 
       * Access Context Manager Admin
       * Access Context Manager Editor
       * Access Context Manager Reader
     * To create and manage access levels, use the [Access Context Manager](https://console.cloud.google.com/projectselector/security/access-level).
  6. If you want to add more roles to the principals, click **Add another role**.

  7. When you're finished adding roles, click **Save**.

You have now added a conditional binding to your resource.




To remove a conditional binding:

  1. Go to the [IAP admin page](https://console.cloud.google.com/security/iap). 

[Go to the IAP admin page](https://console.cloud.google.com/security/iap)

  2. Select the checkbox next to the resource that you want to remove a principal's IAM role from.

  3. On the right side **Info panel** , under **Role / Principal** , click the role that you want to remove from the principal.

  4. Click **Remove** next to the principal. ![](https://docs.cloud.google.com/iap/images/remove.png)

  5. On the **Remove role from principal** dialog that appears, click **Remove**. To remove all non-inherited roles from the principal on the selected resource, select the checkbox before clicking **Remove**.




###  gcloud 

At this time, you can only use the gcloud tool to set project-level conditional bindings.

To set conditional bindings, edit your project's `policy.yaml` file by following the process below:

  1. Open the IAM policy for the app using the following gcloud command: 
         
         gcloud iap web get-iam-policy --project=PROJECT_ID > policy.yaml

  2. Edit the `policy.yaml` file to specify the following:

     * The users and groups you want to apply the IAM condition to.
     * The `iap.httpsResourceAccessor` role to grant them access to the resources.
     * The IAM condition.

The following snippet shows an IAM condition with only one attribute specified. This condition grants access to the user and group if the ACCESS_LEVEL_NAME access level requirements are met and the resource URL path starts with `/`.
    
    bindings:
    ...
      - members:
        - group:EXAMPLE_GROUP@GOOGLE.COM
        - user:EXAMPLE_USER@GOOGLE.COM
        role: roles/iap.httpsResourceAccessor
        condition:
                  expression: "accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME" in
                              request.auth.access_levels && request.path.startsWith("/")
                  title: CONDITION_TITLE
    ...

  3. Bind the policy to the application using the `set-iam-policy` command. 
         
         gcloud iap web set-iam-policy --project=PROJECT_ID policy.yaml




Your IAM policy now includes a conditional binding.

###  API 

To edit your app's `policy.json` file, follow the process below for your app type. See [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_via_the_api) for more information about using the IAM API to manage access policies.

Before doing the application-specific API steps below, export the following variables:
    
    
     export PROJECT_NUM=PROJECT_NUMBER
     export IAP_BASE_URL=https://iap.googleapis.com/v1/projects/${PROJECT_NUM}/iap_web
     # Replace POLICY_FILE.JSON with the name of JSON file to use for setIamPolicy
     export JSON_NEW_POLICY=POLICY_FILE.JSON
     

### App Engine 
    
    
     1. Export the following App Engine variables:
     <pre class="devsite-click-to-copy prettyprint lang-html" suppresswarning="suppresswarning">
     \# The APP_ID is usually the project ID
     export GAE_APP_ID=<var>APP_ID</var>
     export GAE_BASE_URL=${IAP_BASE_URL}/appengine-${GAE_APP_ID}</pre>
    
     1. Get the IAM policy for the App Engine app using the `getIamPolicy` method. The empty data bit at the end turns the `curl` request into POST instead of GET.
    
    
    
    curl -i -H "Authentication: Bearer $(gcloud auth print-access-token)" \\
        ${GAE_BASE_URL}/:getIamPolicy -d ''

1\. Add your IAM conditional binding to the IAM policy JSON file. The following is an example of an edited `policy.json` file that binds the `iap.httpsResourceAccessor` role to two users, granting them access to the IAP-secured resources. An IAM condition has been added to grant them access to the resources only if the ACCESS_LEVEL_NAME access level requirement is met and the resource URL path starts with `/`. Each binding can have only one condition.  
  
**Example policy.json file** 
    
    
    {
    "policy": {
      "bindings": [
            {
              "role": "roles/iap.httpsResourceAccessor",
              "members": [
                  "group:EXAMPLE_GROUP@GOOGLE.COM",
                  "user:EXAMPLE_USER@GOOGLE.COM"
              ],
              "condition": {
                "expression": "\"accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME\" in request.auth.access_levels && request.path.startsWith(\"/\")",
                "title": "CONDITION_NAME"
              }
            }
            ]
      }
    }

1\. Set your new `policy.json` file using the `setIamPolicy` method. 
    
    
     curl -i -H "Authentication: Bearer $(gcloud auth print-access-token)" \\
         ${GAE_BASE_URL}:setIamPolicy -d @${JSON_NEW_POLICY}

#### App Engine services and versions
    
    
     You can also update the IAM policy of a App Engine
     service, all versions, or a specific version of a service. To do this for a specific version of a service:
    
     1. Export the following additional variables.
    
    
    
        export GAE_SERVICE=SERVICE_NAME
        export GAE_VERSION=VERSION_NAME
        

1\. Update the exported GAE_BASE_URL variable. 
    
    
    export GAE_BASE_URL=${IAP_BASE_URL}/appengine-${GAE_APP_ID}/services/${GAE_SERVICE}/versions/${GAE_VERSION}

1\. Get and set the IAM policy for the version using the `getIamPolicy` and `setIamPolicy` commands shown above. 

### GKE and Compute Engine

1\. Export the project ID of your backend service. 
    
    
         export BACKEND_SERVICE_NAME=BACKEND_SERVICE_NAME
    
    
     2. Get the IAM policy for the Compute Engine app using the `getIamPolicy` method. The empty data bit at the end turns the `curl` request into POST instead of GET.
     <pre class="devsite-click-to-copy prettyprint lang-html" suppresswarning="suppresswarning">
     curl -i -H "Authentication: Bearer $(gcloud auth print-access-token)" \\
         ${IAP_BASE_URL}/compute/services/${BACKEND_SERVICE_NAME}:getIamPolicy \\
         -d ''</pre>
     3. Add your IAM conditional binding to the IAM policy JSON file.
        The following is an example of an edited `policy.json` file that binds the
        `iap.httpsResourceAccessor` role to two users, granting them access to the IAP-secured resources. An IAM
        condition has been added to grant them access to the resources only if the <var>ACCESS_LEVEL_NAME</var> access level requirement is met and the resource URL path starts with `/`.
        Each binding can have only one condition.
    
        <br/>**Example policy.json file**
    
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "roles/iap.httpsResourceAccessor",
            "members": [
              "group:EXAMPLE_GROUP@GOOGLE.COM",
              "user:EXAMPLE_USER@GOOGLE.COM"
            ],
            "condition": {
              "expression": "\"accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME\" in request.auth.access_levels && request.path.startsWith(\"/\")",
              "title": "CONDITION_NAME"
            }
          }
        ]
      }
    }

4\. Set your new `policy.json` file using the `setIamPolicy` method. 
    
    
         curl -i -H "Content-Type:application/json" \\
                 -H "Authentication: Bearer $(gcloud auth print-access-token)" \\
                 ${IAP_BASE_URL}/compute/services/${BACKEND_SERVICE_NAME}:setIamPolicy \\
                 -d @${JSON_NEW_POLICY}

## Use hostname and path conditions

Access to your app can be secured using the hostname and path of a request URL. For example, the `request.path.startsWith` IAM condition can be used to only grant access to employees in the **Privileged Access** group if the URL path starts with `/admin`.

For more information about using hostname and path conditions, see [request attributes](https://docs.cloud.google.com/iam/docs/conditions-overview#request_attributes).

### String normalization

A URL has a hostname and path. For example, the URL `https://sheets.google.com/create?query=param` has a hostname of `sheets.google.com` and a path of `/create`.

Backends can interpret hostnames and paths in different ways. To remove ambiguity, IAP normalizes hostname and path strings when checking policies.

IAP performs two policy checks when a request has a non-normalized path. If the non-normalized path passes the policy check, IAP normalizes the path and a second policy check is performed. Access is granted if both the non-normalized and normalized paths pass the policy check.

For example, if a request has the path `/internal;some_param/admin`, IAP first performs a policy check on the non-normalized path (`/internal`). If that passes, IAP performs a second policy check on the normalized path (`/internal/admin`).

#### Hostnames

Hostnames are normalized by:

  * Removing trailing dots
  * Lowercasing characters
  * Converting to ASCII



Hostnames that include non-ASCII characters are further normalized with punycoding. You need to punycode your hostname string for a match to be made.

To punycode your hostname string, use a converter like [Punycoder](https://www.punycoder.com/).

The following are examples of normalized hostnames:

  * `FOO.com` is normalized to `foo.com`
  * `café.fr` is normalized to `xn--caf-dma.fr`



#### Paths

Paths are normalized by:

  * Removing path params
  * Resolving relative paths to their absolute equivalent



A path param includes all characters from a `;` to either the next `/` or the end of the path.

Requests that contain `..;` at the beginning of a path section are considered invalid. For example, `/..;bar/` and `/bar/..;/` return the `HTTP 400: Bad Request` error.

The following are examples of normalized paths:

  * `/internal;some_param/admin` is normalized to `/internal/admin`
  * `/a/../b` is normalized to `/b`
  * `/bar;param1/baz;baz;param2` is normalized to `/bar/baz`



### Subdomain endings

A policy set with `request.host.endsWith("google.com")` will match to both `sub_domain.google.com` and `testgoogle.com`. If your goal is to limit your policy to all subdomains the end with `google.com`, set your policy to `request.host.endsWith(".google.com")`.

Note that setting your policy to `request.host.endsWith(".google.com")` will match with `sub_domain.google.com` but won't match with `google.com` due to the additional `.`.

## Cloud Audit Logs and access levels

[Enabling Cloud Audit Logs](https://docs.cloud.google.com/iap/docs/audit-log-howto) for your IAP-secured project lets you see authorized and unauthorized access requests. View requests and all the [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) a requester has met by completing the following steps: 

  1. Go to the Google Cloud console [ Logs Explorer](https://console.cloud.google.com/logs/query) for your project.   
[ Go to the logs page](https://console.cloud.google.com/logs/query)
  2. On the **resource selector** drop-down list, select a resource. IAP-secured HTTPS resources are under **App Engine Application** and **Compute Engine Backend Service**. IAP-secured SSH and TCP resources are under **Compute Engine VM instance** . 
  3. On the **logs type** drop-down list, select **data_access**. 
     * The **data_access** log type only appears if there was traffic to your resource after you enabled Cloud Audit Logs for IAP. 
  4. Click to expand the date and time of the access you want to review. 
     * Authorized access has a blue `i` icon.
     * Unauthorized access has an orange `!!` icon.
  5. View the access levels the requester has met by clicking to expand sections until you reach `protoPayload` > `requestMetadata` > `requestAttributes` > `auth` > `accessLevels`. 



Note that all access levels that a user has met are visible when viewing a request, including access levels that weren't required to access it. Viewing an unauthorized request doesn't indicate what access levels weren't met. This is determined by comparing the conditions on the resource to the access levels visible on the request. 

See the [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) guide for more information about logs. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
