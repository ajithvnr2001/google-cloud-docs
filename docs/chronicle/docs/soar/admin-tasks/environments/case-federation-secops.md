---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops/
title: Enable federated access \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:45.144426+00:00
---

# Enable federated access  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable federated access

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

The case management federation feature lets secondary customers have their own separate Google Security Operations platform, rather than having their Google SecOps instance operating as environments within a shared instance. This setup is ideal for Managed Security Service Providers (MSSPs) or enterprises that require independent platforms across geographic regions.

All case metadata is synchronized from the secondary (remote) platform to the primary provider's platform as follows:

  * Primary platform analysts can view, access, and act on federated cases if they've been granted access.
  * Secondary customers retain control over which environments and cases are accessible to the primary platform.



When a primary platform analyst opens a remote case link, the system redirects them to the remote platform, if they have the necessary permissions to access the case's environment. On the remote platform, the primary platform analyst can sign in with their email and password. Access requires valid credentials and is granted for the current session only.

## Add secondary platform access for primary platform users

To assign access to one or more remote (secondary) platforms, follow these steps:

  1. In the primary platform, go to **SOAR Settings** > **Advanced** > **Group Mapping**.
  2. Add or edit users, as needed. For more information on how to add users, see [Map users in the SecOps platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).
  3. In the **Platform** field, select as many remote platforms as needed.
  4. Click **Save**.



## Register a new secondary platform on the primary platform

To register a secondary platform, you need an Admin API key for the primary platform and to carry out an API call to generate a sync API key.

Create a new Admin API key if you don't already have one by following these steps, or you can read more about [managing API keys](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-api-keys):

  1. Go to **SOAR Settings > Advanced > API keys**.
  2. Create a new Admin API key.



Generate the sync API key by following these steps:

  1. Execute the following API call, where the variable `$PRIMARY_INSTANCE_URL` is the root URL of your primary SOAR instance, for example `https://primaryinstance.siemplify-soar.com`, and the value for `"host"`. In the data payload, set the "host" value to your secondary SOAR instance, without the `https` prefix (for example `mysecondary.siemplify-soar.com`).
         
         curl --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms" \
         --header 'Content-Type: application/json' \
         --header "AppKey: $ADMIN_API_KEY" \
         --data '{
         "displayName": "My Secondary Platform",
         "host": "mysecondary.siemplify-soar.com"
         }'
         

This returns a sync API key which is unique per secondary platform and used to authenticate to the primary platform.




## Set up metadata sync on the secondary (remote) platform

To enable synchronization on the secondary platform, complete the following steps on the secondary SecOps instance.

### Download the Case Federation integration

To download the Case Federation integration, follow these steps:

  1. In the platform, go to the **Content Hub**.
  2. Select the **Response Integrations** tab and search for **Case Federation**.
  3. Click the **Case Federation integration configuration** and then click **Save**. Don't select the **Is Primary** checkbox.
  4. Go to **Response** > **Job Scheduler** , and then click add**Add**.
  5. In the **Job Name** field, select **Case Federation Sync Job**.
  6. In the **Integration** field, select **Case Federation**.
  7. Click **Create**.
  8. In the **Target Platform** field, enter the hostname of the primary provider. The hostname is the platform URL without the `https://` prefix (for example, `primaryinstance.siemplify-soar.com`).
  9. In the **API key** field, enter the sync API key you created previously.
  10. Set the default sync time to one minute.
  11. Click **Save**.



### Grant access to primary users

This procedure lets you grant permissions to specific environments for the relevant primary platform personas. This lets the primary analyst pivot to the relevant cases in the secondary platform.

To create or edit a user on the secondary platform, follow these steps:

  1. In the secondary platform, go to **SOAR Settings > Advanced > IAM Role Mapping**.
  2. Add or edit users, as needed. For more information on how to add or edit users, see [Map users in the Google SecOps platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).
  3. In the **Environment** field, select the environments that primary platform analysts can access.
  4. Click **Save**.



## Access remote cases from the primary platform

Primary platform users can view remote cases either in the list view or side-by-side view on the **Cases** page.

To open cases on the remote platform, follow these steps:

  1. On the **Cases** page, select either **list view** or the **side-by-side view**.
  2. Do any one of the following:

     * **Side-by-side view**
       1. In the case queue, look for cases marked with an "R" (for remote).
       2. Click a remote case to open it in the corresponding remote platform.
     * **List view**
       1. Locate remote cases in the **Platform** column.
       2. Click the **case ID** to open the case in the remote platform.
  3. Sign in to the remote platform with your email and password.

If you can't sign in, it means that the secondary customer may not have granted you access to the case's source environment.




## List secondary platforms

You can list secondary platforms from the primary platform by running the following command, which returns a list of platform names and IDs:
    
    
    curl --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms/{platform_id}" \
          --header 'Content-Type: application/json' \
          --header "AppKey: $ADMIN_API_KEY"
    

## Delete secondary platforms

You can delete secondary platforms from the primary platform by running the following command:
    
    
    curl -X DELETE --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms/{platform_id}" \
          --header "AppKey: $ADMIN_API_KEY"
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
