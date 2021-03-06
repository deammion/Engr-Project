# ENGR 301 Project *14* Project Proposal and Requirements Document
#### Isabella Tomaz Ketley, Jaya Narayan, Timothy McDermott, Dylan Simpson, Damien Tamasese, Nathan Wong, James Houlihan

## 1. Introduction

Web applications are accessed and used by everyone everywhere. Therefore, ensuring web application security is extremely important, yet it is becoming increasingly difficult. There are many vulnerabilities web applications are susceptible to. The number of potential vulnerabilities makes safeguarding against any exploitation of vulnerabilities very difficult. The exploitation of a single vulnerability may result in an entire website, or user account being compromised.   

XSS is one of the most common vulnerabilities which occurs whenever a web application trusts, or does not validate untrusted data. [1]. An XSS vulnerability can allow an attacker to execute scripts in an end user’s browser, access a user’s cookies, and could even result in an attacker compromising a user’s account [1]. Furthermore, an XSS attack can have huge consequences which are why implementing appropriate security measures are vital.

One way to mitigate the XSS attacks is to use CSP [2]. CSP is an added layer of security that can help protect against different attacks. CSP nonce tags are used to prevent XSS [3]. A nonce is a pseudo-random value intended for one-time use, meaning the nonce changes with each HTTP request [4]. This is to ensure an attacker cannot obtain the value of it. If an application contains script tags in the HTTP response, the nonce value is added as a tag to any trusted script tags within the application. Once the application is run, only script tags that have the correct nonce tag and value will be executed [4]. This ensures that only trusted script tags are allowed to be executed within an application. 

This project will use CSP headers and nonce tags to determine whether or not script tags should be run on a web application, to mitigate XSS attacks.   

### Client

Company: RedShield

Contact: Kirk Jackson <br>
Email: 	kirk@redshield.co <br>
Address: <br>
    RedShield <br>
    Level 12 <br>
    RedShield House <br>
    79 Boulcott St <br>

### 1.1 Purpose

The purpose of this project is to create a working prototype of a proxy plugin program. This program will be capable of reading, interpreting, and analyzing HTTP source code, with the intended purpose of preventing XSS from using CSP nonce tags.

### 1.2 Scope

The scope of this project is to create a proxy plugin capable of reading and interpreting HTTP responses to determine what script tags are safe and unsafe. This program will implement script fingerprinting for non-variable, and non-inline script tags, to prevent XSS attacks. Python unit tests will be used to ensure the validity of the program we create. 

### 1.3 Product overview 
#### 1.3.1 Product perspective

The project will produce a proxy plugin, that will be demonstrated to Red Shield and will assist with the development of their Red Core Shielding technology. The project does not need to directly access or use any of the components of the Red Core Shielding technology, nor does it need to be written in Elixir, which is the native coding language used by Red Core Shielding technology. Red Shield will handle the conversion from Python to Elixir once the project is completed.

The proxy plugin will intercept requests and responses to and from a target web application. This interaction will not interfere with the host server or its standard functionality, except for an unsafe XSS tag creating a browser warning.

The product will function in two phases, the first phase being the collection phase and the second being the operational phase.

During the collection phase, the program will store any HTTP responses sent by the host server to a local machine of the client. This data is then interpreted by the program so it can learn what a standard HTML response from the host server looks like. In doing so the program will then identify what it can consider a ‘safe’ script tag. 

During the operational phase, the program will continue to intercept the HTTP responses from the host server. The program will read and interpret the response, add CSP headers to the HTML response, mark all safe script tags with a nonce tag and send it to the end-user. Furthermore, the two CSP headers which will be inserted into all HTML responses are, Content-Security-Policy with a nonce and Content-Security-Policy-Report-Only with a report-URI URL. These CSP headers will be added to ensure nonce tags can be added to the responses and that any unsafe script tags will get reported to report-uri.com. This is the program's main purpose, automation of CSP in regards to scripting to prevent XSS attacks.

Any script that is not marked as safe will trigger a browser warning. These will be collected using the third-party tool report-uri.com.

#### 1.3.2 Product functions

As discussed above the project will produce a program that will be responsible for blocking XSS attacks by adding CSP protection to web applications. This will be done in the form of adding nonce tags to scripts that are deemed safe to run.  
 
To be able to do this the project will use the MITM proxy software, which enables the use of a proxy plugin. This proxy plugin will be placed on the infrastructure of the owner of a website that wants to use our protection, or on RedShield's infrastructure. This will allow for the proxy plugin to intercept incoming HTTP requests to the webserver before they reach the webserver and the HTTP Responses from the web server before they reach the client.  The HTTP responses will get stored in a secure location where the program will scan through the HTML located in the HTTP responses. As of our initial planning, the HTTP requests will not be required in our project. Two CSP headers will be inserted into all HTML responses. One containing a nonce (Content-Security-Policy) and one containing the URL for an externally generated report from report-uri (Content-Security-Policy-Report-Only). 
 
For the program to be able to differentiate which HTTP responses are safe to add nonce tags to, it will operate in two phases. 

#### Collection Phase

As discussed above, the project will produce a program that is responsible for blocking XSS attacks by adding CSP protection to web applications.  This CSP protection will be enabled through the addition of nonce tags to HTML script tags that have been deemed safe to run. 
 
To be able to achieve the above the program produced will use the MITM proxy software, which enables the use of a proxy plugin. This plugin will be implemented on top of the infrastructure of either; The owner of a website that wants to use our protection. Or on RedShield's infrastructure. This will allow the proxy plugin to intercept incoming HTTP requests to the webserver before they reach the webserver and the HTTP Responses from the web server before they reach the client.  The HTTP responses will get stored in a secure location where the program will scan through the HTML located in the HTTP responses. As of our initial planning, the HTTP requests will not be required in our project. Two CSP headers will be inserted into all HTML responses. One containing a nonce (Content-Security-Policy) and one containing the URL for an externally generated report from report-URI (Content-Security-Policy-Report-Only). 
 
For the program to be able to differentiate which HTTP responses are safe to add nonce tags to, it will operate in two phases. 

#### Collection Phase

The first phase of the program is the collection phase. In this phase, the program will identify which script tags are safe to allow to run. DOM will be used to parse the HTML inside of the collected HTTP responses. Then the parsed HTML from the HTTP responses will be used to find safe tags. Safe script tags will be defined as tags that appear on a URL path for a website at least once. The program assumes that web applications that go through the collection phase will be clean (not containing malicious scripts or modifications). Since we will be able to extract each HTML script by itself, the program will be able to store any scripts that appear in a secure location, and then keep a running count of how often that script appears, alongside which URL path that script appeared on.     
 
So the overall process in the collections stage will look as below;  

Shield has been activated:

- Collect HTTP request URL from the incoming request
- Collect HTTP response from the web application 
- Store the HTTP response  
- Parse the HTTP response using the HTML DOM 
- Record the incidences of external scripts present in the response

Analysis of the HTTP requests content:

- For each HTTP request URL and path:
- Look at the ratio of responses that contain a reference to an external script
- Apply a threshold score to determine if this is a common script
- Record that script as being 'safe' for this URL and path
 
#### Operational Phase

The second phase of our program is the operational phase. In this phase, the program will check the scripts which are appearing on web applications, against the scripts that have appeared when running the collections phase. If a safe script is found then the program will insert a nonce tag into the HTML of the HTTP response where that script appears. This nonce tag will validate that the script tag is safe to execute. Any script tags which the program deems are not safe to run, will be left in the HTML response unmodified, and the web browser will prevent their execution and report an error to report-uri.com.  
 
The main objective of this phase is to be on the lookout for external scripts. That should not be allowed to run. While the initial product will not search for non-variable and non-inline script tags, it has been identified as an ideal extension for the program.   
 
Lastly, the project will also produce a set of documentation detailing the process for setting up the MITM proxy. As well as how to run our program on different devices, how the threshold for safe tags is set and how to modify this, as well as for instructions on how to run the unit tests that will be provided to show that our software does operate as intended.

#### 1.3.3 User characteristics   

**Application Developer**<br>
This class of users includes the developers of the web application. These users are likely to be no longer present or able to change the functionality of the application, hence why this project focuses on implementing CSP using a proxy rather than directly changing the application.

**Website Owner**<br>
This class of users includes the owners of any website that enabled the proxy and program. With the proxy and program enabled, these users would experience no change in how people use their website, except for if a user inputs a script tag, and their data will be protected from attacks that involve XSS.

**Website Visitor**<br>
This class of users includes anyone who accesses a web application that has the proxy and program enabled. With our proxy and program enabled, these users would experience no changes in how they can use the web application unless they are inputting script tags (which would class them as a hacker user).

**Red Shield**<br>
This class of users includes anyone from Red Shield who has direct access to the software. These users would have full access to the code from this project and would be able to test the performance of our software or add features to the code that are not within the scope of this project, before implementing the code into their Red Core Shielding technology.

**Hacker**<br>
This class of users includes anyone trying to attack a web application with XSS that has the proxy and program enabled. With the proxy and program enabled, these users will be unable to attack the webpage through XSS, as any script tags that the user implements will not have the nonce tag for the webpage and so will not be executed.  


#### 1.3.4 Limitations

* **Browsers**:
   * The number of browsers that will receive the full benefits of security from CSP being enforced client-side is limited. This program is limited to Edge, Chrome, and Firefox because these are the only browsers that will receive the full enforcement of the CSP as strict CSP is not enabled for other web browsers.  <br>

<br>

* **Collection Phase**:
  * During the collection phase, the program is limited as it will be assumed that the websites are already clean. Therefore, any script tags inserted by original developers of the web application would have been evaluated and determined to be safe. However, if a page is not initially clean the program could be incorrectly deeming a script tag as being safe.  <br> 

## 2. References

[1]F. Inc., "CSP Nonce ⟶ Examples and Guide", Content-security-policy.com, 2021. [Online]. Available: https://content-security-policy.com/nonce/. [Accessed: 05- Apr- 2021].

[2]M. West and J. Medley, "Content Security Policy  |  Web Fundamentals  |  Google Developers", Google Developers, 2021. [Online]. Available: https://developers.google.com/web/fundamentals/security/csp/#if_you_absolutely_must_use_it_. [Accessed: 05- Apr- 2021].

[3]J. Keith and J. Sambells, DOM Scripting, 2nd ed. O'Reilly, 2010.

[4]"Products - Content Security Policy", Report URI, 2021. [Online]. Available: https://report-uri.com/products/content_security_policy. [Accessed: 05- Apr- 2021].

[5]S. Larsen, "Csper: Content Security Policy made easy", Csper, 2020. [Online]. Available: https://csper.io/blog/an-introduction-to-report-uri. [Accessed: 05- Apr- 2021].

[6]"mitmproxy - an interactive HTTPS proxy", Mitmproxy.org, 2021. [Online]. Available: https://mitmproxy.org/. [Accessed: 05- Apr- 2021].

[7]V. Pattanshetti, "How the MITM Proxy works", Medium, 2020. [Online]. Available: https://vinodpattanshetti49.medium.com/how-the-mitm-proxy-works-8a329cc53fb. [Accessed: 05- Apr- 2021].

[8]"Content Security Policy - OWASP Cheat Sheet Series", Cheatsheetseries.owasp.org, 2021. [Online]. Available: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html. [Accessed: 05- Apr- 2021].

[9]D. Hauscknecht, J. Magazinius, A. Sabelfeld, May I? Content Security Policy Endorsement for Browser Extension, Springer Link, 2015

[10]"OWASP Top Ten Web Application Security Risks | OWASP", Owasp.org, 2021. [Online]. Available: https://owasp.org/www-project-top-ten/. [Accessed: 06- Apr- 2021].

[11]"Cross Site Scripting Prevention - OWASP Cheat Sheet Series", Cheatsheetseries.owasp.org, 2021. [Online]. Available: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html. [Accessed: 06- Apr- 2021].

[12]"Content Security Policy (CSP) - HTTP | MDN", Developer.mozilla.org, 2021. [Online]. Available: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP. [Accessed: 06- Apr- 2021].

[13]T. Hunt, "Locking Down Your Website Scripts with CSP, Hashes, Nonces, and Report URI", Troy Hunt, 2017. [Online]. Available: https://www.troyhunt.com/locking-down-your-website-scripts-with-csp-hashes-nonces-and-report-uri/. [Accessed: 06- Apr- 2021].

References to other documents or standards. Follow the IEEE Citation  Reference scheme, available from the [IEEE website](https://www.ieee.org/) (please use the search box). (1 page, longer if required)

## 3. Specific requirements  
### 3.1 External interfaces

Collection Phase:

Input:

- HTTP responses sent from the host server. The HTML is parsed, and all script tags within the HTML are stored along with a count of how many responses contain a reference to each external script. This is stored as a percentage. Each time the host server is visited in the collection phase, the program counts how many responses contain a reference to each specific script. Larger quantities of references to specific scripts are more likely to be legitimate scripts that the user wants to run whereas, scripts that have low appearances are more likely to be malicious and are not meant to be executed.

Output:

- Unmodified HTTP response after changing the count of the script tags found.

Operational Phase:

Input:

- HTTP responses sent from the host server. The HTML is parsed, and all script tags within the HTML are checked against those the program has deemed safe during the collection stage.

Output:
- HTTP responses with two CSP Headers attached: Content-Security-Policy with a nonce and Content-Security-Policy-Report-Only with the report-uri URL. 
- Scripts that are found to be safe have nonce tags attached to them, allowing them to be executed.
- Any scripts that are deemed unsafe are collected and reported to the report-uri.com application by the website visitor's browser. If any unsafe script tags are found, a browser warning will be triggered.

### 3.2 Functions

#### Use Cases for the Minimum Viable Product:

| Phases    | Explanation     |
| --------- |  -------------  |
|Collection | This is the phase where the program receives multiple versions of a web application's HTTP response and parses the HTTP using DOM. Each time the program parses the HTML, it will search for script tags and store any it finds, along with a count of how many responses contain a reference to this external script. This count is stored as a percentage. If the script tag has been stored previously, the program will increase this count. The collection phase will then determine which script tags are deemed safe. |
|Operational| This is the phase where the program takes an HTTP response and gets the HTML code. The program then searches through the code to add nonce tags to the script tags which have been deemed as safe in the collection phase. |

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |    Parses the HTML of the page  |
|           |    External script tags are found  |
|Goal       |    Program notes new script  |
|           |    Calculates initial count of how many responses contain a reference to this external script tag. |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |    Parses the HTML of the page  |
|           |    Previously found script tags are found again |
|Goal       |    Script tags count increases |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Parses the HTML of the page  |
|           |   Previously found script tag does not appear |
|Goal       |   Script tags count decreases |

| 4         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Parses the HTML of the page  |
|           |   No script tags are found |
|Goal       |   The script tags count decreases for all stored tags |

| 5         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Script tag found has a high occurrence count  |
|Goal       |   Script tag is determined as safe for this URL and path  |

| 6         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Script tag found has a low occurrence count  |
|Goal       |   Script tag is determined as safe for this URL and path  |

| 7         |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   Parses the HTML of the page  |
|           |   No script tags are found |
|Goal       |   No nonces are added  |

| 8         |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   Parses the HTML of the page  |
|           |   Script tag(s) which have been previously determined as safe for this URL and path are found |
|Goal       |   Nonces added to these script tags  |

| 9         |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   Parses the HTML of the page  |
|           |   Script tag which hasn’t been registered before is found |
|Goal       |   Nonces not added to this script tag  |
|           |   Reported on report-uri.com |

| 10         |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   Parses the HTML of the page  |
|           |   Script tag(s) which have been previously determined as safe for this URL and path is found
|           |   Script tag(s) which haven't been registered before are found |
|Goal       |   Nonces added to the script tags deemed as safe   |
|           |   Nonces not added to script tags that aren’t registered |
|           |   Report non registered script tags on report-uri.com |

| 11        |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Parses the HTML of the page  |
|           |   Found inline script tag |
|Goal       |   Script tags count increases  |

| 12        |                 |
| --------- |  -------------  |
|Phase      |   Operational     |
|System     |   Parses the HTML of the page  |
|           |   Found inline script tag |
|Goal       |   Nonce is added and the script is ignored  |

| 13        |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   No HTML in the input  |
|Goal       |   Nothing happens  |

| 14        |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   No HTML in the input  |
|Goal       |   Nothing happens  |

#### Use Cases for Extensions of the Product:

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Operational           |
|System     |   Parses the HTML of the page  |
|           |   Untrusted script tag found within an untrusted script tag |
|Goal       |   Ensure no nonce tags are added and neither tags are executed  |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Operational           |
|System     |   Parses the HTML of the page  |
|           |   Found inline script tag |
|Goal       |   Determine whether the script tag is trusted or not and if it is trusted, add a nonce tag  |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   Script tag found has a low occurrence count |
|Goal       |   Script tag is not determined as safe for this URL and path  |

### 3.3 Usability Requirements

The goal is to design a proxy plugin that adheres to expectations and specifications to create additional security features for web applications. Fulfilling the usability requirements ensures that certain XSS inserted into the website is prevented from executing and safe script tags are executed to prevent websites from breaking due to the security. 

There are no usability requirements for users of the program as the program will not affect the users in any way unless they enter a script tag into the web application. The proxy parses the HTML, determines which tags to add nonces to, and sends the new HTML code to the browser with no effect, or no action needed from the user. Hence the design must be functional and efficient enough to be able to load the correct webpage at a similar time frame to the average time it takes for an average webpage to load. 

### 3.4 Performance requirements

The performance requirements section will discuss how a system will perform once it is in use. For the performance of a system to be deemed successful, the system must adhere to a set of specific requirements. Furthermore, this section will comprehensively outline what a user should expect when interacting with the system. <br>
 
* The number of simultaneous users that the system can support during the collection phase is greater than one. During the operational phase, the system is also able to support greater than one (multiple) users.<br>

* The system should load 98% of the HTML in less than 1 second. <br> 

* If the system loads 98% of the HTML in less than 1 second then with the plugin the system should take 1 second plus up to 1000 milliseconds to load. <br> 

* If delays are experienced 87% of the HTML should load in 2 seconds.<br>

*  The system should not affect the owner of the website, except for if an unsafe script tag is found. This means that if an owner deploys our proxy on their website, they should not experience any changes in how website visitors use their website unless a user inputs a script tag in the website. If a script tag is considered unsafe, the system may affect the owner as it will impact their website visitors. This is because the unsafe script tag will not execute and will cause a browser warning, hence changing what the website should do.<br>

* The program should support the client to receive the full benefits of security from CSP being enforced client-side. This will be achieved by ensuring that the only browsers used are Edge, Chrome, or Firefox.<br>

* The program should be able to notify if any script tags in a webpage are not safe. This will be achieved by collecting and reporting unsafe script tags in ‘report-uri.com’.<br> 

* The resulting data should be visible to clients (website owners) so they can see reports of unsafe script tag removals.<br>

### 3.5 Logical database requirements

#### Class Diagram ####
![alternative text](http://www.plantuml.com/plantuml/png/rLPHQzmu47xVNp7uAO76SAyXB0tfXGQQDcGNxk5w1CKUx-fYIpv9szQ4_FSRZzVok79AEGwEsvSeca_VVFfcDFYj3yg5GrElLgqgdjGE8RjpzbkNFQzMG3yqGOSEUE_XiWZwYmfO3h6YLjx3hTBccVz_aTitfh2DDhlts-qTS9n_PsTncMtt20sTXi9I5dDGTTr131Ushh48wC6XRwtnj5Acd00E_pgW3xJheQhjLx2FVz81doqb6sACMzHoYs5lIoZsM3nvq1MmxXXdVasfeXYmBf6oc9afh-dyjclnv5GwTSLEUVK5xu-ipqk2yoDztlk49aoO5isrhl6ajeKAsfhJ6FhgTC2jvUX0jP2viQMkkYdt3vDxkaY34JABjTPDglOXj7bltqYSD-e98tbqSEx5Tnq6sIyPd55TbEaoxZ4uXwkfJyPALTPzDbohCPjdEZwHh-TjU0xt95YJ010WGisDI70paa7PsPh_ojhr0acQNwrUn6lgAx09rc465nUb2kfHULolZqz2lZ5fsOPutn5uy4PceTIBICh-Mrzp3-_HuKp2PTlMcXk4JUHtnV_SxPKdNS_otMxs6kjIlDXFGoyK1-T8w9WsXY-TKzq7xGDH3z3V_m1VEDs6hThvgUmUJJcUlZ6LfVB7KA5C3wQjT938omfPc-2e8j3R-r69leoB7KQnryus_196z9Jwq59Dy6f-ETAHo6YLy-APoZJ9wLJCNfconWUUja7jJZpMrHkWrHjG8JX_-ZsIp9hX4a3VIiTmlupnY9i9FadBjEprxOTDK04RD84lASqUUo0YbbnujOuL3mjJT5CDjGaGT8EUEXILmr8qIzZAWF1qbuQINB7_aduXAw_Y59q8u-uYcwe2TlSg4C5Sl8p0IghVY8WGNwYwEDGge8n7ku1-l1nVORwUbmJEnLk1Hznfu-6p2NjDAWTxaGdcntZ6HK_4U5k2hgTA9SY4L1eWq3rOtkCYp-VlM10dlSh4mq76XOEZMxxxT4itlUk1vOnBvg6JaeiJRT2KFZqXDtYSBmrLmVqwvlLHUu-gNXgo77WOUF_zGIiwHCw4bqI0lCr_DrXPodow_l-7Qxndula_dR3ylKDb_VKRvLcUi66CJWPcDrM_3SZxMTpl-xJxQ4s1H3clIcI1_D0ctqOCIMy2UOrL87GypK3Hvn6H7awW5_c8MXuP4P_E3Tx--U6Hf8uSFpb6Kfq_6YKh_ZPyIrI7fluR)

#### State Diagram ####
![alternative text](http://www.plantuml.com/plantuml/svg/hLN1QXin4BtxAqIWq1O2FGV793I75Xh7h1Tw27iGwx6pH5vj9JcD2VttQfyiUTPoQWpD8MZUl3Sp6hriRgoJnctMQZJo9qTYPlJhzhPspGk9jz58-9_7pvMul9o8dx9nJRiAO61VxB2Ftyfozkb2I1jPOZos2sMe9bzfCe662mkodMujCMM4XhHV6x9km08Y-1Xzjjnsv9lMJxgfVKEaup0OFvAGY04oiR6u4ey0hnDKvUmu02S3gGQR-RvgjI6C78uyEPSlT2UTH3e6XolZWdkzeAklMYcgNQDRwFPXnYn8Ad3wGrXLd19tO1E58tzWm741ICG9KIX5IEs7w1VIDnUMNAbZeiebc6b01XJMnmlkEYTVZFv4b-v9AFAs7smmzvH-nnWC09mmayOcIURHGHRh722dB7wl3SrhqtJEbXfArCXXBhhJBVMWVmUmMJoml0clQGjQowRrsSpxACrlcsl0or1myodx9ulbVj3IYOduKhrVWK-UIQ-Z5ByuixUKLFL6IKT5OvyVbgLSMT2EuD6Td0hkaV6FFZVNefmloB-1oNAmA3CRujrMfSgCTW06uhbkC__3RkOylvbt3LUST9p9BPUhmCpXm3xBTKV8-PR_rUsaGuFwm9xr4zNFS1hRZfLBUZ1JxVXI-9wJ2bjEqQb7dVkwdWVHxipJKzroHWhZqwK-k70Q4haK8HTqs8C_EjgAGk9VvqIyVgXo0UkLQyRGG1GvNd7RTMhhPNMynH0HsTyUFlWtr2usQ_KN)

| 1         |                 |
| --------- |  -------------  |
|Class      |   Main          |
|Package    |   Proxy       |
|           |                |
|Description|   This is the main class, the relationship between entity Proxy_Activated represents the Main class is activated to begin the entire program.  |
|Responsibility |   To run the entire program logic, and call methods as required. |

| 2         |                 |
| --------- |  -------------  |
|Class      |   IncommingHTTP |
|Package    |   Proxy       |
|           |               |
|Description|   To send all the incoming HTTP messages to.  |
|Responsibility |   To receive HTTP responses and requests. If a response is found then the class should call saveResponse.  |

| 3         |                 |
| --------- |  -------------  |
|Class      |   saveResponse |
|Package    |   Proxy       |
|           |               |
|Description|   To take a response message and get the content of the message.  |
|Responsibility |   To receive HTTP requests. If a response is found then the class should open a file to write to and write the content of the HTTP response to the file.  |

| 4         |                 |
| --------- |  -------------  |
|Class      |   modifyRespose |
|Package    |   Proxy       |
|           |               |
|Description|   To take a response message, apply CSP headers to it and add a nonce tag to the message where an approved script tag appears.  |
|Responsibility |  To make modifications to response messages so that specified scripts are allowed to run. |

| 5         |                 |
| --------- |  -------------  |
|Class      |   Shield |
|Package    |    Application: Collection Phase       |
|           |               |
|Description|    Class to coordinate the entire Collection phase.  |
|Responsibility |  To keep track of the script tags and coordinate the running of the collection phase.  |

| 6         |                 |
| --------- |  -------------  |
|Class      |   HTMLStatement |
|Package    |    Application : Collection Phase       |
|           |                |
|Description|    Class to run actions on the statement being examined by the program.  |
|Responsibility |  Contains the currentStatement variable and getCurrentTags method. Uses these to hold information about the current script tag and is accessed by the other classes that are shown as requiring this class.  |

| 7         |                 |
| --------- |  -------------  |
|Class      |   frequency |
|Package    |    Application: Collection Phase       |
|           |                |
|Description|    Class to keep tabs on how many times a script tag has occurred. |
|Responsibility | Contains the number of times that a script tag has appeared and updates and retrieves this information. |

| 8         |                 |
| --------- |  -------------  |
|Class      |   scriptTag |
|Package    |    Application : Collection Phase       |
|           |                |
|Description|    Class to keep track of script tag content. |
|Responsibility |  Contains the contents of a script tag.  |

| 9         |                 |
| --------- |  -------------  |
|Class      |   safetyRating |
|Package    |    Application: Collection Phase       |
|           |                |
|Description|    Class to work out the safety rating of a script tag. |
|Responsibility |  Contains the safety rating which should start at 0 for a script, and then gets modified. |

| 10         |                 |
| --------- |  -------------  |
|Class      |   parseResponse |
|Package    |    Application : Collection Phase       |
|           |                |
|Description|   Class to parse the HTTPResponse using DOM parsing. |
|Responsibility |  Contains the methods for parsing responses using DOM methods.   |

| 11         |                 |
| --------- |  -------------  |
|Class      |   HTTPResponse |
|Package    |    Application : Collection Phase       |
|           |                |
|Description|    Class to get responses from the File Storage system. |
|Responsibility |  Contains the methods for parsing responses using DOM methods.   |

### 3.6 Design constraints

**Use of Python**<br>
The software for this project will be written in Python. This is an unfamiliar programming language to most team members as their previous coding experience has been focused on Java. This will be a major constraint as team members will have to learn Python during this project which will likely slow development progress.    

**Skill levels**<br>
Team members will have different experiences and specialties in software development and cybersecurity. This will be a constraint on the development process as many team members have limited knowledge about nonce tags, XSS, and HTML parsing.   

**Time-frame and deadlines**<br>
Time-frames and deadlines will be a major constraint on this project as unexpected events are bound to occur that will affect deadlines such as bugs and code deletion. Other commitments, such as other courses that team members take or team member's jobs, can be an issue if there are overlapping deadlines. There is also the chance that team members cannot access campus resources (labs, meeting rooms, etc.) due to the COVID-19 pandemic.

**Performance Expectations**<br>
Performance expectations can be a hindrance as the expectations set by team members before the development process begins may not be met after the project.
This relates to each member of the team as other commitments that team members have will hinder the development process as members will be unable to give 100% of their time and effort to the project.  

### 3.7 Nonfunctional system attributes

The nonfunctional requirements of this project are as follows (in descending order of priority): Security, Data integrity, Reliability, Performance, Scalability, Maintainability, and Usability.<br>
<br>
**Security:**<br>
<br>
The main purpose of this project is to increase internet browser security by implementing CSP nonce tags on all outgoing HTTP requests sent by the host server; security is the top priority.  As such the project will need to produce a program that can perform such implementation without compromising the security of both the website user and the website owner server.<br>
<br>
The proxy plugin must also be able to operate without exposing itself to attack. Since the program has a collection and analysis functionality used to train the system on what to apply the CSP nonce tags to. The program needs security measures to prevent the possibility of this being exploited. Since exploiting this part of the program would result in the ineffective application of the CSP.<br>
<br>
During the collection stage of the program's lifecycle, it will need to operate securely. If the collection stage can be exploited it could be possible for an attacker to intercept the HTTP responses sent by the website owner’s host server and train the system to ignore malicious code or input any code the attacker deems fit. If insecure the attacker could gain the ability to edit more than the script tags. If the program can be exploited in such a way it could lead to an increased possibility of attacks occurring, instead of preventing them.<br>
<br>
During the collection stage the system stores and reads outgoing HTTP requests, and if not stored properly, or access to any outside user this could lead to attackers being able to access this data. The program needs to ensure these files are not accessible. If accessible this could also result in further attacks or privacy breaches.<br>
<br>
Since the program operates as a proxy during the collection and operational stage of its life cycle, the program must also prevent the possibility of exploitation during the operational stage. If an exploit is discovered there could be potential for an attacker to add malicious code to every request processed by the program. Such exploits would once again lead to an increased possibility of attacks affecting any end-user of the website.<br>
<br>
**Data integrity:**<br>
<br>
The purpose of the program is to read and apply CSP nonces to HTTP responses from the website owner's host server. Since it operates as a proxy plugin the program and the project team need to ensure that the data is processed correctly (CSP nonces applied to the correct script tags). Ensuring the data sent from the host server is preserved to prevent incorrect or unreadable HTTP responses from being sent is essential. If the system can not ensure this then it could result in unreadable HTTP responses sent to the website user.<br> 
<br>
This is one of the highest priorities with this program, failure to ensure data integrity will result in the website becoming essentially inaccessible to the website user. If the program cannot maintain data integrity then it can be deemed ineffective.<br>
<br>
**Reliability:**<br>
<br>
The project needs to produce a program capable of running independently as it is implemented by the use of a proxy plugin. Since the proxy is remote to the website owner and the website user, reliability is also a top priority as neither the website user nor website owner has to access to the program. This means if problems arise due to the use of the proxy program, external intervention is required to initiate recovery or termination of the proxy.<br>
<br>
Since external intervention or termination of the proxy plugin is required, if the program malfunctions then the project becomes ineffective. Therefore, the program needs to be as robust as possible as failure can cause the website owner to lose business, traffic, etc, depending on the website's functionality. Failure could potentially result in a security risk depending on the severity of the failure if the program is the only CSP or security protocol the website owner has implemented.<br>
<br>
Reliability will be determined by the program's ability to not only apply CSP to the correct script tags sent in the HTML responses from the website owner's server but also maintain data integrity. By correctly identifying which script tags to encode the program can be as reliable.<br>
<br>
**Performance:**<br>
<br>
The program needs to be able to operate in such a way that it can handle a single request with limited interference/lag between the website server and the website user. If the program is unable to handle a single request without hindering normal use of the website, the owner of the website may see the program as more of a nuisance than a necessary security measure, especially when the program will need to handle multiple requests at once.<br>
<br>
If the program is unable to adhere to the performance requirements stated above this could result in loss of business/traffic to the website. If this were to occur it could become a case of functionality over security resulting in the program being abandoned. If the program is unable to meet these performance requirements then the project has failed.<br>
<br>
**Scalability:**<br>
<br>
This program will potentially need to be able to handle multiple requests at once, with the same amount of limited interference. Scalability is supplemental to performance since if the program is unable to handle a single HTTP request with acceptable latency, then scalability will also be affected. So by meeting the above performance requirements, scalability will be the next non-functional requirement the project team can address.<br> 
<br>
Ensuring the program can operate at the same efficiency whilst handling multiple requests is paramount to ensuring performance capabilities are maintained.  If the program is unable to handle such requests this will lead to downgraded performance. As stated above, this could lead to the proxy plugin being abandoned in favour of performance over security.<br> 
<br>
**Maintainability:**<br>
<br>
As the program is to be designed in such a manner that it operates as a proxy plugin it can be considered to be an independent system. Meaning the website user and the website owner cannot and do not interact with the program (outside the website owner attaching the plugin to their website). The program operates between the two independently of the others. As such maintainability of the program by the website user and website server of the HTTP requests are a null issue.<br>

However, the program may still require maintenance as HTTP continues to change and become increasingly complex. The program needs to be built in a way that will allow for updates and regular patching if it is deemed necessary. Therefore the program needs to be designed in such a way that it can account for the increasing complexity.<br>

Handling some of these changes may be outside the scope of this project, as the scope pertains only to the script tags of an HTTP request. Thus, this level of maintainability is not a priority of this project. However, the program still needs to be designed to be not only functional but also easy to understand, modify and patch if Redshield sees the need.<br>

**Usability:**<br>

Due to the nature of the program being run as a proxy plugin, usability by the website user is null. However, the host's will apply the proxy plugin to their website. As such the program needs to be easy to set up, initiate, and switch between modes. Usability is ranked low as if all other criteria are met then usability will be met as well. Following this logic, if the program can maintain performance, ensure security and data integrity then the program since it operates independently, would meet usability requirements.<br>

### 3.8 Physical and Environmental Requirements 

Since this project is solely software-based, there are no physical or environmental requirements involved. The only requirement this project has is that there must be access to a computer to run the program. Furthermore, the computer must have Python installed on it. The computer must be able to run Python version 3.0 or higher. <br>  

### 3.9 Supporting information
 
The project currently needs no supporting information 

## 4. Verification
### 4.1 Verifying External interfaces

| Aspect        | Input                     | Output                                                                                            | Metrics                                                                       | Criteria                                                                                                                                                                                             |
|---------------|---------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Collection:   | HTTP response.                     | HTTP response. The same HTTP response without any alterations or additions. No added nonces.                  | Matching Hashes.                                                              | Ensuring outgoing data matches the data received can be accomplished by hashing incoming and outgoing data and comparing the hashes to verify the integrity of the data after processing.            |
| MITM Proxy:   | Web Application Data/HTML | HTML Responses                                                                                    | HTML response follows a valid pattern.                                        | -                                                                                                                                                                                                    |
| DOM Parsing:  | Sanitized HTML Response.  | Document Object Model                                                                             | Unit tests passing.  Batch testing passing. No errors are thrown on sample data.  | Unit testing can be used for limited testing.  Batch testing against a larger dataset with robust exception handling and reporting for failed conversions to catch bugs before reaching production.  |
| Operational:  | HTTP response.                     | Altered HTML in the HTTP response. Input HTML with added CSP headers, nonce tags added to safe script tags, and then run as normal.  | Changed Hash                                                                  | Processing can be validated by checking if the input was classified as unsafe or not, then checking if the hash was changed during processing.                                                     |
| Report URI    | Unsafe Script             | HTTP Response. Unsafe scripts are reported to a Report URI service.                               | HTTP response indicating reception.                                           | Reception of a script sent to a Report URI service can be verified by listening for HTTP response codes from the services.                                                                           |

### 4.2 Functions

To verify that the project satisfies its required functions reliably and completely, a combination of continuous integration testing, automated testing and manual testing will be done. Each case specified in section 3.2 will be manually tested to ensure that when the specified system input has happened, the outcome will be what the specified goal states. This will allow any case to be tested to ensure there are no issues and validate that the product meets the specifications laid out in section 3.2. Any unexpected behaviour of the program will be logged as an issue to be fixed. Furthermore, automated tests will be added to test for a range of different inputs, including invalid and no input.

For the minimum viable product, only the cases outlined in section 3.2 relating to this will be tested against. Once the minimum viable product has been attained, then the cases outlined in the extension section of 3.2 will be tested to verify the programs extended behaviour.

### 4.3 Usability Requirements

| Aspect                 | Description                                                        | Criteria                                                                                              |
|------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Execution of unsafe script tags are prevented | Unsafe scripts are prevented from reaching the client              | XSS is prevented                                                                                     |
| Website functionality  | The functionality of the website is not adversely affected  | Safe fallback versions of a site can be reached if script tags are removed or prevented from running |

### 4.4 Performance requirements

| Aspect                                                               | Function        | Metrics                                                                                  | Criteria                                                                                                                                                                                             |
|----------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of Users                                                      | Collection      | Multiple users supported                                                                       | Multiple instances/requests/threads can be handled by the program in parallel                                                                                                                                     |
| Number of Users                                                      | Operational     | Multiple users supported                                                                 | Multiple instances/requests/threads can be handled by the program in parallel                                                                                                                       |
| Loading Speed                                                        | HTML Loading    | 98% of HTML loaded within 1 second plus 1000 milliseconds                                                      | Without outside limitations (bandwidth) the system can load 98% of the data within 1 second plus 1000 milliseconds                                                                                                  |
| Fall Back Loading Speed                                              | HTML Loading    | 87% of HTML loaded within 2 seconds                                                     | Without limitations, the system should be able to load 87% of the data within 2 seconds                                                                                                              |
| Complete functionality on standard browsers (Edge, Chrome, Firefox) | Post-processing | The site will complete all intended functions after processing by the program           | No deprecated or unsupported functions that will affect the output are used The only functions that will be lost are those that violate the security of a process                                  |
| Insecure script notifications                                       | Operational     | Insecure scripts are collected, processed and reported using Report URI                 | Redshield can view notifications or reports of scripts removed by the program via Report URI                                                                                                 |

### 4.5 Logical database requirements

| Class           | Package                 | Purpose                                                                                                               | Metric                                                                                         | Criteria                                                                                                          |
|-----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Main            | Proxy                   | Entry point and logical start for program                                                                             | Program runs as intended or exits with proper handling                                         | Class calls logic in the correct order and handles errors according to convention                                     |
| Incoming HTTP  | Proxy                   | Receives all incoming HTTP messages and forwards any messages with responses to save response                         | All messages with responses are passed along while those without are discarded                 | No messages without responses are forwarded and 100% of messages with responses are forwarded                     |
| Save Response   | Proxy                   | Receives an HTTP request with a response from the Incoming HTTP class and writes the content of the response to a file | HTTP Response file(s) are complete records of all incoming HTTP messages which have responses  | All HTTP responses are written to a file when received                                                           |
| Modify Response | Proxy                   | Modify a response to include nonce tags for authorized scripts                                                        | All safe scripts are given nonces                                                              | 100% of authorized scripts are given nonces and no known unsafe scripts are                                      |
| Shield          | Application: Collection | Track script tags while coordinating the collection phase                                                             | All scripts are tracked against internal metrics                                               | Each script seen during collection is stored correctly tracked against internal attributes (frequency and safety) |
| HTML Statement  | Application: Collection | Run actions and call other classes on the statement currently being evaluated as required                             | All relevant classes to a statement are called when needed                                     | Required classes are called accordingly while the script is evaluated                                             |
| Frequency       | Application: Collection | Track how often a script tag appears on a per-URL path (not site-wide)                                                | Script appearance frequency is accurately tracked for each URL                                 | Class correctly tracks script frequency and differentiates frequency between different pages of a site            |
| Script Tag      | Application: Collection | Contains content of a script tag                                                                                      | No information is lost when storing the script                                                 | Incoming scripts can be stored and then retrieved exactly as they were upon reception                     |
| Safety Rating   | Application: Collection | Determine safety rating for scripts (should fail secure)                                                              | Scripts default to no safety Script safety can be updated by the system               | Scripts default to a safety rating of 0 before they're given a higher trust factor by the system                  |
| Parse Response  | Application: Collection | Parse HTTP Responses using DOM Parsing methods                                                                        | No information is lost during parsing                                                          | HTTP Responses are accurately (reversibly) parsed by DOM Methods                                                  |
| HTTP Response   | Application: Collection | Retrieve responses from the file storage system                                                                       | No information is lost during writing or retrieval                                             | Responses can be stored and retrieved from the local storage of the host securely and without data loss   |

### 4.6 Design constraints

| Aspect                    | Limiting Factor                                               | Countermeasures                                                                                                                                                                                                                                                                                                                              | Criteria                                                                                                                                                                                      |
|---------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python                    | Unfamiliar language                                           | Following best practices Peer programming and code review An objective approach to constructive criticism and advice from team members                                                                                                                                                                                                       | Code is written with consideration of its Big O cost and security Comments and consistent variable names are used Recommendations or requests from other team members are taken on more |
| Skill                     | Individual ability                                            | Each team member will undertake a conscious effort to conduct necessary research and development to build the skills and knowledge required to meet the criteria of the project Peer programming and review                                                                                                                        | Discussion on Mattermost when help is needed Individual research                                                                                                                           |
| Time-frames and Deadlines  | Limited time, short sprint cycles                            | Weekly meetings and assessment of progress and forecasted timelines Frequent assessment of the scope of work assigned to individuals                                                                                                                                                                                                             | Attendance of weekly meetings and labs where workloads can be assessed and evaluated against deadlines                                                                                       |
| Individual contributions | Unbalanced workloads and/or inequitable distribution of work | Specified expectations for work hours; any additional work above the eight hours is at the discretion of an individual Frequent opportunity to discuss workload if a member consistently has to work on the project more than expected Contributions will be tracked through their commits to Gitlab and communication through Mattermost | Eight hours dedicated to the project each week including labs                                                                                                                        |

### 4.7 Nonfunctional system attributes

| Attribute       | Value/Reasoning                                                                                                                                                                                                                                                                                                                                                                                                  | Measurability                                                                                                                                                                                                                                                                                                                                            | Criteria                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Security        | Security is the highest priority of our program Any solution to XSS is worthless if the program is vulnerable to other attacks                                                                                                                                                                                                                                                                                 | Provably insecure scripts can be removed and the secured HTML passed to the user without risking an XSS attack Report URI reports are generated                                                                                                                                                                                                       | Reduction/Limited increase in surface area vulnerability to attack Program fails securely In case of failure the product will deny by default Secure by design - not obscurity Any solutions must be secure even if their design is made public                                                                                                        |
| Data Integrity  | As our product will operate as a proxy it is crucial that any data handled will maintain its integrity                                                                                                                                                                                                                                                                                                          | Hashing data before and after it is processed by the system to be returned                                                                                                                                                                                                                                                                              | Hashes should match for data before and after processing except when an insecure or unsafe script is removed Clients should be able to see reports of unsafe script removals                                                                                                                                                                              |
| Reliability     | In order to be viable as a product and a solution, the program must be reliable Otherwise the clients may lose business, be exposed to security risks as well or elect not to use it                                                                                                                                                                                                                           | Uptime under workload Stress testing with high frequency requests for positive and negative cases to assess script tag encoding and data integrity under load                                                                                                                                                                                         | Reliability will be determined by measuring the ability of the program to handle high frequency requests under realistic environment conditions This criteria includes the accuracy of under high load which should not be expected to drop                                                                                                               |
| Performance     | Similarly to reliability, the program must function with minimal impact on the speed use for end users This is to prevent users from disconnecting and using an insecure connection as well as prevent loss of customers if used with a business application                                                                                                                                                   | The average loading time for a full website on a desktop application is 103 seconds, while a mobile site takes 27 seconds on average Since our solution is remotely hosted it would affect both at a flat rate An increase of less than 20% of the average desktop loading time application (206 seconds) would be an ideal result Less than 50%  | A single connection/request between the host and end-user can be handled without affecting the normal usage of the website                                                                                                                                                                                                                                 |
| Scalability     | The program must handle multiple requests at once without compromising any of the other attributes                                                                                                                                                                                                                                                                                                              | Meeting the above requirements for performance are a prerequisite for scalability Scaling to service multiple requests must maintain the same performance threshold of 20% of the standard loading time in order to be viable                                                                                                                         | The program can operate at the same efficiency whilst handling multiple requests In the event of decreasing performance the proxy may be abandoned for another solution in favour of performance over security                                                                                                                                            |
| Maintainability | Since the program operates on a proxy server it will act as an independent intermediary system and should not be alterable (maintainable) by either the end-user or the host server The code should be written to best practice to allow for future maintenance, however since it will be ported to elixir the final implementation is outside of the scope of our project and up to Redshield to implement   | Following modular design and following best practices laid out in 46: Python This will increase the maintainability for future engineers at Redshield to account for future updates in HTTP, bug fixes, upgrades, and fast rollouts of security patches                                                                                              | Handling these may be outside the scope of this project, as the scope pertains only to the script tags of an HTTP request A high level of maintainability is not a priority of this project, but the program should still be designed in a modular pattern so that changes can be made to individual sections without rewriting extreme volumes of code  |
| Usability       | As a proxy, Usability by the end-user and the  host server owner is null The program still needs to be easy to use by the client Redshield                                                                                                                                                                                                                                                                    | The program can be considered to meet the project requirements if the other attributes criteria are also met If it can maintain performance and ensure security and data integrity then the program would meet usability requirements                                                                                                                 | The program must be easy to set up, initiate, and switch between modes If all other criteria are met then usability will be met as well                                                                                                                                                                                                                   |

### 4.8 Physical and Environmental Requirements <br>

This project is solely software-based and as stated in section 3.8 this means that there are no physical or environmental requirements involved. Hence, the physical or environmental requirements cannot be verified as this project does not have any. The only requirement for this project is to have access to a computer. This computer must also be able to run python version 3.0 or higher. To verify that the project fulfils this requirement access to computer laboratories will be given. The computers in the laboratories are Dell Monitors therefore python version 3.0 can be run on these monitors as they are compatible with python.  <br>

## 5. Development schedule.

### 5.1 Schedule

Identify dates for key project deliverables: 

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   Friday 7th May |
| Minimum Viable Product |   Monday 16th August |
| Further Releases       |   Friday 8th October |
| Final Project          |   Saturday 6th November |

Dates are subject to change as the project continues

### 5.2 Budget

| Item     | Amount |
| -------- |  ----- |
| Software |  nil   |
| Hardware |  nil   |
| Travel   |  nil   |

This project does not require a budget as it makes use of open-source programs such as MITM. Accessing this can be done using personal computers or the computers available at Victoria University of Wellington.<br>

The client is local and has indicated they can travel to Victoria University of Wellington for meetings.<br>

### 5.3 Risks 

If the project will involve any work outside the ECS laboratories, i.e. off-campus activities, these should be included in the following section.<br>

| Risks    | Type     |  Likelihood  |  Impact  | Mitigation |
| ---------|  ------  | ------------ | -------- | ---------- |
|Code being deleted |Technical |  Likely | Moderate-Significant (depending on amount/importance of code)| Use Gitlab to ensure code is backed up and restore it|
|Code being overwritten | Technical |  Very Likely | Moderate| Use Mattermost to notify others of commits and if code is overwritten, use Gitlab to ensure it can be restored |
|Team member unable to contribute for unforeseen reasons |Teamwork |  Possible | Moderate-Significant(depending on project stage)| Keep good documentation of what has been done and what needs to be done so others can pick up tasks without too much hassle |
|Team member has other commitments which cause them to not be available  |Teamwork |  Very Likely  |Minor| Keep good documentation of what is done and what needs to be done so others can pick up tasks without too much hassle and ensure no one is out of the loop. Ensure the team has good communication so if someone is unavailable the rest of the team knows. |
|Team member has not done their specified work| Teamwork |Possible| Significant | Regularly meet up and contact team members to ensure everyone is on track. Refer back to the team contract to ensure everyone is doing their part and what happens if someone isn't.  |
|COVID Lockdown|  |Very Likely| Significant | Ensure everyone can connect online and that all work is online |
|Misunderstanding about the project requirements| Requirements |Likely| Moderate | Ensure constant communication with the client and clear up any uncertainties promptly. |
|Changes to project requirements| Requirements | Possible | Significant | Ensure there is a clear understanding of what is required from the team from the beginning and ensure constant communication with the client. |
|Bugs within code go undetected| Technical |Very Likely| Significant | Create tests for the program to test different aspects of it and minimize the number of errors that go undetected. |
|Team members burning out| Teamwork |Likely| Significant | Ensure everyone is communicating with each other so the team knows if someone is doing too much work and ensure all work is evenly divided. |


### 5.4 Health and Safety

#### Occupational Overuse

Occupational Overuse is a type of overuse injury that may result in Muscle pains, hot or cold flushes, numbness or a restricted range of movement. To prevent this from happening team members will be encouraged to take regular breaks away from their work and personal devices. Furthermore realistic deadlines and workloads will be set to discourage overworking, alongside getting the team to practice good time management to prevent overuse to meet deadlines. 

Additionally, team members will have ergonomic workspaces so that any required equipment will be nearby and easily accessible. This will also encompass ensuring desks are at the correct height to encourage correct posture and reduce straining. Correct postures will be promoted and ensured for all team members and the team will use comfortable chairs which if possible, will have back support. This will reduce straining and incorrect postures in a work environment, mitigating occupational overuse and its potential symptoms. 

https://www.southerncross.co.nz/group/medical-library/occupational-overuse-syndrome-oos

#### Eye Strain

Eye strain occurs when a person has been staring at a computer for large periods without having any breaks away from technology. Insufficient lighting and screen flickering can also contribute to eye strain. As with the Occupational Overuse, the team will be encouraged to take regular breaks away from their work and personal devices. The team will also be encouraged to work in environments that have a sufficient level of lighting, for example not working in the dark with the screen as your only light. The team will also make sure that text displayed in any of the work produced is easily readable to avoid eye strain from having to read small text.

#### Electrical Saftey 

Since we are dealing with technology there is the risk of receiving electrical shocks from any appliances that are used in the process of working on this project. This could pose a small risk to the health of team members when they are dealing with electrical appliances such as laptops, desktop computers, monitors, electrical jugs, and the associated cables for these appliances.  As per the AS/NZS 3760 Standard, to minimise the risk of any electrical shocks the team should be encouraged to only use appliances which have been through the Test and Tag process in the last 12 months.   

#### Cable Management

Unmanaged cables are a safety risk as team members or nearby people can get caught on them and/or trip on them. To manage this risk, all team members will ensure that any cables they use will be kept underneath their desk, mitigating the possibility of someone getting caught on them. Furthermore, all cables which are not being used will be stored away in a cupboard or bag to further mitigate the risk unmanaged cables pose. 

#### COVID-19 Outbreak and/or Lockdown

To manage the safety risk of another Covid-19 outbreak or lockdown, team members will ensure all work is saved online using Gitlab so access to the University labs is not mandatory. Furthermore, everyone involved in the project will ensure they have a way to contact each other online. This will ensure all members of the team can work from home. This will mitigate this safety risk as it ensures that if there was a Covid-19 outbreak or lockdown, members do not need to expose themselves to any additional Covid-19 risks to do this project.

#### Natural Disaster 

To manage the safety risk of earthquakes, cyclones, or tsunamis team members will ensure that they each have an understanding of the basic Natural Disaster responses that should be carried out in the event of any of the above mentioned natural disasters so that our team maximises their chances of getting through the disasters without injury. This basic knowledge should include what to do in the initial stage of a natural disaster as well as where to go and what to do after a natural disaster has occurred.  

#### Health and Safety at External Workplaces

The project does not require any work or testing to be held off-campus. However, there is a possibility that some meetings will be held at Red Shield’s office. To receive a Health and Safety induction for this external workplace, team members will get in contact with the client to arrange this, before any work being done at the clients' office. 

#### Human or Animal Test Subjects

This project does not include any human or animal subjects. This is because all testing can and will be done by the team, using different web applications. 

#### 5.4.1 Safety Plans

Project requirements do not involve risk of death, serious harm, harm or injury.

## 6. Appendices
### 6.1 Assumptions and dependencies 

Below is a list of assumptions and dependencies for this project:<br>

* It is assumed that during the collection phase, the websites scanned (HTML being parsed) will be clean. <br>
* It is assumed that if the scripts are hosted on a different domain, they have not been modified after the original application developer determining they are safe to include in their application. <br>
* It is assumed that users of this program will have access to either of the following browsers: Edge, Chrome or Firefox.<br>
* It is assumed that users have access to a technological device (i.e. computer, cellular phone, tablet).<br>
* It is assumed that users have internet access to run this program.<br>
* A dependency is that the browsers used must either be Edge, Chrome or Firefox to gain the full benefits of security from CSP being inforced client-side. <br>


### 6.2 Acronyms and abbreviations

* CSP - Content Security Policy<br>
* MITM  - Man In The Middle<br>
* DOM - Document Object Model<br>
* HTML - Hyper-Text Markup Language<br>
* HTTP - Hyper-Text Transfer Protocol<br>
* XSS - Cross Site Scripting<br>

## 7. Contributions

| Contributors  | Sections     |
| ------        |  ----------  |
|    Dylan      | 1.3.2, 3.5, 6.2, 5.4, proofreading and grammer             |
|    Isabella   | 1, 1.1, 1.2, 1.3.1, 3.2, 3.3, 4.2, 5.2, 5.3, 5.4, 5.4.1, proofreading and grammar  |
|    Damien     | 1.1, 1.2,1.3.1, 3.7, 4.7, 5.2, proofreading and grammar    |
|    James      | 1.3.3, 3.6, 3.9, 4.6, 5.1             |
|    Jaya       |1.3.4, 3.4, 3.8, 4.8, 5.3, 6.1 |
|    Nathan     | 2, 3.1, 5, proofreading and grammar             |
|    Timothy    |4.1, 4.3, 4.4, 4.5, 4.6, 4.7, proofreading and grammar|
