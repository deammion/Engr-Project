<h1>Group 14: Redshield 👋</h1>
<p align="center">
![python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)
</p>



## About
This project is home to project 14, a plugin for mitmproxy written in python designed to prevent unsafe script execution & XSS attacks on webpages.

Client: Red Shield (Point of Contact: Kirk Jackson)

Scheduled Lab Times: Tuesday 10am - 12pm & Thursday 10am - 12pm


### Features
- Learn normal traffic for a site
- Identify safe and unsafe scripts
- Attach nonce tags to safe scripts to prevent execution
- Report unsafe scripts using report-uri
- Minimal impact to the experience of end users

### Authors: 
Damien Tamasese, Dylan Simpson, Isabella Maria, James Houlihan, Jaya Narayan, Nathan Wong, Timothy McDermott

 
  
## Installation

Install with git

```bash
git clone https://gitlab.ecs.vuw.ac.nz/course-work/engr300/2021/group14/group-14.git
```

## Usage

To configure and use this project, follow the steps listed in [configuration.md](https://gitlab.ecs.vuw.ac.nz/course-work/engr300/2021/group14/group-14/-/blob/master/configuration.md).

Once the environment is configured, each phase can be started using:

```
mitmproxy -s /<path-to-script>/<phase>.py
```
There are three phases in the project architecture: Collection, analysis, and operational. The collection phase is integrated with analysis and analysis does not have to be run if the inputs gathered using collection; analysis can still be run manually to go over any files which have not been checked. 

Once scripts have been collected and analysed, the operational phase can be run to begin script tagging and filtering.

  
## Contributing
- Commits to master should only be merges or comment fixes. 
- Master should always hold a functional version of the project. Only merge working versions from development.
- Functionality changes should be built from the development branch; seperate branches should be created for each feature from this.
- Each branch must pass the pipeline assesment before being merged back into the development branch. 




  
