# ENGR 301: Project Requirements Document

The aim of this document is to specify the requirements of the system your group is to build. The focus of a requirements document is the problem you are attempting to solve:  not a first attempt at a solution to that problem. This document should communicate clearly to the supervisor, client and course coordinator what the system you build is going to do, and what constraints it must meet while doing so.

The document should also demonstrate your understanding of the main analysis principles and quality guidelines, and applicable standards, using tools and notations as necessary to communicate the requirements precisely, unambiguously and clearly in a written technical document. Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure that you focus your efforts on those requirements that are most important to completing a successful system: if sections are at their page limit, indicate how many items would be expected in a complete specification. 

The ENGR 301 project proposal and requirements document should be based on the standard ISO/IEC/IEEE 29148:2011(E), primarily sections 8.4 and 9.5, plus section 9.4 for projects involving hardware and ISO 25010 SQuaRE for systemic requirements. While excerpts from the standard have been quoted within the template, to understand what is required it will be necessary to read earlier sections of the standards themselves. A supplementary treatment of requirements gathering in engineering projects may be found in [Requirements in Engineering Projects](https://victoria.rl.talis.com/items/F166DA94-DAD8-FBDB-0785-7A63C9BA3603.html?referrer=%2Flists%2F5886F297-2506-1F17-45D9-7F04CEE284EE.html%23item-F166DA94-DAD8-FBDB-0785-7A63C9BA3603) (Talis). The requirements document should contain the sections listed below, and conform to the formatting rules listed at the end of this brief. 

All team members are expected to contribute equally to the document and list their contributions in section 6 of the document. You should work on your document in your team's GitLab repository. While collective contributions are expected to be the exception rather than the rule, if more than one team member has contributed to a particular commit then all those team member IDs should be included in the first line of the git commit message. `git blame`, `git diff`, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually, commit early and commit often. Any team wishing to separate individually contributed sections into a single file before collation into the single proposal document for submission is welcome to do so.

---

<div style="page-break-after: always;"></div>

# ENGR 301 Project *14* Project Proposal and Requirements Document
#### Isabella Tomaz Ketley, Jaya Narayan, Timothy McDermott, Dylan Simpson, Damien Tamasese, Nathan Wong, James Houlihan

## 1. Introduction

Web applications are accessed and used everywhere therefore ensuring web application security is becoming increasingly difficult. There are many vulnerabilities web applications are susceptible too and ensuring all of these are secured against or can be very difficult. These days, all it takes is for an attacker to exploit a single vulnerability, to compromise a whole website or user accounts.  

XSS is one of the most common vulnerabilities that occurs whenever a web application trusts, or does not validate untrusted data. [1]. A XSS vulnerability can allow an attacker to execute scripts in an end user’s browser, access a user’s cookies, and could even result in an attacker compromising a user’s account [1]. Furthermore an XSS attack can have huge consequences which is why implementing appropriate security measures are vital.

One way to mitigate the XSS attacks is to use CSP [2]. CSP is an added layer of security which can help protect against different attacks. CSP nonce tags are used to prevent XSS [3]. A nonce is a pseudo-random value intended for one time use meaning the nonce changes with each HTTP request to ensure an attacker cannot obtain the value of it [4]. If an application contains script tags in the HTTP, the nonce value is added as a tag to any trusted script tags within the application. Once the application is run, only script tags which have the nonce tag, with the correct nonce value will be executed and run [4]. This ensures that only trusted script tags are allowed to be executed within an application. 

This project will use CSP nonce tags to determine whether or not script tags should be run on a web application, in order to mitigate XSS attacks. 

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

The Purpose of this project is to create a working prototype of a stand alone program capable of a reading, interpepting, and analyising HTTP source code with the intended purpose of preventing XSS, using nonce tags.

### 1.2 Scope

The scope of this project is to create a MITM proxy capable of reading and interperting HTTP responses to determine what script tags are safe and unsafe. This program will implement script fingerprinting using nonce for non-variable, and non-inline script tags, to prevent XSS attacks. Python unit test will be used to ensure the validity of the program we create. 

### 1.3 Product overview 
#### 1.3.1 Product perspective

The project will produce a proxy program that will be demonstrated to Red Shield which will assist with the development of their Red Core Shielding technology. The project does not need to directly access or use any of the components of the Red Core Shielding technology, nor does it need to be written in elixir, which is the native coding language used by Red Core Shielding technology. Red Shield will handle the conversion from python to elixir, once the project is completed.

The project will produce a system which will interact with any host server implementing the proxy program. This interaction will not interfere with the host server or its standard functionality and the project team will ensure this, with the exception of an unsafe XSS tag being tagged, notified and added. 

The product will function in two stages. The first stage being the collection stage and the second being the operational stage.

During the first stage the program will store any HTTP responses sent by the host server to a local machine of the client. This data is then interpreted by the program so it can learn what a standard HTML response from the host server looks like. In doing so the program will then identify what it can consider a ‘safe’ script tag. 

During the operational stage the program will continue to intercept the HTTP responses from the host server, read and interpret this response and mark all ‘safe’ script tags with a nonce tag and send it to the end user. This is the program's main purpose, automation of CSP in regards to scripting to prevent XSS attacks.

Any ‘unsafe’ script the program identifies will recorded and reported via the use of report-url.com

#### 1.3.2 Product functions

As discussed above the project will produce a program that will be responsible for blocking XSS attacks by adding CSP protection to web applications. This will be done in the form of adding nonce tags to scripts that are deemed safe to run.  
 
To be able to do this the project will implement a MITM proxy. This proxy will be responsible for tracking all outgoing HTTP requests from a device and all incoming HTTP responses from the web application. The HTTP responses will get stored in a secure location where the program will scan through the HTML located in the HTTP responses. As of our initial planning, the HTTP requests will not be required in our project.  
 
For the program to be able to differentiate which HTTP responses are safe to add nonce tags to it will operate in two phases. The first phase of the program is the collection stage. When operating in this phase the program will be busy identifying which script tags are safe to add nonce tags to, and which scripts are not safe not have nonce tags to. This phase will be where the program is using the collected HTTP responses to calculate the chance that content inside an HTML script tag is safe to run. Safe script tags will be defined as tags that appear on the clean page, in the collection phase over a certain threshold. For example, a script tag that appears 80 / 100 times the page is loaded will likely be safe to run. The exact point at which a program is deemed safe to run will be determined at a later stage through testing. The program assumes that web applications will be clean (not containing malicious scripts or modifications)   
 
DOM parsing will be the parsing method that will be used on the HTML inside of the collected HTTP responses, and from this determine which script tags are present and how often they are present. Since we will be able to extract each HTML script by itself, the program will be able to store any scripts that appear in a secure location, and then keep a running count of how often that script appears.  
 
So the overall process in the collections stage will look as below;  
Collect HTTP response from web application 
Store the HTTP response.  
Parse the HTTP response using DOM. 
Track all HTML scripts present from that request.  
Adjust weighting of safe scripts.  
Repeat.  
 
The second phase of our program is the real phase. In this, the program will check the scripts that are appearing on web applications, against the scripts that have appeared when running the collections phase. If a safe script is found then the program will insert a nonce tag into the HTML of the HTTP response where that script appears. This nonce tag will validate that the script tag is safe to execute. Any script tags which the program deems are not safe to run, will be collected and reported in ‘report-uri.com’.  
 
Both phases of this program will only check for non-variable and non-inline script tags.  
 
Lastly, the project will also produce a set of documentation detailing the process for setting up the MITM proxy as well as how to run our program on different devices.

#### 1.3.3 User characteristics   

One page identifying the main classes of users and their characteristics (9.5.5)

**Website Owner**<br>
This class of users include the owners of any website that enabled our proxy and program. With our proxy and program enabled, these users would experience no change in how people use their website, and their data will be protected from attacks that involve XSS. 

**Average Web Page Surfer**<br>
This class of users include anyone who accesses a web application that has the proxy and program enabled. With our proxy and program enabled, these users would experience no changes in how they are able to use the web application unless they are inputting script tags (which would class them as a hacker user).   

**A Red Shield Tester**<br>
This class of users include anyone from Red Shield who has direct access to the software. These users would have full access to the code from this project and would be able to test the performance of the software or add features to the code that are not within the scope of this project before implementing the code into their Red Core Shielding technology to be released to Red Shield’s clients. 

**A Hacker trying to attack a web application with XSS**<br>
This class of users include anyone trying to attack a web application with XSS that has the proxy and program enabled. With the proxy and program enabled, these users will be unable to attack the webpage using XSS as the proxy program will prevent unsafe scripting.

#### 1.3.4 Limitations

* **Browsers**:
   * The number of browsers the program can successfully run on is limited. This program is limited to Edge, Chrome and FireFox because strict CPS is not enabled for other web browsers.<br>

<br>

* **Collection Phase**:
  * During the collection phase the program is limited as it will be assumed that websites are already clean. Therefore, any scripts on that page which are often present will be deemed to be safe. However, if a page is not initially clean the program could be incorrectly considering a script tag as being safe. 

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

[13]T. Hunt, "Locking Down Your Website Scripts with CSP, Hashes, Nonces and Report URI", Troy Hunt, 2017. [Online]. Available: https://www.troyhunt.com/locking-down-your-website-scripts-with-csp-hashes-nonces-and-report-uri/. [Accessed: 06- Apr- 2021].

References to other documents or standards. Follow the IEEE Citation  Reference scheme, available from the [IEEE website](https://www.ieee.org/) (please use the search box). (1 page, longer if required)

## 3. Specific requirements  
### 3.1 External interfaces

Collection:

Input:

- HTTP responses sent from the host server. The HTML is parsed, and all script tags within the HTML are stored along with their probability of occuring. This is stored as a percentage. Each time the host server is visited in the collection phase, the percentage of each script tag increases or decreases depending on whether they are found in the HTML or not.

- All script tags found in this phase are collected and stored along with their percentage and these are deemed as safe.

Output:

- Unmodified HTTP response after changing the percentage of the script tags found.

Operational:

Input:

- HTTP responses sent from the host server. The HTML is parsed, and all script tags within the HTML are checked against those the program has deemed safe during the collection stage.

Output:
- Scripts that are found to be safe have nonce tags attached to them, allowing them to run.
- Any scripts that are deemed unsafe are collected and reported in a ‘report-uri.com’ document.

### 3.2 Functions

#### Use Cases for the Minimum Viable Product:

| Phases    | Explanation     |
| --------- |  -------------  |
|Collection |  This is the phase where the program receives multiple versions of a web application HTTP response and parses the HTTP using DOM. Each time the program parses the HTML, it will search for script tags and store any it finds, along with its probability of occurring. If the script tag has been stored previously, the program will increase the probability that the tag has appeared. |
|Real       | This is the phase where the program takes a HTTP response, gets the HTML code. The program then searches through the code to add nonce tags to the trusted script tags. To determine which script tags are trusted, the program uses the probability that the script tag occurs which is calculated in the collection phase. |

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * New script tags are found  |
|Goal       |   * Program notes new script  |
|           |   * Calculates initial probability of script tag occuring, which is stored as a percentage. |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Previously found script tags are found again |
|Goal       |   * Script tags percentages increase |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Previously found script tags does not appear |
|Goal       |   * Script tags percentages decreases |

| 4         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * No script tags are found |
|Goal       |   * Script tags percentages decreases  |

| 5         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * No script tags are found |
|Goal       |   * No nonces are added  |

| 6         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag(s) with high percentages are found |
|Goal       |   * Nonces added to these script tags  |

| 7         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag(s) with low percentages are found |
|Goal       |   * Nonces added to these script tags  |

| 8         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag which hasn’t been registered before |
|Goal       |   * Nonces not added to these script tags  |
|           |   * Reported on report-uri.com |

| 9         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Found script tag which has a high percentage 
|           |    * Found a script tag which hasn’t been registered before |
|Goal       |   * Nonces added to these script tags with high percentages   |
|           |   * Nonces not added to script tags which aren’t registered |
|           |   * Report non registered script tags on report-uri.com |

| 10        |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Nonce is added and script is ignored  |

| 11        |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Script tags percentage increases  |

| 12        |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * No HTML in the input  |
|Goal       |   * Nothing happens  |

| 13        |                 |
| --------- |  -------------  |
|Phase      |   Operational    |
|System     |   * No HTML in the input  |
|Goal       |   * Nothing happens  |

#### Use Cases for Extensions of the Product:

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Untrusted script tag found within a trusted script tag |
|Goal       |   * Add a nonce tag to the outside script tag and ensure the untrusted script tag does not run  |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Untrusted script tag found within a untrusted script tag |
|Goal       |   * Ensure no nonce tags and added and neither tags are executed  |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Determine whether the script tag is trusted or not and if it is trusted, add a nonce tag  |

### 3.3 Usability Requirements

The goal is to design a proxy program which adheres to appreciate expectations and specifications to create additional security features for web applications. Fulfilling the usability requirements ensures that certain XSS inserted to the website is prevented from executing and safe script tags are applied to prevent websites from breaking due to the security. 

There are no usability requirements for users of the program as the program will not affect the users in any way, unless they enter a script tag into the web application. The proxy parses the HTML, determines which tags to add nonces too and sends the new HTML code to the browser with no effect, or no action needed from the user. Hence the design must be functional and efficient enough to be able to load the correct webpage at a similar time frame to the avergae time it takes for a web page to load. 

### 3.4 Performance requirements

The performance requirements section will discuss how a system will perform once it is in use. In order for the performance of a system to be deemed successful, the system must adhere to a set of specific requirements. Furthermore, this section will comprehensively outline what a user should expect when interacting with the system. <br>
 
* The number of simultaneous users that the system can support during the collection phase is 1. However, during the real phase the system is able to support >1 (multiple) users.<br>

* The system should load 98% of the HTML in less than 1 second. <br> 

* If delays are experienced 87% of the HTML should load in 2 seconds.<br>

* The system should not affect the user end of the website. Therefore, this means that if users use any website with our proxy and program enabled, they should not experience any changes in how they are able to utilize the websites. However, if a script tag is considered unsafe the system will affect users as the unsafe script tag will not run hence changing what the website should do. <br>

* The program should have 100% functionality if users use Edge, Chrome or FireFox as browsers.<br>

* During the collection phase the program should be able to identify which script tags contained within the HTML are safe. This will be achieved by the program scanning through websites that are clean. <br>

* The program should insert nonce tags in script tags during the real phase to indicate which script tags are deemed safe.<br>

* The program should be able to notify if script tags in a webpage are not safe. This will be achieved by collecting and reporting unsafe script tags in ‘report-uri.com’.<br> 

* The program should be able to support data encryption when handling HTTP requests to maintain data integrity.<br> 

* The program should be able to manage a single request at once without there being significant disruption in between the host server and the users. <br>

* As the nonce is a pseudo-random value intended for one time use, the program should ensure that at every request the nonce changes.<br>


### 3.5 Logical database requirements

#### Class Diagram ####
![alternative text](http://www.plantuml.com/plantuml/png/rLPHQzmu47xVNp7uAO76SAyXB0tfXGQQDcGNxk5w1CKUx-fYIpv9szQ4_FSRZzVok79AEGwEsvSeca_VVFfcDFYj3yg5GrElLgqgdjGE8RjpzbkNFQzMG3yqGOSEUE_XiWZwYmfO3h6YLjx3hTBccVz_aTitfh2DDhlts-qTS9n_PsTncMtt20sTXi9I5dDGTTr131Ushh48wC6XRwtnj5Acd00E_pgW3xJheQhjLx2FVz81doqb6sACMzHoYs5lIoZsM3nvq1MmxXXdVasfeXYmBf6oc9afh-dyjclnv5GwTSLEUVK5xu-ipqk2yoDztlk49aoO5isrhl6ajeKAsfhJ6FhgTC2jvUX0jP2viQMkkYdt3vDxkaY34JABjTPDglOXj7bltqYSD-e98tbqSEx5Tnq6sIyPd55TbEaoxZ4uXwkfJyPALTPzDbohCPjdEZwHh-TjU0xt95YJ010WGisDI70paa7PsPh_ojhr0acQNwrUn6lgAx09rc465nUb2kfHULolZqz2lZ5fsOPutn5uy4PceTIBICh-Mrzp3-_HuKp2PTlMcXk4JUHtnV_SxPKdNS_otMxs6kjIlDXFGoyK1-T8w9WsXY-TKzq7xGDH3z3V_m1VEDs6hThvgUmUJJcUlZ6LfVB7KA5C3wQjT938omfPc-2e8j3R-r69leoB7KQnryus_196z9Jwq59Dy6f-ETAHo6YLy-APoZJ9wLJCNfconWUUja7jJZpMrHkWrHjG8JX_-ZsIp9hX4a3VIiTmlupnY9i9FadBjEprxOTDK04RD84lASqUUo0YbbnujOuL3mjJT5CDjGaGT8EUEXILmr8qIzZAWF1qbuQINB7_aduXAw_Y59q8u-uYcwe2TlSg4C5Sl8p0IghVY8WGNwYwEDGge8n7ku1-l1nVORwUbmJEnLk1Hznfu-6p2NjDAWTxaGdcntZ6HK_4U5k2hgTA9SY4L1eWq3rOtkCYp-VlM10dlSh4mq76XOEZMxxxT4itlUk1vOnBvg6JaeiJRT2KFZqXDtYSBmrLmVqwvlLHUu-gNXgo77WOUF_zGIiwHCw4bqI0lCr_DrXPodow_l-7Qxndula_dR3ylKDb_VKRvLcUi66CJWPcDrM_3SZxMTpl-xJxQ4s1H3clIcI1_D0ctqOCIMy2UOrL87GypK3Hvn6H7awW5_c8MXuP4P_E3Tx--U6Hf8uSFpb6Kfq_6YKh_ZPyIrI7fluR)
#### State Diagram ####
![alternative text](http://www.plantuml.com/plantuml/svg/hLN1QXin4BtxAqIWq1O2FGV793I75Xh7h1Tw27iGwx6pH5vj9JcD2VttQfyiUTPoQWpD8MZUl3Sp6hriRgoJnctMQZJo9qTYPlJhzhPspGk9jz58-9_7pvMul9o8dx9nJRiAO61VxB2Ftyfozkb2I1jPOZos2sMe9bzfCe662mkodMujCMM4XhHV6x9km08Y-1Xzjjnsv9lMJxgfVKEaup0OFvAGY04oiR6u4ey0hnDKvUmu02S3gGQR-RvgjI6C78uyEPSlT2UTH3e6XolZWdkzeAklMYcgNQDRwFPXnYn8Ad3wGrXLd19tO1E58tzWm741ICG9KIX5IEs7w1VIDnUMNAbZeiebc6b01XJMnmlkEYTVZFv4b-v9AFAs7smmzvH-nnWC09mmayOcIURHGHRh722dB7wl3SrhqtJEbXfArCXXBhhJBVMWVmUmMJoml0clQGjQowRrsSpxACrlcsl0or1myodx9ulbVj3IYOduKhrVWK-UIQ-Z5ByuixUKLFL6IKT5OvyVbgLSMT2EuD6Td0hkaV6FFZVNefmloB-1oNAmA3CRujrMfSgCTW06uhbkC__3RkOylvbt3LUST9p9BPUhmCpXm3xBTKV8-PR_rUsaGuFwm9xr4zNFS1hRZfLBUZ1JxVXI-9wJ2bjEqQb7dVkwdWVHxipJKzroHWhZqwK-k70Q4haK8HTqs8C_EjgAGk9VvqIyVgXo0UkLQyRGG1GvNd7RTMhhPNMynH0HsTyUFlWtr2usQ_KN)

| 1         |                 |
| --------- |  -------------  |
|Class      |   Main          |
|Package    |   * Proxy       |
|           |   *             |
|Description|   * This is the main class, the relationship between entity Proxy_Activated represents the main being activated to beging the entire program  |
|Respsosibility |   * To run the entire program logic, call methods as required |

| 2         |                 |
| --------- |  -------------  |
|Class      |   IncommingHTTP |
|Package    |   * Proxy       |
|           |   *             |
|Description|   * To send all the incomming HTTP messages to.  |
|Respsosibility |   * To recieve HTTP Responses and Requests, if a response is found then the class should call saveResponse  |

| 3         |                 |
| --------- |  -------------  |
|Class      |   saveResponse |
|Package    |   * Proxy       |
|           |   *             |
|Description|   * To take a response message and get the content of the message.  |
|Respsosibility |   * To recieve HTTP Requests, if a response is found then the class should open the a file to write to and write the content of the HTTP response to the file  |

| 4         |                 |
| --------- |  -------------  |
|Class      |   modifyRespose |
|Package    |   * Proxy       |
|           |   *             |
|Description|   * To take a response message and get the apply a nonce tag to the message where a approved script tag appears.  |
|Respsosibility |   * To make modification to response messages so that specified scripts are allowed to run |

| 5         |                 |
| --------- |  -------------  |
|Class      |   Shield |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * Class to co-ordinate the entire Collection phase  |
|Respsosibility | * To keep track of the script tags and co-ordinate the running of the collections phase  |

| 6         |                 |
| --------- |  -------------  |
|Class      |   HTMLStatement |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to run actions on the statement being examined by the program  |
|Respsosibility | * Contain the currentStatement as a string and use the getCurrentTags to go through a script tag with the other classes that this class requires.  |

| 7         |                 |
| --------- |  -------------  |
|Class      |   frequency |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to keep tabs on how many times a script tag has appear |
|Respsosibility | * contain the times that a script tag has appeared and updates and retrieves them.  |

| 8         |                 |
| --------- |  -------------  |
|Class      |   scriptTag |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to keep track of script tag content |
|Respsosibility | * contain the content of a script tag.  |

| 9         |                 |
| --------- |  -------------  |
|Class      |   safteyRating |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to work out the saftey rating of a script tag |
|Respsosibility | * contain the saftey rating which should start at 0 for a script, and then gets modified   |

| 10         |                 |
| --------- |  -------------  |
|Class      |   parseResponse |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to parse the HTTPResponse using DOM parsing |
|Respsosibility | * Contains the methods for parsing responses using dom methods   |

| 11         |                 |
| --------- |  -------------  |
|Class      |   HTTPResponse |
|Package    |   * Application : Collection Phase       |
|           |   *             |
|Description|   * class to get responses from the File Storage system. |
|Respsosibility | * Contains the methods for parsing responses using dom methods   |

### 3.6 Design constraints

**Use of Python**<br>
The software for this project will be written in python code which is an unfamiliar programming language to most team members as most of their previous coding experience has been focused on Java. This will be a major constraint as team members will have to learn python during this project which will likely slow development progress.    

**Skill levels**<br>
Team members will have different experiences and specialties in software development and cybersecurity. This will be a constraint on the development process as many team members have limited knowledge about nonce tags, XSS and HTML parsing.   

**Timeframe and deadlines**<br>
Timeframes and deadlines will be a major constraint on this project as unexpected events are bound to occur that will affect deadlines such as bugs and code deletion. Other commitments, such as other courses that team members take or team members jobs, can be an issue if there are overlapping deadlines. There is also the chance that team members cannot access campus resources (labs, meeting rooms etc.) due to the COVID-19 pandemic.

**Performance Expectations**<br>
Performance expectations can be a hindrance as the expectations set by team members before the development process begins may not be met at the conclusion of the project.
This relates to each member of the team as other commitments that team members have will hinder the development process as members will be unable to give 100% of their time/effort to the project.  

### 3.7 Nonfunctional system attributes

The nonfunctional requirements of this project are as follows (in descending order of priority): Security, Data integrity, Reliability, Performance, Scalability, Maintainability, and Usability.<br>
<br>
**Security:**<br>
<br>
The main purpose of this project is to increase internet browser security by implementing CSP nonce tags on all outgoing HTTP requests sent by the host server; security is the top priority.  As such the project will need to produce a program that can perform such implementation without compromising security of both the end user and the host server.<br>
<br>
The program/proxy must also be able to operate without exposing itself to attack. Since the program has a read functionality used to train the system on what to apply the CSP nonce tags to. The program needs security measures to prevent the possibility of this being exploited. Since exploiting this part of the program would result in ineffective application of the CSP.<br>
<br>
During the reading stage of the programs lifecycle it will need to operate in a way that is secure. If the reading stage can be exploited it could be possible for an attacker to intercept the incoming HTTP requests and train the system to ignore malicious code or input any code the attacker deems fit. If unsecure the attacker could gain the ability to edit more than the script tags. If the program can be exploited in such a way it could lead to an increased possibility of attacks occurring, instead of preventing them.<br>
<br>
During the reading stage the system stores and reads outgoing HTTP requests, and if not stored properly, or accessible to any outside user this could lead to attackers being able to access this data. The program needs to ensure these files are not accessible. If accessible this could also result in further attacks or privacy breaches.<br>
<br>
Since the program operates as a proxy during each stage of its life cycle the program must also prevent the possibility of exploitation during the encoding stage. If an exploit is discovered there could be potential for an attacker to add malicious code to every request processed by the program. Such exploits would once again lead to an increased possibility of attacks affecting any end user of the website.<br>
<br>
**Data integrity:**<br>
<br>
The purpose of the program is to read and encrypt HTTP responses from the host websites server. Since it operates on a proxy the program and the project team need to ensure that the data is encrypted correctly. Ensuring the data sent from the host server is preserved to prevent incorrect or unreadable HTTP responses being sent is essential. If the system can not ensure this then it could result in unreadable HTTP responses sent to the end user.<br> 
<br>
This is one of the highest priorities with this program, failure to ensure data integrity will result in the host website becoming essentially inaccessible to the end user. If the program cannot maintain data integrity then it is deemed a failure.<br>
<br>
**Reliability:**<br>
<br>
The project needs to produce a program capable of running independently as it is implemented by use of a proxy server. Since the proxy is remote to the host and end user, reliability is also a top priority as neither the end user or host server have access to the program. This means if problems arise due to the use of said program, external intervention is required to initiate recovery.<br>
<br>
Since external intervention or termination of the proxy is required, if the program malfunctions then the project becomes null and void. Therefore, the program needs to be as robust as possible as failure can cause the host server to lose business, traffic etc, depending on the host site. Failure could potentially result in a security risk depending on the severity of the failure, if the program is the only CSP or security protocol the host server is operating.<br>
<br>
Reliability will be determined by the program's ability to not only encode the correct script tags sent in the HTML response from the host server, but also maintain data integrity. By correctly identifying which script tags to encode the program can be as reliable.<br>
<br>
**Performance:**<br>
<br>
The program needs to be able to operate in such a way that it can handle a single request at once with limited interference/lag between the host server and the end user. If the program is unable to handle a single request without hindering normal use of the host website, the owner of the host server may see the program as more of a nuisance than a necessary security measure, especially when the program will need to handle multiple requests at once.<br>
<br>
If the program is unable to adhere to the performance requirements stated above this could result in loss of business/traffic to the host server. If this were to occur it could become a case of functionality over security resulting in the program being abandoned. If the program is unable to meet these performance requirements then the project has failed.<br>
<br>
**Scalability:**<br>
<br>
This program will potentially need to be able to handle multiple requests at once, with the same amount of limited interference. Scalability is supplemental to performance since if the program is unable to handle a single HTTP request with acceptable latency, then scalability will also be affected. So by meeting the above performance requirements, scalability will be the next non-functional requirement the project team can address.<br> 
<br>
Ensuring the program can operate at the same efficiency whilst handling multiple requests is paramount to ensuring performance capabilities are maintained.  If the program is unable to handle such requests this will lead to downgraded performance. As stated above, this could lead to the proxy being abandoned in favour of performance over security.<br> 
<br>
**Maintainability:**<br>
<br>
As the program is to be designed in such a manner that it operates on a proxy server it can be considered to be an independent system. Meaning the end user and the owner of the host server cannot and do not interact with the program. The program operates between the two independently of the others. As such maintainability of the program by the end user and host server of the HTML requests are a null issue.<br>

However, the program may still require maintenance as HTTP continues to change and become increasingly complex. The program needs to be built in a way that will allow for updates and regular patching if it is deemed necessary or the program needs to be designed in such a way that it can account for the increasing complexity.<br>

Handling some of these changes may be outside the scope of this project, as the scope pertains only to the script tags of an HTTP request. Thus, this level of maintainability is not a priority of this project. However, the program needs to be designed to be not only functional but also easy to understand, modify and patch if Redshield sees the need.<br>

**Usability:**<br>

Due to the nature of the program being run in as a proxy, usability by the end user and the  host server owner is null. However, the program still needs to be easy to use by the client Redshield. As such the program needs to be easy to set up, initiate, and switch between modes. Usability is ranked low as if all other criteria are met then usability will be met as well. Following this logic, if the program can maintain performance, ensure security and data integrity then the program, since it operates independently, would meet usability requirements.<br>

### 3.8 Physical and Environmental Requirements 

Due to the fact that this project is solely a software-based project there are no physical or environmental requirements involved. The only requirement this project has is that there must be access to a computer to run the program. Furthermore, the computer must have python installed on it. It is vital that the computer is able to run python version 3.0 or higher. <br>  

### 3.9 Supporting information

see 9.5.19. 

The project currently needs no supporting infomation 

## 4. Verification
### 4.1 Verifying External interfaces

| Aspect        | Input                     | Output                                                                                            | Metrics                                                                       | Criteria                                                                                                                                                                                             |
|---------------|---------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Collection:   | HTML.                     | HTML. The exact same HTML without any alterations or additions. No added nonces.                  | Matching Hashes.                                                              | Ensuring outgoing data matches the data received can be accomplished by hashing incoming and outgoing data and comparing the hashes to verify the integrity of the data after processing.            |
| MITM Proxy:   | Web Application Data/HTML | HTML Responses                                                                                    | HTML response follows a valid pattern.                                        | -                                                                                                                                                                                                    |
| DOM Parsing:  | Sanitised HTML Response.  | Document Object Model                                                                             | Unit tests passing.  Batch testing passing. No errors thrown on sample data.  | Unit testing can be used for limited testing.  Batch testing against a larger dataset with robust exception handling and reporting for failed conversions to catch bugs before reaching production.  |
| Operational:  | HTML.                     | Altered HTML. Input HTML with added safe script tags and add nonce tags, and then run as normal.  | Changed Hash                                                                  | Processing can be validated by checking if an input was classified as unsafe or not, then checking if the hash was changed during processing.                                                     |
| Report URI    | Unsafe Script             | HTTP Response. Unsafe scripts are reported to a Report URI service.                               | HTTP response indicating reception.                                           | Reception of a script sent to a Report URI service can be verified by listening for HTTP response codes from the services.                                                                           |

### 4.2 Functions

To verify that the project satisfies it’s required functions in a reliable and complete way, a combination of continuous integration testing, automated testing and manual testing will be done. Each case specified in section 3.2 will be manually tested to ensure that when the specified system input has happened, the outcome will be what the specified goal states. This will allow any case to be tested, to ensure there are no issues and validate that the product meets the specifications laid out in section 3.2. Any unexpected behaviour of the program will be logged as an issue to be fixed. Furthermore, automated tests will be added to test for a range of different inputs, including invalid and no input.

For the minimum viable product, only the cases outlined in section 3.2 relating to this will be tested against. Once the minimum viable product has been attained, then the cases outlined in the extension section of 3.2 will be tested against to verify the programs extended behaviour.

### 4.3 Usability Requirements

| Aspect                 | Description                                                        | Criteria                                                                                              |
|------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Removal unsafe scripts | Unsafe scripts are prevented from reaching the client              | XSS is prevented.                                                                                     |
| Website functionality  | The functionality of the website is not adversely affected by the  | Safe fallback versions of a site can be reached if script tags are removed or prevented from running. |

### 4.4 Performance requirements

| Aspect                                                               | Function        | Metrics                                                                                  | Criteria                                                                                                                                                                                             |
|----------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of Users                                                      | Collection      | One user supported                                                                       | A single instance of the program can run during the collection phase.                                                                                                                                |
| Number of Users                                                      | Operational     | Multiple users supported                                                                 | Multiple instances/requests/threads can be handled by the program in parallel.                                                                                                                       |
| Request management                                                   | Operational     | Single request processing speed.                                                         | The program can handle a single request at a pace fast enough to not result in significant disruption between the client and the server.                                                             |
| Loading Speed                                                        | HTML Loading    | 98% of HTML loaded within 1 second.                                                      | Without outside limitations (bandwidth) the system is able to load 98% of the data within 1 second.                                                                                                  |
| Fall Back Loading Speed                                              | HTML Loading    | 87% of HTML loaded within 2 seconds.                                                     | Without limitations the system should be able to load 87% of the data within 2 seconds.                                                                                                              |
| Unsafe script functionality                                          | Post processing | Performance of the outside website is not adversely affected by the removal of a script. | The program will learn which scripts are used by the website under normal operation, any removed scripts should not be of critical importance to the website.                                        |
| Complete functionality on standard browsers. (Edge, Chrome, Firefox) | Post processing | The site will complete all intended functions after processing by the program.           | No deprecated or unsupported functions that will affect the output are used. The only functions that will be lost are those that violate the security of a process.                                  |
| Identification of safe scripts                                       | Collection      | Hostile scripts are not categorised as safe by the program.                              | Sample sites are verified to be clean/secure before being used in collection.                                                                                                                        |
| Nonce tags addition                                                  | Operational     | Nonce tags are added to all scripts deemed safe.                                         | No insecure scripts have nonce tags added. All secure scripts are given nonces.                                                                                                                      |
| Insecure script notifications.                                       | Operational     | Insecure scripts are collected, processed and reported using Report URI.                 | Redshield is able to view notifications or reports of scripts removed by the program via Report URI.                                                                                                 |
| Encryption                                                           | Operational     | HTTP request encryption is supported.                                                    | Decrypted data should never be exposed to outside services except when being processed using Report URI. Secure encryption methods should be used and keys should only be stored or used internally. |
| Nonce reuse                                                          | Operational     | The nonce should change for every script and be used only as a one time value.           | Nonce tags will be rendered invalid after they are used for the first time.                                                                                                                          |
| Nonce generation                                                     | Operational     | The generation process of the nonce should not be reversible or replicable.              | Secure methods for generation will be used on the server side, nonce generation will never be assigned to the client.                                                                                |

### 4.5 Logical database requirements

## 4.6 Design constraints
| Aspect                    | Limiting Factor                                               | Countermeasures                                                                                                                                                                                                                                                                                                                              | Criteria                                                                                                                                                                                      |
|---------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python                    | Unfamiliar language                                           | Following best practices.  Peer programming and code review.  Objective approach to constructive criticism and advice from team members.                                                                                                                                                                                                       | Code is written with consideration of its Big O cost and security.  Comments and consistent variable names are used.  Recommendations or requests from other team members are taken on mored. |
| Skill                     | Individual ability                                            | Each team member will undertake a conscious effort to conduct necessary research and development in order to build the skills and knowledge required to meet the criteria of the project.  Peer programming and review.                                                                                                                        | Discussion on mattermost when help is needed.  Individual research.                                                                                                                           |
| Timeframes and Deadlines  | Limited time, short sprint cycles.                            | Weekly meetings and assessment of progress and forecasted timelines. Frequent assessment of scope of work assigned to individuals.                                                                                                                                                                                                             | Attendance of weekly meetings and labs where workloads can be assessed and evaluated against deadlines.                                                                                       |
| Individual contributions. | Unbalanced workloads and/or inequitable distribution of work. | Specified expectations for work hours; any additional work above the eight hours is at the discretion of an individual.  Frequent opportunity to discuss workload if a member consistently has to work on the project more than expected.  Contributions will be tracked through their commits to Gitlab and communication through mattermost. | Eight hours of time dedicated to the project each week including labs.                                                                                                                        |

## 4.7 Nonfunctional system attributes

| Attribute       | Value/Reasoning                                                                                                                                                                                                                                                                                                                                                                                                  | Measurability                                                                                                                                                                                                                                                                                                                                            | Criteria                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Security        | Security is the highest priority of our program. Any solution to XSS is worthless if the program is vulnerable to other attacks.                                                                                                                                                                                                                                                                                 | Provably insecure scripts can be removed and the secured html passed to the user without risking an XSS attack.  Report URI reports are generated.                                                                                                                                                                                                       | Reduction/Limited increase in surface area vulnerability to attack. Program fails securely. In case of failure the product will deny by default. Secure by design - not obscurity. Any solutions must be secure even if their design is made public.                                                                                                        |
| Data Integrity  | As our product will operate as a proxy it is crucial that any data handled will maintain its integrity.                                                                                                                                                                                                                                                                                                          | Hashing data before and after it is processed by the system to be returned.                                                                                                                                                                                                                                                                              | Hashes should match for data before and after processing except when an insecure or unsafe script is removed. Clients should be able to see reports of unsafe script removals.                                                                                                                                                                              |
| Reliability     | In order to be viable as a product and a solution, the program must be reliable. Otherwise the clients may lose business, be exposed to security risks as well or elect not to use it.                                                                                                                                                                                                                           | Uptime under workload.  Stress testing with high frequency requests for positive and negative cases to assess script tag encoding and data integrity under load.                                                                                                                                                                                         | Reliability will be determined by measuring the ability of the program to handle high frequency requests under realistic environment conditions. This criteria includes the accuracy of under high load which should not be expected to drop.                                                                                                               |
| Performance     | Similarly to reliability, the program must function with minimal impact on the speed use for end users. This is to prevent users from disconnecting and using an insecure connection as well as prevent loss of customers if used with a business application.                                                                                                                                                   | The average loading time for a full website on a desktop application is 10.3 seconds, while a mobile site takes 27 seconds on average.  Since our solution is remotely hosted it would affect both at a flat rate.  An increase of less than 20% of the average desktop loading time application (2.06 seconds) would be an ideal result. Less than 50%  | A single connection/request between the host and end user can be handled without affecting the normal usage of the website.                                                                                                                                                                                                                                 |
| Scalability     | The program must handle multiple requests at once without compromising any of the other attributes.                                                                                                                                                                                                                                                                                                              | Meeting the above requirements for performance are a prerequisite for scalability.  Scaling to service multiple requests must maintain the same performance threshold of 20% of the standard loading time in order to be viable.                                                                                                                         | The program can operate at the same efficiency whilst handling multiple requests. In the event of decreasing performance the proxy may be abandoned for another solution in favour of performance over security.                                                                                                                                            |
| Maintainability | Since the program operates on a proxy server it will act as an independent intermediary system and should not be alterable (maintainable) by either the end user or the host server.  The code should be written to best practice to allow for future maintenance, however since it will be ported to elixir the final implementation is outside of the scope of our project and up to redshield to implement.   | Following modular design and following best practices laid out in 4.6: Python.  This will increase the maintainability for future engineers at redshield to account for future updates in HTTP, bug fixes, upgrades, and fast rollouts of security patches.                                                                                              | Handling these may be outside the scope of this project, as the scope pertains only to the script tags of an HTTP request.  A high level of maintainability is not a priority of this project, but the program should still be designed in a modular pattern so that changes can be made to individual sections without rewriting extreme volumes of code.  |
| Usability       | As a proxy, Usability by the end user and the  host server owner is null.  The program still needs to be easy to use by the client Redshield.                                                                                                                                                                                                                                                                    | The program can be considered to meet the project requirements if the other attributes criteria are also met.  If it can maintain performance and ensure security and data integrity then the program would meet usability requirements.                                                                                                                 | The program must be easy to set up, initiate, and switch between modes. If all other criteria are met then usability will be met as well.                                                                                                                                                                                                                   |

### 4.8 Physical and Environmental Requirements <br>

This project is solely a software-based project and as stated in section 3.8 this means that there are no physical or environmental requirements involved. Hence, the physical or environmental requirements cannot be verified as this project does not have any. The only requirement for this project is to have a computer. This computer must also be able run python version 3.0 or higher. In order to verify that the project fulfils this requirement access to computer laboratories will be given. The computers in the laboratories are Dell Monitors therefore python version 3.0 can be run on these monitors as they are compatible with python.  <br>

## 5. Development schedule.

### 5.1 Schedule

Identify dates for key project deliverables: 

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   Friday 7th May (Project Architecture and Design Document due)     |
| Minimum Viable Product |   Monday 16th August  (Trimester 2 mid-tri break begins)    |
| Further Releases       |   Friday 8th October  (Trimester 2 and full-year teaching period ends)    |
| Final Project          |   Saturday 6th November (End-year assessment period ends)      |

Dates are subject to change as project continues

### 5.2 Budget

| Item     | Amount |
| -------- |  ----- |
| Software |  nil   |
| Hardware |  nil   |
| Travel   |  nil   |

This project does not require a budget as it makes use of open source programs such as MITM. Accessing this can be done using personal computers or the computers available at Victoria University of Wellington.<br>

The Client is local, and has indicated they can travel to Victoria University of Wellington for meetings.<br>

### 5.3 Risks 

Identify the ten most important project risks to achieving project goals: their type, likelihood, impact, and mitigation strategies (3 pages).

If the project will involve any work outside the ECS laboratories, i.e. off-campus activities, these should be included in the following section.<br>

| Risks    | Type     |  Likelihood  |  Impact  | Mitigation |
| ---------|  ------  | ------------ | -------- | ---------- |
|Code being deleted |Technical |  Likely | Moderate-Significant (depending on amount/importance)| Use Gitlab |
|Code being overwritten | Technical |  Very Likely | Moderate| Mattermost to notify others of commitments and if code is overwritten, use gitlab to restore it |
|Team member unable to contribute for unforeseen reasons |Teamwork |  Possible | Moderate-Significant(depending on project stage)| Keep good documentation of what is done so others can pick up tasks without too much hassle |
|Team member has other commitments which cause them to not be available  |Teamwork |  Very Likely  |Minor| Keep good documentation of what is done so others can pick up tasks without too much hassle and ensure no one is out of the loop |
|Team member has not done their specified work| Teamwork |Possible| Significant | Regularly meet up and contact team members to ensure everyone is on track  |
|COVID Lockdown|  |Very Likely| Significant | Ensure everyone is able to connect online and all work is online |
|Misunderstanding about the project requirements| Requirements |Likely| Moderate | Ensure constant communication with the client and clear up any uncertainties promptly |
|Changes to project requirements| Requirements | Possible | Significant | Ensure there is a clear understanding of what is required from the team from the beginning and ensure constant communication with client |
|Bugs within code go undetected| Technical |Very Likely| Significant | Create tests for the program, to test different aspects of it and minimize the number of errors that go undetected |
|Team members burning out| Teamwork |Likely| Significant | Ensure everyone is communicating with each other so the team knows if someone is doing too much work and ensure all work is evenly divided |


### 5.4 Health and Safety
#### Occupational Overuse

To manage occupational overuse, team members will ensure that they take regular breaks away from their devices. Furthermore, realistic deadlines will be set for tasks and the team will practice good time management to prevent overuse in order to meet deadlines. 

Additionally, team members will have ergonomic workspaces so that any required equipment will be nearby and easily accessible. This will also encompass ensuring desks are at the correct height to encourage correct posture and reduce straining. Correct postures will be promoted and ensured for all team members and the team will use comfortable chairs which if possible, will have back support. This will reduce straining and incorrect postures in a work environment, mitigating occupational overuse and its potential symptoms. 

https://www.southerncross.co.nz/group/medical-library/occupational-overuse-syndrome-oos

#### Cable Management

Unmanaged cables are a safety risk as team members or nearby people can get caught on them and/or trip on them. In order to manage this risk, all team members will ensure that any cables they use will be kept underneath their desk, mitigating the possibility of someone getting caught on it. Furthermore, all cables which are not being used will be stored away in a cupboard or bag to further mitigate the risk unmanaged cables pose. 

#### Health and Safety at External Workplaces

The project does not require any work or testing to be held off-campus. However, there is a possibility that some meetings will be held at Red Shield’s office. In order to receive a Health and Safety induction for this external workplace, team members will get in contact with the client to arrange this, prior to any work being done at the clients' office. 

#### Human or Animal Test Subjects

This project does not include any human or animal subjects. This is because all testing can and will be done by the team, using different web applications. 

#### 5.4.1 Safety Plans

Project requirements do not involve risk of death, serious harm, harm or injury.

## 6. Appendices
### 6.1 Assumptions and dependencies 

One page on assumptions and dependencies (9.5.7).<br>


Below is a list of assumptions and dependencies for this project:<br>

* It is assumed that during the collection phase, the websites used will be clean. <br>
* It is assumed that users of this program will have access to either of the following browsers, Edge, Chrome or FireFox.<br>
* It is assumed that users have access to a technological device (i.e., computer, cellular phone, tablet).<br>
* It is assumed that users have access to internet to run this program.<br>
* A dependency is that the browsers used must either be Edge, Chrome or FireFox. <br>


### 6.2 Acronyms and abbreviations

CSP - Content Security Policy
MITM  - Man In The Middle
DOM - Document Object Model
HTML - Hyper-Text Markup Language
HTTP - Hyper-Text Transfer Protocol
XSS - Cross Site Scripting

## 7. Contributions

| Contributors  | Sections     |
| ------        |  ----------  |
|    Dylan      | 1.3.2, 3.5, 6.2             |
|    Isabella   | 1, 1.1, 1.2, 1.3.1, 5.4.1, 5.2, 3.2, 3.3, 5.3, 5.4, 5.4.1, proofreading and grammar  |
|    Damien     | 1.1, 1.2,1.3.1, 3.7, 4.7, 5.2, proofreading and grammar    |
|    James      | 1.3.3, 3.6, 3.9, 4.6, 5.1             |
|    Jaya       |1.3.4, 3.4, 3.8, 4.8, 5.3, 6.1 |
|    Nathan     |              |
|    Timothy    |4.1, 4.3, 4.4, 4.6, 4.7|

---

## Formatting Rules 

 * Write your document using [Markdown](https://gitlab.ecs.vuw.ac.nz/help/user/markdown#gitlab-flavored-markdown-gfm) and ensure you commit your work to your team's GitLab repository.
 * Major sections should be separated by a horizontal rule.


## Assessment  

The goal of a requirements document is the problem you are attempting to solve:  not a first attempt at a solution to that problem. The most important factor in the assessmernt of the document is how will it meet that goal. The document will be assessed for both presentation and content. 

The presentation will be based on how easy it is to read, correct spelling, grammar, punctuation, clear diagrams, and so on.

The content will be assessed according to its clarity, consistency, relevance, critical engagement and a demonstrated understanding of the material in the course. We look for evidence these traits are represented and assess the level of performance against these traits. While being comprehensive and easy to understand, this document must be reasonably concise too. You will be affected negatively by writing a report with too many pages (far more than what has been suggested for each section above).

We aim to evaluate ENGR301 documents and projects as if they were real projects rather than academic exercises &mdash; especially as they are real projects with real clients. The best way to get a good mark in a document is to do the right thing for your project, your client, and your team. We encourage you to raise questions with your tutor or course staff, as soon as possible, so you can incorporate their feedback into your work.

---
