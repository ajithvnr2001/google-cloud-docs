---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action/
title: Develop your first custom action \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:22.105433+00:00
---

# Develop your first custom action  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop your first custom action

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

In your [first custom integration](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-integration), you defined its parameters, and created a **Ping** action to test the connection. This document guides you through how to create two new actions for your custom integration:

  * **Get domain details** : Retrieves domain information and presents the result in JSON format.
  * **Enrich entities** : Enriches entities with domain details.

**Note:** These procedures require knowledge of Python and object-oriented programming. We also recommend exploring the SDK modules.

## Create a custom action

To create a custom action, follow these steps:

  1. Go to the Integrated Development Environment (IDE) and click add**Add** to add a new IDE item.
  2. Select the **Action** radio button.
  3. Name the action `Get Domain Details` and select the integration.
  4. Click **Create**. The IDE generates a new template with built-in code comments and explanations. 



## Configure action parameters

Based on the [WHOIS XML API documentation](https://whois.whoisxmlapi.com/documentation/making-requests), the **Get Domain Details** action requires two parameters: `Check Availability` and `Domain Name`. To configure these parameters, follow these steps:

  1. In the IDE module, click add **Add**. 
  2. Create the first parameter: Fill in the fields for **Check Availability** and click **Save**. This parameter indicates whether the domain is available or not and its result will be used in the automation you create later. 
  3. Create the second parameter: Fill in the fields for **Domain Name** and click **Save**. Use this field to enter the domain you want the action to check. 



## Edit the Get Domain Details action

To edit the **Get Domain Details** action, follow these steps:

  1. Copy the provided code for **Get Domain Details** , and paste it into the IDE. Review the code. The object must use the class's `end` method to return an output message and a result value, for example:  
`siemplify.end(msg, None)`
  2. Extract integration & action parameters: The integration parameters, such as the **API Key** , are extracted using the `siemplify.extract_configuration_param` function. Similarly, the action parameters you configured, including `Domain Name` and `Check availability`, are extracted with the `siemplify.extract_action_param` function. 
         
         api_key =
             siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,
             param_name="API Key") 
         url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&outputFormat=json" 
             domain = siemplify.extract_action_param(param_name="Domain Name",
             print_value=True) availability_check =
             siemplify.extract_action_param(param_name="Check availability",
             is_mandatory=False, print_value=True)
           

  3. Build the request and process the result:
     1. After you've extracted the integration and action parameters, you can build the request URL. The URL is constructed based on the Boolean value of the `availability_check` parameter.
     2. Once the URL is ready, send a request to the WHOIS site.
     3. Parse the site's response and add the relevant data to the action's result.
     4. Define the output message that will be presented to the user and include the JSON result.  

            
            # Add domain to scan
                  url = f"{url}&domainName={domain}"
                  # Determine availability check
                  if availability_check.lower() == 'true':
                      availability_check_qs = 1
                  else:
                      availability_check_qs = 0
                  url = f"{url}&da={availability_check_qs}"
                  response = requests.get(url)
                  response.raise_for_status()
                  # Add a Json result that can be used in the next steps of the playbook.
                  siemplify.result.add_result_json(response.json())
                  # Add the Json to the action result presented in the context details.
                  siemplify.result.add_json("WhoisDetails", response.json())
                  msg = f"Fetched data for {domain}"
                  siemplify.end(msg, None)
              if __name__ == "__main__":
                  main()
              




### Add a JSON result to the action

As part of the **Get Domain Details** action, click the **Get Domain Details** to add a JSON example. Use the JSON example in the playbook designer in the ["Create your first automation"](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation) procedure to extract a specific field in the JSON. 

  1. Get the JSON: Copy the JSON from the WHOIS site's [JSON example](https://docs.cloud.google.com/static/chronicle/docs/soar/respond/start-developing/json-example.json). 
  2. Enable the JSON icon: In the **Details** tab of the IDE, enable the **Include JSON Result** toggle to make the JSON icon visible at the top of the IDE. 
  3. Import the JSON: Click  file_json  **Manage JSON Sample > login  Import JSON Example**.



## Test the action

To test the action you've created, follow these steps: 

  1. Go to the **Testing** tab.
  2. In the **Scope** select your **Test Case** and **Integration Instance**.
  3. Click  slideshow  **Play** in the IDE.
  4. View the action's result in the **Testing** tab. You can also review the logs and prints by checking the **Debug Output** tab after the test is complete. 



## Create a test case

If you don't have any test cases in your environment, go to the **Cases > Ingest alert as test case** to create one. This action creates a test case that appears with a **Test** label in your case queue. After creating the test case, go back to the IDE and choose the test case from the list. 

To create a test case, follow these steps:

  1. Go to the **Cases** page and select a case.
  2. Ingest the alert as a test case. This creates a new case with a **Test** label in your case queue.



After you've created a test case, return to the IDE and select it from the list.

## Create an enrichment action

This part of the procedure focuses on creating an enrichment action to add new data to entities. The enriched data can then be viewed in the **Entity Explorer**. To create an enrichment action, follow these steps: 

  1. In the IDE, create a new action and name it `Enrich Entities`.
  2. Copy and paste the following code into the action: 
         
         from SiemplifyAction import SiemplifyAction 
           from SiemplifyUtils import output_handler 
           from SiemplifyDataModel import EntityTypes
           
           import requests
           
           # Example Consts: 
           INTEGRATION_NAME = "My first Integration - Whois XML API" 
         
           SCRIPT_NAME = "WHOIS XML API EnrichEntities"
           
           @output_handler 
           def main():    
               siemplify = SiemplifyAction()    
               siemplify.script_name = SCRIPT_NAME    
               siemplify.LOGGER.info("================= Main - Param Init =================")     
         
               api_key =
               siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,
               param_name="API Key") url =
               f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&outputFormat=json"
               
               
               siemplify.LOGGER.info("----------------- Main - Started -----------------")
               output_message = "output message :" # human readable message, showed in UI
               as the action result successful_entities = [] # In case this actions
               contains entity based logic, collect successful entity.identifiers 
               
             for entity in siemplify.target_entities:        
             siemplify.LOGGER.info(f"processing entity {entity.identifier}")
               if (entity.entity_type == EntityTypes.HOSTNAME and not entity.is_internal)
               or entity.entity_type == EntityTypes.URL: entity_to_scan = entity.identifier
               
                     scan_url = f"{url}&domainName={entity_to_scan}"              response = requests.get(scan_url)            
                     response.raise_for_status()            
                     register_details = response.json().get("WhoisRecord", {}).get("registrant", {})            if register_details:                
                 entity.additional_properties.update(register_details)        successful_entities.append(entity) 
         
               if successful_entities:        
                 output_message += "\n Successfully processed entities:\n {}".format("\n
                 ".join([x.identifier for x in successful_entities]))
                 siemplify.update_entities(successful_entities) # This is the actual
                 enrichment (this function sends the data back to the server) 
             else:        
                 output_message += "\n No entities where processed."      
           result_value = len(successful_entities) 
         
               siemplify.LOGGER.info("----------------- Main - Finished -----------------")    
               siemplify.end(output_message, result_value) 
         
           if __name__ == "__main__":    
               main()
           

  3. Extract parameters. The script extracts the API Key from the integration's configuration. This key is necessary to authenticate requests to the WHOIS XML API. 
  4. Identify target entities. The script identifies which entities to process. It iterates through all the entities and focuses only on two types:
     * Non-internal hostnames
     * URLs
    
    for entity in siemplify.target_entities:        
            siemplify.LOGGER.info(f"processing entity {entity.identifier}") if
            (entity.entity_type == EntityTypes.HOSTNAME and not entity.is_internal) or
            entity.entity_type == EntityTypes.URL: entity_to_scan = entity.identifier
      

  5. Scan the domain and define the enrichment step of the action and the output message. This action runs on an **Entity** scope and, therefore, doesn't require you to configure specific parameters; this is already embedded in the code: 
         
         scan_url = f"{url}&domainName={entity_to_scan}"
         
                       response = requests.get(scan_url) response.raise_for_status()
                       register_details = response.json().get("WhoisRecord",
                       {}).get("registrant", {}) if register_details:
                           entity.additional_properties.update(register_details)
                           successful_entities.append(entity)
         
         
               if successful_entities:
                   output_message += "\n Successfully processed entities:\n {}".format("\n
                   ".join([x.identifier for x in successful_entities]))
                   siemplify.update_entities(successful_entities) # This is the actual
                   enrichment (this function sends the data back to the server)
               else:
                   output_message += "\n No entities where processed."
         
         
               result_value = len(successful_entities) 
           

  6. Enable the action and click **Save**. You've now created a custom integration with three custom actions:
     * A **Ping** action to test the connection to the WHOIS XML API product.
     * A **Get Domain Details** action to extract data about a domain and present it as a JSON result.
     * An **Enrich Entities** action to add additional data to target entities, which you can see in the **Entity Explorer** module.

You're now ready to [create your first automation](https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation) using the actions you customized.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
