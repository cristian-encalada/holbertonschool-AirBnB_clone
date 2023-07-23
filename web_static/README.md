# AirBnB clone - Web static

## Table of contents

   1. [Background Context](#background-context)
   2. [Requirements](#requirements)
   3. [Mandatory Tasks](#mandatory-tasks)
   4. [Advanced Tasks](#advanced-tasks)
   5. [Author](#author)

## Background Context

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

## Requirements

### Python scripts

* Allowed editors: ``vi``, ``vim``, ``emacs``
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be W3C compliant and validate with W3C-Validator
* All your CSS files should be in `styles` folder
* All your images should be in `images` folder
* You are not allowed to use `!important` and `id` (`#...` in the CSS file)
* You are not allowed to use tags `img`, `embed` and `iframe`
* You are not allowed to use Javascript
* Current screenshots have been done on `Chrome 56` or more.
* No cross browsers
* You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

 <img align="center" alt="AirBnB_web_static" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_web_static.png?raw=true" />

## Mandatory Tasks

### 0. Inline styling

Write an HTML page that displays a header and a footer.

Layout:

* Body:
    * no margin
    * no padding
* Header:
    * color #FF0000 (red)
    * height: 70px
    * width: 100%
* Footer:
    * color #00FF00 (green)
    * height: 60px
    * width: 100%
    * text `Holberton School` center vertically and horizontally
    * always at the bottom at the page

__Requirements:__

* You must use the header and footer tags
* You are not allowed to import any files
* You are not allowed to use the style tag in the head tag
* Use inline styling for all your tags


 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_0.png?raw=true" />

File: [0-index.html](./0-index.html)

### 1. Head styling

Write an HTML page that displays a header and a footer by using the `style` tag in the head tag (same as `0-index.html`)

__Requirements:__

* You must use the `header` and `footer` tags
* You are not allowed to import any files
* No inline styling
* You must use the `style` tag in the `head` tag

The layout must be exactly the same as `0-index.html`

File: [1-index.html](./1-index.html)

### 2. CSS files

Write an HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)

__Requirements:__

* You must use the `header` and `footer` tags
* No inline styling
* You must have 3 CSS files:
    * `styles/2-common.css`: for global style (i.e. the body style)
    * `styles/2-header.css`: for header style
    * `styles/2-footer.css`: for footer style

The layout must be exactly the same as `1-index.html`

Files:

* [2-index.html](./2-index.html)
* [styles/2-common.css](./styles/2-common.css)
* [styles/2-header.css](./styles/2-header.css)
* [styles/2-footer.css](./styles/2-footer.css)

### 3. Zoning done! 

Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

* Common:
    * no margin
    * no padding
    * font color: #484848
    * font size: 14px
    * font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
    * icon in the browser tab
* Header:
    * color: white
    * height: 70px
    * width: 100%
    * border bottom 1px #CCCCCC
    * logo align on left and center vertically (20px space at the left)
* Footer:
    * color white
    * height: 60px
    * width: 100%
    * border top 1px #CCCCCC
    * text Best School center vertically and horizontally
    * always at the bottom at the page

__Requirements:__

* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 3 CSS files:
    * `styles/3-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_3.png?raw=true" />

Files:

* [3-index.html](./3-index.html)
* [styles/3-common.css](./styles/3-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [images/](./images/)

### 4. Search! 

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)

* Container:
    * between header and footer tags, add a div:
        * classname: container
        * max width 1000px
        * margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
        * center horizontally
* Filter section:
    * tag section
    * classname filters
    * inside the .container
    * color white
    * height: 70px
    * width: 100% of the container
    * border 1px #DDDDDD with radius 4px
* Button search:
    * tag button
    * text Search
    * font size: 18px
    * inside the section filters
    * background color #FF5A5F
    * text color #FFFFFF
    * height: 48px
    * width: 20% of the section filters
    * no borders
    * border radius: 4px
    * center vertically and at 30px of the right border
    * change opacity to 90% when the mouse is on the button

__Requirements:__

* You must use: `header`, `footer`, `section`, `button` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 4 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/4-filters.css`: for the filters style

`4-index.html` __won’t be W3C valid__, don’t worry, it’s temporary

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_4.png?raw=true" />

Files:

* [4-index.html](./4-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/4-filters.css](./styles/4-filters.css)
* [images/](./images/)

### 5. More filters 

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

* Locations and Amenities filters:
    * tag: div
    * classname: locations for location tag and amenities for the other
    * inside the section filters (same level as the button Search)
    * height: 100% of the section filters
    * width: 25% of the section filters
    * border right #DDDDDD 1px only for the first left filter
    * contains a title:
        * tag: h3
        * font weight: 600
        * text States or Amenities
    * contains a subtitle:
        * tag: h4
        * font weight: 400
        * font size: 14px
        * text with fake contents

__Requirements:__

* You must use: header, footer, section, button, h3, h4 tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 4 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/5-filters.css`: for the filters style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_5.png?raw=true" />

Files:

* [5-index.html](./5-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/5-filters.css](./styles/5-filters.css)
* [images/](./images/)


### 6. It's (h)over 

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
    * tag ul
    * classname popover
    * text should be fake now
    * inside each div
    * not displayed by default
    * color #FAFAFA
    * width same as the div filter
    * border #DDDDDD 1px with border radius 4px
    * no list display
    * Location filter has 2 levels of ul/li:
        * state -> cities
        * state name must be display in a h2 tag (font size 16px)

__Requirements:__

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 4 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_6.1.png?raw=true" />

  <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_6.2.png?raw=true" />

Files:

* [5-index.html](./5-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/6-filters.css](./styles/6-filters.css)
* [images/](./images/)

### 7. Display results 

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

* Add Places section:
    * tag: section
    * classname: places
    * same level as the filters section, inside .container
    * contains a title:
        * tag: h1
        * text: Places
        * align in the top left
        * font size: 30px
    * contains multiple “Places” as listing (horizontal or vertical) describe by:
        * tag: article
        * width: 390px
        * padding and margin 20px
        * border #FF5A5F 1px with radius 4px
        * contains the place name:
            * tag: h2
            * font size: 30px
            * center horizontally

__Requirements:__

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/7-places.css`: for the places style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_7.png?raw=true" />

Files:

* [5-index.html](./5-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/6-filters.css](./styles/6-filters.css)
* [styles/7-places.css](./styles/7-places.css)
* [images/](./images/)

### 8. More details 

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:

* Price by night:
    * tag: div
    * classname: price_by_night
    * same level as the place name
    * font color: #FF5A5F
    * border: #FF5A5F 4px rounded
    * min width: 60px
    * height: 60px
    * font size: 30px
    * align: the top right (with space)
* Information section:
    * tag: div
    * classname: information
    * height: 80px
    * border: top and bottom #DDDDDD 1px
    * contains (align vertically):
        * Number of guests:
            * tag: div
            * classname: max_guest
            * width: 100px
            * fake text
            * icon
        * Number of bedrooms:
            * tag: div
            * classname: number_rooms
            * width: 100px
            * fake text
            * icon
        * Number of bathrooms:
            * tag: div
            * classname: number_bathrooms
            * width: 100px
            * fake text
            * icon
* User section:
    * tag: div
    * classname: user
    * text Owner: `<fake text>`
    * Owner text should be in bold
* Description section:
    * tag: div
    * classname: description

__Requirements:__

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/8-places.css`: for the places style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_8.png?raw=true" />

Files:

* [5-index.html](./5-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/6-filters.css](./styles/6-filters.css)
* [styles/8-places.css](./styles/8-places.css)
* [images/](./images/)

## Advanced Tasks

### 9. Full details 

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 8-index.html)

Add more information to a Place article:

* List of Amenities:
    * tag div
    * classname amenities
    * margin top 40px
    * contains:
        * title:
            * tag h2
            * text Amenities
            * font size 16px
            * border bottom #DDDDDD 1px
        * list of amenities:
            * tag ul / li
            * no list style
            * icons on the left: Pet friendly, TV, Wifi, etc… feel free to add more
* List of Reviews:
    * tag div
    * classname reviews
    * margin top 40px
    * contains:
        * title:
            * tag h2
            * text Reviews
            * font size 16px
            * border bottom #DDDDDD 1px
        * list of review:
            * tag ul / li
            * no list style
            * a review is described by:
                * h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
                * p tag for the text (font size 12px)

__Requirements:__

* You must use: header, footer, section, button, h3, h4, ul, li tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All `images` must be stored in the images folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (i.e body style)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/100-places.css`: for the places style

 <img align="center" alt="web_static_0" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/web_static_9.png?raw=true" />

Files:

* [5-index.html](./5-index.html)
* [styles/4-common.css](./styles/4-common.css)
* [styles/3-header.css](./styles/3-header.css)
* [styles/3-footer.css](./styles/3-footer.css)
* [styles/6-filters.css](./styles/6-filters.css)
* [styles/100-places.css](./styles/100-places.css)
* [images/](./images/)

### 10. Flex

Improve the Places section by using [Flexible boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) for all Place articles

Check [Flexbox Froggy](http://flexboxfroggy.com/)

### 11. Responsive design

Improve the page by adding [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly in mobile or small screens.

Examples:

* no horizontal scrolling
* redesign search bar depending of the width
* etc.

### 12. Accessibility

Improve the page by adding [Accessibility support](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

Examples:

* Colors contrast
* Header tags
* etc.


## Author

* __Cristian Encalada__ - *Holberton Student* 
    - Github: [Cristian Encalada](https://github.com/cristian-encalada/)
