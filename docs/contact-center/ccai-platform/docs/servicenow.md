---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/servicenow/
title: ServiceNow \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:19:14.240861+00:00
---

# ServiceNow  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  ServiceNow Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides integration with ServiceNow CRM.

## ServiceNow developer settings

Preferred minimum ServiceNow Version requirements: `Tokyo patch 1`

## Set up a basic auth user

It is likely that the ServiceNow administrator account has 2-step verification enabled and associated with that user. As a result, it cannot be used to gain administrator access in CCAI Platform. You must create a user account in ServiceNow for this purpose. 

Create a basic user with credentials:

  1. Go to **User > New**.

  2. Fill in details, and select Web service access only.

  3. Make note of the user ID and password.




## Required roles in ServiceNow

Default roles in ServiceNow are pre-configured to provide specific access and permissions within the platform. Admins can create and configure roles that grant specific permissions, which govern what users and groups with that role can do.

To perform this integration, you need to have the following roles in ServiceNow:

  * **user_admin** : This role is designed for administrators who need to manage users, groups, locations, and companies within the ServiceNow instance.

  * **sn_incident_read** : This role provides read-only access to the Incident Management Application and its related functions. It allows users to view incident records.

  * **sn_incident_write** : This role grants write access to the Incident Management Application and its related functions, allowing users to create and modify incident records.

  * **personalize_dictionary** : This role allows customization of dictionary entries and labels to meet specific business requirements.

  * **function_field_admin** : This role is intended for users who need to create, edit, and view function fields specifically within the report designer. It does not provide the ability to create or delete function fields from the platform list or form.




## Configure instance views

The following sections outline the configuration changes needed to instance views.

### (Optional) Add favorites

Favorites are a quick way to find your most commonly used links within the ServiceNow instance. To add a favorite, select the star icon next to a field in the Navigator panel. If you want to later filter the navigator panel to only see your favorites, you can select the star icon directly below the filter navigator field in the Navigator panel.

Examples of useful Favorites:

  * Incidents: Associations to records for Custom CRM.
  * Users: Associations to accounts for Custom CRM.
  * Rest API Explorer: A good way to test the API.



### Add custom fields manually

Select the expander icon (3 horizontal lines) in the upper left hand corner inside the object view you would like to change. You can do this in Self Service View or Default View.

  1. In the menu select **Configure > Form Design** to open the Form Designer.

  2. In the left column, select the **Field Types** tab.

  3. Drag the type of custom field you would like to add.

  4. Once you drop the field type into the section you want, select the cog icon to see **Settings**.

  5. Inside the window, change the label and take note of the name. The name is what you use in CCAI Platform app settings.

  6. Select **Save** in the upper right-hand corner of the screen.


**Note:** If you want to ensure that separate fields are filled out according to the SDK being used, give each of these custom fields different names.

### Map session data to the CRM

You must map the appropriate session data from CCAIP using Dialogflow and use the following parameters:

**Virtual Agent Data**
    
    
    {
      "ujet": {
        "session_variable": {
          "capture_target": "payload",
          "payload": {
            "value_one": "$session.params.payload_value_one"
          };
          "capture_type": [ "comment", "field" ] // optional, default of ["comment"]
        }
      }
    }
    

**Metadata**
    
    
    https://INSTANCE.service-now.com/api/now/table/sys_dictionary?sysparm_query=name%3Dsys_user https://INSTANCE.service-now.com/api/now/table/sys_dictionary?sysparm_query=name%3Dincident
    

Label: `column_label`

API Key: `element`

Custom fields are same level as the standard fields in the response of `sys_user` or `incident`.

**Upload a file from CCAI Platform to the CRM**
    
    
    https://INSTANCE_URL.service-now.com/api/now/attachment/upload
    

Method: `POST`

Request data format: `property`

Response data location: `data.result`

Type: `Multi-part form`

Attachment type: `Attachment Url`

Attachment Url: `download_link`

Params: `table below`

**Example request** :
    
    
    {
        file: FILE_DATA,
        table_name: incident,
        table_sys_id: RECORD_ID
    }
    

## Integrate agent adapters (custom forms)

**Note:** Click to call buttons for top of incidents/cases/contacts/users are included with CCAI Platform, so this section only applies to custom forms.

The following steps walk you through the process of enabling agent adapters and the **Click to Call** function in the ServiceNow Instance. 

### Install and configure OpenFrame

**Note:** With multiple configurations within a Servicenow Instance, your user may not have access to a newly created configuration. Check your groups and the list of OpenFrame configuration orders to determine which configuration your user is using. OpenFrame might not appear to agents by default. If agents don't see OpenFrame, they might need to be added to the role `sn_openframe_user`. 

  1. Navigate to **All > System Applications > All Available Applications > All**.

  2. Search for OpenFrame.

  3. Install OpenFrame.

  4. Once installed, navigate to **All > OpenFrame > Configurations**.

  5. Create configuration with a URL. If you have multiple configurations within a Servicenow Instance, your user might not have access to a newly created configuration. Check your groups and the list of OpenFrame configuration orders to determine which configuration your user is using.

  6. Type `sys_properties.list` into search.

  7. Edit `glide.ui.concourse.onmessage_enforce_same_origin_whitelist`.

  8. Add the new URL to the list of values.

  9. Edit `sn_openframe.cross.origin.access`.

  10. Add `autoplay` to the list of values.




### Enable Next UI Experience for Users

  1. Type `sys_properties.list` in the navigation bar and click **Enter**.

  2. Set the system property `glide.ui.polaris.experience` to **true**.

  3. Set the user preference `glide.ui.polaris.use` to **false** for system.

  4. Set the user preference `glide.ui.polaris.use` to **true** for a user. (You can create a user-preference row.)




### Update System Properties

  1. Enter `sys_properties.list` into the navigation bar and click **Enter**.

  2. Edit `glide.ui.concourse.onmessage_enforce_same_origin_whitelist`.

  3. Add the URL to the list of values. Multiple values need to be comma separated.

**Note:** It's important the URL does not end with a `/`, or else it won't work.
  4. Edit `sn_openframe.cross.origin.access`.

  5. Add autoplay to the list of values.

  6. Edit `glide.ui.polaris.experience`.

  7. Change to **false** , because some features do not work if enabled.




### Add Click to Call to the top of the form

  1. Navigate to **System UI** > **UI Actions**.

  2. Select **Create New Action**.

  3. In the form as illustrated, select the table that this Click to Call will be a part of.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/clicktocall.png)

  4. For forms with a reference to a contact or user, use the `g_form.getReference` API to access the user's phone number. For custom tables, the Reference ID and the resulting attributes may differ. Communication to CCAI Platform will be the same, so the payload and data structure must remain identical to the following:
         
         function clickToDial() {
           var user = g_form.getReference('caller_id',function(res) {
             var phone = res.phone || res.mobile_phone;
             var payload = {"name": "clicktodial", "number": phone}; 
             var data = {"payload": payload, "method": "openframe_communication" }; 
             CustomEvent.fireAll("openframe_request", data);
           });
         }
         

  5. For forms with a number within the form to call, use the `g_form.getValue` API to retrieve the relevant values. This is an example from the UI action for the Users table. For custom tables, the form field names may differ. Communication to the CCAI Platform will be the same, so the payload and data structure must remain identical to the following:
         
         function clickToDial() {
           var phone = g_form.getValue('phone') || g_form.getValue('mobile_phone');
           var payload = {"name": "clicktodial", "number": phone}; 
           var context = {"payload": payload, "method" : "openframe_communication" }; 
           CustomEvent.fireAll("openframe_request", context);
         }
         




### Add Click to Call next to references

  1. The call button next to references to contacts must be edited within the form. Right-click the field and navigate to **Configure Dictionary**. For attributes add either the value `show_phone` or `show_phone_customer_service` to the `ref_contributions` value.

  2. In UI Macros, edit `show_phone` and `show_phone_customer_service`.

  3. Replace the following:




**Previous** :
    
    
    var task =    {"entity": p.attr('data-task-table'), "query" :"sys_id="+p.attr('data-task-id')+"$[AMP]sysparm_view="+p.attr('data-task-view'),"value":p.attr('data-task-value'),"label":p.attr('data-task-label')};
                                            var company = {"entity": p.attr('data-company-table'),"query":"sys_id="+p.attr('data-company-id')+"$[AMP]sysparm_view="+p.attr('data-task-view'),"value":p.attr('data-company-value'),"label":p.attr('data-company-label')};
                                            var caller = {"entity": p.attr('data-caller-table'),"query": "sys_id="+p.attr('data-caller-id')+"$[AMP]sysparm_view="+p.attr('data-task-view'),"value":p.attr('data-caller-value'),"label":p.attr('data-caller-label')};
                                            
                                            var callContext = [];
                                            callContext.push(task);
                                            callContext.push(company);
                                            callContext.push(caller);
                    
                                            var metaData = {"phoneNumber":p.attr('data-caller-phone'),"taskId":p.attr('data-task-id')};
                                            
                                            var data =    {"metaData":metaData , "data": callContext};
                                            var payload = {"type": "OUTGOING_CALL", "data" : data};
                                            var createInteractionData ={};
                                            createInteractionData.interactionSysId = -1;
                                            createInteractionData.direction = 'outbound';
                                            createInteractionData.context_document = p.attr('data-task-id');
                                            createInteractionData.context_table = p.attr('data-task-table');
                                            createInteractionData.account = p.attr('data-company-id');
                                            if(p.attr('data-caller-table') === 'customer_contact')
                                                    createInteractionData.contact = p.attr('data-caller-id');
                                            createInteractionData.opened_for = p.attr('data-caller-id');
            
                                            var ga = new GlideAjax('sn_openframe.OpenFrameAjaxUtility');
                                            ga.addParam('sysparm_name', 'createInteractionWithPropertyCheck');
                                            ga.addParam('context', JSON.stringify(createInteractionData));
                                            ga.getXML(function(serverResponse) {
                                                    var result = serverResponse.responseXML.getElementsByTagName("result");
                                                    var output = JSON.parse(result[0].getAttribute("data"));
                                                    if(output.status == "success"){
                                                            var interaction = {"entity": "interaction", "query" :"sys_id="+output.fields.interactionSysId, "value":output.fields.number, "label":"Interaction", "display":false};
                                                            payload.data.data.push(interaction);
                                                    }
                                                    var context = {"payload": payload, "method" : "openframe_communication" };
                                                    jslog("context with interaction : "+ JSON.stringify(context));
                                                    CustomEvent.fireAll("openframe_request", context);
                                            });
    

**New** :
    
    
    var phone = p.attr('data-caller-phone')
                       var payload = {"name": "clicktodial", "number": phone}; 
                       var data = {"payload": payload, "method": "openframe_communication" }; 
                       CustomEvent.fireAll("openframe_request", data);
    

## CRM settings

The following steps illustrate how to connect the API to ServiceNow using the CCAI Platform portal.

  1. In the CCAI Platform portal, navigate to **Settings > Developer Settings > CRM**.

  2. In the Agent Platform section, select **ServiceNow**.

  3. Enter your ServiceNow domain information in the **ServiceNow Domain** field. This might be a developer instance or vendor instance as needed, but is a direct correlation to the instance and is the first part of the URL in the ServiceNow portal web address: `https://{your instance}.servicenow.com`.

  4. In the **ServiceNow Cloud Selection** field, select `Incident` for a basic ticket type. If you select `Custom`, additional options will appear. Incidents are extensions of task table; custom objects should be extensions of incidents.

  5. In the **Authentication Credentials** fields, enter your username and password.

  6. **If you selected`Incident` for the Cloud Selection Field type** you will see the following fields:

     * **Lookup Account Object** includes three drop-down fields: `Object Type`, `Phone Number lookup fields`, and `Phone number primary field`.
  7. **If you selected`Custom` for the Cloud Selection Field type** you will see the following fields:

     * **Lookup Record Object** : 
       * **Base Record Object Type** : Select either a `task` or `incident` table type.
       * **Record Object Type** : This field will populate with data if an incident table has been extended, and you can select it if required.
     * **Lookup Account Object** includes three drop-down fields: `Object Type`, `Phone Number lookup fields`, and `Phone number primary field`.
  8. **Custom User ID Fields** : Check this box if you want to enable custom user lookup fields for Mobile or Web SDK sessions.

  9. **Phone Number Format** : Provides the ability to select the format you would like to use for displaying phone numbers.

  10. **Session Metadata File** : Check this box to attach session metadata to CRM records.

  11. Click **Save** to save your selections. If you have checked the **Custom User ID Fields** box, you will have the option to create custom fields for records. This will add custom fields tabs to the bottom of each ServiceNow Incident below the resolution code and resolution notes sections of the page.




### Custom fields for records

These are custom fields that have already been created for the ServiceNow Instance in the Form Designer. Instructions about how to create other custom fields can be found in the ServiceNow documentation under **ServiceNow CRM Setup** , section **Add Custom Fields Manually**.

Field | Type | Definition  
---|---|---  
`u_ujet_custom_field_after_call_work` | String | After Call Work duration  
`u_ujet_custom_field_call_duration` | String | Call Duration  
`u_ujet_custom_field_comm_id` | Integer | Call or chat ID depending on contact type  
`u_ujet_custom_field_rating` | Integer | CSAT score  
`u_ujet_custom_field_email_via_web` | String | Email sent from web  
`u_ujet_custom_field_feedback` | String | Feedback  
`u_ujet_custom_field_from_phone_number` | String | Phone number of caller  
`u_ujet_custom_field_hold_duration` | String | Total hold time  
`u_ujet_custom_field_menu_path` | String | Menu Selection  
`u_ujet_custom_field_queue_name` | String | Queue Name  
`u_ujet_custom_field_session_type` | String | Session Type  
`u_ujet_custom_field_verification` | True/False | Confirm verification completed  
`u_ujet_custom_field_wait_time` | String | Total wait time  
  
## Set up OAuth

To configure OAuth, take steps to create an OAuth application in ServiceNow. Then, enter credentials (OAuth Client ID and OAuth Client Secret) under **Developer Settings > CRM > Authentication Method**.

### Create an OAuth application in Service Now

  1. In your ServiceNow account, navigate to **All > System OAuth > Application Registry**.

  2. Create an OAuth application and select **Create an OAuth API endpoint for external clients**.

  3. Configure the following fields:

     * **Name** : Enter a unique Name.

     * **Client ID** : The Client ID is automatically generated by the ServiceNow OAuth server.

     * **Client Secret** : This is the client secret for the OAuth application. Leave it empty for auto-generation.

     * **Refresh Token Lifespan** : The time, in seconds, the refresh token will be valid.

     * **Access Token Lifespan** : The time, in seconds, the access token will be valid.

     * **Redirect URL** : Enter your environment URL plus the subdirectory. For example: `https://servicenow.yourcompany.co/v1/servicenow/oauth_callback`

     * **Enforce Token Restriction** : Restricts the access token usage to the APIs defined in the REST API Access Policies found in the ServiceNow documentation. Unselecting this option would allow access token usage across other REST APIs.

  4. Click **Submit**.

  5. After creating the application, go back into the record and retrieve the **Client ID** and the newly created **Client Secret**.




### Update settings in developer settings

  1. Navigate to **Developer Settings > CRM**.

  2. Be sure the settings are entered and configured as per the previous steps.

  3. Under authentication method, click **OAuth**.

  4. Enter the OAuth Client ID and OAuth client secret. (See step 5 above.)

  5. Click **save**.

  6. Click **link credentials**.




## Custom field mapping for Virtual Agent

If using Virtual Agent, configure this field in the **Custom Field Mappings** screen. This allows the Virtual Agent variables to transfer over from the Virtual Agent session payload to ServiceNow. Variable names can be any string, the field labels listed here are an example.

In the **Custom Field Mappings** screen, configure the connection between the variables created by the payload definitions you used in the initial Virtual Agent configuration and the relevant variable within ServiceNow.

Field Mapping Title | CRM Field Label | Custom Data Field Label  
---|---|---  
Virtual Agent Feedback | `ccaip_custom_field_incident_feedback` | `va_feedback`  
  
## Configure other Settings

You will find the other settings that will allow you to properly integrate CCAI Platform into your ServiceNow Instance under the **Settings** drop-down menu. Refer to the links in the following list for additional information about configuring each section.

  * [Languages and Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Customizing_Languages__Recordings____Messages)
  * [Users and Teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent___Team_Configuration)
  * [Virtual Agent](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent)
  * [Campaigns](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Campaign_Management)
  * [Surveys](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Surveys)
  * [Queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup)
  * [Calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features)
  * [Chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-settings-web-and-mobile)
  * [SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/SMS)
  * [Consumer Management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Consumer_Management)
  * [Developer Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings)



## Test outputs

You can now verify the functionality of your call and chat flows by clicking on the relevant buttons at the top of the screen of the CCAI Platform portal. It is important to ensure your pop-up blocker is disabled when running this test.

You should expect an **Incident** to be created in **ServiceNow** , with the call or chat contact listed in the **Activities** section of the Incident. This should show up as a **Work Note** , rather than an Incident Comment, so that this backend activity is not visible to customers.

The case description will autopopulate with "Call using CCAI Platform" or "Chat using CCAI Platform" and might need to be updated by agents.

**Note:** You should see both an activity and a work note in the Incident when a contact occurs. This is especially important if you want to export your contacts to external storage rather than the CRM itself. For more information, see [Set up external storage for CRMs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).

Once you are satisfied with the outputs of your call or chat you can enter a resolution code and note (if ServiceNow resolution code and notes fields have been configured), then close the case.

To verify that the case has closed, you might need to click the `back` navigation button on your browser. It is expected behavior in the ServiceNow Instance that after resolving the case it automatically closes and advances you to a customer record page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
