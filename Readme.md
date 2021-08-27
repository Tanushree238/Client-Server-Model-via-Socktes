This is a client-server application, built using sockets.

What are Sockets?
    A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.

Where is Socket used?
    The socket is generally employed in client-server applications. The server creates a socket, attaches it to a network port address then waits for the client to contact it. The client creates a socket and then attempts to connect to the server socket. When the connection is established, the transfer of data takes place. 
    A socket works above the TCP layer in TCP-IP Model, so using sockets we can create our application layer protocol like HTTP, HTTPS, FTP, etc. 

There are 4 types of Socket Types -
    Stream Sockets
    Datagram Sockets
    Raw Sockets
    Squenced Packed Sockets