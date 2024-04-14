import string
from socketserver import BaseRequestHandler, ThreadingTCPServer
from random import randint

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


def remove(got: str) -> str:
    blacklist = [".", ",", " "] + list(string.ascii_letters)

    for char in blacklist:
        got = got.replace(char, "")

    got = got.lstrip("0")  # Remove zeros at the beginning

    return got


class ThreadingTCPRequestHandler(BaseRequestHandler):
    """Custom class to handle incoming requests"""

    def generate(self) -> bool | None:
        number = randint(10, 1000000)
        self.request.settimeout(1)
        self.request.sendall(b"Number: " + str(number).encode() + b"\n")

        try:
            answer = readuntil(self.request, b"\n").decode()
            answer = remove(answer)

            org_len = len(str(number))
            new_len = len(str(answer))
            if new_len > org_len and int(answer) == number:
                return True

            return False

        except ValueError:
            return False
        except TimeoutError:
            self.request.sendall(b"\nToo slow.\n")
            return None

    def handle(self):
        """Handle incoming request"""

        self.request.sendall(
            b"Give me 5 integers, that are equal, but longer:\n"
        )

        for _ in range(5):
            out = self.generate()
            if out is None:  # if answer was too slow
                return
            if not out:
                self.request.sendall(b"Wrong answer.\n")
                return

        with open("flag.txt", "rb") as f:
            flag = f.read()

        self.request.sendall(b"Congratulations, here is the flag: " + flag)


if __name__ == "__main__":
    ThreadingTCPServer((HOST, PORT), ThreadingTCPRequestHandler).serve_forever()
