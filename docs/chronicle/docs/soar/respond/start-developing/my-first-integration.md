---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-integration/
title: Develop your first custom integration \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:04.499938+00:00
---

# Develop your first custom integration  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop your first custom integration

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create a custom integration in the Integrated Development Environment (IDE) with the same structure as commercial integrations. Custom integrations appear in the Content Hub where you can configure them for different environments to use in playbooks, manual actions, and remote agents. You can also import and export them, like other IDE items. 

In this custom integration example, you'll build a custom integration for the **WHOIS XML API** product. Start by creating your first integration including the registration process to the WHOIS product, including registering for the product and creating the required API key. 

## Choose the product to integrate with

  1. In this example, you'll integrate with the **WHOIS XML API** product, a free open source tool that provides API access to domain data, including registrant name, organization, email address, registration address, registrar information, domain creation, expiration, and update dates, domain availability, and age.
  2. Go to [WHOIS XML API/](https://www.whoisxmlapi.com/) and register. 
  3. After you sign in, get your API key from your account page: <https://user.whoisxmlapi.com/products>
  4. Use this API key in your integration parameters. 



## Create the first custom integration in the IDE

To create your first custom integration in the IDE, follow these steps:

  1. On the **Response > IDE** page, click  add  **Add** to add a new IDE item.
  2. Select the **Integration** radio button and enter a name for the integration.
  3. Click **Create**. The integration appears with a custom integration icon.
  4. Click settings **Settings**.
  5. In the integration dialog, define the **Icon** , **Description** , **Python Dependencies** , and **Integration Parameters**.  
In this example, the following details appear:
     * An image of the WhoisXML API logo is uploaded. This image appears in the Content Hub with the integration.
     * An SVG icon has been added next to the integration in the IDE with a brief description and one parameter, the API Key. This is the parameter that the **Who Is XML API** Product requires for the configuration of the integration.
     * You don't need additional Python libraries for this integration. By default, the integration is set to run on Python 3.7, and you can change the version in **Settings**.
**Note:** Script dependencies are Python libraries that your custom integration must import. You can add them in formats, such as Wheel files (`WHL`), tarballs (`TAR`), Gzip archives (`GZ`), or Python files (`PY`). Each integration runs in its own virtual environment, letting you include specific library versions even if a different version is already installed on the system. For example, if you need a particular version of the requests library, download it from a trusted source (such as PyPI or GitHub) and add it to the script dependencies. If the dependency is not in the virtual environment, the integration uses the system-installed version instead. 


## Configure the default instance

Once you create the integration, you can view it in your Google SecOps Response Integrations (search the integration name in the search bar or filter the Integration type by **Custom Integrations**) with the image, description and parameter you defined for the integration.

  1. Click settings **Settings** > **Configure a default Instance**.
  2. Enter your API key and click **Save**.
  3. Optional: To configure the integration for another environment (not the default environment), click the **Configure** tab and set parameters for that instance.
**Note:** You must create a **Ping** action before the built-in **Test button** can work. 


## Create a Ping action

  1. In **Response > IDE**, click  add **Add > Add New IDE Item**.
  2. Select the **Action** radio button, enter a name, and select the integration.
  3. Click **Create**. Review the generated code template.
  4. Copy the following code for the **Ping** action. The **Ping** action uses the `API Key` parameter you configured for the integration and puts it in the URL provided by the product for testing purposes. For details, see [Create custom actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action). 
    
    from SiemplifyAction import SiemplifyAction
    from SiemplifyUtils import output_handler
    import requests
    
    INTEGRATION_NAME = "My first Integration - Whois XML API"
    SCRIPT_NAME = "Whois XML API Ping"
    
    @output_handler
    def main():
        siemplify = SiemplifyAction()
        siemplify.script_name = SCRIPT_NAME
    
        api_key = siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,
                                                        param_name="API Key")
        url = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName=google.com".format(api_key=api_key)
    
        res = requests.get(url)
        res.raise_for_status()
    
        if "ApiKey authenticate failed" in res.content.decode("utf-8"):
            raise Exception("Error, bad credentials")
    
        siemplify.end("Successful Connection", True)
    if __name__ == "__main__":
        main() 
    

  5. Click the toggle above the action and then **Save** to test the connection to the product. 
  6. Go to the **Google SecOps Marketplace** , click settings **Configure default instance** , and make sure that the integration is configured and saved.
  7. Click **Test** to test the integration. A successful connection displays a green checkmark; a failed connection displays an X with the associated error.
  8. After you complete authentication, create your first custom action in the custom integration. For details, see [Create custom actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
