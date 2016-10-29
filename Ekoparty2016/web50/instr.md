### RFC 7230

Get just basic information from this server (ctf.ekoparty.org).

---

RFC 7230 is HTTP/1.1, so let's connect to the server.

    nc ctf.ekoparty.org 80

What page to request ? We are supposed to get *basic* information, so...

    GET basic
    ---
    HTTP/1.1 400 Bad Request
    Server: EKO{this_is_my_great_server}
    Date: Fri, 28 Oct 2016 10:39:35 GMT
    Content-Type: text/html
    Content-Length: 166
    Connection: close

Flag : `EKO{this_is_my_great_server}`
