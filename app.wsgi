def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Python is working'
    output += '<BR>Suck it</br> HTML <font color="RED"> WORKS! </font>' 
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
         
    return [output]
