# ENGR 301 Project *14* Architectural Design and Proof-of-Concept

#### Isabella Tomaz Ketley, Jaya Narayan, Timothy McDermott, Dylan Simpson, Damien Tamasese, Nathan Wong, James Houlihan

## Development Setup


To get started hacking on mitmproxy, please install a recent version of Python (we require at least Python 3.8). Then, do the following:

Linux / macOS
```
# 1) Verify that these commands work:
python3 --version
python3 -m pip --help
python3 -m venv --help
# 2) Install:
git clone https://gitlab.ecs.vuw.ac.nz/course-work/engr300/2021/group14/group-14.git
cd mitmproxy
python3 -m venv venv
venv/bin/pip install -e ".[dev]"
```

Windows
```
# 1) Verify that this command works:
python --version
# 2) Install:
git clone https://gitlab.ecs.vuw.ac.nz/course-work/engr300/2021/group14/group-14.git
cd mitmproxy
python -m venv venv
venv\Scripts\pip install -e .[dev]
```

This will clone mitmproxy's source code into a directory with the same name, and then create an isolated Python environment (a virtualenv) into which all dependencies are installed. Mitmproxy itself is installed as "editable", so any changes to the source in the repository will be reflected live in the virtualenv.

The main executables for the project – mitmdump, mitmproxy, and mitmweb – are all created within the virtualenv. After activating the virtualenv, they will be on your $PATH, and you can run them like any other command:

Linux / macOS
```
source venv/bin/activate
mitmdump --version
```

Windows
```
venv\Scripts\activate
mitmdump --version
```

Taken from https://github.com/mitmproxy/mitmproxy/blob/main/CONTRIBUTING.md

Once this has been installed follow the following steps to set it up on a browser:

Firefox
```
1. Open Firefox
2. Type in about:profiles in the address bar.
3. You will see the profiles screen
4. Click "Create a new profile" and give it a name of "mitmproxy"
```

Now you have two completely separate Firefox profiles set up - your original one, which you'll do your regular web browsing in, and a special one that's just for using with mitmproxy. <br>

Any time you want to start the second profile, go to about:profiles in the location bar, and then click "Launch profile in new browser"


Download FoxyProxy
```
1. In your new browser window, go to Add-ons and install "FoxyProxy Standard". 
2. On the FoxyProxy icon that's added to your browser toolbar, go to settings and Add Proxy. 
3. Set the proxy details to 127.0.0.1 port 8086
4. Click "Save and Edit Patterns"
5. Enter the URL for a website which you would like to direct traffic through our program
6. Then you can enable FoxyProxy just for the patterns we have set up
```
Everything should work as normal in your browser. The only sites that won't work are the sites you have added as patterns to FoxyProxy, because you haven't started up the mitm proxy. Once the proxy is started these sites will be accessable.

Setting up the Proxy
```
mitmdump --listen-host 127.0.0.1 --listen-port 8086 --mode regular
```

Now when you go to the URLs entered into FoxyProxy, it will go via the mitmdump proxy, and you will see the details on your terminal

