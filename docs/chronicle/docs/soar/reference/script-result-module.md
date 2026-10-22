---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module/
title: ScriptResult module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:11.267472+00:00
---

# ScriptResult module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/script-result-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  ScriptResult module 

### add_entity_json

Add the json result with entity identifier as title.
    
    
    siemplify.result.add_entity_json(entity_identifier, json_data)
    

### add_result_json

Add the json result to the case.
    
    
    siemplify.result.add_result_json(json_data)
    

### add_entity_content

Add the json result with entity identifier as title.
    
    
    siemplify.result.add_entity_content(entity_identifier, content)
    

### add_entity_table

Add data table with the entity identifier as table title.
    
    
    siemplify.result.add_entity_table(entity_identifier, data_table)
    

### add_entity_attachment

Add the json result with entity identifier as title.
    
    
    siemplify.result.add_entity_attachment(entity_identifier, filename, file_contents, additional_data=None)
    

### add_entity_html_report

Add html data with entity identifier as title.
    
    
    siemplify.result.add_entity_html_report(entity_identifier, report_name, report_contents)
    

### add_entity_link

Add json result with entity identifier as title.
    
    
    siemplify.result.add_entity_link(entity_identifier, link)
    

### add_link

Add a web link to the selected entity.
    
    
    siemplify.add_link(title, link)
    

### add_attachment

Add attachment.
    
    
    siemplify.result.add_attachment(title, filename, file_contents, additional_data)
    

### add_content
    
    
    siemplify.result.add_content(entity_identifier, content)
    

### add_html
    
    
    siemplify.result.add_html(title, report_name, report_contents)
    

### add_json

Add a json result with entity identifier as title.
    
    
    siemplify.result.add_json(entity_identifier, json_data)
    

### add_data_table
    
    
    siemplify.result.add_data_table(title, data_table)
    

### loadConfigFromFile

Load logger config file.
    
    
    loadConfigFromFile(run_folder=run_folder, log_location=log_location)
    

### exception

This function logs a message with ERROR level in logs. In addition, the traceback of the last exception will be written to the logs as well.
    
    
    exception(message)
    

### error

This function logs a message with ERROR level in logs.
    
    
    error(message)
    

### warn

This function logs a message with WARN level in logs.
    
    
    warn(message)
    

### info

This function logs a message with INFO level in logs.
    
    
    info(message)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
