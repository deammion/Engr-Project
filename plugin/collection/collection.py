from mitmproxy import http

def response(flow: http.HTTPFlow):
    print("response")
    file = open("html.txt", "a")
    file.write(flow.response.text + "\n")
    file.close()
    print(flow.request.pretty_url)