---
url: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference/
title: A2UI component gallery reference \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:33.472907+00:00
---

# A2UI component gallery reference  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  A2UI component gallery reference Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a comprehensive reference for all available A2UI components, including layout, display, interactive, and container components, as well as common properties.

## Material catalog components and basic catalog components

A2UI provides two distinct component catalogs for building agent user interfaces: the material catalog and the basic catalog.

**Note:** The basic catalog is referred to as the "standard catalog" in v0.8. See the [0.8 component model documentation](https://a2ui.org/specification/v0.8-a2ui/#section-2-the-component-model) for information.

The _material catalog_ contains components specifically designed to adhere to Google Material Design guidelines, offering a richer, more styled set of UI elements that are supported in A2UI v0.9 configurations.

The _basic catalog_ contains standard, design-system-agnostic UI primitives—such as layouts, actions, and inputs—supported in both A2UI v0.9 and v0.8 configurations.

## Material catalog components

This section provides a reference for available A2UI Material Design components, including layout, display, navigation, and input components.

**Note:** The A2UI Material Catalog components are supported in A2UI version v0.9 configurations. For more information about A2UI versions, see [Specification Versions](https://a2ui.org/#specification-versions) in the A2UI documentation.

## Material catalog common properties

All components, regardless of their specific type, share a set of common properties that can be configured:

Property | Required | Description  
---|---|---  
`id` | Yes | A unique identifier for the component within the current surface.  
`accessibility` | No | Attributes to improve accessibility, such as labels and roles.  
`weight` | No |  A value used in `MaterialRow` or `MaterialColumn` layouts to control how much space the component takes up relative to its siblings, similar to `flex-grow`.   
  
## Material catalog layout components

Layout components are used to structure and arrange other components within the user interface.

### MaterialCard

Material Design card container.

The following table outlines the properties available for the `MaterialCard` component:

Property | Required | Default Value | Description  
---|---|---|---  
`children` | Yes | - | Defines the children IDs.  
`appearance` | No | `raised` | The card appearance style. One of: "outlined", "raised".  
`align` | No | `start` | Alignment of children. One of: "center", "end", "start", "stretch".  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`href` | No | - | Optional URL to navigate to when the card is clicked. When set, the card becomes interactive and opens the URL in a new tab.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialCard",
        "appearance": "outlined",
        "children": [
          "card-content"
        ]
      },
      {
        "id": "card-content",
        "component": "MaterialText",
        "text": "Card content"
      }
    ]
    

### MaterialColumn

Layout container that arranges items vertically using Material guidelines.

The following table outlines the properties available for the `MaterialColumn` component:

Property | Required | Default Value | Description  
---|---|---|---  
`children` | Yes | - | Defines the children IDs.  
`justify` | No | `start` | Defines the arrangement of children along the main axis (vertically). One of: "start", "center", "end", "spaceBetween", "spaceAround", "spaceEvenly".  
`align` | No | `stretch` | Horizontal alignment of children ("start", "center", "end", "stretch").  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialColumn",
        "children": [
          "demo-column-header",
          "demo-column-content",
          "demo-column-footer"
        ],
        "justify": "start",
        "align": "stretch"
      },
      {
        "id": "demo-column-header",
        "component": "MaterialText",
        "text": "Header",
        "usageHint": "h2"
      },
      {
        "id": "demo-column-content",
        "component": "MaterialText",
        "text": "Content goes here",
        "usageHint": "body"
      },
      {
        "id": "demo-column-footer",
        "component": "MaterialText",
        "text": "Footer",
        "usageHint": "caption"
      }
    ]
    

### MaterialDialog

Material Design menu dialog container.

The following table outlines the properties available for the `MaterialDialog` component:

Property | Required | Default Value | Description  
---|---|---|---  
`open` | No | `false` | Whether the dialog is open. Can be a literal boolean or a data binding reference.  
`title` | No | - | The title of the dialog.  
`disableClose` | No | `false` | Whether the user can close the dialog by clicking outside or pressing Escape.  
`width` | No | - | The width of the dialog (e.g. "500px").  
`height` | No | - | The height of the dialog (e.g. "400px").  
`children` | Yes | - | Defines the children IDs.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialColumn",
        "children": [
          "open-button",
          "confirmation-dialog"
        ],
        "justify": "start",
        "align": "start"
      },
      {
        "id": "open-button",
        "component": "MaterialButton",
        "label": "Delete Item",
        "variant": "raised",
        "action": {
          "event": {
            "name": "requestDelete"
          }
        }
      },
      {
        "id": "confirmation-dialog",
        "component": "MaterialDialog",
        "open": {
          "path": "/app/dialogOpen"
        },
        "title": "Delete Confirmation",
        "children": [
          "dialog-layout"
        ]
      },
      {
        "id": "dialog-layout",
        "component": "MaterialColumn",
        "children": [
          "dialog-text",
          "dialog-actions"
        ],
        "justify": "start",
        "align": "stretch"
      },
      {
        "id": "dialog-text",
        "component": "MaterialText",
        "text": "Are you sure you want to permanently delete this item?"
      },
      {
        "id": "dialog-actions",
        "component": "MaterialRow",
        "children": [
          "cancel-button",
          "confirm-button"
        ],
        "justify": "end",
        "align": "center"
      },
      {
        "id": "cancel-button",
        "component": "MaterialButton",
        "label": "Cancel",
        "variant": "basic",
        "action": {
          "event": {
            "name": "closeDialog"
          }
        }
      },
      {
        "id": "confirm-button",
        "component": "MaterialButton",
        "label": "Delete",
        "variant": "raised",
        "action": {
          "event": {
            "name": "confirmDelete"
          }
        }
      }
    ]
    

### MaterialDivider

Material Design dividing line.

The following table outlines the properties available for the `MaterialDivider` component:

Property | Required | Default Value | Description  
---|---|---|---  
`inset` | No | `false` | Whether the divider is inset.  
`vertical` | No | `false` | Whether the divider is vertical.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialColumn",
        "children": [
          "text-above",
          "divider",
          "text-below"
        ],
        "justify": "start",
        "align": "stretch"
      },
      {
        "id": "text-above",
        "component": "MaterialText",
        "text": "This is the content above the divider."
      },
      {
        "id": "divider",
        "component": "MaterialDivider",
        "inset": false,
        "vertical": false
      },
      {
        "id": "text-below",
        "component": "MaterialText",
        "text": "This is the content below the divider."
      }
    ]
    

### MaterialExpansionPanel

Material Design expansion panel container.

The following table outlines the properties available for the `MaterialExpansionPanel` component:

Property | Required | Default Value | Description  
---|---|---|---  
`title` | No | - | The title displayed in the expansion panel header.  
`description` | No | - | The description displayed in the expansion panel header.  
`expanded` | No | `false` | Whether the panel is expanded. Can be a literal boolean or a data binding reference.  
`disabled` | No | `false` | Whether the expansion panel is disabled.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`children` | Yes | - | Defines the children IDs.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialExpansionPanel",
        "title": "Advanced Options",
        "description": "Configure advanced settings",
        "expanded": false,
        "children": [
          "panel-content"
        ]
      },
      {
        "id": "panel-content",
        "component": "MaterialText",
        "text": "Advanced settings content goes here"
      }
    ]
    

### MaterialGridList

A2UI container component for grid layout. Uses Angular Material Grid List to arrange child components into tiles.

The following table outlines the properties available for the `MaterialGridList` component:

Property | Required | Default Value | Description  
---|---|---|---  
`children` | Yes | - | Defines the children IDs.  
`cols` | No | `2` | Number of columns in the grid list. Can be a literal number or a data binding reference.  
`rowHeight` | No | `1:1` | Row height ratio or fixed height (e.g. "100px"). Can be a literal string or a data binding reference.  
`gutterSize` | No | `1px` | Size of the grid gutter. Can be a literal string or a data binding reference.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialGridList",
        "cols": 2,
        "rowHeight": "1:1",
        "gutterSize": "8px",
        "children": [
          "card-a",
          "card-b",
          "card-c",
          "card-d"
        ]
      },
      {
        "id": "card-a",
        "component": "MaterialCard",
        "children": [
          "text-a"
        ]
      },
      {
        "id": "text-a",
        "component": "MaterialText",
        "text": "Card A"
      },
      {
        "id": "card-b",
        "component": "MaterialCard",
        "children": [
          "text-b"
        ]
      },
      {
        "id": "text-b",
        "component": "MaterialText",
        "text": "Card B"
      },
      {
        "id": "card-c",
        "component": "MaterialCard",
        "children": [
          "text-c"
        ]
      },
      {
        "id": "text-c",
        "component": "MaterialText",
        "text": "Card C"
      },
      {
        "id": "card-d",
        "component": "MaterialCard",
        "children": [
          "text-d"
        ]
      },
      {
        "id": "text-d",
        "component": "MaterialText",
        "text": "Card D"
      }
    ]
    

### MaterialRow

Layout container that arranges items horizontally using Material guidelines.

The following table outlines the properties available for the `MaterialRow` component:

Property | Required | Default Value | Description  
---|---|---|---  
`children` | Yes | - | Defines the children IDs.  
`justify` | No | `start` | Defines the arrangement of children along the main axis (horizontally). One of: "start", "center", "end", "spaceAround", "spaceBetween", "spaceEvenly".  
`align` | No | `stretch` | Vertical alignment of children ("start", "center", "end", "stretch").  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialRow",
        "children": [
          "item-icon",
          "item-details",
          "item-action"
        ],
        "justify": "spaceBetween",
        "align": "center"
      },
      {
        "id": "item-icon",
        "component": "MaterialIcon",
        "icon": "shopping_bag",
        "color": "primary"
      },
      {
        "id": "item-details",
        "component": "MaterialColumn",
        "children": [
          "item-title",
          "item-subtitle"
        ],
        "justify": "start",
        "align": "start"
      },
      {
        "id": "item-title",
        "component": "MaterialText",
        "text": "Premium Wireless Headphones",
        "usageHint": "subtitle1"
      },
      {
        "id": "item-subtitle",
        "component": "MaterialText",
        "text": "$299.99 \u2022 Active Noise Cancelling",
        "usageHint": "caption"
      },
      {
        "id": "item-action",
        "component": "MaterialButton",
        "label": "Buy Now",
        "variant": "raised",
        "action": {
          "event": {
            "name": "buy_clicked"
          }
        }
      }
    ]
    

## Material catalog content components

Display and content components are used to present information, media, and status to the user.

### MaterialBadge

Displays a Material Design badge over a child element.

The following table outlines the properties available for the `MaterialBadge` component:

Property | Required | Default Value | Description  
---|---|---|---  
`text` | No | - | Text content to display in the badge.  
`color` | No | - | Color palette of the badge ("primary", "accent", "warn").  
`position` | No | `above after` | Position of the badge relative to the container ("above after", "above before", "below after", "below before").  
`size` | No | `medium` | Size of the badge ("small", "medium", "large").  
`overlap` | No | `true` | Whether the badge should overlap its container.  
`disabled` | No | `false` | Whether the badge is disabled.  
`hidden` | No | `false` | Whether the badge is hidden.  
`description` | No | - | Accessible description for the badge.  
`children` | Yes | - | Defines the children IDs.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialBadge",
        "text": "42",
        "color": "warn",
        "children": [
          "badge-content"
        ]
      },
      {
        "id": "badge-content",
        "component": "MaterialButton",
        "label": "Notifications"
      }
    ]
    

### MaterialIcon

Displays a Material Design icon.

The following table outlines the properties available for the `MaterialIcon` component:

Property | Required | Default Value | Description  
---|---|---|---  
`icon` | Yes | - | The name of the Material Icon to display.  
`color` | No | - | Color palette of the icon (primary, accent, warn).  
`tooltip` | No | - | Optional tooltip text to display on hover/focus.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialIcon",
        "icon": "favorite",
        "color": "warn"
      }
    ]
    

### MaterialImage

A2UI component for rendering an image in a Material Design context. Supports rounded corners, aspect ratio, and object-fit properties.

The following table outlines the properties available for the `MaterialImage` component:

Property | Required | Default Value | Description  
---|---|---|---  
`url` | Yes | - | The URL of the image to display.  
`alt` | No | - | Accessible alt text for the image.  
`fit` | No | - | Specifies how the image should be resized to fit its container. One of: "fill", "contain", "cover", "scaleDown", "none".  
`width` | No | - | Custom width of the image (e.g. "100px", "100%").  
`height` | No | - | Custom height of the image (e.g. "100px", "100%").  
`aspectRatio` | No | - | Custom aspect ratio of the image (e.g. "16/9", "1").  
`roundedCorners` | No | `false` | Whether to apply Material Design standard rounded corners.  
`borderRadius` | No | - | Custom border radius of the image (e.g. "50%", "12px"). Overrides roundedCorners.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialImage",
        "url": "https://www.gstatic.com/marketing-cms/assets/images/c5/3a/200414104c669203c62270f7884f/google-wordmarks-2x.webp=n-w100-h32-fcrop64=1,00000000ffffffff-rw",
        "width": "100px",
        "height": "32px",
        "fit": "scaleDown",
        "roundedCorners": true,
        "alt": "Google Wordmark"
      }
    ]
    

### MaterialProgressBar

A2UI wrapper for the Angular Material Progress Bar component. Supports determinate, indeterminate, buffer, and query modes.

The following table outlines the properties available for the `MaterialProgressBar` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | `0` | The progress value (0 to 100) in determinate and buffer modes.  
`mode` | No | `determinate` | The mode of the progress bar. One of: "determinate", "indeterminate", "buffer", "query".  
`bufferValue` | No | `0` | The buffer value (0 to 100) in buffer mode.  
`color` | No | - | Color palette of the progress bar ("primary", "accent", "warn").  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialProgressBar",
        "mode": "determinate",
        "value": 75,
        "bufferValue": 90,
        "color": "primary",
        "ariaLabel": "Loading progress"
      }
    ]
    

### MaterialProgressSpinner

A2UI wrapper for the Angular Material Progress Spinner component. Supports determinate and indeterminate modes, and custom dimensions.

The following table outlines the properties available for the `MaterialProgressSpinner` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | `0` | The progress value (0 to 100) in determinate mode.  
`mode` | No | `determinate` | The mode of the spinner. One of: "determinate", "indeterminate".  
`diameter` | No | `40` | The diameter of the progress spinner in pixels.  
`strokeWidth` | No | `4` | The width of the spinner stroke in pixels.  
`color` | No | - | Color palette of the spinner ("primary", "accent", "warn").  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialProgressSpinner",
        "mode": "indeterminate",
        "diameter": 40,
        "strokeWidth": 4,
        "color": "accent",
        "ariaLabel": "Loading data"
      }
    ]
    

### MaterialTable

A2UI wrapper for the Angular Material Table component. Renders structured data into columns and rows.

The following table outlines the properties available for the `MaterialTable` component:

Property | Required | Default Value | Description  
---|---|---|---  
`columns` | Yes | - | An array of column definitions, each specifying a {header, field} object.  
`rows` | Yes | - | The list of data rows. Can be an array of key-value records or a data binding reference.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`caption` | No | - | An accessible caption/description for the table.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialTable",
        "columns": [
          {
            "header": "ID",
            "field": "id"
          },
          {
            "header": "Name",
            "field": "name"
          },
          {
            "header": "Role",
            "field": "role"
          }
        ],
        "rows": {
          "path": "/company/users"
        }
      }
    ]
    

### MaterialText

Displays text with Material typography.

The following table outlines the properties available for the `MaterialText` component:

Property | Required | Default Value | Description  
---|---|---|---  
`text` | Yes | - | The text to be displayed. This can be a literal string or a reference to a value in the data model.  
`usageHint` | No | `body` | A hint for the typography style. One of: "h1", "h2", "h3", "h4", "h5", "subtitle1", "subtitle2", "body1", "body2", "body", "caption".  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialText",
        "text": "Headline Large (H1)",
        "usageHint": "h1"
      }
    ]
    

## Material catalog navigation components

Navigation and action components allow users to perform actions or navigate between views.

### MaterialButton

Material Design button.

The following table outlines the properties available for the `MaterialButton` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The text label to display on the button.  
`leadingIcon` | No | - | The name of the Material Icon to display before the label.  
`trailingIcon` | No | - | The name of the Material Icon to display after the label.  
`variant` | No | `basic` | The button style variant. One of: "raised", "flat", "stroked", "icon", "fab", "mini-fab", "basic".  
`appearance` | No | - | The visual appearance of the button. One of: "text", "filled", "elevated", "outlined", "tonal".  
`disabled` | No | `false` | Whether the button is disabled.  
`action` | No | - | The action to be dispatched when the button is clicked.  
`tooltip` | No | - | Tooltip text to display on hover.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`disableRipple` | No | `false` | Whether the ripple effect on click is disabled.  
`extended` | No | `false` | Whether the button is extended with additional label or icon space.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialButton",
        "label": "Raised Button",
        "variant": "raised",
        "tooltip": "Click me!",
        "action": {
          "event": {
            "name": "click"
          }
        }
      }
    ]
    

### MaterialIconButton

Material Design icon button.

The following table outlines the properties available for the `MaterialIconButton` component:

Property | Required | Default Value | Description  
---|---|---|---  
`icon` | Yes | - | The name of the Material Icon to display.  
`action` | Yes | - | The client-side action to be dispatched when the icon button is clicked.  
`ariaLabel` | Yes | - | Discernible text for screen readers. Recommended for accessibility since the button only contains an icon.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`color` | No | - | Color palette of the button (primary, accent, warn).  
`disabled` | No | `false` | Whether the button is disabled.  
`tooltip` | No | - | Tooltip text to display on hover.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialIconButton",
        "icon": "favorite",
        "ariaLabel": "Favorite",
        "color": "warn",
        "action": {
          "event": {
            "name": "click"
          }
        }
      }
    ]
    

### MaterialMenu

A2UI wrapper for the Angular Material Menu component. Provides a trigger button and drop-down menu items.

The following table outlines the properties available for the `MaterialMenu` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The text label displayed on the menu trigger button.  
`icon` | No | - | The name of the Material Icon to display on the trigger button.  
`disabled` | No | `false` | Whether the menu trigger button is disabled.  
`value` | No | - | The currently selected value. Can be a literal string or a data binding reference.  
`options` | Yes | - | The list of menu options available. Can be an array of {label, value} objects or a data binding reference.  
`action` | No | - | The client-side action to be dispatched when a menu item is selected.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialMenu",
        "label": "Options",
        "icon": "more_vert",
        "value": {
          "path": "/menu/selectedOption"
        },
        "options": [
          {
            "label": "Settings",
            "value": "settings"
          },
          {
            "label": "Help",
            "value": "help"
          },
          {
            "label": "Logout",
            "value": "logout"
          }
        ],
        "action": {
          "event": {
            "name": "menuSelection"
          }
        }
      }
    ]
    

### MaterialTabs

A2UI wrapper for the Angular Material Tabs component. Renders tabbed navigation and manages active tab selection.

The following table outlines the properties available for the `MaterialTabs` component:

Property | Required | Default Value | Description  
---|---|---|---  
`tabs` | Yes | - | An array of tab definitions, each specifying a {label, content} object.  
`activeTab` | No | `0` | The 0-based index of the currently active tab. Can be a literal number or a data binding reference.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialTabs",
        "activeTab": {
          "path": "/app/selectedTab"
        },
        "tabs": [
          {
            "label": "Overview",
            "content": "Overview content"
          },
          {
            "label": "Details",
            "content": "Details content"
          },
          {
            "label": "Reviews",
            "content": "Reviews content"
          }
        ]
      }
    ]
    

## Material catalog input components

Input and form components allow users to enter text, make selections, and toggle options.

### MaterialButtonToggle

Material Design button toggle group for single selection.

The following table outlines the properties available for the `MaterialButtonToggle` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | - | The currently selected value. This can be a literal string or a reference to a value in the data model.  
`options` | Yes | - | The list of options available for selection. Can be an array of {label, value} objects or a data binding reference.  
`disabled` | No | `false` | Whether the button toggle group is disabled.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`appearance` | No | `standard` | The appearance style of the button toggle group. One of: "legacy", "standard".  
`vertical` | No | `false` | Whether the button toggle group is arranged vertically.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialButtonToggle",
        "ariaLabel": "Text alignment",
        "value": {
          "path": "/user/alignment"
        },
        "options": [
          {
            "label": "Left",
            "value": "left"
          },
          {
            "label": "Center",
            "value": "center"
          },
          {
            "label": "Right",
            "value": "right"
          }
        ]
      }
    ]
    

### MaterialCheckbox

Material Design checkbox component for boolean state. For optimal accessibility, provide a descriptive label or use ariaLabel for assistive technologies.

The following table outlines the properties available for the `MaterialCheckbox` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The text label displayed next to the checkbox.  
`checked` | No | `false` | Whether the checkbox is checked. This can be a literal boolean or a reference to a value in the data model.  
`disabled` | No | `false` | Whether the checkbox is disabled.  
`color` | No | - | Color palette of the checkbox ("primary", "accent", "warn").  
`labelPosition` | No | `after` | Position of the label relative to the checkbox ("before", "after").  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`tooltip` | No | - | Tooltip text to display on hover.  
`checks` | No | - | An array of validation rules (each containing a dynamic boolean condition and an error message) that are reactively evaluated to determine the input's validity.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialCheckbox",
        "label": "Agree to Terms and Conditions",
        "ariaLabel": "Agree to Terms and Conditions",
        "checked": {
          "path": "/user/agreedToTerms"
        },
        "color": "primary"
      }
    ]
    

### MaterialChips

Material Design chip listbox component for single selection.

The following table outlines the properties available for the `MaterialChips` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | - | The currently selected value. This can be a literal string or a reference to a value in the data model.  
`options` | Yes | - | The list of chip options. Can be an array of {label, value} objects or a data binding reference.  
`disabled` | No | `false` | Whether the chip listbox is disabled.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`action` | No | - | The action to dispatch when a chip is selected.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialChips",
        "ariaLabel": "Filter by status",
        "value": {
          "path": "/user/status"
        },
        "options": [
          {
            "label": "All",
            "value": "all"
          },
          {
            "label": "Active",
            "value": "active"
          },
          {
            "label": "Completed",
            "value": "completed"
          }
        ]
      }
    ]
    

### MaterialDatepicker

Material Design datepicker component.

The following table outlines the properties available for the `MaterialDatepicker` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The label for the datepicker field.  
`placeholder` | No | - | The placeholder text.  
`value` | No | - | The current selected date in ISO format.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`disabled` | No | `false` | Whether the datepicker is disabled.  
`checks` | No | - | An array of validation rules (each containing a dynamic boolean condition and an error message) that are reactively evaluated to determine the input's validity.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialDatepicker",
        "label": "Appointment Date",
        "placeholder": "Choose a date",
        "ariaLabel": "Appointment Date",
        "value": {
          "path": "/appointment/date"
        }
      }
    ]
    

### MaterialInput

Material Design text input field.

The following table outlines the properties available for the `MaterialInput` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The label for the input field.  
`placeholder` | No | - | The placeholder text.  
`value` | No | - | The current value of the input. This can be a literal string or a reference to a value in the data model.  
`disabled` | No | `false` | Whether the input is disabled.  
`name` | No | - | The name of the input element.  
`readonly` | No | `false` | Whether the input is read-only.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`type` | No | `text` | The type of input control to display. One of: "text", "number", "email", "tel", "date". "password" is not allowed.  
`validationRegexp` | No | - | Regular expression for input validation.  
`checks` | No | - | An array of validation rules (each containing a dynamic boolean condition and an error message) that are reactively evaluated to determine the input's validity.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialInput",
        "label": "First Name",
        "placeholder": "John",
        "value": {
          "path": "/user/firstName"
        }
      }
    ]
    

### MaterialRadioButton

A2UI wrapper for the Angular Material Radio Button component. Supports single selection from a list of options within a radio group.

The following table outlines the properties available for the `MaterialRadioButton` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | - | The currently selected value. Can be a literal string or a data binding reference.  
`options` | Yes | - | The list of radio options available. Can be an array of {label, value} objects or a data binding reference.  
`disabled` | No | `false` | Whether the radio group is disabled.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`color` | No | - | Color palette of the radio button ("primary", "accent", "warn").  
`labelPosition` | No | `after` | Position of the label relative to the radio button. One of: "before", "after".  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialRadioButton",
        "ariaLabel": "Delivery options",
        "value": {
          "path": "/order/deliverySpeed"
        },
        "options": [
          {
            "label": "Standard",
            "value": "standard"
          },
          {
            "label": "Express",
            "value": "express"
          },
          {
            "label": "Next Day",
            "value": "nextDay"
          }
        ],
        "color": "primary",
        "labelPosition": "after"
      }
    ]
    

### MaterialSelect

Material Design select (drop-down) component for single selection. For optimal accessibility, always provide a descriptive label or use aria-label for assistive technologies.

The following table outlines the properties available for the `MaterialSelect` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The label for the select field.  
`placeholder` | No | - | The placeholder text shown when no value is selected.  
`value` | No | - | The current selected value. This can be a literal string or a reference to a value in the data model.  
`options` | Yes | - | The list of options available for selection. Can be an array of {label, value} objects or a data binding reference.  
`disabled` | No | `false` | Whether the select component is disabled.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`checks` | No | - | An array of validation rules (each containing a dynamic boolean condition and an error message) that are reactively evaluated to determine the input's validity.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialSelect",
        "label": "Favorite Color",
        "placeholder": "Choose a color",
        "ariaLabel": "Select your favorite color",
        "value": {
          "path": "/user/favoriteColor"
        },
        "options": [
          {
            "label": "Red",
            "value": "red"
          },
          {
            "label": "Green",
            "value": "green"
          },
          {
            "label": "Blue",
            "value": "blue"
          }
        ]
      }
    ]
    

### MaterialSlideToggle

A2UI wrapper for the Angular Material Slide Toggle component. Supports boolean toggle bindings and custom accessibility attributes.

The following table outlines the properties available for the `MaterialSlideToggle` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The text label displayed next to the slide toggle.  
`checked` | No | `false` | Whether the slide toggle is checked. Can be a literal boolean or a data binding reference.  
`disabled` | No | `false` | Whether the slide toggle is disabled.  
`required` | No | `false` | Whether the slide toggle is required.  
`color` | No | - | Color palette of the toggle ("primary", "accent", "warn").  
`labelPosition` | No | `after` | Position of the label relative to the toggle ("before", "after").  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`tooltip` | No | - | Tooltip text to display on hover.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialSlideToggle",
        "label": "Enable notifications",
        "ariaLabel": "Enable notifications toggle",
        "checked": {
          "path": "/settings/notifications"
        },
        "color": "accent",
        "labelPosition": "after"
      }
    ]
    

### MaterialSlider

A2UI wrapper for the Angular Material Slider component. Supports numeric value selection and range constraints.

The following table outlines the properties available for the `MaterialSlider` component:

Property | Required | Default Value | Description  
---|---|---|---  
`value` | No | `0` | The current value of the slider. Can be a literal number or a data binding reference.  
`min` | No | `0` | The minimum value of the slider.  
`max` | No | `100` | The maximum value of the slider.  
`step` | No | `1` | The step increment of the slider.  
`disabled` | No | `false` | Whether the slider is disabled.  
`color` | No | - | Color palette of the slider ("primary", "accent", "warn").  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialSlider",
        "min": 0,
        "max": 100,
        "step": 5,
        "value": {
          "path": "/audio/volume"
        },
        "color": "primary",
        "ariaLabel": "Volume adjustment"
      }
    ]
    

### MaterialTimepicker

A2UI wrapper for the Angular Material Timepicker component. Supports time selection and form field integration.

The following table outlines the properties available for the `MaterialTimepicker` component:

Property | Required | Default Value | Description  
---|---|---|---  
`label` | No | - | The text label for the timepicker field.  
`placeholder` | No | - | The placeholder text.  
`value` | No | - | The current selected time in ISO format. Can be a literal string or a data binding reference.  
`ariaLabel` | No | - | Discernible text for screen readers. Recommended for accessibility when no visible label is present.  
`ariaLabelledby` | No | - | Identifies the element (or elements) that labels the current element. Used for accessibility.  
`ariaDescribedby` | No | - | Identifies the element (or elements) that describes the current element. Used for accessibility.  
`disabled` | No | `false` | Whether the timepicker is disabled.  
`checks` | No | - | An array of validation rules (each containing a dynamic boolean condition and an error message) that are reactively evaluated to determine the input's validity.  
`style` | No | - | Inline styles to apply to the element.  
`weight` | No | - | Layout weight for the element when placed in a flex container.  
      
    
    [
      {
        "id": "root",
        "component": "MaterialTimepicker",
        "label": "Set Alarm",
        "placeholder": "Select time",
        "ariaLabel": "Set Alarm Time",
        "value": {
          "path": "/alarm/time"
        }
      }
    ]
    

## Basic catalog components

This section provides a reference for available A2UI basic catalog components.

**Note:** Gemini Enterprise supports A2UI versions v0.9 and v0.8. For more information about A2UI versions, see [Specification Versions](https://a2ui.org/#specification-versions) in the A2UI documentation.**Note:** The basic catalog is referred to as the "standard catalog" in v0.8. See the [0.8 component model documentation](https://a2ui.org/specification/v0.8-a2ui/#section-2-the-component-model) for information.

## Basic catalog schema files

For more information on these properties, see:

  * [**v0.9** basic catalog definition (JSON schema)](https://github.com/a2ui-project/a2ui/blob/main/specification/v0_9/catalogs/basic/catalog.json)
  * [**v0.8** standard catalog definition (JSON schema)](https://a2ui.org/specification/v0_8/standard_catalog_definition.json)



## Basic catalog common properties

All components, regardless of their specific type, share a set of common properties that can be configured:

Property | Required | Description  
---|---|---  
`id` | Yes | A unique identifier for the component within the current surface.  
`accessibility` | No | Attributes to improve accessibility, such as labels and roles.  
`weight` | No |  A value used in `Row` or `Column` layouts to control how much space the component takes up relative to its siblings, similar to `flex-grow`.   
  
## Basic catalog layout components

Layout components are used to structure and arrange other components within the user interface. The following layout components are available:

### Row

A `Row` is a layout component used to arrange its child components horizontally, from left to right. It acts as a container where you can place multiple components side-by-side. The exact spacing and positioning of the children within the row can be controlled using the `justify`/`distribution` and `align`/`alignment` properties.

The following table outlines the properties available for the `Row` component:

Property | Type/Values | Description  
---|---|---  
`children` |  **v0.9:** Array of component IDs or template definition  
**v0.8:** `explicitList` or `template` | The child components to be arranged horizontally within the Row.  
`justify` (v0.9)  
`distribution` (v0.8)  | `start`, `center`, `end`, `spaceBetween`, `spaceAround`, `spaceEvenly` | Controls how child components are distributed along the horizontal axis.  
`align` (v0.9)  
`alignment` (v0.8)  | `start`, `center`, `end`, `stretch` | Controls how child components are aligned on the vertical axis.  
  
### v0.9 JSON
    
    
    {
      "id": "toolbar",
      "component": "Row",
      "children": ["btn1", "btn2", "btn3"],
      "justify": "spaceBetween",
      "align": "center"
    }
    

### v0.8 JSON
    
    
    {
      "id": "toolbar",
      "component": {
        "Row": {
          "children": { "explicitList": ["btn1", "btn2", "btn3"] },
          "distribution": "spaceBetween",
          "alignment": "center"
        }
      }
    }
    

### Column

A `Column` is a layout component used to arrange its child components vertically, from top to bottom. It acts as a container where you can place multiple components one below the other. The exact spacing and positioning of the children within the column can be controlled using the `justify`/`distribution` and `align`/`alignment` properties.

The following table outlines the properties available for the `Column` component:

Property | Type/Values | Description  
---|---|---  
`children` |  **v0.9:** Array of component IDs or template definition  
**v0.8:** `explicitList` or `template` | The child components to be arranged vertically within the Column.  
`justify` (v0.9)  
`distribution` (v0.8)  |  `start`, `center`, `end`, `spaceBetween`, `spaceAround`, `spaceEvenly` | Controls how child components are distributed along the vertical axis.  
`align` (v0.9)  
`alignment` (v0.8)  |  `start`, `center`, `end`, `stretch` |  Controls how child components are aligned on the horizontal axis.   
  
### v0.9 JSON
    
    
    {
      "id": "content",
      "component": "Column",
      "children": ["header", "body", "footer"],
      "justify": "start",
      "align": "stretch"
    }
    

### v0.8 JSON
    
    
    {
      "id": "content",
      "component": {
        "Column": {
          "children": { "explicitList": ["header", "body", "footer"] },
          "distribution": "start",
          "alignment": "stretch"
        }
      }
    }
    

### List

A `List` is a layout component that displays a scrollable list of items. It supports static children and dynamic templates for generating items from data. The scroll direction can be vertical or horizontal.

The following table outlines the properties available for the `List` component:

Property | Type/Values | Description  
---|---|---  
`children` |  **v0.9:** Array of component IDs or template definition  
**v0.8:** `explicitList` or `template` | The items to be displayed in the list.  
`direction` | `vertical`, `horizontal` | The scroll direction of the list.  
`align` (v0.9)  
`alignment` (v0.8)  | `start`, `center`, `end`, `stretch` | Controls how list items are aligned on the cross axis.  
  
### v0.9 JSON
    
    
    {
      "id": "message-list",
      "component": "List",
      "children": {
        "componentId": "message-item",
        "path": "/messages"
      },
      "direction": "vertical"
    }
    

### v0.8 JSON
    
    
    {
      "id": "message-list",
      "component": {
        "List": {
          "children": {
            "template": {
              "dataBinding": "/messages",
              "componentId": "message-item"
            }
          },
          "direction": "vertical"
        }
      }
    }
    

## Basic catalog display components

Display components are used to present information to the user. The following display components are available:

### Text

The `Text` component displays text content and supports various styling hints, such as headings, captions, and body text.

The following table outlines the properties available for the `Text` component:

Property | Type/Values | Description  
---|---|---  
`text` |  **v0.9:** String or `DataBinding`  
**v0.8:** `BoundValue` | The text content to display.  
`variant` (v0.9)  
`usageHint` (v0.8)  | `h1`, `h2`, `h3`, `h4`, `h5`, `caption`, `body` | Styling hint for the text.  
  
### v0.9 JSON
    
    
    {
      "id": "title",
      "component": "Text",
      "text": "Welcome to A2UI",
      "variant": "h1"
    }
    

### v0.8 JSON
    
    
    {
      "id": "title",
      "component": {
        "Text": {
          "text": { "literalString": "Welcome to A2UI" },
          "usageHint": "h1"
        }
      }
    }
    

### Image

An `Image` component displays images from a specified URL and provides options to control how the image fits its container.

The following table outlines the properties available for the `Image` component:

Property | Type/Values | Description  
---|---|---  
`url` |  **v0.9:** String or `DataBinding`  
**v0.8:** `BoundValue` | The URL of the image to display.  
`fit` | String | How the image should fit its container (e.g., "cover").  
`variant` (v0.9)  
`usageHint` (v0.8)  | String | Hint for usage or styling variants (e.g., "hero").  
  
### v0.9 JSON
    
    
    {
      "id": "hero",
      "component": "Image",
      "url": "https://example.com/hero.png",
      "fit": "cover",
      "variant": "hero"
    }
    

### v0.8 JSON
    
    
    {
      "id": "hero",
      "component": {
        "Image": {
          "url": { "literalString": "https://example.com/hero.png" },
          "fit": "cover",
          "usageHint": "hero"
        }
      }
    }
    

### Icon

The `Icon` component displays icons from a standard set defined in the catalog.

The following table outlines the properties available for the `Icon` component:

Property | Type/Values | Description  
---|---|---  
`name` |  **v0.9:** String or `DataBinding`  
**v0.8:** `BoundValue` | The name of the icon to display (e.g., "check").  
  
### v0.9 JSON
    
    
    {
      "id": "check-icon",
      "component": "Icon",
      "name": "check"
    }
    

### v0.8 JSON
    
    
    {
      "id": "check-icon",
      "component": {
        "Icon": {
          "name": { "literalString": "check" }
        }
      }
    }
    

### Divider

The `Divider` component displays a visual separator line, which can be either horizontal or vertical.

The following table outlines the properties available for the `Divider` component:

Property | Type/Values | Description  
---|---|---  
`axis` | `horizontal`, `vertical` | The orientation of the divider line.  
  
### v0.9 JSON
    
    
    {
      "id": "separator",
      "component": "Divider",
      "axis": "horizontal"
    }
    

### v0.8 JSON
    
    
    {
      "id": "separator",
      "component": {
        "Divider": {
          "axis": "horizontal"
        }
      }
    }
    

## Basic catalog interactive components

Interactive components let you interact with the application, such as providing input or triggering actions. The following interactive components are available:

### Button

The `Button` component is a clickable element that triggers a specific action or event within the application.

The following table outlines the properties available for the `Button` component:

Property | Type/Values | Description  
---|---|---  
`child` | Component ID | The ID of the component to display inside the button (e.g., a Text component).  
`variant` (v0.9)  
`primary` (v0.8)  |  **v0.9:** String (e.g., `"primary"`)  
**v0.8:** Boolean  | The styling type or emphasis applied to the button.  
`action` |  **v0.9:** Event Object (e.g. keying `event`)   
**v0.8:** Action Object (e.g. keying `name`)  | The action to trigger when the button is clicked.  
  
### v0.9 JSON
    
    
    {
      "id": "submit-btn",
      "component": "Button",
      "child": "submit-text",
      "variant": "primary",
      "action": {
        "event": {
          "name": "submit_form"
        }
      }
    }
    

### v0.8 JSON
    
    
    {
      "id": "submit-btn",
      "component": {
        "Button": {
          "child": "submit-text",
          "primary": true,
          "action": {
            "name": "submit_form"
          }
        }
      }
    }
    

### TextField

The `TextField` is an interactive component that lets you input text. It also supports optional validation.

The following table outlines the properties available for the `TextField` component:

Property | Type/Values | Description  
---|---|---  
`label` |  **v0.9:** String  
**v0.8:** `BoundValue` | The label for the text field.  
`value` (v0.9)  
`text` (v0.8)  |  **v0.9:** String or `DataBinding`  
**v0.8:** `BoundValue` | The text content or bound path.  
`textFieldType` | `shortText`, `longText`, `number`, `obscured`, `date` | The type of text field.  
`validationRegexp` | String | Regular expression for validation.  
  
### v0.9 JSON
    
    
    {
      "id": "email-input",
      "component": "TextField",
      "label": "Email Address",
      "value": { "path": "/user/email" },
      "textFieldType": "shortText"
    }
    

### v0.8 JSON
    
    
    {
      "id": "email-input",
      "component": {
        "TextField": {
          "label": { "literalString": "Email Address" },
          "text": { "path": "/user/email" },
          "textFieldType": "shortText"
        }
      }
    }
    

### CheckBox

The `CheckBox` component is a boolean toggle that lets you switch a setting on or off.

The following table outlines the properties available for the `CheckBox` component:

Property | Type/Values | Description  
---|---|---  
`label` |  **v0.9:** String  
**v0.8:** `BoundValue` | The label for the checkbox.  
`value` |  **v0.9:** `DataBinding` (boolean)  
**v0.8:** `BoundValue` (boolean)  | The value of the checkbox (true/false) or bound path.  
  
### v0.9 JSON
    
    
    {
      "id": "terms-checkbox",
      "component": "CheckBox",
      "label": "I agree to the terms",
      "value": { "path": "/form/agreedToTerms" }
    }
    

### v0.8 JSON
    
    
    {
      "id": "terms-checkbox",
      "component": {
        "CheckBox": {
          "label": { "literalString": "I agree to the terms" },
          "value": { "path": "/form/agreedToTerms" }
        }
      }
    }
    

### Slider

The `Slider` component lets you select a numeric value from a specific range.

The following table outlines the properties available for the `Slider` component:

Property | Type/Values | Description  
---|---|---  
`value` |  **v0.9:** `DataBinding` (number)  
**v0.8:** `BoundValue` (number)  | The current value of the slider or bound path.  
`minValue` | Number | The minimum value of the range.  
`maxValue` | Number | The maximum value of the range.  
  
### v0.9 JSON
    
    
    {
      "id": "volume",
      "component": "Slider",
      "value": { "path": "/settings/volume" },
      "minValue": 0,
      "maxValue": 100
    }
    

### v0.8 JSON
    
    
    {
      "id": "volume",
      "component": {
        "Slider": {
          "value": { "path": "/settings/volume" },
          "minValue": 0,
          "maxValue": 100
        }
      }
    }
    

### DateTimeInput

The `DateTimeInput` component lets you pick a date and time.

The following table outlines the properties available for the `DateTimeInput` component:

Property | Type/Values | Description  
---|---|---  
`value` |  **v0.9:** `DataBinding`  
**v0.8:** `BoundValue` | The selected date/time value or bound path.  
`enableDate` | Boolean | Whether to enable date selection.  
`enableTime` | Boolean | Whether to enable time selection.  
  
### v0.9 JSON
    
    
    {
      "id": "date-picker",
      "component": "DateTimeInput",
      "value": { "path": "/booking/date" },
      "enableDate": true,
      "enableTime": false
    }
    

### v0.8 JSON
    
    
    {
      "id": "date-picker",
      "component": {
        "DateTimeInput": {
          "value": { "path": "/booking/date" },
          "enableDate": true,
          "enableTime": false
        }
      }
    }
    

### ChoicePicker (v0.9) / MultipleChoice (v0.8)

Select one or more options from a list. Note that this component has been renamed into **ChoicePicker** in v0.9 from **MultipleChoice** in v0.8.

The following table outlines the properties available:

Property | Type/Values | Description  
---|---|---  
`options` | Array of Objects | The list of options selectable by the user. Each option should have a label (string in v0.9, BoundValue in v0.8) and a value.  
`selections` |  **v0.9:** `DataBinding`  
**v0.8:** `BoundValue` | The selected values or bound path.  
`maxAllowedSelections` | Number | The maximum number of selections allowed.  
  
### v0.9 JSON
    
    
    {
      "id": "country-select",
      "component": "ChoicePicker",
      "options": [
        { "label": "USA", "value": "us" },
        { "label": "Canada", "value": "ca" }
      ],
      "selections": { "path": "/form/country" },
      "maxAllowedSelections": 1
    }
    

### v0.8 JSON
    
    
    {
      "id": "country-select",
      "component": {
        "MultipleChoice": {
          "options": [
            { "label": { "literalString": "USA" }, "value": "us" },
            { "label": { "literalString": "Canada" }, "value": "ca" }
          ],
          "selections": { "path": "/form/country" },
          "maxAllowedSelections": 1
        }
      }
    }
    

## Basic catalog container components

Container components are used to group and organize other components. The following container components are available:

### Card

A `Card` component is a container with elevation, a border, and padding that groups related content.

The following table outlines the properties available for the `Card` component:

Property | Type/Values | Description  
---|---|---  
`child` | Component ID | The ID of the component to display inside the card.  
  
### v0.9 JSON
    
    
    {
      "id": "info-card",
      "component": "Card",
      "child": "card-content"
    }
    

### v0.8 JSON
    
    
    {
      "id": "info-card",
      "component": {
        "Card": {
          "child": "card-content"
        }
      }
    }
    

### Modal

A `Modal` component is an overlay dialog triggered by an entry point component.

The following table outlines the properties available for the `Modal` component:

Property | Type/Values | Description  
---|---|---  
`entryPointChild` | Component ID | The ID of the component that triggers the modal (e.g., a Button).  
`contentChild` | Component ID | The ID of the component to display as the content of the modal.  
  
### v0.9 JSON
    
    
    {
      "id": "confirmation-modal",
      "component": "Modal",
      "entryPointChild": "open-modal-btn",
      "contentChild": "modal-content"
    }
    

### v0.8 JSON
    
    
    {
      "id": "confirmation-modal",
      "component": {
        "Modal": {
          "entryPointChild": "open-modal-btn",
          "contentChild": "modal-content"
        }
      }
    }
    

### Tabs

A `Tabs` component provides a tabbed interface for organizing content into switchable panels.

The following table outlines the properties available for the `Tabs` component:

Property | Type/Values | Description  
---|---|---  
`tabItems` | Array of Objects | The list of tabs. Each item should have a `title` (string in v0.9, BoundValue in v0.8) and a `child` (component ID).  
  
### v0.9 JSON
    
    
    {
      "id": "settings-tabs",
      "component": "Tabs",
      "tabItems": [
        { "title": "General", "child": "general-tab" },
        { "title": "Privacy", "child": "privacy-tab" }
      ]
    }
    

### v0.8 JSON
    
    
    {
      "id": "settings-tabs",
      "component": {
        "Tabs": {
          "tabItems": [
            { "title": { "literalString": "General" }, "child": "general-tab" },
            { "title": { "literalString": "Privacy" }, "child": "privacy-tab" }
          ]
        }
      }
    }
    

## Version differences summary

The component names and properties are largely the same across versions. The structural differences are:

Aspect | v0.8 | v0.9  
---|---|---  
Component wrapper | `"component": { "Text": { ... } }` | `"component": "Text", ...props`  
String values | `{ "literalString": "Hello" }` | `"Hello"`  
Children | `{ "explicitList": ["a", "b"] }` | `["a", "b"]`  
Data binding | `{ "path": "/data" }` | `{ "path": "/data" }` (same)  
Text/Image styling | `usageHint` | `variant`  
Button styling | `primary: true` | `variant: "primary"`  
Action format | `{ "name": "..." }` | `{ "event": { "name": "..." } }`  
Choice component | `MultipleChoice` | `ChoicePicker`  
Layout alignment | `distribution`, `alignment` | `justify`, `align`  
TextField value | `text` | `value`  
  
## Evolution guide

For information on moving from v0.8 to v0.9, see the [v0.8 to v0.9 Evolution Guide](https://a2ui.org/specification/v0.9-evolution-guide/)

## Live examples

To see all components in action:
    
    
    cd samples/client/angular
    yarn start gallery
    

**Note:** **Package Manager Usage:** Running the built-in sample applications within the A2UI repository requires Yarn (`yarn start gallery`) as configured by Corepack workspaces. For your own regular usage and standalone projects outside this repository, use the package manager of your choice (e.g. npm, pnpm).

## What's next

  * [**Defining Your Own Catalog**](https://a2ui.org/guides/defining-your-own-catalog/): Build your own components
  * [**Theming Guide**](https://a2ui.org/guides/theming/): Style components to match your brand



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
