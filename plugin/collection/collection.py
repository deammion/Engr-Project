from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    print("request")
    file = open("html.txt", "a")
    file.write(flow.request.pretty_url + "\n")
    file.close()

def response(flow: http.HTTPFlow):
    print("response")