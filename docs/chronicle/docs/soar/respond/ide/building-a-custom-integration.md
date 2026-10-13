---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/building-a-custom-integration/
title: Build custom integrations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:05.882716+00:00
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

This document explains how to create custom integrations inside the Integrated Development Environment (IDE) using the same structure as commercial integrations. You can find and configure custom integrations in the Content Hub for various environments. You can then use them in playbooks, manual actions, and remote agents. Import and export capability is also supported, similar to other IDE items. 

**Note:** For a standardized development framework, quality assurance guidelines, and best practices for building and submitting custom integrations, see [Custom integrations guide](https://github.com/chronicle/content-hub/blob/main/docs/content_deep_dive/response_integrations/response_integration_structure.md). 

## Create a custom integration in the IDE

You can build a custom integration for the Armis product and create a manager along with a **Ping** action. Knowledge of Python and object-oriented programming is assumed for this procedure.

### Use case: Build a custom Armis integration

To create the custom integration in the IDE, follow these steps:

  1. In the main menu, go to **Response > IDE**.
  2. Click add**Create New Item** and select **Integration**.
  3. Enter a name and click **Create**.



The integration is now listed with the  settings **Settings** option, indicating it's a custom integration. 

Click  settings **Settings** to display the integration settings where you can define the icon, description, Python dependencies, and integration parameters. 

**Note:** Script dependencies are Python libraries required by your custom integration. Dependencies can be uploaded as `.WHL`, `.TAR`, `.GZ`, or `.PY` files. Each integration runs in its own virtual environment, letting you use specific library versions, regardless of what's installed on the underlying system. For example, to use a different version of the requests library, download it from a trusted source such as PyPI or GitHub and add it as a script dependency.   
For dependencies that require a pre-compiled binary wheel (like packages with C extensions), the SOAR platform uses standard cpython built against the `manylinux_2_17_x86_64` architecture. When selecting a `.WHL` file, verify that it's compatible with this tag.   
If a library is not installed in the virtual environment, the integration falls back to the system-installed version.   
  
If you are using a custom or proprietary `.WHL` file (such as `TIPCommon`) that requires nested sub-dependencies, you must manually upload individual wheel files for the entire dependency tree (for example: `anyio`, `certifi`, `httpx`, `idna`, or `sniffio`) before saving. Failing to resolve nested dependencies will result in a generic `errorCode: 2000` failure. For a complete list of required platform libraries, see the [Community Guide on Retrieving TIPCommon](https://security.googlecloudcommunity.com/google-security-operations-2/retrieving-latest-version-of-tipcommon-and-its-dependencies-1880). 

If a dependency package doesn't have a pre-compiled wheel (`.WHL`) file available for the `manylinux_2_17_x86_64` architecture, or if you need a specific source code version, you can provide a direct URL to the source code (for example, a `.tar.gz` file). The platform's dependency resolver, `uv`, supports defining these source URLs in the `[tool.uv.sources]` table within your `pyproject.toml` file. For example: 
    
    
    [project]
    # ... other project fields ...
    
    [tool.uv.sources]
    compressed-rtf = { url = "https://files.pythonhosted.org/packages/.../compressed_rtf-1.0.6.tar.gz" }
    dkimpy = { url = "https://files.pythonhosted.org/packages/.../dkimpy-1.1.8.tar.gz" }

For more details on defining different types of dependencies using `uv`, see the `uv` documentation on [Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/). 

### Recommended workflow: Advanced dependency management using mp CLI

For integrations requiring complex or multi-layered external libraries like `TIPCommon`, Google recommends bypassing manual IDE uploads entirely and developing them locally using the **Marketplace CLI (mp)** tool. This tool automatically tracks and packages nested dependencies using the `uv` package manager. 

#### Prerequisites

  * Python 3.11 or later installed on your local development machine.
  * The `uv` Python package manager installed (see the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)).



#### Initial Setup

  1. Fork and clone the official [Content Hub repository](https://github.com/chronicle/content-hub) to your local environment.
  2. Install the `mp` tool using `uv`: 
         
         uv tool install mp --from git+https://github.com/chronicle/content-hub.git#subdirectory=packages/mp

  3. Sign in to your Google SecOps environment using your instance root URL and your legacy API key: 
         
         mp login --api-root https://{YOUR_INSTANCE}.siemplify-soar.com --api-key {YOUR_LEGACY_API_KEY}

**Note:** The CLI tool requires your legacy SOAR instance URL and API key format for authentication. 
  4. Configure your local root repository path: 
         
         mp config --root-path /path/to/cloned/content-hub

  5. Create a custom subdirectory for your proprietary integrations within the repository layout at: `content-hub/content/response_integrations/custom/`



#### Adding TIPCommon or Complex Dependencies to an Integration

If you have an integration created in the IDE that needs `TIPCommon` or other multi-layered libraries, use the following local workflow to manage its dependencies safely:

  1. Navigate to your custom integration directory inside your cloned repository: 
         
         cd content-hub/content/response_integrations/custom/

  2. Pull the existing integration structure down from your Google SecOps instance: 
         
         mp pull --type integration --name "{INTEGRATION_NAME}"

  3. Change directory into the newly pulled integration folder: 
         
         cd {INTEGRATION_NAME}

  4. Use `uv` to inject the required `TIPCommon` wheel file package. This automatically tracks and downloads the nested sub-dependency wheels into your local environment package configuration: 
         
         uv pip install /path/to/wheels/TIPCommon-your-version-py3-none-any.whl

  5. Push the fully compiled integration along with its newly tracked dependency tree back up to your Google SecOps instance: 
         
         mp push --type integration --name "{INTEGRATION_NAME}"




#### Verifying the installation

To confirm that your dependencies successfully packaged without encountering an `errorCode: 2000` loop, do the following:

  * Open your custom integration inside the IDE.
  * Add a test line to import a module from the package, such as: `from TIPCommon.extraction import extract_action_param`
  * Click the **Test/Play** button to debug the execution. If the script compiles cleanly without throwing a `ModuleNotFoundError`, your nested dependencies are correctly resolved.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
