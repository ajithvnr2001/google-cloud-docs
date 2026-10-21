---
url: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/add-dashboard-widgets/
title: Add SOAR dashboard widgets \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:29:50.852268+00:00
---

# Add SOAR dashboard widgets  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/add-dashboard-widgets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add SOAR dashboard widgets

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes the Google Security Operations SOAR dashboard widgets you can use to display data related to the status of your SOC, derived from cases, alerts, and playbooks. Widgets help visualize key metrics—such as alert reduction, case prioritization, and automation performance—directly within a SOAR dashboard. Each dashboard can contain up to 12 widgets, which you can add based on your monitoring needs.

By showing the percentage of alerts that have been grouped into cases, the widgets demonstrate how [alert grouping](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/alert-grouping-mechanism-admin) helps reduce the number of individual alerts that require investigation.

For example, the **Alert Reduction** widget shows the ratio of cases to alerts using this formula:   
1 - ( Cases / Alerts ) * 100% If four alerts are grouped into three cases, the number of alerts requiring investigation is reduced by 25%, as three grouped cases replace four individual alerts.

##  Add a widget to a SOAR dashboard

  1. Go to **Dashboards & Reports > SOAR Dashboards**.
  2. Click  add **Add Widget**. **Note:** If the dashboard is newly created, you can also click  add **Add** in the empty dashboard. 
  3. In the **Widget Settings** dialog:
     * Enter a title for the widget (required).
     * The **Time** and **Environment** fields are auto-filled based on the dashboard settings.
  4. Select a **Widget Width**.
  5. Select the **Data Display Form** :
     * **Pie chart** (default format)
     * **Horizontal bar graph**
     * **Vertical bar graph**
     * **Table**
  6. On the side pane, specify fields relevant to the selected display form.
     * For example, if using a **Pie Chart** , configure:
       * **Number of**
       * **Calculate field**
       * **Group by**
       * **Number of Results**
       * **Order by**
     * For a **Table** , fields include:
       * **Number of**
       * **Calculate field**
       * **Axis A**
       * **Axis B**
**Note:** The **Group By** options display differently, depending on whether you select **Cases** or **Alerts**.
  7. In the **Filters** pane, select the data filters to apply:
     * The top 15 filters are shown by default.
     * Use the search bar to add filters not listed.
  8. Click **Save** to add the widget to the dashboard with the specified display format, fields, and filters.



For details about the data display form and corresponding fields, see [View data display forms and fields](https://docs.cloud.google.com/soar-dashboards/add-dashboard-widgets#data-display-forms-and-fields). 

## View data display forms and fields

Data Display Form  |  Fields   
---|---  
Pie Chart  
Horizontal Bar Graph  
Vertical Bar Graph  
| 

  * Number of 
  * Calculate field 
  * Group by 
  * Number of Results 
  * Order by 

  
      
    
    <tr>
      <td>
        Table
      </td>
      <td>
        <ul>
          <li>
            Number of
          </li>
          <li>
            Calculate field
          </li>
          <li>
            Axis A
          </li>
          <li>
            Axis B
          </li>
        </ul>
      </td>
    </tr>
    

Number of  |  Group by fields   
---|---  
If you choose **Alerts** | 

  * Entity Identifier 
  * Environment 
  * Network 
  * Playbook 
  * Product 
  * Rule Name 

  
If you choose **Cases** | 

  * Analyst 
  * Environment 
  * Importance 
  * Priority 
  * Tag 
  * Stage 

  
If you choose **Playbooks** | 

  * Playbook Name 
  * Environment 
  * Blocks 

  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
