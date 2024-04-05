from socketserver import BaseRequestHandler, ThreadingTCPServer

HOST = "0.0.0.0"
PORT = 6002

BLACKLIST = ["open", "read", "exec", "{", "}", "\\", "globals", "BLACKLIST"]


def readuntil(sock, char):
    ret = b""
    while True:
        c = sock.recv(1)
        if char == c or not c:
            break
        ret += c
    return ret


class ThreadingTCPRequestHandler(BaseRequestHandler):
    """Custom class to handle incoming requests"""

    def loop(self):
        self.request.settimeout(20)
        self.request.sendall(b"\nYour expression: ")

        try:
            expression = readuntil(self.request, b"\n").decode()
        except TimeoutError:
            self.request.sendall(b"\n\nTimed out.\n\n")
            return

        for word in BLACKLIST:
            if word in expression:
                self.request.sendall(b"\nSome of your input is blacklisted.\n")
                self.loop()
                return

        try:
            answer = eval(expression)
            self.request.sendall(b"Answer: " + str(answer).encode() + b'\n\n')
            self.loop()
        except Exception as e:
            print(e)
            self.request.sendall(b"\nSorry, an error occurred.\n")
            self.loop()

    def handle(self):
        """Handle incoming request"""

        self.request.sendall(
            b"\n--- calculator V2 ---\nYou can insert some mathematical expressions here.\n"
        )

        self.loop()


if __name__ == "__main__":
    ThreadingTCPServer((HOST, PORT), ThreadingTCPRequestHandler).serve_forever()
