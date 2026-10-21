---
url: https://docs.cloud.google.com/looker/docs/components-example/
title: Building a tabbed dashboard with Looker components \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:00:24.029049+00:00
---

# Building a tabbed dashboard with Looker components  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/components-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Building a tabbed dashboard with Looker components Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** We recommend that you use the [**Tabbed Dashboards** feature](https://docs.cloud.google.com/looker/docs/tabbed-dashboards) to add tabs to dashboards by using dashboard edit options. Tabs let you better organize content, improve data storytelling, enhance performance, and reduce clutter.

One example of how UI components can enhance an embedded application is to use them to create tabbed navigation for dashboards:

![A sample dashboard with a tabbed interface.](https://docs.cloud.google.com/static/looker/docs/images/components-tabbed-dash-2206.png)

The following example adds tabbed dashboards to [a basic TypeScript extension](https://docs.cloud.google.com/looker/docs/extension-intro-to-building) that was built using Looker's extension framework.

To work through this example, make sure your setup meets the requirements and then use these steps:

  1. Build a basic TypeScript extension.
  2. Create the file `src/Dashboards.tsx` to connect and store dashboards.
  3. Create the file `src/Tabs.tsx` to store the `Tabs` component.
  4. Replace the HelloWorld reference in `src/App.tsx`.
  5. Update the `manifest.lkml` file with embed entitlement.
  6. Publish the extension to your Looker instance.



## Requirements

You will need a few elements before you start:

  * You must have access to a Looker instance with the [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) enabled.
  * You must have [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission.
  * You should have several [user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) within Looker to place within the UI tabs.
  * Whether you're building in the extension framework or in your own standalone React application, it is important to authenticate with Looker's API and have access to the Looker SDK object. Read about [Looker API authentication](https://docs.cloud.google.com/looker/docs/api-auth) or our [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) for more information.
  * This example uses the [Looker Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk). To allow the Embed SDK to run against your instance, `http://localhost:8080` must be included in the [Embedded Domain Allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#embedded_domain_allowlist) inside the **Embed** page of the **Admin** panel.
  * Make sure that you have installed the Looker Components [NPM package](https://www.npmjs.com/package/@looker/components). Information on installing and using the components package can be found in the README document, available on both GitHub and NPM:

    * [Installing and using the components package (GitHub)](https://github.com/looker-open-source/components#readme)
    * [Installing and using the components package (NPM)](https://www.npmjs.com/package/@looker/components)



## Step 1: Build a basic TypeScript extension

To build an extension, follow the instructions on the [Introduction to building a Looker extension](https://docs.cloud.google.com/looker/docs/extension-intro-to-building) documentation page. To make the extension a TypeScript extension, use the following modifications:

  * If you [use the `create-looker-extension` tool](https://docs.cloud.google.com/looker/docs/extension-intro-to-building#using_create-looker-extension_to_create_an_extension_template) to create the extension template, choose React for the framework and TypeScript for the language.
  * If you [clone the Git repository](https://docs.cloud.google.com/looker/docs/extension-intro-to-building#cloning_a_git_repository_to_create_an_extension_template) to create the extension template, navigate to the `extension-examples/react/TypeScript/helloworld-ts` directory in the second step.



## Step 2: Create the file `src/Dashboards.tsx` to connect and store dashboards

Inside the `src` directory of your new extension, create a `Dashboards.tsx` file. This file will connect and store the dashboards that you've built inside Looker.

Inside the file, paste the following code. This code creates a reusable dashboard component.

**There is one location in the code of an instance URL,`https://mycompany.looker.com`. Change this to your Looker instance URL.**
    
    
    import React, { useCallback } from "react";
    import { LookerEmbedSDK } from "@looker/embed-sdk";
    import styled from "styled-components";
    
    export const EmbeddedDashboard = (props: { id: number | string }) => {
     const [dashboard, setDashboard] = React.useState();
     const setupDashboard = (dashboard: any) => {
       setDashboard(dashboard);
     };
     const embedCtrRef = useCallback((el) => {
       const hostUrl = "https://mycompany.looker.com";
       if (el && hostUrl) {
         el.innerHTML = "";
         LookerEmbedSDK.init(hostUrl);
         LookerEmbedSDK.createDashboardWithId(props.id)
           .withNext()
           .appendTo(el)
           .build()
           .connect()
           .then(setupDashboard)
           .catch((error) => {
             console.error("Connection error", error);
           });
       }
     }, []);
     return <EmbedContainer ref={embedCtrRef}></EmbedContainer>;
    };
    
    export const EmbedContainer = styled.div`
     width: 100%;
     height: 95vh;
     & > iframe {
       width: 100%;
       height: 100%;
     }
    `;
    

In the previous code example, the following things are happening:

  * The import statements are bringing in the needed dependencies.
        
        import React, { useCallback } from "react";
        import { LookerEmbedSDK } from "@looker/embed-sdk";
        import styled from "styled-components";
        

  * The next code block creates an `EmbeddedDashboard` object, which is an `EmbedContainer` object that contains a dashboard iframe. This component is reusable; you can use it for any dashboard by passing a different `id` property. The iframe is generated from the [Looker Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk) by using the dashboard ID that is passed to it. **Be sure to update`https://mycompany.looker.com/` to your Looker instance URL.**
        
        export const EmbeddedDashboard = (props: { id: number | string }) => {
        const [dashboard, setDashboard] = React.useState();
        const setupDashboard = (dashboard: any) => {
          setDashboard(dashboard);
        };
        const embedCtrRef = useCallback((el) => {
          const hostUrl = "https://mycompany.looker.com/";
          if (el && hostUrl) {
            el.innerHTML = "";
            LookerEmbedSDK.init(hostUrl);
            LookerEmbedSDK.createDashboardWithId(props.id)
              .withNext()
              .appendTo(el)
              .build()
              .connect()
              .then(setupDashboard)
              .catch((error) => {
                console.error("Connection error", error);
              });
          }
        }, []);
        return <EmbedContainer ref={embedCtrRef}></EmbedContainer>;
        };
        

  * The final block styles the EmbedContainer.
        
        export const EmbedContainer = styled.div`
            width: 100%;
            height: 95vh;
            & > iframe {
              width: 100%;
              height: 100%;
            }
        `;
        




## Step 3: Create the file `src/Tabs.tsx` to store the `Tabs` component

Inside the `src` directory of your new extension, create a `Tabs.tsx` file. This file stores the `Tabs` component and references the Looker dashboard ID for each dashboard.

Inside that file, paste the following code (the section following this one explains what the code is doing):
    
    
    import React from "react";
    import { ComponentsProvider, Tabs2, Tab2 } from "@looker/components";
    import { EmbeddedDashboard } from "./Dashboards";
    
    export const Tabs = () => (
     <ComponentsProvider>
       <Tabs2>
         <Tab2 id="5" label="Order Analysis Dashboard">
          Order data from the last 12 months
           <EmbeddedDashboard1 id={5} />
         </Tab2>
         <Tab2 id="2" label="Inventory Dashboard">
           Current global inventory
           <EmbeddedDashboard2 id={2} />
         </Tab2>
         <Tab2 id="7" label="Customer Dashboard">
           Anonymized customer data
           <EmbeddedDashboard3 id={7} />
         </Tab2>
       </Tabs2>
     </ComponentsProvider>
    )
    

In the previous code example, the following things are happening:

  * The import statements are bringing in the needed dependencies and components, as well as the `EmbeddedDashboard` objects that were created in the `Dashboards.tsx` file.
        
        import React from "react";
        import { ComponentsProvider, Tabs2, Tab2 } from "@looker/components";
        import { EmbeddedDashboard } from "./Dashboard";
        

  * The export statement makes the `Tabs` object available to be imported into other components.
        
        export const Tabs = () => (
        

  * The `ComponentsProvider` wraps around individual components to help with theming.
        
        <ComponentsProvider>
        </ComponentsProvider>
        

  * The [`Tabs2` component and its child component, `Tab2`, create three tabs](https://looker-open-source.github.io/components/latest/?path=/docs/docs-tabs2--docs) and link them to the Looker dashboards.
        
        <Tabs2>
         <Tab2 id="5" label="Order Analysis Dashboard">
          Order data from the last 12 months
           <EmbeddedDashboard id={5} />
         </Tab2>
         <Tab2 id="2" label="Inventory Dashboard">
           Current global inventory
           <EmbeddedDashboard id={2} />
         </Tab2>
         <Tab2 id="7" label="Customer Dashboard">
           Anonymized customer data
           <EmbeddedDashboard id={7} />
         </Tab2>
        </Tabs2>
        

    * The `id` property of `Tab2` accepts a unique tab ID. **Update the ID as necessary for your environment.**
    * The `label` property accepts the label that will appear on each tab. **Update the ID as appropriate for the dashboard that you're using.**
    * A string that is placed inside the Tab2 tags will appear at the top of the content area for that tab. **Update or remove the string as needed.**
    * The `EmbeddedDashboard` objects are placed within the tab. Their `id` properties accept the ID of the dashboard that is to be embedded inside that tab. **When you're building your own tabbed dashboard, replace this value with the ID for the dashboard that you want to use.** You can find the numeric dashboard ID in the URL after `dashboards/`. For example, if the URL is `https://example.looker.com/dashboards/61?Recording+Date=10+weeks&Country=US`, then the dashboard ID would be `61`.



## Step 4: Replace the HelloWorld reference in `src/App.tsx`

Navigate to your `App.tsx` file in the `src` directory. Remove the HelloWorld import statement:

`import { HelloWorld } from './HelloWorld'`

and replace it with:

`import { Tabs } from './Tabs'`

Additionally, in the `src/App.tsx` file, replace `<HelloWorld/>` with `<Tabs/>`.

Optionally, you can also delete the `HelloWorld.tsx` file from this directory since you will no longer be using it.

## Step 5: Update the `manifest.lkml` file with embed entitlement

Add the following [entitlement](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#use_embeds) to the entitlements section of the [`manifest.lkml` file](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) in your LookML project:

`use_embeds: yes`

The `manifest.lkml` file should look like this:
    
    
    application: name {
      label: "label"
      url: "http://localhost:8080/bundle.js"
      # file: "bundle.js
      entitlements: {
        core_api_methods: ["me"] #Add more entitlements here as you develop new functionality
        use_embeds: yes
      }
    }
    

Now you can navigate to your extension, which appears in the **Applications** folder in the left navigation panel. If you've started your local development server with `yarn develop`, you can see the embedded, tabbed dashboards.

## Step 6: Publish the extension to your Looker instance

To show the extension to other Looker users, publish the extension to your Looker instance by following these steps:

  1. With your development server running, navigate to `localhost:8080/bundle.js`.
  2. Save the content of the browser window locally on your computer as a `.js` file.
  3. Make sure you are in development mode, and then drag and drop the `.js` file into your extension project. Save your changes.
  4. In the `manifest.lkml` file, comment out the line `url: "http://localhost:8080/bundle.js"`.
  5. In the `manifest.lkml` file, uncomment the line `# file: "bundle.js"` and make sure the filename matches the filename of the `.js` file you uploaded to your project. Save your changes.
  6. [Commit and deploy](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production) your changes.



Once your changes are deployed, you will no longer need to start your local development server to see the extension, and users on your Looker instance should be able to see the extension if they navigate to it inside the **Applications** folder in the main navigation panel.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
