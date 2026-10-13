---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee/
title: Step 7: Deploy to an Apigee environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:02.683454+00:00
---

# Step 7: Deploy to an Apigee environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 7: Deploy to an Apigee environment Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

After you complete local development and testing with Apigee in VS Code, you are ready to deploy your API as an archive to an Apigee environment. In this step, you'll create an Apigee environment that supports archive deployment and deploy an archive of your API proxy configuration to the Apigee environment.

**Before you begin** : Install Google Cloud SDK and the `gcloud beta apigee` component, as described in [Getting started using gcloud with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started). 

  1. Follow the steps in [Create an environment](https://cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-environment) to perform the following: 
     1. Create a new **dev** environment in your Apigee organization, enabling **Archive** as the deployment type. Use the [UI](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#creating-a-new-environment-in-the-ui) or [API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create). 
     2. Attach the environment to a runtime instance using the [Instances attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments).

This command triggers a long-running operation. Ensure that the environment has been attached to the runtime before continuing. 

     3. Create an environment group if you do not already have one using the [Create environment groups API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create).

Ensure that the environment group has been created before continuing. You can check the status of your new group using a request like the following:
            
            curl -i -H "$AUTH" -H "Content-Type:application/json" \
              "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/ENVIRONMENT_NAME"

     4. Attach the new environment to the environment group using the [Environment group attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments). 

Attaching an environment to the group makes the proxies in that environment routable via the hostnames in the group. This triggers a long-running operation that can take several minutes to complete. We recommend that you wait a minute or two before continuing to the next step. In the meantime you can check the status of the operation as before.

  2. Deploy an archive of your API proxy configuration to the Apigee environment. 
     1. In the **Terminal** tab in Apigee VS Code, navigate to the **myapigeeworkspace** directory. 
            
            cd myapigeeworkspace

When you run `ls` the directory should contain the `src` folder. 

     2. Run the following command: 
            
            gcloud beta apigee archives deploy --environment=dev --labels=release=052021

The following provides an example of the response: 
            
            Using Apigee organization dev
            Waiting for operation [b64c2665-b5ac-43cc-9e2d-232e8895c2ed] to complete...done

  3. Run the following command in the **Terminal** tab to test your API: 
         
         curl https://INTERNAL_LOAD_BALANCER_IP/helloworld /
           -H "Host: ENV_GROUP_HOSTNAME" 

For more information about the variables in this example and how to set up API access, see [Deploy a sample proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample). 

The following error message is displayed: 
         
         {"fault":{"faultstring":"Failed to resolve API Key variable request.queryparam.apikey",
           "detail":{"errorcode":"steps.oauth.v2.FailedToResolveAPIKey"}}}
         

You need to create an API product that includes the `helloworld` API, then create and register a developer with the API product in order to obtain an API key. 

  4. Obtain an API key. 
     1. Create an API product using the Apigee UI: 
        1. Go to the API products page: 

In the Google Cloud console, go to the **Distribution > API products** page.

[Go to API products](https://console.cloud.google.com/apigee/apiproducts)

        2. Click **\+ Create**.
        3. Enter the Product Details for your API product.  

        4. Enter the following information in the fields: Field | Setting  
---|---  
`Name: ` | **myproduct**  
`Display name: ` | **myproduct**  
`Environment: ` | **dev**  
`Access: ` | **Public**  
`Quota: ` | Leave blank  
`Allowed OAuth scope: ` | Leave blank  
        5. In the **Operations** section, click **\+ Add an Operation**.
        6. Under **Source** select **helloworld** from the API Proxy dropdown menu.
        7. Under **Operation** , in the Path field, enter `/`. 

Leave other fields set to their defaults.

        8. Click **Save** to save the Operation.
        9. Click **Save** to save the API product.
     2. Create a developer in your organization: 
        1. In the Google Cloud console, go to the **Distribution > Developers** page.

[Go to Developers](https://console.cloud.google.com/apigee/developers)

        2. Click **\+ Create**.
        3. Enter the following information in the fields: Field | Setting  
---|---  
`First Name: ` | **Alex**  
`Last Name: ` | **Hamilton**  
`Username: ` | **ahamilton**  
`Email: ` | **ahamilton@example.com**  
        4. Click **Add**.
     3. Register an app: 
        1. Open the app editor. 
           1. In the Google Cloud console, go to the **Distribution > Apps** page.

[Go to Apps](https://console.cloud.google.com/apigee/apps)

           2. Click **\+ Create**.
        2. Enter the following information in the fields: Field | Setting  
---|---  
`Name: ` | **myapp**  
`Display name: ` | **myapp**  
`Developer: ` | **ahamilton@example.com**  
`Callback URL: ` | Leave blank  
`Notes: ` | Leave blank  
`Expiry: ` | **Never**  
`Product: ` | 
           1. Click **Add product**.
           2. Select **myproduct**.
           3. Click **Add**.  
`Custom attributes: ` | Leave blank  
        3. Click **Create**.
     4. Copy the API key. 
        1. In the Google Cloud console, go to the **Distribution > Apps** page.

[Go to Apps](https://console.cloud.google.com/apigee/apps)

        2. Click **myapp**.
        3. In the **Credentials** section, next to **Key** , click  visibility_off  **Show**. 
        4. Click  content_copy **Copy**. 
  5. Run the curl call again passing the API key using the `apikey` query parameter, as follows: 
         
         curl -v https://$PUBLIC_FACING_IP/helloworld?apikey=ZQA5euYtNeJ7ZCGCJMpvd6F2BZOmxOzY

The following response is returned:
         
         {
           "root": {
             "city": "San Jose",
             "firstName": "John",
             "lastName": "Doe",
             "state": "CA"
           }
         }




**Congratulations!** You've successfully deployed your API archive to an Apigee environment!

In the next step, you'll promote your API archive to an Apigee production environment.

[1](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-workspace) [2](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy) [3](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy) [4](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-test) [5](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-change-target-endpoint) [6](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-attach-policy) [7](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-deploy-apigee) [(NEXT) Step 8: Promote an archive to production](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-promote)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
