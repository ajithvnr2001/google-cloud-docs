---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/building-a-custom-integration/
title: Build custom integrations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T09:47:48.662681+00:00
---

# Build custom integrations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/building-a-custom-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build custom integrations

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains the workflows for building custom integrations for Google SecOps. The current best practice is to develop integrations locally using your preferred IDE and manage them via GitHub using modern GitOps workflows. For legacy environments or quick prototypes, you can also build integrations directly inside the built-in SOAR IDE. 

**Note:** For a standardized development framework, quality assurance guidelines, and best practices for building and submitting custom integrations, see [Custom integrations guide](https://github.com/chronicle/content-hub/blob/main/docs/content_deep_dive/response_integrations/response_integration_structure.md). 

## Local IDE & GitHub workflow (recommended)

Developing integrations locally and managing them via GitHub is the recommended workflow. This approach aligns with modern GitOps practices, allowing for better version control, collaboration, and automated dependency management.

For detailed technical steps, installation guides, and modern commands using the **Marketplace CLI** tool and `uv` package manager, refer to the official [Chronicle Content Hub GitHub Repository](https://github.com/chronicle/content-hub/tree/main/packages/mp). 

#### Conceptual workflow overview

To develop custom integrations locally, it is recommended that you follow this GitOps lifecycle. For the exact, up-to-date syntax of these commands, see the [official MP CLI documentation on GitHub](https://github.com/chronicle/content-hub/tree/main/packages/mp).

  1. **Fork and clone:** Clone the official `content-hub` repository to your local development machine.
  2. **Install tools:** Install the `mp` CLI tool and the `uv` Python package manager.
  3. **Authenticate:** Log in to your Google SecOps environment via the MP CLI using your instance URL and API keys.
  4. **Develop locally:** Use your preferred IDE (like VS Code or PyCharm) to write your integration code, taking advantage of local debugging and testing tools.
  5. **Manage dependencies:** Use `uv` to declare and manage dependencies (like `TIPCommon`) in your local `pyproject.toml` file.
  6. **Synchronize:** Use `mp pull` and `mp push` commands to synchronize your local code with your Google SecOps instance for testing and deployment.



## Alternative: Create a custom integration in the built-in IDE

If you are maintaining legacy integrations, testing a script quickly, or working in an environment where local development is restricted, you can use the built-in IDE.

### Use case: Build a custom Armis integration

To create the custom integration in the IDE, follow these steps:

  1. In the main menu, go to **Response > IDE**.
  2. Click add**Create New Item** and select **Integration**.
  3. Enter a name and click **Create**.



The integration is now listed with the  settings **Settings** option, indicating it's a custom integration. 

Click  settings **Settings** to display the integration settings where you can define the icon, description, Python dependencies, and integration parameters. 

**Note:** Script dependencies are Python libraries required by your custom integration. Dependencies can be uploaded as `.WHL`, `.TAR`, `.GZ`, or `.PY` files. Each integration runs in its own virtual environment, letting you use specific library versions, regardless of what's installed on the underlying system.   
  
If you are using a custom or proprietary `.WHL` file (such as `TIPCommon`) that requires nested sub-dependencies, you must manually upload individual wheel files for the entire dependency tree before saving. Failing to resolve nested dependencies results in a generic `errorCode: 2000` failure. For advanced dependency tracking, consider using the **Local IDE & GitHub workflow**. 

### Create a custom manager

Managers are wrappers for third-party tool APIs. Although not mandatory, we recommend them for integrations that interact with external tools. Managers shouldn't import from the SDK. After creation, import them into connectors, actions, and jobs.

To create a custom manager, follow these steps:

  1. In the IDE, click add**Create New Item** and select **Manager**.
  2. Select the **Armis** integration and enter a manager's name.  

  3. Edit and run the following script:


    
    
    import requests
    
    
    class ArmisManager:
       def init(self, api_root, api_token):
           self.api_root = api_root
           self.api_token = api_token
           self.session = requests.session()
           self.session.headers = {"Accept": "application/json"}
    
    
       def auth(self):
           endpoint = "{}/api/vi/access_token/*"
           params = {"secret_key" : self.api_token}
           response = self.session.post(endpoint.format(self.api_root), params=params)
           self.validate_response(response)
           access_token = response.json()["data"]["access_token"]
           self.session.headers.update({"Authorization": access_token})
           return True
    
    
       def get_device_by_ip(self, device_ip):
           endpoint = "{}/api/vi/devices/"
           params = {"ip": device_ip}
           response = self.session.get(endpoint.format(self.api_root), params=params)
           self.validate_response(response)
           return response.json()["data"]["data"]
    
    
       @staticmethod
       def validate_response(res, error_msg="An error occurred"):
           """Validate a response
    
    
           :param res: (requests. Response) The response to validate
           :param error_msg: (str) The error message to display
           """
           try:
               res.raise_for_status()
           except requests.HTTPError as error:
               raise Exception("(error_msg): (error) (text)".format(
                   error_msg=error_msg,
                   error=error,
                   text=error.response.content
               ))
    

**Note:** A manager is not required for basic actions. However, we recommend to create one when grouping small actions for data parsing and transformation. 

## Parameters, Google SecOps Content Hub configuration, and the Ping action

Parameters defined in the integration settings appear in the Google SecOps Content Hub configuration. The parameters include:

  * **API Root** : The base URL for the service you're connecting to.
  * **API Secret** : A confidential key used to authenticate your application with the service.
  * **Verify SSL** checkbox: If enabled, verifies that the SSL certificate for the connection to the Armis server is valid.
  * **Run Remotely** checkbox: A setting that determines whether the code or task will be executed on a remote server instead of locally. When this option is enabled, the system sends the necessary instructions and data to a dedicated server for processing.



To update the parameters, follow these steps:

  1. Enter the correct credentials.
  2. Click **Save** > **Test**.

**Note:** Always click **Save** after updating credentials. All third-party integrations must implement a **Ping** action. The **Test** button runs this action to validate connectivity. 

If the **Ping** action is missing, the **Test** button fails and displays a red **X**. 

### Implement a Ping action

The logic of the **Ping** action acts like a successful authentication.

To implement a **Ping** action, do the following:

  1. In the IDE, create a new **Action** in the Armis integration named `Ping`.
  2. Use the `ArmisManager` `auth` method to verify authentication.



### Enable the integration

To enable the integration, follow these steps:

  1. In **Response > IDE**, click the **Enable/Disable** toggle to the **ON** position.
  2. Click **Save**. A green toggle confirms success. Credentials from the Content Hub are passed to ArmisManager. If `auth` completes without errors, the **Test** button shows a green checkmark.



Use the `extract_configuration_param` method to import parameters from the integration configuration. Alternatively, use `extract_action_param` to define parameters within the action itself. However, the **Ping** action should always use configuration parameters, as those are tested by the Content Hub. 

## View custom integrations

Go to the Content Hub and search for the custom integration you created. If you didn't create an image during the initial configuration, the default custom image will be assigned to it. Note that Content Hub updates don't override or delete any custom integrations. 

## Export and import in the IDE

Do one of the following actions:

  * To **import** integrations, do the following:
    1. Upload a ZIP file with the correct folder structure; the integration appears in the IDE and the Content Hub.
    2. Click **Import**. The integration appears in both the IDE and the Content Hub.
    3. The system generates a ZIP file containing the definition, scripts, and configuration. The **Managers** folder is not included automatically.
  * To **export** integrations, do the following:
    * Click **Export** to download the package.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
