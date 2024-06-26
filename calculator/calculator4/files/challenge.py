import math
from socketserver import BaseRequestHandler, ThreadingTCPServer

HOST = "0.0.0.0"
PORT = 6004


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
        self.request.sendall(b"Your expression:")

        try:
            expression = readuntil(self.request, b"\n").decode()
        except TimeoutError:
            self.request.sendall(b"\n\nTimed out.\n\n")
            return

        try:
            answer = eval(expression, {"__builtins__": None, "math": math})
            self.request.sendall(b"Answer: " + str(answer).encode() + b'\n\n')
            self.loop()
        except Exception as e:
            print(e)
            self.request.sendall(b"\nSorry, an error occurred.\n\n")

    def handle(self):
        """Handle incoming request"""

        self.request.sendall(
            b"\n--- calculator V4 ---\nYou can insert some mathematical expressions here.\n\n"
        )

        self.loop()


if __name__ == "__main__":
    ThreadingTCPServer((HOST, PORT), ThreadingTCPRequestHandler).serve_forever()

