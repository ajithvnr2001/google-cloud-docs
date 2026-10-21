---
url: https://docs.cloud.google.com/looker/docs/2616/data-apps/
title: Looker Data Apps overview and setup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:47:50.139672+00:00
---

# Looker Data Apps overview and setup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2616/data-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker Data Apps overview and setup

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by using the [Looker Data Apps - Preview Issues form](https://forms.gle/t7GqiwQnDgNyoFVV8).**Note:** As a preview feature, Looker Data Apps is subject to the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-terms).

**Looker Data Apps** are freeform canvas dashboards that are built by local AI coding agents, such as Gemini CLI, Claude Code, or Cursor, from natural-language prompts. Unlike standard grid dashboards, Data Apps give you complete visual layout control (including absolute positioning, overlapping elements, and custom web components) while remaining bound to Looker's governed LookML semantic layer and user permissions.

When you build a Data App, the AI coding agent runs on your local machine to generate the application code. After you publish the Data App to Looker, no AI model is involved when users open or interact with the dashboard.

## Overview of Looker Data Apps

A Data App is a Looker extension, which is powered by the [Looker Extension Framework](https://docs.cloud.google.com/looker/docs/2616/extension-overview) and which runs within a single-element User-Defined Dashboard (UDD).

Key capabilities include the following:

  * **AI-assisted authoring, zero runtime AI** : You use an AI coding agent on your computer to generate the layout and component code from prompts. Published Data Apps run as standard web components inside Looker without calling any AI model when users view the dashboard.
  * **Network-isolated sandbox** : Because an AI agent writes the application code, Looker runs every Data App inside an isolated browser sandbox that blocks outbound network connections. The application code can communicate only with your Looker instance, so query results and user credentials cannot be sent to external servers.
  * **Governed data access** : Data Apps query data exclusively through Looker's LookML semantic layer. Every query runs under the viewing user's Looker permissions, model access, and row-level access filters.
  * **Interactive controls and scheduled delivery** : Data Apps include built-in interactive filters, cross-filtering, and drill views inside the app, and Data Apps support Looker PDF downloads and scheduled email delivery.



## Before you begin

Before you install the developer tools and author a Data App, verify that you meet the following prerequisites:

### Instance requirements

  * You must use a Looker-hosted instance that's running Looker 26.18 or later.
  * A Looker admin must enable the **Data Apps** preview toggle in the **Admin** panel under **General > Previews**. For more information, see the [Preview Features documentation page](https://docs.cloud.google.com/looker/docs/2616/admin-panel-general-preview-features).
  * Users' browsers must have network access to `www.gstatic.com` to load the Data Apps runtime libraries.



### Required permissions

To create and publish a Data App, you must have the following:

  * The [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/2616/organizing-spaces#folder_access_levels) access level for the folder in which you want to place the dashboard
  * The [`access_data`](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#access_data), [`explore`](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#explore), [`see_user_dashboards`](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#see_user_dashboards), and [`save_dashboards`](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#save_dashboards) (or [`save_content`](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#save_content)) Looker permissions
  * [Access to the LookML models](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-roles#model_sets) for any data that you want to use in the dashboard



To view a published Data App, your users must have the following:

  * The [**View**](https://docs.cloud.google.com/looker/docs/2616/organizing-spaces#folder_access_levels) access level to the destination folder

  * The `access_data`, `explore`, and `see_user_dashboards` Looker permissions for the underlying LookML models




### Looker API credentials

Your developer tools access your Looker instance by using the [Looker API](https://docs.cloud.google.com/looker/docs/2616/api-overview). To grant your developer tools access to the Looker API, you need an [API key](https://docs.cloud.google.com/looker/docs/2616/user-account#api-keys), which consists of a client ID and a client secret. You provide your client ID and client secret to the developer tools when you configure the setup options.

To retrieve your API key, follow these steps:

  1. Your Looker admin must [enable **API Keys** for your user account](https://docs.cloud.google.com/looker/docs/2616/admin-panel-users-users#api_keys) in the **Admin > Users** page.
  2. In Looker, go to your [user **Account**](https://docs.cloud.google.com/looker/docs/2616/user-account) page.
  3. In the **Authentication** section, next to the **API Keys** heading, click **Manage**.
  4. In the **API Keys** page, you can [view your existing API keys or create new API keys](https://docs.cloud.google.com/looker/docs/2616/user-account#api-keys).
  5. Copy the **Client ID** and **Client Secret** for your selected API key.



### Folder identifier

Identify the numeric ID of the Looker folder where you want to publish your Data Apps. In Looker, open the target folder (such as **Shared** or **My Folder**) and note the number at the end of the URL:
    
    
    https://LOOKER_INSTANCE_URL/folders/FOLDER_ID
    

### Limitations

Looker Data Apps have the following limitations:

  * **Embedding, theming, and printing** : Data Apps don't support [embedding](https://docs.cloud.google.com/looker/docs/2616/embed-getting-started), [internal dashboard themes](https://docs.cloud.google.com/looker/docs/2616/themes-for-internal-dashboards), or printing. However, you can customize visual styling directly in the Data App by prompting your AI coding agent.
  * **Copying Data Apps** : Avoid [copying a Data App](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards#copying_dashboards) in Looker. Because copies reference the same underlying application, changes made to one copy are mirrored across all copies.
  * **LookML export and import** : Exporting a Data App [as LookML](https://docs.cloud.google.com/looker/docs/2616/viewing-dashboards#getting_the_lookml_from_a_dashboard) and [importing a Data App from LookML](https://docs.cloud.google.com/looker/docs/2616/converting-lookml-to-user-defined-dashboard) aren't supported.
  * **Dependency on`www.gstatic.com`**: Data Apps require network access to `www.gstatic.com` to load runtime and component libraries. Users' browsers must be able to reach `www.gstatic.com` to render Data Apps.



## Install the developer tools

To author Data Apps, install the developer tools in your local development environment (macOS or Linux).

**Note:** The Data Apps developer tools require Python version 3.9 or later. If you don't have Python installed in your local development environment, see the [official Python installation guide](https://www.python.org/downloads/) to install Python.

### Run the installation script

Open a terminal on a machine with access to your AI coding agent, and run the following command:
    
    
    bash <(curl -fsSL https://dl.google.com/looker-data-apps/install.sh)
    

### Configure setup options

During installation, respond to the interactive prompts:

  1. **Install directory** : Enter the local path where you want to store your Data Apps project, or press **Enter** to accept the default (`~/looker-data-apps`).
  2. **Looker instance URL** : Enter your Looker instance URL, such as `https://myinstance.looker.com`.
  3. **Looker API client_id** : Enter your **Client ID**.
  4. **Looker API client_secret** : Enter your **Client Secret** (saved locally to `data-apps-config.json` with owner-only file permissions).
  5. **Looker folder ID** : Enter the target folder ID that you identified in Folder identifier, or press **Enter** to accept the default folder, which is folder `1`, the **Shared** folder.



After you complete the prompts, the installer automatically runs a four-step verification check to confirm that your credentials work and that your Looker instance can store and serve Data Apps.

## Author, preview, and publish a Data App

Follow this workflow to create a Data App with your AI coding agent:

### Step 1: Start your AI coding agent

In your terminal, navigate to your Data Apps installation directory (`~/looker-data-apps`) and launch your AI coding agent.

### Step 2: Prompt the agent to generate a Data App

Using natural language to write your prompts, ask the agent to build an application. Your application must be based on existing Explores and views, but you don't need to use technical identifiers. For example:
    
    
    Build a responsive Looker Data App using the faa model and the
    large\_flight\_data explore. I want this to be a dynamic, dark-themed operations
    center.
    
    Please include the following components:
    
    The Map (Centerpiece): Create a custom visual that visualizes flights moving
    from their Origin to Destination. Include a timeline slider (or playback
    animation) based on Departure Time and Arrival Time so I can watch the flights
    move over time.
    
    KPI Strip: Across the top, include a row of KPI cards showing the total flight
    Count, average Delay Mins, total Total Revenue, and average Load Factor.
    
    Trend Chart: Include a line chart showing how Carbon Emissions and Total Revenue change over
    the Departure Date periods.
    
    Interactive Filters: Include drop-down filters for Airline, Status, and Origin
    that wire into the charts and map to update the data dynamically.
    

The AI agent inspects your LookML Explores, writes the component definition, and starts the local preview server.

### Step 3: Inspect the local preview

Open the local preview URL (`http://localhost:8765`) that's provided by your agent.

You can also run `make start` (or `python3 skills/data-app-previewer/tools/start-preview.py`) in your terminal to view a gallery of all local apps that you have created.

### Step 4: Iteratively refine your app

Talk to your AI agent to refine layout, styling, and interactions:

  * _"Align the 3 metric cards to the right side of the canvas."_
  * _"Add a date range slider above the trend chart."_
  * _"Change the background to a subtle neutral gray and add rounded cards with soft drop shadows."_



### Step 5: Publish the Data App to Looker

When you are satisfied with the design, prompt your agent to deploy the app:
    
    
    Publish this app to Looker.
    

The agent runs the publishing script, which packages the component script and creates or updates a dashboard object in your configured folder.

### Step 6: View the Data App in Looker

Click the Looker link that's returned by the agent. Your Data App loads inside Looker with full support for user access filters, folder sharing, and platform features.

## Suggestions for things to try

To explore the capabilities of Looker Data Apps during the preview, try the following scenarios:

### Replicate existing reports from images

Upload a screenshot of an existing report from another BI tool (such as Tableau or Power BI) or a slide deck to your AI agent. Prompt the agent:
    
    
    Replicate the layout, visual hierarchy, and color scheme shown in this
    screenshot, binding the charts to our customer_analytics explore.
    

Multi-modal AI agents can extract coordinate geometry, typography, and color palettes from images to generate matching Data App layouts.

### Design custom layouts

Move beyond standard rectangular grids by creating asymmetric layouts:

  * Create floating KPI cards that partially overlap hero banners.
  * Add multi-column executive summary sidebars next to wide data grids.
  * Apply custom corporate branding, font styles, and background gradients.



### Incorporate rich interactive UI components

Ask your agent to add interactive web elements:

  * **Tabbed navigation** : Organize complex operational metrics across multiple tabs without page reloads.
  * **Modal dialogs and drawers** : Open detailed breakdown views or glossary definitions when you click a metric.
  * **Interactive filters and controls** : Add custom toggle buttons, sliders, and search inputs that update chart series dynamically.



### Use advanced data tables and visualizations

Take advantage of built-in component libraries:

  * **AG Grid integration** : Embed interactive data tables that support column sorting, column resizing, and cell formatting.
  * **Advanced Highcharts types** : Generate gauges, heatmaps, treemaps, and Sankey diagrams that standard dashboard tiles don't support.



### Test Looker platform features

Verify that your Data App integrates with Looker workflows:

  * **Cross-filtering** : Configure charts so that selecting a category in one chart filters the remaining visualizations.
  * **PDF export** : Download the entire dashboard as a PDF.
  * **Scheduled delivery** : Set up an automated schedule to send a PDF snapshot of your Data App to your team by email.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
